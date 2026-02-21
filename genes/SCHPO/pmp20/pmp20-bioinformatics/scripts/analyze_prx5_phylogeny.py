#!/usr/bin/env python3
"""Analyze Prx5 homolog panel with catalytic-state mapping and UPGMA tree."""

from __future__ import annotations

import argparse
import csv
import json
from dataclasses import dataclass
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
    return (matches / aligned) if aligned else 0.0


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


def catalytic_class(record: dict[str, Any]) -> str:
    act_sites = record.get("act_site_positions", [])
    resolving = choose_resolving_positions(record)
    cys_count = len(record.get("cysteine_positions", []))

    if act_sites and resolving:
        return "peroxidatic_plus_resolving"
    if act_sites and not resolving:
        return "peroxidatic_only"
    if cys_count:
        return "cysteine_present_no_act_site"
    return "no_cysteine"


@dataclass
class ClusterNode:
    name: str
    members: set[str]
    height: float
    newick: str


def cluster_distance(node_a: ClusterNode, node_b: ClusterNode, pairwise_distance: dict[tuple[str, str], float]) -> float:
    total = 0.0
    count = 0
    for a in node_a.members:
        for b in node_b.members:
            key = tuple(sorted((a, b)))
            total += pairwise_distance[key]
            count += 1
    return (total / count) if count else 0.0


def build_upgma_newick(labels: list[str], pairwise_distance: dict[tuple[str, str], float]) -> str:
    clusters: dict[str, ClusterNode] = {
        label: ClusterNode(name=label, members={label}, height=0.0, newick=label) for label in labels
    }
    counter = 1

    while len(clusters) > 1:
        keys = sorted(clusters.keys())
        best_pair: tuple[str, str] | None = None
        best_distance = float("inf")

        for i, key_i in enumerate(keys):
            for key_j in keys[i + 1 :]:
                distance = cluster_distance(clusters[key_i], clusters[key_j], pairwise_distance)
                if distance < best_distance:
                    best_distance = distance
                    best_pair = (key_i, key_j)

        if best_pair is None:
            raise RuntimeError("Failed to find a cluster pair for UPGMA")

        left = clusters.pop(best_pair[0])
        right = clusters.pop(best_pair[1])

        new_height = best_distance / 2.0
        left_branch = max(0.0, new_height - left.height)
        right_branch = max(0.0, new_height - right.height)

        merged = ClusterNode(
            name=f"cluster_{counter}",
            members=left.members | right.members,
            height=new_height,
            newick=f"({left.newick}:{left_branch:.6f},{right.newick}:{right_branch:.6f})",
        )
        counter += 1
        clusters[merged.name] = merged

    final_node = next(iter(clusters.values()))
    return final_node.newick + ";"


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
    parser.add_argument("--neighbor-count", type=int, default=10)
    parser.add_argument("--output-dir", required=True, type=Path)
    args = parser.parse_args()

    args.output_dir.mkdir(parents=True, exist_ok=True)
    proteins = json.loads(args.proteins_json.read_text(encoding="utf-8"))

    proteins = [protein for protein in proteins if protein.get("sequence")]
    proteins_by_id = {protein["protein_id"]: protein for protein in proteins}

    if args.target_id not in proteins_by_id:
        raise SystemExit(f"Target protein_id {args.target_id!r} not found in proteins JSON")

    summary_rows = []
    for protein in proteins:
        resolving = choose_resolving_positions(protein)
        summary_rows.append(
            {
                "protein_id": protein["protein_id"],
                "accession": protein.get("accession", ""),
                "display_name": protein.get("display_name", ""),
                "organism": protein.get("organism", ""),
                "sequence_length": len(protein["sequence"]),
                "cys_count": len(protein.get("cysteine_positions", [])),
                "peroxidatic_positions": ",".join(str(x) for x in protein.get("act_site_positions", [])),
                "resolving_positions": ",".join(str(x) for x in resolving),
                "catalytic_class": catalytic_class(protein),
            }
        )

    pairwise_rows = []
    pairwise_distance: dict[tuple[str, str], float] = {}

    for i, protein_a in enumerate(proteins):
        for protein_b in proteins[i + 1 :]:
            aln_a, aln_b = needleman_wunsch(protein_a["sequence"], protein_b["sequence"])
            identity = aligned_identity(aln_a, aln_b)
            key = tuple(sorted((protein_a["protein_id"], protein_b["protein_id"])))
            pairwise_distance[key] = 1.0 - identity

            pairwise_rows.append(
                {
                    "protein_a": protein_a["protein_id"],
                    "accession_a": protein_a.get("accession", ""),
                    "protein_b": protein_b["protein_id"],
                    "accession_b": protein_b.get("accession", ""),
                    "identity": round(identity, 4),
                }
            )

    labels = [protein["protein_id"] for protein in proteins]
    newick = build_upgma_newick(labels, pairwise_distance)

    target = proteins_by_id[args.target_id]
    target_neighbors = []
    for protein in proteins:
        if protein["protein_id"] == args.target_id:
            continue
        aln_t, aln_x = needleman_wunsch(target["sequence"], protein["sequence"])
        identity = aligned_identity(aln_t, aln_x)

        template_perox = protein.get("act_site_positions", [])
        template_resolving = choose_resolving_positions(protein)

        mapped_perox_position, mapped_perox_residue = (None, "")
        mapped_resolve_position, mapped_resolve_residue = (None, "")

        if template_perox:
            mapped_perox_position, mapped_perox_residue = map_reference_position_to_query(
                aln_t,
                aln_x,
                template_perox[0],
            )

        if template_resolving:
            mapped_resolve_position, mapped_resolve_residue = map_reference_position_to_query(
                aln_t,
                aln_x,
                template_resolving[0],
            )

        target_neighbors.append(
            {
                "target_id": args.target_id,
                "neighbor_id": protein["protein_id"],
                "neighbor_accession": protein.get("accession", ""),
                "neighbor_organism": protein.get("organism", ""),
                "identity": round(identity, 4),
                "neighbor_peroxidatic": ",".join(str(x) for x in template_perox),
                "neighbor_resolving": ",".join(str(x) for x in template_resolving),
                "target_residue_at_neighbor_peroxidatic": mapped_perox_residue,
                "target_position_at_neighbor_peroxidatic": mapped_perox_position,
                "target_residue_at_neighbor_resolving": mapped_resolve_residue,
                "target_position_at_neighbor_resolving": mapped_resolve_position,
                "neighbor_catalytic_class": catalytic_class(protein),
            }
        )

    target_neighbors.sort(key=lambda row: row["identity"], reverse=True)
    target_neighbors = target_neighbors[: args.neighbor_count]

    catalytic_counts: dict[str, int] = {}
    for row in summary_rows:
        catalytic_counts[row["catalytic_class"]] = catalytic_counts.get(row["catalytic_class"], 0) + 1

    top_neighbor_counts: dict[str, int] = {}
    for row in target_neighbors:
        top_neighbor_counts[row["neighbor_catalytic_class"]] = (
            top_neighbor_counts.get(row["neighbor_catalytic_class"], 0) + 1
        )

    summary_tsv = args.output_dir / "prx5_catalytic_state.tsv"
    pairwise_tsv = args.output_dir / "prx5_pairwise_identity.tsv"
    neighbors_tsv = args.output_dir / "pmp20_neighbor_context.tsv"
    tree_file = args.output_dir / "prx5_upgma_tree.newick"
    report_json = args.output_dir / "prx5_phylogeny_report.json"

    write_tsv(summary_rows, summary_tsv)
    write_tsv(pairwise_rows, pairwise_tsv)
    write_tsv(target_neighbors, neighbors_tsv)
    tree_file.write_text(newick + "\n", encoding="utf-8")

    report = {
        "n_proteins": len(proteins),
        "target_id": args.target_id,
        "tree_file": str(tree_file),
        "summary_file": str(summary_tsv),
        "pairwise_file": str(pairwise_tsv),
        "neighbors_file": str(neighbors_tsv),
        "catalytic_class_counts": catalytic_counts,
        "top_neighbor_catalytic_class_counts": top_neighbor_counts,
    }
    report_json.write_text(json.dumps(report, indent=2), encoding="utf-8")

    print(f"Wrote {summary_tsv}")
    print(f"Wrote {pairwise_tsv}")
    print(f"Wrote {neighbors_tsv}")
    print(f"Wrote {tree_file}")
    print(f"Wrote {report_json}")


if __name__ == "__main__":
    main()
