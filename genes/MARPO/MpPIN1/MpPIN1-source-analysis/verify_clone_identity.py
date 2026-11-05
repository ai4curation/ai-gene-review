"""Reproduce the genome-record versus published MpPINZ clone sequence comparison.
Run from the repository root with uv run python <this script>.
The UniProt JSON is downloaded unchanged from its normal REST endpoint.
"""
from pathlib import Path
import hashlib, json, re
import urllib.request
here = Path(__file__).resolve().parent
url = 'https://rest.uniprot.org/uniprotkb/A0A075ILB5.json'
raw = here / 'A0A075ILB5.json'
if not raw.exists():
    with urllib.request.urlopen(url) as r: raw.write_bytes(r.read())
d = json.loads(raw.read_text())
record = (here.parent / 'MpPIN1-uniprot.txt').read_text()
seq = ''.join(re.findall('[A-Z]+', record.split('\nSQ   ')[1].split('\n',1)[1].split('//')[0]))
clone = d['sequence']['value']
result = {'source_url':url, 'clone_accession':d['primaryAccession'], 'genome_accession':'A0A2R6WHW5',
          'sequence_identical':seq == clone, 'genome_length':len(seq), 'clone_length':len(clone),
          'sequence_sha256':hashlib.sha256(seq.encode()).hexdigest(),
          'download_sha256':hashlib.sha256(raw.read_bytes()).hexdigest(),
          'clone_embl_references':[x for x in d['uniProtKBCrossReferences'] if x['database']=='EMBL']}
(here/'clone-identity.json').write_text(json.dumps(result,indent=2)+'\n')
assert seq == clone, result
print(json.dumps(result,indent=2))
