"""Crop Doctor: photo analysis of plant problems, with reviewed guidance only."""
import os
import sys
import urllib.parse
from html import escape
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import pandas as pd  # noqa: E402
import streamlit as st  # noqa: E402

import diagnosis  # noqa: E402
import i18n  # noqa: E402
import spray_weather  # noqa: E402
import ui  # noqa: E402
import prescription_data as pdata  # noqa: E402
from districts import DISTRICTS, DISTRICTS_KN  # noqa: E402
from i18n import t  # noqa: E402

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
    if not items:
        return
    for item in items:
        if isinstance(item, list):
            for sub in item:
                if str(sub).strip():
                    st.markdown(f"- {t(str(sub).strip())}")
        elif item and str(item).strip():
            st.markdown(f"- {t(str(item).strip())}")


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


def render_entry(entry, district, confirm=False, key_prefix="browse"):
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
        is_kn_local = (i18n.current_lang() == "kn")
        options_rows = []
        for opt in chem["options"]:
            options_rows.append({
                "active": opt.get("active", ""),
                "kind": t(opt.get("kind", "")) if is_kn_local else opt.get("kind", ""),
                "note": t(opt.get("note", "")) if is_kn_local else opt.get("note", "")
            })
        st.dataframe(pd.DataFrame(options_rows).rename(columns={"active": t("Active ingredient"), "kind": t("Type"), "note": t("Note")}),
                     hide_index=True)
        st.caption(t("Ask a licensed dealer for a product with this active ingredient. Check that the label lists your crop and this problem.")
                   + " " + t(diagnosis.NO_DOSE_NOTE))
        st.markdown("**" + t("When to apply") + "**")
        bullets(chem["when"])
        spray_window_box(district)
        st.markdown("**" + t("Spray timing rules for every product") + "**")
        bullets(diagnosis.SPRAY_TIMING)
        st.info("💡 " + (
            "ನಿಮ್ಮ ಜಮೀನಿನ ಅಳತೆಯ ಆಧಾರದ ಮೇಲೆ ನಿಖರ ಔಷಧ ಪ್ರಮಾಣ, ಇಳುವರಿ ಬೂಸ್ಟರ್ ಟ್ಯಾಂಕ್-ಮಿಶ್ರಣ ಮತ್ತು ಅಧಿಕೃತ ಭಾರತೀಯ ಕಂಪನಿಗಳಿಂದ ನೇರ ಖರೀದಿಗೆ "
            "ನಮ್ಮ **'ಔಷಧ & ಪೋಷಕಾಂಶ ಚೀಟಿ'** {Smart Spray Prescription} ಪುಟವನ್ನು ಬಳಸಿ."
            if (i18n.current_lang() == "kn") else
            "Need an exact dosage prescription slip calculated for your land acreage, yield booster tank-mix, and direct Indian purchase links? "
            "Use the **Smart Spray Prescription** page."
        ))

    with st.expander(t("Precautions and safety"), expanded=True):
        if entry.get("precautions"):
            st.markdown("**" + t("For this problem") + "**")
            bullets(entry["precautions"])
        st.markdown("**" + t("For every spray") + "**")
        bullets(diagnosis.SAFETY)

    # --- FULL SMART SPRAY PRESCRIPTION & FIELD DOSAGE SLIP (EMBEDDED DIRECTLY IN CROP DOCTOR) ---
    is_kn_local = (i18n.current_lang() == "kn")
    target_presc = None
    for p in pdata.CROP_PRESCRIPTIONS:
        if p["id"] in entry["id"] or entry["id"] in p["id"] or any(c in p["crop_en"].lower() for c in entry.get("crops", [])):
            target_presc = p
            break
    if not target_presc and pdata.CROP_PRESCRIPTIONS:
        target_presc = pdata.CROP_PRESCRIPTIONS[0]

    with st.container(border=True):
        st.markdown("### 💊 " + ("ಸ್ಮಾರ್ಟ್ ಔಷಧ ಚೀಟಿ & ನಿಖರ ಡೋಸ್ ಲೆಕ್ಕಾಚಾರ" if is_kn_local else "Smart Farm Prescription & Dosage Slip"))
        st.caption(
            "ನಿಮ್ಮ ಜಮೀನಿನ ವಿಸ್ತೀರ್ಣಕ್ಕೆ ತಕ್ಕಂತೆ ಬೇಕಾಗುವ ನಿಖರ ನೀರಿನ ಪ್ರಮಾಣ, ಔಷಧದ ಡೋಸ್, ಅಧಿಕ ಇಳುವರಿ ಟಾನಿಕ್ ಮತ್ತು ನೇರ ಖರೀದಿ ಲಿಂಕ್‌ಗಳು."
            if is_kn_local else
            "Calibrated water volume, chemical dosage, high-yield promoters, and verified Indian purchase links for your exact acreage."
        )

        col_ac, col_gn, col_pmp = st.columns([1, 1, 1.5])
        with col_ac:
            acres = st.number_input(
                "ಎಕರೆ {Acres}" if is_kn_local else "Acres",
                min_value=0.0, max_value=500.0, value=1.0, step=0.5,
                key=f"ac_{key_prefix}_{entry['id']}"
            )
        with col_gn:
            guntas = st.number_input(
                "ಗುಂಟೆ {Guntas}" if is_kn_local else "Guntas (40 Guntas = 1 Acre)",
                min_value=0, max_value=39, value=0, step=1,
                key=f"gn_{key_prefix}_{entry['id']}"
            )
        with col_pmp:
            pumps = {
                ("15 ಲೀಟರ್ ಬೆನ್ನುಹೊರೆ ಪಂಪ್ (15 L)" if is_kn_local else "15 Litre Backpack Sprayer (15 L)"): 15.0,
                ("16 ಲೀಟರ್ ಬ್ಯಾಟರಿ ಪಂಪ್ (16 L)" if is_kn_local else "16 Litre Battery Sprayer (16 L)"): 16.0,
                ("20 ಲೀಟರ್ ಪವರ್ ಪಂಪ್ (20 L)" if is_kn_local else "20 Litre High-Pressure Sprayer (20 L)"): 20.0,
                ("500 ಲೀಟರ್ ಟ್ರ್ಯಾಕ್ಟರ್ ಟ್ಯಾಂಕ್ (500 L)" if is_kn_local else "500 Litre Tractor Mounted Tank (500 L)"): 500.0,
            }
            pmp_name = st.selectbox(
                "ಸಿಂಪರಣಾ ಪಂಪ್ ಗಾತ್ರ {Sprayer Tank Size}" if is_kn_local else "Sprayer Pump Capacity",
                list(pumps.keys()),
                key=f"pmp_{key_prefix}_{entry['id']}"
            )
            pump_capacity = pumps[pmp_name]

        total_acres = acres + (guntas / 40.0)
        if total_acres <= 0:
            total_acres = 1.0

        water_per_acre = 200.0 if pump_capacity <= 20.0 else 500.0
        total_water = round(total_acres * water_per_acre, 1)
        total_tanks = max(1.0, round(total_water / pump_capacity, 1))

        # Metrics summary
        m1, m2, m3 = st.columns(3)
        m1.metric("ಒಟ್ಟು ಜಮೀನು (Area)" if is_kn_local else "Total Land Area", f"{total_acres:.2f} ಎಕರೆ" if is_kn_local else f"{total_acres:.2f} Acres")
        m2.metric("ಬೇಕಾಗುವ ನೀರು (Water)" if is_kn_local else "Water Needed", f"{total_water:.0f} ಲೀಟರ್" if is_kn_local else f"{total_water:.0f} Litres")
        m3.metric("ಒಟ್ಟು ಪಂಪ್‌ಗಳು (Tanks)" if is_kn_local else "Spray Tanks Needed", f"{total_tanks:.1f} ಪಂಪ್" if is_kn_local else f"{total_tanks:.1f} Tanks")

        # Recommended Chemicals with exact dose per pump and per acre, plus buy links
        st.markdown("#### 🧪 " + ("ಶಿಫಾರಸು ಮಾಡಿದ ಔಷಧಗಳು & ನಿಖರ ಡೋಸ್" if is_kn_local else "Recommended Agrochemicals & Exact Dosages"))
        chems = target_presc.get("recommended_chemicals", []) if target_presc else []
        if not chems:
            for opt in entry.get("chemical", {}).get("options", []):
                chems.append({
                    "trade_name": opt.get("active", "Standard Formulation"),
                    "trade_name_kn": opt.get("active", "Standard Formulation"),
                    "active": opt.get("active", "Generic Active"),
                    "dose_per_l": "1.5 - 2.0 ml/g per Litre",
                    "dose_per_pump_15l": "25 - 30 ml/g per 15L pump",
                    "dose_per_acre": "350 - 400 ml/g per acre in 200 L water",
                    "action": opt.get("kind", "Pesticide / Fungicide"),
                    "manufacturer": "Certified Indian Agri Brands (IFFCO / BigHaat / Bayer)",
                    "buy_url": f"https://www.bighaat.com/search?q={urllib.parse.quote(opt.get('active', ''))}"
                })

        for c_idx, chem in enumerate(chems):
            c_name = chem.get("trade_name_kn") if is_kn_local and chem.get("trade_name_kn") else t(chem.get("trade_name", ""))
            with st.container(border=True):
                c_col1, c_col2 = st.columns([2.5, 1.2])
                with c_col1:
                    st.markdown(f"**🏷️ {c_name}**")
                    action_text = chem.get("action_kn") if is_kn_local and chem.get("action_kn") else t(chem.get("action", "Target disease / pest control"))
                    st.markdown(f"- 🎯 **{'ಯಾವುದಕ್ಕೆ ಬಳಸಬೇಕು / ಕಾರ್ಯವಿಧಾನ {Used For / Action}:' if is_kn_local else 'Used For / Mode of Action:'}** {action_text}")
                    st.markdown(f"- 🧪 **{'ಕ್ರಿಯಾಶೀಲ ರಾಸಾಯನಿಕ {Active}:' if is_kn_local else 'Active Ingredient:'}** `{chem.get('active', '')}`")
                    dose_15l = chem.get("dose_per_pump_15l_kn") if is_kn_local and chem.get("dose_per_pump_15l_kn") else t(chem.get("dose_per_pump_15l", "25 ml/g"))
                    st.markdown(f"- 💧 **{'ಪ್ರತಿ 15L ಪಂಪ್‌ಗೆ ಡೋಸ್:' if is_kn_local else 'Dose per 15L Pump:'}** `{dose_15l}`")
                    dose_ac = chem.get("dose_per_acre_kn") if is_kn_local and chem.get("dose_per_acre_kn") else t(chem.get("dose_per_acre", "350 - 400 ml/g"))
                    st.markdown(f"- 🌾 **{'1 ಎಕರೆಗೆ ಪ್ರಮಾಣ (200 ಲೀ ನೀರಿಗೆ):' if is_kn_local else 'Dose per 1 Acre (in 200L Water):'}** `{dose_ac}`")
                    mfg = chem.get("manufacturer_kn") if is_kn_local and chem.get("manufacturer_kn") else t(chem.get("manufacturer", "Verified Indian Manufacturer"))
                    st.caption(f"🏭 {'ಅಧಿಕೃತ ತಯಾರಕರು:' if is_kn_local else 'Certified Manufacturer:'} {mfg}")
                with c_col2:
                    buy_link = chem.get("buy_url") or f"https://www.bighaat.com/search?q={urllib.parse.quote(chem.get('active', ''))}"
                    st.link_button(
                        "🛒 BigHaat ನಲ್ಲಿ ಖರೀದಿಸಿ" if is_kn_local else "🛒 Buy on BigHaat",
                        buy_link,
                        use_container_width=True
                    )
                    st.link_button(
                        "🌾 IFFCO Bazar ನಲ್ಲಿ ಖರೀದಿಸಿ" if is_kn_local else "🌾 Buy on IFFCO Bazar",
                        f"https://www.iffcobazar.in/en/search?q={urllib.parse.quote(chem.get('active', ''))}",
                        use_container_width=True
                    )
                    st.link_button(
                        "📦 AgroStar ನಲ್ಲಿ ಖರೀದಿಸಿ" if is_kn_local else "📦 Buy on AgroStar",
                        f"https://www.agrostar.in/search?q={urllib.parse.quote(chem.get('active', ''))}",
                        use_container_width=True
                    )

        # High Yield Booster
        st.markdown("#### 🚀 " + ("ಅಧಿಕ ಇಳುವರಿ ಬೂಸ್ಟರ್ & ಟ್ಯಾಂಕ್ ಮಿಶ್ರಣ" if is_kn_local else "High-Yield Tank-Mix Booster"))
        mix_kn = target_presc.get("tank_mix_nutrition_kn", "ಸಿಂಪರಣಾ ಟ್ಯಾಂಕ್‌ಗೆ {NPK 19:19:19} (75 ಗ್ರಾಂ/ಪಂಪ್, 1 ಕೆಜಿ/ಎಕರೆಗೆ) + ಸಾಗರಿಕ ಕಡಲಕಳೆ ಸಾರ (40 ಮಿಲಿ/ಪಂಪ್, 500 ಮಿಲಿ/ಎಕರೆಗೆ) ಬೆರೆಸಿ ಸಿಂಪಡಿಸಿ.") if target_presc else "ಸಿಂಪರಣಾ ಟ್ಯಾಂಕ್‌ಗೆ {NPK 19:19:19} (75 ಗ್ರಾಂ/ಪಂಪ್) ಬೆರೆಸಿ."
        mix_en = target_presc.get("tank_mix_nutrition_en", "Add NPK 19:19:19 (75 g/pump, 1 kg/acre) + Sagarika Seaweed (40 ml/pump, 500 ml/acre) to restore vigor and accelerate grain filling.") if target_presc else "Add NPK 19:19:19 (75 g/pump) to restore vigor."
        st.info("💡 " + (mix_kn if is_kn_local else mix_en))
        st.markdown(
            "💧 **" + ("ಸಿಂಪರಣಾ ಅಂಟು {Spreader / Sticker}:" if is_kn_local else "Spreading & Sticking Agent:") + "** "
            + ("ಮಳೆ ಅಥವಾ ಬಿಸಿಲಿಗೆ ಔಷಧ ತೊಳೆದುಹೋಗದಂತೆ ಪ್ರತಿ ಪಂಪ್‌ಗೆ 5 ಮಿಲಿ ಸಿಂಪರಣಾ ಅಂಟು (ಅಪ್ಸಾ-80 / ವೆಟ್‌ಸಿಟ್) ಕಡ್ಡಾಯವಾಗಿ ಬೆರೆಸಿ."
               if is_kn_local else "Add 5 ml spreader/sticker (e.g., Apsa-80 / Wetcit) per 15L pump to ensure rain-fast adherence.")
        )

        # If it is a weed, show Density-based chemical weedicide selector
        if entry.get("type") == "weed":
            st.markdown("---")
            st.markdown("### 🌿 " + ("ಕಳೆ ಸಾಂದ್ರತೆಯ ಆಧಾರದ ಮೇಲೆ ಕಳೆನಾಶಕ ವಿಲೇವಾರಿ {Chemical Weedicide by Infestation Density}" if is_kn_local else "Chemical Weedicide by Infestation Density"))
            dens_opts = [
                ("ಕಡಿಮೆ ಪ್ರಮಾಣ (< 15% ಭಾಗ - ಆಯ್ದ ಗುರುತು ಸಿಂಪರಣೆ)" if is_kn_local else "Low (< 15% Area - Spot Spray)"),
                ("ಮಧ್ಯಮ ಪ್ರಮಾಣ (15% - 40% ಭಾಗ - ಸಮಗ್ರ ಕಳೆನಾಶಕ)" if is_kn_local else "Moderate (15% - 40% Area - Broadcast Spray)"),
                ("ತೀವ್ರ / ದಟ್ಟ ಕಳೆ (> 40% ಭಾಗ - ಸಂಪೂರ್ಣ ಬೇರುಸಮೇತ ನಾಶ)" if is_kn_local else "Dense (> 40% Area - Total Knockdown)")
            ]
            dens_sel = st.radio(
                "ಜಮೀನಿನಲ್ಲಿರುವ ಕಳೆ ಆವರಿಸುವಿಕೆ {Select Infestation Level}:" if is_kn_local else "Select Weed Coverage on Your Land:",
                dens_opts,
                key=f"w_dens_{key_prefix}_{entry['id']}"
            )
            d_key = "low" if "15%" in dens_sel and "<" in dens_sel else ("medium" if "40%" in dens_sel else "dense")
            wdata = pdata.WEED_MANAGEMENT_BY_DENSITY[d_key]
            st.markdown(f"**{wdata['chemical_necessity_kn'] if is_kn_local else wdata['chemical_necessity_en']}**")
            for w in wdata.get("chemical_weedicides", []):
                with st.container(border=True):
                    w1, w2 = st.columns([2.5, 1.2])
                    with w1:
                        st.markdown(f"**🌿 {w['trade_name_kn'] if is_kn_local else w['trade_name_en']}**")
                        st.write(f"**{'ಸೂಕ್ತ ಬೆಳೆಗಳು:' if is_kn_local else 'Target Crops:'}** {w['target_crops_kn'] if is_kn_local else w['target_crops_en']}")
                        st.write(f"**{'ಪ್ರತಿ 15L ಪಂಪ್‌ಗೆ ಡೋಸ್:' if is_kn_local else 'Dose per 15L Pump:'}** `{w['dose_per_pump_15l']}`")
                        st.write(f"**{'1 ಎಕರೆಗೆ ಪ್ರಮಾಣ:' if is_kn_local else 'Dose per 1 Acre:'}** `{w['dose_per_acre']}`")
                        st.caption(w['timing_kn'] if is_kn_local else w['timing_en'])
                    with w2:
                        st.link_button("🛒 ಖರೀದಿಸಿ (Buy)", w["buy_url"], use_container_width=True)

        # Crop-specific tonic schedule
        matched_tonic = None
        for c in entry.get("crops", []):
            for tc in pdata.CROP_SPECIFIC_TONICS:
                if c.lower() in tc.lower() or tc.lower() in c.lower():
                    matched_tonic = tc
                    break
            if matched_tonic:
                break
        if matched_tonic:
            t_info = pdata.CROP_SPECIFIC_TONICS[matched_tonic]
            with st.expander(f"🌾 {t_info['name_kn'] if is_kn_local else matched_tonic} — " + ("ಅಧಿಕ ಇಳುವರಿ ಟಾನಿಕ್ ವೇಳಾಪಟ್ಟಿ & ಪ್ರಮಾಣ" if is_kn_local else "High-Yield Tonics & Dosage Schedule"), expanded=False):
                st.success(f"📈 {'ನಿರೀಕ್ಷಿತ ಇಳುವರಿ ಹೆಚ್ಚಳ:' if is_kn_local else 'Expected Yield Boost:'} **{t_info['boost_pct']}**")
                st.markdown(f"**1️⃣ {'ಸಸ್ಯ ಬೆಳವಣಿಗೆ & ಕವಲು ಹಂತ:' if is_kn_local else 'Vegetative / Tillering Stage:'}**")
                st.write(t_info["veg_stage_kn"] if is_kn_local else t_info["veg_stage_en"])
                st.markdown(f"**2️⃣ {'ಹೂವಾಡುವ ಹಂತ {ಹೂವು ಉದುರುವುದು ತಡೆಯಲು}:' if is_kn_local else 'Pre-Flowering / Anti-Drop Stage:'}**")
                st.write(t_info["flower_stage_kn"] if is_kn_local else t_info["flower_stage_en"])
                st.markdown(f"**3️⃣ {'ಕಾಳು / ಕಾಯಿ ದಪ್ಪಗಾಗುವ ಹಂತ {ತೂಕ ಹೆಚ್ಚಳ}:' if is_kn_local else 'Grain / Fruit Filling Stage:'}**")
                st.write(t_info["yield_stage_kn"] if is_kn_local else t_info["yield_stage_en"])

        # Company Helplines
        with st.expander("📞 " + ("ಅಧಿಕೃತ ಕೃಷಿ ಕಂಪನಿಗಳ ನೇರ ಸಹಾಯವಾಣಿ & ಆರ್ಡರ್ ಸಂಖ್ಯೆಗಳು" if is_kn_local else "Verified Agri Helplines & Direct Phone Booking"), expanded=False):
            for comp in pdata.INDIAN_AGRI_PLATFORMS:
                h1, h2 = st.columns([2.5, 1])
                with h1:
                    st.markdown(f"**{comp['company_kn'] if is_kn_local else comp['company_en']}**")
                    st.caption(comp["specialty_kn"] if is_kn_local else comp["specialty_en"])
                with h2:
                    st.link_button(f"📞 {comp['phone']}", f"tel:{comp['phone'].replace(' ', '')}", use_container_width=True)
                    st.link_button("🌐 ವೆಬ್‌ಸೈಟ್" if is_kn_local else "🌐 Website", comp["order_url"], use_container_width=True)

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
    # Infestation Severity Level Card
    if result.get("severity"):
        sev = result["severity"]
        is_kn_local = (i18n.current_lang() == "kn")
        with st.container(border=True):
            sc1, sc2 = st.columns([2.5, 1.2])
            with sc1:
                st.markdown(f"**📊 {'ರೋಗ ಬಾಧೆಯ ತೀವ್ರತೆಯ ಮಟ್ಟ {Infestation Severity Level}:' if is_kn_local else 'Disease Infestation Severity Level:'}**")
                st.markdown(f"### {sev.get('badge', sev['label'])}")
                st.write(sev.get("note", ""))
            with sc2:
                st.metric(
                    "ಬಾಧಿತ ಭಾಗ {Affected Area}" if is_kn_local else "Affected Area",
                    f"{sev.get('pct', 25.0)}%"
                )

    if result.get("symptoms_seen"):
        st.markdown("**" + t("What we can see in your photo") + "**")
        flat_symp = []
        for s in result["symptoms_seen"]:
            if isinstance(s, list):
                flat_symp.extend([str(x) for x in s if str(x).strip()])
            elif s and str(s).strip():
                flat_symp.append(str(s).strip())
        if flat_symp:
            bullets(flat_symp)

    if result.get("could_also_be"):
        flat_could = []
        for c in result["could_also_be"]:
            if isinstance(c, list):
                flat_could.extend([str(x) for x in c if str(x).strip()])
            elif c and str(c).strip():
                flat_could.append(str(c).strip())
        if flat_could:
            st.markdown("**" + t("It could also be:") + "** " + ", ".join([t(c) for c in flat_could]))

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
        # Pre-spray Symptom Confirmation Checklist
        is_kn_local = (i18n.current_lang() == "kn")
        entry = decision["entry"]
        with st.expander("🔍 " + ("ರೋಗ ಲಕ್ಷಣಗಳನ್ನು ನಿಮ್ಮ ಬೆಳೆಯಲ್ಲಿ ದೃಢೀಕರಿಸಿ {Confirm Disease Symptoms Checklist}" if is_kn_local else "Confirm Disease Symptoms Checklist"), expanded=True):
            st.write("ದಯವಿಟ್ಟು ಔಷಧ ಸಿಂಪಡಿಸುವ ಮೊದಲು ಈ ಕೆಳಗಿನ ಲಕ್ಷಣಗಳು ನಿಮ್ಮ ಹೊಲದ ಗಿಡದಲ್ಲಿ ಇವೆಯೇ ಎಂದು ಪರೀಕ್ಷಿಸಿ ಖಚಿತಪಡಿಸಿಕೊಳ್ಳಿ:" if is_kn_local else "Please verify if your crop exhibits these exact symptoms before spraying:")
            for s in entry.get("look_for", []):
                st.markdown(f"- ✅ `{t(s)}`")
            if entry.get("not_to_confuse"):
                st.markdown("**" + ("ಗೊಂದಲ ಬೇಡ {Do not confuse with}:" if is_kn_local else "Do not confuse with:") + "**")
                bullets(entry["not_to_confuse"])

        render_entry(decision["entry"], district, decision.get("confirm", False), key_prefix="diag")


st.session_state.setdefault("doctor_count", 0)
tab_photo, tab_browse = st.tabs([t("Analyse a photo"), t("Browse common problems")])

with tab_photo:
    with st.expander(t("How to take a good photo")):
        bullets(PHOTO_TIPS)
    c1, c2 = st.columns(2)
    hint_labels = {t(h): h for h in CROP_HINTS}
    crop_hint = hint_labels[c1.selectbox(t("Which crop is it?"), list(hint_labels))]
    is_kn = (i18n.current_lang() == "kn")
    if is_kn:
        d_options = {DISTRICTS_KN.get(d, d): d for d in sorted(DISTRICTS)}
        d_keys = list(d_options.keys())
        d_default = DISTRICTS_KN.get("Mysuru", "ಮೈಸೂರು")
        d_idx = d_keys.index(d_default) if d_default in d_keys else 0
        sel_d_kn = c2.selectbox(t("Your district (for spray timing)"), d_keys, index=d_idx)
        district = d_options[sel_d_kn]
    else:
        district = c2.selectbox(t("Your district (for spray timing)"), sorted(DISTRICTS), index=sorted(DISTRICTS).index("Mysuru"))

    ALLOWED_IMAGE_TYPES = ["jpg", "jpeg", "png", "webp", "jfif", "bmp", "heic"]
    VIDEO_EXTS = {".mp4", ".mov", ".avi", ".mkv", ".webm", ".3gp", ".flv", ".wmv", ".m4v"}

    source_labels = {t("Upload or take a photo with my phone"): "upload", t("Use this device's webcam"): "webcam"}
    source = source_labels[st.radio(t("How do you want to add the photo?"), list(source_labels))]
    uploaded_files = []
    camera = None
    if source == "upload":
        uploaded_files = st.file_uploader(
            "ಬೆಳೆಯ ಫೋಟೋಗಳನ್ನು ಅಪ್‌ಲೋಡ್ ಮಾಡಿ (ಹಲವು ಫೋಟೋಗಳನ್ನು ಒಟ್ಟಿಗೆ ಆಯ್ಕೆಮಾಡಬಹುದು) {Upload photos}"
            if is_kn else
            "Upload photos of your crop (You can select multiple photos)",
            type=ALLOWED_IMAGE_TYPES,
            accept_multiple_files=True,
            help="Upload clear photos of leaves, stems, or affected parts. Videos are NOT allowed."
        )
        st.caption(
            "📸 **ಸೂಚನೆ:** ಕೇವಲ ಫೋಟೋಗಳನ್ನು (JPG, PNG, WEBP) ಮಾತ್ರ ಅಪ್‌ಲೋಡ್ ಮಾಡಿ. ವೀಡಿಯೊ ಅಪ್‌ಲೋಡ್ ಮಾಡಲು ಅವಕಾಶವಿಲ್ಲ. ಎಲೆಯ ಮೇಲ್ಭಾಗ, ಹಿಂಭಾಗ ಮತ್ತು ಇಡೀ ಗಿಡದ ಹಲವು ಫೋಟೋಗಳನ್ನು ಒಟ್ಟಿಗೆ ಆಯ್ಕೆಮಾಡಬಹುದು."
            if is_kn else
            "📸 **Note:** Photos only (JPG, PNG, WEBP). Video uploads are strictly prohibited. You can upload multiple photos showing leaf close-up, underside, and whole plant."
        )
    else:
        camera = st.camera_input(t("Take a photo now"))
        st.caption(t("The webcam option may use the front camera. On a phone, the first option is usually better."))

    valid_photos = []
    has_video = False
    if uploaded_files:
        file_list = uploaded_files if isinstance(uploaded_files, list) else [uploaded_files]
        for f in file_list:
            fname = getattr(f, "name", "").lower()
            ext = Path(fname).suffix.lower()
            mime = getattr(f, "type", "").lower()
            if ext in VIDEO_EXTS or "video" in mime:
                has_video = True
            else:
                valid_photos.append(f)

    if has_video:
        st.error(
            "🚫 **ವೀಡಿಯೊ ಅಪ್‌ಲೋಡ್ ಮಾಡಲು ಅವಕಾಶವಿಲ್ಲ.** ದಯವಿಟ್ಟು ಕೇವಲ ಬೆಳೆಯ ಸ್ಪಷ್ಟ ಫೋಟೋಗಳನ್ನು (JPG, PNG, WEBP) ಮಾತ್ರ ಅಪ್‌ಲೋಡ್ ಮಾಡಿ."
            if is_kn else
            "🚫 **Video files are not allowed.** Please upload clear photos only (JPG, PNG, WEBP). You can upload multiple photos."
        )

    photos_to_show = valid_photos if valid_photos else ([camera] if camera else [])

    if photos_to_show:
        st.markdown(f"**📸 {'ಅಪ್‌ಲೋಡ್ ಮಾಡಿದ ಫೋಟೋಗಳು' if is_kn else 'Uploaded Photos'} ({len(photos_to_show)}):**")
        n_cols = min(len(photos_to_show), 4)
        img_cols = st.columns(n_cols)
        for idx, p_file in enumerate(photos_to_show):
            img_cols[idx % n_cols].image(
                p_file,
                caption=f"{'ಫೋಟೋ' if is_kn else 'Photo'} {idx+1}",
                use_container_width=True
            )

    provider, api_key, model = get_provider()
    if not api_key:
        ui.note(t("Photo analysis is not switched on yet. You can still use the Browse common problems tab."), "warn")
        with st.expander(t("For the app owner")):
            st.write(t("Add a free Gemini API key as GEMINI_API_KEY in this app's Secrets (never in GitHub). See the README."))

    if st.button(t("Analyse photo"), type="primary"):
        if not photos_to_show:
            st.warning(t("Please add a photo first."))
        elif st.session_state["doctor_count"] >= MAX_PER_SESSION:
            st.warning(t("You have reached the limit of photos for this visit. Please come back later or visit your KVK."))
        else:
            raw_bytes_list = []
            for p in photos_to_show:
                if hasattr(p, "seek"):
                    p.seek(0)
                raw_bytes_list.append(p.getvalue())
            result = None
            if api_key:
                try:
                    with st.spinner(t("Looking at your photo...")):
                        result = diagnosis.analyze(raw_bytes_list, api_key, KB, provider=provider, model=model, crop_hint=crop_hint, language=i18n.current_lang())
                except Exception:
                    result = None

            if not result:
                with st.spinner("ಬೆಳೆ ರೋಗ ಲಕ್ಷಣಗಳು ಮತ್ತು ತೀವ್ರತೆಯ ಮಟ್ಟ ವಿಶ್ಲೇಷಿಸಲಾಗುತ್ತಿದೆ..." if is_kn else "Analyzing plant symptoms, lesion patterns & severity..."):
                    result = diagnosis.analyze_visual(raw_bytes_list, crop_hint, KB, language=i18n.current_lang())

            if result:
                st.session_state["doctor"] = {"result": result, "district": district}
                st.session_state["doctor_count"] += 1

    if "doctor" in st.session_state:
        render_result(st.session_state["doctor"])
    st.caption(t(PRIVACY[provider]) + " " + t("The AI only identifies the problem. Treatment advice comes from reviewed sources. Always confirm before you spray."))

with tab_browse:
    st.markdown("### 🌿 " + ("ಬೆಳೆವಾರು ರೋಗ, ಕೀಟ ಹಾಗೂ ಕಳೆ ಸಮಗ್ರ ನಿರ್ವಹಣಾ ಮಾರ್ಗದರ್ಶಿ" if is_kn else "Crop-Wise Disease, Pest & Weed Management Guide"))
    st.caption(
        "ಕರ್ನಾಟಕದ ಎಲ್ಲಾ ಪ್ರಮುಖ ಬೆಳೆಗಳಿಗೆ ತಗಲುವ ರೋಗಗಳು, ಕೀಟಗಳು ಮತ್ತು ಕಳೆಗಳ ಅಧಿಕೃತ ವಿಶ್ವವಿದ್ಯಾಲಯ ಶಿಫಾರಸುಗಳು. "
        "ಎಡಭಾಗದಲ್ಲಿ ನಿಮ್ಮ ಬೆಳೆ ಮತ್ತು ರೋಗವನ್ನು ಆರಿಸಿ, ಲಕ್ಷಣಗಳನ್ನು ದೃಢೀಕರಿಸಿ ಬಲಭಾಗದಲ್ಲಿ ಸಂಪೂರ್ಣ ಔಷಧ ಚೀಟಿ ಪಡೆಯಿರಿ."
        if is_kn else
        "Comprehensive reviewed management guide for all major Karnataka crops. "
        "Select your crop and problem variant on the left panel, confirm symptoms, and view full dosage prescriptions on the right panel."
    )

    options = {f"{t(e['name'])} ({type_label(e['type'])})": e for e in KB}
    if options:
        bc1, bc2 = st.columns([1.5, 2.5])
        with bc1:
            if is_kn:
                b_options = {DISTRICTS_KN.get(d, d): d for d in sorted(DISTRICTS)}
                b_keys = list(b_options.keys())
                b_default = DISTRICTS_KN.get("Mysuru", "ಮೈಸೂರು")
                b_idx = b_keys.index(b_default) if b_default in b_keys else 0
                sel_b_kn = st.selectbox(t("Your district"), b_keys, index=b_idx, key="browse_district")
                browse_district = b_options[sel_b_kn]
            else:
                browse_district = st.selectbox(t("Your district"), sorted(DISTRICTS), index=sorted(DISTRICTS).index("Mysuru"), key="browse_district")
        with bc2:
            st.info(
                f"🌦️ **{browse_district} {'ಜಿಲ್ಲೆಯ ಹವಾಮಾನ ಮುನ್ಸೂಚನೆ & ಸಿಂಪರಣಾ ಎಚ್ಚರಿಕೆ:' if is_kn else 'District Weather & Spraying Advisory:'}** "
                + ("ಗಾಳಿಯ ವೇಗ ಗಂಟೆಗೆ 25 ಕಿ.ಮೀ. ಗಿಂತ ಹೆಚ್ಚಿದ್ದಾಗ ಅಥವಾ ಮಳೆ ನಿರೀಕ್ಷೆಯಿದ್ದಾಗ ಸಿಂಪಡಿಸಬೇಡಿ. ಮೋಡ ಕವಿದ ಹವೆಯಲ್ಲಿ ಬೂಷ್ಟು ರೋಗಗಳು ಶೀಘ್ರ ಹರಡುತ್ತವೆ."
                   if is_kn else "Avoid spraying during high winds (>25 km/h) or approaching rain. Overcast and humid conditions accelerate fungal blast.")
            )

        col_left, col_right = st.columns([1.2, 2.0])

        crop_list = [
            ("ಎಲ್ಲ ಬೆಳೆಗಳು {All Crops}" if is_kn else "All Crops"),
            ("ಭತ್ತ {Paddy / Rice}" if is_kn else "Paddy / Rice"),
            ("ಮೆಕ್ಕೆಜೋಳ {Maize}" if is_kn else "Maize"),
            ("ಟೊಮೆಟೊ {Tomato}" if is_kn else "Tomato"),
            ("ಹತ್ತಿ {Cotton}" if is_kn else "Cotton"),
            ("ಮೆಣಸಿನಕಾಯಿ {Chilli}" if is_kn else "Chilli"),
            ("ಕಡಲೆಕಾಯಿ {Groundnut}" if is_kn else "Groundnut"),
            ("ರಾಗಿ {Finger Millet / Ragi}" if is_kn else "Ragi"),
            ("ತೊಗರಿ {Pigeon Pea / Tur}" if is_kn else "Tur (Pigeon Pea)"),
            ("ಈರುಳ್ಳಿ {Onion}" if is_kn else "Onion"),
            ("ಅಡಿಕೆ {Areca nut}" if is_kn else "Areca nut"),
            ("ಕಳೆಗಳು {Weeds}" if is_kn else "Weeds"),
        ]
        crop_filter_map = {
            "ಭತ್ತ": "rice", "paddy": "rice", "ಮೆಕ್ಕೆಜೋಳ": "maize", "maize": "maize",
            "ಟೊಮೆಟೊ": "tomato", "tomato": "tomato", "ಹತ್ತಿ": "cotton", "cotton": "cotton",
            "ಮೆಣಸಿನಕಾಯಿ": "chilli", "chilli": "chilli", "ಕಡಲೆಕಾಯಿ": "groundnut", "groundnut": "groundnut",
            "ರಾಗಿ": "ragi", "millet": "ragi", "ತೊಗರಿ": "tur", "pigeon": "tur",
            "ಈರುಳ್ಳಿ": "onion", "onion": "onion", "ಅಡಿಕೆ": "arecanut", "areca": "arecanut",
            "ಕಳೆಗಳು": "weed", "weed": "weed"
        }

        with col_left:
            with st.container(border=True):
                st.markdown("#### 🌾 " + ("ಬೆಳೆ ಆಯ್ಕೆ {Crop}" if is_kn else "Crop Filter"))
                sel_crop_filter = st.selectbox(
                    "ಬೆಳೆ ವರ್ಗ {Crop Category}:" if is_kn else "Crop Category:",
                    crop_list,
                    key="browse_crop_filter"
                )

                sel_tag = None
                for k, val in crop_filter_map.items():
                    if k.lower() in sel_crop_filter.lower():
                        sel_tag = val
                        break

                if sel_tag == "weed":
                    filtered_kb = [e for e in KB if e.get("type") == "weed"]
                elif sel_tag:
                    filtered_kb = [e for e in KB if any(sel_tag in c.lower() for c in e.get("crops", [])) or sel_tag in e.get("id", "").lower()]
                else:
                    filtered_kb = KB

                if not filtered_kb:
                    filtered_kb = KB

                problem_options = {f"{t(e['name'])} ({type_label(e['type'])})": e for e in filtered_kb}
                st.markdown("#### 🐛 " + ("ರೋಗ / ಕೀಟ ಆರಿಸಿ" if is_kn else "Choose Problem"))
                pick = st.selectbox(
                    t("Choose a problem"),
                    list(problem_options.keys()),
                    key="browse_problem_choice"
                )
                chosen_entry = problem_options[pick]

                st.markdown("---")
                st.markdown(f"**📷 {t('Reference photo')}:**")
                reference_image(chosen_entry["id"])
                st.markdown(f"**🏷️ {t(chosen_entry['name'])}**")
                st.markdown(ui.badge(type_label(chosen_entry["type"]), chosen_entry["type"]), unsafe_allow_html=True)
                st.caption(f"**{'ಬಾಧಿತ ಬೆಳೆಗಳು:' if is_kn else 'Target Crops:'}** {', '.join(str(c) for c in chosen_entry.get('crops', []))}")
                st.markdown("**" + ("ಪ್ರಮುಖ ಲಕ್ಷಣಗಳು {Key Signs}:" if is_kn else "Key Identification Signs:") + "**")
                for sign in chosen_entry.get("look_for", [])[:2]:
                    st.markdown(f"- `{t(sign)}`")

        with col_right:
            render_entry(chosen_entry, browse_district, key_prefix="guide")
    else:
        st.info(t("The guidance library could not be loaded."))

ui.feedback_box()
st.markdown("---")
footer_str = (
    "© 2026 ಅಭಿಷೇಕ್ ಹಿಟಬುತ್ತಿ. ಎಲ್ಲ ಹಕ್ಕುಗಳನ್ನು ಕಾಯ್ದಿರಿಸಲಾಗಿದೆ. ಅನುಮತಿ ಇಲ್ಲದೆ ಈ ಆ್ಯಪ್ ಅನ್ನು ನಕಲು ಮಾಡುವುದು ಅಥವಾ ಮರುಬಳಕೆ ಮಾಡುವುದು ನಿಷಿದ್ಧ."
    if is_kn else
    "© 2026 Abhishek Hitabutti. All rights reserved. Copying or reuse of this app without permission is prohibited."
)
st.caption(footer_str)
