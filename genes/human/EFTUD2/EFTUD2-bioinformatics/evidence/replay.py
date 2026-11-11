#!/usr/bin/env python3
"""Recompute literal EFTUD2 evidence projections using only bundled database records."""
import argparse
import hashlib
import io
import json
from pathlib import Path
import re
import tarfile

HERE = Path(__file__).resolve().parent

def require(condition, message):
    if not condition:
        raise ValueError(message)

def read_inputs(archive):
    manifest = json.loads((HERE / 'input-manifest.json').read_text())
    if not archive.is_file():
        raise ValueError(f'Missing input archive: {archive}')
    require(hashlib.sha256(archive.read_bytes()).hexdigest() == manifest['archive_sha256'], 'Input archive SHA256 mismatch')
    expected = {x['name']: x for x in manifest['inputs']}
    data = {}
    with tarfile.open(archive, 'r:gz') as handle:
        for member in handle:
            require(member.isfile() and member.name in expected, f'Unexpected archive member: {member.name}')
            require(member.name not in data, f'Duplicate archive member: {member.name}')
            raw = handle.extractfile(member).read()
            record = expected[member.name]
            require(len(raw) == record['bytes'] and hashlib.sha256(raw).hexdigest() == record['sha256'], f'Input checksum: {member.name}')
            data[member.name] = raw
    require(set(data) == set(expected), 'Missing input records')
    return data

def project(data, config):
    load = lambda name: json.loads(data[name])
    accession = config['target_accession']
    target = load('UniProt-' + accession + '.json')
    sequence = target['sequence']['value']
    root = load('PTHR42908-tree.json')['search']['tree_topology']['annotation_node']
    target_paths = []
    node_count = 0
    def visit(node, path):
        nonlocal node_count
        node_count += 1
        current = path + [{'id': node['persistent_id'], 'name': node.get('node_name'), 'event': node.get('event_type')}]
        if node['persistent_id'] == config['target_leaf']:
            target_paths.append(current)
        children = node.get('children', {}).get('annotation_node', [])
        for child in children if isinstance(children, list) else [children]:
            visit(child, current)
    visit(root, [])
    require(len(target_paths) == 1, 'Target must have one literal tree path')
    path_ids = {x['id'] for x in target_paths[0]}
    assertions = []
    for index, line in enumerate(data['IBD.gaf'].decode().splitlines()):
        cells = line.split('\t')
        if len(cells) >= 15 and cells[1] in path_ids:
            assertions.append({'line': index, 'node': cells[1], 'qualifier': cells[3], 'go_id': cells[4], 'evidence': cells[6], 'donors': cells[7].split('|')})
    msa = load('PTHR42908-familymsa.json')['search']['MSA_list']['sequence_info']
    alignment = [x for x in msa if x['persistent_id'] == config['target_leaf']]
    require(len(alignment) == 1, 'One MSA target expected')
    ungapped = re.sub('[^A-Za-z]', '', alignment[0]['sequence']).upper()
    ip = load('InterPro-' + accession + '.json')['results']
    domains = sorted({x['metadata']['accession'] for x in ip})
    lineage = set(target['organism']['lineage'] + [target['organism']['scientificName'], 'Homo'])
    rule = load('ARBA00026330.json')
    matching_sets = []
    for index, condition_set in enumerate(rule['mainRule']['conditionSets']):
        satisfied = []
        for condition in condition_set['conditions']:
            values = {x['value'] for x in condition['conditionValues']}
            if condition['type'] == 'InterPro id':
                match = bool(values.intersection(domains))
            elif condition['type'] == 'taxon':
                match = bool(values.intersection(lineage))
            else:
                match = False
            satisfied.append(not match if condition.get('isNegative') else match)
        if all(satisfied):
            matching_sets.append({'index': index, 'condition_set': condition_set})
    structures = []
    for entry in load('RCSB-Q15029-structures.json')['data']['entries']:
        for entity in entry.get('polymer_entities') or []:
            identifiers = entity['rcsb_polymer_entity_container_identifiers']
            references = identifiers.get('reference_sequence_identifiers') or []
            if not any(x['database_name'] == 'UniProt' and x['database_accession'] == accession for x in references):
                continue
            deposited = entity['entity_poly']['pdbx_seq_one_letter_code_can']
            structures.append({'pdb': entry['rcsb_id'], 'entity': entity['rcsb_id'], 'title': entry['struct']['title'], 'citation': entry['rcsb_primary_citation'], 'chains': identifiers['auth_asym_ids'], 'organisms': entity.get('rcsb_entity_source_organism', []), 'deposited_sequence_length': len(deposited), 'deposited_reference_sequence_equals_canonical': deposited == sequence})
    terms = {r['id']: r for name in ['GO-original-terms.json', 'GO-stage-RNA.json', 'GO-binding-terms.json', 'GO-class-additional.json'] for r in load(name)['results']}
    stage_contexts = []
    for index in config['stage_rows']:
        source = config['source_annotations'][index]
        pmid = int(source['original_reference_id'].split(':')[1])
        stage_contexts.append({'row': index, 'source': source, 'original_definition': terms[source['term']['id']], 'source_models': [x for x in structures if x['citation'].get('pdbx_database_id_PubMed') == pmid]})
    interactions = []
    mitab = data['IntAct-Q15029.mitab'].decode().splitlines()
    for index, source in enumerate(config['source_annotations']):
        if source['term']['id'] != 'GO:0005515':
            continue
        partners = {x.replace('UniProtKB:', 'uniprotkb:') for x in source.get('supporting_entities', []) if x.startswith('UniProtKB:')}
        hits = []
        for line_number, line in enumerate(mitab):
            cells = line.split('\t')
            if len(cells) < 42:
                continue
            ids = {cells[0].split('-')[0], cells[1].split('-')[0]}
            if 'uniprotkb:' + accession in ids and ids.intersection(partners) and source['original_reference_id'].replace('PMID:', 'pubmed:') in cells[8].split('|'):
                hits.append({'line': line_number, 'id_a': cells[0], 'id_b': cells[1], 'method': cells[6], 'publication': cells[8], 'taxon_a': cells[9], 'taxon_b': cells[10], 'type': cells[11], 'interaction_id': cells[13], 'expansion': cells[15], 'role_a': cells[18], 'role_b': cells[19], 'host': cells[28], 'negative': cells[35], 'feature_a': cells[36], 'feature_b': cells[37]})
        interactions.append({'row': index, 'source': source, 'records': hits})
    nodes = {int(name[9:-5]): load(name) for name in data if name.startswith('Reactome-') and name.endswith('.json')}
    target_entities = {key for key, node in nodes.items() if node.get('referenceEntity', {}).get('identifier') == config['reactome_reference']}
    edges = ['input', 'output', 'hasComponent', 'hasMember', 'hasCandidate', 'physicalEntity', 'catalystActivity']
    def paths(node_id, trail):
        if node_id in target_entities:
            return [trail]
        results = []
        node = nodes.get(node_id, {})
        visited = {x['id'] for x in trail}
        for edge in edges:
            children = node.get(edge, [])
            for child in children if isinstance(children, list) else [children]:
                if not isinstance(child, dict) or child.get('dbId') not in nodes or child['dbId'] in visited:
                    continue
                results.extend(paths(child['dbId'], trail + [{'id': child['dbId'], 'edge': edge}]))
        return results
    reactome = []
    for root_id in config['reactome_roots']:
        root_node = nodes[root_id]
        reactome.append({'root_id': root_id, 'name': root_node['displayName'], 'compartment': root_node.get('compartment'), 'paths': paths(root_id, [{'id': root_id}])})
    return {'target': {'accession': accession, 'length': len(sequence), 'organism': target['organism']}, 'paint': {'nodes': node_count, 'path': target_paths[0], 'literal_assertions': assertions, 'msa_exact_canonical': ungapped == sequence}, 'interpro': domains, 'arba': {'matching_sets': matching_sets, 'annotations': rule['mainRule']['annotations']}, 'structures': structures, 'stage_contexts': stage_contexts, 'interactions': interactions, 'reactome': reactome}

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--inputs', type=Path, default=HERE / 'inputs.tar.gz')
    parser.add_argument('--output', type=Path, help='Write derived JSON here; default prints JSON to stdout.')
    parser.add_argument('--check', action='store_true', help='Compare recomputed objects with the shipped results without writing.')
    args = parser.parse_args()
    data = read_inputs(args.inputs)
    result = project(data, json.loads((HERE / 'config.json').read_text()))
    if args.check:
        require(result == json.loads((HERE / 'results.json').read_text()), 'Recomputed results differ')
        print(json.dumps({'status': 'PASS', 'inputs': len(data), 'sources': len(json.loads((HERE / 'config.json').read_text())['source_annotations']), 'structures': len(result['structures']), 'binding_rows': len(result['interactions']), 'literal_interaction_records': sum(len(x['records']) for x in result['interactions']), 'reactome_roots': len(result['reactome']), 'reactome_paths': sum(len(x['paths']) for x in result['reactome'])}))
    elif args.output:
        args.output.write_text(json.dumps(result, indent=2, ensure_ascii=False) + '\n')
    else:
        print(json.dumps(result, indent=2, ensure_ascii=False))

if __name__ == '__main__':
    main()
