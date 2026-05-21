#!/usr/bin/env python3
"""Build Boltz/BioLM inputs for the Complex III CYC1:UQCRFS1 interface pilot."""

from __future__ import annotations

from pathlib import Path
import re
from typing import Any


ROOT = Path(__file__).resolve().parent
REPO = ROOT.parents[1]
OUT_DIR = ROOT / "inputs"

SPECS = {
    "A": {
        "gene": "CYC1",
        "uniprot": REPO / "genes/human/CYC1/CYC1-uniprot.txt",
        "start": 85,
        "end": 281,
        "note": "intermembrane-space cytochrome c1 heme domain",
    },
    "B": {
        "gene": "UQCRFS1",
        "uniprot": REPO / "genes/human/UQCRFS1/UQCRFS1-uniprot.txt",
        "start": 141,
        "end": 274,
        "note": "intermembrane-space Rieske head domain",
    },
}


def read_uniprot_sequence(path: Path) -> str:
    in_seq = False
    parts: list[str] = []
    for line in path.read_text().splitlines():
        if line.startswith("SQ   "):
            in_seq = True
            continue
        if in_seq:
            if line.startswith("//"):
                break
            parts.append(re.sub(r"[^A-Z]", "", line))
    sequence = "".join(parts)
    if not sequence:
        raise ValueError(f"No sequence found in {path}")
    return sequence


def subseq(full: str, start: int, end: int) -> str:
    return full[start - 1 : end]


def build_records() -> list[dict[str, Any]]:
    records = []
    for chain_id, spec in SPECS.items():
        full = read_uniprot_sequence(Path(spec["uniprot"]))
        records.append(
            {
                **spec,
                "chain": chain_id,
                "sequence": subseq(full, spec["start"], spec["end"]),
            }
        )
    return records


def write_fasta(records: list[dict[str, Any]]) -> Path:
    lines = []
    for record in records:
        lines.append(
            f">{record['chain']}|{record['gene']}|"
            f"{record['start']}-{record['end']}|{record['note']}"
        )
        lines.append(record["sequence"])
    path = OUT_DIR / "cyc1_uqcrfs1_ims_domains.fasta"
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return path


def write_yaml(records: list[dict[str, Any]]) -> Path:
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
    path = OUT_DIR / "cyc1_uqcrfs1_ims_domains.yaml"
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return path


def write_manifest(records: list[dict[str, Any]]) -> Path:
    lines = ["chain,gene,start,end,note,length"]
    for record in records:
        lines.append(
            f"{record['chain']},{record['gene']},{record['start']},"
            f"{record['end']},{record['note']},{len(record['sequence'])}"
        )
    path = ROOT / "cyc1_uqcrfs1_ims_domains_manifest.csv"
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return path


def main() -> None:
    OUT_DIR.mkdir(exist_ok=True)
    records = build_records()
    paths = [write_fasta(records), write_yaml(records), write_manifest(records)]
    print("Wrote:")
    for path in paths:
        print(f"  {path}")


if __name__ == "__main__":
    main()
