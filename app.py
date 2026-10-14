"""KisanDrishti entry point. Sets up the page, the language switch and the navigation menu."""
import streamlit as st

import i18n
import ui
from i18n import t

st.set_page_config(page_title="KisanDrishti", page_icon="🌾", initial_sidebar_state="expanded")
ui.inject_css()

pages = [
    st.Page("views/home.py", title=t("Crop advisor"), icon="🌾", default=True),
    st.Page("views/crop_doctor.py", title=t("Crop Doctor"), icon="🩺", url_path="doctor"),
    st.Page("views/season_planner.py", title=t("Season planner"), icon="🗓️", url_path="season"),
    st.Page("views/weather.py", title=t("Weather precautions"), icon="⛈️", url_path="weather"),
    st.Page("views/schemes.py", title=t("Schemes and help"), icon="📋", url_path="schemes"),
    st.Page("views/about.py", title=t("About and privacy"), icon="ℹ️", url_path="about"),
]
page = st.navigation(pages)
i18n.language_picker(translated=page.url_path not in i18n.UNTRANSLATED_PAGES)
page.run()
