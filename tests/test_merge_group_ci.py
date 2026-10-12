"""Protect the required integration check and cancellation boundaries."""

from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]


def test_queue_runs_required_check_without_cancelling_other_groups():
    workflow = yaml.safe_load((ROOT / ".github/workflows/main.yaml").read_text())
    assert "merge_group" in workflow.get("on", workflow.get(True))
    assert workflow["jobs"]["test"]["strategy"]["matrix"]["python-version"] == ["3.12"]
    concurrency = workflow["concurrency"]
    assert concurrency["cancel-in-progress"] == (
        "${{ github.event_name == 'pull_request' || github.event_name == 'push' }}"
    )
    assert "(github.event_name == 'push' && github.ref)" in concurrency["group"]
    assert "github.run_id" in concurrency["group"]
    steps = workflow["jobs"]["test"]["steps"]
    assert next(s for s in steps if s.get("id") == "changes")["uses"] == "dorny/paths-filter@v4"
    for name in ("Run test suite", "Test valid/invalid examples", "Check agentic automation",
                 "Validate modules (scoped)", "Validate family reviews (scoped)",
                 "Validate history records (scoped)",
                 "Fetch benchmark baseline and review snapshot commits",
                 "Validate all gene schemas (merge queue)"):
        step = next(s for s in steps if s.get("name") == name)
        assert "github.event_name == 'merge_group'" in step["if"]
    paint = next(s for s in steps if s.get("name", "").startswith("Verify PAINT slices"))
    assert "merge_group" not in paint["if"]


def test_queue_rollout_is_bounded_and_does_not_bypass_protection():
    config = yaml.safe_load((ROOT / ".github/merge-queue-ruleset.yaml").read_text())
    assert config["bypass_actors"] == []
    assert config["conditions"]["ref_name"]["include"] == ["refs/heads/main"]
    rule, = config["rules"]
    assert rule["type"] == "merge_queue"
    assert rule["parameters"]["max_entries_to_build"] == 1
    assert rule["parameters"]["max_entries_to_merge"] == 1
    assert rule["parameters"]["grouping_strategy"] == "ALLGREEN"
    assert rule["parameters"]["check_response_timeout_minutes"] == 360
