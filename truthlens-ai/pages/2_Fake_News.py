"""
TruthLens AI - Fake News Text Intelligence (Road to Milky Way Theme)
Classifies news articles and narrative claims using fine-tuned NLP models and LIME explainability.
"""

import streamlit as st
import sys
import os
import plotly.graph_objects as go

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

st.set_page_config(
    page_title="Fake News Detection | TruthLens AI",
    page_icon="📝",
    layout="wide",
    initial_sidebar_state="expanded"
)

from ui_common import load_custom_css, render_sidebar_telemetry, render_header, render_html
from models.text_detector import get_text_detector
from evaluation.lime_explainer import TextLimeExplainer
from database.db import insert_analysis

load_custom_css()
render_sidebar_telemetry()

render_header(
    title="TEXT FORENSICS // MISINFORMATION ENGINE",
    subtitle="Semantic and linguistic attribution to evaluate news credibility and sensationalism",
    badge_text="NLP ENGINE READY",
    badge_type="info"
)

# Sample texts for quick hackathon evaluation
SAMPLE_TEXTS = {
    "Real: Fed Interest Rates": (
        "The Federal Reserve held benchmark interest rates steady following a two-day policy meeting, "
        "signaling that inflation has continued to moderate toward its two percent annual target while "
        "the labor market remains resilient. Chairman Jerome Powell stated that future policy moves "
        "will depend entirely on incoming economic data and labor reports."
    ),
    "Real: James Webb Discovery": (
        "NASA's James Webb Space Telescope has captured detailed spectroscopic data of an exoplanet's atmosphere, "
        "identifying water vapor, sulfur dioxide, and silicate clouds in unprecedented clarity. "
        "The scientific findings were published after rigorous peer review in the Astrophysical Journal."
    ),
    "Fake: Antarctica Retinal Reset": (
        "ALERT: Secret globalist meeting in Antarctica decided that all paper currency will be banned "
        "this Friday and replaced with mandatory retinal scan digital IDs or you will permanently lose "
        "access to your home and food supplies! Spread this urgent truth before it is erased!"
    ),
    "Fake: Synthetic Clones Tribunal": (
        "SHOCKING SECRET: Classified military tribunal documents prove all major world leaders have been "
        "secretly executed and replaced by synthetic biological clones that recharge in deep underground "
        "bunkers during solar eclipses! The mainstream media refuses to broadcast the leaked files!"
    )
}

render_html("""
    <div style="font-size: 0.82rem; font-weight: 800; color: #ffe3c5; letter-spacing: 0.08em; text-transform: uppercase; margin-bottom: 0.4rem;">
        Load Verified Benchmark Samples
    </div>
""")

btn_cols = st.columns(4)
selected_sample = None
for idx, (label, sample_text) in enumerate(SAMPLE_TEXTS.items()):
    with btn_cols[idx]:
        if st.button(label, key=f"sample_{idx}", use_container_width=True):
            st.session_state["text_input_area"] = sample_text

current_val = st.session_state.get("text_input_area", "")
text_input = st.text_area(
    "News Article / Narrative Text",
    value=current_val,
    height=160,
    placeholder="Paste news headline, full article excerpt, or narrative claim here...",
    help="Enter at least 15 words for reliable linguistic and attribution analysis."
)

c_left, c_right = st.columns([1, 4])
with c_left:
    analyze_clicked = st.button("⚡ Run Forensic Analysis", key="btn_run_text", use_container_width=True)

if analyze_clicked:
    if not text_input or len(text_input.strip().split()) < 5:
        st.error("Input validation failed: Please enter a meaningful news article with at least 5 words.")
    else:
        with st.spinner("Executing neural semantic inspection and calculating token attributions..."):
            detector = get_text_detector()
            res = detector.analyze(text_input)

            if not res.get("success"):
                st.error(f"Analysis failed: {res.get('error', 'Unknown error')}")
            else:
                pred = res["prediction"]
                conf = res["confidence"]
                probs = res["probabilities"]
                model_name = res["model_name"]
                status_msg = res["status_message"]

                # Log into SQLite DB
                tracking_code = insert_analysis(
                    media_type="Text",
                    content_summary=text_input[:200],
                    model_name=model_name,
                    prediction=pred,
                    confidence=conf,
                    status="COMPLETED",
                    metadata={
                        "probabilities": probs,
                        "engine_status": status_msg
                    }
                )

                render_html("<div style='height: 1rem;'></div>")

                # --- RESULTS CARDS ---
                r1, r2, r3 = st.columns([1.2, 1, 1.2])

                with r1:
                    is_fake = "FAKE" in pred
                    badge_style = "border-left: 5px solid #d13f30;" if is_fake else "border-left: 5px solid #22d974;"
                    pred_color = "#d13f30" if is_fake else "#22d974"
                    render_html(f"""
                        <div class="cyber-card" style="{badge_style}">
                            <div style="font-size: 0.72rem; color: #a9b4e8; text-transform: uppercase; font-weight: 700; letter-spacing: 0.08em;">
                                Forensic Classification
                            </div>
                            <div style="font-size: 1.6rem; font-weight: 900; color: {pred_color}; margin: 0.3rem 0; font-family: 'JetBrains Mono', monospace;">
                                {pred}
                            </div>
                            <div style="font-size: 0.75rem; color: #a9b4e8;">
                                Tracking ID: <span style="color: #ffe3c5; font-family: 'JetBrains Mono', monospace; font-weight: 700;">{tracking_code}</span>
                            </div>
                        </div>
                    """)

                with r2:
                    render_html(f"""
                        <div class="cyber-card">
                            <div style="font-size: 0.72rem; color: #a9b4e8; text-transform: uppercase; font-weight: 700; letter-spacing: 0.08em;">
                                Model Confidence
                            </div>
                            <div style="font-size: 1.6rem; font-weight: 900; color: #FFFFFF; margin: 0.3rem 0; font-family: 'JetBrains Mono', monospace;">
                                {conf * 100:.1f}%
                            </div>
                            <div style="font-size: 0.75rem; color: #a9b4e8;">
                                Softmax probability margin
                            </div>
                        </div>
                    """)

                with r3:
                    render_html(f"""
                        <div class="cyber-card">
                            <div style="font-size: 0.72rem; color: #a9b4e8; text-transform: uppercase; font-weight: 700; letter-spacing: 0.08em;">
                                Active Forensic Engine
                            </div>
                            <div style="font-size: 0.95rem; font-weight: 800; color: #ffe3c5; margin: 0.4rem 0;">
                                {model_name}
                            </div>
                            <div style="font-size: 0.72rem; color: #a9b4e8;">
                                {status_msg}
                            </div>
                        </div>
                    """)

                # Class probabilities breakdown bar
                render_html("""
                    <div style="font-size: 0.82rem; font-weight: 800; color: #ffe3c5; letter-spacing: 0.08em; text-transform: uppercase; margin: 0.75rem 0 0.4rem 0;">
                        Class Probability Spectrum
                    </div>
                """)

                fig_prob = go.Figure()
                fig_prob.add_trace(go.Bar(
                    y=["Classification"],
                    x=[probs["REAL"] * 100],
                    name="Authentic / Real",
                    orientation="h",
                    marker=dict(color="#22d974"),
                    text=[f"REAL: {probs['REAL']*100:.1f}%"],
                    textposition="inside"
                ))
                fig_prob.add_trace(go.Bar(
                    y=["Classification"],
                    x=[probs["POTENTIALLY FAKE"] * 100],
                    name="Potentially Fake",
                    orientation="h",
                    marker=dict(color="#d13f30"),
                    text=[f"POTENTIALLY FAKE: {probs['POTENTIALLY FAKE']*100:.1f}%"],
                    textposition="inside"
                ))
                fig_prob.update_layout(
                    barmode="stack",
                    paper_bgcolor="rgba(0,0,0,0)",
                    plot_bgcolor="rgba(0,0,0,0)",
                    font=dict(color="#ffe3c5", family="Inter"),
                    margin=dict(l=10, r=10, t=10, b=10),
                    height=80,
                    showlegend=True,
                    xaxis=dict(showgrid=False, range=[0, 100]),
                    yaxis=dict(showticklabels=False)
                )
                st.plotly_chart(fig_prob, use_container_width=True)

                # --- EXPLAINABLE AI (LIME) ---
                render_html("<div style='height: 1rem;'></div>")
                render_html("""
                    <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 0.5rem;">
                        <span style="font-size: 0.82rem; font-weight: 800; color: #ffe3c5; letter-spacing: 0.08em; text-transform: uppercase;">
                            🧠 Explainable AI: Token Attribution (LIME)
                        </span>
                        <span class="badge-info">LOCAL ATTRIBUTION</span>
                    </div>
                """)

                with st.spinner("Generating LIME local surrogate explanations..."):
                    explainer = TextLimeExplainer()
                    lime_res = explainer.explain(text_input, detector.predict_proba, num_features=10)

                    if lime_res["available"] and lime_res["features"]:
                        features = lime_res["features"]
                        
                        col_lime1, col_lime2 = st.columns([1.5, 1])
                        
                        with col_lime1:
                            words = [f["word"] for f in features]
                            weights = [f["weight"] for f in features]
                            colors = ["#d13f30" if w > 0 else "#22d974" for w in weights]
                            
                            fig_lime = go.Figure(go.Bar(
                                x=weights,
                                y=words,
                                orientation="h",
                                marker_color=colors,
                                text=[f"{w:+.3f}" for w in weights],
                                textposition="auto"
                            ))
                            fig_lime.update_layout(
                                paper_bgcolor="rgba(0,0,0,0)",
                                plot_bgcolor="rgba(0,0,0,0)",
                                font=dict(color="#ffe3c5", family="Inter"),
                                margin=dict(l=20, r=20, t=20, b=20),
                                height=260,
                                yaxis=dict(autorange="reversed", gridcolor="rgba(38, 50, 127, 0.35)"),
                                xaxis=dict(title="Attribution Weight (Red: Fake, Green: Real)", gridcolor="rgba(38, 50, 127, 0.35)")
                            )
                            st.plotly_chart(fig_lime, use_container_width=True)

                        with col_lime2:
                            render_html("""
                                <div class="cyber-card" style="height: 260px; overflow-y: auto;">
                                    <div style="font-weight: 800; color: #ffe3c5; font-size: 0.85rem; margin-bottom: 0.4rem;">
                                        Token Weight Ledger
                                    </div>
                                    <div style="font-size: 0.72rem; color: #a9b4e8; margin-bottom: 0.6rem;">
                                        Positive weights increase probability of misleading classification.
                                    </div>
                            """)
                            for f in features:
                                is_pos = f["weight"] > 0
                                w_col = "#d13f30" if is_pos else "#22d974"
                                render_html(f"""
                                    <div style="display: flex; justify-content: space-between; padding: 0.25rem 0; border-bottom: 1px solid #141d5a; font-family: 'JetBrains Mono', monospace; font-size: 0.72rem;">
                                        <span style="color: #FFFFFF;">{f['word']}</span>
                                        <span style="color: {w_col}; font-weight: 700;">{f['weight']:+.4f}</span>
                                    </div>
                                """)
                            render_html("</div>")
                    else:
                        st.info("LIME surrogate explanation unavailable or could not generate sufficient feature perturbances for this short text sample.")

                # Transparent methodology disclaimer
                render_html("""
                    <div style="background: #0a1240; border: 2px solid #26327f; border-radius: 10px; padding: 0.85rem 1.15rem; margin-top: 1rem; font-size: 0.75rem; color: #a9b4e8; line-height: 1.5; box-shadow: 3px 3px 0px #182276;">
                        <span style="color: #ffe3c5; font-weight: 800;">AUDIT PROTOCOL NOTICE:</span> This engine detects lexical patterns, clickbait grammar, sensationalist rhetoric, and narrative indicators common in deceptive reporting. It is an assistive AI tool and does not replace human investigative journalism or factual ground-truth verification.
                    </div>
                """)
