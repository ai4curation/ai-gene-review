"""Typer sub-app for shadowing upstream issue trackers (``ai-gene-review shadow-issues``)."""

from __future__ import annotations

import csv
import sys
from collections import Counter
from functools import cache
from pathlib import Path
from typing import Any, Optional

import typer
import yaml
from typing_extensions import Annotated

from ai_gene_review.shadow_issues.guard import find_notification_hazards
from ai_gene_review.shadow_issues.store import (
    ISSUES_DIR,
    QUEUES,
    effective_score,
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
    shallow_boundary,
)
from ai_gene_review.shadow_issues.sync import GitHubClient, github_token, sync_tracker

shadow_issues_app = typer.Typer(
    help="Shadow upstream annotation issue trackers (issues/<tracker>/)."
)

SCHEMA = Path(__file__).parent.parent / "schema" / "shadow_issue.yaml"

# Where the committed reports live on the web, so a ratings table links correctly
# wherever it is pasted or rendered. This repository, not an upstream tracker.
REPORT_LINK_BASE = "https://github.com/ai4curation/ai-gene-review/blob/main/issues"

# The scored dimensions of a ShadowRating, in table order.
DIMENSIONS = (
    "outcome",
    "triage",
    "diagnosis",
    "actions",
    "downstream",
    "added_value",
    "harm",
)

# Downstream evidence kinds: checks of released data, which must say when they
# were made and which release they saw.
DOWNSTREAM_EVIDENCE = ("GOA_DIFF", "MAPPING_RELEASE")

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
        counts[f"ratings={len(rating_files(folder))}"] += 1
    for key, value in sorted(counts.items()):
        typer.echo(f"{key}\t{value}")


@shadow_issues_app.command("backfill-prior-work")
def backfill_prior_work_cmd(
    tracker: TrackerArg = "go-annotation",
    root: RootOpt = ISSUES_DIR,
    allow_shallow: Annotated[
        bool,
        typer.Option(
            help="Run on a shallow clone; only after checking the hidden commits name no issue."
        ),
    ] = False,
) -> None:
    """Rewrite NAMES_ISSUE prior_work from git history (COVERS_SUBJECT entries are kept).

    The git repository searched is the one holding ``--root`` (its parent folder).
    """
    repo_root = root.resolve().parent
    boundary = shallow_boundary(repo_root)
    if boundary and allow_shallow:
        typer.echo(
            "warning: shallow clone; history behind "
            + ", ".join(c[:12] for c in boundary)
            + " is not searched",
            err=True,
        )
    found = commits_naming_issues(repo_root, tracker, allow_shallow=allow_shallow)
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
    tracker: TrackerArg = "go-annotation",
    root: RootOpt = ISSUES_DIR,
    link_base: Annotated[
        str,
        typer.Option(
            help="URL or relative path that issues/ is reached by from where the "
            "table will be read."
        ),
    ] = REPORT_LINK_BASE,
) -> None:
    """Print a markdown table of every rating (rating.yaml and rating-<label>.yaml files).

    An adjudicated dimension shows as ``score → adjudicated value*``, or as
    ``score*`` when the last ruling upheld the rater's score.
    """
    header = [
        "issue",
        "rating",
        "kind",
        "blinding",
        *DIMENSIONS,
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
            for dimension in DIMENSIONS:
                # Show the final ruling, marked, beside the score as the rater
                # wrote it; the last adjudication of a dimension is the one that counts.
                rulings = rating.get("adjudications") or []
                if not any(r.get("dimension") == dimension for r in rulings):
                    continue
                raw, final = (
                    rating.get(dimension, "-"),
                    effective_score(rating, dimension),
                )
                rating[dimension] = f"{raw}*" if final == raw else f"{raw} → {final}*"
            row = [
                f"{tracker} {folder.name}",
                rating_path.stem,
                issue["triage"].get("kind", "-"),
                issue["shadow"].get("blinding", "-"),
                *(rating.get(d, "-") for d in DIMENSIONS),
                rating["independence"],
                f"[report]({link_base}/{tracker}/{folder.name}/{report_for(rating_path).name})",
            ]
            typer.echo("| " + " | ".join(str(c) for c in row) + " |")


@shadow_issues_app.command("agreement")
def agreement_cmd(
    tracker: TrackerArg = "go-annotation", root: RootOpt = ISSUES_DIR
) -> None:
    """Raw inter-rater agreement per dimension, over issues rated more than once.

    Compares the scores as the raters wrote them, not adjudicated values: the
    question is whether independent raters agree, not whether they were right.
    An issue counts for a dimension when at least two of its ratings scored it,
    and agrees when all of those scores are equal. This is raw agreement, not
    chance-corrected: most scores are AGREE or NONE, so independent guesses
    would often agree too. Report Cohen's or Fleiss' kappa once the sample is
    large enough to estimate it.
    """
    compared: Counter[str] = Counter()
    agreed: Counter[str] = Counter()
    rated_twice = 0
    for folder in iter_issue_folders(root / tracker):
        ratings = [yaml.safe_load(p.read_text()) for p in rating_files(folder)]
        if len(ratings) < 2:
            continue
        rated_twice += 1
        for dimension in DIMENSIONS:
            scores = [r[dimension] for r in ratings if r.get(dimension)]
            if len(scores) < 2:
                continue
            compared[dimension] += 1
            agreed[dimension] += len(set(scores)) == 1
    typer.echo(f"{tracker}: issues rated twice or more: {rated_twice}")
    typer.echo("")
    typer.echo("| dimension | compared | agreed | raw agreement |")
    typer.echo("|---|---|---|---|")
    for dimension in DIMENSIONS:
        n, k = compared[dimension], agreed[dimension]
        share = f"{round(100 * k / n)}%" if n else "-"
        typer.echo(f"| {dimension} | {n} | {k} | {share} |")


PAINT_SLICE_REQUIRED = ("node", "go_id", "evidence", "negated", "date")


def read_paint_slice(
    path: Path,
) -> tuple[list[str], dict[tuple[str, str, str, str], dict[str, str]]]:
    """The columns and rows of a ``<FAMILY>-paint.tsv`` slice, rows keyed by node, term, evidence and negation.

    PAINT makes one assertion per key, so a repeated key is an error, not a row
    to drop; so is a slice without the columns paint-diff reads.
    """
    rows: dict[tuple[str, str, str, str], dict[str, str]] = {}
    with path.open(newline="") as fh:
        reader = csv.DictReader(fh, delimiter="\t")
        columns = list(reader.fieldnames or [])
        missing = [c for c in PAINT_SLICE_REQUIRED if c not in columns]
        if missing:
            raise ValueError(
                f"{path}: not a PAINT slice, no {', '.join(missing)} column"
            )
        for row in reader:
            key = (row["node"], row["go_id"], row["evidence"], row["negated"])
            if key in rows:
                raise ValueError(f"{path}: more than one row for {key}")
            rows[key] = row
    return columns, rows


@shadow_issues_app.command("paint-diff")
def paint_diff_cmd(
    old: Annotated[Path, typer.Argument(help="Earlier <FAMILY>-paint.tsv slice.")],
    new: Annotated[Path, typer.Argument(help="Later <FAMILY>-paint.tsv slice.")],
    node: Annotated[
        Optional[list[str]], typer.Option(help="Only this PTN node (repeatable).")
    ] = None,
    go: Annotated[
        Optional[list[str]], typer.Option(help="Only this GO term (repeatable).")
    ] = None,
) -> None:
    """List PAINT node annotations (IBD, IRD, IKR) added, removed or changed between two slices.

    This is how a rater sees whether a PAINT curator's change has been released:
    compare the slice from the snapshot before the fix with a later one. Get the
    earlier slice from git (``git show REV:interpro/panther/F/F-paint.tsv``) and
    the later one by re-running ``just fetch-panther-paint F`` after the pinned
    PAINT snapshot moves on. Output columns: change, node, term, evidence, NOT,
    then the date of an added or removed row, or each changed column of a
    changed row (``date old -> new``, ``seeds +added -dropped``, and so on).
    If the two slices have different columns, a first ``header`` line says so
    (``+added -dropped``) and rows are compared on the shared columns only.
    """
    old_columns, before = read_paint_slice(old)
    new_columns, after = read_paint_slice(new)
    shared = [c for c in new_columns if c in old_columns]
    if old_columns != new_columns:
        typer.echo(
            "\t".join(
                ["header"]
                + [f"+{c}" for c in new_columns if c not in old_columns]
                + [f"-{c}" for c in old_columns if c not in new_columns]
            )
        )

    def wanted(key: tuple[str, str, str, str]) -> bool:
        return (not node or key[0] in node) and (not go or key[1] in go)

    def label(key: tuple[str, str, str, str]) -> str:
        return "\t".join([key[0], key[1], key[2], "NOT" if key[3] == "true" else ""])

    for key in sorted(set(before) | set(after)):
        if not wanted(key):
            continue
        if key not in after:
            typer.echo(f"removed\t{label(key)}\t{before[key]['date']}")
        elif key not in before:
            typer.echo(f"added\t{label(key)}\t{after[key]['date']}")
        else:
            changes = []
            for column in shared:
                was, now = before[key][column], after[key][column]
                if was == now:
                    continue
                if column == "seeds":
                    old_seeds, new_seeds = set(was.split("|")), set(now.split("|"))
                    changes.append(
                        "seeds "
                        + " ".join(
                            [f"+{s}" for s in sorted(new_seeds - old_seeds)]
                            + [f"-{s}" for s in sorted(old_seeds - new_seeds)]
                        )
                    )
                else:
                    changes.append(f"{column} {was} -> {now}")
            if changes:
                typer.echo("\t".join(["changed", label(key), *changes]))


def diff_covers(path: str, diff_text: str) -> bool:
    r"""True if a unified diff has a file header for ``path``.

    Matches the ``---`` old-file or ``+++`` new-file header, so a modified,
    added (``--- /dev/null``), deleted or renamed file counts, in git,
    ``--no-prefix`` or plain ``diff -u`` form. A git change with no hunks (a
    pure rename, a mode change) has no such header, so git's own ``diff --git
    a/<old> b/<new>`` line counts too. A context line that merely quotes the
    path does not, since it starts with a space.

    >>> diff_covers("x.yaml", "diff --git a/x.yaml b/x.yaml\n--- a/x.yaml\n+++ b/x.yaml\n")
    True
    >>> diff_covers("x.yaml", "--- x.yaml\t2026-11-17\n+++ x.yaml\n")
    True
    >>> diff_covers("x.yaml", "--- /dev/null\n+++ b/x.yaml\n")
    True
    >>> diff_covers("x.yaml", "diff --git a/w.yaml b/x.yaml\nrename from w.yaml\nrename to x.yaml\n")
    True
    >>> diff_covers("x.sh", "diff --git a/x.sh b/x.sh\nold mode 100644\nnew mode 100755\n")
    True
    >>> diff_covers("x.yaml", "--- a/y.yaml\n+++ b/y.yaml\n  see a/x.yaml here\n")
    False
    """
    for line in diff_text.split("\n"):
        if line.startswith(("--- ", "+++ ")):
            if line[4:].split("\t")[0] in (path, f"a/{path}", f"b/{path}"):
                return True
        elif line.startswith("diff --git "):
            if f" a/{path} " in f"{line} " or line.endswith(f" b/{path}"):
                return True
    return False


def work_product_problems(issue: dict, repo_root: Path) -> list[str]:
    """Check work products: one that landed exists; one that did not names a preserved diff of it.

    Paths are repository-relative, so ``repo_root`` is the parent of ``--root``.

    >>> work_product_problems({"shadow": {"work_products": [
    ...     {"kind": "GENE_REVIEW", "path": "x.yaml", "landed": False}]}}, Path("."))
    ['work product x.yaml has landed: false but no preserved_diff']
    >>> work_product_problems({"shadow": {"work_products": [
    ...     {"kind": "OTHER", "path": "pyproject.toml"}]}}, Path("."))
    []
    """
    problems = []
    for product in (issue.get("shadow") or {}).get("work_products") or []:
        if not product.get("path"):
            continue  # path is required, so the schema check reports it
        diff = product.get("preserved_diff")
        if (
            product.get("landed") is not False
            and not (repo_root / product["path"]).exists()
        ):
            problems.append(f"work product {product['path']} does not exist")
        if product.get("landed") is False and not diff:
            problems.append(
                f"work product {product['path']} has landed: false but no preserved_diff"
            )
        elif diff and not (repo_root / diff).exists():
            problems.append(f"preserved_diff {diff} does not exist")
        elif diff and not diff_covers(product["path"], (repo_root / diff).read_text()):
            problems.append(f"preserved_diff {diff} has no diff of {product['path']}")
    return problems


def evidence_problems(issue: dict[str, Any]) -> list[str]:
    """Downstream evidence must say when it was checked and which release it saw.

    >>> evidence_problems({"resolution": {"evidence": [{"kind": "GOA_DIFF", "ref": "QuickGO"}]}})
    ... # doctest: +NORMALIZE_WHITESPACE
    ['GOA_DIFF evidence QuickGO needs checked_at',
     'GOA_DIFF evidence QuickGO needs source_release',
     'GOA_DIFF evidence QuickGO needs source_release_date']
    """
    problems = []
    for item in (issue.get("resolution") or {}).get("evidence") or []:
        # kind and ref are required, so the schema check reports them if absent.
        kind, ref = item.get("kind"), item.get("ref", "?")
        if kind not in DOWNSTREAM_EVIDENCE:
            continue
        for field in ("checked_at", "source_release", "source_release_date"):
            if not item.get(field):
                problems.append(f"{kind} evidence {ref} needs {field}")
    return problems


@cache
def dimension_values() -> dict[str, frozenset[str]]:
    """The permissible values of each ShadowRating dimension, from its enum in the schema.

    >>> values = dimension_values()
    >>> "PENDING_RELEASE" in values["downstream"], "PENDING_RELEASE" in values["actions"]
    (True, False)
    """
    from linkml_runtime.utils.schemaview import SchemaView

    view = SchemaView(str(SCHEMA))
    return {
        dimension: frozenset(
            view.get_enum(
                view.induced_slot(dimension, "ShadowRating").range
            ).permissible_values
        )
        for dimension in DIMENSIONS
    }


def adjudication_problems(rating: dict[str, Any]) -> list[str]:
    """An adjudication restates the score it disputes, and both values fit the dimension.

    >>> adjudication_problems({"actions": "AGREE", "adjudications": [{"dimension": "actions",
    ...     "rater_value": "PARTIAL", "adjudicated_value": "AGREE"}]})
    ['adjudication of actions has rater_value PARTIAL but the rating has AGREE']
    """
    problems = []
    for ruling in rating.get("adjudications") or []:
        dimension = ruling.get("dimension")
        if dimension not in DIMENSIONS:
            continue  # the schema's RatingDimensionEnum already reports it
        allowed = dimension_values()[dimension]
        for field in ("rater_value", "adjudicated_value"):
            if ruling.get(field) not in allowed:
                problems.append(
                    f"adjudication {field} {ruling.get(field)} is not a {dimension} value"
                )
        if ruling.get("rater_value") != rating.get(dimension):
            problems.append(
                f"adjudication of {dimension} has rater_value {ruling.get('rater_value')} "
                f"but the rating has {rating.get(dimension)}"
            )
    return problems


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
            if target == "ShadowIssue":
                problems += work_product_problems(data, root.parent)
                problems += evidence_problems(data)
            if target == "ShadowRating":
                problems += adjudication_problems(data)
                if not report_for(path).exists():
                    problems.append(
                        f"{path.name} has no {report_for(path).name} beside it"
                    )
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
