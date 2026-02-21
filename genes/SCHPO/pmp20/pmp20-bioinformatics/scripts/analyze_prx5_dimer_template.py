#!/usr/bin/env python3
"""Template-based dimer interface analysis for Prx5 homologs."""

from __future__ import annotations

import argparse
import csv
import json
import math
from pathlib import Path
from typing import Any
from urllib.request import Request, urlopen


def needleman_wunsch(seq_a: str, seq_b: str, match: int = 1, mismatch: int = -1, gap: int = -1) -> tuple[str, str]:
    rows = len(seq_a) + 1
    cols = len(seq_b) + 1
    score = [[0] * cols for _ in range(rows)]
    trace = [[""] * cols for _ in range(rows)]

    for i in range(1, rows):
        score[i][0] = i * gap
        trace[i][0] = "U"
    for j in range(1, cols):
        score[0][j] = j * gap
        trace[0][j] = "L"

    for i in range(1, rows):
        for j in range(1, cols):
            diag = score[i - 1][j - 1] + (match if seq_a[i - 1] == seq_b[j - 1] else mismatch)
            up = score[i - 1][j] + gap
            left = score[i][j - 1] + gap
            best = max(diag, up, left)
            score[i][j] = best
            if best == diag:
                trace[i][j] = "D"
            elif best == up:
                trace[i][j] = "U"
            else:
                trace[i][j] = "L"

    i = len(seq_a)
    j = len(seq_b)
    aln_a: list[str] = []
    aln_b: list[str] = []

    while i > 0 or j > 0:
        direction = trace[i][j] if i >= 0 and j >= 0 else ""
        if direction == "D":
            aln_a.append(seq_a[i - 1])
            aln_b.append(seq_b[j - 1])
            i -= 1
            j -= 1
        elif direction == "U":
            aln_a.append(seq_a[i - 1])
            aln_b.append("-")
            i -= 1
        else:
            aln_a.append("-")
            aln_b.append(seq_b[j - 1])
            j -= 1

    return "".join(reversed(aln_a)), "".join(reversed(aln_b))


def map_reference_position_to_query(query_aln: str, reference_aln: str, reference_position: int) -> tuple[int | None, str]:
    query_index = 0
    reference_index = 0
    for query_residue, reference_residue in zip(query_aln, reference_aln):
        if query_residue != "-":
            query_index += 1
        if reference_residue != "-":
            reference_index += 1

        if reference_residue != "-" and reference_index == reference_position:
            if query_residue == "-":
                return None, "-"
            return query_index, query_residue

    return None, "-"


def choose_resolving_positions(record: dict[str, Any]) -> list[int]:
    act_sites = set(record.get("act_site_positions", []))
    disulfid_pairs = record.get("disulfid_pairs", [])

    candidates: set[int] = set()
    for pair in disulfid_pairs:
        if len(pair) != 2:
            continue
        for position in pair:
            if position not in act_sites:
                candidates.add(position)

    if candidates:
        return sorted(candidates)

    cysteines = record.get("cysteine_positions", [])
    if not cysteines:
        return []

    if act_sites:
        peroxidatic = min(act_sites)
        downstream = [position for position in cysteines if position > peroxidatic]
        if downstream:
            return sorted(downstream)

    if len(cysteines) > 1:
        return sorted(cysteines[1:])

    return []


def download_pdb(pdb_id: str, output_path: Path) -> None:
    url = f"https://files.rcsb.org/download/{pdb_id}.pdb"
    request = Request(url, headers={"User-Agent": "pmp20-bioinformatics/0.1"})
    with urlopen(request, timeout=120) as response:
        content = response.read()
    output_path.write_bytes(content)


def parse_sg_coordinates(pdb_path: Path) -> dict[tuple[str, int], tuple[float, float, float]]:
    coords: dict[tuple[str, int], tuple[float, float, float]] = {}
    with pdb_path.open("r", encoding="utf-8") as handle:
        for line in handle:
            if not line.startswith("ATOM"):
                continue
            atom_name = line[12:16].strip()
            residue_name = line[17:20].strip()
            chain_id = line[21].strip() or "A"
            if atom_name != "SG" or residue_name != "CYS":
                continue

            residue_text = line[22:26].strip()
            if not residue_text:
                continue
            residue_number = int(residue_text)

            x_coord = float(line[30:38])
            y_coord = float(line[38:46])
            z_coord = float(line[46:54])
            coords[(chain_id, residue_number)] = (x_coord, y_coord, z_coord)

    return coords


def distance(a: tuple[float, float, float], b: tuple[float, float, float]) -> float:
    dx = a[0] - b[0]
    dy = a[1] - b[1]
    dz = a[2] - b[2]
    return math.sqrt(dx * dx + dy * dy + dz * dz)


def write_tsv(rows: list[dict[str, Any]], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        path.write_text("", encoding="utf-8")
        return

    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()), delimiter="\t")
        writer.writeheader()
        for row in rows:
            writer.writerow(row)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--proteins-json", required=True, type=Path)
    parser.add_argument("--target-id", default="pmp20_schpo")
    parser.add_argument("--template-id", default="prx5_o43099")
    parser.add_argument("--template-pdb-id", default="5J9B")
    parser.add_argument("--output-dir", required=True, type=Path)
    args = parser.parse_args()

    args.output_dir.mkdir(parents=True, exist_ok=True)
    proteins = json.loads(args.proteins_json.read_text(encoding="utf-8"))
    proteins_by_id = {protein["protein_id"]: protein for protein in proteins}

    if args.target_id not in proteins_by_id:
        raise SystemExit(f"Target protein_id not found: {args.target_id}")
    if args.template_id not in proteins_by_id:
        raise SystemExit(f"Template protein_id not found: {args.template_id}")

    target = proteins_by_id[args.target_id]
    template = proteins_by_id[args.template_id]

    template_peroxidatic_positions = template.get("act_site_positions", [])
    template_resolving_positions = choose_resolving_positions(template)

    if not template_peroxidatic_positions:
        raise SystemExit("Template has no ACT_SITE peroxidatic position")
    if not template_resolving_positions:
        raise SystemExit("Template has no candidate resolving position")

    template_cp = template_peroxidatic_positions[0]
    template_cr = template_resolving_positions[0]

    pdb_dir = args.output_dir / "pdb_templates"
    pdb_dir.mkdir(parents=True, exist_ok=True)
    pdb_path = pdb_dir / f"{args.template_pdb_id}.pdb"
    if not pdb_path.exists():
        download_pdb(args.template_pdb_id, pdb_path)

    sg_coords = parse_sg_coordinates(pdb_path)

    required_sites = [
        ("A", template_cp),
        ("A", template_cr),
        ("B", template_cp),
        ("B", template_cr),
    ]
    missing_sites = [site for site in required_sites if site not in sg_coords]

    distance_rows: list[dict[str, Any]] = []

    comparisons = [
        ("A_cp_to_A_cr", ("A", template_cp), ("A", template_cr)),
        ("B_cp_to_B_cr", ("B", template_cp), ("B", template_cr)),
        ("A_cp_to_B_cr", ("A", template_cp), ("B", template_cr)),
        ("A_cr_to_B_cp", ("A", template_cr), ("B", template_cp)),
        ("A_cp_to_B_cp", ("A", template_cp), ("B", template_cp)),
        ("A_cr_to_B_cr", ("A", template_cr), ("B", template_cr)),
    ]

    for label, site_a, site_b in comparisons:
        if site_a in sg_coords and site_b in sg_coords:
            dist = distance(sg_coords[site_a], sg_coords[site_b])
            distance_rows.append(
                {
                    "comparison": label,
                    "chain_site_a": f"{site_a[0]}:{site_a[1]}",
                    "chain_site_b": f"{site_b[0]}:{site_b[1]}",
                    "distance_angstrom": round(dist, 3),
                }
            )
        else:
            distance_rows.append(
                {
                    "comparison": label,
                    "chain_site_a": f"{site_a[0]}:{site_a[1]}",
                    "chain_site_b": f"{site_b[0]}:{site_b[1]}",
                    "distance_angstrom": "",
                }
            )

    target_aln, template_aln = needleman_wunsch(target["sequence"], template["sequence"])

    target_cp_pos, target_cp_res = map_reference_position_to_query(target_aln, template_aln, template_cp)
    target_cr_pos, target_cr_res = map_reference_position_to_query(target_aln, template_aln, template_cr)

    summary_row = {
        "target_id": args.target_id,
        "target_accession": target.get("accession", ""),
        "template_id": args.template_id,
        "template_accession": template.get("accession", ""),
        "template_pdb_id": args.template_pdb_id,
        "template_peroxidatic_position": template_cp,
        "template_resolving_position": template_cr,
        "target_residue_at_template_peroxidatic": target_cp_res,
        "target_position_at_template_peroxidatic": target_cp_pos,
        "target_residue_at_template_resolving": target_cr_res,
        "target_position_at_template_resolving": target_cr_pos,
        "target_has_cys_at_peroxidatic_map": "yes" if target_cp_res == "C" else "no",
        "target_has_cys_at_resolving_map": "yes" if target_cr_res == "C" else "no",
        "target_supports_template_like_cp_cr_pair": "yes" if target_cp_res == "C" and target_cr_res == "C" else "no",
        "missing_template_sites": ",".join(f"{chain}:{pos}" for chain, pos in missing_sites),
        "template_pdb_path": str(pdb_path),
    }

    summary_tsv = args.output_dir / "dimer_template_mapping_summary.tsv"
    distances_tsv = args.output_dir / "dimer_template_sg_distances.tsv"
    report_json = args.output_dir / "dimer_template_report.json"

    write_tsv([summary_row], summary_tsv)
    write_tsv(distance_rows, distances_tsv)

    report = {
        "summary": summary_row,
        "distances": distance_rows,
        "summary_file": str(summary_tsv),
        "distances_file": str(distances_tsv),
    }
    report_json.write_text(json.dumps(report, indent=2), encoding="utf-8")

    print(f"Wrote {summary_tsv}")
    print(f"Wrote {distances_tsv}")
    print(f"Wrote {report_json}")


if __name__ == "__main__":
    main()
