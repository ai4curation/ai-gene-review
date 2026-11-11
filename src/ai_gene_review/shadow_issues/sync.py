"""Fetch issues from an upstream GitHub tracker into ``issues/<tracker>/``.

Read-only: this only issues GET requests, so it never notifies anyone upstream.
"""

from __future__ import annotations

import os
import shutil
import subprocess
from dataclasses import dataclass, field
from datetime import datetime, time, timedelta, timezone
from pathlib import Path
from typing import Any, Iterator

import requests
import yaml

from ai_gene_review.shadow_issues.store import (
    TrackerConfig,
    parse_time,
    store_issue,
    write_yaml,
)

API = "https://api.github.com"

#: How far before the cursor each incremental sync starts (see :func:`sync_tracker`).
CURSOR_OVERLAP = timedelta(hours=1)


def github_token() -> str | None:
    """A token from ``GITHUB_TOKEN``/``GH_TOKEN`` or the gh CLI, if any.

    Unauthenticated requests work for public repositories but are limited to 60 an hour.
    """
    for var in ("GITHUB_TOKEN", "GH_TOKEN"):
        if os.environ.get(var):
            return os.environ[var]
    if shutil.which("gh"):
        result = subprocess.run(
            ["gh", "auth", "token"], capture_output=True, text=True, check=False
        )
        if result.returncode == 0 and result.stdout.strip():
            return result.stdout.strip()
    return None


@dataclass
class GitHubClient:
    """Minimal paginating GET client for the GitHub REST API."""

    token: str | None = None
    session: requests.Session = field(default_factory=requests.Session)

    def __post_init__(self) -> None:
        self.session.headers["Accept"] = "application/vnd.github+json"
        self.session.headers["X-GitHub-Api-Version"] = "2022-11-28"
        if self.token:
            self.session.headers["Authorization"] = f"Bearer {self.token}"

    def paginate(
        self, path: str, params: dict[str, Any] | None = None
    ) -> Iterator[dict[str, Any]]:
        """Yield every item from a paginated list endpoint."""
        url: str | None = f"{API}{path}"
        query = {"per_page": 100, **(params or {})}
        while url:
            response = self.session.get(url, params=query, timeout=60)
            response.raise_for_status()
            yield from response.json()
            url = response.links.get("next", {}).get("url")
            query = {}


@dataclass
class SyncReport:
    issues_seen: int = 0
    stubs_created: int = 0
    records_appended: int = 0
    items_skipped: int = 0
    newest_updated_at: str | None = None


def read_cursor(tracker_dir: Path) -> str | None:
    state = tracker_dir / "sync-state.yaml"
    if not state.exists():
        return None
    return yaml.safe_load(state.read_text())["last_updated_at"]


def sync_tracker(
    tracker_dir: Path,
    client: GitHubClient,
    since: str | None = None,
    limit: int | None = None,
) -> SyncReport:
    """Fetch every issue updated since the cursor (or ``since``) and store it.

    Only issues created on or after the tracker's ``backfill_since`` are kept.
    Pull requests are skipped. The cursor advances to the newest ``updated_at``
    stored, so an interrupted run resumes where it stopped.

    The query starts :data:`CURSOR_OVERLAP` before the cursor. Results are sorted
    by ``updated_at``, so an issue updated while a run is paging can move to a
    page already read and be missed; the next run's overlap picks it up again.
    Re-reading is free, since thread appends are deduplicated.
    """
    config = TrackerConfig.load(tracker_dir)
    cursor = read_cursor(tracker_dir)
    if since:
        start = since
    elif cursor:
        start = (parse_time(cursor) - CURSOR_OVERLAP).isoformat()
    else:
        start = datetime.combine(
            config.backfill_since, time(), timezone.utc
        ).isoformat()
    floor = datetime.combine(config.backfill_since, time(), timezone.utc)
    report = SyncReport()
    params = {"state": "all", "since": start, "sort": "updated", "direction": "asc"}
    for issue in client.paginate(f"/repos/{config.repo}/issues", params):
        if "pull_request" in issue or parse_time(issue["created_at"]) < floor:
            continue
        timeline = list(
            client.paginate(f"/repos/{config.repo}/issues/{issue['number']}/timeline")
        )
        result = store_issue(config, tracker_dir, issue, timeline)
        report.issues_seen += 1
        report.records_appended += result.appended
        report.stubs_created += int(result.created)
        report.items_skipped += result.skipped
        report.newest_updated_at = issue["updated_at"]
        write_yaml(
            tracker_dir / "sync-state.yaml", {"last_updated_at": issue["updated_at"]}
        )
        if limit is not None and report.issues_seen >= limit:
            break
    return report
