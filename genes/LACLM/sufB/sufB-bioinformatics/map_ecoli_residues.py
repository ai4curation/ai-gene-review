"""Map functionally essential E. coli SufB residues onto L. lactis SufB (A2RMK5).

Residues tested (E. coli SufB numbering, Yuda et al. 2017, PMID:28839209):
  C254 - sulfur acceptor from SufE
  C405, E434 - de novo cluster site at the SufB-SufD interface

Run from this directory:
  uv run python map_ecoli_residues.py
"""

from pathlib import Path

from Bio import SeqIO
from Bio.Align import PairwiseAligner, substitution_matrices

HERE = Path(__file__).parent
ECOLI_RESIDUES = {254: "C", 405: "C", 434: "E"}


def main() -> None:
    ecoli = next(SeqIO.parse(HERE / "ecoli_sufB_P77522.fasta", "fasta"))
    query = next(SeqIO.parse(HERE / "A2RMK5.fasta", "fasta"))
    aligner = PairwiseAligner()
    aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
    aligner.open_gap_score = -11
    aligner.extend_gap_score = -1
    aligner.mode = "global"
    aln = aligner.align(str(ecoli.seq), str(query.seq))[0]

    # identity over aligned (non-gap) columns
    ident = aligned = 0
    e2q = {}
    for (es, ee), (qs, qe) in zip(*aln.aligned):
        for i, j in zip(range(es, ee), range(qs, qe)):
            aligned += 1
            ident += ecoli.seq[i] == query.seq[j]
            e2q[i + 1] = j + 1
    print(f"E. coli SufB {ecoli.id} length {len(ecoli.seq)}; query {query.id} length {len(query.seq)}")
    print(f"aligned columns: {aligned}; identity: {ident / aligned:.1%}")
    for pos, aa in ECOLI_RESIDUES.items():
        assert ecoli.seq[pos - 1] == aa, f"E. coli residue {pos} is not {aa}"
        q = e2q.get(pos)
        if q is None:
            print(f"E. coli {aa}{pos}: gap in query")
            continue
        window_e = ecoli.seq[pos - 6 : pos + 5]
        window_q = query.seq[q - 6 : q + 5]
        print(f"E. coli {aa}{pos} -> query {query.seq[q - 1]}{q}   E.coli {window_e}  query {window_q}")


if __name__ == "__main__":
    main()
