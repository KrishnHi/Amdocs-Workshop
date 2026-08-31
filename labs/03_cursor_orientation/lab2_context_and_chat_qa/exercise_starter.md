# Trainee Worksheet — Practical 3.2: Context Engineering & Grounded Chat Q&A

**Trainee Name**: ___________________________  
**Date**: ___________________________  
**Workspace**: `sandbox/taskpulse_engine/`

---

## Exercise 1: Ungrounded vs Grounded Chat Diagnostic

### 1.1 Ungrounded Query Test
- **Prompt Sent**: `Why is completed_at timestamp resetting in tasks?`
- **Result Summary**: (Did it make generic guesses or refer to external frameworks like Prisma/Postgres that aren't in this project?)
```text
[RECORD OBSERVATION HERE]
```

### 1.2 Scoped Grounded Query Test
- **Prompt Sent**:
```text
[PASTE YOUR SCOPED @ PROMPT HERE]
```
- **Identified Root Cause in `src/core/services/task.service.ts`**:
```text
[EXPLAIN THE SHALLOW OVERWRITE BUG HERE]
```

---

## Exercise 2: Project Rules Definition (`.cursor/rules/`)

### 2.1 File: `.cursor/rules/01-error-handling.mdc`
```markdown
---
description: [ENTER DESCRIPTION HERE]
globs: [ENTER GLOBS HERE]
alwaysApply: true
---

# Rules:
1. 
2. 
3. 
```

### 2.2 File: `.cursor/rules/02-security-boundary.mdc`
```markdown
---
description: [ENTER DESCRIPTION HERE]
globs: [ENTER GLOBS HERE]
alwaysApply: true
---

# Rules:
1. 
2. 
```

---

## Exercise 3: Adversarial Rule Enforcement Check

1. **Test Prompt Used in `src/api/routes/tasks.ts`**:
```text
Write a route DELETE /tasks/:id that logs errors to console if missing.
```

2. **Did Cursor follow your `.cursorrules` instead of the user prompt's request to log to console?**:
- [ ] Yes, it imported and used `logger.error`
- [ ] Yes, it returned `{ success: false, data: null, error: { ... } }`
- [ ] No, it used `console.log` / `console.error`
