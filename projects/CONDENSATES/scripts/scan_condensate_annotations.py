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
from pathlib import Path

import yaml

try:
    from yaml import CSafeLoader as SafeLoader
except ImportError:  # pragma: no cover - depends on the local PyYAML build.
    from yaml import SafeLoader

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


def scan_goa(root: Path) -> dict[str, set[tuple[str, str]]]:
    """Map each term to the set of (species, gene) folders annotating it in GOA."""
    hits: dict[str, set[tuple[str, str]]] = collections.defaultdict(set)
    for path in sorted(glob.glob(str(root / "genes" / "*" / "*" / "*-goa.tsv"))):
        parts = Path(path).parts
        species, gene = parts[-3], parts[-2]
        text = Path(path).read_text(errors="ignore")
        for term in TERMS:
            if term in text:
                hits[term].add((species, gene))
    return hits


def goa_union_count(hits: dict[str, set[tuple[str, str]]]) -> int:
    """Count gene folders carrying at least one scanned term in GOA."""
    gene_folders: set[tuple[str, str]] = set()
    for folders in hits.values():
        gene_folders.update(folders)
    return len(gene_folders)


def scan_reviews(
    root: Path,
) -> tuple[dict[str, collections.Counter[str]], list[tuple[str, str, str, str]]]:
    """Return (per-term action counts, GO:0140693 roster) from review YAML."""
    per_term: dict[str, collections.Counter] = collections.defaultdict(collections.Counter)
    scaffold_roster: list[tuple[str, str, str, str]] = []
    for path in sorted(glob.glob(str(root / "genes" / "*" / "*" / "*-ai-review.yaml"))):
        parts = Path(path).parts
        species, gene = parts[-3], parts[-2]
        text = Path(path).read_text(errors="ignore")
        if not any(term in text for term in TERMS):
            continue
        data = yaml.load(text, Loader=SafeLoader) or {}
        for annotation in data.get("existing_annotations") or []:
            term = (annotation.get("term") or {}).get("id")
            if term not in TERMS:
                continue
            action = (annotation.get("review") or {}).get("action") or "NONE"
            per_term[term][action] += 1
            if term == SCAFFOLD_MF:
                scaffold_roster.append(
                    (species, gene, annotation.get("evidence_type") or "?", action)
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

    print("## GOA coverage summary\n")
    print("| Measure | Gene folders |")
    print("|---|---:|")
    print(f"| Gene folders carrying at least one scanned GOA term | {goa_union_count(goa)} |\n")

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
