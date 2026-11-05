"""Compare rat Klf3 (D4A4V3) with mouse (Q60980) and human (P57682) KLF3.

Fetches sequences from the UniProt REST API, runs global pairwise alignments
(BLOSUM62) and reports percent identity overall and over the C-terminal
zinc-finger region, plus presence of motifs characterised in mouse BKLF:
  - the CtBP-binding motif P-V-D-L-S/T (Turner & Crossley 1998, PMID:9724649)
  - the SUMO-acceptor lysines K10 and K197 (Perdomo et al. 2005, PMID:15684403)
  - three C2H2 zinc fingers (C-x2-4-C-x12-H-x3-5-H)

Usage: uv run python compare_orthologs.py
"""

import re
import urllib.request

from Bio import Align
from Bio.Align import substitution_matrices

ACCS = {"rat": "D4A4V3", "mouse": "Q60980", "human": "P57682"}


def fetch(acc: str) -> str:
    url = f"https://rest.uniprot.org/uniprotkb/{acc}.fasta"
    with urllib.request.urlopen(url) as fh:
        lines = fh.read().decode().splitlines()
    return "".join(line.strip() for line in lines if not line.startswith(">"))


def identity(a: str, b: str) -> tuple[float, int]:
    aligner = Align.PairwiseAligner()
    aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
    aligner.open_gap_score = -10
    aligner.extend_gap_score = -0.5
    aln = aligner.align(a, b)[0]
    s1, s2 = aln[0], aln[1]
    cols = len(s1)
    ident = sum(1 for x, y in zip(s1, s2) if x == y and x != "-")
    return 100.0 * ident / cols, cols


def main() -> None:
    seqs = {k: fetch(v) for k, v in ACCS.items()}
    for k, s in seqs.items():
        print(f"{k} {ACCS[k]} length={len(s)}")
    rat = seqs["rat"]
    zf_re = re.compile(r"C.{2,4}C.{12}H.{3,5}H")
    zfs = [(m.start() + 1, m.end()) for m in zf_re.finditer(rat)]
    print(f"rat C2H2 zinc fingers (1-based start,end): {zfs}")
    zf_start = zfs[0][0] - 1 if zfs else len(rat) - 90
    for other in ("mouse", "human"):
        pid, cols = identity(rat, seqs[other])
        print(f"rat vs {other}: overall identity {pid:.1f}% over {cols} columns")
        o = seqs[other]
        o_zfs = [m.start() for m in zf_re.finditer(o)]
        o_start = o_zfs[0] if o_zfs else len(o) - 90
        pid_zf, cols_zf = identity(rat[zf_start:], o[o_start:])
        print(f"rat vs {other}: zinc-finger region identity {pid_zf:.1f}% over {cols_zf} columns")
    for k, s in seqs.items():
        motifs = [(m.start() + 1, m.group()) for m in re.finditer(r"PVDL[ST]", s)]
        print(f"{k}: CtBP motif PVDL[ST] at {motifs}")
        k10 = s[9] if len(s) >= 10 else None
        k197 = s[196] if len(s) >= 197 else None  # human numbering is offset by one insertion
        print(f"{k}: residue 10={k10} residue 197={k197}")


if __name__ == "__main__":
    main()
