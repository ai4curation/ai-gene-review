"""Resolve the repository root a validation hook should run against.

Hooks are invoked as ``$CLAUDE_PROJECT_DIR/.claude/hooks/<hook>.py``, and
``$CLAUDE_PROJECT_DIR`` stays pinned to the session's project directory. When a subagent
works in a git worktree, the hook therefore ran against the **main checkout** rather than
the tree holding the file being edited, and validated content that did not exist there:

- a ``file:`` reference to a ``GENE-bioinformatics/RESULTS.md`` the agent had just written
  was reported missing, and
- a ``supporting_text`` quoting a publication the agent had just fetched into its own
  ``publications/`` was reported unverifiable,

because ``validation/supporting_text.py`` anchors its publications cache on the root it is
given. Both failures look like genuine validation errors, so the rational response is to
delete the reference — which is what happened, more than once, to valid content.

Deriving the root from the **edited file** instead makes the hook validate the tree the
author is actually working in. This is the same walk-up idiom the repository's own
bioinformatics scripts already use.
"""

from pathlib import Path

# A repo root is identified by these entries existing together. ``genes`` alone is too
# weak (an agent scratch directory can contain one); pairing it with ``src`` pins it to a
# checkout of this project.
ROOT_MARKERS = ("genes", "src")


def is_repo_root(candidate: Path) -> bool:
    """True when *candidate* looks like a checkout of this repository.

    >>> is_repo_root(Path("/definitely/not/a/repo"))
    False
    """
    return all((candidate / marker).is_dir() for marker in ROOT_MARKERS)


def find_repo_root(target: Path, fallback: Path) -> Path:
    """Return the repo root containing *target*, else *fallback*.

    The search walks upward from *target* so that a file inside a git worktree resolves to
    that worktree rather than to whichever checkout the hook script happens to live in.

    A path that is not inside any checkout falls back, so a hook can never end up with no
    root at all::

        >>> fallback = Path("/fallback/root")
        >>> find_repo_root(Path("/nowhere/at/all/GENE-ai-review.yaml"), fallback)
        PosixPath('/fallback/root')

    The fallback is returned as given, without being probed -- callers pass the historical
    ``__file__``-derived root, which is correct whenever the hook and the file share a
    checkout.
    """
    target = target.resolve() if target.is_absolute() else (Path.cwd() / target).resolve()
    for candidate in (target, *target.parents):
        if candidate.is_dir() and is_repo_root(candidate):
            return candidate
    return fallback


def hook_script_root(hook_file: str) -> Path:
    """The historical root: two levels up from ``.claude/hooks/<hook>.py``."""
    return Path(hook_file).resolve().parent.parent.parent
