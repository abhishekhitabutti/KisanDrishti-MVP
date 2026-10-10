"""Tests for the crop model pipeline."""
import pickle
import sys
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
import train  # noqa: E402


def test_dataset_is_clean():
    df = pd.read_csv(ROOT / "Crop_recommendation.csv")
    assert list(df.columns) == train.FEATURES + ["label"]
    assert df["label"].nunique() == 22
    assert df.isna().sum().sum() == 0
    assert df["ph"].between(0, 14).all()
    assert df["humidity"].between(0, 100).all()


def test_model_learns_real_patterns(tmp_path):
    metrics = train.train(ROOT / "Crop_recommendation.csv", tmp_path)
    # Random guessing over 22 crops would score about 4.5%
    assert metrics["holdout_accuracy"] > 0.95
    assert metrics["n_crops"] == 22


def test_profiles_cover_every_crop(tmp_path):
    train.train(ROOT / "Crop_recommendation.csv", tmp_path)
    with open(tmp_path / "crop_profiles.pkl", "rb") as f:
        profiles = pickle.load(f)
    assert len(profiles) == 22
    for crop, p in profiles.items():
        for feature in train.FEATURES:
            lo, hi = p["ranges"][feature]
            assert lo <= p[feature] <= hi, (crop, feature)


def test_typical_rice_field_predicts_rice(tmp_path):
    train.train(ROOT / "Crop_recommendation.csv", tmp_path)
    with open(tmp_path / "crop_recommendation_model.pkl", "rb") as f:
        model = pickle.load(f)
    rice_like = np.array([[90, 42, 43, 20.9, 82.0, 6.5, 203.0]])
    assert model.predict(rice_like)[0] == "rice"


def test_prediction_is_stable_for_small_changes(tmp_path):
    train.train(ROOT / "Crop_recommendation.csv", tmp_path)
    with open(tmp_path / "crop_recommendation_model.pkl", "rb") as f:
        model = pickle.load(f)
    df = pd.read_csv(ROOT / "Crop_recommendation.csv")
    X = df[train.FEATURES].to_numpy()
    nudged = X.copy()
    nudged[:, 0] += 1
    flipped = (model.predict(nudged) != model.predict(X)).mean()
    assert flipped < 0.05
