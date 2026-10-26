# /// script
# requires-python = ">=3.10"
# dependencies = ["biopython", "requests"]
# ///
"""Compare Drosophila CG34117 (Q0KI97) with human FMC1 (Q96HJ9, same PANTHER
subfamily PTHR31716:SF1) and yeast Fmc1 (P40491, PANTHER PTHR28015).

Fetches sequences and PANTHER cross-references from UniProt REST, runs global
(BLOSUM62, gap open -10, extend -0.5) pairwise alignments, reports identity and
locates an N-terminal LYR-like tripeptide ([LIVF]-Y-R/K). Prints results only;
nothing is hardcoded.
"""

import re
import requests
from Bio import Align
from Bio.Align import substitution_matrices

ACCS = {"Q0KI97": "CG34117 (fly)", "Q96HJ9": "FMC1 (human)", "P40491": "Fmc1 (yeast)"}


def fetch(acc: str) -> tuple[str, list[str]]:
    r = requests.get(f"https://rest.uniprot.org/uniprotkb/{acc}.txt", timeout=60)
    r.raise_for_status()
    lines = r.text.splitlines()
    seq_lines, in_seq, panther = [], False, []
    for ln in lines:
        if ln.startswith("DR   PANTHER;"):
            panther.append(ln.split(";")[1].strip())
        if ln.startswith("SQ "):
            in_seq = True
            continue
        if ln.startswith("//"):
            in_seq = False
        if in_seq:
            seq_lines.append(ln.replace(" ", ""))
    return "".join(seq_lines), panther


def identity(aln) -> tuple[float, int]:
    a, b = aln[0], aln[1]
    pairs = [(x, y) for x, y in zip(a, b) if x != "-" and y != "-"]
    same = sum(1 for x, y in pairs if x == y)
    return (100.0 * same / len(pairs) if pairs else 0.0), len(pairs)


def main() -> None:
    seqs = {}
    for acc, name in ACCS.items():
        s, p = fetch(acc)
        seqs[acc] = s
        lyr = [(m.start() + 1, m.group()) for m in re.finditer(r"[LIVF]Y[RK]", s)]
        print(f"{acc}\t{name}\tlength={len(s)}\tPANTHER={','.join(p)}\tLYR-like={lyr}")
    aligner = Align.PairwiseAligner()
    aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
    aligner.open_gap_score = -10
    aligner.extend_gap_score = -0.5
    aligner.mode = "global"
    accs = list(ACCS)
    for i in range(len(accs)):
        for j in range(i + 1, len(accs)):
            a, b = accs[i], accs[j]
            aln = aligner.align(seqs[a], seqs[b])[0]
            pid, n = identity(aln)
            print(f"\n{a} vs {b}: score={aln.score:.1f} identity={pid:.1f}% over {n} aligned positions")
            print(aln)


if __name__ == "__main__":
    main()
