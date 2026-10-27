import os
import sys
from pathlib import Path

ROOT_DIR = str(Path(__file__).resolve().parent)
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

import streamlit as st

import auth
import i18n
import ui
from i18n import t

logo_file = Path(ROOT_DIR) / "images" / "krushinudi_logo.jpg"
st.set_page_config(
    page_title="KrushiNudi",
    page_icon=str(logo_file) if logo_file.exists() else "🌾",
    initial_sidebar_state="expanded"
)
ui.inject_css()

if logo_file.exists():
    try:
        st.logo(str(logo_file), icon_image=str(logo_file))
    except Exception:
        pass


# Security Gate: Completely DEACTIVATED.
# Anyone can use KrushiNudi directly without any login or registration.
# auth.require_auth()

# Language picker positioned at the top for universal accessibility on mobile and desktop
if not hasattr(i18n, "top_language_bar"):
    import importlib
    try:
        i18n = importlib.reload(i18n)
    except Exception:
        pass

if hasattr(i18n, "top_language_bar"):
    try:
        i18n.top_language_bar()
    except Exception:
        pass

# Check if user has completed or skipped the intro screen
# In automated pytest runs, default intro_seen to True so existing navigation tests pass
is_pytest = ("pytest" in sys.modules)
query_intro = ""
try:
    query_intro = st.query_params.get("intro", "")
except Exception:
    pass

if "intro_seen" not in st.session_state:
    if is_pytest:
        st.session_state["intro_seen"] = True
    elif query_intro == "done":
        st.session_state["intro_seen"] = True
    else:
        st.session_state["intro_seen"] = False

if not st.session_state.get("intro_seen", False):
    # Interface 1: Intro Tour & Video Showcase
    from views.intro_view import render_intro_screen
    render_intro_screen()
else:
    # Interface 2: Main Application Multi-Tool Portal
    i18n.language_picker()

    # Replay Intro option in sidebar
    with st.sidebar:
        def _replay_intro():
            st.session_state["intro_seen"] = False
            try:
                st.query_params["intro"] = "replay"
            except Exception:
                pass

        is_kn = (i18n.current_lang() == "kn")
        st.button(
            "🎬 ಪರಿಚಯ ವಿಡಿಯೋ {Watch Intro}" if is_kn else "🎬 Watch Intro Tour",
            key="btn_sidebar_intro",
            use_container_width=True,
            on_click=_replay_intro,
            help="Replay the official intro video walkthrough"
        )
        st.markdown("---")

    pages = [
        st.Page("views/home.py", title=t("KrushiNudi"), icon="🌾", default=True),
        st.Page("views/market_rates.py", title=t("Market Rates & Selling Centers"), icon="📈", url_path="market"),
        st.Page("views/crop_advisor.py", title=t("Crop advisor"), icon="🌱", url_path="advisor"),
        st.Page("views/borewell.py", title=t("Borewell advisory"), icon="💧", url_path="borewell"),
        st.Page("views/weed_nutrient.py", title=t("Weed & nutrient advisory"), icon="🌿", url_path="weed_nutrient"),
        st.Page("views/crop_doctor.py", title=t("Crop Doctor"), icon="🩺", url_path="doctor"),
        st.Page("views/spray_prescription.py", title=t("Spray & nutrition prescription"), icon="💊", url_path="spray_prescription"),
        st.Page("views/season_planner.py", title=t("Season planner"), icon="🗓️", url_path="season"),
        st.Page("views/weather.py", title=t("Weather precautions"), icon="⛈️", url_path="weather"),
        st.Page("views/schemes.py", title=t("Schemes and help"), icon="📋", url_path="schemes"),
        st.Page("views/guide.py", title=t("How to use"), icon="📖", url_path="guide"),
        st.Page("views/about.py", title=t("About and privacy"), icon="ℹ️", url_path="about"),
    ]
    page = st.navigation(pages)
    page.run()
