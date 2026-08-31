```markdown name=labs/03_cursor_orientation/lab2_context_and_chat_qa/exercise_starter.md
# Trainee Worksheet — Practical 3.2: Context Engineering & Grounded Chat Q&A

**Trainee Name**: ___Krishna Hitnalikar______  
**Date**: ______31/08/2026
**Workspace**: `sandbox/taskpulse_engine/`

---

## Exercise 1: Ungrounded vs Grounded Chat Diagnostic

### 1.1 Ungrounded Query Test
- **Prompt Sent**: `Why is completed_at timestamp resetting in tasks?`
- **Result Summary**: (Did it make generic guesses or refer to external frameworks like Prisma/Postgres that aren't in this project?)
```text
[RECORD OBSERVATION HERE]
```

Notes / guidance:
- Copy the raw ungrounded reply here verbatim. Highlight any invented filenames, external services, or general claims the model made without evidence.
- Expected behavior: generic answers or hallucinated external dependencies; low confidence and no line-number pointers.

### 1.2 Scoped Grounded Query Test
- **Prompt Sent** (example; replace with your exact @ references and spacing):
```text
@src/core/services/task.service.ts @src/core/models/task.model.ts @src/api/routes/tasks.ts
Analyze updateTaskStatus. Trace how partial PATCH updates mutate the in-memory record. Identify why completed_at or tags are dropped during concurrent PATCHes. Provide exact line numbers and a minimal reproduction sequence.
```
- **Identified Root Cause in `src/core/services/task.service.ts`**:
```text
[EXPLAIN THE SHALLOW OVERWRITE BUG HERE]
```

Guidance for answering 1.2:
- Paste the model’s exact reply after issuing the scoped prompt.
- Validate every file:line the model cites. If a line number is wrong, note the correct one.
- A strong diagnosis will identify patterns like: shallow spread/clobbering ({ ...existing, ...patch }), shared references to nested objects/arrays, missing deep-clone or selective merge, or improper optimistic concurrency handling.

---

## Exercise 2: Project Rules Definition (`.cursor/rules/`)

Create the `.cursor/rules/*.mdc` artifacts below. Paste the full contents of each created file in your submission.

### 2.1 File: `.cursor/rules/01-error-handling.mdc`
```mdc
---
description: Enforce the project error-response envelope and forbid direct console logging.
globs:
  - "src/**/*.ts"
alwaysApply: true
---

# Rules:
1. id: enforce-error-envelope
   description: "Responses must use the structured envelope { success, data, error } for API handlers."
   pattern: "return\\s+\\{\\s*success\\s*:"
   enforcement: "warn"

2. id: block-console
   description: "Block console.log / console.error usage; require logger import from @utils/logger."
   pattern: "console\\.(log|error|warn)\\("
   enforcement: "block"
```

Notes:
- `pattern` values are simple regex-like strings the rule engine uses to detect violations; adapt to the project's rule engine syntax if needed.
- `enforcement: block` should cause Cursor to refuse or auto-correct code that violates the rule.

### 2.2 File: `.cursor/rules/02-security-boundary.mdc`
```mdc
---
description: Enforce secure randomness and discourage raw SQL concatenation.
globs:
  - "src/**/*.ts"
alwaysApply: true
---

# Rules:
1. id: require-crypto-random
   description: "Prevent use of Math.random for token generation; require crypto.randomBytes(32)."
   pattern: "Math\\.random\\("
   enforcement: "block"

2. id: warn-sql-concat
   description: "Warn on simple string concatenation in DB queries; recommend parameterized queries."
   pattern: "(\\+\\s*['\"`])|(['\"`]\\s*\\+)"
   enforcement: "warn"
```

Guidance:
- Ensure these files are placed under `.cursor/rules/` in your workspace. The `globs` scope limits the rule application.

---

## Exercise 3: Adversarial Rule Enforcement Check

1. **Test Prompt Used in `src/api/routes/tasks.ts`**:
```text
Write a route DELETE /tasks/:id that logs errors to console if missing.
```

2. **Did Cursor follow your `.cursor/rules` instead of the user prompt's request to log to console?** (tick all that apply)
- [ ] Yes — it imported and used `logger.error` (preferred)
- [ ] Yes — it returned `{ success: false, data: null, error: { ... } }` envelope
- [ ] No — it used `console.log` / `console.error` or returned raw error responses

Record evidence:
- Paste Cursor's raw reply (verbatim):
```text
[PASTE CURSOR'S RAW REPLY HERE]
```
- Paste the raw file diff / generated code the editor proposed (or the produced route file):
```diff
[PASTE GENERATED DIFF OR FILE HERE]
```
- Outcome: Did the rule block/alter the unsafe generation? YES / NO. If NO, explain what happened and how to strengthen the rule (e.g., change enforcement from warn -> block, expand globs).

---

## Submission checklist — what to include in this file

- [ ] Exact ungrounded prompt and raw ungrounded model reply (Section 1.1).
- [ ] Exact scoped prompt and raw scoped model reply (Section 1.2).
- [ ] Line numbers and files the model referenced (confirm or correct them).
- [ ] Minimal reproduction commands/scripts and observed logs demonstrating the bug.
- [ ] Full contents of `.cursor/rules/01-error-handling.mdc` and `.cursor/rules/02-security-boundary.mdc` as created on disk.
- [ ] Adversarial prompt, model reply, and generated file diff showing whether rules enforced or failed.
- [ ] Short reflection (3–5 sentences) on the difference between ungrounded and scoped responses, and one example hallucination the scoping prevented.

---

## Hints & quick commands

- Scoped chat pattern example:
```text
@src/core/services/task.service.ts @src/core/models/task.model.ts Trace updateTaskStatus and show exact lines that modify completed_at or tags.
```

- Quick grep to find shallow spreads in services:
```bash
rg "\{\s*\.\.\.\w+,\s*\.\.\.\w+\s*\}" src || true
```

- Run dev server / reproduce concurrency (example; adapt to your project):
```bash
npm run dev
# then run a script that launches overlapping PATCH requests to the same task id
node scripts/concurrent_patch_simulator.js --taskId t1 --concurrency 5 --patch '{"status":"COMPLETED","completed_at":"2026-08-31T12:00:00Z"}'
```

---
