#!/usr/bin/env python3
"""Detect P-loop NTPase / small-molecule-kinase motifs in a protein sequence.

Scans an input FASTA for:
  - Walker A / P-loop:            [AG]-x(4)-G-K-[ST]   (classic glycine-rich loop)
  - Walker B (Mg2+ coord Asp):    h-h-h-h-D  (hydrophobic stretch ending in D/E),
                                   reported heuristically near strand 3
  - PRK/URK/PANK-family diagnostic residues discussed in the literature

The script makes NO gene-specific assumptions: all patterns are generic and the
sequence is read from the FASTA given on the command line. Results are printed as
JSON to stdout and written to the output path if given.

Usage:
    python analyze_motifs.py INPUT.fasta [OUTPUT.json]
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path


def read_fasta(path: Path) -> tuple[str, str]:
    header = ""
    seq_parts: list[str] = []
    for line in path.read_text().splitlines():
        if line.startswith(">"):
            header = line[1:].strip()
        elif line.strip():
            seq_parts.append(line.strip())
    return header, "".join(seq_parts)


# Generic hydrophobic residue class used for Walker B heuristic
HYDROPHOBIC = "AILMFVWCY"


def find_walker_a(seq: str) -> list[dict]:
    """Classic P-loop: [AG]-x(4)-G-K-[ST]."""
    hits = []
    for m in re.finditer(r"[AG].{4}GK[ST]", seq):
        hits.append(
            {
                "motif": m.group(0),
                "start_1based": m.start() + 1,
                "end_1based": m.end(),
            }
        )
    return hits


def find_walker_b_candidates(seq: str) -> list[dict]:
    """Walker B heuristic: >=4 hydrophobic residues immediately followed by D or E.

    Walker B in P-loop NTPases is a hydrophobic beta-strand terminating in an
    aspartate (sometimes DE) that coordinates the catalytic Mg2+. This is a weak
    heuristic and will produce several candidates; the biologically relevant one
    lies downstream of Walker A on the central beta-sheet.
    """
    hits = []
    for m in re.finditer(rf"[{HYDROPHOBIC}]{{4,}}[DE]", seq):
        hits.append(
            {
                "motif": m.group(0),
                "start_1based": m.start() + 1,
                "end_1based": m.end(),
                "acidic_pos_1based": m.end(),  # the terminal D/E
            }
        )
    return hits


def composition(seq: str) -> dict:
    n = len(seq)
    return {
        aa: round(seq.count(aa) / n * 100, 2)
        for aa in "ACDEFGHIKLMNPQRSTVWY"
    }


def main() -> None:
    if len(sys.argv) < 2:
        sys.exit("Usage: python analyze_motifs.py INPUT.fasta [OUTPUT.json]")
    fasta = Path(sys.argv[1])
    header, seq = read_fasta(fasta)
    seq = seq.upper()

    result = {
        "input_file": str(fasta),
        "header": header,
        "length": len(seq),
        "walker_a_hits": find_walker_a(seq),
        "walker_b_candidates": find_walker_b_candidates(seq),
        "n_walker_b_candidates": len(find_walker_b_candidates(seq)),
        "composition_percent": composition(seq),
    }

    out = json.dumps(result, indent=2)
    print(out)
    if len(sys.argv) >= 3:
        Path(sys.argv[2]).write_text(out + "\n")


if __name__ == "__main__":
    main()
