"""Verify archived assayed proteins from preserved authoritative responses.

No network request and no source modification. The raw records are literal
UniSave versions, independently baselined before annotation curation.
"""
import hashlib
import json
from pathlib import Path
import re

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]


def main():
    baseline = json.loads((HERE / 'archived-extension-baseline.json').read_text())
    methods = (HERE / 'published-methods.txt').read_text()
    results = []
    for accession, genbank, version in [('A0A0S7X285','KPJ56532',20),('A0A0S7X265','KPJ56533',18)]:
        path = ROOT / f'genes/9BACT/{accession}/{accession}-uniprot.txt'
        raw = path.read_text()
        saved = baseline[f'genes/9BACT/{accession}/{accession}-ai-review.yaml']
        current = json.loads((HERE / (accession+'-current.json')).read_text())
        versions = json.loads((HERE / (accession+'-unisave.json')).read_text())['results']
        entries = json.loads((HERE / ('uniparc-'+genbank+'.json')).read_text())['results']
        assert genbank in methods
        assert current['primaryAccession'] == accession
        assert current['inactiveReason']['inactiveReasonType'] == 'DELETED'
        assert any(v['entryVersion']==version for v in versions)
        assert re.search(r'NCBI_TaxID=1703766(?:\s|;)', raw)
        assert re.search(r'^AC   '+accession+r';',raw,re.M)
        seq = ''.join(re.findall('[A-Z]+',raw.split('\nSQ   ',1)[1].split('\n',1)[1].split('//',1)[0]))
        match = next(e for e in entries if accession+'.1' in e.get('uniProtKBAccessions',[]))
        assert seq == match['sequence']['value']
        digest=hashlib.sha256(path.read_bytes()).hexdigest()
        assert digest == saved['raw_sha256'][str(path.relative_to(ROOT))]
        assert hashlib.sha256(seq.encode()).hexdigest() == saved['sequence_sha256']
        results.append({'accession':accession,'published_clone':genbank,'archive_version':version,'sequence_length':len(seq),'uniparc':match['uniParcId'],'sequence_match':True,'raw_sha256':digest,'deletion_reason':current['inactiveReason']['deletedReason']})
    (HERE / 'identity-verification.json').write_text(json.dumps(results,indent=2)+'\n')
    print('Both archived sequences match the published clone mappings and pre-curation raw hashes')


if __name__=='__main__':
    main()
