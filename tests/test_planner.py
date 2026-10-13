"""Season planner content and page tests."""
import re
from pathlib import Path

import pytest
from streamlit.testing.v1 import AppTest

import planner_data as pdata

ROOT = Path(__file__).resolve().parent.parent
PAGE = str(ROOT / "pages" / "4_Season_Planner.py")
DOSE = re.compile(r"\d+(\.\d+)?\s*(g|gm|ml|kg|l|lit|litre|litres|liter)\b\s*(/|per)|@")
ALL_ITEMS = [i for items in pdata.ITEMS.values() for i in items]


def test_every_practice_has_steps_and_sources():
    ids = [i["id"] for i in ALL_ITEMS]
    assert len(ids) == len(set(ids)) and len(ids) >= 8
    for i in ALL_ITEMS:
        assert i["title"] and i["summary"] and i["steps"] and i["sources"], i["id"]
        for key in i["sources"]:
            assert pdata.SRC[key]["url"].startswith("https://"), (i["id"], key)


def test_no_doses_in_planner_content():
    for i in ALL_ITEMS:
        text = " ".join(str(v) for v in i.values())
        assert not DOSE.search(text), (i["id"], DOSE.search(text).group(0))


def test_stages_match_content_keys():
    assert set(pdata.STAGES) == set(pdata.ITEMS)


@pytest.mark.parametrize("sprouted,tested,level", [
    (90, 100, "good"), (85, 100, "good"), (82, 100, "ok"), (75, 100, "weak"), (40, 100, "low"),
    (17, 20, "good"), (120, 100, "error"), (5, 0, "error"),
])
def test_germination_verdict(sprouted, tested, level):
    assert pdata.germination_verdict(sprouted, tested)[1] == level


def test_percentage_with_fewer_seeds():
    assert pdata.germination_verdict(17, 20)[0] == 85.0


def test_page_loads_with_four_stage_tabs():
    at = AppTest.from_file(PAGE, default_timeout=30).run()
    assert not at.exception
    assert [t.label for t in at.tabs][:4] == pdata.STAGES


def test_calculator_shows_warning_for_weak_seed_and_success_for_good():
    at = AppTest.from_file(PAGE, default_timeout=30).run()
    at.number_input(key="gc_sprouted").set_value(60).run()
    assert any("Too low" in w.value for w in at.warning)
    at.number_input(key="gc_sprouted").set_value(90).run()
    assert any("Good" in s.value for s in at.success)
    assert not at.exception
