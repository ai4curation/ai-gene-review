#!/usr/bin/env python3
"""Fetch IEDB epitope counts per allergen molecule (intervention-pressure signal).

Adds the missing axis of the ALLERGENS prioritization metric. The IEDB IQ-API
(query-api.iedb.org, PostgREST) exposes a pre-aggregated ``antigen_search`` view
(one row per source antigen, with arrays of epitope / B-cell / T-cell assay /
reference ids and antibody isotypes).

Join key caveat: IEDB keys allergens under its own UniProt accessions
(e.g. Fel d 1 = UNIPROT:A0ABI7XLA3), which differ from the Swiss-Prot accessions
this repo uses (P30438). IEDB does, however, label them by **WHO/IUIS allergen
name** ("Fel d 1"), which is exactly our ``allergen_molecule`` key. So this ETL
joins by *allergen molecule name within source taxon*, not by accession: it pulls
all antigens for each taxon present in the local index and matches rows whose name
reduces to one of our molecules.

For each allergen molecule it records distinct epitope, B-cell-assay, T-cell-assay
and reference counts and whether any IgE-isotype antibody response is recorded
(the most allergy-relevant flag). Output: ``iedb_epitopes.tsv``.

Usage:
    uv run python projects/ALLERGENS/fetch_iedb_epitopes.py
"""

from __future__ import annotations

import argparse
import csv
import re
from collections import defaultdict
from pathlib import Path

import requests

# WHO/IUIS allergen designation, e.g. "Fel d 1", "Can f 6", "Bet v 1" — possibly
# embedded in a longer IEDB name ("Major allergen Can f 1", "Lipocalin Can f 6.0101")
# and possibly carrying an isoallergen (.0101) or chain (-A) suffix to strip.
ALLERGEN_DESIGNATION = re.compile(r"\b([A-Z][a-z]{1,4} [a-z] \d+)(?:\.\d+|-[A-Za-z0-9]+)?\b")

PROJECT_DIR = Path(__file__).resolve().parent
IEDB_API = "https://query-api.iedb.org/antigen_search"
SELECT = (
    "parent_source_antigen_iri,parent_source_antigen_names,structure_ids,"
    "bcell_ids,tcell_ids,reference_ids,antibody_isotypes"
)


def molecules_by_taxon(index_path: Path) -> dict[str, set[str]]:
    """Read the local allergen index -> {taxon_id: {allergen_molecule, ...}}."""
    by_taxon: dict[str, set[str]] = defaultdict(set)
    with index_path.open() as fh:
        for row in csv.DictReader(fh, delimiter="\t"):
            mol = (row.get("allergen_molecule") or "").strip()
            taxon = (row.get("source_taxon_id") or "").strip()
            if mol and taxon:
                by_taxon[taxon].add(mol)
    return by_taxon


def reduce_name(name: str) -> str:
    """IEDB antigen name -> bare WHO/IUIS allergen molecule.

    Extracts the allergen designation (handling embedded forms such as
    "Major allergen Can f 1" and isoallergen suffixes such as "Can f 6.0101");
    falls back to stripping a trailing "(UniProt:...)" tag.
    """
    m = ALLERGEN_DESIGNATION.search(name)
    if m:
        return m.group(1)
    return name.split(" (")[0].strip()


def fetch_taxon_antigens(taxon: str) -> list[dict]:
    """All antigens for a source taxon, paginated via the Range header.

    The IEDB API rejects an ``offset`` query param, so pagination uses PostgREST
    ``Range``/``Range-Unit: items`` headers (some taxa have >1000 antigens).
    """
    page = 1000
    out: list[dict] = []
    start = 0
    params = {"source_organism_iris": f"cs.{{NCBITaxon:{taxon}}}", "select": SELECT}
    while True:
        headers = {"Range-Unit": "items", "Range": f"{start}-{start + page - 1}"}
        r = requests.get(IEDB_API, params=params, headers=headers, timeout=60)
        r.raise_for_status()
        batch = r.json()
        out.extend(batch)
        if len(batch) < page:
            break
        start += page
    return out


FIELDS = [
    "allergen_molecule", "source_taxon_id", "n_epitopes", "n_bcell_assays",
    "n_tcell_assays", "n_references", "has_ige", "iedb_antigen_iris",
]


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--index", type=Path, default=PROJECT_DIR / "allergen_index.tsv")
    ap.add_argument("--output", type=Path, default=PROJECT_DIR / "iedb_epitopes.tsv")
    args = ap.parse_args()

    wanted = molecules_by_taxon(args.index)
    rows_out: list[dict] = []
    for taxon, molecules in sorted(wanted.items()):
        try:
            antigens = fetch_taxon_antigens(taxon)
        except requests.RequestException as exc:
            print(f"  taxon {taxon}: query failed ({exc}); skipping")
            continue
        # aggregate IEDB antigen rows by reduced molecule name
        agg: dict[str, dict] = {}
        for a in antigens:
            for nm in a.get("parent_source_antigen_names") or []:
                mol = reduce_name(nm)
                if mol not in molecules:
                    continue
                d = agg.setdefault(mol, {"ep": set(), "bc": set(), "tc": set(),
                                         "ref": set(), "ige": False, "iris": set()})
                d["ep"].update(a.get("structure_ids") or [])
                d["bc"].update(a.get("bcell_ids") or [])
                d["tc"].update(a.get("tcell_ids") or [])
                d["ref"].update(a.get("reference_ids") or [])
                d["iris"].add(a.get("parent_source_antigen_iri"))
                if "IgE" in (a.get("antibody_isotypes") or []):
                    d["ige"] = True
        for mol in sorted(molecules):
            d = agg.get(mol)
            rows_out.append({
                "allergen_molecule": mol,
                "source_taxon_id": taxon,
                "n_epitopes": len(d["ep"]) if d else 0,
                "n_bcell_assays": len(d["bc"]) if d else 0,
                "n_tcell_assays": len(d["tc"]) if d else 0,
                "n_references": len(d["ref"]) if d else 0,
                "has_ige": ("yes" if d and d["ige"] else "no"),
                "iedb_antigen_iris": ";".join(sorted(i for i in d["iris"] if i)) if d else "",
            })

    rows_out.sort(key=lambda r: (-r["n_epitopes"], r["allergen_molecule"]))
    with args.output.open("w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=FIELDS, delimiter="\t")
        w.writeheader()
        w.writerows(rows_out)

    matched = [r for r in rows_out if r["n_epitopes"]]
    print(f"Wrote {len(rows_out)} molecule rows ({len(matched)} with IEDB epitopes) -> {args.output}")
    for r in matched:
        print(f"  {r['allergen_molecule']} (taxon {r['source_taxon_id']}): "
              f"{r['n_epitopes']} epitopes, IgE={r['has_ige']}, refs={r['n_references']}")


if __name__ == "__main__":
    main()
