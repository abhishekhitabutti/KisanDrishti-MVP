"""Simple English/Kannada switch. English text is the key; a missing translation falls back to English."""
import json
from pathlib import Path

import streamlit as st

HERE = Path(__file__).resolve().parent
LANGS = {"en": "English", "kn": "ಕನ್ನಡ"}
REVIEW_NOTICE = ("This Kannada translation was made with machine help and has not been checked by an expert. "
                 "If anything is unclear, switch to English or ask your agriculture officer.")
UNTRANSLATED = "This page is not translated into Kannada yet."


@st.cache_resource
def _kannada():
    for base in (HERE, Path.cwd()):
        path = base / "translations" / "kn.json"
        if path.exists():
            return json.loads(path.read_text(encoding="utf-8"))
    return {}


UNTRANSLATED_PAGES = set()


def current_lang():
    radio = st.session_state.get("lang_radio")
    if radio is not None:
        return "kn" if radio == LANGS["kn"] else "en"
    return st.session_state.get("lang", "en")


def t(text, **kw):
    """Translate an English string, then fill in {placeholders}."""
    out = _kannada().get(text, text) if current_lang() == "kn" else text
    return out.format(**kw) if kw else out


def crop(name):
    """Crop name: in Kannada mode show Kannada name with English reference."""
    if current_lang() == "kn":
        kn = _kannada().get(f"crop:{name}")
        if kn:
            return f"{kn} ({name})"
    return name


def language_picker(translated=True):
    lang = current_lang()
    with st.sidebar:
        logo_path = HERE / "images" / "krushinudi_logo.jpg"
        if logo_path.exists():
            st.image(str(logo_path), use_container_width=True)
            if lang == "kn":
                st.markdown(
                    "<div style='text-align: center; margin-top: -6px; margin-bottom: 12px;'>"
                    "<div style='font-size: 1.25rem; font-weight: 800; color: #1B5E20;'>ಕೃಷಿನುಡಿ</div>"
                    "<div style='font-size: 0.76rem; font-weight: 600; color: #2E7D32;'>— ಬುದ್ಧಿವಂತ ಕೃಷಿಯ ಧ್ವನಿ —</div>"
                    "<div style='font-size: 0.7rem; color: #555; margin-top: 2px;'>🌱 ಬೆಳೆ ಸಲಹೆ · 💧 ಬೋರ್‌ವೆಲ್ · ⛅ ಹವಾಮಾನ · 🐛 ರೋಗ ಪತ್ತೆ · 📈 ಮಾರುಕಟ್ಟೆ</div>"
                    "</div>",
                    unsafe_allow_html=True
                )
            else:
                st.markdown(
                    "<div style='text-align: center; margin-top: -6px; margin-bottom: 12px;'>"
                    "<div style='font-size: 1.25rem; font-weight: 800; color: #1B5E20;'>KrushiNudi</div>"
                    "<div style='font-size: 0.76rem; font-weight: 600; color: #2E7D32;'>— AI Powered Farming Guidance —</div>"
                    "<div style='font-size: 0.7rem; color: #555; margin-top: 2px;'>🌱 Crop Advice · 💧 Borewell · ⛅ Weather · 🐛 Pest Doctor · 📈 Market</div>"
                    "</div>",
                    unsafe_allow_html=True
                )
        else:
            st.markdown(
                """
                <div style="background: linear-gradient(135deg, #1B5E20 0%, #2E7D32 100%); padding: 14px 14px 12px 14px; border-radius: 14px; text-align: center; color: white; margin-bottom: 12px; box-shadow: 0 3px 10px rgba(27, 94, 32, 0.2);">
                    <div style="font-size: 1.3rem; font-weight: 800; letter-spacing: -0.3px; display: flex; align-items: center; justify-content: center; gap: 8px;">
                        <span>🌾</span> KrushiNudi <span>🍃</span>
                    </div>
                    <div style="font-size: 0.76rem; color: #E8F5E9; margin-top: 2px; font-weight: 500;">
                        The Voice of Intelligent Agriculture
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )
        st.markdown("**🌐 ಭಾಷೆ / Language**")
        choice = st.radio(
            "Language / ಭಾಷೆ",
            list(LANGS.values()),
            index=0 if lang == "en" else 1,
            horizontal=True,
            key="lang_radio",
            label_visibility="collapsed",
        )
        st.session_state["lang"] = "kn" if choice == LANGS["kn"] else "en"
        if st.session_state["lang"] == "kn":
            st.caption(t(REVIEW_NOTICE))
            if not translated:
                st.info(t(UNTRANSLATED))
        st.markdown("---")
    return st.session_state["lang"]


def top_language_bar():
    """Prominent, mobile-friendly language switcher rendered at the top of the main container."""
    try:
        lang = current_lang()
        with st.container():
            col_l1, col_l2 = st.columns([2.2, 1.8])
            with col_l1:
                brand_sub = "ಬುದ್ಧಿವಂತ ಕೃಷಿಯ ಧ್ವನಿ" if lang == "kn" else "Smart Farm Advisory"
                st.markdown(
                    f"<div style='font-size:1.05rem; font-weight:800; color:#1B5E20; padding-top:4px; display:flex; align-items:center; gap:6px;'>"
                    f"🌾 <b>KrushiNudi</b> <span style='font-size:0.75rem; font-weight:600; color:#2E7D32; background:#E8F5E9; padding:2px 8px; border-radius:8px;'>{brand_sub}</span></div>",
                    unsafe_allow_html=True
                )
            with col_l2:
                b1, b2 = st.columns(2)
                with b1:
                    if lang == "en":
                        st.markdown(
                            "<div style='background:#2E7D32; color:#ffffff; font-size:0.8rem; font-weight:700; padding:5px 4px; border-radius:8px; text-align:center;'>🇬🇧 English</div>",
                            unsafe_allow_html=True
                        )
                    else:
                        if st.button("English", key="top_bar_en", use_container_width=True):
                            st.session_state["lang"] = "en"
                            st.session_state["lang_radio"] = LANGS["en"]
                            st.rerun()
                with b2:
                    if lang == "kn":
                        st.markdown(
                            "<div style='background:#2E7D32; color:#ffffff; font-size:0.8rem; font-weight:700; padding:5px 4px; border-radius:8px; text-align:center;'>🌾 ಕನ್ನಡ</div>",
                            unsafe_allow_html=True
                        )
                    else:
                        if st.button("ಕನ್ನಡ", key="top_bar_kn", use_container_width=True):
                            st.session_state["lang"] = "kn"
                            st.session_state["lang_radio"] = LANGS["kn"]
                            st.rerun()
            st.markdown("<div style='border-bottom: 1px solid #E0EAE0; margin-bottom: 12px; margin-top: 4px;'></div>", unsafe_allow_html=True)
    except Exception:
        pass

