#!/usr/bin/env python3
"""Test whether Pseudomonas putida KT2440 encodes an ADP-heptose 6-epimerase (HldD).

The ADP-heptose pathway terminates at ADP-D-glycero-beta-D-manno-heptose unless a
C-6 epimerase (HldD/RfaD, EC 5.1.3.20) converts it to the L,D stereoisomer. This
script asks UniProt whether KT2440 has such an enzyme, and runs the identical
queries against a positive control organism so that an empty result can be
distinguished from a broken query.

No expected accession, count or conclusion is hardcoded: the script reports
whatever UniProt returns, and writes both the per-query hit counts and the raw
rows. Interpretation is left to RESULTS.md.
"""

from __future__ import annotations

import argparse
import csv
import json
import sys
import urllib.parse
import urllib.request

API = "https://rest.uniprot.org/uniprotkb/search"

# (label, query fragment applied per-taxon)
QUERIES = [
    ("gene_name", "(gene:hldD OR gene:rfaD)"),
    ("ec_number", "ec:5.1.3.20"),
    ("name_text", "heptose-6-epimerase"),
]

# (taxon_id, description, role)
TAXA = [
    ("160488", "Pseudomonas putida KT2440", "target"),
    ("208964", "Pseudomonas aeruginosa PAO1", "positive_control"),
]

FIELDS = "accession,protein_name,gene_names"


def run_query(taxon: str, frag: str, timeout: int) -> list[dict[str, str]]:
    """Return UniProt rows for one taxon/query combination."""
    q = f"taxonomy_id:{taxon} AND {frag}"
    url = f"{API}?{urllib.parse.urlencode({'query': q, 'fields': FIELDS, 'format': 'tsv'})}"
    with urllib.request.urlopen(url, timeout=timeout) as fh:
        text = fh.read().decode("utf-8")
    lines = text.splitlines()
    if not lines:
        return []
    reader = csv.DictReader(lines, delimiter="\t")
    return [dict(row) for row in reader]


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--timeout", type=int, default=60)
    ap.add_argument("--out", default="hldd_absence.tsv")
    args = ap.parse_args()

    out_rows: list[dict[str, str]] = []
    failures: list[str] = []
    for taxon, desc, role in TAXA:
        for label, frag in QUERIES:
            try:
                rows = run_query(taxon, frag, args.timeout)
            except Exception as exc:  # external service
                failures.append(f"{taxon}/{label}: {exc}")
                print(f"QUERY FAILED {desc} [{label}]: {exc}", file=sys.stderr)
                continue
            print(f"{desc} [{label}]: {len(rows)} hit(s)")
            for row in rows:
                print(f"    {row.get('Entry')}  {row.get('Gene Names')}  {row.get('Protein names')}")
            if not rows:
                # "NA" rather than empty fields: trailing empty TSV columns read as
                # trailing whitespace to tooling, and an absent hit is not a blank value.
                out_rows.append({"taxon_id": taxon, "organism": desc, "role": role,
                                 "query": label, "n_hits": "0", "accession": "NA",
                                 "gene_names": "NA", "protein_names": "NA"})
            for row in rows:
                out_rows.append({"taxon_id": taxon, "organism": desc, "role": role,
                                 "query": label, "n_hits": str(len(rows)),
                                 "accession": row.get("Entry", ""),
                                 "gene_names": row.get("Gene Names", ""),
                                 "protein_names": row.get("Protein names", "")})

    with open(args.out, "w", newline="", encoding="utf-8") as fh:
        # lineterminator="\n": csv defaults to CRLF, whose CR reads as trailing whitespace.
        w = csv.DictWriter(fh, delimiter="\t", lineterminator="\n", fieldnames=[
            "taxon_id", "organism", "role", "query", "n_hits",
            "accession", "gene_names", "protein_names"])
        w.writeheader()
        w.writerows(out_rows)
    print(f"\nwrote {args.out} ({len(out_rows)} row(s))")
    if failures:
        print("INCOMPLETE: some queries failed; results below are partial:", file=sys.stderr)
        for f in failures:
            print("  " + f, file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
