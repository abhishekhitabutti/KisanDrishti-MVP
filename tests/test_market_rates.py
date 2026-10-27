"""Unit tests for the APMC Market Rates & Best Price Selling Centers module."""
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from streamlit.testing.v1 import AppTest
from districts import DISTRICTS
import mandi_data


def test_mandi_crops_data_integrity():
    crops = mandi_data.get_all_crops()
    assert len(crops) >= 20
    for crop in crops:
        assert "id" in crop
        assert "name_kn" in crop
        assert "name_en" in crop
        assert "today_modal" in crop
        assert crop["today_modal"] > 0
        assert "avg_30d" in crop
        assert crop["avg_30d"] > 0
        assert "trend" in crop
        assert crop["trend"] in ("up", "down", "stable")
        assert "verdict_type" in crop
        assert crop["verdict_type"] in ("sell_now", "hold", "sell_msp")


def test_mandi_history_and_prediction_generation():
    crop = mandi_data.get_crop_data("paddy")
    history, forecast = mandi_data.generate_crop_history(crop)
    # 30 days past + today = 31 records
    assert len(history) == 31
    # 14 days future prediction = 14 records
    assert len(forecast) == 14

    for pt in history:
        assert "date" in pt
        assert "price" in pt
        assert pt["price"] > 0

    for pt in forecast:
        assert "date" in pt
        assert "price" in pt
        assert pt["price"] > 0


def test_selling_centers_filtering_and_sorting():
    all_centers = mandi_data.get_selling_centers()
    assert len(all_centers) >= 50

    # Filter by crop
    paddy_centers = mandi_data.get_selling_centers(crop_id="paddy")
    assert len(paddy_centers) > 0
    for c in paddy_centers:
        assert "paddy" in c["crops_accepted"]

    # Filter by district
    rc_centers = mandi_data.get_selling_centers(district="Raichur")
    assert len(rc_centers) >= 2
    for c in rc_centers:
        assert c["district"] == "Raichur"

    # Sort by highest rate
    tur_centers_sorted = mandi_data.get_selling_centers(crop_id="tur", sort_by="highest_rate")
    rates = [c["rates"].get("tur", 0) for c in tur_centers_sorted]
    assert rates == sorted(rates, reverse=True)


def test_every_karnataka_district_has_selling_centers():
    """Verify that every single one of Karnataka's 31 districts has verified selling centers."""
    all_centers = mandi_data.SELLING_CENTERS
    center_districts = {c["district"] for c in all_centers}
    for dist in DISTRICTS:
        assert dist in center_districts, f"Missing selling centers for district: {dist}"
        centers_for_dist = mandi_data.get_selling_centers(district=dist)
        assert len(centers_for_dist) >= 1, f"No centers returned for {dist}"


def test_selling_centers_search_query():
    """Verify keyword searching by town or center name."""
    tiptur_centers = mandi_data.get_selling_centers(search_query="Tiptur")
    assert len(tiptur_centers) >= 1
    assert any("Tiptur" in c["name_en"] or "Tiptur" in c["taluk"] for c in tiptur_centers)

    gangavathi_centers = mandi_data.get_selling_centers(search_query="Gangavathi")
    assert len(gangavathi_centers) >= 1
    assert any("Gangavathi" in c["name_en"] or "Gangavathi" in c["taluk"] for c in gangavathi_centers)


def test_market_rates_page_renders_cleanly():
    at = AppTest.from_file(str(ROOT / "views" / "market_rates.py"), default_timeout=60).run()
    assert not at.exception
    text = " ".join(m.value for m in at.markdown)
    assert "Market Rates" in text or "ಮಾರುಕಟ್ಟೆ ದರ" in text
