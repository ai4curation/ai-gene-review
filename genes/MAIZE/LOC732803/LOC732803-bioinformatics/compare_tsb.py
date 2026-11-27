"""Compare K7TR93 (LOC732803) with the Swiss-Prot maize TSB entries.

Usage (from the repository root):
    uv run python genes/MAIZE/LOC732803/LOC732803-bioinformatics/compare_tsb.py

Reads the UniProt flat files in this folder and the gene folder, performs global
pairwise alignments (BLOSUM62, gap open -10, extend -0.5) and reports:
  * percent identity of K7TR93 to P43284 (TSB2/ORP2, fragment), P43283 (TSB1/ORP1)
    and K7TTR0 (LOC732842, the chromosome-4 paralog), and of K7TTR0 to both Swiss-Prot entries
  * the residue in K7TR93 aligned to the curated PLP lysine (MOD_RES) of P43284
  * whether the TrpB PROSITE-like PLP motif context (H-K-x-N-N) is present\n  * whether the tryptic peptide QALNVFR reported from the native complex occurs in each sequence.
Nothing is hard-coded; all numbers are computed from the sequences.
"""

import re
import sys
from pathlib import Path

from Bio import Align
from Bio.Align import substitution_matrices
from Bio import SwissProt

HERE = Path(__file__).resolve().parent
GENE_DIR = HERE.parent


def load(path: Path):
    with open(path) as fh:
        return SwissProt.read(fh)


def mod_res_positions(rec):
    out = []
    for f in rec.features:
        if f.type == "MOD_RES":
            out.append((int(f.location.start) + 1, f.qualifiers.get("note", "")))
    return out


def align(a: str, b: str):
    aligner = Align.PairwiseAligner()
    aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
    aligner.open_gap_score = -10
    aligner.extend_gap_score = -0.5
    aligner.mode = "global"
    return aligner.align(a, b)[0]


def identity(aln):
    ident = 0
    cols = 0
    for (s1, e1), (s2, e2) in zip(*aln.aligned):
        for i, j in zip(range(s1, e1), range(s2, e2)):
            cols += 1
            if aln.target[i] == aln.query[j]:
                ident += 1
    return ident, cols


def map_pos(aln, query_pos_1based):
    """Map a 1-based position in query to the target (1-based) or None."""
    q0 = query_pos_1based - 1
    for (s1, e1), (s2, e2) in zip(*aln.aligned):
        if s2 <= q0 < e2:
            return s1 + (q0 - s2) + 1
    return None


def main():
    target = load(GENE_DIR / "LOC732803-uniprot.txt")
    tsb2 = load(HERE / "P43284-uniprot.txt")
    tsb1 = load(HERE / "P43283-uniprot.txt")
    tseq = target.sequence
    print(f"K7TR93 length: {len(tseq)}")
    paralog = load(HERE / "K7TTR0-uniprot.txt")
    for name, rec in (("P43284 (TSB2/ORP2)", tsb2), ("P43283 (TSB1/ORP1)", tsb1),
                      ("K7TTR0 (LOC732842, chr 4 paralog)", paralog)):
        aln = align(tseq, rec.sequence)
        ident, cols = identity(aln)
        print(f"{name}: length {len(rec.sequence)}; aligned columns {cols}; "
              f"identical {ident} ({100.0 * ident / cols:.1f}% of aligned columns)")
        for pos, note in mod_res_positions(rec):
            tpos = map_pos(aln, pos)
            res = tseq[tpos - 1] if tpos else "-"
            print(f"  {name} MOD_RES {pos} ({note}; residue {rec.sequence[pos-1]}) "
                  f"-> K7TR93 position {tpos} residue {res}")
    # Same comparison from the chr-4 paralog's side, to judge the Swiss-Prot assignment
    for name, rec in (("P43284 (TSB2/ORP2)", tsb2), ("P43283 (TSB1/ORP1)", tsb1)):
        aln = align(paralog.sequence, rec.sequence)
        ident, cols = identity(aln)
        print(f"K7TTR0 vs {name}: identical {ident}/{cols} "
              f"({100.0 * ident / cols:.1f}% of aligned columns)")
    for m in re.finditer(r"H(K).NN", tseq):
        print(f"K7TR93 H-K-x-N-N motif at {m.start()+1}-{m.end()}; lysine at {m.start(1)+1}")
    # Is the native-complex peptide QALNVFR (PMID:18430213, assigned to ZmTSB1)
    # a tryptic peptide (preceded by K/R, ending in R) of each sequence?
    pep = "QALNVFR"
    for name, seq in (("K7TR93", tseq), ("K7TTR0", paralog.sequence),
                      ("P43283", tsb1.sequence), ("P43284", tsb2.sequence)):
        hits = [m.start() + 1 for m in re.finditer(pep, seq)]
        tryptic = [h for h in hits if h > 1 and seq[h - 2] in "KR"]
        print(f"{pep} in {name}: positions {hits}; tryptic (preceded by K/R): {tryptic}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
