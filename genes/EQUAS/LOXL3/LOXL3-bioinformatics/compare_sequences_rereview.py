# /// script
# requires-python = ">=3.10"
# dependencies = ["biopython>=1.83"]
# ///
"""Compare donkey LOXL3 (A0A9L0K7N3) with horse A0A9L0TKN1 and human P58215.

Reports global identity, unaligned donkey segments (N-terminal extension, internal
insertions) and whether catalytic residues are conserved.

Usage: uv run --script compare_sequences_rereview.py DONKEY.txt HORSE.txt HUMAN.txt
"""
import sys
from Bio import SeqIO
from Bio.Align import PairwiseAligner, substitution_matrices


def read(path):
    return str(next(SeqIO.parse(path, "swiss")).seq)


def align(a, b):
    al = PairwiseAligner()
    al.mode = "global"
    al.substitution_matrix = substitution_matrices.load("BLOSUM62")
    al.open_gap_score = -10
    al.extend_gap_score = -0.5
    al.end_gap_score = 0
    return al.align(a, b)[0]


def mapping(aln):
    """Map query (seq A, 1-based) positions to target (seq B) positions."""
    m = {}
    for (a0, a1), (b0, b1) in zip(*aln.aligned):
        for i in range(a1 - a0):
            m[a0 + i + 1] = b0 + i + 1
    return m


def unaligned_segments(length, mapped):
    segs, start = [], None
    for p in range(1, length + 1):
        if p not in mapped and start is None:
            start = p
        if p in mapped and start is not None:
            segs.append((start, p - 1))
            start = None
    if start is not None:
        segs.append((start, length))
    return segs


def report(name_a, a, name_b, b):
    aln = align(a, b)
    m = mapping(aln)
    ident = sum(1 for p, q in m.items() if a[p - 1] == b[q - 1])
    print(f"## {name_a} vs {name_b}")
    print(f"lengths {len(a)} vs {len(b)}; aligned pairs {len(m)}; identical {ident}; "
          f"identity {100 * ident / len(m):.2f}%; coverage of {name_b} {100 * len(set(m.values())) / len(b):.1f}%")
    for s, e in unaligned_segments(len(a), m):
        print(f"{name_a} residues {s}-{e} ({e - s + 1} aa) have no aligned {name_b} residue: {a[s - 1:e]}")
    return m


def main():
    donkey, horse, human = (read(p) for p in sys.argv[1:4])
    report("donkey", donkey, "horse", horse)
    m_dh = report("donkey", donkey, "human", human)
    report("horse", horse, "human", human)
    inv = {v: k for k, v in m_dh.items()}
    print("## human catalytic/cofactor residues mapped to donkey")
    for pos in (607, 609, 611, 634, 670):
        d = inv.get(pos)
        print(f"human {human[pos - 1]}{pos} -> donkey {donkey[d - 1] + str(d) if d else 'gap'}")


if __name__ == "__main__":
    main()
