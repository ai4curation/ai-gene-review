"""Which AHNAK2 papers produced GO annotations, and which produced none?

Affinage's `gates_passed` certifies precision, not recall, so the interesting
question is not "did it cite real papers" but "how much of what is published
about AHNAK2 reached GOA at all". Query QuickGO **by reference** for every paper
this review relies on and count the entities each one annotates.

Two things fall out of the same query:

* A paper with 0 annotations anywhere is a coverage gap.
* A paper that annotates the complex plus every subunit with identical evidence
  is a projection, not N independent findings (so count distinct entity ids, not
  annotations, and refuse to answer from a truncated page).

Also checks the known FGF1 nonclassical-export machinery (S100A13, SYT1, FGF1
itself) so a proposed term for AHNAK2 is the term GO already uses for that
pathway rather than one invented here.

Run: uv run python gap_by_reference.py
"""

from __future__ import annotations

import json

from uniprot import _cached_get

BASE = "https://www.ebi.ac.uk/QuickGO/services/annotation/search"

PAPERS = {
    "PMID:17185750": "AHNAK/dysferlin complex (source of every AHNAK2 NAS + IPI row)",
    "PMID:24675079": "PRX and AHNAK2 PDZ domain-swapped homodimers (PDB 4CN0)",
    "PMID:20833135": "AHNAK1 and AHNAK2 are costameric proteins",
    "PMID:15007166": "the AHNAKs are giant propeller-like proteins (AHNAK2 discovery)",
    "PMID:21940993": "self-regulated alternative splicing at the AHNAK locus",
    "PMID:25560297": "AHNAK2 in the stress-induced nonclassical FGF1 secretion pathway",
    "PMID:31011849": "AHNAK2 as a cause of autosomal recessive CMT",
    "PMID:37349884": "AHNAK2-RUVBL1 and G1/S progression",
    "PMID:38751848": "AHNAK2 stabilises c-MET in PDAC",
    "PMID:39849106": "AHNAK2 and cortactin in filopodia",
    "PMID:33363388": "AHNAK2 and TGF-beta/Smad3 EMT",
}

# The published FGF1 nonclassical-export machinery. What BP term does GO give
# these? Use it rather than inventing one for AHNAK2.
FGF1_MACHINERY = {
    "FGF1": "P05230",
    "S100A13": "Q99584",
    "SYT1": "P21579",
    "CSNK2A1": "P68400",
}
SECRETION_TERMS = {
    "GO:0009306": "protein secretion",
    "GO:0050714": "positive regulation of protein secretion",
    "GO:0006887": "exocytosis",
    "GO:0140353": "lipid export from cell",
}


def qg(url: str, key: str) -> dict:
    d = json.loads(_cached_get(url, key))
    n, got = d.get("numberOfHits", 0), len(d.get("results", []))
    if n > got:
        # Do not read a page total as the whole. Say so instead of guessing.
        d["_truncated"] = True
    return d


def main() -> None:
    print("=== GO annotations produced by each AHNAK2-relevant paper ===")
    for pmid, what in PAPERS.items():
        d = qg(f"{BASE}?reference={pmid}&limit=100", f"qgref_{pmid.replace(':', '_')}")
        n = d.get("numberOfHits", 0)
        if d.get("_truncated"):
            print(f"{pmid}  {n} annotations -- entity count UNAVAILABLE (paginated); "
                  f"projection test unreliable.  [{what}]")
            continue
        ents = sorted({r["geneProductId"] for r in d["results"]})
        subj = [r for r in d["results"] if r["geneProductId"] == "UniProtKB:Q8IVF2"]
        print(f"{pmid}  {n} annotation(s) over {len(ents)} entit(y/ies); "
              f"{len(subj)} on AHNAK2.  [{what}]")
        if n and not subj:
            syms = sorted({r.get("symbol") or r["geneProductId"] for r in d["results"]})
            print(f"    annotates: {', '.join(syms)}  -- but nothing on AHNAK2")
    print()

    print("=== what GO gives the published FGF1 nonclassical-export machinery ===")
    for name, acc in FGF1_MACHINERY.items():
        for go_id, label in SECRETION_TERMS.items():
            u = (f"{BASE}?geneProductId=UniProtKB:{acc}&goId={go_id}"
                 "&goUsage=descendants&goUsageRelationships=is_a,part_of&limit=100")
            res = qg(u, f"qgsec_{acc}_{go_id.replace(':', '_')}")
            if res.get("_truncated"):
                print(f"{name:9s} {go_id}: truncated, not reported")
                continue
            hits = res["results"]
            if not hits:
                continue
            for r in hits:
                print(f"{name:9s} holds {r['goId']} ({r.get('goName') or label}) "
                      f"[{r['goEvidence']}] {r.get('qualifier')} {r.get('reference')}")
    print()


if __name__ == "__main__":
    main()
