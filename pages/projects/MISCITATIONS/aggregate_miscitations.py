#!/usr/bin/env python3
"""Aggregate every curated ``reference_review`` into a miscitation register.

The schema lets a reviewer record a manual judgment on each cited reference
(``references[].reference_review``) with a ``correctness`` drawn from
``ReferenceCorrectnessEnum`` (VERIFIED / UNVERIFIED / WRONG_IDENTIFIER /
MISCITED / DISPUTED / LOW_QUALITY) and a free-text ``review_notes``.

Nothing previously aggregated that flag, so a miscitation found while reviewing
one gene stayed buried in that gene's YAML. This walks every
``genes/*/*/*-ai-review.yaml``, pulls out each ``reference_review``, and writes:

- ``reports/miscitations.tsv`` -- one row per adjudicated reference, for querying.
- ``projects/MISCITATIONS/miscitation-register.md`` -- the rendered register
  (counts by correctness, counts by organism, and a table of every non-VERIFIED
  reference) that the MISCITATIONS project page links to.

Usage::

    uv run python projects/MISCITATIONS/aggregate_miscitations.py
"""

from __future__ import annotations

import argparse
import csv
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable

import yaml

REPO_ROOT = Path(__file__).resolve().parents[2]
GENES_DIR = REPO_ROOT / "genes"
TSV_OUT = REPO_ROOT / "reports" / "miscitations.tsv"
MD_OUT = REPO_ROOT / "projects" / "MISCITATIONS" / "miscitation-register.md"

REGEN_CMD = "uv run python projects/MISCITATIONS/aggregate_miscitations.py"

# ReferenceCorrectnessEnum, in the order we want to report them.
CORRECTNESS_ORDER = [
    "WRONG_IDENTIFIER",
    "MISCITED",
    "DISPUTED",
    "LOW_QUALITY",
    "UNVERIFIED",
    "VERIFIED",
]
# Everything except VERIFIED is "adjudicated but not clean". UNVERIFIED means
# "not yet checked", so it is reported separately from the genuine problems.
PROBLEM_VALUES = ["WRONG_IDENTIFIER", "MISCITED", "DISPUTED", "LOW_QUALITY"]

RELEVANCE_ORDER = ["HIGH", "MEDIUM", "LOW", "NONE"]

MAX_NOTE_CHARS = 400


@dataclass
class RefRow:
    """One adjudicated reference, flattened for tabular output."""

    source_file: str
    organism: str
    gene_symbol: str
    gene_id: str
    reference_id: str
    title: str
    relevance: str
    correctness: str
    review_notes: str
    is_invalid: str


def _clean(value: Any) -> str:
    """Collapse a YAML scalar to a single-line string."""
    if value is None:
        return ""
    return " ".join(str(value).split())


def _iter_review_files(genes_dir: Path) -> Iterable[Path]:
    return sorted(genes_dir.glob("*/*/*-ai-review.yaml"))


def collect_rows(genes_dir: Path) -> tuple[list[RefRow], int, int]:
    """Return (rows, n_files_scanned, n_files_with_reference_review)."""
    rows: list[RefRow] = []
    n_files = 0
    n_with = 0

    for path in _iter_review_files(genes_dir):
        n_files += 1
        try:
            doc = yaml.safe_load(path.read_text())
        except yaml.YAMLError:
            continue
        if not isinstance(doc, dict):
            continue

        organism = path.parent.parent.name
        gene_symbol = _clean(doc.get("gene_symbol")) or path.parent.name
        gene_id = _clean(doc.get("id"))

        refs = doc.get("references")
        if not isinstance(refs, list):
            continue

        file_had_review = False
        for ref in refs:
            if not isinstance(ref, dict):
                continue
            review = ref.get("reference_review")
            if not isinstance(review, dict):
                continue
            file_had_review = True
            rows.append(
                RefRow(
                    source_file=str(path.relative_to(REPO_ROOT)),
                    organism=organism,
                    gene_symbol=gene_symbol,
                    gene_id=gene_id,
                    reference_id=_clean(ref.get("id")),
                    title=_clean(ref.get("title")),
                    relevance=_clean(review.get("relevance")).upper(),
                    correctness=_clean(review.get("correctness")).upper(),
                    review_notes=_clean(review.get("review_notes")),
                    is_invalid="true" if ref.get("is_invalid") else "",
                )
            )
        if file_had_review:
            n_with += 1

    return rows, n_files, n_with


def _counts(values: Iterable[str]) -> dict[str, int]:
    out: dict[str, int] = {}
    for v in values:
        out[v] = out.get(v, 0) + 1
    return out


def _ordered_counts(counts: dict[str, int], order: list[str]) -> list[tuple[str, int]]:
    """Counts in the canonical order first, then any unexpected values."""
    seen = set(order)
    ordered = [(k, counts[k]) for k in order if k in counts]
    extra = sorted(
        ((k, v) for k, v in counts.items() if k not in seen),
        key=lambda kv: (-kv[1], kv[0]),
    )
    return ordered + extra


def _md_escape(text: str) -> str:
    """Escape the characters that would break a Markdown table cell."""
    return text.replace("|", "\\|")


def _truncate(text: str, limit: int = MAX_NOTE_CHARS) -> str:
    if len(text) <= limit:
        return text
    return text[: limit - 1].rstrip() + "…"


def write_tsv(rows: list[RefRow], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="") as handle:
        writer = csv.writer(handle, delimiter="\t", lineterminator="\n")
        writer.writerow(
            [
                "organism",
                "gene_symbol",
                "gene_id",
                "reference_id",
                "title",
                "relevance",
                "correctness",
                "is_invalid",
                "review_notes",
                "source_file",
            ]
        )
        for row in sorted(
            rows, key=lambda r: (r.organism, r.gene_symbol, r.reference_id)
        ):
            writer.writerow(
                [
                    row.organism,
                    row.gene_symbol,
                    row.gene_id,
                    row.reference_id,
                    row.title,
                    row.relevance,
                    row.correctness,
                    row.is_invalid,
                    row.review_notes,
                    row.source_file,
                ]
            )


def render_markdown(rows: list[RefRow], n_files: int, n_with: int) -> str:
    total = len(rows)
    correctness_counts = _counts(r.correctness for r in rows if r.correctness)
    n_problem = sum(correctness_counts.get(v, 0) for v in PROBLEM_VALUES)
    n_unverified = correctness_counts.get("UNVERIFIED", 0)
    pct = (100.0 * n_problem / total) if total else 0.0

    lines: list[str] = []
    lines.append("---")
    lines.append('title: "Miscitation Register"')
    # This is a machine-generated multi-organism table, not prose: bare symbols in
    # it are data, and autolinking them produces only ambiguity warnings.
    lines.append("autolink_gene_symbols: false")
    lines.append("---")
    lines.append("")
    lines.append("# Miscitation Register")
    lines.append("")
    lines.append(
        f"<!-- GENERATED FILE. Do not edit by hand. Regenerate with `{REGEN_CMD}`. -->"
    )
    lines.append("")
    lines.append(
        "This register is rendered directly from the `references[].reference_review` "
        "blocks curated in the gene-review YAML (see the "
        "[Reference schema class](../../src/ai_gene_review/schema/gene_review.yaml)). "
        "It is the structured, queryable counterpart to the worked cases on the "
        "[parent project page](../MISCITATIONS.md)."
    )
    lines.append("")
    lines.append(
        f"**{total} adjudicated reference(s)** across **{n_with}** of **{n_files}** "
        f"reviewed gene files."
    )
    lines.append("")
    lines.append(
        f"- **Flagged as a citation problem** (WRONG_IDENTIFIER / MISCITED / DISPUTED / "
        f"LOW_QUALITY): **{n_problem} ({pct:.1f}%)**"
    )
    lines.append(f"- **Not yet checked** (UNVERIFIED): {n_unverified}")
    lines.append("")

    # --- counts by correctness -------------------------------------------------
    lines.append("## By correctness")
    lines.append("")
    lines.append("| Correctness | Count | Share |")
    lines.append("|---|---:|---:|")
    for value, count in _ordered_counts(correctness_counts, CORRECTNESS_ORDER):
        share = (100.0 * count / total) if total else 0.0
        lines.append(f"| {value} | {count} | {share:.1f}% |")
    lines.append("")

    # --- counts by relevance ---------------------------------------------------
    relevance_counts = _counts(r.relevance for r in rows if r.relevance)
    if relevance_counts:
        lines.append("## By relevance")
        lines.append("")
        lines.append("| Relevance | Count |")
        lines.append("|---|---:|")
        for value, count in _ordered_counts(relevance_counts, RELEVANCE_ORDER):
            lines.append(f"| {value} | {count} |")
        lines.append("")

    # --- counts by organism ----------------------------------------------------
    lines.append("## By organism")
    lines.append("")
    lines.append(
        "Organisms with at least one adjudicated reference, ranked by the number "
        "of flagged citation problems."
    )
    lines.append("")
    lines.append(
        "| Organism | Adjudicated | Flagged | WRONG_IDENTIFIER | MISCITED | "
        "DISPUTED | LOW_QUALITY | UNVERIFIED |"
    )
    lines.append("|---|---:|---:|---:|---:|---:|---:|---:|")
    organisms = sorted({r.organism for r in rows})
    org_stats = []
    for org in organisms:
        org_rows = [r for r in rows if r.organism == org]
        counts = _counts(r.correctness for r in org_rows if r.correctness)
        flagged = sum(counts.get(v, 0) for v in PROBLEM_VALUES)
        org_stats.append((org, len(org_rows), flagged, counts))
    for org, n, flagged, counts in sorted(
        org_stats, key=lambda s: (-s[2], -s[1], s[0])
    ):
        lines.append(
            f"| {org} | {n} | {flagged} | "
            f"{counts.get('WRONG_IDENTIFIER', 0)} | {counts.get('MISCITED', 0)} | "
            f"{counts.get('DISPUTED', 0)} | {counts.get('LOW_QUALITY', 0)} | "
            f"{counts.get('UNVERIFIED', 0)} |"
        )
    lines.append("")

    # --- the flagged references ------------------------------------------------
    lines.append("## Flagged references")
    lines.append("")
    lines.append(
        "Every reference whose `correctness` is not `VERIFIED` and not `UNVERIFIED`, "
        "i.e. every reference a reviewer has positively judged to be a citation or "
        f"soundness problem. Notes are truncated at {MAX_NOTE_CHARS} characters; the "
        "full text is in the source YAML and in `reports/miscitations.tsv`."
    )
    lines.append("")

    flagged_rows = [r for r in rows if r.correctness in PROBLEM_VALUES]
    for value in PROBLEM_VALUES:
        subset = [r for r in flagged_rows if r.correctness == value]
        if not subset:
            continue
        lines.append(f"### {value} ({len(subset)})")
        lines.append("")
        lines.append("| Organism | Gene | Reference | Title | Rel. | Notes |")
        lines.append("|---|---|---|---|---|---|")
        for row in sorted(
            subset, key=lambda r: (r.organism, r.gene_symbol, r.reference_id)
        ):
            lines.append(
                "| {org} | {gene} | {ref} | {title} | {rel} | {notes} |".format(
                    org=_md_escape(row.organism),
                    gene=_md_escape(row.gene_symbol),
                    ref=_md_escape(row.reference_id),
                    title=_md_escape(_truncate(row.title, 120)),
                    rel=_md_escape(row.relevance),
                    notes=_md_escape(_truncate(row.review_notes)),
                )
            )
        lines.append("")

    if not flagged_rows:
        lines.append("_No references are currently flagged._")
        lines.append("")

    return "\n".join(lines) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--genes-dir", type=Path, default=GENES_DIR, help="root of the genes/ tree"
    )
    parser.add_argument("--tsv-out", type=Path, default=TSV_OUT)
    parser.add_argument("--md-out", type=Path, default=MD_OUT)
    args = parser.parse_args()

    rows, n_files, n_with = collect_rows(args.genes_dir)
    write_tsv(rows, args.tsv_out)

    args.md_out.parent.mkdir(parents=True, exist_ok=True)
    args.md_out.write_text(render_markdown(rows, n_files, n_with))

    counts = _counts(r.correctness for r in rows if r.correctness)
    flagged = sum(counts.get(v, 0) for v in PROBLEM_VALUES)
    print(f"scanned {n_files} review files ({n_with} carry reference_review)")
    print(f"{len(rows)} adjudicated references; {flagged} flagged")
    for value, count in _ordered_counts(counts, CORRECTNESS_ORDER):
        print(f"  {value:<18} {count}")
    print(f"wrote {args.tsv_out.relative_to(REPO_ROOT)}")
    print(f"wrote {args.md_out.relative_to(REPO_ROOT)}")


if __name__ == "__main__":
    main()
