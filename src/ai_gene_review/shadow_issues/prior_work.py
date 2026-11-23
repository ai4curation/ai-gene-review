"""Find commits in this repository that name an upstream issue (``NAMES_ISSUE`` prior work).

Such a commit was made with the issue's thread in view, so shadow work on that
issue cannot be blind to it. The derivation is reproducible:
``ai-gene-review shadow-issues backfill-prior-work`` rewrites every issue's
``NAMES_ISSUE`` entries from ``git log`` and leaves ``COVERS_SUBJECT`` entries,
which are curated, alone.
"""

from __future__ import annotations

import re
import subprocess
from collections import defaultdict
from pathlib import Path
from typing import Any

#: A commit naming more issues than this is a bulk (squash or batch) commit.
BULK_THRESHOLD = 3


def issue_numbers(message: str, tracker: str) -> set[int]:
    """Upstream issue numbers a commit message names.

    Matches the forms this project asks authors to use, ``issues/<tracker>/N`` and
    ``<tracker> N``, and the older forms ``<tracker>#N``, ``<tracker>/issues/N``
    and ``<tracker> issue N``. The bare ``<tracker> N`` form needs a number of at
    least three digits that does not start a range, so "go-annotation 5516-6649"
    (a span of issues, not one) is not read as naming issue 5516.

    >>> sorted(issue_numbers("Fix (go-annotation#6591); see geneontology/go-annotation/issues/6414", "go-annotation"))
    [6414, 6591]
    >>> sorted(issue_numbers("go-annotation issue #5886 and the go-annotation tracker", "go-annotation"))
    [5886]
    >>> sorted(issue_numbers("Shadows issues/go-annotation/6700; cf. go-annotation 6701.", "go-annotation"))
    [6700, 6701]
    >>> issue_numbers("Backfilled go-annotation 5516-6649 and go-annotation 5516–6649", "go-annotation")
    set()
    >>> issue_numbers("Bump (#168); go-annotation 12 rows", "go-annotation")
    set()
    """
    t = re.escape(tracker)
    pattern = re.compile(
        rf"(?:issues/{t}/|{t}(?:#|/issues/| issue #?))(\d+)\b"
        rf"|(?<![/\w]){t} (\d{{3,}})\b(?!\s*[-–]\s*\d)"
    )
    return {int(a or b) for a, b in pattern.findall(message)}


def _is_shallow(repo_root: Path) -> bool:
    out = subprocess.run(
        ["git", "rev-parse", "--is-shallow-repository"],
        cwd=repo_root,
        capture_output=True,
        text=True,
        check=True,
    ).stdout.strip()
    return out == "true"


def shallow_boundary(repo_root: Path) -> list[str]:
    """Commits whose parents a shallow clone hides; empty for a full clone."""
    path = subprocess.run(
        ["git", "rev-parse", "--git-path", "shallow"],
        cwd=repo_root,
        capture_output=True,
        text=True,
        check=True,
    ).stdout.strip()
    shallow = (repo_root / path) if not Path(path).is_absolute() else Path(path)
    return (
        shallow.read_text().split()
        if _is_shallow(repo_root) and shallow.exists()
        else []
    )


def commits_naming_issues(
    repo_root: Path, tracker: str, allow_shallow: bool = False
) -> dict[int, list[dict[str, Any]]]:
    """Map issue number to the commits naming it, newest first.

    Each entry has ``commit`` (12-character hash), ``subject``, and ``bulk`` (the
    commit names more than :data:`BULK_THRESHOLD` issues).

    A commit that touches the issue's own folder ``issues/<tracker>/N/`` is the
    shadow protocol's own record (triage, shadow work, a rating, or the commit
    that created the mirror), not prior work, so it is skipped for that issue.

    Raises on a shallow clone, whose truncated history would silently drop
    entries, unless ``allow_shallow`` is set by someone who has checked that the
    hidden commits name no issue (see :func:`shallow_boundary`).
    """
    if _is_shallow(repo_root) and not allow_shallow:
        raise RuntimeError(
            "git history is shallow (boundary: "
            + ", ".join(c[:12] for c in shallow_boundary(repo_root))
            + "); fetch the full history (git fetch --unshallow), or pass "
            "--allow-shallow after checking the hidden commits name no issue"
        )
    log = subprocess.run(
        ["git", "log", "--name-only", "--format=%x1e%H%x00%s%x00%B%x1f"],
        cwd=repo_root,
        capture_output=True,
        text=True,
        check=True,
    ).stdout
    found: dict[int, list[dict[str, Any]]] = defaultdict(list)
    for entry in log.split("\x1e"):
        if not entry.strip():
            continue
        header, _, files = entry.partition("\x1f")
        sha, subject, body = header.strip("\n").split("\x00", 2)
        touched = set(files.split())
        numbers = issue_numbers(f"{subject}\n{body}", tracker)
        for number in numbers:
            own = f"issues/{tracker}/{number}/"
            if any(path.startswith(own) for path in touched):
                continue
            found[number].append(
                {
                    "commit": sha[:12],
                    "subject": subject,
                    "bulk": len(numbers) > BULK_THRESHOLD,
                }
            )
    return found


def names_issue_entries(commits: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """``prior_work`` entries for one issue, oldest first.

    Bulk commits are dropped when a specific commit also names the issue; when
    only bulk commits do, they are kept with a note.

    >>> names_issue_entries([{"commit": "b", "subject": "Batch", "bulk": True},
    ...                      {"commit": "a", "subject": "Fix it", "bulk": False}])
    [{'relation': 'NAMES_ISSUE', 'commit': 'a', 'subject': 'Fix it'}]
    >>> names_issue_entries([{"commit": "b", "subject": "Batch", "bulk": True}])[0]["note"]
    'Bulk commit naming more than 3 upstream issues; the work for this issue is one part of it.'
    """
    specific = [c for c in commits if not c["bulk"]]
    chosen = specific or commits
    entries = []
    for c in reversed(chosen):
        entry = {
            "relation": "NAMES_ISSUE",
            "commit": c["commit"],
            "subject": c["subject"],
        }
        if c["bulk"]:
            entry["note"] = (
                f"Bulk commit naming more than {BULK_THRESHOLD} upstream issues; "
                "the work for this issue is one part of it."
            )
        entries.append(entry)
    return entries


def merge_prior_work(
    existing: list[dict[str, Any]], names_issue: list[dict[str, Any]]
) -> list[dict[str, Any]]:
    """Replace the NAMES_ISSUE entries in ``existing``, keeping every other entry.

    >>> merge_prior_work([{"relation": "NAMES_ISSUE", "commit": "old"},
    ...                   {"relation": "COVERS_SUBJECT", "commit": "c"}],
    ...                  [{"relation": "NAMES_ISSUE", "commit": "new"}])
    [{'relation': 'NAMES_ISSUE', 'commit': 'new'}, {'relation': 'COVERS_SUBJECT', 'commit': 'c'}]
    """
    return names_issue + [e for e in existing if e.get("relation") != "NAMES_ISSUE"]
