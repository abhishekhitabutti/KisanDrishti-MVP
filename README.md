# KrushiNudi (ಕೃಷಿನುಡಿ)

**Smart Farm Advisory · The Voice of Intelligent Agriculture**  
*Smarter Insights. Better Farming.*

**Live Application:** https://krushinudi-mvp.streamlit.app/  
**Source Code:** https://github.com/abhishekhitabutti/KisanDrishti-MVP

---

## About KrushiNudi

KrushiNudi is a farmer-first, bilingual (Kannada and English) precision agriculture platform engineered for Karnataka smallholder farmers. Developed by Abhishek Hitabutti, a B.Tech CSE (AI & ML) student at Amity University Bengaluru and the son of a farmer, KrushiNudi provides data-driven, actionable guidance across the entire crop season:
- **Pre-Sowing:** Soil nutrient-crop matching, seed germination rate testing, and scientific borewell groundwater feasibility advisory.
- **Sowing & Input Planning:** Non-chemical weed suppression, compost recycling, and minimum-effective-dose fertilizer guidance.
- **Growing Season:** Photo-based disease diagnosis with verified non-chemical cultural steps, integrated spray timing, and 7-day weather hazard forecasting.
- **Post-Harvest & Protection:** PMFBY 72-hour localized damage reporting assistance, PM-KISAN, KCC low-interest loan documentation, and grain storage precautions.

---

## Languages

Full bilingual support for **English** and **ಕನ್ನಡ (Kannada)** with a simple toggle on every page.
- In Kannada mode, interface text is 100% pure Kannada, with scientific and technical acronyms like `{N}`, `{P}`, `{K}`, `{pH}`, `{PMFBY}`, `{KCC}`, `{KVK}`, `{RSK}`, and `{AI}` preserved in clear braces.
- All 31 Karnataka districts are translated natively (`DISTRICTS_KN`).
- Developer and credit attributions are consistently localized as **ಅಭಿಷೇಕ್ ಹಿಟಬುತ್ತಿ**.

---

## Application Structure

`app.py` is the application entry point providing page routing, language state management, and configuration.

### Core Modules (`views/`)
1. **🌾 Crop Advisor (`views/home.py`):**  
   Evaluates 7 soil and climate parameters (Nitrogen, Phosphorus, Potassium, Soil pH, Temperature, Humidity, and Rainfall) against a trained Random Forest model. Recommends the highest-confidence crop among 22 varieties, maps field suitability, and flags nutrient deficiency pointers without prescribing unverified chemical doses.
2. **📖 User Guide & Interactive Demo (`views/guide.py`):**  
   A step-by-step interactive manual with built-in live simulation sandboxes for all tools, seed germination vigor calculator, weather hazard simulation, and document readiness meters.
3. **💧 Borewell Water Advisory (`views/borewell.py`):**  
   Data-backed groundwater feasibility analysis using Central Ground Water Board (CGWB) records across all 31 Karnataka districts. Estimates strike depth, extraction sustainability status, financial budgeting, and hard-stop drilling depth limits to protect farmers from dry-borewell debt traps.
4. **🩺 Crop Doctor (`views/crop_doctor.py`):**  
   Camera or gallery photo diagnosis powered by AI computer vision (Google Gemini free tier / Anthropic API). Diagnostic identification maps to a reviewed agricultural knowledge base (`knowledge/issues.json`) sourced from ICAR, TNAU, and State Agricultural Universities. Prioritizes non-chemical cultural practices first, displays approved active ingredients, and enforces weather-dependent spray rules.
5. **🗓️ Season Planner (`views/season_planner.py`):**  
   Practical guidelines for each lifecycle phase: Before Sowing, Sowing, Growing, and Harvest & Storage. Includes an interactive seed germination rate calculator and Custom Hiring Centre (CHC / ಕೃಷಿ ಯಂತ್ರಧಾರೆ) machinery rental awareness.
6. **⛈️ Weather Precautions (`views/weather.py`):**  
   Real-time 7-day agro-meteorological forecast from Open-Meteo across all 31 Karnataka districts. Features automated hazard triggers (heavy rainfall, wind gusts, heat stress, dry spells), an IMD warning tracker, and a chemical spray window planner (delay spray if rain ≥ 2.5 mm or gusts ≥ 30 km/h).
7. **📋 Schemes & Help (`views/schemes.py`):**  
   Interactive document readiness checklists and step-by-step application procedures for PMFBY (Crop Insurance with the critical 72-hour localized intimation rule), PM-KISAN, Kisan Credit Card (KCC), and Soil Health Card, plus certified input purchasing safety rules.
8. **ℹ️ About & Privacy (`views/about.py`):**  
   Full disclosure of AI/ML data sources, model boundaries, privacy commitments, and open-source credits.

---

## Authentication & Access Control

- **Frictionless Farmer Access:** Login is completely deactivated so farmers, village kiosks, and judges can access all tools immediately without any registration or passwords.
- **Enterprise Security Gate (Optional):** All underlying authentication logic, salted SHA-256 password hashing, persistent SQLite database storage (`kisan_users.db`), and Fast2SMS cellular SMS OTP verification are preserved in `auth.py` and can be re-enabled anytime by uncommenting `auth.require_auth()` in `app.py`.

---

## Safety & Ethics Principles

1. **No Unverified Doses:** Neither the ML model nor the AI vision API prescribes pesticide or fertilizer dosages. Dosages must always be verified on the official manufacturer label or with local KVK / Raitha Samparka Kendra officials.
2. **Non-Chemical First:** Cultural management (pruning, field sanitation, water drainage) is always prioritized before recommending chemical active ingredients.
3. **Data Privacy:** Photo GPS/location metadata is stripped before analysis. User plant photos are never stored permanently on the server.
4. **Weather-Gated Application:** Spraying is flagged as unsafe whenever rain or high winds would cause chemical wash-off or drift.

---

## Setting Up Photo Analysis (Free Tier)

Photo analysis utilizes Google AI Studio's free Gemini API tier:

1. Obtain a free API key at [aistudio.google.com](https://aistudio.google.com/).
2. In Streamlit Cloud Settings > Secrets (or local `.streamlit/secrets.toml`), configure:
   ```toml
   GEMINI_API_KEY = "your_actual_key"
   ```
3. Never commit API keys to version control. The app gracefully falls back to "Browse Common Problems" mode if no API key is provided.

---

## Running Locally

### Prerequisites
- Python 3.10+
- Virtual environment recommended

### Installation
```bash
git clone https://github.com/abhishekhitabutti/KisanDrishti-MVP.git
cd KisanDrishti-MVP
pip install -r requirements.txt
```

### Launch Application
```bash
streamlit run app.py
```

---

## Running Tests

Automated testing is built using `pytest` and Streamlit's headless `AppTest` framework:
```bash
pytest -v
```

---

## Project Roadmap (Smart India Hackathon / SIH Focus)

- **Module 1 (Pre-Sowing):** Borewell water table depth & feasibility estimation (Implemented) + Soil-crop matching (Implemented) + Seed germination testing (Implemented).
- **Module 2 (Sowing Season):** Non-chemical weed suppression planning and residue/livestock manure composting calculators to reduce synthetic DAP/urea dependency.
- **Module 3 (Growing Season):** Microclimate and humidity-driven fungal disease prediction (blast and blight early warning).
- **Module 4 (Harvest & Market):** Real-time Agmarknet / e-NAM mandi price tracking and cold storage accessibility.

---

## Author & Attribution

**Abhishek Hitabutti (ಅಭಿಷೇಕ್ ಹಿಟಬುತ್ತಿ)**  
B.Tech CSE (AI & ML), Amity University Bengaluru  
GitHub: [github.com/abhishekhitabutti](https://github.com/abhishekhitabutti)  
Email: [abhishekhitabutti@gmail.com](mailto:abhishekhitabutti@gmail.com)

© 2026 Abhishek Hitabutti. All rights reserved.
