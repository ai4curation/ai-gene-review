"""Fetch a separate Neurospora ProtNLM snapshot into a new empty directory.

This fetches sources only. Existing manual gene-name and cohort selection maps
must be reconciled explicitly before regenerating an updated review cohort.
"""
import argparse
from concurrent.futures import ThreadPoolExecutor
import csv
from datetime import datetime, timezone
import gzip
import hashlib
import io
import json
from pathlib import Path

import requests

LIST_URL = 'https://ftp.ebi.ac.uk/pub/contrib/UniProt/ProtNLM2/List_of_UniProt_accessions_that_have_ProtNLM2_annotations.tsv'


def get_records(accession):
    values = []
    for url in [f'https://rest.uniprot.org/uniprotkb/protnlm/{accession}', f'https://rest.uniprot.org/uniprotkb/{accession}.json']:
        response = requests.get(url, timeout=60)
        response.raise_for_status()
        data = response.json()
        assert data['primaryAccession'] == accession, (accession, data['primaryAccession'])
        values.append(data)
    return values


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out-dir', type=Path, required=True)
    args = parser.parse_args()
    if args.out_dir.exists() and any(args.out_dir.iterdir()):
        parser.error('--out-dir must be new or empty')
    source = args.out_dir / 'snapshot'
    source.mkdir(parents=True)
    response = requests.get(LIST_URL, timeout=60)
    response.raise_for_status()
    listed = list(csv.DictReader(io.StringIO(response.content.decode()), delimiter='\t'))
    subset = [row for row in listed if row['Organism (ID)'] == '367110']
    if not subset:
        raise ValueError('No taxon367110 records in current published list')
    with (source / 'accessions.tsv').open('w') as stream:
        writer = csv.DictWriter(stream, fieldnames=list(subset[0]), delimiter='\t', lineterminator='\n')
        writer.writeheader()
        writer.writerows(subset)
    with ThreadPoolExecutor(max_workers=4) as pool:
        data = list(pool.map(get_records, [row['Entry'] for row in subset]))
    for index, name in enumerate(['predictions.jsonl.gz', 'uniprot.jsonl.gz']):
        raw = ''.join(json.dumps(pair[index], sort_keys=True) + '\n' for pair in data).encode()
        (source / name).write_bytes(gzip.compress(raw, mtime=0))
    manifest = dict(retrieved_at_utc=datetime.now(timezone.utc).isoformat(), source_urls={'accession_list': LIST_URL,
                    'predictions': 'https://rest.uniprot.org/uniprotkb/protnlm/{accession}', 'current_uniprot': 'https://rest.uniprot.org/uniprotkb/{accession}.json'},
                    public_list_full_sha256=hashlib.sha256(response.content).hexdigest(), records=len(data),
                    selection='All current published-list taxon367110 records; no manual review cohort selected by this fetcher.',
                    checksums={p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in source.iterdir()},
                    caveat='Current sequences are not proven prediction-time inputs. Prediction placeholder dates do not establish training membership.')
    (args.out_dir / 'manifest.json').write_text(json.dumps(manifest, indent=2) + '\n')
    print(f'Saved {len(data)} source records to {args.out_dir}')


if __name__ == '__main__':
    main()
