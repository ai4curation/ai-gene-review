#!/usr/bin/env python3
"""Fetch the UniProt allergen registry and build a fetch worklist for ALLERGENS.

WHO/IUIS itself offers no stable API, but UniProt's ``Allergen`` keyword
(``KW-0020``) is a curated, API-accessible proxy: every reviewed allergen entry
carries the WHO/IUIS designation inline in its protein names as
``(allergen <name>)`` (e.g. ``(allergen Fel d 1-A)``, ``(allergen Hom s Trx)``).

This script (1) snapshots that registry from the live UniProt REST API into
``uniprot_allergens.tsv`` and (2) cross-references it against the genes already
present under ``genes/`` to emit ``allergen_worklist.tsv`` — the registry members
not yet fetched, each with a ready-to-run ``fetch-gene`` command.

It calls a real API (UniProt REST); it does not fabricate registry data. The
snapshot records the UniProt release it came from for provenance.

Usage:
    uv run python projects/ALLERGENS/fetch_uniprot_allergens.py
"""

from __future__ import annotations

import argparse
import csv
import re
from pathlib import Path

import requests

REPO_ROOT = Path(__file__).resolve().parents[2]
GENES_DIR = REPO_ROOT / "genes"
PROJECT_DIR = REPO_ROOT / "projects" / "ALLERGENS"
UNIPROT_SEARCH = "https://rest.uniprot.org/uniprotkb/search"
QUERY = "keyword:KW-0020 AND reviewed:true"
FIELDS = "accession,id,gene_primary,organism_name,organism_id,protein_name,xref_allergome"
ALLERGEN_NAME_RE = re.compile(r"\(allergen ([^)]+)\)")
ISOALLERGEN_RE = re.compile(r"\.\d+$")          # "Bet v 1.0101"
CHAIN_RE = re.compile(r"-[A-Za-z0-9]+$")         # "Fel d 1-A"


def molecule_of(who_iuis_name: str) -> str:
    """Reduce a WHO/IUIS designation to its molecule unit.

    ``Fel d 1-A`` / ``Fel d 1.0101`` -> ``Fel d 1``; ``Bet v 1`` is unchanged
    (the trailing number is part of the allergen name, not a chain/isoform).
    """
    name = ISOALLERGEN_RE.sub("", who_iuis_name)
    name = CHAIN_RE.sub("", name)
    return name.strip()


def fetch_registry() -> tuple[list[dict], str]:
    """Page through the UniProt allergen keyword set; return rows + release tag."""
    rows: list[dict] = []
    release = ""
    params = {"query": QUERY, "format": "tsv", "fields": FIELDS, "size": 500}
    url = UNIPROT_SEARCH
    while url:
        resp = requests.get(url, params=params, timeout=120)
        resp.raise_for_status()
        release = release or resp.headers.get("x-uniprot-release", "")
        lines = resp.text.splitlines()
        for record in csv.DictReader(lines, delimiter="\t"):
            protein_names = record.get("Protein names", "") or ""
            names = ALLERGEN_NAME_RE.findall(protein_names)
            who = names[-1] if names else ""
            entry_name = record.get("Entry Name", "")
            allergome = (record.get("Allergome", "") or "").split(";")[0]
            rows.append(
                {
                    "accession": record.get("Entry", ""),
                    "entry_name": entry_name,
                    "species_code": entry_name.split("_")[-1] if "_" in entry_name else "",
                    "gene": record.get("Gene Names (primary)", ""),
                    "organism": record.get("Organism", ""),
                    "taxon_id": record.get("Organism (ID)", ""),
                    "who_iuis_name": who,
                    "allergen_molecule": molecule_of(who) if who else "",
                    "allergome_id": allergome,
                }
            )
        # follow cursor pagination via the Link header
        url = resp.links.get("next", {}).get("url")
        params = None  # the next URL already carries query params
    rows.sort(key=lambda r: (r["organism"], r["who_iuis_name"] or r["accession"]))
    return rows, release


def local_accessions() -> set[str]:
    """Accessions already fetched into the repo (first AC of each UniProt record)."""
    accs: set[str] = set()
    for path in GENES_DIR.glob("*/*/*-uniprot.txt"):
        for line in path.read_text().splitlines():
            if line.startswith("AC "):
                accs.add(line.split()[1].rstrip(";"))
                break
    return accs


REG_FIELDS = [
    "accession", "entry_name", "species_code", "gene", "organism", "taxon_id",
    "who_iuis_name", "allergen_molecule", "allergome_id",
]
WORK_FIELDS = [
    "who_iuis_name", "allergen_molecule", "accession", "species_code", "gene",
    "organism", "taxon_id", "fetch_command",
]


def fetch_command(row: dict) -> str:
    gene = row["gene"] or row["accession"]
    code = row["species_code"] or "UNKNOWN"
    return f"uv run ai-gene-review fetch-gene {code} {gene} -u {row['accession']}"


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--registry-out", type=Path, default=PROJECT_DIR / "uniprot_allergens.tsv")
    ap.add_argument("--worklist-out", type=Path, default=PROJECT_DIR / "allergen_worklist.tsv")
    args = ap.parse_args()

    rows, release = fetch_registry()
    present = local_accessions()
    for r in rows:
        r["in_repo"] = "yes" if r["accession"] in present else "no"

    header = f"# UniProt allergen registry (keyword KW-0020, reviewed); release {release}; query: {QUERY}\n"

    with args.registry_out.open("w", newline="") as fh:
        fh.write(header)
        w = csv.DictWriter(fh, fieldnames=REG_FIELDS, delimiter="\t", extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)

    worklist = [r for r in rows if r["in_repo"] == "no"]
    for r in worklist:
        r["fetch_command"] = fetch_command(r)
    with args.worklist_out.open("w", newline="") as fh:
        fh.write(header)
        w = csv.DictWriter(fh, fieldnames=WORK_FIELDS, delimiter="\t", extrasaction="ignore")
        w.writeheader()
        w.writerows(worklist)

    n_present = sum(1 for r in rows if r["in_repo"] == "yes")
    molecules = {r["allergen_molecule"] for r in rows if r["allergen_molecule"]}
    print(f"UniProt allergen registry: {len(rows)} entries ({len(molecules)} molecules), release {release}")
    print(f"  already in repo: {n_present}")
    print(f"  worklist (not yet fetched): {len(worklist)} -> {args.worklist_out.name}")
    if n_present:
        print("  present accessions:", ", ".join(sorted(r["accession"] for r in rows if r["in_repo"] == "yes")))


if __name__ == "__main__":
    main()
