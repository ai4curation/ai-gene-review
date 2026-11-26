# /// script
# requires-python = ">=3.11"
# dependencies = ["biopython==1.85"]
# ///
"""Global alignment of horse ATG3 A0A3Q2L0A4 against reviewed human ATG3 (Q9NT62),
plus a check of which other horse ATG3 UniProt models carry the same segments.

Usage:
    uv run --script compare_horse_human.py human-Q9NT62-uniprot.txt ../ATG3-uniprot.txt \
        horse-other-ATG3-entries.fasta alignment.json 4 5 104 105 108 166 169 264

Reports identity among paired residues, coverage of each sequence, horse segments
with no human partner (insertions), human segments with no horse partner, the horse
residue aligned to each requested human position, and for each other horse model
whether it contains each horse insertion and the canonical human C-terminal peptide.
BLOSUM62, gap open -10, extension -0.5. Similarity does not by itself establish orthology.
"""
import json
import sys
from pathlib import Path

from Bio import Align, SeqIO
from Bio.Align import substitution_matrices


def runs(positions):
    out = []
    for p in positions:
        if out and p == out[-1][1] + 1:
            out[-1][1] = p
        else:
            out.append([p, p])
    return out


def main():
    h, q, others, out = map(Path, sys.argv[1:5])
    positions = [int(p) for p in sys.argv[5:]]
    hr, qr = SeqIO.read(h, "swiss"), SeqIO.read(q, "swiss")
    hs, qs = str(hr.seq), str(qr.seq)
    al = Align.PairwiseAligner()
    al.mode = "global"
    al.substitution_matrix = substitution_matrices.load("BLOSUM62")
    al.open_gap_score, al.extend_gap_score = -10, -0.5
    best = al.align(hs, qs)[0]
    x, y = str(best[0]), str(best[1])
    hi = qi = 0
    hmap, human_gaps, horse_ins = {}, [], []
    for a, b in zip(x, y):
        if a != "-":
            hi += 1
        if b != "-":
            qi += 1
        if a != "-":
            hmap[hi] = (b, qi if b != "-" else None)
            if b == "-":
                human_gaps.append(hi)
        elif b != "-":
            horse_ins.append(qi)
    paired = sum(a != "-" and b != "-" for a, b in zip(x, y))
    ident = sum(a == b and a != "-" for a, b in zip(x, y))
    ins = [
        dict(horse_start=s, horse_end=e, length=e - s + 1, segment=qs[s - 1 : e])
        for s, e in runs(horse_ins)
    ]
    human_cterm = hs[-25:]
    other_models = {}
    for rec in SeqIO.parse(others, "fasta"):
        acc = rec.id.split("|")[1]
        s = str(rec.seq)
        other_models[acc] = dict(
            length=len(s),
            contains_insertions=[i["segment"] in s for i in ins],
            contains_human_canonical_cterm_25aa=human_cterm in s,
        )
    res = dict(
        method="Biopython 1.85 PairwiseAligner global, BLOSUM62, gap open -10, extend -0.5",
        human=dict(accession=hr.id, length=len(hs)),
        horse=dict(accession=qr.id, length=len(qs)),
        paired_residues=paired,
        identical_residues=ident,
        identity_among_paired=round(100 * ident / paired, 2),
        coverage_human=round(100 * paired / len(hs), 2),
        coverage_horse=round(100 * paired / len(qs), 2),
        horse_insertions=ins,
        human_ranges_without_horse_partner=runs(human_gaps),
        horse_has_human_canonical_cterm_25aa=human_cterm in qs,
        checked_positions={
            str(p): dict(human=hs[p - 1], horse=hmap[p][0], horse_pos=hmap[p][1])
            for p in positions
        },
        other_horse_models=other_models,
        alignment=str(best),
    )
    out.write_text(json.dumps(res, indent=2) + "\n")
    print(json.dumps({k: v for k, v in res.items() if k != "alignment"}, indent=2))


if __name__ == "__main__":
    main()
