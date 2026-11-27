#!/usr/bin/env python3
"""Reproduce EDAR source-table and annotation provenance from hash-pinned saved inputs."""
from pathlib import Path
import argparse, json, hashlib, csv, re, base64, math
import openpyxl
ap = argparse.ArgumentParser()
ap.add_argument('--input-map', type=Path, required=True)
ap.add_argument('--manifest', type=Path, default=Path(__file__).with_name('source-manifest.json'))
ap.add_argument('--output', type=Path, required=True)
args = ap.parse_args()
manifest = json.loads(args.manifest.read_text())
mapping = json.loads(args.input_map.read_text())
paths = {}
for key, record in manifest['inputs'].items():
    p = Path(mapping[key]).expanduser()
    p = p if p.is_absolute() else args.input_map.parent / p
    if not p.is_file():
        raise ValueError(key)
    if not hashlib.sha256(p.read_bytes()).hexdigest() == record['sha256']:
        raise ValueError(f'Changed input: {key}')
    paths[key] = p
J = lambda k: json.loads(paths[k].read_text())
seqs = {a: J('UniProt-' + a)['sequence']['value'] for a in ['Q9UNE0', 'Q92838', 'Q8NHL6']}
library = []
pairs = []
spr = []
totals = {}
for n in [1, 4, 5]:
    wb = openpyxl.load_workbook(paths['32822567-S' + str(n)], read_only=True, data_only=True)
    for sh in wb:
        rows = list(sh.iter_rows(values_only=True))
        totals[f'S{n}:{sh.title}'] = {'physical_rows': len(rows), 'data_rows': len(rows) - 1}
        for line, row in enumerate(rows[1:], 2):
            if n == 1 and row[2] in seqs:
                a = row[2]
                full = row[6]
                ecd = row[12]
                start, end = row[10:12]
                if not (full == seqs[a] and ecd == full[start - 1:end] and (len(ecd) == row[13])):
                    raise ValueError('Saved-source integrity check failed')
                library.append({'excel_row': line, 'accession': a, 'gene': row[3], 'full_length': len(full), 'sequence_sha256': hashlib.sha256(full.encode()).hexdigest(), 'current_reference_exact': True, 'ECD_start': start, 'ECD_end': end, 'ECD_length': len(ecd), 'ECD_sequence_sha256': hashlib.sha256(ecd.encode()).hexdigest()})
            if n in [4, 5] and any((str(x) in ['EDAR', 'Q9UNE0'] for x in row)):
                rec = {'sheet': sh.title, 'excel_row': line, 'headers': list(rows[0]), 'fields': list(row)}
                (pairs if n == 4 else spr).append(rec)
                if n == 4:
                    ratios = [row[6 + i] / row[9 + i] for i in range(3)]
                    if not all((math.isclose(a, b, rel_tol=1e-12) for a, b in zip(ratios, row[12:15]))):
                        raise ValueError('Saved-source integrity check failed')
                    if not math.isclose(sum(ratios) / 3, row[15], rel_tol=1e-12):
                        raise ValueError('Saved-source integrity check failed')
raw = list(csv.reader(paths['IntAct'].open(), delimiter='\t'))
interactions = []
for line, row in enumerate(raw, 1):
    if 'pubmed:11035039' not in row[8]:
        continue
    matches = []
    for side in [0, 1]:
        a = row[side].removeprefix('uniprotkb:')
        if a in seqs:
            rogid = base64.b64encode(hashlib.sha1(seqs[a].encode()).digest()).decode().rstrip('=') + '9606'
            matches.append({'accession': a, 'reference_ROGID_matches': 'rogid:' + rogid in row[32 + side]})
    interactions.append({'physical_line': line, 'fields': row, 'sequence_checks': matches})
root = J('PANTHER-tree')['search']['tree_topology']['annotation_node']
nodes = {}
nodepaths = {}

def visit(n, path):
    k = n['persistent_id']
    nodes[k] = n
    nodepaths[k] = path + [k]
    cs = n.get('children', {}).get('annotation_node', [])
    for c in [cs] if isinstance(cs, dict) else cs:
        visit(c, nodepaths[k])
visit(root, [])
targets = [k for k, v in nodes.items() if v.get('node_name', '').endswith('UniProtKB=Q9UNE0')]
if not len(targets) == 1:
    raise ValueError('Saved-source integrity check failed')
tid = targets[0]
msa = J('PANTHER-MSA')['search']['MSA_list']['sequence_info']
aligned = next((x['sequence'] for x in msa if x['persistent_id'] == tid))
if not re.sub('[^A-Za-z]', '', aligned).upper() == seqs['Q9UNE0']:
    raise ValueError('Saved-source integrity check failed')
ibds = []
for line, text in enumerate(paths['IBD'].read_text().splitlines(), 1):
    if text.startswith('!'):
        continue
    f = text.split('\t')
    if len(f) > 6 and f[1] in nodes:
        ibds.append({'line': line, 'fields': f, 'on_target_path': f[1] in nodepaths[tid]})
donors = {}
for a in ['Q9R187', 'Q9HAV5']:
    d = J('QuickGO-' + a)
    if not len(d['results']) == d['numberOfHits']:
        raise ValueError('Saved-source integrity check failed')
    donors[a] = {'total_annotations': d['numberOfHits'], 'selected_annotations': [{k: r.get(k) for k in ['id', 'geneProductId', 'goId', 'qualifier', 'reference', 'goEvidence', 'evidenceCode', 'assignedBy', 'withFrom']} for r in d['results'] if r['goId'] in ['GO:0004888', 'GO:0005886', 'GO:0019221', 'GO:0045177']]}
u = J('UniProt-Q9UNE0')
funfams = {x['id'] for x in u['uniProtKBCrossReferences'] if x['database'] == 'FunFam'}
arba = []
for rid in ['ARBA00027254', 'ARBA00028236', 'ARBA00084990']:
    d = J(rid)
    matches = []
    for i, c in enumerate(d['mainRule']['conditionSets']):
        fs = {v['value'] for x in c['conditions'] if x['type'] == 'FunFam id' for v in x['conditionValues']}
        if fs and fs <= funfams:
            matches.append({'zero_based_condition_set': i, 'conditions': c['conditions']})
    arba.append({'id': rid, 'condition_sets': len(d['mainRule']['conditionSets']), 'matching_sets': matches, 'annotations': d['mainRule']['annotations']})
rs = {k: J('Reactome-' + k) for k in ['R-HSA-5669012', 'R-HSA-5675656', '5669001', '5674596', '5675675']}
chains = []

def walk(k, path):
    d = rs.get(str(k))
    if not d:
        return
    if d.get('referenceEntity', {}).get('identifier') == 'Q9UNE0':
        chains.append({'path': path + [str(k)], 'accession': 'Q9UNE0', 'start': d['startCoordinate'], 'end': d['endCoordinate'], 'compartments': [c['accession'] for c in d['compartment']]})
        return
    for field in ['input', 'output', 'hasComponent']:
        for x in d.get(field, []):
            walk(x['dbId'], path + [str(k), field])
for k in ['R-HSA-5669012', 'R-HSA-5675656']:
    walk(k, [])
out = {'inputs_verified': len(paths), 'ECIA': {'sheet_counts': totals, 'library_sequence_checks': library, 'all_EDAR_incident_rows': pairs, 'EDAR_SPR_rows': spr}, 'IntAct': {'all_records': len(raw), 'selected_source_records': interactions}, 'PAINT': {'nodes': len(nodes), 'MSA_sequences': len(msa), 'target': tid, 'target_path': nodepaths[tid], 'target_sequence_exact': True, 'literal_family_assertions': ibds, 'donors': donors}, 'ARBA': {'official_target_funfams': sorted(funfams), 'official_target_lineage': u['organism']['lineage'], 'rules': arba}, 'InterPro': {'id': 'IPR047526', 'name': J('InterPro')['metadata']['name'], 'GO_mappings': J('InterPro')['metadata']['go_terms']}, 'Reactome': {'target_chains': chains}}
args.output.write_text(json.dumps(out, indent=2) + '\n')
print(json.dumps({'status': 'PASS', 'inputs': len(paths), 'ECIA_rows': len(pairs), 'EDAR_SPR_rows': len(spr), 'library_sequences': len(library), 'IntAct_total': len(raw), 'selected_IntAct': len(interactions), 'PAINT_nodes': len(nodes), 'IBDs': len(ibds), 'Reactome_paths': len(chains)}))
