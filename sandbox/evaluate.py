#!/usr/bin/env python3
"""
Automated CLI Evaluation Harness for Prompt Engineering, Critical Thinking & Cursor Orientation Practicals
Usage:
    python sandbox/evaluate.py --all-solutions
    python sandbox/evaluate.py --lab 1.1 --file labs/01_prompt_engineering/lab1_structured_triage/exercise_starter.md
    python sandbox/evaluate.py --lab 3.1 --file labs/03_cursor_orientation/lab1_inline_engineering/solution_reference.md
"""

import os
import sys
import argparse
from pathlib import Path

# Add workspace root to sys.path
WORKSPACE_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(WORKSPACE_ROOT))

from sandbox.engine.lab1_triage_evaluator import evaluate_triage_output, test_triage_prompt
from sandbox.engine.lab1_cot_evaluator import evaluate_cot_review
from sandbox.engine.lab2_claim_evaluator import evaluate_claim_audit
from sandbox.engine.lab2_fallacy_evaluator import evaluate_fallacy_audit
from sandbox.engine.lab3_cursor_evaluator import (
    evaluate_lab3_1_inline,
    evaluate_lab3_2_context,
    evaluate_lab3_3_composer,
    evaluate_lab3_4_adversarial,
)

GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
BOLD = "\033[1m"
RESET = "\033[0m"

def print_header(title: str):
    print(f"\n{BOLD}{CYAN}{'='*64}{RESET}")
    print(f"{BOLD}{CYAN} [EVAL] {title}{RESET}")
    print(f"{BOLD}{CYAN}{'='*64}{RESET}")

def print_scorecard(score: int, max_score: int, diagnostics: list):
    percentage = (score / max_score) * 100
    color = GREEN if percentage >= 80 else (YELLOW if percentage >= 50 else RED)
    status_label = "[PASSED]" if percentage >= 80 else ("[CONDITIONAL PASS]" if percentage >= 50 else "[ACTION REQUIRED]")
    print(f"\n{BOLD}Evaluation Result: {color}{score}/{max_score} ({percentage:.1f}%) {status_label}{RESET}\n")
    print(f"{BOLD}Diagnostic Breakdown:{RESET}")
    for item in diagnostics:
        print(f"  {item}")
    print()

def run_lab1_1(file_path: Path):
    print_header("Evaluating Lab 1.1: Incident Triage & Structured Extraction")
    if not file_path.exists():
        print(f"{RED}[ERROR] Target file not found: {file_path}{RESET}")
        return

    content = file_path.read_text(encoding="utf-8")
    anatomy = test_triage_prompt(content)
    print(f"{BOLD}1. Prompt Structural Anatomy Analysis ({anatomy['anatomy_score']}/100):{RESET}")
    for fb in anatomy["feedback"]:
        print(f"  {fb}")

    print(f"\n{BOLD}2. Test Cases Validation Matrix:{RESET}")
    total_case_score = 0
    json_blocks = content.split("```json")
    if len(json_blocks) > 1:
        cases = ["A", "B", "C"]
        for idx, block in enumerate(json_blocks[1:4]):
            case_letter = cases[idx] if idx < len(cases) else f"Case {idx+1}"
            raw_json = block.split("```")[0].strip()
            eval_res = evaluate_triage_output(raw_json, expected_case=case_letter)
            total_case_score += eval_res["score"]
            print(f"\n  {BOLD}--- Test Case {case_letter} Evaluation ({eval_res['score']}/100) ---{RESET}")
            for d in eval_res["diagnostics"]:
                print(f"    {d}")
        avg_score = int((anatomy["anatomy_score"] * 0.4) + ((total_case_score / 3) * 0.6))
        print_scorecard(avg_score, 100, ["[INFO] Automated verification against SLA matrix & injection tests completed."])
    else:
        print(f"{YELLOW}[WARN] No JSON output blocks found in file. Execute test cases and record JSON in worksheet.{RESET}")
        print_scorecard(anatomy["anatomy_score"], 100, anatomy["feedback"])

def run_lab1_2(file_path: Path):
    print_header("Evaluating Lab 1.2: Chain-of-Thought Code Reviewer")
    if not file_path.exists():
        print(f"{RED}[ERROR] Target file not found: {file_path}{RESET}")
        return
    content = file_path.read_text(encoding="utf-8")
    res = evaluate_cot_review(content)
    print_scorecard(res["score"], res["max_score"], res["diagnostics"])

def run_lab2_1(file_path: Path):
    print_header("Evaluating Lab 2.1: AI Hallucination & Evidence Audit Matrix")
    if not file_path.exists():
        print(f"{RED}[ERROR] Target file not found: {file_path}{RESET}")
        return
    content = file_path.read_text(encoding="utf-8")
    res = evaluate_claim_audit(content)
    print_scorecard(res["score"], res["max_score"], res["diagnostics"])

def run_lab2_2(file_path: Path):
    print_header("Evaluating Lab 2.2: Architectural Fallacy & Cognitive Bias Assessment")
    if not file_path.exists():
        print(f"{RED}[ERROR] Target file not found: {file_path}{RESET}")
        return
    content = file_path.read_text(encoding="utf-8")
    res = evaluate_fallacy_audit(content)
    print_scorecard(res["score"], res["max_score"], res["diagnostics"])

def run_lab3_1(file_path: Path):
    print_header("Evaluating Lab 3.1: Inline AI Engineering (Ghost Text & Cmd+K)")
    if not file_path.exists():
        print(f"{RED}[ERROR] Target file not found: {file_path}{RESET}")
        return
    content = file_path.read_text(encoding="utf-8")
    res = evaluate_lab3_1_inline(content)
    print_scorecard(res["score"], res["max_score"], res["diagnostics"])

def run_lab3_2(file_path: Path):
    print_header("Evaluating Lab 3.2: Context Engineering & Scoped Chat Q&A")
    if not file_path.exists():
        print(f"{RED}[ERROR] Target file not found: {file_path}{RESET}")
        return
    content = file_path.read_text(encoding="utf-8")
    res = evaluate_lab3_2_context(content)
    print_scorecard(res["score"], res["max_score"], res["diagnostics"])

def run_lab3_3(file_path: Path):
    print_header("Evaluating Lab 3.3: Multi-File Orchestration with Composer")
    if not file_path.exists():
        print(f"{RED}[ERROR] Target file not found: {file_path}{RESET}")
        return
    content = file_path.read_text(encoding="utf-8")
    res = evaluate_lab3_3_composer(content)
    print_scorecard(res["score"], res["max_score"], res["diagnostics"])

def run_lab3_4(file_path: Path):
    print_header("Evaluating Lab 3.4: Adversarial Diff Review & Capstone Project")
    if not file_path.exists():
        print(f"{RED}[ERROR] Target file not found: {file_path}{RESET}")
        return
    content = file_path.read_text(encoding="utf-8")
    res = evaluate_lab3_4_adversarial(content)
    print_scorecard(res["score"], res["max_score"], res["diagnostics"])

def run_all_solutions():
    print(f"\n{BOLD}{GREEN}{'='*64}")
    print(" [SUITE] EXECUTING AUTOMATED VERIFICATION ON ALL INSTRUCTOR SPECIFICATIONS")
    print(f"{'='*64}{RESET}")
    
    sol_1_1 = WORKSPACE_ROOT / "labs/01_prompt_engineering/lab1_structured_triage/solution_reference.md"
    sol_1_2 = WORKSPACE_ROOT / "labs/01_prompt_engineering/lab2_cot_code_reviewer/solution_reference.md"
    sol_2_1 = WORKSPACE_ROOT / "labs/02_critical_thinking/lab1_hallucination_audit/solution_reference.md"
    sol_2_2 = WORKSPACE_ROOT / "labs/02_critical_thinking/lab2_fallacy_buster/solution_reference.md"
    sol_3_1 = WORKSPACE_ROOT / "labs/03_cursor_orientation/lab1_inline_engineering/solution_reference.md"
    sol_3_2 = WORKSPACE_ROOT / "labs/03_cursor_orientation/lab2_context_and_chat_qa/solution_reference.md"
    sol_3_3 = WORKSPACE_ROOT / "labs/03_cursor_orientation/lab3_multi_file_composer/solution_reference.md"
    sol_3_4 = WORKSPACE_ROOT / "labs/03_cursor_orientation/lab4_adversarial_diff_review_project/solution_reference.md"

    run_lab1_1(sol_1_1)
    run_lab1_2(sol_1_2)
    run_lab2_1(sol_2_1)
    run_lab2_2(sol_2_2)
    run_lab3_1(sol_3_1)
    run_lab3_2(sol_3_2)
    run_lab3_3(sol_3_3)
    run_lab3_4(sol_3_4)

def main():
    parser = argparse.ArgumentParser(description="Automated Evaluation Harness for AI Engineering Practicals")
    parser.add_argument("--lab", choices=["1.1", "1.2", "2.1", "2.2", "3.1", "3.2", "3.3", "3.4"], help="Specify lab identifier to evaluate")
    parser.add_argument("--file", type=str, help="Path to trainee markdown worksheet")
    parser.add_argument("--all-solutions", action="store_true", help="Execute automated evaluation across all reference solutions")

    args = parser.parse_args()

    if args.all_solutions:
        run_all_solutions()
        return

    if not args.lab or not args.file:
        parser.print_help()
        sys.exit(1)

    file_path = Path(args.file)
    lab_dispatch = {
        "1.1": run_lab1_1,
        "1.2": run_lab1_2,
        "2.1": run_lab2_1,
        "2.2": run_lab2_2,
        "3.1": run_lab3_1,
        "3.2": run_lab3_2,
        "3.3": run_lab3_3,
        "3.4": run_lab3_4,
    }

    if args.lab in lab_dispatch:
        lab_dispatch[args.lab](file_path)

if __name__ == "__main__":
    main()
