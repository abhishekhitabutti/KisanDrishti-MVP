"""Shared look and feel for KrushiNudi pages."""
from html import escape

import streamlit as st

CSS = """
<style>
.block-container {padding-top: 1.2rem; max-width: 820px;}
.kd-hero {background: linear-gradient(135deg, #1B5E20 0%, #2E7D32 50%, #43A047 100%); color: #fff;
  padding: 1.5rem 1.4rem; border-radius: 18px; margin-bottom: 1.2rem; box-shadow: 0 4px 12px rgba(27,94,32,0.18);}
.kd-hero h1 {color: #fff !important; margin: 0; font-size: 1.85rem; line-height: 1.2; font-weight: 800;}
.kd-hero p {margin: .4rem 0 0; opacity: .95; font-size: .98rem;}
.kn-brand-banner {
  background: linear-gradient(135deg, #1B5E20 0%, #2E7D32 55%, #388E3C 100%);
  border-radius: 20px;
  padding: 24px 20px 22px 20px;
  text-align: center;
  color: #ffffff;
  box-shadow: 0 4px 16px rgba(27, 94, 32, 0.22);
  margin-bottom: 18px;
}
.kn-brand-title {
  font-size: 2.3rem;
  font-weight: 800;
  letter-spacing: -0.5px;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 10px;
  color: #ffffff !important;
}
.kn-brand-tagline {
  color: #E8F5E9;
  font-size: 0.96rem;
  font-weight: 500;
  margin-top: 4px;
  letter-spacing: 0.4px;
}
.kn-weather-ribbon {
  background: #ffffff;
  border: 1px solid #C8E6C9;
  border-left: 6px solid #2E7D32;
  border-radius: 14px;
  padding: 14px 18px;
  margin-bottom: 18px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.05);
}
.kn-card-badge {
  background: #2E7D32;
  color: #ffffff;
  font-size: 0.75rem;
  font-weight: bold;
  padding: 2px 8px;
  border-radius: 10px;
  float: right;
}
.kn-footer {
  background: #1B5E20;
  color: #E8F5E9;
  border-radius: 16px;
  padding: 20px 16px;
  text-align: center;
  margin-top: 26px;
  box-shadow: 0 2px 10px rgba(0,0,0,0.1);
}
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

/* --- Floto Usability Audit Fix 2: Utility Icons Discoverability & Affordance --- */
header[data-testid="stHeader"] {
  background: transparent !important;
  z-index: 99 !important;
}
[data-testid="stToolbar"] {
  right: 1.25rem !important;
  top: 0.6rem !important;
  display: flex !important;
  align-items: center !important;
  gap: 10px !important;
}
[data-testid="stToolbar"] button,
[data-testid="stHeader"] button,
button[data-testid="baseButton-headerNoPadding"],
[data-testid="stActionButton"] button,
[data-testid="stToolbarActionButton"] {
  background: #ffffff !important;
  color: #1B5E20 !important;
  border: 1.5px solid #A5D6A7 !important;
  border-radius: 20px !important;
  padding: 6px 14px !important;
  min-height: 38px !important;
  min-width: 38px !important;
  font-size: 0.95rem !important;
  font-weight: 600 !important;
  box-shadow: 0 2px 6px rgba(0, 0, 0, 0.08) !important;
  transition: all 0.2s ease-in-out !important;
}
[data-testid="stToolbar"] button:hover,
[data-testid="stHeader"] button:hover {
  background: #E8F5E9 !important;
  border-color: #2E7D32 !important;
  transform: translateY(-1px) !important;
  box-shadow: 0 4px 12px rgba(46, 125, 50, 0.2) !important;
}
[data-testid="stToolbar"] svg,
[data-testid="stHeader"] svg {
  width: 1.25rem !important;
  height: 1.25rem !important;
  fill: #1B5E20 !important;
}

/* --- Floto Usability Audit Fix 3: Manage App Viewport Spacing & Padding --- */
#manage-app-button,
[data-testid="manage-app-button"],
div[class*="viewerBadge_container"],
div[class*="viewerBadge"],
div[class*="manageApp"],
.viewerBadge_container__r5y7m,
.viewerBadge_link__qRIco {
  bottom: 24px !important;
  right: 24px !important;
  margin-bottom: 8px !important;
  margin-right: 8px !important;
  padding: 8px 16px !important;
  border-radius: 24px !important;
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.22) !important;
  background-color: #ffffff !important;
  border: 1px solid #C8E6C9 !important;
  z-index: 9999 !important;
}
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
        url = "mailto:abhishekhitabutti@gmail.com?subject=" + quote("KrushiNudi feedback") + "&body=" + quote(body)
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
