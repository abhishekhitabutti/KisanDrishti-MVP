"""Schemes, documents, safe buying and crop disease help for KisanDrishti.
Fully bilingual: 100% pure Kannada localization with technical terms in braces {...}.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import streamlit as st
import i18n
import ui
from i18n import t

IMAGES = Path(__file__).resolve().parent.parent / "images"

# --- ENGLISH SCHEMES DATA ---
SCHEMES_EN = {
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

# --- KANNADA SCHEMES DATA ---
SCHEMES_KN = {
    "ಪ್ರಧಾನ ಮಂತ್ರಿ ಫಸಲ್ ಬಿಮಾ ಯೋಜನೆ {PMFBY}": {
        "slug": "pmfby",
        "what": "ಹವಾಮಾನ ವೈಪರೀತ್ಯ, ಕೀಟ ಅಥವಾ ರೋಗಗಳಿಂದ ಅಧಿಸೂಚಿತ ಬೆಳೆಗೆ ಹಾನಿಯಾದರೆ ಪರಿಹಾರ ನೀಡುವ ವಿಮಾ ಯೋಜನೆ. ರೈತರು ಕೇವಲ ಅಲ್ಪ ಪ್ರಮಾಣದ ಪ್ರೀಮಿಯಂ ಪಾವತಿಸುತ್ತಾರೆ, ಉಳಿದ ಹೆಚ್ಚಿನ ಪಾಲನ್ನು ಸರ್ಕಾರವೇ ಭರಿಸುತ್ತದೆ.",
        "who": "ಅಧಿಸೂಚಿತ ಬೆಳೆ ಬೆಳೆಯುವ ಎಲ್ಲ ರೈತರು, ಮಾನ್ಯತೆ ಪಡೆದ ಗುತ್ತಿಗೆ ರೈತರು ಮತ್ತು ಪಾಲುದಾರ ರೈತರು. ವಿಮೆ ಪಡೆಯುವುದು ಐಚ್ಛಿಕವಾಗಿದೆ.",
        "documents": [
            "ಆಧಾರ್ ಕಾರ್ಡ್ (ಬ್ಯಾಂಕ್ ಖಾತೆ ಮತ್ತು ಮೊಬೈಲ್ ಸಂಖ್ಯೆಗೆ ಲಿಂಕ್ ಆಗಿರಬೇಕು)",
            "ಬ್ಯಾಂಕ್ ಪಾಸ್‌ಬುಕ್ ಅಥವಾ ರದ್ದುಪಡಿಸಿದ ಚೆಕ್ (ರೈತನ ಸ್ವಂತ ಹೆಸರಿನ ಖಾತೆ)",
            "ಜಮೀನಿನ ಪಹಣಿ: {RTC} ಅಥವಾ ಭೂಮಿ ತಂತ್ರಾಂಶದ ಹಕ್ಕು ದಾಖಲೆ",
            "ಬಿತ್ತನೆ ದೃಢೀಕರಣ ಪತ್ರ ಅಥವಾ ಸ್ವಯಂ ಘೋಷಿತ ಬಿತ್ತನೆ ಪ್ರಮಾಣಪತ್ರ",
            "ಗುತ್ತಿಗೆ ರೈತರಾಗಿದ್ದರೆ: ಮಾನ್ಯತೆ ಪಡೆದ ಕೃಷಿ ಗುತ್ತಿಗೆ ಒಪ್ಪಂದ ಪತ್ರ",
            "ಪಾಸ್‌ಪೋರ್ಟ್ ಅಳತೆಯ ಭಾವಚಿತ್ರ",
        ],
        "steps": [
            ("📅", "ಕೊನೆಯ ದಿನಾಂಕವನ್ನು ಪರಿಶೀಲಿಸಿ", "ಪ್ರತಿ ಬೆಳೆಯ ಬಿತ್ತನೆ ಕಾಲ ಆರಂಭವಾದ ಕೆಲವೇ ದಿನಗಳಲ್ಲಿ ನೋಂದಣಿ ಮುಕ್ತಾಯವಾಗುತ್ತದೆ. ನಿಖರ ದಿನಾಂಕಕ್ಕಾಗಿ ನಿಮ್ಮ ಬ್ಯಾಂಕ್, ಗ್ರಾಮ ಒನ್ / ಸಿಎಸ್‌ಸಿ {CSC} ಅಥವಾ ರೈತ ಸಂಪರ್ಕ ಕೇಂದ್ರವನ್ನು {RSK} ಸಂಪರ್ಕಿಸಿ."),
            ("📄", "ದಾಖಲೆಗಳನ್ನು ಸಿದ್ಧಪಡಿಸಿಕೊಳ್ಳಿ", "ಮೇಲಿನ ಪಟ್ಟಿಯ ಎಲ್ಲ ದಾಖಲೆಗಳನ್ನು ಒಗ್ಗೂಡಿಸಿ. ಆಧಾರ್, ಬ್ಯಾಂಕ್ ಪಾಸ್‌ಬುಕ್ ಮತ್ತು ಪಹಣಿಯಲ್ಲಿ ಹೆಸರು ಒಂದೇ ಆಗಿರಬೇಕು. ವ್ಯತ್ಯಾಸವಿದ್ದರೆ ಅರ್ಜಿ ತಿರಸ್ಕೃತವಾಗಬಹುದು."),
            ("🏦", "ಅರ್ಜಿ ಸಲ್ಲಿಸುವ ಕೇಂದ್ರವನ್ನು ಆರಿಸಿ", "ನಿಮ್ಮ ಬ್ಯಾಂಕ್ ಶಾಖೆ ಅಥವಾ ಪ್ರಾಥಮಿಕ ಕೃಷಿ ಪತ್ತಿನ ಸಹಕಾರ ಸಂಘ {PACS}, ಸಿಎಸ್‌ಸಿ {CSC} ಕೇಂದ್ರ, ಅಥವಾ {pmfby.gov.in} ಪೋರ್ಟಲ್‌ನಲ್ಲಿ ಆನ್‌ಲೈನ್ ಮೂಲಕ ಸಲ್ಲಿಸಿ."),
            ("✍️", "ಅರ್ಜಿ ಸಲ್ಲಿಸಿ ಪ್ರೀಮಿಯಂ ಪಾವತಿಸಿ", "ಪಹಣಿಯಲ್ಲಿರುವಂತೆ ಜಮೀನಿನ ಸರ್ವೆ ನಂಬರ್ ಮತ್ತು ಬೆಳೆ ವಿವರಗಳನ್ನು ಸರಿಯಾಗಿ ದಾಖಲಿಸಿ. ಖಾರಿಫ್ ಬೆಳೆಗೆ ವಿಮಾ ಮೊತ್ತದ 2%, ರಬಿ ಆಹಾರ ಬೆಳೆ ಮತ್ತು ಎಣ್ಣೆಕಾಳುಗಳಿಗೆ 1.5%, ಮತ್ತು ವಾಣಿಜ್ಯ/ತೋಟಗಾರಿಕಾ ಬೆಳೆಗಳಿಗೆ 5% ಪ್ರೀಮಿಯಂ ಪಾವತಿಸಿ."),
            ("✅", "ರಶೀದಿಯನ್ನು ಜೋಪಾನವಾಗಿಡಿ", "ಅರ್ಜಿ ಸಂಖ್ಯೆ ಇರುವ ಸ್ವೀಕೃತಿ ರಶೀದಿಯನ್ನು ಸಂರಕ್ಷಿಸಿಡಿ. {pmfby.gov.in} ನಲ್ಲಿ ಅರ್ಜಿ ಸ್ಥಿತಿಯನ್ನು ಪರಿಶೀಲಿಸಬಹುದು."),
        ],
        "extra_title": "ಬೆಳೆ ಹಾನಿಯಾದಾಗ ಏನು ಮಾಡಬೇಕು?",
        "extra": [
            "ಸ್ಥಳೀಯ ಹಾನಿ (ಆಲಿಕಲ್ಲು ಮಳೆ, ಭೂಕುಸಿತ, ಪ್ರವಾಹ, ನೀರು ನಿಲ್ಲುವುದು, ಮಿಂಚಿನಿಂದ ಬೆಂಕಿ) ಮತ್ತು ಕಟಾವಿನ ನಂತರದ ಹಾನಿ ಸಂಭವಿಸಿದರೆ 72 ಗಂಟೆಯೊಳಗೆ ಮಾಹಿತಿ ನೀಡಿ.",
            "14447 ಉಚಿತ ಸಹಾಯವಾಣಿಗೆ ಕರೆ ಮಾಡಿ, ಕ್ರಾಪ್ ಇನ್ಶೂರೆನ್ಸ್ ಮೊಬೈಲ್ ಆ್ಯಪ್ ಮೂಲಕ ಜಿಯೋ-ಟ್ಯಾಗ್ ಮಾಡಿದ ಫೋಟೋ ಅಪ್‌ಲೋಡ್ ಮಾಡಿ, ಅಥವಾ ತಕ್ಷಣ ಬ್ಯಾಂಕ್/ಕೃಷಿ ಇಲಾಖೆಗೆ ಲಿಖಿತ ಮಾಹಿತಿ ನೀಡಿ.",
            "ಬರಗಾಲದಂತಹ ವ್ಯಾಪಕ ಹಾನಿಯನ್ನು ಬೆಳೆ ಕಟಾವು ಪ್ರಯೋಗಗಳ {CCE} ಮೂಲಕ ಸರ್ಕಾರವೇ ಅಂದಾಜಿಸುತ್ತದೆ; ಅದಕ್ಕೆ ಪ್ರತ್ಯೇಕ ವರದಿ ಬೇಕಿಲ್ಲ.",
            "72 ಗಂಟೆ ಮೀರಿದ್ದರೂ ತಕ್ಷಣವೇ ಅಧಿಕಾರಿಗಳಿಗೆ ಮಾಹಿತಿ ನೀಡಿ ಮತ್ತು ಹಾನಿಯ ಛಾಯಾಚಿತ್ರಗಳನ್ನು ಇಟ್ಟುಕೊಳ್ಳಿ.",
        ],
        "links": ["pmfby.gov.in", "ಉಚಿತ ಸಹಾಯವಾಣಿ: 14447"],
    },
    "ಪಿಎಂ-ಕಿಸಾನ್ ಆದಾಯ ಬೆಂಬಲ ಯೋಜನೆ {PM-KISAN}": {
        "slug": "pmkisan",
        "what": "ವರ್ಷಕ್ಕೆ ₹6,000 ನೇರ ಆದಾಯ ಬೆಂಬಲ. ಪ್ರತಿ 4 ತಿಂಗಳಿಗೊಮ್ಮೆ ₹2,000 ರಂತೆ 3 ಕಂತುಗಳಲ್ಲಿ ನೇರವಾಗಿ ರೈತರ ಬ್ಯಾಂಕ್ ಖಾತೆಗೆ ಜಮೆಯಾಗುತ್ತದೆ.",
        "who": "ಅಧಿಕೃತ ಭೂ ದಾಖಲೆಗಳಲ್ಲಿ ಹೆಸರಿರುವ ಕೃಷಿ ಭೂಮಿ ಹೊಂದಿರುವ ರೈತ ಕುಟುಂಬಗಳು. ಸ್ವಂತ ಭೂಮಿ ಹೊಂದಿರದ ಗುತ್ತಿಗೆ ರೈತರಿಗೆ ಇದು ಅನ್ವಯಿಸುವುದಿಲ್ಲ.",
        "documents": [
            "ಆಧಾರ್ ಕಾರ್ಡ್",
            "ಆಧಾರ್ ಲಿಂಕ್ ಆಗಿರುವ ಸಕ್ರಿಯ ಬ್ಯಾಂಕ್ ಖಾತೆ {DBT}",
            "ಸ್ವಂತ ಮಾಲೀಕತ್ವದ ಜಮೀನಿನ ಪಹಣಿ {RTC}",
        ],
        "steps": [
            ("💻", "ಪೋರ್ಟಲ್ ಅಥವಾ ಸಿಎಸ್‌ಸಿ ಕೇಂದ್ರಕ್ಕೆ ಭೇಟಿ ನೀಡಿ", "{pmkisan.gov.in} ಗೆ ಹೋಗಿ, {Farmers Corner} ನಲ್ಲಿ {New Farmer Registration} ಆಯ್ಕೆಮಾಡಿ, ಅಥವಾ ನಿಮ್ಮ ದಾಖಲೆಗಳೊಂದಿಗೆ ಸಿಎಸ್‌ಸಿ {CSC} ಕೇಂದ್ರಕ್ಕೆ ಭೇಟಿ ನೀಡಿ."),
            ("✍️", "ವಿವರಗಳನ್ನು ನಮೂದಿಸಿ", "ಆಧಾರ್ ಸಂಖ್ಯೆ, ಜಿಲ್ಲೆ, ತಾಲ್ಲೂಕು, ಬ್ಯಾಂಕ್ ಖಾತೆ ವಿವರ ಮತ್ತು ಜಮೀನಿನ ಸರ್ವೆ ನಂಬರ್ ದಾಖಲಿಸಿ."),
            ("📱", "ಇ-ಕೆವೈಸಿ {eKYC} ಪೂರ್ಣಗೊಳಿಸಿ", "ಕಂತುಗಳ ಹಣ ನಿರಂತರವಾಗಿ ಜಮೆಯಾಗಲು {eKYC} ಕಡ್ಡಾಯ. ಪೋರ್ಟಲ್‌ನಲ್ಲಿ ಆಧಾರ್ {OTP} ಮೂಲಕ ಅಥವಾ ಸಿಎಸ್‌ಸಿ {CSC} ನಲ್ಲಿ ಬಯೋಮೆಟ್ರಿಕ್ ಮೂಲಕ ಮಾಡಬಹುದು."),
            ("🔎", "ಅರ್ಜಿ ಸ್ಥಿತಿ ಪರಿಶೀಲಿಸಿ", "{pmkisan.gov.in} ನಲ್ಲಿ {Know Your Status} ಮೂಲಕ ಹಣ ಜಮೆಯಾದ ವಿವರವನ್ನು ಪರಿಶೀಲಿಸಿ."),
        ],
        "extra_title": "ಸಹಾಯವಾಣಿ",
        "extra": ["ಪಿಎಂ-ಕಿಸಾನ್ ಉಚಿತ ಸಹಾಯವಾಣಿ: 155261 ಅಥವಾ 011-24300606."],
        "links": ["pmkisan.gov.in"],
    },
    "ಕಿಸಾನ್ ಕ್ರೆಡಿಟ್ ಕಾರ್ಡ್ {KCC}": {
        "slug": "kcc",
        "what": "ಬೀಜ, ರಸಗೊಬ್ಬರ ಮತ್ತು ಕೀಟನಾಶಕಗಳಂತಹ ಕೃಷಿ ವೆಚ್ಚಗಳಿಗಾಗಿ ಬ್ಯಾಂಕ್ ನೀಡುವ ರಿಯಾಯಿತಿ ಬಡ್ಡಿ ದರದ ಕ್ರೆಡಿಟ್ ಕಾರ್ಡ್ ಸಾಲ. ಸಕಾಲದಲ್ಲಿ ಮರುಪಾವತಿಸಿದರೆ ಸರ್ಕಾರದಿಂದ ಹೆಚ್ಚುವರಿ ಬಡ್ಡಿ ರಿಯಾಯಿತಿ ದೊರೆಯುತ್ತದೆ.",
        "who": "ಸ್ವಂತ ಕೃಷಿ ಭೂಮಿ ಹೊಂದಿರುವ ರೈತರು, ಗುತ್ತಿಗೆ ರೈತರು ಮತ್ತು ಜಂಟಿ ಹೊಣೆಗಾರಿಕೆ ಗುಂಪುಗಳ ರೈತರು.",
        "documents": [
            "ಗುರುತಿನ ಚೀಟಿ ಮತ್ತು ವಿಳಾಸದ ಪುರಾವೆ (ಆಧಾರ್, ವೋಟರ್ ಐಡಿ)",
            "ಜಮೀನಿನ ಪಹಣಿ {RTC} ಅಥವಾ ಗುತ್ತಿಗೆ ಕೃಷಿ ಪತ್ರಗಳು",
            "ಪಾಸ್‌ಪೋರ್ಟ್ ಅಳತೆಯ ಭಾವಚಿತ್ರಗಳು",
            "ಬೆಳೆ ಯೋಜನೆ ವಿವರ: ಬೆಳೆಯುವ ಬೆಳೆ ಮತ್ತು ವಿಸ್ತೀರ್ಣ",
            "ಬ್ಯಾಂಕ್ ಉಳಿತಾಯ ಖಾತೆ ವಿವರ",
        ],
        "steps": [
            ("🏦", "ನಿಮ್ಮ ಬ್ಯಾಂಕ್ ಶಾಖೆಗೆ ಭೇಟಿ ನೀಡಿ", "ವಾಣಿಜ್ಯ ಬ್ಯಾಂಕ್, ಗ್ರಾಮೀಣ ಬ್ಯಾಂಕ್ ಅಥವಾ ಸಹಕಾರ ಬ್ಯಾಂಕ್ ಶಾಖೆಗೆ ಭೇಟಿ ನೀಡಿ, ಅಥವಾ ಜನ ಸಮರ್ಥ್ {Jan Samarth} ಪೋರ್ಟಲ್‌ನಲ್ಲಿ ಆನ್‌ಲೈನ್ ಅರ್ಜಿ ಸಲ್ಲಿಸಿ."),
            ("📄", "ಅರ್ಜಿ ಮತ್ತು ದಾಖಲೆಗಳನ್ನು ಸಲ್ಲಿಸಿ", "{KCC} ಅರ್ಜಿ ನಮೂನೆಯನ್ನು ಭರ್ತಿ ಮಾಡಿ. ಬೆಳೆ ಯೋಜನೆಯನ್ನು ನೀಡಿ ಸಾಲದ ಮಿತಿಯನ್ನು ನಿಗದಿಪಡಿಸಿಕೊಳ್ಳಿ."),
            ("🔍", "ಬ್ಯಾಂಕ್ ಪರಿಶೀಲನೆ", "ಬ್ಯಾಂಕ್ ಅಧಿಕಾರಿಗಳು ನಿಮ್ಮ ಭೂ ದಾಖಲೆ ಮತ್ತು ಅರ್ಹತೆಯನ್ನು ಪರಿಶೀಲಿಸುತ್ತಾರೆ, ಅಗತ್ಯವಿದ್ದರೆ ಜಮೀನಿಗೆ ಭೇಟಿ ನೀಡುತ್ತಾರೆ."),
            ("💳", "ಕಾರ್ಡ್ ಮತ್ತು ಪಾಸ್‌ಬುಕ್ ಪಡೆಯಿರಿ", "ಅನುಮೋದನೆಯ ನಂತರ {KCC} ರುಪೇ ಕಾರ್ಡ್ ಮತ್ತು ಜಮೆ-ಖರ್ಚಿನ ವಿವರಗಳ ಪಾಸ್‌ಬುಕ್ ಪಡೆಯಿರಿ."),
        ],
        "extra_title": "ಮುಖ್ಯ ಮಾಹಿತಿ",
        "extra": [
            "ಪ್ರಸ್ತುತ ಸಾಲದ ಮಿತಿ ಮತ್ತು ಬಡ್ಡಿದರ, ಹಾಗೂ ಸಕಾಲಿಕ ಮರುಪಾವತಿ ಬಡ್ಡಿ ಸಬ್ಸಿಡಿ ಕುರಿತು ನಿಮ್ಮ ಬ್ಯಾಂಕ್‌ನಲ್ಲಿ ವಿಚಾರಿಸಿ.",
            "ರಿಯಾಯಿತಿ ದರದ ರಸಗೊಬ್ಬರ ಖರೀದಿಸಲು {KCC} ಸಂಖ್ಯೆಯನ್ನು ಗುರುತಿನ ಚೀಟಿಯಾಗಿ ಬಳಸಬಹುದು.",
            "ಸಾಲವನ್ನು ಸಮಯಕ್ಕೆ ಸರಿಯಾಗಿ ಮರುಪಾವತಿಸಿ, ವಿಳಂಬ ಮಾಡಿದರೆ ಬಡ್ಡಿ ರಿಯಾಯಿತಿಯ ಲಾಭ ಕೈತಪ್ಪುತ್ತದೆ.",
        ],
        "links": ["ಸ್ಥಳೀಯ ಬ್ಯಾಂಕ್ ಶಾಖೆ", "jansamarth.in"],
    },
    "ಮಣ್ಣು ಆರೋಗ್ಯ ಕಾರ್ಡ್ {Soil Health Card}": {
        "slug": "shc",
        "what": "ನಿಮ್ಮ ಜಮೀನಿನ ಮಣ್ಣಿನ ಗುಣಮಟ್ಟ, ಪೋಷಕಾಂಶಗಳ ಮಟ್ಟ ಮತ್ತು ಬೆಳೆವಾರು ರಸಗೊಬ್ಬರ ಶಿಫಾರಸುಗಳನ್ನು ತಿಳಿಸುವ ಉಚಿತ ಸರ್ಕಾರಿ ವರದಿ. ಮಣ್ಣಿಗೆ ಎಷ್ಟು ಬೇಕೋ ಅಷ್ಟೇ ಗೊಬ್ಬರ ಹಾಕಲು ಇದು ನೆರವಾಗುತ್ತದೆ.",
        "who": "ಸ್ವಂತ ಕೃಷಿ ಜಮೀನು ಹೊಂದಿರುವ ಪ್ರತಿಯೊಬ್ಬ ರೈತರು.",
        "documents": ["ಆಧಾರ್ ಕಾರ್ಡ್", "ಜಮೀನಿನ ಸರ್ವೆ ನಂಬರ್ ವಿವರ"],
        "steps": [
            ("📞", "ಕೃಷಿ ಕಚೇರಿಯನ್ನು ಸಂಪರ್ಕಿಸಿ", "ಮಣ್ಣು ಪರೀಕ್ಷೆಗಾಗಿ ನಿಮ್ಮ ತಾಲ್ಲೂಕು ಕೃಷಿ ಅಧಿಕಾರಿ, ರೈತ ಸಂಪರ್ಕ ಕೇಂದ್ರ {RSK} ಅಥವಾ ಕೃಷಿ ವಿಜ್ಞಾನ ಕೇಂದ್ರವನ್ನು {KVK} ಸಂಪರ್ಕಿಸಿ."),
            ("🧪", "ಮಣ್ಣಿನ ಮಾದರಿ ಸಂಗ್ರಹ", "ಕೃಷಿ ಇಲಾಖೆಯ ಸಿಬ್ಬಂದಿ ನಿಮ್ಮ ಜಮೀನಿಗೆ ಬಂದು ವೈಜ್ಞಾನಿಕವಾಗಿ ಮಣ್ಣಿನ ಮಾದರಿ ಸಂಗ್ರಹಿಸಿ ಸ್ಥಳ ಗುರುತಿಸುತ್ತಾರೆ."),
            ("🔬", "ಪ್ರಯೋಗಾಲಯದಲ್ಲಿ ಪರೀಕ್ಷೆ", "ಮಣ್ಣು ಪರೀಕ್ಷಾ ಪ್ರಯೋಗಾಲಯದಲ್ಲಿ 12 ಪ್ರಮುಖ ಪೋಷಕಾಂಶ ಸೂಚ್ಯಂಕಗಳ ಮೇಲೆ ಪರೀಕ್ಷೆ ನಡೆಸಲಾಗುತ್ತದೆ."),
            ("📋", "ಕಾರ್ಡ್ ಪಡೆಯಿರಿ", "ಪೋಷಕಾಂಶ ವಿವರ ಮತ್ತು ಶಿಫಾರಸುಗಳನ್ನು ಒಳಗೊಂಡ ಮುದ್ರಿತ ಕಾರ್ಡ್ ಪಡೆಯಿರಿ. {soilhealth.dac.gov.in} ನಲ್ಲೂ ಇದನ್ನು ಪರಿಶೀಲಿಸಬಹುದು."),
        ],
        "extra_title": "ಗೊಬ್ಬರ ಖರೀದಿಸುವ ಮುನ್ನ ಬಳಸಿ",
        "extra": ["ಕಾರ್ಡ್‌ನಲ್ಲಿ ಶಿಫಾರಸು ಮಾಡಿದ ಪ್ರಮಾಣವನ್ನು ಮಾತ್ರ ಬಳಸಿ. ಹೆಚ್ಚು ಗೊಬ್ಬರ ಹಾಕಿದರೆ ಹೆಚ್ಚು ಇಳುವರಿ ಬರುವುದಿಲ್ಲ, ಬದಲಾಗಿ ದುಡ್ಡು ವ್ಯರ್ಥವಾಗಿ ಮಣ್ಣು ಹಾಳಾಗುತ್ತದೆ."],
        "links": ["soilhealth.dac.gov.in"],
    },
}

FERTILIZER_EN = [
    "Buy from a licensed fertilizer dealer, a cooperative society (PACS) or a cooperative marketing society.",
    "Subsidised fertilizer is sold through a point-of-sale (PoS) machine. Carry your Aadhaar, KCC or voter ID. You get the receipt by SMS on your mobile.",
    "Do not pay more than the MRP printed on the bag. Take the printed bill.",
    "Check the bag: sealed, grade and nutrient percentages printed, maker's name, batch number and MRP.",
    "Use your Soil Health Card to decide how much you need. Over-use wastes money and harms the soil.",
]

FERTILIZER_KN = [
    "ಪರವಾನಗಿ ಪಡೆದ ಗೊಬ್ಬರ ಮಾರಾಟಗಾರರು, ಪ್ರಾಥಮಿಕ ಕೃಷಿ ಪತ್ತಿನ ಸಹಕಾರ ಸಂಘ {PACS} ಅಥವಾ ಕೃಷಿ ಮಾರಾಟ ಸಹಕಾರ ಸಂಘಗಳಿಂದಲೇ ಖರೀದಿಸಿ.",
    "ರಿಯಾಯಿತಿ ದರದ ರಸಗೊಬ್ಬರವನ್ನು ಪಾಯಿಂಟ್-ಆಫ್-ಸೇಲ್ {PoS} ಯಂತ್ರದ ಮೂಲಕವೇ ಮಾರಾಟ ಮಾಡಲಾಗುತ್ತದೆ. ನಿಮ್ಮ ಆಧಾರ್, {KCC} ಅಥವಾ ಮತದಾರರ ಗುರುತಿನ ಚೀಟಿ ತೆಗೆದುಕೊಂಡು ಹೋಗಿ. ಮೊಬೈಲ್‌ಗೆ {SMS} ರಶೀದಿ ಬರುತ್ತದೆ.",
    "ಚೀಲದ ಮೇಲೆ ಮುದ್ರಿಸಲಾದ ಗರಿಷ್ಠ ಮಾರಾಟ ಬೆಲೆಗಿಂತ {MRP} ಹೆಚ್ಚಿನ ಹಣವನ್ನು ನೀಡಬೇಡಿ. ಅಧಿಕೃತ ಮುದ್ರಿತ ರಶೀದಿಯನ್ನು ಖಡ್ಡಾಯವಾಗಿ ಪಡೆಯಿರಿ.",
    "ಚೀಲವನ್ನು ಪರಿಶೀಲಿಸಿ: ಸೀಲ್ ಆಗಿದೆಯೇ, ಪೋಷಕಾಂಶಗಳ ಶೇಕಡಾವಾರು ಪ್ರಮಾಣ, ತಯಾರಕರ ಹೆಸರು, ಬ್ಯಾಚ್ ಸಂಖ್ಯೆ ಮತ್ತು {MRP} ಸ್ಪಷ್ಟವಾಗಿ ಮುದ್ರಿತವಾಗಿದೆಯೇ ಎಂದು ನೋಡಿ.",
    "ನಿಮ್ಮ ಮಣ್ಣು ಆರೋಗ್ಯ ಕಾರ್ಡ್ {Soil Health Card} ಶಿಫಾರಸು ಆಧರಿಸಿ ಮಾತ್ರ ಗೊಬ್ಬರ ಪ್ರಮಾಣ ನಿರ್ಧರಿಸಿ. ಮಿತಿಮೀರಿದ ಗೊಬ್ಬರ ಬಳಕೆ ಹಣ ವ್ಯರ್ಥ ಮಾಡುವುದರ ಜೊತೆಗೆ ಮಣ್ಣಿನ ಸಾರವನ್ನು ಹಾಳುಮಾಡುತ್ತದೆ.",
]

PESTICIDE_EN = [
    "Buy only from a licensed pesticide dealer. Never buy loose, repacked or unlabelled pesticide.",
    "Check the container: sealed, label in good condition, registration number, batch number and expiry date.",
    "Read the colour label. Red means extremely toxic, yellow highly toxic, blue moderately toxic and green slightly toxic. Ask your agriculture officer whether a lower-toxicity option will work.",
    "Take a proper bill showing the product name, batch number and date. Keep the bill and the packing in case you need to complain.",
    "Use only the dose and timing on the label or advised by your agriculture officer. Keep to the waiting period before harvest that the label gives.",
    "Wear gloves, a mask and full clothing when spraying. Never reuse empty containers. Store chemicals locked, away from children, food and animal feed.",
    "If you suspect a fake or poor-quality product, tell your district agriculture office.",
]

PESTICIDE_KN = [
    "ಪರವಾನಗಿ ಪಡೆದ ಅಧಿಕೃತ ಕೀಟನಾಶಕ ಮಾರಾಟಗಾರರಿಂದ ಮಾತ್ರ ಖರೀದಿಸಿ. ಲೇಬಲ್ ಇಲ್ಲದ, ಸಡಿಲವಾದ ಅಥವಾ ಮರುಪ್ಯಾಕ್ ಮಾಡಿದ ಕೀಟನಾಶಕವನ್ನು ಎಂದಿಗೂ ಖರೀದಿಸಬೇಡಿ.",
    "ಡಬ್ಬಿ/ಬಾಟಲಿಯನ್ನು ಪರಿಶೀಲಿಸಿ: ಸೀಲ್ ಗಟ್ಟಿಯಾಗಿದೆಯೇ, ಲೇಬಲ್ ಸ್ಪಷ್ಟವಾಗಿದೆಯೇ, ಕೇಂದ್ರ ಕೀಟನಾಶಕ ಮಂಡಳಿ ನೋಂದಣಿ ಸಂಖ್ಯೆ, ಬ್ಯಾಚ್ ನಂಬರ್ ಮತ್ತು ಅವಧಿ ಮುಗಿಯುವ ದಿನಾಂಕ {Expiry Date} ಸರಿಯಾಗಿದೆಯೇ ಎಂದು ಖಚಿತಪಡಿಸಿಕೊಳ್ಳಿ.",
    "ಬಣ್ಣದ ತ್ರಿಕೋನ ಚಿಹ್ನೆಯನ್ನು ಗಮನಿಸಿ: ಕೆಂಪು (ಅತ್ಯಂತ ತೀವ್ರ ವಿಷಕಾರಿ), ಹಳದಿ (ಹೆಚ್ಚು ವಿಷಕಾರಿ), ನೀಲಿ (ಮಧ್ಯಮ ವಿಷಕಾರಿ), ಮತ್ತು ಹಸಿರು (ಕಡಿಮೆ ವಿಷಕಾರಿ). ಕಡಿಮೆ ವಿಷಕಾರಿ ಔಷಧ ಲಭ್ಯವಿದೆಯೇ ಎಂದು ಕೃಷಿ ಅಧಿಕಾರಿಯನ್ನು ಕೇಳಿ.",
    "ಉತ್ಪನ್ನದ ಹೆಸರು, ಬ್ಯಾಚ್ ಸಂಖ್ಯೆ ಮತ್ತು ದಿನಾಂಕ ನಮೂದಿಸಿರುವ ಅಸಲಿ ಬಿಲ್ ಪಡೆಯಿರಿ. ಗುಣಮಟ್ಟ ಕಳಪೆಯಾಗಿದ್ದರೆ ದೂರು ನೀಡಲು ಬಿಲ್ ಮತ್ತು ಪ್ಯಾಕಿಂಗ್ ಜೋಪಾನವಾಗಿಡಿ.",
    "ಲೇಬಲ್‌ನಲ್ಲಿರುವ ಅಥವಾ ಕೃಷಿ ಅಧಿಕಾರಿಗಳು ಶಿಫಾರಸು ಮಾಡಿದ ಪ್ರಮಾಣ ಮತ್ತು ಸಮಯಕ್ಕೆ ಮಾತ್ರ ಸಿಂಪಡಿಸಿ. ಕೊಯ್ಲಿಗೆ ಮುನ್ನ ಕಾಯಬೇಕಾದ ಕಡ್ಡಾಯ ದಿನಗಳನ್ನು ಪಾಲಿಸಿ.",
    "ಸಿಂಪಡಣೆ ವೇಳೆ ಕೈಗವಸು, ಮಾಸ್ಕ್ ಮತ್ತು ಪೂರ್ಣ ತೋಳಿನ ರಕ್ಷಣಾ ಉಡುಪುಗಳನ್ನು ಧರಿಸಿ. ಖಾಲಿ ಡಬ್ಬಿಗಳನ್ನು ಎಂದಿಗೂ ಮರುಬಳಕೆ ಮಾಡಬೇಡಿ. ರಾಸಾಯನಿಕಗಳನ್ನು ಬೀಗ ಹಾಕಿ ಮಕ್ಕಳು ಮತ್ತು ಆಹಾರದಿಂದ ದೂರವಿಡಿ.",
    "ನಕಲಿ ಅಥವಾ ಕಳಪೆ ಗುಣಮಟ್ಟದ ಔಷಧ ಕಂಡುಬಂದರೆ ತಕ್ಷಣವೇ ಜಿಲ್ಲಾ ಕೃಷಿ ಜಾಗೃತ ಕೋಶಕ್ಕೆ ಮಾಹಿತಿ ನೀಡಿ.",
]

DISEASE_STEPS_EN = [
    ("📸", "Take photos", "Close-ups of the front and back of affected leaves, the whole plant, and a wide view of the field. Note the crop, its age, when it started, whether it is spreading, and the recent weather."),
    ("🧑‍🌾", "Get it identified by an expert", "Show the photos or a fresh sample at your nearest Krishi Vigyan Kendra (search your state and district on kvk.icar.gov.in), your Raitha Samparka Kendra, or your agriculture officer. Some KVKs have plant diagnostic labs."),
    ("💊", "Treat only as advised", "Ask for the product name, dose and timing. Do not mix products on your own. Follow the label."),
    ("🛒", "Buy safely", "Use the Buying inputs safely tab: licensed dealer, sealed pack, bill with batch number."),
    ("🌱", "Meanwhile, reduce spread", "Remove badly infected plant parts, improve airflow and drainage, and avoid walking through the wet crop."),
]

DISEASE_STEPS_KN = [
    ("📸", "ಸ್ಪಷ್ಟ ಛಾಯಾಚಿತ್ರಗಳನ್ನು ತೆಗೆಯಿರಿ", "ಬಾಧಿತ ಎಲೆಗಳ ಮುಂಭಾಗ ಮತ್ತು ಹಿಂಭಾಗದ ಹತ್ತಿರದ ಫೋಟೋ, ಇಡೀ ಗಿಡದ ಫೋಟೋ ಮತ್ತು ಜಮೀನಿನ ವಿಶಾಲ ನೋಟವನ್ನು ತೆಗೆಯಿರಿ. ಬೆಳೆಯ ಹೆಸರು, ಬೆಳೆಯ ವಯಸ್ಸು, ರೋಗ ಆರಂಭವಾದ ದಿನ ಮತ್ತು ಇತ್ತೀಚಿನ ಹವಾಮಾನವನ್ನು ದಾಖಲಿಸಿಕೊಳ್ಳಿ."),
    ("🧑‍🌾", "ಕೃಷಿ ತಜ್ಞರಿಂದ ರೋಗ ಖಚಿತಪಡಿಸಿಕೊಳ್ಳಿ", "ಫೋಟೋಗಳನ್ನು ಅಥವಾ ತಾಜಾ ರೋಗಪೀಡಿತ ಮಾದರಿಯನ್ನು ನಿಮ್ಮ ಹತ್ತಿರದ ಕೃಷಿ ವಿಜ್ಞಾನ ಕೇಂದ್ರಕ್ಕೆ {KVK}, ರೈತ ಸಂಪರ್ಕ ಕೇಂದ್ರಕ್ಕೆ {RSK} ಅಥವಾ ಕೃಷಿ ಅಧಿಕಾರಿಗೆ ತೋರಿಸಿ. ಹಲವು {KVK} ಗಳಲ್ಲಿ ಸಸ್ಯ ರೋಗ ಪತ್ತೆ ಪ್ರಯೋಗಾಲಯಗಳಿರುತ್ತವೆ."),
    ("💊", "ಶಿಫಾರಸು ಮಾಡಿದಂತೆ ಮಾತ್ರ ಔಷಧೋಪಚಾರ ಮಾಡಿ", "ಸೂಕ್ತ ಔಷಧದ ಹೆಸರು, ಸಿಂಪಡಣೆಯ ಪ್ರಮಾಣ ಮತ್ತು ಸಮಯವನ್ನು ತಜ್ಞರಿಂದ ತಿಳಿದುಕೊಳ್ಳಿ. ಸ್ವಂತವಾಗಿ ಯಾವುದೇ ರಾಸಾಯನಿಕಗಳನ್ನು ಮಿಶ್ರಣ ಮಾಡಬೇಡಿ. ಲೇಬಲ್ ಸೂಚನೆ ಪಾಲಿಸಿ."),
    ("🛒", "ಸುರಕ್ಷಿತವಾಗಿ ಖರೀದಿಸಿ", "'ಕೃಷಿ ಪರಿಕರಗಳ ಖರೀದಿ' ಟ್ಯಾಬ್‌ನಲ್ಲಿರುವಂತೆ ಪರವಾನಗಿ ಪಡೆದ ಡೀಲರ್ ಬಳಿ ಸೀಲ್ ಮಾಡಿದ ಪ್ಯಾಕ್ ಮತ್ತು ಬ್ಯಾಚ್ ನಂಬರ್ ಇರುವ ಬಿಲ್‌ನೊಂದಿಗೆ ಖರೀದಿಸಿ."),
    ("🌱", "ಈ ಮಧ್ಯೆ, ರೋಗ ಹರಡುವುದನ್ನು ತಡೆಯಿರಿ", "ತೀವ್ರವಾಗಿ ರೋಗಪೀಡಿತವಾದ ಎಲೆ ಮತ್ತು ಗಿಡಗಳನ್ನು ಕಿತ್ತು ನಾಶಪಡಿಸಿ, ಹೊಲದಲ್ಲಿ ಗಾಳಿ ಮತ್ತು ನೀರು ಸರಾಗವಾಗಿ ಹರಿಯುವಂತೆ ಮಾಡಿ, ಮತ್ತು ತೇವವಿರುವ ಬೆಳೆಯಲ್ಲಿ ತಿರುಗಾಡಬೇಡಿ."),
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


# Main view execution
is_kn = (i18n.current_lang() == "kn")

hero_title = "ಯೋಜನೆಗಳು ಮತ್ತು ಸಹಾಯ" if is_kn else "Schemes and help"
hero_sub = "ಕರ್ನಾಟಕದ ರೈತರಿಗಾಗಿ ಸರ್ಕಾರದ ಪ್ರಮುಖ ಯೋಜನೆಗಳು, ದಾಖಲೆಗಳು ಮತ್ತು ಸುರಕ್ಷಿತ ಖರೀದಿ ಮಾರ್ಗದರ್ಶನ." if is_kn else "Documents, steps and safe buying, for Karnataka farmers."
ui.hero(hero_title, hero_sub, "📋")

caption_text = (
    "ನಿಯಮಗಳು, ಕೊನೆಯ ದಿನಾಂಕಗಳು ಮತ್ತು ಮೊತ್ತಗಳು ಕಾಲಕಾಲಕ್ಕೆ ಬದಲಾಗುತ್ತವೆ. ಅರ್ಜಿ ಸಲ್ಲಿಸುವ ಮುನ್ನ ನಿಮ್ಮ ಬ್ಯಾಂಕ್, ಸಿಎಸ್‌ಸಿ {CSC} ಅಥವಾ ರೈತ ಸಂಪರ್ಕ ಕೇಂದ್ರದಲ್ಲಿ {RSK} ಖಚಿತಪಡಿಸಿಕೊಳ್ಳಿ. ಅಕ್ಟೋಬರ್ 2026 ರ ಅಧಿಕೃತ ಮೂಲಗಳ ಮಾಹಿತಿ."
    if is_kn else
    "Rules, dates and amounts change, so confirm with your bank, CSC or Raitha Samparka Kendra before you apply. Information last checked October 2026."
)
st.caption(caption_text)

tab_labels = ["ಯೋಜನೆಗಳು ಮತ್ತು ದಾಖಲೆಗಳು", "ಕೃಷಿ ಪರಿಕರಗಳ ಸುರಕ್ಷಿತ ಖರೀದಿ", "ಬೆಳೆ ರೋಗ ನಿರ್ವಹಣೆ ಸಹಾಯ"] if is_kn else ["Schemes and documents", "Buying inputs safely", "Crop disease help"]
tab1, tab2, tab3 = st.tabs(tab_labels)

schemes_dict = SCHEMES_KN if is_kn else SCHEMES_EN

with tab1:
    select_label = "ಯೋಜನೆಯನ್ನು ಆಯ್ಕೆಮಾಡಿ" if is_kn else "Choose a scheme"
    choice = st.selectbox(select_label, list(schemes_dict.keys()))
    s = schemes_dict[choice]
    
    what_label = "ಯೋಜನೆಯ ವಿವರ:" if is_kn else "What it is:"
    who_label = "ಅರ್ಹ ಫಲಾನುಭವಿಗಳು:" if is_kn else "Who can apply:"
    st.markdown(f"**{what_label}** {s['what']}")
    st.markdown(f"**{who_label}** {s['who']}")

    docs_title = "ಅಗತ್ಯ ದಾಖಲೆಗಳ ಪರಿಶೀಲನಾ ಪಟ್ಟಿ" if is_kn else "Documents checklist"
    st.subheader(docs_title)
    ticks = [st.checkbox(d, key=f"{s['slug']}_doc_{i}") for i, d in enumerate(s["documents"])]
    if all(ticks):
        success_msg = "ಎಲ್ಲ ದಾಖಲೆಗಳು ಸಿದ್ಧವಾಗಿವೆ. ನೀವು ಈಗ ಸುಲಭವಾಗಿ ಅರ್ಜಿ ಸಲ್ಲಿಸಬಹುದು." if is_kn else "All documents ready. You can go and apply."
        st.success(f"✅ {success_msg}")

    steps_title = "ಅರ್ಜಿ ಸಲ್ಲಿಸುವ ಹಂತಗಳು" if is_kn else "How to apply"
    st.subheader(steps_title)
    step_prefix = "ಹಂತ" if is_kn else "Step"
    for n, (icon, title, text) in enumerate(s["steps"], 1):
        st.markdown(f"**{icon} {step_prefix} {n}: {title}**")
        st.write(text)
        show_step_image(s["slug"], n)

    st.subheader(s["extra_title"])
    bullets(s["extra"])
    where_label = "ಅರ್ಜಿ ಸಲ್ಲಿಸಲು ಅಧಿಕೃತ ಮೂಲಗಳು:" if is_kn else "Where to go:"
    st.markdown(f"**{where_label}** " + " | ".join(s["links"]))

with tab2:
    fert_title = "ರಸಗೊಬ್ಬರ ಖರೀದಿ ನಿಯಮಗಳು" if is_kn else "Fertilizer"
    st.subheader(fert_title)
    bullets(FERTILIZER_KN if is_kn else FERTILIZER_EN)
    
    pest_title = "ಕೀಟನಾಶಕ ಖರೀದಿ ಮತ್ತು ಸುರಕ್ಷತೆ" if is_kn else "Pesticide"
    st.subheader(pest_title)
    bullets(PESTICIDE_KN if is_kn else PESTICIDE_EN)
    
    info_text = (
        "ನಿಮ್ಮ ಮಣ್ಣು ಅಥವಾ ಬೆಳೆಗೆ ಏನು ಅಗತ್ಯವಿದೆ ಎಂದು ತಿಳಿದ ನಂತರವೇ ರಸಗೊಬ್ಬರ ಮತ್ತು ಕೀಟನಾಶಕ ಖರೀದಿಸುವುದು ಪ್ರಯೋಜನಕಾರಿ. ಮೊದಲು ಮಣ್ಣು ಆರೋಗ್ಯ ಕಾರ್ಡ್ {Soil Health Card} ಮತ್ತು ತಜ್ಞರ ರೋಗನಿರ್ಣಯದಿಂದ ಪ್ರಾರಂಭಿಸಿ."
        if is_kn else
        "Fertilizer and pesticide are only worth buying once you know what your soil or crop needs. Start with a Soil Health Card and an expert diagnosis."
    )
    st.info(info_text)

with tab3:
    disease_intro = (
        "ಈ ಆ್ಯಪ್ ಸಸ್ಯ ರೋಗಗಳನ್ನು ಸ್ವತಃ ಅಂತಿಮವಾಗಿ ನಿರ್ಣಯಿಸುವುದಿಲ್ಲ. ಸರಿಯಾದ ಸಹಾಯ ಮತ್ತು ಸೂಕ್ತ ಪರಿಹಾರ ಪಡೆಯಲು ಈ ಹಂತಗಳನ್ನು ಅನುಸರಿಸಿ."
        if is_kn else
        "This app does not diagnose plant diseases. Follow these steps to get the right help and the right product."
    )
    st.write(disease_intro)
    
    steps_data = DISEASE_STEPS_KN if is_kn else DISEASE_STEPS_EN
    for n, (icon, title, text) in enumerate(steps_data, 1):
        step_str = f"ಹಂತ {n}" if is_kn else f"Step {n}"
        st.markdown(f"**{icon} {step_str}: {title}**")
        st.write(text)
        
    helpline_str = (
        "**ಸಹಾಯವಾಣಿ:** ಕಿಸಾನ್ ಕಾಲ್ ಸೆಂಟರ್: 1800-180-1551 | ತುರ್ತು ನೆರವು: 112"
        if is_kn else
        "**Help:** Kisan Call Centre 1800-180-1551 | Emergency 112"
    )
    st.markdown(helpline_str)

ui.feedback_box()
st.markdown("---")
footer_str = (
    "© 2026 ಅಭಿಷೇಕ್ ಹಿಟಬುತ್ತಿ. ಎಲ್ಲ ಹಕ್ಕುಗಳನ್ನು ಕಾಯ್ದಿರಿಸಲಾಗಿದೆ. ಅನುಮತಿ ಇಲ್ಲದೆ ಈ ಆ್ಯಪ್ ಅನ್ನು ನಕಲು ಮಾಡುವುದು ಅಥವಾ ಮರುಬಳಕೆ ಮಾಡುವುದು ನಿಷಿದ್ಧ."
    if is_kn else
    "© 2026 Abhishek Hitabutti. All rights reserved. Copying or reuse of this app without permission is prohibited."
)
st.caption(footer_str)
