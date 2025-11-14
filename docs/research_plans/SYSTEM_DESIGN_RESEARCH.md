# 🏗️ SYSTEM DESIGN RESEARCH - The HOW, not just the WHAT

**Problem:** V1 & V2 prompts only ask CONTENT questions ("What features does Rover have?")
**Missing:** SYSTEM DESIGN questions ("HOW do you build a scalable, extensible research system?")

---

## 🎯 The Questions I SHOULD Have Asked

### Meta-Question 1: HOW to Structure Curated Knowledge?

**What I asked:**
> "What features does Rover have?"

**What I SHOULD ask:**
> "How do successful knowledge systems structure their data?
> - Wikipedia's category system
> - Google's Knowledge Graph structure
> - OpenAI's structured outputs
> - Schema.org ontologies
> - Academic taxonomies (MeSH, ACM CCS, arXiv categories)"

**Why it matters:**
- YAML structure impacts searchability
- Relationships between concepts matter
- Extensibility depends on schema design
- Query patterns depend on data model

---

### Meta-Question 2: HOW to Make Knowledge ACTIONABLE?

**What I asked:**
> "What pricing does Stripe charge?"

**What I SHOULD ask:**
> "How do systems turn static knowledge into RECOMMENDATIONS?
> - Recommendation engines (collaborative filtering, content-based)
> - Expert systems (if-then rules, decision trees)
> - Case-based reasoning
> - Pattern matching algorithms
> - Similarity search (vector embeddings, keyword matching)"

**Why it matters:**
- Curated knowledge is useless if VIBE_ALIGNER can't USE it
- Need algorithms to match user intent → relevant patterns
- "Dog sitting app" → How to detect it's a marketplace?

---

### Meta-Question 3: HOW to Keep Knowledge FRESH?

**What I asked:**
> "What's Rover's current pricing?"

**What I SHOULD ask:**
> "How do systems maintain knowledge over time?
> - Wikipedia's edit history + talk pages
> - StackOverflow's voting + bounties
> - Google's crawling + indexing refresh rates
> - Version control for data (dbt, Pachyderm)
> - Staleness detection (last_updated fields, validation checks)"

**Why it matters:**
- Tech changes fast (frameworks, pricing, features)
- 6-month-old data can be wrong
- Need strategy for quarterly updates
- How to flag stale data?

---

### Meta-Question 4: HOW to Handle AMBIGUITY?

**What I asked:**
> "What features should a marketplace have?"

**What I SHOULD ask:**
> "How do systems handle ambiguous queries?
> - Search engines: Did you mean...?
> - LLMs: Clarifying questions
> - E-commerce: Faceted search + filters
> - Academic: Controlled vocabularies, synonyms
> - Multi-modal search (text + images + filters)"

**Why it matters:**
- User says "social app" → Is that Twitter, Discord, TikTok, dating app?
- Need disambiguation strategies
- How does VIBE_ALIGNER ask clarifying questions?

---

### Meta-Question 5: HOW to VALIDATE Knowledge?

**What I asked:**
> "What does Rover do?"

**What I SHOULD ask:**
> "How do knowledge systems ensure ACCURACY?
> - Wikipedia: Citations required, fact-checking
> - Academic: Peer review, retraction mechanisms
> - Google: E-E-A-T (Experience, Expertise, Authority, Trust)
> - Community voting (Reddit, StackOverflow)
> - Multi-source verification (cross-reference 3+ sources)"

**Why it matters:**
- Wrong data → Wrong recommendations → User builds wrong thing
- Need confidence levels (high/medium/low)
- How to handle conflicting sources?

---

### Meta-Question 6: HOW to Make it EXTENSIBLE?

**What I asked:**
> "What are the top 10 marketplaces?"

**What I SHOULD ask:**
> "How do systems allow COMMUNITY CONTRIBUTIONS?
> - Wikipedia's edit workflow
> - GitHub's PR model
> - StackOverflow's reputation system
> - Awesome Lists (community-curated)
> - Schema evolution (backward compatibility)"

**Why it matters:**
- Can't research ALL domains myself
- Need community to add new categories
- Schema must support future additions
- How to review/validate contributions?

---

## 🔬 SYSTEM DESIGN Research Prompt

### Gemini Deep Research Prompt:

```
RESEARCH OBJECTIVE:
Analyze successful knowledge systems and recommendation engines to identify HOW they structure data, keep it fresh, handle ambiguity, and turn static knowledge into actionable recommendations.

SYSTEMS TO ANALYZE:

1. KNOWLEDGE SYSTEMS:
   - Wikipedia (community knowledge, edit workflows, categories)
   - Google Knowledge Graph (structured data, entities, relationships)
   - Schema.org (semantic markup, ontologies)
   - OpenCyc (common sense reasoning)
   - Wikidata (structured Wikipedia data)

2. RECOMMENDATION SYSTEMS:
   - Amazon (product recommendations)
   - Netflix (content recommendations)
   - Spotify (music recommendations)
   - Google Search (query understanding, did you mean)
   - GitHub Copilot (code suggestions from context)

3. EXPERT SYSTEMS:
   - IBM Watson (question answering)
   - Medical diagnosis systems (UpToDate, Isabel)
   - Legal research (Westlaw, LexisNexis)
   - Tax software (TurboTax decision trees)

4. COMMUNITY CURATION:
   - StackOverflow (Q&A, voting, reputation)
   - Awesome Lists (GitHub community curation)
   - Product Hunt (product discovery, curation)
   - Reddit (voting, moderation)

SPECIFIC QUESTIONS:

1. DATA STRUCTURING:
   - How does Wikipedia organize categories? (hierarchies, tags, metadata)
   - How does Google Knowledge Graph model relationships? (entities, properties)
   - How does Schema.org define types? (inheritance, properties, enums)
   - Best practices for YAML/JSON knowledge bases?
   - Trade-offs: Deep hierarchies vs flat tags vs graph structures?

2. RECOMMENDATION ALGORITHMS:
   - How does Amazon recommend products? (collaborative filtering, content-based)
   - How does Spotify understand music taste? (audio features, listening history)
   - How does Google understand search intent? (query parsing, entity recognition)
   - Pattern matching: Keyword matching vs semantic similarity vs ML?
   - Cold start problem: What if user is new or query is novel?

3. KNOWLEDGE FRESHNESS:
   - How does Wikipedia detect outdated info? (edit history, talk pages)
   - How does Google keep search results fresh? (crawl frequency, QDF)
   - How do knowledge bases version data? (dbt, Pachyderm, Git for data)
   - Staleness detection: last_updated fields, validation checks, automated tests
   - Update strategies: Full refresh vs incremental updates?

4. HANDLING AMBIGUITY:
   - How does Google handle "apple"? (company vs fruit, context)
   - How does Amazon handle "laptop"? (price range, brand, specs filters)
   - Clarifying questions: When to ask vs when to assume?
   - Controlled vocabularies: MeSH, ACM CCS, Library of Congress
   - Synonyms & aliases: How to map "dog sitting" → "pet care" → "animal services"?

5. VALIDATION & ACCURACY:
   - How does Wikipedia ensure accuracy? (citation needed, fact-checking bots)
   - How does StackOverflow rank answers? (voting, accepted answer, reputation)
   - Multi-source verification: Cross-referencing, consensus algorithms
   - Confidence levels: How to represent certainty (high/medium/low)?
   - Conflict resolution: What if sources disagree?

6. EXTENSIBILITY & COMMUNITY:
   - How does Wikipedia handle new categories? (proposal, discussion, consensus)
   - How do Awesome Lists accept contributions? (PR process, review criteria)
   - Schema evolution: Adding new fields without breaking old queries?
   - Backward compatibility: Versioning strategies for knowledge bases?
   - Community incentives: Why do people contribute? (reputation, intrinsic motivation)

7. TECHNICAL IMPLEMENTATION:
   - Storage: SQL vs NoSQL vs graph databases vs YAML files?
   - Search: Elasticsearch, Algolia, vector databases (Pinecone, Weaviate)?
   - Caching: Redis for frequently accessed patterns?
   - APIs: REST vs GraphQL for querying knowledge?
   - Real-time updates: Webhooks, polling, manual refresh?

8. QUERY UNDERSTANDING:
   - Entity extraction: "build dog sitting app" → entities: [dog, sitting, app, marketplace]
   - Intent classification: Is this content? business? creative? scientific?
   - Contextual understanding: Previous messages, user history
   - Fuzzy matching: Typos, synonyms, related concepts
   - Query expansion: "dog sitting" → also search "pet care", "animal services"

9. CASE STUDIES - FAILURES:
   - What knowledge systems FAILED? Why?
   - Outdated data: Examples of systems with stale knowledge
   - Over-complexity: Systems too complex to maintain
   - Under-adoption: Why some systems didn't get community contributions
   - Schema problems: Inflexible schemas that couldn't evolve

10. BEST PRACTICES:
    - Start simple: Minimum viable schema
    - Validate early: Test with real queries
    - Version everything: Track changes, rollback capability
    - Community-first: Make contributing easy
    - Measure quality: Metrics for knowledge base health (coverage, freshness, accuracy)

SOURCES TO PRIORITIZE:
- Wikipedia documentation (MediaWiki, Wikidata)
- Google Research papers (Knowledge Graph, search algorithms)
- Recommendation system papers (collaborative filtering, content-based)
- Schema.org specifications
- StackOverflow blog (community curation)
- Awesome Lists contribution guidelines
- Data versioning tools (dbt docs, Pachyderm)
- Knowledge graph research (academic papers)

OUTPUT FORMAT:
1. Executive Summary
2. Data Structuring Best Practices
3. Recommendation Algorithm Patterns
4. Knowledge Freshness Strategies
5. Ambiguity Handling Techniques
6. Validation & Accuracy Methods
7. Extensibility & Community Patterns
8. Technical Implementation Benchmarks
9. Case Studies (Successes & Failures)
10. Actionable Recommendations for Our System
```

---

## 🎯 Why This Matters

**Without this research:**
- We build beautiful YAML files with great content
- But no clear algorithm to USE that content
- No strategy for keeping it fresh
- No way to handle ambiguity
- No community contribution model

**With this research:**
- We know HOW to structure data (not just WHAT data)
- We have algorithms to match user intent → patterns
- We have update strategies
- We can handle "social app" ambiguity
- We have a contribution model

---

## 🚨 Critical Realizations

**I focused on:**
- ✅ WHAT Rover does (features, pricing)
- ✅ WHAT Notion does (features, pricing)

**I ignored:**
- ❌ HOW Wikipedia structures categories
- ❌ HOW Amazon recommends products
- ❌ HOW Google handles ambiguity
- ❌ HOW StackOverflow validates knowledge
- ❌ HOW to build the SYSTEM

**This is a meta-level research gap.**

---

**Should I add this as "Domain 9: Meta - System Design"?**
**Or separate research track?**
