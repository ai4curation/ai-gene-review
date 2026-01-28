#!/usr/bin/env python3
"""Search for a peptide sequence in translated transcript sequences.

This script translates nucleotide transcripts in three frames and searches for
exact or near-exact peptide matches.
"""

from __future__ import annotations

import argparse
import gzip
from pathlib import Path
from typing import Dict, Iterable, Iterator, Tuple

CODON_TABLE: Dict[str, str] = {
    "TTT": "F", "TTC": "F", "TTA": "L", "TTG": "L",
    "TCT": "S", "TCC": "S", "TCA": "S", "TCG": "S",
    "TAT": "Y", "TAC": "Y", "TAA": "*", "TAG": "*",
    "TGT": "C", "TGC": "C", "TGA": "*", "TGG": "W",
    "CTT": "L", "CTC": "L", "CTA": "L", "CTG": "L",
    "CCT": "P", "CCC": "P", "CCA": "P", "CCG": "P",
    "CAT": "H", "CAC": "H", "CAA": "Q", "CAG": "Q",
    "CGT": "R", "CGC": "R", "CGA": "R", "CGG": "R",
    "ATT": "I", "ATC": "I", "ATA": "I", "ATG": "M",
    "ACT": "T", "ACC": "T", "ACA": "T", "ACG": "T",
    "AAT": "N", "AAC": "N", "AAA": "K", "AAG": "K",
    "AGT": "S", "AGC": "S", "AGA": "R", "AGG": "R",
    "GTT": "V", "GTC": "V", "GTA": "V", "GTG": "V",
    "GCT": "A", "GCC": "A", "GCA": "A", "GCG": "A",
    "GAT": "D", "GAC": "D", "GAA": "E", "GAG": "E",
    "GGT": "G", "GGC": "G", "GGA": "G", "GGG": "G",
}


def read_fasta(path: Path) -> Iterator[Tuple[str, str]]:
    opener = gzip.open if path.suffix == ".gz" else open
    with opener(path, "rt") as handle:
        header = None
        seq_parts = []
        for line in handle:
            line = line.strip()
            if not line:
                continue
            if line.startswith(">"):
                if header:
                    yield header, "".join(seq_parts).upper().replace("U", "T")
                header = line[1:].split()[0]
                seq_parts = []
            else:
                seq_parts.append(line)
        if header:
            yield header, "".join(seq_parts).upper().replace("U", "T")


def translate(seq: str, frame: int) -> str:
    aa = []
    for idx in range(frame, len(seq) - 2, 3):
        codon = seq[idx:idx + 3]
        aa.append(CODON_TABLE.get(codon, "X"))
    return "".join(aa)


def find_matches(aa_seq: str, peptide: str, max_mismatch: int) -> Iterable[Tuple[int, int, str]]:
    pep_len = len(peptide)
    if pep_len == 0:
        return []
    matches = []
    if max_mismatch == 0:
        start = aa_seq.find(peptide)
        while start != -1:
            matches.append((start, 0, peptide))
            start = aa_seq.find(peptide, start + 1)
        return matches

    for start in range(0, len(aa_seq) - pep_len + 1):
        window = aa_seq[start:start + pep_len]
        if "*" in window:
            continue
        mismatches = sum(1 for a, b in zip(window, peptide) if a != b)
        if mismatches <= max_mismatch:
            matches.append((start, mismatches, window))
    return matches


def load_peptide(peptide: str | None, peptide_fasta: Path | None) -> str:
    if peptide:
        return peptide.strip().upper()
    if peptide_fasta:
        for _, seq in read_fasta(peptide_fasta):
            return seq.strip().upper()
    raise ValueError("Provide --peptide or --peptide-fasta")


def main() -> None:
    parser = argparse.ArgumentParser(description="Search peptide in translated transcripts.")
    parser.add_argument("--rna-fasta", required=True, type=Path)
    parser.add_argument("--peptide", help="Peptide sequence (AA)")
    parser.add_argument("--peptide-fasta", type=Path, help="FASTA with peptide sequence")
    parser.add_argument("--max-mismatch", type=int, default=0)
    parser.add_argument("--out-tsv", required=True, type=Path)
    args = parser.parse_args()

    peptide = load_peptide(args.peptide, args.peptide_fasta)
    pep_len = len(peptide)
    args.out_tsv.parent.mkdir(parents=True, exist_ok=True)

    total_transcripts = 0
    total_hits = 0

    with args.out_tsv.open("w") as out:
        out.write("transcript_id\tframe\tstart_nt\tstart_aa\tmismatches\tpeptide\twindow\n")
        for transcript_id, nt_seq in read_fasta(args.rna_fasta):
            total_transcripts += 1
            for frame in (0, 1, 2):
                aa_seq = translate(nt_seq, frame)
                for start_aa, mismatches, window in find_matches(aa_seq, peptide, args.max_mismatch):
                    start_nt = frame + start_aa * 3
                    out.write(
                        f"{transcript_id}\t{frame}\t{start_nt}\t{start_aa}\t{mismatches}\t{peptide}\t{window}\n"
                    )
                    total_hits += 1

    print(f"Processed transcripts: {total_transcripts}")
    print(f"Peptide length: {pep_len}")
    print(f"Total hits: {total_hits}")


if __name__ == "__main__":
    main()
