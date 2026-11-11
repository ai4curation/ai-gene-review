"""Compare the A0A8J1IYX6 catalytic region against human AGC kinases.

Fetches sequences live from UniProt REST and computes Smith-Waterman local
alignments (BLOSUM62, gap open 11, extend 1) of the target kinase domain plus
AGC C-terminal tail (residues 105-424) against each comparator, reporting
identity over the aligned columns. Also prints the target's C-terminal
turn/hydrophobic-motif region for manual inspection.

Run: uv run --with biopython --with requests python compare_agc_rereview.py
"""

import requests
from Bio import Align
from Bio.Align import substitution_matrices

TARGET = "A0A8J1IYX6"
COMPARATORS = {
    "Q05655": "PRKCD (novel PKC delta)",
    "Q04759": "PRKCQ (novel PKC theta)",
    "Q02156": "PRKCE (novel PKC epsilon)",
    "P24723": "PRKCH (novel PKC eta)",
    "P17252": "PRKCA (conventional PKC alpha)",
    "Q05513": "PRKCZ (atypical PKC zeta)",
    "P41743": "PRKCI (atypical PKC iota)",
    "Q16512": "PKN1",
    "P23443": "RPS6KB1 (S6K1)",
    "Q15418": "RPS6KA1 (RSK1)",
    "O75582": "RPS6KA5 (MSK1)",
    "O00141": "SGK1",
    "P31749": "AKT1",
    "P17612": "PRKACA (PKA, outgroup)",
    "Q96LW2": "RSKR (SGK494)",
    "A0A6I8SIW5": "X. tropicalis prkcd (same-species PKC delta)",
    "A0A8J0S8T2": "X. tropicalis prkcq (same-species PKC theta)",
}

# Calibration pair: an accepted vertebrate ortholog pair (human vs frog PKC delta).
CALIBRATION = ("Q05655", "A0A6I8SIW5")


def fetch(acc: str) -> str:
    r = requests.get(f"https://rest.uniprot.org/uniprotkb/{acc}.fasta", timeout=60)
    r.raise_for_status()
    return "".join(r.text.splitlines()[1:])


def main() -> None:
    target = fetch(TARGET)
    query = target[104:]
    aligner = Align.PairwiseAligner()
    aligner.mode = "local"
    aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
    aligner.open_gap_score = -11
    aligner.extend_gap_score = -1
    rows = []
    for acc, label in COMPARATORS.items():
        seq = fetch(acc)
        aln = aligner.align(query, seq)[0]
        ident = cols = 0
        for (qs, qe), (ss, se) in zip(*aln.aligned):
            for i in range(qe - qs):
                cols += 1
                ident += query[qs + i] == seq[ss + i]
        qstart = aln.aligned[0][0][0] + 105
        qend = aln.aligned[0][-1][1] + 104
        sstart = aln.aligned[1][0][0] + 1
        send = aln.aligned[1][-1][1]
        rows.append((aln.score, acc, label, len(seq), ident, cols, qstart, qend, sstart, send))
    rows.sort(reverse=True)
    print("score\tacc\tlabel\tlen\tidentity\taligned_cols\tpct_id\tq_range\ts_range")
    for score, acc, label, ln, ident, cols, qs, qe, ss, se in rows:
        print(f"{score:.0f}\t{acc}\t{label}\t{ln}\t{ident}\t{cols}\t{100*ident/cols:.1f}\t{qs}-{qe}\t{ss}-{se}")
    a, b = (fetch(x) for x in CALIBRATION)
    cal = aligner.align(a[344:], b)[0]
    ci = cc = 0
    for (qs, qe), (ss, se) in zip(*cal.aligned):
        for i in range(qe - qs):
            cc += 1
            ci += a[344 + qs + i] == b[ss + i]
    print(f"\nCalibration {CALIBRATION[0]} (345-end) vs {CALIBRATION[1]}: {ci}/{cc} = {100*ci/cc:.1f}% identity")
    print(f"\nTarget length: {len(target)}")
    print(f"Target C-terminal tail (367-424): {target[366:]}")


if __name__ == "__main__":
    main()
