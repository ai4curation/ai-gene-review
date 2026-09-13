#!/usr/bin/env python3
"""Test whether PANTHER family PTHR32288 (APOLIPOPROTEIN C-IV) is confined to Eutheria.

The four IBA rows on human APOC4 (P55056) all descend from the PAINT IBD node
PANTHER:PTN000792756, which PAINT places at taxon:9347 (Eutheria). If the family
itself is Eutheria-restricted, every extant member is inside the inheriting clade
by construction, and the node placement cannot be over-reaching taxonomically.

This script fetches the family's member list live from the InterPro API, resolves
each distinct source organism's lineage from the UniProt taxonomy REST service,
and reports how many members fall inside / outside NCBI taxon 9347.

Run: uv run python family_taxonomy.py
"""
import json
import sys
import time
import urllib.parse

import requests

FAMILY = "PTHR32288"
EUTHERIA = 9347
INTERPRO = "https://www.ebi.ac.uk/interpro/api"
UNIPROT_TAX = "https://rest.uniprot.org/taxonomy"

S = requests.Session()
S.headers.update({"Accept": "application/json", "User-Agent": "ai-gene-review/APOC4"})


def fetch_members(family: str) -> list[dict]:
    """Every UniProt protein InterPro assigns to the PANTHER family."""
    url = f"{INTERPRO}/protein/UniProt/entry/panther/{family}/?page_size=200"
    out: list[dict] = []
    while url:
        r = S.get(url, timeout=60)
        r.raise_for_status()
        d = r.json()
        for item in d["results"]:
            md = item["metadata"]
            out.append(
                {
                    "accession": md["accession"],
                    "name": md.get("name"),
                    "source_organism": md["source_organism"],
                    "length": md.get("length"),
                }
            )
        url = d.get("next")
        if url:
            time.sleep(0.3)
    return out


def lineage(taxid: int) -> list[int]:
    r = S.get(f"{UNIPROT_TAX}/{taxid}.json", timeout=60)
    r.raise_for_status()
    d = r.json()
    ids = [int(l["taxonId"]) for l in d.get("lineage", [])]
    return [int(d["taxonId"])] + ids


def main() -> int:
    members = fetch_members(FAMILY)
    assert members, "InterPro returned no members for " + FAMILY
    print(f"PANTHER {FAMILY}: {len(members)} UniProt members returned by InterPro")

    lengths = [m["length"] for m in members if m["length"]]
    assert lengths, "no sequence lengths returned"
    print(f"  member length: min={min(lengths)} median={sorted(lengths)[len(lengths)//2]} max={max(lengths)}")

    taxa: dict[int, str] = {}
    for m in members:
        so = m["source_organism"]
        taxa[int(so["taxId"])] = so.get("scientificName") or so.get("fullName") or "?"
    print(f"  distinct source organisms: {len(taxa)}")

    inside, outside = [], []
    for tid, nm in sorted(taxa.items()):
        ln = lineage(tid)
        (inside if EUTHERIA in ln else outside).append((tid, nm, ln[:6]))
        time.sleep(0.1)

    print(f"\nEutheria (taxon {EUTHERIA}) membership of the family's source organisms:")
    print(f"  inside  Eutheria: {len(inside)} organisms")
    print(f"  outside Eutheria: {len(outside)} organisms")
    for tid, nm, ln in outside:
        print(f"    OUTSIDE: {tid} {nm}  lineage_head={ln}")

    n_in = sum(1 for m in members if EUTHERIA in lineage_cache.setdefault(
        int(m["source_organism"]["taxId"]),
        lineage(int(m["source_organism"]["taxId"]))))
    print(f"\n  family members whose organism is inside Eutheria: {n_in}/{len(members)}")

    outside_ids = {t for t, _, _ in outside}
    outside_members = [
        m for m in members if int(m["source_organism"]["taxId"]) in outside_ids
    ]
    print("\n  the non-Eutherian members themselves:")
    for m in outside_members:
        so = m["source_organism"]
        print(f"    {m['accession']:12} len={m['length']:>4}  {so['scientificName']}  name={m['name']}")

    with open("family_members.tsv", "w") as fh:
        fh.write("accession\tlength\ttaxid\torganism\tname\tin_eutheria\n")
        for m in members:
            so = m["source_organism"]
            tid = int(so["taxId"])
            fh.write(
                f"{m['accession']}\t{m['length']}\t{tid}\t{so['scientificName']}\t"
                f"{m['name']}\t{EUTHERIA in lineage_cache[tid]}\n"
            )

    result = {
        "family": FAMILY,
        "n_members": len(members),
        "n_organisms": len(taxa),
        "n_organisms_in_eutheria": len(inside),
        "organisms_outside_eutheria": [
            {"taxid": t, "name": n} for t, n, _ in outside
        ],
        "n_members_in_eutheria": n_in,
        "members_outside_eutheria": [
            {
                "accession": m["accession"],
                "length": m["length"],
                "organism": m["source_organism"]["scientificName"],
                "name": m["name"],
            }
            for m in outside_members
        ],
        "length_min": min(lengths),
        "length_max": max(lengths),
    }
    with open("family_taxonomy_result.json", "w") as fh:
        json.dump(result, fh, indent=2)
    print("\nwrote family_taxonomy_result.json")
    return 0


lineage_cache: dict[int, list[int]] = {}

if __name__ == "__main__":
    sys.exit(main())
