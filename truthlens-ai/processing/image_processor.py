"""
TruthLens AI - Image Processing Module
Validates, inspects, and normalizes image files for forensic analysis.
"""

import os
from typing import Tuple, Optional, Dict, Any
from PIL import Image, ImageOps
import numpy as np


ALLOWED_EXTENSIONS = {".jpg", ".jpeg", ".png"}
MAX_IMAGE_FILE_SIZE_MB = 20


def validate_image_file(uploaded_file) -> Tuple[bool, str]:
    """
    Validate uploaded image for size and supported format.
    """
    if uploaded_file is None:
        return False, "No file uploaded."
        
    ext = os.path.splitext(uploaded_file.name)[1].lower()
    if ext not in ALLOWED_EXTENSIONS:
        return False, f"Unsupported file format '{ext}'. Allowed: {', '.join(ALLOWED_EXTENSIONS)}"
        
    file_size_mb = uploaded_file.size / (1024 * 1024)
    if file_size_mb > MAX_IMAGE_FILE_SIZE_MB:
        return False, f"File size exceeds {MAX_IMAGE_FILE_SIZE_MB}MB limit ({file_size_mb:.1f}MB)."
        
    return True, "Valid"


def load_image_for_analysis(uploaded_file) -> Tuple[Optional[Image.Image], Optional[Dict[str, Any]], str]:
    """
    Safely load an uploaded image into a PIL Image (RGB) and extract forensic metadata.
    """
    valid, msg = validate_image_file(uploaded_file)
    if not valid:
        return None, None, msg
        
    try:
        image = Image.open(uploaded_file)
        # Correct orientation based on EXIF tag if available
        image = ImageOps.exif_transpose(image)
        # Convert to RGB
        if image.mode != "RGB":
            image = image.convert("RGB")
            
        metadata = {
            "format": uploaded_file.type or "image/jpeg",
            "dimensions": f"{image.width} x {image.height}",
            "mode": image.mode,
            "filename": uploaded_file.name,
            "filesize_kb": round(uploaded_file.size / 1024, 2)
        }
        return image, metadata, "Success"
    except Exception as e:
        return None, None, f"Failed to decode image: {str(e)}"
