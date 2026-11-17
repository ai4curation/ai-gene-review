#!/usr/bin/env python3
"""Characterise the alternatively spliced segment of ple (P18459, residues 60-130).

Reads the cached UniProt flat file (../ple-uniprot.txt), extracts the displayed
sequence, and reports the length, acidic/basic residue counts and average
molecular masses of the two UniProt isoforms (displayed, and VSP_000545 which
lacks residues 60-130). Standard library only.

Usage: python isoform_insert.py [path/to/ple-uniprot.txt]
"""
import sys
from pathlib import Path

# Average residue masses (Da), water added once per chain.
AVG = {"A": 71.0788, "R": 156.1875, "N": 114.1038, "D": 115.0886, "C": 103.1388,
       "E": 129.1155, "Q": 128.1307, "G": 57.0519, "H": 137.1411, "I": 113.1594,
       "L": 113.1594, "K": 128.1741, "M": 131.1926, "F": 147.1766, "P": 97.1167,
       "S": 87.0782, "T": 101.1051, "W": 186.2132, "Y": 163.1760, "V": 99.1326}


def mass(seq: str) -> float:
    return sum(AVG[a] for a in seq) + 18.015


def main() -> None:
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parent.parent / "ple-uniprot.txt"
    text = path.read_text()
    sq = text.split("\nSQ ", 1)[1].split("\n", 1)[1].split("//")[0]
    seq = "".join(sq.split())
    seg = seq[59:130]
    short = seq[:59] + seq[130:]
    print(f"displayed isoform: {len(seq)} aa, {mass(seq):.0f} Da")
    print(f"VSP_000545 isoform (lacks 60-130): {len(short)} aa, {mass(short):.0f} Da")
    print(f"segment 60-130: {len(seg)} aa: {seg}")
    acid = sum(seg.count(c) for c in "DE")
    base = sum(seg.count(c) for c in "KR")
    print(f"segment D+E = {acid} ({acid/len(seg):.0%}), K+R = {base}")
    rest_acid = sum(short.count(c) for c in "DE") / len(short)
    print(f"rest of protein D+E fraction = {rest_acid:.0%}")


if __name__ == "__main__":
    main()
