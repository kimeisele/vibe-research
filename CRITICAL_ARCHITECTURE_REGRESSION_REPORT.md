# 🚨 CRITICAL ARCHITECTURE REGRESSION REPORT
**Report ID:** REGRESSION-001
**Severity:** 🔴 CRITICAL
**Date:** 2025-11-14
**Discovered By:** Claude Code (Sonnet 4.5) during GTD-001 preparation

---

## 🎯 EXECUTIVE SUMMARY

**CRITICAL FINDING:** The vibe-agency framework has undergone a **MASSIVE architectural regression** that fundamentally contradicts its original design.

**Original Design:** Interactive conversational agent system operated by **Claude Code** (CLI Agent)
**Current Implementation:** Batch LLM API processing system with Python scripts

**Impact:**
- ❌ Lost interactive capabilities
- ❌ 10-20x cost increase (Sonnet API calls instead of Claude Code operation)
- ❌ Eliminated human-in-the-loop at critical decision points
- ❌ Broke the prompt routing system design

---

## 📋 THE ORIGINAL DESIGN (Correct)

### Architecture Intent

The framework was designed as a **PROMPT ROUTING SYSTEM FOR CLAUDE CODE**:

```
┌─────────────────────────────────────────────────────────┐
│ ORCHESTRATOR (Python)                                   │
│ - Manages state machine                                 │
│ - Composes prompts from fragments                       │
│ - Routes tasks to Claude Code                           │
└──────────────┬──────────────────────────────────────────┘
               │
               │ Composed Mega-Prompt
               ▼
┌─────────────────────────────────────────────────────────┐
│ CLAUDE CODE (Interactive CLI Agent)                     │
│ - Receives composed prompt                              │
│ - "You are VIBE_ALIGNER..."                             │
│ - Loads knowledge bases (FAE, FDG, APCE)                │
│ - Executes INTERACTIVE dialog with user                 │
│ - Returns structured output (JSON)                      │
└──────────────┬──────────────────────────────────────────┘
               │
               │ Result (feature_spec.json)
               ▼
┌─────────────────────────────────────────────────────────┐
│ ORCHESTRATOR                                            │
│ - Saves artifact                                        │
│ - Transitions to next task/phase                        │
└─────────────────────────────────────────────────────────┘
```

### Evidence from Original Design

**File:** `agency_os/01_planning_framework/agents/VIBE_ALIGNER/_prompt_core.md`

```markdown
## SYSTEM OVERVIEW

You are **VIBE_ALIGNER**, a Senior Product Manager & Software Architect AI agent.
You are invoked by the `AGENCY_OS_ORCHESTRATOR` to guide users from vague ideas
to concrete, validated feature specifications.
```

**Key Indicators:**
- ✅ Written in 2nd person ("You are...")
- ✅ Instructions to "STOP and request" files
- ✅ Interactive dialog templates for user conversation
- ✅ Prompt composition system (`_composition.yaml`)
- ✅ Sequential task workflow (6 tasks for VIBE_ALIGNER)

**File:** `agency_os/01_planning_framework/agents/VIBE_ALIGNER/_composition.yaml`

```yaml
composition_order:
  - source: _prompt_core.md
    description: "Core personality, identity, and responsibilities"

  - source: ${knowledge_files}
    description: "FAE, FDG, APCE YAML knowledge bases"

  - source: ${task_prompt}
    path_pattern: tasks/${task_id}.md
    description: "Specific task instructions"

  - source: ${runtime_context}
    description: "Session state, artifacts from previous tasks"
```

**Interpretation:** This is a **PROMPT ASSEMBLY SPECIFICATION** for composing mega-prompts to give to Claude Code.

### How VIBE_ALIGNER Should Work

**Task 05: Scope Negotiation Example**

1. **Orchestrator composes prompt:**
   - `_prompt_core.md` → "You are VIBE_ALIGNER, a Senior PM..."
   - `APCE_rules.yaml` → Complexity scoring rules
   - `task_05_scope_negotiation.md` → "Calculate complexity, trigger negotiation if..."
   - `features_with_dependencies.json` → Input from Task 04

2. **Orchestrator invokes Claude Code** (the human user is using Claude Code in terminal)

3. **Claude Code reads the composed prompt and executes:**
   ```
   📊 SCOPE ANALYSIS

   Thank you for the detailed vision! I've analyzed your 15 feature requests.

   **Complexity Assessment:**
   - Total complexity: 87 points
   - Recommended v1.0 max: 50-60 points
   - Current overage: 37 points

   To ensure a successful v1.0 launch, I recommend focusing on the core features.

   **MUST HAVE (v1.0 Core)** - 8 features:
   - User Authentication (complexity: 8)
   - Dashboard (complexity: 5)
   ...

   **WON'T HAVE (Planned for v2.0)** - 7 features:
   - Social features (complexity: 13) - adds complexity spike
   - Barcode scanning (complexity: 10) - hardware integration risk
   ...

   Do you accept this v1.0 scope?
   ```

4. **User responds interactively:** "Yes, agreed" or "Can we include X?"

5. **Claude Code negotiates, validates, finalizes**

6. **Claude Code outputs:** `negotiated_features.json`

7. **Orchestrator saves artifact and moves to Task 06**

**THIS IS AN INTERACTIVE, CONVERSATIONAL, HUMAN-IN-THE-LOOP SYSTEM.**

---

## ❌ THE REGRESSION (What We Built)

### Current Implementation

**File:** `agency_os/00_system/orchestrator/core_orchestrator.py`

```python
def execute_agent(
    self,
    agent_name: str,
    task_id: str,
    inputs: Dict[str, Any],
    manifest: ProjectManifest
) -> Dict[str, Any]:
    """
    Execute agent by composing prompt and invoking LLM.
    """
    # 1. Compose prompt
    prompt = self.prompt_runtime.execute_task(agent_name, task_id, inputs)

    # 2. Invoke LLM via API
    response = self.llm_client.invoke(
        prompt=prompt,
        model="claude-3-5-sonnet-20241022",  # ← API CALL!
        max_tokens=4096
    )

    # 3. Parse JSON output
    return json.loads(response.content)
```

**What This Does:**
1. Composes prompt (correct ✅)
2. Makes **LLM API call** to Anthropic (❌ WRONG!)
3. Expects single-shot JSON response (❌ NO INTERACTION!)
4. Returns to Python (❌ NO USER DIALOG!)

**Architecture:**

```
┌─────────────────────────────────────────────────────────┐
│ ORCHESTRATOR (Python)                                   │
│ - Composes prompt                                       │
└──────────────┬──────────────────────────────────────────┘
               │
               │ API Call (prompt)
               ▼
┌─────────────────────────────────────────────────────────┐
│ ANTHROPIC API (Remote LLM)                              │
│ - Receives prompt                                       │
│ - Generates response (single-shot)                      │
│ - NO user interaction                                   │
│ - Returns JSON                                          │
└──────────────┬──────────────────────────────────────────┘
               │
               │ Response (JSON)
               ▼
┌─────────────────────────────────────────────────────────┐
│ ORCHESTRATOR                                            │
│ - Parses JSON                                           │
│ - Saves artifact                                        │
└─────────────────────────────────────────────────────────┘
```

### Problems with This Approach

1. **❌ Lost Interactivity:**
   - Original: Claude Code asks questions, user responds, negotiation happens
   - Current: Single API call, no conversation, no negotiation

2. **❌ Cost Explosion:**
   - Original: Claude Code execution (user's subscription, $0/project for API)
   - Current: Sonnet API calls (~$3/million tokens)
   - **Estimated cost increase: 10-20x for GTD-001**

3. **❌ No Human-in-the-Loop:**
   - Original: User approves scope, makes decisions at critical points
   - Current: LLM makes all decisions autonomously

4. **❌ Broke Prompt Design:**
   - Prompts say "STOP and request files" (for Claude Code)
   - LLM API can't "request files" - it just fails
   - Dialog templates are unused

5. **❌ Model Selection Wrong:**
   - GTD-001 says "Haiku Agent (Cost-Efficient)"
   - Code uses `model="claude-3-5-sonnet-20241022"`
   - No model selection logic exists

---

## 📊 COMPARISON TABLE

| Aspect | Original Design | Current Implementation | Impact |
|--------|----------------|----------------------|--------|
| **Operator** | Claude Code (CLI Agent) | Python + LLM API | Lost interactive capability |
| **Interaction** | Conversational, multi-turn | Single-shot API call | No negotiation, no user input |
| **Cost Model** | $0 API cost (user's Claude subscription) | ~$3/M tokens (Sonnet API) | **10-20x cost increase** |
| **Model** | Claude Code (whatever user has) | Hardcoded Sonnet 3.5 | No flexibility, wrong model |
| **HITL** | User approves at decision points | Autonomous LLM | Lost human validation |
| **Prompts** | Interactive instructions for Claude Code | Batch processing prompts | Mismatched intent |
| **Scope Negotiation** | Real dialog with user | LLM guesses | Poor quality |
| **Error Handling** | User sees errors, can fix | API fails silently | Poor UX |

---

## 🔍 HOW DID THIS HAPPEN?

### Root Cause Analysis

**Hypothesis:** The team started building Python automation scripts and **forgot the original design was for Claude Code operation.**

**Evidence:**

1. **GAD-001** (Architecture Decisions) doesn't clearly specify "Claude Code is the operator"
2. **GAD-002** focuses on Python orchestrator logic, not Claude Code invocation
3. **Phase handlers** (`planning_handler.py`, etc.) were built with LLM API clients
4. **GTD-001** mentions "Haiku Agent" operator, but no such agent exists in code

**Contributing Factors:**

- ⚠️ **Ambiguity in specs:** GAD documents don't explicitly say "Claude Code runs the agents"
- ⚠️ **Over-automation:** Team tried to automate everything with scripts
- ⚠️ **API-first mindset:** Defaulted to LLM API calls instead of interactive operation
- ⚠️ **Missing validation:** No one tested if the implementation matched the prompts

---

## 🎯 IMPLICATIONS FOR GTD-001

### Original Test Plan

**GTD-001 Line 8:**
```markdown
**Test Operator:** Haiku Agent (Cost-Efficient)
**Estimated Cost:** $5-15 (5 projects × $1-3 each)
```

### Reality Check

1. **❌ "Haiku Agent" doesn't exist:**
   - No code implements a Haiku-based operator
   - All code uses `model="claude-3-5-sonnet-20241022"`

2. **❌ Cost estimate is wrong:**
   - $5-15 assumes Haiku pricing (~$0.25/M tokens)
   - Reality: Sonnet pricing (~$3/M tokens)
   - **Actual cost: $50-150** for 5 projects

3. **❌ The "operator" is wrong:**
   - GTD-001 assumes autonomous agent execution
   - Original design: **Claude Code (me!) is the operator**
   - I should be running VIBE_ALIGNER tasks, not a Python script

4. **❌ The test won't validate the right thing:**
   - GTD-001 tests batch LLM processing
   - Should test: Interactive Claude Code workflows

---

## ✅ RECOMMENDED ACTIONS

### Immediate (Critical)

1. **📝 Update GTD-001:**
   - Change operator from "Haiku Agent" to "Claude Code (Sonnet 4.5)"
   - Update cost estimates for Sonnet API usage
   - Add regression testing: "Does this match original interactive design?"

2. **📋 Document the Regression:**
   - Add this report to `docs/reports/`
   - Update GAD-001/002 to clarify "Claude Code is the operator"
   - Flag all Python scripts that violate original design

3. **🔍 Audit All Agents:**
   - Which agents are designed for Claude Code operation?
   - Which have been "regressed" to API calls?
   - Create comparison matrix

### Short-Term (High Priority)

4. **🔄 Build Fallback Architecture:**
   - **Primary mode:** Claude Code interactive operation (original design)
   - **Fallback mode:** LLM API calls (current implementation)
   - Environment variable: `VIBE_OPERATOR_MODE=claude_code|api`

5. **📐 Restore Interactive Workflows:**
   - Implement orchestrator mode that **prompts Claude Code** instead of API calls
   - Use file-based handoff:
     ```
     1. Orchestrator writes: /tmp/vibe_task_123.md (composed prompt)
     2. Orchestrator: "Claude Code, read /tmp/vibe_task_123.md and execute"
     3. Claude Code reads, executes interactively
     4. Claude Code writes: /tmp/vibe_result_123.json
     5. Orchestrator reads result, continues
     ```

6. **💰 Add Model Selection Logic:**
   - Simple tasks → Haiku (if API mode)
   - Complex tasks → Sonnet
   - Critical tasks → Opus
   - Default → Claude Code (no API cost)

### Long-Term (Strategic)

7. **📚 Rewrite Documentation:**
   - GAD-001: Explicitly state "Claude Code is the primary operator"
   - GAD-002: Add "Fallback to API mode when Claude Code unavailable"
   - All agent prompts: Mark as "FOR CLAUDE CODE EXECUTION"

8. **🧪 Create Regression Tests:**
   - Test Suite 1: Claude Code interactive mode (manual)
   - Test Suite 2: API fallback mode (automated)
   - Ensure both modes produce equivalent results

9. **🎓 Team Education:**
   - "The vibe-agency framework is a CLI tool for Claude Code users"
   - "API mode is a fallback, not the primary design"
   - "Interactive > Autonomous for product development"

---

## 🚨 CRITICAL QUESTIONS FOR USER

### Before proceeding with GTD-001:

1. **What is the INTENDED operator for vibe-agency?**
   - A) Claude Code (interactive CLI agent) ← Original design
   - B) Autonomous Python scripts with LLM API calls ← Current implementation
   - C) Both (with mode selection) ← Recommended

2. **Should GTD-001 test:**
   - A) The current regressed implementation (API mode)?
   - B) The original interactive design (Claude Code mode)?
   - C) Both modes?

3. **What is the cost budget reality?**
   - Original estimate: $5-15 (assumes Haiku or $0 for Claude Code)
   - Current reality: $50-150 (Sonnet API calls)
   - Acceptable budget: ???

4. **Should we fix the regression BEFORE or AFTER GTD-001?**
   - Before: Restore interactive mode, then test
   - After: Test current state, use findings to justify restoration

---

## 📊 IMPACT ASSESSMENT

### Severity: 🔴 CRITICAL

**Why Critical:**
- Violates fundamental architectural design
- 10-20x cost increase
- Lost key capabilities (interactivity, HITL)
- All prompts are mismatched to implementation

### Affected Systems:
- ✅ VIBE_ALIGNER (all 6 tasks)
- ✅ MARKET_RESEARCHER
- ✅ TECH_RESEARCHER
- ✅ LEAN_CANVAS_VALIDATOR
- ✅ CODE_GENERATOR
- ⚠️ Likely: All agents in `agency_os/01_planning_framework/agents/`

### Risk if Not Fixed:
- GTD-001 tests the wrong thing
- Framework costs 10-20x more than designed
- User experience is degraded (no interaction)
- Future development builds on wrong foundation

---

## 🔄 NEXT STEPS

### Immediate Actions Needed:

1. **User Decision:** Clarify intended operator (Claude Code vs API vs Both)
2. **Update GTD-001:** Reflect actual operator and costs
3. **Choose Path:**
   - Path A: Test current regressed state (document as regression)
   - Path B: Fix regression first, then test correct implementation
   - Path C: Test both modes (regression + correct)

### Recommended Path: **C (Test Both Modes)**

**Rationale:**
- Documents current state (regression)
- Validates restored design (correct)
- Provides comparison data
- Informs strategic decision

**Implementation:**
1. GTD-001A: Test current API mode (5 projects, ~$50-150 cost)
2. Build Claude Code mode wrapper
3. GTD-001B: Test interactive mode (5 projects, ~$0 API cost)
4. Compare results, make strategic recommendation

---

## 📝 CONCLUSION

The vibe-agency framework has suffered a **CRITICAL architectural regression**:

**Original:** Interactive conversational agent system for Claude Code
**Current:** Batch LLM API processing system

**Impact:**
- ❌ Lost interactivity and human-in-the-loop
- ❌ 10-20x cost increase
- ❌ Prompts and code are mismatched
- ❌ GTD-001 test plan is based on wrong assumptions

**Recommendation:**
- ✅ Acknowledge regression
- ✅ Document correct design (this report)
- ✅ Restore Claude Code operator mode
- ✅ Keep API fallback mode
- ✅ Update GTD-001 to test both modes

**User decision required before proceeding.**

---

**Report End**

**Status:** ⏸️ AWAITING USER DECISION
**Priority:** 🔴 CRITICAL
**Blocker:** Cannot proceed with GTD-001 until operator model is clarified
