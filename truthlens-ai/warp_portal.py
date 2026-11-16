"""
TruthLens AI - Warp Speed Portal & Scrollytelling Hero Component
Renders an interactive Three/Canvas hyperspace jump with Web Audio sound synthesis,
parallax starfield, glassmorphism UI, and cinematic transition effects.
"""

def get_warp_portal_html(height: int = 560) -> str:
    """Returns standalone interactive HTML/JS/CSS for the hyperspace warp experience."""
    return f"""
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800;900&family=JetBrains+Mono:wght@500;700;800&display=swap');
    
    * {{
        box-sizing: border-box;
        margin: 0;
        padding: 0;
        user-select: none;
    }}
    
    body {{
        background: #000621;
        color: #ffffff;
        font-family: 'Inter', sans-serif;
        overflow: hidden;
        height: 100vh;
        width: 100vw;
        position: relative;
    }}

    #space-canvas {{
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        z-index: 1;
    }}

    /* Shockwave ring */
    .shockwave {{
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%) scale(0);
        width: 100px;
        height: 100px;
        border-radius: 50%;
        border: 4px solid #ffe3c5;
        box-shadow: 0 0 50px #506cd9, inset 0 0 30px #22d974;
        opacity: 0;
        pointer-events: none;
        z-index: 15;
    }}

    .shockwave.animate {{
        animation: blast-ring 1.3s cubic-bezier(0.1, 0.8, 0.2, 1) forwards;
    }}

    @keyframes blast-ring {{
        0% {{
            transform: translate(-50%, -50%) scale(0.1);
            opacity: 1;
            border-width: 8px;
        }}
        50% {{
            opacity: 0.9;
        }}
        100% {{
            transform: translate(-50%, -50%) scale(18);
            opacity: 0;
            border-width: 1px;
        }}
    }}

    /* Flash overlay */
    #flash-overlay {{
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: #ffffff;
        opacity: 0;
        pointer-events: none;
        z-index: 20;
        transition: opacity 0.4s ease-out;
    }}

    /* Glassmorphism Hero Container */
    #hero-container {{
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        z-index: 10;
        width: 90%;
        max-width: 860px;
        background: rgba(10, 18, 64, 0.72);
        backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px);
        border: 2px solid #26327f;
        border-radius: 20px;
        padding: 2.2rem 2.8rem;
        box-shadow: 4px 4px 0px #182276, 0 20px 60px rgba(0, 6, 33, 0.8);
        text-align: center;
        transition: all 0.6s cubic-bezier(0.16, 1, 0.3, 1);
    }}

    #hero-container.warp-active {{
        transform: translate(-50%, -50%) scale(0.92);
        filter: blur(3px) brightness(1.6);
        opacity: 0.2;
    }}

    #hero-container.post-warp {{
        transform: translate(-50%, -50%) scale(1);
        filter: none;
        opacity: 1;
        border-color: #ffe3c5;
        box-shadow: 5px 5px 0px #182276, 0 0 40px rgba(80, 108, 217, 0.5);
    }}

    .hud-badge {{
        display: inline-flex;
        align-items: center;
        gap: 0.5rem;
        background: rgba(0, 6, 33, 0.85);
        border: 1.5px solid #ffe3c5;
        border-radius: 999px;
        padding: 0.35rem 1rem;
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.75rem;
        font-weight: 700;
        color: #ffe3c5;
        margin-bottom: 1.2rem;
        box-shadow: 2px 2px 0px #182276;
    }}

    .pulse-dot {{
        width: 8px;
        height: 8px;
        border-radius: 50%;
        background: #22d974;
        box-shadow: 0 0 10px #22d974;
        animation: pulse 1.6s infinite ease-in-out;
    }}

    @keyframes pulse {{
        0%, 100% {{ transform: scale(1); opacity: 1; }}
        50% {{ transform: scale(0.7); opacity: 0.4; }}
    }}

    .hero-title {{
        font-size: 2.8rem;
        font-weight: 900;
        letter-spacing: -0.03em;
        line-height: 1.1;
        margin-bottom: 0.8rem;
        background: linear-gradient(135deg, #ffffff 0%, #ffe3c5 55%, #506cd9 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-shadow: 0 0 30px rgba(80, 108, 217, 0.4);
    }}

    .hero-subtitle {{
        font-size: 1rem;
        color: #a9b4e8;
        max-width: 620px;
        margin: 0 auto 1.8rem auto;
        line-height: 1.55;
    }}

    /* Start Warp Button */
    .btn-warp {{
        position: relative;
        display: inline-flex;
        align-items: center;
        justify-content: center;
        gap: 0.75rem;
        background: #506cd9;
        color: #ffffff;
        font-family: 'JetBrains Mono', monospace;
        font-size: 1.05rem;
        font-weight: 800;
        letter-spacing: 0.05em;
        padding: 1rem 2.5rem;
        border-radius: 999px;
        border: 2.5px solid #ffe3c5;
        box-shadow: 4px 4px 0px #182276;
        cursor: pointer;
        outline: none;
        transition: all 0.22s cubic-bezier(0.34, 1.2, 0.64, 1);
    }}

    .btn-warp:hover {{
        background: #ffe3c5;
        color: #000621;
        border-color: #ffffff;
        box-shadow: 6px 6px 0px #182276;
        transform: translate(-2px, -2px) scale(1.03);
    }}

    .btn-warp:active {{
        transform: translate(2px, 2px);
        box-shadow: 2px 2px 0px #182276;
    }}

    /* Post-warp metrics grid */
    .warp-metrics {{
        display: none;
        grid-template-columns: repeat(3, 1fr);
        gap: 1rem;
        margin-top: 1.5rem;
        text-align: left;
    }}

    .metric-chip {{
        background: rgba(0, 6, 33, 0.75);
        border: 1.5px solid #26327f;
        border-radius: 10px;
        padding: 0.75rem 1rem;
        box-shadow: 2px 2px 0px #182276;
    }}

    .metric-label {{
        font-size: 0.68rem;
        color: #a9b4e8;
        text-transform: uppercase;
        font-weight: 700;
        letter-spacing: 0.08em;
    }}

    .metric-val {{
        font-family: 'JetBrains Mono', monospace;
        font-size: 1.3rem;
        font-weight: 900;
        color: #22d974;
        margin-top: 0.2rem;
    }}

    /* Screen shake */
    @keyframes screen-shake {{
        0% {{ transform: translate(0, 0); }}
        20% {{ transform: translate(-8px, 6px); }}
        40% {{ transform: translate(7px, -5px); }}
        60% {{ transform: translate(-5px, -4px); }}
        80% {{ transform: translate(4px, 5px); }}
        100% {{ transform: translate(0, 0); }}
    }}

    .shake {{
        animation: screen-shake 0.8s ease-in-out;
    }}
</style>
</head>
<body>

<canvas id="space-canvas"></canvas>
<div class="shockwave" id="shockwave"></div>
<div id="flash-overlay"></div>

<div id="hero-container">
    <div class="hud-badge">
        <span class="pulse-dot"></span>
        <span id="hud-text">BANGALORE OBSERVATION STATION // NODE #01</span>
    </div>
    
    <h1 class="hero-title" id="hero-title">ROAD TO MILKY WAY</h1>
    <p class="hero-subtitle" id="hero-subtitle">
        Next-generation multimodal media intelligence platform. Audits AI-generated landscapes,
        neural text manipulation, voice synthesis, and zero-face video deepfakes at warp speed.
    </p>

    <div id="warp-action-box">
        <button class="btn-warp" id="btn-warp" onclick="initiateHyperspaceJump()">
            <span>⚡ INITIATE WARP SPEED // START</span>
        </button>
    </div>

    <div class="warp-metrics" id="warp-metrics">
        <div class="metric-chip">
            <div class="metric-label">WARP FACTOR</div>
            <div class="metric-val" id="val-warp">9.88 c</div>
        </div>
        <div class="metric-chip">
            <div class="metric-label">SENSOR FIDELITY</div>
            <div class="metric-val" id="val-sens">99.98%</div>
        </div>
        <div class="metric-chip">
            <div class="metric-label">ORBITAL TARGET</div>
            <div class="metric-val" style="color: #ffe3c5;">BANGALORE // IN</div>
        </div>
    </div>
</div>

<script>
    const canvas = document.getElementById('space-canvas');
    const ctx = canvas.getContext('2d');
    const hero = document.getElementById('hero-container');
    const shockwave = document.getElementById('shockwave');
    const flash = document.getElementById('flash-overlay');
    const btnWarp = document.getElementById('btn-warp');
    const warpMetrics = document.getElementById('warp-metrics');
    const heroTitle = document.getElementById('hero-title');
    const heroSubtitle = document.getElementById('hero-subtitle');
    const hudText = document.getElementById('hud-text');

    let w, h, cx, cy;
    let stars = [];
    const NUM_STARS = 450;
    let speed = 1.2;
    let targetSpeed = 1.2;
    let isWarping = false;
    let warpComplete = false;
    let mouseX = 0, mouseY = 0;

    function resize() {{
        w = canvas.width = window.innerWidth;
        h = canvas.height = window.innerHeight;
        cx = w / 2;
        cy = h / 2;
    }}
    window.addEventListener('resize', resize);
    resize();

    window.addEventListener('mousemove', (e) => {{
        mouseX = (e.clientX - cx) * 0.05;
        mouseY = (e.clientY - cy) * 0.05;
    }});

    // Initialize stars with 3D depth
    for (let i = 0; i < NUM_STARS; i++) {{
        stars.push({{
            x: (Math.random() - 0.5) * w * 2,
            y: (Math.random() - 0.5) * h * 2,
            z: Math.random() * w,
            pz: Math.random() * w,
            color: Math.random() > 0.8 ? '#ffe3c5' : (Math.random() > 0.5 ? '#506cd9' : (Math.random() > 0.3 ? '#22d974' : '#ffffff'))
        }});
    }}

    // Web Audio Hyperspace Sound Synthesizer
    function playWarpAudio() {{
        try {{
            const AudioContext = window.AudioContext || window.webkitAudioContext;
            if (!AudioContext) return;
            const actx = new AudioContext();

            // 1. Sub-bass resonance sweep
            const oscSub = actx.createOscillator();
            const gainSub = actx.createGain();
            oscSub.type = 'sine';
            oscSub.frequency.setValueAtTime(90, actx.currentTime);
            oscSub.frequency.exponentialRampToValueAtTime(32, actx.currentTime + 1.4);
            gainSub.gain.setValueAtTime(0.5, actx.currentTime);
            gainSub.gain.exponentialRampToValueAtTime(0.01, actx.currentTime + 1.4);
            oscSub.connect(gainSub);
            gainSub.connect(actx.destination);
            oscSub.start();
            oscSub.stop(actx.currentTime + 1.4);

            // 2. High-frequency laser warp rise
            const oscLaser = actx.createOscillator();
            const gainLaser = actx.createGain();
            oscLaser.type = 'sawtooth';
            oscLaser.frequency.setValueAtTime(140, actx.currentTime);
            oscLaser.frequency.exponentialRampToValueAtTime(880, actx.currentTime + 0.8);
            oscLaser.frequency.exponentialRampToValueAtTime(220, actx.currentTime + 1.5);
            gainLaser.gain.setValueAtTime(0.2, actx.currentTime);
            gainLaser.gain.exponentialRampToValueAtTime(0.001, actx.currentTime + 1.5);
            oscLaser.connect(gainLaser);
            gainLaser.connect(actx.destination);
            oscLaser.start();
            oscLaser.stop(actx.currentTime + 1.5);

            // 3. Noise burst
            const bufferSize = actx.sampleRate * 1.0;
            const noiseBuffer = actx.createBuffer(1, bufferSize, actx.sampleRate);
            const output = noiseBuffer.getChannelData(0);
            for (let i = 0; i < bufferSize; i++) {{
                output[i] = Math.random() * 2 - 1;
            }}
            const whiteNoise = actx.createBufferSource();
            whiteNoise.buffer = noiseBuffer;
            const filter = actx.createBiquadFilter();
            filter.type = 'bandpass';
            filter.frequency.setValueAtTime(600, actx.currentTime);
            filter.frequency.exponentialRampToValueAtTime(1600, actx.currentTime + 0.5);
            const gainNoise = actx.createGain();
            gainNoise.gain.setValueAtTime(0.3, actx.currentTime);
            gainNoise.gain.exponentialRampToValueAtTime(0.01, actx.currentTime + 0.9);
            whiteNoise.connect(filter);
            filter.connect(gainNoise);
            gainNoise.connect(actx.destination);
            whiteNoise.start();
            whiteNoise.stop(actx.currentTime + 1.0);
        }} catch(e) {{
            console.log('Audio init skipped', e);
        }}
    }}

    function initiateHyperspaceJump() {{
        if (isWarping) return;
        isWarping = true;
        playWarpAudio();

        // 1. Ramp star velocity to hyperspace
        targetSpeed = 55.0;

        // 2. Animate hero blur
        hero.classList.add('warp-active');

        // 3. Shockwave blast
        shockwave.classList.remove('animate');
        void shockwave.offsetWidth;
        shockwave.classList.add('animate');

        // 4. Camera shake
        document.body.classList.add('shake');

        // 5. Whiteout flash at peak
        setTimeout(() => {{
            flash.style.opacity = '0.85';
            setTimeout(() => {{
                flash.style.opacity = '0';
            }}, 350);
        }}, 700);

        // 6. Settle into post-warp station orbit
        setTimeout(() => {{
            targetSpeed = 2.4;
            document.body.classList.remove('shake');
            hero.classList.remove('warp-active');
            hero.classList.add('post-warp');

            // Update contents
            hudText.innerHTML = "WARP EXPEDITION COMPLETED // ORBIT REACHED";
            heroTitle.innerHTML = "BANGALORE MILKY WAY NODE";
            heroSubtitle.innerHTML = "Hyperspace navigation verified. Multimodal intelligence telemetry active. Scroll down for forensic timeline, global threat radar, and live neural decoders.";
            
            warpMetrics.style.display = 'grid';
            btnWarp.innerHTML = "<span>🚀 RE-ENGAGE HYPERSPACE WARP</span>";
            isWarping = false;
            warpComplete = true;
        }}, 1400);
    }}

    // Animation loop
    function render() {{
        // Smooth speed interpolation
        speed += (targetSpeed - speed) * 0.08;

        // Clear canvas with trail blur during warp
        ctx.fillStyle = isWarping ? 'rgba(0, 6, 33, 0.35)' : 'rgba(0, 6, 33, 0.75)';
        ctx.fillRect(0, 0, w, h);

        const currentCx = cx + mouseX;
        const currentCy = cy + mouseY;

        for (let i = 0; i < NUM_STARS; i++) {{
            let s = stars[i];
            s.pz = s.z;
            s.z -= speed;

            if (s.z <= 0) {{
                s.z = w;
                s.pz = w;
                s.x = (Math.random() - 0.5) * w * 2;
                s.y = (Math.random() - 0.5) * h * 2;
            }}

            const k = 220 / s.z;
            const px = s.x * k + currentCx;
            const py = s.y * k + currentCy;

            const pk = 220 / s.pz;
            const ppx = s.x * pk + currentCx;
            const ppy = s.y * pk + currentCy;

            if (px >= 0 && px < w && py >= 0 && py < h) {{
                const size = Math.max(0.8, (1 - s.z / w) * 3.5);
                ctx.beginPath();
                if (speed > 10) {{
                    // Hyperspace velocity streaks
                    ctx.moveTo(ppx, ppy);
                    ctx.lineTo(px, py);
                    ctx.lineWidth = Math.min(size * 1.5, 4);
                    ctx.strokeStyle = s.color;
                    ctx.stroke();
                }} else {{
                    // Normal point stars
                    ctx.arc(px, py, size, 0, Math.PI * 2);
                    ctx.fillStyle = s.color;
                    ctx.fill();
                }}
            }}
        }}

        requestAnimationFrame(render);
    }}

    render();
</script>
</body>
</html>
    """
