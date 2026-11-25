# /// script
# requires-python = ">=3.10"
# dependencies = ["biopython", "requests"]
# ///
"""Align horse TGFBR3 (F7E1V2) to human TGFBR3 (Q03167, canonical) and mouse (O88393),
report identity, gaps and conservation of functionally characterised human residues."""
import requests
from Bio import Align
from Bio.Align import substitution_matrices

def fetch(acc):
    r = requests.get(f"https://rest.uniprot.org/uniprotkb/{acc}.fasta", timeout=60)
    r.raise_for_status()
    return "".join(r.text.splitlines()[1:])

horse = fetch("F7E1V2")
human = fetch("Q03167")
mouse = fetch("O88393")
al = Align.PairwiseAligner(mode="global", open_gap_score=-10, extend_gap_score=-0.5,
                           substitution_matrix=substitution_matrices.load("BLOSUM62"))

def report(name, ref):
    a = al.align(ref, horse)[0]
    # map ref positions -> horse positions
    m = {}
    ident = alnlen = 0
    for (rs, re_), (qs, qe) in zip(*a.aligned):
        for i in range(re_ - rs):
            m[rs + i + 1] = qs + i + 1
            alnlen += 1
            ident += ref[rs + i] == horse[qs + i]
    print(f"== {name}: len ref={len(ref)} horse={len(horse)}; aligned={alnlen}; identity over aligned={ident/alnlen:.3f}")
    # gaps in horse relative to ref
    prev = 0
    for (rs, re_), (qs, qe) in zip(*a.aligned):
        if rs > prev:
            print(f"   ref residues {prev+1}-{rs} have no horse counterpart ({rs-prev} aa)")
        prev = re_
    if prev < len(ref):
        print(f"   ref residues {prev+1}-{len(ref)} have no horse counterpart")
    return m

m = report("human Q03167", human)
# Human residues from UniProt Q03167 features: SIGNAL 1-20, GAG sites S534 and S545, phospho-Thr840 (PubMed:12958365), C-terminal PDZ motif
for pos in (1, 20, 534, 545, 737, 751, 840):
    h = m.get(pos)
    print(f"   human {human[pos-1]}{pos} -> horse {horse[h-1]+str(h) if h else 'gap'}")
print("   human C-term:", human[-10:], " horse C-term:", horse[-10:])
report("mouse O88393", mouse)
print("horse N-term 1-40:", horse[:40])
print("human N-term 1-40:", human[:40])
