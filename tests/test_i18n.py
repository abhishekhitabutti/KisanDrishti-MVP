"""Kannada translation tests: the file is well formed and the pages use it without errors."""
import io
import json
import re
from pathlib import Path

import pytest
from streamlit.testing.v1 import AppTest

import diagnosis
import i18n
import planner_data

ROOT = Path(__file__).resolve().parent.parent
KN = json.loads((ROOT / "translations" / "kn.json").read_text(encoding="utf-8"))
KANNADA_CHAR = re.compile(r"[\u0c80-\u0cff]")
PLACEHOLDER = re.compile(r"\{(\w+)\}")
ROUTER = str(ROOT / "app.py")
HOME, WEATHER, SCHEMES = str(ROOT / "views" / "home.py"), "views/weather.py", "views/schemes.py"
ADVISOR = str(ROOT / "views" / "crop_advisor.py")
DOCTOR, PLANNER = str(ROOT / "views" / "crop_doctor.py"), str(ROOT / "views" / "season_planner.py")


def flatten(obj, out):
    if isinstance(obj, str):
        out.add(obj)
    elif isinstance(obj, dict):
        for v in obj.values():
            flatten(v, out)
    elif isinstance(obj, list):
        for v in obj:
            flatten(v, out)
    return out


# Content that is not translated yet (long guidance texts). Phase 2.
# Plus text that comes from the photo-analysis model, which is asked to answer in Kannada itself.
UNTRANSLATED_OK = (flatten(diagnosis.load_kb(), set()) | flatten(planner_data.ITEMS, set())
                   | {"Mysuru", "spots", "Brown spot", "Rice blast"})


def test_every_translation_is_kannada_and_keeps_its_placeholders():
    for key, value in KN.items():
        assert KANNADA_CHAR.search(value), key
        if key.startswith("crop:"):
            continue
        assert set(PLACEHOLDER.findall(key)) == set(PLACEHOLDER.findall(value)), key
        assert key.count("**") == value.count("**"), key


def test_all_22_crops_have_a_kannada_name():
    import pickle
    profiles = pickle.load(open(ROOT / "crop_profiles.pkl", "rb"))
    assert not [c for c in profiles if f"crop:{c}" not in KN]


def test_crop_label_always_keeps_the_english_name(monkeypatch):
    monkeypatch.setattr(i18n.st, "session_state", {"lang": "kn"})
    assert i18n.crop("rice") == "ಭತ್ತ (rice)"
    monkeypatch.setattr(i18n.st, "session_state", {"lang": "en"})
    assert i18n.crop("rice") == "rice"


def run_in_kannada(path, state=None, record=None):
    at = AppTest.from_file(path, default_timeout=60)
    at.session_state["lang"] = "kn"
    for k, v in (state or {}).items():
        at.session_state[k] = v
    return at.run()


def markdown_text(at):
    return " ".join(m.value for m in at.markdown)


def test_home_page_in_kannada(monkeypatch):
    at = run_in_kannada(HOME)
    assert not at.exception
    assert "ಕೃಷಿನುಡಿ" in markdown_text(at)


def test_crop_advisor_in_kannada(monkeypatch):
    at = run_in_kannada(ADVISOR)
    assert not at.exception
    assert "ಕೃಷಿನುಡಿ" in markdown_text(at)
    at.button[0].click().run()
    assert not at.exception
    assert any("ಅತ್ಯುತ್ತಮ ಹೊಂದಾಣಿಕೆ" in s.value for s in at.success)


def test_switching_with_the_radio_changes_language():
    at = AppTest.from_file(ROUTER, default_timeout=40).run()
    assert "KrushiNudi" in markdown_text(at)
    at.radio(key="lang_radio").set_value("ಕನ್ನಡ").run()
    assert "ಕೃಷಿನುಡಿ" in markdown_text(at) and not at.exception
    at.radio(key="lang_radio").set_value("English").run()
    assert "KrushiNudi" in markdown_text(at)


def test_crop_doctor_in_kannada_shows_safety_text_in_kannada():
    result = {"crop": "rice", "category": "disease", "kb_id": "rice_blast", "name": "Rice blast", "confidence": "high",
              "symptoms_seen": ["spots"], "could_also_be": [], "photo_quality": "good", "photo_tip": ""}
    at = run_in_kannada(DOCTOR, {"doctor": {"result": result, "district": "Mysuru"}})
    assert not at.exception
    text = markdown_text(at)
    assert "ಇದು ಹೇಗೆ ಕಾಣುತ್ತದೆ" in text                      # section heading
    assert "ಮೊದಲು ಲೇಬಲ್ ಪೂರ್ತಿ ಓದಿ" in text               # first safety rule, in Kannada
    assert "ಕೀಟನಾಶಕ ಮಾರ್ಗದರ್ಶನ" in " ".join(e.label for e in at.expander)


def test_planner_and_other_pages_in_kannada():
    at = run_in_kannada(PLANNER)
    assert not at.exception and "ಋತು ಯೋಜಕ" in markdown_text(at)
    for view in (WEATHER, SCHEMES, "views/about.py"):
        at = AppTest.from_file(ROUTER, default_timeout=40)
        at.session_state["lang"] = "kn"
        at.run().switch_page(view).run()
        assert not at.exception, view


@pytest.mark.parametrize("path,state", [
    (ROUTER, {}),
    (HOME, {}),
    (ADVISOR, {"advice": {"inputs": {"N": 60, "P": 50, "K": 50, "ph": 6.5, "temperature": 25.0, "humidity": 65.0, "rainfall": 100.0},
                          "top": [("rice", 0.9), ("jute", 0.1), ("maize", 0.0)]}}),
    (PLANNER, {}),
    (DOCTOR, {"doctor": {"result": {"crop": "rice", "category": "disease", "kb_id": "rice_blast", "name": "Rice blast",
                                    "confidence": "medium", "symptoms_seen": ["spots"], "could_also_be": ["Brown spot"],
                                    "photo_quality": "good", "photo_tip": ""}, "district": "Mysuru"}}),
])
def test_no_interface_text_is_missing_a_translation(monkeypatch, path, state):
    """Every interface string the page asks for must have a Kannada version, except the long guidance texts."""
    asked = set()
    original = i18n.t

    def spy(text, **kw):
        asked.add(text)
        return original(text, **kw)

    monkeypatch.setattr(i18n, "t", spy)
    run_in_kannada(path, state)
    missing = {s for s in asked if s not in KN and s not in UNTRANSLATED_OK and s.strip()}
    assert not missing, sorted(missing)[:10]


def test_kannada_request_goes_to_the_model(monkeypatch):
    import urllib.request
    from conftest import FakeResponse
    seen = {}

    def fake(req, timeout=0):
        seen["body"] = json.loads(req.data.decode())
        reply = {"candidates": [{"content": {"parts": [{"text": json.dumps({"crop": "rice", "category": "unclear"})}]}}]}
        return FakeResponse(json.dumps(reply).encode())

    monkeypatch.setattr(urllib.request, "urlopen", fake)
    from PIL import Image
    buf = io.BytesIO()
    Image.new("RGB", (60, 60), "green").save(buf, format="JPEG")
    diagnosis.analyze(buf.getvalue(), "k", diagnosis.load_kb(), provider="gemini", language="kn")
    assert "Kannada" in seen["body"]["contents"][0]["parts"][0]["text"]
    diagnosis.analyze(buf.getvalue(), "k", diagnosis.load_kb(), provider="gemini")
    assert "Kannada" not in seen["body"]["contents"][0]["parts"][0]["text"]
