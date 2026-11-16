"""
TruthLens AI - UI Components & Telemetry Utility
Renders cybersecurity command-center headers, cards, system monitors, and sidebar telemetries.
"""

import streamlit as st
import os
import re
import psutil
from database.db import get_statistics
from models.text_detector import get_text_detector
from models.image_detector import get_image_detector
from models.deepfake_detector import get_deepfake_detector


def render_html(html_str: str):
    """
    Safely render raw HTML in Streamlit.
    Strips leading line indentation and eliminates multi-newlines so CommonMark
    never misinterprets indented tags as <pre><code> blocks.
    """
    cleaned = re.sub(r"^[ \t]+", "", html_str, flags=re.MULTILINE)
    cleaned = re.sub(r"\n{2,}", "\n", cleaned)
    st.markdown(cleaned, unsafe_allow_html=True)


def load_custom_css():
    """Inject the dark cybersecurity command center stylesheet."""
    css_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets", "styles.css")
    if os.path.exists(css_path):
        with open(css_path, "r", encoding="utf-8") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


def render_sidebar_telemetry():
    """Render cybersecurity telemetry, engine status indicators, and system diagnostics in sidebar."""
    with st.sidebar:
        render_html("""
            <div style="padding: 0.8rem 0; border-bottom: 1px solid rgba(22, 139, 255, 0.25); margin-bottom: 1rem;">
                <div style="display: flex; align-items: center; gap: 0.6rem;">
                    <div style="background: linear-gradient(135deg, #168BFF, #38D9FF); width: 34px; height: 34px; border-radius: 8px; display: flex; align-items: center; justify-content: center; font-size: 1.2rem; box-shadow: 0 0 12px rgba(56, 217, 255, 0.5);">
                        🛡️
                    </div>
                    <div>
                        <div style="font-weight: 800; font-size: 1.15rem; color: #FFFFFF; letter-spacing: -0.02em;">TRUTHLENS <span style="color: #38D9FF;">AI</span></div>
                        <div style="font-size: 0.68rem; color: #8BA2C1; letter-spacing: 0.08em; text-transform: uppercase;">Media Forensics Platform</div>
                    </div>
                </div>
            </div>
            <div style="font-size: 0.72rem; color: #8BA2C1; font-weight: 700; text-transform: uppercase; letter-spacing: 0.08em; margin-bottom: 0.6rem;">AI Detection Engines</div>
        """)
        
        # Check text engine
        text_det = get_text_detector()
        text_status = "online" if "Active" in text_det.status_message or "Transformer" in text_det.status_message or "Baseline" in text_det.status_message else "threat"
        
        # Check image engine
        img_det = get_image_detector()
        img_status = "online" if img_det.status == "ONLINE" else "standby"
        
        # Check deepfake engine
        df_det = get_deepfake_detector()
        df_status = "online" if df_det.is_configured else "standby"

        render_html(f"""
            <div style="background: #081628; border: 1px solid rgba(22, 139, 255, 0.2); border-radius: 6px; padding: 0.75rem; margin-bottom: 1rem;">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.4rem; font-size: 0.8rem;">
                    <span style="color: #F0F4F8;">NLP Fake News</span>
                    <span><span class="pulse-dot {text_status}"></span> <span style="font-size: 0.72rem; color: #8BA2C1;">READY</span></span>
                </div>
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.4rem; font-size: 0.8rem;">
                    <span style="color: #F0F4F8;">Synthetic Vision</span>
                    <span><span class="pulse-dot {img_status}"></span> <span style="font-size: 0.72rem; color: #8BA2C1;">{'READY' if img_status == 'online' else 'STANDBY'}</span></span>
                </div>
                <div style="display: flex; justify-content: space-between; align-items: center; font-size: 0.8rem;">
                    <span style="color: #F0F4F8;">XceptionNet Facial</span>
                    <span><span class="pulse-dot {df_status}"></span> <span style="font-size: 0.72rem; color: #8BA2C1;">{'ACTIVE' if df_status == 'online' else 'STANDBY'}</span></span>
                </div>
            </div>
            <div style="font-size: 0.72rem; color: #8BA2C1; font-weight: 700; text-transform: uppercase; letter-spacing: 0.08em; margin-bottom: 0.6rem;">Hardware Telemetry</div>
        """)

        # GPU detection
        try:
            import torch
            has_cuda = torch.cuda.is_available()
            gpu_name = torch.cuda.get_device_name(0) if has_cuda else "None (CPU Mode)"
        except Exception:
            has_cuda = False
            gpu_name = "CPU Only"

        # CPU / RAM
        try:
            cpu_usage = psutil.cpu_percent()
            ram_usage = psutil.virtual_memory().percent
        except Exception:
            cpu_usage = 0
            ram_usage = 0

        render_html(f"""
            <div style="background: #081628; border: 1px solid rgba(22, 139, 255, 0.2); border-radius: 6px; padding: 0.75rem; margin-bottom: 1.25rem; font-family: 'JetBrains Mono', monospace; font-size: 0.75rem;">
                <div style="color: #38D9FF; margin-bottom: 0.3rem;">⚡ ACCEL: {'CUDA ACTIVE' if has_cuda else 'CPU FALLBACK'}</div>
                <div style="color: #8BA2C1; font-size: 0.7rem; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; margin-bottom: 0.5rem;" title="{gpu_name}">{gpu_name}</div>
                <div style="display: flex; justify-content: space-between; color: #F0F4F8; margin-bottom: 0.2rem;">
                    <span>CPU Load</span><span>{cpu_usage}%</span>
                </div>
                <div style="display: flex; justify-content: space-between; color: #F0F4F8;">
                    <span>System RAM</span><span>{ram_usage}%</span>
                </div>
            </div>
            <div style="font-size: 0.68rem; color: #4F6785; text-align: center; border-top: 1px solid rgba(22, 139, 255, 0.15); padding-top: 0.75rem;">
                TruthLens v1.0.4-PROD<br/>Unified Python Media Forensics
            </div>
        """)


def render_header(title: str, subtitle: str, badge_text: str = "FORENSIC SYSTEM ONLINE", badge_type: str = "safe"):
    """Render consistent command-center top title bar."""
    badge_class = f"badge-{badge_type}"
    render_html(f"""
        <div class="cyber-header">
            <div>
                <div class="cyber-header-title">{title}</div>
                <div class="cyber-header-subtitle">{subtitle}</div>
            </div>
            <div>
                <span class="{badge_class}">
                    <span class="pulse-dot {'online' if badge_type == 'safe' else ('threat' if badge_type == 'threat' else 'standby')}"></span>
                    {badge_text}
                </span>
            </div>
        </div>
    """)
