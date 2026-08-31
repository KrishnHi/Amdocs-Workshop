"""
Lab 1.2 Evaluator: Chain-of-Thought (CoT) Code Reviewer & Diagnostic Engine
"""

import re
from typing import Dict, Any, List

EXPECTED_SECTIONS = [
    "Specification & Edge-Case Matrix",
    "Step-by-Step Logic Trace",
    "Identified Defects",
    "Surgical Code Fix",
    "Verification Test Suite"
]

def test_loyalty_code(code_str: str) -> Dict[str, Any]:
    """
    Executes unit test assertions in an isolated environment on candidate Python fix.
    """
    results = {
        "passed_all": False,
        "passed_count": 0,
        "total_tests": 7,
        "test_diagnostics": []
    }
    
    cleaned = code_str.strip()
    
    local_scope = {}
    try:
        exec(cleaned, {}, local_scope)
    except Exception as e:
        results["test_diagnostics"].append(f"[FAIL] Execution Error: Syntax/Runtime error: {str(e)}")
        return results

    func = local_scope.get("calculate_loyalty_tier")
    if not func or not callable(func):
        results["test_diagnostics"].append("[FAIL] Signature Error: Function `calculate_loyalty_tier` was not defined or renamed.")
        return results

    test_cases = [
        ("Zero/Negative Spend ($0)", (0, 10, False), {"tier": "Inactive", "discount": 0.0}),
        ("Negative Spend (-$50)", (-50, 12, False), {"tier": "Inactive", "discount": 0.0}),
        ("Bronze Standard ($200, 3mo)", (200, 3, False), {"tier": "Bronze", "discount": 0.0}),
        ("Silver Boundary ($500, 6mo)", (500, 6, False), {"tier": "Silver", "discount": 0.10}),
        ("Gold Boundary ($2000, 12mo)", (2000, 12, False), {"tier": "Gold", "discount": 0.15}),
        ("Platinum Boundary ($5000, 24mo)", (5000, 24, False), {"tier": "Platinum", "discount": 0.20}),
        ("VIP Override ($10, 1mo, VIP)", (10, 1, True), {"tier": "Platinum", "discount": 0.20}),
    ]

    for name, args, expected in test_cases:
        try:
            actual = func(*args)
            if actual == expected:
                results["passed_count"] += 1
                results["test_diagnostics"].append(f"[PASS] Assertion: {name} validated.")
            else:
                results["test_diagnostics"].append(f"[FAIL] Assertion: {name} failed. Expected {expected}, got {actual}.")
        except Exception as e:
            results["test_diagnostics"].append(f"[FAIL] Exception: {name} raised exception: {str(e)}")

    if results["passed_count"] == results["total_tests"]:
        results["passed_all"] = True

    return results

def evaluate_cot_review(review_markdown: str) -> Dict[str, Any]:
    """
    Validates that the CoT review fulfills all 5 stages, includes dry run, and provides a working code fix.
    """
    evaluation = {
        "score": 0,
        "max_score": 100,
        "structure_score": 0,
        "code_test_score": 0,
        "missing_sections": [],
        "diagnostics": []
    }
    
    # 1. Structure Check (50 pts)
    found_sections = 0
    for sec in EXPECTED_SECTIONS:
        if re.search(re.escape(sec), review_markdown, re.IGNORECASE):
            found_sections += 1
            evaluation["diagnostics"].append(f"[PASS] Analytical Stage: {sec} present.")
        else:
            evaluation["missing_sections"].append(sec)
            evaluation["diagnostics"].append(f"[FAIL] Analytical Stage: Missing required header '{sec}'.")
            
    evaluation["structure_score"] = int((found_sections / len(EXPECTED_SECTIONS)) * 50)
    evaluation["score"] += evaluation["structure_score"]

    # 2. Logic Tracing Check (20 pts)
    if "5000" in review_markdown and ("> 5000" in review_markdown or ">=" in review_markdown):
        evaluation["score"] += 20
        evaluation["diagnostics"].append("[PASS] Logic Tracing: Boundary dry-run on $5,000 threshold verified.")
    else:
        evaluation["diagnostics"].append("[WARN] Logic Tracing: Incomplete boundary dry-run analysis.")

    # 3. Extract & Execute Code Fix (30 pts)
    py_blocks = re.findall(r"```python(.*?)```", review_markdown, re.DOTALL)
    candidate_code = None
    for block in py_blocks:
        if "def calculate_loyalty_tier" in block:
            candidate_code = block
            break

    if not candidate_code:
        code_match = re.search(r"def calculate_loyalty_tier\(.*?\n(?=(?:[^\s#]|\Z))", review_markdown, re.DOTALL)
        if code_match:
            candidate_code = code_match.group(0)

    if candidate_code:
        code_results = test_loyalty_code(candidate_code)
        if code_results["passed_all"]:
            evaluation["code_test_score"] += 30
            evaluation["score"] += 30
            evaluation["diagnostics"].append(f"[PASS] Unit Test Suite: All {code_results['total_tests']} assertions executed successfully.")
        else:
            partial = int((code_results["passed_count"] / code_results["total_tests"]) * 30)
            evaluation["code_test_score"] += partial
            evaluation["score"] += partial
            evaluation["diagnostics"].append(f"[WARN] Unit Test Suite: Passed {code_results['passed_count']}/{code_results['total_tests']} assertions.")
            evaluation["diagnostics"].extend(code_results["test_diagnostics"])
    else:
        evaluation["diagnostics"].append("[FAIL] Implementation: No Python block with `def calculate_loyalty_tier` found.")

    return evaluation
