# /// script
# requires-python = ">=3.10"
# dependencies = ["biopython>=1.83"]
# ///
"""Compare horse SLC27A5 gene models F6X2Q2 and A0A5F5PXH2 with human Q9Y2P5.

Usage (from the repository root):
    uv run --script genes/HORSE/SLC27A5/SLC27A5-bioinformatics/compare_models.py

Inputs (all local, in this folder or the gene folder):
    ../SLC27A5-uniprot.txt          F6X2Q2 flat file (benchmark accession)
    A0A5F5PXH2.fasta                 alternative horse model from the same Ensembl gene
    Q9Y2P5.fasta                     human SLC27A5 (Swiss-Prot)

Reports global identity/coverage and the aligned blocks, the C-terminal region of each
horse model after the last block that aligns to human, and whether the conserved
ANL C-terminal catalytic lysine motif region of human (residues 570-690) is present.
"""

from pathlib import Path

from Bio import SeqIO
from Bio.Align import PairwiseAligner, substitution_matrices

HERE = Path(__file__).parent


def read_flatfile_seq(path: Path) -> str:
    rec = SeqIO.read(str(path), "swiss")
    return str(rec.seq)


def read_fasta(path: Path) -> str:
    return str(SeqIO.read(str(path), "fasta").seq)


def aligner() -> PairwiseAligner:
    a = PairwiseAligner()
    a.mode = "global"
    a.substitution_matrix = substitution_matrices.load("BLOSUM62")
    a.open_gap_score = -10
    a.extend_gap_score = -0.5
    a.end_gap_score = 0
    return a


def compare(name_a: str, seq_a: str, name_b: str, seq_b: str) -> None:
    aln = aligner().align(seq_a, seq_b)[0]
    ident = 0
    pairs = 0
    for (sa, ea), (sb, eb) in zip(*aln.aligned):
        for i, j in zip(range(sa, ea), range(sb, eb)):
            pairs += 1
            ident += seq_a[i] == seq_b[j]
    print(f"## {name_a} (len {len(seq_a)}) vs {name_b} (len {len(seq_b)})")
    print(f"aligned pairs {pairs}; identical {ident}; identity {100 * ident / pairs:.2f}%")
    print("aligned blocks (A start-end : B start-end, 1-based):")
    for (sa, ea), (sb, eb) in zip(*aln.aligned):
        bid = sum(seq_a[i] == seq_b[j] for i, j in zip(range(sa, ea), range(sb, eb)))
        print(f"  {sa + 1}-{ea} : {sb + 1}-{eb}  (block identity {100 * bid / (ea - sa):.1f}%)")
    print()


def main() -> None:
    f6x = read_flatfile_seq(HERE.parent / "SLC27A5-uniprot.txt")
    a0a = read_fasta(HERE / "A0A5F5PXH2.fasta")
    hum = read_fasta(HERE / "Q9Y2P5.fasta")
    compare("F6X2Q2", f6x, "A0A5F5PXH2", a0a)
    compare("F6X2Q2", f6x, "human Q9Y2P5", hum)
    compare("A0A5F5PXH2", a0a, "human Q9Y2P5", hum)
    print("## C-terminal 120 residues")
    print(f"F6X2Q2      {f6x[-120:]}")
    print(f"A0A5F5PXH2  {a0a[-120:]}")
    print(f"human       {hum[-120:]}")


if __name__ == "__main__":
    main()
