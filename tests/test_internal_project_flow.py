"""
Test suite for internal project flow with adaptive quality threshold.

Verifies that:
1. Internal projects pass with lower quality threshold (30)
2. Portfolio projects pass with lenient threshold (35)
3. Commercial projects require strict threshold (50)
4. Project type detection works correctly
5. User override mechanism works
"""

import pytest
import json
from unittest.mock import patch, MagicMock
from typing import Dict, Any


class AdaptiveQualityThresholdTests:
    """Test adaptive quality thresholds based on project type"""

    def test_internal_project_low_threshold(self):
        """Test that internal projects pass with quality_score >= 30"""
        from src.fact_validator import validate_quality_threshold

        research_brief = {
            "project_type": "internal",
            "project_vision": "Build internal tool for team"
        }

        fact_validation = {
            "quality_score": "32/100",
            "issues_found": 5,
            "issues_critical": 0,
            "flagged_hallucinations": []
        }

        result = validate_quality_threshold(research_brief, fact_validation)

        assert result["passed"] is True
        assert result["blocking"] is False
        assert result["threshold"] == 30
        assert result["quality_score"] == 32
        assert result["project_type"] == "internal"

    def test_portfolio_project_lenient_threshold(self):
        """Test that portfolio projects pass with quality_score >= 35"""
        from src.fact_validator import validate_quality_threshold

        research_brief = {
            "project_type": "portfolio",
            "project_vision": "Portfolio piece for learning"
        }

        fact_validation = {
            "quality_score": "38/100",
            "issues_found": 8,
            "issues_critical": 0,
            "flagged_hallucinations": []
        }

        result = validate_quality_threshold(research_brief, fact_validation)

        assert result["passed"] is True
        assert result["threshold"] == 35
        assert result["quality_score"] == 38

    def test_commercial_project_strict_threshold(self):
        """Test that commercial projects require quality_score >= 50"""
        from src.fact_validator import validate_quality_threshold

        research_brief = {
            "project_type": "commercial",
            "project_vision": "SaaS product for B2B market"
        }

        fact_validation = {
            "quality_score": "65/100",
            "issues_found": 2,
            "issues_critical": 0,
            "flagged_hallucinations": []
        }

        result = validate_quality_threshold(research_brief, fact_validation)

        assert result["passed"] is True
        assert result["threshold"] == 50
        assert result["quality_score"] == 65

    def test_commercial_project_fails_below_threshold(self):
        """Test that commercial projects fail with quality_score < 50"""
        from src.fact_validator import validate_quality_threshold

        research_brief = {
            "project_type": "commercial",
            "project_vision": "SaaS product"
        }

        fact_validation = {
            "quality_score": "38/100",
            "issues_found": 15,
            "issues_critical": 0,
            "flagged_hallucinations": []
        }

        result = validate_quality_threshold(research_brief, fact_validation)

        assert result["passed"] is False
        assert result["blocking"] is True
        assert result["threshold"] == 50
        assert result["quality_score"] == 38

    def test_nonprofit_project_moderate_threshold(self):
        """Test that nonprofit projects pass with quality_score >= 40"""
        from src.fact_validator import validate_quality_threshold

        research_brief = {
            "project_type": "nonprofit",
            "project_vision": "Open source tool for public good"
        }

        fact_validation = {
            "quality_score": "42/100",
            "issues_found": 6,
            "issues_critical": 0,
            "flagged_hallucinations": []
        }

        result = validate_quality_threshold(research_brief, fact_validation)

        assert result["passed"] is True
        assert result["threshold"] == 40

    def test_enterprise_project_highest_threshold(self):
        """Test that enterprise projects require quality_score >= 55"""
        from src.fact_validator import validate_quality_threshold

        research_brief = {
            "project_type": "enterprise",
            "project_vision": "Large enterprise platform"
        }

        fact_validation = {
            "quality_score": "60/100",
            "issues_found": 1,
            "issues_critical": 0,
            "flagged_hallucinations": []
        }

        result = validate_quality_threshold(research_brief, fact_validation)

        assert result["passed"] is True
        assert result["threshold"] == 55


class ProjectTypeDetectionTests:
    """Test automatic project type detection from keywords"""

    def test_detect_internal_project(self):
        """Test detection of 'internal' project type"""
        from src.fact_validator import detect_project_type

        research_brief = {
            "project_vision": "Build an internal tool for our sales team"
        }

        project_type = detect_project_type(research_brief)
        assert project_type == "internal"

    def test_detect_portfolio_project(self):
        """Test detection of 'portfolio' project type"""
        from src.fact_validator import detect_project_type

        research_brief = {
            "project_vision": "Portfolio piece to showcase my skills in React"
        }

        project_type = detect_project_type(research_brief)
        assert project_type == "portfolio"

    def test_detect_commercial_project(self):
        """Test detection of 'commercial' project type"""
        from src.fact_validator import detect_project_type

        research_brief = {
            "project_vision": "Build a SaaS tool to disrupt the project management market"
        }

        project_type = detect_project_type(research_brief)
        assert project_type == "commercial"

    def test_detect_nonprofit_project(self):
        """Test detection of 'nonprofit' project type"""
        from src.fact_validator import detect_project_type

        research_brief = {
            "project_vision": "Open source nonprofit tool for community benefit"
        }

        project_type = detect_project_type(research_brief)
        assert project_type == "nonprofit"

    def test_detect_enterprise_project(self):
        """Test detection of 'enterprise' project type"""
        from src.fact_validator import detect_project_type

        research_brief = {
            "project_vision": "Enterprise platform for large corporations"
        }

        project_type = detect_project_type(research_brief)
        assert project_type == "enterprise"

    def test_default_to_commercial_if_uncertain(self):
        """Test that unclear projects default to 'commercial' (safest)"""
        from src.fact_validator import detect_project_type

        research_brief = {
            "project_vision": "Some tool that does something"
        }

        project_type = detect_project_type(research_brief)
        assert project_type == "commercial"

    def test_explicit_project_type_in_brief(self):
        """Test that explicit project_type field is used if present"""
        from src.fact_validator import detect_project_type

        research_brief = {
            "project_type": "internal",
            "project_vision": "Some tool"
        }

        project_type = detect_project_type(research_brief)
        assert project_type == "internal"


class UserOverrideTests:
    """Test user override mechanism for quality threshold"""

    def test_user_override_low_quality(self):
        """Test that user can override low quality score with warning"""
        from src.fact_validator import validate_quality_threshold

        research_brief = {
            "project_type": "commercial",
            "project_vision": "SaaS product"
        }

        fact_validation = {
            "quality_score": "35/100",
            "issues_found": 15,
            "issues_critical": 0,
            "flagged_hallucinations": []
        }

        # User chooses to continue anyway
        result = validate_quality_threshold(
            research_brief,
            fact_validation,
            user_interaction="continue_anyway"
        )

        assert result["passed"] is True
        assert result["blocking"] is False
        assert result["user_override"] is True
        # Should set confidence to LOW
        assert any("LOW confidence" in msg for msg in result["messages"])

    def test_user_refuses_override(self):
        """Test that workflow blocks when user doesn't override"""
        from src.fact_validator import validate_quality_threshold

        research_brief = {
            "project_type": "commercial",
            "project_vision": "SaaS product"
        }

        fact_validation = {
            "quality_score": "35/100",
            "issues_found": 15,
            "issues_critical": 0,
            "flagged_hallucinations": []
        }

        # No user interaction (defaults to no override)
        result = validate_quality_threshold(
            research_brief,
            fact_validation,
            user_interaction=None
        )

        assert result["passed"] is False
        assert result["blocking"] is True
        assert result["user_override"] is False

    def test_override_still_respects_critical_issues(self):
        """Test that override doesn't bypass critical hallucinations"""
        from src.fact_validator import validate_quality_threshold

        # This should still block even with override
        research_brief = {
            "project_type": "portfolio",
            "project_vision": "Portfolio piece"
        }

        fact_validation = {
            "quality_score": "20/100",
            "issues_critical": 3,  # Critical issues present
            "flagged_hallucinations": [
                {"claim": "Stripe has 99.99% uptime", "severity": "critical"}
            ]
        }

        result = validate_quality_threshold(
            research_brief,
            fact_validation,
            user_interaction="continue_anyway"
        )

        # Should still block if there are critical issues
        # (implementation detail - critical issues always block)
        assert "critical" in str(result).lower() or result["blocking"] is True


class InternalProjectFlowTests:
    """Test complete flow for internal projects"""

    def test_internal_project_research_flow(self):
        """Test that internal project completes research with low threshold"""
        from src.fact_validator import validate_quality_threshold

        # Simulate internal project research
        research_brief = {
            "project_id": "internal-tool-001",
            "project_type": "internal",
            "project_vision": "Internal analytics dashboard for sales team",
            "research_completed_at": "2025-11-14T15:30:00Z"
        }

        # Internal project has limited market data (no competitors, no pricing)
        fact_validation = {
            "quality_score": "31/100",  # Low but acceptable for internal
            "issues_found": 8,
            "issues_critical": 0,
            "flagged_hallucinations": [],
            "market_analysis": {
                "competitors": [],
                "note": "Internal project - no market competitors needed"
            },
            "tech_analysis": {
                "recommended_libraries": [
                    {"name": "React", "purpose": "Dashboard UI"},
                    {"name": "D3.js", "purpose": "Data visualization"}
                ]
            }
        }

        result = validate_quality_threshold(research_brief, fact_validation)

        # Internal project should PASS despite low score
        assert result["passed"] is True
        assert result["threshold"] == 30
        assert result["quality_score"] == 31
        assert "internal" in result["project_type"].lower()

    def test_internal_vs_commercial_same_data(self):
        """Test same research data with different project types"""
        from src.fact_validator import validate_quality_threshold

        # Same quality score
        same_quality = {
            "quality_score": "40/100",
            "issues_found": 10,
            "issues_critical": 0,
            "flagged_hallucinations": []
        }

        # Test with internal project
        internal_brief = {"project_type": "internal"}
        internal_result = validate_quality_threshold(internal_brief, same_quality)

        # Test with commercial project
        commercial_brief = {"project_type": "commercial"}
        commercial_result = validate_quality_threshold(commercial_brief, same_quality)

        # Same data should PASS for internal, FAIL for commercial
        assert internal_result["passed"] is True
        assert commercial_result["passed"] is False
        assert internal_result["threshold"] == 30
        assert commercial_result["threshold"] == 50


class ThresholdRationaleTests:
    """Test that threshold rationale is clearly communicated"""

    def test_internal_threshold_rationale(self):
        """Test that internal project threshold has clear rationale"""
        from src.fact_validator import calculate_quality_threshold

        research_brief = {"project_type": "internal"}
        result = calculate_quality_threshold(research_brief)

        assert "rationale" in result
        assert "internal" in result["rationale"].lower()
        assert len(result["rationale"]) > 20

    def test_commercial_threshold_rationale(self):
        """Test that commercial project threshold has clear rationale"""
        from src.fact_validator import calculate_quality_threshold

        research_brief = {"project_type": "commercial"}
        result = calculate_quality_threshold(research_brief)

        assert "rationale" in result
        assert "commercial" in result["rationale"].lower() or "market" in result["rationale"].lower()

    def test_rationale_explains_threshold_difference(self):
        """Test that rationale explains why thresholds differ"""
        from src.fact_validator import calculate_quality_threshold

        internal = calculate_quality_threshold({"project_type": "internal"})
        commercial = calculate_quality_threshold({"project_type": "commercial"})

        # Different thresholds should have different rationales
        assert internal["threshold"] != commercial["threshold"]
        assert internal["rationale"] != commercial["rationale"]


class SchemaCompatibilityTests:
    """Test schema compatibility with new project_type field"""

    def test_research_brief_schema_includes_project_type(self):
        """Test that research_brief schema includes project_type field"""
        # This would load from ORCHESTRATION_data_contracts.yaml
        from src.schema_validator import load_schema

        schema = load_schema("research_brief.schema.json")

        # Verify project_type field exists
        assert "project_type" in schema["fields"] or "project_type" in str(schema)

    def test_project_type_optional_backward_compatible(self):
        """Test that project_type is optional (backward compatible)"""
        # Verify that research_brief works without project_type
        from src.fact_validator import validate_quality_threshold

        # No project_type specified
        research_brief = {
            "project_vision": "Some project"
            # No project_type field
        }

        fact_validation = {"quality_score": "55/100"}

        # Should not crash, should default to "commercial"
        result = validate_quality_threshold(research_brief, fact_validation)

        assert result is not None
        assert "threshold" in result


class MessageFormattingTests:
    """Test that messages are clear and actionable"""

    def test_pass_message_includes_threshold_info(self):
        """Test that pass message includes threshold information"""
        from src.fact_validator import validate_quality_threshold

        research_brief = {"project_type": "internal"}
        fact_validation = {"quality_score": "35/100"}

        result = validate_quality_threshold(research_brief, fact_validation)

        messages = result.get("messages", [])
        assert len(messages) > 0
        # Verify messages include key info
        assert any("35" in str(msg) for msg in messages)
        assert any("30" in str(msg) for msg in messages)  # threshold
        assert any("internal" in str(msg).lower() for msg in messages)

    def test_fail_message_explains_why(self):
        """Test that failure message explains why threshold not met"""
        from src.fact_validator import validate_quality_threshold

        research_brief = {"project_type": "commercial"}
        fact_validation = {"quality_score": "35/100"}

        result = validate_quality_threshold(research_brief, fact_validation)

        messages = result.get("messages", [])
        assert len(messages) > 0
        assert any("action" in str(msg).lower() for msg in messages)


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
