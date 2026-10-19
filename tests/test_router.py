"""Navigation, About page and camera behaviour."""
from pathlib import Path

from streamlit.testing.v1 import AppTest

ROOT = Path(__file__).resolve().parent.parent
ROUTER = str(ROOT / "app.py")
VIEWS = {"views/guide.py": "How to Use KrushiNudi", "views/borewell.py": "Borewell Water Advisory",
         "views/weed_nutrient.py": "Weed & Nutrient Advisor",
         "views/crop_doctor.py": "Crop Doctor", "views/spray_prescription.py": "Smart Spray Prescription",
         "views/season_planner.py": "Season planner", "views/weather.py": "Weather precautions",
         "views/schemes.py": "Schemes and help", "views/about.py": "About and privacy"}


def element_types(node, found=None):
    found = set() if found is None else found
    for child in getattr(node, "children", {}).values():
        found.add(child.type)
        element_types(child, found)
    return found


def test_router_opens_every_page_with_its_own_heading():
    for view, title in VIEWS.items():
        at = AppTest.from_file(str(ROOT / view), default_timeout=30).run()
        assert not at.exception, view
        text = " ".join(m.value for m in at.markdown)
        assert (title in text or title.replace("&", "&amp;") in text), view


def test_home_page_has_landing_cards_and_the_advisor():
    at = AppTest.from_file(ROUTER, default_timeout=40).run()
    assert not at.exception
    text = " ".join(m.value for m in at.markdown)
    assert "Beta" in text and "crops in the advisor" in text and "Crop Doctor" in text
    assert len(at.slider) == 7


def test_about_page_is_honest_about_privacy_and_limits():
    at = AppTest.from_file(ROUTER, default_timeout=40).run().switch_page("views/about.py").run()
    text = " ".join(m.value for m in at.markdown)
    assert "does **not store**" in text and "Gemini" in text and "not yet been reviewed" in text
    assert "gives no pesticide or fertilizer doses" in text


def test_camera_opens_only_when_the_person_chooses_it():
    at = AppTest.from_file(str(ROOT / "views" / "crop_doctor.py"), default_timeout=30).run()
    assert "camera_input" not in element_types(at.main)        # no camera request on page load
    assert "file_uploader" in element_types(at.main)
    at.radio[0].set_value("Use this device's webcam").run()
    assert "camera_input" in element_types(at.main)
    at.radio[0].set_value("Upload or take a photo with my phone").run()
    assert "camera_input" not in element_types(at.main)
