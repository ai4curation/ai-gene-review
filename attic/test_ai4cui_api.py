"""Tests for AI4CUI FastAPI backend.

Following FastAPI testing best practices:
- Use TestClient for synchronous tests
- Test endpoints independently
- Use fixtures for test data
- Test error conditions
- Verify response schemas
"""

import pytest
from fastapi.testclient import TestClient
from pathlib import Path
from unittest.mock import Mock, patch
from datetime import datetime

from ai4cui.api import app, status_cache, cache_timestamp
from ai4cui.models import JobStatus, JobStatusEnum, CriteriaResult
from ai4cui.plugin import CurationPlugin
from ai4cui.models import Job, ProgressCriteria


class MockPlugin(CurationPlugin):
    """Mock plugin for testing."""

    def __init__(self):
        """Initialize with test data."""
        self.jobs = {
            "test/job1": Job(
                job_id="test/job1",
                display_name="Test Job 1",
                directory="/tmp/test/job1",
                description="Test job 1"
            ),
            "test/job2": Job(
                job_id="test/job2",
                display_name="Test Job 2",
                directory="/tmp/test/job2",
                description="Test job 2"
            ),
        }

    def get_all_job_ids(self):
        """Return test job IDs."""
        return list(self.jobs.keys())

    def get_job(self, job_id: str):
        """Get test job."""
        return self.jobs.get(job_id)

    def get_job_directory(self, job_id: str):
        """Get job directory."""
        return Path(self.jobs[job_id].directory)

    def get_progress_criteria(self, job_id: str):
        """Return mock criteria."""
        return [
            ProgressCriteria(
                name="Test Criterion 1",
                description="Test criterion 1",
                check=lambda jid: CriteriaResult(met=True, message="Test passed"),
                weight=1.0,
            ),
            ProgressCriteria(
                name="Test Criterion 2",
                description="Test criterion 2",
                check=lambda jid: CriteriaResult(met=False, message="Test failed", hint="Fix the test"),
                weight=1.0,
            ),
        ]

    def compute_job_status(self, job_id: str, agent_port=None):
        """Compute mock job status."""
        criteria = self.get_progress_criteria(job_id)
        results = [c.check(job_id) for c in criteria]

        progress = sum(1 for r in results if r.met) / len(results) * 100 if results else 0

        return JobStatus(
            job_id=job_id,
            status=JobStatusEnum.IN_PROGRESS,
            progress_percent=progress,
            criteria_results=results,
            agent_port=agent_port,
        )

    def get_initial_instructions(self, job_id: str):
        """Return mock instructions."""
        return f"Please work on {job_id}"


@pytest.fixture
def mock_plugin():
    """Create mock plugin fixture."""
    return MockPlugin()


@pytest.fixture
def client(mock_plugin):
    """Create test client with mock plugin."""
    # Inject mock plugin into app
    import ai4cui.api
    original_plugin = ai4cui.api.plugin_instance
    original_manager = ai4cui.api.job_manager

    # Set mock plugin
    ai4cui.api.plugin_instance = mock_plugin
    from ai4cui.job_manager import JobManager
    ai4cui.api.job_manager = JobManager(mock_plugin)

    # Load mock cache
    ai4cui.api.status_cache = {
        "test/job1": mock_plugin.compute_job_status("test/job1"),
        "test/job2": mock_plugin.compute_job_status("test/job2"),
    }
    ai4cui.api.cache_timestamp = datetime.now().timestamp()

    # Create client
    with TestClient(app) as test_client:
        yield test_client

    # Restore original plugin
    ai4cui.api.plugin_instance = original_plugin
    ai4cui.api.job_manager = original_manager


class TestHealthEndpoint:
    """Tests for /health endpoint."""

    def test_health_check_success(self, client):
        """Test health check returns 200."""
        response = client.get("/health")
        assert response.status_code == 200

        data = response.json()
        assert data["status"] == "ok"
        assert "cache_size" in data
        assert "cache_age_seconds" in data

    def test_health_check_has_cache_info(self, client):
        """Test health check includes cache information."""
        response = client.get("/health")
        data = response.json()

        assert data["cache_size"] == 2  # Two test jobs
        assert isinstance(data["cache_age_seconds"], (int, float))


class TestStatsEndpoint:
    """Tests for /stats endpoint."""

    def test_stats_success(self, client):
        """Test stats endpoint returns correct data."""
        response = client.get("/stats")
        assert response.status_code == 200

        data = response.json()
        assert data["total_jobs"] == 2
        assert data["active_agents"] == 0  # No agents in test
        assert "cache_age_seconds" in data
        assert "last_refresh" in data

    def test_stats_schema(self, client):
        """Test stats response matches schema."""
        response = client.get("/stats")
        data = response.json()

        # Verify all required fields
        required_fields = ["total_jobs", "active_agents", "cache_age_seconds", "last_refresh"]
        for field in required_fields:
            assert field in data, f"Missing field: {field}"

        # Verify types
        assert isinstance(data["total_jobs"], int)
        assert isinstance(data["active_agents"], int)
        assert isinstance(data["cache_age_seconds"], (int, float))
        assert isinstance(data["last_refresh"], str)


class TestJobsEndpoint:
    """Tests for /jobs endpoint."""

    def test_list_jobs_success(self, client):
        """Test listing all jobs."""
        response = client.get("/jobs")
        assert response.status_code == 200

        data = response.json()
        assert isinstance(data, list)
        assert len(data) == 2

    def test_job_summary_schema(self, client):
        """Test job summary has correct schema."""
        response = client.get("/jobs")
        data = response.json()

        job = data[0]
        required_fields = ["job_id", "display_name", "progress_percent", "status", "has_agent"]
        for field in required_fields:
            assert field in job, f"Missing field: {field}"

    def test_job_summary_values(self, client):
        """Test job summary has correct values."""
        response = client.get("/jobs")
        data = response.json()

        # Find test/job1
        job1 = next(j for j in data if j["job_id"] == "test/job1")

        assert job1["display_name"] == "Test Job 1"
        assert job1["progress_percent"] == 50.0  # 1 of 2 criteria passed
        assert job1["status"] == "in_progress"
        assert job1["has_agent"] is False
        assert job1["agent_port"] is None


class TestJobDetailEndpoint:
    """Tests for /jobs/{job_id} endpoint."""

    def test_get_job_success(self, client):
        """Test getting specific job details."""
        response = client.get("/jobs/test/job1")
        assert response.status_code == 200

        data = response.json()
        assert data["job_id"] == "test/job1"
        assert data["display_name"] == "Test Job 1"

    def test_get_job_not_found(self, client):
        """Test 404 for non-existent job."""
        response = client.get("/jobs/test/nonexistent")
        assert response.status_code == 404

        data = response.json()
        assert "not found" in data["detail"].lower()

    def test_job_detail_schema(self, client):
        """Test job detail response schema."""
        response = client.get("/jobs/test/job1")
        data = response.json()

        required_fields = [
            "job_id", "display_name", "status", "progress_percent",
            "has_agent", "criteria_results"
        ]
        for field in required_fields:
            assert field in data, f"Missing field: {field}"

    def test_job_criteria_results(self, client):
        """Test criteria results in job detail."""
        response = client.get("/jobs/test/job1")
        data = response.json()

        criteria = data["criteria_results"]
        assert len(criteria) == 2

        # First criterion should pass
        assert criteria[0]["name"] == "Test Criterion 1"
        assert criteria[0]["met"] is True
        assert criteria[0]["message"] == "Test passed"

        # Second criterion should fail with hint
        assert criteria[1]["name"] == "Test Criterion 2"
        assert criteria[1]["met"] is False
        assert criteria[1]["message"] == "Test failed"
        assert criteria[1]["hint"] == "Fix the test"

    def test_job_detail_path_with_slash(self, client):
        """Test job ID with slash in path."""
        response = client.get("/jobs/test/job1")
        assert response.status_code == 200

        data = response.json()
        assert data["job_id"] == "test/job1"


class TestRefreshEndpoints:
    """Tests for cache refresh endpoints."""

    def test_refresh_single_job(self, client, mock_plugin):
        """Test refreshing a single job."""
        response = client.post("/jobs/test/job1/refresh")
        assert response.status_code == 200

        data = response.json()
        assert data["status"] == "ok"
        assert data["job_id"] == "test/job1"

    def test_refresh_nonexistent_job(self, client):
        """Test refreshing non-existent job returns 404."""
        response = client.post("/jobs/test/nonexistent/refresh")
        assert response.status_code == 404

    def test_refresh_all_cache(self, client):
        """Test refreshing entire cache."""
        response = client.post("/cache/refresh")
        assert response.status_code == 200

        data = response.json()
        assert data["status"] == "ok"
        assert "jobs_refreshed" in data
        assert "elapsed_seconds" in data
        assert data["jobs_refreshed"] == 2


class TestErrorHandling:
    """Tests for error handling."""

    def test_invalid_endpoint(self, client):
        """Test 404 for invalid endpoint."""
        response = client.get("/invalid/endpoint")
        assert response.status_code == 404

    def test_method_not_allowed(self, client):
        """Test 405 for wrong HTTP method."""
        response = client.post("/health")  # GET only
        assert response.status_code == 405


class TestCORS:
    """Tests for CORS middleware."""

    def test_cors_headers_present(self, client):
        """Test CORS headers are present."""
        response = client.options("/health")

        # CORS headers should be present
        assert "access-control-allow-origin" in response.headers

    def test_cors_allows_all_origins(self, client):
        """Test CORS allows all origins (for localhost development)."""
        response = client.options(
            "/health",
            headers={"Origin": "http://localhost:5123"}
        )

        assert response.headers.get("access-control-allow-origin") == "*"


class TestCachePerformance:
    """Tests for cache performance characteristics."""

    def test_cache_is_fast(self, client):
        """Test that cached endpoints respond quickly."""
        import time

        start = time.time()
        response = client.get("/jobs")
        elapsed = time.time() - start

        assert response.status_code == 200
        # Should be < 100ms for cached data
        assert elapsed < 0.1, f"Response took {elapsed:.3f}s, expected < 0.1s"

    def test_multiple_requests_use_cache(self, client):
        """Test that multiple requests use the same cache."""
        # First request
        response1 = client.get("/jobs/test/job1")
        data1 = response1.json()

        # Second request (should use cache)
        response2 = client.get("/jobs/test/job1")
        data2 = response2.json()

        # Data should be identical (same cache)
        assert data1 == data2


class TestAPIDocumentation:
    """Tests for API documentation."""

    def test_openapi_schema_available(self, client):
        """Test OpenAPI schema is available."""
        response = client.get("/openapi.json")
        assert response.status_code == 200

        schema = response.json()
        assert "openapi" in schema
        assert "info" in schema
        assert schema["info"]["title"] == "AI4CUI API"

    def test_docs_available(self, client):
        """Test Swagger docs are available."""
        response = client.get("/docs")
        assert response.status_code == 200
        assert b"swagger" in response.content.lower()

    def test_redoc_available(self, client):
        """Test ReDoc is available."""
        response = client.get("/redoc")
        assert response.status_code == 200
        assert b"redoc" in response.content.lower()


# Integration test markers
pytestmark = pytest.mark.integration


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
