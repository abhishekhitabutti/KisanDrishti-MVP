# KisanDrishti

A farmer-first advisory web app for Karnataka: crop suggestions, weather precautions, and step-by-step help with schemes and safe buying of inputs.

**Live demo:** https://kisandrishti-mvp.streamlit.app/

## What it does

- **Crop advisor (home page):** enter 7 field measures (N, P, K, temperature, humidity, pH, rainfall) and get the top 3 crops with confidence, plus nutrient pointers for the best match. A "Check any crop" tool shows how your field fits each of the 22 crops.
- **Weather precautions:** 7-day forecast by Karnataka district (Open-Meteo, refreshed about every 30 minutes), hazard flags for the next 3 days, matching precautions, and a way to enter an official IMD warning you heard on the government telecast.
- **Schemes and help:** documents checklists and steps for crop insurance (PMFBY), PM-KISAN, Kisan Credit Card and Soil Health Card; safe buying of fertilizer and pesticide; and how to get a crop disease diagnosed.

## How it works

`Crop_recommendation.csv` -> `train.py` (Random Forest, 20% hold-out evaluation) -> `crop_recommendation_model.pkl`, `crop_profiles.pkl`, `metrics.json` -> `app.py`.

Adding a crop means adding labeled rows to the CSV and running `python train.py`.

## Data and limits

The model is trained on a public crop recommendation dataset (2,200 rows, 22 crops) that its authors describe as built by augmenting rainfall, climate and fertilizer data for India. Hold-out accuracy is 99.5%, but this is a clean dataset and is **not field-collected data**, so accuracy on real farms can be lower. N, P and K are on the dataset's scale, not lab readings. The app gives guidance, not doses. Weather hazard thresholds are simple rules, except rainfall classes which follow IMD. Rules and dates for schemes change, so confirm locally.

## Run locally

```
pip install -r requirements.txt
python train.py
streamlit run app.py
```

## Tests

```
pip install pytest
pytest -q
```

GitHub Actions runs the tests on every push.

## Roadmap

1. Kannada and English language toggle (with native-speaker review)
2. Farmer and agriculture officer feedback form
3. Mandi price tracking
4. Weather-triggered crop disease risk
5. Borewell water estimate from public groundwater data (inverse distance weighting)

## Author

Abhishek Hitabutti, B.Tech CSE (AI & ML), Amity University Bengaluru. GitHub: https://github.com/abhishekhitabutti

(c) 2026 Abhishek Hitabutti. All rights reserved.
