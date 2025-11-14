"""
Test suite for API fallback mechanisms.

Verifies that the framework handles API failures gracefully without crashing:
- GitHub API rate limit → npm registry fallback
- Google Custom Search quota exceeded → DuckDuckGo fallback
- Both APIs fail → Manual check placeholders
"""

import pytest
import json
from unittest.mock import patch, MagicMock
from typing import Dict, List, Any


class GitHubAPIFallbackTests:
    """Test GitHub API fallback chain: GitHub API → npm registry → manual check"""

    @patch('github_api.get_repo_stats')
    def test_github_api_success(self, mock_github):
        """Test successful GitHub API call"""
        mock_github.return_value = {
            "source": "github_api",
            "stars": 15000,
            "watchers": 500,
            "forks": 2000,
            "last_updated": "2025-11-14T10:30:00Z",
            "language": "Python"
        }

        # Should return GitHub metrics without fallback
        from src.tech_researcher import get_library_info_with_fallback
        result = get_library_info_with_fallback(
            library_name="pytest",
            github_url="https://github.com/pytest-dev/pytest"
        )

        assert result["source"] == "github_api"
        assert result["stars"] == 15000
        assert result["reliability"] == "high"

    @patch('github_api.get_repo_stats')
    def test_github_rate_limit_triggers_npm_fallback(self, mock_github):
        """Test that GitHub rate limit triggers npm registry fallback"""
        mock_github.side_effect = Exception("GitHub rate limit exceeded (60/hour)")

        with patch('npm_registry.get_package_info') as mock_npm:
            mock_npm.return_value = {
                "source": "npm_registry",
                "package_name": "pytest",
                "downloads_weekly": 50000000,
                "maintainers": ["maintainer1"],
                "note": "GitHub metrics unavailable - using npm data as proxy"
            }

            from src.tech_researcher import get_library_info_with_fallback
            result = get_library_info_with_fallback(
                library_name="pytest",
                github_url="https://github.com/pytest-dev/pytest"
            )

            assert result["source"] == "npm_registry"
            assert result["reliability"] == "medium"
            assert "fallback_reason" in result
            assert "GitHub rate limit" in result["fallback_reason"]

    @patch('github_api.get_repo_stats')
    @patch('npm_registry.get_package_info')
    def test_both_apis_fail_return_manual_placeholder(self, mock_npm, mock_github):
        """Test that both API failures return actionable manual check placeholder"""
        mock_github.side_effect = Exception("GitHub API rate limit")
        mock_npm.side_effect = Exception("npm registry unreachable")

        from src.tech_researcher import get_library_info_with_fallback
        result = get_library_info_with_fallback(
            library_name="pytest",
            github_url="https://github.com/pytest-dev/pytest"
        )

        assert result["source"] == "manual_check_required"
        assert result["reliability"] == "low"
        assert result["stars"] == "UNKNOWN"
        assert result["status"] == "API_UNAVAILABLE"
        assert "how_to_verify" in result
        assert isinstance(result["how_to_verify"], list)
        assert len(result["how_to_verify"]) > 0
        # Verify GitHub URL is included in manual check
        assert any("github.com/pytest-dev/pytest" in item for item in result["how_to_verify"])

    @patch('github_api.get_repo_stats')
    def test_repository_not_found_404_handled(self, mock_github):
        """Test that 404 (deleted repository) returns manual check, not crash"""
        mock_github.side_effect = Exception("Repository not found (404)")

        from src.tech_researcher import get_library_info_with_fallback
        result = get_library_info_with_fallback(
            library_name="deleted-lib",
            github_url="https://github.com/deleted-account/deleted-repo"
        )

        # Should not crash, should provide manual check
        assert result["source"] == "manual_check_required"
        assert result["reliability"] == "low"
        assert "repository_not_found" in result.get("error", "")

    def test_task_completes_without_crash(self):
        """Test that task_03_library_comparison completes even with API failures"""
        # Simulate task processing with multiple libraries, some failing
        libraries = [
            {"name": "React", "github_url": "https://github.com/facebook/react"},
            {"name": "axios", "github_url": "https://github.com/axios/axios"},
            {"name": "lodash", "github_url": "https://github.com/lodash/lodash"}
        ]

        with patch('github_api.get_repo_stats') as mock_github:
            # First call succeeds, others fail
            mock_github.side_effect = [
                {"source": "github_api", "stars": 220000},
                Exception("rate_limit"),
                Exception("rate_limit")
            ]

            with patch('npm_registry.get_package_info') as mock_npm:
                mock_npm.side_effect = [
                    {"source": "npm_registry", "downloads_weekly": 50000000},
                    Exception("npm unavailable")
                ]

                from src.tech_researcher import process_libraries
                result = process_libraries(libraries)

                # Task should complete without crashing
                assert result is not None
                assert len(result) == 3
                assert result[0]["source"] == "github_api"
                assert result[1]["source"] == "npm_registry"
                assert result[2]["source"] == "manual_check_required"


class GoogleSearchAPIFallbackTests:
    """Test Google Custom Search fallback chain: Google → DuckDuckGo → manual"""

    @patch('google_custom_search.search')
    def test_google_search_success(self, mock_google):
        """Test successful Google Custom Search call"""
        mock_google.return_value = [
            {"title": "Asana", "link": "https://asana.com", "snippet": "..."},
            {"title": "Monday.com", "link": "https://monday.com", "snippet": "..."}
        ]

        from src.market_researcher import search_with_fallback
        result = search_with_fallback(
            query="project management software",
            google_api_key="test_key",
            search_engine_id="test_id"
        )

        assert result["source"] == "google_custom_search"
        assert result["reliability"] == "high"
        assert len(result["results"]) == 2

    @patch('google_custom_search.search')
    def test_google_quota_exceeded_triggers_duckduckgo(self, mock_google):
        """Test that Google quota exceeded triggers DuckDuckGo fallback"""
        mock_google.side_effect = Exception("Google quota exceeded (100/day)")

        with patch('duckduckgo_search.search') as mock_ddg:
            mock_ddg.return_value = [
                {"title": "Asana", "link": "https://asana.com", "snippet": "..."},
                {"title": "Monday.com", "link": "https://monday.com", "snippet": "..."}
            ]

            from src.market_researcher import search_with_fallback
            result = search_with_fallback(
                query="project management software"
            )

            assert result["source"] == "duckduckgo"
            assert result["reliability"] == "medium"
            assert "fallback_reason" in result
            assert "Google quota" in result["fallback_reason"]

    @patch('google_custom_search.search')
    @patch('duckduckgo_search.search')
    def test_both_search_apis_fail_return_manual(self, mock_ddg, mock_google):
        """Test that both search APIs failing returns manual search guidance"""
        mock_google.side_effect = Exception("Google quota exceeded")
        mock_ddg.side_effect = Exception("DuckDuckGo unavailable")

        from src.market_researcher import search_with_fallback
        result = search_with_fallback(query="project management software")

        assert result["source"] == "manual_search_required"
        assert result["reliability"] == "low"
        assert len(result.get("results", [])) == 0
        assert "manual_instructions" in result
        assert "manual_instructions" in result or "search_keywords" in result

    def test_task_completes_without_crash(self):
        """Test that competitor identification completes even with API failures"""
        queries = [
            "project management software",
            "alternative to Asana",
            "team collaboration tools"
        ]

        with patch('google_custom_search.search') as mock_google:
            # First call succeeds, others fail quota
            mock_google.side_effect = [
                [{"title": "Asana", "link": "https://asana.com"}],
                Exception("Google quota exceeded"),
                Exception("Google quota exceeded")
            ]

            with patch('duckduckgo_search.search') as mock_ddg:
                mock_ddg.side_effect = [
                    [{"title": "Monday.com", "link": "https://monday.com"}],
                    Exception("DuckDuckGo unavailable")
                ]

                from src.market_researcher import search_competitors
                result = search_competitors(queries)

                # Task should complete without crashing
                assert result is not None
                assert len(result) == 3
                assert result[0]["source"] == "google_custom_search"
                assert result[1]["source"] == "duckduckgo"
                assert result[2]["source"] == "manual_search_required"


class LoggingAndMetricsTests:
    """Verify API fallback logging and metrics tracking"""

    def test_fallback_metrics_captured(self):
        """Test that fallback metrics are properly recorded"""
        from src.tech_researcher import process_libraries

        with patch('github_api.get_repo_stats') as mock_github:
            mock_github.side_effect = [
                {"source": "github_api", "stars": 15000},
                Exception("rate_limit"),
                Exception("rate_limit")
            ]

            libraries = [
                {"name": "React", "github_url": "https://github.com/facebook/react"},
                {"name": "axios", "github_url": "https://github.com/axios/axios"},
                {"name": "lodash", "github_url": "https://github.com/lodash/lodash"}
            ]

            with patch('npm_registry.get_package_info') as mock_npm:
                mock_npm.side_effect = [
                    {"source": "npm_registry"},
                    Exception("npm unavailable")
                ]

                result, metrics = process_libraries(libraries, return_metrics=True)

                # Verify metrics captured
                assert metrics["total_libraries"] == 3
                assert metrics["github_api_success"] == 1
                assert metrics["npm_fallback_used"] == 1
                assert metrics["manual_check_used"] == 1
                assert metrics["fallback_rate"] == "66.7%"

    def test_all_failures_logged(self):
        """Test that all API failures are logged with context"""
        from src.tech_researcher import get_library_info_with_fallback

        with patch('github_api.get_repo_stats') as mock_github:
            mock_github.side_effect = Exception("Rate limit")

            with patch('npm_registry.get_package_info') as mock_npm:
                mock_npm.side_effect = Exception("npm unavailable")

                with patch('logging.warning') as mock_log:
                    result = get_library_info_with_fallback(
                        "pytest",
                        "https://github.com/pytest-dev/pytest"
                    )

                    # Verify logging happened
                    assert mock_log.called
                    # Should log both failures
                    assert any("rate_limit" in str(call) for call in mock_log.call_args_list)


class EdgeCaseTests:
    """Test edge cases and error conditions"""

    def test_network_timeout_handled(self):
        """Test that network timeouts are handled gracefully"""
        with patch('github_api.get_repo_stats') as mock_github:
            mock_github.side_effect = TimeoutError("Connection timeout")

            from src.tech_researcher import get_library_info_with_fallback
            result = get_library_info_with_fallback(
                "pytest",
                "https://github.com/pytest-dev/pytest"
            )

            # Should provide fallback, not crash
            assert result is not None
            assert "error" in result or "fallback_reason" in result

    def test_invalid_github_url_handled(self):
        """Test that invalid GitHub URLs are handled"""
        from src.tech_researcher import get_library_info_with_fallback

        result = get_library_info_with_fallback(
            "test-lib",
            "not-a-valid-url"
        )

        assert result is not None
        assert "source" in result
        assert result["reliability"] in ["low", "medium", "high"]

    def test_empty_api_response_handled(self):
        """Test that empty API responses don't cause crashes"""
        with patch('google_custom_search.search') as mock_google:
            mock_google.return_value = []  # Empty results

            from src.market_researcher import search_with_fallback
            result = search_with_fallback("obscure-project")

            # Should not crash on empty response
            assert result is not None
            assert isinstance(result["results"], list)


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
