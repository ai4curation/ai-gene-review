"""Exercise retry writes, backoff, supersession and workflow isolation."""

import importlib.util
import subprocess
from datetime import datetime, timedelta, timezone
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "retry_reviews", ROOT / "scripts/retry_failed_reviews.py"
)
assert SPEC is not None and SPEC.loader is not None
retry = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(retry)
UTC = timezone.utc
NOW = datetime(2026, 9, 6, 12, tzinfo=UTC)


def run(**overrides):
    row = {
        "id": 20,
        "event": "pull_request",
        "status": "completed",
        "conclusion": "failure",
        "head_sha": "abc",
        "run_attempt": 1,
        "pull_requests": [{"number": 7}],
        "created_at": (NOW - timedelta(hours=5)).isoformat(),
        "updated_at": (NOW - timedelta(hours=2)).isoformat(),
    }
    return row | overrides


def pr(**overrides):
    # These are deliberately the opposite of merge eligibility.
    return {
        "state": "open",
        "draft": True,
        "user": {"login": "human"},
        "assignees": [{"login": "human"}],
        "base": {"repo": {"full_name": "owner/repo"}},
        "head": {"sha": "abc", "ref": "feature", "repo": {"full_name": "owner/repo"}},
    } | overrides


def reason(row=None, pull=None, peers=(), reviews=()):
    return retry.skip_reason(row or run(), pull or pr(), peers, reviews, NOW, 1, "owner/repo")


def test_human_owned_assigned_draft_can_be_retried():
    assert reason() is None


@pytest.mark.parametrize(
    "attempt,hours,eligible",
    [
        (1, 0.5, False),
        (1, 1, True),
        (2, 5, False),
        (2, 6, True),
        (3, 23, False),
        (3, 24, True),
        (8, 24, True),
    ],
)
def test_backoff_uses_latest_attempt_completion(attempt, hours, eligible):
    row = run(
        run_attempt=attempt, updated_at=(NOW - timedelta(hours=hours)).isoformat()
    )
    assert (reason(row) is None) == eligible


@pytest.mark.parametrize(
    "changes",
    [
        {"status": "queued", "conclusion": None},
        {"status": "in_progress", "conclusion": None},
        {"conclusion": "success"},
        {"conclusion": "cancelled"},
        {"conclusion": "skipped"},
        {"run_attempt": 50},
        {"created_at": (NOW - timedelta(days=30)).isoformat()},
        {"head_sha": "old"},
    ],
)
def test_ineligible_attempts_are_not_retried(changes):
    assert reason(run(**changes))


def test_closed_pr_and_superseding_reviews():
    assert reason(pull=pr(state="closed"))
    assert reason(peers=[run(id=21, status="in_progress", conclusion=None)])
    assert reason(peers=[run(id=21, created_at=(NOW - timedelta(hours=1)).isoformat())])
    assert reason(peers=[run(id=21, conclusion="success", updated_at=NOW.isoformat())])
    assert reason(peers=[run(id=21, conclusion="skipped")]) is None


@pytest.mark.parametrize("state", ["APPROVED", "CHANGES_REQUESTED"])
def test_current_bot_verdict_stops_retry_but_old_verdict_does_not(state):
    review = {
        "id": 1,
        "user": {"login": "ai4c-reviewer[bot]"},
        "state": state,
        "commit_id": "abc",
    }
    assert reason(reviews=[review])
    assert reason(reviews=[review | {"commit_id": "old"}]) is None
    assert reason(reviews=[review | {"state": "DISMISSED"}]) is None


def test_manual_run_is_rerunnable_despite_main_sha():
    assert reason(run(event="workflow_dispatch", head_sha="main-sha")) is None


@pytest.mark.parametrize("event", ["pull_request", "workflow_dispatch", "issue_comment"])
def test_generated_artifacts_are_not_retried(event):
    generated = pr(head=pr()["head"] | {"ref": "auto/generate-project-pages"})
    assert "generated artifacts" in reason(run(event=event), generated)


def test_automatic_fork_review_is_excluded_but_existing_manual_review_is_authorized():
    fork = pr(head=pr()["head"] | {"repo": {"full_name": "contributor/fork"}})
    assert "fork PRs" in reason(pull=fork)
    assert reason(run(event="workflow_dispatch", head_sha="main-sha"), fork) is None
    assert reason(run(event="issue_comment", head_sha="main-sha"), fork) is None


def test_missing_or_wrong_repository_metadata_fails_closed():
    assert reason(pull=pr(base={"repo": {"full_name": "other/repo"}}))
    assert reason(pull=pr(base={}))
    assert reason(pull=pr(head=pr()["head"] | {"repo": None}))


def harness(monkeypatch, rows=None, current=None, reviews=None, fresh=None):
    rows = rows or [run()]
    writes = []
    monkeypatch.setenv("GH_RETRY_TOKEN", "writer")
    monkeypatch.setattr(retry, "workflow_runs", lambda *args: list(rows))
    monkeypatch.setattr(retry, "pages", lambda *args: reviews or [])

    def read(path):
        if "/actions/runs/" in path:
            return current or next(r for r in rows if path.endswith(str(r["id"])))
        if "/pulls/" in path:
            repo = path.split("/pulls/")[0].removeprefix("repos/")
            return pr(
                base={"repo": {"full_name": repo}},
                head={"sha": "abc", "ref": "feature", "repo": {"full_name": repo}},
            )
        if "/workflows/" in path:
            return {"workflow_runs": fresh or rows}
        raise AssertionError(path)

    monkeypatch.setattr(retry, "api", read)
    monkeypatch.setattr(
        retry, "gh", lambda *args, **kwargs: writes.append((args, kwargs))
    )
    return writes


def test_sweep_issues_exact_failed_job_rerun(monkeypatch):
    writes = harness(monkeypatch)
    rows, errors = retry.sweep("owner/repo", NOW, dry_run=False)
    assert errors == 0
    assert writes == [
        (("run", "rerun", "20", "--failed", "--repo", "owner/repo"), {"write": True})
    ]
    assert "retried failed jobs" in rows[0]


@pytest.mark.parametrize(
    "kwargs", [{"dry_run": True}, {"limit": 0}, {"specific_pr": 8}]
)
def test_dry_run_zero_budget_and_specific_pr_never_write(monkeypatch, kwargs):
    writes = harness(monkeypatch)
    retry.sweep("owner/repo", NOW, **({"dry_run": False} | kwargs))
    assert not writes


def test_manual_retry_started_since_discovery_is_left_alone(monkeypatch):
    writes = harness(
        monkeypatch, current=run(status="queued", conclusion=None, run_attempt=2)
    )
    retry.sweep("owner/repo", NOW, dry_run=False)
    assert not writes


def test_new_review_arriving_during_sweep_prevents_retry(monkeypatch):
    writes = harness(
        monkeypatch, fresh=[run(id=30, status="in_progress", conclusion=None)]
    )
    retry.sweep("owner/repo", NOW, dry_run=False)
    assert not writes


def test_only_latest_failure_retried_once_per_pr(monkeypatch):
    old = run(
        id=10,
        created_at=(NOW - timedelta(days=1)).isoformat(),
        updated_at=(NOW - timedelta(hours=8)).isoformat(),
    )
    writes = harness(monkeypatch, rows=[old, run()])
    retry.sweep("owner/repo", NOW, dry_run=False)
    assert len(writes) == 1
    assert writes[0][0][2] == "20"


def test_read_failure_does_not_retry(monkeypatch):
    writes = harness(monkeypatch)

    def fail(path):
        raise subprocess.CalledProcessError(1, ["gh"])

    monkeypatch.setattr(retry, "api", fail)
    rows, errors = retry.sweep("owner/repo", NOW, dry_run=False)
    assert not writes and errors == 1
    assert "error" in rows[0]


@pytest.mark.parametrize("field,error", [("base", "AttributeError"), ("head", "TypeError")])
@pytest.mark.parametrize("refresh", [1, 2])
def test_null_pr_metadata_does_not_abort_other_prs(monkeypatch, field, error, refresh):
    older = run(
        id=10,
        pull_requests=[{"number": 8}],
        updated_at=(NOW - timedelta(hours=8)).isoformat(),
    )
    writes = harness(monkeypatch, rows=[older, run()])
    original = retry.api
    reads = 0

    def read(path):
        nonlocal reads
        if path.endswith("/pulls/8"):
            reads += 1
            if reads == refresh:
                return pr(**{field: None})
        return original(path)

    monkeypatch.setattr(retry, "api", read)
    rows, errors = retry.sweep("owner/repo", NOW, limit=1, dry_run=False)
    assert errors == 1
    assert f"PR #8, run 10: error ({error}); no further action on this PR." in rows
    assert len(writes) == 1 and writes[0][0][2] == "20"
    assert any("PR #7, run 20: retried failed jobs" in row for row in rows)


@pytest.mark.parametrize("payload", [None, [], {"workflow_runs": None}])
def test_malformed_branch_run_payload_does_not_abort_other_prs(monkeypatch, payload):
    older = run(
        id=10,
        pull_requests=[{"number": 8}],
        updated_at=(NOW - timedelta(hours=8)).isoformat(),
    )
    writes = harness(monkeypatch, rows=[older, run()])
    original = retry.api
    reads = 0

    def read(path):
        nonlocal reads
        if "/workflows/" in path:
            reads += 1
            if reads == 1:
                return payload
        return original(path)

    monkeypatch.setattr(retry, "api", read)
    rows, errors = retry.sweep("owner/repo", NOW, limit=1, dry_run=False)
    assert errors == 1
    assert "PR #8, run 10: error (TypeError); no further action on this PR." in rows
    assert len(writes) == 1 and writes[0][0][2] == "20"


def test_exhausted_run_does_not_spend_retry_budget(monkeypatch):
    exhausted = run(
        id=10,
        pull_requests=[{"number": 8}],
        run_attempt=50,
        updated_at=(NOW - timedelta(days=2)).isoformat(),
    )
    writes = harness(monkeypatch, rows=[exhausted, run()])
    rows, errors = retry.sweep("owner/repo", NOW, limit=1, dry_run=False)
    assert errors == 0
    assert "50-attempt limit" in rows[0]
    assert len(writes) == 1 and writes[0][0][2] == "20"


def test_failed_rerun_request_does_not_spend_successful_retry_capacity(monkeypatch):
    older = run(
        id=10,
        pull_requests=[{"number": 8}],
        updated_at=(NOW - timedelta(hours=8)).isoformat(),
    )
    harness(monkeypatch, rows=[older, run()])
    attempted = []

    def rerun(*args, **kwargs):
        attempted.append(args[2])
        if args[2] == "10":
            raise subprocess.CalledProcessError(1, ["gh"])

    monkeypatch.setattr(retry, "gh", rerun)
    rows, errors = retry.sweep("owner/repo", NOW, limit=1, dry_run=False)
    assert errors == 1
    assert attempted == ["10", "20"]
    assert any("PR #7, run 20: retried" in row for row in rows)


def test_resolve_dispatch_and_legacy_dispatch(monkeypatch):
    assert (
        retry.run_pr(
            run(event="workflow_dispatch", pull_requests=[], display_title="Review PR #42"),
            "o/r",
        ) == 42
    )
    monkeypatch.setattr(
        retry,
        "pages",
        lambda *args: [{"id": 99, "name": "dispatch-guard", "status": "completed"}],
    )
    monkeypatch.setattr(
        retry,
        "gh",
        lambda *args: "2026-09-06 Dispatched PR #7: head_ref='feature' author='human'",
    )
    assert retry.run_pr(run(event="workflow_dispatch", pull_requests=[]), "o/r") == 7


@pytest.mark.parametrize("payload,error", [(None, "AttributeError"), (run(pull_requests=None), "TypeError")])
def test_malformed_run_association_returns_diagnostic(payload, error):
    assert retry.resolve_run(payload, "owner/repo") == (payload, None, error)


def test_malformed_completed_run_association_does_not_abort_other_prs(monkeypatch):
    malformed = run(id=30, pull_requests=None)
    writes = harness(monkeypatch, rows=[run(), malformed], fresh=[run()])
    calls = 0

    def discovered(*args):
        nonlocal calls
        calls += 1
        return [run(), malformed] if calls == 1 else []

    monkeypatch.setattr(retry, "workflow_runs", discovered)
    rows, errors = retry.sweep("owner/repo", NOW, dry_run=False)
    assert errors == 0
    assert "Run 30: cannot resolve PR (TypeError)." in rows
    assert "Run 30: deferred; PR association unavailable." in rows
    assert len(writes) == 1 and writes[0][0][2] == "20"


def test_legacy_aigr_dispatch_resolves_from_pr_number_environment(monkeypatch):
    monkeypatch.setattr(
        retry, "pages",
        lambda *args: [{"id": 99, "name": "claude-review", "status": "completed"}],
    )
    monkeypatch.setattr(retry, "gh", lambda *args: "2026-09-06T12:00:00Z   PR_NUMBER: 2804")
    assert retry.run_pr(run(event="workflow_dispatch", pull_requests=[]), "o/r") == 2804


def test_legacy_comment_title_cannot_override_numeric_workflow_input(monkeypatch):
    monkeypatch.setattr(
        retry, "pages",
        lambda *args: [{"id": 99, "name": "claude-review", "status": "completed"}],
    )
    monkeypatch.setattr(retry, "gh", lambda *args: "2026-09-06T12:00:00Z   PR_NUMBER: 2804")
    row = run(event="issue_comment", pull_requests=[], display_title="Review PR #999")
    assert retry.run_pr(row, "o/r") == 2804
    monkeypatch.setattr(retry, "gh", lambda *args: "no trustworthy association")
    assert retry.run_pr(row, "o/r") is None


def test_unresolved_active_legacy_run_defers_without_duplicate_writes(monkeypatch):
    writes = harness(
        monkeypatch,
        rows=[run(), run(id=30, pull_requests=[], status="queued", conclusion=None)],
    )
    rows, _ = retry.sweep("o/r", NOW, dry_run=False)
    assert not writes
    assert "active legacy review" in rows[-1]


def stale_queue(**overrides):
    return run(
        id=30,
        event="issue_comment",
        status="queued",
        conclusion=None,
        pull_requests=[],
        updated_at=(NOW - timedelta(days=2)).isoformat(),
    ) | overrides


@pytest.mark.parametrize("during_discovery", [False, True])
def test_stale_jobless_unassociated_queue_does_not_starve_known_pr(monkeypatch, during_discovery):
    queued = stale_queue()
    writes = harness(monkeypatch, rows=[run(), queued], fresh=[run()])
    if during_discovery:
        calls = []

        def discovered(*args):
            calls.append(args)
            return [run()] if len(calls) == 1 else [queued]

        monkeypatch.setattr(retry, "workflow_runs", discovered)
    rows, errors = retry.sweep("owner/repo", NOW, dry_run=False)
    assert errors == 0
    assert len(writes) == 1 and writes[0][0][2] == "20"
    assert sum("ignored for duplicate suppression" in row for row in rows) == 1
    assert any("No run was cancelled or retried" in row for row in rows)


@pytest.mark.parametrize(
    "changes,jobs",
    [
        ({"updated_at": (NOW - timedelta(hours=23)).isoformat()}, []),
        ({"status": "in_progress"}, []),
        ({"status": "waiting"}, []),
        ({"status": "pending"}, []),
        ({"pull_requests": [{"number": 7}]}, []),
        ({}, [{"id": 50, "status": "queued"}]),
        ({}, [{"id": 50, "status": "completed"}]),
    ],
)
def test_stale_queue_refresh_activity_still_blocks(monkeypatch, changes, jobs):
    calls = []

    def current(path):
        calls.append(path)
        return stale_queue(**changes)

    monkeypatch.setattr(retry, "api", current)
    monkeypatch.setattr(retry, "pages", lambda *args: jobs)
    ignored, diagnostic = retry.unassociated_active_disposition(stale_queue(), "owner/repo", NOW)
    assert not ignored and "deferred" in diagnostic
    assert calls == ["repos/owner/repo/actions/runs/30"]


@pytest.mark.parametrize("lookup", ["api", "pages"])
def test_stale_queue_refresh_read_failure_still_blocks(monkeypatch, lookup):
    monkeypatch.setattr(retry, "api", lambda *args: stale_queue())
    monkeypatch.setattr(retry, "pages", lambda *args: [])

    def fail(*args):
        raise subprocess.CalledProcessError(1, ["gh"])

    monkeypatch.setattr(retry, lookup, fail)
    ignored, diagnostic = retry.unassociated_active_disposition(stale_queue(), "owner/repo", NOW)
    assert not ignored and "cannot verify" in diagnostic


@pytest.mark.parametrize(
    "endpoint,payload",
    [
        ("run", None),
        ("run", []),
        ("jobs", {"jobs": None}),
        ("jobs", {"jobs": {}}),
    ],
)
def test_stale_queue_malformed_refresh_cannot_prove_no_activity(monkeypatch, endpoint, payload):
    def read(path):
        if path.endswith("/30"):
            return payload if endpoint == "run" else stale_queue()
        assert "/30/jobs?" in path
        return payload

    monkeypatch.setattr(retry, "api", read)
    ignored, diagnostic = retry.unassociated_active_disposition(stale_queue(), "owner/repo", NOW)
    assert not ignored
    assert "cannot verify an unassociated active review (TypeError)" in diagnostic


def test_recent_unassociated_queue_during_final_scan_has_explicit_deferral(monkeypatch):
    queued = stale_queue(updated_at=NOW.isoformat())
    writes = harness(monkeypatch, rows=[run(), queued], fresh=[run()])
    calls = []

    def discovered(*args):
        calls.append(args)
        return [run()] if len(calls) == 1 else [queued]

    monkeypatch.setattr(retry, "workflow_runs", discovered)
    rows, errors = retry.sweep("owner/repo", NOW, dry_run=False)
    assert not writes and errors == 0
    assert any("unassociated active review run 30" in row for row in rows)
    assert not any("RuntimeError" in row for row in rows)


def test_writer_token_only_reaches_rerun(monkeypatch):
    monkeypatch.setenv("GH_TOKEN", "reader")
    monkeypatch.setenv("GH_RETRY_TOKEN", "writer")
    environments = []

    def execute(args, **kwargs):
        environments.append(kwargs["env"])
        return subprocess.CompletedProcess(args, 0, stdout="{}")

    monkeypatch.setattr(retry.subprocess, "run", execute)
    retry.gh("api", "some/path")
    retry.gh("run", "rerun", "20", "--failed", write=True)
    assert [env["GH_TOKEN"] for env in environments] == ["reader", "writer"]
    assert all("GH_RETRY_TOKEN" not in env for env in environments)


def test_write_never_falls_back_to_discovery_credentials(monkeypatch):
    monkeypatch.setenv("GH_TOKEN", "reader")
    monkeypatch.delenv("GH_RETRY_TOKEN", raising=False)
    monkeypatch.setattr(retry.subprocess, "run", lambda *args, **kwargs: pytest.fail("subprocess ran"))
    with pytest.raises(RuntimeError, match="GH_RETRY_TOKEN"):
        retry.gh("run", "rerun", "20", "--failed", write=True)


def test_pr_event_with_empty_association_resolves_by_commit_and_branch(monkeypatch):
    monkeypatch.setattr(
        retry,
        "pages",
        lambda path: [
            {"number": 7, "head": {"ref": "feature"}},
            {"number": 8, "head": {"ref": "different"}},
        ],
    )
    assert retry.run_pr(run(pull_requests=[], head_branch="feature"), "o/r") == 7
    assert retry.run_pr(
        run(pull_requests=[], head_branch="feature", display_title="Review PR #999"), "o/r"
    ) == 7


def test_discovery_splits_above_github_search_limit(monkeypatch):
    calls = []

    def read(path):
        calls.append(path)
        if len(calls) == 1:
            return {"total_count": 1001, "workflow_runs": []}
        return {"total_count": 1, "workflow_runs": [run(id=len(calls))]}

    monkeypatch.setattr(retry, "api", read)
    found = retry.workflow_runs("o/r", NOW - timedelta(days=1), NOW, "failure")
    assert len(calls) == 3
    assert {r["id"] for r in found} == {2, 3}
    assert all("status=failure" in path for path in calls)


def test_discovery_reads_later_pages(monkeypatch):
    def read(path):
        rows = (
            [run(id=i) for i in range(100)]
            if path.endswith("&page=1")
            else [run(id=101)]
        )
        return {"total_count": 101, "workflow_runs": rows}

    monkeypatch.setattr(retry, "api", read)
    assert (
        len(retry.workflow_runs("o/r", NOW - timedelta(days=1), NOW, "failure")) == 101
    )


def test_operator_minimum_delay_can_increase_backoff():
    assert retry.delay_hours(1, 12) == 12
    assert retry.delay_hours(2, 12) == 12
    assert retry.delay_hours(3, 12) == 24


def test_newer_manual_review_prevents_write(monkeypatch):
    manual = run(
        id=30,
        event="workflow_dispatch",
        head_sha="main",
        pull_requests=[],
        display_title="Review PR #7",
        status="in_progress",
        conclusion=None,
    )
    writes = harness(monkeypatch, rows=[run(), manual])
    retry.sweep("o/r", NOW, dry_run=False)
    assert not writes


def test_manual_fork_branch_main_does_not_match_unrelated_manual_reviews(monkeypatch):
    manual = run(event="workflow_dispatch", head_sha="default-branch-sha")
    unrelated = run(
        id=30,
        event="issue_comment",
        pull_requests=[{"number": 99}],
        conclusion="success",
        created_at=(NOW - timedelta(hours=1)).isoformat(),
    )
    writes = harness(monkeypatch, rows=[manual])
    original = retry.api

    def read(path):
        if "/workflows/" in path:
            assert "branch=main" in path
            return {"workflow_runs": [] if "event=pull_request" in path else [unrelated]}
        if "/pulls/" in path:
            return pr(head={"sha": "abc", "ref": "main", "repo": {"full_name": "contributor/fork"}})
        return original(path)

    monkeypatch.setattr(retry, "api", read)
    rows, errors = retry.sweep("owner/repo", NOW, dry_run=False)
    assert errors == 0
    assert len(writes) == 1 and writes[0][0][2] == "20"


def test_late_success_on_old_commit_does_not_hide_current_failure():
    old = run(id=15, head_sha="old", conclusion="success", updated_at=NOW.isoformat())
    assert reason(peers=[old]) is None


def test_deleted_reviewer_does_not_crash_recovery():
    assert reason(reviews=[{"id": 1, "user": None, "state": "APPROVED"}]) is None


def test_zero_delay_explicitly_bypasses_backoff():
    assert retry.delay_hours(1, 0) == 0
    assert retry.delay_hours(5, 0) == 0


def test_summary_links_actions_first_and_keeps_diagnostics():
    rows = [
        "Run 30: cannot resolve PR (CalledProcessError).",
        "Run 30: deferred; PR association unavailable.",
        "PR #9, run 29: skipped; PR is closed.",
        "PR #7, run 20: retried failed jobs (attempt 2).",
        "PR #8, run 21: deferred; retry budget reached.",
    ]
    summary = retry.render_summary("owner/repo", rows, False, 1)
    assert "Live run: 1 rerun requests accepted (limit: 1)." in summary
    assert "1 PRs deferred at the retry limit" in summary
    assert "[PR #7](https://github.com/owner/repo/pull/7)" in summary
    assert "[run 20](https://github.com/owner/repo/actions/runs/20)" in summary
    assert "[Run 30](https://github.com/owner/repo/actions/runs/30)" in summary
    assert summary.index("### Restarted reviews") < summary.index("<details>")
    assert "PR lookup diagnostics (2 messages)" in summary
    assert "Messages, not unique PRs or runs" in summary
    assert "they have not been queued" in summary
    for row in rows:
        assert row.split(": ", 1)[1] in summary


def test_summary_dry_run_does_not_claim_restarts():
    summary = retry.render_summary(
        "owner/repo", ["PR #7, run 20: would retry failed jobs (attempt 2)."], True, 5
    )
    assert "Dry run: no rerun requests issued; 1 would restart (limit: 5)." in summary
    assert "### Would restart (dry run) (1)" in summary
    assert "### Restarted reviews" not in summary


@pytest.mark.parametrize(
    "row",
    [
        "Review retries disabled (budget 0).",
        "No failed review runs need recovery.",
        "Retries deferred: an active legacy review cannot yet be associated with a PR.",
        "Discovery failed (CalledProcessError); no retries issued.",
        "PR #7, run 20: error (CalledProcessError); no further action on this PR.",
    ],
)
def test_summary_preserves_zero_action_and_error_notices(row):
    summary = retry.render_summary("owner/repo", [row], False, 5)
    assert "Live run: 0 rerun requests accepted" in summary
    assert row.split(": ")[-1] in summary


def test_main_writes_same_linked_summary_to_stdout_and_actions(
    monkeypatch, tmp_path, capsys
):
    output = tmp_path / "summary.md"
    monkeypatch.setenv("GITHUB_STEP_SUMMARY", str(output))
    monkeypatch.setattr(
        retry,
        "sweep",
        lambda *args: (["PR #7, run 20: would retry failed jobs (attempt 2)."], 0),
    )
    assert retry.main(["--repo", "owner/repo"]) == 0
    assert capsys.readouterr().out.strip() == output.read_text().strip()
    assert "https://github.com/owner/repo/actions/runs/20" in output.read_text()


@pytest.mark.parametrize(
    "payload",
    [
        None,
        [],
        {"total_count": None, "workflow_runs": []},
        {"total_count": 0, "workflow_runs": None},
        {"total_count": 0, "workflow_runs": {}},
        {"total_count": 1, "workflow_runs": [None]},
    ],
)
def test_cli_malformed_discovery_reports_error_without_writes(monkeypatch, capsys, payload):
    writes = []
    monkeypatch.setenv("GH_RETRY_TOKEN", "writer")
    monkeypatch.setattr(retry, "api", lambda path: payload)
    monkeypatch.setattr(retry, "gh", lambda *args, **kwargs: writes.append(args))
    assert retry.main(["--repo", "owner/repo", "--execute"]) == 1
    assert not writes
    summary = capsys.readouterr().out
    assert "Discovery failed (TypeError); no retries issued." in summary
    assert "Live run: 0 rerun requests accepted" in summary


def test_cli_discovery_request_failure_reports_error_without_writes(monkeypatch, capsys):
    writes = []
    monkeypatch.setenv("GH_RETRY_TOKEN", "writer")

    def fail(path):
        raise subprocess.CalledProcessError(1, ["gh"])

    monkeypatch.setattr(retry, "api", fail)
    monkeypatch.setattr(retry, "gh", lambda *args, **kwargs: writes.append(args))
    assert retry.main(["--repo", "owner/repo", "--execute"]) == 1
    assert not writes
    assert "Discovery failed (CalledProcessError); no retries issued." in capsys.readouterr().out


@pytest.mark.parametrize("mode", [[], ["--dry-run"]])
def test_cli_defaults_to_read_only_even_with_a_writer_available(monkeypatch, mode):
    writes = harness(monkeypatch)
    assert retry.main(["--repo", "owner/repo", *mode]) == 0
    assert not writes


def test_execute_requires_writer_before_discovery(monkeypatch):
    monkeypatch.delenv("GH_RETRY_TOKEN", raising=False)
    monkeypatch.setattr(retry, "sweep", lambda *args: pytest.fail("discovery ran"))
    with pytest.raises(SystemExit) as exc:
        retry.main(["--repo", "owner/repo", "--execute"])
    assert exc.value.code == 2


def test_execute_cli_uses_explicit_live_mode(monkeypatch):
    writes = harness(monkeypatch)
    assert retry.main(["--repo", "owner/repo", "--execute", "--min-delay-hours", "0"]) == 0
    assert len(writes) == 1
