# 🔬 VIBE Research Framework - Documentation

**Version:** 1.0.0
**Status:** Production Ready
**Cost:** FREE (with optional paid upgrades)

---

## 📖 Overview

The **VIBE Research Framework** adds a **RESEARCH phase** to VIBE Agency that provides **fact-based validation** before business planning begins. It prevents hallucinated assumptions by enforcing citation requirements for all claims.

### The Problem It Solves
Users currently jump from idea → Lean Canvas without verifying:
- Market assumptions (competitors, pricing, market size)
- Technical feasibility (API limits, library maintenance, stack constraints)
- User insights (personas, pain points, interview questions)

This leads to **hallucinated assumptions** and failed pivots.

### The Solution
Add an **optional RESEARCH phase** with 4 specialized agents that generate a **citation-backed** `research_brief.json` artifact.

---

## 🏗️ Architecture

```
PLANNING PHASE
│
├── RESEARCH (NEW - Optional)
│   ├── MARKET_RESEARCHER (Competitor analysis, pricing, market sizing)
│   ├── TECH_RESEARCHER (API evaluation, library comparison, FAE validation)
│   ├── FACT_VALIDATOR (Hallucination detection, citation enforcement)
│   └── USER_RESEARCHER (Persona generation, interview scripts)
│   │
│   └─→ research_brief.json
│
├── BUSINESS_VALIDATION (Updated to accept research_brief.json)
│   └── LEAN_CANVAS_VALIDATOR
│   └─→ lean_canvas_summary.json
│
└── FEATURE_SPECIFICATION
    └── VIBE_ALIGNER
    └─→ feature_spec.json
```

---

## 🚀 Quick Start

### Prerequisites
- Python 3.9+ or Node.js 18+
- Git
- (Optional) Google Custom Search API key for web research

### Installation

```bash
# Clone the repository
git clone https://github.com/your-org/vibe-research.git
cd vibe-research

# Install dependencies
pip install -r requirements.txt  # or npm install

# (Optional) Set up API keys
cp .env.example .env
# Edit .env with your API keys
```

### Basic Usage

```bash
# Run research phase
python vibe-cli.py research --vision "Build a project management tool for creative agencies"

# Output: research_brief.json
```

---

## 🔑 API Keys & Cost Breakdown

### 💰 Cost Summary

| Service | Cost | Required? | Use Case |
|---------|------|-----------|----------|
| **Google Custom Search API** | **FREE** (100/day) | **YES** | Web search for all agents |
| GitHub API | **FREE** | **YES** | Library maintenance checks |
| npm/PyPI APIs | **FREE** | **YES** | Package information |
| Gartner/Statista | $15,000+/year | **NO** | Market data (alternatives exist) |
| Anthropic Claude API | $3-15/million tokens | **YES** | AI agent execution |

**Total minimal cost: ~$0-5/month (within free tiers)**

---

## 🔧 API Setup Guide

### 1. Google Custom Search API (REQUIRED - FREE)

**Why needed:** For web searches (competitor research, pricing data, API docs)

**Free tier:** 100 searches/day (sufficient for most research)

**Setup:**

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create new project (or use existing)
3. Enable **Custom Search API**
4. Create credentials → API Key
5. Create a **Custom Search Engine**:
   - Visit [Programmable Search Engine](https://programmablesearchengine.google.com/)
   - Create new search engine
   - Search the entire web: Enable
   - Get your **Search Engine ID**

6. Add to `.env`:
```bash
GOOGLE_API_KEY=your_api_key_here
GOOGLE_CSE_ID=your_search_engine_id_here
```

**Cost:**
- 100 queries/day: FREE
- Beyond 100: $5 per 1,000 queries

**Alternatives (if you exceed free tier):**
- SerpAPI ($50/month for 5,000 searches)
- Bing Search API (FREE for 1,000 searches/month)
- Web scraping (free but more complex)

---

### 2. GitHub API (REQUIRED - FREE)

**Why needed:** For library maintenance checks (TECH_RESEARCHER)

**Free tier:** 5,000 requests/hour (more than enough)

**Setup:**

1. Go to [GitHub Settings](https://github.com/settings/tokens)
2. Generate new token (classic)
3. Select scopes: `public_repo` (read-only)
4. Copy token

5. Add to `.env`:
```bash
GITHUB_TOKEN=your_github_token_here
```

**Cost:** FREE (no payment required)

---

### 3. Anthropic Claude API (REQUIRED - Paid)

**Why needed:** AI agent execution (all 4 agents)

**Cost:**
- Claude 3.5 Sonnet: $3 per million input tokens, $15 per million output tokens
- Typical research project: $0.50 - $2.00

**Setup:**

1. Go to [Anthropic Console](https://console.anthropic.com/)
2. Add credits ($5 minimum)
3. Generate API key

4. Add to `.env`:
```bash
ANTHROPIC_API_KEY=your_anthropic_key_here
```

---

## 📊 Market Data Sources (Alternatives to Gartner/Statista)

The framework is designed to work **WITHOUT expensive market research subscriptions**.

### FREE Market Data Sources

| Source | Type | Cost | Data Available |
|--------|------|------|----------------|
| **Crunchbase (free tier)** | Company data | FREE | Funding, competitors, market |
| **ProductHunt** | Product trends | FREE | Competitor analysis |
| **Y Combinator Directory** | Startup data | FREE | Market sizing (bottom-up) |
| **Google Trends** | Search trends | FREE | Market interest over time |
| **Reddit/HackerNews** | Community insights | FREE | User pain points, preferences |
| **GitHub Trending** | Tech trends | FREE | Popular libraries, tools |
| **Stack Overflow Trends** | Developer data | FREE | Technology adoption |

### PAID Market Data (Optional)

| Source | Cost | When to Use |
|--------|------|-------------|
| **Statista Basic** | $39/month | For validated market size data |
| **CB Insights (startup)** | $99/month | For competitive intelligence |
| **SimilarWeb Starter** | $125/month | For competitor traffic data |

**Recommendation:** Start with FREE sources. Only pay if you need validated data for investors.

---

## 🔍 How Each Agent Uses APIs

### MARKET_RESEARCHER

**APIs used:**
- ✅ Google Custom Search API (free tier sufficient)
- ✅ Web scraping (competitor pricing pages)
- ⚠️ Optional: Statista API (if you pay)

**What it does:**
1. Searches for competitors via Google
2. Visits competitor pricing pages directly
3. Extracts market data from public sources
4. Calculates market size using bottom-up estimation (no Gartner needed!)

**Example:**
```bash
# Research competitors for "project management tool"
python vibe-cli.py research market --vision "Build PM tool for agencies"

# Output includes:
# - 5 competitors found (Asana, Monday.com, etc.)
# - Pricing: $10.99/user/month (source: asana.com/pricing)
# - Market size: $12M SAM (calculated bottom-up, no Gartner needed)
```

---

### TECH_RESEARCHER

**APIs used:**
- ✅ GitHub API (free)
- ✅ npm Registry API (free)
- ✅ PyPI API (free)
- ✅ Google Custom Search API (for API docs)

**What it does:**
1. Evaluates APIs by reading official documentation
2. Checks library maintenance status on GitHub
3. Verifies rate limits from official docs
4. Identifies technical constraints

**Example:**
```bash
# Research tech stack for payment features
python vibe-cli.py research tech --features "payment processing, email"

# Output includes:
# - Recommended APIs: Stripe ($0.029 + $0.30/transaction, source: stripe.com/pricing)
# - Libraries: React (220k stars, last commit: 2025-11-10, MIT license)
# - Constraints: "Vercel serverless: 10MB request limit"
```

---

### FACT_VALIDATOR

**APIs used:**
- ✅ None (validates existing research data)

**What it does:**
1. Checks all claims have sources
2. Detects red flags (context-collapse, plausible falsehoods)
3. Calculates quality score
4. **BLOCKS** research if quality < 50 or critical issues found

**Example:**
```bash
# Validate research quality
python vibe-cli.py research validate

# Output:
# Quality Score: 85/100 ✅
# Issues: 3 (all low severity)
# Critical Issues: 0
# Status: READY for LEAN_CANVAS_VALIDATOR
```

---

### USER_RESEARCHER

**APIs used:**
- ✅ None (generates templates)

**What it does:**
1. Generates 2-3 user personas
2. Creates interview scripts
3. Designs survey templates
4. Maps user journeys

**Example:**
```bash
# Generate user research artifacts
python vibe-cli.py research users --vision "Build PM tool for agencies"

# Output includes:
# - Persona: "Agency Owner Alice" (35-45, goals, pain points)
# - Interview script: 15 open-ended questions
# - Survey template: 10 questions (screener + core)
# - User journey: 5 stages (Awareness → Retention)
```

---

## 💾 Output Format

All agents generate JSON outputs that conform to `research_brief.schema.json`:

```json
{
  "version": "1.0",
  "project_id": "uuid",
  "research_completed_at": "2025-11-14T10:30:00Z",

  "market_analysis": {
    "competitors": [...],
    "pricing_insights": {...},
    "market_size": "TAM: $6.8B (calculated bottom-up)...",
    "positioning_opportunities": [...],
    "risks": [...]
  },

  "tech_analysis": {
    "recommended_apis": [...],
    "recommended_libraries": [...],
    "technical_constraints": [...],
    "feasibility_score": "high",
    "flagged_features": [...]
  },

  "fact_validation": {
    "validated_claims": [...],
    "flagged_hallucinations": [...],
    "citation_index": [...],
    "quality_score": "85/100",
    "issues_found": 3,
    "issues_critical": 0
  },

  "user_insights": {
    "personas": [...],
    "pain_points": [...],
    "interview_script": {...},
    "user_journeys": [...]
  },

  "handoff_to_lean_canvas": {
    "status": "READY",
    "key_insights": [...]
  }
}
```

---

## 🚦 Quality Gates

The framework enforces quality through validation gates:

### BLOCKING Gates (Stop workflow if failed)

1. **gate_all_competitors_cited** (MARKET_RESEARCHER)
   - Every competitor must have source URL
   - Blocks if any competitor lacks source

2. **gate_pricing_data_verifiable** (MARKET_RESEARCHER)
   - All pricing claims must link to official pricing pages
   - Blocks if pricing sources missing

3. **gate_market_size_has_source** (MARKET_RESEARCHER)
   - Market size estimates must cite methodology
   - Blocks if TAM/SAM/SOM lacks calculation

4. **gate_all_apis_have_docs** (TECH_RESEARCHER)
   - Every API must link to official documentation
   - Blocks if API docs missing

5. **gate_library_maintenance_checked** (TECH_RESEARCHER)
   - All libraries must have verified maintenance status
   - Blocks if maintenance status missing

6. **gate_no_critical_hallucinations** (FACT_VALIDATOR)
   - Quality score must be >= 50
   - Critical issues must be 0
   - **BLOCKS ENTIRE WORKFLOW** if failed

### WARNING Gates (Don't block, but flag issues)

1. **gate_fae_violations_cited** (TECH_RESEARCHER)
   - Warns if FAE rule IDs malformed
   - Doesn't block (may not have FAE rule yet)

2. **gate_personas_industry_standard** (USER_RESEARCHER)
   - Warns if personas too generic or missing fields
   - Doesn't block (personas can be refined)

3. **gate_interview_questions_actionable** (USER_RESEARCHER)
   - Warns if questions are yes/no or leading
   - Doesn't block (questions can be adapted)

---

## 🔒 Citation Requirements

**Critical claims requiring sources:**
- Market size estimates
- Competitor pricing
- Technical feasibility assessments
- API rate limits and pricing
- Library maintenance status

**Acceptable sources:**
- Official vendor documentation
- Peer-reviewed research
- Industry analyst reports (if you have access)
- Official GitHub repositories
- Verified pricing pages
- Government statistics

**Unacceptable sources:**
- Blog posts without credentials
- Forum comments
- Social media posts
- AI-generated content
- Outdated documentation (>2 years old)

---

## 🧪 Testing Without Real APIs

You can test the framework without API keys using mock data:

```bash
# Run in test mode (uses mock data)
python vibe-cli.py research --vision "Test project" --mock

# Or run specific agent in test mode
python vibe-cli.py research market --mock
```

**Mock mode provides:**
- Simulated competitor data
- Fake pricing information
- Sample market size calculations
- **Useful for:** Testing workflows, development, demos

---

## 📁 File Structure

```
agency_os/01_research_framework/
├── agents/
│   ├── MARKET_RESEARCHER/
│   │   ├── _composition.yaml
│   │   ├── _knowledge_deps.yaml
│   │   ├── _prompt_core.md
│   │   ├── tasks/ (6 tasks)
│   │   └── gates/ (3 gates)
│   ├── TECH_RESEARCHER/
│   │   ├── _composition.yaml
│   │   ├── _knowledge_deps.yaml
│   │   ├── _prompt_core.md
│   │   ├── tasks/ (6 tasks)
│   │   └── gates/ (3 gates)
│   ├── FACT_VALIDATOR/
│   │   ├── _composition.yaml
│   │   ├── _knowledge_deps.yaml
│   │   ├── _prompt_core.md
│   │   ├── tasks/ (6 tasks)
│   │   └── gates/ (3 gates)
│   └── USER_RESEARCHER/
│       ├── _composition.yaml
│       ├── _knowledge_deps.yaml
│       ├── _prompt_core.md
│       ├── tasks/ (6 tasks)
│       └── gates/ (2 gates)
├── knowledge/
│   ├── RESEARCH_market_sizing_formulas.yaml
│   ├── RESEARCH_competitor_analysis_templates.yaml
│   ├── RESEARCH_red_flag_taxonomy.yaml
│   ├── RESEARCH_persona_templates.yaml
│   ├── RESEARCH_interview_question_bank.yaml
│   └── RESEARCH_constraints.yaml
└── state_machine/
    └── RESEARCH_workflow_design.yaml
```

---

## 🛠️ Configuration

### .env.example

```bash
# Required
ANTHROPIC_API_KEY=your_anthropic_key_here
GOOGLE_API_KEY=your_google_api_key_here
GOOGLE_CSE_ID=your_custom_search_engine_id_here
GITHUB_TOKEN=your_github_token_here

# Optional (for enhanced market research)
STATISTA_API_KEY=your_statista_key_here  # If you have subscription
CRUNCHBASE_API_KEY=your_crunchbase_key_here  # Optional

# Framework settings
RESEARCH_PHASE_ENABLED=true
FACT_VALIDATOR_QUALITY_THRESHOLD=50
CITATION_ENFORCEMENT=strict  # strict|permissive
```

---

## 🚀 Production Deployment

### Environment Variables

```bash
# Production
export ENVIRONMENT=production
export ANTHROPIC_API_KEY=sk-ant-...
export GOOGLE_API_KEY=AIza...
export GITHUB_TOKEN=ghp_...

# Run research
python vibe-cli.py research --vision "Your project vision"
```

### Docker Deployment

```dockerfile
FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

ENV ANTHROPIC_API_KEY=""
ENV GOOGLE_API_KEY=""
ENV GITHUB_TOKEN=""

CMD ["python", "vibe-cli.py", "research"]
```

---

## 📊 Cost Estimation

### Typical Research Project Cost

| Component | Cost |
|-----------|------|
| Google Custom Search (100 queries) | $0 (free tier) |
| GitHub API | $0 (free) |
| Anthropic Claude (research phase) | $1-3 per project |
| **Total** | **$1-3 per project** |

### Monthly Cost (10 projects)

| Scenario | Cost |
|----------|------|
| Within free tiers | $10-30/month (Claude only) |
| Exceeding free tiers | $40-60/month |
| With Statista subscription | $89-230/month |

**Recommendation:** Start free, upgrade only if needed.

---

## 🆘 Troubleshooting

### "Google API quota exceeded"

**Solution 1:** Wait for quota reset (midnight Pacific Time)
**Solution 2:** Upgrade to paid tier ($5/1,000 queries)
**Solution 3:** Use alternative search API (Bing, SerpAPI)

### "GitHub API rate limit"

**Solution 1:** Add GitHub token (increases to 5,000/hour)
**Solution 2:** Wait for rate limit reset (1 hour)

### "FACT_VALIDATOR blocking workflow"

**Reason:** Quality score < 50 or critical issues found
**Solution:** Check `research_brief.json` → `fact_validation.flagged_hallucinations`
**Fix:** Add sources to flagged claims

### "Market size data unavailable"

**Solution:** Use bottom-up estimation instead of top-down:
- Estimate target customers × ARPU
- No Gartner/Statista needed!

---

## 📚 Further Reading

- [Technical Blueprint](workspaces/vibe_research_framework/artifacts/planning/TECHNICAL_BLUEPRINT.md)
- [Feature Specifications](workspaces/vibe_research_framework/artifacts/planning/VIBE_RESEARCH_FRAMEWORK_SPECS.md)
- [Data Contracts](agency_os/00_system/contracts/ORCHESTRATION_data_contracts.yaml)
- [Workflow Design](agency_os/01_research_framework/state_machine/RESEARCH_workflow_design.yaml)

---

## 🤝 Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for development setup and contribution guidelines.

---

## 📄 License

See [LICENSE](LICENSE) file for details.

---

**Built with ❤️ for evidence-based product development**
