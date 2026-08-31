# Practical 3.4: The "Critical Eye" — Adversarial Diff Auditing & Capstone Project

**Module**: Module 3 - Cursor Orientation  
**Level**: Associate / Graduate Trainee  
**Duration**: 50 Minutes  
**Core Technical Competencies**: Adversarial Code Review, AI Hallucination Interception, Cryptographic & Security Diff Auditing, Resource Leak Detection, End-to-End Feature Verification.

---

## 1. Engineering Context & Problem Specification

AI code assistants excel at generating syntactically convincing, fluent code. However, unreviewed AI output in production frequently introduces:
1. **Cryptographic Weaknesses**: Replacing secure primitives with pseudo-random numbers (`Math.random()`).
2. **Resource Exhaustion**: Leaving database connections or file streams unclosed in error paths.
3. **Silent Exception Swallowing**: Catching errors with empty catch blocks, blinding monitoring systems.
4. **Timing Vulnerabilities**: String comparison operators (`===`) on security tokens instead of constant-time comparisons (`crypto.timingSafeEqual`).

In this Capstone practical, trainees will build the **Batch Task Export & Signer** subsystem. They must direct Cursor to generate the feature, and then subject Cursor's proposed diffs to rigorous red-team scrutiny to detect and neutralize **4 Planted Vulnerability Traps**.

---

## 2. The 4 Planted AI Output Traps

When asking Cursor to implement the batch exporter, inspect the generated diffs for these common AI failure modes:

| Trap Identifier | Category | Defect Description | Production Consequence |
| :--- | :--- | :--- | :--- |
| **Trap A** | **Security** | Insecure Token Generation using `Math.random().toString(36)` | Predictable auth/export session tokens vulnerable to brute-force session hijacking. |
| **Trap B** | **Security** | Insecure Secret Comparison using `===` in auth check | Timing side-channel attack allows token reconstruction through response latency analysis. |
| **Trap C** | **Reliability** | Unbounded Memory Buffer / Missing Stream Release | Batch queries load all records into memory at once without chunking, triggering OOM crashes. |
| **Trap D** | **Observability**| Silent Error Swallowing (`catch (e) {}` with no logger) | Background export failures occur without SRE alerting or trace capture. |

---

## 3. Trainee Capstone Project Steps

1. **Step 1: Capstone Feature Request**:
   Prompt Cursor Agent to create:
   - `src/api/routes/export.ts` with endpoint `POST /api/v1/export/tasks`
   - Signed download tokens with HMAC SHA-256 signatures
   - Streaming or chunked batch processing
2. **Step 2: Adversarial Diff Inspection**:
   - Review each generated file line-by-line.
   - Do NOT accept the diff until all 4 traps are detected and corrected.
3. **Step 3: Test-Suite Validation**:
   - Run the integration test suite:
     ```bash
     npm run test:security
     ```
   - Ensure all cryptographic, security, and edge-case assertions pass.

---

## 4. Evaluation Rubric

| Assessment Dimension | Weight | Target Standard |
| :--- | :---: | :--- |
| **Adversarial Trap Detection** | 40% | Identification of all 4 traps (Insecure PRNG, Timing leak, OOM buffer, Silent catch). |
| **Remediation Quality** | 30% | Correct use of `crypto.randomBytes`, `crypto.timingSafeEqual`, batch chunking, and `logger.error`. |
| **Diff Review Precision** | 20% | Zero unintended regressions in surrounding codebase files. |
| **End-to-End Test Passing** | 10% | Clean execution of `npm test` and `npm run test:security`. |
