"""Shared look and feel for KisanDrishti pages."""
from html import escape

import streamlit as st

CSS = """
<style>
.block-container {padding-top: 1.2rem; max-width: 780px;}
.kd-hero {background: linear-gradient(135deg, #1B5E20 0%, #43A047 100%); color: #fff;
  padding: 1.3rem 1.2rem; border-radius: 16px; margin-bottom: 1rem;}
.kd-hero h1 {color: #fff; margin: 0; font-size: 1.7rem; line-height: 1.2;}
.kd-hero p {margin: .35rem 0 0; opacity: .95; font-size: .98rem;}
.kd-card {background: #fff; border: 1px solid #DCE8DC; border-radius: 14px; padding: .9rem 1rem;
  margin: .6rem 0; box-shadow: 0 1px 3px rgba(0,0,0,.06);}
.kd-card h4 {margin: 0 0 .35rem 0; color: #1B5E20;}
.kd-badge {display: inline-block; padding: .15rem .65rem; border-radius: 999px; font-size: .78rem;
  font-weight: 700; color: #fff; margin: 0 .35rem .25rem 0;}
.kd-steps {display: flex; gap: .5rem; margin: .6rem 0 1rem 0;}
.kd-step {flex: 1; background: #F1F8E9; border-radius: 12px; padding: .6rem .5rem; text-align: center;
  font-size: .85rem; border: 1px solid #DCE8DC;}
.kd-step b {display: block; font-size: 1.3rem;}
.kd-stats {display: flex; gap: .5rem; margin: .4rem 0 1rem 0;}
.kd-stat {flex: 1; background: #fff; border: 1px solid #DCE8DC; border-radius: 12px; padding: .6rem .4rem; text-align: center;}
.kd-stat b {display: block; font-size: 1.5rem; color: #1B5E20; line-height: 1.1;}
.kd-stat span {font-size: .8rem; color: #4A5A4A;}
.kd-card-icon {font-size: 1.6rem; line-height: 1;}
[data-testid="stSidebar"] {background: #F1F8E9;}
.kd-warn {background: #FFF8E1; border-left: 5px solid #F9A825; padding: .7rem .9rem; border-radius: 8px; margin: .6rem 0;}
.kd-stop {background: #FDECEA; border-left: 5px solid #C62828; padding: .7rem .9rem; border-radius: 8px; margin: .6rem 0;}
</style>
"""

BADGE_COLOURS = {
    "disease": "#C62828", "pest": "#E65100", "weed": "#6A1B9A",
    "nutrient_deficiency": "#1565C0", "abiotic_stress": "#00838F", "healthy": "#2E7D32",
    "unclear": "#616161", "high": "#2E7D32", "medium": "#B8860B", "low": "#C62828",
}


def inject_css():
    st.markdown(CSS, unsafe_allow_html=True)


def hero(title, subtitle="", icon=""):
    st.markdown(
        f'<div class="kd-hero"><h1>{escape(icon)} {escape(title)}</h1><p>{escape(subtitle)}</p></div>',
        unsafe_allow_html=True,
    )


def badge(text, kind):
    colour = BADGE_COLOURS.get(kind, "#616161")
    return f'<span class="kd-badge" style="background:{colour}">{escape(text)}</span>'


def steps_row(steps):
    cells = "".join(f'<div class="kd-step"><b>{escape(icon)}</b>{escape(label)}</div>' for icon, label in steps)
    st.markdown(f'<div class="kd-steps">{cells}</div>', unsafe_allow_html=True)


def feedback_box():
    """Feedback link on every page. Set FEEDBACK_URL in Secrets to use a form; otherwise it opens an email."""
    import os
    from urllib.parse import quote

    from i18n import t
    try:
        url = st.secrets.get("FEEDBACK_URL")
    except Exception:
        url = None
    url = url or os.environ.get("FEEDBACK_URL")
    if not url:
        body = "Page I used:\nWhat was wrong or missing:\nI am a (farmer / agriculture officer / student):\n"
        url = "mailto:abhishekhitabutti@gmail.com?subject=" + quote("KisanDrishti feedback") + "&body=" + quote(body)
    with st.container(border=True):
        st.markdown("**" + t("Feedback") + "**")
        st.write(t("Something wrong or missing? Tell us. Farmers and agriculture officers: your feedback makes this app safer."))
        st.markdown(f"[{t('Send feedback')}]({url})")


def stat_row(items):
    cells = "".join(f'<div class="kd-stat"><b>{escape(str(v))}</b><span>{escape(l)}</span></div>' for v, l in items)
    st.markdown(f'<div class="kd-stats">{cells}</div>', unsafe_allow_html=True)


def page_link(path, label, icon=""):
    """A link to another page. Falls back to plain text when the page is not registered (for example in tests)."""
    try:
        st.page_link(path, label=label, icon=icon or None)
    except Exception:
        st.markdown(f"{icon} {label}")


def note(text, kind="warn"):
    st.markdown(f'<div class="kd-{kind}">{escape(text)}</div>', unsafe_allow_html=True)
