"""
Lab 2.2 Evaluator: Architectural Fallacy & Cognitive Bias Assessment
"""

import re
from typing import Dict, Any, List

FALLACY_GROUND_TRUTH = {
    "Excerpt A": {
        "expected": "False Dilemma",
        "aliases": ["false dilemma", "either/or", "black or white", "black-and-white", "false dichotomy"]
    },
    "Excerpt B": {
        "expected": "False Cause",
        "aliases": ["false cause", "post hoc", "correlation", "causation", "questionable cause"]
    },
    "Excerpt C": {
        "expected": "Straw Man",
        "aliases": ["straw man", "strawman", "caricature", "distorting"]
    },
    "Excerpt D": {
        "expected": "Appeal to Authority",
        "aliases": ["appeal to authority", "bandwagon", "ad verecundiam", "influencer", "popularity"]
    }
}

ASSUMPTIONS_KEYWORDS = [
    ("DevOps & Operational Competency", ["skill", "devops", "kubernetes", "kafka", "training", "expertise"]),
    ("Network Latency & Distributed Complexity", ["network", "latency", "distributed", "saga", "transaction", "hop"]),
    ("Release Cadence Root Cause", ["ci/cd", "pipeline", "testing", "qa", "bottleneck", "automation"])
]

def evaluate_fallacy_audit(audit_text: str) -> Dict[str, Any]:
    """
    Evaluates trainee's identification of logical fallacies and unstated assumptions.
    """
    results = {
        "score": 0,
        "max_score": 100,
        "fallacies_found": 0,
        "assumptions_found": 0,
        "diagnostics": []
    }
    
    text_lower = audit_text.lower()
    
    # 1. Fallacy Identification (60 pts)
    for excerpt, data in FALLACY_GROUND_TRUTH.items():
        found = False
        for alias in data["aliases"]:
            if alias in text_lower:
                found = True
                break
        if found:
            results["fallacies_found"] += 1
            results["score"] += 15
            results["diagnostics"].append(f"[PASS] Fallacy Taxonomy ({excerpt}): Accurately classified as '{data['expected']}'.")
        else:
            results["diagnostics"].append(f"[FAIL] Fallacy Taxonomy ({excerpt}): Missed classification for '{data['expected']}'.")

    # 2. Unstated Assumptions (30 pts)
    for name, kws in ASSUMPTIONS_KEYWORDS:
        found_kw = False
        for kw in kws:
            if kw in text_lower:
                found_kw = True
                break
        if found_kw:
            results["assumptions_found"] += 1
            results["score"] += 10
            results["diagnostics"].append(f"[PASS] Assumption Analysis: Unmasked operational prerequisite '{name}'.")
        else:
            results["diagnostics"].append(f"[WARN] Assumption Analysis: Omitted hidden assumption regarding '{name}'.")

    # 3. Phased Counter-Proposal Check (10 pts)
    if any(term in text_lower for term in ["modular", "ci/cd", "phase", "incremental", "monolith", "metric"]):
        results["score"] += 10
        results["diagnostics"].append("[PASS] Strategic Roadmap: Formulated incremental, risk-managed modernization proposal.")
    else:
        results["diagnostics"].append("[WARN] Strategic Roadmap: Counter-proposal lacks phased technical deliverables.")

    return results
