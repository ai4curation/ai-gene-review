"""Public build/source provenance, deliberately excluding Git identities."""

from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass
from datetime import datetime, timezone
from html import escape
import json
import os
from pathlib import Path
import subprocess
from urllib.parse import quote

REPOSITORY_URL = "https://github.com/ai4curation/ai-gene-review"
SITE_BUILD_MARKER = "<!-- site-build-info -->"


def _git(directory: Path, *args: str) -> str | None:
    """Read Git metadata; standalone source exports need not have Git installed."""
    try:
        result = subprocess.run(
            ["git", "--literal-pathspecs", "-C", str(directory), *args],
            capture_output=True, text=True, check=False,
        )
    except FileNotFoundError:
        return None
    return result.stdout.rstrip("\n") if result.returncode == 0 else None


def _utc(value: datetime) -> str:
    """Serialize an aware timestamp in UTC, without implying filesystem freshness."""
    if value.tzinfo is None:
        raise ValueError("Provenance timestamps must include a timezone")
    return value.astimezone(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z")


def display_time(value: str) -> str:
    """Format a provenance timestamp for readers.

    >>> display_time('2026-10-09T08:42:00Z')
    '09 Oct 2026, 08:42 UTC'
    """
    return datetime.fromisoformat(value).astimezone(timezone.utc).strftime("%d %b %Y, %H:%M UTC")


@dataclass(frozen=True)
class SourceRevision:
    """Last commit touching one source, plus any local divergence from HEAD."""

    path: str
    commit: str | None
    committed_at: str | None
    local_changes: bool
    history_incomplete: bool = False

    @property
    def commit_url(self) -> str | None:
        """Link to the change without embedding its author or commit message."""
        return f"{REPOSITORY_URL}/commit/{self.commit}" if self.commit else None

    @property
    def source_url(self) -> str | None:
        """Pin the source link to a revision at which this path exists."""
        return f"{REPOSITORY_URL}/blob/{self.commit}/{quote(self.path, safe='/')}" if self.commit else None

    @property
    def display_date(self) -> str | None:
        """Human-readable UTC commit time."""
        return display_time(self.committed_at) if self.committed_at else None


class SourceHistory:
    """Snapshot Git state once per rendering batch, then query individual sources.

    Only hashes, committer timestamps and paths are read. An unrelated repository
    commit must not change a page's stamp. Shallow boundary commits are not
    trustworthy evidence of when a file last changed, so their dates are omitted.
    """

    def __init__(self, directory: Path) -> None:
        root = _git(directory.resolve(), "rev-parse", "--show-toplevel")
        self.root = Path(root) if root else None
        self.head: str | None = None
        self.changed: set[str] = set()
        self.shallow: set[str] = set()
        if self.root is None:
            return
        self.head = _git(self.root, "rev-parse", "--verify", "HEAD")
        # Read dirty paths once, not once per project in a full publication build.
        if self.head:
            changed = _git(self.root, "diff", "--name-only", "-z", self.head, "--")
            if changed is None:
                self.root = None
                return
            self.changed.update(changed.split("\0"))
        untracked = _git(self.root, "ls-files", "--others", "--exclude-standard", "-z")
        if untracked:
            self.changed.update(untracked.split("\0"))
        shallow_path = _git(self.root, "rev-parse", "--git-path", "shallow")
        if shallow_path:
            path = self.root / shallow_path
            if path.is_file():
                self.shallow = set(path.read_text().splitlines())

    def for_file(self, path: Path) -> SourceRevision | None:
        """Describe this Markdown source, not its renderer or generated assets."""
        path = path.resolve()
        if self.root is None or not path.is_relative_to(self.root):
            return None
        relative = path.relative_to(self.root).as_posix()
        record = _git(
            self.root, "log", "-1", "--format=%H%x00%cI", "--follow",
            self.head, "--", relative,
        ) if self.head else ""
        if record is None:
            return None
        if not record:
            return SourceRevision(relative, None, None, local_changes=True)
        commit, timestamp = record.split("\0")
        dirty = relative in self.changed
        if commit in self.shallow:
            return SourceRevision(relative, None, None, dirty, history_incomplete=True)
        return SourceRevision(relative, commit, _utc(datetime.fromisoformat(timestamp)), dirty)


def collect_build_info(
    repo_root: Path, *, built_at: datetime | None = None,
    environ: Mapping[str, str] | None = None,
) -> dict[str, str | None]:
    """Record the staged artifact's time, actual checkout and originating run.

    GITHUB_SHA can describe the workflow ref rather than the checkout. Recovery
    redeploys these bytes unchanged, retaining the original build provenance.
    """
    environ = os.environ if environ is None else environ
    commit = _git(repo_root, "rev-parse", "--verify", "HEAD")
    run_id = environ.get("GITHUB_RUN_ID", "")
    attempt = environ.get("GITHUB_RUN_ATTEMPT", "")
    run_url = None
    if environ.get("GITHUB_ACTIONS") == "true" and run_id.isdecimal():
        run_url = f"{REPOSITORY_URL}/actions/runs/{run_id}"
        if attempt.isdecimal():
            run_url += f"/attempts/{attempt}"
    return {
        "built_at": _utc(built_at or datetime.now(timezone.utc)),
        "source_commit": commit,
        "source_url": f"{REPOSITORY_URL}/commit/{commit}" if commit else None,
        "run_url": run_url,
    }


def stamp_site_build(output_dir: Path, info: Mapping[str, str | None]) -> None:
    """Stamp only the disposable site; no browser fetch or GitHub API is needed."""
    timestamp = info["built_at"]
    assert timestamp is not None
    details = info.get("run_url") or "build-info.json"
    stamp = (
        '<p class="build-info">Site built: '
        f'<time datetime="{escape(timestamp, quote=True)}">{display_time(timestamp)}</time>'
        f' · <a href="{escape(details, quote=True)}">Build details</a></p>'
    )
    homepage = output_dir / "index.html"
    original = homepage.read_text(encoding="utf-8")
    homepage.write_text(original.replace(SITE_BUILD_MARKER, stamp), encoding="utf-8")
    (output_dir / "build-info.json").write_text(
        json.dumps(dict(info), indent=2) + "\n", encoding="utf-8",
    )
