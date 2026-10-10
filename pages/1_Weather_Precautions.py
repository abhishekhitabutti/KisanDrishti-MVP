"""Weather precautions page for KisanDrishti.

Live forecast: Open-Meteo (free, no key). Not an official warning.
Official IMD warnings can be entered by hand from the government telecast / IMD apps.
"""
import json
import urllib.parse
import urllib.request
from datetime import datetime, timedelta, timezone

import pandas as pd
import streamlit as st

st.set_page_config(page_title="Weather Precautions | KisanDrishti", page_icon="⛈️")

# Approximate district headquarters (latitude, longitude)
DISTRICTS = {
    "Bagalkote": (16.18, 75.70), "Ballari": (15.14, 76.92), "Belagavi": (15.85, 74.50),
    "Bengaluru Rural": (13.25, 77.71), "Bengaluru Urban": (12.97, 77.59), "Bidar": (17.91, 77.52),
    "Chamarajanagar": (11.93, 76.94), "Chikkaballapura": (13.43, 77.73), "Chikkamagaluru": (13.32, 75.77),
    "Chitradurga": (14.23, 76.40), "Dakshina Kannada": (12.91, 74.86), "Davanagere": (14.47, 75.92),
    "Dharwad": (15.46, 75.01), "Gadag": (15.43, 75.63), "Hassan": (13.00, 76.10),
    "Haveri": (14.79, 75.40), "Kalaburagi": (17.33, 76.83), "Kodagu": (12.42, 75.74),
    "Kolar": (13.14, 78.13), "Koppal": (15.35, 76.15), "Mandya": (12.52, 76.90),
    "Mysuru": (12.30, 76.64), "Raichur": (16.21, 77.36), "Ramanagara": (12.72, 77.28),
    "Shivamogga": (13.93, 75.57), "Tumakuru": (13.34, 77.10), "Udupi": (13.34, 74.75),
    "Uttara Kannada": (14.81, 74.13), "Vijayanagara": (15.27, 76.39), "Vijayapura": (16.83, 75.71),
    "Yadgir": (16.77, 77.14),
}

IST = timezone(timedelta(hours=5, minutes=30))

PRECAUTIONS = {
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

GENERAL = [
    "Register for IMD alerts: the Mausam, Meghdoot (farm advisories) and Damini (lightning) apps, and the IMD SMS service.",
    "Keep Aadhaar, land records, bank passbook and the crop insurance receipt in a waterproof cover, with your phone charged.",
    "Wear gloves, a mask and full clothing when spraying. Wash hands and clothes after. Store chemicals locked, away from children, food and animal feed. Never reuse empty pesticide containers.",
    "Use only the dose on the label or advised by your agriculture officer. More is not better and it costs you money.",
    "Keep livestock vaccinations up to date as advised by your veterinarian.",
    "Check your crop insurance enrolment before the season. Damage from a localized calamity must be reported within 72 hours.",
]

IMD_COLOURS = {
    "No warning (green)": "No action needed. Keep checking for updates.",
    "Yellow: be aware": "Stay updated. Plan your field work around the weather and keep inputs and produce protected.",
    "Orange: be prepared": "Be prepared. Finish urgent harvesting and spraying early, move produce and livestock to safe places, and avoid unnecessary travel.",
    "Red: take action": "Take action now. Avoid field work, move people and livestock to safety, and follow instructions from local officials.",
}
IMD_HAZARDS = {
    "Heavy rain": "Heavy rain",
    "Thunderstorm and lightning": "Thunderstorm and lightning",
    "Strong winds": "Strong wind",
    "Heat wave": "Heat",
}


def rain_class(mm):
    """IMD 24-hour rainfall classes (mm)."""
    if mm < 0.1:
        return "No rain"
    if mm < 2.5:
        return "Very light"
    if mm < 15.6:
        return "Light"
    if mm < 64.5:
        return "Moderate"
    if mm < 115.6:
        return "Heavy"
    if mm < 204.5:
        return "Very heavy"
    return "Extremely heavy"


@st.cache_data(ttl=1800, show_spinner="Loading the latest forecast...")
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


def hazards_for(daily):
    """Return {hazard: [day labels]} for the next 3 days, plus a 7-day dry spell check."""
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
        found["Dry week ahead"] = ["next 7 days"]
    return found


st.title("Weather precautions")
st.caption("For Karnataka farmers. General guidance, not crop-specific advice.")

district = st.selectbox("Your district", sorted(DISTRICTS), index=sorted(DISTRICTS).index("Mysuru"))
if st.button("Refresh forecast"):
    fetch_forecast.clear()

lat, lon = DISTRICTS[district]
try:
    daily, updated = fetch_forecast(lat, lon)
except Exception:
    daily, updated = None, None
    st.error("Could not load the forecast right now. Check your internet and press Refresh. You can still use the official warning section below.")

if daily is not None:
    st.caption(f"Forecast for {district} (model data from Open-Meteo, not an official warning). Updated {updated}. It refreshes automatically about every 30 minutes.")
    found = hazards_for(daily)

    st.subheader("Next 3 days")
    if found:
        for hazard, days in found.items():
            st.warning(f"{hazard}: {', '.join(days)}")
    else:
        st.success("No major weather hazard in the next 3 days in this forecast.")

    table = pd.DataFrame({
        "Day": pd.to_datetime(daily["date"]).dt.strftime("%a %d %b"),
        "Rain (mm)": daily["rain"].round(1),
        "Rain class": daily["rain"].apply(rain_class),
        "Max / Min (°C)": daily["tmax"].round(0).astype(int).astype(str) + " / " + daily["tmin"].round(0).astype(int).astype(str),
        "Gusts (km/h)": daily["gust"].round(0).astype(int),
        "Humidity (%)": daily["humidity"].astype(int),
    })
    st.dataframe(table, hide_index=True)

    if found:
        st.subheader("What to do")
        for hazard in found:
            with st.expander(hazard, expanded=True):
                for tip in PRECAUTIONS[hazard]:
                    st.markdown(f"- {tip}")

st.subheader("Official warning (enter it yourself)")
st.write("Heard a warning on the government weather telecast, IMD or the Mausam app? Pick it here for matching precautions.")
colour = st.selectbox("Warning colour for your district", list(IMD_COLOURS))
st.info(IMD_COLOURS[colour])
if not colour.startswith("No warning"):
    chosen = st.multiselect("Warning type", list(IMD_HAZARDS))
    for name in chosen:
        with st.expander(name, expanded=True):
            for tip in PRECAUTIONS[IMD_HAZARDS[name]]:
                st.markdown(f"- {tip}")

with st.expander("General precautions for every farmer"):
    for tip in GENERAL:
        st.markdown(f"- {tip}")

st.subheader("Help and official sources")
st.markdown(
    "- Crop insurance (PMFBY) helpline: **14447**. Report localized crop loss within 72 hours.\n"
    "- Kisan Call Centre: **1800-180-1551**.\n"
    "- Emergency: **112**.\n"
    "- Official weather warnings: mausam.imd.gov.in\n"
    "- Crop insurance: pmfby.gov.in\n"
    "- For advice on your own crop, contact your nearest Krishi Vigyan Kendra or Raitha Samparka Kendra."
)

st.markdown("---")
st.caption("© 2026 Abhishek Hitabutti. All rights reserved. Copying or reuse of this app without permission is prohibited.")
