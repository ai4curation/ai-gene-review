#!/usr/bin/env python3
"""Print a compact curation context for ARGO139 genes.

Bundles what a reviewer needs to assess a ProTrek retrieval hit against the same
gene the BioReason evaluation scored: UniProt identity lines, curated GOA, the
AIGR review's description and core-function terms, the existing GO-GPT and
BioReason-SFT VDCL calls for the same gene, and ProTrek's ranked hits.

Usage: uv run python projects/PROTREK_EVALUATION/dump_argo139_context.py SYMBOL [SYMBOL ...]
"""
from __future__ import annotations

import csv
import sys
import textwrap
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).parent
QUERIES = HERE / "argo139_sequences.tsv"
HITS = HERE / "argo139_protrek_hits.tsv"
CALLS = HERE / "argo139_protrek_go_calls.csv"


def main() -> int:
    wanted = sys.argv[1:]
    if not wanted:
        raise SystemExit(__doc__)

    queries = {r["symbol"]: r for r in csv.DictReader(QUERIES.open(), delimiter="\t")}
    hits = list(csv.DictReader(HITS.open(), delimiter="\t")) if HITS.exists() else []
    calls = list(csv.DictReader(CALLS.open())) if CALLS.exists() else []

    for symbol in wanted:
        q = queries.get(symbol)
        if not q:
            print(f"!! {symbol} not in ARGO139")
            continue
        acc, d = q["accession"], ROOT / "genes" / q["species_dir"] / symbol
        print(f"\n{'=' * 72}\n### {symbol} ({q['species_dir']}, {acc}, {q['length']} aa)")

        flat = d / f"{symbol}-uniprot.txt"
        if flat.exists():
            for line in flat.read_text().splitlines():
                if line.startswith(("DE   RecName", "DE   SubName", "CC   -!- SIMILARITY", "DR   PANTHER")):
                    print(line[:150])

        goa = d / f"{symbol}-goa.tsv"
        if goa.exists():
            terms = {}
            for row in csv.DictReader(goa.open(), delimiter="\t"):
                terms.setdefault(row["GO TERM"], (row["GO NAME"], set()))[1].add(row["GO EVIDENCE CODE"])
            print(f"-- GOA ({len(terms)} terms) --")
            for t, (name, ev) in sorted(terms.items()):
                print(f"   {t} {name} [{','.join(sorted(ev))}]")

        rev = d / f"{symbol}-ai-review.yaml"
        if rev.exists():
            data = yaml.safe_load(rev.read_text()) or {}
            print(f"-- AIGR review (status: {data.get('status', '?')}) --")
            print(textwrap.fill((data.get("description") or "").strip()[:900], 116))
            print("-- core_functions --")
            for cf in data.get("core_functions") or []:
                bits = []
                for slot in ("molecular_function", "contributes_to_molecular_function",
                             "directly_involved_in", "locations", "in_complex"):
                    v = cf.get(slot)
                    if not v:
                        continue
                    items = v if isinstance(v, list) else [v]
                    bits.append(f"{slot}=" + ", ".join(
                        f"{i['id']} {i['label']}" for i in items if isinstance(i, dict)))
                print("  * " + "; ".join(bits))
                print(textwrap.fill((cf.get("description") or "")[:230], 112, initial_indent="    ",
                                    subsequent_indent="    "))

        for label, suffix in (("GO-GPT leaf", "gogpt-leaf-predictions"),
                              ("BioReason-SFT", "sft-predictions")):
            f = d / f"{symbol}-{suffix}.yaml"
            if not f.exists():
                continue
            data = yaml.safe_load(f.read_text()) or {}
            preds = data.get("predictions") or []
            shown = [p for p in preds if p["review"]["assessment"] != "UNC"][:6]
            print(f"-- {label} ({len(preds)} preds; non-UNC shown) --")
            for p in shown:
                print(f"   {p['predicted_term']['id']} {p['predicted_term']['label']} "
                      f"[{p['review']['assessment']}]")

        print("-- ProTrek GO top5 --")
        for r in calls:
            if r["accession"] == acc and int(r["rank"]) <= 5:
                extra = f"/{r['goa_match_label']}" if r["goa_match_label"] else ""
                print(f"   #{r['rank']} {float(r['protrek_score']):6.2f} {r['aspect']} "
                      f"{r['pred_id'] or '(unresolved)'} {r['pred_label']} [{r['match_category']}{extra}]")
        print("-- ProTrek Function top2 --")
        for r in hits:
            if r["accession"] == acc and r["subsection"] == "Function" and int(r["rank"]) <= 2:
                print(f"   #{r['rank']} {float(r['protrek_score']):6.2f} {r['text'][:230]}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
