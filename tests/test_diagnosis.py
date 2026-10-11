import base64
import io
import json
import urllib.error
import urllib.request

import pytest
from PIL import Image

import diagnosis
from conftest import FakeResponse

KB = diagnosis.load_kb()


def make_result(**over):
    base = {"crop": "rice", "category": "disease", "kb_id": "rice_blast", "name": "Rice blast", "confidence": "high",
            "symptoms_seen": ["spindle-shaped spots"], "could_also_be": [], "photo_quality": "good", "photo_tip": ""}
    base.update(over)
    return base


def test_prepare_image_shrinks_and_converts_to_jpeg():
    buf = io.BytesIO()
    Image.new("RGBA", (3000, 2000), (10, 200, 10, 255)).save(buf, format="PNG")
    b64, media = diagnosis.prepare_image(buf.getvalue())
    img = Image.open(io.BytesIO(base64.b64decode(b64)))
    assert media == "image/jpeg" and img.format == "JPEG"
    assert max(img.size) <= 1568


def test_prepare_image_rejects_non_images():
    with pytest.raises(diagnosis.AnalysisError):
        diagnosis.prepare_image(b"this is not an image")


def test_parse_result_reads_fenced_json():
    text = 'Here you go:\n```json\n{"crop": "Rice", "category": "disease", "kb_id": "rice_blast", "name": "Rice blast", "confidence": "high"}\n```'
    r = diagnosis.parse_result(text, KB)
    assert r["crop"] == "rice" and r["kb_id"] == "rice_blast" and r["confidence"] == "high"


def test_parse_result_coerces_bad_values_to_safe_ones():
    r = diagnosis.parse_result('{"category": "banana", "confidence": "sure", "kb_id": "made_up", "photo_quality": "great"}', KB)
    assert r["category"] == "unclear" and r["confidence"] == "low" and r["kb_id"] == "none"


def test_parse_result_rejects_text_without_json():
    with pytest.raises(diagnosis.AnalysisError):
        diagnosis.parse_result("I think it is blast.", KB)


@pytest.mark.parametrize("over,mode", [
    ({"photo_quality": "poor"}, "retake"),
    ({"category": "unclear"}, "retake"),
    ({"category": "healthy", "kb_id": "none"}, "healthy"),
    ({"category": "nutrient_deficiency", "kb_id": "none"}, "non_pesticide"),
    ({"kb_id": "none"}, "expert_only"),
    ({"confidence": "low"}, "expert_only"),
    ({"crop": "tomato"}, "expert_only"),
    ({"category": "pest"}, "expert_only"),
    ({}, "guided"),
])
def test_decide_never_shows_chemicals_without_a_confident_reviewed_match(over, mode):
    assert diagnosis.decide(make_result(**over), KB)["mode"] == mode


def test_decide_flags_medium_confidence_for_confirmation():
    d = diagnosis.decide(make_result(confidence="medium"), KB)
    assert d["mode"] == "guided" and d["confirm"] is True


def test_weed_matches_any_crop():
    d = diagnosis.decide(make_result(crop="maize", category="weed", kb_id="parthenium"), KB)
    assert d["mode"] == "guided"


def test_analyze_anthropic_sends_image_and_parses_reply(monkeypatch):
    seen = {}

    def fake_urlopen(req, timeout=0):
        seen["headers"] = dict(req.header_items())
        seen["body"] = json.loads(req.data.decode())
        reply = {"content": [{"type": "text", "text": json.dumps({
            "crop": "rice", "category": "disease", "kb_id": "rice_blast", "name": "Rice blast", "confidence": "medium"})}]}
        return FakeResponse(json.dumps(reply).encode())

    monkeypatch.setattr(urllib.request, "urlopen", fake_urlopen)
    buf = io.BytesIO()
    Image.new("RGB", (200, 200), "green").save(buf, format="JPEG")
    r = diagnosis.analyze(buf.getvalue(), "test-key", KB, provider="anthropic", crop_hint="Rice (paddy)")
    assert r["kb_id"] == "rice_blast"
    assert seen["headers"]["X-api-key"] == "test-key"
    content = seen["body"]["messages"][0]["content"]
    assert content[0]["type"] == "image" and "Rice (paddy)" in content[1]["text"]
    assert "Do not give treatment" in seen["body"]["system"]


def test_analyze_gemini_sends_key_in_header_and_parses_reply(monkeypatch):
    seen = {}

    def fake_urlopen(req, timeout=0):
        seen["url"] = req.full_url
        seen["headers"] = {k.lower(): v for k, v in req.header_items()}
        seen["body"] = json.loads(req.data.decode())
        reply = {"candidates": [{"content": {"parts": [{"text": json.dumps({
            "crop": "tomato", "category": "disease", "kb_id": "tomato_early_blight", "name": "Early blight",
            "confidence": "high", "symptoms_seen": ["target-like rings"]})}]}}]}
        return FakeResponse(json.dumps(reply).encode())

    monkeypatch.setattr(urllib.request, "urlopen", fake_urlopen)
    buf = io.BytesIO()
    Image.new("RGB", (200, 200), "green").save(buf, format="JPEG")
    r = diagnosis.analyze(buf.getvalue(), "free-key", KB, provider="gemini", model="gemini-test", crop_hint="Tomato")
    assert r["kb_id"] == "tomato_early_blight" and r["confidence"] == "high"
    assert "gemini-test:generateContent" in seen["url"]
    assert "free-key" not in seen["url"]  # the key travels in a header, not in the URL
    assert seen["headers"]["x-goog-api-key"] == "free-key"
    parts = seen["body"]["contents"][0]["parts"]
    assert "inline_data" in parts[1] and "Tomato" in parts[0]["text"]
    assert seen["body"]["generationConfig"]["responseMimeType"] == "application/json"
    assert "Do not give treatment" in seen["body"]["system_instruction"]["parts"][0]["text"]


def test_gemini_reply_with_no_candidates_is_handled(monkeypatch):
    monkeypatch.setattr(urllib.request, "urlopen", lambda req, timeout=0: FakeResponse(json.dumps({"promptFeedback": {}}).encode()))
    buf = io.BytesIO()
    Image.new("RGB", (50, 50), "green").save(buf, format="JPEG")
    with pytest.raises(diagnosis.AnalysisError):
        diagnosis.analyze(buf.getvalue(), "k", KB, provider="gemini")


def test_unknown_provider_is_rejected():
    buf = io.BytesIO()
    Image.new("RGB", (50, 50), "green").save(buf, format="JPEG")
    with pytest.raises(diagnosis.AnalysisError):
        diagnosis.analyze(buf.getvalue(), "k", KB, provider="nope")


def test_photo_location_data_is_removed():
    exif = Image.Exif()
    exif[0x010F] = "TestPhone"      # camera make
    exif[0x8825] = {1: "N", 2: (12.0, 58.0, 0.0)}  # GPS block
    buf = io.BytesIO()
    Image.new("RGB", (300, 300), "green").save(buf, format="JPEG", exif=exif)
    assert len(Image.open(io.BytesIO(buf.getvalue())).getexif()) > 0   # the original has metadata
    b64, _ = diagnosis.prepare_image(buf.getvalue())
    cleaned = Image.open(io.BytesIO(base64.b64decode(b64)))
    assert len(cleaned.getexif()) == 0


@pytest.mark.parametrize("provider", ["anthropic", "gemini"])
@pytest.mark.parametrize("code", [401, 404, 429, 500])
def test_analyze_turns_http_errors_into_friendly_messages(monkeypatch, code, provider):
    def fake_urlopen(req, timeout=0):
        raise urllib.error.HTTPError("u", code, "err", {}, None)
    monkeypatch.setattr(urllib.request, "urlopen", fake_urlopen)
    buf = io.BytesIO()
    Image.new("RGB", (50, 50), "green").save(buf, format="JPEG")
    with pytest.raises(diagnosis.AnalysisError) as exc:
        diagnosis.analyze(buf.getvalue(), "k", KB, provider=provider)
    assert "Traceback" not in str(exc.value) and len(str(exc.value)) > 10
