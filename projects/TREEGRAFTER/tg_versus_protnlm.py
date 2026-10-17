#!/usr/bin/env python3
"""Compare reviewed TreeGrafter rows with reviewed ProtNLM2 GO predictions.

The two sets are judged on different scales: TreeGrafter rows by a gene
review action (ACCEPT ... REMOVE), ProtNLM2 predictions by the VDCL
assessment of a PredictionReview (COR/CNN/LSP correct, UNC uncertain,
NPI/PLI/REP incorrect). Only proteins carrying both can be compared directly.
Most ProtNLM cohorts are PANTHER reference genomes (HORSE, FLY, POMBE,
NEUROSPORA ...), whose proteins receive PAINT IBA rows and no TreeGrafter
rows, so the overlap is small.

For each protein with both, every (TreeGrafter row, ProtNLM prediction) pair
in the same aspect is related by GO is_a/part_of: same term, ProtNLM deeper
(descendant), ProtNLM shallower (ancestor), sibling (shared direct parent), or
unrelated. A ProtNLM prediction related to no TreeGrafter row is listed with
relation ``protnlm_only``; a TreeGrafter row related to no prediction with
``treegrafter_only``.

Output: tg_versus_protnlm.tsv next to this script, and a printed summary.

Run:
  uv run --with pyyaml projects/TREEGRAFTER/tg_versus_protnlm.py --go-obo go-basic.obo
"""
from __future__ import annotations

import argparse
import csv
import glob
import os
import sys
from collections import Counter

import yaml

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, HERE)
from propagation_rules import ancestors, load_go  # noqa: E402

ASPECT = {"GO_MF": "molecular_function", "GO_BP": "biological_process",
          "GO_CC": "cellular_component"}
CORRECT = {"COR", "CNN", "LSP"}
WRONG = {"NPI", "PLI", "REP"}


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--go-obo", required=True)
    args = ap.parse_args()
    parents, _ = load_go(args.go_obo)
    cache: dict = {}

    def anc(t):
        return ancestors(t, parents, cache)

    tg: dict = {}
    for r in csv.DictReader(open(os.path.join(HERE, "treegrafter_review.tsv")), delimiter="\t"):
        tg.setdefault(os.path.dirname(r["file"]), []).append(r)
    rows = []
    for pr in sorted(glob.glob(os.path.join(ROOT, "genes/*/*/*protnlm-predictions-review.yaml"))):
        d = os.path.relpath(os.path.dirname(pr), ROOT)
        if d not in tg:
            continue
        doc = yaml.safe_load(open(pr)) or {}
        preds = []
        for p in doc.get("predictions") or []:
            t = p.get("predicted_term") or {}
            if p.get("predicted_term_type") in ASPECT and str(t.get("id", "")).startswith("GO:"):
                preds.append({"id": t["id"], "label": t.get("label", ""),
                              "aspect": ASPECT[p["predicted_term_type"]],
                              "assessment": (p.get("review") or {}).get("assessment", "")})
        used_tg, used_p = set(), set()
        for i, t in enumerate(tg[d]):
            for j, p in enumerate(preds):
                if p["aspect"] != t["aspect"]:
                    continue
                a, b = t["term_id"], p["id"]
                if a == b:
                    rel = "same_term"
                elif a in anc(b):
                    rel = "protnlm_deeper"
                elif b in anc(a):
                    rel = "protnlm_shallower"
                elif parents.get(a, set()) & parents.get(b, set()):
                    rel = "sibling"
                else:
                    continue
                used_tg.add(i)
                used_p.add(j)
                rows.append({"protein": d.split("/", 1)[1], "relation": rel, "aspect": t["aspect"],
                             "tg_term": a, "tg_label": t["term_label"], "tg_action": t["action"],
                             "protnlm_term": b, "protnlm_label": p["label"],
                             "protnlm_assessment": p["assessment"]})
        for i, t in enumerate(tg[d]):
            if i not in used_tg:
                rows.append({"protein": d.split("/", 1)[1], "relation": "treegrafter_only",
                             "aspect": t["aspect"], "tg_term": t["term_id"], "tg_label": t["term_label"],
                             "tg_action": t["action"], "protnlm_term": "", "protnlm_label": "",
                             "protnlm_assessment": ""})
        for j, p in enumerate(preds):
            if j not in used_p:
                rows.append({"protein": d.split("/", 1)[1], "relation": "protnlm_only",
                             "aspect": p["aspect"], "tg_term": "", "tg_label": "", "tg_action": "",
                             "protnlm_term": p["id"], "protnlm_label": p["label"],
                             "protnlm_assessment": p["assessment"]})
    cols = ["protein", "relation", "aspect", "tg_term", "tg_label", "tg_action",
            "protnlm_term", "protnlm_label", "protnlm_assessment"]
    out = os.path.join(HERE, "tg_versus_protnlm.tsv")
    with open(out, "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=cols, delimiter="\t", lineterminator="\n")
        w.writeheader()
        w.writerows(rows)
    print(f"wrote {out}: {len({r['protein'] for r in rows})} proteins, {len(rows)} rows")
    print(Counter(r["relation"] for r in rows))
    print("TreeGrafter actions:", Counter(r["tg_action"] for r in rows if r["tg_action"] and r["relation"] in ("treegrafter_only",)) )
    print("ProtNLM-only assessments:", Counter(r["protnlm_assessment"] for r in rows if r["relation"] == "protnlm_only"))
    # How the ProtNLM cohorts split between IBA (PANTHER reference proteomes)
    # and TreeGrafter, from each protein's own GOA file.
    pr_files = sorted(glob.glob(os.path.join(ROOT, "genes/*/*/*protnlm-predictions-review.yaml")))
    with_iba = with_tg = 0
    for pr in pr_files:
        refs = set()
        for goa in glob.glob(os.path.join(os.path.dirname(pr), "*-goa.tsv")):
            refs |= {r["REFERENCE"] for r in csv.DictReader(open(goa), delimiter="\t")}
        with_iba += "GO_REF:0000033" in refs
        with_tg += "GO_REF:0000118" in refs
    reviewed_tg = sum(os.path.relpath(os.path.dirname(pr), ROOT) in tg for pr in pr_files)
    print(f"ProtNLM prediction-review files: {len(pr_files)}; on proteins with IBA rows: {with_iba}; "
          f"with TreeGrafter rows in GOA: {with_tg}; with reviewed TreeGrafter rows in the snapshot: {reviewed_tg}")
    horse = [r for goa in glob.glob(os.path.join(ROOT, "genes/HORSE/*/*-goa.tsv"))
             for r in csv.DictReader(open(goa), delimiter="\t")]
    print(f"HORSE: {len(glob.glob(os.path.join(ROOT, 'genes/HORSE/*/')))} genes, "
          f"{sum(r['REFERENCE'] == 'GO_REF:0000033' for r in horse)} IBA rows, "
          f"{sum(r['REFERENCE'] == 'GO_REF:0000118' for r in horse)} TreeGrafter rows")
    for rel in ("same_term", "protnlm_deeper", "protnlm_shallower", "sibling", "protnlm_only"):
        rs = [r for r in rows if r["relation"] == rel]
        if rs:
            print(f"  {rel}: {len(rs)} pairs, ProtNLM correct {sum(r['protnlm_assessment'] in CORRECT for r in rs)}, "
                  f"wrong {sum(r['protnlm_assessment'] in WRONG for r in rs)}")


if __name__ == "__main__":
    main()
