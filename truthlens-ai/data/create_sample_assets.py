"""
TruthLens AI - Sample Asset Generator
Generates sample images for immediate local testing of image forensics.
"""

from PIL import Image, ImageDraw
import numpy as np
import os

DATA_DIR = os.path.dirname(os.path.abspath(__file__))

def create_sample_images():
    """Create sample images for hackathon demonstration."""
    # 1. Natural scene style sample
    img_real = Image.new("RGB", (400, 400), color=(30, 80, 150))
    draw_real = ImageDraw.Draw(img_real)
    draw_real.ellipse((100, 100, 300, 300), fill=(220, 180, 140), outline=(255, 255, 255))
    draw_real.rectangle((140, 180, 180, 200), fill=(40, 40, 40))
    draw_real.rectangle((220, 180, 260, 200), fill=(40, 40, 40))
    draw_real.line((200, 210, 200, 240), fill=(180, 100, 80), width=4)
    draw_real.arc((160, 240, 240, 270), start=0, end=180, fill=(180, 50, 50), width=4)
    img_real.save(os.path.join(DATA_DIR, "sample_portrait.png"))

    # 2. High-frequency digital noise artifact sample
    noise = np.random.randint(0, 256, (400, 400, 3), dtype=np.uint8)
    img_noise = Image.fromarray(noise)
    img_noise.save(os.path.join(DATA_DIR, "sample_synthetic_artifact.png"))
    
    print("Sample test assets generated in data/ folder.")

if __name__ == "__main__":
    create_sample_images()
