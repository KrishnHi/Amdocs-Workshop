# Trainee Worksheet — Practical 3.1: Inline AI Engineering

**Trainee Name**: ___________________________  
**Date**: ___________________________  
**Workspace**: `sandbox/taskpulse_engine/`

---

## Instructions (updated)
Perform the three inline-editing exercises using your editor’s Cursor/inline-AI features. For every generated suggestion you accept, record: (A) the raw ghost-text or inline suggestion, (B) the exact keyboard actions or inline prompt you used, (C) the final accepted code, and (D) any diff lines you rejected with a short reason. Be strict: reject any suggestion that adds third-party dependencies, removes telemetry/type assertions, or introduces unbounded memory structures.

---

## Exercise 1: Ghost Text Tab Shaping Log (filterTasksByPriorityAndDate)

File: `src/core/services/task.service.ts`  
Function: `filterTasksByPriorityAndDate(tasks, priority, sinceDate)`

1. Paste the initial raw ghost-text suggestion you saw when you pressed `Tab` (single accept) here:
```typescript
// Raw ghost-text suggestion (paste verbatim)
