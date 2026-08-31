# Trainee Practical Assessment: Practical 1.2

**Trainee Name**:Krishna Hitnalikar_  
**Employee ID**: 215677
**Date**: ________31/08/2026______________  

---

## Instructions
Complete the Task Decomposition Blueprint in Section 1 and craft your master Chain-of-Thought review prompt in Section 2. Execute the prompt against the target code and paste the 5-stage markdown output in Section 3.

---

## Section 1: Task Decomposition Blueprint

| Stage | Stage Title | Specific Analytical Directive |
| :--- | :--- | :--- |
| **Stage 1** | Requirement Analysis & Boundary Mapping | Enumerate all tier thresholds and expected outputs for boundary, below-boundary, above-boundary, zero/negative spend, and VIP override; record expected discounts and business rules. |
| **Stage 2** | Trace Execution & Dry Run | Perform a line-by-line dry-run trace for spend_amount=5000, account_age_months=24, is_vip=False; evaluate each branch and record boolean results and control flow. |
| **Stage 3** | Root Cause Defect Diagnosis | Identify logic defects (e.g., misuse of '>' vs '>='), input-validation gaps (None, negative tenure, invalid types), and rank severity [High|Medium|Low] with impact analysis. |
| **Stage 4** | Surgical Code Refactoring | Produce a minimal, backward-compatible fix preserving function name/signature: replace strict inequalities with inclusive ones, add defensive checks and type annotations, keep VIP override. |
| **Stage 5** | Regression Test Assertions | Provide 5–7 standalone Python `assert` statements verifying negative/zero spend, Bronze, exact Silver/Gold/Platinum boundaries, and VIP override; ensure assertions run and pass.

---

## Section 2: Master Chain-of-Thought Prompt Template

```text
You are a Principal Software Engineer performing a rigorous pre-merge code review. Follow these constraints:
1) Do NOT add external third-party libraries — use Python 3.10+ standard library only.
2) Do NOT change the function name, parameters, or return structure.
3) Perform explicit dry-run evaluation for boundary values before proposing any code changes.
4) Output exactly the following five markdown section headers and content in order:
   ### 1. Specification & Edge-Case Matrix
   ### 2. Step-by-Step Logic Trace (Chain-of-Thought)
   ### 3. Identified Defects & Severity
   ### 4. Surgical Code Fix
   ### 5. Verification Test Suite

Task:
- I will provide the target source code as {{SOURCE_CODE}} inside <target_code>...</target_code>.
- Produce each section as follows:

### 1. Specification & Edge-Case Matrix
- Build a concise table containing: case description, spend_amount, account_age_months, is_vip, expected tier, expected discount.
- Include: negative spend, zero spend, bronze example, exact silver boundary, exact gold boundary, exact platinum boundary, VIP override.

### 2. Step-by-Step Logic Trace (Chain-of-Thought)
- Dry-run the given function for: spend_amount = 5000, account_age_months = 24, is_vip = False.
- Show evaluation of each conditional (with actual boolean results) and explain why the function returns its final tier/discount.

### 3. Identified Defects & Severity
- List every defect found, label severity as [High | Medium | Low], and briefly explain impact and likelihood.
- Explicitly call out any misuse of '>' vs '>=' and missing input validations.

### 4. Surgical Code Fix
- Provide the corrected Python function only (preserve original function name and parameter names).
- Include concise type annotations and defensive input validation (None checks, invalid types, negative tenure).
- Keep implementation minimal and readable; no new dependencies.

### 5. Verification Test Suite
- Provide 5–7 executable Python `assert` statements that verify boundaries and VIP override.
- These `assert`s must run as-is with the corrected function and pass.

Finally: after the five sections, include a one-line summary of why the fix is correct.

<target_code>
{{SOURCE_CODE}}
</target_code>
