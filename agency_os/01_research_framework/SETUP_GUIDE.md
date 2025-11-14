# 🚀 VIBE Research Framework - Setup Guide

**Time to set up:** 15-20 minutes
**Cost:** FREE (with optional paid upgrades)

---

## 📋 Prerequisites

- Python 3.9+ OR Node.js 18+
- Git
- Google account (for free APIs)
- GitHub account (for free token)
- Anthropic account (requires payment, but cheap: $1-3/project)

---

## 🎯 Step-by-Step Setup

### Step 1: Clone Repository

```bash
git clone https://github.com/your-org/vibe-research.git
cd vibe-research
```

---

### Step 2: Install Dependencies

**Python:**
```bash
pip install -r requirements.txt
```

**Node.js:**
```bash
npm install
```

---

### Step 3: Set Up API Keys

Copy the example environment file:
```bash
cp .env.example .env
```

Now we'll fill in the API keys one by one...

---

### Step 4: Get Anthropic API Key (REQUIRED - ~$5 minimum)

**Why needed:** To run the AI agents (all 4 research agents)

**Cost:** $3 per million input tokens, $15 per million output tokens
- Typical research project: $1-3
- Monthly (10 projects): ~$10-30

**Setup:**

1. Go to [https://console.anthropic.com/](https://console.anthropic.com/)
2. Sign up / Log in
3. Click **"Get API keys"**
4. Add payment method (minimum $5 credit)
5. Click **"Create Key"**
6. Copy the key (starts with `sk-ant-api03-...`)

7. Add to `.env`:
```bash
ANTHROPIC_API_KEY=sk-ant-api03-your_key_here
```

✅ **Done! Most important key configured.**

---

### Step 5: Get Google Custom Search API (REQUIRED - FREE)

**Why needed:** To search the web for competitor data, pricing, API docs

**Free tier:** 100 searches/day (enough for most projects!)

**Setup:**

#### 5a. Enable Google Custom Search API

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create new project or select existing:
   - Click dropdown at top
   - Click **"New Project"**
   - Name: "VIBE Research"
   - Click **"Create"**

3. Enable Custom Search API:
   - Go to [API Library](https://console.cloud.google.com/apis/library)
   - Search for **"Custom Search API"**
   - Click on it
   - Click **"Enable"**

4. Create API key:
   - Go to [Credentials](https://console.cloud.google.com/apis/credentials)
   - Click **"Create Credentials"** → **"API key"**
   - Copy the API key (starts with `AIza...`)

5. Add to `.env`:
```bash
GOOGLE_API_KEY=AIza_your_key_here
```

#### 5b. Create Custom Search Engine

1. Go to [Programmable Search Engine](https://programmablesearchengine.google.com/)
2. Click **"Add"** or **"Get Started"**
3. Configure:
   - **Name:** VIBE Research Search
   - **What to search:** Search the entire web
   - Toggle **"Search the entire web"** → ON
   - Click **"Create"**

4. Get Search Engine ID:
   - Click on your new search engine
   - Go to **"Setup"** tab
   - Copy **"Search engine ID"** (looks like `0123456789abcdef0:a1b2c3d4e5f`)

5. Add to `.env`:
```bash
GOOGLE_CSE_ID=your_search_engine_id_here
```

✅ **Done! You now have 100 free searches per day.**

---

### Step 6: Get GitHub Token (REQUIRED - FREE)

**Why needed:** To check library maintenance status (TECH_RESEARCHER)

**Free tier:** 5,000 requests/hour (way more than needed!)

**Setup:**

1. Go to [GitHub Settings → Tokens](https://github.com/settings/tokens)
2. Click **"Generate new token"** → **"Generate new token (classic)"**
3. Configure:
   - **Note:** VIBE Research Framework
   - **Expiration:** 90 days (or No expiration)
   - **Select scopes:** Check `public_repo` only
   - Click **"Generate token"**

4. Copy the token (starts with `ghp_...`)
   - ⚠️ **Important:** Copy now! You can't see it again.

5. Add to `.env`:
```bash
GITHUB_TOKEN=ghp_your_token_here
```

✅ **Done! All required APIs configured.**

---

### Step 7: Verify Configuration

Test that everything works:

```bash
# Test API keys
python -c "import os; from dotenv import load_dotenv; load_dotenv(); \
print('✅ Anthropic:', 'OK' if os.getenv('ANTHROPIC_API_KEY') else '❌ Missing'); \
print('✅ Google:', 'OK' if os.getenv('GOOGLE_API_KEY') else '❌ Missing'); \
print('✅ GitHub:', 'OK' if os.getenv('GITHUB_TOKEN') else '❌ Missing')"
```

Expected output:
```
✅ Anthropic: OK
✅ Google: OK
✅ GitHub: OK
```

---

## 🧪 Test Your Setup

Run a test research project:

```bash
# Test with mock data (no API calls)
python vibe-cli.py research --vision "Test project" --mock

# Test with real APIs (uses your API keys)
python vibe-cli.py research --vision "Build a task management app"
```

Expected output:
```
🔬 Starting RESEARCH phase...
✅ MARKET_RESEARCHER: Found 5 competitors
✅ TECH_RESEARCHER: Evaluated 3 APIs, 8 libraries
✅ FACT_VALIDATOR: Quality score 85/100 ✅
✅ USER_RESEARCHER: Generated 3 personas

📄 Output: research_brief.json
```

---

## 💰 Cost Monitoring

### Stay Within Free Tiers

**Daily usage tracker:**
```bash
# Check today's Google Search usage
python vibe-cli.py research stats --today

# Output:
# Google Searches: 23/100 (77 remaining today)
# GitHub API calls: 145/5000 (4855 remaining this hour)
```

### Set Up Alerts

Add to `.env`:
```bash
# Alert when approaching limits
GOOGLE_SEARCH_ALERT_THRESHOLD=80  # Alert at 80/100 searches
GITHUB_API_ALERT_THRESHOLD=4500   # Alert at 4500/5000 requests
```

---

## 🔧 Optional: Enhanced Market Research

If you want **validated market size data** (not required!):

### Option A: Statista Basic ($39/month)

**When to use:** Need specific market size numbers for investors

**Setup:**
1. Sign up at [statista.com](https://www.statista.com/)
2. Subscribe to Basic plan ($39/month)
3. Get API key from account settings
4. Add to `.env`:
```bash
STATISTA_API_KEY=your_statista_key_here
```

### Option B: Use Free Alternatives (Recommended!)

**Instead of Statista, use:**
- Bottom-up market sizing (calculate yourself)
- Crunchbase free tier
- Public sources (Reddit, HackerNews, ProductHunt)

**How to calculate market size without Statista:**
```
TAM = Total potential customers × Average revenue per customer
SAM = TAM × % of your segment
SOM = SAM × realistic market share (1-5% for startups)

Example:
- Total freelancers: 100M (Google search: "number of freelancers worldwide")
- Your segment: Designers (10% of freelancers) = 10M
- Your price: $10/month = $120/year
- TAM = 100M × $120 = $12B
- SAM = 10M × $120 = $1.2B
- SOM (2% market share) = $1.2B × 0.02 = $24M
```

✅ **No expensive subscriptions needed!**

---

## 🚨 Troubleshooting

### "Invalid API key" errors

**Check:**
1. Did you copy the full key? (No spaces, complete string)
2. Is the key in `.env` file? (Not `.env.example`)
3. Did you load environment variables? (Restart terminal/IDE)

**Test individual keys:**
```bash
# Test Anthropic
curl https://api.anthropic.com/v1/models \
  -H "x-api-key: $ANTHROPIC_API_KEY"

# Test Google
curl "https://www.googleapis.com/customsearch/v1?key=$GOOGLE_API_KEY&cx=$GOOGLE_CSE_ID&q=test"

# Test GitHub
curl -H "Authorization: token $GITHUB_TOKEN" \
  https://api.github.com/rate_limit
```

---

### "Quota exceeded" errors

**Google Custom Search:**
- You've hit 100 searches today
- Wait until midnight Pacific Time for reset
- OR upgrade to paid tier ($5/1,000 queries)
- OR use alternative (SerpAPI, Bing Search API)

**GitHub API:**
- You've hit 5,000 requests/hour
- Wait 1 hour for reset
- OR reduce requests (shouldn't happen normally)

---

### "FACT_VALIDATOR blocking workflow"

**This is intentional!** Quality score too low or critical issues found.

**Check the report:**
```bash
cat research_brief.json | jq '.fact_validation.flagged_hallucinations'
```

**Fix:**
1. Look at flagged issues
2. Add sources to claims
3. Re-run research
4. Quality gate will pass once sources added

---

## 📊 Understanding Costs

### What You'll Actually Pay

**Month 1 (10 research projects):**
| Item | Cost |
|------|------|
| Anthropic Claude | $10-30 |
| Google Custom Search | $0 (free tier) |
| GitHub API | $0 (free) |
| **Total** | **$10-30** |

**If you exceed free tiers:**
| Item | Cost |
|------|------|
| Anthropic Claude | $10-30 |
| Google (101-500 searches) | $2 |
| GitHub API | $0 (very unlikely to exceed) |
| **Total** | **$12-32** |

**Optional upgrades:**
- Statista Basic: +$39/month
- SerpAPI: +$50/month

**Recommendation:** Start with free tiers, upgrade only if needed.

---

## 🎓 Next Steps

1. ✅ **APIs configured** → Test research project
2. 📖 **Read documentation** → [README.md](README.md)
3. 🚀 **Run real research** → `python vibe-cli.py research --vision "Your idea"`
4. 📊 **Review output** → Check `research_brief.json`
5. 🔄 **Integrate with planning** → Pass to LEAN_CANVAS_VALIDATOR

---

## 🆘 Need Help?

- **Documentation:** [README.md](README.md)
- **Issues:** [GitHub Issues](https://github.com/your-org/vibe-research/issues)
- **Discussions:** [GitHub Discussions](https://github.com/your-org/vibe-research/discussions)

---

**You're ready to research! 🚀**
