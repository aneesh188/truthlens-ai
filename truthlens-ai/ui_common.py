"""
TruthLens AI - UI Components & Telemetry Utility (CyberShield AI Theme)
Renders high-tech cyber defense headers, glassmorphism cards, neural monitors, and sidebar telemetries.
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
    """Inject the CyberShield AI cyber defense stylesheet."""
    css_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets", "styles.css")
    if os.path.exists(css_path):
        with open(css_path, "r", encoding="utf-8") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


def render_sidebar_telemetry():
    """Render cyber telemetry, engine status indicators, and system diagnostics in sidebar."""
    with st.sidebar:
        render_html("""
            <div style="padding: 0.8rem 0; border-bottom: 1.5px solid rgba(22, 139, 255, 0.25); margin-bottom: 1rem;">
                <div style="display: flex; align-items: center; gap: 0.65rem;">
                    <div style="background: linear-gradient(135deg, #168BFF, #00E5FF); width: 38px; height: 38px; border-radius: 8px; display: flex; align-items: center; justify-content: center; font-size: 1.25rem; box-shadow: 0 0 12px rgba(0, 229, 255, 0.4); border: 1.5px solid #38D9FF;">
                        🛡️
                    </div>
                    <div>
                        <div style="font-weight: 900; font-size: 1.15rem; color: #FFFFFF; letter-spacing: -0.01em;">CyberShield <span style="color: #38D9FF;">AI</span></div>
                        <div style="font-size: 0.68rem; color: #8FA2C1; letter-spacing: 0.08em; text-transform: uppercase;">Real-Time Threat Intel</div>
                    </div>
                </div>
            </div>
            <div style="font-size: 0.72rem; color: #38D9FF; font-weight: 800; text-transform: uppercase; letter-spacing: 0.09em; margin-bottom: 0.6rem;">Active Threat Engines</div>
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
            <div style="background: rgba(6, 21, 43, 0.85); border: 1.5px solid rgba(22, 139, 255, 0.3); border-radius: 8px; padding: 0.75rem 0.9rem; margin-bottom: 1rem; box-shadow: 0 4px 15px rgba(2, 11, 26, 0.5);">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.45rem; font-size: 0.8rem;">
                    <span style="color: #F0F4F8; font-weight: 600;">Behavior Analysis</span>
                    <span><span class="pulse-dot {text_status}"></span> <span style="font-size: 0.72rem; color: #10E79D; font-weight: 700;">SCANNING</span></span>
                </div>
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.45rem; font-size: 0.8rem;">
                    <span style="color: #F0F4F8; font-weight: 600;">Anomaly Detection (ViT)</span>
                    <span><span class="pulse-dot {img_status}"></span> <span style="font-size: 0.72rem; color: {'#10E79D' if img_status == 'online' else '#FFB300'}; font-weight: 700;">{'ONLINE' if img_status == 'online' else 'STANDBY'}</span></span>
                </div>
                <div style="display: flex; justify-content: space-between; align-items: center; font-size: 0.8rem;">
                    <span style="color: #F0F4F8; font-weight: 600;">ML Video Classification</span>
                    <span><span class="pulse-dot {df_status}"></span> <span style="font-size: 0.72rem; color: {'#10E79D' if df_status == 'online' else '#FFB300'}; font-weight: 700;">{'ACTIVE' if df_status == 'online' else 'STANDBY'}</span></span>
                </div>
            </div>
            <div style="font-size: 0.72rem; color: #38D9FF; font-weight: 800; text-transform: uppercase; letter-spacing: 0.09em; margin-bottom: 0.6rem;">SOC Node Diagnostics</div>
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
            <div style="background: rgba(6, 21, 43, 0.85); border: 1.5px solid rgba(22, 139, 255, 0.3); border-radius: 8px; padding: 0.75rem 0.9rem; margin-bottom: 1.25rem; font-family: 'JetBrains Mono', monospace; font-size: 0.75rem; box-shadow: 0 4px 15px rgba(2, 11, 26, 0.5);">
                <div style="color: #10E79D; margin-bottom: 0.35rem; font-weight: 700;">⚡ ACCELERATOR: {'CUDA ACTIVE' if has_cuda else 'CPU FALLBACK'}</div>
                <div style="color: #8FA2C1; font-size: 0.7rem; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; margin-bottom: 0.5rem;" title="{gpu_name}">{gpu_name}</div>
                <div style="display: flex; justify-content: space-between; color: #F0F4F8; margin-bottom: 0.25rem;">
                    <span>CPU Core Load</span><span style="color: #38D9FF;">{cpu_usage}%</span>
                </div>
                <div style="display: flex; justify-content: space-between; color: #F0F4F8;">
                    <span>Memory Allocation</span><span style="color: #38D9FF;">{ram_usage}%</span>
                </div>
            </div>
            <div style="font-size: 0.68rem; color: #8FA2C1; text-align: center; border-top: 1.5px solid rgba(22, 139, 255, 0.2); padding-top: 0.75rem;">
                CyberShield AI // TruthLens Enterprise<br/>Security Operations Command
            </div>
        """)


def render_header(title: str, subtitle: str, badge_text: str = "SYSTEM PROTECTED", badge_type: str = "safe"):
    """Render consistent CyberShield AI HUD top title bar."""
    badge_class = f"badge-{badge_type}"
    render_html(f"""
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1.25rem; padding-bottom: 0.75rem; border-bottom: 1.5px solid rgba(22, 139, 255, 0.25); flex-wrap: wrap; gap: 0.75rem;">
            <div>
                <div style="font-size: 1.35rem; font-weight: 900; color: #FFFFFF; font-family: 'Inter', sans-serif; letter-spacing: -0.01em;">
                    {title}
                </div>
                <div style="font-size: 0.78rem; color: #8FA2C1; margin-top: 0.15rem; font-weight: 500;">
                    {subtitle}
                </div>
            </div>
            <div>
                <span class="{badge_class}">
                    <span class="pulse-dot {'online' if badge_type == 'safe' else ('threat' if badge_type == 'threat' else 'standby')}"></span>
                    {badge_text}
                </span>
            </div>
        </div>
    """)
