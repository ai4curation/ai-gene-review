# /// script
# requires-python = ">=3.10"
# dependencies = ["biopython"]
# ///
"""Align the four horse GEMIN5 gene-model products (all from ENSECAG00000020479)
to human GEMIN5 (Q8TEQ6) and report gaps relative to human.

Run: uv run compare_isoforms_rereview.py
FASTA inputs were downloaded from rest.uniprot.org/uniprotkb/<ACC>.fasta.
"""
from pathlib import Path
from Bio import SeqIO
from Bio.Align import PairwiseAligner, substitution_matrices

HERE = Path(__file__).parent
HUMAN = "Q8TEQ6"
HORSE = ["F6WDM0", "A0A9L0R5P7", "A0A3Q2H9B3", "A0A9L0TIL3"]


def load(acc: str) -> str:
    return str(next(SeqIO.parse(HERE / f"{acc}.fasta", "fasta")).seq)


def aligner() -> PairwiseAligner:
    a = PairwiseAligner()
    a.mode = "global"
    a.substitution_matrix = substitution_matrices.load("BLOSUM62")
    a.open_gap_score = -10
    a.extend_gap_score = -0.5
    a.target_end_gap_score = 0
    a.query_end_gap_score = 0
    return a


def gaps_in_query(aln, min_len: int = 5):
    """Return human (target) segments (1-based, inclusive) with no aligned query residue."""
    blocks_t, _ = aln.aligned
    segs = []
    prev_end = 0
    for s, e in blocks_t:
        if s - prev_end >= min_len:
            segs.append((prev_end + 1, s))
        prev_end = e
    return segs, prev_end


def main() -> None:
    human = load(HUMAN)
    al = aligner()
    print(f"human {HUMAN} length {len(human)}")
    for acc in HORSE:
        horse = load(acc)
        aln = al.align(human, horse)[0]
        bt, bq = aln.aligned
        ident = sum(
            sum(1 for i, j in zip(range(ts, te), range(qs, qe)) if human[i] == horse[j])
            for (ts, te), (qs, qe) in zip(bt, bq)
        )
        paired = sum(te - ts for ts, te in bt)
        segs, last = gaps_in_query(aln)
        if len(human) - last >= 5:
            segs.append((last + 1, len(human)))
        # horse insertions relative to human
        ins = []
        for k in range(1, len(bq)):
            gap = bq[k][0] - bq[k - 1][1]
            if gap >= 5:
                ins.append((bq[k - 1][1] + 1, bq[k][0], bt[k][0]))
        print(f"\n{acc} length {len(horse)}: paired {paired}, identity {ident/paired:.3f}")
        print(f"  human segments absent from {acc} (>=5 aa): {segs}")
        print(f"  {acc} insertions vs human (>=5 aa; horse start,end, after human pos): {ins}")


if __name__ == "__main__":
    main()
