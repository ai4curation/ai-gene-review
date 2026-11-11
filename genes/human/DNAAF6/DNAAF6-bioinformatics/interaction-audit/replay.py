#!/usr/bin/env python3
"""Recompute the selected DNAAF6 interaction records and sequence checks, offline."""
from pathlib import Path
import argparse, base64, collections, hashlib, json, re


def sha(data):
    return hashlib.sha256(data).hexdigest()


def calculate(root):
    names = ['source-rows.json', 'intact-all.tsv', 'reference-sequences.fasta', 'input-provenance.json']
    raw = {name: (root / name).read_bytes() for name in names}
    sources = json.loads(raw['source-rows.json'])
    provenance = json.loads(raw['input-provenance.json'])
    target = provenance['target']
    assert sha(raw['intact-all.tsv']) == provenance['mitab']['sha256']
    sequences = {}
    current = None
    for line in raw['reference-sequences.fasta'].decode().splitlines():
        if line.startswith('>'):
            current = line[1:].split()[0]
            assert current not in sequences
            sequences[current] = ''
        elif line.strip():
            assert current is not None
            sequences[current] += line.strip()
    for spec in provenance['sequences']:
        seq = sequences[spec['accession']]
        assert len(seq) == spec['length']
        assert sha(seq.encode()) == spec['sequence_sha256']
    records = [line.split('\t') for line in raw['intact-all.tsv'].decode().splitlines() if line and not line.startswith('#')]
    assert all(len(row) == 42 for row in records)
    groups, used, checks = [], set(), 0
    for item in sources:
        source = item['source']
        pmid = source['original_reference_id'].removeprefix('PMID:')
        partners = [s.removeprefix('UniProtKB:') for s in source['supporting_entities']]
        assert len(partners) == 1
        partner = partners[0]
        selected = []
        for index, row in enumerate(records):
            ids = [row[k].removeprefix('uniprotkb:') for k in [0, 1]]
            if set(ids) != {target, partner} or 'pubmed:' + pmid not in row[8].split('|'):
                continue
            assert row[35] == 'false', 'A selected negative/unspecified interaction needs adjudication'
            entities = []
            for side, accession in enumerate(ids):
                taxon = re.search(r'taxid:(\d+)', row[9 + side]).group(1)
                checksum = base64.b64encode(hashlib.sha1(sequences[accession].encode()).digest()).decode().rstrip('=')
                computed = 'rogid:' + checksum + taxon
                actual = row[32 + side].split('|')
                assert computed in actual, (accession, computed, actual)
                checks += 1
                entities.append({'accession': accession, 'taxon': int(taxon), 'length': len(sequences[accession]), 'rogid': computed, 'feature': row[36 + side], 'participant_identification': row[40 + side]})
            selected.append({'raw_row': index, 'interaction_id': row[13], 'method': row[6], 'host': row[28], 'negative': row[35], 'entities': entities})
            assert index not in used, 'A raw interaction was assigned to multiple source groups'
            used.add(index)
        assert selected, ('No records match source', item['source_index'])
        assert any('MI:1356' in r['method'] for r in selected), 'Missing validated two-hybrid stage'
        groups.append({'source_index': item['source_index'], 'pmid': pmid, 'partner': partner, 'record_count': len(selected), 'records': selected})
    return {'input_sha256': {n: sha(raw[n]) for n in names}, 'source_head': provenance['source_head'], 'raw_record_count': len(records), 'selected_source_groups': len(groups), 'selected_record_count': len(used), 'participant_sequence_checks': checks, 'unselected_raw_rows': sorted(set(range(len(records))) - used), 'groups': groups, 'interpretation': 'Counts distinguish source-row groups from assay stages. ROGIDs authenticate reference sequences, not fusion-tag-free constructs, complete native interfaces, physiological coexistence or functional equivalence of all products.'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true', help='Compare with the committed output without writing files')
    args = parser.parse_args()
    root = Path(__file__).resolve().parent
    result = calculate(root)
    path = root / 'RESULTS.json'
    if args.check:
        assert result == json.loads(path.read_text()), 'The saved result differs from recomputation'
    else:
        path.write_text(json.dumps(result, indent=2, ensure_ascii=False) + '\n')
    print(json.dumps({k: result[k] for k in ['raw_record_count', 'selected_source_groups', 'selected_record_count', 'participant_sequence_checks']}, sort_keys=True))


if __name__ == '__main__':
    main()
