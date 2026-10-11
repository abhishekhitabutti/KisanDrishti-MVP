import io
import json
import sys
import urllib.request
from pathlib import Path

import pytest
import streamlit as st

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))


class FakeResponse(io.BytesIO):
    def __enter__(self):
        return self

    def __exit__(self, *args):
        return False


def forecast_payload(rain=(0, 0, 0), gust=(10, 10, 10)):
    days = ["2026-10-11", "2026-10-12", "2026-10-13"]
    return {"daily": {"time": days, "precipitation_sum": list(rain), "wind_gusts_10m_max": list(gust)},
            "hourly": {"time": [], "relative_humidity_2m": []}}


@pytest.fixture(autouse=True)
def no_real_network(monkeypatch):
    """Every test gets a calm, dry fake forecast unless it installs its own fake."""
    def fake_urlopen(url, timeout=0):
        return FakeResponse(json.dumps(forecast_payload()).encode())
    monkeypatch.setattr(urllib.request, "urlopen", fake_urlopen)
    st.cache_data.clear()
    yield
    st.cache_data.clear()
