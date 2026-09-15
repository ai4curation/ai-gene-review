#!/usr/bin/env python3
"""Compare KT2440 AstA chains with characterized P. aeruginosa subunits."""

from io import TextIOWrapper
from urllib.request import urlopen

from Bio import Align, SeqIO


ACCESSIONS = {
    "PSEPK AstA-I": "Q88EI3",
    "PSEPK AstA-II": "Q88EI2",
    "P. aeruginosa alpha AruF": "P80357",
    "P. aeruginosa beta AruG": "P80358",
}


def fetch_sequence(accession: str):
    url = f"https://rest.uniprot.org/uniprotkb/{accession}.fasta"
    with urlopen(url) as response:  # noqa: S310 - fixed UniProt HTTPS endpoint
        return SeqIO.read(TextIOWrapper(response), "fasta").seq


def identity(query, target):
    aligner = Align.PairwiseAligner()
    aligner.mode = "global"
    aligner.match_score = 1
    aligner.mismatch_score = 0
    aligner.open_gap_score = -1
    aligner.extend_gap_score = -0.1
    alignment = aligner.align(query, target)[0]
    counts = alignment.counts()
    aligned_residues = counts.identities + counts.mismatches
    return counts.identities, aligned_residues, 100 * counts.identities / aligned_residues


def main():
    sequences = {name: fetch_sequence(accession) for name, accession in ACCESSIONS.items()}
    print("query\ttarget\tidentical\taligned_residues\tpercent_identity")
    for query in ("PSEPK AstA-I", "PSEPK AstA-II"):
        for target in ("P. aeruginosa alpha AruF", "P. aeruginosa beta AruG"):
            identical, aligned, percent = identity(sequences[query], sequences[target])
            print(f"{query}\t{target}\t{identical}\t{aligned}\t{percent:.1f}")


if __name__ == "__main__":
    main()
