/Users/cjm/orca/workspaces/ai-gene-review/aigr-modules-taxon/.venv/bin/python -P - <<'PY'
from pathlib import Path
import json
s=Path('analysis/module_audits/bacterial_nonhomologous_end_joining/setup-20261107')
rows=[]
for p in s.glob('*-uniprot.json'):
 d=json.loads(p.read_text())['response']
 for x in d.get('results',[d]):
  rows.append({'accession':x['primaryAccession'],'entry':x['uniProtkbId'],'length':x['sequence']['length'],'panther':[c for c in x.get('uniProtKBCrossReferences',[]) if c['database']=='PANTHER'],'domains':[c for c in x.get('uniProtKBCrossReferences',[]) if c['database'] in ['InterPro','Pfam']]})
(s/'family-domain-map.json').write_text(json.dumps(rows,indent=2)+'\n')
for x in rows:print(json.dumps({k:v for k,v in x.items() if k!='domains'}))
PY
 head -5 interpro/panther/PTHR42705/PTHR42705-entries.csv
 head -5 interpro/panther/PTHR42705/PTHR42705-paint.tsv
