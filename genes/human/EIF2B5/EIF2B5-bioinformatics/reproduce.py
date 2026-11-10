"""Replay literal database joins from a hash-checked local archive (Python 3.10+)."""
import argparse
import base64
import csv
import hashlib
import io
import json
from pathlib import Path, PurePosixPath
from html.parser import HTMLParser
import re
import zipfile


def require(ok, message):
    if not ok:
        raise ValueError(message)


def load_inputs(folder):
    manifest = json.loads((folder / 'inputs.json').read_text())
    archive_name = PurePosixPath(manifest['archive']['path'])
    require(len(archive_name.parts) == 1 and not archive_name.is_absolute(), 'Archive must be local to inputs directory')
    require(hashlib.sha256((folder / 'config.json').read_bytes()).hexdigest() == manifest['configuration_sha256'], 'Configuration SHA256 mismatch')
    archive = folder / manifest['archive']['path']
    require(archive.is_file(), 'Missing local input archive: ' + str(archive))
    require(hashlib.sha256(archive.read_bytes()).hexdigest() == manifest['archive']['sha256'], 'Archive SHA256 mismatch')
    records = manifest['members']
    names = [r['member'] for r in records]
    require(len(set(names)) == len(names), 'Duplicate manifest members')
    data = {}
    with zipfile.ZipFile(archive) as z:
        require(len(z.namelist()) == len(set(z.namelist())) and set(z.namelist()) == set(names), 'Unexpected or duplicate archive members')
        require(sum(x.file_size for x in z.infolist()) < 100 * 1024**2, 'Archive exceeds bounded uncompressed size')
        for r in records:
            path = PurePosixPath(r['member'])
            require(not path.is_absolute() and '..' not in path.parts and '\\' not in r['member'], 'Unsafe archive name')
            b = z.read(r['member'])
            require(len(b) == r['bytes'] and hashlib.sha256(b).hexdigest() == r['sha256'], 'Member SHA256 mismatch: ' + r['member'])
            data[r['member']] = b
    return data


def derive(data, config):
    def obj(name):
        return json.loads(data[name])

    official = obj(config['official'])
    accession = official['primaryAccession']
    sequence = official['sequence']['value']
    sources = obj(config['sources'])
    raw_goa = list(csv.DictReader(io.StringIO(data[config['goa']].decode()), delimiter='\t'))

    def source_key(r):
        return (r['term']['id'], r['evidence_type'], r['original_reference_id'], r.get('qualifier', ''), tuple(sorted(r.get('supporting_entities', []))), r.get('negated', False), r.get('isoform'))

    def raw_key(r):
        qualifiers = r['QUALIFIER'].split('|')
        relation = [q for q in qualifiers if q != 'NOT']
        product = r['GENE PRODUCT ID']
        return (r['GO TERM'], r['GO EVIDENCE CODE'], r['REFERENCE'], relation[0] if relation else '', tuple(sorted(set(r['WITH/FROM'].split('|')) - {''})), 'NOT' in qualifiers, product if '-' in product else None)

    raw_keys = [raw_key(r) for r in raw_goa]
    require(len(raw_keys) == len(set(raw_keys)), 'Ambiguous raw GOA context')
    require(set(raw_keys) == {source_key(r) for r in sources}, 'GOA/source contexts differ')
    joins = [{'source_index': i, 'raw_index': raw_keys.index(source_key(s))} for i, s in enumerate(sources)]

    tree = obj(config['tree'])['search']['tree_topology']['annotation_node']
    nodes, paths = {}, {}

    def visit(n, ancestors):
        key = n['persistent_id']
        require(key not in nodes, 'Duplicate tree node')
        nodes[key], paths[key] = n, ancestors + [key]
        children = n.get('children', {}).get('annotation_node', [])
        for child in ([children] if isinstance(children, dict) else children):
            visit(child, paths[key])

    visit(tree, [])
    leaves = [n for n in nodes.values() if n.get('node_name', '').endswith('UniProtKB=' + accession)]
    require(len(leaves) == 1, 'Nonunique target leaf')
    target = leaves[0]
    alignment = obj(config['msa'])['search']['MSA_list']['sequence_info']
    target_sequences = [s for s in alignment if s['persistent_id'] == target['persistent_id']]
    require(len(target_sequences) == 1, 'Nonunique aligned target')
    aligned = re.sub('[^A-Za-z]', '', target_sequences[0]['sequence']).upper()
    require(aligned == sequence, 'Aligned target sequence differs from official record')
    ibds = []
    for r in obj(config['ibd_extract'])['records']:
        fields = r['line'].rstrip('\n').split('\t')
        require(fields[1] in paths[target['persistent_id']], 'IBD node outside target lineage')
        ibds.append({'original_physical_line': r['physical_line'], 'fields': fields})

    records = []
    for line, fields in enumerate(csv.reader(io.StringIO(data[config['intact']].decode()), delimiter='\t'), 1):
        if not fields or fields[0].startswith('#'):
            continue
        require(len(fields) >= 42, 'Truncated MITAB record')
        records.append({'physical_line': line, 'fields': fields})
    interactions = []
    for i, s in enumerate(sources):
        if s['term']['id'] not in config['binding_terms']:
            continue
        expected = {x.split(':', 1)[1] for x in s.get('supporting_entities', []) if x.startswith('UniProtKB:')}
        selected = []
        for r in records:
            f = r['fields']
            if s['original_reference_id'].replace('PMID:', 'pubmed:') not in f[8].split('|'):
                continue
            ids = [x.split(':', 1)[-1] for x in f[:2]]
            if accession not in ids:
                continue
            partner = ids[1] if ids[0] == accession else ids[0]
            if expected and partner not in expected:
                continue
            selected.append(r)
        interactions.append({'source_index': i, 'partners_expected': sorted(expected), 'records': selected})
    partners = []
    for name in config['partner_records']:
        u = obj(name)
        seq = u['sequence']['value']
        partners.append({'accession': u['primaryAccession'], 'taxon': u['organism']['taxonId'], 'length': len(seq), 'reference_ROGID': base64.b64encode(hashlib.sha1(seq.encode()).digest()).decode().rstrip('=') + str(u['organism']['taxonId']), 'functions': [c for c in u.get('comments', []) if c['commentType'] == 'FUNCTION']})

    xrefs = {x['id'] for x in official['uniProtKBCrossReferences']}
    lineage = set(official['organism']['lineage'] + [official['organism']['scientificName']])
    rules = []
    for name in config['rules']:
        rule = obj(name)
        matches = []
        for i, condition_set in enumerate(rule['mainRule']['conditionSets']):
            satisfied = []
            for condition in condition_set['conditions']:
                require(not condition['isNegative'], 'Unsupported negative ARBA condition')
                values = [x['value'] for x in condition['conditionValues']]
                if condition['type'] == 'taxon':
                    satisfied.append(any(v in lineage for v in values))
                elif condition['type'] in ['InterPro id', 'PANTHER id', 'FunFam id']:
                    satisfied.append(any(v in xrefs for v in values))
                else:
                    raise ValueError('Unsupported ARBA predicate: ' + condition['type'])
            if all(satisfied):
                matches.append({'condition_set_index': i, 'conditions': condition_set['conditions']})
        rules.append({'input': name, 'matching_condition_sets': matches, 'annotations': rule['mainRule']['annotations']})

    donors = []
    for name in config['donors']:
        d = obj(name)
        require(d['numberOfHits'] == len(d['results']), 'Incomplete QuickGO donor response')
        donors.append({'input': name, 'total_records': len(d['results']), 'matching_current_donor_records': [r for r in d['results'] if r['goId'] in config['donor_terms']]})
    nodes = {str(obj(n)['dbId']): obj(n) for n in config['reactome']}
    edges = []
    for node_id, n in nodes.items():
        for relation in ['input', 'output', 'hasComponent', 'catalystActivity', 'physicalEntity']:
            values = n.get(relation, [])
            for value in ([values] if isinstance(values, dict) else values):
                if str(value.get('dbId')) in nodes:
                    edges.append({'from': node_id, 'relation': relation, 'to': str(value['dbId'])})
    targets = [key for key, n in nodes.items() if n.get('referenceEntity', {}).get('identifier') == accession]
    require(len(targets) == 1, 'Nonunique Reactome target')
    target_id = targets[0]
    target_entity = nodes[target_id]
    require(target_entity['startCoordinate'] == config.get('reactome_target_start', 1) and target_entity['endCoordinate'] == len(sequence), 'Reactome target sequence span mismatch')
    paths_out = []

    def walk(node, path, seen):
        if node == target_id:
            paths_out.append(path)
            return
        for edge in edges:
            if edge['from'] == node and edge['to'] not in seen:
                walk(edge['to'], path + [edge], seen | {edge['to']})

    for root in config['reactome_roots']:
        walk(str(root), [], {str(root)})
    require({p[0]['from'] for p in paths_out} == set(map(str, config['reactome_roots'])), 'Missing root-to-target pathway')
    result = {'identity': {'accession': accession, 'length': len(sequence), 'sequence_sha256': hashlib.sha256(sequence.encode()).hexdigest()}, 'goa': {'rows': len(raw_goa), 'joins': joins}, 'paint': {'tree_nodes': len(paths), 'target': target, 'target_path': paths[target['persistent_id']], 'aligned_length': len(aligned), 'literal_IBDs': ibds}, 'interactions': {'all_records': len(records), 'source_joins': interactions, 'partner_classes': partners}, 'propagation': {'rules': rules, 'donors': donors}, 'reactome': {'target': target_entity, 'edges': edges, 'paths': paths_out}}

    if config.get('hpa'):
        parser = LocationTableParser()
        parser.feed(data[config['hpa']].decode())
        scores = []
        text = ' '.join(parser.all_text)
        for location, score in re.findall(r'Localized to the\s+([A-Za-z ]+?)\s*\((enhanced|supported|approved|uncertain)\)', text, re.I):
            item = {'location': location.strip(), 'reliability': score.lower()}
            if item not in scores:
                scores.append(item)
        require(scores and parser.rows, 'HPA location scores or assay rows not found')
        result['localization'] = {'location_specific_scores': scores, 'cell_line_rows': parser.rows, 'uniprot_location_record': obj(config['uniprot_location']), 'figure_pixels_inspected': False}
    return result


class LocationTableParser(HTMLParser):
    """Extract table text, without interpreting images or aggregate reliability."""
    def __init__(self):
        super().__init__()
        self.cells = None
        self.cell = None
        self.rows = []
        self.all_text = []

    def handle_starttag(self, tag, attrs):
        if tag == 'tr':
            self.cells = []
        elif tag in ('td', 'th') and self.cells is not None:
            self.cell = []

    def handle_data(self, text):
        normalized = ' '.join(text.split())
        if normalized:
            self.all_text.append(normalized)
            if self.cell is not None:
                self.cell.append(normalized)

    def handle_endtag(self, tag):
        if tag in ('td', 'th') and self.cell is not None:
            if self.cells is not None:
                self.cells.append(' '.join(self.cell))
            self.cell = None
        elif tag == 'tr' and self.cells is not None:
            cells = self.cells
            if len(cells) == 7 and re.fullmatch(r'HPA\d+', cells[1]):
                self.rows.append({'antibody': cells[1], 'cell_line': cells[2], 'RNA_nTPM': cells[3], 'location': cells[4], 'single_cell_variation': cells[5], 'cell_cycle_variation': cells[6]})
            self.cells = None



def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--inputs', type=Path, default=Path(__file__).resolve().parent)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    require(not args.output.exists(), 'Refuse to overwrite output')
    data = load_inputs(args.inputs)
    config = json.loads((args.inputs / 'config.json').read_text())
    result = derive(data, config)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({'status': 'PASS', 'target': result['identity'], 'source_rows': result['goa']['rows'], 'tree_nodes': result['paint']['tree_nodes'], 'IBDs': len(result['paint']['literal_IBDs']), 'interaction_records': result['interactions']['all_records'], 'binding_sources': len(result['interactions']['source_joins']), 'reactome_paths': len(result['reactome']['paths'])}))


if __name__ == '__main__':
    main()
