# TRUTHLENS AI — Multimodal Media Intelligence Platform
### Advanced Cybersecurity Command Center for Misinformation, Synthetic Images & Deepfakes

TruthLens AI is an end-to-end media forensics and multimodal intelligence platform designed to audit and classify suspect digital content. It brings together state-of-the-art Natural Language Processing, Vision Transformers, and Computer Vision under a cybersecurity command-center interface.

---

## 🌟 Core Forensic Modalities

1. **Fake News Text Intelligence (`pages/2_Fake_News.py`)**
   - Classifies articles, rumors, and social claims as **REAL** or **POTENTIALLY FAKE**.
   - Dual-engine architecture: Pretrained Hugging Face sequence classifier with an auditable TF-IDF Logistic Regression baseline trained on benchmark datasets.
   - **Explainable AI with LIME**: Computes local token attributions, visualizing which words drove prediction towards misleading or factual patterns.
   - Transparent disclaimer: Audits stylistic and semantic patterns; does not verify absolute historical truth.

2. **AI-Generated Image Forensics (`pages/3_AI_Image.py`)**
   - Detects generative synthesis artifacts from **Midjourney**, **DALL-E**, and **Stable Diffusion**.
   - Leverages fine-tuned **Vision Transformers (ViT)**.
   - Reports authentic vs synthetic probabilities without fabricating predictions if weights are absent.

3. **Universal AI Video Forensics (`pages/4_Deepfake_Video.py`)**
   - **Zero-Face Multi-Category Detection**: Unlike conventional deepfake tools that fail on face-free footage, TruthLens AI analyzes landscapes, cities, nature, animation, synthetic humans, and visual inpainting.
   - **5 Core Forensic Taxonomies**:
     1. *Face Deepfakes*: Face swapping, reenactment, synthetic face generation.
     2. *Fully AI-Generated Videos*: Generative landscapes, synthetic architecture, wildlife.
     3. *AI-Generated Synthetic Humans*: Full-body synthetic avatars and unnatural body motion.
     4. *AI-Generated Animation*: Cartoons, 3D CGI characters, stylized synthesis.
     5. *AI-Manipulated Videos*: Inpainting, object insertion/removal, background alterations.
   - **Stratified Temporal Sampling**: Proportional sampling across beginning (25%), middle (38-62%), and climax (75-100%) to prevent missing anomalies in long videos.
   - **Vision Transformer (ViT) Full-Frame Analysis**: Extracts synthetic latent noise patterns even when 0 faces are present.
   - **Temporal Optical Flow & Frequency Coherence**: Uses Farneback dense optical flow and 2D FFT spectral analysis to detect non-physical motion vector divergence and texture flickering.
   - **Audio Spectral & Neural Vocoder Forensics**: Uses FFmpeg to extract audio and SciPy FFT to detect synthetic neural vocoder brickwall cutoffs (>7.2kHz attenuation) and unnatural silence floors.
   - **Suspicious Frame Evidence Gallery**: Highlights flagged frames with timestamps, category badges, and specific forensic trigger reasons.

4. **Comparative Model Intelligence (`pages/5_Model_Evaluation.py`)**
   - Evaluates two distinct architectures (*L2 Logistic Regression* vs *Multinomial Naive Bayes*) on identical held-out test splits (30%).
   - Displays exact Accuracy, Precision, Recall, F1-scores, Confusion Matrices, and Classification Reports.

5. **Auditing History Vault (`pages/6_Analysis_History.py`)**
   - Persistent SQLite database ledger storing analysis codes, timestamps, modality, models, confidence, and metadata.
   - Search, filter by modality, inspect record JSON, and export full CSV audit reports.
   - Privacy-first zero-media storage: raw images and video frames are processed transiently and discarded immediately.

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
streamlit run app.py
```

The application will start at `http://localhost:8501`.

---

## 📁 Project Architecture

```text
truthlens-ai/
├── app.py                     # Master application entrypoint & dashboard launcher
├── dashboard_view.py          # Unified cybersecurity command center view
├── ui_common.py               # Shared header, telemetry, and CSS loaders
├── requirements.txt           # Verified Python dependencies
├── README.md                  # Comprehensive platform documentation
├── .gitignore                 # Safe repository exclusions
│
├── pages/
│   ├── 1_Dashboard.py         # Cybersecurity overview & active metrics
│   ├── 2_Fake_News.py         # Text misinformation & LIME explainability
│   ├── 3_AI_Image.py          # Vision Transformer synthetic image detection
│   ├── 4_Deepfake_Video.py    # OpenCV temporal video & facial deepfake analysis
│   ├── 5_Model_Evaluation.py  # Empirical model evaluation & confusion matrices
│   ├── 6_Analysis_History.py  # SQLite forensic audit history ledger
│   └── 7_About.py             # System architecture & threat modeling guide
│
├── models/
│   ├── text_detector.py       # Dual-engine fake news text classifier
│   ├── image_detector.py      # Vision Transformer AI-image detector
│   └── deepfake_detector.py   # XceptionNet facial manipulation classifier
│
├── processing/
│   ├── face_detector.py       # OpenCV face localization & context cropping
│   ├── video_processor.py     # Universal multi-stage video forensic pipeline
│   ├── temporal_analyzer.py   # Farneback optical flow & 2D FFT flicker coherence
│   ├── audio_analyzer.py      # FFmpeg audio extraction & FFT vocoder cutoff forensics
│   ├── scene_classifier.py    # 5-category forensic scene taxonomy classifier
│   └── image_processor.py     # Image validation, EXIF decoding & normalization
│
├── evaluation/
│   ├── metrics.py             # Accuracy, precision, recall, F1 & confusion matrices
│   ├── model_comparison.py    # Comparative benchmarking suite on held-out split
│   └── lime_explainer.py      # LIME text feature attribution
│
├── database/
│   └── db.py                  # SQLite schema, queries, and statistics engine
│
├── assets/
│   └── styles.css             # Cyber command center CSS theme
│
├── data/
│   ├── dataset.py             # Benchmark news dataset generator
│   └── news_benchmark.json    # Verified authentic and fake news samples
│
└── checkpoints/
    └── .gitkeep               # Directory for FaceForensics++ Xception weights
```

---

## 🎯 Model Configuration & Checkpoints

### 1. Fake News Text Model
- **Primary:** `jy46604790/Fake-News-Bert-Detect` (loaded on-the-fly via Hugging Face Transformers).
- **Baseline:** Pretrained TF-IDF + Logistic Regression trained on `data/news_benchmark.json`. Operates offline automatically if external network or Hugging Face is unreachable.

### 2. AI Image Vision Model
- **Primary:** `umm-maybe/AI-image-detector` (Vision Transformer).
- Operates on RGB images; automatically reports unconfigured status if offline weights or connection are unavailable.

### 3. FaceForensics++ XceptionNet Deepfake Model
- Architecture: Standard 2-class XceptionNet with normalization $(0.5, 0.5, 0.5)$.
- Default checkpoint path: `checkpoints/xception_deepfake.pth`.
- If no checkpoint is present in `checkpoints/`, the system will isolate faces, extract frames, and report that the weights are pending without fabricating results.

---

## 🛡️ Hackathon Demonstration Walkthrough

1. **Dashboard Overview:**
   - Launch `app.py`. Review real-time hardware telemetry (RTX 3050 GPU detected, CPU load, RAM).
   - Point out the stored audit statistics (all live from SQLite).

2. **Test Fake News Detection:**
   - Navigate to **Fake News Detection**.
   - Click one of the 4 verified benchmark buttons (e.g. *Fed Interest Rates* or *Antarctica Retinal Reset*).
   - Click **Run Forensic Analysis**.
   - Demonstrate the classification verdict, probability spectrum, and **LIME Explainable AI chart** highlighting influential tokens.

3. **Test AI Image Detection:**
   - Navigate to **AI Image Detection**.
   - Upload any suspect image.
   - Review metadata extraction (dimensions, format, payload).
   - Execute synthetic vision inspection.

4. **Test Video Deepfake Detection:**
   - Navigate to **Deepfake Video Detection**.
   - Upload an MP4 video or test static portrait face localization.
   - Adjust sampling slider and execute temporal analysis.
   - Observe real-time frame extraction, face bounding boxes, and temporal manipulation curves.

5. **Model Evaluation & History:**
   - Navigate to **Model Evaluation** to review empirical accuracy, precision, recall, and interactive confusion matrices.
   - Check **Analysis History** to view the audit ledger, search by tracking code, inspect raw JSON metadata, and export CSV logs.
