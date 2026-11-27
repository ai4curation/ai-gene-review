"""Check for the J-domain HPD tripeptide in EIP9/SDJ1 and PTHR45496 relatives.

The HPD motif in the helix II-III loop of J domains is required for stimulating
Hsp70 ATPase activity. This script fetches sequences and J-domain coordinates
from the UniProt REST API and reports whether HPD occurs inside the annotated
J domain. Usage: python jdomain_hpd_check.py
"""
import json
import re
import urllib.request

ACCESSIONS = {
    "Q9FMF3": "EIP9/SDJ1 At5g64360 (PTHR45496:SF19)",
    "Q9ZU99": "SDJ2 At2g01710 (PTHR45496:SF1)",
    "Q0WQM3": "SDJ3 At1g62970 (PTHR45496:SF10)",
    "Q9SZ59": "ADMETOS At4g11940 (PTHR45496:SF32)",
    "P08622": "E. coli DnaJ (canonical positive control)",
}


def fetch(acc: str) -> dict:
    url = f"https://rest.uniprot.org/uniprotkb/{acc}.json"
    with urllib.request.urlopen(url) as r:
        return json.load(r)


def main() -> None:
    print("accession\tdescription\tJ_domain\tJ_domain_seq\tHPD_in_J\tHPD_positions_anywhere")
    for acc, desc in ACCESSIONS.items():
        rec = fetch(acc)
        seq = rec["sequence"]["value"]
        jdoms = [
            f for f in rec.get("features", [])
            if f["type"] == "Domain" and f.get("description", "").startswith("J")
        ]
        hpd_all = [m.start() + 1 for m in re.finditer("HPD", seq)]
        if not jdoms:
            print(f"{acc}\t{desc}\tNA\tNA\tNA\t{hpd_all}")
            continue
        start = jdoms[0]["location"]["start"]["value"]
        end = jdoms[0]["location"]["end"]["value"]
        jseq = seq[start - 1:end]
        print(f"{acc}\t{desc}\t{start}-{end}\t{jseq}\t{'HPD' in jseq}\t{hpd_all}")


if __name__ == "__main__":
    main()
