# Trainee Practical Assessment: Practical 2.2

**Trainee Name**: ___Krishna Hitnaikar
**Employee ID**: _____215677
**Date**: ______31/08/2026

---

## Instructions
Carefully examine the architecture memo in `ai_proposal.md`. Complete the Fallacy Identification Matrix (Section 1), extract and analyze unstated operational assumptions (Section 2), and author a pragmatic 3‑phase engineering counter-proposal (Section 3). For each entry supply concise, evidence-based reasoning and at least one concrete remediation or verification action. Use facts, metrics, and measurable acceptance criteria where possible.

---

## Section 1: Fallacy Identification Matrix

| Target Excerpt | Formal Fallacy Name | Technical Breakdown & Reasoning Defect |
| :--- | :--- | :--- |
| **Excerpt A** — "Either we immediately decompose our entire monolith into a mesh of 35 decentralized microservices by the end of this quarter, or our technology platform will implode." | False Dilemma (Black-and-White) | Presents only two extreme options and excludes intermediate approaches (incremental extraction, modular monolith, strangler pattern). Technical consequence: forces unrealistic scheduling and resource allocation, increases coordination/rollback risk, and ignores prerequisite operational maturity (CI, observability). Remediation: propose incremental extraction with pilot services and gates (see Phase 1 acceptance criteria). |
| **Excerpt B** — "NetStream migrated to 500+ microservices and saw subscribers grow 350%; therefore we will increase subscribers by 300% if we do the same." | False Cause (Post Hoc) / Overgeneralization | Infers causation from a single historical correlation without controlling for confounders (market, product changes, investment). Technical consequence: drives strategy by vanity metrics, leading to scope inflation and misaligned investment. Remediation: require causality evidence (A/B analysis, baseline telemetry) and decouple engineering KPIs from speculative business outcomes. |
| **Excerpt C** — "Engineers who want to keep a modular monolith are arguing for 1990s spaghetti code and are therefore wrong." | Straw Man | Mischaracterizes a reasonable, modern alternative (modular monolith / modularization) as extreme and straw-manned. Technical consequence: discards lower-risk, high-value options (refactor-in-place, interface stabilization) and prematurely escalates scope. Remediation: evaluate modular monolith benefits and show objective metrics (deploy frequency, test coverage) before dismissing. |
| **Excerpt D** — "A viral LinkedIn post by a Cloud Visionary settled the debate and validates immediate migration." | Appeal to Authority (Social Proof) | Uses popularity/authority rather than technical evidence. Technical consequence: encourages bandwagon decisions that may not fit organizational context. Remediation: require primary-source evidence, case-study context, and internal readiness checks before adopting influencer-driven guidance. |

---

## Section 2: Unmasking Unstated Operational Assumptions

For each assumption, provide (a) the assumption text, (b) technical risk if false, and (c) mitigation / verification action.

1. Assumption: Mature CI/CD pipelines, automated test suites, and reliable deployment rollback exist.
   - Technical Risk: Without CI/CD and automated tests, splitting services increases regression risk, slows delivery, and makes version coordination brittle. Incidents and rollbacks will rise.
   - Mitigation / Verification: Inventory current pipelines (Jenkins/GitHub Actions/GitLab) and test coverage % by service. Acceptance: minimum 70% unit test coverage and green pipeline with automated canary rollouts for pilot service.

2. Assumption: Observability (metrics, distributed tracing, logs, alerting) is present and comprehensive.
   - Technical Risk: Lack of tracing/metrics prevents root-cause analysis in distributed systems and increases MTTR dramatically.
   - Mitigation / Verification: Deploy OpenTelemetry or equivalent across monolith endpoints; require successful end-to-end trace for a sample user flow. Acceptance: ability to trace request across components with <1s diagnostic time for pilot issues.

3. Assumption: Team structure and SRE/ops capacity can support 35 independent services (ownership, runbooks, on-call).
   - Technical Risk: Service sprawl without ownership causes operational debt, alert fatigue, and inconsistent SLAs.
   - Mitigation / Verification: Map team boundaries to proposed services; require a service ownership charter and runbook before extraction. Acceptance: each pilot service has an owner, a runbook, and a 1-week on-call rotation plan.

4. Assumption: Data consistency and transactional integrity can be handled without wholesale re-architecture.
   - Technical Risk: Extracting services that share transactional boundaries can lead to data anomalies, complex sagas, and customer-facing failures.
   - Mitigation / Verification: Identify bounded contexts and data ownership; create a data migration/consistency plan and simulation of eventual-consistency scenarios. Acceptance: no critical end-to-end transaction loses ACID guarantees without an approved saga pattern and compensating actions.

5. Assumption: Networking, security, and infra (service mesh, API gateway) can be provisioned and scaled safely.
   - Technical Risk: Unprepared infra leads to misconfigurations, security holes, and latency regressions.
   - Mitigation / Verification: Pilot ingress patterns with rate limiting and canary traffic. Acceptance: successful canary with no >1% error rate increase and latency regression within agreed SLO.

---

## Section 3: Phased Engineering Counter-Proposal

Goal: reduce risk, validate value, and incrementally realize benefits of service-oriented architecture.

Phase 0 — Prepare & Harden (2–6 weeks)
- Objectives:
  - Establish baselines: current deploy frequency, lead time, MTTR, test coverage per module.
  - Improve CI/CD, add automated integration tests, and add or extend telemetry (metrics + traces).
  - Define governance: service definition template, SLA contract template, rollback playbook.
- Deliverables:
  - CI/CD checklist passed for candidate modules.
  - Observability baseline dashboards and runbook templates.
  - Service ownership charters for pilot teams.
- Success Criteria:
  - Green pipelines for targeted modules; ability to run full regression suite in <30 minutes.
  - End-to-end traceability for critical user journey.

Phase 1 — Modular Monolith + Pilot Extraction (8–12 weeks)
- Objectives:
  - Refactor codebase to a modular monolith (clear module boundaries, internal API/interface contracts).
  - Select 1–2 low-risk, high-value services to extract (criteria: low coupling, high transaction isolation, measurable business value).
  - Implement extraction using strangler pattern and consumer-driven contracts.
- Deliverables:
  - Extracted pilot services (e.g., auth, billing) with API contracts and automated contract tests.
  - Traffic routing plan (feature flags, API gateway routes), canary deployment strategy, rollback steps.
- Success Criteria:
  - Pilot extraction deploys independently with no >1% production error increase.
  - Automated contract tests run in CI and block incompatible changes.
  - Measured deployment frequency improvement or latency/resource improvement vs baseline.

Phase 2 — Iterative Serviceization & Platform Maturity (quarterly roadmap)
- Objectives:
  - Expand extraction based on telemetry and business priority.
  - Harden platform (service mesh optional, centralized observability, operational playbooks).
  - Introduce rate-limiting, backpressure, and circuit breaker patterns for downstream protection.
- Deliverables:
  - Migration playbook per service family, cost & capacity plan, SLO/SLA definitions.
  - Operational metrics dashboard showing velocity vs reliability (deployments per week, MTTR, error budget consumption).
- Success Criteria:
  - Each extracted service meets SLA and ownership requirements.
  - No systemic increase in MTTR; engineering velocity measured by deploy frequency improves or is maintained.

Implementation notes & constraints
- Do not start broad extraction before Phase 0 completion.
- Prioritize high-value, low-coupling services for Phase 1 to reduce blast radius.
- Use feature toggles and consumer-driven contracts to prevent breaking changes.
- Evaluate need for service mesh only after several services require advanced traffic management.

---

## Section 4: Submission Checklist (what to include)

- [ ] Completed Fallacy Identification Matrix (Section 1) with concise technical consequences and one remediation per excerpt.
- [ ] Unstated Assumptions list (Section 2) with risk and verification action for each.
- [ ] Phased Counter-Proposal (Section 3) with deliverables and measurable success criteria.
- [ ] Evidence appendix: at least two internal metrics/figures (e.g., current deploy frequency, test coverage) or references to authoritative docs for proposed patterns (e.g., strangler fig pattern, contract testing).
- [ ] Short risk log: top 3 risks and a proposed mitigation for each.

---

## Appendix: Quick evidence & references (suggested links to cite)

- Strangler Fig pattern: https://martinfowler.com/bliki/StranglerApplication.html  
- Consumer-driven contract testing (Pact, contract test concepts): https://docs.pact.io/  
- Service ownership and SRE principles: https://landing.google.com/sre/sre-book/  
- Observability (OpenTelemetry): https://opentelemetry.io/  
- Canary deployment patterns: https://martinfowler.com/articles/canary-release.html

---

If you want, I will now:
- (A) Paste this completed exercise_starter.md into the repository (create a commit/PR), or
- (B) Produce a sample filled submission based on the instructor reference (solution_reference.md) that you can use as a model answer, or
- (C) Generate a small "fallacy-linter" script that scans ai_proposal.md for absolute-language patterns and extracts candidate fallacy lines.

Which one should I do next?
