# /// script
# requires-python = ">=3.10"
# dependencies = ["biopython>=1.81"]
# ///
"""Serpin architecture check for C28G1.2 (Q18287) against its tree neighbours.

The paralogous C. elegans serpins SRP-2 (O17365), SRP-6 (G5EFH4), SRP-3 (G5ECY2)
and SRP-1 (G5EE40) sit with C28G1.2 in the same PANTHER duplication clade
(PTN002479232; see panther_tree_placement.txt). For each, this script:

* reports protein length;
* searches for the serpin hinge consensus at the N-terminal end of the
  reactive-centre loop (P17-P9, approximately E-E-G-T/S-E-A-A-A), allowing
  one mismatch;
* aligns Q18287 locally against each neighbour (BLOSUM62) and reports which
  neighbour residues the alignment covers.

Run: uv run --script serpin_architecture.py > serpin_architecture.txt
"""

import re
import urllib.request

from Bio import Align
from Bio.Align import substitution_matrices

ACCS = {
    "Q18287": "C28G1.2",
    "O17365": "srp-2",
    "G5EFH4": "srp-6",
    "G5ECY2": "srp-3",
    "G5EE40": "srp-1",
}

HINGE = re.compile(r"(?=([EKDQ][EKDQ]G[TS]E[AG]A[AGST]))")
HINGE_LOOSE = "EEGTEAAA"


def fetch(acc):
    url = f"https://rest.uniprot.org/uniprotkb/{acc}.fasta"
    with urllib.request.urlopen(url, timeout=60) as r:
        lines = r.read().decode().splitlines()
    return "".join(x for x in lines if not x.startswith(">"))


def best_hinge(seq):
    """Best match to EEGTEAAA allowing mismatches; return (pos1, window, mismatches)."""
    best = None
    for i in range(len(seq) - len(HINGE_LOOSE) + 1):
        w = seq[i : i + len(HINGE_LOOSE)]
        mm = sum(a != b for a, b in zip(w, HINGE_LOOSE))
        if best is None or mm < best[2]:
            best = (i + 1, w, mm)
    return best


def main():
    seqs = {a: fetch(a) for a in ACCS}
    print("Lengths and hinge-region search")
    for a, name in ACCS.items():
        s = seqs[a]
        strict = [(m.start() + 1, m.group(1)) for m in HINGE.finditer(s)]
        pos, win, mm = best_hinge(s)
        print(
            f"  {a} {name}: length={len(s)} strict_hinge={strict} "
            f"best_EEGTEAAA_window={win}@{pos} mismatches={mm}"
        )
    print()
    aligner = Align.PairwiseAligner()
    aligner.mode = "local"
    aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
    aligner.open_gap_score = -11
    aligner.extend_gap_score = -1
    q = seqs["Q18287"]
    print("Local alignment of Q18287 against neighbours")
    for a, name in ACCS.items():
        if a == "Q18287":
            continue
        t = seqs[a]
        aln = aligner.align(q, t)[0]
        qb, tb = aln.aligned
        qcov = (int(qb[0][0]) + 1, int(qb[-1][1]))
        tcov = (int(tb[0][0]) + 1, int(tb[-1][1]))
        ident = sum(
            1
            for (qs, qe), (ts, te) in zip(qb, tb)
            for i, j in zip(range(qs, qe), range(ts, te))
            if q[i] == t[j]
        )
        alen = sum(int(qe - qs) for qs, qe in qb)
        print(
            f"  vs {a} {name}: score={aln.score:.0f} Q18287 {qcov[0]}-{qcov[1]} "
            f"aligns to {name} {tcov[0]}-{tcov[1]} of {len(t)}; "
            f"identity={ident}/{alen} ({100 * ident / alen:.1f}%)"
        )
        gaps = [
            (int(tb[k][1]) + 1, int(tb[k + 1][0]))
            for k in range(len(tb) - 1)
            if int(tb[k + 1][0]) - int(tb[k][1]) >= 10
        ]
        print(f"      {name} segments (>=10 aa) with no Q18287 counterpart: {gaps}")


if __name__ == "__main__":
    main()
