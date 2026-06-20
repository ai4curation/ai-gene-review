#!/usr/bin/env python
"""Reproducible, stratified-by-aspect sampler for the EVIDENCE_SOURCE_SUFFICIENCY study.

Draws a fixed-seed sample of human gene reviews (status COMPLETE) and emits the
labeling instrument as TSVs. Stratification by GO aspect is achieved by taking
*all* MF and BP ACCEPT annotations in each selected gene and *capping* the
abundant CC aspect, so the labeled set is balanced rather than CC-dominated
(ACCEPT annotations across COMPLETE human genes are ~CC 12k / BP 6.7k / MF 5.5k).

Outputs (under --out, default this script's ``sample/`` dir):

* ``selected_genes.tsv``           - the sampled genes + per-aspect counts
* ``annotation_instrument.tsv``    - one row per labeled ACCEPT annotation (Layer 2)
* ``reference_instrument.tsv``     - one row per reference in selected genes (Layer 1)
* ``blind_ablation_assignments.tsv`` - the blinded validation subsample

Run:

    uv run python projects/EVIDENCE_SOURCE_SUFFICIENCY/sample/sample_genes.py \
        --seed 20260614 --n-genes 30 --cc-cap 10 --per-gene-cap 30
"""

from __future__ import annotations

import argparse
import csv
import glob
import os
import random
from pathlib import Path
from typing import Dict, List, Optional

import yaml

# Optional reuse of the publication-type machinery for pre-filling Layer 1.
try:
    from ai_gene_review.etl.publication_type import classify_reference_id
    from ai_gene_review.tools.analyze_evidence_sources import (
        DEFAULT_TYPE_CACHE,
        load_type_cache,
        resolve_publication_type,
    )

    _HAVE_PT = True
except Exception:  # pragma: no cover - keep the sampler usable standalone
    _HAVE_PT = False

ASPECT_CODE = {
    "molecular_function": "MF",
    "biological_process": "BP",
    "cellular_component": "CC",
}
BLIND_BUNDLES = ["ABSTRACT_ONLY", "REVIEW_ONLY", "DEEP_RESEARCH_ONLY"]

ANNOTATION_COLUMNS = [
    # machine-filled
    "gene",
    "term_id",
    "term_label",
    "aspect",
    "evidence_code",
    "qualifier",
    "original_reference_ids",
    "support_reference_ids",
    # human-filled observations
    "justifying_fact",
    "fact_in_abstract",  # Y / N / partial
    "fact_in_review",  # Y / N
    "fact_in_deep_research",  # Y / N
    "section_of_fact",  # reference_section_type vocab
    "minimal_sufficient_tier",  # derived: ABSTRACT / REVIEW / DEEP_RESEARCH / FULLTEXT_PRIMARY
    "labeler",
    "confidence",
    "notes",
]

REFERENCE_COLUMNS = [
    "gene",
    "reference_id",
    "publication_type_auto",
    # human-filled
    "publication_type_final",
    "is_review_final",  # Y / N
    "notes",
]

BLIND_COLUMNS = [
    "gene",
    "term_id",
    "aspect",
    "bundle",  # which restricted evidence bundle the blind reviewer gets
    # blind-filled (reviewer is blinded to the original ACCEPT and to full text)
    "blind_verdict",  # ACCEPT / UNDECIDED / REJECT
    "blind_reason",
    "blind_reviewer",
]


def aspect_map_for_gene(gene_dir: str) -> Dict[str, str]:
    """Map GO term id -> aspect code (MF/BP/CC) from a gene's GOA TSV(s)."""
    m: Dict[str, str] = {}
    for goa in glob.glob(os.path.join(gene_dir, "*-goa.tsv")):
        with open(goa) as f:
            for row in csv.DictReader(f, delimiter="\t"):
                term = (row.get("GO TERM") or "").strip()
                aspect = ASPECT_CODE.get((row.get("GO ASPECT") or "").strip())
                if term and aspect:
                    m[term] = aspect
    return m


def collect_accept_annotations(data: dict, amap: Dict[str, str]) -> List[dict]:
    """Return ACCEPT annotation rows (with aspect) for a gene review dict."""
    gene = data.get("gene_symbol") or ""
    rows: List[dict] = []
    for ann in data.get("existing_annotations") or []:
        review = ann.get("review") or {}
        if review.get("action") != "ACCEPT":
            continue
        term = ann.get("term") or {}
        term_id = term.get("id") or ""
        support = [
            sb.get("reference_id")
            for sb in (review.get("supported_by") or [])
            if sb.get("reference_id")
        ]
        rows.append(
            {
                "gene": gene,
                "term_id": term_id,
                "term_label": term.get("label") or "",
                "aspect": amap.get(term_id, "unknown"),
                "evidence_code": ann.get("evidence_type") or "",
                "qualifier": ann.get("qualifier") or "",
                "original_reference_ids": ann.get("original_reference_id") or "",
                "support_reference_ids": "|".join(support),
            }
        )
    return rows


def select_gene_annotations(
    accept_rows: List[dict], rng: random.Random, cc_cap: int, per_gene_cap: int
) -> List[dict]:
    """Pick which ACCEPT annotations of one gene to label.

    Takes all MF and BP rows, a capped random subset of CC rows, then trims to
    ``per_gene_cap`` total (dropping CC first, then BP) to bound clustering.
    """
    by_aspect: Dict[str, List[dict]] = {"MF": [], "BP": [], "CC": [], "unknown": []}
    for r in accept_rows:
        by_aspect.get(r["aspect"], by_aspect["unknown"]).append(r)

    cc = by_aspect["CC"][:]
    rng.shuffle(cc)
    chosen = by_aspect["MF"] + by_aspect["BP"] + cc[:cc_cap]

    if len(chosen) > per_gene_cap:
        # drop CC first, then BP, keeping MF
        keep: List[dict] = []
        for aspect in ("MF", "BP", "CC", "unknown"):
            for r in chosen:
                if r["aspect"] == aspect and len(keep) < per_gene_cap:
                    keep.append(r)
        chosen = keep
    return chosen


def collect_reference_rows(
    data: dict, type_cache: Optional[dict]
) -> List[dict]:
    """One row per reference id appearing anywhere in a selected gene review."""
    gene = data.get("gene_symbol") or ""
    seen: Dict[str, dict] = {}

    def add(ref_id: Optional[str]):
        if not ref_id or ref_id in seen:
            return
        if _HAVE_PT:
            ptype = (
                resolve_publication_type(ref_id, type_cache or {})
                if type_cache is not None
                else (classify_reference_id(ref_id) or "UNKNOWN")
            )
        else:
            ptype = ""
        seen[ref_id] = {
            "gene": gene,
            "reference_id": ref_id,
            "publication_type_auto": ptype,
            "publication_type_final": "",
            "is_review_final": "",
            "notes": "",
        }

    for ref in data.get("references") or []:
        add(ref.get("id"))
    for ann in data.get("existing_annotations") or []:
        add(ann.get("original_reference_id"))
        for sb in (ann.get("review") or {}).get("supported_by") or []:
            add(sb.get("reference_id"))
    return list(seen.values())


def write_tsv(path: Path, columns: List[str], rows: List[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=columns, delimiter="\t", extrasaction="ignore")
        w.writeheader()
        for r in rows:
            w.writerow(r)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--genes-dir", default="genes/human")
    ap.add_argument("--status", default="COMPLETE")
    ap.add_argument("--seed", type=int, default=20260614)
    ap.add_argument("--n-genes", type=int, default=30)
    ap.add_argument("--cc-cap", type=int, default=10, help="max CC ACCEPT annotations labeled per gene")
    ap.add_argument("--per-gene-cap", type=int, default=30, help="max total labeled annotations per gene")
    ap.add_argument("--blind-frac", type=float, default=0.18)
    ap.add_argument("--out", default=str(Path(__file__).parent))
    args = ap.parse_args()

    rng = random.Random(args.seed)
    type_cache = None
    if _HAVE_PT and Path(DEFAULT_TYPE_CACHE).exists():
        type_cache = load_type_cache(DEFAULT_TYPE_CACHE)

    # Frame: COMPLETE gene reviews that have >=1 ACCEPT annotation.
    candidates: List[tuple[str, dict, List[dict]]] = []
    for y in sorted(glob.glob(os.path.join(args.genes_dir, "*/*-ai-review.yaml"))):
        data = yaml.safe_load(open(y))
        if not data or data.get("status") != args.status:
            continue
        amap = aspect_map_for_gene(os.path.dirname(y))
        accepts = collect_accept_annotations(data, amap)
        if accepts:
            candidates.append((y, data, accepts))

    rng.shuffle(candidates)
    selected = candidates[: args.n_genes]

    annotation_rows: List[dict] = []
    reference_rows: List[dict] = []
    gene_summary: List[dict] = []
    for y, data, accepts in selected:
        chosen = select_gene_annotations(accepts, rng, args.cc_cap, args.per_gene_cap)
        annotation_rows.extend(chosen)
        reference_rows.extend(collect_reference_rows(data, type_cache))
        counts = {a: sum(1 for r in chosen if r["aspect"] == a) for a in ("MF", "BP", "CC")}
        gene_summary.append(
            {
                "gene": data.get("gene_symbol") or Path(y).stem,
                "path": y,
                "n_labeled": len(chosen),
                "MF": counts["MF"],
                "BP": counts["BP"],
                "CC": counts["CC"],
            }
        )

    # Blind-ablation subsample, stratified by aspect, bundles round-robin.
    by_aspect: Dict[str, List[dict]] = {}
    for r in annotation_rows:
        by_aspect.setdefault(r["aspect"], []).append(r)
    blind_rows: List[dict] = []
    bundle_i = 0
    for aspect, rows in sorted(by_aspect.items()):
        pool = rows[:]
        rng.shuffle(pool)
        k = max(1, round(len(pool) * args.blind_frac)) if pool else 0
        for r in pool[:k]:
            blind_rows.append(
                {
                    "gene": r["gene"],
                    "term_id": r["term_id"],
                    "aspect": r["aspect"],
                    "bundle": BLIND_BUNDLES[bundle_i % len(BLIND_BUNDLES)],
                    "blind_verdict": "",
                    "blind_reason": "",
                    "blind_reviewer": "",
                }
            )
            bundle_i += 1

    out = Path(args.out)
    write_tsv(out / "selected_genes.tsv", ["gene", "path", "n_labeled", "MF", "BP", "CC"], gene_summary)
    write_tsv(out / "annotation_instrument.tsv", ANNOTATION_COLUMNS, annotation_rows)
    write_tsv(out / "reference_instrument.tsv", REFERENCE_COLUMNS, reference_rows)
    write_tsv(out / "blind_ablation_assignments.tsv", BLIND_COLUMNS, blind_rows)

    totals = {a: sum(1 for r in annotation_rows if r["aspect"] == a) for a in ("MF", "BP", "CC", "unknown")}
    print(f"seed={args.seed}  genes={len(selected)}")
    print(f"labeled ACCEPT annotations: {len(annotation_rows)}  by aspect: {totals}")
    print(f"references to type: {len(reference_rows)}")
    print(f"blind-ablation rows: {len(blind_rows)}")
    print(f"outputs written to {out}/")


if __name__ == "__main__":
    main()
