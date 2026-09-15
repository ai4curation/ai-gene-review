"""Download separate immutable UniProt JSON inputs; existing files are retained."""
import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
from urllib.request import urlopen
p=argparse.ArgumentParser()
p.add_argument('--out',required=True,type=Path)
p.add_argument('accessions',nargs='+')
a=p.parse_args();a.out.mkdir(parents=True,exist_ok=True)
manifest=[]
for acc in a.accessions:
    url=f'https://rest.uniprot.org/uniprotkb/{acc}.json'
    path=a.out/(acc+'.json')
    if not path.exists():
        with urlopen(url,timeout=90) as response: raw=response.read()
        record=json.loads(raw)
        if record['primaryAccession']!=acc: raise ValueError('Accession mismatch')
        path.write_bytes(raw)
    manifest.append({'accession':acc,'url':url,'file':path.name,'sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'local_file_timestamp_utc':datetime.fromtimestamp(path.stat().st_mtime,timezone.utc).isoformat()})
(a.out.parent/'sources.json').write_text(json.dumps(manifest,indent=2)+'\n')
