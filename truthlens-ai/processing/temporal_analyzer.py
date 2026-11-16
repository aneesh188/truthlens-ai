"""
TruthLens AI - Temporal Video Coherence & Motion Forensic Analyzer
Inspects inter-frame consistency, optical flow divergence, structural jitter (SSIM drift),
and frequency flickering typical of generative diffusion and video synthesis models.
"""

import cv2
import numpy as np
from typing import List, Dict, Any, Tuple


class TemporalForensicAnalyzer:
    """
    Evaluates temporal stability across consecutive video frames to detect
    generative frame warping, texture morphing, and unnatural flow fields.
    """

    def __init__(self):
        pass

    def compute_frame_difference(self, prev_gray: np.ndarray, curr_gray: np.ndarray) -> float:
        """Calculate normalized mean absolute pixel divergence between consecutive frames."""
        diff = cv2.absdiff(prev_gray, curr_gray)
        return float(np.mean(diff) / 255.0)

    def compute_optical_flow_divergence(self, prev_gray: np.ndarray, curr_gray: np.ndarray) -> Tuple[float, float]:
        """
        Compute Farneback dense optical flow and measure magnitude variance and flow roughness.
        Generative video models often have erratic local motion vectors and non-physical warping.
        """
        # Downscale for fast temporal computation
        h, w = prev_gray.shape[:2]
        small_prev = cv2.resize(prev_gray, (160, 120), interpolation=cv2.INTER_AREA)
        small_curr = cv2.resize(curr_gray, (160, 120), interpolation=cv2.INTER_AREA)

        flow = cv2.calcOpticalFlowFarneback(
            small_prev, small_curr, None,
            pyr_scale=0.5, levels=3, winsize=15,
            iterations=3, poly_n=5, poly_sigma=1.2, flags=0
        )

        mag, ang = cv2.cartToPolar(flow[..., 0], flow[..., 1])
        mean_mag = float(np.mean(mag))
        std_mag = float(np.std(mag))
        
        # Flow divergence / angular entropy (higher = erratic, non-physical vector field)
        flow_roughness = float(std_mag / (mean_mag + 1e-5))
        return mean_mag, flow_roughness

    def compute_high_frequency_flicker(self, gray_frame: np.ndarray) -> float:
        """
        Measure 2D frequency power spectrum in high bands via FFT.
        Generative diffusion models introduce periodic checkerboard or noise fluctuations in high frequencies.
        """
        f = np.fft.fft2(gray_frame)
        fshift = np.fft.fftshift(f)
        magnitude_spectrum = 20 * np.log(np.abs(fshift) + 1e-5)
        
        h, w = gray_frame.shape
        cy, cx = h // 2, w // 2
        
        # High frequency outer perimeter
        outer_mask = np.ones((h, w), dtype=bool)
        cv2.circle(outer_mask.view(np.uint8), (cx, cy), min(cx, cy) // 2, 0, -1)
        
        high_freq_power = float(np.mean(magnitude_spectrum[outer_mask]))
        return high_freq_power

    def analyze_sequence(self, frames_rgb: List[np.ndarray], timestamps: List[float]) -> Dict[str, Any]:
        """
        Analyze a temporal sequence of extracted video frames (RGB).
        Returns overall temporal inconsistency score and frame-by-frame motion metrics.
        """
        if len(frames_rgb) < 2:
            return {
                "temporal_inconsistency_score": 0.15,
                "confidence": 0.5,
                "motion_smoothness": 1.0,
                "flicker_index": 0.0,
                "frame_metrics": []
            }

        grays = [cv2.cvtColor(f, cv2.COLOR_RGB2GRAY) for f in frames_rgb]
        
        frame_metrics = []
        flow_roughness_list = []
        pixel_diffs = []
        hf_powers = [self.compute_high_frequency_flicker(g) for g in grays]

        for i in range(len(grays) - 1):
            prev_g = grays[i]
            curr_g = grays[i + 1]
            
            p_diff = self.compute_frame_difference(prev_g, curr_g)
            mean_mag, flow_roughness = self.compute_optical_flow_divergence(prev_g, curr_g)
            
            pixel_diffs.append(p_diff)
            flow_roughness_list.append(flow_roughness)
            
            hf_shift = abs(hf_powers[i + 1] - hf_powers[i])
            
            # Anomaly indicator: high flow roughness + irregular high-frequency texture drift
            frame_anomaly_score = float(np.clip(
                (flow_roughness * 0.45) + (p_diff * 1.5) + (hf_shift * 0.05),
                0.0, 1.0
            ))

            frame_metrics.append({
                "from_index": i,
                "to_index": i + 1,
                "timestamp_sec": timestamps[i],
                "pixel_divergence": round(p_diff, 4),
                "motion_magnitude": round(mean_mag, 3),
                "flow_roughness": round(flow_roughness, 3),
                "texture_flicker": round(hf_shift, 3),
                "temporal_anomaly_score": round(frame_anomaly_score, 4)
            })

        # Aggregated temporal inconsistency
        avg_roughness = float(np.mean(flow_roughness_list)) if flow_roughness_list else 0.0
        avg_diff = float(np.mean(pixel_diffs)) if pixel_diffs else 0.0
        std_hf = float(np.std(hf_powers)) if hf_powers else 0.0
        
        # Calibrate temporal score between 0.0 and 1.0
        # AI videos (Sora/Runway/Pika) usually have roughness > 1.2 and high texture variance
        raw_score = (avg_roughness * 0.35) + (avg_diff * 2.0) + (std_hf * 0.08)
        temporal_score = float(np.clip(raw_score, 0.05, 0.95))

        return {
            "temporal_inconsistency_score": round(temporal_score, 4),
            "flow_roughness": round(avg_roughness, 4),
            "texture_jitter_std": round(std_hf, 4),
            "average_frame_divergence": round(avg_diff, 4),
            "frame_metrics": frame_metrics
        }
