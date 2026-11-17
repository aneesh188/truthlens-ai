# TRUTHLENS AI — Multimodal Media Intelligence & Cybersecurity Platform
### Real-Time Threat Intelligence, Universal AI Video Forensics & Deepfake Detection

[![Python 3.11](https://img.shields.io/badge/Python-3.11-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.30+-FF4B4B.svg)](https://streamlit.io/)
[![PyTorch](https://img.shields.io/badge/PyTorch-2.0+-EE4C2C.svg)](https://pytorch.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

**TruthLens AI** is an enterprise-grade multimodal media intelligence and forensics platform designed to detect, analyze, and catalog synthetic digital media and misinformation. Built with a high-performance **CyberShield AI Security Operations Center (SOC)** interface, TruthLens delivers real-time threat intelligence, explainable NLP misinformation detection, Vision Transformer synthetic image classification, and universal zero-face video forensics.

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

| Component | Technologies |
|---|---|
| **Runtime & Language** | Python 3.11 |
| **Frontend & UI** | Streamlit, Custom Cyber SOC CSS, HTML5 Canvas, JavaScript, Web Audio API |
| **Deep Learning** | PyTorch, CUDA / CPU Fallback, Torchvision |
| **Pretrained Models** | Hugging Face Transformers (`umm-maybe/AI-image-detector`, RoBERTa/BERT) |
| **Computer Vision** | OpenCV (`cv2`), Farneback Optical Flow, 2D FFT Spectral Analysis |
| **Audio Forensics** | SciPy FFT, FFmpeg Audio Demuxing |
| **Explainable AI** | LIME (Local Interpretable Model-agnostic Explanations) |
| **Visualization** | Plotly Graph Objects, HTML5 Canvas, SVG |
| **Database** | SQLite3 persistent metadata ledger |

---

## 🚀 Quickstart & Installation

### 1. Clone the Repository
```bash
git clone https://github.com/aneesh188/truthlens-ai.git
cd truthlens-ai
```

### 2. Install Dependencies
```powershell
pip install -r truthlens-ai/requirements.txt
```

### 3. Launch the Application
You can run the application directly using either:

**Using Python / Streamlit:**
```powershell
cd truthlens-ai
python -m streamlit run app.py
```

**Using the Windows launcher script:**
```powershell
.\run_truthlens.bat
```

Access the command center in your browser at `http://localhost:8501`.

---

## 📁 Repository Structure

```text
truthlens-ai/
├── run_truthlens.bat              # One-click Windows batch launcher
├── run_truthlens.ps1              # One-click PowerShell launcher
├── README.md                      # Platform documentation
├── .gitignore                     # Repository exclusions
│
└── truthlens-ai/
    ├── app.py                     # Master application entrypoint
    ├── dashboard_view.py          # CyberShield AI SOC command center
    ├── warp_portal.py             # 3D Hyperspace dive tunnel & particle sphere
    ├── ui_common.py               # Shared header, telemetry, and CSS loaders
    ├── requirements.txt           # Python package dependencies
    ├── README.md                  # Component documentation
    ├── truthlens.db               # SQLite metadata audit ledger
    │
    ├── pages/
    │   ├── 1_Dashboard.py         # Real-time threat intelligence dashboard
    │   ├── 2_Fake_News.py         # Text misinformation & LIME explainability
    │   ├── 3_AI_Image.py          # Vision Transformer synthetic image detection
    │   ├── 4_Deepfake_Video.py    # Universal AI video forensics (Zero-face + faces)
    │   ├── 5_Analysis_History.py  # SQLite audit ledger & CSV export vault
    │   └── 6_About.py             # Architecture, threat modeling & ethics
    │
    ├── models/
    │   ├── text_detector.py       # Dual-engine fake news text classifier
    │   ├── image_detector.py      # Vision Transformer AI image classifier
    │   └── deepfake_detector.py   # Facial manipulation classifier
    │
    ├── processing/
    │   ├── video_processor.py     # Universal multi-stage video forensic pipeline
    │   ├── face_detector.py       # OpenCV face localization & context cropping
    │   ├── temporal_analyzer.py   # Farneback optical flow & 2D FFT flicker coherence
    │   ├── audio_analyzer.py      # FFmpeg audio extraction & FFT vocoder cutoff forensics
    │   ├── scene_classifier.py    # 5-category forensic scene taxonomy classifier
    │   └── image_processor.py     # Image validation, EXIF decoding & normalization
    │
    ├── evaluation/
    │   ├── metrics.py             # Accuracy, precision, recall, F1 & confusion matrices
    │   ├── model_comparison.py    # Comparative benchmarking suite
    │   └── lime_explainer.py      # LIME text feature attribution
    │
    ├── database/
    │   └── db.py                  # SQLite schema, queries, and statistics engine
    │
    ├── assets/
    │   └── styles.css             # CyberShield AI SOC stylesheet & animations
    │
    └── data/
        ├── dataset.py             # Benchmark news dataset generator
        └── news_benchmark.json    # Verified authentic and fake news samples
```

---

## 🛡️ License

This project is licensed under the MIT License - see the LICENSE file for details.
