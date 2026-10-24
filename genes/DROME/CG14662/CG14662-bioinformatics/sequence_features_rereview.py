"""Sequence-feature analysis of Q9VN74 (CG14662) for the full re-review.

Reads the sequence from the cached UniProt flat file and reports:
- N-terminal charge before the first predicted hydrophobic segment (positive-inside rule)
- Kyte-Doolittle hydrophobic windows (19 aa, threshold 1.6)
- N-glycosylation sequons (N-X-S/T, X != P)
- Ser/Thr and Cys content per region
- Leucine-rich repeat-like LxxLxLxxN/C motifs
Usage: uv run --no-project python sequence_features_rereview.py
"""
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
UNIPROT = HERE.parent / "CG14662-uniprot.txt"

KD = {"A": 1.8, "R": -4.5, "N": -3.5, "D": -3.5, "C": 2.5, "Q": -3.5, "E": -3.5, "G": -0.4,
      "H": -3.2, "I": 4.5, "L": 3.8, "K": -3.9, "M": 1.9, "F": 2.8, "P": -1.6, "S": -0.8,
      "T": -0.7, "W": -0.9, "Y": -1.3, "V": 4.2}


def read_seq(path: Path) -> str:
    lines = path.read_text().splitlines()
    i = next(n for n, l in enumerate(lines) if l.startswith("SQ   "))
    seq = "".join(l.strip().replace(" ", "") for l in lines[i + 1:] if not l.startswith("//"))
    return seq


def hydrophobic_windows(seq: str, w: int = 19, thr: float = 1.6):
    scores = [sum(KD[a] for a in seq[i:i + w]) / w for i in range(len(seq) - w + 1)]
    segs, start = [], None
    for i, s in enumerate(scores):
        if s >= thr and start is None:
            start = i
        if s < thr and start is not None:
            segs.append((start + 1, i + w - 1, round(max(scores[start:i]), 2)))
            start = None
    if start is not None:
        segs.append((start + 1, len(seq), round(max(scores[start:]), 2)))
    return segs


def region_stats(seq: str, a: int, b: int):
    r = seq[a - 1:b]
    return {"region": f"{a}-{b}", "len": len(r),
            "ST_frac": round((r.count("S") + r.count("T")) / len(r), 2),
            "C_count": r.count("C"),
            "KR": r.count("K") + r.count("R"), "DE": r.count("D") + r.count("E")}


def main():
    seq = read_seq(UNIPROT)
    print("length", len(seq))
    print("hydrophobic windows (start,end,max_KD):", hydrophobic_windows(seq))
    sequons = [m.start() + 1 for m in re.finditer(r"(?=N[^P][ST])", seq)]
    print("N-glyc sequons (N position):", sequons)
    for a, b in [(1, 28), (51, 290), (291, 336), (337, 420), (448, 550)]:
        print(region_stats(seq, a, b))
    lrr = [(m.start() + 1, m.group()) for m in re.finditer(r"L..L.L..[NC]", seq)]
    print("LxxLxLxxN/C motifs:", lrr)
    tail = seq[447:]
    print("tyrosine motifs YxxL/I/V/F in C-terminal tail:",
          [(m.start() + 448, m.group(1)) for m in re.finditer(r"(?=(Y..[LIVF]))", tail)])


if __name__ == "__main__":
    main()
