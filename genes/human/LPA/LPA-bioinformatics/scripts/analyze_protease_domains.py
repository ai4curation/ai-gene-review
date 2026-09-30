#!/usr/bin/env python3
"""Align UniProt-defined peptidase S1 domains and map reference functional sites."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path
from typing import Any

from Bio import Align
from Bio.Align import substitution_matrices


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input-dir", type=Path, required=True)
    parser.add_argument("--reference", required=True)
    parser.add_argument("--targets", nargs="+", required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    return parser.parse_args()


def load_record(input_dir: Path, accession: str) -> dict[str, Any]:
    return json.loads((input_dir / "uniprot_json" / f"{accession}.json").read_text())


def location(feature: dict[str, Any]) -> tuple[int, int]:
    return feature["location"]["start"]["value"], feature["location"]["end"]["value"]


def protease_domain(record: dict[str, Any]) -> tuple[int, int]:
    matches = [
        location(feature)
        for feature in record["features"]
        if feature["type"] == "Domain" and "Peptidase S1" in feature.get("description", "")
    ]
    if len(matches) != 1:
        raise ValueError(f"Expected one Peptidase S1 domain, found {matches}")
    return matches[0]


def sequence(record: dict[str, Any], bounds: tuple[int, int]) -> str:
    start, end = bounds
    return record["sequence"]["value"][start - 1 : end]


def active_sites(record: dict[str, Any]) -> list[int]:
    return [
        location(feature)[0]
        for feature in record["features"]
        if feature["type"] == "Active site"
        and "Charge relay system" in feature.get("description", "")
    ]


def activation_junction(record: dict[str, Any], domain_start: int) -> tuple[int, int, str]:
    exact = [
        feature
        for feature in record["features"]
        if feature["type"] == "Site"
        and location(feature) == (domain_start - 1, domain_start)
        and "Cleavage" in feature.get("description", "")
    ]
    description = exact[0].get("description", "") if exact else "not annotated at domain boundary"
    return domain_start - 1, domain_start, description


def align_domains(reference: str, target: str) -> Align.Alignment:
    aligner = Align.PairwiseAligner(mode="global")
    aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
    aligner.open_gap_score = -10.0
    aligner.extend_gap_score = -0.5
    return aligner.align(reference, target)[0]


def map_reference_offset(alignment: Align.Alignment, ref_offset: int) -> int | None:
    coordinates = alignment.coordinates
    for block in range(coordinates.shape[1] - 1):
        r0, r1 = int(coordinates[0, block]), int(coordinates[0, block + 1])
        t0, t1 = int(coordinates[1, block]), int(coordinates[1, block + 1])
        if r0 <= ref_offset < r1:
            if (r1 - r0) == (t1 - t0):
                return t0 + (ref_offset - r0)
            return None
    return None


def interpro_summary(input_dir: Path, accession: str) -> tuple[int, list[str]]:
    payload = json.loads((input_dir / "interpro_json" / f"{accession}.json").read_text())
    entries = []
    kringle_fragments: set[tuple[int, int]] = set()
    for result in payload["results"]:
        metadata = result["metadata"]
        entry_accession = metadata.get("accession")
        if entry_accession in {"IPR009003", "IPR001254"}:
            entries.append(entry_accession)
        # Count only the integrated InterPro entry. Member-database matches are
        # also returned and would otherwise count the same domain repeatedly.
        if entry_accession == "IPR000001":
            for protein in result.get("proteins", []):
                for hit in protein.get("entry_protein_locations", []):
                    for fragment in hit.get("fragments", []):
                        kringle_fragments.add((fragment["start"], fragment["end"]))
    return len(kringle_fragments), sorted(set(entries))


def write_tsv(path: Path, fieldnames: list[str], rows: list[dict[str, object]]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(
            handle, fieldnames=fieldnames, delimiter="\t", lineterminator="\n"
        )
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    args = parse_args()
    args.output_dir.mkdir(parents=True, exist_ok=True)
    accessions = [args.reference, *args.targets]
    records = {acc: load_record(args.input_dir, acc) for acc in accessions}
    bounds = {acc: protease_domain(record) for acc, record in records.items()}
    domains = {acc: sequence(record, bounds[acc]) for acc, record in records.items()}

    metadata_rows: list[dict[str, object]] = []
    for accession in accessions:
        record = records[accession]
        start, end = bounds[accession]
        kringle_count, interpro_entries = interpro_summary(args.input_dir, accession)
        metadata_rows.append(
            {
                "accession": accession,
                "recommended_name": record["proteinDescription"]["recommendedName"]["fullName"]["value"],
                "organism": record["organism"]["scientificName"],
                "sequence_length": record["sequence"]["length"],
                "protease_domain_start": start,
                "protease_domain_end": end,
                "protease_domain_length": len(domains[accession]),
                "uniprot_charge_relay_sites": ",".join(map(str, active_sites(record))) or "none",
                "interpro_kringle_fragment_count": kringle_count,
                "interpro_protease_entries": ",".join(interpro_entries) or "none",
            }
        )
    write_tsv(args.output_dir / "record_summary.tsv", list(metadata_rows[0]), metadata_rows)

    with (args.output_dir / "protease_domains.fasta").open("w") as handle:
        for accession in accessions:
            start, end = bounds[accession]
            handle.write(f">{accession}|UniProt:{start}-{end}\n{domains[accession]}\n")

    reference = args.reference
    ref_start, _ = bounds[reference]
    ref_sites = active_sites(records[reference])
    if len(ref_sites) != 3:
        raise ValueError(f"Reference {reference} does not have exactly three charge-relay sites")

    site_rows: list[dict[str, object]] = []
    identity_rows: list[dict[str, object]] = []
    junction_rows: list[dict[str, object]] = []
    ref_junction = activation_junction(records[reference], ref_start)
    ref_sequence = records[reference]["sequence"]["value"]

    for target in args.targets:
        alignment = align_domains(domains[reference], domains[target])
        target_start, _ = bounds[target]
        target_sequence = records[target]["sequence"]["value"]
        aligned_pairs = alignment.aligned
        matches = 0
        aligned_length = 0
        for (r0, r1), (t0, t1) in zip(aligned_pairs[0], aligned_pairs[1]):
            ref_piece = domains[reference][r0:r1]
            target_piece = domains[target][t0:t1]
            matches += sum(a == b for a, b in zip(ref_piece, target_piece))
            aligned_length += len(ref_piece)
        identity_rows.append(
            {
                "reference": reference,
                "target": target,
                "alignment_score": f"{alignment.score:.1f}",
                "identical_aligned_residues": matches,
                "aligned_residues": aligned_length,
                "percent_identity": f"{100 * matches / aligned_length:.2f}",
            }
        )
        alignment_text = str(alignment).rstrip("\r\n") + "\n"
        (args.output_dir / f"alignment_{reference}_vs_{target}.txt").write_text(
            alignment_text, encoding="utf-8"
        )

        target_annotated_sites = set(active_sites(records[target]))
        for order, ref_position in enumerate(ref_sites, start=1):
            ref_offset = ref_position - ref_start
            target_offset = map_reference_offset(alignment, ref_offset)
            target_position = target_start + target_offset if target_offset is not None else None
            site_rows.append(
                {
                    "triad_order": order,
                    "reference_accession": reference,
                    "reference_position": ref_position,
                    "reference_residue": ref_sequence[ref_position - 1],
                    "target_accession": target,
                    "target_position": target_position if target_position is not None else "gap",
                    "target_residue": target_sequence[target_position - 1] if target_position else "-",
                    "target_uniprot_active_site_annotation": target_position in target_annotated_sites,
                }
            )

        target_junction = activation_junction(records[target], target_start)
        junction_rows.append(
            {
                "reference_accession": reference,
                "reference_boundary": f"{ref_junction[0]}|{ref_junction[1]}",
                "reference_residues": ref_sequence[ref_junction[0] - 1 : ref_junction[1]],
                "reference_cleavage_annotation": ref_junction[2],
                "target_accession": target,
                "target_boundary": f"{target_junction[0]}|{target_junction[1]}",
                "target_residues": target_sequence[target_junction[0] - 1 : target_junction[1]],
                "target_cleavage_annotation": target_junction[2],
            }
        )

    write_tsv(args.output_dir / "pairwise_identity.tsv", list(identity_rows[0]), identity_rows)
    write_tsv(args.output_dir / "active_site_comparison.tsv", list(site_rows[0]), site_rows)
    write_tsv(args.output_dir / "activation_junction_comparison.tsv", list(junction_rows[0]), junction_rows)


if __name__ == "__main__":
    main()
