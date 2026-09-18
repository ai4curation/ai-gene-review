#!/usr/bin/env python3
"""Record, in a committed file, every ComplexPortal complex that contains human AP5B1.

Why this exists: the AP5B1 review's cellular-component knowledge gap turns on the claim that
ComplexPortal curates the AP-5/SPG11/SPG15 hexamer as CPX-20045 while GO has no term for it,
and CPX-20045 is asserted as a machine-readable `skos:exactMatch` in the review's
`proposed_new_terms`. Unlike CPX-5181, that identifier appears in no other committed artifact,
so it was the one load-bearing id in the review with nothing behind it in the repository.
This script fetches it live and writes the evidence next to the analysis it supports.

The GO cross-reference field is the point of the exercise: if a future ComplexPortal release
adds one to CPX-20045, the ontology gap has been closed and `proposed_new_terms` should be
retired. Re-running this is how you find out.

Usage:  uv run python complexportal_provenance.py [--json complexportal.json]
"""

from __future__ import annotations

import argparse
import json
import sys

import requests

SEARCH = "https://www.ebi.ac.uk/intact/complex-ws/search/{query}?format=json"
DETAIL = "https://www.ebi.ac.uk/intact/complex-ws/complex/{ac}"

ACCESSION = "Q2VPB7"
EXPECTED_GENE = "AP5B1"
# The complex the review's proposed_new_terms points at; fetched in detail and asserted.
KEY_COMPLEX = "CPX-20045"


def search(query: str) -> list[dict]:
    r = requests.get(SEARCH.format(query=query), timeout=60)
    r.raise_for_status()
    return r.json().get("elements", [])


def detail(ac: str) -> dict:
    r = requests.get(DETAIL.format(ac=ac), timeout=60)
    r.raise_for_status()
    return r.json()


def summarise(d: dict) -> dict:
    xrefs = d.get("crossReferences", []) or []
    return {
        "name": d.get("name"),
        "participants": [
            {
                "identifier": p.get("identifier"),
                "name": p.get("name"),
                "stoichiometry": p.get("stochiometry"),
            }
            for p in d.get("participants", [])
        ],
        "go_cross_references": [
            {"id": x.get("identifier"), "description": x.get("description")}
            for x in xrefs
            if x.get("database") == "go"
        ],
        "pubmed_cross_references": [
            x.get("identifier") for x in xrefs if x.get("database") == "pubmed"
        ],
        "properties": d.get("properties"),
    }


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--json", default="complexportal.json", help="output path")
    args = ap.parse_args()

    hits = search(ACCESSION)
    assert hits, f"ComplexPortal returned no complexes for {ACCESSION}"
    report = {
        "query_accession": ACCESSION,
        "complexes_containing_this_protein": [
            {
                "complex_ac": h.get("complexAC"),
                "complex_name": h.get("complexName"),
                "organism": h.get("organismName"),
            }
            for h in hits
        ],
    }

    acs = [h.get("complexAC") for h in hits]
    assert KEY_COMPLEX in acs, (
        f"{KEY_COMPLEX} no longer lists {ACCESSION} as a participant "
        f"(got {acs}); the review's proposed_new_terms mapping needs rechecking."
    )

    report["detail"] = {}
    for ac in sorted({KEY_COMPLEX, "CPX-5181", "CPX-26503"}):
        report["detail"][ac] = summarise(detail(ac))

    key = report["detail"][KEY_COMPLEX]
    go_refs = key["go_cross_references"]

    print(f"ComplexPortal complexes containing {ACCESSION} ({EXPECTED_GENE}):")
    for c in report["complexes_containing_this_protein"]:
        print(f"  {c['complex_ac']:<12} {c['complex_name']}  [{c['organism']}]")

    print(f"\n{KEY_COMPLEX}: {key['name']}")
    for p in key["participants"]:
        print(f"  participant: {p['identifier']:<12} {p['name']}  ({p['stoichiometry']})")
    print(f"  PubMed: {', '.join(key['pubmed_cross_references']) or 'none'}")
    print(f"  GO cross-references: {go_refs if go_refs else 'NONE'}")

    for ac in ("CPX-5181", "CPX-26503"):
        print(f"\n{ac}: {report['detail'][ac]['name']}")
        print(f"  GO cross-references: "
              f"{report['detail'][ac]['go_cross_references'] or 'NONE'}")

    if go_refs:
        print(
            f"\nNOTE: {KEY_COMPLEX} now carries a GO cross-reference. If it names a class for "
            "the hexamer, the ontology gap recorded in the review has been closed and the "
            "proposed_new_terms entry should be retired."
        )
    else:
        print(
            f"\n{KEY_COMPLEX} carries no GO cross-reference: the hexamer is curated by "
            "ComplexPortal and has no GO class, which is the gap the review records."
        )

    with open(args.json, "w") as fh:
        json.dump(report, fh, indent=2)
    print(f"\nwrote {args.json}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
