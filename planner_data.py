"""Season planner content. Every practice lists its sources. No doses are given anywhere."""

SRC = {
    "uaex": {"title": "University of Arkansas Extension: Seed germination test at home", "url": "https://www.uaex.uada.edu/publications/pdf/FSA-3149.pdf"},
    "nrcs": {"title": "USDA NRCS: Using a ragdoll test to estimate field germination", "url": "https://www.nrcs.usda.gov/plantmaterials/mspmctn4808.pdf"},
    "vic": {"title": "Agriculture Victoria: Testing crop seed for sowing", "url": "https://agriculture.vic.gov.au/crops-and-horticulture/grains-pulses-and-cereals/crop-production/general-agronomy/testing-crop-seed-for-sowing"},
    "ucd": {"title": "UC Davis: Seed germination testing (ragdoll) fact sheet", "url": "https://epakag.ucdavis.edu/vocational_training/factsheets/fs-seed-germination-test-ragdoll.pdf"},
    "icar_weed": {"title": "ICAR Indian Farming: Weed management strategies", "url": "https://epubs.icar.org.in/index.php/IndFarm/article/download/165717/59653/457864"},
    "isws23": {"title": "Indian Journal of Weed Science 2023: Stale seed bed and leguminous cover crops in cotton", "url": "https://www.isws.org.in/IJWSn/File/2023_55_Issue-1_46-49.pdf"},
    "isws12": {"title": "Indian Journal of Weed Science 2012: Soil solarization and the weed seed bank", "url": "https://www.isws.org.in/IJWSn/File/2012_44_Issue-2_122-123.pdf"},
    "phyto": {"title": "Journal of Pharmacognosy and Phytochemistry 2019: Off-season soil solarization and IWM", "url": "https://phytojournal.com/archives/2019/vol8issue3/PartZ/8-2-282-705.pdf"},
    "sare": {"title": "SARE: Purple nutsedge", "url": "https://www.sare.org/publications/manage-weeds-on-your-farm/purple-nutsedge"},
    "tnau_compost": {"title": "TNAU Agritech Portal: Compost", "url": "https://agritech.tnau.ac.in/org_farm/orgfarm_composting.html"},
    "mandya": {"title": "Organic Mandya: Compost from farm waste and cow manure", "url": "https://organicmandya.com/blogs/news/how-to-prepare-free-compost-from-farm-waste-and-cow-manure-the-organic-mandya-way"},
    "syscom": {"title": "FiBL SysCom Kenya: Making quality farm compost (leaflet)", "url": "https://systems-comparison.fibl.org/fileadmin/syscom/documents/Leaflets/Kenya/SysComKenya_leaflet_composting.pdf"},
    "pib_ncu": {"title": "PIB: Neem coated urea", "url": "https://static.pib.gov.in/WriteReadData/specificdocs/documents/2021/sep/Neem%20Coated%20.pdf"},
    "icar_ncu": {"title": "ICAR: Use and effectiveness of neem coated urea", "url": "https://epubs.icar.org.in/index.php/IJAgS/article/download/122695/46653/332869"},
    "ls_bio": {"title": "Lok Sabha answer on use of bio-fertilizers (Government of India)", "url": "https://eparlib.nic.in/bitstream/123456789/1468786/1/AU855.pdf"},
    "icar_herm": {"title": "ICAR Indian Farming: Hermetic technology for grain storage", "url": "https://epubs.icar.org.in/index.php/IndFarm/article/download/103521/40557/267105"},
    "illinois": {"title": "University of Illinois Postharvest Institute: Grain handling system", "url": "https://postharvestinstitute.illinois.edu/?p=7915"},
    "tifac": {"title": "TIFAC: Technologies to minimise grain storage loss", "url": "https://tifac.org.in/index.php/programmes/activities/8-publication/157-technologies-to-minimise-grain-storage-loss?start=4"},
    "kyd": {"title": "SDM Institute: Study of the Krishi Yantra Dhare scheme in Karnataka", "url": "https://www.sdmimd.ac.in/conferenceproceedings/iec2025papers/IEC25201.pdf"},
    "isee": {"title": "Indian Journal of Extension Education: Farmers and custom hiring centres in Tumakuru", "url": "https://epubs.icar.org.in/index.php/IJEE/article/view/122625"},
}

STAGES = ["Before sowing", "Sowing season", "Growing season", "Harvest and storage"]

ITEMS = {
    "Before sowing": [
        {
            "id": "seed_test", "title": "Test your seed before you sow",
            "summary": "A home test tells you how many seeds will really sprout, before you spend money and time sowing a whole field.",
            "steps": [
                "Mix the seed lot well and take 100 seeds. Include small, broken and discoloured seeds, because the whole lot has them.",
                "Wet a firm paper towel and squeeze out the extra water. A very soft kitchen towel is a poor choice, because roots grow into it.",
                "Spread the seeds on the towel, roll it loosely into a tube, and put it in a plastic bag. Keep it somewhere warm.",
                "Keep the towel damp, not soaking. Too much water cuts off air and spoils the test.",
                "After about 4 days, open it, count the sprouted seeds and take them out. Count again after 3 or 4 more days.",
                "With 100 seeds, the number that sprouted is the germination percentage. Repeating with 3 separate lots of 100 gives a more reliable answer.",
            ],
            "cautions": ["Some crops need more days, and hard-coated seeds can be slow. Ask your seed dealer or KVK for your crop."],
            "sources": ["uaex", "nrcs", "vic", "ucd"],
        },
        {
            "id": "summer_plough", "title": "Deep summer ploughing and solarisation",
            "summary": "Heat from the summer sun can be used to dry out and kill weed seeds and the tubers of weeds such as nutgrass.",
            "steps": [
                "Plough deeply in the hot season and repeat after 3 to 4 weeks, so roots and tubers are lifted up to dry in the sun.",
                "For solarisation, wet the soil, then cover it tightly with clear, transparent polythene sheet during the hottest weeks. In one Indian study 40 days of solarisation worked best.",
                "Inspect the sheet often and repair holes. Keep people and animals off it.",
            ],
            "cautions": [
                "Use clear, transparent sheet, as in the studies.",
                "No single method clears weeds for ever. Combined with other methods it can lower weed numbers over 2 to 3 seasons.",
            ],
            "sources": ["isws12", "phyto", "sare", "icar_weed"],
        },
    ],
    "Sowing season": [
        {
            "id": "stale_seedbed", "title": "Stale seedbed: let the weeds sprout first",
            "summary": "Prepare the field early and let the first flush of weeds come up. Then clear them just before you sow, so fewer weeds are left to compete with your crop.",
            "steps": [
                "Prepare the seedbed and let rain or irrigation make weed seeds sprout.",
                "Wait until you can see the weeds coming up.",
                "Clear them with very shallow tillage, or ask your agriculture officer about a suitable option.",
                "Sow without ploughing deeply, because deep tillage brings up new weed seeds.",
            ],
            "cautions": ["It reduces weeds but is not a complete answer. Use it together with mulch, cover crops and timely weeding."],
            "sources": ["icar_weed", "isws23"],
        },
        {
            "id": "cover_crops", "title": "Smother weeds with cover crops and intercrops",
            "summary": "Fast-growing crops such as sunn hemp and fodder cowpea shade out weeds. A maize and cowpea mix is another way to keep weeds down.",
            "steps": [
                "Grow sunn hemp or fodder cowpea as a cover crop before or between main crops, so that weeds get little light.",
                "In widely spaced crops, ask your KVK whether a cowpea intercrop suits your crop and season.",
                "Mulch the soil with straw or crop residue to stop weed seeds sprouting and to hold soil moisture.",
                "Pull or cut weeds before they flower. Weed problems start with weed seed in the soil, so do not let them seed.",
            ],
            "cautions": ["Local varieties and timing matter. Ask your KVK for the best cover crop for your district."],
            "sources": ["isws23", "icar_weed"],
        },
        {
            "id": "compost", "title": "Make compost from farm waste and dung",
            "summary": "Crop residue, weeds and cow dung can become compost, so you spend less on bought fertilizer.",
            "steps": [
                "Collect crop residue, dry leaves, weeds and banana stems instead of burning them. Chop or shred hard material so it rots faster.",
                "Make a heap or pit in a corner of the farm that is easy to reach. Put down alternate layers of dry waste and cow dung.",
                "Keep the heap moist like a wrung-out sponge. A dry heap stops working and a very wet heap smells bad.",
                "Turn the heap now and then to let air in. Cover it to hold in moisture.",
                "It is ready when it is dark, crumbly and smells of earth. Farm compost can take about 5 to 6 months, and less with good turning.",
                "Spread it on the soil before sowing.",
            ],
            "cautions": ["A properly managed heap gets hot, and the heat helps kill weed seeds and disease germs. Keep diseased plants and seeding weeds out of a heap you cannot keep hot."],
            "sources": ["tnau_compost", "mandya", "syscom"],
        },
        {
            "id": "fertilizer", "title": "Use fertilizer wisely",
            "summary": "Use your Soil Health Card to decide what your soil needs, and make each bag count.",
            "steps": [
                "Get a Soil Health Card first (see the Schemes and Help page) and follow its crop-wise advice.",
                "Urea sold in India is neem coated, which releases nitrogen more slowly so less is wasted. Use it as the card advises.",
                "Ask your agriculture officer which bio-fertilizer suits your crop. Government and ICAR sources list Rhizobium, Azotobacter, Azospirillum and phosphate-solubilising types, used along with other nutrient management.",
                "Check the label of every bag. Buy only from a licensed dealer.",
            ],
            "cautions": [
                "This app gives no doses. The amount comes from your Soil Health Card or agriculture officer.",
                "Bio-fertilizers are recommended but are not compulsory, and results depend on crop and soil.",
            ],
            "sources": ["pib_ncu", "icar_ncu", "ls_bio"],
        },
    ],
    "Growing season": [],
    "Harvest and storage": [
        {
            "id": "storage", "title": "Store grain safely: dry, clean and rodent-proof",
            "summary": "Damp grain rots and attracts insects, and rats and mice can empty a store. Most losses can be prevented with a few steps.",
            "steps": [
                "Dry the grain well before storing. Studies we found keep cereals at about 12 percent moisture or lower. Pulses and oilseeds differ, so ask your KVK for your crop.",
                "Clean the grain. Remove dirt, dust and broken grain before it goes in.",
                "Store in a clean, dry room or bin that rats and mice cannot get into. Stack bags on a waterproof sheet, away from the walls.",
                "Sweep up spilled grain and waste around the store, because they attract pests.",
                "Check the store often for insects, mould and droppings.",
                "Sealed hermetic bags stop insects without sprays and can keep dry grain for a year or more.",
            ],
            "cautions": [
                "Hermetic bags do not stop rats, so keep them in a rodent-proof room.",
                "Grain that is stored damp, even in a sealed bag, can still go mouldy.",
            ],
            "sources": ["icar_herm", "illinois", "tifac"],
        },
        {
            "id": "machinery", "title": "Rent machinery instead of buying it",
            "summary": "Karnataka's Krishi Yantra Dhare scheme runs Custom Hire Service Centres, so small farmers can rent tractors and harvesters at modest rates.",
            "steps": [
                "Ask your Raitha Samparka Kendra where the nearest Krishi Yantra Dhare centre is and how to book.",
                "Book early in the harvest and sowing seasons, when demand is high.",
                "Farmers using these centres pay by the acre or the hour, and do not need to own a machine.",
            ],
            "cautions": ["Booking methods and rates can change, so confirm the current process at your RSK."],
            "sources": ["kyd", "isee"],
        },
    ],
}


def germination_verdict(sprouted, tested):
    """Return (percentage, level, message). Thresholds follow Agriculture Victoria for cereal and pulse seed."""
    if tested <= 0 or sprouted < 0 or sprouted > tested:
        return None, "error", "Check the numbers. The sprouted seeds cannot be more than the seeds tested."
    pct = round(100.0 * sprouted / tested, 1)
    if pct >= 85:
        return pct, "good", "Good. This seed should do well."
    if pct >= 80:
        return pct, "ok", "Acceptable for cereal and pulse seed."
    if pct >= 70:
        return pct, "weak", "Weak. Ask your seed dealer or KVK whether to replace it or sow more thickly."
    return pct, "low", "Too low for cereal seed. Do not sow it. Ask your seed dealer about replacing it."


SRC_KN = {
    "uaex": {"title": "ಅರ್ಕಾನ್ಸಾಸ್ ವಿಶ್ವವಿದ್ಯಾಲಯ: ಮನೆಯಲ್ಲೇ ಬೀಜ ಮೊಳಕೆ ಪರೀಕ್ಷೆ", "url": "https://www.uaex.uada.edu/publications/pdf/FSA-3149.pdf"},
    "nrcs": {"title": "ಯುಎಸ್‌ಡಿಎ {USDA} ನೈಸರ್ಗಿಕ ಸಂಪನ್ಮೂಲ ಸಂರಕ್ಷಣಾ ಸಂಸ್ಥೆ: ರಾಗ್-ಡಾಲ್ ಪರೀಕ್ಷೆ", "url": "https://www.nrcs.usda.gov/plantmaterials/mspmctn4808.pdf"},
    "vic": {"title": "ಅಗ್ರಿಕಲ್ಚರ್ ವಿಕ್ಟೋರಿಯಾ: ಬಿತ್ತನೆ ಬೆಳೆ ಬೀಜಗಳ ಪರೀಕ್ಷಾ ವಿಧಾನ", "url": "https://agriculture.vic.gov.au/crops-and-horticulture/grains-pulses-and-cereals/crop-production/general-agronomy/testing-crop-seed-for-sowing"},
    "ucd": {"title": "ಯುಸಿ ಡೇವಿಸ್ {UC Davis}: ಬೀಜ ಮೊಳಕೆ ಪರೀಕ್ಷಾ ಕೈಪಿಡಿ", "url": "https://epakag.ucdavis.edu/vocational_training/factsheets/fs-seed-germination-test-ragdoll.pdf"},
    "icar_weed": {"title": "ಐಸಿಎಆರ್ {ICAR} ಇಂಡಿಯನ್ ಫಾರ್ಮಿಂಗ್: ಕಳೆ ನಿರ್ವಹಣಾ ತಂತ್ರಗಳು", "url": "https://epubs.icar.org.in/index.php/IndFarm/article/download/165717/59653/457864"},
    "isws23": {"title": "ಭಾರತೀಯ ಕಳೆ ವಿಜ್ಞಾನ ಜರ್ನಲ್ 2023: ಹತ್ತಿಯಲ್ಲಿ ಹಳೆಯ ಬೀಜಪಾತಿ ಮತ್ತು ದ್ವಿದಳ ಹೊದಿಕೆ ಬೆಳೆಗಳು", "url": "https://www.isws.org.in/IJWSn/File/2023_55_Issue-1_46-49.pdf"},
    "isws12": {"title": "ಭಾರತೀಯ ಕಳೆ ವಿಜ್ಞಾನ ಜರ್ನಲ್ 2012: ಮಣ್ಣಿನ ಸೌರೀಕರಣ ಮತ್ತು ಕಳೆ ನಿಯಂತ್ರಣ", "url": "https://www.isws.org.in/IJWSn/File/2012_44_Issue-2_122-123.pdf"},
    "phyto": {"title": "ಜರ್ನಲ್ ಆಫ್ ಫಾರ್ಮಾಕಾಗ್ನಸಿ: ಬೇಸಿಗೆಯ ಮಣ್ಣಿನ ಸೌರೀಕರಣ", "url": "https://phytojournal.com/archives/2019/vol8issue3/PartZ/8-2-282-705.pdf"},
    "sare": {"title": "ಸಸ್ಟೈನಬಲ್ ಅಗ್ರಿಕಲ್ಚರ್ ರಿಸರ್ಚ್ {SARE}: ಕೋರೆ ಹುಲ್ಲು ನಿರ್ವಹಣೆ", "url": "https://www.sare.org/publications/manage-weeds-on-your-farm/purple-nutsedge"},
    "tnau_compost": {"title": "ಟಿಎನ್‌ಎಯು {TNAU} ಅಗ್ರಿಟೆಕ್ ಪೋರ್ಟಲ್: ಕಾಂಪೋಸ್ಟ್ ಗೊಬ್ಬರ ತಯಾರಿಕೆ", "url": "https://agritech.tnau.ac.in/org_farm/orgfarm_composting.html"},
    "mandya": {"title": "ಆರ್ಗ್ಯಾನಿಕ್ ಮಂಡ್ಯ: ಕೃಷಿ ತ್ಯಾಜ್ಯ ಮತ್ತು ಸಗಣಿಯಿಂದ ನೈಸರ್ಗಿಕ ಕಾಂಪೋಸ್ಟ್", "url": "https://organicmandya.com/blogs/news/how-to-prepare-free-compost-from-farm-waste-and-cow-manure-the-organic-mandya-way"},
    "syscom": {"title": "ಫಿಬಿಎಲ್ ಸಿಸ್‌ಕಾಮ್ {FiBL SysCom}: ಗುಣಮಟ್ಟದ ಕಾಂಪೋಸ್ಟ್ ಕೈಪಿಡಿ", "url": "https://systems-comparison.fibl.org/fileadmin/syscom/documents/Leaflets/Kenya/SysComKenya_leaflet_composting.pdf"},
    "pib_ncu": {"title": "ಪಿಐಬಿ {PIB}: ಬೇವಿನ ಲೇಪಿತ ಯೂರಿಯಾ ಮಾಹಿತಿ", "url": "https://static.pib.gov.in/WriteReadData/specificdocs/documents/2021/sep/Neem%20Coated%20.pdf"},
    "icar_ncu": {"title": "ಐಸಿಎಆರ್ {ICAR}: ಬೇವಿನ ಲೇಪಿತ ಯೂರಿಯಾದ ಪರಿಣಾಮಕಾರಿ ಬಳಕೆ", "url": "https://epubs.icar.org.in/index.php/IJAgS/article/download/122695/46653/332869"},
    "ls_bio": {"title": "ಲೋಕಸಭಾ ಅಧಿಕೃತ ವರದಿ: ಜೈವಿಕ ಗೊಬ್ಬರಗಳ ಬಳಕೆ", "url": "https://eparlib.nic.in/bitstream/123456789/1468786/1/AU855.pdf"},
    "icar_herm": {"title": "ಐಸಿಎಆರ್ {ICAR} ಇಂಡಿಯನ್ ಫಾರ್ಮಿಂಗ್: ಧಾನ್ಯ ಸಂಗ್ರಹಣೆಯಲ್ಲಿ ಹರ್ಮೆಟಿಕ್ ತಂತ್ರಜ್ಞಾನ", "url": "https://epubs.icar.org.in/index.php/IndFarm/article/download/103521/40557/267105"},
    "illinois": {"title": "ಇಲಿನಾಯ್ಸ್ ವಿಶ್ವವಿದ್ಯಾಲಯ: ಸುಧಾರಿತ ಧಾನ್ಯ ನಿರ್ವಹಣಾ ವ್ಯವಸ್ಥೆ", "url": "https://postharvestinstitute.illinois.edu/?p=7915"},
    "tifac": {"title": "ಟೈಫಾಕ್ {TIFAC}: ಧಾನ್ಯ ಸಂಗ್ರಹಣಾ ನಷ್ಟ ತಗ್ಗಿಸುವ ತಂತ್ರಜ್ಞಾನಗಳು", "url": "https://tifac.org.in/index.php/programmes/activities/8-publication/157-technologies-to-minimise-grain-storage-loss?start=4"},
    "kyd": {"title": "ಎಸ್‌ಡಿಎಂ ಇನ್‌ಸ್ಟಿಟ್ಯೂಟ್: ಕರ್ನಾಟಕದ ಕೃಷಿ ಯಂತ್ರಧಾರೆ ಯೋಜನೆಯ ಅಧ್ಯಯನ ವರದಿ", "url": "https://www.sdmimd.ac.in/conferenceproceedings/iec2025papers/IEC25201.pdf"},
    "isee": {"title": "ವಿಸ್ತರಣಾ ಶಿಕ್ಷಣ ಜರ್ನಲ್: ಕಸ್ಟಮ್ ಹೈರಿಂಗ್ ಕೇಂದ್ರಗಳ ರೈತ ಅಧ್ಯಯನ", "url": "https://epubs.icar.org.in/index.php/IJEE/article/view/122625"},
}

STAGES_KN = ["ಬಿತ್ತನೆಗೆ ಮುನ್ನ", "ಬಿತ್ತನೆ ಕಾಲ", "ಬೆಳವಣಿಗೆ ಕಾಲ", "ಕೊಯ್ಲು ಮತ್ತು ಸಂಗ್ರಹಣೆ"]

ITEMS_KN = {
    "ಬಿತ್ತನೆಗೆ ಮುನ್ನ": [
        {
            "id": "seed_test",
            "title": "ಬಿತ್ತನೆಗೆ ಮುನ್ನ ಬೀಜದ ಮೊಳಕೆ ಪರೀಕ್ಷೆ ಮಾಡಿ",
            "summary": "ಇಡೀ ಜಮೀನಿನಲ್ಲಿ ಬಿತ್ತನೆ ಮಾಡಿ ಹಣ ಮತ್ತು ಶ್ರಮ ವ್ಯರ್ಥ ಮಾಡುವ ಮುನ್ನ, ಮನೆಯಲ್ಲೇ ಸರಳ ಪರೀಕ್ಷೆ ಮೂಲಕ ಎಷ್ಟು ಬೀಜಗಳು ಮೊಳಕೆಯೊಡೆಯುತ್ತವೆ ಎಂಬುದನ್ನು ಖಚಿತಪಡಿಸಿಕೊಳ್ಳಿ.",
            "steps": [
                "ಬೀಜದ ರಾಶಿಯನ್ನು ಚೆನ್ನಾಗಿ ಬೆರೆಸಿ ಯಾದೃಚ್ಛಿಕವಾಗಿ 100 ಬೀಜಗಳನ್ನು ಆರಿಸಿ. ಇಡೀ ರಾಶಿಯ ನೈಜ ಸ್ಥಿತಿ ತಿಳಿಯಲು ಸಣ್ಣ, ಒಡೆದ ಮತ್ತು ಬಣ್ಣಗೆಟ್ಟ ಬೀಜಗಳನ್ನೂ ಒಳಗೊಂಡಿರಿ.",
                "ದಪ್ಪವಾದ ಕಾಗದದ ಟವೆಲ್ ಅಥವಾ ಹತ್ತಿ ಬಟ್ಟೆಯನ್ನು ಒದ್ದೆ ಮಾಡಿ ಹೆಚ್ಚುವರಿ ನೀರನ್ನು ಹಿಂಡಿ ತೆಗೆಯಿರಿ. ಅತಿ ಮೃದುವಾದ ಅಡುಗೆಮನೆಯ ಪೇಪರ್ ಬೇಡ, ಏಕೆಂದರೆ ಬೇರುಗಳು ಅದರಲ್ಲಿ ಸಿಕ್ಕಿಹಾಕಿಕೊಳ್ಳುತ್ತವೆ.",
                "ಬೀಜಗಳನ್ನು ಬಟ್ಟೆಯ ಮೇಲೆ ಸಮನಾಗಿ ಹರಡಿ, ಸಡಿಲವಾಗಿ ಸುತ್ತಿ ಪ್ಲಾಸ್ಟಿಕ್ ಚೀಲದಲ್ಲಿಟ್ಟು ಬೆಚ್ಚಗಿನ ಸ್ಥಳದಲ್ಲಿಡಿ.",
                "ಬಟ್ಟೆ ಸದಾ ತೇವವಾಗಿರುವಂತೆ ನೋಡಿಕೊಳ್ಳಿ, ಆದರೆ ಹೆಚ್ಚು ನೀರು ನಿಲ್ಲಿಸಬೇಡಿ. ಅತಿಯಾದ ನೀರು ಗಾಳಿಯಾಡುವುದನ್ನು ತಡೆದು ಬೀಜ ಹಾಳುಮಾಡುತ್ತದೆ.",
                "ಸುಮಾರು 4 ದಿನಗಳ ನಂತರ ತೆರೆದು, ಮೊಳಕೆಯೊಡೆದ ಬೀಜಗಳನ್ನು ಎಣಿಸಿ ಪ್ರತ್ಯೇಕಿಸಿ. ನಂತರ ಇನ್ನೂ 3 ರಿಂದ 4 ದಿನಗಳ ನಂತರ ಪುನಃ ಎಣಿಕೆ ಮಾಡಿ.",
                "100 ಬೀಜಗಳಲ್ಲಿ ಮೊಳಕೆಯೊಡೆದ ಬೀಜಗಳ ಒಟ್ಟು ಸಂಖ್ಯೆಯೇ ಮೊಳಕೆ ಶೇಕಡಾವಾರು ಆಗಿರುತ್ತದೆ. 100 ಬೀಜಗಳ 3 ಪ್ರತ್ಯೇಕ ಗುಂಪುಗಳಲ್ಲಿ ಪರೀಕ್ಷಿಸಿದರೆ ಹೆಚ್ಚು ನಿಖರ ಫಲಿತಾಂಶ ಸಿಗುತ್ತದೆ.",
            ],
            "cautions": ["ಕೆಲವು ಬೆಳೆಗಳಿಗೆ ಹೆಚ್ಚು ದಿನಗಳು ಬೇಕಾಗಬಹುದು ಮತ್ತು ಗಟ್ಟಿ ಸಿಪ್ಪೆಯ ಬೀಜಗಳು ನಿಧಾನವಾಗಿ ಮೊಳಕೆಯೊಡೆಯುತ್ತವೆ. ನಿಮ್ಮ ಬೆಳೆಗೆ ತಕ್ಕಂತೆ {KVK} ಅಥವಾ ಬೀಜ ಮಾರಾಟಗಾರರನ್ನು ಕೇಳಿ."],
            "sources": ["uaex", "nrcs", "vic", "ucd"],
        },
        {
            "id": "summer_plough",
            "title": "ಬೇಸಿಗೆಯ ಆಳವಾದ ಉಳುಮೆ ಮತ್ತು ಸೌರೀಕರಣ {ಸೋಲರೈಸೇಶನ್}",
            "summary": "ಬೇಸಿಗೆಯ ಬಿಸಿಲಿನ ತಾಪವನ್ನು ಬಳಸಿ ಮಣ್ಣಿನಲ್ಲಿರುವ ಕಳೆ ಬೀಜಗಳು, ರೋಗಾಣುಗಳು ಮತ್ತು ಕೋರೆ ಹುಲ್ಲಿನಂತಹ ಹಾನಿಕಾರಕ ಗೆಡ್ಡೆಗಳನ್ನು ಒಣಗಿಸಿ ನಾಶಪಡಿಸಬಹುದು.",
            "steps": [
                "ಬೇಸಿಗೆಯ ಬಿಸಿಲಿನಲ್ಲಿ ಜಮೀನನ್ನು ಆಳವಾಗಿ ಉಳುಮೆ ಮಾಡಿ, 3 ರಿಂದ 4 ವಾರಗಳ ನಂತರ ಮತ್ತೆ ಉಳುಮೆ ಮಾಡಿ; ಇದರಿಂದ ಬೇರುಗಳು ಮತ್ತು ಗೆಡ್ಡೆಗಳು ಮೇಲೆ ಬಂದು ಬಿಸಿಲಿಗೆ ಒಣಗುತ್ತವೆ.",
                "ಮಣ್ಣಿನ ಸೌರೀಕರಣಕ್ಕಾಗಿ {ಸೋಲರೈಸೇಶನ್}: ಮಣ್ಣನ್ನು ಹದವಾಗಿ ತೇವಗೊಳಿಸಿ, ಅತಿ ಹೆಚ್ಚು ಬಿಸಿಲಿರುವ ವಾರಗಳಲ್ಲಿ ಪಾರದರ್ಶಕ ಬಿಳಿ ಪಾಲಿಥೀನ್ ಶೀಟ್‌ನಿಂದ ಗಾಳಿಯಾಡದಂತೆ ಬಿಗಿಯಾಗಿ ಮುಚ್ಚಿ. ಭಾರತೀಯ ಅಧ್ಯಯನಗಳ ಪ್ರಕಾರ 40 ದಿನಗಳ ಸೌರೀಕರಣ ಅತ್ಯುತ್ತಮ ಫಲಿತಾಂಶ ನೀಡುತ್ತದೆ.",
                "ಹಾಳೆಯನ್ನು ಆಗಾಗ ಪರಿಶೀಲಿಸಿ ರಂಧ್ರಗಳಿದ್ದರೆ ಸರಿಪಡಿಸಿ. ಪ್ರಾಣಿಗಳು ಮತ್ತು ಜನರನ್ನು ಅದರ ಮೇಲೆ ಹೋಗದಂತೆ ನೋಡಿಕೊಳ್ಳಿ.",
            ],
            "cautions": [
                "ವೈಜ್ಞಾನಿಕ ಅಧ್ಯಯನಗಳಲ್ಲಿ ತಿಳಿಸಿದಂತೆ ಸ್ಪಷ್ಟ ಪಾರದರ್ಶಕ ಪ್ಲಾಸ್ಟಿಕ್ ಹಾಳೆಯನ್ನೇ ಬಳಸಿ.",
                "ಯಾವುದೇ ಒಂದೇ ಪದ್ಧತಿ ಕಳೆಯನ್ನು ಶಾಶ್ವತವಾಗಿ ನಿವಾರಿಸುವುದಿಲ್ಲ. ಇತರ ಪದ್ಧತಿಗಳ ಜೊತೆಗೆ ಸಂಯೋಜಿಸಿದರೆ 2 ರಿಂದ 3 ಋತುಗಳಲ್ಲಿ ಕಳೆಗಳ ಸಂಖ್ಯೆ ಗಣನೀಯವಾಗಿ ಕಡಿಮೆಯಾಗುತ್ತದೆ.",
            ],
            "sources": ["isws12", "phyto", "sare", "icar_weed"],
        },
    ],
    "ಬಿತ್ತನೆ ಕಾಲ": [
        {
            "id": "stale_seedbed",
            "title": "ಹಳೆಯ ಬೀಜಪಾತಿ ಪದ್ಧತಿ: ಮೊದಲು ಕಳೆಗಳು ಮೊಳಕೆಯೊಡೆಯಲು ಬಿಡಿ",
            "summary": "ಮುಖ್ಯ ಬೆಳೆ ಬಿತ್ತನೆಗೆ ಮೊದಲೇ ಜಮೀನು ಸಿದ್ಧಪಡಿಸಿ ಕಳೆಗಳು ಮೊದಲು ಮೊಳಕೆಯೊಡೆಯಲು ಬಿಡಿ. ನಂತರ ಬಿತ್ತನೆಗೆ തൊಟ್ಟುಮುಂಚೆ ಅವುಗಳನ್ನು ನಾಶಪಡಿಸಿ, ಇದರಿಂದ ಬೆಳೆಯೊಂದಿಗೆ ಕಳೆಗಳ ಪೈಪೋಟಿ ಕಡಿಮೆಯಾಗುತ್ತದೆ.",
            "steps": [
                "ಬೀಜಪಾತಿಯನ್ನು ಸಿದ್ಧಪಡಿಸಿ ಮಳೆ ಅಥವಾ ಹಗುರ ನೀರಾವರಿ ಮೂಲಕ ಕಳೆ ಬೀಜಗಳು ಮೊಳಕೆಯೊಡೆಯುವಂತೆ ಮಾಡಿ.",
                "ಕಳೆಗಳು ಮೇಲಕ್ಕೆ ಬರುವವರೆಗೆ ಕಾಯಿರಿ.",
                "ಮೇಲ್ಮೈಯ ಅತ್ಯಂತ ಹಗುರವಾದ ಉಳುಮೆಯ ಮೂಲಕ ಕಳೆಗಳನ್ನು ಕಿತ್ತು ಹಾಕಿ, ಅಥವಾ ಕೃಷಿ ಅಧಿಕಾರಿಗಳ ಸಲಹೆಯಂತೆ ಸೂಕ್ತ ವಿಧಾನ ಬಳಸಿ.",
                "ಆಳವಾದ ಉಳುಮೆ ಮಾಡದೆ ನೇರವಾಗಿ ಬಿತ್ತನೆ ಮಾಡಿ, ಏಕೆಂದರೆ ಆಳವಾದ ಉಳುಮೆಯಿಂದ ಕೆಳಗಿರುವ ಹೊಸ ಕಳೆ ಬೀಜಗಳು ಮೇಲೆ ಬರುತ್ತವೆ.",
            ],
            "cautions": ["ಇದು ಕಳೆಗಳನ್ನು ಕಡಿಮೆ ಮಾಡುತ್ತದೆ ಆದರೆ ಸಂಪೂರ್ಣ ಪರಿಹಾರವಲ್ಲ. ಮಲ್ಚಿಂಗ್, ಹೊದಿಕೆ ಬೆಳೆಗಳು ಮತ್ತು ಸಮಯಕ್ಕೆ ಸರಿಯಾಗಿ ಕಳೆ ಕೀಳುವ ವಿಧಾನಗಳೊಂದಿಗೆ ಸಂಯೋಜಿಸಿ."],
            "sources": ["icar_weed", "isws23"],
        },
        {
            "id": "cover_crops",
            "title": "ಹೊದಿಕೆ ಬೆಳೆಗಳು ಮತ್ತು ಅಂತರಬೆಳೆಗಳ ಮೂಲಕ ಕಳೆ ನಿಗ್ರಹ",
            "summary": "ಸಣಬು ಮತ್ತು ಮೇವಿನ ಅಲಸಂದಿಯಂತಹ ವೇಗವಾಗಿ ಬೆಳೆಯುವ ಬೆಳೆಗಳು ನೆಲವನ್ನು ಆವರಿಸಿ ಕಳೆಗಳಿಗೆ ಬಿಸಿಲು ಸಿಗದಂತೆ ಮಾಡಿ ಕಳೆಗಳನ್ನು ನಾಶಪಡಿಸುತ್ತವೆ.",
            "steps": [
                "ಮುಖ್ಯ ಬೆಳೆಗಳ ಮುನ್ನ ಅಥವಾ ಮಧ್ಯದಲ್ಲಿ ಸಣಬು ಅಥವಾ ಮೇವಿನ ಅಲಸಂದಿಯನ್ನು ಹೊದಿಕೆ ಬೆಳೆಯಾಗಿ ಬೆಳೆಯಿರಿ, ಇದರಿಂದ ಕಳೆಗಳಿಗೆ ಬೆಳಕು ಸಿಗುವುದಿಲ್ಲ.",
                "ಹೆಚ್ಚು ಅಂತರವಿರುವ ಸಾಲು ಬೆಳೆಗಳಲ್ಲಿ ನಿಮ್ಮ ಜಿಲ್ಲೆಯ ಋತುವಿಗೆ ಅಲಸಂದಿ ಅಂತರಬೆಳೆ ಸೂಕ್ತವೇ ಎಂದು ಕೃಷಿ ವಿಜ್ಞಾನ ಕೇಂದ್ರವನ್ನು {KVK} ವಿಚಾರಿಸಿ.",
                "ಕಳೆ ಬೀಜಗಳು ಮೊಳಕೆಯೊಡೆಯುವುದನ್ನು ತಡೆಯಲು ಮತ್ತು ಮಣ್ಣಿನ ತೇವಾಂಶ ಉಳಿಸಲು ಕೃಷಿ ತ್ಯಾಜ್ಯ ಅಥವಾ ಒಣಹುಲ್ಲಿನಿಂದ ಮಲ್ಚಿಂಗ್ ಮಾಡಿ.",
                "ಕಳೆಗಳು ಹೂ ಬಿಡುವ ಮೊದಲೇ ಕಿತ್ತು ತೆಗೆಯಿರಿ; ಕಳೆಗಳು ಬೀಜ ಬಿಡಲು ಬಿಡಬೇಡಿ.",
            ],
            "cautions": ["ಸ್ಥಳೀಯ ತಳಿಗಳು ಮತ್ತು ಬಿತ್ತನೆಯ ಸಮಯ ಮುಖ್ಯ. ನಿಮ್ಮ ಜಿಲ್ಲೆಗೆ ಉತ್ತಮವಾದ ಹೊದಿಕೆ ಬೆಳೆಗಾಗಿ {KVK} ಸಂಪರ್ಕಿಸಿ."],
            "sources": ["isws23", "icar_weed"],
        },
        {
            "id": "compost",
            "title": "ಕೃಷಿ ತ್ಯಾಜ್ಯ ಮತ್ತು ಸಗಣಿಯಿಂದ ನೈಸರ್ಗಿಕ ಕಾಂಪೋಸ್ಟ್ ಗೊಬ್ಬರ ತಯಾರಿಕೆ",
            "summary": "ಬೆಳೆ ತ್ಯಾಜ್ಯ, ಒಣ ಎಲೆಗಳು ಮತ್ತು ಸಗಣಿಯನ್ನು ಕಾಂಪೋಸ್ಟ್ ಆಗಿ ಪರಿವರ್ತಿಸಿ, ಹೊರಗಿನಿಂದ ಖರೀದಿಸುವ ದುಬಾರಿ ಗೊಬ್ಬರದ ವೆಚ್ಚವನ್ನು ತಗ್ಗಿಸಿ.",
            "steps": [
                "ಬೆಳೆ ತ್ಯಾಜ್ಯ, ಒಣ ಎಲೆಗಳು, ಕಳೆಗಳು ಮತ್ತು ಬಾಳೆ ದಿಂಡುಗಳನ್ನು ಸುಡುವ ಬದಲು ಸಂಗ್ರಹಿಸಿ. ಬೇಗ ಕೊಳೆಯಲು ಗಟ್ಟಿಯಾದ ತ್ಯಾಜ್ಯವನ್ನು ತುಂಡರಿಸಿ.",
                "ಜಮೀನಿನ ಸುಲಭವಾಗಿ ತಲುಪಬಹುದಾದ ಮೂಲೆಯಲ್ಲಿ ಗುಂಡಿ ಅಥವಾ ರಾಶಿ ಮಾಡಿ. ಒಣ ತ್ಯಾಜ್ಯ ಮತ್ತು ಸಗಣಿಯ ಪದರಗಳನ್ನು ಒಂದರ ಮೇಲೊಂದು ಜೋಡಿಸಿ.",
                "ರಾಶಿಯನ್ನು ಹಿಂಡಿದ ಸ್ಪಂಜಿನಂತೆ ಹದವಾಗಿ ತೇವವಾಗಿಡಿ. ತೇವಾಂಶ ಇಲ್ಲದಿದ್ದರೆ ಕೊಳೆಯುವುದು ನಿಲ್ಲುತ್ತದೆ, ಅತಿಯಾದ ನೀರಿದ್ದರೆ ದುರ್ವಾಸನೆ ಬರುತ್ತದೆ.",
                "ಗಾಳಿಯಾಡಲು ಆಗಾಗ ರಾಶಿಯನ್ನು ತಿರುವಿ ಹಾಕಿ. ತೇವಾಂಶ ಆವಿಯಾಗದಂತೆ ಮೇಲೆ ಮುಚ್ಚಿಡಿ.",
                "ಗೊಬ್ಬರವು ಕಪ್ಪು ಬಣ್ಣಕ್ಕೆ ತಿರುಗಿ, ಪುಡಿಯಾಗಿ, ಮಣ್ಣಿನ ಸುವಾಸನೆ ಬಂದಾಗ ಸಿದ್ಧವಾಗುತ್ತದೆ. ಇದಕ್ಕೆ ಸುಮಾರು 5 ರಿಂದ 6 ತಿಂಗಳು ಬೇಕಾಗುತ್ತದೆ.",
                "ಬಿತ್ತನೆಗೆ ಮುನ್ನ ಜಮೀನಿಗೆ ಸಮನಾಗಿ ಹರಡಿ ಮಣ್ಣಿನಲ್ಲಿ ಬೆರೆಸಿ.",
            ],
            "cautions": ["ಸರಿಯಾಗಿ ನಿರ್ವಹಿಸಿದ ರಾಶಿಯಲ್ಲಿ ಶಾಖ ಉತ್ಪತ್ತಿಯಾಗುತ್ತದೆ; ಈ ಶಾಖವು ಕಳೆ ಬೀಜಗಳು ಮತ್ತು ರೋಗಾಣುಗಳನ್ನು ಕೊಲ್ಲಲು ನೆರವಾಗುತ್ತದೆ. ಶಾಖ ಉತ್ಪತ್ತಿಯಾಗದ ರಾಶಿಗೆ ರೋಗಪೀಡಿತ ಗಿಡಗಳನ್ನು ಹಾಕಬೇಡಿ."],
            "sources": ["tnau_compost", "mandya", "syscom"],
        },
        {
            "id": "fertilizer",
            "title": "ರಸಗೊಬ್ಬರವನ್ನು ಜಾಣ್ಮೆಯಿಂದ ಬಳಸಿ ವೆಚ್ಚ ಉಳಿಸಿ",
            "summary": "ನಿಮ್ಮ ಮಣ್ಣು ಆರೋಗ್ಯ ಕಾರ್ಡ್ {Soil Health Card} ಆಧರಿಸಿ ಮಣ್ಣಿಗೆ ಅಗತ್ಯವಿರುವಷ್ಟೇ ಗೊಬ್ಬರ ನೀಡಿ, ಪ್ರತಿ ಚೀಲದ ಹಣಕ್ಕೂ ಸರಿಯಾದ ಇಳುವರಿ ಪಡೆಯಿರಿ.",
            "steps": [
                "ಮೊದಲು ಮಣ್ಣು ಆರೋಗ್ಯ ಕಾರ್ಡ್ ಪಡೆಯಿರಿ ಮತ್ತು ಅದರಲ್ಲಿ ಶಿಫಾರಸು ಮಾಡಿದ ಬೆಳೆವಾರು ಪ್ರಮಾಣವನ್ನು ಅನುಸರಿಸಿ.",
                "ಭಾರತದಲ್ಲಿ ಮಾರಾಟವಾಗುವ ಯೂರಿಯಾ ಬೇವಿನ ಲೇಪಿತವಾಗಿರುತ್ತದೆ {Neem Coated Urea}; ಇದು ಸಾರಜನಕವನ್ನು ನಿಧಾನವಾಗಿ ಬಿಡುಗಡೆ ಮಾಡಿ ನಷ್ಟವಾಗುವುದನ್ನು ತಪ್ಪಿಸುತ್ತದೆ.",
                "ನಿಮ್ಮ ಬೆಳೆಗೆ ಯಾವ ಜೈವಿಕ ಗೊಬ್ಬರ {Bio-fertilizer} ಸೂಕ್ತವೆಂದು ಕೃಷಿ ಅಧಿಕಾರಿಯನ್ನು ಕೇಳಿ. ರೈಜೋಬಿಯಂ, ಅಜೋಟೋಬ್ಯಾಕ್ಟರ್, ಅಜೋಸ್ಪೈರಿಲಮ್ ಮತ್ತು ರಂಜಕ ಕರಗಿಸುವ ಬ್ಯಾಕ್ಟೀರಿಯಾಗಳನ್ನು ಇತರ ಪೋಷಕಾಂಶಗಳ ಜೊತೆಗೆ ಬಳಸಿ.",
                "ಪ್ರತಿ ಚೀಲದ ಲೇಬಲ್ ಪರಿಶೀಲಿಸಿ. ಪರವಾನಗಿ ಪಡೆದ ಅಧಿಕೃತ ಡೀಲರ್ ಬಳಿಯೇ ಖರೀದಿಸಿ.",
            ],
            "cautions": [
                "ಈ ಆ್ಯಪ್ ಯಾವುದೇ ನಿರ್ದಿಷ್ಟ ಪ್ರಮಾಣ ನೀಡುವುದಿಲ್ಲ. ಪ್ರಮಾಣವನ್ನು ನಿಮ್ಮ ಮಣ್ಣು ಆರೋಗ್ಯ ಕಾರ್ಡ್ ಅಥವಾ ಕೃಷಿ ಅಧಿಕಾರಿಯಿಂದ ಪಡೆಯಿರಿ.",
                "ಜೈವಿಕ ಗೊಬ್ಬರಗಳನ್ನು ಶಿಫಾರಸು ಮಾಡಲಾಗುತ್ತದೆ, ಆದರೆ ಅವುಗಳ ಫಲಿತಾಂಶ ಬೆಳೆ ಮತ್ತು ಮಣ್ಣಿನ ಮೇಲೆ ಅವಲಂಬಿತವಾಗಿರುತ್ತದೆ.",
            ],
            "sources": ["pib_ncu", "icar_ncu", "ls_bio"],
        },
    ],
    "ಬೆಳವಣಿಗೆ ಕಾಲ": [],
    "ಕೊಯ್ಲು ಮತ್ತು ಸಂಗ್ರಹಣೆ": [
        {
            "id": "storage",
            "title": "ಧಾನ್ಯವನ್ನು ಸುರಕ್ಷಿತವಾಗಿ ಸಂಗ್ರಹಿಸಿ: ಒಣ, ಸ್ವಚ್ಛ ಮತ್ತು ಕೀಟ-ಇಲಿಗಳಿಂದ ಮುಕ್ತ",
            "summary": "ತೇವಾಂಶವಿರುವ ಧಾನ್ಯ ಕೊಳೆಯುತ್ತದೆ ಮತ್ತು ಕೀಟಗಳನ್ನು ಆಕರ್ಷಿಸುತ್ತದೆ; ಇಲಿ-ಹೆಗ್ಗಣಗಳು ಧಾನ್ಯದ ದಾಸ್ತಾನನ್ನು ಹಾಳುಮಾಡುತ್ತವೆ. ಸರಳ ಮುನ್ನೆಚ್ಚರಿಕೆಯಿಂದ ಹೆಚ್ಚಿನ ನಷ್ಟವನ್ನು ತಡೆಯಬಹುದು.",
            "steps": [
                "ಧಾನ್ಯವನ್ನು ಸಂಗ್ರಹಿಸುವ ಮೊದಲು ಚೆನ್ನಾಗಿ ಒಣಗಿಸಿ. ಧಾನ್ಯಗಳಲ್ಲಿ ಸುಮಾರು 12% ಅಥವಾ ಅದಕ್ಕಿಂತ ಕಡಿಮೆ ತೇವಾಂಶವಿರಬೇಕು. ಬೇಳೆಕಾಳು ಮತ್ತು ಎಣ್ಣೆಕಾಳುಗಳಿಗೆ ಇದು ಬೇರೆಯಾಗಿರುತ್ತದೆ, ನಿಮ್ಮ {KVK} ಯನ್ನು ಕೇಳಿ.",
                "ಧಾನ್ಯವನ್ನು ಚೆನ್ನಾಗಿ ಸ್ವಚ್ಛಗೊಳಿಸಿ. ಧೂಳು, ಕಸ ಮತ್ತು ಒಡೆದ ಧಾನ್ಯಗಳನ್ನು ಬೇರ್ಪಡಿಸಿ.",
                "ಇಲಿಗಳು ಪ್ರವೇಶಿಸಲಾಗದ ಸ್ವಚ್ಛ, ಒಣ ಕೋಣೆಯಲ್ಲಿ ಸಂಗ್ರಹಿಸಿ. ಚೀಲಗಳನ್ನು ಗೋಡೆಯಿಂದ ದೂರವಿರಿಸಿ, ನೀರಿನ ಸೋರಿಕೆ ತಡೆಯಲು ಪ್ಲಾಸ್ಟಿಕ್ ಶೀಟ್ ಮೇಲೆ ಜೋಡಿಸಿ.",
                "ದಾಸ್ತಾನು ಕೋಣೆಯ ಸುತ್ತಲೂ ಚೆಲ್ಲಿದ ಧಾನ್ಯವನ್ನು ಗುಡಿಸಿ ಸ್ವಚ್ಛವಾಗಿಡಿ; ಚೆಲ್ಲಿದ ಧಾನ್ಯವು ಕೀಟ ಮತ್ತು ಇಲಿಗಳನ್ನು ಆಕರ್ಷಿಸುತ್ತದೆ.",
                "ಕೀಟಗಳು, ಶಿಲೀಂಧ್ರ ಅಥವಾ ಇಲಿ ಹಿಕ್ಕೆಯ ಲಕ್ಷಣಗಳಿಗಾಗಿ ದಾಸ್ತಾನನ್ನು ಆಗಾಗ ಪರಿಶೀಲಿಸಿ.",
                "ಗಾಳಿಯಾಡದ ಹರ್ಮೆಟಿಕ್ ಚೀಲಗಳು {Hermetic Bags} ಕೀಟನಾಶಕ ಸಿಂಪಡಣೆ ಇಲ್ಲದೆಯೇ ಕೀಟಗಳನ್ನು ತಡೆಯುತ್ತವೆ ಮತ್ತು ಒಂದು ವರ್ಷಕ್ಕೂ ಹೆಚ್ಚು ಕಾಲ ಧಾನ್ಯವನ್ನು ಸುರಕ್ಷಿತವಾಗಿಡುತ್ತವೆ.",
            ],
            "cautions": [
                "ಹರ್ಮೆಟಿಕ್ ಚೀಲಗಳು ಇಲಿಗಳನ್ನು ತಡೆಯುವುದಿಲ್ಲ, ಆದ್ದರಿಂದ ಅವುಗಳನ್ನು ಇಲಿ ಮುಕ್ತ ಕೋಣೆಯಲ್ಲಿಯೇ ಇರಿಸಿ.",
                "ತೇವವಿರುವ ಧಾನ್ಯವನ್ನು ಗಾಳಿಯಾಡದ ಚೀಲದಲ್ಲಿಟ್ಟರೂ ಬೂಷ್ಟು ಬೆಳೆಯುವ ಸಾಧ್ಯತೆ ಇರುತ್ತದೆ.",
            ],
            "sources": ["icar_herm", "illinois", "tifac"],
        },
        {
            "id": "machinery",
            "title": "ಖರೀದಿಸುವ ಬದಲು ಕೃಷಿ ಯಂತ್ರಗಳನ್ನು ಬಾಡಿಗೆಗೆ ಪಡೆಯಿರಿ {ಕೃಷಿ ಯಂತ್ರಧಾರೆ}",
            "summary": "ಕರ್ನಾಟಕ ಸರ್ಕಾರದ ಕೃಷಿ ಯಂತ್ರಧಾರೆ ಯೋಜನೆಯಡಿ ಕಸ್ಟಮ್ ಹೈರ್ ಸೇವಾ ಕೇಂದ್ರಗಳು ಕಾರ್ಯನಿರ್ವಹಿಸುತ್ತಿದ್ದು, ಸಣ್ಣ ಮತ್ತು ಅತಿ ಸಣ್ಣ ರೈತರು ಟ್ರ್ಯಾಕ್ಟರ್ ಮತ್ತು ಕಟಾವು ಯಂತ್ರಗಳನ್ನು ರಿಯಾಯಿತಿ ದರದಲ್ಲಿ ಬಾಡಿಗೆಗೆ ಪಡೆಯಬಹುದು.",
            "steps": [
                "ನಿಮ್ಮ ಸಮೀಪದ ಕೃಷಿ ಯಂತ್ರಧಾರೆ ಕೇಂದ್ರ ಎಲ್ಲಿದೆ ಮತ್ತು ಮುಂಗಡ ಕಾಯ್ದಿರಿಸುವುದು ಹೇಗೆ ಎಂದು ರೈತ ಸಂಪರ್ಕ ಕೇಂದ್ರದಲ್ಲಿ {RSK} ವಿಚಾರಿಸಿ.",
                "ಬೇಡಿಕೆ ಹೆಚ್ಚಿರುವ ಬಿತ್ತನೆ ಮತ್ತು ಕಟಾವಿನ ಅವಧಿಯಲ್ಲಿ ಮೊದಲೇ ಕಾಯ್ದಿರಿಸಿ.",
                "ಈ ಕೇಂದ್ರಗಳನ್ನು ಬಳಸುವ ರೈತರು ಎಕರೆ ಅಥವಾ ಗಂಟೆಯ ಆಧಾರದ ಮೇಲೆ ಬಾಡಿಗೆ ಪಾವತಿಸುತ್ತಾರೆ; ಸ್ವಂತ ಯಂತ್ರ ಖರೀದಿಸುವ ಅಗತ್ಯವಿರುವುದಿಲ್ಲ.",
            ],
            "cautions": ["ಕಾಯ್ದಿರಿಸುವ ವಿಧಾನ ಮತ್ತು ದರಗಳು ಬದಲಾಗಬಹುದು, ಆದ್ದರಿಂದ ನಿಮ್ಮ ಸ್ಥಳೀಯ {RSK} ಯಲ್ಲಿ ಪ್ರಸ್ತುತ ನಿಯಮಗಳನ್ನು ಖಚಿತಪಡಿಸಿಕೊಳ್ಳಿ."],
            "sources": ["kyd", "isee"],
        },
    ],
}

