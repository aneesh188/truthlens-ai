"""
TruthLens AI - TRACE: Sensory Dive, Hyperspace Tunnel & Fluid 3D Sphere Experience
Recreates the exact visual experience from TRACE (Digital Trust & Media Intelligence Platform):
1. Stage 1: Detective Silhouettes, Greek Psi symbol, data coordinates, serif headline "Can you trust what you see?"
2. Stage 2: 15-second Hyperspace Dive Tunnel with 3D flying particle vortex, circular percentage tracker, countdown timer & Skip button.
3. Stage 3: Smooth transition to the TRACE platform featuring the 3D rotating point-cloud particle sphere with orbital ring,
   luminous lime-green (#bbf451) accents, custom magnetic cursor, and direct forensic dispatch launchpads.
"""

def get_trace_experience_html() -> str:
    """Returns standalone interactive HTML/JS/CSS for the complete TRACE sensory dive and landing experience."""
    return """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@500;700;800;900&family=Playfair+Display:ital,wght@0,600;0,800;1,600;1,800&family=Inter:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;700;800&display=swap');

    :root {
        --bg-void: #03070d;
        --bg-card: rgba(8, 16, 28, 0.75);
        --neon-lime: #bbf451;
        --neon-glow: rgba(187, 244, 81, 0.45);
        --accent-blue: #506cd9;
        --text-white: #ffffff;
        --text-dim: #8fa0b5;
        --border-glass: rgba(187, 244, 81, 0.22);
    }

    * {
        box-sizing: border-box;
        margin: 0;
        padding: 0;
        cursor: default;
    }

    body {
        background: var(--bg-void);
        color: var(--text-white);
        font-family: 'Inter', -apple-system, sans-serif;
        overflow-x: hidden;
        min-height: 100vh;
        position: relative;
    }

    /* Custom magnetic cursor */
    #cursor-follower {
        position: fixed;
        width: 32px;
        height: 32px;
        border: 1.5px solid var(--neon-lime);
        border-radius: 50%;
        pointer-events: none;
        z-index: 9999;
        transform: translate(-50%, -50%);
        transition: width 0.2s, height 0.2s, border-color 0.2s, background-color 0.2s;
        box-shadow: 0 0 12px var(--neon-glow);
    }

    #cursor-dot {
        position: fixed;
        width: 5px;
        height: 5px;
        background: var(--neon-lime);
        border-radius: 50%;
        pointer-events: none;
        z-index: 10000;
        transform: translate(-50%, -50%);
    }

    /* Stage 1: Sensory Dive Intro Screen */
    #stage-dive-intro {
        position: relative;
        width: 100%;
        min-height: 640px;
        background: radial-gradient(circle at 50% 40%, rgba(20, 35, 20, 0.35) 0%, rgba(3, 7, 13, 0.98) 75%), #03070d;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        padding: 1.5rem 2.5rem;
        overflow: hidden;
        border-radius: 16px;
        border: 1px solid rgba(187, 244, 81, 0.15);
    }

    /* Top dive header */
    .dive-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.75rem;
        letter-spacing: 0.08em;
        z-index: 10;
    }

    .dive-header-left {
        display: flex;
        align-items: center;
        gap: 0.75rem;
        color: var(--neon-lime);
    }

    .tag-gateway {
        background: rgba(187, 244, 81, 0.1);
        border: 1px solid var(--neon-lime);
        color: var(--neon-lime);
        padding: 0.2rem 0.55rem;
        border-radius: 4px;
        font-size: 0.68rem;
    }

    .btn-skip {
        background: transparent;
        color: #8fa0b5;
        border: 1px solid rgba(143, 160, 181, 0.3);
        padding: 0.35rem 0.85rem;
        border-radius: 4px;
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.72rem;
        font-weight: 700;
        cursor: pointer;
        transition: all 0.2s ease;
    }

    .btn-skip:hover {
        color: var(--neon-lime);
        border-color: var(--neon-lime);
        box-shadow: 0 0 10px var(--neon-glow);
    }

    /* Center Detective Stage */
    .detective-stage {
        position: relative;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        margin: 1.5rem 0;
        z-index: 10;
    }

    .detective-wrapper {
        position: relative;
        width: 320px;
        height: 220px;
        display: flex;
        align-items: center;
        justify-content: center;
        cursor: pointer;
    }

    .detective-silhouette {
        transition: all 0.3s cubic-bezier(0.34, 1.3, 0.64, 1);
    }

    .detective-wrapper:hover .detective-silhouette {
        transform: scale(1.05);
        filter: drop-shadow(0 0 20px rgba(187, 244, 81, 0.6));
    }

    /* Floating symbols around detective */
    .symbol-psi {
        position: absolute;
        top: 20px;
        left: 50px;
        color: #ffffff;
        font-size: 1.2rem;
        font-family: serif;
        opacity: 0.75;
        animation: float-slow 3s infinite ease-in-out;
    }

    .symbol-data-1 {
        position: absolute;
        bottom: 40px;
        right: 40px;
        color: var(--neon-lime);
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.7rem;
        opacity: 0.7;
    }

    .symbol-data-2 {
        position: absolute;
        bottom: 70px;
        right: 25px;
        color: #8fa0b5;
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.65rem;
    }

    .symbol-hex {
        position: absolute;
        bottom: 25px;
        right: -80px;
        color: #8fa0b5;
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.8rem;
        letter-spacing: 0.1em;
    }

    .badge-continuum {
        background: rgba(0, 0, 0, 0.6);
        border: 1px solid rgba(187, 244, 81, 0.3);
        border-radius: 999px;
        padding: 0.25rem 0.8rem;
        color: var(--neon-lime);
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.68rem;
        font-weight: 700;
        letter-spacing: 0.08em;
        margin-bottom: 0.8rem;
        display: inline-flex;
        align-items: center;
        gap: 0.4rem;
    }

    .hero-heading-serif {
        font-family: 'Playfair Display', serif;
        font-size: 2.7rem;
        font-weight: 600;
        letter-spacing: -0.01em;
        text-align: center;
        margin-bottom: 0.6rem;
        color: #ffffff;
    }

    .hero-heading-serif em {
        font-style: italic;
        color: var(--neon-lime);
        text-shadow: 0 0 20px rgba(187, 244, 81, 0.4);
    }

    .hero-desc {
        font-size: 0.88rem;
        color: var(--text-dim);
        text-align: center;
        max-width: 580px;
        line-height: 1.55;
        margin-bottom: 1.5rem;
    }

    .btn-detective-start {
        background: var(--neon-lime);
        color: #03070d;
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.85rem;
        font-weight: 800;
        letter-spacing: 0.06em;
        padding: 0.75rem 2rem;
        border-radius: 999px;
        border: none;
        cursor: pointer;
        box-shadow: 0 0 25px rgba(187, 244, 81, 0.45);
        transition: all 0.25s cubic-bezier(0.34, 1.3, 0.64, 1);
        display: inline-flex;
        align-items: center;
        gap: 0.6rem;
    }

    .btn-detective-start:hover {
        transform: translateY(-3px) scale(1.03);
        box-shadow: 0 0 35px rgba(187, 244, 81, 0.7);
        background: #d4ff78;
    }

    /* Stage 2: Hyperspace Dive Tunnel Canvas & Overlay */
    #stage-tunnel-dive {
        display: none;
        position: relative;
        width: 100%;
        height: 640px;
        border-radius: 16px;
        overflow: hidden;
        border: 1px solid var(--neon-lime);
        box-shadow: 0 0 40px rgba(187, 244, 81, 0.25);
    }

    #tunnel-canvas {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        z-index: 1;
    }

    .tunnel-hud {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        z-index: 10;
        pointer-events: none;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        padding: 1.8rem 2.5rem;
    }

    .tunnel-top {
        display: flex;
        justify-content: space-between;
        align-items: center;
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.75rem;
    }

    .countdown-box {
        background: rgba(0, 0, 0, 0.75);
        border: 1px solid var(--neon-lime);
        color: var(--neon-lime);
        padding: 0.4rem 0.9rem;
        border-radius: 4px;
        font-weight: 800;
        font-size: 0.8rem;
        letter-spacing: 0.08em;
    }

    .tunnel-center {
        text-align: center;
        margin: auto;
    }

    /* Circular progress ring */
    .progress-circle-wrap {
        position: relative;
        width: 110px;
        height: 110px;
        margin: 0 auto 1.2rem auto;
    }

    .progress-circle-svg {
        transform: rotate(-90deg);
        width: 110px;
        height: 110px;
    }

    .progress-circle-bg {
        fill: none;
        stroke: rgba(255, 255, 255, 0.1);
        stroke-width: 6;
    }

    .progress-circle-fill {
        fill: none;
        stroke: var(--neon-lime);
        stroke-width: 6;
        stroke-linecap: round;
        stroke-dasharray: 283;
        stroke-dashoffset: 283;
        transition: stroke-dashoffset 0.1s linear;
        filter: drop-shadow(0 0 10px var(--neon-lime));
    }

    .progress-percentage {
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        font-family: 'JetBrains Mono', monospace;
        font-size: 1.2rem;
        font-weight: 900;
        color: #ffffff;
    }

    .phase-title {
        font-family: 'Cinzel', serif;
        font-size: 1.35rem;
        font-weight: 700;
        letter-spacing: 0.08em;
        color: #ffffff;
        margin-bottom: 0.4rem;
        text-shadow: 0 0 15px rgba(255, 255, 255, 0.6);
    }

    .phase-sub {
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.75rem;
        color: var(--neon-lime);
        letter-spacing: 0.08em;
        margin-bottom: 1.2rem;
    }

    .tunnel-bar-track {
        width: 320px;
        height: 4px;
        background: rgba(255, 255, 255, 0.15);
        border-radius: 999px;
        margin: 0 auto;
        overflow: hidden;
    }

    .tunnel-bar-fill {
        width: 0%;
        height: 100%;
        background: var(--neon-lime);
        box-shadow: 0 0 10px var(--neon-lime);
        transition: width 0.1s linear;
    }

    /* Stage 3: Destination Web Experience (TRACE / TruthLens Platform) */
    #stage-destination {
        display: none;
        position: relative;
        width: 100%;
        opacity: 0;
        transition: opacity 0.8s ease-in;
    }

    /* TRACE Navigation */
    .trace-nav {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 1rem 1.8rem;
        background: rgba(6, 12, 22, 0.85);
        backdrop-filter: blur(20px);
        border: 1px solid rgba(187, 244, 81, 0.2);
        border-radius: 12px;
        margin-bottom: 0.6rem;
    }

    .trace-brand {
        display: flex;
        align-items: center;
        gap: 0.75rem;
    }

    .brand-icon {
        width: 28px;
        height: 28px;
        border-radius: 50%;
        border: 2px solid var(--neon-lime);
        display: flex;
        align-items: center;
        justify-content: center;
        box-shadow: 0 0 10px var(--neon-glow);
    }

    .brand-icon-inner {
        width: 10px;
        height: 10px;
        border-radius: 50%;
        background: var(--neon-lime);
    }

    .brand-title {
        font-family: 'JetBrains Mono', monospace;
        font-size: 1.1rem;
        font-weight: 900;
        color: #ffffff;
        letter-spacing: 0.05em;
    }

    .brand-pill-online {
        background: rgba(187, 244, 81, 0.15);
        color: var(--neon-lime);
        font-size: 0.62rem;
        font-family: 'JetBrains Mono', monospace;
        padding: 0.15rem 0.45rem;
        border-radius: 3px;
        border: 1px solid var(--neon-lime);
        margin-left: 0.4rem;
    }

    .brand-sub {
        font-size: 0.65rem;
        color: var(--text-dim);
        letter-spacing: 0.08em;
        text-transform: uppercase;
    }

    .trace-links {
        display: flex;
        gap: 1.5rem;
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.75rem;
        font-weight: 700;
    }

    .trace-link {
        color: var(--text-dim);
        cursor: pointer;
        transition: color 0.2s ease;
    }

    .trace-link:hover, .trace-link.active {
        color: var(--neon-lime);
    }

    .trace-controls {
        display: flex;
        gap: 0.6rem;
        align-items: center;
    }

    .btn-investigate {
        background: rgba(187, 244, 81, 0.15);
        border: 1.5px solid var(--neon-lime);
        color: var(--neon-lime);
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.75rem;
        font-weight: 800;
        padding: 0.45rem 1.15rem;
        border-radius: 999px;
        cursor: pointer;
        transition: all 0.2s ease;
    }

    .btn-investigate:hover {
        background: var(--neon-lime);
        color: #03070d;
        box-shadow: 0 0 15px var(--neon-glow);
    }

    /* Secondary Telemetry Ribbon */
    .telemetry-ribbon {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 0.4rem 1.5rem;
        background: rgba(3, 7, 13, 0.7);
        border: 1px solid rgba(143, 160, 181, 0.15);
        border-radius: 6px;
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.68rem;
        color: var(--text-dim);
        margin-bottom: 1.25rem;
    }

    .telemetry-ribbon span.highlight {
        color: var(--neon-lime);
    }

    /* Destination Hero Grid: Left Content + Right 3D Particle Sphere */
    .dest-hero-grid {
        display: grid;
        grid-template-columns: 1.15fr 0.95fr;
        gap: 2rem;
        align-items: center;
        margin-bottom: 2rem;
    }

    .dest-hero-left {
        padding-right: 1rem;
    }

    .platform-badge {
        display: inline-flex;
        align-items: center;
        gap: 0.4rem;
        color: var(--text-dim);
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.72rem;
        font-weight: 700;
        letter-spacing: 0.08em;
        text-transform: uppercase;
        margin-bottom: 1rem;
    }

    .platform-badge::before {
        content: '';
        width: 6px;
        height: 6px;
        border-radius: 50%;
        background: var(--neon-lime);
        box-shadow: 0 0 8px var(--neon-lime);
    }

    .dest-title {
        font-family: 'Playfair Display', serif;
        font-size: 3.4rem;
        font-weight: 800;
        line-height: 1.12;
        letter-spacing: -0.02em;
        margin-bottom: 1.2rem;
        color: #ffffff;
    }

    .dest-title span.lime-underline {
        color: var(--neon-lime);
        position: relative;
        display: inline-block;
        font-style: italic;
    }

    .dest-title span.lime-underline::after {
        content: '';
        position: absolute;
        bottom: 2px;
        left: 0;
        width: 100%;
        height: 3px;
        background: var(--neon-lime);
        box-shadow: 0 0 12px var(--neon-glow);
    }

    .dest-desc {
        font-size: 0.95rem;
        color: var(--text-dim);
        line-height: 1.65;
        margin-bottom: 1.8rem;
        max-width: 520px;
    }

    .dest-cta-row {
        display: flex;
        gap: 1rem;
        align-items: center;
        margin-bottom: 2rem;
    }

    .btn-cta-lime {
        background: var(--neon-lime);
        color: #03070d;
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.85rem;
        font-weight: 800;
        padding: 0.85rem 2rem;
        border-radius: 999px;
        border: none;
        cursor: pointer;
        box-shadow: 0 0 25px rgba(187, 244, 81, 0.45);
        transition: all 0.25s ease;
    }

    .btn-cta-lime:hover {
        transform: translateY(-2px);
        box-shadow: 0 0 35px rgba(187, 244, 81, 0.7);
        background: #d4ff78;
    }

    .btn-cta-outline {
        background: rgba(6, 12, 22, 0.6);
        color: #ffffff;
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.85rem;
        font-weight: 700;
        padding: 0.85rem 1.8rem;
        border-radius: 999px;
        border: 1.5px solid rgba(143, 160, 181, 0.3);
        cursor: pointer;
        transition: all 0.2s ease;
    }

    .btn-cta-outline:hover {
        border-color: var(--neon-lime);
        color: var(--neon-lime);
    }

    /* 3 Bottom Metrics */
    .dest-metric-chips {
        display: flex;
        gap: 1.5rem;
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.75rem;
        border-top: 1px solid rgba(143, 160, 181, 0.15);
        padding-top: 1.2rem;
    }

    .dest-chip-item b {
        color: #ffffff;
        font-size: 0.95rem;
    }

    .dest-chip-item span {
        color: var(--text-dim);
        font-size: 0.68rem;
        display: block;
    }

    /* Right 3D Particle Sphere Container */
    .sphere-container {
        position: relative;
        width: 100%;
        height: 440px;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
    }

    #sphere-canvas {
        width: 100%;
        height: 380px;
    }

    .sphere-telemetry-tag {
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.68rem;
        color: var(--neon-lime);
        letter-spacing: 0.08em;
        margin-top: 0.4rem;
        opacity: 0.85;
    }

    @keyframes float-slow {
        0%, 100% { transform: translateY(0); }
        50% { transform: translateY(-8px); }
    }
</style>
</head>
<body>

<!-- Custom magnetic cursor -->
<div id="cursor-follower"></div>
<div id="cursor-dot"></div>

<!-- STAGE 1: SENSORY DIVE INTRO SCREEN -->
<div id="stage-dive-intro">
    <div class="dive-header">
        <div class="dive-header-left">
            <span>TRACE // HYPERSPACE SENSORY DIVE (15s FLIGHT)</span>
            <span class="tag-gateway">ROAD TO TRUTH GATEWAY</span>
        </div>
        <div>
            <button class="btn-skip" onclick="skipToWebsite()">SKIP TO WEBSITE [ESC] &gt;</button>
        </div>
    </div>

    <div class="detective-stage">
        <!-- Detective Silhouettes Vector Illustration -->
        <div class="detective-wrapper" onclick="startHyperspaceDive()">
            <div class="symbol-psi">Ψ</div>
            <div class="symbol-data-1">0xFA 1</div>
            <div class="symbol-data-2">0x4F</div>
            
            <svg class="detective-silhouette" width="300" height="190" viewBox="0 0 300 190" fill="none" xmlns="http://www.w3.org/2000/svg">
                <!-- Left Detective -->
                <path d="M 55 120 L 45 180 L 80 180 L 70 120 Z" fill="#2d3748" opacity="0.55"/>
                <circle cx="62" cy="115" r="14" fill="#2d3748" opacity="0.55"/>
                <ellipse cx="62" cy="108" rx="20" ry="5" fill="#2d3748" opacity="0.55"/>
                
                <!-- Right Detective -->
                <path d="M 235 120 L 225 180 L 260 180 L 250 120 Z" fill="#2d3748" opacity="0.55"/>
                <circle cx="242" cy="115" r="14" fill="#2d3748" opacity="0.55"/>
                <ellipse cx="242" cy="108" rx="20" ry="5" fill="#2d3748" opacity="0.55"/>

                <!-- Center Lead Detective (Glowing in Neon Lime) -->
                <!-- Trenchcoat Body -->
                <path d="M 125 75 L 105 180 L 195 180 L 175 75 Z" fill="#0b1724" stroke="#bbf451" stroke-width="2.5"/>
                <!-- Lapel Collars -->
                <path d="M 125 75 L 140 125 L 150 95 L 160 125 L 175 75" fill="none" stroke="#bbf451" stroke-width="2"/>
                <!-- Fedora Hat Brim -->
                <ellipse cx="150" cy="62" rx="42" ry="10" fill="#0b1724" stroke="#bbf451" stroke-width="2.5"/>
                <!-- Fedora Hat Crown -->
                <path d="M 130 62 C 130 42 170 42 170 62 Z" fill="#0b1724" stroke="#bbf451" stroke-width="2.5"/>
                
                <!-- Glowing Tie / Sensor Badge -->
                <rect x="145" y="125" width="10" height="4" rx="2" fill="#ffd166"/>
                <circle cx="150" cy="145" r="3" fill="#ffffff"/>
                <circle cx="150" cy="160" r="3" fill="#ffffff"/>
                
                <!-- Server / Document Icon Floating next to detective -->
                <rect x="180" y="110" width="18" height="24" rx="3" fill="#0b1724" stroke="#ffffff" stroke-width="1.8"/>
                <line x1="185" y1="116" x2="193" y2="116" stroke="#ffffff" stroke-width="1.5"/>
                <line x1="185" y1="122" x2="193" y2="122" stroke="#ffffff" stroke-width="1.5"/>
                <line x1="185" y1="128" x2="191" y2="128" stroke="#ffffff" stroke-width="1.5"/>

                <!-- Glowing contour frame around detective -->
                <rect x="92" y="32" width="116" height="154" rx="4" fill="none" stroke="rgba(187, 244, 81, 0.45)" stroke-width="1.5" stroke-dasharray="8,6"/>
            </svg>
        </div>

        <div class="badge-continuum">
            <span>●</span> 3D DATA CONTINUUM READY
        </div>

        <h1 class="hero-heading-serif">
            Can you trust <em>what you see?</em>
        </h1>
        <p class="hero-desc">
            Every piece of synthetic content leaves a footprint. Click below to dive through 15 seconds
            of hyperspace deconstruction across layers of distorted reality.
        </p>

        <button class="btn-detective-start" onclick="startHyperspaceDive()">
            <span>🔍 CLICK DETECTIVE TO START // 15S DIVE</span>
        </button>
    </div>

    <div style="font-family: 'JetBrains Mono', monospace; font-size: 0.68rem; color: #8fa0b5; text-align: center;">
        TRUTHLENS FORENSIC CONTINUUM // 0x4F LATENCY PROTOCOL
    </div>
</div>

<!-- STAGE 2: HYPERSPACE DIVE TUNNEL SCREEN -->
<div id="stage-tunnel-dive">
    <canvas id="tunnel-canvas"></canvas>

    <div class="tunnel-hud">
        <div class="tunnel-top">
            <div style="color: var(--neon-lime);">
                <span>TRACE // HYPERSPACE SENSORY DIVE (WARP VELOCITY: 6.824 M/S)</span>
            </div>
            <div style="display: flex; gap: 0.8rem; align-items: center;">
                <div class="countdown-box" id="countdown-timer">COUNTDOWN: 15.0s</div>
                <button class="btn-skip" onclick="skipToWebsite()">SKIP [ESC] &gt;</button>
            </div>
        </div>

        <div class="tunnel-center">
            <div class="progress-circle-wrap">
                <svg class="progress-circle-svg" viewBox="0 0 100 100">
                    <circle class="progress-circle-bg" cx="50" cy="50" r="45"></circle>
                    <circle class="progress-circle-fill" id="progress-circle" cx="50" cy="50" r="45"></circle>
                </svg>
                <div class="progress-percentage" id="progress-pct">0%</div>
            </div>

            <div class="phase-title" id="phase-title">PHASE 1/4: SENSORY DECONSTRUCTION</div>
            <div class="phase-sub" id="phase-sub">ALTITUDE: 0.00M // DECRYPTING CONTENT FOOTPRINTS</div>

            <div class="tunnel-bar-track">
                <div class="tunnel-bar-fill" id="tunnel-bar-fill"></div>
            </div>
        </div>

        <div style="font-family: 'JetBrains Mono', monospace; font-size: 0.68rem; color: #8fa0b5; display: flex; justify-content: space-between;">
            <span>RADIAL VELOCITY ACTIVE</span>
            <span>TARGET: DIGITAL TRUTH GATEWAY</span>
        </div>
    </div>
</div>

<!-- STAGE 3: DESTINATION PLATFORM SCREEN (TRACE) -->
<div id="stage-destination">
    <!-- Top Navigation -->
    <div class="trace-nav">
        <div class="trace-brand">
            <div class="brand-icon">
                <div class="brand-icon-inner"></div>
            </div>
            <div>
                <div style="display: flex; align-items: center;">
                    <span class="brand-title">TRACE</span>
                    <span class="brand-pill-online">ONLINE</span>
                </div>
                <div class="brand-sub">NEXUS INTELLIGENCE LAB</div>
            </div>
        </div>

        <div class="trace-links">
            <span class="trace-link active">00 // STORY</span>
            <span class="trace-link">01 // MEDIA</span>
            <span class="trace-link">02 // INFO</span>
            <span class="trace-link">03 // SECURITY</span>
        </div>

        <div class="trace-controls">
            <button class="btn-skip" style="border-radius: 999px;">☀️ LIGHT</button>
            <button class="btn-investigate" onclick="scrollToDiagnostics()">INVESTIGATE &gt;</button>
        </div>
    </div>

    <!-- Status Ribbon -->
    <div class="telemetry-ribbon">
        <div>
            <span>SENSORY_TELEMETRY // <span class="highlight">FLUID CONTINUUM</span></span>
            <span style="margin-left: 1.5rem;">SHA-256 REPRODUCIBILITY ACTIVE</span>
        </div>
        <div>
            <span>SPEC: <span class="highlight">ISO/IEC 27037 FORENSIC STANDARD</span></span>
        </div>
    </div>

    <!-- Hero Section: Left Text + Right 3D Particle Sphere Globe -->
    <div class="dest-hero-grid">
        <div class="dest-hero-left">
            <div class="platform-badge">
                DIGITAL TRUST & MEDIA INTELLIGENCE PLATFORM
            </div>

            <h1 class="dest-title">
                Can you trust<br/>
                <span class="lime-underline">what you see?</span>
            </h1>

            <p class="dest-desc">
                Reality can be manipulated. Information can be fabricated. TRACE helps you investigate
                what lies beneath digital content through verifiable, mathematical, and cryptographic forensics.
            </p>

            <div class="dest-cta-row">
                <button class="btn-cta-lime" onclick="scrollToDiagnostics()">
                    START INVESTIGATION
                </button>
                <button class="btn-cta-outline" onclick="restartSensoryDive()">
                    🔍 EXPLORE TRACE
                </button>
            </div>

            <div class="dest-metric-chips">
                <div class="dest-chip-item">
                    <b>12 MODULES</b>
                    <span>FORENSIC SUITE</span>
                </div>
                <div class="dest-chip-item">
                    <b>ADVERSARY</b>
                    <span>RESISTANT ENGINE</span>
                </div>
                <div class="dest-chip-item">
                    <b>ZERO RETENTION</b>
                    <span>PRIVACY ASSURED</span>
                </div>
            </div>
        </div>

        <!-- Right 3D Particle Sphere -->
        <div class="sphere-container">
            <canvas id="sphere-canvas"></canvas>
            <div class="sphere-telemetry-tag">
                @SIGNAL_ACQUISITION RADIAL DENSITY: 2400 PTS LATENCY: 1.2ms
            </div>
        </div>
    </div>
</div>

<script>
    // Magnetic Custom Cursor
    const cursorFollower = document.getElementById('cursor-follower');
    const cursorDot = document.getElementById('cursor-dot');
    let mouseX = window.innerWidth / 2;
    let mouseY = window.innerHeight / 2;
    let followerX = mouseX;
    let followerY = mouseY;

    window.addEventListener('mousemove', (e) => {
        mouseX = e.clientX;
        mouseY = e.clientY;
        cursorDot.style.left = mouseX + 'px';
        cursorDot.style.top = mouseY + 'px';
    });

    function animateCursor() {
        followerX += (mouseX - followerX) * 0.15;
        followerY += (mouseY - followerY) * 0.15;
        cursorFollower.style.left = followerX + 'px';
        cursorFollower.style.top = followerY + 'px';
        requestAnimationFrame(animateCursor);
    }
    animateCursor();

    // Stage Handlers
    const stageIntro = document.getElementById('stage-dive-intro');
    const stageTunnel = document.getElementById('stage-tunnel-dive');
    const stageDest = document.getElementById('stage-destination');

    let diveDuration = 15.0; // 15 seconds
    let diveRemaining = diveDuration;
    let diveTimer = null;
    let isDiving = false;

    // Web Audio Sound Synthesizer
    function playSensoryDiveAudio() {
        try {
            const AudioContext = window.AudioContext || window.webkitAudioContext;
            if (!AudioContext) return;
            const actx = new AudioContext();

            // Sub-bass sweep
            const osc = actx.createOscillator();
            const gain = actx.createGain();
            osc.type = 'sawtooth';
            osc.frequency.setValueAtTime(60, actx.currentTime);
            osc.frequency.exponentialRampToValueAtTime(180, actx.currentTime + 3);
            gain.gain.setValueAtTime(0.4, actx.currentTime);
            gain.gain.exponentialRampToValueAtTime(0.01, actx.currentTime + 4);
            osc.connect(gain);
            gain.connect(actx.destination);
            osc.start();
            osc.stop(actx.currentTime + 4);
        } catch(e) {}
    }

    // Escape Key listener for quick skip
    window.addEventListener('keydown', (e) => {
        if (e.key === 'Escape') {
            skipToWebsite();
        }
    });

    function startHyperspaceDive() {
        if (isDiving) return;
        isDiving = true;
        playSensoryDiveAudio();

        stageIntro.style.display = 'none';
        stageTunnel.style.display = 'block';
        initTunnelCanvas();

        diveRemaining = diveDuration;
        const countdownEl = document.getElementById('countdown-timer');
        const progressCircle = document.getElementById('progress-circle');
        const progressPct = document.getElementById('progress-pct');
        const phaseTitle = document.getElementById('phase-title');
        const phaseSub = document.getElementById('phase-sub');
        const tunnelBar = document.getElementById('tunnel-bar-fill');

        const startTime = Date.now();

        diveTimer = setInterval(() => {
            const elapsed = (Date.now() - startTime) / 1000;
            const remaining = Math.max(0, diveDuration - elapsed);
            const progress = Math.min(1.0, elapsed / diveDuration);
            const pct = Math.floor(progress * 100);

            countdownEl.innerText = `COUNTDOWN: ${remaining.toFixed(1)}s`;
            progressPct.innerText = `${pct}%`;
            tunnelBar.style.width = `${pct}%`;

            // Circle perimeter = 2 * PI * 45 = 282.74
            const offset = 283 - (283 * progress);
            progressCircle.style.strokeDashoffset = offset;

            // Phase milestones
            if (pct < 25) {
                phaseTitle.innerText = "PHASE 1/4: SENSORY DECONSTRUCTION";
                phaseSub.innerText = `ALTITUDE: ${(elapsed * 400).toFixed(0)}M // DECRYPTING CONTENT FOOTPRINTS`;
            } else if (pct < 50) {
                phaseTitle.innerText = "PHASE 2/4: HYPERSPACE DIVE TUNNEL // ROAD TO TRUTH";
                phaseSub.innerText = `VELOCITY: ${(elapsed * 900).toFixed(0)} KM/S // PARSING NOISE CONTINUUM`;
            } else if (pct < 75) {
                phaseTitle.innerText = "PHASE 3/4: MAXIMUM WARP VELOCITY // REVEALING FOOTPRINTS";
                phaseSub.innerText = "SPECTRAL HARMONICS COHERENT // ZERO ANOMALIES MASKED";
            } else {
                phaseTitle.innerText = "PHASE 4/4: CONVERGENCE AT DIGITAL TRUTH GATEWAY";
                phaseSub.innerText = "ESTABLISHING CRYPTOGRAPHIC ANCHOR // DECRYPTED";
            }

            if (remaining <= 0) {
                clearInterval(diveTimer);
                finishDive();
            }
        }, 50);
    }

    function skipToWebsite() {
        if (diveTimer) clearInterval(diveTimer);
        finishDive();
    }

    function finishDive() {
        isDiving = false;
        stageTunnel.style.display = 'none';
        stageIntro.style.display = 'none';
        stageDest.style.display = 'block';

        setTimeout(() => {
            stageDest.style.opacity = '1';
            initSphereCanvas();
        }, 50);
    }

    function restartSensoryDive() {
        stageDest.style.opacity = '0';
        setTimeout(() => {
            stageDest.style.display = 'none';
            stageIntro.style.display = 'flex';
        }, 300);
    }

    function scrollToDiagnostics() {
        window.parent.postMessage({ type: 'streamlit:scroll', target: 'diagnostics' }, '*');
    }

    // -------------------------------------------------------------
    // STAGE 2: 3D HYPERSPACE TUNNEL PARTICLE CANVAS
    // -------------------------------------------------------------
    let tunnelCanvas, tunnelCtx, tW, tH, tunnelParticles = [];
    const NUM_TUNNEL_PARTICLES = 650;

    function initTunnelCanvas() {
        tunnelCanvas = document.getElementById('tunnel-canvas');
        if (!tunnelCanvas) return;
        tunnelCtx = tunnelCanvas.getContext('2d');
        tW = tunnelCanvas.width = tunnelCanvas.offsetWidth;
        tH = tunnelCanvas.height = tunnelCanvas.offsetHeight;

        tunnelParticles = [];
        for (let i = 0; i < NUM_TUNNEL_PARTICLES; i++) {
            tunnelParticles.push({
                x: (Math.random() - 0.5) * tW * 2,
                y: (Math.random() - 0.5) * tH * 2,
                z: Math.random() * tW,
                pz: Math.random() * tW,
                color: Math.random() > 0.4 ? '#bbf451' : (Math.random() > 0.5 ? '#506cd9' : '#ffffff')
            });
        }

        requestAnimationFrame(renderTunnel);
    }

    function renderTunnel() {
        if (!isDiving || !tunnelCtx) return;
        tunnelCtx.fillStyle = 'rgba(3, 7, 13, 0.35)';
        tunnelCtx.fillRect(0, 0, tW, tH);

        const cx = tW / 2;
        const cy = tH / 2;

        for (let i = 0; i < NUM_TUNNEL_PARTICLES; i++) {
            let p = tunnelParticles[i];
            p.pz = p.z;
            p.z -= 28; // high speed

            if (p.z <= 0) {
                p.z = tW;
                p.pz = tW;
                p.x = (Math.random() - 0.5) * tW * 2;
                p.y = (Math.random() - 0.5) * tH * 2;
            }

            const k = 250 / p.z;
            const px = p.x * k + cx;
            const py = p.y * k + cy;

            const pk = 250 / p.pz;
            const ppx = p.x * pk + cx;
            const ppy = p.y * pk + cy;

            if (px >= 0 && px < tW && py >= 0 && py < tH) {
                tunnelCtx.beginPath();
                tunnelCtx.moveTo(ppx, ppy);
                tunnelCtx.lineTo(px, py);
                tunnelCtx.lineWidth = Math.min(3.5, (1 - p.z / tW) * 4);
                tunnelCtx.strokeStyle = p.color;
                tunnelCtx.stroke();
            }
        }

        requestAnimationFrame(renderTunnel);
    }

    // -------------------------------------------------------------
    // STAGE 3: 3D ROTATING PARTICLE SPHERE (POINT CLOUD GLOBE)
    // -------------------------------------------------------------
    let sphereCanvas, sphereCtx, sW, sH;
    let spherePoints = [];
    let ringPoints = [];
    const SPHERE_POINTS_COUNT = 2400;
    const RING_POINTS_COUNT = 450;
    let angleX = 0.2;
    let angleY = 0;

    function initSphereCanvas() {
        sphereCanvas = document.getElementById('sphere-canvas');
        if (!sphereCanvas) return;
        sphereCtx = sphereCanvas.getContext('2d');
        sW = sphereCanvas.width = sphereCanvas.offsetWidth;
        sH = sphereCanvas.height = sphereCanvas.offsetHeight;

        spherePoints = [];
        const radius = 135;

        // Fibonacci sphere point distribution (2400 points)
        const phi = Math.PI * (3 - Math.sqrt(5));
        for (let i = 0; i < SPHERE_POINTS_COUNT; i++) {
            const y = 1 - (i / (SPHERE_POINTS_COUNT - 1)) * 2;
            const radiusAtY = Math.sqrt(1 - y * y);
            const theta = phi * i;

            const x = Math.cos(theta) * radiusAtY;
            const z = Math.sin(theta) * radiusAtY;

            spherePoints.push({
                x: x * radius,
                y: y * radius,
                z: z * radius
            });
        }

        // Elliptical planetary orbit ring
        ringPoints = [];
        const ringRadius = 185;
        for (let i = 0; i < RING_POINTS_COUNT; i++) {
            const rad = (i / RING_POINTS_COUNT) * Math.PI * 2;
            ringPoints.push({
                x: Math.cos(rad) * ringRadius,
                y: (Math.sin(rad) * ringRadius * 0.35),
                z: Math.sin(rad) * ringRadius
            });
        }

        sphereCanvas.addEventListener('mousemove', (e) => {
            const rect = sphereCanvas.getBoundingClientRect();
            const relX = e.clientX - rect.left - sW / 2;
            const relY = e.clientY - rect.top - sH / 2;
            angleX = relY * 0.001;
            angleY = relX * 0.001;
        });

        requestAnimationFrame(renderSphere);
    }

    function renderSphere() {
        if (!sphereCtx) return;
        sphereCtx.clearRect(0, 0, sW, sH);

        angleY += 0.007; // continuous rotation
        const cosY = Math.cos(angleY);
        const sinY = Math.sin(angleY);
        const cosX = Math.cos(angleX);
        const sinX = Math.sin(angleX);

        const cx = sW / 2;
        const cy = sH / 2;

        // Draw 3D Sphere Points
        for (let i = 0; i < SPHERE_POINTS_COUNT; i++) {
            const p = spherePoints[i];

            // Rotate around Y
            let x1 = p.x * cosY - p.z * sinY;
            let z1 = p.z * cosY + p.x * sinY;

            // Rotate around X
            let y1 = p.y * cosX - z1 * sinX;
            let z2 = z1 * cosX + p.y * sinX;

            const scale = 320 / (320 + z2);
            const px = x1 * scale + cx;
            const py = y1 * scale + cy;

            if (scale > 0) {
                const alpha = Math.max(0.12, (z2 + 135) / 270);
                const ptSize = Math.max(0.7, scale * 1.5);
                sphereCtx.beginPath();
                sphereCtx.arc(px, py, ptSize, 0, Math.PI * 2);
                sphereCtx.fillStyle = `rgba(187, 244, 81, ${alpha.toFixed(2)})`;
                sphereCtx.fill();
            }
        }

        // Draw Orbit Ring Points
        for (let i = 0; i < RING_POINTS_COUNT; i++) {
            const rp = ringPoints[i];

            let x1 = rp.x * cosY - rp.z * sinY;
            let z1 = rp.z * cosY + rp.x * sinY;

            let y1 = rp.y * cosX - z1 * sinX;
            let z2 = z1 * cosX + rp.y * sinX;

            const scale = 320 / (320 + z2);
            const px = x1 * scale + cx;
            const py = y1 * scale + cy;

            if (scale > 0) {
                const alpha = Math.max(0.15, (z2 + 185) / 370);
                sphereCtx.beginPath();
                sphereCtx.arc(px, py, 1.2, 0, Math.PI * 2);
                sphereCtx.fillStyle = `rgba(255, 255, 255, ${alpha.toFixed(2)})`;
                sphereCtx.fill();
            }
        }

        requestAnimationFrame(renderSphere);
    }
</script>
</body>
</html>
"""


def get_warp_portal_html(height: int = 680) -> str:
    """Alias for get_trace_experience_html to support legacy or custom callers."""
    return get_trace_experience_html()

