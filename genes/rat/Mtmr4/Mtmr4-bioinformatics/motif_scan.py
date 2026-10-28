"""Scan the rat Mtmr4 (A0A8I6A3Q2) UniProt sequence for functional motifs.

Usage: python3 motif_scan.py ../Mtmr4-uniprot.txt
Reports the myotubularin CX5R catalytic loop, the FYVE R(R/K)HHCR PI3P-binding
signature, PY (PPxY) motifs and GPPxxxY (CEP55-binding, ESCRT-I like) motifs.
"""
import re
import sys


def read_seq(path):
    txt = open(path).read()
    body = txt.split("\nSQ   SEQUENCE", 1)[1].split("\n", 1)[1].split("//")[0]
    return re.sub(r"[^A-Z]", "", body)


MOTIFS = {
    "CX5R catalytic loop (C.{5}R)": r"C.{5}R",
    "PTP active-site HCxxGxxR(T/S)": r"HC..G..R[TS]",
    "FYVE PI3P-binding R(R/K)HHCR": r"R[RK]HHCR",
    "PY motif PPxY": r"PP.Y",
    "GPPxxxY CEP55-binding motif": r"GPP...Y",
}


def main(path):
    seq = read_seq(path)
    print(f"sequence length: {len(seq)}")
    for name, pat in MOTIFS.items():
        hits = [(m.start() + 1, m.group()) for m in re.finditer(pat, seq)]
        if name.startswith("CX5R"):
            # report only hits inside the annotated phosphatase domain (153-570)
            hits = [h for h in hits if 153 <= h[0] <= 570]
        print(f"{name}: {hits if hits else 'none'}")
    print(f"residue 407: {seq[406]}")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "../Mtmr4-uniprot.txt")
