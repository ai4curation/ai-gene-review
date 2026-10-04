"""List UniProt entries classified in PANTHER PTHR38820 (ANNEXIN-2 RECEPTOR), by organism.

Tests the claim (PMID:23640736) that the ANXA2R gene is peculiar to human:
    uv run python panther_orthologs.py
"""
import collections
import urllib.request

URL = ("https://rest.uniprot.org/uniprotkb/search?query=xref:panther-PTHR38820"
       "&fields=accession,organism_name,gene_names,length&format=tsv&size=500")


def main() -> None:
    with urllib.request.urlopen(URL) as r:
        rows = [line.split("\t") for line in r.read().decode().strip().split("\n")[1:]]
    print(f"UniProt entries in PTHR38820: {len(rows)}")
    print(f"distinct organisms: {len({row[1] for row in rows})}")
    by_org = collections.Counter(row[1] for row in rows)
    for acc, org, genes, length in rows:
        if org.startswith(("Homo sapiens", "Mus musculus", "Rattus", "Pan troglodytes", "Sus scrofa", "Loxodonta")):
            print(f"{acc}\t{org}\t{genes}\t{length}")
    print("non-mammalian organisms:", [o for o in by_org if any(k in o for k in ("Gallus", "Danio", "Xenopus", "Drosophila"))])


if __name__ == "__main__":
    main()
