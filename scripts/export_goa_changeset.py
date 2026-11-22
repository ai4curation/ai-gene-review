#!/usr/bin/env python3
"""Export AI gene reviews as a GOA change set (one TSV row per proposed edit).

Each reviewed existing annotation becomes one row keyed by the GAF fields used
to match it back to GOA: UniProt accession, GO term, qualifier (relation),
evidence code and reference. `NEW` annotations are exported too, with the
qualifier a consumer needs to construct a GAF row. Downstream tools (e.g. the
genesets enrichment eval) decide which actions to apply; this export makes no
such choice.

Output contract:
- Two leading `# ` comment lines record provenance (ai-gene-review commit, with
  `-dirty` when the working tree had uncommitted changes, and the organism and
  number of review files). Read with `comment="#"` (pandas) or skip lines that
  start with `#`; the third line is the TSV header.
- `retired` is `true` for annotations the review marks as no longer in GOA, so a
  consumer can tell an expected non-match from a key mismatch.
- `replacement_term_ids` lists MODIFY replacements; a replacement that is a
  proposed new term (no GO id yet) is written as `NTR`, and
  `replacement_is_proposed_term` is `true` on that row. A consumer applying
  MODIFY should skip such rows rather than drop the original term.
- `is_core_function_term` is an exact-id match against the review's
  `core_functions` GO terms (MF, BP and CC pooled). It is not ancestor-aware.
- The run exits non-zero if any review file could not be read; the output is
  written to a temporary file and only moved into place on success.

Usage:
    uv run python scripts/export_goa_changeset.py --organism human \
        -o exports/goa_changeset_human.tsv
"""

from __future__ import annotations

import argparse
import csv
import os
import subprocess
import sys
import tempfile
from pathlib import Path

import yaml

try:
    Loader = yaml.CSafeLoader
except AttributeError:  # pragma: no cover - libyaml absent
    Loader = yaml.SafeLoader

REPO_ROOT = Path(__file__).resolve().parents[1]

COLUMNS = [
    "uniprot_id",
    "gene_symbol",
    "term_id",
    "term_label",
    "qualifier",
    "evidence_type",
    "original_reference_id",
    "negated",
    "isoform",
    "retired",
    "action",
    "replacement_term_ids",
    "replacement_is_proposed_term",
    "is_core_function_term",
]

# core_functions slots holding GO terms. anatomical_locations (UBERON/CL) and
# substrates (CHEBI) are deliberately excluded: they are not GO terms.
SINGLE_VALUED_GO_SLOTS = ("molecular_function", "contributes_to_molecular_function", "in_complex")
MULTI_VALUED_GO_SLOTS = ("directly_involved_in", "locations")


class ReviewFileError(ValueError):
    """A review file that parses as YAML but does not have the expected shape."""


def core_function_terms(doc: dict) -> set[str]:
    terms: set[str] = set()
    for cf in doc.get("core_functions") or []:
        if not isinstance(cf, dict):
            continue
        candidates = [cf.get(slot) for slot in SINGLE_VALUED_GO_SLOTS]
        for slot in MULTI_VALUED_GO_SLOTS:
            candidates.extend(cf.get(slot) or [])
        for term in candidates:
            if isinstance(term, dict) and term.get("id"):
                terms.add(term["id"])
    return terms


def rows_for(path: Path) -> list[dict]:
    with path.open() as handle:
        doc = yaml.load(handle, Loader=Loader) or {}
    if not isinstance(doc, dict):
        raise ReviewFileError(f"top level is {type(doc).__name__}, not a mapping")
    uniprot = doc.get("id", "")
    symbol = doc.get("gene_symbol", "")
    core = core_function_terms(doc)
    rows = []
    for index, ann in enumerate(doc.get("existing_annotations") or []):
        if not isinstance(ann, dict):
            raise ReviewFileError(f"existing_annotations[{index}] is not a mapping")
        term = ann.get("term") or {}
        review = ann.get("review") or {}
        replacements = []
        proposed = False
        for t in review.get("proposed_replacement_terms") or []:
            if not isinstance(t, dict):
                continue
            term_id = str(t.get("id", ""))
            if term_id.startswith("GO:"):
                replacements.append(term_id)
            elif term_id:
                replacements.append("NTR")
                proposed = True
        rows.append(
            {
                "uniprot_id": uniprot,
                "gene_symbol": symbol,
                "term_id": term.get("id", ""),
                "term_label": term.get("label", ""),
                "qualifier": ann.get("qualifier", "") or "",
                "evidence_type": ann.get("evidence_type", ""),
                "original_reference_id": ann.get("original_reference_id", ""),
                "negated": "true" if ann.get("negated") else "",
                "isoform": ann.get("isoform", "") or "",
                "retired": "true" if ann.get("retired") else "",
                "action": review.get("action") or "",
                "replacement_term_ids": "|".join(replacements),
                "replacement_is_proposed_term": "true" if proposed else "",
                "is_core_function_term": "true" if term.get("id") in core else "",
            }
        )
    return rows


def git_describe(repo: Path) -> str:
    try:
        return subprocess.check_output(
            ["git", "-C", str(repo), "describe", "--always", "--dirty", "--abbrev=40"],
            text=True,
            stderr=subprocess.DEVNULL,
        ).strip()
    except (OSError, subprocess.CalledProcessError):
        return "unknown"


def export(organism_dir: Path, organism: str, output: Path) -> tuple[int, int, int]:
    """Write the change set; return (files, rows, unreadable files)."""
    files = sorted(organism_dir.glob("*/*-ai-review.yaml"))
    output.parent.mkdir(parents=True, exist_ok=True)
    n_rows = 0
    n_errors = 0
    fd, tmp_name = tempfile.mkstemp(dir=output.parent, prefix=f".{output.name}.", suffix=".tmp")
    try:
        with os.fdopen(fd, "w", newline="") as out:
            out.write(f"# ai-gene-review commit: {git_describe(REPO_ROOT)}\n")
            out.write(f"# organism: {organism}; review files: {len(files)}\n")
            writer = csv.DictWriter(out, fieldnames=COLUMNS, delimiter="\t", lineterminator="\n")
            writer.writeheader()
            for path in files:
                try:
                    rows = rows_for(path)
                except (yaml.YAMLError, ReviewFileError, AttributeError, TypeError) as exc:
                    n_errors += 1
                    print(f"skip {path}: {exc}", file=sys.stderr)
                    continue
                writer.writerows(rows)
                n_rows += len(rows)
        if n_errors:
            os.unlink(tmp_name)
        else:
            os.replace(tmp_name, output)
    except BaseException:
        if os.path.exists(tmp_name):
            os.unlink(tmp_name)
        raise
    return len(files), n_rows, n_errors


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--organism", default="human")
    parser.add_argument("--genes-dir", type=Path, default=REPO_ROOT / "genes")
    parser.add_argument("-o", "--output", type=Path, required=True)
    args = parser.parse_args(argv)

    organism_dir = args.genes_dir / args.organism
    if not organism_dir.is_dir():
        print(f"error: no such organism directory: {organism_dir}", file=sys.stderr)
        return 2
    n_files, n_rows, n_errors = export(organism_dir, args.organism, args.output)
    if n_files == 0:
        print(f"error: no *-ai-review.yaml files under {organism_dir}", file=sys.stderr)
        return 2
    if n_errors:
        print(f"error: {n_errors} of {n_files} review files unreadable; {args.output} not written", file=sys.stderr)
        return 1
    print(f"{n_files} review files, {n_rows} rows -> {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
