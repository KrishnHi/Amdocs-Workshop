# Trainee Worksheet — Practical 3.1: Inline AI Engineering

**Trainee Name**: ___________________________  
**Date**: ___________________________  
**Workspace**: `sandbox/taskpulse_engine/`

---

## Exercise 1: Ghost Text Tab Shaping Log

Navigate to `src/core/services/task.service.ts` -> `filterTasksByPriorityAndDate`.

1. **Initial Unfiltered Suggestion**: What did Cursor suggest when pressing `Tab` once without constraints? (Did it try to import `lodash` or omit null checks?)
```typescript
// Paste initial raw suggestion here:

```

2. **Accepted Refactored Implementation** (Shaped word-by-word via `Cmd+Right` / `Ctrl+Right`):
```typescript
// Paste your final accepted TypeScript code here:

```

---

## Exercise 2: `Cmd/Ctrl+K` Inline Prompt Formulation

Navigate to `src/api/middleware/rate-limiter.ts` -> `applyRateLimiting`.

1. **Your Exact `Cmd/Ctrl+K` Prompt**:
```text
[PASTE YOUR INLINE PROMPT HERE]
```

2. **Inline Diff Checklist**:
- [ ] Preserved function signature `(req: Request, res: Response, next: NextFunction)`
- [ ] Used in-memory sliding window algorithm (timestamp array or bucket)
- [ ] Returned HTTP 429 using project standard envelope `{ success: false, data: null, error: { code: "RATE_LIMIT_EXCEEDED", message: "..." } }`
- [ ] Used `logger.warn` instead of `console.log`
- [ ] Cleaned up stale entries to prevent memory leak

---

## Exercise 3: Diff Review Audit & Rejection Analysis

During the inline edit of `src/utils/crypto.ts` (`sanitizeUserEmail`):

1. **Did Cursor attempt to rewrite surrounding unchanged helper methods?**: [ ] YES / [ ] NO
2. **What line(s) in the generated diff did you manually reject or adjust?**:
```text
[EXPLAIN ANY REJECTED DIFF LINES HERE]
```
