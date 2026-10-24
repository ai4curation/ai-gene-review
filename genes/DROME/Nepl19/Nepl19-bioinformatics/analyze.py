import json,subprocess,hashlib
from pathlib import Path
from Bio import SeqIO
p=Path(__file__).parent
records=[json.loads((p/x).read_text()) for x in ['P08473.json','Q61391.json','../Nepl19-uniprot-source.json']]
(p/'input.fasta').write_text(''.join('>'+j['primaryAccession']+'\n'+j['sequence']['value']+'\n' for j in records))
reference=records[0]; sites=[f for f in reference['features'] if f['type']=='Active site' or (f['type']=='Binding site' and f.get('ligand',{}).get('name')=='Zn(2+)')]
outputs={}
for mode,flag in [('linsi','--localpair'),('ginsi','--globalpair')]:
 run=subprocess.run(['mafft',flag,'--maxiterate','1000',str(p/'input.fasta')],capture_output=True,text=True,check=True)
 (p/(mode+'.fasta')).write_text(run.stdout);(p/(mode+'-stderr.txt')).write_text(run.stderr)
 seqs={s.id:str(s.seq) for s in SeqIO.parse(p/(mode+'.fasta'),'fasta')};ref=seqs[reference['primaryAccession']];refmap={};n=0
 for col,aa in enumerate(ref):
  if aa!='-':n+=1;refmap[n]=col
 rows=[]
 for f in sites:
  pos=f['location']['start']['value'];col=refmap[pos];row={'reference_position':pos,'reference_residue':ref[col],'role':f.get('ligand',{}).get('name',f['type'])}
  for acc,s in seqs.items():row[acc]={'position':sum(x!='-' for x in s[:col+1]) if s[col]!='-' else None,'residue':s[col],'window':s[max(0,col-8):col+9]}
  rows.append(row)
 outputs[mode]=rows
outputs['input_hashes']={j['primaryAccession']:hashlib.sha256(j['sequence']['value'].encode()).hexdigest() for j in records}
outputs['strategies_agree']=outputs['linsi']==outputs['ginsi'];(p/'results.json').write_text(json.dumps(outputs,indent=2)+'\n');print(json.dumps(outputs,indent=2))
