#!/usr/bin/env python3
"""Count CXXCH c-type heme-binding motifs in the CbcL sequence.

The sequence is read out of the committed UniProt flat file
(genes/GEOSL/cbcL/cbcL-uniprot.txt) so the scan needs no network access and no
dependencies beyond the standard library.

Usage (from the repository root):
    python genes/GEOSL/cbcL/cbcL-bioinformatics/cxxch_scan.py

The expected sequence is pinned: the script recomputes the UniProt CRC64 of the
residues it parsed and compares it, and the length, against EXPECTED_CRC64 and
EXPECTED_LENGTH below. A refetch that changes the entry's sequence therefore
fails loudly instead of silently desynchronising RESULTS.md, which records the
same pinned values. If it fails, re-run the scan and update RESULTS.md and the
pins from the new output rather than editing the table by hand.

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

# UniProtKB:Q74GH2, sequence version as committed in cbcL-uniprot.txt.
EXPECTED_LENGTH = 619
EXPECTED_CRC64 = "12CE553CC08B6BA0"

# CRC64 as UniProt computes it: ISO 3309, reflected, POLY64REV.
_POLY64REV = 0xD800000000000000


def _crc64_table() -> list[int]:
    table = []
    for byte in range(256):
        crc = byte
        for _ in range(8):
            crc = (crc >> 1) ^ _POLY64REV if crc & 1 else crc >> 1
        table.append(crc)
    return table


_CRC64_TABLE = _crc64_table()


def crc64(sequence: str) -> str:
    """Return the UniProt-style CRC64 of a sequence, as 16 uppercase hex digits."""
    crc = 0
    for char in sequence.encode("ascii"):
        crc = _CRC64_TABLE[(crc ^ char) & 0xFF] ^ (crc >> 8)
    return f"{crc:016X}"


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


def check_sequence(seq: str) -> str:
    """Fail unless the parsed sequence is the one this analysis was run on."""
    observed = crc64(seq)
    problems = []
    if len(seq) != EXPECTED_LENGTH:
        problems.append(f"length {len(seq)}, expected {EXPECTED_LENGTH}")
    if observed != EXPECTED_CRC64:
        problems.append(f"CRC64 {observed}, expected {EXPECTED_CRC64}")
    if problems:
        raise SystemExit(
            "the sequence in "
            f"{UNIPROT_FILE} is not the pinned one ({'; '.join(problems)}). "
            "Re-run this scan and update RESULTS.md and the pins from its output."
        )
    return observed


def main() -> int:
    seq = read_sequence(UNIPROT_FILE)
    observed_crc = check_sequence(seq)
    hits = [(m.start() + 1, m.group(1)) for m in MOTIF.finditer(seq)]
    print(f"source: {UNIPROT_FILE}")
    print(f"sequence length: {len(seq)} (pinned {EXPECTED_LENGTH})")
    print(f"sequence CRC64: {observed_crc} (pinned {EXPECTED_CRC64})")
    print(f"CXXCH motifs found: {len(hits)}")
    for pos, motif in hits:
        print(f"  {pos}\t{motif}")
    if hits:
        first = hits[0][0]
        last = hits[-1][0] + len(hits[-1][1]) - 1
        print(f"motif span: residues {first}-{last}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
