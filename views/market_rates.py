"""
KrushiNudi Market Rates & Best-Price Selling Centers.
Author: Abhishek Hitabutti
Copyright: © 2026 Abhishek Hitabutti. All rights reserved.

Daily mandi rates for 22+ Karnataka crops, 30-day price trend graphs,
14-day statistical forecasts, and verified government/APMC/private centers
where farmers can sell their harvest for the highest price.
"""

from html import escape
from pathlib import Path
import sys

# Ensure root directory is in sys.path
ROOT_DIR = Path(__file__).resolve().parent.parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

import pandas as pd
import streamlit as st

from districts import DISTRICTS, DISTRICTS_KN
import i18n
import mandi_data
import ui
from i18n import t

is_kn = (i18n.current_lang() == "kn")

# Page Header
hero_title = "ಮಾರುಕಟ್ಟೆ ದರ & ಗರಿಷ್ಠ ಬೆಲೆ ಮಾರಾಟ ಕೇಂದ್ರಗಳು {Market Rates & Selling Centers}" if is_kn else "Market Rates & Best-Price Selling Centers"
hero_desc = (
    "ಕರ್ನಾಟಕದ ಪ್ರಮುಖ ಬೆಳೆಗಳ ದೈನಂದಿನ ಎಪಿಎಂಸಿ ದರಗಳು, ಬೆಲೆ ಏರಿಕೆ/ಇಳಿಕೆ ಮುನ್ಸೂಚನಾ ಗ್ರಾಫ್ ಹಾಗೂ "
    "ಮಧ್ಯವರ್ತಿಗಳಿಲ್ಲದೆ ಗರಿಷ್ಠ ಬೆಲೆಗೆ ಬೆಳೆ ಮಾರಾಟ ಮಾಡಲು ನಿಮ್ಮ ಜಿಲ್ಲೆಯ ಅಧಿಕೃತ ಖರೀದಿ ಕೇಂದ್ರಗಳು."
    if is_kn else
    "Daily APMC mandi rates across Karnataka crops, 30-day price trend graphs, 14-day predictive forecasts, "
    "and verified government MSP depots, APMCs, and processing centers to sell your crop at the highest price."
)
ui.hero(hero_title, hero_desc, "📈")

# High-Impact Performance Metrics Strip
m1, m2, m3, m4 = st.columns(4)
m1.metric("ಲೈವ್ ಮಾರುಕಟ್ಟೆಗಳು" if is_kn else "APMC Yards Monitored", "31 ಜಿಲ್ಲೆಗಳು" if is_kn else "31 Districts", "ಇ-ನಾಮ್ ನೆಟ್‌ವರ್ಕ್ {e-NAM}")
m2.metric("ದೈನಂದಿನ ಬೆಳೆಗಳು" if is_kn else "Crops Tracked", "22 ಬೆಳೆಗಳು" if is_kn else "22 Key Crops", "ಧಾನ್ಯ, ಕಾಳು, ಮಸಾಲೆ, ತರಕಾರಿ")
m3.metric("ಖರೀದಿ ಕೇಂದ್ರಗಳು & ಮಳಿಗೆಗಳು" if is_kn else "Selling Centers & Shops", "60+ ಕೇಂದ್ರಗಳು" if is_kn else "60+ Verified Hubs", "31 ಜಿಲ್ಲೆಗಳು · ಸರ್ಕಾರಿ, ಎಪಿಎಂಸಿ & FPO" if is_kn else "All 31 Districts · MSP, APMC & FPOs")
m4.metric("ರೈತರ ಸರಾಸರಿ ಉಳಿತಾಯ" if is_kn else "Farmer Extra Profit", "+15% ರಿಂದ 35%" if is_kn else "+15% to 35%", "ಮಧ್ಯವರ್ತಿ ರಹಿತ {Direct}")

# Marketplace Tabs
tab_rates, tab_centers, tab_guide = st.tabs([
    "📊 ದೈನಂದಿನ ದರ & ಬೆಲೆ ಮುನ್ಸೂಚನಾ ಗ್ರಾಫ್ {Daily Rates & Graphs}" if is_kn else "📊 Daily Rates & Price Graphs",
    "🏢 ಗರಿಷ್ಠ ಬೆಲೆ ಮಾರಾಟ ಕೇಂದ್ರಗಳು {Best Price Selling Centers}" if is_kn else "🏢 Best Price Selling Centers & Mandis",
    "📋 ರೈತರ ಮಾರಾಟ ಮಾರ್ಗದರ್ಶಿ {Smart Selling Guide}" if is_kn else "📋 Smart Selling Guide & Checklist"
])

# ==============================================================================
# TAB 1: DAILY MARKET RATES, 30-DAY GRAPHS & 14-DAY PRICE FORECASTS
# ==============================================================================
with tab_rates:
    st.markdown("### 🌾 " + ("ದೈನಂದಿನ ಮಾರುಕಟ್ಟೆ ದರಗಳು & ಬೆಲೆ ಏರಿಕೆ/ಇಳಿಕೆ ಗ್ರಾಫ್" if is_kn else "Daily Mandi Rates & Price Trend Forecasts"))
    st.caption(
        "ನಿಮ್ಮ ಬೆಳೆಯನ್ನು ಆಯ್ಕೆಮಾಡಿ ಇಂದಿನ ಮಾರುಕಟ್ಟೆ ದರ, 30 ದಿನಗಳ ಸರಾಸರಿ ಹಾಗೂ ಬೆಲೆ ಏರಿಕೆಯಾಗುವುದೇ ಅಥವಾ ಇಳಿಕೆಯಾಗುವುದೇ ಎಂಬ ಮುನ್ಸೂಚನೆಯನ್ನು ಪರಿಶೀಲಿಸಿ."
        if is_kn else
        "Select your crop below to see today's modal price, 30-day historical average, and AI/expert forecast on whether prices will rise or fall."
    )

    all_crops = mandi_data.get_all_crops()
    crop_options = {c["id"]: (f"{c['name_kn']} ({c['name_en']})" if is_kn else f"{c['name_en']} ({c['name_kn']})") for c in all_crops}

    # Crop selector with trend indicator badge
    sel_crop_id = st.selectbox(
        "ಬೆಳೆಯನ್ನು ಆಯ್ಕೆಮಾಡಿ {Select Crop}:" if is_kn else "Select Crop:",
        list(crop_options.keys()),
        index=0,
        format_func=lambda cid: crop_options[cid]
    )

    crop_data = mandi_data.get_crop_data(sel_crop_id)
    history, forecast = mandi_data.generate_crop_history(crop_data)

    # 4 Key Metrics Cards
    k1, k2, k3, k4 = st.columns(4)
    with k1:
        with st.container(border=True):
            trend_icon = "📈" if crop_data["trend"] == "up" else ("📉" if crop_data["trend"] == "down" else "⚖️")
            st.markdown(f"**{trend_icon} " + ("ಇಂದಿನ ಸರಾಸರಿ ದರ {Modal}" if is_kn else "Today's Modal Rate") + "**")
            st.markdown(f"<div style='font-size:1.75rem; font-weight:800; color:#1B5E20;'>₹{crop_data['today_modal']:,}</div>", unsafe_allow_html=True)
            st.caption(f"{crop_data['unit']} · {crop_data['pct_change']} " + ("ಹಿಂದಿನ ವಾರಕ್ಕಿಂತ" if is_kn else "vs last week"))

    with k2:
        with st.container(border=True):
            st.markdown("**📊 " + ("30 ದಿನಗಳ ಸರಾಸರಿ {30-Day Avg}" if is_kn else "30-Day Average Rate") + "**")
            st.markdown(f"<div style='font-size:1.75rem; font-weight:700; color:#2E4B2E;'>₹{crop_data['avg_30d']:,}</div>", unsafe_allow_html=True)
            diff_avg = crop_data['today_modal'] - crop_data['avg_30d']
            diff_sign = "+" if diff_avg >= 0 else ""
            diff_color = "#2E7D32" if diff_avg >= 0 else "#C62828"
            st.markdown(f"<span style='color:{diff_color}; font-size:0.82rem; font-weight:600;'>{diff_sign}₹{diff_avg:,} " + ("ಸರಾಸರಿಗಿಂತ" if is_kn else "vs average") + "</span>", unsafe_allow_html=True)

    with k3:
        with st.container(border=True):
            msp_val = crop_data["msp"]
            msp_txt = f"₹{msp_val:,}" if msp_val > 0 else ("MSP ಅನ್ವಯಿಸುವುದಿಲ್ಲ" if is_kn else "No Govt MSP")
            st.markdown("**🏛️ " + ("ಸರ್ಕಾರಿ MSP ಬೆಂಬಲ ಬೆಲೆ" if is_kn else "Government MSP Rate") + "**")
            st.markdown(f"<div style='font-size:1.75rem; font-weight:700; color:#1565C0;'>{msp_txt}</div>", unsafe_allow_html=True)
            if msp_val > 0:
                diff_msp = crop_data['today_modal'] - msp_val
                sign_msp = "+" if diff_msp >= 0 else ""
                col_msp = "#2E7D32" if diff_msp >= 0 else "#C62828"
                lbl_msp = "MSP ಗಿಂತ ಹೆಚ್ಚು" if diff_msp >= 0 else "MSP ಗಿಂತ ಕಡಿಮೆ!"
                st.markdown(f"<span style='color:{col_msp}; font-size:0.82rem; font-weight:600;'>{sign_msp}₹{abs(diff_msp):,} {lbl_msp}</span>", unsafe_allow_html=True)
            else:
                st.caption("ಮುಕ್ತ ಮಾರುಕಟ್ಟೆ ದರ {Market Driven}")

    with k4:
        with st.container(border=True):
            st.markdown("**↕️ " + ("ದೈನಂದಿನ ಬೆಲೆ ವ್ಯಾಪ್ತಿ {Min-Max}" if is_kn else "Today's Price Range") + "**")
            st.markdown(f"<div style='font-size:1.45rem; font-weight:700; color:#455A64;'>₹{crop_data['min_price']:,} - ₹{crop_data['max_price']:,}</div>", unsafe_allow_html=True)
            st.caption("ಕನಿಷ್ಠ ಮತ್ತು ಗರಿಷ್ಠ ಗುಣಮಟ್ಟದ ದರ" if is_kn else "Quality-based min & max range")

    # Interactive Visual Chart (Graph) of 30-Day History and 14-Day Prediction
    st.markdown("#### 📈 " + ("ಬೆಲೆ ಇತಿಹಾಸ & ಮುಂದಿನ 14 ದಿನಗಳ ಮುನ್ಸೂಚನಾ ಗ್ರಾಫ್" if is_kn else "30-Day Price Trend & 14-Day Predictive Graph"))
    st.caption("ಹಸಿರು ಗೆರೆ: ಕಳೆದ 30 ದಿನಗಳ ವಾಸ್ತವಿಕ ದರ | ಕಿತ್ತಳೆ ಗೆರೆ: ಮುಂದಿನ 14 ದಿನಗಳ ನಿರೀಕ್ಷಿತ ದರ | ಕೆಂಪು ಗೆರೆ: 30 ದಿನಗಳ ಸರಾಸರಿ"
               if is_kn else
               "Historical daily modal price vs 30-day moving average and 14-day projected market direction.")

    # Build DataFrame for line_chart
    # Combine history and forecast into continuous timeseries
    chart_rows = []
    avg_line = crop_data["avg_30d"]
    msp_line = crop_data["msp"] if crop_data["msp"] > 0 else None

    for h in history:
        row = {
            "ದಿನಾಂಕ / Date": h["label"],
            "ಮಾರುಕಟ್ಟೆ ದರ (Mandi Price)": h["price"],
            "30 ದಿನಗಳ ಸರಾಸರಿ (30-Day Avg)": avg_line,
        }
        if msp_line:
            row["ಸರ್ಕಾರಿ MSP (Govt MSP)"] = msp_line
        chart_rows.append(row)

    for f in forecast:
        row = {
            "ದಿನಾಂಕ / Date": f["label"],
            "ಮಾರುಕಟ್ಟೆ ದರ (Mandi Price)": f["price"],
            "30 ದಿನಗಳ ಸರಾಸರಿ (30-Day Avg)": avg_line,
        }
        if msp_line:
            row["ಸರ್ಕಾರಿ MSP (Govt MSP)"] = msp_line
        chart_rows.append(row)

    df_chart = pd.DataFrame(chart_rows).set_index("ದಿನಾಂಕ / Date")
    st.line_chart(df_chart, height=340)

    # AI / Statistical Price Trend Verdict Box
    verdict_type = crop_data["verdict_type"]
    if verdict_type == "sell_now":
        box_bg = "#E8F5E9"
        box_border = "#2E7D32"
        badge_icon = "🟢"
        badge_txt = "ಮಾರಾಟಕ್ಕೆ ಅತ್ಯುತ್ತಮ ಸಮಯ {Sell Now}" if is_kn else "Optimal Selling Window: Sell Now"
    elif verdict_type == "hold":
        box_bg = "#FFF8E1"
        box_border = "#F9A825"
        badge_icon = "🟡"
        badge_txt = "ದಾಸ್ತಾನು ಮಾಡಿ ಕಾಯಿರಿ {Hold & Wait}" if is_kn else "Recommendation: Hold & Store"
    else:
        box_bg = "#E3F2FD"
        box_border = "#1565C0"
        badge_icon = "🏛️"
        badge_txt = "ಸರ್ಕಾರಿ MSP ಕೇಂದ್ರಕ್ಕೆ ನೀಡಿ {Sell at Govt Depot}" if is_kn else "Sell at Government MSP Purchase Depot"

    verdict_title = crop_data["verdict_kn"] if is_kn else crop_data["verdict_en"]
    reason_txt = crop_data["forecast_reason_kn"] if is_kn else crop_data["forecast_reason_en"]

    st.markdown(
        f"""
        <div style="background:{box_bg}; border: 2px solid {box_border}; border-radius: 14px; padding: 18px 20px; margin-top: 14px; margin-bottom: 20px;">
            <div style="font-size: 1.15rem; font-weight: 800; color: #1B2A1B; margin-bottom: 6px;">
                {badge_icon} {escape(verdict_title)}
            </div>
            <div style="font-size: 0.95rem; color: #2E4B2E; line-height: 1.5; font-weight: 500;">
                {escape(reason_txt)}
            </div>
            <div style="margin-top: 10px; font-size: 0.85rem; color: #555;">
                🎯 <b>{"ಮುಂದಿನ 14 ದಿನಗಳ ನಿರೀಕ್ಷಿತ ದರ {Target Price}:" if is_kn else "Projected 14-Day Price Target:"}</b>
                <span style="font-size: 1.05rem; font-weight: 800; color: {box_border}; margin-left: 6px;">₹{crop_data['target_14d']:,} {crop_data['unit']}</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

# ==============================================================================
# TAB 2: BEST PRICE SELLING CENTERS & MANDIS (SORT BY DISTRICT & RATE)
# ==============================================================================
with tab_centers:
    st.markdown("### 🏢 " + ("ನಿಮ್ಮ ಬೆಳೆಯನ್ನು ಗರಿಷ್ಠ ಬೆಲೆಗೆ ಖರೀದಿಸುವ ಅಧಿಕೃತ ಕೇಂದ್ರಗಳು" if is_kn else "Verified Centers & Mandis to Sell Your Crop at Highest Rates"))
    st.caption(
        "ದಲ್ಲಾಳಿಗಳಿಲ್ಲದೆ ನೇರವಾಗಿ ಎಪಿಎಂಸಿ ಪ್ರಾಂಗಣ, ಸರ್ಕಾರಿ MSP ಕೇಂದ್ರ, FPO ಸಹಕಾರಿ ಸಂಘ ಅಥವಾ ಪ್ರಮಾಣೀಕೃತ ಗಿರಣಿಗಳಿಗೆ ಮಾರಾಟ ಮಾಡಿ ಗರಿಷ್ಠ ಲಾಭ ಗಳಿಸಿ."
        if is_kn else
        "Sell directly to APMC yards, government MSP depots, FPOs, and certified mills to eliminate middleman margins."
    )

    # Search Box & District Filter Bar
    search_query = st.text_input(
        "🔍 ಕೇಂದ್ರ / ಮಳಿಗೆ / ತಾಲೂಕು ಹುಡುಕಿ {Search Center, Shop or Taluk}:" if is_kn else "🔍 Search Center, Shop, Town or Taluk:",
        placeholder="ಉದಾಹರಣೆಗೆ: ತಿಪಟೂರು, ಸಿರಗುಪ್ಪ, ಗಂಗಾವತಿ, Byadgi, Challakere, Tiptur, Siruguppa..." if is_kn else "e.g., Tiptur, Siruguppa, Gangavathi, Byadgi, Challakere, Mangaluru, Belagavi...",
        key="center_search_kw"
    )

    c_f1, c_f2, c_f3, c_f4 = st.columns([1.6, 1.5, 1.5, 1.8])

    with c_f1:
        dist_options = ["All"] + sorted(DISTRICTS)
        sel_dist = st.selectbox(
            "ಜಿಲ್ಲೆ {District}:" if is_kn else "District:",
            dist_options,
            format_func=lambda d: ("ಎಲ್ಲಾ 31 ಜಿಲ್ಲೆಗಳು {All 31 Districts}" if d == "All" else DISTRICTS_KN.get(d, d)) if is_kn else ("All 31 Districts" if d == "All" else d),
            key="center_filter_dist"
        )

    with c_f2:
        crop_sel_opts = [("all", "ಎಲ್ಲಾ ಬೆಳೆಗಳು {All Crops}" if is_kn else "All Crops")] + [
            (c["id"], c["name_kn"] if is_kn else c["name_en"]) for c in mandi_data.get_all_crops()
        ]
        sel_filter_crop = st.selectbox(
            "ಬೆಳೆ {Crop}:" if is_kn else "Crop:",
            [opt[0] for opt in crop_sel_opts],
            format_func=lambda cid: dict(crop_sel_opts)[cid],
            key="center_filter_crop"
        )

    with c_f3:
        cat_choices = {
            "all": "ಎಲ್ಲಾ ಕೇಂದ್ರಗಳು {All Types}" if is_kn else "All Center Types",
            "msp": "🏛️ ಸರ್ಕಾರಿ MSP ಕೇಂದ್ರಗಳು {Govt MSP}" if is_kn else "🏛️ Govt MSP Centers",
            "apmc": "🏬 ಎಪಿಎಂಸಿ ಪ್ರಾಂಗಣಗಳು {APMC Yards}" if is_kn else "🏬 APMC Main Yards",
            "fpo": "🏢 FPO / ಸಹಕಾರಿ ಸಂಘಗಳು {FPOs}" if is_kn else "🏢 FPOs & Cooperatives",
            "processor": "🌾 ಪ್ರಮಾಣೀಕೃತ ಗಿರಣಿಗಳು {Processors}" if is_kn else "🌾 Certified Mills"
        }
        sel_cat = st.selectbox(
            "ಕೇಂದ್ರದ ಪ್ರಕಾರ {Category}:" if is_kn else "Center Type:",
            list(cat_choices.keys()),
            format_func=lambda cid: cat_choices[cid],
            key="center_filter_cat"
        )

    with c_f4:
        sort_choices = {
            "highest_rate": "💰 ಗರಿಷ್ಠ ಬೆಲೆ ಮೊದಲು {Highest Rate}" if is_kn else "💰 Highest Rate First",
            "district": "📍 ಜಿಲ್ಲಾವಾರು {By District}" if is_kn else "📍 By District (A-Z)",
            "zero_commission": "⚡ ಶೂನ್ಯ ಕಮಿಷನ್ ಮೊದಲು {0% Commission}" if is_kn else "⚡ Zero Commission First"
        }
        sel_sort = st.selectbox(
            "ವಿಂಗಡಿಸಿ {Sort By}:" if is_kn else "Sort By:",
            list(sort_choices.keys()),
            format_func=lambda sid: sort_choices[sid],
            key="center_filter_sort"
        )

    # Fetch Filtered and Sorted Centers
    matching_centers = mandi_data.get_selling_centers(
        crop_id=sel_filter_crop,
        district=sel_dist,
        category=sel_cat,
        sort_by=sel_sort,
        search_query=search_query
    )

    st.markdown(f"**🔍 {len(matching_centers)} " + ("ಅಧಿಕೃತ ಖರೀದಿ ಕೇಂದ್ರಗಳು ಲಭ್ಯವಿದೆ" if is_kn else "Verified Centers Found") + "**")
    st.markdown("---")

    if not matching_centers:
        st.warning("ಆಯ್ಕೆ ಮಾಡಿದ ಜಿಲ್ಲೆ ಅಥವಾ ಬೆಳೆಗೆ ಸದ್ಯಕ್ಕೆ ಯಾವುದೇ ಕೇಂದ್ರಗಳು ಲಭ್ಯವಿಲ್ಲ. ದಯವಿಟ್ಟು 'All Karnataka' ಆಯ್ಕೆಮಾಡಿ."
                   if is_kn else
                   "No centers found matching your filters. Please select 'All Karnataka' or reset crop filter.")
    else:
        for center in matching_centers:
            with st.container(border=True):
                col_c1, col_c2 = st.columns([3.2, 1.8])

                with col_c1:
                    # Category Badge
                    cat_badge_style = {
                        "msp": ("#1565C0", "🏛️ ಸರ್ಕಾರಿ MSP ಖರೀದಿ ಕೇಂದ್ರ {Govt MSP}"),
                        "apmc": ("#2E7D32", "🏬 ಎಪಿಎಂಸಿ ಪ್ರಾಂಗಣ & ಇ-ನಾಮ್ {APMC Yard}"),
                        "fpo": ("#E65100", "🏢 ರೈತರ ಸಹಕಾರಿ / FPO {Cooperative}"),
                        "processor": ("#7B1FA2", "🌾 ಪ್ರಮಾಣೀಕೃತ ಸಂಸ್ಕರಣಾ ಗಿರಣಿ {Mill Direct}")
                    }.get(center["category"], ("#333", "ಖರೀದಿ ಕೇಂದ್ರ"))

                    dist_display = DISTRICTS_KN.get(center["district"], center["district"]) if is_kn else center["district"]
                    verified_badge_txt = "🛡️ ಅಧಿಕೃತ ಪರಿಶೀಲಿತ (Verified)" if is_kn else "🛡️ Verified Official"

                    st.markdown(
                        f"""
                        <span style="background:{cat_badge_style[0]}; color:white; font-size:0.75rem; font-weight:700; padding:2px 8px; border-radius:10px;">
                            {cat_badge_style[1]}
                        </span>
                        <span style="background:#E8F5E9; color:#1B5E20; font-size:0.75rem; font-weight:700; padding:2px 8px; border-radius:10px; margin-left:6px;">
                            {verified_badge_txt}
                        </span>
                        """,
                        unsafe_allow_html=True
                    )

                    c_name = center["name_kn"] if is_kn else center["name_en"]
                    st.markdown(f"#### {c_name}")
                    st.caption(f"📍 {center['address']} · **{dist_display} ({center['taluk']})**")

                    # Rate Highlights
                    rates = center.get("rates", {})
                    if rates:
                        rate_badges = []
                        for cid, rval in rates.items():
                            c_info = mandi_data.get_crop_data(cid)
                            c_lbl = c_info["name_kn"] if is_kn else c_info["name_en"]
                            rate_badges.append(f"<b>{c_lbl}:</b> <span style='color:#1B5E20; font-weight:800;'>₹{rval:,}</span> /qtl")

                        st.markdown(
                            "<div style='background:#F4F8F4; border-left:4px solid #2E7D32; padding:8px 12px; border-radius:8px; margin:8px 0; font-size:0.88rem;'>"
                            + " &nbsp;|&nbsp; ".join(rate_badges[:4]) +
                            "</div>",
                            unsafe_allow_html=True
                        )

                    # Premium over local middlemen
                    st.markdown(f"⭐ **ಲಾಭದ ಅಂಶ:** <span style='color:#2E7D32; font-weight:700;'>{center['premium_vs_local']}</span>", unsafe_allow_html=True)
                    st.caption(f"💰 ಕಮಿಷನ್: **{center['commission']}** | ⚖️ ತೂಕ: **{center['weighing']}**")

                    # Facilities Badges
                    fac_pills = "".join(f"<span style='background:#ECEFF1; color:#37474F; font-size:0.74rem; padding:2px 6px; border-radius:6px; margin-right:5px;'>{f}</span>" for f in center["facilities"])
                    st.markdown(f"<div style='margin-top:4px;'>{fac_pills}</div>", unsafe_allow_html=True)

                with col_c2:
                    st.markdown("<div style='text-align:right;'>", unsafe_allow_html=True)
                    # Contact & Direct Action Buttons
                    st.markdown(f"📞 **ಸಹಾಯವಾಣಿ / Phone:**")
                    st.markdown(f"<div style='font-size:1.15rem; font-weight:800; color:#1565C0; margin-bottom:8px;'>{center['phone']}</div>", unsafe_allow_html=True)
                    st.caption(f"⏰ {center['timings']}")

                    call_href = f"tel:{center['phone'].replace(' ', '')}"
                    maps_href = center["maps_url"]
                    call_label = "📞 ಕರೆ ಮಾಡಿ (Call Center)" if is_kn else "📞 Call Center"
                    maps_label = "🗺️ ದಾರಿ ನೋಡಿ (Google Maps)" if is_kn else "🗺️ View on Google Maps"

                    st.markdown(
                        f"""
                        <div style="display:flex; flex-direction:column; gap:8px; margin-top:12px;">
                            <a href="{call_href}" style="background:#2E7D32; color:white; text-decoration:none; text-align:center; padding:9px 12px; border-radius:10px; font-weight:700; font-size:0.88rem; box-shadow:0 2px 6px rgba(46,125,50,0.25);">
                                {call_label}
                            </a>
                            <a href="{maps_href}" target="_blank" style="background:#FFFFFF; color:#1B5E20; text-decoration:none; text-align:center; padding:8px 12px; border-radius:10px; font-weight:700; font-size:0.85rem; border:1px solid #A5D6A7;">
                                {maps_label}
                            </a>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )
                    st.markdown("</div>", unsafe_allow_html=True)

# ==============================================================================
# TAB 3: SMART SELLING CHECKLIST & MSP PROCESS
# ==============================================================================
with tab_guide:
    st.markdown("### 📋 " + ("ಬೆಳೆ ಮಾರಾಟದಲ್ಲಿ ಗರಿಷ್ಠ ಲಾಭ ಗಳಿಸಲು ರೈತರ ಸ್ಮಾರ್ಟ್ ಮಾರ್ಗದರ್ಶಿ" if is_kn else "Farmer's Smart Checklist to Secure the Best Selling Rate"))
    st.caption(
        "ಮಾರುಕಟ್ಟೆಗೆ ಬೆಳೆ ಕೊಂಡೊಯ್ಯುವ ಮುನ್ನ ಈ 4 ಸೂತ್ರಗಳನ್ನು ಪಾಲಿಸಿದರೆ ಕ್ವಿಂಟಾಲಿಗೆ ₹300 ರಿಂದ ₹600 ವರೆಗೆ ಹೆಚ್ಚುವರಿ ಲಾಭ ಗಳಿಸಬಹುದು."
        if is_kn else
        "Follow these 4 essential steps before taking your produce to the market to maximize your returns."
    )

    g1, g2 = st.columns(2)
    with g1:
        with st.container(border=True):
            st.markdown("#### 1️⃣ ತೇವಾಂಶ ನಿಯಂತ್ರಣ {Moisture Management}")
            st.write(
                "• ಭತ್ತ, ಮೆಕ್ಕೆಜೋಳ, ತೊಗರಿ ಮತ್ತು ಕಡಲೆಗೆ ತೇವಾಂಶ **12% ಗಿಂತ ಕಡಿಮೆ** ಇರಬೇಕು.\n"
                "• ಹತ್ತಿಗೆ ತೇವಾಂಶ **8-10%** ಇರಬೇಕು.\n"
                "• ತೇವಾಂಶ ಹೆಚ್ಚಿದ್ದರೆ ಎಪಿಎಂಸಿ ದಲ್ಲಾಳಿಗಳು ತೂಕದಲ್ಲಿ 2-5 ಕೆಜಿ ಕಡಿತ (ತಾರಾ ಕಡಿತ) ಮಾಡುತ್ತಾರೆ. ಕಣದಲ್ಲಿ 2 ದಿನ ಚೆನ್ನಾಗಿ ಒಣಗಿಸಿ ಕೊಂಡೊಯ್ಯಿರಿ."
                if is_kn else
                "• Keep grains and pulses moisture below 12% to prevent unfair weight deduction.\n"
                "• Cotton moisture should be strictly between 8-10% for Grade-A pricing.\n"
                "• Solar dry your harvest for 2 days on tarpaulin before bringing to market."
            )

        with st.container(border=True):
            st.markdown("#### 2️⃣ ಗ್ರೇಡಿಂಗ್ & ಕ್ಲೀನಿಂಗ್ {Grading & Cleaning}")
            st.write(
                "• ಕಲ್ಲು, ಮಣ್ಣು, ಜಳ್ಳು ಮತ್ತು ಮುರಿದ ಕಾಳುಗಳನ್ನು ತೂರಿ (Winnowing) ಬೇರ್ಪಡಿಸಿ.\n"
                "• ಏಕರೂಪದ ಗಾತ್ರ ಮತ್ತು ಹೊಳಪುಳ್ಳ ಪ್ರಥಮ ದರ್ಜೆ ಧಾನ್ಯಕ್ಕೆ ಮಾರುಕಟ್ಟೆಯಲ್ಲಿ **₹300 - ₹500 ಕ್ವಿಂಟಾಲಿಗೆ ಅಧಿಕ ಬೆಲೆ** ಸಿಗುತ್ತದೆ."
                if is_kn else
                "• Remove chaff, dust, broken grains, and stones using air winnowing.\n"
                "• Uniform, shining Grade-A lots fetch a direct ₹300-500/qtl premium in e-NAM bids."
            )

    with g2:
        with st.container(border=True):
            st.markdown("#### 3️⃣ ಸರ್ಕಾರಿ MSP ಕೇಂದ್ರಕ್ಕೆ ಬೇಕಾಗುವ ದಾಖಲೆಗಳು {MSP Center Checklist}")
            st.write(
                "• **FID / FRUITS ಸಂಖ್ಯೆ:** ಗ್ರಾಮ ಕೃಷಿ ಇಲಾಖೆ ನೀಡಿದ ಗುರುತಿನ ಚೀಟಿ.\n"
                "• **ಚಾಲ್ತಿ ಪಹಣಿ (RTC):** ಬೆಳೆ ನಮೂದಾಗಿರುವ ಇತ್ತೀಚಿನ ಪಹಣಿ ಪತ್ರ.\n"
                "• **ಆಧಾರ್ ಕಾರ್ಡ್ & ಬ್ಯಾಂಕ್ ಪಾಸ್‌ಬುಕ್ ಜೆರಾಕ್ಸ್** (ಆಧಾರ್ ಲಿಂಕ್ ಆದ ಖಾತೆ).\n"
                "• ನೋಂದಣಿ ದಿನಾಂಕದೊಳಗೆ ಸಮೀಪದ KSCMF ಕೇಂದ್ರಕ್ಕೆ ತೆರಳಿ ಟೋಕನ್ ಪಡೆಯಿರಿ."
                if is_kn else
                "• **FID / FRUITS ID:** Karnataka Agriculture Dept Farmer Identification.\n"
                "• **Current RTC / Pahani:** With crop entry shown.\n"
                "• **Aadhaar Card & Bank Passbook Copy:** Aadhaar-seeded account for direct DBT transfer.\n"
                "• Collect your verified registration token before the scheme window closes."
            )

        with st.container(border=True):
            st.markdown("#### 4️⃣ ದಲ್ಲಾಳಿಗಳ ಮೋಸದಿಂದ ಎಚ್ಚರ {Broker Safety Warnings}")
            st.write(
                "⚠️ **ಕಚ್ಚಾ ಚೀಟಿ (Kachha Slip) ತೆಗೆದುಕೊಳ್ಳಬೇಡಿ:** ಯಾವಾಗಲೂ ಅಧಿಕೃತ ಎಪಿಎಂಸಿ ಕಂಪ್ಯೂಟರ್ ರಶೀದಿ ಮಾತ್ರ ಪಡೆಯಿರಿ.\n"
                "⚠️ **ಅನಧಿಕೃತ ತೂಕ ಕಡಿತ:** ಸರ್ಕಾರಿ ಪ್ರಮಾಣಿತ ಧರ್ಮಕಾಂಟಾದಲ್ಲಿ ಮಾತ್ರ ವಾಹನದ ತೂಕ ಮಾಡಿಸಿ.\n"
                "⚠️ **ಇ-ನಾಮ್ ಖಾತರಿ:** ನಿಮ್ಮ ಬೆಳೆ ಇ-ನಾಮ್ ಪೋರ್ಟಲ್‌ನಲ್ಲಿ ನಮೂದಾಗಿದ್ದರೆ ಹಣ ನೇರವಾಗಿ ನಿಮ್ಮ ಬ್ಯಾಂಕ್ ಖಾತೆಗೆ ಜಮೆಯಾಗುತ್ತದೆ."
                if is_kn else
                "⚠️ **Never accept unprinted kachha slips:** Insist on official computer-generated APMC receipts.\n"
                "⚠️ **Verify Tare Weight:** Use only certified weigh-bridges inside APMC yard premises.\n"
                "⚠️ **e-NAM Guarantee:** Transparent electronic bids ensure payment settles within 24 hours into your bank."
            )

st.markdown("---")
st.caption("© 2026 KrushiNudi · Abhishek Hitabutti. APMC Mandi Rates & Farmer Selling Hub. All rights reserved.")
