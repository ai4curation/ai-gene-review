#!/usr/bin/env python3
"""Verify frozen UniProt sequences against RCSB polymer entities; run at repo root."""
from pathlib import Path
import json,hashlib,re,yaml
cache=Path('.cache/module-audit-logs/beta-oxidation-20261106/pao1-dehydrogenases')
proof=yaml.safe_load(Path(__file__).with_name('identity-proof.yaml').read_text())
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
assert sha('publications/PMID_40057486.md')==proof['publication_sha256']
expected={'8PNS':[],'8PU5':[(441,'E','A')],'8PNG':[],'8R1E':[(130,'M','G'),(296,'E','A'),(303,'Q','A')]}
for gene,codes in [('PA0506',['8PNS','8PU5']),('PA0508',['8PNG','8R1E'])]:
    p=cache/(gene+'-identity.json');assert sha(p)==proof['entries'][gene]['response_sha256']
    u=json.loads(p.read_text())['results'][0];seq=u['sequence']['value']
    raw=(Path('genes/PSEAE')/gene/(gene+'-uniprot.txt')).read_text()
    frozen=''.join(re.findall('[A-Z]+',raw.split('\nSQ   ',1)[1].split('\n',1)[1].split('//')[0]))
    assert frozen==seq,(gene,'seed sequence changed')
    for code in codes:
        p=cache/(code+'-entity1.json');assert sha(p)==proof['PDB_entities'][code]['response_sha256']
        d=json.loads(p.read_text());s=d['entity_poly']['pdbx_seq_one_letter_code_can'].replace('\n','')
        assert s[:2]=='GH' and len(s)==len(seq)+2
        assert u['primaryAccession'] in d['rcsb_polymer_entity_container_identifiers']['uniprot_ids']
        diffs=[(i+1,a,b) for i,(a,b) in enumerate(zip(seq,s[2:])) if a!=b]
        assert diffs==expected[code],(code,diffs)
print('PASS: two exact PAO1 sequences, four PDB bridges, GH remnant and all four specified substitutions')
