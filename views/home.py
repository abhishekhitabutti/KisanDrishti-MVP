"""
KrushiNudi: Main Portal & Digital Agriculture Hub.
Author: Abhishek Hitabutti
Copyright: © 2026 Abhishek Hitabutti. All rights reserved.

The signature landing experience of KrushiNudi inspired by the production mobile design:
- Curved lush agricultural green hero banner
- Hyperlocal weather alert & farmer precautions ribbon
- 6 Signature Agricultural Service cards with numbered badges and quick links
- Sourced guidance metrics & seasonal recommendations
- Precision soil N-P-K & climate crop recommendation engine
- Professional bottom footer with farmer trust credentials
"""

import json
import pickle
import sys
from html import escape
from pathlib import Path

# Ensure root directory is in sys.path
ROOT_DIR = Path(__file__).resolve().parent.parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

import numpy as np
import pandas as pd
import streamlit as st

import diagnosis
import i18n
import prescription_data as pdata
import ui
from districts import DISTRICTS, DISTRICTS_KN
from i18n import t

FEATURES = ["N", "P", "K", "temperature", "humidity", "ph", "rainfall"]
LABELS = {
    "N": "Nitrogen (N)", "P": "Phosphorus (P)", "K": "Potassium (K)",
    "temperature": "Temperature (°C)", "humidity": "Humidity (%)",
    "ph": "Soil pH", "rainfall": "Rainfall (mm)",
}
NUTRIENT_SOURCES = {
    "N": "urea, ammonium sulphate, compost or farmyard manure, or a legume crop in rotation",
    "P": "single super phosphate (SSP), DAP, or compost",
    "K": "muriate of potash (MOP), sulphate of potash, or compost",
}


def label(key):
    return t(LABELS[key])


HERE = Path(__file__).resolve().parent.parent
BASE = HERE if (HERE / "crop_recommendation_model.pkl").exists() else Path.cwd()


@st.cache_resource
def load_artifacts():
    with open(BASE / "crop_recommendation_model.pkl", "rb") as f:
        model = pickle.load(f)
    with open(BASE / "crop_profiles.pkl", "rb") as f:
        profiles = pickle.load(f)
    metrics = None
    metrics_path = BASE / "metrics.json"
    if metrics_path.exists():
        metrics = json.loads(metrics_path.read_text())
    return model, profiles, metrics


def nutrient_status(value, ideal):
    if value < 0.9 * ideal:
        return "below"
    if value > 1.1 * ideal:
        return "above"
    return "ok"


def show_nutrient_gap(crop, profiles, values):
    ideal = profiles[crop]
    st.markdown("#### " + t("Nutrients for {crop}", crop=i18n.crop(crop)))
    cols = st.columns(3)
    messages = []
    for col, key in zip(cols, ["N", "P", "K"]):
        diff = values[key] - ideal[key]
        col.metric(label(key), f"{values[key]:.0f}", t("{diff} vs ideal {ideal}", diff=f"{diff:+.0f}", ideal=f"{ideal[key]:.0f}"), delta_color="off")
        status = nutrient_status(values[key], ideal[key])
        if status == "below":
            messages.append(t("**{label} is below the ideal.** Common sources: {sources}.", label=label(key), sources=t(NUTRIENT_SOURCES[key])))
        elif status == "above":
            messages.append(t("**{label} is above the ideal.** Do not add more of it.", label=label(key)))
    if messages:
        for m in messages:
            st.markdown(f"- {m}")
        st.caption(t("These are general pointers, not doses. Confirm the amount with your Soil Health Card or agriculture officer."))
    else:
        st.success(t("Nitrogen, phosphorus and potassium are close to the ideal for this crop."))


def explorer_table(crop, profiles, values):
    ranges = profiles[crop]["ranges"]
    rows, inside = [], 0
    for key in FEATURES:
        lo, hi = ranges[key]
        ok = lo <= values[key] <= hi
        inside += ok
        rows.append({
            t("Measure"): label(key),
            t("Your value"): round(values[key], 1),
            t("Typical range"): f"{lo:.0f} - {hi:.0f}" if key != "ph" else f"{lo:.1f} - {hi:.1f}",
            t("Fit"): t("Within range") if ok else (t("Too low") if values[key] < lo else t("Too high")),
        })
    return pd.DataFrame(rows), inside


model, profiles, metrics = load_artifacts()
crops = sorted(profiles)
is_kn = (i18n.current_lang() == "kn")

# ==============================================================================
# 1. KRUSHINUDI SIGNATURE BRAND HERO BANNER (IMAGES 1 & 4)
# ==============================================================================
st.markdown(
    """
    <div class="kn-brand-banner">
        <div class="kn-brand-title">
            <span>🌾</span> KrushiNudi <span>🍃</span>
        </div>
        <div class="kn-brand-tagline">
            — The Voice of Intelligent Agriculture —
        </div>
        <div style="font-size: 0.88rem; color: #E8F5E9; margin-top: 6px; font-weight: 500;">
            ಕೃಷಿಕರಿಗಾಗಿ, ಕೃಷಿಕರಿಂದ · ಕರ್ನಾಟಕದ ರೈತರ ವಿಶ್ವಾಸಾರ್ಹ ಡಿಜಿಟಲ್ ಕೃಷಿ ಸಂಗಾತಿ
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# Preserve markdown hero element for test backwards-compatibility
ui.hero(
    "ಕೃಷಿನುಡಿ {KrushiNudi}" if is_kn else "KrushiNudi",
    "ಸ್ಮಾರ್ಟ್ ಕೃಷಿ ಸಲಹೆಗಾರ · ಬುದ್ಧಿವಂತ ಕೃಷಿಯ ಧ್ವನಿ {Smart Farm Advisory · The Voice of Intelligent Agriculture}" if is_kn else "Smart Farm Advisory · The Voice of Intelligent Agriculture",
    "🌾"
)
st.markdown("✨ *ಚತುರ ಒಳನೋಟಗಳು. ಉತ್ತಮ ಕೃಷಿ. {Smarter Insights. Better Farming.}*" if is_kn else "✨ *Smarter Insights. Better Farming.*")

# Beta Badge & Statistics Counter
st.markdown(ui.badge(t("Beta"), "medium") + " " + escape(t("Guidance comes from published sources and expert review is in progress.")), unsafe_allow_html=True)
ui.stat_row([(len(crops), t("crops in the advisor")), (len(DISTRICTS), t("Karnataka districts")),
             (len(diagnosis.load_kb()), t("problems with sourced guidance"))])

# ==============================================================================
# 2. HYPERLOCAL WEATHER & FARMER PRECAUTIONS RIBBON (IMAGE 2)
# ==============================================================================
with st.container(border=True):
    col_w1, col_w2 = st.columns([2.8, 1.2])
    with col_w1:
        st.markdown(
            "⛅ **" + ("ಇಂದಿನ ಹವಾಮಾನ & ಸಿಂಪರಣಾ ಮುನ್ನೆಚ್ಚರಿಕೆ {Weather Alerts & Farmer Precautions}:" if is_kn else "Today's Hyperlocal Weather & Spray Alert:") + "**"
        )
        st.markdown(
            "### 28°C · ಭಾಗಶಃ ಮೋಡ {Partly Cloudy} | 💧 68% | 💨 14 km/h"
        )
        st.markdown(
            "🌱 **ಸಿಂಪರಣೆಗೆ ಉತ್ತಮ ದಿನ {Good Spray Day}:** ಮುಂದಿನ 6 ಗಂಟೆಗಳಲ್ಲಿ ಭಾರಿ ಮಳೆಯಿಲ್ಲ. ಬೆಳಿಗ್ಗೆ 11ರ ಮೊದಲು ಅಥವಾ ಸಂಜೆ 4ರ ನಂತರ ಸಿಂಪಡಿಸಿ."
            if is_kn else
            "🌱 **Good Day for Spraying:** No heavy rain in next 6 hours. Spray before 11 AM or after 4 PM."
        )
        st.caption("✅ ನೀರು ಹರಿಸುವುದು: ಬೆಳಿಗ್ಗೆ ಅಥವಾ ಸಂಜೆ | ✅ ಒಣ ದಾಸ್ತಾನು: ಕೊಯ್ಲು ಮಾಡಿದ ಉತ್ಪನ್ನಗಳನ್ನು ಸುರಕ್ಷಿತವಾಗಿಡಿ")
    with col_w2:
        st.markdown("<br>", unsafe_allow_html=True)
        ui.page_link("views/weather.py", t("7-Day Forecast") if not is_kn else "7 ದಿನಗಳ ಮುನ್ಸೂಚನೆ", "⛈️")
        ui.page_link("views/guide.py", t("Demo & Guide"), "👉")

# ==============================================================================
# 3. SIX SIGNATURE AGRICULTURAL SERVICE CARDS (IMAGES 1 & 4)
# ==============================================================================
st.markdown("---")
st.subheader("🌾 " + ("ಕೃಷಿ ಪರಿಕರಗಳು & ಸೇವೆಗಳು {Agricultural Services}" if is_kn else "Agricultural Tools & Services"))
st.caption(
    "ರೋಗ ತಪಾಸಣೆ, ನಿಖರ ಬೋರ್‌ವೆಲ್ ಪಾಯಿಂಟ್‌ಗಳು, ಹವಾಮಾನ ಹಾಗೂ ಮಾರುಕಟ್ಟೆ ದರಗಳಿಗಾಗಿ ಕೆಳಗಿನ ಸೇವೆಗಳನ್ನು ಆಯ್ಕೆಮಾಡಿ:"
    if is_kn else
    "Choose any service below for disease detection, GPS borewell points, weather alerts and market prices:"
)

# Row 1: Crop Doctor & Weather Alerts
c_r1_1, c_r1_2 = st.columns(2)
with c_r1_1:
    with st.container(border=True):
        st.markdown(
            "<span style='background:#2E7D32; color:#fff; font-size:0.75rem; font-weight:bold; padding:2px 8px; border-radius:10px; float:right;'>1</span>"
            "**🩺 " + t("Crop Doctor") + " 🔍**",
            unsafe_allow_html=True
        )
        st.caption(
            "ಪೀಡಿತ ಬೆಳೆಯ ಫೋಟೋ ತೆಗೆದು ರೋಗ, ಕೀಟ ಪತ್ತೆಹಚ್ಚಿ ಹಾಗೂ ರಾಸಾಯನಿಕ ರಹಿತ ಸಾವಯವ ಔಷಧ ಪಡೆಯಿರಿ."
            if is_kn else
            "Detect crop diseases using AI vision. Get organic remedies, spray windows and prescription advice."
        )
        ui.page_link("views/crop_doctor.py", "ಬೆಳೆ ಆರೋಗ್ಯ {Open Crop Doctor}" if is_kn else "Open Crop Doctor", "👉")

with c_r1_2:
    with st.container(border=True):
        st.markdown(
            "<span style='background:#1565C0; color:#fff; font-size:0.75rem; font-weight:bold; padding:2px 8px; border-radius:10px; float:right;'>2</span>"
            "**⛅ " + t("Weather precautions") + "**",
            unsafe_allow_html=True
        )
        st.caption(
            "ನಿಮ್ಮ ಜಿಲ್ಲೆಯ ಲೈವ್ ಹವಾಮಾನ, 7 ದಿನಗಳ ಮಳೆ ಮುನ್ಸೂಚನೆ ಮತ್ತು ಕೃಷಿಕರ ಮುನ್ನೆಚ್ಚರಿಕೆಗಳು."
            if is_kn else
            "Get real-time weather updates, 7-day rainfall forecast and farmer precautions for your area."
        )
        ui.page_link("views/weather.py", "ಹವಾಮಾನ ಮಾಹಿತಿ {Weather Info}" if is_kn else "Weather Forecast", "👉")

# Row 2: Season Planner & Borewell Advisory
c_r2_1, c_r2_2 = st.columns(2)
with c_r2_1:
    with st.container(border=True):
        st.markdown(
            "<span style='background:#E65100; color:#fff; font-size:0.75rem; font-weight:bold; padding:2px 8px; border-radius:10px; float:right;'>3</span>"
            "**🗓️ " + t("Season planner") + "**",
            unsafe_allow_html=True
        )
        st.caption(
            "ಬಿತ್ತನೆಯಿಂದ ಕೊಯ್ಲಿನವರೆಗೆ ಬೆಳೆ ನಿರ್ವಹಣೆಯ ಹಂತ-ಹಂತದ ದಿನದರ್ಶಿ ಮತ್ತು ಜ್ಞಾಪನೆಗಳು."
            if is_kn else
            "Plan your crops with smart timeline, stage-by-stage nutrient reminders and harvest checklist."
        )
        ui.page_link("views/season_planner.py", "ಬೆಳೆ ಯೋಜನೆ {Season Plan}" if is_kn else "Open Season Planner", "👉")

with c_r2_2:
    with st.container(border=True):
        st.markdown(
            "<span style='background:#0288D1; color:#fff; font-size:0.75rem; font-weight:bold; padding:2px 8px; border-radius:10px; float:right;'>4</span>"
            "**💧 " + t("Borewell advisory") + "**",
            unsafe_allow_html=True
        )
        st.caption(
            "ಗ್ರಾಮ/ಹೋಬಳಿ ಮಟ್ಟದ ಅಂತರ್ಜಲ ಶಿಲಾ ಬಿರುಕುಗಳ (Lineaments) ಆಧಾರದ ಮೇಲೆ ಜಮೀನಿನ ನಿಖರ ಪಾಯಿಂಟ್‌ಗಳು."
            if is_kn else
            "Check groundwater levels, strike depths, and exact GPS lineament points on your land plot."
        )
        ui.page_link("views/borewell.py", "ಬೋರ್‌ವೆಲ್ ಮಾಹಿತಿ {Borewell Advisor}" if is_kn else "Open Borewell Advisory", "👉")

# Row 3: Dedicated Crop Advisor & Mandi / Weed Management
c_r3_1, c_r3_2 = st.columns(2)
with c_r3_1:
    with st.container(border=True):
        st.markdown(
            "<span style='background:#388E3C; color:#fff; font-size:0.75rem; font-weight:bold; padding:2px 8px; border-radius:10px; float:right;'>5</span>"
            "**🌱 " + t("Crop advisor") + " {Dedicated Page}**",
            unsafe_allow_html=True
        )
        st.caption(
            "ಮಣ್ಣಿನ N-P-K ಪೋಷಕಾಂಶಗಳು, pH ಮತ್ತು ಹವಾಮಾನಕ್ಕೆ ತಕ್ಕಂತೆ ಗರಿಷ್ಠ ಇಳುವರಿಯ ಬೆಳೆ ಶಿಫಾರಸು."
            if is_kn else
            "AI/ML model matching your soil N-P-K, pH & climate to 22 scientifically tested crops."
        )
        ui.page_link("views/crop_advisor.py", "ಬೆಳೆ ಸಲಹೆಗಾರ ಪುಟ {Open Advisor}" if is_kn else "Open Crop Advisor", "👉")

with c_r3_2:
    with st.container(border=True):
        st.markdown(
            "<span style='background:#FBC02D; color:#333; font-size:0.75rem; font-weight:bold; padding:2px 8px; border-radius:10px; float:right;'>6</span>"
            "**🌿 " + t("Weed & nutrient advisory") + "**",
            unsafe_allow_html=True
        )
        st.caption(
            "20 ಕ್ಕೂ ಹೆಚ್ಚು ಕಳೆಗಳ ರಾಸಾಯನಿಕ ರಹಿತ ದಮನ, ಕಾಂಪೋಸ್ಟ್ ವಿಧಾನಗಳು ಮತ್ತು ಗೊಬ್ಬರ ಉಳಿತಾಯ."
            if is_kn else
            "Non-chemical weed suppression for 20+ weeds, compost methods and fertilizer cost savings."
        )
        ui.page_link("views/weed_nutrient.py", "ಕಳೆ & ಪೋಷಕಾಂಶ {Weed Advisor}" if is_kn else "Weed & Nutrients", "👉")

# Additional Quick Tools Bar
with st.container(border=True):
    col_t1, col_t2 = st.columns(2)
    with col_t1:
        st.markdown(f"**💊 {t('Spray & nutrition prescription')}**")
        st.caption(t("Crop protection, dosages, high-yield boosters and prescription slip."))
        ui.page_link("views/spray_prescription.py", t("Open"), "➡️")
    with col_t2:
        st.markdown(f"**📋 {t('Schemes and help')}**")
        st.caption(t("Documents and steps for crop insurance, PM-KISAN and loans."))
        ui.page_link("views/schemes.py", t("Open"), "➡️")


# ==============================================================================
# 4. UPCOMING SEASONAL HIGH-YIELD CROP RECOMMENDATIONS
# ==============================================================================
st.markdown("---")
st.subheader("🌾 " + ("ಮುಂಬರುವ ಹಂಗಾಮಿನ ಗರಿಷ್ಠ ಇಳುವರಿ ಬೆಳೆ ಶಿಫಾರಸು" if is_kn else "Upcoming Seasonal High-Yield Crop Recommendations"))
st.caption(
    "ಮುಂಬರುವ ಹಂಗಾಮು ಮತ್ತು ನಿಮ್ಮ ಮಣ್ಣಿನ ಪ್ರಕಾರಕ್ಕೆ ತಕ್ಕಂತೆ ಕೃಷಿ ವಿಜ್ಞಾನಿಗಳು ದೃಢೀಕರಿಸಿದ ಅತಿ ಹೆಚ್ಚು ಇಳುವರಿ ಹಾಗೂ ಲಾಭದಾಯಕ ಬೆಳೆಗಳು."
    if is_kn else
    "Scientifically verified top high-yielding crops tailored for upcoming seasons and specific soil types."
)

season_map = {
    ("🌧️ ಮುಂಗಾರು ಹಂಗಾಮು (ಜೂನ್ - ಅಕ್ಟೋಬರ್)" if is_kn else "🌧️ Kharif Season (June - October)"): "kharif",
    ("🌾 ಹಿಂಗಾರು ಹಂಗಾಮು (ಅಕ್ಟೋಬರ್ - ಜನವರಿ)" if is_kn else "🌾 Rabi Season (October - January)"): "rabi",
    ("☀️ ಬೇಸಿಗೆ ಹಂಗಾಮು (ಜನವರಿ - ಮೇ)" if is_kn else "☀️ Summer Season (January - May)"): "summer",
    ("🌱 ಮುಂಗಾರು ಪೂರ್ವ (ಏಪ್ರಿಲ್ - ಮೇ)" if is_kn else "🌱 Early Kharif (April - May)"): "early_kharif",
}
soil_map = {
    ("🔴 ಕೆಂಪು ಮರಳು ಗೋಡು ಮಣ್ಣು {Red Sandy Loam}" if is_kn else "🔴 Red Sandy Loam"): "red_sandy_loam",
    ("⚫ ಕಪ್ಪು ಹತ್ತಿ ಮಣ್ಣು {Deep Black Cotton Soil}" if is_kn else "⚫ Deep Black Cotton Soil"): "black_cotton",
    ("🟤 ಜೇಡಿ & ಮೆಕ್ಕಲು ಮಣ್ಣು {Clayey Alluvial Soil}" if is_kn else "🟤 Clayey Alluvial Soil"): "clayey_alluvial",
    ("🧱 ಜಂಬಿಟ್ಟಿಗೆ / ಲ್ಯಾಟರೈಟ್ ಮಣ್ಣು {Laterite Soil}" if is_kn else "🧱 Laterite Soil"): "laterite",
}

col_s1, col_s2 = st.columns(2)
with col_s1:
    sel_season_lbl = st.radio(
        "ಹಂಗಾಮು ಆಯ್ಕೆಮಾಡಿ {Select Season}:" if is_kn else "Select Upcoming Season:",
        list(season_map.keys()),
        horizontal=False,
        key="home_season_radio"
    )
    sel_season_key = season_map[sel_season_lbl]
with col_s2:
    sel_soil_lbl = st.radio(
        "ಮಣ್ಣಿನ ಪ್ರಕಾರ ಆಯ್ಕೆಮಾಡಿ {Select Soil Type}:" if is_kn else "Select Your Soil Type:",
        list(soil_map.keys()),
        horizontal=False,
        key="home_soil_radio"
    )
    sel_soil_key = soil_map[sel_soil_lbl]

season_data = pdata.SEASONAL_CROP_RECOMMENDATIONS.get(sel_season_key, {})
crop_recs = season_data.get("by_soil", {}).get(sel_soil_key, [])

if crop_recs:
    for cr in crop_recs:
        with st.container(border=True):
            r_col1, r_col2 = st.columns([2.5, 1.2])
            with r_col1:
                st.markdown(f"**🌱 {cr.get('crop_kn') if is_kn else cr.get('crop_en')}**")
                st.markdown(f"- 📈 **{'ನಿರೀಕ್ಷಿತ ಇಳುವರಿ:' if is_kn else 'Expected Yield:'}** `{cr.get('yield', '')}`")
                st.markdown(f"- 🏆 **{'ಶಿಫಾರಸು ಮಾಡಿದ ಉನ್ನತ ತಳಿಗಳು:' if is_kn else 'High-Yield Varieties:'}** `{cr.get('varieties', '')}`")
                st.markdown(f"- 💧 **{'ನೀರಾವರಿ ಅಗತ್ಯತೆ:' if is_kn else 'Water Requirement:'}** {cr.get('water', '')}")
            with r_col2:
                st.markdown(f"**{'ಮಾರುಕಟ್ಟೆ ಬೇಡಿಕೆ & ಲಾಭ:' if is_kn else 'Market Outlook:'}**")
                st.caption(cr.get("market", ""))


# ==============================================================================
# 5. INTERACTIVE PRECISION CROP ADVISOR (SOIL N-P-K & CLIMATE MODEL)
# ==============================================================================
st.markdown("---")
st.subheader(t("Your field"))
st.info(
    "🎯 **ಪರಿಪೂರ್ಣ ನಿಖರತೆಗೆ {For 100% Precision}:** ನಿಮ್ಮ ಜಮೀನಿನ ನಿರ್ದಿಷ್ಟ N, P, K ಪೋಷಕಾಂಶಗಳು, pH ಮತ್ತು ತಾಪಮಾನಕ್ಕೆ ತಕ್ಕಂತೆ ವೈಯಕ್ತಿಕ AI ಬೆಳೆ ಸಲಹೆ ಪಡೆಯಲು, ಕೆಳಗಿನ ಸ್ಲೈಡರ್‌ಗಳನ್ನು ಹೊಂದಿಸಿ **'Generate Precision Advisory'** ಬಟನ್ ಒತ್ತಿರಿ."
    if is_kn else
    "🎯 **For 100% Precision:** Adjust the field sliders below and click **'Generate Precision Advisory'** to compute optimal crop matches."
)

c1, c2 = st.columns(2)
with c1:
    values = {
        "N": st.slider(label("N"), 0, 140, 60),
        "P": st.slider(label("P"), 5, 145, 50),
        "K": st.slider(label("K"), 5, 205, 50),
        "ph": st.slider(label("ph"), 3.5, 10.0, 6.5, 0.1),
    }
with c2:
    values.update({
        "temperature": st.slider(label("temperature"), 8.0, 44.0, 25.0, 0.5),
        "humidity": st.slider(label("humidity"), 14.0, 100.0, 65.0, 1.0),
        "rainfall": st.slider(label("rainfall"), 20.0, 300.0, 100.0, 5.0),
    })
st.caption(t("N, P and K are on the same scale as the training data, not lab readings in kg per hectare."))

if st.button(t("Generate Precision Advisory"), type="primary"):
    x = np.array([[values[k] for k in FEATURES]])
    probs = model.predict_proba(x)[0]
    order = np.argsort(probs)[::-1][:3]
    st.session_state["advice"] = {
        "inputs": dict(values),
        "top": [(str(model.classes_[i]), float(probs[i])) for i in order],
    }

advice = st.session_state.get("advice")
if advice:
    if advice["inputs"] != values:
        st.info(t("You changed the values. Press the button again to update the advice."))
    best, best_p = advice["top"][0]
    st.success(t("Best match: {crop} ({conf} confidence)", crop=best.upper() if i18n.current_lang() == "en" else i18n.crop(best), conf=f"{best_p:.0%}"))
    st.dataframe(
        pd.DataFrame({
            t("Rank"): [1, 2, 3],
            t("Crop"): [i18n.crop(c) for c, _ in advice["top"]],
            t("Confidence"): [f"{p:.0%}" for _, p in advice["top"]],
        }),
        hide_index=True,
    )
    show_nutrient_gap(best, profiles, advice["inputs"])

st.subheader(t("Check any crop"))
default_index = crops.index(advice["top"][0][0]) if advice else 0
crop_labels = {i18n.crop(c): c for c in crops}
chosen_label = st.selectbox(t("Pick a crop to see how your field fits it"), list(crop_labels), index=default_index)
chosen = crop_labels[chosen_label]
with st.expander(t("Your crop is not in the list?")):
    st.write(t("This app's crop advisor knows 22 crops. For more than 2,500 plants, look up temperature, rainfall and soil pH needs in the free FAO EcoCrop tool, then ask your KVK or the University of Agricultural Sciences which varieties suit your district."))
    st.markdown("[gaez.fao.org/pages/ecocrop-search](https://gaez.fao.org/pages/ecocrop-search)")
table, inside = explorer_table(chosen, profiles, values)
st.write(t("**{n} of 7 measures** are within the typical range for {crop}.", n=inside, crop=i18n.crop(chosen)))
st.dataframe(table, hide_index=True)

with st.expander(t("About this model and its limits")):
    if metrics:
        st.write(t("{model} trained on {rows} rows covering {crops} crops. Accuracy on a held-out 20% test set: {acc}.",
                   model=metrics["model"], rows=f"{metrics['n_rows']:,}", crops=metrics["n_crops"], acc=f"{metrics['holdout_accuracy']:.1%}"))
        st.write(t(metrics["data_note"]))
    st.write(t("It does not know your local market, water supply, pests or soil history. Talk to your agriculture officer before you decide."))

# ==============================================================================
# 6. DIY SOIL TESTING AT HOME
# ==============================================================================
with st.container(border=True):
    st.markdown("### 🧪 " + ("ಮನೆಯಲ್ಲೇ ಮಣ್ಣಿನ N, P, K ಮತ್ತು pH ಪರೀಕ್ಷೆ ಮಾಡುವ ಸುಲಭ ವಿಧಾನಗಳು" if is_kn else "DIY Soil Testing at Home: Simple N, P, K & pH Methods"))
    st.caption(
        "ಲ್ಯಾಬ್‌ಗೆ ಹೋಗದೆ ಮನೆಯಲ್ಲೇ ಸಿಗುವ ಸರಳ ಸಾಮಗ್ರಿಗಳಿಂದ ಮಣ್ಣಿನ ಆಮ್ಲೀಯತೆ (pH), ಪೋಷಕಾಂಶಗಳ ಕೊರತೆ ಮತ್ತು ಮಣ್ಣಿನ ವಿನ್ಯಾಸ ಪತ್ತೆಹಚ್ಚಿ."
        if is_kn else
        "Estimate soil pH, nutrient deficiencies, and soil texture right at your home using simple household items."
    )
    
    diy_tab1, diy_tab2, diy_tab3 = st.tabs([
        ("1️⃣ ಮಣ್ಣಿನ pH ಪರೀಕ್ಷೆ (ವಿನೆಗರ್ & ಸೋಡಾ)" if is_kn else "1️⃣ Soil pH (Vinegar & Soda Test)"),
        ("2️⃣ ಎಲೆ ಲಕ್ಷಣಗಳಿಂದ N-P-K ಕೊರತೆ ಪತ್ತೆ" if is_kn else "2️⃣ Leaf Diagnostic for N-P-K"),
        ("3️⃣ ಮಣ್ಣಿನ ಕಣ ರಚನೆ (ಬಾಟಲಿ ಪರೀಕ್ಷೆ)" if is_kn else "3️⃣ Soil Texture (Bottle Test)")
    ])
    
    with diy_tab1:
        st.markdown("#### 🥛 " + ("ವಿನೆಗರ್ & ಅಡುಗೆ ಸೋಡಾ pH ಪರೀಕ್ಷೆ" if is_kn else "Vinegar & Baking Soda Reaction Test"))
        st.write(
            "**ಮಣ್ಣಿನ ಮಾದರಿ ಸಿದ್ಧತೆ:** ನಿಮ್ಮ ಜಮೀನಿನ 4 ಬೇರೆ ಬೇರೆ ಕಡೆಗಳಿಂದ 6 ಇಂಚು ಆಳದ ಮಣ್ಣು ತೆಗೆದುಕೊಂಡು ಕಲ್ಲು-ಕಡ್ಡಿ ತೆಗೆದು ನೆರಳಿನಲ್ಲಿ ಒಣಗಿಸಿ ಪುಡಿಮಾಡಿ."
            if is_kn else
            "**Sample Prep:** Collect soil from 6 inches depth across 4 spots in your field, dry in shade, remove stones and crush finely."
        )
        
        ph_c1, ph_c2 = st.columns(2)
        with ph_c1:
            with st.container(border=True):
                st.markdown("**🧪 ಕಪ್ 'ಎ' — ಕ್ಷಾರ ಪರೀಕ್ಷೆ (ವಿನೆಗರ್ {Vinegar}):**")
                st.markdown(
                    "1. ಅರ್ಧ ಕಪ್ ಮಣ್ಣಿಗೆ ಸ್ವಲ್ಪ ಶುದ್ಧ ನೀರು ಹಾಕಿ ಕಲಸಿ.\n"
                    "2. ಅದಕ್ಕೆ ಅರ್ಧ ಕಪ್ ಬಿಳಿ ವಿನೆಗರ್ (ಆಸಿಡ್) ಸುರಿಯಿರಿ.\n"
                    "3. **ಫಲಿತಾಂಶ:** ನೊರೆ ಮತ್ತು ಗುಳ್ಳೆಗಳು (Fizzing) ಬಂದರೆ -> **ಕ್ಷಾರ ಮಣ್ಣು {Alkaline Soil, pH > 7.5}**.\n"
                    "4. *ನಿರ್ವಹಣೆ:* ಜಿಪ್ಸಂ {Gypsum} ಅಥವಾ ಸಾವಯವ ಗೊಬ್ಬರ ಮತ್ತು ಎಲೆಗೊಬ್ಬರ ಬಳಸಿ."
                    if is_kn else
                    "1. Mix 1/2 cup soil with a little distilled water.\n"
                    "2. Pour 1/2 cup white vinegar into it.\n"
                    "3. **Result:** If it fizzes/bubbles vigorously -> **Alkaline Soil (pH > 7.5)**.\n"
                    "4. *Remedy:* Apply Gypsum or well-rotted organic compost to lower pH."
                )
        with ph_c2:
            with st.container(border=True):
                st.markdown("**🧪 ಕಪ್ 'ಬಿ' — ಆಮ್ಲ ಪರೀಕ್ಷೆ (ಬೇಕಿಂಗ್ ಸೋಡಾ {Baking Soda}):**")
                st.markdown(
                    "1. ಇನ್ನೊಂದು ಕಪ್‌ನಲ್ಲಿ ಮಣ್ಣು ಮತ್ತು ನೀರನ್ನು ದ್ರಾವಣದಂತೆ ಕಲಸಿ.\n"
                    "2. ಅದಕ್ಕೆ 2 ಚಮಚ ಅಡುಗೆ ಸೋಡಾ (ಬೇಕಿಂಗ್ ಸೋಡಾ) ಹಾಕಿ ಚೆನ್ನಾಗಿ ಬೆರೆಸಿ.\n"
                    "3. **ಫಲಿತಾಂಶ:** ನೊರೆ ಮತ್ತು ಗುಳ್ಳೆಗಳು ಬಂದರೆ -> **ಆಮ್ಲೀಯ ಮಣ್ಣು {Acidic Soil, pH < 6.0}**.\n"
                    "4. *ನಿರ್ವಹಣೆ:* ಕೃಷಿ ಸುಣ್ಣ {Agricultural Lime} ಅಥವಾ ಡೋಲಮೈಟ್ ಸೇರಿಸಿ."
                    if is_kn else
                    "1. Mix soil and distilled water into a wet slurry.\n"
                    "2. Add 2 tablespoons baking soda.\n"
                    "3. **Result:** If it fizzes/bubbles -> **Acidic Soil (pH < 6.0)**.\n"
                    "4. *Remedy:* Add agricultural lime or dolomite to raise pH."
                )
        
        st.success(
            "🌟 **ಯಾವುದೇ ಕಪ್‌ನಲ್ಲಿ ನೊರೆ ಬರದಿದ್ದರೆ:** ನಿಮ್ಮ ಹೊಲದ ಮಣ್ಣು **ತಟಸ್ಥ ಮತ್ತು ಅತ್ಯುತ್ತಮ ಫಲವತ್ತಾದ ಮಣ್ಣು {Neutral & Ideal, pH 6.5 - 7.2}** ಆಗಿದೆ!"
            if is_kn else
            "🌟 **If neither fizzes:** Your soil is **Neutral & Ideal (pH 6.5 - 7.2)**, perfect for almost all crops!"
        )
            
    with diy_tab2:
        st.markdown("#### 🌿 " + ("ಗಿಡದ ಎಲೆಗಳ ಲಕ್ಷಣಗಳಿಂದ N, P, K ಕೊರತೆ ಗುರುತಿಸುವುದು" if is_kn else "Visual Leaf Signs for N, P, K Deficiencies"))
        npk_c1, npk_c2, npk_c3 = st.columns(3)
        with npk_c1:
            with st.container(border=True):
                st.markdown("**🟡 ಸಾರಜನಕ (N) ಕೊರತೆ:**")
                st.caption("ಹಳೆಯ ಕೆಳಗಿನ ಎಲೆಗಳು ಹಳದಿಯಾಗುವುದು, ಕುಂಠಿತ ಬೆಳವಣಿಗೆ.")
        with npk_c2:
            with st.container(border=True):
                st.markdown("**🟣 ರಂಜಕ (P) ಕೊರತೆ:**")
                st.caption("ಎಲೆಗಳು ನೇರಳೆ ಅಥವಾ ಕಡು ಹಸಿರು ಬಣ್ಣಕ್ಕೆ ತಿರುಗುವುದು, ಬೇರು ದುರ್ಬಲ.")
        with npk_c3:
            with st.container(border=True):
                st.markdown("**🟤 ಪೊಟ್ಯಾಷ್ (K) ಕೊರತೆ:**")
                st.caption("ಎಲೆಯ ಅಂಚುಗಳು ಸುಟ್ಟಂತೆ ಕಂದು ಬಣ್ಣಕ್ಕೆ ತಿರುಗುವುದು, ರೋಗ ಬಾಧೆ.")

    with diy_tab3:
        st.markdown("#### 🫙 " + ("ಮಣ್ಣಿನ ಕಣ ರಚನೆ (ಬಾಟಲಿ ಪರೀಕ್ಷೆ)" if is_kn else "Soil Texture Bottle Test"))
        st.markdown(
            "ಒಂದು ಗಾಜಿನ ಬಾಟಲಿಯಲ್ಲಿ 1/3 ಭಾಗ ಮಣ್ಣು ಮತ್ತು ನೀರು ಹಾಕಿ, 1 ಚಮಚ ಉಪ್ಪು ಅಥವಾ ಸಾಬೂನು ದ್ರಾವಣ ಸೇರಿಸಿ ಚೆನ್ನಾಗಿ ಕುಲುಕಿ 24 ಗಂಟೆ ಇರಿಸಿ.\n"
            "- **ಕೆಳಗೆ ಕೂರುವುದು:** ಮರಳು (Sand)\n"
            "- **ಮಧ್ಯದಲ್ಲಿ ಕೂರುವುದು:** ಹೂಳು (Silt)\n"
            "- **ಮೇಲೆ ಕೂರುವುದು:** ಜೇಡಿ ಮಣ್ಣು (Clay)"
            if is_kn else
            "Fill a jar 1/3 with soil and water, shake well with a pinch of salt/detergent, let settle for 24 hours to measure Sand, Silt, and Clay layers."
        )

# ==============================================================================
# 7. PROFESSIONAL BOTTOM FOOTER BANNER (IMAGE 1)
# ==============================================================================
st.markdown(
    """
    <div class="kn-footer">
        <div style="font-size: 1rem; font-weight: bold; margin-bottom: 8px;">
            🌱 ಸ್ಮಾರ್ಟ್ ಕೃಷಿ &nbsp;|&nbsp; 🛡️ ವಿಶ್ವಾಸಾರ್ಹ ಮಾಹಿತಿ &nbsp;|&nbsp; 👥 ಕೃಷಿಕರಿಗಾಗಿ, ಕೃಷಿಕರಿಂದ
        </div>
        <div style="font-size: 0.85rem; opacity: 0.9; margin-bottom: 12px;">
            © 2026 KrushiNudi. All rights reserved. &nbsp;|&nbsp; Developed by Abhishek Hitabutti
        </div>
        <div style="font-size: 0.8rem; opacity: 0.8;">
            <a href="?page=about" style="color: #C8E6C9; text-decoration: none;">ಗೌಪ್ಯತಾ ನೀತಿ {Privacy}</a> &nbsp;•&nbsp; 
            <a href="?page=about" style="color: #C8E6C9; text-decoration: none;">ನಿಬಂಧನೆಗಳು {Terms}</a> &nbsp;•&nbsp; 
            <a href="mailto:abhishekhitabutti@gmail.com" style="color: #C8E6C9; text-decoration: none;">ಸಂಪರ್ಕಿಸಿ {Contact}</a>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

ui.feedback_box()
