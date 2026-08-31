# Practical 1.2: Chain-of-Thought Code Review & Defect Diagnostic Engine

**Module**: Module 1 - Prompt Engineering  
**Level**: Associate / Graduate Trainee  
**Duration**: 45 Minutes  
**Core Technical Competencies**: Task Decomposition, Multi-Stage Chain-of-Thought (CoT) Prompting, Boundary Condition Dry-Run Tracing, Zero-Hallucination Guardrails, Regression Assertion Suites.

---

## 1. Business Context & Problem Specification

Junior software engineers frequently utilize AI assistants to accelerate code reviews and static analysis during pull request validation. However, naive prompting approaches (`"Review this code and fix the bugs"`) exhibit significant engineering flaws:
- **Superficial Analysis**: Highlights stylistic suggestions (e.g. docstrings) while overlooking critical boundary condition bugs.
- **Uncontrolled Scope Expansion**: Unnecessarily refactors working code, introducing unrequested external dependencies or hallucinated framework methods.
- **Premature Token Generation**: Attempts to generate code immediately without dry-running execution paths, missing subtle inequality off-by-one errors.

In this laboratory, trainees construct a **Multi-Stage Chain-of-Thought Prompt** that decomposes code analysis into five structured analytical stages prior to code generation.

---

## 2. Target Implementation (E-Commerce Loyalty Calculation)

The following Python implementation contains boundary defects:

```python
def calculate_loyalty_tier(spend_amount, account_age_months, is_vip=False):
    """
    Tier Specification:
    - 'Platinum': Spend >= $5,000 AND account_age >= 24 months, OR is_vip is True.
    - 'Gold': Spend >= $2,000 AND account_age >= 12 months.
    - 'Silver': Spend >= $500 AND account_age >= 6 months.
    - 'Bronze': Any active account with positive spend.
    - 'Inactive': Spend <= 0.
    
    Discount Structure:
    - Platinum: 20%
    - Gold: 15%
    - Silver: 10%
    - Bronze: 0%
    - Inactive: 0%
    """
    # Defective Implementation:
    if spend_amount <= 0:
        return {"tier": "Inactive", "discount": 0.0}
    
    if is_vip:
        tier = "Platinum"
        discount = 0.20
    elif spend_amount > 5000 and account_age_months > 24:
        tier = "Platinum"
        discount = 0.20
    elif spend_amount > 2000 and account_age_months > 12:
        tier = "Gold"
        discount = 0.15
    elif spend_amount > 500 and account_age_months > 6:
        tier = "Silver"
        discount = 0.10
    else:
        tier = "Bronze"
        discount = 0.0

    return {"tier": tier, "discount": discount}
```

### Known Target Defects:
1. **Strict Inequality Operator Defect**: Utilizes `>` rather than `>=` across all tier threshold evaluations, misclassifying boundary customers (e.g., exactly $5,000 and 24 months).
2. **Defensive Input Validation**: Lacks type guards and null checks for invalid parameter entries.

---

## 3. Mandatory 5-Stage Output Structure

The prompt must force the model to output exactly five standardized sections:

1. `### 1. Specification & Edge-Case Matrix`: Comprehensive mapping of input boundaries to expected outputs.
2. `### 2. Step-by-Step Logic Trace (Chain-of-Thought)`: Execution trace of a customer at boundary threshold ($5,000, 24 mo).
3. `### 3. Identified Defects & Severity`: Categorized defect catalog (`High`, `Medium`, `Low`).
4. `### 4. Surgical Code Fix`: Corrected Python function maintaining original signature and standard library dependencies.
5. `### 5. Verification Test Suite`: Standalone Python `assert` statements covering all boundary states.

---

## 4. Trainee Deliverables

Open [`exercise_starter.md`](file:///Users/aaryankumar/Documents/promptengg/labs/01_prompt_engineering/lab2_cot_code_reviewer/exercise_starter.md) and execute:
- **Phase 1**: Task Decomposition Blueprint mapping.
- **Phase 2**: Master Chain-of-Thought Prompt Construction.
- **Phase 3**: Execution validation and assertion execution.
