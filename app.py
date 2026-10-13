"""KisanDrishti: crop advisor (main page). Other pages live in the pages/ folder."""
import json
import pickle
from pathlib import Path

import numpy as np
import pandas as pd
import streamlit as st

import i18n
import ui
from i18n import t

st.set_page_config(page_title="KisanDrishti Portal", page_icon="🌾")

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


HERE = Path(__file__).resolve().parent
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

ui.inject_css()
i18n.language_picker()
ui.hero(t("KisanDrishti"), t("Crop advice, a photo-based crop doctor, weather precautions and scheme help for Karnataka farmers."), "🌾")
l1, l2, l3, l4 = st.columns(4)
l1.page_link("pages/3_Crop_Doctor.py", label=t("Crop Doctor"), icon="🩺")
l2.page_link("pages/1_Weather_Precautions.py", label=t("Weather"), icon="⛈️")
l3.page_link("pages/2_Schemes_and_Help.py", label=t("Schemes"), icon="📋")
l4.page_link("pages/4_Season_Planner.py", label=t("Season plan"), icon="🗓️")

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
table, inside = explorer_table(chosen, profiles, values)
st.write(t("**{n} of 7 measures** are within the typical range for {crop}.", n=inside, crop=i18n.crop(chosen)))
st.dataframe(table, hide_index=True)

with st.expander(t("About this model and its limits")):
    if metrics:
        st.write(t("{model} trained on {rows} rows covering {crops} crops. Accuracy on a held-out 20% test set: {acc}.",
                   model=metrics["model"], rows=f"{metrics['n_rows']:,}", crops=metrics["n_crops"], acc=f"{metrics['holdout_accuracy']:.1%}"))
        st.write(t(metrics["data_note"]))
    st.write(t("It does not know your local market, water supply, pests or soil history. Talk to your agriculture officer before you decide."))

st.markdown("---")
st.caption(t("© 2026 Abhishek Hitabutti. All rights reserved. Copying or reuse of this app without permission is prohibited."))
