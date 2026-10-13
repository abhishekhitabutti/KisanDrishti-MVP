"""Season planner: practices for each stage of the farming season, with sources."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import streamlit as st  # noqa: E402

import planner_data as pdata  # noqa: E402
import ui  # noqa: E402

st.set_page_config(page_title="Season Planner | KisanDrishti", page_icon="🗓️")
ui.inject_css()
ui.hero("Season planner", "What to do at each stage of the season. Every practice shows where it comes from.", "🗓️")
ui.steps_row([("🌱", "Before sowing"), ("🚜", "Sowing"), ("🌾", "Growing"), ("📦", "Harvest")])


def bullets(items):
    for item in items:
        st.markdown(f"- {item}")


def render_item(item):
    with st.expander(item["title"]):
        st.write(item["summary"])
        st.markdown("**Steps**")
        bullets(item["steps"])
        if item["cautions"]:
            st.markdown("**Be careful**")
            bullets(item["cautions"])
        st.markdown("**Sources**")
        for key in item["sources"]:
            s = pdata.SRC[key]
            st.markdown(f"- [{s['title']}]({s['url']})")
        if item["id"] == "seed_test":
            germination_calculator()


def germination_calculator():
    st.markdown("---")
    st.markdown("**Work out your germination percentage**")
    c1, c2 = st.columns(2)
    tested = c1.number_input("Seeds tested", min_value=1, max_value=1000, value=100, step=10, key="gc_tested")
    sprouted = c2.number_input("Seeds that sprouted", min_value=0, max_value=1000, value=0, step=1, key="gc_sprouted")
    pct, level, message = pdata.germination_verdict(sprouted, tested)
    if level == "error":
        st.warning(message)
    elif sprouted > 0:
        st.metric("Germination", f"{pct:.0f}%")
        (st.success if level in ("good", "ok") else st.warning)(message)
    st.caption("Thresholds follow Agriculture Victoria advice for cereal and pulse seed. Other crops differ, so ask your seed dealer or KVK.")


tabs = st.tabs(pdata.STAGES)
for tab, stage in zip(tabs, pdata.STAGES):
    with tab:
        if stage == "Growing season":
            st.write("While the crop grows, use these pages:")
            st.markdown("- **Weather precautions:** 7-day forecasts and what to do before bad weather. Open it from the menu.\n"
                        "- **Crop Doctor:** photograph a sick plant, pest or weed. Open it from the menu.\n"
                        "- **Mandi prices:** coming soon.")
            st.info("Check your field every few days. Catching a problem early makes it much easier to deal with.")
        for item in pdata.ITEMS[stage]:
            render_item(item)
        if stage == "Harvest and storage":
            st.info("If your insured crop is damaged by flooding, hail or similar, report it within 72 hours. See the Schemes and Help page.")

st.caption("General practices from published sources. Local conditions differ, so confirm with your KVK or agriculture officer. This app gives no doses.")
st.markdown("---")
st.caption("© 2026 Abhishek Hitabutti. All rights reserved. Copying or reuse of this app without permission is prohibited.")
