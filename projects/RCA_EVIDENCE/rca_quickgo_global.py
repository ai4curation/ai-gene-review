"""Count RCA annotations in all of GOA (QuickGO), by assigning group, for context.

RCA maps to ECO:0000245 "automatically integrated combinatorial evidence used in manual
assertion". Some groups use a descendant (BHF-UCL uses ECO:0007666 "...computational and
experimental evidence used in manual assertion"), so counts use
evidenceCodeUsage=descendants; an exact ECO:0000245 query reports BHF-UCL as 0.

Counts are QuickGO `numberOfHits` (annotation rows) on the day the script is run; they
move with every GOA release, so projects/RCA_EVIDENCE.md quotes them with a date.

Usage:  python3 projects/RCA_EVIDENCE/rca_quickgo_global.py
"""

from __future__ import annotations

import json
import sys
import urllib.parse
import urllib.request

BASE = "https://www.ebi.ac.uk/QuickGO/services/annotation/search"
GROUPS = [
    "SGD", "BHF-UCL", "TAIR", "EcoCyc", "MGI", "FlyBase", "WB", "UniProt", "RGD",
    "ZFIN", "PomBase", "dictyBase", "CGD", "Reactome", "GO_Central", "ComplexPortal",
    "GeneDB", "AgBase", "ARUK-UCL", "AspGD",
]
ASPECTS = ["molecular_function", "biological_process", "cellular_component"]
# the references behind the RCA clusters that occur in this repo's gene corpus
REFERENCES = [
    "GO_REF:0000123",  # SGD YeastPathways -> GO
    "PMID:30358795",  # S. cerevisiae zinc proteome
    "PMID:21166475",  # Arabidopsis proteome (TAIR NOT|located_in cytosol)
    "PMID:28675934",  # matrisome proteomics, one of the BHF-UCL set
    "PMID:12819136",  # mouse/human apoptosis gene comparison (MGI)
]


def hits(**params) -> int:
    q = {"evidenceCode": "ECO:0000245", "evidenceCodeUsage": "descendants", "limit": 1}
    q.update(params)
    req = urllib.request.Request(
        f"{BASE}?{urllib.parse.urlencode(q)}", headers={"Accept": "application/json"}
    )
    with urllib.request.urlopen(req, timeout=60) as resp:
        return int(json.load(resp)["numberOfHits"])


def main() -> int:
    total = hits()
    print(f"All RCA rows in GOA: {total}")
    print("\n## by assigned_by (groups with >0)")
    accounted = 0
    for g in GROUPS:
        n = hits(assignedBy=g)
        accounted += n
        if n:
            print(f"  {n:6d}  {g}")
    print(f"  {total - accounted:6d}  (other groups not in the probe list)")
    print("\n## by aspect")
    for a in ASPECTS:
        print(f"  {hits(aspect=a):6d}  {a}")
    print("\n## by reference (clusters seen in the gene corpus)")
    for r in REFERENCES:
        print(f"  {hits(reference=r):6d}  {r}")
    print("\n## NOT-qualified rows")
    print(f"  {hits(qualifier='NOT|located_in'):6d}  NOT|located_in")
    print("\n## by ECO code")
    for eco in ["ECO:0000245", "ECO:0007666"]:
        print(f"  {hits(evidenceCode=eco, evidenceCodeUsage='exact'):6d}  {eco} (exact)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
