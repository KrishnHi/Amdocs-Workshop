# Trainee Worksheet — Practical 3.1: Inline AI Engineering

**Trainee Name**: __Krishna Hitnalikar
**Date**: ___31/08/2026 
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

2. Describe the exact shaping actions you performed (example: "Accepted word-by-word via Cmd+Right three times; then deleted suggested import line"):
Keyboard actions / navigation used:
Edits made while shaping:

3. Paste your final accepted TypeScript implementation exactly as it exists after acceptance:
// Final accepted implementation (paste full function)

4. Acceptance checklist (tick and explain if any failed)
 No new imports were added (e.g., lodash/moment)
 Function preserves original signature and types
 Strict null/undefined checks were added
 Date parsing/ISO handling is robust
If any item is unchecked, explain why and how you mitigated it:

5. Unit-test suggestions (paste one or two assertions you ran or would run):
// Example assertions
// assert filterTasksByPriorityAndDate([], 'high', '2026-01-01') returns []
// assert tasks on exact sinceDate boundary are included/excluded per spec

## Exercise 2: Cmd/Ctrl+K Inline Prompt Formulation (applyRateLimiting)

File: src/api/middleware/rate-limiter.ts
Function: applyRateLimiting(req, res, next)

1. Paste the exact inline prompt you used with Cmd/Ctrl+K (be precise — instructors will inspect this):

Replace the highlighted placeholder with an in-memory sliding-window rate limiter middleware. Requirements: per-client (IP) limit 100 requests per 60 seconds; preserve signature (req, res, next); respond 429 using project error envelope { success: false, data: null, error: { code: 'RATE_LIMIT_EXCEEDED', message: 'Rate limit exceeded' } }; use logger.warn (no console.log); implement pruning to avoid unbounded Map growth (remove IP entries when empty or older than 5 minutes). Keep code synchronous and dependency-free. Include brief inline comments explaining pruning logic.

2. Paste the raw inline diff the editor produced (the full diff or the changed code block):

// Paste raw diff here (or the full changed function)

3. Diff Review Checklist — mark each and explain rejections

 Preserved function signature (req: Request, res: Response, next: NextFunction)
 Uses sliding-window algorithm (timestamp array or buckets)
 Returns HTTP 429 with project envelope
 Uses logger.warn, no console.log
 Has pruning/cleanup to prevent unbounded Map growth

For any checklist item that failed, paste the rejected lines and a short reason:

[Rejected lines and reason]

4. Final accepted implementation (paste the function you accepted):

// Final accepted middleware implementation

5. Unit tests you ran / would run (examples):

// simulate 101 requests from same IP -> last returns 429
// simulate many distinct IPs -> after retention period Map size reduces

## Exercise 3: Diff Review Audit & Rejection Analysis (sanitizeUserEmail)

File: src/utils/crypto.ts
Function: sanitizeUserEmail(rawEmail)

1. When invoking inline edit, did the editor attempt to rewrite unrelated helper methods?
[ ] YES / [ ] NO
If YES — list the lines it changed and why you rejected them:
Text :
[Explain rejected surrounding changes]

2. Paste the final accepted sanitizeUserEmail implementation:
TypeScript : 
// Final accepted sanitizeUserEmail implementation

3. Provide 5 edge-case assertions you used to verify the sanitizer:
JavaScript
// Examples:
// validate trimming and lowercasing domain part
// validate plus-address normalization or preservation policy
// invalid formats return null/error

## Diff Rejection Template (copy/paste when rejecting)
Whenever you reject a line from the editor-generated diff, record it with this template:

File:
Line(s):
Rejected text:
Reason for rejection (choose one): [adds dependency] [removes telemetry] [introduces console.log] [unbounded memory] [breaks type contract] [other — explain]
Action taken (fix, rewrite, delete, request new suggestion):

Example:

File: src/api/middleware/rate-limiter.ts
Line(s): +14..+22
Rejected text: console.log('hit', ip)
Reason: introduces console.log (should use logger.warn)
Action: Rewrote to logger.warn(...)

## Submission Checklist (what to include in your final exercise submission)

 Exercise 1: ghost-text raw suggestion + shaping log + final function + at least 1 unit test
 Exercise 2: exact inline prompt used + raw diff + diff rejection log (if any) + final function + tests
 Exercise 3: diff audit log + final sanitizer + tests
 Short reflection (3–5 sentences) describing one hallucination or unsafe pattern the editor suggested and how you prevented it.

## Hints, Best Practices & Quick Patterns

Inspect top-of-file diffs first for any new imports before accepting body changes.
Prefer per-request pruning: when you access an IP’s timestamp array, prune expired timestamps; if array empty, delete the Map entry.
For rate limiter retention tuning: prune entries older than (window + retention), e.g., window 60s + retention 5min.
For email sanitization: prefer pragmatic regex (not full RFC) and document edge cases you intentionally do not cover.
Use the editor’s diff inspector (Cmd+Shift+Y or equivalent) to view the whole-file patch before accepting.
