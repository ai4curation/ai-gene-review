from pathlib import Path
import json,re,hashlib
D=Path(__file__).resolve().parent;F=D/'frozen-inputs';IBD=F/'IBD.gaf'
def run():
 sources=json.loads((F/'source-objects.json').read_text());root=json.loads((D/'raw/PTHR12553-treeinfo.json').read_text())['search']['tree_topology']['annotation_node'];nodes={};paths={}
 def walk(n,p):
  ident=n['persistent_id']
  if ident in nodes:raise ValueError('duplicate node')
  nodes[ident]=n;paths[ident]=p+[ident];cs=n.get('children',{}).get('annotation_node',[])
  for c in [cs] if isinstance(cs,dict) else cs:walk(c,p+[ident])
 walk(root,[]);target=[n for n,x in nodes.items() if x.get('node_name','').endswith('UniProtKB=Q9BQ52')]
 if len(target)!=1:raise ValueError('target nonunique')
 target=target[0];path=paths[target];msa=json.loads((D/'raw/PTHR12553-familymsa.json').read_text())['search']['MSA_list']['sequence_info'];hit=[x for x in msa if x['persistent_id']==target]
 if len(hit)!=1:raise ValueError('MSA target')
 sequence=re.sub('[^A-Za-z]','',hit[0]['sequence']).upper();official=json.loads((F/'UniProt-Q9BQ52.json').read_text())['sequence']['value']
 if sequence!=official:raise ValueError('MSA !=826official')
 records=[]
 for line,raw in enumerate(IBD.read_text().splitlines(),1):
  f=raw.split('\t')
  if len(f)>1 and f[1] in path:records.append({'line':line,'fields':f})
 joins=[]
 for i in [14,28,33]:
  s=sources[i];ptn=[v.split(':',1)[1] for v in s['supporting_entities'] if v.startswith('PANTHER:')];r=[x for x in records if x['fields'][1] in ptn and x['fields'][4]==s['term']['id'] and x['fields'][6]=='IBD' and 'NOT' not in x['fields'][3]]
  if len(r)!=1 or set(r[0]['fields'][7].split('|'))!=set(s['supporting_entities'])-{'PANTHER:'+p for p in ptn}:raise ValueError('literal IBD/donor mismatch')
  joins.append({'annotation_index':i,'source':s,'IBD':r[0],'exact_donor_set':True,'placement_on_target_path':all(p in path for p in ptn)})
 donor_nodes=[]
 for n,x in nodes.items():
  name=x.get('node_name','');ac=name.split('UniProtKB=')[-1] if 'UniProtKB=' in name else None
  if ac in ['Q9BQ52','Q80Y81','Q8VYS2','F4J1H7','O44476','Q8MKW7','P36159','P87168','Q10155']:donor_nodes.append({k:x.get(k) for k in ['persistent_id','node_name','gene_id','organism','gene_symbol']})
 return {'target':target,'target_path':path,'nodes':len(nodes),'MSA_sequences':len(msa),'target_sequence_length':len(sequence),'target_sequence_sha256':hashlib.sha256(sequence.encode()).hexdigest(),'target_official_exact':True,'target_subfamily':nodes[target].get('prop_sf_id'),'joins':joins,'all_target_path_IBD_IRD_records':records,'donor_nodes':donor_nodes,'scope':'Ancestor placement and complete saved IBD path scan; no count-based weakness or self-donor circularity inference. Sequence match is canonical only, not alternate-product equivalence.'}
if __name__=='__main__':print(json.dumps(run(),indent=2,sort_keys=True))
