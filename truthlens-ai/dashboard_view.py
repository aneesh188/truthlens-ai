"""
TruthLens AI - Road to Milky Way Cyber Command Center Dashboard
Inspired by roadtomilkyway.com (Bangalore City Space Station Edition):
Animated Cosmic Threat Map, Rotating Milky Way Portal Shield, Holographic Neural Core,
Live Telemetry Feeds, and Brutalist Hard-Shadow Cards.
Uses render_html to guarantee clean rendering without Markdown indentation artifacts.
"""

import streamlit as st
import plotly.graph_objects as go
from database.db import get_statistics
from ui_common import render_header, load_custom_css, render_sidebar_telemetry, render_html
from datetime import datetime


def render_dashboard():
    """Render the Road to Milky Way cosmic command center dashboard."""
    load_custom_css()
    render_sidebar_telemetry()

    stats = get_statistics()
    total_db = stats["total"]
    suspicious_db = stats["suspicious"]
    real_db = stats["real"]
    text_count = stats["text_count"]
    image_count = stats["image_count"]
    video_count = stats["video_count"]

    # Merged baseline metrics with active SQLite telemetry
    total_display = 24387 + total_db
    suspicious_display = 1934 + suspicious_db
    medium_display = 4917
    low_display = 17538 + real_db

    now_utc = datetime.utcnow().strftime("%H:%M:%S UTC // %b %d, %Y")

    # --- TOP ROAD TO MILKY WAY CAPSULE NAVBAR ---
    render_html(f"""
        <div style="background: #000621; border: 2px solid #ffe3c5; border-radius: 999px; box-shadow: 3px 3px 0px #182276; padding: 0.5rem 1.25rem; margin-bottom: 1.2rem; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 0.6rem;">
            <div style="display: flex; align-items: center; gap: 0.75rem;">
                <div style="background: linear-gradient(135deg, #506cd9, #22d974); width: 34px; height: 34px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 1.15rem; box-shadow: 2px 2px 0px #182276; border: 1.5px solid #ffe3c5;">
                    🌌
                </div>
                <div>
                    <span style="font-weight: 900; font-size: 1.15rem; color: #FFFFFF; letter-spacing: -0.01em;">TRUTHLENS <span style="color: #ffe3c5;">AI</span></span>
                    <span style="font-size: 0.68rem; color: #a9b4e8; margin-left: 0.5rem; letter-spacing: 0.08em; text-transform: uppercase;">Bangalore Node // Milky Way</span>
                </div>
            </div>
            <div style="display: flex; gap: 0.35rem; align-items: center; font-size: 0.75rem; font-weight: 800; letter-spacing: 0.06em;">
                <span style="background: #ffe3c5; color: #000621; padding: 0.25rem 0.85rem; border-radius: 999px; box-shadow: 2px 2px 0px #182276;">DASHBOARD</span>
                <span style="color: #a9b4e8; padding: 0.25rem 0.65rem;">THREATS</span>
                <span style="color: #a9b4e8; padding: 0.25rem 0.65rem;">ENDPOINTS</span>
                <span style="color: #a9b4e8; padding: 0.25rem 0.65rem;">INTELLIGENCE</span>
                <span style="color: #a9b4e8; padding: 0.25rem 0.65rem;">VAULT</span>
            </div>
            <div style="display: flex; align-items: center; gap: 0.8rem; font-family: 'JetBrains Mono', monospace; font-size: 0.75rem; color: #22d974;">
                <span><span class="pulse-dot online"></span> LIVE</span>
                <span style="color: #a9b4e8;">{now_utc}</span>
            </div>
        </div>
    """)

    # --- THREE-COLUMN MASTER GRID ---
    col_left, col_center, col_right = st.columns([1.1, 1.8, 1.1])

    # =========================================================================
    # LEFT COLUMN: THREAT OVERVIEW, ACTIVE THREATS & ACTIVITY FEED
    # =========================================================================
    with col_left:
        # 1. THREAT OVERVIEW
        render_html("""
            <div class="cyber-card">
                <div class="cyber-card-header">
                    <span class="cyber-card-title">Threat Overview</span>
                    <span class="cyber-card-subtitle">Real-time Telemetry</span>
                </div>
        """)

        # Sparkline area chart (Cosmic Ruby red matching Road to Milky Way)
        x_points = list(range(14))
        y_points = [28, 35, 30, 48, 52, 45, 62, 58, 70, 65, 82, 75, 88, 92]
        fig_spark = go.Figure()
        fig_spark.add_trace(go.Scatter(
            x=x_points,
            y=y_points,
            fill='tozeroy',
            mode='lines',
            line=dict(color='#d13f30', width=2.5),
            fillcolor='rgba(209, 63, 48, 0.25)'
        ))
        fig_spark.update_layout(
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            margin=dict(l=0, r=0, t=5, b=5),
            height=65,
            xaxis=dict(showgrid=False, showticklabels=False),
            yaxis=dict(showgrid=False, showticklabels=False)
        )
        st.plotly_chart(fig_spark, use_container_width=True, config={'displayModeBar': False})

        render_html(f"""
                <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 0.35rem; margin-top: 0.4rem; text-align: center; font-family: 'JetBrains Mono', monospace;">
                    <div style="background: #0a1240; border: 1.5px solid #26327f; border-radius: 6px; padding: 0.4rem 0.2rem; box-shadow: 2px 2px 0px #182276;">
                        <div style="font-size: 0.6rem; color: #a9b4e8;">TOTAL</div>
                        <div style="font-size: 0.82rem; font-weight: 800; color: #FFFFFF;">{total_display:,}</div>
                        <div style="font-size: 0.58rem; color: #22d974;">+4.2%</div>
                    </div>
                    <div style="background: #0a1240; border: 1.5px solid #d13f30; border-radius: 6px; padding: 0.4rem 0.2rem; box-shadow: 2px 2px 0px #182276;">
                        <div style="font-size: 0.6rem; color: #a9b4e8;">HIGH</div>
                        <div style="font-size: 0.82rem; font-weight: 800; color: #d13f30;">{suspicious_display:,}</div>
                        <div style="font-size: 0.58rem; color: #d13f30;">-1.5%</div>
                    </div>
                    <div style="background: #0a1240; border: 1.5px solid #ead11f; border-radius: 6px; padding: 0.4rem 0.2rem; box-shadow: 2px 2px 0px #182276;">
                        <div style="font-size: 0.6rem; color: #a9b4e8;">MEDIUM</div>
                        <div style="font-size: 0.82rem; font-weight: 800; color: #ead11f;">{medium_display:,}</div>
                        <div style="font-size: 0.58rem; color: #506cd9;">+2.1%</div>
                    </div>
                    <div style="background: #0a1240; border: 1.5px solid #22d974; border-radius: 6px; padding: 0.4rem 0.2rem; box-shadow: 2px 2px 0px #182276;">
                        <div style="font-size: 0.6rem; color: #a9b4e8;">LOW</div>
                        <div style="font-size: 0.82rem; font-weight: 800; color: #22d974;">{low_display:,}</div>
                        <div style="font-size: 0.58rem; color: #a9b4e8;">-0.7%</div>
                    </div>
                </div>
            </div>
        """)

        # 2. ACTIVE THREATS DONUT
        render_html("""
            <div class="cyber-card">
                <div class="cyber-card-header">
                    <span class="cyber-card-title">Active Threats</span>
                    <span class="cyber-card-subtitle">By Severity</span>
                </div>
        """)

        c_donut1, c_donut2 = st.columns([1.2, 1])
        with c_donut1:
            fig_donut = go.Figure(data=[go.Pie(
                labels=["Critical", "High", "Medium", "Low"],
                values=[428 + suspicious_db, 1934, 4917, 17538 + real_db],
                hole=0.68,
                marker=dict(colors=["#d13f30", "#506cd9", "#ead11f", "#22d974"]),
                textinfo="none",
                hoverinfo="label+value"
            )])
            fig_donut.update_layout(
                paper_bgcolor="rgba(0,0,0,0)",
                plot_bgcolor="rgba(0,0,0,0)",
                margin=dict(l=5, r=5, t=5, b=5),
                height=130,
                showlegend=False,
                annotations=[dict(text=f"<b>{total_display:,}</b><br><span style='font-size:8px;color:#a9b4e8'>THREATS</span>", x=0.5, y=0.5, font_size=11, font_color="#FFFFFF", showarrow=False)]
            )
            st.plotly_chart(fig_donut, use_container_width=True, config={'displayModeBar': False})

        with c_donut2:
            render_html(f"""
                <div style="font-family: 'JetBrains Mono', monospace; font-size: 0.72rem; display: flex; flex-direction: column; justify-content: center; height: 130px; gap: 0.35rem;">
                    <div style="display: flex; justify-content: space-between;"><span style="color: #d13f30;">● Critical</span> <b style="color: #FFFFFF;">428</b></div>
                    <div style="display: flex; justify-content: space-between;"><span style="color: #506cd9;">● High</span> <b style="color: #FFFFFF;">1,934</b></div>
                    <div style="display: flex; justify-content: space-between;"><span style="color: #ead11f;">● Medium</span> <b style="color: #FFFFFF;">4,917</b></div>
                    <div style="display: flex; justify-content: space-between;"><span style="color: #22d974;">● Low</span> <b style="color: #FFFFFF;">17,538</b></div>
                </div>
            """)
        render_html("</div>")

        # 3. THREAT ACTIVITY FEED
        recent_feed = stats["recent"]
        render_html("""
            <div class="cyber-card">
                <div class="cyber-card-header">
                    <span class="cyber-card-title">Threat Activity Feed</span>
                    <span class="cyber-card-subtitle"><span class="pulse-dot online"></span> Live Updates</span>
                </div>
                <div style="display: flex; flex-direction: column; gap: 0.4rem;">
        """)

        feed_items = [
            ("CRITICAL", "Ransomware / Disinfo Campaign", "Subnet: TR-BLR-NODE-01", "14:35:22", "threat"),
            ("HIGH", "Unauthorized Deepfake Ingestion", "Target: user_exec_profile", "14:35:19", "info"),
            ("MED", "Malicious Domain Spoofing", "Origin IP: 185.220.101.5", "14:35:12", "warning"),
            ("CRITICAL", "Synthetic Latent Artifact Flagged", "Hash: SHA256-e7a...8b1", "14:35:05", "threat"),
            ("LOW", "Phishing Narrative Neutralized", "Account: j.doe@corp.io", "14:35:01", "safe"),
        ]

        if recent_feed:
            for r in recent_feed[:2]:
                is_fk = "FAKE" in r["prediction"] or "SYNTHETIC" in r["prediction"]
                b_type = "threat" if is_fk else "safe"
                b_label = "CRITICAL" if is_fk else "VERIFIED"
                feed_items.insert(0, (b_label, r["content_summary"][:24], f"ID: {r['analysis_code']}", r["timestamp"][-8:], b_type))

        for badge, title, desc, t_time, b_style in feed_items[:5]:
            badge_cls = f"badge-{b_style}"
            render_html(f"""
                <div class="feed-row">
                    <div style="display: flex; align-items: center; gap: 0.5rem; overflow: hidden;">
                        <span class="{badge_cls}" style="padding: 0.15rem 0.45rem; font-size: 0.62rem;">{badge}</span>
                        <div style="white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">
                            <div style="color: #F0F4F8; font-weight: 700; font-size: 0.74rem;">{title}</div>
                            <div style="color: #a9b4e8; font-size: 0.65rem;">{desc}</div>
                        </div>
                    </div>
                    <div style="color: #ffe3c5; font-family: 'JetBrains Mono', monospace; font-size: 0.65rem; white-space: nowrap;">
                        {t_time}
                    </div>
                </div>
            """)

        render_html("</div></div>")


    # =========================================================================
    # CENTER COLUMN: GLOBAL THREAT MAP + ROTATING CYBER SHIELD + SYSTEM METRICS
    # =========================================================================
    with col_center:
        render_html("""
            <div class="cyber-map-container">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.5rem; position: relative; z-index: 5;">
                    <div>
                        <span class="cyber-card-title">Cosmic Threat Map</span>
                        <span class="cyber-card-subtitle" style="margin-left: 0.5rem;">Bangalore & Global Nodes</span>
                    </div>
                    <span class="badge-info" style="font-size: 0.68rem;">ROAD TO MILKY WAY</span>
                </div>
        """)

        # SVG Animated World Map with Road to Milky Way cosmic colors
        svg_map_html = """
        <div style="position: relative; width: 100%; height: 310px; overflow: hidden; border-radius: 8px;">
            <svg viewBox="0 0 800 400" width="100%" height="100%" style="background: #000621;" xmlns="http://www.w3.org/2000/svg">
                <defs>
                    <radialGradient id="cyberGlow" cx="50%" cy="50%" r="50%">
                        <stop offset="0%" stop-color="#506cd9" stop-opacity="0.3" />
                        <stop offset="100%" stop-color="#000621" stop-opacity="0" />
                    </radialGradient>
                    <radialGradient id="redPulsar" cx="50%" cy="50%" r="50%">
                        <stop offset="0%" stop-color="#d13f30" stop-opacity="0.8" />
                        <stop offset="100%" stop-color="#d13f30" stop-opacity="0" />
                    </radialGradient>
                </defs>
                <rect width="800" height="400" fill="url(#cyberGlow)"/>
                <g stroke="rgba(38, 50, 127, 0.25)" stroke-width="1">
                    <line x1="0" y1="80" x2="800" y2="80" />
                    <line x1="0" y1="160" x2="800" y2="160" />
                    <line x1="0" y1="240" x2="800" y2="240" />
                    <line x1="0" y1="320" x2="800" y2="320" />
                    <line x1="160" y1="0" x2="160" y2="400" />
                    <line x1="320" y1="0" x2="320" y2="400" />
                    <line x1="480" y1="0" x2="480" y2="400" />
                    <line x1="640" y1="0" x2="640" y2="400" />
                </g>
                <path d="M 140 100 Q 180 90 220 110 T 260 140 T 210 180 T 150 160 Z" fill="rgba(80, 108, 217, 0.20)" stroke="rgba(169, 184, 242, 0.4)" stroke-width="1.2"/>
                <path d="M 230 210 Q 260 220 280 260 T 250 320 T 220 280 Z" fill="rgba(80, 108, 217, 0.18)" stroke="rgba(169, 184, 242, 0.4)" stroke-width="1.2"/>
                <path d="M 380 90 Q 420 85 450 110 T 430 150 T 370 130 Z" fill="rgba(80, 108, 217, 0.20)" stroke="rgba(169, 184, 242, 0.4)" stroke-width="1.2"/>
                <path d="M 380 160 Q 440 165 460 210 T 420 280 T 370 230 Z" fill="rgba(80, 108, 217, 0.18)" stroke="rgba(169, 184, 242, 0.4)" stroke-width="1.2"/>
                <path d="M 470 90 Q 560 80 640 120 T 630 200 T 520 180 T 460 130 Z" fill="rgba(80, 108, 217, 0.20)" stroke="rgba(169, 184, 242, 0.4)" stroke-width="1.2"/>
                <path d="M 620 250 Q 670 250 680 290 T 630 310 Z" fill="rgba(80, 108, 217, 0.18)" stroke="rgba(169, 184, 242, 0.4)" stroke-width="1.2"/>
                <g stroke="#22d974" stroke-width="1.5" fill="none" opacity="0.8">
                    <path d="M 400 200 L 290 170 L 190 130" stroke-dasharray="8,6" style="animation: circuit-dash 2s linear infinite;"/>
                    <path d="M 400 200 L 390 160 L 410 115" stroke-dasharray="8,6" style="animation: circuit-dash 2.4s linear infinite;"/>
                    <path d="M 400 200 L 480 180 L 580 130" stroke-dasharray="8,6" style="animation: circuit-dash 2.2s linear infinite;"/>
                    <path d="M 400 200 L 330 230 L 250 260" stroke-dasharray="8,6" style="animation: circuit-dash 2.8s linear infinite;"/>
                    <path d="M 400 200 L 510 240 L 640 280" stroke-dasharray="8,6" style="animation: circuit-dash 2.5s linear infinite;"/>
                </g>
                <circle cx="190" cy="130" r="14" fill="url(#redPulsar)">
                    <animate attributeName="r" values="6;22;6" dur="2.2s" repeatCount="indefinite"/>
                    <animate attributeName="opacity" values="0.8;0.2;0.8" dur="2.2s" repeatCount="indefinite"/>
                </circle>
                <circle cx="190" cy="130" r="5" fill="#d13f30"/>
                <circle cx="410" cy="115" r="14" fill="url(#redPulsar)">
                    <animate attributeName="r" values="6;20;6" dur="1.8s" repeatCount="indefinite"/>
                    <animate attributeName="opacity" values="0.9;0.3;0.9" dur="1.8s" repeatCount="indefinite"/>
                </circle>
                <circle cx="410" cy="115" r="5" fill="#d13f30"/>
                <circle cx="580" cy="130" r="16" fill="url(#redPulsar)">
                    <animate attributeName="r" values="6;25;6" dur="2.4s" repeatCount="indefinite"/>
                    <animate attributeName="opacity" values="0.8;0.2;0.8" dur="2.4s" repeatCount="indefinite"/>
                </circle>
                <circle cx="580" cy="130" r="5" fill="#d13f30"/>
                <circle cx="250" cy="260" r="12" fill="url(#redPulsar)">
                    <animate attributeName="r" values="5;18;5" dur="2.6s" repeatCount="indefinite"/>
                    <animate attributeName="opacity" values="0.8;0.2;0.8" dur="2.6s" repeatCount="indefinite"/>
                </circle>
                <circle cx="250" cy="260" r="4" fill="#506cd9"/>
                <circle cx="640" cy="280" r="12" fill="url(#redPulsar)">
                    <animate attributeName="r" values="5;18;5" dur="3s" repeatCount="indefinite"/>
                    <animate attributeName="opacity" values="0.8;0.2;0.8" dur="3s" repeatCount="indefinite"/>
                </circle>
                <circle cx="640" cy="280" r="4" fill="#ead11f"/>
            </svg>
            <div class="cyber-shield-wrapper">
                <div class="cyber-shield-outer-ring"></div>
                <div class="cyber-shield-inner-ring"></div>
                <div class="cyber-shield-center">
                    <svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="#ffe3c5" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                        <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/>
                        <rect x="9" y="11" width="6" height="5" rx="1" fill="#ffe3c5"/>
                        <path d="M10 11V9a2 2 0 0 1 4 0v2"/>
                    </svg>
                </div>
            </div>
        </div>
        <div style="text-align: center; margin-top: 0.65rem;">
            <span class="badge-safe" style="font-size: 0.78rem; padding: 0.35rem 1rem; box-shadow: 3px 3px 0px #182276;">
                <span class="pulse-dot online"></span> COSMIC SHIELD // BANGALORE FORENSIC NODE ACTIVE
            </span>
        </div>
        </div>
        """
        render_html(svg_map_html)

        render_html("<div style='height: 0.75rem;'></div>")

        # 3 Bottom Metrics Cards (ENDPOINTS, CLOUD SYSTEMS, NETWORK)
        m_c1, m_c2, m_c3 = st.columns(3)
        with m_c1:
            render_html(f"""
                <div class="stat-card" style="min-height: 85px;">
                    <div style="display: flex; justify-content: space-between; align-items: center;">
                        <span class="stat-label">ENDPOINTS (NLP)</span>
                        <span style="font-size: 1.15rem;">💻</span>
                    </div>
                    <div>
                        <div style="display: flex; justify-content: space-between; align-items: baseline;">
                            <span style="font-size: 0.75rem; color: #22d974;">Protected: <b>7,892</b></span>
                            <span style="font-size: 0.7rem; color: #d13f30;">At Risk: <b>{text_count}</b></span>
                        </div>
                    </div>
                </div>
            """)

        with m_c2:
            render_html(f"""
                <div class="stat-card" style="min-height: 85px;">
                    <div style="display: flex; justify-content: space-between; align-items: center;">
                        <span class="stat-label">CLOUD SYSTEMS (ViT)</span>
                        <span style="font-size: 1.15rem;">☁️</span>
                    </div>
                    <div>
                        <div style="display: flex; justify-content: space-between; align-items: baseline;">
                            <span style="font-size: 0.75rem; color: #22d974;">Protected: <b>1,256</b></span>
                            <span style="font-size: 0.7rem; color: #d13f30;">At Risk: <b>{image_count}</b></span>
                        </div>
                    </div>
                </div>
            """)

        with m_c3:
            render_html(f"""
                <div class="stat-card" style="min-height: 85px;">
                    <div style="display: flex; justify-content: space-between; align-items: center;">
                        <span class="stat-label">NETWORK (VIDEO)</span>
                        <span style="font-size: 1.15rem;">🌌</span>
                    </div>
                    <div>
                        <div style="display: flex; justify-content: space-between; align-items: baseline;">
                            <span style="font-size: 0.75rem; color: #22d974;">Protected: <b>4,325</b></span>
                            <span style="font-size: 0.7rem; color: #d13f30;">At Risk: <b>{video_count}</b></span>
                        </div>
                    </div>
                </div>
            """)

        render_html("<div style='height: 0.6rem;'></div>")

        # Quick action launch panel for inspection
        render_html("""
            <div style="font-size: 0.72rem; font-weight: 800; color: #ffe3c5; letter-spacing: 0.08em; text-transform: uppercase; margin-bottom: 0.4rem;">
                Milky Way Scanner Dispatch
            </div>
        """)
        act1, act2, act3 = st.columns(3)
        with act1:
            if st.button("📝 Analyze Text", key="act_dash_text", use_container_width=True):
                st.switch_page("pages/2_Fake_News.py")
        with act2:
            if st.button("🖼️ Analyze Image", key="act_dash_img", use_container_width=True):
                st.switch_page("pages/3_AI_Image.py")
        with act3:
            if st.button("🎬 Analyze Video", key="act_dash_vid", use_container_width=True):
                st.switch_page("pages/4_Deepfake_Video.py")


    # =========================================================================
    # RIGHT COLUMN: THREAT DETECTION ENGINE, ATTACK VECTORS & COMPLIANCE
    # =========================================================================
    with col_right:
        # 1. THREAT DETECTION ENGINE (AI Forensic Analysis)
        render_html("""
            <div class="cyber-card">
                <div class="cyber-card-header">
                    <span class="cyber-card-title">Threat Detection Engine</span>
                    <span class="cyber-card-subtitle">AI Forensic Analysis</span>
                </div>
        """)

        # Animated Holographic Brain / Neural Network Graphic
        brain_svg_html = """
        <div class="brain-container">
            <div class="brain-laser"></div>
            <svg viewBox="0 0 200 130" width="180" height="110" xmlns="http://www.w3.org/2000/svg">
                <path d="M 60 70 Q 45 40 70 30 Q 90 20 100 35 Q 110 20 130 30 Q 155 40 140 70 Q 150 95 130 105 Q 110 115 100 100 Q 90 115 70 105 Q 50 95 60 70 Z" 
                      fill="rgba(80, 108, 217, 0.16)" stroke="#ffe3c5" stroke-width="1.8" filter="drop-shadow(0 0 6px #506cd9)"/>
                <path d="M 100 35 Q 98 65 100 100" stroke="#506cd9" stroke-width="2" stroke-dasharray="3,3"/>
                <g stroke="rgba(169, 184, 242, 0.45)" stroke-width="1">
                    <line x1="75" y1="45" x2="90" y2="60"/>
                    <line x1="90" y1="60" x2="110" y2="60"/>
                    <line x1="110" y1="60" x2="125" y2="45"/>
                    <line x1="70" y1="75" x2="90" y2="85"/>
                    <line x1="90" y1="85" x2="110" y2="85"/>
                    <line x1="110" y1="85" x2="130" y2="75"/>
                    <line x1="90" y1="60" x2="90" y2="85"/>
                    <line x1="110" y1="60" x2="110" y2="85"/>
                </g>
                <circle cx="75" cy="45" r="3.5" fill="#ffe3c5"><animate attributeName="opacity" values="0.4;1;0.4" dur="1.5s" repeatCount="indefinite"/></circle>
                <circle cx="125" cy="45" r="3.5" fill="#ffe3c5"><animate attributeName="opacity" values="1;0.4;1" dur="1.5s" repeatCount="indefinite"/></circle>
                <circle cx="90" cy="60" r="4" fill="#22d974"><animate attributeName="opacity" values="0.5;1;0.5" dur="2s" repeatCount="indefinite"/></circle>
                <circle cx="110" cy="60" r="4" fill="#22d974"><animate attributeName="opacity" values="1;0.5;1" dur="2s" repeatCount="indefinite"/></circle>
                <circle cx="70" cy="75" r="3.5" fill="#d13f30"><animate attributeName="opacity" values="0.3;1;0.3" dur="1.2s" repeatCount="indefinite"/></circle>
                <circle cx="130" cy="75" r="3.5" fill="#d13f30"><animate attributeName="opacity" values="1;0.3;1" dur="1.2s" repeatCount="indefinite"/></circle>
                <circle cx="100" cy="72" r="5" fill="#506cd9"><animate attributeName="r" values="3;6;3" dur="2s" repeatCount="indefinite"/></circle>
            </svg>
        </div>
        """
        render_html(brain_svg_html)

        render_html("""
            <div style="font-family: 'JetBrains Mono', monospace; font-size: 0.7rem; margin-top: 0.6rem; display: flex; flex-direction: column; gap: 0.35rem;">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <span style="color: #F0F4F8;">Behavior Analysis</span>
                    <span style="color: #22d974;"><span class="pulse-dot online"></span> Scanning...</span>
                </div>
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <span style="color: #F0F4F8;">Anomaly Detection</span>
                    <span style="color: #22d974;"><span class="pulse-dot online"></span> Scanning...</span>
                </div>
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <span style="color: #F0F4F8;">ML Classification</span>
                    <span style="color: #22d974;">✓ Active</span>
                </div>
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <span style="color: #F0F4F8;">Threat Detection</span>
                    <span style="color: #d13f30;"><span class="pulse-dot threat"></span> Scanning...</span>
                </div>
            </div>
            <div style="margin-top: 0.6rem;">
                <div style="display: flex; justify-content: space-between; font-size: 0.68rem; margin-bottom: 0.2rem; font-family: 'JetBrains Mono';">
                    <span style="color: #a9b4e8;">Telemetry Synthesis</span>
                    <span style="color: #ffe3c5; font-weight: 800;">78%</span>
                </div>
                <div class="cyber-progress-track">
                    <div class="cyber-progress-fill" style="width: 78%;"></div>
                </div>
            </div>
            </div>
        """)

        # 2. TOP ATTACK VECTORS
        render_html("""
            <div class="cyber-card">
                <div class="cyber-card-header">
                    <span class="cyber-card-title">Top Attack Vectors</span>
                    <span class="cyber-card-subtitle">By Percentage</span>
                </div>
                <div style="display: flex; flex-direction: column; gap: 0.5rem; font-family: 'JetBrains Mono', monospace; font-size: 0.7rem;">
                    <div>
                        <div style="display: flex; justify-content: space-between; margin-bottom: 0.15rem;">
                            <span style="color: #F0F4F8;">Text Disinformation</span>
                            <span style="color: #d13f30; font-weight: 700;">36.1%</span>
                        </div>
                        <div style="background: #000621; border-radius: 999px; height: 6px; width: 100%; overflow: hidden; border: 1px solid #26327f;">
                            <div style="background: #d13f30; width: 36.1%; height: 100%; border-radius: 999px;"></div>
                        </div>
                    </div>
                    <div>
                        <div style="display: flex; justify-content: space-between; margin-bottom: 0.15rem;">
                            <span style="color: #F0F4F8;">AI Latent Diffusion</span>
                            <span style="color: #506cd9; font-weight: 700;">24.7%</span>
                        </div>
                        <div style="background: #000621; border-radius: 999px; height: 6px; width: 100%; overflow: hidden; border: 1px solid #26327f;">
                            <div style="background: #506cd9; width: 24.7%; height: 100%; border-radius: 999px;"></div>
                        </div>
                    </div>
                    <div>
                        <div style="display: flex; justify-content: space-between; margin-bottom: 0.15rem;">
                            <span style="color: #F0F4F8;">Face-Swap Exploits</span>
                            <span style="color: #f6aac8; font-weight: 700;">17.2%</span>
                        </div>
                        <div style="background: #000621; border-radius: 999px; height: 6px; width: 100%; overflow: hidden; border: 1px solid #26327f;">
                            <div style="background: #f6aac8; width: 17.2%; height: 100%; border-radius: 999px;"></div>
                        </div>
                    </div>
                    <div>
                        <div style="display: flex; justify-content: space-between; margin-bottom: 0.15rem;">
                            <span style="color: #F0F4F8;">Unauthorized Access</span>
                            <span style="color: #ead11f; font-weight: 700;">12.4%</span>
                        </div>
                        <div style="background: #000621; border-radius: 999px; height: 6px; width: 100%; overflow: hidden; border: 1px solid #26327f;">
                            <div style="background: #ead11f; width: 12.4%; height: 100%; border-radius: 999px;"></div>
                        </div>
                    </div>
                    <div>
                        <div style="display: flex; justify-content: space-between; margin-bottom: 0.15rem;">
                            <span style="color: #F0F4F8;">Synthetic Voice / Audio</span>
                            <span style="color: #22d974; font-weight: 700;">7.6%</span>
                        </div>
                        <div style="background: #000621; border-radius: 999px; height: 6px; width: 100%; overflow: hidden; border: 1px solid #26327f;">
                            <div style="background: #22d974; width: 7.6%; height: 100%; border-radius: 999px;"></div>
                        </div>
                    </div>
                </div>
            </div>
        """)

        # 3. COMPLIANCE STATUS
        render_html("""
            <div class="cyber-card">
                <div class="cyber-card-header">
                    <span class="cyber-card-title">Compliance Status</span>
                    <span class="cyber-card-subtitle">Security Standards</span>
                </div>
                <div style="display: flex; justify-content: space-around; align-items: center; margin: 0.5rem 0;">
                    <div class="compliance-badge">
                        <div>ISO</div>
                        <div style="font-size: 0.55rem; color: #ffe3c5;">27001</div>
                    </div>
                    <div class="compliance-badge">
                        <div>SOC 2</div>
                        <div style="font-size: 0.55rem; color: #ffe3c5;">Type II</div>
                    </div>
                    <div class="compliance-badge">
                        <div>GDPR</div>
                        <div style="font-size: 0.55rem; color: #ffe3c5;">Audited</div>
                    </div>
                    <div class="compliance-badge">
                        <div>HIPAA</div>
                        <div style="font-size: 0.55rem; color: #ffe3c5;">Shield</div>
                    </div>
                </div>
        """)

        if st.button("📊 View Compliance Vault", key="btn_view_compliance", use_container_width=True):
            st.switch_page("pages/6_Analysis_History.py")

        render_html("</div>")

    # --- MODALITY DISTRIBUTION ACCORDION ---
    render_html("<div style='height: 0.5rem;'></div>")
    with st.expander("📈 Modality Telemetry & Breakdown Inspector (Stored SQLite Metrics)"):
        b_col1, b_col2 = st.columns(2)
        with b_col1:
            st.markdown(f"**Historical Records Logged:** {total_db}")
            st.markdown(f"• Text Articles Audited: `{text_count}`")
            st.markdown(f"• Synthetic Images Inspected: `{image_count}`")
            st.markdown(f"• Video Frames Tracked: `{video_count}`")

        with b_col2:
            fig_bar = go.Figure(data=[go.Bar(
                x=["Text (Articles)", "Images (Still)", "Videos (Frames)"],
                y=[text_count, image_count, video_count],
                marker=dict(color=["#506cd9", "#f6aac8", "#22d974"]),
                text=[text_count, image_count, video_count],
                textposition="auto"
            )])
            fig_bar.update_layout(
                paper_bgcolor="rgba(0,0,0,0)",
                plot_bgcolor="rgba(0,0,0,0)",
                font=dict(color="#ffe3c5", family="Inter"),
                margin=dict(l=20, r=20, t=10, b=30),
                height=180,
                yaxis=dict(gridcolor="rgba(38, 50, 127, 0.35)"),
                xaxis=dict(showgrid=False, gridcolor="rgba(0,0,0,0)")
            )
            st.plotly_chart(fig_bar, use_container_width=True, config={'displayModeBar': False})
