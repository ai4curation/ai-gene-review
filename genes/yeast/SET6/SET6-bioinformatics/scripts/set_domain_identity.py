#!/usr/bin/env python3
"""Pairwise identity of SET6 vs panel, restricted to the SET-domain columns.

Full-length global identity is misleading here because the panel proteins have very
different N/C-terminal extensions (SET1 is 1080 aa, etc.). This script restricts the
comparison to the alignment columns spanning the SET domain, defined by the SET6
SET-domain boundary (UniProt: residues 12-338).

Uses the existing MAFFT MSA (panel_mafft.aln.fasta). No conclusions hardcoded.
"""
from __future__ import annotations

import sys
from pathlib import Path

from Bio import AlignIO

HERE = Path(__file__).resolve().parent
PROJ = HERE.parent
RESULTS = PROJ / "results"

# SET6 SET-domain boundary per UniProt Q12529 feature table.
SET6_DOMAIN_START = 12
SET6_DOMAIN_END = 338


def main() -> int:
    aln = AlignIO.read(RESULTS / "panel_mafft.aln.fasta", "fasta")
    by_id = {rec.id: str(rec.seq) for rec in aln}
    set6_id = [i for i in by_id if i.startswith("Q12529")][0]
    set6_aln = by_id[set6_id]

    # Map SET6 ungapped residue index (1-based) -> alignment column
    res_to_col = {}
    r = 0
    for col, ch in enumerate(set6_aln):
        if ch not in "-.":
            r += 1
            res_to_col[r] = col
    start_col = res_to_col[SET6_DOMAIN_START]
    end_col = res_to_col[SET6_DOMAIN_END]

    cols = range(start_col, end_col + 1)

    lines = ["# SET-domain-restricted pairwise identity: SET6 vs panel", "",
             f"SET6 SET domain = residues {SET6_DOMAIN_START}-{SET6_DOMAIN_END} "
             f"(alignment cols {start_col}-{end_col})", "",
             f"{'protein':22s} {'%id_setdom':>10s} {'ident':>6s} {'aligned_positions':>17s}"]

    results = []
    for rid, seq in by_id.items():
        if rid == set6_id:
            continue
        idents = 0
        aligned = 0
        for c in cols:
            a = set6_aln[c]
            b = seq[c]
            if a not in "-." and b not in "-.":
                aligned += 1
                if a == b:
                    idents += 1
        pid = 100.0 * idents / aligned if aligned else 0.0
        results.append((pid, rid, idents, aligned))

    for pid, rid, idents, aligned in sorted(results, reverse=True):
        lines.append(f"{rid:22s} {pid:10.1f} {idents:6d} {aligned:17d}")

    text = "\n".join(lines) + "\n"
    (RESULTS / "set_domain_identity.txt").write_text(text)
    print(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
