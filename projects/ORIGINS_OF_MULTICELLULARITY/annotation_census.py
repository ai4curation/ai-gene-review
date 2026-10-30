"""Census of experimental GO annotations across the holozoan tree.

Counts GOA annotations with experimental evidence (ECO:0000269 and
descendants: EXP, IDA, IPI, IMP, IGI, IEP and high-throughput variants) for
each lineage relevant to the origin of animal multicellularity, and lists the
annotated gene products for the sparsest lineages.

Usage:
    uv run python projects/ORIGINS_OF_MULTICELLULARITY/annotation_census.py \
        > projects/ORIGINS_OF_MULTICELLULARITY/annotation_census.tsv

Results are whatever QuickGO returns on the day it is run; nothing is
hardcoded.
"""

import json
import sys
import urllib.parse
import urllib.request

QUICKGO = "https://www.ebi.ac.uk/QuickGO/services/annotation/search"
EXPERIMENTAL_ECO = "ECO:0000269"

# (NCBI taxon id, lineage label, list individual rows?)
LINEAGES = [
    (127916, "Ichthyosporea", True),
    (2687318, "Filasterea (Capsaspora)", True),
    (28009, "Choanoflagellata", True),
    (10197, "Ctenophora", True),
    (6040, "Porifera", True),
    (10226, "Placozoa", True),
    (6073, "Cnidaria", False),
    (33208, "Metazoa (all)", False),
]


def fetch(taxon: int, page: int = 1, limit: int = 100) -> dict:
    params = {
        "taxonId": taxon,
        "taxonUsage": "descendants",
        "evidenceCode": EXPERIMENTAL_ECO,
        "evidenceCodeUsage": "descendants",
        "limit": limit,
        "page": page,
    }
    url = f"{QUICKGO}?{urllib.parse.urlencode(params)}"
    req = urllib.request.Request(url, headers={"Accept": "application/json"})
    with urllib.request.urlopen(req, timeout=60) as resp:
        return json.load(resp)


def main() -> None:
    out = sys.stdout
    out.write("lineage\ttaxon\texperimental_annotations\n")
    detail = []
    for taxon, label, list_rows in LINEAGES:
        data = fetch(taxon)
        hits = data.get("numberOfHits", 0)
        out.write(f"{label}\tNCBITaxon:{taxon}\t{hits}\n")
        if list_rows and 0 < hits <= 100:
            for r in data.get("results", []):
                detail.append(
                    (label, r["geneProductId"], r.get("symbol") or "",
                     r["goId"], r["goEvidence"], r["reference"],
                     str(r["taxonId"]))
                )
    out.write("\n# rows for sparse lineages\n")
    out.write("lineage\tgene_product\tsymbol\tgo_id\tevidence\treference\ttaxon\n")
    for row in detail:
        out.write("\t".join(row) + "\n")


if __name__ == "__main__":
    main()
