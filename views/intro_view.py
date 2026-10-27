"""
KrushiNudi Intro & Welcome Interface.
Author: Abhishek Hitabutti
Copyright: © 2026 Abhishek Hitabutti. All rights reserved.

Presented to users upon opening the application before transitioning
to the main multi-tool agricultural dashboard.
"""

from pathlib import Path
import streamlit as st

import i18n
from i18n import t

ROOT_DIR = Path(__file__).resolve().parent.parent


def render_intro_screen():
    """Render the official KrushiNudi welcome and video showcase interface."""
    is_kn = (i18n.current_lang() == "kn")
    logo_file = ROOT_DIR / "images" / "krushinudi_logo.jpg"
    intro_video = ROOT_DIR / "images" / "krushinudi_intro.mp4"

    # Main Brand Header Container
    with st.container():
        col_l, col_r = st.columns([1, 4])
        with col_l:
            if logo_file.exists():
                st.image(str(logo_file), use_container_width=True)
            else:
                st.markdown("<div style='font-size:3.5rem; text-align:center;'>🌾</div>", unsafe_allow_html=True)
        with col_r:
            brand_title = "ಕೃಷಿನುಡಿ {KrushiNudi}" if is_kn else "KrushiNudi"
            brand_sub = "— ಬುದ್ಧಿವಂತ ಕೃಷಿಯ ಧ್ವನಿ · AI Powered Farming Guidance —" if is_kn else "— AI Powered Farming Guidance · Smart Agriculture —"
            brand_desc = (
                "ಕೃಷಿಕರಿಗಾಗಿ, ಕೃಷಿಕರಿಂದ · ಕರ್ನಾಟಕದ ರೈತರ ವಿಶ್ವಾಸಾರ್ಹ ಡಿಜಿಟಲ್ ಕೃಷಿ ಸಂಗಾತಿ"
                if is_kn else
                "For Farmers, By Farmers · Karnataka's Trusted AI Farming Companion"
            )
            st.markdown(
                f"""
                <div style="padding-top: 6px;">
                    <div style="font-size: 2.1rem; font-weight: 800; color: #1B5E20; line-height: 1.2;">
                        {brand_title}
                    </div>
                    <div style="font-size: 1.05rem; font-weight: 700; color: #2E7D32; margin-top: 4px;">
                        {brand_sub}
                    </div>
                    <div style="font-size: 0.9rem; color: #455A64; margin-top: 4px; font-weight: 500;">
                        {brand_desc}
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

    st.markdown("<div style='margin-top: 14px;'></div>", unsafe_allow_html=True)

    # Official Intro Video Showcase Card
    with st.container(border=True):
        st.markdown(
            "### 🎬 " + (
                "ಕೃಷಿನುಡಿ ಅಧಿಕೃತ ಪರಿಚಯ ಮತ್ತು ಬಳಕೆ ವಿಡಿಯೋ {Official Video Tour}"
                if is_kn else
                "KrushiNudi Official Video Tour & Walkthrough"
            )
        )
        if intro_video.exists():
            st.video(str(intro_video))
        else:
            st.info("Intro video is loading...")

        st.caption(
            "✨ ಎಐ ಬೆಳೆ ವೈದ್ಯ, ಬೋರ್‌ವೆಲ್ ಪಾಯಿಂಟ್, ಹವಾಮಾನ ಮುನ್ಸೂಚನೆ ಹಾಗೂ ಗರಿಷ್ಠ ಬೆಲೆ ಮಾರುಕಟ್ಟೆ ಕೇಂದ್ರಗಳ ಸಂಪೂರ್ಣ ಪರಿಚಯ."
            if is_kn else
            "✨ Complete visual introduction to AI crop diagnosis, groundwater survey, weather alerts and mandi market rates."
        )

    # 4 Key Features Highlight Grid
    st.markdown("#### 🌾 " + ("ಕೃಷಿನುಡಿ ಮುಖ್ಯ ಪರಿಕರಗಳ ಕಿರುನೋಟ" if is_kn else "KrushiNudi Core Agricultural Tools"))
    c1, c2 = st.columns(2)
    with c1:
        with st.container(border=True):
            st.markdown(
                "**🩺 " + ("ಬೆಳೆ ವೈದ್ಯ {Crop Doctor}:**" if is_kn else "Crop Doctor:**") +
                (" ಪೀಡಿತ ಗಿಡದ ಫೋಟೋ ತೆಗೆದು ರೋಗ ಪತ್ತೆ ಮಾಡಿ & ಸಾವಯವ ಔಷಧ ಪಡೆಯಿರಿ."
                 if is_kn else
                 " Detect crop diseases via AI photo analysis and get organic remedies.")
            )
        with c1:
            with st.container(border=True):
                st.markdown(
                    "**📈 " + ("ಮಾರುಕಟ್ಟೆ ದರ & ಕೇಂದ್ರಗಳು {Market Rates}:**" if is_kn else "Market Rates & Selling Centers:**") +
                    (" 22 ಬೆಳೆಗಳ ಲೈವ್ ದರ, 30 ದಿನಗಳ ಗ್ರಾಫ್ & ಗರಿಷ್ಠ ಬೆಲೆಗೆ ಖರೀದಿ ಕೇಂದ್ರಗಳು."
                     if is_kn else
                     " Daily APMC prices, 30-day trend graphs & verified highest-price selling hubs.")
                )

    with c2:
        with st.container(border=True):
            st.markdown(
                "**💧 " + ("ಬೋರ್‌ವೆಲ್ ಸಲಹೆ {Borewell Advisory}:**" if is_kn else "Borewell Water Advisory:**") +
                (" ಜಿಪಿಎಸ್ ಆಧಾರಿತ ಅಂತರ್ಜಲ ಶಿಲಾ ಬಿರುಕುಗಳು (Lineaments) & ನಿಖರ ಪಾಯಿಂಟ್‌ಗಳು."
                 if is_kn else
                 " GPS fracture strike depths and high-yield groundwater recharge points.")
            )
        with c2:
            with st.container(border=True):
                st.markdown(
                    "**⛅ " + ("ಹವಾಮಾನ ಮುನ್ನೆಚ್ಚರಿಕೆ {Weather Precautions}:**" if is_kn else "Weather Precautions:**") +
                    (" 7 ದಿನಗಳ ಹವಾಮಾನ ಮುನ್ಸೂಚನೆ & ಕೃಷಿಕರ ಸಿಂಪರಣಾ ಮುನ್ನೆಚ್ಚರಿಕೆಗಳು."
                     if is_kn else
                     " 7-day hyperlocal forecast and farmer spraying advisories.")
                )

    st.markdown("<div style='margin-top: 14px;'></div>", unsafe_allow_html=True)

    # Callback to transition to the application
    def _enter_application():
        st.session_state["intro_seen"] = True
        try:
            st.query_params["intro"] = "done"
        except Exception:
            pass

    # Prominent Call To Action (Enter Application)
    cta_col1, cta_col2 = st.columns([3.2, 1.3], gap="medium")
    with cta_col1:
        st.button(
            "🌾 ಕೃಷಿನುಡಿ ಅಪ್ಲಿಕೇಶನ್‌ಗೆ ಪ್ರವೇಶಿಸಿ {Enter Application} ➡️"
            if is_kn else
            "🌾 Enter KrushiNudi Application ➡️",
            key="btn_enter_app",
            type="primary",
            use_container_width=True,
            on_click=_enter_application,
            help="Click to open the full KrushiNudi agricultural portal"
        )
    with cta_col2:
        st.button(
            "ಮುಂದುವರಿಯಿರಿ ⏭️" if is_kn else "Skip Intro ⏭️",
            key="btn_skip_intro",
            type="secondary",
            use_container_width=True,
            on_click=_enter_application,
            help="Skip directly to the dashboard"
        )

    # Bottom Branding Footer
    st.markdown(
        f"""
        <div style="text-align: center; margin-top: 30px; font-size: 0.82rem; color: #78909C; border-top: 1px solid #ECEFF1; padding-top: 14px;">
            {'🌱 ಸ್ಮಾರ್ಟ್ ಕೃಷಿ &nbsp;|&nbsp; 🛡️ ವಿಶ್ವಾಸಾರ್ಹ ಮಾಹಿತಿ &nbsp;|&nbsp; 👥 ಕೃಷಿಕರಿಗಾಗಿ, ಕೃಷಿಕರಿಂದ' if is_kn else '🌱 Smart Farming &nbsp;|&nbsp; 🛡️ Sourced Intelligence &nbsp;|&nbsp; 👥 For Farmers, By Farmers'}
            <br>
            © 2026 KrushiNudi. All rights reserved. &nbsp;|&nbsp; Developed by Abhishek Hitabutti
        </div>
        """,
        unsafe_allow_html=True
    )
