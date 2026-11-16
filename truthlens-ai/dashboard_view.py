"""
TruthLens AI - CyberShield AI Real-Time Threat Intelligence Dashboard
Faithfully recreates the Cyber Defense SOC Command Center from the reference system:
- Real-time Threat Overview with red sparkline telemetry
- Active Threats donut gauge breakdown
- Live Threat Activity Feed with severity badges
- Global Threat Map with live animated laser attack arcs and pulsing epicenters
- Central Rotating HUD Shield with padlock and circuit traces: SYSTEM PROTECTED // AI THREAT DETECTION ACTIVE
- Three Endpoint, Cloud and Network telemetry cards
- Threat Detection Engine with animated 3D holographic wireframe brain and laser sweep
- Top Attack Vectors progress bars
- Compliance Status circular dials and audit vault link
- Optional Hyperspace Sensory Dive Portal launchpad
"""

import streamlit as st
import plotly.graph_objects as go
from database.db import get_statistics
from ui_common import render_header, load_custom_css, render_sidebar_telemetry, render_html
from datetime import datetime


def render_dashboard():
    """Render the CyberShield AI real-time threat intelligence command center."""
    load_custom_css()
    render_sidebar_telemetry()

    stats = get_statistics()
    total_db = stats["total"]
    suspicious_db = stats["suspicious"]
    real_db = stats["real"]
    text_count = stats["text_count"]
    image_count = stats["image_count"]
    video_count = stats["video_count"]

    # Telemetry baseline numbers merged with SQLite database counts
    total_display = 24387 + total_db
    suspicious_display = 1934 + suspicious_db
    medium_display = 4317
    low_display = 17538 + real_db

    now_utc = datetime.utcnow().strftime("%H:%M:%S UTC // %b %d, %Y")

    # --- TOP CYBERSHIELD AI HEADER & NAVBAR ---
    render_html(f"""
        <div style="background: rgba(6, 21, 43, 0.92); border: 1px solid rgba(22, 139, 255, 0.35); border-radius: 8px; padding: 0.6rem 1.25rem; margin-bottom: 1.1rem; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 0.6rem; box-shadow: 0 4px 20px rgba(0, 0, 0, 0.5);">
            <div style="display: flex; align-items: center; gap: 0.75rem;">
                <div style="background: linear-gradient(135deg, #168BFF, #00E5FF); width: 34px; height: 34px; border-radius: 8px; display: flex; align-items: center; justify-content: center; font-size: 1.15rem; box-shadow: 0 0 12px rgba(22, 139, 255, 0.5); border: 1.5px solid #38D9FF;">
                    🛡️
                </div>
                <div>
                    <span style="font-weight: 800; font-size: 1.1rem; color: #FFFFFF; letter-spacing: -0.01em;">CyberShield <span style="color: #38D9FF;">AI</span></span>
                    <span style="font-size: 0.68rem; color: #8FA2C1; margin-left: 0.5rem; letter-spacing: 0.05em; text-transform: uppercase;">Real-time Threat Intelligence</span>
                </div>
            </div>
            <div style="display: flex; gap: 0.4rem; align-items: center; font-size: 0.75rem; font-weight: 700; letter-spacing: 0.06em;">
                <span style="background: #168BFF; color: #FFFFFF; padding: 0.25rem 0.65rem; border-radius: 4px; box-shadow: 0 0 10px rgba(22, 139, 255, 0.6);">DASHBOARD</span>
                <span style="color: #8BA2C1; padding: 0.25rem 0.5rem;">THREATS</span>
                <span style="color: #8BA2C1; padding: 0.25rem 0.5rem;">ENDPOINTS</span>
                <span style="color: #8BA2C1; padding: 0.25rem 0.5rem;">CLOUD</span>
                <span style="color: #8BA2C1; padding: 0.25rem 0.5rem;">NETWORK</span>
                <span style="color: #8BA2C1; padding: 0.25rem 0.5rem;">INTELLIGENCE</span>
                <span style="color: #8BA2C1; padding: 0.25rem 0.5rem;">REPORTS</span>
                <span style="color: #8BA2C1; padding: 0.25rem 0.5rem;">SETTINGS</span>
            </div>
            <div style="display: flex; align-items: center; gap: 0.8rem; font-family: 'JetBrains Mono', monospace; font-size: 0.75rem; color: #38D9FF;">
                <span><span class="pulse-dot online"></span> LIVE</span>
                <span style="color: #8BA2C1;">{now_utc}</span>
            </div>
        </div>
    """)

    # --- SENSORY DIVE / HYPERSPACE EXPERIENCE ACCORDION ---
    with st.expander("🌌 Launch Hyperspace Sensory Dive // 3D Interactive Media Intelligence Experience"):
        import streamlit.components.v1 as components
        from warp_portal import get_trace_experience_html
        components.html(get_trace_experience_html(), height=660)

    # --- THREE-COLUMN MASTER SOC GRID ---
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
                    <span class="cyber-card-subtitle">Real-time Attack Submissions</span>
                </div>
        """)

        # Sparkline area chart (Crimson threat red with gradient fill)
        x_points = list(range(14))
        y_points = [28, 35, 30, 48, 52, 45, 62, 58, 70, 65, 82, 75, 88, 92]
        fig_spark = go.Figure()
        fig_spark.add_trace(go.Scatter(
            x=x_points,
            y=y_points,
            fill='tozeroy',
            mode='lines',
            line=dict(color='#FF3B5C', width=2),
            fillcolor='rgba(255, 59, 92, 0.25)'
        ))
        fig_spark.update_layout(
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            margin=dict(l=0, r=0, t=5, b=5),
            height=65,
            xaxis=dict(showgrid=False, showticklabels=False, zeroline=False),
            yaxis=dict(showgrid=False, showticklabels=False, zeroline=False)
        )
        st.plotly_chart(fig_spark, use_container_width=True, config={'displayModeBar': False})

        render_html(f"""
                <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 0.35rem; margin-top: 0.4rem; text-align: center; font-family: 'JetBrains Mono', monospace;">
                    <div style="background: rgba(6, 21, 43, 0.7); border: 1px solid rgba(22, 139, 255, 0.3); border-radius: 4px; padding: 0.4rem 0.2rem;">
                        <div style="font-size: 0.6rem; color: #8FA2C1;">TOTAL</div>
                        <div style="font-size: 0.82rem; font-weight: 700; color: #FFFFFF;">{total_display:,}</div>
                        <div style="font-size: 0.58rem; color: #10E79D;">▲ +12.4%</div>
                    </div>
                    <div style="background: rgba(6, 21, 43, 0.7); border: 1px solid rgba(255, 122, 0, 0.35); border-radius: 4px; padding: 0.4rem 0.2rem;">
                        <div style="font-size: 0.6rem; color: #8FA2C1;">HIGH</div>
                        <div style="font-size: 0.82rem; font-weight: 700; color: #FF7A00;">{suspicious_display:,}</div>
                        <div style="font-size: 0.58rem; color: #FF7A00;">▲ +5.8%</div>
                    </div>
                    <div style="background: rgba(6, 21, 43, 0.7); border: 1px solid rgba(56, 217, 255, 0.35); border-radius: 4px; padding: 0.4rem 0.2rem;">
                        <div style="font-size: 0.6rem; color: #8FA2C1;">MEDIUM</div>
                        <div style="font-size: 0.82rem; font-weight: 700; color: #38D9FF;">{medium_display:,}</div>
                        <div style="font-size: 0.58rem; color: #38D9FF;">▼ -2.1%</div>
                    </div>
                    <div style="background: rgba(6, 21, 43, 0.7); border: 1px solid rgba(16, 231, 157, 0.35); border-radius: 4px; padding: 0.4rem 0.2rem;">
                        <div style="font-size: 0.6rem; color: #8FA2C1;">LOW</div>
                        <div style="font-size: 0.82rem; font-weight: 700; color: #10E79D;">{low_display:,}</div>
                        <div style="font-size: 0.58rem; color: #10E79D;">▲ +8.7%</div>
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
                values=[428 + suspicious_db, 1934, 4317, 17538 + real_db],
                hole=0.68,
                marker=dict(colors=["#FF3B5C", "#FF7A00", "#FFB300", "#10E79D"]),
                textinfo="none",
                hoverinfo="label+value"
            )])
            fig_donut.update_layout(
                paper_bgcolor="rgba(0,0,0,0)",
                plot_bgcolor="rgba(0,0,0,0)",
                margin=dict(l=5, r=5, t=5, b=5),
                height=130,
                showlegend=False,
                annotations=[dict(text=f"<b>{total_display:,}</b><br><span style='font-size:8px;color:#8FA2C1'>TOTAL</span>", x=0.5, y=0.5, font_size=11, font_color="#FFFFFF", showarrow=False)]
            )
            st.plotly_chart(fig_donut, use_container_width=True, config={'displayModeBar': False})

        with c_donut2:
            render_html(f"""
                <div style="font-family: 'JetBrains Mono', monospace; font-size: 0.72rem; display: flex; flex-direction: column; justify-content: center; height: 130px; gap: 0.35rem;">
                    <div style="display: flex; justify-content: space-between;"><span style="color: #FF3B5C;">● Critical</span> <b style="color: #FFFFFF;">428</b></div>
                    <div style="display: flex; justify-content: space-between;"><span style="color: #FF7A00;">● High</span> <b style="color: #FFFFFF;">1,934</b></div>
                    <div style="display: flex; justify-content: space-between;"><span style="color: #FFB300;">● Medium</span> <b style="color: #FFFFFF;">4,317</b></div>
                    <div style="display: flex; justify-content: space-between;"><span style="color: #10E79D;">● Low</span> <b style="color: #FFFFFF;">17,608</b></div>
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
                <div style="display: flex; flex-direction: column; gap: 0.35rem;">
        """)

        feed_items = [
            ("CRITICAL", "Ransomware Detected", "Endpoint: FIN-LAPT01-02", "14:35:22", "threat"),
            ("HIGH", "Unauthorized Access Attempt", "User: admin@corpnet.local", "14:35:10", "warning"),
            ("HIGH", "Malicious IP Connection Blocked", "Source IP: 185.220.101.5", "14:34:55", "warning"),
            ("MEDIUM", "Suspicious File Behavior", "File: invoice_january.exe", "14:34:30", "warning"),
            ("LOW", "Phishing Email Quarantined", "User: j.doe@corporate.com", "14:33:40", "safe"),
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
                        <span class="{badge_cls}" style="padding: 0.12rem 0.45rem; font-size: 0.62rem;">{badge}</span>
                        <div style="white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">
                            <div style="color: #F0F4F8; font-weight: 600; font-size: 0.73rem;">{title}</div>
                            <div style="color: #8FA2C1; font-size: 0.65rem;">{desc}</div>
                        </div>
                    </div>
                    <div style="color: #38D9FF; font-family: 'JetBrains Mono', monospace; font-size: 0.65rem; white-space: nowrap;">
                        {t_time}
                    </div>
                </div>
            """)

        render_html("</div></div>")

    # =========================================================================
    # CENTER COLUMN: GLOBAL THREAT MAP + ROTATING CYBER SHIELD + SYSTEM METRICS
    # =========================================================================
    with col_center:
        # Full interactive HTML5 canvas with dot matrix world map, live moving attack laser beams,
        # pulsing threat hotspots, and rotating dual concentric HUD rings with glowing shield.
        map_canvas_html = """
        <div style="background: rgba(6, 21, 43, 0.85); border: 1px solid rgba(22, 139, 255, 0.3); border-radius: 8px; padding: 0.8rem; position: relative; overflow: hidden; box-shadow: 0 8px 30px rgba(0, 0, 0, 0.5);">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.4rem; position: relative; z-index: 10;">
                <div>
                    <span style="font-size: 0.82rem; font-weight: 700; color: #FFFFFF; text-transform: uppercase; letter-spacing: 0.06em;">GLOBAL THREAT MAP</span>
                    <span style="font-size: 0.68rem; color: #8FA2C1; margin-left: 0.5rem; font-family: monospace;">Real-time Attack Visualizer</span>
                </div>
                <span style="background: rgba(22, 139, 255, 0.15); border: 1px solid rgba(22, 139, 255, 0.35); color: #38D9FF; font-size: 0.65rem; padding: 0.15rem 0.55rem; border-radius: 4px; font-family: monospace;">All Threats ▾</span>
            </div>

            <div style="position: relative; width: 100%; height: 320px; overflow: hidden; border-radius: 6px;">
                <canvas id="threatMapCanvas" width="800" height="400" style="width: 100%; height: 100%; background: #020B1A; display: block;"></canvas>
                
                <!-- Center Shield HUD -->
                <div style="position: absolute; left: 50%; top: 52%; transform: translate(-50%, -50%); width: 140px; height: 140px; pointer-events: none; display: flex; align-items: center; justify-content: center; z-index: 5;">
                    <!-- Outer rotating HUD ring -->
                    <div style="position: absolute; width: 130px; height: 130px; border: 2px dashed rgba(56, 217, 255, 0.6); border-radius: 50%; animation: ring-rotate-cw 16s linear infinite;"></div>
                    <!-- Inner counter-rotating ring -->
                    <div style="position: absolute; width: 105px; height: 105px; border: 1.5px dashed rgba(22, 139, 255, 0.7); border-radius: 50%; animation: ring-rotate-ccw 11s linear infinite;"></div>
                    <!-- Center shield badge -->
                    <div style="width: 78px; height: 78px; border-radius: 50%; background: radial-gradient(circle, #168BFF 0%, #061F42 70%, #020B1A 100%); border: 2px solid #38D9FF; display: flex; align-items: center; justify-content: center; box-shadow: 0 0 25px rgba(22, 139, 255, 0.7); animation: shield-glow-pulse 3s infinite ease-in-out;">
                        <svg width="36" height="36" viewBox="0 0 24 24" fill="none" stroke="#FFFFFF" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                            <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/>
                            <rect x="9" y="11" width="6" height="5" rx="1" fill="#FFFFFF"/>
                            <path d="M10 11V9a2 2 0 0 1 4 0v2"/>
                        </svg>
                    </div>
                </div>

                <!-- Shield Status Tag Below -->
                <div style="position: absolute; bottom: 8px; left: 50%; transform: translateX(-50%); z-index: 6; text-align: center; width: 100%;">
                    <div style="display: inline-block; background: rgba(2, 11, 26, 0.85); border: 1px solid rgba(16, 231, 157, 0.5); border-radius: 4px; padding: 0.2rem 0.8rem; box-shadow: 0 0 12px rgba(16, 231, 157, 0.3);">
                        <span style="color: #10E79D; font-size: 0.7rem; font-weight: 700; letter-spacing: 0.05em; font-family: 'JetBrains Mono', monospace;">
                            <span class="pulse-dot online" style="margin-right: 4px;"></span> SYSTEM PROTECTED // AI THREAT DETECTION ACTIVE
                        </span>
                    </div>
                </div>
            </div>

            <script>
            (function() {
                const canvas = document.getElementById('threatMapCanvas');
                if (!canvas) return;
                const ctx = canvas.getContext('2d');
                const W = canvas.width;
                const H = canvas.height;

                // World map simplified landmass dot matrix
                const dots = [];
                // Generate high-tech cyber dot grid across continents
                const landRegions = [
                    // North America
                    { xMin: 100, xMax: 260, yMin: 70, yMax: 180, prob: 0.72 },
                    // South America
                    { xMin: 220, xMax: 300, yMin: 210, yMax: 340, prob: 0.65 },
                    // Europe
                    { xMin: 360, xMax: 470, yMin: 80, yMax: 160, prob: 0.80 },
                    // Africa
                    { xMin: 370, xMax: 480, yMin: 170, yMax: 310, prob: 0.68 },
                    // Asia
                    { xMin: 480, xMax: 700, yMin: 80, yMax: 220, prob: 0.78 },
                    // Australia
                    { xMin: 620, xMax: 720, yMin: 250, yMax: 330, prob: 0.65 }
                ];

                for (let x = 30; x < W - 30; x += 12) {
                    for (let y = 30; y < H - 30; y += 12) {
                        let isLand = false;
                        for (let r of landRegions) {
                            if (x >= r.xMin && x <= r.xMax && y >= r.yMin && y <= r.yMax) {
                                if (Math.random() < r.prob) isLand = true;
                                break;
                            }
                        }
                        if (isLand) {
                            dots.push({ x, y, alpha: 0.25 + Math.random() * 0.35 });
                        }
                    }
                }

                // Attack nodes (cities / epicenters)
                const attackNodes = [
                    { x: 180, y: 120, name: "US-EAST", color: "#FF3B5C" },
                    { x: 120, y: 130, name: "US-WEST", color: "#FF7A00" },
                    { x: 260, y: 270, name: "BR-SAO", color: "#FF3B5C" },
                    { x: 410, y: 110, name: "EU-LON", color: "#FF3B5C" },
                    { x: 440, y: 130, name: "EU-FRA", color: "#FF7A00" },
                    { x: 570, y: 170, name: "IN-HYD", color: "#38D9FF" },
                    { x: 630, y: 130, name: "CN-BEI", color: "#FF3B5C" },
                    { x: 670, y: 150, name: "JP-TYO", color: "#38D9FF" },
                    { x: 670, y: 290, name: "AU-SYD", color: "#FF7A00" }
                ];

                // Animated attack projectile beams
                const beams = [
                    { from: 0, to: 3, progress: 0.1, speed: 0.007 },
                    { from: 6, to: 0, progress: 0.5, speed: 0.006 },
                    { from: 3, to: 5, progress: 0.7, speed: 0.008 },
                    { from: 2, to: 0, progress: 0.3, speed: 0.005 },
                    { from: 6, to: 8, progress: 0.8, speed: 0.007 },
                    { from: 4, to: 7, progress: 0.2, speed: 0.009 }
                ];

                let frame = 0;

                function animate() {
                    frame++;
                    ctx.clearRect(0, 0, W, H);

                    // 1. Draw subtle background coordinate grid
                    ctx.strokeStyle = "rgba(22, 139, 255, 0.08)";
                    ctx.lineWidth = 1;
                    for (let x = 0; x < W; x += 40) {
                        ctx.beginPath();
                        ctx.moveTo(x, 0);
                        ctx.lineTo(x, H);
                        ctx.stroke();
                    }
                    for (let y = 0; y < H; y += 40) {
                        ctx.beginPath();
                        ctx.moveTo(0, y);
                        ctx.lineTo(W, y);
                        ctx.stroke();
                    }

                    // 2. Draw landmass dot matrix
                    for (let d of dots) {
                        ctx.beginPath();
                        ctx.arc(d.x, d.y, 1.8, 0, Math.PI * 2);
                        ctx.fillStyle = `rgba(56, 217, 255, ${d.alpha * 0.5})`;
                        ctx.fill();
                    }

                    // 3. Draw circuit trace paths to the central shield (W/2, H*0.52)
                    const cx = W / 2;
                    const cy = H * 0.52;
                    ctx.strokeStyle = "rgba(56, 217, 255, 0.25)";
                    ctx.lineWidth = 1.2;
                    for (let n of attackNodes) {
                        ctx.beginPath();
                        ctx.moveTo(cx, cy);
                        ctx.lineTo((cx + n.x) / 2, cy);
                        ctx.lineTo(n.x, n.y);
                        ctx.stroke();
                    }

                    // 4. Draw moving attack projectile arcs
                    for (let b of beams) {
                        b.progress += b.speed;
                        if (b.progress > 1) b.progress = 0;

                        const src = attackNodes[b.from];
                        const dst = attackNodes[b.to];

                        // Draw curved Bézier arc
                        const mx = (src.x + dst.x) / 2;
                        const my = Math.min(src.y, dst.y) - 35;

                        ctx.beginPath();
                        ctx.moveTo(src.x, src.y);
                        ctx.quadraticCurveTo(mx, my, dst.x, dst.y);
                        ctx.strokeStyle = "rgba(255, 59, 92, 0.25)";
                        ctx.setLineDash([4, 4]);
                        ctx.stroke();
                        ctx.setLineDash([]);

                        // Calculate projectile position at t = b.progress
                        const t = b.progress;
                        const px = (1 - t) * (1 - t) * src.x + 2 * (1 - t) * t * mx + t * t * dst.x;
                        const py = (1 - t) * (1 - t) * src.y + 2 * (1 - t) * t * my + t * t * dst.y;

                        // Draw glowing missile head
                        ctx.beginPath();
                        ctx.arc(px, py, 3.5, 0, Math.PI * 2);
                        ctx.fillStyle = "#FF3B5C";
                        ctx.shadowColor = "#FF3B5C";
                        ctx.shadowBlur = 10;
                        ctx.fill();
                        ctx.shadowBlur = 0;
                    }

                    // 5. Draw attack nodes with pulsing shockwave rings
                    for (let i = 0; i < attackNodes.length; i++) {
                        const n = attackNodes[i];
                        const pulsePhase = (frame * 0.05 + i) % (Math.PI * 2);
                        const radius = 4 + Math.sin(pulsePhase) * 1.5;
                        const waveR = 6 + ((frame * 0.8 + i * 15) % 25);
                        const waveAlpha = Math.max(0, 1 - waveR / 25);

                        // Ripple wave
                        ctx.beginPath();
                        ctx.arc(n.x, n.y, waveR, 0, Math.PI * 2);
                        ctx.strokeStyle = `rgba(255, 59, 92, ${waveAlpha * 0.6})`;
                        ctx.lineWidth = 1.2;
                        ctx.stroke();

                        // Core epicenter dot
                        ctx.beginPath();
                        ctx.arc(n.x, n.y, radius, 0, Math.PI * 2);
                        ctx.fillStyle = n.color;
                        ctx.shadowColor = n.color;
                        ctx.shadowBlur = 12;
                        ctx.fill();
                        ctx.shadowBlur = 0;
                    }

                    requestAnimationFrame(animate);
                }

                animate();
            })();
            </script>
        </div>
        """
        render_html(map_canvas_html)

        render_html("<div style='height: 0.65rem;'></div>")

        # 3 Bottom Metrics Cards (ENDPOINTS, CLOUD SYSTEMS, NETWORK)
        m_c1, m_c2, m_c3 = st.columns(3)
        with m_c1:
            render_html(f"""
                <div class="stat-card">
                    <div style="display: flex; justify-content: space-between; align-items: center;">
                        <span class="stat-label">ENDPOINTS</span>
                        <span style="font-size: 1.15rem; color: #38D9FF;">💻</span>
                    </div>
                    <div style="margin-top: 0.35rem;">
                        <div style="display: flex; justify-content: space-between; align-items: baseline;">
                            <span style="font-size: 0.74rem; color: #10E79D;">Protected: <b>7,892</b></span>
                            <span style="font-size: 0.7rem; color: #FF3B5C;">At Risk: <b>{23 + text_count}</b></span>
                        </div>
                    </div>
                    <div style="height: 3px; background: rgba(16, 231, 157, 0.2); border-radius: 2px; margin-top: 0.4rem; overflow: hidden;">
                        <div style="width: 96%; height: 100%; background: #10E79D;"></div>
                    </div>
                </div>
            """)

        with m_c2:
            render_html(f"""
                <div class="stat-card">
                    <div style="display: flex; justify-content: space-between; align-items: center;">
                        <span class="stat-label">CLOUD SYSTEMS</span>
                        <span style="font-size: 1.15rem; color: #38D9FF;">☁️</span>
                    </div>
                    <div style="margin-top: 0.35rem;">
                        <div style="display: flex; justify-content: space-between; align-items: baseline;">
                            <span style="font-size: 0.74rem; color: #10E79D;">Protected: <b>1,256</b></span>
                            <span style="font-size: 0.7rem; color: #FF3B5C;">At Risk: <b>{9 + image_count}</b></span>
                        </div>
                    </div>
                    <div style="height: 3px; background: rgba(16, 231, 157, 0.2); border-radius: 2px; margin-top: 0.4rem; overflow: hidden;">
                        <div style="width: 98%; height: 100%; background: #10E79D;"></div>
                    </div>
                </div>
            """)

        with m_c3:
            render_html(f"""
                <div class="stat-card">
                    <div style="display: flex; justify-content: space-between; align-items: center;">
                        <span class="stat-label">NETWORK</span>
                        <span style="font-size: 1.15rem; color: #38D9FF;">🌐</span>
                    </div>
                    <div style="margin-top: 0.35rem;">
                        <div style="display: flex; justify-content: space-between; align-items: baseline;">
                            <span style="font-size: 0.74rem; color: #10E79D;">Protected: <b>4,325</b></span>
                            <span style="font-size: 0.7rem; color: #FF3B5C;">At Risk: <b>{17 + video_count}</b></span>
                        </div>
                    </div>
                    <div style="height: 3px; background: rgba(16, 231, 157, 0.2); border-radius: 2px; margin-top: 0.4rem; overflow: hidden;">
                        <div style="width: 94%; height: 100%; background: #10E79D;"></div>
                    </div>
                </div>
            """)

        render_html("<div style='height: 0.6rem;'></div>")

        # Quick Forensic Scanner Actions
        render_html("""
            <div style="font-size: 0.72rem; font-weight: 700; color: #8FA2C1; letter-spacing: 0.08em; text-transform: uppercase; margin-bottom: 0.4rem;">
                Forensic Scanner Dispatch
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
        # 1. THREAT DETECTION ENGINE (AI Neural Analysis)
        render_html("""
            <div class="cyber-card">
                <div class="cyber-card-header">
                    <span class="cyber-card-title">Threat Detection Engine</span>
                    <span class="cyber-card-subtitle">AI Neural Analysis</span>
                </div>
        """)

        # Animated Holographic 3D Brain with Laser Scanner Sweep
        brain_canvas_html = """
        <div style="position: relative; width: 100%; height: 130px; background: #020B1A; border: 1px solid rgba(22, 139, 255, 0.3); border-radius: 6px; overflow: hidden;">
            <canvas id="brainCanvas" width="300" height="130" style="width: 100%; height: 100%; display: block;"></canvas>
            <!-- Animated horizontal laser scanning bar -->
            <div style="position: absolute; left: 0; width: 100%; height: 2px; background: linear-gradient(90deg, transparent, #00E5FF, #168BFF, transparent); box-shadow: 0 0 10px #00E5FF; animation: scan-laser 3s infinite ease-in-out; pointer-events: none;"></div>
        </div>

        <script>
        (function() {
            const canvas = document.getElementById('brainCanvas');
            if (!canvas) return;
            const ctx = canvas.getContext('2d');
            const W = canvas.width;
            const H = canvas.height;

            // Wireframe nodes representing neural lobes
            const nodes = [
                { x: 110, y: 35, z: 0 }, { x: 150, y: 25, z: 20 }, { x: 190, y: 35, z: 0 },
                { x: 90, y: 65, z: -10 }, { x: 130, y: 55, z: 30 }, { x: 170, y: 55, z: 30 }, { x: 210, y: 65, z: -10 },
                { x: 110, y: 95, z: 10 }, { x: 150, y: 85, z: 40 }, { x: 190, y: 95, z: 10 },
                { x: 150, y: 115, z: 0 }
            ];

            const edges = [
                [0, 1], [1, 2], [0, 3], [1, 4], [1, 5], [2, 6],
                [3, 4], [4, 5], [5, 6], [3, 7], [4, 8], [5, 8], [6, 9],
                [7, 8], [8, 9], [7, 10], [8, 10], [9, 10]
            ];

            let angle = 0;

            function drawBrain() {
                angle += 0.015;
                ctx.clearRect(0, 0, W, H);

                // Draw background grid lines
                ctx.strokeStyle = "rgba(22, 139, 255, 0.06)";
                ctx.lineWidth = 1;
                for (let x = 0; x < W; x += 20) {
                    ctx.beginPath();
                    ctx.moveTo(x, 0);
                    ctx.lineTo(x, H);
                    ctx.stroke();
                }

                // Project and rotate nodes
                const projected = nodes.map(n => {
                    const cosA = Math.cos(angle);
                    const sinA = Math.sin(angle);
                    const rotX = (n.x - 150) * cosA - n.z * sinA + 150;
                    const rotZ = (n.x - 150) * sinA + n.z * cosA;
                    const scale = 200 / (200 + rotZ);
                    return {
                        x: (rotX - 150) * scale + 150,
                        y: (n.y - 65) * scale + 65,
                        alpha: (rotZ + 50) / 100
                    };
                });

                // Draw wireframe edges
                ctx.strokeStyle = "rgba(56, 217, 255, 0.4)";
                ctx.lineWidth = 1.2;
                for (let e of edges) {
                    const p1 = projected[e[0]];
                    const p2 = projected[e[1]];
                    ctx.beginPath();
                    ctx.moveTo(p1.x, p1.y);
                    ctx.lineTo(p2.x, p2.y);
                    ctx.stroke();
                }

                // Draw nodes with glowing points
                for (let p of projected) {
                    ctx.beginPath();
                    ctx.arc(p.x, p.y, 2.5, 0, Math.PI * 2);
                    ctx.fillStyle = "#38D9FF";
                    ctx.shadowColor = "#00E5FF";
                    ctx.shadowBlur = 6;
                    ctx.fill();
                    ctx.shadowBlur = 0;
                }

                requestAnimationFrame(drawBrain);
            }

            drawBrain();
        })();
        </script>
        """
        render_html(brain_canvas_html)

        render_html("""
            <div style="font-family: 'JetBrains Mono', monospace; font-size: 0.7rem; margin-top: 0.55rem; display: flex; flex-direction: column; gap: 0.3rem;">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <span style="color: #8FA2C1;">Behavior Analysis</span>
                    <span style="color: #38D9FF;"><span class="pulse-dot online"></span> Scanning...</span>
                </div>
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <span style="color: #8FA2C1;">Anomaly Detection</span>
                    <span style="color: #38D9FF;"><span class="pulse-dot online"></span> Scanning...</span>
                </div>
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <span style="color: #8FA2C1;">ML Classification</span>
                    <span style="color: #10E79D;">Active</span>
                </div>
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <span style="color: #8FA2C1;">Threat Prediction</span>
                    <span style="color: #FF3B5C;"><span class="pulse-dot threat"></span> Scanning...</span>
                </div>
            </div>
            <div style="margin-top: 0.55rem;">
                <div style="display: flex; justify-content: space-between; font-size: 0.68rem; margin-bottom: 0.2rem; font-family: 'JetBrains Mono';">
                    <span style="color: #8FA2C1;">Processing...</span>
                    <span style="color: #38D9FF; font-weight: 700;">87%</span>
                </div>
                <div style="background: #020B1A; border: 1px solid rgba(22, 139, 255, 0.3); border-radius: 3px; height: 5px; width: 100%; overflow: hidden;">
                    <div style="background: linear-gradient(90deg, #168BFF, #00E5FF); width: 87%; height: 100%;"></div>
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
                <div style="display: flex; flex-direction: column; gap: 0.45rem; font-family: 'JetBrains Mono', monospace; font-size: 0.7rem;">
                    <div>
                        <div style="display: flex; justify-content: space-between; margin-bottom: 0.15rem;">
                            <span style="color: #F0F4F8;">Malware</span>
                            <span style="color: #FF3B5C;">36.1%</span>
                        </div>
                        <div style="background: #020B1A; border-radius: 3px; height: 5px; width: 100%; overflow: hidden;">
                            <div style="background: #FF3B5C; width: 36.1%; height: 100%;"></div>
                        </div>
                    </div>
                    <div>
                        <div style="display: flex; justify-content: space-between; margin-bottom: 0.15rem;">
                            <span style="color: #F0F4F8;">Phishing</span>
                            <span style="color: #FF7A00;">24.7%</span>
                        </div>
                        <div style="background: #020B1A; border-radius: 3px; height: 5px; width: 100%; overflow: hidden;">
                            <div style="background: #FF7A00; width: 24.7%; height: 100%;"></div>
                        </div>
                    </div>
                    <div>
                        <div style="display: flex; justify-content: space-between; margin-bottom: 0.15rem;">
                            <span style="color: #F0F4F8;">Exploits</span>
                            <span style="color: #38D9FF;">17.2%</span>
                        </div>
                        <div style="background: #020B1A; border-radius: 3px; height: 5px; width: 100%; overflow: hidden;">
                            <div style="background: #38D9FF; width: 17.2%; height: 100%;"></div>
                        </div>
                    </div>
                    <div>
                        <div style="display: flex; justify-content: space-between; margin-bottom: 0.15rem;">
                            <span style="color: #F0F4F8;">Unauthorized Access</span>
                            <span style="color: #FFB300;">12.4%</span>
                        </div>
                        <div style="background: #020B1A; border-radius: 3px; height: 5px; width: 100%; overflow: hidden;">
                            <div style="background: #FFB300; width: 12.4%; height: 100%;"></div>
                        </div>
                    </div>
                    <div>
                        <div style="display: flex; justify-content: space-between; margin-bottom: 0.15rem;">
                            <span style="color: #F0F4F8;">Other</span>
                            <span style="color: #10E79D;">7.6%</span>
                        </div>
                        <div style="background: #020B1A; border-radius: 3px; height: 5px; width: 100%; overflow: hidden;">
                            <div style="background: #10E79D; width: 7.6%; height: 100%;"></div>
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
                    <span class="cyber-card-subtitle">Security Compliance Overview</span>
                </div>
                <div style="display: flex; justify-content: space-around; align-items: center; margin: 0.5rem 0;">
                    <div class="compliance-badge">
                        <div>ISO 27001</div>
                        <div style="font-size: 0.55rem; color: #10E79D;">Compliant</div>
                    </div>
                    <div class="compliance-badge">
                        <div>SOC 2</div>
                        <div style="font-size: 0.55rem; color: #10E79D;">Compliant</div>
                    </div>
                    <div class="compliance-badge">
                        <div>GDPR</div>
                        <div style="font-size: 0.55rem; color: #10E79D;">Compliant</div>
                    </div>
                    <div class="compliance-badge">
                        <div>HIPAA</div>
                        <div style="font-size: 0.55rem; color: #10E79D;">Compliant</div>
                    </div>
                </div>
        """)

        if st.button("View Compliance Report", key="btn_view_compliance", use_container_width=True):
            st.switch_page("pages/5_Analysis_History.py")

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
                marker=dict(color=["#168BFF", "#38D9FF", "#10E79D"]),
                text=[text_count, image_count, video_count],
                textposition="auto"
            )])
            fig_bar.update_layout(
                paper_bgcolor="rgba(0,0,0,0)",
                plot_bgcolor="rgba(0,0,0,0)",
                font=dict(color="#F0F4F8", family="Inter"),
                margin=dict(l=20, r=20, t=10, b=30),
                height=180,
                yaxis=dict(gridcolor="rgba(22, 139, 255, 0.2)"),
                xaxis=dict(showgrid=False, gridcolor="rgba(0,0,0,0)")
            )
            st.plotly_chart(fig_bar, use_container_width=True, config={'displayModeBar': False})
