"""Tests for KrushiNudi Intro Tour and Welcome Screen transition to the main application."""
from pathlib import Path
from streamlit.testing.v1 import AppTest

ROOT = Path(__file__).resolve().parent.parent
ROUTER = str(ROOT / "app.py")


def markdown_text(at):
    return " ".join(m.value for m in at.markdown)


def element_types(node, found=None):
    found = set() if found is None else found
    for child in getattr(node, "children", {}).values():
        found.add(child.type)
        element_types(child, found)
    return found


def test_intro_screen_renders_first_and_transitions_to_app():
    at = AppTest.from_file(ROUTER, default_timeout=50)
    at.session_state["intro_seen"] = False
    at.run()
    assert not at.exception

    # 1. Verify Intro Screen Elements
    text = markdown_text(at)
    assert "KrushiNudi" in text
    assert any(b.key == "btn_enter_app" for b in at.button)
    assert any(b.key == "btn_skip_intro" for b in at.button)
    assert "video" in element_types(at.main)

    # 2. Click "Enter Application"
    at.button(key="btn_enter_app").click().run()
    assert not at.exception
    assert at.session_state["intro_seen"] is True

    # 3. Verify Main Application Interface is now displayed
    main_text = markdown_text(at)
    assert "crops in the advisor" in main_text
    assert any(b.key == "btn_sidebar_intro" for b in at.button)


def test_intro_screen_language_switch():
    at = AppTest.from_file(ROUTER, default_timeout=50)
    at.session_state["intro_seen"] = False
    at.run()
    assert not at.exception

    # Switch to Kannada on Intro Screen
    at.button(key="top_bar_kn").click().run()
    assert not at.exception
    text_kn = markdown_text(at)
    assert "ಕೃಷಿನುಡಿ" in text_kn

    # Transition into the app - should remain in Kannada!
    at.button(key="btn_enter_app").click().run()
    assert not at.exception
    assert at.session_state["intro_seen"] is True
    assert at.session_state["lang"] == "kn"
    assert "ಕೃಷಿನುಡಿ" in markdown_text(at)
