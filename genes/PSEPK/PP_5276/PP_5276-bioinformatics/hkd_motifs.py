"""Scan UniProt flat-file sequences for the PLD-superfamily HxK(x4)D catalytic motif.

Usage: python hkd_motifs.py <uniprot.txt> [<uniprot.txt> ...]
Prints each motif match with its 1-based start position. No results are hardcoded.
"""
import re
import sys


def read_sequence(path: str) -> str:
    text = open(path).read()
    block = text.split("\nSQ ", 1)[1].split("\n", 1)[1].split("//", 1)[0]
    return re.sub(r"[^A-Z]", "", block)


for path in sys.argv[1:]:
    seq = read_sequence(path)
    hits = [(m.start() + 1, m.group()) for m in re.finditer(r"H.K.{4}D", seq)]
    print(f"{path}\tlength={len(seq)}\t" + "; ".join(f"{pos}:{motif}" for pos, motif in hits))
