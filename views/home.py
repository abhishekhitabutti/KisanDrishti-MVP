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
from districts import DISTRICTS  # noqa: E402
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
    ("🩺", "Crop Doctor", "Photograph a sick plant, pest or weed and get safe, sourced advice.", "views/crop_doctor.py"),
    ("🗓️", "Season planner", "What to do before sowing, while growing and at harvest.", "views/season_planner.py"),
    ("⛈️", "Weather precautions", "7-day forecast by district and what to do before bad weather.", "views/weather.py"),
    ("📋", "Schemes and help", "Documents and steps for crop insurance, PM-KISAN and loans.", "views/schemes.py"),
]
for row in (CARDS[:2], CARDS[2:]):
    for col, (icon, title, text, path) in zip(st.columns(2), row):
        with col.container(border=True):
            st.markdown(f"**{icon} {t(title)}**")
            st.caption(t(text))
            ui.page_link(path, t("Open"), "➡️")

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

ui.feedback_box()
is_kn = (i18n.current_lang() == "kn")
footer_str = (
    "© 2026 ಅಭಿಷೇಕ್ ಹಿಟಬುತ್ತಿ. ಎಲ್ಲ ಹಕ್ಕುಗಳನ್ನು ಕಾಯ್ದಿರಿಸಲಾಗಿದೆ. ಅನುಮತಿ ಇಲ್ಲದೆ ಈ ಆ್ಯಪ್ ಅನ್ನು ನಕಲು ಮಾಡುವುದು ಅಥವಾ ಮರುಬಳಕೆ ಮಾಡುವುದು ನಿಷಿದ್ಧ."
    if is_kn else
    "© 2026 Abhishek Hitabutti. All rights reserved. Copying or reuse of this app without permission is prohibited."
)
st.caption(footer_str)
