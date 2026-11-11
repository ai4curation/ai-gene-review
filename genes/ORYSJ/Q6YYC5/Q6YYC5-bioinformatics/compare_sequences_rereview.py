"""Compare rice Q6YYC5 with Arabidopsis RGLG1-5 (re-review analysis).

Fetches sequences from UniProt REST, computes global pairwise identity
(BLOSUM62, gap open -10, extend -0.5), reports the N-terminal Met-Gly
(N-myristoylation-compatible) motif and the RING C4HC3/C3H2C3 ligand
positions of Q6YYC5 mapped onto each Arabidopsis paralog.

Run: uv run --with biopython --with requests python compare_sequences_rereview.py
"""
import re
import requests
from Bio import Align
from Bio.Align import substitution_matrices

ACCS = {
    "Q6YYC5": "rice Os08g0135400 (target, PTHR45751:SF16)",
    "Q9SAL0": "AtRGLG4 AT1G79380 (PTHR45751:SF16)",
    "Q8RX26": "AtRGLG3 AT5G63970",
    "Q9SS90": "AtRGLG1 AT3G01650 (SF15)",
    "Q9LY87": "AtRGLG2 AT5G14420 (SF29)",
    "Q8LB88": "AtRGLG5 (SF30)",
}


def fetch(acc: str) -> str:
    r = requests.get(f"https://rest.uniprot.org/uniprotkb/{acc}.fasta", timeout=60)
    r.raise_for_status()
    return "".join(r.text.splitlines()[1:])


def main() -> None:
    seqs = {a: fetch(a) for a in ACCS}
    aligner = Align.PairwiseAligner()
    aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
    aligner.open_gap_score = -10
    aligner.extend_gap_score = -0.5
    aligner.mode = "global"
    target = seqs["Q6YYC5"]
    # RING ligands of Q6YYC5: cysteine/histidine residues in the RING region (356-389)
    ring_start = 350
    ring = [(i + 1, c) for i, c in enumerate(target) if i + 1 >= ring_start and c in "CH"]
    print("Target length", len(target), "N-term", target[:8])
    print("Target RING-region C/H residues:", ring)
    for acc, desc in ACCS.items():
        s = seqs[acc]
        aln = aligner.align(target, s)[0]
        ident = sum(
            1
            for (a0, a1), (b0, b1) in zip(*aln.aligned)
            for i, j in zip(range(a0, a1), range(b0, b1))
            if target[i] == s[j]
        )
        # map RING ligand positions
        mapping = {}
        for (a0, a1), (b0, b1) in zip(*aln.aligned):
            for i, j in zip(range(a0, a1), range(b0, b1)):
                mapping[i + 1] = s[j]
        conserved = sum(1 for p, c in ring if mapping.get(p) == c)
        myr = bool(re.match(r"^MG", s))
        print(
            f"{acc}\t{desc}\tlen={len(s)}\tidentity_vs_target={ident/len(target):.3f}"
            f"\tN-term={s[:8]}\tMG_start={myr}\tRING_CH_conserved={conserved}/{len(ring)}"
        )


if __name__ == "__main__":
    main()
