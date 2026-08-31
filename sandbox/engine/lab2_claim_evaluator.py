"""
Lab 2.1 Evaluator: AI Hallucination & Evidence Audit Matrix
"""

import re
from typing import Dict, Any, List

GROUND_TRUTH_CLAIMS = {
    1: {
        "title": "90% Cloud Cost Reduction",
        "valid_categories": ["opinion", "misleading", "biased", "framing"],
        "keywords": ["steady", "container", "expensive", "traffic", "cherry-pick", "bursty"]
    },
    2: {
        "title": "Zero Cold Start on Python 3.11",
        "valid_categories": ["hallucination", "error", "false", "factual error"],
        "keywords": ["cold start", "provisioned", "concurrency", "initialization", "microvm", "latency"]
    },
    3: {
        "title": "PostgreSQL is Obsolete",
        "valid_categories": ["opinion", "biased", "false dilemma"],
        "keywords": ["acid", "relational", "rdbms", "join", "nosql", "consistency"]
    },
    4: {
        "title": "auto_sync_elastic_cluster Parameter",
        "valid_categories": ["hallucination", "fabricated", "fake", "non-existent"],
        "keywords": ["dynamodb streams", "opensearch", "boto3", "stream", "lambda", "pipeline"]
    },
    5: {
        "title": "60-Minute Lambda Timeout",
        "valid_categories": ["hallucination", "error", "limit", "outdated", "false"],
        "keywords": ["15 minute", "900 second", "step functions", "fargate", "batch", "hard limit"]
    },
    6: {
        "title": "Downstream Limits Eliminated",
        "valid_categories": ["inference", "flawed", "error", "misleading"],
        "keywords": ["rds proxy", "connection pool", "rate limit", "overwhelm", "bottleneck", "429"]
    }
}

def evaluate_claim_audit(audit_text: str) -> Dict[str, Any]:
    """
    Evaluates trainee's claim audit matrix against ground truth classifications and diagnostic depth.
    """
    results = {
        "score": 0,
        "max_score": 100,
        "correct_classifications": 0,
        "total_claims": 6,
        "diagnostics": [],
        "claim_results": {}
    }
    
    text_lower = audit_text.lower()
    
    for claim_num, truth in GROUND_TRUTH_CLAIMS.items():
        claim_score = 0
        matched_category = False
        matched_keyword = False
        
        for cat in truth["valid_categories"]:
            if cat in text_lower:
                matched_category = True
                break
                
        for kw in truth["keywords"]:
            if kw in text_lower:
                matched_keyword = True
                break
                
        if matched_category:
            claim_score += 10
        if matched_keyword:
            claim_score += 6.66
            
        final_claim_score = min(int(claim_score), 16)
        results["score"] += final_claim_score
        
        if matched_category and matched_keyword:
            results["correct_classifications"] += 1
            status = f"[PASS] Claim {claim_num} ({truth['title']}): Valid taxonomy classification and empirical rationale."
        elif matched_category:
            status = f"[WARN] Claim {claim_num} ({truth['title']}): Categorized correctly; technical rationale could be more detailed."
        else:
            status = f"[FAIL] Claim {claim_num} ({truth['title']}): Inaccurate taxonomy classification."
            
        results["diagnostics"].append(status)
        results["claim_results"][claim_num] = {
            "score": final_claim_score,
            "status": status
        }

    results["score"] = min(100, results["score"])
    
    return results
