# /// script
# requires-python = ">=3.11"
# dependencies = ["biopython>=1.83"]
# ///
"""Assign the C-terminal exon content of horse STX3 A0A3Q2H352.

Compares the horse benchmark sequence with human STX3 isoforms A/B and mouse
Stx3 isoforms 3A/3B (UniProt, downloaded to sequences.fasta), and with the other
horse STX3 gene-model entries. The C-terminal region is split into two segments
using mouse 3A/3B as the reference for the mutually exclusive exons:

- SNARE-motif C-terminal half (mouse residues 227-262; exon 9A vs 9B)
- membrane-anchor segment (mouse residues 263-289; exon 10A vs 10B)

Run: uv run --script compare_isoform_segments.py
"""

from pathlib import Path

from Bio import SeqIO
from Bio.Align import PairwiseAligner

HERE = Path(__file__).parent
TARGET = "A0A3Q2H352"


def load() -> dict[str, str]:
    seqs = {}
    for rec in SeqIO.parse(HERE / "sequences.fasta", "fasta"):
        acc = rec.id.split("|")[1]
        seqs[acc] = str(rec.seq)
    return seqs


def identity(a: str, b: str) -> float:
    """Ungapped identity of two equal-length strings.

    >>> identity("ABCD", "ABCE")
    0.75
    """
    assert len(a) == len(b)
    return sum(x == y for x, y in zip(a, b)) / len(a)


def global_identity(a: str, b: str) -> tuple[float, int]:
    aligner = PairwiseAligner(mode="global", match_score=2, mismatch_score=-1,
                              open_gap_score=-10, extend_gap_score=-0.5)
    aln = aligner.align(a, b)[0]
    pairs = ident = 0
    for (s1, e1), (s2, e2) in zip(*aln.aligned):
        for i, j in zip(range(s1, e1), range(s2, e2)):
            pairs += 1
            ident += a[i] == b[j]
    return ident / pairs, pairs


def main() -> None:
    seqs = load()
    t = seqs[TARGET]
    print(f"{TARGET} length {len(t)}")
    segs = {
        "N-term..0-layer (1-226)": (0, 226),
        "SNARE C-half (227-262)": (226, 262),
        "anchor (263-289)": (262, 289),
    }
    refs = ["Q64704-1", "Q64704-2", "Q13277-1"]
    print("\nSegment identity of horse vs references (ungapped, same coordinates):")
    for name, (s, e) in segs.items():
        row = []
        for r in refs:
            rs = seqs[r]
            if len(rs) >= e:
                row.append(f"{r}={identity(t[s:e], rs[s:e]):.2f}")
        print(f"  {name}: horse {t[s:e]}")
        print(f"    {'  '.join(row)}")
    print("\nGlobal identity (Biopython global alignment):")
    for acc, s in seqs.items():
        if acc == TARGET:
            continue
        idt, pairs = global_identity(t, s)
        print(f"  vs {acc} (len {len(s)}): identity {idt:.3f} over {pairs} paired residues")


if __name__ == "__main__":
    main()
