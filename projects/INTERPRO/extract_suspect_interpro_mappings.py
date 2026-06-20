#!/usr/bin/env python3
"""Extract InterPro2GO (GO_REF:0000002) annotations from gene reviews and flag suspect ones.

InterPro2GO mappings are the GO annotations attached to a protein because it matched
an InterPro signature (entry), via the curated InterPro2GO mapping file. In GOA they
appear as IEA annotations with::

    REFERENCE  = GO_REF:0000002
    WITH/FROM  = InterPro:IPRxxxxxx
    ASSIGNED BY = InterPro

This script walks every ``genes/*/*/*-ai-review.yaml``, finds the annotations whose
``original_reference_id`` is ``GO_REF:0000002``, recovers the source InterPro entry
id(s) for each from the matching ``*-goa.tsv`` (the WITH/FROM column), and joins in the
reviewer's action. It then writes:

1. ``suspect_interpro_mappings.tsv`` -- one row per reviewed InterPro2GO annotation,
   with the action and (for non-ACCEPT actions) the reason / proposed replacement.
2. ``interpro_family_priorities.tsv`` -- one row per InterPro entry, aggregating how
   many times it produced an accepted vs a suspect mapping across all reviewed genes.
   This is the prioritized worklist for family-level deep research: entries that
   repeatedly produce suspect (MODIFY / REMOVE / over-annotated) mappings are the ones
   worth researching.

An annotation is "suspect" when its review action is anything other than ``ACCEPT``
(i.e. MODIFY, REMOVE, MARK_AS_OVER_ANNOTATED, KEEP_AS_NON_CORE, UNDECIDED, ...). Plain
ACCEPT means the reviewer endorsed the InterPro2GO mapping as-is.

Reproduce::

    uv run python projects/INTERPRO/extract_suspect_interpro_mappings.py

Outputs are written next to this script (``projects/INTERPRO/``).
"""

from __future__ import annotations

import csv
from collections import defaultdict
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List, Optional, Tuple

import yaml

INTERPRO2GO_REF = "GO_REF:0000002"
# Actions that mean the reviewer did NOT endorse the InterPro2GO mapping as-is.
SUSPECT_ACTIONS = {
    "MODIFY",
    "REMOVE",
    "MARK_AS_OVER_ANNOTATED",
    "KEEP_AS_NON_CORE",
    "UNDECIDED",
}

REPO_ROOT = Path(__file__).resolve().parents[2]
GENES_DIR = REPO_ROOT / "genes"
OUT_DIR = Path(__file__).resolve().parent


@dataclass
class Mapping:
    """A single reviewed InterPro2GO annotation."""

    organism: str
    gene: str
    interpro_ids: List[str]
    term_id: str
    term_label: str
    qualifier: str
    action: str
    reason: str
    proposed_terms: str


@dataclass
class FamilyStats:
    """Aggregated stats for one InterPro entry across all reviewed genes."""

    interpro_id: str
    total: int = 0
    suspect: int = 0
    actions: Dict[str, int] = field(default_factory=lambda: defaultdict(int))
    genes: List[str] = field(default_factory=list)
    term_labels: set = field(default_factory=set)


def _build_goa_index(goa_path: Path) -> Dict[Tuple[str, str], Tuple[List[str], str]]:
    """Map (go_term_id, qualifier) -> (interpro_ids, qualifier) for InterPro2GO rows.

    Falls back to a term-only index so we can still resolve when the qualifier in the
    review YAML is absent.
    """
    index: Dict[Tuple[str, str], Tuple[List[str], str]] = {}
    if not goa_path.exists():
        return index
    with goa_path.open(newline="", encoding="utf-8") as fh:
        reader = csv.DictReader(fh, delimiter="\t")
        for row in reader:
            if (row.get("REFERENCE") or "").strip() != INTERPRO2GO_REF:
                continue
            term = (row.get("GO TERM") or "").strip()
            qualifier = (row.get("QUALIFIER") or "").strip()
            with_from = (row.get("WITH/FROM") or "").strip()
            interpro_ids = [
                part.strip()
                for part in with_from.split("|")
                if part.strip().startswith("InterPro:")
            ]
            interpro_ids = [i.split(":", 1)[1] for i in interpro_ids]
            if term:
                index[(term, qualifier)] = (interpro_ids, qualifier)
                index.setdefault((term, ""), (interpro_ids, qualifier))
    return index


def _extract_proposed_terms(review: dict) -> str:
    terms = review.get("proposed_replacement_terms") or []
    rendered = []
    for term in terms:
        if isinstance(term, dict):
            rendered.append(f"{term.get('id', '')} {term.get('label', '')}".strip())
    return "; ".join(rendered)


def process_review(yaml_path: Path) -> List[Mapping]:
    """Extract reviewed InterPro2GO mappings from a single gene review file."""
    with yaml_path.open(encoding="utf-8") as fh:
        data = yaml.safe_load(fh)
    if not isinstance(data, dict):
        return []

    gene_dir = yaml_path.parent
    organism = gene_dir.parent.name
    gene = gene_dir.name
    goa_index = _build_goa_index(gene_dir / f"{gene}-goa.tsv")

    mappings: List[Mapping] = []
    for ann in data.get("existing_annotations") or []:
        if not isinstance(ann, dict):
            continue
        if (ann.get("original_reference_id") or "").strip() != INTERPRO2GO_REF:
            continue
        term = ann.get("term") or {}
        term_id = (term.get("id") or "").strip()
        term_label = (term.get("label") or "").strip()
        review = ann.get("review") or {}
        action = (review.get("action") or "PENDING").strip()
        reason = (review.get("reason") or review.get("summary") or "").strip()

        # Recover the source InterPro id(s) from GOA; try qualifier-specific first.
        interpro_ids: List[str] = []
        for key in ((term_id, ""),):
            if key in goa_index:
                interpro_ids = goa_index[key][0]
                break

        mappings.append(
            Mapping(
                organism=organism,
                gene=gene,
                interpro_ids=interpro_ids or [],
                term_id=term_id,
                term_label=term_label,
                qualifier="",
                action=action,
                reason=reason,
                proposed_terms=_extract_proposed_terms(review),
            )
        )
    return mappings


def main() -> None:
    review_files = sorted(GENES_DIR.glob("*/*/*-ai-review.yaml"))
    all_mappings: List[Mapping] = []
    for path in review_files:
        all_mappings.extend(process_review(path))

    # Per-annotation TSV
    per_ann = OUT_DIR / "suspect_interpro_mappings.tsv"
    with per_ann.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.writer(fh, delimiter="\t")
        writer.writerow(
            [
                "organism",
                "gene",
                "interpro_ids",
                "go_term_id",
                "go_term_label",
                "action",
                "is_suspect",
                "proposed_replacement_terms",
                "reason",
            ]
        )
        for m in all_mappings:
            writer.writerow(
                [
                    m.organism,
                    m.gene,
                    ",".join(m.interpro_ids),
                    m.term_id,
                    m.term_label,
                    m.action,
                    "yes" if m.action in SUSPECT_ACTIONS else "no",
                    m.proposed_terms,
                    m.reason.replace("\n", " "),
                ]
            )

    # Per-InterPro-entry aggregate TSV (deep-research worklist)
    stats: Dict[str, FamilyStats] = {}
    for m in all_mappings:
        ids = m.interpro_ids or ["UNRESOLVED"]
        for ipr in ids:
            fs = stats.setdefault(ipr, FamilyStats(interpro_id=ipr))
            fs.total += 1
            fs.actions[m.action] += 1
            fs.genes.append(f"{m.organism}/{m.gene}")
            fs.term_labels.add(m.term_label)
            if m.action in SUSPECT_ACTIONS:
                fs.suspect += 1

    priorities = OUT_DIR / "interpro_family_priorities.tsv"
    with priorities.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.writer(fh, delimiter="\t")
        writer.writerow(
            [
                "interpro_id",
                "n_reviewed",
                "n_suspect",
                "suspect_fraction",
                "cached",
                "action_breakdown",
                "example_genes",
                "go_term_labels",
            ]
        )
        for fs in sorted(
            stats.values(), key=lambda s: (s.suspect, s.total), reverse=True
        ):
            cached = (
                REPO_ROOT / "interpro" / "interpro" / fs.interpro_id
            ).exists()
            action_breakdown = ", ".join(
                f"{a}:{n}" for a, n in sorted(fs.actions.items())
            )
            writer.writerow(
                [
                    fs.interpro_id,
                    fs.total,
                    fs.suspect,
                    f"{fs.suspect / fs.total:.2f}" if fs.total else "0.00",
                    "yes" if cached else "no",
                    action_breakdown,
                    "; ".join(sorted(set(fs.genes))[:8]),
                    "; ".join(sorted(t for t in fs.term_labels if t)[:6]),
                ]
            )

    # Console summary
    n_suspect = sum(1 for m in all_mappings if m.action in SUSPECT_ACTIONS)
    n_resolved = sum(1 for m in all_mappings if m.interpro_ids)
    n_entries = len([k for k in stats if k != "UNRESOLVED"])
    print(f"Reviewed gene files scanned : {len(review_files)}")
    print(f"InterPro2GO annotations     : {len(all_mappings)}")
    print(f"  resolved to an IPR id     : {n_resolved}")
    print(f"  flagged suspect (!=ACCEPT): {n_suspect}")
    print(f"Distinct InterPro entries   : {n_entries}")
    print(f"Wrote {per_ann.relative_to(REPO_ROOT)}")
    print(f"Wrote {priorities.relative_to(REPO_ROOT)}")


if __name__ == "__main__":
    main()
