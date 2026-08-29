#!/usr/bin/env python3
"""Measure how deep in ProTrek's ranked list the curated core function appears.

The GOA-overlap categories say whether a prediction agrees with the *existing*
annotation set. This script asks a different and stricter question: does ProTrek
retrieve the molecular function, biological process and location that the AIGR
review identifies as this protein's core biology, and if so at what rank?

For each protein the reference terms are taken from the review's
``core_functions`` block (``molecular_function``,
``contributes_to_molecular_function``, ``directly_involved_in``, ``locations``).
A retrieved term counts as a hit at three strictness levels:

  exact      the retrieved id is the reference id
  descendant the retrieved id is a strict descendant of the reference (more specific)
  ancestor   the retrieved id is a strict ancestor of the reference (less specific)

Reporting the best rank at each level separates "found the right concept" from
"found something in the right part of the ontology".

Usage:
  uv run python projects/PROTREK_EVALUATION/core_function_recall.py \
      --hits projects/PROTREK_EVALUATION/argo50_protrek_hits.tsv \
      --out projects/PROTREK_EVALUATION/argo50_core_function_recall.csv
"""
from __future__ import annotations

import argparse
import csv
import glob
import json
import sys
from collections import Counter
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(Path(__file__).parent))
sys.path.insert(0, str(ROOT / "src"))

from analyze_hits import (  # noqa: E402
    SENTENCE_RE,
    ancestors,
    gene_dir_map,
    normalize_label,
    parse_obo,
)
from ai_gene_review.bioreason_ontology import ensure_frozen_go  # noqa: E402

ASPECT_SLOT = {
    "molecular function": ("molecular_function", "contributes_to_molecular_function"),
    "biological process": ("directly_involved_in",),
    "cellular component": ("locations", "in_complex"),
}


def core_terms(acc: str, dirs: dict[str, Path]) -> dict[str, set[str]]:
    """Reference terms per aspect from the gene's AIGR review core_functions."""
    if acc in dirs:
        hits = [str(p) for p in dirs[acc].glob("*-ai-review.yaml")]
    else:
        hits = glob.glob(str(ROOT / "genes" / "*" / acc / f"{acc}-ai-review.yaml"))
    out = {"molecular function": set(), "biological process": set(), "cellular component": set()}
    if not hits:
        return out
    data = yaml.safe_load(Path(hits[0]).read_text()) or {}
    for cf in data.get("core_functions") or []:
        for aspect, slots in ASPECT_SLOT.items():
            for slot in slots:
                value = cf.get(slot)
                if not value:
                    continue
                items = value if isinstance(value, list) else [value]
                for item in items:
                    if isinstance(item, dict) and item.get("id"):
                        out[aspect].add(item["id"])
    return out


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--hits", required=True, type=Path)
    ap.add_argument("--max-rank", type=int, default=25)
    ap.add_argument("--out", required=True, type=Path)
    ap.add_argument("--summary-out", type=Path, default=None)
    ap.add_argument("--queries", type=Path, default=None,
                    help="query TSV with species_dir/symbol columns (see analyze_hits.py)")
    args = ap.parse_args()

    dirs = gene_dir_map(args.queries)
    by_label, terms, obsolete_by_label = parse_obo(ensure_frozen_go())
    cache: dict[str, set[str]] = {}

    rows = [r for r in csv.DictReader(args.hits.open(), delimiter="\t")
            if r["subsection"] == "GO_annotation" and int(r["rank"]) <= args.max_rank]
    accs = sorted({r["accession"] for r in rows})

    out_rows = []
    for acc in accs:
        refs = core_terms(acc, dirs)
        ranked = []
        for r in sorted((x for x in rows if x["accession"] == acc), key=lambda x: int(x["rank"])):
            m = SENTENCE_RE.match(r["text"].strip())
            if not m:
                continue
            aspect, label = m.group(1), m.group(2).strip()
            ids = sorted(by_label.get(label.lower(), set())
                         or by_label.get(normalize_label(label), set()))
            want_ns = aspect.replace(" ", "_")
            matched = [i for i in ids if terms[i]["namespace"] == want_ns]
            go_id = matched[0] if matched else (ids[0] if ids else "")
            ranked.append((int(r["rank"]), aspect, go_id))

        for aspect, ref_ids in refs.items():
            if not ref_ids:
                continue
            best = {"exact": "", "descendant": "", "ancestor": ""}
            for rank, hit_aspect, go_id in ranked:
                if hit_aspect != aspect or not go_id:
                    continue
                for ref in ref_ids:
                    if go_id == ref:
                        level = "exact"
                    elif ref in ancestors(go_id, terms, cache):
                        level = "descendant"
                    elif go_id in ancestors(ref, terms, cache):
                        level = "ancestor"
                    else:
                        continue
                    if not best[level]:
                        best[level] = f"{rank}:{go_id}"
            out_rows.append({
                "accession": acc,
                "aspect": {"molecular function": "F", "biological process": "P",
                           "cellular component": "C"}[aspect],
                "reference_terms": "|".join(sorted(ref_ids)),
                "best_exact": best["exact"],
                "best_descendant": best["descendant"],
                "best_ancestor": best["ancestor"],
            })

    with args.out.open("w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(out_rows[0].keys()))
        w.writeheader()
        w.writerows(out_rows)

    def rank_of(cell: str) -> int | None:
        return int(cell.split(":")[0]) if cell else None

    summary = {"max_rank": args.max_rank, "rows": len(out_rows),
               "proteins_with_reference_terms": len({r["accession"] for r in out_rows})}
    for aspect in ("F", "P", "C", None):
        subset = [r for r in out_rows if aspect is None or r["aspect"] == aspect]
        if not subset:
            continue
        key = aspect or "ALL"
        stats: dict[str, object] = {"n": len(subset)}
        for level in ("exact", "descendant", "ancestor"):
            ranks = [rank_of(r[f"best_{level}"]) for r in subset]
            ranks = [x for x in ranks if x]
            stats[f"{level}_any_rank"] = len(ranks)
            stats[f"{level}_top1"] = sum(1 for x in ranks if x == 1)
            stats[f"{level}_top3"] = sum(1 for x in ranks if x <= 3)
            stats[f"{level}_top5"] = sum(1 for x in ranks if x <= 5)
        related = [r for r in subset if r["best_exact"] or r["best_descendant"] or r["best_ancestor"]]
        stats["any_relation_any_rank"] = len(related)
        stats["any_relation_top5"] = sum(
            1 for r in related
            if min(x for x in (rank_of(r["best_exact"]), rank_of(r["best_descendant"]),
                               rank_of(r["best_ancestor"])) if x) <= 5)
        summary[key] = stats

    text = json.dumps(summary, indent=2)
    print(text)
    if args.summary_out:
        args.summary_out.write_text(text + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
