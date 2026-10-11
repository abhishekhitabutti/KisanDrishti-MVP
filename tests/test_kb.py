"""The knowledge base is safety-critical, so its shape and content rules are tested."""
import re

import diagnosis

KB = diagnosis.load_kb()
DOSE = re.compile(r"\d+(\.\d+)?\s*(g|gm|ml|kg|l|lit|litre|litres|liter)\b\s*(/|per)|@")
REQUIRED = ["id", "type", "name", "crops", "look_for", "why_it_happens", "act_now", "chemical",
            "precautions", "see_expert_if", "sources", "last_checked"]


def test_kb_is_not_empty_and_ids_are_unique():
    ids = [e["id"] for e in KB]
    assert len(ids) >= 6
    assert len(ids) == len(set(ids))


def test_every_entry_has_required_fields_and_sources():
    for e in KB:
        for key in REQUIRED:
            assert e.get(key), (e["id"], key)
        assert e["type"] in ("disease", "pest", "weed")
        assert e["chemical"]["options"] and e["chemical"]["when"], e["id"]
        for s in e["sources"]:
            assert s["url"].startswith("https://"), (e["id"], s)


def test_no_doses_are_given_anywhere():
    for e in KB:
        text = " ".join(str(v) for v in e.values())
        assert not DOSE.search(text), (e["id"], DOSE.search(text).group(0))


def test_shared_spray_rules_give_no_doses():
    for line in diagnosis.SPRAY_TIMING + diagnosis.SAFETY:
        assert not DOSE.search(line), line
