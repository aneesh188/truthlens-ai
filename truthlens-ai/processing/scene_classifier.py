"""
TruthLens AI - Scene Forensic Classifier & Media Taxonomy Engine
Categorizes video frames into semantic forensic categories:
1. Face Deepfakes & Reenactment
2. Fully AI-Generated Landscapes & Environments
3. AI-Generated Synthetic Humans
4. AI-Generated Animation & 3D Visuals
5. AI Scene Manipulation & Visual Inpainting
"""

import cv2
import numpy as np
from typing import Dict, Any, List


CATEGORIES = [
    "Face Deepfake & Reenactment",
    "Fully AI-Generated Landscape / Nature",
    "AI Architecture & Urban Environment",
    "AI-Generated Human & Movement",
    "AI Animation & 3D CGI",
    "AI Scene Manipulation / Inpainting",
    "Authentic Unmanipulated Footage"
]


class SceneForensicClassifier:
    """
    Analyzes visual structure, edge density, color histograms, and facial presence
    to categorize video content into the 5 core forensic taxonomies.
    """

    def __init__(self):
        pass

    def classify_frame(
        self,
        frame_rgb: np.ndarray,
        faces_count: int,
        synthetic_prob: float,
        face_fake_prob: float = 0.0,
        temporal_anomaly: float = 0.0
    ) -> Dict[str, Any]:
        """
        Determine the most appropriate forensic category for a single frame.
        """
        # If not suspicious
        if synthetic_prob < 0.45 and face_fake_prob < 0.45 and temporal_anomaly < 0.50:
            return {
                "category": "Authentic Unmanipulated Footage",
                "confidence": round(1.0 - max(synthetic_prob, face_fake_prob, temporal_anomaly * 0.5), 3),
                "is_suspicious": False
            }

        # Case 1: Human faces with manipulation evidence
        if faces_count > 0 and face_fake_prob > 0.48:
            return {
                "category": "Face Deepfake & Reenactment",
                "confidence": round(face_fake_prob, 3),
                "is_suspicious": True
            }

        # Analyze scene visual characteristics (Color, Edges, Texture)
        hsv = cv2.cvtColor(frame_rgb, cv2.COLOR_RGB2HSV)
        sat_mean = np.mean(hsv[:, :, 1])
        gray = cv2.cvtColor(frame_rgb, cv2.COLOR_RGB2GRAY)
        
        edges = cv2.Canny(gray, 60, 160)
        edge_density = float(np.sum(edges > 0) / (gray.shape[0] * gray.shape[1]))
        
        # Color distribution (Green/Blue for landscape, Grayscale/Urban for city)
        r_mean = np.mean(frame_rgb[:, :, 0])
        g_mean = np.mean(frame_rgb[:, :, 1])
        b_mean = np.mean(frame_rgb[:, :, 2])

        # Case 2: Animation / 3D Characters (High saturation, strong black contours, cartoon palette)
        if sat_mean > 130 and edge_density > 0.07:
            category = "AI Animation & 3D CGI"
            conf = max(synthetic_prob, 0.72)
        # Case 3: Faces detected but high synthetic frame score without localized face swap -> Synthetic human
        elif faces_count > 0 and synthetic_prob > 0.50:
            category = "AI-Generated Human & Movement"
            conf = max(synthetic_prob, 0.75)
        # Case 4: Nature / Landscape (Dominant greens/blues, natural horizons)
        elif (g_mean > r_mean + 10 or b_mean > r_mean + 15) and edge_density < 0.12:
            category = "Fully AI-Generated Landscape / Nature"
            conf = max(synthetic_prob, 0.70)
        # Case 5: Architecture / Cities (High geometric line density, neutral tones)
        elif edge_density > 0.09 and abs(r_mean - b_mean) < 25:
            category = "AI Architecture & Urban Environment"
            conf = max(synthetic_prob, 0.68)
        # Case 6: Scene Manipulation / Background Inpainting
        elif temporal_anomaly > 0.55:
            category = "AI Scene Manipulation / Inpainting"
            conf = max(synthetic_prob, temporal_anomaly)
        else:
            category = "Fully AI-Generated Environment"
            conf = synthetic_prob

        return {
            "category": category,
            "confidence": round(float(conf), 3),
            "is_suspicious": True
        }

    def aggregate_video_taxonomy(self, frame_classifications: List[Dict[str, Any]]) -> str:
        """
        Aggregate individual frame categories into a dominant video category.
        """
        suspicious_frames = [f for f in frame_classifications if f["is_suspicious"]]
        if not suspicious_frames:
            return "Authentic Unmanipulated Footage"

        # Count frequencies of suspicious categories
        counts = {}
        for f in suspicious_frames:
            cat = f["category"]
            counts[cat] = counts.get(cat, 0) + 1

        # Return category with highest votes
        dominant = max(counts.items(), key=lambda x: x[1])[0]
        return dominant
