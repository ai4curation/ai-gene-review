"""Tests for the deterministic merge controller used by PR Shepherd.

Every load-bearing veto has a negative test. A regression here could merge an
unreviewed or stale pull request, so the fixtures fail closed by default.
"""

import argparse
import importlib.util
import json
import subprocess
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

import pytest


_SPEC = importlib.util.spec_from_file_location(
    "auto_merge_ready_prs",
    Path(__file__).resolve().parents[1] / "scripts" / "auto_merge_ready_prs.py",
)
assert _SPEC is not None
assert _SPEC.loader is not None
auto_merge = importlib.util.module_from_spec(_SPEC)
sys.modules[_SPEC.name] = auto_merge
_SPEC.loader.exec_module(auto_merge)

NOW = datetime(2026, 8, 8, 12, 0, tzinfo=timezone.utc)
HEAD_SHA = "cafe1234"
REQUIRED_CHECK = "test (3.12)"


def approved_review(
    *,
    login="ai4c-reviewer[bot]",
    commit_id=HEAD_SHA,
    state="APPROVED",
    user_type="Bot",
):
    return {
        "user": {"login": login, "type": user_type},
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
        "headRefName": "agent/review-example",
        "headRefOid": HEAD_SHA,
        "labels": [],
        "assignees": [],
        "reviewDecision": "APPROVED",
        "reviews": [approved_review()],
        "changedFiles": 1,
        "changed_files": ["genes/human/EXAMPLE/EXAMPLE-ai-review.yaml"],
        "previous_changed_filenames": [],
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
    kwargs.setdefault("trusted_reviewers", ())
    return auto_merge.evaluate(pr, **kwargs)


def decide_trusted(pr, **kwargs):
    """Evaluate with the optional Bot-identity allowlist enabled."""
    kwargs.setdefault("trusted_reviewers", ("ai4c-reviewer",))
    return decide(pr, **kwargs)


def test_fully_ready_pr_is_eligible():
    assert decide(make_pr()).eligible


def test_approved_draft_requires_explicit_opt_in():
    pr = make_pr(isDraft=True)
    assert not decide(pr).eligible
    assert decide(pr, include_drafts=True).eligible


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


@pytest.mark.parametrize("value", ["1", "300"])
def test_positive_int_accepts_valid_values(value):
    assert auto_merge.positive_int(value) == int(value)


@pytest.mark.parametrize("value", ["0", "-1"])
def test_positive_int_rejects_nonpositive_values(value):
    with pytest.raises(argparse.ArgumentTypeError, match="must be positive"):
        auto_merge.positive_int(value)


def test_non_empty_strips_and_rejects_empty_values():
    assert auto_merge.non_empty("  alice ") == "alice"
    with pytest.raises(argparse.ArgumentTypeError, match="must not be empty"):
        auto_merge.non_empty("   ")


def test_directory_path_prefix_requires_a_normalized_directory_boundary():
    assert auto_merge.directory_path_prefix(" docs/policy/ ") == "docs/policy/"
    for value in ("docs", "/docs/", "docs//", "docs/../", "docs\\policy/"):
        with pytest.raises(argparse.ArgumentTypeError):
            auto_merge.directory_path_prefix(value)


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


@pytest.mark.parametrize("spelling", ["app/", "[bot]", "app/[bot]", " APP/[BOT] "])
def test_trusted_reviewer_cli_rejects_spellings_that_normalize_empty(
    monkeypatch, capsys, spelling
):
    monkeypatch.setattr(auto_merge, "list_open_prs", lambda *_: [])
    with pytest.raises(SystemExit) as exc:
        auto_merge.main(["--repo", "o/r", "--trusted-reviewer", spelling])
    assert exc.value.code == 2
    assert "must identify a Bot login" in capsys.readouterr().err


@pytest.mark.parametrize(
    "login",
    ["ai4c-reviewer", "ai4c-reviewer[bot]", "APP/AI4C-REVIEWER[BOT]"],
)
def test_default_reviewer_spelling_is_trusted(login):
    pr = make_pr(reviews=[approved_review(login=login)])
    assert decide_trusted(pr).eligible


@pytest.mark.parametrize(
    ("login", "user_type"),
    [
        ("ai4c-reviewer", "User"),
        ("ai4c-reviewer[bot]", "User"),
        ("app/ai4c-reviewer", "User"),
        ("ai4c-reviewer", None),
    ],
)
def test_same_named_non_bot_rest_reviewer_is_not_trusted(login, user_type):
    pr = make_pr(reviews=[approved_review(login=login, user_type=user_type)])
    decision = decide_trusted(pr)
    assert not decision.eligible
    assert "did not have a verified Bot identity" in decision.reason


@pytest.mark.parametrize(
    "review",
    [
        {"state": "APPROVED", "commit_id": HEAD_SHA},
        {"user": None, "state": "APPROVED", "commit_id": HEAD_SHA},
        {
            "user": "ai4c-reviewer[bot]",
            "state": "APPROVED",
            "commit_id": HEAD_SHA,
        },
        {
            "author": {"login": "ai4c-reviewer"},
            "user": {"login": "different-bot[bot]", "type": "Bot"},
            "state": "APPROVED",
            "commit_id": HEAD_SHA,
        },
    ],
)
def test_missing_or_unrecognized_rest_user_shape_fails_closed(review):
    assert not decide_trusted(make_pr(reviews=[review])).eligible


def test_ai4c_agent_approval_does_not_count_with_identity_allowlist():
    pr = make_pr(reviews=[approved_review(login="ai4c-agent[bot]")])
    decision = decide_trusted(pr)
    assert not decision.eligible
    assert "no trusted reviewer" in decision.reason


def test_named_additional_bot_reviewer_can_be_explicitly_allowlisted():
    pr = make_pr(reviews=[approved_review(login="release-reviewer[bot]")])
    assert not decide_trusted(pr).eligible
    assert decide(
        pr,
        trusted_reviewers=(*auto_merge.DEFAULT_TRUSTED_REVIEWERS, "release-reviewer"),
    ).eligible


def test_trusted_review_on_stale_commit_does_not_count():
    pr = make_pr(reviews=[approved_review(commit_id="old123")])
    decision = decide_trusted(pr)
    assert not decision.eligible
    assert "not for current head" in decision.reason


def test_non_approval_on_current_head_does_not_count():
    pr = make_pr(reviews=[approved_review(state="COMMENTED")])
    assert not decide_trusted(pr).eligible


@pytest.mark.parametrize(
    "review",
    [
        {"user": None, "state": "APPROVED", "commit_id": HEAD_SHA},
        {
            "user": {"login": "ai4c-reviewer[bot]", "type": "Bot"},
            "state": "APPROVED",
            "commit_id": None,
        },
        approved_review(state="DISMISSED"),
    ],
)
def test_malformed_or_dismissed_reviews_fail_closed(review):
    assert not decide_trusted(make_pr(reviews=[review])).eligible


def test_missing_reviews_fail_closed():
    decision = decide_trusted(make_pr(reviews=[]))
    assert not decision.eligible
    assert "no trusted reviewer" in decision.reason


def test_missing_head_sha_fails_closed_even_with_an_approval():
    decision = decide(make_pr(headRefOid=""))
    assert not decision.eligible
    assert "no head SHA" in decision.reason


def test_graphql_review_shape_fails_closed_without_actor_type():
    review = {
        "author": {"login": "ai4c-reviewer"},
        "state": "APPROVED",
        "commit": {"oid": HEAD_SHA},
    }
    assert not decide_trusted(make_pr(reviews=[review])).eligible


def test_no_trusted_reviewer_configuration_accepts_any_exact_head_approver():
    review = approved_review(login="ai4c-agent[bot]")
    assert decide(make_pr(reviews=[review])).eligible


def test_no_trusted_reviewer_configuration_still_requires_exact_head_approval():
    decision = decide(make_pr(reviews=[approved_review(commit_id="old123")]))
    assert not decision.eligible
    assert "not for current head" in decision.reason


def test_no_trusted_reviewer_configuration_requires_a_rest_approval():
    decision = decide(make_pr(reviews=[]))
    assert not decision.eligible
    assert "no approval is bound to the current head" in decision.reason


# Base freshness policy


def test_recorded_stale_base_does_not_block_an_independent_pr():
    assert decide(make_pr(baseRefOid="old-base-tip")).eligible


# Changed-file path scope


def test_default_allowed_path_prefixes_are_the_conservative_content_set():
    assert auto_merge.DEFAULT_ALLOWED_PATH_PREFIXES == (
        "genes/",
        "genesets/",
        "gocams/",
        "interpro/",
        "modules/",
        "pages/",
        "projects/",
        "publications/",
        "reactome/",
        "rules/",
        "terms/",
        "families/",
        "research/",
    )


def test_allowed_path_canary_mix_is_eligible():
    canaries = [
        f"{prefix}path-canary.yaml"
        for prefix in auto_merge.DEFAULT_ALLOWED_PATH_PREFIXES
    ]
    assert decide(make_pr(changedFiles=len(canaries), changed_files=canaries)).eligible


@pytest.mark.parametrize(
    "disallowed",
    [
        ".github/workflows/main.yaml",
        "scripts/release.py",
        "src/ai_gene_review/cli.py",
        "pyproject.toml",
    ],
)
def test_one_disallowed_path_vetoes_otherwise_allowed_changes(disallowed):
    decision = decide(
        make_pr(
            changedFiles=2,
            changed_files=[
                "genes/human/EXAMPLE/EXAMPLE-ai-review.yaml",
                disallowed,
            ],
        )
    )
    assert not decision.eligible
    assert "outside the allowed path scope" in decision.reason
    assert disallowed in decision.reason


@pytest.mark.parametrize("changed_files", [None, [], [None], [""], [{}]])
def test_missing_empty_or_malformed_changed_files_fail_closed(changed_files):
    decision = decide(make_pr(changed_files=changed_files))
    assert not decision.eligible
    assert "changed" in decision.reason
    assert "file" in decision.reason


def test_additional_path_prefix_expands_without_replacing_defaults():
    pr = make_pr(
        changedFiles=2,
        changed_files=["genes/human/EXAMPLE/review.yaml", "docs/policy.md"],
    )
    assert not decide(pr).eligible
    assert decide(pr, allowed_path_prefixes=["docs/"]).eligible


@pytest.mark.parametrize("count", [None, True, 0, -1, "1"])
def test_missing_or_invalid_total_changed_file_count_fails_closed(count):
    decision = decide(make_pr(changedFiles=count))
    assert not decision.eligible
    assert "no valid total changed-file count" in decision.reason


def test_rest_file_count_must_match_pr_total():
    decision = decide(make_pr(changedFiles=2))
    assert not decision.eligible
    assert "REST returned 1" in decision.reason
    assert "PR API reports 2" in decision.reason


def test_pr_above_rest_file_cap_fails_closed_even_before_count_comparison():
    decision = decide(make_pr(changedFiles=3_001))
    assert not decision.eligible
    assert "exceeding the REST completeness cap of 3000" in decision.reason


def test_exact_rest_file_cap_can_be_proven_complete_by_matching_count():
    files = [f"genes/bulk/file-{index}.yaml" for index in range(3_000)]
    assert decide(make_pr(changedFiles=3_000, changed_files=files)).eligible


def test_duplicate_rest_filenames_fail_closed():
    decision = decide(
        make_pr(changedFiles=2, changed_files=["genes/a.yaml", "genes/a.yaml"])
    )
    assert not decision.eligible
    assert "duplicate filenames" in decision.reason


@pytest.mark.parametrize(
    "path",
    [
        "genes/../.github/workflows/main.yaml",
        "genes//human/review.yaml",
        "genes/./human/review.yaml",
        "/genes/human/review.yaml",
        "genes\\human\\review.yaml",
        "genes/human/review.yaml\n.github/workflows/main.yaml",
        " genes/human/review.yaml",
    ],
)
def test_non_normalized_repo_paths_fail_closed(path):
    decision = decide(make_pr(changed_files=[path]))
    assert not decision.eligible
    assert "non-normalized changed-file path" in decision.reason


def test_rename_source_path_is_also_within_the_perimeter():
    moved_from_infrastructure = make_pr(
        changed_files=["genes/human/EXAMPLE/moved.yaml"],
        previous_changed_filenames=[".github/workflows/main.yaml"],
    )
    assert not decide(moved_from_infrastructure).eligible
    assert decide(
        make_pr(
            changed_files=["genes/human/EXAMPLE/new.yaml"],
            previous_changed_filenames=["genes/human/EXAMPLE/old.yaml"],
        )
    ).eligible


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
    sleeps = []
    monkeypatch.setattr(auto_merge.time, "sleep", sleeps.append)
    assert auto_merge.view_pr("o/r", 7, attempts=2, delay=0.5)["mergeable"] == (
        "MERGEABLE"
    )
    assert len(calls) == 2
    assert sleeps == [0.5]


def test_view_pr_raises_when_mergeability_stays_unknown(monkeypatch):
    calls = []
    sleeps = []

    def fake_gh(args):
        calls.append(args)
        return json.dumps({"mergeable": "UNKNOWN", "mergeStateStatus": "UNKNOWN"})

    monkeypatch.setattr(auto_merge, "_gh", fake_gh)
    monkeypatch.setattr(auto_merge.time, "sleep", sleeps.append)
    with pytest.raises(ValueError, match="mergeability remained UNKNOWN"):
        auto_merge.view_pr("o/r", 7)
    assert len(calls) == 5
    assert sleeps == [2.0, 4.0, 8.0, 16.0]


def test_list_pr_reviews_flattens_paginated_rest_response(monkeypatch):
    pages = [[approved_review()], [approved_review(login="release-reviewer[bot]")]]
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


def test_list_pr_files_flattens_and_validates_paginated_rest_response(monkeypatch):
    pages = [
        [{"filename": "genes/human/EXAMPLE/review.yaml"}],
        [
            {
                "filename": "projects/EXAMPLE.md",
                "status": "renamed",
                "previous_filename": "projects/OLD-EXAMPLE.md",
            }
        ],
    ]
    calls = []
    monkeypatch.setattr(
        auto_merge,
        "_gh",
        lambda args: calls.append(args) or json.dumps(pages),
    )
    inventory = auto_merge.list_pr_files("o/r", 7)
    assert inventory.filenames == (
        "genes/human/EXAMPLE/review.yaml",
        "projects/EXAMPLE.md",
    )
    assert inventory.previous_filenames == ("projects/OLD-EXAMPLE.md",)
    assert calls[0][:3] == ["api", "--paginate", "--slurp"]
    assert calls[0][-1].endswith("/pulls/7/files?per_page=100")


@pytest.mark.parametrize(
    "payload",
    [
        {},
        [],
        [[]],
        [[{"filename": "genes/example.yaml"}], {}],
        [[], [{"filename": "genes/example.yaml"}]],
        [[None]],
        [[{}]],
        [[{"filename": ""}]],
        [[{"filename": "   "}]],
        [[{"filename": "genes/new.yaml", "status": "renamed"}]],
        [
            [
                {
                    "filename": "genes/new.yaml",
                    "status": "renamed",
                    "previous_filename": "",
                }
            ]
        ],
    ],
)
def test_list_pr_files_rejects_missing_empty_or_malformed_data(monkeypatch, payload):
    monkeypatch.setattr(auto_merge, "_gh", lambda _: json.dumps(payload))
    with pytest.raises(ValueError, match="file API"):
        auto_merge.list_pr_files("o/r", 7)


def test_file_inventory_head_check_rejects_movement_and_empty_heads(monkeypatch):
    calls = []
    monkeypatch.setattr(
        auto_merge,
        "_gh",
        lambda args: calls.append(args) or "new-head\n",
    )
    with pytest.raises(
        auto_merge.HeadMovedError, match="head moved during the file-list read"
    ):
        auto_merge.require_unchanged_file_inventory_head("o/r", 7, "old-head")
    assert calls[0][:3] == ["pr", "view", "7"]
    assert calls[0][-2:] == ["--jq", ".headRefOid"]

    with pytest.raises(ValueError, match="had no head SHA"):
        auto_merge.require_unchanged_file_inventory_head("o/r", 7, "")


def test_file_inventory_head_check_accepts_case_insensitive_exact_head(monkeypatch):
    monkeypatch.setattr(auto_merge, "view_pr_head_sha", lambda *_: "ABCDEF")
    auto_merge.require_unchanged_file_inventory_head("o/r", 7, "abcdef")


def test_view_pr_head_sha_retries_api_errors_and_empty_data(monkeypatch):
    responses = [
        subprocess.CalledProcessError(1, "gh", stderr="HTTP 502"),
        "\n",
        "head-sha\n",
    ]
    sleeps = []

    def fake_gh(_args):
        response = responses.pop(0)
        if isinstance(response, Exception):
            raise response
        return response

    monkeypatch.setattr(auto_merge, "_gh", fake_gh)
    monkeypatch.setattr(auto_merge.time, "sleep", sleeps.append)
    assert auto_merge.view_pr_head_sha("o/r", 7, attempts=3, delay=0.25) == "head-sha"
    assert sleeps == [0.25, 0.5]


# End-to-end controller modes


def _run_main(
    monkeypatch,
    tmp_path,
    *,
    view=None,
    views=None,
    args=(),
    post_file_heads=None,
    list_view=None,
    ready_calls=None,
):
    monkeypatch.setenv("GH_MERGE_TOKEN", "writer-token")
    view = view or make_pr(number=42)
    snapshots = [dict(item) for item in (views or [view, view])]
    last_view = {"value": dict(view)}
    post_file_heads = list(post_file_heads or [HEAD_SHA, HEAD_SHA])
    merges = []
    ready_calls = ready_calls if ready_calls is not None else []
    monkeypatch.setattr(
        auto_merge,
        "list_open_prs",
        lambda _repo, _limit, _base: [dict(list_view or make_pr(number=42))],
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
    monkeypatch.setattr(
        auto_merge,
        "list_pr_files",
        lambda _repo, _number: auto_merge.ChangedFileInventory(
            tuple(last_view["value"].get("changed_files", [])),
            tuple(last_view["value"].get("previous_changed_filenames", [])),
        ),
    )
    monkeypatch.setattr(
        auto_merge,
        "view_pr_head_sha",
        lambda _repo, _number: post_file_heads.pop(0),
    )

    monkeypatch.setattr(
        auto_merge,
        "mark_pr_ready",
        lambda repo, number, _token: ready_calls.append((repo, number)),
    )
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


def test_include_drafts_audit_reports_without_marking_ready(monkeypatch, tmp_path):
    draft = make_pr(number=42, isDraft=True)
    ready_calls = []
    code, merges, summary = _run_main(
        monkeypatch,
        tmp_path,
        view=draft,
        list_view=draft,
        ready_calls=ready_calls,
        args=("--dry-run", "--include-drafts"),
    )
    assert code == 0
    assert merges == []
    assert ready_calls == []
    assert "Would merge 1" in summary


def test_include_drafts_execute_marks_ready_then_reverifies_and_merges(
    monkeypatch, tmp_path
):
    draft = make_pr(number=42, isDraft=True)
    ready = make_pr(number=42, isDraft=False)
    ready_calls = []
    code, merges, summary = _run_main(
        monkeypatch,
        tmp_path,
        views=[draft, ready],
        list_view=draft,
        ready_calls=ready_calls,
        args=(
            "--execute",
            "--required-check",
            REQUIRED_CHECK,
            "--include-drafts",
        ),
    )
    assert code == 0
    assert ready_calls == [("o/r", 42)]
    assert merges == [("o/r", 42, 3, HEAD_SHA)]
    assert "Merged 1" in summary


def test_include_drafts_execute_requires_ready_transition(monkeypatch, tmp_path):
    draft = make_pr(number=42, isDraft=True)
    ready_calls = []
    code, merges, summary = _run_main(
        monkeypatch,
        tmp_path,
        views=[draft, draft],
        list_view=draft,
        ready_calls=ready_calls,
        args=(
            "--execute",
            "--required-check",
            REQUIRED_CHECK,
            "--include-drafts",
        ),
    )
    assert code == 0
    assert ready_calls == [("o/r", 42)]
    assert merges == []
    assert "state changed after verification: draft" in summary


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


def test_disallowed_path_added_on_second_read_blocks_execute(monkeypatch, tmp_path):
    initial = make_pr(number=42)
    changed = make_pr(number=42, changed_files=["scripts/new_release.py"])
    code, merges, summary = _run_main(
        monkeypatch,
        tmp_path,
        views=[initial, changed],
        args=("--execute", "--required-check", REQUIRED_CHECK),
    )
    assert code == 0
    assert merges == []
    assert "state changed after verification" in summary
    assert "scripts/new_release.py" in summary


def test_changed_file_count_mismatch_on_second_read_blocks_execute(
    monkeypatch, tmp_path
):
    initial = make_pr(number=42)
    incomplete = make_pr(number=42, changedFiles=2)
    code, merges, summary = _run_main(
        monkeypatch,
        tmp_path,
        views=[initial, incomplete],
        args=("--execute", "--required-check", REQUIRED_CHECK),
    )
    assert code == 0
    assert merges == []
    assert "state changed after verification" in summary
    assert "REST returned 1" in summary
    assert "PR API reports 2" in summary


@pytest.mark.parametrize(
    ("args", "expected_code", "expected_summary"),
    [
        (("--dry-run",), 0, "Skipped 1 near-miss"),
        (
            ("--execute", "--required-check", REQUIRED_CHECK),
            0,
            "Skipped 1 near-miss",
        ),
    ],
)
def test_head_movement_during_file_read_is_a_benign_skip_in_both_modes(
    monkeypatch, tmp_path, args, expected_code, expected_summary
):
    code, merges, summary = _run_main(
        monkeypatch,
        tmp_path,
        args=args,
        post_file_heads=["moved-head"],
    )
    assert code == expected_code
    assert merges == []
    assert expected_summary in summary
    assert "head moved during the file-list read" in summary


def test_head_movement_during_final_file_read_is_a_benign_skip(monkeypatch, tmp_path):
    code, merges, summary = _run_main(
        monkeypatch,
        tmp_path,
        args=("--execute", "--required-check", REQUIRED_CHECK),
        post_file_heads=[HEAD_SHA, "moved-head"],
    )
    assert code == 0
    assert merges == []
    assert "Skipped 1 near-miss" in summary
    assert "head moved during the file-list read" in summary


def test_allowed_path_cli_extension_preserves_default_paths(monkeypatch, tmp_path):
    view = make_pr(
        number=42,
        changedFiles=2,
        changed_files=["genes/human/EXAMPLE/review.yaml", "docs/policy.md"],
    )
    code, merges, summary = _run_main(
        monkeypatch,
        tmp_path,
        view=view,
        args=("--dry-run", "--allowed-path-prefix", "docs/"),
    )
    assert code == 0
    assert merges == []
    assert "Would merge 1" in summary


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


@pytest.mark.parametrize(
    ("args", "error_kind", "expected_code", "expected_summary"),
    [
        (("--dry-run",), "malformed", 0, "Skipped 1 near-miss"),
        (("--dry-run",), "api", 0, "Skipped 1 near-miss"),
        (
            ("--execute", "--required-check", REQUIRED_CHECK),
            "malformed",
            1,
            "Failed to merge 1",
        ),
        (
            ("--execute", "--required-check", REQUIRED_CHECK),
            "api",
            1,
            "Failed to merge 1",
        ),
    ],
)
def test_file_fetch_error_is_fatal_only_in_execute_mode(
    monkeypatch, tmp_path, args, error_kind, expected_code, expected_summary
):
    monkeypatch.setenv("GH_MERGE_TOKEN", "writer-token")
    monkeypatch.setattr(auto_merge, "list_open_prs", lambda *_: [make_pr(number=42)])
    monkeypatch.setattr(auto_merge, "view_pr", lambda *_: make_pr(number=42))
    monkeypatch.setattr(
        auto_merge,
        "list_pr_reviews",
        lambda *_: [approved_review()],
    )
    error = (
        ValueError("bad file payload")
        if error_kind == "malformed"
        else subprocess.CalledProcessError(1, "gh api", stderr="HTTP 502 file API")
    )
    monkeypatch.setattr(
        auto_merge,
        "list_pr_files",
        lambda *_: (_ for _ in ()).throw(error),
    )
    summary = tmp_path / "summary.md"
    code = auto_merge.main(["--repo", "o/r", "--summary-file", str(summary), *args])
    assert code == expected_code
    assert expected_summary in summary.read_text()
    expected_detail = "bad file payload" if error_kind == "malformed" else "HTTP 502"
    assert expected_detail in summary.read_text()


@pytest.mark.parametrize(
    ("args", "expected_code", "expected_summary"),
    [
        (("--dry-run",), 0, "Skipped 1 near-miss"),
        (
            ("--execute", "--required-check", REQUIRED_CHECK),
            1,
            "Failed to merge 1",
        ),
    ],
)
def test_exhausted_unknown_mergeability_is_fatal_only_in_execute_mode(
    monkeypatch, tmp_path, args, expected_code, expected_summary
):
    monkeypatch.setenv("GH_MERGE_TOKEN", "writer-token")
    monkeypatch.setattr(auto_merge, "list_open_prs", lambda *_: [make_pr(number=42)])
    monkeypatch.setattr(
        auto_merge,
        "view_pr",
        lambda *_: (_ for _ in ()).throw(
            ValueError("mergeability remained UNKNOWN after 3 attempt(s)")
        ),
    )
    summary = tmp_path / "summary.md"
    code = auto_merge.main(["--repo", "o/r", "--summary-file", str(summary), *args])
    assert code == expected_code
    assert expected_summary in summary.read_text()
    assert "mergeability remained UNKNOWN" in summary.read_text()


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
    monkeypatch.setattr(
        auto_merge,
        "list_pr_files",
        lambda _repo, number: auto_merge.ChangedFileInventory(
            tuple((older if number == 20 else newer).get("changed_files", [])),
            tuple(
                (older if number == 20 else newer).get("previous_changed_filenames", [])
            ),
        ),
    )
    monkeypatch.setattr(
        auto_merge,
        "view_pr_head_sha",
        lambda _repo, number: (older if number == 20 else newer)["headRefOid"],
    )
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


def test_multi_candidate_dry_run_explains_no_base_refresh():
    report = auto_merge.render_summary(
        merged=[
            {"number": 1, "title": "curate: A"},
            {"number": 2, "title": "curate: B"},
        ],
        skipped=[],
        failed=[],
        dry_run=True,
    )
    assert "re-read before a head-pinned merge" in report
    assert "do not require a branch refresh" in report
