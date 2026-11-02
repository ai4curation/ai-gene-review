"""Compare A0A1S3Y076 with Arabidopsis PRORP1/2/3 and map PRORP1 metal-binding residues.

Inputs: ../A0A1S3Y076-uniprot.txt (target sequence) and relatives.fasta
(UniProt Q680B9 PRORP2, F4JKB6 PRORP3, Q66GI4 PRORP1, fetched from rest.uniprot.org).

Run: uv run --with biopython python compare_prorp_rereview.py
"""

from pathlib import Path

from Bio import SeqIO
from Bio.Align import PairwiseAligner, substitution_matrices

HERE = Path(__file__).parent

# PRORP1 (Q66GI4) metal-binding positions from its UniProt record (BINDING features)
PRORP1_SITES = {
    344: "Zn",
    347: "Zn",
    399: "Mn (catalytic, NYN)",
    474: "Mn (catalytic, NYN)",
    475: "Mn (catalytic, NYN)",
    493: "Mn (catalytic, NYN)",
    548: "Zn",
    565: "Zn",
}


def target_sequence() -> str:
    lines = (HERE.parent / "A0A1S3Y076-uniprot.txt").read_text().splitlines()
    start = next(i for i, line in enumerate(lines) if line.startswith("SQ"))
    seq = "".join(
        line.strip().replace(" ", "") for line in lines[start + 1 :] if not line.startswith("//")
    )
    return seq


def aligner() -> PairwiseAligner:
    a = PairwiseAligner()
    a.mode = "global"
    a.substitution_matrix = substitution_matrices.load("BLOSUM62")
    a.open_gap_score = -10
    a.extend_gap_score = -0.5
    a.end_gap_score = 0
    return a


def residue_map(aln) -> dict[int, int]:
    """Map 1-based positions in seqB (relative) to 1-based positions in seqA (target)."""
    mapping = {}
    for (a0, a1), (b0, b1) in zip(*aln.aligned):
        for off in range(a1 - a0):
            mapping[b0 + off + 1] = a0 + off + 1
    return mapping


def identity(aln) -> tuple[int, int]:
    ident = 0
    cols = 0
    for (a0, a1), (b0, b1) in zip(*aln.aligned):
        for off in range(a1 - a0):
            cols += 1
            if aln.target[a0 + off] == aln.query[b0 + off]:
                ident += 1
    return ident, cols


def main() -> None:
    tseq = target_sequence()
    print(f"A0A1S3Y076 length: {len(tseq)}")
    al = aligner()
    for rec in SeqIO.parse(HERE / "relatives.fasta", "fasta"):
        acc = rec.id.split("|")[1]
        rseq = str(rec.seq)
        aln = al.align(tseq, rseq)[0]
        ident, cols = identity(aln)
        print(
            f"{acc} ({rec.id.split('|')[2]}): length {len(rseq)}; aligned columns {cols}; "
            f"identity {ident}/{cols} = {100 * ident / cols:.1f}%"
        )
        if acc == "Q66GI4":
            m = residue_map(aln)
            for pos, label in PRORP1_SITES.items():
                tpos = m.get(pos)
                tres = tseq[tpos - 1] if tpos else "-"
                print(f"  PRORP1 {rseq[pos - 1]}{pos} [{label}] -> A0A1S3Y076 {tres}{tpos or ''}")
    print(f"A0A1S3Y076 N-terminal 40 aa: {tseq[:40]}")


if __name__ == "__main__":
    main()
