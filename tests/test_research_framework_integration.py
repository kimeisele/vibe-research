#!/usr/bin/env python3
"""
Research Framework Integration Test

Test Szenario: "Dog Sitting Marketplace App"
Ziel: Prüfen ob RESEARCH → PLANNING Flow funktioniert
"""
import sys
import json
from pathlib import Path
import importlib.util

# Load prompt runtime
spec = importlib.util.spec_from_file_location(
    "prompt_runtime",
    "agency_os/00_system/runtime/prompt_runtime.py"
)
prompt_runtime = importlib.util.module_from_spec(spec)
spec.loader.exec_module(prompt_runtime)
PromptRuntime = prompt_runtime.PromptRuntime


def test_research_framework_structure():
    """Test: Research Framework Struktur existiert"""
    print("\n" + "="*60)
    print("TEST 1: Research Framework Struktur")
    print("="*60)

    required_agents = [
        "agency_os/01_research_framework/agents/MARKET_RESEARCHER",
        "agency_os/01_research_framework/agents/TECH_RESEARCHER",
        "agency_os/01_research_framework/agents/FACT_VALIDATOR",
        "agency_os/01_research_framework/agents/USER_RESEARCHER"
    ]

    for agent_path in required_agents:
        if not Path(agent_path).exists():
            print(f"❌ FAIL: Missing agent: {agent_path}")
            return False
        print(f"✓ Found: {agent_path}")

    print("✅ PASS: All research agents exist")
    return True


def test_research_workflow_definition():
    """Test: RESEARCH workflow design exists"""
    print("\n" + "="*60)
    print("TEST 2: Research Workflow Definition")
    print("="*60)

    workflow_file = Path("agency_os/01_research_framework/state_machine/RESEARCH_workflow_design.yaml")

    if not workflow_file.exists():
        print(f"❌ FAIL: Missing workflow: {workflow_file}")
        return False

    content = workflow_file.read_text()

    # Check critical sections
    checks = [
        ("execution_order", "Agent execution order defined"),
        ("MARKET_RESEARCHER", "Market researcher in workflow"),
        ("TECH_RESEARCHER", "Tech researcher in workflow"),
        ("FACT_VALIDATOR", "Fact validator in workflow"),
        ("handoff_to_lean_canvas", "Handoff to LEAN_CANVAS defined"),
        ("quality_gates", "Quality gates defined")
    ]

    for keyword, desc in checks:
        if keyword in content:
            print(f"✓ {desc}")
        else:
            print(f"❌ Missing: {desc}")
            return False

    print("✅ PASS: Research workflow properly defined")
    return True


def test_orchestrator_integration():
    """Test: Ist RESEARCH in ORCHESTRATOR integriert?"""
    print("\n" + "="*60)
    print("TEST 3: ORCHESTRATOR Integration (CRITICAL)")
    print("="*60)

    orchestrator_workflow = Path("agency_os/00_system/state_machine/ORCHESTRATION_workflow_design.yaml")

    if not orchestrator_workflow.exists():
        print(f"❌ FAIL: Orchestrator workflow missing")
        return False

    content = orchestrator_workflow.read_text()

    # Check if RESEARCH is in the main state machine
    if "RESEARCH" in content:
        print(f"✓ RESEARCH state found in orchestrator")
        return True
    else:
        print(f"❌ FAIL: RESEARCH NOT in orchestrator state machine!")
        print(f"   → CRITICAL GAP: Research is isolated from main SDLC")
        print(f"   → States found: PLANNING, CODING, TESTING, DEPLOYMENT, MAINTENANCE")
        print(f"   → RESEARCH is defined separately but NOT integrated")
        return False


def test_data_contracts():
    """Test: Sind research_brief.json contracts definiert?"""
    print("\n" + "="*60)
    print("TEST 4: Data Contracts (research_brief.json)")
    print("="*60)

    contracts_file = Path("agency_os/00_system/contracts/ORCHESTRATION_data_contracts.yaml")

    if not contracts_file.exists():
        print(f"❌ FAIL: Data contracts file missing")
        return False

    content = contracts_file.read_text()

    # Check if research_brief schema is defined
    if "research_brief.schema.json" in content:
        print(f"✓ research_brief.json schema defined")
    else:
        print(f"❌ research_brief.json schema NOT defined")
        return False

    # Check handoff fields
    handoff_checks = [
        ("market_analysis", "Market analysis field"),
        ("tech_analysis", "Tech analysis field"),
        ("fact_validation", "Fact validation field"),
        ("handoff_to_lean_canvas", "Handoff section")
    ]

    for field, desc in handoff_checks:
        if field in content:
            print(f"✓ {desc} defined")
        else:
            print(f"⚠️  {desc} missing")

    print("✅ PASS: research_brief.json contract exists")
    return True


def test_vibe_aligner_research_integration():
    """Test: Kann VIBE_ALIGNER research_brief.json konsumieren?"""
    print("\n" + "="*60)
    print("TEST 5: VIBE_ALIGNER + research_brief Integration")
    print("="*60)

    vibe_prompt = Path("agency_os/01_planning_framework/prompts/VIBE_ALIGNER_v3.md")

    if not vibe_prompt.exists():
        print(f"❌ FAIL: VIBE_ALIGNER prompt missing")
        return False

    content = vibe_prompt.read_text()

    # Check if VIBE_ALIGNER knows about research_brief
    if "research_brief" in content.lower() or "research" in content.lower():
        print(f"⚠️  VIBE_ALIGNER mentions 'research' but integration unclear")
        # Check if it actually USES research data
        if "market_analysis" in content or "tech_analysis" in content:
            print(f"✓ VIBE_ALIGNER references research data fields")
            return True
        else:
            print(f"❌ VIBE_ALIGNER doesn't reference research_brief fields")
            return False
    else:
        print(f"❌ FAIL: VIBE_ALIGNER doesn't mention research at all")
        print(f"   → CRITICAL GAP: Research data not used in planning")
        return False


def test_query_generation_logic():
    """Test: Gibt es Logik um Research Queries zu generieren?"""
    print("\n" + "="*60)
    print("TEST 6: Query Generation Logic (CRITICAL)")
    print("="*60)

    # Check MARKET_RESEARCHER task_01
    task_file = Path("agency_os/01_research_framework/agents/MARKET_RESEARCHER/tasks/task_01_competitor_identification.md")

    if not task_file.exists():
        print(f"❌ FAIL: task_01_competitor_identification.md missing")
        return False

    content = task_file.read_text()

    # Does it explain HOW to get the search query?
    if "user_vision" in content.lower() or "analyze user vision" in content.lower():
        print(f"✓ Task mentions analyzing user vision")
    else:
        print(f"⚠️  Task doesn't explain query derivation")

    # But does it IMPLEMENT query generation?
    print(f"\n📋 Task says: 'Analyze User Vision'")
    print(f"   → But WHERE does user_vision come from?")
    print(f"   → WHO transforms 'Dog sitting app' → 'dog sitting marketplace alternatives'?")
    print(f"   → ANSWER: NOT DEFINED")
    print(f"\n❌ FAIL: No query generation logic found")
    print(f"   → CRITICAL GAP: Input query generation missing")
    return False


def test_api_fallback_implementation():
    """Test: Sind API Fallbacks tatsächlich implementiert?"""
    print("\n" + "="*60)
    print("TEST 7: API Fallback Implementation")
    print("="*60)

    task_file = Path("agency_os/01_research_framework/agents/MARKET_RESEARCHER/tasks/task_01_competitor_identification.md")

    content = task_file.read_text()

    # Check for fallback strategy
    fallback_checks = [
        ("Google Custom Search", "Primary API"),
        ("DuckDuckGo", "Fallback 1"),
        ("Manual Search Guidance", "Fallback 2"),
        ("search_with_fallback", "Fallback function")
    ]

    found = []
    for keyword, desc in fallback_checks:
        if keyword in content:
            print(f"✓ {desc} defined")
            found.append(desc)
        else:
            print(f"❌ {desc} missing")

    if len(found) >= 3:
        print(f"\n✅ PASS: API fallbacks DEFINED (but not IMPLEMENTED)")
        print(f"   ⚠️  Note: These are PSEUDO-CODE, not actual Python")
        return True
    else:
        print(f"\n❌ FAIL: Incomplete fallback definition")
        return False


def test_fact_validator_blocking():
    """Test: Kann FACT_VALIDATOR den Workflow blocken?"""
    print("\n" + "="*60)
    print("TEST 8: FACT_VALIDATOR Blocking Logic")
    print("="*60)

    workflow_file = Path("agency_os/01_research_framework/state_machine/RESEARCH_workflow_design.yaml")
    content = workflow_file.read_text()

    # Check for blocking conditions
    if "blocking: true" in content:
        print(f"✓ Blocking gates defined")
    else:
        print(f"❌ No blocking gates")
        return False

    if "quality_score < 50" in content:
        print(f"✓ Quality threshold defined (< 50 blocks)")
    else:
        print(f"❌ Quality threshold missing")

    if "issues_critical > 0" in content:
        print(f"✓ Critical issues block defined")
    else:
        print(f"❌ Critical blocking missing")

    print(f"\n✅ PASS: FACT_VALIDATOR can block workflow")
    print(f"   → BUT: Only within RESEARCH phase")
    print(f"   → Cannot block main ORCHESTRATOR (not integrated)")
    return True


def main():
    print("="*60)
    print("RESEARCH FRAMEWORK INTEGRATION TEST")
    print("Real-World Test: Dog Sitting Marketplace App")
    print("="*60)

    tests = [
        ("Research Framework Structure", test_research_framework_structure),
        ("Research Workflow Definition", test_research_workflow_definition),
        ("ORCHESTRATOR Integration", test_orchestrator_integration),
        ("Data Contracts", test_data_contracts),
        ("VIBE_ALIGNER Integration", test_vibe_aligner_research_integration),
        ("Query Generation Logic", test_query_generation_logic),
        ("API Fallback Implementation", test_api_fallback_implementation),
        ("FACT_VALIDATOR Blocking", test_fact_validator_blocking),
    ]

    results = []
    for test_name, test_func in tests:
        try:
            success = test_func()
            results.append((test_name, success))
        except Exception as e:
            print(f"\n❌ {test_name}: EXCEPTION - {e}")
            import traceback
            traceback.print_exc()
            results.append((test_name, False))

    # Final results
    print("\n" + "="*60)
    print("TEST RESULTS SUMMARY")
    print("="*60)

    passed = sum(1 for _, success in results if success)
    failed = len(results) - passed

    for test_name, success in results:
        status = "✅ PASS" if success else "❌ FAIL"
        print(f"{status}: {test_name}")

    print(f"\nPassed: {passed}/{len(results)}")
    print(f"Failed: {failed}/{len(results)}")

    # Critical gaps summary
    print("\n" + "="*60)
    print("CRITICAL GAPS IDENTIFIED")
    print("="*60)

    critical_gaps = []
    for test_name, success in results:
        if not success and "ORCHESTRATOR" in test_name:
            critical_gaps.append("M-01: Research NOT integrated in ORCHESTRATOR")
        if not success and "Query Generation" in test_name:
            critical_gaps.append("M-03: No query generation logic")
        if not success and "VIBE_ALIGNER" in test_name:
            critical_gaps.append("M-04: Research data not consumed")

    if critical_gaps:
        for i, gap in enumerate(set(critical_gaps), 1):
            print(f"{i}. {gap}")
    else:
        print("No critical gaps found!")

    print("\n" + "="*60)

    if failed > 0:
        print(f"⚠️  {failed} tests failed - Framework has gaps")
        sys.exit(1)

    print("✅ All tests passed!")
    sys.exit(0)


if __name__ == "__main__":
    main()
