"""
TruthLens AI - XceptionNet Facial Deepfake & Manipulation Detector
Implements the FaceForensics++ XceptionNet architecture for detecting facial swaps and warping artifacts.
Adheres strictly to the verification protocol: requires authentic deepfake-trained weights;
will not falsify detections if weights are not configured.
"""

import os
from typing import Dict, Any, Optional
import numpy as np
from PIL import Image

CHECKPOINT_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "checkpoints")
DEFAULT_WEIGHTS_PATH = os.path.join(CHECKPOINT_DIR, "xception_deepfake.pth")


class XceptionDeepfakeDetector:
    """
    Forensic classifier for detecting face-swap deepfakes using XceptionNet architecture.
    """

    def __init__(self, checkpoint_path: Optional[str] = None):
        self.checkpoint_path = checkpoint_path or DEFAULT_WEIGHTS_PATH
        self.model = None
        self.device = "cpu"
        self.is_configured = False
        self.status_message = ""
        self._init_detector()

    def _init_detector(self):
        """Check for genuine deepfake checkpoint and attempt loading."""
        try:
            import torch
            self.device = "cuda" if torch.cuda.is_available() else "cpu"
            
            if not os.path.exists(self.checkpoint_path):
                self.is_configured = False
                self.status_message = (
                    f"XceptionNet deepfake checkpoint not found at '{os.path.basename(self.checkpoint_path)}'. "
                    "In compliance with forensic accuracy guidelines, raw ImageNet weights will not be "
                    "substituted. Place authentic FaceForensics++ / DFDC weights in checkpoints/ directory."
                )
                return

            # If checkpoint exists, construct model and load weights
            import timm
            # Standard Xception model with 2-class binary head for FaceForensics++
            model = timm.create_model("xception", pretrained=False, num_classes=2)
            
            checkpoint = torch.load(self.checkpoint_path, map_location=self.device)
            state_dict = checkpoint.get("state_dict", checkpoint) if isinstance(checkpoint, dict) else checkpoint
            
            # Clean possible module. prefix from DataParallel training
            cleaned_state_dict = {k.replace("module.", ""): v for k, v in state_dict.items()}
            model.load_state_dict(cleaned_state_dict, strict=False)
            
            model.to(self.device)
            model.eval()
            self.model = model
            self.is_configured = True
            self.status_message = f"XceptionNet Deepfake Model active on {self.device.upper()}."

        except Exception as e:
            self.is_configured = False
            self.status_message = f"Failed to load XceptionNet checkpoint: {str(e)}"

    def predict_face(self, face_bgr: np.ndarray) -> Dict[str, Any]:
        """
        Analyze a single cropped face image (numpy BGR array 299x299).
        Returns manipulation probabilities and prediction.
        """
        if not self.is_configured or self.model is None:
            return {
                "success": False,
                "status": "CHECKPOINT_NOT_CONFIGURED",
                "message": self.status_message,
                "fake_probability": 0.0,
                "real_probability": 0.0
            }

        try:
            import torch
            from torchvision import transforms

            transform = transforms.Compose([
                transforms.ToTensor(),
                transforms.Normalize(mean=[0.5, 0.5, 0.5], std=[0.5, 0.5, 0.5])
            ])

            # Convert BGR to RGB
            face_rgb = face_bgr[:, :, ::-1]
            pil_face = Image.fromarray(face_rgb)
            tensor = transform(pil_face).unsqueeze(0).to(self.device)

            with torch.no_grad():
                outputs = self.model(tensor)
                probs = torch.softmax(outputs, dim=1).cpu().numpy()[0]

            # Index 0: Real, Index 1: Manipulated/Fake
            real_prob = float(probs[0])
            fake_prob = float(probs[1])

            return {
                "success": True,
                "status": "ANALYSIS_COMPLETE",
                "prediction": "MANIPULATED" if fake_prob > 0.5 else "REAL",
                "fake_probability": round(fake_prob, 4),
                "real_probability": round(real_prob, 4),
                "confidence": round(max(real_prob, fake_prob), 4)
            }

        except Exception as e:
            return {
                "success": False,
                "status": "INFERENCE_ERROR",
                "error": str(e),
                "fake_probability": 0.0,
                "real_probability": 0.0
            }


# Singleton cache
_deepfake_detector_instance = None

def get_deepfake_detector() -> XceptionDeepfakeDetector:
    global _deepfake_detector_instance
    if _deepfake_detector_instance is None:
        _deepfake_detector_instance = XceptionDeepfakeDetector()
    return _deepfake_detector_instance
