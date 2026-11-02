#!/usr/bin/env python3
"""Check whether the CcmC heme-binding residues characterised in Escherichia coli
are present, and positionally equivalent, in Shewanella oneidensis MR-1 CcmC.

What is checked
---------------
The WWD domain and its two flanking external histidines (His60, His184 in the
E. coli numbering) are the experimentally defined heme-binding site of CcmC
(PMID:20599545). This script performs a global pairwise alignment of
UniProtKB:Q8EK42 (CCMC_SHEON, the protein under review) against
UniProtKB:P0ABM1 (CCMC_ECOLI) and reports, for each E. coli landmark, the
residue and position it aligns to in Q8EK42.

Nothing here is hardcoded: positions and identities are read off the computed
alignment, and the script reports a mismatch rather than asserting conservation.

Usage
-----
    uv run python align_wwd_domain.py            # fetch both sequences from UniProt
    uv run python align_wwd_domain.py > report.txt

Sequences are fetched from the UniProt REST API. Q8EK42 is cross-checked against
the committed flat file ../ccmC-uniprot.txt when that file is present, so the
analysis cannot silently drift from the sequence the review cites.
"""

from __future__ import annotations

import re
import sys
import urllib.request
from pathlib import Path

from Bio import Align
from Bio.Align import substitution_matrices

ECOLI = "P0ABM1"
SHEON = "Q8EK42"

# Landmarks are given in the E. coli numbering, which is how the literature
# states them; the script maps them onto Q8EK42 rather than assuming a mapping.
HIS_LANDMARKS = (60, 184)
WWD_PATTERN = "WW.WD"


def fetch(accession: str) -> str:
    url = f"https://rest.uniprot.org/uniprotkb/{accession}.fasta"
    with urllib.request.urlopen(url, timeout=60) as fh:
        text = fh.read().decode()
    seq = "".join(line.strip() for line in text.splitlines() if not line.startswith(">"))
    if not seq:
        raise SystemExit(f"no sequence returned for {accession}")
    return seq


def sequence_from_flatfile(path: Path) -> str | None:
    """Pull the SQ block out of a UniProt flat file, if it is available."""
    if not path.exists():
        return None
    lines = path.read_text().splitlines()
    try:
        start = next(i for i, line in enumerate(lines) if line.startswith("SQ   "))
    except StopIteration:
        return None
    out = []
    for line in lines[start + 1 :]:
        if line.startswith("//"):
            break
        out.append(line.replace(" ", ""))
    return "".join(out) or None


def build_aligner() -> Align.PairwiseAligner:
    aligner = Align.PairwiseAligner()
    aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
    aligner.open_gap_score = -11
    aligner.extend_gap_score = -1
    aligner.mode = "global"
    return aligner


def column_map(alignment) -> dict[int, int | None]:
    """Map 1-based target (E. coli) positions to 1-based query (MR-1) positions."""
    mapping: dict[int, int | None] = {}
    a_idx = b_idx = 0
    a_aln, b_aln = alignment[0], alignment[1]
    for a_char, b_char in zip(a_aln, b_aln):
        if a_char != "-":
            a_idx += 1
        if b_char != "-":
            b_idx += 1
        if a_char != "-":
            mapping[a_idx] = b_idx if b_char != "-" else None
    return mapping


def main() -> int:
    ecoli = fetch(ECOLI)
    sheon = fetch(SHEON)

    flat = sequence_from_flatfile(Path(__file__).resolve().parent.parent / "ccmC-uniprot.txt")
    if flat is None:
        print("NOTE: ../ccmC-uniprot.txt not found; skipping flat-file cross-check")
    elif flat != sheon:
        print("ERROR: fetched Q8EK42 sequence differs from the committed flat file")
        return 1
    else:
        print("Flat-file cross-check: fetched Q8EK42 matches ../ccmC-uniprot.txt SQ block")

    print(f"{ECOLI} (CCMC_ECOLI): {len(ecoli)} aa")
    print(f"{SHEON} (CCMC_SHEON): {len(sheon)} aa")

    aligner = build_aligner()
    alignment = aligner.align(ecoli, sheon)[0]
    identities = sum(1 for a, b in zip(alignment[0], alignment[1]) if a == b and a != "-")
    aligned_cols = sum(1 for a, b in zip(alignment[0], alignment[1]) if a != "-" and b != "-")
    print(f"Global alignment: score {alignment.score:.1f}, "
          f"{identities}/{aligned_cols} identical in aligned columns "
          f"({100.0 * identities / aligned_cols:.1f}% identity)")

    mapping = column_map(alignment)

    print("\nAxial histidine landmarks (E. coli numbering -> Q8EK42):")
    for pos in HIS_LANDMARKS:
        target_res = ecoli[pos - 1]
        mapped = mapping.get(pos)
        if mapped is None:
            print(f"  His{pos} ({target_res}) -> aligned to a gap in Q8EK42: NOT CONSERVED")
            continue
        query_res = sheon[mapped - 1]
        verdict = "conserved" if query_res == target_res else "NOT CONSERVED"
        print(f"  {target_res}{pos} -> {query_res}{mapped} in Q8EK42: {verdict}")

    print("\nWWD motif:")
    for name, seq in ((ECOLI, ecoli), (SHEON, sheon)):
        hits = [(m.start() + 1, m.group()) for m in re.finditer(WWD_PATTERN, seq)]
        if not hits:
            print(f"  {name}: no {WWD_PATTERN} match")
        for start, motif in hits:
            print(f"  {name}: {motif} at {start}-{start + len(motif) - 1}")
    ec_hits = [m.start() + 1 for m in re.finditer(WWD_PATTERN, ecoli)]
    for start in ec_hits:
        mapped = [mapping.get(start + i) for i in range(5)]
        print(f"  E. coli {start}-{start + 4} aligns to Q8EK42 positions {mapped}")

    print("\nAlignment around each landmark (E. coli / Q8EK42, aligned columns):")
    a_aln, b_aln = str(alignment[0]), str(alignment[1])
    a_idx = 0
    col_of: dict[int, int] = {}
    for col, char in enumerate(a_aln):
        if char != "-":
            a_idx += 1
            col_of[a_idx] = col
    for label, pos in (("His60", 60), ("WWD", 122), ("His184", 184)):
        col = col_of[pos]
        lo, hi = max(0, col - 8), min(len(a_aln), col + 9)
        print(f"  {label:7s} {a_aln[lo:hi]}")
        print(f"  {'':7s} {b_aln[lo:hi]}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
