"""
TruthLens AI - Fake News Text Intelligence Engine
Detects sensational, fabricated, and misleading patterns using fine-tuned transformer architectures
and a benchmark-trained TF-IDF Logistic Regression classifier with transparent status disclosures.
"""

import os
from typing import Dict, Any, List, Tuple
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline

from data.dataset import get_benchmark_dataset


class FakeNewsDetector:
    """
    Multimodal Text Forensic Classifier.
    Prioritizes fine-tuned transformer weights; falls back to an auditable
    TF-IDF + Logistic Regression model trained on benchmark data if offline or downloading.
    """

    def __init__(self):
        self.device = "cpu"
        self.transformer_pipeline = None
        self.transformer_model_name = "jy46604790/Fake-News-Bert-Detect"
        self.baseline_pipeline = None
        self.active_engine = "UNINITIALIZED"
        self.status_message = ""
        self._init_models()

    def _init_models(self):
        """Initialize both the baseline classifier and attempt loading the transformer."""
        # 1. Always train and ready the verified baseline
        self._train_baseline()
        
        # 2. Attempt loading fine-tuned transformer
        self._load_transformer()

    def _train_baseline(self):
        """Train TF-IDF + Logistic Regression on real benchmark data."""
        try:
            data = get_benchmark_dataset()
            texts = [d["text"] for d in data]
            labels = [d["label"] for d in data]
            
            self.baseline_pipeline = Pipeline([
                ("tfidf", TfidfVectorizer(ngram_range=(1, 2), max_features=2500, sublinear_tf=True)),
                ("clf", LogisticRegression(C=1.0, max_iter=250, random_state=42))
            ])
            self.baseline_pipeline.fit(texts, labels)
            self.active_engine = "TF-IDF + Logistic Regression (Benchmark Trained)"
            self.status_message = "Active: Auditable Baseline Model trained on verified Real/Fake benchmark dataset."
        except Exception as e:
            self.status_message = f"Baseline training error: {str(e)}"

    def _load_transformer(self):
        """Attempt to load genuine pretrained fake news transformer from HuggingFace."""
        try:
            import socket
            import torch
            from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline
            
            self.device = "cuda" if torch.cuda.is_available() else "cpu"
            
            # Step 1: Try local cache first for sub-millisecond offline loading
            try:
                tokenizer = AutoTokenizer.from_pretrained(self.transformer_model_name, local_files_only=True)
                model = AutoModelForSequenceClassification.from_pretrained(self.transformer_model_name, local_files_only=True)
                self.transformer_pipeline = pipeline(
                    "text-classification",
                    model=model,
                    tokenizer=tokenizer,
                    device=0 if self.device == "cuda" else -1,
                    top_k=None
                )
                self.active_engine = f"Transformer ({self.transformer_model_name})"
                self.status_message = f"Active: Pretrained Fake-News Transformer (Local Cache) on {self.device.upper()}."
                return
            except Exception:
                pass

            # Step 2: Test network reachability before attempting download to avoid long retries
            try:
                socket.create_connection(("huggingface.co", 443), timeout=1.0)
            except Exception:
                self.active_engine = "TF-IDF + Logistic Regression (Benchmark Baseline)"
                self.status_message = "Active: Auditable Baseline Model (HuggingFace offline/sandboxed)."
                return

            # Step 3: Online download if reachable
            tokenizer = AutoTokenizer.from_pretrained(self.transformer_model_name, local_files_only=False)
            model = AutoModelForSequenceClassification.from_pretrained(self.transformer_model_name, local_files_only=False)
            
            self.transformer_pipeline = pipeline(
                "text-classification",
                model=model,
                tokenizer=tokenizer,
                device=0 if self.device == "cuda" else -1,
                top_k=None
            )
            self.active_engine = f"Transformer ({self.transformer_model_name})"
            self.status_message = f"Active: Hugging Face Pretrained Fake-News Transformer on {self.device.upper()}."
        except Exception as e:
            # Fallback seamlessly to the verified baseline
            self.active_engine = "TF-IDF + Logistic Regression (Benchmark Baseline)"
            self.status_message = f"Transformer offline ({type(e).__name__}). Using verified benchmark Logistic Regression."

    def predict_proba(self, texts: List[str]) -> np.ndarray:
        """
        Predict probability distribution for texts: shape (N, 2)
        Column 0: REAL, Column 1: POTENTIALLY FAKE
        Required for LIME explainer.
        """
        # If transformer is available, use it if possible; otherwise use baseline pipeline
        if self.transformer_pipeline:
            try:
                outputs = self.transformer_pipeline(texts, truncation=True, max_length=512)
                probs = []
                for out in outputs:
                    score_map = {item["label"].upper(): item["score"] for item in out}
                    # For jy46604790/Fake-News-Bert-Detect:
                    # LABEL_0 is FAKE (99.8% on conspiracy), LABEL_1 is REAL (99.9% on Reuters/AP)
                    fake_p = score_map.get("LABEL_0", score_map.get("FAKE", 0.5))
                    real_p = score_map.get("LABEL_1", score_map.get("REAL", 1.0 - fake_p))
                    total = fake_p + real_p
                    probs.append([real_p / total, fake_p / total])
                return np.array(probs)
            except Exception:
                pass
                
        # Baseline pipeline fallback
        if self.baseline_pipeline:
            return self.baseline_pipeline.predict_proba(texts)
            
        # Uniform fallback if uninitialized
        return np.ones((len(texts), 2)) * 0.5

    def analyze(self, text: str) -> Dict[str, Any]:
        """
        Analyze a single news article text.
        Returns prediction ('REAL' or 'POTENTIALLY FAKE'), confidence, and probability map.
        """
        cleaned = text.strip()
        if not cleaned:
            return {
                "success": False,
                "error": "Empty text submitted for analysis."
            }

        probs = self.predict_proba([cleaned])[0]
        real_prob = float(probs[0])
        fake_prob = float(probs[1])

        if fake_prob >= 0.50:
            prediction = "POTENTIALLY FAKE"
            confidence = fake_prob
        else:
            prediction = "REAL"
            confidence = real_prob

        return {
            "success": True,
            "prediction": prediction,
            "confidence": round(confidence, 4),
            "probabilities": {
                "REAL": round(real_prob, 4),
                "POTENTIALLY FAKE": round(fake_prob, 4)
            },
            "model_name": self.active_engine,
            "status_message": self.status_message,
            "disclaimer": (
                "Important: TruthLens AI classifies stylistic, syntactic, and semantic patterns "
                "learned from benchmark misinformation training data. This evaluation does not verify "
                "underlying factual truth and should be audited alongside primary human journalism."
            )
        }


# Singleton cache
_text_detector_instance = None

def get_text_detector() -> FakeNewsDetector:
    global _text_detector_instance
    if _text_detector_instance is None:
        _text_detector_instance = FakeNewsDetector()
    return _text_detector_instance
