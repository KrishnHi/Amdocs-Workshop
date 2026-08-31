# Automated Evaluation Harness & Interactive Testbench

This directory provides automated evaluation harnesses, static analyzers, an interactive testbench, and a realistic TypeScript sandbox for assessing trainee performance across all 8 AI Engineering practicals.

---

## Operational Modes

---

### Mode 1: Interactive Web Testbench (Recommended for Instructor-Led Sessions)

Initialize a local HTTP service:
```bash
python3 -m http.server 3000 --directory sandbox/web
```
Navigate to `http://localhost:3000` in your web browser.

**Features:**
- **Lab 1.1 Triage Engine**: Real-time prompt evaluation with live JSON schema validation, injection simulation, and SLA classification metrics.
- **Lab 1.2 CoT Code Reviewer**: In-browser Python assertion testing and 5-stage markdown structural verification.
- **Lab 2.1 Hallucination Audit**: Claim categorization challenge with empirical ground-truth feedback and official AWS documentation references.
- **Lab 2.2 Fallacy Assessment**: Logical fallacy identification interface and unstated assumption analyzer.
- **Lab 3.1 Inline AI Engineering**: Interactive Ghost Text shaping and `Cmd/Ctrl+K` in-place refactoring tester with memory leak & error envelope checks.
- **Lab 3.2 Context & Rule Engine**: Scoped `@` prompt analyzer and `.cursor/rules/*.mdc` YAML frontmatter validator.
- **Lab 3.3 Multi-File Composer**: Multi-file execution tree visualizer, agent step analyzer, and diff inspector.
- **Lab 3.4 Adversarial Red-Team Diff Audit**: Interactive 4-trap scanner (Insecure PRNG, Timing Attacks, OOM Buffers, Silent Catch) and automated security assertion runner.
- **Reference Solution Loader**: Pre-loaded model solutions for all 8 practicals.

---

### Mode 2: Automated CLI Evaluation Harness

Run automated static analysis and validation directly against trainee markdown worksheets:

```bash
# Verify All 8 Instructor Reference Solutions:
python3 sandbox/evaluate.py --all-solutions

# Evaluate Individual Module 1 Practicals:
python3 sandbox/evaluate.py --lab 1.1 --file labs/01_prompt_engineering/lab1_structured_triage/exercise_starter.md
python3 sandbox/evaluate.py --lab 1.2 --file labs/01_prompt_engineering/lab2_cot_code_reviewer/exercise_starter.md

# Evaluate Individual Module 2 Practicals:
python3 sandbox/evaluate.py --lab 2.1 --file labs/02_critical_thinking/lab1_hallucination_audit/exercise_starter.md
python3 sandbox/evaluate.py --lab 2.2 --file labs/02_critical_thinking/lab2_fallacy_buster/exercise_starter.md

# Evaluate Individual Module 3 Practicals:
python3 sandbox/evaluate.py --lab 3.1 --file labs/03_cursor_orientation/lab1_inline_engineering/exercise_starter.md
python3 sandbox/evaluate.py --lab 3.2 --file labs/03_cursor_orientation/lab2_context_and_chat_qa/exercise_starter.md
python3 sandbox/evaluate.py --lab 3.3 --file labs/03_cursor_orientation/lab3_multi_file_composer/exercise_starter.md
python3 sandbox/evaluate.py --lab 3.4 --file labs/03_cursor_orientation/lab4_adversarial_diff_review_project/exercise_starter.md
```

---

### Mode 3: Local TypeScript Codebase Sandbox (`taskpulse_engine`)

A runnable TypeScript/Express repository configured with `.cursor/rules/`, structured logging, and unit test suites:

```bash
cd sandbox/taskpulse_engine
npm install
npm test
npm run test:security
```
