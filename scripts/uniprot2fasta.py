#!/usr/bin/env python3
"""
Extract FASTA sequence from UniProt .txt files

Usage:
    python uniprot2fasta.py <uniprot_file> [output_fasta]

Example:
    python uniprot2fasta.py genes/human/RBFOX3/RBFOX3-uniprot.txt
    python uniprot2fasta.py genes/human/RBFOX3/RBFOX3-uniprot.txt RBFOX3.fasta
"""

import sys
import re
from pathlib import Path


def extract_fasta_from_uniprot(uniprot_file):
    """Extract FASTA sequence from UniProt text file"""

    with open(uniprot_file, "r") as f:
        content = f.read()

    # Extract ID
    id_match = re.search(r"^ID\s+(\S+)", content, re.MULTILINE)
    uniprot_id = id_match.group(1) if id_match else "Unknown"

    # Extract accession
    ac_match = re.search(r"^AC\s+([^;]+)", content, re.MULTILINE)
    accession = ac_match.group(1).strip() if ac_match else "Unknown"

    # Extract gene name - handle various formats
    gene_match = re.search(r"^GN\s+Name=([^;{]+)", content, re.MULTILINE)
    if gene_match:
        gene_name = gene_match.group(1).strip()
    else:
        # Try alternative format
        gene_match = re.search(r"^GN\s+([^{]+)", content, re.MULTILINE)
        if gene_match:
            # Extract just the gene name, not the evidence tags
            gene_text = gene_match.group(1)
            # Look for Name= or just take first word
            if "Name=" in gene_text:
                gene_name = gene_text.split("Name=")[1].split()[0].strip(";")
            else:
                gene_name = gene_text.split()[0].strip(";")
        else:
            # Use filename as fallback
            gene_name = uniprot_file.stem.replace("-uniprot", "")

    # Extract organism
    os_match = re.search(r"^OS\s+(.+?)\.", content, re.MULTILINE)
    organism = os_match.group(1).strip() if os_match else "Unknown"

    # Extract sequence - it's between SQ and //
    seq_section = re.search(r"^SQ\s+.+?\n(.*?)^//", content, re.MULTILINE | re.DOTALL)
    if not seq_section:
        raise ValueError(f"No sequence found in {uniprot_file}")

    # Clean sequence - remove spaces and numbers
    sequence = seq_section.group(1)
    sequence = re.sub(r"[^A-Z]", "", sequence)

    # Format as FASTA
    header = f">{accession}|{uniprot_id}|{gene_name} {organism}"

    # Break sequence into 60-char lines
    formatted_seq = []
    for i in range(0, len(sequence), 60):
        formatted_seq.append(sequence[i : i + 60])

    fasta = header + "\n" + "\n".join(formatted_seq)

    return fasta, accession, gene_name


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    uniprot_file = Path(sys.argv[1])

    if not uniprot_file.exists():
        print(f"Error: File {uniprot_file} not found")
        sys.exit(1)

    try:
        fasta, accession, gene_name = extract_fasta_from_uniprot(uniprot_file)

        # Determine output file
        if len(sys.argv) > 2:
            output_file = Path(sys.argv[2])
        else:
            # Default: same directory as input, with .fasta extension
            output_file = uniprot_file.parent / f"{gene_name}.fasta"

        # Write FASTA
        with open(output_file, "w") as f:
            f.write(fasta)

        print(f"Extracted FASTA for {gene_name} ({accession})")
        print(f"Written to: {output_file}")

    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
