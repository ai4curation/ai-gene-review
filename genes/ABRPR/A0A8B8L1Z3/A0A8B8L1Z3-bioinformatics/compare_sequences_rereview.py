# /// script
# requires-python = ">=3.10"
# dependencies = ["biopython"]
# ///
"""Compare A0A8B8L1Z3 to PTHR45496 relatives and inspect its J-domain HPD motif.

Inputs: ../A0A8B8L1Z3-uniprot.txt (query) and relatives.fasta (UniProt FASTA
downloads of Arabidopsis/Populus PTHR45496 members). Prints global-alignment
identity of the query to each relative and the J-domain loop sequence.

Run: uv run compare_sequences_rereview.py
"""

import re
from pathlib import Path

from Bio import SeqIO
from Bio.Align import PairwiseAligner, substitution_matrices

HERE = Path(__file__).parent
SUBFAMILY = {
    "Q9FMF3": "SF19 (EIP9/SDJ1/DNAJ1, At5g64360)",
    "A0A3N7GRR1": "SF19 (Populus)",
    "U5FLI7": "SF19 (Populus)",
    "A0A1P8B2U5": "SF1 (SDJ2/DNAJ2, At2g01710)",
    "Q0WQM3": "SF10 (SDJ3, At1g62970)",
    "Q9SZ59": "SF32 (ADMETOS)",
    "Q9LXB9": "SF28 (At5g09540)",
}


def read_query() -> str:
    text = (HERE.parent / "A0A8B8L1Z3-uniprot.txt").read_text()
    seq_block = text.split("\nSQ ")[1].split("\n", 1)[1].split("//")[0]
    return re.sub(r"[^A-Z]", "", seq_block)


def main() -> None:
    query = read_query()
    print(f"query A0A8B8L1Z3 length {len(query)}")
    jdom = query[69:135]
    print(f"J domain 70-135: {jdom}")
    print(f"HPD present in J domain: {'HPD' in jdom}")
    aligner = PairwiseAligner()
    aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
    aligner.open_gap_score = -10
    aligner.extend_gap_score = -0.5
    aligner.mode = "global"
    for rec in SeqIO.parse(HERE / "relatives.fasta", "fasta"):
        acc = rec.id.split("|")[1]
        seq = str(rec.seq)
        aln = aligner.align(query, seq)[0]
        ident = sum(
            1
            for (qs, qe), (ss, se) in zip(*aln.aligned)
            for i, j in zip(range(qs, qe), range(ss, se))
            if query[i] == seq[j]
        )
        print(
            f"{acc}\t{SUBFAMILY.get(acc, '?')}\tlen {len(seq)}\t"
            f"identical {ident}\tid/query_len {ident / len(query):.3f}\t"
            f"HPD {'HPD' in seq}"
        )
        # locate the query's J-domain loop region in the relative
        loop_q = query.find("EPHRNP")
        cols = [
            j
            for (qs, qe), (ss, se) in zip(*aln.aligned)
            for i, j in zip(range(qs, qe), range(ss, se))
            if loop_q <= i < loop_q + 6
        ]
        if cols:
            print(f"   aligned to query EPHRNP ({loop_q + 1}-{loop_q + 6}): {seq[min(cols):max(cols) + 1]}")


if __name__ == "__main__":
    main()
