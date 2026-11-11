#!/usr/bin/env python3
"""Extract a workbook sequence and compare longest translated ORFs with official proteins.
No biological verdict is encoded. Requires openpyxl3.1.5 and biopython1.85.
"""
import argparse,json,hashlib,re,difflib
from pathlib import Path
import openpyxl
from Bio.Seq import Seq
p=argparse.ArgumentParser();p.add_argument('--workbook',type=Path,required=True);p.add_argument('--sheet',required=True);p.add_argument('--gene',required=True);p.add_argument('--uniprot',type=Path,required=True);p.add_argument('--output',type=Path,required=True);p.add_argument('--fasta',type=Path,action='append',default=[]);a=p.parse_args()
w=openpyxl.load_workbook(a.workbook,read_only=True,data_only=True);s=w[a.sheet];rows=list(s.values);header=next((i,r)for i,r in enumerate(rows)if 'Sequence' in r);seqcol=list(header[1]).index('Sequence');matches=[(i+1,r)for i,r in enumerate(rows)if r[0]==a.gene];assert len(matches)==1;row,r=matches[0];dna=re.sub(r'\s','',r[seqcol]).upper();assert set(dna)<={'A','C','G','T'},set(dna)
u=json.loads(a.uniprot.read_text());refs={u['primaryAccession']:u['sequence']['value']}
for f in a.fasta:refs[f.stem]=''.join(f.read_text().splitlines()[1:])
candidates=[]
for strand,nt in [('+',dna),('-',str(Seq(dna).reverse_complement()))]:
 for frame in range(3):
  aa=str(Seq(nt[frame:len(nt)-(len(nt)-frame)%3]).translate());start=0
  for fragment in aa.split('*'):
   first=fragment.find('M')
   if first>=0:candidates.append({'strand':strand,'frame':frame,'nt_start_0based':frame+(start+first)*3,'sequence':fragment[first:]})
   start+=len(fragment)+1
best=sorted(candidates,key=lambda x:len(x['sequence']),reverse=True)[:3];out=[]
for x in best:
 seq=x.pop('sequence');x.update({'aa_length':len(seq),'aa_sha256':hashlib.sha256(seq.encode()).hexdigest(),'first30':seq[:30],'last30':seq[-30:],'comparisons':[]})
 for name,ref in refs.items():
  blocks=difflib.SequenceMatcher(None,seq,ref,autojunk=False).get_matching_blocks();nonempty=[b for b in blocks if b.size]
  x['comparisons'].append({'reference':name,'reference_length':len(ref),'exact_equal':seq==ref,'exact_substring_start_0based':ref.find(seq),'matching_blocks':[{'query_start':b.a,'reference_start':b.b,'length':b.size}for b in sorted(nonempty,key=lambda z:z.size,reverse=True)[:5]],'total_exact_matching_residues':sum(b.size for b in nonempty)})
 out.append(x)
result={'workbook_sha256':hashlib.sha256(a.workbook.read_bytes()).hexdigest(),'gene':a.gene,'sheet':a.sheet,'physical_row':row,'literal_metadata':{str(header[1][i]):v for i,v in enumerate(r)if v is not None and i!=seqcol},'dna_length':len(dna),'dna_sha256':hashlib.sha256(dna.encode()).hexdigest(),'official_reference_sha256':hashlib.sha256(a.uniprot.read_bytes()).hexdigest(),'longest_orfs':out}
a.output.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
