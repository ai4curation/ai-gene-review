#!/usr/bin/env python3
"""Reproduce EBF3 family placement and deposited-template identities (stdlib only)."""
import argparse
import hashlib
import json
import re
from pathlib import Path
from urllib.request import urlopen


def read_inputs(manifest, paths, download_dir):
    result = {}
    for name, record in manifest['inputs'].items():
        if paths is not None:
            path = Path(paths[name])
            content = path.read_bytes()
        else:
            path = download_dir / name
            if path.exists():
                content = path.read_bytes()
            else:
                with urlopen(record['url'], timeout=120) as response:
                    content = response.read()
                path.write_bytes(content)
        observed = hashlib.sha256(content).hexdigest()
        if observed != record['sha256']:
            raise ValueError(f'{name}: SHA256 mismatch: {observed}')
        result[name] = content.decode('utf-8')
    return result


def fasta(text):
    return ''.join(line.strip() for line in text.splitlines() if not line.startswith('>'))


def translation(text):
    match = re.search(r'/translation="([^"]+)"', text, re.S)
    if not match:
        raise ValueError('No deposited CDS translation found')
    parts = [line[5:].strip() if line.startswith('FT') else line.strip()
             for line in match.group(1).splitlines()]
    return re.sub(r'\s+', '', ''.join(parts))


def derive(raw, target):
    root = json.loads(raw['tree'])['search']['tree_topology']['annotation_node']
    nodes, paths, leaves = {}, {}, []

    def visit(node, ancestors):
        key = node['persistent_id']
        nodes[key] = node
        paths[key] = ancestors + [key]
        children = node.get('children', {}).get('annotation_node', [])
        if isinstance(children, dict):
            children = [children]
        if not children:
            leaves.append(node)
        for child in children:
            visit(child, paths[key])

    visit(root, [])
    matching = [n for n in leaves if 'UniProtKB=' + target in n.get('node_name', '').split('|')]
    if len(matching) != 1:
        raise ValueError(f'Expected one target leaf; found {len(matching)}')
    leaf = matching[0]
    sequences = json.loads(raw['msa'])['search']['MSA_list']['sequence_info']
    target_msa = next(x['sequence'] for x in sequences if x['persistent_id'] == leaf['persistent_id'])
    ungapped = re.sub('[^A-Za-z]', '', target_msa).upper()
    products = {'Q9H4W6-1': fasta(raw['long']), 'Q9H4W6-2': fasta(raw['short'])}
    events = []
    for line in raw['ibd'].splitlines():
        if not line or line.startswith('!'):
            continue
        fields = line.split('\t')
        if fields[1] in paths[leaf['persistent_id']]:
            events.append({'ancestor': fields[1], 'qualifier': fields[3], 'term': fields[4],
                           'reference': fields[5], 'evidence': fields[6],
                           'supporting_entities': fields[7].split('|'), 'date': fields[13]})
    clones = []
    for name in ['HQ258299', 'BC130479']:
        sequence = translation(raw[name])
        clones.append({'record': name, 'length': len(sequence),
                       'sequence_sha256': hashlib.sha256(sequence.encode()).hexdigest(),
                       'exact_product_matches': [key for key, value in products.items() if value == sequence]})
    return {'target_accession': target, 'target_leaf': leaf['persistent_id'],
            'tree_nodes': len(nodes), 'tree_leaves': len(leaves), 'msa_sequences': len(sequences),
            'target_path': paths[leaf['persistent_id']], 'target_msa_length': len(ungapped),
            'target_msa_matches_long': ungapped == products['Q9H4W6-1'],
            'product_lengths': {key: len(value) for key, value in products.items()},
            'lineage_events': events, 'deposited_templates': clones}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--manifest', type=Path, default=Path(__file__).with_name('sources.json'))
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--inputs', type=Path, help='JSON mapping of input keys to saved raw paths')
    group.add_argument('--download-dir', type=Path, help='Fetch public URLs or reuse files in this directory')
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    manifest = json.loads(args.manifest.read_text())
    paths = json.loads(args.inputs.read_text()) if args.inputs else None
    if args.download_dir:
        args.download_dir.mkdir(parents=True, exist_ok=True)
    raw = read_inputs(manifest, paths, args.download_dir)
    result = derive(raw, manifest['target_accession'])
    args.output.write_text(json.dumps(result, indent=2) + '\n')


if __name__ == '__main__':
    main()
