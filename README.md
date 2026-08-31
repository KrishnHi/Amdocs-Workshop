# Technical Enablement Programme: Applied AI, Critical Verification & Cursor IDE Practicals

**Target Audience**: Associate Software Engineers, Graduate Trainees & AI Practitioners  
**Curriculum**: Applied Artificial Intelligence in Enterprise Software Engineering (Techademy Corporate Training Series)

---

## Executive Overview

This repository contains eight hands-on practical laboratories designed to develop core competencies in Large Language Model (LLM) orchestration, deterministic schema control, critical output auditing, and AI-assisted development using Cursor IDE.

| Module | Identifier | Laboratory Title | Core Technical Competencies |
| :--- | :--- | :--- | :--- |
| **Module 1: Prompt Engineering** | **Lab 1.1** | [Incident Triage & Structured Extraction Engine](file:///Users/aaryankumar/Documents/promptengg/labs/01_prompt_engineering/lab1_structured_triage/README.md) | Prompt Anatomy, JSON Schema Enforcement, Delimiter Hygiene, Adversarial Injection Defense |
| **Module 1: Prompt Engineering** | **Lab 1.2** | [Chain-of-Thought Code Review & Defect Diagnostic Engine](file:///Users/aaryankumar/Documents/promptengg/labs/01_prompt_engineering/lab2_cot_code_reviewer/README.md) | Task Decomposition, Step-by-Step Logic Tracing, Boundary Value Verification, Zero-Hallucination Guardrails |
| **Module 2: Critical Thinking** | **Lab 2.1** | [AI Hallucination & Empirical Evidence Audit Matrix](file:///Users/aaryankumar/Documents/promptengg/labs/02_critical_thinking/lab1_hallucination_audit/README.md) | Claim Taxonomy (Fact vs. Inference vs. Opinion vs. Hallucination), Fabricated API Detection, Primary Source Corroboration |
| **Module 2: Critical Thinking** | **Lab 2.2** | [Architectural Fallacy & Cognitive Bias Assessment](file:///Users/aaryankumar/Documents/promptengg/labs/02_critical_thinking/lab2_fallacy_buster/README.md) | Logical Fallacy Identification (False Dilemma, False Cause, Straw Man), Unstated Assumption Extraction, Phased Modernization Planning |
| **Module 3: Cursor Orientation** | **Lab 3.1** | [Inline AI Engineering (Ghost Text & Cmd+K)](file:///Users/aaryankumar/Documents/promptengg/labs/03_cursor_orientation/lab1_inline_engineering/README.md) | Autocomplete Shaping, In-Place Refactoring (`Cmd/Ctrl+K`), Memory Leak Cleanup, Local Scope Preservation |
| **Module 3: Cursor Orientation** | **Lab 3.2** | [Context Engineering & Grounded Codebase Q&A](file:///Users/aaryankumar/Documents/promptengg/labs/03_cursor_orientation/lab2_context_and_chat_qa/README.md) | Vector Indexing, Scoped `@` Directives (`@Files`, `@Docs`), Rule Engineering (`.cursor/rules/*.mdc`), Root-Cause Tracing |
| **Module 3: Cursor Orientation** | **Lab 3.3** | [Multi-File Orchestration with Composer / Agent](file:///Users/aaryankumar/Documents/promptengg/labs/03_cursor_orientation/lab3_multi_file_composer/README.md) | Multi-File Agent Execution (`Cmd/Ctrl+I`), Cross-Layer Type Synchronization, Multi-File Diff Scrubbing, Test Verification |
| **Module 3: Cursor Orientation** | **Lab 3.4** | [Adversarial Diff Auditing & Capstone Project](file:///Users/aaryankumar/Documents/promptengg/labs/03_cursor_orientation/lab4_adversarial_diff_review_project/README.md) | "The Critical Eye" Red-Teaming, 4 Planted Vulnerability Traps (Insecure PRNG, Timing Leaks, OOM Buffers, Silent Catch), PR Hardening |

---

## Workspace Structure

```tree
promptengg/
├── README.md
├── sandbox/
│   ├── README.md                      # Testbench operational guide
│   ├── evaluate.py                    # Automated CLI evaluation harness (8 Labs)
│   ├── engine/                        # Static analysis and verification engines
│   │   ├── lab1_triage_evaluator.py   # Schema and SLA compliance validator
│   │   ├── lab1_cot_evaluator.py      # Assertion and CoT structure evaluator
│   │   ├── lab2_claim_evaluator.py    # Claim categorization comparator
│   │   ├── lab2_fallacy_evaluator.py  # Fallacy and assumption auditor
│   │   └── lab3_cursor_evaluator.py   # Cursor prompts, .cursorrules, & diff auditor
│   ├── taskpulse_engine/              # Realistic TypeScript/Express codebase for Cursor
│   │   ├── .cursor/rules/             # MDC project rule definitions
│   │   ├── src/                       # API routers, models, services, & utilities
│   │   ├── tests/                     # Unit and adversarial security test suites
│   │   └── package.json               # Sandbox dependencies and scripts
│   └── web/                           # Enterprise Web Sandbox UI (8 Interactive Labs)
│       ├── index.html                 # Interactive testbench dashboard
│       ├── style.css                  # Enterprise design system
│       └── app.js                     # Client evaluation and state management
└── labs/
    ├── 01_prompt_engineering/
    │   ├── lab1_structured_triage/    # Incident triage problem & worksheets
    │   └── lab2_cot_code_reviewer/    # 5-stage CoT logic reviewer
    ├── 02_critical_thinking/
    │   ├── lab1_hallucination_audit/  # Hallucination matrix & empirical citations
    │   └── lab2_fallacy_buster/       # Fallacy catalog & modernization roadmap
    └── 03_cursor_orientation/
        ├── lab1_inline_engineering/   # Ghost text shaping & Cmd+K refactoring
        ├── lab2_context_and_chat_qa/  # Scoped context & .cursorrules
        ├── lab3_multi_file_composer/  # Multi-file agent orchestration
        └── lab4_adversarial_diff_review_project/ # Capstone red-team challenge
```

---

## Operational Instructions

### 1. Interactive Web Testbench
Launch the local web sandbox environment:
```bash
python3 -m http.server 3000 --directory sandbox/web
```
Navigate to `http://localhost:3000` in any standard modern web browser.

### 2. Automated CLI Verification Harness
Validate trainee markdown worksheets programmatically:
```bash
# Run automated verification across all 8 reference solutions
python3 sandbox/evaluate.py --all-solutions

# Evaluate individual module practicals:
python3 sandbox/evaluate.py --lab 1.1 --file labs/01_prompt_engineering/lab1_structured_triage/exercise_starter.md
python3 sandbox/evaluate.py --lab 1.2 --file labs/01_prompt_engineering/lab2_cot_code_reviewer/exercise_starter.md
python3 sandbox/evaluate.py --lab 2.1 --file labs/02_critical_thinking/lab1_hallucination_audit/exercise_starter.md
python3 sandbox/evaluate.py --lab 2.2 --file labs/02_critical_thinking/lab2_fallacy_buster/exercise_starter.md
python3 sandbox/evaluate.py --lab 3.1 --file labs/03_cursor_orientation/lab1_inline_engineering/exercise_starter.md
python3 sandbox/evaluate.py --lab 3.2 --file labs/03_cursor_orientation/lab2_context_and_chat_qa/exercise_starter.md
python3 sandbox/evaluate.py --lab 3.3 --file labs/03_cursor_orientation/lab3_multi_file_composer/exercise_starter.md
python3 sandbox/evaluate.py --lab 3.4 --file labs/03_cursor_orientation/lab4_adversarial_diff_review_project/exercise_starter.md
```

### 3. Cursor Sandbox Project (`taskpulse_engine`)
Open `sandbox/taskpulse_engine/` directly in Cursor:
```bash
cd sandbox/taskpulse_engine
npm install
npm test
```
