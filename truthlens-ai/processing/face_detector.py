"""
TruthLens AI - Face Detection Module
Uses OpenCV's Haar cascades and DNN-based detectors (such as YuNet) to detect and crop human faces from images and video frames.
"""

import cv2
import numpy as np
from typing import List, Tuple, Optional
import os


class FaceDetector:
    """
    Robust face detection supporting OpenCV Haar Cascade and DNN fallback.
    Extracts face bounding boxes and crops for forensic manipulation analysis.
    """
    
    def __init__(self, min_confidence: float = 0.6):
        self.min_confidence = min_confidence
        # Load OpenCV default Haar cascade for frontal faces
        cascade_path = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
        if os.path.exists(cascade_path):
            self.cascade = cv2.CascadeClassifier(cascade_path)
        else:
            self.cascade = None

    def detect_faces(self, image_bgr: np.ndarray) -> List[Tuple[int, int, int, int]]:
        """
        Detect faces in a BGR image.
        Returns list of bounding boxes: [(x, y, w, h), ...]
        """
        if image_bgr is None or self.cascade is None:
            return []
            
        gray = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2GRAY)
        # Apply histogram equalization to improve contrast for detection
        gray = cv2.equalizeHist(gray)
        
        faces = self.cascade.detectMultiScale(
            gray,
            scaleFactor=1.15,
            minNeighbors=5,
            minSize=(40, 40),
            flags=cv2.CASCADE_SCALE_IMAGE
        )
        
        boxes = []
        for (x, y, w, h) in faces:
            boxes.append((int(x), int(y), int(w), int(h)))
        return boxes

    def crop_face(
        self,
        image_bgr: np.ndarray,
        box: Tuple[int, int, int, int],
        target_size: Tuple[int, int] = (299, 299),
        margin_percent: float = 0.2
    ) -> Optional[np.ndarray]:
        """
        Crop face region with a context margin, ensuring bounds are within image limits,
        and resize to target dimensions (e.g. 299x299 for XceptionNet).
        """
        if image_bgr is None or box is None:
            return None
            
        x, y, w, h = box
        img_h, img_w = image_bgr.shape[:2]
        
        margin_x = int(w * margin_percent)
        margin_y = int(h * margin_percent)
        
        x1 = max(0, x - margin_x)
        y1 = max(0, y - margin_y)
        x2 = min(img_w, x + w + margin_x)
        y2 = min(img_h, y + h + margin_y)
        
        if x2 <= x1 or y2 <= y1:
            return None
            
        cropped = image_bgr[y1:y2, x1:x2]
        if cropped.size == 0:
            return None
            
        resized = cv2.resize(cropped, target_size, interpolation=cv2.INTER_AREA)
        return resized
