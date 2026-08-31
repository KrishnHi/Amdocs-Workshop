# Practical 3.1: Inline AI Engineering — Autocomplete & In-Place Refactoring

**Module**: Module 3 - Cursor Orientation  
**Level**: Associate / Graduate Trainee  
**Duration**: 35 Minutes  
**Core Technical Competencies**: Cursor Interface Ergonomics, Predictive Tab Completions (Ghost Text), In-Place Code Transformations (`Cmd/Ctrl+K`), Diff Scrubbing & Selective Acceptance, Local Scope Preservation.

---

## 1. Engineering Context & Problem Specification

Modern AI code editors provide continuous predictive assistance directly within the editor buffer. However, uncritical usage leads to:
1. **Scope Bloat**: Blindly pressing `Tab` introduces unnecessary third-party libraries (e.g., pulling in entire `lodash` or `moment.js` packages when vanilla ES6+ suffices).
2. **Context Annihilation**: Poorly framed `Cmd/Ctrl+K` inline prompts rewrite intact surrounding code, deleting existing comments, TypeScript type assertions, or telemetry calls.
3. **Ghost Text Drift**: Accepting autocomplete multi-line suggestions that invent non-existent object methods or invalid enum values.

Trainees will work inside the [`taskpulse-engine`](file:///Users/aaryankumar/Documents/promptengg/sandbox/taskpulse_engine) sandbox to practice high-precision inline editing, line-by-line autocomplete shaping, and strict inline diff auditing.

---

## 2. Technical Lab Tasks

### Task 1: Tab Autocomplete Shaping (Ghost Text Control)
- **Target File**: [`src/core/services/task.service.ts`](file:///Users/aaryankumar/Documents/promptengg/sandbox/taskpulse_engine/src/core/services/task.service.ts)
- **Objective**: Implement `filterTasksByPriorityAndDate(tasks, priority, sinceDate)` using pure TypeScript.
- **Workflow**:
  1. Place the cursor inside the function body.
  2. Let Cursor generate ghost text suggestions.
  3. **Constraint**: Shape the completion word-by-word or line-by-line using `Cmd+Right` / `Ctrl+Right` (or word accept) to ensure zero external dependency imports and strict null-safety checks on `sinceDate`.

### Task 2: In-Place Algorithmic Generation via `Cmd/Ctrl+K`
- **Target File**: [`src/api/middleware/rate-limiter.ts`](file:///Users/aaryankumar/Documents/promptengg/sandbox/taskpulse_engine/src/api/middleware/rate-limiter.ts)
- **Objective**: Replace the placeholder `applyRateLimiting` middleware with an in-memory sliding-window rate limiter (100 requests per 60 seconds per client IP).
- **Workflow**:
  1. Highlight lines 15 to 30 in `src/api/middleware/rate-limiter.ts`.
  2. Invoke `Cmd/Ctrl+K`.
  3. Craft a single, deterministic inline prompt adhering to the project's error envelope standard.
  4. Inspect the generated inline diff (`Cmd+Shift+Y` or Diff Inspector).
  5. Accept the changes only if no memory leaks (unbounded Map keys) or unauthorized `console.log` calls are introduced.

### Task 3: Inline Regex & Data Sanitization
- **Target File**: [`src/utils/crypto.ts`](file:///Users/aaryankumar/Documents/promptengg/sandbox/taskpulse_engine/src/utils/crypto.ts)
- **Objective**: Refactor the naive email sanitization function `sanitizeUserEmail(rawEmail)` using inline `Cmd/Ctrl+K` to trim whitespace, lowercase domain portions, and validate against RFC 5322 compliance.

---

## 3. Trainee Deliverables

Open [`exercise_starter.md`](file:///Users/aaryankumar/Documents/promptengg/labs/03_cursor_orientation/lab1_inline_engineering/exercise_starter.md) and record:
1. **Section 1: Ghost Text Shaping Log**: The exact keyboard actions and diff comparisons.
2. **Section 2: Inline `Cmd/Ctrl+K` Prompt Formulation**: The exact prompt text used for the sliding-window rate limiter.
3. **Section 3: Diff Review Audit**: Identification of any hallucinated imports or formatting violations introduced during the inline edit.

---

## 4. Evaluation Rubric

| Assessment Dimension | Weight | Target Standard |
| :--- | :---: | :--- |
| **Inline Prompt Precision** | 30% | Concise instruction specifying algorithm (sliding window), thresholds (100 req/min), and response format. |
| **Diff Review Rigor** | 30% | Zero unintended modifications to surrounding method signatures or comments; rejection of unneeded imports. |
| **Code Standard Compliance** | 20% | Adherence to project error envelopes (`{ success, data, error }`) and structured logger usage. |
| **Memory & Resource Safety** | 20% | Proper cleanup mechanism (pruning expired timestamp arrays in Map) to prevent unbounded memory growth. |
