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
