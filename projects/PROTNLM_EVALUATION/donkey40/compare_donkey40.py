#!/usr/bin/env python3
"""DONKEY40: compare donkey TreeGrafter rows, horse PAINT IBA rows and donkey
ProtNLM2 GO predictions on the same 40 genes.

Inputs (all in the repo except the GO ontology file):
  - selection.yaml (donkey accession, gene symbol, horse ortholog accession);
  - genes/EQUAS/SYM/SYM-goa.tsv and SYM-ai-review.yaml (donkey GOA rows and
    the reviewer action on each);
  - genes/EQUAS/SYM/SYM-protnlm-predictions-review.yaml (ProtNLM2 GO
    predictions and their VDCL assessments);
  - horse_iba.tsv next to this script: the horse orthologs' GO_REF:0000033 rows,
    written from QuickGO by ``--fetch-horse`` (run once; later runs are offline).

TreeGrafter contributes to donkey GOA in two ways: as its own row
(GO_REF:0000118, ``tg_solo``) and inside a merged electronic row
(GO_REF:0000120 whose WITH/FROM carries a PANTHER:PTN node, ``tg_merged``).
Both are compared against horse IBA, per gene and aspect, by GO is_a/part_of:
same term, TreeGrafter deeper, TreeGrafter shallower, sibling (a shared
direct parent), or unmatched.

Outputs next to this script:
  donkey40_tg_vs_iba.tsv     one row per TreeGrafter row or unmatched IBA row
  donkey40_protnlm_vs.tsv    one row per ProtNLM2 GO prediction, related to the
                             donkey TreeGrafter rows and the horse IBA rows
and a printed summary.

Run:
  python3 projects/PROTNLM_EVALUATION/donkey40/compare_donkey40.py --fetch-horse --go-obo go-basic.obo
  python3 projects/PROTNLM_EVALUATION/donkey40/compare_donkey40.py --go-obo go-basic.obo
"""
from __future__ import annotations

import argparse
import csv
import json
import os
import sys
import time
import urllib.parse
import urllib.request
from collections import Counter

import yaml

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "projects", "TREEGRAFTER"))
from propagation_rules import ancestors, load_go  # noqa: E402

QUICKGO = "https://www.ebi.ac.uk/QuickGO/services/annotation/search"
ASPECT_PRED = {"GO_MF": "molecular_function", "GO_BP": "biological_process",
               "GO_CC": "cellular_component"}
ASPECT_QG = {"molecular_function": "molecular_function", "biological_process": "biological_process",
             "cellular_component": "cellular_component", "F": "molecular_function",
             "P": "biological_process", "C": "cellular_component"}
# TOO_GENERAL (true but entailed by a more specific term in the same review)
# counts as down-graded, like MODIFY: the review did not keep the term as is.
DOWNGRADE = {"REMOVE", "MARK_AS_OVER_ANNOTATED", "MODIFY", "TOO_GENERAL"}
CORRECT, WRONG = {"COR", "CNN", "LSP"}, {"NPI", "PLI", "REP"}
HORSE_TSV = os.path.join(HERE, "horse_iba.tsv")


def get(url: str) -> str:
    for attempt in range(4):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "ai-gene-review/donkey40",
                                                       "Accept": "application/json"})
            with urllib.request.urlopen(req, timeout=120) as r:
                return r.read().decode()
        except Exception:
            if attempt == 3:
                raise
            time.sleep(2 ** attempt)


def fetch_horse(records: list) -> None:
    rows = []
    for rec in records:
        acc, page = rec["horse_accession"], 1
        while True:
            q = urllib.parse.urlencode({"geneProductId": acc, "reference": "GO_REF:0000033",
                                        "limit": 200, "page": page})
            d = json.loads(get(f"{QUICKGO}?{q}"))
            for x in d["results"]:
                rows.append({"gene_symbol": rec["gene_symbol"], "horse_accession": acc,
                             "qualifier": x.get("qualifier", ""), "go_id": x["goId"],
                             "aspect": ASPECT_QG.get(x.get("goAspect", ""), x.get("goAspect", ""))})
            if page >= d["pageInfo"]["total"]:
                break
            page += 1
    with open(HORSE_TSV, "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0]), delimiter="\t", lineterminator="\n")
        w.writeheader()
        w.writerows(rows)
    print(f"wrote {HORSE_TSV}: {len(rows)} horse IBA rows")


def donkey_rows(sym: str) -> list:
    """TreeGrafter-derived donkey GOA rows with the reviewer's action."""
    d = os.path.join(ROOT, "genes", "EQUAS", sym)
    review = yaml.safe_load(open(os.path.join(d, f"{sym}-ai-review.yaml")))
    actions = {}
    for a in review.get("existing_annotations") or []:
        key = (a["term"]["id"], a.get("original_reference_id", ""))
        actions.setdefault(key, (a.get("review") or {}).get("action", ""))
    out, seen = [], set()
    for r in csv.DictReader(open(os.path.join(d, f"{sym}-goa.tsv")), delimiter="\t"):
        ref, w = r["REFERENCE"], r["WITH/FROM"]
        if ref == "GO_REF:0000118":
            kind = "tg_solo"
        elif ref == "GO_REF:0000120" and "PANTHER:PTN" in w:
            kind = "tg_merged"
        else:
            continue
        if "NOT" in r["QUALIFIER"]:
            continue
        key = (r["GO TERM"], ref)
        if key in seen:
            continue
        seen.add(key)
        out.append({"term": r["GO TERM"], "label": r["GO NAME"], "aspect": r["GO ASPECT"],
                    "kind": kind, "action": actions.get(key, "")})
    return out


def relate(a: str, b: str, parents: dict, anc) -> str:
    """Relation of a (left) to b (right)."""
    if a == b:
        return "same_term"
    if b in anc(a):
        return "left_deeper"
    if a in anc(b):
        return "left_shallower"
    if parents.get(a, set()) & parents.get(b, set()):
        return "sibling"
    return ""


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--go-obo", required=True)
    ap.add_argument("--fetch-horse", action="store_true")
    args = ap.parse_args()
    records = yaml.safe_load(open(os.path.join(HERE, "selection.yaml")))["records"]
    if args.fetch_horse or not os.path.exists(HORSE_TSV):
        fetch_horse(records)
    parents, _ = load_go(args.go_obo)
    cache: dict = {}

    def anc(t):
        return ancestors(t, parents, cache)

    horse: dict = {}
    for r in csv.DictReader(open(HORSE_TSV), delimiter="\t"):
        if "not" in r["qualifier"].lower().split("|") or r["qualifier"].upper().startswith("NOT"):
            continue
        horse.setdefault(r["gene_symbol"], {})[r["go_id"]] = r["aspect"]

    tg_rows, pn_rows = [], []
    for rec in records:
        sym = rec["gene_symbol"]
        tg = donkey_rows(sym)
        iba = horse.get(sym, {})
        matched_iba = set()
        rel_name = {"same_term": "same_term", "left_deeper": "tg_deeper",
                    "left_shallower": "tg_shallower", "sibling": "sibling"}
        for t in tg:
            best, best_iba = "tg_unmatched", ""
            order = ["same_term", "left_deeper", "left_shallower", "sibling"]
            for g, asp in iba.items():
                if asp != t["aspect"]:
                    continue
                rel = relate(t["term"], g, parents, anc)
                if rel:
                    matched_iba.add(g)
                    if best == "tg_unmatched" or order.index(rel) < order.index(
                            {v: k for k, v in rel_name.items()}[best]):
                        best, best_iba = rel_name[rel], g
            tg_rows.append({"gene_symbol": sym, "kind": t["kind"], "aspect": t["aspect"],
                            "tg_term": t["term"], "tg_label": t["label"], "tg_action": t["action"],
                            "relation_to_horse_iba": best, "horse_iba_term": best_iba})
        for g, asp in sorted(iba.items()):
            if g not in matched_iba:
                tg_rows.append({"gene_symbol": sym, "kind": "iba_unmatched", "aspect": asp,
                                "tg_term": "", "tg_label": "", "tg_action": "",
                                "relation_to_horse_iba": "iba_unmatched", "horse_iba_term": g})
        pr = os.path.join(ROOT, "genes", "EQUAS", sym, f"{sym}-protnlm-predictions-review.yaml")
        doc = yaml.safe_load(open(pr)) or {}
        for p in doc.get("predictions") or []:
            term = p.get("predicted_term") or {}
            if p.get("predicted_term_type") not in ASPECT_PRED or not str(term.get("id", "")).startswith("GO:"):
                continue
            asp, pid = ASPECT_PRED[p["predicted_term_type"]], term["id"]

            def best_rel(targets):
                out = ""
                for x in targets:
                    rel = relate(pid, x, parents, anc)
                    if rel and (not out or ["same_term", "left_deeper", "left_shallower",
                                            "sibling"].index(rel) < ["same_term", "left_deeper",
                                            "left_shallower", "sibling"].index(out)):
                        out = rel
                return (out.replace("left_", "protnlm_") if out else "none")

            pn_rows.append({"gene_symbol": sym, "aspect": asp, "protnlm_term": pid,
                            "protnlm_label": term.get("label", ""),
                            "assessment": (p.get("review") or {}).get("assessment", ""),
                            "vs_donkey_treegrafter": best_rel([t["term"] for t in tg if t["aspect"] == asp]),
                            "vs_horse_iba": best_rel([g for g, a in iba.items() if a == asp])})

    for name, rows in (("donkey40_tg_vs_iba.tsv", tg_rows), ("donkey40_protnlm_vs.tsv", pn_rows)):
        with open(os.path.join(HERE, name), "w", newline="") as fh:
            w = csv.DictWriter(fh, fieldnames=list(rows[0]), delimiter="\t", lineterminator="\n")
            w.writeheader()
            w.writerows(rows)
        print(f"wrote {name}: {len(rows)} rows")

    tgr = [r for r in tg_rows if r["kind"] != "iba_unmatched"]
    print("\nTreeGrafter rows by kind:", Counter(r["kind"] for r in tgr))
    print("Horse IBA rows:", sum(len(v) for v in horse.values()),
          " unmatched by any TreeGrafter row:", sum(r["kind"] == "iba_unmatched" for r in tg_rows))
    print("\nrelation_to_horse_iba x reviewer action (tg_solo + tg_merged):")
    for rel in ["same_term", "tg_deeper", "tg_shallower", "sibling", "tg_unmatched"]:
        rs = [r for r in tgr if r["relation_to_horse_iba"] == rel]
        if rs:
            dg = sum(r["tg_action"] in DOWNGRADE for r in rs)
            print(f"  {rel:14s} n={len(rs):3d} downgraded={dg:3d} ({100*dg/len(rs):.0f}%)  "
                  f"{dict(Counter(r['tg_action'] for r in rs))}")
    print("\nProtNLM2 assessments:", Counter(r["assessment"] for r in pn_rows))
    for col in ("vs_donkey_treegrafter", "vs_horse_iba"):
        print(f"\nProtNLM2 {col}:")
        for rel, n in Counter(r[col] for r in pn_rows).most_common():
            rs = [r for r in pn_rows if r[col] == rel]
            print(f"  {rel:18s} n={n:3d} correct={sum(r['assessment'] in CORRECT for r in rs)} "
                  f"UNC={sum(r['assessment'] == 'UNC' for r in rs)} "
                  f"wrong={sum(r['assessment'] in WRONG for r in rs)}")


if __name__ == "__main__":
    main()
