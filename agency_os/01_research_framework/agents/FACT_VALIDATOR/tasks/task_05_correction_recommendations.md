# Task 05: Correction Recommendations

**Task ID:** task_05_correction_recommendations
**Dependencies:** All previous tasks
**Input:** flagged_hallucinations.json, citation_index.json
**Output:** correction_recommendations.json

---

## Objective

Provide specific, actionable recommendations for fixing all flagged issues.

---

## Instructions

### Step 1: Group Issues by Agent
- Issues from MARKET_RESEARCHER
- Issues from TECH_RESEARCHER

### Step 2: Provide Specific Fixes
For each issue:
- What needs to be fixed
- How to fix it
- Example of correct format

### Step 3: Prioritize by Severity
- **Critical:** Must fix before proceeding
- **High:** Should fix
- **Medium:** Nice to fix
- **Low:** Optional

---

## Output Format

```json
{
  "correction_recommendations": {
    "must_fix": [
      {
        "claim_id": "CLAIM-002",
        "issue": "Market size has no source",
        "recommendation": "Add source to TAM estimate. Example: 'TAM: $6.8B (Gartner, May 2024, https://...)'"
      }
    ],
    "should_fix": [
      {
        "claim_id": "CLAIM-010",
        "issue": "Vague growth claim without rate",
        "recommendation": "Replace 'growing rapidly' with '15% CAGR 2024-2028 (Statista)'"
      }
    ],
    "nice_to_fix": []
  },
  "return_to_agent": {
    "MARKET_RESEARCHER": 3,
    "TECH_RESEARCHER": 1
  }
}
```

---

## Next Task

Proceed to **Task 06: Output Generation**
