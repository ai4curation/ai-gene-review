#!/usr/bin/env python3
"""Extract source-scoped graph edges and reciprocal CSV records from saved primary data.

Python >=3.9, standard library only. No network calls. Dataset digests and symbol
selection are explicit input files; edge identifiers, counts and values are derived.
"""
import argparse
import csv
import hashlib
import json
from collections import defaultdict
from pathlib import Path


def digest(path):
    h = hashlib.sha256()
    with path.open('rb') as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b''):
            h.update(block)
    return h.hexdigest()


def verified_inputs(directory, manifest):
    paths = {}
    for key, record in manifest['inputs'].items():
        path = directory / record['filename']
        actual = digest(path)
        if actual != record['sha256']:
            raise ValueError(f'{key}: input digest mismatch; do not treat a changed live dataset as this snapshot')
        paths[key] = path
    return paths


def extract_graph(path, target, selected_partners):
    aspects = defaultdict(list)
    for chunk in json.loads(path.read_text()):
        for name, records in chunk.items():
            if not isinstance(records, list):
                raise ValueError(f'CX aspect {name} is not an array')
            aspects[name].extend(records)
    if not all(row.get('success', False) for row in aspects['status']):
        raise ValueError('CX response status is unsuccessful')
    nodes = {row['@id']: row for row in aspects['nodes']}
    if len(nodes) != len(aspects['nodes']):
        raise ValueError('Duplicate CX node identifiers')
    target_nodes = [row for row in aspects['nodes'] if row.get('n') == target]
    if len(target_nodes) != 1:
        raise ValueError(f'Expected one exact symbol node for {target}, found {len(target_nodes)}')
    target_id = target_nodes[0]['@id']
    node_attrs = defaultdict(list)
    edge_attrs = defaultdict(list)
    for row in aspects['nodeAttributes']:
        node_attrs[row['po']].append(row)
    for row in aspects['edgeAttributes']:
        edge_attrs[row['po']].append(row)
    incident, selected = [], []
    for edge in aspects['edges']:
        if target_id not in (edge['s'], edge['t']):
            continue
        partner_id = edge['t'] if edge['s'] == target_id else edge['s']
        partner = nodes[partner_id].get('n')
        keep = partner in selected_partners
        incident.append({'edge_id': edge['@id'], 'source_node_id': edge['s'],
                         'source_name': nodes[edge['s']].get('n'),
                         'target_node_id': edge['t'], 'target_name': nodes[edge['t']].get('n'),
                         'selected_by_partner_filter': keep})
        if keep:
            participants = [nodes[edge['s']], nodes[edge['t']]]
            # Preserve original attributes and endpoint direction. No accession or
            # isoform is inferred for a node that supplies only a gene symbol.
            selected.append({'edge': edge, 'nodes': participants,
                             'nodeAttributes': [a for n in participants for a in node_attrs[n['@id']]],
                             'edgeAttributes': edge_attrs[edge['@id']]})
    return {'network_attributes': aspects['networkAttributes'],
            'node_count': len(nodes), 'edge_count': len(aspects['edges']),
            'target_nodes': target_nodes, 'incident_count': len(incident),
            'selected_count': len(selected), 'incident_edges': incident,
            'selected_edges': selected}


def extract_csv(path, target, selected_partners):
    incident, selected = [], []
    with path.open(newline='', encoding='utf-8-sig') as handle:
        reader = csv.DictReader(handle)
        fields = reader.fieldnames
        required = {'target_gene_name', 'interactor_gene_name', 'interactor_uniprot_ids'}
        if not required <= set(fields or []):
            raise ValueError('Missing required OpenCell column(s)')
        prior_line = reader.line_num
        total = 0
        for data_index, values in enumerate(reader):
            line_start, line_end = prior_line + 1, reader.line_num
            prior_line = line_end
            total += 1
            bait, prey = values['target_gene_name'], values['interactor_gene_name']
            if target not in (bait, prey):
                continue
            partner = prey if bait == target else bait
            keep = partner in selected_partners
            row = {'data_index_zero_based': data_index,
                   'csv_line_start_one_based_including_header': line_start,
                   'csv_line_end_one_based_including_header': line_end,
                   'selected_by_partner_filter': keep, 'values': values}
            incident.append(row)
            if keep:
                selected.append(row)
    return {'columns': fields, 'data_row_count': total,
            'incident_count': len(incident), 'selected_count': len(selected),
            'incident_rows': incident, 'selected_rows': selected}


def compute(directory, manifest, selection):
    paths = verified_inputs(directory, manifest)
    target = selection['target_gene_symbol']
    if not target or not all(isinstance(x, str) and x for x in selection['apms_partner_symbols'] + selection['opencell_partner_symbols']):
        raise ValueError('Gene symbols must be nonempty strings')
    return {'selection': selection,
            'input_sha256': {key: digest(path) for key, path in paths.items()},
            'apms': extract_graph(paths['apms'], target, set(selection['apms_partner_symbols'])),
            'opencell': extract_csv(paths['opencell'], target, set(selection['opencell_partner_symbols']))}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    here = Path(__file__).resolve().parent
    parser.add_argument('--inputs-dir', required=True, type=Path)
    parser.add_argument('--manifest', type=Path, default=here / 'source-manifest.json')
    parser.add_argument('--selection', type=Path, default=here / 'selection.json')
    parser.add_argument('--output', type=Path, default=here / 'RESULTS.json')
    parser.add_argument('--check', action='store_true', help='Compare computed data with the saved output; write nothing')
    args = parser.parse_args()
    result = compute(args.inputs_dir, json.loads(args.manifest.read_text()), json.loads(args.selection.read_text()))
    encoded = json.dumps(result, indent=2, ensure_ascii=False) + '\n'
    if args.check:
        if args.output.read_text() != encoded:
            raise SystemExit('FAIL: saved output differs from raw-derived result')
    else:
        args.output.write_text(encoded)
    print(json.dumps({'status': 'PASS' if args.check else 'WRITTEN', 'target': result['selection']['target_gene_symbol'],
                      'apms_incident': result['apms']['incident_count'], 'apms_selected': result['apms']['selected_count'],
                      'opencell_incident': result['opencell']['incident_count'], 'opencell_selected': result['opencell']['selected_count']}))


if __name__ == '__main__':
    main()
