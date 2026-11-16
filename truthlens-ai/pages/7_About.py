"""
TruthLens AI - System Architecture, Threat Modeling & Forensics Guide
Comprehensive documentation on architecture, algorithmic integrity, ethics, and operational methodology.
"""

import streamlit as st
import sys
import os

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

st.set_page_config(
    page_title="About System | TruthLens AI",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

from ui_common import load_custom_css, render_sidebar_telemetry, render_header, render_html

load_custom_css()
render_sidebar_telemetry()

render_header(
    title="SYSTEM INTELLIGENCE // ARCHITECTURAL DOSSIER",
    subtitle="Engineering specification, threat surface analysis, and ethical operational boundaries",
    badge_text="SPECIFICATION v1.0",
    badge_type="info"
)

col_doc1, col_doc2 = st.columns([1.4, 1])

with col_doc1:
    render_html("""
        <div class="cyber-card">
            <div style="font-size: 1.1rem; font-weight: 800; color: #FFFFFF; margin-bottom: 0.5rem;">
                TruthLens AI: Multimodal Defense Platform
            </div>
            <div style="font-size: 0.85rem; color: #8BA2C1; line-height: 1.6;">
                In an era dominated by rapid generative AI proliferation, adversarial disinformation campaigns exploit 
                cross-modal channels simultaneously: synthetic narratives, hyperrealistic generated imagery, and 
                deepfake facial manipulation. TruthLens AI provides a unified media intelligence command center 
                built in pure Python to triage, inspect, and evaluate suspect assets across all three modalities.
            </div>
        </div>

        <div class="cyber-card">
            <div style="font-size: 1rem; font-weight: 700; color: #38D9FF; margin-bottom: 0.5rem;">
                Forensic Pipeline Architecture
            </div>
            <div style="font-size: 0.82rem; color: #8BA2C1; line-height: 1.6;">
                <b>1. NLP Misinformation Engine:</b> Evaluates textual assertions using fine-tuned sequence classification 
                transformers paired with an auditable TF-IDF Logistic Regression baseline trained on benchmark datasets. 
                Explainability is provided via <i>Local Interpretable Model-agnostic Explanations (LIME)</i>.<br/><br/>
                <b>2. Synthetic Image Engine:</b> Leverages Vision Transformers (ViT) to scrutinize spatial artifacts, 
                structural inconsistencies, and generative synthesis markers without resorting to ungrounded heuristics.<br/><br/>
                <b>3. Facial Deepfake & Video Engine:</b> Uses OpenCV to extract temporal frames, isolates face crops, 
                and inspects boundary warping and face-swap signatures via the FaceForensics++ XceptionNet pipeline.<br/><br/>
                <b>4. Forensic Audit Vault:</b> SQLite database ledger persisting metadata, confidence ratings, and timestamps 
                while immediately releasing raw media payloads to protect privacy.
            </div>
        </div>

        <div class="cyber-card">
            <div style="font-size: 1rem; font-weight: 700; color: #FF454F; margin-bottom: 0.5rem;">
                Ethical Disclaimers & Operational Limits
            </div>
            <div style="font-size: 0.82rem; color: #8BA2C1; line-height: 1.6;">
                • <b>No Absolute Truth Claims:</b> TruthLens AI detects statistical and linguistic anomalies learned from 
                curated training sets. It does not replace investigative journalism, primary source verification, or 
                human critical analysis.<br/>
                • <b>No Groundless Predictions:</b> If an AI checkpoint or face is missing, the system transparently 
                discloses the unconfigured status rather than fabricating predictions.<br/>
                • <b>Adversarial Robustness:</b> Compression, re-encoding, low-light imagery, and novel generative models 
                can degrade confidence. Results should be interpreted as diagnostic signals, not unilateral verdicts.
            </div>
        </div>
    """)

with col_doc2:
    render_html("""
        <div class="cyber-card">
            <div style="font-size: 0.95rem; font-weight: 700; color: #19D69B; margin-bottom: 0.5rem;">
                Technology Stack Specifications
            </div>
            <div style="font-size: 0.8rem; color: #8BA2C1; line-height: 1.5; font-family: 'JetBrains Mono', monospace;">
                • Python: 3.11 Runtime<br/>
                • Frontend: Streamlit (Custom Cyber CSS)<br/>
                • Deep Learning: PyTorch + CUDA/CPU<br/>
                • NLP Models: Hugging Face Transformers<br/>
                • Explainability: LIME (Local Surrogates)<br/>
                • Computer Vision: OpenCV (Haar / YuNet)<br/>
                • Deepfake Arch: XceptionNet (FF++)<br/>
                • Evaluation: Scikit-learn Suite<br/>
                • Visualization: Plotly Interactive<br/>
                • Database: SQLite WAL Persistent
            </div>
        </div>

        <div class="cyber-card">
            <div style="font-size: 0.95rem; font-weight: 700; color: #38D9FF; margin-bottom: 0.5rem;">
                Privacy & Data Security Model
            </div>
            <div style="font-size: 0.8rem; color: #8BA2C1; line-height: 1.5;">
                • <b>Zero-Persistence Raw Media:</b> Video frames and uploaded images are processed in-memory or 
                in secure temporary OS files that are wiped upon completion.<br/>
                • <b>Metadata-Only Logging:</b> Only sanitized summaries and forensic confidence scores are committed 
                to SQLite history.<br/>
                • <b>Local Inference:</b> Models run entirely on host hardware without external data telemetry leaks.
            </div>
        </div>

        <div class="terminal-box" style="margin-top: 0.8rem;">
            [COMMAND CENTER STATUS]<br/>
            STATUS: NOMINAL<br/>
            BUILD: 2026.11-RELEASE<br/>
            INTEGRITY AUDIT: PASSED
        </div>
    """)
