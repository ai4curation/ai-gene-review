"""Compare bovine XIRP2 (E1BL04) with characterized Xin-family proteins.

Fetches sequences from UniProt REST, performs global pairwise alignments
(BLOSUM62, gap open -10, extend -0.5) and reports identity, coverage of the
reference, and coverage of the reference N- and C-terminal 300 residues.
Run: uv run python compare_xin_family.py
"""

import urllib.request

from Bio import SeqIO
from Bio.Align import PairwiseAligner, substitution_matrices
from io import StringIO

QUERY = "E1BL04"
REFS = {
    "A4UGR9": "human XIRP2 (PTHR22591:SF1)",
    "Q4U4S6": "mouse Xirp2 (PTHR22591:SF1)",
    "Q702N8": "human XIRP1 (PTHR22591:SF2)",
    "O70373": "mouse Xirp1 (PTHR22591:SF2)",
}


def fetch(acc: str) -> str:
    url = f"https://rest.uniprot.org/uniprotkb/{acc}.fasta"
    with urllib.request.urlopen(url) as fh:
        rec = next(SeqIO.parse(StringIO(fh.read().decode()), "fasta"))
    return str(rec.seq)


def compare(q: str, r: str) -> dict:
    aligner = PairwiseAligner()
    aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
    aligner.open_gap_score = -10
    aligner.extend_gap_score = -0.5
    aligner.mode = "global"
    aln = aligner.align(q, r)[0]
    ident = 0
    aligned_r = set()
    for (qs, qe), (rs, re_) in zip(*aln.aligned):
        for i, j in zip(range(qs, qe), range(rs, re_)):
            aligned_r.add(j)
            if q[i] == r[j]:
                ident += 1
    n_cov = len([j for j in aligned_r if j < 300]) / 300
    c_cov = len([j for j in aligned_r if j >= len(r) - 300]) / 300
    return {
        "aligned_pairs": len(aligned_r),
        "identity_over_aligned": ident / max(len(aligned_r), 1),
        "ref_coverage": len(aligned_r) / len(r),
        "ref_Nterm300_coverage": n_cov,
        "ref_Cterm300_coverage": c_cov,
    }


def main() -> None:
    q = fetch(QUERY)
    print(f"query {QUERY} length {len(q)}")
    for acc, label in REFS.items():
        r = fetch(acc)
        res = compare(q, r)
        print(f"{acc}\t{label}\tlen={len(r)}\t" + "\t".join(
            f"{k}={v:.3f}" if isinstance(v, float) else f"{k}={v}" for k, v in res.items()))
    lim_check(q)


def lim_check(q: str) -> None:
    """Local alignment of the mouse Xirp2 isoform-1 LIM domain (Q4U4S6 3255-3315,
    PROSITE PRU00125) against the query, to test whether the query carries it."""
    m = fetch("Q4U4S6")
    lim = m[3254:3315]
    aligner = PairwiseAligner()
    aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
    aligner.open_gap_score = -10
    aligner.extend_gap_score = -0.5
    aligner.mode = "local"
    aln = aligner.align(q, lim)[0]
    pairs = sum(e - s for s, e in aln.aligned[1])
    ident = sum(
        1
        for (qs, qe), (rs, re_) in zip(*aln.aligned)
        for i, j in zip(range(qs, qe), range(rs, re_))
        if q[i] == lim[j]
    )
    print(f"LIM check: mouse LIM len={len(lim)} local score={aln.score:.1f} "
          f"aligned={pairs} identities={ident} query_start={aln.aligned[0][0][0] + 1}")


if __name__ == "__main__":
    main()
