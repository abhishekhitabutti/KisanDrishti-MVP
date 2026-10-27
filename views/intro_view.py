"""
KrushiNudi Intro & Welcome Interface.
Author: Abhishek Hitabutti
Copyright: © 2026 Abhishek Hitabutti. All rights reserved.

Presented to users upon opening the application before transitioning
to the main multi-tool agricultural dashboard.
Includes:
- 9-Second Cinematic Studio Startup Animation (HTML5 Canvas + Web Audio API)
- Official Video Tour Player (MP4)
- AI Video Generation Blueprint & Ready Prompt
- 4-Core Agricultural Services Preview
- Seamless One-Click Transition into the KrushiNudi Application
"""

from pathlib import Path
import streamlit as st
import streamlit.components.v1 as components

import i18n
from i18n import t

ROOT_DIR = Path(__file__).resolve().parent.parent


def get_cinematic_animation_html(is_kn=False):
    """Generate the self-contained 9-second cinematic startup animation matching the exact storyboard."""
    brand_name = "ಕೃಷಿನುಡಿ AI" if is_kn else "KrushiNudi AI"
    tagline = "ಬುದ್ಧಿವಂತ ಕೃಷಿ. ಉಜ್ವಲ ಭವಿಷ್ಯ." if is_kn else "Intelligent Farming. Smarter Future."
    enter_label = "🌾 ಕೃಷಿನುಡಿ ಅಪ್ಲಿಕೇಶನ್‌ಗೆ ಪ್ರವೇಶಿಸಿ ➡️" if is_kn else "🌾 Enter Application Dashboard ➡️"

    return f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
      * {{ margin: 0; padding: 0; box-sizing: border-box; }}
      body {{
        background: #030804;
        color: #ffffff;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        min-height: 100vh;
        overflow: hidden;
      }}
      .stage-container {{
        position: relative;
        width: 100%;
        max-width: 480px;
        height: 560px;
        background: radial-gradient(circle at 50% 42%, #0C2814 0%, #041006 65%, #000301 100%);
        border-radius: 20px;
        overflow: hidden;
        box-shadow: 0 16px 50px rgba(0, 0, 0, 0.8), 0 0 30px rgba(46, 125, 50, 0.25);
        border: 1px solid rgba(76, 175, 80, 0.25);
        margin: auto;
      }}
      canvas {{
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        z-index: 1;
      }}
      .scene-overlay {{
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        z-index: 2;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        pointer-events: none;
        text-align: center;
        padding: 24px;
      }}
      .logo-wrapper {{
        position: relative;
        width: 110px;
        height: 110px;
        margin-bottom: 20px;
        opacity: 0;
        transform: scale(0.65) translateY(18px);
        transition: opacity 1.8s cubic-bezier(0.16, 1, 0.3, 1), transform 1.8s cubic-bezier(0.16, 1, 0.3, 1);
      }}
      .logo-wrapper.revealed {{
        opacity: 1;
        transform: scale(1) translateY(0);
      }}
      .logo-wrapper.transitioning {{
        transform: scale(1.12);
        filter: drop-shadow(0 0 35px #4CAF50);
      }}
      .logo-glow {{
        position: absolute;
        top: -18px;
        left: -18px;
        right: -18px;
        bottom: -18px;
        background: radial-gradient(circle, rgba(76, 175, 80, 0.5) 0%, rgba(255, 215, 0, 0.18) 32%, transparent 70%);
        border-radius: 50%;
        filter: blur(14px);
        animation: pulseGlow 3s infinite ease-in-out;
      }}
      @keyframes pulseGlow {{
        0%, 100% {{ transform: scale(0.9); opacity: 0.6; }}
        50% {{ transform: scale(1.15); opacity: 0.95; }}
      }}
      .brand-text {{
        opacity: 0;
        transform: translateY(14px);
        transition: opacity 1.3s ease 0.3s, transform 1.3s ease 0.3s;
      }}
      .brand-text.revealed {{
        opacity: 1;
        transform: translateY(0);
      }}
      .brand-title {{
        font-size: 2rem;
        font-weight: 800;
        letter-spacing: -0.4px;
        background: linear-gradient(135deg, #FFFFFF 15%, #A5D6A7 55%, #FFD54F 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-shadow: 0 4px 20px rgba(46, 125, 50, 0.4);
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 6px;
      }}
      .brand-title .ai-tag {{
        font-size: 0.9rem;
        font-weight: 800;
        padding: 2px 7px;
        background: linear-gradient(135deg, #2E7D32, #1B5E20);
        border: 1px solid #81C784;
        border-radius: 6px;
        -webkit-text-fill-color: #FFFFFF;
        color: #FFFFFF;
        box-shadow: 0 2px 8px rgba(76, 175, 80, 0.4);
      }}
      .brand-tagline {{
        font-size: 0.85rem;
        font-weight: 600;
        color: #C8E6C9;
        letter-spacing: 1.1px;
        text-transform: uppercase;
        margin-top: 8px;
        opacity: 0.92;
      }}
      .wave-shimmer {{
        position: absolute;
        top: 0;
        left: -100%;
        width: 60%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.35), rgba(76, 175, 80, 0.5), transparent);
        transform: skewX(-25deg);
        pointer-events: none;
      }}
      .wave-shimmer.active {{
        animation: sweep 1.5s ease-in-out forwards;
      }}
      @keyframes sweep {{
        0% {{ left: -100%; }}
        100% {{ left: 200%; }}
      }}
      .dashboard-preview {{
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: #0B1C0E;
        z-index: 3;
        opacity: 0;
        transform: scale(0.96);
        pointer-events: none;
        transition: opacity 1.1s ease, transform 1.1s ease;
        display: flex;
        flex-direction: column;
        padding: 22px 18px;
        border-radius: 20px;
      }}
      .dashboard-preview.active {{
        opacity: 1;
        transform: scale(1);
        pointer-events: auto;
      }}
      .controls-bar {{
        position: absolute;
        bottom: 14px;
        left: 16px;
        right: 16px;
        z-index: 10;
        display: flex;
        justify-content: space-between;
        align-items: center;
      }}
      .btn-skip, .btn-sound, .btn-replay {{
        background: rgba(255, 255, 255, 0.12);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.2);
        color: #FFFFFF;
        font-size: 0.76rem;
        font-weight: 600;
        padding: 5px 12px;
        border-radius: 18px;
        cursor: pointer;
        transition: all 0.2s ease;
      }}
      .btn-skip:hover, .btn-sound:hover, .btn-replay:hover {{
        background: rgba(76, 175, 80, 0.4);
        border-color: #81C784;
      }}
      .status-badge {{
        font-size: 0.7rem;
        color: #A5D6A7;
        background: rgba(46, 125, 50, 0.35);
        padding: 3px 10px;
        border-radius: 12px;
        border: 1px solid rgba(76, 175, 80, 0.35);
      }}
    </style>
    </head>
    <body>

    <div class="stage-container" id="stage">
      <canvas id="particleCanvas"></canvas>

      <div class="scene-overlay" id="sceneOverlay">
        <div class="logo-wrapper" id="logoWrapper">
          <div class="logo-glow"></div>
          <div class="wave-shimmer" id="shimmer"></div>
          <!-- KrushiNudi Modern Vector Emblem -->
          <svg viewBox="0 0 120 120" width="110" height="110" fill="none" xmlns="http://www.w3.org/2000/svg">
            <defs>
              <linearGradient id="leafGrad" x1="10" y1="10" x2="110" y2="110" gradientUnits="userSpaceOnUse">
                <stop offset="0%" stop-color="#4CAF50"/>
                <stop offset="60%" stop-color="#1B5E20"/>
                <stop offset="100%" stop-color="#0A3311"/>
              </linearGradient>
              <linearGradient id="goldGrad" x1="0" y1="0" x2="120" y2="120" gradientUnits="userSpaceOnUse">
                <stop offset="0%" stop-color="#FFE082"/>
                <stop offset="50%" stop-color="#FFB300"/>
                <stop offset="100%" stop-color="#FF8F00"/>
              </linearGradient>
            </defs>
            <circle cx="60" cy="60" r="54" stroke="url(#leafGrad)" stroke-width="2.5" stroke-dasharray="6 3" opacity="0.8"/>
            <circle cx="60" cy="55" r="26" fill="url(#goldGrad)" opacity="0.95"/>
            <path d="M 30 92 C 30 50, 60 22, 92 24 C 92 65, 65 92, 30 92 Z" fill="url(#leafGrad)" filter="drop-shadow(0 4px 12px rgba(27,94,32,0.6))"/>
            <path d="M 60 55 L 75 40 M 75 40 L 88 40" stroke="#E8F5E9" stroke-width="2.2" stroke-linecap="round"/>
            <circle cx="88" cy="40" r="3.5" fill="#FFE082"/>
            <path d="M 52 70 L 68 70 M 68 70 L 78 80" stroke="#C8E6C9" stroke-width="2" stroke-linecap="round"/>
            <circle cx="78" cy="80" r="3" fill="#81C784"/>
          </svg>
        </div>

        <div class="brand-text" id="brandText">
          <div class="brand-title">
            <span>{brand_name}</span>
          </div>
          <div class="brand-tagline">{tagline}</div>
        </div>
      </div>

      <!-- Scene 4 Dashboard Reveal -->
      <div class="dashboard-preview" id="dashPreview">
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:12px; border-bottom:1px solid #1B5E20; padding-bottom:8px;">
          <div style="font-weight:800; color:#A5D6A7; font-size:1.05rem;">🌾 {brand_name}</div>
          <div style="font-size:0.75rem; background:#1B5E20; color:#C8E6C9; padding:2px 8px; border-radius:10px;">🟢 Live Connected</div>
        </div>
        <div style="background:rgba(46,125,50,0.22); border:1px solid rgba(76,175,80,0.35); border-radius:12px; padding:10px 12px; margin-bottom:10px;">
          <div style="font-size:0.74rem; color:#81C784; font-weight:700;">⛅ HYPERLOCAL WEATHER & SPRAY</div>
          <div style="font-size:1.1rem; font-weight:800; color:#FFF; margin:2px 0;">28°C · Optimal Spray Window</div>
          <div style="font-size:0.72rem; color:#C8E6C9;">Real-time weather guidance across 31 districts</div>
        </div>
        <div style="display:grid; grid-template-columns:1fr 1fr; gap:8px; margin-bottom:12px;">
          <div style="background:#0F2914; border:1px solid #1B5E20; border-radius:10px; padding:9px;">
            <div style="font-size:0.74rem; color:#81C784;">🩺 Crop Doctor</div>
            <div style="font-size:0.86rem; font-weight:700; color:#FFF;">Instant AI Diagnosis</div>
          </div>
          <div style="background:#0F2914; border:1px solid #1B5E20; border-radius:10px; padding:9px;">
            <div style="font-size:0.74rem; color:#81C784;">📈 Mandi Rates</div>
            <div style="font-size:0.86rem; font-weight:700; color:#FFF;">22 Crops Live</div>
          </div>
          <div style="background:#0F2914; border:1px solid #1B5E20; border-radius:10px; padding:9px;">
            <div style="font-size:0.74rem; color:#81C784;">💧 Borewell</div>
            <div style="font-size:0.86rem; font-weight:700; color:#FFF;">GPS Fracture Depth</div>
          </div>
          <div style="background:#0F2914; border:1px solid #1B5E20; border-radius:10px; padding:9px;">
            <div style="font-size:0.74rem; color:#81C784;">🌱 Advisor</div>
            <div style="font-size:0.86rem; font-weight:700; color:#FFF;">99.5% AI Precision</div>
          </div>
        </div>
        <div style="margin-top:auto;">
          <div style="font-size:0.78rem; text-align:center; color:#A5D6A7; margin-bottom:6px;">✨ Transition Complete · Welcome to KrushiNudi</div>
        </div>
      </div>

      <div class="controls-bar">
        <button class="btn-sound" id="btnSound">🔊 Sound</button>
        <div class="status-badge" id="sceneBadge">Scene 1 (0-2s)</div>
        <button class="btn-replay" id="btnReplay">🔄 Replay</button>
      </div>
    </div>

    <script>
    let audioCtx = null;
    let soundEnabled = true;

    function initAudio() {{
      if (!audioCtx) {{
        try {{
          audioCtx = new (window.AudioContext || window.webkitAudioContext)();
        }} catch(e) {{}}
      }}
      if (audioCtx && audioCtx.state === 'suspended') {{
        audioCtx.resume();
      }}
    }}

    function playTone(freq, type, duration, gainVal, delay=0) {{
      if (!soundEnabled) return;
      setTimeout(() => {{
        initAudio();
        if (!audioCtx) return;
        try {{
          const osc = audioCtx.createOscillator();
          const gain = audioCtx.createGain();
          osc.type = type;
          osc.frequency.setValueAtTime(freq, audioCtx.currentTime);
          gain.gain.setValueAtTime(gainVal, audioCtx.currentTime);
          gain.gain.exponentialRampToValueAtTime(0.0001, audioCtx.currentTime + duration);
          osc.connect(gain);
          gain.connect(audioCtx.destination);
          osc.start();
          osc.stop(audioCtx.currentTime + duration);
        }} catch(e) {{}}
      }}, delay);
    }}

    // Particle system
    const canvas = document.getElementById('particleCanvas');
    const ctx = canvas.getContext('2d');
    let w, h;
    function resize() {{
      w = canvas.width = canvas.offsetWidth;
      h = canvas.height = canvas.offsetHeight;
    }}
    window.addEventListener('resize', resize);
    resize();

    const particles = [];
    const PARTICLE_COUNT = 60;
    for (let i = 0; i < PARTICLE_COUNT; i++) {{
      particles.push({{
        x: Math.random() * w,
        y: Math.random() * h,
        vx: (Math.random() - 0.5) * 0.7,
        vy: -0.35 - Math.random() * 0.5,
        radius: Math.random() * 2.2 + 0.8,
        color: Math.random() > 0.35 ? 'rgba(76, 175, 80,' : 'rgba(255, 215, 0,',
        alpha: Math.random() * 0.7 + 0.2,
        targetX: w / 2,
        targetY: h * 0.36,
        converging: false
      }});
    }}

    function renderParticles() {{
      ctx.clearRect(0, 0, w, h);
      for (let p of particles) {{
        if (p.converging) {{
          p.x += (p.targetX - p.x) * 0.04;
          p.y += (p.targetY - p.y) * 0.04;
          p.alpha = Math.max(0.1, p.alpha * 0.98);
        }} else {{
          p.x += p.vx;
          p.y += p.vy;
          if (p.y < -10) {{ p.y = h + 10; p.x = Math.random() * w; }}
          if (p.x < -10) p.x = w + 10;
          if (p.x > w + 10) p.x = -10;
        }}
        ctx.beginPath();
        ctx.arc(p.x, p.y, p.radius, 0, Math.PI * 2);
        ctx.fillStyle = p.color + p.alpha + ')';
        ctx.shadowBlur = 8;
        ctx.shadowColor = '#4CAF50';
        ctx.fill();
        ctx.shadowBlur = 0;
      }}
      requestAnimationFrame(renderParticles);
    }}
    renderParticles();

    const logoWrapper = document.getElementById('logoWrapper');
    const brandText = document.getElementById('brandText');
    const shimmer = document.getElementById('shimmer');
    const dashPreview = document.getElementById('dashPreview');
    const sceneBadge = document.getElementById('sceneBadge');

    let timers = [];
    function clearAllTimers() {{
      timers.forEach(t => clearTimeout(t));
      timers = [];
    }}

    function runAnimation() {{
      clearAllTimers();
      logoWrapper.classList.remove('revealed', 'transitioning');
      brandText.classList.remove('revealed');
      shimmer.classList.remove('active');
      dashPreview.classList.remove('active');
      particles.forEach(p => p.converging = false);

      // Scene 1: 0 - 2s
      sceneBadge.innerText = "Scene 1: Dark Cinematic Opening (0-2s)";
      playTone(55, 'sine', 2.2, 0.35);

      // Scene 2: 2.2s - 5s
      timers.push(setTimeout(() => {{
        sceneBadge.innerText = "Scene 2: KrushiNudi AI Reveal (2-5s)";
        logoWrapper.classList.add('revealed');
        brandText.classList.add('revealed');
        particles.forEach(p => p.converging = true);
        playTone(220, 'triangle', 2.0, 0.22);
        playTone(329.63, 'sine', 2.2, 0.18, 100);
        playTone(440, 'sine', 2.5, 0.22, 200);
        playTone(659.25, 'sine', 2.0, 0.15, 300);
      }}, 2200));

      // Scene 3: 5.2s - 7s
      timers.push(setTimeout(() => {{
        sceneBadge.innerText = "Scene 3: Digital AI Connection (5-7s)";
        shimmer.classList.add('active');
        playTone(880, 'sine', 1.0, 0.14);
        playTone(1318.5, 'triangle', 1.2, 0.12, 120);
      }}, 5200));

      // Scene 4: 7.2s - 9s
      timers.push(setTimeout(() => {{
        sceneBadge.innerText = "Scene 4: Transition into App (7-9s)";
        logoWrapper.classList.add('transitioning');
        playTone(80, 'sine', 1.5, 0.45);
        playTone(40, 'triangle', 2.0, 0.35, 50);
        timers.push(setTimeout(() => {{
          dashPreview.classList.add('active');
          sceneBadge.innerText = "✨ Application Ready";
        }}, 650));
      }}, 7200));
    }}

    document.getElementById('btnReplay').addEventListener('click', runAnimation);
    document.getElementById('btnSound').addEventListener('click', (e) => {{
      soundEnabled = !soundEnabled;
      e.target.innerText = soundEnabled ? "🔊 Sound" : "🔇 Muted";
      if (soundEnabled) initAudio();
    }});

    window.addEventListener('load', () => {{
      setTimeout(runAnimation, 200);
    }});
    </script>
    </body>
    </html>
    """


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
            brand_title = "ಕೃಷಿನುಡಿ AI {KrushiNudi AI}" if is_kn else "KrushiNudi AI"
            brand_sub = "— ಬುದ್ಧಿವಂತ ಕೃಷಿಯ ಧ್ವನಿ · Intelligent Farming. Smarter Future. —" if is_kn else "— Intelligent Farming. Smarter Future. —"
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
                    <div style="font-size: 1.02rem; font-weight: 700; color: #2E7D32; margin-top: 4px;">
                        {brand_sub}
                    </div>
                    <div style="font-size: 0.88rem; color: #455A64; margin-top: 4px; font-weight: 500;">
                        {brand_desc}
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

    st.markdown("<div style='margin-top: 14px;'></div>", unsafe_allow_html=True)

    # 3-Tab Presentation Container (Cinematic Studio Animation, Video Tour, AI Video Prompt)
    tab_anim, tab_video, tab_prompt = st.tabs([
        "🎬 " + ("ಸಿನಿಮ್ಯಾಟಿಕ್ ಸ್ಟಾರ್ಟಪ್ ಅನಿಮೇಷನ್ (9-Sec Live)" if is_kn else "Cinematic Studio Intro (9-Sec Live)"),
        "🎥 " + ("ಪರಿಚಯ ವಿಡಿಯೋ ಪ್ಲೇಯರ್ (MP4 Tour)" if is_kn else "Video Tour Player (MP4 Tour)"),
        "📋 " + ("ಎಐ ವಿಡಿಯೋ ಪ್ರಾಂಪ್ಟ್ (AI Video Blueprint)" if is_kn else "AI Video Generator Blueprint")
    ])

    with tab_anim:
        st.caption(
            "✨ ಗೇಮ್ ಸ್ಟುಡಿಯೋ ಮಾದರಿಯ 9-ಸೆಕೆಂಡ್ ಸಿನಿಮ್ಯಾಟಿಕ್ ಲೋಗೋ ಮತ್ತು ಆ್ಯಪ್ ಪರಿವರ್ತನಾ ಅನಿಮೇಷನ್ (60 FPS + Web Audio ಧ್ವನಿ ಪರಿಣಾಮಗಳು)."
            if is_kn else
            "✨ Iconic game studio-style 9-second startup animation with emerald particle physics, audio synthesizer, and dashboard reveal."
        )
        anim_html = get_cinematic_animation_html(is_kn)
        components.html(anim_html, height=580, scrolling=False)

    with tab_video:
        st.caption(
            "✨ ಎಐ ಬೆಳೆ ವೈದ್ಯ, ಬೋರ್‌ವೆಲ್ ಪಾಯಿಂಟ್, ಹವಾಮಾನ ಮುನ್ಸೂಚನೆ ಹಾಗೂ ಗರಿಷ್ಠ ಬೆಲೆ ಮಾರುಕಟ್ಟೆ ಕೇಂದ್ರಗಳ ಸಂಪೂರ್ಣ ಪರಿಚಯ."
            if is_kn else
            "✨ Complete visual introduction to AI crop diagnosis, groundwater survey, weather alerts and mandi market rates."
        )
        if intro_video.exists():
            st.video(str(intro_video))
        else:
            st.info("Intro video is loading...")

    with tab_prompt:
        st.markdown(
            "### 🎬 " + (
                "Google Gemini Veo / Runway / Sora ವಿಡಿಯೋ ಪ್ರಾಂಪ್ಟ್"
                if is_kn else
                "Production Video Generation Prompt (Gemini Veo / Runway / Sora)"
            )
        )
        st.caption(
            "ಈ ಪ್ರಾಂಪ್ಟ್ ಅನ್ನು Google AI Studio / Gemini Veo / Sora ಗೆ ಕಾಪಿ-ಪೇಸ್ಟ್ ಮಾಡಿ ನೇರವಾಗಿ 9-ಸೆಕೆಂಡಿನ ಹೊಸ ಸಿನಿಮ್ಯಾಟಿಕ್ MP4 ವಿಡಿಯೋ ಜನರೇಟ್ ಮಾಡಬಹುದು:"
            if is_kn else
            "Copy-paste this exact prompt into Google Gemini, Veo, or Sora to generate a new high-definition cinematic MP4 video:"
        )
        video_prompt_text = (
            "Create a premium, cinematic mobile app startup intro animation for KRUSHINUDI AI, an intelligent smart farming and agricultural guidance application.\n\n"
            "CONCEPT: Make it feel like the iconic opening logo animations of professional mobile game studios, where a studio logo appears dramatically before the actual game begins. Create an original identity for KrushiNudi AI; do not copy any existing company logo or animation.\n\n"
            "SCENE 1 — DARK CINEMATIC OPENING (0–2 seconds)\n"
            "Start with a completely dark, elegant background. Tiny emerald-green particles float gently through the air, resembling glowing seeds and digital data. A soft green light emerges from the center with subtle atmospheric sound effects.\n\n"
            "SCENE 2 — LOGO REVEAL (2–5 seconds)\n"
            "A beautiful, premium, minimalist KrushiNudi AI app icon materializes from glowing particles. The icon combines an emerald leaf, rising sun farming element, and intelligent AI circuit details. Use a sophisticated emerald-green and warm-gold accent palette.\n"
            "Reveal the brand name exactly as:\n"
            "“KrushiNudi AI”\n"
            "Below the logo, reveal the tagline:\n"
            "“Intelligent Farming. Smarter Future.”\n\n"
            "SCENE 3 — BRAND SIGNATURE (5–7 seconds)\n"
            "The logo glows softly while a subtle digital wave travels across it, symbolizing the connection between agriculture, technology, and artificial intelligence. Finish with a short, elegant sonic chime.\n\n"
            "SCENE 4 — TRANSITION INTO THE APP (7–9 seconds)\n"
            "The logo gently shrinks toward the center of the screen. Its emerald-green glow expands into a seamless transition, revealing the REAL KrushiNudi AI application smart farming dashboard with crop recommendations, weather information, and borewell water prediction features.\n\n"
            "VISUAL STYLE: Premium technology brand, cinematic, minimal, polished, smooth motion, emerald green, white, subtle gold accents, clean typography, 9:16 vertical mobile composition."
        )
        st.code(video_prompt_text, language="text")

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
