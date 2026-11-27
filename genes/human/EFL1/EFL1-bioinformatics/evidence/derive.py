"""Reconstruct EFL1 provenance from immutable provider records; no verdict inference."""
from pathlib import Path
import argparse, hashlib, json, re

def require(value, message):
    if not value:
        raise ValueError(message)

def derive(raw, sources, official):
    J = lambda p: json.loads(p.read_text())
    tree = J(raw / 'PTHR42908-tree.json')['search']
    root = tree['tree_topology']['annotation_node']
    paths = {}
    nodes = {}

    def walk(n, path):
        pid = n['persistent_id']
        require(pid not in nodes, 'Duplicate node ' + pid)
        nodes[pid] = n
        paths[pid] = path + [pid]
        children = n.get('children', {}).get('annotation_node', [])
        for child in [children] if isinstance(children, dict) else children:
            walk(child, paths[pid])
    walk(root, [])
    target = [n for n in nodes.values() if 'UniProtKB=' + official['primaryAccession'] in n.get('node_name', '').split('|')]
    require(len(target) == 1, 'Target leaf cardinality')
    target = target[0]
    tid = target['persistent_id']
    path = paths[tid]
    msa = J(raw / 'PTHR42908-familymsa.json')['search']['MSA_list']['sequence_info']
    match = [r for r in msa if r['persistent_id'] == tid]
    require(len(match) == 1, 'MSA target cardinality')
    aligned = match[0]['sequence']
    ungapped = aligned.replace('.', '').replace('-', '').upper()
    require(ungapped == official['sequence']['value'], 'MSA target exact sequence')
    ibd = []
    for line_number, line in enumerate((raw / 'IBD.gaf').read_text().splitlines()):
        if line.startswith('!'):
            continue
        columns = line.split('\t')
        if len(columns) > 8 and columns[1] in path:
            ibd.append({'line': line_number, 'node': columns[1], 'qualifier': columns[3], 'go_id': columns[4], 'evidence': columns[6], 'with_from': columns[7].split('|'), 'date': columns[13], 'raw': line})
    iba = []
    for i, s in enumerate(sources):
        if s['evidence_type'] != 'IBA':
            continue
        source_nodes = [e.split(':', 1)[1] for e in s['supporting_entities'] if e.startswith('PANTHER:')]
        require(len(source_nodes) == 1, 'IBA node')
        node = source_nodes[0]
        direct = [x for x in ibd if x['node'] == node and x['go_id'] == s['term']['id'] and (x['evidence'] == 'IBD')]
        require(len(direct) == 1, 'IBD correspondence')
        row = direct[0]
        donors = [e for e in s['supporting_entities'] if not e.startswith('PANTHER:')]
        require(set(donors) == set(row['with_from']), 'Donor set correspondence')
        iba.append({'source_row': i, 'source_node': node, 'term': s['term'], 'target_descends_from_node': node in path, 'literal_ibd': row, 'self_donor': 'UniProtKB:' + official['primaryAccession'] in donors, 'path_loss_records_for_same_term': [x for x in ibd if x['go_id'] == s['term']['id'] and x['qualifier'] == 'NOT']})
    donor_map = J(raw.parent / 'donor-query-map.json')
    mapped = J(raw.parent / 'donor-mapped-query.json')
    donors = []
    experimental = {'EXP', 'IDA', 'IPI', 'IMP', 'IGI', 'IEP', 'HTP', 'HDA', 'HMP', 'HGI', 'HEP'}
    for record in donor_map:
        d = record['id']
        mapping = next((m for m in mapped if m['literal'] == d), None)
        if mapping:
            acc = mapping['accession']
            u = J(raw / f'UniProt-{acc}.json')
            db, key = d.split(':', 1)
            db = {'FB': 'FlyBase'}.get(db, db)
            require(any((x['database'] == db and x['id'] == key for x in u['uniProtKBCrossReferences'])), 'Literal donor identity ' + d)
            p = raw / f'QuickGO-{acc}.json'
        else:
            acc = d.split(':', 1)[1]
            p = raw.parent / record['path']
        q = J(p)
        require(q['numberOfHits'] == len(q['results']), 'Donor result pagination ' + d)
        donors.append({'literal_source_id': d, 'mapped_accession': acc, 'tree_mapping': mapping, 'current_records_path': str(p.relative_to(raw.parent)), 'matching_current_donor_records': q['results'], 'direct_experimental_records': [x for x in q['results'] if x['goEvidence'] in experimental], 'scope': 'Current donor-record evidence; no donor original-body read is implied. Combined UniProt entries may encode more than one source gene.'})
    funfam = {x['id'] for x in official['uniProtKBCrossReferences'] if x['database'] == 'FunFam'}
    interpro = J(raw / 'InterPro-Q7Z2Z2.json')
    ipr = {x['metadata']['accession']: x for x in interpro['results']}
    rules = []
    for rule in ['ARBA00026818', 'ARBA00085698']:
        r = J(raw / (rule + '.json'))
        matched = []
        for index, cs in enumerate(r['mainRule']['conditionSets']):
            checks = []
            for condition in cs['conditions']:
                typ = condition['type']
                values = condition['conditionValues']
                present = None
                if typ == 'FunFam id':
                    present = all((v['value'] in funfam for v in values))
                if typ == 'InterPro id':
                    present = all((v['value'] in ipr for v in values))
                if typ == 'taxon':
                    present = all((v['value'] in official['organism']['lineage'] or v['value'] == official['organism']['scientificName'] for v in values))
                checks.append({'condition': condition, 'matched': present})
            if all((x['matched'] is True for x in checks)):
                matched.append({'index': index, 'conditions': checks})
        require(matched, 'ARBA sufficient condition ' + rule)
        rules.append({'rule_id': rule, 'matched_alternatives': matched, 'annotations': r['mainRule']['annotations'], 'scope': 'Matches sufficient current rule alternatives, not every alternative; preserved imported source dictionaries remain unchanged.'})
    pairs = []
    raw_lines = (raw / 'IntAct-Q7Z2Z2.mitab').read_text().splitlines()
    for i, line in enumerate(raw_lines):
        c = line.split('\t')
        if len(c) < 42:
            continue
        ids = {c[0].split('-')[0], c[1].split('-')[0]}
        if {'uniprotkb:Q7Z2Z2', 'uniprotkb:Q9Y3A5'} <= ids:
            pairs.append({'raw_line': i, 'id_a': c[0], 'id_b': c[1], 'method': c[6], 'publication': c[8], 'taxon_a': c[9], 'taxon_b': c[10], 'type': c[11], 'stable_id': c[13], 'expansion': c[15], 'experimental_role_a': c[18], 'experimental_role_b': c[19], 'host': c[28], 'negative': c[35], 'feature_a': c[36], 'feature_b': c[37], 'all_fields': c})
    require(len(pairs) == 2, 'Current exact pair count')
    return {'target': {'accession': official['primaryAccession'], 'leaf': tid, 'node': {k: v for k, v in target.items() if k != 'children'}, 'family': tree['parameters']['family'], 'family_version': tree['product']['version'], 'tree_node_count': len(nodes), 'path': [{'id': pid, 'species': nodes[pid].get('species'), 'event_type': nodes[pid].get('event_type')} for pid in path], 'msa_columns': len(aligned), 'ungapped_length': len(ungapped), 'ungapped_sha256': hashlib.sha256(ungapped.encode()).hexdigest(), 'exact_official_sequence': True}, 'iba': iba, 'other_path_ibd_ird_records': ibd, 'donors': donors, 'interpro_target_matches': list(ipr.values()), 'rules': rules, 'interactions': {'raw_total': len(raw_lines), 'pairs': pairs, 'unrecovered_source_PMIDs': ['25991726'], 'scope': 'Current literal IntAct export has 2018 direct-interaction and 2024 proximity records. A missing 2015 export record does not negate the independently read direct experiment.'}}
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--raw', type=Path, required=True)
    parser.add_argument('--sources', type=Path, required=True)
    parser.add_argument('--uniprot', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    result = derive(args.raw, json.loads(args.sources.read_text()), json.loads(args.uniprot.read_text()))
    args.output.write_text(json.dumps(result, indent=2, ensure_ascii=False) + '\n')
    print(json.dumps({'tree_nodes': result['target']['tree_node_count'], 'source_IBA': len(result['iba']), 'donors': len(result['donors']), 'rules': len(result['rules']), 'pairs': len(result['interactions']['pairs']), 'exact_sequence_length': result['target']['ungapped_length']}))
