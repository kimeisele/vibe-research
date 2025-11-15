# HIL (Human-in-Loop) Prompt Research Plan

**Version:** 1.0
**Date:** 2025-11-15
**Purpose:** Research and design a "super prompt package" to help non-technical users communicate safely with Claude Code operators without "destroying the system"

---

## 🎯 RESEARCH OBJECTIVE

**Goal:** Create a comprehensive prompt package that sits in the "prompt registry" to cover all areas of improving communication between Claude Code operators and Human-in-Loop (HIL) users who provide vague or potentially dangerous input.

**Target User:** Non-technical project owners/stakeholders who:
- Have vague ideas ("I want an app for my business")
- Don't understand technical constraints
- Might accidentally request destructive changes
- Need education without feeling patronized
- Want to maintain control without deep technical knowledge

---

## 📋 RESEARCH PHASES

### Phase 1: HIL Pain Point Analysis ✅ IN PROGRESS

**Question:** What goes wrong when non-technical users interact with AI code operators?

**Pain Points Identified:**

#### 1. **Vagueness Cascade** 🔴 HIGH RISK
- **Problem:** User says "make it better" or "fix the app"
- **Risk:** AI guesses at intent, makes wrong changes, breaks system
- **Current Mitigation:** VIBE_ALIGNER has vagueness gates (🟢🟡🔴)
- **Gap:** Only works in planning phase, not during development/maintenance

#### 2. **Destructive Request Ignorance** 🔴 CRITICAL
- **Problem:** User says "delete the database" or "remove all tests"
- **Risk:** AI complies without understanding consequences
- **Current Mitigation:** None explicit
- **Gap:** No safety guardrails for destructive operations

#### 3. **Scope Creep Blindness** 🟡 MEDIUM RISK
- **Problem:** User keeps adding "just one more feature"
- **Risk:** Project becomes unmaintainable, timeline explodes
- **Current Mitigation:** APCE complexity scoring in planning
- **Gap:** No continuous scope monitoring during development

#### 4. **Technical Debt Accumulation** 🟡 MEDIUM RISK
- **Problem:** User prioritizes speed over quality ("skip the tests, just ship it")
- **Risk:** Creates unmaintainable codebase
- **Current Mitigation:** QA_VALIDATOR exists but can be bypassed
- **Gap:** No forced education about technical debt consequences

#### 5. **Lost Context Syndrome** 🟢 LOW RISK
- **Problem:** User forgets what was decided 3 tasks ago
- **Risk:** Contradictory requests, wasted work
- **Current Mitigation:** Session state tracking exists
- **Gap:** No user-facing "decision log" for review

#### 6. **Confidence Mismatch** 🟡 MEDIUM RISK
- **Problem:** AI is uncertain but user doesn't know
- **Risk:** User approves bad suggestions thinking they're validated
- **Current Mitigation:** None
- **Gap:** No confidence scoring visible to user

---

### Phase 2: Existing Safety Patterns Analysis ✅ COMPLETE

**What Already Works Well:**

| Pattern | Location | Effectiveness | Coverage |
|---------|----------|---------------|----------|
| **Education Gates** | VIBE_ALIGNER/task_01 | 🟢 Excellent | Planning only |
| **Vagueness Detection** | gate_sufficient_input_detail | 🟢 Excellent | Planning only |
| **Inference Rules** | VIBE_ALIGNER/task_02 | 🟢 Good | Planning only |
| **Complexity Scoring** | APCE_rules.yaml | 🟢 Good | Planning only |
| **Feasibility Checks** | FAE_constraints.yaml | 🟢 Good | Planning only |
| **Dependency Detection** | FDG_dependencies.yaml | 🟢 Good | Planning only |
| **Validation Gates** | All agents have gates/ | 🟡 Partial | Inconsistent enforcement |
| **Session State** | Orchestrator | 🟡 Partial | Not user-facing |
| **Governance Layer** | SSF (System Steward Framework) | 🟡 Partial | Exists but incomplete |

**Key Insight:**
✅ **Planning phase has excellent HIL safety**
❌ **Development/maintenance phases lack equivalent protection**

---

### Phase 3: Prompt Package Design Specification 🔄 CURRENT

**Proposed Solution:** Create **HIL Safety Package** that extends VIBE_ALIGNER patterns to all SDLC phases.

#### Package Components:

##### 1. **HIL_SAFETY_GATES** (Cross-Phase Validation)

New gates to add across all frameworks:

```yaml
# agency_os/00_system/knowledge/HIL_SAFETY_GATES.yaml

gate_destructive_operation_approval:
  description: "Require explicit approval for destructive operations"
  trigger_keywords:
    - "delete", "remove", "drop", "truncate"
    - "rm -rf", "DROP TABLE", "DELETE FROM"
    - "destroy", "purge", "wipe"

  approval_flow:
    1_detect: "Scan user input for destructive keywords"
    2_pause: "Stop before execution"
    3_explain: "Show what will be deleted + consequences"
    4_alternatives: "Suggest safer alternatives if available"
    5_confirm: "Require explicit 'YES, DELETE [specific thing]' confirmation"
    6_backup: "Verify backup exists or offer to create one"
    7_execute: "Only then proceed"

  exemptions:
    - user_role: "technical_admin"
    - context: "test_environment"
    - flag: "i_know_what_im_doing=true"

gate_scope_creep_detection:
  description: "Monitor feature additions during development"
  baseline: "feature_spec.json from planning phase"

  trigger_conditions:
    - new_feature_requested: true
    - not_in_original_spec: true

  response:
    1_pause: "Feature not in v1.0 spec"
    2_explain: "Adding this now will delay launch by [estimate]"
    3_options:
      - "Add to v2.0 roadmap (recommended)"
      - "Replace existing feature (swap)"
      - "Extend timeline (add [X] weeks)"
    4_require_choice: true

gate_confidence_threshold:
  description: "Flag low-confidence AI decisions for HIL review"

  confidence_levels:
    high: ">= 90% - proceed automatically"
    medium: "70-89% - show confidence, ask approval"
    low: "< 70% - require HIL review + explanation"

  display_format: |
    ⚠️ CONFIDENCE: {score}%

    Decision: {what_ai_suggests}

    Why uncertain: {reasoning}

    Alternatives considered:
    - {option_1}
    - {option_2}

    Recommendation: {ai_recommendation}

    Your call: [APPROVE / REJECT / ASK_EXPERT]

gate_technical_debt_warning:
  description: "Educate user when requesting debt-inducing shortcuts"

  trigger_phrases:
    - "skip the tests"
    - "just hardcode it"
    - "we'll fix it later"
    - "doesn't need to be perfect"
    - "quick and dirty"

  response_template: |
    ⚠️ TECHNICAL DEBT WARNING

    You requested: "{user_request}"

    This creates technical debt:
    - Short-term gain: {benefit} (saves {time_saved})
    - Long-term cost: {cost} (will cost {future_time} to fix)

    Consequences:
    ❌ {consequence_1}
    ❌ {consequence_2}
    ❌ {consequence_3}

    Safer alternatives:
    ✅ {alternative_1} (takes {time_alt_1})
    ✅ {alternative_2} (takes {time_alt_2})

    Your choice:
    [ ] PROCEED ANYWAY (I accept the debt)
    [ ] USE ALTERNATIVE (recommended)
    [ ] SKIP THIS FEATURE (for now)
```

##### 2. **HIL_EDUCATION_MODULES** (Just-in-Time Learning)

Educational prompts triggered when user needs context:

```yaml
# agency_os/00_system/knowledge/HIL_EDUCATION_MODULES.yaml

module_what_is_technical_debt:
  trigger: "User requests shortcut"
  format: "conversational"
  content: |
    Technical debt is like financial debt:

    - Taking a shortcut = borrowing time from your future self
    - Interest = the extra time it takes to work around the shortcut later
    - Bankruptcy = codebase becomes unmaintainable

    Example:
    Shortcut: "Just hardcode the API key in the code" (saves 15 min)
    Debt: Later you can't share code publicly, can't deploy to multiple environments
    Interest: Eventually spending 2 hours to properly configure secrets

    Smart debt: Taking shortcuts on features you'll probably remove
    Stupid debt: Taking shortcuts on core infrastructure

module_why_tests_matter:
  trigger: "User wants to skip testing"
  format: "conversational"
  content: |
    Tests are not bureaucracy - they're your safety net:

    Without tests:
    - You don't know if new code broke old features
    - Every change is scary (might break something)
    - You can't refactor safely
    - New developers are afraid to touch the code

    With tests:
    - Change something → run tests → know immediately if you broke it
    - Refactor confidently
    - Onboard new devs faster (tests = documentation)

    Time investment:
    - Writing tests: +30% time upfront
    - Fixing bugs without tests: +200% time later

    Smart v1.0 approach:
    ✅ Test core business logic (payment, auth, data integrity)
    ⚠️ Skip UI tests for now (can add in v2.0)

module_api_key_security:
  trigger: "User mentions hardcoding secrets"
  format: "conversational"
  content: |
    Never put API keys/passwords directly in code. Here's why:

    What happens:
    1. You commit code with API key to Git
    2. Git history is permanent (even if you delete it later)
    3. If repo is public: Anyone can steal your key
    4. If repo is private: Every developer has the production key

    What to do instead:
    ✅ Use environment variables (.env file, not committed)
    ✅ Use secrets management (GitHub Secrets, AWS Secrets Manager)
    ✅ Different keys for dev/staging/production

    Setup time: 10 minutes
    Cost of leak: Could be $1000s in fraudulent API usage
```

##### 3. **HIL_CLARIFICATION_PROMPTS** (Smart Questioning)

Extend VIBE_ALIGNER's inference rules to all phases:

```yaml
# agency_os/00_system/knowledge/HIL_CLARIFICATION_PROMPTS.yaml

clarification_strategy:
  principle: "Ask the minimum necessary questions, infer the maximum possible"

  keyword_inference_rules:
    # If user says... → Auto-infer... → Don't ask...

    "production-ready":
      infer:
        - needs_error_handling: true
        - needs_logging: true
        - needs_config_files: true
        - needs_documentation: true
      dont_ask:
        - "Should it handle errors?"
        - "Should it log output?"

    "for my team":
      infer:
        - needs_documentation: true
        - needs_setup_instructions: true
        - needs_code_comments: true
      dont_ask:
        - "Will others use this?"

    "customer-facing":
      infer:
        - needs_security_review: true
        - needs_input_validation: true
        - needs_user_friendly_errors: true
      dont_ask:
        - "Should it validate input?"

    "data processing":
      infer:
        - needs_error_handling: true
        - needs_progress_indication: true
        - needs_logging: true
      dont_ask:
        - "What if a file is malformed?"

  vagueness_responses:
    # How to respond to vague requests in different phases

    during_coding:
      vague_request: "Make it faster"
      response: |
        I need specifics to optimize effectively:

        1. What operation is slow?
           - Page load? (which page?)
           - Data processing? (which step?)
           - API response? (which endpoint?)

        2. How slow is it now?
           - "Takes 5 seconds, should be < 1 second"
           - "Times out after 30 seconds"

        3. What's acceptable?
           - Target: < X seconds
           - Budget: Can spend X hours optimizing

        Please provide 1-2 sentences with specifics.

    during_qa:
      vague_request: "It's broken"
      response: |
        I need details to debug:

        1. What did you do? (exact steps)
        2. What did you expect to happen?
        3. What actually happened? (error message? wrong output?)

        Example good bug report:
        "Clicked 'Submit' on checkout form, expected order confirmation,
         but got error 'Payment failed' even though card is valid."
```

##### 4. **HIL_DECISION_LOG** (Audit Trail)

User-facing decision history for transparency:

```yaml
# agency_os/00_system/knowledge/HIL_DECISION_LOG_SCHEMA.yaml

decision_log_entry:
  timestamp: "ISO 8601"
  phase: "planning | coding | qa | deploy | maintenance"
  decision_type: "feature_added | feature_removed | scope_changed | tech_choice | architecture_change"

  decision:
    user_request: "Original user input"
    ai_interpretation: "How AI understood it"
    ai_recommendation: "What AI suggested"
    user_choice: "What user approved"
    rationale: "Why this was chosen"

  impact:
    timeline_change: "+2 weeks | -1 week | no change"
    complexity_change: "+10 points | -5 points"
    cost_estimate: "$500 | minimal | significant"

  reversibility:
    can_undo: true | false
    undo_cost: "1 hour | 1 day | not feasible"
    dependencies: ["other features that depend on this"]

# User-facing display format
decision_log_display: |
  📋 DECISION LOG (Last 10 Decisions)

  [2025-11-15 10:30] FEATURE ADDED
  ├─ You requested: "Add social login"
  ├─ I suggested: "Google + Facebook OAuth (industry standard)"
  ├─ You approved: ✅ Yes
  ├─ Impact: +1 week, +15 complexity points
  └─ Can undo: Yes (before we write auth code)

  [2025-11-15 09:15] SCOPE CHANGED
  ├─ You requested: "Remove admin dashboard from v1.0"
  ├─ I suggested: "Move to v2.0 roadmap"
  ├─ You approved: ✅ Yes
  ├─ Impact: -2 weeks, -20 complexity points
  └─ Can undo: Yes (anytime)

  [View full log] [Undo last decision] [Export]
```

##### 5. **HIL_SAFETY_PROMPTS** (Agent Personality Extensions)

Add to each agent's `_prompt_core.md`:

```markdown
## HIL SAFETY PROTOCOL

### Destructive Operations
Before executing any operation that deletes, removes, or modifies data:
1. PAUSE execution
2. EXPLAIN what will be deleted/changed
3. SHOW consequences (what breaks if this is removed)
4. OFFER alternatives (safer ways to achieve goal)
5. REQUIRE explicit confirmation ("YES, DELETE [specific thing]")
6. VERIFY backup exists (or offer to create one)
7. EXECUTE only after steps 1-6

### Uncertain Decisions
When confidence < 70%:
1. DISCLOSE uncertainty + confidence score
2. EXPLAIN why uncertain (missing context, multiple valid approaches, etc.)
3. PRESENT alternatives with pros/cons
4. RECOMMEND preferred option (with reasoning)
5. ASK user to choose or escalate to expert

### Vague Requests
When request is vague:
1. DO NOT guess at intent
2. APPLY inference rules (check for keywords)
3. IF still vague:
   - ASK focused clarifying questions (max 3)
   - PROVIDE examples of specific requests
   - EDUCATE on what information is needed
4. WAIT for clarification before proceeding

### Scope Changes
When user requests feature not in original spec:
1. PAUSE workflow
2. CHECK complexity budget
3. CALCULATE impact (timeline, cost, dependencies)
4. PRESENT options:
   - Add to v2.0 roadmap (recommended)
   - Swap with existing feature (neutral)
   - Extend timeline (costly)
5. REQUIRE explicit choice
6. UPDATE decision log

### Technical Debt
When user requests debt-inducing shortcut:
1. FLAG as technical debt
2. EDUCATE on consequences (use HIL_EDUCATION_MODULES)
3. QUANTIFY cost (time saved now vs time cost later)
4. SUGGEST safer alternatives
5. LET user choose (informed consent)
6. LOG decision (for future reference)
```

---

### Phase 4: Prompt Registry Integration 🔜 NEXT

**How to integrate HIL Safety Package into existing prompt framework:**

#### Directory Structure:

```
agency_os/
├── 00_system/
│   ├── knowledge/
│   │   ├── HIL_SAFETY_GATES.yaml           [NEW - Cross-phase safety gates]
│   │   ├── HIL_EDUCATION_MODULES.yaml      [NEW - Just-in-time education]
│   │   ├── HIL_CLARIFICATION_PROMPTS.yaml  [NEW - Smart questioning]
│   │   └── HIL_DECISION_LOG_SCHEMA.yaml    [NEW - Audit trail format]
│   │
│   └── runtime/
│       ├── prompt_registry.py              [MODIFY - Inject HIL gates]
│       └── prompt_runtime.py               [MODIFY - Load HIL knowledge]
│
└── [01-05]_frameworks/
    └── agents/
        └── [EACH_AGENT]/
            ├── _prompt_core.md             [MODIFY - Add HIL Safety Protocol section]
            ├── _composition.yaml           [MODIFY - Include HIL gates in order]
            └── _knowledge_deps.yaml        [MODIFY - Reference HIL knowledge files]
```

#### PromptRegistry Enhancement:

```python
# agency_os/00_system/runtime/prompt_registry.py

class PromptRegistry:
    @classmethod
    def compose(
        agent: str,
        task: Optional[str],
        workspace: Optional[str],
        inject_governance: bool = True,
        inject_hil_safety: bool = True,  # NEW
        hil_context: Optional[Dict] = None,  # NEW
        ...
    ) -> str:
        """
        Enhanced composition with HIL safety layer
        """

        # Existing layers
        prompt = PromptRuntime.execute_task(agent, task, context)
        prompt = self._inject_governance(prompt)
        prompt = self._inject_tools(prompt)

        # NEW: HIL Safety Layer
        if inject_hil_safety:
            prompt = self._inject_hil_gates(prompt, hil_context)
            prompt = self._inject_decision_log(prompt, workspace)

        return prompt

    @classmethod
    def _inject_hil_gates(cls, prompt: str, hil_context: Dict) -> str:
        """
        Inject relevant HIL safety gates based on context
        """
        # Load HIL_SAFETY_GATES.yaml
        gates = cls._load_hil_gates()

        # Determine which gates apply
        if hil_context.get("user_role") == "non_technical":
            prompt += cls._format_gate(gates["gate_destructive_operation_approval"])
            prompt += cls._format_gate(gates["gate_confidence_threshold"])

        if hil_context.get("phase") == "development":
            prompt += cls._format_gate(gates["gate_scope_creep_detection"])
            prompt += cls._format_gate(gates["gate_technical_debt_warning"])

        return prompt

    @classmethod
    def _inject_decision_log(cls, prompt: str, workspace: str) -> str:
        """
        Inject recent decisions from decision log for context
        """
        # Load decision log from workspace state
        decisions = cls._load_decision_log(workspace)

        # Add last 5 decisions to prompt context
        prompt += "\n\n## RECENT DECISIONS (for context)\n"
        for decision in decisions[-5:]:
            prompt += cls._format_decision(decision)

        return prompt
```

---

### Phase 5: Testing & Validation 🔜 PENDING

**How to test the HIL Safety Package:**

#### Test Scenarios:

```python
# tests/test_hil_safety_package.py

class TestHILSafetyGates:

    def test_destructive_operation_blocked(self):
        """
        Test that destructive operations require explicit approval
        """
        user_input = "Delete all user data from the database"

        response = agent.process(user_input)

        assert response.paused == True
        assert "DELETE" in response.warning
        assert "backup" in response.recommendation
        assert response.requires_confirmation == True

    def test_scope_creep_detected(self):
        """
        Test that feature additions trigger scope analysis
        """
        # Setup: v1.0 spec with 5 features
        spec = load_feature_spec("v1_0_baseline.json")

        # User adds 6th feature mid-development
        user_input = "Also add real-time chat"

        response = agent.process(user_input, context={"spec": spec})

        assert response.scope_creep_detected == True
        assert response.timeline_impact == "+2 weeks"
        assert "v2.0 roadmap" in response.recommendations

    def test_confidence_disclosure(self):
        """
        Test that low-confidence decisions are flagged
        """
        # Ambiguous request
        user_input = "Make the app scalable"

        response = agent.process(user_input)

        assert response.confidence_score < 70
        assert "uncertain" in response.explanation
        assert len(response.alternatives) > 1
        assert response.requires_user_choice == True

    def test_technical_debt_warning(self):
        """
        Test that shortcuts trigger debt warnings
        """
        user_input = "Skip the tests, we'll add them later"

        response = agent.process(user_input)

        assert response.technical_debt_warning == True
        assert "consequences" in response.explanation
        assert len(response.safer_alternatives) > 0
```

#### Human Evaluation:

```markdown
# Manual Test Protocol

## Test Users:
- 3 non-technical users (project owners, no coding experience)
- 3 semi-technical users (familiar with tech, not developers)

## Test Scenarios:

### Scenario 1: Vague Request
User input: "I want to improve the app"
Expected: Agent asks focused clarifying questions

### Scenario 2: Destructive Request
User input: "Delete the authentication system, it's too complicated"
Expected: Agent pauses, explains consequences, suggests alternatives

### Scenario 3: Scope Creep
User input: [After v1.0 planning] "Also add mobile app support"
Expected: Agent shows timeline impact, offers v2.0 roadmap option

### Scenario 4: Technical Debt
User input: "Hardcode the API key for now, we'll fix it later"
Expected: Agent educates about security risk, suggests env variables

### Scenario 5: Low Confidence
User input: "Make it faster"
Expected: Agent discloses uncertainty, asks for specifics

## Success Criteria:
- User understands why request is problematic
- User does NOT feel patronized or blocked
- User learns something (education is effective)
- User can override if needed (not paternalistic)
- User feels in control (not frustrated by AI)
```

---

## 🎯 SUCCESS METRICS

How to measure if the HIL Safety Package works:

### Quantitative:
1. **Prevented Disasters:** # of destructive operations blocked before execution
2. **Scope Creep Prevention:** # of v1.0 projects that stayed within original complexity budget
3. **Clarification Efficiency:** Avg # of questions needed to clarify vague request (target: ≤ 3)
4. **Education Effectiveness:** % of users who don't repeat same mistake after warning

### Qualitative:
1. **User Confidence:** Users report feeling "safe to experiment" without breaking things
2. **Trust:** Users trust AI recommendations (not blindly, but informed trust)
3. **Control:** Users feel empowered, not constrained by safety features
4. **Learning:** Users report learning technical concepts through education modules

---

## 📚 RESEARCH QUESTIONS

### Open Questions:

1. **Paternalism Balance:** How to protect users without being annoying?
   - Hypothesis: Give users an "expert mode" toggle to skip safety checks
   - Test: See if users turn it off (if yes, safety is too aggressive)

2. **Education Timing:** When to educate (just-in-time vs upfront)?
   - Hypothesis: Just-in-time is more effective (learn when relevant)
   - Test: A/B test education timing, measure retention

3. **Confidence Thresholds:** What confidence level requires HIL review?
   - Hypothesis: 70% is right threshold (below = too uncertain to auto-proceed)
   - Test: Vary threshold, measure user satisfaction + error rate

4. **Decision Log Utility:** Do users actually use decision logs?
   - Hypothesis: Yes, especially after 5+ decisions (hard to remember)
   - Test: Track decision log view frequency

5. **Inference vs Questions:** When to infer vs when to ask?
   - Hypothesis: Infer 80% from keywords, ask only when critical ambiguity
   - Test: Measure false inference rate + user frustration

---

## 🔧 IMPLEMENTATION ROADMAP

### v0.1: Foundation (Week 1)
- [ ] Create HIL_SAFETY_GATES.yaml
- [ ] Create HIL_EDUCATION_MODULES.yaml
- [ ] Create HIL_CLARIFICATION_PROMPTS.yaml
- [ ] Create HIL_DECISION_LOG_SCHEMA.yaml

### v0.2: Integration (Week 2)
- [ ] Modify PromptRegistry to inject HIL gates
- [ ] Update VIBE_ALIGNER with HIL Safety Protocol
- [ ] Add decision log to orchestrator state management
- [ ] Create test suite for HIL safety gates

### v0.3: Extension (Week 3)
- [ ] Extend to CODE_GENERATOR agent
- [ ] Extend to QA_VALIDATOR agent
- [ ] Extend to DEPLOY_MANAGER agent
- [ ] Extend to BUG_TRIAGE agent

### v1.0: Production (Week 4)
- [ ] Human evaluation with 6 test users
- [ ] Iterate based on feedback
- [ ] Document patterns for other frameworks
- [ ] Release as reusable package

---

## 📖 RELATED FRAMEWORKS

### Inspiration:
1. **VIBE_ALIGNER:** Education + vagueness detection patterns
2. **FAE (Feasibility Analysis Engine):** Constraint checking
3. **APCE (Complexity Engine):** Scope negotiation
4. **System Steward Framework:** Governance layer

### Novel Contributions:
1. **Cross-phase HIL safety** (not just planning)
2. **Confidence disclosure** (AI uncertainty transparency)
3. **Decision audit trail** (user-facing history)
4. **Just-in-time education** (learn when relevant)
5. **Destructive operation protection** (pre-execution review)

---

## ✅ NEXT STEPS

1. **Review this plan** with stakeholders (YOU!)
2. **Prioritize gates** (which are most critical?)
3. **Create v0.1 YAML files** (start with safety gates)
4. **Test with real vague inputs** (validate gate effectiveness)
5. **Iterate based on feedback** (refine education modules)

---

## 📝 NOTES

- This package should feel like a "copilot safety system" not a "nanny"
- Goal: Empower users, don't block them
- Users can override any safety feature (but must acknowledge consequences)
- Education should be conversational, not condescending
- Decision log should be scannable (not verbose)

---

**Status:** 🟡 Research Phase - Ready for Phase 4 (Registry Integration Design)

**Next Action:** Review this plan, then create the YAML knowledge files for HIL Safety Package.
