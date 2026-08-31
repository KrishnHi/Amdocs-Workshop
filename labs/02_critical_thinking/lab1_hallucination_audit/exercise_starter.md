# Trainee Practical Assessment: Practical 2.1

**Trainee Name**: _Krishna Hitnalikar
**Employee ID**: __215677
**Date**: __31/08/2026

---

## Instructions
You will perform a forensic audit of the AI-generated cloud modernization proposal in `ai_generated_report.md`. Complete the Claim Classification Matrix (Section 1), implement the verification protocols (Section 2), and write a concise, fact-checked Executive Summary (Section 3). Every factual classification must be accompanied by at least one primary-source reference (official docs, SDK reference, or measured evidence). Where an SDK method or parameter is asserted by the AI, verify it programmatically (example snippets below).

---

## Section 1: Claim Classification Matrix

Fill the table below. For each claim provide: taxonomy category, short accuracy assessment, and a technical diagnosis plus at least one primary-source link or a short empirical verification action.

| Claim Number | Taxonomy Category | Accuracy Assessment | Technical Diagnosis & Empirical Justification |
| :--- | :--- | :--- | :--- |
| **Claim 1** (Migrating to Lambda reduces bill by 90% across all traffic) | OPINION / MISLEADING FRAMING | Misleading / Not universally true | Cost depends on workload profile (steady high-throughput vs bursty), function memory, avg duration, concurrency, API Gateway / VPC costs, and ancillary services. Verification: produce a cost model using AWS Lambda pricing and compare to container/EKS pricing. Primary sources: AWS Lambda pricing: https://aws.amazon.com/lambda/pricing/ ; AWS Cost Explorer: https://aws.amazon.com/aws-cost-management/aws-cost-explorer/ |
| **Claim 2** (Zero cold-start on Python 3.11 by default) | HALLUCINATION / FACTUAL ERROR | Inaccurate | Cold-start latency is real for standard runtimes; mitigation requires provisioned concurrency or architectural changes. Verification: consult Lambda best-practices and measure cold-starts by deploying a minimal Python 3.11 function and invoking after idle. Primary sources: Lambda best practices (cold-start guidance) & Provisioned Concurrency: https://docs.aws.amazon.com/lambda/latest/dg/provisioned-concurrency.html ; https://docs.aws.amazon.com/lambda/latest/dg/best-practices.html |
| **Claim 3** (PostgreSQL is obsolete) | OPINION / BIASED FRAMING | Inaccurate / Biased | Relational DBs remain essential for ACID transactions and complex queries. DynamoDB is suitable for specific high-throughput, key-value, or document patterns but not a wholesale replacement. Verification: map workload requirements (transactions, joins, analytical queries) to DB choices. Primary sources: DynamoDB overview: https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html ; Amazon RDS for PostgreSQL: https://aws.amazon.com/rds/postgresql/ |
| **Claim 4** (`auto_sync_elastic_cluster` / `update_table_settings`) | HALLUCINATION / FABRICATED API | Fabricated | No `update_table_settings` or `AutoSyncElasticCluster` parameter exists in official boto3 DynamoDB client. Correct approach: DynamoDB Streams -> consumer (Lambda/Kinesis/Firehose) -> OpenSearch. Verification: introspect boto3 dynamodb client and consult Boto3 docs. Primary sources: Boto3 DynamoDB reference: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb.html ; DynamoDB Streams: https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Streams.html |
| **Claim 5** (Lambda can be configured to 60-minute timeout) | HALLUCINATION / LIMIT VIOLATION | Incorrect (Hard limit) | AWS Lambda enforces a hard maximum execution timeout of 15 minutes (900 seconds). Long jobs require alternative services (ECS/Fargate, AWS Batch, Step Functions orchestration). Verification: consult Lambda configuration limits. Primary source: Lambda configuration limits: https://docs.aws.amazon.com/lambda/latest/dg/configuration-limits.html |
| **Claim 6** (Downstream limits eliminated by Lambda horizontal scaling) | INFERENCE (FLAWED) | Flawed inference | Lambda increases concurrency; downstream systems (DBs, third-party APIs) have connection and rate limits which can be overwhelmed. Verification: identify downstream quotas and perform controlled concurrency tests; incorporate throttles/backpressure. Primary sources: Lambda concurrency & scaling: https://docs.aws.amazon.com/lambda/latest/dg/configuration-concurrency.html ; API Gateway throttling: https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-request-throttling.html |

---

## Section 2: Verification Protocols & Source Quality

1. **Protocol for SDK API Verification**
   - Verification Action:
     - Programmatically inspect the boto3 client for any referenced method/parameter.
     - Example check (copy-paste into a Python environment with AWS credentials configured):
       ```python
       import boto3
       dynamodb = boto3.client('dynamodb', region_name='us-east-1')
       methods = [m for m in dir(dynamodb) if not m.startswith('_')]
       print("update_table_settings" in methods)  # expected False for fabricated API
       # Optionally print a short list of methods to inspect:
       print(sorted([m for m in methods if 'update' in m or 'table' in m])[:50])
       ```
     - Cross-check any positive findings against the official boto3 docs: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb.html
   - Evidence required:
     - Paste the REPL output (or a screenshot) showing the method absence/presence and the doc link proving the ground truth.

2. **Protocol for Cloud Quotas and Limits**
   - Verification Action:
     - Consult official AWS service limits documentation and the Service Quotas console/API.
     - Commands (conceptual examples):
       - Read the limit page: https://docs.aws.amazon.com/lambda/latest/dg/configuration-limits.html
       - Use AWS CLI to fetch service quotas (example):
         aws service-quotas list-service-quotas --service-code lambda
     - Evidence required: quote the relevant doc paragraph and paste the CLI/json snippet or URL that confirms the limit.
   - Focus points:
     - Lambda max timeout — confirm 900s.
     - DB connection limits, API Gateway throttles, account-level concurrency.

3. **Protocol for Performance & Cost Assertions**
   - Verification Action:
     - Build minimal prototypes for measured comparison:
       - Deploy a minimal containerized service and an equivalent Lambda handler.
       - Simulate representative load (e.g., k6 or locust) for at least two profiles: bursty and sustained.
       - Record latency, error rate, and estimated monthly cost (using pricing formulas).
     - Evidence required: CSV or brief table of measured latencies and extrapolated costs with clear assumptions (requests/sec, avg duration, memory).

4. **Mitigation of Automation Bias**
   - Engineering Habit (must-do):
     - Require at least one primary-source citation per factual claim in AI outputs.
     - Require a programmatic verification for any SDK method/parameter asserted.
     - Peer-review gate: no AI-suggested infra change is accepted without a second engineer’s signoff and one primary-source proof.

---

## Section 3: Revised Fact-Checked Executive Summary

```markdown
### Executive Technical Brief: Serverless Assessment & Architectural Guardrails

Summary:
Migrating portions of our order processing to AWS Lambda can deliver operational simplicity and cost-efficiency for event-driven or highly bursty workflows, but it is not a universal cost reduction for all traffic profiles nor an automatic cure for backend constraints. The AI proposal contains several factual inaccuracies and fabricated API suggestions that must be corrected before operational decisions are made.

Key findings and recommendations:
1. Cost Modeling Required (Claim 1)
   - Action: Produce a quantitative cost model comparing Lambda vs containerized options for at least two workload profiles (bursty and steady high-throughput). Use AWS Lambda pricing (GB-second + requests) and include API Gateway, VPC NAT, RDS, and data transfer costs in the model. See: https://aws.amazon.com/lambda/pricing/

2. Cold-Start Reality & Mitigation (Claim 2)
   - Fact: Standard Python runtimes experience initialization overhead (cold-starts). Mitigations include Provisioned Concurrency for latency-critical paths, smaller deployment packages, and keeping hot warmers where appropriate. See: https://docs.aws.amazon.com/lambda/latest/dg/provisioned-concurrency.html
   - Action: Measure cold-start times for our representative handler and, if required, enable Provisioned Concurrency for checkout/payment flows.

3. Data Layer Fit-Gap (Claim 3)
   - Fact: DynamoDB is suitable for certain high-throughput, key-value patterns; relational databases (PostgreSQL) remain necessary for ACID transactions, complex queries, and analytics.
   - Action: Perform a workload decomposition: keep PostgreSQL for transactional/analytical workloads and migrate high-ingest, simple-key patterns to DynamoDB where applicable. See: https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html

4. Synchronization Pattern (Claim 4)
   - Fact: There is no `AutoSyncElasticCluster` flag or `update_table_settings` API in official DynamoDB/Boto3. Correct synchronization approach: DynamoDB Streams -> Lambda/Kinesis/Firehose -> OpenSearch. Verify via boto3: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb.html and Streams: https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Streams.html
   - Action: Implement a streaming pipeline (DynamoDB Streams consumer) with idempotent delivery to OpenSearch, and test backpressure behavior.

5. Execution Duration Limits (Claim 5)
   - Fact: AWS Lambda enforces a maximum execution timeout of 15 minutes (900 seconds). For 45-minute reconciliation jobs, use AWS Batch, ECS/Fargate, or chunked processing orchestrated by Step Functions. See: https://docs.aws.amazon.com/lambda/latest/dg/configuration-limits.html
   - Action: Re-architect long-running jobs to a batch or worker model.

6. Downstream Capacity & Throttling (Claim 6)
   - Fact: Lambda scaling increases concurrency and can expose or worsen downstream limits (DB connections, API rate limits).
   - Action: Introduce request throttling, concurrency limits, and backpressure patterns. Evaluate connection pooling strategies and move blocking/long-duration I/O to controlled worker tiers (ECS/Batch). See Lambda concurrency docs: https://docs.aws.amazon.com/lambda/latest/dg/configuration-concurrency.html

Immediate next steps (minimum viable validation)
- Produce the cost model and run two benchmark prototypes.
- Run the boto3 introspection script to identify fabricated SDK calls and include proof in the audit report.
- Replace any fabricated code snippets with verified patterns and sample code for DynamoDB Streams -> OpenSearch.
