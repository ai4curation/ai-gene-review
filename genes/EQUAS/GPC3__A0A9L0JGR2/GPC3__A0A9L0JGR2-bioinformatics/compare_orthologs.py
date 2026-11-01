# /// script
# requires-python = ">=3.10"
# dependencies = ["biopython>=1.81"]
# ///
"""Compare donkey GPC3 (A0A9L0JGR2) with human GPC3 (P51654) and mouse Gpc3 (Q8CFZ4).

Usage (from this folder):
  uv run --script compare_orthologs.py ../GPC3__A0A9L0JGR2-uniprot.txt \
      human-GPC3-P51654.fasta mouse-Gpc3-Q8CFZ4.fasta

Global alignment, BLOSUM62, gap open -10, gap extend -0.5. Reports identity, the
donkey residues aligned to the human signal peptide (P51654 FT SIGNAL 1..24) and to the
human functional sites taken from the human UniProt feature table (convertase site
358..359, heparan sulfate attachment S495/S509, GPI-anchor N554). Nothing is hardcoded
except the human site positions, which are read from P51654 features.
"""
import sys

from Bio import Align
from Bio.Align import substitution_matrices

HUMAN_SITES = {
    358: "convertase cleavage site, P1 (SITE 358..359)",
    359: "convertase cleavage site, P1' (SITE 358..359)",
    495: "heparan sulfate attachment (CARBOHYD 495)",
    509: "heparan sulfate attachment (CARBOHYD 509)",
    554: "GPI-anchor amidated asparagine (LIPID 554)",
}


def read_uniprot_seq(path):
    seq, in_sq = [], False
    for line in open(path):
        if line.startswith("SQ"):
            in_sq = True
            continue
        if in_sq:
            if line.startswith("//"):
                break
            seq.append(line.replace(" ", "").strip())
    return "".join(seq)


def read_fasta(path):
    lines = open(path).read().splitlines()
    return lines[0].split("|")[1], "".join(x.strip() for x in lines[1:])


def align(a, b):
    aligner = Align.PairwiseAligner()
    aligner.mode = "global"
    aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
    aligner.open_gap_score = -10
    aligner.extend_gap_score = -0.5
    aln = aligner.align(a, b)[0]
    bmap = {}
    paired = ident = 0
    for (s1, e1), (s2, e2) in zip(*aln.aligned):
        for i in range(e1 - s1):
            paired += 1
            ident += a[s1 + i] == b[s2 + i]
            bmap[s2 + i + 1] = s1 + i + 1
    return paired, ident, bmap


donkey = read_uniprot_seq(sys.argv[1])
print(f"Donkey A0A9L0JGR2 length {len(donkey)}")
for path in sys.argv[2:]:
    acc, other = read_fasta(path)
    paired, ident, omap = align(donkey, other)
    print(f"\n== vs {acc} (length {len(other)}) ==")
    print(f"Identical paired residues: {ident}/{paired} ({100 * ident / paired:.2f}%)")
    print(f"Donkey residues 1..24: {donkey[:24]}")
    print(f"{acc} residues 1..24:    {other[:24]}")
    sp_ident = sum(1 for p in range(1, 25) if p in omap and donkey[omap[p] - 1] == other[p - 1])
    print(f"Signal-peptide positions 1..24 identical: {sp_ident}/24")
    if acc == "P51654":
        for pos, desc in HUMAN_SITES.items():
            d = omap.get(pos)
            dres = donkey[d - 1] if d else "-"
            print(f"Human {other[pos - 1]}{pos} ({desc}) -> donkey {dres}{d if d else ''}")
