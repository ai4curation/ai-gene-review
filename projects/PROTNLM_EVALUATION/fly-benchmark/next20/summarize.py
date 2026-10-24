"""Derive the next fly cohort from explicit selection and frozen source records.

No biological verdict is inferred. Run from the repository root.
"""
import csv
import gzip
import hashlib
import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent
BASE = ROOT.parent
REPO = ROOT.parents[3]


def read_csv(path):
    with path.open() as stream:
        return list(csv.DictReader(stream))


def jsonl(path):
    with gzip.open(path, 'rt') as stream:
        return [json.loads(line) for line in stream if line.strip()]


def write_csv(name, rows):
    with (ROOT / name).open('w') as stream:
        writer = csv.DictWriter(stream, fieldnames=list(rows[0]), lineterminator='\n')
        writer.writeheader()
        writer.writerows(rows)


def claims(record):
    description = record.get('proteinDescription', {})
    names = ([description['recommendedName']] if description.get('recommendedName') else [])
    names += description.get('submissionNames', []) + description.get('alternativeNames', [])
    for name in names:
        if name.get('fullName'):
            node = name['fullName']
            yield 'name', '', node['value'], node
    for node in record.get('uniProtKBCrossReferences', []):
        if node['database'] == 'GO':
            text = next(p['value'] for p in node['properties'] if p['key'] == 'GoTerm')
            yield 'GO', node['id'], text, node
    for comment in record.get('comments', []):
        if comment['commentType'] == 'FUNCTION':
            for node in comment.get('texts', []):
                yield 'function', '', node['value'], node
        if comment['commentType'] == 'SUBCELLULAR LOCATION':
            for location in comment.get('subcellularLocations', []):
                for part in ['location', 'topology', 'orientation']:
                    if part in location:
                        node = location[part]
                        yield part, node.get('id', ''), node['value'], node
    for node in record.get('keywords', []):
        yield 'keyword', node.get('id', ''), node.get('name', ''), node


def main():
    manifest = json.loads((ROOT / 'manifest.json').read_text())
    for name, sha in manifest['checksums'].items():
        assert hashlib.sha256((ROOT / 'snapshot' / name).read_bytes()).hexdigest() == sha
    for name, sha in manifest['reused_sources'].items():
        assert hashlib.sha256((REPO / name).read_bytes()).hexdigest() == sha
    predictions = {x['primaryAccession']: x for x in jsonl(BASE / 'predictions.jsonl.gz')}
    uniprot = {x['primaryAccession']: x for x in jsonl(BASE / 'uniprot.jsonl.gz')}
    published = set(predictions)
    extras = jsonl(ROOT / 'snapshot/additional-api-responses.jsonl.gz')
    for x in extras:
        a = x['accession']
        assert x['prediction_status'] == x['uniprot_status'] == 200
        assert x['prediction']['primaryAccession'] == x['uniprot']['primaryAccession'] == a
        assert a not in predictions
        predictions[a], uniprot[a] = x['prediction'], x['uniprot']
    fb = {}
    with gzip.open(BASE / 'flybase-identifiers.tsv.gz', 'rt') as stream:
        for line in stream:
            if line.startswith('#'):
                continue
            c = line.rstrip('\n').split('\t')
            if len(c) >= 5 and c[1] == 'Dmel':
                for identifier in [c[2]] + c[3].split(','):
                    fb[identifier] = (c[0], c[2], c[4])
    done = {x['flybase_ids'] for x in read_csv(BASE / 'functional-cohort.csv')}
    selected = {x['accession']: x for x in read_csv(ROOT / 'selection.csv')}
    assert len(selected) == 20
    inventory, cohort, statements, fasta = [], [], [], []
    for a, p in sorted(predictions.items()):
        u = uniprot[a]
        assert u['organism']['taxonId'] == 7227
        ids = {fb[x['id']] for x in u.get('uniProtKBCrossReferences', [])
               if x['database'] == 'FlyBase' and x['id'] in fb}
        assert len(ids) == 1, (a, ids)
        gene, primary, annotation = ids.pop()
        emitted = list(claims(p))
        counts = Counter(x[0] for x in emitted)
        sequence = u['sequence']['value']
        row = dict(accession=a, gene_symbol=gene, flybase_id=primary,
                   annotation_id=annotation, current_length=len(sequence),
                   entry_type=u['entryType'], published_list=a in published,
                   already_in_first41=primary in done, selected=a in selected,
                   name_count=counts['name'], go_count=counts['GO'],
                   function_count=counts['function'], location_count=counts['location'],
                   keyword_count=counts['keyword'],
                   sequence_sha256=hashlib.sha256(sequence.encode()).hexdigest())
        inventory.append(row)
        if a not in selected:
            continue
        s = selected[a]
        assert (gene, primary, annotation) == (s['gene_symbol'], s['flybase_id'], s['annotation_id'])
        assert primary not in done, (gene, primary)
        tier = 'GO/function' if counts['GO'] or counts['function'] else ('localization/keyword' if counts['location'] or counts['keyword'] else 'name only')
        record_dir = REPO / 'genes/DROME' / gene
        cohort.append(dict(**s, prediction_tier=tier, source_snapshot='published API snapshot 2026-09-08' if a in published else 'original-export accession; API snapshot 2026-09-09',
                           current_length=len(sequence), entry_type=u['entryType'],
                           go_count=counts['GO'], function_count=counts['function'],
                           location_count=counts['location'], name_count=counts['name'],
                           existing_main_review=(record_dir / (gene + '-ai-review.yaml')).exists(),
                           sequence_sha256=row['sequence_sha256']))
        for kind, identifier, text, node in emitted:
            statements.append(dict(accession=a, gene_symbol=gene, type=kind, id=identifier,
                                   text=text, source_object=json.dumps(node, sort_keys=True)))
        fasta.append(f'>{a} {gene} {primary}\n{sequence}\n')
    cohort.sort(key=lambda x: int(x['priority']))
    assert len(cohort) == len({x['flybase_id'] for x in cohort}) == 20
    write_csv('candidate-inventory.csv', inventory)
    write_csv('cohort.csv', cohort)
    write_csv('prediction-statements.csv', statements)
    (ROOT / 'sequences.fasta').write_text(''.join(fasta))
    summary = dict(candidate_accessions=len(inventory),
                   candidate_gene_ids=len({x['flybase_id'] for x in inventory}),
                   additional_original_export_accessions=len(extras),
                   selected_genes=20, overlap_with_first41=0,
                   selected_tiers=dict(Counter(x['prediction_tier'] for x in cohort)),
                   selected_entry_types=dict(Counter(x['entry_type'] for x in cohort)),
                   selected_sources=dict(Counter(x['source_snapshot'] for x in cohort)),
                   emitted_statement_counts=dict(Counter(x['type'] for x in statements)),
                   review_status='SELECTED_NOT_REVIEWED',
                   caveat='Metabolic enrichment uses biological leads, not prediction correctness. Names, SL locations, paragraphs and GO terms are distinct outputs. No invented GO mappings.')
    (ROOT / 'summary.json').write_text(json.dumps(summary, indent=2) + '\n')
    print(json.dumps(summary, indent=2))


if __name__ == '__main__':
    main()
