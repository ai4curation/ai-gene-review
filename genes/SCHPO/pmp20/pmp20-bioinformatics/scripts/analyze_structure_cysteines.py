#!/usr/bin/env python3
"""Analyze cysteine geometry in AlphaFold structures."""

from __future__ import annotations

import argparse
import csv
import json
import math
from pathlib import Path
from typing import Any


def parse_pdb_cys_sg(pdb_path: Path) -> list[dict[str, Any]]:
    residues: dict[tuple[str, int], dict[str, Any]] = {}

    with pdb_path.open("r", encoding="utf-8") as handle:
        for line in handle:
            if not line.startswith("ATOM"):
                continue
            atom_name = line[12:16].strip()
            residue_name = line[17:20].strip()
            if residue_name != "CYS" or atom_name != "SG":
                continue

            chain_id = line[21].strip() or "A"
            residue_number_text = line[22:26].strip()
            if not residue_number_text:
                continue

            residue_number = int(residue_number_text)
            x_coord = float(line[30:38])
            y_coord = float(line[38:46])
            z_coord = float(line[46:54])
            b_factor = float(line[60:66])

            residues[(chain_id, residue_number)] = {
                "chain_id": chain_id,
                "residue_number": residue_number,
                "x": x_coord,
                "y": y_coord,
                "z": z_coord,
                "plddt": b_factor,
            }

    return sorted(residues.values(), key=lambda x: (x["chain_id"], x["residue_number"]))


def pairwise_distances(cysteine_atoms: list[dict[str, Any]]) -> list[dict[str, Any]]:
    distances: list[dict[str, Any]] = []
    for index, atom_a in enumerate(cysteine_atoms):
        for atom_b in cysteine_atoms[index + 1 :]:
            dx = atom_a["x"] - atom_b["x"]
            dy = atom_a["y"] - atom_b["y"]
            dz = atom_a["z"] - atom_b["z"]
            distance = math.sqrt(dx * dx + dy * dy + dz * dz)
            distances.append(
                {
                    "chain_a": atom_a["chain_id"],
                    "residue_a": atom_a["residue_number"],
                    "chain_b": atom_b["chain_id"],
                    "residue_b": atom_b["residue_number"],
                    "sg_distance_angstrom": round(distance, 3),
                }
            )
    return distances


def write_tsv(rows: list[dict[str, Any]], output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        output_path.write_text("", encoding="utf-8")
        return

    with output_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()), delimiter="\t")
        writer.writeheader()
        for row in rows:
            writer.writerow(row)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--proteins-json", required=True, type=Path)
    parser.add_argument("--manifest-json", required=True, type=Path)
    parser.add_argument("--output-dir", required=True, type=Path)
    args = parser.parse_args()

    args.output_dir.mkdir(parents=True, exist_ok=True)

    proteins = json.loads(args.proteins_json.read_text(encoding="utf-8"))
    manifest_rows = json.loads(args.manifest_json.read_text(encoding="utf-8"))
    manifest_by_protein_id = {row["protein_id"]: row for row in manifest_rows}

    residue_rows: list[dict[str, Any]] = []
    pair_rows: list[dict[str, Any]] = []
    summary_rows: list[dict[str, Any]] = []

    for protein in proteins:
        protein_id = protein["protein_id"]
        manifest = manifest_by_protein_id.get(protein_id, {})
        status = manifest.get("status", "missing")

        sequence_cys_count = len(protein.get("cysteine_positions", []))

        if status != "downloaded":
            summary_rows.append(
                {
                    "protein_id": protein_id,
                    "accession": protein.get("accession", ""),
                    "model_status": status,
                    "sequence_cys_count": sequence_cys_count,
                    "structure_cys_count": "",
                    "min_sg_distance_angstrom": "",
                    "pairs_under_6A": "",
                    "pairs_under_10A": "",
                    "error": manifest.get("error", "No model"),
                }
            )
            continue

        pdb_path = Path(manifest["local_pdb_path"])
        cysteine_atoms = parse_pdb_cys_sg(pdb_path)
        distances = pairwise_distances(cysteine_atoms)

        for atom in cysteine_atoms:
            residue_rows.append(
                {
                    "protein_id": protein_id,
                    "accession": protein.get("accession", ""),
                    "chain_id": atom["chain_id"],
                    "residue_number": atom["residue_number"],
                    "plddt": round(atom["plddt"], 2),
                    "model_path": str(pdb_path),
                }
            )

        for distance_row in distances:
            pair_rows.append(
                {
                    "protein_id": protein_id,
                    "accession": protein.get("accession", ""),
                    **distance_row,
                }
            )

        min_distance = min((entry["sg_distance_angstrom"] for entry in distances), default="")
        pairs_under_6 = sum(1 for entry in distances if entry["sg_distance_angstrom"] <= 6.0)
        pairs_under_10 = sum(1 for entry in distances if entry["sg_distance_angstrom"] <= 10.0)

        summary_rows.append(
            {
                "protein_id": protein_id,
                "accession": protein.get("accession", ""),
                "model_status": status,
                "sequence_cys_count": sequence_cys_count,
                "structure_cys_count": len(cysteine_atoms),
                "min_sg_distance_angstrom": min_distance,
                "pairs_under_6A": pairs_under_6,
                "pairs_under_10A": pairs_under_10,
                "error": "",
            }
        )

    residues_tsv = args.output_dir / "structure_cysteine_residues.tsv"
    pairs_tsv = args.output_dir / "structure_cys_pair_distances.tsv"
    summary_tsv = args.output_dir / "structure_cys_summary.tsv"
    report_json = args.output_dir / "structure_cys_report.json"

    write_tsv(residue_rows, residues_tsv)
    write_tsv(pair_rows, pairs_tsv)
    write_tsv(summary_rows, summary_tsv)

    report = {
        "residue_rows": residue_rows,
        "pair_distance_rows": pair_rows,
        "summary_rows": summary_rows,
        "residues_file": str(residues_tsv),
        "pair_distances_file": str(pairs_tsv),
        "summary_file": str(summary_tsv),
    }
    report_json.write_text(json.dumps(report, indent=2), encoding="utf-8")

    print(f"Wrote {residues_tsv}")
    print(f"Wrote {pairs_tsv}")
    print(f"Wrote {summary_tsv}")
    print(f"Wrote {report_json}")


if __name__ == "__main__":
    main()
