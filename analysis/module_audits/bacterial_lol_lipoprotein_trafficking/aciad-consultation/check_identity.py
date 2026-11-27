"""Reproduce native sequence matches to source-deposited LolDF/LolA entities."""

import hashlib
import json
import re
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[4]
IDENTITY = ROOT / 'analysis/module_audits/bacterial_lol_lipoprotein_trafficking/identity'


def native(gene):
    text = (ROOT / f'genes/ACIAD/{gene}/{gene}-uniprot.txt').read_text()
    return ''.join(re.findall('[A-Z]+', text.split('SQ   SEQUENCE')[1].split('\n', 1)[1].split('//')[0]))


def verify():
    sources = {gene: native(gene) for gene in ('lolA', 'lolC', 'lolD')}
    legacy = json.loads((IDENTITY / 'Q9EYM3-current.json').read_text())['response']
    assert sources['lolC'] == legacy['sequence']['value']
    cases = {'28MF-entity-2.json': 'lolC', '28MF-entity-3.json': 'lolD',
             '29EB-entity-2.json': 'lolD', '29EB-entity-3.json': 'lolC',
             '29EB-entity-4.json': 'lolA', '9R29-entity-1.json': 'lolD',
             '9R29-entity-2.json': 'lolC'}
    output = []
    for filename, gene in cases.items():
        path = IDENTITY / filename
        data = json.loads(path.read_text())
        sequence = data['entity_poly']['pdbx_seq_one_letter_code_can']
        offset = sources[gene].find(sequence)
        assert offset >= 0, filename
        assert data['entity_poly']['rcsb_mutation_count'] == 0, filename
        assert any(s['ncbi_taxonomy_id'] == 62977 for s in data['rcsb_entity_source_organism'])
        output.append({'source': str(path.relative_to(ROOT)),
                       'source_sha256': hashlib.sha256(path.read_bytes()).hexdigest(),
                       'gene': gene, 'entity_length': len(sequence),
                       'native_start': offset + 1, 'native_end': offset + len(sequence),
                       'native_length': len(sources[gene]), 'identity_on_entity': 1.0,
                       'annotated_mutations': 0,
                       'reference_accessions': data['rcsb_polymer_entity_container_identifiers']['reference_sequence_identifiers']})
    tested = {'lolD': {48: 'K', 93: 'Y', 148: 'S', 172: 'E', 205: 'H'},
              'lolC': {40: 'V', 51: 'F', 170: 'P', 173: 'T', 174: 'P', 175: 'S',
                       176: 'P', 177: 'A', 181: 'P', 253: 'W', 270: 'M',
                       274: 'L', 277: 'L', 306: 'T', 365: 'I', 368: 'L'}}
    for gene, residues in tested.items():
        for position, aa in residues.items():
            assert sources[gene][position - 1] == aa, (gene, position, aa)
    return {'result': 'PASS', 'legacy_Q9EYM3_equals_A0ACM8PZZ0': True,
            'entity_matches': output, 'reported_positions_match_native': tested,
            'limitations': ['Entity sequence correspondence does not measure native kinetic flux.',
                           'The paper labels recombinant LolA 29-231; the deposited 202-aa entity matches current Q6F8G3 29-230 exactly. No target sequence was edited.',
                           'The endogenously copurified short lipoprotein-like substrate was not unequivocally identified; PDB short-entity naming is not definitive cargo identification.']}


if __name__ == '__main__':
    print(yaml.safe_dump(verify(), sort_keys=False))
