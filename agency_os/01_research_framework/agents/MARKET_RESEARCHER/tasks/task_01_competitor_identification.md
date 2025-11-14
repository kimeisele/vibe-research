# Task 01: Competitor Identification

**Task ID:** task_01_competitor_identification
**Dependencies:** None (first task)
**Output:** competitor_list.json

---

## Objective

Identify and research 3-5 major competitors in the target market. Include both **direct competitors** (same solution approach) and **indirect competitors** (alternative solutions to the same problem).

---

## Instructions

### Step 1: Analyze User Vision
Review the user's project vision to understand:
- What problem are they solving?
- Who is the target audience?
- What type of solution are they building? (web app, mobile app, SaaS, etc.)

### Step 2: Identify Competitor Categories

Research competitors in these categories:

1. **Direct Competitors:** Companies offering very similar solutions
   - Example: If building a project management tool, look for other project management SaaS

2. **Indirect Competitors:** Companies solving the same problem differently
   - Example: For project management, might include spreadsheets, email-based workflows, or all-in-one productivity suites

3. **Aspirational Competitors:** Larger players the product might compete with eventually
   - Example: Microsoft Project, Jira, Monday.com

### Step 3: Research Each Competitor

For each competitor, gather:
- **Name:** Official company name
- **Positioning:** How do they describe themselves? (from their homepage or About page)
- **Pricing:** Pricing model overview (detailed pricing comes in Task 2)
- **Source:** URL to their main website or product page

### Step 4: Verify Sources

Every competitor must have:
- A working URL (test the link)
- An official source (company website, not blog posts or reviews)
- Recent information (check if company is still active)

---

## Output Format

Generate `competitor_list.json`:

```json
{
  "competitors": [
    {
      "name": "Competitor Name",
      "category": "direct|indirect|aspirational",
      "positioning": "Short description of how they position themselves",
      "pricing_model": "subscription|one-time|freemium|usage-based|custom",
      "target_market": "enterprise|smb|individual|all",
      "source": "https://competitor.com"
    }
  ],
  "research_notes": {
    "market_category": "What category/industry is this?",
    "search_keywords_used": ["keyword1", "keyword2"],
    "competitors_found": 5,
    "research_date": "2025-11-14"
  }
}
```

---

## Quality Checklist

Before completing this task, verify:
- [ ] At least 3 competitors identified (5+ preferred)
- [ ] Mix of direct and indirect competitors included
- [ ] Every competitor has a valid source URL
- [ ] Positioning descriptions are based on official sources, not assumptions
- [ ] All URLs are tested and working
- [ ] No generic competitors listed without specific product names

---

## Example Output

```json
{
  "competitors": [
    {
      "name": "Asana",
      "category": "direct",
      "positioning": "Work management platform for teams to organize and execute work",
      "pricing_model": "freemium",
      "target_market": "smb",
      "source": "https://asana.com"
    },
    {
      "name": "Monday.com",
      "category": "direct",
      "positioning": "Work OS that powers teams to run projects and workflows",
      "pricing_model": "subscription",
      "target_market": "all",
      "source": "https://monday.com"
    },
    {
      "name": "Notion",
      "category": "indirect",
      "positioning": "All-in-one workspace for notes, docs, wikis, and project management",
      "pricing_model": "freemium",
      "target_market": "all",
      "source": "https://notion.so"
    }
  ],
  "research_notes": {
    "market_category": "Project Management & Collaboration Software",
    "search_keywords_used": ["project management software", "team collaboration tools", "work management platform"],
    "competitors_found": 3,
    "research_date": "2025-11-14"
  }
}
```

---

## Common Pitfalls

❌ **Too narrow:** "There are no competitors" → There are ALWAYS alternatives
❌ **Too broad:** Listing every project management tool ever created
❌ **No sources:** Competitor names without URLs
❌ **Outdated info:** Listing defunct companies or abandoned products
❌ **Generic descriptions:** "They make software" instead of specific positioning

---

## Next Task

Once complete, proceed to **Task 02: Pricing Analysis** to gather detailed pricing data for these competitors.
