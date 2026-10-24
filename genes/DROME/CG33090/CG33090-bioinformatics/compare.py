"""Report exact common termini between arbitrary unaligned FASTA sequences."""
import argparse,json,hashlib
from pathlib import Path
from Bio import SeqIO
p=argparse.ArgumentParser();p.add_argument('fasta');p.add_argument('--reference',required=True);p.add_argument('--output',required=True);a=p.parse_args();s={r.id:str(r.seq) for r in SeqIO.parse(a.fasta,'fasta')};ref=s[a.reference];out={'reference':a.reference,'sequences':{}}
for k,v in s.items():
 n=0
 while n<min(len(v),len(ref)) and v[-n-1]==ref[-n-1]:n+=1
 out['sequences'][k]={'length':len(v),'sha256':hashlib.sha256(v.encode()).hexdigest(),'common_suffix_length':n,'reference_prefix':ref[:len(ref)-n],'target_prefix':v[:len(v)-n]}
Path(a.output).write_text(json.dumps(out,indent=2)+'\n')
