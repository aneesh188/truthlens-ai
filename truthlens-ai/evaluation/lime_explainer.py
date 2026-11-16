"""
TruthLens AI - Explainable AI (LIME) Module
Provides local interpretable model-agnostic explanations for text classifications,
identifying which tokens drove prediction towards 'REAL' or 'POTENTIALLY FAKE'.
"""

from typing import List, Tuple, Dict, Any, Callable
import numpy as np


class TextLimeExplainer:
    """
    Wraps LIME TextExplainer for fake news detection models.
    """

    def __init__(self, class_names: List[str] = None):
        self.class_names = class_names or ["REAL", "POTENTIALLY FAKE"]
        self.explainer = None
        self._init_lime()

    def _init_lime(self):
        try:
            from lime.lime_text import LimeTextExplainer
            self.explainer = LimeTextExplainer(
                class_names=self.class_names,
                split_expression=r"\W+",
                bow=True
            )
        except Exception:
            self.explainer = None

    def explain(
        self,
        text: str,
        predict_proba_fn: Callable[[List[str]], np.ndarray],
        num_features: int = 10,
        num_samples: int = 300
    ) -> Dict[str, Any]:
        """
        Generate LIME explanation for a single text instance.
        Returns influential features, weight values, and explanation narrative.
        """
        if not self.explainer:
            self._init_lime()
            
        if not self.explainer:
            return {
                "available": False,
                "error": "LIME package is not available.",
                "features": [],
                "explanation_text": "LIME explainer could not be initialized."
            }

        if len(text.strip().split()) < 3:
            return {
                "available": False,
                "error": "Input text too brief for token attribution.",
                "features": [],
                "explanation_text": "Please provide at least a complete sentence for lexical attribution."
            }

        try:
            # Generate explanation for the highest predicted class
            exp = self.explainer.explain_instance(
                text_instance=text,
                classifier_fn=predict_proba_fn,
                num_features=num_features,
                num_samples=num_samples
            )
            
            # Extract features list: [(word, weight), ...]
            # Positive weight -> indicates class index 1 (POTENTIALLY FAKE)
            # Negative weight -> indicates class index 0 (REAL)
            feature_weights: List[Tuple[str, float]] = exp.as_list()
            
            fake_contributors = [item for item in feature_weights if item[1] > 0]
            real_contributors = [item for item in feature_weights if item[1] < 0]
            
            fake_contributors.sort(key=lambda x: abs(x[1]), reverse=True)
            real_contributors.sort(key=lambda x: abs(x[1]), reverse=True)
            
            explanation_summary = (
                f"LIME identified {len(fake_contributors)} tokens associated with sensational/misleading patterns "
                f"and {len(real_contributors)} tokens associated with standard factual reporting style. "
                "Notice: Feature importance measures model attribution on its training corpus, not absolute factual truth."
            )

            formatted_features = []
            for word, weight in feature_weights:
                formatted_features.append({
                    "word": word,
                    "weight": round(float(weight), 4),
                    "influences": "POTENTIALLY FAKE" if weight > 0 else "REAL",
                    "magnitude": round(abs(float(weight)), 4)
                })

            return {
                "available": True,
                "features": formatted_features,
                "explanation_text": explanation_summary,
                "top_fake_tokens": [w for w, _ in fake_contributors[:5]],
                "top_real_tokens": [w for w, _ in real_contributors[:5]]
            }

        except Exception as e:
            return {
                "available": False,
                "error": f"LIME explanation failed: {str(e)}",
                "features": [],
                "explanation_text": "Explanation computation encountered an internal error."
            }
