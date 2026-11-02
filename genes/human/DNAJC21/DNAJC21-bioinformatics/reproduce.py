# /// script
# requires-python = ">=3.10"
# dependencies = ["xlrd>=2,<3"]
# ///
"""Regenerate literal target data; accepts public downloads or saved raw paths.

uv run reproduce.py --download /tmp/dnajc21-raw --output /tmp/extract.json
uv run reproduce.py --input-map saved-paths.json --output /tmp/extract.json
Use --check source-extracts.json to compare without writing an output file.
Dynamic provider updates cause a hash error, never silent substitution.
"""
from pathlib import Path
import argparse,csv,hashlib,io,json,urllib.request,xml.etree.ElementTree as ET
import xlrd

def extract(manifest,paths):
 result={'target':'DNAJC21 / Q5F1R6','inputs':[],'workbooks':[]}
 for spec in manifest['inputs']:
  p=Path(paths[spec['name']]);raw=p.read_bytes();digest=hashlib.sha256(raw).hexdigest()
  if digest!=spec['sha256']:raise ValueError(f"Input drift: {spec['name']}: {digest}")
  result['inputs'].append({'name':spec['name'],'sha256':digest})
  kind=spec['kind']
  if kind=='workbook':
   book=xlrd.open_workbook(file_contents=raw);sheets=[]
   for sh in book.sheets():
    hits=[]
    for i in range(spec['header_rows'],sh.nrows):
     cells=sh.row_values(i)
     if any(any(q in str(c).upper()for q in ['DNAJC21','DNAJA5','LOC134218','ENSG00000168724'])for c in cells):hits.append({'excel_row':i+1,'cells':cells})
    if hits:sheets.append({'name':sh.name,'shape':[sh.nrows,sh.ncols],'header_rows':[{'excel_row':i+1,'cells':sh.row_values(i)}for i in range(spec['header_rows'])],'records':hits})
   result['workbooks'].append({'source':spec['name'],'pmid':spec['pmid'],'sheets':sheets})
  elif kind=='mitab':
   selected=[]
   for i,v in enumerate(csv.reader(io.StringIO(raw.decode()),delimiter='\t'),1):
    if len(v)>35 and 'uniprotkb:Q5F1R6'in v[:2] and any(q in v[8]for q in ['pubmed:17500595','pubmed:20195357']):selected.append({'source_line':i,'fields':v})
   result['intact']={'source':spec['name'],'format':'PSI-MITAB 2.7, zero-based fields: 0/1 identifiers, 6 method, 8 publication, 9/10 taxa, 13 interaction accession, 15 expansion, 35 negative, 36/37 features','records':selected}
  elif kind=='tree':
   tree=json.loads(raw)['search']['tree_topology']['annotation_node'];found=[]
   def walk(node,path):
    path=path+[node['persistent_id']]
    if node.get('tree_node_type')=='LEAF'and any(q in node.get('node_name','')for q in ['Q5F1R6','P53863','SPAC6B12.08']):found.append({'path':path,'leaf':{k:node.get(k)for k in ['persistent_id','node_name','gene_symbol','organism','gene_id']}})
    children=node.get('children',{}).get('annotation_node',[])
    for child in children if isinstance(children,list)else[children]:walk(child,path)
   walk(tree,[]);result['paint_tree']={'source':spec['name'],'paths':found}
  elif kind=='paint':
   rows=list(csv.DictReader(io.StringIO(raw.decode()),delimiter='\t'));result['paint_ibd']={'source':spec['name'],'records':[x for x in rows if x['node']=='PTN001940778'and x['go_id']=='GO:0005737']}
  elif kind=='hpa':
   root=ET.fromstring(raw);records=[]
   for ce in root.iter('cellExpression'):
    records.append({'attributes':dict(ce.attrib),'locations':[x.text for x in ce.iter('location')],'verification':[{'attributes':dict(x.attrib),'text':x.text}for x in ce.iter('verification')],'cell_lines':[{'attributes':dict(x.attrib),'text':x.text}for x in ce.iter('cellLine')]})
   result['hpa']={'source':spec['name'],'cell_expression':records}
  elif kind=='interpro':
   x=json.loads(raw);result['interpro']={'source':spec['name'],'accession':x['metadata']['accession'],'length':x['metadata']['length'],'go_terms':x['metadata']['go_terms'],'entries':x['entries']}
 return result

def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('--manifest',type=Path,default=Path(__file__).with_name('source-manifest.json'));p.add_argument('--input-map',type=Path);p.add_argument('--download',type=Path);p.add_argument('--output',type=Path);p.add_argument('--check',type=Path);a=p.parse_args()
 if bool(a.input_map)==bool(a.download):p.error('Choose exactly one of --input-map or --download')
 if bool(a.output)==bool(a.check):p.error('Choose exactly one of --output or --check')
 m=json.loads(a.manifest.read_text());paths={}
 if a.input_map:paths=json.loads(a.input_map.read_text())
 else:
  a.download.mkdir(parents=True,exist_ok=True)
  for x in m['inputs']:
   dest=a.download/x['name']
   if not dest.exists():
    req=urllib.request.Request(x['url'],headers={'User-Agent':'DNAJC21-source-replay/1.0'})
    with urllib.request.urlopen(req,timeout=90)as response:raw=response.read()
    if hashlib.sha256(raw).hexdigest()!=x['sha256']:raise ValueError(f"Public source changed for {x['name']}; use the fixed saved source")
    dest.write_bytes(raw)
   paths[x['name']]=str(dest)
 result=extract(m,paths)
 if a.check:
  if result!=json.loads(a.check.read_text()):raise ValueError('Extract differs from regenerated source values')
  print('PASS: all source hashes and regenerated extract values match')
 else:a.output.write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n');print('Wrote exact regenerated extract')
if __name__=='__main__':main()
