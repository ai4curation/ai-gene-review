"""Check source preservation and original-deposit identity; not assay validation."""
import argparse
from collections import Counter
import hashlib
from pathlib import Path
import re

from Bio import SeqIO
import yaml


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def sequence(path):
    text = path.read_text().split('SQ   SEQUENCE')[1].split('\n', 1)[1].split('//')[0]
    return ''.join(re.findall('[A-Z]+', text))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--all-sources', action='store_true')
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    here = Path(__file__).resolve().parent
    root = here.parents[3]
    baseline = yaml.safe_load((here / 'seed-baseline.yaml').read_text())
    mapping = yaml.safe_load((here / 'member-map.yaml').read_text())
    sources = dict(baseline['protected'])
    if args.all_sources:
        complete = baseline['complete_source_baseline']
        path = root / complete['cache_path']
        assert sha(path) == complete['sha256'], 'complete baseline modified'
        sources.update(yaml.safe_load(path.read_text())['protected'])
    for path, digest in sources.items():
        assert sha(root / path) == digest, f'source changed: {path}'
    record = SeqIO.read(here / 'AF010139.1.embl', 'embl')
    deposited = {
        f.qualifiers['gene'][0]: f.qualifiers['translation'][0]
        for f in record.features
        if f.type == 'CDS' and 'gene' in f.qualifiers
    }
    counts = Counter()
    genes = []
    for member in mapping['members']:
        gene = member['gene']
        doc = yaml.safe_load((root / member['review_path']).read_text())
        original = baseline['genes'][gene]
        rows = [{k: v for k, v in row.items() if k != 'review'}
                for row in doc['existing_annotations']]
        assert rows == original['annotations'], f'ordered payload changed: {gene}'
        assert doc['id'] == original['id'] == member['accession']
        assert doc['status'] == 'COMPLETE'
        seq = sequence(root / f'genes/AZOVI/{gene}/{gene}-uniprot.txt')
        assert seq == deposited[gene], f'primary deposit mismatch: {gene}'
        assert hashlib.sha256(seq.encode()).hexdigest() == member['sequence_sha256']
        actions = Counter(row['review']['action'] for row in doc['existing_annotations'])
        assert 'PENDING' not in actions and 'NEW' not in actions
        counts.update(actions)
        genes.append({'gene': gene, 'accession': doc['id'], 'original_rows': len(rows),
                      'actions': dict(actions), 'sequence_matches_primary_deposit': True})
    comparator = mapping['iron_loading_comparator']
    assert sha(root / comparator['source_path']) == comparator['source_sha256']
    positions = [37, 39, 63, 105, 106]
    ligand_sequences = {org: sequence(root / f'genes/{org}/iscU/iscU-uniprot.txt')
                        for org in ['AZOVI', 'ECOLI']}
    ligands = {org: {pos: seq[pos - 1] for pos in positions}
               for org, seq in ligand_sequences.items()}
    assert ligands['AZOVI'] == ligands['ECOLI'] == dict(zip(positions, 'CDCHC'))
    result = {'status': 'PASS', 'gene_count': len(genes),
              'original_rows': sum(g['original_rows'] for g in genes),
              'new_rows': 0, 'retired_rows': 0, 'actions': dict(counts),
              'protected_files_checked': len(sources), 'genes': genes,
              'iscU_comparative_ligands': ligands,
              'limit': 'Preservation and sequence identity, not independent assay coverage.'}
    output = yaml.safe_dump(result, sort_keys=False)
    if args.output:
        args.output.write_text(output)
    print(output)


if __name__ == '__main__':
    main()
