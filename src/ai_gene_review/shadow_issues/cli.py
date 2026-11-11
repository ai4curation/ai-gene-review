"""Typer sub-app for shadowing upstream issue trackers (``ai-gene-review shadow-issues``)."""

from __future__ import annotations

import sys
from collections import Counter
from pathlib import Path
from typing import Optional

import typer
import yaml
from typing_extensions import Annotated

from ai_gene_review.shadow_issues.guard import find_notification_hazards
from ai_gene_review.shadow_issues.store import (
    ISSUES_DIR,
    QUEUES,
    issue_dir,
    iter_issue_folders,
    load_issue,
    parse_time,
    queue_for,
    read_thread,
    rating_files,
    render_thread,
    report_for,
    write_yaml,
)
from ai_gene_review.shadow_issues.prior_work import (
    commits_naming_issues,
    merge_prior_work,
    names_issue_entries,
)
from ai_gene_review.shadow_issues.sync import GitHubClient, github_token, sync_tracker

shadow_issues_app = typer.Typer(
    help="Shadow upstream annotation issue trackers (issues/<tracker>/)."
)

SCHEMA = Path(__file__).parent.parent / "schema" / "shadow_issue.yaml"

TrackerArg = Annotated[
    str, typer.Argument(help="Tracker key, the folder under issues/.")
]
RootOpt = Annotated[Path, typer.Option(help="Folder holding the tracker folders.")]


@shadow_issues_app.command("sync")
def sync_cmd(
    tracker: TrackerArg = "go-annotation",
    root: RootOpt = ISSUES_DIR,
    since: Annotated[
        Optional[str], typer.Option(help="Override the cursor (ISO time).")
    ] = None,
    limit: Annotated[
        Optional[int], typer.Option(help="Stop after this many issues.")
    ] = None,
) -> None:
    """Fetch new and updated upstream issues (read-only GETs) and create stubs."""
    report = sync_tracker(
        root / tracker, GitHubClient(github_token()), since=since, limit=limit
    )
    typer.echo(
        f"{tracker}: {report.issues_seen} issues fetched, {report.stubs_created} new stubs, "
        f"{report.records_appended} thread records appended, "
        f"{report.items_skipped} incomplete timeline items skipped; cursor {report.newest_updated_at}"
    )


@shadow_issues_app.command("outstanding")
def outstanding_cmd(
    tracker: TrackerArg = "go-annotation",
    root: RootOpt = ISSUES_DIR,
    queue: Annotated[
        Optional[str], typer.Option(help=f"Only this queue: {', '.join(QUEUES)}.")
    ] = None,
    study: Annotated[
        Optional[str], typer.Option(help="Only RETROSPECTIVE or PROSPECTIVE.")
    ] = None,
    limit: Annotated[
        int, typer.Option(help="Rows to list per queue (0 = counts only).")
    ] = 20,
) -> None:
    """List issues waiting for triage, shadow work, or rating (prospective and newest first)."""
    rows: dict[str, list[tuple[dict, dict]]] = {q: [] for q in QUEUES}
    for folder in iter_issue_folders(root / tracker):
        source, issue = load_issue(folder)
        if study and issue["study"] != study:
            continue
        waiting = queue_for(folder, source, issue)
        if waiting and (queue is None or waiting == queue):
            rows[waiting].append((source, issue))
    for name, items in rows.items():
        if queue and name != queue:
            continue
        items.sort(key=lambda si: (si[1]["study"] != "PROSPECTIVE", -si[0]["number"]))
        typer.echo(f"## {name}: {len(items)}")
        for source, issue in items[:limit]:
            kind = (
                issue["triage"].get("kind")
                or issue["triage"].get("suggested_kind")
                or "-"
            )
            typer.echo(
                f"{source['number']}\t{issue['study'][:5]}\t{source['state']}\t{kind}\t{source['title'][:90]}"
            )


@shadow_issues_app.command("show")
def show_cmd(
    number: Annotated[int, typer.Argument(help="Upstream issue number.")],
    tracker: Annotated[str, typer.Option(help="Tracker key.")] = "go-annotation",
    root: RootOpt = ISSUES_DIR,
    as_of: Annotated[
        Optional[str], typer.Option(help="Hide everything after this ISO time.")
    ] = None,
    opening_only: Annotated[
        bool, typer.Option(help="Show only the opening post (BLIND).")
    ] = False,
) -> None:
    """Print a thread as markdown, optionally cut at a snapshot time for blinded work."""
    records = read_thread(issue_dir(root / tracker, number) / "thread.jsonl")
    if not records:
        raise typer.BadParameter(f"No thread for {tracker} {number}; run sync first.")
    typer.echo(
        render_thread(records, parse_time(as_of) if as_of else None, opening_only),
        nl=False,
    )


@shadow_issues_app.command("stats")
def stats_cmd(
    tracker: TrackerArg = "go-annotation", root: RootOpt = ISSUES_DIR
) -> None:
    """Counts by study, upstream state, triage kind and shadow status."""
    counts: Counter[str] = Counter()
    for folder in iter_issue_folders(root / tracker):
        source, issue = load_issue(folder)
        triage = issue["triage"]
        counts[f"study={issue['study']}"] += 1
        counts[f"state={source['state']}"] += 1
        counts[f"triage={triage['status']}"] += 1
        counts[
            f"kind={triage.get('kind') or 'suggested:' + str(triage.get('suggested_kind'))}"
        ] += 1
        counts[f"shadow={issue['shadow']['status']}"] += 1
        counts[f"rated={(folder / 'rating.yaml').exists()}"] += 1
    for key, value in sorted(counts.items()):
        typer.echo(f"{key}\t{value}")


@shadow_issues_app.command("backfill-prior-work")
def backfill_prior_work_cmd(
    tracker: TrackerArg = "go-annotation", root: RootOpt = ISSUES_DIR
) -> None:
    """Rewrite NAMES_ISSUE prior_work from git history (COVERS_SUBJECT entries are kept)."""
    found = commits_naming_issues(Path("."), tracker)
    changed = 0
    for folder in iter_issue_folders(root / tracker):
        path = folder / "issue.yaml"
        issue = yaml.safe_load(path.read_text())
        merged = merge_prior_work(
            issue.get("prior_work", []),
            names_issue_entries(found.get(int(folder.name), [])),
        )
        if merged == issue.get("prior_work", []):
            continue
        if merged:
            issue["prior_work"] = merged
        else:
            issue.pop("prior_work", None)
        write_yaml(path, issue)
        changed += 1
    typer.echo(f"{tracker}: prior_work updated on {changed} issues")


@shadow_issues_app.command("ratings")
def ratings_cmd(
    tracker: TrackerArg = "go-annotation", root: RootOpt = ISSUES_DIR
) -> None:
    """Print a markdown table of every rating (rating.yaml and rating-<label>.yaml files)."""
    dimensions = ("triage", "diagnosis", "actions", "downstream", "added_value", "harm")
    header = [
        "issue",
        "rating",
        "kind",
        "blinding",
        "outcome",
        *dimensions,
        "independence",
        "report",
    ]
    typer.echo("| " + " | ".join(header) + " |")
    typer.echo("|" + "---|" * len(header))
    for folder in iter_issue_folders(root / tracker):
        ratings = rating_files(folder)
        if not ratings:
            continue
        _, issue = load_issue(folder)
        for rating_path in ratings:
            rating = yaml.safe_load(rating_path.read_text())
            row = [
                f"{tracker} {folder.name}",
                rating_path.stem,
                issue["triage"].get("kind", "-"),
                issue["shadow"].get("blinding", "-"),
                rating["outcome"],
                *(rating.get(d, "-") for d in dimensions),
                rating["independence"],
                f"[report](../issues/{tracker}/{folder.name}/{report_for(rating_path).name})",
            ]
            typer.echo("| " + " | ".join(str(c) for c in row) + " |")


@shadow_issues_app.command("validate")
def validate_cmd(
    tracker: TrackerArg = "go-annotation", root: RootOpt = ISSUES_DIR
) -> None:
    """Validate issue.yaml (ShadowIssue), self-rating.yaml (SelfRating) and rating.yaml (ShadowRating)."""
    from linkml.validator import Validator
    from linkml.validator.plugins import JsonschemaValidationPlugin

    validator = Validator(
        str(SCHEMA), validation_plugins=[JsonschemaValidationPlugin(closed=True)]
    )
    failures = 0
    folders = iter_issue_folders(root / tracker)
    for folder in folders:
        checks = [
            (folder / "issue.yaml", "ShadowIssue"),
            (folder / "self-rating.yaml", "SelfRating"),
        ] + [(path, "ShadowRating") for path in rating_files(folder)]
        for path, target in checks:
            if not path.exists():
                continue
            data = yaml.safe_load(path.read_text())
            problems = [r.message for r in validator.validate(data, target).results]
            if data.get("number") != int(folder.name) or data.get("tracker") != tracker:
                problems.append(
                    f"tracker/number do not match folder {tracker}/{folder.name}"
                )
            if target == "ShadowRating" and not report_for(path).exists():
                problems.append(f"{path.name} has no {report_for(path).name} beside it")
            for problem in problems:
                failures += 1
                typer.echo(f"{path}: {problem}", err=True)
    typer.echo(f"Checked {len(folders)} issue folders; {failures} problems.")
    if failures:
        raise typer.Exit(1)


@shadow_issues_app.command("check-text")
def check_text_cmd(
    files: Annotated[
        Optional[list[Path]], typer.Argument(help="Files to check; stdin if none.")
    ] = None,
) -> None:
    """Fail if text would notify upstream (issue URLs, org/repo#N, @mentions other than cmungall)."""
    sources = (
        [(str(f), f.read_text()) for f in files]
        if files
        else [("<stdin>", sys.stdin.read())]
    )
    hazards = [
        (name, h) for name, text in sources for h in find_notification_hazards(text)
    ]
    for name, hazard in hazards:
        typer.echo(f"{name}: {hazard}", err=True)
    if hazards:
        raise typer.Exit(1)
