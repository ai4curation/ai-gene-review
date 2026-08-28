#!/usr/bin/env python3
"""Approximate training-set overlap check for the ARGO-ProtNLM-50 queries.

ProTrek's pretraining pairs come from (a) SwissProt and (b) TrEMBL50 -- TrEMBL
clustered at 50% identity, keeping only the cluster *representative*. So a
TrEMBL query protein is a plausible training member only if it is the
representative of its UniRef50 cluster. This script asks UniProt's UniRef API
for each query's UniRef50 cluster and records whether the query is that
cluster's representative, plus whether it is a reviewed (SwissProt) entry.

This is an approximation: it uses the current UniRef50 release, not the one
ProTrek was built from, and cluster representatives can change between releases.
Treat a "representative" call as "plausibly in training", not proof.

Usage:
  uv run python projects/PROTREK_EVALUATION/check_training_overlap.py \
      --queries projects/PROTREK_EVALUATION/argo50_sequences.tsv \
      --out projects/PROTREK_EVALUATION/argo50_training_overlap.csv
"""
from __future__ import annotations

import argparse
import csv
import json
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path

UNIREF = "https://rest.uniprot.org/uniref/search"
UNIPROT = "https://rest.uniprot.org/uniprotkb/search"


def get_json(url: str, params: dict, retries: int = 4) -> dict:
    query = f"{url}?{urllib.parse.urlencode(params)}"
    for attempt in range(retries):
        try:
            with urllib.request.urlopen(query, timeout=60) as fh:
                return json.loads(fh.read().decode())
        except Exception as exc:  # noqa: BLE001 - network flakiness is expected
            if attempt == retries - 1:
                raise
            print(f"  retry {attempt + 1} after {exc}", file=sys.stderr)
            time.sleep(2 ** attempt)
    return {}


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--queries", required=True, type=Path)
    ap.add_argument("--out", required=True, type=Path)
    args = ap.parse_args()

    rows = list(csv.DictReader(args.queries.open(), delimiter="\t"))
    out = []
    for i, r in enumerate(rows, 1):
        acc = r["accession"]
        res = get_json(UNIREF, {"query": f"uniprot_id:{acc} AND identity:0.5",
                                "fields": "id,name,count,types", "format": "json"})
        clusters = res.get("results", [])
        cluster_id = rep = ""
        n_members = 0
        if clusters:
            c = clusters[0]
            cluster_id = c.get("id", "")
            n_members = c.get("memberCount", 0)
            members = c.get("members") or []
            # UniRef ids are UniRef50_<representative accession>
            rep = cluster_id.split("_", 1)[1] if "_" in cluster_id else ""
            if rep not in members and members:
                rep = members[0]

        rev = get_json(UNIPROT, {"query": f"accession:{acc}", "fields": "reviewed", "format": "json"})
        reviewed = ""
        if rev.get("results"):
            reviewed = str(rev["results"][0].get("entryType", ""))

        out.append({
            "accession": acc,
            "uniref50_cluster": cluster_id,
            "uniref50_representative": rep,
            "is_uniref50_representative": str(rep == acc),
            "uniref50_member_count": n_members,
            "uniprot_entry_type": reviewed,
        })
        print(f"[{i}/{len(rows)}] {acc} rep={rep} ({'SELF' if rep == acc else 'other'})", file=sys.stderr)

    with args.out.open("w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(out[0].keys()))
        w.writeheader()
        w.writerows(out)
    n_rep = sum(1 for r in out if r["is_uniref50_representative"] == "True")
    print(f"wrote {args.out}: {n_rep}/{len(out)} queries are their UniRef50 cluster representative")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
