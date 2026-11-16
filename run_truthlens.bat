@echo off
echo ==========================================================
echo    TRUTHLENS AI - MULTIMODAL MEDIA INTELLIGENCE PLATFORM
echo ==========================================================
cd /d "%~dp0truthlens-ai"
python -m streamlit run app.py
pause
