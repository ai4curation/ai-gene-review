#!/usr/bin/env python3
"""Replay EGFR source joins, snapshot lifecycle and the AP2M1 peptide table.

Only the standard library is required. No retrieval or curation decisions occur.
"""
import argparse
import csv
import gzip
import hashlib
import io
import json
from pathlib import Path
import re
import xml.etree.ElementTree as ET
import zipfile


def require(condition, message):
    if not condition:
        raise ValueError(message)


def load_inputs(base):
    manifest = json.loads((base / 'inputs.json').read_text())
    payloads = {}
    for name, item in manifest.items():
        raw = (base / item['path']).read_bytes()
        require(hashlib.sha256(raw).hexdigest() == item['sha256'], 'Input changed: ' + name)
        if name == 'intact':
            raw = gzip.decompress(raw)
            require(hashlib.sha256(raw).hexdigest() == item['uncompressed_sha256'], 'Decompressed interaction source changed')
        payloads[name] = raw
    return manifest, payloads


def contexts(tsv):
    rows = list(csv.reader(io.StringIO(tsv.decode()), delimiter='\t'))
    header, rows = rows[0], rows[1:]
    require(header[0] in ['GENE PRODUCT DB', 'DB'], 'Unexpected GOA header')
    values = []
    for line, row in enumerate(rows, 2):
        qualifier = row[3].split('|')
        relation = next((q for q in qualifier if q != 'NOT'), None)
        support = tuple(sorted(set(filter(None, re.split(r'[|,]', row[10])))))
        isoform = row[1] if re.search(r'-\d+$', row[1]) else None
        key = (row[4], row[8], row[9], 'NOT' in qualifier, support, isoform, relation)
        values.append((line, key))
    return values


def source_key(source):
    return (source['term']['id'], source['evidence_type'], source['original_reference_id'],
            bool(source.get('negated')), tuple(sorted(set(source.get('supporting_entities') or []))),
            source.get('isoform'), source.get('qualifier'))


def interaction_projection(raw, sources):
    records = list(csv.reader(io.StringIO(raw.decode()), delimiter='\t'))
    require(all(len(r) >= 42 for r in records), 'Incomplete MITAB 2.7 fields')
    def ids(row, side):
        return set((row[side] + '|' + row[side + 2]).lower().split('|'))
    joins, selected = [], {}
    for item in sources:
        source = item['source']
        if source['evidence_type'] != 'IPI':
            continue
        partners = source.get('supporting_entities', [])
        if not partners and source['term']['id'] == 'GO:0042802':
            partners = ['UniProtKB:P00533']
        partner_rows = []
        for partner in partners:
            if not partner.startswith('UniProtKB:'):
                continue
            accession = partner.split(':', 1)[1].lower()
            found = []
            for line, record in enumerate(records, 1):
                if 'pubmed:' + source.get('original_reference_id', '').split(':')[-1] not in record[8].split('|'):
                    continue
                sides = [side for side in (0, 1) if 'uniprotkb:p00533' in ids(record, side)
                         and 'uniprotkb:' + accession in ids(record, 1 - side)]
                if sides:
                    found.append({'line': line, 'target_sides': sides})
                    selected[line] = record
            partner_rows.append({'partner': partner, 'records': found})
        joins.append({'source_row': item['annotation_index'], 'source_reference': source.get('original_reference_id'),
                      'term': source['term']['id'], 'partners': partner_rows})
    fields = {0: 'id_a', 1: 'id_b', 2: 'alternative_ids_a', 3: 'alternative_ids_b', 6: 'method',
              8: 'publication', 9: 'taxon_a', 10: 'taxon_b', 11: 'interaction_type', 13: 'record_ids',
              14: 'confidence', 16: 'biological_role_a', 17: 'biological_role_b',
              18: 'experimental_role_a', 19: 'experimental_role_b', 20: 'interactor_type_a',
              21: 'interactor_type_b', 32: 'checksum_a', 33: 'checksum_b',
              35: 'negative', 36: 'features_a', 37: 'features_b'}
    compact = [{'line': line, **{name: record[i] for i, name in fields.items()}}
               for line, record in sorted(selected.items())]
    return {'raw_records': len(records), 'joins': joins, 'selected_records': compact}


def workbook_rows(raw, sheet_name):
    ns = {'m': 'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}
    rel_ns = '{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id'
    with zipfile.ZipFile(io.BytesIO(raw)) as archive:
        strings = []
        if 'xl/sharedStrings.xml' in archive.namelist():
            root = ET.fromstring(archive.read('xl/sharedStrings.xml'))
            strings = [''.join(node.itertext()) for node in root.findall('m:si', ns)]
        workbook = ET.fromstring(archive.read('xl/workbook.xml'))
        sheets = [s for s in workbook.findall('m:sheets/m:sheet', ns) if s.attrib['name'] == sheet_name]
        require(len(sheets) == 1, 'Worksheet not uniquely identified')
        relations = ET.fromstring(archive.read('xl/_rels/workbook.xml.rels'))
        target = next(r.attrib['Target'] for r in relations if r.attrib['Id'] == sheets[0].attrib[rel_ns])
        target = target.lstrip('/') if target.startswith('/') else 'xl/' + target
        root = ET.fromstring(archive.read(target))
        result = []
        for row in root.findall('m:sheetData/m:row', ns):
            cells = {}
            for cell in row.findall('m:c', ns):
                letters = re.match(r'[A-Z]+', cell.attrib['r']).group()
                col = 0
                for char in letters:
                    col = col * 26 + ord(char) - 64
                value = cell.find('m:v', ns)
                kind = cell.attrib.get('t')
                if kind == 's':
                    value = strings[int(value.text)] if value is not None else None
                elif kind == 'inlineStr':
                    node = cell.find('m:is', ns)
                    value = ''.join(node.itertext()) if node is not None else None
                elif value is not None:
                    value = value.text
                    if kind not in ('str', 'e'):
                        value = float(value) if any(x in value.lower() for x in ('.', 'e')) else int(value)
                cells[col - 1] = value
            result.append({'zero_based_row': int(row.attrib['r']) - 1,
                           'cells': [cells.get(i) for i in range(max(cells, default=-1) + 1)]})
        return result


def replay(base):
    manifest, data = load_inputs(base)
    sources = json.loads(data['source_contexts'])
    current = contexts(data['current_goa'])
    current_keys = {key for _, key in current}
    retired = [s['annotation_index'] for s in sources if s['source'].get('retired')]
    missing = [s['annotation_index'] for s in sources if s['action'] != 'NEW'
               and source_key(s['source']) not in current_keys]
    active = {source_key(s['source']) for s in sources if s['action'] != 'NEW' and not s['source'].get('retired')}
    require(retired == missing, 'Lifecycle flags do not match absent historical contexts')
    require(active == current_keys, 'Current source coverage differs')
    lifecycle = {'all_objects': len(sources), 'historical_retired_indices': retired,
                 'current_raw_rows': len(current), 'current_distinct_contexts': len(current_keys),
                 'historical_new_indices': [s['annotation_index'] for s in sources if s['action'] == 'NEW'],
                 'old_raw_rows': len(contexts(data['old_goa']))}
    table = workbook_rows(data['peptide_table'], manifest['peptide_table']['sheet'])
    selected = [r for r in table if 'P00533' in r['cells']]
    peptide = {'sheet': manifest['peptide_table']['sheet'], 'source_rows': len(table),
               'header': next(r for r in table if 'SLIM Containing Protein Accession' in r['cells']),
               'target_rows': selected}
    return {'interactions': interaction_projection(data['intact'], sources), 'lifecycle': lifecycle, 'peptide': peptide}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--base', type=Path, default=Path(__file__).resolve().parent)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    result = replay(args.base)
    if args.output:
        args.output.mkdir(parents=True, exist_ok=True)
        for name, value in result.items():
            (args.output / (name + '.json')).write_text(json.dumps(value, indent=2, ensure_ascii=False) + '\n')
    else:
        expected = {name: json.loads((args.base / 'outputs' / (name + '.json')).read_text()) for name in result}
        require(result == expected, 'Derived output mismatch')
    print(json.dumps({'status': 'PASS', 'raw_interactions': result['interactions']['raw_records'],
                      'source_joins': len(result['interactions']['joins']),
                      'selected_records': len(result['interactions']['selected_records']),
                      'lifecycle': result['lifecycle'], 'peptide_target_rows': len(result['peptide']['target_rows'])}))


if __name__ == '__main__':
    main()
