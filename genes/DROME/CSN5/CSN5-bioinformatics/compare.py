"""Global protein alignment using BLOSUM62, gap open -10, extension -0.5."""
import argparse,json
from pathlib import Path
from Bio.Align import PairwiseAligner,substitution_matrices
p=argparse.ArgumentParser();p.add_argument('target');p.add_argument('reference');p.add_argument('output');a=p.parse_args()
t=json.loads(Path(a.target).read_text());r=json.loads(Path(a.reference).read_text());s=t['sequence']['value'];q=r['sequence']['value']; x=PairwiseAligner();x.substitution_matrix=substitution_matrices.load('BLOSUM62');x.open_gap_score=-10;x.extend_gap_score=-0.5;al=x.align(q,s)[0]; (o:=Path(a.output)).mkdir(exist_ok=True);(o/'alignment.txt').write_text(str(al));mapping={};eq=0
for (a,b),(c,d) in zip(al.aligned[0],al.aligned[1]):
 for i,j in zip(range(a,b),range(c,d)):mapping[int(i+1)]=int(j+1);eq+=int(q[i]==s[j])
feat=[]
for f in r.get('features',[]):
 if f['type'] in ['Active site','Binding site','Domain','Region','Motif','Site']:
  start=f['location']['start'].get('value');end=f['location']['end'].get('value');n=sum(k in mapping for k in range(start,end+1)) if start and end else 0
  feat.append({'type':f['type'],'description':f.get('description'),'reference_start':start,'reference_end':end,'aligned_reference_residues':n,'target_start':mapping.get(start),'target_end':mapping.get(end),'single_residue_target':s[mapping[start]-1] if start==end and start in mapping else None})
(o/'results.json').write_text(json.dumps({'target':t['primaryAccession'],'reference':r['primaryAccession'],'target_length':len(s),'reference_length':len(q),'identical_residues':eq,'aligned_pairs':len(mapping),'reference_coverage':len(mapping)/len(q),'target_coverage':len(mapping)/len(s),'mapped_features':feat},indent=2)+'\n')
