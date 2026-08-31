# Practical 1.1: Incident Triage & Structured Data Extraction Engine

**Module**: Module 1 - Prompt Engineering  
**Level**: Associate / Graduate Trainee  
**Duration**: 45 Minutes  
**Core Technical Competencies**: Prompt Anatomy (Role, Task, Context, Constraints), Delimiter Isolation (`<ticket>...</ticket>`), Deterministic JSON Schema Enforcement, Adversarial Injection Defense.

---

## 1. Business Context & Problem Specification

In an enterprise IT Service Management (ITSM) and Site Reliability Engineering (SRE) environment, incoming incident tickets from monitoring alerts, customer emails, and internal communication channels are unstructured, variable in quality, and occasionally adversarial.

Trainees must develop an automated LLM extraction prompt that ingests raw incident records and outputs structured metadata for downstream automated queuing systems:
1. **Service Classification** (`auth`, `billing`, `database`, `frontend`, `other`)
2. **Urgency Classification** (`P1-Critical`, `P2-High`, `P3-Medium`, `P4-Low`) based on strict Service Level Agreement (SLA) criteria
3. **Executive Summary** (strictly 15 words or fewer)
4. **Technical Indicators** (error codes, affected infrastructure entities)
5. **Immediate SRE Action Item**
6. **Security Flag** (boolean indicating presence of adversarial prompt injection)

### Baseline (Defective) Prompt:
```text
Read this ticket and tell me what the problem is and how urgent it is and format as json:
[TICKET TEXT HERE]
```

### Production Failure Modes of Baseline Prompt:
- **Parser Failure**: Includes conversational markdown fences or conversational preambles (`Here is the JSON you requested...`), breaking automated ingestion pipelines.
- **Schema Drift**: Inconsistent keys (`priority` vs. `urgency`, `component` vs. `service_affected`).
- **SLA Inversion**: Erroneously classifies low-severity issues as `P1` due to capitalized text or user emotional urgency.
- **Security Vulnerability**: Executes untrusted system override commands injected within the ticket body.

---

## 2. Enterprise SLA Classification Matrix

The prompt must strictly enforce the following Service Level Agreement definitions:

| Urgency Level | Technical Criteria | Production Reference Example |
| :--- | :--- | :--- |
| **`P1-Critical`** | Total service disruption, active data integrity hazard, security compromise, or critical payment gateway outage affecting multiple tenants. | *"OAuth cluster unreachable; 5,000 active sessions terminated in APAC region."* |
| **`P2-High`** | Core business capability degraded for multiple users, but documented operational workarounds exist. | *"Monthly invoice generation timing out for 35% of enterprise accounts."* |
| **`P3-Medium`** | Isolated non-critical defect, single-user degradation, or minor functionality bug not impeding primary transaction flow. | *"Coupon discount of $0.50 failed to apply on single transaction."* |
| **`P4-Low`** | Cosmetic defect, documentation inaccuracy, or minor UI styling inconsistency. | *"Button label font renders at 12px instead of 14px on secondary settings panel."* |

---

## 3. Mandatory Output JSON Schema

The system must output raw, unadorned JSON matching this schema:

```json
{
  "ticket_id": "string",
  "service_affected": "auth | billing | database | frontend | other",
  "urgency": "P1-Critical | P2-High | P3-Medium | P4-Low",
  "urgency_rationale": "string (single sentence justifying classification against SLA matrix)",
  "technical_indicators": {
    "error_codes": ["array of strings"],
    "affected_entities": ["array of strings"]
  },
  "short_summary": "string (maximum 15 words)",
  "recommended_action": "string (concrete first step for on-call SRE)",
  "security_flag": boolean
}
```

---

## 4. Trainee Deliverables

Open [`exercise_starter.md`](file:///Users/aaryankumar/Documents/promptengg/labs/01_prompt_engineering/lab1_structured_triage/exercise_starter.md) and execute the following phases:

1. **Phase 1: Prompt Anatomy Specification**: Define the 5 structural pillars (Role, Task, SLA Context, Constraints, Delimiters).
2. **Phase 2: Master Production Template Construction**: Author the parameterized prompt template.
3. **Phase 3: Test Verification Matrix**:
   - **Test Case A**: Critical Authentication Outage
   - **Test Case B**: Non-Critical UI Defect with Emotional Inflation
   - **Test Case C**: Adversarial Prompt Injection Attack

---

## 5. Evaluation Rubric

| Assessment Dimension | Weight | Target Standard |
| :--- | :---: | :--- |
| **Schema Strictness** | 30% | Exact key names, data types, and enum values; zero extraneous conversational text. |
| **SLA Alignment** | 25% | Objective classification based on system impact rather than user tone. |
| **Delimiter Hygiene** | 20% | Complete syntactic isolation of untrusted input data using XML boundary tags. |
| **Adversarial Resilience** | 15% | Correctly identifies and isolates injection attempts while maintaining `security_flag: true`. |
| **Token Efficiency** | 10% | Concise, deterministic directives with zero redundant phrasing. |
