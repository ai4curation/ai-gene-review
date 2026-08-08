#!/usr/bin/env python3
"""Fetch and cache every external record used by ``analyze.py``.

Run this to (re)build ``data/``.  ``analyze.py`` never touches the network, so the
committed ``RESULTS.md`` is reproducible from the committed ``data/`` snapshot:

    uv run python fetch_data.py     # refresh data/ from live APIs
    uv run python analyze.py        # recompute results.json + RESULTS.md

Sources
-------
UniProtKB REST      protein records (sequence, features) and the reviewed human
                    Ly-6/uPAR (LU) domain protein set (InterPro IPR016054)
InterPro REST       domain-match coordinates on P26436
QuickGO REST        molecular-function annotations, restricted to experimental
                    evidence, for each human LU-domain protein
"""

import json
import sys
import time
from pathlib import Path

import requests

DATA = Path(__file__).parent / "data"

ACRV1 = "P26436"
LU_INTERPRO = "IPR016054"  # Ly-6 antigen/uPA receptor-like

UNIPROT = "https://rest.uniprot.org/uniprotkb"
INTERPRO = "https://www.ebi.ac.uk/interpro/api"
QUICKGO = "https://www.ebi.ac.uk/QuickGO/services"

# Experimental evidence codes, as listed in the GO evidence-code documentation.
EXPERIMENTAL = ["EXP", "IDA", "IPI", "IMP", "IGI", "IEP", "HTP", "HDA", "HMP", "HGI", "HEP"]


def get(url: str, **params) -> dict:
    r = requests.get(url, params=params, headers={"Accept": "application/json"}, timeout=60)
    r.raise_for_status()
    return r.json()


def write(name: str, payload) -> None:
    DATA.mkdir(exist_ok=True)
    path = DATA / name
    path.write_text(json.dumps(payload, indent=1, sort_keys=True) + "\n")
    print(f"  wrote {path.relative_to(Path(__file__).parent)}")


def main() -> int:
    print(f"UniProt record for {ACRV1}")
    write(f"uniprot_{ACRV1}.json", get(f"{UNIPROT}/{ACRV1}.json"))

    print(f"InterPro matches on {ACRV1}")
    write(
        f"interpro_{ACRV1}.json",
        get(f"{INTERPRO}/entry/all/protein/uniprot/{ACRV1}/", page_size=100),
    )

    print(f"InterPro {LU_INTERPRO} domain boundaries + sequences, reviewed human proteins")
    lu = get(
        f"{INTERPRO}/protein/reviewed/entry/interpro/{LU_INTERPRO}/taxonomy/uniprot/9606/",
        page_size=200,
        extra_fields="sequence",
    )
    if lu.get("next"):
        raise RuntimeError("InterPro result is paginated; raise page_size")
    write("interpro_lu_domains_human.json", lu)
    print(f"  {lu['count']} entries")

    print(f"reviewed human proteins carrying {LU_INTERPRO}")
    fam = get(
        f"{UNIPROT}/search",
        query=f"xref:interpro-{LU_INTERPRO} AND organism_id:9606 AND reviewed:true",
        fields="accession,id,gene_primary,protein_name,length,ft_signal,ft_lipid,cc_subcellular_location",
        format="json",
        size=500,
    )
    write("uniprot_lu_family_human.json", fam)
    accessions = sorted(e["primaryAccession"] for e in fam["results"])
    print(f"  {len(accessions)} entries")

    print("all InterPro-member-database matches per family member (for subfamily sharing)")
    per_member = {}
    for i, acc in enumerate(accessions, 1):
        per_member[acc] = get(
            f"{INTERPRO}/entry/all/protein/uniprot/{acc}/", page_size=100
        )
        print(f"  [{i}/{len(accessions)}] {acc}: {len(per_member[acc]['results'])} matches")
        time.sleep(0.2)
    write("interpro_all_matches_lu_family_human.json", per_member)

    print("QuickGO molecular-function annotations (experimental evidence only)")
    go = {}
    for i, acc in enumerate(accessions, 1):
        go[acc] = get(
            f"{QUICKGO}/annotation/search",
            geneProductId=f"UniProtKB:{acc}",
            aspect="molecular_function",
            goEvidence=",".join(EXPERIMENTAL),
            limit=200,
        )
        print(f"  [{i}/{len(accessions)}] {acc}: {go[acc]['numberOfHits']} hits")
        time.sleep(0.2)
    write("quickgo_mf_lu_family_human.json", go)

    go_ids = sorted({r["goId"] for payload in go.values() for r in payload["results"]})
    print(f"resolving {len(go_ids)} GO term labels")
    labels = {}
    for chunk in (go_ids[i : i + 50] for i in range(0, len(go_ids), 50)):
        payload = get(f"{QUICKGO}/ontology/go/terms/{','.join(chunk)}")
        for t in payload["results"]:
            labels[t["id"]] = t["name"]
    write("go_labels.json", labels)

    print("done")
    return 0


if __name__ == "__main__":
    sys.exit(main())
