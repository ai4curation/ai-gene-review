#!/usr/bin/env python3
"""Count CXXCH c-type heme-binding motifs in the CbcL sequence.

The sequence is read out of the committed UniProt flat file
(genes/GEOSL/cbcL/cbcL-uniprot.txt) so the scan needs no network access and no
dependencies beyond the standard library.

Usage (from the repository root):
    python genes/GEOSL/cbcL/cbcL-bioinformatics/cxxch_scan.py

Overlapping matches are reported: CXXCH motifs in multiheme cytochromes can
share a cysteine, so the scan uses a lookahead rather than re.finditer's
non-overlapping default. Positions are 1-based, at the first C of the motif.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

UNIPROT_FILE = Path(__file__).resolve().parent.parent / "cbcL-uniprot.txt"
MOTIF = re.compile(r"(?=(C..CH))")


def read_sequence(path: Path) -> str:
    """Return the amino-acid sequence from a UniProt flat file."""
    lines = path.read_text().splitlines()
    try:
        start = next(i for i, line in enumerate(lines) if line.startswith("SQ   "))
    except StopIteration:
        raise SystemExit(f"no SQ line found in {path}")
    residues = []
    for line in lines[start + 1 :]:
        if line.startswith("//"):
            break
        residues.append(line.replace(" ", ""))
    return "".join(residues)


def main() -> int:
    seq = read_sequence(UNIPROT_FILE)
    hits = [(m.start() + 1, m.group(1)) for m in MOTIF.finditer(seq)]
    print(f"source: {UNIPROT_FILE}")
    print(f"sequence length: {len(seq)}")
    print(f"CXXCH motifs found: {len(hits)}")
    for pos, motif in hits:
        print(f"  {pos}\t{motif}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
