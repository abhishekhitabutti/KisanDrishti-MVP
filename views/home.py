"""KrushiNudi: crop advisor (home view). The router in app.py shows it with the other views."""
import json
import sys
import pickle
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from html import escape  # noqa: E402

import numpy as np  # noqa: E402
import pandas as pd  # noqa: E402
import streamlit as st  # noqa: E402

import diagnosis  # noqa: E402
import i18n  # noqa: E402
import ui  # noqa: E402
import prescription_data as pdata  # noqa: E402
from districts import DISTRICTS, DISTRICTS_KN  # noqa: E402
from i18n import t  # noqa: E402


FEATURES = ["N", "P", "K", "temperature", "humidity", "ph", "rainfall"]
LABELS = {
    "N": "Nitrogen (N)", "P": "Phosphorus (P)", "K": "Potassium (K)",
    "temperature": "Temperature (°C)", "humidity": "Humidity (%)",
    "ph": "Soil pH", "rainfall": "Rainfall (mm)",
}
# Plain-language fertilizer sources. Amounts are NOT given: confirm with a soil test.
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
hero_title = "ಕೃಷಿನುಡಿ {KrushiNudi}" if is_kn else "KrushiNudi"
hero_sub = (
    "ಸ್ಮಾರ್ಟ್ ಕೃಷಿ ಸಲಹೆಗಾರ · ಬುದ್ಧಿವಂತ ಕೃಷಿಯ ಧ್ವನಿ {Smart Farm Advisory · The Voice of Intelligent Agriculture}"
    if is_kn else
    "Smart Farm Advisory · The Voice of Intelligent Agriculture"
)
ui.hero(hero_title, hero_sub, "🌾")
promo_tagline = (
    "✨ *ಚತುರ ಒಳನೋಟಗಳು. ಉತ್ತಮ ಕೃಷಿ. {Smarter Insights. Better Farming.}*"
    if is_kn else
    "✨ *Smarter Insights. Better Farming.*"
)
st.markdown(promo_tagline)

st.markdown(ui.badge(t("Beta"), "medium") + escape(t("Guidance comes from published sources and expert review is in progress.")), unsafe_allow_html=True)
ui.stat_row([(len(crops), t("crops in the advisor")), (len(DISTRICTS), t("Karnataka districts")),
             (len(diagnosis.load_kb()), t("problems with sourced guidance"))])

with st.container(border=True):
    gc1, gc2 = st.columns([3, 1])
    with gc1:
        st.markdown(f"**📖 {t('How to use the app')}**")
        st.caption(t("Step-by-step guide and live demo of all KrushiNudi tools"))
    with gc2:
        ui.page_link("views/guide.py", t("Demo & Guide"), "👉")

CARDS = [
    ("💧", "Borewell advisory", "Groundwater depth, feasibility and drilling budget.", "views/borewell.py"),
    ("🌿", "Weed & nutrient advisory", "Non-chemical weed suppression, compost and fertilizer savings.", "views/weed_nutrient.py"),
    ("🩺", "Crop Doctor", "Photograph a sick plant, pest or weed and get safe, sourced advice.", "views/crop_doctor.py"),
    ("💊", "Spray & nutrition prescription", "Crop protection, dosages, high-yield boosters and prescription slip.", "views/spray_prescription.py"),
    ("🗓️", "Season planner", "What to do before sowing, while growing and at harvest.", "views/season_planner.py"),
    ("⛈️", "Weather precautions", "7-day forecast by district and what to do before bad weather.", "views/weather.py"),
    ("📋", "Schemes and help", "Documents and steps for crop insurance, PM-KISAN and loans.", "views/schemes.py"),
]
for i in range(0, len(CARDS), 2):
    row = CARDS[i:i+2]
    cols = st.columns(len(row))
    for col, (icon, title, text, path) in zip(cols, row):
        with col.container(border=True):
            st.markdown(f"**{icon} {t(title)}**")
            st.caption(t(text))
            ui.page_link(path, t("Open"), "➡️")

# --- UPCOMING SEASONAL HIGH-YIELD CROP RECOMMENDATIONS (BY SOIL TYPE) ---
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

st.info(
    "🎯 **ಪರಿಪೂರ್ಣ ನಿಖರತೆಗೆ {For 100% Precision}:** ನಿಮ್ಮ ಜಮೀನಿನ ನಿರ್ದಿಷ್ಟ N, P, K ಪೋಷಕಾಂಶಗಳು, pH ಮತ್ತು ತಾಪಮಾನಕ್ಕೆ ತಕ್ಕಂತೆ ವೈಯಕ್ತಿಕ AI ಬೆಳೆ ಸಲಹೆ ಪಡೆಯಲು, ಕೆಳಗಿನ **'ನಿಮ್ಮ ಜಮೀನು {Your Field}'** ಸ್ಲೈಡರ್‌ಗಳನ್ನು ಹೊಂದಿಸಿ **'Generate Precision Advisory'** ಬಟನ್ ಒತ್ತಿರಿ."
    if is_kn else
    "🎯 **For 100% Precision:** If you know your field's exact N, P, K, pH and weather readings, adjust the sliders in **'Your Field'** below and click **'Generate Precision Advisory'**."
)

st.subheader(t("Your field"))
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
        with st.expander("🥬 " + ("ಕೆಂಪು ಎಲೆಕೋಸು ನೈಸರ್ಗಿಕ pH ಲಿಟ್ಮಸ್ ಪೇಪರ್ ವಿಧಾನ" if is_kn else "Red Cabbage Natural pH Indicator Method")):
            st.markdown(
                "- ನೇರಳೆ/ಕೆಂಪು ಎಲೆಕೋಸನ್ನು ನೀರಿನಲ್ಲಿ ಕುದಿಸಿ ನೇರಳೆ ಬಣ್ಣದ ದ್ರಾವಣ ತಯಾರಿಸಿ.\n"
                "- ಕಾಫಿ ಫಿಲ್ಟರ್ ಪೇಪರ್ ತುಂಡುಗಳನ್ನು ಈ ದ್ರಾವಣದಲ್ಲಿ ಅದ್ದಿ ಒಣಗಿಸಿದರೆ ನೈಸರ್ಗಿಕ pH ಪೇಪರ್ ಸಿದ್ಧವಾಗುತ್ತದೆ.\n"
                "- ಮಣ್ಣಿನ ತಿಳಿನೀರಿನಲ್ಲಿ ಅದ್ದಿದಾಗ: **ಗುಲಾಬಿ/ಕೆಂಪು ಬಣ್ಣ** ಬಂದರೆ ಆಮ್ಲೀಯ (Acidic); **ನೀಲಿ/ಹಸಿರು ಬಣ್ಣ** ಬಂದರೆ ತಟಸ್ಥ ಅಥವಾ ಕ್ಷಾರ (Alkaline)."
                if is_kn else
                "- Boil chopped red cabbage in water to extract natural purple anthocyanin indicator liquid.\n"
                "- Soak coffee filter paper strips and dry in shade to make DIY pH test strips.\n"
                "- Dip in soil clear water: Turns **Pink/Red** in acidic soil; turns **Blue/Green** in neutral/alkaline soil."
            )
            
    with diy_tab2:
        st.markdown("#### 🌿 " + ("ಗಿಡದ ಎಲೆಗಳ ಲಕ್ಷಣಗಳಿಂದ N, P, K ಕೊರತೆ ಗುರುತಿಸುವುದು" if is_kn else "Visual Leaf Signs for N, P, K Deficiencies"))
        st.caption(
            "ಗಿಡಗಳು ತಮ್ಮ ಪೋಷಕಾಂಶಗಳ ಕೊರತೆಯನ್ನು ಎಲೆಗಳ ಬಣ್ಣ ಮತ್ತು ರಚನೆಯ ಮೂಲಕ ಸ್ಪಷ್ಟವಾಗಿ ತೋರಿಸುತ್ತವೆ:"
            if is_kn else
            "Plants communicate nutrient deficiencies clearly through distinct leaf discoloration patterns:"
        )
        
        npk_c1, npk_c2, npk_c3 = st.columns(3)
        with npk_c1:
            with st.container(border=True):
                st.markdown("**🟢 ಸಾರಜನಕ {Nitrogen - N} ಕೊರತೆ:**")
                st.markdown(
                    "- **ಲಕ್ಷಣ:** ಗಿಡದ ಕೆಳಭಾಗದ ಹಳೆಯ ಎಲೆಗಳು ನಡುದಿಂಡಿನಿಂದ ಪ್ರಾರಂಭವಾಗಿ 'V' ಆಕಾರದಲ್ಲಿ ಹಳದಿಯಾಗುವುದು (Yellowing of older leaves).\n"
                    "- **ಪರಿಣಾಮ:** ಗಿಡ ಕುಬ್ಜವಾಗುತ್ತದೆ, ಕವಲುಗಳು ಕಡಿಮೆ.\n"
                    "- **ಮನೆಮದ್ದು:** ಜೀವಾಮೃತ, ಹಸಿರೆಲೆ ಗೊಬ್ಬರ (ಸೆಣಬು, ಡಯಾಂಚ), ಎರೆಹುಳು ಗೊಬ್ಬರ ಅಥವಾ 2% ಯೂರಿಯಾ ಸಿಂಪರಣೆ."
                    if is_kn else
                    "- **Symptom:** V-shaped yellowing starting from midrib of older lower leaves.\n"
                    "- **Impact:** Stunted plant height, poor tillering.\n"
                    "- **Remedy:** Apply Jeevamrutha, vermicompost, cow dung slurry or 2% urea foliar spray."
                )
        with npk_c2:
            with st.container(border=True):
                st.markdown("**🟣 ರಂಜಕ {Phosphorus - P} ಕೊರತೆ:**")
                st.markdown(
                    "- **ಲಕ್ಷಣ:** ಕೆಳಭಾಗದ ಎಲೆಗಳ ಹಿಂಭಾಗ ಹಾಗೂ ಅಂಚುಗಳು ನೇರಳೆ / ಕೆನ್ನೀಲಿ (Purple / Bronze) ಬಣ್ಣಕ್ಕೆ ತಿರುಗುವುದು.\n"
                    "- **ಪರಿಣಾಮ:** ಬೇರುಗಳು ಆಳಕ್ಕೆ ಇಳಿಯುವುದಿಲ್ಲ, ಕಾಳು ಕಟ್ಟುವುದಿಲ್ಲ.\n"
                    "- **ಮನೆಮದ್ದು:** ಮೂಳೆ ಪುಡಿ (Bone meal), ಪಿಎಸ್‌ಬಿ {PSB} ಜೈವಿಕ ಗೊಬ್ಬರ ಅಥವಾ ಸಿಂಗಲ್ ಸೂಪರ್ ಫಾಸ್ಫೇಟ್ {SSP}."
                    if is_kn else
                    "- **Symptom:** Dark purplish-bronze tint on leaf margins and undersides of older leaves.\n"
                    "- **Impact:** Severely stunted root development, delayed flowering.\n"
                    "- **Remedy:** Apply Phosphate Solubilizing Bacteria (PSB), bone meal, or Single Super Phosphate."
                )
        with npk_c3:
            with st.container(border=True):
                st.markdown("**🟠 ಪೊಟ್ಯಾಶ್ {Potassium - K} ಕೊರತೆ:**")
                st.markdown(
                    "- **ಲಕ್ಷಣ:** ಹಳೆಯ ಎಲೆಗಳ ಅಂಚುಗಳು ಬೆಂಕಿಯಲ್ಲಿ ಸುಟ್ಟಂತೆ (Leaf edge scorch / burn) ಕಂದು ಬಣ್ಣಕ್ಕೆ ತಿರುಗಿ ಒಣಗುವುದು.\n"
                    "- **ಪರಿಣಾಮ:** ಕಾಳು, ಕಾಯಿಗಳಲ್ಲಿ ತೂಕ ಇರುವುದಿಲ್ಲ, ರೋಗ ನಿರೋಧಕ ಶಕ್ತಿ ಕುಸಿಯುತ್ತದೆ.\n"
                    "- **ಮನೆಮದ್ದು:** ಕಟ್ಟಿಗೆಯ ಬೂದಿ (Wood ash - ಅತ್ಯುತ್ತಮ ನೈಸರ್ಗಿಕ ಪೊಟ್ಯಾಶ್) ಅಥವಾ ಎಂಒಪಿ {MOP}."
                    if is_kn else
                    "- **Symptom:** Yellowing and scorching/burning of outer leaf margins like burnt edges.\n"
                    "- **Impact:** Weak stalks, lodging, shrivelled grains and disease vulnerability.\n"
                    "- **Remedy:** Broadcast clean wood ash (natural potash) or apply MOP."
                )

    with diy_tab3:
        st.markdown("#### 🏺 " + ("ಮಣ್ಣಿನ ಕಣ ರಚನೆ (ಮರಳು, ಗೋಡು, ಜೇಡಿ) ಬಾಟಲಿ ಪರೀಕ್ಷೆ" if is_kn else "Soil Texture Sedimentation Test (Sand, Silt, Clay)"))
        st.markdown(
            "1. ಪಾರದರ್ಶಕ ಗಾಜಿನ ಬಾಟಲಿಗೆ (Glass Jar) 1/3 ಭಾಗ ಜಮೀನಿನ ಮಣ್ಣು ಹಾಕಿ.\n"
            "2. ಬಾಟಲಿಗೆ 3/4 ಭಾಗದಷ್ಟು ನೀರು ಮತ್ತು 1 ಚಮಚ ಉಪ್ಪು ಅಥವಾ ಡಿಟರ್ಜೆಂಟ್ ಹಾಕಿ ಮುಚ್ಚಳ ಹಾಕಿ 5 ನಿಮಿಷ ಚೆನ್ನಾಗಿ ಕುಲುಕಿ.\n"
            "3. ಬಾಟಲಿಯನ್ನು ಸಮತಟ್ಟಾದ ಸ್ಥಳದಲ್ಲಿ 24 ಗಂಟೆಗಳ ಕಾಲ ಅಲುಗಾಡಿಸದೆ ಇಡಿ.\n"
            "4. **ಫಲಿತಾಂಶ:**\n"
            "   - **1 ನಿಮಿಷದಲ್ಲಿ ತಳದಲ್ಲಿ ನಿಲ್ಲುವುದು:** ಮರಳು {Sand} (ದಪ್ಪ ಕಣಗಳು - 40% ಕ್ಕಿಂತ ಹೆಚ್ಚಿದ್ದರೆ ಕೆಂಪು ಮರಳು ಮಣ್ಣು).\n"
            "   - **2 ಗಂಟೆಯಲ್ಲಿ ನಿಲ್ಲುವುದು:** ಗೋಡು {Silt} (ಮಧ್ಯಮ ಕಣಗಳು).\n"
            "   - **24 ಗಂಟೆಯಲ್ಲಿ ಮೇಲ್ಭಾಗದಲ್ಲಿ ನಿಲ್ಲುವುದು:** ಜೇಡಿ {Clay} (ನಯವಾದ ಕಪ್ಪು ಕಣಗಳು - ಹೆಚ್ಚು ಜೇಡಿ ಇದ್ದರೆ ಕಪ್ಪು ಹತ್ತಿ ಮಣ್ಣು).\n"
            "   - ಇದರಿಂದ ನಿಮ್ಮ ಹೊಲದ ಮಣ್ಣಿನ ಪ್ರಕಾರವನ್ನು ನಿಖರವಾಗಿ ಪತ್ತೆಹಚ್ಚಬಹುದು."
            if is_kn else
            "1. Fill 1/3 of a clean glass jar with dry sieved soil.\n"
            "2. Add clean water up to 3/4 level plus 1 tsp salt/detergent to disperse particles. Shake vigorously for 5 minutes.\n"
            "3. Place on a flat surface and let settle for 24 hours undisturbed.\n"
            "4. **Observation:**\n"
            "   - **After 1 minute:** Bottom layer is coarse **Sand**.\n"
            "   - **After 2 hours:** Middle layer is smooth **Silt**.\n"
            "   - **After 24 hours:** Top layer is fine **Clay**.\n"
            "   - Calculate layer percentages to confirm whether your field is Sandy Loam, Clayey, or Black Cotton Soil."
        )

# --- DISTRICT SOIL TESTING LAB DIRECTORY & 100% FREE GOVERNMENT BENEFITS ---
with st.container(border=True):
    st.markdown("### 🏛️ " + ("ಜಿಲ್ಲಾವಾರು ಕೃಷಿ ಇಲಾಖೆ, ಮಣ್ಣು ಪರೀಕ್ಷಾ ಕೇಂದ್ರಗಳು & 100% ಉಚಿತ ಸರ್ಕಾರಿ ಸೌಲಭ್ಯಗಳು" if is_kn else "District Soil Testing Labs & 100% Free Govt Agri Benefits"))
    st.markdown(
        "🟢 **ಪ್ರಮುಖ ಸೂಚನೆ {Crucial Price Notice}:**\n"
        "- **ಸರ್ಕಾರಿ ಮಣ್ಣು ಆರೋಗ್ಯ ಕಾರ್ಡ್ {Govt Soil Health Card}:** ನಿಮ್ಮ ಹೋಬಳಿಯ ರೈತ ಸಂಪರ್ಕ ಕೇಂದ್ರದಲ್ಲಿ (RSK) ಮಣ್ಣು ಪರೀಕ್ಷೆ **ಸಂಪೂರ್ಣ 100% ಉಚಿತ (₹0 / FREE)**!\n"
        "- **ಖಾಸಗಿ ಲ್ಯಾಬ್‌ಗಳಲ್ಲಿ ಪರೀಕ್ಷಾ ಶುಲ್ಕ {Private Lab Testing Cost}:** ₹150 ರಿಂದ ₹200 ಪ್ರತಿ ಮಾದರಿಗೆ ಮಾತ್ರ."
        if is_kn else
        "🟢 **Crucial Pricing Notice:**\n"
        "- **Government Soil Health Card Scheme:** Soil testing at your local Raitha Samparka Kendra (RSK) is **100% FREE of cost (Rs. 0)**!\n"
        "- **Private Certified Agri Labs:** Standard fee is approx **Rs. 150 to Rs. 200 per sample**."
    )

    st.markdown("#### 📍 " + ("ನಿಮ್ಮ ಜಿಲ್ಲೆಯ ಕೃಷಿ ಇಲಾಖೆ, ಮಣ್ಣು ಪರೀಕ್ಷಾ ಲ್ಯಾಬ್ & ಸಂಪರ್ಕ ಸಂಖ್ಯೆಗಳು" if is_kn else "Nearest Agri Directorate, Soil Testing Lab & Helplines"))
    
    dist_list = sorted(pdata.KARNATAKA_DISTRICT_AGRI_CENTRES.keys())
    if is_kn:
        d_dict = {f"{pdata.KARNATAKA_DISTRICT_AGRI_CENTRES[d]['kn']} ({d})": d for d in dist_list}
        d_sel_name = st.selectbox("ಜಿಲ್ಲೆ ಆಯ್ಕೆಮಾಡಿ {Select District}:", list(d_dict.keys()), key="home_district_lab_sel")
        chosen_dist = d_dict[d_sel_name]
    else:
        chosen_dist = st.selectbox("Select District for Soil Lab & RSKs:", dist_list, key="home_district_lab_sel")
    
    d_center = pdata.KARNATAKA_DISTRICT_AGRI_CENTRES.get(chosen_dist, {})
    with st.container(border=True):
        dc1, dc2 = st.columns([2.5, 1.2])
        with dc1:
            st.markdown(f"**🏢 {'ಜಿಲ್ಲಾ ಕೃಷಿ ಜಂಟಿ ನಿರ್ದೇಶಕರ ಕಚೇರಿ {JDA}:' if is_kn else 'District Joint Director of Agriculture (JDA):'}**")
            st.write(d_center.get("jda_office", ""))
            st.markdown(f"**🔬 {'ಕೃಷಿ ವಿಜ್ಞಾನ ಕೇಂದ್ರದ ಮಣ್ಣು ಪರೀಕ್ಷಾ ಲ್ಯಾಬ್ {KVK / Soil Lab}:' if is_kn else 'ICAR-KVK / University Soil Testing Lab:'}**")
            st.write(d_center.get("kvk_lab", ""))
            st.markdown(f"**🌾 {'ತಾಲೂಕು ರೈತ ಸಂಪರ್ಕ ಕೇಂದ್ರಗಳು {RSKs}:' if is_kn else 'Raitha Samparka Kendras (RSK Centers):'}**")
            st.caption(d_center.get("rsk_centers", ""))
        with dc2:
            phone_num = d_center.get("phone", "1800 180 1551")
            first_phone = phone_num.split("/")[0].strip()
            st.markdown(f"**📞 {'ಸಂಪರ್ಕ ಸಂಖ್ಯೆ:' if is_kn else 'Phone Helpline:'}**")
            st.write(f"`{phone_num}`")
            st.link_button(
                "📞 ಕರೆ ಮಾಡಿ (Call Lab)" if is_kn else "📞 Call Soil Lab",
                f"tel:{first_phone.replace(' ', '').replace('-', '')}",
                use_container_width=True
            )
            st.link_button(
                "📞 ಕಿಸಾನ್ ಕಾಲ್ ಸೆಂಟರ್" if is_kn else "📞 Kisan Call Centre",
                "tel:18001801551",
                use_container_width=True
            )

    st.markdown("#### 🎁 " + ("ಕೃಷಿ ಇಲಾಖೆಯಲ್ಲಿ ರೈತರಿಗೆ ದೊರೆಯುವ 6 ಪ್ರಮುಖ ಉಚಿತ/ರಿಯಾಯಿತಿ ಸೌಲಭ್ಯಗಳು" if is_kn else "Top 6 Free / Highly Subsidized Government Agriculture Benefits"))
    
    for i in range(0, len(pdata.FREE_GOVT_AGRI_BENEFITS), 2):
        b_cols = st.columns(2)
        b_chunk = pdata.FREE_GOVT_AGRI_BENEFITS[i:i+2]
        for b_col, ben in zip(b_cols, b_chunk):
            with b_col.container(border=True):
                st.markdown(f"**{ben['title_kn'] if is_kn else ben['title_en']}**")
                st.success(ben['cost_kn'] if is_kn else ben['cost_en'])
                st.write(ben['details_kn'] if is_kn else ben['details_en'])
                st.caption(f"**{'ಎಲ್ಲಿ ಪಡೆಯಬೇಕು:' if is_kn else 'Where to get:'}** {ben['where_to_avail_kn'] if is_kn else ben['where_to_avail_kn']}")

ui.feedback_box()
is_kn = (i18n.current_lang() == "kn")
footer_str = (
    "© 2026 ಅಭಿಷೇಕ್ ಹಿಟಬುತ್ತಿ. ಎಲ್ಲ ಹಕ್ಕುಗಳನ್ನು ಕಾಯ್ದಿರಿಸಲಾಗಿದೆ. ಅನುಮತಿ ಇಲ್ಲದೆ ಈ ಆ್ಯಪ್ ಅನ್ನು ನಕಲು ಮಾಡುವುದು ಅಥವಾ ಮರುಬಳಕೆ ಮಾಡುವುದು ನಿಷಿದ್ಧ."
    if is_kn else
    "© 2026 Abhishek Hitabutti. All rights reserved. Copying or reuse of this app without permission is prohibited."
)
st.caption(footer_str)
