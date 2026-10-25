"""
Direct Farm-to-Consumer (F2C) Market Data Engine for KrushiNudi.
Author: Abhishek Hitabutti
Copyright: © 2026 Abhishek Hitabutti. All rights reserved.

Eliminating middlemen by connecting Karnataka farmers directly with consumers,
retail buyers, and organic food enthusiasts.
"""

import json
from datetime import datetime
from pathlib import Path

DATA_FILE = Path(__file__).resolve().parent / "market_listings.json"

CATEGORIES = [
    {"id": "all", "name_en": "All Produce", "name_kn": "ಎಲ್ಲಾ ಉತ್ಪನ್ನಗಳು", "icon": "🛒"},
    {"id": "grains", "name_en": "Millets & Grains", "name_kn": "ಸಿರಿಧಾನ್ಯ & ಧಾನ್ಯಗಳು", "icon": "🌾"},
    {"id": "vegetables", "name_en": "Fresh Vegetables", "name_kn": "ತಾಜಾ ತರಕಾರಿಗಳು", "icon": "🥕"},
    {"id": "fruits", "name_en": "Fruits & Orchards", "name_kn": "ಹಣ್ಣುಗಳು", "icon": "🥭"},
    {"id": "organic", "name_en": "Organic & Jaggery", "name_kn": "ಸಾವಯವ & ಬೆಲ್ಲ", "icon": "🍯"},
    {"id": "oils", "name_en": "Cold-Pressed Oils", "name_kn": "ಗಾಣದ ಎಣ್ಣೆಗಳು", "icon": "🫒"},
    {"id": "spices", "name_en": "Spices & Plantation", "name_kn": "ಮಸಾಲೆ & ತೋಟಗಾರಿಕೆ", "icon": "🌿"},
]

DEFAULT_LISTINGS = [
    {
        "id": "list_001",
        "farmer_name": "ಸುರೇಶ್ ಗೌಡ {Suresh Gowda}",
        "phone": "+91 98450 12345",
        "whatsapp": "919845012345",
        "district": "Mandya",
        "taluk": "Maddur",
        "village": "ಕೊಪ್ಪ {Koppa}",
        "crop_name_kn": "ಸಾವಯವ ಬೆಲ್ಲದ ಪುಡಿ",
        "crop_name_en": "Organic Chemical-Free Jaggery Powder",
        "category": "organic",
        "variety": "ದೇಸಿ ಕಬ್ಬಿನ ನೈಸರ್ಗಿಕ ಬೆಲ್ಲ (No Chemicals / No Hydros)",
        "quantity": "25 ಕ್ವಿಂಟಾಲ್ {Quintals}",
        "farm_price": 65,
        "mandi_price": 40,
        "retail_price": 110,
        "unit": "kg",
        "harvest_date": "2026-10-20",
        "is_organic": True,
        "badge_kn": "ಸಾವಯವ ಪ್ರಮಾಣಿತ",
        "badge_en": "Certified Organic",
        "description_kn": "ಯಾವುದೇ ರಾಸಾಯನಿಕ ಅಥವಾ ಬಣ್ಣ ಬಳಸದೆ ಸಾಂಪ್ರದಾಯಿಕ ಕೊಪ್ಪಣೆಯಲ್ಲಿ ತಯಾರಿಸಿದ 100% ಶುದ್ಧ ಪುಡಿ ಬೆಲ್ಲ. ಚಹಾ, ಪಾಯಸಕ್ಕೆ ಅತ್ಯುತ್ತಮ.",
        "description_en": "100% pure, unadulterated jaggery powder processed without chemical clarifying agents. Direct from Mandya cane fields.",
        "created_at": "2026-10-20"
    },
    {
        "id": "list_002",
        "farmer_name": "ಬಸವರಾಜ ಪಾಟೀಲ {Basavaraj Patil}",
        "phone": "+91 99801 23456",
        "whatsapp": "919980123456",
        "district": "Haveri",
        "taluk": "Byadgi",
        "village": "ಮೋಟೆಬೆನ್ನೂರು {Motebennur}",
        "crop_name_kn": "ಬ್ಯಾಡಗಿ ಡಬ್ಬಿ ಒಣ ಮೆಣಸಿನಕಾಯಿ",
        "crop_name_en": "Authentic Byadgi Dabba Red Chilli",
        "category": "spices",
        "variety": "GI Tagged Byadgi Dabba (High Colour, Low Pungency)",
        "quantity": "15 ಕ್ವಿಂಟಾಲ್ {Quintals}",
        "farm_price": 420,
        "mandi_price": 310,
        "retail_price": 580,
        "unit": "kg",
        "harvest_date": "2026-10-18",
        "is_organic": True,
        "badge_kn": "ಜಿಐ ಟ್ಯಾಗ್ ಮಾನ್ಯತೆ",
        "badge_en": "GI Tagged Origin",
        "description_kn": "ಗರಿಷ್ಠ ಕೆಂಪು ಬಣ್ಣ, ಕಡಿಮೆ ಖಾರ ಮತ್ತು ಅದ್ಭುತ ಪರಿಮಳ ಹೊಂದಿರುವ ಅಧಿಕೃತ ಬ್ಯಾಡಗಿ ಡಬ್ಬಿ ಮೆಣಸಿನಕಾಯಿ. ಮಸಾಲೆ ಪುಡಿಗಳಿಗೆ ಪ್ರಸಿದ್ಧ.",
        "description_en": "Famous GI tagged Byadgi chillies with deep red colour, rich oleoresin and mild heat. Sun-dried naturally.",
        "created_at": "2026-10-18"
    },
    {
        "id": "list_003",
        "farmer_name": "ಮಂಜುನಾಥ ನಾಯಕ್ {Manjunath Nayak}",
        "phone": "+91 97412 34567",
        "whatsapp": "919741234567",
        "district": "Mysuru",
        "taluk": "Hunsur",
        "village": "ಬಿಳಿಕೆರೆ {Bilikere}",
        "crop_name_kn": "ಸಾವಯವ ನವಣೆ ಸಿರಿಧಾನ್ಯ",
        "crop_name_en": "Organic Foxtail Millet (Navane)",
        "category": "grains",
        "variety": "ಅನ್‌ಪಾಲಿಶ್ಡ್ ನವಣೆ ಅಕ್ಕಿ (Desi Heirloom)",
        "quantity": "30 ಕ್ವಿಂಟಾಲ್ {Quintals}",
        "farm_price": 75,
        "mandi_price": 48,
        "retail_price": 135,
        "unit": "kg",
        "harvest_date": "2026-10-22",
        "is_organic": True,
        "badge_kn": "ಪೌಷ್ಟಿಕ ಸಿರಿಧಾನ್ಯ",
        "badge_en": "Nutri-Cereal",
        "description_kn": "ನೈಸರ್ಗಿಕ ಕೃಷಿಯಲ್ಲಿ ಬೆಳೆದ ಪೌಷ್ಟಿಕ ನವಣೆ. ಮಧುಮೇಹ ಮತ್ತು ರಕ್ತದೊತ್ತಡ ನಿಯಂತ್ರಣಕ್ಕೆ ಅತ್ಯುತ್ತಮ ನಾರಿನಂಶವುಳ್ಳ ಸಿರಿಧಾನ್ಯ.",
        "description_en": "Naturally farmed, unpolished foxtail millet rich in dietary fibre and protein. Direct from Hunsur organic cluster.",
        "created_at": "2026-10-22"
    },
    {
        "id": "list_004",
        "farmer_name": "ಶ್ರೀಮತಿ ಕಾವೇರಿ ಅಮ್ಮ {Kaveri Amma}",
        "phone": "+91 94481 56789",
        "whatsapp": "919448156789",
        "district": "Belagavi",
        "taluk": "Gokak",
        "village": "ಕೌಜಲಗಿ {Koujalagi}",
        "crop_name_kn": "ದೇಸಿ ಸೋನಾ ಮಸೂರಿ ಅಕ್ಕಿ (ಹಳೆ ಅಕ್ಕಿ)",
        "crop_name_en": "Desi Aged Sona Masoori Raw Rice",
        "category": "grains",
        "variety": "1 ವರ್ಷ ಹಳೆಯ ಸೋನಾ ಮಸೂರಿ (Single Polished)",
        "quantity": "50 ಕ್ವಿಂಟಾಲ್ {Quintals}",
        "farm_price": 58,
        "mandi_price": 38,
        "retail_price": 85,
        "unit": "kg",
        "harvest_date": "2026-09-15",
        "is_organic": False,
        "badge_kn": "ಕೀಟನಾಶಕ ಮುಕ್ತ",
        "badge_en": "Pesticide-Free",
        "description_kn": "ಘಟಪ್ರಭಾ ನದಿ ನೀರಿನಲ್ಲಿ ಬೆಳೆದ 1 ವರ್ಷ ಹಳೆಯ ಅನ್ನ ರುಚಿಕರವಾದ ಸೋನಾ ಮಸೂರಿ ಅಕ್ಕಿ. 25 ಕೆ.ಜಿ. ಚೀಲಗಳಲ್ಲಿ ಲಭ್ಯ.",
        "description_en": "1-year aged premium Sona Masoori raw rice grown with river irrigation. Cook fluffy and non-sticky.",
        "created_at": "2026-09-15"
    },
    {
        "id": "list_005",
        "farmer_name": "ಆನಂದ ರಾವ್ {Anand Rao}",
        "phone": "+91 96325 87410",
        "whatsapp": "919632587410",
        "district": "Shivamogga",
        "taluk": "Thirthahalli",
        "village": "ಆಗುಂಬೆ {Agumbe Ghats}",
        "crop_name_kn": "ಶುದ್ಧ ಕಾಡುಜೇನು ತುಪ್ಪ",
        "crop_name_en": "Raw Wild Forest Honey",
        "category": "organic",
        "variety": "ಪಶ್ಚಿಮ ಘಟ್ಟಗಳ ನೈಸರ್ಗಿಕ ಕಾಡುಜೇನು",
        "quantity": "120 ಬಾಟಲ್ {Bottles}",
        "farm_price": 480,
        "mandi_price": 320,
        "retail_price": 750,
        "unit": "kg",
        "harvest_date": "2026-10-15",
        "is_organic": True,
        "badge_kn": "ಮಲೆನಾಡು ಶುದ್ಧತೆ",
        "badge_en": "100% Raw Forest",
        "description_kn": "ಯಾವುದೇ ಸಂಸ್ಕರಣೆ ಅಥವಾ ಬಿಸಿ ಮಾಡದೆ ಶೋಧಿಸಿದ ಮಲೆನಾಡಿನ 100% ಕಚ್ಚಾ ಕಾಡುಜೇನು. ಔಷಧೀಯ ಗುಣಗಳಿಂದ ಸಮೃದ್ಧ.",
        "description_en": "Unheated, unfiltered wild honey sustainably harvested from Western Ghats flora. High medicinal enzyme content.",
        "created_at": "2026-10-15"
    },
    {
        "id": "list_006",
        "farmer_name": "ಪ್ರಕಾಶ್ ಕುಮಾರ್ {Prakash Kumar}",
        "phone": "+91 98860 11223",
        "whatsapp": "919886011223",
        "district": "Kolar",
        "taluk": "Mulbagal",
        "village": "ಅವಣಿ {Avani}",
        "crop_name_kn": "ತಾಜಾ ನಾಟಿ ಟೊಮೆಟೊ",
        "crop_name_en": "Farm-Fresh Desi Tomatoes",
        "category": "vegetables",
        "variety": "ದೇಸಿ ಹುಳಿ ತಳಿ (High Lycopene)",
        "quantity": "40 ಕ್ರೇಟ್‌ಗಳು {Crates}",
        "farm_price": 22,
        "mandi_price": 12,
        "retail_price": 42,
        "unit": "kg",
        "harvest_date": "2026-10-25",
        "is_organic": False,
        "badge_kn": "ಇಂದು ಬೆಳಿಗ್ಗೆ ಕೊಯ್ಲು",
        "badge_en": "Harvested Today",
        "description_kn": "ಇಂದೇ ಜಮೀನಿನಿಂದ ಕಿತ್ತ ತಾಜಾ ಕೆಂಪು ನಾಟಿ ಟೊಮೆಟೊ. ಸಾರು, ಸಾಂಬಾರ್ ಹಾಗೂ ಗ್ರೇವಿಗೆ ಅದ್ಭುತ ಹುಳಿ ರುಚಿ.",
        "description_en": "Freshly plucked farm-gate desi tomatoes with balanced tartness and juiciness. Wholesale and bulk crate orders welcome.",
        "created_at": "2026-10-25"
    },
    {
        "id": "list_007",
        "farmer_name": "ಸಿದ್ಧರಾಮಯ್ಯ {Siddaramaiah}",
        "phone": "+91 94802 33445",
        "whatsapp": "919480233445",
        "district": "Bagalkot",
        "taluk": "Mudhol",
        "village": "ಲೋಕಾಪುರ {Lokapur}",
        "crop_name_kn": "ಮರದ ಗಾಣದ ಶುದ್ಧ ಕಡಲೆಕಾಯಿ ಎಣ್ಣೆ",
        "crop_name_en": "Wood Cold-Pressed Groundnut Oil",
        "category": "oils",
        "variety": "ಸಾಂಪ್ರದಾಯಿಕ ಮರದ ಗಾಣ (Mara Gana Churning)",
        "quantity": "200 ಲೀಟರ್ {Litres}",
        "farm_price": 230,
        "mandi_price": 160,
        "retail_price": 340,
        "unit": "L",
        "harvest_date": "2026-10-21",
        "is_organic": True,
        "badge_kn": "ನೈಸರ್ಗಿಕ ಗಾಣ",
        "badge_en": "Cold Pressed",
        "description_kn": "ನಾಟಿ ಕಡಲೆಕಾಯಿ ಬೀಜಗಳಿಂದ ಮರದ ಗಾಣದಲ್ಲಿ ಯಾವುದೇ ರಾಸಾಯನಿಕವಿಲ್ಲದೆ ತಯಾರಿಸಿದ ದಪ್ಪನೆಯ ನೈಸರ್ಗಿಕ ಅಡುಗೆ ಎಣ್ಣೆ.",
        "description_en": "Pure cold-pressed groundnut oil extracted in traditional wooden marachekku under 38°C to retain antioxidants.",
        "created_at": "2026-10-21"
    },
    {
        "id": "list_008",
        "farmer_name": "ರಮೇಶ್ ಹೆಗಡೆ {Ramesh Hegde}",
        "phone": "+91 97314 55667",
        "whatsapp": "919731455667",
        "district": "Uttara Kannada",
        "taluk": "Sirsi",
        "village": "ಬನವಾಸಿ {Banavasi}",
        "crop_name_kn": "ಮಲೆನಾಡು ಬೋಲ್ಡ್ ಕರಿಮೆಣಸು",
        "crop_name_en": "Malabar Bold Black Pepper",
        "category": "spices",
        "variety": "ಪನ್ನಿಯೂರು-1 ತಳಿ (Grade A Bold)",
        "quantity": "10 ಕ್ವಿಂಟಾಲ್ {Quintals}",
        "farm_price": 620,
        "mandi_price": 480,
        "retail_price": 890,
        "unit": "kg",
        "harvest_date": "2026-10-10",
        "is_organic": True,
        "badge_kn": "ಮಲೆನಾಡು ಮಸಾಲೆ",
        "badge_en": "Western Ghats Spice",
        "description_kn": "ಅಡಿಕೆ ತೋಟಗಳಲ್ಲಿ ಬಳ್ಳಿ ಹಬ್ಬಿಸಿ ನೈಸರ್ಗಿಕವಾಗಿ ಕೊಯ್ಲು ಮಾಡಿದ ಕಪ್ಪು, ದಪ್ಪ ಕಾಳುಗಳ ತೀಕ್ಷ್ಣ ಕರಿಮೆಣಸು.",
        "description_en": "Grade A sun-dried bold black peppercorns grown organically in inter-cropped areca orchards.",
        "created_at": "2026-10-10"
    }
]


def load_listings():
    """Load produce listings from JSON file or initialize with verified defaults."""
    if DATA_FILE.exists():
        try:
            with open(DATA_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
                if isinstance(data, list) and len(data) > 0:
                    return data
        except Exception:
            pass

    # Save defaults
    try:
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump(DEFAULT_LISTINGS, f, indent=2, ensure_ascii=False)
    except Exception:
        pass
    return DEFAULT_LISTINGS


def add_listing(item):
    """Add a new produce listing posted by a farmer."""
    listings = load_listings()
    item_id = f"list_{int(datetime.now().timestamp())}"
    item["id"] = item_id
    item["created_at"] = datetime.now().strftime("%Y-%m-%d")
    listings.insert(0, item)
    try:
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump(listings, f, indent=2, ensure_ascii=False)
    except Exception:
        pass
    return item
