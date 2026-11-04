#!/usr/bin/env python3
"""Proteome-wide inventory of bacterial microcompartment (BMC) shell proteins.

Queries the UniProt REST API for proteins carrying BMC shell signatures in the
reference proteomes of Pseudomonas putida KT2440 (UP000000556) and, as a positive
control, Escherichia coli K-12 (UP000000625). Also lists the KT2440 genes around
eutBC (PP_0538-PP_0548) to show the local eut locus.

Usage: python3 bmc_shell_inventory.py > bmc_shell_inventory.tsv
Results are printed as fetched; nothing is hard-coded.
"""
import sys
import urllib.parse
import urllib.request

API = "https://rest.uniprot.org/uniprotkb/search"
FIELDS = "accession,gene_names,protein_name,xref_pfam,xref_interpro"
PROTEOMES = {"UP000000556": "Pseudomonas putida KT2440", "UP000000625": "Escherichia coli K-12"}
# PF00936 BMC domain (hexamers: EutM/EutK/EutL/EutS/PduA/CcmK ...);
# PF03319 EutN/CcmL pentamer (vertex) domain; IPR000249 BMC domain; IPR004992 EutN/CcmL.
SIGNATURES = ["pfam-PF00936", "pfam-PF03319", "interpro-IPR000249", "interpro-IPR004992"]


def fetch(query: str) -> list[str]:
    url = API + "?" + urllib.parse.urlencode({"query": query, "format": "tsv", "fields": FIELDS, "size": 500})
    with urllib.request.urlopen(url, timeout=60) as resp:
        lines = resp.read().decode().strip().splitlines()
    return lines[1:]


def main() -> None:
    print("section\tproteome\tquery\taccession\tgene_names\tprotein_name\tpfam\tinterpro")
    for prot, label in PROTEOMES.items():
        for sig in SIGNATURES:
            q = f"proteome:{prot} AND xref:{sig}"
            rows = fetch(q)
            print(f"count\t{label}\t{q}\t{len(rows)}\t\t\t\t")
            for r in rows:
                print(f"hit\t{label}\t{q}\t{r}")
    # Local eut locus in KT2440
    for n in range(538, 549):
        locus = f"PP_{n:04d}"
        rows = fetch(f"proteome:UP000000556 AND gene:{locus}")
        for r in rows:
            print(f"locus\tPseudomonas putida KT2440\t{locus}\t{r}")
        if not rows:
            print(f"locus\tPseudomonas putida KT2440\t{locus}\tNO_ENTRY\t\t\t\t")


if __name__ == "__main__":
    sys.exit(main())
