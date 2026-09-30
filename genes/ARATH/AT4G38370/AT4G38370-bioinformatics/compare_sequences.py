#!/usr/bin/env python3
"""Map a selected UniProt product to a verified prediction-donor reference.
Run with the repository environment: UV_NO_SYNC=1 uv run python compare_sequences.py.
Alignments describe sequence correspondence, not protein expression or activity.
"""
import json
from pathlib import Path
from Bio.Align import PairwiseAligner, substitution_matrices
HERE=Path(__file__).resolve().parent
GENE=HERE.parent.name
selected=json.loads((HERE.parent/f'{GENE}-protnlm-source.json').read_text())['uniprot']
reference=json.loads((HERE.parent/f'{GENE}-prediction-donor.json').read_text())
a=reference['sequence']['value']; b=selected['sequence']['value']
aligner=PairwiseAligner(); aligner.substitution_matrix=substitution_matrices.load('BLOSUM62')
aligner.open_gap_score=-10;aligner.extend_gap_score=-0.5
aln=aligner.align(a,b)[0]
pairs={}
segments=[]
for (x,y),(u,v) in zip(aln.aligned[0],aln.aligned[1]):
 x,y,u,v=map(int,(x,y,u,v));segments.append({'reference_start':x+1,'reference_end':y,'target_start':u+1,'target_end':v,'identical':sum(a[x+k]==b[u+k] for k in range(y-x))})
 for k in range(y-x):pairs[x+k+1]=u+k+1
features=[]
for f in reference.get('features',[]):
 if f['type'] not in {'Active site','Binding site','Transmembrane','Signal','Transit peptide','Domain','Motif','Site'}:continue
 start=f['location']['start'].get('value');end=f['location']['end'].get('value')
 if not start or not end:continue
 mapped=[(p,pairs[p]) for p in range(start,end+1) if p in pairs]
 identities=sum(a[p-1]==b[q-1] for p,q in mapped)
 features.append({'type':f['type'],'description':f.get('description',''),'reference_start':start,'reference_end':end,'mapped_count':len(mapped),'length':end-start+1,'identical_count':identities,'target_positions':[q for p,q in mapped]})
out={'selected_accession':selected['primaryAccession'],'selected_length':len(b),'reference_accession':reference['primaryAccession'],'reference_length':len(a),'method':'Biopython PairwiseAligner global BLOSUM62, gap open -10, extension -0.5','aligned_segments':segments,'reference_features':features,'caveat':'A shared segment does not establish that a truncated product folds, is expressed, localizes, or catalyzes the full-length reaction.'}
(HERE/'results.json').write_text(json.dumps(out,indent=2)+'\n')
(HERE/'alignment.txt').write_text(str(aln)+'\n')
lines=[f'# {GENE}: exact selected product and prediction-donor reference', '',f"Selected {out['selected_accession']} has {len(b)} residues; reference {out['reference_accession']} has {len(a)} residues.",'',out['method']+'.', '', '| Reference interval | Selected interval | Identical residues |','|---|---|---|']
for s in segments:lines.append(f"| {s['reference_start']}–{s['reference_end']} | {s['target_start']}–{s['target_end']} | {s['identical']} |")
lines+=['','Reference feature mapping (sequence coverage does not establish retained function):','', '| Reference feature | Interval | Mapped / length | Identical |','|---|---|---|---|']
for f in features:lines.append(f"| {f['type']}: {f['description']} | {f['reference_start']}–{f['reference_end']} | {f['mapped_count']} / {f['length']} | {f['identical_count']} |")
lines+=['',out['caveat'],'','Inputs are the sibling frozen ProtNLM source and prediction-donor reference JSON files. Reproduce with `UV_NO_SYNC=1 uv run python compare_sequences.py` from this directory.','']
(HERE/'RESULTS.md').write_text('\n'.join(lines))
