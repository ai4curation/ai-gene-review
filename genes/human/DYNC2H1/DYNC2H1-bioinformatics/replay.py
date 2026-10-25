"""Saved-input DYNC2H1 evidence extraction, Python 3.9+ standard library.

--check compares computed projections with saved outputs; never uses the network.
This reconstructs source records, not scientific annotation verdicts.
"""
from pathlib import Path
from html.parser import HTMLParser
import argparse, json, hashlib, base64, collections, re, zipfile, tarfile, io, xml.etree.ElementTree as ET

D=Path(__file__).resolve().parent
DATA={}
def raw(name): return DATA[name]
def J(name): return json.loads(raw(name))
def H(name): return hashlib.sha256(raw(name)).hexdigest()
def compute():
 out={}; src=J('source-objects.json')
 official=J('UniProt-Q8NCM8.json')
 root=J('PTHR10676-tree.json')['search']['tree_topology']['annotation_node']; nodes=[]
 def walk(n,path):
  path=path+[n['persistent_id']]
  nodes.append({**{k:v for k,v in n.items() if k!='children' and not k.startswith('PANTHER_GO_')},'path':path})
  ch=n.get('children',{}).get('annotation_node',[])
  for c in ch if isinstance(ch,list) else [ch]:walk(c,path)
 walk(root,[])
 target=[n for n in nodes if 'Q8NCM8' in str(n)]; assert len(target)==1
 msa=J('PTHR10676-msa.json')['search']['MSA_list']['sequence_info']
 ms=[m for m in msa if m['persistent_id']==target[0]['persistent_id']]; assert len(ms)==1
 aligned=ms[0]['sequence']; unaligned=aligned.replace('-','').replace('.','').upper()
 assert unaligned==official['sequence']['value']
 node_ids={v for a in src for v in a.get('supporting_entities',[]) if v.startswith('PANTHER:PTN')}
 ibdp='IBD.gaf'; rows=[]
 for no,line in enumerate(raw(ibdp).decode().splitlines(),1):
  if line.startswith('!'):continue
  f=line.split('\t')
  if any(node.split(':')[1] in line for node in node_ids):rows.append({'line':no,'evidence':f[6],'fields':f})
 out['paint.json']={'target':target[0],'tree_node_count':len(nodes),'MSA_count':len(msa),'unaligned_sequence_length':len(unaligned),'sequence_sha256':hashlib.sha256(unaligned.encode()).hexdigest(),'literal_sources':rows,'queried_ancestral_nodes':sorted(node_ids),'node_records':[n for n in nodes if n['persistent_id'] in {v.split(':')[1] for v in node_ids}|{'PTN000072732'}],'IBD_source':str(ibdp),'IBD_sha256':H(ibdp)}
 rs={int(Path(n).stem.split('-')[1]):J(n) for n in DATA if n.startswith('Reactome-') and n.endswith('.json')}
 paths=[]
 def traverse(n,path,rels):
  if n in path:return
  x=rs.get(n)
  if not x:return
  path=path+[n]
  if x.get('referenceEntity',{}).get('identifier')=='Q8NCM8':
   paths.append({'ids':path,'relations':rels,'labels':[rs[k]['displayName'] for k in path],'leaf':{'accession':'Q8NCM8','start':x['startCoordinate'],'end':x['endCoordinate'],'compartments':[{'id':'GO:'+c['accession'],'label':c['displayName']} for c in x['compartment']]}});return
  for rel in ['input','output','hasComponent','hasMember','hasCandidate']:
   ids={v if isinstance(v,int) else v['dbId'] for v in x.get(rel,[])}
   for k in sorted(ids):traverse(k,path,rels+[rel])
 roots=sorted({int(a['original_reference_id'].split('-')[-1]) for a in src if a['original_reference_id'].startswith('Reactome:')})
 for n in roots:traverse(n,[],[])
 out['reactome.json']={'roots':roots,'fetched_records':len(rs),'target_paths':paths,'summary':[{'id':n,'name':rs[n]['displayName'],'text':[v['text'] for v in rs[n].get('summation',[])]} for n in roots]}
 class Table(HTMLParser):
  def __init__(self):super().__init__();self.rows=[];self.row=None;self.cell=None
  def handle_starttag(self,t,a):
   if t=='tr':self.row=[]
   if t in ('th','td') and self.row is not None:self.cell=[]
  def handle_data(self,d):
   if self.cell is not None:self.cell.append(d)
  def handle_endtag(self,t):
   if t in ('td','th') and self.cell is not None:self.row.append(' '.join(' '.join(self.cell).split()));self.cell=None
   if t=='tr' and self.row is not None:self.rows.append(self.row);self.row=None
 ep='19056867-nhlbi-exosome.html'; html=raw(ep).decode(); table=Table();table.feed(html)
 header=next(x for x in table.rows if 'Gene Name' in x); targets=[{'zero_based_tr_index':i,'cells':x,'record':dict(zip(header,x))} for i,x in enumerate(table.rows) if 'DYNC2H1' in x]
 refs=re.findall(r'<li>(.*?)</li>',html,re.S)
 refids=[re.search(r'pubmed/(\d+)',r).group(1) for r in refs if re.search(r'pubmed/(\d+)',r)]
 out['exosome.json']={'source_path':str(ep),'source_sha256':H(ep),'header':header,'target_rows':targets,'numbered_reference_pmids':refids,'table_tr_count':len(table.rows),'scope':'Protein identification; no peptide sequences, vesicle topology, secretion mechanism, or isoform-specificity inferred.'}
 products=J('products.json'); checks={p['id']:base64.b64encode(hashlib.sha1(p['sequence'].encode()).digest()).decode().rstrip('=')+'9606' for p in products}
 records=[]
 for no,line in enumerate(raw('intact-Q8NCM8.tsv').decode().splitlines(),1):
  f=line.split('\t')
  if len(f)<34 or f[0].startswith('#'):continue
  records.append({'line':no,'fields':f,'target_ROGID_product_matches':[k for k,v in checks.items() if any(v in z for z in f[32:34])]})
 out['interactions.json']={'record_count':len(records),'per_publication':dict(collections.Counter(r['fields'][8] for r in records)),'29742051_records':[r for r in records if 'pubmed:29742051' in r['fields'][8]],'21525035_records':[r for r in records if 'pubmed:21525035' in r['fields'][8]],'official_product_ROGIDs':checks}
 return out
def main():
 parser=argparse.ArgumentParser(description=__doc__)
 parser.add_argument('--check',action='store_true',help='read only: compare with published computed outputs')
 parser.add_argument('--archive',type=Path,default=D/'inputs.tar.gz')
 parser.add_argument('--output',type=Path,default=D/'outputs')
 a=parser.parse_args(); manifest=json.loads((D/'source-manifest.json').read_text())
 assert hashlib.sha256(a.archive.read_bytes()).hexdigest()==manifest['archive_sha256']
 with tarfile.open(a.archive,'r:gz') as z:
  for m in z.getmembers():
   assert m.isfile() and '/' not in m.name and m.name not in DATA
   DATA[m.name]=z.extractfile(m).read()
 assert set(DATA)=={r['path'] for r in manifest['inputs']}
 for r in manifest['inputs']:
  assert len(raw(r['path']))==r['bytes'] and H(r['path'])==r['sha256'],r['path']
 out=compute()
 # Mechanically reproduced results; interpretation is stated separately in RESULTS.md.
 if not a.check:a.output.mkdir(parents=True,exist_ok=True)
 for name,x in out.items():
  if a.check:assert json.loads((a.output/name).read_text())==x,name
  else:(a.output/name).write_text(json.dumps(x,indent=2)+'\n')
 print(json.dumps({'mode':'check' if a.check else 'write','input_files':len(DATA),'projections':len(out),'tree_nodes':out['paint.json']['tree_node_count'],'sequence':out['paint.json']['unaligned_sequence_length'],'literal_IBD_records':sum(r['evidence']=='IBD' for r in out['paint.json']['literal_sources']),'Reactome_paths':len(out['reactome.json']['target_paths']),'IntAct_records':out['interactions.json']['record_count'],'exosome_target_rows':len(out['exosome.json']['target_rows'])}))
if __name__=='__main__':main()
