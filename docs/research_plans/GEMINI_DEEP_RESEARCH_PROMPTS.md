# 🔬 Gemini Deep Research Prompts - Phase 1

**Purpose:** Build curated market intelligence for MARKET_PATTERNS.yaml and COMPETITOR_INTELLIGENCE.yaml
**Timeline:** Week 1 (5 initial categories, then expand to 20)
**Method:** Use Gemini Deep Research (1.5+ model) for comprehensive analysis

---

## 📋 Instructions for Running These Prompts

1. **Copy each prompt below into Gemini Deep Research**
2. **Let it run for 15-30 minutes** (it will search 100+ sources)
3. **Export results as Markdown** (or copy full output)
4. **I'll process into YAML format**

**Important:** Run ALL 5 prompts in parallel if possible - each is independent.

---

## 🎯 Category 1: Two-Sided Marketplaces (Local Services)

### Gemini Deep Research Prompt:

```
RESEARCH OBJECTIVE:
Analyze successful two-sided marketplaces for local services (Rover, TaskRabbit, Thumbtack, Care.com, Handy) to identify common patterns, critical features, pricing strategies, and technical architecture decisions.

SPECIFIC QUESTIONS TO ANSWER:

1. MARKET LEADERS ANALYSIS:
   - Identify the top 10 marketplaces in this category (dog sitting, home cleaning, handyman, caregiving, etc.)
   - For EACH marketplace, find:
     * Founded year
     * Total funding raised (Crunchbase data)
     * Current GMV or revenue (if public)
     * Number of service providers on platform
     * Geographic presence
     * Business model (commission %, booking fees, subscriptions)

2. FEATURE ANALYSIS - V1.0 vs V2.0+:
   For Rover, TaskRabbit, and Care.com specifically:
   - What features did they launch with? (V1.0)
   - What features did they add later? (V2.0+)
   - Timeline: when were key features like GPS tracking, insurance, background checks added?
   - Find blog posts, press releases, or Wayback Machine screenshots showing feature evolution

3. TRUST & SAFETY PATTERNS:
   - What trust & safety features do 80%+ of these marketplaces have?
   - Background check providers (Checkr, Onfido, etc.)
   - Insurance coverage (who provides? typical coverage amounts?)
   - Verification processes (ID, phone, email, social)
   - Review systems (rating scales, verification, moderation)

4. PRICING PATTERNS:
   - Commission rates: What % do marketplaces charge? (15%? 20%? 25%?)
   - Booking fees: Fixed fees per transaction?
   - Subscription models: Any marketplaces with monthly subscriptions?
   - Payment splits: How are marketplace fees structured?

5. TECHNICAL STACK (Inferred from job postings, tech blogs, BuiltWith):
   - Backend frameworks (Rails, Node, Django?)
   - Databases (PostgreSQL, MongoDB?)
   - Payment processors (Stripe Connect, Braintree?)
   - Communication (Twilio, SendGrid?)
   - Background checks API (Checkr?)
   - Hosting (AWS, GCP, Heroku?)

6. COMMON PITFALLS & LESSONS LEARNED:
   - Find postmortems, founder interviews, case studies
   - What mistakes did early marketplaces make?
   - What features were "table stakes" vs "nice to have"?
   - Any marketplaces that failed? Why?

7. MVP DEFINITION:
   - What's the absolute minimum feature set to launch a local services marketplace?
   - What can be deferred to V2.0 without harming user experience?

SOURCES TO PRIORITIZE:
- Crunchbase (funding, founding dates)
- TechCrunch, The Information (deep dives)
- Company blogs (Rover blog, TaskRabbit blog)
- Wayback Machine (historical feature analysis)
- Job postings (tech stack clues)
- User reviews (Reddit, TrustPilot - common pain points)
- SEC filings (if public companies)

OUTPUT FORMAT:
Please structure your findings as:
1. Executive Summary (key insights, patterns)
2. Company Profiles (10 marketplaces)
3. Feature Evolution Timeline (V1.0 → V2.0 for top 3)
4. Trust & Safety Standards (industry norms)
5. Pricing Benchmarks (commission rates, fees)
6. Tech Stack Patterns (common choices)
7. Lessons Learned (mistakes to avoid)
8. MVP Recommendations (must-have vs nice-to-have)
```

---

## 🎯 Category 2: SaaS - Productivity & Collaboration Tools

### Gemini Deep Research Prompt:

```
RESEARCH OBJECTIVE:
Analyze successful SaaS productivity and collaboration tools (Notion, Slack, Linear, Airtable, Figma, Monday.com) to identify critical features, pricing tiers, onboarding strategies, and technical architecture patterns.

SPECIFIC QUESTIONS TO ANSWER:

1. MARKET LEADERS ANALYSIS:
   - Top 10 SaaS tools in productivity/collaboration
   - For EACH:
     * Founded year
     * Funding raised
     * ARR (Annual Recurring Revenue) if disclosed
     * Number of users/teams
     * Key differentiators
     * Target market (startups, SMB, enterprise?)

2. FEATURE ANALYSIS - MVP vs GROWTH:
   For Notion, Slack, and Linear specifically:
   - What was their MVP? (First version features)
   - What features drove explosive growth?
   - Timeline: when did they add integrations, API, mobile apps, etc?
   - Find early screenshots (Product Hunt, Wayback Machine)

3. PRICING STRATEGY PATTERNS:
   - Free tier: What's included? What's limited? (seats, storage, features)
   - Paid tiers: How many tiers? Typical price points?
   - Per-seat vs usage-based vs flat-rate pricing?
   - When do companies add enterprise tier?
   - Self-serve vs sales-assisted motion?

4. ONBOARDING & ACTIVATION:
   - How do successful SaaS tools onboard users?
   - Time to value: How quickly can user see benefit?
   - Aha moments: What's the hook that gets users to stick?
   - Templates, pre-filled data, or blank canvas?

5. TECHNICAL STACK (from job postings, tech blogs, StackShare):
   - Frontend: React, Vue, Svelte?
   - Backend: Node, Python, Go, Elixir?
   - Database: PostgreSQL, MongoDB, CockroachDB?
   - Real-time: WebSockets, Pusher, Ably?
   - Auth: Auth0, Firebase, custom?
   - Hosting: Vercel, AWS, GCP?

6. FREEMIUM → PAID CONVERSION:
   - What features are gated behind paid plans?
   - Common upgrade triggers (team size, storage, advanced features)
   - Typical conversion rates (if disclosed)

7. PRODUCT-LED GROWTH TACTICS:
   - Viral loops: How do users invite others?
   - Network effects: What creates lock-in?
   - Integrations: Which integrations drive adoption?

8. COMMON MISTAKES:
   - Feature bloat: Tools that added too much too fast
   - Pricing mistakes: Companies that changed pricing and faced backlash
   - Technical debt: Migration stories, rewrites

SOURCES TO PRIORITIZE:
- Company blogs (Notion, Slack, Linear engineering blogs)
- Product Hunt (early versions)
- Wayback Machine (pricing page evolution)
- Pricing pages (current state)
- OpenSaaS.com (pricing comparisons)
- SaaS metrics blogs (ChartMogul, Baremetrics)
- Tech blogs (InfoQ, HackerNoon - architecture decisions)

OUTPUT FORMAT:
1. Executive Summary
2. Company Profiles (10 SaaS tools)
3. MVP → Growth Features Timeline
4. Pricing Tier Patterns
5. Onboarding Best Practices
6. Tech Stack Patterns
7. Freemium Strategies
8. Lessons Learned
```

---

## 🎯 Category 3: E-Commerce (D2C Brands)

### Gemini Deep Research Prompt:

```
RESEARCH OBJECTIVE:
Analyze successful direct-to-consumer (D2C) e-commerce brands (Warby Parker, Allbirds, Glossier, Casper, Away) to identify critical features, supply chain patterns, customer acquisition strategies, and technical infrastructure.

SPECIFIC QUESTIONS TO ANSWER:

1. MARKET LEADERS ANALYSIS:
   - Top 10 D2C brands (various verticals: fashion, CPG, home goods)
   - For EACH:
     * Founded year
     * Funding / valuation
     * Revenue (if public)
     * Key differentiator (DTC approach, sustainability, quality)
     * Channel mix (own site, Amazon, retail?)

2. E-COMMERCE PLATFORM CHOICES:
   - Shopify vs custom builds: Who uses what?
   - When do brands outgrow Shopify?
   - Headless commerce: Who's using it?
   - Platform costs: Shopify tiers, payment processing fees

3. MUST-HAVE FEATURES (V1.0):
   - Core e-commerce: product pages, cart, checkout
   - Customer accounts: Login, order history, saved items
   - Inventory management: How is it handled at early stage?
   - Fulfillment: In-house, 3PL, dropshipping?
   - Returns/exchanges: Policies and implementation

4. CUSTOMER ACQUISITION:
   - Primary channels: Paid social, influencers, content, SEO?
   - CAC (Customer Acquisition Cost): Industry benchmarks
   - LTV (Lifetime Value): Repeat purchase rates
   - Referral programs: How do brands incentivize word-of-mouth?

5. TECHNICAL STACK:
   - E-commerce platform (Shopify, BigCommerce, custom)
   - Payment gateway (Stripe, PayPal, Adyen)
   - Email/SMS (Klaviyo, Attentive, Sendlane)
   - Analytics (Segment, Google Analytics, Mixpanel)
   - A/B testing (Optimizely, VWO)
   - Reviews (Yotpo, Bazaarvoice, Trustpilot)

6. SUBSCRIPTION MODELS:
   - Which D2C brands offer subscriptions?
   - Subscription vs one-time purchase: conversion rates?
   - Churn rates: How do brands retain subscribers?
   - Platforms: ReCharge, Bold, custom?

7. SUPPLY CHAIN & FULFILLMENT:
   - Manufacturing: Overseas, domestic, hybrid?
   - 3PL partners: ShipBob, Flexport, in-house?
   - Inventory risk: How do brands manage pre-orders, backorders?

8. COMMON PITFALLS:
   - Inventory: Overstocking, understocking nightmares
   - Fulfillment: Scaling issues during growth
   - Payment fraud: Chargeback management
   - Returns: Reverse logistics complexity

SOURCES TO PRIORITIZE:
- Built With (tech stack detection)
- eCommerce Fuel, Shopify blogs
- D2C Twitter accounts (founders sharing lessons)
- Podcast interviews (How I Built This, eCommerce Influence)
- Reddit r/ecommerce (pain points)
- SEC filings (for public companies like Warby Parker)

OUTPUT FORMAT:
1. Executive Summary
2. Brand Profiles (10 D2C brands)
3. Platform Choice Patterns
4. Must-Have Features (MVP)
5. Customer Acquisition Playbook
6. Tech Stack Patterns
7. Subscription Models
8. Lessons Learned
```

---

## 🎯 Category 4: Developer Tools (CLI/API Platforms)

### Gemini Deep Research Prompt:

```
RESEARCH OBJECTIVE:
Analyze successful developer tool platforms (Stripe, Vercel, Supabase, Render, Railway, Clerk, Neon) to identify critical features, pricing strategies, developer experience patterns, and technical architecture.

SPECIFIC QUESTIONS TO ANSWER:

1. MARKET LEADERS ANALYSIS:
   - Top 10 developer tool platforms (payments, hosting, auth, databases)
   - For EACH:
     * Founded year
     * Funding / valuation
     * Number of developers using platform
     * Key differentiator (DX, pricing, features)
     * Open-source vs proprietary

2. DEVELOPER EXPERIENCE (DX) PATTERNS:
   - Onboarding: Time from signup to first API call?
   - Documentation: Structure, examples, SDKs
   - CLI tools: What makes a great developer CLI?
   - Dashboard: Developer portal features
   - Testing: Sandbox environments, test API keys

3. PRICING MODELS:
   - Free tier: What's included? What limits?
   - Usage-based: Per API call, per GB, per user?
   - Flat-rate tiers: When do companies offer them?
   - Enterprise: Custom pricing, dedicated support?
   - Typical price points: Stripe (2.9% + 30¢), Vercel ($20/user), etc.

4. MVP FEATURES (What did they launch with?):
   For Stripe, Vercel, Supabase:
   - Initial feature set (v1.0)
   - Growth features (what drove adoption?)
   - Timeline: API versioning, new endpoints, platform expansion

5. TECHNICAL ARCHITECTURE:
   - API design: REST, GraphQL, webhooks?
   - SDKs: Which languages supported first?
   - Infrastructure: AWS, GCP, multi-cloud?
   - Rate limiting: How is it implemented?
   - Authentication: API keys, OAuth, JWT?

6. GO-TO-MARKET STRATEGY:
   - Developer evangelism: Content, conferences, sponsorships
   - Community: Discord, forums, GitHub discussions
   - Self-serve: How easy is it to start without talking to sales?
   - Open-source strategy: OSS as marketing?

7. INTEGRATION ECOSYSTEM:
   - Which integrations are table stakes? (Slack, GitHub, Vercel, etc.)
   - Marketplace: Do they have integration marketplaces?
   - Webhooks: How are they implemented?

8. COMMON MISTAKES:
   - API breaking changes (migration nightmares)
   - Pricing changes (developer backlash)
   - Over-complexity (too many features, bad DX)
   - Under-documentation

SOURCES TO PRIORITIZE:
- Official docs (Stripe, Vercel, Supabase docs)
- Engineering blogs (high-quality technical content)
- GitHub repos (open-source projects)
- HackerNews (developer sentiment)
- Developer surveys (Stack Overflow, State of JS)
- Pricing pages (current state + Wayback Machine)
- ProductHunt (early versions)

OUTPUT FORMAT:
1. Executive Summary
2. Platform Profiles (10 developer tools)
3. DX Best Practices
4. Pricing Model Patterns
5. MVP Feature Set
6. Tech Architecture Patterns
7. GTM Playbook
8. Lessons Learned
```

---

## 🎯 Category 5: Booking & Scheduling Systems

### Gemini Deep Research Prompt:

```
RESEARCH OBJECTIVE:
Analyze successful booking and scheduling platforms (Calendly, Cal.com, Acuity, TidyCal, SavvyCal) to identify critical features, pricing strategies, integration patterns, and technical implementation.

SPECIFIC QUESTIONS TO ANSWER:

1. MARKET LEADERS ANALYSIS:
   - Top 10 scheduling/booking tools
   - For EACH:
     * Founded year
     * Funding / revenue
     * Number of users
     * Key differentiator (features, pricing, UX)
     * Open-source vs proprietary (Cal.com is OSS!)

2. FEATURE ANALYSIS - CORE vs PREMIUM:
   - Core features (all tools have): Calendar sync, availability rules, booking links
   - Premium features (upsell opportunities): Team scheduling, payments, workflows
   - V1.0 MVP: What's the absolute minimum to launch?

3. CALENDAR INTEGRATION PATTERNS:
   - Which calendars integrate: Google, Outlook, Apple, other?
   - Sync method: CalDAV, OAuth, webhooks?
   - Conflict detection: How is availability calculated?
   - Time zone handling: Best practices

4. PRICING STRATEGIES:
   - Free tier: Limits? (meetings per month, features, branding)
   - Paid tiers: Price points? ($8-15/mo seems standard)
   - Team pricing: Per-seat or flat-rate?
   - Add-ons: Payments, SMS reminders, custom domains

5. TECHNICAL IMPLEMENTATION:
   - Frontend: React, Vue, plain JS?
   - Backend: Node, Python, Go?
   - Database: How are availability rules stored?
   - Real-time: WebSockets for live availability?
   - Calendar APIs: Google Calendar API, Microsoft Graph

6. USER FLOW PATTERNS:
   - Booking flow: Steps from link click to confirmed booking
   - Email confirmations: What info is included?
   - Reminders: When are they sent? (24h before, 1h before?)
   - Cancellations/rescheduling: How is it handled?

7. INTEGRATION ECOSYSTEM:
   - Common integrations: Zoom, Google Meet, Stripe, Zapier
   - Webhooks: What events trigger webhooks?
   - Embed options: iFrame, JavaScript widget, API

8. DIFFERENTIATION STRATEGIES:
   How do tools differentiate in a crowded market?
   - Calendly: Enterprise features, workflows
   - Cal.com: Open-source, white-label
   - SavvyCal: Recipient-first UX (let them pick time)
   - TidyCal: One-time payment (no subscription)

9. COMMON PITFALLS:
   - Time zone bugs (notorious complexity)
   - Calendar sync delays (not truly real-time)
   - Spam bookings (no verification)
   - Over-complication (too many features)

SOURCES TO PRIORITIZE:
- Product comparison sites (G2, Capterra)
- User reviews (Reddit, Twitter complaints)
- Pricing pages (current + historical)
- Cal.com GitHub repo (open-source insights)
- Engineering blogs (if available)
- HackerNews threads (developer opinions)

OUTPUT FORMAT:
1. Executive Summary
2. Platform Profiles (10 tools)
3. Core vs Premium Features
4. Calendar Integration Patterns
5. Pricing Tier Strategies
6. Technical Implementation Guide
7. Differentiation Playbook
8. Lessons Learned
```

---

## 📊 Summary of 5 Categories

| Category | Archetype Examples | Key Insights We Need |
|----------|-------------------|---------------------|
| **1. Two-Sided Marketplaces** | Rover, TaskRabbit, Thumbtack | Trust & safety features, commission rates, V1.0 features |
| **2. SaaS (Productivity)** | Notion, Slack, Linear | Freemium models, onboarding, real-time collab patterns |
| **3. E-Commerce (D2C)** | Warby Parker, Allbirds | Shopify vs custom, fulfillment, customer acquisition |
| **4. Developer Tools** | Stripe, Vercel, Supabase | DX patterns, pricing models, API design |
| **5. Booking/Scheduling** | Calendly, Cal.com | Calendar sync, availability logic, pricing tiers |

---

## 🎯 Next Steps After Running These Prompts

1. **Export all 5 Gemini Deep Research results**
2. **I'll process them into:**
   - `MARKET_PATTERNS.yaml` (common patterns per category)
   - `COMPETITOR_INTELLIGENCE.yaml` (deep dives on 50 companies)
   - `TECH_ECOSYSTEM_MAP.yaml` (integrations, pricing)

3. **Estimated processing time:** 8-12 hours after receiving research results

---

## 🚀 BONUS: Additional Strategic Research Questions

If you want to go DEEPER (optional, but valuable):

### 🔬 Meta-Analysis Prompt

```
RESEARCH OBJECTIVE:
Analyze patterns across ALL successful startups (YC companies, Unicorns, IPOs from 2010-2024) to identify:

1. FEATURE VELOCITY:
   - How fast do successful companies ship features? (releases per month)
   - V1.0 → Product-Market Fit: typical timeline?
   - Feature bloat: when do companies add too much?

2. TECHNICAL DEBT PATTERNS:
   - When do companies rewrite? (scale triggers)
   - Monolith → microservices: typical timeline?
   - Tech stack changes: when and why?

3. PRICING EVOLUTION:
   - How often do companies change pricing?
   - Freemium → paid-only: success stories?
   - Price increases: how do users react?

4. COMMON FAILURE MODES:
   - Product: wrong features, bad UX, no PMF
   - Technical: scaling issues, security breaches
   - Business: bad unit economics, high CAC, low LTV

5. TIME TO METRICS:
   - First 100 users: typical timeline?
   - First $1M ARR: benchmarks by category?
   - Series A metrics: what do VCs look for?

SOURCES:
- YC Library (startup advice)
- First Round Review (in-depth case studies)
- Sequoia Arc (growth playbooks)
- SaaStr (SaaS benchmarks)
- Crunchbase (funding data)
- SEC filings (public companies)
```

---

**Ready to run?** Let me know when you have the results and I'll start processing! 🚀
