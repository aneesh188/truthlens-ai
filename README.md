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

## 🚀 How to Run the Project (Step-by-Step Guide)

Follow these instructions to set up and run TruthLens AI on your local machine.

### Prerequisites

- **Python 3.11** (or Python 3.10+) installed. Download from [python.org](https://www.python.org/).
- **Git** installed. Download from [git-scm.com](https://git-scm.com/).
- *(Optional)* An NVIDIA GPU with CUDA drivers for accelerated deep learning inference. If no GPU is found, the system automatically falls back to CPU mode.

---

### Step 1: Clone the Repository

Open your terminal or command prompt and clone the repository:

```bash
git clone https://github.com/aneesh188/truthlens-ai.git
cd truthlens-ai
```

---

### Step 2: (Recommended) Create and Activate a Virtual Environment

It is recommended to run the project inside a virtual environment to prevent package conflicts.

**On Windows (PowerShell):**
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```
*(If PowerShell restricts script execution, run: `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass`)*

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

Install all required Python libraries via pip:

```bash
pip install -r truthlens-ai/requirements.txt
```

> **Note:** If you are already inside the `truthlens-ai/` directory, simply run:
> ```bash
> pip install -r requirements.txt
> ```

---

### Step 4: Launch TruthLens AI

You have two easy ways to launch the platform:

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

Once started, the terminal will display the local URL. Open your web browser and navigate to:

👉 **`http://localhost:8501`**

---

## 📖 How to Use TruthLens AI (User Walkthrough)

Once the application is running in your browser:

1. **Dashboard & Threat Intelligence (`pages/1_Dashboard.py`)**:
   - Inspect the real-time CyberShield AI command center with live animated attack arcs and rotating shield HUD.
   - Click the expandable **"Launch Hyperspace Sensory Dive"** at the top to experience the 3D particle tunnel and globe.
   - Review CPU/GPU hardware utilization and active threat engines in the left sidebar.

2. **Fake News Text Intelligence (`pages/2_Fake_News.py`)**:
   - Enter any news headline, article body, or claim in the text box.
   - Or click one of the pre-loaded benchmark buttons (e.g. *Fed Interest Rates* or *Antarctica Retinal Reset*).
   - Click **Run Forensic Analysis**.
   - Review the authentic vs fake verdict and inspect the **LIME Explainable AI token attribution chart** showing which words triggered the verdict.

3. **AI-Generated Image Forensics (`pages/3_AI_Image.py`)**:
   - Upload any image file (`PNG`, `JPG`, `WEBP`).
   - Click **Run Forensic Inspection**.
   - Review the Vision Transformer synthetic probability and EXIF payload integrity.

4. **Universal Video Forensics (`pages/4_Deepfake_Video.py`)**:
   - Upload any video file (`MP4`, `AVI`, `MOV`).
   - Adjust the frame sampling slider (samples frames proportionally across start, middle, and end).
   - Click **Execute Forensic Inspection**.
   - The engine automatically runs:
     - 5-Category Taxonomy Classification (works even with **zero human faces**).
     - Temporal Optical Flow consistency (Farneback motion vectors).
     - Audio spectral FFT analysis to flag synthetic neural vocoder cutoffs.
     - Flagged frame evidence gallery with timestamps.

5. **Analysis History & Audit Vault (`pages/5_Analysis_History.py`)**:
   - View the persistent SQLite ledger of all inspections performed.
   - Filter by modality (Text, Image, Video) or search by tracking code.
   - Export full compliance audit reports to CSV with one click.

---

## 🛠️ Troubleshooting FAQ

<details>
<summary><b>1. Error: <code>'streamlit' is not recognized as the name of a cmdlet</code></b></summary>
<br>
This happens on Windows when Python's <code>Scripts</code> directory is not in your system environment variable <code>PATH</code>.
<br><br>
<b>Solution:</b> Always launch with Python module syntax:
<pre><code>python -m streamlit run app.py</code></pre>
</details>

<details>
<summary><b>2. How do I change the default port (8501)?</b></summary>
<br>
If port 8501 is already in use by another service, launch with a custom port:
<pre><code>python -m streamlit run app.py --server.port 8502</code></pre>
</details>

<details>
<summary><b>3. Does TruthLens AI require an internet connection?</b></summary>
<br>
No! TruthLens AI is designed with offline fallback capabilities:
<ul>
  <li>If external model weights cannot be downloaded, the system automatically uses its local pretrained TF-IDF Logistic Regression classifier and local computer vision pipelines.</li>
  <li>All facial localization, Farneback optical flow, 2D FFT spectral analysis, and SQLite history work 100% locally and offline.</li>
</ul>
</details>

<details>
<summary><b>4. Does TruthLens AI store my uploaded media?</b></summary>
<br>
No. TruthLens AI follows a <b>Zero-Persistence Privacy Architecture</b>:
<ul>
  <li>Uploaded images and video frames are processed transiently in-memory and deleted immediately upon completion.</li>
  <li>Only sanitized audit metadata (timestamp, modality, verdict, and confidence score) is recorded to the SQLite ledger.</li>
</ul>
</details>

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
