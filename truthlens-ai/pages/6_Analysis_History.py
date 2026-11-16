"""
TruthLens AI - Forensic Audit History & Telemetry Log
Full audit trail of all multimodal analyses stored in SQLite with search, filters, and export capabilities.
"""

import streamlit as st
import sys
import os
import pandas as pd

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

st.set_page_config(
    page_title="Analysis History | TruthLens AI",
    page_icon="📜",
    layout="wide",
    initial_sidebar_state="expanded"
)

from ui_common import load_custom_css, render_sidebar_telemetry, render_header, render_html
from database.db import get_all_analyses, clear_history, delete_analysis, get_analysis_by_id

load_custom_css()
render_sidebar_telemetry()

render_header(
    title="AUDIT LOG // HISTORICAL TELEMETRY VAULT",
    subtitle="Persistent immutable ledger of forensic classifications, model verdicts, and metadata",
    badge_text="SQLITE LEDGER",
    badge_type="info"
)

# Filters Row
f_col1, f_col2, f_col3 = st.columns([1.5, 2.5, 1.2])

with f_col1:
    media_filter = st.selectbox(
        "Filter by Modality",
        options=["All", "Text", "Image", "Video"],
        index=0
    )

with f_col2:
    search_query = st.text_input(
        "Search Audit Ledger",
        placeholder="Search by Tracking Code, Summary, or Model Engine..."
    )

with f_col3:
    limit_count = st.selectbox(
        "Display Rows",
        options=[25, 50, 100, 250],
        index=1
    )

records = get_all_analyses(
    media_type=media_filter,
    search_query=search_query,
    limit=limit_count
)

render_html(f"""
    <div style="display: flex; justify-content: space-between; align-items: center; margin: 1rem 0 0.5rem 0;">
        <div style="font-size: 0.82rem; font-weight: 700; color: #8BA2C1; letter-spacing: 0.08em; text-transform: uppercase;">
            Matching Records: <span style="color: #38D9FF;">{len(records)}</span>
        </div>
    </div>
""")

if records:
    # Prepare DataFrame
    table_data = []
    for r in records:
        table_data.append({
            "ID": r["id"],
            "Tracking Code": r["analysis_code"],
            "Timestamp": r["timestamp"],
            "Modality": r["media_type"],
            "Content Summary": r["content_summary"],
            "Model Name": r["model_name"],
            "Verdict": r["prediction"],
            "Confidence": f"{float(r['confidence']) * 100:.1f}%",
            "Status": r["status"]
        })
    df = pd.DataFrame(table_data)
    st.dataframe(df, use_container_width=True, hide_index=True)

    # Export & Clear Row
    c_exp1, c_exp2, c_clear = st.columns([1.5, 1.5, 1.5])
    
    with c_exp1:
        csv_data = df.to_csv(index=False).encode("utf-8")
        st.download_button(
            "📥 Export Audit Ledger (CSV)",
            data=csv_data,
            file_name="truthlens_forensic_audit.csv",
            mime="text/csv",
            use_container_width=True
        )

    with c_clear:
        if st.button("🗑️ Clear Audit History", key="btn_clear_db", use_container_width=True):
            st.session_state["confirm_clear"] = True

    if st.session_state.get("confirm_clear"):
        st.warning("⚠️ Are you sure you want to permanently erase all analysis records?")
        col_yes, col_no = st.columns([1, 1])
        with col_yes:
            if st.button("Yes, Erase All Records", key="btn_confirm_erase"):
                deleted_rows = clear_history()
                st.session_state["confirm_clear"] = False
                st.success(f"Successfully erased {deleted_rows} audit records.")
                st.rerun()
        with col_no:
            if st.button("Cancel", key="btn_cancel_erase"):
                st.session_state["confirm_clear"] = False
                st.rerun()

    # Detailed Inspection Expander
    render_html("<div style='height: 1.5rem;'></div>")
    render_html("""
        <div style="font-size: 0.82rem; font-weight: 700; color: #8BA2C1; letter-spacing: 0.08em; text-transform: uppercase; margin-bottom: 0.5rem;">
            Inspect Individual Record Metadata
        </div>
    """)

    selected_code = st.selectbox(
        "Select Record Tracking Code to Inspect",
        options=[r["analysis_code"] for r in records]
    )

    if selected_code:
        record_detail = next((r for r in records if r["analysis_code"] == selected_code), None)
        if record_detail:
            d_col1, d_col2 = st.columns([1, 1])
            with d_col1:
                render_html(f"""
                    <div class="terminal-box">
                        [RECORD AUDIT SHEET]<br/>
                        • Code: {record_detail['analysis_code']}<br/>
                        • Timestamp: {record_detail['timestamp']}<br/>
                        • Media Modality: {record_detail['media_type']}<br/>
                        • Classification: {record_detail['prediction']}<br/>
                        • Confidence: {record_detail['confidence']*100:.2f}%<br/>
                        • Status: {record_detail['status']}
                    </div>
                """)
            with d_col2:
                st.markdown(f"**Stored Forensic Metadata (JSON):**")
                st.json(record_detail["metadata"])

else:
    render_html("""
        <div class="cyber-card" style="text-align: center; padding: 3rem;">
            <div style="font-size: 2.2rem; margin-bottom: 0.5rem;">📜</div>
            <div style="font-size: 1.05rem; font-weight: 700; color: #FFFFFF;">Audit Ledger is Empty</div>
            <div style="font-size: 0.82rem; color: #8BA2C1; margin-top: 0.25rem;">
                No forensic analyses match the specified filter criteria. Analyses performed across Text, Image, and Video will automatically appear here.
            </div>
        </div>
    """)
