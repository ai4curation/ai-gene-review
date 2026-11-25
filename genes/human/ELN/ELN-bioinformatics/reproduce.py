#!/usr/bin/env python3
"""Reconstruct saved ELN database evidence offline with Python's standard library.

All executable reconstruction logic is visible in this file. The archive holds
only the exact raw/inputs files listed by input-manifest.json.
"""
from pathlib import Path, PurePosixPath
import collections,hashlib,json
import tarfile,tempfile
BASE=Path(__file__).resolve().parent
D=BASE;R=D/'raw';J=lambda p:json.loads(p.read_text())
EDGES=('input','output','hasComponent','repeatedUnit','hasMember','hasCandidate','catalystActivity','physicalEntity')
def need(value,message):
 if not value:raise ValueError(message)
def derive():
 nodes={}
 for p in sorted(R.glob('Reactome-*.json')):
  if p.name.endswith('.receipt.json'):continue
  x=J(p)
  if 'dbId'in x:nodes[x['dbId']]=(x,p)
 sources=J(D/'inputs/source-objects.json');rows=[]
 for i,s in enumerate(sources):
  ref=s['original_reference_id']
  if not ref.startswith('Reactome:'):continue
  root=int(ref.rsplit('-',1)[1]);witnesses=[];unexpanded=[]
  def walk(n,path):
   if n not in nodes:unexpanded.append(dict(dbId=n,path=path));return
   x,p=nodes[n];r=x.get('referenceEntity',{})
   if r.get('identifier')=='P15502':witnesses.append(dict(path=path,node=n,class_name=x['schemaClass'],reference_dbId=r['dbId'],reference_identifier=r['identifier'],start=x.get('startCoordinate'),end=x.get('endCoordinate'),compartments=[dict(id='GO:'+v['accession'],name=v['displayName'])for v in x.get('compartment',[])],raw_path=str(p.relative_to(D))))
   for k in EDGES:
    vals=x.get(k,[]);vals=vals if isinstance(vals,list)else[vals]
    for ordinal,v in enumerate(vals):
     c=v['dbId']if isinstance(v,dict)else v
     if c in[a['to']for a in path]:continue
     walk(c,path+[dict(from_id=n,edge=k,ordinal=ordinal,to=c)])
  walk(root,[]);rows.append(dict(index=i,source=s,root=root,root_class=nodes[root][0]['schemaClass'],root_name=nodes[root][0]['displayName'],chimeric=nodes[root][0].get('isChimeric',False),witnesses=witnesses,unexpanded_branches=unexpanded))
 q=J(R/'QuickGO-P54320-page1.json');terms=sorted({s['term']['id']for s in sources if any('P54320'in a for a in s.get('supporting_entities',[]))})
 joins={term:[dict(raw_index=i,record=r)for i,r in enumerate(q['results'])if r['goId']==term]for term in terms};u=J(R/'UniProt-P54320.json')
 return dict(reactome_rows=rows,donor_total=q['numberOfHits'],donor_saved_rows=len(q['results']),donor_page_info=q['pageInfo'],donor_exact_term_joins=joins,donor_uniprot_ensembl=[a for a in u['uniProtKBCrossReferences']if a['database']=='Ensembl'],homology=J(R/'Ensembl-Eln-orthology.json'),interpro_target=J(R/'InterPro-P15502.json'))
def source_key(s):return(s['term']['id'],s['evidence_type'],s['original_reference_id'],s.get('qualifier',''),tuple(sorted(s.get('supporting_entities',[]))),s.get('isoform',''))
def raw_key(r):
 support=sorted({x['db']+':'+x['id']for g in(r.get('withFrom')or[])for x in g['connectedXrefs']})
 acc=r['geneProductId'].split(':',1)[1]
 return(r['goId'],r['goEvidence'],r['reference'],r.get('qualifier',''),tuple(support),acc if '-'in acc else '')
def replay(root, integrity):
 global D,R
 D=root;R=D/'raw'
 actual=derive();need(actual==J(BASE/'results.json'),'database reconstruction differs')
 sources=J(D/'inputs/source-objects.json');raw=J(D/'inputs/raw-quickgo-contexts.json');recon=J(D/'inputs/reconciliation.json')
 joins=[]
 for i,s in enumerate(sources):
  matches=[j for j,r in enumerate(raw)if raw_key(r)==source_key(s)];need(matches,'source lacks raw context: '+str(i));joins.append((i,matches))
 need([(x['annotation_index'],x['raw_api_indices'])for x in recon['joins']]==joins,'raw/source join changed')
 need(set(j for _,js in joins for j in js)==set(range(len(raw))),'unaccounted raw contexts')
 products=J(D/'inputs/product-boundary.json')['official']['products'];sequence_proof=[]
 for p in products:
  seq=''.join((R/(p['id']+'.fasta')).read_text().splitlines()[1:]);need(len(seq)==p['length']and hashlib.sha256(seq.encode()).hexdigest()==p['sequence_sha256'],'product sequence '+p['id']);sequence_proof.append(dict(id=p['id'],length=len(seq)))
 u=J(R/'UniProt-P15502.json');need(u['sequence']['value']==''.join((R/'P15502.fasta').read_text().splitlines()[1:]),'displayed sequence')
 terms={x['id']:x for x in J(R/'QuickGO-source-terms.json')['results']};terms.update({x['id']:x for x in J(R/'QuickGO-elastic-fiber-assembly.json')['results']})
 for parent,child in [('GO:0005201','GO:0030023'),('GO:0085029','GO:0048251')]:need(dict(id=child,relation='is_a')in terms[parent]['children'],'typed ontology edge')
 for r in actual['reactome_rows']:
  need(r['witnesses'],'no human target path')
  for w in r['witnesses']:need(w['reference_identifier']=='P15502'and any(c['id']=='GO:0005576'for c in w['compartments']),'target/compartment')
 print(json.dumps(dict(status='PASS',checked_files=len(integrity),source_objects=len(sources),raw_contexts=len(raw),raw_context_multiplicities=[dict(index=i,raw_indices=js)for i,js in joins if len(js)>1],reactome_events=len(actual['reactome_rows']),target_paths=sum(len(r['witnesses'])for r in actual['reactome_rows']),unexpanded_non_target_branches=sum(len(r['unexpanded_branches'])for r in actual['reactome_rows']),current_mouse_donor_rows=actual['donor_saved_rows'],products=sequence_proof,scope='Positive database paths and saved source/product boundary; no assertion that unexpanded branches are absent or that all products are experimentally equivalent.'),sort_keys=True))
def safe_name(name):
 """Accept only canonical two-component names in the two input directories."""
 if not isinstance(name,str) or "\\" in name:
  raise ValueError('unsafe archive path: '+str(name))
 p=PurePosixPath(name)
 if p.is_absolute() or len(p.parts)!=2 or p.parts[0] not in ('raw','inputs') or any(x in ('','.','..')for x in p.parts) or str(p)!=name:
  raise ValueError('unsafe archive path: '+name)
 return p

def checked_bytes(path, record):
 b=path.read_bytes()
 need(len(b)==record['bytes'] and hashlib.sha256(b).hexdigest()==record['sha256'],'changed file: '+path.name)
 return b

def unpack_inputs(archive, root, integrity):
 """Validate the whole bounded archive, then write ordinary files into an empty temp directory."""
 need(root.is_dir() and not root.is_symlink() and not any(root.iterdir()),'extraction directory must be empty')
 expected={}
 for x in integrity:
  name=x['path'];safe_name(name)
  need(name not in expected,'duplicate manifest path: '+name)
  need(type(x['bytes'])is int and 0<=x['bytes']<=10*1024*1024,'invalid member size: '+name)
  need(x['mode']==0o644,'unexpected file mode: '+name)
  expected[name]=x
 need(len(expected)==99,'expected exactly 99 input members')
 need(sum(x['bytes']for x in integrity)<=10*1024*1024,'input size limit')
 contents={}
 with tarfile.open(archive,'r:gz')as t:
  for member in t:
   name=member.name;safe_name(name)
   need(name in expected,'unexpected archive member: '+name)
   need(name not in contents,'duplicate archive member: '+name)
   need(member.isreg() and not member.issparse(),'non-regular archive member: '+name)
   x=expected[name]
   need(member.size==x['bytes'] and member.mode==x['mode'],'member size/mode differs: '+name)
   stream=t.extractfile(member)
   need(stream is not None,'missing archive data: '+name)
   b=stream.read(x['bytes']+1)
   need(len(b)==x['bytes'] and hashlib.sha256(b).hexdigest()==x['sha256'],'member hash differs: '+name)
   contents[name]=b
 need(set(contents)==set(expected),'archive member set differs')
 for name,b in contents.items():
  p=root.joinpath(*PurePosixPath(name).parts);p.parent.mkdir(exist_ok=True)
  with p.open('xb')as f:f.write(b)
  p.chmod(expected[name]['mode'])

def main():
 manifest=J(BASE/'archive-manifest.json')
 need(manifest['archive']=='database-evidence.tar.gz','unexpected archive name')
 need(manifest['members']==99,'archive member count')
 archive=BASE/manifest['archive'];checked_bytes(archive,manifest)
 for name in ('input-manifest.json','results.json'):
  checked_bytes(BASE/name,manifest['visible_files'][name])
 inputs=J(BASE/'input-manifest.json')
 need(inputs['version']==1,'input manifest version')
 with tempfile.TemporaryDirectory(prefix='ELN-replay-')as tmp:
  root=Path(tmp);unpack_inputs(archive,root,inputs['inputs']);replay(root,inputs['inputs'])
if __name__=='__main__':main()
