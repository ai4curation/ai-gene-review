#!/usr/bin/env python3
"""Retrospectively backfill history/ records from GitHub pull requests.

Walks the pull requests named with ``--pr`` or enumerated with ``--state``
(one of the two is required; prefer ``--state merged``) and, for each curated
target a PR touches (gene review, module, GO-CAM review, project page, schema), scaffolds
an append-only history record under ``history/`` seeded from the PR's
metadata: title, body, author, branch, changed files, and timestamps. See
``docs/history.md`` for the record format and layout rules.

Backfilled records are deliberately conservative:

- The session timestamp is the PR's ``mergedAt`` (or ``createdAt`` for
  unmerged PRs), not the time the backfill ran, so records sort into real
  chronology.
- The filename shortid is derived deterministically from the PR URL and the
  target path, so re-running the backfill never duplicates a record.
- The event type is ``CREATE`` when the PR adds the target's primary file,
  ``EDIT`` when it modifies it, and ``GENERAL`` when the target was inferred
  only from ancillary files (notes, bioinformatics folders, etc.).
- ``details`` always states that the record was backfilled from PR metadata,
  so a later reader can weigh it accordingly. Enrich by hand where the PR
  discussion holds more context.
- A target whose primary file does not exist on the checkout is skipped with
  a message rather than written. The derived path is a convention, and the
  convention breaks for GO-CAM dirs without a ``-review.yaml``, gene dirs
  touched only in ancillary files, and closed-unmerged PRs; committed records
  must point at a real file.

Requirements: this script shells out to the ``gh`` CLI and needs it installed
and authenticated (``gh auth status``). It does not fall back to anything
else; without ``gh`` it exits with an error rather than pretending to work.

Examples
--------
Dry-run over all merged PRs (prefer ``merged``: an open PR's new files are
not on the checkout, so their targets are skipped as missing)::

    uv run python scripts/backfill_history_from_prs.py --state merged --dry-run

Backfill two specific PRs::

    uv run python scripts/backfill_history_from_prs.py --pr 2613 --pr 2667

Then validate and commit::

    just validate-history-all
    git add history/
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
import subprocess
import sys
from dataclasses import dataclass, field
from datetime import UTC, datetime
from pathlib import Path

import yaml

ROOT_DIR = Path(__file__).parent.parent
REPO = "ai4curation/ai-gene-review"
REPO_URL = f"https://github.com/{REPO}"

# Branch-name prefixes that identify the agent that authored the work. The PR
# author account is often the human who launched the agent, so both are
# recorded: the agent (when inferable) first, then the account.
AGENT_BRANCH_PREFIXES = {
    "claude/": ("claude-code", "claude-code"),
    "codex/": ("codex", "codex"),
    "copilot/": ("copilot", "copilot"),
}


class _LiteralStr(str):
    """A string forced to serialize as a YAML literal block scalar (``|``)."""


def _literal_representer(dumper: yaml.Dumper, data: _LiteralStr):
    return dumper.represent_scalar("tag:yaml.org,2002:str", str(data), style="|")


yaml.add_representer(_LiteralStr, _literal_representer)


def _gh(args: list[str]) -> str:
    result = subprocess.run(
        ["gh", *args], capture_output=True, text=True, check=False
    )
    if result.returncode != 0:
        sys.exit(f"error: gh {' '.join(args[:3])}... failed:\n{result.stderr.strip()}")
    return result.stdout


@dataclass
class Target:
    kind: str
    slug: str
    path: str  # repo-relative primary file for the target
    organism: str | None = None
    # changed files in the PR that belong to this target, path -> status
    files: dict[str, str] = field(default_factory=dict)

    @property
    def history_dir(self) -> Path:
        subdir = {
            "gene": "genes",
            "module": "modules",
            "gocam": "gocams",
            "project": "projects",
            "schema": "schema",
        }[self.kind]
        out = Path("history") / subdir
        if self.kind == "gene":
            out = out / (self.organism or "")
        return out / self.slug


def classify_file(path: str) -> Target | None:
    """Map one changed file to the curated target it belongs to, if any."""
    m = re.match(r"genes/([^/]+)/([^/]+)/", path)
    if m:
        organism, gene = m.groups()
        return Target(
            kind="gene",
            slug=gene,
            organism=organism,
            path=f"genes/{organism}/{gene}/{gene}-ai-review.yaml",
        )
    # Nested module YAMLs (e.g. modules/experimental/gapmind-mining/*.yaml) are
    # real repo content; keying on the stem keeps one target per module file.
    m = re.match(r"modules/(?:.+/)?([^/]+)\.ya?ml$", path)
    if m:
        return Target(kind="module", slug=m.group(1), path=path)
    m = re.match(r"gocams/([^/]+)/", path)
    if m:
        model = m.group(1)
        return Target(
            kind="gocam", slug=model, path=f"gocams/{model}/{model}-review.yaml"
        )
    # A project is `projects/FOO.md` plus an optional `projects/FOO/` folder of
    # supporting material (the convention in CLAUDE.md). Both map to project FOO,
    # mirroring the generous gene rule above -- otherwise a PR touching only
    # sub-pages reported "no curated targets touched" and silently wrote nothing.
    m = re.match(r"projects/([^/]+)\.md$", path)
    if m:
        return Target(kind="project", slug=m.group(1), path=path)
    m = re.match(r"projects/([^/]+)/", path)
    if m:
        slug = m.group(1)
        return Target(kind="project", slug=slug, path=f"projects/{slug}.md")
    if path.startswith("src/ai_gene_review/schema/"):
        return Target(kind="schema", slug=Path(path).stem, path=path)
    return None


def collect_targets(files: list[dict]) -> list[Target]:
    targets: dict[tuple, Target] = {}
    for f in files:
        t = classify_file(f["filename"])
        if t is None:
            continue
        key = (t.kind, t.organism, t.slug)
        targets.setdefault(key, t).files[f["filename"]] = f["status"]
    return list(targets.values())


def target_path_exists(target: Target) -> bool:
    """Whether the target's primary file resolves on this checkout.

    ``classify_file`` derives the primary path by convention from the directory
    a changed file sits in, and the convention does not always hold. The common
    case is GO-CAMs: every ``gocams/<MODEL>/`` file maps to
    ``<MODEL>-review.yaml``, but the review file is optional and most models
    have only the cached ``-src.yaml``. Gene directories touched solely in
    ancillary files (notes, bioinformatics/) can likewise lack an
    ``-ai-review.yaml``, and so can closed-unmerged PRs whose files never
    landed.

    ``tests/test_history_schema.py::test_committed_history_records_follow_layout``
    requires every committed record's ``target.path`` to exist (or to carry
    ``target.superseded_by``), so writing such a record turns a backfill into a
    red ``main``. ``scripts/new_history.py`` guards the same way via
    ``target_missing_warning``.
    """
    return (ROOT_DIR / target.path).exists()


def existing_record_for(target: Target, pr_url: str) -> Path | None:
    """Find a committed history record already linking this target to this PR."""
    hist_dir = ROOT_DIR / target.history_dir
    if not hist_dir.is_dir():
        return None
    for path in sorted(hist_dir.glob("*.yaml")):
        try:
            record = yaml.safe_load(path.read_text(encoding="utf-8"))
        except yaml.YAMLError:
            continue
        prs = ((record or {}).get("links") or {}).get("prs") or []
        if pr_url in prs:
            return path
    return None


def build_record(pr: dict, target: Target) -> tuple[dict, Path]:
    pr_url = pr["url"]
    ts_raw = pr.get("mergedAt") or pr["createdAt"]
    ts = datetime.fromisoformat(ts_raw.replace("Z", "+00:00")).astimezone(UTC)
    file_ts = ts.strftime("%Y-%m-%dT%H%M%SZ")
    iso_ts = ts.strftime("%Y-%m-%dT%H:%M:%SZ")
    shortid = hashlib.sha1(f"{pr_url}|{target.path}".encode()).hexdigest()[:6]

    branch = pr.get("headRefName") or ""
    author = (pr.get("author") or {}).get("login") or "unknown"
    actors: list[dict] = []
    for prefix, (name, tool) in AGENT_BRANCH_PREFIXES.items():
        if branch.startswith(prefix):
            actors.append({"type": "ai_agent", "name": name, "agent_tool": tool})
            break
    actor_type = "automation" if author.endswith("[bot]") else "human"
    actors.append({"type": actor_type, "name": author})

    primary_status = target.files.get(target.path)
    if primary_status == "added":
        event_type = "CREATE"
    elif primary_status in {"modified", "changed", "renamed"}:
        event_type = "EDIT"
    else:
        event_type = "GENERAL"

    state_note = {
        "MERGED": "merged",
        "OPEN": "open at backfill time",
        "CLOSED": "closed without merge",
    }.get(pr.get("state", ""), pr.get("state", "unknown"))

    body = (pr.get("body") or "").strip()
    body_excerpt = body[:1500] + ("\n[...truncated]" if len(body) > 1500 else "")
    file_lines = "\n".join(
        f"  - {path} ({status})" for path, status in sorted(target.files.items())
    )
    details = (
        f"Backfilled from PR #{pr['number']} metadata ({state_note}); "
        "not a contemporaneous session record.\n\n"
        f"Files changed for this target:\n{file_lines}\n"
    )
    if body_excerpt:
        details += f"\nPR description:\n{body_excerpt}\n"

    session_id = f"{file_ts}-{_actor_token(actors[0]['name'])}-{shortid}"

    target_block: dict = {"kind": target.kind, "slug": target.slug}
    if target.organism:
        target_block["organism"] = target.organism
    target_block["path"] = target.path

    record = {
        "history_version": 1,
        "target": target_block,
        "session": {"id": session_id, "timestamp": iso_ts, "actors": actors},
        "links": {"issues": [], "prs": [pr_url], "urls": []},
        "events": [
            {
                "type": event_type,
                # In the GENERAL case the primary file was not in the PR at all
                # -- the target was inferred from ancillary files -- so we have
                # no evidence it changed. Claiming "changed" there overstates
                # what the PR metadata actually shows.
                "outcome": "changed" if event_type != "GENERAL" else "no_change",
                "summary": pr["title"].strip()[:200],
                "details": _LiteralStr(details),
            }
        ],
    }
    out_path = target.history_dir / f"{session_id}.yaml"
    return record, out_path


def _actor_token(name: str) -> str:
    token = re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")
    return token or "actor"


def pr_numbers_for_state(state: str, limit: int) -> list[int]:
    out = _gh(
        [
            "pr",
            "list",
            "--repo",
            REPO,
            "--state",
            state,
            "--limit",
            str(limit),
            "--json",
            "number",
        ]
    )
    numbers = [row["number"] for row in json.loads(out)]
    # `gh pr list` returns exactly `limit` rows both when that is all there is
    # and when it truncated, so say so rather than letting "Done: N written"
    # imply the whole state was covered.
    if len(numbers) == limit:
        print(
            f"warning: --limit {limit} reached enumerating --state {state}; "
            "there may be more PRs. Re-run with a higher --limit to cover them.",
            file=sys.stderr,
        )
    return numbers


def fetch_pr(number: int) -> dict:
    pr = json.loads(
        _gh(
            [
                "pr",
                "view",
                str(number),
                "--repo",
                REPO,
                "--json",
                "number,title,body,author,createdAt,mergedAt,state,headRefName,url",
            ]
        )
    )
    # --paginate with a per-item --jq filter emits one JSON object per line,
    # which concatenates cleanly across pages.
    files_out = _gh(
        [
            "api",
            "--paginate",
            f"repos/{REPO}/pulls/{number}/files",
            "--jq",
            ".[] | {filename, status}",
        ]
    )
    pr["files"] = [json.loads(line) for line in files_out.splitlines() if line.strip()]
    return pr


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    p.add_argument("--pr", action="append", type=int, default=[], help="PR number (repeatable).")
    p.add_argument("--state", choices=["open", "merged", "closed", "all"], help="Enumerate PRs in this state instead of naming them.")
    p.add_argument("--limit", type=int, default=200, help="Max PRs to enumerate with --state (default 200).")
    p.add_argument("--dry-run", action="store_true", help="Print planned records without writing.")
    args = p.parse_args(argv)

    if shutil.which("gh") is None:
        sys.exit(
            "error: the `gh` CLI is required (this script reads PR metadata "
            "through it). Install gh and run `gh auth login` first."
        )
    if not args.pr and not args.state:
        p.error("give --pr numbers or --state to enumerate PRs")

    numbers = list(args.pr)
    if args.state:
        numbers.extend(pr_numbers_for_state(args.state, args.limit))
    numbers = sorted(set(numbers))

    written, skipped, missing = 0, 0, 0
    for number in numbers:
        pr = fetch_pr(number)
        targets = collect_targets(pr["files"])
        if not targets:
            print(f"PR #{number}: no curated targets touched; skipping.")
            continue
        for target in targets:
            if not target_path_exists(target):
                print(
                    f"PR #{number} -> {target.path}: target file does not exist "
                    "on this checkout; skipping (a committed record must point "
                    "at a real file). Write one by hand with an explicit path "
                    "if this target is genuinely curated."
                )
                missing += 1
                continue
            existing = existing_record_for(target, pr["url"])
            if existing:
                print(f"PR #{number} -> {target.path}: record exists ({existing.relative_to(ROOT_DIR)}); skipping.")
                skipped += 1
                continue
            record, out_path = build_record(pr, target)
            if (ROOT_DIR / out_path).exists():
                print(f"PR #{number} -> {target.path}: {out_path} exists; skipping.")
                skipped += 1
                continue
            if args.dry_run:
                print(f"[dry-run] would write {out_path}")
                continue
            abs_path = ROOT_DIR / out_path
            abs_path.parent.mkdir(parents=True, exist_ok=True)
            with abs_path.open("w", encoding="utf-8") as fh:
                yaml.dump(record, fh, sort_keys=False, default_flow_style=False, allow_unicode=True)
            print(f"Wrote {out_path}")
            written += 1

    print(
        f"Done: {written} written, {skipped} skipped, "
        f"{missing} skipped for a missing target file.",
        file=sys.stderr,
    )
    if written:
        print("Next: just validate-history-all && git add history/", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
