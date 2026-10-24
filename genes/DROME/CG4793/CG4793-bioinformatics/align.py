"""Align an annotated target domain to active-site-annotated UniProt controls.
All input filenames and target domain coordinates are CLI arguments. No biological
outcomes are hardcoded. Outputs include all pairwise alignments and site maps.
"""
import argparse,json,hashlib
from pathlib import Path
from Bio import Align,SeqIO
from Bio.Align import substitution_matrices
p=argparse.ArgumentParser();p.add_argument('--target',type=Path,required=True);p.add_argument('--start',type=int,required=True);p.add_argument('--end',type=int,required=True);p.add_argument('--controls',type=Path,nargs='+',required=True);p.add_argument('--refseq',type=Path);p.add_argument('--out',type=Path,required=True);a=p.parse_args()
t=json.loads(a.target.read_text());seq=t['sequence']['value'];domain=seq[a.start-1:a.end]
assert 1<=a.start<=a.end<=len(seq)
results={'target':t['primaryAccession'],'length':len(seq),'sequence_sha256':hashlib.sha256(seq.encode()).hexdigest(),'domain':[a.start,a.end],'comparisons':[]}
if a.refseq:
 ref=SeqIO.read(a.refseq,'fasta');results['refseq']={'id':ref.id,'length':len(ref),'identical':str(ref.seq)==seq}
for control in a.controls:
 c=json.loads(control.read_text());cs=c['sequence']['value'];chain=next(f for f in c['features'] if f['type']=='Chain');start=chain['location']['start']['value'];end=chain['location']['end']['value'];mature=cs[start-1:end]
 al=Align.PairwiseAligner();al.substitution_matrix=substitution_matrices.load('BLOSUM62');al.open_gap_score=-10;al.extend_gap_score=-0.5;al.mode='global'
 x=al.align(mature,domain)[0];mapping={int(i)+start:int(j)+a.start for i,j in zip(*x.indices) if i>=0 and j>=0};sites=[]
 for f in c['features']:
  if f['type']!='Active site':continue
  pos=f['location']['start']['value'];q=mapping.get(pos);sites.append({'control_position':pos,'control_residue':cs[pos-1],'target_position':q,'target_residue':seq[q-1] if q else None,'target_context':seq[max(0,q-6):q+5] if q else None})
 count=int(sum(i>=0 and j>=0 for i,j in zip(*x.indices)));ident=int(sum(mature[i]==domain[j] for i,j in zip(*x.indices) if i>=0 and j>=0))
 results['comparisons'].append({'control':c['primaryAccession'],'control_chain':[start,end],'score':x.score,'aligned_pairs':count,'identity_fraction':ident/count,'target_domain_coverage':count/len(domain),'control_coverage':count/len(mature),'sites':sites,'alignment':str(x)})
a.out.write_text(json.dumps(results,indent=2)+'\n')
print(json.dumps({k:v for k,v in results.items() if k!='comparisons'}));print([(c['control'],c['sites']) for c in results['comparisons']])
