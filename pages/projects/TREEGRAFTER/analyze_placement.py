#!/usr/bin/env python3
"""Join failing TreeGrafter annotations to their PANTHER tree placement.

The question this answers: *when a TreeGrafter (GO_REF:0000118) inference is
down-graded in review, is it because the protein was placed on the WRONG part
of the PANTHER tree, or because the placement was fine but the propagated GO
term was too general / assumed a catalysis the protein has lost?*

For every reviewed TreeGrafter annotation that was down-graded
(REMOVE / MARK_AS_OVER_ANNOTATED / MODIFY) we join three pieces of
already-recorded placement evidence — no TreeGrafter re-run needed:

  * graft node      : the PANTHER ancestral node (PTN...) the term was
                      propagated from, taken from the gene's GOA WITH/FROM.
  * PANTHER family  : PTHRxxxxx + family name, from the UniProt record
                      (DR PANTHER line).
  * PANTHER subfam  : PTHRxxxxx:SFn + subfamily name, from UniProt.

We then surface, side by side, the propagated GO term and the subfamily name so
a reader can judge placement quality. (UniProt's PANTHER subfamily assignment is
itself produced by the same PANTHER classification TreeGrafter uses, so it is a
faithful proxy for "where on the tree this protein landed".)

Output: treegrafter_placement.tsv  (one row per down-graded annotation)

Run:
  python3 projects/TREEGRAFTER/analyze_placement.py
"""
from __future__ import annotations

import csv
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
REVIEW_TSV = os.path.join(HERE, "treegrafter_review.tsv")
TREEGRAFTER_REF = "GO_REF:0000118"
DOWNGRADE = {"REMOVE", "MARK_AS_OVER_ANNOTATED", "MODIFY"}

PANTHER_FAM = re.compile(r"PANTHER;\s*(PTHR\d+);\s*([^;]+?)\s*;?\s*\d*\.?$")
PANTHER_SF = re.compile(r"PANTHER;\s*(PTHR\d+:SF\d+);\s*([^;]+?)\s*;?\s*\d*\.?$")


def gene_dir_for(review_path: str) -> str:
    return os.path.dirname(os.path.join(ROOT, review_path))


def graft_node(gene_dir: str, term_id: str) -> str:
    """PANTHER PTN node that this term was propagated from (GOA WITH/FROM)."""
    goa = _first(gene_dir, "-goa.tsv")
    if not goa:
        return ""
    with open(goa) as fh:
        for line in fh:
            cols = line.rstrip("\n").split("\t")
            if len(cols) < 11:
                continue
            if cols[4] == term_id and cols[9] == TREEGRAFTER_REF:
                m = re.search(r"(PTN\d+)", cols[10])
                return m.group(1) if m else ""
    return ""


def panther_family(gene_dir: str):
    """(family_id, family_name, subfamily_id, subfamily_name) from UniProt."""
    up = _first(gene_dir, "-uniprot.txt")
    fam = subfam = ("", "")
    if not up:
        return ("", "", "", "")
    with open(up) as fh:
        for line in fh:
            if "PANTHER;" not in line:
                continue
            msf = PANTHER_SF.search(line)
            if msf:
                subfam = (msf.group(1), msf.group(2).strip())
                continue
            mfam = PANTHER_FAM.search(line)
            if mfam:
                fam = (mfam.group(1), mfam.group(2).strip())
    return (fam[0], fam[1], subfam[0], subfam[1])


def _first(gene_dir: str, suffix: str) -> str:
    try:
        for name in os.listdir(gene_dir):
            if name.endswith(suffix):
                return os.path.join(gene_dir, name)
    except FileNotFoundError:
        pass
    return ""


def main() -> None:
    out_rows = []
    with open(REVIEW_TSV) as fh:
        for r in csv.DictReader(fh, delimiter="\t"):
            if r["action"] not in DOWNGRADE:
                continue
            gd = gene_dir_for(r["file"])
            fam_id, fam_name, sf_id, sf_name = panther_family(gd)
            out_rows.append({
                "action": r["action"],
                "gene": r["gene"],
                "taxon": r["taxon"],
                "propagated_term_id": r["term_id"],
                "propagated_term_label": r["term_label"],
                "graft_node": graft_node(gd, r["term_id"]),
                "panther_family": fam_id,
                "panther_family_name": fam_name,
                "panther_subfamily": sf_id,
                "panther_subfamily_name": sf_name,
            })

    out_rows.sort(key=lambda x: (x["action"], x["gene"], x["propagated_term_id"]))
    out = os.path.join(HERE, "treegrafter_placement.tsv")
    fields = ["action", "gene", "taxon", "propagated_term_id",
              "propagated_term_label", "graft_node", "panther_family",
              "panther_family_name", "panther_subfamily", "panther_subfamily_name"]
    with open(out, "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=fields, delimiter="\t")
        w.writeheader()
        w.writerows(out_rows)

    have_sf = sum(1 for r in out_rows if r["panther_subfamily"])
    have_node = sum(1 for r in out_rows if r["graft_node"])
    print(f"Down-graded TreeGrafter annotations: {len(out_rows)}")
    print(f"  with PANTHER subfamily recovered: {have_sf}")
    print(f"  with graft node (PTN) recovered:  {have_node}")
    print(f"Wrote {os.path.relpath(out, ROOT)}")


if __name__ == "__main__":
    main()
