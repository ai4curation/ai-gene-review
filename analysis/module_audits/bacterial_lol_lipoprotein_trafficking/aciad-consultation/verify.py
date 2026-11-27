"""Strict seeded-payload, curated-new-row, source and construct-identity checks."""

import copy
import hashlib
import json
from pathlib import Path

import yaml
from check_identity import verify as verify_identity

ROOT = Path(__file__).resolve().parents[4]
AUDIT = Path(__file__).resolve().parent
GENES = ('lolA', 'lolB', 'lolC', 'lolD')
NEW_TERMS = {'lolA': 'GO:0140598', 'lolC': 'GO:0140306', 'lolD': 'GO:0140306'}


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def payload(rows):
    return [{key: value for key, value in row.items() if key != 'review'} for row in rows]


def verify():
    before = yaml.safe_load((AUDIT / 'before.yaml').read_text())
    baseline = json.loads((AUDIT.parent / 'additional-seed-baseline.json').read_text())
    expected_actions = {
        'lolA': ['ACCEPT', 'MODIFY', 'ACCEPT', 'ACCEPT'],
        'lolB': ['ACCEPT', 'MODIFY'],
        'lolC': ['ACCEPT', 'MODIFY', 'ACCEPT', 'ACCEPT', 'ACCEPT'],
        'lolD': ['ACCEPT', 'ACCEPT', 'ACCEPT', 'ACCEPT', 'MODIFY'],
    }
    ledger = []
    for gene in GENES:
        path = f'genes/ACIAD/{gene}/{gene}-ai-review.yaml'
        original = before['reviews'][gene]
        assert original == baseline['reviews'][path]['document'], gene
        current = yaml.safe_load((ROOT / path).read_text())
        assert current['status'] == 'COMPLETE'
        for key in ('id', 'gene_symbol', 'taxon', 'product_type'):
            assert current[key] == original[key], (gene, key)
        count = len(original['existing_annotations'])
        rows = current['existing_annotations']
        assert payload(rows[:count]) == payload(original['existing_annotations']), gene
        assert len(rows) == count + (gene in NEW_TERMS), gene
        for index, row in enumerate(rows[:count]):
            assert row['review']['action'] == expected_actions[gene][index]
            assert row['review'].get('reason') and row['review'].get('supported_by')
            ledger.append({'gene': gene, 'row': index, 'term': row['term']['id'],
                           'before': original['existing_annotations'][index]['review']['action'],
                           'after': row['review']['action']})
        if gene in NEW_TERMS:
            row = rows[-1]
            assert row['term']['id'] == NEW_TERMS[gene]
            assert row['review']['action'] == 'NEW'
            assert row['evidence_type'] == 'IDA'
            assert row['original_reference_id'] == 'PMID:42736309'
            assert row['qualifier'] == ('enables' if gene == 'lolA' else 'contributes_to')
            assert not row.get('retired', False)
        # Guards must reject corruption of qualifiers, evidence, lifecycle and row order.
        for key, value in (('qualifier', 'contributes_to'), ('evidence_type', 'EXP'), ('retired', True)):
            altered = copy.deepcopy(original['existing_annotations'])
            altered[0][key] = value
            assert payload(altered) != payload(original['existing_annotations'])
        altered = list(reversed(original['existing_annotations']))
        assert payload(altered) != payload(original['existing_annotations'])
        core = current['core_functions'][0]
        if gene == 'lolC':
            assert 'molecular_function' not in core
            assert core['contributes_to_molecular_function']['id'] == 'GO:0140306'
        if gene == 'lolD':
            assert core['molecular_function']['id'] == 'GO:0016887'
            assert core['contributes_to_molecular_function']['id'] == 'GO:0140306'
            ref = next(r for r in current['references'] if r['id'].endswith('lolD-uniprot.txt'))
            defect = ref['reference_review']['source_defects'][0]
            assert defect['slot'] == 'CC:SUBUNIT' and defect['confidence'] == 'CONFIRMED'
        if gene == 'lolB':
            assert 'PMID:42736309' not in {r['id'] for r in current['references']}
            assert core['proposed_molecular_function'] == current['proposed_new_terms'][0]['proposed_name']
    protected = dict(baseline['protected_files_sha256'])
    closure = yaml.safe_load((AUDIT / 'source-closure.yaml').read_text())
    protected.update(closure['files_sha256'])
    for path, digest in protected.items():
        assert sha(ROOT / path) == digest, f'Protected source changed: {path}'
    identity = verify_identity()
    assert identity == yaml.safe_load((AUDIT / 'identity-mapping.yaml').read_text())
    prior_handoff = AUDIT.parent / 'psepk-consultation/handoff.json'
    prior = json.loads(prior_handoff.read_text())
    for path, digest in prior['files_sha256'].items():
        assert sha(ROOT / path) == digest, f'Frozen PSEPK artifact changed: {path}'
    assert len(ledger) == 16
    return {'result': 'PASS', 'ordered_original_rows': 16,
            'historical_new_rows_at_seed': 0, 'authored_new_MF_rows': 3,
            'authored_new_BP_rows': 0, 'retirements': 0,
            'source_files_protected': len(protected), 'payload_mutation_tests': 16,
            'exact_construct_identity_cases': len(identity['entity_matches']),
            'prior_PSEPK_handoff_unchanged': True, 'action_ledger': ledger,
            'scope': 'Four ACIAD reviews; no full-corpus validation.'}


if __name__ == '__main__':
    print(yaml.safe_dump(verify(), sort_keys=False))
