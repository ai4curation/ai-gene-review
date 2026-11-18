"""Does the Aryal et al. 2014 "cytosol" HDA data set contain peroxisomal matrix markers?

GOA carries a cytosol (GO:0005829) HDA row for Arabidopsis MVD1 (O23722) and MK
(P46086) from PMID:25293756, a size-exclusion proteomics study of the crude
cytosolic (soluble, post-microsomal) fraction of leaf homogenates.  A soluble
fraction prepared without peroxisome-marker controls will also contain matrix
proteins released from peroxisomes broken during homogenisation.  This script
asks QuickGO which gene products carry an annotation from that paper, and checks
(i) positive controls (MVD1, MK, which GOA shows are annotated from it) and
(ii) classical peroxisomal matrix enzymes of Arabidopsis leaves, resolved from
their AGI locus codes through UniProt at run time.

Usage:
    python cytosolic_fraction_markers.py > RESULTS-raw.txt
"""

from __future__ import annotations

import json
import sys
import urllib.parse
import urllib.request

REFERENCE = "PMID:25293756"

POSITIVE_CONTROLS = {"MVD1": "At2g38700", "MK": "At5g27450"}
PEROXISOMAL_MARKERS = {
    "CAT1 catalase": "At1g20630",
    "CAT2 catalase": "At4g35090",
    "CAT3 catalase": "At1g20620",
    "GLO1 glycolate oxidase": "At3g14420",
    "HPR hydroxypyruvate reductase": "At1g68010",
    "PMDH2 peroxisomal malate dehydrogenase": "At5g09660",
    "PED1/KAT2 3-ketoacyl-CoA thiolase": "At2g33150",
    "MLS malate synthase": "At5g03860",
    "ICL isocitrate lyase": "At3g21720",
}
OTHER_QUERIES = {"PMK": "At1g31910", "MVD2": "At3g54250"}


def get_json(url: str) -> dict:
    req = urllib.request.Request(url, headers={"Accept": "application/json"})
    with urllib.request.urlopen(req, timeout=120) as handle:
        return json.load(handle)


def reviewed_accession(locus: str) -> str | None:
    query = urllib.parse.quote(f"gene:{locus} AND organism_id:3702 AND reviewed:true")
    url = f"https://rest.uniprot.org/uniprotkb/search?query={query}&fields=accession&format=json"
    results = get_json(url).get("results", [])
    return results[0]["primaryAccession"] if results else None


def annotated_products() -> dict[str, set[str]]:
    products: dict[str, set[str]] = {}
    page = 1
    while True:
        url = ("https://www.ebi.ac.uk/QuickGO/services/annotation/search?"
               f"reference={REFERENCE}&limit=200&page={page}")
        data = get_json(url)
        for row in data["results"]:
            acc = row["geneProductId"].split(":", 1)[1]
            products.setdefault(acc, set()).add(f"{row['goId']} {row['goEvidence']}")
        if page >= data["pageInfo"]["total"]:
            break
        page += 1
    return products


def report(label: str, locus: str, products: dict[str, set[str]]) -> None:
    acc = reviewed_accession(locus)
    if acc is None:
        print(f"| {label} | {locus} | not resolved | - |")
        return
    found = products.get(acc)
    print(f"| {label} | {locus} | {acc} | {', '.join(sorted(found)) if found else 'absent'} |")


def main() -> int:
    products = annotated_products()
    terms: dict[str, int] = {}
    for annots in products.values():
        for a in annots:
            terms[a] = terms.get(a, 0) + 1
    print(f"# Gene products annotated from {REFERENCE}\n")
    print(f"- distinct gene products: {len(products)}")
    print(f"- term/evidence combinations: {terms}\n")
    print("| protein | AGI | UniProt | annotation from this paper |")
    print("|---|---|---|---|")
    for group in (POSITIVE_CONTROLS, PEROXISOMAL_MARKERS, OTHER_QUERIES):
        for label, locus in group.items():
            report(label, locus, products)
    return 0


if __name__ == "__main__":
    sys.exit(main())
