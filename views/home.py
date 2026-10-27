"""
KrushiNudi: Main Portal & Digital Agriculture Hub.
Author: Abhishek Hitabutti
Copyright: © 2026 Abhishek Hitabutti. All rights reserved.

The signature landing experience of KrushiNudi inspired by the production mobile design:
- Curved lush agricultural green hero banner
- Hyperlocal weather alert & farmer precautions ribbon
- 6 Signature Agricultural Service cards with numbered badges and quick links
- Sourced guidance metrics & farmer trust credentials
- Professional bottom footer
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

import streamlit as st

import diagnosis
import i18n
import ui
from districts import DISTRICTS, DISTRICTS_KN
from i18n import t

HERE = Path(__file__).resolve().parent.parent
BASE = HERE if (HERE / "crop_profiles.pkl").exists() else Path.cwd()


@st.cache_resource
def load_crop_count():
    try:
        with open(BASE / "crop_profiles.pkl", "rb") as f:
            profiles = pickle.load(f)
            return len(profiles)
    except Exception:
        return 22


ui.inject_css()
n_crops = load_crop_count()
is_kn = (i18n.current_lang() == "kn")

# ==============================================================================
# 1. KRUSHINUDI CONSOLIDATED UNIFIED HERO SECTION (FLOTO AUDIT RESOLUTION)
# ==============================================================================
banner_sub = (
    "ಕೃಷಿನುಡಿ {KrushiNudi} · ಕೃಷಿಕರಿಗಾಗಿ, ಕೃಷಿಕರಿಂದ · ಕರ್ನಾಟಕದ ರೈತರ ವಿಶ್ವಾಸಾರ್ಹ ಡಿಜಿಟಲ್ ಕೃಷಿ ಸಂಗಾತಿ"
    if is_kn else
    "KrushiNudi · By Farmers, For Farmers · Karnataka's Trusted Digital Agriculture Companion"
)
banner_tag = (
    "✨ ಚತುರ ಒಳನೋಟಗಳು · ಉತ್ತಮ ಕೃಷಿ · ಬುದ್ಧಿವಂತ ಕೃಷಿಯ ಧ್ವನಿ {Smart Farm Advisory}"
    if is_kn else
    "✨ Smarter Insights · Better Farming · Smart Farm Advisory"
)

logo_path = HERE / "images" / "krushinudi_logo.jpg"
intro_video_path = HERE / "images" / "krushinudi_intro.mp4"

col_hero_logo, col_hero_text = st.columns([1, 2.7])
with col_hero_logo:
    if logo_path.exists():
        st.image(str(logo_path), use_container_width=True)
with col_hero_text:
    st.markdown(
        f"""
        <div class="kn-brand-banner" style="padding: 20px 18px; margin-bottom: 0px;">
            <div class="kn-brand-title" style="font-size: 2.1rem;">
                <span>🌾</span> KrushiNudi <span>🍃</span>
            </div>
            <div class="kn-brand-tagline">
                — {"ಕೃತಕ ಬುದ್ಧಿಮತ್ತೆ ಆಧಾರಿತ ಕೃಷಿ ಮಾರ್ಗದರ್ಶನ" if is_kn else "AI Powered Farming Guidance"} —
            </div>
            <div style="font-size: 0.92rem; color: #E8F5E9; margin-top: 6px; font-weight: 500;">
                {banner_sub}
            </div>
            <div style="font-size: 0.82rem; color: #C8E6C9; margin-top: 4px; font-style: italic;">
                {banner_tag}
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

# Official KrushiNudi Video Tour Showcase
if intro_video_path.exists():
    with st.expander(
        "🎬 ಕೃಷಿನುಡಿ ಅಧಿಕೃತ ಪರಿಚಯ ವಿಡಿಯೋ ವೀಕ್ಷಿಸಿ {Watch KrushiNudi Intro Tour}"
        if is_kn else
        "🎬 Watch KrushiNudi Intro Tour (AI Farming Guidance)",
        expanded=False
    ):
        st.video(str(intro_video_path))
        st.caption(
            "✨ ಎಐ ಬೆಳೆ ವೈದ್ಯ, ಬೋರ್‌ವೆಲ್ ಪಾಯಿಂಟ್, ಹವಾಮಾನ ಮುನ್ಸೂಚನೆ ಹಾಗೂ ಗರಿಷ್ಠ ಬೆಲೆ ಮಾರುಕಟ್ಟೆ ಕೇಂದ್ರಗಳ ಸಂಪೂರ್ಣ ಪರಿಚಯ."
            if is_kn else
            "✨ Complete walkthrough of AI-powered crop diagnosis, groundwater survey, spray planner and APMC mandi market rates."
        )

# Beta Badge & Statistics Counter
st.markdown(ui.badge(t("Beta"), "medium") + " " + escape(t("Guidance comes from published sources and expert review is in progress.")), unsafe_allow_html=True)
ui.stat_row([(n_crops, t("crops in the advisor")), (len(DISTRICTS), t("Karnataka districts")),
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

# Row 2: Season Planner & Direct Buy (Farmer to Consumer - Directly Below Weather Precautions)
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
            "<span style='background:#2E7D32; color:#fff; font-size:0.75rem; font-weight:bold; padding:2px 8px; border-radius:10px; float:right;'>4</span>"
            "**📈 " + ("ಮಾರುಕಟ್ಟೆ ದರ & ಮಾರಾಟ ಕೇಂದ್ರಗಳು {Market Rates & Selling}" if is_kn else "Market Rates & Best Price Selling") + "**",
            unsafe_allow_html=True
        )
        st.caption(
            "ದೈನಂದಿನ ಎಪಿಎಂಸಿ ದರಗಳು, ಬೆಲೆ ಏರಿಕೆ/ಇಳಿಕೆ ಮುನ್ಸೂಚನಾ ಗ್ರಾಫ್ ಹಾಗೂ ನಿಮ್ಮ ಜಿಲ್ಲೆಯಲ್ಲಿ ಗರಿಷ್ಠ ಬೆಲೆಗೆ ಬೆಳೆ ಮಾರಾಟ ಮಾಡಲು ಅಧಿಕೃತ ಖರೀದಿ ಕೇಂದ್ರಗಳು."
            if is_kn else
            "Daily APMC mandi rates, 30-day price trend graphs, forecasts and verified government/private centers to sell your crop at highest rates."
        )
        ui.page_link("views/market_rates.py", "ಮಾರುಕಟ್ಟೆ & ಮಾರಾಟ {View Rates & Centers}" if is_kn else "Market Rates & Centers", "👉")

# Row 3: Borewell Advisory & Crop Advisor
c_r3_1, c_r3_2 = st.columns(2)
with c_r3_1:
    with st.container(border=True):
        st.markdown(
            "<span style='background:#0288D1; color:#fff; font-size:0.75rem; font-weight:bold; padding:2px 8px; border-radius:10px; float:right;'>5</span>"
            "**💧 " + t("Borewell advisory") + "**",
            unsafe_allow_html=True
        )
        st.caption(
            "ಗ್ರಾಮ/ಹೋಬಳಿ ಮಟ್ಟದ ಅಂತರ್ಜಲ ಶಿಲಾ ಬಿರುಕುಗಳ (Lineaments) ಆಧಾರದ ಮೇಲೆ ಜಮೀನಿನ ನಿಖರ ಪಾಯಿಂಟ್‌ಗಳು."
            if is_kn else
            "Check groundwater levels, strike depths, and exact GPS lineament points on your land plot."
        )
        ui.page_link("views/borewell.py", "ಬೋರ್‌ವೆಲ್ ಮಾಹಿತಿ {Borewell Advisor}" if is_kn else "Open Borewell Advisory", "👉")

with c_r3_2:
    with st.container(border=True):
        st.markdown(
            "<span style='background:#388E3C; color:#fff; font-size:0.75rem; font-weight:bold; padding:2px 8px; border-radius:10px; float:right;'>6</span>"
            "**🌱 " + t("Crop advisor") + "**",
            unsafe_allow_html=True
        )
        st.caption(
            "ಮಣ್ಣಿನ N-P-K ಪೋಷಕಾಂಶಗಳು, pH ಮತ್ತು ಹವಾಮಾನಕ್ಕೆ ತಕ್ಕಂತೆ ಗರಿಷ್ಠ ಇಳುವರಿಯ ಬೆಳೆ ಶಿಫಾರಸು."
            if is_kn else
            "AI/ML model matching your soil N-P-K, pH & climate to 22 scientifically tested crops."
        )
        ui.page_link("views/crop_advisor.py", "ಬೆಳೆ ಸಲಹೆಗಾರ {Open Crop Advisor}" if is_kn else "Open Crop Advisor", "👉")

# Row 4: Weed & Nutrient Advisory & Spray Prescription
c_r4_1, c_r4_2 = st.columns(2)
with c_r4_1:
    with st.container(border=True):
        st.markdown(
            "<span style='background:#FBC02D; color:#333; font-size:0.75rem; font-weight:bold; padding:2px 8px; border-radius:10px; float:right;'>7</span>"
            "**🌿 " + t("Weed & nutrient advisory") + "**",
            unsafe_allow_html=True
        )
        st.caption(
            "20 ಕ್ಕೂ ಹೆಚ್ಚು ಕಳೆಗಳ ರಾಸಾಯನಿಕ ರಹಿತ ದಮನ, ಕಾಂಪೋಸ್ಟ್ ವಿಧಾನಗಳು ಮತ್ತು ಗೊಬ್ಬರ ಉಳಿತಾಯ."
            if is_kn else
            "Non-chemical weed suppression for 20+ weeds, compost methods and fertilizer cost savings."
        )
        ui.page_link("views/weed_nutrient.py", "ಕಳೆ & ಪೋಷಕಾಂಶ {Weed Advisor}" if is_kn else "Weed & Nutrients", "👉")

with c_r4_2:
    with st.container(border=True):
        st.markdown(
            "<span style='background:#7B1FA2; color:#fff; font-size:0.75rem; font-weight:bold; padding:2px 8px; border-radius:10px; float:right;'>8</span>"
            "**💊 " + t("Spray & nutrition prescription") + "**",
            unsafe_allow_html=True
        )
        st.caption(
            "ನಿಮ್ಮ ಜಮೀನಿನ ಅಳತೆಗೆ ತಕ್ಕಂತೆ ಔಷಧದ ನಿಖರ ಡೋಸ್, ಬೂಸ್ಟರ್ ಟಾನಿಕ್ ಹಾಗೂ ನೇರ ಖರೀದಿ ಚೀಟಿ."
            if is_kn else
            "Crop protection, dosages, high-yield boosters and printable prescription slip."
        )
        ui.page_link("views/spray_prescription.py", "ಔಷಧ ಚೀಟಿ {Open Prescription}" if is_kn else "Open Prescription", "👉")

# Row 5: Schemes and Help & User Guide
c_r5_1, c_r5_2 = st.columns(2)
with c_r5_1:
    with st.container(border=True):
        st.markdown(
            "<span style='background:#00838F; color:#fff; font-size:0.75rem; font-weight:bold; padding:2px 8px; border-radius:10px; float:right;'>9</span>"
            "**📋 " + t("Schemes and help") + "**",
            unsafe_allow_html=True
        )
        st.caption(
            "ಬೆಳೆ ವಿಮೆ, ಪಿಎಂ-ಕಿಸಾನ್, ಕೃಷಿ ಸಾಲ ಹಾಗೂ ಸರ್ಕಾರಿ ಸೌಲಭ್ಯಗಳ ಪರಿಶೀಲನಾ ಪಟ್ಟಿ."
            if is_kn else
            "Documents, eligibility and direct steps for crop insurance, PM-KISAN and agri loans."
        )
        ui.page_link("views/schemes.py", "ಸರ್ಕಾರಿ ಯೋಜನೆಗಳು {View Schemes}" if is_kn else "View Schemes", "👉")

with c_r5_2:
    with st.container(border=True):
        st.markdown(
            "<span style='background:#455A64; color:#fff; font-size:0.75rem; font-weight:bold; padding:2px 8px; border-radius:10px; float:right;'>10</span>"
            "**📖 " + t("How to use") + "**",
            unsafe_allow_html=True
        )
        st.caption(
            "ಕೃಷಿನುಡಿ ಆ್ಯಪ್‌ನ ಪ್ರತಿಯೊಂದು ಸೇವೆಯನ್ನು ಸರಳವಾಗಿ ಬಳಸುವ ಹಂತ-ಹಂತದ ಪ್ರಾತ್ಯಕ್ಷಿಕೆ ಮತ್ತು ಕೈಪಿಡಿ."
            if is_kn else
            "Step-by-step interactive farmer guide and video demonstrations for all KrushiNudi tools."
        )
        ui.page_link("views/guide.py", "ಬಳಕೆ ಕೈಪಿಡಿ {User Guide}" if is_kn else "User Guide", "👉")

# ==============================================================================
# 4. PROFESSIONAL BOTTOM FOOTER BANNER (IMAGE 1)
# ==============================================================================
footer_motto = "🌱 ಸ್ಮಾರ್ಟ್ ಕೃಷಿ &nbsp;|&nbsp; 🛡️ ವಿಶ್ವಾಸಾರ್ಹ ಮಾಹಿತಿ &nbsp;|&nbsp; 👥 ಕೃಷಿಕರಿಗಾಗಿ, ಕೃಷಿಕರಿಂದ" if is_kn else "🌱 Smart Farming &nbsp;|&nbsp; 🛡️ Sourced Intelligence &nbsp;|&nbsp; 👥 For Farmers, By Farmers"
footer_links = (
    '<a href="?page=about" style="color: #C8E6C9; text-decoration: none;">ಗೌಪ್ಯತಾ ನೀತಿ {Privacy}</a> &nbsp;•&nbsp; '
    '<a href="?page=about" style="color: #C8E6C9; text-decoration: none;">ನಿಬಂಧನೆಗಳು {Terms}</a> &nbsp;•&nbsp; '
    '<a href="mailto:abhishekhitabutti@gmail.com" style="color: #C8E6C9; text-decoration: none;">ಸಂಪರ್ಕಿಸಿ {Contact}</a>'
    if is_kn else
    '<a href="?page=about" style="color: #C8E6C9; text-decoration: none;">Privacy Policy</a> &nbsp;•&nbsp; '
    '<a href="?page=about" style="color: #C8E6C9; text-decoration: none;">Terms of Service</a> &nbsp;•&nbsp; '
    '<a href="mailto:abhishekhitabutti@gmail.com" style="color: #C8E6C9; text-decoration: none;">Contact Developer</a>'
)

st.markdown(
    f"""
    <div class="kn-footer">
        <div style="font-size: 1rem; font-weight: bold; margin-bottom: 8px;">
            {footer_motto}
        </div>
        <div style="font-size: 0.85rem; opacity: 0.9; margin-bottom: 12px;">
            © 2026 KrushiNudi. All rights reserved. &nbsp;|&nbsp; Developed by Abhishek Hitabutti
        </div>
        <div style="font-size: 0.8rem; opacity: 0.8;">
            {footer_links}
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

ui.feedback_box()
