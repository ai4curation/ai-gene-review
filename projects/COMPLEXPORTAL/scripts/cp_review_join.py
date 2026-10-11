"""Join ComplexPortal-assigned GOA rows to the action given in each gene review.

Usage (from repo root): uv run python projects/COMPLEXPORTAL/scripts/cp_review_join.py OUT.json
Matches on (GO term, evidence code, reference). Prints action tallies overall, by evidence and by aspect.
"""
import csv, glob, os, yaml, collections, json, sys
rows=[]; nogoa=0; noreview=0
for tsv in glob.glob('genes/*/*/*-goa.tsv'):
    d=os.path.dirname(tsv); gene=os.path.basename(d); org=d.split('/')[1]
    cp=[r for r in csv.DictReader(open(tsv),delimiter='\t') if r.get('ASSIGNED BY')=='ComplexPortal']
    if not cp: continue
    rev=os.path.join(d,f'{gene}-ai-review.yaml')
    if not os.path.exists(rev): noreview+=len(cp); continue
    try: y=yaml.safe_load(open(rev))
    except Exception: continue
    idx=collections.defaultdict(list)
    for a in y.get('existing_annotations') or []:
        t=(a.get('term') or {}).get('id'); idx[(t,a.get('evidence_type'),a.get('original_reference_id'))].append(a)
    for r in cp:
        k=(r['GO TERM'],r['GO EVIDENCE CODE'],r['REFERENCE'])
        hits=idx.get(k,[])
        act=None
        if hits:
            rv=hits[0].get('review') or {}
            act=rv.get('action')
        rows.append(dict(org=org,gene=gene,term=r['GO TERM'],name=r['GO NAME'],aspect=r['GO ASPECT'],ev=r['GO EVIDENCE CODE'],ref=r['REFERENCE'],action=act or 'UNMATCHED',summary=(hits[0].get('review') or {}).get('summary','') if hits else ''))
json.dump(rows,open(sys.argv[1],'w'))
print('cp rows in reviewed genes',len(rows),'| rows in genes without review',noreview)
c=collections.Counter(r['action'] for r in rows); print(c.most_common())
for ev in ['NAS','IDA','IPI','IMP']:
    print(ev, collections.Counter(r['action'] for r in rows if r['ev']==ev).most_common())
for asp in ['biological_process','cellular_component']:
    print(asp, collections.Counter(r['action'] for r in rows if r['aspect']==asp).most_common())
