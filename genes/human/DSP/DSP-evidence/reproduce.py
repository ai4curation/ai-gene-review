# /// script
# requires-python = ">=3.9"
# dependencies = ["PyYAML==6.0.3", "xlrd==2.0.2", "beautifulsoup4==4.14.3"]
# ///
"""Extract measured target records from authenticated public source files.

Use --input-map with saved files, or --download to retrieve public URLs.
The thesis extraction additionally requires the external pdftotext program.
This script does not infer localization, activity or annotation verdicts.
"""
import argparse
import hashlib
import json
from pathlib import Path
import re
import subprocess
import tempfile
from urllib.request import Request, urlopen

from bs4 import BeautifulSoup
import xlrd
import yaml


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--input-map', type=Path, help='JSON or YAML mapping source keys to saved raw-file paths')
    parser.add_argument('--download', action='store_true', help='Retrieve missing files from the manifest public URLs')
    parser.add_argument('--cache-dir', type=Path, default=Path('source-downloads'))
    parser.add_argument('--output-dir', type=Path, required=True)
    parser.add_argument('--manifest', type=Path, default=Path(__file__).with_name('source-manifest.yaml'))
    args = parser.parse_args()
    manifest = yaml.safe_load(args.manifest.read_text())
    mapping = yaml.safe_load(args.input_map.read_text()) if args.input_map else {}
    resolved = {}
    for item in manifest['sources']:
        key = item['key']
        if key in mapping:
            path = Path(mapping[key]).expanduser()
        elif args.download:
            args.cache_dir.mkdir(parents=True, exist_ok=True)
            path = args.cache_dir / item['filename']
            if not path.exists():
                with urlopen(Request(item['url'], headers={'User-Agent': 'DSP-source-extraction/1.0'}), timeout=90) as response:
                    raw = response.read()
                if hashlib.sha256(raw).hexdigest() != item['sha256']:
                    raise ValueError(f'{key}: downloaded bytes differ from the recorded source; inspect independently, do not silently replace')
                path.write_bytes(raw)
        else:
            raise ValueError(f'{key}: supply a saved file in --input-map or explicitly use --download')
        raw = path.read_bytes()
        if hashlib.sha256(raw).hexdigest() != item['sha256']:
            raise ValueError(f'{key}: source hash mismatch')
        resolved[key] = path

    target = manifest['target']
    results = {'target': target, 'measurements': []}
    # RNA capture: exact ENSEMBL/symbol membership, all measured fields retained.
    book = xlrd.open_workbook(str(resolved['rna-table']))
    for sheet in book.sheets():
        header = sheet.row_values(0)
        for i in range(1, sheet.nrows):
            row = sheet.row_values(i)
            if target['ensembl'] in row and target['symbol'] in row:
                results['measurements'].append({'source': 'PMID:22658674', 'sheet': sheet.name,
                    'excel_row': i + 1, 'fields': dict(zip(header, row))})
    # Exosome table: export measurement fields only, not copied functional annotations.
    book = xlrd.open_workbook(str(resolved['parotid-table']))
    for sheet in book.sheets():
        header = sheet.row_values(0)
        if 'Gene' not in header:
            continue
        gene_col = header.index('Gene')
        columns = ['LocusID', 'Description', 'Sequence Count', 'SpectrumCount', 'Sequence Coverage', 'Length', 'Gene']
        for i in range(1, sheet.nrows):
            row = sheet.row_values(i)
            if row[gene_col] == target['symbol']:
                results['measurements'].append({'source': 'PMID:19199708', 'sheet': sheet.name,
                    'excel_row': i + 1, 'fields': {h: row[header.index(h)] for h in columns}})
    # Urinary Table 1: identify the target by its protein name and preserve literal cells.
    soup = BeautifulSoup(resolved['urinary-original'].read_bytes(), 'html.parser')
    for table_index, table in enumerate(soup.find_all('table')):
        for row_index, tr in enumerate(table.find_all('tr')):
            cells = [' '.join(c.stripped_strings) for c in tr.find_all(['th','td'], recursive=False)]
            if any(target['protein_name'].lower() in c.lower() for c in cells):
                results['measurements'].append({'source': 'PMID:19056867', 'html_table_index': table_index,
                    'html_row_index': row_index, 'measurement_cells': cells[:4]})
    # Study-specific thesis Annex 8.2, not the later chromatin-study tables.
    with tempfile.TemporaryDirectory(prefix='dsp-thesis-') as work:
        text_path = Path(work) / 'thesis.txt'
        subprocess.run(['pdftotext','-layout',str(resolved['sperm-thesis']),str(text_path)], check=True)
        text = text_path.read_text()
    pattern = re.compile(r'^\s*' + re.escape(target['symbol']) + r'\s+(.+?)\s+' + re.escape(target['uniprot']) + r'\s+(\d+(?:\.\d+)?)\s+(\d+)\s*$', re.M)
    sections = list(re.finditer(re.escape('8.2. Article publicat i informació suplementària'), text))
    if not sections:
        raise ValueError('Cannot locate the thesis study-specific annex')
    # The contents page repeats the heading; only actual measured rows are emitted.
    for heading in sections:
        start = heading.start()
        end = text.find('8.3.', start + 10)
        if end < 0:
            raise ValueError('Cannot bound the thesis study-specific annex')
        for match in pattern.finditer(text[start:end]):
            results['measurements'].append({'source': 'PMID:21630459 author thesis', 'section': 'Annex 8.2 / Table 8.1',
                'symbol': target['symbol'], 'accession': target['uniprot'], 'description': match.group(1).strip(),
                'coverage_percent': float(match.group(2)), 'peptides': int(match.group(3))})

    # Exact Reactome graph traversal from selected immutable API responses.
    query = {str(item['db_id']): json.loads(resolved[item['key']].read_text())
             for item in manifest['sources'] if item.get('kind') == 'reactome-query'}
    paths = []
    complex_classes = {'Complex','DefinedSet','CandidateSet','OpenSet','Polymer'}
    def walk(obj, path, seen):
        if isinstance(obj, int): obj = query[str(obj)]
        identifier = obj['dbId']
        if identifier in seen: return
        name = obj.get('displayName', '')
        category = obj.get('schemaClass', '')
        if category not in complex_classes and not any(n.lower() in name.lower() for n in [target['symbol'],target['protein_name']]):
            return
        current = query[str(identifier)]
        step = {'db_id': identifier, 'name': name, 'schema_class': category}
        if current.get('referenceEntity', {}).get('identifier') == target['uniprot']:
            paths.append({'steps': path + [step], 'accession': target['uniprot'],
                'start': current.get('startCoordinate'), 'end': current.get('endCoordinate'),
                'compartments': [c.get('displayName') for c in current.get('compartment',[])]})
            return
        for edge in ['hasComponent','hasMember','hasCandidate','repeatedUnit']:
            for child in current.get(edge, []):
                walk(child, path + [dict(step, edge=edge)], seen | {identifier})
    for identifier in manifest['reactome_events']:
        event = query[str(identifier)]
        for edge in ['input','output']:
            for child in event.get(edge, []):
                walk(child, [{'db_id':identifier,'name':event['displayName'],'schema_class':event['schemaClass'],'edge':edge}], set())
    args.output_dir.mkdir(parents=True, exist_ok=True)
    (args.output_dir/'measurements.yaml').write_text(yaml.safe_dump(results, allow_unicode=True, sort_keys=False))
    (args.output_dir/'reactome-paths.yaml').write_text(yaml.safe_dump({'target':target['uniprot'],'paths':paths}, allow_unicode=True, sort_keys=False))
    print(json.dumps({'measurement_records':len(results['measurements']),'reactome_paths':len(paths),'authenticated_sources':len(resolved)}))


if __name__ == '__main__':
    main()
