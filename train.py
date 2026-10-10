"""Train the KisanDrishti crop recommendation model.

Run:  python train.py
Writes: crop_recommendation_model.pkl, crop_profiles.pkl, metrics.json

To add a new crop: add labeled rows to Crop_recommendation.csv and run this script again.
"""
import json
import pickle
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split

FEATURES = ["N", "P", "K", "temperature", "humidity", "ph", "rainfall"]

DATA_NOTE = (
    "Public crop recommendation dataset (2,200 rows, 22 crops) built by augmenting "
    "rainfall, climate and fertilizer data for India. It is not field-collected data, "
    "so accuracy on real farms can be lower. Use the result as guidance and confirm "
    "with your agriculture officer."
)


def train(csv_path="Crop_recommendation.csv", out_dir="."):
    out_dir = Path(out_dir)
    df = pd.read_csv(csv_path)
    X = df[FEATURES].to_numpy()
    y = df["label"].to_numpy()

    # 1) Honest evaluation on a 20% hold-out set the model never trains on
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    eval_model = RandomForestClassifier(n_estimators=200, random_state=42, n_jobs=-1)
    eval_model.fit(X_train, y_train)
    pred = eval_model.predict(X_test)
    accuracy = accuracy_score(y_test, pred)
    report = classification_report(y_test, pred, output_dict=True, zero_division=0)

    # 2) Final model for the app: refit on all rows
    model = RandomForestClassifier(n_estimators=200, random_state=42, n_jobs=-1)
    model.fit(X, y)

    # 3) Ideal profile per crop: mean values plus a typical range (5th to 95th percentile)
    profiles = {}
    for crop, g in df.groupby("label"):
        profile = {f: float(g[f].mean()) for f in FEATURES}
        profile["ranges"] = {
            f: (float(np.percentile(g[f], 5)), float(np.percentile(g[f], 95)))
            for f in FEATURES
        }
        profiles[crop] = profile

    metrics = {
        "model": "RandomForestClassifier (200 trees)",
        "n_rows": int(len(df)),
        "n_crops": int(df["label"].nunique()),
        "test_size": 0.2,
        "holdout_accuracy": round(float(accuracy), 4),
        "per_crop_f1": {c: round(report[c]["f1-score"], 3) for c in sorted(profiles)},
        "data_note": DATA_NOTE,
    }

    with open(out_dir / "crop_recommendation_model.pkl", "wb") as f:
        pickle.dump(model, f)
    with open(out_dir / "crop_profiles.pkl", "wb") as f:
        pickle.dump(profiles, f)
    with open(out_dir / "metrics.json", "w") as f:
        json.dump(metrics, f, indent=2)
    return metrics


if __name__ == "__main__":
    m = train()
    print(f"Crops: {m['n_crops']} | Rows: {m['n_rows']}")
    print(f"Hold-out accuracy: {m['holdout_accuracy']:.2%}")
