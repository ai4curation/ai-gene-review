"""Offline standard-library replay of fixed source/database evidence.

Run `python reproduce.py` beside its visible modules and input archive.
No network, package installation, gene validation or article-body input is used.
"""
from pathlib import Path
import collections,csv,hashlib,importlib.util,io,json,sys,tarfile,tempfile
sys.dont_write_bytecode=True
D=Path(__file__).resolve().parent
J=lambda p:json.loads(p.read_text())
H=lambda b:hashlib.sha256(b).hexdigest()
def need(v,m):
 if not v:raise ValueError(m)
def digest(x):return H(json.dumps(x,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode())
def mod(name):
 spec=importlib.util.spec_from_file_location(name,D/(name+'.py'));m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m
def coarse(a):return(a['term']['id'],a['evidence_type'],a['original_reference_id'],a.get('qualifier',''),a.get('negated',False),a.get('isoform'))
def tr(r):
 q=r['QUALIFIER'].split('|');return(r['GO TERM'],r['GO EVIDENCE CODE'],r['REFERENCE'],next((v for v in q if v!='NOT'),''),'NOT'in q,r['GENE PRODUCT ID']if'-'in r['GENE PRODUCT ID']else None)
def qr(r):
 q=r['qualifier'].split('|');acc=r['geneProductId'].split(':',1)[1];return(r['goId'],r['goEvidence'],r['reference'],next((v for v in q if v!='NOT'),''),'NOT'in q,acc if'-'in acc else None)
def wf(r):return sorted({x['db']+':'+x['id']for g in r.get('withFrom')or[]for x in g['connectedXrefs']})
def sources(root):
 src=J(root/'bootstrap-v1/source-objects.json');q=J(root/'source-boundary-v1/QuickGO-rows.json')
 old=list(csv.DictReader((root/'historical-goa.tsv').open(),delimiter='\t'));current=list(csv.DictReader((root/'bootstrap-v1/normal-current-goa.tsv').open(),delimiter='\t'));joins=[]
 for i,a in enumerate(src):
  oi=[j for j,r in enumerate(old)if tr(r)==coarse(a)];qi=[j for j,r in enumerate(q)if qr(r)==coarse(a)];ni=[j for j,r in enumerate(current)if tr(r)==coarse(a)]
  need(oi and qi and ni,'uncovered inherited source')
  joins.append({'index':i,'source':a,'historical_tsv_indices':oi,'current_raw_indices':qi,'current_normal_indices':ni,'current_source_ids':[q[j]['id']for j in qi],'current_support_lists':[wf(q[j])for j in qi],'historical_support_lists':[sorted(set(old[j]['WITH/FROM'].split('|'))-{''})for j in oi]})
 need(joins==J(root/'bootstrap-v1/source-joins.json'),'source joins')
 for name,rows in [('current_raw_indices',q),('historical_tsv_indices',old),('current_normal_indices',current)]:
  need(set(j for x in joins for j in x[name])==set(range(len(rows))),'unmatched contexts '+name)
 need(set(map(qr,q))==set(map(tr,current))==set(map(coarse,src)),'source claim-set difference')
 oldfull=collections.Counter((tr(r),tuple(sorted(set(r['WITH/FROM'].split('|'))-{''})))for r in old)
 newfull=collections.Counter((qr(r),tuple(wf(r)))for r in q)
 need(newfull==collections.Counter((tr(r),tuple(sorted(set(r['WITH/FROM'].split('|'))-{''})))for r in current),'current full support mismatch')
 delta={'historical_only':[{'coarse':list(k[0]),'support':list(k[1]),'count':v}for k,v in(oldfull-newfull).items()],'current_only':[{'coarse':list(k[0]),'support':list(k[1]),'count':v}for k,v in(newfull-oldfull).items()]}
 need(delta==J(root/'bootstrap-v1/full-context-delta.json'),'support changes')
 lines=[]
 for i,r in sorted(enumerate(q),key=lambda z:(0 if z[1]['goEvidence']=='IBA'else 1,-int(z[1]['date']),z[1]['goId'])):
  db,acc=r['geneProductId'].split(':',1);w='|'.join(x['db']+':'+x['id']for g in r.get('withFrom')or[]for x in g['connectedXrefs'])
  line='\t'.join([db,acc,r['symbol'],r['qualifier'],r['goId'],r['goName'],r['goAspect'],r['evidenceCode'],r['goEvidence'],r['reference'],w,str(r['taxonId']),r['taxonName'],r['assignedBy'],r['name'],r['date']])
  if line not in lines:lines.append(line)
 tsv=root/'bootstrap-v1/normal-current-goa.tsv';header=tsv.read_text().splitlines()[0]
 need((header+'\n'+'\n'.join(lines)+'\n').encode()==tsv.read_bytes(),'normal raw projection')
 return {'joins':joins,'support_delta':delta,'summary':{'effective_sources':len(src),'raw_contexts':len(q),'normal_contexts':len(current),'historical_contexts':len(old),'all_contexts_covered':True}}
def lateral(root):
 raw=root/'owner-evidence-v1/raw';terms={x['id']:x for x in J(raw/'GO-terms-owner.json')['results']};terms.update({x['id']:x for x in J(raw/'GO-unsaturated-elongation.json')['results']});out=[]
 for i,old,new in [(9,'GO:0006636','GO:0019368'),(16,'GO:0035338','GO:0042761')]:
  rows=[]
  for term in [old,new]:
   paths=J(raw/(term.replace(':','')+'-typedpaths-is_a.json'))['results'];need(paths and all(p and p[0]['child']==term and p[-1]['parent']=='GO:0008150'for p in paths),'typed endpoints')
   edges=sorted({(e['child'],e['relationship'],e['parent'])for p in paths for e in p});need(all(e[1]=='is_a'for e in edges),'typed is_a')
   rows.append({'term':term,'name':terms[term]['name'],'definition':terms[term]['definition']['text'],'paths':len(paths),'edges':[list(e)for e in edges],'ancestors':sorted({e[2]for e in edges})})
  need(old not in rows[1]['ancestors']and new not in rows[0]['ancestors'],'lateral type')
  out.append({'index':i,'before':rows[0],'after':rows[1],'relationship':'lateral'})
 return out
def run():
 manifest=J(D/'input-manifest.json');expected=J(D/'expected-results.json')
 with tempfile.TemporaryDirectory(prefix='elovl4-offline-')as tmp:
  root=Path(tmp)
  with tarfile.open(D/'input-evidence.tar.gz','r:gz')as tf:
   members=tf.getmembers();need(len(members)==len(manifest['files']),'input count');mapping={x['path']:x for x in manifest['files']};need(set(mapping)=={m.name for m in members},'input names')
   for m in members:
    p=Path(m.name);need(m.isfile()and not p.is_absolute()and '..'not in p.parts and p.suffix not in ['.py','.sh','.md','.xml','.html','.pdf'],'input-only safe archive')
    b=tf.extractfile(m).read();pin=mapping[m.name];need(H(b)==pin['sha256']and len(b)==pin['bytes'],'input hash '+m.name);out=root/p;out.parent.mkdir(parents=True,exist_ok=True);out.write_bytes(b)
  s=sources(root);paint=mod('derive_paint');paint.O=root;paint.D=root/'owner-evidence-v1';paint.IBD=paint.D/'raw/PANTHER-current-IBD.gaf';p=paint.run();p.pop('IBD_path')
  db=mod('derive_database');db.O=root;db.E=root/'owner-evidence-v1';b=db.derive();t=lateral(root)
  actual={'source_reconciliation':digest(s),'paint':digest(p),'database':digest(b),'lateral':digest(t)}
  need(actual==expected['projection_sha256'],'derived evidence differs')
  summary=dict(s['summary'],target_amino_acids=p['target_sequence_length'],paint_target=p['target'],paint_path_nodes=len(p['target_path']),paint_terms=len(p['joins']),imported_HuRI_partners=b['huri']['imported_partner_count'],HuRI_pair_records=sum(len(x['records'])for x in b['huri']['imported_pairs']),selected_experimental_donor_records=len(b['donor_records']),rules=[{'id':r['id'],'matched_sets':r['matching_set_indices'],'unknown_sets':r['unknown_set_indices']}for r in b['rules']],lateral_rows=[x['index']for x in t])
  need(summary==expected['summary'],'summary derivation')
  return {'result':'PASS','input_files':len(members),'projection_sha256':actual,'summary':summary,'article_bodies_in_archive':0,'network_calls':0}
if __name__=='__main__':print(json.dumps(run(),indent=2,sort_keys=True))
