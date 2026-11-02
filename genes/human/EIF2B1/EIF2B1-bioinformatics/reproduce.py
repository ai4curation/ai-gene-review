#!/usr/bin/env python3
"""Replay EIF2B1 source identities from frozen database responses, offline."""
import argparse
import base64
import csv
import hashlib
import io
import json
from pathlib import Path
import re
import zipfile

HERE = Path(__file__).resolve().parent
# PSI-MITAB 2.7 zero-based columns. Reference checksums are not insert sequences.
PARTICIPANT_A, PARTICIPANT_B = 0, 1
METHOD, REFERENCE, TAXON_A, TAXON_B = 6, 8, 9, 10
INTERACTION_TYPE, INTERACTION_ID = 11, 13
COMMENT, HOST = 27, 28
CHECKSUM_A, CHECKSUM_B, NEGATIVE = 32, 33, 35
FEATURE_A, FEATURE_B = 36, 37


def require(condition, message):
    if not condition:
        raise ValueError(message)


def sha(data):
    return hashlib.sha256(data).hexdigest()


def rogid(sequence, taxon):
    return base64.b64encode(hashlib.sha1(sequence.encode()).digest()).decode().rstrip('=') + str(taxon)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--manifest', type=Path, default=HERE / 'source-manifest.json')
    parser.add_argument('--archive', type=Path, default=HERE / 'source-inputs.zip')
    parser.add_argument('--inputs-dir', type=Path, help='Use an extracted, hash-checked input directory instead')
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    manifest = json.loads(args.manifest.read_text())
    raw = {}
    if args.inputs_dir:
        for item in manifest['inputs']:
            raw[item['name']] = (args.inputs_dir / item['name']).read_bytes()
    else:
        require(sha(args.archive.read_bytes()) == manifest['archive']['sha256'], 'Archive hash changed')
        with zipfile.ZipFile(args.archive) as archive:
            require(set(archive.namelist()) == {x['name'] for x in manifest['inputs']}, 'Archive member set changed')
            raw = {name: archive.read(name) for name in archive.namelist()}
    for item in manifest['inputs']:
        require(sha(raw[item['name']]) == item['sha256'], 'Input hash changed: ' + item['name'])
        require(len(raw[item['name']]) == item['bytes'], 'Input size changed: ' + item['name'])
    def load(name):
        return json.loads(raw[name])
    sources = load('source-objects.json')
    official = {load(item['name'])['primaryAccession']: load(item['name'])
                for item in manifest['inputs'] if item['kind'] == 'UniProt'}
    target = official['Q14232']
    sequences = {acc: {'sequence': item['sequence']['value'], 'taxon': item['organism']['taxonId']}
                 for acc, item in official.items()}
    for item in sequences.values():
        item['ROGID'] = rogid(item['sequence'], item['taxon'])

    root = load('PTHR45860-tree.json')['search']['tree_topology']['annotation_node']
    nodes, ancestry = {}, {}
    def visit(node, parents):
        ident = node['persistent_id']
        require(ident not in nodes, 'Repeated PAINT node')
        nodes[ident], ancestry[ident] = node, parents + [ident]
        children = node.get('children', {}).get('annotation_node', [])
        if isinstance(children, dict):
            children = [children]
        for child in children:
            visit(child, parents + [ident])
    visit(root, [])
    targets = [x for x in nodes.values() if x.get('node_name', '').endswith('UniProtKB=Q14232')]
    require(len(targets) == 1, 'Nonunique PAINT target')
    leaf = targets[0]
    msa = load('PTHR45860-msa.json')['search']['MSA_list']['sequence_info']
    matches = [x for x in msa if x['persistent_id'] == leaf['persistent_id']]
    require(len(matches) == 1, 'Nonunique target alignment')
    sequence = re.sub('[^A-Za-z]', '', matches[0]['sequence']).upper()
    require(sequence == sequences['Q14232']['sequence'], 'Target alignment sequence mismatch')
    propagated_nodes = {x.split(':', 1)[1] for source in sources if source['evidence_type'] == 'IBA'
                        for x in source.get('supporting_entities', []) if x.startswith('PANTHER:PTN')}
    ibds = []
    for line, text in enumerate(raw['IBD.gaf'].decode().splitlines(), 1):
        fields = text.split('\t')
        if len(fields) > 6 and fields[1] in propagated_nodes:
            require(fields[1] in ancestry[leaf['persistent_id']], 'IBD node outside target ancestry')
            ibds.append({'physical_line': line, 'fields': fields})
    require({x['fields'][1] for x in ibds} == propagated_nodes, 'Missing literal IBD premise')
    donor = load('Q64270-QuickGO-page1.json')
    require(donor['numberOfHits'] == len(donor['results']), 'Incomplete donor query')

    records = []
    for line, fields in enumerate(csv.reader(io.StringIO(raw['IntAct-Q14232.tsv'].decode()), delimiter='\t'), 1):
        if not fields or fields[0].startswith('#'):
            continue
        require(len(fields) >= 42, 'Truncated MITAB record at line ' + str(line))
        records.append({'physical_line': line, 'fields': fields})
    joins, occurrences = [], []
    for index, source in enumerate(sources):
        if source['term']['id'] not in {'GO:0005515', 'GO:0042802'}:
            continue
        wanted = {x.split(':', 1)[1] for x in source.get('supporting_entities', []) if x.startswith('UniProtKB:')}
        if source['term']['id'] == 'GO:0042802':
            wanted = {'Q14232'}
        ref = source['original_reference_id'].replace('PMID:', 'pubmed:')
        selected = []
        for record in records:
            fields = record['fields']
            pair = [fields[i].split(':', 1)[-1] for i in [PARTICIPANT_A, PARTICIPANT_B]]
            if ref not in fields[REFERENCE].split('|') or 'Q14232' not in pair:
                continue
            partner = pair[1] if pair[0] == 'Q14232' else pair[0]
            if wanted and partner not in wanted:
                continue
            selected.append({**record, 'method': fields[METHOD], 'taxa': fields[TAXON_A:TAXON_B + 1],
                             'interaction_type': fields[INTERACTION_TYPE], 'interaction_id': fields[INTERACTION_ID],
                             'host': fields[HOST], 'negative': fields[NEGATIVE],
                             'assayed_features': fields[FEATURE_A:FEATURE_B + 1]})
            for side, acc in enumerate(pair):
                require(acc in sequences, 'No official reference sequence: ' + acc)
                checksums = [x.split(':', 1)[1] for x in fields[CHECKSUM_A + side].split('|') if x.startswith('rogid:')]
                expected = sequences[acc]['ROGID']
                occurrences.append({'source_index': index, 'physical_line': record['physical_line'], 'side': side,
                                    'accession': acc, 'reference_checksums': checksums, 'computed_ROGID': expected,
                                    'matches': expected in checksums, 'assayed_feature': fields[FEATURE_A + side],
                                    'negative': fields[NEGATIVE]})
        joins.append({'source_index': index, 'source': source, 'expected_partners': sorted(wanted), 'records': selected})
    # Sequence comparison is kept separate from biochemical classification.
    variant, canonical = sequences['Q7KZS0']['sequence'], sequences['P63279']['sequence']
    prefix = 0
    for aa, bb in zip(variant, canonical):
        if aa != bb:
            break
        prefix += 1

    graph = {str(n): load(f'Reactome-{n}.json') for n in [72670, 72722, 72526, 72528, 72529, 72517]}
    def edge(start, predicate, end):
        values = graph[str(start)][predicate]
        if not isinstance(values, list):
            values = [values]
        require(end in [x['dbId'] for x in values], f'Missing Reactome edge {start}:{predicate}:{end}')
        return {'from': start, 'predicate': predicate, 'to': end}
    chains = [{'source_index': 28, 'edges': [edge(72670, 'input', 72526), edge(72526, 'hasComponent', 72517)]},
              {'source_index': 29, 'edges': [edge(72722, 'catalystActivity', 72528), edge(72528, 'physicalEntity', 72526), edge(72526, 'hasComponent', 72517)]},
              {'source_index': 29, 'input_edges': [edge(72722, 'input', 72529), edge(72529, 'hasComponent', 72526), edge(72526, 'hasComponent', 72517)]}]
    entity = graph['72517']
    require(entity['referenceEntity']['identifier'] == 'Q14232', 'Wrong Reactome target')
    require(str(entity['species']['taxId']) == '9606', 'Wrong Reactome species')
    require(entity['compartment'][0]['accession'] == '0005829', 'Target cytosol annotation missing')

    features = {x['featureId']: x for x in target['features'] if x['type'] == 'Alternative sequence'}
    natural_products = []
    for comment in target['comments']:
        if comment['commentType'] != 'ALTERNATIVE PRODUCTS':
            continue
        for isoform in comment['isoforms']:
            acc = isoform['isoformIds'][0]
            seq = sequences['Q14232']['sequence']
            variants = sorted([features[x] for x in isoform.get('sequenceIds', [])], key=lambda x: x['location']['start']['value'], reverse=True)
            for feature in variants:
                a, b = feature['location']['start']['value'] - 1, feature['location']['end']['value']
                change = feature['alternativeSequence']
                require(not change.get('originalSequence') or seq[a:b] == change['originalSequence'], 'Alternative-product reference mismatch')
                seq = seq[:a] + change.get('alternativeSequences', [''])[0] + seq[b:]
            fasta_seq = ''.join(raw[acc + '.fasta'].decode().splitlines()[1:])
            require(seq == fasta_seq, 'Alternative-product FASTA mismatch')
            natural_products.append({'id': acc, 'length': len(seq), 'sequence_sha256': sha(seq.encode()), 'sequence_ids': isoform.get('sequenceIds', [])})

    closures = {x['id']: x['ancestors'] for x in load('GO-refinement-ancestors.json')['results']}
    refinements = []
    for item in load('refinement-selection.json'):
        old = sources[item['source_index']]['term']['id']
        new = item['replacement_id']
        require(old in closures[new], f'Original term {old} not ancestor of {new}')
        refinements.append({**item, 'original_id': old, 'original_in_typed_ancestry': True})
    result = {'source_count': len(sources), 'natural_products': natural_products,
              'paint': {'tree_nodes': len(nodes), 'target': leaf, 'target_path': ancestry[leaf['persistent_id']],
                        'sequence_length': len(sequence), 'literal_IBDs': ibds, 'rat_donor_rows': donor['results']},
              'interactions': {'total_captured_records': len(records), 'joins': joins, 'sequence_occurrences': occurrences,
                               'matching_reference_checksums': sum(x['matches'] for x in occurrences),
                               'UBE2I_comparison': {'variant': 'Q7KZS0', 'canonical': 'P63279', 'common_prefix': prefix,
                                                   'variant_length': len(variant), 'canonical_length': len(canonical),
                                                   'variant_tail': variant[prefix:], 'canonical_tail': canonical[prefix:]}},
              'reactome': {'chains': chains, 'target': {k: entity[k] for k in ['dbId', 'stId', 'startCoordinate', 'endCoordinate', 'compartment', 'species', 'referenceEntity']}},
              'refinement_ancestry': refinements,
              'scope': 'Source-derived identities and relationships, not automated functional verdicts. Curated reference checksums do not authenticate experimental inserts.'}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    require(not args.output.exists(), 'Refusing to overwrite output')
    args.output.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({'status': 'PASS', 'sources': len(sources), 'products': len(natural_products), 'tree_nodes': len(nodes),
                      'IBDs': len(ibds), 'IntAct_records': len(records), 'joins': len(joins), 'sequence_occurrences': len(occurrences),
                      'sequence_matches': sum(x['matches'] for x in occurrences), 'refinements': len(refinements), 'output_sha256': sha(args.output.read_bytes())}))


if __name__ == '__main__':
    main()
