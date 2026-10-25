"""
KrushiNudi Direct Farm-to-Consumer (F2C) Market.
Author: Abhishek Hitabutti
Copyright: © 2026 Abhishek Hitabutti. All rights reserved.

Connecting Karnataka farmers directly with urban consumers, bulk buyers,
and organic food lovers to eliminate middlemen and ensure fair farm-gate prices.
"""

import urllib.parse
from html import escape
from pathlib import Path
import sys

# Ensure root directory is in sys.path
ROOT_DIR = Path(__file__).resolve().parent.parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

import streamlit as st

from districts import DISTRICTS, DISTRICTS_KN
import f2c_data
import i18n
import ui
from i18n import t

is_kn = (i18n.current_lang() == "kn")

# Page Header
hero_title = "ರೈತರಿಂದ ನೇರ ಖರೀದಿ {Direct Farm-to-Consumer Market}" if is_kn else "Direct Farm-to-Consumer (F2C) Market"
hero_desc = (
    "ಮಧ್ಯವರ್ತಿಗಳ ಹಾವಳಿಯಿಲ್ಲದೆ ನೇರವಾಗಿ ಸ್ಥಳೀಯ ರೈತರಿಂದ ತಾಜಾ, ಅಧಿಕೃತ ಉತ್ಪನ್ನಗಳನ್ನು ಖರೀದಿಸಿ. "
    "ರೈತರಿಗೆ ನ್ಯಾಯಯುತ ಲಾಭದಾಯಕ ಬೆಲೆ, ಗ್ರಾಹಕರಿಗೆ ನೈಜ ಗುಣಮಟ್ಟ ಹಾಗೂ ಗರಿಷ್ಠ ಉಳಿತಾಯ!"
    if is_kn else
    "Direct from Karnataka farmers to consumers with zero middlemen. "
    "Better farm-gate prices for farmers, 100% fresh authentic produce and savings for buyers."
)
ui.hero(hero_title, hero_desc, "🛒")

# High-Impact Banner Metrics
m1, m2, m3, m4 = st.columns(4)
m1.metric("ರೈತರ ಹೆಚ್ಚುವರಿ ಆದಾಯ" if is_kn else "Farmer Extra Income", "+45%", "ಮಧ್ಯವರ್ತಿ ರಹಿತ {No Brokers}")
m2.metric("ಗ್ರಾಹಕರ ಉಳಿತಾಯ" if is_kn else "Buyer Savings", "28%", "ಸೂಪರ್‌ಮಾರ್ಕೆಟ್‌ಗಿಂತ ಕಡಿಮೆ {vs Retail}")
m3.metric("ಕೊಯ್ಲಿನಿಂದ ಮನೆಬಾಗಿಲಿಗೆ" if is_kn else "Freshness Turnaround", "< 24 ಗಂಟೆ" if is_kn else "< 24 Hours", "ನೇರ ತಾಜಾತನ {Direct Fresh}")
m4.metric("ಕರ್ನಾಟಕದ ಜಿಲ್ಲೆಗಳು" if is_kn else "Districts Covered", "31 ಜಿಲ್ಲೆಗಳು" if is_kn else "31 Districts", "FPO & ಪ್ರಗತಿಪರ ರೈತರು")

# Marketplace Tabs
tab_buy, tab_sell, tab_calc, tab_rules = st.tabs([
    "🛒 ತಾಜಾ ಉತ್ಪನ್ನಗಳು {Browse & Buy}" if is_kn else "🛒 Browse & Buy Produce",
    "🌾 ಬೆಳೆ ಮಾರಾಟಕ್ಕೆ ಸೇರಿಸಿ {List Produce}" if is_kn else "🌾 List Your Harvest (For Farmers)",
    "📈 ಲಾಭದ ಕ್ಯಾಲ್ಕುಲೇಟರ್ {Profit Calculator}" if is_kn else "📈 F2C Profit Benchmark",
    "🛡️ ಸುರಕ್ಷಿತ ವ್ಯಾಪಾರ ನಿಯಮಗಳು {Fair-Trade Rules}" if is_kn else "🛡️ Safe Direct Trade Rules"
])

# ==============================================================================
# TAB 1: BROWSE PRODUCE & BUY (FOR CONSUMERS & BULK BUYERS)
# ==============================================================================
with tab_buy:
    st.markdown("### 🌾 " + ("ಕರ್ನಾಟಕದ ರೈತರಿಂದ ನೇರ ಕೊಯ್ಲಿನ ಉತ್ಪನ್ನಗಳು" if is_kn else "Direct Farm-Fresh Listings from Karnataka Farmers"))
    st.caption(
        "ಯಾವುದೇ ಕಮಿಷನ್ ದಲ್ಲಾಳಿಗಳಿಲ್ಲದೆ ನೇರವಾಗಿ ರೈತರಿಗೆ ಕರೆ ಮಾಡಿ ಅಥವಾ WhatsApp ಮೂಲಕ ಆರ್ಡರ್ ಮಾಡಿ."
        if is_kn else
        "Zero broker commissions. Call the farmer directly or place orders via instant WhatsApp messaging."
    )

    # Filter Bar
    f_col1, f_col2, f_col3 = st.columns([1.5, 1.5, 2])
    with f_col1:
        cat_choices = {c["id"]: (c["name_kn"] if is_kn else c["name_en"]) for c in f2c_data.CATEGORIES}
        sel_cat = st.selectbox(
            "ವರ್ಗ {Category}:" if is_kn else "Category:",
            list(cat_choices.keys()),
            format_func=lambda cid: f"{cat_choices[cid]}"
        )
    with f_col2:
        dist_options = ["All"] + sorted(DISTRICTS)
        sel_dist = st.selectbox(
            "ಜಿಲ್ಲೆ {District}:" if is_kn else "District:",
            dist_options,
            format_func=lambda d: ("ಎಲ್ಲಾ ಜಿಲ್ಲೆಗಳು {All Karnataka}" if d == "All" else DISTRICTS_KN.get(d, d)) if is_kn else ("All Karnataka" if d == "All" else d)
        )
    with f_col3:
        search_query = st.text_input(
            "ಉತ್ಪನ್ನ ಅಥವಾ ರೈತರ ಹೆಸರು ಹುಡುಕಿ {Search}:" if is_kn else "Search produce or farmer name:",
            placeholder="ಉದಾ: ಬೆಲ್ಲ, ರಾಗಿ, ಮೆಣಸಿನಕಾಯಿ, Honey, Rice..."
        ).strip().lower()

    # Load Listings
    all_listings = f2c_data.load_listings()
    filtered = []
    for item in all_listings:
        if sel_cat != "all" and item.get("category") != sel_cat:
            continue
        if sel_dist != "All" and item.get("district") != sel_dist:
            continue
        if search_query:
            match_str = f"{item.get('crop_name_kn', '')} {item.get('crop_name_en', '')} {item.get('farmer_name', '')} {item.get('district', '')} {item.get('variety', '')}".lower()
            if search_query not in match_str:
                continue
        filtered.append(item)

    st.markdown(f"**{'ಲಭ್ಯವಿರುವ ಉತ್ಪನ್ನಗಳು' if is_kn else 'Available Listings'}: ({len(filtered)})**")

    if not filtered:
        st.info(
            "🔍 ನಿಮ್ಮ ಹುಡುಕಾಟಕ್ಕೆ ತಕ್ಕ ಉತ್ಪನ್ನಗಳು ಸದ್ಯಕ್ಕೆ ಲಭ್ಯವಿಲ್ಲ. ದಯವಿಟ್ಟು ಬೇರೆ ವರ್ಗ ಅಥವಾ ಜಿಲ್ಲೆಯನ್ನು ಆರಿಸಿ."
            if is_kn else
            "🔍 No produce found matching your search. Please try a different category or district."
        )
    else:
        # Display in 2 responsive columns
        for idx in range(0, len(filtered), 2):
            card_col1, card_col2 = st.columns(2)
            cols = [card_col1, card_col2]

            for c_i in range(2):
                if idx + c_i < len(filtered):
                    item = filtered[idx + c_i]
                    with cols[c_i]:
                        with st.container(border=True):
                            crop_title = item.get("crop_name_kn" if is_kn else "crop_name_en") or item.get("crop_name_en")
                            badge_title = item.get("badge_kn" if is_kn else "badge_en", "Verified")
                            dist_name = DISTRICTS_KN.get(item.get("district"), item.get("district")) if is_kn else item.get("district")

                            # Card Header
                            st.markdown(
                                f"""
                                <div style="display:flex; justify-content:space-between; align-items:flex-start; margin-bottom:6px;">
                                    <div>
                                        <span style="font-size:1.15rem; font-weight:800; color:#1B5E20;">{escape(crop_title)}</span>
                                        <div style="font-size:0.8rem; color:#666;">{escape(item.get('variety', ''))}</div>
                                    </div>
                                    <span style="background:#E8F5E9; color:#2E7D32; font-size:0.75rem; font-weight:700; padding:3px 9px; border-radius:10px; border:1px solid #C8E6C9;">
                                        ✅ {escape(badge_title)}
                                    </span>
                                </div>
                                """,
                                unsafe_allow_html=True
                            )

                            # Farmer Credentials
                            st.markdown(
                                f"👨‍🌾 **{item.get('farmer_name')}** · 📍 *{item.get('village')}, {item.get('taluk')}, {dist_name}*"
                            )

                            # Price Comparison Bar
                            f_price = item.get("farm_price", 0)
                            m_price = item.get("mandi_price", 0)
                            r_price = item.get("retail_price", 0)
                            unit = item.get("unit", "kg")

                            st.markdown(
                                f"""
                                <div style="background:#F4F8F4; border:1px solid #DCE8DC; border-radius:12px; padding:10px 12px; margin:8px 0;">
                                    <div style="display:flex; justify-content:space-between; align-items:center;">
                                        <div>
                                            <span style="font-size:0.75rem; color:#666;">{'ರೈತರ ನೇರ ದರ {Direct Price}:' if is_kn else 'Farm-Gate Direct Price:'}</span>
                                            <div style="font-size:1.45rem; font-weight:800; color:#1B5E20;">₹{f_price} <span style="font-size:0.85rem; font-weight:500;">/ {unit}</span></div>
                                        </div>
                                        <div style="text-align:right; font-size:0.8rem; line-height:1.4;">
                                            <div><span style="color:#C62828; text-decoration:line-through;">{'ಮಾರುಕಟ್ಟೆ {City Store}:' if is_kn else 'Supermarket:'} ₹{r_price}</span></div>
                                            <div style="color:#2E7D32; font-weight:700;">{'ಉಳಿತಾಯ {You Save}:' if is_kn else 'You Save:'} ₹{max(0, r_price - f_price)} / {unit}</div>
                                        </div>
                                    </div>
                                </div>
                                """,
                                unsafe_allow_html=True
                            )

                            # Description & Quantity
                            desc = item.get("description_kn" if is_kn else "description_en", "")
                            st.caption(f"📦 **{'ಲಭ್ಯತೆ {Available}:' if is_kn else 'Stock Available:'}** `{item.get('quantity')}`")
                            st.write(desc)

                            # Direct Action Contact Buttons
                            btn_col1, btn_col2 = st.columns(2)
                            with btn_col1:
                                phone_clean = item.get("phone", "").replace(" ", "").replace("-", "")
                                st.link_button(
                                    "📞 " + ("ಕರೆ ಮಾಡಿ {Call}" if is_kn else "Call Farmer"),
                                    f"tel:{phone_clean}",
                                    use_container_width=True
                                )
                            with btn_col2:
                                wa_num = item.get("whatsapp", phone_clean)
                                wa_msg = urllib.parse.quote(
                                    f"ನಮಸ್ಕಾರ {item.get('farmer_name')}, ನಾನು ಕೃಷಿನುಡಿ ಆ್ಯಪ್‌ನಲ್ಲಿ ನಿಮ್ಮ '{crop_title}' ಉತ್ಪನ್ನವನ್ನು ನೋಡಿದೆ. ಖರೀದಿಸಲು ವಿವರಗಳನ್ನು ತಿಳಿಸಿ."
                                    if is_kn else
                                    f"Hello {item.get('farmer_name')}, I saw your '{crop_title}' on KrushiNudi. I would like to purchase. Please share details."
                                )
                                st.link_button(
                                    "💬 " + ("WhatsApp ಆರ್ಡರ್" if is_kn else "WhatsApp Order"),
                                    f"https://wa.me/{wa_num}?text={wa_msg}",
                                    use_container_width=True
                                )

# ==============================================================================
# TAB 2: LIST PRODUCE (FOR FARMERS TO SELL DIRECTLY)
# ==============================================================================
with tab_sell:
    st.markdown("### 👨‍🌾 " + ("ನಿಮ್ಮ ಬೆಳೆಯನ್ನು ನೇರವಾಗಿ ಗ್ರಾಹಕರಿಗೆ ಮಾರಾಟ ಮಾಡಿ" if is_kn else "List Your Farm Produce for Direct Sale"))
    st.caption(
        "ಯಾವುದೇ ಕಮಿಷನ್ ಅಥವಾ ನೋಂದಣಿ ಶುಲ್ಕವಿಲ್ಲ. ನಿಮ್ಮ ಫಸಲಿನ ವಿವರಗಳನ್ನು ಕೆಳಗೆ ಭರ್ತಿ ಮಾಡಿ. "
        "ಕರ್ನಾಟಕದ ಸಾವಿರಾರು ಗ್ರಾಹಕರು ಮತ್ತು ಸಗಟು ವ್ಯಾಪಾರಿಗಳು ನೇರವಾಗಿ ನಿಮ್ಮ ಮೊಬೈಲ್‌ಗೆ ಕರೆ ಮಾಡುತ್ತಾರೆ."
        if is_kn else
        "Zero listing fees, zero broker commissions. Post your harvest details below to receive direct calls and WhatsApp orders from buyers."
    )

    with st.container(border=True):
        st.markdown("#### 📝 " + ("ಬೆಳೆ ಮತ್ತು ರೈತರ ವಿವರಗಳ ನೋಂದಣಿ ಫಾರ್ಮ್" if is_kn else "Produce & Farmer Details Form"))

        s_col1, s_col2 = st.columns(2)
        with s_col1:
            f_name = st.text_input("ರೈತರ ಹೆಸರು {Farmer Name} *", placeholder="ಉದಾ: ಬಸವರಾಜ ಪಾಟೀಲ")
            f_phone = st.text_input("ಸಂಪರ್ಕ ಮೊಬೈಲ್ ಸಂಖ್ಯೆ {Phone Number} *", placeholder="ಉದಾ: +91 98450 12345")
            f_wa = st.text_input("WhatsApp ಸಂಖ್ಯೆ {WhatsApp Number}", placeholder="ಉದಾ: 9845012345")
            f_dist = st.selectbox(
                "ಜಿಲ್ಲೆ {District} *",
                sorted(DISTRICTS),
                index=sorted(DISTRICTS).index("Mandya"),
                format_func=lambda d: DISTRICTS_KN.get(d, d) if is_kn else d
            )
            f_taluk = st.text_input("ತಾಲೂಕು {Taluk} *", placeholder="ಉದಾ: ಮದ್ದೂರು / Maddur")
            f_village = st.text_input("ಹಳ್ಳಿ / ಜಮೀನು {Village / Farm Location} *", placeholder="ಉದಾ: ಕೊಪ್ಪ / Koppa")

        with s_col2:
            p_cat = st.selectbox(
                "ಉತ್ಪನ್ನದ ವರ್ಗ {Category} *",
                [c for c in f2c_data.CATEGORIES if c["id"] != "all"],
                format_func=lambda c: f"{c['icon']} {c['name_kn'] if is_kn else c['name_en']}"
            )
            p_name = st.text_input("ಬೆಳೆ / ಉತ್ಪನ್ನದ ಹೆಸರು {Crop Name} *", placeholder="ಉದಾ: ಸಾವಯವ ಬೆಲ್ಲ, ನಾಟಿ ರಾಗಿ, ಸೋನಾ ಮಸೂರಿ ಅಕ್ಕಿ")
            p_variety = st.text_input("ತಳಿ / ವಿಧ {Variety / Grade}", placeholder="ಉದಾ: ದೇಸಿ ತಳಿ, 1 ವರ್ಷ ಹಳೆಯ ಅಕ್ಕಿ, ಕೆಮಿಕಲ್ ಫ್ರೀ")
            p_qty = st.text_input("ಲಭ್ಯವಿರುವ ಒಟ್ಟು ಪ್ರಮಾಣ {Available Quantity} *", placeholder="ಉದಾ: 25 ಕ್ವಿಂಟಾಲ್ / 50 ಚೀಲ / 200 ಕೆ.ಜಿ.")
            p_unit = st.selectbox("ದರದ ಘಟಕ {Unit}", ["kg", "Quintal", "Litre", "Box", "Crate", "Bottle"])
            p_price = st.number_input("ನಿಮ್ಮ ನೇರ ಮಾರಾಟ ದರ (₹ ಪ್ರತಿ ಘಟಕಕ್ಕೆ) {Direct Price} *", min_value=1.0, value=50.0, step=1.0)
            p_organic = st.checkbox("🌱 ಇದು ಸಾವಯವ / ರಾಸಾಯನಿಕ ರಹಿತ ಫಸಲು {Organic / Pesticide-free}", value=True)

        p_desc = st.text_area(
            "ಉತ್ಪನ್ನದ ಗುಣಮಟ್ಟ ಮತ್ತು ವಿತರಣೆಯ ವಿಶೇಷತೆಗಳು {Description & Quality Notes}:",
            placeholder="ಉದಾ: ನಮ್ಮದೇ ಜಮೀನಿನಲ್ಲಿ ಬೆಳೆದ ನೈಸರ್ಗಿಕ ಬೆಳೆ. ನೇರ ಪ್ಯಾಕಿಂಗ್ ಮತ್ತು ತಾಜಾತನದ ಗ್ಯಾರಂಟಿ. ಸಾರಿಗೆ ಸೌಲಭ್ಯವಿದೆ."
        )

        if st.button("🚀 ಮಾರುಕಟ್ಟೆಯಲ್ಲಿ ಪ್ರಕಟಿಸಿ {Publish Listing on KrushiNudi}", type="primary", use_container_width=True):
            if not f_name or not f_phone or not p_name or not f_taluk:
                st.error("⚠️ ದಯವಿಟ್ಟು ಕಡ್ಡಾಯವಾಗಿ ನಮೂದಿಸಬೇಕಾದ ಎಲ್ಲಾ ವಿವರಗಳನ್ನು ಭರ್ತಿ ಮಾಡಿ (ಹೆಸರು, ಫೋನ್, ಬೆಳೆ, ತಾಲೂಕು).")
            else:
                new_item = {
                    "farmer_name": f_name,
                    "phone": f_phone,
                    "whatsapp": f_wa.strip() or f_phone.replace("+", "").replace(" ", "").replace("-", ""),
                    "district": f_dist,
                    "taluk": f_taluk,
                    "village": f_village or f_taluk,
                    "crop_name_kn": p_name,
                    "crop_name_en": p_name,
                    "category": p_cat["id"],
                    "variety": p_variety or "ಕೃಷಿ ತಾಜಾ ತಳಿ",
                    "quantity": p_qty or "ಲಭ್ಯವಿದೆ",
                    "farm_price": int(p_price),
                    "mandi_price": int(p_price * 0.7),
                    "retail_price": int(p_price * 1.5),
                    "unit": p_unit,
                    "harvest_date": "ಇತ್ತೀಚಿನ ಫಸಲು",
                    "is_organic": p_organic,
                    "badge_kn": "ಸಾವಯವ ಪ್ರಮಾಣಿತ" if p_organic else "ರೈತರ ತಾಜಾ ಫಸಲು",
                    "badge_en": "Organic Farm" if p_organic else "Farm Fresh",
                    "description_kn": p_desc or "ಉತ್ತಮ ಗುಣಮಟ್ಟದ ಕೃಷಿ ಉತ್ಪನ್ನ. ನೇರ ಸಂಪರ್ಕಿಸಿ.",
                    "description_en": p_desc or "Direct harvest from Karnataka farm. Call for delivery.",
                }
                f2c_data.add_listing(new_item)
                st.success("🎉 ಅಭಿನಂದನೆಗಳು! ನಿಮ್ಮ ಉತ್ಪನ್ನವನ್ನು ಕೃಷಿನುಡಿ ಮಾರುಕಟ್ಟೆಯಲ್ಲಿ ಯಶಸ್ವಿಯಾಗಿ ಪ್ರಕಟಿಸಲಾಗಿದೆ. ಖರೀದಿದಾರರು ನೇರವಾಗಿ ನಿಮ್ಮ ಮೊಬೈಲ್‌ಗೆ ಕರೆ ಮಾಡುತ್ತಾರೆ.")
                st.balloons()

# ==============================================================================
# TAB 3: F2C PROFIT BENCHMARK CALCULATOR
# ==============================================================================
with tab_calc:
    st.markdown("### 📈 " + ("ನೇರ ಮಾರಾಟದ ಮೂಲಕ ರೈತರಿಗೆ ಸಿಗುವ ಹೆಚ್ಚುವರಿ ಆದಾಯದ ಹೋಲಿಕೆ" if is_kn else "F2C Direct Sales Extra Profit Calculator"))
    st.caption(
        "ಸಾಮಾನ್ಯ ಎಪಿಎಂಸಿ ದಲ್ಲಾಳಿ ಮಂಡಿಗಿಂತ ಕೃಷಿನುಡಿ ನೇರ ಖರೀದಿಯ ಮೂಲಕ ನೀವು ಎಷ್ಟು ಲಕ್ಷ ರೂಪಾಯಿ ಉಳಿಸಬಹುದು ಮತ್ತು ಗಳಿಸಬಹುದು ಎಂದು ಲೆಕ್ಕ ಹಾಕಿ:"
        if is_kn else
        "Calculate your real farm-gate profit margins by bypassing middlemen commission and transport cuts:"
    )

    with st.container(border=True):
        col_c1, col_c2 = st.columns(2)
        with col_c1:
            crop_type = st.selectbox(
                "ಬೆಳೆ ಆಯ್ಕೆಮಾಡಿ {Select Crop}:",
                [
                    ("ರಾಗಿ {Ragi}", 30, 48, 65),
                    ("ಸೋನಾ ಮಸೂರಿ ಭತ್ತ / ಅಕ್ಕಿ {Rice}", 38, 58, 85),
                    ("ಬೆಲ್ಲದ ಪುಡಿ {Jaggery Powder}", 40, 65, 110),
                    ("ಬ್ಯಾಡಗಿ ಮೆಣಸಿನಕಾಯಿ {Byadgi Chilli}", 310, 420, 580),
                    ("ಶುದ್ಧ ಜೇನುತುಪ್ಪ {Honey}", 300, 480, 750),
                    ("ನಾಟಿ ಟೊಮೆಟೊ {Tomatoes}", 12, 22, 42),
                ],
                format_func=lambda x: x[0]
            )
            c_name, m_rate, f_rate, r_rate = crop_type

            harvest_qty = st.slider(
                "ನಿಮ್ಮ ಫಸಲಿನ ಪ್ರಮಾಣ (ಕ್ವಿಂಟಾಲ್‌ಗಳಲ್ಲಿ) {Harvest in Quintals}:",
                min_value=5, max_value=200, value=30, step=5
            )
            qty_kg = harvest_qty * 100

        with col_c2:
            mandi_total = qty_kg * m_rate
            direct_total = qty_kg * f_rate
            extra_profit = direct_total - mandi_total
            profit_pct = round((extra_profit / mandi_total) * 100, 1) if mandi_total > 0 else 0

            st.markdown(f"#### 💰 {c_name} — {'ಆದಾಯದ ಹೋಲಿಕೆ {Income Comparison}' if is_kn else 'Income Comparison'}:")
            st.write(f"- 📉 **{'ದಲ್ಲಾಳಿ ಮಂಡಿ ಆದಾಯ {Mandi Earning}:' if is_kn else 'Mandi Broker Earning:'}** `₹{mandi_total:,.0f}` (₹{m_rate}/kg)")
            st.write(f"- 🚀 **{'ಕೃಷಿನುಡಿ ನೇರ ಮಾರಾಟ ಆದಾಯ {F2C Earning}:' if is_kn else 'KrushiNudi Direct Earning:'}** `₹{direct_total:,.0f}` (₹{f_rate}/kg)")
            st.markdown("---")
            st.success(
                f"🌟 **{'ನಿಮ್ಮ ಕೈಸೇರುವ ನಿವ್ವಳ ಹೆಚ್ಚುವರಿ ಲಾಭ {Net Extra Profit}:' if is_kn else 'Net Extra Profit directly into your bank:'}**\n\n"
                f"### +₹{extra_profit:,.0f} (+{profit_pct}% {'ಹೆಚ್ಚು ಲಾಭ' if is_kn else 'Extra Margin'})"
            )

# ==============================================================================
# TAB 4: DIRECT TRADE FAIR PRACTICE GUIDELINES
# ==============================================================================
with tab_rules:
    st.markdown("### 🛡️ " + ("ಸುರಕ್ಷಿತ ಮತ್ತು ನ್ಯಾಯಯುತ ನೇರ ವ್ಯಾಪಾರದ ಮಾರ್ಗಸೂಚಿಗಳು" if is_kn else "Fair Trade Direct Purchase Guidelines"))
    with st.container(border=True):
        st.markdown("#### 👥 " + ("ಗ್ರಾಹಕರಿಗೆ ಸಲಹೆಗಳು {Tips for Buyers}:" if is_kn else "Tips for Buyers:"))
        st.write(
            "1. **ಗುಣಮಟ್ಟ ಪರಿಶೀಲನೆ:** ದೊಡ್ಡ ಪ್ರಮಾಣದ ಧಾನ್ಯಗಳನ್ನು ಆರ್ಡರ್ ಮಾಡುವ ಮುನ್ನ ಸ್ಯಾಂಪಲ್ (ಮಾದರಿ) ಫೋಟೋ ಅಥವಾ ವೀಡಿಯೋ ಕೇಳಿ ಖಚಿತಪಡಿಸಿಕೊಳ್ಳಿ.\n"
            "2. **ಪಾವತಿ ಭದ್ರತೆ:** ಮುಂಗಡ ಪೂರ್ಣ ಪಾವತಿಗಿಂತ ಭಾಗಶಃ ಮುಂಗಡ ಹಾಗೂ ಡೆಲಿವರಿ ನಂತರ ಬಾಕಿ UPI ಮೂಲಕ ಪಾವತಿಸುವುದು ಸೂಕ್ತ.\n"
            "3. **ಸಾರಿಗೆ ವ್ಯವಸ್ಥೆ:** ಕರ್ನಾಟಕದೊಳಗೆ KSRTC ಲಾಜಿಸ್ಟಿಕ್ಸ್ (KSRTC Logistics / Parcel Service) ಅಥವಾ ಸ್ಥಳೀಯ ಸರಕು ಆಟೋಗಳ ಮೂಲಕ ಅತಿ ಕಡಿಮೆ ವೆಚ್ಚದಲ್ಲಿ ನೇರವಾಗಿ ಪಾರ್ಸೆಲ್ ಪಡೆಯಬಹುದು."
            if is_kn else
            "1. **Quality Check:** Request clear photos or video samples of the produce bags before dispatch.\n"
            "2. **Secure Payments:** Transact directly with the farmer via UPI (Google Pay, PhonePe) or direct bank transfer upon dispatch slip confirmation.\n"
            "3. **Affordable Transport:** Utilize KSRTC Cargo Logistics or local rural transport operators for economical doorstep parcel delivery across Karnataka."
        )

    with st.container(border=True):
        st.markdown("#### 🌾 " + ("ರೈತರಿಗೆ ಸಲಹೆಗಳು {Tips for Farmers}:" if is_kn else "Tips for Farmers:"))
        st.write(
            "1. **ಸಮಗ್ರ ತೂಕ ಮತ್ತು ಶುದ್ಧತೆ:** ಕಲ್ಲು-ಮಣ್ಣು ರಹಿತವಾಗಿ ಕ್ಲೀನ್ ಮಾಡಿದ ಧಾನ್ಯಗಳನ್ನು ಬಲವಾದ ಚೀಲಗಳಲ್ಲಿ ಪ್ಯಾಕ್ ಮಾಡಿ.\n"
            "2. **ಪ್ರಾಮಾಣಿಕ ಬೆಲೆ:** ನಗರದ ಸೂಪರ್‌ಮಾರ್ಕೆಟ್‌ಗಿಂತ 20-30% ಕಡಿಮೆ ಬೆಲೆ ನಿಗದಿಪಡಿಸಿದರೆ ಗ್ರಾಹಕರು ನಿರಂತರವಾಗಿ ನಿಮ್ಮಿಂದಲೇ ಖರೀದಿಸುತ್ತಾರೆ.\n"
            "3. **ಗ್ರಾಹಕರ ವಿಶ್ವಾಸ:** ಪ್ರತಿ ಚೀಲದ ಮೇಲೂ ನಿಮ್ಮ ಜಮೀನಿನ ಹೆಸರು ಮತ್ತು ಮೊಬೈಲ್ ನಂಬರ್ ಹಾಕಿ, ಶಾಶ್ವತ ಗ್ರಾಹಕ ಬಳಗವನ್ನು ಬೆಳೆಸಿಕೊಳ್ಳಿ."
            if is_kn else
            "1. **Cleaning & Grading:** Ensure grains and produce are clean, graded, and packed in moisture-resistant bags.\n"
            "2. **Competitive Farm-Gate Pricing:** Set prices 20-30% below retail store rates to win permanent repeating customers.\n"
            "3. **Farmer Brand Identity:** Include your farm name and phone number on each delivery box/bag to build your own direct farm brand."
        )

ui.feedback_box()
st.markdown("---")
footer_str = (
    "© 2026 ಕೃಷಿನುಡಿ · ಅಭಿಷೇಕ್ ಹಿಟಬುತ್ತಿ. ರೈತರಿಂದ ಗ್ರಾಹಕರಿಗೆ ನೇರ ಕೃಷಿ ಕ್ರಾಂತಿ. ಎಲ್ಲ ಹಕ್ಕುಗಳನ್ನು ಕಾಯ್ದಿರಿಸಲಾಗಿದೆ."
    if is_kn else
    "© 2026 KrushiNudi · Abhishek Hitabutti. Direct Farm-to-Consumer Revolution. All rights reserved."
)
st.caption(footer_str)

