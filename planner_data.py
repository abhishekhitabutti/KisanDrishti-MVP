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
