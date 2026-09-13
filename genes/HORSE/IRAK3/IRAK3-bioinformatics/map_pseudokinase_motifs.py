"""Map published human IRAK3 motifs into the frozen horse UniProt sequence.

Human positions: PMID:33238146. Sequence correspondence is not an activity assay.
Run with UV_NO_SYNC=1 uv run python map_pseudokinase_motifs.py.
"""
from pathlib import Path
import json,hashlib
from Bio.Align import PairwiseAligner,substitution_matrices
here=Path(__file__).resolve().parent
root=here.parents[3]
def seq(p):
 text=p.read_text();return ''.join(c for c in text.split('\nSQ ',1)[1].split('\n',1)[1].split('//')[0] if c.isalpha())
a=seq(root/'genes/human/IRAK3/IRAK3-uniprot.txt');b=seq(root/'genes/HORSE/IRAK3/IRAK3-uniprot.txt')
x=PairwiseAligner();x.substitution_matrix=substitution_matrices.load('BLOSUM62');x.open_gap_score=-10;x.extend_gap_score=-0.5;aln=x.align(a,b)[0];pairs={}
for (s,e),(u,v) in zip(aln.aligned[0],aln.aligned[1]):
 for off in range(int(e-s)):pairs[int(s)+off+1]=int(u)+off+1
rows=[]
for label,s,e in [('catalytic-loop CGS',291,293),('Mg-binding-loop DFA',311,313)]:
 mapped=[pairs.get(i) for i in range(s,e+1)]
 rows.append({'motif':label,'human_positions':list(range(s,e+1)),'human_sequence':a[s-1:e],'horse_positions':mapped,'horse_sequence':''.join(b[i-1] if i else '-' for i in mapped)})
out={'reference':'Q9Y616','target':'A0A3Q2HDT6','source':'PMID:33238146','method':'Global BLOSUM62; gap open -10, extension -0.5','sequence_sha256':{'human':hashlib.sha256(a.encode()).hexdigest(),'horse':hashlib.sha256(b.encode()).hexdigest()},'motifs':rows,'limits':'Current frozen UniProt sequences, not an assay or verification of prediction-time input. Motif conservation does not establish absence of every possible catalytic mechanism.'}
(here/'pseudokinase-motifs.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(rows,indent=2))
