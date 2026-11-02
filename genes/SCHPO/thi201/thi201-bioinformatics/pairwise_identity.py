import sys
from Bio import Align
from Bio.Align import substitution_matrices
def seq(path):
    s=[];on=False
    for l in open(path):
        if l.startswith('SQ'): on=True; continue
        if l.startswith('//'): break
        if on: s.append(l.strip().replace(' ',''))
    return ''.join(s)
files=dict(a.split('=') for a in sys.argv[1:])
seqs={k:seq(v) for k,v in files.items()}
al=Align.PairwiseAligner(); al.substitution_matrix=substitution_matrices.load('BLOSUM62'); al.open_gap_score=-10; al.extend_gap_score=-0.5; al.mode='local'
ks=list(seqs)
for i in range(len(ks)):
    for j in range(i+1,len(ks)):
        a=al.align(seqs[ks[i]],seqs[ks[j]])[0]
        idn=sum(1 for x,y in zip(*a) if x==y and x!='-'); L=sum(1 for x,y in zip(*a) if x!='-' and y!='-')
        print(f"{ks[i]}\t{ks[j]}\tlen{len(seqs[ks[i]])}/{len(seqs[ks[j]])}\taligned {L}\tid {idn/L:.2f}")
