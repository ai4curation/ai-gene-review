#!/usr/bin/env python3
"""Scaffold a valid ai-gene-review history record.

History records are append-only curation/review/audit provenance files stored
outside the curated content:

    history/genes/<organism>/<GENE>/<TIMESTAMP>-<actor>-<shortid>.yaml
    history/modules/<SLUG>/<TIMESTAMP>-<actor>-<shortid>.yaml
    history/gocams/<MODEL>/<TIMESTAMP>-<actor>-<shortid>.yaml
    history/projects/<SLUG>/<TIMESTAMP>-<actor>-<shortid>.yaml
    history/schema/<SLUG>/... and history/other/<SLUG>/...

They are documented in ``docs/history.md`` and validated against
``src/ai_gene_review/schema/history.yaml``. The mechanism is ported from
dismech (https://github.com/monarch-initiative/dismech).

This helper removes the friction that keeps curation PRs from including a
record: it generates the correct path, a UTC timestamp, a collision-proof
session id, and a schema-valid skeleton, so a curator only supplies the event
content. It is the intended way to *start* a record -- edit the emitted
``details`` afterwards, then validate with ``just validate-history <path>``.

Examples
--------
Record creation of a new gene review (AI-assisted)::

    uv run python scripts/new_history.py \
        --kind gene --organism human --slug CFAP300 \
        --event CREATE --outcome changed \
        --summary "Create review: CFAP300" \
        --actor-name claude-code --actor-type ai_agent \
        --agent-tool claude-code \
        --sections existing_annotations,core_functions \
        --pr 2500 --details "De-novo review from falcon deep research."

Record a human review of a module that changed nothing::

    uv run python scripts/new_history.py \
        --kind module --slug activin_receptor_signaling \
        --event REVIEW --outcome no_change \
        --summary "Review: activin receptor signaling" \
        --actor-name cjm --actor-type human \
        --issue 1234 --details "Spot-checked members and evidence; no edits needed."

The script prints the path it created as its final stdout line, so automation
can capture it.
"""

from __future__ import annotations

import argparse
import re
import secrets
import sys
from datetime import UTC, datetime
from pathlib import Path

import yaml

REPO_URL = "https://github.com/ai4curation/ai-gene-review"

# Kinds whose target path can be derived from the slug (and organism for
# genes). ``schema``/``other`` targets require an explicit --path.
DERIVED_KINDS = ["gene", "module", "gocam", "project"]
KINDS = DERIVED_KINDS + ["schema", "other"]

# kind -> history/ subdirectory. Genes additionally nest by organism.
KIND_SUBDIRS = {
    "gene": "genes",
    "module": "modules",
    "gocam": "gocams",
    "project": "projects",
    "schema": "schema",
    "other": "other",
}

EVENTS = ["GENERAL", "CREATE", "EDIT", "REVIEW", "AUDIT"]
OUTCOMES = ["changed", "no_change", "needs_followup", "blocked"]
ACTOR_TYPES = ["human", "ai_agent", "automation", "other"]


class _LiteralStr(str):
    """A string forced to serialize as a YAML literal block scalar (``|``)."""


def _literal_representer(dumper: yaml.Dumper, data: _LiteralStr):
    return dumper.represent_scalar("tag:yaml.org,2002:str", str(data), style="|")


yaml.add_representer(_LiteralStr, _literal_representer)


def _actor_slug(name: str) -> str:
    """Filename-safe actor token: lowercase, non-alnum collapsed to '-'."""
    slug = re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")
    return slug or "actor"


def _expand_ref(value: str, kind: str) -> str:
    """Turn a bare issue/PR number into a full GitHub URL; pass URLs through."""
    value = value.strip()
    if not value:
        return value
    if value.startswith(("http://", "https://")):
        return value
    if value.isdigit():
        segment = "issues" if kind == "issue" else "pull"
        return f"{REPO_URL}/{segment}/{value}"
    return value


def _split_csv(value: str | None) -> list[str]:
    if not value:
        return []
    return [part.strip() for part in value.split(",") if part.strip()]


def derived_target_path(kind: str, slug: str, organism: str | None) -> str:
    if kind == "gene":
        return f"genes/{organism}/{slug}/{slug}-ai-review.yaml"
    if kind == "module":
        return f"modules/{slug}.yaml"
    if kind == "gocam":
        return f"gocams/{slug}/{slug}-review.yaml"
    if kind == "project":
        return f"projects/{slug}.md"
    raise ValueError(f"no derived path for kind {kind!r}")


def history_dir_for(kind: str, slug: str, organism: str | None) -> Path:
    out = Path("history") / KIND_SUBDIRS[kind]
    if kind == "gene":
        out = out / (organism or "")
    return out / slug


def build_record(args: argparse.Namespace) -> tuple[dict, Path]:
    now = datetime.now(UTC).replace(microsecond=0)
    file_ts = now.strftime("%Y-%m-%dT%H%M%SZ")
    iso_ts = now.strftime("%Y-%m-%dT%H:%M:%SZ")
    shortid = secrets.token_hex(3)

    # Resolve the target path.
    if args.kind in DERIVED_KINDS:
        if not args.slug:
            sys.exit(f"error: --slug is required for kind '{args.kind}'")
        if args.kind == "gene" and not args.organism:
            sys.exit("error: --organism is required for kind 'gene'")
        path = args.path or derived_target_path(args.kind, args.slug, args.organism)
    else:
        if not args.path:
            sys.exit(f"error: --path is required for kind '{args.kind}'")
        path = args.path

    slug = args.slug or Path(path).stem

    actor_token = _actor_slug(args.actor_name)
    session_id = f"{file_ts}-{actor_token}-{shortid}"

    actor: dict = {"type": args.actor_type, "name": args.actor_name}
    if args.model:
        actor["model"] = args.model
    if args.agent_tool:
        actor["agent_tool"] = args.agent_tool
    if args.agent_version:
        actor["agent_version"] = args.agent_version

    target: dict = {"kind": args.kind}
    if slug:
        target["slug"] = slug
    if args.kind == "gene":
        target["organism"] = args.organism
    target["path"] = path

    event: dict = {"type": args.event, "outcome": args.outcome}
    sections = _split_csv(args.sections)
    if sections:
        event["sections"] = sections
    event["summary"] = args.summary
    event["details"] = _LiteralStr(
        (args.details or "TODO: replace with curation/review notes.").rstrip() + "\n"
    )

    record = {
        "history_version": 1,
        "target": target,
        "session": {
            "id": session_id,
            "timestamp": iso_ts,
            "actors": [actor],
        },
        "links": {
            "issues": [_expand_ref(v, "issue") for v in args.issue],
            "prs": [_expand_ref(v, "pr") for v in args.pr],
            "urls": list(args.url),
        },
        "events": [event],
    }

    out_dir = history_dir_for(args.kind, slug, args.organism)
    out_path = out_dir / f"{session_id}.yaml"
    return record, out_path


def target_missing_warning(path: str) -> str | None:
    """Warn when scaffolding a record whose target does not exist on disk.

    ``tests/test_history_schema.py`` requires every committed record's target to
    resolve (or to carry ``target.superseded_by`` when the entry was later
    renamed), so catching a bad slug here saves a red ``main``.
    """
    if Path(path).exists():
        return None
    return (
        f"warning: target {path} does not exist yet.\n"
        "  If this is a typo or a stale slug, fix --slug/--organism/--path before committing:\n"
        "  committed records must point at a real file, or carry a\n"
        "  'target.superseded_by' block when the entry was renamed later.\n"
        "  If you are scaffolding ahead of creating the entry, ignore this."
    )


def parse_args(argv: list[str]) -> argparse.Namespace:
    p = argparse.ArgumentParser(
        description="Scaffold a schema-valid ai-gene-review history record.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    p.add_argument("--kind", required=True, choices=KINDS, help="Target object kind.")
    p.add_argument("--slug", help="Target slug (gene symbol, module/gocam/project file stem).")
    p.add_argument("--organism", help="Organism dir for gene targets (e.g. human, worm, SCHPO).")
    p.add_argument("--path", help="Explicit repo-relative target path (required for schema/other; overrides the derived path otherwise).")
    p.add_argument("--event", default="EDIT", choices=EVENTS, help="Event type (default: EDIT).")
    p.add_argument("--outcome", default="changed", choices=OUTCOMES, help="Event outcome (default: changed).")
    p.add_argument("--summary", required=True, help="Short one-line summary for listings.")
    p.add_argument("--details", help="Rich free-text notes (multi-line ok). Placeholder inserted if omitted.")
    p.add_argument("--sections", help="Comma-separated section names touched (e.g. existing_annotations,core_functions).")
    p.add_argument("--actor-name", default="claude-code", help="Actor name (default: claude-code).")
    p.add_argument("--actor-type", default="ai_agent", choices=ACTOR_TYPES, help="Actor category (default: ai_agent).")
    p.add_argument("--model", help="Model id for AI-assisted curation.")
    p.add_argument("--agent-tool", help="Agent tool/client (e.g. claude-code, codex).")
    p.add_argument("--agent-version", help="Agent tool/client version.")
    p.add_argument("--issue", action="append", default=[], help="Issue number or URL (repeatable).")
    p.add_argument("--pr", action="append", default=[], help="PR number or URL (repeatable).")
    p.add_argument("--url", action="append", default=[], help="Other relevant URL (repeatable).")
    p.add_argument("--force", action="store_true", help="Overwrite if the target file already exists.")
    return p.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(sys.argv[1:] if argv is None else argv)
    record, out_path = build_record(args)

    if out_path.exists() and not args.force:
        sys.exit(f"error: {out_path} already exists (use --force to overwrite)")

    warning = target_missing_warning(record["target"]["path"])
    if warning:
        print(warning, file=sys.stderr)

    out_path.parent.mkdir(parents=True, exist_ok=True)
    with out_path.open("w", encoding="utf-8") as fh:
        yaml.dump(record, fh, sort_keys=False, default_flow_style=False, allow_unicode=True)

    print(f"Wrote history record: {out_path}", file=sys.stderr)
    print(f"Next: edit the 'details', then run: just validate-history {out_path}", file=sys.stderr)
    print(out_path)  # machine-capturable final stdout line
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
