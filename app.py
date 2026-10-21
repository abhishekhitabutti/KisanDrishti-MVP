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

st.set_page_config(page_title="KrushiNudi", page_icon="🌾", initial_sidebar_state="expanded")
ui.inject_css()


# Security Gate: Completely DEACTIVATED.
# Anyone can use KrushiNudi directly without any login or registration.
# To re-activate later after building the project, uncomment the line below:
# auth.require_auth()

pages = [
    st.Page("views/home.py", title=t("Crop advisor"), icon="🌾", default=True),
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
i18n.language_picker(translated=page.url_path not in i18n.UNTRANSLATED_PAGES)
page.run()
