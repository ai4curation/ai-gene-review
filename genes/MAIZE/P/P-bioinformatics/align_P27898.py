"""Global alignment of TrEMBL C6G8B2 (B73 P1) with Swiss-Prot P27898 (Myb-related protein P).

Fetches both sequences from the UniProt REST API and reports identity over
the N-terminal R2R3 MYB region and over the full alignment.
Run: uv run python align_P27898.py
"""
import io
import urllib.request

from Bio import SeqIO
from Bio.Align import PairwiseAligner, substitution_matrices


def fetch(acc: str) -> str:
    url = f"https://rest.uniprot.org/uniprotkb/{acc}.fasta"
    with urllib.request.urlopen(url) as fh:
        return str(next(SeqIO.parse(io.StringIO(fh.read().decode()), "fasta")).seq)


def main() -> None:
    a, b = fetch("P27898"), fetch("C6G8B2")
    al = PairwiseAligner(mode="global", open_gap_score=-10, extend_gap_score=-0.5)
    al.substitution_matrix = substitution_matrices.load("BLOSUM62")
    aln = al.align(a, b)[0]
    print(aln)
    # identity over first N residues of C6G8B2 (no gaps there)
    first_mismatch = next((i for i, (x, y) in enumerate(zip(a, b)) if x != y), None)
    prefix_id = sum(x == y for x, y in zip(a[:250], b[:250]))
    print(f"P27898 length {len(a)}; C6G8B2 length {len(b)}")
    print(f"First mismatch position (1-based): {first_mismatch + 1 if first_mismatch is not None else 'none'}")
    print(f"Identical residues in positions 1-250: {prefix_id}/250")
    s = str(aln).splitlines()
    print("Divergence begins after the shared region; see alignment above.")


if __name__ == "__main__":
    main()
