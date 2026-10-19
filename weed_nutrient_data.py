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
