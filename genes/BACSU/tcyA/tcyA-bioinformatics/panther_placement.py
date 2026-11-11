"""Report PANTHER family/subfamily and CDD placement for TcyA and relevant comparators.

Queries the UniProt REST API (live) and prints one TSV row per accession.
Usage: uv run python panther_placement.py
"""
import json
import urllib.request

ACCESSIONS = {
    "P42199": "B. subtilis TcyA (target)",
    "P42400": "B. subtilis YckB (paralog, uncharacterized)",
    "O34406": "B. subtilis TcyJ (TcyJKLMN SBP)",
    "D3VIU4": "X. nematophila D3VIU4 (benchmark relative)",
    "P0AEM9": "E. coli TcyJ/FliY cystine SBP",
    "Q5F9M1": "N. gonorrhoeae Ngo0372 cystine SBP (crystal structure)",
}


def fetch(acc: str) -> dict:
    url = f"https://rest.uniprot.org/uniprotkb/{acc}.json"
    with urllib.request.urlopen(url) as fh:
        return json.load(fh)


def xrefs(entry: dict, db: str) -> list[str]:
    return [x["id"] for x in entry.get("uniProtKBCrossReferences", []) if x["database"] == db]


print("accession\tdescription\tPANTHER\tCDD\tlength")
for acc, desc in ACCESSIONS.items():
    e = fetch(acc)
    print(
        f"{acc}\t{desc}\t{';'.join(xrefs(e, 'PANTHER'))}\t{';'.join(xrefs(e, 'CDD'))}\t{e['sequence']['length']}"
    )
