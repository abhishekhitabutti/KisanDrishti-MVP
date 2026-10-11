"""Crop Doctor: photo analysis of plant problems, with reviewed guidance only."""
import os
import sys
from html import escape
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import pandas as pd  # noqa: E402
import streamlit as st  # noqa: E402

import diagnosis  # noqa: E402
import spray_weather  # noqa: E402
import ui  # noqa: E402
from districts import DISTRICTS  # noqa: E402

st.set_page_config(page_title="Crop Doctor | KisanDrishti", page_icon="🩺")
ui.inject_css()
ui.hero("Crop Doctor", "Photograph a sick plant, pest or weed. Get clear steps, spray timing and safety advice.", "🩺")

KB = diagnosis.load_kb()
IMAGES = Path(__file__).resolve().parent.parent / "images" / "issues"
MAX_PER_SESSION = 5
CROP_HINTS = ["Not sure", "Rice (paddy)", "Ragi (finger millet)", "Maize", "Jowar (sorghum)", "Bajra", "Wheat",
              "Tur (pigeon pea)", "Bengal gram (chickpea)", "Green gram", "Black gram", "Horse gram", "Groundnut",
              "Sunflower", "Soybean", "Cotton", "Sugarcane", "Tomato", "Chilli", "Onion", "Potato", "Brinjal",
              "Cabbage", "Okra", "Banana", "Mango", "Grapes", "Pomegranate", "Areca nut", "Coconut", "Coffee",
              "Pepper", "Turmeric", "Other"]
TYPE_LABEL = {"disease": "Disease", "pest": "Pest", "weed": "Weed", "nutrient_deficiency": "Nutrient problem",
              "abiotic_stress": "Weather or soil stress", "healthy": "Healthy", "unclear": "Not clear"}
PHOTO_TIPS = [
    "Take the photo in daylight, without shadow, and hold the phone steady.",
    "Take one close-up of the affected leaf, fruit or insect so the spots or damage fill the picture.",
    "Take a second photo of the whole plant, and show both sides of the leaf if you can.",
    "One problem per photo. Do not include hands, tools or many different plants.",
]


def secret(name):
    try:
        value = st.secrets.get(name)
    except Exception:
        value = None
    return value or os.environ.get(name)


def get_provider():
    """Prefer the free Gemini key, then Anthropic. Returns (provider, key, model) or (None, None, None)."""
    if secret("GEMINI_API_KEY"):
        return "gemini", secret("GEMINI_API_KEY"), secret("GEMINI_MODEL") or diagnosis.DEFAULT_GEMINI_MODEL
    if secret("ANTHROPIC_API_KEY"):
        return "anthropic", secret("ANTHROPIC_API_KEY"), secret("ANTHROPIC_MODEL") or diagnosis.DEFAULT_MODEL
    return None, None, None


PRIVACY = {
    "gemini": "Your photo is sent to Google's Gemini service for analysis. On Google's free tier, Google may use it to improve its "
              "products. Location data is removed from the photo first. Please do not upload photos with people in them. "
              "This app does not store your photo.",
    "anthropic": "Your photo is sent to an AI service (Anthropic) for analysis. Location data is removed from the photo first. "
                 "This app does not store your photo.",
    None: "Photo analysis is switched off, so no photo is sent anywhere.",
}


def bullets(items):
    for item in items:
        st.markdown(f"- {item}")


def expert_help_box(reasons=None):
    with st.container(border=True):
        st.markdown("#### Get expert help")
        if reasons:
            st.write("Go to an expert at once if:")
            bullets(reasons)
        bullets([
            "Your nearest Krishi Vigyan Kendra (KVK) or Raitha Samparka Kendra, or your agriculture officer. Take the photos or a fresh sample.",
            "Kisan Call Centre: 1800-180-1551.",
        ])


def reference_image(entry_id):
    for ext in ("jpg", "jpeg", "png"):
        path = IMAGES / f"{entry_id}.{ext}"
        if path.exists():
            st.image(str(path), caption="Reference photo")
            return


def spray_window_box(district):
    st.markdown("**Best day to spray**")
    try:
        daily = spray_weather.fetch_daily(*DISTRICTS[district])
        rows, message = spray_weather.spray_window(daily)
    except Exception:
        st.info("Could not load the forecast. Check the Weather page before you spray.")
        return
    st.write(message)
    st.dataframe(pd.DataFrame(rows).drop(columns=["_key"]), hide_index=True)
    st.caption(f"Forecast for {district}. Simple rules: wait if rain is 2.5 mm or more or gusts reach 30 km/h.")


def render_entry(entry, district, confirm=False):
    if confirm:
        ui.note("This is a likely match, not a certain one. Confirm with your KVK or agriculture officer before you spray anything.", "warn")
    reference_image(entry["id"])
    st.markdown("#### What it looks like")
    bullets(entry["look_for"])
    if entry.get("not_to_confuse"):
        st.markdown("**Do not confuse with**")
        bullets(entry["not_to_confuse"])
    st.write(entry["why_it_happens"])

    st.markdown("#### Do this first (no spray)")
    bullets(entry["act_now"])

    chem = entry["chemical"]
    label = "Herbicide guidance" if entry["type"] == "weed" else "Pesticide guidance"
    with st.expander(f"{label}: what to use and when", expanded=True):
        st.markdown("**Options commonly advised**")
        st.dataframe(pd.DataFrame(chem["options"]).rename(columns={"active": "Active ingredient", "kind": "Type", "note": "Note"}),
                     hide_index=True)
        st.caption("Ask a licensed dealer for a product with this active ingredient. Check that the label lists your crop and this problem. "
                   + diagnosis.NO_DOSE_NOTE)
        st.markdown("**When to apply**")
        bullets(chem["when"])
        spray_window_box(district)
        st.markdown("**Spray timing rules for every product**")
        bullets(diagnosis.SPRAY_TIMING)

    with st.expander("Precautions and safety", expanded=True):
        if entry.get("precautions"):
            st.markdown("**For this problem**")
            bullets(entry["precautions"])
        st.markdown("**For every spray**")
        bullets(diagnosis.SAFETY)

    expert_help_box(entry["see_expert_if"])
    with st.expander("Sources"):
        for s in entry["sources"]:
            st.markdown(f"- [{s['title']}]({s['url']})")
        st.caption(f"Reviewed {entry['last_checked']}. Some sources are from outside India. Products must be registered in India "
                   "for your crop, so confirm with your agriculture officer.")


def render_result(state):
    result, district = state["result"], state["district"]
    decision = diagnosis.decide(result, KB)
    mode = decision["mode"]
    head = (f'<div class="kd-card"><h4>{escape(result["name"])}</h4>'
            f'{ui.badge(TYPE_LABEL[result["category"]], result["category"])}'
            f'{ui.badge("Confidence: " + result["confidence"], result["confidence"])}'
            f'<div>Crop seen: {escape(result["crop"])}</div></div>')
    st.markdown(head, unsafe_allow_html=True)
    if result["symptoms_seen"]:
        st.markdown("**What we can see in your photo**")
        bullets(result["symptoms_seen"])
    if result["could_also_be"]:
        st.markdown("**It could also be:** " + ", ".join(result["could_also_be"]))

    if mode == "retake":
        ui.note("The photo is not clear enough to say what the problem is. " + (result["photo_tip"] or ""), "warn")
        bullets(PHOTO_TIPS)
        st.write("Do not spray anything until you know the cause.")
        expert_help_box()
    elif mode == "healthy":
        st.success("The plant looks healthy in this photo. Keep checking your field every few days.")
    elif mode == "non_pesticide":
        st.info("This looks like a nutrient or weather-stress problem, not a pest or disease. Spraying a pesticide will not fix it. "
                "Get your soil tested (see Soil Health Card on the Schemes and Help page) and ask your agriculture officer.")
        expert_help_box()
    elif mode == "expert_only":
        ui.note("We cannot give spray advice for this one with enough certainty. Spraying the wrong product wastes money and can harm "
                "your crop and your health.", "stop")
        st.markdown("**What to do now**")
        bullets([
            "Take clear close-up photos and keep a fresh affected sample if you can.",
            "Show them at your nearest KVK or Raitha Samparka Kendra or to your agriculture officer.",
            "Do not spray anything until the cause is known.",
            "Remove and destroy badly affected plant parts if only a few plants are affected.",
        ])
        expert_help_box()
    else:
        render_entry(decision["entry"], district, decision.get("confirm", False))


st.session_state.setdefault("doctor_count", 0)
tab_photo, tab_browse = st.tabs(["Analyse a photo", "Browse common problems"])

with tab_photo:
    ui.steps_row([("📸", "Take a photo"), ("🔍", "We analyse it"), ("✅", "Get guidance")])
    with st.expander("How to take a good photo"):
        bullets(PHOTO_TIPS)
    c1, c2 = st.columns(2)
    crop_hint = c1.selectbox("Which crop is it?", CROP_HINTS)
    district = c2.selectbox("Your district (for spray timing)", sorted(DISTRICTS), index=sorted(DISTRICTS).index("Mysuru"))
    uploaded = st.file_uploader("Upload a photo", type=["jpg", "jpeg", "png"])
    with st.expander("Or use the camera"):
        camera = st.camera_input("Take a photo now")
    image = uploaded or camera

    provider, api_key, model = get_provider()
    if not api_key:
        ui.note("Photo analysis is not switched on yet. You can still use the Browse common problems tab.", "warn")
        with st.expander("For the app owner"):
            st.write("Add a free Gemini API key as GEMINI_API_KEY in this app's Secrets (never in GitHub). See the README.")
    elif st.button("Analyse photo", type="primary"):
        if image is None:
            st.warning("Please add a photo first.")
        elif st.session_state["doctor_count"] >= MAX_PER_SESSION:
            st.warning("You have reached the limit of photos for this visit. Please come back later or visit your KVK.")
        else:
            try:
                with st.spinner("Looking at your photo..."):
                    result = diagnosis.analyze(image.getvalue(), api_key, KB, provider=provider, model=model, crop_hint=crop_hint)
                st.session_state["doctor"] = {"result": result, "district": district}
                st.session_state["doctor_count"] += 1
            except diagnosis.AnalysisError as exc:
                st.error(str(exc))

    if "doctor" in st.session_state:
        render_result(st.session_state["doctor"])
    st.caption(PRIVACY[provider] + " The AI only identifies the problem. Treatment advice comes from reviewed sources. "
               "Always confirm before you spray.")

with tab_browse:
    st.write("Reviewed guidance for common problems. More are added as they are checked by experts.")
    options = {f"{e['name']} ({TYPE_LABEL[e['type']]})": e for e in KB}
    if options:
        pick = st.selectbox("Choose a problem", list(options))
        browse_district = st.selectbox("Your district", sorted(DISTRICTS), index=sorted(DISTRICTS).index("Mysuru"), key="browse_district")
        render_entry(options[pick], browse_district)
    else:
        st.info("The guidance library could not be loaded.")

st.markdown("---")
st.caption("© 2026 Abhishek Hitabutti. All rights reserved. Copying or reuse of this app without permission is prohibited.")
