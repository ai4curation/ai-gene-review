# /// script
# requires-python = ">=3.10"
# dependencies = ["biopython", "requests"]
# ///
"""GFG-motif and EF-hand loop scan for CG32086-RA (Q8IQG0) versus human EFHB.

PMID:38538594 defines GFG repeats (~31 residues, Gly-Phe-Gly signature) as the
microtubule-lattice-binding repeats of FAP21/EFHB. This script:
  1. fetches Q8IQG0, human EFHB (Q8N7U6) and the two fly PTHR12086:SF12 paralogs;
  2. lists every exact 'GFG' tripeptide and every looser G-[FYW]-G tripeptide;
  3. globally aligns Q8IQG0 to Q8N7U6 (BLOSUM62, open -11, extend -1) and reports,
     for each human GFG, the aligned fly residues, so conservation of motif
     positions (not just motif counts) can be judged;
  4. scans all sequences for the PROSITE PS00018 EF-hand Ca-binding loop.
It reports what it finds; it does not decide whether a sequence is a MIP.
Run: uv run gfg_motif_scan.py
"""
import re

import requests
from Bio import Align
from Bio.Align import substitution_matrices

ACCS = {
    "Q8IQG0": "fly CG32086-RA (PTHR12086:SF12)",
    "Q8N7U6": "human EFHB/CFAP21 (PTHR12086:SF12)",
    "Q7KUG5": "fly FBgn0053489 (PTHR12086:SF12)",
    "Q8MST3": "fly FBgn0053490 (PTHR12086:SF12)",
}
PS00018 = re.compile(
    r"(?=(D[^W][DNS][^ILVFYW][DENSTG][DNQGHRK][^GP][LIVMC][DENQSTAGC]..[DE]))"
)


def fetch(acc: str) -> str:
    r = requests.get(f"https://rest.uniprot.org/uniprotkb/{acc}.fasta", timeout=60)
    r.raise_for_status()
    return "".join(r.text.splitlines()[1:])


seqs = {a: fetch(a) for a in ACCS}
print("## Sequences")
for a, s in seqs.items():
    print(f"{a}\t{len(s)} aa\t{ACCS[a]}")

print("\n## Exact GFG and G-[FYW]-G tripeptides (1-based start)")
for a, s in seqs.items():
    exact = [m.start() + 1 for m in re.finditer(r"(?=GFG)", s)]
    loose = [m.start() + 1 for m in re.finditer(r"(?=G[FYW]G)", s)]
    print(f"{a}\tGFG n={len(exact)} {exact}\tG[FYW]G n={len(loose)} {loose}")

print("\n## PS00018 EF-hand Ca-binding loop matches")
for a, s in seqs.items():
    hits = [(m.start() + 1, m.group(1)) for m in PS00018.finditer(s)]
    print(f"{a}\t{hits if hits else 'none'}")

aligner = Align.PairwiseAligner()
aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
aligner.open_gap_score = -11
aligner.extend_gap_score = -1
aligner.mode = "global"
aligner.end_gap_score = 0  # free end gaps: human has an N-terminal extension
fly, hum = seqs["Q8IQG0"], seqs["Q8N7U6"]
aln = aligner.align(fly, hum)[0]

# map human position -> fly position
h2f: dict[int, int] = {}
for (fs, fe), (hs, he) in zip(*aln.aligned):
    for k in range(fe - fs):
        h2f[hs + k] = fs + k

print("\n## Global alignment Q8IQG0 vs Q8N7U6 (free end gaps)")
print(f"score {aln.score}")
pairs = [(h2f[h], h) for h in sorted(h2f)]
ident = sum(1 for f, h in pairs if fly[f] == hum[h])
print(f"aligned pairs {len(pairs)}; identical {ident} ({ident / len(pairs):.2f})")
print(f"human span aligned: {min(h2f) + 1}-{max(h2f) + 1}; fly span: {min(h2f.values()) + 1}-{max(h2f.values()) + 1}")

print("\n## Human EFHB G-[FYW]-G motifs and aligned fly residues")
for m in re.finditer(r"(?=G[FYW]G)", hum):
    h = m.start()
    tri = hum[h:h + 3]
    fpos = [h2f.get(h + k) for k in range(3)]
    if None in fpos:
        print(f"human {h + 1} {tri}\tfly: unaligned")
    else:
        ftri = "".join(fly[p] for p in fpos)
        print(f"human {h + 1} {tri}\tfly {fpos[0] + 1} {ftri}\t{'conserved' if re.fullmatch('G[FYW]G', ftri) else 'not conserved'}")

print("\n## Human EFHB EF-hand region 561-632 (UniProt EF-hand domains) and aligned fly residues")
print("Canonical loop positions 1,3,5,7,9,12 of human 610-621 (DVDNDGFINYLE) are the Ca ligands.")
loop_start = 610 - 1
print("pos\thuman\tfly_pos\tfly")
for h in range(560, 632):
    f = h2f.get(h)
    mark = "*" if loop_start <= h < loop_start + 12 and (h - loop_start) in (0, 2, 4, 6, 8, 11) else ""
    print(f"{h + 1}{mark}\t{hum[h]}\t{'-' if f is None else f + 1}\t{'-' if f is None else fly[f]}")
