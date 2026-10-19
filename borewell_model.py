"""Scientific Borewell Water Depth & Feasibility Estimation Engine for Karnataka.
Combines CGWB hydrogeological data, topography, soil characteristics, and empirical neighbor outcomes.
"""
from groundwater_data import KARNATAKA_GROUNDWATER


def calculate_borewell_feasibility(
    district: str,
    topography: str = "plain",
    nearby_working: int = 1,
    nearby_dry: int = 0,
    has_water_body: bool = False,
    soil_type: str = "red",
) -> dict:
    """Calculate groundwater depth range, feasibility score, financial cost estimate, and safety advisories.
    
    Parameters:
        district: District name in Karnataka
        topography: "valley", "plain", or "upland"
        nearby_working: Number of functioning borewells within 500m (0 to 5)
        nearby_dry: Number of failed or dry borewells within 500m (0 to 5)
        has_water_body: True if stream, pond, lake or irrigation canal exists within 500m
        soil_type: "red", "black", "laterite", or "alluvial"
    """
    data = KARNATAKA_GROUNDWATER.get(district)
    if not data:
        data = KARNATAKA_GROUNDWATER["Dharwad"]  # safe fallback

    min_base_ft, max_base_ft, hard_stop_base_ft = data["depth_range_ft"]
    base_prob = data["base_probability"]
    casing_base_ft = data["casing_depth_ft"]

    # 1. Topography Adjustments
    topo_factor = 1.0
    topo_prob = 0
    if topography == "valley":
        topo_factor = 0.85
        topo_prob = +12
    elif topography == "upland":
        topo_factor = 1.25
        topo_prob = -18

    # 2. Surface Water Proximity (within 500m)
    water_factor = 0.92 if has_water_body else 1.0
    water_prob = +10 if has_water_body else 0

    # 3. Soil Casing Requirements
    casing_ft = casing_base_ft
    if soil_type == "black":
        casing_ft += 25
    elif soil_type == "alluvial":
        casing_ft += 35
    elif soil_type == "laterite":
        casing_ft = max(30, casing_ft - 15)

    # 4. Empirical Local Evidence (Nearby Working vs Dry Wells)
    working_bonus = min(nearby_working * 5, 15)
    dry_penalty = min(nearby_dry * 12, 36)
    dry_depth_penalty = 1.12 if nearby_dry >= 2 else 1.0

    # 5. Estimated Depth Range
    est_min_ft = int(min_base_ft * topo_factor * water_factor)
    est_max_ft = int(max_base_ft * topo_factor * dry_depth_penalty)
    hard_stop_ft = int(hard_stop_base_ft * (1.15 if topography == "upland" else 1.0))

    # Ensure logical bounds
    est_min_ft = max(60, est_min_ft)
    est_max_ft = max(est_min_ft + 80, est_max_ft)

    # 6. Final Probability Score (bounded 15% to 92%)
    calc_prob = base_prob + topo_prob + water_prob + working_bonus - dry_penalty
    final_prob = max(15, min(92, calc_prob))

    # Probability Category
    if final_prob >= 72:
        prob_category = "High"
        prob_category_kn = "ಉತ್ತಮ ಸಂಭವನೀಯತೆ {High}"
        prob_color = "green"
    elif final_prob >= 48:
        prob_category = "Moderate"
        prob_category_kn = "ಸಾಧಾರಣ ಸಂಭವನೀಯತೆ {Moderate}"
        prob_color = "orange"
    else:
        prob_category = "High Risk"
        prob_category_kn = "ಹೆಚ್ಚು ಅಪಾಯಕಾರಿ {High Risk}"
        prob_color = "red"

    # 7. Financial Cost Estimation (Karnataka market drilling rates)
    # Drilling: ₹95 - ₹115/ft, Casing pipe (heavy PVC/MS): ₹390 - ₹450/ft, Pump & elect: ₹45,000 - ₹65,000
    cost_drilling_min = est_min_ft * 95
    cost_drilling_max = est_max_ft * 115
    cost_casing_min = casing_ft * 390
    cost_casing_max = casing_ft * 450
    cost_pump_min = 45000
    cost_pump_max = 65000

    total_cost_min = cost_drilling_min + cost_casing_min + cost_pump_min
    total_cost_max = cost_drilling_max + cost_casing_max + cost_pump_max

    # 8. Summer Drying Risk
    summer_drop = data["summer_drop_ft"]
    if summer_drop >= 40 or data["status"] in ("Critical", "Over-Exploited"):
        summer_risk = "High"
        summer_risk_kn = "ಹೆಚ್ಚು (ಬೇಸಿಗೆಯಲ್ಲಿ ನೀರು ತೀವ್ರ ಕುಸಿಯುವ ಅಪಾಯ)"
    elif summer_drop >= 25:
        summer_risk = "Moderate"
        summer_risk_kn = "ಸಾಧಾರಣ (ಬೇಸಿಗೆಯಲ್ಲಿ 20-30 ಅಡಿ ಕುಸಿಯಬಹುದು)"
    else:
        summer_risk = "Low"
        summer_risk_kn = "ಕಡಿಮೆ (ಸುಸ್ಥಿರ ನೈಸರ್ಗಿಕ ಮರುಪೂರಣ)"

    return {
        "district": district,
        "cgwb_status": data["status"],
        "cgwb_status_kn": data["status_kn"],
        "extraction_pct": data["extraction_pct"],
        "aquifer_type": data["aquifer_type"],
        "aquifer_type_kn": data["aquifer_type_kn"],
        "est_min_ft": est_min_ft,
        "est_max_ft": est_max_ft,
        "hard_stop_ft": hard_stop_ft,
        "casing_ft": casing_ft,
        "final_prob": final_prob,
        "prob_category": prob_category,
        "prob_category_kn": prob_category_kn,
        "prob_color": prob_color,
        "summer_drop_ft": summer_drop,
        "summer_risk": summer_risk,
        "summer_risk_kn": summer_risk_kn,
        "total_cost_min": total_cost_min,
        "total_cost_max": total_cost_max,
        "notes_en": data["notes_en"],
        "notes_kn": data["notes_kn"],
    }

