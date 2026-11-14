#!/usr/bin/env python3
"""Query the M-CSA (Mechanism and Catalytic Site Atlas) for catalytic mechanism.

M-CSA (https://www.ebi.ac.uk/thornton-srv/m-csa) is an EBI/Thornton-group curated
database of enzyme reaction mechanisms and catalytic residues. Its open REST API
(no auth) is the authoritative source for "which residues do the chemistry" — the
mechanism context needed to judge whether a predicted substrate could actually be
turned over (binding-pose plausibility, reaction class).

Examples:
    python query_mcsa.py --uniprot P56868
    python query_mcsa.py --ec 5.1.1.3 --json out.json

The UniProt filter is exact; the EC filter scans entries client-side (the API
returns all entries paginated). Output lists catalytic residues and the curated
reaction.
"""
from __future__ import annotations

import argparse
import json
import sys

import requests

API = "https://www.ebi.ac.uk/thornton-srv/m-csa/api/entries/"


def by_uniprot(acc: str) -> list[dict]:
    params = {
        "format": "json",
        "entries.proteins.sequences.uniprot_ids": acc,
        "page_size": 10,
    }
    r = requests.get(API, params=params, timeout=60)
    r.raise_for_status()
    return r.json().get("results", [])


def by_ec(ec: str) -> list[dict]:
    """Page through all entries and keep those whose all_ecs contains `ec`."""
    out: list[dict] = []
    url: str | None = f"{API}?format=json&page_size=100"
    while url:
        r = requests.get(url, timeout=60)
        r.raise_for_status()
        data = r.json()
        for entry in data.get("results", []):
            if ec in (entry.get("all_ecs") or []):
                out.append(entry)
        url = data.get("next")
    return out


def summarize(entry: dict) -> None:
    print(f"\n=== M-CSA {entry.get('mcsa_id')}: {entry.get('enzyme_name')} ===")
    print(f"  EC(s): {', '.join(entry.get('all_ecs') or []) or '?'}")
    print(f"  reference UniProt: {entry.get('reference_uniprot_id')}")
    desc = (entry.get("description") or "").strip().replace("\n", " ")
    if desc:
        print(f"  description: {desc[:300]}{'...' if len(desc) > 300 else ''}")
    residues = entry.get("residues") or []
    print(f"  catalytic residues: {len(residues)}")
    for res in residues[:25]:
        roles = res.get("roles_summary") or ""
        # residue identity/number lives in nested chain records; show what's present
        chains = res.get("residue_chains") or res.get("residue_sequences") or []
        label = ""
        if chains:
            c = chains[0]
            label = f"{c.get('code', '?')}{c.get('resid', c.get('auth_resid', '?'))}"
        print(f"    - {label or '(residue)'}: {roles}")


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--uniprot", help="UniProt accession (exact match)")
    ap.add_argument("--ec", help="EC number (client-side scan)")
    ap.add_argument("--json", help="Write raw JSON results to this path")
    args = ap.parse_args()

    if not (args.uniprot or args.ec):
        raise SystemExit("Provide --uniprot or --ec")

    entries = by_uniprot(args.uniprot) if args.uniprot else by_ec(args.ec)
    print(f"# {len(entries)} M-CSA entr{'y' if len(entries) == 1 else 'ies'} found",
          file=sys.stderr)
    if args.json:
        with open(args.json, "w") as fh:
            json.dump(entries, fh, indent=2)
        print(f"# wrote {args.json}", file=sys.stderr)
    for entry in entries:
        summarize(entry)


if __name__ == "__main__":
    main()
