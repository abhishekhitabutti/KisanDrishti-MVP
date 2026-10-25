"""Unit tests for the Direct Farm-to-Consumer (F2C) marketplace."""
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from streamlit.testing.v1 import AppTest
import f2c_data


def test_f2c_data_loads_default_listings():
    listings = f2c_data.load_listings()
    assert len(listings) >= 8
    for item in listings:
        assert "farmer_name" in item
        assert "phone" in item
        assert "crop_name_kn" in item
        assert "farm_price" in item
        assert item["farm_price"] > 0
        assert "district" in item


def test_f2c_categories_structure():
    cats = f2c_data.CATEGORIES
    assert len(cats) >= 6
    cat_ids = [c["id"] for c in cats]
    assert "all" in cat_ids
    assert "grains" in cat_ids
    assert "vegetables" in cat_ids


def test_f2c_add_listing(tmp_path, monkeypatch):
    test_file = tmp_path / "test_listings.json"
    monkeypatch.setattr(f2c_data, "DATA_FILE", test_file)

    initial_len = len(f2c_data.load_listings())
    new_item = {
        "farmer_name": "ಟೆಸ್ಟ್ ಕೃಷಿಕ",
        "phone": "+91 99999 88888",
        "district": "Belagavi",
        "taluk": "Chikkodi",
        "village": "ನಿಪ್ಪಾಣಿ",
        "crop_name_kn": "ಸಾವಯವ ಬೆಲ್ಲ",
        "crop_name_en": "Organic Jaggery",
        "category": "organic",
        "farm_price": 60,
        "quantity": "10 Quintals"
    }
    added = f2c_data.add_listing(new_item)
    assert added["id"].startswith("list_")
    updated = f2c_data.load_listings()
    assert len(updated) == initial_len + 1
    assert updated[0]["farmer_name"] == "ಟೆಸ್ಟ್ ಕೃಷಿಕ"


def test_direct_market_page_renders_cleanly():
    at = AppTest.from_file(str(ROOT / "views" / "direct_market.py"), default_timeout=45).run()
    assert not at.exception
    text = " ".join(m.value for m in at.markdown)
    assert "Direct Farm-to-Consumer" in text or "ರೈತರಿಂದ ನೇರ ಖರೀದಿ" in text

