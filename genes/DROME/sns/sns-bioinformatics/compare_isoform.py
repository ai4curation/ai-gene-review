"""Compare arbitrary UniProt JSON sequence against a FASTA isoform, retaining alignment."""
import argparse,json,hashlib
from pathlib import Path
from Bio import Align,SeqIO
from Bio.Align import substitution_matrices
p=argparse.ArgumentParser();p.add_argument('--target',type=Path,required=True);p.add_argument('--reference',type=Path,required=True);p.add_argument('--out',type=Path,required=True);a=p.parse_args();j=json.loads(a.target.read_text());s=j['sequence']['value'];r=SeqIO.read(a.reference,'fasta');t=str(r.seq);al=Align.PairwiseAligner();al.mode='global';al.substitution_matrix=substitution_matrices.load('BLOSUM62');al.open_gap_score=-10;al.extend_gap_score=-0.5;x=al.align(t,s)[0];pairs=[(int(i),int(k)) for i,k in zip(*x.indices) if i>=0 and k>=0];blocks=[]
for n in range(x.coordinates.shape[1]-1):
 r0,r1=map(int,x.coordinates[0,n:n+2]);q0,q1=map(int,x.coordinates[1,n:n+2]);
 if r1-r0!=q1-q0:blocks.append({'reference_span':[r0+1,r1],'target_span':[q0+1,q1],'reference_sequence':t[r0:r1],'target_sequence':s[q0:q1]})
out={'target':j['primaryAccession'],'length':len(s),'sha256':hashlib.sha256(s.encode()).hexdigest(),'reference':r.id,'reference_length':len(t),'aligned_pairs':len(pairs),'identical_pairs':sum(t[i]==s[k] for i,k in pairs),'indels':blocks,'alignment':str(x)};a.out.write_text(json.dumps(out,indent=2)+'\n');print({k:v for k,v in out.items() if k!='alignment'})
