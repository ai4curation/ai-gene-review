"""Summarize an externally computed MSA; coordinates are supplied explicitly."""
import argparse,json,hashlib
from pathlib import Path
from Bio import SeqIO
p=argparse.ArgumentParser();p.add_argument('alignment');p.add_argument('--reference',required=True);p.add_argument('--sites',type=int,nargs='+',required=True);p.add_argument('--output',required=True);args=p.parse_args()
seqs={r.id:str(r.seq) for r in SeqIO.parse(args.alignment,'fasta')};ref=seqs[args.reference]
cols={};n=0
for c,a in enumerate(ref):
 if a!='-':n+=1;cols[n]=c
assert all(x in cols for x in args.sites)
out={'alignment_sha256':hashlib.sha256(Path(args.alignment).read_bytes()).hexdigest(),'reference':args.reference,'sequences':{}}
for name,s in seqs.items():
 positions={};n=0
 for c,a in enumerate(s):
  if a!='-':n+=1;positions[c]=n
 mapped=[]
 for site in args.sites:
  c=cols[site];mapped.append({'reference_position':site,'reference_residue':ref[c],'target_position':positions.get(c),'target_residue':s[c],'aligned_context':s[max(0,c-10):c+11]})
 paired=[(a,b) for a,b in zip(ref,s) if a!='-' and b!='-']
 out['sequences'][name]={'length':len(s.replace('-','')),'paired_residues':len(paired),'identity_over_paired':sum(a==b for a,b in paired)/len(paired),'sites':mapped}
Path(args.output).write_text(json.dumps(out,indent=2)+'\n')
