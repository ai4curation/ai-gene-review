"""Freeze a separate pombe cohort from an original ProtNLM XML export.

Requires --source-xml and a new empty --out-dir. Never overwrites this snapshot.
Taxonomy is resolved using current UniProt primary accessions, because the export
has placeholder organism fields. Historical secondary accessions are not searched.
"""
import argparse
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
import csv
from datetime import datetime, timezone
import gzip
import hashlib
import io
import json
from pathlib import Path
import xml.etree.ElementTree as ET

import requests
from summarize import NS, summarize

URLS = {
    'published_accessions': 'https://ftp.ebi.ac.uk/pub/contrib/UniProt/ProtNLM2/List_of_UniProt_accessions_that_have_ProtNLM2_annotations.tsv',
    'uniprot_index': 'https://rest.uniprot.org/uniprotkb/stream?query=taxonomy_id%3A4896&format=tsv&fields=accession%2Cid%2Corganism_id%2Corganism_name%2Cgene_names%2Clength%2Creviewed',
    'pombase_identifiers': 'https://www.pombase.org/data/names_and_identifiers/gene_IDs_names_products.tsv',
}
FILES = {'published_accessions': 'published-accessions.tsv', 'uniprot_index': 'uniprot-pombe-index.tsv', 'pombase_identifiers': 'pombase-identifiers.tsv'}


def fetch_records(accession):
    response = requests.get(f'https://rest.uniprot.org/uniprotkb/{accession}.json', timeout=90)
    response.raise_for_status()
    record = response.json()
    assert record['primaryAccession'] == accession, accession
    prediction = requests.get(f'https://rest.uniprot.org/uniprotkb/protnlm/{accession}', timeout=90)
    if prediction.status_code not in {200, 404}:
        prediction.raise_for_status()
    return record, dict(accession=accession, url=prediction.url, status=prediction.status_code, response=prediction.json())


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source-xml', type=Path, required=True)
    parser.add_argument('--out-dir', type=Path, required=True)
    args = parser.parse_args()
    if args.out_dir.exists() and any(args.out_dir.iterdir()):
        parser.error('--out-dir must be new or empty')
    original_bytes = args.source_xml.read_bytes()
    source = args.out_dir / 'snapshot'
    source.mkdir(parents=True)
    downloaded = {}
    for key, url in URLS.items():
        response = requests.get(url, timeout=120)
        response.raise_for_status()
        (source / FILES[key]).write_bytes(response.content)
        downloaded[key] = list(csv.DictReader(io.StringIO(response.content.decode()), delimiter='\t'))
    current = {r['Entry'] for r in downloaded['uniprot_index']}
    identifiers = {r['external_id'] for r in downloaded['pombase_identifiers']}
    original = ET.fromstring(original_bytes).findall(NS + 'entry')
    subset = ET.Element(NS + 'uniprot')
    for entry in original:
        if entry.findtext(NS + 'accession') in current:
            subset.append(entry)
    accessions = [entry.findtext(NS + 'accession') for entry in subset]
    assert accessions and len(set(accessions)) == len(accessions)
    assert set(accessions) <= identifiers, 'Unresolved PomBase identifiers'
    ET.ElementTree(subset).write(source / 'predictions.xml', encoding='utf-8', xml_declaration=True)
    with ThreadPoolExecutor(max_workers=4) as pool:
        results = list(pool.map(fetch_records, accessions))
    for filename, records in [('uniprot.jsonl.gz', [r for r,p in results]), ('api-availability.jsonl.gz', [p for r,p in results])]:
        data = ''.join(json.dumps(r, sort_keys=True) + '\n' for r in records).encode()
        (source / filename).write_bytes(gzip.compress(data, mtime=0))
    manifest = dict(retrieved_at_utc=datetime.now(timezone.utc).isoformat(), source_kind='pre-release XML export',
                    original_xml_filename=args.source_xml.name, original_xml_sha256=hashlib.sha256(original_bytes).hexdigest(),
                    original_xml_records=len(original), current_taxonomy_index_records=len(current),
                    selection='Original XML primary accessions joined to current UniProt taxonomy_id:4896 index, resolved against PomBase accession mappings.',
                    source_urls=URLS, checksums={p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in source.iterdir()},
                    current_uniprot_records=len(results), prediction_api_availability=dict(Counter(str(p['status']) for r,p in results)),
                    caveat='XML sequence/taxonomy/date fields are placeholders; actual prediction-time input sequences and training membership are not established. Current sequences are fetched separately. Subset XML is reserialized, retaining all element values, attributes and evidence.')
    (args.out_dir / 'manifest.json').write_text(json.dumps(manifest, indent=2) + '\n')
    summarize(args.out_dir)


if __name__ == '__main__':
    main()
