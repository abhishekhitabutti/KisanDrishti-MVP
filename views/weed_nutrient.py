"""
KrushiNudi Module 2: Sowing Season Weed & Nutrient Advisory
- Non-chemical weed suppression for notorious Karnataka weeds
- Allelopathic smother crop rotation planning
- On-farm crop residue & cattle manure composting calculator
- Traditional Karnataka bio-formulations (Jeevamrutha, Beejamrutha)
- Chemical fertilizer safety & banned pesticide alerts
100% pure Kannada localization with technical terms in braces {...}.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import streamlit as st
import i18n
import ui
from i18n import t
import weed_nutrient_data as wdata

is_kn = (i18n.current_lang() == "kn")

# --- HERO SECTION ---
hero_title = "ಕಳೆ & ಸಾವಯವ ಪೋಷಕಾಂಶ ಸಲಹೆಗಾರ" if is_kn else "Weed & Nutrient Advisor"
hero_sub = (
    "ಕಳೆಗಳ ನೈಸರ್ಗಿಕ ನಿಯಂತ್ರಣ, ಕೃಷಿ ತ್ಯಾಜ್ಯದಿಂದ ಸಾವಯವ ಕಾಂಪೋಸ್ಟ್ ತಯಾರಿಕೆ ಮತ್ತು ರಸಗೊಬ್ಬರದ ಖರ್ಚು ಉಳಿತಾಯ ಮಾರ್ಗದರ್ಶಿ."
    if is_kn else
    "Non-chemical weed suppression, on-farm organic composting calculator, and fertilizer safety."
)
ui.hero(hero_title, hero_sub, "🌿")

steps_row = [
    ("🚜", "ಬೇಸಿಗೆ ಉಳುಮೆ" if is_kn else "Deep ploughing"),
    ("🌱", "ಸಹಬೆಳೆ ಹೊದಿಕೆ" if is_kn else "Smother crops"),
    ("♻️", "ಕಾಂಪೋಸ್ಟ್ ಗೊಬ್ಬರ" if is_kn else "Farm compost"),
    ("🛡️", "ಪರಿಸರ ರಕ್ಷಣೆ" if is_kn else "Safe inputs"),
]
ui.steps_row(steps_row)

tab_labels = [
    "🌿 ಕಳೆ ನಿಯಂತ್ರಣ ತಂತ್ರಗಳು" if is_kn else "🌿 Weed Suppression",
    "🧮 ಕಾಂಪೋಸ್ಟ್ & ಉಳಿತಾಯ ಲೆಕ್ಕ" if is_kn else "🧮 Compost Calculator",
    "🧪 ಸಾಂಪ್ರದಾಯಿಕ ಸಾವಯವ ಸೂತ್ರಗಳು" if is_kn else "🧪 Bio-Formulations",
    "⚠️ ರಾಸಾಯನಿಕ ಸುರಕ್ಷತೆ & ಎಚ್ಚರಿಕೆ" if is_kn else "⚠️ Chemical Safety",
]
tab_weed, tab_calc, tab_bio, tab_safety = st.tabs(tab_labels)


# ==========================================
# TAB 1: WEED SUPPRESSION & COVER CROPS
# ==========================================
with tab_weed:
    st.markdown(
        "### " + ("ಕರ್ನಾಟಕದ ಪ್ರಮುಖ ಹಠಮಾರಿ ಕಳೆಗಳ ನೈಸರ್ಗಿಕ ನಿಯಂತ್ರಣ" if is_kn else "Non-Chemical Suppression of Problematic Weeds")
    )
    st.write(
        "ಕಳೆನಾಶಕಗಳ ನಿರಂತರ ಬಳಕೆಯಿಂದ ಕಳೆಗಳು ಪ್ರತಿರೋಧ ಶಕ್ತಿ ಬೆಳೆಸಿಕೊಳ್ಳುತ್ತವೆ ಮತ್ತು ಬೋರ್‌ವೆಲ್ ನೀರು ಕಲುಷಿತವಾಗುತ್ತದೆ. "
        "ಕೃಷಿ ವಿಜ್ಞಾನ ಸಂಸ್ಥೆಗಳು {ICAR / UAS} ದೃಢಪಡಿಸಿದ ನೈಸರ್ಗಿಕ ಪದ್ಧತಿಗಳಿಂದ ಕಳೆಯ ಬೀಜ ಬ್ಯಾಂಕ್ ಅನ್ನು 2-3 ಋತುಗಳಲ್ಲಿ 80% ಕ್ಕೂ ಹೆಚ್ಚು ಕುಗ್ಗಿಸಬಹುದು."
        if is_kn else
        "Constant chemical herbicides lead to weed resistance and groundwater pollution. "
        "These science-backed non-chemical agronomic practices deplete the soil weed seed bank by over 80% across 2-3 seasons."
    )

    weed_options = {
        w["id"]: (w["name_kn"] + f" ({w['botanical']})" if is_kn else w["name_en"] + f" ({w['botanical']})")
        for w in wdata.WEEDS_DATA
    }
    
    selected_weed_id = st.selectbox(
        "ಕಳೆಯನ್ನು ಆಯ್ಕೆಮಾಡಿ:" if is_kn else "Select problematic weed:",
        options=list(weed_options.keys()),
        format_func=lambda wid: weed_options[wid],
        key="select_weed_choice"
    )
    
    weed_item = next(w for w in wdata.WEEDS_DATA if w["id"] == selected_weed_id)
    
    with st.container(border=True):
        col_w1, col_w2 = st.columns([3, 1])
        with col_w1:
            st.markdown(f"#### {weed_item['name_kn'] if is_kn else weed_item['name_en']}")
            st.caption(f"ವೈಜ್ಞಾನಿಕ ಹೆಸರು: *{weed_item['botanical']}* | ವರ್ಗ: {weed_item['type']}")
            st.markdown(f"**{'ಬೆಳೆಗೆ ಉಂಟುಮಾಡುವ ಹಾನಿ:' if is_kn else 'Crop Damage:'}**")
            st.write(weed_item["damage_kn"] if is_kn else weed_item["damage_en"])
        with col_w2:
            st.info(
                f"**{'ಮೂಲ ಸೂತ್ರ:' if is_kn else 'Golden Rule:'}**\n\n"
                f"{'ಬೀಜ ಕಟ್ಟುವ ಮುನ್ನವೇ ಕಿತ್ತುಹಾಕಿ!' if is_kn else 'Never let weeds set seed!'}"
            )

        st.markdown("---")
        st.markdown(f"**🛠️ {'ಹಂತ ಹಂತದ ನೈಸರ್ಗಿಕ ನಿಯಂತ್ರಣ ಕ್ರಮಗಳು:' if is_kn else 'Step-by-step Non-chemical Suppression Tactics:'}**")
        tactics = weed_item["tactics_kn"] if is_kn else weed_item["tactics_en"]
        for idx, tactic in enumerate(tactics, 1):
            st.markdown(f"**{idx}.** {tactic}")

    st.markdown("---")
    st.markdown("### " + ("ಕಳೆ ದಮನಕಾರಿ ಮತ್ತು ಹಸಿರೆಲೆ ಗೊಬ್ಬರದ ಬೆಳೆಗಳು" if is_kn else "Allelopathic Smother & Cover Crops"))
    st.write(
        "ಮುಖ್ಯ ಬೆಳೆಯ ಮೊದಲು ಅಥವಾ ಸಾಲುಗಳ ನಡುವೆ ಈ ಬೆಳೆಗಳನ್ನು ಬೆಳೆಯುವುದರಿಂದ ಕಳೆಗಳಿಗೆ ಸೂರ್ಯನ ಬೆಳಕು ಸಿಗುವುದಿಲ್ಲ ಮತ್ತು ಮಣ್ಣಿಗೆ ಅಪಾರ ಸಾರಜನಕ ದೊರೆಯುತ್ತದೆ:"
        if is_kn else
        "Growing these cover crops before or between main crops starves weeds of sunlight while naturally fixing atmospheric nitrogen:"
    )

    for crop in wdata.COVER_CROPS_DATA:
        with st.expander(f"🌱 {crop['name_kn'] if is_kn else crop['name_en']} (*{crop['botanical']}*)"):
            col_c1, col_c2 = st.columns(2)
            with col_c1:
                st.markdown(f"- **{'ಬೀಜದ ಪ್ರಮಾಣ:' if is_kn else 'Seed rate:'}** `{crop['seed_rate']}`")
                st.markdown(f"- **{'ಬೆಳವಣಿಗೆ ಅವಧಿ:' if is_kn else 'Duration:'}** `{crop['duration']}`")
                st.markdown(f"- **{'ಹಸಿರು ಜೈವಿಕ ರಾಶಿ:' if is_kn else 'Biomass:'}** `{crop['biomass']}`")
            with col_c2:
                st.markdown(f"- **{'ಸಾರಜನಕ ಸೇರ್ಪಡೆ {N}:' if is_kn else 'Nitrogen fixed {N}:'}** `{crop['n_added']}`")
                st.markdown(f"- **{'ಕಳೆ ದಮನ ಪರಿಣಾಮ:' if is_kn else 'Weed suppression:'}**")
                st.write(crop["weed_smother_kn"] if is_kn else crop["weed_smother"])


# ==========================================
# TAB 2: COMPOST & FERTILIZER SAVINGS CALCULATOR
# ==========================================
with tab_calc:
    st.markdown(
        "### " + ("ಕೃಷಿ ತ್ಯಾಜ್ಯದಿಂದ ಕಾಂಪೋಸ್ಟ್ & ಖರ್ಚು ಉಳಿತಾಯ ಲೆಕ್ಕಾಚಾರ ಯಂತ್ರ" if is_kn else "On-Farm Compost & Fertilizer Savings Calculator")
    )
    st.write(
        "ಬೆಳೆ ಕಟಾವಿನ ನಂತರ ಉಳಿಯುವ ರವದಿ, ಕಡ್ಡಿ-ಕಸ, ಒಣ ಹುಲ್ಲು ಮತ್ತು ದನ-ಕರುಗಳ ಸಗಣಿಯನ್ನು ಸುಡದೆ ಕಾಂಪೋಸ್ಟ್ ಮಾಡಿದರೆ "
        "ಯೂರಿಯಾ ಮತ್ತು {DAP} ಕೊಳ್ಳುವ ಸಾವಿರಾರು ರೂಪಾಯಿ ಹಣ ಉಳಿತಾಯವಾಗುತ್ತದೆ. ನಿಮ್ಮ ಜಮೀನಿನ ಲೆಕ್ಕ ಹಾಕಿ ನೋಡಿ:"
        if is_kn else
        "Instead of burning crop stalks, straw and cattle dung, converting them into rich farm compost saves substantial money on purchased Urea and DAP. Test your farm numbers below:"
    )

    with st.container(border=True):
        col_in1, col_in2, col_in3 = st.columns(3)
        with col_in1:
            acres_val = st.number_input(
                "ಜಮೀನಿನ ವಿಸ್ತೀರ್ಣ (ಎಕರೆಗಳಲ್ಲಿ):" if is_kn else "Land holding (Acres):",
                min_value=0.5, max_value=50.0, value=2.0, step=0.5, key="calc_acres"
            )
        with col_in2:
            cattle_val = st.number_input(
                "ದನ / ಎಮ್ಮೆ / ಎತ್ತುಗಳ ಸಂಖ್ಯೆ:" if is_kn else "Cattle / Cows count:",
                min_value=0, max_value=30, value=2, step=1, key="calc_cattle"
            )
        with col_in3:
            residue_val = st.number_input(
                "ಲಭ್ಯವಿರುವ ಬೆಳೆ ತ್ಯಾಜ್ಯ / ಕಸ (ಕ್ವಿಂಟಾಲ್):" if is_kn else "Available crop residue (Quintals):",
                min_value=0.0, max_value=200.0, value=15.0, step=2.0, key="calc_residue"
            )

        res_calc = wdata.calculate_compost_savings(acres_val, cattle_val, residue_val)

        st.markdown("---")
        st.markdown(f"#### 📊 {'6 ತಿಂಗಳ ಋತುವಿನಲ್ಲಿ ನಿಮ್ಮ ಅಂದಾಜು ಉತ್ಪಾದನೆ & ಉಳಿತಾಯ:' if is_kn else 'Estimated 6-Month Seasonal Output & Savings:'}")

        mcol1, mcol2, mcol3, mcol4 = st.columns(4)
        with mcol1:
            st.metric(
                label="ಸಿದ್ಧ ಕಾಂಪೋಸ್ಟ್ ಗೊಬ್ಬರ" if is_kn else "Finished Compost",
                value=f"{res_calc['finished_compost_tonnes']} ಟನ್ / Ton",
                delta=f"{res_calc['cartloads']} ಗಾಡಿಗಳು (Carts)"
            )
        with mcol2:
            st.metric(
                label="ಉಳಿತಾಯವಾದ ಯೂರಿಯಾ" if is_kn else "Urea Bags Saved",
                value=f"{res_calc['urea_bags_saved']} ಚೀಲಗಳು",
                delta=f"{res_calc['org_n_kg']} kg {('ಸಾರಜನಕ' if is_kn else 'N')}"
            )
        with mcol3:
            st.metric(
                label="ಉಳಿತಾಯವಾದ DAP" if is_kn else "DAP Bags Saved",
                value=f"{res_calc['dap_bags_saved']} ಚೀಲಗಳು",
                delta=f"{res_calc['org_p_kg']} kg {('ರಂಜಕ' if is_kn else 'P')}"
            )
        with mcol4:
            st.metric(
                label="ಉಳಿತಾಯವಾದ ಒಟ್ಟು ಹಣ" if is_kn else "Direct Money Saved",
                value=f"₹{res_calc['money_saved_rs']:,}",
                delta=f"SOC: {res_calc['soc_rating']}/10"
            )

    st.markdown("#### 🌿 " + ("ಉತ್ತಮ ಕಾಂಪೋಸ್ಟ್ ತಯಾರಿಸುವ 4 ಪ್ರಮುಖ ನಿಯಮಗಳು" if is_kn else "4 Core Rules of Quality Composting"))
    c_rules = [
        ("1. ಪದರಗಳ ಜೋಡಣೆ (C:N ಅನುಪಾತ)", "ತಳದಲ್ಲಿ 8 ಇಂಚು ಒಣ ತ್ಯಾಜ್ಯ (ಕಾರ್ಬನ್), ಮೇಲೆ 4 ಇಂಚು ಹಸಿ ಸಗಣಿ/ಹಸಿರೆಲೆ (ಸಾರಜನಕ) ಹಾಕಿ ಪರ್ಯಾಯ ಪದರಗಳನ್ನು ನಿರ್ಮಿಸಿ.",
         "1. Layering (C:N Ratio)", "Alternate 8-inch dry brown residue layers (carbon) with 4-inch fresh cattle dung/green leaf layers (nitrogen)."),
        ("2. ತೇವಾಂಶ ನಿರ್ವಹಣೆ", "ಕಾಂಪೋಸ್ಟ್ ರಾಶಿಯು ಹಿಂಡಿದ ಸ್ಪಂಜಿನಂತೆ ತೇವವಾಗಿರಬೇಕು (50-60% ತೇವಾಂಶ). ಅತಿಯಾದ ನೀರು ದುರ್ವಾಸನೆ ಉಂಟುಮಾಡುತ್ತದೆ, ಒಣಗಿದರೆ ಕೊಳೆಯುವುದು ನಿಲ್ಲುತ್ತದೆ.",
         "2. Moisture Balance", "Maintain moisture like a wrung-out sponge (50-60%). Sogginess causes foul odors; bone-dry piles stop working."),
        ("3. ಗಾಳಿಯಾಡುವಿಕೆ (ತಿರುವು ಹಾಕುವುದು)", "ಪ್ರತಿ 3-4 ವಾರಗಳಿಗೊಮ್ಮೆ ರಾಶಿಯನ್ನು ಬುಡಮೇಲು ಮಾಡಿ ತಿರುಗಿಸಿ. ಇದರಿಂದ ಆಮ್ಲಜನಕ ಸಿಕ್ಕು ಉಪಯುಕ್ತ ಬ್ಯಾಕ್ಟೀರಿಯಾಗಳು ವೇಗವಾಗಿ ಕೊಳೆಯಿಸುತ್ತವೆ.",
         "3. Aeration (Turning)", "Turn the heap inside out every 3-4 weeks to infuse oxygen and maintain active aerobic microbial heat."),
        ("4. ಬಿಸಿಯ ರಕ್ಷಣೆ", "ಉತ್ತಮ ಕಾಂಪೋಸ್ಟ್ ರಾಶಿಯಲ್ಲಿ ತಾಪಮಾನ 55-65°C ವರೆಗೆ ಏರುತ್ತದೆ. ಈ ಬಿಸಿಯು ಕಳೆಯ ಬೀಜಗಳನ್ನು ಮತ್ತು ರೋಗಾಣುಗಳನ್ನು ನೈಸರ್ಗಿಕವಾಗಿ ಕೊಲ್ಲುತ್ತದೆ.",
         "4. Thermal Peak", "A well-managed heap naturally heats up to 55-65°C, effectively pasteurizing weed seeds and plant pathogen spores.")
    ]
    for r in c_rules:
        with st.container(border=True):
            st.markdown(f"**{r[0] if is_kn else r[2]}**")
            st.write(r[1] if is_kn else r[3])


# ==========================================
# TAB 3: TRADITIONAL BIO-FORMULATIONS
# ==========================================
with tab_bio:
    st.markdown(
        "### " + ("ಕರ್ನಾಟಕದ ಸಾಂಪ್ರದಾಯಿಕ ನೈಸರ್ಗಿಕ ಕೃಷಿ ಸೂತ್ರಗಳು" if is_kn else "Traditional Karnataka Natural Farming Formulations")
    )
    st.write(
        "ಸ್ಥಳೀಯ ನಾಟಿ ಹಸುವಿನ ಸಗಣಿ ಮತ್ತು ಗೋಮೂತ್ರದಲ್ಲಿ ಕೋಟ್ಯಂತರ ಪ್ರಯೋಜನಕಾರಿ ಸೂಕ್ಷ್ಮಾಣು ಜೀವಿಗಳಿವೆ. "
        "ಇವುಗಳನ್ನು ತಯಾರಿಸಿ ಬಳಸುವುದರಿಂದ ಮಣ್ಣಿನ ಫಲವತ್ತತೆ ಸುಧಾರಿಸಿ ರಾಸಾಯನಿಕ ಗೊಬ್ಬರಗಳ ಮೇಲಿನ ಅವಲಂಬನೆ ಕಡಿಮೆಯಾಗುತ್ತದೆ:"
        if is_kn else
        "Indigenous cattle manure contains billions of beneficial plant-growth promoting microbes. "
        "These tested low-cost on-farm bio-formulations regenerate depleted soils and reduce dependence on chemical bags:"
    )

    for bio in wdata.BIO_FORMULATIONS:
        with st.expander(f"🏺 {bio['name_kn'] if is_kn else bio['name_en']}", expanded=(bio["id"] == "jeevamrutha")):
            st.markdown(f"**{'ಉದ್ದೇಶ & ಪ್ರಯೋಜನ:' if is_kn else 'Purpose & Benefit:'}**")
            st.write(bio["purpose_kn"] if is_kn else bio["purpose_en"])
            
            st.markdown(f"**🛒 {'ಬೇಕಾಗುವ ಸಾಮಗ್ರಿಗಳು:' if is_kn else 'Ingredients:'}**")
            ingrs = bio["ingredients_kn"] if is_kn else bio["ingredients_en"]
            for ing in ingrs:
                st.markdown(f"- {ing}")
                
            st.markdown(f"**⏳ {'ತಯಾರಿಸುವ ವಿಧಾನ:' if is_kn else 'Preparation Method:'}**")
            st.write(bio["preparation_kn"] if is_kn else bio["preparation_en"])
            
            st.markdown(f"**💧 {'ಬಳಸುವ ಪ್ರಮಾಣ & ಹಂತ:' if is_kn else 'Application Rate & Timing:'}**")
            st.info(bio["application_kn"] if is_kn else bio["application_en"])


# ==========================================
# TAB 4: CHEMICAL FERTILIZER SAFETY & BANNED CHEMICALS
# ==========================================
with tab_safety:
    st.markdown(
        "### " + ("ರಾಸಾಯನಿಕ ಗೊಬ್ಬರ ಸುರಕ್ಷತೆ & ನಿಷೇಧಿತ ವಿಷಕಾರಿ ಕೀಟನಾಶಕಗಳ ಎಚ್ಚರಿಕೆ" if is_kn else "Chemical Safety & Banned Toxic Pesticides Alert")
    )
    st.write(
        "ಅನಿವಾರ್ಯ ಸಂದರ್ಭಗಳಲ್ಲಿ ರಾಸಾಯನಿಕಗಳನ್ನು ಬಳಸುವಾಗ ಅತ್ಯಂತ ಕನಿಷ್ಠ ಪರಿಣಾಮಕಾರಿ ಪ್ರಮಾಣವನ್ನು ಮಾತ್ರ ಬಳಸಿ. "
        "ಅಂತರ್ಜಲ, ಜಾನುವಾರು ಮತ್ತು ಮನುಷ್ಯರ ಆರೋಗ್ಯವನ್ನು ಹಾಳುಮಾಡುವ ಅಪಾಯಕಾರಿ ಕೆಂಪು ತ್ರಿಕೋನದ ಕೀಟನಾಶಕಗಳನ್ನು ಎಂದಿಗೂ ಬಳಸಬೇಡಿ:"
        if is_kn else
        "When synthetic inputs are unavoidable, adhere to minimum effective doses. "
        "Never use red-triangle banned pesticides that contaminate borewell water, poison cattle, and destroy human health:"
    )

    st.markdown("#### 🚫 " + ("ನಿಷೇಧಿತ / ಅತ್ಯಂತ ಅಪಾಯಕಾರಿ ಕೀಟನಾಶಕಗಳು (Red-Triangle Alert)" if is_kn else "Restricted & Banned Toxic Chemicals"))
    for chem in wdata.SAFETY_DATA["banned_chemicals"]:
        with st.container(border=True):
            st.markdown(f"**🛑 {chem['name']}**")
            st.markdown(f"- **{'ಅಪಾಯ:' if is_kn else 'Hazard:'}** {chem['hazard_kn'] if is_kn else chem['hazard']}")
            st.caption(f"ಸ್ಥಿತಿ: {chem['status']}")

    st.markdown("---")
    st.markdown("#### 🌿 " + ("ಪರಿಸರಸ್ನೇಹಿ ಪರ್ಯಾಯ ಮಾರ್ಗಗಳು" if is_kn else "Eco-Friendly Nutrient Alternatives"))
    for eco in wdata.SAFETY_DATA["eco_friendly_alternatives"]:
        with st.container(border=True):
            st.markdown(f"**✅ {eco['title_kn'] if is_kn and 'title_kn' in eco else eco['title_en']}**")
            st.write(eco["desc_kn"] if is_kn else eco["desc_en"])

    st.markdown("---")
    with st.container(border=True):
        st.markdown(f"**📞 {'ತುರ್ತು ಸಹಾಯವಾಣಿಗಳು ಮತ್ತು ಕೃಷಿ ಸಂಪರ್ಕ:' if is_kn else 'Emergency & Farmer Helplines:'}**")
        st.markdown(
            "- **ಕಿಸಾನ್ ಕಾಲ್ ಸೆಂಟರ್ {Kisan Call Centre}:** `1800-180-1551` (ಉಚಿತ ಕರೆ - ಬೆಳಗ್ಗೆ 6 ರಿಂದ ರಾತ್ರಿ 10 ರವರೆಗೆ)\n"
            "- **ಕರ್ನಾಟಕ ರೈತರ ಸಹಾಯವಾಣಿ {Karnataka Farmer Distress Helpline}:** `1800-425-1552`\n"
            "- **ವಿಷಬಾಧೆ ತುರ್ತು ಚಿಕಿತ್ಸೆ {Poison Emergency}:** ಹತ್ತಿರದ ಪ್ರಾಥಮಿಕ ಆರೋಗ್ಯ ಕೇಂದ್ರ ಅಥವಾ ತಾಲೂಕು ಆಸ್ಪತ್ರೆಗೆ ತಕ್ಷಣ ಭೇಟಿ ನೀಡಿ."
            if is_kn else
            "- **Kisan Call Centre:** `1800-180-1551` (Toll-Free, 6 AM to 10 PM in Kannada)\n"
            "- **Karnataka Farmer Distress Helpline:** `1800-425-1552`\n"
            "- **Poison Emergency:** Rush immediately to your nearest Primary Health Centre or Taluk Hospital."
        )

# --- FEEDBACK & FOOTER ---
ui.feedback_box()
st.markdown("---")
footer_text = (
    "© 2026 ಅಭಿಷೇಕ್ ಹಿಟಬುತ್ತಿ. ಎಲ್ಲಾ ಹಕ್ಕುಗಳನ್ನು ಕಾಯ್ದಿರಿಸಲಾಗಿದೆ. ಅನುಮತಿಯಿಲ್ಲದೆ ಈ ಅಪ್ಲಿಕೇಶನ್ ಅನ್ನು ನಕಲಿಸುವುದು ಅಥವಾ ಮರುಬಳಕೆ ಮಾಡುವುದನ್ನು ನಿಷೇಧಿಸಲಾಗಿದೆ."
    if is_kn else
    "© 2026 Abhishek Hitabutti. All rights reserved. Copying or reuse of this app without permission is prohibited."
)
st.caption(footer_text)
