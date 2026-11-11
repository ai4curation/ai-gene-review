"""Local mirror of an upstream issue tracker, one folder per issue.

Layout (``issues/<tracker>/``)::

    tracker.yaml            # config: upstream repo, date windows, label -> kind hints
    sync-state.yaml         # cursor: newest upstream updated_at seen (machine-owned)
    <number>/
      source.yaml           # current upstream state (machine-owned, overwritten)
      thread.jsonl          # append-only issue/comment/event records (machine-owned)
      issue.yaml            # ShadowIssue: triage, shadow work, resolution (curated)
      shadow.md             # our work log (curated, optional)
      rating.yaml           # ShadowRating from an independent rater (curated, optional)

The sync writes only the machine-owned files and creates ``issue.yaml`` once, as a
stub; it never rewrites curated files.

``thread.jsonl`` records carry a ``key`` and ``updated_at``. A record is appended
when that pair is new, so an edited comment appears twice, once per version, and
:func:`latest_records` returns the newest version of each.
"""

from __future__ import annotations

import json
from dataclasses import dataclass
from datetime import date, datetime
from pathlib import Path
from typing import Any, Iterable, NamedTuple

import yaml

ISSUES_DIR = Path("issues")


@dataclass(frozen=True)
class TrackerConfig:
    """Configuration for one shadowed tracker (``issues/<key>/tracker.yaml``)."""

    key: str
    repo: str
    backfill_since: date
    prospective_since: date
    label_kinds: dict[str, str]

    @classmethod
    def load(cls, tracker_dir: Path) -> "TrackerConfig":
        """Read ``tracker.yaml`` from a tracker folder."""
        data = yaml.safe_load((tracker_dir / "tracker.yaml").read_text())
        return cls(
            key=tracker_dir.name,
            repo=data["repo"],
            backfill_since=date.fromisoformat(str(data["backfill_since"])),
            prospective_since=date.fromisoformat(str(data["prospective_since"])),
            label_kinds=data.get("label_kinds", {}),
        )

    def study_for(self, created_at: str) -> str:
        """Classify an issue by creation date.

        >>> cfg = TrackerConfig("t", "o/r", date(2024, 1, 1), date(2026, 11, 10), {})
        >>> cfg.study_for("2026-11-09T23:59:00Z"), cfg.study_for("2026-11-10T00:00:00Z")
        ('RETROSPECTIVE', 'PROSPECTIVE')
        """
        return (
            "PROSPECTIVE"
            if parse_time(created_at).date() >= self.prospective_since
            else "RETROSPECTIVE"
        )

    def suggest_kind(self, labels: Iterable[str]) -> str | None:
        """First label (in ``label_kinds`` order) that maps to a kind.

        >>> cfg = TrackerConfig("t", "o/r", date(2024, 1, 1), date(2026, 1, 1),
        ...                     {"PAINT annotation": "PAINT_IBA", "ARBA": "MAPPING_RULE"})
        >>> cfg.suggest_kind(["ARBA", "PAINT annotation"])
        'PAINT_IBA'
        >>> cfg.suggest_kind(["FlyBase"]) is None
        True
        """
        present = set(labels)
        return next(
            (kind for label, kind in self.label_kinds.items() if label in present), None
        )


def parse_time(value: str) -> datetime:
    """Parse a GitHub ISO timestamp.

    >>> parse_time("2026-07-17T10:00:00Z").isoformat()
    '2026-07-17T10:00:00+00:00'
    """
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


def issue_dir(tracker_dir: Path, number: int) -> Path:
    return tracker_dir / str(number)


def _login(user: dict[str, Any] | None) -> str | None:
    return user["login"] if user else None


def issue_record(issue: dict[str, Any]) -> dict[str, Any]:
    """The opening post, as a thread record."""
    return {
        "type": "issue",
        "key": "issue",
        "created_at": issue["created_at"],
        "updated_at": issue["updated_at"],
        "author": _login(issue["user"]),
        "title": issue["title"],
        "state": issue["state"],
        "state_reason": issue.get("state_reason"),
        "labels": sorted(label["name"] for label in issue["labels"]),
        "body": issue["body"] or "",
    }


def _dig(item: dict[str, Any], *keys: str) -> Any:
    """Follow nested keys, returning None as soon as one is missing.

    GitHub timeline items are not always complete (a cross-reference from a repo
    that was since deleted or made private has no ``repository``), and one odd
    item must not stop the mirror.

    >>> _dig({"a": {"b": 1}}, "a", "b"), _dig({"a": None}, "a", "b"), _dig({}, "a")
    (1, None, None)
    """
    value: Any = item
    for key in keys:
        if not isinstance(value, dict):
            return None
        value = value.get(key)
    return value


#: Timeline events stored in thread.jsonl; others (subscribed, mentioned, ...) are dropped.
KEPT_EVENTS = frozenset(
    {
        "commented",
        "labeled",
        "unlabeled",
        "closed",
        "reopened",
        "renamed",
        "assigned",
        "unassigned",
        "referenced",
        "cross-referenced",
    }
)


def timeline_record(item: dict[str, Any]) -> dict[str, Any] | None:
    """Compact a timeline item into a thread record.

    Comments keep their body. Other events keep what is needed to reconstruct the
    resolution: labels, closing, and cross-references to issues or commits elsewhere.
    Returns None for events not in :data:`KEPT_EVENTS`, and for kept events that
    lack the fields their record needs; :func:`store_issue` counts the latter as
    skipped rather than failing.

    >>> timeline_record({"event": "labeled", "id": 7, "created_at": "2026-01-01T00:00:00Z",
    ...                  "actor": {"login": "a"}, "label": {"name": "ARBA"}})["label"]
    'ARBA'
    >>> timeline_record({"event": "subscribed", "id": 8, "created_at": "2026-01-01T00:00:00Z"}) is None
    True
    >>> timeline_record({"event": "cross-referenced", "created_at": "2026-01-01T00:00:00Z",
    ...                  "source": {"issue": {"number": 3, "title": "gone"}}}) is None
    True
    """
    event = item.get("event")
    created = item.get("created_at")
    if event not in KEPT_EVENTS or created is None:
        return None
    if event == "commented":
        if item.get("id") is None:
            return None
        return {
            "type": "comment",
            "key": f"comment:{item['id']}",
            "created_at": created,
            "updated_at": item.get("updated_at") or created,
            "author": _dig(item, "user", "login"),
            "body": item.get("body") or "",
        }
    base = {
        "type": "event",
        "event": event,
        "created_at": created,
        "updated_at": created,
        "author": _dig(item, "actor", "login"),
    }
    if event == "cross-referenced":
        repo = _dig(item, "source", "issue", "repository", "full_name")
        number = _dig(item, "source", "issue", "number")
        if repo is None or number is None:
            return None
        return {
            **base,
            "key": f"xref:{repo}#{number}",
            "source_repo": repo,
            "source_number": number,
            "source_title": _dig(item, "source", "issue", "title"),
            "source_is_pr": "pull_request" in (_dig(item, "source", "issue") or {}),
        }
    if item.get("id") is None:
        return None
    record = {**base, "key": f"event:{item['id']}"}
    if event in ("labeled", "unlabeled"):
        label = _dig(item, "label", "name")
        if label is None:
            return None
        return {**record, "label": label}
    if event == "closed":
        return {**record, "state_reason": item.get("state_reason")}
    if event == "renamed":
        return {**record, "rename": item.get("rename")}
    if event in ("assigned", "unassigned"):
        return {**record, "assignee": _dig(item, "assignee", "login")}
    if event == "referenced":
        if item.get("commit_id") is None:
            return None
        return {**record, "commit_id": item["commit_id"]}
    return record


def read_thread(path: Path) -> list[dict[str, Any]]:
    """All records in a ``thread.jsonl`` file, in file order."""
    if not path.exists():
        return []
    # Split on "\n" only: str.splitlines() also splits on U+2028 and friends, which
    # json.dumps(ensure_ascii=False) leaves unescaped inside comment bodies.
    return [json.loads(line) for line in path.read_text().split("\n") if line.strip()]


_ISSUE_CONTENT = ("title", "state", "state_reason", "labels", "body")


def _changed(opening: dict[str, Any], existing: list[dict[str, Any]]) -> bool:
    """Whether the opening post differs from the last version stored.

    The issue's ``updated_at`` moves with every comment or label, so the opening
    post is versioned by content instead of by timestamp.

    >>> rec = {"type": "issue", "title": "T", "state": "open", "state_reason": None,
    ...        "labels": [], "body": "B", "updated_at": "1"}
    >>> _changed(rec, []), _changed(rec, [{**rec, "updated_at": "0"}]), _changed(rec, [{**rec, "state": "closed"}])
    (True, False, True)
    """
    previous = [r for r in existing if r["type"] == "issue"]
    if not previous:
        return True
    last = previous[-1]
    return any(last.get(field) != opening.get(field) for field in _ISSUE_CONTENT)


def append_new_records(path: Path, records: Iterable[dict[str, Any]]) -> int:
    """Append records whose (key, updated_at) is not already in the file.

    Returns the number appended. Existing lines are never rewritten.
    """
    seen = {(r["key"], r["updated_at"]) for r in read_thread(path)}
    new = [r for r in records if (r["key"], r["updated_at"]) not in seen]
    if new:
        with path.open("a") as handle:
            for record in new:
                handle.write(
                    json.dumps(record, ensure_ascii=False, sort_keys=True) + "\n"
                )
    return len(new)


def latest_records(records: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Newest version of each record key, ordered by creation time.

    >>> recs = [{"key": "c1", "created_at": "1", "updated_at": "1", "body": "old"},
    ...         {"key": "c2", "created_at": "2", "updated_at": "2", "body": "x"},
    ...         {"key": "c1", "created_at": "1", "updated_at": "3", "body": "new"}]
    >>> [r["body"] for r in latest_records(recs)]
    ['new', 'x']
    """
    newest: dict[str, dict[str, Any]] = {}
    for record in records:
        current = newest.get(record["key"])
        if current is None or record["updated_at"] >= current["updated_at"]:
            newest[record["key"]] = record
    return sorted(newest.values(), key=lambda r: r["created_at"])


def source_snapshot(
    issue: dict[str, Any], records: list[dict[str, Any]]
) -> dict[str, Any]:
    """Current upstream state of an issue, for ``source.yaml``.

    ``comment_count`` counts comments ever mirrored. thread.jsonl is append-only
    and the timeline does not report deletions, so after an upstream comment is
    deleted this count stays above upstream's.
    """
    latest = latest_records(records)
    return {
        "number": issue["number"],
        "url": issue["html_url"],
        "title": issue["title"],
        "state": issue["state"],
        "state_reason": issue.get("state_reason"),
        "labels": sorted(label["name"] for label in issue["labels"]),
        "author": _login(issue["user"]),
        "created_at": issue["created_at"],
        "updated_at": issue["updated_at"],
        "closed_at": issue.get("closed_at"),
        "comment_count": sum(1 for r in latest if r["type"] == "comment"),
        "linked_repos": sorted(
            {r["source_repo"] for r in latest if r.get("source_repo")}
        ),
    }


def stub_issue(config: TrackerConfig, issue: dict[str, Any]) -> dict[str, Any]:
    """Initial curated ``issue.yaml`` for a newly seen issue.

    ``suggested_kind`` comes from the labels the issue has when first synced. For
    a PROSPECTIVE issue that is close to its labels at creation. For a
    RETROSPECTIVE (backfilled) issue it is the post-resolution label set, which
    can encode the curators' disposition (``ARBA - checked``, ``no clear
    request``), so no suggestion is made and triage is not handed the answer.
    """
    study = config.study_for(issue["created_at"])
    triage: dict[str, Any] = {"status": "UNTRIAGED"}
    if study == "PROSPECTIVE":
        kind = config.suggest_kind(label["name"] for label in issue["labels"])
        if kind:
            triage["suggested_kind"] = kind
    return {
        "tracker": config.key,
        "number": issue["number"],
        "study": study,
        "triage": triage,
        "shadow": {"status": "NOT_STARTED"},
    }


def write_yaml(path: Path, data: dict[str, Any]) -> None:
    path.write_text(
        yaml.safe_dump(data, sort_keys=False, allow_unicode=True, width=100)
    )


class StoreResult(NamedTuple):
    """Outcome of storing one issue."""

    appended: int
    """Thread records appended."""
    created: bool
    """Whether issue.yaml was created."""
    skipped: int
    """Kept-kind timeline items dropped because they lacked required fields."""


def store_issue(
    config: TrackerConfig,
    tracker_dir: Path,
    issue: dict[str, Any],
    timeline: list[dict[str, Any]],
) -> "StoreResult":
    """Write one fetched issue into its folder."""
    folder = issue_dir(tracker_dir, issue["number"])
    folder.mkdir(parents=True, exist_ok=True)
    thread = folder / "thread.jsonl"
    opening = issue_record(issue)
    converted = [(item, timeline_record(item)) for item in timeline]
    records = [r for _, r in converted if r is not None]
    skipped = sum(
        1 for item, r in converted if r is None and item.get("event") in KEPT_EVENTS
    )
    if _changed(opening, read_thread(thread)):
        records.insert(0, opening)
    appended = append_new_records(thread, records)
    write_yaml(folder / "source.yaml", source_snapshot(issue, read_thread(thread)))
    curated = folder / "issue.yaml"
    created = not curated.exists()
    if created:
        write_yaml(curated, stub_issue(config, issue))
    return StoreResult(appended, created, skipped)


def load_issue(folder: Path) -> tuple[dict[str, Any], dict[str, Any]]:
    """(source.yaml, issue.yaml) for one issue folder."""
    return (
        yaml.safe_load((folder / "source.yaml").read_text()),
        yaml.safe_load((folder / "issue.yaml").read_text()),
    )


def iter_issue_folders(tracker_dir: Path) -> list[Path]:
    """Issue folders, numerically ordered."""
    return sorted(
        (p for p in tracker_dir.iterdir() if p.is_dir() and p.name.isdigit()),
        key=lambda p: int(p.name),
    )


def report_for(rating_path: Path) -> Path:
    """The report that must accompany a rating file.

    >>> report_for(Path("6596/rating.yaml")).name, report_for(Path("6596/rating-same-model.yaml")).name
    ('report.md', 'report-same-model.md')
    """
    return rating_path.with_name(
        rating_path.name.replace("rating", "report", 1).replace(".yaml", ".md")
    )


def rating_files(folder: Path) -> list[Path]:
    """An issue's ratings: the primary ``rating.yaml`` first, then ``rating-<label>.yaml``.

    An issue can be rated more than once, for example by raters of different
    independence. ``rating.yaml`` is the primary rating (the most independent);
    the others are kept so that raters can be compared.
    """
    primary = folder / "rating.yaml"
    others = sorted(folder.glob("rating-*.yaml"))
    return ([primary] if primary.exists() else []) + others


QUEUES = ("untriaged", "in_progress", "needs_shadow", "needs_rating")


def queue_for(
    folder: Path, source: dict[str, Any], issue: dict[str, Any]
) -> str | None:
    """Which work queue an issue is waiting in, if any.

    - ``untriaged``: nobody has decided whether it is in scope.
    - ``in_progress``: shadow work started but not finished; resume it.
    - ``needs_shadow``: in scope, and our work has not started.
    - ``needs_rating``: our work is done, upstream has closed the issue, and no
      rating exists yet.
    """
    triage, shadow = issue["triage"], issue["shadow"]
    if triage["status"] == "UNTRIAGED":
        return "untriaged"
    if shadow["status"] == "IN_PROGRESS":
        return "in_progress"
    if triage.get("in_scope") and shadow["status"] == "NOT_STARTED":
        return "needs_shadow"
    if (
        shadow["status"] == "DONE"
        and source["state"] == "closed"
        and not (folder / "rating.yaml").exists()
    ):
        return "needs_rating"
    return None


def render_thread(
    records: list[dict[str, Any]],
    as_of: datetime | None = None,
    opening_only: bool = False,
) -> str:
    """Markdown view of a thread, as a worker or rater should see it.

    ``as_of`` hides every record (and every edit) made after that time, which is
    how a worker is held to a thread snapshot. ``opening_only`` shows just the
    opening post's title, author, date and text (the BLIND protocol), without
    labels or state: for a backfilled issue those are post-resolution and can
    encode the curators' disposition. Records keep their keys so a resolution can
    cite them.

    >>> recs = [{"type": "issue", "key": "issue", "created_at": "2026-01-01T00:00:00Z",
    ...          "updated_at": "2026-01-01T00:00:00Z", "author": "a", "title": "T",
    ...          "state": "open", "labels": [], "body": "B"},
    ...         {"type": "comment", "key": "comment:1", "created_at": "2026-01-02T00:00:00Z",
    ...          "updated_at": "2026-01-02T00:00:00Z", "author": "b", "body": "fixed"}]
    >>> "fixed" in render_thread(recs), "fixed" in render_thread(recs, as_of=parse_time("2026-01-01T12:00:00Z"))
    (True, False)
    >>> "labels" in render_thread(recs, opening_only=True)
    False
    """
    visible = [
        r for r in records if as_of is None or parse_time(r["updated_at"]) <= as_of
    ]
    latest = latest_records(visible)
    openings = [r for r in latest if r["type"] == "issue"]
    # The first stored version of the opening post can postdate as_of (it is
    # stamped with the issue's updated_at when first synced). Show its text, which
    # is the best available, but not its labels or state, which would leak.
    opening = (
        openings[0] if openings else next(r for r in records if r["type"] == "issue")
    )
    labels = (
        ", ".join(opening["labels"])
        if openings
        else "(withheld: recorded after the snapshot)"
    )
    byline = f"Opened by {opening['author']} at {opening['created_at']}"
    if opening_only:
        return (
            "\n".join([f"# {opening['title']}", "", byline, "", opening["body"]]) + "\n"
        )
    lines = [
        f"# {opening['title']}",
        "",
        f"{byline}; labels: {labels or 'none'}",
        "",
        opening["body"],
    ]
    for record in latest:
        if record["type"] == "comment":
            lines += [
                "",
                f"## [{record['key']}] {record['author']} at {record['created_at']}",
                "",
                record["body"],
            ]
        elif record["type"] == "event":
            detail = (
                record.get("label")
                or record.get("source_repo")
                or record.get("state_reason")
                or ""
            )
            lines += [
                "",
                f"- [{record['key']}] {record['event']} {detail} by {record['author']} at {record['created_at']}",
            ]
    return "\n".join(lines) + "\n"
