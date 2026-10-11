"""KisanDrishti: crop advisor (main page). Other pages live in the pages/ folder."""
import json
import pickle
from pathlib import Path

import numpy as np
import pandas as pd
import streamlit as st

import ui

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
    st.markdown(f"#### Nutrients for {crop}")
    cols = st.columns(3)
    messages = []
    for col, key in zip(cols, ["N", "P", "K"]):
        diff = values[key] - ideal[key]
        col.metric(LABELS[key], f"{values[key]:.0f}", f"{diff:+.0f} vs ideal {ideal[key]:.0f}", delta_color="off")
        status = nutrient_status(values[key], ideal[key])
        if status == "below":
            messages.append(f"**{LABELS[key]} is below the ideal.** Common sources: {NUTRIENT_SOURCES[key]}.")
        elif status == "above":
            messages.append(f"**{LABELS[key]} is above the ideal.** Do not add more of it.")
    if messages:
        for m in messages:
            st.markdown(f"- {m}")
        st.caption("These are general pointers, not doses. Confirm the amount with your Soil Health Card or agriculture officer.")
    else:
        st.success("Nitrogen, phosphorus and potassium are close to the ideal for this crop.")


def explorer_table(crop, profiles, values):
    ranges = profiles[crop]["ranges"]
    rows, inside = [], 0
    for key in FEATURES:
        lo, hi = ranges[key]
        ok = lo <= values[key] <= hi
        inside += ok
        rows.append({
            "Measure": LABELS[key],
            "Your value": round(values[key], 1),
            "Typical range": f"{lo:.0f} to {hi:.0f}" if key != "ph" else f"{lo:.1f} to {hi:.1f}",
            "Fit": "Within range" if ok else ("Too low" if values[key] < lo else "Too high"),
        })
    return pd.DataFrame(rows), inside


model, profiles, metrics = load_artifacts()
crops = sorted(profiles)

ui.inject_css()
ui.hero("KisanDrishti", "Crop advice, a photo-based crop doctor, weather precautions and scheme help for Karnataka farmers.", "🌾")
l1, l2, l3 = st.columns(3)
l1.page_link("pages/3_Crop_Doctor.py", label="Crop Doctor", icon="🩺")
l2.page_link("pages/1_Weather_Precautions.py", label="Weather", icon="⛈️")
l3.page_link("pages/2_Schemes_and_Help.py", label="Schemes", icon="📋")

st.subheader("Your field")
c1, c2 = st.columns(2)
with c1:
    values = {
        "N": st.slider(LABELS["N"], 0, 140, 60),
        "P": st.slider(LABELS["P"], 5, 145, 50),
        "K": st.slider(LABELS["K"], 5, 205, 50),
        "ph": st.slider(LABELS["ph"], 3.5, 10.0, 6.5, 0.1),
    }
with c2:
    values.update({
        "temperature": st.slider(LABELS["temperature"], 8.0, 44.0, 25.0, 0.5),
        "humidity": st.slider(LABELS["humidity"], 14.0, 100.0, 65.0, 1.0),
        "rainfall": st.slider(LABELS["rainfall"], 20.0, 300.0, 100.0, 5.0),
    })
st.caption("N, P and K are on the same scale as the training data, not lab readings in kg per hectare.")

if st.button("Generate Precision Advisory", type="primary"):
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
        st.info("You changed the values. Press the button again to update the advice.")
    best, best_p = advice["top"][0]
    st.success(f"Best match: {best.upper()} ({best_p:.0%} confidence)")
    st.dataframe(
        pd.DataFrame({
            "Rank": [1, 2, 3],
            "Crop": [c for c, _ in advice["top"]],
            "Confidence": [f"{p:.0%}" for _, p in advice["top"]],
        }),
        hide_index=True,
    )
    show_nutrient_gap(best, profiles, advice["inputs"])

st.subheader("Check any crop")
default_index = crops.index(advice["top"][0][0]) if advice else 0
chosen = st.selectbox("Pick a crop to see how your field fits it", crops, index=default_index)
table, inside = explorer_table(chosen, profiles, values)
st.write(f"**{inside} of 7 measures** are within the typical range for {chosen}.")
st.dataframe(table, hide_index=True)

with st.expander("About this model and its limits"):
    if metrics:
        st.write(
            f"{metrics['model']} trained on {metrics['n_rows']:,} rows covering {metrics['n_crops']} crops. "
            f"Accuracy on a held-out 20% test set: {metrics['holdout_accuracy']:.1%}."
        )
        st.write(metrics["data_note"])
    st.write("It does not know your local market, water supply, pests or soil history. Talk to your agriculture officer before you decide.")

st.markdown("---")
st.caption("© 2026 Abhishek Hitabutti. All rights reserved. Copying or reuse of this app without permission is prohibited.")
