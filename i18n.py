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


def set_language(target_lang):
    """Switch active language between 'en' and 'kn'.
    Invoked safely via on_click callback before widgets are instantiated.
    """
    st.session_state["lang"] = target_lang
    st.session_state["lang_radio"] = LANGS.get(target_lang, "English")
    try:
        st.query_params["lang"] = target_lang
    except Exception:
        pass


def _on_lang_radio_change():
    choice = st.session_state.get("lang_radio")
    target = "kn" if choice == LANGS["kn"] else "en"
    st.session_state["lang"] = target
    try:
        st.query_params["lang"] = target
    except Exception:
        pass


def current_lang():
    radio = st.session_state.get("lang_radio")
    if radio is not None:
        return "kn" if radio == LANGS["kn"] else "en"
    if "lang" in st.session_state:
        return st.session_state["lang"]
    try:
        qp = st.query_params.get("lang")
        if qp in ("kn", "en"):
            st.session_state["lang"] = qp
            st.session_state["lang_radio"] = LANGS[qp]
            return qp
    except Exception:
        pass
    return "en"


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
        radio_kw = {
            "label": "Language / ಭಾಷೆ",
            "options": list(LANGS.values()),
            "horizontal": True,
            "key": "lang_radio",
            "on_change": _on_lang_radio_change,
            "label_visibility": "collapsed",
        }
        if "lang_radio" not in st.session_state:
            radio_kw["index"] = 0 if lang == "en" else 1

        choice = st.radio(**radio_kw)
        st.session_state["lang"] = "kn" if choice == LANGS["kn"] else "en"
        if st.session_state["lang"] == "kn":
            st.caption(t(REVIEW_NOTICE))
            if not translated:
                st.info(t(UNTRANSLATED))
        st.markdown("---")
    return st.session_state["lang"]


def top_language_bar():
    """Prominent, mobile-friendly language switcher rendered at the top of the main container."""
    lang = current_lang()
    is_kn = (lang == "kn")

    with st.container():
        col_l1, col_l2 = st.columns([1.6, 1.4], gap="small")
        with col_l1:
            brand_sub = "ಬುದ್ಧಿವಂತ ಕೃಷಿಯ ಧ್ವನಿ" if is_kn else "AI Powered Farming Guidance"
            brand_title = "🌾 ಕೃಷಿನುಡಿ" if is_kn else "🌾 KrushiNudi"
            st.markdown(
                f"<div style='padding-top:4px; display:flex; align-items:center; gap:8px;'>"
                f"<div style='font-size:1.15rem; font-weight:800; color:#1B5E20; line-height:1.2;'>"
                f"{brand_title} <span style='font-size:0.75rem; font-weight:600; color:#2E7D32; background:#E8F5E9; padding:2px 8px; border-radius:8px; margin-left:4px;'>{brand_sub}</span>"
                f"</div>"
                f"</div>",
                unsafe_allow_html=True
            )
        with col_l2:
            b1, b2 = st.columns(2, gap="small")
            with b1:
                st.button(
                    "🇬🇧 English" if not is_kn else "English",
                    key="top_bar_en",
                    type="primary" if not is_kn else "secondary",
                    on_click=set_language,
                    args=("en",),
                    use_container_width=True,
                    disabled=(not is_kn),
                    help="Switch to English"
                )
            with b2:
                st.button(
                    "🌾 ಕನ್ನಡ" if is_kn else "ಕನ್ನಡ",
                    key="top_bar_kn",
                    type="primary" if is_kn else "secondary",
                    on_click=set_language,
                    args=("kn",),
                    use_container_width=True,
                    disabled=is_kn,
                    help="ಕನ್ನಡಕ್ಕೆ ಬದಲಾಯಿಸಿ"
                )
        st.markdown("<div style='border-bottom: 2px solid #E8F5E9; margin-bottom: 12px; margin-top: 4px;'></div>", unsafe_allow_html=True)

