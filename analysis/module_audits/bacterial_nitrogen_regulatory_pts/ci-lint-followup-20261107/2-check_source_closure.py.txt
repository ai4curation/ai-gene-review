"""Resolve every scientific reference in the three owned reviews, without fetching."""
from pathlib import Path
import json,hashlib
import yaml
A=Path('analysis/module_audits/bacterial_nitrogen_regulatory_pts/psepk-review-20261107')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def refs(x):
 if isinstance(x,dict):
  for k,v in x.items():
   if k in ('id','reference_id','original_reference_id') and isinstance(v,str) and v.startswith(('PMID:','file:','GO_REF:')):yield v
   yield from refs(v)
 elif isinstance(x,list):
  for y in x:yield from refs(y)
ledger={};deps={};missing=[]
for g in ('ptsP','ptsH','ptsN'):
 f=Path(f'genes/PSEPK/{g}/{g}-ai-review.yaml')
 for r in sorted(set(refs(yaml.safe_load(f.read_text())))):
  if r not in ledger:
   if r.startswith('GO_REF:'):ledger[r]={'kind':'annotation method provenance'};continue
   if r.startswith('PMID:'):p=Path('publications/PMID_'+r.split(':')[1]+'.md')
   else:
    n=r.removeprefix('file:');p=Path(n) if Path(n).is_file() else Path('genes')/n
   if not p.is_file():missing.append(r);continue
   deps[str(p)]=sha(p);ledger[r]={'path':str(p),'sha256':sha(p),'reviews':[]}
  if 'reviews' in ledger[r] and str(f) not in ledger[r]['reviews']:ledger[r]['reviews'].append(str(f))
# Raw annotation files are preservation inputs, never biological supports.
for p in Path('genes/PSEPK').glob('pts*/*-goa.tsv'):
 if p.parent.name in ('ptsP','ptsH','ptsN'):deps[str(p)]=sha(p)
for pat in ('PMID_18296519-pmc-body*','PMID_21236318-*','PMID_26224366-*'):
 for p in Path('analysis/module_audits/bacterial_nitrogen_regulatory_pts/literature-acquisition-20261107').glob(pat):deps[str(p)]=sha(p)
p=Path('analysis/module_audits/bacterial_nitrogen_regulatory_pts/acquisition-20261107/module-falcon-attempt.json');deps[str(p)]=sha(p)
assert not missing,missing
print(json.dumps({'result':'PASS','references':ledger,'source_dependencies':deps,'missing':missing},indent=2))
