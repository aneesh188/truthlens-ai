"""
TruthLens AI - Comparative Model Intelligence & Benchmark Engine
Evaluates two distinct text classification architectures on identical held-out test datasets.
"""

from typing import Dict, Any, Tuple
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline

from data.dataset import get_train_test_split
from evaluation.metrics import compute_classification_metrics


class ModelBenchmarkSuite:
    """
    Trains and evaluates two distinct classification architectures on the same benchmark split:
    - Model A: TF-IDF + L2 Logistic Regression (Linear Margin Classifier)
    - Model B: TF-IDF + Multinomial Naive Bayes (Probabilistic Generative Baseline)
    """

    def __init__(self):
        self.model_a_name = "TF-IDF + Logistic Regression (L2)"
        self.model_b_name = "TF-IDF + Multinomial Naive Bayes"
        
        self.pipeline_a = Pipeline([
            ("tfidf", TfidfVectorizer(ngram_range=(1, 2), max_features=1500, sublinear_tf=True)),
            ("clf", LogisticRegression(C=1.0, max_iter=200, random_state=42))
        ])
        
        self.pipeline_b = Pipeline([
            ("tfidf", TfidfVectorizer(ngram_range=(1, 2), max_features=1500)),
            ("clf", MultinomialNB(alpha=0.5))
        ])
        
        self.is_trained = False
        self.train_size = 0
        self.test_size = 0
        self.cached_results = None

    def run_benchmark(self, force_retrain: bool = False) -> Dict[str, Any]:
        """
        Execute train/test evaluation on held-out test set and compute comparison metrics.
        """
        if self.is_trained and not force_retrain and self.cached_results:
            return self.cached_results

        X_train, X_test, y_train, y_test = get_train_test_split(test_size=0.30, random_state=42)
        
        self.train_size = len(X_train)
        self.test_size = len(X_test)
        
        # Fit both models on identical training split
        self.pipeline_a.fit(X_train, y_train)
        self.pipeline_b.fit(X_train, y_train)
        
        # Predict on identical held-out test split
        y_pred_a = self.pipeline_a.predict(X_test)
        y_pred_b = self.pipeline_b.predict(X_test)
        
        # Compute exact metrics
        metrics_a = compute_classification_metrics(y_test, y_pred_a)
        metrics_b = compute_classification_metrics(y_test, y_pred_b)
        
        self.is_trained = True
        
        self.cached_results = {
            "model_a": {
                "name": self.model_a_name,
                "type": "Linear / Margin Classifier",
                "metrics": metrics_a,
                "pipeline": self.pipeline_a
            },
            "model_b": {
                "name": self.model_b_name,
                "type": "Probabilistic Generative",
                "metrics": metrics_b,
                "pipeline": self.pipeline_b
            },
            "train_samples": self.train_size,
            "test_samples": self.test_size,
            "total_benchmark_samples": self.train_size + self.test_size,
            "test_texts": X_test,
            "test_labels": y_test
        }
        
        return self.cached_results


_global_suite = None

def get_benchmark_suite() -> ModelBenchmarkSuite:
    """Singleton getter for the benchmark suite."""
    global _global_suite
    if _global_suite is None:
        _global_suite = ModelBenchmarkSuite()
    return _global_suite
