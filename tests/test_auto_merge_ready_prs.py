"""Tests for the deterministic merge controller used by PR Shepherd.

Every load-bearing veto has a negative test. A regression here could merge an
unreviewed or stale pull request, so the fixtures fail closed by default.
"""

import argparse
import importlib.util
import json
import subprocess
import sys
from datetime import UTC, datetime, timedelta
from pathlib import Path

import pytest


_SPEC = importlib.util.spec_from_file_location(
    "auto_merge_ready_prs",
    Path(__file__).resolve().parents[1] / "scripts" / "auto_merge_ready_prs.py",
)
auto_merge = importlib.util.module_from_spec(_SPEC)
sys.modules[_SPEC.name] = auto_merge
_SPEC.loader.exec_module(auto_merge)

NOW = datetime(2026, 8, 8, 12, 0, tzinfo=UTC)
HEAD_SHA = "cafe1234"
BASE_SHA = "base1234"
REQUIRED_CHECK = "test (3.12)"


def approved_review(
    *,
    login="ai4c-reviewer[bot]",
    commit_id=HEAD_SHA,
    state="APPROVED",
):
    return {
        "user": {"login": login},
        "state": state,
        "commit_id": commit_id,
    }


def make_pr(**overrides):
    """Return a final-view payload that satisfies every merge guard."""
    pr = {
        "number": 100,
        "title": "curate: review example gene",
        "state": "OPEN",
        "isDraft": False,
        "baseRefName": "main",
        "baseRefOid": BASE_SHA,
        "headRefName": "agent/review-example",
        "headRefOid": HEAD_SHA,
        "labels": [],
        "assignees": [],
        "reviewDecision": "APPROVED",
        "reviews": [approved_review()],
        "mergeable": "MERGEABLE",
        "mergeStateStatus": "CLEAN",
        "createdAt": (NOW - timedelta(days=5)).isoformat().replace("+00:00", "Z"),
        "statusCheckRollup": [
            {
                "__typename": "CheckRun",
                "name": REQUIRED_CHECK,
                "status": "COMPLETED",
                "conclusion": "SUCCESS",
            },
            {
                "__typename": "CheckRun",
                "name": "review",
                "status": "COMPLETED",
                "conclusion": "SUCCESS",
            },
        ],
    }
    pr.update(overrides)
    return pr


def decide(pr, **kwargs):
    kwargs.setdefault("now", NOW)
    kwargs.setdefault("min_age_days", 3)
    kwargs.setdefault("base_branch", "main")
    kwargs.setdefault("current_base_sha", BASE_SHA)
    return auto_merge.evaluate(pr, **kwargs)


def test_fully_ready_pr_is_eligible():
    assert decide(make_pr()).eligible


def test_required_check_can_be_enabled():
    assert decide(make_pr(), required_checks=[REQUIRED_CHECK]).eligible


@pytest.mark.parametrize(
    ("overrides", "expected"),
    [
        ({"state": "CLOSED"}, "not open"),
        ({"isDraft": True}, "draft"),
        ({"baseRefName": "dev"}, "base branch"),
        ({"headRefName": "auto/generate-pages"}, "excluded lane"),
        ({"labels": [{"name": "shepherd:hold"}]}, "held by label"),
        ({"labels": ["shepherd:hold"]}, "held by label"),
        ({"assignees": [{"login": "cmungall"}]}, "assigned to cmungall"),
        ({"reviewDecision": "CHANGES_REQUESTED"}, "not approved"),
        ({"reviewDecision": None}, "not approved"),
        ({"mergeable": "CONFLICTING"}, "merge conflicts"),
        ({"mergeable": "UNKNOWN"}, "mergeability is unknown"),
        ({"mergeStateStatus": "BLOCKED"}, "not clean"),
        ({"mergeStateStatus": "BEHIND"}, "not clean"),
    ],
)
def test_each_general_guard_blocks(overrides, expected):
    decision = decide(make_pr(**overrides))
    assert not decision.eligible
    assert expected in decision.reason


def test_custom_hold_label_and_excluded_prefix_block():
    assert not decide(
        make_pr(labels=[{"name": "merge:hold"}]), hold_label="merge:hold"
    ).eligible
    assert not decide(
        make_pr(headRefName="release/generated"),
        excluded_head_prefixes=["release/"],
    ).eligible


def test_default_generated_prefix_cannot_be_removed_by_extra_prefixes():
    decision = decide(
        make_pr(headRefName="auto/generate-pages"),
        excluded_head_prefixes=(
            *auto_merge.DEFAULT_EXCLUDED_HEAD_PREFIXES,
            "release/",
        ),
    )
    assert not decision.eligible


def test_age_gate_and_tag():
    pr = make_pr(
        createdAt=(NOW - timedelta(days=2, hours=23)).isoformat().replace("+00:00", "Z")
    )
    decision = decide(pr)
    assert not decision.eligible
    assert "<3d" in decision.reason
    assert decision.code == auto_merge.TOO_YOUNG


def test_zero_age_threshold_is_explicitly_supported():
    pr = make_pr(createdAt=(NOW - timedelta(minutes=1)).isoformat())
    assert not decide(pr).eligible
    assert decide(pr, min_age_days=0).eligible


@pytest.mark.parametrize("value", ["0", "3", "14"])
def test_non_negative_int_accepts_valid_values(value):
    assert auto_merge.non_negative_int(value) == int(value)


@pytest.mark.parametrize("value", ["-1", "-3"])
def test_non_negative_int_rejects_negative_values(value):
    with pytest.raises(argparse.ArgumentTypeError, match="zero or positive"):
        auto_merge.non_negative_int(value)


def test_non_empty_strips_and_rejects_empty_values():
    assert auto_merge.non_empty("  alice ") == "alice"
    with pytest.raises(argparse.ArgumentTypeError, match="must not be empty"):
        auto_merge.non_empty("   ")


# Exact-head trusted approval guards


@pytest.mark.parametrize(
    ("spelling", "expected"),
    [
        ("ai4c-reviewer", "ai4c-reviewer"),
        ("AI4C-REVIEWER[BOT]", "ai4c-reviewer"),
        ("app/ai4c-reviewer", "ai4c-reviewer"),
        (" APP/AI4C-REVIEWER[BOT] ", "ai4c-reviewer"),
    ],
)
def test_login_normalization(spelling, expected):
    assert auto_merge.normalize_login(spelling) == expected


@pytest.mark.parametrize(
    "login",
    ["ai4c-reviewer", "ai4c-reviewer[bot]", "APP/AI4C-REVIEWER[BOT]"],
)
def test_default_reviewer_spelling_is_trusted(login):
    pr = make_pr(reviews=[approved_review(login=login)])
    assert decide(pr).eligible


def test_ai4c_agent_approval_intentionally_does_not_count():
    pr = make_pr(reviews=[approved_review(login="ai4c-agent[bot]")])
    decision = decide(pr)
    assert not decision.eligible
    assert "no trusted reviewer" in decision.reason


def test_named_additional_reviewer_can_be_explicitly_allowlisted():
    pr = make_pr(reviews=[approved_review(login="maintainer")])
    assert not decide(pr).eligible
    assert decide(
        pr,
        trusted_reviewers=(*auto_merge.DEFAULT_TRUSTED_REVIEWERS, "maintainer"),
    ).eligible


def test_trusted_review_on_stale_commit_does_not_count():
    pr = make_pr(reviews=[approved_review(commit_id="old123")])
    decision = decide(pr)
    assert not decision.eligible
    assert "not for current head" in decision.reason


def test_non_approval_on_current_head_does_not_count():
    pr = make_pr(reviews=[approved_review(state="COMMENTED")])
    assert not decide(pr).eligible


@pytest.mark.parametrize(
    "review",
    [
        {"user": None, "state": "APPROVED", "commit_id": HEAD_SHA},
        {
            "user": {"login": "ai4c-reviewer[bot]"},
            "state": "APPROVED",
            "commit_id": None,
        },
        approved_review(state="DISMISSED"),
    ],
)
def test_malformed_or_dismissed_reviews_fail_closed(review):
    assert not decide(make_pr(reviews=[review])).eligible


def test_missing_reviews_fail_closed():
    decision = decide(make_pr(reviews=[]))
    assert not decision.eligible
    assert "no trusted reviewer" in decision.reason


def test_missing_head_sha_fails_closed_even_with_an_approval():
    decision = decide(make_pr(headRefOid=""))
    assert not decision.eligible
    assert "no head SHA" in decision.reason


def test_graphql_review_shape_is_supported():
    review = {
        "author": {"login": "ai4c-reviewer"},
        "state": "APPROVED",
        "commit": {"oid": HEAD_SHA},
    }
    assert decide(make_pr(reviews=[review])).eligible


def test_no_trusted_reviewer_configuration_fails_closed():
    decision = decide(make_pr(), trusted_reviewers=[])
    assert not decision.eligible
    assert "no trusted reviewers configured" in decision.reason


# Base-tip guards


def test_missing_pr_base_sha_fails_closed():
    decision = decide(make_pr(baseRefOid=""))
    assert not decision.eligible
    assert "no base SHA" in decision.reason


def test_missing_current_base_tip_fails_closed():
    decision = decide(make_pr(), current_base_sha="")
    assert not decision.eligible
    assert "could not verify" in decision.reason


def test_stale_pr_base_fails_closed():
    decision = decide(make_pr(baseRefOid="oldbase"))
    assert not decision.eligible
    assert "is stale" in decision.reason
    assert BASE_SHA in decision.reason


def test_base_sha_comparison_is_case_insensitive():
    assert decide(make_pr(baseRefOid="ABCDEF"), current_base_sha="abcdef").eligible


# Check rollup and named required checks


@pytest.mark.parametrize(
    ("rollup", "expected"),
    [
        (None, "no status checks"),
        ([], "no status checks"),
        (
            [{"name": "test", "status": "COMPLETED", "conclusion": "FAILURE"}],
            "checks not passing",
        ),
        (
            [{"name": "test", "status": "COMPLETED", "conclusion": "CANCELLED"}],
            "checks not passing",
        ),
        (
            [{"name": "test", "status": "IN_PROGRESS", "conclusion": None}],
            "checks still running",
        ),
        ([{"context": "legacy", "state": "FAILURE"}], "checks not passing"),
        ([{"context": "legacy", "state": "PENDING"}], "checks still running"),
        ([{"context": "legacy", "state": "EXPECTED"}], "checks still running"),
        (
            [{"name": "optional", "status": "COMPLETED", "conclusion": "SKIPPED"}],
            "no successful check",
        ),
    ],
)
def test_rollup_failures_block(rollup, expected):
    decision = decide(make_pr(statusCheckRollup=rollup))
    assert not decision.eligible
    assert expected in decision.reason


def test_skipped_and_neutral_checks_are_allowed_beside_a_success():
    rollup = [
        {"name": "test", "status": "COMPLETED", "conclusion": "SUCCESS"},
        {"name": "skip", "status": "COMPLETED", "conclusion": "SKIPPED"},
        {"name": "neutral", "status": "COMPLETED", "conclusion": "NEUTRAL"},
    ]
    assert decide(make_pr(statusCheckRollup=rollup)).eligible


def test_legacy_success_is_accepted():
    assert decide(
        make_pr(statusCheckRollup=[{"context": "legacy", "state": "SUCCESS"}])
    ).eligible


def test_typename_wins_over_shape():
    rollup = [
        {
            "__typename": "StatusContext",
            "context": "legacy",
            "state": "FAILURE",
            "status": "COMPLETED",
        }
    ]
    decision = decide(make_pr(statusCheckRollup=rollup))
    assert not decision.eligible
    assert "legacy=failure" in decision.reason


def test_missing_required_check_blocks_even_when_other_checks_succeed():
    decision = decide(make_pr(), required_checks=["security"])
    assert not decision.eligible
    assert "required checks not explicitly successful: security" in decision.reason


@pytest.mark.parametrize("conclusion", ["SKIPPED", "NEUTRAL"])
def test_required_check_must_be_explicit_success(conclusion):
    rollup = [
        {"name": "test", "status": "COMPLETED", "conclusion": "SUCCESS"},
        {"name": "security", "status": "COMPLETED", "conclusion": conclusion},
    ]
    decision = decide(make_pr(statusCheckRollup=rollup), required_checks=["security"])
    assert not decision.eligible
    assert "not explicitly successful" in decision.reason


def test_each_repeated_required_check_must_succeed():
    decision = decide(make_pr(), required_checks=[REQUIRED_CHECK, "security"])
    assert not decision.eligible
    assert "security" in decision.reason


def test_legacy_required_check_can_explicitly_succeed():
    rollup = [{"context": "legacy", "state": "SUCCESS"}]
    assert decide(
        make_pr(statusCheckRollup=rollup), required_checks=["legacy"]
    ).eligible


# List stage deferral


def test_list_stage_defers_final_only_fields():
    pr = make_pr(
        headRefOid="",
        baseRefOid="",
        reviews=[],
        mergeable="UNKNOWN",
        mergeStateStatus="UNKNOWN",
        statusCheckRollup=None,
    )
    assert decide(pr, final=False).eligible
    assert not decide(pr).eligible


@pytest.mark.parametrize(
    "overrides",
    [
        {"isDraft": True},
        {"headRefName": "auto/generate-pages"},
        {"labels": [{"name": "shepherd:hold"}]},
        {"assignees": [{"login": "cmungall"}]},
        {"reviewDecision": "CHANGES_REQUESTED"},
        {"baseRefName": "dev"},
        {"mergeable": "CONFLICTING"},
    ],
)
def test_list_stage_still_enforces_available_guards(overrides):
    assert not decide(make_pr(**overrides), final=False).eligible


# API helpers


def test_gh_only_injects_writer_token_for_explicit_write_calls(monkeypatch):
    monkeypatch.setenv("GH_TOKEN", "reader-token")
    monkeypatch.setenv("GH_MERGE_TOKEN", "writer-token")
    calls = []

    def fake_run(args, **kwargs):
        calls.append((args, kwargs))
        return subprocess.CompletedProcess(args, 0, stdout="ok", stderr="")

    monkeypatch.setattr(auto_merge.subprocess, "run", fake_run)
    assert auto_merge._gh(["api", "repos/o/r"]) == "ok"
    assert calls[-1][1]["env"]["GH_TOKEN"] == "reader-token"
    assert "GH_MERGE_TOKEN" not in calls[-1][1]["env"]

    assert auto_merge._gh(["api", "repos/o/r"], token="writer-token") == "ok"
    assert calls[-1][1]["env"]["GH_TOKEN"] == "writer-token"
    assert "GH_MERGE_TOKEN" not in calls[-1][1]["env"]


def test_view_pr_retries_until_mergeability_resolves(monkeypatch):
    payloads = [
        {"mergeable": "UNKNOWN", "mergeStateStatus": "UNKNOWN"},
        {"mergeable": "MERGEABLE", "mergeStateStatus": "CLEAN"},
    ]
    calls = []

    def fake_gh(args):
        calls.append(args)
        return json.dumps(payloads[len(calls) - 1])

    monkeypatch.setattr(auto_merge, "_gh", fake_gh)
    monkeypatch.setattr(auto_merge.time, "sleep", lambda _: None)
    assert auto_merge.view_pr("o/r", 7)["mergeable"] == "MERGEABLE"
    assert len(calls) == 2


def test_list_pr_reviews_flattens_paginated_rest_response(monkeypatch):
    pages = [[approved_review()], [approved_review(login="maintainer")]]
    calls = []
    monkeypatch.setattr(
        auto_merge,
        "_gh",
        lambda args: calls.append(args) or json.dumps(pages),
    )
    reviews = auto_merge.list_pr_reviews("o/r", 7)
    assert len(reviews) == 2
    assert calls[0][:3] == ["api", "--paginate", "--slurp"]
    assert calls[0][-1].endswith("/pulls/7/reviews?per_page=100")


@pytest.mark.parametrize("payload", [{}, [[{"state": "APPROVED"}], {}]])
def test_list_pr_reviews_rejects_malformed_pages(monkeypatch, payload):
    monkeypatch.setattr(auto_merge, "_gh", lambda _: json.dumps(payload))
    with pytest.raises(ValueError, match="list"):
        auto_merge.list_pr_reviews("o/r", 7)


def test_view_base_tip_encodes_branch_and_rejects_empty(monkeypatch):
    calls = []
    monkeypatch.setattr(
        auto_merge, "_gh", lambda args: calls.append(args) or "abc123\n"
    )
    assert auto_merge.view_base_tip("o/r", "release/v1") == "abc123"
    assert "release%2Fv1" in calls[0][1]

    monkeypatch.setattr(auto_merge, "_gh", lambda _: "\n")
    with pytest.raises(ValueError, match="could not resolve"):
        auto_merge.view_base_tip("o/r", "main")


# End-to-end controller modes


def _run_main(
    monkeypatch,
    tmp_path,
    *,
    view=None,
    views=None,
    args=(),
    base_tips=None,
):
    monkeypatch.setenv("GH_MERGE_TOKEN", "writer-token")
    view = view or make_pr(number=42)
    snapshots = [dict(item) for item in (views or [view, view])]
    last_view = {"value": dict(view)}
    base_tips = list(base_tips or [BASE_SHA, BASE_SHA])
    merges = []
    monkeypatch.setattr(
        auto_merge,
        "list_open_prs",
        lambda _repo, _limit, _base: [make_pr(number=42)],
    )

    def fake_view_pr(_repo, _number):
        snapshot = snapshots.pop(0) if len(snapshots) > 1 else snapshots[0]
        last_view["value"] = dict(snapshot)
        return dict(snapshot)

    monkeypatch.setattr(auto_merge, "view_pr", fake_view_pr)
    monkeypatch.setattr(
        auto_merge,
        "list_pr_reviews",
        lambda _repo, _number: list(last_view["value"].get("reviews", [])),
    )

    def fake_base_tip(_repo, _base):
        return base_tips.pop(0)

    monkeypatch.setattr(auto_merge, "view_base_tip", fake_base_tip)
    monkeypatch.setattr(
        auto_merge,
        "merge_pr",
        lambda repo, number, days, head, _token: merges.append(
            (repo, number, days, head)
        ),
    )
    summary = tmp_path / "summary.md"
    code = auto_merge.main(["--repo", "o/r", "--summary-file", str(summary), *args])
    return code, merges, summary.read_text()


def test_default_mode_is_report_only(monkeypatch, tmp_path):
    code, merges, summary = _run_main(monkeypatch, tmp_path)
    assert code == 0
    assert merges == []
    assert "Would merge 1" in summary
    assert "dry run" in summary


def test_explicit_dry_run_never_merges(monkeypatch, tmp_path):
    code, merges, summary = _run_main(monkeypatch, tmp_path, args=("--dry-run",))
    assert code == 0
    assert merges == []
    assert "Would merge 1" in summary


def test_execute_merges_and_pins_verified_head(monkeypatch, tmp_path):
    code, merges, summary = _run_main(
        monkeypatch,
        tmp_path,
        args=("--execute", "--required-check", REQUIRED_CHECK),
    )
    assert code == 0
    assert merges == [("o/r", 42, 3, HEAD_SHA)]
    assert "Merged 1" in summary


def test_required_check_cli_is_enforced(monkeypatch, tmp_path):
    code, merges, summary = _run_main(
        monkeypatch,
        tmp_path,
        args=("--execute", "--required-check", "security"),
    )
    assert code == 0
    assert merges == []
    assert "required checks not explicitly successful" in summary


def test_base_movement_after_final_verification_blocks_execute(monkeypatch, tmp_path):
    code, merges, summary = _run_main(
        monkeypatch,
        tmp_path,
        args=("--execute", "--required-check", REQUIRED_CHECK),
        base_tips=[BASE_SHA, "newbase"],
    )
    assert code == 0
    assert merges == []
    assert "base branch moved after verification" in summary


def test_hold_added_after_verification_blocks_execute(monkeypatch, tmp_path):
    initial = make_pr(number=42)
    held = make_pr(number=42, labels=[{"name": "shepherd:hold"}])
    code, merges, summary = _run_main(
        monkeypatch,
        tmp_path,
        views=[initial, held],
        args=("--execute", "--required-check", REQUIRED_CHECK),
    )
    assert code == 0
    assert merges == []
    assert "state changed after verification: held by label" in summary


def test_execute_and_dry_run_are_mutually_exclusive(monkeypatch):
    monkeypatch.setattr(auto_merge, "list_open_prs", lambda *_: [])
    with pytest.raises(SystemExit) as exc:
        auto_merge.main(["--repo", "o/r", "--execute", "--dry-run"])
    assert exc.value.code == 2


def test_execute_requires_an_explicit_required_check(monkeypatch):
    monkeypatch.setattr(auto_merge, "list_open_prs", lambda *_: [])
    with pytest.raises(SystemExit) as exc:
        auto_merge.main(["--repo", "o/r", "--execute"])
    assert exc.value.code == 2


def test_execute_requires_a_separate_write_token(monkeypatch):
    monkeypatch.delenv("GH_MERGE_TOKEN", raising=False)
    monkeypatch.setattr(auto_merge, "list_open_prs", lambda *_: [])
    with pytest.raises(SystemExit) as exc:
        auto_merge.main(
            ["--repo", "o/r", "--execute", "--required-check", REQUIRED_CHECK]
        )
    assert exc.value.code == 2


def test_review_fetch_error_fails_execute_mode_loudly(monkeypatch, tmp_path):
    monkeypatch.setenv("GH_MERGE_TOKEN", "writer-token")
    monkeypatch.setattr(auto_merge, "list_open_prs", lambda *_: [make_pr(number=42)])
    monkeypatch.setattr(auto_merge, "view_pr", lambda *_: make_pr(number=42))
    monkeypatch.setattr(
        auto_merge,
        "list_pr_reviews",
        lambda *_: (_ for _ in ()).throw(ValueError("bad review payload")),
    )
    summary = tmp_path / "summary.md"
    code = auto_merge.main(
        [
            "--repo",
            "o/r",
            "--summary-file",
            str(summary),
            "--execute",
            "--required-check",
            REQUIRED_CHECK,
        ]
    )
    assert code == 1
    assert "Failed to merge 1" in summary.read_text()
    assert "could not re-verify: bad review payload" in summary.read_text()


def test_review_fetch_error_is_a_nonfatal_skip_in_audit_mode(monkeypatch, tmp_path):
    monkeypatch.setattr(auto_merge, "list_open_prs", lambda *_: [make_pr(number=42)])
    monkeypatch.setattr(auto_merge, "view_pr", lambda *_: make_pr(number=42))
    monkeypatch.setattr(
        auto_merge,
        "list_pr_reviews",
        lambda *_: (_ for _ in ()).throw(ValueError("bad review payload")),
    )
    summary = tmp_path / "summary.md"
    code = auto_merge.main(
        ["--repo", "o/r", "--summary-file", str(summary), "--dry-run"]
    )
    assert code == 0
    assert "Skipped 1 near-miss" in summary.read_text()


def test_execute_processes_oldest_candidate_first(monkeypatch, tmp_path):
    monkeypatch.setenv("GH_MERGE_TOKEN", "writer-token")
    older = make_pr(
        number=20,
        title="older",
        createdAt=(NOW - timedelta(days=10)).isoformat().replace("+00:00", "Z"),
    )
    newer = make_pr(
        number=10,
        title="newer",
        createdAt=(NOW - timedelta(days=5)).isoformat().replace("+00:00", "Z"),
    )
    monkeypatch.setattr(
        auto_merge, "list_open_prs", lambda *_: [dict(newer), dict(older)]
    )
    monkeypatch.setattr(
        auto_merge,
        "view_pr",
        lambda _repo, number: dict(older if number == 20 else newer),
    )
    monkeypatch.setattr(
        auto_merge,
        "list_pr_reviews",
        lambda _repo, number: list(
            (older if number == 20 else newer).get("reviews", [])
        ),
    )
    monkeypatch.setattr(auto_merge, "view_base_tip", lambda *_: BASE_SHA)
    merges = []
    monkeypatch.setattr(
        auto_merge,
        "merge_pr",
        lambda _repo, number, _days, _head, _token: merges.append(number),
    )
    summary = tmp_path / "summary.md"
    code = auto_merge.main(
        [
            "--repo",
            "o/r",
            "--summary-file",
            str(summary),
            "--execute",
            "--required-check",
            REQUIRED_CHECK,
        ]
    )
    assert code == 0
    assert merges == [20, 10]


# Merge invocation and reporting


def test_merge_pr_always_pins_the_head(monkeypatch):
    calls = []
    monkeypatch.setattr(
        auto_merge,
        "_gh",
        lambda args, *, token=None: calls.append((args, token)) or "",
    )
    auto_merge.merge_pr("o/r", 7, 3, HEAD_SHA, "writer-token")
    merge, token = calls[0]
    assert merge[merge.index("--match-head-commit") + 1] == HEAD_SHA
    assert token == "writer-token"
    assert calls[1][1] == "writer-token"


@pytest.mark.parametrize("head_sha", ["", "   "])
def test_merge_pr_refuses_empty_head_sha(monkeypatch, head_sha):
    monkeypatch.setattr(
        auto_merge,
        "_gh",
        lambda _args: pytest.fail("gh must not run without a head SHA"),
    )
    with pytest.raises(ValueError, match="refusing to merge"):
        auto_merge.merge_pr("o/r", 7, 3, head_sha, "writer-token")


def test_merge_pr_refuses_empty_write_token(monkeypatch):
    monkeypatch.setattr(
        auto_merge,
        "_gh",
        lambda _args, **_kwargs: pytest.fail("gh must not run without a write token"),
    )
    with pytest.raises(ValueError, match="dedicated write token"):
        auto_merge.merge_pr("o/r", 7, 3, HEAD_SHA, "  ")


def test_comment_failure_does_not_mask_successful_merge(monkeypatch):
    def fake_gh(args, *, token=None):
        assert token == "writer-token"
        if args[1] == "comment":
            raise subprocess.CalledProcessError(1, "gh", stderr="rate limited")
        return ""

    monkeypatch.setattr(auto_merge, "_gh", fake_gh)
    auto_merge.merge_pr("o/r", 7, 3, HEAD_SHA, "writer-token")


GH_REFUSAL = (
    "X Pull request o/r#7 is not mergeable: head branch was modified.\n"
    "To use administrator privileges, add --admin.\n"
)


def test_benign_race_and_error_rendering():
    assert auto_merge.is_benign_merge_failure(GH_REFUSAL)
    exc = subprocess.CalledProcessError(1, "gh", stderr=GH_REFUSAL)
    assert auto_merge._gh_error(exc).startswith("Pull request")
    assert "--admin" not in auto_merge._gh_error(exc)
    assert not auto_merge.is_benign_merge_failure("HTTP 403")
    assert not auto_merge.is_benign_merge_failure("Pull request is not mergeable")


def test_dry_run_summary_never_claims_a_merge():
    report = auto_merge.render_summary(
        merged=[{"number": 1, "title": "curate: A"}],
        skipped=[{"number": 2, "reason": "draft"}],
        failed=[],
        dry_run=True,
    )
    assert "Would merge 1" in report
    assert "dry run" in report
    assert "**Merged" not in report
    assert "#2 — draft" in report
