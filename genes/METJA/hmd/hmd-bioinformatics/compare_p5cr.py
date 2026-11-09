"""Compare M. jannaschii Hmd (Q58194) with characterised P5C reductases.

Fetches sequences from UniProt REST, makes global (Needleman-Wunsch,
BLOSUM62, gap open -10 / extend -0.5) alignments of Hmd against each
comparator, and reports percent identity over aligned columns, the residue
aligned to Hmd Cys176 (the FeGP iron ligand), a shuffled-sequence identity baseline (20 shuffles of the
comparator, seed 0), a Smith-Waterman local score z-score against 100 further shuffles,
and whether each sequence
carries a [GA]x[GA]xx[GA] dinucleotide-binding-like motif in its first 40 residues.
Run: uv run python genes/METJA/hmd/hmd-bioinformatics/compare_p5cr.py
"""
import random
import re
import urllib.request

from Bio import Align
from Bio.Align import substitution_matrices

ACCS = {
    "Q58194": "Hmd M. jannaschii",
    "O27211": "Hmd M. thermautotrophicus",
    "P0A9L8": "ProC E. coli",
    "P32263": "PRO3 S. cerevisiae",
    "P32322": "PYCR1 human",
    "Q53H96": "PYCR3 human",
}


def fetch(acc):
    url = f"https://rest.uniprot.org/uniprotkb/{acc}.fasta"
    txt = urllib.request.urlopen(url, timeout=60).read().decode()
    return "".join(txt.splitlines()[1:])


def main():
    seqs = {a: fetch(a) for a in ACCS}
    aligner = Align.PairwiseAligner()
    aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
    aligner.open_gap_score = -10
    aligner.extend_gap_score = -0.5
    aligner.mode = "global"
    hmd = seqs["Q58194"]
    print(f"Q58194 length {len(hmd)}; residue 176 = {hmd[175]}")
    for acc, name in ACCS.items():
        s = seqs[acc]
        m = re.search(r"[GA].[GA]..[GA]", s[:40])
        motif = f"{m.group()} at {m.start() + 1}" if m else "none"
        if acc == "Q58194":
            print(f"{acc}\t{name}\tlen {len(s)}\t[GA]x[GA]xx[GA](1-40): {motif}")
            continue
        aln = aligner.align(hmd, s)[0]
        ident = cols = 0
        at176 = "-"
        for (a0, a1), (b0, b1) in zip(*aln.aligned):
            for i, j in zip(range(a0, a1), range(b0, b1)):
                cols += 1
                ident += hmd[i] == s[j]
                if i == 175:
                    at176 = f"{s[j]}{j + 1}"
        rnd = random.Random(0)
        shuf_ids = []
        for _ in range(20):
            sh = "".join(rnd.sample(s, len(s)))
            a2 = aligner.align(hmd, sh)[0]
            si = sc = 0
            for (a0, a1), (b0, b1) in zip(*a2.aligned):
                for i, j in zip(range(a0, a1), range(b0, b1)):
                    sc += 1
                    si += hmd[i] == sh[j]
            shuf_ids.append(100 * si / sc)
        base = sum(shuf_ids) / len(shuf_ids)
        # local (Smith-Waterman) score z-score against 100 shuffles
        loc = Align.PairwiseAligner()
        loc.substitution_matrix = aligner.substitution_matrix
        loc.open_gap_score = -11
        loc.extend_gap_score = -1
        loc.mode = "local"
        real = loc.score(hmd, s)
        null = [loc.score(hmd, "".join(rnd.sample(s, len(s)))) for _ in range(100)]
        mu = sum(null) / len(null)
        sd = (sum((x - mu) ** 2 for x in null) / (len(null) - 1)) ** 0.5
        z = (real - mu) / sd
        print(
            f"{acc}\t{name}\tlen {len(s)}\tidentity {100 * ident / cols:.1f}% "
            f"over {cols} aligned cols (shuffled baseline {base:.1f}%)\tres. aligned to Hmd C176: {at176}"
            f"\tlocal SW score {real:.0f}, z={z:.1f} vs 100 shuffles"
            f"\t[GA]x[GA]xx[GA](1-40): {motif}"
        )


if __name__ == "__main__":
    main()
