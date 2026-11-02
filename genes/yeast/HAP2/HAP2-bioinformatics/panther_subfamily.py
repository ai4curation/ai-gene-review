# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""Query the PANTHER geneinfo service for the family/subfamily of HAP2 and relatives.

Usage: uv run --script panther_subfamily.py > panther_subfamily.json
Prints family_id and sf_id for each accession/taxon pair (or "unmapped").
"""
import json
import urllib.request

QUERIES = [
    ("P06774", "559292", "S. cerevisiae HAP2"),
    ("Q7SGY4", "367110", "N. crassa NCU03033"),
    ("P23511", "9606", "human NFYA"),
]

BASE = "https://www.pantherdb.org/services/oai/pantherdb/geneinfo"


def lookup(acc: str, taxon: str) -> dict:
    url = f"{BASE}?geneInputList={acc}&organism={taxon}"
    req = urllib.request.Request(url, headers={"User-Agent": "curl/8.0"})
    with urllib.request.urlopen(req, timeout=120) as r:
        data = json.load(r)
    search = data["search"]
    gene = search.get("mapped_genes", {}).get("gene")
    if gene is None:
        return {"status": "unmapped"}
    return {
        "status": "mapped",
        "panther_version": search["product"]["version"],
        "family_id": gene["family_id"],
        "sf_id": gene["sf_id"],
    }


def main() -> None:
    out = []
    for acc, taxon, label in QUERIES:
        rec = {"accession": acc, "taxon": taxon, "label": label}
        rec.update(lookup(acc, taxon))
        out.append(rec)
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
