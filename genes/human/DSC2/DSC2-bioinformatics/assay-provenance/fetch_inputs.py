"""Fetch the real public inputs; preserve failures and never substitute fabricated data."""
from pathlib import Path
import argparse,datetime,hashlib,io,json,zipfile
import requests

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--output-dir',type=Path,required=True);a=p.parse_args()
    d=a.output_dir;d.mkdir(parents=True,exist_ok=False);receipts=[]
    urls={f'UniProt-{x}.json':f'https://rest.uniprot.org/uniprotkb/{x}.json'for x in ['Q02487','Q14126']}
    urls['IntAct-Q02487.mitab']='https://www.ebi.ac.uk/Tools/webservices/psicquic/intact/webservices/current/search/query/identifier:Q02487?format=tab27&firstResult=0&maxResults=10000'
    urls['supplementary.zip']='https://www.ebi.ac.uk/europepmc/webservices/rest/PMC9365698/supplementaryFiles'
    try:
        for name,url in urls.items():
            r=requests.get(url,timeout=120);(d/name).write_bytes(r.content)
            receipts.append({'file':name,'url':url,'final_url':r.url,'status':r.status_code,'content_type':r.headers.get('Content-Type'),'time_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'sha256':hashlib.sha256(r.content).hexdigest()})
            r.raise_for_status()
        z=zipfile.ZipFile(d/'supplementary.zip')
        for wanted in ['41586_2022_5028_MOESM4_ESM.xlsx','41586_2022_5028_MOESM6_ESM.xlsx']:
            matches=[n for n in z.namelist()if Path(n).name==wanted]
            if len(matches)!=1:raise ValueError(f'Unique real supplement not found: {wanted}')
            (d/wanted).write_bytes(z.read(matches[0]))
        for name in ['UniProt-Q02487.json','UniProt-Q14126.json']:json.loads((d/name).read_text())
    finally:
        (d/'fetch-receipts.json').write_text(json.dumps(receipts,indent=2)+'\n')
