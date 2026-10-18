"""Season planner: practices for each stage of the farming season, with sources.
Fully bilingual: 100% pure Kannada localization with technical terms in braces {...}.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import streamlit as st
import i18n
import planner_data as pdata
import ui
from i18n import t

is_kn = (i18n.current_lang() == "kn")

hero_title = "ಋತು ಯೋಜಕ" if is_kn else "Season planner"
hero_sub = (
    "ಕೃಷಿ ಋತುವಿನ ಪ್ರತಿ ಹಂತದಲ್ಲಿ ಏನು ಮಾಡಬೇಕು? ಎಲ್ಲ ಪದ್ಧತಿಗಳಿಗೂ ಅಧಿಕೃತ ಸಂಶೋಧನಾ ಆಧಾರಗಳನ್ನು ನೀಡಲಾಗಿದೆ."
    if is_kn else
    "What to do at each stage of the season. Every practice shows where it comes from."
)
ui.hero(hero_title, hero_sub, "🗓️")

steps_list = [
    ("🌱", "ಬಿತ್ತನೆಗೆ ಮುನ್ನ" if is_kn else "Before sowing"),
    ("🚜", "ಬಿತ್ತನೆ ಕಾಲ" if is_kn else "Sowing"),
    ("🌾", "ಬೆಳವಣಿಗೆ ಕಾಲ" if is_kn else "Growing"),
    ("📦", "ಕೊಯ್ಲು ಮತ್ತು ಸಂಗ್ರಹಣೆ" if is_kn else "Harvest"),
]
ui.steps_row(steps_list)


def bullets(items):
    for item in items:
        st.markdown(f"- {item}")


def render_item(item, is_kn_mode):
    with st.expander(item["title"]):
        st.write(item["summary"])
        st.markdown("**" + ("ಹಂತಗಳು:" if is_kn_mode else "Steps") + "**")
        bullets(item["steps"])
        if item.get("cautions"):
            st.markdown("**" + ("ಎಚ್ಚರಿಕೆ:" if is_kn_mode else "Be careful") + "**")
            bullets(item["cautions"])
        st.markdown("**" + ("ಅಧಿಕೃತ ಸಂಶೋಧನಾ ಮೂಲಗಳು:" if is_kn_mode else "Sources") + "**")
        src_dict = pdata.SRC_KN if is_kn_mode else pdata.SRC
        for key in item["sources"]:
            s = src_dict.get(key, pdata.SRC.get(key))
            if s:
                st.markdown(f"- [{s['title']}]({s['url']})")
        if item["id"] == "seed_test":
            germination_calculator(is_kn_mode)


def germination_calculator(is_kn_mode):
    st.markdown("---")
    st.markdown("**" + ("ನಿಮ್ಮ ಬೀಜದ ಮೊಳಕೆ ಸಾಮರ್ಥ್ಯದ ಶೇಕಡಾವಾರು ಲೆಕ್ಕ ಹಾಕಿ" if is_kn_mode else "Work out your germination percentage") + "**")
    c1, c2 = st.columns(2)
    tested_label = "ಪರೀಕ್ಷಿಸಿದ ಒಟ್ಟು ಬೀಜಗಳು" if is_kn_mode else "Seeds tested"
    sprouted_label = "ಮೊಳಕೆಯೊಡೆದ ಬೀಜಗಳು" if is_kn_mode else "Seeds that sprouted"
    
    tested = c1.number_input(tested_label, min_value=1, max_value=1000, value=100, step=10, key="gc_tested")
    sprouted = c2.number_input(sprouted_label, min_value=0, max_value=1000, value=0, step=1, key="gc_sprouted")
    
    pct, level, message = pdata.germination_verdict(sprouted, tested)
    
    kn_verdicts = {
        "good": "ಉತ್ತಮ. ಈ ಬೀಜವು ಅತ್ಯುತ್ತಮವಾಗಿ ಬೆಳೆಯುತ್ತದೆ.",
        "ok": "ಧಾನ್ಯ ಮತ್ತು ಬೇಳೆಕಾಳು ಬೀಜಗಳಿಗೆ ಸ್ವೀಕಾರಾರ್ಹ ಗುಣಮಟ್ಟ.",
        "weak": "ದುರ್ಬಲ ಮೊಳಕೆ ಪ್ರಮಾಣ. ಬೀಜ ಬದಲಾಯಿಸಬೇಕೇ ಅಥವಾ ಹೆಚ್ಚು ದಟ್ಟವಾಗಿ ಬಿತ್ತಬೇಕೇ ಎಂದು ಬೀಜ ಮಾರಾಟಗಾರ ಅಥವಾ {KVK} ಅನ್ನು ಸಂಪರ್ಕಿಸಿ.",
        "low": "ಧಾನ್ಯದ ಬೀಜಕ್ಕೆ ತುಂಬಾ ಕಡಿಮೆ ಮೊಳಕೆ ಪ್ರಮಾಣ. ಇದನ್ನು ಬಿತ್ತಬೇಡಿ. ಬದಲಿಸುವ ಕುರಿತು ಬೀಜ ಮಾರಾಟಗಾರರನ್ನು ಕೇಳಿ.",
        "error": "ಸಂಖ್ಯೆಗಳನ್ನು ಪರಿಶೀಲಿಸಿ. ಮೊಳಕೆಯೊಡೆದ ಬೀಜಗಳು ಪರೀಕ್ಷಿಸಿದ ಬೀಜಗಳಿಗಿಂತ ಹೆಚ್ಚಿರಲು ಸಾಧ್ಯವಿಲ್ಲ.",
    }
    
    display_message = kn_verdicts.get(level, message) if is_kn_mode else message
    
    if level == "error":
        st.warning(display_message)
    elif sprouted > 0:
        metric_label = "ಮೊಳಕೆ ಪ್ರಮಾಣ" if is_kn_mode else "Germination"
        st.metric(metric_label, f"{pct:.0f}%")
        (st.success if level in ("good", "ok") else st.warning)(display_message)
        
    caption_note = (
        "ಮಿತಿಗಳು ಧಾನ್ಯ ಮತ್ತು ಬೇಳೆಕಾಳು ಬೀಜಗಳ ಕೃಷಿ ಸಂಶೋಧನಾ ಮಾನದಂಡಗಳನ್ನು ಅನುಸರಿಸುತ್ತವೆ. ಇತರ ಬೆಳೆಗಳಿಗೆ ಇದು ಬದಲಾಗಬಹುದು, ಆದ್ದರಿಂದ ನಿಮ್ಮ ಕೃಷಿ ವಿಜ್ಞಾನ ಕೇಂದ್ರವನ್ನು {KVK} ಸಂಪರ್ಕಿಸಿ."
        if is_kn_mode else
        "Thresholds follow Agriculture Victoria advice for cereal and pulse seed. Other crops differ, so ask your seed dealer or KVK."
    )
    st.caption(caption_note)


stages_list = pdata.STAGES_KN if is_kn else pdata.STAGES
items_dict = pdata.ITEMS_KN if is_kn else pdata.ITEMS

tabs = st.tabs(stages_list)
for tab, stage in zip(tabs, stages_list):
    with tab:
        if (is_kn and stage == "ಬೆಳವಣಿಗೆ ಕಾಲ") or (not is_kn and stage == "Growing season"):
            if is_kn:
                st.write("ಬೆಳೆ ಬೆಳೆಯುತ್ತಿರುವ ಸಮಯದಲ್ಲಿ ಈ ಕೆಳಗಿನ ಪುಟಗಳನ್ನು ಬಳಸಿ:")
                st.markdown(
                    "- **ಹವಾಮಾನ ಮುನ್ನೆಚ್ಚರಿಕೆಗಳು:** 7 ದಿನಗಳ ಮುನ್ಸೂಚನೆ ಮತ್ತು ಕೆಟ್ಟ ಹವಾಮಾನ ಬರುವ ಮುನ್ನ ಮುನ್ನೆಚ್ಚರಿಕೆ ಕ್ರಮಗಳು.\n"
                    "- **ಬೆಳೆ ವೈದ್ಯ:** ರೋಗಪೀಡಿತ ಗಿಡ, ಕೀಟ ಅಥವಾ ಕಳೆಯ ಫೋಟೋ ತೆಗೆದು ಚಿಕಿತ್ಸಾ ಸಲಹೆ ಪಡೆಯಿರಿ.\n"
                    "- **ಮಂಡಿ ಧಾರಣೆ:** ಶೀಘ್ರದಲ್ಲೇ ಬರಲಿದೆ."
                )
                st.info("ಪ್ರತಿ ಕೆಲವು ದಿನಗಳಿಗೊಮ್ಮೆ ನಿಮ್ಮ ಜಮೀನನ್ನು ಪರಿಶೀಲಿಸಿ. ಸಮಸ್ಯೆಯನ್ನು ಆರಂಭದಲ್ಲೇ ಗುರುತಿಸಿದರೆ ನಿಭಾಯಿಸುವುದು ತುಂಬಾ ಸುಲಭ.")
            else:
                st.write("While the crop grows, use these pages:")
                st.markdown(
                    "- **Weather precautions:** 7-day forecasts and what to do before bad weather. Open it from the menu.\n"
                    "- **Crop Doctor:** photograph a sick plant, pest or weed. Open it from the menu.\n"
                    "- **Mandi prices:** coming soon."
                )
                st.info("Check your field every few days. Catching a problem early makes it much easier to deal with.")
                
        for item in items_dict.get(stage, []):
            render_item(item, is_kn)
            
        if (is_kn and stage == "ಕೊಯ್ಲು ಮತ್ತು ಸಂಗ್ರಹಣೆ") or (not is_kn and stage == "Harvest and storage"):
            insurance_note = (
                "ವಿಮೆ ಮಾಡಿಸಿದ ಬೆಳೆ ಪ್ರವಾಹ, ಆಲಿಕಲ್ಲು ಮಳೆ ಅಥವಾ ಅಂತಹುದರಿಂದ ಹಾನಿಯಾದರೆ 72 ಗಂಟೆಗಳೊಳಗೆ ವರದಿ ಮಾಡಿ. ಯೋಜನೆಗಳು ಮತ್ತು ಸಹಾಯ ಪುಟ ನೋಡಿ."
                if is_kn else
                "If your insured crop is damaged by flooding, hail or similar, report it within 72 hours. See the Schemes and Help page."
            )
            st.info(insurance_note)

disclaimer_note = (
    "ಪ್ರಕಟಿತ ಸಂಶೋಧನಾ ಆಧಾರಗಳಿಂದ ಪಡೆದ ಸಾಮಾನ್ಯ ಕೃಷಿ ಪದ್ಧತಿಗಳು. ಸ್ಥಳೀಯ ಪರಿಸ್ಥಿತಿಗಳು ಬೇರೆಯಾಗಿರುವುದರಿಂದ ನಿಮ್ಮ ಕೃಷಿ ವಿಜ್ಞಾನ ಕೇಂದ್ರ {KVK} ಅಥವಾ ಕೃಷಿ ಅಧಿಕಾರಿಯೊಂದಿಗೆ ಖಚಿತಪಡಿಸಿಕೊಳ್ಳಿ. ಈ ಆ್ಯಪ್ ಯಾವುದೇ ರಾಸಾಯನಿಕ ಪ್ರಮಾಣಗಳನ್ನು ನೀಡುವುದಿಲ್ಲ."
    if is_kn else
    "General practices from published sources. Local conditions differ, so confirm with your KVK or agriculture officer. This app gives no doses."
)
st.caption(disclaimer_note)

ui.feedback_box()
st.markdown("---")
footer_text = (
    "© 2026 ಅಭಿಷೇಕ್ ಹಿಟಬುತ್ತಿ. ಎಲ್ಲ ಹಕ್ಕುಗಳನ್ನು ಕಾಯ್ದಿರಿಸಲಾಗಿದೆ. ಅನುಮತಿ ಇಲ್ಲದೆ ಈ ಆ್ಯಪ್ ಅನ್ನು ನಕಲು ಮಾಡುವುದು ಅಥವಾ ಮರುಬಳಕೆ ಮಾಡುವುದು ನಿಷಿದ್ಧ."
    if is_kn else
    "© 2026 Abhishek Hitabutti. All rights reserved. Copying or reuse of this app without permission is prohibited."
)
st.caption(footer_text)
