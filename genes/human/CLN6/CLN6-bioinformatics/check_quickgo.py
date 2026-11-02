#!/usr/bin/env python3
"""Retrieve or replay complete QuickGO searches and compare literal data.

No annotation action or biological correctness is inferred. URLs, snapshots,
TSVs and record identifiers are inputs. All HTTP bodies are saved before parsing.
"""
import argparse
from collections import Counter
import csv
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import sys
from urllib.error import HTTPError
from urllib.parse import parse_qsl, urlencode, urlsplit, urlunsplit
from urllib.request import Request, urlopen
import yaml


def sha(data):
    return hashlib.sha256(data).hexdigest()


def stamp():
    return datetime.now(timezone.utc).isoformat()


def write_yaml(path, value):
    path.write_text(yaml.safe_dump(value, sort_keys=False, allow_unicode=True))


def with_parameter(url, key, value):
    parts = urlsplit(url)
    params = [(k, v) for k, v in parse_qsl(parts.query) if k != key]
    params.append((key, str(value)))
    return urlunsplit((parts.scheme, parts.netloc, parts.path, urlencode(params), parts.fragment))


def read_pages(entries, root):
    pages = []
    for entry in entries:
        raw = (root / entry['path']).read_bytes()
        if sha(raw) != entry['sha256']:
            raise ValueError('Saved page hash mismatch: ' + entry['path'])
        pages.append(json.loads(raw))
    return pages


def complete(pages):
    if not pages:
        raise ValueError('No pages')
    total = pages[0]['pageInfo']['total']
    hits = pages[0]['numberOfHits']
    # QuickGO may represent an empty search with total=0 and a first empty page.
    expected = max(1, total)
    if len(pages) != expected:
        raise ValueError('Incomplete page collection')
    records = []
    for i, page in enumerate(pages, 1):
        info = page['pageInfo']
        if info['current'] != i or info['total'] != total or page['numberOfHits'] != hits:
            raise ValueError('Inconsistent pagination; snapshot completeness unresolved')
        records.extend(page['results'])
    if len(records) != hits or len({r['id'] for r in records}) != hits:
        raise ValueError('Hit count or unique record IDs disagree across pages')
    return records


def retrieve(url, directory, max_pages):
    directory.mkdir(parents=True, exist_ok=True)
    entries, pages = [], []
    page_number, total = 1, 1
    while page_number <= total:
        if page_number > max_pages:
            raise ValueError('Configured page bound exceeded; incomplete query')
        request_url = url if page_number == 1 else with_parameter(url, 'page', page_number)
        receipt = {'url': request_url, 'started_at': stamp()}
        try:
            response = urlopen(Request(request_url, headers={'Accept': 'application/json'}), timeout=90)
        except HTTPError as error:
            response = error
        with response:
            raw = response.read()
            receipt.update(status=response.status, effective_url=response.url,
                           headers=dict(response.headers.items()), finished_at=stamp(),
                           bytes=len(raw), sha256=sha(raw))
        name = 'page-' + str(page_number) + '.json'
        (directory / name).write_bytes(raw)
        write_yaml(directory / (name + '.receipt.yaml'), receipt)
        entries.append({'path': str(directory.name + '/' + name), 'sha256': sha(raw),
                        'receipt': str(directory.name + '/' + name + '.receipt.yaml')})
        if receipt['status'] != 200:
            raise ValueError('HTTP ' + str(receipt['status']) + '; raw failure retained')
        data = json.loads(raw)
        pages.append(data)
        total = max(1, data['pageInfo']['total'])
        page_number += 1
    complete(pages)
    return entries, pages


# Only shared literal fields are compared: TSV has no QuickGO record ID and its
# WITH/FROM flattening differs from the API's nested representation.
FIELDS = ('geneProductId', 'qualifier', 'goId', 'goEvidence', 'evidenceCode',
          'reference', 'assignedBy', 'date', 'taxonId')
TSV_FIELDS = ('GENE PRODUCT ID', 'QUALIFIER', 'GO TERM', 'GO EVIDENCE CODE',
              'ECO ID', 'REFERENCE', 'ASSIGNED BY', 'DATE', 'TAXON ID')


def api_key(record):
    return tuple(str(record.get(k, '')) for k in FIELDS)


def tsv_key(row):
    values = [row.get(k, '') for k in TSV_FIELDS]
    values[0] = row['GENE PRODUCT DB'] + ':' + values[0]
    return tuple(values)


def expanded(counter):
    return [dict(zip(FIELDS, key), count=count) for key, count in sorted(counter.items())]


def compare_tsv(path, product, observed):
    if not path.is_file():
        return {'path': str(path), 'status': 'UNAVAILABLE', 'comparison': 'inconclusive'}
    raw = path.read_bytes()
    rows = list(csv.DictReader(raw.decode().splitlines(), delimiter='\t'))
    if rows and not set(TSV_FIELDS + ('GENE PRODUCT DB', 'GO ASPECT')) <= set(rows[0]):
        raise ValueError('Unexpected TSV columns: ' + str(path))
    rows = [r for r in rows if r['GO ASPECT'] == 'cellular_component'
            and r['GENE PRODUCT DB'] + ':' + r['GENE PRODUCT ID'] == product]
    records = [r for r in observed if r['geneProductId'] == product]
    api, tsv = Counter(map(api_key, records)), Counter(map(tsv_key, rows))
    return {'path': str(path), 'sha256': sha(raw), 'bytes': len(raw),
            'status': 'COMPARED', 'product': product, 'api_records': len(records),
            'tsv_rows': len(rows), 'comparison_fields': list(FIELDS),
            'api_only': expanded(api - tsv), 'tsv_only': expanded(tsv - api),
            'equal_projection': api == tsv,
            'limitation': 'Literal shared-field comparison only; differing snapshots do not identify the cause or validate the biological annotation.'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--config', required=True, type=Path)
    parser.add_argument('--repo-root', required=True, type=Path)
    parser.add_argument('--output', required=True, type=Path)
    parser.add_argument('--observations', type=Path, help='Replay a generated manifest without network calls')
    parser.add_argument('--query', help='Select one named query from the config')
    parser.add_argument('--page-size', type=int, help='Override limit, for example to exercise pagination')
    args = parser.parse_args()
    if args.output.exists():
        parser.error('Output directory already exists; choose a new path to preserve receipts')
    args.output.mkdir(parents=True)
    report = {'started_at': stamp(), 'status': 'INCONCLUSIVE', 'mode': 'replay' if args.observations else 'live',
              'config_sha256': sha(args.config.read_bytes()), 'queries': [],
              'scope': 'Literal API/snapshot/TSV observations, not a biological annotation assessment.'}
    manifest = {'queries': []}
    try:
        config = yaml.safe_load(args.config.read_text())
        if args.page_size is not None and not 1 <= args.page_size <= 200:
            raise ValueError('Page size must be between 1 and 200')
        selected = [q for q in config['queries'] if args.query is None or q['name'] == args.query]
        if not selected:
            raise ValueError('No matching configured query')
        replay = yaml.safe_load(args.observations.read_text()) if args.observations else None
        for query in selected:
            name = query['name']
            if Path(name).name != name or name in ('.', '..'):
                raise ValueError('Query name must be a simple directory name')
            url = query['url']
            if args.page_size is not None:
                url = with_parameter(url, 'limit', args.page_size)
            if replay is not None:
                candidates = [q for q in replay['queries'] if q['name'] == name and q['url'] == url]
                if len(candidates) != 1:
                    raise ValueError('Replay manifest query/URL mismatch')
                entries = candidates[0]['pages']
                pages = read_pages(entries, args.observations.parent)
            else:
                entries, pages = retrieve(url, args.output / name, config.get('max_pages', 100))
                manifest['queries'].append({'name': name, 'url': url, 'pages': entries})
                write_yaml(args.output / 'manifest.yaml', manifest)
            observed = complete(pages)
            snapshot_pages = read_pages(query['snapshot_pages'], args.config.parent)
            snapshot = complete(snapshot_pages)
            current_by_id, old_by_id = ({r['id']: r for r in rs} for rs in [observed, snapshot])
            common = set(current_by_id) & set(old_by_id)
            changed = [{'id': key, 'saved': old_by_id[key], 'observed': current_by_id[key]}
                       for key in sorted(common) if old_by_id[key] != current_by_id[key]]
            item = {'name': name, 'url': url, 'pages': len(pages), 'number_of_hits': len(observed),
                    'complete': True, 'snapshot_records': len(snapshot),
                    'record_objects_equal': current_by_id == old_by_id,
                    'raw_page_hashes_equal': [e['sha256'] for e in entries] == [e['sha256'] for e in query['snapshot_pages']],
                    'added_records': [current_by_id[k] for k in sorted(set(current_by_id) - set(old_by_id))],
                    'removed_records': [old_by_id[k] for k in sorted(set(old_by_id) - set(current_by_id))],
                    'changed_records': changed,
                    'records_of_interest': [{'id': k, 'present': k in current_by_id, 'record': current_by_id.get(k)}
                                            for k in config.get('records_of_interest', []) if k in current_by_id or k in old_by_id],
                    'tsv_comparisons': [compare_tsv(args.repo_root / path, product, observed)
                                        for product, path in query.get('repository_tsvs', {}).items()]}
            report['queries'].append(item)
        report['status'] = 'COMPLETE'
    except Exception as error:
        report['error'] = type(error).__name__ + ': ' + str(error)
    report['finished_at'] = stamp()
    write_yaml(args.output / 'report.yaml', report)
    print(report['status'], args.output / 'report.yaml')
    return 0 if report['status'] == 'COMPLETE' else 1


if __name__ == '__main__':
    sys.exit(main())
