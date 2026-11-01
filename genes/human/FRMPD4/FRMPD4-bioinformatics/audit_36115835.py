#!/usr/bin/env python3
"""Replay the FRMPD4 source audit; Python standard library only, no network.

The XLSX remains an external, checksum-pinned source. Outputs contain measurements
and source joins, never automatically generated GO curation decisions.
"""
import argparse
import collections
import csv
import hashlib
import json
import math
from pathlib import Path
import posixpath
import re
import xml.etree.ElementTree as ET
import zipfile

NS = {'s': 'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}
REL = '{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id'
WORKBOOK_SHA = 'ada912921164f0a79630c6a714b9ff264a7217ad3e646153ef498eb456206795'
# Original Methods: Interaction measurements with holdup experiments, Sec20.
# BI cutoff and columns: measured BI, conversion peptide concentration (micromolar).
METHODS = {'DAPF': (0.05, 'M', 'P'), 'SAPF': (0.1, 'AB', 'AE'), 'LYSC': (0.1, 'R', 'V')}


def require(condition, message):
    if not condition:
        raise ValueError(message)


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def tabread(path):
    with Path(path).open(newline='') as stream:
        return list(csv.DictReader(stream, delimiter='\t'))


def tabwrite(path, rows, fields=None):
    require(rows or fields, 'No output fields')
    with path.open('w', newline='') as stream:
        writer = csv.DictWriter(stream, fieldnames=fields or list(rows[0]), delimiter='\t', lineterminator='\n')
        writer.writeheader()
        writer.writerows(rows)


def read_workbook(path):
    require(digest(path) == WORKBOOK_SHA, 'Workbook checksum changed; inspect before use')
    with zipfile.ZipFile(path) as archive:
        strings = []
        if 'xl/sharedStrings.xml' in archive.namelist():
            root = ET.fromstring(archive.read('xl/sharedStrings.xml'))
            strings = [''.join(si.itertext()) for si in root]
        rels = {r.get('Id'): r.get('Target') for r in ET.fromstring(archive.read('xl/_rels/workbook.xml.rels'))}
        workbook = ET.fromstring(archive.read('xl/workbook.xml'))
        sheet = next(s for s in workbook.findall('s:sheets/s:sheet', NS) if s.get('name') == 'PDZ-PBM interactome')
        target = rels[sheet.get(REL)]
        target = target.lstrip('/') if target.startswith('/') else posixpath.normpath('xl/' + target)
        rows, headers = [], None
        with archive.open(target) as stream:
            for _, row in ET.iterparse(stream, events=('end',)):
                if row.tag != '{' + NS['s'] + '}row':
                    continue
                cells = {}
                for cell in row.findall('s:c', NS):
                    value = cell.find('s:v', NS)
                    value = value.text if value is not None else None
                    if cell.get('t') == 's' and value is not None:
                        value = strings[int(value)]
                    elif cell.get('t') == 'inlineStr':
                        value = ''.join(cell.find('s:is', NS).itertext())
                    if value is not None:
                        cells[re.sub('[0-9]', '', cell.get('r'))] = value
                if row.get('r') == '1':
                    headers = cells
                if cells.get('A') == 'FRMPD4' or cells.get('C') == 'Q14CM0':
                    rows.append({'row': int(row.get('r')), 'cells': cells})
                row.clear()
    require(headers['AG'] == 'COMP_neglogKd' and headers['AH'] == 'COMP_method', 'Column meanings changed')
    return headers, rows


def describe_measurement(row):
    values = row['cells']
    comp = float(values['AG']) if 'AG' in values else None
    fp = float(values['H']) if 'H' in values else None
    method = values.get('AH', '')
    cutoff, bi_column, concentration_column = METHODS.get(method, (None, '', ''))
    bi = float(values[bi_column]) if bi_column in values else None
    concentration = float(values[concentration_column]) if concentration_column in values else None
    # Derived sensitivity estimate from original Eq2 with the stated usual 4uM PDZ.
    # This is explicitly a calculation, NOT an author-reported per-domain cutoff.
    estimated_pkd_limit = None
    if concentration is not None and cutoff is not None:
        kd_limit_um = (concentration - 4.0 * cutoff) * (1.0 - cutoff) / cutoff
        if kd_limit_um > 0:
            estimated_pkd_limit = -math.log10(kd_limit_um * 1e-6)
    quantified = (comp is not None and comp > 0) or (fp is not None and fp > 0)
    if comp == 0:
        require(bi is not None and cutoff is not None and bi < cutoff,
                'Composite zero lacks matching below-cutoff BI: row ' + str(row['row']))
    return dict(workbook_row=row['row'], PDZ=values.get('A', ''), PBM=values.get('B', ''),
                PBM_accession=values.get('C', ''), natural_10mer=values.get('D', ''),
                assayed_10mer=values.get('E', ''), composite_pKd=values.get('AG', ''),
                composite_method=method, FP_Kd_uM=values.get('H', ''),
                quantified=quantified, BI_cell=bi_column + str(row['row']) if bi_column else '',
                BI=values.get(bi_column, ''), method_BI_cutoff=cutoff,
                BI_below_cutoff=bi < cutoff if bi is not None and cutoff is not None else '',
                conversion_concentration_cell=concentration_column + str(row['row']) if concentration_column else '',
                conversion_concentration_uM=values.get(concentration_column, ''),
                calculated_pKd_limit_assuming_4uM_PDZ=estimated_pkd_limit,
                author_reported_pKd_limit='not separately supplied in this worksheet',
                literal_less_than_value=any(v.startswith('<') for v in values.values()),
                interpretation='quantified fragment interaction' if quantified else 'composite zero with below-detection BI; not absence')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--workbook', type=Path, required=True)
    parser.add_argument('--goa', type=Path, required=True)
    parser.add_argument('--inputs', type=Path, default=Path(__file__).resolve().parent / 'inputs')
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    metadata = json.loads((args.inputs / 'provenance.json').read_text())
    for name, expected in metadata['input_sha256'].items():
        require(digest(args.inputs / name) == expected, 'Input snapshot changed: ' + name)
    require(digest(args.goa) == metadata['goa_sha256'], 'Native GOA export changed')
    goa = tabread(args.goa)
    contexts = tabread(args.inputs / 'contexts.tsv')
    records = [json.loads(line) for line in (args.inputs / 'intact-36115835.jsonl').read_text().splitlines()]
    headers, target_rows = read_workbook(args.workbook)
    joins, measurements = [], []
    used = set()
    for context in contexts:
        partner = context['partner']
        native = goa[int(context['tsv_physical_line']) - 2]
        require(native['WITH/FROM'] == 'UniProtKB:' + partner and native['REFERENCE'] == 'PMID:36115835'
                and native['GO TERM'] == 'GO:0005515' and native['GO EVIDENCE CODE'] == 'IPI', 'GOA context mismatch')
        matched, aliases = [], set()
        for record in records:
            f = record['fields']
            if {f[0].split('-')[0], f[1].split('-')[0]} != {'uniprotkb:Q14CM0', 'uniprotkb:' + partner}:
                continue
            require('pubmed:36115835' in f[8], 'Wrong source')
            side = int(f[1].split('-')[0] == 'uniprotkb:' + partner)
            aliases.update(re.findall(r'uniprotkb:([^|]+)\(gene name(?: synonym)?\)', f[4 + side]))
            matched.append(record)
            used.add(record['source_line'])
        aliases = {a.casefold() for a in aliases}
        require(matched, 'Missing curated partner snapshot ' + partner)
        selected = []
        for row in target_rows:
            v = row['cells']
            forward = v.get('C') == 'Q14CM0' and v.get('A', '').split('_')[0].casefold() in aliases
            reverse = v.get('A') == 'FRMPD4' and v.get('C') == partner
            if not (forward or reverse):
                continue
            if forward:
                require(v['D'] == v['E'] == 'RLPKIKETTV', 'Modified target peptide')
            m = describe_measurement(row)
            m.update(raw_index=context['raw_index'], tsv_physical_line=context['tsv_physical_line'],
                     partner=partner, target_role='C-terminal peptide 1313-1322' if forward else 'PDZ domain 67-160')
            selected.append(m)
            measurements.append(m)
        require(selected, 'No original author rows for ' + partner)
        positives = [m for m in selected if m['quantified']]
        finite, numeric_matches = [], []
        for record in matched:
            literal = record['fields'][29]
            match = re.fullmatch(r'kd:([\d.]+)x10\^-6\(molar\)', literal)
            if not match:
                require(literal in ('kd:1.0x10(molar)', '-'), 'Unrecognized curated parameter ' + literal)
                continue
            finite.append(record)
            value = float(match[1])
            for m in positives:
                candidates = []
                if m['composite_pKd'] and float(m['composite_pKd']) > 0:
                    candidates.append(10 ** (6 - float(m['composite_pKd'])))
                if m['FP_Kd_uM']:
                    candidates.append(float(m['FP_Kd_uM']))
                if any(math.isclose(value, x, rel_tol=1e-6) for x in candidates):
                    numeric_matches.append(m['workbook_row'])
        require(not finite or numeric_matches, 'Finite curated affinity has no numeric original match')
        require(positives or not finite, 'Unsupported finite curated affinity')
        joins.append(dict(raw_index=context['raw_index'], tsv_physical_line=context['tsv_physical_line'], partner=partner,
                          author_rows=','.join(str(m['workbook_row']) for m in selected),
                          quantified_rows=','.join(str(m['workbook_row']) for m in positives),
                          target_roles=';'.join(sorted({m['target_role'] for m in positives})),
                          intact_records=len(matched), finite_intact_records=len(finite),
                          numeric_match_rows=','.join(map(str, sorted(set(numeric_matches)))),
                          interpretation='positive original fragment measurement' if positives else 'unresolved quantitative support'))
    require(len(used) == len(records), 'Unjoined curated records')
    args.output.mkdir(parents=True, exist_ok=False)
    columns = list(headers)
    tabwrite(args.output / 'all-target-rows.tsv', [dict(workbook_row=r['row'], **{c:r['cells'].get(c, '') for c in columns}) for r in target_rows])
    tabwrite(args.output / 'matched-measurements.tsv', measurements)
    tabwrite(args.output / 'context-summary.tsv', joins)
    summary = dict(workbook_sha256=digest(args.workbook), goa_sha256=digest(args.goa),
                   target_workbook_rows=len(target_rows), contexts=len(joins), matched_measurements=len(measurements),
                   intact_records=len(records), interpretations=dict(collections.Counter(x['interpretation'] for x in joins)),
                   original_positive_without_finite_intact=[x['raw_index'] for x in joins if x['quantified_rows'] and not x['finite_intact_records']],
                   limits=['No source row is silently removed.', 'No exact author-reported per-domain pKd cutoff is invented.',
                           'Composite zero and the literal IntAct 10-molar-looking field are not physical affinity measurements.',
                           'No GO action, full-length endogenous complex, infection process or physiological role is inferred automatically.'])
    (args.output / 'summary.json').write_text(json.dumps(summary, indent=2) + '\n')
    print(json.dumps(summary, indent=2))


if __name__ == '__main__':
    main()
