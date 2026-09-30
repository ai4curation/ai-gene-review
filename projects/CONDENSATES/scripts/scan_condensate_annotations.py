#!/usr/bin/env python3
"""Audit condensate-space GO annotations across the ai-gene-review corpus.

Emits three tables used by ``projects/CONDENSATES/CONDENSATES-go-audit.md``:

1. per-term GOA coverage -- how many gene folders carry each condensate-space
   term in their ``*-goa.tsv``;
2. per-term review outcomes -- what curators did with each term in
   ``*-ai-review.yaml``;
3. the ``GO:0140693`` roster -- every gene bearing the condensate-scaffold
   molecular function, with evidence code and review action.

Nothing here is hardcoded: rerun after corpus changes and paste the output.

    uv run python projects/CONDENSATES/scripts/scan_condensate_annotations.py

The term list is curated by hand (see TERMS) because GO has no
"biomolecular condensate" class to enumerate from -- ``GO:0043228``
membraneless organelle also subsumes ribosomes and cytoskeletal structures,
which are not condensates. That absence is itself a finding of the audit.
"""

from __future__ import annotations

import argparse
import collections
import glob
import re
from pathlib import Path

# Curated condensate-space terms. CC unless noted.
TERMS: dict[str, str] = {
    "GO:0005730": "nucleolus",
    "GO:0016604": "nuclear body",
    "GO:0016605": "PML body",
    "GO:0016607": "nuclear speck",
    "GO:0042382": "paraspeckles",
    "GO:0010494": "cytoplasmic stress granule",
    "GO:0000932": "P-body",
    "GO:0035770": "ribonucleoprotein granule",
    "GO:0036464": "cytoplasmic ribonucleoprotein granule",
    "GO:0140168": "nuclear ribonucleoprotein granule",
    "GO:0043186": "P granule",
    "GO:0045495": "pole plasm",
    "GO:0000407": "phagophore assembly site",
    "GO:0140693": "molecular condensate scaffold activity (MF)",
    "GO:0140694": "membraneless organelle assembly (BP)",
    "GO:0043228": "membraneless organelle (parent)",
    "GO:0043232": "intracellular membraneless organelle (parent)",
}

SCAFFOLD_MF = "GO:0140693"

# An existing_annotations entry starts at column 0 with "- term:" followed by
# an indented id. Capture through to the next entry.
ANNOTATION_RE = re.compile(r"^- term:\n\s+id: (GO:\d+)\n(.*?)(?=^- term:|\Z)", re.S | re.M)
ACTION_RE = re.compile(r"\n\s+action: ([A-Z_]+)")
EVIDENCE_RE = re.compile(r"\n\s*evidence_type: (\S+)")


def scan_goa(root: Path) -> dict[str, set[tuple[str, str]]]:
    """Map each term to the set of (species, gene) folders annotating it in GOA."""
    hits: dict[str, set[tuple[str, str]]] = collections.defaultdict(set)
    for path in glob.glob(str(root / "genes" / "*" / "*" / "*-goa.tsv")):
        parts = Path(path).parts
        species, gene = parts[-3], parts[-2]
        text = Path(path).read_text(errors="ignore")
        for term in TERMS:
            if term in text:
                hits[term].add((species, gene))
    return hits


def scan_reviews(root: Path):
    """Return (per-term action counts, GO:0140693 roster) from review YAML."""
    per_term: dict[str, collections.Counter] = collections.defaultdict(collections.Counter)
    scaffold_roster: list[tuple[str, str, str, str]] = []
    for path in glob.glob(str(root / "genes" / "*" / "*" / "*-ai-review.yaml")):
        parts = Path(path).parts
        species, gene = parts[-3], parts[-2]
        text = Path(path).read_text(errors="ignore")
        start = text.find("\nexisting_annotations:")
        if start < 0:
            continue
        end = text.find("\ncore_functions:", start)
        body = text[start : end if end > 0 else len(text)]
        for match in ANNOTATION_RE.finditer(body):
            term = match.group(1)
            if term not in TERMS:
                continue
            block = match.group(2)
            action = ACTION_RE.search(block)
            action = action.group(1) if action else "NONE"
            per_term[term][action] += 1
            if term == SCAFFOLD_MF:
                evidence = EVIDENCE_RE.search(block)
                scaffold_roster.append(
                    (species, gene, evidence.group(1) if evidence else "?", action)
                )
    return per_term, scaffold_roster


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--root", type=Path, default=Path(__file__).resolve().parents[3],
        help="Repository root (default: inferred from this script's location).",
    )
    args = parser.parse_args()

    goa = scan_goa(args.root)
    per_term, scaffold_roster = scan_reviews(args.root)

    print("## GOA coverage\n")
    print("| Term | Label | Gene folders |")
    print("|---|---|---|")
    for term, label in sorted(TERMS.items(), key=lambda kv: -len(goa.get(kv[0], ()))):
        print(f"| {term} | {label} | {len(goa.get(term, ()))} |")

    total = sum(sum(c.values()) for c in per_term.values())
    print(f"\n## Review outcomes ({total} reviewed annotations)\n")
    print("| Term | Label | Actions |")
    print("|---|---|---|")
    for term, counts in sorted(per_term.items(), key=lambda kv: -sum(kv[1].values())):
        actions = ", ".join(f"{a} {n}" for a, n in counts.most_common())
        print(f"| {term} | {TERMS[term]} | {actions} |")

    overall: collections.Counter = collections.Counter()
    for counts in per_term.values():
        overall.update(counts)
    print("\nAll actions combined: " + ", ".join(f"{a} {n}" for a, n in overall.most_common()))

    print(f"\n## {SCAFFOLD_MF} roster ({len(scaffold_roster)} annotations)\n")
    print("| Species | Gene | Evidence | Action |")
    print("|---|---|---|---|")
    for species, gene, evidence, action in sorted(scaffold_roster):
        print(f"| {species} | {gene} | {evidence} | {action} |")


if __name__ == "__main__":
    main()
