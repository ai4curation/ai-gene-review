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

    Matches ``<tracker>#N``, ``<tracker>/issues/N`` and ``<tracker> issue N``.

    >>> sorted(issue_numbers("Fix (go-annotation#6591); see geneontology/go-annotation/issues/6414", "go-annotation"))
    [6414, 6591]
    >>> sorted(issue_numbers("go-annotation issue #5886 and the go-annotation tracker", "go-annotation"))
    [5886]
    >>> issue_numbers("Bump (#168)", "go-annotation")
    set()
    """
    pattern = re.compile(rf"{re.escape(tracker)}(?:#|/issues/| issue #?)(\d+)\b")
    return {int(n) for n in pattern.findall(message)}


def commits_naming_issues(
    repo_root: Path, tracker: str
) -> dict[int, list[dict[str, Any]]]:
    """Map issue number to the commits naming it, newest first.

    Each entry has ``commit`` (12-character hash), ``subject``, and ``bulk`` (the
    commit names more than :data:`BULK_THRESHOLD` issues).
    """
    log = subprocess.run(
        ["git", "log", "--format=%H%x00%s%x00%B%x1e"],
        cwd=repo_root,
        capture_output=True,
        text=True,
        check=True,
    ).stdout
    found: dict[int, list[dict[str, Any]]] = defaultdict(list)
    for entry in log.split("\x1e"):
        if not entry.strip():
            continue
        sha, subject, body = entry.strip("\n").split("\x00", 2)
        numbers = issue_numbers(f"{subject}\n{body}", tracker)
        for number in numbers:
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
