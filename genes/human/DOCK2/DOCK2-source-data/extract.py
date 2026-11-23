#!/usr/bin/env python3
"""Project literal DOCK2 interaction records from public PSI-MITAB 2.7 sources."""
import argparse,csv,hashlib,json,urllib.request
from pathlib import Path
HERE=Path(__file__).resolve().parent
FIELDS={0:'id_a',1:'id_b',2:'alt_id_a',3:'alt_id_b',4:'alias_a',5:'alias_b',6:'detection_method',7:'author',8:'publication',9:'taxon_a',10:'taxon_b',11:'interaction_type',12:'source_database',13:'interaction_ids',14:'confidence',15:'expansion',16:'biological_role_a',17:'biological_role_b',18:'experimental_role_a',19:'experimental_role_b',25:'annotation_a',26:'annotation_b',27:'interaction_annotations',28:'host_organism',32:'checksum_a',33:'checksum_b',35:'negative',36:'feature_a',37:'feature_b',40:'identification_a',41:'identification_b'}
def tokens(v):return set(v.split('|'))
def match(a,acc):
 return any('uniprotkb:'+acc in tokens(a[i])for i in [0,2,4])
def read(p):
 return[(i+1,row)for i,row in enumerate(csv.reader(p.open(),delimiter='\t'))if row and not row[0].startswith('#')]
def project(selection,intact,mint):
 src={'intact':read(intact),'mint':read(mint)};out=[]
 for s in selection:
  found=[]
  for db,rows in src.items():
   for line,a in rows:
    if len(a)<42:raise ValueError(f'{db} line {line}: expected 42 MITAB fields, received {len(a)}')
    if 'pubmed:'+s['pmid'] not in tokens(a[8]):continue
    if not((match(a,s['target'])and match([a[1],a[0],a[3],a[2],a[5],a[4]],s['partner']))or(match(a,s['partner'])and match([a[1],a[0],a[3],a[2],a[5],a[4]],s['target']))):continue
    found.append({'database':db,'physical_line_1based':line,'fields':{name:a[i]for i,name in FIELDS.items()}})
  out.append(dict(s,records=found))
 return{'selection_count':len(selection),'raw_sha256':{db:hashlib.sha256(p.read_bytes()).hexdigest()for db,p in [('intact',intact),('mint',mint)]},'selected_record_count':sum(len(s['records'])for s in out),'assertions':out}
def main():
 p=argparse.ArgumentParser();p.add_argument('--intact',type=Path);p.add_argument('--mint',type=Path);p.add_argument('--download',type=Path,help='Download the two public current sources here; results may differ after database updates.');p.add_argument('--selection',type=Path,default=HERE/'selection.json');p.add_argument('--out',type=Path,required=True);a=p.parse_args()
 if a.download:
  a.download.mkdir(parents=True,exist_ok=True)
  for db in ['intact','mint']:
   u=f'https://www.ebi.ac.uk/Tools/webservices/psicquic/{db}/webservices/current/search/query/id%3AQ92608?format=tab27&firstResult=0&maxResults=10000';q=a.download/(db+'.tsv')
   with urllib.request.urlopen(urllib.request.Request(u,headers={'Accept':'text/plain'}),timeout=90)as r:q.write_bytes(r.read())
   setattr(a,db,q)
 if not a.intact or not a.mint:p.error('provide both saved --intact and --mint, or --download')
 v=project(json.loads(a.selection.read_text()),a.intact,a.mint);a.out.parent.mkdir(parents=True,exist_ok=True);a.out.write_text(json.dumps(v,indent=2,ensure_ascii=False)+'\n');print(json.dumps({'assertions':v['selection_count'],'records':v['selected_record_count']}))
if __name__=='__main__':main()
