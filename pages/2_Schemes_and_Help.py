"""Schemes, documents, safe buying and crop disease help for KisanDrishti.

Optional screenshots: put images in an `images` folder named <slug>_step<N>.png
(for example images/pmfby_step3.png). They appear under that step automatically.
Information last checked October 2026 from government and public sources.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import streamlit as st  # noqa: E402

import i18n  # noqa: E402
import ui  # noqa: E402

st.set_page_config(page_title="Schemes and Help | KisanDrishti", page_icon="📋")

IMAGES = Path(__file__).resolve().parent.parent / "images"

SCHEMES = {
    "Crop insurance (PMFBY)": {
        "slug": "pmfby",
        "what": "Insurance that pays you if a notified crop is damaged by weather, pests or disease. You pay a small share of the premium and the government pays the rest.",
        "who": "Farmers growing notified crops, including tenant farmers and sharecroppers with a valid agreement or certificate. Enrolment is voluntary.",
        "documents": [
            "Aadhaar card (linked to your bank account and mobile number)",
            "Bank passbook or cancelled cheque (account in your own name)",
            "Land record: RTC or Record of Rights (Bhoomi portal)",
            "Sowing certificate or self-declaration of sowing, as prescribed",
            "Tenants only: cultivation agreement or the certificate the state prescribes",
            "Passport-size photo",
        ],
        "steps": [
            ("📅", "Check the last date", "Enrolment closes soon after the sowing season starts for each crop. Ask your bank, Common Service Centre (CSC) or Raitha Samparka Kendra for the exact date. Check your passbook too, in case your bank has already deducted a premium."),
            ("📄", "Collect your documents", "Tick the checklist above. Your name must match on Aadhaar, bank record and land record. Mismatches are a common reason for rejection."),
            ("🏦", "Choose where to apply", "Your bank branch or PACS, a CSC, or online at pmfby.gov.in (Farmer Corner, then Guest Farmer)."),
            ("✍️", "Fill in the form and pay your share", "Enter the crop, area and land details exactly as in your land record. Your share is 2% of the sum insured for kharif crops, 1.5% for rabi food crops and oilseeds, and 5% for commercial and horticultural crops."),
            ("✅", "Keep the receipt", "Save the receipt or application number. You can check your application status in Farmer Corner on pmfby.gov.in."),
        ],
        "extra_title": "If your crop is damaged",
        "extra": [
            "Localized damage (hailstorm, landslide, flooding or inundation, cloudburst, fire caused by lightning) and losses after harvest: report within 72 hours.",
            "Report by calling 14447, using the Crop Insurance app (take geo-tagged photos of the damaged field), or telling your bank or agriculture office.",
            "Wide-area losses such as drought are assessed through crop-cutting experiments, so you do not report them one by one.",
            "If you miss the 72 hours, still report and keep your photos.",
        ],
        "links": ["pmfby.gov.in", "Helpline 14447"],
    },
    "PM-KISAN income support": {
        "slug": "pmkisan",
        "what": "Direct income support of Rs 6,000 a year, paid in three instalments of Rs 2,000 into your bank account.",
        "who": "Landholding farmer families whose land is in official land records. Tenant farmers without land in their name are generally not covered.",
        "documents": [
            "Aadhaar card",
            "Bank account linked to Aadhaar",
            "Land record showing your ownership",
        ],
        "steps": [
            ("💻", "Open the portal or go to a CSC", "Go to pmkisan.gov.in, open Farmers Corner and choose New Farmer Registration. Or take your documents to a Common Service Centre."),
            ("✍️", "Enter your details", "Aadhaar number, state and district, bank details and land details. Keep them the same as in your documents."),
            ("📱", "Complete eKYC", "eKYC is compulsory to keep receiving instalments. You can do OTP eKYC on the portal, or biometric eKYC at a CSC."),
            ("🔎", "Check your status", "On pmkisan.gov.in use Know Your Status to see whether your instalment has been released."),
        ],
        "extra_title": "Help",
        "extra": ["PM-KISAN helpline: 155261 or 011-24300606."],
        "links": ["pmkisan.gov.in"],
    },
    "Kisan Credit Card (KCC)": {
        "slug": "kcc",
        "what": "A bank credit card for farm expenses such as seed, fertilizer and pesticides. Interest is lower than most private loans, and the government may reduce it further if you repay on time.",
        "who": "Farmers who own land or cultivate it on lease or tenancy, subject to the bank's checks.",
        "documents": [
            "Identity proof and address proof",
            "Land ownership record, or tenancy or lease papers",
            "Passport-size photos",
            "Your crop plan: what you will grow and the area",
            "Bank account details",
        ],
        "steps": [
            ("🏦", "Visit your bank", "Go to a commercial bank, rural bank or cooperative bank branch, or apply on your bank's website or the Jan Samarth portal."),
            ("📄", "Submit the form and documents", "Ask for the KCC application form. Give your crop plan so the bank can set your limit."),
            ("🔍", "Bank verification", "The bank checks your land record and eligibility, and may visit your land."),
            ("💳", "Receive your card", "After approval you get the card and a passbook that records your limit, withdrawals and repayments."),
        ],
        "extra_title": "Good to know",
        "extra": [
            "Ask your bank for the current credit limit and interest rate, and whether interest subvention for timely repayment applies to you.",
            "Your KCC number can also be used as ID when you buy subsidised fertilizer.",
            "Repay on time. Delays can cost you the interest benefit.",
        ],
        "links": ["Your bank branch", "jansamarth.in"],
    },
    "Soil Health Card": {
        "slug": "shc",
        "what": "A free soil test report for your land with fertilizer advice crop by crop. It helps you apply only what the soil needs.",
        "who": "Any farmer, for their own land.",
        "documents": ["Aadhaar card", "Details of your land (survey number)"],
        "steps": [
            ("📞", "Contact the agriculture office", "Ask your District or Block Agriculture Officer, your Raitha Samparka Kendra, or your Krishi Vigyan Kendra for soil testing."),
            ("🧪", "Soil sample is collected", "An official collects soil from your field and records its location."),
            ("🔬", "Testing", "The sample is tested at a soil testing lab on 12 soil measures."),
            ("📋", "Get your card", "You get a card with your soil results and fertilizer advice. You can also look it up on soilhealth.dac.gov.in."),
        ],
        "extra_title": "Use it before buying fertilizer",
        "extra": ["Apply the amounts the card recommends. More is not better, and it costs you money."],
        "links": ["soilhealth.dac.gov.in"],
    },
}

FERTILIZER = [
    "Buy from a licensed fertilizer dealer, a cooperative society (PACS) or a cooperative marketing society.",
    "Subsidised fertilizer is sold through a point-of-sale (PoS) machine. Carry your Aadhaar, KCC or voter ID. You get the receipt by SMS on your mobile.",
    "Do not pay more than the MRP printed on the bag. Take the printed bill.",
    "Check the bag: sealed, grade and nutrient percentages printed, maker's name, batch number and MRP.",
    "Use your Soil Health Card to decide how much you need. Over-use wastes money and harms the soil.",
]
PESTICIDE = [
    "Buy only from a licensed pesticide dealer. Never buy loose, repacked or unlabelled pesticide.",
    "Check the container: sealed, label in good condition, registration number, batch number and expiry date.",
    "Read the colour label. Red means extremely toxic, yellow highly toxic, blue moderately toxic and green slightly toxic. Ask your agriculture officer whether a lower-toxicity option will work.",
    "Take a proper bill showing the product name, batch number and date. Keep the bill and the packing in case you need to complain.",
    "Use only the dose and timing on the label or advised by your agriculture officer. Keep to the waiting period before harvest that the label gives.",
    "Wear gloves, a mask and full clothing when spraying. Never reuse empty containers. Store chemicals locked, away from children, food and animal feed.",
    "If you suspect a fake or poor-quality product, tell your district agriculture office.",
]
DISEASE_STEPS = [
    ("📸", "Take photos", "Close-ups of the front and back of affected leaves, the whole plant, and a wide view of the field. Note the crop, its age, when it started, whether it is spreading, and the recent weather."),
    ("🧑‍🌾", "Get it identified by an expert", "Show the photos or a fresh sample at your nearest Krishi Vigyan Kendra (search your state and district on kvk.icar.gov.in), your Raitha Samparka Kendra, or your agriculture officer. Some KVKs have plant diagnostic labs."),
    ("💊", "Treat only as advised", "Ask for the product name, dose and timing. Do not mix products on your own. Follow the label."),
    ("🛒", "Buy safely", "Use the Buying inputs safely tab: licensed dealer, sealed pack, bill with batch number."),
    ("🌱", "Meanwhile, reduce spread", "Remove badly infected plant parts, improve airflow and drainage, and avoid walking through the wet crop."),
]


def show_step_image(slug, n):
    for ext in ("png", "jpg", "jpeg"):
        path = IMAGES / f"{slug}_step{n}.{ext}"
        if path.exists():
            st.image(str(path), caption="Screenshot for this step")
            return


def bullets(items):
    for item in items:
        st.markdown(f"- {item}")


ui.inject_css()
i18n.language_picker(translated=False)
ui.hero("Schemes and help", "Documents, steps and safe buying, for Karnataka farmers.", "📋")
st.caption("Rules, dates and amounts change, so confirm with your bank, CSC or Raitha Samparka Kendra before you apply. Information last checked October 2026.")

tab1, tab2, tab3 = st.tabs(["Schemes and documents", "Buying inputs safely", "Crop disease help"])

with tab1:
    choice = st.selectbox("Choose a scheme", list(SCHEMES))
    s = SCHEMES[choice]
    st.markdown(f"**What it is:** {s['what']}")
    st.markdown(f"**Who can apply:** {s['who']}")

    st.subheader("Documents checklist")
    ticks = [st.checkbox(d, key=f"{s['slug']}_doc_{i}") for i, d in enumerate(s["documents"])]
    if all(ticks):
        st.success("All documents ready. You can go and apply.")

    st.subheader("How to apply")
    for n, (icon, title, text) in enumerate(s["steps"], 1):
        st.markdown(f"**{icon} Step {n}: {title}**")
        st.write(text)
        show_step_image(s["slug"], n)

    st.subheader(s["extra_title"])
    bullets(s["extra"])
    st.markdown("**Where to go:** " + " | ".join(s["links"]))

with tab2:
    st.subheader("Fertilizer")
    bullets(FERTILIZER)
    st.subheader("Pesticide")
    bullets(PESTICIDE)
    st.info("Fertilizer and pesticide are only worth buying once you know what your soil or crop needs. Start with a Soil Health Card and an expert diagnosis.")

with tab3:
    st.write("This app does not diagnose plant diseases. Follow these steps to get the right help and the right product.")
    for n, (icon, title, text) in enumerate(DISEASE_STEPS, 1):
        st.markdown(f"**{icon} Step {n}: {title}**")
        st.write(text)
    st.markdown("**Help:** Kisan Call Centre 1800-180-1551 | Emergency 112")

ui.feedback_box()
st.markdown("---")
st.caption("© 2026 Abhishek Hitabutti. All rights reserved. Copying or reuse of this app without permission is prohibited.")
