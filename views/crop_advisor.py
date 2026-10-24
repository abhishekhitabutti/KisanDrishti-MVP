"""
KrushiNudi: Dedicated Crop Advisor View (AI/ML Soil N-P-K & Climate Precision Engine).
Author: Abhishek Hitabutti
Copyright: © 2026 Abhishek Hitabutti. All rights reserved.
"""

import json
import pickle
import sys
from html import escape
from pathlib import Path

# Add project root to sys.path
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

# Header
hero_title = "ಬೆಳೆ ಸಲಹೆಗಾರ {Crop Advisor}" if is_kn else "Crop Advisor"
hero_sub = (
    "ಮಣ್ಣಿನ N-P-K ಪೋಷಕಾಂಶಗಳು, pH ಮತ್ತು ಹವಾಮಾನಕ್ಕೆ ತಕ್ಕಂತೆ ಗರಿಷ್ಠ ಇಳುವರಿಯ ವೈಜ್ಞಾನಿಕ ಬೆಳೆ ಶಿಫಾರಸು"
    if is_kn else
    "Precision crop suitability and yield recommendation powered by machine learning and Soil Health Card data"
)
ui.hero(hero_title, hero_sub, "🌱")

st.markdown(ui.badge(t("Beta"), "medium") + " " + escape(t("Guidance comes from published sources and expert review is in progress.")), unsafe_allow_html=True)
ui.stat_row([(len(crops), t("crops in the advisor")), (len(DISTRICTS), t("Karnataka districts")),
             (len(diagnosis.load_kb()), t("problems with sourced guidance"))])

# Seasonal high-yield recommendations
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
        key="advisor_season_radio"
    )
    sel_season_key = season_map[sel_season_lbl]
with col_s2:
    sel_soil_lbl = st.radio(
        "ಮಣ್ಣಿನ ಪ್ರಕಾರ ಆಯ್ಕೆಮಾಡಿ {Select Soil Type}:" if is_kn else "Select Your Soil Type:",
        list(soil_map.keys()),
        horizontal=False,
        key="advisor_soil_radio"
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

st.info(
    "🎯 **ಪರಿಪೂರ್ಣ ನಿಖರತೆಗೆ {For 100% Precision}:** ನಿಮ್ಮ ಜಮೀನಿನ ನಿರ್ದಿಷ್ಟ N, P, K ಪೋಷಕಾಂಶಗಳು, pH ಮತ್ತು ತಾಪಮಾನಕ್ಕೆ ತಕ್ಕಂತೆ ವೈಯಕ್ತಿಕ AI ಬೆಳೆ ಸಲಹೆ ಪಡೆಯಲು, ಕೆಳಗಿನ **'ನಿಮ್ಮ ಜಮೀನು {Your Field}'** ಸ್ಲೈಡರ್‌ಗಳನ್ನು ಹೊಂದಿಸಿ **'Generate Precision Advisory'** ಬಟನ್ ಒತ್ತಿರಿ."
    if is_kn else
    "🎯 **For 100% Precision:** If you know your field's exact N, P, K, pH and weather readings, adjust the sliders in **'Your Field'** below and click **'Generate Precision Advisory'**."
)

st.subheader(t("Your field"))
c1, c2 = st.columns(2)
with c1:
    values = {
        "N": st.slider(label("N"), 0, 140, 60, key="adv_n"),
        "P": st.slider(label("P"), 5, 145, 50, key="adv_p"),
        "K": st.slider(label("K"), 5, 205, 50, key="adv_k"),
        "ph": st.slider(label("ph"), 3.5, 10.0, 6.5, 0.1, key="adv_ph"),
    }
with c2:
    values.update({
        "temperature": st.slider(label("temperature"), 8.0, 44.0, 25.0, 0.5, key="adv_temp"),
        "humidity": st.slider(label("humidity"), 14.0, 100.0, 65.0, 1.0, key="adv_hum"),
        "rainfall": st.slider(label("rainfall"), 20.0, 300.0, 100.0, 5.0, key="adv_rain"),
    })
st.caption(t("N, P and K are on the same scale as the training data, not lab readings in kg per hectare."))

if st.button(t("Generate Precision Advisory"), type="primary", key="adv_btn_calc"):
    x = np.array([[values[k] for k in FEATURES]])
    probs = model.predict_proba(x)[0]
    order = np.argsort(probs)[::-1][:3]
    st.session_state["adv_advice"] = {
        "inputs": dict(values),
        "top": [(str(model.classes_[i]), float(probs[i])) for i in order],
    }

advice = st.session_state.get("adv_advice")
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
chosen_label = st.selectbox(t("Pick a crop to see how your field fits it"), list(crop_labels), index=default_index, key="adv_crop_sel")
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

# --- DIY HOME TESTING FOR N, P, K & pH ---
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

# Attribution & Feedback
ui.feedback_box()
st.markdown("---")
st.caption("© 2026 Abhishek Hitabutti | KrushiNudi Crop Advisor")
