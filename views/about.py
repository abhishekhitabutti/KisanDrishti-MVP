"""About, data sources, limits, privacy and credits.
Fully bilingual: 100% pure Kannada localization with technical terms in braces {...}.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import streamlit as st
import diagnosis
import i18n
import ui
from i18n import t

APP_VERSION_EN = "0.7 (beta), October 2026"
APP_VERSION_KN = "0.7 {ಬೀಟಾ}, ಅಕ್ಟೋಬರ್ 2026"

is_kn = (i18n.current_lang() == "kn")

hero_title = "ಬಗ್ಗೆ ಮತ್ತು ಗೌಪ್ಯತೆ" if is_kn else "About and privacy"
hero_sub = (
    "ಈ ಆ್ಯಪ್ ಏನು, ಇದರ ಸಲಹೆಗಳು ಎಲ್ಲಿಂದ ಬರುತ್ತವೆ, ಇದರ ಮಿತಿಗಳು ಮತ್ತು ನಿಮ್ಮ ಮಾಹಿತಿಯನ್ನು ಹೇಗೆ ನಿರ್ವಹಿಸಲಾಗುತ್ತದೆ."
    if is_kn else
    "What this app is, where its advice comes from, what it cannot do, and how your data is handled."
)
ui.hero(hero_title, hero_sub, "ℹ️")

# Section 1: What it is
sec1_title = "ಕೃಷಿನುಡಿ {KrushiNudi} ಎಂದರೇನು?" if is_kn else "What KrushiNudi is"
st.subheader(sec1_title)
tagline_display = (
    "**ಕೃಷಿನುಡಿ {KrushiNudi}** · ಸ್ಮಾರ್ಟ್ ಕೃಷಿ ಸಲಹೆಗಾರ {Smart Farm Advisory} · ಬುದ್ಧಿವಂತ ಕೃಷಿಯ ಧ್ವನಿ {The Voice of Intelligent Agriculture}\n\n*✨ ಚತುರ ಒಳನೋಟಗಳು. ಉತ್ತಮ ಕೃಷಿ. {Smarter Insights. Better Farming.}*"
    if is_kn else
    "**KrushiNudi** · Smart Farm Advisory · The Voice of Intelligent Agriculture\n\n*✨ Smarter Insights. Better Farming.*"
)
st.markdown(tagline_display)
sec1_body = (
    "ಕರ್ನಾಟಕದ ರೈತರಿಗಾಗಿ ಅಭಿವೃದ್ಧಿಪಡಿಸಲಾದ ಉಚಿತ ಕೃಷಿ ಸಲಹಾ ತಂತ್ರಾಂಶ. ಇದನ್ನು ಬೆಂಗಳೂರಿನ ಅಮಿಟಿ ವಿಶ್ವವಿದ್ಯಾಲಯದ {Amity University Bengaluru} "
    "ಬಿ.ಟೆಕ್ ಕಂಪ್ಯೂಟರ್ ಸೈನ್ಸ್ ಕೃತಕ ಬುದ್ಧಿಮತ್ತೆ ಮತ್ತು ಯಂತ್ರ ಕಲಿಕೆ {B.Tech CSE (AI & ML)} ವಿದ್ಯಾರ್ಥಿ ಅಭಿಷೇಕ್ ಹಿಟಬುತ್ತಿ {Abhishek Hitabutti} ರೂಪಿಸಿದ್ದಾರೆ. "
    "ಇದು ಯಾವುದೇ ಸರ್ಕಾರಿ ಅಧಿಕೃತ ಸೇವೆಯಲ್ಲ. ಇದರಲ್ಲಿ ಯಾವುದೇ ವಾಣಿಜ್ಯ ಜಾಹೀರಾತುಗಳಿಲ್ಲ."
    if is_kn else
    "A free advisory app for Karnataka farmers, built by Abhishek Hitabutti, a B.Tech CSE (AI & ML) student at Amity University "
    "Bengaluru. It is not a government service. It has no advertising."
)
st.write(sec1_body)
version_label = f"ಆವೃತ್ತಿ: {APP_VERSION_KN}" if is_kn else f"Version {APP_VERSION_EN}"
st.caption(version_label)

# Section 2: Where advice comes from
sec2_title = "ಕೃಷಿ ಸಲಹೆಗಳ ಮೂಲಗಳು" if is_kn else "Where the advice comes from"
st.subheader(sec2_title)
kb_count = len(diagnosis.load_kb())
if is_kn:
    st.markdown(
        "- **ಬೆಳೆ ಸಲಹೆಗಾರ:** 22 ಬೆಳೆಗಳ ಸಾರ್ವಜನಿಕ ಬೆಳೆ ಶಿಫಾರಸು ಡೇಟಾಸೆಟ್ ಆಧಾರಿತ ರ‍್ಯಾಂಡಮ್ ಫಾರೆಸ್ಟ್ {Random Forest} ಯಂತ್ರ ಕಲಿಕೆ ಮಾದರಿ.\n"
        f"- **ಬೆಳೆ ವೈದ್ಯ:** ಕೃತಕ ಬುದ್ಧಿಮತ್ತೆ {{AI}} ಮಾದರಿಯು ಕೇವಲ ರೋಗ ಅಥವಾ ಕೀಟವನ್ನು ಗುರುತಿಸುತ್ತದೆ. ಚಿಕಿತ್ಸಾ ಮಾರ್ಗದರ್ಶನವು ಐಸಿಎಆರ್ {{ICAR}}, "
        f"ತಮಿಳುನಾಡು ಕೃಷಿ ವಿಶ್ವವಿದ್ಯಾಲಯ {{TNAU}} ಮತ್ತು ರಾಜ್ಯ ಕೃಷಿ ವಿಶ್ವವಿದ್ಯಾಲಯಗಳ {kb_count} ಪರಿಶೀಲಿತ ಸಂಶೋಧನಾ ಗ್ರಂಥಾಲಯದಿಂದ ಬರುತ್ತದೆ.\n"
        "- **ಹವಾಮಾನ ಮುನ್ನೆಚ್ಚರಿಕೆಗಳು:** ಓಪನ್-ಮೆಟಿಯೋ {Open-Meteo} ನೇರ ಮುನ್ಸೂಚನೆ ಹಾಗೂ ಭಾರತೀಯ ಹವಾಮಾನ ಇಲಾಖೆಯ {IMD} ಅಧಿಕೃತ ಎಚ್ಚರಿಕೆಗಳು.\n"
        "- **ಯೋಜನೆಗಳು ಮತ್ತು ಸಹಾಯ:** ಸರ್ಕಾರದ ಅಧಿಕೃತ ಪೋರ್ಟಲ್‌ಗಳು ಮತ್ತು ಸಾರ್ವಜನಿಕ ಕೃಷಿ ವಿಸ್ತರಣಾ ಮೂಲಗಳು.\n"
        "- **ಋತು ಯೋಜಕ:** ಪ್ರತಿ ಕೃಷಿ ಪದ್ಧತಿಯ ಅಡಿಯಲ್ಲಿ ಪಟ್ಟಿ ಮಾಡಲಾದ ಕೃಷಿ ಸಂಶೋಧನಾ ವಿಸ್ತರಣಾ ಆಧಾರಗಳು."
    )
else:
    st.markdown(
        "- **Crop advisor:** a Random Forest model trained on a public crop recommendation dataset (22 crops).\n"
        "- **Crop Doctor:** an AI model only identifies the problem in your photo. The treatment guidance comes from a "
        f"library of {kb_count} reviewed entries, each with its sources (ICAR, TNAU and university papers), and is shown only when the match is confident.\n"
        "- **Weather precautions:** forecasts from Open-Meteo. You can also enter an official IMD warning you heard on the government telecast.\n"
        "- **Schemes and help:** the government portals for each scheme, and public extension sources.\n"
        "- **Season planner:** extension and research sources, listed under each practice."
    )

# Section 3: Limits
sec3_title = "ನೀವು ತಿಳಿದುಕೊಳ್ಳಬೇಕಾದ ಮಿತಿಗಳು" if is_kn else "Limits you should know"
st.subheader(sec3_title)
if is_kn:
    st.markdown(
        "- ಈ ಮಾರ್ಗದರ್ಶನವನ್ನು **ಕೃಷಿ ತಜ್ಞರು ಇನ್ನೂ ಅಂತಿಮವಾಗಿ ಪರಿಶೀಲಿಸಿಲ್ಲ**. ಪರಿಶೀಲನಾ ಪ್ರಕ್ರಿಯೆ ಪ್ರಗತಿಯಲ್ಲಿದೆ.\n"
        "- ಬೆಳೆ ಸಲಹೆಗಾರವು 22 ಬೆಳೆಗಳನ್ನು ಮಾತ್ರ ಒಳಗೊಂಡಿದೆ. ಇದು ನೈಜ ಹೊಲಗಳಿಂದ ನೇರವಾಗಿ ಸಂಗ್ರಹಿಸಿದ ಡೇಟಾ ಅಲ್ಲ, ಆದ್ದರಿಂದ ವಾಸ್ತವಿಕ ಜಮೀನುಗಳಲ್ಲಿ ನಿಖರತೆ ಕಡಿಮೆಯಾಗುವ ಸಾಧ್ಯತೆಯಿದೆ.\n"
        "- ಬೆಳೆ ವೈದ್ಯವು ಸೀಮಿತ ಸಂಖ್ಯೆಯ ರೋಗ-ಕೀಟಗಳನ್ನು ಮಾತ್ರ ಗುರುತಿಸಬಲ್ಲದು. ಅಸ್ಪಷ್ಟತೆ ಇದ್ದಾಗ ಕೃಷಿ ತಜ್ಞರ ಬಳಿ ಹೋಗಲು ಸೂಚಿಸುತ್ತದೆ.\n"
        "- ಹವಾಮಾನ ವೈಪರೀತ್ಯದ ಮಿತಿಗಳು ಸರಳ ನಿಯಮಗಳಾಗಿವೆ. ಮುನ್ಸೂಚನೆಗಳಲ್ಲಿ ಬದಲಾವಣೆಗಳು ಸಹಜ.\n"
        "- ಈ ಆ್ಯಪ್ **ಯಾವುದೇ ಕೀಟನಾಶಕ ಅಥವಾ ರಸಗೊಬ್ಬರದ ನಿರ್ದಿಷ್ಟ ಪ್ರಮಾಣ ನೀಡುವುದಿಲ್ಲ**. ಪ್ರಮಾಣವನ್ನು ಉತ್ಪನ್ನದ ಲೇಬಲ್, ನಿಮ್ಮ ಮಣ್ಣು ಆರೋಗ್ಯ ಕಾರ್ಡ್ ಅಥವಾ ಕೃಷಿ ಅಧಿಕಾರಿಗಳಿಂದ ಮಾತ್ರ ಪಡೆಯಬೇಕು.\n"
        "- ಇದು ನಿಮ್ಮ ಸ್ಥಳೀಯ ಕೃಷಿ ಅಧಿಕಾರಿ, ಕೃಷಿ ವಿಜ್ಞಾನ ಕೇಂದ್ರ {KVK} ಅಥವಾ ರೈತ ಸಂಪರ್ಕ ಕೇಂದ್ರಕ್ಕೆ {RSK} ಪರ್ಯಾಯವಲ್ಲ."
    )
else:
    st.markdown(
        "- The guidance has **not yet been reviewed by an agriculture expert**. Expert review is in progress.\n"
        "- The crop advisor knows 22 crops. Its dataset is described as built by augmenting rainfall, climate and fertilizer data, "
        "so it is **not field-collected data** and accuracy on real farms can be lower.\n"
        "- Crop Doctor knows a small number of problems. For anything else it tells you to see an expert.\n"
        "- Weather hazard thresholds are simple rules. Forecasts can be wrong.\n"
        "- The app **gives no pesticide or fertilizer doses**. Doses come from the product label, your Soil Health Card or your agriculture officer.\n"
        "- It cannot replace your agriculture officer, KVK or Raitha Samparka Kendra."
    )

# Section 4: Privacy
sec4_title = "ಗೌಪ್ಯತೆ ಮತ್ತು ಸುರಕ್ಷತೆ" if is_kn else "Privacy"
st.subheader(sec4_title)
if is_kn:
    st.markdown(
        "- **ಈ ಆ್ಯಪ್ ಬಳಸಲು ಲಾಗಿನ್ ಅಥವಾ ಖಾತೆ ಅಗತ್ಯವಿಲ್ಲ.**\n"
        "- **ಛಾಯಾಚಿತ್ರಗಳು:** ಈ ಆ್ಯಪ್ ನಿಮ್ಮ ಫೋಟೋಗಳನ್ನು ತನ್ನ ಸರ್ವರ್‌ನಲ್ಲಿ ಸಂಗ್ರಹಿಸುವುದಿಲ್ಲ {does **not store**}. "
        "ಫೋಟೋ ವಿಶ್ಲೇಷಣೆಗಾಗಿ ಗೂಗಲ್‌ನ ಜೆಮಿನಿ {Gemini} ಸೇವೆಗೆ ಕಳುಹಿಸಲಾಗುತ್ತದೆ. ಸ್ಥಳದ {GPS} ಮಾಹಿತಿಯನ್ನು ಮೊದಲೇ ತೆಗೆದುಹಾಕಲಾಗುತ್ತದೆ. "
        "ಜನರಿರುವ ಫೋಟೋಗಳನ್ನು ಅಪ್‌ಲೋಡ್ ಮಾಡಬೇಡಿ.\n"
        "- **ಹವಾಮಾನ:** ನೀವು ಆಯ್ಕೆಮಾಡುವ ಜಿಲ್ಲೆಯ ಕೇಂದ್ರ ಬಿಂದುವಿನ ನಿರ್ದೇಶಾಂಕಗಳನ್ನು ಮಾತ್ರ ಮುನ್ಸೂಚನೆ ಸೇವೆಗೆ ಕಳುಹಿಸಲಾಗುತ್ತದೆ.\n"
        "- **ಪ್ರತಿಕ್ರಿಯೆ:** ನೀವು ಇಮೇಲ್ ಮೂಲಕ ಪ್ರತಿಕ್ರಿಯೆ ಕಳುಹಿಸಿದಾಗ ನಿಮ್ಮ ಇಮೇಲ್ ವಿಳಾಸ ಮತ್ತು ಸಂದೇಶ ನಮಗೆ ತಲುಪುತ್ತದೆ.\n"
        "- ತಾಂತ್ರಿಕ ಹೋಸ್ಟಿಂಗ್ ಸೇವೆಯು ವೆಬ್‌ಸೈಟ್‌ಗಳ ಸಾಮಾನ್ಯ ಲಾಗ್‌ಗಳನ್ನು ಮಾತ್ರ ನಿರ್ವಹಿಸುತ್ತದೆ."
    )
else:
    st.markdown(
        "- **No login or account is needed** to use this app.\n"
        "- **Photos:** This app does **not store** your photos on any server. "
        "Photos are sent to Google's Gemini service for analysis. On Google's free tier, Google may use the content to improve its products. "
        "Location data is removed from the photo first. Please do not upload photos with people in them.\n"
        "- **Weather:** only the centre point of the district you pick is sent to the forecast service.\n"
        "- **Feedback:** if you email feedback, we receive your email address and message.\n"
        "- The hosting service may keep standard technical logs, as any website does."
    )

# Section 5: Credits
sec5_title = "ಕೃತಜ್ಞತೆಗಳು" if is_kn else "Credits"
st.subheader(sec5_title)
if is_kn:
    st.markdown(
        "- ಹವಾಮಾನ ಮಾಹಿತಿ: [Open-Meteo.com](https://open-meteo.com/).\n"
        "- ಬೆಳೆ ಶಿಫಾರಸು ಡೇಟಾಸೆಟ್: ಸಾರ್ವಜನಿಕ ಬೆಳೆ ಡೇಟಾಸೆಟ್ (22 ಬೆಳೆಗಳು, 2,200 ಸಾಲುಗಳು).\n"
        "- ಹೆಚ್ಚುವರಿ ಬೆಳೆಗಳು: ಎಫ್‌ಎಒ ಇಕೋಕ್ರಾಪ್ [FAO EcoCrop database](https://gaez.fao.org/pages/ecocrop-search).\n"
        "- ಕೃಷಿ ಮಾರ್ಗದರ್ಶನ ಮೂಲಗಳನ್ನು ಪ್ರತಿ ಬೆಳೆ ವೈದ್ಯ ಮತ್ತು ಋತು ಯೋಜಕ ನಮೂದುಗಳಲ್ಲಿ ನೀಡಲಾಗಿದೆ.\n"
        "- ಮೂಲ ಕೋಡ್: [github.com/abhishekhitabutti/KisanDrishti-MVP](https://github.com/abhishekhitabutti/KisanDrishti-MVP). ಎಲ್ಲ ಹಕ್ಕುಗಳನ್ನು ಕಾಯ್ದಿರಿಸಲಾಗಿದೆ."
    )
else:
    st.markdown(
        "- Weather data by [Open-Meteo.com](https://open-meteo.com/).\n"
        "- Crop recommendation dataset: a public dataset (22 crops, 2,200 rows) widely shared on Kaggle. Check its terms before reusing it.\n"
        "- More crops: the [FAO EcoCrop database](https://gaez.fao.org/pages/ecocrop-search).\n"
        "- Guidance sources are listed inside each Crop Doctor entry and each Season Planner practice.\n"
        "- Source code: [github.com/abhishekhitabutti/KisanDrishti-MVP](https://github.com/abhishekhitabutti/KisanDrishti-MVP). All rights reserved."
    )

# Section 6: Contact
sec6_title = "ಸಂಪರ್ಕ" if is_kn else "Contact"
st.subheader(sec6_title)
contact_text = (
    "ಅಭಿಷೇಕ್ ಹಿಟಬುತ್ತಿ {Abhishek Hitabutti}: [abhishekhitabutti@gmail.com](mailto:abhishekhitabutti@gmail.com). ರೈತರು, ಕೃಷಿ ಅಧಿಕಾರಿಗಳು ಮತ್ತು {KVK} ತಜ್ಞರ ಸಲಹೆ ಮತ್ತು ತಿದ್ದುಪಡಿಗಳನ್ನು ಮುಕ್ತವಾಗಿ ಸ್ವಾಗತಿಸಲಾಗುತ್ತದೆ."
    if is_kn else
    "Abhishek Hitabutti: [abhishekhitabutti@gmail.com](mailto:abhishekhitabutti@gmail.com). Corrections from farmers, agriculture officers and KVK staff are very welcome."
)
st.markdown(contact_text)

ui.feedback_box()
st.markdown("---")
footer_str = (
    "© 2026 ಅಭಿಷೇಕ್ ಹಿಟಬುತ್ತಿ. ಎಲ್ಲ ಹಕ್ಕುಗಳನ್ನು ಕಾಯ್ದಿರಿಸಲಾಗಿದೆ. ಅನುಮತಿ ಇಲ್ಲದೆ ಈ ಆ್ಯಪ್ ಅನ್ನು ನಕಲು ಮಾಡುವುದು ಅಥವಾ ಮರುಬಳಕೆ ಮಾಡುವುದು ನಿಷಿದ್ಧ."
    if is_kn else
    "© 2026 Abhishek Hitabutti. All rights reserved. Copying or reuse of this app without permission is prohibited."
)
st.caption(footer_str)