"""How to use KrushiNudi - Interactive App Demo and User Guide.
Fully bilingual: 100% pure Kannada localization with technical terms in braces {...}.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import streamlit as st
import i18n
import ui
from i18n import t

is_kn = (i18n.current_lang() == "kn")

# --- HERO SECTION ---
hero_title = "ಆ್ಯಪ್ ಬಳಕೆ ಮಾರ್ಗದರ್ಶಿ ಮತ್ತು ಡೆಮೊ" if is_kn else "How to Use KrushiNudi"
hero_sub = (
    "ಕೃಷಿನುಡಿಯ {KrushiNudi} ಎಲ್ಲಾ 6 ಮುಖ್ಯ ಕೃಷಿ ಉಪಕರಣಗಳ ಹಂತ ಹಂತದ ಬಳಕೆ ವಿವರ, ರೈತ ಸಲಹೆಗಳು ಮತ್ತು ನೇರ ಪ್ರಾಯೋಗಿಕ ಡೆಮೊ {Live Demo}."
    if is_kn else
    "Complete step-by-step guide, practical farmer tips, and live interactive demo for all 6 core agricultural tools."
)
ui.hero(hero_title, hero_sub, "📖")

# --- QUICK START OVERVIEW ---
st.markdown("### " + ("ತ್ವರಿತ ಆರಂಭ: 3 ಸರಳ ಹಂತಗಳು" if is_kn else "Quick Start: 3 Simple Steps"))
step_cols = st.columns(3)
with step_cols[0]:
    with st.container(border=True):
        st.markdown(f"**🌾 {'1. ಮಣ್ಣು & ಬೆಳೆ' if is_kn else '1. Soil & Crop'}**")
        st.caption(
            "ಮಣ್ಣಿನ ಪೋಷಕಾಂಶಗಳನ್ನು ({N}, {P}, {K}, {pH}) ಹೊಂದಿಸಿ ನಿಮ್ಮ ಹೊಲಕ್ಕೆ ಅತ್ಯಂತ ಸೂಕ್ತವಾದ ಬೆಳೆಯನ್ನು ಆಯ್ಕೆಮಾಡಿ."
            if is_kn else
            "Set soil measures (N, P, K, pH) to find the best-matched crop for your land."
        )
with step_cols[1]:
    with st.container(border=True):
        st.markdown(f"**🩺 {'2. ರೋಗ & ಹವಾಮಾನ' if is_kn else '2. Health & Weather'}**")
        st.caption(
            "ರೋಗಪೀಡಿತ ಗಿಡದ ಫೋಟೋ ತೆಗೆದು ಚಿಕಿತ್ಸೆ ತಿಳಿಯಿರಿ ಮತ್ತು 7 ದಿನಗಳ ಹವಾಮಾನ ನೋಡಿ ಸಿಂಪಡಣೆ ಸಮಯ ನಿಗದಿಪಡಿಸಿ."
            if is_kn else
            "Photograph sick plants for safe treatment steps and check 7-day spray timing."
        )
with step_cols[2]:
    with st.container(border=True):
        st.markdown(f"**📋 {'3. ಋತು & ಯೋಜನೆಗಳು' if is_kn else '3. Season & Schemes'}**")
        st.caption(
            "ಬೀಜ ಮೊಳಕೆ ಶೇಕಡಾವಾರು ಲೆಕ್ಕ ಹಾಕಿ, {PMFBY} ಬೆಳೆ ವಿಮೆ ಮತ್ತು ಕಿಸಾನ್ ಕ್ರೆಡಿಟ್ ಕಾರ್ಡ್ {KCC} ಸೌಲಭ್ಯ ಪಡೆಯಿರಿ."
            if is_kn else
            "Calculate seed germination vigor, prepare PMFBY insurance claims and loan records."
        )

st.markdown("---")

# --- INTERACTIVE TABS ---
tab_titles = [
    "🌾 ಬೆಳೆ ಸಲಹೆಗಾರ" if is_kn else "🌾 Crop Advisor",
    "🩺 ಬೆಳೆ ವೈದ್ಯ" if is_kn else "🩺 Crop Doctor",
    "🗓️ ಋತು ಯೋಜಕ" if is_kn else "🗓️ Season Planner",
    "⛈️ ಹವಾಮಾನ ರಕ್ಷಣೆ" if is_kn else "⛈️ Weather Precautions",
    "📋 ಯೋಜನೆಗಳು & ಸಹಾಯ" if is_kn else "📋 Schemes & Help",
    "🔒 ಖಾತೆ & ಸುರಕ್ಷತೆ" if is_kn else "🔒 Account & Privacy",
]

t1, t2, t3, t4, t5, t6 = st.tabs(tab_titles)

# ==========================================
# TAB 1: CROP ADVISOR
# ==========================================
with t1:
    st.subheader("ಬೆಳೆ ಸಲಹೆಗಾರ {Crop Advisor} ಹೇಗೆ ಬಳಸುವುದು?" if is_kn else "How to use the Crop Advisor")
    if is_kn:
        st.markdown(
            "ಬೆಳೆ ಸಲಹೆಗಾರವು ಯಂತ್ರ ಕಲಿಕೆ ಮಾದರಿಯನ್ನು {Random Forest Model} ಬಳಸಿಕೊಂಡು ಕರ್ನಾಟಕದ 22 ಪ್ರಮುಖ ಬೆಳೆಗಳಲ್ಲಿ ನಿಮ್ಮ ಹೊಲಕ್ಕೆ "
            "ಅತ್ಯಂತ ಸೂಕ್ತವಾದ ಬೆಳೆಯನ್ನು ಶಿಫಾರಸು ಮಾಡುತ್ತದೆ.\n\n"
            "**ಬಳಸುವ 3 ಹಂತಗಳು:**\n"
            "1. **ಅಳತೆಗಳನ್ನು ನಮೂದಿಸಿ:** ನಿಮ್ಮ ಮಣ್ಣು ಆರೋಗ್ಯ ಕಾರ್ಡ್ {Soil Health Card} ಆಧಾರದ ಮೇಲೆ ಸಾರಜನಕ {N}, ರಂಜಕ {P}, ಪೊಟ್ಯಾಸಿಯಂ {K}, "
            "ಮಣ್ಣಿನ ಹುಳಿ-ಖಾರ {pH}, ತಾಪಮಾನ, ಆರ್ದ್ರತೆ ಮತ್ತು ಮಳೆಯ ಸ್ಲೈಡರ್‌ಗಳನ್ನು ಸರಿಹೊಂದಿಸಿ.\n"
            "2. **'ಸಲಹೆ ಪಡೆಯಿರಿ' ಬಟನ್ ಒತ್ತಿ:** ಕೃತಕ ಬುದ್ಧಿಮತ್ತೆಯು 2,200 ಹೊಲಗಳ ತರಬೇತಿ ಡೇಟಾದೊಂದಿಗೆ ನಿಮ್ಮ ಮಣ್ಣನ್ನು ತಾಳೆ ನೋಡುತ್ತದೆ.\n"
            "3. **ಫಲಿತಾಂಶ ಪರಿಶೀಲಿಸಿ:** ಮೊದಲ ಸ್ಥಾನದಲ್ಲಿರುವ ಬೆಳೆ, ವಿಶ್ವಾಸಾರ್ಹತೆಯ ಶೇಕಡಾವಾರು ಮತ್ತು ಪೋಷಕಾಂಶಗಳ ಕೊರತೆಯನ್ನು ನಿವಾರಿಸಲು ಸಾಮಾನ್ಯ ಗೊಬ್ಬರಗಳ "
            "(ಯೂರಿಯಾ {Urea}, ಸಿಂಗಲ್ ಸೂಪರ್ ಫಾಸ್ಫೇಟ್ {SSP}, ಮ್ಯೂರಿಯೇಟ್ ಆಫ್ ಪೊಟ್ಯಾಶ್ {MOP}) ಸೂಚನೆಗಳನ್ನು ಓದಿ."
        )
    else:
        st.markdown(
            "The Crop Advisor uses a trained Random Forest machine learning model to recommend the best match among 22 Karnataka crops "
            "based on soil nutrients and local climate conditions.\n\n"
            "**3 Steps to use:**\n"
            "1. **Set your measures:** Adjust Nitrogen (N), Phosphorus (P), Potassium (K), Soil pH, Temperature, Humidity, and Rainfall sliders.\n"
            "2. **Click 'Generate Precision Advisory':** The model matches your numbers against 2,200 training records.\n"
            "3. **Review recommendations:** See the best-matched crop, confidence score, ideal nutrient ranges, and practical sources for any deficiencies."
        )

    # Interactive Demo Box for Crop Advisor
    with st.container(border=True):
        st.markdown(f"**🎮 {'ನೇರ ಡೆಮೊ: ಮಣ್ಣಿನ ಮಾದರಿ ಪರೀಕ್ಷಿಸಿ' if is_kn else 'Live Demo: Test Soil Scenarios'}**")
        st.caption(
            "ವಿವಿಧ ಮಣ್ಣಿನ ಮಾದರಿಗಳನ್ನು ಆರಿಸಿ ಬೆಳೆ ಸಲಹೆಗಾರ ಹೇಗೆ ಕಾರ್ಯನಿರ್ವಹಿಸುತ್ತದೆ ಎಂಬುದನ್ನು ಕೆಳಗೆ ನೋಡಿ:"
            if is_kn else
            "Select a realistic soil scenario below to see how the Crop Advisor responds instantly:"
        )

        preset_options = [
            "ದಕ್ಷಿಣ ಕರ್ನಾಟಕದ ಕೆಂಪು ಮರಳು ಮಣ್ಣು (ರಾಗಿ ಮಾದರಿ)" if is_kn else "Southern Karnataka Red Sandy Loam (Ragi Preset)",
            "ನದಿ ಕಣಿವೆಯ ಗೋಡು ಮಣ್ಣು (ಭತ್ತ ಮಾದರಿ)" if is_kn else "River Basin Wetland Alluvial Soil (Rice/Paddy Preset)",
            "ಉತ್ತರ ಕರ್ನಾಟಕದ ಕಪ್ಪು ಹತ್ತಿ ಮಣ್ಣು (ಹತ್ತಿ ಮಾದರಿ)" if is_kn else "Northern Karnataka Black Cotton Soil (Cotton Preset)",
        ]
        choice = st.selectbox("ಮಣ್ಣಿನ ಸನ್ನಿವೇಶ ಆಯ್ಕೆಮಾಡಿ" if is_kn else "Select soil scenario", preset_options, key="demo_soil_preset")

        if "ರಾಗಿ" in choice or "Ragi" in choice:
            demo_crop = "ರಾಗಿ {Ragi}" if is_kn else "Ragi (Finger Millet)"
            demo_conf = "96%"
            demo_n_status = "ಸಾರಜನಕ ಆದರ್ಶ ಮಟ್ಟಕ್ಕೆ ಹತ್ತಿರವಾಗಿದೆ {N: 52 / 50}" if is_kn else "Nitrogen is near ideal (52 vs 50)"
            demo_advice = "ಕಡಿಮೆ ಮಳೆ ಮತ್ತು ಕೆಂಪು ಮಣ್ಣಿನ ವಲಯಕ್ಕೆ ರಾಗಿ ಅತ್ಯಂತ ಸೂಕ್ತ ಬೆಳೆಯಾಗಿದೆ." if is_kn else "Ragi is exceptionally well suited for red sandy soils with low rainfall."
        elif "ಭತ್ತ" in choice or "Rice" in choice:
            demo_crop = "ಭತ್ತ {Rice}" if is_kn else "Rice (Paddy)"
            demo_conf = "98%"
            demo_n_status = "ಹೆಚ್ಚು ಸಾರಜನಕ ಮತ್ತು ಹೆಚ್ಚಿನ ತೇವಾಂಶ ಲಭ್ಯವಿದೆ {Rainfall: 210mm}" if is_kn else "High nitrogen and high water availability (Rainfall: 210mm)"
            demo_advice = "ನೀರು ನಿಲ್ಲುವ ಗೋಡು ಮಣ್ಣಿಗೆ ಉತ್ತಮ ಹೊಂದಾಣಿಕೆ." if is_kn else "Excellent fit for water-retentive clay loam soils."
        else:
            demo_crop = "ಹತ್ತಿ {Cotton}" if is_kn else "Cotton"
            demo_conf = "94%"
            demo_n_status = "ಪೊಟ್ಯಾಸಿಯಂ ಕೊರತೆ ಇದೆ. {MOP} ಗೊಬ್ಬರ ಬಳಸಿ" if is_kn else "Potassium is below ideal. Consider MOP compost."
            demo_advice = "ಆಳವಾದ ಕಪ್ಪು ಮಣ್ಣಿನಲ್ಲಿ ಹತ್ತಿ ಉತ್ತಮ ಇಳುವರಿ ನೀಡುತ್ತದೆ." if is_kn else "Deep black soils offer great moisture-holding capacity for cotton."

        dcol1, dcol2 = st.columns(2)
        with dcol1:
            st.metric("ಶಿಫಾರಸು ಮಾಡಿದ ಬೆಳೆ" if is_kn else "Recommended Crop", demo_crop, f"{demo_conf} " + ("ವಿಶ್ವಾಸ" if is_kn else "confidence"))
        with dcol2:
            st.info(f"**{'ಪೋಷಕಾಂಶಗಳ ಸ್ಥಿತಿ' if is_kn else 'Nutrient Status'}:** {demo_n_status}\n\n*{demo_advice}*")

    ui.page_link("views/home.py", "ಬೆಳೆ ಸಲಹೆಗಾರ ಪುಟಕ್ಕೆ ಹೋಗಿ" if is_kn else "Go to Crop Advisor Page", "🌾")


# ==========================================
# TAB 2: CROP DOCTOR
# ==========================================
with t2:
    st.subheader("ಬೆಳೆ ವೈದ್ಯ {Crop Doctor} ಹೇಗೆ ಬಳಸುವುದು?" if is_kn else "How to use the Crop Doctor")
    if is_kn:
        st.markdown(
            "ಬೆಳೆ ವೈದ್ಯವು ನಿಮ್ಮ ಬೆಳೆಯ ಫೋಟೋವನ್ನು ನೋಡಿ ರೋಗ, ಕೀಟ, ಅಥವಾ ಪೋಷಕಾಂಶಗಳ ಕೊರತೆಯನ್ನು ಗುರುತಿಸುತ್ತದೆ ಮತ್ತು ಐಸಿಎಆರ್ {ICAR} ಹಾಗೂ "
            "ರಾಜ್ಯ ಕೃಷಿ ವಿಶ್ವವಿದ್ಯಾಲಯಗಳ ಸಂಶೋಧಿತ ಚಿಕಿತ್ಸಾ ಕ್ರಮಗಳನ್ನು ನೀಡುತ್ತದೆ.\n\n"
            "**ಸ್ಪಷ್ಟ ಫೋಟೋ ತೆಗೆಯುವ 4 ನಿಯಮಗಳು:**\n"
            "- ☀️ **ನೈಸರ್ಗಿಕ ಬೆಳಕು:** ಹಗಲಿನ ಬೆಳಕಿನಲ್ಲಿ ಫೋಟೋ ತೆಗೆಯಿರಿ. ತೀವ್ರವಾದ ನೆರಳು ಅಥವಾ ಕತ್ತಲು ಇರಬಾರದು.\n"
            "- 🔍 **ಹತ್ತಿರದ ನೋಟ:** ರೋಗಪೀಡಿತ ಎಲೆ, ಕಲೆ ಅಥವಾ ಕೀಟವು ಕ್ಯಾಮೆರಾ ಚೌಕಟ್ಟನ್ನು ತುಂಬುವಂತೆ ಹತ್ತಿರದಿಂದ ಫೋಕಸ್ ಮಾಡಿ.\n"
            "- 🌿 **ಗಿಡ ಮಾತ್ರ:** ಫೋಟೋದಲ್ಲಿ ನಿಮ್ಮ ಕೈಗಳು, ಕೃಷಿ ಉಪಕರಣಗಳು ಅಥವಾ ಪಾದರಕ್ಷೆಗಳು ಬರದಂತೆ ನೋಡಿಕೊಳ್ಳಿ.\n"
            "- 🎯 **ಒಂದೇ ಸಮಸ್ಯೆ:** ಪ್ರತಿ ಫೋಟೋದಲ್ಲಿ ಒಂದೇ ಸಮಸ್ಯೆಯನ್ನು ಮಾತ್ರ ಸೆರೆಹಿಡಿಯಿರಿ."
        )
    else:
        st.markdown(
            "The Crop Doctor analyses photos of affected plants to diagnose diseases, pests, weeds, or nutrient deficiencies, "
            "providing reviewed treatments from ICAR, TNAU, and State Agricultural Universities.\n\n"
            "**4 Rules for Taking an Accurate Photo:**\n"
            "- ☀️ **Natural daylight:** Take photos in clear daytime light. Avoid deep shadows or night flash.\n"
            "- 🔍 **Close-up framing:** Let the affected spot, lesion, or insect fill the entire frame.\n"
            "- 🌿 **Clean background:** Avoid including fingers, farm implements, boots, or ground clutter.\n"
            "- 🎯 **One issue per photo:** Focus on a single diseased leaf or pest cluster at a time."
        )

    # Interactive Demo Box for Crop Doctor
    with st.container(border=True):
        st.markdown(f"**🎮 {'ನೇರ ಡೆಮೊ: ರೋಗ ತಪಾಸಣೆ ಮತ್ತು ಚಿಕಿತ್ಸೆ' if is_kn else 'Live Demo: Diagnosis & Treatment'}**")
        st.caption(
            "ಸಾಮಾನ್ಯ ರೋಗದ ಮಾದರಿಯನ್ನು ಆಯ್ಕೆಮಾಡಿ ಮತ್ತು ಬೆಳೆ ವೈದ್ಯ ನೀಡುವ ಪರಿಹಾರ ಕ್ರಮಗಳನ್ನು ಗಮನಿಸಿ:"
            if is_kn else
            "Choose a common crop issue to preview the exact diagnosis and safety guidance:"
        )

        problem_choice = st.selectbox(
            "ಸಮಸ್ಯೆಯನ್ನು ಆರಿಸಿ" if is_kn else "Select sample issue",
            [
                "ಭತ್ತದ ಕುತ್ತಿಗೆ ರೋಗ {Rice Blast}" if is_kn else "Rice Blast (Pyricularia oryzae)",
                "ಟೊಮೆಟೊ ಮುಂಚಿನ ಎಲೆ ಮಚ್ಚೆ ರೋಗ {Tomato Early Blight}" if is_kn else "Tomato Early Blight (Alternaria solani)",
                "ಮೆಕ್ಕೆಜೋಳದ ಸೈನಿಕ ಹುಳು {Maize Fall Armyworm}" if is_kn else "Maize Fall Armyworm (Spodoptera frugiperda)",
            ],
            key="demo_doctor_problem"
        )

        if "Rice Blast" in problem_choice or "ಕುತ್ತಿಗೆ ರೋಗ" in problem_choice:
            st.markdown(ui.badge("ರೋಗ {Disease}" if is_kn else "Disease", "disease"), unsafe_allow_html=True)
            if is_kn:
                st.write("**ಮೊದಲು ಇದನ್ನು ಮಾಡಿ (ಸಿಂಪಡಣೆ ಇಲ್ಲದೆ):** ಸಾರಜನಕ ಗೊಬ್ಬರವನ್ನು {Urea} ಅತಿಯಾಗಿ ಹಾಕಬೇಡಿ. ಹೊಲದಲ್ಲಿ ನೀರು ನಿಲ್ಲದಂತೆ ಬಸಿದು ಹೋಗಲು ಕಾಲುವೆ ಮಾಡಿ.")
                st.write("**ಪರಿಶೀಲಿತ ರಾಸಾಯನಿಕ ಆಯ್ಕೆ:** ಟ್ರೈಸೈಕ್ಲಾಜೋಲ್ {Tricyclazole 75% WP} ಅಥವಾ ಅಜಾಕ್ಸಿಸ್ಟ್ರೋಬಿನ್ {Azoxystrobin}.")
            else:
                st.write("**Do this first (no spray):** Stop excess nitrogen (urea) applications. Improve field drainage.")
                st.write("**Approved chemical options:** Tricyclazole 75% WP or Azoxystrobin (consult agriculture officer for local dosage).")
        elif "Tomato" in problem_choice or "ಟೊಮೆಟೊ" in problem_choice:
            st.markdown(ui.badge("ರೋಗ {Disease}" if is_kn else "Disease", "disease"), unsafe_allow_html=True)
            if is_kn:
                st.write("**ಮೊದಲು ಇದನ್ನು ಮಾಡಿ (ಸಿಂಪಡಣೆ ಇಲ್ಲದೆ):** ನೆಲಕ್ಕೆ ತಾಗುವ ಕೆಳಗಿನ ಹಳದಿ ಎಲೆಗಳನ್ನು ಕತ್ತರಿಸಿ ಸುಟ್ಟುಹಾಕಿ. ಗಿಡಗಳಿಗೆ ಬುಡದಲ್ಲಿ ನೀರು ಕೊಡಿ.")
                st.write("**ಪರಿಶೀಲಿತ ರಾಸಾಯನಿಕ ಆಯ್ಕೆ:** ಮ್ಯಾಂಕೋಜೆಬ್ {Mancozeb 75% WP} ಅಥವಾ ಕಾಪರ್ ಆಕ್ಸಿಕ್ಲೋರೈಡ್ {Copper Oxychloride}.")
            else:
                st.write("**Do this first (no spray):** Prune lower infected leaves touching the soil. Water at the base, not over the foliage.")
                st.write("**Approved chemical options:** Mancozeb 75% WP or Copper Oxychloride 50% WP.")
        else:
            st.markdown(ui.badge("ಕೀಟ {Pest}" if is_kn else "Pest", "pest"), unsafe_allow_html=True)
            if is_kn:
                st.write("**ಮೊದಲು ಇದನ್ನು ಮಾಡಿ (ಸಿಂಪಡಣೆ ಇಲ್ಲದೆ):** ಮೊಟ್ಟೆಯ ರಾಶಿಗಳನ್ನು ಕೈಯಿಂದ ಆರಿಸಿ ನಾಶಪಡಿಸಿ. ಸುಳಿಯಲ್ಲಿ ಮರಳು ಮತ್ತು ಬೇವಿನ ಪುಡಿ ಹಾಕಿ.")
                st.write("**ಪರಿಶೀಲಿತ ರಾಸಾಯನಿಕ ಆಯ್ಕೆ:** ಎಮಾಮೆಕ್ಟಿನ್ ಬೆಂಜೊಯೇಟ್ {Emamectin Benzoate 5% SG} ಅಥವಾ ಕ್ಲೋರಾಂಟ್ರಾನಿಲಿಪ್ರೋಲ್ {Chlorantraniliprole}.")
            else:
                st.write("**Do this first (no spray):** Hand-pick egg masses. Apply neem cake powder or dry sand into plant whorls.")
                st.write("**Approved chemical options:** Emamectin Benzoate 5% SG or Chlorantraniliprole 18.5% SC.")

        st.caption("⚠️ " + ("ಗಮನಿಸಿ: ಈ ಆ್ಯಪ್ ಯಾವುದೇ ರಾಸಾಯನಿಕ ಪ್ರಮಾಣ ನೀಡುವುದಿಲ್ಲ. ಪ್ರಮಾಣಕ್ಕಾಗಿ ಲೇಬಲ್ ಅಥವಾ ಕೃಷಿ ಅಧಿಕಾರಿಯನ್ನು ಸಂಪರ್ಕಿಸಿ." if is_kn else "Note: This app gives no doses. Always confirm label dose with your agriculture officer."))

    ui.page_link("views/crop_doctor.py", "ಬೆಳೆ ವೈದ್ಯ ಪುಟಕ್ಕೆ ಹೋಗಿ" if is_kn else "Go to Crop Doctor Page", "🩺")


# ==========================================
# TAB 3: SEASON PLANNER
# ==========================================
with t3:
    st.subheader("ಋತು ಯೋಜಕ {Season Planner} ಹೇಗೆ ಬಳಸುವುದು?" if is_kn else "How to use the Season Planner")
    if is_kn:
        st.markdown(
            "ಋತು ಯೋಜಕವು ಬಿತ್ತನೆಯಿಂದ ಹಿಡಿದು ಕೊಯ್ಲಿನವರೆಗೆ ರೈತರು ಅನುಸರಿಸಬೇಕಾದ ವೈಜ್ಞಾನಿಕ ಕೃಷಿ ಪದ್ಧತಿಗಳನ್ನು 4 ಹಂತಗಳಲ್ಲಿ ಒದಗಿಸುತ್ತದೆ:\n\n"
            "1. **ಬಿತ್ತನೆಗೆ ಮೊದಲು {Before Sowing}:** ಬೇಸಿಗೆ ಉಳುಮೆ, ಮಣ್ಣು ಪರೀಕ್ಷೆ, ಕೊಟ್ಟಿಗೆ ಗೊಬ್ಬರ ಮತ್ತು ಬೀಜೋಪಚಾರ.\n"
            "2. **ಬಿತ್ತನೆ {Sowing}:** ಬೀಜದ ಪ್ರಮಾಣ, ಸಾಲಿನ ಅಂತರ ಮತ್ತು ಅತ್ಯಂತ ಮುಖ್ಯವಾದ ಬೀಜ ಮೊಳಕೆ ಪರೀಕ್ಷೆ.\n"
            "3. **ಬೆಳವಣಿಗೆ {Growing}:** ಕಳೆ ಕೀಳುವುದು, ಸೂಕ್ತ ಸಮಯದಲ್ಲಿ ಮೇಲುಗೊಬ್ಬರ ನೀಡುವುದು ಮತ್ತು ಕೀಟ ನಿಗಾ.\n"
            "4. **ಕೊಯ್ಲು ಮತ್ತು ಸಂಗ್ರಹಣೆ {Harvest & Storage}:** ಧಾನ್ಯವನ್ನು ಸರಿಯಾಗಿ ಒಣಗಿಸುವುದು (12% ತೇವಾಂಶ) ಮತ್ತು ಸುರಕ್ಷಿತ ದಾಸ್ತಾನು."
        )
    else:
        st.markdown(
            "The Season Planner lays out verified agricultural practices across all four crop lifecycle stages:\n\n"
            "1. **Before Sowing:** Summer deep ploughing, soil testing, farmyard manure application, and bio-seed treatment.\n"
            "2. **Sowing:** Recommended seed rate, line spacing, depth, and crucial seed germination vigor testing.\n"
            "3. **Growing:** Inter-cultivation, weed management, split fertilizer application, and pest surveillance.\n"
            "4. **Harvest & Storage:** Optimum grain maturity harvesting, drying to 12% moisture, and pest-free storage."
        )

    # Interactive Demo Box for Germination Calculator
    with st.container(border=True):
        st.markdown(f"**🎮 {'ನೇರ ಡೆಮೊ: ಬೀಜ ಮೊಳಕೆ ಸಾಮರ್ಥ್ಯ ಲೆಕ್ಕಾಚಾರ' if is_kn else 'Live Demo: Seed Germination Calculator'}**")
        st.caption(
            "100 ಬೀಜಗಳನ್ನು ಒದ್ದೆ ಬಟ್ಟೆಯಲ್ಲಿಟ್ಟು ಪರೀಕ್ಷಿಸಿದಾಗ ಎಷ್ಟು ಮೊಳಕೆಯೊಡೆದಿವೆ ಎಂಬುದನ್ನು ಸ್ಲೈಡರ್‌ನಲ್ಲಿ ನಮೂದಿಸಿ:"
            if is_kn else
            "Simulate testing 100 seeds on a damp cloth/paper to check germination vigor:"
        )

        germ_sprouted = st.slider(
            "100 ರಲ್ಲಿ ಮೊಳಕೆಯೊಡೆದ ಬೀಜಗಳ ಸಂಖ್ಯೆ" if is_kn else "Number of seeds sprouted (out of 100)",
            min_value=0, max_value=100, value=86, key="demo_germ_slider"
        )
        pct = germ_sprouted

        if pct >= 85:
            st.success(
                f"✅ **{pct}% {'ಮೊಳಕೆ ಪ್ರಮಾಣ - ಅತ್ಯುತ್ತಮ ಗುಣಮಟ್ಟದ ಬೀಜ' if is_kn else 'Germination - High Vigor Seed'}**\n\n" +
                ("ಈ ಬೀಜ ಅತ್ಯುತ್ತಮವಾಗಿದ್ದು, ಶಿಫಾರಸು ಮಾಡಿದ ಸಾಮಾನ್ಯ ಪ್ರಮಾಣದಲ್ಲಿ ಬಿತ್ತನೆ ಮಾಡಬಹುದು." if is_kn else "Excellent seed vigor. You can proceed with standard sowing rates.")
            )
        elif pct >= 70:
            st.warning(
                f"⚠️ **{pct}% {'ಮೊಳಕೆ ಪ್ರಮಾಣ - ಸಾಧಾರಣ ಬೀಜ' if is_kn else 'Germination - Acceptable Vigor'}**\n\n" +
                ("ಧಾನ್ಯ ಮತ್ತು ಬೇಳೆಕಾಳುಗಳಿಗೆ ಇದು ಸ್ವೀಕಾರಾರ್ಹ. ಆದರೆ ಹೊಲದಲ್ಲಿ ಸರಿಯಾದ ಸಾಂದ್ರತೆಗಾಗಿ ಬಿತ್ತನೆ ಬೀಜದ ಪ್ರಮಾಣವನ್ನು 15% ಹೆಚ್ಚಿಸಿ." if is_kn else "Acceptable for cereals and pulses. Increase seed rate by 15% to maintain plant density.")
            )
        else:
            st.error(
                f"❌ **{pct}% {'ಮೊಳಕೆ ಪ್ರಮಾಣ - ಕಳಪೆ ಗುಣಮಟ್ಟದ ಬೀಜ' if is_kn else 'Germination - Weak/Unusable Seed'}**\n\n" +
                ("ಈ ಬೀಜವನ್ನು ಬಿತ್ತನೆ ಮಾಡಬೇಡಿ! ಬೀಜ ಮಾರಾಟಗಾರರಿಂದ ಬದಲಾಯಿಸಿಕೊಳ್ಳಿ ಅಥವಾ ಹೊಸ ಬೀಜ ಖರೀದಿಸಿ." if is_kn else "Do not sow this seed. Sprouting rate is too low. Replace the seed batch.")
            )

    ui.page_link("views/season_planner.py", "ಋತು ಯೋಜಕ ಪುಟಕ್ಕೆ ಹೋಗಿ" if is_kn else "Go to Season Planner Page", "🗓️")


# ==========================================
# TAB 4: WEATHER PRECAUTIONS
# ==========================================
with t4:
    st.subheader("ಹವಾಮಾನ ರಕ್ಷಣೆ {Weather Precautions} ಹೇಗೆ ಬಳಸುವುದು?" if is_kn else "How to use Weather Precautions")
    if is_kn:
        st.markdown(
            "ಕರ್ನಾಟಕದ ಎಲ್ಲಾ 31 ಜಿಲ್ಲೆಗಳ 7 ದಿನಗಳ ಹವಾಮಾನ ಮುನ್ಸೂಚನೆಯನ್ನು ಪರಿಶೀಲಿಸಿ ನಿಮ್ಮ ಕೃಷಿ ಕೆಲಸಗಳನ್ನು ಯೋಜಿಸಲು ಈ ಪುಟ ಸಹಾಯ ಮಾಡುತ್ತದೆ.\n\n"
            "**ಔಷಧ ಸಿಂಪಡಣೆಯ 3 ಮುಖ್ಯ ನಿಯಮಗಳು:**\n"
            "- 🌧️ **ಮಳೆ ಮುನ್ನೆಚ್ಚರಿಕೆ:** 24 ಗಂಟೆಗಳಲ್ಲಿ 2.5 ಮಿ.ಮೀ. ಗಿಂತ ಹೆಚ್ಚು ಮಳೆಯ ಸಂಭವವಿದ್ದರೆ ಯಾವುದೇ ಕೀಟನಾಶಕ ಅಥವಾ ಗೊಬ್ಬರ ಸಿಂಪಡಿಸಬೇಡಿ. ಮಳೆಗೆ ಔಷಧ ತೊಳೆದುಹೋಗಿ ಹಣ ವ್ಯರ್ಥವಾಗುತ್ತದೆ.\n"
            "- 💨 **ಗಾಳಿಯ ರಭಸ:** ಗಾಳಿಯ ವೇಗ ಗಂಟೆಗೆ 30 ಕಿ.ಮೀ. ದಾಟಿದ್ದರೆ ಸಿಂಪಡಿಸಬೇಡಿ. ಔಷಧವು ಗಾಳಿಗೆ ಹಾರಿ ಅಕ್ಕಪಕ್ಕದ ಬೆಳೆಗಳಿಗೆ ಮತ್ತು ಜೇನುನೊಣಗಳಿಗೆ ಹಾನಿಯುಂಟುಮಾಡುತ್ತದೆ.\n"
            "- ⏰ **ಉತ್ತಮ ಸಮಯ:** ಸಿಂಪಡಣೆಯನ್ನು ಬೆಳಿಗ್ಗೆ 11 ಗಂಟೆಯ ಒಳಗೆ ಅಥವಾ ಸಂಜೆ 3 ಗಂಟೆಯ ನಂತರ ಮಾತ್ರ ಮಾಡಿ. ಮಧ್ಯಾಹ್ನದ ಬಿಸಿಲಿನಲ್ಲಿ ಔಷಧ ಬೇಗ ಆವಿಯಾಗುತ್ತದೆ."
        )
    else:
        st.markdown(
            "This view checks live 7-day weather forecasts for all 31 Karnataka districts and gives clear safety triggers for field operations.\n\n"
            "**3 Vital Rules for Spraying:**\n"
            "- 🌧️ **Rain Warning:** Do not spray if rain >= 2.5 mm is expected within 24 hours. Rain washes off chemicals.\n"
            "- 💨 **Wind Gusts:** Do not spray when wind gusts reach 30 km/h or higher. Spray drift damages adjacent crops, pollinators, and human health.\n"
            "- ⏰ **Safe Window:** Spray strictly before 11:00 AM or after 3:00 PM. Avoid hot mid-day sun to prevent chemical burn and rapid evaporation."
        )

    # Interactive Demo Box for Weather Precautions
    with st.container(border=True):
        st.markdown(f"**🎮 {'ನೇರ ಡೆಮೊ: ಹವಾಮಾನ ಮುನ್ನೆಚ್ಚರಿಕೆ ಸನ್ನಿವೇಶಗಳು' if is_kn else 'Live Demo: Weather Warning Scenarios'}**")
        st.caption(
            "ವಿವಿಧ ಹವಾಮಾನ ಪರಿಸ್ಥಿತಿಗಳನ್ನು ಪರೀಕ್ಷಿಸಿ ಮತ್ತು ಆ್ಯಪ್ ನೀಡುವ ಸುರಕ್ಷತಾ ಎಚ್ಚರಿಕೆಗಳನ್ನು ನೋಡಿ:"
            if is_kn else
            "Switch between weather conditions to see automated hazard detection in action:"
        )

        weather_choice = st.radio(
            "ಹವಾಮಾನ ಸನ್ನಿವೇಶ ಆಯ್ಕೆಮಾಡಿ" if is_kn else "Select weather condition",
            [
                "ಮಳೆ ಮತ್ತು ಗಾಳಿಯ ಮುನ್ನೆಚ್ಚರಿಕೆ (ಅಪಾಯದ ದಿನ)" if is_kn else "Heavy Rain & Wind Hazard (Unsafe to Spray)",
                "ಶಾಂತ ಮತ್ತು ಒಣ ಹವೆ (ಸಿಂಪಡಣೆಗೆ ಉತ್ತಮ ದಿನ)" if is_kn else "Calm & Dry Weather (Optimal Spray Day)",
            ],
            key="demo_weather_choice"
        )

        if "ಮಳೆ" in weather_choice or "Heavy Rain" in weather_choice:
            st.warning(
                ("⚠️ **ಭಾರಿ ಮಳೆ ಮತ್ತು ಗಾಳಿ ಎಚ್ಚರಿಕೆ:** ಮಳೆ: 42 ಮಿ.ಮೀ., ಗಾಳಿ: 38 ಕಿ.ಮೀ./ಗಂ.\n\n"
                 "👉 **ಸಲಹೆ:** ಇಂದು ಯಾವುದೇ ಸಿಂಪಡಣೆ ಮಾಡಬೇಡಿ! ಹೊಲದಲ್ಲಿ ನೀರು ನಿಲ್ಲದಂತೆ ಬಸಿಗಾಲುವೆಗಳನ್ನು ಸಿದ್ಧಪಡಿಸಿ.")
                if is_kn else
                ("⚠️ **Heavy Rain & Wind Hazard:** Rain: 42 mm, Wind Gusts: 38 km/h.\n\n"
                 "👉 **Action:** Postpone all chemical spraying! Clear field drainage channels to prevent waterlogging.")
            )
        else:
            st.success(
                ("✅ **ಶಾಂತ ಹವಾಮಾನ:** ಮಳೆ: 0 ಮಿ.ಮೀ., ಗಾಳಿ: 12 ಕಿ.ಮೀ./ಗಂ.\n\n"
                 "👉 **ಸಲಹೆ:** ಸಿಂಪಡಣೆಗೆ ಇಂದು ಅತ್ಯಂತ ಅನುಕೂಲಕರ ದಿನ. ಬೆಳಿಗ್ಗೆ 11 ರ ಮೊದಲು ಅಥವಾ ಸಂಜೆ 3 ರ ನಂತರ ಸಿಂಪಡಣೆ ಪೂರ್ಣಗೊಳಿಸಿ.")
                if is_kn else
                ("✅ **Calm & Dry Window:** Rain: 0 mm, Wind: 12 km/h.\n\n"
                 "👉 **Action:** Optimal day for spraying. Complete spray before 11:00 AM or after 3:00 PM.")
            )

    ui.page_link("views/weather.py", "ಹವಾಮಾನ ಮುನ್ನೆಚ್ಚರಿಕೆ ಪುಟಕ್ಕೆ ಹೋಗಿ" if is_kn else "Go to Weather Precautions Page", "⛈️")


# ==========================================
# TAB 5: SCHEMES & HELP
# ==========================================
with t5:
    st.subheader("ಸರ್ಕಾರಿ ಯೋಜನೆಗಳು & ಸಹಾಯ {Schemes & Help} ಹೇಗೆ ಬಳಸುವುದು?" if is_kn else "How to use Schemes & Help")
    if is_kn:
        st.markdown(
            "ಕೃಷಿ ಇಲಾಖೆಯ ಪ್ರಮುಖ ಯೋಜನೆಗಳಾದ ಬೆಳೆ ವಿಮೆ, ಆದಾಯ ಬೆಂಬಲ ಮತ್ತು ಕಡಿಮೆ ಬಡ್ಡಿದರದ ಸಾಲಗಳ ವಿವರ ಮತ್ತು ಅರ್ಜಿ ಸಲ್ಲಿಸುವ ಹಂತಗಳನ್ನು ಇಲ್ಲಿ ಪಡೆಯಬಹುದು.\n\n"
            "**ಪ್ರಮುಖ ಯೋಜನೆಗಳ ವಿವರ:**\n"
            "- 🛡️ **ಬೆಳೆ ವಿಮೆ {PMFBY}:** ಖಾರಿಫ್ ಬೆಳೆಗಳಿಗೆ ಕೇವಲ 2%, ರಬಿ ಬೆಳೆಗಳಿಗೆ 1.5% ಪ್ರೀಮಿಯಂ. ಪ್ರವಾಹ ಅಥವಾ ಆಲಿಕಲ್ಲು ಮಳೆಯಿಂದ ಬೆಳೆ ಹಾನಿಯಾದರೆ "
            "**72 ಗಂಟೆಗಳೊಳಗೆ ಸಹಾಯವಾಣಿ {14447} ಅಥವಾ ಕ್ರಾಪ್ ಇನ್ಶೂರೆನ್ಸ್ ಆ್ಯಪ್ ಮೂಲಕ ವರದಿ ಮಾಡುವುದು ಕಡ್ಡಾಯ.**\n"
            "- 💰 **ಪಿಎಂ-ಕಿಸಾನ್ {PM-KISAN}:** ವಾರ್ಷಿಕ ₹6,000 ಆದಾಯ ಬೆಂಬಲ (ಪ್ರತಿ 4 ತಿಂಗಳಿಗೊಮ್ಮೆ ₹2,000). {e-KYC} ಕಡ್ಡಾಯ.\n"
            "- 💳 **ಕಿಸಾನ್ ಕ್ರೆಡಿಟ್ ಕಾರ್ಡ್ {KCC}:** ಸಮಯಕ್ಕೆ ಸರಿಯಾಗಿ ಸಾಲ ಮರುಪಾವತಿ ಮಾಡಿದರೆ ಕೇವಲ 4% ಬಡ್ಡಿದರದಲ್ಲಿ ಕೃಷಿ ಸಾಲ.\n"
            "- 🧪 **ಮಣ್ಣು ಆರೋಗ್ಯ ಕಾರ್ಡ್ {Soil Health Card}:** ನಿಮ್ಮ ಮಣ್ಣಿನ 12 ಪೋಷಕಾಂಶಗಳ ಉಚಿತ ಪ್ರಯೋಗಾಲಯ ಪರೀಕ್ಷೆ."
        )
    else:
        st.markdown(
            "Access clear requirements, document checklists, and application steps for major agricultural schemes and subsidies.\n\n"
            "**Key Schemes Covered:**\n"
            "- 🛡️ **Crop Insurance (PMFBY):** Subsidized premium (2% Kharif, 1.5% Rabi). If crops are damaged by localized flooding or hail, "
            "**report within 72 hours via toll-free 14447 or the Crop Insurance App.**\n"
            "- 💰 **PM-KISAN:** Rs. 6,000 annual income support in 3 equal installments. eKYC is mandatory.\n"
            "- 💳 **Kisan Credit Card (KCC):** Short-term crop loans at an effective 4% interest rate with prompt repayment.\n"
            "- 🧪 **Soil Health Card:** Free laboratory analysis of 12 soil nutrient parameters every 3 years."
        )

    # Interactive Demo Box for Document Checklist
    with st.container(border=True):
        st.markdown(f"**🎮 {'ನೇರ ಡೆಮೊ: ದಾಖಲೆಗಳ ಸಿದ್ಧತೆ ಪರಿಶೀಲನೆ' if is_kn else 'Live Demo: Document Readiness Checklist'}**")
        st.caption(
            "ಯೋಜನೆಗಳಿಗೆ ಅರ್ಜಿ ಸಲ್ಲಿಸಲು ನಿಮ್ಮ ಬಳಿ ಇರುವ ದಾಖಲೆಗಳನ್ನು ಗುರುತು ಮಾಡಿ ಸಿದ್ಧತೆ ಪರೀಕ್ಷಿಸಿ:"
            if is_kn else
            "Tick off the documents you have ready to see your application readiness score:"
        )

        doc1 = st.checkbox("ಆಧಾರ್ ಕಾರ್ಡ್ (ಬ್ಯಾಂಕ್ ಖಾತೆಗೆ ಲಿಂಕ್ ಆಗಿರಬೇಕು)" if is_kn else "Aadhaar Card (linked to active bank account)", value=True, key="demo_doc1")
        doc2 = st.checkbox("ಜಮೀನಿನ ಪಹಣಿ / {RTC} (ಭೂಮಿ ಪೋರ್ಟಲ್‌ನಿಂದ)" if is_kn else "Land Record / RTC (from Bhoomi portal)", value=True, key="demo_doc2")
        doc3 = st.checkbox("ಬ್ಯಾಂಕ್ ಪಾಸ್‌ಬುಕ್ ಅಥವಾ ರದ್ದಾದ ಚೆಕ್" if is_kn else "Bank passbook or cancelled cheque", value=True, key="demo_doc3")
        doc4 = st.checkbox("ಬಿತ್ತನೆ ದೃಢೀಕರಣ ಪತ್ರ {Sowing Certificate}" if is_kn else "Sowing certificate or self-declaration", value=False, key="demo_doc4")

        ready_count = sum([doc1, doc2, doc3, doc4])
        st.progress(ready_count / 4.0)

        if ready_count == 4:
            st.success("🎉 " + ("ಅತ್ಯುತ್ತಮ! ನಿಮ್ಮ ಎಲ್ಲಾ 4 ದಾಖಲೆಗಳು ಸಿದ್ಧವಾಗಿವೆ. ನೀವು ಅರ್ಜಿ ಸಲ್ಲಿಸಬಹುದು." if is_kn else "All 4 documents ready! You are fully prepared to apply."))
        else:
            st.info(f"📋 {ready_count}/4 " + ("ದಾಖಲೆಗಳು ಸಿದ್ಧವಾಗಿವೆ. ಬಾಕಿ ಇರುವ ದಾಖಲೆಗಳನ್ನು ಸಂಗ್ರಹಿಸಿ." if is_kn else "documents ready. Collect remaining documents before visiting the centre."))

    ui.page_link("views/schemes.py", "ಯೋಜನೆಗಳು ಮತ್ತು ಸಹಾಯ ಪುಟಕ್ಕೆ ಹೋಗಿ" if is_kn else "Go to Schemes & Help Page", "📋")


# ==========================================
# TAB 6: SECURITY & PRIVACY
# ==========================================
with t6:
    st.subheader("ಖಾತೆ ಸುರಕ್ಷತೆ ಮತ್ತು ಗೌಪ್ಯತೆ {Security & Privacy}" if is_kn else "Account Security & Privacy")
    if is_kn:
        st.markdown(
            "ರೈತರ ಖಾತೆ ಸುರಕ್ಷತೆ ಮತ್ತು ಗೌಪ್ಯತೆಯನ್ನು ಕೃಷಿನುಡಿ {KrushiNudi} ಅತ್ಯಂತ ಗಂಭೀರವಾಗಿ ಪರಿಗಣಿಸುತ್ತದೆ:\n\n"
            "- 🔓 **ಸುಲಭ ಪ್ರವೇಶ:** ರೈತರು ಯಾವುದೇ ಲಾಗಿನ್ ಅಥವಾ ಖಾತೆ ಇಲ್ಲದೆ ಆ್ಯಪ್‌ನ ಎಲ್ಲಾ ಸೇವೆಗಳನ್ನು ತಕ್ಷಣ ಉಚಿತವಾಗಿ ಬಳಸಬಹುದು.\n"
            "- 🛡️ **ಶಾಶ್ವತ ಖಾತೆ ಸಂಗ್ರಹಣೆ:** ಖಾತೆ ಸಕ್ರಿಯಗೊಳಿಸಿದಾಗ ನಿಮ್ಮ ವಿವರಗಳನ್ನು ಶಾಶ್ವತ ಡೇಟಾಬೇಸ್‌ನಲ್ಲಿ {SQLite} ಸುರಕ್ಷಿತವಾಗಿಡಲಾಗುತ್ತದೆ. "
            "ಆ್ಯಪ್ ನವೀಕರಣವಾದರೂ ನಿಮ್ಮ ನೋಂದಣಿ ವಿವರಗಳು ಎಂದಿಗೂ ಅಳಿಸಿಹೋಗುವುದಿಲ್ಲ.\n"
            "- ⏱️ **30 ನಿಮಿಷಗಳ ಸ್ವಯಂ ಲಾಗೌಟ್:** ಗ್ರಾಮದ ಸಾಮಾನ್ಯ ಸೇವಾ ಕೇಂದ್ರಗಳಲ್ಲಿ ಅಥವಾ ಕುಟುಂಬದ ಇತರರು ನಿಮ್ಮ ಮೊಬೈಲ್ ಬಳಸುವಾಗ ನಿಮ್ಮ ಖಾತೆಯನ್ನು "
            "ಸುರಕ್ಷಿತವಾಗಿಡಲು 30 ನಿಮಿಷಗಳ ನಿಷ್ಕ್ರಿಯತೆಯ ನಂತರ ಅಧಿವೇಶನವು ಸ್ವಯಂಚಾಲಿತವಾಗಿ ಮುಕ್ತಾಯಗೊಳ್ಳುತ್ತದೆ.\n"
            "- 📱 **ಮೊಬೈಲ್ {SMS OTP} ಭದ್ರತೆ:** ಪಾಸ್‌ವರ್ಡ್ ಮರೆತರೆ {Fast2SMS} ಸೆಲ್ಯುಲಾರ್ ಗೇಟ್‌ವೇ ಮೂಲಕ ನಿಮ್ಮ ಅಧಿಕೃತ ಮೊಬೈಲ್ ಸಂಖ್ಯೆಗೆ ನೇರ {SMS} ಬರುತ್ತದೆ.\n"
            "- 🔒 **ಗೌಪ್ಯತೆ ರಕ್ಷಣೆ:**\n"
            "  - ರಹಸ್ಯ {OTP} ಕೋಡ್ ಅನ್ನು ವೆಬ್ ಪರದೆಯ ಮೇಲೆ ಎಂದಿಗೂ ಪ್ರದರ್ಶಿಸಲಾಗುವುದಿಲ್ಲ.\n"
            "  - ನಿಮ್ಮ ಮೊಬೈಲ್ ಸಂಖ್ಯೆಯನ್ನು ಗೌಪ್ಯವಾಗಿ ಮುಚ್ಚಿಡಲಾಗುತ್ತದೆ (`98******10`).\n"
            "  - ಫೋಟೋ ವಿಶ್ಲೇಷಣೆ ನಡೆಸುವ ಮುನ್ನ ಜಿಪಿಎಸ್ ಸ್ಥಳದ ಮಾಹಿತಿಯನ್ನು {GPS Metadata} ಸಂಪೂರ್ಣವಾಗಿ ಅಳಿಸಿಹಾಕಲಾಗುತ್ತದೆ ಮತ್ತು ಫೋಟೋಗಳನ್ನು ಆ್ಯಪ್‌ನಲ್ಲಿ ಸಂಗ್ರಹಿಸುವುದಿಲ್ಲ."
        )
    else:
        st.markdown(
            "KrushiNudi enforces enterprise-grade security and strict farmer privacy protections:\n\n"
            "- 🔓 **Frictionless Access:** No login or account registration is required to use all advisory features.\n"
            "- 🛡️ **Permanent Account Persistence:** When login is activated, accounts are secured in a persistent SQLite database (`kisan_users.db`). "
            "Your login credentials never expire or get wiped during application redeployments.\n"
            "- ⏱️ **30-Minute Inactivity Auto-Logout:** Protects your account when accessing the app on shared devices or at village Common Service Centres.\n"
            "- 📱 **Cellular SMS OTP Password Recovery:** Fast2SMS cellular SMS gateway delivers real-time one-time passwords directly to your mobile phone.\n"
            "- 🔒 **Privacy Guarantees:**\n"
            "  - OTPs are strictly confidential and never displayed on the web application UI.\n"
            "  - Mobile numbers are masked for data protection (`98******10`).\n"
            "  - Plant photo analysis strips GPS coordinates before processing, and no farmer photos are stored permanently."
        )

    ui.page_link("views/about.py", "ಬಗ್ಗೆ ಮತ್ತು ಗೌಪ್ಯತೆ ಪುಟಕ್ಕೆ ಹೋಗಿ" if is_kn else "Go to About & Privacy Page", "ℹ️")

st.markdown("---")

# --- FREQUENTLY ASKED QUESTIONS ---
st.subheader("ಸಾಮಾನ್ಯ ಪ್ರಶ್ನೆಗಳು {FAQ}" if is_kn else "Frequently Asked Questions")

with st.expander("ಈ ಆ್ಯಪ್ ಉಚಿತವೇ? / Is this app free?" if is_kn else "Is KrushiNudi free to use?"):
    st.write(
        "ಹೌದು, ಕೃಷಿನುಡಿ {KrushiNudi} ಕರ್ನಾಟಕದ ರೈತರಿಗಾಗಿ ಸಂಪೂರ್ಣ ಉಚಿತವಾಗಿದೆ. ಇದರಲ್ಲಿ ಯಾವುದೇ ಜಾಹೀರಾತುಗಳಿಲ್ಲ."
        if is_kn else
        "Yes, KrushiNudi is completely free for all farmers. It contains no advertisements and charges no fees."
    )

with st.expander("ಕನ್ನಡ ಮತ್ತು ಇಂಗ್ಲಿಷ್ ಭಾಷೆ ಬದಲಾಯಿಸುವುದು ಹೇಗೆ? / How to switch languages?"):
    st.write(
        "ಆ್ಯಪ್‌ನ ಎಡಭಾಗದ ಸೈಡ್‌ಬಾರ್‌ನಲ್ಲಿರುವ 'Language / ಭಾಷೆ' ಆಯ್ಕೆಯ ಮೂಲಕ ನೀವು ಯಾವುದೇ ಸಮಯದಲ್ಲಿ ಕನ್ನಡ ಅಥವಾ ಇಂಗ್ಲಿಷ್‌ಗೆ ಬದಲಾಯಿಸಬಹುದು."
        if is_kn else
        "Use the 'Language / ಭಾಷೆ' toggle in the left sidebar to switch between Kannada and English at any moment."
    )

with st.expander("ರಾಸಾಯನಿಕಗಳ ನಿಖರ ಪ್ರಮಾಣವನ್ನು ಆ್ಯಪ್ ಏಕೆ ನೀಡುವುದಿಲ್ಲ? / Why does the app not give chemical doses?"):
    st.write(
        "ರಾಸಾಯನಿಕಗಳ ಪ್ರಮಾಣವು ಹೊಲದ ಮಣ್ಣು, ಬೆಳೆಯ ವಯಸ್ಸು ಮತ್ತು ಸ್ಥಳೀಯ ಹವಾಮಾನವನ್ನು ಅವಲಂಬಿಸಿರುತ್ತದೆ. ತಪ್ಪಾದ ಪ್ರಮಾಣವು ಬೆಳೆಗೆ ಮತ್ತು ಮಾನವನ ಆರೋಗ್ಯಕ್ಕೆ "
        "ಹಾನಿ ಉಂಟುಮಾಡಬಹುದು. ಆದ್ದರಿಂದ ಯಾವಾಗಲೂ ಉತ್ಪನ್ನದ ಅಧಿಕೃತ ಲೇಬಲ್ ಅಥವಾ ಕೃಷಿ ಅಧಿಕಾರಿಯಿಂದ ಪ್ರಮಾಣವನ್ನು ಖಚಿತಪಡಿಸಿಕೊಳ್ಳಿ."
        if is_kn else
        "Pesticide dosages depend on crop age, formulation, and soil conditions. Wrong doses can damage crops and endanger health. Always consult the product label or your local agriculture officer."
    )

with st.expander("ತುರ್ತು ಕೃಷಿ ಸಹಾಯಕ್ಕೆ ಯಾರನ್ನು ಸಂಪರ್ಕಿಸಬೇಕು? / Emergency Agriculture Helpline"):
    st.markdown(
        "📞 **ಕಿಸಾನ್ ಕಾಲ್ ಸೆಂಟರ್ {Kisan Call Centre}:** ಉಚಿತ ಟೋಲ್-ಫ್ರೀ ಸಂಖ್ಯೆ `1800-180-1551`\n\n"
        "🏛️ ನಿಮ್ಮ ಹತ್ತಿರದ **ರೈತ ಸಂಪರ್ಕ ಕೇಂದ್ರ {RSK}** ಅಥವಾ **ಕೃಷಿ ವಿಜ್ಞಾನ ಕೇಂದ್ರ {KVK}** ಕ್ಕೆ ಭೇಟಿ ನೀಡಿ."
        if is_kn else
        "📞 **Kisan Call Centre:** Toll-free `1800-180-1551`\n\n"
        "🏛️ Visit your nearest **Raitha Samparka Kendra (RSK)** or **Krishi Vigyan Kendra (KVK)**."
    )

# --- FEEDBACK & FOOTER ---
ui.feedback_box()
st.markdown("---")
footer_str = (
    "© 2026 ಅಭಿಷೇಕ್ ಹಿಟಬುತ್ತಿ. ಎಲ್ಲ ಹಕ್ಕುಗಳನ್ನು ಕಾಯ್ದಿರಿಸಲಾಗಿದೆ. ಅನುಮತಿ ಇಲ್ಲದೆ ಈ ಆ್ಯಪ್ ಅನ್ನು ನಕಲು ಮಾಡುವುದು ಅಥವಾ ಮರುಬಳಕೆ ಮಾಡುವುದು ನಿಷಿದ್ಧ."
    if is_kn else
    "© 2026 Abhishek Hitabutti. All rights reserved. Copying or reuse of this app without permission is prohibited."
)
st.caption(footer_str)
