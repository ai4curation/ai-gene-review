"""Compare K7TTR0 (LOC732842, orp1 locus) with Swiss-Prot TSB1 (P43283) and the
chromosome-10 paralog K7TR93 (LOC732803, orp2 locus).

Usage (from the repository root):
    uv run python genes/MAIZE/LOC732842/LOC732842-bioinformatics/compare_tsb1.py

Reports, computed from the sequences (nothing hard-coded):
  * percent identity of K7TTR0 to P43283 and K7TR93 (global, BLOSUM62, -10/-0.5)
  * the K7TTR0 residue aligned to the curated PLP lysine (MOD_RES) of P43283
  * occurrence in each sequence of the tryptic peptides PMID:18430213 reported from the
    native 160 kD complex (ADGTGPLIYLK, DATSEAIR, QALNVFR)
  * occurrence of the N-terminal peptide encoded by the PMID:18430213 ZmTSB1 forward
    expression primer (CATATGGCGGCCTCCCCCGCTGCCG -> translated here), i.e. where the
    recombinant mature ZmTSB1 construct starts.
"""

from pathlib import Path

from Bio import Align, SwissProt
from Bio.Align import substitution_matrices
from Bio.Seq import Seq

HERE = Path(__file__).resolve().parent
GENE_DIR = HERE.parent
PEPTIDES = ["ADGTGPLIYLK", "DATSEAIR", "QALNVFR"]
PRIMER = "CATATGGCGGCCTCCCCCGCTGCCG"


def load(p):
    with open(p) as fh:
        return SwissProt.read(fh)


def align(a, b):
    al = Align.PairwiseAligner()
    al.substitution_matrix = substitution_matrices.load("BLOSUM62")
    al.open_gap_score = -10
    al.extend_gap_score = -0.5
    al.mode = "global"
    return al.align(a, b)[0]


def identity(aln):
    ident = cols = 0
    for (s1, e1), (s2, e2) in zip(*aln.aligned):
        for i, j in zip(range(s1, e1), range(s2, e2)):
            cols += 1
            ident += aln.target[i] == aln.query[j]
    return ident, cols


def map_pos(aln, qpos):
    q0 = qpos - 1
    for (s1, e1), (s2, e2) in zip(*aln.aligned):
        if s2 <= q0 < e2:
            return s1 + (q0 - s2) + 1
    return None


def main():
    tgt = load(GENE_DIR / "LOC732842-uniprot.txt")
    tsb1 = load(HERE / "P43283-uniprot.txt")
    par = load(HERE / "K7TR93-uniprot.txt")
    t = tgt.sequence
    print(f"K7TTR0 length: {len(t)}")
    for name, rec in (("P43283 (Swiss-Prot TSB1/ORP1, fragment)", tsb1),
                      ("K7TR93 (LOC732803, orp2 locus)", par)):
        aln = align(t, rec.sequence)
        i, c = identity(aln)
        print(f"{name}: length {len(rec.sequence)}; aligned cols {c}; identical {i}; "
              f"identity {100*i/c:.1f}%")
    aln = align(t, tsb1.sequence)
    for f in tsb1.features:
        if f.type == "MOD_RES":
            p = int(f.location.start) + 1
            m = map_pos(aln, p)
            res = t[m - 1] if m else None
            ctx = t[m - 3:m + 3] if m else None
            print(f"P43283 MOD_RES {p} ({f.qualifiers.get('note')}) -> K7TTR0 {res}{m}; context {ctx}")
    for pep in PEPTIDES:
        for name, s in (("K7TTR0", t), ("K7TR93", par.sequence), ("P43283", tsb1.sequence)):
            pos = s.find(pep)
            prev = s[pos - 1] if pos > 0 else None
            print(f"peptide {pep} in {name}: {'pos ' + str(pos + 1) + ', preceded by ' + str(prev) if pos >= 0 else 'absent'}")
    prot = str(Seq(PRIMER[:24]).translate())
    core = prot[1:]  # drop the NdeI-derived His before Met
    print(f"primer translation: {prot}; searching for {core}")
    for name, s in (("K7TTR0", t), ("K7TR93", par.sequence)):
        pos = s.find(core[1:])  # without the initiator Met added by the primer
        print(f"  {core[1:]} in {name}: {'pos ' + str(pos + 1) if pos >= 0 else 'absent'}")


if __name__ == "__main__":
    main()
