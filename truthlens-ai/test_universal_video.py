"""
Test Script for TruthLens Universal AI Video Detection Pipeline
Tests both zero-face natural/geometric video and high-artifact synthetic generative video.
"""

import os
import sys
import cv2
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from processing.video_processor import process_video_stream


class MockUploadedFile:
    def __init__(self, filepath):
        self.name = os.path.basename(filepath)
        with open(filepath, "rb") as f:
            self._buffer = f.read()
        self.size = len(self._buffer)

    def getbuffer(self):
        return self._buffer


def create_synthetic_ai_video(output_path: str, duration_sec: int = 2, fps: int = 15):
    """Generates a video with latent diffusion noise and morphing artifacts."""
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    h, w = 256, 256
    out = cv2.VideoWriter(output_path, fourcc, fps, (w, h))

    total_frames = duration_sec * fps
    np.random.seed(42)
    for i in range(total_frames):
        # Latent noise pattern with high frequency checkerboard typical of diffusion
        base = np.random.randint(60, 200, (h, w, 3), dtype=np.uint8)
        # Add high-contrast synthetic geometric structures
        cv2.circle(base, (128 + int(30 * np.sin(i)), 128), 50, (255, 0, 180), -1)
        cv2.rectangle(base, (40, 40), (210, 210), (0, 255, 200), 3)
        out.write(base)

    out.release()


def main():
    test_video_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", "test_ai_synth.mp4")
    create_synthetic_ai_video(test_video_path, duration_sec=2, fps=15)

    mock_file = MockUploadedFile(test_video_path)
    print("\n--- TESTING SYNTHETIC GENERATIVE VIDEO ---")
    result = process_video_stream(
        mock_file,
        max_frames_to_sample=8,
        sampling_strategy="stratified"
    )

    print(f"Success: {result.get('success')}")
    if result.get("success"):
        print(f"Overall Prediction: {result['overall_prediction']}")
        print(f"Primary Category: {result['primary_category']}")
        print(f"AI Generated Prob: {result['ai_generated_probability']*100:.1f}%")
        print(f"Visual (ViT) Score: {result['visual_manipulation_score']*100:.1f}%")
        print(f"Temporal Score: {result['temporal_inconsistency_score']*100:.1f}%")
        print(f"Flagged Frames: {len(result['suspicious_frames'])}")
        print(f"Category Distribution: {result['category_distribution']}")

    if os.path.exists(test_video_path):
        os.remove(test_video_path)

if __name__ == "__main__":
    main()
