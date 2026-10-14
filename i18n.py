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


UNTRANSLATED_PAGES = {"weather", "schemes", "about"}


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
    """Crop name: in Kannada mode show 'ಭತ್ತ (rice)' so a wrong translation never hides the English name."""
    if current_lang() == "kn":
        kn = _kannada().get(f"crop:{name}")
        if kn:
            return f"{kn} ({name})"
    return name


def language_picker(translated=True):
    lang = current_lang()
    choice = st.radio("Language / ಭಾಷೆ", list(LANGS.values()), index=0 if lang == "en" else 1, horizontal=True, key="lang_radio")
    st.session_state["lang"] = "kn" if choice == LANGS["kn"] else "en"
    if st.session_state["lang"] == "kn":
        st.caption(t(REVIEW_NOTICE))
        if not translated:
            st.info(t(UNTRANSLATED))
    return st.session_state["lang"]
