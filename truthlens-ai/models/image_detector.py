"""
TruthLens AI - AI-Generated Synthetic Image Detector
Uses fine-tuned Vision Transformer (ViT) / ResNet architectures to detect generative AI artifacts (e.g., Midjourney, DALL-E, Stable Diffusion).
Strictly verifies genuine model checkpoints and transparently reports unconfigured states without inventing results.
"""

import os
from typing import Dict, Any, Optional
from PIL import Image
import numpy as np


class SyntheticImageDetector:
    """
    Forensic Vision Classifier for AI-generated vs authentic images.
    """

    def __init__(self, model_id: str = "umm-maybe/AI-image-detector"):
        self.model_id = model_id
        self.pipeline = None
        self.device = "cpu"
        self.status = "NOT_LOADED"
        self.status_message = "Detector uninitialized."
        self._load_model()

    def _load_model(self):
        """Attempt to load genuine pretrained AI image classification pipeline."""
        try:
            import socket
            import torch
            from transformers import pipeline, AutoImageProcessor, AutoModelForImageClassification
            
            self.device = "cuda" if torch.cuda.is_available() else "cpu"
            
            # Step 1: Try local cache first for instant load
            try:
                processor = AutoImageProcessor.from_pretrained(self.model_id, local_files_only=True)
                model = AutoModelForImageClassification.from_pretrained(self.model_id, local_files_only=True)
                self.pipeline = pipeline(
                    "image-classification",
                    model=model,
                    feature_extractor=processor,
                    device=0 if self.device == "cuda" else -1
                )
                self.status = "ONLINE"
                self.status_message = f"Pretrained Vision Transformer (Cached: {self.model_id}) on {self.device.upper()}."
                return
            except Exception:
                pass

            # Step 2: Check network reachability before trying download
            try:
                socket.create_connection(("huggingface.co", 443), timeout=1.0)
            except Exception:
                self.status = "NOT_CONFIGURED"
                self.status_message = "Vision checkpoint not cached locally and network is offline/isolated."
                self.pipeline = None
                return

            # Step 3: Online download
            processor = AutoImageProcessor.from_pretrained(self.model_id, local_files_only=False)
            model = AutoModelForImageClassification.from_pretrained(self.model_id, local_files_only=False)
            
            self.pipeline = pipeline(
                "image-classification",
                model=model,
                feature_extractor=processor,
                device=0 if self.device == "cuda" else -1
            )
            self.status = "ONLINE"
            self.status_message = f"Pretrained Vision Transformer ({self.model_id}) loaded on {self.device.upper()}."
        except Exception as e:
            self.status = "NOT_CONFIGURED"
            self.status_message = (
                f"Model checkpoint unavailable ({type(e).__name__}). "
                "Ensure internet access to pull 'umm-maybe/AI-image-detector' or stage offline weights."
            )
            self.pipeline = None

    def analyze(self, pil_image: Image.Image) -> Dict[str, Any]:
        """
        Analyze an image for generative AI signatures.
        """
        if pil_image is None:
            return {"success": False, "error": "No image supplied."}

        # If model is not loaded/configured, return honest status
        if self.status != "ONLINE" or self.pipeline is None:
            return {
                "success": False,
                "status": "MODEL_NOT_CONFIGURED",
                "error": self.status_message,
                "model_name": self.model_id,
                "disclaimer": (
                    "Important: TruthLens AI will not fabricate random scores when checkpoints are missing. "
                    "Configure or download the model weights to run neural forensic inference."
                )
            }

        try:
            # Run inference
            results = self.pipeline(pil_image)
            # results format: [{'label': 'artificial', 'score': 0.94}, {'label': 'human', 'score': 0.06}]
            
            synthetic_prob = 0.5
            real_prob = 0.5
            
            for res in results:
                label_lower = res["label"].lower()
                score = float(res["score"])
                if any(k in label_lower for k in ["artificial", "fake", "synthetic", "ai"]):
                    synthetic_prob = score
                elif any(k in label_lower for k in ["human", "real", "authentic"]):
                    real_prob = score

            # Normalize probabilities
            total = synthetic_prob + real_prob
            if total > 0:
                synthetic_prob = synthetic_prob / total
                real_prob = real_prob / total

            if synthetic_prob >= 0.50:
                prediction = "SYNTHETIC / AI-GENERATED"
                confidence = synthetic_prob
            else:
                prediction = "LIKELY AUTHENTIC"
                confidence = real_prob

            return {
                "success": True,
                "status": "ANALYSIS_COMPLETE",
                "prediction": prediction,
                "confidence": round(confidence, 4),
                "probabilities": {
                    "SYNTHETIC": round(synthetic_prob, 4),
                    "AUTHENTIC": round(real_prob, 4)
                },
                "model_name": f"ViT ({self.model_id})",
                "device": self.device.upper(),
                "disclaimer": (
                    "Notice: Generative models evolve rapidly. Re-compression, downscaling, social media "
                    "filters, or unseen diffusion architectures can induce false positives or negatives. "
                    "Use this assessment as an assistive forensic signal."
                )
            }

        except Exception as e:
            return {
                "success": False,
                "status": "INFERENCE_ERROR",
                "error": f"Inference execution failed: {str(e)}",
                "model_name": self.model_id
            }


# Singleton cache
_image_detector_instance = None

def get_image_detector() -> SyntheticImageDetector:
    global _image_detector_instance
    if _image_detector_instance is None:
        _image_detector_instance = SyntheticImageDetector()
    return _image_detector_instance
