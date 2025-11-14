# 🎯 ITERATIVE ARCHITECTURE RECOVERY PLAN
**Plan ID:** RECOVERY-001
**Date:** 2025-11-14
**Purpose:** Systematische Wiederherstellung der korrekten Architektur
**Approach:** Iterativ, wasserdicht, Git-basiert (KEIN AI SLOP!)

---

## 🚨 AKTUELLE SITUATION

### Was wir entdeckt haben:
1. **MASSIVE REGRESSION:** vibe-agency wurde von "Claude Code Operator System" zu "LLM API Batch Processing" umgebaut
2. **VERDACHT:** Das gleiche Problem könnte beim Research Framework passiert sein
3. **FEHLENDE KLARHEIT:** Core Components Hierarchie (SSF → agency_os → knowledge) nicht klar dokumentiert
4. **GIT HISTORIE:** Evtl. kritische Entscheidungen VOR GAD-001/002 nicht festgehalten

### Was der User will:
- ✅ **Keine weitere Regression!**
- ✅ **Schnell Klarheit** über die richtige Architektur
- ✅ **Iterativer Plan** (nicht zu viel auf einmal)
- ✅ **Git Truth > Documentation** (AI Slop vermeiden)

---

## 📋 ITERATIVER PLAN (Phasen)

### PHASE 1: FUNDAMENTALS KLÄREN (Jetzt!)
**Ziel:** Core Components Hierarchie und Rollen verstehen

#### 1.1 System Steward Framework (SSF) - COMPLETED ✅
**Findings:**
- ✅ **SSF_ROUTER**: Intent routing, "Du bist der Archivar"
- ✅ **LEAD_ARCHITECT**: Strategic decisions, Governance
- ✅ **AUDITOR**: Validation, Quality Gates
- ✅ **Rolle**: "Du führst den Uhrmacher (den Menschen) durch die SOPs"
- ✅ **WICHTIG**: "Du erschaffst nichts; Du liest die Pläne"

**Interpretation:**
→ System Steward ist das META-FRAMEWORK, das den "Uhrmacher" (Claude Code) führt
→ Der "Uhrmacher" = **Claude Code User** (der Mensch + AI Agent)
→ SSF ist KEIN autonomer Agent, sondern ein GUIDANCE SYSTEM

#### 1.2 Agency OS Hierarchie - IN PROGRESS
**Zu klären:**
- [ ] Was ist "agency_os" genau? (Operating System? Framework Collection?)
- [ ] Hierarchie: SSF → agency_os → Frameworks (01-05)?
- [ ] Wer orchestriert wen?

**Datenpunkte:**
```
agency_os/
├── 00_system/          # Core: Orchestrator, Runtime, Contracts
├── 01_planning_framework/  # VIBE_ALIGNER, etc.
├── 02_code_gen_framework/
├── 03_qa_framework/
├── 04_deploy_framework/
└── 05_maintenance_framework/
```

**Hypothese:**
- **Layer 1**: System Steward (Meta-Governance)
- **Layer 2**: agency_os/00_system (Core Orchestrator)
- **Layer 3**: Frameworks 01-05 (SDLC Phases)
- **Layer 4**: Agents (VIBE_ALIGNER, etc.)
- **Operator**: Claude Code (führt Agents aus)

#### 1.3 Knowledge Base System - PENDING
**Zu klären:**
- [ ] Wo ist die Knowledge Base? (system_steward_framework/knowledge/? agency_os/01_planning_framework/knowledge/?)
- [ ] Wie wird sie geladen?
- [ ] Ist sie korrekt implementiert? (Verdacht: Nein!)

**User-Hinweis:** "das knowledge system ist, vermutlich, auch noch nicht korrekt so wie angedacht implementiert"

---

### PHASE 2: GIT HISTORIE ANALYSE (Nächster Schritt)
**Ziel:** Ursprüngliche Architektur-Entscheidungen finden

#### 2.1 Pre-GAD Commits analysieren
**Git-Befehle:**
```bash
# Finde ersten Commit
git log --all --reverse --oneline | head -1

# Analyse erste 20 Commits
git log --all --reverse --oneline | head -20

# Suche nach Architektur-Keywords
git log --all --grep="architecture\|design\|operator\|orchestrator" --oneline

# Diff zwischen erstem Commit und jetzt
git diff 004e95f..HEAD -- agency_os/00_system/
```

**Fragen:**
- Wann wurde PromptRuntime gebaut?
- Wann wurde LLM API Integration gebaut?
- Was war die URSPRÜNGLICHE Intention?

#### 2.2 ARCHITECTURE_GAP_ANALYSIS.md tiefenanalyse
**Gefunden:** GAP-001 sagt "Human must manually copy/paste prompts to Claude Code"

**Das ist KEIN Gap, das ist das DESIGN!**

**Zu prüfen:**
- Wer hat GAP-001 als "Missing" markiert?
- Wann wurde entschieden, LLM API zu bauen?
- War das eine bewusste Design-Änderung oder ein Missverständnis?

**Git-Befehl:**
```bash
git log --all -p -- docs/architecture/ARCHITECTURE_GAP_ANALYSIS.md
```

#### 2.3 Zugriff auf vibe-agency Original-Historie?
**User-Frage:** "hast du zugriff auf die originale vibe-agency historie? oder nur ab migration?"

**Zu prüfen:**
- Ist vibe-agency ein separates Repo?
- Ist vibe-research ein Fork/Clone?
- Gibt es eine .git/config remote zu vibe-agency?

**Git-Befehl:**
```bash
git remote -v
git log --all --oneline | tail -1  # Ältester Commit
```

---

### PHASE 3: RESEARCH FRAMEWORK CHECK (Parallel)
**Ziel:** Prüfen ob Research Framework die GLEICHE Regression hat

**User-Warnung:** "das passiert gleich wieder oder ist schon passiert mit dem research modul!!"

#### 3.1 Research Framework Struktur
**Zu finden:**
```bash
find . -path "*research*" -name "*.py" -o -name "*.md" | grep -v ".git"
```

**Erwartete Komponenten:**
- MARKET_RESEARCHER
- TECH_RESEARCHER
- FACT_VALIDATOR
- USER_RESEARCHER

#### 3.2 Check: Ist Research Framework interactive oder API-based?
**Zu prüfen:**
- Haben Research Agents _composition.yaml? (→ designed for Claude Code)
- Gibt es Python scripts die LLM API calls machen? (→ Regression!)
- Sind Prompts in 2nd Person? ("You are MARKET_RESEARCHER...")

**Red Flags:**
- ❌ `llm_client.invoke()` in research code
- ❌ Hardcoded `model="claude-sonnet-..."`
- ❌ Keine interaktive Dialog-Templates

#### 3.3 Vergleich: Research vs. VIBE_ALIGNER
**Parallel-Analyse:**
| Aspekt | VIBE_ALIGNER | Research Framework |
|--------|--------------|-------------------|
| _composition.yaml? | ✅ Exists | ??? |
| Interactive tasks? | ✅ 6 tasks with dialogs | ??? |
| LLM API calls? | ❌ (in regression) | ??? |
| Designed for Claude Code? | ✅ Yes | ??? |

---

### PHASE 4: KLASSISCHE CODE BASICS (Später)
**Ziel:** Grundlegende Code-Struktur verbessern

**User-Hinweis:** "uns fehlen auch - vermutlich - klassische code basics - daran fehlt es auch komplett"

**Was fehlt wahrscheinlich:**
- [ ] Proper error handling
- [ ] Logging
- [ ] Tests
- [ ] Type hints
- [ ] Documentation
- [ ] Configuration management

**ABER:** Das ist NICHT JETZT! Erst Architektur klären, dann Code Quality.

---

## 🔄 EXECUTION STRATEGY (Iterativ & Wasserdicht)

### Round 1: IMMEDIATE CLARITY (Heute)

**Step 1.1:** System Steward Rolle verstehen ✅ DONE
- SSF ist Guidance System für Claude Code
- "Du führst den Uhrmacher durch die SOPs"
- Kein autonomer Agent

**Step 1.2:** agency_os Hierarchie klären 🔄 IN PROGRESS
- [ ] README.md von agency_os/00_system/ lesen
- [ ] Orchestrator-Code analysieren (wer ruft wen?)
- [ ] Diagramm machen: SSF → 00_system → Frameworks → Agents

**Step 1.3:** Research Framework Regression-Check 🔄 PARALLEL
- [ ] Finde Research Agents (_composition.yaml?)
- [ ] Check für LLM API calls
- [ ] Vergleich mit VIBE_ALIGNER Struktur

**Output:** `ROUND_1_FINDINGS.md`
- Core Components Hierarchie
- Research Framework Status
- Next Questions

### Round 2: GIT ARCHEOLOGY (Morgen?)

**Step 2.1:** Git Historie deep dive
- [ ] Analysiere erste 50 Commits
- [ ] Finde "Wann wurde LLM API gebaut?"
- [ ] Finde "Was war vor GAP-001?"

**Step 2.2:** ARCHITECTURE_GAP_ANALYSIS.md Git History
- [ ] Wer schrieb GAP-001?
- [ ] Wann wurde es zum "Gap"?
- [ ] Gab es eine Design-Diskussion?

**Step 2.3:** vibe-agency Original Zugriff?
- [ ] Check git remote
- [ ] Ist vibe-research ein Fork?
- [ ] Können wir Original-Commits sehen?

**Output:** `ROUND_2_GIT_FINDINGS.md`
- Architektur-Timeline
- LLM API Decision Point
- Original Design Intent

### Round 3: ARCHITECTURE RESTORATION (Nächste Woche?)

**Step 3.1:** Definiere CORRECT Architecture
- [ ] Basierend auf Git Truth + SSF Rolle
- [ ] Dual-Mode Design (Claude Code + API Fallback)
- [ ] Klare Hierarchie dokumentieren

**Step 3.2:** Update GTD-001
- [ ] Operator = Claude Code (nicht "Haiku Agent")
- [ ] Cost = $0 für Claude Code Mode (nicht $5-15)
- [ ] Test Plan = Interactive Workflows

**Step 3.3:** Restoration Roadmap
- [ ] Schritt-für-Schritt Plan
- [ ] Was muss gebaut werden?
- [ ] Was muss entfernt werden?

**Output:** `ARCHITECTURE_RESTORATION_ROADMAP.md`

---

## ✅ SUCCESS CRITERIA (Per Round)

### Round 1 Success:
- ✅ SSF Rolle klar verstanden
- ✅ agency_os Hierarchie dokumentiert
- ✅ Research Framework Regression-Status bekannt
- ✅ User kann entscheiden: "Weiter zu Round 2?"

### Round 2 Success:
- ✅ Git Historie analysiert
- ✅ Original Design Intent gefunden
- ✅ LLM API Decision Point identifiziert
- ✅ User kann entscheiden: "Restoration starten?"

### Round 3 Success:
- ✅ Korrekte Architektur definiert
- ✅ Restoration Roadmap erstellt
- ✅ GTD-001 updated
- ✅ User kann entscheiden: "Mit Restoration beginnen?"

---

## 🚧 CURRENT STATUS

**Phase:** Round 1 (IMMEDIATE CLARITY)
**Progress:**
- ✅ Step 1.1: SSF Rolle verstanden
- 🔄 Step 1.2: agency_os Hierarchie (IN PROGRESS)
- ⏳ Step 1.3: Research Framework Check (PENDING)

**Blocker:** NONE
**Next Action:** Finish Step 1.2 + 1.3, create ROUND_1_FINDINGS.md

---

## 📊 DECISION POINTS (User Input Required)

### Decision Point 1: Nach Round 1
**Question:** "Haben wir genug Klarheit über die Hierarchie, oder brauchen wir Git-Archeology?"
**Options:**
- A) Genug Klarheit → Skip Round 2, go to Restoration
- B) Brauchen Git Truth → Continue to Round 2
- C) Pause, digest findings first

### Decision Point 2: Nach Round 2
**Question:** "Wollen wir die Regression fixen oder dokumentieren?"
**Options:**
- A) Sofort fixen (Restoration starten)
- B) Erst GTD-001 mit current state testen, dann fixen
- C) Beide Modi parallel testen (Claude Code + API)

### Decision Point 3: Research Framework
**Question:** "Wenn Research Framework die gleiche Regression hat, was machen wir?"
**Options:**
- A) Parallel fixen (mit VIBE_ALIGNER)
- B) Erst VIBE_ALIGNER, dann Research
- C) Nur dokumentieren, später fixen

---

## 🎯 DELIVERABLES (Per Round)

### Round 1:
- `ROUND_1_FINDINGS.md` - Core Components Hierarchie + Research Status
- `CORE_COMPONENTS_DIAGRAM.md` - Visual Hierarchy

### Round 2:
- `ROUND_2_GIT_FINDINGS.md` - Git Archeology Results
- `ARCHITECTURE_TIMELINE.md` - Wann wurde was entschieden

### Round 3:
- `ARCHITECTURE_RESTORATION_ROADMAP.md` - Step-by-step Restoration
- `GTD_001_UPDATED.md` - Korrigierter Test Plan

---

## 🔒 ANTI-SLOP GUARANTEES

**This plan is WATERPROOF because:**

1. **Git-basiert:** Findings kommen aus Code/Git, nicht aus AI Spekulation
2. **Iterativ:** User kann nach jeder Round stoppen/entscheiden
3. **Dokumentiert:** Jede Round produziert Artefakt für Review
4. **Checkpoints:** Success Criteria per Round, nicht am Ende
5. **User-Driven:** Decision Points eingebaut, kein Autopilot

**Was wir NICHT tun:**
- ❌ Spekulieren über "was gemeint war"
- ❌ Alles auf einmal fixen wollen
- ❌ Dokumentation als Truth nehmen (Git > Docs)
- ❌ Ohne User-Approval weitermachen

---

## ⏭️ IMMEDIATE NEXT STEPS

**Jetzt (in dieser Session):**
1. [IN PROGRESS] agency_os Hierarchie klären (Step 1.2)
2. [PENDING] Research Framework Check (Step 1.3)
3. [PENDING] Create `ROUND_1_FINDINGS.md`
4. [WAITING] User Decision: Continue to Round 2?

**User-Frage:**
**"Soll ich Round 1 jetzt abschließen (Steps 1.2 + 1.3), oder willst du erstmal das bisherige verdauen?"**

---

**Plan Status:** ⏸️ AWAITING USER INPUT
**Current Round:** 1 (IMMEDIATE CLARITY)
**Completion:** 33% (1/3 steps done)

---

END OF PLAN
