"""Assign Msed_1695 (A4YHE8) to a Cdv ESCRT-III paralog group.

Fetches sequences of all Metallosphaera sedula DSM 5348 CdvB-family proteins and the
four Sulfolobus acidocaldarius DSM 639 Cdv ESCRT-III paralogs from UniProt REST, runs
global pairwise alignments (BLOSUM62, gap open -10, extend -0.5) and prints percent
identity (identical positions / aligned columns excluding end gaps) for every
M. sedula x S. acidocaldarius pair, plus the best S. acidocaldarius hit per M. sedula
protein.

Run: uv run --with biopython python paralog_assignment.py
"""

import urllib.request

from Bio import Align
from Bio.Align import substitution_matrices

MSED = {
    "A4YHE8": "Msed_1695",
    "A4YIR6": "Msed_2179",
    "A4YHC4": "Msed_1671",
    "A4YI57": "Msed_1969",
}
SACI = {
    "Q4J924": "Saci_1373 CdvB",
    "Q4JBG6": "Saci_0451 CdvB1",
    "Q4J8Y4": "Saci_1416 CdvB2",
    "Q4J8G7": "Saci_1601 CdvB3",
}


def fetch(acc: str) -> str:
    url = f"https://rest.uniprot.org/uniprotkb/{acc}.fasta"
    with urllib.request.urlopen(url, timeout=60) as fh:
        lines = fh.read().decode().splitlines()
    return "".join(line.strip() for line in lines if not line.startswith(">"))


def identity(aligner: Align.PairwiseAligner, a: str, b: str) -> tuple[float, int]:
    aln = aligner.align(a, b)[0]
    s1, s2 = aln[0], aln[1]
    # trim end gaps
    idx = [i for i in range(len(s1)) if s1[i] != "-" and s2[i] != "-"]
    start, end = idx[0], idx[-1] + 1
    cols = end - start
    same = sum(1 for i in range(start, end) if s1[i] == s2[i] and s1[i] != "-")
    return 100.0 * same / cols, cols


def main() -> None:
    aligner = Align.PairwiseAligner()
    aligner.mode = "global"
    aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
    aligner.open_gap_score = -10
    aligner.extend_gap_score = -0.5
    aligner.end_gap_score = 0

    seqs = {acc: fetch(acc) for acc in list(MSED) + list(SACI)}
    print("query\tquery_len\ttarget\ttarget_len\tpct_identity\taligned_cols")
    best = {}
    for m, mname in MSED.items():
        for s, sname in SACI.items():
            pid, cols = identity(aligner, seqs[m], seqs[s])
            print(f"{m} {mname}\t{len(seqs[m])}\t{s} {sname}\t{len(seqs[s])}\t{pid:.1f}\t{cols}")
            if m not in best or pid > best[m][1]:
                best[m] = (sname, pid)
    # M. sedula B1/B2-family pair against each other
    pid, cols = identity(aligner, seqs["A4YHE8"], seqs["A4YIR6"])
    print(f"A4YHE8 Msed_1695\t{len(seqs['A4YHE8'])}\tA4YIR6 Msed_2179\t{len(seqs['A4YIR6'])}\t{pid:.1f}\t{cols}")
    pid, cols = identity(aligner, seqs["Q4JBG6"], seqs["Q4J8Y4"])
    print(f"Q4JBG6 Saci_0451 CdvB1\t{len(seqs['Q4JBG6'])}\tQ4J8Y4 Saci_1416 CdvB2\t{len(seqs['Q4J8Y4'])}\t{pid:.1f}\t{cols}")
    print("\nBest S. acidocaldarius hit per M. sedula protein:")
    for m, (sname, pid) in best.items():
        print(f"{m} {MSED[m]}\t{sname}\t{pid:.1f}")


if __name__ == "__main__":
    main()
