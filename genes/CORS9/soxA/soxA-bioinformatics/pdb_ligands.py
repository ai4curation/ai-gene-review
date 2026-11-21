#!/usr/bin/env python3
"""List the non-polymer ligands, per chain, in the PDB structures of
Corynebacterium sp. U-96 heterotetrameric sarcosine oxidase (SoxA chain A,
SoxB chain B, SoxG chain C, SoxD chain D), using the RCSB Data API.

Usage: python3 pdb_ligands.py [PDB_ID ...]   (default: the six UniProt-listed entries)
Prints a TSV: pdb_id, comp_id, name, auth_chains. Standard library only.
"""
import json
import sys
import urllib.request

DEFAULT = ["1VRQ", "1X31", "3AD7", "3AD8", "3AD9", "3ADA"]
API = "https://data.rcsb.org/rest/v1/core"


def get(url):
    with urllib.request.urlopen(url, timeout=60) as r:
        return json.load(r)


def main(ids):
    print("pdb_id\tcomp_id\tname\tauth_chains")
    for pdb in ids:
        entry = get(f"{API}/entry/{pdb}")
        for ent in entry["rcsb_entry_container_identifiers"].get("non_polymer_entity_ids", []):
            d = get(f"{API}/nonpolymer_entity/{pdb}/{ent}")
            comp = d["pdbx_entity_nonpoly"]["comp_id"]
            name = d["pdbx_entity_nonpoly"]["name"]
            chains = ",".join(d["rcsb_nonpolymer_entity_container_identifiers"].get("auth_asym_ids", []))
            print(f"{pdb}\t{comp}\t{name}\t{chains}")


if __name__ == "__main__":
    main(sys.argv[1:] or DEFAULT)
