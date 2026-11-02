"""Repository-wide pytest guard: no test session may write into committed data.

This lives at the repository root, not in ``tests/``, because the root conftest
is loaded for every invocation under the rootdir, including
``pytest --doctest-modules src``, which never loads ``tests/conftest.py``.
"""

import subprocess
from pathlib import Path
from typing import Optional

import pytest

REPO_ROOT = Path(__file__).resolve().parent
# Committed curated data and caches that no test may write to; tests use tmp_path.
PROTECTED_TREES = ("publications", "genes", "reactome")

_status_key = pytest.StashKey[Optional[str]]()
_changes_key = pytest.StashKey[list[str]]()


def _protected_tree_status() -> Optional[str]:
    """Return git's porcelain status of the protected trees, or None without git.

    Untracked files are included, so a newly cached ``PMID_*.md`` counts too;
    git-ignored files are not. The status lines carry no content hash, so the
    comparison is blind to further edits to a file that was already modified
    before the session, and it attributes any change made during the session
    (an editor save, a concurrent ``just fetch-gene``) to the tests.
    """
    try:
        result = subprocess.run(
            ["git", "status", "--porcelain", "--untracked-files=all", "--", *PROTECTED_TREES],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
            check=True,
        )
    except (OSError, subprocess.CalledProcessError):  # not a git checkout
        return None
    return result.stdout


def pytest_sessionstart(session):
    """Snapshot the protected trees before any test runs."""
    session.config.stash[_status_key] = _protected_tree_status()


def pytest_sessionfinish(session, exitstatus):
    """Fail an otherwise passing run if the protected trees changed during it."""
    before = session.config.stash.get(_status_key, None)
    if before is None:
        return
    after = _protected_tree_status()
    if after is None or after == before:
        return
    changed = sorted(set(after.splitlines()) - set(before.splitlines()))
    session.config.stash[_changes_key] = changed or [
        "(status changed for files already modified before the run)"
    ]
    # Keep more specific outcomes (interrupted, usage error, no tests collected).
    if session.exitstatus == pytest.ExitCode.OK:
        session.exitstatus = pytest.ExitCode.TESTS_FAILED


def pytest_terminal_summary(terminalreporter):
    """Report protected-tree changes in the summary, next to the final result line."""
    changed = terminalreporter.config.stash.get(_changes_key, None)
    if not changed:
        return
    terminalreporter.write_sep(
        "=",
        "tests modified committed " + "/".join(PROTECTED_TREES) + " (use tmp_path)",
        red=True,
        bold=True,
    )
    for line in changed:
        terminalreporter.write_line(line, red=True)
