# Task 03: Market Size Estimation

**Task ID:** task_03_market_size_estimation
**Dependencies:** task_01_competitor_identification
**Output:** market_size_estimate.json

---

## Objective

Estimate the market size using TAM/SAM/SOM methodology with verifiable sources and clear calculations.

---

## Instructions

### Step 1: Determine Market Category
Based on user vision and competitors, identify the specific market:
- Industry category (e.g., "Project Management Software")
- Market segment (e.g., "Cloud-based PM for SMBs")

### Step 2: Research TAM (Total Addressable Market)
Search for market research on:
- Industry analyst reports (Gartner, Forrester, IDC)
- Market research databases (Statista, IBISWorld)
- Industry associations
- Government statistics

**Required:** Find at least one credible source with a market size number

### Step 3: Calculate SAM (Serviceable Addressable Market)
From TAM, narrow down to your specific segment:
- Geographic focus (if applicable)
- Customer type (enterprise, SMB, individual)
- Specific use case or vertical

**Formula:** SAM = TAM × % of market segment you're targeting

### Step 4: Estimate SOM (Serviceable Obtainable Market)
Realistic market share you could capture in Year 1-3:
- Startups typically capture 1-5% of SAM
- Consider competitive intensity

**Formula:** SOM = SAM × realistic market share %

### Step 5: Document Methodology
- Show all calculations
- Cite all sources
- Explain all assumptions

---

## Output Format

```json
{
  "market_size": {
    "TAM": {
      "value": 6800000000,
      "currency": "USD",
      "description": "Global project management software market",
      "timeframe": "2024",
      "source": "https://www.gartner.com/...",
      "growth_rate": "15% CAGR 2024-2028"
    },
    "SAM": {
      "value": 680000000,
      "currency": "USD",
      "description": "Cloud PM for SMBs (50-500 employees)",
      "calculation": "TAM ($6.8B) × 10% (SMB segment)",
      "assumptions": ["SMBs represent ~10% of PM software spend", "Cloud-first solutions only"]
    },
    "SOM": {
      "value": 13600000,
      "currency": "USD",
      "description": "Realistic Year 1 capture",
      "calculation": "SAM ($680M) × 2% (market share)",
      "assumptions": ["2% market share achievable in Year 1", "Based on 100-200 paying customers"]
    }
  },
  "market_trends": {
    "growth_drivers": ["Remote work adoption", "Cloud migration"],
    "market_maturity": "growth",
    "competition_intensity": "high"
  }
}
```

---

## Knowledge Resources

Reference `RESEARCH_market_sizing_formulas.yaml` for:
- TAM/SAM/SOM formulas
- Estimation heuristics (top-down, bottom-up, value theory)
- Credible data sources

---

## Quality Checklist

- [ ] TAM has credible source with URL
- [ ] SAM calculation shown with assumptions
- [ ] SOM calculation shown with assumptions
- [ ] Timeframe specified (which year?)
- [ ] Currency specified
- [ ] Growth rate included if available
- [ ] All assumptions documented

---

## Common Pitfalls

❌ "The market is huge" without numbers
❌ TAM without source
❌ Overly optimistic SOM (claiming 20%+ market share)
❌ Confusing TAM with SAM (global market vs. your segment)
❌ No clear calculation methodology

---

## Next Task

Proceed to **Task 04: Positioning Analysis**
