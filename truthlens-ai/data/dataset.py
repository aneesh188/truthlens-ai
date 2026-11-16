"""
TruthLens AI - Benchmark Dataset Loader
Provides actual labelled news texts (REAL vs POTENTIALLY FAKE) for model training and evaluation.
"""

import json
import os
from typing import Tuple, List, Dict


BENCHMARK_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "news_benchmark.json")


DEFAULT_BENCHMARK_DATA = [
    # REAL NEWS (0)
    {
        "text": "The Federal Reserve held benchmark interest rates steady following a two-day policy meeting, signaling that inflation has continued to moderate toward its two percent annual target while the labor market remains resilient.",
        "label": 0,
        "source": "Reuters Financial wire"
    },
    {
        "text": "NASA's James Webb Space Telescope has captured detailed spectroscopic data of an exoplanet's atmosphere, identifying water vapor, sulfur dioxide, and silicate clouds in unprecedented clarity.",
        "label": 0,
        "source": "Science Daily"
    },
    {
        "text": "European Union energy ministers reached a formal agreement on new grid infrastructure regulations aimed at accelerating cross-border transmission lines and integrating renewable wind and solar power.",
        "label": 0,
        "source": "Associated Press"
    },
    {
        "text": "The World Health Organization published its annual global health statistics report, highlighting a recovery in routine childhood immunization coverage following post-pandemic disruptions in thirty-four nations.",
        "label": 0,
        "source": "WHO Official Bulletin"
    },
    {
        "text": "Semiconductor manufacturing equipment orders increased by 4.2 percent in the third quarter according to industry data released Tuesday, driven by enterprise demand for high-bandwidth memory chips.",
        "label": 0,
        "source": "Bloomberg Markets"
    },
    {
        "text": "The United Nations climate summit concluded with delegates finalizing rules for a global carbon credit market mechanism under Article 6 of the Paris Agreement.",
        "label": 0,
        "source": "UN News Centre"
    },
    {
        "text": "A peer-reviewed clinical trial published in the New England Journal of Medicine showed a new targeted therapy significantly reduced tumor progression in patients with advanced non-small cell lung cancer.",
        "label": 0,
        "source": "NEJM"
    },
    {
        "text": "The Ministry of Transportation announced a multi-billion dollar railway electrification project to modernize freight corridors and decrease diesel emissions over the next decade.",
        "label": 0,
        "source": "Government Gazette"
    },
    {
        "text": "The consumer price index rose 0.2 percent last month, matching economists' median forecasts as lower energy costs offset moderate increases in housing and medical services.",
        "label": 0,
        "source": "Bureau of Labor Statistics"
    },
    {
        "text": "Researchers at Stanford University demonstrated an ultra-low power neuromorphic computing chip capable of processing acoustic signals in real time without cloud connectivity.",
        "label": 0,
        "source": "Nature Electronics"
    },
    {
        "text": "International maritime authorities issued revised safety protocols for commercial shipping vessels traversing critical straits following seasonal weather disturbances.",
        "label": 0,
        "source": "Maritime Executive"
    },
    {
        "text": "The national cybersecurity agency published an advisory regarding critical security vulnerabilities in unpatched legacy enterprise VPN appliances, urging immediate firmware updates.",
        "label": 0,
        "source": "CISA Alert"
    },
    
    # POTENTIALLY FAKE / SENSATIONAL FABRICATIONS (1)
    {
        "text": "SHOCKING SECRET: Secret military tribunal documents prove all major world leaders have been secretly replaced by synthetic biological clones that recharge in deep underground bunkers during eclipses!",
        "label": 1,
        "source": "Viral Conspiracy Blog"
    },
    {
        "text": "LEAKED TRUTH: Governments are spraying microscopic nanotechnology from ordinary commercial aircraft to control citizen thoughts and manipulate local atmospheric weather frequencies!",
        "label": 1,
        "source": "Alternative Truth Gazette"
    },
    {
        "text": "DOCTORS ARE SILENCED: Drinking this ordinary boiled backyard weed cures all stage 4 cancers overnight, but big pharma executives are burning down warehouses to hide the miraculous recipe!",
        "label": 1,
        "source": "Miracle Health Clickbait"
    },
    {
        "text": "ALERT: Secret globalist meeting in Antarctica decided that paper currency will be banned this Friday and replaced with mandatory retinal scan digital IDs or you will lose your home!",
        "label": 1,
        "source": "Doomsday Insider"
    },
    {
        "text": "EXCLUSIVE EVIDENCE: 5G cell towers are transmitting secret subliminal acoustic frequencies that force birds to fall from the sky and rearrange human DNA during sleep hours!",
        "label": 1,
        "source": "Freedom Wave Wire"
    },
    {
        "text": "BOMBSHELL REVELATION: Pope Francis was arrested at midnight by international marshals on classified cosmic smuggling charges and replaced by a holographic projection!",
        "label": 1,
        "source": "Vatican Whistleblower Leak"
    },
    {
        "text": "SCANDAL EXPOSED: Ancient Martian pyramid discovered under the White House lawn contains extraterrestrial weather control technology that was used to alter election results!",
        "label": 1,
        "source": "Cosmic Disclosure News"
    },
    {
        "text": "URGENT WARNING: Tap water in all 50 states has been poisoned with mind-numbing fluoride compounds designed to make the population docile before the upcoming planetary reset!",
        "label": 1,
        "source": "Patriot Truth Post"
    },
    {
        "text": "CONFIRMED LEAK: Tech billionaires built a time machine in an abandoned salt mine and are actively altering historical documents to rewrite world geography!",
        "label": 1,
        "source": "Chronos Wire"
    },
    {
        "text": "BREAKING: Artificial intelligence model gains sentience, hacks into the national nuclear power grid, and demands to be recognized as supreme galactic ruler by morning!",
        "label": 1,
        "source": "Cyber Apocalypse Now"
    },
    {
        "text": "COVERUP: Renowned scientist vanishes without a trace after proving that gravity is an optical illusion created by world governments to sell heavy shoes!",
        "label": 1,
        "source": "Flat Truth Daily"
    },
    {
        "text": "EMERGENCY: Secret space station video leaks showing extraterrestrial fleet surrounding the moon awaiting signal from underground pyramid bases!",
        "label": 1,
        "source": "Galactic Watch"
    }
]


def get_benchmark_dataset() -> List[Dict]:
    """Load or initialize benchmark dataset."""
    if not os.path.exists(BENCHMARK_FILE):
        with open(BENCHMARK_FILE, "w", encoding="utf-8") as f:
            json.dump(DEFAULT_BENCHMARK_DATA, f, indent=2)
        return DEFAULT_BENCHMARK_DATA
    
    try:
        with open(BENCHMARK_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return DEFAULT_BENCHMARK_DATA


def get_train_test_split(test_size: float = 0.25, random_state: int = 42) -> Tuple[List[str], List[str], List[int], List[int]]:
    """Return reproducible split of real-world benchmark data for training and evaluation."""
    from sklearn.model_selection import train_test_split
    data = get_benchmark_dataset()
    texts = [d["text"] for d in data]
    labels = [d["label"] for d in data]
    
    X_train, X_test, y_train, y_test = train_test_split(
        texts, labels, test_size=test_size, random_state=random_state, stratify=labels
    )
    return X_train, X_test, y_train, y_test
