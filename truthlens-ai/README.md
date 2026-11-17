# TRUTHLENS AI — Multimodal Media Intelligence & Cybersecurity Platform
### Real-Time Threat Intelligence, Universal AI Video Forensics & Deepfake Detection

[![Python 3.11](https://img.shields.io/badge/Python-3.11-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.30+-FF4B4B.svg)](https://streamlit.io/)
[![PyTorch](https://img.shields.io/badge/PyTorch-2.0+-EE4C2C.svg)](https://pytorch.org/)
[![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-green.svg)](https://opencv.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

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
- **Zero-Face Multi-Category Detection**: Unlike conventional facial deepfake tools that fail on face-free footage, TruthLens AI analyzes videos even when **NO human face** is present:
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

## 🚀 How to Run the Project (Step-by-Step Guide)

Follow these instructions to set up and run TruthLens AI on your local machine.

### Prerequisites

- **Python 3.11** (or Python 3.10+) installed. Download from [python.org](https://www.python.org/).
- **Git** installed. Download from [git-scm.com](https://git-scm.com/).
- *(Optional)* An NVIDIA GPU with CUDA drivers for accelerated deep learning inference. If no GPU is found, the system automatically falls back to CPU mode.

---

### Step 1: Clone the Repository

```bash
git clone https://github.com/aneesh188/truthlens-ai.git
cd truthlens-ai
```

---

### Step 2: (Recommended) Create and Activate a Virtual Environment

**On Windows (PowerShell):**
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

**On Windows (Command Prompt):**
```cmd
python -m venv venv
venv\Scripts\activate.bat
```

**On macOS / Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

---

### Step 3: Install Required Dependencies

```bash
pip install -r truthlens-ai/requirements.txt
```

---

### Step 4: Launch TruthLens AI

#### Option A: Run via Python Module (Recommended for All Platforms)
From inside the repository:

```powershell
cd truthlens-ai
python -m streamlit run app.py
```

> **Why `python -m streamlit run app.py`?**
> On Windows, running `streamlit run app.py` directly can sometimes fail with `'streamlit' is not recognized as a cmdlet` if Python's `Scripts/` folder is not added to your system `PATH`. Invoking Python with `-m streamlit` works reliably every time!

#### Option B: Windows 1-Click Launchers
If you are on Windows, simply double-click or run either launcher from the root folder:
- **Batch file**: Double-click `run_truthlens.bat`
- **PowerShell script**: Right-click `run_truthlens.ps1` and select *Run with PowerShell*, or run:
  ```powershell
  .\run_truthlens.ps1
  ```

---

### Step 5: Open in Your Browser

Open your web browser and navigate to:

👉 **`http://localhost:8501`**

---

## 🛠️ Troubleshooting FAQ

- **Error: `'streamlit' is not recognized as a cmdlet`**: Always run using `python -m streamlit run app.py`.
- **Change Default Port**: Run `python -m streamlit run app.py --server.port 8502`.
- **Offline Mode**: If external model weights cannot be reached, the system automatically uses local offline fallback classifiers and local computer vision pipelines.
- **Privacy Architecture**: All media is processed transiently in-memory and wiped immediately upon completion.
