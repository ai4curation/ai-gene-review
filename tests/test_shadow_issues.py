"""Tests for shadowing upstream issue trackers (issues/<tracker>/)."""

import json
import subprocess
import sys
from pathlib import Path

import pytest
import yaml
from typer.testing import CliRunner

from ai_gene_review.cli import app
from ai_gene_review.shadow_issues.guard import find_notification_hazards
from ai_gene_review.shadow_issues.store import (
    TrackerConfig,
    iter_issue_folders,
    load_issue,
    queue_for,
    read_thread,
    render_thread,
    store_issue,
)

REPO_ROOT = Path(__file__).resolve().parents[1]
HOOK = REPO_ROOT / ".claude" / "hooks" / "upstream_notification_hook.py"
GUARD = REPO_ROOT / "src" / "ai_gene_review" / "shadow_issues" / "guard.py"
AT = "@"  # kept out of literals so this file never reads as a mention


def make_issue(
    number=101,
    body="IPR001806 maps to GTPase activity",
    state="open",
    labels=("InterPro mapping",),
):
    """An issue as the GitHub REST API returns it (fields the store reads)."""
    return {
        "number": number,
        "html_url": f"https://github.com/example/tracker/issues/{number}",
        "title": "InterPro2GO issue: IPR001806 Small GTPase",
        "state": state,
        "state_reason": "completed" if state == "closed" else None,
        "labels": [{"name": name} for name in labels],
        "user": {"login": "curator1"},
        "created_at": "2025-03-01T10:00:00Z",
        "updated_at": "2025-03-05T10:00:00Z",
        "closed_at": "2025-03-05T10:00:00Z" if state == "closed" else None,
        "body": body,
    }


def comment(cid, body, created, updated=None):
    return {
        "event": "commented",
        "id": cid,
        "user": {"login": "curator2"},
        "created_at": created,
        "updated_at": updated or created,
        "body": body,
    }


@pytest.fixture
def tracker_dir(tmp_path):
    folder = tmp_path / "issues" / "example"
    folder.mkdir(parents=True)
    (folder / "tracker.yaml").write_text(
        yaml.safe_dump(
            {
                "repo": "example/tracker",
                "backfill_since": "2024-11-10",
                "prospective_since": "2026-11-10",
                "label_kinds": {"InterPro mapping": "MAPPING_RULE"},
            }
        )
    )
    return folder


@pytest.fixture
def config(tracker_dir):
    return TrackerConfig.load(tracker_dir)


def test_store_creates_stub_and_is_idempotent(config, tracker_dir):
    timeline = [comment(1, "Removed from IPR001806.", "2025-03-04T10:00:00Z")]
    assert store_issue(config, tracker_dir, make_issue(), timeline) == (2, True, 0)
    issue = yaml.safe_load((tracker_dir / "101" / "issue.yaml").read_text())
    assert issue["study"] == "RETROSPECTIVE"
    # Backfilled labels are post-resolution, so a retrospective stub gets no hint.
    assert issue["triage"] == {"status": "UNTRIAGED"}

    # A re-sync with nothing new appends nothing and leaves curated edits alone.
    issue["triage"] = {"status": "TRIAGED", "kind": "MAPPING_RULE", "in_scope": True}
    (tracker_dir / "101" / "issue.yaml").write_text(yaml.safe_dump(issue))
    later = {**make_issue(), "updated_at": "2025-04-01T00:00:00Z"}
    assert store_issue(config, tracker_dir, later, timeline) == (0, False, 0)
    assert (
        yaml.safe_load((tracker_dir / "101" / "issue.yaml").read_text())["triage"][
            "status"
        ]
        == "TRIAGED"
    )


def test_prospective_stub_gets_label_hint(config, tracker_dir):
    new = {**make_issue(number=202), "created_at": "2026-11-12T00:00:00Z"}
    store_issue(config, tracker_dir, new, [])
    issue = yaml.safe_load((tracker_dir / "202" / "issue.yaml").read_text())
    assert issue["study"] == "PROSPECTIVE"
    assert issue["triage"] == {"status": "UNTRIAGED", "suggested_kind": "MAPPING_RULE"}


def test_incomplete_timeline_items_are_skipped_not_fatal(config, tracker_dir):
    """One odd item (e.g. a cross-reference from a deleted repo) must not wedge the sync."""
    timeline = [
        comment(1, "kept", "2025-03-02T00:00:00Z"),
        {
            "event": "cross-referenced",
            "created_at": "2025-03-03T00:00:00Z",
            "source": {"issue": {"number": 9, "title": "gone"}},
        },
        {"event": "labeled", "id": 5, "created_at": "2025-03-03T00:00:00Z"},
        {"event": "subscribed", "id": 6, "created_at": "2025-03-03T00:00:00Z"},
    ]
    result = store_issue(config, tracker_dir, make_issue(), timeline)
    assert (result.appended, result.skipped) == (2, 2)
    bodies = [r.get("body") for r in read_thread(tracker_dir / "101" / "thread.jsonl")]
    assert "kept" in bodies


def test_edits_are_appended_as_new_versions(config, tracker_dir):
    store_issue(
        config, tracker_dir, make_issue(), [comment(1, "draft", "2025-03-02T00:00:00Z")]
    )
    edited = [
        comment(1, "final", "2025-03-02T00:00:00Z", updated="2025-03-03T00:00:00Z")
    ]
    # Closing an issue bumps its updated_at, as GitHub does.
    closed = {**make_issue(state="closed"), "updated_at": "2025-03-06T00:00:00Z"}
    store_issue(config, tracker_dir, closed, edited)
    records = read_thread(tracker_dir / "101" / "thread.jsonl")
    assert [r["body"] for r in records if r["type"] == "comment"] == ["draft", "final"]
    assert [r["state"] for r in records if r["type"] == "issue"] == ["open", "closed"]
    source, _ = load_issue(tracker_dir / "101")
    assert source["state"] == "closed" and source["comment_count"] == 1


def test_thread_survives_unicode_line_separators(config, tracker_dir):
    store_issue(config, tracker_dir, make_issue(body="line one\u2028line two"), [])
    store_issue(
        config,
        tracker_dir,
        {**make_issue(body="x"), "updated_at": "2025-04-01T00:00:00Z"},
        [],
    )
    assert [r["body"] for r in read_thread(tracker_dir / "101" / "thread.jsonl")] == [
        "line one\u2028line two",
        "x",
    ]


def test_snapshot_hides_later_comments_and_edits(config, tracker_dir):
    store_issue(
        config, tracker_dir, make_issue(), [comment(1, "draft", "2025-03-02T00:00:00Z")]
    )
    store_issue(
        config,
        tracker_dir,
        make_issue(),
        [
            comment(1, "final", "2025-03-02T00:00:00Z", updated="2025-03-03T00:00:00Z"),
            comment(2, "fixed in release 111", "2025-03-04T00:00:00Z"),
        ],
    )
    from ai_gene_review.shadow_issues.store import parse_time

    records = read_thread(tracker_dir / "101" / "thread.jsonl")
    snapshot = render_thread(records, as_of=parse_time("2025-03-02T12:00:00Z"))
    assert (
        "draft" in snapshot
        and "final" not in snapshot
        and "release 111" not in snapshot
    )
    blind = render_thread(records, opening_only=True)
    assert "IPR001806" in blind and "draft" not in blind and "final" not in blind
    # Labels can encode the curators' disposition, so the blind view omits them.
    assert "InterPro mapping" not in blind and "labels" not in blind


@pytest.mark.parametrize(
    "triage,shadow,state,rated,expected",
    [
        (
            {"status": "UNTRIAGED"},
            {"status": "NOT_STARTED"},
            "open",
            False,
            "untriaged",
        ),
        (
            {"status": "TRIAGED", "in_scope": True},
            {"status": "NOT_STARTED"},
            "open",
            False,
            "needs_shadow",
        ),
        (
            {"status": "TRIAGED", "in_scope": False},
            {"status": "NOT_STARTED"},
            "open",
            False,
            None,
        ),
        (
            {"status": "TRIAGED", "in_scope": True},
            {"status": "IN_PROGRESS"},
            "closed",
            False,
            "in_progress",
        ),
        (
            {"status": "TRIAGED", "in_scope": True},
            {"status": "DONE"},
            "open",
            False,
            None,
        ),
        (
            {"status": "TRIAGED", "in_scope": True},
            {"status": "DONE"},
            "closed",
            False,
            "needs_rating",
        ),
        (
            {"status": "TRIAGED", "in_scope": True},
            {"status": "DONE"},
            "closed",
            True,
            None,
        ),
    ],
)
def test_queue_for(tmp_path, triage, shadow, state, rated, expected):
    if rated:
        (tmp_path / "rating.yaml").write_text("{}")
    assert (
        queue_for(tmp_path, {"state": state}, {"triage": triage, "shadow": shadow})
        == expected
    )


@pytest.mark.parametrize(
    "text,kinds",
    [
        ("Shadows issues/go-annotation/6606", []),
        ("go-annotation 6606, see #12", []),
        ("Addresses geneontology/go-annotation#6606", ["shorthand_reference"]),
        (
            "see https://github.com/geneontology/go-ontology/issues/32321",
            ["url_reference"],
        ),
        ("see https://github.com/ai4curation/ai-gene-review/pull/1", []),
        (f"thanks {AT}ValWood", ["mention"]),
        (f"cc {AT}cmungall", []),
        (f"`{AT}decorator` and ```\n{AT}code\n```", []),
        ("Co-Authored-By: Claude <noreply@anthropic.com>", []),
    ],
)
def test_guard(text, kinds):
    assert [h.kind for h in find_notification_hazards(text)] == kinds


def test_guard_script_keeps_markdown_headings_but_drops_commit_comments(tmp_path):
    body = tmp_path / "body.md"
    body.write_text("# Summary\n\n## geneontology/go-annotation#1\n")
    assert (
        subprocess.run(
            [sys.executable, str(GUARD), str(body)], capture_output=True
        ).returncode
        == 1
    )
    message = tmp_path / "COMMIT_EDITMSG"
    message.write_text("Title\n# geneontology/go-annotation#1 (git template comment)\n")
    run = subprocess.run(
        [sys.executable, str(GUARD), "--commit-msg", str(message)], capture_output=True
    )
    assert run.returncode == 0


@pytest.mark.parametrize(
    "command,blocked",
    [
        ('git commit -m "Shadow go-annotation 6606"', False),
        ('git commit -m "Addresses geneontology/go-annotation#6606"', True),
        (f'gh pr create --title t --body "thanks {AT}ValWood"', True),
        ("gh issue view 6606 -R geneontology/go-annotation", False),
        ("grep -r geneontology/go-annotation#1 .", False),
        (
            "gh api repos/x/y/issues/1/comments --field body='geneontology/go-annotation#1'",
            True,
        ),
        (
            "gh api repos/x/y/issues/1/comments --raw-field=body='geneontology/go-annotation#1'",
            True,
        ),
    ],
)
def test_bash_hook(command, blocked):
    payload = json.dumps({"tool_input": {"command": command}, "cwd": str(REPO_ROOT)})
    run = subprocess.run(
        [sys.executable, str(HOOK)], input=payload, capture_output=True, text=True
    )
    assert run.returncode == (2 if blocked else 0)


@pytest.mark.parametrize(
    "tool,tool_input,blocked",
    [
        (
            "mcp__github__add_issue_comment",
            {"body": "Shadows geneontology/go-annotation#6596"},
            True,
        ),
        (
            "mcp__github_comment__update_claude_comment",
            {"body": f"done, thanks {AT}ValWood"},
            True,
        ),
        (
            "mcp__github__create_pull_request",
            {"title": "t", "body": "Shadows issues/go-annotation/6596"},
            False,
        ),
        ("Read", {"file_path": "issues/go-annotation/6596/thread.jsonl"}, False),
    ],
)
def test_hook_checks_github_mcp_tools(tool, tool_input, blocked):
    payload = json.dumps({"tool_name": tool, "tool_input": tool_input, "cwd": "."})
    run = subprocess.run(
        [sys.executable, str(HOOK)], input=payload, capture_output=True, text=True
    )
    assert run.returncode == (2 if blocked else 0)


def test_hook_reads_gh_api_input_file(tmp_path):
    payload_file = tmp_path / "payload.json"
    payload_file.write_text('{"body": "see geneontology/go-annotation#1"}')
    payload = json.dumps(
        {
            "tool_input": {
                "command": f"gh api repos/x/y/issues/1/comments --input {payload_file}"
            },
            "cwd": str(tmp_path),
        }
    )
    run = subprocess.run(
        [sys.executable, str(HOOK)], input=payload, capture_output=True, text=True
    )
    assert run.returncode == 2


def test_bash_hook_reads_body_file(tmp_path):
    body = tmp_path / "body.md"
    body.write_text("Fixes https://github.com/geneontology/go-annotation/issues/1\n")
    payload = json.dumps(
        {
            "tool_input": {"command": f"gh pr create --title t --body-file {body}"},
            "cwd": str(tmp_path),
        }
    )
    run = subprocess.run(
        [sys.executable, str(HOOK)], input=payload, capture_output=True, text=True
    )
    assert run.returncode == 2


def test_cli_validate_show_outstanding(config, tracker_dir):
    store_issue(
        config, tracker_dir, make_issue(), [comment(1, "fixed", "2025-03-04T10:00:00Z")]
    )
    root = str(tracker_dir.parent)
    runner = CliRunner()

    result = runner.invoke(
        app, ["shadow-issues", "validate", "example", "--root", root]
    )
    assert result.exit_code == 0, result.output

    result = runner.invoke(
        app,
        [
            "shadow-issues",
            "show",
            "101",
            "--tracker",
            "example",
            "--root",
            root,
            "--opening-only",
        ],
    )
    assert (
        result.exit_code == 0
        and "IPR001806" in result.output
        and "fixed" not in result.output
    )

    result = runner.invoke(
        app, ["shadow-issues", "outstanding", "example", "--root", root]
    )
    assert result.exit_code == 0 and "## untriaged: 1" in result.output

    self_rating = tracker_dir / "101" / "self-rating.yaml"
    self_rating.write_text(
        "tracker: example\nnumber: 101\nworker: w\nconfidence: VERY_HIGH\n"
    )
    result = runner.invoke(
        app, ["shadow-issues", "validate", "example", "--root", root]
    )
    assert result.exit_code == 1 and "VERY_HIGH" in result.output
    self_rating.write_text(
        "tracker: example\nnumber: 101\nworker: w\nconfidence: HIGH\n"
    )
    result = runner.invoke(
        app, ["shadow-issues", "validate", "example", "--root", root]
    )
    assert result.exit_code == 0, result.output

    issue_yaml = tracker_dir / "101" / "issue.yaml"
    issue_yaml.write_text(issue_yaml.read_text().replace("NOT_STARTED", "FINISHED"))
    result = runner.invoke(
        app, ["shadow-issues", "validate", "example", "--root", root]
    )
    assert result.exit_code == 1


RATING = {
    "tracker": "example",
    "number": 101,
    "rater": "shadow-issues-rater",
    "rater_model": "claude-sonnet-5",
    "rater_run": "https://github.com/ai4curation/ai-gene-review/actions/runs/1",
    "independence": "DIFFERENT_MODEL",
    "rated_at": "2026-11-11T00:00:00Z",
    "self_rating_seen": "NEVER",
    "outcome": "CONCORDANT",
    "triage": "AGREE",
    "downstream": "PENDING_RELEASE",
    "summary": "Same fix.",
}


@pytest.mark.parametrize(
    "change,error",
    [
        ({"self_rating_seen": False}, "self_rating_seen"),
        ({"independence": "SELF_DECLARED"}, "SELF_DECLARED"),
        ({"report_url": "ftp://example.org/x"}, "report_url"),
    ],
)
def test_rating_fields_are_checked(config, tracker_dir, change, error):
    store_issue(config, tracker_dir, make_issue(), [])
    (tracker_dir / "101" / "report.md").write_text("# report\n")
    (tracker_dir / "101" / "rating.yaml").write_text(
        yaml.safe_dump({**RATING, **change})
    )
    result = CliRunner().invoke(
        app, ["shadow-issues", "validate", "example", "--root", str(tracker_dir.parent)]
    )
    assert result.exit_code == 1 and error in result.output


def test_rating_needs_report_and_is_tabulated(config, tracker_dir):
    store_issue(config, tracker_dir, make_issue(), [])
    (tracker_dir / "101" / "rating.yaml").write_text(yaml.safe_dump(RATING))
    root = str(tracker_dir.parent)
    runner = CliRunner()
    result = runner.invoke(
        app, ["shadow-issues", "validate", "example", "--root", root]
    )
    assert result.exit_code == 1 and "no report.md" in result.output

    (tracker_dir / "101" / "report.md").write_text("# report\n")
    result = runner.invoke(
        app, ["shadow-issues", "validate", "example", "--root", root]
    )
    assert result.exit_code == 0, result.output

    result = runner.invoke(app, ["shadow-issues", "ratings", "example", "--root", root])
    assert "| example 101 |" in result.output and "DIFFERENT_MODEL" in result.output


def test_committed_tracker_validates():
    """The committed mirror stays schema-valid."""
    tracker = REPO_ROOT / "issues" / "go-annotation"
    assert TrackerConfig.load(tracker).repo == "geneontology/go-annotation"
    assert iter_issue_folders(tracker)
    result = CliRunner().invoke(
        app,
        ["shadow-issues", "validate", "go-annotation", "--root", str(tracker.parent)],
    )
    assert result.exit_code == 0, result.output
