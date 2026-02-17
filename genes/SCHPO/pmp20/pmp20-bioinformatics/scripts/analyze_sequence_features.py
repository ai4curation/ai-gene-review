#!/usr/bin/env python3
"""Analyze cysteine topology and catalytic-site correspondence across proteins."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path
from typing import Any


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


def aligned_identity(aln_a: str, aln_b: str) -> float:
    aligned = 0
    matches = 0
    for aa, bb in zip(aln_a, aln_b):
        if aa == "-" or bb == "-":
            continue
        aligned += 1
        if aa == bb:
            matches += 1
    if aligned == 0:
        return 0.0
    return matches / aligned


def map_reference_position_to_query(
    query_aln: str,
    reference_aln: str,
    reference_position: int,
) -> tuple[int | None, str]:
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


def window_around_position(sequence: str, position: int, flank: int = 5) -> str:
    if position < 1 or position > len(sequence):
        return ""
    start = max(0, position - 1 - flank)
    end = min(len(sequence), position + flank)
    return sequence[start:end]


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


def protein_summary_row(record: dict[str, Any]) -> dict[str, Any]:
    sequence = record["sequence"]
    cysteines = record.get("cysteine_positions", [])
    act_sites = record.get("act_site_positions", [])
    resolving_positions = choose_resolving_positions(record)

    anchor_position = act_sites[0] if act_sites else (cysteines[0] if cysteines else 0)
    anchor_window = window_around_position(sequence, anchor_position) if anchor_position else ""

    return {
        "protein_id": record["protein_id"],
        "display_name": record.get("display_name", ""),
        "role": record.get("role", ""),
        "activity_label": record.get("activity_label", ""),
        "accession": record.get("accession", ""),
        "sequence_length": len(sequence),
        "cys_count": len(cysteines),
        "cysteine_positions": ",".join(str(x) for x in cysteines),
        "act_site_positions": ",".join(str(x) for x in act_sites),
        "candidate_resolving_positions": ",".join(str(x) for x in resolving_positions),
        "anchor_position": anchor_position,
        "anchor_window_11aa": anchor_window,
        "has_second_cysteine": "yes" if len(cysteines) >= 2 else "no",
    }


def analyze_targets(records: list[dict[str, Any]]) -> list[dict[str, Any]]:
    targets = [record for record in records if record.get("role") == "target"]
    active_controls = [
        record
        for record in records
        if record.get("activity_label") == "active" and record.get("role") != "target"
    ]

    comparisons: list[dict[str, Any]] = []

    for target in targets:
        target_sequence = target["sequence"]

        for control in active_controls:
            control_sequence = control["sequence"]
            target_aln, control_aln = needleman_wunsch(target_sequence, control_sequence)
            identity = aligned_identity(target_aln, control_aln)

            control_act_sites = control.get("act_site_positions", [])
            control_peroxidatic = control_act_sites[0] if control_act_sites else 0
            control_resolving_positions = choose_resolving_positions(control)

            perox_target_pos, perox_target_res = (None, "-")
            if control_peroxidatic:
                perox_target_pos, perox_target_res = map_reference_position_to_query(
                    target_aln,
                    control_aln,
                    control_peroxidatic,
                )

            if control_resolving_positions:
                for resolving_position in control_resolving_positions:
                    resolve_target_pos, resolve_target_res = map_reference_position_to_query(
                        target_aln,
                        control_aln,
                        resolving_position,
                    )
                    comparisons.append(
                        {
                            "target_id": target["protein_id"],
                            "target_accession": target.get("accession", ""),
                            "active_control_id": control["protein_id"],
                            "active_control_accession": control.get("accession", ""),
                            "aligned_identity": round(identity, 4),
                            "control_peroxidatic_position": control_peroxidatic,
                            "target_residue_at_control_peroxidatic": perox_target_res,
                            "target_position_at_control_peroxidatic": perox_target_pos,
                            "control_resolving_position": resolving_position,
                            "target_residue_at_control_resolving": resolve_target_res,
                            "target_position_at_control_resolving": resolve_target_pos,
                        }
                    )
            else:
                comparisons.append(
                    {
                        "target_id": target["protein_id"],
                        "target_accession": target.get("accession", ""),
                        "active_control_id": control["protein_id"],
                        "active_control_accession": control.get("accession", ""),
                        "aligned_identity": round(identity, 4),
                        "control_peroxidatic_position": control_peroxidatic,
                        "target_residue_at_control_peroxidatic": perox_target_res,
                        "target_position_at_control_peroxidatic": perox_target_pos,
                        "control_resolving_position": "",
                        "target_residue_at_control_resolving": "",
                        "target_position_at_control_resolving": "",
                    }
                )

    return comparisons


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
    parser.add_argument("--output-dir", required=True, type=Path)
    args = parser.parse_args()

    records = json.loads(args.proteins_json.read_text(encoding="utf-8"))
    args.output_dir.mkdir(parents=True, exist_ok=True)

    summary_rows = [protein_summary_row(record) for record in records]
    comparison_rows = analyze_targets(records)

    summary_tsv = args.output_dir / "sequence_cysteine_summary.tsv"
    comparison_tsv = args.output_dir / "target_vs_active_alignment.tsv"
    report_json = args.output_dir / "sequence_feature_report.json"

    write_tsv(summary_rows, summary_tsv)
    write_tsv(comparison_rows, comparison_tsv)

    report = {
        "n_proteins": len(records),
        "n_targets": sum(1 for record in records if record.get("role") == "target"),
        "summary_file": str(summary_tsv),
        "comparison_file": str(comparison_tsv),
        "summary_rows": summary_rows,
        "comparisons": comparison_rows,
    }
    report_json.write_text(json.dumps(report, indent=2), encoding="utf-8")

    print(f"Wrote {summary_tsv}")
    print(f"Wrote {comparison_tsv}")
    print(f"Wrote {report_json}")


if __name__ == "__main__":
    main()
