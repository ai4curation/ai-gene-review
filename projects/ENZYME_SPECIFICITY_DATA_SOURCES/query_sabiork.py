#!/usr/bin/env python3
"""Query SABIO-RK for experimental enzyme kinetic parameters (Km, kcat, ...).

SABIO-RK (https://sabiork.h-its.org) is an open curated database of reaction
kinetics. This script uses its REST `kineticlawsExportTsv` endpoint (no auth) to
pull per-substrate parameters, which are the authoritative cached evidence for
enzyme substrate specificity (kcat/Km).

Examples:
    python query_sabiork.py --ec 2.7.1.1 --organism "Homo sapiens"
    python query_sabiork.py --ec 2.7.1.1 --tsv hexokinase.tsv --summary

Notes:
    * Query syntax is SABIO-RK's: fields combine with AND, quote multi-word
      values, e.g. --organism "Homo sapiens".
    * Parameters of type Km / kcat / kcat/Km are the specificity-relevant ones;
      --summary highlights Km and kcat grouped by associated substrate species.
"""
from __future__ import annotations

import argparse
import csv
import io
import sys
from collections import defaultdict

import requests

ENDPOINT = "https://sabiork.h-its.org/sabioRestWebServices/kineticlawsExportTsv"
FIELDS = [
    "EntryID", "ECNumber", "Organism", "UniprotID", "Substrate",
    "Parameter", "PubMedID",
]


def build_query(ec: str | None, organism: str | None, uniprot: str | None) -> str:
    clauses = []
    if ec:
        clauses.append(f"ECNumber:{ec}")
    if organism:
        clauses.append(f'Organism:"{organism}"')
    if uniprot:
        clauses.append(f"UniprotID:{uniprot}")
    if not clauses:
        raise SystemExit("Provide at least one of --ec / --organism / --uniprot")
    return " AND ".join(clauses)


def fetch(query: str) -> str:
    data = [("fields[]", f) for f in FIELDS] + [("q", query)]
    resp = requests.post(ENDPOINT, data=data, timeout=60)
    if resp.status_code == 404:
        return ""  # SABIO-RK returns 404 when a query matches nothing
    resp.raise_for_status()
    return resp.text


def summarize(tsv: str) -> None:
    """Print Km and kcat grouped by associated substrate species."""
    reader = csv.DictReader(io.StringIO(tsv), delimiter="\t")
    by_param: dict[str, dict[str, list[str]]] = {
        "Km": defaultdict(list), "kcat": defaultdict(list),
    }
    for row in reader:
        ptype = (row.get("parameter.type") or "").strip()
        species = (row.get("parameter.associatedSpecies") or "?").strip()
        val = (row.get("parameter.startValue") or "").strip()
        unit = (row.get("parameter.unit") or "").strip()
        if not val:
            continue
        key = "Km" if ptype.lower() == "km" else "kcat" if ptype.lower() in {"kcat", "turnover number"} else None
        if key:
            by_param[key][species].append(f"{val} {unit}".strip())

    for key in ("Km", "kcat"):
        print(f"\n## {key} by substrate species")
        if not by_param[key]:
            print("  (none found)")
            continue
        for species, vals in sorted(by_param[key].items()):
            shown = ", ".join(vals[:6]) + (" ..." if len(vals) > 6 else "")
            print(f"  {species}: n={len(vals)}  [{shown}]")


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--ec", help="EC number, e.g. 2.7.1.1")
    ap.add_argument("--organism", help='Organism name, e.g. "Homo sapiens"')
    ap.add_argument("--uniprot", help="UniProt accession")
    ap.add_argument("--tsv", help="Write raw TSV to this path")
    ap.add_argument("--summary", action="store_true",
                    help="Print Km/kcat grouped by substrate species")
    args = ap.parse_args()

    query = build_query(args.ec, args.organism, args.uniprot)
    print(f"# SABIO-RK query: {query}", file=sys.stderr)
    tsv = fetch(query)
    if not tsv.strip():
        print("No kinetic records found.", file=sys.stderr)
        return

    nrows = max(0, tsv.strip().count("\n"))
    print(f"# {nrows} parameter rows returned", file=sys.stderr)
    if args.tsv:
        with open(args.tsv, "w") as fh:
            fh.write(tsv)
        print(f"# wrote {args.tsv}", file=sys.stderr)
    if args.summary:
        summarize(tsv)
    elif not args.tsv:
        sys.stdout.write(tsv)


if __name__ == "__main__":
    main()
