"""Rebuild the Neurospora census from frozen sources and explicit gene/selection maps."""
from collections import Counter
import csv
import gzip
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def read_csv(path):
    with path.open() as stream:
        return list(csv.DictReader(stream))


def save(name, rows):
    with (ROOT / name).open('w') as stream:
        writer = csv.DictWriter(stream, fieldnames=list(rows[0]), lineterminator='\n')
        writer.writeheader()
        writer.writerows(rows)


def statements(record):
    for item in record.get('uniProtKBCrossReferences', []):
        if item['database'] == 'GO':
            yield 'GO', item['id'], next(p['value'] for p in item['properties'] if p['key'] == 'GoTerm'), item.get('evidences', [])
    for comment in record.get('comments', []):
        if comment['commentType'] == 'FUNCTION':
            for item in comment.get('texts', []):
                yield 'function', '', item['value'], item.get('evidences', [])
        elif comment['commentType'] == 'SUBCELLULAR LOCATION':
            for location in comment.get('subcellularLocations', []):
                for kind, item in location.items():
                    yield 'location' if kind == 'location' else kind, item.get('id', ''), item['value'], item.get('evidences', [])
    for item in record.get('keywords', []):
        yield 'keyword', item['id'], item['name'], item.get('evidences', [])


def main():
    manifest = json.loads((ROOT / 'manifest.json').read_text())
    for name, digest in manifest['checksums'].items():
        assert hashlib.sha256((ROOT / 'snapshot' / name).read_bytes()).hexdigest() == digest, name
    with (ROOT / 'snapshot/accessions.tsv').open() as stream:
        listed = list(csv.DictReader(stream, delimiter='\t'))
    records = {}
    for key, name in [('predictions', 'predictions.jsonl.gz'), ('uniprot', 'uniprot.jsonl.gz')]:
        records[key] = {r['primaryAccession']: r for r in map(json.loads, gzip.open(ROOT / 'snapshot' / name, 'rt'))}
        assert set(records[key]) == {r['Entry'] for r in listed}
    genes = {r['accession']: r for r in read_csv(ROOT / 'gene-map.csv')}
    selection = {r['accession']: r for r in read_csv(ROOT / 'selection.csv')}
    assert set(selection) <= set(records['predictions'])
    inventory, claims, provenance = [], [], []
    for listed_row in listed:
        accession = listed_row['Entry']
        current, predicted = records['uniprot'][accession], records['predictions'][accession]
        gene = genes[accession]
        assert current['organism']['taxonId'] == int(listed_row['Organism (ID)'])
        extracted = list(statements(predicted))
        counts = Counter(kind for kind, ident, text, evidence in extracted)
        chosen = selection.get(accession, {})
        inventory.append(dict(accession=accession, gene_symbol=gene['gene_symbol'], locus_tag=gene['locus_tag'],
                              current_length=current['sequence']['length'], go_count=counts['GO'], function_count=counts['function'],
                              location_count=counts['location'], selected=bool(chosen), review_tier=chosen.get('review_tier', 'outside initial cohort'),
                              selection_reason=chosen.get('selection_reason', '')))
        for kind, ident, text, evidence in extracted:
            row = dict(accession=accession, gene_symbol=gene['gene_symbol'], type=kind, id=ident, text=text)
            claims.append(row)
            provenance.append({**row, 'evidence_json': json.dumps(evidence, sort_keys=True)})
    save('inventory.csv', inventory)
    cohort = [r for r in inventory if r['selected']]
    save('review-cohort.csv', cohort)
    save('prediction-statements.csv', claims)
    save('review-predictions.csv', [r for r in claims if r['accession'] in selection])
    save('claim-provenance.csv', provenance)
    with (ROOT / 'sequences.fasta').open('w') as stream:
        for row in inventory:
            stream.write(f">{row['accession']} {row['gene_symbol']} {row['locus_tag']}\n{records['uniprot'][row['accession']]['sequence']['value']}\n")
    summary = dict(published_records=len(inventory), distinct_gene_identifiers=len({r['locus_tag'] for r in inventory}),
                   go_function_records=sum(bool(r['go_count'] or r['function_count']) for r in inventory),
                   location_only_records=sum(bool(r['location_count']) and not (r['go_count'] or r['function_count']) for r in inventory),
                   reviewed_cohort_records=len(cohort), selected_tiers=dict(Counter(r['review_tier'] for r in cohort)),
                   selected_statement_counts=dict(Counter(r['type'] for r in claims if r['accession'] in selection)),
                   all_statement_counts=dict(Counter(r['type'] for r in claims)),
                   current_entry_types=dict(Counter(r['entryType'] for r in records['uniprot'].values())),
                   caveat='Selection is retrospective: all GO/function-bearing records plus four purposively selected localization cases. Counts do not assign biological validity; current sequences do not establish prediction-time inputs.')
    (ROOT / 'summary.json').write_text(json.dumps(summary, indent=2) + '\n')
    print(json.dumps(summary, indent=2))


if __name__ == '__main__':
    main()
