"""N-terminal presequence and C-terminal PTS1 analysis for C. puteana MDH A0A5M3MRX5.

Fetches sequences from UniProt REST, aligns the target to its C. puteana paralog
and to the three S. cerevisiae MDH isozymes (MDH1 mitochondrial, MDH2 cytosolic,
MDH3 peroxisomal), and reports:
  * how many residues the target extends N-terminally beyond the start of the
    aligned conserved core (the GAxGGIG Rossmann motif region),
  * composition of that extension (Arg/Lys, Asp/Glu, Ser/Thr, hydrophobic),
  * the last three residues (PTS1 check, canonical [SAC][KRH][LM]).
Run: uv run python targeting_analysis.py > targeting_output.txt
"""
import re
import sys
import urllib.request

from Bio import Align
from Bio.Align import substitution_matrices

ACCS = {
    "A0A5M3MRX5": "C. puteana CONPUDRAFT_136560 (target)",
    "A0A5M3MC96": "C. puteana CONPUDRAFT_157993 (paralog)",
    "P17505": "S. cerevisiae MDH1 (mitochondrial)",
    "P22133": "S. cerevisiae MDH2 (cytosolic)",
    "P32419": "S. cerevisiae MDH3 (peroxisomal)",
}


def fetch(acc):
    url = f"https://rest.uniprot.org/uniprotkb/{acc}.fasta"
    with urllib.request.urlopen(url, timeout=60) as fh:
        lines = fh.read().decode().splitlines()
    return "".join(line.strip() for line in lines if not line.startswith(">"))


def motif_start(seq):
    # Lactate/malate DH NAD-binding glycine-rich motif (GxxGGxG-like)
    m = re.search(r"G[AG].GG[IV]G", seq)
    return m.start() if m else None


def composition(seg):
    return {
        "length": len(seg),
        "basic_RK": sum(seg.count(c) for c in "RK"),
        "acidic_DE": sum(seg.count(c) for c in "DE"),
        "hydroxyl_ST": sum(seg.count(c) for c in "ST"),
        "hydrophobic_AILMFVW": sum(seg.count(c) for c in "AILMFVW"),
    }


def main():
    seqs = {a: fetch(a) for a in ACCS}
    aligner = Align.PairwiseAligner()
    aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
    aligner.open_gap_score = -10
    aligner.extend_gap_score = -0.5
    aligner.mode = "global"
    target = seqs["A0A5M3MRX5"]
    print("accession\tdescription\tlength\tmotif_start(0-based)\tN-terminal_segment_before_motif\tcomposition\tC-term_3")
    for acc, desc in ACCS.items():
        s = seqs[acc]
        ms = motif_start(s)
        seg = s[:ms] if ms is not None else ""
        print(f"{acc}\t{desc}\t{len(s)}\t{ms}\t{seg}\t{composition(seg)}\t{s[-3:]}")
    print()
    print("Pairwise global identity of target to each sequence (identical positions / aligned columns without end gaps):")
    for acc in ACCS:
        if acc == "A0A5M3MRX5":
            continue
        aln = aligner.align(target, seqs[acc])[0]
        ident = cols = 0
        for (a0, a1), (b0, b1) in zip(*aln.aligned):
            for i, j in zip(range(a0, a1), range(b0, b1)):
                cols += 1
                ident += target[i] == seqs[acc][j]
        print(f"{acc}\t{ACCS[acc]}\tidentity={ident}/{cols}={ident / cols:.3f}")


if __name__ == "__main__":
    sys.exit(main())
