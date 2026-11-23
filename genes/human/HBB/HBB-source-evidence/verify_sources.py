"""Extract compact, reproducible source records without retaining full responses.

Python standard library only. A failed retrieval/identity check is reported as
inconclusive and exits nonzero; results are never substituted from expectations.
The output directory must not already contain either output file.
"""

import argparse
import datetime
import hashlib
from html.parser import HTMLParser
import json
from pathlib import Path
import re
from urllib.request import Request, urlopen


class Tables(HTMLParser):
    def __init__(self):
        super().__init__()
        self.tables, self.lis = [], []
        self.table = self.row = self.cell = self.li = None

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'table':
            self.table = []
        if tag == 'tr':
            self.row = []
        if tag in ('td', 'th'):
            self.cell = []
        if tag == 'li':
            self.li = []
        if tag == 'a' and self.li is not None and attrs.get('href'):
            self.li.append(attrs['href'])

    def handle_data(self, value):
        if self.cell is not None:
            self.cell.append(value)
        if self.li is not None:
            self.li.append(value)

    def handle_endtag(self, tag):
        if tag in ('td', 'th') and self.cell is not None:
            if self.row is not None:
                self.row.append(' '.join(' '.join(self.cell).split()))
            self.cell = None
        if tag == 'tr' and self.row is not None:
            if self.table is not None:
                self.table.append(self.row)
            self.row = None
        if tag == 'table' and self.table is not None:
            self.tables.append(self.table)
            self.table = None
        if tag == 'li' and self.li is not None:
            self.lis.append(' '.join(' '.join(self.li).split()))
            self.li = None


def digest(record):
    data = json.dumps(record, ensure_ascii=False, sort_keys=True, separators=(',', ':')).encode()
    return hashlib.sha256(data).hexdigest()


def fetch(url, accept='*/*'):
    request = Request(url, headers={'User-Agent': 'ai-gene-review source evidence', 'Accept': accept})
    with urlopen(request, timeout=30) as response:
        raw = response.read()
        meta = {'url': response.url, 'http_status': response.status, 'bytes': len(raw),
                'response_sha256': hashlib.sha256(raw).hexdigest()}
    return raw, meta


def table_row(raw, identifier):
    parser = Tables()
    parser.feed(raw.decode('utf-8'))
    matches = []
    for table in parser.tables:
        if not table:
            continue
        for row in table[1:]:
            if identifier in row:
                if len(row) != len(table[0]):
                    raise ValueError('Header/data column counts differ')
                matches.append(dict(zip(table[0], row)))
    if len(matches) != 1:
        raise ValueError(f'{identifier}: expected one source row, found {len(matches)}')
    return matches[0], parser


def field(row, fragment):
    values = [v for k, v in row.items() if fragment.lower() in k.lower()]
    if len(values) != 1:
        raise ValueError(f'Ambiguous or missing column: {fragment}')
    return values[0]


def verified(meta, record, quote):
    return {'status': 'verified', 'source': meta, 'record': record,
            'extraction_sha256': digest(record), 'quote': quote}


def urinary(args):
    raw, meta = fetch('https://esbl.nhlbi.nih.gov/Databases/UrinaryExosomes/')
    row, parser = table_row(raw, args.refseq)
    selected = {key: field(row, key) for key in ['Protein Name', 'Gene Name', 'Peptide', 'RefSeq', 'Reference']}
    if selected['Gene Name'] != args.gene:
        raise ValueError('NIH gene identity differs from requested gene')
    refnum = int(selected['Reference'])
    bibliography = parser.lis[refnum - 1]
    pmids = re.findall(r'(?:pubmed/|pubmed\.ncbi\.nlm\.nih\.gov/)(\d+)', bibliography)
    if len(set(pmids)) != 1:
        raise ValueError('NIH bibliography does not identify a unique PubMed record')
    selected['PMID'] = pmids[0]
    selected['bibliography'] = bibliography
    quote = (f"NIH urinary exosome entry: {selected['Gene Name']} | {selected['RefSeq']} | "
             f"peptides={selected['Peptide']} | PMID:{selected['PMID']}.")
    # Exercise the same row selector on a different source-provided identifier.
    controls = [dict(zip(t[0], r)) for t in parser.tables if t for r in t[1:]
                if len(r) == len(t[0]) and args.refseq not in r and any('RefSeq' in k for k in t[0])]
    if not controls:
        raise ValueError('No independent table row available for parser control')
    control_id = field(controls[0], 'RefSeq')
    control, _ = table_row(raw, control_id)
    control_selected = {key: field(control, key) for key in ['Gene Name', 'RefSeq', 'Peptide']}
    result = verified(meta, selected, quote)
    result['parser_control'] = {'different_identifier': control_id,
                                'record': control_selected, 'sha256': digest(control_selected)}
    return result


def reactome(args, stable_id):
    raw, meta = fetch('https://reactome.org/ContentService/data/query/' + stable_id, 'application/json')
    item = json.loads(raw)
    ref = item['referenceEntity']
    if item['stId'] != stable_id or ref['identifier'] != args.uniprot:
        raise ValueError('Reactome entity/accession does not match requested identity')
    if ref['databaseName'] != 'UniProt' or item['speciesName'] != 'Homo sapiens':
        raise ValueError('Unexpected reference database or species')
    compartments = [{'id': 'GO:' + c['accession'], 'label': c['displayName']}
                    for c in item['compartment']]
    selected = {'stId': item['stId'], 'displayName': item['displayName'],
                'speciesName': item['speciesName'], 'uniprot': ref['identifier'],
                'compartments': compartments}
    quote = (f"Reactome {selected['stId']}: UniProt:{selected['uniprot']} | {selected['speciesName']} | "
             + '; '.join(c['id'] + ' ' + c['label'] for c in compartments) + '.')
    return verified(meta, selected, quote)


def platelet(args):
    raw, meta = fetch('https://pmc.ncbi.nlm.nih.gov/articles/PMC3650338/')
    row, _ = table_row(raw, args.platelet_protein)
    if 'id="TI"' not in raw.decode('utf-8'):
        raise ValueError('Expected primary Table I section not present')
    quote = 'PMC3650338 Table I: ' + ' | '.join(f'{k}={v}' for k, v in row.items()) + '.'
    return verified(meta, {'table': 'Table I (section TI)', 'row': row}, quote)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--gene', required=True)
    parser.add_argument('--refseq', required=True)
    parser.add_argument('--uniprot', required=True)
    parser.add_argument('--platelet-protein', required=True)
    parser.add_argument('--tertiary-entity', required=True)
    parser.add_argument('--ficolin-entity', required=True)
    parser.add_argument('--output-dir', type=Path, required=True)
    args = parser.parse_args()
    output = args.output_dir
    if any((output / f).exists() for f in ['checks.json', 'RESULTS.md']):
        parser.error('Use a new output directory; retained evidence will not be overwritten')
    calls = {'urinary_exosome': lambda: urinary(args),
             'tertiary': lambda: reactome(args, args.tertiary_entity),
             'ficolin': lambda: reactome(args, args.ficolin_entity),
             'platelet': lambda: platelet(args)}
    checks = {}
    for name, call in calls.items():
        try:
            checks[name] = call()
        except Exception as error:
            checks[name] = {'status': 'inconclusive', 'error': f'{type(error).__name__}: {error}'}
    result = {'checked_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
              'parameters': {k: str(v) for k, v in vars(args).items()},
              'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'checks': checks}
    lines = ['# Source-record extraction results', '', 'Generated by `verify_sources.py`.', '',
             'These are database/table observations. Functional interpretation is in the gene review and notes.', '',
             'Full HTTP responses were parsed in memory and were not saved. Response hashes may change when upstream HTML changes; normalized extraction hashes identify the selected records.', '',
             'Checked UTC: ' + result['checked_utc'], '']
    for name, item in checks.items():
        lines += ['## ' + name, '', 'Status: ' + item['status'], '']
        if item['status'] == 'verified':
            lines += [item['quote'], '', 'Source: ' + item['source']['url'], '',
                      'Raw-response SHA256: `' + item['source']['response_sha256'] + '`', '',
                      'Selected-record SHA256: `' + item['extraction_sha256'] + '`', '']
            if 'parser_control' in item:
                lines += ['Independent table-row parser control: `' + json.dumps(item['parser_control'], ensure_ascii=False, sort_keys=True) + '`', '']
        else:
            lines += [item['error'], '']
    output.mkdir(parents=True, exist_ok=True)
    (output / 'checks.json').write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
    (output / 'RESULTS.md').write_text('\n'.join(lines))
    print(json.dumps({k: v['status'] for k, v in checks.items()}))
    return 0 if all(c['status'] == 'verified' for c in checks.values()) else 1


if __name__ == '__main__':
    raise SystemExit(main())
