"""Shared look and feel for KrushiNudi pages."""
from html import escape

import streamlit as st

CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Noto+Sans+Kannada:wght@400;500;600;700&display=swap');

html, body, [class*="css"] {
  font-family: 'Plus Jakarta Sans', 'Noto Sans Kannada', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif !important;
}

.block-container {
  padding-top: 1.2rem !important;
  padding-bottom: 2.5rem !important;
  max-width: 980px !important;
}

.kd-hero {
  background: linear-gradient(135deg, #1B5E20 0%, #2E7D32 55%, #388E3C 100%);
  color: #ffffff;
  padding: 1.6rem 1.6rem;
  border-radius: 18px;
  margin-bottom: 1.4rem;
  box-shadow: 0 4px 16px rgba(27, 94, 32, 0.18);
}
.kd-hero h1 {
  color: #ffffff !important;
  margin: 0;
  font-size: 1.95rem;
  line-height: 1.25;
  font-weight: 800;
  letter-spacing: -0.3px;
}
.kd-hero p {
  margin: 0.45rem 0 0;
  opacity: 0.95;
  font-size: 1rem;
  line-height: 1.45;
}

.kn-brand-banner {
  background: linear-gradient(135deg, #1B5E20 0%, #2E7D32 55%, #388E3C 100%);
  border-radius: 20px;
  padding: 26px 22px 24px 22px;
  text-align: center;
  color: #ffffff;
  box-shadow: 0 6px 20px rgba(27, 94, 32, 0.22);
  margin-bottom: 18px;
  position: relative;
  overflow: hidden;
}
.kn-brand-title {
  font-size: 2.45rem;
  font-weight: 800;
  letter-spacing: -0.5px;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 12px;
  color: #ffffff !important;
  text-shadow: 0 2px 4px rgba(0, 0, 0, 0.12);
}
.kn-brand-tagline {
  color: #E8F5E9;
  font-size: 1rem;
  font-weight: 600;
  margin-top: 4px;
  letter-spacing: 0.5px;
}

.kn-weather-ribbon {
  background: #ffffff;
  border: 1px solid #C8E6C9;
  border-left: 6px solid #2E7D32;
  border-radius: 16px;
  padding: 16px 20px;
  margin-bottom: 18px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.05);
}

.kn-card-badge {
  background: #2E7D32;
  color: #ffffff;
  font-size: 0.78rem;
  font-weight: 700;
  padding: 3px 9px;
  border-radius: 12px;
  float: right;
}

.kn-footer {
  background: #1B5E20;
  color: #E8F5E9;
  border-radius: 18px;
  padding: 24px 18px;
  text-align: center;
  margin-top: 28px;
  box-shadow: 0 3px 12px rgba(0,0,0,0.12);
}

/* --- Unified Hero Section (Usability Audit Resolution) --- */
.kn-hero-unified {
  background: linear-gradient(135deg, #1B5E20 0%, #2E7D32 55%, #388E3C 100%);
  border-radius: 20px;
  padding: 26px 28px;
  color: #ffffff;
  box-shadow: 0 6px 20px rgba(27, 94, 32, 0.22);
  margin-bottom: 16px;
  position: relative;
  overflow: hidden;
}
.kn-hero-title {
  font-size: 2.35rem;
  font-weight: 800;
  letter-spacing: -0.5px;
  color: #ffffff !important;
  line-height: 1.15;
  margin: 0;
}
.kn-hero-tagline {
  font-size: 0.95rem;
  font-weight: 600;
  color: #C8E6C9;
  letter-spacing: 0.5px;
  text-transform: uppercase;
  margin-bottom: 4px;
}
.kn-hero-desc {
  font-size: 0.92rem;
  color: #E8F5E9;
  opacity: 0.95;
  margin-top: 6px;
  margin-bottom: 18px;
  font-weight: 500;
}
.kn-hero-cta-group {
  display: flex;
  gap: 12px;
  flex-wrap: wrap;
  align-items: center;
}
.kn-btn-cta-primary {
  background: #FFFFFF;
  color: #1B5E20 !important;
  font-weight: 700;
  font-size: 0.9rem;
  padding: 9px 20px;
  border-radius: 24px;
  text-decoration: none;
  box-shadow: 0 3px 10px rgba(0, 0, 0, 0.15);
  transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
  display: inline-flex;
  align-items: center;
  gap: 6px;
}
.kn-btn-cta-primary:hover {
  background: #E8F5E9;
  transform: translateY(-1px);
  box-shadow: 0 5px 14px rgba(0, 0, 0, 0.22);
  color: #0A3D0E !important;
}
.kn-btn-cta-secondary {
  background: rgba(255, 255, 255, 0.15);
  color: #FFFFFF !important;
  font-weight: 600;
  font-size: 0.9rem;
  padding: 9px 18px;
  border-radius: 24px;
  text-decoration: none;
  border: 1px solid rgba(255, 255, 255, 0.35);
  transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
  display: inline-flex;
  align-items: center;
  gap: 6px;
}
.kn-btn-cta-secondary:hover {
  background: rgba(255, 255, 255, 0.26);
  transform: translateY(-1px);
}
@media (max-width: 640px) {
  .kn-hero-unified {
    padding: 20px 18px;
  }
  .kn-hero-title {
    font-size: 1.85rem;
  }
  .kn-hero-cta-group {
    flex-direction: column;
    align-items: stretch;
  }
  .kn-btn-cta-primary, .kn-btn-cta-secondary {
    justify-content: center;
  }
}

.kd-card {
  background: #ffffff;
  border: 1px solid #DCE8DC;
  border-radius: 16px;
  padding: 1.1rem 1.2rem;
  margin: 0.7rem 0;
  box-shadow: 0 2px 6px rgba(0,0,0,0.04);
}
.kd-card h4 {
  margin: 0 0 0.4rem 0;
  color: #1B5E20;
  font-weight: 700;
}

.kd-badge {
  display: inline-block;
  padding: 0.2rem 0.7rem;
  border-radius: 999px;
  font-size: 0.78rem;
  font-weight: 700;
  color: #fff;
  margin: 0 0.35rem 0.25rem 0;
}

.kd-steps {display: flex; gap: .5rem; margin: .6rem 0 1rem 0;}
.kd-step {flex: 1; background: #F1F8E9; border-radius: 12px; padding: .6rem .5rem; text-align: center;
  font-size: .85rem; border: 1px solid #DCE8DC;}
.kd-step b {display: block; font-size: 1.3rem;}

.kd-stats {
  display: flex;
  gap: 0.75rem;
  margin: 0.6rem 0 1.2rem 0;
}
.kd-stat {
  flex: 1;
  background: #ffffff;
  border: 1px solid #DCE8DC;
  border-radius: 14px;
  padding: 0.75rem 0.6rem;
  text-align: center;
  box-shadow: 0 1px 4px rgba(0, 0, 0, 0.03);
}
.kd-stat b {
  display: block;
  font-size: 1.6rem;
  color: #1B5E20;
  line-height: 1.15;
}
.kd-stat span {
  font-size: 0.82rem;
  color: #4A5A4A;
  font-weight: 500;
}

.kn-safety-strip {
  display: flex;
  gap: 10px;
  margin: 12px 0 16px 0;
  flex-wrap: wrap;
}
.kn-safety-card {
  flex: 1;
  min-width: 105px;
  background: #F9FAF9;
  border: 1px solid #DCE8DC;
  border-radius: 12px;
  padding: 10px 6px;
  text-align: center;
  font-size: 0.78rem;
  font-weight: 600;
  color: #2E4B2E;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.02);
}
.kn-safety-card div {
  font-size: 1.35rem;
  margin-bottom: 4px;
}

.kd-card-icon {font-size: 1.6rem; line-height: 1;}
[data-testid="stSidebar"] {background: #F4F8F4 !important; border-right: 1px solid #E0EAE0 !important;}
.kd-warn {background: #FFF8E1; border-left: 5px solid #F9A825; padding: .7rem .9rem; border-radius: 8px; margin: .6rem 0;}
.kd-stop {background: #FDECEA; border-left: 5px solid #C62828; padding: .7rem .9rem; border-radius: 8px; margin: .6rem 0;}

/* --- Completely Hide Developer Toolbar, Cloud Badges & Watermarks for Visitors --- */
header[data-testid="stHeader"] {
  background: transparent !important;
  color: transparent !important;
}

header[data-testid="stHeader"] > div:not([data-testid="stSidebarCollapsedControl"]) {
  display: none !important;
  visibility: hidden !important;
  opacity: 0 !important;
  pointer-events: none !important;
  width: 0 !important;
  height: 0 !important;
  overflow: hidden !important;
}

[data-testid="stSidebarCollapsedControl"] {
  display: block !important;
  visibility: visible !important;
  z-index: 99999 !important;
}

#GithubIcon,
header a[href*="github.com"],
header a[href*="github"],
header button,
header [data-testid="stToolbarActions"],
[data-testid="stToolbar"],
[data-testid="stToolbarActions"],
[data-testid="stHeaderActions"],
[data-testid="stHeaderActionElements"],
[data-testid="stDecoration"],
[data-testid="stStatusWidget"],
.stAppDeployButton,
.stDeployButton,
button[data-testid="stToolbarActionButton"],
button[data-testid="baseButton-headerNoPadding"],
button[title="Fork this app"],
button[title="Star this app"],
button[title="Share this app"],
button[title="View source code"],
div[class*="stAppToolbar"],
div[class*="Toolbar"],
div[class*="toolbar"],
div[class*="headerActions"],
div[data-testid="stToolbarActions"],
div[data-testid="stToolbarFloatingFrame"],
#MainMenu,
footer,
[data-testid="stFooter"],
#manage-app-button,
[data-testid="manage-app-button"],
div[class*="viewerBadge_container"],
div[class*="viewerBadge"],
div[class*="manageApp"],
div[class*="floatingBadge"],
div[class*="StreamlitBranding"],
a[class*="viewerBadge"],
.viewerBadge_container__r5y7m,
.viewerBadge_link__qRIco {
  display: none !important;
  visibility: hidden !important;
  opacity: 0 !important;
  height: 0 !important;
  width: 0 !important;
  pointer-events: none !important;
  overflow: hidden !important;
  position: absolute !important;
  left: -9999px !important;
  top: -9999px !important;
}

/* --- Enterprise Agricultural Theme Polish --- */
.block-container {
  padding-top: 1.2rem !important;
  padding-bottom: 2.5rem !important;
  max-width: 960px !important;
}
div[data-testid="stVerticalBlockBorderWrapper"] > div {
  border-radius: 14px !important;
  border-color: #DCE8DC !important;
  background-color: #FFFFFF !important;
  box-shadow: 0 1px 4px rgba(0, 0, 0, 0.04) !important;
  transition: box-shadow 0.2s ease, border-color 0.2s ease !important;
}
div[data-testid="stVerticalBlockBorderWrapper"] > div:hover {
  border-color: #A5D6A7 !important;
  box-shadow: 0 4px 12px rgba(46, 125, 50, 0.08) !important;
}
.stButton > button {
  border-radius: 10px !important;
  font-weight: 600 !important;
  border: 1px solid #C8E6C9 !important;
  transition: all 0.2s ease !important;
}
.stButton > button:hover {
  border-color: #2E7D32 !important;
  background-color: #E8F5E9 !important;
  color: #1B5E20 !important;
}
[data-testid="stPageLink-NavLink"] {
  border-radius: 10px !important;
  padding: 6px 12px !important;
  font-weight: 500 !important;
  transition: all 0.2s ease !important;
}
[data-testid="stPageLink-NavLink"]:hover {
  background-color: #E8F5E9 !important;
  color: #1B5E20 !important;
}
button[data-baseweb="tab"] {
  font-weight: 600 !important;
  font-size: 0.92rem !important;
}
button[data-baseweb="tab"][aria-selected="true"] {
  color: #1B5E20 !important;
  border-bottom-color: #2E7D32 !important;
}

/* ====================================================================
   PREMIUM SEGMENTED LANGUAGE SWITCHER (TOP BAR & SIDEBAR)
   ==================================================================== */
/* Top bar language buttons */
div.st-key-top_bar_en, div.st-key-top_bar_kn {
  display: flex !important;
}

div.st-key-top_bar_en button, div.st-key-top_bar_kn button {
  border-radius: 24px !important;
  font-size: 0.85rem !important;
  font-weight: 700 !important;
  height: 36px !important;
  min-height: 36px !important;
  padding: 4px 14px !important;
  transition: all 0.22s cubic-bezier(0.16, 1, 0.3, 1) !important;
  display: flex !important;
  align-items: center !important;
  justify-content: center !important;
  letter-spacing: 0.2px !important;
}

/* Active Selected Language: Luxurious Emerald Gradient with Soft Ambient Glow */
div.st-key-top_bar_en button:disabled, div.st-key-top_bar_kn button:disabled,
div.st-key-top_bar_en button[kind="primary"], div.st-key-top_bar_kn button[kind="primary"] {
  background: linear-gradient(135deg, #1B5E20 0%, #2E7D32 100%) !important;
  color: #FFFFFF !important;
  border: 1px solid #1B5E20 !important;
  box-shadow: 0 3px 10px rgba(27, 94, 32, 0.28) !important;
  opacity: 1 !important;
  cursor: default !important;
  pointer-events: none !important;
}

/* Inactive Clickable Language: Crisp Clean Pill with Soft Border & Hover Feedback */
div.st-key-top_bar_en button[kind="secondary"], div.st-key-top_bar_kn button[kind="secondary"] {
  background: #FFFFFF !important;
  color: #2E7D32 !important;
  border: 1.5px solid #C8E6C9 !important;
  box-shadow: 0 1px 4px rgba(0, 0, 0, 0.04) !important;
  cursor: pointer !important;
}

div.st-key-top_bar_en button[kind="secondary"]:hover, div.st-key-top_bar_kn button[kind="secondary"]:hover {
  background: #E8F5E9 !important;
  border-color: #2E7D32 !important;
  color: #1B5E20 !important;
  transform: translateY(-1px) !important;
  box-shadow: 0 4px 10px rgba(46, 125, 50, 0.16) !important;
}

/* Sidebar Modern Segmented Control for Radio */
div[data-testid="stSidebar"] div[role="radiogroup"] {
  display: flex !important;
  background: #F1F8F1 !important;
  border: 1.5px solid #C8E6C9 !important;
  border-radius: 28px !important;
  padding: 4px !important;
  gap: 4px !important;
  margin-top: 4px !important;
  margin-bottom: 8px !important;
}

div[data-testid="stSidebar"] div[role="radiogroup"] > label {
  flex: 1 !important;
  margin: 0 !important;
  padding: 6px 12px !important;
  border-radius: 22px !important;
  justify-content: center !important;
  text-align: center !important;
  background: transparent !important;
  transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1) !important;
  cursor: pointer !important;
  border: none !important;
}

div[data-testid="stSidebar"] div[role="radiogroup"] > label > div:first-child {
  display: none !important; /* Discard old-fashioned radio circles */
}

div[data-testid="stSidebar"] div[role="radiogroup"] > label p {
  margin: 0 !important;
  font-weight: 600 !important;
  font-size: 0.85rem !important;
  color: #2E7D32 !important;
}

div[data-testid="stSidebar"] div[role="radiogroup"] > label[data-checked="true"],
div[data-testid="stSidebar"] div[role="radiogroup"] > label:has(input:checked) {
  background: linear-gradient(135deg, #1B5E20 0%, #2E7D32 100%) !important;
  box-shadow: 0 3px 8px rgba(27, 94, 32, 0.25) !important;
}

div[data-testid="stSidebar"] div[role="radiogroup"] > label[data-checked="true"] p,
div[data-testid="stSidebar"] div[role="radiogroup"] > label:has(input:checked) p {
  color: #FFFFFF !important;
  font-weight: 700 !important;
}

/* Mobile viewport adjustments */
@media (max-width: 640px) {
  div.st-key-top_bar_en button, div.st-key-top_bar_kn button {
    font-size: 0.78rem !important;
    height: 34px !important;
    min-height: 34px !important;
    padding: 2px 8px !important;
  }
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
    inject_css()
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
