"""Fetch original prediction payloads and ordinary UniProt identity/sequence records."""
import argparse,csv,gzip,hashlib,importlib.util,io,json,sys
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime,timezone
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
parser=argparse.ArgumentParser(description='Fetch a separate complete D. melanogaster ProtNLM census; preserve existing snapshots.')
parser.add_argument('--out-dir',required=True,type=Path)
args=parser.parse_args()
root=Path(__file__).resolve().parent.parent
out=args.out_dir
out.mkdir(parents=True,exist_ok=True)
if any(out.iterdir()): raise SystemExit('Output directory must be empty; use a new snapshot directory')
u='https://ftp.ebi.ac.uk/pub/contrib/UniProt/ProtNLM2/List_of_UniProt_accessions_that_have_ProtNLM2_annotations.tsv'
r=requests.get(u,timeout=60);r.raise_for_status();raw=r.content
allrows=list(csv.DictReader(io.StringIO(raw.decode()),delimiter='\t'))
rows=[x for x in allrows if x['Organism (ID)']=='7227']
with (out/'accessions.tsv').open('w') as f:
 w=csv.DictWriter(f,fieldnames=list(rows[0]),delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(rows)
spec=importlib.util.spec_from_file_location('fetch',root/'fetch_protnlm_api.py');m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
def fetch(row):
 acc=row['Entry']; p=m.fetch_one(acc)
 r=requests.get('https://rest.uniprot.org/uniprotkb/'+acc+'.json',timeout=60);r.raise_for_status()
 return p,r.json()
with ThreadPoolExecutor(max_workers=5) as pool:
 results=list(pool.map(fetch,rows))
assert all(p for p,u in results)
checks={}
for name,records in [('predictions',[x[0] for x in results]),('uniprot',[x[1] for x in results])]:
 data=''.join(json.dumps(x,sort_keys=True)+'\n' for x in records).encode()
 (out/(name+'.jsonl.gz')).write_bytes(gzip.compress(data,mtime=0));checks[name+'_jsonl_sha256']=hashlib.sha256(data).hexdigest()
manifest={'retrieved_at':datetime.now(timezone.utc).isoformat(),'accession_list_url':u,'full_accession_list_sha256':hashlib.sha256(raw).hexdigest(),'full_list_records':len(allrows),'selected_taxon':'7227','selected_organism':'Drosophila melanogaster','selected_records':len(rows),'selection_rule':'All accession-list rows with Organism (ID) = 7227; no function or gene-name filtering.','api_url_template':'https://rest.uniprot.org/uniprotkb/protnlm/{accession}','uniprot_url_template':'https://rest.uniprot.org/uniprotkb/{accession}.json','successful_prediction_responses':len(results),'successful_uniprot_responses':len(results),'accessions_sha256':hashlib.sha256((out/'accessions.tsv').read_bytes()).hexdigest(),**checks,'sequence_caveat':'Current UniProt sequences, not proven prediction-time inputs. Placeholder prediction entryAudit dates are not release or sequence dates.'}
fb_dir='https://s3ftp.flybase.org/releases/current/precomputed_files/genes/'
r=requests.get(fb_dir,timeout=30);r.raise_for_status()
links=[urljoin(fb_dir,a['href']) for a in BeautifulSoup(r.text,'html.parser').select('a[href]') if 'fbgn_annotation_ID' in a['href']]
assert len(links)==1,links
r=requests.get(links[0],timeout=60);r.raise_for_status()
(out/'flybase-identifiers.tsv.gz').write_bytes(r.content)
manifest.update(flybase_identifier_url=links[0],flybase_identifier_gzip_sha256=hashlib.sha256(r.content).hexdigest())
(out/'manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
print(json.dumps(manifest,indent=2))
