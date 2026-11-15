"""Inventory SynGO-assigned GO annotations in this repository and how reviews judged them.

Reads every committed ``genes/<org>/<GENE>/<GENE>-goa.tsv``, keeps rows whose
ASSIGNED BY is SynGO, and joins each row to the matching
``existing_annotations`` entry of the gene's review (same GO term, evidence
code and reference) to pick up the review action.

Writes ``data/syngo_rows.yaml`` (one record per SynGO row) and prints a summary.
Deterministic: rows are sorted, and nothing is fetched from the network.

Run from the repository root:

    python projects/SYNGO_PROVENANCE/syngo_inventory.py
"""
from __future__ import annotations

import collections
import csv
import glob
import os
import sys

import yaml

OUT = "projects/SYNGO_PROVENANCE/data/syngo_rows.yaml"
csv.field_size_limit(10**8)


def review_index(review_path: str) -> dict:
    """Map (term, evidence, reference) -> list of review actions."""
    idx: dict = collections.defaultdict(list)
    if not os.path.exists(review_path):
        return idx
    try:
        doc = yaml.safe_load(open(review_path)) or {}
    except yaml.YAMLError:
        return idx
    for ann in doc.get("existing_annotations") or []:
        key = (ann["term"]["id"], ann.get("evidence_type"), ann.get("original_reference_id"))
        idx[key].append(((ann.get("review") or {}).get("action")))
    return idx


def main() -> None:
    records = []
    for goa in sorted(glob.glob("genes/*/*/*-goa.tsv")):
        with open(goa) as fh:
            rows = list(csv.reader(fh, delimiter="\t"))
        if not rows or "ASSIGNED BY" not in rows[0]:
            continue
        h = rows[0]
        col = {name: (h.index(name) if name in h else None)
               for name in ("ASSIGNED BY", "GO TERM", "GO NAME", "GO EVIDENCE CODE", "REFERENCE", "TAXON ID", "QUALIFIER")}
        get = lambda r, name: r[col[name]] if col[name] is not None and col[name] < len(r) else None
        org, gene = goa.split("/")[1], goa.split("/")[2]
        idx = review_index(goa.replace("-goa.tsv", "-ai-review.yaml"))
        seen = set()
        for r in rows[1:]:
            if len(r) <= col["ASSIGNED BY"] or r[col["ASSIGNED BY"]] != "SynGO":
                continue
            key = (r[col["GO TERM"]], r[col["GO EVIDENCE CODE"]], r[col["REFERENCE"]])
            if key in seen:  # GOA repeats rows that differ only in extensions or date
                continue
            seen.add(key)
            actions = [a for a in idx.get(key, []) if a not in (None, "PENDING")]
            records.append({
                "organism_dir": org,
                "gene": gene,
                "taxon": get(r, "TAXON ID"),
                "term_id": key[0],
                "term_label": get(r, "GO NAME"),
                "qualifier": get(r, "QUALIFIER"),
                "evidence": key[1],
                "reference": key[2],
                "review_action": actions[0] if len(set(actions)) == 1 else (sorted(set(actions)) or None),
            })
    records.sort(key=lambda x: (x["organism_dir"], x["gene"], x["term_id"], x["evidence"], x["reference"]))

    taxa = collections.Counter(x["taxon"] for x in records)
    reviewed = [x for x in records if x["review_action"]]
    actions = collections.Counter(
        x["review_action"] if isinstance(x["review_action"], str) else "MIXED" for x in reviewed)
    human_codes = collections.Counter(x["evidence"] for x in records if x["taxon"] == "9606")
    summary = {
        "syngo_rows": len(records),
        "genes": len({(x["organism_dir"], x["gene"]) for x in records}),
        "rows_by_taxon": dict(taxa.most_common()),
        "human_rows_by_evidence": dict(human_codes.most_common()),
        "reviewed_rows": len(reviewed),
        "reviewed_rows_by_action": dict(actions.most_common()),
    }
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w") as fh:
        yaml.safe_dump({"summary": summary, "rows": records}, fh, sort_keys=False, allow_unicode=True, width=120)
    yaml.safe_dump(summary, sys.stdout, sort_keys=False)


if __name__ == "__main__":
    main()
