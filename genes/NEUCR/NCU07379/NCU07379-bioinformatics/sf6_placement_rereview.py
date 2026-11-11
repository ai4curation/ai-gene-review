# /// script
# requires-python = ">=3.10"
# dependencies = ["biopython>=1.83", "requests"]
# ///
"""Place NCU07379 (V5IQW8) within PANTHER PTHR40621:SF6 relative to the
characterised Yap1/Pap1/NapA clade and the FlbB clade.

Steps (all computed, nothing hard-coded):
1. Fetch sequences from UniProt REST.
2. Local Smith-Waterman (BLOSUM62, gap 11/1) identity of NCU07379, NCU03905
   and A. nidulans FlbB against every sequence.
3. MAFFT (L-INS-i) alignment, neighbour-joining tree from identity distances
   over the alignment, with 100 bootstrap replicates (column resampling).
4. Count cysteines in the C-terminal 150 residues (Yap1 c-CRD proxy).

Run: uv run --script sf6_placement_rereview.py > RESULTS-rereview-raw.txt
Requires `mafft` on PATH.
"""

import io
import subprocess
import sys

import requests
from Bio import AlignIO, Phylo, SeqIO
from Bio.Align import PairwiseAligner, substitution_matrices
from Bio.Phylo.Consensus import bootstrap_trees, get_support
from Bio.Phylo.TreeConstruction import DistanceCalculator, DistanceTreeConstructor

SEQS = {
    "V5IQW8": "NCU07379 N.crassa (target)",
    "F7VKT3": "Sordaria macrospora (UniRef50 of target)",
    "G4NCR2": "MGG_00342 M.oryzae SF6",
    "G3J390": "CCM_01128 C.militaris SF6",
    "C8VBM8": "FlbB A.nidulans",
    "F5HEL0": "NCU03905 N.crassa SF6",
    "G4N6V5": "MGG_12814 M.oryzae SF6",
    "Q5AW17": "NapA A.nidulans",
    "Q4WMH0": "Yap1 A.fumigatus",
    "Q01663": "Pap1 S.pombe",
    "P19880": "Yap1 S.cerevisiae",
    "P24813": "Cad1/Yap2 S.cerevisiae",
    "P40917": "Cin5/Yap4 S.cerevisiae",
    "Q03935": "Yap6 S.cerevisiae",
    "P40574": "Yap5 S.cerevisiae",
    "Q08182": "Yap7 S.cerevisiae",
    "Q06596": "Arr1/Yap8 S.cerevisiae",
    "Q5AJU7": "Cap1 C.albicans",
    "P38749": "Yap3 S.cerevisiae (SF8, outgroup)",
    "V5IQK5": "NCU01994 N.crassa (SF8, outgroup)",
    "P0C5H8": "KapC A.nidulans (SF11, outgroup)",
}


def fetch(acc: str):
    r = requests.get(f"https://rest.uniprot.org/uniprotkb/{acc}.fasta", timeout=60)
    r.raise_for_status()
    rec = SeqIO.read(io.StringIO(r.text), "fasta")
    rec.id = acc
    rec.description = SEQS[acc]
    return rec


def local_identity(aligner, a, b):
    aln = aligner.align(a, b)[0]
    ident = sum(
        1
        for (s1, e1), (s2, e2) in zip(*aln.aligned)
        for i, j in zip(range(s1, e1), range(s2, e2))
        if a[i] == b[j]
    )
    alen = sum(e1 - s1 for (s1, e1) in aln.aligned[0])
    return ident, alen, aln.score


def main():
    recs = [fetch(a) for a in SEQS]
    seqs = {r.id: str(r.seq) for r in recs}
    aligner = PairwiseAligner()
    aligner.mode = "local"
    aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
    aligner.open_gap_score = -11
    aligner.extend_gap_score = -1

    print("## Sequences")
    for r in recs:
        cterm = str(r.seq)[-150:]
        print(f"{r.id}\t{len(r.seq)}\t{r.description}\tCys_in_Cterm150={cterm.count('C')}")

    for q in ["V5IQW8", "F5HEL0", "C8VBM8"]:
        print(f"\n## Local SW vs {q} ({SEQS[q]})")
        rows = []
        for t in SEQS:
            if t == q:
                continue
            ident, alen, score = local_identity(aligner, seqs[q], seqs[t])
            rows.append((score, t, ident, alen))
        for score, t, ident, alen in sorted(rows, reverse=True):
            print(f"{t}\t{SEQS[t]}\tscore={score:.0f}\tid={ident}/{alen}={ident/alen:.2f}")

    fasta = "".join(f">{r.id}\n{r.seq}\n" for r in recs)
    out = subprocess.run(
        ["mafft", "--localpair", "--maxiterate", "1000", "--quiet", "-"],
        input=fasta, capture_output=True, text=True, check=True,
    ).stdout
    with open("sf6_placement_rereview.aln.fasta", "w") as fh:
        fh.write(out)
    aln = AlignIO.read(io.StringIO(out), "fasta")
    calc = DistanceCalculator("blosum62")
    cons = DistanceTreeConstructor(calc, "nj")
    tree = cons.build_tree(aln)
    tree.root_with_outgroup("P0C5H8")
    print("\n## NJ tree (BLOSUM62 distance, rooted on KapC)")
    Phylo.draw_ascii(tree, file=sys.stdout)

    trees = list(bootstrap_trees(aln, 100, cons))
    support_tree = get_support(tree, trees)
    print("\n## NJ tree with bootstrap support (% of 100 column-resampled NJ replicates)")
    for clade in support_tree.get_nonterminals():
        if clade.confidence is not None:
            members = sorted(t.name for t in clade.get_terminals())
            if len(members) < len(SEQS) - 1:
                print(f"{clade.confidence:.0f}\t{','.join(members)}")
    print(support_tree.format("newick"))

if __name__ == "__main__":
    main()
