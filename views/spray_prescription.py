"""
KrushiNudi Module: Smart Spray & High-Yield Nutrition Prescription (ಔಷಧ ಚೀಟಿ & ಅಧಿಕ ಇಳುವರಿ ಪ್ರಿಸ್ಕ್ರಿಪ್ಷನ್)
Seamlessly connected to Crop Doctor (ಬೆಳೆ ವೈದ್ಯ) for direct prescription generation.
Features:
- Direct diagnosis integration with Crop Doctor
- Crop-wise diseases & pests with exact chemical actives and dosages (per L & per 15L pump)
- Crop-specific growth & nutritional tonics separately for EVERY crop (Vegetative, Flowering, Yield Booster)
- Weed disposal & suppression methods tailored by weed infestation density (Low, Moderate, Heavy)
- Digital Farm Prescription Calculator based on land area (Acres & Guntas) and sprayer type
- Tank-mix compatibility matrix & safe mixing sequence
- Verified Indian agricultural companies, direct purchase portals, and toll-free helpline numbers.
100% bilingual (English & Pure Kannada) with technical terms enclosed in braces {...}.
"""

import sys
from datetime import datetime
from html import escape
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import pandas as pd
import streamlit as st
import i18n
import ui
from i18n import t
import prescription_data as pdata

is_kn = (i18n.current_lang() == "kn")

# --- HERO SECTION ---
hero_title = "ಔಷಧ & ಪೋಷಕಾಂಶ ಚೀಟಿ" if is_kn else "Smart Spray Prescription"
hero_sub = (
    "ಬೆಳೆ ವೈದ್ಯರಿಗೆ {Crop Doctor} ನೇರವಾಗಿ ಸಂಪರ್ಕಿತ: ರೋಗ-ಕೀಟ ನಿಯಂತ್ರಣ, ಪ್ರತ್ಯೇಕ ಬೆಳೆವಾರು ಪೋಷಕಾಂಶ ಟಾನಿಕ್‌ಗಳು, ಕಳೆ ಸಾಂದ್ರತೆ ವಿಲೇವಾರಿ, ಮತ್ತು ಜಮೀನಿನ ಅಳತೆಯ ಡಿಜಿಟಲ್ ಪ್ರಿಸ್ಕ್ರಿಪ್ಷನ್."
    if is_kn else
    "Directly connected to Crop Doctor: disease/pest treatments, crop-specific nutritional tonics, density-based weed disposal, and land-size prescription slip."
)
ui.hero(hero_title, hero_sub, "💊")

steps_row = [
    ("🩺", "ಬೆಳೆ ವೈದ್ಯ" if is_kn else "Crop Doctor"),
    ("💧", "ನಿಖರ ಡೋಸ್" if is_kn else "Exact dosage"),
    ("🌾", "ಬೆಳೆ ಟಾನಿಕ್" if is_kn else "Growth tonic"),
    ("🧮", "ಔಷಧ ಚೀಟಿ" if is_kn else "Prescription slip"),
    ("🚚", "ನೇರ ಖರೀದಿ" if is_kn else "Direct buy"),
]
ui.steps_row(steps_row)

# --- DIRECT CONNECTION BANNER WITH CROP DOCTOR ---
presc_target_id = st.session_state.get("presc_target_id")
target_crop_obj = None
if presc_target_id:
    target_crop_obj = next((p for p in pdata.CROP_PRESCRIPTIONS if p["id"] == presc_target_id), None)

c_banner1, c_banner2 = st.columns([3, 1])
with c_banner1:
    if target_crop_obj:
        st.success(
            f"🩺 **{'ಬೆಳೆ ವೈದ್ಯರಿಂದ ನೇರ ಶಿಫಾರಸು:' if is_kn else 'Direct from Crop Doctor Diagnosis:'}** "
            f"**{target_crop_obj['crop_kn'] if is_kn else target_crop_obj['crop_en']}** — "
            f"*{target_crop_obj['problem_kn'] if is_kn else target_crop_obj['problem_en']}*"
        )
    else:
        st.info(
            "🩺 " + (
                "ಹೊಸ ರೋಗದ ಲಕ್ಷಣಗಳು ಕಂಡಿವೆಯೇ? ಫೋಟೋ ತೆಗೆದು ಪರೀಕ್ಷಿಸಲು **ಬೆಳೆ ವೈದ್ಯರನ್ನು** ಬಳಸಿ."
                if is_kn else
                "Notice disease symptoms on your crop? Photograph leaves to identify issues using **Crop Doctor**."
            )
        )
with c_banner2:
    ui.page_link(
        "views/crop_doctor.py",
        "📸 " + ("ಬೆಳೆ ವೈದ್ಯ" if is_kn else "Crop Doctor"),
        icon="🩺"
    )

# --- MAIN TABS ---
tab_labels = [
    "📋 ಬೆಳೆ ರೋಗ & ಕೀಟನಾಶಕ ಮಾರ್ಗದರ್ಶಿ" if is_kn else "📋 Disease & Pest Advisory",
    "🌾 ಬೆಳೆವಾರು ಬೆಳವಣಿಗೆ & ಟಾನಿಕ್‌ಗಳು" if is_kn else "🌾 Crop-Wise Tonics",
    "🌿 ಕಳೆ ಸಾಂದ್ರತೆ & ವಿಲೇವಾರಿ" if is_kn else "🌿 Weed Disposal by Density",
    "🚀 ಅಧಿಕ ಇಳುವರಿ ಪ್ರವರ್ಧಕಗಳು" if is_kn else "🚀 High-Yield Promoters",
    "🧮 ಡಿಜಿಟಲ್ ಔಷಧ ಚೀಟಿ (ಕ್ಯಾಲ್ಕುಲೇಟರ್)" if is_kn else "🧮 Prescription Calculator",
    "⚠️ ಟ್ಯಾಂಕ್-ಮಿಕ್ಸ್ ನಿಯಮಗಳು" if is_kn else "⚠️ Tank-Mix Rules",
    "🛒 ಭಾರತೀಯ ಕೃಷಿ ಕಂಪನಿಗಳು & ಕರೆ" if is_kn else "🛒 Indian Agri Companies",
]
tab_pest, tab_crop_tonics, tab_weed_density, tab_yield, tab_calc, tab_mix, tab_companies = st.tabs(tab_labels)


# ==============================================================================
# TAB 1: DISEASE & PEST CHEMICAL ADVISORY
# ==============================================================================
with tab_pest:
    st.markdown(
        "### " + ("🌾 ಬೆಳೆವಾರು ರೋಗ-ಕೀಟ ನಿಯಂತ್ರಣ ಮತ್ತು ಸಿಂಪರಣಾ ಮಾರ್ಗದರ್ಶಿ" if is_kn else "🌾 Crop-Wise Disease & Pest Management Guide")
    )
    st.caption(
        "ಕೃಷಿ ವಿಶ್ವವಿದ್ಯಾಲಯಗಳು (UAS Bangalore, UAS Dharwad, TNAU, ICAR) ಶಿಫಾರಸು ಮಾಡಿದ ವೈಜ್ಞಾನಿಕ ರಾಸಾಯನಿಕಗಳು ಮತ್ತು ಎಲೆ ಪೋಷಕಾಂಶಗಳು."
        if is_kn else
        "Scientific recommendations formulated by ICAR and state agricultural universities with safe dosage and tank-mix nutrition."
    )

    crop_options = {
        (p["crop_kn"] if is_kn else p["crop_en"]) + " - " + (p["problem_kn"] if is_kn else p["problem_en"]): p["id"]
        for p in pdata.CROP_PRESCRIPTIONS
    }
    crop_keys = list(crop_options.keys())

    default_idx = 0
    if presc_target_id:
        for idx, key in enumerate(crop_keys):
            if crop_options[key] == presc_target_id:
                default_idx = idx
                break

    selected_crop_label = st.selectbox(
        "ಬೆಳೆ ಮತ್ತು ಸಮಸ್ಯೆಯನ್ನು ಆಯ್ಕೆಮಾಡಿ:" if is_kn else "Select Crop & Problem:",
        crop_keys,
        index=default_idx
    )
    selected_id = crop_options[selected_crop_label]
    p_item = next(p for p in pdata.CROP_PRESCRIPTIONS if p["id"] == selected_id)

    c1, c2 = st.columns([2, 1])
    with c1:
        st.markdown(f"#### 🎯 {p_item['problem_kn'] if is_kn else p_item['problem_en']}")
        st.markdown(f"**{'ರೋಗ / ಕೀಟದ ಲಕ್ಷಣಗಳು:' if is_kn else 'Observed Symptoms:'}**")
        st.info(p_item["symptoms_kn"] if is_kn else p_item["symptoms_en"])

    with c2:
        badge_text = "ಕೀಟ ಬಾಧೆ" if (is_kn and p_item["type"] == "pest") else ("ಶಿಲೀಂಧ್ರ ರೋಗ" if is_kn else p_item["type"].capitalize())
        st.markdown(f"**ವರ್ಗ:** {ui.badge(badge_text, 'pest' if p_item['type'] == 'pest' else 'disease')}", unsafe_allow_html=True)
        st.markdown(f"**ಅನ್ವಯವಾಗುವ ಬೆಳೆ:** `{p_item['crop_kn'] if is_kn else p_item['crop_en']}`")

    st.markdown(f"**🧪 {'ಶಿಫಾರಸು ಮಾಡಿದ ಅಧಿಕೃತ ಔಷಧಗಳು & ನಿಖರ ಪ್ರಮಾಣ:' if is_kn else 'Recommended Chemicals & Exact Dosages:'}**")
    chem_rows = []
    for c in p_item["recommended_chemicals"]:
        chem_rows.append({
            "ಔಷಧದ ಹೆಸರು" if is_kn else "Product Name": c["trade_name_kn"] if is_kn else c["trade_name"],
            "ರಾಸಾಯನಿಕ ಅಂಶ" if is_kn else "Active Ingredient": c["active"],
            "1 ಲೀಟರ್ ನೀರಿಗೆ" if is_kn else "Dose / Litre": c["dose_per_l"],
            "15L ಪಂಪ್‌ಗೆ" if is_kn else "Dose / 15L Pump": c["dose_per_pump_15l"],
            "ತಯಾರಕರು" if is_kn else "Manufacturer": c["manufacturer"]
        })
    st.dataframe(pd.DataFrame(chem_rows), hide_index=True, use_container_width=True)

    st.markdown(f"**🌿 {'ಟ್ಯಾಂಕ್‌ಗೆ ಬೆರೆಸಬೇಕಾದ ಪೋಷಕಾಂಶ (ಅಧಿಕ ಚೇತರಿಕೆ & ಇಳುವರಿಗಾಗಿ):' if is_kn else 'Tank-Mix Nutrition to Add (For Fast Recovery & High Yield):'}**")
    st.success(f"💡 {p_item['tank_mix_nutrition_kn'] if is_kn else p_item['tank_mix_nutrition_en']}")

    st.markdown(f"**🛡️ {'ಔಷಧ ಸಿಂಪಡಿಸುವಾಗ ಪಾಲಿಸಬೇಕಾದ ಕಡ್ಡಾಯ ಕ್ರಮಗಳು:' if is_kn else 'Spraying Measures & Cultural Practices:'}**")
    measures = p_item["spraying_measures_kn"] if is_kn else p_item["spraying_measures_en"]
    for m in measures:
        st.markdown(f"- {m}")


# ==============================================================================
# TAB 2: CROP-WISE GROWTH & NUTRITIONAL TONICS (SEPARATE FOR EVERY CROP)
# ==============================================================================
with tab_crop_tonics:
    st.markdown(
        "### " + ("🌾 ಪ್ರತಿ ಬೆಳೆಗೂ ಪ್ರತ್ಯೇಕ ಬೆಳವಣಿಗೆ & ಪೋಷಕಾಂಶ ಟಾನಿಕ್ ವೇಳಾಪಟ್ಟಿ" if is_kn else "🌾 Dedicated Stage-Wise Nutritional Tonics for Every Crop")
    )
    st.caption(
        "ಪ್ರತಿಯೊಂದು ಬೆಳೆಗೂ ಸಸಿ ಹಂತ, ಹೂವಾಡುವ ಹಂತ ಮತ್ತು ಕಾಯಿ/ಕಾಳು ತುಂಬುವ ಹಂತಗಳಲ್ಲಿ ಸಿಂಪಡಿಸಬೇಕಾದ ಅತ್ಯುತ್ತಮ ಟಾನಿಕ್‌ಗಳು ಮತ್ತು ನಿಖರ ಡೋಸ್‌ಗಳು."
        if is_kn else
        "Tailored stage-specific growth boosters, bio-stimulants, and foliar nutrients designed specifically for each major crop."
    )

    tonic_crops = list(pdata.CROP_SPECIFIC_TONICS.keys())
    sel_tonic_crop = st.selectbox(
        "ಬೆಳೆಯನ್ನು ಆಯ್ಕೆಮಾಡಿ:" if is_kn else "Select Crop for Nutrition Plan:",
        tonic_crops
    )
    t_plan = pdata.CROP_SPECIFIC_TONICS[sel_tonic_crop]

    st.markdown(f"#### 🎯 {t_plan['name_kn'] if is_kn else sel_tonic_crop} — 3-ಹಂತದ ಇಳುವರಿ ಬೂಸ್ಟರ್ ವೇಳಾಪಟ್ಟಿ")
    st.markdown(f"**ನಿರೀಕ್ಷಿತ ಇಳುವರಿ ಹೆಚ್ಚಳ:** {ui.badge(t_plan['boost_pct'], 'healthy')}", unsafe_allow_html=True)

    col_t1, col_t2, col_t3 = st.columns(3)
    with col_t1:
        with st.container(border=True):
            st.markdown(f"**🌱 {'ಹಂತ 1: ಸಸಿ & ಕವಲು ಹಂತ' if is_kn else 'Stage 1: Vegetative Flush'}**")
            st.caption(t_plan["veg_stage_kn"] if is_kn else t_plan["veg_stage_en"])
    with col_t2:
        with st.container(border=True):
            st.markdown(f"**🌸 {'ಹಂತ 2: ಹೂವಾಡುವ ಹಂತ' if is_kn else 'Stage 2: Flowering Booster'}**")
            st.caption(t_plan["flower_stage_kn"] if is_kn else t_plan["flower_stage_en"])
    with col_t3:
        with st.container(border=True):
            st.markdown(f"**🌾 {'ಹಂತ 3: ಕಾಳು / ಕಾಯಿ ಮಾಗುವಿಕೆ' if is_kn else 'Stage 3: Grain / Fruit Size'}**")
            st.caption(t_plan["yield_stage_kn"] if is_kn else t_plan["yield_stage_en"])

    st.markdown("---")
    st.markdown("**🛒 ಭಾರತದ ಅಧಿಕೃತ ಪೋಷಕಾಂಶಗಳ ನೇರ ಖರೀದಿ ಲಿಂಕ್‌ಗಳು:**")
    quick_prods = [
        ("IFFCO Sagarika Liquid (ಕಡಲಕಳೆ ಟಾನಿಕ್)", "https://www.iffcobazar.in/en/product/sagarika-liquid"),
        ("IFFCO Nano Urea Plus (ನ್ಯಾನೋ ಯೂರಿಯಾ)", "https://www.iffcobazar.in/en/product/iffco-nano-urea-liquid"),
        ("WSF 19:19:19 (ಕರಗುವ ಗೊಬ್ಬರ)", "https://www.iffcobazar.in/en/product/wsf-19-19-19-fertiliser"),
        ("WSF 00:52:34 (ಹೂವು ಉತ್ತೇಜಕ)", "https://www.bighaat.com/products/0-52-34-fertilizer"),
        ("Chelated Boron 20% (ಬೋರಾನ್)", "https://www.bighaat.com/products/multiplex-boron"),
    ]
    qp_cols = st.columns(len(quick_prods))
    for col, (name, link) in zip(qp_cols, quick_prods):
        col.link_button(name, link, use_container_width=True)


# ==============================================================================
# TAB 3: WEED DISPOSAL BY INFESTATION DENSITY & LAND PORTION
# ==============================================================================
with tab_weed_density:
    st.markdown(
        "### " + ("🌿 ಜಮೀನಿನ ಕಳೆ ಸಾಂದ್ರತೆಗೆ ಅನುಗುಣವಾಗಿ ವಿಲೇವಾರಿ & ನಿಯಂತ್ರಣ ವಿಧಾನಗಳು" if is_kn else "🌿 Weed Disposal & Suppression Methods Tailored by Infestation Density")
    )
    st.write(
        "ಜಮೀನಿನಲ್ಲಿ ಕಳೆ ಆವರಿಸಿರುವ ವಿಸ್ತೀರ್ಣಕ್ಕೆ (ಕಡಿಮೆ, ಮಧ್ಯಮ ಅಥವಾ ತೀವ್ರ ದಟ್ಟ) ತಕ್ಕಂತೆ ಸೂಕ್ತ ನೈಸರ್ಗಿಕ, ಯಾಂತ್ರಿಕ ಮತ್ತು ಕಾಂಪೋಸ್ಟ್ ವಿಲೇವಾರಿ ಕ್ರಮಗಳು."
        if is_kn else
        "Strategic weed disposal and suppression methods calibrated to the portion and density of weeds acquired by the land."
    )

    density_mode = st.radio(
        "ನಿಮ್ಮ ಜಮೀನಿನಲ್ಲಿ ಕಳೆಯ ಸಾಂದ್ರತೆ ಎಷ್ಟಿದೆ?" if is_kn else "Current Weed Infestation Level on Your Plot:",
        [
            "ಕಡಿಮೆ ಸಾಂದ್ರತೆ (< 15% ಭಾಗ) - Low Infestation",
            "ಮಧ್ಯಮ ಸಾಂದ್ರತೆ (15% - 40% ಭಾಗ) - Moderate Infestation",
            "ತೀವ್ರ ದಟ್ಟ ಸಾಂದ್ರತೆ (> 40% ಬೆಳೆ ಮುಳುಗಿಸುವ ಕಳೆ) - Dense Infestation"
        ],
        horizontal=True
    )

    if "Low" in density_mode:
        density_key = "low"
    elif "Moderate" in density_mode:
        density_key = "medium"
    else:
        density_key = "dense"

    w_plan = pdata.WEED_MANAGEMENT_BY_DENSITY[density_key]

    with st.container(border=True):
        st.markdown(f"#### 🔍 {w_plan['title_kn'] if is_kn else w_plan['title_en']}")
        st.markdown(
            f"**ರಾಸಾಯನಿಕ ಅಗತ್ಯತೆ:** "
            f"<span style='background:{w_plan['badge_color']}; color:#fff; padding:0.2rem 0.6rem; border-radius:12px; font-weight:bold;'>"
            f"{w_plan['chemical_necessity_kn'] if is_kn else w_plan['chemical_necessity_en']}</span>",
            unsafe_allow_html=True
        )
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown(f"**{'ಕೈಗೊಳ್ಳಬೇಕಾದ ಕ್ರಮಗಳು & ವಿಲೇವಾರಿ ವಿಧಾನಗಳು:' if is_kn else 'Action Steps & Organic Disposal Methods:'}**")
        steps = w_plan["action_steps_kn"] if is_kn else w_plan["action_steps_en"]
        for stp in steps:
            st.markdown(f"- {stp}")

        if "chemical_weedicides" in w_plan:
            st.markdown("---")
            st.markdown(f"**{'ಶಿಫಾರಸು ಮಾಡಿದ ಕಳೆನಾಶಕಗಳು & ನಿಖರ ಡೋಸ್ {Chemical Weedicides}:' if is_kn else 'Recommended Chemical Weedicides & Exact Dosages:'}**")
            for cw in w_plan["chemical_weedicides"]:
                with st.container(border=True):
                    cw_col1, cw_col2 = st.columns([2.5, 1])
                    with cw_col1:
                        st.markdown(f"**🌿 {cw['trade_name_kn'] if is_kn else cw['trade_name_en']}**")
                        st.write(f"**{'ಸೂಕ್ತ ಬೆಳೆಗಳು:' if is_kn else 'Target Crops:'}** {cw['target_crops_kn'] if is_kn else cw['target_crops_en']}")
                        st.write(f"**{'15L ಪಂಪ್‌ಗೆ ಡೋಸ್:' if is_kn else 'Dose per 15L Pump:'}** `{cw['dose_per_pump_15l']}`")
                        st.write(f"**{'1 ಎಕರೆಗೆ ಪ್ರಮಾಣ:' if is_kn else 'Dose per 1 Acre:'}** `{cw['dose_per_acre']}`")
                        st.caption(cw['timing_kn'] if is_kn else cw['timing_en'])
                    with cw_col2:
                        st.link_button("🛒 ಖರೀದಿಸಿ (Buy)", cw["buy_url"], use_container_width=True)

    st.markdown("---")
    st.markdown(
        "#### ♻️ ಕಳೆ ತ್ಯಾಜ್ಯದಿಂದ ಅಧಿಕ ತಾಪಮಾನದ ಜೈವಿಕ ಕಾಂಪೋಸ್ಟ್ ತಯಾರಿಕೆ {Thermophilic Composting}:"
        if is_kn else
        "#### ♻️ Converting Weed Residue into Safe Organic Compost (Thermophilic Composting):"
    )
    st.info(
        "ಕಳೆಗಳನ್ನು ಬದು ಅಥವಾ ಕಾಲುವೆಗೆ ಎಸೆಯುವುದರಿಂದ ಮಳೆ ನೀರಿನಲ್ಲಿ ಬೀಜಗಳು ಹರಡಿ ಮುಂದಿನ ವರ್ಷ 10 ಪಟ್ಟು ಹೆಚ್ಚು ಕಳೆ ಬರುತ್ತದೆ! "
        "ಕೀಳಲಾದ ಕಳೆಯನ್ನು 1 ಮೀಟರ್ ಆಳದ ಗುಂಡಿಯಲ್ಲಿ ಸೆಗಣಿ ಗಂಜಲ, ಕೃಷಿ ತ್ಯಾಜ್ಯ ಮತ್ತು ಟ್ರೈಕೋಡರ್ಮದೊಂದಿಗೆ ಪದರಗಳಾಗಿ ಹಾಕಿ. "
        "ಗುಂಡಿಯಲ್ಲಿ ಉಂಟಾಗುವ 55°C ತಾಪಮಾನಕ್ಕೆ ಎಲ್ಲಾ ಕಳೆ ಬೀಜಗಳು ಸತ್ತು ಉತ್ತಮ ಸಾರಜನಕಯುಕ್ತ ಸಾವಯವ ಗೊಬ್ಬರವಾಗುತ್ತದೆ."
        if is_kn else
        "Throwing weeds on field bunds spreads dormant weed seeds into irrigation channels, causing a 10x heavier infestation next season! "
        "Instead, layer weeds in a 1-meter deep pit with cattle dung slurry and Trichoderma. "
        "The resulting 55°C thermophilic fermentation heat sterilizes all weed seed banks, turning residue into rich organic fertilizer."
    )


# ==============================================================================
# TAB 4: HIGH-YIELD BIOSTIMULANTS & PROMOTERS
# ==============================================================================
with tab_yield:
    st.markdown(
        "### " + ("🚀 ಅಧಿಕ ಇಳುವರಿ ಪೋಷಕಾಂಶಗಳು, ನ್ಯಾನೋ ತಂತ್ರಜ್ಞಾನ & ಜೈವಿಕ ಉತ್ತೇಜಕಗಳು" if is_kn else "🚀 High-Yield Promoters, Nanotechnology & Biostimulants")
    )
    st.caption(
        "ಕೇವಲ ರೋಗ ನಿಯಂತ್ರಣವಲ್ಲದೆ, ಹೂವು ಉದುರುವುದು ತಡೆದು, ಕಾಳು ದಪ್ಪಗಾಗಿಸಿ 15-25% ಅಧಿಕ ಇಳುವರಿ ನೀಡುವ ಭಾರತದ ಅತ್ಯುತ್ತಮ ಪೋಷಕಾಂಶಗಳು."
        if is_kn else
        "Essential water-soluble fertilizers, nanotechnology nutrients, and plant growth regulators to maximize grain filling and crop yield."
    )

    for item in pdata.HIGH_YIELD_PROMOTERS:
        name_title = item["name_kn"] if is_kn else item["name_en"]
        cat_title = item["category_kn"] if is_kn else item["category_en"]
        with st.expander(f"✨ {name_title} — ({cat_title})", expanded=(item["id"] in ["sagarika", "nano_urea"])):
            col_a, col_b = st.columns([3, 1])
            with col_a:
                st.markdown(f"**{'ಪ್ರಯೋಜನಗಳು & ಇಳುವರಿ ಹೆಚ್ಚಳ:' if is_kn else 'Benefits & Yield Impact:'}**")
                st.write(item["benefits_kn"] if is_kn else item["benefits_en"])

                st.markdown(f"**{'ಸಿಂಪಡಿಸುವ ಹಂತ & ಕಾಲಾವಧಿ:' if is_kn else 'Application Timing:'}**")
                st.info(item["timing_kn"] if is_kn else item["timing_en"])

                st.markdown(
                    f"**{'ಟ್ಯಾಂಕ್ ಮಿಶ್ರಣ ಹೊಂದಾಣಿಕೆ:' if is_kn else 'Tank-Mix Compatibility:'}** "
                    f"`{item['compatible_with']}`"
                )

            with col_b:
                st.markdown(f"**{'15L ಪಂಪ್‌ಗೆ ಡೋಸ್:' if is_kn else 'Dose per 15L Pump:'}**")
                st.markdown(f"### `{item['dose_per_pump_15l'].split()[0]}`")
                st.caption(f"{'ಲೀಟರ್‌ಗೆ:' if is_kn else 'Per Litre:'} {item['dose_per_litre']}")
                st.markdown(f"**{'1 ಎಕರೆಗೆ ಪ್ರಮಾಣ:' if is_kn else 'Dose per Acre:'}**")
                st.info(item.get("dose_per_acre", "500 ml/1 kg in 200L water"))
                st.markdown(f"**ತಯಾರಕರು:** `{item['manufacturer']}`")
                st.link_button(
                    "🛒 ನೇರ ಖರೀದಿ" if is_kn else "🛒 Order Online",
                    item["buy_url"],
                    use_container_width=True
                )


# ==============================================================================
# TAB 5: DIGITAL PRESCRIPTION CALCULATOR
# ==============================================================================
with tab_calc:
    st.markdown(
        "### " + ("🧮 ಡಿಜಿಟಲ್ ಕೃಷಿ ಔಷಧ ಚೀಟಿ (ಪ್ರಿಸ್ಕ್ರಿಪ್ಷನ್ ಕ್ಯಾಲ್ಕುಲೇಟರ್)" if is_kn else "🧮 Digital Farm Prescription Slip Calculator")
    )
    st.write(
        "ನಿಮ್ಮ ಜಮೀನಿನ ವಿಸ್ತೀರ್ಣ (ಎಕರೆ & ಗುಂಟೆ) ಮತ್ತು ಸಿಂಪರಣಾ ಪಂಪ್ ಆಯ್ಕೆಮಾಡಿ. ಬೇಕಾಗುವ ನೀರಿನ ಪ್ರಮಾಣ, ಔಷಧದ ಪ್ರಮಾಣ ಮತ್ತು ಖರೀದಿಸಬೇಕಾದ ಒಟ್ಟು ಬಾಟಲಿಗಳ ಲೆಕ್ಕಾಚಾರ ಪಡೆಯಿರಿ."
        if is_kn else
        "Enter your land area (Acres & Guntas) and sprayer type to calculate the exact water volume, chemical dosage, and total bottles/packs to buy."
    )

    c_in1, c_in2, c_in3 = st.columns([2, 1, 1])
    with c_in1:
        calc_crop_options = {
            (p["crop_kn"] if is_kn else p["crop_en"]) + " - " + (p["problem_kn"] if is_kn else p["problem_en"]): p
            for p in pdata.CROP_PRESCRIPTIONS
        }
        calc_keys = list(calc_crop_options.keys())
        default_calc_idx = 0
        if presc_target_id:
            for idx, key in enumerate(calc_keys):
                if calc_crop_options[key]["id"] == presc_target_id:
                    default_calc_idx = idx
                    break

        sel_crop_name = st.selectbox(
            "ಬೆಳೆ & ಸಮಸ್ಯೆ ಆಯ್ಕೆಮಾಡಿ:" if is_kn else "Select Crop & Problem:",
            calc_keys,
            index=default_calc_idx,
            key="calc_crop_sel"
        )
        active_presc = calc_crop_options[sel_crop_name]

    with c_in2:
        acres = st.number_input("ಎಕರೆ {Acres}:" if is_kn else "Acres:", min_value=0.0, max_value=50.0, value=1.0, step=0.5)
    with c_in3:
        guntas = st.number_input("ಗುಂಟೆ {Guntas}:" if is_kn else "Guntas:", min_value=0, max_value=39, value=0, step=1)

    total_acres = acres + (guntas / 40.0)

    c_sp1, c_sp2 = st.columns(2)
    with c_sp1:
        sprayer_labels = {
            s["name_kn"] if is_kn else s["name_en"]: k for k, s in pdata.SPRAYER_CONFIGS.items()
        }
        sel_sprayer_label = st.selectbox(
            "ಸಿಂಪರಣಾ ಪಂಪ್ ವಿಧ:" if is_kn else "Sprayer Equipment:",
            list(sprayer_labels.keys())
        )
        sprayer_key = sprayer_labels[sel_sprayer_label]
        sprayer_cfg = pdata.SPRAYER_CONFIGS[sprayer_key]

    with c_sp2:
        growth_booster_options = {
            "ಯಾವುದೂ ಬೇಡ {None}": None
        }
        for b in pdata.HIGH_YIELD_PROMOTERS:
            growth_booster_options[b["name_kn"] if is_kn else b["name_en"]] = b
        sel_booster_label = st.selectbox(
            "ಜೊತೆಗೆ ಬೆರೆಸುವ ಇಳುವರಿ ಬೂಸ್ಟರ್ / ಟಾನಿಕ್:" if is_kn else "Add Yield Booster / Foliar Nutrient:",
            list(growth_booster_options.keys())
        )
        selected_booster = growth_booster_options[sel_booster_label]

    # Calculations
    is_veg = any(v in active_presc["id"] for v in ["chilli", "tomato", "onion"])
    pumps_per_acre = sprayer_cfg["pumps_per_acre_vegetables"] if is_veg else sprayer_cfg["pumps_per_acre_field_crop"]
    total_pumps = round(pumps_per_acre * total_acres, 1)
    if total_pumps < 1.0 and total_acres > 0:
        total_pumps = 1.0
    total_water_litres = int(total_pumps * sprayer_cfg["volume_l"])

    primary_chem = active_presc["recommended_chemicals"][0]

    st.markdown("---")
    st.markdown(
        f"### 📋 {'ಅಧಿಕೃತ ಕೃಷಿ ಔಷಧ ಚೀಟಿ {Farm Prescription Slip}' if is_kn else 'Official Farm Prescription Slip'}"
    )

    now_date = datetime.now().strftime("%d-%b-%Y")
    st.markdown(f"""
    <div style="background-color: #F8FBF8; border: 2px solid #2E7D32; border-radius: 12px; padding: 1.2rem; font-family: sans-serif;">
        <div style="display: flex; justify-content: space-between; border-bottom: 2px solid #2E7D32; padding-bottom: 0.5rem; margin-bottom: 1rem;">
            <div>
                <h3 style="color: #1B5E20; margin: 0;">🌾 ಕೃಷಿನುಡಿ ಸ್ಮಾರ್ಟ್ ಔಷಧ ಚೀಟಿ (KrushiNudi Prescription)</h3>
                <span style="color: #4A5A4A; font-size: 0.9rem;">ದಿನಾಂಕ / Date: {now_date} | ವಿನ್ಯಾಸಕರು: ಅಭಿಷೇಕ್ ಹಿಟಬುತ್ತಿ</span>
            </div>
            <div style="text-align: right;">
                <span style="background: #2E7D32; color: #fff; padding: 0.3rem 0.8rem; border-radius: 20px; font-weight: bold; font-size: 0.85rem;">RX VERIFIED</span>
            </div>
        </div>
        <p><b>ಬೆಳೆ & ಸಮಸ್ಯೆ / Crop & Problem:</b> {active_presc['crop_kn'] if is_kn else active_presc['crop_en']} — {active_presc['problem_kn'] if is_kn else active_presc['problem_en']}</p>
        <p><b>ಜಮೀನಿನ ವಿಸ್ತೀರ್ಣ / Land Size:</b> {acres} ಎಕರೆ {guntas} ಗುಂಟೆ ({total_acres:.2f} Acres)</p>
        <p><b>ಸ್ಪ್ರೇಯರ್ ಮಾದರಿ / Equipment:</b> {sprayer_cfg['name_kn'] if is_kn else sprayer_cfg['name_en']}</p>
        <p><b>ಒಟ್ಟು ಸಿಂಪರಣಾ ಪಂಪ್‌ಗಳು / Total Pumps:</b> <b style="color: #C62828; font-size: 1.2rem;">{total_pumps} ಪಂಪ್‌ಗಳು</b> (ಒಟ್ಟು ನೀರು: <b>{total_water_litres} ಲೀಟರ್</b>)</p>
        <hr style="border: 0; border-top: 1px dashed #A5D6A7; margin: 0.8rem 0;">
        <h4 style="color: #1B5E20; margin-bottom: 0.5rem;">💊 ಸಿಂಪಡಿಸಬೇಕಾದ ಔಷಧಿಗಳ ಪ್ರಮಾಣ (Dosage per Pump & Total to Buy):</h4>
        <ol style="margin-left: 1.2rem; line-height: 1.6;">
            <li><b>ಮುಖ್ಯ ಕೀಟನಾಶಕ / ಶಿಲೀಂಧ್ರನಾಶಕ:</b> {primary_chem['trade_name_kn'] if is_kn else primary_chem['trade_name']} ({primary_chem['active']})<br>
                ➔ ಪ್ರತಿ ಪಂಪ್‌ಗೆ ಡೋಸ್: <b>{primary_chem['dose_per_pump_15l']}</b><br>
                ➔ ಇಡೀ ಜಮೀನಿಗೆ ಬೇಕಾಗುವ ಒಟ್ಟು ಅಂದಾಜು ಔಷಧ: <b>{total_pumps} ಪಂಪ್‌ಗಳಿಗೆ ತಕ್ಕಂತೆ ಖರೀದಿಸಿ</b>.
            </li>
            {"<li><b>ಇಳುವರಿ ಬೂಸ್ಟರ್ / ಪೋಷಕಾಂಶ:</b> " + (selected_booster['name_kn'] if is_kn else selected_booster['name_en']) + "<br>➔ ಪ್ರತಿ ಪಂಪ್‌ಗೆ ಡೋಸ್: <b>" + selected_booster['dose_per_pump_15l'] + "</b></li>" if selected_booster else ""}
            <li><b>ಸಿಲಿಕಾನ್ ಅಂಟು ದ್ರಾವಣ (Silicon Spreader):</b> ಪ್ರತಿ ಪಂಪ್‌ಗೆ <b>5 ಮಿಲಿ</b> (ಔಷಧ ಎಲೆಯ ಮೇಲೆ ಹರಡಲು ಮತ್ತು ಮಳೆಗೆ ತೊಳೆದುಹೋಗದಿರಲು).</li>
        </ol>
        <div style="background: #E8F5E9; border-left: 4px solid #2E7D32; padding: 0.6rem 0.8rem; border-radius: 6px; margin-top: 0.8rem;">
            <b>💧 ಔಷಧಿ ಬೆರೆಸುವ ಸರಿಯಾದ ವಿಧಾನ (Mixing Sequence):</b><br>
            1. ಮೊದಲು ಪಂಪ್‌ಗೆ ಅರ್ಧ ಭಾಗ ನೀರು ತುಂಬಿ ➔ 2. ಕರಗುವ ಗೊಬ್ಬರ/ಪುಡಿ ಔಷಧ ಬೆರೆಸಿ ಕಲಕಿ ➔ 3. ದ್ರವ ಔಷಧ ಹಾಕಿ ➔ 4. ಪೋಷಕಾಂಶ/ಟಾನಿಕ್ ಹಾಕಿ ➔ 5. ಕೊನೆಯಲ್ಲಿ ಅಂಟು ದ್ರಾವಣ ಬೆರೆಸಿ ಪೂರ್ತಿ ನೀರು ತುಂಬಿ.
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    col_dl, col_call = st.columns(2)
    with col_dl:
        prescription_text = f"""
==================================================
        KRUSHINUDI FARM PRESCRIPTION SLIP
         ಕೃಷಿನುಡಿ ಅಧಿಕೃತ ಕೃಷಿ ಔಷಧ ಚೀಟಿ
==================================================
ದಿನಾಂಕ / Date: {now_date}
ಅಭಿವೃದ್ಧಿಪಡಿಸಿದವರು / Developed by: Abhishek Hitabutti (ಅಭಿಷೇಕ್ ಹಿಟಬುತ್ತಿ)
--------------------------------------------------
ಬೆಳೆ / Crop: {active_presc['crop_kn'] if is_kn else active_presc['crop_en']}
ಸಮಸ್ಯೆ / Problem: {active_presc['problem_kn'] if is_kn else active_presc['problem_en']}
ಜಮೀನಿನ ಅಳತೆ / Land: {total_acres:.2f} Acres ({acres} Acres, {guntas} Guntas)
ಸ್ಪ್ರೇಯರ್ / Sprayer: {sprayer_cfg['name_kn'] if is_kn else sprayer_cfg['name_en']}
ಒಟ್ಟು ನೀರು / Total Water: {total_water_litres} Litres ({total_pumps} Pumps)

ಔಷಧ 1: {primary_chem['trade_name_kn'] if is_kn else primary_chem['trade_name']}
ಡೋಸ್: {primary_chem['dose_per_pump_15l']}

{"ಔಷಧ 2: " + (selected_booster['name_kn'] if is_kn else selected_booster['name_en']) + "\nಡೋಸ್: " + selected_booster['dose_per_pump_15l'] if selected_booster else ""}
ಅಂಟು ದ್ರಾವಣ / Sticker: 5 ml per pump

ಮುಖ್ಯ ಸೂಚನೆ: ಮುಂಜಾನೆ ಅಥವಾ ಸಂಜೆ ಮಾತ್ರ ಸಿಂಪಡಿಸಿ. ಕಳೆನಾಶಕ ಪಂಪ್ ಬಳಸಬೇಡಿ.
==================================================
"""
        st.download_button(
            "📥 ಔಷಧ ಚೀಟಿ ಡೌನ್‌ಲೋಡ್ ಮಾಡಿ (Download Text Slip)" if is_kn else "📥 Download Prescription Slip",
            prescription_text,
            file_name=f"KrushiNudi_Prescription_{active_presc['id']}.txt",
            mime="text/plain",
            use_container_width=True
        )

    with col_call:
        st.link_button(
            "📞 ಕಿಸಾನ್ ಕಾಲ್ ಸೆಂಟರ್ ತಜ್ಞರೊಂದಿಗೆ ಮಾತನಾಡಿ (1800 180 1551)" if is_kn else "📞 Call Kisan Call Centre (1800 180 1551)",
            "tel:18001801551",
            use_container_width=True
        )


# ==============================================================================
# TAB 6: TANK-MIX COMPATIBILITY RULES & SAFETY
# ==============================================================================
with tab_mix:
    st.markdown(
        "### " + ("⚠️ ಟ್ಯಾಂಕ್-ಮಿಶ್ರಣ ನಿಯಮಗಳು & ರಾಸಾಯನಿಕ ಹೊಂದಾಣಿಕೆ" if is_kn else "⚠️ Tank-Mix Compatibility Matrix & Safety Rules")
    )
    st.write(
        "ಹಲವಾರು ಔಷಧಗಳನ್ನು ಒಟ್ಟಿಗೆ ಬೆರೆಸಿ ಸಿಂಪಡಿಸುವಾಗ ಈ ನಿಯಮಗಳನ್ನು ಕಟ್ಟುನಿಟ್ಟಾಗಿ ಪಾಲಿಸಿ. ತಪ್ಪಾದ ಮಿಶ್ರಣದಿಂದ ಬೆಳೆ ಸುಟ್ಟುಹೋಗುವ ಮತ್ತು ಔಷಧ ಶಕ್ತಿ ಕಳೆದುಕೊಳ್ಳುವ ಅಪಾಯವಿದೆ."
        if is_kn else
        "Follow these scientific compatibility rules when mixing multiple agrochemicals to prevent phytotoxicity, crop leaf scorch, or nozzle clogging."
    )

    for rule in pdata.TANK_MIX_RULES:
        if rule["status"] == "SAFE":
            st.markdown(f"#### ✅ {rule['title_kn'] if is_kn else rule['title_en']}")
            items = rule["items_kn"] if is_kn else rule["items_en"]
            for itm in items:
                st.markdown(f"- 🟢 {itm}")
        else:
            st.markdown(f"#### 🚫 {rule['title_kn'] if is_kn else rule['title_en']}")
            items = rule["items_kn"] if is_kn else rule["items_en"]
            for itm in items:
                st.markdown(f"- 🔴 **{itm}**")

    st.markdown("---")
    st.markdown(
        "#### " + ("🪣 'ಜಾರ್ ಪರೀಕ್ಷೆ' (Jar Test) - ಮಿಶ್ರಣ ಸುರಕ್ಷಿತವೇ ಎಂದು ತಿಳಿಯಲು ಸರಳ ವಿಧಾನ:" if is_kn else "🪣 The 5-Minute 'Jar Test' - How to check compatibility before spraying:")
    )
    st.info(
        "1 ಲೀಟರ್ ನೀರಿನ ಪ್ಲಾಸ್ಟಿಕ್ ಬಾಟಲಿಗೆ ನೀವು ಸಿಂಪಡಿಸಲು ನಿರ್ಧರಿಸಿದ ಔಷಧಗಳು ಮತ್ತು ಗೊಬ್ಬರಗಳನ್ನು ಸಮಪ್ರಮಾಣದಲ್ಲಿ ಹಾಕಿ ಚೆನ್ನಾಗಿ ಕುಲುಕಿ 5 ನಿಮಿಷ ಬಿಡಿ. "
        "ದ್ರಾವಣದಲ್ಲಿ ಹಾಲೊಡೆದಂತೆ ಹೆಪ್ಪುಗಟ್ಟಿದರೆ, ಬಿಸಿಯಾದರೆ ಅಥವಾ ಕೆಳಗೆ ಗಟ್ಟಿಯಾಗಿ ಕುಳಿತರೆ ಆ ಔಷಧಗಳನ್ನು ಒಟ್ಟಿಗೆ ಬೆರೆಸಬಾರದು!"
        if is_kn else
        "Take a small transparent jar with 1 litre of water. Add proportional quantities of the intended tank-mix chemicals and shake well for 10 seconds. "
        "Wait 5 minutes: if the mixture curdles, produces heat, forms flakes or sediment, DO NOT mix them in your farm sprayer!"
    )


# ==============================================================================
# TAB 7: INDIAN AGRI COMPANIES & DIRECT PURCHASE PLATFORMS
# ==============================================================================
with tab_companies:
    st.markdown(
        "### " + ("🛒 ಭಾರತದ ಪ್ರಮುಖ ಕೃಷಿ ಕಂಪನಿಗಳು & ಮನೆಬಾಗಿಲಿಗೆ ನೇರ ಖರೀದಿ" if is_kn else "🛒 Top Indian Agri Companies & Direct Procurement Portals")
    )
    st.write(
        "ನಕಲಿ ಮತ್ತು ಕಲಬೆರಕೆ ಔಷಧಗಳಿಂದ ರೈತರನ್ನು ರಕ್ಷಿಸಲು ಅಧಿಕೃತ ಕಂಪನಿಗಳ ನೇರ ಖರೀದಿ ಲಿಂಕ್‌ಗಳು ಮತ್ತು ಟೋಲ್-ಫ್ರೀ ಕಾಲ್ ಆರ್ಡರ್ ವ್ಯವಸ್ಥೆ."
        if is_kn else
        "Protect farmers from spurious or counterfeit inputs by buying directly from certified Indian manufacturers and leading delivery platforms."
    )

    for comp in pdata.INDIAN_AGRI_PLATFORMS:
        with st.container(border=True):
            col_info, col_action = st.columns([3, 1])
            with col_info:
                st.markdown(f"#### 🏢 {comp['company_kn'] if is_kn else comp['company_en']}")
                st.write(comp["specialty_kn"] if is_kn else comp["specialty_en"])
                st.markdown(f"**🚚 {'ಡೆಲಿವರಿ ವಿವರ:' if is_kn else 'Delivery info:'}** {comp['delivery_note_kn'] if is_kn else comp['delivery_note_en']}")

                prods_str = " · ".join(f"`{p}`" for p in comp["popular_products"])
                st.markdown(f"**{'ಪ್ರಮುಖ ಉತ್ಪನ್ನಗಳು:' if is_kn else 'Top Products:'}** {prods_str}")

            with col_action:
                st.markdown(f"**{'ಉಚಿತ ಕಾಲ್ ಬುಕಿಂಗ್:' if is_kn else 'Toll-Free Helpline:'}**")
                st.markdown(f"### `{comp['phone']}`")
                st.link_button(
                    "🌐 ಆನ್‌ಲೈನ್ ಆರ್ಡರ್ ಮಾಡಿ" if is_kn else "🌐 Order Online",
                    comp["order_url"],
                    use_container_width=True
                )
                st.link_button(
                    "📞 ಫೋನ್ ಕರೆ ಮಾಡಿ" if is_kn else "📞 Call Now",
                    f"tel:{comp['phone'].replace(' ', '')}",
                    use_container_width=True
                )


# ==========================================
# FOOTER ATTRIBUTION
# ==========================================
ui.feedback_box()
st.markdown("---")
footer_text = (
    "© 2026 ಅಭಿಷೇಕ್ ಹಿಟಬುತ್ತಿ. ಎಲ್ಲಾ ಹಕ್ಕುಗಳನ್ನು ಕಾಯ್ದಿರಿಸಲಾಗಿದೆ. ಅನುಮತಿಯಿಲ್ಲದೆ ಈ ಅಪ್ಲಿಕೇಶನ್ ಅನ್ನು ನಕಲಿಸುವುದು ಅಥವಾ ಮರುಬಳಕೆ ಮಾಡುವುದನ್ನು ನಿಷೇಧಿಸಲಾಗಿದೆ."
    if is_kn else
    "© 2026 Abhishek Hitabutti. All rights reserved. Copying or reuse of this app without permission is prohibited."
)
st.caption(footer_text)
