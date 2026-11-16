"""
TruthLens AI - Model Intelligence, Benchmarking & Comparative Evaluation
Compares multiple classification architectures on identical held-out test data.
Adheres strictly to scientific rigor: no fabricated figures, proper train/test separation.
"""

import streamlit as st
import sys
import os
import plotly.graph_objects as go
import pandas as pd

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

st.set_page_config(
    page_title="Model Evaluation | TruthLens AI",
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="expanded"
)

from ui_common import load_custom_css, render_sidebar_telemetry, render_header, render_html
from evaluation.model_comparison import get_benchmark_suite

load_custom_css()
render_sidebar_telemetry()

render_header(
    title="MODEL INTELLIGENCE // COMPARATIVE BENCHMARKING",
    subtitle="Rigorous empirical evaluation of NLP classification architectures on held-out test splits",
    badge_text="AUDITED EVALUATION",
    badge_type="info"
)

render_html("""
    <div class="cyber-card">
        <div style="font-weight: 700; color: #FFFFFF; font-size: 1rem; margin-bottom: 0.3rem;">
            Evaluation Protocol & Train/Test Separation
        </div>
        <div style="font-size: 0.82rem; color: #8BA2C1; line-height: 1.5;">
            TruthLens AI strictly evaluates algorithms on a held-out test split (30%) isolated from model fitting.
            Both architectures below are trained on the identical 70% corpus and evaluated across standard classification metrics:
            Accuracy, Precision (macro), Recall (macro), and F1-score.
        </div>
    </div>
""")

suite = get_benchmark_suite()

col_btn, col_empty = st.columns([1, 3])
with col_btn:
    run_eval_btn = st.button("⚡ Execute Benchmark Suite", key="btn_run_eval", use_container_width=True)

if run_eval_btn or suite.is_trained:
    with st.spinner("Training baseline architectures on 70% split and evaluating on held-out 30% test split..."):
        results = suite.run_benchmark(force_retrain=run_eval_btn)

    model_a = results["model_a"]
    model_b = results["model_b"]
    metrics_a = model_a["metrics"]
    metrics_b = model_b["metrics"]

    # Top sample count badges
    render_html(f"""
        <div style="display: flex; gap: 1rem; margin-bottom: 1rem; font-family: 'JetBrains Mono', monospace; font-size: 0.78rem;">
            <span class="badge-info">Training Set: {results['train_samples']} samples</span>
            <span class="badge-safe">Held-Out Test Set: {results['test_samples']} samples</span>
            <span class="badge-warning">Corpus Total: {results['total_benchmark_samples']} verified instances</span>
        </div>
    """)

    # Side-by-side metric cards
    col_a, col_b = st.columns(2)

    with col_a:
        render_html(f"""
            <div class="cyber-card" style="border-left: 4px solid #168BFF;">
                <div style="font-size: 0.72rem; color: #8BA2C1; text-transform: uppercase; font-weight: 700; letter-spacing: 0.08em;">
                    Architecture A ({model_a['type']})
                </div>
                <div style="font-size: 1.25rem; font-weight: 800; color: #38D9FF; margin: 0.2rem 0;">
                    {model_a['name']}
                </div>
                <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 0.5rem; margin-top: 0.75rem;">
                    <div>
                        <div style="font-size: 0.7rem; color: #8BA2C1;">Accuracy</div>
                        <div style="font-size: 1.3rem; font-weight: 800; color: #FFFFFF; font-family: 'JetBrains Mono';">{metrics_a['accuracy']*100:.1f}%</div>
                    </div>
                    <div>
                        <div style="font-size: 0.7rem; color: #8BA2C1;">Precision</div>
                        <div style="font-size: 1.3rem; font-weight: 800; color: #19D69B; font-family: 'JetBrains Mono';">{metrics_a['precision']*100:.1f}%</div>
                    </div>
                    <div>
                        <div style="font-size: 0.7rem; color: #8BA2C1;">Recall</div>
                        <div style="font-size: 1.3rem; font-weight: 800; color: #38D9FF; font-family: 'JetBrains Mono';">{metrics_a['recall']*100:.1f}%</div>
                    </div>
                    <div>
                        <div style="font-size: 0.7rem; color: #8BA2C1;">F1-Score</div>
                        <div style="font-size: 1.3rem; font-weight: 800; color: #C084FC; font-family: 'JetBrains Mono';">{metrics_a['f1']*100:.1f}%</div>
                    </div>
                </div>
            </div>
        """)

    with col_b:
        render_html(f"""
            <div class="cyber-card" style="border-left: 4px solid #C084FC;">
                <div style="font-size: 0.72rem; color: #8BA2C1; text-transform: uppercase; font-weight: 700; letter-spacing: 0.08em;">
                    Architecture B ({model_b['type']})
                </div>
                <div style="font-size: 1.25rem; font-weight: 800; color: #C084FC; margin: 0.2rem 0;">
                    {model_b['name']}
                </div>
                <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 0.5rem; margin-top: 0.75rem;">
                    <div>
                        <div style="font-size: 0.7rem; color: #8BA2C1;">Accuracy</div>
                        <div style="font-size: 1.3rem; font-weight: 800; color: #FFFFFF; font-family: 'JetBrains Mono';">{metrics_b['accuracy']*100:.1f}%</div>
                    </div>
                    <div>
                        <div style="font-size: 0.7rem; color: #8BA2C1;">Precision</div>
                        <div style="font-size: 1.3rem; font-weight: 800; color: #19D69B; font-family: 'JetBrains Mono';">{metrics_b['precision']*100:.1f}%</div>
                    </div>
                    <div>
                        <div style="font-size: 0.7rem; color: #8BA2C1;">Recall</div>
                        <div style="font-size: 1.3rem; font-weight: 800; color: #38D9FF; font-family: 'JetBrains Mono';">{metrics_b['recall']*100:.1f}%</div>
                    </div>
                    <div>
                        <div style="font-size: 0.7rem; color: #8BA2C1;">F1-Score</div>
                        <div style="font-size: 1.3rem; font-weight: 800; color: #C084FC; font-family: 'JetBrains Mono';">{metrics_b['f1']*100:.1f}%</div>
                    </div>
                </div>
            </div>
        """)

    # Comparative Grouped Bar Chart
    render_html("""
        <div style="font-size: 0.82rem; font-weight: 700; color: #8BA2C1; letter-spacing: 0.08em; text-transform: uppercase; margin: 1.25rem 0 0.5rem 0;">
            Direct Comparative Metrics Spectrum
        </div>
    """)

    metric_names = ["Accuracy", "Precision", "Recall", "F1-Score"]
    vals_a = [metrics_a["accuracy"] * 100, metrics_a["precision"] * 100, metrics_a["recall"] * 100, metrics_a["f1"] * 100]
    vals_b = [metrics_b["accuracy"] * 100, metrics_b["precision"] * 100, metrics_b["recall"] * 100, metrics_b["f1"] * 100]

    fig_comp = go.Figure(data=[
        go.Bar(name="Model A: Logistic Regression (L2)", x=metric_names, y=vals_a, marker_color="#168BFF", text=[f"{v:.1f}%" for v in vals_a], textposition="auto"),
        go.Bar(name="Model B: Naive Bayes", x=metric_names, y=vals_b, marker_color="#C084FC", text=[f"{v:.1f}%" for v in vals_b], textposition="auto")
    ])
    fig_comp.update_layout(
        barmode="group",
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(color="#F0F4F8", family="Inter"),
        margin=dict(l=20, r=20, t=20, b=20),
        height=280,
        yaxis=dict(title="Score (%)", range=[0, 105], gridcolor="rgba(22, 139, 255, 0.15)"),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
    )
    st.plotly_chart(fig_comp, use_container_width=True)

    # Confusion Matrices
    st.markdown("""
        <div style="font-size: 0.82rem; font-weight: 700; color: #8BA2C1; letter-spacing: 0.08em; text-transform: uppercase; margin: 1.25rem 0 0.5rem 0;">
            Confusion Matrices on Held-Out Test Set
        </div>
    """, unsafe_allow_html=True)

    cm_col1, cm_col2 = st.columns(2)

    with cm_col1:
        st.markdown(f"<div style='font-size: 0.8rem; font-weight: 700; color: #38D9FF; margin-bottom: 0.3rem;'>{model_a['name']}</div>", unsafe_allow_html=True)
        cm_a = metrics_a["confusion_matrix"]
        fig_cm_a = go.Figure(data=go.Heatmap(
            z=cm_a,
            x=["Pred: REAL", "Pred: FAKE"],
            y=["Actual: REAL", "Actual: FAKE"],
            colorscale=[[0, "#081628"], [1, "#168BFF"]],
            text=cm_a,
            texttemplate="%{text}",
            showscale=False
        ))
        fig_cm_a.update_layout(
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            font=dict(color="#F0F4F8", family="Inter"),
            margin=dict(l=40, r=20, t=10, b=20),
            height=200
        )
        st.plotly_chart(fig_cm_a, use_container_width=True)

    with cm_col2:
        st.markdown(f"<div style='font-size: 0.8rem; font-weight: 700; color: #C084FC; margin-bottom: 0.3rem;'>{model_b['name']}</div>", unsafe_allow_html=True)
        cm_b = metrics_b["confusion_matrix"]
        fig_cm_b = go.Figure(data=go.Heatmap(
            z=cm_b,
            x=["Pred: REAL", "Pred: FAKE"],
            y=["Actual: REAL", "Actual: FAKE"],
            colorscale=[[0, "#081628"], [1, "#C084FC"]],
            text=cm_b,
            texttemplate="%{text}",
            showscale=False
        ))
        fig_cm_b.update_layout(
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            font=dict(color="#F0F4F8", family="Inter"),
            margin=dict(l=40, r=20, t=10, b=20),
            height=200
        )
        st.plotly_chart(fig_cm_b, use_container_width=True)

    # Classification Reports
    with st.expander("📄 Detailed Scikit-Learn Classification Reports (JSON Breakdown)"):
        rep_col1, rep_col2 = st.columns(2)
        with rep_col1:
            st.markdown(f"**{model_a['name']}**")
            st.json(metrics_a["classification_report"])
        with rep_col2:
            st.markdown(f"**{model_b['name']}**")
            st.json(metrics_b["classification_report"])

else:
    st.markdown("""
        <div class="cyber-card" style="text-align: center; padding: 3rem;">
            <div style="font-size: 2.2rem; margin-bottom: 0.5rem;">⚖️</div>
            <div style="font-size: 1.05rem; font-weight: 700; color: #FFFFFF;">Ready to Run Empirical Model Comparison</div>
            <div style="font-size: 0.82rem; color: #8BA2C1; margin-top: 0.25rem;">
                Click "Execute Benchmark Suite" to train both architectures on the training partition and test them on the held-out partition.
            </div>
        </div>
    """, unsafe_allow_html=True)
