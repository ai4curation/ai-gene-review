#!/usr/bin/env python3
"""Export AI gene reviews as a GOA change set (one TSV row per proposed edit).

Each reviewed existing annotation becomes one row keyed by the GAF fields used
to match it back to GOA (UniProt accession, GO term, evidence code, reference).
`NEW` annotations and MODIFY replacements are emitted so a consumer can add the
proposed terms. Downstream tools (e.g. the genesets enrichment eval) decide
which actions to apply; this export makes no such choice.

Usage:
    uv run python scripts/export_goa_changeset.py --organism human \
        -o exports/goa_changeset_human.tsv
"""

from __future__ import annotations

import argparse
import csv
import subprocess
import sys
from pathlib import Path

import yaml

try:
    Loader = yaml.CSafeLoader
except AttributeError:  # pragma: no cover - libyaml absent
    Loader = yaml.SafeLoader

COLUMNS = [
    "uniprot_id",
    "gene_symbol",
    "term_id",
    "term_label",
    "evidence_type",
    "original_reference_id",
    "negated",
    "isoform",
    "action",
    "replacement_term_ids",
    "is_core_function_term",
]


def core_function_terms(doc: dict) -> set[str]:
    terms: set[str] = set()
    for cf in doc.get("core_functions") or []:
        for slot in ("molecular_function", "contributes_to_molecular_function"):
            term = cf.get(slot)
            if isinstance(term, dict) and term.get("id"):
                terms.add(term["id"])
        for slot in ("directly_involved_in", "locations", "in_complex"):
            for term in cf.get(slot) or []:
                if isinstance(term, dict) and term.get("id"):
                    terms.add(term["id"])
            term = cf.get(slot)
            if isinstance(term, dict) and term.get("id"):
                terms.add(term["id"])
    return terms


def rows_for(path: Path) -> list[dict]:
    with path.open() as handle:
        doc = yaml.load(handle, Loader=Loader) or {}
    uniprot = doc.get("id", "")
    symbol = doc.get("gene_symbol", "")
    core = core_function_terms(doc)
    rows = []
    for ann in doc.get("existing_annotations") or []:
        term = ann.get("term") or {}
        review = ann.get("review") or {}
        action = review.get("action") or ""
        replacements = [
            t.get("id", "")
            for t in review.get("proposed_replacement_terms") or []
            if isinstance(t, dict) and str(t.get("id", "")).startswith("GO:")
        ]
        rows.append(
            {
                "uniprot_id": uniprot,
                "gene_symbol": symbol,
                "term_id": term.get("id", ""),
                "term_label": term.get("label", ""),
                "evidence_type": ann.get("evidence_type", ""),
                "original_reference_id": ann.get("original_reference_id", ""),
                "negated": "true" if ann.get("negated") else "",
                "isoform": ann.get("isoform", "") or "",
                "action": action,
                "replacement_term_ids": "|".join(replacements),
                "is_core_function_term": "true" if term.get("id") in core else "",
            }
        )
    return rows


def git_sha(repo: Path) -> str:
    try:
        return subprocess.check_output(
            ["git", "-C", str(repo), "rev-parse", "HEAD"], text=True
        ).strip()
    except (OSError, subprocess.CalledProcessError):
        return "unknown"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--organism", default="human")
    parser.add_argument("--genes-dir", type=Path, default=Path("genes"))
    parser.add_argument("-o", "--output", type=Path, required=True)
    args = parser.parse_args()

    files = sorted((args.genes_dir / args.organism).glob("*/*-ai-review.yaml"))
    args.output.parent.mkdir(parents=True, exist_ok=True)
    n_rows = 0
    n_errors = 0
    with args.output.open("w", newline="") as out:
        out.write(f"# ai-gene-review commit: {git_sha(args.genes_dir.resolve().parent)}\n")
        out.write(f"# organism: {args.organism}; review files: {len(files)}\n")
        writer = csv.DictWriter(out, fieldnames=COLUMNS, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        for path in files:
            try:
                rows = rows_for(path)
            except yaml.YAMLError as exc:
                n_errors += 1
                print(f"skip {path}: {exc}", file=sys.stderr)
                continue
            writer.writerows(rows)
            n_rows += len(rows)
    print(f"{len(files)} review files, {n_rows} rows, {n_errors} unparseable -> {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
