# /// script
# requires-python = ">=3.10"
# dependencies = ["biopython>=1.83"]
# ///
"""Conservation of the PARD3B-specific PDZ2-PDZ3 linker (LKB1-binding region).

Huo & Macara 2014 (PMID:24859006) map LKB1 binding of Par3L to a short sequence
between PDZ2 and PDZ3 that has no similarity to Par3. Human PARD3B (Q8TEW8)
PDZ2 = 383-468, PDZ3 = 498-585, so the linker is human 469-497.

This script aligns (global, BLOSUM62, open -10, extend -0.5) the human PARD3B
sequence to: donkey A0A9L0JEY6 (local UniProt flat file), mouse Pard3b Q9CSB4
and human PARD3 Q8TEW0 (both fetched from UniProt REST), and reports, for each
human PARD3B region given, the number of aligned and identical residues and the
aligned segments.

Usage:
  uv run --script compare_interpdz_rereview.py <donkey_uniprot.txt> <human_Q8TEW8.fasta> start-end [start-end ...]
"""
import sys
import urllib.request
from Bio import Align
from Bio.Align import substitution_matrices


def parse_flat(path):
    seq, inseq = [], False
    for line in open(path):
        if line.startswith("SQ"):
            inseq = True
            continue
        if line.startswith("//"):
            break
        if inseq:
            seq.append("".join(line.split()))
    return "".join(seq)


def parse_fasta_text(txt):
    return "".join(l.strip() for l in txt.splitlines() if not l.startswith(">"))


def fetch(acc):
    url = f"https://rest.uniprot.org/uniprotkb/{acc}.fasta"
    return parse_fasta_text(urllib.request.urlopen(url).read().decode())


def aligner():
    al = Align.PairwiseAligner()
    al.substitution_matrix = substitution_matrices.load("BLOSUM62")
    al.open_gap_score = -10
    al.extend_gap_score = -0.5
    al.mode = "global"
    return al


def region_report(human, other, regions, label):
    aln = aligner().align(human, other)[0]
    hmap = {}
    for (hs, he), (os_, oe) in zip(*aln.aligned):
        for i, j in zip(range(hs, he), range(os_, oe)):
            hmap[i] = j
    for start, end in regions:
        idx = range(start - 1, end)
        aligned = [i for i in idx if i in hmap]
        ident = sum(human[i] == other[hmap[i]] for i in aligned)
        hseg = human[start - 1:end]
        oseg = "".join(other[hmap[i]] if i in hmap else "-" for i in idx)
        print(f"{label}: human PARD3B {start}-{end}: {len(aligned)} of {end - start + 1} aligned, {ident} identical")
        print(f"  human PARD3B {hseg}")
        print(f"  {label:12s} {oseg}")


donkey_file, human_fasta = sys.argv[1], sys.argv[2]
regions = [tuple(int(x) for x in r.split("-")) for r in sys.argv[3:]]
human = parse_fasta_text(open(human_fasta).read())
others = {
    "donkey": parse_flat(donkey_file),
    "mouse_Pard3b": fetch("Q9CSB4"),
    "human_PARD3": fetch("Q8TEW0"),
}
for label, seq in others.items():
    region_report(human, seq, regions, label)
