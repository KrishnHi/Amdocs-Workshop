# Trainee Worksheet — Practical 3.3: Multi-File Orchestration with Composer

**Trainee Name**: ___________________________  
**Date**: ___________________________  
**Workspace**: `sandbox/taskpulse_engine/`

---

## Exercise 1: Master Composer / Agent Prompt Formulation

Open Composer (`Cmd/Ctrl+I`) in Agent mode.

```text
[PASTE YOUR MULTI-FILE COMPOSER MASTER PROMPT HERE]
```

### Prompt Checklist:
- [ ] Included `@` references to `@src/core/`, `@src/api/`, and `@docs/architecture.md`
- [ ] Listed numbered execution steps per file
- [ ] Explicitly specified negative constraints (e.g., *"Do not modify database/client.ts"*)
- [ ] Specified error-handling envelope and TypeScript strict typing constraints

---

## Exercise 2: Multi-File Diff Audit & Review Log

Record what files Composer proposed to edit, and what you did during review:

| File Target | Action Taken (Accepted / Rejected / Manually Edited) | Review Notes & Detected Anomalies |
| :--- | :--- | :--- |
| `src/core/models/audit.model.ts` | `[ ] Accepted [ ] Rejected [ ] Edited` | |
| `src/core/services/task.service.ts` | `[ ] Accepted [ ] Rejected [ ] Edited` | |
| `src/core/services/notification.ts` | `[ ] Accepted [ ] Rejected [ ] Edited` | |
| `src/api/routes/webhooks.ts` | `[ ] Accepted [ ] Rejected [ ] Edited` | |
| `src/api/server.ts` | `[ ] Accepted [ ] Rejected [ ] Edited` | |
| `tests/unit/webhook.spec.ts` | `[ ] Accepted [ ] Rejected [ ] Edited` | |

---

## Exercise 3: Test Verification Output

Execute in terminal:
```bash
npm test
```

Paste the terminal test execution summary:
```text
[PASTE TEST SUITE OUTPUT HERE]
```
