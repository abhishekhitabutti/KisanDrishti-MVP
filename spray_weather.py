"""Spray-window check: is the next 3 days calm and dry enough to spray?

Forecast data comes from Open-Meteo (free, no key). The thresholds are simple rules, not IMD limits.
"""
import json
import urllib.parse
import urllib.request

import pandas as pd
import streamlit as st


@st.cache_data(ttl=1800, show_spinner=False)
def fetch_daily(lat, lon):
    params = {
        "latitude": lat, "longitude": lon,
        "daily": "precipitation_sum,wind_gusts_10m_max",
        "timezone": "Asia/Kolkata", "forecast_days": 3,
    }
    url = "https://api.open-meteo.com/v1/forecast?" + urllib.parse.urlencode(params)
    with urllib.request.urlopen(url, timeout=15) as resp:
        data = json.loads(resp.read().decode("utf-8"))
    daily = pd.DataFrame(data["daily"]).rename(columns={"precipitation_sum": "rain", "wind_gusts_10m_max": "gust"})
    return daily


def verdict(rain_mm, gust_kmh):
    if rain_mm >= 2.5 or gust_kmh >= 30:
        return "wait", "Wait"
    if rain_mm >= 0.5 or gust_kmh >= 20:
        return "careful", "Be careful"
    return "good", "Good"


def spray_window(daily):
    """Return table rows and an overall message for the next 3 days."""
    rows = []
    for _, r in daily.iterrows():
        key, label = verdict(float(r["rain"]), float(r["gust"]))
        day = pd.to_datetime(r["date"] if "date" in daily.columns else r["time"]).strftime("%a %d %b")
        rows.append({"Day": day, "Rain (mm)": round(float(r["rain"]), 1),
                     "Gusts (km/h)": round(float(r["gust"])), "Spraying": label, "_key": key})
    good = [r["Day"] for r in rows if r["_key"] == "good"]
    if rows and rows[0]["_key"] == "good":
        message = "Today looks calm and dry. If you spray, do it before 11 AM or after 3 PM."
    elif good:
        message = f"Best day to spray in this forecast: {good[0]}. Avoid wet or windy days."
    else:
        message = "No calm, dry day in the next 3 days. Wait for a better window unless an expert says it is urgent."
    return rows, message
