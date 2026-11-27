#!/usr/bin/env python3
"""Reconstruct EIF2AK4 PAINT, donor and ARBA provenance from hash-pinned inputs.

This program uses only the Python standard library and performs no retrieval.
It computes evidence joins, not biological curation actions.
"""
import argparse
import csv
import hashlib
import json
from pathlib import Path


def require(ok, message):
    if not ok:
        raise ValueError(message)


def load_json(path):
    return json.loads(path.read_text())


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--input-dir', type=Path, required=True,
                        help='directory containing the exact files named in inputs.json')
    parser.add_argument('--output-dir', type=Path, required=True)
    args = parser.parse_args()
    here = Path(__file__).resolve().parent
    manifest = load_json(here / 'inputs.json')
    paths = {}
    for record in manifest['inputs']:
        path = (here if record.get('bundled') else args.input_dir) / record['name']
        data = path.read_bytes()
        require(hashlib.sha256(data).hexdigest() == record['sha256'],
                'Input hash mismatch: ' + record['name'])
        require(len(data) == record['bytes'], 'Input length mismatch: ' + record['name'])
        paths[record['name']] = path
    contexts = load_json(paths['source-contexts.json'])
    uniprot = load_json(paths['UniProt-Q9P2K8.json'])
    tree = load_json(paths['PTHR11042-treeinfo.json'])['search']['tree_topology']['annotation_node']
    msa = load_json(paths['PTHR11042-familymsa.json'])['search']['MSA_list']['sequence_info']
    nodes, parent = {}, {}

    def walk(node, previous=None):
        key = node['persistent_id']
        require(key not in nodes, 'Duplicate tree node')
        nodes[key], parent[key] = node, previous
        children = node.get('children', {}).get('annotation_node', [])
        for child in ([children] if isinstance(children, dict) else children):
            walk(child, key)

    walk(tree)
    targets = [key for key, node in nodes.items()
               if 'UniProtKB=Q9P2K8' in node.get('node_name', '').split('|')]
    require(len(targets) == 1, 'Target leaf is not unique')
    target = targets[0]
    lineage, node = [], target
    while node is not None:
        lineage.append(node)
        node = parent[node]
    lineage.reverse()
    target_msa = [entry for entry in msa if entry['persistent_id'] == target]
    require(len(target_msa) == 1, 'Target MSA record is not unique')
    sequence = target_msa[0]['sequence'].replace('-', '').replace('.', '').upper()
    require(sequence == uniprot['sequence']['value'], 'Target/reference sequence mismatch')
    paint_rows = [r for r in contexts if r['source']['evidence_type'] == 'IBA']
    selected_terms = {r['source']['term']['id'] for r in paint_rows}
    all_path_records = []
    with paths['IBD.gaf'].open() as handle:
        for line, fields in enumerate(csv.reader(handle, delimiter='\t'), 1):
            if len(fields) > 14 and fields[1] in lineage:
                all_path_records.append({'line': line, 'fields': fields})
    selected_path_records = [r for r in all_path_records if r['fields'][4] in selected_terms]
    paint_joins = []
    for row in paint_rows:
        source = row['source']
        ancestors = [s.split(':')[-1] for s in source.get('supporting_entities', [])
                     if s.startswith('PANTHER:PTN')]
        require(len(ancestors) == 1 and ancestors[0] in lineage, 'IBD ancestor not on target path')
        records = [r for r in selected_path_records
                   if r['fields'][1] == ancestors[0] and r['fields'][4] == source['term']['id']
                   and r['fields'][6] == 'IBD']
        require(len(records) == 1, 'Expected one literal IBD')
        paint_joins.append({'index': row['index'], 'source': source,
                            'ancestor': ancestors[0], 'literal_IBD': records})
    paint = {'tree_nodes': len(nodes), 'msa_sequences': len(msa), 'target': target,
             'target_name': nodes[target]['node_name'], 'lineage': lineage,
             'target_sequence_length': len(sequence),
             'target_sequence_sha256': hashlib.sha256(sequence.encode()).hexdigest(),
             'target_sequence_exact': True, 'all_path_records': all_path_records,
             'term_path_records': selected_path_records, 'rows': paint_joins}

    donor_records = {}
    for accession in ['Q9QZ05', 'P15442']:
        response = load_json(paths['QuickGO-' + accession + '-page1.json'])
        require(response['numberOfHits'] == len(response['results']),
                'Incomplete donor response: ' + accession)
        donor_records[accession] = response['results']
    donors = []
    for row in contexts:
        source = row['source']
        if source['evidence_type'] != 'ISS':
            continue
        accessions = [v.split(':', 1)[1] for v in source.get('supporting_entities', [])
                      if v.startswith('UniProtKB:')]
        require(len(accessions) == 1 and accessions[0] in donor_records, 'Unexpected ISS donor')
        accession = accessions[0]
        records = [r for r in donor_records[accession] if r['goId'] == source['term']['id']]
        donors.append({'index': row['index'], 'source': source, 'donor': accession,
                       'exact_term_records': records})

    rule = load_json(paths['ARBA00028884.json'])
    databases = {'InterPro id': 'InterPro', 'PANTHER id': 'PANTHER', 'FunFam id': 'FunFam'}
    sets = []
    for index, condition_set in enumerate(rule['mainRule']['conditionSets']):
        checks = []
        for condition in condition_set['conditions']:
            kind, values = condition['type'], condition['conditionValues']
            if kind == 'taxon':
                matches = [v for v in values
                           if v['value'] in uniprot['organism']['lineage'] + [uniprot['organism']['scientificName']]
                           or str(v.get('cvId')) == str(uniprot['organism']['taxonId'])]
            else:
                require(kind in databases, 'Unsupported ARBA condition type: ' + kind)
                ids = {r['id'] for r in uniprot['uniProtKBCrossReferences']
                       if r['database'] == databases[kind]}
                matches = [v for v in values if v['value'] in ids]
            passed = not bool(matches) if condition['isNegative'] else bool(matches)
            checks.append({'condition': condition, 'matched_values': matches, 'passed': passed})
        sets.append({'index': index, 'passed': all(c['passed'] for c in checks), 'checks': checks})
    arba = {'rule': rule['uniRuleId'], 'annotations': rule['mainRule']['annotations'],
            'all_condition_sets': sets, 'satisfied_indices': [s['index'] for s in sets if s['passed']]}

    args.output_dir.mkdir(parents=True, exist_ok=False)
    for name, data in [('paint.json', paint), ('donor-joins.json', donors), ('arba.json', arba)]:
        (args.output_dir / name).write_text(json.dumps(data, indent=2, ensure_ascii=False) + '\n')
    summary = {'source_contexts': len(contexts), 'PAINT_rows': len(paint_joins),
               'ISS_rows': len(donors), 'tree_nodes': len(nodes), 'MSA_sequences': len(msa),
               'target_sequence_length': len(sequence), 'ARBA_condition_sets': len(sets),
               'ARBA_satisfied_indices': arba['satisfied_indices']}
    print(json.dumps(summary, sort_keys=True))


if __name__ == '__main__':
    main()
