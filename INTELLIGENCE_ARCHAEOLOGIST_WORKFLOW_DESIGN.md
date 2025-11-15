# 🏛️ INTELLIGENCE_ARCHAEOLOGIST - Agent Workflow Design

**Version:** 0.1.0 (DRAFT)
**Date:** 2025-11-15
**Purpose:** Data-driven intelligence generation from Git + Code repositories
**Inspired by:** VIBE_ALIGNER workflow structure

---

## 🎯 MISSION STATEMENT

> "Extract measurable intelligence from repository history and codebase structure to understand **what was built, how it evolved, and why decisions were made** - enabling data-driven learning for future projects."

**NOT for:** Automated fixing (that's different agents)
**FOR:** Intelligence gathering, pattern recognition, learning from past

---

## 🧬 THREE-AGENT SYSTEM ARCHITECTURE

```
┌─────────────────────────────────────────────────────────────┐
│  ORCHESTRATOR (Makefile + Jupyter Notebooks)                │
│  - Coordinates 3 agents                                      │
│  - Aggregates intelligence                                   │
│  - Generates unified reports                                 │
└──────────────┬──────────────────────────────────────────────┘
               │
               ├─────────────────┬─────────────────┬
               ▼                 ▼                 ▼
    ┌──────────────────┐ ┌─────────────────┐ ┌─────────────────┐
    │ GIT_ARCHAEOLOGIST│ │ CODE_COMPLEXITY │ │ DECISION_MINER  │
    │                  │ │     ANALYZER    │ │                 │
    │ History Mining   │ │  Quality Metrics│ │  Why Analysis   │
    └──────────────────┘ └─────────────────┘ └─────────────────┘
```

---

## 🔍 AGENT 1: GIT_ARCHAEOLOGIST

### Core Responsibility
Extract timeline-based intelligence from Git history

### Tasks

#### **Task 01: Timeline Mapping**
```yaml
input: .git/
output: data/timeline.json

what_it_does:
  - Maps all commits chronologically
  - Identifies phases (setup, development, refactoring, regression)
  - Detects velocity changes
  - Flags "interesting" commits (large changes, reverts, migrations)

metrics:
  - commits_per_week: int
  - avg_files_per_commit: float
  - largest_commits: List[commit_hash]
  - phase_transitions: List[{date, phase, trigger}]
```

#### **Task 02: Decision Mining**
```yaml
input: git log --all -p
output: data/architectural_decisions.json

what_it_does:
  - Scans commit messages for decision keywords
    (ARCHITECTURE, DESIGN, DECIDED, MIGRATE, REFACTOR)
  - Extracts context from diffs
  - Classifies decision type
  - Links related commits

decision_taxonomy:
  - architectural_change
  - technology_adoption
  - pattern_migration
  - api_design
  - performance_optimization
  - security_enhancement

example_output:
  - decision_id: DEC-001
    date: 2025-11-10
    type: architectural_change
    description: "Migrated from Claude Code to LLM API batch processing"
    commit: c081d34
    files_affected: [core_orchestrator.py, planning_handler.py]
    reversions: [c6fcbc2]  # Later flagged as regression!
```

#### **Task 03: Contributor Analysis**
```yaml
input: git shortlog -sn --all
output: data/contributors.json

what_it_does:
  - Maps who contributed what
  - Identifies code ownership zones
  - Detects collaboration patterns
  - Measures contribution diversity

metrics:
  - top_contributors: List[{name, commits, files}]
  - code_ownership: Dict[file_path, primary_author]
  - collaboration_index: float  # How many files have >1 author
  - bus_factor: int  # How many people need to disappear before project stalls
```

#### **Task 04: Pattern Detection**
```yaml
input: git log --all --oneline
output: data/commit_patterns.json

what_it_does:
  - Detects commit message patterns
  - Identifies development cycles
  - Spots anomalies (unusual commit times, huge commits)
  - Recognizes workflow patterns (feature branches, hotfixes)

patterns:
  - conventional_commits: bool  # Uses "feat:", "fix:", etc?
  - emoji_usage: bool
  - pr_workflow: bool  # Merge commits detected?
  - release_cadence: Optional[str]  # "weekly", "monthly", etc
```

#### **Task 05: Regression Detection**
```yaml
input: data/timeline.json + data/architectural_decisions.json
output: data/regressions.json

what_it_does:
  - Identifies when code/design goes backwards
  - Detects contradictory decisions
  - Flags potential quality decay
  - Links to original "good state"

regression_signals:
  - code_complexity_spike
  - revert_of_previous_work
  - contradictory_architecture_decision
  - test_coverage_drop
  - documentation_removal

example:
  - regression_id: REG-001
    detected_at: c081d34
    type: contradictory_architecture_decision
    original_design: "Interactive Claude Code operator"
    regression: "Batch LLM API processing"
    severity: CRITICAL
    impact: "10-20x cost increase, lost interactivity"
```

#### **Task 06: Archaeological Report**
```yaml
input: All previous task outputs
output: GIT_ARCHAEOLOGY_REPORT.md

what_it_does:
  - Synthesizes all git-based intelligence
  - Creates visual timeline
  - Highlights key insights
  - Provides recommendations

sections:
  - Project Timeline
  - Key Decision Points
  - Contributor Overview
  - Pattern Analysis
  - Detected Regressions
  - Recommendations for Future
```

---

## 📊 AGENT 2: CODE_COMPLEXITY_ANALYZER

### Core Responsibility
Quantify code quality and track technical debt

### Tasks

#### **Task 01: Complexity Baseline**
```yaml
input: codebase (current state)
output: data/complexity_baseline.json

what_it_does:
  - Calculates cyclomatic complexity per file/function
  - Measures LOC (lines of code)
  - Counts functions, classes, modules
  - Identifies complexity hotspots

metrics:
  - total_loc: int
  - total_functions: int
  - avg_complexity_per_function: float
  - complexity_hotspots: List[{file, function, complexity}]

tools:
  - radon (Python complexity)
  - lizard (multi-language)
  - cloc (line counting)
```

#### **Task 02: Trend Analysis**
```yaml
input: git history + complexity metrics
output: data/complexity_trends.json

what_it_does:
  - Checks out each commit
  - Runs complexity analysis
  - Tracks how complexity evolves
  - Identifies complexity spikes

metrics:
  - complexity_over_time: List[{commit, date, avg_complexity}]
  - complexity_direction: "increasing" | "decreasing" | "stable"
  - biggest_complexity_spike: {commit, delta}

visualization:
  - Line graph: Complexity over time
  - Heatmap: Which files got more complex?
```

#### **Task 03: Hotspot Detection**
```yaml
input: git log --numstat + complexity data
output: data/code_hotspots.json

what_it_does:
  - Identifies files that change frequently + are complex
  - Flags high-risk areas (complex + churning)
  - Prioritizes refactoring targets

formula:
  hotspot_score = complexity * change_frequency

output:
  - file: agency_os/00_system/orchestrator/core_orchestrator.py
    complexity: 45
    changes: 12
    hotspot_score: 540
    risk_level: HIGH
    recommendation: "Refactor or add tests"
```

#### **Task 04: Dependency Graph**
```yaml
input: import statements, module structure
output: data/dependency_graph.json

what_it_does:
  - Maps module dependencies
  - Detects circular dependencies
  - Calculates coupling metrics
  - Identifies "god modules" (everything depends on it)

metrics:
  - coupling: Dict[module, List[dependencies]]
  - circular_deps: List[cycle]
  - most_depended_on: List[module]
  - orphan_modules: List[module]  # Nothing depends on it

visualization:
  - Directed graph (nodes = modules, edges = imports)
  - Highlight cycles in red
```

#### **Task 05: Technical Debt Quantification**
```yaml
input: All complexity data + git history
output: data/technical_debt.json

what_it_does:
  - Counts TODOs, FIXMEs, HACKs in code
  - Identifies code duplication
  - Flags missing tests
  - Estimates "cost to fix"

debt_categories:
  - todos: {count, estimated_hours}
  - code_duplication: {percentage, files}
  - missing_tests: {files_without_tests}
  - high_complexity: {files_above_threshold}

total_debt_estimate:
  hours: 42
  priority_breakdown:
    critical: 8h
    high: 15h
    medium: 12h
    low: 7h
```

#### **Task 06: Quality Report**
```yaml
input: All complexity task outputs
output: CODE_QUALITY_REPORT.md

sections:
  - Complexity Baseline
  - Trend Analysis (better or worse?)
  - Hotspot Prioritization
  - Dependency Health
  - Technical Debt Summary
  - Refactoring Roadmap
```

---

## 🧠 AGENT 3: DECISION_MINER

### Core Responsibility
Extract the "WHY" behind architectural and design choices

### Tasks

#### **Task 01: Architecture Decision Extraction**
```yaml
input:
  - git log (commit messages)
  - Pull Request descriptions (if available)
  - Documentation (GAD, docs/)
output: data/architecture_decisions.json

what_it_does:
  - NLP on commit messages to extract decisions
  - Parses ADR (Architecture Decision Records) if present
  - Links commits to documentation
  - Classifies decision types

decision_schema:
  - id: ADR-001
    title: "Use Claude Code as primary operator"
    date: 2025-11-01
    status: "accepted" | "superseded" | "deprecated"
    context: "We need interactive workflows with users"
    decision: "Use Claude Code CLI agent for all agent execution"
    consequences:
      - "Zero API cost for users"
      - "Interactive, not batch"
    sources: [commit_hash, doc_path]
```

#### **Task 02: Trade-off Analysis**
```yaml
input: data/architecture_decisions.json
output: data/trade_offs.json

what_it_does:
  - Identifies explicit trade-offs in decisions
  - Detects implicit trade-offs (from consequences)
  - Categorizes by trade-off type
  - Links to outcomes

trade_off_types:
  - speed_vs_quality
  - cost_vs_features
  - simplicity_vs_flexibility
  - performance_vs_maintainability
  - short_term_vs_long_term

example:
  - trade_off_id: TO-001
    decision: ADR-001 (Claude Code operator)
    chosen: "Claude Code (interactive, $0 API cost)"
    rejected: "LLM API batch processing (autonomous, $3/M tokens)"
    trade_off_type: cost_vs_features
    actual_outcome: "Later regressed to LLM API (REG-001)"
    lesson: "Team didn't understand original design"
```

#### **Task 03: Pattern Identification**
```yaml
input: All architecture decisions
output: data/architectural_patterns.json

what_it_does:
  - Groups similar decisions
  - Identifies recurring patterns
  - Detects architectural principles
  - Recognizes anti-patterns

patterns:
  - "Prefer interactive over autonomous"
  - "Cost optimization via free APIs"
  - "Modular agent system"
  - "Knowledge base driven prompts"

anti_patterns:
  - "Implementing before understanding design"
  - "Over-automation (LLM API everywhere)"
  - "Docs not matching code"
```

#### **Task 04: Consistency Check**
```yaml
input:
  - data/architecture_decisions.json
  - data/regressions.json (from GIT_ARCHAEOLOGIST)
output: data/consistency_analysis.json

what_it_does:
  - Checks if implementation matches decisions
  - Flags contradictions
  - Identifies drift from principles
  - Measures adherence score

consistency_metrics:
  - decision_implementation_rate: 60%  # Only 60% of decisions actually implemented
  - contradictory_decisions: List[{decision_a, decision_b, conflict}]
  - principle_violations: List[{principle, violation}]

example:
  - violation:
      principle: "Claude Code is the operator"
      implementation: "LLM API batch processing"
      severity: CRITICAL
      detected_by: REG-001
```

#### **Task 05: Wisdom Synthesis**
```yaml
input: All DECISION_MINER outputs
output: data/project_wisdom.json

what_it_does:
  - Extracts "lessons learned"
  - Identifies what worked vs didn't
  - Synthesizes best practices
  - Generates recommendations

wisdom_categories:
  - what_worked: List[insight]
  - what_failed: List[insight]
  - unexpected_outcomes: List[insight]
  - apply_to_future: List[recommendation]

example:
  what_worked:
    - "Modular agent architecture is flexible"
    - "Knowledge bases prevent hallucinations"
    - "Git-first workflow enables archaeology"

  what_failed:
    - "Over-automation without understanding design"
    - "Docs diverged from code quickly"
    - "No regression testing for architecture"

  apply_to_future:
    - "Always validate implementation against design docs"
    - "Set up architecture tests (assert operator == claude_code)"
    - "Regular git archaeology sessions"
```

#### **Task 06: Recommendation Engine**
```yaml
input: data/project_wisdom.json + all metrics
output: DECISION_MINING_REPORT.md

what_it_does:
  - Generates actionable recommendations
  - Prioritizes by impact
  - Links to supporting data
  - Provides implementation guidance

recommendations:
  - "Restore Claude Code operator (based on REG-001)"
  - "Add architecture tests to prevent regressions"
  - "Schedule monthly git archaeology sessions"
  - "Create ADR process for future decisions"
```

---

## 🛠️ TOOLING & IMPLEMENTATION

### Jupyter Notebooks (Exploration Phase)

```
intelligence_notebooks/
│
├── 01_git_archaeology.ipynb
│   ├── Cell 1: Setup (import gitpython, pandas, matplotlib)
│   ├── Cell 2: Clone & analyze commit history
│   ├── Cell 3: Timeline visualization
│   ├── Cell 4: Decision keyword extraction
│   ├── Cell 5: Contributor analysis
│   ├── Cell 6: Export data/timeline.json
│
├── 02_code_complexity.ipynb
│   ├── Cell 1: Install radon, lizard
│   ├── Cell 2: Run complexity analysis
│   ├── Cell 3: Visualize complexity hotspots
│   ├── Cell 4: Trend over time (checkout each commit)
│   ├── Cell 5: Dependency graph visualization
│   ├── Cell 6: Export data/complexity_baseline.json
│
├── 03_decision_mining.ipynb
│   ├── Cell 1: Load commit messages + docs
│   ├── Cell 2: NLP keyword extraction (spacy)
│   ├── Cell 3: Classify decisions
│   ├── Cell 4: Trade-off detection
│   ├── Cell 5: Consistency check
│   ├── Cell 6: Export data/architecture_decisions.json
│
├── 04_dependency_analysis.ipynb
│   ├── Cell 1: Parse Python imports
│   ├── Cell 2: Build dependency graph (networkx)
│   ├── Cell 3: Detect cycles
│   ├── Cell 4: Visualize with graphviz
│   ├── Cell 5: Export data/dependency_graph.json
│
└── 05_unified_intelligence.ipynb
    ├── Cell 1: Load all data/*.json
    ├── Cell 2: Cross-reference insights
    ├── Cell 3: Generate unified dashboard
    ├── Cell 4: Interactive visualizations (plotly)
    ├── Cell 5: Export INTELLIGENCE_REPORT.md
```

### Makefile (Automation Phase)

```makefile
# INTELLIGENCE_ARCHAEOLOGIST Automation Pipeline

# Directories
DATA_DIR := data
REPORTS_DIR := reports
NOTEBOOKS_DIR := intelligence_notebooks

# Python
PYTHON := python3
JUPYTER := jupyter

# Targets
.PHONY: all clean intelligence quick-check visualize

# === MAIN PIPELINE ===

all: clean intelligence visualize

intelligence: git-archaeology code-complexity decision-mining unified-report

# === AGENT TASKS ===

git-archaeology:
	@echo "🔍 [GIT_ARCHAEOLOGIST] Running..."
	@mkdir -p $(DATA_DIR)
	$(PYTHON) scripts/agents/git_archaeologist.py \
		--repo . \
		--output $(DATA_DIR)/git_intelligence.json
	@echo "✅ Git archaeology complete"

code-complexity:
	@echo "📊 [CODE_COMPLEXITY_ANALYZER] Running..."
	$(PYTHON) scripts/agents/complexity_analyzer.py \
		--repo . \
		--output $(DATA_DIR)/complexity_metrics.json
	@echo "✅ Complexity analysis complete"

decision-mining:
	@echo "🧠 [DECISION_MINER] Running..."
	$(PYTHON) scripts/agents/decision_miner.py \
		--repo . \
		--docs docs/ \
		--output $(DATA_DIR)/architecture_decisions.json
	@echo "✅ Decision mining complete"

# === REPORTING ===

unified-report:
	@echo "📝 Generating unified intelligence report..."
	@mkdir -p $(REPORTS_DIR)
	$(PYTHON) scripts/generate_unified_report.py \
		--git $(DATA_DIR)/git_intelligence.json \
		--complexity $(DATA_DIR)/complexity_metrics.json \
		--decisions $(DATA_DIR)/architecture_decisions.json \
		--output $(REPORTS_DIR)/INTELLIGENCE_REPORT.md
	@echo "✅ Report generated: $(REPORTS_DIR)/INTELLIGENCE_REPORT.md"

# === VISUALIZATION ===

visualize:
	@echo "📈 Generating visualizations..."
	$(JUPYTER) nbconvert --execute \
		$(NOTEBOOKS_DIR)/05_unified_intelligence.ipynb \
		--to html \
		--output $(REPORTS_DIR)/intelligence_dashboard.html
	@echo "✅ Dashboard: $(REPORTS_DIR)/intelligence_dashboard.html"

# === QUICK CHECKS ===

quick-check:
	@echo "⚡ Quick intelligence check (last 10 commits)..."
	$(PYTHON) scripts/quick_intelligence.py --limit 10

# === UTILITY ===

clean:
	@echo "🧹 Cleaning previous intelligence data..."
	rm -rf $(DATA_DIR)/*.json
	rm -rf $(REPORTS_DIR)/*
	@echo "✅ Clean complete"

# === DEVELOPMENT ===

notebook:
	@echo "🔬 Starting Jupyter notebook server..."
	cd $(NOTEBOOKS_DIR) && $(JUPYTER) notebook

install-deps:
	@echo "📦 Installing dependencies..."
	pip install -r requirements-intelligence.txt
	@echo "✅ Dependencies installed"
```

---

## 📊 DATA PIPELINE

```
┌─────────────────┐
│  Git Repository │
│   (.git/)       │
└────────┬────────┘
         │
         ├──────────────────────┬──────────────────────┬
         │                      │                      │
         ▼                      ▼                      ▼
┌──────────────────┐  ┌──────────────────┐  ┌──────────────────┐
│ GIT_ARCHAEOLOGIST│  │CODE_COMPLEXITY   │  │ DECISION_MINER   │
│                  │  │    ANALYZER      │  │                  │
└────────┬─────────┘  └────────┬─────────┘  └────────┬─────────┘
         │                     │                     │
         ▼                     ▼                     ▼
    git_intelligence.json  complexity_metrics.json  architecture_decisions.json
         │                     │                     │
         └─────────────────────┴─────────────────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │  UNIFIED AGGREGATOR  │
                    │  (generate_report.py)│
                    └──────────┬───────────┘
                               │
                ┌──────────────┴──────────────┐
                ▼                             ▼
    INTELLIGENCE_REPORT.md         intelligence_dashboard.html
         (Markdown)                      (Interactive)
```

---

## 🎯 OUTPUT DELIVERABLES

### 1. Raw Data (JSON)
- `data/git_intelligence.json` - All git metrics
- `data/complexity_metrics.json` - Code quality data
- `data/architecture_decisions.json` - Extracted decisions
- `data/regressions.json` - Detected regressions
- `data/dependency_graph.json` - Module dependencies

### 2. Reports (Markdown)
- `INTELLIGENCE_REPORT.md` - Unified findings
- `GIT_ARCHAEOLOGY_REPORT.md` - Git-specific insights
- `CODE_QUALITY_REPORT.md` - Complexity analysis
- `DECISION_MINING_REPORT.md` - Architectural wisdom

### 3. Visualizations (HTML)
- `intelligence_dashboard.html` - Interactive dashboard
  - Timeline graph (commits over time)
  - Complexity heatmap
  - Dependency graph (interactive)
  - Decision timeline
  - Contributor charts

### 4. Notebooks (Exploratory)
- `*.ipynb` files - Reproducible analysis workflows

---

## 🔬 EXAMPLE USE CASES

### Use Case 1: "Why did we make that decision?"
```bash
make decision-mining
# → Generates architecture_decisions.json
# → Search for keyword: "operator"
# → Find: ADR-001: "Use Claude Code as operator"
# → See reasoning, trade-offs, consequences
```

### Use Case 2: "Is our code getting worse?"
```bash
make code-complexity
# → Tracks complexity over time
# → Shows: Spike at commit c081d34
# → Correlate with git archaeology
# → Find: Same commit = architecture regression!
```

### Use Case 3: "What should we refactor first?"
```bash
make intelligence  # Full pipeline
# → Hotspot detection finds:
#    core_orchestrator.py (complexity: 45, changes: 12, score: 540)
# → Recommendation: Refactor this file first
```

### Use Case 4: "Monthly intelligence review"
```bash
make clean && make all
# → Fresh intelligence report
# → Review dashboard.html with team
# → Discuss findings, plan next sprint
```

---

## 🚀 IMPLEMENTATION ROADMAP

### Phase 1: Prototype (Week 1-2)
- [ ] Create Jupyter notebooks for each agent
- [ ] Implement basic git archaeology (timeline, contributors)
- [ ] Basic complexity analysis (radon on Python files)
- [ ] Simple decision mining (keyword search in commits)
- [ ] Manual testing on vibe-research repo (30 commits)

### Phase 2: Automation (Week 3-4)
- [ ] Extract logic from notebooks to Python scripts
- [ ] Create Makefile pipeline
- [ ] Add data validation
- [ ] Implement unified report generator
- [ ] Test on multiple repos

### Phase 3: Advanced Features (Week 5-6)
- [ ] NLP for decision extraction (spacy, transformers)
- [ ] Dependency graph visualization (networkx + graphviz)
- [ ] Interactive dashboard (plotly dash)
- [ ] Regression detection algorithm
- [ ] Trade-off analysis

### Phase 4: Productization (Week 7-8)
- [ ] Package as `vibe-intelligence` CLI tool
- [ ] Add to vibe-agency as intelligence module
- [ ] GitHub Action for CI/CD
- [ ] Documentation + examples
- [ ] Beta testing with vibe-research

---

## 💡 WHY THIS DESIGN?

### Alignment with VIBE_ALIGNER Pattern:
- ✅ **Multi-task workflow** (6 tasks per agent)
- ✅ **Knowledge bases** (patterns, taxonomies)
- ✅ **Structured outputs** (JSON artifacts)
- ✅ **Orchestration** (Makefile = orchestrator)
- ✅ **Human-in-the-loop** (Jupyter for exploration)

### Data-Driven & Measurable:
- ✅ All metrics are **quantifiable** (complexity numbers, commit counts)
- ✅ **Reproducible** (Makefile ensures same results)
- ✅ **Version controlled** (commit intelligence data)
- ✅ **Visualizable** (graphs, charts, dashboards)

### Learning-Oriented:
- ✅ **Retrospective** (understand past, don't just fix)
- ✅ **Pattern extraction** (learn what works)
- ✅ **Wisdom synthesis** (codify best practices)
- ✅ **Future-facing** (recommendations for next projects)

---

## 🎯 SUCCESS CRITERIA

This workflow is successful if it can:

1. **Answer the regression question:** "When did we go from Claude Code to LLM API, and why?"
2. **Quantify code quality:** "Is our codebase getting better or worse?"
3. **Extract decisions:** "What architectural decisions were made, and do we still agree?"
4. **Predict risk:** "Which files are most likely to cause problems?"
5. **Generate wisdom:** "What should we do differently next time?"

---

## 📎 NEXT STEPS

### To start prototyping:

```bash
# 1. Create notebook directory
mkdir -p intelligence_notebooks

# 2. Start Jupyter
cd intelligence_notebooks
jupyter notebook

# 3. Create first notebook: 01_git_archaeology.ipynb

# 4. Install dependencies
pip install gitpython pandas matplotlib radon lizard networkx
```

### Questions to answer:
- Should we start with Jupyter or scripts?
- Which agent to prototype first? (I vote GIT_ARCHAEOLOGIST)
- What's the MVP? (Timeline + basic decision mining?)

---

**END OF DESIGN DOC**

**Status:** 🎨 DESIGN COMPLETE, READY FOR PROTOTYPING
**Next Action:** User decides: Start with Jupyter notebook or Makefile?
**Estimated Effort:** 2-3 days for MVP, 2 weeks for full system
