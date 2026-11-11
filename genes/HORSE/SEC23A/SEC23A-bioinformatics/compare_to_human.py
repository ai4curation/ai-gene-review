# /// script
# requires-python = ">=3.10"
# dependencies = ["biopython", "requests"]
# ///
"""Global alignment of horse SEC23A (A0A3Q2H5Z6) to human SEC23A (Q15436) and SEC23B (Q15437).

Reports length, identity, gap columns and whether the cysteines of the
Sec23/Sec24-type zinc-finger region (human residues 56-100) are conserved.
"""
import requests
from Bio import Align
from Bio.Align import substitution_matrices

def fetch(acc):
    r = requests.get(f"https://rest.uniprot.org/uniprotkb/{acc}.fasta", timeout=60)
    r.raise_for_status()
    return "".join(r.text.splitlines()[1:])

horse = fetch("A0A3Q2H5Z6")
aligner = Align.PairwiseAligner()
aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
aligner.open_gap_score = -10
aligner.extend_gap_score = -0.5
aligner.mode = "global"
for acc, name in [("Q15436", "human SEC23A"), ("Q15437", "human SEC23B")]:
    hs = fetch(acc)
    aln = aligner.align(horse, hs)[0]
    ident = sum(1 for a, b in zip(*aln.indices) if a >= 0 and b >= 0 and horse[a] == hs[b])
    gaps = sum(1 for a, b in zip(*aln.indices) if a < 0 or b < 0)
    print(f"{name} {acc}: horse_len={len(horse)} ref_len={len(hs)} identical={ident} "
          f"identity_vs_ref={ident/len(hs):.3f} gap_columns={gaps}")
    if acc == "Q15436":
        m = {b: a for a, b in zip(*aln.indices) if a >= 0 and b >= 0}
        diffs = [f"{hs[b]}{b+1}{horse[a]}" for a, b in zip(*aln.indices) if a >= 0 and b >= 0 and horse[a] != hs[b]]
        print("  substitutions (human pos, horse residue):", diffs)
        # zinc finger cysteines in human 61..96 region
        cys = [i + 1 for i in range(55, 100) if hs[i] == "C"]
        print("  human Cys in 56-100:", cys, " horse at same:", [horse[m[c-1]] + str(m[c-1]+1) for c in cys])
