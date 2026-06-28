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
from collections import defaultdict
from pathlib import Path

import requests

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
    """IEDB antigen name -> bare allergen molecule (strip the trailing UniProt tag)."""
    return name.split(" (")[0].strip()


def fetch_taxon_antigens(taxon: str) -> list[dict]:
    params = {"source_organism_iris": f"cs.{{NCBITaxon:{taxon}}}", "select": SELECT, "limit": "500"}
    r = requests.get(IEDB_API, params=params, timeout=60)
    r.raise_for_status()
    return r.json()


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
