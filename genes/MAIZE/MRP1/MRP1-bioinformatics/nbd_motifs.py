"""Locate ABC nucleotide-binding-domain motifs in the MRP1 (Q6Y3I1) sequence.

Reads the sequence from the cached UniProt flat file and reports Walker A,
ABC signature and Walker B motif matches, plus the residue that follows the
Walker B hydrophobic stretch (catalytic E in a consensus site, D/other in a
degenerate site). Usage: python nbd_motifs.py ../MRP1-uniprot.txt
"""
import re
import sys


def read_seq(path):
    text = open(path).read()
    block = text.split("\nSQ ")[1].split("\n", 1)[1]
    return "".join(c for c in block if c.isalpha())


def main(path):
    s = read_seq(path)
    print(f"length\t{len(s)}")
    patterns = {
        "walker_A": r"G..G.GK[ST]",
        "abc_signature": r"[LIVMFYW]S[AG]GQ",
        "walker_B": r"[ILVMFY]{4}D[DE]",
    }
    for name, pat in patterns.items():
        for m in re.finditer(pat, s):
            print(f"{name}\t{m.start() + 1}-{m.end()}\t{m.group()}")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "../MRP1-uniprot.txt")
