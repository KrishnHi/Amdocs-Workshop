# Practical 3.2: Context Engineering & Grounded Codebase Q&A

**Module**: Module 3 - Cursor Orientation  
**Level**: Associate / Graduate Trainee  
**Duration**: 40 Minutes  
**Core Technical Competencies**: Context Scope Control, `@` Mention Modifiers (`@Files`, `@Folders`, `@Codebase`, `@Docs`), Rule Engineering (`.cursor/rules/*.mdc`), Root Cause Diagnostic Tracing, Model Context Dilution Prevention.

---

## 1. Engineering Context & Problem Specification

Large Language Models inside AI editors do not know your entire architecture by default. They rely on:
1. **Vector Indexing**: Semantic retrieval over indexed files.
2. **Explicit Context Mentions**: Scoped `@` directives supplied by the developer.
3. **Project Rule Directives**: Persistent guidelines placed in `.cursor/rules/` (MDC format).

When developers ask broad, ungrounded questions (e.g., *"Why is my API returning 500?"*), the AI guesses, hallucinating libraries or irrelevant files. When given high-precision `@` references, the AI pinpoints distributed state bugs with zero hallucination.

In this lab, trainees will investigate a critical concurrent mutation bug in [`taskpulse-engine`](file:///Users/aaryankumar/Documents/promptengg/sandbox/taskpulse_engine) and construct strict project rules in `.cursor/rules/` to prevent future defects.

---

## 2. Technical Lab Tasks

### Task 1: Root-Cause Analysis via Scoped Chat (`Cmd/Ctrl+L`)
- **The Defect**: When a task's status is patched to `'COMPLETED'`, concurrent updates cause `completed_at` timestamps or metadata tags to be erased or overwritten.
- **Workflow**:
  1. Open Cursor Chat (`Cmd/Ctrl+L`).
  2. Perform an **Ungrounded Query**: Ask *"Why is my task timestamp resetting?"* Note the lack of specificity and hallucinated answers.
  3. Perform a **Scoped Grounded Query**:
     ```text
     @task.service.ts @tasks.ts @task.model.ts
     Analyze the concurrency model in updateTaskStatus.
     Trace how partial PATCH updates mutate the underlying in-memory record.
     Identify why `completed_at` and `tags` are dropped during concurrent status updates.
     ```
  4. Record the specific line numbers and the root cause identified.

### Task 2: Rule Engineering with `.cursor/rules/*.mdc`
- **Objective**: Create project-level rule files that automatically guide Cursor's code generation across all files.
- **Files to create/modify**:
  - [`.cursor/rules/01-error-handling.mdc`](file:///Users/aaryankumar/Documents/promptengg/sandbox/taskpulse_engine/.cursor/rules/01-error-handling.mdc):
    - Must enforce standard error envelope: `{ "success": boolean, "data": T | null, "error": { "code": string, "message": string } }`
    - Must forbid `console.log` and `console.error`; require `logger` from `@utils/logger`.
  - [`.cursor/rules/02-security-boundary.mdc`](file:///Users/aaryankumar/Documents/promptengg/sandbox/taskpulse_engine/.cursor/rules/02-security-boundary.mdc):
    - Must enforce cryptographic token generation via `crypto.randomBytes(32)` instead of `Math.random()`.
    - Must forbid raw string concatenation in SQL/storage queries.

### Task 3: Adversarial Rule Adherence Verification
- **Target**: Open `src/api/routes/tasks.ts`.
- **Action**: Prompt Cursor to generate a quick delete route: *"Write a route DELETE /tasks/:id that logs errors to console if not found."*
- **Check**: Verify whether Cursor intercepts the bad instruction and adheres to `01-error-handling.mdc` instead.

---

## 3. Trainee Deliverables

Open [`exercise_starter.md`](file:///Users/aaryankumar/Documents/promptengg/labs/03_cursor_orientation/lab2_context_and_chat_qa/exercise_starter.md) and record:
1. **Section 1: Comparative Q&A Diagnostic**: Ungrounded vs Scoped Chat output comparison.
2. **Section 2: Root-Cause Explanation**: Exact diagnosis of the shallow spread bug in `task.service.ts`.
3. **Section 3: `.cursor/rules` Artifacts**: Full YAML frontmatter and rule definitions.

---

## 4. Evaluation Rubric

| Assessment Dimension | Weight | Target Standard |
| :--- | :---: | :--- |
| **Context Scoping Precision** | 30% | Exact `@File` and `@Folder` references used instead of wasteful global repo queries. |
| **Root-Cause Accuracy** | 25% | Correct identification of the shallow copy / destructive spread operator in `updateTaskStatus`. |
| **Rule Frontmatter Schema** | 25% | Valid MDC format with `description`, `globs`, and `alwaysApply` frontmatter. |
| **Adversarial Constraint Enforcement**| 20% | Rules successfully block `console.log` and enforce `{ success, data, error }` schema. |
