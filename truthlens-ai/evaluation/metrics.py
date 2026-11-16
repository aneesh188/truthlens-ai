"""
TruthLens AI - Evaluation Metrics & Performance Benchmarks
Computes genuine classification metrics: Accuracy, Precision, Recall, F1, Confusion Matrix.
"""

from typing import Dict, Any, List
import numpy as np
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    classification_report
)


def compute_classification_metrics(
    y_true: List[int],
    y_pred: List[int],
    labels: List[str] = None
) -> Dict[str, Any]:
    """
    Compute rigorous evaluation metrics on real ground-truth and prediction arrays.
    """
    labels = labels or ["REAL", "POTENTIALLY FAKE"]
    
    y_true_arr = np.array(y_true)
    y_pred_arr = np.array(y_pred)
    
    acc = float(accuracy_score(y_true_arr, y_pred_arr))
    prec = float(precision_score(y_true_arr, y_pred_arr, zero_division=0))
    rec = float(recall_score(y_true_arr, y_pred_arr, zero_division=0))
    f1 = float(f1_score(y_true_arr, y_pred_arr, zero_division=0))
    
    cm = confusion_matrix(y_true_arr, y_pred_arr, labels=[0, 1]).tolist()
    
    report_dict = classification_report(
        y_true_arr,
        y_pred_arr,
        target_names=labels,
        output_dict=True,
        zero_division=0
    )
    
    return {
        "accuracy": round(acc, 4),
        "precision": round(prec, 4),
        "recall": round(rec, 4),
        "f1": round(f1, 4),
        "confusion_matrix": cm,
        "labels": labels,
        "classification_report": report_dict,
        "total_samples": len(y_true)
    }
