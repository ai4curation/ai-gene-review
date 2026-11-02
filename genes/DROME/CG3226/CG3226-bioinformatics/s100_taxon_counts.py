"""Count UniProt proteins matching the S100 Pfam domain (PF01023) per taxon via the InterPro REST API.

Usage: python s100_taxon_counts.py > s100_taxon_counts.tsv
Empty response (HTTP 204) from the API means zero matching proteins in that taxon.
"""
import json
import urllib.request

TAXA = {
    "7227": "Drosophila melanogaster",
    "50557": "Insecta",
    "6656": "Arthropoda",
    "6231": "Nematoda",
    "6447": "Mollusca",
    "7586": "Echinodermata",
    "7711": "Chordata",
    "7712": "Tunicata",
    "7735": "Cephalochordata",
    "7742": "Vertebrata",
    "33208": "Metazoa",
}
ACC = "PF01023"


def count(taxid: str):
    url = (f"https://www.ebi.ac.uk/interpro/api/protein/UniProt/entry/pfam/{ACC}/"
           f"taxonomy/uniprot/{taxid}/?page_size=1")
    with urllib.request.urlopen(url, timeout=60) as r:
        body = r.read()
        if r.status == 204 or not body:
            return 0
        return json.loads(body)["count"]


if __name__ == "__main__":
    print("taxid\ttaxon\tPF01023_protein_count")
    for t, name in TAXA.items():
        try:
            c = count(t)
        except Exception as e:  # report, do not invent
            c = f"ERROR:{e}"
        print(f"{t}\t{name}\t{c}")
