"""Crop Doctor: photo analysis of plant problems, with reviewed guidance only."""
import os
import sys
from html import escape
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import pandas as pd  # noqa: E402
import streamlit as st  # noqa: E402

import diagnosis  # noqa: E402
import i18n  # noqa: E402
import spray_weather  # noqa: E402
import ui  # noqa: E402
from districts import DISTRICTS  # noqa: E402
from i18n import t  # noqa: E402

st.set_page_config(page_title="Crop Doctor | KisanDrishti", page_icon="🩺")
ui.inject_css()
i18n.language_picker()
ui.hero(t("Crop Doctor"), t("Photograph a sick plant, pest or weed. Get clear steps, spray timing and safety advice."), "🩺")

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
        st.markdown(f"- {t(item)}")


def type_label(kind):
    return t(TYPE_LABEL[kind])


def expert_help_box(reasons=None):
    with st.container(border=True):
        st.markdown("#### " + t("Get expert help"))
        if reasons:
            st.write(t("Go to an expert at once if:"))
            bullets(reasons)
        bullets([
            "Your nearest Krishi Vigyan Kendra (KVK) or Raitha Samparka Kendra, or your agriculture officer. Take the photos or a fresh sample.",
            "Kisan Call Centre: 1800-180-1551.",
        ])


def reference_image(entry_id):
    for ext in ("jpg", "jpeg", "png"):
        path = IMAGES / f"{entry_id}.{ext}"
        if path.exists():
            st.image(str(path), caption=t("Reference photo"))
            return


def translate_spray_message(message):
    prefix, suffix = "Best day to spray in this forecast: ", ". Avoid wet or windy days."
    if message.startswith(prefix) and message.endswith(suffix):
        return t(prefix + "{day}" + suffix, day=message[len(prefix):-len(suffix)])
    return t(message)


def spray_window_box(district):
    st.markdown("**" + t("Best day to spray") + "**")
    try:
        daily = spray_weather.fetch_daily(*DISTRICTS[district])
        rows, message = spray_weather.spray_window(daily)
    except Exception:
        st.info(t("Could not load the forecast. Check the Weather page before you spray."))
        return
    st.write(translate_spray_message(message))
    table = pd.DataFrame(rows).drop(columns=["_key"])
    table["Spraying"] = table["Spraying"].map(t)
    st.dataframe(table.rename(columns={c: t(c) for c in table.columns}), hide_index=True)
    st.caption(t("Forecast for {district}. Simple rules: wait if rain is 2.5 mm or more or gusts reach 30 km/h.", district=district))


def render_entry(entry, district, confirm=False):
    if confirm:
        ui.note(t("This is a likely match, not a certain one. Confirm with your KVK or agriculture officer before you spray anything."), "warn")
    reference_image(entry["id"])
    st.markdown("#### " + t("What it looks like"))
    bullets(entry["look_for"])
    if entry.get("not_to_confuse"):
        st.markdown("**" + t("Do not confuse with") + "**")
        bullets(entry["not_to_confuse"])
    st.write(t(entry["why_it_happens"]))

    st.markdown("#### " + t("Do this first (no spray)"))
    bullets(entry["act_now"])

    chem = entry["chemical"]
    label = "Herbicide guidance" if entry["type"] == "weed" else "Pesticide guidance"
    with st.expander(t("{label}: what to use and when", label=t(label)), expanded=True):
        st.markdown("**" + t("Options commonly advised") + "**")
        st.dataframe(pd.DataFrame(chem["options"]).rename(columns={"active": t("Active ingredient"), "kind": t("Type"), "note": t("Note")}),
                     hide_index=True)
        st.caption(t("Ask a licensed dealer for a product with this active ingredient. Check that the label lists your crop and this problem.")
                   + " " + t(diagnosis.NO_DOSE_NOTE))
        st.markdown("**" + t("When to apply") + "**")
        bullets(chem["when"])
        spray_window_box(district)
        st.markdown("**" + t("Spray timing rules for every product") + "**")
        bullets(diagnosis.SPRAY_TIMING)

    with st.expander(t("Precautions and safety"), expanded=True):
        if entry.get("precautions"):
            st.markdown("**" + t("For this problem") + "**")
            bullets(entry["precautions"])
        st.markdown("**" + t("For every spray") + "**")
        bullets(diagnosis.SAFETY)

    expert_help_box(entry["see_expert_if"])
    with st.expander(t("Sources")):
        for s in entry["sources"]:
            st.markdown(f"- [{s['title']}]({s['url']})")
        st.caption(t("Reviewed {date}. Some sources are from outside India. Products must be registered in India for your crop, so confirm with your agriculture officer.",
                     date=entry["last_checked"]))


def render_result(state):
    result, district = state["result"], state["district"]
    decision = diagnosis.decide(result, KB)
    mode = decision["mode"]
    head = (f'<div class="kd-card"><h4>{escape(result["name"])}</h4>'
            f'{ui.badge(type_label(result["category"]), result["category"])}'
            f'{ui.badge(t("Confidence: {level}", level=t(result["confidence"])), result["confidence"])}'
            f'<div>{escape(t("Crop seen: {crop}", crop=result["crop"]))}</div></div>')
    st.markdown(head, unsafe_allow_html=True)
    if result["symptoms_seen"]:
        st.markdown("**" + t("What we can see in your photo") + "**")
        bullets(result["symptoms_seen"])
    if result["could_also_be"]:
        st.markdown("**" + t("It could also be:") + "** " + ", ".join(result["could_also_be"]))

    if mode == "retake":
        ui.note(t("The photo is not clear enough to say what the problem is.") + " " + (result["photo_tip"] or ""), "warn")
        bullets(PHOTO_TIPS)
        st.write(t("Do not spray anything until you know the cause."))
        expert_help_box()
    elif mode == "healthy":
        st.success(t("The plant looks healthy in this photo. Keep checking your field every few days."))
    elif mode == "non_pesticide":
        st.info(t("This looks like a nutrient or weather-stress problem, not a pest or disease. Spraying a pesticide will not fix it. Get your soil tested (see Soil Health Card on the Schemes and Help page) and ask your agriculture officer."))
        expert_help_box()
    elif mode == "expert_only":
        ui.note(t("We cannot give spray advice for this one with enough certainty. Spraying the wrong product wastes money and can harm your crop and your health."), "stop")
        st.markdown("**" + t("What to do now") + "**")
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
tab_photo, tab_browse = st.tabs([t("Analyse a photo"), t("Browse common problems")])

with tab_photo:
    ui.steps_row([("📸", t("Take a photo")), ("🔍", t("We analyse it")), ("✅", t("Get guidance"))])
    with st.expander(t("How to take a good photo")):
        bullets(PHOTO_TIPS)
    c1, c2 = st.columns(2)
    hint_labels = {t(h): h for h in CROP_HINTS}
    crop_hint = hint_labels[c1.selectbox(t("Which crop is it?"), list(hint_labels))]
    district = c2.selectbox(t("Your district (for spray timing)"), sorted(DISTRICTS), index=sorted(DISTRICTS).index("Mysuru"))
    uploaded = st.file_uploader(t("Upload a photo"), type=["jpg", "jpeg", "png"])
    with st.expander(t("Or use the camera")):
        camera = st.camera_input(t("Take a photo now"))
    image = uploaded or camera

    provider, api_key, model = get_provider()
    if not api_key:
        ui.note(t("Photo analysis is not switched on yet. You can still use the Browse common problems tab."), "warn")
        with st.expander(t("For the app owner")):
            st.write(t("Add a free Gemini API key as GEMINI_API_KEY in this app's Secrets (never in GitHub). See the README."))
    elif st.button(t("Analyse photo"), type="primary"):
        if image is None:
            st.warning(t("Please add a photo first."))
        elif st.session_state["doctor_count"] >= MAX_PER_SESSION:
            st.warning(t("You have reached the limit of photos for this visit. Please come back later or visit your KVK."))
        else:
            try:
                with st.spinner(t("Looking at your photo...")):
                    result = diagnosis.analyze(image.getvalue(), api_key, KB, provider=provider, model=model, crop_hint=crop_hint, language=i18n.current_lang())
                st.session_state["doctor"] = {"result": result, "district": district}
                st.session_state["doctor_count"] += 1
            except diagnosis.AnalysisError as exc:
                st.error(str(exc))

    if "doctor" in st.session_state:
        render_result(st.session_state["doctor"])
    st.caption(t(PRIVACY[provider]) + " " + t("The AI only identifies the problem. Treatment advice comes from reviewed sources. Always confirm before you spray."))

with tab_browse:
    st.write(t("Reviewed guidance for common problems. More are added as they are checked by experts."))
    options = {f"{t(e['name'])} ({type_label(e['type'])})": e for e in KB}
    if options:
        pick = st.selectbox(t("Choose a problem"), list(options))
        browse_district = st.selectbox(t("Your district"), sorted(DISTRICTS), index=sorted(DISTRICTS).index("Mysuru"), key="browse_district")
        render_entry(options[pick], browse_district)
    else:
        st.info(t("The guidance library could not be loaded."))

ui.feedback_box()
st.markdown("---")
st.caption(t("© 2026 Abhishek Hitabutti. All rights reserved. Copying or reuse of this app without permission is prohibited."))
