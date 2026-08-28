#!/usr/bin/env python3
"""Print a compact curation context for one or more ARGO-ProtNLM-50 proteins.

Bundles what a reviewer needs to assess a ProTrek retrieval hit: the UniProt
protein name and family lines, the curated GOA terms, the AIGR review's own
description and core functions, the ProtNLM2 predictions for the same protein,
and ProTrek's ranked hits across the retrieved subsections.

Usage: uv run python projects/PROTREK_EVALUATION/dump_context.py ACC [ACC ...]
"""
from __future__ import annotations

import csv
import glob
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
HITS = Path(__file__).parent / "argo50_protrek_hits.tsv"
CALLS = Path(__file__).parent / "argo50_protrek_go_calls.csv"
NLM = ROOT / "projects/PROTNLM_EVALUATION/bench50_evaluation_results.csv"


def gene_dir(acc: str) -> Path:
    hits = glob.glob(str(ROOT / "genes" / "*" / acc))
    if not hits:
        raise SystemExit(f"no gene directory for {acc}")
    return Path(hits[0])


def main() -> int:
    accs = sys.argv[1:]
    if not accs:
        raise SystemExit(__doc__)

    hits = list(csv.DictReader(HITS.open(), delimiter="\t"))
    calls = list(csv.DictReader(CALLS.open()))
    nlm = list(csv.DictReader(NLM.open())) if NLM.exists() else []

    for acc in accs:
        d = gene_dir(acc)
        print(f"\n{'=' * 78}\n### {acc}  ({d.parent.name})\n{'=' * 78}")

        flat = d / f"{acc}-uniprot.txt"
        if flat.exists():
            for line in flat.read_text().splitlines():
                if line.startswith(("DE   ", "OS   ", "CC   -!- SIMILARITY", "CC   -!- FUNCTION",
                                    "DR   InterPro", "DR   Pfam", "DR   PANTHER", "KW   ")):
                    print(line)

        goa = d / f"{acc}-goa.tsv"
        if goa.exists():
            print("\n-- GOA --")
            seen = set()
            for row in csv.DictReader(goa.open(), delimiter="\t"):
                key = (row["GO TERM"], row["GO EVIDENCE CODE"])
                if key in seen:
                    continue
                seen.add(key)
                print(f"  {row['QUALIFIER']:16s} {row['GO TERM']} {row['GO NAME']}"
                      f"  [{row['GO EVIDENCE CODE']} {row['REFERENCE']} {row['WITH/FROM']}]")

        review = d / f"{acc}-ai-review.yaml"
        if review.exists():
            data = yaml.safe_load(review.read_text())
            print("\n-- AIGR review description --")
            print((data.get("description") or "").strip())
            cf = data.get("core_functions") or []
            if cf:
                print("\n-- AIGR core_functions --")
                print(yaml.safe_dump(cf, sort_keys=False, width=100).strip())

        mine = [r for r in nlm if r["accession"] == acc]
        if mine:
            print("\n-- ProtNLM2 predictions --")
            for r in mine:
                print(f"  {r['pred_id']} {r['pred_label']}  [{r['match_category']}]")

        print("\n-- ProTrek GO_annotation hits (top 5) --")
        for r in calls:
            if r["accession"] == acc and int(r["rank"]) <= 5:
                print(f"  #{r['rank']} score={r['protrek_score']:>7s} {r['aspect']} "
                      f"{r['pred_id'] or '(unresolved)'} {r['pred_label']}  "
                      f"[{r['match_category']}{'/' + r['goa_match_label'] if r['goa_match_label'] else ''}]")

        for sub in ("Function", "Subcellular_location", "Catalytic_activity"):
            rows = [r for r in hits if r["accession"] == acc and r["subsection"] == sub and int(r["rank"]) <= 3]
            if rows:
                print(f"\n-- ProTrek {sub} hits (top 3) --")
                for r in rows:
                    text = r["text"] if len(r["text"]) < 300 else r["text"][:300] + " ..."
                    print(f"  #{r['rank']} score={float(r['protrek_score']):>6.2f} {text}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
