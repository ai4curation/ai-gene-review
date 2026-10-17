#!/usr/bin/env python3
"""Where does TreeGrafter add something, or beat another electronic source?

For every review file that carries reviewed TreeGrafter (GO_REF:0000118) rows,
compare each TreeGrafter row with the other annotations on the same protein,
using GO is_a/part_of ancestry, and with the reviewer's action on each side:

  sole_source        TreeGrafter row with no other annotation on the protein,
                     from any source, to the same term, an ancestor or a
                     descendant: the statement exists only because TreeGrafter
                     made it.
  deeper_than        TreeGrafter term is a strict descendant of a term another
                     electronic pipeline gave the same protein (InterPro2GO
                     GO_REF:0000002, ARBA GO_REF:0000117, UniRule
                     GO_REF:0000104, EC2GO GO_REF:0000003, UniProt keyword
                     GO_REF:0000043, subcellular location GO_REF:0000044).
  shallower_than     the reverse: the other pipeline's term is the deeper one.
  conflicts_with     same aspect, neither term subsumes the other, and the two
                     terms share a direct parent (sibling calls).

Each pair keeps both reviewer actions, so the summary can say who the review
sided with. "Kept" means ACCEPT or KEEP_AS_NON_CORE; "down-graded" means
REMOVE, MODIFY, MARK_AS_OVER_ANNOTATED or TOO_GENERAL. Retired rows are skipped.

Outputs (next to this script):
  tg_versus_other_sources.tsv          one row per TreeGrafter row x relation
  tg_versus_other_sources_summary.tsv  counts per relation, source and outcome

Run:
  uv run --with pyyaml projects/TREEGRAFTER/tg_versus_other_sources.py --go-obo go-basic.obo
"""
from __future__ import annotations

import argparse
import csv
import os
import sys
from collections import Counter

import yaml

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, HERE)
from propagation_rules import ancestors, load_go  # noqa: E402

TG = "GO_REF:0000118"
PIPELINES = {
    "GO_REF:0000002": "InterPro2GO",
    "GO_REF:0000117": "ARBA",
    "GO_REF:0000104": "UniRule",
    "GO_REF:0000003": "EC2GO",
    "GO_REF:0000043": "UniProt keyword",
    "GO_REF:0000044": "UniProt subcellular location",
    "GO_REF:0000120": "combined IEA",
}
KEPT = {"ACCEPT", "KEEP_AS_NON_CORE"}
# TOO_GENERAL (true but entailed by a more specific term in the same review)
# counts as down-graded, like MODIFY: the review did not keep the term as is.
DOWN = {"REMOVE", "MODIFY", "MARK_AS_OVER_ANNOTATED", "TOO_GENERAL"}


def outcome(action: str) -> str:
    return "kept" if action in KEPT else "down-graded" if action in DOWN else "other"


def load_rows(path: str) -> list[dict]:
    doc = yaml.safe_load(open(path)) or {}
    out = []
    for a in doc.get("existing_annotations") or []:
        if a.get("retired") or a.get("negated"):
            continue
        t = (a.get("term") or {})
        if not str(t.get("id", "")).startswith("GO:"):
            continue
        out.append({"id": t["id"], "label": t.get("label", ""),
                    "ref": str(a.get("original_reference_id", "")),
                    "evidence": a.get("evidence_type", ""),
                    "action": ((a.get("review") or {}).get("action") or ""),
                    "reason": " ".join(str((a.get("review") or {}).get("reason") or "").split())[:300]})
    return out


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--go-obo", required=True)
    ap.add_argument("--review-tsv", default=os.path.join(HERE, "treegrafter_review.tsv"))
    args = ap.parse_args()
    parents, _ = load_go(args.go_obo)
    cache: dict = {}

    def anc(t):
        return ancestors(t, parents, cache)

    files = sorted({r["file"] for r in csv.DictReader(open(args.review_tsv), delimiter="\t")})
    pairs = []
    for f in files:
        rows = load_rows(os.path.join(ROOT, f))
        tg_rows = [r for r in rows if r["ref"] == TG]
        others = [r for r in rows if r["ref"] != TG]
        species = f.split("/")[1]
        gene = f.split("/")[2]
        for t in tg_rows:
            base = {"species": species, "gene": gene, "tg_term": t["id"], "tg_label": t["label"],
                    "tg_action": t["action"], "tg_reason": t["reason"], "file": f}
            related = [o for o in others
                       if o["id"] == t["id"] or o["id"] in anc(t["id"]) or t["id"] in anc(o["id"])]
            if not related:
                pairs.append({**base, "relation": "sole_source", "source": "", "other_term": "",
                              "other_label": "", "other_action": "", "other_reason": ""})
            for o in others:
                src = PIPELINES.get(o["ref"])
                if not src:
                    continue
                if o["id"] in anc(t["id"]):
                    rel = "deeper_than"
                elif t["id"] in anc(o["id"]):
                    rel = "shallower_than"
                elif (parents.get(t["id"], set()) & parents.get(o["id"], set())) and o["id"] != t["id"]:
                    rel = "conflicts_with"
                else:
                    continue
                pairs.append({**base, "relation": rel, "source": src, "other_term": o["id"],
                              "other_label": o["label"], "other_action": o["action"],
                              "other_reason": o["reason"]})

    cols = ["relation", "source", "species", "gene", "tg_term", "tg_label", "tg_action",
            "other_term", "other_label", "other_action", "tg_reason", "other_reason", "file"]
    out = os.path.join(HERE, "tg_versus_other_sources.tsv")
    with open(out, "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=cols, delimiter="\t", lineterminator="\n")
        w.writeheader()
        w.writerows(sorted(pairs, key=lambda p: (p["relation"], p["source"], p["species"],
                                                  p["gene"], p["tg_term"], p["other_term"])))
    summ = Counter()
    for p in pairs:
        key = (p["relation"], p["source"] or "-", outcome(p["tg_action"]),
               outcome(p["other_action"]) if p["source"] else "-")
        summ[key] += 1
    out_s = os.path.join(HERE, "tg_versus_other_sources_summary.tsv")
    with open(out_s, "w", newline="") as fh:
        w = csv.writer(fh, delimiter="\t", lineterminator="\n")
        w.writerow(["relation", "source", "treegrafter_outcome", "other_outcome", "pairs"])
        for k, v in sorted(summ.items()):
            w.writerow([*k, v])
    print(open(out_s).read())


if __name__ == "__main__":
    main()
