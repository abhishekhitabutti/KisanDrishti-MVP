"""Tests for the Streamlit pages using Streamlit's AppTest (no browser needed)."""
import io
import json
import urllib.request
from pathlib import Path

import streamlit as st
from streamlit.testing.v1 import AppTest

ROOT = Path(__file__).resolve().parent.parent


class FakeResponse(io.BytesIO):
    def __enter__(self):
        return self

    def __exit__(self, *args):
        return False


def fake_forecast(rain, tmax, tmin, gust, humidity):
    days = [f"2026-10-{10 + i}" for i in range(7)]
    hourly_time = [f"{d}T{h:02d}:00" for d in days for h in range(24)]
    return {
        "daily": {"time": days, "temperature_2m_max": tmax, "temperature_2m_min": tmin,
                  "precipitation_sum": rain, "wind_gusts_10m_max": gust},
        "hourly": {"time": hourly_time, "relative_humidity_2m": [humidity] * len(hourly_time)},
    }


def run_weather(payload=None, fail=False, monkeypatch=None):
    def fake_urlopen(url, timeout=0):
        if fail:
            raise OSError("no network")
        return FakeResponse(json.dumps(payload).encode())

    monkeypatch.setattr(urllib.request, "urlopen", fake_urlopen)
    st.cache_data.clear()
    at = AppTest.from_file(str(ROOT / "views" / "weather.py"), default_timeout=30)
    return at.run()


def test_main_page_gives_top_three_crops():
    at = AppTest.from_file(str(ROOT / "views" / "home.py"), default_timeout=30).run()
    assert not at.exception
    at.button[0].click().run()
    assert not at.exception
    assert any("Best match" in s.value for s in at.success)
    assert len(at.selectbox[0].options) == 22


def test_weather_page_flags_storm(monkeypatch):
    payload = fake_forecast([80, 10, 0, 0, 0, 0, 0], [39] + [31] * 6, [24] + [22] * 6, [55] + [20] * 6, 88)
    at = run_weather(payload, monkeypatch=monkeypatch)
    assert not at.exception
    flagged = " ".join(w.value for w in at.warning)
    assert "Heavy rain" in flagged and "Strong wind" in flagged and "Heat" in flagged


def test_weather_page_flags_dry_week(monkeypatch):
    payload = fake_forecast([0] * 7, [30] * 7, [19] * 7, [15] * 7, 50)
    at = run_weather(payload, monkeypatch=monkeypatch)
    assert any("Dry week" in w.value for w in at.warning)


def test_weather_page_survives_no_network(monkeypatch):
    at = run_weather(fail=True, monkeypatch=monkeypatch)
    assert not at.exception
    assert any("Could not load" in e.value for e in at.error)


def test_schemes_page_checklist():
    at = AppTest.from_file(str(ROOT / "views" / "schemes.py"), default_timeout=30).run()
    assert not at.exception
    for box in at.checkbox:
        box.check()
    at.run()
    assert any("All documents ready" in s.value for s in at.success)


PAGES = [ROOT / "views" / "home.py", ROOT / "views" / "weather.py", ROOT / "views" / "schemes.py",
         ROOT / "views" / "crop_doctor.py", ROOT / "views" / "season_planner.py", ROOT / "views" / "about.py",
         ROOT / "views" / "guide.py", ROOT / "views" / "borewell.py", ROOT / "views" / "weed_nutrient.py"]


def all_markdown(at):
    return " ".join(m.value for m in at.markdown)


def test_every_page_has_a_feedback_link(monkeypatch):
    monkeypatch.delenv("FEEDBACK_URL", raising=False)
    for page in PAGES:
        at = AppTest.from_file(str(page), default_timeout=30).run()
        assert not at.exception, page
        assert "[Send feedback](mailto:" in all_markdown(at), page


def test_feedback_form_link_can_be_set_without_code_changes(monkeypatch):
    monkeypatch.setenv("FEEDBACK_URL", "https://forms.example.com/abc")
    at = AppTest.from_file(str(PAGES[0]), default_timeout=30).run()
    assert "[Send feedback](https://forms.example.com/abc)" in all_markdown(at)


def test_home_page_points_to_more_crops():
    at = AppTest.from_file(str(PAGES[0]), default_timeout=30).run()
    assert "gaez.fao.org/pages/ecocrop-search" in all_markdown(at)


def test_weed_nutrient_page_renders_cleanly():
    at = AppTest.from_file(str(ROOT / "views" / "weed_nutrient.py"), default_timeout=30).run()
    assert not at.exception
    text = all_markdown(at)
    assert "Weed & Nutrient Advisor" in text or "ಕಳೆ & ಸಾವಯವ ಪೋಷಕಾಂಶ" in text

