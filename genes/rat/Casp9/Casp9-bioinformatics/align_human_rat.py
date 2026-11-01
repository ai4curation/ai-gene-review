"""Global alignment of human CASP9 (P55211) and rat Casp9 (Q9JHK1).

Maps functionally annotated human residues (catalytic dyad, ABL1 and AKT
phosphosites) onto the rat sequence. Run from the repository root:

    uv run python genes/rat/Casp9/Casp9-bioinformatics/align_human_rat.py
"""
from Bio import Align
from Bio.Align import substitution_matrices

HUMAN = "genes/human/CASP9/CASP9-uniprot.txt"
RAT = "genes/rat/Casp9/Casp9-uniprot.txt"
SITES = {
    237: "catalytic His (human ACT_SITE)",
    287: "catalytic Cys (human ACT_SITE)",
    125: "Thr125, phosphorylated by MAPK1 (inhibitory)",
    153: "Tyr153, phosphorylated by ABL1",
    196: "Ser196, phosphorylated by AKT1 (inhibitory)",
}


def read_seq(path):
    text = open(path).read()
    block = text.split("\nSQ ")[1].split("\n", 1)[1].split("//")[0]
    return "".join(c for c in block if c.isalpha())


def main():
    h, r = read_seq(HUMAN), read_seq(RAT)
    aligner = Align.PairwiseAligner()
    aligner.mode = "global"
    aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
    aligner.open_gap_score = -10
    aligner.extend_gap_score = -0.5
    aln = aligner.align(h, r)[0]
    mapping = {}
    for (hs, he), (rs, _re) in zip(*aln.aligned):
        for i in range(he - hs):
            mapping[hs + i + 1] = rs + i + 1
    ident = sum(1 for k, v in mapping.items() if h[k - 1] == r[v - 1])
    print(f"human length {len(h)}, rat length {len(r)}")
    print(f"aligned positions {len(mapping)}, identical {ident} "
          f"({100 * ident / len(mapping):.1f}% of aligned)")
    print("human_pos\thuman_res\trat_pos\trat_res\thuman_window\trat_window\tnote")
    for pos, note in sorted(SITES.items()):
        rp = mapping.get(pos)
        hw = h[max(0, pos - 6):pos + 5]
        rw = r[max(0, rp - 6):rp + 5] if rp else "-"
        print(f"{pos}\t{h[pos-1]}\t{rp}\t{r[rp-1] if rp else '-'}\t{hw}\t{rw}\t{note}")


if __name__ == "__main__":
    main()
