# Launch TruthLens AI Platform
Write-Host "==========================================================" -ForegroundColor Cyan
Write-Host "   TRUTHLENS AI - MULTIMODAL MEDIA INTELLIGENCE PLATFORM   " -ForegroundColor Cyan
Write-Host "==========================================================" -ForegroundColor Cyan
Write-Host "Starting Streamlit Cybersecurity Command Center..." -ForegroundColor Green

Set-Location -Path "$PSScriptRoot\truthlens-ai"
python -m streamlit run app.py
