"""
TruthLens AI - Universal AI Video Forensics (Road to Milky Way Theme)
Multi-category forensic analysis detecting AI-generated landscapes, cities, nature, animation,
synthetic humans, facial deepfakes, and visual scene manipulation across temporal video streams.
"""

import streamlit as st
import sys
import os
import cv2
import numpy as np
import plotly.graph_objects as go
from PIL import Image

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

st.set_page_config(
    page_title="Universal AI Video Detection | TruthLens AI",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="expanded"
)

from ui_common import load_custom_css, render_sidebar_telemetry, render_header, render_html
from processing.video_processor import process_video_stream, validate_video_file
from processing.face_detector import FaceDetector
from models.deepfake_detector import get_deepfake_detector
from database.db import insert_analysis

load_custom_css()
render_sidebar_telemetry()

render_header(
    title="UNIVERSAL AI VIDEO RECOGNITION // FORENSIC INTELLIGENCE",
    subtitle="Zero-face capable multi-category analysis: landscapes, cities, nature, synthetic humans, animation & face deepfakes",
    badge_text="MULTIMODAL FORENSICS",
    badge_type="info"
)

tab_video, tab_image = st.tabs(["🎬 Universal AI Video Forensics", "👤 Static Face Manipulation Analysis"])

detector = get_deepfake_detector()

# ----------------- TAB 1: UNIVERSAL AI VIDEO ANALYSIS -----------------
with tab_video:
    render_html("""
        <div style="font-size: 0.82rem; font-weight: 800; color: #ffe3c5; letter-spacing: 0.08em; text-transform: uppercase; margin-bottom: 0.4rem;">
            Ingest Video Asset (MP4, AVI, MOV, MKV, WEBM)
        </div>
    """)

    video_file = st.file_uploader(
        "Upload Video Stream for Universal Forensics",
        type=["mp4", "avi", "mov", "mkv", "webm"],
        help="Upload videos up to 60MB. TruthLens analyzes full-frame generative textures, facial deepfakes, temporal optical flow, and audio vocoders.",
        key="uploader_universal_video"
    )

    col_ctrl1, col_ctrl2, col_ctrl3 = st.columns(3)
    with col_ctrl1:
        sampling_strategy = st.selectbox(
            "Temporal Sampling Strategy",
            options=["Stratified (Beginning, Middle, End)", "Uniform Step Sampling"],
            index=0,
            help="Stratified samples frames equally across the start, middle, and climax of the video."
        )
    with col_ctrl2:
        max_samples = st.slider("Maximum Sampled Frames", min_value=12, max_value=60, value=24, step=6)
    with col_ctrl3:
        sampling_rate = st.slider("Step Interval (Uniform Mode)", min_value=5, max_value=45, value=15, step=5)

    strat_key = "stratified" if "Stratified" in sampling_strategy else "uniform"

    if video_file:
        st.video(video_file)

        if st.button("⚡ Execute Universal Forensic Analysis", key="btn_run_universal_video", use_container_width=True):
            prog_bar = st.progress(0.0)
            status_box = st.empty()

            def update_progress(ratio, msg):
                prog_bar.progress(min(max(0.0, float(ratio)), 1.0))
                status_box.markdown(
                    f"<div style='font-size: 0.75rem; color: #22d974; font-family: \"JetBrains Mono\", monospace; padding: 0.25rem 0;'>⚡ {msg}</div>",
                    unsafe_allow_html=True
                )

            predict_fn = detector.predict_face if detector.is_configured else None

            with st.spinner("Executing multimodal neural and acoustic forensic pipelines..."):
                results = process_video_stream(
                    video_file,
                    frame_step=sampling_rate,
                    max_frames_to_sample=max_samples,
                    sampling_strategy=strat_key,
                    predict_face_fn=predict_fn,
                    progress_callback=update_progress
                )

            prog_bar.empty()
            status_box.empty()

            if not results.get("success"):
                st.error(f"Forensic Processing Error: {results.get('error')}")
            else:
                pred = results["overall_prediction"]
                conf = results["confidence"]
                ai_prob = results["ai_generated_probability"]
                visual_score = results["visual_manipulation_score"]
                face_score = results["face_manipulation_probability"]
                temporal_score = results["temporal_inconsistency_score"]
                audio_score = results["audio_authenticity_score"]
                primary_cat = results["primary_category"]
                cat_dist = results["category_distribution"]
                total_faces = results["total_faces_detected"]
                frames_sampled = results["frames_sampled"]
                explanation = results["explanation"]
                audio_report = results["audio_report"]
                suspicious_frames = results.get("suspicious_frames", [])

                # Log to SQLite
                tracking_code = insert_analysis(
                    media_type="Video",
                    content_summary=f"{video_file.name} [{primary_cat}] ({results['duration_sec']}s, {results['total_video_frames']} frames)",
                    model_name="TruthLens Multimodal Forensic Pipeline (ViT + Farneback + FFT)",
                    prediction=pred,
                    confidence=conf,
                    status="COMPLETED",
                    metadata={
                        "category": primary_cat,
                        "ai_generated_prob": ai_prob,
                        "visual_score": visual_score,
                        "face_score": face_score,
                        "temporal_score": temporal_score,
                        "audio_authenticity": audio_score,
                        "frames_sampled": frames_sampled,
                        "faces_detected": total_faces,
                        "duration_sec": results["duration_sec"],
                        "fps": results["fps"]
                    }
                )

                st.markdown("<div style='height: 1rem;'></div>", unsafe_allow_html=True)

                # ================= TOP VERDICT BANNER =================
                is_ai_detected = ai_prob >= 0.48
                verdict_color = "#d13f30" if is_ai_detected else "#22d974"
                badge_bg = "rgba(209, 63, 48, 0.16)" if is_ai_detected else "rgba(34, 217, 116, 0.16)"
                badge_border = "#d13f30" if is_ai_detected else "#22d974"

                render_html(f"""
                    <div class="cyber-card" style="border-left: 6px solid {verdict_color}; background: #0a1240; padding: 1.25rem 1.5rem; margin-bottom: 1.25rem;">
                        <div style="display: flex; justify-content: space-between; align-items: flex-start; flex-wrap: wrap; gap: 1rem;">
                            <div>
                                <div style="display: flex; align-items: center; gap: 0.6rem; margin-bottom: 0.4rem;">
                                    <span style="background: {badge_bg}; border: 1.5px solid {badge_border}; color: {verdict_color}; font-size: 0.72rem; font-weight: 800; padding: 0.2rem 0.65rem; border-radius: 999px; letter-spacing: 0.08em;">
                                        {primary_cat.upper()}
                                    </span>
                                    <span style="font-size: 0.75rem; color: #a9b4e8; font-family: 'JetBrains Mono', monospace;">AUDIT ID: {tracking_code}</span>
                                </div>
                                <div style="font-size: 1.4rem; font-weight: 900; color: #FFFFFF; font-family: 'JetBrains Mono', monospace; letter-spacing: 0.02em;">
                                    {pred}
                                </div>
                            </div>
                            <div style="text-align: right;">
                                <div style="font-size: 0.72rem; color: #a9b4e8; text-transform: uppercase; letter-spacing: 0.08em; font-weight: 700;">Composite AI Probability</div>
                                <div style="font-size: 2.2rem; font-weight: 900; color: {verdict_color}; font-family: 'JetBrains Mono', monospace; line-height: 1.1;">
                                    {ai_prob*100:.1f}%
                                </div>
                                <div style="font-size: 0.72rem; color: #ffe3c5;">Confidence Margin: {conf*100:.1f}%</div>
                            </div>
                        </div>
                    </div>
                """)

                # ================= 5-METRIC FORENSIC TELEMETRY =================
                render_html("""
                    <div style="font-size: 0.8rem; font-weight: 800; color: #ffe3c5; letter-spacing: 0.08em; text-transform: uppercase; margin-bottom: 0.6rem;">
                        Multi-Stage Forensic Telemetry Gauges
                    </div>
                """)

                c_m1, c_m2, c_m3, c_m4, c_m5 = st.columns(5)

                with c_m1:
                    render_html(f"""
                        <div class="stat-card">
                            <div class="stat-label">AI Video Probability</div>
                            <div class="stat-value" style="color: {'#d13f30' if ai_prob > 0.5 else '#22d974'};">{ai_prob*100:.1f}%</div>
                            <div class="stat-footer">Multi-modal synthesis</div>
                        </div>
                    """)

                with c_m2:
                    render_html(f"""
                        <div class="stat-card">
                            <div class="stat-label">Full-Frame ViT Score</div>
                            <div class="stat-value" style="color: {'#506cd9' if visual_score > 0.5 else '#22d974'};">{visual_score*100:.1f}%</div>
                            <div class="stat-footer">Zero-face scene texture</div>
                        </div>
                    """)

                with c_m3:
                    face_str = f"{face_score*100:.1f}%" if face_score is not None else "0 Faces"
                    face_sub = f"{total_faces} face(s) localized" if face_score is not None else "Pure scene/landscape"
                    render_html(f"""
                        <div class="stat-card">
                            <div class="stat-label">Facial Deepfake</div>
                            <div class="stat-value" style="color: {'#d13f30' if face_score and face_score > 0.5 else '#a9b4e8'};">{face_str}</div>
                            <div class="stat-footer">{face_sub}</div>
                        </div>
                    """)

                with c_m4:
                    render_html(f"""
                        <div class="stat-card">
                            <div class="stat-label">Temporal Inconsistency</div>
                            <div class="stat-value" style="color: {'#ead11f' if temporal_score > 0.4 else '#22d974'};">{temporal_score*100:.1f}%</div>
                            <div class="stat-footer">Flow divergence & flicker</div>
                        </div>
                    """)

                with c_m5:
                    has_aud = audio_report.get("has_audio", False)
                    aud_val = f"{audio_score*100:.0f}%" if has_aud else "Silent"
                    aud_col = "#22d974" if (has_aud and audio_score > 0.5) else ("#506cd9" if has_aud else "#a9b4e8")
                    render_html(f"""
                        <div class="stat-card">
                            <div class="stat-label">Acoustic Authenticity</div>
                            <div class="stat-value" style="color: {aud_col};">{aud_val}</div>
                            <div class="stat-footer">{'FFT Vocoder Analysis' if has_aud else 'No Audio Stream'}</div>
                        </div>
                    """)

                st.markdown("<div style='height: 1.25rem;'></div>", unsafe_allow_html=True)

                # ================= 2-COLUMN: CATEGORY BREAKDOWN & AUDIO FORENSICS =================
                col_left, col_right = st.columns([1.2, 1.0])

                with col_left:
                    render_html("""
                        <div class="cyber-card" style="height: 100%;">
                            <div style="font-size: 0.85rem; font-weight: 800; color: #FFFFFF; margin-bottom: 0.8rem; display: flex; justify-content: space-between;">
                                <span>TAXONOMY DETECTION BREAKDOWN</span>
                                <span style="font-size: 0.72rem; color: #38D9FF; font-family: monospace;">CYBERSHIELD AI</span>
                            </div>
                    """)

                    category_palette = {
                        "Face Deepfake & Reenactment": "#d13f30",
                        "Fully AI-Generated Landscape / Nature": "#506cd9",
                        "AI Architecture & Urban Environment": "#ffe3c5",
                        "AI-Generated Human & Movement": "#ead11f",
                        "AI Animation & 3D CGI": "#f6aac8",
                        "AI Scene Manipulation / Inpainting": "#a9b8f2",
                        "Authentic Unmanipulated Footage": "#22d974"
                    }

                    for cat_name, cat_pct in cat_dist.items():
                        c_color = category_palette.get(cat_name, "#a9b4e8")
                        render_html(f"""
                            <div style="margin-bottom: 0.65rem;">
                                <div style="display: flex; justify-content: space-between; font-size: 0.76rem; margin-bottom: 0.2rem;">
                                    <span style="color: #F0F4F8; font-weight: 600;">{cat_name}</span>
                                    <span style="color: {c_color}; font-weight: 800; font-family: monospace;">{cat_pct:.1f}%</span>
                                </div>
                                <div style="background: #000621; border-radius: 999px; height: 6px; width: 100%; overflow: hidden; border: 1px solid #26327f;">
                                    <div style="background: {c_color}; width: {cat_pct}%; height: 100%; border-radius: 999px;"></div>
                                </div>
                            </div>
                        """)

                    render_html("</div>")

                with col_right:
                    aud_status = audio_report.get("status", "N/A")
                    aud_summary = audio_report.get("summary", "Acoustic evaluation complete.")
                    render_html(f"""
                        <div class="cyber-card" style="height: 100%;">
                            <div style="font-size: 0.85rem; font-weight: 800; color: #FFFFFF; margin-bottom: 0.6rem; display: flex; justify-content: space-between;">
                                <span>AUDIO & VOCODER FORENSICS</span>
                                <span style="font-size: 0.72rem; color: #ffe3c5; font-family: monospace;">FFT ANALYSIS</span>
                            </div>
                            <div style="font-size: 0.78rem; color: #a9b4e8; margin-bottom: 0.8rem; line-height: 1.45;">
                                {aud_summary}
                            </div>
                            <div class="terminal-box" style="font-size: 0.72rem; padding: 0.65rem;">
                                [AUDIO STREAM STATUS]: {aud_status}<br/>
                                [VOCAL SYNTHESIS PROB]: {audio_report.get('synthetic_speech_probability', 0.0)*100:.1f}%<br/>
                                [ACOUSTIC AUTHENTICITY]: {audio_score*100:.1f}%<br/>
                                [FREQUENCY CUTOFF FORENSIC]: {'TRIGGERED (>7.2kHz attenuation)' if audio_report.get('has_audio') and audio_report.get('synthetic_speech_probability', 0) > 0.45 else 'NORMAL / PASS'}
                            </div>
                        </div>
                    """)

                st.markdown("<div style='height: 1.25rem;'></div>", unsafe_allow_html=True)

                # ================= TIMELINE INTERACTIVE CHART =================
                frames_analyzed = results["frames_analyzed"]
                if frames_analyzed:
                    render_html("""
                        <div style="font-size: 0.82rem; font-weight: 800; color: #ffe3c5; letter-spacing: 0.08em; text-transform: uppercase; margin-bottom: 0.4rem;">
                            Temporal Forensic Timeline (Frame-by-Frame Progression)
                        </div>
                    """)

                    t_stamps = [f["timestamp_sec"] for f in frames_analyzed]
                    vit_vals = [f["vit_synthetic_score"] * 100 for f in frames_analyzed]
                    face_vals = [f["face_fake_score"] * 100 for f in frames_analyzed]
                    cats = [f["category"] for f in frames_analyzed]

                    fig_timeline = go.Figure()

                    # ViT General Scene Score Trace
                    fig_timeline.add_trace(go.Scatter(
                        x=t_stamps,
                        y=vit_vals,
                        mode="lines+markers",
                        name="Full-Frame ViT AI Score (%)",
                        line=dict(color="#506cd9", width=2.5),
                        marker=dict(size=7, symbol="circle"),
                        text=cats,
                        hovertemplate="Time: %{x}s<br>ViT AI Score: %{y:.1f}%<br>Category: %{text}<extra></extra>"
                    ))

                    # Face Deepfake Score Trace (if faces present)
                    if any(f["faces_count"] > 0 for f in frames_analyzed):
                        fig_timeline.add_trace(go.Scatter(
                            x=t_stamps,
                            y=face_vals,
                            mode="lines+markers",
                            name="Facial Deepfake Score (%)",
                            line=dict(color="#d13f30", width=2, dash="dot"),
                            marker=dict(size=6, symbol="diamond"),
                            hovertemplate="Time: %{x}s<br>Face Score: %{y:.1f}%<extra></extra>"
                        ))

                    # Threshold line
                    fig_timeline.add_hline(
                        y=50,
                        line_dash="dash",
                        line_color="#ffe3c5",
                        annotation_text="Suspicion Threshold (50%)",
                        annotation_position="bottom right"
                    )

                    fig_timeline.update_layout(
                        paper_bgcolor="rgba(0,0,0,0)",
                        plot_bgcolor="rgba(0,0,0,0)",
                        font=dict(color="#ffe3c5", family="Inter"),
                        margin=dict(l=25, r=25, t=25, b=25),
                        height=280,
                        legend=dict(
                            orientation="h",
                            yanchor="bottom",
                            y=1.02,
                            xanchor="right",
                            x=1,
                            font=dict(size=11)
                        ),
                        xaxis=dict(
                            title="Video Timeline (Seconds)",
                            showgrid=False,
                            zeroline=False,
                            color="#a9b4e8"
                        ),
                        yaxis=dict(
                            title="Synthetic Likelihood (%)",
                            range=[0, 105],
                            showgrid=True,
                            gridcolor="rgba(38, 50, 127, 0.35)",
                            zeroline=False,
                            color="#a9b4e8"
                        )
                    )
                    st.plotly_chart(fig_timeline, use_container_width=True)

                # ================= SUSPICIOUS FRAME GALLERY =================
                if suspicious_frames:
                    render_html("""
                        <div style="font-size: 0.85rem; font-weight: 800; color: #FFFFFF; letter-spacing: 0.08em; text-transform: uppercase; margin: 1.25rem 0 0.8rem 0; display: flex; align-items: center; gap: 0.5rem;">
                            <span>📸 SUSPICIOUS FRAME EVIDENCE GALLERY</span>
                            <span class="badge-threat" style="font-size: 0.68rem;">FLAGGED FRAMES</span>
                        </div>
                    """)

                    cols_gallery = st.columns(min(4, len(suspicious_frames)))
                    for idx, s_frame in enumerate(suspicious_frames):
                        col_idx = idx % min(4, len(suspicious_frames))
                        with cols_gallery[col_idx]:
                            render_html(f"""
                                <div class="cyber-card" style="padding: 0.6rem; margin-bottom: 0.8rem; border: 2px solid #26327f;">
                                    <div style="position: relative; width: 100%; border-radius: 6px; overflow: hidden; margin-bottom: 0.4rem; background: #000; border: 1px solid #141d5a;">
                                        <img src="{s_frame['thumbnail']}" style="width: 100%; height: auto; display: block;" alt="Suspicious Frame" />
                                        <div style="position: absolute; bottom: 4px; right: 4px; background: rgba(0, 6, 33, 0.88); color: #ffe3c5; font-size: 0.68rem; font-family: monospace; padding: 2px 6px; border-radius: 999px; border: 1px solid #ffe3c5;">
                                            {s_frame['timestamp_sec']}s
                                        </div>
                                    </div>
                                    <div style="font-size: 0.72rem; font-weight: 800; color: #ffe3c5; text-transform: uppercase; margin-bottom: 0.2rem;">
                                        {s_frame['category']}
                                    </div>
                                    <div style="font-size: 0.68rem; color: #a9b4e8; line-height: 1.35;">
                                        {s_frame['reason']}
                                    </div>
                                </div>
                            """)

                # ================= FORENSIC AUDIT SUMMARY BOX =================
                render_html(f"""
                    <div style="background: #0a1240; border: 2px solid #26327f; border-radius: 10px; padding: 1rem 1.25rem; margin-top: 1.25rem; font-size: 0.82rem; color: #a9b4e8; line-height: 1.6; box-shadow: 3px 3px 0px #182276;">
                        <span style="color: #ffe3c5; font-weight: 800; letter-spacing: 0.06em;">COMPREHENSIVE MULTI-MODAL AUDIT REPORT:</span><br/>
                        {explanation}
                    </div>
                """)


# ----------------- TAB 2: STATIC FACE ANALYSIS -----------------
with tab_image:
    render_html("""
        <div style="font-size: 0.82rem; font-weight: 800; color: #ffe3c5; letter-spacing: 0.08em; text-transform: uppercase; margin-bottom: 0.4rem;">
            Ingest Static Portrait (JPG, PNG)
        </div>
    """)

    face_img_file = st.file_uploader(
        "Upload Portrait Image",
        type=["jpg", "jpeg", "png"],
        key="uploader_face_img"
    )

    if face_img_file:
        pil_face = Image.open(face_img_file).convert("RGB")
        img_np = np.array(pil_face)
        img_bgr = cv2.cvtColor(img_np, cv2.COLOR_RGB2BGR)

        detector_fc = FaceDetector()
        boxes = detector_fc.detect_faces(img_bgr)

        col_f1, col_f2 = st.columns([1, 1])

        with col_f1:
            annotated = img_bgr.copy()
            for (x, y, w, h) in boxes:
                cv2.rectangle(annotated, (x, y), (x + w, y + h), (34, 217, 116), 2)
            annotated_rgb = cv2.cvtColor(annotated, cv2.COLOR_BGR2RGB)
            st.image(annotated_rgb, caption=f"Detected {len(boxes)} face(s)", use_container_width=True)

        with col_f2:
            render_html(f"""
                <div class="cyber-card">
                    <div style="font-weight: 800; color: #FFFFFF; font-size: 1rem; margin-bottom: 0.4rem;">
                        Facial Localization Status
                    </div>
                    <div style="font-size: 0.82rem; color: #a9b4e8; line-height: 1.5;">
                        Identified <b>{len(boxes)}</b> human face regions in the static image.<br/>
                        Each detected face is cropped and normalized to 299x299 dimensions for XceptionNet forensic feature extraction.
                    </div>
                </div>
            """)

            if len(boxes) == 0:
                st.warning("No human face detected. Please upload an image with a visible frontal human face.")
            else:
                if st.button("⚡ Score Facial Manipulation", key="btn_score_face", use_container_width=True):
                    for idx, box in enumerate(boxes):
                        cropped = detector_fc.crop_face(img_bgr, box, target_size=(299, 299))
                        if cropped is not None:
                            if detector.is_configured:
                                pred_res = detector.predict_face(cropped)
                                render_html(f"""
                                    <div class="terminal-box" style="margin-top: 0.5rem;">
                                        [FACE #{idx+1} EVALUATION]<br/>
                                        Verdict: {pred_res.get('prediction')}<br/>
                                        Fake Probability: {pred_res.get('fake_probability', 0)*100:.1f}%<br/>
                                        Authentic Probability: {pred_res.get('real_probability', 0)*100:.1f}%
                                    </div>
                                """)
                            else:
                                st.info(f"Face #{idx+1} normalized to 299x299. Deepfake weights unconfigured in `checkpoints/`.")
