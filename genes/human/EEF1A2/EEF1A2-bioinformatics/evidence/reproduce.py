"""Reproduce source joins from checksum-verified inputs using the standard library."""
import argparse
import base64
import hashlib
import json
import re
import tarfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
TARGET = 'Q05639'
BINDING_TERMS = {'GO:0005515', 'GO:0019901'}
DONOR_FILES = {'QuickGO-P62631.json', 'QuickGO-Q71V39.json', 'QuickGO-P68104.json'}
MITAB_ID_A, MITAB_ID_B = 0, 1
MITAB_METHOD, MITAB_PUBLICATION = 6, 8
MITAB_TAXON_A, MITAB_TAXON_B = 9, 10
MITAB_INTERACTION_TYPE, MITAB_IDENTIFIERS = 11, 13
MITAB_EXPANSION = 15
MITAB_ROLES_START, MITAB_ROLES_STOP = 16, 20
MITAB_ROGID_A, MITAB_ROGID_B = 32, 33
MITAB_NEGATIVE, MITAB_FEATURE_A, MITAB_FEATURE_B = 35, 36, 37
MINIMUM_MITAB_COLUMNS = MITAB_FEATURE_B + 1
GAF_NODE, GAF_TERM, GAF_EVIDENCE = 1, 4, 6


def require(condition, message):
    if not condition:
        raise ValueError(message)


def load_inputs(input_dir=None):
    manifest = json.loads((HERE / 'input-manifest.json').read_text())
    contents = {}
    if input_dir is not None:
        for item in manifest['inputs']:
            path = input_dir / item['name']
            require(path.is_file(), f'Missing saved input: {path}')
            contents[item['name']] = path.read_bytes()
    else:
        archive = HERE / manifest['archive']['name']
        require(archive.is_file(), 'Missing raw-inputs.tar.gz; restore the bundle or pass --input-dir.')
        require(hashlib.sha256(archive.read_bytes()).hexdigest() == manifest['archive']['sha256'],
                'Raw archive checksum mismatch.')
        with tarfile.open(archive, 'r:gz') as handle:
            members = handle.getmembers()
            for item in manifest['inputs']:
                matches = [member for member in members if member.name == item['name']]
                require(len(matches) == 1 and matches[0].isfile(),
                        f'Missing, duplicated or non-file archive member: {item["name"]}')
                stream = handle.extractfile(matches[0])
                require(stream is not None, f'Cannot read archive member: {item["name"]}')
                contents[item['name']] = stream.read()
    for item in manifest['inputs']:
        require(hashlib.sha256(contents[item['name']]).hexdigest() == item['sha256'],
                f'Input checksum mismatch: {item["name"]}')
    return contents


def parse_records(data, comment_prefix, minimum_columns, label):
    records = []
    for physical_line, text in enumerate(data.decode().splitlines(), 1):
        if not text or text.startswith(comment_prefix):
            continue
        fields = text.split('\t')
        require(len(fields) >= minimum_columns,
                f'Malformed {label} record at physical line {physical_line}: {len(fields)} columns')
        records.append(fields)
    return records


def analyze(raw):
    def read(name):
        return json.loads(raw[name])

    source = read('source-contexts.json')
    nodes, paths = {}, {}

    def visit(node, path):
        if isinstance(node, list):
            for item in node:
                visit(item, path)
            return
        identifier = node['persistent_id']
        path = path + [identifier]
        require(identifier not in nodes, f'Duplicate tree node: {identifier}')
        nodes[identifier], paths[identifier] = node, path
        visit(node.get('children', {}).get('annotation_node', []), path)

    visit(read('PTHR23115-tree.json')['search']['tree_topology']['annotation_node'], [])
    leaves = [key for key, node in nodes.items() if f'UniProtKB={TARGET}' in node.get('node_name', '')]
    require(len(leaves) == 1, 'Target tree leaf is not unique')
    leaf = leaves[0]
    target_path = paths[leaf]
    msa = read('PTHR23115-familymsa.json')['search']['MSA_list']['sequence_info']
    sequences = {row['persistent_id']: row['sequence'] for row in msa}
    official = read(f'UniProt-{TARGET}.json')['sequence']['value']
    require(leaf in sequences, 'Target tree leaf is missing from the MSA')
    require(re.sub('[^A-Za-z]', '', sequences[leaf]).upper() == official,
            'Target MSA is not the official sequence')
    gaf = parse_records(raw['IBD.gaf'], '!', GAF_EVIDENCE + 1, 'GAF')
    imported_terms = {row['term']['id'] for row in source}
    effective = [row for row in gaf if row[GAF_NODE] in target_path
                 and row[GAF_EVIDENCE] == 'IBD' and row[GAF_TERM] in imported_terms]
    losses = [row for row in gaf if row[GAF_NODE] in target_path and row[GAF_EVIDENCE] in ['IRD', 'IKR']]
    paint = {'target_leaf': leaf, 'path': target_path, 'node_count': len(nodes),
             'msa_rows': len(msa), 'alignment_width': len(sequences[leaf]),
             'target_length': len(official), 'target_msa_exact': True,
             'effective_ibds': effective, 'loss_annotations_on_target_path': losses}
    records = parse_records(raw['IntAct-Q05639.mitab'], '#', MINIMUM_MITAB_COLUMNS, 'MITAB')

    def sequence_rogid(accession):
        record = read(f'UniProt-{accession}.json')
        sequence, taxon = record['sequence']['value'], record['organism']['taxonId']
        checksum = base64.b64encode(hashlib.sha1(sequence.encode()).digest()).decode().rstrip('=')
        return {'accession': accession, 'taxon': taxon, 'length': len(sequence),
                'sequence_sha256': hashlib.sha256(sequence.encode()).hexdigest(),
                'rogid': checksum + str(taxon)}

    pairs = []
    for index, annotation in enumerate(source):
        if annotation['term']['id'] not in BINDING_TERMS:
            continue
        partners = [value.split(':', 1)[1] for value in annotation.get('supporting_entities', [])
                    if value.startswith('UniProtKB:')]
        require(len(partners) == 1, f'Binding source row {index} does not identify one partner')
        partner = partners[0]
        pmid = annotation['original_reference_id'].split(':')[-1]
        selected = []
        for record_index, row in enumerate(records):
            if f'pubmed:{pmid}' not in row[MITAB_PUBLICATION].split('|'):
                continue
            if {row[MITAB_ID_A], row[MITAB_ID_B]} != {f'uniprotkb:{TARGET}', f'uniprotkb:{partner}'}:
                continue
            checks = []
            for id_column, rogid_column in [(MITAB_ID_A, MITAB_ROGID_A), (MITAB_ID_B, MITAB_ROGID_B)]:
                check = sequence_rogid(row[id_column].split(':', 1)[1])
                check['literal_rogid'] = row[rogid_column]
                check['matches'] = 'rogid:' + check['rogid'] in row[rogid_column].split('|')
                checks.append(check)
            identifiers = re.findall(r'EBI-\d+', row[MITAB_IDENTIFIERS])
            selected.append({
                'record_index_zero_based': record_index,
                'id_a': row[MITAB_ID_A], 'id_b': row[MITAB_ID_B],
                'method': row[MITAB_METHOD], 'publication': row[MITAB_PUBLICATION],
                'taxon_a': row[MITAB_TAXON_A], 'taxon_b': row[MITAB_TAXON_B],
                'interaction_type': row[MITAB_INTERACTION_TYPE], 'identifiers': row[MITAB_IDENTIFIERS],
                'public_urls': ['https://www.ebi.ac.uk/intact/interaction/' + value for value in identifiers],
                'expansion': row[MITAB_EXPANSION], 'roles': row[MITAB_ROLES_START:MITAB_ROLES_STOP],
                'negative': row[MITAB_NEGATIVE], 'feature_a': row[MITAB_FEATURE_A],
                'feature_b': row[MITAB_FEATURE_B], 'reference_sequence_checks': checks})
        pairs.append({'row': index, 'partner': partner, 'source': annotation['original_reference_id'],
                      'records': selected})

    graph = {key: value for item in read('40205054-apms-network.json') for key, value in item.items()}
    graph_nodes = {node['@id']: node for node in graph['nodes']}
    apms = []
    for edge in graph['edges']:
        names = {graph_nodes[edge['s']]['n'], graph_nodes[edge['t']]['n']}
        if names in [{'EEF1A2', 'TTLL12'}, {'EEF1A2', 'ABTB1'}]:
            apms.append({'edge': edge, 'source': graph_nodes[edge['s']], 'target': graph_nodes[edge['t']],
                         'attributes': [item for item in graph['edgeAttributes'] if item['po'] == edge['@id']]})
    donors = []
    for name in sorted(raw):
        if name not in DONOR_FILES:
            continue
        accession = name[8:-5]
        query, record = read(name), read(f'UniProt-{accession}.json')
        require(len(query['results']) == query['numberOfHits'], f'Incomplete donor query: {accession}')
        donor_leaves = [key for key, node in nodes.items()
                        if f'UniProtKB={accession}' in node.get('node_name', '')]
        donors.append({'accession': accession, 'organism': record['organism'], 'genes': record.get('genes'),
                       'matching_current_donor_records': [row for row in query['results'] if row['goId'] in imported_terms],
                       'alignment': [{'leaf': key,
                                      'sequence_exact': re.sub('[^A-Za-z]', '', sequences[key]).upper() == record['sequence']['value']}
                                     for key in donor_leaves if key in sequences]})
    partner_classes = []
    for accession in sorted({pair['partner'] for pair in pairs}):
        record = read(f'UniProt-{accession}.json')
        partner_classes.append({'accession': accession, 'organism': record['organism'],
                                'genes': record.get('genes'), 'sequence_length': len(record['sequence']['value']),
                                'classification_records': [item for item in record.get('comments', [])
                                                           if item['commentType'] in ['FUNCTION', 'CATALYTIC ACTIVITY', 'CAUTION', 'SIMILARITY']]})
    return {'target': TARGET, 'source_rows': len(source), 'paint': paint,
            'raw_intact_records': len(records), 'pairs': pairs, 'donors': donors,
            'partner_classes': partner_classes, 'apms_edges': apms,
            'scope': 'Database reference sequences, curated pair records and AP-MS coassociations; not experimental insert sequencing or proof of direct contact for every edge.'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--input-dir', type=Path)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    try:
        result = analyze(load_inputs(args.input_dir))
        args.output.write_text(json.dumps(result, indent=2, ensure_ascii=False) + '\n')
    except (OSError, ValueError, KeyError, tarfile.TarError) as error:
        parser.exit(1, f'ERROR: {error}\n')
    print('PASS: raw-derived source joins for', result['source_rows'], 'rows;',
          len(result['pairs']), 'binding contexts;', len(result['paint']['effective_ibds']), 'ancestral IBDs.')


if __name__ == '__main__':
    main()
