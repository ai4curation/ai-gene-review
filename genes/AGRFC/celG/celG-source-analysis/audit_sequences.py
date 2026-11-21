#!/usr/bin/env python3
"""Reproduce archived sequence length/start comparisons; no source mutation."""
from pathlib import Path
import re,json,hashlib
root=Path(__file__).resolve().parents[4]
def seq(p):
 t=p.read_text()
 if p.suffix=='.fasta':return ''.join(t.splitlines()[1:]).replace(' ','')
 t=t.split('\nSQ ')[-1].split('\n',1)[1].split('//')[0]
 return re.sub('[^A-Z]','',t)
paths=[root/'genes/AGRFC/celA/celA-uniprot.txt',root/'genes/AGRFC/celA/celA-source-analysis/AAK90083.1.fasta',root/'genes/AGRFC/celA/celA-source-analysis/A9CEZ7-unisave-v1.txt',root/'genes/AGRFC/celG/celG-uniprot.txt',Path(__file__).parent/'AAK90086.1.fasta',Path(__file__).parent/'AAK90086.2.fasta',Path(__file__).parent/'Q8U4V1-unisave-v1.txt']
records=[{'file':str(p.relative_to(root)),'residues':len(seq(p)),'n_terminal_20':seq(p)[:20],'sequence_sha256':hashlib.sha256(seq(p).encode()).hexdigest()} for p in paths]
a,b,c,g,old,new,uv1=[seq(p) for p in paths]
result={'records':records,'comparisons':{'current_celA_matches_AAK90083_1':a==b,'current_celA_matches_unisave_v1':a==c,'current_celG_matches_AAK90086_2':g==new,'old_celG_matches_unisave_v1':old==uv1,'celA_residue_594':a[593],'celA_584_to_604':a[583:604]},'limitations':'Sequence matches identify archived database records, not exact unpublished constructs. The 2018 CelG 781-residue model and Atu3306 label are not reconciled by these records.'}
print(json.dumps(result,indent=2))
