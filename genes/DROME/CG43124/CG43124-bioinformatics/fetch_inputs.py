#!/usr/bin/env python3
"""Refresh actual source data; see README before using on a reviewed snapshot."""
import gzip,json,urllib.request
from pathlib import Path
p=Path(__file__).resolve().parent; d=p/'inputs'; d.mkdir(exist_ok=True)
repo=p.parents[3]
for acc in ['P00760','Q90WD8']:
    for ext in ['json','fasta']:
        with urllib.request.urlopen(f'https://rest.uniprot.org/uniprotkb/{acc}.{ext}') as r:
            (d/f'{acc}.{ext}').write_bytes(r.read())
with urllib.request.urlopen('https://www.ebi.ac.uk/interpro/wwwapi/entry/pfam/PF00089?annotation=hmm') as r:
    data=r.read()
(d/'PF00089.hmm').write_bytes(gzip.decompress(data) if data.startswith(b'\x1f\x8b') else data)
with gzip.open(repo/'projects/PROTNLM_EVALUATION/fly-benchmark/uniprot.jsonl.gz','rt') as f:
    rec=next(r for line in f if (r:=json.loads(line))['primaryAccession']=='A0A0B4K7P3')
(d/'A0A0B4K7P3.fasta').write_text('>A0A0B4K7P3\n'+rec['sequence']['value']+'\n')
