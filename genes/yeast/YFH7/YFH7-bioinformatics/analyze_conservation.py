#!/usr/bin/env python3
"""Assess orthology/conservation of a UniProt protein via UniRef clusters.

Strategy (all public, stable REST APIs; no key needed):
  1. Look up the UniRef50 and UniRef90 clusters containing the accession.
  2. Enumerate cluster members and their source organisms.
  3. Summarise the taxonomic span (how many species, which kingdoms/phyla) to
     judge whether the protein is lineage-restricted or broadly conserved.

Nothing is hardcoded to a particular gene; the accession is a CLI argument.

Usage:
    python analyze_conservation.py ACCESSION [OUTPUT.json]
"""
from __future__ import annotations

import json
import sys

from pathlib import Path

import requests

TIMEOUT = 40
SEARCH = "https://rest.uniprot.org/uniref/search"


def get_cluster(acc: str, identity: str) -> dict:
    """identity in {'1.0','0.9','0.5'} -> UniRef100/90/50."""
    params = {
        "query": f"(uniprot_id:{acc}) AND (identity:{identity})",
        "fields": "id,name,count,members,organism,common_taxon",
        "format": "json",
        "size": "1",
    }
    r = requests.get(SEARCH, params=params, timeout=TIMEOUT)
    r.raise_for_status()
    results = r.json().get("results", [])
    return results[0] if results else {}


def summarise_members(cluster: dict) -> dict:
    # UniRef search returns `members` as accession strings and organism names in
    # a parallel `organisms` list; representativeMember carries its own organism.
    organisms = []
    for o in cluster.get("organisms", []):
        if isinstance(o, dict):
            organisms.append(o.get("scientificName", ""))
        elif isinstance(o, str):
            organisms.append(o)
    rep = cluster.get("representativeMember", {})
    rep_org = rep.get("organismName", "") if isinstance(rep, dict) else ""
    if rep_org:
        organisms.append(rep_org)
    organisms = [o for o in organisms if o]
    return {
        "cluster_id": cluster.get("id"),
        "cluster_name": cluster.get("name"),
        "member_count": cluster.get("memberCount") or cluster.get("count"),
        "common_taxon": (cluster.get("commonTaxon") or {}).get("scientificName"),
        "common_taxon_id": (cluster.get("commonTaxon") or {}).get("taxonId"),
        "distinct_organisms_in_listing": len(set(organisms)),
        "organisms_sample": sorted(set(organisms))[:60],
    }


def main() -> None:
    if len(sys.argv) < 2:
        sys.exit("Usage: python analyze_conservation.py ACCESSION [OUTPUT.json]")
    acc = sys.argv[1]

    result = {"accession": acc, "clusters": {}}
    for label, ident in [("UniRef50", "0.5"), ("UniRef90", "0.9")]:
        cluster = get_cluster(acc, ident)
        if cluster:
            result["clusters"][label] = summarise_members(cluster)
        else:
            result["clusters"][label] = {"error": "no cluster found"}

    out = json.dumps(result, indent=2)
    print(out)
    if len(sys.argv) >= 3:
        Path(sys.argv[2]).write_text(out + "\n")


if __name__ == "__main__":
    main()
