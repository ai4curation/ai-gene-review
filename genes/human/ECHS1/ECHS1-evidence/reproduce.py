#!/usr/bin/env python3
"""Extract selected interaction and mitochondrial-inventory records from saved inputs.

Python 3.9+, standard library only. Original input hashes are mandatory.
No network requests, credentials, manuscript text or curation decisions are generated.
"""
import argparse
import hashlib
import json
import posixpath
from pathlib import Path
import xml.etree.ElementTree as ET
import zipfile

HERE = Path(__file__).resolve().parent
NS = {'s': 'http://schemas.openxmlformats.org/spreadsheetml/2006/main',
      'r': 'http://schemas.openxmlformats.org/officeDocument/2006/relationships'}


def authenticate(path, expected):
    data = path.read_bytes()
    actual = hashlib.sha256(data).hexdigest()
    if actual != expected:
        raise ValueError(f'Input hash mismatch for {path}: {actual}')
    return data


def interactions(data, target, publications):
    records = []
    selected = []
    for physical_line, line in enumerate(data.decode('utf-8').splitlines(), 1):
        if not line or line.startswith('#'):
            continue
        cells = line.split('\t')
        if len(cells) < 15:
            raise ValueError(f'Incomplete MITAB record at line {physical_line}')
        records.append(cells)
        accessions = {token.split(':', 1)[-1] for cell in cells[:2]
                      for token in cell.split('|')}
        paper_ids = {token.split(':', 1)[-1] for token in cells[8].split('|')
                     if token.startswith('pubmed:')}
        if target in accessions and paper_ids.intersection(publications):
            selected.append({'physical_line': physical_line, 'columns': cells})
    return {'total_records': len(records), 'selected': selected}


def column_number(address):
    number = 0
    for char in address:
        if not char.isalpha():
            break
        number = number * 26 + ord(char.upper()) - ord('A') + 1
    return number


def workbook(data, target):
    result = []
    import io
    with zipfile.ZipFile(io.BytesIO(data)) as archive:
        strings = []
        if 'xl/sharedStrings.xml' in archive.namelist():
            root = ET.fromstring(archive.read('xl/sharedStrings.xml'))
            strings = [''.join(node.itertext()) for node in root.findall('s:si', NS)]
        rels = ET.fromstring(archive.read('xl/_rels/workbook.xml.rels'))
        targets = {x.attrib['Id']: x.attrib['Target'] for x in rels}
        root = ET.fromstring(archive.read('xl/workbook.xml'))
        for sheet in root.findall('s:sheets/s:sheet', NS):
            name = sheet.attrib['name']
            if name not in ['(A) All protein groups', '(B) MitoCoP (1,134 genes)']:
                continue
            rel = targets[sheet.attrib['{' + NS['r'] + '}id']]
            member = rel.lstrip('/') if rel.startswith('/') else posixpath.normpath('xl/' + rel)
            data_root = ET.fromstring(archive.read(member))
            rows = []
            for row in data_root.findall('s:sheetData/s:row', NS):
                values = {}
                for cell in row.findall('s:c', NS):
                    index = column_number(cell.attrib['r'])
                    kind = cell.attrib.get('t')
                    value = cell.findtext('s:v', default=None, namespaces=NS)
                    if kind == 's' and value is not None:
                        value = strings[int(value)]
                    elif kind == 'inlineStr':
                        value = ''.join(cell.find('s:is', NS).itertext())
                    elif value is not None and kind not in ['str', 'e']:
                        value = float(value) if any(x in value.lower() for x in ['.', 'e']) else int(value)
                    values[index] = value
                rows.append((int(row.attrib['r']), values))
            headers = dict(rows)[2]
            matches = []
            accession_column = 3 if name.startswith('(A)') else 2
            for number, values in rows:
                accessions = str(values.get(accession_column, '')).split(';')
                if target not in accessions:
                    continue
                fields = [{'column': index, 'header': header, 'value': values.get(index)}
                          for index, header in sorted(headers.items())
                          if index <= 9 or str(header).startswith('MitoCoP')
                          or str(header).startswith('Classification')]
                matches.append({'excel_row': number, 'fields': fields})
            result.append({'sheet': name, 'matches': matches})
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ['intact', 'mint', 'mitocop']:
        parser.add_argument('--' + name, required=True, type=Path)
    parser.add_argument('--target', default='P30084')
    parser.add_argument('--output', required=True, type=Path)
    args = parser.parse_args()
    manifest = json.loads((HERE/'source-manifest.json').read_text())
    raw = {name: authenticate(getattr(args, name), item['sha256'])
           for name, item in manifest['sources'].items()}
    output = {'target': args.target,
              'intact': interactions(raw['intact'], args.target, {'24510904','24947832','31046837'}),
              'mint': interactions(raw['mint'], args.target, {'23416296'}),
              'mitocop': workbook(raw['mitocop'], args.target)}
    args.output.write_text(json.dumps(output, ensure_ascii=False, indent=2)+'\n')
    print(json.dumps({'intact_selected':len(output['intact']['selected']),
                      'mint_selected':len(output['mint']['selected']),
                      'mitocop_matches':sum(len(x['matches']) for x in output['mitocop'])}))


if __name__ == '__main__':
    main()
