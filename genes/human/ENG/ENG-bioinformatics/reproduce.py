#!/usr/bin/env python3
"""Reconstruct ENG machine-source context from frozen data using Python 3.10+."""
import argparse
import hashlib
import json
from pathlib import Path, PurePosixPath
import tempfile
import zipfile

import database_context
from source_projection import derive as project_sources


def need(condition, message):
    if not condition:
        raise ValueError(message)


def load(path):
    return json.loads(path.read_text())


def reconstruct(directory):
    manifest = load(directory / 'input-manifest.json')
    expected = {x['member']: x for x in manifest['files']}
    need(len(expected) == len(manifest['files']), 'Duplicate manifest member')
    with tempfile.TemporaryDirectory(prefix='eng-source-context-') as temp:
        root = Path(temp)
        with zipfile.ZipFile(directory / 'inputs.zip') as archive:
            need(set(archive.namelist()) == set(expected), 'Archive scope differs')
            need(len(archive.namelist()) == len(expected), 'Duplicate archive member')
            for member in archive.namelist():
                path = PurePosixPath(member)
                need(not path.is_absolute() and '..' not in path.parts, 'Unsafe member path')
                raw = archive.read(member)
                record = expected[member]
                need(len(raw) == record['bytes'] and hashlib.sha256(raw).hexdigest() == record['sha256'], 'Input mismatch: ' + member)
                dest = root / member
                dest.parent.mkdir(parents=True, exist_ok=True)
                dest.write_bytes(raw)
        sources = load(root / 'bootstrap-v1/source-objects.json')
        source_context = project_sources(
            load(root / 'source-boundary-v1/QuickGO-rows.json'),
            load(root / 'source-boundary-v1/raw/QuickGO-enriched.json'),
            (root / 'normal-archive/genes/human/ENG/ENG-goa.tsv').read_text(),
            sources,
        )
        uniprot = load(root / 'intake-v1/raw/UniProt-P17813.json')
        need(uniprot['primaryAccession'] == 'P17813' and uniprot['organism']['taxonId'] == 9606, 'Target identity')
        sequence = uniprot['sequence']['value']
        feature = next(f for f in uniprot['features'] if f.get('featureId') == 'VSP_004233')
        start = feature['location']['start']['value'] - 1
        end = feature['location']['end']['value']
        need(sequence[start:end] == feature['alternativeSequence']['originalSequence'], 'Alternative-sequence preimage')
        alternatives = feature['alternativeSequence']['alternativeSequences']
        need(len(alternatives) == 1, 'Ambiguous alternative sequence')
        short = sequence[:start] + alternatives[0] + sequence[end:]
        products = []
        for accession, value in [('P17813-1', sequence), ('P17813-2', short)]:
            fasta = (root / ('source-boundary-v1/raw/' + accession + '.fasta')).read_text().splitlines()
            need(accession in fasta[0] and ''.join(fasta[1:]) == value, 'Official natural-product sequence: ' + accession)
            products.append({'id': accession, 'length': len(value), 'sequence_sha256': hashlib.sha256(value.encode()).hexdigest()})
        database_context.configure(root)
        databases = database_context.derive()
        return {
            'source_context': source_context,
            'products': products,
            'processing_features': [f for f in uniprot['features'] if f['type'] in ['Signal', 'Chain', 'Transmembrane', 'Alternative sequence']],
            'database_context': databases,
            'negated_sources': [i for i, s in enumerate(sources) if s.get('negated')],
            'contribution_sources': [i for i, s in enumerate(sources) if s.get('qualifier') == 'contributes_to'],
            'scope': 'Source identity and current applicability only; no biological review decisions generated.',
        }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, help='Save independently computed results to this path.')
    parser.add_argument('--check', action='store_true', help='Compare independently computed results to expected-results.json.')
    args = parser.parse_args()
    directory = Path(__file__).resolve().parent
    result = reconstruct(directory)
    if args.check:
        need(result == load(directory / 'expected-results.json'), 'Results changed')
    if args.output:
        args.output.write_text(json.dumps(result, indent=2, ensure_ascii=False) + '\n')
    print(json.dumps({
        'status': 'PASS', 'raw_records': result['source_context']['raw_API_count'],
        'normal_TSV_rows': result['source_context']['normal_TSV_count'],
        'source_objects': result['source_context']['seed_source_count'],
        'products': [{'id': x['id'], 'length': x['length']} for x in result['products']],
        'negated': len(result['negated_sources']), 'contributes_to': len(result['contribution_sources']),
        'PAINT_joins': len(result['database_context']['paint_joins']),
        'science_decisions_generated': 0, 'expected_results_compared': args.check,
    }, sort_keys=True))


if __name__ == '__main__':
    main()
