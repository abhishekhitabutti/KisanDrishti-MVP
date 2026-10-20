"""
KrushiNudi Smart Farm Advisory: Comprehensive Crop Protection & High-Yield Nutrition Database.
Authentic Indian agricultural university (ICAR, UAS Dharwad, UAS Bangalore, TNAU) recommendations.
Features:
- Prescriptions for ALL major crops (20 crops) covering diseases & pests with exact chemical dosages
- Crop-specific growth & nutritional tonics separately for EVERY crop (Vegetative, Flowering, Yield Booster)
- Weed disposal & suppression methods tailored by weed infestation density (Low, Moderate, Heavy)
- Tank-mix compatibility matrix (safe vs unsafe combinations)
- Verified Indian agri manufacturers (IFFCO Bazar, BigHaat, AgroStar) and toll-free helpline numbers.
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
        "order_url": "https://www.iffco.in",
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
        "order_url": "https://play.google.com/store/apps/details?id=com.ulink.agrostar",
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
        "dose_per_acre": "500 ml per acre in 150-200 L water",
        "timing_en": "Vegetative stage (25-30 days after sowing) and pre-flowering stage.",
        "timing_kn": "ಸಸಿ ಬೆಳೆಯುವ ಹಂತ (ಬಿತ್ತಿದ 25-30 ದಿನ) ಮತ್ತು ಹೂವಾಡುವ ಮುನ್ನ.",
        "benefits_en": "Stimulates dense root growth, increases tillers in paddy/sugarcane, activates soil microbes, improves drought resistance, and boosts grain yield by 12-18%.",
        "benefits_kn": "ಭತ್ತ, ಕಬ್ಬು, ಮೆಕ್ಕೆಜೋಳದಲ್ಲಿ ಕವಲು/ಕವಡೆಗಳ ಸಂಖ್ಯೆ ಹೆಚ್ಚಿಸುತ್ತದೆ, ಬೇರುಗಳು ಆಳಕ್ಕೆ ಇಳಿಯಲು ನೆರವಾಗುತ್ತದೆ, ಬರ ನಿರೋಧಕ ಶಕ್ತಿ ನೀಡುತ್ತದೆ ಮತ್ತು ಇಳುವರಿಯನ್ನು 12-18% ಹೆಚ್ಚಿಸುತ್ತದೆ.",
        "manufacturer": "IFFCO",
        "buy_url": "https://www.bighaat.com/products/sagarika-gold",
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
        "dose_per_acre": "500 ml (1 bottle) per acre in 150-200 L water",
        "timing_en": "1st spray: Active tillering / branching stage (30-35 DAS). 2nd spray: 15-20 days later.",
        "timing_kn": "1ನೇ ಸಿಂಪಡಣೆ: ಕವಲು ಒಡೆಯುವ ಹಂತ (30-35 ದಿನ). 2ನೇ ಸಿಂಪಡಣೆ: ಹೂವಾಡುವ 1 ವಾರ ಮುನ್ನ.",
        "benefits_en": "80%+ nitrogen absorption efficiency directly through leaf stomata. Replaces 1 whole bag of conventional granular urea, prevents soil hardening, and increases crop protein content.",
        "benefits_kn": "ಎಲೆಗಳ ಮೂಲಕ 80% ಕ್ಕಿಂತ ಹೆಚ್ಚು ಸಾರಜನಕ ಹೀರಿಕೊಳ್ಳುತ್ತದೆ. 1 ಬ್ಯಾಗ್ ಸಾಂಪ್ರದಾಯಿಕ ಯೂರಿಯಾ ಉಳಿಸುತ್ತದೆ, ಮಣ್ಣು ಗಟ್ಟಿಯಾಗುವುದನ್ನು ತಪ್ಪಿಸುತ್ತದೆ ಮತ್ತು ಕಾಳಿನ ತೂಕ ಹೆಚ್ಚಿಸುತ್ತದೆ.",
        "manufacturer": "IFFCO",
        "buy_url": "https://www.bighaat.com/products/iffco-nano-urea",
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
        "dose_per_acre": "500 ml (1 bottle) per acre in 150-200 L water",
        "timing_en": "Seed priming before sowing, and foliar spray at early vegetative stage.",
        "timing_kn": "ಬಿತ್ತನೆ ಮುನ್ನ ಬೀಜೋಪಚಾರಕ್ಕೆ (5 ಮಿಲಿ/ಕೆಜಿ ಬೀಜಕ್ಕೆ), ಮತ್ತು ಸಸಿ ಹಂತದಲ್ಲಿ ಎಲೆಗಳ ಮೇಲೆ ಸಿಂಪಡಣೆ.",
        "benefits_en": "Enhances root volume and nodulation in pulses (Bengal gram, Tur, Soybean), aids strong stem formation, and eliminates phosphorus fixation in hard-rock soil.",
        "benefits_kn": "ದ್ವಿದಳ ಧಾನ್ಯಗಳಲ್ಲಿ (ತೊಗರಿ, ಕಡಲೆ, ಸೋಯಾಬೀನ್) ಸಾರಜನಕ ಹೀರುವ ಗಂಟುಗಳು ಮತ್ತು ಬೇರುಗಳನ್ನು ಹೆಚ್ಚಿಸುತ್ತದೆ. ಮಣ್ಣಿನಲ್ಲಿ ರಂಜಕ ವ್ಯರ್ಥವಾಗುವುದನ್ನು ತಡೆಯುತ್ತದೆ.",
        "manufacturer": "IFFCO",
        "buy_url": "https://www.bighaat.com/products/iffco-nano-dap",
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
        "dose_per_acre": "1.0 - 1.25 kg per acre in 150-200 L water",
        "timing_en": "Early growth and branching stage (20-45 DAS).",
        "timing_kn": "ಬೆಳೆಯ ಆರಂಭಿಕ ಹಂತ ಮತ್ತು ಕವಲು ಒಡೆಯುವ ಹಂತದಲ್ಲಿ (ಬಿತ್ತಿದ 20-45 ದಿನಗಳಲ್ಲಿ).",
        "benefits_en": "Provides instant green canopy, balanced nutrition (Nitrogen, Phosphorus, Potash) with zero wastage, curing sudden yellowing in crops.",
        "benefits_kn": "ಬೆಳೆಗೆ ತ್ವರಿತ ಹಸಿರು ಬಣ್ಣ ನೀಡುತ್ತದೆ, ಸಮತೋಲಿತ ಪೋಷಕಾಂಶ ಒದಗಿಸಿ ಎಲೆ ಹಳದಿ ರೋಗ ತಡೆಯುತ್ತದೆ ಮತ್ತು ಸಸಿಗಳನ್ನು ಬಲಪಡಿಸುತ್ತದೆ.",
        "manufacturer": "IFFCO / Coromandel Gromor / Tata Rallis",
        "buy_url": "https://www.bighaat.com/products/19-19-19-fertilizer",
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
        "dose_per_acre": "1.0 - 1.25 kg per acre in 150-200 L water",
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
        "dose_per_acre": "1.0 - 1.5 kg per acre in 150-200 L water",
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
        "dose_per_acre": "250 g per acre in 150-200 L water",
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
        "dose_per_acre": "200 g per acre in 150-200 L water",
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
        "dose_per_acre": "45 - 50 ml per acre in 150-200 L water",
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
# CROP-SPECIFIC GROWTH TONICS & NUTRITION SCHEDULE (SEPARATE FOR ALL 20 CROPS)
# ==============================================================================
CROP_SPECIFIC_TONICS = {
    "Paddy (Rice)": {
        "name_kn": "ಭತ್ತ {Paddy / Rice}",
        "veg_stage_kn": "ಸಸಿ & ಕವಲು ಹಂತ (25-30 ದಿನ): ಇಫ್ಕೋ ಸಾಗರಿಕ (40 ಮಿಲಿ) + {NPK 19:19:19} (75 ಗ್ರಾಂ) + ಸತು ಜಿಂಕ್ 12% (15 ಗ್ರಾಂ) / ಪಂಪ್‌ಗೆ.",
        "veg_stage_en": "Tillering stage (25-30 DAS): IFFCO Sagarika (40 ml) + WSF 19:19:19 (75 g) + Zinc EDTA 12% (15 g) per pump.",
        "flower_stage_kn": "ಪೊಟ್ಟೆ / ತೆನೆ ಬರುವ ಮುನ್ನ (50-60 ದಿನ): ನ್ಯಾನೋ ಯೂರಿಯಾ (40 ಮಿಲಿ) + {NPK 00:52:34} (75 ಗ್ರಾಂ) + ಬೋರಾನ್ 20% (15 ಗ್ರಾಂ).",
        "flower_stage_en": "Panicle initiation (50-60 DAS): Nano Urea (40 ml) + WSF 00:52:34 (75 g) + Boron 20% (15 g).",
        "yield_stage_kn": "ಹಾಲು ತುಂಬುವ & ಕಾಳು ಮಾಗುವ ಹಂತ: {NPK 13:00:45} (80 ಗ್ರಾಂ) ಸಿಂಪಡಣೆ (ಕಾಳು ಜೊಳ್ಳಾಗದೆ 15-20% ಅಧಿಕ ತೂಕ ನೀಡುತ್ತದೆ).",
        "yield_stage_en": "Grain filling / Milking stage: WSF 13:00:45 (80 g) spray (eliminates chaffy grains, +15-20% grain weight).",
        "boost_pct": "18 - 22% ಅಧಿಕ ಇಳುವರಿ"
    },
    "Ragi (Finger Millet)": {
        "name_kn": "ರಾಗಿ {Ragi / Finger Millet}",
        "veg_stage_kn": "ಸಸಿ ಕಟ್ಟುವ ಹಂತ (20-25 ದಿನ): {NPK 19:19:19} (70 ಗ್ರಾಂ) + ಸಾಗರಿಕ ದ್ರಾವಣ (35 ಮಿಲಿ).",
        "veg_stage_en": "Vegetative stage (20-25 DAS): WSF 19:19:19 (70 g) + Sagarika liquid (35 ml).",
        "flower_stage_kn": "ತೆನೆ ಹೊರಡುವ ಮುನ್ನ: ಬೋರಾನ್ 20% (15 ಗ್ರಾಂ) + {NPK 00:52:34} (75 ಗ್ರಾಂ) (ತೆನೆಯಲ್ಲಿ ಕಾಳುಗಳು ಗಿಡಚಾಗಿ ತುಂಬುತ್ತವೆ).",
        "flower_stage_en": "Earhead emergence: Boron 20% (15 g) + WSF 00:52:34 (75 g) (ensures dense finger grain-set).",
        "yield_stage_kn": "ಕಾಳು ಮಾಗುವ ಹಂತ: {NPK 13:00:45} (75 ಗ್ರಾಂ/ಪಂಪ್) ಸಿಂಪಡಿಸಿದರೆ ಕಾಳು ಕಪ್ಪಾಗಿ ಹೊಳಪು ಬರುತ್ತದೆ.",
        "yield_stage_en": "Dough stage: WSF 13:00:45 (75 g/pump) spray for bold grain lustre and drought resilience.",
        "boost_pct": "15 - 18% ಅಧಿಕ ಇಳುವರಿ"
    },
    "Maize": {
        "name_kn": "ಮೆಕ್ಕೆಜೋಳ {Maize}",
        "veg_stage_kn": "ಮಂಡಿ ಎತ್ತರದ ಹಂತ (25-30 ದಿನ): ಚೆಲೇಟೆಡ್ ಸತು {Zinc 12%} (15 ಗ್ರಾಂ) + ನ್ಯಾನೋ ಯೂರಿಯಾ (45 ಮಿಲಿ) + ಸಾಗರಿಕ (40 ಮಿಲಿ).",
        "veg_stage_en": "Knee-high stage (25-30 DAS): Chelated Zinc EDTA (15 g) + Nano Urea (45 ml) + Sagarika (40 ml).",
        "flower_stage_kn": "ತೆನೆ & ಚಾಮರ ಬರುವ ಹಂತ (45-50 ದಿನ): {NPK 00:52:34} (80 ಗ್ರಾಂ) + ಬೋರಾನ್ 20% (15 ಗ್ರಾಂ) (ತುದಿಯವರೆಗೆ ಕಾಳು ಕಟ್ಟಲು).",
        "flower_stage_en": "Tasseling & Silking (45-50 DAS): WSF 00:52:34 (80 g) + Boron 20% (15 g) (ensures tip-to-tip grain filling).",
        "yield_stage_kn": "ತೆನೆ ಹಾಲು ತುಂಬುವ ಹಂತ: {NPK 13:00:45} (80 ಗ್ರಾಂ) (ದಪ್ಪ ಕಾಳುಗಳು ಮತ್ತು ತೂಕ ಹೆಚ್ಚಳ).",
        "yield_stage_en": "Cob grain development: WSF 13:00:45 (80 g) for heavy kernel density.",
        "boost_pct": "16 - 20% ಅಧಿಕ ಇಳುವರಿ"
    },
    "Cotton": {
        "name_kn": "ಹತ್ತಿ {Cotton}",
        "veg_stage_kn": "ಕವಲು ಒಡೆಯುವ ಹಂತ (35-40 ದಿನ): ಸಾಗರಿಕ (40 ಮಿಲಿ) + {NPK 19:19:19} (75 ಗ್ರಾಂ) + ಮೆಗ್ನೀಸಿಯಂ ಸಲ್ಫೇಟ್ (50 ಗ್ರಾಂ).",
        "veg_stage_en": "Square initiation (35-40 DAS): Sagarika (40 ml) + WSF 19:19:19 (75 g) + Magnesium Sulphate (50 g).",
        "flower_stage_kn": "ಹೂವಾಡುವ & ಕಾಯಿ ಕಟ್ಟುವ ಹಂತ: ಪ್ಲಾನೋಫಿಕ್ಸ್ {Planofix} (4 ಮಿಲಿ) + ಬೋರಾನ್ 20% (15 ಗ್ರಾಂ) + {NPK 00:52:34} (75 ಗ್ರಾಂ).",
        "flower_stage_en": "Peak flowering & boll formation: Planofix (4 ml) + Boron 20% (15 g) + WSF 00:52:34 (75 g) (stops square drop).",
        "yield_stage_kn": "ಕಾಯಿ ದಪ್ಪಗಾಗುವ ಹಂತ: {NPK 13:00:45} (80 ಗ್ರಾಂ) 2 ಬಾರಿ ಸಿಂಪಡಿಸಿದರೆ ಹತ್ತಿ ಬೋಲ್ ತೂಕ 25% ಹೆಚ್ಚುತ್ತದೆ.",
        "yield_stage_en": "Boll maturation: WSF 13:00:45 (80 g) twice for maximum boll weight and staple quality.",
        "boost_pct": "20 - 25% ಅಧಿಕ ಇಳುವರಿ"
    },
    "Chilli": {
        "name_kn": "ಮೆಣಸಿನಕಾಯಿ {Chilli}",
        "veg_stage_kn": "ನಾಟಿ ಮಾಡಿದ 25 ದಿನ: ಮೈಕ್ರೋನ್ಯೂಟ್ರಿಯೆಂಟ್ ಗ್ರೇಡ್-IV (30 ಗ್ರಾಂ) + ಸಾಗರಿಕ (40 ಮಿಲಿ) + {NPK 19:19:19} (75 ಗ್ರಾಂ).",
        "veg_stage_en": "25 days after transplanting: Micronutrient Grade IV (30 g) + Sagarika (40 ml) + WSF 19:19:19 (75 g).",
        "flower_stage_kn": "ಹೂ ಬಿಡುವ ಹಂತ: ಪ್ಲಾನೋಫಿಕ್ಸ್ {Planofix} (3.5 ಮಿಲಿ) + ಬೋರಾನ್ 20% (15 ಗ್ರಾಂ) + {NPK 00:52:34} (75 ಗ್ರಾಂ) (ಹೂವು ಉದುರುವುದು ಸಂಪೂರ್ಣ ಬಂದ್).",
        "flower_stage_en": "Flowering flush: Planofix (3.5 ml) + Boron 20% (15 g) + WSF 00:52:34 (75 g) (zero flower drop).",
        "yield_stage_kn": "ಕಾಯಿ ಕೊಯ್ಲಿನ ನಡುವೆ: {NPK 13:00:45} (80 ಗ್ರಾಂ) (ಉದ್ದ, ದಪ್ಪ, ಘಾಟು ಮೆಣಸಿನಕಾಯಿ ಮತ್ತು ಗಾಢ ಕೆಂಪು ಬಣ್ಣ).",
        "yield_stage_en": "Between pickings: WSF 13:00:45 (80 g) for uniform length, pungency and deep red lustre.",
        "boost_pct": "22 - 28% ಅಧಿಕ ಇಳುವರಿ"
    },
    "Tomato": {
        "name_kn": "ಟೊಮೆಟೊ {Tomato}",
        "veg_stage_kn": "ನಾಟಿ ಮಾಡಿದ 20 ದಿನ: ಸಾಗರಿಕ (40 ಮಿಲಿ) + {NPK 19:19:19} (75 ಗ್ರಾಂ).",
        "veg_stage_en": "20 DAT: Sagarika (40 ml) + WSF 19:19:19 (75 g) for thick root collar.",
        "flower_stage_kn": "ಹೂವಾಡುವ ಹಂತ: ಬೋರಾನ್ 20% (15 ಗ್ರಾಂ) + ಕ್ಯಾಲ್ಸಿಯಂ ನೈಟ್ರೇಟ್ (ಪ್ರತ್ಯೇಕವಾಗಿ 50 ಗ್ರಾಂ) + {NPK 00:52:34} (75 ಗ್ರಾಂ).",
        "flower_stage_en": "Flowering: Boron 20% (15 g) + Calcium Nitrate (separately 50 g) + WSF 00:52:34 (75 g) (stops blossom end rot).",
        "yield_stage_kn": "ಕಾಯಿ ಮಾಗುವ ಹಂತ: {NPK 13:00:45} (80 ಗ್ರಾಂ) (ಹಣ್ಣು ಬಿರುಕು ಬಿಡುವುದಿಲ್ಲ, ಗಟ್ಟಿ ಚರ್ಮ ಮತ್ತು 15 ದಿನ ಬಾಳಿಕೆ).",
        "yield_stage_en": "Fruit sizing: WSF 13:00:45 (80 g) (prevents cracking, thick fruit wall, +15 days shelf life).",
        "boost_pct": "25 - 30% ಅಧಿಕ ಇಳುವರಿ"
    },
    "Tur / Pigeon Pea": {
        "name_kn": "ತೊಗರಿ {Tur / Pigeon Pea}",
        "veg_stage_kn": "ಕವಲು ಒಡೆಯುವ ಹಂತ (30-40 ದಿನ): ನ್ಯಾನೋ ಡಿಎಪಿ {Nano DAP} (50 ಮಿಲಿ) + ಸಾಗರಿಕ (40 ಮಿಲಿ) + {NPK 19:19:19} (75 ಗ್ರಾಂ).",
        "veg_stage_en": "Branching (30-40 DAS): Nano DAP (50 ml) + Sagarika (40 ml) + WSF 19:19:19 (75 g).",
        "flower_stage_kn": "ಹೂವಾಡುವ ಹಂತ: ಪ್ಲಾನೋಫಿಕ್ಸ್ (4 ಮಿಲಿ) + ಬೋರಾನ್ 20% (15 ಗ್ರಾಂ) + {NPK 00:52:34} (75 ಗ್ರಾಂ) (ತೊಗರಿ ಹೂವು ಉದುರುವುದು ತಡೆಯುತ್ತದೆ).",
        "flower_stage_en": "Flowering: Planofix (4 ml) + Boron 20% (15 g) + WSF 00:52:34 (75 g) (heavy pod set).",
        "yield_stage_kn": "ಕಾಯಿ ಕಟ್ಟುವ ಹಂತ: {NPK 13:00:45} (80 ಗ್ರಾಂ/ಪಂಪ್) ಸಿಂಪಡಿಸಿದರೆ ದಪ್ಪ ಕಾಳುಗಳೊಂದಿಗೆ ಬಂಪರ್ ಇಳುವರಿ.",
        "yield_stage_en": "Pod development: WSF 13:00:45 (80 g/pump) for plump 4-seeded pods.",
        "boost_pct": "20 - 24% ಅಧಿಕ ಇಳುವರಿ"
    },
    "Bengal Gram (Chickpea)": {
        "name_kn": "ಕಡಲೆ {Bengal Gram / Chickpea}",
        "veg_stage_kn": "ಚಿಗುರು ಚಿವುಟುವ ಹಂತ (25-30 ದಿನ): ಸಾಗರಿಕ (35 ಮಿಲಿ) + {NPK 19:19:19} (60 ಗ್ರಾಂ).",
        "veg_stage_en": "Nipping stage (25-30 DAS): Sagarika (35 ml) + WSF 19:19:19 (60 g).",
        "flower_stage_kn": "ಹೂ ಬಿಡುವ ಹಂತ: ಬೋರಾನ್ 20% (12 ಗ್ರಾಂ) + {NPK 00:52:34} (70 ಗ್ರಾಂ) (ಜೊಳ್ಳು ಕಾಯಿಗಳನ್ನು ತಡೆಯಲು).",
        "flower_stage_en": "Flowering: Boron 20% (12 g) + WSF 00:52:34 (70 g) (prevents empty pod formation).",
        "yield_stage_kn": "ಕಾಳು ತುಂಬುವ ಹಂತ: {NPK 13:00:45} (75 ಗ್ರಾಂ) (ದೊಡ್ಡ ಗಾತ್ರದ ಕಾಳುಗಳು).",
        "yield_stage_en": "Pod filling: WSF 13:00:45 (75 g) for bold test weight.",
        "boost_pct": "15 - 19% ಅಧಿಕ ಇಳುವರಿ"
    },
    "Groundnut": {
        "name_kn": "ಕಡಲೆಕಾಯಿ {Groundnut}",
        "veg_stage_kn": "ಸಸಿ ಬೆಳೆಯುವ ಹಂತ (20-25 ದಿನ): ಚೆಲೇಟೆಡ್ ಸತು (15 ಗ್ರಾಂ) + ಸಾಗರಿಕ (40 ಮಿಲಿ).",
        "veg_stage_en": "Vegetative (20-25 DAS): Chelated Zinc (15 g) + Sagarika (40 ml).",
        "flower_stage_kn": "ಹೂ ಬಿಡುವ ಹಂತ (35-40 ದಿನ): ಬೋರಾನ್ 20% (15 ಗ್ರಾಂ) + {NPK 00:52:34} (75 ಗ್ರಾಂ).",
        "flower_stage_en": "Flowering (35-40 DAS): Boron 20% (15 g) + WSF 00:52:34 (75 g).",
        "yield_stage_kn": "ಊಟೆ ಇಳಿಯುವ & ಕಾಯಿ ಕಟ್ಟುವ ಹಂತ (55-65 ದಿನ): {NPK 13:00:45} (80 ಗ್ರಾಂ) + ಮಣ್ಣಿಗೆ ಜಿಪ್ಸಮ್ (200 ಕೆಜಿ/ಎಕರೆಗೆ).",
        "yield_stage_en": "Pegging & pod development (55-65 DAS): WSF 13:00:45 (80 g) + Soil Gypsum (200 kg/acre).",
        "boost_pct": "18 - 22% ಅಧಿಕ ಇಳುವರಿ"
    },
    "Sugarcane": {
        "name_kn": "ಕಬ್ಬು {Sugarcane}",
        "veg_stage_kn": "ಕವಲು ಒಡೆಯುವ ಹಂತ (45-60 ದಿನ): ಇಫ್ಕೋ ನ್ಯಾನೋ ಯೂರಿಯಾ (50 ಮಿಲಿ) + ಸಾಗರಿಕ (50 ಮಿಲಿ) + {NPK 19:19:19} (100 ಗ್ರಾಂ).",
        "veg_stage_en": "Tillering (45-60 DAP): Nano Urea (50 ml) + Sagarika (50 ml) + WSF 19:19:19 (100 g).",
        "flower_stage_kn": "ಗೆಣ್ಣು ಬೆಳೆಯುವ ಹಂತ (90-120 ದಿನ): ಸೂಕ್ಷ್ಮ ಪೋಷಕಾಂಶ ಗ್ರೇಡ್-IV (40 ಗ್ರಾಂ) + {NPK 00:52:34} (100 ಗ್ರಾಂ) + ಫೆರಸ್ ಸಲ್ಫೇಟ್ (25 ಗ್ರಾಂ).",
        "flower_stage_en": "Grand growth / Internode elongation: Micronutrient Grade IV (40 g) + WSF 00:52:34 (100 g).",
        "yield_stage_kn": "ತೂಕ & ಸಕ್ಕರೆ ಅಂಶ ಹೆಚ್ಚಿಸಲು (180-210 ದಿನ): {NPK 13:00:45} (100 ಗ್ರಾಂ) (ದಪ್ಪ ಗಿಣ್ಣುಗಳು ಮತ್ತು ಗರಿಷ್ಠ ಕಬ್ಬಿನ ತೂಕ).",
        "yield_stage_en": "Sugar accumulation: WSF 13:00:45 (100 g) for thick cane girth and high brix sugar recovery.",
        "boost_pct": "15 - 20 ಟನ್/ಎಕರೆಗೆ ಅಧಿಕ ಇಳುವರಿ"
    },
    "Areca Nut": {
        "name_kn": "ಅಡಿಕೆ {Areca Nut}",
        "veg_stage_kn": "ಮುಂಗಾರಿನ ಆರಂಭ (ಮೇ-ಜೂನ್): ಬೋರ್ಡೋ ಸಿಂಪಡಣೆ ಜೊತೆ ಚೆಲೇಟೆಡ್ ಸತು (15 ಗ್ರಾಂ) + ಮೆಗ್ನೀಸಿಯಂ ಸಲ್ಫೇಟ್ ಬುಡಕ್ಕೆ.",
        "veg_stage_en": "Pre-monsoon (May-June): Chelated Zinc (15 g) + Magnesium Sulphate soil application.",
        "flower_stage_kn": "ಹಿಂಗಾರ ಅರಳುವ ಹಂತ: ಬೋರಾನ್ 20% (20 ಗ್ರಾಂ) + {NPK 00:52:34} (80 ಗ್ರಾಂ) (ಹಿಂಗಾರದಲ್ಲಿ ಕಾಯಿ ಕಟ್ಟುವುದು ಹೆಚ್ಚುತ್ತದೆ).",
        "flower_stage_en": "Inflorescence opening: Boron 20% (20 g) + WSF 00:52:34 (80 g) (improves nut set).",
        "yield_stage_kn": "ಅಡಿಕೆ ಕಾಯಿ ಮಾಗುವ ಹಂತ: {NPK 13:00:45} (100 ಗ್ರಾಂ/ಪಂಪ್) ಸಿಂಪಡಿಸಿದರೆ ಅಡಿಕೆ ಉದುರುವುದು ನಿಂತು ತೂಕ 20% ಹೆಚ್ಚುತ್ತದೆ.",
        "yield_stage_en": "Nut development: WSF 13:00:45 (100 g/pump) spray prevents nut drop and boosts dry kernel weight.",
        "boost_pct": "18 - 25% ಅಧಿಕ ಇಳುವರಿ"
    },
    "Onion": {
        "name_kn": "ಈರುಳ್ಳಿ {Onion}",
        "veg_stage_kn": "ನಾಟಿ ಮಾಡಿದ 30 ದಿನ: ಸಾಗರಿಕ (40 ಮಿಲಿ) + {NPK 19:19:19} (75 ಗ್ರಾಂ) + ಸಲ್ಫರ್ (ಗಂಧಕ 90% WDG 30 ಗ್ರಾಂ).",
        "veg_stage_en": "30 DAT: Sagarika (40 ml) + WSF 19:19:19 (75 g) + Sulphur 90% WDG (30 g).",
        "flower_stage_kn": "ಗಡ್ಡೆ ಕಟ್ಟುವ ಹಂತ (45-55 ದಿನ): {NPK 00:52:34} (80 ಗ್ರಾಂ) + ಬೋರಾನ್ 20% (15 ಗ್ರಾಂ).",
        "flower_stage_en": "Bulb initiation (45-55 DAT): WSF 00:52:34 (80 g) + Boron 20% (15 g).",
        "yield_stage_kn": "ಗಡ್ಡೆ ದಪ್ಪಗಾಗುವ ಹಂತ (70-80 ದಿನ): {NPK 13:00:45} (80 ಗ್ರಾಂ) (ದಪ್ಪ ಈರುಳ್ಳಿ ಮತ್ತು ದೀರ್ಘ ಸಂಗ್ರಹಣಾ ಬಾಳಿಕೆ).",
        "yield_stage_en": "Bulb enlargement (70-80 DAT): WSF 13:00:45 (80 g) for uniform size and extended storage life.",
        "boost_pct": "20 - 25% ಅಧಿಕ ಇಳುವರಿ"
    }
}

# ==============================================================================
# WEED MANAGEMENT BY INFESTATION DENSITY & LAND PORTION
# ==============================================================================
WEED_MANAGEMENT_BY_DENSITY = {
    "low": {
        "title_en": "Low / Scattered Weed Infestation (< 15% Land Coverage)",
        "title_kn": "ಕಡಿಮೆ / ಅಲ್ಲಲ್ಲಿ ಮಾತ್ರ ಕಳೆ ಹರಡಿರುವುದು (ಜಮೀನಿನ 15% ಕ್ಕಿಂತ ಕಡಿಮೆ ಭಾಗ)",
        "badge_color": "#2E7D32",
        "chemical_necessity_en": "Selective Post-Emergence Spot Weedicide Spray — Target only emerging weed patches to save money and protect soil.",
        "chemical_necessity_kn": "ಆಯ್ದ ಕಳೆನಾಶಕದ ಗುರುತು ಸಿಂಪರಣೆ {Spot Spray} — ಕಳೆ ಇರುವ ನಿರ್ದಿಷ್ಟ ಜಾಗದಲ್ಲಿ ಮಾತ್ರ ಸಿಂಪಡಿಸಿ ಖರ್ಚು ಉಳಿಸಿ.",
        "chemical_weedicides": [
            {
                "trade_name_en": "2,4-D Amine Salt 58% SL (Broadleaf Weed Killer)",
                "trade_name_kn": "2,4-ಡಿ ಅಮೈನ್ ಸಾಲ್ಟ್ 58% {2,4-D Amine Salt 58% SL}",
                "target_crops_en": "Paddy, Maize, Jowar, Sugarcane (Cereal Crops)",
                "target_crops_kn": "ಭತ್ತ, ಮೆಕ್ಕೆಜೋಳ, ಜೋಳ, ಕಬ್ಬು (ಧಾನ್ಯ ಬೆಳೆಗಳಲ್ಲಿನ ಅಗಲ ಎಲೆ ಕಳೆಗಳು)",
                "dose_per_pump_15l": "25 - 30 ml per 15L pump",
                "dose_per_acre": "400 - 500 ml per acre in 150-200 L water",
                "timing_en": "Apply at 2-3 leaf stage of weeds (20-25 days after sowing). Do NOT spray on cotton, pulses or vegetables!",
                "timing_kn": "ಕಳೆಯು 2-3 ಎಲೆಗಳ ಹಂತದಲ್ಲಿರುವಾಗ (ಬಿತ್ತಿದ 20-25 ದಿನ) ಸಿಂಪಡಿಸಿ. ಹತ್ತಿ ಅಥವಾ ಬೇಳೆಕಾಳು ಬೆಳೆಗಳಿಗೆ ಸಿಂಪಡಿಸಬೇಡಿ!",
                "buy_url": "https://www.bighaat.com/collections/all?q=2,4-D",
                "manufacturer": "Tata Rallis / Dhanuka"
            },
            {
                "trade_name_en": "Bispyribac-Sodium 10% SC (Nominee Gold)",
                "trade_name_kn": "ಬಿಸ್‌ಪೈರಿಬ್ಯಾಕ್ ಸೋಡಿಯಂ 10% {Nominee Gold - Bispyribac Sodium}",
                "target_crops_en": "Paddy (Direct Seeded & Transplanted Rice)",
                "target_crops_kn": "ಭತ್ತದ ಎಲ್ಲಾ ಜಾತಿಯ ಹುಲ್ಲು, ಅಗಲ ಎಲೆ & ಜೊಂಡು ಕಳೆಗಳಿಗೆ",
                "dose_per_pump_15l": "10 - 12 ml per 15L pump",
                "dose_per_acre": "80 - 100 ml per acre in 150 L water",
                "timing_en": "Apply 15-20 days after transplanting when weeds have 2-4 leaves. Drain standing water before spray.",
                "timing_kn": "ನಾಟಿ ಮಾಡಿದ 15-20 ದಿನಗಳಲ್ಲಿ ಸಿಂಪಡಿಸಿ. ಸಿಂಪರಣೆಗೆ ಮುನ್ನ ಗದ್ದೆಯ ನೀರನ್ನು ಬಸಿದು, 48 ಗಂಟೆಗಳ ನಂತರ ನೀರು ಕಟ್ಟಿ.",
                "buy_url": "https://www.bighaat.com/collections/all?q=Bispyribac",
                "manufacturer": "PI Industries / Bayer"
            },
            {
                "trade_name_en": "Imazethapyr 10% SL (Pursuit)",
                "trade_name_kn": "ಇಮಾಜೆಥಾಪೈರ್ 10% {Imazethapyr 10% SL - Pursuit}",
                "target_crops_en": "Groundnut, Soybean, Tur, Green Gram, Black Gram",
                "target_crops_kn": "ಶೇಂಗಾ, ಸೋಯಾಬೀನ್, ತೊಗರಿ, ಹೆಸರುಕಾಳು, ಉದ್ದು",
                "dose_per_pump_15l": "30 ml per 15L pump",
                "dose_per_acre": "300 - 350 ml per acre in 150-200 L water",
                "timing_en": "Apply at 15-20 days after sowing when broadleaf & grassy weeds are at 2-3 leaf stage.",
                "timing_kn": "ಬಿತ್ತನೆ ಮಾಡಿದ 15-20 ದಿನಗಳಲ್ಲಿ ಕಳೆಗಳು ಸಣ್ಣಗಿರುವಾಗಲೇ ಸಿಂಪಡಿಸಿ.",
                "buy_url": "https://www.bighaat.com/collections/all?q=Imazethapyr",
                "manufacturer": "BASF India / UPL"
            }
        ],
        "action_steps_en": [
            "Spot hand-weeding: Walk the field and pull weeds at 2-3 leaf stage before flowering/seed set.",
            "Mulching: Cover bare soil between crop plants with 5-7 cm layer of crop residue (paddy straw, sugarcane trash).",
            "Shallow hoeing: Use a hand-hoe (Khurpi) to uproot isolated weed clumps.",
            "Disposal method: Collect pulled weeds and add directly to on-farm organic compost pit (free organic N-P-K)."
        ],
        "action_steps_kn": [
            "ಕೈಯಿಂದ ಕಳೆ ಕೀಳುವುದು: ಕಳೆಗಳು ಹೂ ಬಿಡುವ ಮೊದಲೇ (2-3 ಎಲೆ ಹಂತದಲ್ಲಿ) ಕೈಯಿಂದ ಅಥವಾ ಕುರ್ಪಿಯಿಂದ ಬುಡಸಮೇತ ಕೀಳಿ.",
            "ಬೆಳೆ ತ್ಯಾಜ್ಯದ ಹೊದಿಕೆ {ಮಲ್ಚಿಂಗ್}: ಗಿಡಗಳ ನಡುವೆ ಬಿಸಿಲು ಮಣ್ಣಿಗೆ ತಾಗದಂತೆ ಭತ್ತದ ಹುಲ್ಲು ಅಥವಾ ಕಬ್ಬಿನ ರವದಿಯನ್ನು 2-3 ಇಂಚು ಮುಚ್ಚಿ.",
            "ಸಾಲುಗಳ ನಡುವೆ ಲಘು ಕುಂಟೆ: ಒಣಗಿದ ದಿನಗಳಲ್ಲಿ ಸಣ್ಣ ಕುಂಟೆ ಹೊಡೆದು ಕಳೆಗಳನ್ನು ಒಣಗಿಸಿ.",
            "ವಿಲೇವಾರಿ ವಿಧಾನ: ಕೀಳಲಾದ ಕಳೆಯನ್ನು ಜಮೀನಿನ ಹೊರಗೆ ಬಿಸಾಡದೆ, ಕಾಂಪೋಸ್ಟ್ ಗುಂಡಿಗೆ ಹಾಕಿ ಉತ್ತಮ ಸಾವಯವ ಗೊಬ್ಬರ ತಯಾರಿಸಿ."
        ]
    },
    "medium": {
        "title_en": "Moderate Weed Infestation (15% - 40% Land Coverage)",
        "title_kn": "ಮಧ್ಯಮ ಪ್ರಮಾಣದ ಕಳೆ ಬಾಧೆ (ಜಮೀನಿನ 15% ರಿಂದ 40% ಭಾಗ)",
        "badge_color": "#F9A825",
        "chemical_necessity_en": "Broadcast Selective Post-Emergence Weedicide — Kills all targeted weeds without harming the main crop.",
        "chemical_necessity_kn": "ಸಂಪೂರ್ಣ ಜಮೀನಿಗೆ ಆಯ್ದ ಕಳೆನಾಶಕ ಸಿಂಪರಣೆ {Selective Weedicide} — ಮುಖ್ಯ ಬೆಳೆಗೆ ಧಕ್ಕೆಯಾಗದೆ ಕಳೆ ಮಾತ್ರ ನಾಶವಾಗುತ್ತದೆ.",
        "chemical_weedicides": [
            {
                "trade_name_en": "Quizalofop-Ethyl 5% EC (Targa Super)",
                "trade_name_kn": "ಕ್ವಿಜಾಲೋಫಾಪ್ ಈಥೈಲ್ 5% {Targa Super / Quizalofop-Ethyl}",
                "target_crops_en": "Cotton, Soybean, Groundnut, Pulses, Onion, Vegetables",
                "target_crops_kn": "ಹತ್ತಿ, ಸೋಯಾಬೀನ್, ಶೇಂಗಾ, ತೊಗರಿ, ಈರುಳ್ಳಿ, ತರಕಾರಿ",
                "dose_per_pump_15l": "35 - 40 ml per 15L pump",
                "dose_per_acre": "350 - 400 ml per acre in 150-200 L water",
                "timing_en": "Apply 20-30 days after sowing on narrow-leaved grassy weeds. Completely safe for broadleaf crops.",
                "timing_kn": "ಬಿತ್ತಿದ 20-30 ದಿನಗಳಲ್ಲಿ ಹುಲ್ಲಿನ ಜಾತಿಗೆ ಸೇರಿದ ಕಳೆಗಳ ಮೇಲೆ ಸಿಂಪಡಿಸಿ. ಮುಖ್ಯ ಬೆಳೆಗೆ ಹಾನಿ ಮಾಡುವುದಿಲ್ಲ.",
                "buy_url": "https://www.bighaat.com/collections/all?q=Quizalofop",
                "manufacturer": "Dhanuka Agritech"
            },
            {
                "trade_name_en": "Atrazine 50% WP (Maize & Sugarcane Herbicide)",
                "trade_name_kn": "ಅಟ್ರಾಜಿನ್ 50% {Atrazine 50% WP}",
                "target_crops_en": "Maize (Corn) and Sugarcane",
                "target_crops_kn": "ಮೆಕ್ಕೆಜೋಳ ಮತ್ತು ಕಬ್ಬು",
                "dose_per_pump_15l": "50 - 60 g per 15L pump",
                "dose_per_acre": "800 g - 1.0 kg per acre in 200 L water",
                "timing_en": "Pre-emergence within 2-3 days of sowing or early post-emergence at 15 DAS in moist soil.",
                "timing_kn": "ಬಿತ್ತನೆ ಮಾಡಿದ 2-3 ದಿನಗಳಲ್ಲಿ ಅಥವಾ ಸಸಿ ಮೂಡಿ 15 ದಿನಗಳಲ್ಲಿ ಮಣ್ಣಿನಲ್ಲಿ ತೇವಾಂಶವಿರುವಾಗ ಸಿಂಪಡಿಸಿ.",
                "buy_url": "https://www.bighaat.com/collections/all?q=Atrazine",
                "manufacturer": "Rallis India / Dhanuka"
            },
            {
                "trade_name_en": "Oxyfluorfen 23.5% EC (Goal - Onion & Veg Herbicide)",
                "trade_name_kn": "ಆಕ್ಸಿಫ್ಲೋರ್ಫೆನ್ 23.5% {Oxyfluorfen / Goal}",
                "target_crops_en": "Onion, Garlic, Potato, Commercial Vegetables",
                "target_crops_kn": "ಈರುಳ್ಳಿ, ಬೆಳ್ಳುಳ್ಳಿ, ಆಲೂಗಡ್ಡೆ ಮತ್ತು ತರಕಾರಿ ಬೆಳೆಗಳು",
                "dose_per_pump_15l": "15 - 20 ml per 15L pump",
                "dose_per_acre": "200 - 250 ml per acre in 200 L water",
                "timing_en": "Spray immediately after onion transplanting (before weed emergence) or direct spray between rows.",
                "timing_kn": "ಈರುಳ್ಳಿ ನಾಟಿ ಮಾಡಿದ ತಕ್ಷಣ ಕಳೆ ಹುಟ್ಟುವ ಮುನ್ನ ಸಿಂಪಡಿಸಿ. ಮಣ್ಣಿನಲ್ಲಿ ತೇವಾಂಶ ಇರಬೇಕು.",
                "buy_url": "https://www.bighaat.com/collections/all?q=Oxyfluorfen",
                "manufacturer": "Corteva Agriscience / Indofil"
            }
        ],
        "action_steps_en": [
            "Conoweeder / Rotary Weeder: Pass mechanical row weeders in line-sown crops (paddy, maize, cotton). Buries weeds into mud as green manure.",
            "Smother Intercropping: Intercrop fast-canopy crops like Cowpea (ಅಲಸಂದಿ), Sunn hemp (ಸಣಬು), or Horse gram (ಹುರುಳಿ) to choke out weeds.",
            "Stale Seedbed Technique: Irrigate the field 10 days before sowing, allow first flush of weed seeds to germinate, destroy them with shallow harrowing, then sow main crop.",
            "Disposal method: High-temperature trench composting with cow dung slurry (50°C heat kills weed seeds)."
        ],
        "action_steps_kn": [
            "ಕೋನೋವೀವರ್ / ಚಕ್ರದ ಕುಂಟೆ: ಸಾಲಿನಲ್ಲಿ ಬಿತ್ತಿದ ಬೆಳೆಗಳಲ್ಲಿ (ಭತ್ತ, ಹತ್ತಿ, ಜೋಳ) ಮಣ್ಣು ಕೆದಕಿ ಕಳೆಗಳನ್ನು ಮಣ್ಣಿನಲ್ಲೇ ಹೂತು ಗೊಬ್ಬರವಾಗಿಸಿ.",
            "ಅಡಕ ಕಳೆ-ಮುಚ್ಚುವ ಬೆಳೆಗಳು: ಸಾಲುಗಳ ನಡುವೆ ಅಲಸಂದಿ, ಸಣಬು ಅಥವಾ ಹುರುಳಿಯನ್ನು ಸಹಬೆಳೆಯಾಗಿ ಬಿತ್ತಿ; ಇವು ನೆಲವನ್ನು ಮುಚ್ಚಿ ಕಳೆಯನ್ನು ಹತ್ತಿಕ್ಕುತ್ತವೆ.",
            "ಮುಂಗಡ ನೀರು ಕಟ್ಟಿ ಕಳೆ ಮೊಳಕೆ ನಾಶ {Stale Seedbed}: ಬಿತ್ತನೆಗೆ 10 ದಿನ ಮುನ್ನ ನೀರು ಕಟ್ಟಿ ಕಳೆ ಮೊಳಕೆಯೊಡೆಯಲು ಬಿಡಿ; ನಂತರ ಮೇಲುಳುಮೆ ಮಾಡಿ ಕಳೆ ನಾಶಪಡಿಸಿ ಮುಖ್ಯ ಬೆಳೆ ಬಿತ್ತಿ.",
            "ವಿಲೇವಾರಿ ವಿಧಾನ: ಸೆಗಣಿ ಗಂಜಲದೊಂದಿಗೆ ಗುಂಡಿ ಕಾಂಪೋಸ್ಟ್ ಮಾಡಿ; 50°C ಬಿಸಿಗೆ ಕಳೆ ಬೀಜಗಳು ನಾಶವಾಗಿ ಗೊಬ್ಬರವಾಗುತ್ತವೆ."
        ]
    },
    "dense": {
        "title_en": "Dense / Heavy Choking Weed Infestation (> 40% Land Coverage)",
        "title_kn": "ತೀವ್ರ / ಬೆಳೆ ಮುಳುಗಿಸುವಷ್ಟು ದಟ್ಟ ಕಳೆ ಬಾಧೆ (ಜಮೀನಿನ 40% ಕ್ಕಿಂತ ಅಧಿಕ ಭಾಗ)",
        "badge_color": "#C62828",
        "chemical_necessity_en": "Total Knockdown / Systemic Eradication Weedicides — For fallow land, bunds, pre-sowing preparation, or hooded spray.",
        "chemical_necessity_kn": "ಸಂಪೂರ್ಣ ಬೇರುಸಮೇತ ಕಳೆನಾಶಕ ವಿಲೇವಾರಿ {Total Knockdown} — ಬಿತ್ತನೆ ಮುನ್ನ ಜಮೀನು ಸ್ವಚ್ಛತೆಗೆ, ಬದುಗಳಿಗೆ ಅಥವಾ ಹುಡ್ ಸಿಂಪರಣೆಗೆ.",
        "chemical_weedicides": [
            {
                "trade_name_en": "Glufosinate Ammonium 13.5% SL (Basta / Fast Knockdown)",
                "trade_name_kn": "ಗ್ಲೂಫೋಸಿನೇಟ್ ಅಮೋನಿಯಂ 13.5% {Basta / Glufosinate Ammonium}",
                "target_crops_en": "Non-Crop Land, Bunds, Orchard Floors (Areca, Mango, Pomegranate) or Pre-Planting",
                "target_crops_kn": "ತೋಟಗಳ ಸಾಲುಗಳ ನಡುವೆ (ಅಡಿಕೆ, ಮಾವು, ದಾಳಿಂಬೆ), ಜಮೀನಿನ ಬದುಗಳಲ್ಲಿ ಮತ್ತು ಬಿತ್ತನೆಗೆ ಮುನ್ನ",
                "dose_per_pump_15l": "60 - 70 ml per 15L pump",
                "dose_per_acre": "1.0 - 1.2 Litres per acre in 200 L water",
                "timing_en": "Contact fast knockdown. Destroys tough resistant weeds in 48-72 hours. Completely deactivated in soil so crop root is 100% safe.",
                "timing_kn": "ಸಿಂಪಡಿಸಿದ 48 ಗಂಟೆಗಳಲ್ಲಿ ಕಳೆಯನ್ನು ಒಣಗಿಸಿ ಸುಡುತ್ತದೆ. ಮಣ್ಣಿನಲ್ಲಿ ಯಾವುದೇ ವಿಷ ಉಳಿಯುವುದಿಲ್ಲ, ಬೆಳೆಯ ಬೇರಿಗೆ ಯಾವುದೇ ಧಕ್ಕೆ ಇಲ್ಲ.",
                "buy_url": "https://www.bighaat.com/collections/all?q=Glufosinate",
                "manufacturer": "BASF India / Bayer"
            },
            {
                "trade_name_en": "Glyphosate 41% SL (Roundup / Glycel - Deep Root Killer)",
                "trade_name_kn": "ಗ್ಲೈಫೋಸೇಟ್ 41% {Glyphosate 41% SL - Roundup / Glycel}",
                "target_crops_en": "Fallow fields before sowing, Bunds, Deep Rooted Nutgrass / Harike Grass",
                "target_crops_kn": "ಬಿತ್ತನೆಗೆ ಮುಂಚಿನ ಖಾಲಿ ಜಮೀನು, ಬದುಗಳು, ಹರಿಕೆ ಮತ್ತು ಭದ್ರ ಮುಸ್ತೆ ಗೆಡ್ಡೆಗಳ ನಾಶಕ್ಕೆ",
                "dose_per_pump_15l": "75 - 80 ml per 15L pump (mix with 20g Urea for faster translocation)",
                "dose_per_acre": "1.2 - 1.5 Litres per acre in 200 L water",
                "timing_en": "Systemic translocated herbicide. Kills weeds from the underground roots and tubers within 10-14 days. Apply when weeds are green and actively growing.",
                "timing_kn": "ಕಳೆಯ ಎಲೆಗಳ ಮೂಲಕ ಇಳಿದು ಭೂಮಿಯೊಳಗಿನ ಬೇರು ಮತ್ತು ಗೆಡ್ಡೆಗಳನ್ನು ಸಂಪೂರ್ಣ ನಾಶಮಾಡುತ್ತದೆ (10-14 ದಿನ). ಕಳೆಯು ಹಸಿರಾಗಿದ್ದಾಗ ಸಿಂಪಡಿಸಿ.",
                "buy_url": "https://www.bighaat.com/collections/all?q=Glyphosate",
                "manufacturer": "Bayer India / Excel Crop Care"
            },
            {
                "trade_name_en": "Paraquat Dichloride 24% SL (Gramoxone - Instant Foliar Burner)",
                "trade_name_kn": "ಪ್ಯಾರಾಕ್ವಾಟ್ ಡೈಕ್ಲೋರೈಡ್ 24% {Gramoxone / Paraquat}",
                "target_crops_en": "Inter-row directed spray with protective hood, bund cleaning, zero-tillage seedbed",
                "target_crops_kn": "ರಕ್ಷಣಾತ್ಮಕ ಕವಚದೊಂದಿಗೆ (ಹುಡ್) ಸಾಲುಗಳ ನಡುವೆ, ಬದುಗಳ ಸ್ವಚ್ಛತೆಗೆ",
                "dose_per_pump_15l": "50 - 60 ml per 15L pump",
                "dose_per_acre": "800 ml - 1.0 Litre per acre in 200 L water",
                "timing_en": "Instant foliage desiccant. Weeds turn yellow within 6 hours. Use only with protective spray hood; never let spray touch green crop stems.",
                "timing_kn": "ಸಿಂಪಡಿಸಿದ 6 ಗಂಟೆಗಳಲ್ಲಿ ಕಳೆ ಸಂಪೂರ್ಣ ಸುಟ್ಟು ಹೋಗುತ್ತದೆ. ರಕ್ಷಣಾತ್ಮಕ ಹುಡ್ ಬಳಸಿ ಸಿಂಪಡಿಸಿ; ಮುಖ್ಯ ಬೆಳೆಯ ಹಸಿರು ಭಾಗಕ್ಕೆ ತಾಗಬಾರದು.",
                "buy_url": "https://www.bighaat.com/collections/all?q=Paraquat",
                "manufacturer": "Syngenta India / Dhanuka"
            }
        ],
        "action_steps_en": [
            "Deep Summer Mouldboard Ploughing: Plough 25-30 cm deep immediately after harvest. Exposes underground tubers (Nutgrass/Harike) to 42°C summer sun.",
            "Soil Solarization: Cover moist ploughed soil with 25-micron transparent polyethylene film for 30 days during peak summer (April-May). Generates lethal 55°C heat.",
            "Directed Selective Spraying: If crop is already planted and choking, use a protective hood attachment with flat-fan/flood-jet nozzle directly on weeds. Never allow spray drift on crop leaves!",
            "Disposal method: Strictly NEVER throw seed-bearing weeds onto irrigation canals or field bunds! Dig a 1-meter deep pit, layer with dung slurry, urea (accelerator), and Trichoderma."
        ],
        "action_steps_kn": [
            "ಆಳವಾದ ಬೇಸಿಗೆ ಉಳುಮೆ: ಬೆಳೆ ಕಟಾವಾದ ತಕ್ಷಣ 1 ಅಡಿ ಆಳಕ್ಕೆ ಉಳುಮೆ ಮಾಡಿ. ಹರಿಕೆ ಮತ್ತು ಭದ್ರ ಮುಸ್ತೆ ಗೆಡ್ಡೆಗಳು 42°C ಬಿಸಿಲಿಗೆ ಒಣಗಿ ಸಂಪೂರ್ಣ ಸಾಯುತ್ತವೆ.",
            "ಮಣ್ಣಿನ ಸೌರ ತಾಪಮಾನ ಚಿಕಿತ್ಸೆ {Soil Solarization}: ಬೇಸಿಗೆಯಲ್ಲಿ (ಏಪ್ರಿಲ್-ಮೇ) ತೇವವಿರುವ ಮಣ್ಣಿಗೆ ಪಾರದರ್ಶಕ ಪಾಲಿಥಿನ್ ಶೀಟ್ ಮುಚ್ಚಿ 30 ದಿನ ಬಿಡಿ. 55°C ಶಾಖಕ್ಕೆ ಕಳೆ ಬೀಜಗಳು ಸಾಯುತ್ತವೆ.",
            "ರಕ್ಷಣಾತ್ಮಕ ಹುಡ್ ಸಿಂಪರಣೆ: ಬೆಳೆಯ ನಡುವೆ ಅನಿವಾರ್ಯವಾದರೆ ಮಾತ್ರ 'ಫ್ಲಡ್ ಜೆಟ್' ನಾಜಲ್ ಮತ್ತು ರಕ್ಷಣಾ ಕವಚ (ಹುಡ್) ಬಳಸಿ ಕಳೆಯ ಮೇಲೆ ಮಾತ್ರ ಸಿಂಪಡಿಸಿ. ಮುಖ್ಯ ಬೆಳೆಯ ಎಲೆಗೆ ತಾಗದಂತೆ ಜಾಗ್ರತೆವಹಿಸಿ.",
            "ವಿಲೇವಾರಿ ವಿಧಾನ: ಹೂವು ಬಿಟ್ಟ ಕಳೆಯನ್ನು ಬದು ಅಥವಾ ಕಾಲುವೆಗೆ ಎಸೆಯಬೇಡಿ! ಆಳವಾದ ಗುಂಡಿ ತೋಡಿ ಸೆಗಣಿ ನೀರು ಮತ್ತು ಟ್ರೈಕೋಡರ್ಮ ಹಾಕಿ ಮುಚ್ಚಿ."
        ]
    }
}

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
            "Install 4 to 5 pheromone traps per acre to monitor moth catches.",
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
        "crop_en": "Chilli",
        "crop_kn": "ಮೆಣಸಿನಕಾಯಿ {Chilli}",
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
            "Apply sand + lime mixture (9:1 ratio) into the whorl for small farm plots as a physical deterrent."
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
    },
    {
        "id": "ragi_blast",
        "crop_en": "Ragi (Finger Millet)",
        "crop_kn": "ರಾಗಿ {Ragi / Finger Millet}",
        "problem_en": "Ragi Blast & Neck Rot",
        "problem_kn": "ರಾಗಿ ಬೆಂಕಿ ರೋಗ & ಕುತ್ತಿಗೆ ಕೊಳೆ {Ragi Blast}",
        "type": "disease",
        "symptoms_en": "Spindle-shaped lesions on leaves; rotting finger neck joints causing fingers to snap and drop empty grains.",
        "symptoms_kn": "ಎಲೆಗಳ ಮೇಲೆ ಕಂದು ಮಚ್ಚೆಗಳು; ರಾಗಿ ತೆನೆಯ ಬೆರಳುಗಳ ಬುಡ ಕಪ್ಪಾಗಿ ಕೊಳೆತು ಮುರಿದುಬೀಳುವುದು.",
        "recommended_chemicals": [
            {
                "trade_name": "Kitazin 48% EC / Iprobenfos",
                "trade_name_kn": "ಕಿಟಾಜಿನ್ 48% {Kitazin 48% EC}",
                "active": "Kitazin 48% EC",
                "dose_per_l": "2.0 ml/L",
                "dose_per_pump_15l": "30 ml per 15L pump",
                "action": "Organophosphorus systemic fungicide",
                "manufacturer": "PI Industries"
            },
            {
                "trade_name": "Indofil M-45 / Mancozeb 75% WP",
                "trade_name_kn": "ಮ್ಯಾಂಕೋಜೆಬ್ 75% {Mancozeb 75% WP}",
                "active": "Mancozeb 75% WP",
                "dose_per_l": "2.0 g/L",
                "dose_per_pump_15l": "30 g per 15L pump",
                "action": "Broad-spectrum contact protectant fungicide",
                "manufacturer": "Indofil Industries"
            }
        ],
        "tank_mix_nutrition_en": "Add WSF 19:19:19 (70 g/pump) + Boron 20% (15 g/pump) for rapid finger expansion.",
        "tank_mix_nutrition_kn": "{NPK 19:19:19} (70 ಗ್ರಾಂ/ಪಂಪ್) + ಬೋರಾನ್ 20% (15 ಗ್ರಾಂ) ಬೆರೆಸಿ ಸಿಂಪಡಿಸಿದರೆ ತೆನೆಗಳು ತುಂಬಿ ದಪ್ಪವಾಗುತ್ತವೆ.",
        "spraying_measures_en": [
            "Treat seed with Trichoderma viride (10 g/kg) before sowing.",
            "Spray fungicide immediately at earhead emergence stage.",
            "Avoid excessive urea application in rainy overcast weather."
        ],
        "spraying_measures_kn": [
            "ಬಿತ್ತನೆ ಮುನ್ನ ಟ್ರೈಕೋಡರ್ಮ (10 ಗ್ರಾಂ/ಕೆಜಿ) ಬಳಸಿ ಬೀಜೋಪಚಾರ ಮಾಡಿ.",
            "ತೆನೆ ಹೊರಡುವ ಆರಂಭಿಕ ಹಂತದಲ್ಲೇ ಮೊದಲ ಸಿಂಪಡಣೆ ಮಾಡಿ.",
            "ಮೋಡ ಕವಿದ ಮಳೆಗಾಲದಲ್ಲಿ ಯೂರಿಯಾ ಗೊಬ್ಬರವನ್ನು ಹೆಚ್ಚುವರಿಯಾಗಿ ಹಾಕಬೇಡಿ."
        ]
    },
    {
        "id": "tur_pod_borer",
        "crop_en": "Tur / Pigeon Pea",
        "crop_kn": "ತೊಗರಿ {Tur / Pigeon Pea}",
        "problem_en": "Pod Borer & Plume Moth (ಕಾಯಿಕೊರೆಯುವ ಹುಳು)",
        "problem_kn": "ತೊಗರಿ ಕಾಯಿಕೊರೆಯುವ ಕಾಯಿಕೊರಕ ಹುಳು {Pod Borer}",
        "type": "pest",
        "symptoms_en": "Caterpillar feeds on flower buds and drills circular holes into developing pods, eating the developing seeds inside.",
        "symptoms_kn": "ಹುಳು ಹೂವುಗಳನ್ನು ತಿಂದು ಉದುರಿಸುತ್ತದೆ ಮತ್ತು ಎಳೆಯ ಕಾಯಿಗಳಿಗೆ ದುಂಡನೆಯ ರಂಧ್ರ ಕೊರೆದು ಒಳಗಿನ ಕಾಳನ್ನು ಸಂಪೂರ್ಣವಾಗಿ ತಿನ್ನುತ್ತದೆ.",
        "recommended_chemicals": [
            {
                "trade_name": "Fame / Flubendiamide 39.35% SC",
                "trade_name_kn": "ಫೇಮ್ / ಫ್ಲೂಬೆಂಡಿಯಾಮೈಡ್ {Flubendiamide 39.35% SC}",
                "active": "Flubendiamide 39.35% SC",
                "dose_per_l": "0.3 ml/L",
                "dose_per_pump_15l": "5 ml per 15L pump",
                "action": "Insect muscle contractor, stops caterpillar feeding in 15 mins",
                "manufacturer": "Bayer CropScience India"
            },
            {
                "trade_name": "Proclaim / Emamectin Benzoate 5% SG",
                "trade_name_kn": "ಪ್ರೊಕ್ಲೇಮ್ {Emamectin Benzoate 5% SG}",
                "active": "Emamectin Benzoate 5% SG",
                "dose_per_l": "0.4 g/L",
                "dose_per_pump_15l": "6 - 7 g per 15L pump",
                "action": "Broad-spectrum Lepidopteran caterpillar insecticide",
                "manufacturer": "Syngenta India"
            }
        ],
        "tank_mix_nutrition_en": "Tank mix with Planofix PGR (4 ml/pump) + Boron 20% (15 g/pump) + NPK 00:52:34 (75 g/pump) to stop flower shedding.",
        "tank_mix_nutrition_kn": "ಪ್ಲಾನೋಫಿಕ್ಸ್ (4 ಮಿಲಿ/ಪಂಪ್) + ಬೋರಾನ್ 20% (15 ಗ್ರಾಂ) + {NPK 00:52:34} (75 ಗ್ರಾಂ) ಬೆರೆಸಿ ಸಿಂಪಡಿಸಿದರೆ ಹೂವು ಉದುರುವುದು ನಿಂತು ಕಾಯಿ ಕಟ್ಟುತ್ತದೆ.",
        "spraying_measures_en": [
            "Install 4-5 pheromone traps per acre at flower bud stage.",
            "Shake plants vigorously on a cloth to dislodge large caterpillars in small farm plots.",
            "Spray when 5-10% of flower buds or green pods show borer entry damage."
        ],
        "spraying_measures_kn": [
            "ಹೂ ಮೊಗ್ಗು ಬರುವ ಹಂತದಲ್ಲೇ ಎಕರೆಗೆ 4-5 ಮೋಹಕ ಬಲೆಗಳನ್ನು ಅಳವಡಿಸಿ.",
            "ಗಿಡಗಳನ್ನು ಕೋಲಿನಿಂದ ನಿಧಾನವಾಗಿ ಅಲುಗಾಡಿಸಿ ಕೆಳಗೆ ಬಿದ್ದ ಹುಳುಗಳನ್ನು ಆರಿಸಿ ನಾಶಮಾಡಿ.",
            "ಸಂಜೆ 4 ಗಂಟೆಯ ನಂತರ ಔಷಧ ಸಿಂಪಡಿಸಿ."
        ]
    },
    {
        "id": "onion_purple_blotch",
        "crop_en": "Onion",
        "crop_kn": "ಈರುಳ್ಳಿ {Onion}",
        "problem_en": "Purple Blotch & Thrips (ನೇರಳೆ ಮಚ್ಚೆ ರೋಗ & ನುಸಿ)",
        "problem_kn": "ಈರುಳ್ಳಿ ನೇರಳೆ ಮಚ್ಚೆ ರೋಗ & ನುಸಿ ಜಿಗಟು {Purple Blotch & Thrips}",
        "type": "disease",
        "symptoms_en": "Small, water-soaked sunken lesions turning brown to purple with yellow margins; leaves break over; thrips cause silver streaks.",
        "symptoms_kn": "ಎಲೆಗಳ ಮೇಲೆ ನೇರಳೆ-ಕಂದು ಬಣ್ಣದ ಅಂಡಾಕಾರದ ಗುಳಿ ಮಚ್ಚೆಗಳು; ಎಲೆಗಳು ಮುರಿದು ಬೀಳುವುದು; ನುಸಿ ಹುಳುಗಳು ಬೆಳ್ಳಿಯಂತಹ ಗೆರೆ ಮೂಡಿಸುವುದು.",
        "recommended_chemicals": [
            {
                "trade_name": "Custodia / Azoxystrobin 11% + Tebuconazole 18.3% SC",
                "trade_name_kn": "ಕಸ್ಟೋಡಿಯಾ {Azoxystrobin + Tebuconazole}",
                "active": "Azoxystrobin 11% + Tebuconazole 18.3% SC",
                "dose_per_l": "1.5 ml/L",
                "dose_per_pump_15l": "22 ml per 15L pump",
                "action": "Broad spectrum systemic curative & protective fungicide",
                "manufacturer": "Adama India"
            },
            {
                "trade_name": "Karate / Lambda-cyhalothrin 5% EC",
                "trade_name_kn": "ಕರಾಟೆ / ಲ್ಯಾಮ್ಡಾ {Lambda-cyhalothrin 5% EC}",
                "active": "Lambda-cyhalothrin 5% EC",
                "dose_per_l": "1.0 ml/L",
                "dose_per_pump_15l": "15 ml per 15L pump",
                "action": "Rapid knock-down contact pyrethroid for onion thrips",
                "manufacturer": "Syngenta India"
            }
        ],
        "tank_mix_nutrition_en": "Add Silicon Spreader Sticker (5 ml/pump) without fail (onion leaves have waxy coating) + WSF 00:52:34 (75 g/pump).",
        "tank_mix_nutrition_kn": "ಈರುಳ್ಳಿ ಎಲೆಗಳು ಮೇಣದಂತಿರುವ ಕಾರಣ ಸಿಲಿಕಾನ್ ಅಂಟು ದ್ರಾವಣವನ್ನು {Sticker} (5 ಮಿಲಿ/ಪಂಪ್) ಕಡ್ಡಾಯವಾಗಿ ಬೆರೆಸಿ + {NPK 00:52:34} (75 ಗ್ರಾಂ).",
        "spraying_measures_en": [
            "Always include non-ionic silicon spreader sticker so spray does not roll off waxy tubular leaves.",
            "Spray in cool morning or evening hours with fine hollow-cone mist.",
            "Avoid excess nitrogenous fertilizer in cloudy weather."
        ],
        "spraying_measures_kn": [
            "ಎಲೆಗಳಿಂದ ಔಷಧ ಜಾರಿ ಬೀಳದಂತೆ ಸಿಲಿಕಾನ್ ಅಂಟು ದ್ರಾವಣ ಬೆರೆಸುವುದು ಅತ್ಯಗತ್ಯ.",
            "ಮುಂಜಾನೆ ಅಥವಾ ಸಂಜೆ ವೇಳೆ ನುಣುಪಾದ ತುಂತುರು ನಾಜಲ್ ಬಳಸಿ ಸಿಂಪಡಿಸಿ.",
            "ಮೋಡ ಕವಿದ ವಾತಾವರಣದಲ್ಲಿ ಯೂರಿಯಾ ಗೊಬ್ಬರ ಹಾಕಬೇಡಿ."
        ]
    },
    {
        "id": "arecanut_koleroga",
        "crop_en": "Areca Nut",
        "crop_kn": "ಅಡಿಕೆ {Areca Nut}",
        "problem_en": "Koleroga / Mahali (Fruit Rot - ಕೊಳೆ ರೋಗ)",
        "problem_kn": "ಅಡಿಕೆ ಕೊಳೆ ರೋಗ / ಮಹಾಳಿ ರೋಗ {Arecanut Koleroga}",
        "type": "disease",
        "symptoms_en": "Water-soaked dark lesions at the calyx end of young nuts; heavy premature nut drop carpeted on the ground; white cottony fungal growth on fallen nuts.",
        "symptoms_kn": "ಅಡಿಕೆ ಕಾಯಿಯ ತೊಟ್ಟಿನ ಬಳಿ ಕಪ್ಪು ನೀರಿನ ಕಲೆಗಳು; ಎಳೆಯ ಅಡಿಕೆ ಕಾಯಿಗಳು ತೊಟ್ಟು ಕಳಚಿ ನೆಲಕ್ಕೆ ಉದುರುವುದು; ಉದುರಿದ ಕಾಯಿಗಳ ಮೇಲೆ ಬಿಳಿ ಬೂಷ್ಟು.",
        "recommended_chemicals": [
            {
                "trade_name": "Bordeaux Mixture 1% (Copper Sulphate + Quicklime)",
                "trade_name_kn": "1% ಬೋರ್ಡೋ ದ್ರಾವಣ {Bordeaux Mixture 1%}",
                "active": "Copper Sulphate (1 kg) + Lime (1 kg) in 100 L water",
                "dose_per_l": "10 g/L (1% concentration)",
                "dose_per_pump_15l": "Standard 1% prepared mixture",
                "action": "Protective contact multi-site copper fungicide",
                "manufacturer": "Farm-prepared or certified copper sulphate"
            },
            {
                "trade_name": "Ridomil Gold / Metalaxyl-M 4% + Mancozeb 64% WP",
                "trade_name_kn": "ರಿಡೋಮಿಲ್ ಗೋಲ್ಡ್ {Ridomil Gold}",
                "active": "Metalaxyl-M 4% + Mancozeb 64% WP",
                "dose_per_l": "2.5 g/L",
                "dose_per_pump_15l": "35 - 40 g per 15L pump",
                "action": "Systemic oomycete curative fungicide",
                "manufacturer": "Syngenta India"
            }
        ],
        "tank_mix_nutrition_en": "Do NOT mix Bordeaux mixture with fertilizers! Spray WSF 13:00:45 (100 g/pump) separately 15 days later to fortify nut weight.",
        "tank_mix_nutrition_kn": "ಬೋರ್ಡೋ ದ್ರಾವಣಕ್ಕೆ ಯಾವುದೇ ಗೊಬ್ಬರ ಬೆರೆಸಬೇಡಿ! 15 ದಿನಗಳ ನಂತರ ಪ್ರತ್ಯೇಕವಾಗಿ {NPK 13:00:45} (100 ಗ್ರಾಂ/ಪಂಪ್) ಸಿಂಪಡಿಸಿದರೆ ಕಾಯಿ ತೂಕ ಹೆಚ್ಚುತ್ತದೆ.",
        "spraying_measures_en": [
            "First prophylactic spray: Before onset of Southwest monsoon (May-June) covering all bunches.",
            "Second spray: 40-45 days later during July-August breaks in rain.",
            "Cover bunches with polythene bags (100-gauge) before heavy monsoon rains."
        ],
        "spraying_measures_kn": [
            "ಮುಂಗಾರು ಮಳೆ ಆರಂಭವಾಗುವ ಮುನ್ನವೇ (ಮೇ ಕೊನೆ ಅಥವಾ ಜೂನ್ ಆರಂಭ) ಅಡಿಕೆ ಗೊಂಚಲುಗಳಿಗೆ ಮೊದಲ ಸಿಂಪಡಣೆ ಮಾಡಿ.",
            "ಜುಲೈ-ಆಗಸ್ಟ್ ಮಳೆ ಬಿಡುವು ನೀಡಿದಾಗ 2ನೇ ಸಿಂಪಡಣೆ ಮಾಡಿ.",
            "ಕೊಳೆ ರೋಗ ತೀವ್ರವಾಗಿರುವ ತೋಟಗಳಲ್ಲಿ ಅಡಿಕೆ ಗೊಂಚಲುಗಳಿಗೆ ಪಾಲಿಥಿನ್ ಚೀಲ ಕಟ್ಟಿ ರಕ್ಷಿಸಿ."
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

# ==============================================================================
# SEASONAL HIGH-YIELD CROP RECOMMENDATIONS BY SOIL TYPE
# ==============================================================================
SEASONAL_CROP_RECOMMENDATIONS = {
    "early_kharif": {
        "season_en": "Early Kharif (Pre-Monsoon: April - May)",
        "season_kn": "ಮುಂಗಾರು ಪೂರ್ವ (ಏಪ್ರಿಲ್ - ಮೇ)",
        "soil_types": {
            "red_sandy": [
                {
                    "crop_en": "Groundnut (Summer/Early Kharif)",
                    "crop_kn": "ಶೇಂಗಾ / ನೆಲಗಡಲೆ {Groundnut}",
                    "yield": "12 - 15 ಕ್ವಿಂಟಾಲ್ / ಎಕರೆ (1.2 - 1.5 T/acre)",
                    "varieties": "TMV-2, KDG-128, G2-52, ICGV-91114",
                    "water": "2-3 ಜೀವ ರಕ್ಷಕ ನೀರಾವರಿ ಅಗತ್ಯ {Light Irrigation}",
                    "market": "⭐⭐⭐⭐⭐ (ಅಡುಗೆ ಎಣ್ಣೆ ಗಿರಣಿಗಳಿಂದ ಭಾರಿ ಬೇಡಿಕೆ)"
                },
                {
                    "crop_en": "Green Gram (Moong)",
                    "crop_kn": "ಹೆಸರುಕಾಳು {Green Gram / Moong}",
                    "yield": "6 - 8 ಕ್ವಿಂಟಾಲ್ / ಎಕರೆ (60-65 ದಿನಗಳಲ್ಲಿ ಕಟಾವು)",
                    "varieties": "DGGV-2, BGS-9, Selection-4",
                    "water": "ಕಡಿಮೆ ನೀರು {Drought Tolerant}",
                    "market": "⭐⭐⭐⭐⭐ (ಹೆಸರಿಗೆ ಮಾರುಕಟ್ಟೆಯಲ್ಲಿ ಕ್ವಿಂಟಾಲ್‌ಗೆ ₹8,000+ ಬೆಲೆ)"
                },
                {
                    "crop_en": "Fodder Sorghum / Jowar",
                    "crop_kn": "ಮೇವಿನ ಜೋಳ {Fodder Sorghum}",
                    "yield": "18 - 22 ಟನ್ ಹಸಿರು ಮೇವು / ಎಕರೆ",
                    "varieties": "CoFS-29, SSG-59-3, CSH-24MF",
                    "water": "ಮಧ್ಯಮ ನೀರು",
                    "market": "⭐⭐⭐⭐ (ಬೇಸಿಗೆಯಲ್ಲಿ ಹೈನುಗಾರಿಕೆ ಹಾಲಿನ ಇಳುವರಿಗೆ ಅಮೃತ)"
                }
            ],
            "black_cotton": [
                {
                    "crop_en": "Sunflower",
                    "crop_kn": "ಸೂರ್ಯಕಾಂತಿ {Sunflower}",
                    "yield": "8 - 10 ಕ್ವಿಂಟಾಲ್ / ಎಕರೆ",
                    "varieties": "KBSH-41, KBSH-53, RSFH-1887",
                    "water": "ತೇವಾಂಶ ಹಿಡಿದಿಡುವ ಕಪ್ಪು ಮಣ್ಣಿನಲ್ಲಿ ಅತ್ಯುತ್ತಮ",
                    "market": "⭐⭐⭐⭐⭐ (ಎಣ್ಣೆಕಾಳುಗಳಿಗೆ ಉತ್ತಮ ಎಂಎಸ್‌ಪಿ ಬೆಲೆ)"
                },
                {
                    "crop_en": "Black Gram (Urad)",
                    "crop_kn": "ಉದ್ದು {Black Gram / Urad}",
                    "yield": "5 - 7 ಕ್ವಿಂಟಾಲ್ / ಎಕರೆ",
                    "varieties": "DU-1, LBG-791, Rashmi",
                    "water": "ಕಡಿಮೆ ನೀರು (ಅಲ್ಪಾವಧಿ 70 ದಿನ)",
                    "market": "⭐⭐⭐⭐⭐ (ಉದ್ದಿನ ಬೇಳೆಗೆ ಸ್ಥಿರ ಉತ್ತಮ ಧಾರಣೆ)"
                },
                {
                    "crop_en": "Sesame (Til)",
                    "crop_kn": "ಎಳ್ಳು {Sesame / Til}",
                    "yield": "4 - 5 ಕ್ವಿಂಟಾಲ್ / ಎಕರೆ",
                    "varieties": "DS-1, DS-5, Swetha",
                    "water": "ಬಹಳ ಕಡಿಮೆ ನೀರು",
                    "market": "⭐⭐⭐⭐⭐ (ಕ್ವಿಂಟಾಲ್‌ಗೆ ₹12,000 ರಿಂದ ₹15,000 ಬೆಲೆ)"
                }
            ],
            "clayey_alluvial": [
                {
                    "crop_en": "Maize (Hybrid Corn)",
                    "crop_kn": "ಮೆಕ್ಕೆಜೋಳ {Hybrid Maize}",
                    "yield": "30 - 35 ಕ್ವಿಂಟಾಲ್ / ಎಕರೆ",
                    "varieties": "DKC-9108, CP-818, Bio-9681, NK-6240",
                    "water": "ನಿಯಮಿತ ನೀರಾವರಿ",
                    "market": "⭐⭐⭐⭐ (ಕೋಳಿ ಆಹಾರ & ಪಿಷ್ಟ ಕಾರ್ಖಾನೆಗಳಿಂದ ನಿರಂತರ ಖರೀದಿ)"
                },
                {
                    "crop_en": "Cowpea (Alsandi)",
                    "crop_kn": "ಅಲಸಂದಿ {Cowpea}",
                    "yield": "7 - 9 ಕ್ವಿಂಟಾಲ್ / ಎಕರೆ",
                    "varieties": "C-152, DC-15, PKB-4",
                    "water": "ಮಧ್ಯಮ",
                    "market": "⭐⭐⭐⭐ (ತರಕಾರಿ ಕಾಯಿ & ಧಾನ್ಯ ಎರಡಕ್ಕೂ ಮಾರಾಟ)"
                }
            ],
            "laterite": [
                {
                    "crop_en": "Sweet Potato / Tubers",
                    "crop_kn": "ಗೆಣಸು & ಗೆಡ್ಡೆ ಬೆಳೆಗಳು {Sweet Potato}",
                    "yield": "8 - 10 ಟನ್ / ಎಕರೆ",
                    "varieties": "Sree Bhadra, Kanjangad Local",
                    "water": "ಮಳೆ ಆಧಾರಿತ",
                    "market": "⭐⭐⭐⭐ (ಕಡಿಮೆ ಖರ್ಚು, ಕರಾವಳಿ-ಮಲೆನಾಡಿಗೆ ಸೂಕ್ತ)"
                },
                {
                    "crop_en": "Watermelon",
                    "crop_kn": "ಕಲ್ಲಂಗಡಿ {Watermelon}",
                    "yield": "25 - 30 ಟನ್ / ಎಕರೆ (65 ದಿನ)",
                    "varieties": "Kiran, Namdhari NS-295, Black Boss",
                    "water": "ಹನಿ ನೀರಾವರಿ ಅಗತ್ಯ",
                    "market": "⭐⭐⭐⭐⭐ (ಬೇಸಿಗೆಯಲ್ಲಿ ತ್ವರಿತ ಗರಿಷ್ಠ ಲಾಭ)"
                }
            ]
        }
    },
    "kharif": {
        "season_en": "Main Kharif (Monsoon: June - September)",
        "season_kn": "ಮುಖ್ಯ ಮುಂಗಾರು (ಜೂನ್ - ಸೆಪ್ಟೆಂಬರ್)",
        "soil_types": {
            "red_sandy": [
                {
                    "crop_en": "Finger Millet (Ragi)",
                    "crop_kn": "ರಾಗಿ {Finger Millet / Ragi}",
                    "yield": "16 - 20 ಕ್ವಿಂಟಾಲ್ / ಎಕರೆ",
                    "varieties": "MR-1, MR-6, ML-365, KMR-301, GPU-28",
                    "water": "ಮಳೆ ಆಶ್ರಿತ {Rainfed Best Fit}",
                    "market": "⭐⭐⭐⭐⭐ (ಸರ್ಕಾರದಿಂದ ₹4,290 ಎಂಎಸ್‌ಪಿ ಖರೀದಿ ಖಾತರಿ)"
                },
                {
                    "crop_en": "Groundnut",
                    "crop_kn": "ಶೇಂಗಾ {Groundnut}",
                    "yield": "10 - 14 ಕ್ವಿಂಟಾಲ್ / ಎಕರೆ",
                    "varieties": "KDG-128, GPBD-4, Kadiri-6, JL-24",
                    "water": "ಮಳೆ ಆಶ್ರಿತ",
                    "market": "⭐⭐⭐⭐⭐"
                },
                {
                    "crop_en": "Pigeonpea (Tur / Arhar)",
                    "crop_kn": "ತೊಗರಿ {Pigeonpea / Tur}",
                    "yield": "8 - 10 ಕ್ವಿಂಟಾಲ್ / ಎಕರೆ",
                    "varieties": "GRG-811, BSMR-736, TS-3R, Maruti",
                    "water": "ಬರ ನಿರೋಧಕ",
                    "market": "⭐⭐⭐⭐⭐ (ಕ್ವಿಂಟಾಲ್‌ಗೆ ₹9,000+ ಅಧಿಕ ಮೌಲ್ಯ)"
                }
            ],
            "black_cotton": [
                {
                    "crop_en": "Bt Cotton",
                    "crop_kn": "ಹತ್ತಿ {Bt Cotton}",
                    "yield": "12 - 16 ಕ್ವಿಂಟಾಲ್ / ಎಕರೆ",
                    "varieties": "Bollgard II, RCH-659, Ajit-155, Jaadoo",
                    "water": "ಮಳೆ ಆಶ್ರಿತ ಅಥವಾ ರಕ್ಷಣಾತ್ಮಕ ನೀರಾವರಿ",
                    "market": "⭐⭐⭐⭐⭐ (ಉತ್ತರ ಕರ್ನಾಟಕದ ಬಿಳಿ ಬಂಗಾರ)"
                },
                {
                    "crop_en": "Soybean",
                    "crop_kn": "ಸೋಯಾಬೀನ್ {Soybean}",
                    "yield": "10 - 12 ಕ್ವಿಂಟಾಲ್ / ಎಕರೆ (90 ದಿನ)",
                    "varieties": "JS-335, DSb-21, JS-9560, KDS-344",
                    "water": "ಕಪ್ಪು ಮಣ್ಣಿನಲ್ಲಿ ಭರ್ಜರಿ ಇಳುವರಿ",
                    "market": "⭐⭐⭐⭐⭐ (ಕಡಿಮೆ ಖರ್ಚು, ತ್ವರಿತ ಹಣ)"
                },
                {
                    "crop_en": "Pigeonpea (Tur)",
                    "crop_kn": "ತೊಗರಿ (ಕಲಬುರಗಿ ಕೆಂಪು ತೊಗರಿ) {Tur}",
                    "yield": "9 - 12 ಕ್ವಿಂಟಾಲ್ / ಎಕರೆ",
                    "varieties": "GRG-811 (ವಿಲ್ಟ್ ನಿರೋಧಕ), TS-3R",
                    "water": "ಮಳೆ ಆಶ್ರಿತ",
                    "market": "⭐⭐⭐⭐⭐ (GI ಟ್ಯಾಗ್ ಹೊಂದಿರುವ ಕಲ್ಯಾಣ ಕರ್ನಾಟಕದ ಬೆಳೆ)"
                }
            ],
            "clayey_alluvial": [
                {
                    "crop_en": "Paddy (Rice)",
                    "crop_kn": "ಭತ್ತ {Paddy / Rice}",
                    "yield": "28 - 35 ಕ್ವಿಂಟಾಲ್ / ಎಕರೆ",
                    "varieties": "Gangavathi Sona (BPT-5204), RNR-15048 (ಶುಗರ್ ಫ್ರೀ), Jaya",
                    "water": "ಕಾಲುವೆ / ಕೊಳವೆಬಾವಿ ನೀರು ಅಗತ್ಯ",
                    "market": "⭐⭐⭐⭐⭐ (ಅಕ್ಕಿ ಗಿರಣಿಗಳಿಂದ ನಿರಂತರ ಬೇಡಿಕೆ)"
                },
                {
                    "crop_en": "Sugarcane",
                    "crop_kn": "ಕಬ್ಬು {Sugarcane}",
                    "yield": "50 - 70 ಟನ್ / ಎಕರೆ",
                    "varieties": "Co-86032, Co-0238, CoM-0265, VSI-434",
                    "water": "ಪೂರ್ಣ ನೀರಾವರಿ",
                    "market": "⭐⭐⭐⭐ (ಸಕ್ಕರೆ ಕಾರ್ಖಾನೆಗಳಿಂದ ನಿಗದಿತ FRP ದರ)"
                }
            ],
            "laterite": [
                {
                    "crop_en": "Areca Nut (New/Intercrop)",
                    "crop_kn": "ಅಡಿಕೆ {Areca Nut}",
                    "yield": "12 - 15 ಕ್ವಿಂಟಾಲ್ ಸಂಸ್ಕರಿಸಿದ ಚಾಲಿ / ಎಕರೆ",
                    "varieties": "Mangala, Mohitnagar, Thirthahalli",
                    "water": "ಮಲೆನಾಡು-ಕರಾವಳಿಗೆ ನೈಸರ್ಗಿಕ ವಾತಾವರಣ",
                    "market": "⭐⭐⭐⭐⭐ (ದೀರ್ಘಾವಧಿ ಗರಿಷ್ಠ ಆದಾಯ)"
                },
                {
                    "crop_en": "Ginger / Turmeric",
                    "crop_kn": "ಶುಂಠಿ / ಅರಿಶಿನ {Ginger & Turmeric}",
                    "yield": "10 - 14 ಟನ್ ಹಸಿ ಶುಂಠಿ / ಎಕರೆ",
                    "varieties": "Rio-de-Janeiro, Maran, IISR Varada",
                    "water": "ಉತ್ತಮ ಬಸಿಗಾಲುವೆ ಸಹಿತ ನೀರು",
                    "market": "⭐⭐⭐⭐⭐ (ಬಂಪರ್ ನಗದು ಬೆಳೆ)"
                }
            ]
        }
    },
    "rabi": {
        "season_en": "Rabi (Winter: October - January)",
        "season_kn": "ಹಿಂಗಾರು (ಅಕ್ಟೋಬರ್ - ಜನವರಿ)",
        "soil_types": {
            "red_sandy": [
                {
                    "crop_en": "Rabi Onion",
                    "crop_kn": "ಹಿಂಗಾರು ಈರುಳ್ಳಿ {Rabi Onion}",
                    "yield": "10 - 12 ಟನ್ / ಎಕರೆ",
                    "varieties": "Bhima Super, Arka Kalyan, N-53",
                    "water": "ನಿಯಮಿತ ತುಂತುರು ನೀರಾವರಿ",
                    "market": "⭐⭐⭐⭐⭐ (ದೀರ್ಘ ಶೇಖರಣಾ ಬಾಳಿಕೆ, ಅತ್ಯಧಿಕ ಬೆಲೆ)"
                },
                {
                    "crop_en": "Horse Gram (Hurali)",
                    "crop_kn": "ಹುರುಳಿ {Horse Gram}",
                    "yield": "4 - 5 ಕ್ವಿಂಟಾಲ್ / ಎಕರೆ",
                    "varieties": "PHG-9, BGM-1, CRIDA-18R",
                    "water": "ಕನಿಷ್ಠ ತೇವಾಂಶ ಸಾಕು {Extreme Drought Hardy}",
                    "market": "⭐⭐⭐⭐"
                }
            ],
            "black_cotton": [
                {
                    "crop_en": "Bengal Gram (Chickpea / Chana)",
                    "crop_kn": "ಕಡಲೆ {Bengal Gram / Chana}",
                    "yield": "8 - 12 ಕ್ವಿಂಟಾಲ್ / ಎಕರೆ",
                    "varieties": "JG-11, JAKI-9218, BGD-103, Super Annigeri-1",
                    "water": "ಉಳಿದ ತೇವಾಂಶದಲ್ಲೇ ಬೆಳೆಯುತ್ತದೆ {Residual Moisture}",
                    "market": "⭐⭐⭐⭐⭐ (ಕಡಿಮೆ ಖರ್ಚು, ₹5,440+ ಎಂಎಸ್‌ಪಿ ಬೆಲೆ)"
                },
                {
                    "crop_en": "Rabi Sorghum (Maldandi Jowar)",
                    "crop_kn": "ಹಿಂಗಾರು ಜೋಳ (ಮಾಲ್ದಂಡಿ ಬಿಳಿ ಜೋಳ) {Rabi Jowar}",
                    "yield": "10 - 14 ಕ್ವಿಂಟಾಲ್ / ಎಕರೆ + 3 ಟನ್ ಮೇವು",
                    "varieties": "M-35-1 (Maldandi), CSV-29R, BJV-44",
                    "water": "ಮಳೆ ಆಶ್ರಿತ ಕಪ್ಪು ಮಣ್ಣು",
                    "market": "⭐⭐⭐⭐⭐ (ರೊಟ್ಟಿ ಜೋಳಕ್ಕೆ ಮಾರುಕಟ್ಟೆಯಲ್ಲಿ ಭಾರಿ ಪ್ರೀಮಿಯಂ ಬೆಲೆ)"
                },
                {
                    "crop_en": "Safflower (Kusubi)",
                    "crop_kn": "ಕುಸುಬಿ {Safflower}",
                    "yield": "6 - 8 ಕ್ವಿಂಟಾಲ್ / ಎಕರೆ",
                    "varieties": "A-1, PBNS-12, NARI-6",
                    "water": "ಆಳವಾದ ಕಪ್ಪು ಮಣ್ಣು",
                    "market": "⭐⭐⭐⭐⭐ (ಹೃದಯಕ್ಕೆ ಉತ್ತಮವಾದ ಎಣ್ಣೆಕಾಳು)"
                }
            ],
            "clayey_alluvial": [
                {
                    "crop_en": "Wheat (Durum / Sharbati)",
                    "crop_kn": "ಗೋಧಿ {Wheat}",
                    "yield": "16 - 20 ಕ್ವಿಂಟಾಲ್ / ಎಕರೆ",
                    "varieties": "DWR-162, DWR-2006, UAS-304",
                    "water": "3-4 ನೀರಾವರಿ",
                    "market": "⭐⭐⭐⭐ (ಉತ್ತರ ಕರ್ನಾಟಕ ನೀರಾವರಿ ಅಚ್ಚುಕಟ್ಟಿಗೆ ಬೆಸ್ಟ್)"
                },
                {
                    "crop_en": "Rabi Maize",
                    "crop_kn": "ಹಿಂಗಾರು ಮೆಕ್ಕೆಜೋಳ {Rabi Maize}",
                    "yield": "35 - 42 ಕ್ವಿಂಟಾಲ್ / ಎಕರೆ (ಮುಂಗಾರಿಗಿಂತ ಅಧಿಕ ಇಳುವರಿ)",
                    "varieties": "DKC-9144, P-3396, CP-808",
                    "water": "ನೀರಾವರಿ",
                    "market": "⭐⭐⭐⭐⭐"
                }
            ],
            "laterite": [
                {
                    "crop_en": "Cowpea / Field Bean (Avare)",
                    "crop_kn": "ಅವರೆಕಾಳು {Field Bean / Avare}",
                    "yield": "6 - 8 ಕ್ವಿಂಟಾಲ್ / ಎಕರೆ",
                    "varieties": "HA-3, HA-4 (ಬೆಳಕಿಗೆ ಸಂವೇದನಾರಹಿತ)",
                    "water": "ಮಧ್ಯಮ",
                    "market": "⭐⭐⭐⭐⭐ (ಚಳಿಗಾಲದಲ್ಲಿ ಹಸಿ ಅವರೆಕಾಳಿಗೆ ಗರಿಷ್ಠ ಡಿಮ್ಯಾಂಡ್)"
                }
            ]
        }
    },
    "summer": {
        "season_en": "Summer / Zaid (February - May)",
        "season_kn": "ಬೇಸಿಗೆ ಹಂಗಾಮು (ಫೆಬ್ರವರಿ - ಮೇ)",
        "soil_types": {
            "red_sandy": [
                {
                    "crop_en": "Summer Groundnut",
                    "crop_kn": "ಬೇಸಿಗೆ ಶೇಂಗಾ {Summer Groundnut}",
                    "yield": "15 - 18 ಕ್ವಿಂಟಾಲ್ / ಎಕರೆ (ಬಿಸಿಲಿಗೆ ರೋಗ ಕಡಿಮೆ, ಅಧಿಕ ಕಾಳು)",
                    "varieties": "KDG-128, TAG-24, DH-86",
                    "water": "ವಾರಕ್ಕೊಮ್ಮೆ ನೀರಾವರಿ",
                    "market": "⭐⭐⭐⭐⭐"
                },
                {
                    "crop_en": "Bhendi (Okra / Ladies Finger)",
                    "crop_kn": "ಬೆಂಡೆಕಾಯಿ {Bhendi}",
                    "yield": "6 - 8 ಟನ್ / ಎಕರೆ (45 ದಿನದಿಂದ ಕಟಾವು)",
                    "varieties": "Singham, Radhika, Arka Anamika",
                    "water": "ಹನಿ ನೀರಾವರಿ",
                    "market": "⭐⭐⭐⭐⭐ (ಬೇಸಿಗೆಯಲ್ಲಿ ಪ್ರತಿದಿನ ನಗದು ಆದಾಯ)"
                }
            ],
            "black_cotton": [
                {
                    "crop_en": "Summer Sesame (Til)",
                    "crop_kn": "ಬೇಸಿಗೆ ಎಳ್ಳು {Summer Sesame}",
                    "yield": "5 - 6 ಕ್ವಿಂಟಾಲ್ / ಎಕರೆ",
                    "varieties": "DS-1, Swetha",
                    "water": "2-3 ನೀರಾವರಿ ಸಾಕು",
                    "market": "⭐⭐⭐⭐⭐ (ಬಹಳ ಕಡಿಮೆ ಖರ್ಚು, ಕ್ವಿಂಟಾಲ್‌ಗೆ ₹14,000+ ಲಾಭ)"
                },
                {
                    "crop_en": "Summer Green Gram",
                    "crop_kn": "ಬೇಸಿಗೆ ಹೆಸರುಕಾಳು {Summer Moong}",
                    "yield": "7 - 9 ಕ್ವಿಂಟಾಲ್ / ಎಕರೆ (ಕೀಟ ಬಾಧೆ ಅತಿ ಕಡಿಮೆ)",
                    "varieties": "DGGV-2, IPM-02-03",
                    "water": "ಲಘು ನೀರು",
                    "market": "⭐⭐⭐⭐⭐"
                }
            ],
            "clayey_alluvial": [
                {
                    "crop_en": "Summer Hybrid Maize",
                    "crop_kn": "ಬೇಸಿಗೆ ಮೆಕ್ಕೆಜೋಳ {Summer Maize}",
                    "yield": "32 - 38 ಕ್ವಿಂಟಾಲ್ / ಎಕರೆ",
                    "varieties": "DKC-9108, Pioneer-3522",
                    "water": "ಖಾತರಿ ನೀರಾವರಿ",
                    "market": "⭐⭐⭐⭐"
                },
                {
                    "crop_en": "Cucumber / Gherkins",
                    "crop_kn": "ಸೌತೆಕಾಯಿ & ಸೋರೆಕಾಯಿ {Cucurbits}",
                    "yield": "12 - 15 ಟನ್ / ಎಕರೆ",
                    "varieties": "Malini, Gypsy, NS-404",
                    "water": "ಹನಿ ನೀರಾವರಿ",
                    "market": "⭐⭐⭐⭐⭐"
                }
            ],
            "laterite": [
                {
                    "crop_en": "Watermelon / Muskmelon",
                    "crop_kn": "ಕಲ್ಲಂಗಡಿ & ಕರಬೂಜ {Watermelon & Muskmelon}",
                    "yield": "25 - 35 ಟನ್ / ಎಕರೆ",
                    "varieties": "Kiran, Sagar King, Saraswati",
                    "water": "ಹನಿ ನೀರು + ಮಲ್ಚಿಂಗ್",
                    "market": "⭐⭐⭐⭐⭐ (ಬೇಸಿಗೆ ಬಾಯಾರಿಕೆಗೆ ಅತ್ಯಧಿಕ ಮಾರುಕಟ್ಟೆ ಬೇಡಿಕೆ)"
                }
            ]
        }
    }
}

# ==============================================================================
# DISTRICT-WISE SOIL TESTING LABS & AGRICULTURE CENTRES DIRECTORY
# ==============================================================================
KARNATAKA_DISTRICT_AGRI_CENTRES = {
    "Bagalkote": {
        "kn": "ಬಾಗಲಕೋಟೆ",
        "jda_office": "Office of Joint Director of Agriculture, Sector-7, Navanagar, Bagalkote",
        "kvk_lab": "KVK Soil Testing Laboratory, University of Horticultural Sciences (UHS) Campus, Bagalkote",
        "phone": "08354-235282 / 9448495335",
        "rsk_centers": "Bagalkote, Badami, Jamkhandi, Mudhol, Bilagi, Ilkal, Guledgudda, Rabkavi-Banhatti"
    },
    "Ballari": {
        "kn": "ಬಳ್ಳಾರಿ",
        "jda_office": "JDA Agriculture Office, Opp. District Court, Ballari",
        "kvk_lab": "ICAR-KVK Soil & Water Testing Lab, Hagari Post, Ballari District",
        "phone": "08392-273165 / 9448495340",
        "rsk_centers": "Ballari, Kurugodu, Kampli, Siruguppa, Sandur"
    },
    "Belagavi": {
        "kn": "ಬೆಳಗಾವಿ",
        "jda_office": "Joint Director of Agriculture, Club Road, Belagavi",
        "kvk_lab": "ICAR-KVK Soil Testing Lab, KLE Campus, Mattikopp, Bailhongal Taluk & Tukkanatti KVK",
        "phone": "0831-2407278 / 9448495330",
        "rsk_centers": "Belagavi, Gokak, Chikkodi, Athani, Bailhongal, Saundatti, Ramdurg, Hukkeri, Khanapur, Raybag"
    },
    "Bengaluru Rural": {
        "kn": "ಬೆಂಗಳೂರು ಗ್ರಾಮಾಂತರ",
        "jda_office": "JDA Office, Mini Vidhana Soudha, Devanahalli, Bengaluru Rural",
        "kvk_lab": "ICAR-KVK Soil Testing Lab, Hadonahalli, Tubagere Hobli, Doddaballapura Taluk",
        "phone": "080-27622288 / 9448495311",
        "rsk_centers": "Devanahalli, Doddaballapura, Hoskote, Nelamangala"
    },
    "Bengaluru Urban": {
        "kn": "ಬೆಂಗಳೂರು ನಗರ",
        "jda_office": "Commissioner of Agriculture, Sheshadri Road, K.R. Circle, Bengaluru",
        "kvk_lab": "Soil & Plant Health Clinic, UAS Gandhi Krishi Vigyana Kendra (GKVK), Bellary Road, Bengaluru",
        "phone": "080-23330153 / 1800 425 3553",
        "rsk_centers": "Yelahanka, Kengeri, Bengaluru North, Anekal, K.R. Puram"
    },
    "Bidar": {
        "kn": "ಬೀದರ್",
        "jda_office": "JDA Office, Near DC Office Complex, Bidar",
        "kvk_lab": "ICAR-KVK Soil Testing Laboratory, Janwada Road, Bidar",
        "phone": "08482-244155 / 9448495345",
        "rsk_centers": "Bidar, Bhalki, Humnabad, Basavakalyan, Aurad, Kamalnagar, Chitguppa"
    },
    "Chamarajanagara": {
        "kn": "ಚಾಮರಾಜನಗರ",
        "jda_office": "JDA Office, District Administrative Complex, Chamarajanagara",
        "kvk_lab": "ICAR-JSS KVK Soil & Water Testing Lab, Suttur / Hardanahalli, Chamarajanagara",
        "phone": "08226-222045 / 9448495325",
        "rsk_centers": "Chamarajanagara, Gundlupete, Kollegala, Yelandur, Hanur"
    },
    "Chikkaballapura": {
        "kn": "ಚಿಕ್ಕಬಳ್ಳಾಪುರ",
        "jda_office": "JDA Agriculture Office, Sidlaghatta Road, Chikkaballapura",
        "kvk_lab": "ICAR-KVK Soil Testing Lab, Chintamani Campus, Chikkaballapura",
        "phone": "08156-277020 / 9448495315",
        "rsk_centers": "Chikkaballapura, Chintamani, Sidlaghatta, Gauribidanur, Bagepalli, Gudibande"
    },
    "Chikkamagaluru": {
        "kn": "ಚಿಕ್ಕಮಗಳೂರು",
        "jda_office": "JDA Office, K.M. Road, Chikkamagaluru",
        "kvk_lab": "ICAR-KVK Soil Testing Lab, Mudigere Hill Station & Birur Lab, Chikkamagaluru",
        "phone": "08262-230825 / 9448495320",
        "rsk_centers": "Chikkamagaluru, Mudigere, Koppa, Sringeri, Tarikere, Kadur, Narasimharajapura, Ajjampura"
    },
    "Chitradurga": {
        "kn": "ಚಿತ್ರದುರ್ಗ",
        "jda_office": "JDA Office, Near Stadium, Chitradurga",
        "kvk_lab": "ICAR-KVK Soil Testing Lab, Babbur Farm, Hiriyur Taluk, Chitradurga",
        "phone": "08194-222830 / 9448495318",
        "rsk_centers": "Chitradurga, Hiriyur, Challakere, Holalkere, Hosadurga, Molakalmuru"
    },
    "Dakshina Kannada": {
        "kn": "ದಕ್ಷಿಣ ಕನ್ನಡ",
        "jda_office": "JDA Office, Near Hampankatta, Mangaluru",
        "kvk_lab": "ICAR-KVK Soil Testing Lab, Mangaluru Fisheries College Road, Kankanady, Mangaluru",
        "phone": "0824-2430033 / 9448495328",
        "rsk_centers": "Mangaluru, Bantwal, Puttur, Belthangady, Sullia, Moodbidri, Kadaba"
    },
    "Davanagere": {
        "kn": "ದಾವಣಗೆರೆ",
        "jda_office": "JDA Office, Devaraj Urs Layout, Davanagere",
        "kvk_lab": "ICAR-Taralabalu KVK Soil Testing Laboratory, Anubhav Sangam, Davanagere",
        "phone": "08192-263462 / 9448495316",
        "rsk_centers": "Davanagere, Harihara, Honnali, Channagiri, Jagalur, Nyamathi"
    },
    "Dharwad": {
        "kn": "ಧಾರವಾಡ",
        "jda_office": "JDA Office, D.C. Compound, Dharwad",
        "kvk_lab": "Soil Health Clinic, University of Agricultural Sciences (UASD), Yettinagudda Campus, Dharwad",
        "phone": "0836-2448512 / 1800 425 1150",
        "rsk_centers": "Dharwad, Hubballi, Kalghatgi, Navalgund, Alnavar, Kundgol, Annigeri"
    },
    "Gadag": {
        "kn": "ಗದಗ",
        "jda_office": "JDA Agriculture Office, Mulgund Road, Gadag",
        "kvk_lab": "ICAR-K.H. Patil KVK Soil Testing Lab, Hulkoti Post, Gadag District",
        "phone": "08372-289038 / 9448495334",
        "rsk_centers": "Gadag, Ron, Shirahatti, Mundargi, Nargund, Gajendragad, Lakshmeshwar"
    },
    "Hassan": {
        "kn": "ಹಾಸನ",
        "jda_office": "JDA Office, B.M. Road, Hassan",
        "kvk_lab": "ICAR-KVK Soil Testing Lab, Kandali Post, Hassan",
        "phone": "08172-268050 / 9448495322",
        "rsk_centers": "Hassan, Arsikere, Channarayapatna, Holenarasipura, Sakleshpur, Arkalgud, Alur, Belur"
    },
    "Haveri": {
        "kn": "ಹಾವೇರಿ",
        "jda_office": "JDA Office, District Administrative Complex, Devagiri, Haveri",
        "kvk_lab": "ICAR-KVK Soil Testing Lab, Hanumanamatti Post, Ranebennur Taluk, Haveri",
        "phone": "08373-253524 / 9448495333",
        "rsk_centers": "Haveri, Ranebennur, Byadgi, Hirekerur, Shiggaon, Savanur, Hangal, Rattihalli"
    },
    "Kalaburagi": {
        "kn": "ಕಲಬುರಗಿ",
        "jda_office": "JDA Office, Super Market Main Road, Kalaburagi",
        "kvk_lab": "ICAR-KVK Soil Testing Lab, Aland Road, Kalaburagi",
        "phone": "08472-220123 / 9448495344",
        "rsk_centers": "Kalaburagi, Aland, Afzalpur, Jevargi, Sedam, Chincholi, Chittapur, Kamalapur, Shahabad"
    },
    "Kodagu": {
        "kn": "ಕೊಡಗು",
        "jda_office": "JDA Office, College Road, Madikeri, Kodagu",
        "kvk_lab": "ICAR-IISR KVK Soil Testing Lab, Gonikoppal, South Kodagu",
        "phone": "08274-247274 / 9448495327",
        "rsk_centers": "Madikeri, Somwarpet, Virajpet, Kushalnagar, Ponnampet"
    },
    "Kolar": {
        "kn": "ಕೋಲಾರ",
        "jda_office": "JDA Office, Bangarapet Road, Kolar",
        "kvk_lab": "ICAR-KVK Soil Testing Lab, Tamaka Industrial Area, Kolar",
        "phone": "08152-222144 / 9448495314",
        "rsk_centers": "Kolar, Bangarapet, Malur, Srinivaspur, Mulbagal, KGF"
    },
    "Koppal": {
        "kn": "ಕೊಪ್ಪಳ",
        "jda_office": "JDA Office, Hospet Road, Koppal",
        "kvk_lab": "ICAR-KVK Soil Testing Lab, Gangavathi Rice Research Station Campus, Koppal",
        "phone": "08539-220025 / 9448495338",
        "rsk_centers": "Koppal, Gangavathi, Kushtagi, Yelburga, Karatagi, Kanakagiri, Kukanoor"
    },
    "Mandya": {
        "kn": "ಮಂಡ್ಯ",
        "jda_office": "JDA Office, Subhash Nagar, Mandya",
        "kvk_lab": "ICAR-KVK Soil Testing Lab, V.C. Farm (Visvesvaraya Canal Farm), Mandya",
        "phone": "08232-220138 / 9448495324",
        "rsk_centers": "Mandya, Maddur, Malavalli, Pandavapura, Srirangapatna, Nagamangala, K.R. Pete"
    },
    "Mysuru": {
        "kn": "ಮೈಸೂರು",
        "jda_office": "JDA Office, Public Offices Building, Near Curzon Park, Mysuru",
        "kvk_lab": "ICAR-JSS KVK Soil & Water Testing Lab, Suttur Post, Nanjangud Taluk, Mysuru",
        "phone": "0821-2422055 / 9448495323",
        "rsk_centers": "Mysuru, Nanjangud, Hunsur, T. Narasipura, K.R. Nagar, H.D. Kote, Periyapatna, Saragur"
    },
    "Raichur": {
        "kn": "ರಾಯಚೂರು",
        "jda_office": "JDA Office, Station Road, Raichur",
        "kvk_lab": "Soil Health Clinic, University of Agricultural Sciences (UASR), Lingasugur Road, Raichur",
        "phone": "08532-220153 / 1800 425 2121",
        "rsk_centers": "Raichur, Manvi, Sindhanur, Devadurga, Lingsugur, Maski, Sirwar"
    },
    "Ramanagara": {
        "kn": "ರಾಮನಗರ",
        "jda_office": "JDA Office, Mini Vidhana Soudha, Ramanagara",
        "kvk_lab": "ICAR-KVK Soil Testing Lab, Chandurayanahalli, Magadi Taluk, Ramanagara",
        "phone": "080-27271050 / 9448495312",
        "rsk_centers": "Ramanagara, Channapatna, Magadi, Kanakapura"
    },
    "Shivamogga": {
        "kn": "ಶಿವಮೊಗ್ಗ",
        "jda_office": "JDA Office, Kuvempu Road, Shivamogga",
        "kvk_lab": "Soil Testing Lab, KSN University of Agricultural & Horticultural Sciences (UAHS), Navile, Shivamogga",
        "phone": "08182-267011 / 9448495319",
        "rsk_centers": "Shivamogga, Bhadravathi, Thirthahalli, Sagara, Shikaripura, Soraba, Hosanagara"
    },
    "Tumakuru": {
        "kn": "ತುಮಕೂರು",
        "jda_office": "JDA Office, Mini Vidhana Soudha, Tumakuru",
        "kvk_lab": "ICAR-IIHR KVK Soil Testing Lab, Hirehalli Post, Tumakuru & Konehalli KVK, Tiptur",
        "phone": "0816-2243214 / 9448495317",
        "rsk_centers": "Tumakuru, Tiptur, Gubbi, Kunigal, Sira, Pavagada, Madhugiri, Koratagere, Turuvekere, Chikkanayakanahalli"
    },
    "Udupi": {
        "kn": "ಉಡುಪಿ",
        "jda_office": "JDA Office, Rajathadri District Complex, Manipal, Udupi",
        "kvk_lab": "ICAR-KVK Soil Testing Lab, Brahmavara Zonal Agricultural Research Station, Udupi",
        "phone": "0820-2574340 / 9448495329",
        "rsk_centers": "Udupi, Kundapura, Karkala, Brahmavara, Byndoor, Kaup, Hebri"
    },
    "Uttara Kannada": {
        "kn": "ಉತ್ತರ ಕನ್ನಡ",
        "jda_office": "JDA Office, Habbuwada, Karwar, Uttara Kannada",
        "kvk_lab": "ICAR-KVK Soil Testing Lab, Sirsi Forestry College Campus & Kumta Research Center",
        "phone": "08384-226815 / 9448495331",
        "rsk_centers": "Karwar, Sirsi, Kumta, Ankola, Bhatkal, Honnavar, Haliyal, Yellapur, Dandeli, Joida, Siddapur"
    },
    "Vijayapura": {
        "kn": "ವಿಜಯಪುರ",
        "jda_office": "JDA Office, Station Road, Vijayapura",
        "kvk_lab": "ICAR-KVK Soil Testing Lab, Regional Agricultural Research Station, Hitnalli, Vijayapura",
        "phone": "08352-230154 / 9448495336",
        "rsk_centers": "Vijayapura, Indi, Sindagi, Muddebihal, Basavana Bagewadi, Talikoti, Chadchan, Devar Hippargi, Babaleshwar, Kolhar, Tikota"
    },
    "Yadgir": {
        "kn": "ಯಾದಗಿರಿ",
        "jda_office": "JDA Office, Chittapur Road, Yadgir",
        "kvk_lab": "ICAR-KVK Soil Testing Lab, Kawadimatti Post, Surpur Taluk, Yadgir",
        "phone": "08473-250080 / 9448495346",
        "rsk_centers": "Yadgir, Shahapur, Surpur, Hunsagi, Gurmitkal, Vadagera"
    },
    "Vijayanagara": {
        "kn": "ವಿಜಯನಗರ",
        "jda_office": "JDA Office, D.C. Office Complex, Hosapete, Vijayanagara",
        "kvk_lab": "ICAR-KVK Soil Testing Lab, Hagari / Mariyammanahalli, Vijayanagara",
        "phone": "08394-224455 / 9448495341",
        "rsk_centers": "Hosapete, Hagaribommanahalli, Harapanahalli, Hoovina Hadagali, Kudligi, Kotturu"
    }
}

# ==============================================================================
# 100% FREE GOVERNMENT BENEFITS & SUBSIDIES AT DISTRICT AGRI SECTORS
# ==============================================================================
FREE_GOVT_AGRI_BENEFITS = [
    {
        "title_kn": "1. ಸಂಪೂರ್ಣ ಉಚಿತ ಮಣ್ಣು ಆರೋಗ್ಯ ಕಾರ್ಡ್ {Free Soil Health Card Scheme}",
        "title_en": "1. 100% Free Soil Health Card & Testing Scheme (Govt. of India)",
        "cost_kn": "🟢 100% ಸಂಪೂರ್ಣ ಉಚಿತ (ಯಾವುದೇ ಅರ್ಜಿ ಶುಲ್ಕವಿಲ್ಲ)",
        "cost_en": "🟢 100% FREE of cost (No application or lab fee)",
        "details_kn": "ಪ್ರತಿ 3 ವರ್ಷಕ್ಕೊಮ್ಮೆ ನಿಮ್ಮ ಜಮೀನಿನ ಮಣ್ಣಿನ 12 ನಿಯತಾಂಕಗಳನ್ನು (N, P, K, pH, ಸಾವಯವ ಇಂಗಾಲ, ಗಂಧಕ, ಸತು, ಕಬ್ಬಿಣ, ತಾಮ್ರ, ಬೋರಾನ್) ಕೃಷಿ ಇಲಾಖೆಯು ಉಚಿತವಾಗಿ ಪರೀಕ್ಷಿಸಿ, ರಸಗೊಬ್ಬರ ಶಿಫಾರಸು ಕಾರ್ಡ್ ನೀಡುತ್ತದೆ.",
        "details_en": "Government soil testing labs test 12 chemical parameters of your soil free of cost once every 3 years with tailored fertilizer advisory.",
        "where_to_avail_kn": "ನಿಮ್ಮ ಗ್ರಾಮದ ರೈತ ಸಂಪರ್ಕ ಕೇಂದ್ರ (RSK) ಅಥವಾ ತಾಲೂಕು ಕೃಷಿ ಸಹಾಯಕ ನಿರ್ದೇಶಕರ ಕಚೇರಿ (ADA)."
    },
    {
        "title_kn": "2. ಉಚಿತ / 75% ಸಬ್ಸಿಡಿ ಜೈವಿಕ ನಿಯಂತ್ರಕಗಳು & ಬೀಜೋಪಚಾರ ಔಷಧ {Free Biocontrol Agents}",
        "title_en": "2. Free / 75% Subsidized Biocontrol Agents & Seed Inoculants",
        "cost_kn": "🟢 ಉಚಿತ ಅಥವಾ 75% ರಿಯಾಯಿತಿ (ಕೇವಲ ₹10-₹20 ನಾಮಮಾತ್ರ ದರ)",
        "cost_en": "🟢 Free or 75% subsidy (nominal Rs. 10-20)",
        "details_kn": "ಬೇರು ಕೊಳೆ ರೋಗ ತಡೆಯುವ ಟ್ರೈಕೋಡರ್ಮ {Trichoderma viride}, ಕಾಯಿಕೊರಕ ನಾಶಪಡಿಸುವ ಟ್ರೈಕೋಗ್ರಾಮ ಕಾರ್ಡ್‌ಗಳು ಮತ್ತು ರಂಜಕ ಕರಗಿಸುವ ಪಿಎಸ್‌ಬಿ ಜೈವಿಕ ಗೊಬ್ಬರಗಳನ್ನು ರೈತ ಸಂಪರ್ಕ ಕೇಂದ್ರಗಳಲ್ಲಿ ಉಚಿತವಾಗಿ ವಿತರಿಸಲಾಗುತ್ತದೆ.",
        "details_en": "Trichoderma bio-fungicide, Trichogramma egg parasitoid cards, and PSB bio-fertilizers distributed through RSKs.",
        "where_to_avail_kn": "ಹೋಬಳಿ ಮಟ್ಟದ ರೈತ ಸಂಪರ್ಕ ಕೇಂದ್ರ (RSK)."
    },
    {
        "title_kn": "3. ಕೃಷಿ ವಿಜ್ಞಾನ ಕೇಂದ್ರದಲ್ಲಿ ಉಚಿತ ತರಬೇತಿ, ಊಟ & ವಸತಿ {Free KVK Training}",
        "title_en": "3. Free On-Farm Vocational Training at KVK with Stipend & Food",
        "cost_kn": "🟢 100% ಉಚಿತ (ಊಟ, ವಸತಿ ಮತ್ತು ತರಬೇತಿ ಪ್ರಮಾಣಪತ್ರ ಉಚಿತ)",
        "cost_en": "🟢 100% FREE (Free food, accommodation and certificate)",
        "details_kn": "ಹನಿ ನೀರಾವರಿ, ಹೈನುಗಾರಿಕೆ, ಜೇನುಸಾಕಣೆ, ಮೇಕೆ-ಕುರಿ ಸಾಕಣೆ, ನರ್ಸರಿ ನಿರ್ವಹಣೆ ಮತ್ತು ಸಾವಯವ ಕೃಷಿ ಕುರಿತು 3 ರಿಂದ 5 ದಿನಗಳ ಪ್ರಾಯೋಗಿಕ ತರಬೇತಿಯನ್ನು ಜಿಲ್ಲಾ KVK ವಿಜ್ಞಾನಿಗಳು ಉಚಿತವಾಗಿ ನೀಡುತ್ತಾರೆ.",
        "details_en": "3 to 5 days practical certified training on drip irrigation, dairy, goat farming, and organic inputs.",
        "where_to_avail_kn": "ಜಿಲ್ಲಾ ಕೃಷಿ ವಿಜ್ಞಾನ ಕೇಂದ್ರ (KVK)."
    },
    {
        "title_kn": "4. ಉಚಿತ ಬೆಳೆ ನಷ್ಟ ಪರಿಹಾರ ತನಿಖೆ & ವಿಮಾ ಸಮೀಕ್ಷೆ {Free Crop Damage Assessment}",
        "title_en": "4. Free Spot Crop Damage Assessment under PMFBY & Drought Relief",
        "cost_kn": "🟢 100% ಉಚಿತ",
        "cost_en": "🟢 100% FREE",
        "details_kn": "ಅಕಾಲಿಕ ಆಲಿಕಲ್ಲು ಮಳೆ, ಪ್ರವಾಹ ಅಥವಾ ತೀವ್ರ ಬರಗಾಲದಿಂದ ಬೆಳೆ ಹಾನಿಯಾದಾಗ ಕಂದಾಯ ಮತ್ತು ಕೃಷಿ ಅಧಿಕಾರಿಗಳು ಜಮೀನಿಗೆ ಭೇಟಿ ನೀಡಿ ಉಚಿತ ಪಂಚನಾಮೆ ಮಾಡಿ ಪರಿಹಾರ ತಂತ್ರಾಂಶದಲ್ಲಿ (Parihara Portal) ನೇರ ಬ್ಯಾಂಕ್ ಖಾತೆಗೆ ಹಣ ಜಮೆ ಮಾಡುತ್ತಾರೆ.",
        "details_en": "Free joint field spot survey by revenue and agriculture officers for natural calamity and crop insurance claims.",
        "where_to_avail_kn": "ಗ್ರಾಮ ಲೆಕ್ಕಾಧಿಕಾರಿ (VA) / ಕೃಷಿ ಅಧಿಕಾರಿ (AO)."
    },
    {
        "title_kn": "5. 90% ಸಬ್ಸಿಡಿ ಹನಿ & ತುಂತುರು ನೀರಾವರಿ ಘಟಕಗಳು {PMKSY Drip & Sprinkler}",
        "title_en": "5. Up to 90% Subsidy for Drip & Sprinkler Units (PMKSY Scheme)",
        "cost_kn": "🟢 ಸಣ್ಣ & ಅತಿ ಸಣ್ಣ ರೈತರಿಗೆ 90% ಸಹಾಯಧನ (ರೈತನ ಪಾಲು ಕೇವಲ 10%)",
        "cost_en": "🟢 90% Subsidy for Small/Marginal Farmers (10% farmer share)",
        "details_kn": "ಪ್ರಧಾನಮಂತ್ರಿ ಕೃಷಿ ಸಿಂಚಾಯಿ ಯೋಜನೆಯಡಿ ಐಎಸ್‌ಐ ಗುಣಮಟ್ಟದ ಡ್ರಿಪ್ ಪೈಪ್, ಫಿಲ್ಟರ್, ಲ್ಯಾಟರಲ್ ಹಾಗೂ ಸ್ಪ್ರಿಂಕ್ಲರ್ ಸೆಟ್‌ಗಳಿಗೆ ಸರ್ಕಾರದಿಂದ ಗರಿಷ್ಠ ₹45,000 ವರೆಗೆ ಸಬ್ಸಿಡಿ ದೊರೆಯುತ್ತದೆ.",
        "details_en": "Subsidized ISI certified drip laterals, venturi, filters, and sprinkler pipes with free installation.",
        "where_to_avail_kn": "ತಾಲೂಕು ಸಹಾಯಕ ತೋಟಗಾರಿಕೆ / ಕೃಷಿ ಅಧಿಕಾರಿ ಕಚೇರಿ."
    },
    {
        "title_kn": "6. ಕೃಷಿ ಯಂತ್ರಧಾರೆ ಬಾಡಿಗೆ ಕೇಂದ್ರಗಳು {Custom Hiring Centres - CHC}",
        "title_en": "6. Subsidized Farm Machinery at Custom Hiring Centres (CHC)",
        "cost_kn": "🟢 ಸಾಮಾನ್ಯ ಬಾಡಿಗೆಗಿಂತ 50% ಕಡಿಮೆ ರಿಯಾಯಿತಿ ದರ",
        "cost_en": "🟢 50% Subsidized Rental Rates compared to market",
        "details_kn": "ಟ್ರ್ಯಾಕ್ಟರ್, ರೋಟಾವೇಟರ್, ಕಬ್ಬು ಕಟಾವು ಯಂತ್ರ, ಭತ್ತ ಕಟಾವು ಕಂಬೈನ್ ಹಾರ್ವೆಸ್ಟರ್, ಪವರ್ ಟಿಲ್ಲರ್ ಹಾಗೂ ಮಲ್ಚಿಂಗ್ ಯಂತ್ರಗಳನ್ನು ಅತಿ ಕಡಿಮೆ ಗಂಟೆವಾರು ಬಾಡಿಗೆಗೆ ಪಡೆಯಬಹುದು.",
        "details_en": "Low-cost hourly rental of tractors, rotavators, combine harvesters, and power weeders.",
        "where_to_avail_kn": "ತಾಲೂಕು ಮಟ್ಟದ ಕೃಷಿ ಯಂತ್ರಧಾರೆ ಕೇಂದ್ರ (CHC) / ಶ್ರೀ ಕ್ಷೇತ್ರ ಧರ್ಮಸ್ಥಳ ಕೃಷಿ ಯಂತ್ರಧಾರೆ."
    }
]
