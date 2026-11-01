"""Align P91866 (F32H2.6) to the ketosynthase (KS) region of C. elegans FASN-1
(P91871, F32H2.5) and human FASN (P49327) and report which residues of P91866
correspond to the human FASN KS catalytic triad (Cys161, His293, His331;
UniProt ACT_SITE features for P49327).

Sequences are parsed from the local UniProt flat files in this repository.
Usage: uv run python align_ks.py
"""
from pathlib import Path
from Bio import Align
from Bio.Align import substitution_matrices

ROOT = Path(__file__).resolve().parents[4]
FILES = {
    "P91866": ROOT / "genes/worm/P91866/P91866-uniprot.txt",
    "P91871_fasn-1": ROOT / "genes/worm/fasn-1/fasn-1-uniprot.txt",
    "P49327_FASN": ROOT / "genes/human/FASN/FASN-uniprot.txt",
}
HUMAN_ACT = {161: "KS Cys (acyl-enzyme)", 293: "KS His", 331: "KS His"}


def read_seq(path):
    seq, on = [], False
    for line in path.read_text().splitlines():
        if line.startswith("SQ "):
            on = True
            continue
        if on:
            if line.startswith("//"):
                break
            seq.append(line.replace(" ", ""))
    return "".join(seq)


def aligner():
    a = Align.PairwiseAligner()
    a.substitution_matrix = substitution_matrices.load("BLOSUM62")
    a.open_gap_score = -10
    a.extend_gap_score = -0.5
    a.mode = "local"
    return a


def pos_map(aln):
    """Map target (index 0) 1-based positions to query (index 1) residues."""
    m = {}
    t_seq, q_seq = aln.target, aln.query
    for (ts, te), (qs, qe) in zip(*aln.aligned):
        for i in range(te - ts):
            m[ts + i + 1] = (qs + i + 1, q_seq[qs + i])
    return m


def identity(aln):
    ident = n = 0
    for (ts, te), (qs, qe) in zip(*aln.aligned):
        for i in range(te - ts):
            n += 1
            ident += aln.target[ts + i] == aln.query[qs + i]
    return ident, n


def main():
    seqs = {k: read_seq(v) for k, v in FILES.items()}
    q = seqs["P91866"]
    print(f"P91866 length: {len(q)}")
    a = aligner()
    for name in ("P91871_fasn-1", "P49327_FASN"):
        t = seqs[name][:500]
        aln = a.align(t, q)[0]
        ident, n = identity(aln)
        print(f"\n=== {name} (residues 1-500) vs P91866 ===")
        print(f"score={aln.score:.1f} aligned_pairs={n} identity={ident}/{n} ({100*ident/max(n,1):.1f}%)")
        print(aln)
    # human catalytic residues
    h = seqs["P49327_FASN"]
    aln = a.align(h[:500], q)[0]
    m = pos_map(aln)
    print("\nHuman FASN KS catalytic residues and the aligned P91866 residue:")
    for p, label in HUMAN_ACT.items():
        got = m.get(p)
        res = f"P91866 {got[1]}{got[0]}" if got else "not aligned (outside/gap)"
        print(f"  FASN {h[p-1]}{p} ({label}): {res}")
    print("  P91866 cysteines:", [i + 1 for i, c in enumerate(q) if c == "C"])


if __name__ == "__main__":
    main()
