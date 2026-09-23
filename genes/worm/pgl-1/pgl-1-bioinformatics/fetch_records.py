#!/usr/bin/env python3
"""Fetch exact UniProt records and InterPro matches; keep retrieval provenance."""
import argparse,datetime,hashlib,json,urllib.request
from pathlib import Path
p=argparse.ArgumentParser();p.add_argument('accessions',nargs='+');args=p.parse_args();provenance=[]
for acc in args.accessions:
    for name,url in [('uniprot',f'https://rest.uniprot.org/uniprotkb/{acc}.json'),('interpro',f'https://www.ebi.ac.uk/interpro/api/entry/all/protein/uniprot/{acc}/')]:
        page = 1
        while url:
            request=urllib.request.Request(url,headers={'Accept':'application/json'})
            with urllib.request.urlopen(request,timeout=90) as response: raw=response.read()
            data=json.loads(raw)
            if name=='uniprot' and data['primaryAccession']!=acc:raise ValueError('Accession mismatch')
            suffix = '' if page == 1 else f'-page-{page}'
            path=Path(f'{acc}-{name}{suffix}.json');path.write_bytes(raw)
            provenance.append({'accession':acc,'url':url,'path':str(path),'sha256':hashlib.sha256(raw).hexdigest(),'retrieved_utc':datetime.datetime.now(datetime.timezone.utc).isoformat()})
            url = data.get('next') if name == 'interpro' else None
            page += 1
Path('source-provenance.json').write_text(json.dumps(provenance,indent=2)+'\n')
