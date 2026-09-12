"""Han & Kursula (PMID:24675079) solved the PDZ domains of BOTH periaxin and
AHNAK2 and reported the same intertwined, domain-swapped homodimer for each.
UniProt records it on both entries with ECO:0000269.

Does GO record it on both? Query QuickGO by reference and by gene product.

A reference-level query is the discriminator: if the paper produced GO
annotations for one protein and not the other, the gap is a coverage gap on a
specific paper, not a judgement that the AHNAK2 dimer is unsupported.

Run: uv run python gap_homodimer.py
"""

from __future__ import annotations

import json
from pathlib import Path

from uniprot import _cached_get

PAPER = "PMID:24675079"
SUBJECTS = {
    "AHNAK2": "Q8IVF2",
    "PRX": "Q9BXM0",
    "AHNAK": "Q09666",
}
DIMER_TERMS = {
    "GO:0042803": "protein homodimerization activity",
    "GO:0046982": "protein heterodimerization activity",
    "GO:0051260": "protein homooligomerization",
}


def qg(url: str, key: str) -> dict:
    d = json.loads(_cached_get(url, key))
    if d.get("numberOfHits", 0) > len(d.get("results", [])):
        raise SystemExit(f"truncated QuickGO result for {key}: "
                         f"{d['numberOfHits']} hits, {len(d['results'])} read")
    return d


def main() -> None:
    base = "https://www.ebi.ac.uk/QuickGO/services/annotation/search"

    d = qg(f"{base}?reference={PAPER}&limit=100", "qg_ref_24675079")
    print(f"{PAPER} -> {d['numberOfHits']} GO annotation(s) in all of GOA")
    entities = sorted({r["geneProductId"] for r in d["results"]})
    print(f"  entities annotated: {len(entities)}")
    for r in d["results"]:
        print(f"    {r['geneProductId']:22s} {r.get('symbol'):8s} {r['goId']} "
              f"{r['goEvidence']:5s} {r.get('qualifier')}")
    if not d["results"]:
        print("    (none -- the structure produced no GO annotation for any protein)")
    print()

    for name, acc in SUBJECTS.items():
        for go_id, label in DIMER_TERMS.items():
            u = (f"{base}?geneProductId=UniProtKB:{acc}&goId={go_id}"
                 "&goUsage=descendants&goUsageRelationships=is_a,part_of&limit=100")
            res = qg(u, f"qg_dim_{acc}_{go_id.replace(':', '_')}")["results"]
            if res:
                for r in res:
                    print(f"{name:7s} {go_id} {label}: {r['goEvidence']} {r.get('reference')}")
            else:
                print(f"{name:7s} {go_id} {label}: NO annotation")
    print()


if __name__ == "__main__":
    main()
