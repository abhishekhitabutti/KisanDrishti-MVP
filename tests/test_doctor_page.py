from pathlib import Path

from streamlit.testing.v1 import AppTest

import diagnosis

ROOT = Path(__file__).resolve().parent.parent
PAGE = str(ROOT / "views" / "crop_doctor.py")


def make_result(**over):
    base = {"crop": "rice", "category": "disease", "kb_id": "rice_blast", "name": "Rice blast", "confidence": "high",
            "symptoms_seen": ["spindle-shaped grey spots"], "could_also_be": ["Brown spot"], "photo_quality": "good", "photo_tip": ""}
    base.update(over)
    return base


def run_with(result, monkeypatch, key="test-key", var="ANTHROPIC_API_KEY"):
    for name in ("GEMINI_API_KEY", "ANTHROPIC_API_KEY"):
        monkeypatch.delenv(name, raising=False)
    if key:
        monkeypatch.setenv(var, key)
    at = AppTest.from_file(PAGE, default_timeout=30)
    if result is not None:
        at.session_state["doctor"] = {"result": result, "district": "Mysuru"}
    return at.run()


def text_of(at):
    parts = [m.value for m in at.markdown] + [i.value for i in at.info] + [w.value for w in at.warning]
    parts += [s.value for s in at.success] + [e.label for e in at.expander]
    return " ".join(parts)


def test_page_loads_without_key_and_browse_tab_works(monkeypatch):
    at = run_with(None, monkeypatch, key=None)
    assert not at.exception
    assert len(at.tabs) == 2
    assert "not switched on" in text_of(at) or "not switched on" in " ".join(m.value for m in at.markdown)
    assert len(at.selectbox[2].options) >= 6  # browse list of problems


def test_confident_match_shows_guidance_and_spray_window(monkeypatch):
    at = run_with(make_result(), monkeypatch)
    assert not at.exception
    t = text_of(at)
    assert "Tricyclazole" in " ".join(str(d.value) for d in at.tabs[0].dataframe)
    assert "Best day to spray" in t and "Precautions and safety" in t and "No dose" not in t
    assert "Confirm with your KVK" not in t  # high confidence needs no extra warning


def test_medium_confidence_asks_for_confirmation(monkeypatch):
    at = run_with(make_result(confidence="medium"), monkeypatch)
    assert "Confirm with your KVK" in " ".join(m.value for m in at.markdown)


def test_unknown_problem_gets_no_chemical_advice(monkeypatch):
    at = run_with(make_result(kb_id="none", name="Unknown leaf spot", confidence="low"), monkeypatch)
    t = " ".join(m.value for m in at.markdown)
    assert "cannot give spray advice" in t
    # the photo tab must show no product table; the browse tab is a separate, reviewed library
    assert not any("Active ingredient" in list(d.value.columns) for d in at.tabs[0].dataframe)


def test_blurry_photo_asks_for_retake(monkeypatch):
    at = run_with(make_result(category="unclear", photo_quality="poor", photo_tip="Move closer to the leaf."), monkeypatch)
    t = " ".join(m.value for m in at.markdown)
    assert "not clear enough" in t and "Move closer" in t


def test_healthy_plant_message(monkeypatch):
    at = run_with(make_result(category="healthy", kb_id="none", name="Healthy leaf"), monkeypatch)
    assert any("looks healthy" in s.value for s in at.success)


def captions(at):
    return " ".join(c.value for c in at.caption)


def test_free_gemini_key_is_preferred_and_privacy_note_is_honest(monkeypatch):
    at = run_with(make_result(), monkeypatch, var="GEMINI_API_KEY")
    assert not at.exception
    note = captions(at)
    assert "Google's Gemini" in note and "may use it to improve" in note and "Location data is removed" in note


def test_no_key_means_no_photo_is_sent_anywhere(monkeypatch):
    at = run_with(None, monkeypatch, key=None)
    assert "no photo is sent anywhere" in captions(at)


def test_provider_choice_prefers_gemini(monkeypatch):
    monkeypatch.setenv("GEMINI_API_KEY", "g")
    monkeypatch.setenv("ANTHROPIC_API_KEY", "a")
    at = AppTest.from_file(PAGE, default_timeout=30).run()
    assert "Google's Gemini" in captions(at)
