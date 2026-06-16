#!/usr/bin/env python3
"""Build Boltz Model C inputs for the COX2/SCO1/SCO2 attribution test."""

from __future__ import annotations

from pathlib import Path
from typing import Any

from make_inputs import REPO, ROOT, read_uniprot_sequence, subseq


OUT_DIR = ROOT / "inputs"

MODEL_C_FULL = {
    "A": {
        "gene": "MT-CO2",
        "uniprot": ROOT / "P00403_MT-CO2_uniprot.txt",
        "start": 1,
        "end": 227,
        "note": "full mature mitochondrial coding sequence; includes TM helices and IMS CuA domain",
    },
    "B": {
        "gene": "SCO1",
        "uniprot": REPO / "genes/human/SCO1/SCO1-uniprot.txt",
        "start": 68,
        "end": 301,
        "note": "mature form from OpenScientist Model C specification",
    },
    "C": {
        "gene": "SCO2",
        "uniprot": REPO / "genes/human/SCO2/SCO2-uniprot.txt",
        "start": 42,
        "end": 266,
        "note": "mature form from OpenScientist Model C specification",
    },
}

MODEL_C_DOMAINS = {
    "A": {
        "gene": "MT-CO2",
        "uniprot": ROOT / "P00403_MT-CO2_uniprot.txt",
        "start": 88,
        "end": 227,
        "note": "IMS CuA domain",
    },
    "B": {
        "gene": "SCO1",
        "uniprot": REPO / "genes/human/SCO1/SCO1-uniprot.txt",
        "start": 112,
        "end": 301,
        "note": "IMS metallochaperone domain",
    },
    "C": {
        "gene": "SCO2",
        "uniprot": REPO / "genes/human/SCO2/SCO2-uniprot.txt",
        "start": 79,
        "end": 266,
        "note": "IMS metallochaperone domain",
    },
}

MODEL_A_DOMAINS = {
    "A": MODEL_C_DOMAINS["A"],
    "B": MODEL_C_DOMAINS["B"],
}

COPPER_LIGANDS = [
    ("U1", "MT-CO2 CuA site copper 1"),
    ("U2", "MT-CO2 CuA site copper 2"),
    ("U3", "SCO1 CxxxC/His copper"),
    ("U4", "SCO2 CxxxC/His copper"),
]

COPPER_CONTACTS = {
    "U1": [("A", 161), ("A", 196), ("A", 200)],
    "U2": [("A", 196), ("A", 198), ("A", 200), ("A", 204), ("A", 207)],
    "U3": [("B", 169), ("B", 173), ("B", 260)],
    "U4": [("C", 133), ("C", 137), ("C", 224)],
}


def ligand_ids_for_specs(specs: dict[str, dict[str, Any]]) -> list[tuple[str, str]]:
    chains = set(specs)
    ligand_ids = []
    for ligand_id, note in COPPER_LIGANDS:
        contact_chains = {chain_id for chain_id, _pos in COPPER_CONTACTS[ligand_id]}
        if contact_chains <= chains:
            ligand_ids.append((ligand_id, note))
    return ligand_ids


def build_records(specs: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    records = []
    for chain_id, spec in specs.items():
        full = read_uniprot_sequence(Path(spec["uniprot"]))
        seq = subseq(full, spec["start"], spec["end"])
        records.append({**spec, "chain": chain_id, "sequence": seq})
    return records


def shifted_contacts(
    contacts: list[tuple[str, int]],
    specs: dict[str, dict[str, Any]],
) -> list[tuple[str, int]]:
    shifted = []
    for chain_id, original_position in contacts:
        start = int(specs[chain_id]["start"])
        end = int(specs[chain_id]["end"])
        if not start <= original_position <= end:
            raise ValueError(
                f"{chain_id} residue {original_position} is outside {start}-{end}"
            )
        shifted.append((chain_id, original_position - start + 1))
    return shifted


def write_fasta(name: str, records: list[dict[str, Any]]) -> Path:
    lines = []
    for record in records:
        lines.append(
            f">{record['chain']}|{record['gene']}|"
            f"{record['start']}-{record['end']}|{record['note']}"
        )
        lines.append(record["sequence"])
    path = OUT_DIR / f"{name}.fasta"
    path.write_text("\n".join(lines) + "\n")
    return path


def write_yaml(
    name: str,
    records: list[dict[str, Any]],
    specs: dict[str, dict[str, Any]],
    include_copper: bool = False,
) -> Path:
    lines = ["version: 1", "sequences:"]
    for record in records:
        lines.extend(
            [
                "  - protein:",
                f"      id: {record['chain']}",
                f"      sequence: {record['sequence']}",
                "      msa: empty",
                (
                    f"      # {record['gene']} residues "
                    f"{record['start']}-{record['end']}; {record['note']}"
                ),
            ]
    )

    if include_copper:
        ligand_ids = ligand_ids_for_specs(specs)
        for ligand_id, note in ligand_ids:
            lines.extend(
                [
                    "  - ligand:",
                    f"      id: {ligand_id}",
                    "      ccd: CU",
                    f"      # {note}",
                ]
            )
        lines.append("constraints:")
        for ligand_id, _note in ligand_ids:
            contacts = shifted_contacts(COPPER_CONTACTS[ligand_id], specs)
            contact_text = ", ".join(f"[{chain}, {pos}]" for chain, pos in contacts)
            lines.extend(
                [
                    "  - pocket:",
                    f"      binder: {ligand_id}",
                    f"      contacts: [{contact_text}]",
                    "      max_distance: 4.0",
                    "      force: true",
                ]
            )

    suffix = "_cu_pocket" if include_copper else ""
    path = OUT_DIR / f"{name}{suffix}.yaml"
    path.write_text("\n".join(lines) + "\n")
    return path


def write_manifest(name: str, records: list[dict[str, Any]]) -> Path:
    lines = ["chain,gene,start,end,note,length"]
    for record in records:
        lines.append(
            f"{record['chain']},{record['gene']},{record['start']},"
            f"{record['end']},{record['note']},{len(record['sequence'])}"
        )
    path = ROOT / f"{name}_manifest.csv"
    path.write_text("\n".join(lines) + "\n")
    return path


def write_input_set(name: str, specs: dict[str, dict[str, Any]]) -> list[Path]:
    records = build_records(specs)
    return [
        write_fasta(name, records),
        write_yaml(name, records, specs, include_copper=False),
        write_yaml(name, records, specs, include_copper=True),
        write_manifest(name, records),
    ]


def main() -> None:
    OUT_DIR.mkdir(exist_ok=True)
    paths = []
    paths.extend(write_input_set("cox2_sco1_sco2_model_c_full", MODEL_C_FULL))
    paths.extend(write_input_set("cox2_sco1_sco2_model_c_domains", MODEL_C_DOMAINS))
    paths.extend(write_input_set("cox2_sco1_model_a_domains", MODEL_A_DOMAINS))
    print("Wrote:")
    for path in paths:
        print(f"  {path}")


if __name__ == "__main__":
    main()
