#!/usr/bin/env python3
"""Deterministically squash-merge pull requests that satisfy a fixed policy.

This is intended as the non-agentic closing step of the PR Shepherd. It never
judges a change. It re-reads GitHub state immediately before merging and only
merges when every mechanical guard passes:

* the PR is open, non-draft, unassigned, and targets the configured base;
* the aggregate review decision is APPROVED;
* the PR is old enough, conflict-free, and GitHub reports a CLEAN merge state;
* every changed file is under a conservative content-path allowlist;
* every reported check is complete and non-failing, with at least one SUCCESS;
* every optionally named required check has an explicit SUCCESS result.

The initial bulk list is only a cheap candidate scan. GitHub computes
mergeability lazily and large bulk GraphQL requests for mergeStateStatus can
fail, so mergeability, exact-head approval, and checks are evaluated only on a
fresh per-PR view when configured. The final merge is pinned with
--match-head-commit.
The PR does not have to be rebased onto the latest base-branch tip. GitHub
re-evaluates mergeability against the current base, while the controller pins
the exact reviewed and tested head with ``--match-head-commit``. This matches
DisMech's closing policy and avoids rerunning CI and review for unrelated base
changes. Branch protection still requires the named head check, dismisses stale
approvals after a head push, resolves review threads, and grants neither
automation App a bypass. The workflow keeps execute mode behind a repository
feature flag until those settings are installed.

Production follows DisMech and relies on GitHub's aggregate APPROVED decision
plus branch protection that dismisses stale reviews after a head push. An
optional stricter Bot-identity gate remains available through repeatable
``--trusted-reviewer`` arguments, but the workflow does not enable it.

The closing pass intentionally does not filter by PR author or head repository.
An otherwise eligible human-authored or fork PR is in scope once GitHub reports
the aggregate review decision as APPROVED. Automatic agentic review is narrower,
but its author/branch ingress rules are not implicit merge-controller policy.

The controller is report-only by default. Actual merging requires the explicit
``--execute`` flag and a separate ``GH_MERGE_TOKEN`` credential. Read operations
continue to use the read-only ``GH_TOKEN``; the writer credential is injected
only into the merge and courtesy-comment subprocesses. ``--dry-run`` is retained
as a visible workflow guard. The ``shepherd:hold`` label, assignment, draft
state, and the separate ``auto/generate-*`` lane all veto this controller.
"""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
import time
from collections.abc import Iterable
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone


LIST_FIELDS = (
    "number,title,author,isDraft,createdAt,assignees,reviewDecision,"
    "mergeable,baseRefName,headRefName,labels,url"
)
VIEW_FIELDS = (
    LIST_FIELDS + ",state,statusCheckRollup,headRefOid,mergeStateStatus,changedFiles"
)

DEFAULT_TRUSTED_REVIEWERS: tuple[str, ...] = ()
DEFAULT_EXCLUDED_HEAD_PREFIXES = ("auto/generate-",)
DEFAULT_ALLOWED_PATH_PREFIXES = (
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
MAX_REST_CHANGED_FILES = 3_000
PASSING_CONCLUSIONS = frozenset({"SUCCESS", "SKIPPED", "NEUTRAL"})
PASSING_STATES = frozenset({"SUCCESS", "NEUTRAL"})

BENIGN_MERGE_FAILURES = (
    "head branch was modified",
    "base branch was modified",
    "already merged",
    "pull request is closed",
    "no commits between",
)
GH_STATUS_MARKERS = ("X ", "! ", "✓ ")

MERGE_COMMENT = (
    "🐑 **PR Shepherd** (deterministic sweep) — Squash-merged: approved, "
    "unassigned, no conflicts, all "
    "checks green, and open longer than {days} days. No further action needed."
)
TOO_YOUNG = "too_young"


@dataclass(frozen=True)
class Decision:
    """Outcome of applying the merge predicate to one PR."""

    eligible: bool
    reason: str
    code: str = ""


@dataclass(frozen=True)
class ChangedFileInventory:
    """Complete paths returned by one paginated REST file-list read."""

    filenames: tuple[str, ...]
    previous_filenames: tuple[str, ...] = ()


class HeadMovedError(ValueError):
    """A benign PR-head race observed while collecting a file inventory."""


def non_negative_int(value: str) -> int:
    """Parse an age threshold and reject values that widen it by accident."""
    parsed = int(value)
    if parsed < 0:
        raise argparse.ArgumentTypeError(
            f"must be zero or positive, got {parsed}; a negative threshold "
            "would merge PRs of any age"
        )
    return parsed


def positive_int(value: str) -> int:
    """Parse a strictly positive scan bound."""
    parsed = int(value)
    if parsed <= 0:
        raise argparse.ArgumentTypeError(f"must be positive, got {parsed}")
    return parsed


def non_empty(value: str) -> str:
    """Parse a repeatable name argument without accepting an empty guard."""
    parsed = value.strip()
    if not parsed:
        raise argparse.ArgumentTypeError("must not be empty")
    return parsed


def directory_path_prefix(value: str) -> str:
    """Parse a normalized directory prefix with an explicit path boundary."""
    parsed = non_empty(value)
    if not parsed.endswith("/"):
        raise argparse.ArgumentTypeError("must end with '/' to define a directory")
    directory = parsed[:-1]
    if (
        not directory
        or parsed.startswith("/")
        or "\\" in parsed
        or any(part in {"", ".", ".."} for part in directory.split("/"))
        or any(ord(character) < 32 or ord(character) == 127 for character in parsed)
    ):
        raise argparse.ArgumentTypeError(
            "must be a normalized relative directory prefix"
        )
    return parsed


def normalize_login(login: str) -> str:
    """Normalize GitHub App login spellings without broadening trust."""
    normalized = login.strip().casefold()
    if normalized.startswith("app/"):
        normalized = normalized.removeprefix("app/")
    if normalized.endswith("[bot]"):
        normalized = normalized.removesuffix("[bot]")
    return normalized


def trusted_reviewer_login(value: str) -> str:
    """Parse a trusted Bot login and reject spellings that normalize empty."""
    parsed = non_empty(value)
    if not normalize_login(parsed):
        raise argparse.ArgumentTypeError(
            "must identify a Bot login after removing app/ and [bot] markers"
        )
    return parsed


def _parse_ts(value: str) -> datetime:
    return datetime.fromisoformat(value)


def _review_author_login(review: dict) -> str:
    # Invariant: load-bearing reviews come only from list_pr_reviews' REST data.
    user = review.get("user")
    if isinstance(user, dict):
        return str(user.get("login") or "")
    return ""


def _review_author_is_bot(review: dict) -> bool:
    """Require the load-bearing REST author to carry GitHub's Bot identity type."""
    user = review.get("user")
    return isinstance(user, dict) and str(user.get("type") or "").casefold() == "bot"


def _review_commit_oid(review: dict) -> str:
    if review.get("commit_id"):
        return str(review["commit_id"])
    commit = review.get("commit")
    if isinstance(commit, dict):
        return str(commit.get("oid") or "")
    return str(commit or "")


def trusted_head_approval_decision(
    reviews: list[dict] | None,
    *,
    head_sha: str,
    trusted_reviewers: Iterable[str],
) -> Decision:
    """Require an APPROVED review on exactly the current head.

    When ``trusted_reviewers`` is non-empty, additionally require an allowlisted
    Bot identity.  An empty allowlist deliberately matches DisMech's aggregate
    reviewer policy while retaining controller-side exact-head binding.
    """
    if not head_sha.strip():
        return Decision(False, "no head SHA in the API response")

    trusted = {normalize_login(login) for login in trusted_reviewers}
    trusted.discard("")

    approvals_on_other_commits: set[str] = set()
    approvals_without_bot_identity: set[str] = set()
    for review in reviews or []:
        if (review.get("state") or "").upper() != "APPROVED":
            continue
        login = normalize_login(_review_author_login(review))
        if trusted:
            if login not in trusted:
                continue
            if not _review_author_is_bot(review):
                approvals_without_bot_identity.add(login)
                continue
        review_sha = _review_commit_oid(review).strip()
        if review_sha.casefold() == head_sha.strip().casefold() and review_sha:
            reviewer = login or "a reviewer"
            return Decision(True, f"current head approved by {reviewer}")
        approvals_on_other_commits.add(login or "a reviewer")

    if approvals_on_other_commits:
        reviewers = ", ".join(sorted(approvals_on_other_commits))
        return Decision(
            False,
            f"approval by {reviewers} is not for current head {head_sha}",
        )
    if approvals_without_bot_identity:
        reviewers = ", ".join(sorted(approvals_without_bot_identity))
        return Decision(
            False,
            f"allowlisted approval did not have a verified Bot identity: {reviewers}",
        )
    if trusted:
        return Decision(False, "no trusted reviewer approved the current head")
    return Decision(False, "no approval is bound to the current head")


def _check_name(entry: dict) -> str:
    return str(entry.get("name") or entry.get("context") or "(unnamed check)")


def _is_check_run(entry: dict) -> bool:
    typename = entry.get("__typename")
    if typename:
        return typename == "CheckRun"
    return "conclusion" in entry or "status" in entry


def _is_explicit_success(entry: dict) -> bool:
    if _is_check_run(entry):
        return (entry.get("status") or "").upper() == "COMPLETED" and (
            entry.get("conclusion") or ""
        ).upper() == "SUCCESS"
    return (entry.get("state") or "").upper() == "SUCCESS"


def check_rollup_decision(
    rollup: list[dict] | None,
    *,
    required_checks: Iterable[str] = (),
) -> Decision:
    """Require all reported checks green and named checks explicitly successful."""
    if not rollup:
        return Decision(False, "no status checks reported on the head commit")

    pending: list[str] = []
    failing: list[str] = []
    successes = 0

    for entry in rollup:
        name = _check_name(entry)
        if _is_check_run(entry):
            status = (entry.get("status") or "").upper()
            conclusion = (entry.get("conclusion") or "").upper()
            if status != "COMPLETED" or not conclusion:
                pending.append(name)
            elif conclusion in PASSING_CONCLUSIONS:
                if conclusion == "SUCCESS":
                    successes += 1
            else:
                failing.append(f"{name}={conclusion.lower()}")
        else:
            state = (entry.get("state") or "").upper()
            if state in {"PENDING", "EXPECTED"} or not state:
                pending.append(name)
            elif state in PASSING_STATES:
                if state == "SUCCESS":
                    successes += 1
            else:
                failing.append(f"{name}={state.lower()}")

    if failing:
        return Decision(False, "checks not passing: " + ", ".join(sorted(failing)))
    if pending:
        return Decision(False, "checks still running: " + ", ".join(sorted(pending)))
    if not successes:
        return Decision(False, "no successful check on the head commit")

    required = tuple(
        dict.fromkeys(name.strip() for name in required_checks if name.strip())
    )
    missing = [
        name
        for name in required
        if not any(
            _check_name(entry) == name and _is_explicit_success(entry)
            for entry in rollup
        )
    ]
    if missing:
        return Decision(
            False,
            "required checks not explicitly successful: " + ", ".join(missing),
        )
    return Decision(True, f"{successes} check(s) passing")


def changed_files_decision(
    changed_files: list[str] | None,
    *,
    expected_file_count: object,
    previous_filenames: list[str] | None = None,
    allowed_path_prefixes: Iterable[str] = (),
) -> Decision:
    """Require every changed file to stay within a conservative content scope."""
    if (
        isinstance(expected_file_count, bool)
        or not isinstance(expected_file_count, int)
        or expected_file_count <= 0
    ):
        return Decision(
            False, "no valid total changed-file count in the PR API response"
        )
    if expected_file_count > MAX_REST_CHANGED_FILES:
        return Decision(
            False,
            f"PR reports {expected_file_count} changed files, exceeding the REST "
            f"completeness cap of {MAX_REST_CHANGED_FILES}",
        )
    if not changed_files:
        return Decision(False, "no changed files in the REST API response")
    previous_filenames = previous_filenames or []

    prefixes = tuple(
        dict.fromkeys(
            (
                *DEFAULT_ALLOWED_PATH_PREFIXES,
                *(prefix.strip() for prefix in allowed_path_prefixes if prefix.strip()),
            )
        )
    )
    malformed = [
        path
        for path in (*changed_files, *previous_filenames)
        if not isinstance(path, str) or not path.strip()
    ]
    if malformed:
        return Decision(False, "malformed changed-file data in the REST API response")

    non_normalized = [
        path
        for path in (*changed_files, *previous_filenames)
        if path != path.strip()
        or path.startswith("/")
        or "\\" in path
        or any(part in {"", ".", ".."} for part in path.split("/"))
        or any(ord(character) < 32 or ord(character) == 127 for character in path)
    ]
    if non_normalized:
        return Decision(
            False,
            "non-normalized changed-file path in the REST API response: "
            + ", ".join(repr(path) for path in non_normalized),
        )

    if len(set(changed_files)) != len(changed_files):
        return Decision(False, "duplicate filenames in the REST API response")
    if len(changed_files) != expected_file_count:
        return Decision(
            False,
            f"REST returned {len(changed_files)} changed file(s), but the PR API "
            f"reports {expected_file_count}",
        )

    disallowed = sorted(
        path
        for path in (*changed_files, *previous_filenames)
        if not any(path.startswith(prefix) for prefix in prefixes)
    )
    if disallowed:
        return Decision(
            False,
            "changed files outside the allowed path scope: " + ", ".join(disallowed),
        )
    return Decision(True, f"{len(changed_files)} changed file(s) in allowed paths")


def evaluate(
    pr: dict,
    *,
    now: datetime,
    min_age_days: int,
    base_branch: str,
    trusted_reviewers: Iterable[str] = DEFAULT_TRUSTED_REVIEWERS,
    required_checks: Iterable[str] = (),
    hold_label: str = "shepherd:hold",
    excluded_head_prefixes: Iterable[str] = DEFAULT_EXCLUDED_HEAD_PREFIXES,
    allowed_path_prefixes: Iterable[str] = (),
    final: bool = True,
) -> Decision:
    """Apply cheap list guards or the complete final merge predicate."""
    state = (pr.get("state") or "").upper()
    if final and not state:
        return Decision(False, "no state in the API response")
    if state and state != "OPEN":
        return Decision(False, f"not open (state={state.lower()})")
    if pr.get("isDraft"):
        return Decision(False, "draft")
    if pr.get("baseRefName") != base_branch:
        return Decision(
            False, f"base branch is {pr.get('baseRefName')!r}, not {base_branch!r}"
        )

    head_ref = str(pr.get("headRefName") or "")
    excluded_prefix = next(
        (prefix for prefix in excluded_head_prefixes if head_ref.startswith(prefix)),
        None,
    )
    if excluded_prefix:
        return Decision(False, f"head branch is in excluded lane {excluded_prefix!r}")

    labels = {
        str(label.get("name") or "") if isinstance(label, dict) else str(label)
        for label in (pr.get("labels") or [])
    }
    if hold_label in labels:
        return Decision(False, f"held by label {hold_label!r}")

    assignees = pr.get("assignees") or []
    if assignees:
        logins = ", ".join(a.get("login", "?") for a in assignees)
        return Decision(False, f"assigned to {logins}")

    review = (pr.get("reviewDecision") or "").upper()
    if review != "APPROVED":
        return Decision(
            False, f"review decision is {review.lower() or 'none'}, not approved"
        )

    created = _parse_ts(pr["createdAt"])
    age = now - created
    if age < timedelta(days=min_age_days):
        hours = age.total_seconds() / 3600
        return Decision(False, f"only {hours:.0f}h old (<{min_age_days}d)", TOO_YOUNG)

    mergeable = (pr.get("mergeable") or "").upper()
    if mergeable == "CONFLICTING":
        return Decision(False, "merge conflicts with the base branch")

    if not final:
        return Decision(True, "candidate (pending per-PR verification)")

    paths = changed_files_decision(
        pr.get("changed_files"),
        expected_file_count=pr.get("changedFiles"),
        previous_filenames=pr.get("previous_changed_filenames"),
        allowed_path_prefixes=allowed_path_prefixes,
    )
    if not paths.eligible:
        return paths

    approval = trusted_head_approval_decision(
        pr.get("reviews"),
        head_sha=str(pr.get("headRefOid") or "").strip(),
        trusted_reviewers=trusted_reviewers,
    )
    if not approval.eligible:
        return approval

    if mergeable != "MERGEABLE":
        return Decision(False, f"mergeability is {mergeable.lower() or 'unset'}")
    merge_state = (pr.get("mergeStateStatus") or "").upper()
    if merge_state != "CLEAN":
        return Decision(
            False, f"merge state is {merge_state.lower() or 'unset'}, not clean"
        )

    checks = check_rollup_decision(
        pr.get("statusCheckRollup"), required_checks=required_checks
    )
    if not checks.eligible:
        return checks
    return Decision(True, f"ready ({age.days}d old)")


def _gh(args: list[str], *, token: str | None = None) -> str:
    env = os.environ.copy()
    # Never leak the dedicated writer credential to discovery subprocesses (or
    # under its nonstandard name to any child). Only the explicit write calls
    # replace GH_TOKEN with it.
    env.pop("GH_MERGE_TOKEN", None)
    if token is not None:
        env["GH_TOKEN"] = token
    result = subprocess.run(
        ["gh", *args], check=True, capture_output=True, text=True, env=env
    )
    return result.stdout


def _gh_error(exc: subprocess.CalledProcessError) -> str:
    for line in (exc.stderr or "").splitlines():
        cleaned = line.strip()
        for marker in GH_STATUS_MARKERS:
            cleaned = cleaned.removeprefix(marker)
        cleaned = cleaned.strip()
        if cleaned:
            return cleaned
    return f"gh exited {exc.returncode}"


def is_benign_merge_failure(stderr: str) -> bool:
    lowered = stderr.lower()
    return any(marker in lowered for marker in BENIGN_MERGE_FAILURES)


def list_open_prs(repo: str, limit: int, base_branch: str) -> list[dict]:
    out = _gh(
        [
            "pr",
            "list",
            "--repo",
            repo,
            "--state",
            "open",
            "--base",
            base_branch,
            "--limit",
            str(limit),
            "--json",
            LIST_FIELDS,
        ]
    )
    return json.loads(out)


def view_pr(repo: str, number: int, *, attempts: int = 5, delay: float = 2.0) -> dict:
    """Fetch one PR, retrying UNKNOWN mergeability with exponential backoff."""
    pr: dict = {}
    for attempt in range(attempts):
        pr = json.loads(
            _gh(["pr", "view", str(number), "--repo", repo, "--json", VIEW_FIELDS])
        )
        unresolved = {
            (pr.get("mergeable") or "").upper(),
            (pr.get("mergeStateStatus") or "").upper(),
        }
        if "UNKNOWN" not in unresolved:
            return pr
        if attempt < attempts - 1:
            time.sleep(delay * (2**attempt))
    unresolved_fields = [
        field
        for field in ("mergeable", "mergeStateStatus")
        if (pr.get(field) or "").upper() == "UNKNOWN"
    ]
    raise ValueError(
        "mergeability remained UNKNOWN after "
        f"{attempts} attempt(s): {', '.join(unresolved_fields)}"
    )


def list_pr_reviews(repo: str, number: int) -> list[dict]:
    """Fetch all reviews with the load-bearing reviewer and commit fields."""
    pages = json.loads(
        _gh(
            [
                "api",
                "--paginate",
                "--slurp",
                f"repos/{repo}/pulls/{number}/reviews?per_page=100",
            ]
        )
    )
    if not isinstance(pages, list):
        raise ValueError("review API did not return a list of pages")
    reviews: list[dict] = []
    for page in pages:
        if not isinstance(page, list):
            raise ValueError("review API page was not a list")
        reviews.extend(review for review in page if isinstance(review, dict))
    return reviews


def list_pr_files(repo: str, number: int) -> ChangedFileInventory:
    """Fetch and strictly validate every changed filename from paginated REST."""
    pages = json.loads(
        _gh(
            [
                "api",
                "--paginate",
                "--slurp",
                f"repos/{repo}/pulls/{number}/files?per_page=100",
            ]
        )
    )
    if not isinstance(pages, list) or not pages:
        raise ValueError("file API did not return a non-empty list of pages")

    filenames: list[str] = []
    previous_filenames: list[str] = []
    for page in pages:
        if not isinstance(page, list):
            raise ValueError("file API page was not a list")
        if not page:
            raise ValueError("file API page was empty")
        for entry in page:
            if not isinstance(entry, dict):
                raise ValueError("file API entry was not an object")
            filename = entry.get("filename")
            if not isinstance(filename, str) or not filename.strip():
                raise ValueError("file API entry had no valid filename")
            filenames.append(filename)
            previous_filename = entry.get("previous_filename")
            if previous_filename is not None:
                if (
                    not isinstance(previous_filename, str)
                    or not previous_filename.strip()
                ):
                    raise ValueError("file API entry had no valid previous filename")
                previous_filenames.append(previous_filename)
            elif str(entry.get("status") or "").casefold() == "renamed":
                raise ValueError("renamed file API entry had no previous filename")
    if not filenames:
        raise ValueError("file API returned no changed files")
    return ChangedFileInventory(tuple(filenames), tuple(previous_filenames))


def view_pr_head_sha(
    repo: str, number: int, *, attempts: int = 5, delay: float = 2.0
) -> str:
    """Re-read the live PR head, retrying transient API errors or empty data."""
    args = [
        "pr",
        "view",
        str(number),
        "--repo",
        repo,
        "--json",
        "headRefOid",
        "--jq",
        ".headRefOid",
    ]
    for attempt in range(attempts):
        try:
            oid = _gh(args).strip()
        except subprocess.CalledProcessError:
            if attempt == attempts - 1:
                raise
        else:
            if oid:
                return oid
            if attempt == attempts - 1:
                raise ValueError(f"could not resolve the current head for PR #{number}")
        time.sleep(delay * (2**attempt))
    raise AssertionError("unreachable head-SHA retry state")


def require_unchanged_file_inventory_head(
    repo: str, number: int, expected_head_sha: object
) -> None:
    """Reject a file inventory if the PR head moved while it was being read."""
    expected = str(expected_head_sha or "").strip()
    if not expected:
        raise ValueError(f"PR #{number} had no head SHA before the file-list read")
    observed = view_pr_head_sha(repo, number)
    if observed.casefold() != expected.casefold():
        raise HeadMovedError(
            f"PR #{number} head moved during the file-list read: "
            f"{expected} -> {observed}"
        )


def merge_pr(
    repo: str,
    number: int,
    min_age_days: int,
    head_sha: str,
    write_token: str,
) -> None:
    """Squash-merge exactly the verified head, then post a courtesy comment."""
    head_sha = head_sha.strip()
    if not head_sha:
        raise ValueError("refusing to merge without a verified head SHA")
    write_token = write_token.strip()
    if not write_token:
        raise ValueError("refusing to merge without a dedicated write token")
    _gh(
        [
            "pr",
            "merge",
            str(number),
            "--repo",
            repo,
            "--squash",
            "--match-head-commit",
            head_sha,
        ],
        token=write_token,
    )
    try:
        _gh(
            [
                "pr",
                "comment",
                str(number),
                "--repo",
                repo,
                "--body",
                MERGE_COMMENT.format(days=min_age_days),
            ],
            token=write_token,
        )
    except subprocess.CalledProcessError as exc:
        print(
            f"WARN  #{number}: merged, but posting the comment failed: {_gh_error(exc)}",
            file=sys.stderr,
        )


def render_summary(
    merged: list[dict],
    skipped: list[dict],
    failed: list[dict],
    *,
    dry_run: bool = False,
) -> str:
    title = "## 🐑 Deterministic auto-merge sweep"
    if dry_run:
        title += " (dry run — nothing was merged)"
    lines = [title, ""]
    verb = "Would merge" if dry_run else "Merged"
    if merged:
        lines.append(f"**{verb} {len(merged)}:**")
        lines += [f"- #{row['number']} — {row['title']}" for row in merged]
        if dry_run and len(merged) > 1:
            lines.extend(
                [
                    "",
                    "_Each candidate is re-read before a head-pinned merge. Unrelated "
                    "changes on `main` do not require a branch refresh, CI rerun, or "
                    "new review._",
                ]
            )
    else:
        lines.append(f"**{verb} 0** — nothing met every criterion.")
    lines.append("")
    if failed:
        lines.append(f"**Failed to merge {len(failed)}:**")
        lines += [f"- #{row['number']} — {row['reason']}" for row in failed]
        lines.append("")
    if skipped:
        lines.append(
            f"<details><summary>Skipped {len(skipped)} near-miss PR(s)</summary>"
        )
        lines.append("")
        lines += [f"- #{row['number']} — {row['reason']}" for row in skipped]
        lines.extend(["", "</details>"])
    return "\n".join(lines) + "\n"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--repo", required=True, help="owner/name of the repository")
    parser.add_argument(
        "--min-age-days",
        type=non_negative_int,
        default=3,
        help="minimum PR age in days (default: 3; 0 disables the age gate)",
    )
    parser.add_argument(
        "--base-branch",
        default="main",
        help="only merge PRs targeting this branch (default: main)",
    )
    parser.add_argument(
        "--limit",
        type=positive_int,
        default=300,
        help="max open PRs to scan (default: 300)",
    )
    parser.add_argument(
        "--trusted-reviewer",
        action="append",
        type=trusted_reviewer_login,
        default=[],
        help=(
            "require this Bot reviewer to approve the exact head; repeatable "
            "and optional (production relies on GitHub's APPROVED decision)"
        ),
    )
    parser.add_argument(
        "--allowed-path-prefix",
        action="append",
        type=directory_path_prefix,
        default=[],
        help=(
            "additional normalized directory prefix allowed by the merge controller; "
            "must end with '/', repeatable (the conservative defaults always remain)"
        ),
    )
    parser.add_argument(
        "--required-check",
        action="append",
        type=non_empty,
        default=[],
        help="check name that must explicitly succeed; repeatable (default: none)",
    )
    parser.add_argument(
        "--hold-label",
        type=non_empty,
        default="shepherd:hold",
        help="label that vetoes automatic merging (default: shepherd:hold)",
    )
    parser.add_argument(
        "--exclude-head-prefix",
        action="append",
        type=non_empty,
        default=[],
        help=(
            "additional head prefix excluded from this lane; repeatable "
            "(auto/generate- is always excluded)"
        ),
    )
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument(
        "--execute",
        action="store_true",
        help="perform eligible merges; without this flag the controller only reports",
    )
    mode.add_argument(
        "--dry-run",
        action="store_true",
        help="explicitly report without merging (also the default)",
    )
    parser.add_argument(
        "--summary-file",
        default=os.environ.get("GITHUB_STEP_SUMMARY"),
        help="append a markdown report here (default: GITHUB_STEP_SUMMARY)",
    )
    args = parser.parse_args(argv)
    if args.execute and not args.required_check:
        parser.error("--execute requires at least one --required-check")
    write_token = os.environ.get("GH_MERGE_TOKEN", "").strip()
    if args.execute and not write_token:
        parser.error("--execute requires a non-empty GH_MERGE_TOKEN")

    trusted_reviewers = tuple(args.trusted_reviewer)
    excluded_head_prefixes = (
        *DEFAULT_EXCLUDED_HEAD_PREFIXES,
        *args.exclude_head_prefix,
    )
    dry_run = not args.execute
    now = datetime.now(timezone.utc)
    prs = list_open_prs(args.repo, args.limit, args.base_branch)
    if len(prs) >= args.limit:
        print(
            f"WARNING: hit the --limit of {args.limit} open PRs; older PRs were "
            "not scanned. Raise --limit.",
            file=sys.stderr,
        )

    candidates: list[dict] = []
    skipped: list[dict] = []
    for pr in prs:
        decision = evaluate(
            pr,
            now=now,
            min_age_days=args.min_age_days,
            base_branch=args.base_branch,
            trusted_reviewers=trusted_reviewers,
            required_checks=args.required_check,
            hold_label=args.hold_label,
            excluded_head_prefixes=excluded_head_prefixes,
            allowed_path_prefixes=args.allowed_path_prefix,
            final=False,
        )
        if decision.eligible:
            candidates.append(pr)
        elif (
            pr.get("reviewDecision") or ""
        ).upper() == "APPROVED" and decision.code != TOO_YOUNG:
            skipped.append({"number": pr["number"], "reason": decision.reason})

    print(
        f"Scanned {len(prs)} open PR(s); {len(candidates)} passed the "
        "list-level predicate."
    )

    # Process oldest PR first, then PR number as a stable tie-breaker, rather
    # than relying on the changing default order of `gh pr list`.
    candidates.sort(key=lambda pr: (_parse_ts(pr["createdAt"]), int(pr["number"])))

    merged: list[dict] = []
    failed: list[dict] = []
    for pr in candidates:
        number = pr["number"]
        try:
            fresh = view_pr(args.repo, number)
            fresh["reviews"] = list_pr_reviews(args.repo, number)
            files = list_pr_files(args.repo, number)
            fresh["changed_files"] = list(files.filenames)
            fresh["previous_changed_filenames"] = list(files.previous_filenames)
            require_unchanged_file_inventory_head(
                args.repo, number, fresh.get("headRefOid")
            )
        except HeadMovedError as exc:
            reason = str(exc)
            print(f"SKIP  #{number}: {reason}")
            skipped.append({"number": number, "reason": reason})
            continue
        except (subprocess.CalledProcessError, ValueError) as exc:
            detail = (
                _gh_error(exc)
                if isinstance(exc, subprocess.CalledProcessError)
                else str(exc)
            )
            reason = f"could not re-verify: {detail}"
            if dry_run:
                print(f"SKIP  #{number}: {reason}", file=sys.stderr)
                skipped.append({"number": number, "reason": reason})
            else:
                print(f"FAIL  #{number}: {reason}", file=sys.stderr)
                failed.append({"number": number, "reason": reason})
            continue

        decision = evaluate(
            fresh,
            now=datetime.now(timezone.utc),
            min_age_days=args.min_age_days,
            base_branch=args.base_branch,
            trusted_reviewers=trusted_reviewers,
            required_checks=args.required_check,
            hold_label=args.hold_label,
            excluded_head_prefixes=excluded_head_prefixes,
            allowed_path_prefixes=args.allowed_path_prefix,
        )
        if not decision.eligible:
            print(f"SKIP  #{number}: {decision.reason}")
            skipped.append({"number": number, "reason": decision.reason})
            continue
        if dry_run:
            print(
                f"DRY-RUN would merge #{number}: {fresh['title']} — {decision.reason}"
            )
            merged.append({"number": number, "title": fresh["title"]})
            continue
        # Re-read every load-bearing field immediately before the write. This
        # catches a newly added hold/assignee, review or check change, and head
        # movement. The exact reviewed/tested head remains pinned at merge time.
        try:
            fresh = view_pr(args.repo, number)
            fresh["reviews"] = list_pr_reviews(args.repo, number)
            files = list_pr_files(args.repo, number)
            fresh["changed_files"] = list(files.filenames)
            fresh["previous_changed_filenames"] = list(files.previous_filenames)
            require_unchanged_file_inventory_head(
                args.repo, number, fresh.get("headRefOid")
            )
        except HeadMovedError as exc:
            reason = str(exc)
            print(f"SKIP  #{number}: {reason}")
            skipped.append({"number": number, "reason": reason})
            continue
        except (subprocess.CalledProcessError, ValueError) as exc:
            detail = (
                _gh_error(exc)
                if isinstance(exc, subprocess.CalledProcessError)
                else str(exc)
            )
            reason = f"could not perform final re-verification: {detail}"
            print(f"FAIL  #{number}: {reason}", file=sys.stderr)
            failed.append({"number": number, "reason": reason})
            continue

        final_decision = evaluate(
            fresh,
            now=datetime.now(timezone.utc),
            min_age_days=args.min_age_days,
            base_branch=args.base_branch,
            trusted_reviewers=trusted_reviewers,
            required_checks=args.required_check,
            hold_label=args.hold_label,
            excluded_head_prefixes=excluded_head_prefixes,
            allowed_path_prefixes=args.allowed_path_prefix,
        )
        if not final_decision.eligible:
            reason = f"state changed after verification: {final_decision.reason}"
            print(f"SKIP  #{number}: {reason}")
            skipped.append({"number": number, "reason": reason})
            continue
        try:
            merge_pr(
                args.repo,
                number,
                args.min_age_days,
                fresh["headRefOid"],
                write_token,
            )
        except subprocess.CalledProcessError as exc:
            reason = _gh_error(exc)
            if is_benign_merge_failure(exc.stderr or reason):
                print(f"SKIP  #{number}: {reason}")
                skipped.append({"number": number, "reason": reason})
            else:
                print(f"FAIL  #{number}: {reason}", file=sys.stderr)
                failed.append({"number": number, "reason": reason})
            continue
        print(f"MERGED #{number}: {fresh['title']}")
        merged.append({"number": number, "title": fresh["title"]})

    report = render_summary(merged, skipped, failed, dry_run=dry_run)
    print()
    print(report)
    if args.summary_file:
        with open(args.summary_file, "a", encoding="utf-8") as handle:
            handle.write(report)
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
