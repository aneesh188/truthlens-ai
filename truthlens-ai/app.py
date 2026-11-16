"""
TruthLens AI - Multimodal Media Intelligence Platform
Master Application Entrypoint
"""

import streamlit as st
import sys
import os

# Add root folder to sys.path so modules import reliably
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

st.set_page_config(
    page_title="TruthLens AI | Media Forensics Command Center",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

from dashboard_view import render_dashboard

if __name__ == "__main__":
    render_dashboard()
