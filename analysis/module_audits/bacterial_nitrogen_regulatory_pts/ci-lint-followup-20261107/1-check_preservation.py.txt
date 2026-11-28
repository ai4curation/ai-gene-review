"""Read-only ordered-payload and protected-file audit for the PSEPK review follow-up."""
from pathlib import Path
import hashlib
import json
import yaml
A=Path('analysis/module_audits/bacterial_nitrogen_regulatory_pts/psepk-review-20261107')
before=json.loads((A/'before.json').read_text())
def digest(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def payload(row): return {k:v for k,v in row.items() if k not in ('review','retired')}
report={'genes':{},'protected_files':{},'machine_rows':0,'historical_new_rows':0,'newly_authored_rows':0,'retired_historical_new_rows':0}
for g,old in before['reviews'].items():
 p=Path(f'genes/PSEPK/{g}/{g}-ai-review.yaml');new=yaml.safe_load(p.read_text());o=old['existing_annotations'];n=new['existing_annotations']
 assert len(o)==len(n),(g,'row count')
 assert [payload(r) for r in o]==[payload(r) for r in n],(g,'ordered payload')
 oldnew=[i for i,r in enumerate(o) if r['review']['action']=='NEW'];newnew=[i for i,r in enumerate(n) if r['review']['action']=='NEW'];assert oldnew==newnew,(g,'NEW lifecycle')
 assert not any(r['review']['action']=='PENDING' for r in n)
 retired=[i for i,r in enumerate(n) if r.get('retired')];assert all(i in oldnew for i in retired)
 report['genes'][g]={'rows':len(n),'machine_rows':len(n)-len(oldnew),'historical_new_rows':len(oldnew),'retired_indices_zero_based':retired,'ordered_payloads_and_qualifiers_unchanged':True,'status':new['status']}
 report['machine_rows']+=len(n)-len(oldnew);report['historical_new_rows']+=len(oldnew);report['retired_historical_new_rows']+=len(retired)
for name,record in before['files'].items():
 if name.endswith(('-ai-review.yaml','-ai-review.html','-notes.md')):continue
 p=Path(name);assert digest(p)==record['sha256'],name;assert oct(p.stat().st_mode&0o777)==record['mode'],name
 report['protected_files'][name]=record
assert report['machine_rows']==11 and report['historical_new_rows']==7
assert report['retired_historical_new_rows']==1
report['result']='PASS'
print(json.dumps(report,indent=2))
