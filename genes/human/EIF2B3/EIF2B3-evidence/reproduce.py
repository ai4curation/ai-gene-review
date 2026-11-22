"""Reconstruct bounded source projections from the preserved official responses."""
from pathlib import Path
import hashlib
import json
import re
import argparse
from html.parser import HTMLParser

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--input-dir', required=True, type=Path)
parser.add_argument('--output', required=True, type=Path)
args = parser.parse_args()
E = args.input_dir
J = lambda p: json.loads(p.read_text())
manifest = J(Path(__file__).with_name('inputs.json'))
for item in manifest['inputs']:
    path = E / item['name']
    if not path.is_file():
        raise ValueError('Missing required saved input: ' + item['name'])
    if path.stat().st_size != item['bytes'] or hashlib.sha256(path.read_bytes()).hexdigest() != item['sha256']:
        raise ValueError('Input hash or size mismatch: ' + item['name'])
u = J(E / 'UniProt-Q9NR50.json')
tree = J(E / 'PTHR45989-treeinfo.json')['search']['tree_topology']['annotation_node']
nodes = []

def walk(value, path):
    if isinstance(value, dict):
        current = path + [value['persistent_id']] if 'persistent_id' in value else path
        if 'persistent_id' in value:
            nodes.append((current, value))
        for child in value.values():
            if isinstance(child, (dict, list)):
                walk(child, current)
    elif isinstance(value, list):
        for child in value:
            walk(child, path)

walk(tree, [])
target_path, target = next((p, n) for p, n in nodes if n.get('tree_node_type') == 'LEAF' and 'UniProtKB=Q9NR50' in n.get('node_name', ''))
msa = J(E / 'PTHR45989-familymsa.json')['search']['MSA_list']['sequence_info']
seq = next(n['sequence'] for n in msa if n['persistent_id'] == target['persistent_id'])
seq = re.sub(r'[.\-]', '', seq).upper()
if not (seq == u['sequence']['value']):
    raise ValueError('Source consistency check failed: ' + "seq == u['sequence']['value']")
ibd_path = E / 'IBD.gaf'
ibds = []
for number, line in enumerate(ibd_path.read_text().splitlines(), 1):
    cols = line.split('\t')
    if len(cols) >= 15 and cols[1] in target_path:
        ibds.append({'line': number, 'fields': cols})
paint = dict(nodes=len(nodes), sequences=len(msa), target=target['node_name'], target_node=target['persistent_id'],
             path=target_path, sequence_length=len(seq), sequence_sha256=hashlib.sha256(seq.encode()).hexdigest(),
             ibd_file='IBD.gaf', ibd_sha256=hashlib.sha256(ibd_path.read_bytes()).hexdigest(), path_records=ibds)
actual = {db: {r['id'] for r in u['uniProtKBCrossReferences'] if r['database'] == db} for db in ['InterPro', 'PANTHER', 'FunFam']}
actual['taxon'] = set(u['organism']['lineage'] + [u['organism']['scientificName']])
rules = {}
for name in ['ARBA00028188', 'ARBA00088579', 'ARBA00027100', 'ARBA00026561']:
    rule = J(E / (name + '.json'))['mainRule']
    matches = []
    for i, condition_set in enumerate(rule['conditionSets']):
        proof = []
        for condition in condition_set['conditions']:
            kind = condition['type'].replace(' id', '')
            if kind not in actual:
                raise ValueError('Unimplemented condition type: ' + kind)
            values = [v['value'] for v in condition['conditionValues']]
            satisfied = bool(set(values) & actual[kind])
            if condition.get('isNegative'):
                satisfied = not satisfied
            proof.append(dict(type=kind, values=values, satisfied=satisfied))
        if all(p['satisfied'] for p in proof):
            matches.append(dict(index=i, conditions=proof))
    rules[name] = dict(matches=matches, annotations=rule['annotations'])
donors = {}
for name in ['P70541', 'P56288', 'P09032']:
    filename = 'QuickGO-P70541-page1.json' if name == 'P70541' else 'QuickGO-' + name + '.json'
    source = J(E / filename)
    if not (source['numberOfHits'] == len(source['results'])):
        raise ValueError('Source consistency check failed: ' + "source['numberOfHits'] == len(source['results'])")
    donors[name] = dict(total=source['numberOfHits'], selected=[r for r in source['results'] if r['goId'] in
                       ['GO:0009408', 'GO:0009749', 'GO:0043434', 'GO:0002183', 'GO:0005085', 'GO:0005851', 'GO:0003743']])
shared = E
r72670 = J(shared / 'Reactome-72670.json')
r72722 = J(shared / 'Reactome-72722.json')
complex_ = J(shared / 'Reactome-72526.json')
gamma = J(E / 'Reactome-72525.json')
if not (any(r['dbId'] == 72526 for r in r72670['input'])):
    raise ValueError('Source consistency check failed: ' + "any(r['dbId'] == 72526 for r in r72670['input'])")
if not (any(r['dbId'] == 72526 for r in r72722['output'])):
    raise ValueError('Source consistency check failed: ' + "any(r['dbId'] == 72526 for r in r72722['output'])")
if not (any(r['dbId'] == 72525 for r in complex_['hasComponent'])):
    raise ValueError('Source consistency check failed: ' + "any(r['dbId'] == 72525 for r in complex_['hasComponent'])")
if not (gamma['referenceEntity']['identifier'] == 'Q9NR50'):
    raise ValueError('Source consistency check failed: ' + "gamma['referenceEntity']['identifier'] == 'Q9NR50'")
if not (gamma['compartment'][0]['accession'] == '0005829'):
    raise ValueError('Source consistency check failed: ' + "gamma['compartment'][0]['accession'] == '0005829'")
reactome = dict(paths=[['72670', 'input', '72526', 'hasComponent', '72525', 'referenceEntity', 'Q9NR50'],
                      ['72722', 'output', '72526', 'hasComponent', '72525', 'referenceEntity', 'Q9NR50']],
                compartment='GO:0005829', species=gamma['speciesName'], interval=[gamma['startCoordinate'], gamma['endCoordinate']])
class VisibleText(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ignore = 0
        self.parts = []
    def handle_starttag(self, tag, attrs):
        if tag in ('script', 'style'):
            self.ignore += 1
    def handle_endtag(self, tag):
        if tag in ('script', 'style') and self.ignore:
            self.ignore -= 1
    def handle_data(self, data):
        if not self.ignore and data.strip():
            self.parts.append(data.strip())
reader = VisibleText()
reader.feed((E / 'HPA-ENSG00000070785-subcellular.html').read_text())
html = ' '.join(reader.parts)
anchor = 'Localized to the Vesicles (supported), Cytosol (supported)'
if not (anchor in html):
    raise ValueError('Source consistency check failed: ' + 'anchor in html')
if 'HPA024219' not in html:
    raise ValueError('The selected antibody identifier is absent')
start = html.index(anchor)
hpa = dict(url='https://www.proteinatlas.org/ENSG00000070785-EIF2B3/subcellular',
           location_summary=html[start:start + len(anchor)],
           cell_lines=[x for x in ['A-431', 'U-251MG', 'U2OS'] if x in html],
           antibody='HPA024219', interpretation='The human cytosol location itself is supported; image pixels were not inspected.')
result = dict(paint=paint, rules=rules, donors=donors, reactome=reactome, hpa=hpa)
destination = args.output
destination.write_text(json.dumps(result, indent=2, ensure_ascii=False) + '\n')
print(json.dumps(dict(paint_nodes=len(nodes), msa=len(msa), target_length=len(seq), path_records=len(ibds),
                      rules={k: [m['index'] for m in v['matches']] for k, v in rules.items()},
                      donor_counts={k: v['total'] for k, v in donors.items()}, reactome_paths=2, hpa_cytosol='supported')))
