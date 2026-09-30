#!/usr/bin/env python3
"""Summarize InterPro regions and zinc-coordinating residue patterns from sequence."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path


TARGETS = {
    "IPR001841": "RING_type_zinc_finger",
    "IPR018957": "C3HC4_RING_type",
    "IPR017907": "RING_conserved_site",
    "IPR003111": "Lon_N_terminal",
    "IPR003593": "AAA_plus_ATPase_domain",
    "IPR003959": "AAA_type_ATPase_core",
    "IPR004815": "Lon_protease_family",
    "IPR008268": "Peptidase_S16_active_site",
    "IPR008269": "Lon_proteolytic_domain",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--uniprot-dir", type=Path, required=True)
    parser.add_argument("--interpro-dir", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--presence-output", type=Path, required=True)
    parser.add_argument("--regions", type=Path, required=True)
    parser.add_argument("--ring-output", type=Path, required=True)
    return parser.parse_args()


def locations(record: dict) -> list[tuple[str, str, int, int]]:
    found = []
    for result in record.get("results", []):
        accession = result.get("metadata", {}).get("accession", "")
        if accession not in TARGETS:
            continue
        for protein in result.get("proteins", []):
            for location in protein.get("entry_protein_locations", []):
                fragments = location.get("fragments", [])
                if len(fragments) != 1:
                    continue
                fragment = fragments[0]
                found.append((accession, TARGETS[accession], int(fragment["start"]), int(fragment["end"])))
    return found


def ligand_pattern(sequence: str, start: int, end: int) -> tuple[int, str, str]:
    region = sequence[start - 1 : end]
    positions = [(i + start, aa) for i, aa in enumerate(region) if aa in {"C", "H"}]
    signature = ";".join(f"{aa}{position}" for position, aa in positions)
    spacings = ";".join(
        str(positions[i + 1][0] - positions[i][0] - 1) for i in range(len(positions) - 1)
    )
    return len(positions), signature, spacings


def main() -> None:
    args = parse_args()
    for path in (args.output, args.presence_output, args.regions, args.ring_output):
        path.parent.mkdir(parents=True, exist_ok=True)
    with args.manifest.open() as handle:
        manifest = list(csv.DictReader(handle, delimiter="\t"))
    architecture_rows = []
    presence_rows = []
    ring_rows = []
    fasta_records = []
    for item in manifest:
        accession = item["accession"]
        uniprot = json.loads((args.uniprot_dir / f"{accession}.json").read_text())
        interpro = json.loads((args.interpro_dir / f"{accession}.json").read_text())
        sequence = uniprot["sequence"]["value"]
        observed_locations = locations(interpro)
        observed_iprs = {ipr for ipr, _, _, _ in observed_locations}
        for ipr, domain in TARGETS.items():
            matching = [(start, end) for seen, _, start, end in observed_locations if seen == ipr]
            presence_rows.append(
                {
                    **item,
                    "interpro_accession": ipr,
                    "domain": domain,
                    "present": str(ipr in observed_iprs).lower(),
                    "locations": ";".join(f"{start}-{end}" for start, end in matching) or "-",
                }
            )
        for ipr, domain, start, end in observed_locations:
            region_id = f"{accession}|{domain}|{start}-{end}"
            architecture_rows.append(
                {
                    **item,
                    "interpro_accession": ipr,
                    "domain": domain,
                    "start": start,
                    "end": end,
                    "region_length": end - start + 1,
                    "sequence_length": len(sequence),
                }
            )
            fasta_records.append((region_id, sequence[start - 1 : end]))
            if domain in {"RING_type_zinc_finger", "C3HC4_RING_type"}:
                count, signature, spacings = ligand_pattern(sequence, start, end)
                ring_rows.append(
                    {
                        **item,
                        "interpro_accession": ipr,
                        "start": start,
                        "end": end,
                        "cys_his_count": count,
                        "cys_his_signature": signature,
                        "inter_ligand_spacings": spacings,
                    }
                )
    fields = list(architecture_rows[0])
    with args.output.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, delimiter="\t", fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(architecture_rows)
    presence_fields = list(presence_rows[0])
    with args.presence_output.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, delimiter="\t", fieldnames=presence_fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(presence_rows)
    ring_fields = list(ring_rows[0])
    with args.ring_output.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, delimiter="\t", fieldnames=ring_fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(ring_rows)
    with args.regions.open("w") as handle:
        for name, seq in fasta_records:
            handle.write(f">{name}\n")
            handle.write("\n".join(seq[i : i + 60] for i in range(0, len(seq), 60)) + "\n")


if __name__ == "__main__":
    main()
