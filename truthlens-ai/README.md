# TRUTHLENS AI — Multimodal Media Intelligence & Cybersecurity Platform
### Real-Time Threat Intelligence, Universal AI Video Forensics & Deepfake Detection

TruthLens AI is an enterprise-grade multimodal media intelligence and forensics platform designed to detect, analyze, and catalog synthetic digital media and misinformation. Built with a high-performance **CyberShield AI Security Operations Center (SOC)** interface, TruthLens delivers real-time threat intelligence, explainable NLP misinformation detection, Vision Transformer synthetic image classification, and universal zero-face video forensics.

---

## 🌟 Key Capabilities & Architecture

### 1. CyberShield AI Command Center (`pages/1_Dashboard.py`)
- **Real-Time Threat Overview**: Live attack submissions telemetry with gradient sparkline charts and percentage trends.
- **Active Threats Severity Donut**: Multi-segment breakdown tracking Critical, High, Medium, and Low severity events.
- **Live Threat Activity Feed**: Real-time event ticker tracking ransomware, deepfakes, phishing narratives, and malicious connection attempts.
- **Interactive Global Threat Map**: Dotted matrix world map with live animated laser attack arcs, pulsing threat epicenters, and radiating circuit traces.
- **Central Rotating HUD Shield**: Concentric circular rings with radar sweep and real-time telemetry: `SYSTEM PROTECTED // AI THREAT DETECTION ACTIVE`.
- **Holographic 3D Neural Engine**: Canvas-rendered 3D rotating brain model with a horizontal cyan laser scanner sweep and real-time engine health telemetry.
- **Top Attack Vectors & Security Compliance**: Progress bars across Malware, Phishing, Exploits, Unauthorized Access, and 4 circular compliance dials (`ISO 27001`, `SOC 2`, `GDPR`, `HIPAA`).
- **Interactive Hyperspace Sensory Dive Portal**: Embedded 3D particle vortex and audio synthesizer transition module.

### 2. Fake News Text Intelligence (`pages/2_Fake_News.py`)
- **Transformer & Baseline NLP Engines**: Sequence classification via Hugging Face Transformers alongside an auditable TF-IDF Logistic Regression offline baseline.
- **Explainable AI (LIME)**: Local token attribution computing which specific words and phrases drove classification towards fake or authentic patterns.
- **Probability Spectrum**: Calibrated confidence visualization across authentic and deceptive linguistic patterns.

### 3. AI-Generated Image Forensics (`pages/3_AI_Image.py`)
- **Generative Synthesis Detection**: Detects artifacts from Midjourney, Stable Diffusion, DALL-E, and Imagen.
- **Vision Transformers (ViT)**: Fine-tuned patch-based latent inspection.
- **Payload & Metadata Extraction**: Forensic analysis of dimensions, color channels, and EXIF headers.

### 4. Universal AI Video Forensics (`pages/4_Deepfake_Video.py`)
- **Zero-Face Multi-Category Detection**: Unlike conventional facial deepfake tools, TruthLens AI analyzes videos even when **NO human face** is present:
  1. *Face Deepfakes*: Face swapping, reenactment, synthetic facial generation.
  2. *Fully AI-Generated Videos*: AI landscapes, architecture, synthetic nature, and cities.
  3. *AI-Generated Synthetic Humans*: Full-body synthetic human motion and synthetic avatars.
  4. *AI-Generated Animation*: Stylized synthesis, 3D CGI characters, synthetic cartoons.
  5. *AI-Manipulated Videos*: Visual inpainting, object insertion/removal, and background alterations.
- **Stratified Temporal Sampling**: Samples frames proportionally from the beginning (25%), middle (38-62%), and ending (75-100%) to prevent missing localized anomalies.
- **Temporal Optical Flow & Frequency Coherence**: Farneback dense optical flow and 2D FFT spectral analysis detecting non-physical motion vector divergence and texture flickering.
- **Audio Spectral & Neural Vocoder Forensics**: Identifies synthetic vocoder brickwall cutoffs (>7.2kHz attenuation) and unnatural silence floors.
- **Suspicious Frame Evidence Gallery**: Highlights flagged frames with timestamps, category tags, and forensic trigger reasons.

### 5. Forensic Audit History Vault (`pages/5_Analysis_History.py`)
- Persistent SQLite database ledger logging tracking codes, timestamps, forensic modality, confidence, and detection metadata.
- Filter, search, inspect raw JSON records, and export CSV audit reports.
- **Privacy First**: Zero persistent raw media storage. Media frames are processed in-memory and wiped immediately upon completion.

### 6. Architectural Dossier & Threat Modeling (`pages/6_About.py`)
- Complete engineering specifications, threat surfaces, model boundaries, and ethical guidelines.

---

## 💻 Tech Stack

- **Python 3.11**
- **Streamlit** (Cybersecurity Command Center UI & Custom CSS)
- **PyTorch** (Deep Learning & CUDA Acceleration)
- **Hugging Face Transformers** (RoBERTa/BERT, Vision Transformers)
- **OpenCV** (`cv2` video decoding, face detection, normalization)
- **Scikit-learn** (Metrics, classification pipelines, confusion matrices)
- **LIME** (Local Interpretable Model-agnostic Explanations)
- **Plotly** (Interactive radar, donut, and temporal charts)
- **SQLite** (Persistent audit history ledger)
- **Pandas & NumPy** (Data processing)

---

## 🚀 Quickstart & Execution Guide

### 1. Prerequisites
Ensure you have **Python 3.11** installed on your system.

### 2. Dependency Installation
Run the following PowerShell command inside `truthlens-ai`:

```powershell
pip install -r requirements.txt
```

### 3. Launching the Command Center
Execute:

```powershell
python -m streamlit run app.py
```

The application will start at `http://localhost:8501`.
