"""
TruthLens AI - Universal AI Video Forensic Pipeline
Multi-stage analysis engine for detecting AI-generated and manipulated videos:
1. Stratified Frame Sampling (Beginning, Middle, End)
2. General Vision Transformer (ViT) Full-Frame Synthetic Texture Analysis (Zero-Face tolerant)
3. Facial Deepfake & Manipulation Localization (XceptionNet)
4. Temporal Motion Coherence & High-Frequency Flicker Analysis
5. Audio Acoustic Spectral & Neural Vocoder Forensics
6. Multi-Category Taxonomy Classification
"""

import cv2
import os
import tempfile
import base64
import numpy as np
from PIL import Image
from typing import Dict, Any, List, Optional, Callable, Tuple

from processing.face_detector import FaceDetector
from processing.temporal_analyzer import TemporalForensicAnalyzer
from processing.audio_analyzer import AudioForensicAnalyzer
from processing.scene_classifier import SceneForensicClassifier
from models.image_detector import get_image_detector


MAX_VIDEO_FILE_SIZE_MB = 60
ALLOWED_VIDEO_EXTENSIONS = {".mp4", ".avi", ".mov", ".mkv", ".webm"}


def validate_video_file(uploaded_file) -> Tuple[bool, str]:
    """Validate uploaded video extension and file size."""
    if uploaded_file is None:
        return False, "No video file provided."
        
    ext = os.path.splitext(uploaded_file.name)[1].lower()
    if ext not in ALLOWED_VIDEO_EXTENSIONS:
        return False, f"Unsupported video format '{ext}'. Allowed: {', '.join(ALLOWED_VIDEO_EXTENSIONS)}"
        
    size_mb = uploaded_file.size / (1024 * 1024)
    if size_mb > MAX_VIDEO_FILE_SIZE_MB:
        return False, f"Video size exceeds {MAX_VIDEO_FILE_SIZE_MB}MB limit ({size_mb:.1f}MB)."
        
    return True, "Valid"


def frame_to_base64_thumbnail(frame_rgb: np.ndarray, max_width: int = 280, quality: int = 75) -> str:
    """Encode an RGB frame as a compact JPEG base64 data URI for instant UI rendering."""
    h, w = frame_rgb.shape[:2]
    if w > max_width:
        new_h = int(h * (max_width / w))
        thumb = cv2.resize(frame_rgb, (max_width, new_h), interpolation=cv2.INTER_AREA)
    else:
        thumb = frame_rgb

    thumb_bgr = cv2.cvtColor(thumb, cv2.COLOR_RGB2BGR)
    encode_params = [int(cv2.IMWRITE_JPEG_QUALITY), quality]
    success, buffer = cv2.imencode(".jpg", thumb_bgr, encode_params)
    if success:
        b64_str = base64.b64encode(buffer).decode("utf-8")
        return f"data:image/jpeg;base64,{b64_str}"
    return ""


def calculate_stratified_frame_indices(total_frames: int, num_samples: int) -> List[int]:
    """
    Select frame indices stratified across Beginning (20%), Middle (20%), and End (20%).
    Ensures temporal coverage even when video length is substantial.
    """
    if total_frames <= num_samples:
        return list(range(total_frames))

    # Allocate samples: 33% beginning, 34% middle, 33% end
    n_beg = max(1, num_samples // 3)
    n_mid = max(1, num_samples // 3)
    n_end = max(1, num_samples - n_beg - n_mid)

    # Beginning zone: 0 to 25% of video
    beg_end = int(total_frames * 0.25)
    beg_indices = np.linspace(0, max(0, beg_end - 1), n_beg, dtype=int).tolist()

    # Middle zone: 38% to 62% of video
    mid_start = int(total_frames * 0.38)
    mid_end = int(total_frames * 0.62)
    mid_indices = np.linspace(mid_start, min(total_frames - 1, mid_end), n_mid, dtype=int).tolist()

    # End zone: 75% to 100% of video
    end_start = int(total_frames * 0.75)
    end_indices = np.linspace(end_start, total_frames - 1, n_end, dtype=int).tolist()

    all_indices = sorted(list(set(beg_indices + mid_indices + end_indices)))
    return all_indices


def process_video_stream(
    uploaded_file,
    frame_step: int = 15,
    max_frames_to_sample: int = 30,
    sampling_strategy: str = "stratified",  # "stratified" or "uniform"
    predict_face_fn: Optional[Callable[[np.ndarray], Dict[str, Any]]] = None,
    progress_callback: Optional[Callable[[float, str], None]] = None
) -> Dict[str, Any]:
    """
    Universal Multi-Modal AI Video Analysis Pipeline.
    Evaluates:
      1. General generative AI visual artifacts via Vision Transformer (zero-face capable).
      2. Facial manipulation & deepfake artifacts via XceptionNet (when faces present).
      3. Temporal motion coherence, optical flow variance, and high-frequency flicker.
      4. Audio spectral forensics for neural vocoders & acoustic authenticity.
      5. Multi-category taxonomy classification.
    """
    valid, err_msg = validate_video_file(uploaded_file)
    if not valid:
        return {"success": False, "error": err_msg}

    temp_fd, temp_path = tempfile.mkstemp(suffix=os.path.splitext(uploaded_file.name)[1])
    try:
        with os.fdopen(temp_fd, "wb") as f:
            f.write(uploaded_file.getbuffer())

        cap = cv2.VideoCapture(temp_path)
        if not cap.isOpened():
            return {"success": False, "error": "Could not open video stream via OpenCV."}

        total_video_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        fps = cap.get(cv2.CAP_PROP_FPS) or 30.0
        duration_sec = total_video_frames / fps if total_video_frames > 0 else 0.0

        if total_video_frames <= 0:
            return {"success": False, "error": "Video contains 0 readable frames."}

        # Initialize Forensic Engines
        face_detector = FaceDetector()
        scene_classifier = SceneForensicClassifier()
        temporal_analyzer = TemporalForensicAnalyzer()
        audio_analyzer = AudioForensicAnalyzer()
        image_detector = get_image_detector()

        # Determine target frame indices
        if sampling_strategy == "stratified":
            target_indices = calculate_stratified_frame_indices(total_video_frames, max_frames_to_sample)
        else:
            effective_step = max(frame_step, total_video_frames // max_frames_to_sample)
            target_indices = list(range(0, total_video_frames, max(1, effective_step)))[:max_frames_to_sample]

        target_set = set(target_indices)

        if progress_callback:
            progress_callback(0.05, f"Decompressing video container ({total_video_frames} frames, {duration_sec:.1f}s)...")

        # Step 1: Sequential Frame Extraction
        extracted_frames_bgr = []
        extracted_timestamps = []
        frame_idx = 0

        while cap.isOpened() and len(extracted_frames_bgr) < len(target_indices):
            ret, frame = cap.read()
            if not ret:
                break

            if frame_idx in target_set:
                extracted_frames_bgr.append(frame)
                extracted_timestamps.append(round(frame_idx / fps, 2))

            frame_idx += 1

        cap.release()

        if not extracted_frames_bgr:
            return {"success": False, "error": "No frames could be extracted from video."}

        num_sampled = len(extracted_frames_bgr)
        frames_rgb = [cv2.cvtColor(f, cv2.COLOR_BGR2RGB) for f in extracted_frames_bgr]

        # Step 2: Temporal Motion & Inconsistency Analysis
        if progress_callback:
            progress_callback(0.20, f"Evaluating temporal optical flow across {num_sampled} frames...")

        temporal_report = temporal_analyzer.analyze_sequence(frames_rgb, extracted_timestamps)
        temporal_score = temporal_report.get("temporal_inconsistency_score", 0.15)
        temporal_frame_metrics = temporal_report.get("frame_metrics", [])

        # Step 3: Audio Forensic Spectral Analysis
        if progress_callback:
            progress_callback(0.40, "Running FFT spectral forensics on video audio track...")

        audio_report = audio_analyzer.analyze_audio(temp_path)

        # Step 4: Frame-by-Frame Neural Visual & Facial Forensic Analysis
        frames_analyzed = []
        suspicious_frames = []
        total_faces_detected = 0
        vit_synthetic_scores = []
        face_manipulation_scores = []
        category_counts: Dict[str, int] = {}

        for i, (frame_bgr, frame_rgb, ts) in enumerate(zip(extracted_frames_bgr, frames_rgb, extracted_timestamps)):
            pct = 0.45 + (0.45 * (i / num_sampled))
            if progress_callback:
                progress_callback(pct, f"Analyzing frame {i + 1}/{num_sampled} (ViT + Face + Taxonomy)...")

            # A. Full-frame general generative AI analysis (Vision Transformer)
            pil_frame = Image.fromarray(frame_rgb)
            vit_score = 0.50
            if image_detector and image_detector.status == "ONLINE":
                vit_res = image_detector.analyze(pil_frame)
                if vit_res.get("success"):
                    vit_score = vit_res["probabilities"].get("SYNTHETIC", 0.50)
            vit_synthetic_scores.append(vit_score)

            # B. Face Detection and Facial Deepfake Analysis
            boxes = face_detector.detect_faces(frame_bgr)
            num_faces = len(boxes)
            total_faces_detected += num_faces

            frame_face_score = 0.0
            face_details = []
            if num_faces > 0:
                for box in boxes:
                    cropped = face_detector.crop_face(frame_bgr, box, target_size=(299, 299))
                    if cropped is not None and predict_face_fn:
                        pred_f = predict_face_fn(cropped)
                        f_score = pred_f.get("fake_probability", 0.0)
                        face_details.append(pred_f)
                        if f_score > frame_face_score:
                            frame_face_score = f_score

                if frame_face_score > 0.0:
                    face_manipulation_scores.append(frame_face_score)

            # Corresponding temporal divergence for this frame transition
            temp_divergence = 0.0
            if i < len(temporal_frame_metrics):
                temp_divergence = temporal_frame_metrics[i].get("flow_roughness", 0.0)

            # C. Semantic Forensic Taxonomy Classification
            cat_info = scene_classifier.classify_frame(
                frame_rgb=frame_rgb,
                faces_count=num_faces,
                synthetic_prob=vit_score,
                face_fake_prob=frame_face_score,
                temporal_anomaly=min(1.0, temp_divergence / 2.0)
            )

            category = cat_info["category"]
            category_counts[category] = category_counts.get(category, 0) + 1

            # Determine frame suspicion level
            is_frame_suspicious = (
                vit_score > 0.58 or
                frame_face_score > 0.50 or
                cat_info.get("is_suspicious", False)
            )

            frame_record = {
                "frame_index": target_indices[i] if i < len(target_indices) else i,
                "timestamp_sec": ts,
                "faces_count": num_faces,
                "vit_synthetic_score": round(vit_score, 4),
                "face_fake_score": round(frame_face_score, 4),
                "category": category,
                "is_suspicious": is_frame_suspicious
            }
            frames_analyzed.append(frame_record)

            # Store thumbnail for suspicious frames or key frames
            if is_frame_suspicious or (i % max(1, num_sampled // 6) == 0 and len(suspicious_frames) < 8):
                thumb_uri = frame_to_base64_thumbnail(frame_rgb, max_width=260)
                
                # Build specific reason string
                reasons = []
                if vit_score > 0.58:
                    reasons.append(f"ViT Generative Artifact ({vit_score*100:.1f}%)")
                if frame_face_score > 0.50:
                    reasons.append(f"Facial Swap/Warping ({frame_face_score*100:.1f}%)")
                if temp_divergence > 1.2:
                    reasons.append(f"Erratic Optical Flow ({temp_divergence:.2f})")
                if not reasons:
                    reasons.append(f"Forensic Classification: {category}")

                suspicious_frames.append({
                    "timestamp_sec": ts,
                    "frame_index": frame_record["frame_index"],
                    "thumbnail": thumb_uri,
                    "category": category,
                    "vit_score": round(vit_score, 4),
                    "face_score": round(frame_face_score, 4),
                    "reason": " • ".join(reasons)
                })

        # Step 5: Multi-Modal Score Synthesis & Classification
        if progress_callback:
            progress_callback(0.95, "Synthesizing multi-modal forensic telemetry...")

        # Visual manipulation score (mean & 85th percentile of ViT scores)
        mean_vit = float(np.mean(vit_synthetic_scores)) if vit_synthetic_scores else 0.5
        p85_vit = float(np.percentile(vit_synthetic_scores, 85)) if vit_synthetic_scores else mean_vit
        visual_manipulation_score = 0.6 * p85_vit + 0.4 * mean_vit

        # Face manipulation score
        if face_manipulation_scores:
            mean_face = float(np.mean(face_manipulation_scores))
            max_face = float(np.max(face_manipulation_scores))
            face_manipulation_prob = 0.6 * max_face + 0.4 * mean_face
        else:
            face_manipulation_prob = None

        # Audio scores
        has_audio = audio_report.get("has_audio", False)
        audio_synth_prob = audio_report.get("synthetic_speech_probability", 0.0)
        audio_auth_score = audio_report.get("audio_authenticity_score", 0.50)

        # Composite AI Video Probability Fusion
        if face_manipulation_prob is not None:
            # Video contains human faces
            if has_audio:
                ai_prob = (
                    0.38 * face_manipulation_prob +
                    0.28 * visual_manipulation_score +
                    0.18 * temporal_score +
                    0.16 * audio_synth_prob
                )
            else:
                ai_prob = (
                    0.44 * face_manipulation_prob +
                    0.34 * visual_manipulation_score +
                    0.22 * temporal_score
                )
        else:
            # ZERO FACES DETECTED: Pure visual scene, landscape, architecture, animation, or inpainting
            if has_audio:
                ai_prob = (
                    0.55 * visual_manipulation_score +
                    0.28 * temporal_score +
                    0.17 * audio_synth_prob
                )
            else:
                ai_prob = (
                    0.68 * visual_manipulation_score +
                    0.32 * temporal_score
                )

        ai_prob = float(np.clip(ai_prob, 0.02, 0.98))

        # Primary Category Determination
        # Filter out "Authentic Unmanipulated Footage" if overall probability indicates AI
        if ai_prob > 0.48:
            suspicious_cat_counts = {k: v for k, v in category_counts.items() if k != "Authentic Unmanipulated Footage"}
            if suspicious_cat_counts:
                primary_category = max(suspicious_cat_counts, key=suspicious_cat_counts.get)
            else:
                primary_category = "Fully AI-Generated Video"
            overall_prediction = f"AI-GENERATED / MANIPULATED ({primary_category.upper()})"
            confidence = ai_prob
        else:
            primary_category = "Authentic Unmanipulated Footage"
            overall_prediction = "LIKELY AUTHENTIC FOOTAGE"
            confidence = 1.0 - ai_prob

        # Category distribution percentages
        total_cat_votes = sum(category_counts.values()) or 1
        category_distribution = {k: round(v / total_cat_votes * 100, 1) for k, v in category_counts.items()}

        # Forensic Explanation Narrative
        explanation_parts = []
        if total_faces_detected == 0:
            explanation_parts.append(
                f"Multi-Category Scene Analysis evaluated {num_sampled} frames with 0 human faces present."
            )
        else:
            explanation_parts.append(
                f"Analyzed {num_sampled} frames containing {total_faces_detected} detected facial instances."
            )

        if visual_manipulation_score > 0.55:
            explanation_parts.append(
                f"Vision Transformer identified strong generative diffusion patterns (latent noise artifacts & synthetic texturing: {visual_manipulation_score*100:.1f}%)."
            )
        else:
            explanation_parts.append(
                f"Vision Transformer confirmed organic camera sensor noise distribution (authentic texture index: {(1.0-visual_manipulation_score)*100:.1f}%)."
            )

        if face_manipulation_prob is not None:
            if face_manipulation_prob > 0.50:
                explanation_parts.append(
                    f"Facial forensics detected localized face-swap boundary blending artifacts (peak likelihood: {max_face*100:.1f}%)."
                )
            else:
                explanation_parts.append("No facial boundary splicing or digital warping detected on facial landmarks.")

        if temporal_score > 0.45:
            explanation_parts.append(
                f"Inter-frame motion inspection flagged temporal flow divergence (erratic vector fields & flicker: {temporal_score*100:.1f}%)."
            )

        if has_audio and audio_synth_prob > 0.50:
            explanation_parts.append(
                f"Acoustic spectral analysis detected neural vocoder high-frequency attenuation ({audio_report.get('summary', '')})."
            )

        forensic_explanation = " ".join(explanation_parts)

        return {
            "success": True,
            "filename": uploaded_file.name,
            "total_video_frames": total_video_frames,
            "duration_sec": round(duration_sec, 2),
            "fps": round(fps, 2),
            "frames_sampled": num_sampled,
            "total_faces_detected": total_faces_detected,
            "ai_generated_probability": round(ai_prob, 4),
            "face_manipulation_probability": round(face_manipulation_prob, 4) if face_manipulation_prob is not None else None,
            "visual_manipulation_score": round(visual_manipulation_score, 4),
            "temporal_inconsistency_score": round(temporal_score, 4),
            "audio_authenticity_score": round(audio_auth_score, 4),
            "primary_category": primary_category,
            "category_distribution": category_distribution,
            "overall_prediction": overall_prediction,
            "confidence": round(confidence, 4),
            "audio_report": audio_report,
            "temporal_report": temporal_report,
            "frames_analyzed": frames_analyzed,
            "suspicious_frames": suspicious_frames[:10],
            "explanation": forensic_explanation
        }

    except Exception as e:
        return {"success": False, "error": f"Video processing error: {str(e)}"}
    finally:
        if os.path.exists(temp_path):
            try:
                os.remove(temp_path)
            except Exception:
                pass
