import json
from pathlib import Path
from Bio import SeqIO
p=Path(__file__).parent
j={a:json.loads((p/(a+'.json')).read_text()) for a in ['Q8MST5','E1JIZ8','Q9VAX7']}
s=j['Q8MST5']['sequence']['value'];record=SeqIO.read(p/'NM_001170282.2.gb','genbank');ref=next(f.qualifiers['translation'][0] for f in record.features if f.type=='CDS')
out={'target':'Q8MST5','length':len(s),'refseq_identical':s==ref,'comparisons':{}}
for a,x in j.items():
 t=x['sequence']['value'];out['comparisons'][a]={'length':len(t),'identical':s==t,'differences':[{'position':i+1,'target':c,'other':d} for i,(c,d) in enumerate(zip(s,t)) if c!=d]}
(p/'results.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
