"""Weather precautions page for KisanDrishti.
Live forecast from Open-Meteo with automated agricultural hazard flags.
Fully localized in pure Kannada and English.
"""
import json
import urllib.parse
import urllib.request
from datetime import datetime, timedelta, timezone
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import pandas as pd
import streamlit as st

import i18n
import ui
from districts import DISTRICTS, DISTRICTS_KN

IST = timezone(timedelta(hours=5, minutes=30))

PRECAUTIONS_EN = {
    "Heavy rain": [
        "Clear drains and field bunds so water does not stand in the field.",
        "Do not spray pesticides or apply fertilizer just before heavy rain. It washes away, wastes money and pollutes water.",
        "If crops are mature, harvest early where possible. Cover cut produce and store it dry and off the ground.",
        "Move livestock, seed, grain and equipment to higher, dry ground. Keep fodder covered.",
        "Stay away from flooded streams, canals and fallen power lines.",
        "If insured crops are damaged by flooding or inundation, report it within 72 hours: call 14447 or use the Crop Insurance app, and take photos.",
    ],
    "Thunderstorm and lightning": [
        "Stop field work and shelter in a pucca building or a closed vehicle. Do not stand under an isolated tree.",
        "Keep away from water, wire fences and metal tools. If caught in the open, crouch low with feet together. Do not lie flat.",
        "Switch off the pump set and electrical equipment before the storm if you can do it safely.",
        "Use the Damini app for lightning alerts.",
    ],
    "Strong wind": [
        "Prop up tall crops, banana and papaya plants and young trees. Secure polyhouse and shade-net sheets.",
        "Do not spray in wind. Drift harms you, neighbours, bees and animals.",
        "Secure roofs, sheets and loose tools.",
        "If you have crop insurance, ask your bank or the agriculture office whether the damage qualifies, and report within 72 hours.",
    ],
    "Heat": [
        "Irrigate early morning or evening, and mulch to hold soil moisture.",
        "Avoid field work between 12 and 3 pm. Drink water often, cover your head and rest in the shade.",
        "Dizziness, headache or confusion in the heat can be heatstroke. Get urgent medical help.",
        "Give livestock shade and clean water, and keep them out of the midday sun.",
        "Do not apply fertilizer on dry, hot soil without irrigation.",
    ],
    "Humid and warm (fungal diseases favoured)": [
        "Check crops every 2 to 3 days for spots, lesions or white growth on leaves.",
        "Improve airflow: keep proper spacing and remove badly infected leaves or plants.",
        "Do not spray just in case. If you see symptoms, show a photo or sample to your Krishi Vigyan Kendra or agriculture officer before choosing a fungicide.",
        "Use only recommended doses of approved products. Never use banned or unlabelled chemicals.",
        "Avoid evening irrigation that keeps leaves wet overnight.",
    ],
    "Dry week ahead": [
        "Plan irrigation by priority. Crops at flowering and grain filling are the most sensitive to water stress.",
        "Mulch with crop residue and remove weeds that compete for water.",
        "Avoid heavy top-dressing of fertilizer without soil moisture.",
        "Check your borewell water level before relying on it, and store drinking water for livestock.",
    ],
}

PRECAUTIONS_KN = {
    "Heavy rain": [
        "ಜಮೀನಿನಲ್ಲಿ ನೀರು ನಿಲ್ಲದಂತೆ ಬದುಗಳು ಮತ್ತು ಚರಂಡಿಗಳನ್ನು ಸ್ವಚ್ಛಗೊಳಿಸಿ ನೀರು ಸರಾಗವಾಗಿ ಹರಿಯುವಂತೆ ಮಾಡಿ.",
        "ಭಾರೀ ಮಳೆಯ ಮುನ್ನ ಕೀಟನಾಶಕ ಅಥವಾ ರಸಗೊಬ್ಬರ ಸಿಂಪಡಿಸಬೇಡಿ; ಮಳೆ ನೀರಿನಲ್ಲಿ ಕೊಚ್ಚಿಹೋಗಿ ಹಣ ವ್ಯರ್ಥವಾಗುತ್ತದೆ.",
        "ಬೆಳೆಗಳು ಮಾಗಿದ್ದರೆ, ಸಾಧ್ಯವಾದಷ್ಟು ಬೇಗ ಕಟಾವು ಮಾಡಿ ಒಣ ಜಾಗದಲ್ಲಿ ಟಾರ್ಪಲ್‌ನಿಂದ ಮುಚ್ಚಿಡಿ.",
        "ಜಾನುವಾರುಗಳು, ಬೀಜ, ಧಾನ್ಯ ಮತ್ತು ಉಪಕರಣಗಳನ್ನು ಎತ್ತರದ ಒಣ ಜಾಗಕ್ಕೆ ಸ್ಥಳಾಂತರಿಸಿ. ಮೇವನ್ನು ಸುರಕ್ಷಿತವಾಗಿ ಮುಚ್ಚಿಡಿ.",
        "ಹಳ್ಳ-ಕೊಳ್ಳಗಳು, ಕಾಲುವೆಗಳು ಮತ್ತು ಬಿದ್ದ ವಿದ್ಯುತ್ ತಂತಿಗಳಿಂದ ದೂರವಿರಿ.",
        "ವಿಮೆ ಮಾಡಿದ ಬೆಳೆಗೆ ಪ್ರವಾಹದಿಂದ ಹಾನಿಯಾದರೆ 72 ಗಂಟೆಯೊಳಗೆ 14447 ಸಹಾಯವಾಣಿಗೆ ಕರೆ ಮಾಡಿ ಅಥವಾ ಕ್ರಾಪ್ ಇನ್ಶೂರೆನ್ಸ್ ಆ್ಯಪ್‌ನಲ್ಲಿ ಫೋಟೋ ಅಪ್‌ಲೋಡ್ ಮಾಡಿ.",
    ],
    "Thunderstorm and lightning": [
        "ಜಮೀನಿನ ಕೆಲಸವನ್ನು ತಕ್ಷಣ ನಿಲ್ಲಿಸಿ ಗಟ್ಟಿ ಕಟ್ಟಡ ಅಥವಾ ವಾಹನದಲ್ಲಿ ಆಶ್ರಯ ಪಡೆಯಿರಿ. ಮರದ ಕೆಳಗೆ ನಿಲ್ಲಬೇಡಿ.",
        "ನೀರು, ತಂತಿ ಬೇಲಿ ಮತ್ತು ಲೋಹದ ಉಪಕರಣಗಳಿಂದ ದೂರವಿರಿ. ಬಯಲಿನಲ್ಲಿ ಸಿಲುಕಿದರೆ ತಲೆ ತಗ್ಗಿಸಿ ಕಾಲುಗಳನ್ನು ಒಟ್ಟಿಗೆ ಇಟ್ಟು ಕುಳಿತುಕೊಳ್ಳಿ.",
        "ಗುಡುಗು ಮಿಂಚು ಆರಂಭವಾಗುವ ಮುನ್ನ ಕೃಷಿ ಪಂಪ್‌ಸೆಟ್ ಮತ್ತು ವಿದ್ಯುತ್ ಉಪಕರಣಗಳನ್ನು ಆಫ್ ಮಾಡಿ.",
        "ಸಿಡಿಲಿನ ಮುನ್ಸೂಚನೆಗಾಗಿ ದಾಮಿನಿ {Damini} ಮೊಬೈಲ್ ಆ್ಯಪ್ ಬಳಸಿ.",
    ],
    "Strong wind": [
        "ಬಾಳೆ, ಪರಂಗಿ ಮತ್ತು ಎತ್ತರದ ಬೆಳೆಗಳಿಗೆ ಆಸರೆ ಕೋಲುಗಳನ್ನು ಕಟ್ಟಿ. ಪಾಲಿಹೌಸ್ ಮತ್ತು ಶೇಡ್-ನೆಟ್ ಶೀಟ್‌ಗಳನ್ನು ಭದ್ರಪಡಿಸಿ.",
        "ಬಿರುಗಾಳಿಯಲ್ಲಿ ಔಷಧ ಸಿಂಪಡಿಸಬೇಡಿ; ಗಾಳಿಗೆ ಔಷಧ ಹಾರಿ ನೆರೆಹೊರೆಯವರಿಗೆ ಮತ್ತು ಜೇನುನೊಣಗಳಿಗೆ ಹಾನಿಯುಂಟುಮಾಡುತ್ತದೆ.",
        "ಕೊಟ್ಟಿಗೆಯ ಮೇಲ್ಛಾವಣಿ ಮತ್ತು ಕೃಷಿ ಸಲಕರಣೆಗಳನ್ನು ಸುರಕ್ಷಿತವಾಗಿ ಕಟ್ಟಿಡಿ.",
        "ಬೆಳೆ ವಿಮೆ ಹೊಂದಿದ್ದರೆ 72 ಗಂಟೆಯೊಳಗೆ ಸ್ಥಳೀಯ ಕೃಷಿ ಇಲಾಖೆಗೆ ಮಾಹಿತಿ ನೀಡಿ.",
    ],
    "Heat": [
        "ಮುಂಜಾನೆ ಅಥವಾ ಸಂಜೆ ವೇಳೆ ನೀರಾವರಿ ಮಾಡಿ, ತೇವಾಂಶ ಉಳಿಸಿಕೊಳ್ಳಲು ಬೆಳೆ ತ್ಯಾಜ್ಯದಿಂದ ಹೊದಿಕೆ {ಮಲ್ಚಿಂಗ್} ಮಾಡಿ.",
        "ಮಧ್ಯಾಹ್ನ 12 ರಿಂದ 3 ಗಂಟೆಯವರೆಗೆ ಕಠಿಣ ಕೆಲಸ ಮಾಡಬೇಡಿ. ಹೆಚ್ಚು ನೀರು ಕುಡಿಯಿರಿ, ನೆರಳಿನಲ್ಲಿ ವಿಶ್ರಮಿಸಿ.",
        "ತಲೆತಿರುಗುವಿಕೆ ಅಥವಾ ಆಯಾಸ ಕಂಡುಬಂದರೆ ತಕ್ಷಣ ವೈದ್ಯಕೀಯ ನೆರವು ಪಡೆಯಿರಿ.",
        "ಜಾನುವಾರುಗಳಿಗೆ ನೆರಳು ಮತ್ತು ಶುದ್ಧ ಕುಡಿಯುವ ನೀರನ್ನು ಒದಗಿಸಿ.",
        "ಒಣ ಮಣ್ಣಿಗೆ ನೀರಾವರಿ ಇಲ್ಲದೆ ರಸಗೊಬ್ಬರ ಹಾಕಬೇಡಿ.",
    ],
    "Humid and warm (fungal diseases favoured)": [
        "ಪ್ರತಿ 2-3 ದಿನಗಳಿಗೊಮ್ಮೆ ಎಲೆಗಳ ಮೇಲೆ ಕಲೆಗಳು ಅಥವಾ ಶಿಲೀಂಧ್ರ ರೋಗ ಲಕ್ಷಣಗಳಿವೆಯೇ ಎಂದು ಪರೀಕ್ಷಿಸಿ.",
        "ಗಾಳಿಯಾಡುವಿಕೆ ಉತ್ತಮವಾಗಿರಲು ಅಂತರ ಕಾಯ್ದುಕೊಳ್ಳಿ ಮತ್ತು ರೋಗಪೀಡಿತ ಎಲೆಗಳನ್ನು ತೆಗೆದು ನಾಶಪಡಿಸಿ.",
        "ರೋಗ ಲಕ್ಷಣ ಕಂಡುಬಂದರೆ ಕೃಷಿ ವಿಜ್ಞಾನ ಕೇಂದ್ರ {KVK} ಅಥವಾ ರೈತ ಸಂಪರ್ಕ ಕೇಂದ್ರಕ್ಕೆ {RSK} ತೋರಿಸಿ ಸಲಹೆ ಪಡೆಯಿರಿ.",
        "ಶಿಫಾರಸು ಮಾಡಿದ ಪ್ರಮಾಣವನ್ನು ಮಾತ್ರ ಬಳಸಿ. ನಿಷೇಧಿತ ರಾಸಾಯನಿಕಗಳನ್ನು ಬಳಸಬೇಡಿ.",
        "ರಾತ್ರಿಯಿಡೀ ಎಲೆಗಳು ತೇವವಾಗಿ ಉಳಿಯುವಂತೆ ಸಂಜೆ ವೇಳೆ ನೀರಾವರಿ ಮಾಡಬೇಡಿ.",
    ],
    "Dry week ahead": [
        "ಆದ್ಯತೆಯ ಆಧಾರದ ಮೇಲೆ ನೀರಾವರಿ ಯೋಜಿಸಿ. ಹೂವಾಡುವ ಮತ್ತು ಕಾಳು ತುಂಬುವ ಹಂತದಲ್ಲಿರುವ ಬೆಳೆಗಳಿಗೆ ಮೊದಲ ಆದ್ಯತೆ ನೀಡಿ.",
        "ತೇವಾಂಶ ಸಂರಕ್ಷಣೆಗಾಗಿ ಬೆಳೆ ತ್ಯಾಜ್ಯದ ಹೊದಿಕೆ {ಮಲ್ಚಿಂಗ್} ಮಾಡಿ ಮತ್ತು ಕಳೆಗಳನ್ನು ತೆಗೆಯಿರಿ.",
        "ಮಣ್ಣಿನಲ್ಲಿ ತೇವಾಂಶವಿಲ್ಲದೆ ಮೇಲುಗೊಬ್ಬರ ಹಾಕಬೇಡಿ.",
        "ಜಾನುವಾರುಗಳಿಗೆ ಕುಡಿಯುವ ನೀರನ್ನು ಸಂಗ್ರಹಿಸಿಟ್ಟುಕೊಳ್ಳಿ.",
    ],
}

HAZARD_NAMES_KN = {
    "Heavy rain": "ಭಾರೀ ಮಳೆ",
    "Thunderstorm and lightning": "ಗುಡುಗು ಮತ್ತು ಮಿಂಚು",
    "Strong wind": "ಬಲವಾದ ಗಾಳಿ",
    "Heat": "ತೀವ್ರ ಬಿಸಿಗಾಳಿ",
    "Humid and warm (fungal diseases favoured)": "ಹೆಚ್ಚಿನ ತೇವಾಂಶ ಮತ್ತು ಶಿಲೀಂಧ್ರ ರೋಗದ ಅಪಾಯ",
    "Dry week ahead": "ಮುಂದಿನ 7 ದಿನ ಒಣ ಹವಾಮಾನ",
}

GENERAL_EN = [
    "Register for IMD alerts: the Mausam, Meghdoot (farm advisories) and Damini (lightning) apps, and the IMD SMS service.",
    "Keep Aadhaar, land records, bank passbook and the crop insurance receipt in a waterproof cover, with your phone charged.",
    "Wear gloves, a mask and full clothing when spraying. Wash hands and clothes after. Store chemicals locked, away from children, food and animal feed. Never reuse empty pesticide containers.",
    "Use only the dose on the label or advised by your agriculture officer. More is not better and it costs you money.",
    "Keep livestock vaccinations up to date as advised by your veterinarian.",
    "Check your crop insurance enrolment before the season. Damage from a localized calamity must be reported within 72 hours.",
]

GENERAL_KN = [
    "ಹವಾಮಾನ ಎಚ್ಚರಿಕೆಗಳಿಗಾಗಿ ಮೌಸಮ್ {Mausam}, ಮೇಘದೂತ್ {Meghdoot} ಮತ್ತು ದಾಮಿನಿ {Damini} ಮೊಬೈಲ್ ಆ್ಯಪ್‌ಗಳನ್ನು ಡೌನ್‌ಲೋಡ್ ಮಾಡಿ.",
    "ಆಧಾರ್, ಪಹಣಿ {RTC}, ಬ್ಯಾಂಕ್ ಪಾಸ್‌ಬುಕ್ ಮತ್ತು ಬೆಳೆ ವಿಮೆ ರಸೀದಿಗಳನ್ನು ನೀರಿನಿಂದ ರಕ್ಷಿಸುವ ಕವರ್‌ನಲ್ಲಿ ಸುರಕ್ಷಿತವಾಗಿಡಿ.",
    "ಔಷಧ ಸಿಂಪಡಿಸುವಾಗ ಕೈಗವಸು, ಮಾಸ್ಕ್ ಮತ್ತು ಪೂರ್ಣ ಉಡುಪು ಧರಿಸಿ. ನಂತರ ಕೈ-ಕಾಲುಗಳನ್ನು ಸಾಬೂನಿನಿಂದ ಸ್ವಚ್ಛವಾಗಿ ತೊಳೆಯಿರಿ.",
    "ಲೇಬಲ್‌ನಲ್ಲಿ ಅಥವಾ ಕೃಷಿ ಅಧಿಕಾರಿಗಳು ಶಿಫಾರಸು ಮಾಡಿದ ಪ್ರಮಾಣವನ್ನು ಮಾತ್ರ ಬಳಸಿ. ಹೆಚ್ಚಿನ ಪ್ರಮಾಣ ಬಳಕೆ ಹಣ ವ್ಯರ್ಥ ಮತ್ತು ಬೆಳೆಗೆ ಹಾನಿ.",
    "ಜಾನುವಾರುಗಳಿಗೆ ಕಾಲಕಾಲಕ್ಕೆ ಪಶುವೈದ್ಯರ ಸಲಹೆಯಂತೆ ಲಸಿಕೆ ಹಾಕಿಸಿ.",
    "ಬೆಳೆ ಹಾನಿಯಾದಲ್ಲಿ 72 ಗಂಟೆಯೊಳಗೆ 14447 ಸಹಾಯವಾಣಿಗೆ ಕರೆ ಮಾಡಿ ಅಥವಾ ವಿಮಾ ಕಂಪನಿಗೆ ವರದಿ ನೀಡಿ.",
]

IMD_COLOURS_EN = {
    "No warning (green)": "No action needed. Keep checking for updates.",
    "Yellow: be aware": "Stay updated. Plan your field work around the weather and keep inputs and produce protected.",
    "Orange: be prepared": "Be prepared. Finish urgent harvesting and spraying early, move produce and livestock to safe places, and avoid unnecessary travel.",
    "Red: take action": "Take action now. Avoid field work, move people and livestock to safety, and follow instructions from local officials.",
}

IMD_COLOURS_KN = {
    "ಯಾವುದೇ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ (ಹಸಿರು)": "ಯಾವುದೇ ತುರ್ತು ಕ್ರಮ ಅಗತ್ಯವಿಲ್ಲ. ನಿಯಮಿತ ಕೃಷಿ ಚಟುವಟಿಕೆ ಮುಂದುವರಿಸಿ.",
    "ಹಳದಿ ಎಚ್ಚರಿಕೆ: ಜಾಗರೂಕರಾಗಿರಿ": "ಹವಾಮಾನ ಬದಲಾವಣೆ ಗಮನಿಸಿ. ಕೃಷಿ ಕೆಲಸಗಳನ್ನು ಯೋಜಿಸಿ ಕೃಷಿ ಉತ್ಪನ್ನಗಳನ್ನು ರಕ್ಷಿಸಿ.",
    "ಕಿತ್ತಳೆ ಎಚ್ಚರಿಕೆ: ಸಿದ್ಧರಾಗಿರಿ": "ಸಿದ್ಧತೆ ಮಾಡಿಕೊಳ್ಳಿ. ತುರ್ತು ಕಟಾವು ಮುಗಿಸಿ, ಜಾನುವಾರುಗಳನ್ನು ಸುರಕ್ಷಿತ ಸ್ಥಳಕ್ಕೆ ತನ್ನಿ.",
    "ಕೆಂಪು ಎಚ್ಚರಿಕೆ: ತಕ್ಷಣ ಕ್ರಮ ಕೈಗೊಳ್ಳಿ": "ತಕ್ಷಣ ಕ್ರಮ ಕೈಗೊಳ್ಳಿ. ಜಮೀನಿನ ಕೆಲಸ ನಿಲ್ಲಿಸಿ, ಸುರಕ್ಷಿತ ಕಟ್ಟಡದಲ್ಲಿ ಆಶ್ರಯ ಪಡೆಯಿರಿ.",
}

IMD_HAZARDS_EN = {
    "Heavy rain": "Heavy rain",
    "Thunderstorm and lightning": "Thunderstorm and lightning",
    "Strong winds": "Strong wind",
    "Heat wave": "Heat",
}

IMD_HAZARDS_KN = {
    "ಭಾರೀ ಮಳೆ": "Heavy rain",
    "ಗುಡುಗು ಮತ್ತು ಮಿಂಚು": "Thunderstorm and lightning",
    "ಬಲವಾದ ಗಾಳಿ": "Strong wind",
    "ಬಿಸಿಗಾಳಿ": "Heat",
}

def rain_class(mm, is_kn):
    if is_kn:
        if mm < 0.1: return "ಮಳೆಯಿಲ್ಲ"
        if mm < 2.5: return "ಬಹಳ ಹಗುರ ಮಳೆ"
        if mm < 15.6: return "ಹಗುರ ಮಳೆ"
        if mm < 64.5: return "ಸಾಧಾರಣ ಮಳೆ"
        if mm < 115.6: return "ಭಾರೀ ಮಳೆ"
        if mm < 204.5: return "ಅತಿ ಭಾರೀ ಮಳೆ"
        return "ಅತ್ಯಂತ ಭಾರೀ ಮಳೆ"
    else:
        if mm < 0.1: return "No rain"
        if mm < 2.5: return "Very light"
        if mm < 15.6: return "Light"
        if mm < 64.5: return "Moderate"
        if mm < 115.6: return "Heavy"
        if mm < 204.5: return "Very heavy"
        return "Extremely heavy"

@st.cache_data(ttl=1800, show_spinner="Loading forecast...")
def fetch_forecast(lat, lon):
    params = {
        "latitude": lat,
        "longitude": lon,
        "daily": "temperature_2m_max,temperature_2m_min,precipitation_sum,wind_gusts_10m_max",
        "hourly": "relative_humidity_2m",
        "timezone": "Asia/Kolkata",
        "forecast_days": 7,
    }
    url = "https://api.open-meteo.com/v1/forecast?" + urllib.parse.urlencode(params)
    with urllib.request.urlopen(url, timeout=15) as resp:
        data = json.loads(resp.read().decode("utf-8"))
    daily = pd.DataFrame(data["daily"]).rename(columns={
        "time": "date", "temperature_2m_max": "tmax", "temperature_2m_min": "tmin",
        "precipitation_sum": "rain", "wind_gusts_10m_max": "gust"})
    hourly = pd.DataFrame(data["hourly"])
    hourly["date"] = hourly["time"].str[:10]
    humidity = hourly.groupby("date")["relative_humidity_2m"].mean().round(0)
    daily["humidity"] = daily["date"].map(humidity)
    return daily, datetime.now(IST).strftime("%d %b %Y, %I:%M %p IST")

def hazards_for(daily, is_kn):
    found = {}
    for i, row in daily.head(3).iterrows():
        label = pd.to_datetime(row["date"]).strftime("%a %d %b")
        if row["rain"] >= 64.5:
            found.setdefault("Heavy rain", []).append(label)
        if row["gust"] >= 40:
            found.setdefault("Strong wind", []).append(label)
        if row["tmax"] >= 38:
            found.setdefault("Heat", []).append(label)
        if row["humidity"] >= 85 and row["tmin"] >= 20:
            found.setdefault("Humid and warm (fungal diseases favoured)", []).append(label)
    if daily["rain"].sum() < 5:
        found["Dry week ahead"] = ["ಮುಂದಿನ 7 ದಿನಗಳು" if is_kn else "next 7 days"]
    return found

is_kn = (i18n.current_lang() == "kn")

hero_title = "ಹವಾಮಾನ ಮುನ್ನೆಚ್ಚರಿಕೆಗಳು" if is_kn else "Weather precautions"
hero_desc = (
    "ಕರ್ನಾಟಕದ ಜಿಲ್ಲೆಗಳಿಗೆ 7 ದಿನಗಳ ಹವಾಮಾನ ಮುನ್ಸೂಚನೆ ಮತ್ತು ಕೃಷಿ ಮುನ್ನೆಚ್ಚರಿಕೆ ಕ್ರಮಗಳು."
    if is_kn else
    "7-day forecast by district, with what to do before the weather turns. General guidance, not crop-specific advice."
)
ui.hero(hero_title, hero_desc, "⛈️")

district = st.selectbox(
    "ನಿಮ್ಮ ಜಿಲ್ಲೆಯನ್ನು ಆರಿಸಿ" if is_kn else "Your district",
    sorted(DISTRICTS),
    index=sorted(DISTRICTS).index("Mysuru"),
    format_func=lambda d: DISTRICTS_KN.get(d, d) if is_kn else d
)

if st.button("ಹವಾಮಾನ ವಿವರ ನವೀಕರಿಸಿ" if is_kn else "Refresh forecast"):
    fetch_forecast.clear()

lat, lon = DISTRICTS[district]
try:
    daily, updated = fetch_forecast(lat, lon)
except Exception:
    daily, updated = None, None
    err_text = (
        "ಪ್ರಸ್ತುತ ಹವಾಮಾನ ವಿವರಗಳನ್ನು ಲೋಡ್ ಮಾಡಲು ಸಾಧ್ಯವಾಗುತ್ತಿಲ್ಲ. ಇಂಟರ್ನೆಟ್ ಸಂಪರ್ಕ ಪರಿಶೀಲಿಸಿ."
        if is_kn else
        "Could not load the forecast right now. Check your internet and press Refresh. You can still use the official warning section below."
    )
    st.error(err_text)

if daily is not None:
    district_display = DISTRICTS_KN.get(district, district) if is_kn else district
    caption_text = (
        f"{district_display} ಜಿಲ್ಲೆಯ ಹವಾಮಾನ ಮುನ್ಸೂಚನೆ (ಓಪನ್-ಮೆಟಿಯೊ). ನವೀಕರಿಸಿದ ಸಮಯ: {updated}."
        if is_kn else
        f"Forecast for {district} (model data from Open-Meteo, not an official warning). Updated {updated}. It refreshes automatically about every 30 minutes."
    )
    st.caption(caption_text)
    found = hazards_for(daily, is_kn)

    st.subheader("ಮುಂದಿನ 3 ದಿನಗಳ ಮುನ್ಸೂಚನೆ" if is_kn else "Next 3 days")
    if found:
        for hazard, days in found.items():
            h_name = HAZARD_NAMES_KN.get(hazard, hazard) if is_kn else hazard
            st.warning(f"⚠️ **{h_name}**: {', '.join(days)}")
    else:
        st.success("ಮುಂದಿನ 3 ದಿನಗಳಲ್ಲಿ ಯಾವುದೇ ಗಂಭೀರ ಹವಾಮಾನ ಅಪಾಯವಿಲ್ಲ." if is_kn else "No major weather hazard in the next 3 days in this forecast.")

    table = pd.DataFrame({
        "ದಿನಾಂಕ" if is_kn else "Day": pd.to_datetime(daily["date"]).dt.strftime("%a %d %b"),
        "ಮಳೆ (ಮಿ.ಮೀ)" if is_kn else "Rain (mm)": daily["rain"].round(1),
        "ಮಳೆಯ ಪ್ರಮಾಣ" if is_kn else "Rain class": daily["rain"].apply(lambda r: rain_class(r, is_kn)),
        "ಗರಿಷ್ಠ / ಕನಿಷ್ಠ ತಾಪಮಾನ (°C)" if is_kn else "Max / Min (°C)": daily["tmax"].round(0).astype(int).astype(str) + " / " + daily["tmin"].round(0).astype(int).astype(str),
        "ಗಾಳಿಯ ವೇಗ (km/h)" if is_kn else "Gusts (km/h)": daily["gust"].round(0).astype(int),
        "ಆರ್ದ್ರತೆ (%)" if is_kn else "Humidity (%)": daily["humidity"].astype(int),
    })
    st.dataframe(table, hide_index=True)

    if found:
        st.subheader("ರೈತರು ಕೈಗೊಳ್ಳಬೇಕಾದ ತುರ್ತು ಮುನ್ನೆಚ್ಚರಿಕೆಗಳು" if is_kn else "What to do")
        for hazard in found:
            h_name = HAZARD_NAMES_KN.get(hazard, hazard) if is_kn else hazard
            tips = PRECAUTIONS_KN.get(hazard, PRECAUTIONS_EN.get(hazard, [])) if is_kn else PRECAUTIONS_EN.get(hazard, [])
            with st.expander(h_name, expanded=True):
                for tip in tips:
                    st.markdown(f"- {tip}")

st.subheader("ಅಧಿಕೃತ ಸರ್ಕಾರಿ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ" if is_kn else "Official warning (enter it yourself)")
st.write(
    "ದೂರದರ್ಶನ, ರೇಡಿಯೋ ಅಥವಾ ಮೌಸಮ್ {Mausam} ಆ್ಯಪ್‌ನಲ್ಲಿ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಕೇಳಿದ್ದೀರಾ? ಅದಕ್ಕೆ ತಕ್ಕ ಮುನ್ನೆಚ್ಚರಿಕೆ ತಿಳಿಯಲು ಇಲ್ಲಿ ಆರಿಸಿ."
    if is_kn else
    "Heard a warning on the government weather telecast, IMD or the Mausam app? Pick it here for matching precautions."
)

colours_dict = IMD_COLOURS_KN if is_kn else IMD_COLOURS_EN
colour = st.selectbox(
    "ನಿಮ್ಮ ಜಿಲ್ಲೆಯ ಎಚ್ಚರಿಕೆ ಬಣ್ಣದ ಸಂಕೇತ" if is_kn else "Warning colour for your district",
    list(colours_dict.keys())
)
st.info(colours_dict[colour])

hazards_dict = IMD_HAZARDS_KN if is_kn else IMD_HAZARDS_EN
no_warn_check = colour.startswith("ಯಾವುದೇ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ") if is_kn else colour.startswith("No warning")

if not no_warn_check:
    chosen = st.multiselect(
        "ಎಚ್ಚರಿಕೆಯ ವಿಧವನ್ನು ಆರಿಸಿ" if is_kn else "Warning type",
        list(hazards_dict.keys())
    )
    for name in chosen:
        canonical = hazards_dict[name]
        tips = PRECAUTIONS_KN.get(canonical, PRECAUTIONS_EN.get(canonical, [])) if is_kn else PRECAUTIONS_EN.get(canonical, [])
        with st.expander(name, expanded=True):
            for tip in tips:
                st.markdown(f"- {tip}")

with st.expander("ಪ್ರತಿಯೊಬ್ಬ ರೈತರಿಗಾಗಿ ಸಾಮಾನ್ಯ ಮುನ್ನೆಚ್ಚರಿಕೆ ನಿಯಮಗಳು" if is_kn else "General precautions for every farmer"):
    tips_gen = GENERAL_KN if is_kn else GENERAL_EN
    for tip in tips_gen:
        st.markdown(f"- {tip}")

st.subheader("ಸಹಾಯವಾಣಿ ಮತ್ತು ಅಧಿಕೃತ ಸಂಪರ್ಕ ಕೇಂದ್ರಗಳು" if is_kn else "Help and official sources")
if is_kn:
    st.markdown(
        "- ಬೆಳೆ ವಿಮೆ {PMFBY} ಸಹಾಯವಾಣಿ: **14447** (ಬೆಳೆ ಹಾನಿಯಾದರೆ 72 ಗಂಟೆಯೊಳಗೆ ಕರೆ ಮಾಡಿ ವರದಿ ಸಲ್ಲಿಸಿ).\n"
        "- ಕಿಸಾನ್ ಕಾಲ್ ಸೆಂಟರ್: **1800-180-1551** (ಉಚಿತ ಕರೆ).\n"
        "- ತುರ್ತು ಸೇವೆ: **112**.\n"
        "- ಅಧಿಕೃತ ಹವಾಮಾನ ಜಾಲತಾಣ: mausam.imd.gov.in\n"
        "- ಬೆಳೆ ವಿಮೆ ಪೋರ್ಟಲ್: pmfby.gov.in\n"
        "- ನಿಮ್ಮ ಬೆಳೆಗೆ ಸೂಕ್ತ ತಾಂತ್ರಿಕ ಸಲಹೆಗಾಗಿ ಹತ್ತಿರದ ಕೃಷಿ ವಿಜ್ಞಾನ ಕೇಂದ್ರ {KVK} ಅಥವಾ ರೈತ ಸಂಪರ್ಕ ಕೇಂದ್ರವನ್ನು {RSK} ಸಂಪರ್ಕಿಸಿ."
    )
else:
    st.markdown(
        "- Crop insurance (PMFBY) helpline: **14447**. Report localized crop loss within 72 hours.\n"
        "- Kisan Call Centre: **1800-180-1551**.\n"
        "- Emergency: **112**.\n"
        "- Official weather warnings: mausam.imd.gov.in\n"
        "- Crop insurance: pmfby.gov.in\n"
        "- For advice on your own crop, contact your nearest Krishi Vigyan Kendra or Raitha Samparka Kendra."
    )

ui.feedback_box()
st.markdown("---")
st.caption("© 2026 ಅಭಿಷೇಕ್ ಹಿಟಬುತ್ತಿ. ಕಿಸಾನ್ ದೃಷ್ಟಿ {AI} ಕೃಷಿ ಸಲಹಾ ವೇದಿಕೆ. ಎಲ್ಲ ಹಕ್ಕುಗಳನ್ನು ಕಾಯ್ದಿರಿಸಲಾಗಿದೆ." if is_kn else "© 2026 Abhishek Hitabutti. All rights reserved. Copying or reuse of this app without permission is prohibited.")
