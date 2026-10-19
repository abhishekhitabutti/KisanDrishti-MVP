"""
Scientific Borewell Water Depth & Feasibility Estimation Engine for Karnataka.
Combines Government India-WRIS (Water Resources Information System) / CGWB observation stations,
GPS mobile coordinates, Inverse Distance Weighting (IDW), topography, and empirical local ground truth.
URL: https://indiawris.gov.in/wris/#/groundWater
"""
import math
from groundwater_data import KARNATAKA_GROUNDWATER
from wris_groundwater_data import WRIS_STATIONS
from districts import DISTRICTS


def haversine_distance_km(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    """Calculate the great circle distance in kilometers between two GPS points."""
    R = 6371.0  # Earth's radius in kilometers
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = (math.sin(dlat / 2) ** 2 +
         math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) *
         math.sin(dlon / 2) ** 2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return round(R * c, 2)


def get_nearest_wris_stations(lat: float, lon: float, top_k: int = 3):
    """Find the top_k nearest India-WRIS / CGWB National Hydrograph observation stations."""
    stations_with_dist = []
    for s in WRIS_STATIONS:
        d = haversine_distance_km(lat, lon, s["lat"], s["lon"])
        item = dict(s)
        item["distance_km"] = d
        stations_with_dist.append(item)
    stations_with_dist.sort(key=lambda x: x["distance_km"])
    return stations_with_dist[:top_k]


def calculate_borewell_feasibility(
    district: str,
    topography: str = "plain",
    nearby_working: int = 1,
    nearby_dry: int = 0,
    has_water_body: bool = False,
    soil_type: str = "red",
    custom_lat: float = None,
    custom_lon: float = None,
) -> dict:
    """
    Calculate scientific groundwater strike depth range, assurance score,
    expected water discharge force (in inches and LPM), and budgeting.
    Integrates live India-WRIS / CGWB station hydrogeological records.
    """
    data = KARNATAKA_GROUNDWATER.get(district)
    if not data:
        data = KARNATAKA_GROUNDWATER["Dharwad"]

    # Resolve GPS Coordinates (use custom lat/lon if provided, else district headquarters)
    if custom_lat is not None and custom_lon is not None:
        user_lat, user_lon = float(custom_lat), float(custom_lon)
    else:
        user_lat, user_lon = DISTRICTS.get(district, (15.46, 75.01))

    # Fetch 3 nearest India-WRIS observation stations
    nearest_stations = get_nearest_wris_stations(user_lat, user_lon, top_k=3)
    primary_station = nearest_stations[0]

    # Spatial Inverse Distance Weighting (IDW) for water table and recharge trends
    weights = [1.0 / max(1.0, s["distance_km"]) for s in nearest_stations]
    total_w = sum(weights)
    norm_w = [w / total_w for w in weights]

    interp_dtw_pre_m = sum(nw * s["water_level_pre_m"] for nw, s in zip(norm_w, nearest_stations))
    interp_dtw_post_m = sum(nw * s["water_level_post_m"] for nw, s in zip(norm_w, nearest_stations))
    interp_trend_m_yr = sum(nw * s["decadal_trend_m_yr"] for nw, s in zip(norm_w, nearest_stations))

    # Depth Bounds
    min_base_ft, max_base_ft, hard_stop_base_ft = primary_station["strike_depth_ft"]
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

    est_min_ft = max(60, est_min_ft)
    est_max_ft = max(est_min_ft + 80, est_max_ft)

    # 6. Scientific Assurance Score (ಖಾತರಿ ಪ್ರಮಾಣ %)
    # Base assurance reflects distance to monitored government well & historical trend
    dist_km = primary_station["distance_km"]
    if dist_km <= 5.0:
        dist_confidence = 82
    elif dist_km <= 15.0:
        dist_confidence = 74
    else:
        dist_confidence = 65

    trend_bonus = +8 if interp_trend_m_yr > 0 else (-12 if interp_trend_m_yr < -0.15 else -4)
    recharge_delta = interp_dtw_pre_m - interp_dtw_post_m
    recharge_bonus = +6 if recharge_delta >= 4.0 else 0

    calc_assurance = (dist_confidence + trend_bonus + recharge_bonus +
                      topo_prob + water_prob + working_bonus - dry_penalty)
    final_assurance = max(18, min(94, calc_assurance))

    # Assurance Category
    if final_assurance >= 72:
        assurance_category = "High Assurance"
        assurance_category_kn = "ಉತ್ತಮ ವೈಜ್ಞಾನಿಕ ಖಾತರಿ {High Assurance}"
        assurance_color = "green"
    elif final_assurance >= 50:
        assurance_category = "Moderate Assurance"
        assurance_category_kn = "ಸಾಧಾರಣ ಖಾತರಿ {Moderate Assurance}"
        assurance_color = "orange"
    else:
        assurance_category = "High Financial Risk"
        assurance_category_kn = "ಅಧಿಕ ಆರ್ಥಿಕ ಅಪಾಯ {High Risk}"
        assurance_color = "red"

    # 7. Water Force & Discharge (ಜಲಬಲ ಮತ್ತು ಇಂಚುಗಳಲ್ಲಿ ಹೊರಹರಿವು)
    yield_inches = primary_station["yield_inches"]
    yield_lpm = primary_station["yield_lpm"]
    rec_pump_hp = primary_station["rec_pump_hp"]

    # Adjust discharge force if multiple dry wells or upland
    if nearby_dry >= 2 or topography == "upland":
        yield_force_category = "Low Force"
        yield_force_kn = f"{yield_inches} ಇಂಚು (ಕಡಿಮೆ ಜಲಬಲ)"
        drip_capacity_acres = "1.0 - 1.5 acres drip irrigation"
        drip_capacity_acres_kn = "1.0 - 1.5 ಎಕರೆ ಹನಿ ನೀರಾವರಿ"
    elif final_assurance >= 70:
        yield_force_category = "Strong Force"
        yield_force_kn = f"{yield_inches} ಇಂಚು (ಉತ್ತಮ ಜಲಬಲ)"
        drip_capacity_acres = "3.0 - 4.5 acres drip irrigation"
        drip_capacity_acres_kn = "3.0 - 4.5 ಎಕರೆ ಹನಿ ನೀರಾವರಿ"
    else:
        yield_force_category = "Moderate Force"
        yield_force_kn = f"{yield_inches} ಇಂಚು (ಸಾಧಾರಣ ಜಲಬಲ)"
        drip_capacity_acres = "2.0 - 2.5 acres drip irrigation"
        drip_capacity_acres_kn = "2.0 - 2.5 ಎಕರೆ ಹನಿ ನೀರಾವರಿ"

    # 8. Financial Budget (Karnataka drilling rates)
    cost_drilling_min = est_min_ft * 95
    cost_drilling_max = est_max_ft * 115
    cost_casing_min = casing_ft * 390
    cost_casing_max = casing_ft * 450
    cost_pump_min = 45000
    cost_pump_max = 65000

    total_cost_min = cost_drilling_min + cost_casing_min + cost_pump_min
    total_cost_max = cost_drilling_max + cost_casing_max + cost_pump_max

    # 9. Summer Drying Risk
    summer_drop_m = round(primary_station["water_level_pre_m"] - primary_station["water_level_post_m"], 1)
    summer_drop_ft = int(summer_drop_m * 3.28)

    if summer_drop_ft >= 35 or data["status"] in ("Critical", "Over-Exploited"):
        summer_risk = "High"
        summer_risk_kn = f"ಹೆಚ್ಚು (ಬೇಸಿಗೆಯಲ್ಲಿ ~{summer_drop_ft} ಅಡಿ ನೀರು ಕುಸಿಯುವ ಅಪಾಯ)"
    elif summer_drop_ft >= 20:
        summer_risk = "Moderate"
        summer_risk_kn = f"ಸಾಧಾರಣ (ಬೇಸಿಗೆಯಲ್ಲಿ ~{summer_drop_ft} ಅಡಿ ಕುಸಿಯಬಹುದು)"
    else:
        summer_risk = "Low"
        summer_risk_kn = "ಕಡಿಮೆ (ಸುಸ್ಥಿರ ನೈಸರ್ಗಿಕ ಮರುಪೂರಣ)"

    return {
        "district": district,
        "user_lat": user_lat,
        "user_lon": user_lon,
        "primary_station": primary_station,
        "nearest_stations": nearest_stations,
        "distance_to_station_km": dist_km,
        "cgwb_status": data["status"],
        "cgwb_status_kn": data["status_kn"],
        "extraction_pct": data["extraction_pct"],
        "aquifer_type": primary_station["aquifer_rock"],
        "aquifer_type_kn": primary_station["aquifer_rock"],
        "est_min_ft": est_min_ft,
        "est_max_ft": est_max_ft,
        "hard_stop_ft": hard_stop_ft,
        "casing_ft": casing_ft,
        "final_prob": final_assurance,
        "prob_category": assurance_category,
        "prob_category_kn": assurance_category_kn,
        "prob_color": assurance_color,
        "yield_inches": yield_inches,
        "yield_lpm": yield_lpm,
        "yield_force_category": yield_force_category,
        "yield_force_kn": yield_force_kn,
        "rec_pump_hp": rec_pump_hp,
        "drip_capacity_acres": drip_capacity_acres,
        "drip_capacity_acres_kn": drip_capacity_acres_kn,
        "interp_dtw_pre_m": round(interp_dtw_pre_m, 1),
        "interp_dtw_post_m": round(interp_dtw_post_m, 1),
        "interp_trend_m_yr": round(interp_trend_m_yr, 3),
        "summer_drop_ft": summer_drop_ft,
        "summer_risk": summer_risk,
        "summer_risk_kn": summer_risk_kn,
        "total_cost_min": total_cost_min,
        "total_cost_max": total_cost_max,
        "notes_en": data["notes_en"],
        "notes_kn": data["notes_kn"],
    }
