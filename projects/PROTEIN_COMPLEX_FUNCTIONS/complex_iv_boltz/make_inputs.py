#!/usr/bin/env python3
"""Build Boltz inputs for the Complex IV COX2 copper-maturation pilot."""

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent
REPO = ROOT.parents[1]

SOURCES = {
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
    "D": {
        "gene": "COA6",
        "uniprot": ROOT / "Q5JTJ3_COA6_uniprot.txt",
        "start": 55,
        "end": 98,
        "note": "Cx9C domain",
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


def main() -> None:
    out_dir = ROOT / "inputs"
    out_dir.mkdir(exist_ok=True)

    records = []
    for chain_id, spec in SOURCES.items():
        full = read_uniprot_sequence(spec["uniprot"])
        seq = subseq(full, spec["start"], spec["end"])
        records.append((chain_id, spec["gene"], spec["start"], spec["end"], spec["note"], seq))

    fasta_lines = []
    for chain_id, gene, start, end, note, seq in records:
        fasta_lines.append(f">{chain_id}|{gene}|{start}-{end}|{note}")
        fasta_lines.append(seq)
    (out_dir / "cox2_sco1_sco2_coa6_domains.fasta").write_text("\n".join(fasta_lines) + "\n")

    yaml_lines = ["version: 1", "sequences:"]
    for chain_id, gene, start, end, note, seq in records:
        yaml_lines.extend(
            [
                "  - protein:",
                f"      id: {chain_id}",
                f"      sequence: {seq}",
                "      msa: empty",
                f"      # {gene} residues {start}-{end}; {note}",
            ]
        )
    (out_dir / "cox2_sco1_sco2_coa6_domains.yaml").write_text("\n".join(yaml_lines) + "\n")

    manifest = ["chain,gene,start,end,note,length"]
    for chain_id, gene, start, end, note, seq in records:
        manifest.append(f"{chain_id},{gene},{start},{end},{note},{len(seq)}")
    (ROOT / "domain_manifest.csv").write_text("\n".join(manifest) + "\n")

    print("Wrote:")
    print(f"  {out_dir / 'cox2_sco1_sco2_coa6_domains.yaml'}")
    print(f"  {out_dir / 'cox2_sco1_sco2_coa6_domains.fasta'}")
    print(f"  {ROOT / 'domain_manifest.csv'}")


if __name__ == "__main__":
    main()
