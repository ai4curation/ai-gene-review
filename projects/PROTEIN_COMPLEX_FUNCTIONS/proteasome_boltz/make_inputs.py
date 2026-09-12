#!/usr/bin/env python3
"""Build Boltz/BioLM inputs for a proteasome PSMB5:PSMA1 attribution pilot."""

from __future__ import annotations

from pathlib import Path
import re
from typing import Any


ROOT = Path(__file__).resolve().parent
REPO = ROOT.parents[1]
OUT_DIR = ROOT / "inputs"

SPECS = {
    "A": {
        "gene": "PSMB5",
        "uniprot": REPO / "genes/human/PSMB5/PSMB5-uniprot.txt",
        "start": 60,
        "end": 263,
        "note": "mature beta5 catalytic proteasome subunit; active-site Thr60 is residue 1 in this input",
    },
    "B": {
        "gene": "PSMA1",
        "uniprot": REPO / "genes/human/PSMA1/PSMA1-uniprot.txt",
        "start": 1,
        "end": 263,
        "note": "alpha-ring structural proteasome subunit",
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
    seq = "".join(parts)
    if not seq:
        raise ValueError(f"No sequence found in {path}")
    return seq


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
    path = OUT_DIR / "psmb5_psma1_attribution_domains.fasta"
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
    path = OUT_DIR / "psmb5_psma1_attribution_domains.yaml"
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return path


def write_manifest(records: list[dict[str, Any]]) -> Path:
    lines = ["chain,gene,start,end,note,length"]
    for record in records:
        lines.append(
            f"{record['chain']},{record['gene']},{record['start']},"
            f"{record['end']},{record['note']},{len(record['sequence'])}"
        )
    path = ROOT / "psmb5_psma1_attribution_domains_manifest.csv"
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
