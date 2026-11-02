# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""Look up PANTHER family/subfamily assignments for vas2 and its sigma-adaptin relatives.

Queries the PANTHER geneinfo service (pantherdb.org) live; nothing is hardcoded.
Run: uv run --script panther_subfamily_rereview.py
"""
import json
import urllib.request

QUERIES = {
    "284812": ["Q9P7N2"],  # S. pombe vas2/aps1
    "559292": ["P35181", "Q00381", "P47064"],  # S. cerevisiae APS1, APS2, APS3
    "9606": ["P61966", "P56377", "Q96PC3", "P53680", "Q92572", "Q9Y587"],  # human sigma adaptins
}

URL = "https://www.pantherdb.org/services/oai/pantherdb/geneinfo?geneInputList={ids}&organism={tax}"


def lookup(tax: str, ids: list[str]) -> list[tuple[str, str, str]]:
    req = urllib.request.Request(URL.format(ids=",".join(ids), tax=tax), headers={"User-Agent": "curl/8.0"})
    with urllib.request.urlopen(req, timeout=120) as r:
        data = json.load(r)["search"]
    genes = data.get("mapped_genes", {}).get("gene", [])
    genes = genes if isinstance(genes, list) else [genes]
    return [(g.get("accession", ""), g.get("sf_id", ""), g.get("sf_name", "")) for g in genes]


if __name__ == "__main__":
    print("taxon\taccession\tsubfamily\tsubfamily_name")
    for tax, ids in QUERIES.items():
        for acc, sf, name in lookup(tax, ids):
            print(f"{tax}\t{acc}\t{sf}\t{name}")
