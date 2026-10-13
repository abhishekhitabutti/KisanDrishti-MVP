# KisanDrishti

A farmer-first advisory web app for Karnataka: crop suggestions, a photo-based Crop Doctor, weather precautions, and step-by-step help with schemes and safe buying of inputs.

**Live demo:** https://kisandrishti-mvp.streamlit.app/

## Pages

- **Crop advisor (home):** enter 7 field measures and get the top 3 crops with confidence and nutrient pointers. "Check any crop" shows how your field fits each of the 22 crops in the training data.
- **Crop Doctor:** upload or take a photo of a plant problem, pest or weed. An AI vision model (free Gemini tier) identifies it. Treatment advice never comes from the AI: it comes from a reviewed knowledge base (`knowledge/issues.json`) with sources, and only when the match is confident. Otherwise the app sends the farmer to an expert. Includes spray-timing check from the weather forecast, and safety precautions.
- **Weather precautions:** 7-day forecast by district, hazard flags, matching precautions, and entry of an official IMD warning.
- **Season planner:** practices for each stage of the season (seed germination test with a calculator, summer ploughing and solarisation, stale seedbed, cover crops, compost, fertilizer use, safe grain storage, renting machinery), each with its sources and no doses.
- **Schemes and help:** document checklists and steps for PMFBY, PM-KISAN, KCC and Soil Health Card; safe buying of fertilizer and pesticide.

## How the Crop Doctor stays safe

1. The model returns only an identification (crop, category, matching knowledge-base id, confidence). It is told not to give treatment or doses.
2. `diagnosis.decide()` allows chemical guidance only for a medium or high confidence match with a reviewed entry for that crop. Everything else is "get expert help".
3. The knowledge base never contains doses (a test enforces this). Doses come from the product label or the agriculture officer.
4. Photo quality and low confidence lead to a "retake photo" or "see an expert" screen, not a guess.

## Setting up photo analysis (free)

Photo analysis uses Google's Gemini API free tier. No credit card is needed.

1. Open aistudio.google.com, sign in with a Google account, choose Get API key, then Create API key.
2. In Streamlit Cloud open your app, then Settings, then Secrets, and paste:

```
GEMINI_API_KEY = "your-key"
```

3. Never put the key in GitHub, and do not enable billing on the Google project, or the free tier no longer applies.
4. If a photo gives a model error, add `GEMINI_MODEL = "name"` to Secrets using a model name shown in AI Studio.

Free-tier limits are shown per project in AI Studio and can change. Each visit is limited to 5 photos to protect the free quota. When the limit is reached, the page tells the farmer to use the Browse tab.

**Privacy:** on Google's free tier, Google may use the content to improve its products. The app says so on the page, removes location data from every photo before sending, asks users not to upload photos with people, and does not store photos. If you prefer a paid service with different terms, set `ANTHROPIC_API_KEY` instead; the free Gemini key is used first when both exist. Without any key, the page works in browse mode and sends nothing anywhere.

## Data and limits

- Crop model: public crop recommendation dataset (2,200 rows, 22 crops) described as built by augmenting rainfall, climate and fertilizer data for India. Hold-out accuracy is 99.5%, but it is not field-collected data, so real-farm accuracy can be lower.
- Crop Doctor knowledge base: 6 reviewed entries so far (rice blast, maize fall armyworm, tomato early and late blight, parthenium, nutgrass). Some sources are from outside India. It needs review by an agriculture expert before wide use. More entries are added only with sources.
- Weather hazard thresholds are simple rules, except rainfall classes which follow IMD. Scheme rules and dates change.

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

1. More reviewed Crop Doctor and Season Planner entries, reviewed by a KVK or agricultural university
2. Crop library for more crops (needs a reviewed open dataset)
3. Kannada and English toggle with native-speaker review
4. Farmer and agriculture officer feedback form
5. Mandi prices, weather-linked disease risk, borewell water estimate

## Author

Abhishek Hitabutti, B.Tech CSE (AI & ML), Amity University Bengaluru. GitHub: https://github.com/abhishekhitabutti

(c) 2026 Abhishek Hitabutti. All rights reserved.
