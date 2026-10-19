"""
KrushiNudi Smart Farm Advisory: Comprehensive Crop Protection & High-Yield Nutrition Database.
Authentic Indian agricultural university (ICAR, UAS Dharwad, UAS Bangalore, TNAU) recommendations.
Features:
- Crop-wise diseases & pests with exact chemical actives, dosages (per L & per 15L pump)
- High-yielding growth promoters, water-soluble fertilizers (WSF), and chelated micronutrients
- Tank-mix compatibility matrix (safe vs unsafe combinations)
- Verified Indian agri manufacturers, direct online order portals (IFFCO Bazar, BigHaat, AgroStar),
  and toll-free ordering & advisory phone numbers.
100% bilingual (English & Kannada) with technical terms enclosed in braces {...}.
"""

# ==============================================================================
# TOP INDIAN AGRI COMPANIES & DIRECT PROCUREMENT PLATFORMS
# ==============================================================================
INDIAN_AGRI_PLATFORMS = [
    {
        "id": "iffco_bazar",
        "company_en": "IFFCO (Indian Farmers Fertiliser Cooperative)",
        "company_kn": "ಇಫ್ಕೋ {IFFCO - ಭಾರತೀಯ ರೈತರ ರಸಗೊಬ್ಬರ ಸಹಕಾರ ಸಂಸ್ಥೆ}",
        "specialty_en": "World pioneer of Nano Urea & Nano DAP, Sagarika seaweed biostimulant, water-soluble fertilizers, and bio-fertilizers.",
        "specialty_kn": "ವಿಶ್ವದ ಮೊದಲ ನ್ಯಾನೋ ಯೂರಿಯಾ & ನ್ಯಾನೋ ಡಿಎಪಿ {Nano DAP}, ಸಾಗರಿಕ ಕಡಲಕಳೆ ಬಯೋ-ಸ್ಟಿಮ್ಯುಲಂಟ್ ಮತ್ತು 100% ನೀರಿನಲ್ಲಿ ಕರಗುವ ಗೊಬ್ಬರಗಳು.",
        "phone": "1800 103 1967",
        "order_url": "https://www.iffcobazar.in",
        "delivery_note_en": "Free doorstep delivery to all rural pin codes across Karnataka with no minimum order.",
        "delivery_note_kn": "ಕರ್ನಾಟಕದ ಎಲ್ಲಾ ಗ್ರಾಮೀಣ ಪಿನ್‌ಕೋಡ್‌ಗಳಿಗೆ ಉಚಿತ ಮನೆಬಾಗಿಲು ಡೆಲಿವರಿ ಲಭ್ಯ.",
        "popular_products": ["Nano Urea (500 ml)", "Nano DAP (500 ml)", "Sagarika Liquid (1 L)", "WSF 19:19:19", "WSF 00:52:34"]
    },
    {
        "id": "bighaat",
        "company_en": "BigHaat India (Bengaluru, Karnataka)",
        "company_kn": "ಬಿಗ್‌ಹಾಟ್ ಇಂಡಿಯಾ {BigHaat - ಬೆಂಗಳೂರು, ಕರ್ನಾಟಕ}",
        "specialty_en": "India's largest digital agri-inputs marketplace. 100% genuine branded pesticides, fungicides, hybrid seeds, and farm tools.",
        "specialty_kn": "ಭಾರತದ ಪ್ರಮುಖ ಡಿಜಿಟಲ್ ಕೃಷಿ ಮಾರುಕಟ್ಟೆ. 100% ಅಸಲಿ ಬ್ರ್ಯಾಂಡೆಡ್ ಕೀಟನಾಶಕ, ಶಿಲೀಂಧ್ರನಾಶಕ, ಲಘು ಪೋಷಕಾಂಶ ಮತ್ತು ಸುಧಾರಿತ ಬೀಜಗಳು.",
        "phone": "1800 3000 2434",
        "order_url": "https://www.bighaat.com",
        "delivery_note_en": "Cash on delivery (COD) available across all 31 districts of Karnataka. Expert agronomist call support.",
        "delivery_note_kn": "ಕರ್ನಾಟಕದ ಎಲ್ಲಾ ಜಿಲ್ಲೆಗಳಿಗೂ ಕ್ಯಾಶ್ ಆನ್ ಡೆಲಿವರಿ {COD} ಸೌಲಭ್ಯ ಮತ್ತು ಕೃಷಿ ತಜ್ಞರ ಫೋನ್ ಮಾರ್ಗದರ್ಶನ.",
        "popular_products": ["Coragen", "Ridomil Gold", "Saaf Fungicide", "Amistar Top", "Planofix PGR", "Multiplex Grade IV"]
    },
    {
        "id": "agrostar",
        "company_en": "AgroStar India",
        "company_kn": "ಅಗ್ರೋಸ್ಟಾರ್ ಇಂಡಿಯಾ {AgroStar India}",
        "specialty_en": "Direct-to-farmer agri platform offering leading Indian brands (Tata Rallis, Dhanuka, PI Industries, Bayer India, UPL).",
        "specialty_kn": "ರೈತರಿಗೆ ನೇರ ಸರಬರಾಜು ಮಾಡುವ ಕೃಷಿ ವೇದಿಕೆ (ಟಾಟಾ ರ‍್ಯಾಲಿಸ್, ಧನುಕಾ, ಪಿಐ ಇಂಡಸ್ಟ್ರೀಸ್, ಯುಪಿಎಲ್ ಬ್ರ್ಯಾಂಡ್‌ಗಳು).",
        "phone": "1800 120 4040",
        "order_url": "https://www.agrostar.in",
        "delivery_note_en": "Direct village courier delivery with missed-call telephone order booking.",
        "delivery_note_kn": "ಮಿಸ್ಡ್ ಕಾಲ್ ಮೂಲಕ ಫೋನ್‌ನಲ್ಲಿಯೇ ನೇರ ಆರ್ಡರ್ ಮತ್ತು ಗ್ರಾಮ ಮಟ್ಟದ ಡೆಲಿವರಿ.",
        "popular_products": ["Tata Rallis Contaf Plus", "Dhanuka EM-1", "PI Industries Keefun", "UPL Saaf"]
    },
    {
        "id": "kcc_gov",
        "company_en": "Kisan Call Centre (Govt. of India)",
        "company_kn": "ಕಿಸಾನ್ ಕಾಲ್ ಸೆಂಟರ್ {KCC - ಭಾರತ ಸರ್ಕಾರ}",
        "specialty_en": "Free toll-free expert agricultural advice in Kannada from certified government agricultural officers.",
        "specialty_kn": "ಕೃಷಿ ತಜ್ಞರು ಮತ್ತು ವಿಜ್ಞಾನಿಗಳಿಂದ ಉಚಿತ ಕನ್ನಡ ಭಾಷಾ ಕೃಷಿ ಸಲಹೆ ಮತ್ತು ಸರ್ಕಾರಿ ಅನುಮೋದಿತ ಔಷಧಿ ಮಾರ್ಗದರ್ಶನ.",
        "phone": "1800 180 1551",
        "order_url": "https://dhaatupaatha.icar.gov.in",
        "delivery_note_en": "Available 6:00 AM to 10:00 PM all 7 days a week. Free call from any mobile network.",
        "delivery_note_kn": "ವಾರದ ಎಲ್ಲಾ 7 ದಿನಗಳೂ ಬೆಳಗ್ಗೆ 6:00 ರಿಂದ ರಾತ್ರಿ 10:00 ರವರೆಗೆ ಉಚಿತ ಫೋನ್ ಕರೆ ಸೇವೆ.",
        "popular_products": ["KVK Farm Advisory", "Government RSK Seed & Input Support", "Soil Health Card Guidance"]
    }
]

# ==============================================================================
# HIGH-YIELDING GROWTH PROMOTERS, WSF NUTRITION & BIOSTIMULANTS
# ==============================================================================
HIGH_YIELD_PROMOTERS = [
    {
        "id": "sagarika",
        "name_en": "IFFCO Sagarika (Seaweed Biostimulant)",
        "name_kn": "ಇಫ್ಕೋ ಸಾಗರಿಕ ಕಡಲಕಳೆ ಜೈವಿಕ ಉತ್ತೇಜಕ {IFFCO Sagarika}",
        "category_en": "Organic Bio-Stimulant & Root Booster",
        "category_kn": "ಸಾವಯವ ಜೈವಿಕ ಉತ್ತೇಜಕ & ಬೇರು ಬೆಳೆಸುವ ಟಾನಿಕ್",
        "dose_per_litre": "2.5 - 3.0 ml/litre",
        "dose_per_pump_15l": "40 - 45 ml per 15L pump",
        "timing_en": "Vegetative stage (25-30 days after sowing) and pre-flowering stage.",
        "timing_kn": "ಸಸಿ ಬೆಳೆಯುವ ಹಂತ (ಬಿತ್ತಿದ 25-30 ದಿನ) ಮತ್ತು ಹೂವಾಡುವ ಮುನ್ನ.",
        "benefits_en": "Stimulates dense root growth, increases tillers in paddy/sugarcane, activates soil microbes, improves drought resistance, and boosts grain yield by 12-18%.",
        "benefits_kn": "ಭತ್ತ, ಕಬ್ಬು, ಮೆಕ್ಕೆಜೋಳದಲ್ಲಿ ಕವಲು/ಕವಡೆಗಳ ಸಂಖ್ಯೆ ಹೆಚ್ಚಿಸುತ್ತದೆ, ಬೇರುಗಳು ಆಳಕ್ಕೆ ಇಳಿಯಲು ನೆರವಾಗುತ್ತದೆ, ಬರ ನಿರೋಧಕ ಶಕ್ತಿ ನೀಡುತ್ತದೆ ಮತ್ತು ಇಳುವರಿಯನ್ನು 12-18% ಹೆಚ್ಚಿಸುತ್ತದೆ.",
        "manufacturer": "IFFCO",
        "buy_url": "https://www.iffcobazar.in/en/product/sagarika-liquid",
        "compatible_with": "All fungicides, insecticides, and water-soluble fertilizers (WSF)."
    },
    {
        "id": "nano_urea",
        "name_en": "IFFCO Nano Urea Plus (16% N)",
        "name_kn": "ಇಫ್ಕೋ ನ್ಯಾನೋ ಯೂರಿಯಾ ಪ್ಲಸ್ {IFFCO Nano Urea}",
        "category_en": "Liquid Nanotechnology Nitrogen Fertilizer",
        "category_kn": "ದ್ರವರೂಪದ ನ್ಯಾನೋ ತಂತ್ರಜ್ಞಾನ ಸಾರಜನಕ ರಸಗೊಬ್ಬರ",
        "dose_per_litre": "2.0 - 4.0 ml/litre",
        "dose_per_pump_15l": "35 - 50 ml per 15L pump",
        "timing_en": "1st spray: Active tillering / branching stage (30-35 DAS). 2nd spray: 15-20 days later.",
        "timing_kn": "1ನೇ ಸಿಂಪಡಣೆ: ಕವಲು ಒಡೆಯುವ ಹಂತ (30-35 ದಿನ). 2ನೇ ಸಿಂಪಡಣೆ: ಹೂವಾಡುವ 1 ವಾರ ಮುನ್ನ.",
        "benefits_en": "80%+ nitrogen absorption efficiency directly through leaf stomata. Replaces 1 whole bag of conventional granular urea, prevents soil hardening, and increases crop protein content.",
        "benefits_kn": "ಎಲೆಗಳ ಮೂಲಕ 80% ಕ್ಕಿಂತ ಹೆಚ್ಚು ಸಾರಜನಕ ಹೀರಿಕೊಳ್ಳುತ್ತದೆ. 1 ಬ್ಯಾಗ್ ಸಾಂಪ್ರದಾಯಿಕ ಯೂರಿಯಾ ಉಳಿಸುತ್ತದೆ, ಮಣ್ಣು ಗಟ್ಟಿಯಾಗುವುದನ್ನು ತಪ್ಪಿಸುತ್ತದೆ ಮತ್ತು ಕಾಳಿನ ತೂಕ ಹೆಚ್ಚಿಸುತ್ತದೆ.",
        "manufacturer": "IFFCO",
        "buy_url": "https://www.iffcobazar.in/en/product/iffco-nano-urea-liquid",
        "compatible_with": "Compatible with most bio-stimulants and non-alkaline agrochemicals."
    },
    {
        "id": "nano_dap",
        "name_en": "IFFCO Nano DAP (8% N, 16% P2O5)",
        "name_kn": "ಇಫ್ಕೋ ನ್ಯಾನೋ ಡಿಎಪಿ {IFFCO Nano DAP}",
        "category_en": "Liquid Nanotechnology Phosphorus Booster",
        "category_kn": "ದ್ರವರೂಪದ ನ್ಯಾನೋ ರಂಜಕ ಪೋಷಕಾಂಶ",
        "dose_per_litre": "3.0 - 4.0 ml/litre (foliar) or 5 ml/kg seed treatment",
        "dose_per_pump_15l": "50 - 60 ml per 15L pump",
        "timing_en": "Seed priming before sowing, and foliar spray at early vegetative stage.",
        "timing_kn": "ಬಿತ್ತನೆ ಮುನ್ನ ಬೀಜೋಪಚಾರಕ್ಕೆ (5 ಮಿಲಿ/ಕೆಜಿ ಬೀಜಕ್ಕೆ), ಮತ್ತು ಸಸಿ ಹಂತದಲ್ಲಿ ಎಲೆಗಳ ಮೇಲೆ ಸಿಂಪಡಣೆ.",
        "benefits_en": "Enhances root volume and nodulation in pulses (Bengal gram, Tur, Soybean), aids strong stem formation, and eliminates phosphorus fixation in hard-rock soil.",
        "benefits_kn": "ದ್ವಿದಳ ಧಾನ್ಯಗಳಲ್ಲಿ (ತೊಗರಿ, ಕಡಲೆ, ಸೋಯಾಬೀನ್) ಸಾರಜನಕ ಹೀರುವ ಗಂಟುಗಳು ಮತ್ತು ಬೇರುಗಳನ್ನು ಹೆಚ್ಚಿಸುತ್ತದೆ. ಮಣ್ಣಿನಲ್ಲಿ ರಂಜಕ ವ್ಯರ್ಥವಾಗುವುದನ್ನು ತಡೆಯುತ್ತದೆ.",
        "manufacturer": "IFFCO",
        "buy_url": "https://www.iffcobazar.in/en/product/iffco-nano-dap-liquid",
        "compatible_with": "Compatible with Sagarika and bio-fungicides."
    },
    {
        "id": "wsf_19_19_19",
        "name_en": "Water Soluble NPK 19:19:19 (Balanced Starter)",
        "name_kn": "100% ನೀರಿನಲ್ಲಿ ಕರಗುವ ಗೊಬ್ಬರ {NPK 19:19:19}",
        "category_en": "100% Water Soluble Vegetative Fertilizer",
        "category_kn": "ಸಮತೋಲಿತ ಆರಂಭಿಕ ಕರಗುವ ಗೊಬ್ಬರ",
        "dose_per_litre": "5.0 g/litre",
        "dose_per_pump_15l": "75 - 80 g per 15L pump",
        "timing_en": "Early growth and branching stage (20-45 DAS).",
        "timing_kn": "ಬೆಳೆಯ ಆರಂಭಿಕ ಹಂತ ಮತ್ತು ಕವಲು ಒಡೆಯುವ ಹಂತದಲ್ಲಿ (ಬಿತ್ತಿದ 20-45 ದಿನಗಳಲ್ಲಿ).",
        "benefits_en": "Provides instant green canopy, balanced nutrition (Nitrogen, Phosphorus, Potash) with zero wastage, curing sudden yellowing in crops.",
        "benefits_kn": "ಬೆಳೆಗೆ ತ್ವರಿತ ಹಸಿರು ಬಣ್ಣ ನೀಡುತ್ತದೆ, ಸಮತೋಲಿತ ಪೋಷಕಾಂಶ ಒದಗಿಸಿ ಎಲೆ ಹಳದಿ ರೋಗ ತಡೆಯುತ್ತದೆ ಮತ್ತು ಸಸಿಗಳನ್ನು ಬಲಪಡಿಸುತ್ತದೆ.",
        "manufacturer": "IFFCO / Coromandel Gromor / Tata Rallis",
        "buy_url": "https://www.iffcobazar.in/en/product/wsf-19-19-19-fertiliser",
        "compatible_with": "Can be mixed with most insecticides and fungicides. Do NOT mix with copper or sulphur."
    },
    {
        "id": "wsf_00_52_34",
        "name_en": "Monopotassium Phosphate NPK 00:52:34 (Flower Booster)",
        "name_kn": "ಹೂವು & ಮೊಗ್ಗು ಉತ್ತೇಜಕ {NPK 00:52:34 - ಮೊನೊಪೊಟ್ಯಾಸಿಯಂ ಫಾಸ್ಫೇಟ್}",
        "category_en": "Pre-Flowering & Root Fortifier",
        "category_kn": "ಹೂವಾಡುವ ಹಂತದ ವಿಶೇಷ ರಂಜಕ & ಪೊಟ್ಯಾಷ್ ಗೊಬ್ಬರ",
        "dose_per_litre": "5.0 g/litre",
        "dose_per_pump_15l": "75 g per 15L pump",
        "timing_en": "Just before flowering and at initial flowering stage.",
        "timing_kn": "ಹೂ ಮೊಗ್ಗು ಕಟ್ಟುವ ಹಂತದಲ್ಲಿ ಮತ್ತು ಹೂ ಬಿಡುವ ಆರಂಭದಲ್ಲಿ.",
        "benefits_en": "Prevents flower drop, promotes heavy uniform flowering in chilli, tomato, cotton, and pulses, and enhances disease resistance against downy mildew.",
        "benefits_kn": "ಮೆಣಸಿನಕಾಯಿ, ಟೊಮೆಟೊ, ಹತ್ತಿ, ತೊಗರಿಯಲ್ಲಿ ಹೂವು ಉದುರುವುದನ್ನು ತಡೆಯುತ್ತದೆ, ಅಧಿಕ ಹೂವುಗಳನ್ನು ಅರಳಿಸುತ್ತದೆ ಮತ್ತು ಕಾಯಿ ಕಟ್ಟುವ ಪ್ರಮಾಣ ಹೆಚ್ಚಿಸುತ್ತದೆ.",
        "manufacturer": "IFFCO / Coromandel",
        "buy_url": "https://www.bighaat.com/products/0-52-34-fertilizer",
        "compatible_with": "Can be tank-mixed with Boron 20% and insecticide sprays."
    },
    {
        "id": "wsf_13_00_45",
        "name_en": "Potassium Nitrate NPK 13:00:45 (Grain & Fruit Expander)",
        "name_kn": "ಕಾಳು ತುಂಬುವ & ಹೊಳಪು ನೀಡುವ ಗೊಬ್ಬರ {NPK 13:00:45 - ಪೊಟ್ಯಾಸಿಯಂ ನೈಟ್ರೇಟ್}",
        "category_en": "Fruit & Grain Development Booster",
        "category_kn": "ಕಾಳು ದಪ್ಪಗಾಗಿಸುವ & ಕಾಂತಿ ಹೆಚ್ಚಿಸುವ ಗೊಬ್ಬರ",
        "dose_per_litre": "5.0 - 6.0 g/litre",
        "dose_per_pump_15l": "80 - 100 g per 15L pump",
        "timing_en": "Grain filling stage (paddy, maize) or fruit development stage (tomato, pomegranate, cotton).",
        "timing_kn": "ಕಾಳು ಕಟ್ಟುವ ಮತ್ತು ಹಾಲು ತುಂಬುವ ಹಂತದಲ್ಲಿ (ಭತ್ತ, ಜೋಳ) ಅಥವಾ ಕಾಯಿ ಮಾಗುವ ಹಂತದಲ್ಲಿ (ಟೊಮೆಟೊ, ಹತ್ತಿ).",
        "benefits_en": "Maximizes grain weight, enhances bold shiny seeds, prevents premature drying, and increases market mandi price by 10-15%.",
        "benefits_kn": "ಕಾಳು ಜೊಳ್ಳಾಗುವುದನ್ನು ತಡೆದು ದಪ್ಪ, ಗಟ್ಟಿ ಮತ್ತು ಹೊಳಪುಳ್ಳ ಕಾಳುಗಳನ್ನು ನೀಡುತ್ತದೆ. ಮಾರುಕಟ್ಟೆಯಲ್ಲಿ ಉತ್ತಮ ಧಾರಣೆ ತಂದುಕೊಡುತ್ತದೆ.",
        "manufacturer": "Coromandel / IFFCO / Mahadhan",
        "buy_url": "https://www.bighaat.com/products/potassium-nitrate-13-0-45",
        "compatible_with": "Compatible with most fungicides and insecticides."
    },
    {
        "id": "chelated_boron",
        "name_en": "Disodium Octaborate Tetrahydrate (Boron 20%)",
        "name_kn": "ಕರಗುವ ಬೋರಾನ್ 20% {Chelated Boron 20%}",
        "category_en": "Essential Micronutrient for Pollination",
        "category_kn": "ಪರಾಗಸ್ಪರ್ಶ & ಕಾಯಿ ಬಿರುಕು ತಡೆಯುವ ಸೂಕ್ಷ್ಮ ಪೋಷಕಾಂಶ",
        "dose_per_litre": "1.0 - 1.5 g/litre",
        "dose_per_pump_15l": "15 - 20 g per 15L pump",
        "timing_en": "Flowering stage and pod/fruit initiation stage.",
        "timing_kn": "ಹೂವಾಡುವ ಹಂತ ಮತ್ತು ಎಳೆಯ ಕಾಯಿ ಕಟ್ಟುವ ಹಂತ.",
        "benefits_en": "Enables 100% pollination, prevents hollow seeds in sunflower/groundnut, stops fruit cracking in tomato/pomegranate, and increases sugar translocation.",
        "benefits_kn": "ಸೂರ್ಯಕಾಂತಿ, ಕಡಲೆಯಲ್ಲಿ ಜೊಳ್ಳು ಕಾಳು ತಡೆಯುತ್ತದೆ, ಟೊಮೆಟೊ ಮತ್ತು ದಾಳಿಂಬೆಯಲ್ಲಿ ಹಣ್ಣು ಬಿರುಕು ಬಿಡುವುದನ್ನು ಸಂಪೂರ್ಣ ನಿಯಂತ್ರಿಸುತ್ತದೆ.",
        "manufacturer": "Multiplex / Tata Rallis / Coromandel",
        "buy_url": "https://www.bighaat.com/products/multiplex-boron",
        "compatible_with": "Can be safely tank-mixed with NPK 00:52:34 or NPK 13:00:45."
    },
    {
        "id": "chelated_zinc",
        "name_en": "Chelated Zinc EDTA 12%",
        "name_kn": "ಚೆಲೇಟೆಡ್ ಸತು (ಜಿಂಕ್) 12% {Zinc EDTA 12%}",
        "category_en": "Enzyme Activator & Interveinal Chlorosis Cure",
        "category_kn": "ಎಲೆ ಹಳದಿ ರೋಗ ತಡೆಯುವ ಸತು ಪೋಷಕಾಂಶ",
        "dose_per_litre": "1.0 g/litre",
        "dose_per_pump_15l": "15 g per 15L pump",
        "timing_en": "Vegetative stage (20-30 DAS) when leaf veins show yellow stripes.",
        "timing_kn": "ಸಸಿ ಬೆಳೆಯುವ ಹಂತದಲ್ಲಿ ಎಲೆಗಳ ನರಗಳು ಹಳದಿಯಾದಾಗ.",
        "benefits_en": "Prevents Khaira disease in paddy and white bud in maize. Activates plant growth hormones and enhances chlorophyll synthesis.",
        "benefits_kn": "ಭತ್ತದಲ್ಲಿ ಬರುವ 'ಖೈರಾ ರೋಗ' ಮತ್ತು ಮೆಕ್ಕೆಜೋಳದ 'ಬಿಳಿ ಮೊಗ್ಗು ರೋಗ' ತಡೆಯುತ್ತದೆ. ಹಸಿರು ಕ್ಲೋರೋಫಿಲ್ ಹೆಚ್ಚಿಸುತ್ತದೆ.",
        "manufacturer": "Multiplex / IFFCO / Coromandel",
        "buy_url": "https://www.bighaat.com/products/multiplex-chelamin-plus",
        "compatible_with": "Compatible with WSF 19:19:19. Do NOT mix directly with phosphorus fertilizers in high concentration."
    },
    {
        "id": "planofix",
        "name_en": "Planofix - Alpha Naphthyl Acetic Acid (NAA 4.5% SL)",
        "name_kn": "ಪ್ಲಾನೋಫಿಕ್ಸ್ ಹೂವು ಉದುರುವುದು ತಡೆಯುವ ಹಾರ್ಮೋನ್ {Planofix PGR}",
        "category_en": "Plant Growth Regulator (PGR)",
        "category_kn": "ಸಸ್ಯ ಬೆಳವಣಿಗೆ ನಿಯಂತ್ರಕ {PGR}",
        "dose_per_litre": "0.25 ml/litre (Strict: 4 ml per 15-litre pump)",
        "dose_per_pump_15l": "4 ml per 15L pump (Never exceed dose!)",
        "timing_en": "Peak flowering stage in chilli, cotton, tomato, mango, and pulses.",
        "timing_kn": "ಮೆಣಸಿನಕಾಯಿ, ಹತ್ತಿ, ತೊಗರಿ, ಟೊಮೆಟೊದಲ್ಲಿ ಹೂವುಗಳು ಗರಿಷ್ಠ ಪ್ರಮಾಣದಲ್ಲಿರುವಾಗ.",
        "benefits_en": "Drastically reduces flower and square shedding (drop rate falls by 60-80%), resulting in bumper fruiting and heavy pod set.",
        "benefits_kn": "ಹೂವು ಮತ್ತು ಚಿಗುರು ಮೊಗ್ಗು ಉದುರುವುದನ್ನು 80% ರಷ್ಟು ಕಡಿಮೆ ಮಾಡುತ್ತದೆ. ಹತ್ತಿ ಮತ್ತು ತರಕಾರಿಗಳಲ್ಲಿ ಬಂಪರ್ ಇಳುವರಿ ನೀಡುತ್ತದೆ.",
        "manufacturer": "Bayer CropScience India",
        "buy_url": "https://www.bighaat.com/products/planofix-plant-growth-regulator",
        "compatible_with": "Compatible with most insecticides and fungicides. Follow exact dosage strictly."
    }
]

# ==============================================================================
# DISEASE & PEST SPECIFIC CROP PRESCRIPTIONS WITH EXACT DOSAGES
# ==============================================================================
CROP_PRESCRIPTIONS = [
    {
        "id": "paddy_blast",
        "crop_en": "Paddy (Rice)",
        "crop_kn": "ಭತ್ತ {Paddy / Rice}",
        "problem_en": "Rice Blast (Leaf & Neck Blast)",
        "problem_kn": "ಭತ್ತದ ಕುತ್ತಿಗೆ ಕೊಳೆ ರೋಗ & ಎಲೆ ಬೆಂಕಿ ರೋಗ {Rice Blast}",
        "type": "disease",
        "symptoms_en": "Spindle-shaped brown lesions on leaves with grey centers; dark rotting lesions at panicle neck causing heads to drop and produce empty chaff.",
        "symptoms_kn": "ಎಲೆಗಳ ಮೇಲೆ ಕಂದು ಅಂಚಿನ ಬೂದಿ ಬಣ್ಣದ ಮಚ್ಚೆಗಳು; ತೆನೆಯ ಕುತ್ತಿಗೆ ಕಪ್ಪಾಗಿ ಕೊಳೆತು ಧಾನ್ಯ ತುಂಬದೆ ಜೊಳ್ಳಾಗುವುದು.",
        "recommended_chemicals": [
            {
                "trade_name": "Beam / Baan / Tricyclazole 75% WP",
                "trade_name_kn": "ಬೀಮ್ / ಟ್ರೈಸೈಕ್ಲಜೋಲ್ 75% {Tricyclazole 75% WP}",
                "active": "Tricyclazole 75% WP",
                "dose_per_l": "0.6 g/L",
                "dose_per_pump_15l": "10 g per 15L pump",
                "action": "Systemic preventive & curative fungicide",
                "manufacturer": "Corteva / Rallis India"
            },
            {
                "trade_name": "Contaf Plus / Hexaconazole 5% SC",
                "trade_name_kn": "ಕಾಂಟಾಫ್ ಪ್ಲಸ್ / ಹೆಕ್ಸಾಕೊನಜೋಲ್ {Hexaconazole 5% SC}",
                "active": "Hexaconazole 5% SC",
                "dose_per_l": "2.0 ml/L",
                "dose_per_pump_15l": "30 ml per 15L pump",
                "action": "Broad-spectrum systemic triazole fungicide",
                "manufacturer": "Tata Rallis India"
            }
        ],
        "tank_mix_nutrition_en": "Add NPK 19:19:19 (75 g/pump) + Chelated Zinc EDTA 12% (15 g/pump) to restore damaged leaf area. Do NOT apply extra urea into standing water.",
        "tank_mix_nutrition_kn": "ಸಿಂಪರಣಾ ಟ್ಯಾಂಕ್‌ಗೆ {NPK 19:19:19} (75 ಗ್ರಾಂ/ಪಂಪ್) + ಚೆಲೇಟೆಡ್ ಸತು {Zinc 12%} (15 ಗ್ರಾಂ/ಪಂಪ್) ಬೆರೆಸಿ ಸಿಂಪಡಿಸಿ. ನಿಂತ ನೀರಿಗೆ ಯೂರಿಯಾ ಹಾಕಬೇಡಿ.",
        "spraying_measures_en": [
            "Spray in early morning (7 to 10 AM) after morning dew dries.",
            "Drain excess water from the paddy field if standing for more than 4 days.",
            "Clean field bunds of wild grassy weeds that host blast spores.",
            "Pre-harvest interval (PHI): Stop spraying 21 days before harvest."
        ],
        "spraying_measures_kn": [
            "ಮುಂಜಾನೆ ಇಬ್ಬನಿ ಆವಿಯಾದ ನಂತರ (7 ರಿಂದ 10 ಗಂಟೆ ಒಳಗೆ) ಸಿಂಪಡಿಸಿ.",
            "ಜಮೀನಿನಲ್ಲಿ 4 ದಿನಕ್ಕಿಂತ ಹೆಚ್ಚು ನೀರು ನಿಲ್ಲದಂತೆ ಹೆಚ್ಚುವರಿ ನೀರನ್ನು ಬಸಿದು ಹೊರಹಾಕಿ.",
            "ಬದುಗಳಲ್ಲಿರುವ ಕಳೆ ಹುಲ್ಲುಗಳನ್ನು ತೆಗೆದು ಸ್ವಚ್ಛಗೊಳಿಸಿ; ಇವು ರೋಗಾಣುಗಳನ್ನು ಹರಡುತ್ತವೆ.",
            "ಕೊಯ್ಲಿಗೆ 21 ದಿನಗಳ ಮುನ್ನ ಔಷಧ ಸಿಂಪಡಣೆಯನ್ನು ಕಡ್ಡಾಯವಾಗಿ ನಿಲ್ಲಿಸಿ {PHI}."
        ]
    },
    {
        "id": "paddy_bph",
        "crop_en": "Paddy (Rice)",
        "crop_kn": "ಭತ್ತ {Paddy / Rice}",
        "problem_en": "Brown Plant Hopper (BPH - ಜಿಗಿ ಹುಳು)",
        "problem_kn": "ಕಂದು ಜಿಗಿ ಹುಳು {Brown Plant Hopper - BPH}",
        "type": "pest",
        "symptoms_en": "Pests congregate at the base of the plant stem, sucking sap and causing circular yellow-brown patches in the field known as 'hopper burn'.",
        "symptoms_kn": "ಗಿಡದ ಬುಡದಲ್ಲಿ ಜಿಗಿ ಹುಳುಗಳು ಗುಂಪುಗೂಡಿ ರಸ ಹೀರುತ್ತವೆ. ಜಮೀನಿನಲ್ಲಿ ಬೆಳೆ ವೃತ್ತಾಕಾರವಾಗಿ ಒಣಗಿ ಸುಟ್ಟುಹೋದಂತೆ ಕಾಣುತ್ತದೆ ('ಹಾಪರ್ ಬರ್ನ್').",
        "recommended_chemicals": [
            {
                "trade_name": "Chess / Pymetrozine 50% WDG",
                "trade_name_kn": "ಚೆಸ್ / ಪೈಮೆಟ್ರೋಜೈನ್ {Pymetrozine 50% WDG}",
                "active": "Pymetrozine 50% WDG",
                "dose_per_l": "0.6 g/L",
                "dose_per_pump_15l": "10 g per 15L pump",
                "action": "Paralyzes sucking mouthparts of hoppers",
                "manufacturer": "Syngenta India"
            },
            {
                "trade_name": "Osheen / Token / Dinotefuran 20% SG",
                "trade_name_kn": "ಓಶಿನ್ / ಡೈನೋಟೆಫ್ಯುರಾನ್ {Dinotefuran 20% SG}",
                "active": "Dinotefuran 20% SG",
                "dose_per_l": "0.4 g/L",
                "dose_per_pump_15l": "6 - 8 g per 15L pump",
                "action": "Rapid systemic insecticide with strong translaminar action",
                "manufacturer": "PI Industries / Bharat Rasayan"
            }
        ],
        "tank_mix_nutrition_en": "Do NOT add nitrogenous fertilizers! Add Potassium Nitrate NPK 13:00:45 (80 g/pump) to thicken plant cell walls and impart pest resistance.",
        "tank_mix_nutrition_kn": "ಯಾವುದೇ ಯೂರಿಯಾ ಅಥವಾ ಸಾರಜನಕ ಗೊಬ್ಬರ ಹಾಕಬೇಡಿ! ಪೊಟ್ಯಾಸಿಯಂ ನೈಟ್ರೇಟ್ {NPK 13:00:45} (80 ಗ್ರಾಂ/ಪಂಪ್) ಬೆರೆಸಿ ಗಿಡದ ಕೋಶಗಳನ್ನು ಗಟ್ಟಿಗೊಳಿಸಿ.",
        "spraying_measures_en": [
            "Direct the spray nozzle straight at the base (bottom) of the stem, not on top of the canopy.",
            "Create 'alleyways' (skip one row every 2-3 meters) for sunlight and air circulation.",
            "Alternate wetting and drying (AWD) the field to break the hopper life cycle."
        ],
        "spraying_measures_kn": [
            "ಔಷಧದ ನಾಜಲ್ ಅನ್ನು ಎಲೆಗಳ ಮೇಲಲ್ಲ, ಗಿಡದ ಬುಡಕ್ಕೆ ನೇರವಾಗಿ ಮುಖಮಾಡಿ ಸಿಂಪಡಿಸಬೇಕು.",
            "ಗಾಳಿ-ಬೆಳಕು ಆಡಲು ಪ್ರತಿ 2-3 ಮೀಟರ್‌ಗೆ 'ದಾರಿ' (ಪಾಥ್) ಬಿಡಿ.",
            "ಗದ್ದೆಯ ನೀರನ್ನು ಸಂಪೂರ್ಣವಾಗಿ ಬಸಿದು 2-3 ದಿನ ಒಣಗಿಸಿ, ನಂತರ ಮತ್ತೆ ನೀರು ಕಟ್ಟಿ."
        ]
    },
    {
        "id": "cotton_pink_bollworm",
        "crop_en": "Cotton",
        "crop_kn": "ಹತ್ತಿ {Cotton}",
        "problem_en": "Pink Bollworm & American Bollworm",
        "problem_kn": "ಗುಲಾಬಿ ಕಾಯಿಕೊರೆಯುವ ಹುಳು {Pink Bollworm}",
        "type": "pest",
        "symptoms_en": "Rosetted flowers that fail to open ('rosette flower'); holes bored into green bolls plugged with excreta; stained damaged lint inside.",
        "symptoms_kn": "ಹೂವುಗಳು ಅರಳದೆ ಮುದುಡಿಕೊಳ್ಳುವುದು ('ರೋಸೆಟ್ ಫ್ಲವರ್'); ಎಳೆಯ ಕಾಯಿಗಳಿಗೆ ರಂಧ್ರ ಕೊರೆದು ಒಳಗೆ ಹತ್ತಿ ಬೀಜ ಮತ್ತು ನೂಲನ್ನು ತಿಂದು ಕಪ್ಪಾಗಿಸುವುದು.",
        "recommended_chemicals": [
            {
                "trade_name": "Coragen / Chlorantraniliprole 18.5% SC",
                "trade_name_kn": "ಕೊರಾಜನ್ {Chlorantraniliprole 18.5% SC}",
                "active": "Chlorantraniliprole 18.5% SC",
                "dose_per_l": "0.3 ml/L",
                "dose_per_pump_15l": "5 ml per 15L pump",
                "action": "Activates ryanodine receptor, paralyzing caterpillars",
                "manufacturer": "FMC India"
            },
            {
                "trade_name": "Proclaim / Emamectin Benzoate 5% SG",
                "trade_name_kn": "ಪ್ರೊಕ್ಲೇಮ್ / ಎಮಾಮೆಕ್ಟಿನ್ ಬೆಂಜೋಯೇಟ್ {Emamectin Benzoate 5% SG}",
                "active": "Emamectin Benzoate 5% SG",
                "dose_per_l": "0.4 g/L",
                "dose_per_pump_15l": "6 - 7 g per 15L pump",
                "action": "Stomach and contact poison for Lepidopteran larvae",
                "manufacturer": "Syngenta India / Dhanuka"
            }
        ],
        "tank_mix_nutrition_en": "Mix with Planofix PGR (4 ml/pump) + Boron 20% (15 g/pump) + NPK 00:52:34 (75 g/pump) to stop flower/square drop and boost boll retention.",
        "tank_mix_nutrition_kn": "ಪ್ಲಾನೋಫಿಕ್ಸ್ {Planofix} (4 ಮಿಲಿ/ಪಂಪ್) + ಬೋರಾನ್ 20% (15 ಗ್ರಾಂ/ಪಂಪ್) + {NPK 00:52:34} (75 ಗ್ರಾಂ) ಬೆರೆಸಿ ಸಿಂಪಡಿಸಿದರೆ ಹೂಮೊಗ್ಗು ಉದುರುವುದು ನಿಂತು ಕಾಯಿ ದಪ್ಪವಾಗುತ್ತದೆ.",
        "spraying_measures_en": [
            "Install 4 to 5 pheromone traps per acre to monitor moth catches (spray when 8 moths/trap/night for 3 days).",
            "Spray in the evening when larvae emerge from eggshells.",
            "Collect and destroy fallen rosette flowers and infested bolls."
        ],
        "spraying_measures_kn": [
            "ಪ್ರತಿ ಎಕರೆಗೆ 4-5 ಮೋಹಕ ಬಲೆಗಳನ್ನು (ಫೆರಮೋನ್ ಟ್ರ್ಯಾಪ್) ಕಟ್ಟಿ ಪತಂಗಗಳ ಸಂಖ್ಯೆ ಗಮನಿಸಿ.",
            "ಸಂಜೆ 4 ಗಂಟೆಯ ನಂತರ ಸಿಂಪಡಿಸಿ; ಆಗ ಕೀಟಗಳು ಚುರುಕಾಗಿರುತ್ತವೆ.",
            "ಉದುರಿದ ಮುದುಡಿದ ಹೂವುಗಳು ಮತ್ತು ಕೊಳೆತ ಕಾಯಿಗಳನ್ನು ಆರಿಸಿ ಮಣ್ಣಿನಲ್ಲಿ ಹೂತುಹಾಕಿ."
        ]
    },
    {
        "id": "chilli_murda_complex",
        "crop_en": "Chilli & Capsicum",
        "crop_kn": "ಮೆಣಸಿನಕಾಯಿ {Chilli / Capsicum}",
        "problem_en": "Chilli Leaf Curl & Murda Complex (Thrips & Mites)",
        "problem_kn": "ಮೆಣಸಿನಕಾಯಿ ಮುರಡ ರೋಗ / ಎಲೆ ಮುದುಡು ರೋಗ {Chilli Leaf Curl}",
        "type": "pest",
        "symptoms_en": "Upward leaf curling ('boat shape') caused by thrips; downward curling ('inverted boat') caused by mites; stunted bushy growth.",
        "symptoms_kn": "ಎಲೆಗಳು ದೋಣಿಯಾಕಾರದಲ್ಲಿ ಮೇಲ್ಮುಖವಾಗಿ ಮುದುಡುವುದು (ನುಸಿ/ಜಿಗಟು); ಎಲೆಗಳು ಕೆಳಮುಖವಾಗಿ ಮುದುಡುವುದು (ಕೆಂಪು ಜೀರುಂಡೆ/ಮೈಟ್ಸ್). ಗಿಡ ಗಿಡ್ಡವಾಗಿ ನಿಲ್ಲುವುದು.",
        "recommended_chemicals": [
            {
                "trade_name": "Ulala / Flonicamid 50% WG",
                "trade_name_kn": "ಉಲಾಲಾ / ಫ್ಲೋನಿಕಾಮಿಡ್ {Flonicamid 50% WG}",
                "active": "Flonicamid 50% WG",
                "dose_per_l": "0.35 g/L",
                "dose_per_pump_15l": "6 g per 15L pump",
                "action": "Selective feeding blocker for sap-sucking thrips & whiteflies",
                "manufacturer": "UPL India"
            },
            {
                "trade_name": "Oberon / Spiromesifen 22.9% SC",
                "trade_name_kn": "ಒಬೆರಾನ್ / ಸ್ಪೈರೋಮೆಸಿಫೆನ್ {Spiromesifen 22.9% SC}",
                "active": "Spiromesifen 22.9% SC",
                "dose_per_l": "1.0 ml/L",
                "dose_per_pump_15l": "15 ml per 15L pump",
                "action": "Lipid biosynthesis inhibitor against mites and whitefly nymphs",
                "manufacturer": "Bayer CropScience India"
            }
        ],
        "tank_mix_nutrition_en": "Tank mix with Micronutrient Grade IV (35 g/pump) + Sagarika Biostimulant (40 ml/pump) to restart stunted apical vegetative flush.",
        "tank_mix_nutrition_kn": "ಸೂಕ್ಷ್ಮ ಪೋಷಕಾಂಶ ಗ್ರೇಡ್-IV {Grade IV} (35 ಗ್ರಾಂ/ಪಂಪ್) + ಸಾಗರಿಕ ದ್ರಾವಣ (40 ಮಿಲಿ/ಪಂಪ್) ಬೆರೆಸಿ ಸಿಂಪಡಿಸಿದರೆ ಗಿಡ ಹೊಸ ಹಸಿರು ಚಿಗುರು ಒಡೆಯುತ್ತದೆ.",
        "spraying_measures_en": [
            "Install blue sticky traps for thrips and yellow sticky traps for whiteflies (10 per acre).",
            "Use a hollow cone nozzle and ensure under-surface leaf coverage.",
            "Maintain soil moisture; drought stress aggravates mite infestation."
        ],
        "spraying_measures_kn": [
            "ಎಕರೆಗೆ 10 ಹಳದಿ ಮತ್ತು 10 ನೀಲಿ ಅಂಟು ಬಲೆಗಳನ್ನು ಕಟ್ಟಿ ಕೀಟಗಳನ್ನು ನಿಯಂತ್ರಿಸಿ.",
            "ಎಲೆಯ ಹಿಂಭಾಗ ಸಂಪೂರ್ಣವಾಗಿ ನೆನೆಯುವಂತೆ ಕೆಳಗಿನಿಂದ ಮೇಲಕ್ಕೆ ಸಿಂಪಡಿಸಿ.",
            "ಜಮೀನಿನಲ್ಲಿ ತೇವಾಂಶ ಕಾಪಾಡಿಕೊಳ್ಳಿ; ಒಣ ಹವೆ ಇದ್ದಾಗ ನುಸಿ ಹುಳುಗಳು ತೀವ್ರವಾಗುತ್ತವೆ."
        ]
    },
    {
        "id": "tomato_early_late_blight",
        "crop_en": "Tomato",
        "crop_kn": "ಟೊಮೆಟೊ {Tomato}",
        "problem_en": "Early Blight & Late Blight",
        "problem_kn": "ಟೊಮೆಟೊ ಅಂಗಮಾರಿ & ಸುಡು ರೋಗ {Early & Late Blight}",
        "type": "disease",
        "symptoms_en": "Concentric rings ('target board') on lower leaves (early blight); water-soaked black patches on leaves and brown sunken rot on green fruit (late blight).",
        "symptoms_kn": "ಕೆಳಭಾಗದ ಎಲೆಗಳ ಮೇಲೆ ಗುರಿಯ ಹಲಗೆಯಂತಹ {Target board} ವೃತ್ತಾಕಾರದ ಕಪ್ಪು ಕಲೆಗಳು; ಕಾಯಿಗಳ ಮೇಲೆ ಕಂದು ಕೊಳೆತ ಗುಳಿಗಳು.",
        "recommended_chemicals": [
            {
                "trade_name": "Ridomil Gold / Metalaxyl-M 4% + Mancozeb 64% WP",
                "trade_name_kn": "ರಿಡೋಮಿಲ್ ಗೋಲ್ಡ್ {Ridomil Gold}",
                "active": "Metalaxyl-M 4% + Mancozeb 64% WP",
                "dose_per_l": "2.5 g/L",
                "dose_per_pump_15l": "35 - 40 g per 15L pump",
                "action": "Systemic and contact oomycete fungicide",
                "manufacturer": "Syngenta India"
            },
            {
                "trade_name": "Amistar Top / Azoxystrobin 18.2% + Difenoconazole 11.4% SC",
                "trade_name_kn": "ಅಮಿಸ್ಟಾರ್ ಟಾಪ್ {Amistar Top}",
                "active": "Azoxystrobin 18.2% + Difenoconazole 11.4% SC",
                "dose_per_l": "1.0 ml/L",
                "dose_per_pump_15l": "15 ml per 15L pump",
                "action": "Broad-spectrum strobilurin + triazole fungicide",
                "manufacturer": "Syngenta India"
            }
        ],
        "tank_mix_nutrition_en": "Mix with Boron 20% (15 g/pump) to stop fruit cracking, and NPK 00:52:34 (70 g/pump) for heavy fruit set.",
        "tank_mix_nutrition_kn": "ಹಣ್ಣು ಬಿರುಕು ಬಿಡುವುದನ್ನು ತಡೆಯಲು ಬೋರಾನ್ 20% (15 ಗ್ರಾಂ/ಪಂಪ್) ಮತ್ತು {NPK 00:52:34} (70 ಗ್ರಾಂ/ಪಂಪ್) ಬೆರೆಸಿ ಸಿಂಪಡಿಸಿ.",
        "spraying_measures_en": [
            "Stake tomato plants with bamboo poles to keep leaves and fruit away from moist soil.",
            "Prune lower infected leaves touching the soil.",
            "Avoid overhead sprinkler irrigation during cloudy or humid weather."
        ],
        "spraying_measures_kn": [
            "ಗಿಡಗಳನ್ನು ಬಿದಿರಿನ ಕೋಲುಗಳಿಗೆ ಕಟ್ಟಿ ಮಣ್ಣಿನಿಂದ ಮೇಲಕ್ಕೆ ನಿಲ್ಲಿಸಿ.",
            "ಮಣ್ಣಿಗೆ ತಾಗುತ್ತಿರುವ ಕೆಳಗಿನ ರೋಗಪೀಡಿತ ಎಲೆಗಳನ್ನು ಕತ್ತರಿಸಿ ತೆಗೆಯಿರಿ.",
            "ಮೋಡ ಕವಿದ ವಾತಾವರಣದಲ್ಲಿ ಸಂಜೆ ವೇಳೆ ನೀರು ಹಾಯಿಸಬೇಡಿ."
        ]
    },
    {
        "id": "maize_fall_armyworm",
        "crop_en": "Maize",
        "crop_kn": "ಮೆಕ್ಕೆಜೋಳ {Maize}",
        "problem_en": "Fall Armyworm (FAW - ಸೈನಿಕ ಹುಳು)",
        "problem_kn": "ಮೆಕ್ಕೆಜೋಳದ ಸೈನಿಕ ಹುಳು {Fall Armyworm - FAW}",
        "type": "pest",
        "symptoms_en": "Pin-holes on young leaves expanding into ragged elongated tears; heavy sawdust-like frass inside the central leaf whorl; damaged cob silks.",
        "symptoms_kn": "ಎಲೆಗಳ ಮೇಲೆ ರಂಧ್ರಗಳು ಮತ್ತು ಹರಿದಂತಹ ಗುರುತುಗಳು; ಸುಳಿಯ ಒಳಗೆ ಮರದ ಪುಡಿಯಂತಹ ಹಿಕ್ಕೆ; ತೆನೆ ಕೊರೆದು ಹಾಳುಮಾಡುವುದು.",
        "recommended_chemicals": [
            {
                "trade_name": "Coragen / Chlorantraniliprole 18.5% SC",
                "trade_name_kn": "ಕೊರಾಜನ್ {Coragen 18.5% SC}",
                "active": "Chlorantraniliprole 18.5% SC",
                "dose_per_l": "0.4 ml/L",
                "dose_per_pump_15l": "6 ml per 15L pump",
                "action": "Systemic stomach insecticide with long residual control",
                "manufacturer": "FMC India"
            },
            {
                "trade_name": "Delegate / Spinetoram 11.7% SC",
                "trade_name_kn": "ಡೆಲಿಗೇಟ್ / ಸ್ಪಿನೆಟೋರಾಮ್ {Spinetoram 11.7% SC}",
                "active": "Spinetoram 11.7% SC",
                "dose_per_l": "0.5 ml/L",
                "dose_per_pump_15l": "8 ml per 15L pump",
                "action": "Fermentation-derived green-chemistry spinosyn insecticide",
                "manufacturer": "Corteva Agriscience India"
            }
        ],
        "tank_mix_nutrition_en": "Add Chelated Zinc EDTA 12% (15 g/pump) + Nano Urea (40 ml/pump) to spur new whorl emergence and overcome chewing shock.",
        "tank_mix_nutrition_kn": "ಚೆಲೇಟೆಡ್ ಸತು {Zinc 12%} (15 ಗ್ರಾಂ/ಪಂಪ್) + ನ್ಯಾನೋ ಯೂರಿಯಾ (40 ಮಿಲಿ/ಪಂಪ್) ಬೆರೆಸಿ ಸಿಂಪಡಿಸಿದರೆ ಸುಳಿ ವೇಗವಾಗಿ ಬೆಳೆದು ಗರಿಷ್ಠ ತೆನೆ ಕಟ್ಟುತ್ತದೆ.",
        "spraying_measures_en": [
            "Crucial: Target the spray nozzle directly into the central whorl of every plant.",
            "Spray in the early morning (before 9 AM) or late evening when caterpillars come out of the whorl.",
            "Apply sand + lime mixture (9:1 ratio) into the whorl for small farm plots as a zero-cost physical deterrent."
        ],
        "spraying_measures_kn": [
            "ಮುಖ್ಯ ಸೂಚನೆ: ಔಷಧದ ನಾಜಲ್ ಅನ್ನು ನೇರವಾಗಿ ಗಿಡದ ಸುಳಿಯ (ಸೆಂಟರ್ ವರ್ಲ್) ಒಳಗೆ ಸಿಂಪಡಿಸಬೇಕು.",
            "ಮುಂಜಾನೆ 9 ಗಂಟೆ ಒಳಗೆ ಅಥವಾ ಸಂಜೆ ವೇಳೆ ಸಿಂಪಡಿಸಿ.",
            "ಸುಳಿಗೆ ಮರಳು ಮತ್ತು ಸುಣ್ಣದ ಪುಡಿ (9:1 ಪ್ರಮಾಣ) ಹಾಕುವುದರಿಂದ ಹುಳುಗಳು ಹೊರಬರುತ್ತವೆ."
        ]
    },
    {
        "id": "groundnut_tikka",
        "crop_en": "Groundnut",
        "crop_kn": "ಕಡಲೆಕಾಯಿ {Groundnut}",
        "problem_en": "Tikka Leaf Spot & Rust",
        "problem_kn": "ಕಡಲೆಕಾಯಿ ತಿಕ್ಕಾ ರೋಗ / ಎಲೆ ಚುಕ್ಕೆ ರೋಗ & ತುಕ್ಕು ರೋಗ {Tikka Disease}",
        "type": "disease",
        "symptoms_en": "Small circular dark brown to black spots with a bright yellow halo on upper leaf surfaces; severe defoliation and shrivelled pods.",
        "symptoms_kn": "ಎಲೆಗಳ ಮೇಲೆ ಹಳದಿ ಅಂಚುಳ್ಳ ದುಂಡನೆಯ ಕಪ್ಪು ಚುಕ್ಕೆಗಳು; ಎಲೆಗಳು ಉದುರಿ ಕಾಳು ಕಟ್ಟದೆ ಬರಿ ಜೊಳ್ಳಾಗುವುದು.",
        "recommended_chemicals": [
            {
                "trade_name": "Saaf / Carbendazim 12% + Mancozeb 63% WP",
                "trade_name_kn": "ಸಾಫ್ {Saaf - Carbendazim + Mancozeb}",
                "active": "Carbendazim 12% + Mancozeb 63% WP",
                "dose_per_l": "2.0 g/L",
                "dose_per_pump_15l": "30 g per 15L pump",
                "action": "Dual contact and systemic fungicide",
                "manufacturer": "UPL India"
            },
            {
                "trade_name": "Folicur / Tebuconazole 25.9% EC",
                "trade_name_kn": "ಫೋಲಿಕೂರ್ / ಟೆಬುಕೊನಜೋಲ್ {Tebuconazole 25.9% EC}",
                "active": "Tebuconazole 25.9% EC",
                "dose_per_l": "1.25 ml/L",
                "dose_per_pump_15l": "20 ml per 15L pump",
                "action": "Ergosterol demethylation inhibitor systemic fungicide",
                "manufacturer": "Bayer CropScience India"
            }
        ],
        "tank_mix_nutrition_en": "Mix with Boron 20% (15 g/pump) + NPK 13:00:45 (80 g/pump) during pegging/pod formation to ensure bold oil-rich kernels.",
        "tank_mix_nutrition_kn": "ಊಟೆ ಇಳಿಯುವ ಹಂತದಲ್ಲಿ ಬೋರಾನ್ 20% (15 ಗ್ರಾಂ/ಪಂಪ್) + {NPK 13:00:45} (80 ಗ್ರಾಂ/ಪಂಪ್) ಬೆರೆಸಿ ಸಿಂಪಡಿಸಿದರೆ ದಪ್ಪ ಕಡಲೆಕಾಯಿ ಕಾಳುಗಳು ತುಂಬುತ್ತವೆ.",
        "spraying_measures_en": [
            "Apply Gypsum at 200 kg/acre at 40-45 days after sowing (flowering stage) to enhance shell calcium.",
            "Spray fungicide immediately at first appearance of spots (usually 35-40 days after sowing).",
            "Burn or bury infected crop residue after harvest."
        ],
        "spraying_measures_kn": [
            "ಬಿತ್ತಿದ 40-45 ದಿನಗಳಲ್ಲಿ ಎಕರೆಗೆ 200 ಕೆಜಿ ಜಿಪ್ಸಮ್ ಮಣ್ಣಿಗೆ ಹಾಕಿ ಮಣ್ಣು ಏರಿಸಿ.",
            "ಚುಕ್ಕೆಗಳು ಕಂಡ ತಕ್ಷಣವೇ ತಡಮಾಡದೆ ಸಿಂಪಡಿಸಿ.",
            "ಕೊಯ್ಲಿನ ನಂತರ ರೋಗಪೀಡಿತ ಗಿಡದ ತ್ಯಾಜ್ಯವನ್ನು ನಾಶಪಡಿಸಿ."
        ]
    }
]

# ==============================================================================
# TANK-MIX COMPATIBILITY MATRIX
# ==============================================================================
TANK_MIX_RULES = [
    {
        "status": "SAFE",
        "title_en": "SAFE COMBINATIONS (Can be mixed in the same pump)",
        "title_kn": "ಸುರಕ್ಷಿತ ಮಿಶ್ರಣಗಳು (ಒಂದೇ ಪಂಪ್‌ನಲ್ಲಿ ಒಟ್ಟಿಗೆ ಬೆರೆಸಬಹುದು)",
        "items_en": [
            "Systemic Fungicide (e.g. Hexaconazole, Tricyclazole) + Insecticide (e.g. Coragen, Proclaim).",
            "Water Soluble Fertilizer (19:19:19, 00:52:34, 13:00:45) + Most Fungicides & Insecticides.",
            "IFFCO Sagarika Biostimulant + Nano Urea + Standard Fungicide/Insecticide.",
            "Chelated Micronutrients (Boron 20%, Zinc EDTA 12%) + Foliar Fertilizers (00:52:34).",
            "Silicon Spreader/Sticker (e.g. Apsa-80, Silwet) (5 ml/pump) can be added to any foliar spray."
        ],
        "items_kn": [
            "ಶಿಲೀಂಧ್ರನಾಶಕ (ಹೆಕ್ಸಾಕೊನಜೋಲ್, ಟ್ರೈಸೈಕ್ಲಜೋಲ್) + ಕೀಟನಾಶಕ (ಕೊರಾಜನ್, ಪ್ರೊಕ್ಲೇಮ್).",
            "ನೀರಿನಲ್ಲಿ ಕರಗುವ ರಸಗೊಬ್ಬರ (19:19:19, 00:52:34) + ಕೀಟನಾಶಕಗಳು.",
            "ಇಫ್ಕೋ ಸಾಗರಿಕ ಬಯೋ-ಸ್ಟಿಮ್ಯುಲಂಟ್ + ನ್ಯಾನೋ ಯೂರಿಯಾ + ಶಿಲೀಂಧ್ರನಾಶಕ.",
            "ಚೆಲೇಟೆಡ್ ಬೋರಾನ್ 20% + ಸತು ಜಿಂಕ್ 12% + ಕರಗುವ ರಸಗೊಬ್ಬರ.",
            "ಸಿಲಿಕಾನ್ ಸ್ಟಿಕ್ಕರ್ / ಅಂಟು ದ್ರಾವಣವನ್ನು (5 ಮಿಲಿ/ಪಂಪ್) ಯಾವುದೇ ಎಲೆ ಸಿಂಪರಣೆಗೆ ಬೆರೆಸಬಹುದು."
        ]
    },
    {
        "status": "UNSAFE",
        "title_en": "STRICTLY PROHIBITED (NEVER MIX - Destroys crop & chemical efficacy)",
        "title_kn": "ಕಡ್ಡಾಯವಾಗಿ ಬೆರೆಸಬಾರದು (ಬೆಳೆ ಸುಟ್ಟುಹೋಗುತ್ತದೆ ಅಥವಾ ಔಷಧ ನಿಷ್ಕ್ರಿಯಗೊಳ್ಳುತ್ತದೆ)",
        "items_en": [
            "NEVER mix Weedicides (herbicides like Glyphosate, 2,4-D, Paraquat) with any insecticide or fertilizer! Dedicate a separate sprayer for weedicides.",
            "NEVER mix Copper Oxychloride (COC) or Bordeaux Mixture with other chemicals or bio-fertilizers (inactivates systemic chemicals and kills beneficial microbes).",
            "NEVER mix Sulphur fungicides with Emulsifiable Concentrates (EC) or oils in hot weather (burns leaves).",
            "NEVER mix Calcium Nitrate with Phosphorus or Sulphate fertilizers (forms insoluble rocky precipitate that blocks pump nozzles).",
            "NEVER mix Bio-control agents (Trichoderma, Pseudomonas) with synthetic chemical fungicides."
        ],
        "items_kn": [
            "ಕಳೆನಾಶಕಗಳನ್ನು (ಗ್ಲೈಫೋಸೇಟ್, 2,4-D) ಯಾವುದೇ ಕಾರಣಕ್ಕೂ ಕೀಟನಾಶಕ ಅಥವಾ ಗೊಬ್ಬರದೊಂದಿಗೆ ಬೆರೆಸಬೇಡಿ! ಕಳೆನಾಶಕಕ್ಕೆ ಪ್ರತ್ಯೇಕ ಪಂಪ್ ಇರಲಿ.",
            "ತಾಮ್ರದ ಶಿಲೀಂಧ್ರನಾಶಕಗಳನ್ನು {COC / ಬೋರ್ಡೋ ದ್ರಾವಣ} ಇತರ ರಾಸಾಯನಿಕಗಳೊಂದಿಗೆ ಅಥವಾ ಜೈವಿಕ ಗೊಬ್ಬರಗಳೊಂದಿಗೆ ಬೆರೆಸಬೇಡಿ.",
            "ಗಂಧಕವನ್ನು {Sulphur} ಬಿಸಿಲಿನಲ್ಲಿ ತೈಲ ಆಧಾರಿತ ಕೀಟನಾಶಕಗಳೊಂದಿಗೆ {EC} ಬೆರೆಸಬೇಡಿ (ಎಲೆಗಳು ಸುಟ್ಟುಹೋಗುತ್ತವೆ).",
            "ಕ್ಯಾಲ್ಸಿಯಂ ನೈಟ್ರೇಟ್ ಅನ್ನು ರಂಜಕ ಅಥವಾ ಸಲ್ಫೇಟ್ ಗೊಬ್ಬರಗಳೊಂದಿಗೆ ಬೆರೆಸಬೇಡಿ (ಪಾಚಿ ಕಟ್ಟಿ ಪಂಪ್ ನಾಜಲ್ ಜಾಮ್ ಆಗುತ್ತದೆ).",
            "ಟ್ರೈಕೋಡರ್ಮ ಅಥವಾ ಸ್ಯೂಡೋಮೊನಾಸ್ ಜೈವಿಕ ಶಿಲೀಂಧ್ರನಾಶಕಗಳನ್ನು ರಾಸಾಯನಿಕ ಶಿಲೀಂಧ್ರನಾಶಕಗಳೊಂದಿಗೆ ಬೆರೆಸಬಾರದು."
        ]
    }
]

# ==============================================================================
# WATER VOLUME & SPRAYER CONSTANTS
# ==============================================================================
SPRAYER_CONFIGS = {
    "knapsack_15": {
        "name_en": "Backpack Manual/Battery Knapsack Pump (15 Litres)",
        "name_kn": "ಬ್ಯಾಟರಿ / ಕೈ ಚಾಲಿತ ಬೆನ್ನು ಪಂಪ್ {15 ಲೀಟರ್}",
        "volume_l": 15,
        "pumps_per_acre_field_crop": 10,   # 150 L / acre
        "pumps_per_acre_vegetables": 13,   # 200 L / acre
    },
    "knapsack_16": {
        "name_en": "Heavy Battery Sprayer (16 Litres)",
        "name_kn": "ದೊಡ್ಡ ಬ್ಯಾಟರಿ ಸ್ಪ್ರೇಯರ್ {16 ಲೀಟರ್}",
        "volume_l": 16,
        "pumps_per_acre_field_crop": 9,    # ~144 L / acre
        "pumps_per_acre_vegetables": 12,   # ~192 L / acre
    },
    "tractor_barrel_200": {
        "name_en": "Power Sprayer / Tractor Mounted Barrel (200 Litres)",
        "name_kn": "ಟ್ರಾಕ್ಟರ್ / ಪವರ್ ಸ್ಪ್ರೇಯರ್ ಬ್ಯಾರೆಲ್ {200 ಲೀಟರ್}",
        "volume_l": 200,
        "pumps_per_acre_field_crop": 1,    # 200 L / acre
        "pumps_per_acre_vegetables": 1.25, # 250 L / acre
    }
}

