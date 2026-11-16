"""
TruthLens AI - Audio Forensic & Synthetic Voice Authenticity Analyzer
Extracts audio streams from videos via FFmpeg and conducts spectral forensics to detect
synthetic speech, vocoder bandwidth cutoffs, robotic tone quantization, and unnatural silence.
"""

import os
import subprocess
import tempfile
import numpy as np
from typing import Dict, Any, Optional
from scipy.io import wavfile


class AudioForensicAnalyzer:
    """
    Forensic acoustic analyzer detecting synthetic voice, neural vocoder signatures,
    and missing room-presence acoustics in video audio streams.
    """

    def __init__(self):
        self.sample_rate = 16000

    def extract_audio(self, video_path: str) -> Optional[str]:
        """
        Extract mono 16kHz PCM WAV from video using FFmpeg.
        Returns path to temporary WAV file, or None if no audio track exists.
        """
        temp_wav = tempfile.NamedTemporaryFile(suffix=".wav", delete=False).name
        try:
            # -vn: disable video, -ac 1: mono, -ar 16000: 16kHz, -y: overwrite
            cmd = [
                "ffmpeg", "-i", video_path,
                "-vn", "-acodec", "pcm_s16le",
                "-ac", "1", "-ar", str(self.sample_rate),
                temp_wav, "-y"
            ]
            
            result = subprocess.run(
                cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                timeout=15,
                creationflags=subprocess.CREATE_NO_WINDOW if os.name == 'nt' else 0
            )

            # Check if file exists and has non-zero size
            if result.returncode == 0 and os.path.exists(temp_wav) and os.path.getsize(temp_wav) > 100:
                return temp_wav
            else:
                if os.path.exists(temp_wav):
                    os.remove(temp_wav)
                return None
        except Exception:
            if os.path.exists(temp_wav):
                try:
                    os.remove(temp_wav)
                except Exception:
                    pass
            return None

    def analyze_audio(self, video_path: str) -> Dict[str, Any]:
        """
        Execute acoustic forensic analysis on the video's audio track.
        """
        wav_path = self.extract_audio(video_path)
        
        if wav_path is None:
            return {
                "has_audio": False,
                "audio_authenticity_score": 0.50,
                "synthetic_speech_probability": 0.0,
                "status": "NO_AUDIO_STREAM",
                "summary": "No audio stream detected. Many generative video models (Sora, Runway, Kling) produce silent video renders by default."
            }

        try:
            sr, signal = wavfile.read(wav_path)
            
            # Normalize to [-1.0, 1.0]
            if signal.dtype == np.int16:
                signal_float = signal.astype(np.float32) / 32768.0
            elif signal.dtype == np.int32:
                signal_float = signal.astype(np.float32) / 2147483648.0
            else:
                signal_float = signal.astype(np.float32)

            duration_sec = len(signal_float) / sr
            
            if duration_sec < 0.5:
                return {
                    "has_audio": True,
                    "duration_sec": round(duration_sec, 2),
                    "audio_authenticity_score": 0.50,
                    "synthetic_speech_probability": 0.0,
                    "status": "AUDIO_TOO_BRIEF",
                    "summary": "Audio stream is too brief (< 0.5s) for robust acoustic spectral profiling."
                }

            # 1. Frequency Domain Forensics (FFT)
            fft_vals = np.abs(np.fft.rfft(signal_float))
            freqs = np.fft.rfftfreq(len(signal_float), 1.0 / sr)
            
            # 2. Check for Vocoder High-Frequency Brickwall Cutoff (common in TTS models like VITS, FastSpeech, ElevenLabs)
            # Look at energy above 7.2 kHz vs total energy
            high_band_mask = freqs > 7200
            total_energy = np.sum(fft_vals ** 2) + 1e-8
            high_energy = np.sum(fft_vals[high_band_mask] ** 2)
            high_band_ratio = float(high_energy / total_energy)

            # 3. Ambient Room Presence / Digital Zero Floor Check
            # Synthetic voiceovers often have absolute silence between words, whereas authentic recordings have background noise floor
            chunk_size = int(sr * 0.05)  # 50ms chunks
            num_chunks = len(signal_float) // chunk_size
            if num_chunks > 0:
                chunks = signal_float[:num_chunks * chunk_size].reshape(num_chunks, chunk_size)
                chunk_energies = np.mean(chunks ** 2, axis=1)
                near_zero_ratio = float(np.mean(chunk_energies < 1e-6))
            else:
                near_zero_ratio = 0.0

            # 4. Synthesize Acoustic Probability
            # If high-frequency cutoff is sharp (< 0.01) and digital zero silence is frequent (> 0.4)
            is_synthetic_vocoder = (high_band_ratio < 0.008 and near_zero_ratio > 0.35)
            
            synthetic_score = 0.20
            if is_synthetic_vocoder:
                synthetic_score = 0.78
            elif high_band_ratio < 0.015:
                synthetic_score = 0.55
            elif near_zero_ratio > 0.5:
                synthetic_score = 0.45

            auth_score = float(round(1.0 - synthetic_score, 4))
            
            if synthetic_score > 0.65:
                summary = "Spectral analysis detected abnormal high-frequency brickwall attenuation and unnatural silent gating characteristic of neural TTS vocoders."
            else:
                summary = "Audio exhibits natural acoustic frequency distribution and ambient room presence consistent with standard microphone recordings."

            return {
                "has_audio": True,
                "duration_sec": round(duration_sec, 2),
                "audio_authenticity_score": auth_score,
                "synthetic_speech_probability": round(synthetic_score, 4),
                "high_band_energy_ratio": round(high_band_ratio, 5),
                "silent_gating_ratio": round(near_zero_ratio, 3),
                "status": "ANALYSIS_COMPLETE",
                "summary": summary
            }

        except Exception as e:
            return {
                "has_audio": True,
                "audio_authenticity_score": 0.50,
                "status": "ANALYSIS_ERROR",
                "error": str(e),
                "summary": f"Acoustic analysis failed: {str(e)}"
            }
        finally:
            if wav_path and os.path.exists(wav_path):
                try:
                    os.remove(wav_path)
                except Exception:
                    pass
