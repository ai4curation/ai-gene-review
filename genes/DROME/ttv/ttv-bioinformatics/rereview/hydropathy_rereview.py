"""Kyte-Doolittle maximum 19-residue window hydropathy for ttv-PC (D5SHU8) and full-length Ttv (Q9V730).

A window mean >= 1.6 is the classical Kyte & Doolittle threshold for a candidate
transmembrane / signal-anchor segment. Reports the maximum window and its location
for each sequence; no outcome is hardcoded.

Usage: uv run --no-project --with biopython==1.85 python hydropathy_rereview.py
"""

import json
import sys
from pathlib import Path

from Bio import SeqIO

KD = {"A": 1.8, "R": -4.5, "N": -3.5, "D": -3.5, "C": 2.5, "Q": -3.5, "E": -3.5,
      "G": -0.4, "H": -3.2, "I": 4.5, "L": 3.8, "K": -3.9, "M": 1.9, "F": 2.8,
      "P": -1.6, "S": -0.8, "T": -0.7, "W": -0.9, "Y": -1.3, "V": 4.2}
WINDOW = 19
HERE = Path(__file__).parent


def max_window(seq: str, window: int = WINDOW) -> tuple[float, int]:
    """Return (max mean hydropathy, 1-based start) over all windows.

    >>> max_window("IIII", 2)
    (4.5, 1)
    """
    best = (-99.0, 0)
    for i in range(len(seq) - window + 1):
        score = sum(KD[a] for a in seq[i:i + window]) / window
        if score > best[0]:
            best = (round(score, 2), i + 1)
    return best


def main() -> None:
    out = {}
    for acc in ["D5SHU8", "Q9V730"]:
        seq = str(next(SeqIO.parse(HERE / f"{acc}.fasta", "fasta")).seq)
        score, start = max_window(seq)
        out[acc] = {"max_window_mean": score, "window_start": start,
                    "window_seq": seq[start - 1:start - 1 + WINDOW],
                    "candidate_tm_ge_1.6": score >= 1.6}
    json.dump(out, sys.stdout, indent=2)
    print()


if __name__ == "__main__":
    main()
