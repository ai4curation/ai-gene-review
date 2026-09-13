"""Are AHNAK2's IntAct interactions independent experiments, or one screen?

UniProt's INTERACTION block lists 16 partners for AHNAK2, almost all `NbExp=3`.
`NbExp` counts *sub-methods*, and a single Y2H screen is routinely logged as
`two hybrid array` + `two hybrid pooling` + `validated two hybrid` -- three rows
for one experiment. Expand the records and count distinct experiments and
distinct detection methods instead.

Also records which AHNAK2 isoform each interaction was measured on: UniProt puts
most of them on an isoform accession rather than on Q8IVF2-1. Only
Q8IVF2-2 (793 aa) is genuinely short; Q8IVF2-3 is 5695 aa, lacking only the
N-terminal 100 residues and retaining the PDZ domain.

Run: uv run python intact_partners.py
"""

from __future__ import annotations

import json
from collections import Counter

from uniprot import _cached_get

ACC = "Q8IVF2"


def main() -> None:
    url = (f"https://www.ebi.ac.uk/intact/ws/interaction/findInteractions/{ACC}"
           "?page=0&pageSize=200")
    d = json.loads(_cached_get(url, f"intact_{ACC}"))
    rows = d.get("content", d if isinstance(d, list) else [])
    total = d.get("totalElements", len(rows))
    if total > len(rows):
        raise SystemExit(f"IntAct returned {len(rows)} of {total} rows -- paginate "
                         "before drawing any conclusion")
    print(f"IntAct: {len(rows)} interaction evidence record(s) for {ACC}")

    methods = Counter(r.get("detectionMethod") for r in rows)
    pubs = Counter(r.get("publicationPubmedIdentifier") for r in rows)
    types = Counter(r.get("type") for r in rows)
    hosts = Counter(r.get("hostOrganism") for r in rows)
    print(f"  distinct publications: {len(pubs)}")
    for p, n in pubs.most_common():
        print(f"    PMID:{p}: {n} record(s)")
    print(f"  detection methods: {dict(methods)}")
    print(f"  interaction types: {dict(types)}")
    print(f"  host systems: {dict(hosts)}")
    print()

    def bare(v: str) -> str:
        return v.split(" ")[0]

    # Which AHNAK2 chain was actually tested?
    isoforms: Counter[str] = Counter()
    partners: set[str] = set()
    for r in rows:
        for side in ("idA", "idB"):
            v = bare(r.get(side, ""))
            if v.split("-")[0] == ACC:
                isoforms[v] += 1
            else:
                partners.add(v)
    print(f"  AHNAK2 chain tested: {dict(isoforms)}")
    print(f"  distinct partners: {len(partners)}")
    print()

    # How many of these partners reached GOA as a GO:0005515 row on AHNAK2?
    d2 = json.loads(_cached_get(
        "https://www.ebi.ac.uk/QuickGO/services/annotation/search"
        f"?geneProductId=UniProtKB:{ACC}&goId=GO:0005515&limit=100",
        "qg_ahnak2_0005515"))
    if d2["numberOfHits"] > len(d2["results"]):
        raise SystemExit("truncated QuickGO GO:0005515 result")
    goa_partners = {
        x["id"] for r in d2["results"] for c in (r.get("withFrom") or [])
        for x in c.get("connectedXrefs", [])
    }
    print(f"  GO:0005515 rows on AHNAK2 in GOA: {d2['numberOfHits']}, "
          f"naming partners {sorted(goa_partners)}")
    print(f"  IntAct partners that reached GOA: "
          f"{sorted(goa_partners & {p.split('-')[0] for p in partners}) or 'none'}")


if __name__ == "__main__":
    main()
