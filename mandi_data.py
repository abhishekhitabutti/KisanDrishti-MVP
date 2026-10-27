"""
KrushiNudi APMC Mandi Market Rates, Historical Trends & Best-Price Selling Centers.
Author: Abhishek Hitabutti
Copyright: © 2026 Abhishek Hitabutti. All rights reserved.

Comprehensive market intelligence for Karnataka farmers:
- Real-time modal, min, max, 30-day average, and MSP rates across 22 crops.
- 30-day historical price points and 14-day predictive trends.
- Actionable AI/expert selling verdicts (Sell Now vs Hold vs MSP Depot).
- Verified directory of MSP Procurement Centers, APMC Yards, FPOs & Certified Processors.
- District and crop filtering with 'Highest Rate First' sorting.
"""

from datetime import datetime, timedelta

# ==============================================================================
# 1. COMPREHENSIVE KARNATAKA CROPS MARKET INTELLIGENCE
# ==============================================================================

CROPS_MARKET_DATA = {
    "paddy": {
        "id": "paddy",
        "name_kn": "ಭತ್ತ / ಅಕ್ಕಿ (ಸೋನಾ ಮಸೂರಿ)",
        "name_en": "Paddy / Rice (Sona Masoori)",
        "category": "grains",
        "unit": "₹ / ಕ್ವಿಂಟಾಲ್",
        "today_modal": 2580,
        "min_price": 2350,
        "max_price": 2750,
        "avg_30d": 2470,
        "msp": 2320,
        "trend": "up",
        "pct_change": "+4.4%",
        "verdict_type": "hold",
        "verdict_kn": "10-15 ದಿನ ದಾಸ್ತಾನು ಮಾಡಿ {Hold & Wait}",
        "verdict_en": "Hold for 10-15 days. Expected gain: +₹120-180/qtl due to festive mill demand.",
        "forecast_reason_kn": "ದೀಪಾವಳಿ ಮತ್ತು ಹಬ್ಬದ ಋತುವಿನ ಹಿನ್ನೆಲೆಯಲ್ಲಿ ಅಕ್ಕಿ ಗಿರಣಿಗಳ ಖರೀದಿ ಹೆಚ್ಚುತ್ತಿದೆ. ಮುಂದಿನ 2 ವಾರಗಳಲ್ಲಿ ಬೆಲೆ ₹2,700 ದಾಟುವ ನಿರೀಕ್ಷೆಯಿದೆ.",
        "forecast_reason_en": "Rice mills in Raichur and Gangavathi are actively stocking up ahead of festive demand; prices expected to touch ₹2,700/qtl.",
        "target_14d": 2710,
        "base_history_offset": 2420,
        "trend_slope": 5.5,
    },
    "ragi": {
        "id": "ragi",
        "name_kn": "ರಾಗಿ (Finger Millet)",
        "name_en": "Finger Millet (Ragi)",
        "category": "grains",
        "unit": "₹ / ಕ್ವಿಂಟಾಲ್",
        "today_modal": 4350,
        "min_price": 4100,
        "max_price": 4550,
        "avg_30d": 4190,
        "msp": 4290,
        "trend": "up",
        "pct_change": "+3.8%",
        "verdict_type": "hold",
        "verdict_kn": "10-15 ದಿನ ದಾಸ್ತಾನು ಮಾಡಿ {Hold & Wait}",
        "verdict_en": "Hold for 10-15 days. Health food processing demand is surging.",
        "forecast_reason_kn": "ಬೆಂಗಳೂರು, ಮೈಸೂರು ನಗರಗಳಲ್ಲಿ ಸಿರಿಧಾನ್ಯ ಉತ್ಪನ್ನಗಳ ಬೇಡಿಕೆ ಗರಿಷ್ಠ ಮಟ್ಟದಲ್ಲಿದೆ. ಮುಕ್ತ ಮಾರುಕಟ್ಟೆ ದರವು ಸರ್ಕಾರಿ MSP ಗಿಂತ ₹150-250 ಹೆಚ್ಚಾಗಿದೆ.",
        "forecast_reason_en": "High urban demand for millet flour and breakfast mixes. Open market rates are comfortably above government MSP.",
        "target_14d": 4480,
        "base_history_offset": 4120,
        "trend_slope": 8.0,
    },
    "maize": {
        "id": "maize",
        "name_kn": "ಮೆಕ್ಕೆಜೋಳ (Maize)",
        "name_en": "Maize (Corn)",
        "category": "grains",
        "unit": "₹ / ಕ್ವಿಂಟಾಲ್",
        "today_modal": 2340,
        "min_price": 2180,
        "max_price": 2450,
        "avg_30d": 2210,
        "msp": 2225,
        "trend": "up",
        "pct_change": "+5.9%",
        "verdict_type": "sell_now",
        "verdict_kn": "ಈಗಲೇ ಮಾರಾಟ ಮಾಡಿ {Sell Now}",
        "verdict_en": "Sell current stock now. New Kharif arrivals will peak in 2 weeks.",
        "forecast_reason_kn": "ಕೋಳಿ ಆಹಾರ ಮತ್ತು ಪಿಷ್ಟ (Starch) ಕಾರ್ಖಾನೆಗಳಿಂದ ಉತ್ತಮ ಖರೀದಿ ಇದೆ. ನವೆಂಬರ್ ಮೊದಲ ವಾರದಲ್ಲಿ ಹೊಸ ಬೆಳೆ ಒಳಹರಿವು ಹೆಚ್ಚಿ ದರ ಇಳಿಯಬಹುದು.",
        "forecast_reason_en": "Strong poultry feed demand in Davanagere and Haveri; take profit now before peak harvesting arrivals bring rates down.",
        "target_14d": 2280,
        "base_history_offset": 2180,
        "trend_slope": 5.2,
    },
    "tur": {
        "id": "tur",
        "name_kn": "ತೊಗರಿ (Red Gram / Pigeon Pea)",
        "name_en": "Red Gram / Tur (Pigeon Pea)",
        "category": "pulses",
        "unit": "₹ / ಕ್ವಿಂಟಾಲ್",
        "today_modal": 10600,
        "min_price": 9900,
        "max_price": 11200,
        "avg_30d": 10050,
        "msp": 7550,
        "trend": "up",
        "pct_change": "+5.5%",
        "verdict_type": "sell_now",
        "verdict_kn": "ಈಗಲೇ ಮಾರಾಟ ಮಾಡಿ {Sell Now}",
        "verdict_en": "Sell at current peak prices. Massive +₹3,050 premium over MSP!",
        "forecast_reason_kn": "ಕಲಬುರಗಿ, ಯಾದಗಿರಿ ಮಾರುಕಟ್ಟೆಯಲ್ಲಿ ತೊಗರಿ ದರ ಐತಿಹಾಸಿಕ ಗರಿಷ್ಠ ಮಟ್ಟದಲ್ಲಿದೆ. ಸರ್ಕಾರಿ MSP (₹7,550) ಗಿಂತ ₹3,000 ಅಧಿಕ ಲಾಭ ಪಡೆಯುವ ಸದವಕಾಶ.",
        "forecast_reason_en": "Record peak prices in Kalaburagi market. Phenomenal opportunity to realize 40% margin over government MSP.",
        "target_14d": 10450,
        "base_history_offset": 9800,
        "trend_slope": 28.0,
    },
    "bengal_gram": {
        "id": "bengal_gram",
        "name_kn": "ಕಡಲೆ (Bengal Gram / Chana)",
        "name_en": "Bengal Gram / Chana",
        "category": "pulses",
        "unit": "₹ / ಕ್ವಿಂಟಾಲ್",
        "today_modal": 6550,
        "min_price": 6200,
        "max_price": 6800,
        "avg_30d": 6320,
        "msp": 5650,
        "trend": "up",
        "pct_change": "+3.6%",
        "verdict_type": "hold",
        "verdict_kn": "10-15 ದಿನ ದಾಸ್ತಾನು ಮಾಡಿ {Hold & Wait}",
        "verdict_en": "Hold for 10-15 days. Festive besan mill demand will raise rates.",
        "forecast_reason_kn": "ಗದಗ ಮತ್ತು ವಿಜಯಪುರ ಮಾರುಕಟ್ಟೆಗಳಲ್ಲಿ ದಾಲ್ ಮಿಲ್‌ಗಳ ಖರೀದಿ ಬಿರುಸಾಗಿದೆ. ದರಗಳು ₹6,700 ವರೆಗೆ ಮುಟ್ಟುವ ಸಾಧ್ಯತೆಯಿದೆ.",
        "forecast_reason_en": "Dal mills across Gadag and Bagalkote actively buying for sweets manufacture. Target ₹6,700/qtl.",
        "target_14d": 6720,
        "base_history_offset": 6250,
        "trend_slope": 10.0,
    },
    "cotton": {
        "id": "cotton",
        "name_kn": "ಹತ್ತಿ (Cotton - DCH/Bunny)",
        "name_en": "Cotton (Long Staple)",
        "category": "commercial",
        "unit": "₹ / ಕ್ವಿಂಟಾಲ್",
        "today_modal": 7750,
        "min_price": 7350,
        "max_price": 8100,
        "avg_30d": 7480,
        "msp": 7521,
        "trend": "up",
        "pct_change": "+3.6%",
        "verdict_type": "sell_now",
        "verdict_kn": "ಈಗಲೇ ಮಾರಾಟ ಮಾಡಿ {Sell Now}",
        "verdict_en": "Sell top quality bales now. CCI buying will anchor market prices.",
        "forecast_reason_kn": "ರಾಯಚೂರು ಮತ್ತು ಬಳ್ಳಾರಿ ಜಿನ್ನಿಂಗ್ ಮಿಲ್‌ಗಳಿಂದ ಉತ್ತಮ ಬೇಡಿಕೆ. ತೇವಾಂಶ 8-10% ಒಳಗೆ ಇದ್ದರೆ ಗರಿಷ್ಠ ₹8,000 ದರ ಸಿಗಲಿದೆ.",
        "forecast_reason_en": "Ginning mills in Raichur and Ballari actively purchasing clean dry lots with moisture below 10%.",
        "target_14d": 7690,
        "base_history_offset": 7400,
        "trend_slope": 12.0,
    },
    "byadgi_chilli": {
        "id": "byadgi_chilli",
        "name_kn": "ಬ್ಯಾಡಗಿ ಮೆಣಸಿನಕಾಯಿ (Byadgi Chilli - KDL/Dabbi)",
        "name_en": "Byadgi Dry Chilli (KDL/Dabbi)",
        "category": "spices",
        "unit": "₹ / ಕ್ವಿಂಟಾಲ್",
        "today_modal": 39500,
        "min_price": 32000,
        "max_price": 48000,
        "avg_30d": 37200,
        "msp": 0,
        "trend": "up",
        "pct_change": "+6.2%",
        "verdict_type": "hold",
        "verdict_kn": "10-15 ದಿನ ದಾಸ್ತಾನು ಮಾಡಿ {Hold & Wait}",
        "verdict_en": "Hold deep red lots. Oleoresin export buyers offering heavy premiums.",
        "forecast_reason_kn": "ಬ್ಯಾಡಗಿ ಎಪಿಎಂಸಿಯಲ್ಲಿ ಅಂತರರಾಷ್ಟ್ರೀಯ ಮಸಾಲಾ ರಫ್ತುದಾರರು ಹಾಗೂ ಓಲಿಯೋರೆಸಿನ್ ಕಂಪನಿಗಳಿಂದ ಭಾರಿ ಪೈಪೋಟಿ. ಗುಣಮಟ್ಟದ ಡಬ್ಬಿ ತಳಿಗೆ ₹45,000+ ದರ ನಿರೀಕ್ಷೆ.",
        "forecast_reason_en": "Intense bidding by oleoresin extraction units and spice exporters in Byadgi yard. Premium deep red lots crossing ₹45,000/qtl.",
        "target_14d": 41500,
        "base_history_offset": 36500,
        "trend_slope": 100.0,
    },
    "green_chilli": {
        "id": "green_chilli",
        "name_kn": "ಹಸಿ ಮೆಣಸಿನಕಾಯಿ (Green Chilli)",
        "name_en": "Green Fresh Chilli",
        "category": "vegetables",
        "unit": "₹ / ಕ್ವಿಂಟಾಲ್",
        "today_modal": 3400,
        "min_price": 2800,
        "max_price": 3900,
        "avg_30d": 3780,
        "msp": 0,
        "trend": "down",
        "pct_change": "-10.1%",
        "verdict_type": "sell_now",
        "verdict_kn": "ತಕ್ಷಣ ಮಾರಾಟ ಮಾಡಿ {Sell Immediately}",
        "verdict_en": "Perishable crop. Harvest and sell without holding.",
        "forecast_reason_kn": "ಹಾವೇರಿ ಮತ್ತು ಬೆಳಗಾವಿ ಜಿಲ್ಲೆಗಳಿಂದ ಹೆಚ್ಚಿನ ಪ್ರಮಾಣದಲ್ಲಿ ಮಾರುಕಟ್ಟೆಗೆ ಬರುತ್ತಿರುವುದರಿಂದ ದರ ಇಳಿಕೆಯಾಗುತ್ತಿದೆ. ಕೊಯ್ಲು ಮಾಡಿ ತಕ್ಷಣ ಮಾರಾಟ ಮಾಡಿ.",
        "forecast_reason_en": "Fresh supply surge from Haveri and Belagavi. Perishable commodity, liquidate harvested batches immediately.",
        "target_14d": 3200,
        "base_history_offset": 3850,
        "trend_slope": -15.0,
    },
    "onion": {
        "id": "onion",
        "name_kn": "ಈರುಳ್ಳಿ (Onion - Bellary / Bangalore Rose)",
        "name_en": "Onion (Bellary / Bangalore Rose)",
        "category": "vegetables",
        "unit": "₹ / ಕ್ವಿಂಟಾಲ್",
        "today_modal": 2850,
        "min_price": 2200,
        "max_price": 3400,
        "avg_30d": 3250,
        "msp": 0,
        "trend": "down",
        "pct_change": "-12.3%",
        "verdict_type": "hold",
        "verdict_kn": "ಒಣಗಿಸಿ ದಾಸ್ತಾನು ಮಾಡಿ {Dry & Store}",
        "verdict_en": "Solar dry and store properly. Prices will rebound in December.",
        "forecast_reason_kn": "ಚಿತ್ರದುರ್ಗ ಮತ್ತು ಗದಗದಲ್ಲಿ ಹೊಸ ಬೆಳೆ ಕೊಯ್ಲು ಆರಂಭವಾದ್ದರಿಂದ ಮಾರುಕಟ್ಟೆ ತಾತ್ಕಾಲಿಕವಾಗಿ ಕುಸಿದಿದೆ. ಸರಿಯಾಗಿ ಕ್ಯೂರಿಂಗ್ ಮಾಡಿ 3 ವಾರ ದಾಸ್ತಾನು ಮಾಡಿದರೆ ₹3,500+ ದರ ಸಿಗಲಿದೆ.",
        "forecast_reason_en": "Temporary arrival glut from Chitradurga Kharif harvest. Cure properly and store; prices will climb to ₹3,500 in 3-4 weeks.",
        "target_14d": 3150,
        "base_history_offset": 3350,
        "trend_slope": -16.0,
    },
    "tomato": {
        "id": "tomato",
        "name_kn": "ಟೊಮೆಟೊ (Tomato - Hybrid / Desi)",
        "name_en": "Tomato (Hybrid / Desi)",
        "category": "vegetables",
        "unit": "₹ / ಕ್ವಿಂಟಾಲ್",
        "today_modal": 1850,
        "min_price": 1400,
        "max_price": 2250,
        "avg_30d": 1520,
        "msp": 0,
        "trend": "up",
        "pct_change": "+21.7%",
        "verdict_type": "sell_now",
        "verdict_kn": "ಈಗಲೇ ಮಾರಾಟ ಮಾಡಿ {Sell Fresh Today}",
        "verdict_en": "Good price surge in Kolar & Madanapalle. Sell high-grade crates today.",
        "forecast_reason_kn": "ಕೋಲಾರ ಎಪಿಎಂಸಿಯಲ್ಲಿ ಹೊರರಾಜ್ಯಗಳ (ತಮಿಳುನಾಡು, ಮಹಾರಾಷ್ಟ್ರ) ವ್ಯಾಪಾರಿಗಳು ಹೆಚ್ಚಿನ ಪ್ರಮಾಣದಲ್ಲಿ ಖರೀದಿಸುತ್ತಿದ್ದು, ಪೆಟ್ಟಿಗೆಗೆ ₹450-550 ವರೆಗೆ ಸಿಗುತ್ತಿದೆ.",
        "forecast_reason_en": "Strong buying interest from Tamil Nadu and Andhra wholesale traders in Kolar APMC. Realize profits on current flushes.",
        "target_14d": 1780,
        "base_history_offset": 1450,
        "trend_slope": 14.0,
    },
    "arecanut": {
        "id": "arecanut",
        "name_kn": "ಅಡಿಕೆ (Arecanut - Rashi / Chali)",
        "name_en": "Arecanut / Betelnut (Rashi / Chali)",
        "category": "plantation",
        "unit": "₹ / ಕ್ವಿಂಟಾಲ್",
        "today_modal": 54500,
        "min_price": 49000,
        "max_price": 58500,
        "avg_30d": 53200,
        "msp": 0,
        "trend": "up",
        "pct_change": "+2.4%",
        "verdict_type": "hold",
        "verdict_kn": "ಕ್ಯಾಂಪ್ಕೋ / TSS ನಲ್ಲಿ ದಾಸ್ತಾನು ಮಾಡಿ {Hold in CAMPCO/TSS}",
        "verdict_en": "Hold dry lots in CAMPCO warehouse. Steady northward trend.",
        "forecast_reason_kn": "ಶಿವಮೊಗ್ಗ ಮತ್ತು ಸಿರ್ಸಿ ಮಾರುಕಟ್ಟೆಗಳಲ್ಲಿ ಉತ್ತರ ಭಾರತದ ಪಾನ್ ಮಸಾಲಾ ಕಂಪನಿಗಳ ಖರೀದಿ ಸ್ಥಿರವಾಗಿದೆ. ಕ್ಯಾಂಪ್ಕೋ ಉಗ್ರಾಣದಲ್ಲಿ ದಾಸ್ತಾನು ಇಟ್ಟು ಮುಂಗಡ ಸಾಲ ಪಡೆಯಬಹುದು.",
        "forecast_reason_en": "Consistent demand in Shivamogga, Sagar, and Sirsi from North Indian industrial buyers. Store in cooperative warehouses to capture ₹56,000+.",
        "target_14d": 55800,
        "base_history_offset": 52800,
        "trend_slope": 60.0,
    },
    "coconut": {
        "id": "coconut",
        "name_kn": "ತೆಂಗಿನಕಾಯಿ / ಕೊಬ್ಬರಿ (Coconut & Copra)",
        "name_en": "Coconut (per 1000 nuts) / Milling Copra",
        "category": "plantation",
        "unit": "₹ / 1,000 ಕಾಯಿ",
        "today_modal": 28500,
        "min_price": 25000,
        "max_price": 32000,
        "avg_30d": 26800,
        "msp": 12000,
        "trend": "up",
        "pct_change": "+6.3%",
        "verdict_type": "sell_now",
        "verdict_kn": "ಈಗಲೇ ಮಾರಾಟ ಮಾಡಿ {Sell Now}",
        "verdict_en": "Prices are at a strong 12-month high in Maddur & Tiptur.",
        "forecast_reason_kn": "ಮದ್ದೂರು ಎಳನೀರು ಮಾರುಕಟ್ಟೆ ಹಾಗೂ ತಿಪಟೂರು ಕೊಬ್ಬರಿ ಮಾರುಕಟ್ಟೆಯಲ್ಲಿ ಹಬ್ಬದ ಬೇಡಿಕೆಯಿಂದಾಗಿ ದರ ₹28-32 ಪ್ರತಿ ಕಾಯಿಗೆ ಏರಿದೆ. ಉತ್ತಮ ಲಾಭ ಗಳಿಸಿ.",
        "forecast_reason_en": "Tiptur copra and Maddur tender coconut markets seeing 12-month peak prices ahead of festive rush. Excellent selling window.",
        "target_14d": 28200,
        "base_history_offset": 26400,
        "trend_slope": 70.0,
    },
    "groundnut": {
        "id": "groundnut",
        "name_kn": "ಕಡಲೆಕಾಯಿ (Groundnut / Peanut)",
        "name_en": "Groundnut with Shell",
        "category": "commercial",
        "unit": "₹ / ಕ್ವಿಂಟಾಲ್",
        "today_modal": 6950,
        "min_price": 6450,
        "max_price": 7400,
        "avg_30d": 6680,
        "msp": 6783,
        "trend": "up",
        "pct_change": "+4.0%",
        "verdict_type": "hold",
        "verdict_kn": "10-15 ದಿನ ದಾಸ್ತಾನು ಮಾಡಿ {Hold & Wait}",
        "verdict_en": "Hold dry pods. Edible oil mills in Challakere are bidding aggressively.",
        "forecast_reason_kn": "ಚಳ್ಳಕೆರೆ ಮತ್ತು ರಾಯಚೂರು ಎಣ್ಣೆ ಗಿರಣಿಗಳಿಂದ ಎಣ್ಣೆ ಅಂಶ ಹೆಚ್ಚಿರುವ ಶೇಂಗಾಕ್ಕೆ ಭಾರಿ ಬೇಡಿಕೆ. ಮುಂಬರುವ ವಾರಗಳಲ್ಲಿ ₹7,200 ತಲುಪುವ ನಿರೀಕ್ಷೆ.",
        "forecast_reason_en": "Oil extraction mills in Challakere 'Oil City' bidding competitively for high-oil TMV-2 pods.",
        "target_14d": 7180,
        "base_history_offset": 6620,
        "trend_slope": 11.0,
    },
    "soybean": {
        "id": "soybean",
        "name_kn": "ಸೋಯಾಬೀನ್ (Soybean)",
        "name_en": "Soybean",
        "category": "commercial",
        "unit": "₹ / ಕ್ವಿಂಟಾಲ್",
        "today_modal": 4720,
        "min_price": 4400,
        "max_price": 4950,
        "avg_30d": 4650,
        "msp": 4892,
        "trend": "down",
        "pct_change": "-3.5%",
        "verdict_type": "sell_msp",
        "verdict_kn": "ಸರ್ಕಾರಿ MSP ಖರೀದಿ ಕೇಂದ್ರಕ್ಕೆ ನೀಡಿ {Sell at Govt MSP Center}",
        "verdict_en": "Open market is below MSP! Sell at government KSCMF/NAFED depot for guaranteed ₹4,892.",
        "forecast_reason_kn": "ಮುಕ್ತ ಮಾರುಕಟ್ಟೆಯಲ್ಲಿ ಸೋಯಾಬೀನ್ ದರ ₹4,720 ಇದ್ದು, ಸರ್ಕಾರಿ ಕನಿಷ್ಠ ಬೆಂಬಲ ಬೆಲೆ ₹4,892 ಆಗಿದೆ. ಸರ್ಕಾರದ ಬೆಂಬಲ ಬೆಲೆ ಕೇಂದ್ರಕ್ಕೆ ನೋಂದಾಯಿಸಿ ಕ್ವಿಂಟಾಲಿಗೆ ₹172 ಹೆಚ್ಚುವರಿ ಲಾಭ ಪಡೆಯಿರಿ.",
        "forecast_reason_en": "Open mandi rate is trading at a discount to MSP (₹4,892). Register at local KSCMF purchase depot to secure guaranteed profits.",
        "target_14d": 4700,
        "base_history_offset": 4800,
        "trend_slope": -3.0,
    },
    "sugarcane": {
        "id": "sugarcane",
        "name_kn": "ಕಬ್ಬು (Sugarcane)",
        "name_en": "Sugarcane (Crushing Cane)",
        "category": "commercial",
        "unit": "₹ / ಟನ್ (FRP)",
        "today_modal": 3400,
        "min_price": 3250,
        "max_price": 3550,
        "avg_30d": 3380,
        "msp": 3400,
        "trend": "stable",
        "pct_change": "+0.6%",
        "verdict_type": "sell_now",
        "verdict_kn": "ಸಕ್ಕರೆ ಕಾರ್ಖಾನೆಗೆ ಸರಬರಾಜು ಮಾಡಿ {Deliver to Sugar Mill}",
        "verdict_en": "Send ripe cane to registered cooperative or private sugar factory.",
        "forecast_reason_kn": "ಕಬ್ಬು ನುರಿಸುವ ಹಂಗಾಮು ಚುರುಕಾಗಿದೆ. ಬೆಳಗಾವಿ, ಬಾಗಲಕೋಟೆ ಮತ್ತು ಮಂಡ್ಯ ಕಾರ್ಖಾನೆಗಳಲ್ಲಿ ನಿಗದಿತ FRP ದರ (₹3,400/ಟನ್) ನೀಡಲಾಗುತ್ತಿದೆ.",
        "forecast_reason_en": "Crushing season in full swing across Belagavi and Bagalkote. Deliver timely to maximize recovery and earn statutory FRP bonuses.",
        "target_14d": 3420,
        "base_history_offset": 3370,
        "trend_slope": 1.0,
    },
    "sunflower": {
        "id": "sunflower",
        "name_kn": "ಸೂರ್ಯಕಾಂತಿ (Sunflower Seed)",
        "name_en": "Sunflower Seed",
        "category": "commercial",
        "unit": "₹ / ಕ್ವಿಂಟಾಲ್",
        "today_modal": 6150,
        "min_price": 5800,
        "max_price": 6400,
        "avg_30d": 6020,
        "msp": 7280,
        "trend": "down",
        "pct_change": "-2.1%",
        "verdict_type": "sell_msp",
        "verdict_kn": "ಸರ್ಕಾರಿ MSP ಖರೀದಿ ಕೇಂದ್ರಕ್ಕೆ ನೀಡಿ {Sell at Govt MSP Center}",
        "verdict_en": "Huge +₹1,130 advantage at Govt MSP Center over open mandi!",
        "forecast_reason_kn": "ಮುಕ್ತ ಮಾರುಕಟ್ಟೆಯಲ್ಲಿ ₹6,150 ದರವಿದೆ. ಆದರೆ ಸರ್ಕಾರಿ ಬೆಂಬಲ ಬೆಲೆ ₹7,280 ಆಗಿದೆ. ರೈತರು ತಕ್ಷಣ ಹತ್ತಿರದ KSCMF ಖರೀದಿ ಕೇಂದ್ರಕ್ಕೆ ಹೋಗಿ ಹೆಸರು ನೋಂದಾಯಿಸಿಕೊಳ್ಳಬೇಕು.",
        "forecast_reason_en": "Massive price divergence. Government MSP is ₹7,280, offering over ₹1,100/qtl more than open private market. Prioritize MSP purchase centers.",
        "target_14d": 6120,
        "base_history_offset": 6250,
        "trend_slope": -4.0,
    },
    "jowar": {
        "id": "jowar",
        "name_kn": "ಬಿಳಿ ಜೋಳ (Jowar / Sorghum - Maldandi)",
        "name_en": "White Jowar / Sorghum (Maldandi)",
        "category": "grains",
        "unit": "₹ / ಕ್ವಿಂಟಾಲ್",
        "today_modal": 3750,
        "min_price": 3400,
        "max_price": 4100,
        "avg_30d": 3580,
        "msp": 3371,
        "trend": "up",
        "pct_change": "+4.7%",
        "verdict_type": "hold",
        "verdict_kn": "10-15 ದಿನ ದಾಸ್ತಾನು ಮಾಡಿ {Hold & Wait}",
        "verdict_en": "Hold premium Maldandi lots. Steady winter demand for roti.",
        "forecast_reason_kn": "ವಿಜಯಪುರ, ಬಾಗಲಕೋಟೆಯಲ್ಲಿ ಮಾಲ್ದಂಡಿ ಜೋಳಕ್ಕೆ ಚಳಿಗಾಲದ ಆರಂಭದಲ್ಲಿ ಬೇಡಿಕೆ ಹೆಚ್ಚಾಗುತ್ತಿದೆ. ಗುಣಮಟ್ಟದ ಧಾನ್ಯಕ್ಕೆ ₹4,000+ ದರ ಸಿಗುವ ನಿರೀಕ್ಷೆ.",
        "forecast_reason_en": "Rising winter consumption for premium Maldandi jowar in North Karnataka. Hold for ₹4,000+ price mark.",
        "target_14d": 3920,
        "base_history_offset": 3520,
        "trend_slope": 8.0,
    },
    "ginger": {
        "id": "ginger",
        "name_kn": "ಹಸಿ ಶುಂಠಿ (Fresh Ginger)",
        "name_en": "Fresh Ginger",
        "category": "spices",
        "unit": "₹ / 60 ಕೆಜಿ ಚೀಲ",
        "today_modal": 5200,
        "min_price": 4600,
        "max_price": 5800,
        "avg_30d": 4850,
        "msp": 0,
        "trend": "up",
        "pct_change": "+7.2%",
        "verdict_type": "sell_now",
        "verdict_kn": "ಈಗಲೇ ಮಾರಾಟ ಮಾಡಿ {Sell Now}",
        "verdict_en": "Excellent returns in Hassan, Kodagu and Shimoga. Liquidate current pickings.",
        "forecast_reason_kn": "ದೆಹಲಿ, ಮುಂಬೈ ಮಾರುಕಟ್ಟೆಗಳಿಂದ ಶುಂಠಿಗೆ ಅತ್ಯುತ್ತಮ ಬೇಡಿಕೆ. ಹಾಸನ, ಮಡಿಕೇರಿ ರೈತರಿಗೆ ಬಂಪರ್ ದರ ಸಿಗುತ್ತಿದೆ.",
        "forecast_reason_en": "High north-Indian demand fetching strong prices for Karnataka green ginger. Good time to liquidate.",
        "target_14d": 5350,
        "base_history_offset": 4750,
        "trend_slope": 15.0,
    },
    "black_pepper": {
        "id": "black_pepper",
        "name_kn": "ಕಾಳುಮೆಣಸು (Black Pepper - Garbled)",
        "name_en": "Black Pepper (Garbled)",
        "category": "spices",
        "unit": "₹ / ಕೆಜಿ",
        "today_modal": 660,
        "min_price": 620,
        "max_price": 710,
        "avg_30d": 635,
        "msp": 0,
        "trend": "up",
        "pct_change": "+3.9%",
        "verdict_type": "hold",
        "verdict_kn": "ದಾಸ್ತಾನು ಮಾಡಿ {Hold in Dry Storage}",
        "verdict_en": "Hold well-dried 550GL+ pepper. Exporters projecting ₹700/kg.",
        "forecast_reason_kn": "ಕೊಡಗು, ಚಿಕ್ಕಮಗಳೂರಿನಲ್ಲಿ ಕಾಳುಮೆಣಸಿನ ಜಾಗತಿಕ ಪೂರೈಕೆ ಕೊರತೆಯಿಂದ ದರ ಹೆಚ್ಚಾಗುತ್ತಿದೆ. ತೇವಾಂಶ 11% ಒಳಗೆ ಒಣಗಿಸಿಟ್ಟರೆ ₹700+ ಗ್ಯಾರಂಟಿ.",
        "forecast_reason_en": "Global supply squeeze in Vietnam and Indonesia lifting Indian black pepper. Keep moisture below 11% to command ₹700/kg.",
        "target_14d": 685,
        "base_history_offset": 630,
        "trend_slope": 1.2,
    },
    "cardamom": {
        "id": "cardamom",
        "name_kn": "ಏಲಕ್ಕಿ (Small Green Cardamom)",
        "name_en": "Small Green Cardamom (7-8mm)",
        "category": "spices",
        "unit": "₹ / ಕೆಜಿ",
        "today_modal": 2550,
        "min_price": 2200,
        "max_price": 2900,
        "avg_30d": 2380,
        "msp": 0,
        "trend": "up",
        "pct_change": "+7.1%",
        "verdict_type": "sell_now",
        "verdict_kn": "ಸ್ಪೈಸ್ ಬೋರ್ಡ್ ಹರಾಜಿನಲ್ಲಿ ಮಾರಾಟ ಮಾಡಿ {Sell via Spices Board Auction}",
        "verdict_en": "Spices Board auctions in Sakleshpur and Bodinayakanur yielding high prices.",
        "forecast_reason_kn": "ಹಬ್ಬದ ಋತುವಿನಲ್ಲಿ ಸಿಹಿ ತಿನಿಸುಗಳ ತಯಾರಿಕೆಗೆ ಭಾರಿ ಬೇಡಿಕೆ. ಸಕಲೇಶಪುರ ಮತ್ತು ಮೂಡಿಗೆರೆ ರೈತರು ಇ-ಹರಾಜಿನಲ್ಲಿ ಗರಿಷ್ಠ ಲಾಭ ಗಳಿಸಬಹುದು.",
        "forecast_reason_en": "Festive sweet manufacture spiking consumption. Sell via official Spices Board e-auctions to avoid broker deductions.",
        "target_14d": 2620,
        "base_history_offset": 2320,
        "trend_slope": 6.5,
    },
    "banana": {
        "id": "banana",
        "name_kn": "ಬಾಳೆಹಣ್ಣು (Yelakki / Robusta)",
        "name_en": "Banana (Yelakki / Robusta)",
        "category": "fruits",
        "unit": "₹ / ಕ್ವಿಂಟಾಲ್",
        "today_modal": 2300,
        "min_price": 1900,
        "max_price": 2650,
        "avg_30d": 2180,
        "msp": 0,
        "trend": "up",
        "pct_change": "+5.5%",
        "verdict_type": "sell_now",
        "verdict_kn": "ತಕ್ಷಣ ಮಾರಾಟ ಮಾಡಿ {Sell Ready Bunches}",
        "verdict_en": "Festive demand active in Bengaluru wholesale markets.",
        "forecast_reason_kn": "ನಂಜನಗೂಡು ಮತ್ತು ರಾಮನಗರ ಮಾರುಕಟ್ಟೆಯಲ್ಲಿ ಏಲಕ್ಕಿ ಬಾಳೆಗೆ ಉತ್ತಮ ಧಾರಣೆ. ಹಣ್ಣಾಗುವ ಮುನ್ನವೇ ಕೊಯ್ಲು ಮಾಡಿ ವ್ಯಾಪಾರಿಗಳಿಗೆ ತಲುಪಿಸಿ.",
        "forecast_reason_en": "Strong retail demand in Bengaluru and Mysuru. Harvest at 80% maturity and sell directly to wholesale buyers.",
        "target_14d": 2350,
        "base_history_offset": 2150,
        "trend_slope": 4.5,
    },
    "potato": {
        "id": "potato",
        "name_kn": "ಆಲೂಗಡ್ಡೆ (Potato - Table / Processing)",
        "name_en": "Potato (Hassan / Kolar Table Variety)",
        "category": "vegetables",
        "unit": "₹ / ಕ್ವಿಂಟಾಲ್",
        "today_modal": 1980,
        "min_price": 1650,
        "max_price": 2300,
        "avg_30d": 2150,
        "msp": 0,
        "trend": "down",
        "pct_change": "-7.9%",
        "verdict_type": "hold",
        "verdict_kn": "ಕೋಲ್ಡ್ ಸ್ಟೋರೇಜ್‌ನಲ್ಲಿ ದಾಸ್ತಾನು ಮಾಡಿ {Store in Cold Storage}",
        "verdict_en": "Local harvest is flooding mandis. Keep in cold storage for 4 weeks.",
        "forecast_reason_kn": "ಹಾಸನ ಮತ್ತು ಚಿಕ್ಕಬಳ್ಳಾಪುರದಲ್ಲಿ ಸ್ಥಳೀಯ ಕೊಯ್ಲು ಮುಕ್ತಾಯ ಹಂತದಲ್ಲಿದ್ದು ತಾತ್ಕಾಲಿಕ ಬೆಲೆ ಕುಸಿತವಾಗಿದೆ. ಕೋಲ್ಡ್ ಸ್ಟೋರೇಜ್‌ನಲ್ಲಿ ಇಟ್ಟರೆ ಡಿಸೆಂಬರ್‌ನಲ್ಲಿ ₹2,400+ ದರ ಸಿಗಲಿದೆ.",
        "forecast_reason_en": "Post-harvest supply surge in Hassan. Shift produce to licensed cold storage to sell at ₹2,400+ in December.",
        "target_14d": 2120,
        "base_history_offset": 2220,
        "trend_slope": -8.0,
    },
}


def generate_crop_history(crop_info):
    """Generate calibrated 30-day historical prices and 14-day forecasted prices."""
    base_price = crop_info["base_history_offset"]
    slope = crop_info["trend_slope"]
    today = datetime.now()

    # 30-day past prices
    history = []
    for i in range(30, 0, -1):
        dt = today - timedelta(days=i)
        day_index = 30 - i
        # smooth curve with realistic micro fluctuation
        fluctuation = (day_index % 3 - 1) * (slope * 0.4)
        price = round(base_price + (day_index * slope) + fluctuation)
        history.append({
            "date": dt.strftime("%Y-%m-%d"),
            "price": max(10, price),
            "label": dt.strftime("%d %b")
        })

    # Today's price
    history.append({
        "date": today.strftime("%Y-%m-%d"),
        "price": crop_info["today_modal"],
        "label": "ಇಂದು / Today"
    })

    # 14-day future prediction
    forecast = []
    current_modal = crop_info["today_modal"]
    target = crop_info["target_14d"]
    step = (target - current_modal) / 14.0

    for i in range(1, 15):
        dt = today + timedelta(days=i)
        f_price = round(current_modal + (step * i) + ((i % 2) * (slope * 0.2)))
        forecast.append({
            "date": dt.strftime("%Y-%m-%d"),
            "price": max(10, f_price),
            "label": dt.strftime("%d %b")
        })

    return history, forecast


# ==============================================================================
# 2. VERIFIED DIRECT SELLING CENTERS & PROCUREMENT HUBS IN KARNATAKA
# ==============================================================================

SELLING_CENTERS = [
    # --------------------------------------------------------------------------
    # 1. BAGALKOTE DISTRICT (ಬಾಗಲಕೋಟೆ)
    # --------------------------------------------------------------------------
    {
        "id": "bgk_apmc_main",
        "name_kn": "ಬಾಗಲಕೋಟೆ ಪ್ರಧಾನ ಎಪಿಎಂಸಿ ಪ್ರಾಂಗಣ & ಒಣದ್ರಾಕ್ಷಿ-ಮೆಕ್ಕೆಜೋಳ ಮಂಡಿ",
        "name_en": "Bagalkote Principal APMC Yard & Raisin Trading Complex",
        "category": "apmc",
        "district": "Bagalkote",
        "taluk": "Bagalkote",
        "address": "ನವನಗರ, ಸೆಕ್ಟರ್ 62, ಬಾಗಲಕೋಟೆ - 587103",
        "crops_accepted": ["maize", "jowar", "bengal_gram", "soybean", "sugarcane"],
        "rates": {
            "maize": 2350,
            "jowar": 3820,
            "bengal_gram": 6620,
            "soybean": 4760,
            "sugarcane": 3440
        },
        "premium_vs_local": "+₹150 - ₹220/ಕ್ವಿಂಟಾಲ್ ಸ್ಥಳೀಯ ದಲ್ಲಾಳಿಗಳಿಗಿಂತ ಹೆಚ್ಚು",
        "commission": "1.5% APMC ನಿಯಂತ್ರಿತ ಶುಲ್ಕ",
        "payment_mode": "ಇ-ನಾಮ್ RTGS / ಬ್ಯಾಂಕ್ ವರ್ಗಾವಣೆ (24 ಗಂಟೆ)",
        "weighing": "ಸರ್ಕಾರಿ ಮುದ್ರೆಯುಳ್ಳ ಡಿಜಿಟಲ್ ಧರ್ಮಕಾಂಟಾ",
        "facilities": ["ಇ-ನಾಮ್ ಆನ್‌ಲೈನ್ ಬಿಡ್ಡಿಂಗ್", "ಒಣದ್ರಾಕ್ಷಿ ಕೋಲ್ಡ್ ಸ್ಟೋರೇಜ್", "ಉಚಿತ 3 ದಿನ ದಾಸ್ತಾನು ಶೆಡ್", "ರೈತ ವಿಶ್ರಾಂತಿ ಗೃಹ"],
        "phone": "+91 8354 235410",
        "timings": "ಬೆಳಿಗ್ಗೆ 8:00 ರಿಂದ ಸಂಜೆ 5:30 (ಸೋಮ - ಶನಿ)",
        "maps_url": "https://maps.google.com/?q=APMC+Market+Navanagar+Bagalkote"
    },
    {
        "id": "bgk_jamkhandi_fpo",
        "name_kn": "ಜಮಖಂಡಿ ಕಬ್ಬು & ಎಣ್ಣೆಕಾಳು ಸಹಕಾರಿ ಸಂಸ್ಕರಣಾ ಖರೀದಿ ಕೇಂದ್ರ",
        "name_en": "Jamkhandi Cane & Oilseeds Farmers Cooperative Center",
        "category": "fpo",
        "district": "Bagalkote",
        "taluk": "Jamkhandi",
        "address": "ಮುಧೋಳ ರಸ್ತೆ, ಜಮಖಂಡಿ, ಬಾಗಲಕೋಟೆ - 587301",
        "crops_accepted": ["sugarcane", "soybean", "maize", "bengal_gram"],
        "rates": {
            "sugarcane": 3480,
            "soybean": 4790,
            "maize": 2360,
            "bengal_gram": 6650
        },
        "premium_vs_local": "+₹180/ಕ್ವಿಂಟಾಲ್ ನೇರ ಸಹಕಾರಿ ಖರೀದಿ ಬೋನಸ್",
        "commission": "0% (ಸಹಕಾರಿ ಸದಸ್ಯತ್ವ ಶೂನ್ಯ ಕಮಿಷನ್)",
        "payment_mode": "ಸ್ಥಳದಲ್ಲೇ DBT / ಬ್ಯಾಂಕ್ ವರ್ಗಾವಣೆ",
        "weighing": "ಪಾರದರ್ಶಕ ಎಲೆಕ್ಟ್ರಾನಿಕ್ ತೂಕ",
        "facilities": ["ಶೂನ್ಯ ಕಮಿಷನ್", "ಸಹಕಾರಿ ಬೋನಸ್", "ಕಬ್ಬಿನ ತೂಕದ ತ್ವರಿತ ರಶೀದಿ"],
        "phone": "+91 8353 220145",
        "timings": "ಬೆಳಿಗ್ಗೆ 8:30 ರಿಂದ ಸಂಜೆ 5:00",
        "maps_url": "https://maps.google.com/?q=Jamkhandi+Farmers+Cooperative+Bagalkote"
    },

    # --------------------------------------------------------------------------
    # 2. BALLARI DISTRICT (ಬಳ್ಳಾರಿ)
    # --------------------------------------------------------------------------
    {
        "id": "bly_apmc_main",
        "name_kn": "ಬಳ್ಳಾರಿ ಪ್ರಧಾನ ಎಪಿಎಂಸಿ ಪ್ರಾಂಗಣ & ಹತ್ತಿ-ಮೆಕ್ಕೆಜೋಳ ಮಾರುಕಟ್ಟೆ",
        "name_en": "Ballari Principal APMC Yard & Cotton Market",
        "category": "apmc",
        "district": "Ballari",
        "taluk": "Ballari",
        "address": "ಕೊಳಗಳ ರಸ್ತೆ, ಬಳ್ಳಾರಿ - 583104",
        "crops_accepted": ["cotton", "maize", "paddy", "green_chilli", "sunflower"],
        "rates": {
            "cotton": 7820,
            "maize": 2360,
            "paddy": 2590,
            "green_chilli": 3520,
            "sunflower": 6240
        },
        "premium_vs_local": "+₹200 - ₹300 ಜಿನ್ನಿಂಗ್ ಗಿರಣಿಗಳ ನೇರ ಬಿಡ್ಡಿಂಗ್",
        "commission": "1.5% APMC ನಿಯಂತ್ರಿತ",
        "payment_mode": "ಇ-ನಾಮ್ RTGS / ಬ್ಯಾಂಕ್ ವರ್ಗಾವಣೆ",
        "weighing": "ಕಂಪ್ಯೂಟರೀಕೃತ ಧರ್ಮಕಾಂಟಾ",
        "facilities": ["ಹತ್ತಿ ತೇವಾಂಶ ಪರೀಕ್ಷಾ ಲ್ಯಾಬ್", "ಇ-ನಾಮ್ ಹರಾಜು", "ಬೃಹತ್ ಗೋದಾಮು ಶೆಡ್"],
        "phone": "+91 8392 272180",
        "timings": "ಬೆಳಿಗ್ಗೆ 8:00 ರಿಂದ ಸಂಜೆ 6:00",
        "maps_url": "https://maps.google.com/?q=APMC+Market+Yard+Ballari"
    },
    {
        "id": "bly_siruguppa_rice",
        "name_kn": "ಸಿರುಗುಪ್ಪ ಭತ್ತದ ಗಿರಣಿಗಳ ಸಗಟು ಖರೀದಿ ಕೇಂದ್ರ (ಕರ್ನಾಟಕದ ಭತ್ತದ ಕಣಜ)",
        "name_en": "Siruguppa Mega Rice Millers & Paddy Wholesale Hub",
        "category": "processor",
        "district": "Ballari",
        "taluk": "Siruguppa",
        "address": "ಸಿಂಧನೂರು ಮುಖ್ಯ ರಸ್ತೆ, ಸಿರುಗುಪ್ಪ, ಬಳ್ಳಾರಿ - 583121",
        "crops_accepted": ["paddy", "maize", "cotton"],
        "rates": {
            "paddy": 2640,
            "maize": 2370,
            "cotton": 7850
        },
        "premium_vs_local": "+₹160 ಸೋನಾ ಮಸೂರಿ ಭತ್ತಕ್ಕೆ ರಾಜ್ಯದಲ್ಲೇ ಅತ್ಯಧಿಕ ದರ",
        "commission": "0% (ಮಿಲ್ ನೇರ ಖರೀದಿ - ಮಧ್ಯವರ್ತಿ ರಹಿತ)",
        "payment_mode": "ಸ್ಥಳದಲ್ಲೇ RTGS / ಚೆಕ್ ಪಾವತಿ (24 ಗಂಟೆ)",
        "weighing": "100% ಡಿಜಿಟಲ್ ವೇಯಿಂಗ್ ಬ್ರಿಡ್ಜ್",
        "facilities": ["ನೇರ ಗಿರಣಿ ದರ", "ಸ್ಪಾಟ್ ಪೇಮೆಂಟ್", "ವೇಗದ ಅನ್‌ಲೋಡಿಂಗ್ ಸೌಲಭ್ಯ"],
        "phone": "+91 8396 222045",
        "timings": "ಬೆಳಿಗ್ಗೆ 8:00 ರಿಂದ ಸಂಜೆ 6:30",
        "maps_url": "https://maps.google.com/?q=Siruguppa+Rice+Mills+Ballari"
    },

    # --------------------------------------------------------------------------
    # 3. BELAGAVI DISTRICT (ಬೆಳಗಾವಿ)
    # --------------------------------------------------------------------------
    {
        "id": "belagavi_khasbag_apmc",
        "name_kn": "ಬೆಳಗಾವಿ ಖಾಸ್‌ಬಾಗ್ ಪ್ರಧಾನ ಎಪಿಎಂಸಿ ಪ್ರಾಂಗಣ & ಸಗಟು ಮಂಡಿ",
        "name_en": "Belagavi Khasbag Principal APMC Market Yard",
        "category": "apmc",
        "district": "Belagavi",
        "taluk": "Belagavi",
        "address": "ಖಾಸ್‌ಬಾಗ್, ಹಳೆಯ ಪುಣೆ-ಬೆಂಗಳೂರು ರಸ್ತೆ, ಬೆಳಗಾವಿ - 590003",
        "crops_accepted": ["onion", "maize", "soybean", "sugarcane", "potato", "green_chilli"],
        "rates": {
            "onion": 2980,
            "maize": 2350,
            "soybean": 4760,
            "sugarcane": 3420,
            "potato": 2020,
            "green_chilli": 3480
        },
        "premium_vs_local": "+₹200 ಗೋವಾ ಮತ್ತು ಮುಂಬೈ ವ್ಯಾಪಾರಿಗಳ ನೇರ ಖರೀದಿ",
        "commission": "1.5% APMC ನಿಯಂತ್ರಿತ",
        "payment_mode": "ಇ-ನಾಮ್ RTGS / ನಗದು ಪಾವತಿ",
        "weighing": "ಎಲೆಕ್ಟ್ರಾನಿಕ್ ಕಂಪ್ಯೂಟರೀಕೃತ ತೂಕ",
        "facilities": ["ಗೋವಾ, ಕೊಲ್ಹಾಪುರ ನೇರ ಸರಬರಾಜು", "ಬೃಹತ್ ಶೀತಲ ದಾಸ್ತಾನು", "ದೈನಂದಿನ ಹರಾಜು"],
        "phone": "+91 831 2420311",
        "timings": "ಬೆಳಿಗ್ಗೆ 7:00 ರಿಂದ ಸಂಜೆ 6:00",
        "maps_url": "https://maps.google.com/?q=APMC+Market+Yard+Khasbag+Belagavi"
    },
    {
        "id": "bailhongal_cotton_apmc",
        "name_kn": "ಬೈಲಹೊಂಗಲ ಹತ್ತಿ & ಎಣ್ಣೆಕಾಳು ಉಪ ಮಾರುಕಟ್ಟೆ ಪ್ರಾಂಗಣ",
        "name_en": "Bailhongal Cotton & Oilseeds Sub-Market Yard",
        "category": "apmc",
        "district": "Belagavi",
        "taluk": "Bailhongal",
        "address": "ಸವದತ್ತಿ ರಸ್ತೆ, ಬೈಲಹೊಂಗಲ, ಬೆಳಗಾವಿ - 591102",
        "crops_accepted": ["cotton", "soybean", "groundnut", "maize"],
        "rates": {
            "cotton": 7780,
            "soybean": 4740,
            "groundnut": 6980,
            "maize": 2320
        },
        "premium_vs_local": "+₹180 ಸ್ಥಳೀಯ ಹತ್ತಿ ಜಿನ್ನಿಂಗ್ ಮಿಲ್‌ಗಳಿಂದ ನೇರ ಸ್ಪರ್ಧೆ",
        "commission": "1.5% ನಿಯಂತ್ರಿತ",
        "payment_mode": "RTGS / ಚೆಕ್",
        "weighing": "ಡಿಜಿಟಲ್ ಧರ್ಮಕಾಂಟಾ",
        "facilities": ["ಹತ್ತಿ ತೇವಾಂಶ ಲ್ಯಾಬ್", "ಜಿನ್ನಿಂಗ್ ಕನೆಕ್ಟ್", "ಶೇಖರಣಾ ಗೋದಾಮು"],
        "phone": "+91 8288 233215",
        "timings": "ಬೆಳಿಗ್ಗೆ 8:30 ರಿಂದ ಸಂಜೆ 5:00",
        "maps_url": "https://maps.google.com/?q=APMC+Bailhongal"
    },

    # --------------------------------------------------------------------------
    # 4. BENGALURU RURAL DISTRICT (ಬೆಂಗಳೂರು ಗ್ರಾಮಾಂತರ)
    # --------------------------------------------------------------------------
    {
        "id": "blr_rural_doddaballapur",
        "name_kn": "ದೊಡ್ಡಬಳ್ಳಾಪುರ ಎಪಿಎಂಸಿ ಉಪ ಪ್ರಾಂಗಣ & ರಾಗಿ-ತರಕಾರಿ ಸಗಟು ಮಂಡಿ",
        "name_en": "Doddaballapura APMC Yard & Fresh Produce Terminal",
        "category": "apmc",
        "district": "Bengaluru Rural",
        "taluk": "Doddaballapura",
        "address": "ಡಿ-ಕ್ರಾಸ್, ದೊಡ್ಡಬಳ್ಳಾಪುರ - 561203",
        "crops_accepted": ["ragi", "tomato", "potato", "maize", "green_chilli"],
        "rates": {
            "ragi": 4380,
            "tomato": 1960,
            "potato": 2060,
            "maize": 2340,
            "green_chilli": 3520
        },
        "premium_vs_local": "+₹150 ರಾಜಧಾನಿ ಮಾರುಕಟ್ಟೆ ಸಾಮೀಪ್ಯದ ಅಧಿಕ ದರ",
        "commission": "1.5% APMC ನಿಯಂತ್ರಿತ",
        "payment_mode": "ಇ-ನಾಮ್ RTGS / UPI",
        "weighing": "ಎಲೆಕ್ಟ್ರಾನಿಕ್ ತಕ್ಕಡಿ",
        "facilities": ["ಬೆಂಗಳೂರು ನಗರ ನೇರ ಲಿಂಕ್", "ದೈನಂದಿನ ಹರಾಜು", "ಕ್ರೇಟ್ ವಿನಿಮಯ"],
        "phone": "+91 80 2762 2450",
        "timings": "ಬೆಳಿಗ್ಗೆ 6:30 ರಿಂದ ಸಂಜೆ 4:30",
        "maps_url": "https://maps.google.com/?q=APMC+Doddaballapur"
    },
    {
        "id": "blr_rural_hosakote",
        "name_kn": "ಹೊಸಕೋಟೆ ತರಕಾರಿ & ಧಾನ್ಯ ಸಗಟು ವ್ಯಾಪಾರ ಪ್ರಾಂಗಣ",
        "name_en": "Hosakote Agro-Produce Wholesale Hub",
        "category": "fpo",
        "district": "Bengaluru Rural",
        "taluk": "Hosakote",
        "address": "ರಾಷ್ಟ್ರೀಯ ಹೆದ್ದಾರಿ 75, ಹೊಸಕೋಟೆ - 562114",
        "crops_accepted": ["tomato", "green_chilli", "potato", "ragi", "banana"],
        "rates": {
            "tomato": 1980,
            "green_chilli": 3540,
            "potato": 2080,
            "ragi": 4390,
            "banana": 2380
        },
        "premium_vs_local": "+₹180 ಚೆನ್ನೈ-ಬೆಂಗಳೂರು ಕಾರಿಡಾರ್ ರಫ್ತು ದರ",
        "commission": "1% ಸಹಕಾರಿ ಶುಲ್ಕ",
        "payment_mode": "ಸ್ಥಳದಲ್ಲೇ ನಗದು / ಬ್ಯಾಂಕ್ ವರ್ಗಾವಣೆ",
        "weighing": "ಡಿಜಿಟಲ್ ವೇಯಿಂಗ್ ಸ್ಕೇಲ್",
        "facilities": ["ಅಂತರರಾಜ್ಯ ಲಾರಿ ಲೋಡಿಂಗ್", "ಕೋಲ್ಡ್ ರೂಮ್ ಸೌಲಭ್ಯ", "ಸ್ಪಾಟ್ ಕ್ಯಾಶ್"],
        "phone": "+91 80 2793 1120",
        "timings": "ಬೆಳಿಗ್ಗೆ 6:00 ರಿಂದ ಮಧ್ಯಾಹ್ನ 3:30",
        "maps_url": "https://maps.google.com/?q=Hosakote+Vegetable+Market"
    },

    # --------------------------------------------------------------------------
    # 5. BENGALURU URBAN DISTRICT (ಬೆಂಗಳೂರು ನಗರ)
    # --------------------------------------------------------------------------
    {
        "id": "blr_yeshwanthpur_apmc",
        "name_kn": "ಬೆಂಗಳೂರು ಯಶವಂತಪುರ ಪ್ರಧಾನ ಎಪಿಎಂಸಿ ಪ್ರಾಂಗಣ (ರಾಜ್ಯದ ಅತಿ ದೊಡ್ಡ ಸಗಟು ಮಂಡಿ)",
        "name_en": "Bengaluru Yeshwanthpur Principal Mega APMC Market Yard",
        "category": "apmc",
        "district": "Bengaluru Urban",
        "taluk": "Bengaluru North",
        "address": "ಯಶವಂತಪುರ, ತುಮಕೂರು ಮುಖ್ಯ ರಸ್ತೆ, ಬೆಂಗಳೂರು - 560022",
        "crops_accepted": ["ragi", "paddy", "onion", "bengal_gram", "tur", "coconut", "potato"],
        "rates": {
            "ragi": 4420,
            "paddy": 2640,
            "onion": 3050,
            "bengal_gram": 6650,
            "tur": 10900,
            "coconut": 29800,
            "potato": 2100
        },
        "premium_vs_local": "+₹200 - ₹350 ರಾಜಧಾನಿಯ ಅತ್ಯುನ್ನತ ಚಿಲ್ಲರೆ ಬೇಡಿಕೆ ಲಾಭ",
        "commission": "1.5% ಅಧಿಕೃತ ಇ-ನಾಮ್",
        "payment_mode": "ಇ-ನಾಮ್ RTGS / ನೆಫ್ಟ್ ಪಾವತಿ",
        "weighing": "100% ಡಿಜಿಟಲ್ ಧರ್ಮಕಾಂಟಾ",
        "facilities": ["ಕರ್ನಾಟಕದ ಅತ್ಯುನ್ನತ ಬೆಲೆ", "ಇ-ನಾಮ್ ಪಾರದರ್ಶಕತೆ", "ದಿನದ 24 ಗಂಟೆಯೂ ಸರಕು ಅನ್‌ಲೋಡಿಂಗ್", "ಬೃಹತ್ ಗೋದಾಮುಗಳು"],
        "phone": "+91 80 2337 1515",
        "timings": "ಬೆಳಿಗ್ಗೆ 6:00 ರಿಂದ ರಾತ್ರಿ 8:00 (24 ಗಂಟೆ ಪ್ರವೇಶ)",
        "maps_url": "https://maps.google.com/?q=Yeshwanthpur+APMC+Yard+Bangalore"
    },
    {
        "id": "blr_hopcoms_central",
        "name_kn": "ಹಾಪ್‌ಕಾಮ್ಸ್ (HOPCOMS) ಕೇಂದ್ರ ಖರೀದಿ ವಿಭಾಗ & ರೈತ ಸೇವಾ ಕೇಂದ್ರ",
        "name_en": "HOPCOMS Central Procurement & Farmers Terminal, Lalbagh",
        "category": "fpo",
        "district": "Bengaluru Urban",
        "taluk": "Bengaluru South",
        "address": "ಲಾಲ್‌ಬಾಗ್ ದಕ್ಷಿಣ ದ್ವಾರದ ಬಳಿ, ಬೆಂಗಳೂರು - 560004",
        "crops_accepted": ["tomato", "onion", "potato", "banana", "green_chilli", "coconut"],
        "rates": {
            "tomato": 2000,
            "onion": 3080,
            "potato": 2120,
            "banana": 2420,
            "green_chilli": 3580,
            "coconut": 29900
        },
        "premium_vs_local": "+₹250 ಸರ್ಕಾರಿ ಬೆಂಬಲಿತ ಹಾಪ್‌ಕಾಮ್ಸ್ ಪ್ರೀಮಿಯಂ ದರ",
        "commission": "0% (ರೈತರ ಸಹಕಾರಿ - ಶೂನ್ಯ ಕಮಿಷನ್)",
        "payment_mode": "ನೇರ ಬ್ಯಾಂಕ್ ಖಾತೆಗೆ NEFT / RTGS (24 ಗಂಟೆ)",
        "weighing": "ಪಾರದರ್ಶಕ ಎಲೆಕ್ಟ್ರಾನಿಕ್ ತಕ್ಕಡಿ",
        "facilities": ["100% ಶೂನ್ಯ ದಲ್ಲಾಳಿ", "ಖಚಿತ ಪಾವತಿ", "ಕರ್ನಾಟಕ ಸರ್ಕಾರಿ ಸಹಯೋಗ"],
        "phone": "+91 80 2657 8764",
        "timings": "ಬೆಳಿಗ್ಗೆ 7:00 ರಿಂದ ಸಂಜೆ 4:00",
        "maps_url": "https://maps.google.com/?q=HOPCOMS+Head+Office+Lalbagh+Bangalore"
    },

    # --------------------------------------------------------------------------
    # 6. BIDAR DISTRICT (ಬೀದರ್)
    # --------------------------------------------------------------------------
    {
        "id": "bdr_apmc_main",
        "name_kn": "ಬೀದರ್ ಪ್ರಧಾನ ಗಾಂಧಿ ಗಂಜ್ ಎಪಿಎಂಸಿ ಪ್ರಾಂಗಣ & ಸೋಯಾಬಿನ್ ಮಾರುಕಟ್ಟೆ",
        "name_en": "Bidar Gandhi Gunj Principal APMC & Soybean Yard",
        "category": "apmc",
        "district": "Bidar",
        "taluk": "Bidar",
        "address": "ಗಾಂಧಿ ಗಂಜ್, ರೈಲ್ವೆ ನಿಲ್ದಾಣ ರಸ್ತೆ, ಬೀದರ್ - 585401",
        "crops_accepted": ["soybean", "tur", "bengal_gram", "jowar", "sugarcane"],
        "rates": {
            "soybean": 4820,
            "tur": 10750,
            "bengal_gram": 6640,
            "jowar": 3840,
            "sugarcane": 3430
        },
        "premium_vs_local": "+₹180 - ₹260 ಮಹಾರಾಷ್ಟ್ರ-ತೆಲಂಗಾಣ ಗಡಿ ಸ್ಪರ್ಧಾತ್ಮಕ ದರ",
        "commission": "1.5% APMC ನಿಯಂತ್ರಿತ",
        "payment_mode": "ಇ-ನಾಮ್ RTGS / ಬ್ಯಾಂಕ್ ಚೆಕ್",
        "weighing": "ಡಿಜಿಟಲ್ ಧರ್ಮಕಾಂಟಾ",
        "facilities": ["ಸೋಯಾ ಪ್ರೊಸೆಸಿಂಗ್ ಲಿಂಕ್", "ಇ-ನಾಮ್ ಲೈವ್ ಬಿಡ್ಡಿಂಗ್", "ಉಚಿತ ದಾಸ್ತಾನು ಶೆಡ್"],
        "phone": "+91 8482 225330",
        "timings": "ಬೆಳಿಗ್ಗೆ 8:00 ರಿಂದ ಸಂಜೆ 5:30",
        "maps_url": "https://maps.google.com/?q=Gandhi+Gunj+APMC+Bidar"
    },
    {
        "id": "bdr_bhalki_pulses",
        "name_kn": "ಭಾಲ್ಕಿ ಬೇಳೆಕಾಳು & ಎಣ್ಣೆಕಾಳು ಸಹಕಾರಿ ಖರೀದಿ ಪ್ರಾಂಗಣ",
        "name_en": "Bhalki Pulses & Oilseeds Cooperative Procurement Yard",
        "category": "fpo",
        "district": "Bidar",
        "taluk": "Bhalki",
        "address": "ಹುಮ್ನಾಬಾದ್ ರಸ್ತೆ, ಭಾಲ್ಕಿ, ಬೀದರ್ - 585328",
        "crops_accepted": ["tur", "soybean", "bengal_gram", "jowar"],
        "rates": {
            "tur": 10800,
            "soybean": 4840,
            "bengal_gram": 6650,
            "jowar": 3850
        },
        "premium_vs_local": "+₹200 ಸ್ಥಳೀಯ ಮಧ್ಯವರ್ತಿಗಳಿಗಿಂತ ಹೆಚ್ಚು",
        "commission": "0% (ಸಹಕಾರಿ ನೇರ ಖರೀದಿ)",
        "payment_mode": "ನೇರ DBT ಬ್ಯಾಂಕ್ ವರ್ಗಾವಣೆ",
        "weighing": "ಪಾರದರ್ಶಕ ಎಲೆಕ್ಟ್ರಾನಿಕ್ ತೂಕ",
        "facilities": ["ಶೂನ್ಯ ಕಮಿಷನ್", "ಬೇಳೆ ಗಿರಣಿ ನೇರ ಪೂರೈಕೆ", "ರೈತ ಭವನ"],
        "phone": "+91 8484 262210",
        "timings": "ಬೆಳಿಗ್ಗೆ 8:30 ರಿಂದ ಸಂಜೆ 5:00",
        "maps_url": "https://maps.google.com/?q=APMC+Market+Bhalki+Bidar"
    },

    # --------------------------------------------------------------------------
    # 7. CHAMARAJANAGAR DISTRICT (ಚಾಮರಾಜನಗರ)
    # --------------------------------------------------------------------------
    {
        "id": "cmr_apmc_main",
        "name_kn": "ಚಾಮರಾಜನಗರ ಪ್ರಧಾನ ಎಪಿಎಂಸಿ ಪ್ರಾಂಗಣ & ಅರಿಶಿನ-ಬಾಳೆ ಮಾರುಕಟ್ಟೆ",
        "name_en": "Chamarajanagar Principal APMC & Banana Terminal",
        "category": "apmc",
        "district": "Chamarajanagar",
        "taluk": "Chamarajanagar",
        "address": "ರಾಮಸಮುದ್ರ, ಸಂತೆಮರಹಳ್ಳಿ ರಸ್ತೆ, ಚಾಮರಾಜನಗರ - 571313",
        "crops_accepted": ["banana", "sunflower", "ragi", "sugarcane", "maize"],
        "rates": {
            "banana": 2400,
            "sunflower": 6280,
            "ragi": 4350,
            "sugarcane": 3440,
            "maize": 2340
        },
        "premium_vs_local": "+₹150 ತಮಿಳುನಾಡು-ಕೇರಳ ರಫ್ತುದಾರರ ನೇರ ಖರೀದಿ",
        "commission": "1.5% ನಿಯಂತ್ರಿತ ಶುಲ್ಕ",
        "payment_mode": "ಇ-ನಾಮ್ RTGS / ಬ್ಯಾಂಕ್ ಖಾತೆಗೆ ಪಾವತಿ",
        "weighing": "ಡಿಜಿಟಲ್ ವೇಯಿಂಗ್ ಬ್ರಿಡ್ಜ್",
        "facilities": ["ಬಾಳೆ ಹಣ್ಣು ಗ್ರೇಡಿಂಗ್ ಶೆಡ್", "ಇ-ನಾಮ್ ನೆಟ್‌ವರ್ಕ್", "ತಮಿಳುನಾಡು ಗಡಿ ವ್ಯಾಪಾರ"],
        "phone": "+91 8226 222040",
        "timings": "ಬೆಳಿಗ್ಗೆ 7:30 ರಿಂದ ಸಂಜೆ 5:00",
        "maps_url": "https://maps.google.com/?q=APMC+Market+Chamarajanagar"
    },
    {
        "id": "cmr_gundlupet_market",
        "name_kn": "ಗುಂಡ್ಲುಪೇಟೆ ಸೂರ್ಯಕಾಂತಿ & ತರಕಾರಿ ಸಗಟು ಖರೀದಿ ಪ್ರಾಂಗಣ",
        "name_en": "Gundlupete Sunflower & Agro-Produce Trading Center",
        "category": "apmc",
        "district": "Chamarajanagar",
        "taluk": "Gundlupete",
        "address": "ಊಟಿ ಮುಖ್ಯ ರಸ್ತೆ, ಗುಂಡ್ಲುಪೇಟೆ - 571111",
        "crops_accepted": ["sunflower", "banana", "onion", "tomato"],
        "rates": {
            "sunflower": 6320,
            "banana": 2410,
            "onion": 2940,
            "tomato": 1940
        },
        "premium_vs_local": "+₹180 ಎಣ್ಣೆ ಗಿರಣಿಗಳ ಪೈಪೋಟಿ ದರ",
        "commission": "1.5% APMC ಅಧಿಕೃತ",
        "payment_mode": "ಸ್ಪಾಟ್ ಕ್ಯಾಶ್ / ಬ್ಯಾಂಕ್ RTGS",
        "weighing": "ಕಂಪ್ಯೂಟರೀಕೃತ ತೂಕ",
        "facilities": ["ಕೇರಳ-ತಮಿಳುನಾಡು ಹೆದ್ದಾರಿ ಸಂಪರ್ಕ", "ಶೇಖರಣಾ ಗೋದಾಮು"],
        "phone": "+91 8229 222135",
        "timings": "ಬೆಳಿಗ್ಗೆ 7:00 ರಿಂದ ಸಂಜೆ 4:30",
        "maps_url": "https://maps.google.com/?q=APMC+Yard+Gundlupet"
    },

    # --------------------------------------------------------------------------
    # 8. CHIKKABALLAPURA DISTRICT (ಚಿಕ್ಕಬಳ್ಳಾಪುರ)
    # --------------------------------------------------------------------------
    {
        "id": "ckb_apmc_main",
        "name_kn": "ಚಿಕ್ಕಬಳ್ಳಾಪುರ ಪ್ರಧಾನ ಎಪಿಎಂಸಿ ತರಕಾರಿ & ಹೂವಿನ ಪ್ರಾಂಗಣ",
        "name_en": "Chikkaballapura Principal APMC Vegetable Terminal",
        "category": "apmc",
        "district": "Chikkaballapura",
        "taluk": "Chikkaballapura",
        "address": "ಶಿಡ್ಲಘಟ್ಟ ರಸ್ತೆ, ಚಿಕ್ಕಬಳ್ಳಾಪುರ - 562101",
        "crops_accepted": ["tomato", "potato", "ragi", "green_chilli"],
        "rates": {
            "tomato": 1970,
            "potato": 2080,
            "ragi": 4370,
            "green_chilli": 3520
        },
        "premium_vs_local": "+₹140 ರಾಷ್ಟ್ರೀಯ ಹೈವೇ ಕಾರಿಡಾರ್ ಬೇಡಿಕೆ",
        "commission": "1.5% ನಿಯಂತ್ರಿತ",
        "payment_mode": "ಸ್ಥಳದಲ್ಲೇ ನಗದು / ಬ್ಯಾಂಕ್ ಪಾವತಿ",
        "weighing": "ಎಲೆಕ್ಟ್ರಾನಿಕ್ ಕ್ರೇಟ್ ತಕ್ಕಡಿ",
        "facilities": ["ದೈನಂದಿನ ಬೆಳಗಿನ ಹರಾಜು", "ಕೋಲ್ಡ್ ಸ್ಟೋರೇಜ್", "ಕ್ರೇಟ್ ವಿನಿಮಯ"],
        "phone": "+91 8156 272230",
        "timings": "ಬೆಳಿಗ್ಗೆ 6:00 ರಿಂದ ಮಧ್ಯಾಹ್ನ 3:00",
        "maps_url": "https://maps.google.com/?q=APMC+Market+Chikkaballapur"
    },
    {
        "id": "ckb_chintamani_groundnut",
        "name_kn": "ಚಿಂತಾಮಣಿ ಕಡಲೆಕಾಯಿ & ವಾಣಿಜ್ಯ ಬೆಳೆ ಎಪಿಎಂಸಿ ಪ್ರಾಂಗಣ",
        "name_en": "Chintamani Groundnut & Commercial Crops APMC Yard",
        "category": "apmc",
        "district": "Chikkaballapura",
        "taluk": "Chintamani",
        "address": "ಶ್ರೀನಿವಾಸಪುರ ರಸ್ತೆ, ಚಿಂತಾಮಣಿ - 563125",
        "crops_accepted": ["groundnut", "ragi", "tomato", "maize"],
        "rates": {
            "groundnut": 7120,
            "ragi": 4360,
            "tomato": 1960,
            "maize": 2330
        },
        "premium_vs_local": "+₹170 ಎಣ್ಣೆ ಗಿರಣಿಗಳ ನೇರ ಖರೀದಿ ಪ್ರೀಮಿಯಂ",
        "commission": "1.5% ಅಧಿಕೃತ",
        "payment_mode": "ಇ-ನಾಮ್ RTGS / ಚೆಕ್",
        "weighing": "ಡಿಜಿಟಲ್ ಧರ್ಮಕಾಂಟಾ",
        "facilities": ["ಶೇಂಗಾ ಕ್ಲೀನಿಂಗ್ ಮೆಷಿನ್", "ಆಂಧ್ರಪ್ರದೇಶ ಗಡಿ ವ್ಯಾಪಾರ"],
        "phone": "+91 8154 252180",
        "timings": "ಬೆಳಿಗ್ಗೆ 7:30 ರಿಂದ ಸಂಜೆ 5:00",
        "maps_url": "https://maps.google.com/?q=APMC+Chintamani"
    },

    # --------------------------------------------------------------------------
    # 9. CHIKKAMAGALURU DISTRICT (ಚಿಕ್ಕಮಗಳೂರು)
    # --------------------------------------------------------------------------
    {
        "id": "ckm_apmc_main",
        "name_kn": "ಚಿಕ್ಕಮಗಳೂರು ಪ್ರಧಾನ ಎಪಿಎಂಸಿ ಪ್ರಾಂಗಣ & ಕಾಫಿ-ಮಸಾಲೆ ಮಾರುಕಟ್ಟೆ",
        "name_en": "Chikkamagaluru Principal APMC Spices & Agro Market",
        "category": "apmc",
        "district": "Chikkamagaluru",
        "taluk": "Chikkamagaluru",
        "address": "ಕೆ.ಎಂ. ರಸ್ತೆ, ಚಿಕ್ಕಮಗಳೂರು - 577101",
        "crops_accepted": ["black_pepper", "cardamom", "ginger", "ragi", "arecanut"],
        "rates": {
            "black_pepper": 670,
            "cardamom": 2620,
            "ginger": 5260,
            "ragi": 4340,
            "arecanut": 55400
        },
        "premium_vs_local": "+₹30 - ₹50/ಕೆಜಿ ಕಾಳುಮೆಣಸಿಗೆ ರಫ್ತು ಪ್ರೀಮಿಯಂ",
        "commission": "1.5% APMC ನಿಯಂತ್ರಿತ",
        "payment_mode": "RTGS / ನೇರ ಬ್ಯಾಂಕ್ ವರ್ಗಾವಣೆ",
        "weighing": "ಪಾರದರ್ಶಕ ಎಲೆಕ್ಟ್ರಾನಿಕ್ ತಕ್ಕಡಿ",
        "facilities": ["ಮಸಾಲೆ ಗುಣಮಟ್ಟ ಪರೀಕ್ಷೆ", "ಉಗ್ರಾಣ ರಶೀದಿ ಸಾಲ", "ರಫ್ತುದಾರರ ನೇರ ಕೌಂಟರ್"],
        "phone": "+91 8262 230450",
        "timings": "ಬೆಳಿಗ್ಗೆ 8:30 ರಿಂದ ಸಂಜೆ 5:00",
        "maps_url": "https://maps.google.com/?q=APMC+Market+Chikkamagaluru"
    },
    {
        "id": "ckm_kadur_onion",
        "name_kn": "ಕಡೂರು ಈರುಳ್ಳಿ & ದವಸ ಧಾನ್ಯಗಳ ಎಪಿಎಂಸಿ ಉಪ ಪ್ರಾಂಗಣ",
        "name_en": "Kadur Onion & Commercial Grains APMC Sub-Yard",
        "category": "apmc",
        "district": "Chikkamagaluru",
        "taluk": "Kadur",
        "address": "ಬಾಣಾವರ ರಸ್ತೆ, ಕಡೂರು, ಚಿಕ್ಕಮಗಳೂರು - 577548",
        "crops_accepted": ["onion", "ragi", "maize", "sunflower"],
        "rates": {
            "onion": 2950,
            "ragi": 4350,
            "maize": 2340,
            "sunflower": 6250
        },
        "premium_vs_local": "+₹160 ಈರುಳ್ಳಿ ಸಗಟು ಖರೀದಿದಾರರ ಸ್ಪರ್ಧೆ",
        "commission": "1.5% ನಿಯಂತ್ರಿತ",
        "payment_mode": "ಇ-ನಾಮ್ RTGS / ನಗದು",
        "weighing": "ಡಿಜಿಟಲ್ ಧರ್ಮಕಾಂಟಾ",
        "facilities": ["ದೊಡ್ಡ ಒಣಗಿಸುವ ಪ್ರಾಂಗಣ", "ರೈಲ್ವೆ ಸಂಪರ್ಕ"],
        "phone": "+91 8267 221230",
        "timings": "ಬೆಳಿಗ್ಗೆ 8:00 ರಿಂದ ಸಂಜೆ 5:00",
        "maps_url": "https://maps.google.com/?q=APMC+Yard+Kadur"
    },

    # --------------------------------------------------------------------------
    # 10. CHITRADURGA DISTRICT (ಚಿತ್ರದುರ್ಗ)
    # --------------------------------------------------------------------------
    {
        "id": "cta_apmc_main",
        "name_kn": "ಚಿತ್ರದುರ್ಗ ಪ್ರಧಾನ ಎಪಿಎಂಸಿ ಪ್ರಾಂಗಣ & ಹತ್ತಿ-ಶೇಂಗಾ ಮಾರುಕಟ್ಟೆ",
        "name_en": "Chitradurga Principal APMC Yard & Cotton-Groundnut Market",
        "category": "apmc",
        "district": "Chitradurga",
        "taluk": "Chitradurga",
        "address": "ಕೆಳಗೋಟೆ, ರಾಷ್ಟ್ರೀಯ ಹೆದ್ದಾರಿ 48, ಚಿತ್ರದುರ್ಗ - 577501",
        "crops_accepted": ["groundnut", "cotton", "onion", "maize", "ragi", "sunflower"],
        "rates": {
            "groundnut": 7180,
            "cotton": 7790,
            "onion": 2960,
            "maize": 2360,
            "ragi": 4360,
            "sunflower": 6280
        },
        "premium_vs_local": "+₹180 - ₹250 ರಾಜ್ಯ ಹೆದ್ದಾರಿ ಹರಾಜು ಪೈಪೋಟಿ",
        "commission": "1.5% ನಿಯಂತ್ರಿತ",
        "payment_mode": "ಇ-ನಾಮ್ RTGS / ಬ್ಯಾಂಕ್ ಖಾತೆಗೆ",
        "weighing": "ಕಂಪ್ಯೂಟರೀಕೃತ ಡಿಜಿಟಲ್ ಧರ್ಮಕಾಂಟಾ",
        "facilities": ["ಇ-ನಾಮ್ ಬಿಡ್ಡಿಂಗ್", "ಬೃಹತ್ ಗೋದಾಮು ಶೆಡ್", "ರೈತ ಭವನ"],
        "phone": "+91 8194 222460",
        "timings": "ಬೆಳಿಗ್ಗೆ 8:00 ರಿಂದ ಸಂಜೆ 5:30",
        "maps_url": "https://maps.google.com/?q=APMC+Market+Yard+Chitradurga"
    },
    {
        "id": "challakere_oil_cluster",
        "name_kn": "ಚಳ್ಳಕೆರೆ ಎಣ್ಣೆ ಗಿರಣಿಗಳ ಸಂಘ & ಕಡಲೆಕಾಯಿ ನೇರ ಖರೀದಿ ಕೇಂದ್ರ",
        "name_en": "Challakere Oil Millers Association Direct Groundnut Hub",
        "category": "processor",
        "district": "Chitradurga",
        "taluk": "Challakere",
        "address": "ಬಳ್ಳಾರಿ ರಸ್ತೆ, ಇಂಡಸ್ಟ್ರಿಯಲ್ ಏರಿಯಾ, ಚಳ್ಳಕೆರೆ 'ಆಯಿಲ್ ಸಿಟಿ' - 577522",
        "crops_accepted": ["groundnut", "sunflower"],
        "rates": {
            "groundnut": 7250,
            "sunflower": 6350
        },
        "premium_vs_local": "+₹300 - ₹450 ಗಿರಣಿಗಳಿಂದ ನೇರ ಖರೀದಿ, ಮಧ್ಯವರ್ತಿ ಕಮಿಷನ್ ಶೂನ್ಯ",
        "commission": "0% (ಮಿಲ್ ನೇರ ಖರೀದಿ)",
        "payment_mode": "ಸ್ಥಳದಲ್ಲೇ RTGS / ಚೆಕ್ ಪಾವತಿ",
        "weighing": "ಕಂಪ್ಯೂಟರೀಕೃತ ಬ್ರಿಡ್ಜ್ ಸ್ಕೇಲ್",
        "facilities": ["ಎಣ್ಣೆ ಅಂಶ (Oil content) ಆಧಾರಿತ ಹೆಚ್ಚುವರಿ ಪ್ರೀಮಿಯಂ", "ಸ್ಪಾಟ್ ಪೇಮೆಂಟ್", "ಶೂನ್ಯ ಕಮಿಷನ್"],
        "phone": "+91 8195 222840",
        "timings": "ಬೆಳಿಗ್ಗೆ 8:30 ರಿಂದ ಸಂಜೆ 6:00",
        "maps_url": "https://maps.google.com/?q=Challakere+Industrial+Area"
    },

    # --------------------------------------------------------------------------
    # 11. DAKSHINA KANNADA DISTRICT (ದಕ್ಷಿಣ ಕನ್ನಡ)
    # --------------------------------------------------------------------------
    {
        "id": "campco_puttur_hub",
        "name_kn": "ಕ್ಯಾಂಪ್ಕೋ (CAMPCO) ಕೇಂದ್ರ ಕಚೇರಿ & ಅಡಿಕೆ-ಕೋಕೋ ಖರೀದಿ ವಿಭಾಗ",
        "name_en": "The CAMPCO Ltd Central Procurement Division",
        "category": "fpo",
        "district": "Dakshina Kannada",
        "taluk": "Puttur",
        "address": "ಕ್ಯಾಂಪ್ಕೋ ಟವರ್ಸ್, ಮಿಷನ್ ಸ್ಟ್ರೀಟ್, ಮಂಗಳೂರು & ಪುತ್ತೂರು - 575001",
        "crops_accepted": ["arecanut", "black_pepper", "coconut"],
        "rates": {
            "arecanut": 55800,
            "black_pepper": 675,
            "coconut": 29000
        },
        "premium_vs_local": "+₹800 ರೈತರ ಸ್ವಂತ ಸಹಕಾರಿ ಸಂಸ್ಥೆ, ಶೂನ್ಯ ದಲ್ಲಾಳಿ ಕಡಿತ",
        "commission": "0% (ಸಹಕಾರಿ ಸದಸ್ಯತ್ವ ಬೋನಸ್ ಲಭ್ಯ)",
        "payment_mode": "ನೇರ ಬ್ಯಾಂಕ್ ಖಾತೆಗೆ NEFT / RTGS (24 ಗಂಟೆ)",
        "weighing": "100% ಗ್ಯಾರಂಟಿ ಡಿಜಿಟಲ್ ತೂಕ",
        "facilities": ["ರೈತರ ಸಹಕಾರಿ ಒಡೆತನ", "ಉಗ್ರಾಣ ರಶೀದಿ ಸಾಲ ಸೌಲಭ್ಯ (Warehouse Loan)", "ವಾರ್ಷಿಕ ಡಿವಿಡೆಂಡ್"],
        "phone": "+91 824 2422581",
        "timings": "ಬೆಳಿಗ್ಗೆ 9:00 ರಿಂದ ಸಂಜೆ 5:00",
        "maps_url": "https://maps.google.com/?q=CAMPCO+Head+Office+Mangalore"
    },
    {
        "id": "mng_baikampady_apmc",
        "name_kn": "ಮಂಗಳೂರು ಬೈಕಂಪಾಡಿ ಪ್ರಧಾನ ಎಪಿಎಂಸಿ ಪ್ರಾಂಗಣ & ಕರಾವಳಿ ಮಂಡಿ",
        "name_en": "Mangaluru Baikampady Principal APMC Yard",
        "category": "apmc",
        "district": "Dakshina Kannada",
        "taluk": "Mangaluru",
        "address": "ಬೈಕಂಪಾಡಿ ಕೈಗಾರಿಕಾ ಪ್ರದೇಶ, ಮಂಗಳೂರು - 575011",
        "crops_accepted": ["coconut", "arecanut", "black_pepper", "paddy"],
        "rates": {
            "coconut": 29600,
            "arecanut": 55900,
            "black_pepper": 678,
            "paddy": 2580
        },
        "premium_vs_local": "+₹200 ಕರಾವಳಿ ರಫ್ತು ಹಬ್ ಪ್ರೀಮಿಯಂ",
        "commission": "1.5% APMC ನಿಯಂತ್ರಿತ",
        "payment_mode": "ಇ-ನಾಮ್ RTGS / ಬ್ಯಾಂಕ್ ವರ್ಗಾವಣೆ",
        "weighing": "ಡಿಜಿಟಲ್ ಧರ್ಮಕಾಂಟಾ",
        "facilities": ["ಬಂದರು ರಫ್ತು ಸಂಪರ್ಕ", "ಕೊಬ್ಬರಿ ತೇವಾಂಶ ಲ್ಯಾಬ್", "ಶೇಖರಣಾ ಗೋದಾಮು"],
        "phone": "+91 824 2407230",
        "timings": "ಬೆಳಿಗ್ಗೆ 8:00 ರಿಂದ ಸಂಜೆ 5:30",
        "maps_url": "https://maps.google.com/?q=APMC+Baikampady+Mangalore"
    },

    # --------------------------------------------------------------------------
    # 12. DAVANAGERE DISTRICT (ದಾವಣಗೆರೆ)
    # --------------------------------------------------------------------------
    {
        "id": "davanagere_apmc_main",
        "name_kn": "ದಾವಣಗೆರೆ ಪ್ರಧಾನ ಎಪಿಎಂಸಿ ಪ್ರಾಂಗಣ (ದಕ್ಷಿಣ ಭಾರತದ ಮೆಕ್ಕೆಜೋಳ ಕಣಜ)",
        "name_en": "Davanagere Principal APMC Yard (South India Maize Capital)",
        "category": "apmc",
        "district": "Davanagere",
        "taluk": "Davanagere",
        "address": "ಹದಡಿ ರಸ್ತೆ, ದಾವಣಗೆರೆ - 577005",
        "crops_accepted": ["maize", "paddy", "ragi", "sunflower"],
        "rates": {
            "maize": 2380,
            "paddy": 2590,
            "ragi": 4340,
            "sunflower": 6220
        },
        "premium_vs_local": "+₹120 ಪಿಷ್ಟ ಕಾರ್ಖಾನೆಗಳಿಂದ ನೇರ ಸ್ಪರ್ಧೆ",
        "commission": "1.5% ನಿಯಂತ್ರಿತ ಶುಲ್ಕ",
        "payment_mode": "ಇ-ನಾಮ್ RTGS / ಸ್ಥಳೀಯ ಬ್ಯಾಂಕ್ ಚೆಕ್",
        "weighing": "ಡಿಜಿಟಲ್ ಧರ್ಮಕಾಂಟಾ",
        "facilities": ["ಪಿಷ್ಟ & ಕೋಳಿ ಆಹಾರ ಮಿಲ್‌ಗಳ ಹಬ್", "ತ್ವರಿತ ಅನ್‌ಲೋಡಿಂಗ್", "ಗ್ರೇಡಿಂಗ್ ಪರೀಕ್ಷೆ"],
        "phone": "+91 8192 230488",
        "timings": "ಬೆಳಿಗ್ಗೆ 8:00 ರಿಂದ ಸಂಜೆ 5:30",
        "maps_url": "https://maps.google.com/?q=APMC+Market+Yard+Davanagere"
    },
    {
        "id": "dvr_harihara_paddy",
        "name_kn": "ಹರಿಹರ ಭತ್ತ & ಮೆಕ್ಕೆಜೋಳ ಸಗಟು ಖರೀದಿ ಕೇಂದ್ರ",
        "name_en": "Harihara Paddy & Maize Procurement Hub",
        "category": "apmc",
        "district": "Davanagere",
        "taluk": "Harihara",
        "address": "ಶಿವಮೊಗ್ಗ ರಸ್ತೆ, ಹರಿಹರ, ದಾವಣಗೆರೆ - 577601",
        "crops_accepted": ["paddy", "maize", "sugarcane", "ragi"],
        "rates": {
            "paddy": 2610,
            "maize": 2390,
            "sugarcane": 3460,
            "ragi": 4350
        },
        "premium_vs_local": "+₹150 ತುಂಗಭದ್ರಾ ನದಿ ಪಾತ್ರದ ಬೆಳೆಗಳಿಗೆ ಅತ್ಯುತ್ತಮ ದರ",
        "commission": "1.5% ಅಧಿಕೃತ",
        "payment_mode": "ಇ-ನಾಮ್ RTGS / ಬ್ಯಾಂಕ್ ಖಾತೆಗೆ",
        "weighing": "ಕಂಪ್ಯೂಟರೀಕೃತ ಧರ್ಮಕಾಂಟಾ",
        "facilities": ["ಗಿರಣಿ ನೇರ ಲಿಂಕ್", "ಶೇಖರಣಾ ಗೋದಾಮು"],
        "phone": "+91 8192 241280",
        "timings": "ಬೆಳಿಗ್ಗೆ 8:00 ರಿಂದ ಸಂಜೆ 5:00",
        "maps_url": "https://maps.google.com/?q=APMC+Harihara"
    },

    # --------------------------------------------------------------------------
    # 13. DHARWAD DISTRICT (ಧಾರವಾಡ)
    # --------------------------------------------------------------------------
    {
        "id": "hubli_amargol_apmc",
        "name_kn": "ಹುಬ್ಬಳ್ಳಿ ಅಮರಗೋಳ ಪ್ರಧಾನ ಎಪಿಎಂಸಿ ಪ್ರಾಂಗಣ (ಉತ್ತರ ಕರ್ನಾಟಕದ ಹೆಬ್ಬಾಗಿಲು)",
        "name_en": "Hubballi Amargol Principal APMC Yard (North Karnataka Hub)",
        "category": "apmc",
        "district": "Dharwad",
        "taluk": "Hubballi",
        "address": "ಅಮರಗೋಳ, ಪುಣೆ-ಬೆಂಗಳೂರು ಹೈವೇ, ಹುಬ್ಬಳ್ಳಿ - 580025",
        "crops_accepted": ["onion", "green_chilli", "bengal_gram", "cotton", "maize", "soybean", "jowar"],
        "rates": {
            "onion": 2920,
            "bengal_gram": 6580,
            "cotton": 7720,
            "maize": 2340,
            "soybean": 4750,
            "jowar": 3780,
            "green_chilli": 3490
        },
        "premium_vs_local": "+₹150 - ₹250 ಬೃಹತ್ ಇ-ನಾಮ್ ಟ್ರೇಡಿಂಗ್ ವಾಲ್ಯೂಮ್",
        "commission": "1.5% ಇ-ನಾಮ್ ಪಾರದರ್ಶಕ ಶುಲ್ಕ",
        "payment_mode": "ಇ-ನಾಮ್ ಖಚಿತ ಬ್ಯಾಂಕ್ DBT",
        "weighing": "ಡಿಜಿಟಲ್ ವೇಯಿಂಗ್ ಬ್ರಿಡ್ಜ್",
        "facilities": ["100+ ಎಕರೆ ಮಾರುಕಟ್ಟೆ", "ರೈಲ್ವೆ ಸರಕು ಸಾಗಣೆ ನೇರ ಸಂಪರ್ಕ", "ಇ-ನಾಮ್ ಎಲೆಕ್ಟ್ರಾನಿಕ್ ಪಾವತಿ", "ರೈತ ವಿಶ್ರಾಂತಿ ನಿಲಯ"],
        "phone": "+91 836 2223400",
        "timings": "ಬೆಳಿಗ್ಗೆ 8:00 ರಿಂದ ಸಂಜೆ 6:00",
        "maps_url": "https://maps.google.com/?q=Amargol+APMC+Market+Yard+Hubli"
    },
    {
        "id": "dhw_dharwad_pulses",
        "name_kn": "ಧಾರವಾಡ ಕೃಷಿ ಉತ್ಪನ್ನ ಉಪ ಮಾರುಕಟ್ಟೆ ಪ್ರಾಂಗಣ & ಸೋಯಾಬಿನ್ ಮಂಡಿ",
        "name_en": "Dharwad Commercial Crops Sub-Yard & Soybean Depot",
        "category": "apmc",
        "district": "Dharwad",
        "taluk": "Dharwad",
        "address": "ಬೆಳಗಾವಿ ರಸ್ತೆ, ನರೇಂದ್ರ ಬೈಪಾಸ್ ಬಳಿ, ಧಾರವಾಡ - 580008",
        "crops_accepted": ["soybean", "cotton", "bengal_gram", "jowar"],
        "rates": {
            "soybean": 4780,
            "cotton": 7760,
            "bengal_gram": 6610,
            "jowar": 3800
        },
        "premium_vs_local": "+₹160 ನೇರ ವ್ಯಾಪಾರಿ ಬಿಡ್ಡಿಂಗ್ ಪ್ರೀಮಿಯಂ",
        "commission": "1.5% ನಿಯಂತ್ರಿತ",
        "payment_mode": "ಇ-ನಾಮ್ RTGS",
        "weighing": "ಡಿಜಿಟಲ್ ಧರ್ಮಕಾಂಟಾ",
        "facilities": ["ಕೃಷಿ ವಿವಿ ತಾಂತ್ರಿಕ ಗ್ರೇಡಿಂಗ್", "ಶುದ್ಧ ತೂಕ ಭರವಸೆ"],
        "phone": "+91 836 2441220",
        "timings": "ಬೆಳಿಗ್ಗೆ 8:30 ರಿಂದ ಸಂಜೆ 5:00",
        "maps_url": "https://maps.google.com/?q=APMC+Market+Dharwad"
    },

    # --------------------------------------------------------------------------
    # 14. GADAG DISTRICT (ಗದಗ)
    # --------------------------------------------------------------------------
    {
        "id": "gadag_bengalgram_apmc",
        "name_kn": "ಗದಗ ಪ್ರಧಾನ ಎಪಿಎಂಸಿ ಪ್ರಾಂಗಣ (ಕಡಲೆ & ಸೂರ್ಯಕಾಂತಿ ವಿಶೇಷ ಮಂಡಿ)",
        "name_en": "Gadag Principal APMC Yard (Chana & Sunflower Trading)",
        "category": "apmc",
        "district": "Gadag",
        "taluk": "Gadag",
        "address": "ಮುಂಡರಗಿ ರಸ್ತೆ, ಗದಗ - 582101",
        "crops_accepted": ["bengal_gram", "sunflower", "onion", "groundnut", "jowar"],
        "rates": {
            "bengal_gram": 6620,
            "sunflower": 6280,
            "onion": 2900,
            "groundnut": 7040,
            "jowar": 3760
        },
        "premium_vs_local": "+₹180 ಕಡಲೆ ಮತ್ತು ಶೇಂಗಾಕ್ಕೆ ದಾಲ್ ಮಿಲ್‌ಗಳಿಂದ ಉತ್ತಮ ಬೆಲೆ",
        "commission": "1.5% APMC ನಿಯಂತ್ರಿತ",
        "payment_mode": "ಇ-ನಾಮ್ RTGS / ಚೆಕ್",
        "weighing": "ಎಲೆಕ್ಟ್ರಾನಿಕ್ ಧರ್ಮಕಾಂಟಾ",
        "facilities": ["ಇ-ನಾಮ್ ಲೈವ್ ಬಿಡ್ಡಿಂಗ್", "ಕಡಲೆ ಕ್ಲೀನಿಂಗ್ & ಗ್ರೇಡಿಂಗ್ ಶೆಡ್", "ರೈತ ಭವನ"],
        "phone": "+91 8372 238210",
        "timings": "ಬೆಳಿಗ್ಗೆ 8:00 ರಿಂದ ಸಂಜೆ 5:00",
        "maps_url": "https://maps.google.com/?q=APMC+Market+Gadag"
    },
    {
        "id": "gdg_ron_fpo",
        "name_kn": "ರೋಣ ರೈತ ಉತ್ಪಾದಕ ಸಹಕಾರಿ ಸಂಘ (FPO) & ಎಣ್ಣೆಕಾಳು ಖರೀದಿ ಕೇಂದ್ರ",
        "name_en": "Ron Oilseeds & Pulses Farmer Producer Company (FPO)",
        "category": "fpo",
        "district": "Gadag",
        "taluk": "Ron",
        "address": "ಮುಂಡರಗಿ-ರೋಣ ರಸ್ತೆ, ರೋಣ, ಗದಗ - 582209",
        "crops_accepted": ["bengal_gram", "sunflower", "groundnut", "onion"],
        "rates": {
            "bengal_gram": 6650,
            "sunflower": 6310,
            "groundnut": 7080,
            "onion": 2920
        },
        "premium_vs_local": "+₹210 ಶೂನ್ಯ ಮಧ್ಯವರ್ತಿ ಲಾಭ",
        "commission": "0% (ಎಫ್‌ಪಿಒ ರೈತ ಸದಸ್ಯತ್ವ ಶೂನ್ಯ ಕಮಿಷನ್)",
        "payment_mode": "ನೇರ DBT ಬ್ಯಾಂಕ್ ಖಾತೆಗೆ",
        "weighing": "ಪಾರದರ್ಶಕ ಎಲೆಕ್ಟ್ರಾನಿಕ್ ತಕ್ಕಡಿ",
        "facilities": ["ಶೂನ್ಯ ಕಮಿಷನ್", "ಗ್ರೇಡಿಂಗ್ ಯಂತ್ರಗಳು", "ಸಹಕಾರಿ ಡಿವಿಡೆಂಡ್"],
        "phone": "+91 8381 267340",
        "timings": "ಬೆಳಿಗ್ಗೆ 8:30 ರಿಂದ ಸಂಜೆ 5:00",
        "maps_url": "https://maps.google.com/?q=APMC+Ron+Gadag"
    },

    # --------------------------------------------------------------------------
    # 15. HASSAN DISTRICT (ಹಾಸನ)
    # --------------------------------------------------------------------------
    {
        "id": "hassan_apmc_main",
        "name_kn": "ಹಾಸನ ಪ್ರಧಾನ ಎಪಿಎಂಸಿ ಆಲೂಗಡ್ಡೆ & ಮೆಕ್ಕೆಜೋಳ ಮಾರುಕಟ್ಟೆ",
        "name_en": "Hassan Principal APMC Potato & Maize Market",
        "category": "apmc",
        "district": "Hassan",
        "taluk": "Hassan",
        "address": "ಬಿ.ಎಂ. ರಸ್ತೆ, ಹಾಸನ - 573201",
        "crops_accepted": ["potato", "maize", "ginger", "ragi", "black_pepper"],
        "rates": {
            "potato": 2040,
            "maize": 2330,
            "ginger": 5250,
            "ragi": 4330,
            "black_pepper": 660
        },
        "premium_vs_local": "+₹140 ಸ್ಥಳೀಯ ದಲ್ಲಾಳಿಗಳಿಗಿಂತ ಅಧಿಕ ದರ",
        "commission": "1.5% ಅಧಿಕೃತ",
        "payment_mode": "RTGS / ಸ್ಥಳದಲ್ಲೇ ಚೆಕ್",
        "weighing": "ಡಿಜಿಟಲ್ ಧರ್ಮಕಾಂಟಾ",
        "facilities": ["ಆಲೂಗಡ್ಡೆ ಕೋಲ್ಡ್ ಸ್ಟೋರೇಜ್ ಕನೆಕ್ಷನ್", "ಶುಂಠಿ ವಾಶಿಂಗ್ & ಪ್ಯಾಕಿಂಗ್ ಶೆಡ್"],
        "phone": "+91 8172 268420",
        "timings": "ಬೆಳಿಗ್ಗೆ 7:30 ರಿಂದ ಸಂಜೆ 5:00",
        "maps_url": "https://maps.google.com/?q=APMC+Yard+Hassan"
    },
    {
        "id": "hsn_sakleshpur_spices",
        "name_kn": "ಸಕಲೇಶಪುರ ಮಸಾಲೆ & ಕಾಳುಮೆಣಸು ಬೆಳೆಗಾರರ ಸಹಕಾರಿ ಮಾರುಕಟ್ಟೆ",
        "name_en": "Sakleshpur Planters & Spices Cooperative Marketing Society",
        "category": "fpo",
        "district": "Hassan",
        "taluk": "Sakleshpur",
        "address": "ಬಿ.ಎಂ. ರಸ್ತೆ, ಆಜಾದ್ ರಸ್ತೆ ಜಂಕ್ಷನ್, ಸಕಲೇಶಪುರ - 573134",
        "crops_accepted": ["black_pepper", "cardamom", "ginger", "potato"],
        "rates": {
            "black_pepper": 672,
            "cardamom": 2640,
            "ginger": 5290,
            "potato": 2050
        },
        "premium_vs_local": "+₹35/ಕೆಜಿ ಗುಣಮಟ್ಟದ ಗ್ರೇಡಿಂಗ್ ಪ್ರೀಮಿಯಂ",
        "commission": "0% (ಸಹಕಾರಿ ಸದಸ್ಯತ್ವ ಶೂನ್ಯ ಕಮಿಷನ್)",
        "payment_mode": "ನೇರ RTGS / ನೆಫ್ಟ್ ಪಾವತಿ",
        "weighing": "ಪಾರದರ್ಶಕ ನಿಖರ ಎಲೆಕ್ಟ್ರಾನಿಕ್ ತೂಕ",
        "facilities": ["ಮಲೆನಾಡು ಮಸಾಲೆ ರಫ್ತು ಲಿಂಕ್", "ಉಗ್ರಾಣ ರಶೀದಿ ಸಾಲ"],
        "phone": "+91 8173 244150",
        "timings": "ಬೆಳಿಗ್ಗೆ 8:30 ರಿಂದ ಸಂಜೆ 5:00",
        "maps_url": "https://maps.google.com/?q=Sakleshpur+Spices+Market"
    },

    # --------------------------------------------------------------------------
    # 16. HAVERI DISTRICT (ಹಾವೇರಿ)
    # --------------------------------------------------------------------------
    {
        "id": "byadgi_chilli_market",
        "name_kn": "ಬ್ಯಾಡಗಿ ಅಂತರರಾಷ್ಟ್ರೀಯ ಮೆಣಸಿನಕಾಯಿ ಎಪಿಎಂಸಿ ಪ್ರಾಂಗಣ",
        "name_en": "Byadgi International Chilli APMC Yard (Asia's #1 Spice Hub)",
        "category": "apmc",
        "district": "Haveri",
        "taluk": "Byadgi",
        "address": "ಎಪಿಎಂಸಿ ಮಾರ್ಕೆಟ್ ಯಾರ್ಡ್, ಬ್ಯಾಡಗಿ, ಹಾವೇರಿ ಜಿಲ್ಲೆ - 581106",
        "crops_accepted": ["byadgi_chilli", "green_chilli", "maize", "groundnut"],
        "rates": {
            "byadgi_chilli": 42000,
            "green_chilli": 3550,
            "maize": 2360,
            "groundnut": 7020
        },
        "premium_vs_local": "+₹1,500 - ₹3,000 ಅಂತರರಾಷ್ಟ್ರೀಯ ರಫ್ತುದಾರರಿಂದ ನೇರ ಬಿಡ್",
        "commission": "1.5% APMC ನಿಯಂತ್ರಿತ",
        "payment_mode": "ಇ-ನಾಮ್ RTGS ನೇರ ಖಾತೆಗೆ",
        "weighing": "100% ಕಂಪ್ಯೂಟರೀಕೃತ ಡಿಜಿಟಲ್ ತೂಕ",
        "facilities": ["ಜಾಗತಿಕ ಓಲಿಯೋರೆಸಿನ್ ರಫ್ತುದಾರರು", "ಕ್ವಾಲಿಟಿ ಅಸೆಸ್‌ಮೆಂಟ್ ಲ್ಯಾಬ್", "20 ಎಕರೆ ಬೃಹತ್ ಒಣಗಿಸುವ ಪ್ರಾಂಗಣ", "ರೈತ ಭವನ"],
        "phone": "+91 8375 228225",
        "timings": "ಬೆಳಿಗ್ಗೆ 7:00 ರಿಂದ ಸಂಜೆ 6:30",
        "maps_url": "https://maps.google.com/?q=Byadgi+Chilli+APMC+Market"
    },
    {
        "id": "hvr_ranebennur_seed",
        "name_kn": "ರಾಣೆಬೆನ್ನೂರು ಪ್ರಧಾನ ಎಪಿಎಂಸಿ ಪ್ರಾಂಗಣ & ಮೆಕ್ಕೆಜೋಳ ಮಂಡಿ",
        "name_en": "Ranebennur Principal APMC Yard & Maize Hub",
        "category": "apmc",
        "district": "Haveri",
        "taluk": "Ranebennur",
        "address": "ಹಳೆಯ ಪುಣೆ-ಬೆಂಗಳೂರು ರಸ್ತೆ, ರಾಣೆಬೆನ್ನೂರು - 581115",
        "crops_accepted": ["maize", "groundnut", "cotton", "byadgi_chilli"],
        "rates": {
            "maize": 2370,
            "groundnut": 7060,
            "cotton": 7810,
            "byadgi_chilli": 41800
        },
        "premium_vs_local": "+₹140 ಬೀಜ ಕಂಪನಿಗಳ ನೇರ ಸ್ಪರ್ಧೆ",
        "commission": "1.5% ಅಧಿಕೃತ",
        "payment_mode": "ಇ-ನಾಮ್ RTGS / ಬ್ಯಾಂಕ್ ಚೆಕ್",
        "weighing": "ಡಿಜಿಟಲ್ ಧರ್ಮಕಾಂಟಾ",
        "facilities": ["ಬೀಜ ಸಂಸ್ಕರಣಾ ಲಿಂಕ್", "ಇ-ನಾಮ್ ಲೈವ್ ಬಿಡ್ಡಿಂಗ್"],
        "phone": "+91 8373 266450",
        "timings": "ಬೆಳಿಗ್ಗೆ 8:00 ರಿಂದ ಸಂಜೆ 5:30",
        "maps_url": "https://maps.google.com/?q=APMC+Ranebennur"
    },

    # --------------------------------------------------------------------------
    # 17. KALABURAGI DISTRICT (ಕಲಬುರಗಿ)
    # --------------------------------------------------------------------------
    {
        "id": "klb_nehru_gunj",
        "name_kn": "ಕಲಬುರಗಿ ನೆಹರು ಗಂಜ್ ಪ್ರಧಾನ ತೊಗರಿ ಮಾರುಕಟ್ಟೆ ಪ್ರಾಂಗಣ",
        "name_en": "Kalaburagi Nehru Gunj Principal Tur Mandi Yard",
        "category": "apmc",
        "district": "Kalaburagi",
        "taluk": "Kalaburagi",
        "address": "ನೆಹರು ಗಂಜ್, ರೈಲ್ವೆ ನಿಲ್ದಾಣ ರಸ್ತೆ, ಕಲಬುರಗಿ - 585104",
        "crops_accepted": ["tur", "bengal_gram", "soybean", "jowar"],
        "rates": {
            "tur": 10850,
            "bengal_gram": 6620,
            "soybean": 4780,
            "jowar": 3820
        },
        "premium_vs_local": "+₹300 ಕ್ವಿಂಟಾಲಿಗೆ ಮುಕ್ತ ಸ್ಪರ್ಧಾತ್ಮಕ ಹರಾಜು",
        "commission": "1.5% ನಿಯಂತ್ರಿತ ಲೈಸೆನ್ಸ್ ಆಯೋಗ",
        "payment_mode": "ಇ-ನಾಮ್ RTGS / ನೇರ ಚೆಕ್",
        "weighing": "ಡಿಜಿಟಲ್ ಧರ್ಮಕಾಂಟಾ & ಎಲೆಕ್ಟ್ರಾನಿಕ್ ತಕ್ಕಡಿ",
        "facilities": ["ಭಾರತದ ನಂ.1 ತೊಗರಿ ಮಾರುಕಟ್ಟೆ", "ಇ-ನಾಮ್ ಹರಾಜು", "ದಾಲ್ ಮಿಲ್ ನೇರ ಖರೀದಿ", "ಉಚಿತ ಕುಡಿಯುವ ನೀರು & ಕ್ಯಾಂಟೀನ್"],
        "phone": "+91 8472 220455",
        "timings": "ಬೆಳಿಗ್ಗೆ 7:30 ರಿಂದ ಸಂಜೆ 6:00",
        "maps_url": "https://maps.google.com/?q=Nehru+Gunj+APMC+Kalaburagi"
    },
    {
        "id": "klb_nafed_msp",
        "name_kn": "NAFED / KSCMF ತೊಗರಿ & ಕಡಲೆ ಸರ್ಕಾರಿ ಖರೀದಿ ಕೇಂದ್ರ, ಸೇಡಂ ರಸ್ತೆ",
        "name_en": "NAFED/KSCMF MSP Pulses Procurement Center, Sedam Road",
        "category": "msp",
        "district": "Kalaburagi",
        "taluk": "Kalaburagi",
        "address": "ಸೇಡಂ ರಸ್ತೆ, ಎಫ್‌ಸಿಐ ಗೋದಾಮು ಬಳಿ, ಕಲಬುರಗಿ - 585105",
        "crops_accepted": ["tur", "bengal_gram", "soybean"],
        "rates": {
            "tur": 7550,
            "bengal_gram": 5650,
            "soybean": 4892
        },
        "premium_vs_local": "ಸರ್ಕಾರಿ ಕನಿಷ್ಠ ಬೆಂಬಲ ಬೆಲೆ ಭದ್ರತೆ",
        "commission": "0% (ಶೂನ್ಯ ಶುಲ್ಕ)",
        "payment_mode": "ನೇರ DBT ಬ್ಯಾಂಕ್ ವರ್ಗಾವಣೆ",
        "weighing": "ಸರ್ಕಾರಿ ಪ್ರಮಾಣೀಕೃತ ತೂಕ",
        "facilities": ["ಸರ್ಕಾರಿ ಗ್ಯಾರಂಟಿ", "ಉಚಿತ ಗೋಣಿ ಚೀಲ ಸೌಲಭ್ಯ", "ತ್ವರಿತ ಅನ್‌ಲೋಡಿಂಗ್"],
        "phone": "+91 8472 261890",
        "timings": "ಬೆಳಿಗ್ಗೆ 9:00 ರಿಂದ ಸಂಜೆ 5:00",
        "maps_url": "https://maps.google.com/?q=Sedam+Road+Procurement+Kalaburagi"
    },

    # --------------------------------------------------------------------------
    # 18. KODAGU DISTRICT (ಕೊಡಗು)
    # --------------------------------------------------------------------------
    {
        "id": "kdg_gonikoppal_spices",
        "name_kn": "ಗೋಣಿಕೊಪ್ಪಲು & ಮಡಿಕೇರಿ ಮಸಾಲೆ ಬೆಳೆಗಾರರ ಸಹಕಾರಿ ಮಾರಾಟ ಸಂಘ",
        "name_en": "Gonikoppal Planters Spices & Coffee Cooperative Society",
        "category": "fpo",
        "district": "Kodagu",
        "taluk": "Virajpet",
        "address": "ಮುಖ್ಯ ರಸ್ತೆ, ಗೋಣಿಕೊಪ್ಪಲು, ಕೊಡಗು - 571213",
        "crops_accepted": ["black_pepper", "cardamom", "ginger", "paddy"],
        "rates": {
            "black_pepper": 682,
            "cardamom": 2660,
            "ginger": 5320,
            "paddy": 2570
        },
        "premium_vs_local": "+₹40/ಕೆಜಿ ನೇರ ಅಂತರರಾಷ್ಟ್ರೀಯ ರಫ್ತು ಬೆಲೆ",
        "commission": "0% (ಸಹಕಾರಿ ಸದಸ್ಯತ್ವ ಶೂನ್ಯ ಕಮಿಷನ್)",
        "payment_mode": "ನೇರ RTGS / ನೆಫ್ಟ್ (24 ಗಂಟೆ)",
        "weighing": "ನಿಖರ ಎಲೆಕ್ಟ್ರಾನಿಕ್ ಸ್ಕೇಲ್",
        "facilities": ["ಕೊಡಗು ಮಸಾಲೆ ರಫ್ತು ಪ್ರಮಾಣೀಕರಣ", "ಉಗ್ರಾಣ ಸಾಲ", "ಸಹಕಾರಿ ಬೋನಸ್"],
        "phone": "+91 8274 247220",
        "timings": "ಬೆಳಿಗ್ಗೆ 9:00 ರಿಂದ ಸಂಜೆ 5:00",
        "maps_url": "https://maps.google.com/?q=Gonikoppal+Cooperative+Society+Kodagu"
    },
    {
        "id": "kdg_somwarpet_ginger",
        "name_kn": "ಸೋಮವಾರಪೇಟೆ ಶುಂಠಿ & ಕಾಳುಮೆಣಸು ಸಗಟು ಖರೀದಿ ಪ್ರಾಂಗಣ",
        "name_en": "Somwarpet Ginger & Black Pepper Trading Center",
        "category": "apmc",
        "district": "Kodagu",
        "taluk": "Somwarpet",
        "address": "ಹಾಸನ ರಸ್ತೆ, ಸೋಮವಾರಪೇಟೆ, ಕೊಡಗು - 571236",
        "crops_accepted": ["ginger", "black_pepper", "cardamom"],
        "rates": {
            "ginger": 5340,
            "black_pepper": 678,
            "cardamom": 2650
        },
        "premium_vs_local": "+₹150 ಶುಂಠಿಗೆ ಕೇರಳ-ಮಹಾರಾಷ್ಟ್ರ ವ್ಯಾಪಾರಿಗಳ ಸ್ಪರ್ಧೆ",
        "commission": "1.5% ನಿಯಂತ್ರಿತ",
        "payment_mode": "ಸ್ಥಳದಲ್ಲೇ ನಗದು / ಬ್ಯಾಂಕ್ ವರ್ಗಾವಣೆ",
        "weighing": "ಡಿಜಿಟಲ್ ಧರ್ಮಕಾಂಟಾ",
        "facilities": ["ಶುಂಠಿ ತೊಳೆಯುವ ಪ್ರಾಂಗಣ", "ಟ್ರಕ್ ಲೋಡಿಂಗ್"],
        "phone": "+91 8276 282140",
        "timings": "ಬೆಳಿಗ್ಗೆ 8:00 ರಿಂದ ಸಂಜೆ 5:30",
        "maps_url": "https://maps.google.com/?q=Somwarpet+APMC+Yard"
    },

    # --------------------------------------------------------------------------
    # 19. KOLAR DISTRICT (ಕೋಲಾರ)
    # --------------------------------------------------------------------------
    {
        "id": "kolar_tomato_apmc",
        "name_kn": "ಕೋಲಾರ ಪ್ರಧಾನ ಎಪಿಎಂಸಿ ಮಾರುಕಟ್ಟೆ ಪ್ರಾಂಗಣ (ಏಷ್ಯಾದ 2ನೇ ಅತಿದೊಡ್ಡ ಟೊಮೆಟೊ ಮಂಡಿ)",
        "name_en": "Kolar Principal APMC Yard (Asia's 2nd Largest Tomato Market)",
        "category": "apmc",
        "district": "Kolar",
        "taluk": "Kolar",
        "address": "ಬೆಂಗಳೂರು-ಚೆನ್ನೈ ಹೈವೇ, ಕೋಲಾರ - 563101",
        "crops_accepted": ["tomato", "green_chilli", "ragi", "potato"],
        "rates": {
            "tomato": 1950,
            "green_chilli": 3500,
            "ragi": 4320,
            "potato": 2050
        },
        "premium_vs_local": "+₹150 - ₹300 ದೆಹಲಿ/ಮುಂಬೈ/ಚೆನ್ನೈ ಸಗಟು ಖರೀದಿದಾರರ ಪೈಪೋಟಿ",
        "commission": "1.5% ನಿಯಂತ್ರಿತ",
        "payment_mode": "ಸ್ಥಳದಲ್ಲೇ ನಗದು / ತಕ್ಷಣದ UPI/NEFT",
        "weighing": "ಎಲೆಕ್ಟ್ರಾನಿಕ್ ಕ್ರೇಟ್ ತೂಕ",
        "facilities": ["ದೈನಂದಿನ ಹರಾಜು", "ಕೋಲ್ಡ್ ಸ್ಟೋರೇಜ್ ಹಬ್", "ಕ್ರೇಟ್ ವಿನಿಮಯ ಕೌಂಟರ್", "ರಾಷ್ಟ್ರೀಯ ಲಾರಿ ಸಾಗಣೆ ಸಂಪರ್ಕ"],
        "phone": "+91 8152 222148",
        "timings": "ಬೆಳಿಗ್ಗೆ 6:00 ರಿಂದ ಮಧ್ಯಾಹ್ನ 3:00",
        "maps_url": "https://maps.google.com/?q=Kolar+APMC+Tomato+Market"
    },
    {
        "id": "klr_srinivaspur_fpo",
        "name_kn": "ಶ್ರೀನಿವಾಸಪುರ ರೈತ ಉತ್ಪಾದಕ ಸಂಸ್ಥೆ (FPO) & ಟೊಮೆಟೊ-ಮಾವು ಮಂಡಿ",
        "name_en": "Srinivaspur Horticulture Farmers Producer Co (FPO)",
        "category": "fpo",
        "district": "Kolar",
        "taluk": "Srinivaspur",
        "address": "ಮದನಪಲ್ಲಿ ರಸ್ತೆ, ಶ್ರೀನಿವಾಸಪುರ, ಕೋಲಾರ - 563135",
        "crops_accepted": ["tomato", "ragi", "potato", "green_chilli"],
        "rates": {
            "tomato": 1980,
            "ragi": 4350,
            "potato": 2070,
            "green_chilli": 3530
        },
        "premium_vs_local": "+₹180 FPO ನೇರ ಖರೀದಿ ಪ್ರೀಮಿಯಂ",
        "commission": "0% (ಶೂನ್ಯ ಕಮಿಷನ್)",
        "payment_mode": "ನೇರ DBT ಬ್ಯಾಂಕ್ ವರ್ಗಾವಣೆ",
        "weighing": "ನಿಖರ ಡಿಜಿಟಲ್ ಸ್ಕೇಲ್",
        "facilities": ["ಶೂನ್ಯ ಕಮಿಷನ್", "ಕ್ರೇಟ್ ಸೌಲಭ್ಯ", "ತ್ವರಿತ ಅನ್‌ಲೋಡಿಂಗ್"],
        "phone": "+91 8157 245130",
        "timings": "ಬೆಳಿಗ್ಗೆ 6:30 ರಿಂದ ಮಧ್ಯಾಹ್ನ 3:30",
        "maps_url": "https://maps.google.com/?q=Srinivaspur+Farmers+Producer+Company"
    },

    # --------------------------------------------------------------------------
    # 20. KOPPAL DISTRICT (ಕೊಪ್ಪಳ)
    # --------------------------------------------------------------------------
    {
        "id": "kpl_gangavathi_rice",
        "name_kn": "ಗಂಗಾವತಿ ಭತ್ತ & ಅಕ್ಕಿ ಗಿರಣಿಗಳ ಬೃಹತ್ ಸಗಟು ಮಾರುಕಟ್ಟೆ (ಏಷ್ಯಾದ ಭತ್ತದ ಕಣಜ)",
        "name_en": "Gangavathi Mega Rice Millers & Paddy Trading Terminal",
        "category": "processor",
        "district": "Koppal",
        "taluk": "Gangavathi",
        "address": "ಸಿಂಧನೂರು ರಸ್ತೆ, ಗಂಗಾವತಿ, ಕೊಪ್ಪಳ - 583227",
        "crops_accepted": ["paddy", "maize", "cotton", "sunflower"],
        "rates": {
            "paddy": 2660,
            "maize": 2380,
            "cotton": 7860,
            "sunflower": 6280
        },
        "premium_vs_local": "+₹180 ಸೋನಾ ಮಸೂರಿ ಭತ್ತಕ್ಕೆ ರಾಜ್ಯದಲ್ಲೇ ಅತ್ಯುನ್ನತ ಮಿಲ್ ಬಿಡ್ಡಿಂಗ್",
        "commission": "0% (ಮಿಲ್ ನೇರ ಖರೀದಿ - ಶೂನ್ಯ ಕಮಿಷನ್)",
        "payment_mode": "ಸ್ಥಳದಲ್ಲೇ RTGS / NEFT (24 ಗಂಟೆ)",
        "weighing": "100% ಡಿಜಿಟಲ್ ಧರ್ಮಕಾಂಟಾ",
        "facilities": ["50+ ಭತ್ತದ ಗಿರಣಿಗಳ ನೇರ ಕೌಂಟರ್", "ಸ್ಪಾಟ್ ಪಾವತಿ", "ವೇಗದ ತೂಕ & ಅನ್‌ಲೋಡಿಂಗ್"],
        "phone": "+91 8533 230155",
        "timings": "ಬೆಳಿಗ್ಗೆ 8:00 ರಿಂದ ಸಂಜೆ 6:30",
        "maps_url": "https://maps.google.com/?q=Gangavathi+Rice+Mills+Koppal"
    },
    {
        "id": "kpl_apmc_main",
        "name_kn": "ಕೊಪ್ಪಳ ಪ್ರಧಾನ ಎಪಿಎಂಸಿ ಪ್ರಾಂಗಣ & ಶೇಂಗಾ-ಮೆಕ್ಕೆಜೋಳ ಮಂಡಿ",
        "name_en": "Koppal Principal APMC Yard & Oilseeds Market",
        "category": "apmc",
        "district": "Koppal",
        "taluk": "Koppal",
        "address": "ಹೊಸಪೇಟೆ ರಸ್ತೆ, ಕೊಪ್ಪಳ - 583231",
        "crops_accepted": ["groundnut", "jowar", "maize", "sunflower", "cotton"],
        "rates": {
            "groundnut": 7090,
            "jowar": 3790,
            "maize": 2350,
            "sunflower": 6260,
            "cotton": 7800
        },
        "premium_vs_local": "+₹160 ನಿಯಂತ್ರಿತ ಇ-ನಾಮ್ ಹರಾಜು ಲಾಭ",
        "commission": "1.5% APMC ಅಧಿಕೃತ",
        "payment_mode": "ಇ-ನಾಮ್ RTGS / ಬ್ಯಾಂಕ್ ಖಾತೆಗೆ",
        "weighing": "ಕಂಪ್ಯೂಟರೀಕೃತ ಧರ್ಮಕಾಂಟಾ",
        "facilities": ["ಇ-ನಾಮ್ ಹರಾಜು", "ಉಚಿತ ದಾಸ್ತಾನು ಶೆಡ್", "ರೈತ ಭವನ"],
        "phone": "+91 8539 220240",
        "timings": "ಬೆಳಿಗ್ಗೆ 8:00 ರಿಂದ ಸಂಜೆ 5:30",
        "maps_url": "https://maps.google.com/?q=APMC+Market+Yard+Koppal"
    },

    # --------------------------------------------------------------------------
    # 21. MANDYA DISTRICT (ಮಂಡ್ಯ)
    # --------------------------------------------------------------------------
    {
        "id": "mandya_jaggery_apmc",
        "name_kn": "ಮಂಡ್ಯ ಎಪಿಎಂಸಿ ಬೆಲ್ಲ & ಭತ್ತದ ಸಗಟು ಮಾರುಕಟ್ಟೆ ಪ್ರಾಂಗಣ",
        "name_en": "Mandya APMC Jaggery & Paddy Wholesale Yard",
        "category": "apmc",
        "district": "Mandya",
        "taluk": "Mandya",
        "address": "ಕೆ.ಆರ್. ಪೇಟೆ ರಸ್ತೆ, ಮಂಡ್ಯ - 571401",
        "crops_accepted": ["paddy", "sugarcane", "ragi", "banana"],
        "rates": {
            "paddy": 2600,
            "sugarcane": 3450,
            "ragi": 4360,
            "banana": 2350
        },
        "premium_vs_local": "+₹180 ಸ್ಥಳೀಯ ದಲ್ಲಾಳಿಗಳಿಗಿಂತ ಅಧಿಕ",
        "commission": "1.5% APMC ಅಧಿಕೃತ",
        "payment_mode": "ತಕ್ಷಣದ ನಗದು / ಬ್ಯಾಂಕ್ ಪಾವತಿ",
        "weighing": "ಡಿಜಿಟಲ್ ಧರ್ಮಕಾಂಟಾ",
        "facilities": ["ಶುದ್ಧ ಸಾವಯವ ಬೆಲ್ಲ ಪರೀಕ್ಷೆ", "ಭತ್ತದ ಗಿರಣಿ ನೇರ ಕೌಂಟರ್", "ಸಕ್ಕರೆ ಕಾರ್ಖಾನೆ ಟೋಕನ್ ಕೌಂಟರ್"],
        "phone": "+91 8232 224089",
        "timings": "ಬೆಳಿಗ್ಗೆ 8:00 ರಿಂದ ಸಂಜೆ 5:00",
        "maps_url": "https://maps.google.com/?q=APMC+Market+Yard+Mandya"
    },
    {
        "id": "maddur_coconut_hub",
        "name_kn": "ಮದ್ದೂರು ರಾಷ್ಟ್ರೀಯ ಎಳನೀರು & ತೆಂಗಿನಕಾಯಿ ವಹಿವಾಟು ಕೇಂದ್ರ",
        "name_en": "Maddur National Tender Coconut Wholesale Terminal",
        "category": "apmc",
        "district": "Mandya",
        "taluk": "Maddur",
        "address": "ಬೆಂಗಳೂರು-ಮೈಸೂರು ಎಕ್ಸ್‌ಪ್ರೆಸ್‌ವೇ, ಮದ್ದೂರು - 571428",
        "crops_accepted": ["coconut", "banana"],
        "rates": {
            "coconut": 29500,
            "banana": 2400
        },
        "premium_vs_local": "+₹3-5 ಪ್ರತಿ ಎಳನೀರಿಗೆ ಸ್ಥಳೀಯ ದಲ್ಲಾಳಿಗಳಿಗಿಂತ ಹೆಚ್ಚು",
        "commission": "1% ಮಾರುಕಟ್ಟೆ ಶುಲ್ಕ",
        "payment_mode": "ಸ್ಥಳದಲ್ಲೇ ನಗದು / ಬ್ಯಾಂಕ್ ಟ್ರಾನ್ಸ್‌ಫರ್",
        "weighing": "ಕೌಂಟ್ ಆಧಾರಿತ ಪರಿಶೀಲನೆ & ಗ್ರೇಡಿಂಗ್",
        "facilities": ["ಭಾರತದ ನಂ.1 ಎಳನೀರು ಮಾರುಕಟ್ಟೆ", "ಹೈದರಾಬಾದ್, ಮುಂಬೈ ನೇರ ಟ್ರಕ್ ಲೋಡಿಂಗ್", "ತಕ್ಷಣದ ನಗದು ಪಾವತಿ"],
        "phone": "+91 8232 232110",
        "timings": "ಬೆಳಿಗ್ಗೆ 6:00 ರಿಂದ ಸಂಜೆ 6:00",
        "maps_url": "https://maps.google.com/?q=Maddur+Coconut+Market"
    },

    # --------------------------------------------------------------------------
    # 22. MYSURU DISTRICT (ಮೈಸೂರು)
    # --------------------------------------------------------------------------
    {
        "id": "mys_bandipalya_apmc",
        "name_kn": "ಮೈಸೂರು ಬಂಡಿಪಾಳ್ಯ ಪ್ರಧಾನ ಎಪಿಎಂಸಿ ಪ್ರಾಂಗಣ (ದಕ್ಷಿಣ ಕರ್ನಾಟಕದ ಬೃಹತ್ ಮಂಡಿ)",
        "name_en": "Mysuru Bandipalya Principal APMC Yard",
        "category": "apmc",
        "district": "Mysuru",
        "taluk": "Mysuru",
        "address": "ಬಂಡಿಪಾಳ್ಯ, ಊಟಿ ರಸ್ತೆ, ಮೈಸೂರು - 570025",
        "crops_accepted": ["paddy", "ragi", "banana", "cotton", "sugarcane", "coconut"],
        "rates": {
            "paddy": 2620,
            "ragi": 4390,
            "banana": 2420,
            "cotton": 7820,
            "sugarcane": 3450,
            "coconut": 29600
        },
        "premium_vs_local": "+₹180 - ₹260 ಪ್ರವಾಸಿ ಮತ್ತು ಸಗಟು ನಗರದ ಅತ್ಯಧಿಕ ಬೇಡಿಕೆ",
        "commission": "1.5% APMC ನಿಯಂತ್ರಿತ",
        "payment_mode": "ಇ-ನಾಮ್ RTGS / ಬ್ಯಾಂಕ್ ಖಾತೆಗೆ",
        "weighing": "ಡಿಜಿಟಲ್ ಧರ್ಮಕಾಂಟಾ",
        "facilities": ["ಇ-ನಾಮ್ ಲೈವ್ ಬಿಡ್ಡಿಂಗ್", "ಬೃಹತ್ ಶೇಖರಣಾ ಗೋದಾಮುಗಳು", "ರೈತ ಭವನ"],
        "phone": "+91 821 2482340",
        "timings": "ಬೆಳಿಗ್ಗೆ 7:00 ರಿಂದ ಸಂಜೆ 6:00",
        "maps_url": "https://maps.google.com/?q=Bandipalya+APMC+Mysore"
    },
    {
        "id": "mys_nanjangud_banana",
        "name_kn": "ನಂಜನಗೂಡು ರಸಬಾಳೆ & ಕೃಷಿ ಉತ್ಪನ್ನಗಳ ಸಹಕಾರಿ ಖರೀದಿ ಕೇಂದ್ರ",
        "name_en": "Nanjangud Banana & Organic Growers Cooperative Center",
        "category": "fpo",
        "district": "Mysuru",
        "taluk": "Nanjangud",
        "address": "ಗುಂಡ್ಲುಪೇಟೆ ಮುಖ್ಯ ರಸ್ತೆ, ನಂಜನಗೂಡು, ಮೈಸೂರು - 571301",
        "crops_accepted": ["banana", "sugarcane", "ragi", "paddy"],
        "rates": {
            "banana": 2450,
            "sugarcane": 3470,
            "ragi": 4380,
            "paddy": 2600
        },
        "premium_vs_local": "+₹220 ಜಿಐ ಟ್ಯಾಗ್ (GI Tag) ರಸಬಾಳೆಗೆ ಪ್ರೀಮಿಯಂ ದರ",
        "commission": "0% (ಸಹಕಾರಿ ನೇರ ಖರೀದಿ)",
        "payment_mode": "ಸ್ಥಳದಲ್ಲೇ ನಗದು / ಬ್ಯಾಂಕ್ ವರ್ಗಾವಣೆ",
        "weighing": "ಪಾರದರ್ಶಕ ಎಲೆಕ್ಟ್ರಾನಿಕ್ ತಕ್ಕಡಿ",
        "facilities": ["ಜಿಐ ಪ್ರಮಾಣೀಕರಣ", "ಬಾಳೆ ಹಣ್ಣು ಗ್ರೇಡಿಂಗ್", "ಶೂನ್ಯ ಮಧ್ಯವರ್ತಿ"],
        "phone": "+91 8221 226150",
        "timings": "ಬೆಳಿಗ್ಗೆ 8:00 ರಿಂದ ಸಂಜೆ 5:00",
        "maps_url": "https://maps.google.com/?q=Nanjangud+Cooperative+Market+Mysore"
    },

    # --------------------------------------------------------------------------
    # 23. RAICHUR DISTRICT (ರಾಯಚೂರು)
    # --------------------------------------------------------------------------
    {
        "id": "rc_apmc_main",
        "name_kn": "ರಾಯಚೂರು ಪ್ರಧಾನ ಎಪಿಎಂಸಿ ಪ್ರಾಂಗಣ & ಇ-ನಾಮ್ ಟ್ರೇಡಿಂಗ್ ಕೇಂದ್ರ",
        "name_en": "Raichur Principal APMC Yard & e-NAM Trading Terminal",
        "category": "apmc",
        "district": "Raichur",
        "taluk": "Raichur",
        "address": "ಹೈದರಾಬಾದ್ ರಸ್ತೆ, ಕೃಷಿ ಮಾರುಕಟ್ಟೆ ಪ್ರಾಂಗಣ, ರಾಯಚೂರು - 584102",
        "crops_accepted": ["paddy", "cotton", "tur", "groundnut", "sunflower"],
        "rates": {
            "paddy": 2620,
            "cotton": 7850,
            "tur": 10750,
            "groundnut": 7050,
            "sunflower": 6250
        },
        "premium_vs_local": "+₹150 - ₹250 ಸ್ಥಳೀಯ ದಲ್ಲಾಳಿಗಳಿಗಿಂತ ಹೆಚ್ಚು",
        "commission": "1.5% APMC ನಿಯಂತ್ರಿತ ಶುಲ್ಕ (ಶೂನ್ಯ ಅನಧಿಕೃತ ಕಡಿತ)",
        "payment_mode": "ತಕ್ಷಣದ ಇ-ನಾಮ್ RTGS / ಬ್ಯಾಂಕ್ ವರ್ಗಾವಣೆ (24 ಗಂಟೆ)",
        "weighing": "ಸರ್ಕಾರಿ ಮುದ್ರೆಯುಳ್ಳ ಡಿಜಿಟಲ್ ಎಲೆಕ್ಟ್ರಾನಿಕ್ ಧರ್ಮಕಾಂಟಾ",
        "facilities": ["ಇ-ನಾಮ್ ಆನ್‌ಲೈನ್ ಬಿಡ್ಡಿಂಗ್", "ಉಚಿತ 3 ದಿನ ದಾಸ್ತಾನು ಶೆಡ್", "ತೇವಾಂಶ ಪರೀಕ್ಷಾ ಲ್ಯಾಬ್", "ರೈತ ವಿಶ್ರಾಂತಿ ಗೃಹ"],
        "phone": "+91 8532 235120",
        "timings": "ಬೆಳಿಗ್ಗೆ 8:00 ರಿಂದ ಸಂಜೆ 5:30 (ಸೋಮ - ಶನಿ)",
        "maps_url": "https://maps.google.com/?q=APMC+Market+Yard+Raichur"
    },
    {
        "id": "rc_kscmf_msp",
        "name_kn": "ಕರ್ನಾಟಕ ರಾಜ್ಯ ಸಹಕಾರ ಮಾರಾಟ ಮಹಾಮಂಡಳ (KSCMF) ಸರ್ಕಾರಿ ಬೆಂಬಲ ಬೆಲೆ ಖರೀದಿ ಕೇಂದ್ರ",
        "name_en": "KSCMF Govt MSP Procurement Depot, Raichur",
        "category": "msp",
        "district": "Raichur",
        "taluk": "Raichur",
        "address": "ಕೈಗಾರಿಕಾ ಪ್ರದೇಶ, ಮಾನ್ವಿ ರಸ್ತೆ, ರಾಯಚೂರು - 584103",
        "crops_accepted": ["paddy", "cotton", "sunflower", "soybean", "jowar"],
        "rates": {
            "paddy": 2320,
            "cotton": 7521,
            "sunflower": 7280,
            "soybean": 4892,
            "jowar": 3371
        },
        "premium_vs_local": "100% ಗ್ಯಾರಂಟಿ ಸರ್ಕಾರಿ MSP ಬೆಲೆ (ಸೂರ್ಯಕಾಂತಿಗೆ +₹1,130 ಹೆಚ್ಚು!)",
        "commission": "0% (ಸಂಪೂರ್ಣ ಶೂನ್ಯ ಕಮಿಷನ್ - ಮಧ್ಯವರ್ತಿ ರಹಿತ)",
        "payment_mode": "ನೇರ ಆಧಾರ್ ಲಿಂಕ್ಡ್ DBT ಬ್ಯಾಂಕ್ ಪಾವತಿ",
        "weighing": "ಸರ್ಕಾರಿ ಪರಿಶೀಲಿತ ಡಿಜಿಟಲ್ ತೂಕ",
        "facilities": ["100% ಶೂನ್ಯ ಕಮಿಷನ್", "ನೇರ ಖಾತೆಗೆ ಹಣ", "ಗುಣಮಟ್ಟ ಗ್ರೇಡಿಂಗ್", "FID/FRUITS ಪರಿಶೀಲನೆ"],
        "phone": "+91 8532 238411",
        "timings": "ಬೆಳಿಗ್ಗೆ 9:30 ರಿಂದ ಸಂಜೆ 5:00",
        "maps_url": "https://maps.google.com/?q=KSCMF+Procurement+Depot+Raichur"
    },
    {
        "id": "rc_sindhanur_paddy",
        "name_kn": "ಸಿಂಧನೂರು ಸೋನಾ ಮಸೂರಿ ಭತ್ತದ ಗಿರಣಿಗಳ ಕ್ಲಸ್ಟರ್ & ಸಗಟು ಖರೀದಿ ಪ್ರಾಂಗಣ",
        "name_en": "Sindhanur Sona Masoori Rice Millers Cluster & APMC Hub",
        "category": "processor",
        "district": "Raichur",
        "taluk": "Sindhanur",
        "address": "ಕುಷ್ಟಗಿ ರಸ್ತೆ, ಸಿಂಧನೂರು, ರಾಯಚೂರು - 584128",
        "crops_accepted": ["paddy", "cotton", "sunflower"],
        "rates": {
            "paddy": 2650,
            "cotton": 7880,
            "sunflower": 6290
        },
        "premium_vs_local": "+₹170 ಭತ್ತದ ನೇರ ಮಿಲ್ ರಫ್ತು ಪ್ರೀಮಿಯಂ",
        "commission": "0% (ಮಿಲ್ ನೇರ ಖರೀದಿ)",
        "payment_mode": "ಸ್ಪಾಟ್ RTGS / ಬ್ಯಾಂಕ್ ಖಾತೆಗೆ",
        "weighing": "ಕಂಪ್ಯೂಟರೀಕೃತ ಧರ್ಮಕಾಂಟಾ",
        "facilities": ["ಏಷ್ಯಾದ ಪ್ರಸಿದ್ಧ ಅಕ್ಕಿ ಗಿರಣಿಗಳು", "ಸ್ಪಾಟ್ ಪಾವತಿ"],
        "phone": "+91 8535 220330",
        "timings": "ಬೆಳಿಗ್ಗೆ 8:00 ರಿಂದ ಸಂಜೆ 6:00",
        "maps_url": "https://maps.google.com/?q=Sindhanur+Rice+Mills+Raichur"
    },

    # --------------------------------------------------------------------------
    # 24. RAMANAGARA DISTRICT (ರಾಮನಗರ)
    # --------------------------------------------------------------------------
    {
        "id": "rmn_apmc_main",
        "name_kn": "ರಾಮನಗರ ಪ್ರಧಾನ ಎಪಿಎಂಸಿ ಪ್ರಾಂಗಣ & ರಾಗಿ-ರೇಷ್ಮೆ ಮಂಡಿ",
        "name_en": "Ramanagara Principal APMC Yard & Farmers Terminal",
        "category": "apmc",
        "district": "Ramanagara",
        "taluk": "Ramanagara",
        "address": "ಐಜೂರು, ಬೆಂಗಳೂರು-ಮೈಸೂರು ಹೈವೇ, ರಾಮನಗರ - 562159",
        "crops_accepted": ["ragi", "tomato", "coconut", "banana"],
        "rates": {
            "ragi": 4380,
            "tomato": 1960,
            "coconut": 29500,
            "banana": 2390
        },
        "premium_vs_local": "+₹160 ರಾಜಧಾನಿ ಹೆದ್ದಾರಿ ವ್ಯಾಪಾರ ಸ್ಪರ್ಧೆ",
        "commission": "1.5% ನಿಯಂತ್ರಿತ",
        "payment_mode": "ಇ-ನಾಮ್ RTGS / UPI",
        "weighing": "ಡಿಜಿಟಲ್ ಧರ್ಮಕಾಂಟಾ",
        "facilities": ["ಎಕ್ಸ್‌ಪ್ರೆಸ್‌ವೇ ನೇರ ಸಂಪರ್ಕ", "ಶೇಖರಣಾ ಗೋದಾಮು"],
        "phone": "+91 80 2727 1410",
        "timings": "ಬೆಳಿಗ್ಗೆ 7:00 ರಿಂದ ಸಂಜೆ 5:00",
        "maps_url": "https://maps.google.com/?q=APMC+Ramanagara"
    },
    {
        "id": "rmn_channapatna_fpo",
        "name_kn": "ಚನ್ನಪಟ್ಟಣ ತೆಂಗು & ಹಣ್ಣುಗಳ ಸಹಕಾರಿ ಮಾರಾಟ ಕೇಂದ್ರ",
        "name_en": "Channapatna Coconut & Fruits Cooperative Market",
        "category": "fpo",
        "district": "Ramanagara",
        "taluk": "Channapatna",
        "address": "ಬಿ.ಎಂ. ರಸ್ತೆ, ಚನ್ನಪಟ್ಟಣ, ರಾಮನಗರ - 562160",
        "crops_accepted": ["coconut", "banana", "ragi", "tomato"],
        "rates": {
            "coconut": 29700,
            "banana": 2400,
            "ragi": 4370,
            "tomato": 1950
        },
        "premium_vs_local": "+₹190 ನೇರ ಸಹಕಾರಿ ಮಾರಾಟ ಬೋನಸ್",
        "commission": "0% (ಶೂನ್ಯ ಕಮಿಷನ್)",
        "payment_mode": "ಸ್ಥಳದಲ್ಲೇ ನಗದು / ಬ್ಯಾಂಕ್ ಖಾತೆಗೆ",
        "weighing": "ಪಾರದರ್ಶಕ ಎಲೆಕ್ಟ್ರಾನಿಕ್ ತಕ್ಕಡಿ",
        "facilities": ["ಶೂನ್ಯ ಕಮಿಷನ್", "ಎಳನೀರು & ಒಣಕೊಬ್ಬರಿ ಕೌಂಟರ್"],
        "phone": "+91 80 2725 2140",
        "timings": "ಬೆಳಿಗ್ಗೆ 7:30 ರಿಂದ ಸಂಜೆ 5:00",
        "maps_url": "https://maps.google.com/?q=Channapatna+APMC+Yard"
    },

    # --------------------------------------------------------------------------
    # 25. SHIVAMOGGA DISTRICT (ಶಿವಮೊಗ್ಗ)
    # --------------------------------------------------------------------------
    {
        "id": "shimoga_areca_apmc",
        "name_kn": "ಶಿವಮೊಗ್ಗ ಪ್ರಧಾನ ಎಪಿಎಂಸಿ ಅಡಿಕೆ & ಭತ್ತದ ಮಾರುಕಟ್ಟೆ ಪ್ರಾಂಗಣ",
        "name_en": "Shivamogga Principal APMC Arecanut & Paddy Yard",
        "category": "apmc",
        "district": "Shivamogga",
        "taluk": "Shivamogga",
        "address": "ಸಾಗರ ರಸ್ತೆ, ಶಿವಮೊಗ್ಗ - 577204",
        "crops_accepted": ["arecanut", "paddy", "ginger", "black_pepper"],
        "rates": {
            "arecanut": 55200,
            "paddy": 2570,
            "ginger": 5280,
            "black_pepper": 665
        },
        "premium_vs_local": "+₹600 - ₹1,200 ಅಡಿಕೆ ಗುಣಮಟ್ಟದ ಗ್ರೇಡಿಂಗ್ ಪ್ರೀಮಿಯಂ",
        "commission": "1.5% ಅಧಿಕೃತ ನಿಯಂತ್ರಿತ ಶುಲ್ಕ",
        "payment_mode": "ಕ್ಯಾಂಪ್ಕೋ / ಎಪಿಎಂಸಿ RTGS ನೇರ ಖಾತೆಗೆ",
        "weighing": "ಪಾರದರ್ಶಕ ಎಲೆಕ್ಟ್ರಾನಿಕ್ ತಕ್ಕಡಿ",
        "facilities": ["ರಾಶಿ/ಚಾಲಿ ಅಧಿಕೃತ ಗ್ರೇಡಿಂಗ್", "ಕ್ಯಾಂಪ್ಕೋ ಶಾಖೆ ಲಭ್ಯ", "ಸುರಕ್ಷಿತ ಉಗ್ರಾಣ ಸಾಲ"],
        "phone": "+91 8182 222950",
        "timings": "ಬೆಳಿಗ್ಗೆ 8:30 ರಿಂದ ಸಂಜೆ 5:30",
        "maps_url": "https://maps.google.com/?q=APMC+Market+Shimoga"
    },
    {
        "id": "smg_sagar_areca",
        "name_kn": "ಸಾಗರ ಬಿಳಿ & ಕೆಂಪು ಅಡಿಕೆ ಸಗಟು ಮಾರುಕಟ್ಟೆ ಪ್ರಾಂಗಣ",
        "name_en": "Sagar Arecanut & Spices Wholesale Trading Terminal",
        "category": "apmc",
        "district": "Shivamogga",
        "taluk": "Sagar",
        "address": "ಜೋಗ ರಸ್ತೆ, ಸಾಗರ, ಶಿವಮೊಗ್ಗ - 577401",
        "crops_accepted": ["arecanut", "ginger", "black_pepper", "paddy"],
        "rates": {
            "arecanut": 55600,
            "ginger": 5300,
            "black_pepper": 674,
            "paddy": 2580
        },
        "premium_vs_local": "+₹800 ಕೆಂಪು ಅಡಿಕೆಗೆ ಪ್ರಸಿದ್ಧ ಟೆಂಡರ್ ಹರಾಜು ದರ",
        "commission": "1.5% ನಿಯಂತ್ರಿತ",
        "payment_mode": "ಇ-ನಾಮ್ RTGS / ಬ್ಯಾಂಕ್ ವರ್ಗಾವಣೆ",
        "weighing": "ಡಿಜಿಟಲ್ ಧರ್ಮಕಾಂಟಾ",
        "facilities": ["ಅಡಿಕೆ ಗ್ರೇಡಿಂಗ್ ಲ್ಯಾಬ್", "ಕ್ಯಾಂಪ್ಕೋ ಖರೀದಿ ಕೌಂಟರ್"],
        "phone": "+91 8183 226120",
        "timings": "ಬೆಳಿಗ್ಗೆ 8:30 ರಿಂದ ಸಂಜೆ 5:00",
        "maps_url": "https://maps.google.com/?q=APMC+Sagar+Shimoga"
    },

    # --------------------------------------------------------------------------
    # 26. TUMAKURU DISTRICT (ತುಮಕೂರು)
    # --------------------------------------------------------------------------
    {
        "id": "tmk_apmc_main",
        "name_kn": "ತುಮಕೂರು ಪ್ರಧಾನ ಎಪಿಎಂಸಿ ಪ್ರಾಂಗಣ & ಕಲ್ಪತರು ಧಾನ್ಯ ಮಾರುಕಟ್ಟೆ",
        "name_en": "Tumakuru Principal APMC Yard & Food Grain Complex",
        "category": "apmc",
        "district": "Tumakuru",
        "taluk": "Tumakuru",
        "address": "ಬಟವಾಡಿ, ರಾಷ್ಟ್ರೀಯ ಹೆದ್ದಾರಿ 48, ತುಮಕೂರು - 572103",
        "crops_accepted": ["ragi", "groundnut", "maize", "coconut"],
        "rates": {
            "ragi": 4390,
            "groundnut": 7100,
            "maize": 2360,
            "coconut": 29700
        },
        "premium_vs_local": "+₹170 - ₹240 ರಾಜಧಾನಿ ಸಂಪರ್ಕದ ಹೆದ್ದಾರಿ ಪೈಪೋಟಿ",
        "commission": "1.5% APMC ನಿಯಂತ್ರಿತ",
        "payment_mode": "ಇ-ನಾಮ್ RTGS / ಬ್ಯಾಂಕ್ ವರ್ಗಾವಣೆ",
        "weighing": "ಡಿಜಿಟಲ್ ಧರ್ಮಕಾಂಟಾ",
        "facilities": ["ಇ-ನಾಮ್ ಹರಾಜು", "ಬೃಹತ್ ಕೊಬ್ಬರಿ & ರಾಗಿ ಗೋದಾಮು", "ರೈತ ಭವನ"],
        "phone": "+91 816 2281240",
        "timings": "ಬೆಳಿಗ್ಗೆ 8:00 ರಿಂದ ಸಂಜೆ 5:30",
        "maps_url": "https://maps.google.com/?q=Batawadi+APMC+Yard+Tumkur"
    },
    {
        "id": "tmk_tiptur_copra",
        "name_kn": "ತಿಪಟೂರು ಕೊಬ್ಬರಿ ಮಂಡಳಿ & ಕೊಬ್ಬರಿ ಸಗಟು ಮಾರುಕಟ್ಟೆ (ವಿಶ್ವವಿಖ್ಯಾತ ಕೊಬ್ಬರಿ ಕಣಜ)",
        "name_en": "Tiptur Copra Board & National Coconut Wholesale Terminal",
        "category": "apmc",
        "district": "Tumakuru",
        "taluk": "Tiptur",
        "address": "ಎಪಿಎಂಸಿ ಮಾರ್ಕೆಟ್ ಯಾರ್ಡ್, ತಿಪಟೂರು - 572201",
        "crops_accepted": ["coconut", "ragi", "groundnut"],
        "rates": {
            "coconut": 30200,
            "ragi": 4380,
            "groundnut": 7140
        },
        "premium_vs_local": "+₹500 - ₹1,200 ವಿಶ್ವವಿಖ್ಯಾತ ತಿಪಟೂರು ಉಂಡೆ ಕೊಬ್ಬರಿಗೆ ಗರಿಷ್ಠ ದರ",
        "commission": "1.5% ನಿಯಂತ್ರಿತ",
        "payment_mode": "ಇ-ನಾಮ್ RTGS / ನೇರ ಬ್ಯಾಂಕ್ ವರ್ಗಾವಣೆ",
        "weighing": "100% ಕಂಪ್ಯೂಟರೀಕೃತ ಡಿಜಿಟಲ್ ತೂಕ",
        "facilities": ["ಭಾರತದ ನಂ.1 ಉಂಡೆ ಕೊಬ್ಬರಿ ಮಾರುಕಟ್ಟೆ", "ಜಾಗತಿಕ ತೈಲ ಕಂಪನಿಗಳ ನೇರ ಬಿಡ್", "ಸೈಂಟಿಫಿಕ್ ಗ್ರೇಡಿಂಗ್ ಲ್ಯಾಬ್"],
        "phone": "+91 8134 251320",
        "timings": "ಬೆಳಿಗ್ಗೆ 7:30 ರಿಂದ ಸಂಜೆ 6:00",
        "maps_url": "https://maps.google.com/?q=Tiptur+APMC+Coconut+Market"
    },

    # --------------------------------------------------------------------------
    # 27. UDUPI DISTRICT (ಉಡುಪಿ)
    # --------------------------------------------------------------------------
    {
        "id": "udp_adi_udupi_apmc",
        "name_kn": "ಉಡುಪಿ ಆದಿ ಉಡುಪಿ ಪ್ರಧಾನ ಎಪಿಎಂಸಿ ಪ್ರಾಂಗಣ & ಕರಾವಳಿ ಕೃಷಿ ಮಂಡಿ",
        "name_en": "Udupi Adi Udupi Principal APMC Yard",
        "category": "apmc",
        "district": "Udupi",
        "taluk": "Udupi",
        "address": "ಆದಿ ಉಡುಪಿ, ಮಲ್ಪೆ ರಸ್ತೆ, ಉಡುಪಿ - 576103",
        "crops_accepted": ["paddy", "coconut", "arecanut", "black_pepper"],
        "rates": {
            "paddy": 2590,
            "coconut": 29700,
            "arecanut": 55800,
            "black_pepper": 676
        },
        "premium_vs_local": "+₹200 ಕರಾವಳಿ ಸಹಕಾರಿ ನಿಯಂತ್ರಿತ ದರ",
        "commission": "1.5% ನಿಯಂತ್ರಿತ",
        "payment_mode": "ಇ-ನಾಮ್ RTGS / ಬ್ಯಾಂಕ್ ಖಾತೆಗೆ",
        "weighing": "ಡಿಜಿಟಲ್ ಧರ್ಮಕಾಂಟಾ",
        "facilities": ["ಕರಾವಳಿ ತೋಟಗಾರಿಕೆ ಮಾರುಕಟ್ಟೆ", "ಕ್ಯಾಂಪ್ಕೋ ಕೌಂಟರ್"],
        "phone": "+91 820 2521140",
        "timings": "ಬೆಳಿಗ್ಗೆ 8:00 ರಿಂದ ಸಂಜೆ 5:00",
        "maps_url": "https://maps.google.com/?q=Adi+Udupi+APMC+Yard"
    },
    {
        "id": "udp_kundapura_planters",
        "name_kn": "ಕುಂದಾಪುರ ತೆಂಗು & ಅಡಿಕೆ ಬೆಳೆಗಾರರ ಸಹಕಾರಿ ಸಂಘ",
        "name_en": "Kundapura Coconut & Areca Planters Cooperative Society",
        "category": "fpo",
        "district": "Udupi",
        "taluk": "Kundapura",
        "address": "ರಾಷ್ಟ್ರೀಯ ಹೆದ್ದಾರಿ 66, ಕುಂದಾಪುರ, ಉಡುಪಿ - 576201",
        "crops_accepted": ["coconut", "arecanut", "paddy"],
        "rates": {
            "coconut": 29800,
            "arecanut": 55900,
            "paddy": 2600
        },
        "premium_vs_local": "+₹220 ಸಹಕಾರಿ ಬೋನಸ್ & ನೇರ ಖರೀದಿ ಲಾಭ",
        "commission": "0% (ಶೂನ್ಯ ಕಮಿಷನ್)",
        "payment_mode": "ಸ್ಥಳದಲ್ಲೇ ಬ್ಯಾಂಕ್ NEFT / RTGS",
        "weighing": "ಪಾರದರ್ಶಕ ಎಲೆಕ್ಟ್ರಾನಿಕ್ ತಕ್ಕಡಿ",
        "facilities": ["ಶೂನ್ಯ ಕಮಿಷನ್", "ವಾರ್ಷಿಕ ಬೋನಸ್", "ಉಗ್ರಾಣ ರಶೀದಿ ಸಾಲ"],
        "phone": "+91 8254 230410",
        "timings": "ಬೆಳಿಗ್ಗೆ 8:30 ರಿಂದ ಸಂಜೆ 5:00",
        "maps_url": "https://maps.google.com/?q=Kundapura+Planters+Cooperative"
    },

    # --------------------------------------------------------------------------
    # 28. UTTARA KANNADA DISTRICT (ಉತ್ತರ ಕನ್ನಡ)
    # --------------------------------------------------------------------------
    {
        "id": "sirsi_tss_hub",
        "name_kn": "ತೋಟಗಾರರ ಸಹಕಾರಿ ಮಾರಾಟ ಸಂಘ (TSS) ಲಿಮಿಟೆಡ್, ಸಿರ್ಸಿ",
        "name_en": "The Totgars' Cooperative Sale Society Ltd (TSS), Sirsi",
        "category": "fpo",
        "district": "Uttara Kannada",
        "taluk": "Sirsi",
        "address": "ಟಿಎಸ್‌ಎಸ್ ರಸ್ತೆ, ಸಿರ್ಸಿ, ಉತ್ತರ ಕನ್ನಡ - 581401",
        "crops_accepted": ["arecanut", "black_pepper", "cardamom"],
        "rates": {
            "arecanut": 56000,
            "black_pepper": 680,
            "cardamom": 2600
        },
        "premium_vs_local": "+₹800 - ₹1,500 ಪ್ರಸಿದ್ಧ ಟಿಎಸ್‌ಎಸ್ ಟೆಂಡರ್ ಹರಾಜು ಪದ್ಧತಿ",
        "commission": "1% ಸಹಕಾರಿ ಶುಲ್ಕ (ಬೋನಸ್ ಮರುಪಾವತಿ)",
        "payment_mode": "ಟಿಎಸ್‌ಎಸ್ ಬ್ಯಾಂಕ್ ಖಾತೆಗೆ ನೇರ ಕ್ರೆಡಿಟ್ / NEFT",
        "weighing": "100% ನಿಖರ ಸ್ವಿಸ್ ಎಲೆಕ್ಟ್ರಾನಿಕ್ ತಕ್ಕಡಿ",
        "facilities": ["ಏಷ್ಯಾದ ಅತ್ಯಂತ ವಿಶ್ವಾಸಾರ್ಹ ಮಸಾಲೆ ಸಹಕಾರಿ", "ಸೈಂಟಿಫಿಕ್ ಗ್ರೇಡಿಂಗ್", "ರೈತರಿಗೆ ರಿಯಾಯಿತಿ ಕೃಷಿ ಪರಿಕರ ಮಾರಾಟ"],
        "phone": "+91 8384 226251",
        "timings": "ಬೆಳಿಗ್ಗೆ 8:30 ರಿಂದ ಸಂಜೆ 5:00",
        "maps_url": "https://maps.google.com/?q=TSS+Society+Sirsi"
    },
    {
        "id": "uk_kumta_coastal",
        "name_kn": "ಕುಮಟಾ ತೆಂಗು & ಕರಾವಳಿ ಮಸಾಲೆ ಕೃಷಿ ಮಾರುಕಟ್ಟೆ",
        "name_en": "Kumta Coconut & Coastal Spices Trading Terminal",
        "category": "apmc",
        "district": "Uttara Kannada",
        "taluk": "Kumta",
        "address": "ಎಪಿಎಂಸಿ ಯಾರ್ಡ್, ಹೆಗಡೆ ರಸ್ತೆ, ಕುಮಟಾ - 581343",
        "crops_accepted": ["coconut", "black_pepper", "cardamom", "arecanut"],
        "rates": {
            "coconut": 29600,
            "black_pepper": 675,
            "cardamom": 2620,
            "arecanut": 55700
        },
        "premium_vs_local": "+₹190 ಕರಾವಳಿ ಮಸಾಲೆ ಗುಣಮಟ್ಟ ಪ್ರೀಮಿಯಂ",
        "commission": "1.5% ನಿಯಂತ್ರಿತ",
        "payment_mode": "ಇ-ನಾಮ್ RTGS / ಚೆಕ್",
        "weighing": "ಡಿಜಿಟಲ್ ಧರ್ಮಕಾಂಟಾ",
        "facilities": ["ಕರಾವಳಿ ಸಾಂಬಾರ ದಿನಸಿ ಮಂಡಿ", "ಉಗ್ರಾಣ ಶೆಡ್"],
        "phone": "+91 8386 222120",
        "timings": "ಬೆಳಿಗ್ಗೆ 8:00 ರಿಂದ ಸಂಜೆ 5:00",
        "maps_url": "https://maps.google.com/?q=APMC+Market+Kumta"
    },

    # --------------------------------------------------------------------------
    # 29. VIJAYANAGARA DISTRICT (ವಿಜಯನಗರ)
    # --------------------------------------------------------------------------
    {
        "id": "vjn_hosapete_apmc",
        "name_kn": "ಹೊಸಪೇಟೆ ಪ್ರಧಾನ ಎಪಿಎಂಸಿ ಪ್ರಾಂಗಣ & ತುಂಗಭದ್ರಾ ಬೆಳೆ ಮಂಡಿ",
        "name_en": "Hosapete Principal APMC Yard & Tungabhadra Agri Terminal",
        "category": "apmc",
        "district": "Vijayanagara",
        "taluk": "Hosapete",
        "address": "ಅಮರಾವತಿ ರಸ್ತೆ, ಹೊಸಪೇಟೆ, ವಿಜಯನಗರ - 583201",
        "crops_accepted": ["paddy", "sugarcane", "maize", "cotton", "sunflower"],
        "rates": {
            "paddy": 2610,
            "sugarcane": 3460,
            "maize": 2360,
            "cotton": 7820,
            "sunflower": 6260
        },
        "premium_vs_local": "+₹170 ತುಂಗಭದ್ರಾ ಆಯಕಟ್ಟು ಬೆಳೆಗಳಿಗೆ ಗರಿಷ್ಠ ಬೆಲೆ",
        "commission": "1.5% APMC ನಿಯಂತ್ರಿತ",
        "payment_mode": "ಇ-ನಾಮ್ RTGS / ಬ್ಯಾಂಕ್ ವರ್ಗಾವಣೆ",
        "weighing": "ಡಿಜಿಟಲ್ ಧರ್ಮಕಾಂಟಾ",
        "facilities": ["ಇ-ನಾಮ್ ಟ್ರೇಡಿಂಗ್", "ಸಕ್ಕರೆ ಕಾರ್ಖಾನೆ ಕನೆಕ್ಷನ್", "ಉಚಿತ ದಾಸ್ತಾನು"],
        "phone": "+91 8394 228140",
        "timings": "ಬೆಳಿಗ್ಗೆ 8:00 ರಿಂದ ಸಂಜೆ 5:30",
        "maps_url": "https://maps.google.com/?q=APMC+Market+Hosapete"
    },
    {
        "id": "vjn_harapanahalli_fpo",
        "name_kn": "ಹರಪನಹಳ್ಳಿ ಹತ್ತಿ & ಮೆಕ್ಕೆಜೋಳ ರೈತರ ಉತ್ಪಾದಕ ಸಂಘ (FPO)",
        "name_en": "Harapanahalli Cotton & Maize Farmers Producer Co",
        "category": "fpo",
        "district": "Vijayanagara",
        "taluk": "Harapanahalli",
        "address": "ಕೊಟ್ಟೂರು ರಸ್ತೆ, ಹರಪನಹಳ್ಳಿ, ವಿಜಯನಗರ - 583131",
        "crops_accepted": ["cotton", "maize", "groundnut", "sunflower"],
        "rates": {
            "cotton": 7840,
            "maize": 2370,
            "groundnut": 7080,
            "sunflower": 6280
        },
        "premium_vs_local": "+₹200 ಶೂನ್ಯ ದಲ್ಲಾಳಿ ಸಹಕಾರಿ ಲಾಭ",
        "commission": "0% (ಶೂನ್ಯ ಕಮಿಷನ್)",
        "payment_mode": "ನೇರ DBT ಬ್ಯಾಂಕ್ ಖಾತೆಗೆ",
        "weighing": "ಪಾರದರ್ಶಕ ಎಲೆಕ್ಟ್ರಾನಿಕ್ ತಕ್ಕಡಿ",
        "facilities": ["ಶೂನ್ಯ ಕಮಿಷನ್", "ಹತ್ತಿ ಜಿನ್ನಿಂಗ್ ಲಿಂಕ್", "ರೈತ ಸೇವಾ ಕೇಂದ್ರ"],
        "phone": "+91 8398 251120",
        "timings": "ಬೆಳಿಗ್ಗೆ 8:30 ರಿಂದ ಸಂಜೆ 5:00",
        "maps_url": "https://maps.google.com/?q=Harapanahalli+Farmers+Cooperative"
    },

    # --------------------------------------------------------------------------
    # 30. VIJAYAPURA DISTRICT (ವಿಜಯಪುರ)
    # --------------------------------------------------------------------------
    {
        "id": "vijayapura_apmc_main",
        "name_kn": "ವಿಜಯಪುರ ಪ್ರಧಾನ ಎಪಿಎಂಸಿ ಪ್ರಾಂಗಣ & ಒಣದ್ರಾಕ್ಷಿ (ರೈಸಿನ್) ಟ್ರೇಡಿಂಗ್ ಕಾಂಪ್ಲೆಕ್ಸ್",
        "name_en": "Vijayapura Principal APMC Yard & Raisin Trading Complex",
        "category": "apmc",
        "district": "Vijayapura",
        "taluk": "Vijayapura",
        "address": "ಸಿಂದಗಿ ರಸ್ತೆ, ವಿಜಯಪುರ - 586101",
        "crops_accepted": ["jowar", "bengal_gram", "tur", "maize", "soybean"],
        "rates": {
            "jowar": 3850,
            "bengal_gram": 6600,
            "tur": 10700,
            "maize": 2320,
            "soybean": 4750
        },
        "premium_vs_local": "+₹150 ಮಾಲ್ದಂಡಿ ಜೋಳ ಮತ್ತು ಕಡಲೆಗೆ ಗರಿಷ್ಠ ಬೆಲೆ",
        "commission": "1.5% ಅಧಿಕೃತ ಶುಲ್ಕ",
        "payment_mode": "ಇ-ನಾಮ್ RTGS ನೇರ ಬ್ಯಾಂಕ್ ವರ್ಗಾವಣೆ",
        "weighing": "ಡಿಜಿಟಲ್ ಧರ್ಮಕಾಂಟಾ",
        "facilities": ["ಮಾಲ್ದಂಡಿ ಜೋಳದ ವಿಶೇಷ ಮಾರುಕಟ್ಟೆ", "ಒಣದ್ರಾಕ್ಷಿ ಕೋಲ್ಡ್ ಸ್ಟೋರೇಜ್", "ಇ-ನಾಮ್ ಟ್ರೇಡಿಂಗ್"],
        "phone": "+91 8352 250123",
        "timings": "ಬೆಳಿಗ್ಗೆ 8:00 ರಿಂದ ಸಂಜೆ 5:30",
        "maps_url": "https://maps.google.com/?q=APMC+Market+Yard+Vijayapura"
    },
    {
        "id": "vjp_indi_jowar",
        "name_kn": "ಇಂಡಿ ಮಾಲ್ದಂಡಿ ಜೋಳ & ದ್ವಿದಳ ಧಾನ್ಯಗಳ ಸಗಟು ಖರೀದಿ ಪ್ರಾಂಗಣ",
        "name_en": "Indi Maldandi Jowar & Pulses Wholesale APMC Sub-Yard",
        "category": "apmc",
        "district": "Vijayapura",
        "taluk": "Indi",
        "address": "ರೈಲ್ವೆ ಸ್ಟೇಷನ್ ರಸ್ತೆ, ಇಂಡಿ, ವಿಜಯಪುರ - 586209",
        "crops_accepted": ["jowar", "bengal_gram", "tur", "maize"],
        "rates": {
            "jowar": 3880,
            "bengal_gram": 6640,
            "tur": 10750,
            "maize": 2340
        },
        "premium_vs_local": "+₹180 ಜಿಐ ಟ್ಯಾಗ್ ಮಾಲ್ದಂಡಿ ಜೋಳಕ್ಕೆ ಅತ್ಯುನ್ನತ ಮಹಾರಾಷ್ಟ್ರ ಗಡಿ ದರ",
        "commission": "1.5% ನಿಯಂತ್ರಿತ",
        "payment_mode": "ಇ-ನಾಮ್ RTGS / ಚೆಕ್",
        "weighing": "ಕಂಪ್ಯೂಟರೀಕೃತ ಧರ್ಮಕಾಂಟಾ",
        "facilities": ["ಮಾಲ್ದಂಡಿ ಜೋಳದ ವಿಶೇಷ ಟ್ರೇಡಿಂಗ್", "ಉಚಿತ ಶೇಖರಣಾ ಶೆಡ್"],
        "phone": "+91 8359 225130",
        "timings": "ಬೆಳಿಗ್ಗೆ 8:00 ರಿಂದ ಸಂಜೆ 5:00",
        "maps_url": "https://maps.google.com/?q=APMC+Yard+Indi+Vijayapura"
    },

    # --------------------------------------------------------------------------
    # 31. YADGIR DISTRICT (ಯಾದಗಿರಿ)
    # --------------------------------------------------------------------------
    {
        "id": "ydg_apmc_main",
        "name_kn": "ಯಾದಗಿರಿ ಪ್ರಧಾನ ಎಪಿಎಂಸಿ ಪ್ರಾಂಗಣ & ಹತ್ತಿ ಗಂಜ್",
        "name_en": "Yadgir Principal APMC Yard & Cotton Gunj",
        "category": "apmc",
        "district": "Yadgir",
        "taluk": "Yadgir",
        "address": "ಚಿತ್ತಾಪುರ ರಸ್ತೆ, ಯಾದಗಿರಿ - 585202",
        "crops_accepted": ["cotton", "paddy", "tur", "jowar", "bengal_gram"],
        "rates": {
            "cotton": 7840,
            "paddy": 2600,
            "tur": 10780,
            "jowar": 3820,
            "bengal_gram": 6620
        },
        "premium_vs_local": "+₹190 ಜಿನ್ನಿಂಗ್ ಮಿಲ್‌ಗಳಿಂದ ನೇರ ಸ್ಪರ್ಧಾತ್ಮಕ ಹರಾಜು",
        "commission": "1.5% APMC ನಿಯಂತ್ರಿತ",
        "payment_mode": "ಇ-ನಾಮ್ RTGS / ಬ್ಯಾಂಕ್ ವರ್ಗಾವಣೆ",
        "weighing": "ಡಿಜಿಟಲ್ ಧರ್ಮಕಾಂಟಾ",
        "facilities": ["ಹತ್ತಿ ತೇವಾಂಶ ಲ್ಯಾಬ್", "ಇ-ನಾಮ್ ಲೈವ್ ಬಿಡ್ಡಿಂಗ್", "ರೈತ ವಿಶ್ರಾಂತಿ ನಿಲಯ"],
        "phone": "+91 8473 251140",
        "timings": "ಬೆಳಿಗ್ಗೆ 8:00 ರಿಂದ ಸಂಜೆ 5:30",
        "maps_url": "https://maps.google.com/?q=APMC+Yard+Yadgir"
    },
    {
        "id": "ydg_shahapur_msp",
        "name_kn": "ಶಹಾಪುರ ತೊಗರಿ & ಭತ್ತದ ನೇರ ಖರೀದಿ ಕೇಂದ್ರ & ದಾಲ್ ಮಿಲ್ ಕ್ಲಸ್ಟರ್",
        "name_en": "Shahapur Tur & Paddy Direct Procurement Hub & Dal Mill Cluster",
        "category": "processor",
        "district": "Yadgir",
        "taluk": "Shahapur",
        "address": "ಸುರಪುರ-ಶಹಾಪುರ ಮುಖ್ಯ ರಸ್ತೆ, ಶಹಾಪುರ, ಯಾದಗಿರಿ - 585223",
        "crops_accepted": ["tur", "paddy", "cotton", "jowar"],
        "rates": {
            "tur": 10840,
            "paddy": 2630,
            "cotton": 7850,
            "jowar": 3830
        },
        "premium_vs_local": "+₹220 ದಾಲ್ ಮಿಲ್ ನೇರ ಖರೀದಿ ಬೋನಸ್",
        "commission": "0% (ಮಿಲ್ ನೇರ ಖರೀದಿ - ಶೂನ್ಯ ಕಮಿಷನ್)",
        "payment_mode": "ಸ್ಥಳದಲ್ಲೇ RTGS / NEFT (24 ಗಂಟೆ)",
        "weighing": "ಕಂಪ್ಯೂಟರೀಕೃತ ಡಿಜಿಟಲ್ ತೂಕ",
        "facilities": ["ದಾಲ್ ಮಿಲ್ ಕ್ಲಸ್ಟರ್", "ಸ್ಪಾಟ್ ಪಾವತಿ", "ಶೂನ್ಯ ಕಮಿಷನ್"],
        "phone": "+91 8473 242130",
        "timings": "ಬೆಳಿಗ್ಗೆ 8:30 ರಿಂದ ಸಂಜೆ 6:00",
        "maps_url": "https://maps.google.com/?q=Shahapur+APMC+Yard+Yadgir"
    }
]




# ==============================================================================
# 3. HELPER FUNCTIONS FOR FILTERING, SORTING & QUERYING
# ==============================================================================

def get_all_crops():
    """Return all crops with basic metadata."""
    return list(CROPS_MARKET_DATA.values())


def get_crop_data(crop_id):
    """Return detailed market intelligence for a single crop."""
    return CROPS_MARKET_DATA.get(crop_id, CROPS_MARKET_DATA["paddy"])


def get_selling_centers(crop_id=None, district=None, category=None, sort_by="highest_rate", search_query=None):
    """
    Filter and sort selling centers based on crop, district, category, and criteria.
    sort_by options:
    - 'highest_rate': Center paying highest price for the selected crop first
    - 'district': Alphabetical by district
    - 'zero_commission': Centers with 0% commission (MSP / Direct Processors / FPO) first
    """
    results = list(SELLING_CENTERS)

    # 1. Filter by crop
    if crop_id and crop_id != "all":
        results = [c for c in results if crop_id in c["crops_accepted"]]

    # 2. Filter by district
    if district and district != "All":
        results = [c for c in results if c["district"].strip().lower() == district.strip().lower()]

    # 3. Filter by category
    if category and category != "all":
        results = [c for c in results if c["category"] == category]

    # 4. Search query (by town, taluk, center/shop name)
    if search_query and search_query.strip():
        q = search_query.strip().lower()
        results = [
            c for c in results
            if q in c["name_en"].lower()
            or q in c["name_kn"].lower()
            or q in c["taluk"].lower()
            or q in c["district"].lower()
            or q in c["address"].lower()
        ]

    # 4. Sorting logic
    if sort_by == "highest_rate" and crop_id and crop_id != "all":
        # Sort by buying rate for the chosen crop descending
        results.sort(key=lambda c: c.get("rates", {}).get(crop_id, 0), reverse=True)
    elif sort_by == "zero_commission":
        # Centers with 0% commission first
        results.sort(key=lambda c: (0 if "0%" in c["commission"] or c["category"] == "msp" else 1, c["district"]))
    else:
        # Default: by district then name
        results.sort(key=lambda c: (c["district"], c["name_en"]))

    return results

