"""
Sandbox Evaluator Engine Package
Contains evaluation engines for Prompt Engineering, Critical Thinking, and Cursor Orientation practicals.
"""

from .lab1_triage_evaluator import evaluate_triage_output, test_triage_prompt
from .lab1_cot_evaluator import evaluate_cot_review, test_loyalty_code
from .lab2_claim_evaluator import evaluate_claim_audit
from .lab2_fallacy_evaluator import evaluate_fallacy_audit
from .lab3_cursor_evaluator import (
    evaluate_lab3_1_inline,
    evaluate_lab3_2_context,
    evaluate_lab3_3_composer,
    evaluate_lab3_4_adversarial,
)

__all__ = [
    "evaluate_triage_output",
    "test_triage_prompt",
    "evaluate_cot_review",
    "test_loyalty_code",
    "evaluate_claim_audit",
    "evaluate_fallacy_audit",
    "evaluate_lab3_1_inline",
    "evaluate_lab3_2_context",
    "evaluate_lab3_3_composer",
    "evaluate_lab3_4_adversarial",
]
