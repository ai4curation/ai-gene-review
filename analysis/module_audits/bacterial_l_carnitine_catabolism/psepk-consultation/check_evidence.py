"""Reproduce sequence comparisons and check frozen curation/source preservation."""
from collections import Counter
from hashlib import sha256
from pathlib import Path
import json
import re

from openpyxl import load_workbook

from Bio import Align
from Bio.Align import substitution_matrices
import yaml

ROOT = Path(__file__).resolve().parents[4]
HERE = Path(__file__).resolve().parent
CACHE = HERE


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


def sequence(path):
    text = path.read_text().split('SQ   SEQUENCE', 1)[1].split('\n', 1)[1].split('//')[0]
    return re.sub(r'[^A-Z]', '', text)


def compare(left, right):
    aligner = Align.PairwiseAligner(mode='global')
    aligner.substitution_matrix = substitution_matrices.load('BLOSUM62')
    aligner.open_gap_score = -10
    aligner.extend_gap_score = -0.5
    alignment = aligner.align(left, right)[0]
    a, b = str(alignment[0]), str(alignment[1])
    identical = sum(x == y and x != '-' for x, y in zip(a, b))
    return {'lengths': [len(left), len(right)], 'alignment_columns': len(a),
            'identical_columns': identical, 'identity_percent': round(100 * identical / len(a), 3),
            'aligned_left': a, 'aligned_right': b}


def preservation(baseline, documents):
    counts = Counter()
    changes = []
    historical_new = 0
    for name, old in baseline['reviews'].items():
        new = documents[name]
        assert len(old['existing_annotations']) == len(new['existing_annotations']), name
        for index, (a, b) in enumerate(zip(old['existing_annotations'], new['existing_annotations'])):
            assert {k: v for k, v in a.items() if k != 'review'} == {
                k: v for k, v in b.items() if k != 'review'}, (name, index, 'payload changed')
            counts[b['review']['action']] += 1
            if a['review']['action'] == 'NEW':
                historical_new += 1
                assert b['review']['action'] == 'NEW', (name, index, 'historical proposal changed')
            if a['review']['action'] != b['review']['action']:
                changes.append({'file': name, 'index': index, 'term': a['term']['id'],
                                'before': a['review']['action'], 'after': b['review']['action']})
    for name, expected in baseline['protected_sha256'].items():
        assert digest(ROOT / name) == expected, name
    return {'ordered_rows': sum(counts.values()), 'historical_new_preserved': historical_new,
            'protected_files': len(baseline['protected_sha256']), 'final_actions': dict(counts),
            'action_changes': changes, 'new_rows': 0, 'retired_rows': 0}


def main():
    baseline = yaml.safe_load((HERE / 'baseline.yaml').read_text())
    docs = {name: yaml.safe_load((ROOT / name).read_text()) for name in baseline['reviews']}
    result = preservation(baseline, docs)
    result['sequence_method'] = 'Biopython global BLOSUM62; gap open -10, extend -0.5; identity denominator all alignment columns'
    result['sequence_comparisons'] = {}
    for target, donor in [('PP_0303', 'cdhC'), ('PP_0301', 'cdhB'), ('lcdH', 'cdhA')]:
        a = ROOT / f'genes/PSEPK/{target}/{target}-uniprot.txt'
        b = ROOT / f'genes/PSEAE/{donor}/{donor}-uniprot.txt'
        result['sequence_comparisons'][target] = {'input_sha256': {str(a.relative_to(ROOT)): digest(a),
                                                                str(b.relative_to(ROOT)): digest(b)},
                                                  **compare(sequence(a), sequence(b))}
    pdb = json.loads((CACHE / '2HLJ-entity.json').read_text())
    result['2HLJ'] = {'source_url': 'https://data.rcsb.org/rest/v1/core/polymer_entity/2HLJ/1',
                     'response_sha256': digest(CACHE / '2HLJ-entity.json'),
                     'source': pdb['entity_src_gen'],
                     **compare(sequence(ROOT / 'genes/PSEPK/PP_0301/PP_0301-uniprot.txt'),
                               pdb['entity_poly']['pdbx_seq_one_letter_code_can'])}
    mapping_path = HERE / '24240508-data246.xlsx'
    screen_path = HERE / '24240508-data248.xlsx'
    mapping = list(load_workbook(mapping_path, data_only=True).worksheets[0].iter_rows(values_only=True))
    screen = list(load_workbook(screen_path, data_only=True).worksheets[0].iter_rows(values_only=True))
    target = [row for row in mapping if row[1] == 'Q88R31']
    assert len(target) == 1 and target[0][0] == 'BKACE_511'
    assay = [row for row in screen if row[0] == target[0][0].replace('_', '')]
    assert len(assay) == 1 and assay[0][1] == 'Pseudomonas putida (strain KT2440)'
    result['primary_target_screen'] = {
        'source_sha256': {mapping_path.name: digest(mapping_path), screen_path.name: digest(screen_path)},
        'mapping_row': list(target[0]),
        'screen_columns': dict(zip(screen[0], assay[0])),
        'interpretation': 'Pre-process screening values; no unsupported units, kinetics, physiological substrate claim or processed positive-call threshold inferred.',
        'GO0043720': 'UNDECIDED pending processed KAH assay interpretation',
        'other_representatives': {acc: [list(row[:4]) for row in mapping if row[1] == acc]
                                  for acc in ['Q9HTH7', 'Q02DX5', 'Q7D3B4', 'B1SWX4', 'A3SRB7']},
        'PAO1_PA14_screen_rows': [list(row[:10]) for row in screen if row[0] in ['BKACE529', 'BKACE361']],
    }
    import copy
    faults = []
    for fault in ['id', 'order', 'historical_new']:
        altered = copy.deepcopy(docs)
        rows = altered['genes/PSEPK/caiX/caiX-ai-review.yaml']['existing_annotations']
        if fault == 'id':
            rows[0]['term']['id'] = 'GO:9999999'
        elif fault == 'order':
            rows[0], rows[1] = rows[1], rows[0]
        else:
            rows[2]['review']['action'] = 'REMOVE'
        try:
            preservation(baseline, altered)
        except AssertionError:
            faults.append(fault)
        else:
            raise AssertionError(f'Fault not detected: {fault}')
    result['detected_deliberate_faults'] = faults
    (HERE / 'results.yaml').write_text(yaml.safe_dump(result, sort_keys=False, width=100))
    print(yaml.safe_dump({k: v for k, v in result.items() if k not in {'sequence_comparisons', '2HLJ', 'primary_target_screen'}}, sort_keys=False))
    for name, row in result['sequence_comparisons'].items():
        print(name, row['identity_percent'])
    print('2HLJ', result['2HLJ']['identity_percent'])


if __name__ == '__main__':
    main()
