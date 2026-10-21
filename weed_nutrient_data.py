"""
Weed Suppression & On-Farm Organic Nutrient Advisory Data
Scientific references:
- ICAR - Directorate of Weed Research (DWR), Jabalpur
- UAS Bangalore (GKVK) & UAS Dharwad Package of Practices
- TNAU Agritech Organic Farming & Vermicomposting Portal
- Central Insecticides Board & Registration Committee (CIBRC) Banned Chemical Lists
- National Centre of Organic and Natural Farming (NCONF), Ghaziabad
"""

# 1. MAJOR KARNATAKA WEED PROFILES & NON-CHEMICAL SUPPRESSION
WEEDS_DATA = [
    {
        "id": "cynodon",
        "name_en": "Bermuda Grass / Wiregrass",
        "name_kn": "ಹರಿಕೆ / ಗರಿಕೆ ಹುಲ್ಲು",
        "botanical": "Cynodon dactylon",
        "type": "Perennial Grass (ದೀರ್ಘಾವಧಿ ಹುಲ್ಲು)",
        "damage_en": "Forms dense underground rhizome mats down to 30 cm. Robs nitrogen and soil moisture, drastically cutting yields in maize, cotton, sugarcane, and pulses.",
        "damage_kn": "ನೆಲದೊಳಗೆ 30 ಸೆಂ.ಮೀ. ವರೆಗೆ ಬೇರು ಮತ್ತು ಗಂಟುಗಳ ಬಲವಾದ ಜಾಲವನ್ನು ಹರಡುತ್ತದೆ. ಮಣ್ಣಿನ ಸಾರಜನಕ ಮತ್ತು ತೇವಾಂಶವನ್ನು ಹೀರಿ ಮುಸುಕಿನ ಜೋಳ, ಹತ್ತಿ, ಕಬ್ಬು ಮತ್ತು ದ್ವಿದಳ ಧಾನ್ಯಗಳಲ್ಲಿ ಇಳುವರಿಯನ್ನು ಕುಂಠಿತಗೊಳಿಸುತ್ತದೆ.",
        "tactics_en": [
            "Deep Summer Ploughing (ಬೇಸಿಗೆಯ ಆಳವಾದ ಉಳುಮೆ): Plough twice during April-May peak heat. Expose underground rhizomes to 40°C+ baking sun for 3 weeks.",
            "Smother Cropping: Dense sowing of Sunn hemp (ಸಣಬು) or fodder cowpea (ಅಲಸಂದೆ) shades out regrowth completely within 45 days.",
            "Stale Seedbed Method: Pre-irrigate 10 days before sowing, let stolons sprout, then shallow-till to exhaust carbohydrate reserves in roots.",
            "Exhaustion: Never allow seed heads to form; repeat mechanical inter-cultivation (ಎಡೆಕುಂಟೆ ಹೊಡೆಯುವುದು) at 21-day intervals."
        ],
        "tactics_kn": [
            "ಬೇಸಿಗೆಯ ಆಳವಾದ ಉಳುಮೆ: ಏಪ್ರಿಲ್-ಮೇ ತಿಂಗಳ ಸುಡುವ ಬಿಸಿಲಿನಲ್ಲಿ 2-3 ಬಾರಿ ಆಳವಾಗಿ ಉಳುಮೆ ಮಾಡಿ, ನೆಲದೊಳಗಿನ ಬೇರು-ಗಂಟುಗಳನ್ನು ಬಿಸಿಲಿಗೆ ಒಡ್ಡಿ ಒಣಗಿಸಿ.",
            "ದಟ್ಟ ಸಹಬೆಳೆ ಹೊದಿಕೆ: ಸಣಬು ಅಥವಾ ಮೇವಿನ ಅಲಸಂದೆಯನ್ನು ದಟ್ಟವಾಗಿ ಬಿತ್ತುವುದರಿಂದ ಸೂರ್ಯನ ಬೆಳಕು ಸಿಗದೆ ಹರಿಕೆಯ ಚಿಗುರುಗಳು ಸಂಪೂರ್ಣವಾಗಿ ನಾಶವಾಗುತ್ತವೆ.",
            "ಹಳೆಯ ಬಿತ್ತನೆ ಮಡಿ ವಿಧಾನ: ಬಿತ್ತನೆಗೆ 10-15 ದಿನ ಮುನ್ನ ಲಘು ನೀರು ಕೊಟ್ಟು, ಹರಿಕೆ ಚಿಗುರಿದ ನಂತರ ಮೇಲ್ಮೈ ಕುಂಟೆ ಹೊಡೆದು ಬೇರುಗಳಲ್ಲಿನ ಪಿಷ್ಟದ ಶಕ್ತಿಯನ್ನು ಕುಗ್ಗಿಸಿ.",
            "ಹೂ ಬಿಡಲು ಬಿಡಬೇಡಿ: ನಿರಂತರವಾಗಿ 21 ದಿನಗಳ ಅಂತರದಲ್ಲಿ ಎಡೆಕುಂಟೆ ಓಡಿಸಿ ಮತ್ತು ಹೂ ಗೊಂಚಲು ಬರುವ ಮುನ್ನವೇ ಕಳೆ ಕೀಳಿ."
        ]
    },
    {
        "id": "cyperus",
        "name_en": "Purple Nutsedge / Nutgrass",
        "name_kn": "ಭದ್ರ ಮುಸ್ತೆ / ಕೊರೆ ಹುಲ್ಲು",
        "botanical": "Cyperus rotundus",
        "type": "Perennial Sedge (ಗಡ್ಡೆ ಕೊರೆ ಹುಲ್ಲು)",
        "damage_en": "Considered the world's worst agricultural weed. Produces extensive chains of underground tubers (ಗಡ್ಡೆಗಳು) that survive droughts and herbicides for years.",
        "damage_kn": "ಜಗತ್ತಿನ ಅತ್ಯಂತ ಹಠಮಾರಿ ಕಳೆ. ನೆಲದೊಳಗೆ ಸರಪಳಿಯಂತಹ ಕಪ್ಪು ಗಡ್ಡೆಗಳನ್ನು ರೂಪಿಸಿ ವರ್ಷಗಟ್ಟಲೆ ಬರಗಾಲ ಮತ್ತು ಕಳೆನಾಶಕಗಳನ್ನು ತಡೆದುಕೊಂಡು ಬೆಳೆಯುತ್ತದೆ. ತೇವಾಂಶ ಮತ್ತು ಗೊಬ್ಬರವನ್ನು ಲೂಟಿ ಮಾಡುತ್ತದೆ.",
        "tactics_en": [
            "Soil Solarization (ಮಣ್ಣಿನ ಸೌರ ತಾಪನ): Wet the soil in May, cover tightly with 25-50 micron clear transparent polythene sheet for 4-6 weeks. Kills up to 85% of tubers.",
            "Allelopathic Sorghum Rotation: Sorghum root exudates (sorgoleone) act as natural bio-herbicides that naturally suppress nutgrass tuber sprouting.",
            "Deep Summer Chisel Ploughing: Invert soil to 25-35 cm depth in summer so tuber chains detach and desiccate.",
            "Avoid Chopping with Rotavator: Never run a rotavator through heavily infested nutgrass, as blades slice single tubers into dozens of viable new plants!"
        ],
        "tactics_kn": [
            "ಮಣ್ಣಿನ ಸೌರ ತಾಪನ {Soil Solarization}: ಮೇ ತಿಂಗಳಲ್ಲಿ ಮಣ್ಣನ್ನು ನೆನೆಸಿ, 25-50 ಮೈಕ್ರಾನ್ ಪಾರದರ್ಶಕ ಬಿಳಿ ಪ್ಲಾಸ್ಟಿಕ್ ಶೀಟ್‌ನಿಂದ 4-6 ವಾರಗಳ ಕಾಲ ಬಿಗಿಯಾಗಿ ಮುಚ್ಚಿ. ಮಣ್ಣಿನ ತಾಪ 50°C ಏರಿ ಗಡ್ಡೆಗಳು ಸಾಯುತ್ತವೆ.",
            "ಜೋಳದ ಬೆಳೆ ಪರಿವರ್ತನೆ: ಜೋಳದ ಬೇರುಗಳಿಂದ ಬಿಡುಗಡೆಯಾಗುವ ಸೊರ್ಗೊಲಿಯೋನ್ {Sorgoleone} ಎಂಬ ನೈಸರ್ಗಿಕ ಜೈವಿಕ ರಾಸಾಯನಿಕವು ಭದ್ರ ಮುಸ್ತೆಯ ಗಡ್ಡೆಗಳು ಮೊಳಕೆಯೊಡೆಯುವುದನ್ನು ತಡೆಯುತ್ತದೆ.",
            "ಬೇಸಿಗೆಯ ಆಳವಾದ ನೇಗಿಲು ಉಳುಮೆ: ಗಡ್ಡೆಗಳು ಸೂರ್ಯನ ಸುಡುಬಿಸಿಲಿಗೆ ಒಣಗುವಂತೆ ಮೇಲಕ್ಕೆ ತಳ್ಳಿ.",
            "ರೊಟಾವೇಟರ್ ಬಳಸಬೇಡಿ: ಕೊರೆ ಹುಲ್ಲಿರುವ ಜಮೀನಿನಲ್ಲಿ ರೊಟಾವೇಟರ್ ಓಡಿಸಬೇಡಿ! ಬ್ಲೇಡ್‌ಗಳು ಒಂದೊಂದು ಗಡ್ಡೆಯನ್ನು ನೂರಾರು ತುಂಡುಗಳನ್ನಾಗಿ ಮಾಡಿ ಕಳೆಯನ್ನು ಇಡೀ ಜಮೀನಿಗೆ ಹರಡುತ್ತವೆ!"
        ]
    },
    {
        "id": "parthenium",
        "name_en": "Parthenium / Congress Grass",
        "name_kn": "ಕಾಂಗ್ರೆಸ್ ಗಿಡ / ಪಾರ್ಥೇನಿಯಂ",
        "botanical": "Parthenium hysterophorus",
        "type": "Invasive Annual Herb (ಆಕ್ರಮಣಕಾರಿ ಕಳೆ)",
        "damage_en": "Releases toxic parthenin chemicals that inhibit crop germination. Causes severe skin eczema, bronchitis, and milk tainting in cattle.",
        "damage_kn": "ಇದರ ಎಲೆ ಮತ್ತು ಪರಾಗದಲ್ಲಿರುವ ಪಾರ್ಥೆನಿನ್ {Parthenin} ವಿಷವು ಮುಖ್ಯ ಬೆಳೆಯ ಮೊಳಕೆಯನ್ನು ನಾಶಪಡಿಸುತ್ತದೆ. ಮನುಷ್ಯರಿಗೆ ಮತ್ತು ಜಾನುವಾರುಗಳಿಗೆ ತೀವ್ರ ಚರ್ಮದ ಅಲರ್ಜಿ, ತುರಿಕೆ ಮತ್ತು ಉಸಿರಾಟದ ತೊಂದರೆ ಉಂಟುಮಾಡುತ್ತದೆ.",
        "tactics_en": [
            "Pre-Flowering Manual Pulling: Uproot plants when soil is damp, before flower buds open. Always wear protective rubber gloves and full sleeves.",
            "Biological Competition: Broadcast seeds of Cassia sericea (ತಗಚೆ / ಚಾಗಚೆ ಬೀಜ) or Marigold (ಚೆಂಡು ಹೂ) on borders and wastelands to outcompete Parthenium.",
            "Mexican Beetle Bio-Control: Release Zygogramma bicolorata beetles during monsoon. They feed voraciously on parthenium leaves without harming crops.",
            "Hot Composting: Never put mature parthenium into cool heaps; only add pre-flowering young plants to rapid hot compost pits exceeding 55°C."
        ],
        "tactics_kn": [
            "ಹೂ ಬಿಡುವ ಮುನ್ನವೇ ಕೀಳುವುದು: ಮಣ್ಣು ತೇವವಾಗಿದ್ದಾಗ ಹೂ ಮೊಗ್ಗು ಬಿಡುವ ಮುನ್ನವೇ ಕೈಗವಸು {Gloves} ಧರಿಸಿ ಬೇರುಸಹಿತ ಕಿತ್ತು ಹಾಕಿ.",
            "ಜೈವಿಕ ಸ್ಪರ್ಧಾತ್ಮಕ ಗಿಡಗಳು: ಜಮೀನಿನ ಬದುಗಳಲ್ಲಿ ಮತ್ತು ಪಾಳು ಬಿದ್ದ ಜಾಗದಲ್ಲಿ ತಗಚೆ {Cassia sericea} ಅಥವಾ ಚೆಂಡು ಹೂವಿನ ಬೀಜ ಬಿತ್ತಿ. ಇವು ಕಾಂಗ್ರೆಸ್ ಗಿಡ ಬೆಳೆಯುವುದನ್ನು ನೈಸರ್ಗಿಕವಾಗಿ ತಡೆಯುತ್ತವೆ.",
            "ಮೆಕ್ಸಿಕನ್ ಜೀರುಂಡೆ {Zygogramma beetle}: ಮುಂಗಾರು ಆರಂಭದಲ್ಲಿ ಜೈವಿಕ ನಿಯಂತ್ರಣಕ್ಕೆ ಈ ಜೀರುಂಡೆಗಳನ್ನು ಬಿಟ್ಟರೆ ಕಾಂಗ್ರೆಸ್ ಗಿಡದ ಎಲೆಗಳನ್ನು ತಿಂದು ನಾಶಪಡಿಸುತ್ತವೆ.",
            "ಬಿಸಿ ಕಾಂಪೋಸ್ಟ್ ಎಚ್ಚರಿಕೆ: ಹೂ ಬಿಟ್ಟ ಕಾಂಗ್ರೆಸ್ ಗಿಡವನ್ನು ಕಾಂಪೋಸ್ಟ್‌ಗೆ ಹಾಕಬೇಡಿ; ಹೂ ಬಿಡುವ ಮುಂಚಿನ ಎಳೆಯ ಗಿಡಗಳನ್ನು ಮಾತ್ರ ಬಿಸಿ ಕಾಂಪೋಸ್ಟ್ ಗುಂಡಿಗೆ ಸೇರಿಸಿ."
        ]
    },
    {
        "id": "amaranthus",
        "name_en": "Spiny Amaranth / Thorny Pigweed",
        "name_kn": "ಮುಳ್ಳು ದಂಟು / ಕಾಡು ಅಮರಾಂತ್",
        "botanical": "Amaranthus spinosus",
        "type": "Annual Broadleaf Weed (ಮುಳ್ಳಿನ ಅಗಲ ಎಲೆ ಕಳೆ)",
        "damage_en": "Single plant produces over 100,000 tiny seeds. Sharp thorns injure grazing cattle and manual harvest labor; robs heavy amounts of soil potash and nitrogen.",
        "damage_kn": "ಒಂದೇ ಗಿಡವು 1 ಲಕ್ಷಕ್ಕೂ ಅಧಿಕ ಬೀಜಗಳನ್ನು ಉತ್ಪಾದಿಸುತ್ತದೆ. ಚೂಪಾದ ಮುಳ್ಳುಗಳಿಂದ ಕೂಡಿ ಕೊಯ್ಲು ಮಾಡುವ ಕೃಷಿ ಕಾರ್ಮಿಕರಿಗೆ ಮತ್ತು ದನ-ಕರುಗಳಿಗೆ ಗಾಯ ಮಾಡುತ್ತದೆ. ಮಣ್ಣಿನ ಪೊಟ್ಯಾಷ್ ಮತ್ತು ಸಾರಜನಕವನ್ನು ಅಪಾರ ಪ್ರಮಾಣದಲ್ಲಿ ನುಂಗಿಹಾಕುತ್ತದೆ.",
        "tactics_en": [
            "Stale Seedbed Method: Prepare seedbed, irrigate lightly to trigger flushes of amaranth germination, then kill with shallow blade harrow before main sowing.",
            "Organic Mulching: Spread 8-10 cm layer of dry crop residue (paddy straw / bagasse) to block sunlight and prevent tiny seeds from germinating.",
            "Intercropping: Intercrop pigeon pea (ತೊಗರಿ) with groundnut (ಕಡಲೆಕಾಯಿ) or cowpea to cover the soil inter-rows tightly.",
            "Zero Tolerance Before Seed-Set: Pull weeds while tender before black seeds mature and fall onto soil."
        ],
        "tactics_kn": [
            "ಹಳೆಯ ಬಿತ್ತನೆ ಮಡಿ ವಿಧಾನ {Stale Seedbed}: ಬಿತ್ತನೆಗೆ ಮುಂಚೆ ನೀರು ಹಾಯಿಸಿ, ಮುಳ್ಳು ದಂಟಿನ ಬೀಜಗಳು ಮೊಳಕೆಯೊಡೆದ ತಕ್ಷಣ ಮೇಲ್ಮೈ ಕುಂಟೆ ಹೊಡೆದು ನಾಶಮಾಡಿ ಮುಖ್ಯ ಬೆಳೆ ಬಿತ್ತಿ.",
            "ಸಾವಯವ ಹೊದಿಕೆ {Mulching}: 8-10 ಸೆಂ.ಮೀ. ಭತ್ತದ ಒಣ ಹುಲ್ಲು ಅಥವಾ ಕಬ್ಬಿನ ರವದಿಯನ್ನು ಹೊದಿಸುವುದರಿಂದ ಸೂರ್ಯನ ಬೆಳಕು ಸಿಗದೆ ಸಣ್ಣ ಬೀಜಗಳು ಮೊಳಕೆಯೊಡೆಯುವುದಿಲ್ಲ.",
            "ಸಾಲುಗಳ ನಡುವೆ ಸಹಬೆಳೆ: ತೊಗರಿ, ಕಡಲೆಕಾಯಿ ಅಥವಾ ಅಲಸಂದೆ ಬೆಳೆದು ಜಮೀನಿನ ನೆಲವನ್ನು ಸಂಪೂರ್ಣವಾಗಿ ಮುಚ್ಚಿ.",
            "ಬೀಜ ಕಟ್ಟುವ ಮುನ್ನವೇ ಕಿತ್ತುಹಾಕಿ: ಕಪ್ಪು ಬೀಜಗಳು ಮಣ್ಣಿಗೆ ಉದುರುವ ಮುನ್ನವೇ ಸಣ್ಣ ಗಿಡಗಳಿರುವಾಗಲೇ ಕೀಳಿ."
        ]
    },
    {
        "id": "commelina",
        "name_en": "Tropical Spiderwort / Dayflower",
        "name_kn": "ಒಂಟೆ ಹುಲ್ಲು / ಕಮ್ಯೂನಿಸ್ / ನೀರೊತ್ತಿ",
        "botanical": "Commelina benghalensis",
        "type": "Creeping Herb (ನೆಲತೆವಳು ಕಳೆ)",
        "damage_en": "Creeping stems root at every node. Unique ability to produce both aerial flowers and underground subterranean self-pollinating seeds that evade surface tillage.",
        "damage_kn": "ನೆಲದ ಮೇಲೆ ತೆವಳುತ್ತಾ ಪ್ರತಿ ಗೆಣ್ಣಿನಲ್ಲೂ ಹೊಸ ಬೇರುಗಳನ್ನು ಬಿಡುತ್ತದೆ. ಇದು ನೆಲದ ಮೇಲೂ ಹೂ ಬಿಡುತ್ತದೆ ಮತ್ತು ಮಣ್ಣಿನೊಳಗೂ ಗುಪ್ತ ಬೀಜಗಳನ್ನು ಉತ್ಪಾದಿಸುವ ವಿಶಿಷ್ಟ ಸ್ವಭಾವ ಹೊಂದಿದ್ದು ಬೇಗ ನಾಶವಾಗುವುದಿಲ್ಲ.",
        "tactics_en": [
            "Dry Weather Manual Desiccation: Hand-weed during hot dry sunshine days. If uprooted on wet rainy soil, broken stem pieces quickly re-root!",
            "Avoid High Moisture Stagnation: Improve drainage channels; commelina thrives aggressively in soggy waterlogged furrows.",
            "Deep Inversion: Deep mouldboard ploughing buries underground seed capsules deep beneath the emergence zone.",
            "Aggressive Cover Cropping: Fast-growing green manure crops (ಧೈಂಚಾ / ಸಣಬು) smother creeping stems effectively."
        ],
        "tactics_kn": [
            "ಬಿಸಿಲಿನಲ್ಲಿ ಕಿತ್ತು ಒಣಗಿಸಿ: ಒಣ ಬಿಸಿಲಿನ ದಿನಗಳಲ್ಲಿ ಮಾತ್ರ ಕೈಯಿಂದ ಕಳೆ ಕೀಳಿ. ತೇವವಾದ ಮಣ್ಣಿನಲ್ಲಿ ಕಿತ್ತರೆ ಮುರಿದ ಸಣ್ಣ ತುಂಡುಗಳು ಸಹ ಮತ್ತೆ ಬೇರೂರಿ ಬೆಳೆಯುತ್ತವೆ!",
            "ಜಮೀನಿನಲ್ಲಿ ನೀರು ನಿಲ್ಲದಂತೆ ನೋಡಿಕೊಳ್ಳಿ: ಕಮ್ಯೂನಿಸ್ ಕಳೆಯು ನಿಂತ ನೀರಿನ ತೇವಾಂಶದಲ್ಲಿ ಅತಿ ವೇಗವಾಗಿ ಹರಡುತ್ತದೆ.",
            "ಆಳವಾದ ನೇಗಿಲು ಉಳುಮೆ: ಮಣ್ಣಿನೊಳಗಿನ ಗುಪ್ತ ಬೀಜಕೋಶಗಳು ಆಳಕ್ಕೆ ಹೋಗುವಂತೆ ಮಗುಚಿ ಹಾಕಿ.",
            "ಧೈಂಚಾ ಅಥವಾ ಸಣಬಿನ ದಟ್ಟ ಬೆಳೆ: ಎತ್ತರಕ್ಕೆ ಬೆಳೆಯುವ ಹಸಿರೆಲೆ ಗೊಬ್ಬರದ ಬೆಳೆಗಳನ್ನು ಬೆಳೆದು ಇದರ ಹರಡುವಿಕೆಯನ್ನು ತಡೆಯಿರಿ."
        ]
    },
    {
        "id": "echinochloa",
        "category": "grass",
        "name_en": "Barnyard Grass / Jungle Rice",
        "name_kn": "ಜಂಗಲಿ ಭತ್ತ / ಊದಲು ಕಳೆ ಹುಲ್ಲು",
        "botanical": "Echinochloa colona / crus-galli",
        "type": "Annual Grass Weed (ವಾರ್ಷಿಕ ಹುಲ್ಲು ಕಳೆ)",
        "damage_en": "Mimics paddy seedlings closely in nursery and early tillering stage. Can deplete 60-80% of applied nitrogen fertilizer and reduce paddy yields by up to 50% if unweeded.",
        "damage_kn": "ಭತ್ತದ ಪೈರಿನಂತೆಯೇ ಕಾಣುವ ಕಪಟ ಕಳೆ. ಸಸಿಮಡಿ ಮತ್ತು ಮೊದಲ 30 ದಿನಗಳಲ್ಲಿ ಭತ್ತದಂತೆಯೇ ಬೆಳೆದು ರೈತರಿಗೆ ಮೋಸ ಮಾಡುತ್ತದೆ. ಬೆಳೆಗೆ ಹಾಕಿದ 60-80% ಸಾರಜನಕ ಗೊಬ್ಬರವನ್ನು ನುಂಗಿ ಭತ್ತದ ಇಳುವರಿಯನ್ನು 50% ರಷ್ಟು ಕುಗ್ಗಿಸುತ್ತದೆ.",
        "tactics_en": [
            "Continuous Water Ponding: Maintain 5 cm continuous standing water depth in transplanted paddy fields during the first 2-3 weeks; barnyard grass seeds cannot germinate under submergence.",
            "Stale Seedbed in Lowland: Pre-irrigate 12-15 days before final puddle, allow barnyard grass flush to emerge, then destroy completely with rotary tiller or power tiller.",
            "Cono-Weeder Operation: Run mechanical cono-weeder (ಕನೋ ವೀಡರ್) twice at 15 and 30 days after transplanting in line-planted SRI paddy to incorporate weeds into mud as green manure.",
            "Azolla Bio-Cover: Dual-crop Azolla pinnata (400 kg/acre) which multiplies to cover water surface in 10 days, cutting off sunlight and suppressing weed emergence by 70%."
        ],
        "tactics_kn": [
            "ನಿರಂತರ ನೀರಿನ ಮಟ್ಟ ನಿರ್ವಹಣೆ: ನಾಟಿ ಮಾಡಿದ ಮೊದಲ 15-20 ದಿನಗಳ ಕಾಲ ಗದ್ದೆಯಲ್ಲಿ ನಿರಂತರ 5 ಸೆಂ.ಮೀ. ನೀರು ನಿಲ್ಲಿಸಿ. ನೀರಿನೊಳಗೆ ಮುಳುಗಿದಾಗ ಜಂಗಲಿ ಭತ್ತದ ಬೀಜಗಳು ಮೊಳಕೆಯೊಡೆಯುವುದಿಲ್ಲ.",
            "ಹಳೆಯ ಬಿತ್ತನೆ ಮಡಿ ವಿಧಾನ {Stale Seedbed}: ಗದ್ದೆ ಸಿದ್ಧತೆಗೆ 12-15 ದಿನ ಮುನ್ನ ನೀರು ಕೊಟ್ಟು ಜಂಗಲಿ ಭತ್ತ ಮೊಳಕೆಯೊಡೆದ ತಕ್ಷಣ ಪವರ್ ಟಿಲ್ಲರ್‌ನಿಂದ ಕೆಸರು ಮಾಡಿ ಹೂತುಹಾಕಿ.",
            "ಕೋನೋ ವೀಡರ್ ಯಂತ್ರ ಬಳಕೆ: ಸಾಲು ನಾಟಿ ಮಾಡಿದ ಗದ್ದೆಯಲ್ಲಿ ನಾಟಿ ಮಾಡಿದ 15 ಮತ್ತು 30ನೇ ದಿನಕ್ಕೆ ಕೋನೋ ವೀಡರ್ {Cono-weeder} ಓಡಿಸಿ ಕಳೆಯನ್ನು ಕೆಸರಿನೊಳಗೆ ಅದುಮಿ ಹಸಿರೆಲೆ ಗೊಬ್ಬರವಾಗಿಸಿ.",
            "ಅಜೋಲ್ಲಾ ಜೈವಿಕ ಹೊದಿಕೆ {Azolla}: ಗದ್ದೆಯಲ್ಲಿ ಎಕರೆಗೆ 400 ಕೆಜಿ ಅಜೋಲ್ಲಾ ಬಿಟ್ಟರೆ 10 ದಿನಗಳಲ್ಲಿ ಇಡೀ ನೀರನ್ನು ಹಸಿರಾಗಿ ಆವರಿಸಿ ಸೂರ್ಯನ ಬೆಳಕು ತಡೆದು ಕಳೆ ಬೆಳೆಯುವುದನ್ನು 70% ತಡೆಯುತ್ತದೆ."
        ]
    },
    {
        "id": "orobanche",
        "category": "parasitic",
        "name_en": "Broomrape / Root Parasite",
        "name_kn": "ಬೆಂಕಿ ಕಳೆ / ವ್ಯಾಘ್ರನಖಿ / ಹೊಗೆಸೊಪ್ಪಿನ ಮೂಲ ಪರಾವಲಂಬಿ",
        "botanical": "Orobanche cernua / ramosa",
        "type": "Holoparasitic Root Weed (ಮೂಲ ಪರಾವಲಂಬಿ ಬೆಂಕಿ ಕಳೆ)",
        "damage_en": "Lacks chlorophyll; produces underground haustoria that tap directly into root vascular bundles of tobacco, tomato, brinjal, potato, and mustard. Causes severe wilting, stunting, and 40-70% crop collapse.",
        "damage_kn": "ಹರಿತ್ತು ಇಲ್ಲದ ಸಂಪೂರ್ಣ ಪರಾವಲಂಬಿ ಕಳೆ. ಹೊಗೆಸೊಪ್ಪು, ಟೊಮೆಟೊ, ಬದನೆ, ಆಲೂಗಡ್ಡೆ ಮತ್ತು ಸಾಸಿವೆ ಗಿಡಗಳ ಬೇರುಗಳಿಗೆ ಅಂಟಿಕೊಂಡು ಆಹಾರ ಮತ್ತು ನೀರನ್ನು ಹೀರುತ್ತದೆ. ಗಿಡಗಳು ಬೆಂಕಿಯಲ್ಲಿ ಸುಟ್ಟಂತೆ ಒಣಗುವುದರಿಂದ ಇದನ್ನು ಬೆಂಕಿ ಕಳೆ ಎನ್ನುತ್ತಾರೆ.",
        "tactics_en": [
            "Trap & Catch Cropping (ಆತ್ಮಹತ್ಯಾ ಮೊಳಕೆ): Rotate with false hosts like sorghum (ಜೋಳ), sunn hemp (ಸಣಬು), or cotton. Their root exudates trigger Orobanche seed germination, but cannot be infected, causing seeds to die suicidal deaths.",
            "Pre-Flowering Manual Rogueing: Walk infested plots weekly and pull out emergent Orobanche spikes before violet flowers open and release millions of microscopic dust seeds.",
            "Soil Solarization: Cover moist bed with 50-micron transparent plastic for 40 days in peak summer (April-May) to thermally kill dormant underground seed banks.",
            "Deep Trench Inversion Ploughing: Use mouldboard plough to bury dust seeds below 20 cm depth where germination stimulants cannot trigger emergence."
        ],
        "tactics_kn": [
            "ಆತ್ಮಹತ್ಯಾ ಮೊಳಕೆ ಬೆಳೆ ಪರಿವರ್ತನೆ {Trap Cropping}: ಮುಖ್ಯ ಬೆಳೆಗೂ ಮುನ್ನ ಸಣಬು ಅಥವಾ ಜೋಳ ಬೆಳೆಯಿರಿ. ಇವುಗಳ ಬೇರಿನ ಸ್ರಾವವು ಬೆಂಕಿ ಕಳೆಯ ಬೀಜ ಮೊಳಕೆಯೊಡೆಯುವಂತೆ ಪ್ರೇರೇಪಿಸುತ್ತದೆ, ಆದರೆ ಕಳೆಗೆ ಆಶ್ರಯ ಸಿಗದೆ ಮೊಳಕೆಯೊಡೆದ ತಕ್ಷಣ ತಾನಾಗಿಯೇ ಸಾಯುತ್ತದೆ.",
            "ಹೂ ಬಿಡುವ ಮುನ್ನವೇ ಕೈಯಿಂದ ಕೀಳುವಿಕೆ: ನೇರಳೆ ಹೂ ಬಿಟ್ಟು ಲಕ್ಷಾಂತರ ಸೂಕ್ಷ್ಮ ಧೂಳಿನಂತಹ ಬೀಜಗಳು ಮಣ್ಣಿಗೆ ಬೀಳುವ ಮುನ್ನವೇ ಹೊರಬಂದ ಗಿಡಗಳನ್ನು ಬುಡಸಹಿತ ಕಿತ್ತು ಸುಟ್ಟುಹಾಕಿ.",
            "ಬೇಸಿಗೆ ಮಣ್ಣಿನ ಸೌರ ತಾಪನ {Solarization}: ಏಪ್ರಿಲ್-ಮೇ ತಿಂಗಳಲ್ಲಿ ಮಣ್ಣನ್ನು ನೆನೆಸಿ 50 ಮೈಕ್ರಾನ್ ಪಾರದರ್ಶಕ ಬಿಳಿ ಪ್ಲಾಸ್ಟಿಕ್ ಶೀಟ್ ಹೊದಿಸಿ 40 ದಿನ ಬಿಡಿ; ಬಿಸಿಯ ತಾಪಕ್ಕೆ ಬೀಜಗಳು ನಾಶವಾಗುತ್ತವೆ.",
            "ಆಳವಾದ ನೇಗಿಲು ಉಳುಮೆ: ಮಣ್ಣನ್ನು ಆಳವಾಗಿ ತಿರುವಿ ಬೀಜಗಳು 20 ಸೆಂ.ಮೀ.ಗಿಂತ ಆಳಕ್ಕೆ ಹೋಗುವಂತೆ ಮಾಡಿ."
        ]
    },
    {
        "id": "cuscuta",
        "category": "parasitic",
        "name_en": "Dodder / Golden Thread",
        "name_kn": "ಬಂಗಾರದ ಬಳ್ಳಿ / ಅಮರವೇಲು / ಆಕಾಶಬಳ್ಳಿ",
        "botanical": "Cuscuta reflexa / campestris",
        "type": "Stem Parasite (ಕಾಂಡ ಪರಾವಲಂಬಿ ಬಳ್ಳಿ)",
        "damage_en": "Leafless parasitic golden-yellow twine with no roots. Pierces crop stems with haustorial suckers, choking pulses (blackgram, greengram), niger, lucerne, onion, and chilli, causing complete field devastation.",
        "damage_kn": "ಬೇರು ಮತ್ತು ಎಲೆಗಳಿಲ್ಲದ ಚಿನ್ನದ ಬಣ್ಣದ ದಾರದಂತಹ ಪರಾವಲಂಬಿ ಬಳ್ಳಿ. ಉದ್ದು, ಹೆಸರು, ಹುಚ್ಚೆಳ್ಳು, ಕುದುರೆಮೆಂತೆ, ಈರುಳ್ಳಿ ಮತ್ತು ಮೆಣಸಿನಕಾಯಿ ಗಿಡಗಳ ಕಾಂಡಕ್ಕೆ ಹೀರೊರಳುಗಳನ್ನು ಚುಚ್ಚಿ ರಸಹೀರಿ ಇಡೀ ಜಮೀನನ್ನೇ ಬಲೆ ಬೀಸಿ ನಾಶಮಾಡುತ್ತದೆ.",
        "tactics_en": [
            "Brine Water Seed Cleaning: Float crop seed lot in 10% saltwater (brine) solution. Dense crop seeds sink to bottom while lighter dodder seeds float up and can be skimmed off completely.",
            "Spot Rogueing & Safe In-Situ Incineration: Immediately upon first sight, cut affected host plant parts along with the dodder twine, seal in sack, and burn completely off-field before seed capsules ripen.",
            "Resistant Crop Rotation: Rotate heavily infested plots with non-host cereals or grasses (maize, pearl millet, ragi, sorghum) for 2 seasons; dodder haustoria cannot penetrate monocot fibrous stems.",
            "Neem & Castor Cake Soil Application: Apply 250 kg/acre neem or castor cake during final land preparation; phenolic extracts significantly reduce dodder seedling attachment."
        ],
        "tactics_kn": [
            "ಉಪ್ಪು ನೀರಿನಲ್ಲಿ ಬೀಜ ಶುದ್ಧೀಕರಣ: ಬಿತ್ತನೆ ಬೀಜಗಳನ್ನು 10% ಉಪ್ಪಿನ ನೀರಿನಲ್ಲಿ ಹಾಕಿ ಕಲಕಿ. ಭಾರವಾದ ಮುಖ್ಯ ಬೆಳೆ ಬೀಜಗಳು ಕೆಳಗೆ ಕುಳಿತುಕೊಳ್ಳುತ್ತವೆ, ಹಗುರವಾದ ಬಂಗಾರದ ಬಳ್ಳಿಯ ಬೀಜಗಳು ತೇಲುತ್ತವೆ; ತೇಲುವ ಕಳೆ ಬೀಜಗಳನ್ನು ಜರಡಿಯಿಂದ ಬೇರ್ಪಡಿಸಿ.",
            "ಸ್ಪಾಟ್ ನಿರ್ಮೂಲನೆ ಮತ್ತು ಸುಡುವುದು: ಜಮೀನಿನಲ್ಲಿ ಕಂಡ ತಕ್ಷಣ ಬಳ್ಳಿ ಸುತ್ತಿಕೊಂಡ ಗಿಡವನ್ನು ಬುಡಸಹಿತ ಕತ್ತರಿಸಿ ಚೀಲದಲ್ಲಿ ತುಂಬಿ ಜಮೀನಿನಿಂದ ಆಚೆ ತಂದು ಸುಟ್ಟುಹಾಕಿ; ಯಾವುದೇ ತುಂಡು ಮಣ್ಣಿಗೆ ಬೀಳದಂತೆ ನೋಡಿಕೊಳ್ಳಿ.",
            "ಏಕದಳ ಧಾನ್ಯಗಳ ಬೆಳೆ ಪರಿವರ್ತನೆ: ಕಳೆ ಬಾಧಿತ ಜಮೀನಿನಲ್ಲಿ 2 ಋತುಗಳ ಕಾಲ ಜೋಳ, ರಾಗಿ, ಸಜ್ಜೆ ಅಥವಾ ಮೆಕ್ಕೆಜೋಳ ಬೆಳೆಯಿರಿ; ಬಂಗಾರದ ಬಳ್ಳಿಯು ಏಕದಳ ಹುಲ್ಲಿನ ಕಾಂಡವನ್ನು ಭೇದಿಸಲು ಸಾಧ್ಯವಿಲ್ಲದೆ ಸಾಯುತ್ತದೆ.",
            "ಬೇವಿನ ಹಿಂಡಿ ಬಳಕೆ: ಎಕರೆಗೆ 200-250 ಕೆಜಿ ಬೇವಿನ ಹಿಂಡಿ ಅಥವಾ ಹರಳೆಣ್ಣೆ ಹಿಂಡಿಯನ್ನು ಕೊನೆಯ ಉಳುಮೆಯಲ್ಲಿ ಮಣ್ಣಿಗೆ ಸೇರಿಸಿ."
        ]
    },
    {
        "id": "striga",
        "category": "parasitic",
        "name_en": "Witchweed / Fireweed",
        "name_kn": "ವಿಚ್ ಕಳೆ / ಬೆಂಕಿ ಹುಲ್ಲು / ಸಿಡುಬು ಕಳೆ",
        "botanical": "Striga asiatica / lutea",
        "type": "Root Semi-Parasite (ಬೇರು ಅರೆ-ಪರಾವಲಂಬಿ ಕಳೆ)",
        "damage_en": "Attaches to cereal root systems (sorghum, maize, pearl millet, sugarcane). Secretes phytotoxins that mimic acute drought stress and stunt crop growth, causing plants to wither as if scorched by fire.",
        "damage_kn": "ಜೋಳ, ಮೆಕ್ಕೆಜೋಳ, ಸಜ್ಜೆ ಮತ್ತು ಕಬ್ಬಿನ ಬೇರುಗಳಿಗೆ ಅಂಟಿಕೊಳ್ಳುವ ಅಪಾಯಕಾರಿ ಕಳೆ. ಇದು ಬೆಳೆಯ ಬೇರಿನಿಂದ ನೀರು-ಪೋಷಕಾಂಶ ಕದಿಯುವುದಲ್ಲದೆ ವಿಷಕಾರಿ ದ್ರವ ಬಿಡುಗಡೆ ಮಾಡಿ ಗಿಡಗಳು ಬೆಂಕಿಯಲ್ಲಿ ಸುಟ್ಟಂತೆ ಒಣಗುತ್ತವೆ. ಬರಗಾಲದಂತೆ ಬೆಳೆ ಮುದುಡುತ್ತದೆ.",
        "tactics_en": [
            "Intercropping Legumes (Allelopathic Cover): Intercrop sorghum/maize with cowpea or desmodium in 1:1 or 2:1 ratio. Legume root volatiles suppress Striga seed germination and haustorial attachment.",
            "High Organic Nitrogen Enrichment: Apply 5 tonnes/acre well-decomposed FYM or 1.5 tonnes vermicompost. Striga only infects nutrient-depleted soils; abundant organic soil nitrogen shuts down Striga stimulant receptors.",
            "False-Host Legume Rotation: Rotate fields with cotton, groundnut, or sunflower which induce suicidal Striga germination without allowing attachment.",
            "Early Hand-Pulling Before Pink/Yellow Blooms: Uproot emergent shoots by hand as soon as visible above soil, before flowers bloom and each plant sheds 50,000 viable seeds."
        ],
        "tactics_kn": [
            "ದ್ವಿದಳ ಸಹಬೆಳೆ {Intercropping}: ಜೋಳ ಅಥವಾ ಮುಸುಕಿನ ಜೋಳದ ಜೊತೆಗೆ ಸಾಲಿನಲ್ಲಿ ಅಲಸಂದೆ {Cowpea} ಅಥವಾ ಹುರುಳಿ ಬೆಳೆಯಿರಿ. ಇವುಗಳ ಬೇರುಗಳು ವಿಚ್ ಕಳೆ ಮೊಳಕೆಯೊಡೆಯುವುದನ್ನು ನೈಸರ್ಗಿಕವಾಗಿ ತಡೆಯುತ್ತವೆ.",
            "ಸಾವಯವ ಸಾರಜನಕ ಮತ್ತು ಕೊಟ್ಟಿಗೆ ಗೊಬ್ಬರ: ಎಕರೆಗೆ 4-5 ಟನ್ ಕೊಟ್ಟಿಗೆ ಗೊಬ್ಬರ ಅಥವಾ 1.5 ಟನ್ ಎರೆಹುಳು ಗೊಬ್ಬರ ಹಾಕಿ. ಫಲವತ್ತಾದ ಮಣ್ಣಿನಲ್ಲಿ ಬೆಂಕಿ ಹುಲ್ಲಿನ ಸೋಂಕು ತಗಲುವುದಿಲ್ಲ; ಕೇವಲ ಸಾರಜನಕ ಕೊರತೆಯಿರುವ ಬಂಜರು ಮಣ್ಣಿನಲ್ಲಿ ಮಾತ್ರ ಇದು ವಿಪರೀತವಾಗುತ್ತದೆ.",
            "ಸುಳ್ಳು ಆಶ್ರಯ ಬೆಳೆ ಪರಿವರ್ತನೆ {False Hosts}: ಹತ್ತಿ, ಕಡಲೆಕಾಯಿ ಅಥವಾ ಸೂರ್ಯಕಾಂತಿ ಬೆಳೆ ಪರಿವರ್ತನೆ ಮಾಡಿ; ಇವು ಕಳೆಯ ಬೀಜ ಮೊಳಕೆಯೊಡೆದು ಆಶ್ರಯ ಸಿಗದೆ ಸಾಯುವಂತೆ ಮಾಡುತ್ತವೆ.",
            "ಹೂ ಬಿಡುವ ಮುನ್ನವೇ ಕೀಳುವಿಕೆ: ನೆಲದಿಂದ ಮೇಲೆ ಬಂದ ತಕ್ಷಣ ಗುಲಾಬಿ/ಹಳದಿ ಹೂ ಬಿಡುವ ಮುಂಚೆಯೇ ಕೈಯಿಂದ ಕಿತ್ತು ಸುಟ್ಟುಹಾಕಿ."
        ]
    },
    {
        "id": "eichhornia",
        "category": "aquatic_invasive",
        "name_en": "Water Hyacinth / River Devil",
        "name_kn": "ಜಲಕಳೆ / ಆನೆ ಗಿಡ / ಕೆರೆ ಕಳೆ / ನೀರು ಕಳೆ",
        "botanical": "Eichhornia crassipes",
        "type": "Free-Floating Aquatic Macrophyte (ತೇಲುವ ಜಲಕಳೆ)",
        "damage_en": "Aggressively chokes farm irrigation ponds, river barrages, open wells, and canal gates. Doubles biomass every 10 days, transpiring water at 3x normal lake evaporation rate and choking fish.",
        "damage_kn": "ರೈತರ ಕೃಷಿ ಹೊಂಡ, ನೀರಾವರಿ ಕಾಲುವೆ, ಕೆರೆಗಳು ಮತ್ತು ಬೋರ್‌ವೆಲ್ ಮರುಪೂರಣ ಹಳ್ಳಗಳನ್ನು ಸಂಪೂರ್ಣವಾಗಿ ಆವರಿಸುತ್ತದೆ. ಪ್ರತಿ 10 ದಿನಕ್ಕೆ ದುಪ್ಪಟ್ಟಾಗಿ ಬೆಳೆದು ಅಪಾರ ನೀರನ್ನು ಬಾಷ್ಪೀಕರಣ ಮಾಡಿ ಬತ್ತಿಸುತ್ತದೆ ಮತ್ತು ನೀರು ಕಲುಷಿತಗೊಳಿಸುತ್ತದೆ.",
        "tactics_en": [
            "Pre-Monsoon Manual Barrier Dragging: Erect wire mesh fences at farm pond inlets; drag out floating mats with bamboo booms during low-water summer months onto dry bunds.",
            "High-Value Potash Aerobic Composting: Mix harvested green water hyacinth with 20% cow dung and dry paddy straw in aerobic windrows; produces exceptional potassium-rich organic manure within 45 days.",
            "Biological Weevil Release: Release Neochetina weevils (Neochetina eichhorniae & N. bruchi) supplied by ICAR-DWR; weevils feed exclusively on water hyacinth petiole crowns without touching crops.",
            "Drying as Orchard Mulch: Spread air-dried water hyacinth biomass as a 10 cm moisture-retentive organic mulch ring around coconut, arecanut, and fruit trees."
        ],
        "tactics_kn": [
            "ಬೇಸಿಗೆಯಲ್ಲಿ ಜಾಲರಿಯಿಂದ ಎಳೆದು ಹೊರಹಾಕುವುದು: ಕೃಷಿ ಹೊಂಡ ಮತ್ತು ಕಾಲುವೆಗಳ ಮುಖದ್ವಾರದಲ್ಲಿ ಬಿದಿರಿನ ಬೊಂಬು ಅಥವಾ ತಂತಿ ಜಾಲರಿ ಕಟ್ಟಿ, ಬೇಸಿಗೆಯಲ್ಲಿ ನೀರು ಕಡಿಮೆಯಿದ್ದಾಗ ಹಗ್ಗದಿಂದ ದಡಕ್ಕೆ ಎಳೆದು ಒಣಗಿಸಿ.",
            "ಪೊಟ್ಯಾಷ್ ಸಮೃದ್ಧ ಕಾಂಪೋಸ್ಟ್ ತಯಾರಿಕೆ: ಹೊರತೆಗೆದ ಜಲಕಳೆಯನ್ನು ಹಸುವಿನ ಸಗಣಿ ಮತ್ತು ಒಣ ಹುಲ್ಲಿನ ಜೊತೆ ಬೆರೆಸಿ ಕಾಂಪೋಸ್ಟ್ ಮಾಡಿ; ಇದು ತೋಟಗಾರಿಕಾ ಬೆಳೆಗಳಿಗೆ ಅತ್ಯುತ್ತಮ ನೈಸರ್ಗಿಕ ಪೊಟ್ಯಾಷ್ ಗೊಬ್ಬರವಾಗುತ್ತದೆ.",
            "ಮೆಕ್ಸಿಕನ್ ಜಲಕಳೆ ಜೀರುಂಡೆ {Neochetina weevils}: ಕೃಷಿ ವಿಶ್ವವಿದ್ಯಾಲಯಗಳಿಂದ ಲಭ್ಯವಿರುವ ನಿಯೋಚೆಟಿನಾ ಜೀರುಂಡೆಗಳನ್ನು ಕೆರೆಗಳಿಗೆ ಬಿಟ್ಟರೆ ಅವು ಕಳೆಯ ಗಿಣ್ಣುಗಳನ್ನು ತಿಂದು ನೈಸರ್ಗಿಕವಾಗಿ ಒಣಗಿಸುತ್ತವೆ.",
            "ತೆಂಗು-ಅಡಿಕೆ ತೋಟಕ್ಕೆ ಹೊದಿಕೆ: ಒಣಗಿದ ಜಲಕಳೆಯನ್ನು ತೆಂಗು ಮತ್ತು ಅಡಿಕೆ ಮರಗಳ ಬುಡದಲ್ಲಿ 4 ಇಂಚು ದಪ್ಪಗೆ ಹೊದಿಕೆಯಾಗಿ {Mulching} ಹರಡಿ ತೇವಾಂಶ ಕಾಪಾಡಿ."
        ]
    },
    {
        "id": "lantana",
        "category": "aquatic_invasive",
        "name_en": "Wild Sage / Lantana Camara",
        "name_kn": "ಉನ್ನಿ ಗಿಡ / ಲಾಂತನಾ ಪೊದೆ / ಕಾಡು ಮುಳ್ಳು ಪೊದೆ",
        "botanical": "Lantana camara",
        "type": "Perennial Woody Invasive Shrub (ದೀರ್ಘಾವಧಿ ಮುಳ್ಳಿನ ಪೊದೆ)",
        "damage_en": "Forms impenetrable dense thickets overtaking farm bunds, agroforestry borders, and pastures. Leaves contain hepatotoxins that cause severe photosensitization and liver failure in cattle.",
        "damage_kn": "ಜಮೀನಿನ ಬದುಗಳು, ಪಾಳು ಬಿದ್ದ ಜಾಗ ಮತ್ತು ಮೇವಿನ ಹುಲ್ಲುಗಾವಲುಗಳನ್ನು ಆಕ್ರಮಿಸುವ ದಟ್ಟ ಮುಳ್ಳಿನ ಪೊದೆ. ಇದರ ಎಲೆಗಳಲ್ಲಿರುವ ಲ್ಯಾಂಟಡೆನ್ {Lantadene} ವಿಷವು ದನ-ಕರುಗಳ ಯಕೃತ್ತನ್ನು ಹಾಳುಮಾಡುತ್ತದೆ ಮತ್ತು ಚರ್ಮದ ರೋಗ ತರುತ್ತದೆ.",
        "tactics_en": [
            "Cut-Root-Stock Method (CRSM): Cut the primary root 5 to 7 cm below ground level using a pickaxe or tractor-mounted ripper; prevents regrowth by eliminating subterranean coppicing nodes.",
            "Competitive Canopy Revegetation: Plant aggressive native competitors like bamboo, subabul (ಸುಬಾಬುಲ್), or Cassia tora along cleared bunds to block sunlight.",
            "Summer Controlled Burning: Pile uprooted dry branches on root stumps during peak March-April heat and burn thoroughly to destroy underground root crowns.",
            "Charcoal & Biochar Conversion: Convert harvested woody stems into on-farm biochar using simple pit pyrolysis to enhance soil carbon and moisture retention."
        ],
        "tactics_kn": [
            "ಬುಡದ ಕತ್ತರಿಸುವ ವಿಧಾನ {Cut-Root-Stock}: ಕೇವಲ ಮೇಲಿನ ಕೊಂಬೆ ಕತ್ತರಿಸಬೇಡಿ; ಪಿಕಾಸಿ ಬಳಸಿ ಮಣ್ಣಿನ 2 ಇಂಚು ಆಳದಲ್ಲಿ ಮುಖ್ಯ ಬೇರನ್ನು ಕತ್ತರಿಸಿ ಕಿತ್ತುಹಾಕಿ, ಇದರಿಂದ ಹೊಸ ಚಿಗುರು ಬರುವುದಿಲ್ಲ.",
            "ಸ್ಪರ್ಧಾತ್ಮಕ ಬದು ಗಿಡಗಳ ನೆಡುವಿಕೆ: ಬದುಗಳಲ್ಲಿ ಸುಬಾಬುಲ್, ತಗಚೆ ಅಥವಾ ಬಿದಿರು ನೆಟ್ಟು ನೆರಳು ಮಾಡಿ, ಸೂರ್ಯನ ಬೆಳಕು ಸಿಗದೆ ಲಾಂತನಾ ಚಿಗುರುವುದನ್ನು ತಡೆಯಿರಿ.",
            "ಬೇಸಿಗೆಯಲ್ಲಿ ಒಣಗಿಸಿ ಸುಡುವುದು: ಏಪ್ರಿಲ್ ಬಿಸಿಲಿನಲ್ಲಿ ಬೇರು ಸಮೇತ ಕಿತ್ತ ಪೊದೆಗಳನ್ನು ಬದುವಿನ ಮೇಲೆ ಒಣಗಿಸಿ ಸುಟ್ಟು ಕರಕಲಾಗಿಸಿ.",
            "ಬಯೋಚಾರ್ {Biochar} ತಯಾರಿಕೆ: ದಪ್ಪನೆಯ ಒಣ ಕಾಂಡಗಳಿಂದ ಜಮೀನಿನಲ್ಲೇ ಇದ್ದಿಲು/ಬಯೋಚಾರ್ ತಯಾರಿಸಿ ಮಣ್ಣಿಗೆ ಸೇರಿಸಿದರೆ ಫಲವತ್ತತೆ ಹೆಚ್ಚುತ್ತದೆ."
        ]
    },
    {
        "id": "trianthema",
        "category": "broadleaf",
        "name_en": "Horse Purslane / Black Pigweed",
        "name_kn": "ಕಪ್ಪು ಸಬ್ಬಸಿಗೆ ಕಳೆ / ಸಾರಣೆ ಕಳೆ / ಮುಕ್ಕರಟ್ಟೆ",
        "botanical": "Trianthema portulacastrum",
        "type": "Fleshy Annual Broadleaf Weed (ರಸಭರಿತ ಅಗಲ ಎಲೆ ಕಳೆ)",
        "damage_en": "Emerges aggressively within 48 hours of sowing in cotton, sugarcane, maize, and pulses. Fleshy prostrate carpets shade out emerging crop seedlings and rob high amounts of soil potash.",
        "damage_kn": "ಬಿತ್ತನೆ ಮಾಡಿದ ಕೇವಲ 48 ಗಂಟೆಗಳಲ್ಲಿ ಮೊಳಕೆಯೊಡೆಯುವ ಅತಿ ವೇಗದ ಕಳೆ. ಹತ್ತಿ, ಕಬ್ಬು, ಮುಸುಕಿನ ಜೋಳ ಮತ್ತು ತರಕಾರಿ ಬೆಳೆಗಳ ಮೇಲೆ ಹರಡಿ ಸಸಿಗಳನ್ನು ಮುಚ್ಚಿಹಾಕುತ್ತದೆ. ಮಣ್ಣಿನ ತೇವಾಂಶ ಮತ್ತು ಪೊಟ್ಯಾಷ್ ಅನ್ನು ಲೂಟಿ ಮಾಡುತ್ತದೆ.",
        "tactics_en": [
            "Stale Seedbed Method: Give light pre-sowing irrigation, allow Trianthema to germinate within 3-4 days, then destroy flush with a shallow blade harrow before crop sowing.",
            "Thick Residue Mulching: Apply 8-10 cm layer of sugarcane trash or paddy straw; darkness completely inhibits germination of light-sensitive Trianthema seeds.",
            "Early Inter-row Cultivation (ಎಡೆಕುಂಟೆ): Run inter-cultivation blade harrow at 15-18 days after crop emergence before fleshy taproot establishes deeply.",
            "Smother Intercropping with Cowpea: Plant 1 row of cowpea between every 2 rows of cotton or sugarcane; shades out Trianthema carpets within 25 days."
        ],
        "tactics_kn": [
            "ಹಳೆಯ ಬಿತ್ತನೆ ಮಡಿ ವಿಧಾನ {Stale Seedbed}: ಬಿತ್ತನೆಗೆ 5 ದಿನ ಮುನ್ನ ಲಘು ನೀರು ಕೊಡಿ; ಕಪ್ಪು ಸಬ್ಬಸಿಗೆ ಕಳೆ 3 ದಿನದಲ್ಲೇ ಮೊಳಕೆಯೊಡೆಯುತ್ತದೆ. ತಕ್ಷಣ ಕುಂಟೆ ಹೊಡೆದು ನಾಶಮಾಡಿ ಮುಖ್ಯ ಬೆಳೆ ಬಿತ್ತಿ.",
            "ಕಬ್ಬಿನ ರವದಿ / ಒಣ ಹುಲ್ಲಿನ ಹೊದಿಕೆ: 3-4 ಇಂಚು ದಪ್ಪ ರವದಿ ಹೊದಿಸಿದರೆ ಕತ್ತಲೆಯಲ್ಲಿ ಇದರ ಬೀಜಗಳು ಮೊಳಕೆಯೊಡೆಯಲು ಸಾಧ್ಯವಿಲ್ಲ.",
            "15ನೇ ದಿನಕ್ಕೆ ಎಡೆಕುಂಟೆ ಹೊಡೆಯುವುದು: ಬೆಳೆ ಮೊಳಕೆಯೊಡೆದ 15-18 ದಿನಗಳಲ್ಲಿ ಬೇರು ಆಳಕ್ಕೆ ಇಳಿಯುವ ಮುನ್ನವೇ ಎಡೆಕುಂಟೆ ಓಡಿಸಿ.",
            "ಅಲಸಂದೆ ಸಹಬೆಳೆ: ಹತ್ತಿ ಅಥವಾ ಕಬ್ಬಿನ ಸಾಲುಗಳ ನಡುವೆ ಅಲಸಂದೆ ಬೆಳೆದರೆ 25 ದಿನಗಳಲ್ಲಿ ನೆಲ ಮುಚ್ಚಿ ಕಳೆ ಬೆಳೆಯುವುದನ್ನು ತಡೆಯುತ್ತದೆ."
        ]
    },
    {
        "id": "digitaria",
        "category": "grass",
        "name_en": "Crabgrass / Fingergrass",
        "name_kn": "ಏಡಿ ಹುಲ್ಲು / ಕಾಡು ಹುಲ್ಲು / ಬೆರಳು ಹುಲ್ಲು",
        "botanical": "Digitaria sanguinalis",
        "type": "Annual Spreading Grass (ತೆವಳುವ ವಾರ್ಷಿಕ ಹುಲ್ಲು ಕಳೆ)",
        "damage_en": "Spreading annual grass that roots vigorously at lower stem nodes. Competes severely with groundnut, maize, soybean, and finger millet, reducing pod and grain yields by up to 45%.",
        "damage_kn": "ನೆಲದ ಮೇಲೆ ಹರಡುತ್ತಾ ತನ್ನ ಪ್ರತಿ ಗಿಣ್ಣಿನಲ್ಲೂ ಬೇರುಗಳನ್ನು ಬಿಡುವ ವಾರ್ಷಿಕ ಹುಲ್ಲು. ಕಡಲೆಕಾಯಿ, ರಾಗಿ, ಮುಸುಕಿನ ಜೋಳ ಮತ್ತು ಸೋಯಾಬೀನ್ ಬೆಳೆಗಳಲ್ಲಿ ಗೊಬ್ಬರ ಮತ್ತು ತೇವಾಂಶವನ್ನು ಹೀರಿ ಇಳುವರಿಯನ್ನು 45% ರಷ್ಟು ಕುಗ್ಗಿಸುತ್ತದೆ.",
        "tactics_en": [
            "Deep Summer Mouldboard Inversion: Invert topsoil 20 cm in peak summer; exposes shallow seed bank to high desiccation heat.",
            "Narrow Row Spacing: Reduce crop row spacing by 15-20% to encourage early canopy closure and shade suppression.",
            "Shallow Blade Harrowing Before Node Rooting: Inter-cultivate with a sharp sweep blade at 14 and 28 days when seedlings are small and haven't rooted at stem nodes.",
            "Organic Mulch in Broad Beds: Cover broad bed furrows with 5-7 cm organic crop residues."
        ],
        "tactics_kn": [
            "ಬೇಸಿಗೆಯ ಆಳವಾದ ನೇಗಿಲು ಉಳುಮೆ: ಮೇ ತಿಂಗಳಲ್ಲಿ ಮಣ್ಣನ್ನು ಮಗುಚಿ ಹಾಕಿ ಬೀಜಗಳನ್ನು ಬಿಸಿಲಿಗೆ ಒಡ್ಡಿ ಒಣಗಿಸಿ.",
            "ಸಾಲುಗಳ ಅಂತರ ಕಿರಿದಾಗಿಸಿ: ಬೆಳೆಯ ಸಾಲುಗಳ ಅಂತರವನ್ನು ಸ್ವಲ್ಪ ಕಡಿಮೆ ಮಾಡಿ ಎಲೆಗಳ ಮೇಲಾವರಣದಿಂದ ನೆರಳು ಬೀಳುವಂತೆ ಮಾಡಿ ಕಳೆಯನ್ನು ದಮನಿಸಿ.",
            "ಗಿಣ್ಣುಗಳಲ್ಲಿ ಬೇರು ಬಿಡುವ ಮುನ್ನವೇ ಎಡೆಕುಂಟೆ: ಬೆಳೆ ಬಂದ 14 ಮತ್ತು 28ನೇ ದಿನಕ್ಕೆ ಚೂಪಾದ ಎಡೆಕುಂಟೆ ಹೊಡೆದು ಗಿಡಗಳನ್ನು ಬೇರುಸಹಿತ ಮೇಲಕ್ಕೆತ್ತಿ ಒಣಗಿಸಿ.",
            "ಸಾವಯವ ಹೊದಿಕೆ {Mulching}: ಸಾಲುಗಳ ಮಧ್ಯೆ ಒಣ ಕೃಷಿ ತ್ಯಾಜ್ಯವನ್ನು ಹರಡಿ ಸೂರ್ಯನ ಬೆಳಕು ತಡೆಯಿರಿ."
        ]
    },
    {
        "id": "argemone",
        "category": "broadleaf",
        "name_en": "Mexican Prickly Poppy / Satyanashi",
        "name_kn": "ಬ್ರಹ್ಮದಂಡಿ / ಕಾಡು ಕಸುಗಾಯಿ ಮುಳ್ಳುಗಿಡ / ಸತ್ಯನಾಶಿ",
        "botanical": "Argemone mexicana",
        "type": "Prickly Annual Broadleaf (ಮುಳ್ಳಿನ ವಾರ್ಷಿಕ ಕಳೆ)",
        "damage_en": "Prickly weed with yellow latex and sharp spines. Seeds contaminate mustard and edible oilseed harvests; contains sanguinarine toxin which causes epidemic dropsy, glaucoma, and heart failure.",
        "damage_kn": "ಹಳದಿ ಹಾಲನ್ನು ಹೊಂದಿರುವ ಚೂಪಾದ ಮುಳ್ಳಿನ ಗಿಡ. ಇದರ ಕಪ್ಪು ಬೀಜಗಳು ಸಾಸಿವೆ ಬೀಜವನ್ನು ಹೋಲುತ್ತವೆ. ಸಾಸಿವೆ ಎಣ್ಣೆಯಲ್ಲಿ ಇದರ ಬೀಜ ಬೆರೆತರೆ ಸಾಂಗ್ಯುನೇರಿನ್ {Sanguinarine} ಎಂಬ ವಿಷಕಾರಿ ಅಂಶದಿಂದ ಮಾರಣಾಂತಿಕ ಡ್ರಾಪ್ಸಿ {Dropsy} ರೋಗ ಮತ್ತು ಕುರುಡುತನ ಬರುತ್ತದೆ.",
        "tactics_en": [
            "Early Rosette Hand Weeding: Pull out weed rosettes during early vegetative growth before spines harden and yellow flowers bloom; wear heavy protective rubber gloves.",
            "Wetland Paddy Crop Rotation: Rotate infested fields with flooded lowland paddy; saturated anaerobic soil conditions rot and kill Argemone seeds completely within 6 weeks.",
            "Clean Certified Seed Sieve Sorting: Screen mustard and oilseed stocks through 1.5 mm mesh sieves to separate irregular prickly poppy seeds from spherical mustard seeds.",
            "Safe Thermal Incineration: Never discard flowering or fruiting Argemone plants on field bunds; burn them immediately to prevent seed shed."
        ],
        "tactics_kn": [
            "ಎಳೆಯ ಹಂತದಲ್ಲೇ ಕೈಗವಸು ಧರಿಸಿ ಕೀಳುವುದು: ಮುಳ್ಳು ಗಟ್ಟಿಯಾಗುವ ಮತ್ತು ಹಳದಿ ಹೂ ಬಿಡುವ ಮುಂಚೆಯೇ ರಬ್ಬರ್ ಕೈಗವಸು ಧರಿಸಿ ಬುಡಸಹಿತ ಕಿತ್ತುಹಾಕಿ.",
            "ಭತ್ತದ ಗದ್ದೆ ಬೆಳೆ ಪರಿವರ್ತನೆ: ಕಳೆ ಹೆಚ್ಚಿರುವ ಜಮೀನಿನಲ್ಲಿ ಗದ್ದೆ ಮಾಡಿ ಭತ್ತ ಬೆಳೆಯಿರಿ; ನೀರು ನಿಲ್ಲಿಸಿದಾಗ ಆಮ್ಲಜನಕ ಕೊರತೆಯಿಂದ ಈ ಕಳೆಯ ಬೀಜಗಳು ಕೊಳೆತು ನಾಶವಾಗುತ್ತವೆ.",
            "ಜರಡಿ ಹಿಡಿದು ಬೀಜ ಸ್ವಚ್ಛಗೊಳಿಸುವುದು: ಸಾಸಿವೆ ಬೀಜವನ್ನು ಬಿತ್ತುವ ಮುನ್ನ 1.5 ಮಿಮೀ ಜರಡಿ ಹಿಡಿದು ಬ್ರಹ್ಮದಂಡಿಯ ಬೀಜಗಳನ್ನು ಬೇರ್ಪಡಿಸಿ.",
            "ಸುಟ್ಟು ನಾಶಮಾಡುವುದು: ಕೀಳಲಾದ ಗಿಡಗಳನ್ನು ಬದುವಿನ ಮೇಲೆ ಎಸೆಯದೆ ಜಮೀನಿನಿಂದ ಹೊರಗೆ ತಂದು ಸುಟ್ಟುಹಾಕಿ."
        ]
    },
    {
        "id": "ageratum",
        "category": "broadleaf",
        "name_en": "Goat Weed / White Weed",
        "name_kn": "ಕಾಡು ಹೊಗೆಸೊಪ್ಪು / ಗಂಧದ ಕಳೆ / ಅಜ್ಜಿನ ಗಿಡ",
        "botanical": "Ageratum conyzoides",
        "type": "Aromatic Annual Broadleaf (ವಾಸನೆಯುಕ್ತ ಅಗಲ ಎಲೆ ಕಳೆ)",
        "damage_en": "Aromatic annual weed rampant in plantations (coffee, spices, arecanut, ginger) and vegetables. Acts as an alternative breeding host for whiteflies and vector of Tomato Leaf Curl Virus.",
        "damage_kn": "ತೋಟಗಾರಿಕಾ ಬೆಳೆಗಳಾದ ಅಡಿಕೆ, ಕಾಫಿ, ಶುಂಠಿ, ಏಲಕ್ಕಿ ಮತ್ತು ತರಕಾರಿಗಳಲ್ಲಿ ವಿಪರೀತವಾಗಿ ಹರಡುವ ವಾಸನೆಯುಕ್ತ ಕಳೆ. ಇದು ಬಿಳಿ ನೊಣಗಳಿಗೆ {Whiteflies} ಆಶ್ರಯ ನೀಡುತ್ತದೆ ಮತ್ತು ಟೊಮೆಟೊ ಎಲೆ ಮುದುರು ವೈರಸ್ ಹರಡಲು ಕಾರಣವಾಗುತ್ತದೆ.",
        "tactics_en": [
            "Organic Mulch Blanket: Spread a 7-10 cm layer of coffee cherry husk, arecanut fronds, or dried leaves; blocks the light required for tiny photoblastic Ageratum seeds to germinate.",
            "Pre-Bloom Hand Pulling: Uproot easily by hand after light rains when soil is soft, strictly before white-lilac flower clusters form.",
            "Cover Cropping with Velvet Bean: Sow Velvet bean (Mucuna pruriens) or Cowpea in plantation interspaces to choke out Ageratum carpet within 40 days.",
            "Composting Prior to Flowering: Add tender pre-flowering plants directly to farm compost pits; decomposes rapidly into nutrient-rich green matter."
        ],
        "tactics_kn": [
            "ಕಾಫಿ ಸಿಪ್ಪೆ / ಅಡಿಕೆ ಸೋಗೆಯ ಹೊದಿಕೆ: ಮರಗಳ ಬುಡ ಮತ್ತು ಸಾಲುಗಳ ಮಧ್ಯೆ 3-4 ಇಂಚು ಒಣ ಎಲೆ ಅಥವಾ ಕಾಫಿ ಸಿಪ್ಪೆ ಹೊದಿಸಿ ಬೆಳಕು ಬೀಳದಂತೆ ಮಾಡಿ.",
            "ಹೂ ಬಿಡುವ ಮುನ್ನ ಕೈಯಿಂದ ಕೀಳುವುದು: ಮಳೆ ಬಿದ್ದ ನಂತರ ಮಣ್ಣು ಮೆತ್ತಗಿದ್ದಾಗ ಬಿಳಿ ಹೂ ಬಿಡುವ ಮುಂಚೆಯೇ ಕೈಯಿಂದ ಸುಲಭವಾಗಿ ಕಿತ್ತು ತೆಗೆಯಿರಿ.",
            "ವೆಲ್ವೆಟ್ ಬೀನ್ / ಅಲಸಂದೆ ಹೊದಿಕೆ ಬೆಳೆ: ತೋಟಗಳಲ್ಲಿ ಸಾಲುಗಳ ಮಧ್ಯೆ ವೆಲ್ವೆಟ್ ಬೀನ್ {Mucuna} ಬೆಳೆಸಿ ಕಳೆಯನ್ನು ಸಂಪೂರ್ಣವಾಗಿ ಹತ್ತಿಕ್ಕಿ.",
            "ಹೂ ಬಿಡದ ಗಿಡಗಳಿಂದ ಕಾಂಪೋಸ್ಟ್: ಎಳೆಯ ಗಿಡಗಳನ್ನು ಕಾಂಪೋಸ್ಟ್ ಗುಂಡಿಗೆ ಸೇರಿಸಿ ಉತ್ತಮ ಹಸಿರೆಲೆ ಗೊಬ್ಬರ ಪಡೆಯಿರಿ."
        ]
    },
    {
        "id": "xanthium",
        "category": "broadleaf",
        "name_en": "Cocklebur / Burweed",
        "name_kn": "ಮರಳು ಮುಳ್ಳು / ಕಾಡು ಭೇಂಡಿ / ಗೊಖ್ರು ಮುಳ್ಳು",
        "botanical": "Xanthium strumarium",
        "type": "Coarse Annual Broadleaf (ಮುಳ್ಳಿನ ಕಾಯಿ ವಾರ್ಷಿಕ ಕಳೆ)",
        "damage_en": "Hard hooked burs cling tenaciously to animal fur, sheep wool, and farmer clothing, severely degrading wool quality. Emerging cotyledons contain carboxyatractyloside, highly poisonous to grazing livestock.",
        "damage_kn": "ಕೊಂಡಿಯಂತಹ ಮುಳ್ಳಿನ ಕಾಯಿಗಳನ್ನು ಹೊಂದಿರುವ ಕಳೆ. ದನ-ಕುರಿಗಳ ತುಪ್ಪಳ ಮತ್ತು ರೈತರ ಬಟ್ಟೆಗೆ ಅಂಟಿಕೊಂಡು ವೇಗವಾಗಿ ಹರಡುತ್ತದೆ. ಇದರ ಎಳೆಯ ಮೊಳಕೆಗಳಲ್ಲಿರುವ ವಿಷಕಾರಿ ಅಂಶದಿಂದ ಕುರಿ ಮತ್ತು ಜಾನುವಾರುಗಳು ತಿಂದರೆ ವಿಷಬಾಧೆಯಾಗುತ್ತದೆ.",
        "tactics_en": [
            "Mechanical Mowing Before Bur Hardening: Mow or scythe stands when green flower heads first appear; preventing hard spiny bur formation breaks the multi-year seed cycle.",
            "Deep Ploughing Burial: Burs cannot emerge from depths greater than 8 cm. Invert topsoil with deep disc ploughing during summer land preparation.",
            "Biological Rust Fungus Inoculation: Encourage endemic rust fungus (Puccinia xanthii) which attacks leaves and prevents viable seed production.",
            "Competitive Sunn Hemp Smother: Broadcast 30 kg/ha sunn hemp along field borders and stream banks to outcompete Cocklebur stands."
        ],
        "tactics_kn": [
            "ಕಾಯಿ ಮುಳ್ಳಾಗುವ ಮುನ್ನವೇ ಕುಯ್ದು ಹಾಕುವುದು: ಹಸಿರು ಹೂ ಗೊಂಚಲು ಬಂದ ತಕ್ಷಣವೇ ಕುಡುಗೋಲಿನಿಂದ ಕುಯ್ದು ಹಾಕಿ, ಗಟ್ಟಿಯಾದ ಮುಳ್ಳಿನ ಕಾಯಿ ಕಟ್ಟಲು ಬಿಡಬೇಡಿ.",
            "ಆಳವಾದ ನೇಗಿಲು ಉಳುಮೆ: ಇದರ ಕಾಯಿಗಳು 8 ಸೆಂ.ಮೀ.ಗಿಂತ ಆಳದಲ್ಲಿದ್ದರೆ ಮೊಳಕೆಯೊಡೆಯಲು ಸಾಧ್ಯವಿಲ್ಲ; ಡಿಸ್ಕ್ ನೇಗಿಲಿನಿಂದ ಮಣ್ಣನ್ನು ಆಳವಾಗಿ ತಿರುವಿ ಮುಚ್ಚಿಹಾಕಿ.",
            "ಸಣಬಿನ ಸ್ಪರ್ಧಾತ್ಮಕ ಬೆಳೆ: ಬದುಗಳಲ್ಲಿ ಮತ್ತು ನೀರಿನ ಕಾಲುವೆ ಬದಿಗಳಲ್ಲಿ ಸಣಬನ್ನು ದಟ್ಟವಾಗಿ ಬಿತ್ತಿ ಮುಳ್ಳು ಬೆಳೆಯದಂತೆ ತಡೆಯಿರಿ.",
            "ಬೇಸಿಗೆಯಲ್ಲಿ ಕಿತ್ತು ಸುಡುವುದು: ಒಣಗಿದ ಗಿಡಗಳನ್ನು ಕಾಯಿ ಸಮೇತ ರಾಶಿ ಹಾಕಿ ಜಮೀನಿನಿಂದ ಹೊರಗೆ ಸುಟ್ಟುಹಾಕಿ."
        ]
    },
    {
        "id": "mimosa",
        "category": "aquatic_invasive",
        "name_en": "Sensitive Plant / Touch-Me-Not",
        "name_kn": "ಮುಟ್ಟಿದರೆ ಮುನಿ / ಮುಳ್ಳು ಲಜ್ಜಾವತಿ / ನಾಚಿಕೆ ಮುಳ್ಳು",
        "botanical": "Mimosa pudica",
        "type": "Thorny Creeping Perennial Subshrub (ಮುಳ್ಳಿನ ತೆವಳು ಪೊದೆ)",
        "damage_en": "Forms prickly ground-hugging mats in plantations, orchards, pasturelands, and bunds. Sharp recurved thorns injure barefoot farm workers, puncture tractor tires, and choke plantation ground.",
        "damage_kn": "ನೆಲದ ಮೇಲೆ ಚಾಪೆಯಂತೆ ಹರಡುವ ಮುಳ್ಳಿನ ದೀರ್ಘಾವಧಿ ಕಳೆ. ಇದರ ಚೂಪಾದ ಮುಳ್ಳುಗಳು ಕೃಷಿ ಕಾರ್ಮಿಕರ ಕಾಲಿಗೆ ಚುಚ್ಚಿ ಗಾಯ ಮಾಡುತ್ತವೆ ಮತ್ತು ಟ್ರ್ಯಾಕ್ಟರ್ ಟೈರ್‌ಗೆ ಹಾನಿ ಮಾಡುತ್ತವೆ. ತೋಟಗಳಲ್ಲಿ ಇತರ ಉಪಯುಕ್ತ ಸಸ್ಯಗಳನ್ನು ಬೆಳೆಯಲು ಬಿಡುವುದಿಲ್ಲ.",
        "tactics_en": [
            "Manual Root-Crown Grubbing: Use a pickaxe or sharp weeding hoe to sever woody taproot 5 cm below the soil line when ground is damp.",
            "Heavy Sheet Mulching: Cover infested orchard rings with thick biodegradable banana pseudostem slices or opaque black mulching sheet for 60 days.",
            "Planting Vigorous Shade Covers: Establish dense tall forage legumes like Stylosanthes guianensis or Desmodium; sensitive plant is shade-intolerant and dies under low light.",
            "Spot Desiccation Tillage: Harrow lightly during blazing April sun to detach woody crowns and desiccate them before monsoon rains."
        ],
        "tactics_kn": [
            "ಪಿಕಾಸಿಯಿಂದ ಆಳವಾಗಿ ಕಿತ್ತುಹಾಕುವುದು: ಮಳೆ ಬಿದ್ದಾಗ ಮಣ್ಣು ಮೆತ್ತಗಿದ್ದಾಗ ಪಿಕಾಸಿಯಿಂದ ನೆಲದ 2 ಇಂಚು ಕೆಳಗೆ ಗಟ್ಟಿಯಾದ ಬೇರನ್ನು ಕತ್ತರಿಸಿ ಬುಡಸಹಿತ ಕಿತ್ತುಹಾಕಿ.",
            "ಬಾಳೆ ದಿಂಡು / ಪ್ಲಾಸ್ಟಿಕ್ ಹೊದಿಕೆ: ಬಾಳೆ ದಿಂಡಿನ ಹೋಳುಗಳು ಅಥವಾ ಕಪ್ಪು ಪ್ಲಾಸ್ಟಿಕ್ ಶೀಟ್ ಹೊದಿಸಿ ಸೂರ್ಯನ ಬೆಳಕು ತಡೆದು ಒಣಗಿಸಿ.",
            "ನೆರಳು ನೀಡುವ ಮೇವಿನ ಬೆಳೆಗಳು: ಸ್ಟೈಲೋ {Stylosanthes} ಅಥವಾ ಡೆಸ್ಮೋಡಿಯಂನಂತಹ ಎತ್ತರದ ಮೇವಿನ ಬೆಳೆಗಳನ್ನು ಬೆಳೆಸಿ; ನೆರಳಿನಲ್ಲಿ ನಾಚಿಕೆ ಮುಳ್ಳು ಬದುಕಲಾರದು.",
            "ಬೇಸಿಗೆ ಬಿಸಿಲಿನಲ್ಲಿ ಒಣಗಿಸುವುದು: ಏಪ್ರಿಲ್ ಬಿಸಿಲಿನಲ್ಲಿ ಉಳುಮೆ ಮಾಡಿ ಬೇರುಗಳನ್ನು ನೆಲದಿಂದ ಮೇಲೆತ್ತಿ ಒಣಗಿಸಿ."
        ]
    },
    {
        "id": "convolvulus",
        "category": "aquatic_invasive",
        "name_en": "Field Bindweed / Creeping Jenny",
        "name_kn": "ಬೆಟ್ಟದ ಹರಳು ಬಳ್ಳಿ / ಹಿರಣಖುರಿ / ಕಳೆ ಬಳ್ಳಿ",
        "botanical": "Convolvulus arvensis",
        "type": "Deep-Rooted Perennial Vine (ಆಳ ಬೇರಿನ ಕಳೆ ಬಳ್ಳಿ)",
        "damage_en": "Extensive root system penetrates 3 to 6 meters into deep subsoil. Twines tightly around wheat, pulses, maize, and cotton, pulling down standing crops and causing severe mechanical harvesting blockages.",
        "damage_kn": "ನೆಲದೊಳಗೆ 10 ರಿಂದ 20 ಅಡಿ ಆಳದವರೆಗೆ ಇಳಿಯುವ ಭೀಕರ ಬೇರುಗಳನ್ನು ಹೊಂದಿರುವ ಬಳ್ಳಿ. ಗೋಧಿ, ಕಡಲೆ, ತೊಗರಿ ಮತ್ತು ಹತ್ತಿ ಬೆಳೆಗಳ ಕಾಂಡಕ್ಕೆ ಬಿಗಿಯಾಗಿ ಸುತ್ತಿಕೊಂಡು ಬೆಳೆಯನ್ನು ಕೆಳಕ್ಕೆ ಎಳೆದು ಬೀಳಿಸುತ್ತದೆ ಮತ್ತು ಕೊಯ್ಲು ಯಂತ್ರಗಳಿಗೆ ಅಡ್ಡಿಪಡಿಸುತ್ತದೆ.",
        "tactics_en": [
            "Repeated Exhaustion Cultivation: Shallow cultivate at strict 14 to 21 day intervals for one full season; exhausts starch reserves in deep perennial root systems.",
            "Allelopathic Dense Sudangrass / Sorghum: Plant high-density forage sorghum or hybrid Sudangrass; aggressive shading suppresses climbing shoots.",
            "High-Temperature Summer Solarization: Irrigate and cover tightly with 50-micron transparent plastic during peak summer to bake top 30 cm root crowns.",
            "Rigorous Hand-Pulling Before Seed Set: Hand-pull climbing vines before pinkish-white trumpet flowers set long-lived seeds (seeds remain viable for over 30 years!)."
        ],
        "tactics_kn": [
            "ನಿರಂತರ 20 ದಿನಕ್ಕೊಮ್ಮೆ ಕುಂಟೆ ಹೊಡೆಯುವುದು: ಸತತವಾಗಿ 2-3 ವಾರಗಳ ಅಂತರದಲ್ಲಿ ಕುಂಟೆ ಹೊಡೆದು ಚಿಗುರುಗಳನ್ನು ಕತ್ತರಿಸುತ್ತಿದ್ದರೆ ಬೇರಿನಲ್ಲಿರುವ ಪಿಷ್ಟದ ಶಕ್ತಿ ಖಾಲಿಯಾಗಿ ಬಳ್ಳಿ ಸಾಯುತ್ತದೆ.",
            "ದಟ್ಟ ಜೋಳ ಅಥವಾ ಮೇವಿನ ಹುಲ್ಲು: ಜಮೀನಿನಲ್ಲಿ ದಟ್ಟವಾಗಿ ಮೇವಿನ ಜೋಳ ಬೆಳೆಯಿರಿ; ಎತ್ತರದ ಬೆಳೆಯ ನೆರಳಿನಲ್ಲಿ ಕಳೆ ಬಳ್ಳಿ ಹರಡಲು ಸಾಧ್ಯವಾಗುವುದಿಲ್ಲ.",
            "ಬೇಸಿಗೆ ಸೌರ ತಾಪನ {Solarization}: ಮೇ ತಿಂಗಳಲ್ಲಿ ಮಣ್ಣು ನೆನೆಸಿ ಪ್ಲಾಸ್ಟಿಕ್ ಶೀಟ್ ಹೊದಿಸಿ ಬೇರುಗಳನ್ನು ಸುಟ್ಟುಹಾಕಿ.",
            "ಹೂ ಬಿಡುವ ಮುನ್ನವೇ ಕೀಳುವಿಕೆ: ಬಿಳಿ/ಗುಲಾಬಿ ಬಣ್ಣದ ಕಹಳೆ ಹೂ ಬಿಟ್ಟು ಬೀಜ ಕಟ್ಟುವ ಮುನ್ನವೇ ಕಿತ್ತು ತೆಗೆಯಿರಿ (ಇದರ ಬೀಜಗಳು ಮಣ್ಣಿನಲ್ಲಿ 30 ವರ್ಷಗಳವರೆಗೆ ಜೀವಂತವಾಗಿರುತ್ತವೆ!)."
        ]
    },
    {
        "id": "chenopodium",
        "category": "broadleaf",
        "name_en": "Common Lambsquarters / Fat-Hen",
        "name_kn": "ಕಾಡು ಬಸಳೆ / ಹುಚ್ಚು ಪಾಲಕ್ / ಬಾತೂ ಕಳೆ",
        "botanical": "Chenopodium album",
        "type": "Winter Annual Broadleaf (ಹಿಂಗಾರು ವಾರ್ಷಿಕ ಅಗಲ ಎಲೆ ಕಳೆ)",
        "damage_en": "Fast-growing winter weed producing up to 75,000 seeds per plant. Competes intensely with wheat, chickpeas, mustard, onion, and potato, absorbing huge quantities of soil potassium and moisture.",
        "damage_kn": "ಹಿಂಗಾರು ಋತುವಿನಲ್ಲಿ ಗೋಧಿ, ಕಡಲೆ, ಸಾಸಿವೆ, ಈರುಳ್ಳಿ ಮತ್ತು ಆಲೂಗಡ್ಡೆ ಬೆಳೆಗಳಲ್ಲಿ ಬರುವ ಕಳೆ. ಒಂದೇ ಗಿಡವು 70,000 ಕ್ಕೂ ಹೆಚ್ಚು ಬೀಜ ಬಿಡುತ್ತದೆ. ಮಣ್ಣಿನಲ್ಲಿರುವ ಅಪಾರ ಪ್ರಮಾಣದ ಪೊಟ್ಯಾಷ್ ಮತ್ತು ತೇವಾಂಶವನ್ನು ಹೀರಿ ಮುಖ್ಯ ಬೆಳೆಯನ್ನು ಸೊರಗಿಸುತ್ತದೆ.",
        "tactics_en": [
            "Stale Seedbed Before Rabi Sowing: Pre-irrigate in October-November, let Chenopodium flush emerge, then harrow shallowly before sowing wheat or chickpeas.",
            "Early Hand-Weeding as Nutritious Farm Food: Hand-weed tender seedlings at 20-25 days; young Chenopodium leaves ('Bathua') are delicious, rich in iron, calcium, and vitamins, traditionally consumed as greens or livestock fodder.",
            "Close Row Canopy Planting: Reduce inter-row spacing to 18-20 cm in wheat/chickpeas to shade out photophilic Chenopodium seedlings.",
            "Organic Rice Straw Mulching in Vegetables: Lay 5-8 cm straw mulch between vegetable ridges (onion, garlic, potato) to prevent seedling emergence."
        ],
        "tactics_kn": [
            "ಹಿಂಗಾರು ಹಳೆಯ ಬಿತ್ತನೆ ಮಡಿ ವಿಧಾನ {Stale Seedbed}: ಅಕ್ಟೋಬರ್-ನವೆಂಬರ್‌ನಲ್ಲಿ ಬಿತ್ತನೆಗೆ ಮುನ್ನ ನೀರು ಕೊಟ್ಟು, ಕಾಡು ಬಸಳೆ ಮೊಳಕೆಯೊಡೆದ ತಕ್ಷಣ ಕುಂಟೆ ಹೊಡೆದು ನಾಶಮಾಡಿ.",
            "20ನೇ ದಿನಕ್ಕೆ ಕಳೆ ಕಿತ್ತು ಪೌಷ್ಟಿಕ ಆಹಾರವಾಗಿ ಬಳಸಿ: ಬೆಳೆ ಬಂದ 20-25 ದಿನಗಳಲ್ಲಿ ಎಳೆಯ ಗಿಡಗಳನ್ನು ಕೈಯಿಂದ ಕೀಳಿ; ಈ 'ಬಾತೂ' ಸೊಪ್ಪು ಕೃಷಿ ಕುಟುಂಬಗಳಿಗೆ ಕಬ್ಬಿಣಾಂಶ ಮತ್ತು ಕ್ಯಾಲ್ಸಿಯಂ ಸಮೃದ್ಧ ಅತ್ಯುತ್ತಮ ಪೌಷ್ಟಿಕ ತರಕಾರಿಯಾಗಿದೆ ಅಥವಾ ದನಗಳಿಗೆ ಉತ್ತಮ ಮೇವು.",
            "ಸಾಲುಗಳ ಅಂತರ ಕಿರಿದಾಗಿಸಿ: ಗೋಧಿ ಮತ್ತು ಕಡಲೆಯಲ್ಲಿ ಸಾಲುಗಳ ಅಂತರ ಕಡಿಮೆ ಮಾಡಿ ಬೆಳೆಯ ನೆರಳು ಬೀಳುವಂತೆ ಮಾಡಿ.",
            "ತರಕಾರಿಗಳಲ್ಲಿ ಒಣ ಹುಲ್ಲಿನ ಹೊದಿಕೆ: ಈರುಳ್ಳಿ ಮತ್ತು ಬೆಳ್ಳುಳ್ಳಿ ಸಾಲುಗಳಲ್ಲಿ ಭತ್ತದ ಒಣ ಹುಲ್ಲು ಹೊದಿಸಿ ಕಳೆ ಬರದಂತೆ ತಡೆಯಿರಿ."
        ]
    },
    {
        "id": "celosia",
        "category": "broadleaf",
        "name_en": "Silver Cockscomb / Feather Cockscomb",
        "name_kn": "ಕಾಡು ಕೊಳಕಿ / ಕುದುರೆ ಜುಟ್ಟು ಕಳೆ / ಬೆಳ್ಳಿ ಜುಟ್ಟು",
        "botanical": "Celosia argentea",
        "type": "Erect Annual Broadleaf (ನೆಟ್ಟಗೆ ಬೆಳೆಯುವ ವಾರ್ಷಿಕ ಕಳೆ)",
        "damage_en": "Erect annual with silvery-pink terminal flower spikes. Widely infests rainfed maize, soybean, groundnut, sorghum, and ragi, competing severely for nitrogen and serving as alternate host for root-knot nematodes.",
        "damage_kn": "ಬೆಳ್ಳಿಯಂತಹ ಹೊಳಪಿನ ಜುಟ್ಟಿನ ಹೂವುಗಳನ್ನು ಬಿಡುವ ಕಳೆ. ಮಳೆಯಾಶ್ರಿತ ಮುಸುಕಿನ ಜೋಳ, ಸೋಯಾಬೀನ್, ಕಡಲೆಕಾಯಿ, ಜೋಳ ಮತ್ತು ರಾಗಿ ಹೊಲಗಳಲ್ಲಿ ವಿಪರೀತವಾಗಿ ಹರಡುತ್ತದೆ. ಸಾರಜನಕವನ್ನು ಹೀರುವುದಲ್ಲದೆ ಬೇರು ಗಂಟು ಜಂತುಹುಳುಗಳಿಗೆ {Nematodes} ಆಶ್ರಯ ನೀಡುತ್ತದೆ.",
        "tactics_en": [
            "Early Uprooting Before Silvery Plumes Turn Seed: Rogue out plants manually when tender, strictly before pink-silvery flower spikes mature into thousands of black seeds.",
            "Stale Seedbed with Early Monsoon Showers: Till immediately after pre-monsoon showers (Rohini/Mrigashira rains), allow flush emergence, and harrow down.",
            "Intercropping Fast-Growing Cowpea: Plant spreading cowpea or horsegram between maize or sorghum rows to block soil light within 30 days.",
            "Crop Rotation with Wetland Paddy: Rotate heavily infested upland parcels with lowland puddle-transplanted paddy to destroy seed viability."
        ],
        "tactics_kn": [
            "ಹೂವು ಬೆಳ್ಳಿ ಬಣ್ಣಕ್ಕೆ ತಿರುಗುವ ಮುನ್ನವೇ ಕೀಳುವಿಕೆ: ಗಿಡಗಳು ಎಳೆಯದಾಗಿರುವಾಗಲೇ ಕೈಯಿಂದ ಕೀಳಿ; ಜುಟ್ಟು ಹೂವು ಬಲಿತು ಕಪ್ಪು ಬೀಜಗಳು ಮಣ್ಣಿಗೆ ಉದುರದಂತೆ ತಡೆಯಿರಿ.",
            "ಮುಂಗಾರು ಮುಂಚಿನ ಮಳೆಯಲ್ಲಿ ಕುಂಟೆ ಹೊಡೆಯುವುದು: ರೋಹಿಣಿ ಅಥವಾ ಮೃಗಶಿರಾ ಮಳೆಯಾದ ತಕ್ಷಣ ಜಮೀನು ಹದಮಾಡಿ, ಕಳೆ ಮೊಳಕೆಯೊಡೆದ ತಕ್ಷಣ ಕುಂಟೆ ಹೊಡೆದು ಬಿತ್ತನೆ ಮಾಡಿ.",
            "ಅಲಸಂದೆ / ಹುರುಳಿ ಸಹಬೆಳೆ: ಮುಸುಕಿನ ಜೋಳ ಅಥವಾ ಜೋಳದ ಸಾಲುಗಳ ನಡುವೆ ಹರಡುವ ಅಲಸಂದೆ ಅಥವಾ ಹುರುಳಿ ಬೆಳೆದು ಸೂರ್ಯನ ಬೆಳಕು ತಡೆದು ಕಳೆ ದಮನಿಸಿ.",
            "ಗದ್ದೆ ಭತ್ತದ ಬೆಳೆ ಪರಿವರ್ತನೆ: ಕಳೆ ಜಾಸ್ತಿಯಿರುವ ಜಾಗದಲ್ಲಿ ಗದ್ದೆ ಮಾಡಿ ಒಂದು ಋತು ಭತ್ತ ಬೆಳೆದರೆ ಬೀಜಗಳು ಕೊಳೆತು ಹೋಗುತ್ತವೆ."
        ]
    }
]

# 2. ALLELOPATHIC SMOTHER & COVER CROPS
COVER_CROPS_DATA = [
    {
        "name_en": "Sunn Hemp",
        "name_kn": "ಸಣಬು",
        "botanical": "Crotalaria juncea",
        "seed_rate": "25-30 kg/ha",
        "duration": "45-50 days before flowering",
        "biomass": "20-25 tonnes/ha fresh green biomass",
        "n_added": "80-120 kg organic Nitrogen per hectare",
        "weed_smother": "Reduces weed biomass by 85-90%; root exudates suppress root-knot nematodes in tomato and vegetables.",
        "weed_smother_kn": "ಕಳೆಯ ಪ್ರಮಾಣವನ್ನು 85-90% ಕುಗ್ಗಿಸುತ್ತದೆ; ಇದರ ಬೇರುಗಳು ಟೊಮೆಟೊ ಮತ್ತು ತರಕಾರಿಗಳಲ್ಲಿ ಬರುವ ಬೇರು ಗಂಟು ಜಂತುಹುಳುಗಳನ್ನು {Nematodes} ನೈಸರ್ಗಿಕವಾಗಿ ನಾಶಪಡಿಸುತ್ತವೆ."
    },
    {
        "name_en": "Fodder Cowpea",
        "name_kn": "ಮೇವಿನ ಅಲಸಂದೆ",
        "botanical": "Vigna unguiculata",
        "seed_rate": "20-25 kg/ha",
        "duration": "40-60 days",
        "biomass": "15-20 tonnes/ha",
        "n_added": "60-80 kg organic Nitrogen per hectare",
        "weed_smother": "Forms a dense green carpet within 30 days that starves germinating weed seeds of sunlight and conserves topsoil moisture.",
        "weed_smother_kn": "30 ದಿನಗಳಲ್ಲಿ ನೆಲದ ಮೇಲೆ ಹಸಿರು ರತ್ನಗಂಬಳಿಯಂತೆ ದಟ್ಟವಾಗಿ ಹರಡಿ ಕಳೆಗಳಿಗೆ ಸೂರ್ಯನ ಬೆಳಕು ಸಿಗದಂತೆ ಮಾಡುತ್ತದೆ ಮತ್ತು ಮಣ್ಣಿನ ತೇವಾಂಶವನ್ನು ಕಾಪಾಡುತ್ತದೆ."
    },
    {
        "name_en": "Dhaincha",
        "name_kn": "ಡಯಾಂಚ / ಧೈಂಚಾ",
        "botanical": "Sesbania aculeata",
        "seed_rate": "30-35 kg/ha",
        "duration": "45 days",
        "biomass": "20-25 tonnes/ha",
        "n_added": "70-100 kg organic Nitrogen per hectare",
        "weed_smother": "Tolerates saline, alkaline, and waterlogged Karnataka black soils; vigorous growth chokes broadleaf weeds.",
        "weed_smother_kn": "ಕರ್ನಾಟಕದ ಕ್ಷಾರಯುಕ್ತ, ಜೌಗು ಮತ್ತು ಕಪ್ಪು ಮಣ್ಣಿನಲ್ಲೂ ಸಮೃದ್ಧವಾಗಿ ಬೆಳೆದು ಹಠಮಾರಿ ಕಳೆಗಳನ್ನು ಉಸಿರುಗಟ್ಟಿಸಿ ಸಾಯಿಸುತ್ತದೆ."
    },
    {
        "name_en": "Forage Sorghum / Jowar",
        "name_kn": "ಜೋಳ (ಕಳೆ ದಮನಕಾರಿ ಬೆಳೆ ಪರಿವರ್ತನೆ)",
        "botanical": "Sorghum bicolor",
        "seed_rate": "15-20 kg/ha",
        "duration": "Rotational break crop",
        "biomass": "High forage value",
        "n_added": "Supplies abundant organic carbon",
        "weed_smother": "Roots secrete Sorgoleone, one of nature's most potent allelopathic bio-herbicides, inhibiting nutgrass and pigweed germination for months.",
        "weed_smother_kn": "ಇದರ ಬೇರುಗಳು ಸೊರ್ಗೊಲಿಯೋನ್ {Sorgoleone} ಎಂಬ ನೈಸರ್ಗಿಕ ಕಳೆನಾಶಕವನ್ನು ಸ್ರವಿಸಿ ನಂತರ ಬೆಳೆಯುವ ಬೆಳೆಯಲ್ಲಿ ಕೊರೆ ಹುಲ್ಲು ಮತ್ತು ಮುಳ್ಳು ದಂಟು ಹುಟ್ಟದಂತೆ ತಡೆಯುತ್ತವೆ."
    }
]

# 3. COMPOST & FERTILIZER SAVINGS CALCULATOR
def calculate_compost_savings(acres: float, cattle_count: int, crop_residue_quintals: float):
    """
    Computes finished farm compost yield, organic N-P-K additions,
    equivalent synthetic fertilizer bags saved (Urea and DAP), and estimated rupee savings.
    Based on standard ICAR/TNAU composting agronomy metrics.
    """
    # Daily manure collected per adult cow ~ 12 kg (dung + absorbed urine in straw bedding)
    # Annual dung produced = 12 * 365 = 4,380 kg per cow
    # For a 6-month seasonal batch: ~2,190 kg raw cattle manure per cow
    manure_batch_kg = cattle_count * 2190.0
    
    # Residue in kg (dry biomass: paddy straw, cotton stalks, jowar stubble, weeds)
    residue_kg = crop_residue_quintals * 100.0
    
    # Optimum C:N composting mass: total raw mass entering compost pit
    total_raw_biomass_kg = manure_batch_kg + residue_kg
    
    # During 90-120 days of aerobic microbial decomposition, mass reduces by 35-40% due to CO2 & moisture loss
    finished_compost_kg = total_raw_biomass_kg * 0.62
    finished_compost_tonnes = round(finished_compost_kg / 1000.0, 2)
    cartloads = round(finished_compost_tonnes / 0.75, 1) # Standard Karnataka bullock cart ~ 750 kg
    
    # Nutrient content of well-decomposed rural compost (ICAR benchmark averages):
    # Nitrogen (N): ~0.75%
    # Phosphorus (P2O5): ~0.35%
    # Potassium (K2O): ~0.70%
    org_n_kg = round(finished_compost_kg * 0.0075, 1)
    org_p_kg = round(finished_compost_kg * 0.0035, 1)
    org_k_kg = round(finished_compost_kg * 0.0070, 1)
    
    # Synthetic fertilizer equivalents:
    # 1 bag (45 kg) of Neem-Coated Urea has 46% N = ~20.7 kg pure N
    # 1 bag (50 kg) of DAP has 46% P2O5 and 18% N = 23 kg P2O5 and 9 kg N
    # 1 bag (50 kg) of MOP (Muriate of Potash) has 60% K2O = 30 kg K2O
    urea_bags_saved = round(org_n_kg / 20.7, 1)
    dap_bags_saved = round(org_p_kg / 23.0, 1)
    mop_bags_saved = round(org_k_kg / 30.0, 1)
    
    # Monetary savings (Official subsidized MRP: Urea ~₹267/bag, DAP ~₹1,350/bag, MOP ~₹1,650/bag):
    # Plus indirect savings on soil conditioning and drought resilience:
    money_saved_rs = round(
        (urea_bags_saved * 267.0) +
        (dap_bags_saved * 1350.0) +
        (mop_bags_saved * 1650.0)
    )
    
    # Soil organic carbon (SOC) impact score (out of 10)
    soc_rating = min(10.0, round(finished_compost_tonnes / (max(0.5, acres) * 2.0) * 10, 1))
    
    return {
        "finished_compost_tonnes": finished_compost_tonnes,
        "cartloads": cartloads,
        "org_n_kg": org_n_kg,
        "org_p_kg": org_p_kg,
        "org_k_kg": org_k_kg,
        "urea_bags_saved": urea_bags_saved,
        "dap_bags_saved": dap_bags_saved,
        "mop_bags_saved": mop_bags_saved,
        "money_saved_rs": money_saved_rs,
        "soc_rating": soc_rating
    }

# 4. KARNATAKA TRADITIONAL BIO-FORMULATIONS
BIO_FORMULATIONS = [
    {
        "id": "jeevamrutha",
        "name_en": "Liquid Jeevamrutha (ಜೀವಾಮೃತ)",
        "name_kn": "ದ್ರವ ಜೀವಾಮೃತ {Liquid Jeevamrutha}",
        "purpose_en": "Microbial inoculant that activates beneficial bacteria and earthworms in the soil.",
        "purpose_kn": "ಮಣ್ಣಿನಲ್ಲಿ ನೈಸರ್ಗಿಕ ಎರೆಹುಳುಗಳು ಮತ್ತು ಪ್ರಯೋಜನಕಾರಿ ಸೂಕ್ಷ್ಮಜೀವಿಗಳನ್ನು ಸಕ್ರಿಯಗೊಳಿಸುವ ಜೈವಿಕ ದ್ರಾವಣ.",
        "ingredients_en": [
            "10 kg Fresh Native Cow Dung (ನಾಟಿ ಹಸುವಿನ ಸಗಣಿ)",
            "10 Liters Native Cow Urine (ಗೋಮೂತ್ರ)",
            "2 kg Organic Jaggery (ಕಪ್ಪು ಬೆಲ್ಲ)",
            "2 kg Pulse Flour - Gram/Chickpea/Cowpea (ದ್ವಿದಳ ಧಾನ್ಯದ ಹಿಟ್ಟು)",
            "Handful of undisturbed fertile farm/banyan tree soil (ಜಮೀನಿನ ಜೀವಂತ ಮಣ್ಣು)",
            "200 Liters Water"
        ],
        "ingredients_kn": [
            "10 ಕೆಜಿ ತಾಜಾ ನಾಟಿ ಹಸುವಿನ ಸಗಣಿ",
            "10 ಲೀಟರ್ ನಾಟಿ ಹಸುವಿನ ಗೋಮೂತ್ರ",
            "2 ಕೆಜಿ ಸಾವಯವ ಕಪ್ಪು ಬೆಲ್ಲ",
            "2 ಕೆಜಿ ದ್ವಿದಳ ಧಾನ್ಯದ ಹಿಟ್ಟು (ಕಡಲೆಹಿಟ್ಟು ಅಥವಾ ಅಲಸಂದೆ ಹಿಟ್ಟು)",
            "ಒಂದು ಹಿಡಿ ರಾಸಾಯನಿಕ ಮುಟ್ಟದ ಜಮೀನಿನ ಅಥವಾ ಆಲದ ಮರದ ಕೆಳಗಿನ ಫಲವತ್ತಾದ ಜೀವಂತ ಮಣ್ಣು",
            "200 ಲೀಟರ್ ಶುದ್ಧ ನೀರು"
        ],
        "preparation_en": "Mix thoroughly in a 200L plastic drum in the shade. Stir clockwise with a wooden stick for 5 minutes twice daily (morning and evening). Keep covered with a gunny bag. Ferment for 48 to 72 hours in summer (longer in winter).",
        "preparation_kn": "200 ಲೀಟರ್ ಪ್ಲಾಸ್ಟಿಕ್ ಡ್ರಮ್‌ನಲ್ಲಿ ನೆರಳಿನಲ್ಲಿ ಚೆನ್ನಾಗಿ ಬೆರೆಸಿ. ಪ್ರತಿದಿನ ಬೆಳಿಗ್ಗೆ ಮತ್ತು ಸಂಜೆ 5 ನಿಮಿಷಗಳ ಕಾಲ ಮರದ ಕೋಲಿನಿಂದ ಪ್ರದಕ್ಷಿಣಾಕಾರವಾಗಿ (Clockwise) ತಿರುಗಿಸಿ. ಗೋಣಿಚೀಲದಿಂದ ಮುಚ್ಚಿಡಿ. 48 ರಿಂದ 72 ಗಂಟೆಗಳಲ್ಲಿ (2-3 ದಿನಗಳಲ್ಲಿ) ಸಿದ್ಧವಾಗುತ್ತದೆ.",
        "application_en": "Apply 200 Liters per acre through irrigation water or drenching around root zones every 15-21 days during vegetative and flowering stages.",
        "application_kn": "ಎಕರೆಗೆ 200 ಲೀಟರ್ ಜೀವಾಮೃತವನ್ನು ಹನಿ ನೀರಾವರಿ ಅಥವಾ ಕಾಲುವೆ ನೀರಿನ ಜೊತೆ ತಿಂಗಳಿಗೆ 2 ಬಾರಿ ಗಿಡಗಳ ಬೇರುಗಳ ಹತ್ತಿರ ತಲುಪಿಸಿ."
    },
    {
        "id": "beejamrutha",
        "name_en": "Beejamrutha Seed Treatment (ಬೀಜಾಮೃತ)",
        "name_kn": "ಬೀಜಾಮೃತ ಬೀಜೋಪಚಾರ {Beejamrutha}",
        "purpose_en": "Protects newly sown seeds from soil-borne fungi, collar rot, and bacterial wilt while enhancing early germination.",
        "purpose_kn": "ಬಿತ್ತಿದ ಬೀಜಗಳಿಗೆ ಬರುವ ಶಿಲೀಂಧ್ರ ರೋಗಗಳು, ಬೇರು ಕೊಳೆತ ಮತ್ತು ಸೊರಗು ರೋಗಗಳನ್ನು ತಡೆದು ಆರಂಭಿಕ ಮೊಳಕೆ ಸಾಮರ್ಥ್ಯ ಹೆಚ್ಚಿಸುತ್ತದೆ.",
        "ingredients_en": [
            "5 kg Fresh Cow Dung (ಸಗಣಿ)",
            "5 Liters Cow Urine (ಗೋಮೂತ್ರ)",
            "50 grams Edible Lime / Chuna (ಸುಣ್ಣ)",
            "Handful of virgin field soil (ಜಮೀನಿನ ಮಣ್ಣು)",
            "20 Liters Water"
        ],
        "ingredients_kn": [
            "5 ಕೆಜಿ ನಾಟಿ ಹಸುವಿನ ಸಗಣಿ",
            "5 ಲೀಟರ್ ಗೋಮೂತ್ರ",
            "50 ಗ್ರಾಂ ತಿನ್ನುವ ಸುಣ್ಣ",
            "ಒಂದು ಹಿಡಿ ಫಲವತ್ತಾದ ಮಣ್ಣು",
            "20 ಲೀಟರ್ ನೀರು"
        ],
        "preparation_en": "Hang cow dung in a cloth bag suspended in 20L water for 12 hours. Squeeze the dung extract into water. Mix slaked lime separately in water and add to the barrel with cow urine and soil. Stir well.",
        "preparation_kn": "ಸಗಣಿಯನ್ನು ತೆಳುವಾದ ಬಟ್ಟೆಯಲ್ಲಿ ಕಟ್ಟಿ 20 ಲೀಟರ್ ನೀರಿನಲ್ಲಿ 12 ಗಂಟೆ ನೆನೆಸಿ ರಸವನ್ನು ಹಿಂಡಿ. ಸುಣ್ಣವನ್ನು ಪ್ರತ್ಯೇಕವಾಗಿ ನೀರಿನಲ್ಲಿ ಕರಗಿಸಿ, ಗೋಮೂತ್ರ ಮತ್ತು ಮಣ್ಣಿನ ಜೊತೆ ಬೆರೆಸಿ ಚೆನ್ನಾಗಿ ಕದಡಿ.",
        "application_en": "Gently coat seeds with hands, dry in the shade for 30 minutes before sowing. Do not dry in direct hot sun.",
        "application_kn": "ಬೀಜಗಳಿಗೆ ಬೀಜಾಮೃತವನ್ನು ಮೃದುವಾಗಿ ಲೇಪಿಸಿ, ನೆರಳಿನಲ್ಲಿ 30 ನಿಮಿಷ ಒಣಗಿಸಿ ನಂತರ ತಕ್ಷಣ ಬಿತ್ತನೆ ಮಾಡಿ. ಬಿಸಿಲಿನಲ್ಲಿ ಒಣಗಿಸಬೇಡಿ."
    },
    {
        "id": "ghana_jeevamrutha",
        "name_en": "Ghana Jeevamrutha (ಘನ ಜೀವಾಮೃತ - Dry Form)",
        "name_kn": "ಘನ ಜೀವಾಮೃತ {Ghana Jeevamrutha}",
        "purpose_en": "Solid organic microbial fertilizer ideal for rainfed dryland farming where drip/flood irrigation is unavailable.",
        "purpose_kn": "ಹನಿ ನೀರಾವರಿ ಇಲ್ಲದ ಒಣಭೂಮಿ ಮತ್ತು ಮಳೆಯಾಶ್ರಿತ ಜಮೀನುಗಳಿಗೆ ಬಿತ್ತನೆ ಸಮಯದಲ್ಲಿ ಸಾಲಿನಲ್ಲಿ ಹಾಕಬಹುದಾದ ಘನ ಗೊಬ್ಬರ.",
        "ingredients_en": [
            "100 kg Well-rotted Farmyard Manure / Desi Cow Dung",
            "10 Liters Liquid Jeevamrutha"
        ],
        "ingredients_kn": [
            "100 ಕೆಜಿ ಚೆನ್ನಾಗಿ ಕಳಿತ ಕೊಟ್ಟಿಗೆ ಗೊಬ್ಬರ ಅಥವಾ ಒಣ ನಾಟಿ ಸಗಣಿ ಪುಡಿ",
            "10 ಲೀಟರ್ ದ್ರವ ಜೀವಾಮೃತ"
        ],
        "preparation_en": "Spread dry manure evenly in shade. Sprinkle liquid Jeevamrutha on top, mix uniformly. Heap and cover with gunny bags for 48 hours, then dry in shade and store in bags.",
        "preparation_kn": "ನೆರಳಿನಲ್ಲಿ ಗೊಬ್ಬರವನ್ನು ಹರಡಿ, ಮೇಲೆ ದ್ರವ ಜೀವಾಮೃತವನ್ನು ಸಮನಾಗಿ ಸಿಂಪಡಿಸಿ ಬೆರೆಸಿ. ರಾಶಿ ಮಾಡಿ 48 ಗಂಟೆ ಗೋಣಿಚೀಲ ಮುಚ್ಚಿ ನಂತರ ನೆರಳಿನಲ್ಲಿ ಒಣಗಿಸಿ ಚೀಲಗಳಲ್ಲಿ ತುಂಬಿಡಿ.",
        "application_en": "Broadcast 100-200 kg per acre in furrows during final land preparation or sowing.",
        "application_kn": "ಕೊನೆಯ ಉಳುಮೆಯ ಸಮಯದಲ್ಲಿ ಅಥವಾ ಬಿತ್ತನೆಯ ವೇಳೆ ಸಾಲುಗಳಲ್ಲಿ ಎಕರೆಗೆ 100-200 ಕೆಜಿ ಹಾಕಿ."
    },
    {
        "id": "neemastra",
        "name_en": "Neemastra / Agniastra (ನೀಮಾಸ್ತ್ರ)",
        "name_kn": "ನೀಮಾಸ್ತ್ರ / ಅಗ್ನಿಯಸ್ತ್ರ {Neemastra}",
        "purpose_en": "Natural botanical pest repellent against sap-sucking pests (aphids, thrips, whiteflies) and small caterpillars.",
        "purpose_kn": "ರಸಹೀರುವ ಕೀಟಗಳು (ಜಿಗಟು, ನುಸಿ, ಬಿಳಿ ನೊಣ) ಮತ್ತು ಎಳೆಯ ಲದ್ದಿ ಹುಳುಗಳನ್ನು ನಿಯಂತ್ರಿಸುವ ನೈಸರ್ಗಿಕ ಕಷಾಯ.",
        "ingredients_en": [
            "5 kg Crushed Neem Leaves or Neem Seed Kernels (ಬೇವಿನ ಸೊಪ್ಪು ಅಥವಾ ಬೀಜ)",
            "5 Liters Cow Urine (ಗೋಮೂತ್ರ)",
            "1 kg Fresh Cow Dung (ಸಗಣಿ)",
            "100 Liters Water"
        ],
        "ingredients_kn": [
            "5 ಕೆಜಿ ಅರೆದ ಬೇವಿನ ಸೊಪ್ಪು ಅಥವಾ ಬೇವಿನ ಬೀಜದ ಪುಡಿ",
            "5 ಲೀಟರ್ ಗೋಮೂತ್ರ",
            "1 ಕೆಜಿ ಹಸುವಿನ ಸಗಣಿ",
            "100 ಲೀಟರ್ ನೀರು"
        ],
        "preparation_en": "Crush leaves into a pulp. Mix with cow dung, cow urine, and water in a drum. Cover with gunny cloth and ferment in shade for 48 hours, stirring twice daily. Filter through fine cloth.",
        "preparation_kn": "ಬೇವಿನ ಸೊಪ್ಪನ್ನು ರುಬ್ಬಿ ಸಗಣಿ, ಗೋಮೂತ್ರ ಮತ್ತು ನೀರಿನೊಂದಿಗೆ ಡ್ರಮ್‌ನಲ್ಲಿ ಬೆರೆಸಿ. 48 ಗಂಟೆ ನೆರಳಿನಲ್ಲಿ ಕೊಳೆಯಲು ಬಿಟ್ಟು, ನಂತರ ತೆಳುವಾದ ಬಟ್ಟೆಯಿಂದ ಸೋಸಿ ಸಂಗ್ರಹಿಸಿ.",
        "application_en": "Spray directly on affected leaves early in the morning or late evening. Do not dilute further.",
        "application_kn": "ಬೆಳಿಗ್ಗೆ ಅಥವಾ ಸಂಜೆ ವೇಳೆ ಎಲೆಗಳ ಮೇಲೆ ನೇರವಾಗಿ ಸಿಂಪಡಿಸಿ. ಕೀಟಗಳ ಬಾಧೆ ಹೆಚ್ಚಾಗಿದ್ದರೆ 8-10 ದಿನಗಳ ನಂತರ ಪುನರಾವರ್ತಿಸಿ."
    }
]

# 5. CHEMICAL SAFETY & BANNED PESTICIDE ALERTS
SAFETY_DATA = {
    "banned_chemicals": [
        {
            "name": "Monocrotophos (ಮೋನೋಕ್ರೋಟೋಫಾಸ್)",
            "hazard": "Extremely toxic organophosphate. Causes severe neurological paralysis in humans and instantly kills grazing livestock, poultry, and birds.",
            "hazard_kn": "ಅತ್ಯಂತ ಅಪಾಯಕಾರಿ ವಿಷ. ಮನುಷ್ಯರಲ್ಲಿ ನರಮಂಡಲದ ಪಾರ್ಶ್ವವಾಯು ಉಂಟುಮಾಡುತ್ತದೆ ಮತ್ತು ಮೇಯುವ ದನ-ಕರುಗಳು, ಕೋಳಿ ಹಾಗೂ ಪಕ್ಷಿಗಳನ್ನು ತಕ್ಷಣ ಸಾಯಿಸುತ್ತದೆ.",
            "status": "Strictly restricted / banned on vegetables and pulses in Karnataka."
        },
        {
            "name": "Endosulfan (ಎಂಡೋಸಲ್ಫಾನ್)",
            "hazard": "Nationally banned by Supreme Court of India. Persistent organic pollutant that leaches into groundwater aquifers and causes congenital birth deformities and cancer.",
            "hazard_kn": "ಸುಪ್ರೀಂ ಕೋರ್ಟ್‌ನಿಂದ ಭಾರತಾದ್ಯಂತ ಸಂಪೂರ್ಣ ನಿಷೇಧಿಸಲಾಗಿದೆ. ಅಂತರ್ಜಲ ಮತ್ತು ಬೋರ್‌ವೆಲ್ ನೀರಿಗೆ ಸೇರಿ ಹುಟ್ಟುವ ಮಕ್ಕಳಲ್ಲಿ ಅಂಗವೈಕಲ್ಯ ಹಾಗೂ ಕ್ಯಾನ್ಸರ್ ಉಂಟುಮಾಡುತ್ತದೆ.",
            "status": "Completely Banned across India."
        },
        {
            "name": "Phorate / Thimet (ಫೋರೇಟ್ / ತೈಮೆಟ್)",
            "hazard": "Red-triangle lethal granular chemical. Highly toxic via skin absorption; poisons soil earthworms and contaminates underground water tables.",
            "hazard_kn": "ಕೆಂಪು ತ್ರಿಕೋನದ ಮಾರಕ ಹರಳು ರೂಪದ ವಿಷ. ಚರ್ಮದ ಮೂಲಕ ನೇರವಾಗಿ ದೇಹ ಸೇರಿ ವಿಷವೇರುತ್ತದೆ; ಮಣ್ಣಿನ ಎರೆಹುಳುಗಳನ್ನು ಕೊಂದು ಅಂತರ್ಜಲವನ್ನು ಕಲುಷಿತಗೊಳಿಸುತ್ತದೆ.",
            "status": "Severely restricted. Banned in many crops."
        },
        {
            "name": "Paraquat Dichloride (ಪ್ಯಾರಾಕ್ವಾಟ್)",
            "hazard": "Extremely lethal non-selective herbicide with no known medical antidote. Accidental splash or ingestion causes irreversible pulmonary fibrosis (lung failure).",
            "hazard_kn": "ಯಾವುದೇ ಔಷಧೀಯ ವಿಷಹಾರಕ {Antidote} ಇಲ್ಲದ ಅತ್ಯಂತ ಮಾರಕ ಕಳೆನಾಶಕ. ಸಣ್ಣ ಹನಿ ಸಿಡಿದರೂ ಅಥವಾ ಉಸಿರಾಡಿದರೂ ಶ್ವಾಸಕೋಶವನ್ನು ಶಾಶ್ವತವಾಗಿ ನಿಷ್ಕ್ರಿಯಗೊಳಿಸುತ್ತದೆ.",
            "status": "High-hazard restricted chemical."
        }
    ],
    "eco_friendly_alternatives": [
        {
            "title_en": "Neem-Coated Urea (ಬೇವು ಲೇಪಿತ ಯೂರಿಯಾ)",
            "desc_en": "Slows nitrification, allowing plants to absorb 20-30% more nitrogen. Greatly reduces hazardous nitrate leaching into drinking borewell aquifers.",
            "desc_kn": "ಸಾರಜನಕವು ನಿಧಾನವಾಗಿ ಗಿಡಕ್ಕೆ ಸಿಗುವಂತೆ ಮಾಡುತ್ತದೆ. ಬೋರ್‌ವೆಲ್ ಮತ್ತು ಕುಡಿಯುವ ನೀರಿಗೆ ನೈಟ್ರೇಟ್ ವಿಷ ಸೇರುವುದನ್ನು ತಡೆಯುತ್ತದೆ."
        },
        {
            "title_en": "Bio-Fertilizer Consortia (ಜೈವಿಕ ರಸಗೊಬ್ಬರಗಳು)",
            "desc_en": "Rhizobium for pulses (fixes 50-100 kg N), Azotobacter/Azospirillum for cereals, and PSB (Phosphate Solubilizing Bacteria) to dissolve locked rock phosphate in soil.",
            "desc_kn": "ದ್ವಿದಳ ಧಾನ್ಯಗಳಿಗೆ ರೈಜೋಬಿಯಂ {Rhizobium}, ಏಕದಳ ಧಾನ್ಯಗಳಿಗೆ ಅಜೋಟೋಬ್ಯಾಕ್ಟರ್ {Azotobacter}, ಮತ್ತು ಮಣ್ಣಿನಲ್ಲಿ ಕರಗದ ರಂಜಕವನ್ನು ಕರಗಿಸಲು {PSB} ಬ್ಯಾಕ್ಟೀರಿಯಾಗಳನ್ನು ಬಳಸಿ."
        },
        {
            "title_en": "Soil Health Card Balanced Application (ಮಣ್ಣು ಆರೋಗ್ಯ ಕಾರ್ಡ್)",
            "desc_en": "Never dump chemical fertilizers blindly by habit. Always test soil at your local RSK / KVK every 2 years and apply only the deficit nutrients.",
            "desc_kn": "ಅಭ್ಯಾಸಬಲದಿಂದ ಕುರುಡಾಗಿ ಗೊಬ್ಬರ ಚೆಲ್ಲಬೇಡಿ. ಪ್ರತಿ 2 ವರ್ಷಕ್ಕೊಮ್ಮೆ ರೈತ ಸಂಪರ್ಕ ಕೇಂದ್ರದಲ್ಲಿ ಮಣ್ಣು ಪರೀಕ್ಷೆ ಮಾಡಿಸಿ ಕೊರತೆಯಿರುವ ಪೋಷಕಾಂಶಗಳನ್ನು ಮಾತ್ರ ನೀಡಿ."
        }
    ]
}

