"""Inventory SynGO-assigned GO annotations in this repository and how reviews judged them.

Reads every committed ``genes/<org>/<GENE>/<GENE>-goa.tsv``, keeps rows whose
ASSIGNED BY is SynGO, and joins each row to the matching
``existing_annotations`` entry of the gene's review (same GO term, evidence
code, reference and negation) to pick up the review actions.

Two units are counted. A *row* is one GOA line (deduplicated on term,
qualifier, evidence code and reference). A *claim* is one gene + term +
reference: SynGO usually files a single assertion as an IDA + IMP (+ NAS)
set on the same paper, so several rows make one claim.

Writes ``data/syngo_rows.yaml`` (one record per SynGO row) and prints a summary.
Deterministic: rows are sorted, and nothing is fetched from the network.
Paths are resolved from this file, so it can be run from any directory:

    python projects/SYNGO_PROVENANCE/syngo_inventory.py
"""
from __future__ import annotations

import collections
import csv
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "projects/SYNGO_PROVENANCE/data/syngo_rows.yaml"
COLUMNS = ("ASSIGNED BY", "GO TERM", "GO NAME", "GO EVIDENCE CODE", "REFERENCE", "TAXON ID", "QUALIFIER")
csv.field_size_limit(10**8)


def review_index(review_path: Path) -> dict:
    """Map (term, evidence, reference, negated) -> list of review actions."""
    idx: dict = collections.defaultdict(list)
    if not review_path.exists():
        return idx
    try:
        with review_path.open() as fh:
            doc = yaml.load(fh, Loader=getattr(yaml, "CSafeLoader", yaml.SafeLoader)) or {}
    except yaml.YAMLError:
        return idx
    for ann in doc.get("existing_annotations") or []:
        key = (ann["term"]["id"], ann.get("evidence_type"), ann.get("original_reference_id"),
               bool(ann.get("negated")))
        idx[key].append((ann.get("review") or {}).get("action"))
    return idx


def main() -> None:
    goa_files = sorted((ROOT / "genes").glob("*/*/*-goa.tsv"))
    if not goa_files:
        sys.exit(f"no GOA files found under {ROOT / 'genes'}")
    records = []
    for goa in goa_files:
        with goa.open() as fh:
            rows = list(csv.reader(fh, delimiter="\t"))
        if not rows or "ASSIGNED BY" not in rows[0]:
            continue
        col = {name: (rows[0].index(name) if name in rows[0] else None) for name in COLUMNS}

        def get(r, name):
            i = col[name]
            return r[i] if i is not None and i < len(r) else None

        syngo = [r for r in rows[1:] if get(r, "ASSIGNED BY") == "SynGO"]
        if not syngo:
            continue
        org, gene = goa.parent.parent.name, goa.parent.name
        idx = review_index(goa.with_name(goa.name.replace("-goa.tsv", "-ai-review.yaml")))
        seen = set()
        for r in syngo:
            term, code, ref, qual = get(r, "GO TERM"), get(r, "GO EVIDENCE CODE"), get(r, "REFERENCE"), get(r, "QUALIFIER")
            if not (term and code and ref):
                continue
            key = (term, qual, code, ref)
            if key in seen:  # GOA repeats rows that differ only in extensions or date
                continue
            seen.add(key)
            negated = bool(qual and qual.startswith("NOT"))
            actions = sorted({a for a in idx.get((term, code, ref, negated), []) if a not in (None, "PENDING")})
            records.append({
                "organism_dir": org,
                "gene": gene,
                "taxon": get(r, "TAXON ID"),
                "term_id": term,
                "term_label": get(r, "GO NAME"),
                "qualifier": qual,
                "evidence": code,
                "reference": ref,
                "review_actions": actions,
            })
    records.sort(key=lambda x: (x["organism_dir"], x["gene"], x["term_id"], x["qualifier"] or "",
                                x["evidence"], x["reference"]))

    def claim(x):
        return (x["organism_dir"], x["gene"], x["term_id"], x["qualifier"], x["reference"])

    claims = {claim(x): x["taxon"] for x in records}
    human = [x for x in records if x["taxon"] == "9606"]
    actions = collections.Counter(
        x["review_actions"][0] if len(x["review_actions"]) == 1 else ("MIXED" if x["review_actions"] else "UNREVIEWED")
        for x in records)
    summary = {
        "syngo_rows": len(records),
        "distinct_claims": len(claims),
        "genes": len({(x["organism_dir"], x["gene"]) for x in records}),
        "rows_by_taxon": dict(collections.Counter(x["taxon"] for x in records).most_common()),
        "claims_by_taxon": dict(collections.Counter(claims.values()).most_common()),
        "human_rows_by_evidence": dict(collections.Counter(x["evidence"] for x in human).most_common()),
        "human_experimental_claims": len({claim(x) for x in human if x["evidence"] in ("IDA", "IMP", "EXP", "IEP")}),
        "rows_by_review_action": dict(actions.most_common()),
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    with OUT.open("w") as fh:
        yaml.safe_dump({"summary": summary, "rows": records}, fh, sort_keys=False, allow_unicode=True, width=120)
    yaml.safe_dump(summary, sys.stdout, sort_keys=False)


if __name__ == "__main__":
    main()
