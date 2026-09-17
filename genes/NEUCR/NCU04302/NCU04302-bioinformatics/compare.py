# /// script
# requires-python = ">=3.12"
# dependencies = ["biopython==1.85"]
# ///
"""Global BLOSUM62 alignment of UniProt JSON sequences; no biological labels inferred."""
import argparse,json,hashlib
from pathlib import Path
from Bio.Align import PairwiseAligner,substitution_matrices
p=argparse.ArgumentParser();p.add_argument('query',type=Path);p.add_argument('references',type=Path,nargs='+');p.add_argument('--output',type=Path,required=True);a=p.parse_args()
q=json.loads(a.query.read_text());qs=q['sequence']['value'];aligner=PairwiseAligner(mode='global',substitution_matrix=substitution_matrices.load('BLOSUM62'),open_gap_score=-10,extend_gap_score=-0.5)
rows=[]
for path in a.references:
 r=json.loads(path.read_text());rs=r['sequence']['value'];al=aligner.align(qs,rs)[0];x,y=al[0],al[1];pairs=[(u,v) for u,v in zip(x,y) if u!='-' and v!='-'];matches=sum(u==v for u,v in pairs)
 rows.append({'query':q['primaryAccession'],'reference':r['primaryAccession'],'query_length':len(qs),'reference_length':len(rs),'query_sha256':hashlib.sha256(qs.encode()).hexdigest(),'reference_sha256':hashlib.sha256(rs.encode()).hexdigest(),'score':al.score,'aligned_residue_pairs':len(pairs),'identities':matches,'identity_over_residue_pairs':matches/len(pairs),'query_coverage':len(pairs)/len(qs),'reference_coverage':len(pairs)/len(rs),'query_alignment':x,'reference_alignment':y})
a.output.write_text(json.dumps({'method':'global BLOSUM62; gap open -10; extension -0.5; first optimal alignment','results':rows},indent=2)+'\n')
print(json.dumps([{k:v for k,v in r.items() if 'alignment' not in k and 'sha256' not in k} for r in rows],indent=2))
