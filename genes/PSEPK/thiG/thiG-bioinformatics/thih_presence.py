"""Count ThiH (2-iminoacetate synthase), ThiO (glycine oxidase) and ThiF entries in the
proteomes of P. putida KT2440 (taxon 160488), B. subtilis 168 (224308) and E. coli K-12
(83333) using UniProt REST queries. Prints the query and the accessions returned.

Usage: python thih_presence.py > thih_presence.out
"""
import urllib.parse
import urllib.request

ORGS = {"P. putida KT2440": 160488, "B. subtilis 168": 224308, "E. coli K-12": 83333}
QUERIES = {
    "ThiH": "(gene_exact:thiH OR ec:4.1.99.19 OR xref:interpro-IPR012726)",
    "ThiO": "(gene_exact:thiO OR ec:1.4.3.19)",
    "ThiF": "(gene_exact:thiF OR ec:2.7.7.73)",
}


def run(q):
    url = ("https://rest.uniprot.org/uniprotkb/search?format=tsv&fields=accession,gene_names&query="
           + urllib.parse.quote(q))
    with urllib.request.urlopen(url, timeout=120) as r:
        rows = r.read().decode().strip().splitlines()[1:]
    return rows


for org, tax in ORGS.items():
    for name, q in QUERIES.items():
        full = f"organism_id:{tax} AND {q}"
        rows = run(full)
        print(f"{org}\t{name}\t{len(rows)} entries\t{'; '.join(rows)}")
