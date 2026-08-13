#!/usr/bin/env python3
"""Verify a cross-ortholog GO audit of bacterial enolase surface/secreted terms.

Context
-------
The blinded OpenScientist run on the GO:0005576 hypothesis
(`../eno-hypotheses/function-hypothesis-go-0005576/openscientist.md`) built its
headline argument on a table of enolase orthologs, claiming the extracellular /
cell-surface GO terms are *anti-correlated* with real surface biology: applied by
rule to enolases with no surface evidence, absent from enolases where surface
display is experimentally established.

That is a checkable claim about public data, so this script checks it. For each
accession it asks UniProt what the protein actually is, and asks QuickGO which of
GO:0005576 (extracellular region) and GO:0009986 (cell surface) it carries, with
evidence codes and references.

The script asserts no conclusion. It prints what the APIs return; read the output.

Reproduce with:
    uv run --with requests python check_ortholog_go_audit.py
"""

from __future__ import annotations

import sys

import requests

UNIPROT = "https://rest.uniprot.org/uniprotkb/{acc}.json"
QUICKGO = "https://www.ebi.ac.uk/QuickGO/services/annotation/search"
CC_TERMS = "GO:0005576,GO:0009986"

# Accessions as listed in the OpenScientist audit table, with the identity the
# report assigned to each. The point of the script is to test those assignments,
# so the labels below are the *claims*, not verified facts.
CLAIMED = [
    ("Q88MF9", "P. putida KT2440 enolase (the query)"),
    ("P0A6P9", "E. coli enolase"),
    ("P64075", "M. tuberculosis enolase"),
    ("P77972", "Bifidobacterium enolase"),
    ("P9WNV9", "M. tuberculosis enolase"),
    ("Q8DR60", "S. pneumoniae enolase"),
    ("P0A4G2", "S. aureus enolase"),
]

# The enolases of the two organisms the report said lack the terms, looked up
# independently. These are the accessions used as pathogen controls in
# check_plasminogen_motif.py, so identity is already established there.
CONTROLS = [
    ("Q97QS2", "S. pneumoniae TIGR4 enolase (control from motif analysis)"),
    ("P99088", "S. aureus N315 enolase (control from motif analysis)"),
]


def protein_identity(acc: str) -> tuple[str, str]:
    """Return (protein name, organism) as UniProt records them."""
    r = requests.get(
        UNIPROT.format(acc=acc),
        params={"fields": "protein_name,organism_name"},
        timeout=30,
    )
    r.raise_for_status()
    d = r.json()
    desc = d.get("proteinDescription", {})
    name = desc.get("recommendedName", {}).get("fullName", {}).get("value")
    if not name:
        subs = desc.get("submissionNames") or [{}]
        name = subs[0].get("fullName", {}).get("value", "?")
    return name, d.get("organism", {}).get("scientificName", "?")


def cc_annotations(acc: str) -> list[tuple[str, str, str]]:
    """Return (go_id, evidence, reference) for the two surface/secreted terms."""
    r = requests.get(
        QUICKGO,
        params={"geneProductId": f"UniProtKB:{acc}", "goId": CC_TERMS, "limit": 50},
        headers={"Accept": "application/json"},
        timeout=30,
    )
    r.raise_for_status()
    rows = r.json().get("results", [])
    seen = {(x["goId"], x["goEvidence"], x["reference"]) for x in rows}
    return sorted(seen)


def report(acc: str, claim: str) -> bool:
    """Print one accession's real identity and CC annotations.

    Returns whether the claimed identity mentions enolase and UniProt agrees.
    """
    try:
        name, org = protein_identity(acc)
        anns = cc_annotations(acc)
    except requests.RequestException as exc:  # network/API problem, not a result
        print(f"{acc}: LOOKUP FAILED ({exc})")
        return False

    claims_enolase = "enolase" in claim.lower()
    is_enolase = "enolase" in name.lower()
    flag = "" if claims_enolase == is_enolase else "   <-- IDENTITY MISMATCH"

    print(f"{acc}  claimed: {claim}{flag}")
    print(f"        actual: {name} | {org}")
    if anns:
        for go_id, ev, ref in anns:
            print(f"        {go_id}  {ev:4s}  {ref}")
    else:
        print("        no GO:0005576 / GO:0009986 annotation")
    print()
    return claims_enolase == is_enolase


def main() -> int:
    print("=" * 78)
    print("Accessions as listed in the OpenScientist cross-ortholog audit table")
    print("=" * 78)
    agree = [report(acc, claim) for acc, claim in CLAIMED]

    print("=" * 78)
    print("Enolases of the organisms the report said lack the terms")
    print("=" * 78)
    for acc, claim in CONTROLS:
        report(acc, claim)

    print("=" * 78)
    print(f"identity check: {sum(agree)}/{len(agree)} claimed identities matched UniProt")
    print("=" * 78)
    return 0


if __name__ == "__main__":
    sys.exit(main())
