# /// script
# requires-python = ">=3.10"
# dependencies = ["biopython", "requests"]
# ///
"""Re-review analysis for C6T1A2: fetch PTHR47593 soybean members and characterised
Arabidopsis ZFP proteins from UniProt, report global pairwise identity to C6T1A2
(Needleman-Wunsch, BLOSUM62), and locate the QALGGH zinc-finger motif and the
C-terminal EAR-like (LxLxL / DLNxxP) motifs by regex. PANTHER tree placement is
handled separately by panther_tree_placement_rereview.py."""
import re
import requests
from Bio import Align
from Bio.Align import substitution_matrices

ACCS = {
    "C6T1A2": "target, PTHR47593:SF9",
    "Q1H8M0": "soybean zfp1 (SF9)",
    "A0A2K7G974": "soybean ZFP1 (SF9)",
    "I1K296": "soybean SF9",
    "K7KN68": "soybean SF9",
    "A0A0K2CT86": "soybean SF9",
    "K7N376": "soybean SF8",
    "C6SYT9": "soybean SF8",
    "Q39266": "Arabidopsis ZFP7",
    "Q39263": "Arabidopsis ZFP4",
    "Q39262": "Arabidopsis ZFP3",
    "Q39261": "Arabidopsis ZFP2",
}


def fasta(acc: str) -> str:
    r = requests.get(f"https://rest.uniprot.org/uniprotkb/{acc}.fasta", timeout=60)
    r.raise_for_status()
    return "".join(r.text.splitlines()[1:])


def main() -> None:
    aligner = Align.PairwiseAligner()
    aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
    aligner.open_gap_score = -10
    aligner.extend_gap_score = -0.5
    aligner.mode = "global"
    seqs = {a: fasta(a) for a in ACCS}
    target = seqs["C6T1A2"]
    print("accession\tnote\tlength\tidentity_to_C6T1A2\tQALGGH_pos\tEAR_like")
    for acc, note in ACCS.items():
        s = seqs[acc]
        aln = aligner.align(target, s)[0]
        ident = sum(
            1
            for (a0, a1), (b0, b1) in zip(*aln.aligned)
            for i, j in zip(range(a0, a1), range(b0, b1))
            if target[i] == s[j]
        )
        pct = 100 * ident / min(len(target), len(s))
        q = [m.start() + 1 for m in re.finditer("QALGGH", s)]
        ear = [f"{m.group()}@{m.start()+1}" for m in re.finditer(r"L.L.L|DLN..P", s)]
        print(f"{acc}\t{note}\t{len(s)}\t{pct:.1f}\t{q}\t{ear}")
    print("C6T1A2 vs Q1H8M0 identical sequence:", seqs["C6T1A2"] == seqs["Q1H8M0"])
    print("C6T1A2 vs A0A2K7G974 identical sequence:", seqs["C6T1A2"] == seqs["A0A2K7G974"])


if __name__ == "__main__":
    main()
