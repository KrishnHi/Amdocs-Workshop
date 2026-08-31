# Practical 2.2: Architectural Fallacy & Cognitive Bias Assessment

**Module**: Module 2 - Critical Thinking  
**Level**: Associate / Graduate Trainee  
**Duration**: 45 Minutes  
**Core Technical Competencies**: Logical Fallacy Identification (False Dilemma, False Cause, Straw Man, Appeal to Authority), Unstated Risk Assumptions Extraction, Phased Modernization Planning.

---

## 1. Business Context & Problem Specification

Engineering teams frequently utilize AI assistants to formulate architectural proposals, refactoring roadmaps, and technology selection memos. 

Because LLM training data is heavily weighted toward promotional internet blog posts, AI-generated strategy documents often replicate common reasoning defects: false dichotomies, correlation-causation fallacies, and distorted portrayals of legacy systems. Adopting such proposals without critical analysis exposes enterprise systems to severe delivery delays, operational instability, and budget overruns.

In this laboratory, trainees dissect an AI-generated architecture proposal ([`ai_proposal.md`](file:///Users/aaryankumar/Documents/promptengg/labs/02_critical_thinking/lab2_fallacy_buster/ai_proposal.md)), extract unstated operational assumptions, and formulate an incremental modernization strategy.

---

## 2. Catalog of Enterprise AI Fallacies

| Formal Fallacy | Technical Definition | Manifestation in AI Technical Proposals |
| :--- | :--- | :--- |
| **False Dilemma (Black-and-White)** | Presenting two extreme options as the sole alternatives while ignoring pragmatic intermediate solutions. | *"Either we execute an immediate total rewrite into 35 microservices this quarter, or the company fails."* |
| **False Cause (Post Hoc)** | Inferring a direct causal relationship solely from historical temporal correlation. | *"Streaming Platform X adopted microservices and their revenue grew 350%; therefore microservices will triple our revenue."* |
| **Straw Man** | Caricaturing and exaggerating an opposing technical position to make it easier to invalidate. | *"Advocating for a modular monolith is equivalent to demanding 1990s unmaintainable spaghetti code without tests."* |
| **Appeal to Authority** | Validating an engineering strategy based on influencer endorsement or social media popularity rather than empirical data. | *"A prominent social media influencer with 150k followers stated monoliths are dead, proving we must migrate immediately."* |

---

## 3. Unstated Operational Assumptions

An **unstated assumption** is a prerequisite that must hold true for a conclusion to be valid, but which the proposal fails to substantiate or plan for.

*Example*:
- **Asserted Premise**: "Microservices allow independent squad deployments."
- **Asserted Conclusion**: "Adopting microservices will immediately increase engineering velocity."
- **Hidden Prerequisites**:
  1. Assumes the organization possesses mature DevOps, automated CI/CD pipelines, and distributed observability (OpenTelemetry).
  2. Assumes distributed network latency and failure modes will not degrade transactional SLAs.
  3. Assumes data consistency can be maintained without introducing distributed 2PC/Saga transaction complexity.

---

## 4. Trainee Deliverables

Open [`exercise_starter.md`](file:///Users/aaryankumar/Documents/promptengg/labs/02_critical_thinking/lab2_fallacy_buster/exercise_starter.md) and execute:
- **Phase 1: Fallacy Identification Matrix**: Map the 4 logical fallacies in the proposal with precise technical explanations.
- **Phase 2: Unmasking Unstated Assumptions**: Extract at least 3 operational/organizational prerequisites omitted from the proposal.
- **Phase 3: Phased Modernization Strategy**: Author a realistic 3-phase engineering counter-proposal prioritizing test automation and modular encapsulation.

---

## 5. Evaluation Rubric

| Assessment Dimension | Weight | Target Standard |
| :--- | :---: | :--- |
| **Fallacy Taxonomy** | 35% | Accurately identifies False Dilemma, False Cause, Straw Man, and Appeal to Authority. |
| **Assumption Extraction** | 30% | Detects hidden organizational, tooling, and network latency risks. |
| **Pragmatic Strategy** | 25% | Formulates an incremental, risk-managed roadmap (e.g. modular monolith before service extraction). |
| **Analytical Tone** | 10% | Objective, evidence-based engineering prose with zero emotional hyperbole. |
