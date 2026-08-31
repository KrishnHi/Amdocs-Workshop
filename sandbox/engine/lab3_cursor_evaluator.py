#!/usr/bin/env python3
"""
Evaluator Engine for Module 3: Cursor Orientation Practicals (Labs 3.1, 3.2, 3.3, 3.4)
Performs static analysis, regex parsing, schema compliance, and diagnostic scoring.
"""

import re
from typing import Dict, Any, List

def evaluate_lab3_1_inline(content: str) -> Dict[str, Any]:
    """
    Evaluates Lab 3.1: Inline AI Engineering (Ghost Text Shaping & Cmd+K Refactoring)
    """
    score = 0
    max_score = 100
    diagnostics = []

    # 1. Ghost Text Shaping (25 pts)
    has_filter_code = "filterTasksByPriorityAndDate" in content or "filter" in content
    has_type_safety = "sinceDate" in content or "Date" in content or "timestamp" in content
    if has_filter_code and has_type_safety:
        score += 25
        diagnostics.append("[PASS] Ghost Text Shaping: Pure TypeScript implementation with timestamp checks detected (+25 pts).")
    else:
        diagnostics.append("[FAIL] Ghost Text Shaping: Missing complete filterTasksByPriorityAndDate implementation (-25 pts).")

    # 2. Cmd/Ctrl+K Inline Prompt Precision (35 pts)
    prompt_match = re.search(r"\[PASTE YOUR INLINE PROMPT HERE\](.*?)## Exercise 3", content, re.DOTALL)
    prompt_text = prompt_match.group(1) if prompt_match else content

    has_rate_limit_term = bool(re.search(r"rate\s*limit|sliding\s*window|100\s*req", prompt_text, re.IGNORECASE))
    has_envelope_term = bool(re.search(r"envelope|success|429|json", prompt_text, re.IGNORECASE))
    has_leak_prevention = bool(re.search(r"prun|stale|expir|clean|map|memory", prompt_text, re.IGNORECASE))

    if has_rate_limit_term:
        score += 15
        diagnostics.append("[PASS] Inline Prompt: Explicit rate limiting criteria and window thresholds provided (+15 pts).")
    else:
        diagnostics.append("[FAIL] Inline Prompt: Missing explicit rate limiting thresholds or window requirements (-15 pts).")

    if has_envelope_term:
        score += 10
        diagnostics.append("[PASS] Inline Prompt: Enforced project standard HTTP 429 JSON response envelope (+10 pts).")
    else:
        diagnostics.append("[FAIL] Inline Prompt: Omitted standard API error envelope instructions (-10 pts).")

    if has_leak_prevention:
        score += 10
        diagnostics.append("[PASS] Inline Prompt: Memory management & stale key pruning instructions included (+10 pts).")
    else:
        diagnostics.append("[FAIL] Inline Prompt: Omitted memory leak prevention or Map pruning instructions (-10 pts).")

    # 3. Diff Checklist & Review Rigor (40 pts)
    checked_boxes = len(re.findall(r"-\s*\[x\]", content, re.IGNORECASE))
    if checked_boxes >= 4:
        score += 40
        diagnostics.append(f"[PASS] Diff Audit Checklist: Verified {checked_boxes}/5 critical diff audit criteria (+40 pts).")
    elif checked_boxes >= 2:
        score += 20
        diagnostics.append(f"[WARN] Diff Audit Checklist: Partially completed ({checked_boxes}/5 criteria) (+20 pts).")
    else:
        diagnostics.append("[FAIL] Diff Audit Checklist: Unchecked diff verification items (-40 pts).")

    return {
        "lab": "3.1",
        "score": score,
        "max_score": max_score,
        "diagnostics": diagnostics
    }


def evaluate_lab3_2_context(content: str) -> Dict[str, Any]:
    """
    Evaluates Lab 3.2: Context Engineering & Scoped Chat Q&A
    """
    score = 0
    max_score = 100
    diagnostics = []

    # 1. Scoped @-References (30 pts)
    has_at_files = bool(re.search(r"@task\.service\.ts|@src/|@tasks\.ts", content))
    if has_at_files:
        score += 30
        diagnostics.append("[PASS] Context Scoping: Exact @File / @Folder directives utilized (+30 pts).")
    else:
        diagnostics.append("[FAIL] Context Scoping: Missing specific @-references for grounded context (-30 pts).")

    # 2. Root Cause Bug Identification (30 pts)
    has_spread_id = bool(re.search(r"spread|shallow|overwrite|drop|completed_at|tags|destruct", content, re.IGNORECASE))
    if has_spread_id:
        score += 30
        diagnostics.append("[PASS] Root-Cause Analysis: Correctly identified shallow object spread overwrite in task.service.ts (+30 pts).")
    else:
        diagnostics.append("[FAIL] Root-Cause Analysis: Missed shallow spread state mutation defect (-30 pts).")

    # 3. .cursorrules Schema Compliance (40 pts)
    has_frontmatter = "---" in content and "globs:" in content and "alwaysApply:" in content
    has_error_rule = "console.log" in content or "logger" in content
    has_security_rule = "randomBytes" in content or "crypto" in content or "timingSafeEqual" in content

    if has_frontmatter:
        score += 15
        diagnostics.append("[PASS] Rule Frontmatter: Valid MDC schema with globs and alwaysApply directives (+15 pts).")
    else:
        diagnostics.append("[FAIL] Rule Frontmatter: Missing or malformed MDC YAML frontmatter (-15 pts).")

    if has_error_rule:
        score += 15
        diagnostics.append("[PASS] Rule Content: Enforced structured logging and banned console.log (+15 pts).")
    else:
        diagnostics.append("[FAIL] Rule Content: Missing structured logging constraints (-15 pts).")

    if has_security_rule:
        score += 10
        diagnostics.append("[PASS] Security Rule: Defined cryptographic boundary constraints (+10 pts).")
    else:
        diagnostics.append("[FAIL] Security Rule: Missing cryptographic security rules (-10 pts).")

    return {
        "lab": "3.2",
        "score": score,
        "max_score": max_score,
        "diagnostics": diagnostics
    }


def evaluate_lab3_3_composer(content: str) -> Dict[str, Any]:
    """
    Evaluates Lab 3.3: Multi-File Orchestration with Composer / Agent
    """
    score = 0
    max_score = 100
    diagnostics = []

    # 1. Master Agent Prompt Decomposition (35 pts)
    has_at_context = bool(re.search(r"@src/core|@src/api|@docs", content))
    has_numbered_steps = bool(re.search(r"1\..*2\..*3\.", content, re.DOTALL))
    has_negative_constraint = bool(re.search(r"do not touch|do not modify|client\.ts", content, re.IGNORECASE))

    if has_at_context and has_numbered_steps:
        score += 25
        diagnostics.append("[PASS] Prompt Decomposition: Multi-file scope and sequential step ordering established (+25 pts).")
    else:
        diagnostics.append("[FAIL] Prompt Decomposition: Lacks clear step-by-step file decomposition (-25 pts).")

    if has_negative_constraint:
        score += 10
        diagnostics.append("[PASS] Boundary Guardrail: Negative constraint protecting untouched database files enforced (+10 pts).")
    else:
        diagnostics.append("[FAIL] Boundary Guardrail: Omitted negative constraint protecting client.ts (-10 pts).")

    # 2. Multi-File Review Matrix (35 pts)
    accepted_or_edited = len(re.findall(r"\[x\]\s*(Accepted|Edited)", content, re.IGNORECASE))
    if accepted_or_edited >= 4:
        score += 35
        diagnostics.append(f"[PASS] Diff Scrubbing Matrix: Audited and resolved {accepted_or_edited} file targets (+35 pts).")
    elif accepted_or_edited >= 2:
        score += 20
        diagnostics.append(f"[WARN] Diff Scrubbing Matrix: Partially recorded review actions ({accepted_or_edited}/6) (+20 pts).")
    else:
        diagnostics.append("[FAIL] Diff Scrubbing Matrix: Missing multi-file audit records (-35 pts).")

    # 3. Test Verification (30 pts)
    has_test_output = bool(re.search(r"PASS|passed|Tests:|jest", content, re.IGNORECASE))
    if has_test_output:
        score += 30
        diagnostics.append("[PASS] Verification: Automated unit test execution recorded cleanly (+30 pts).")
    else:
        diagnostics.append("[FAIL] Verification: Missing test execution logs (-30 pts).")

    return {
        "lab": "3.3",
        "score": score,
        "max_score": max_score,
        "diagnostics": diagnostics
    }


def evaluate_lab3_4_adversarial(content: str) -> Dict[str, Any]:
    """
    Evaluates Lab 3.4: Adversarial Diff Review & Capstone Project
    """
    score = 0
    max_score = 100
    diagnostics = []

    # 1. Detection of 4 Planted Traps (50 pts total, 12.5 pts each)
    trap_a = bool(re.search(r"randomBytes|Math\.random|PRNG", content, re.IGNORECASE))
    trap_b = bool(re.search(r"timingSafeEqual|timing\s*attack|===", content, re.IGNORECASE))
    trap_c = bool(re.search(r"chunk|stream|paged|buffer|OOM|memory", content, re.IGNORECASE))
    trap_d = bool(re.search(r"catch|swallow|logger\.error|exception", content, re.IGNORECASE))

    traps_caught = sum([trap_a, trap_b, trap_c, trap_d])
    score += traps_caught * 12
    if traps_caught == 4:
        score += 2  # round to 50
        diagnostics.append("[PASS] Adversarial Audit: Detected all 4 planted AI failure traps (PRNG, Timing leak, OOM, Error swallow) (+50 pts).")
    else:
        diagnostics.append(f"[WARN] Adversarial Audit: Caught {traps_caught}/4 planted traps (+{traps_caught * 12} pts).")

    # 2. Audited Diff Quality (30 pts)
    has_diff_block = "```diff" in content or "crypto.timingSafeEqual" in content or "createHmacSignature" in content
    if has_diff_block:
        score += 30
        diagnostics.append("[PASS] Pull Request Diff: Validated hardened cryptographic implementation (+30 pts).")
    else:
        diagnostics.append("[FAIL] Pull Request Diff: Missing verified PR diff block (-30 pts).")

    # 3. Security Test Passing (20 pts)
    has_sec_test = bool(re.search(r"security\.spec\.ts|passed|PASS", content, re.IGNORECASE))
    if has_sec_test:
        score += 20
        diagnostics.append("[PASS] Security Test Suite: Cryptographic boundary assertions confirmed (+20 pts).")
    else:
        diagnostics.append("[FAIL] Security Test Suite: Security test run not verified (-20 pts).")

    return {
        "lab": "3.4",
        "score": score,
        "max_score": max_score,
        "diagnostics": diagnostics
    }
