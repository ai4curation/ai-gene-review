#!/usr/bin/env python3
"""Compare PRK/URK/PANK-family diagnostic motifs across two or more FASTA files.

The PRK/URK/PANK (phosphoribulokinase / uridine kinase / pantothenate kinase)
small-molecule kinases carry two diagnostic sequence blocks:
  (1) the Walker A / P-loop  [AG]-x(4)-G-K-[ST]   (ATP phosphate binding)
  (2) a second conserved  [IV]-[IV]-[IL]-E-G  block on a downstream beta-strand
      (the family's characteristic nucleotide/substrate-region signature,
       e.g. the '(I/V)ILEG' seen in uridine kinases)

Given several FASTA files, report the presence/position of each block so the
target can be compared against a known family member. No gene-specific values
are hardcoded; every sequence comes from a file argument.

Usage:
    python compare_urk_motifs.py TARGET.fasta REFERENCE.fasta [MORE.fasta ...]
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

WALKER_A = re.compile(r"[AG].{4}GK[ST]")
URK_BLOCK2 = re.compile(r"[IV][IV][IL]EG")


def read_fasta(path: Path) -> tuple[str, str]:
    header, parts = "", []
    for line in path.read_text().splitlines():
        if line.startswith(">"):
            header = line[1:].strip()
        elif line.strip():
            parts.append(line.strip())
    return header, "".join(parts).upper()


def scan(seq: str) -> dict:
    wa = WALKER_A.search(seq)
    b2 = URK_BLOCK2.search(seq)
    return {
        "walker_a": {"motif": wa.group(0), "start_1based": wa.start() + 1}
        if wa
        else None,
        "urk_block2": {"motif": b2.group(0), "start_1based": b2.start() + 1}
        if b2
        else None,
    }


def main() -> None:
    if len(sys.argv) < 2:
        sys.exit("Usage: python compare_urk_motifs.py FASTA1 [FASTA2 ...]")
    out = {}
    for arg in sys.argv[1:]:
        p = Path(arg)
        header, seq = read_fasta(p)
        out[p.name] = {"header": header, "length": len(seq), **scan(seq)}
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
