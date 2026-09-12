#!/usr/bin/env python3
"""Fetch domain architecture and orthology signals for a UniProt accession.

Queries public REST APIs (no API key required):
  - UniProtKB entry           -> domain cross-references, family comment, features
  - InterPro entry API        -> member-database domains mapped to the protein
  - PANTHER family (if given) -> family name

All identifiers are passed on the command line; nothing is hardcoded to a
particular gene. Results are written as JSON.

Usage:
    python analyze_domains_orthology.py ACCESSION [OUTPUT.json]
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import requests

UNIPROT = "https://rest.uniprot.org/uniprotkb/{acc}.json"
INTERPRO_PROTEIN = (
    "https://www.ebi.ac.uk/interpro/api/entry/all/protein/uniprot/{acc}/"
)
TIMEOUT = 30


def fetch_uniprot(acc: str) -> dict:
    r = requests.get(UNIPROT.format(acc=acc), timeout=TIMEOUT)
    r.raise_for_status()
    return r.json()


def fetch_interpro(acc: str) -> dict:
    r = requests.get(INTERPRO_PROTEIN.format(acc=acc), timeout=TIMEOUT)
    if r.status_code == 204:
        return {"results": []}
    r.raise_for_status()
    return r.json()


def parse_uniprot(d: dict) -> dict:
    xrefs = {}
    for x in d.get("uniProtKBCrossReferences", []):
        db = x["database"]
        if db in (
            "InterPro",
            "Pfam",
            "PANTHER",
            "SUPFAM",
            "Gene3D",
            "CDD",
            "PROSITE",
            "PRINTS",
            "OrthoDB",
            "eggNOG",
            "HOGENOM",
            "InParanoid",
        ):
            props = {p["key"]: p["value"] for p in x.get("properties", [])}
            xrefs.setdefault(db, []).append(
                {"id": x["id"], "name": props.get("EntryName", "")}
            )

    # family / similarity comment
    families = []
    for c in d.get("comments", []):
        if c.get("commentType") == "SIMILARITY":
            for t in c.get("texts", []):
                families.append(t.get("value", ""))

    # sequence features
    features = []
    for f in d.get("features", []):
        features.append(
            {
                "type": f.get("type"),
                "description": f.get("description", ""),
                "start": f.get("location", {}).get("start", {}).get("value"),
                "end": f.get("location", {}).get("end", {}).get("value"),
            }
        )

    seq = d.get("sequence", {}).get("value", "")
    return {
        "accession": d.get("primaryAccession"),
        "protein_name": d.get("proteinDescription", {})
        .get("recommendedName", {})
        .get("fullName", {})
        .get("value"),
        "length": len(seq),
        "cross_references": xrefs,
        "similarity_comments": families,
        "features": features,
    }


def parse_interpro(d: dict) -> list[dict]:
    out = []
    for r in d.get("results", []):
        meta = r.get("metadata", {})
        locations = []
        for pr in r.get("proteins", []):
            for e in pr.get("entry_protein_locations", []):
                for frag_group in e.get("fragments", []):
                    locations.append(
                        {
                            "start": frag_group.get("start"),
                            "end": frag_group.get("end"),
                        }
                    )
        out.append(
            {
                "accession": meta.get("accession"),
                "name": meta.get("name"),
                "type": meta.get("type"),
                "source_database": meta.get("source_database"),
                "locations": locations,
            }
        )
    return out


def main() -> None:
    if len(sys.argv) < 2:
        sys.exit("Usage: python analyze_domains_orthology.py ACCESSION [OUTPUT.json]")
    acc = sys.argv[1]

    up = parse_uniprot(fetch_uniprot(acc))
    interpro = parse_interpro(fetch_interpro(acc))

    result = {
        "accession": acc,
        "uniprot": up,
        "interpro_domains": interpro,
    }
    out = json.dumps(result, indent=2)
    print(out)
    if len(sys.argv) >= 3:
        Path(sys.argv[2]).write_text(out + "\n")


if __name__ == "__main__":
    main()
