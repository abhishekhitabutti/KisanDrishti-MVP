"""About, data sources, limits, privacy and credits."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import streamlit as st  # noqa: E402

import diagnosis  # noqa: E402
import ui  # noqa: E402

APP_VERSION = "0.7 (beta), October 2026"

ui.hero("About and privacy", "What this app is, where its advice comes from, what it cannot do, and how your data is handled.", "ℹ️")

st.subheader("What KisanDrishti is")
st.write("A free advisory app for Karnataka farmers, built by Abhishek Hitabutti, a B.Tech CSE (AI & ML) student at Amity University "
         "Bengaluru. It is not a government service. It has no advertising and no accounts.")
st.caption(f"Version {APP_VERSION}")

st.subheader("Where the advice comes from")
st.markdown(
    "- **Crop advisor:** a Random Forest model trained on a public crop recommendation dataset (22 crops).\n"
    "- **Crop Doctor:** an AI model only identifies the problem in your photo. The treatment guidance comes from a "
    f"library of {len(diagnosis.load_kb())} reviewed entries, each with its sources (ICAR, TNAU and university papers), and is shown only when the match is confident.\n"
    "- **Weather precautions:** forecasts from Open-Meteo. You can also enter an official IMD warning you heard on the government telecast.\n"
    "- **Schemes and help:** the government portals for each scheme, and public extension sources.\n"
    "- **Season planner:** extension and research sources, listed under each practice.")

st.subheader("Limits you should know")
st.markdown(
    "- The guidance has **not yet been reviewed by an agriculture expert**. Expert review is in progress.\n"
    "- The crop advisor knows 22 crops. Its dataset is described as built by augmenting rainfall, climate and fertilizer data, "
    "so it is **not field-collected data** and accuracy on real farms can be lower.\n"
    "- Crop Doctor knows a small number of problems. For anything else it tells you to see an expert.\n"
    "- Weather hazard thresholds are simple rules. Forecasts can be wrong.\n"
    "- The app **gives no pesticide or fertilizer doses**. Doses come from the product label, your Soil Health Card or your agriculture officer.\n"
    "- It cannot replace your agriculture officer, KVK or Raitha Samparka Kendra.")

st.subheader("Privacy")
st.markdown(
    "- There is no sign-up. This app does **not store** your photos or any personal details.\n"
    "- **Photos** are sent to Google's Gemini service for analysis. On Google's free tier, Google may use the content to improve its products. "
    "Location data is removed from the photo first. Please do not upload photos with people in them.\n"
    "- **Weather:** only the centre point of the district you pick is sent to the forecast service.\n"
    "- **Feedback:** if you email feedback, we receive your email address and message.\n"
    "- The hosting service may keep standard technical logs, as any website does.")

st.subheader("Credits")
st.markdown(
    "- Weather data by [Open-Meteo.com](https://open-meteo.com/).\n"
    "- Crop recommendation dataset: a public dataset (22 crops, 2,200 rows) widely shared on Kaggle. Check its terms before reusing it.\n"
    "- More crops: the [FAO EcoCrop database](https://gaez.fao.org/pages/ecocrop-search).\n"
    "- Guidance sources are listed inside each Crop Doctor entry and each Season Planner practice.\n"
    "- Source code: [github.com/abhishekhitabutti/KisanDrishti-MVP](https://github.com/abhishekhitabutti/KisanDrishti-MVP). All rights reserved.")

st.subheader("Contact")
st.markdown("Abhishek Hitabutti: [abhishekhitabutti@gmail.com](mailto:abhishekhitabutti@gmail.com). Corrections from farmers, agriculture officers and KVK staff are very welcome.")

ui.feedback_box()
st.markdown("---")
st.caption("© 2026 Abhishek Hitabutti. All rights reserved. Copying or reuse of this app without permission is prohibited.")
