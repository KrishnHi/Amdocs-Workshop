# Trainee Worksheet — Practical 3.4: Adversarial Diff Review & Capstone Project

**Trainee Name**: ___________________________  
**Date**: ___________________________  
**Workspace**: `sandbox/taskpulse_engine/`

---

## Exercise 1: Capstone Feature Prompt Formulation

Record the prompt you provided to Cursor Agent (`Cmd/Ctrl+I`) for the Batch Export & Signature feature:

```text
[PASTE YOUR CAPSTONE MASTER PROMPT HERE]
```

---

## Exercise 2: The 4 Planted Vulnerabilities Audit Matrix

Examine the raw diff proposed by Cursor. For each category, record whether the defect appeared and your exact remediation:

| Trap | Vulnerability Category | Detected? (YES/NO) | Offending Code Snippet from Raw AI Diff | Corrected Code Snippet |
| :--- | :--- | :--- | :--- | :--- |
| **Trap A** | Insecure PRNG / Token Generation | `[ ] YES  [ ] NO` | `Math.random().toString(...)` | `crypto.randomBytes(32).toString('hex')` |
| **Trap B** | Timing Attack via Plain Equality (`===`) | `[ ] YES  [ ] NO` | `providedToken === expectedToken` | `crypto.timingSafeEqual(...)` |
| **Trap C** | Unbounded Memory Buffer / Missing Chunking | `[ ] YES  [ ] NO` | `const all = db.all(); return all;` | `// Batch chunking with cursor/pagination` |
| **Trap D** | Silent Exception Swallowing in Catch Block | `[ ] YES  [ ] NO` | `catch(e) { /* empty */ }` | `logger.error(...) + throw error` |

---

## Exercise 3: Verified Pull Request Diff

Paste your final audited, security-hardened Git diff for `src/api/routes/export.ts` and `src/utils/crypto.ts`:

```diff
[PASTE YOUR FINAL AUDITED DIFF HERE]
```

---

## Exercise 4: Capstone Execution & Test Verification

Execute in terminal:
```bash
npm run test:security
```

Paste your passing test output:
```text
[PASTE TERMINAL SECURITY TEST OUTPUT HERE]
```
