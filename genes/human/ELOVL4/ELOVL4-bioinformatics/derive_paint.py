from pathlib import Path
import json,re,hashlib
O=Path(__file__).resolve().parent;D=O/'owner-evidence-v1';J=lambda p:json.loads(p.read_text())
IBD=D/'raw/PANTHER-current-IBD.gaf'
def run():
 joins=J(O/'bootstrap-v1/source-joins.json');root=J(D/'raw/PTHR11157-treeinfo.json')['search']['tree_topology']['annotation_node'];nodes={};paths={}
 def walk(n,p):
  ident=n['persistent_id']
  if ident in nodes:raise ValueError('duplicate node')
  nodes[ident]=n;paths[ident]=p+[ident];cs=n.get('children',{}).get('annotation_node',[])
  for c in [cs]if isinstance(cs,dict)else cs:walk(c,p+[ident])
 walk(root,[]);targets=[n for n,x in nodes.items()if x.get('node_name','').endswith('UniProtKB=Q9GZR5')]
 if len(targets)!=1:raise ValueError('target nonunique')
 target=targets[0];path=paths[target];msa=J(D/'raw/PTHR11157-familymsa.json')['search']['MSA_list']['sequence_info'];hit=[x for x in msa if x['persistent_id']==target]
 if len(hit)!=1:raise ValueError('MSA target')
 seq=re.sub('[^A-Za-z]','',hit[0]['sequence']).upper();official=J(O/'intake-v1/raw/UniProt-Q9GZR5.json')['sequence']['value']
 if seq!=official:raise ValueError('MSA reference mismatch')
 records=[]
 for line,raw in enumerate(IBD.read_text().splitlines(),1):
  f=raw.split('\t')
  if len(f)>7 and f[1]in path:records.append({'line':line,'fields':f})
 out=[]
 for item in joins[:7]:
  support=item['current_support_lists'][0];ptn=[x.split(':',1)[1]for x in support if x.startswith('PANTHER:PTN')]
  matches=[r for r in records if r['fields'][1]in ptn and r['fields'][4]==item['source']['term']['id'] and r['fields'][6]=='IBD'and 'NOT'not in r['fields'][3]]
  expected=set(support)-{'PANTHER:'+p for p in ptn};actual=set('|'.join(r['fields'][7]for r in matches).split('|'))
  out.append({'index':item['index'],'source':item['source'],'ptns':ptn,'placement_on_target_path':all(p in path for p in ptn),'records':matches,'expected_donors':sorted(expected),'actual_donors':sorted(actual),'exact_donor_match':expected==actual})
 donorids={v for row in out for v in row['actual_donors']}
 donor_nodes=[]
 for n,x in nodes.items():
  name=x.get('node_name','');gid=x.get('gene_id','')
  if any(v.split(':',1)[-1]in name or v==gid for v in donorids):donor_nodes.append({k:x.get(k)for k in ['persistent_id','node_name','gene_id','organism','gene_symbol','prop_sf_id']})
 return {'target':target,'target_path':path,'nodes':len(nodes),'MSA_sequences':len(msa),'target_sequence_length':len(seq),'target_sequence_sha256':hashlib.sha256(seq.encode()).hexdigest(),'target_official_exact':True,'target_subfamily':nodes[target].get('prop_sf_id'),'joins':out,'all_target_path_records':records,'donor_nodes':donor_nodes,'IBD_path':str(IBD.resolve()),'IBD_sha256':hashlib.sha256(IBD.read_bytes()).hexdigest(),'scope':'All saved IBD/IRD records on the target path scanned. Donor cardinality is descriptive only; target self-evidence is legitimate.'}
