"""
TruthLens AI - AI-Generated Image Forensics (Road to Milky Way Theme)
Analyzes still photographs and artwork for generative AI artifacts (Midjourney, DALL-E, Stable Diffusion).
"""

import streamlit as st
import sys
import os
import plotly.graph_objects as go
from PIL import Image

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

st.set_page_config(
    page_title="AI Image Detection | TruthLens AI",
    page_icon="🖼️",
    layout="wide",
    initial_sidebar_state="expanded"
)

from ui_common import load_custom_css, render_sidebar_telemetry, render_header, render_html
from processing.image_processor import load_image_for_analysis
from models.image_detector import get_image_detector
from database.db import insert_analysis

load_custom_css()
render_sidebar_telemetry()

render_header(
    title="IMAGE FORENSICS // SYNTHETIC VISION ENGINE",
    subtitle="Detect generative diffusion, latent GAN synthesis, and digital photomanipulation",
    badge_text="VISION TRANSFORMER",
    badge_type="info"
)

uploaded_file = st.file_uploader(
    "Upload Media File (JPG, JPEG, PNG)",
    type=["jpg", "jpeg", "png"],
    help="Maximum upload size: 20MB. High-resolution uncompressed formats yield optimal forensic fidelity."
)

if uploaded_file:
    pil_img, metadata, msg = load_image_for_analysis(uploaded_file)
    
    if pil_img is None:
        st.error(f"Image validation error: {msg}")
    else:
        col_img, col_forensics = st.columns([1.1, 1.4])
        
        with col_img:
            st.image(pil_img, caption=f"Uploaded Asset: {metadata['filename']} ({metadata['dimensions']})", use_container_width=True)
            
            # Metadata panel
            render_html(f"""
                <div class="terminal-box" style="margin-top: 0.6rem;">
                    [ASSET AUDIT METADATA]<br/>
                    • Dimensions: {metadata['dimensions']}<br/>
                    • Color Mode: {metadata['mode']}<br/>
                    • Payload Size: {metadata['filesize_kb']} KB<br/>
                    • Format: {metadata['format']}
                </div>
            """)

        with col_forensics:
            render_html("""
                <div style="font-size: 0.82rem; font-weight: 800; color: #ffe3c5; letter-spacing: 0.08em; text-transform: uppercase; margin-bottom: 0.5rem;">
                    Forensic Inspection Controls
                </div>
            """)
            
            if st.button("⚡ Inspect Synthetic Signatures", key="btn_run_image", use_container_width=True):
                with st.spinner("Executing neural latent-artifact classification..."):
                    detector = get_image_detector()
                    res = detector.analyze(pil_img)

                    if not res.get("success"):
                        render_html(f"""
                            <div class="cyber-card" style="border-left: 5px solid #ead11f;">
                                <div style="font-weight: 800; color: #ead11f; font-size: 1rem; margin-bottom: 0.3rem;">
                                    ⚠️ {res.get('status', 'ANALYSIS_HALTED')}
                                </div>
                                <div style="font-size: 0.82rem; color: #F0F4F8; line-height: 1.5;">
                                    {res.get('error', 'The synthetic vision detector is not active.')}
                                </div>
                                <div style="font-size: 0.75rem; color: #a9b4e8; margin-top: 0.5rem;">
                                    {res.get('disclaimer', '')}
                                </div>
                            </div>
                        """)
                    else:
                        pred = res["prediction"]
                        conf = res["confidence"]
                        probs = res["probabilities"]
                        model_name = res["model_name"]
                        device = res["device"]

                        # Insert into SQLite Database
                        tracking_code = insert_analysis(
                            media_type="Image",
                            content_summary=f"{metadata['filename']} ({metadata['dimensions']})",
                            model_name=model_name,
                            prediction=pred,
                            confidence=conf,
                            status="COMPLETED",
                            metadata={
                                "probabilities": probs,
                                "device": device,
                                "image_metadata": metadata
                            }
                        )

                        is_synthetic = "SYNTHETIC" in pred
                        pred_color = "#d13f30" if is_synthetic else "#22d974"
                        badge_border = "border-left: 5px solid #d13f30;" if is_synthetic else "border-left: 5px solid #22d974;"

                        render_html(f"""
                            <div class="cyber-card" style="{badge_border}">
                                <div style="font-size: 0.72rem; color: #a9b4e8; text-transform: uppercase; font-weight: 700; letter-spacing: 0.08em;">
                                    Synthetic Vision Verdict
                                </div>
                                <div style="font-size: 1.7rem; font-weight: 900; color: {pred_color}; margin: 0.3rem 0; font-family: 'JetBrains Mono', monospace;">
                                    {pred}
                                </div>
                                <div style="display: flex; justify-content: space-between; font-size: 0.75rem; color: #a9b4e8;">
                                    <span>Tracking Code: <b style="color: #ffe3c5; font-family: 'JetBrains Mono', monospace;">{tracking_code}</b></span>
                                    <span>Device: <b style="color: #FFFFFF;">{device}</b></span>
                                </div>
                            </div>
                        """)

                        # Metric Cards
                        m1, m2 = st.columns(2)
                        with m1:
                            render_html(f"""
                                <div class="stat-card">
                                    <div class="stat-label">Confidence</div>
                                    <div class="stat-value">{conf*100:.1f}%</div>
                                    <div class="stat-footer">Model certainty</div>
                                </div>
                            """)
                        with m2:
                            render_html(f"""
                                <div class="stat-card">
                                    <div class="stat-label">Model Target</div>
                                    <div class="stat-value" style="font-size: 1.05rem; color: #ffe3c5; word-break: break-all;">
                                        {model_name}
                                    </div>
                                    <div class="stat-footer">Vision Transformer</div>
                                </div>
                            """)

                        # Probability Distribution Bar
                        render_html("<div style='height: 0.8rem;'></div>")
                        render_html("""
                            <div style="font-size: 0.8rem; font-weight: 800; color: #ffe3c5; letter-spacing: 0.08em; text-transform: uppercase; margin-bottom: 0.3rem;">
                                Generative Probability Spectrum
                            </div>
                        """)

                        fig_prob = go.Figure()
                        fig_prob.add_trace(go.Bar(
                            y=["Probabilities"],
                            x=[probs["AUTHENTIC"] * 100],
                            name="Authentic / Real",
                            orientation="h",
                            marker=dict(color="#22d974"),
                            text=[f"AUTHENTIC: {probs['AUTHENTIC']*100:.1f}%"],
                            textposition="inside"
                        ))
                        fig_prob.add_trace(go.Bar(
                            y=["Probabilities"],
                            x=[probs["SYNTHETIC"] * 100],
                            name="AI Generated",
                            orientation="h",
                            marker=dict(color="#d13f30"),
                            text=[f"SYNTHETIC: {probs['SYNTHETIC']*100:.1f}%"],
                            textposition="inside"
                        ))
                        fig_prob.update_layout(
                            barmode="stack",
                            paper_bgcolor="rgba(0,0,0,0)",
                            plot_bgcolor="rgba(0,0,0,0)",
                            font=dict(color="#ffe3c5", family="Inter"),
                            margin=dict(l=10, r=10, t=10, b=10),
                            height=75,
                            showlegend=True,
                            xaxis=dict(showgrid=False, range=[0, 100]),
                            yaxis=dict(showticklabels=False)
                        )
                        st.plotly_chart(fig_prob, use_container_width=True)

                        # Disclaimer
                        render_html(f"""
                            <div style="background: #0a1240; border: 2px solid #26327f; border-radius: 10px; padding: 0.85rem 1.15rem; margin-top: 1rem; font-size: 0.75rem; color: #a9b4e8; line-height: 1.5; box-shadow: 3px 3px 0px #182276;">
                                <span style="color: #ffe3c5; font-weight: 800;">LIMITATION DISCLOSURE:</span> {res['disclaimer']}
                            </div>
                        """)
else:
    render_html("""
        <div class="cyber-card" style="text-align: center; padding: 3.5rem 2rem;">
            <div style="font-size: 2.5rem; margin-bottom: 0.8rem;">🖼️</div>
            <div style="font-size: 1.15rem; font-weight: 800; color: #FFFFFF;">Drag & Drop Image for Media Forensic Ingestion</div>
            <div style="font-size: 0.82rem; color: #a9b4e8; max-width: 500px; margin: 0.5rem auto 0 auto; line-height: 1.5;">
                Upload suspect photos, social media imagery, or photorealistic art to test against latent diffusion patterns and generative GAN signatures.
            </div>
        </div>
    """)
