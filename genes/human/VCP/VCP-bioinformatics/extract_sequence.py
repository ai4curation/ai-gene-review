#!/usr/bin/env python3
"""Extract amino acid sequence from UniProt flat file and write as FASTA."""

import sys
import re
from pathlib import Path


def extract_sequence_from_uniprot(uniprot_file: Path) -> tuple[str, str, str]:
    """Extract accession, gene name, and sequence from UniProt flat file.

    Returns (accession, gene_name, sequence).
    """
    accession = ""
    gene_name = ""
    in_sequence = False
    seq_lines = []

    with open(uniprot_file) as f:
        for line in f:
            if line.startswith("AC   ") and not accession:
                accession = line.split()[1].rstrip(";")
            elif line.startswith("GN   Name=") and not gene_name:
                match = re.search(r"Name=(\S+)", line)
                if match:
                    gene_name = match.group(1).rstrip(";")
            elif line.startswith("SQ   SEQUENCE"):
                in_sequence = True
            elif in_sequence:
                if line.startswith("//"):
                    break
                seq_lines.append(line.strip().replace(" ", ""))

    sequence = "".join(seq_lines)
    return accession, gene_name, sequence


def main():
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} <uniprot_flat_file> <output_fasta>", file=sys.stderr)
        sys.exit(1)

    uniprot_file = Path(sys.argv[1])
    output_fasta = Path(sys.argv[2])

    accession, gene_name, sequence = extract_sequence_from_uniprot(uniprot_file)

    with open(output_fasta, "w") as f:
        f.write(f">{accession}|{gene_name} OS=Homo sapiens\n")
        # Write sequence in 60-char lines
        for i in range(0, len(sequence), 60):
            f.write(sequence[i:i+60] + "\n")

    print(f"Wrote {len(sequence)} aa for {accession} ({gene_name}) to {output_fasta}")


if __name__ == "__main__":
    main()
