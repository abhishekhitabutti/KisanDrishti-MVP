"""Borewell Water Advisory & Depth Estimator for KrushiNudi.
Provides scientific groundwater feasibility, depth ranges, and risk prevention for Karnataka farmers.
Fully bilingual: 100% pure Kannada localization with technical terms in braces {...}.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import streamlit as st
import i18n
import ui
from borewell_model import calculate_borewell_feasibility
from districts import DISTRICTS, DISTRICTS_KN
from i18n import t

is_kn = (i18n.current_lang() == "kn")

# --- HERO SECTION ---
hero_title = "ಬೋರ್‌ವೆಲ್ ನೀರು ಲಭ್ಯತೆ & ಆಳ ಅಂದಾಜು" if is_kn else "Borewell Water Advisory"
hero_sub = (
    "ಕೇಂದ್ರ ಅಂತರ್ಜಲ ಮಂಡಳಿ {CGWB} ವರದಿಗಳು ಮತ್ತು ಸ್ಥಳೀಯ ಭೂಲಕ್ಷಣದ ಆಧಾರದ ಮೇಲೆ ವೈಜ್ಞಾನಿಕ ಆಳ, ಸಂಭವನೀಯತೆ ಮತ್ತು ವೆಚ್ಚದ ಅಂದಾಜು."
    if is_kn else
    "Scientific groundwater strike depth, feasibility probability, and financial budgeting based on CGWB data."
)
ui.hero(hero_title, hero_sub, "💧")

st.markdown(
    "💡 *" +
    ("ರೈತರು ಕಣ್ಣುಮುಚ್ಚಿ ಬೋರ್‌ವೆಲ್ ಕೊರೆದು ಸಾಲದ ಸುಳಿಗೆ ಸಿಲುಕುವುದನ್ನು ತಡೆಯಲು ಈ ವೈಜ್ಞಾನಿಕ ಮಾರ್ಗದರ್ಶಿ ರೂಪಿಸಲಾಗಿದೆ."
     if is_kn else
     "Designed to protect smallholder farmers from blind drilling and debt traps through scientific risk assessment.") +
    "*"
)

# --- INPUT SECTION ---
st.subheader("ನಿಮ್ಮ ಜಮೀನಿನ ವಿವರಗಳು" if is_kn else "Your Field & Location Details")

c1, c2 = st.columns(2)

with c1:
    # District Selection
    if is_kn:
        d_keys = sorted(DISTRICTS_KN.keys(), key=lambda x: DISTRICTS_KN[x])
        kn_names = [DISTRICTS_KN[k] for k in d_keys]
        default_idx = kn_names.index("ಬೆಳಗಾವಿ") if "ಬೆಳಗಾವಿ" in kn_names else 0
        sel_kn = st.selectbox("ನಿಮ್ಮ ಜಿಲ್ಲೆ {District}", kn_names, index=default_idx)
        district = d_keys[kn_names.index(sel_kn)]
    else:
        district_list = sorted(DISTRICTS.keys())
        default_idx = district_list.index("Belagavi") if "Belagavi" in district_list else 0
        district = st.selectbox("Your District", district_list, index=default_idx)

    # Topography Selection
    topo_options = {
        "plain": "ಸಾಮಾನ್ಯ ಬಯಲು / ಇಳಿಜಾರು ಜಮೀನು {Mid-slope / Plain}" if is_kn else "Mid-slope / Plain Ground",
        "valley": "ಕಣಿವೆ / ತಗ್ಗು ಪ್ರದೇಶ {Valley / Lowland - High Recharge}" if is_kn else "Valley / Lowland (Natural drainage)",
        "upland": "ಗುಡ್ಡಗಾಡು / ಎತ್ತರದ ಜಮೀನು {Upland / Ridge - High Runoff}" if is_kn else "Upland / Ridge (Fast runoff)",
    }
    topo_choice = st.selectbox(
        "ಭೂಮಿಯ ಇಳಿಜಾರು / ಲಕ್ಷಣ {Topography}" if is_kn else "Land Topography",
        list(topo_options.keys()),
        format_func=lambda x: topo_options[x],
        index=0
    )

    # Soil type
    soil_options = {
        "red": "ಕೆಂಪು ಮರಳು ಮಿಶ್ರಿತ ಗೋಡು ಮಣ್ಣು {Red Sandy Loam}" if is_kn else "Red Sandy Loam",
        "black": "ಆಳವಾದ ಕಪ್ಪು ಜೇಡಿ ಮಣ್ಣು {Deep Black Cotton Soil}" if is_kn else "Deep Black Clay Soil",
        "laterite": "ಜಂಬಿಟ್ಟಿಗೆ ಕೆಂಪು ಕಲ್ಲು ಮಣ್ಣು {Laterite Soil}" if is_kn else "Laterite Crust Soil",
        "alluvial": "ನದಿ ಬಯಲಿನ ಮೆಕ್ಕಲು ಮಣ್ಣು {River Basin Alluvial}" if is_kn else "River Alluvial Soil",
    }
    soil_choice = st.selectbox(
        "ಮಣ್ಣಿನ ವಿಧ {Soil Type}" if is_kn else "Soil Profile",
        list(soil_options.keys()),
        format_func=lambda x: soil_options[x],
        index=0
    )

with c2:
    # Nearby empirical data (Crucial local ground truth)
    st.markdown("**ಸ್ಥಳೀಯ ಬೋರ್‌ವೆಲ್ ಅನುಭವ {Nearby Ground Truth}**" if is_kn else "**Nearby Borewell History (500m radius)**")
    working_wells = st.slider(
        "500 ಮೀಟರ್ ಒಳಗೆ ನೀರು ಬರುತ್ತಿರುವ ಬೋರ್‌ವೆಲ್‌ಗಳು" if is_kn else "Functioning borewells within 500m",
        min_value=0, max_value=5, value=1
    )
    dry_wells = st.slider(
        "500 ಮೀಟರ್ ಒಳಗೆ ವಿಫಲವಾದ / ಬತ್ತಿದ ಬೋರ್‌ವೆಲ್‌ಗಳು" if is_kn else "Dry or failed borewells within 500m",
        min_value=0, max_value=5, value=0
    )
    water_body = st.checkbox(
        "500 ಮೀಟರ್ ವ್ಯಾಪ್ತಿಯಲ್ಲಿ ಕೆರೆ, ಹಳ್ಳ ಅಥವಾ ನೀರಾವರಿ ಕಾಲುವೆ ಇದೆ" if is_kn else "Lake, perennial stream, pond or irrigation canal within 500m",
        value=False
    )

# --- RUN CALCULATION ---
res = calculate_borewell_feasibility(
    district=district,
    topography=topo_choice,
    nearby_working=working_wells,
    nearby_dry=dry_wells,
    has_water_body=water_body,
    soil_type=soil_choice,
)

st.markdown("---")
st.subheader("ವೈಜ್ಞಾನಿಕ ಸಾಧ್ಯತೆ ಮತ್ತು ಆಳದ ವರದಿ" if is_kn else "Scientific Feasibility & Depth Report")

# --- STATS ROW ---
col_m1, col_m2, col_m3 = st.columns(3)
with col_m1:
    with st.container(border=True):
        st.markdown(f"**{'ಅಂದಾಜು ಕೊರೆಯುವ ಆಳ' if is_kn else 'Recommended Depth Range'}**")
        st.markdown(f"### {res['est_min_ft']} - {res['est_max_ft']} {'ಅಡಿ {ft}' if is_kn else 'feet'}")
        st.caption(f"{int(res['est_min_ft']*0.3048)} - {int(res['est_max_ft']*0.3048)} ಮೀಟರ್ {int(res['est_min_ft']*0.3048)}-{int(res['est_max_ft']*0.3048)}m" if is_kn else f"{int(res['est_min_ft']*0.3048)} - {int(res['est_max_ft']*0.3048)} meters")

with col_m2:
    with st.container(border=True):
        st.markdown(f"**{'ನೀರು ಸಿಗುವ ಸಂಭವನೀಯತೆ' if is_kn else 'Success Probability'}**")
        st.markdown(f"### {res['final_prob']}%")
        st.caption(res["prob_category_kn"] if is_kn else res["prob_category"])

with col_m3:
    with st.container(border=True):
        st.markdown(f"**{'ಅಂತರ್ಜಲ ಬಳಕೆ ವರ್ಗ' if is_kn else 'CGWB Taluk Status'}**")
        st.markdown(f"### {res['cgwb_status_kn'].split('{')[0].strip() if is_kn else res['cgwb_status']}")
        st.caption(f"ಬಳಕೆ ಪ್ರಮಾಣ: {res['extraction_pct']}%" if is_kn else f"Extraction: {res['extraction_pct']}%")

# --- FINANCIAL & BUDGETING METRIC ---
with st.container(border=True):
    bcol1, bcol2 = st.columns([2, 1])
    with bcol1:
        st.markdown(f"**💰 {'ಅಂದಾಜು ಒಟ್ಟು ಹೂಡಿಕೆ ವೆಚ್ಚ' if is_kn else 'Estimated Investment Budget'}**")
        st.write(
            f"ಕೊರೆಯುವ ವೆಚ್ಚ, {res['casing_ft']} ಅಡಿ ಕೇಸಿಂಗ್ ಪೈಪ್ {res['casing_ft']}ft casing, ಸಬ್‌ಮರ್ಸಿಬಲ್ ಪಂಪ್ ಮತ್ತು ವಿದ್ಯುತ್ ಸಂಪರ್ಕ ಒಳಗೊಂಡಂತೆ:\n"
            f"**₹{res['total_cost_min']:,} ರಿಂದ ₹{res['total_cost_max']:,}**"
            if is_kn else
            f"Includes drilling charges, {res['casing_ft']} ft heavy casing pipe, submersible pump set, and electrical fitting:\n"
            f"**₹{res['total_cost_min']:,} to ₹{res['total_cost_max']:,}**"
        )
    with bcol2:
        if res["final_prob"] >= 70:
            st.success("✅ " + ("ಕೊರೆಯಲು ಅನುಕೂಲಕರ ಸನ್ನಿವೇಶ" if is_kn else "Favorable Hydrogeology"))
        elif res["final_prob"] >= 48:
            st.warning("⚠️ " + ("ಮಧ್ಯಮ ಅಪಾಯ - ಎಚ್ಚರಿಕೆ ಅಗತ್ಯ" if is_kn else "Moderate Risk - Caution Needed"))
        else:
            st.error("❌ " + ("ಅಧಿಕ ಅಪಾಯ - ಕೊರೆಯುವುದು ಸೂಕ್ತವಲ್ಲ" if is_kn else "High Financial Risk"))

# --- HARD STOP WARNING (PREVENTS DEBT TRAP) ---
st.warning(
    f"🛑 **{'ಅತಿಯಾಗಿ ಕೊರೆಯುವುದನ್ನು ನಿಲ್ಲಿಸುವ ಮಿತಿ {Hard Stop Rule}:' if is_kn else 'Maximum Economic Drilling Stop Rule:'}** " +
    (f"ನಿಮ್ಮ ಭಾಗದಲ್ಲಿ **{res['hard_stop_ft']} ಅಡಿಗಿಂತ** ಆಳವಾಗಿ ಕೊರೆಯಬೇಡಿ. ಈ ಆಳ ದಾಟಿದ ನಂತರ ಕಲ್ಲುಬಂಡೆಯಲ್ಲಿ ಬಿರುಕುಗಳು ಮುಚ್ಚಿಹೋಗುತ್ತವೆ. "
     f"ಹೆಚ್ಚು ಆಳ ಕೊರೆದರೆ ಕೇವಲ ರಿಗ್ ಮಾಲೀಕರಿಗೆ ಹಣ ಪಾವತಿಸಬೇಕಾಗುತ್ತದೆಯೇ ಹೊರತು ನೀರು ಸಿಗುವ ಸಾಧ್ಯತೆ ಅತ್ಯಂತ ಕಡಿಮೆ."
     if is_kn else
     f"Do not drill beyond **{res['hard_stop_ft']} feet**. Deep secondary fracture permeability drops sharply beyond this depth in hard crystalline rock. Continuing past this limit substantially escalates debt with minimal chance of striking water.")
)

# --- EXPANDABLE ACTIONABLE GUIDANCE ---
st.markdown("---")
st.subheader("ಬೋರ್‌ವೆಲ್ ಕೊರೆಯುವ ಮುನ್ನ ರೈತರು ಅನುಸರಿಸಬೇಕಾದ ನಿಯಮಗಳು" if is_kn else "Pre-Drilling Scientific Action Checklist")

with st.expander("🔬 1. ವೈಜ್ಞಾನಿಕ ಭೂಭೌತ ಸರ್ವೇ {Electrical Resistivity Survey} - ಯಾಕೆ ಮಾಡಿಸಬೇಕು?"):
    st.markdown(
        "ತೆಂಗಿನಕಾಯಿ ಅಥವಾ ವಾಟರ್ ಡೌಸಿಂಗ್ ವಿಧಾನವು ಕೇವಲ ನಂಬಿಕೆಯಾಗಿದ್ದು ಅದಕ್ಕೆ ಯಾವುದೇ ವೈಜ್ಞಾನಿಕ ಆಧಾರವಿಲ್ಲ.\n\n"
        "- ಕೇವಲ **₹2,000 ರಿಂದ ₹3,000** ವೆಚ್ಚದಲ್ಲಿ ಅಧಿಕೃತ ಜಲಭೂವಿಜ್ಞಾನಿಯಿಂದ {Hydrogeologist} ವಿದ್ಯುತ್ ರೋಧಕತೆ ಪರೀಕ್ಷೆ {Resistivity Test} ಮಾಡಿಸಿ.\n"
        "- ಇದು ನೆಲದೊಳಗೆ ಎಷ್ಟು ಅಡಿಯಲ್ಲಿ ಬಂಡೆಯ ಬಿರುಕುಗಳು {Fracture Zones} ಇವೆ ಎಂಬುದನ್ನು ಖಚಿತವಾಗಿ ಹೇಳುತ್ತದೆ.\n"
        "- **₹2,00,000 ಬೋರ್‌ವೆಲ್ ಹಣ ವ್ಯರ್ಥವಾಗುವುದನ್ನು ₹2,500 ಸರ್ವೇ ರಕ್ಷಿಸುತ್ತದೆ.**"
        if is_kn else
        "Traditional water divining carries zero geological proof and often leads to dry bores.\n\n"
        "- Invest **Rs 2,000 to Rs 3,000** in a certified hydrogeologist's Electrical Resistivity Survey.\n"
        "- The survey accurately detects depth to fractured saturated zones before moving heavy drilling rigs.\n"
        "- Spending Rs 2,500 upfront protects Rs 2,00,000 of hard-earned money and prevents debt traps."
    )

with st.expander("🌧️ 2. ಬೋರ್‌ವೆಲ್ ಮಳೆನೀರು ಮರುಪೂರಣ ಗುಂಡಿ {Rainwater Recharge Pit}"):
    st.markdown(
        f"ಬೇಸಿಗೆಯಲ್ಲಿ ನಿಮ್ಮ ಬೋರ್‌ವೆಲ್ ಬತ್ತಿಹೋಗದಂತೆ ತಡೆಯಲು ಮರುಪೂರಣ ಗುಂಡಿ ಅತ್ಯಗತ್ಯ. ನಿಮ್ಮ ಜಿಲ್ಲೆಯಲ್ಲಿ ಬೇಸಿಗೆಯಲ್ಲಿ ಸರಾಸರಿ **{res['summer_drop_ft']} ಅಡಿ** ನೀರಿನ ಮಟ್ಟ ಕುಸಿಯುತ್ತದೆ.\n\n"
        "**ನಿರ್ಮಾಣ ಹಂತಗಳು:**\n"
        "1. ಬೋರ್‌ವೆಲ್ ಕೇಸಿಂಗ್ ಪೈಪ್‌ನ ಸುತ್ತಲೂ 10x10 ಅಡಿ ಅಗಲ ಹಾಗೂ 8 ಅಡಿ ಆಳದ ಗುಂಡಿ ತೋಡಿ.\n"
        "2. ಕೇಸಿಂಗ್ ಪೈಪ್‌ಗೆ ಸಣ್ಣ ರಂಧ್ರಗಳನ್ನು ಕೊರೆದು ಜಾಲರಿ ಬಟ್ಟೆ {Nylon Mesh} ಸುತ್ತಿ.\n"
        "3. ಕೆಳಗೆ ದೊಡ್ಡ ಜಲ್ಲಿಕಲ್ಲು (40mm), ಮಧ್ಯ ಸಣ್ಣ ಜಲ್ಲಿ (20mm) ಮತ್ತು ಮೇಲೆ ದಪ್ಪ ಮರಳು ತುಂಬಿ.\n"
        "4. ಮಳೆಗಾಲದ ಮಳೆನೀರು ಈ ಫಿಲ್ಟರ್ ಮೂಲಕ ಹಾದು ನೇರವಾಗಿ ಭೂಮಿಯ ಆಳದ ಬಿರುಕುಗಳನ್ನು ತಲುಪುತ್ತದೆ."
        if is_kn else
        f"Prevent your borewell from drying out in summer. Average summer water drop in your district is **{res['summer_drop_ft']} ft**.\n\n"
        "**Construction Steps:**\n"
        "1. Dig a 10x10 ft pit, 8 ft deep around the borewell casing.\n"
        "2. Drill micro-perforations into casing pipe and wrap tightly with nylon mesh.\n"
        "3. Layer coarse gravel (40mm) at bottom, medium gravel (20mm) in middle, and coarse sand on top.\n"
        "4. Monsoon runoff filters into the pit and directly replenishes deep aquifer fractures."
    )

with st.expander("🏛️ 3. ಗಂಗಾ ಕಲ್ಯಾಣ ಯೋಜನೆ {Ganga Kalyana Yojana} - ಉಚಿತ ಬೋರ್‌ವೆಲ್ ಸೌಲಭ್ಯ"):
    st.markdown(
        "ಕರ್ನಾಟಕ ಸರ್ಕಾರದ ಹಿಂದುಳಿದ ವರ್ಗಗಳ ಕಲ್ಯಾಣ ಇಲಾಖೆ ಹಾಗೂ ನಿಗಮಗಳಿಂದ ಸಣ್ಣ ಮತ್ತು ಅತಿ ಸಣ್ಣ ರೈತರಿಗೆ ಉಚಿತ ಬೋರ್‌ವೆಲ್ ಸೌಲಭ್ಯ ಒದಗಿಸಲಾಗುತ್ತದೆ.\n\n"
        "- **ಅರ್ಹತೆ:** ಸಣ್ಣ/ಅತಿ ಸಣ್ಣ ರೈತರು (1.20 ರಿಂದ 5 ಎಕರೆ ಒಣಭೂಮಿ).\n"
        "- **ಸೌಲಭ್ಯ:** ಬೋರ್‌ವೆಲ್ ಕೊರೆಯುವುದು, ಕೇಸಿಂಗ್ ಪೈಪ್, ಪಂಪ್‌ಸೆಟ್ ಅಳವಡಿಕೆ ಮತ್ತು ವಿದ್ಯುದ್ದೀಕರಣ ಸಂಪೂರ್ಣ ಉಚಿತ.\n"
        "- **ಅರ್ಜಿ ಸಲ್ಲಿಸುವ ಸ್ಥಳ:** ಗ್ರಾಮ ಒನ್ {Grama One} ಅಥವಾ [sevasindhu.karnataka.gov.in](https://sevasindhu.karnataka.gov.in) ಪೋರ್ಟಲ್."
        if is_kn else
        "Government of Karnataka provides free community/individual irrigation borewells for eligible small and marginal farmers.\n\n"
        "- **Eligibility:** Small/marginal farmers (1.20 to 5 acres dryland).\n"
        "- **Benefit:** Free drilling, casing pipe, submersible pump set, and electrical grid energization.\n"
        "- **Where to Apply:** Grama One centres or Seva Sindhu portal (sevasindhu.karnataka.gov.in)."
    )

with st.expander("🪨 4. ಈ ಜಿಲ್ಲೆಯ ಭೂಗರ್ಭ ಶಿಲಾ ರಚನೆ {Aquifer Lithology}"):
    st.markdown(
        f"**ಶಿಲಾ ವಿಧ:** {res['aquifer_type_kn'] if is_kn else res['aquifer_type']}\n\n"
        f"**ವೈಜ್ಞಾನಿಕ ವಿವರ:** {res['notes_kn'] if is_kn else res['notes_en']}"
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

