#!/usr/bin/env python3
"""Fetch CDC48/p97 orthologs from UniProt for conservation analysis.

Retrieves well-characterized orthologs across eukaryotes for multiple sequence
alignment and conservation analysis.

Input: FASTA file (used only to extract the accession)
Output: Multi-FASTA file with orthologs
"""

import sys
import time
from pathlib import Path

import requests
from Bio import SeqIO


# Well-characterized CDC48/p97 orthologs with known UniProt accessions
ORTHOLOGS = {
    "P55072": ("Homo sapiens", "VCP"),
    "Q01853": ("Mus musculus", "Vcp"),
    "P25694": ("Saccharomyces cerevisiae", "CDC48"),
    "Q9P3A7": ("Schizosaccharomyces pombe", "cdc48"),
    "Q7KN62": ("Drosophila melanogaster", "TER94"),
    "P54811": ("Caenorhabditis elegans", "cdc-48.1"),
    "Q9SZJ3": ("Arabidopsis thaliana", "CDC48A"),
    "Q5ZL72": ("Gallus gallus", "VCP"),
    "Q7ZU99": ("Danio rerio", "vcp"),
}


def fetch_uniprot_fasta(accession: str) -> str | None:
    """Fetch FASTA sequence from UniProt REST API."""
    url = f"https://rest.uniprot.org/uniprotkb/{accession}.fasta"
    response = requests.get(url, timeout=30)
    if response.status_code == 200:
        return response.text
    print(f"Warning: Failed to fetch {accession}: HTTP {response.status_code}", file=sys.stderr)
    return None


def main():
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} <input_fasta> <output_fasta>", file=sys.stderr)
        sys.exit(1)

    input_fasta = Path(sys.argv[1])
    output_fasta = Path(sys.argv[2])

    # Read the input to get the primary accession
    record = next(SeqIO.parse(input_fasta, "fasta"))
    primary_accession = record.id.split("|")[0]

    print(f"Primary sequence: {primary_accession} ({len(record.seq)} aa)")
    print(f"Fetching {len(ORTHOLOGS)} orthologs...")

    sequences = []
    for accession, (species, gene) in ORTHOLOGS.items():
        if accession == primary_accession:
            # Use the local sequence
            sequences.append(f">{accession}|{gene} OS={species}\n{str(record.seq)}\n")
            print(f"  {accession} ({species} {gene}): local [{len(record.seq)} aa]")
            continue

        fasta_text = fetch_uniprot_fasta(accession)
        if fasta_text:
            # Replace the header with a cleaner version
            lines = fasta_text.strip().split("\n")
            seq = "".join(lines[1:])
            sequences.append(f">{accession}|{gene} OS={species}\n{seq}\n")
            print(f"  {accession} ({species} {gene}): fetched [{len(seq)} aa]")
        else:
            print(f"  {accession} ({species} {gene}): FAILED")

        time.sleep(0.5)  # Be polite to UniProt API

    with open(output_fasta, "w") as f:
        f.writelines(sequences)

    print(f"\nWrote {len(sequences)} sequences to {output_fasta}")


if __name__ == "__main__":
    main()
