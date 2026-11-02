# /// script
# requires-python = ">=3.11"
# dependencies = ["biopython==1.85"]
# ///
"""Global alignment of a human UniProt record against the horse UniProt record.

Usage: uv run compare_to_human.py HUMAN.txt HORSE.txt OUT.json [human_pos ...]
Reports identity among paired residues, coverage of each sequence, the human
ranges absent from the horse sequence, and the horse residue aligned to each
requested human position. BLOSUM62, gap open -10, extension -0.5.
Pairwise similarity does not by itself establish orthology or function.
"""
import json, sys
from pathlib import Path
from Bio import Align, SeqIO
from Bio.Align import substitution_matrices


def main():
    h, d, out = map(Path, sys.argv[1:4])
    positions = [int(p) for p in sys.argv[4:]]
    hr, dr = SeqIO.read(h, "swiss"), SeqIO.read(d, "swiss")
    al = Align.PairwiseAligner()
    al.mode = "global"
    al.substitution_matrix = substitution_matrices.load("BLOSUM62")
    al.open_gap_score, al.extend_gap_score = -10, -0.5
    best = al.align(hr.seq, dr.seq)[0]
    x, y = str(best[0]), str(best[1])
    hi = di = 0
    hmap = {}
    gaps = []  # human residues with no horse partner
    for a, b in zip(x, y):
        if a != "-":
            hi += 1
        if b != "-":
            di += 1
        if a != "-":
            hmap[hi] = (b, di if b != "-" else None)
            if b == "-":
                gaps.append(hi)
    ranges = []
    for p in gaps:
        if ranges and p == ranges[-1][1] + 1:
            ranges[-1][1] = p
        else:
            ranges.append([p, p])
    paired = sum(a != "-" and b != "-" for a, b in zip(x, y))
    ident = sum(a == b and a != "-" for a, b in zip(x, y))
    res = dict(
        method="Biopython 1.85 PairwiseAligner global, BLOSUM62, gap open -10, extend -0.5",
        human=dict(accession=hr.id, length=len(hr)),
        horse=dict(accession=dr.id, length=len(dr)),
        paired_residues=paired,
        identical_residues=ident,
        identity_among_paired=round(100 * ident / paired, 2),
        coverage_human=round(100 * paired / len(hr), 2),
        coverage_horse=round(100 * paired / len(dr), 2),
        human_ranges_without_horse_partner=[r for r in ranges if r[1] - r[0] >= 4],
        checked_positions={str(p): dict(human=str(hr.seq[p - 1]), horse=hmap[p][0], horse_pos=hmap[p][1]) for p in positions},
        alignment=str(best),
    )
    out.write_text(json.dumps(res, indent=2) + "\n")
    print(json.dumps({k: v for k, v in res.items() if k != "alignment"}, indent=2))


if __name__ == "__main__":
    main()
