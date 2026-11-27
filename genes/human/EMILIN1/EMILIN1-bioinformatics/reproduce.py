#!/usr/bin/env python3
"""Offline, standard-library replay of saved EMILIN1 database and tabular data.

No network calls, environment installation, article-body parsing or biological
verdict generation. Input hashes are checked before any reconstruction.
"""
import argparse
import csv
import hashlib
import io
import json
from pathlib import Path, PurePosixPath
import re
import xml.etree.ElementTree as ET
import zipfile

HERE = Path(__file__).resolve().parent
TOKEN = re.compile(r'(?<![A-Za-z0-9])(?:EMILIN1|EMILIN-1|Q9Y6C2(?:-\d+)?)(?![A-Za-z0-9])', re.I)
NS = {'s': 'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}

def sha(data):
    return hashlib.sha256(data).hexdigest()

def require(condition, message):
    if not condition:
        raise ValueError(message)

class Inputs:
    def __init__(self):
        self.manifest = json.loads((HERE / 'input-manifest.json').read_text())
        self.archive = zipfile.ZipFile(HERE / 'inputs.zip')
        expected = {r['member'] for r in self.manifest['files']}
        require(set(self.archive.namelist()) == expected, 'Archive membership drift')
        for row in self.manifest['files']:
            data = self.archive.read(row['member'])
            require(len(data) == row['bytes'] and sha(data) == row['sha256'], 'Input drift: ' + row['member'])
    def data(self, name):
        return self.archive.read(name)
    def text(self, name):
        return self.data(name).decode('utf-8-sig')
    def json(self, name):
        return json.loads(self.data(name))


def workbook_targets(data, protein_reports_only=False):
    """Read XLSX cached values directly; do not evaluate formulas or infer peptides."""
    results = []
    with zipfile.ZipFile(io.BytesIO(data)) as archive:
        strings = []
        if 'xl/sharedStrings.xml' in archive.namelist():
            for item in ET.fromstring(archive.read('xl/sharedStrings.xml')).findall('s:si', NS):
                strings.append(''.join(node.text or '' for node in item.iter('{'+NS['s']+'}t')))
        rels = {r.attrib['Id']: r.attrib['Target'] for r in ET.fromstring(archive.read('xl/_rels/workbook.xml.rels'))}
        sheets = ET.fromstring(archive.read('xl/workbook.xml')).findall('s:sheets/s:sheet', NS)
        for sheet in sheets:
            title = sheet.attrib['name']
            if protein_reports_only and title != '(A) Protein Report':
                continue
            rid = sheet.attrib['{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id']
            target = rels[rid]
            member = target.lstrip('/') if target.startswith('/') else str(PurePosixPath('xl') / target)
            headers, hits = [], []
            for row in ET.fromstring(archive.read(member)).findall('s:sheetData/s:row', NS):
                cells = {}
                for cell in row.findall('s:c', NS):
                    value = cell.find('s:v', NS)
                    kind = cell.get('t')
                    if kind == 'inlineStr':
                        text = ''.join(t.text or '' for t in cell.findall('.//s:t', NS))
                    elif value is None:
                        continue
                    elif kind == 's':
                        text = strings[int(value.text)]
                    else:
                        text = value.text or ''
                    cells[cell.attrib['r']] = text
                n = int(row.attrib['r'])
                if n <= 8:
                    headers.append({'row': n, 'cells': cells})
                matches = {key: value for key, value in cells.items() if TOKEN.search(value)}
                if matches:
                    hits.append({'row': n, 'matched_cells': matches, 'cells': cells})
            results.append({'sheet': title, 'headers': headers, 'target_rows': hits})
    return results


def paint_projection(data, sources, official):
    root = data.json('database/PTHR15427-treeinfo.json')['search']['tree_topology']['annotation_node']
    nodes, paths = {}, {}
    def walk(node, ancestors):
        key = node['persistent_id']
        require(key not in nodes, 'Duplicate tree node')
        nodes[key] = node
        paths[key] = ancestors + [key]
        children = node.get('children', {}).get('annotation_node', [])
        for child in [children] if isinstance(children, dict) else children:
            walk(child, paths[key])
    walk(root, [])
    targets = [key for key, node in nodes.items() if node.get('node_name', '').endswith('UniProtKB=Q9Y6C2')]
    require(len(targets) == 1, 'Nonunique target')
    target = targets[0]
    msa = data.json('database/PTHR15427-familymsa.json')['search']['MSA_list']['sequence_info']
    sequences = [record for record in msa if record['persistent_id'] == target]
    require(len(sequences) == 1, 'Nonunique target MSA')
    sequence = re.sub('[^A-Za-z]', '', sequences[0]['sequence']).upper()
    require(sequence == official['sequence']['value'], 'Target sequence mismatch')
    path_records, ligand_records = [], []
    for line, text in enumerate(data.text('database/IBD.gaf').splitlines(), 1):
        fields = text.split('\t')
        if len(fields) <= 7:
            continue
        record = {'line': line, 'fields': fields}
        if fields[1] in paths[target]:
            path_records.append(record)
        if fields[4] == 'GO:0048018' and 'UniProtKB:Q9H8L6' in fields[7].split('|'):
            ligand_records.append({**record, 'on_target_path': fields[1] in paths[target]})
    joins = []
    for index, source in enumerate(sources):
        if source['evidence_type'] != 'IBA':
            continue
        ptns = [v.split(':', 1)[1] for v in source.get('supporting_entities', []) if v.startswith('PANTHER:PTN')]
        records = [r for r in path_records if r['fields'][1] in ptns and r['fields'][4] == source['term']['id'] and r['fields'][6] == 'IBD' and 'NOT' not in r['fields'][3]]
        donors = sorted({v for r in records for v in r['fields'][7].split('|')})
        imported = sorted(v for v in source.get('supporting_entities', []) if not v.startswith('PANTHER:PTN'))
        joins.append({'index': index, 'ptns': ptns, 'on_path': all(p in paths[target] for p in ptns), 'records': records, 'donors': donors, 'imported_donors': imported, 'exact_donor_match': donors == imported})
    return {'target': target, 'path': paths[target], 'length': len(sequence), 'sequence_exact': True, 'all_path_records': path_records, 'joins': joins, 'current_ligand_records': ligand_records}


def database_projection(data, official):
    values = {'InterPro id': set(), 'FunFam id': set(), 'taxon': set(official['organism']['lineage']) | {official['organism']['scientificName']}}
    for record in official['uniProtKBCrossReferences']:
        if record['database'] in ('InterPro', 'FunFam'):
            values[record['database']+' id'].add(record['id'])
    rule = data.json('database/ARBA00084594.json')
    conditions = []
    for index, group in enumerate(rule['mainRule']['conditionSets']):
        checks = []
        for condition in group['conditions']:
            present = any(v['value'] in values.get(condition['type'], set()) for v in condition['conditionValues'])
            checks.append(not present if condition.get('isNegative') else present)
        conditions.append({'index': index, 'condition_results': checks, 'satisfied': all(checks)})
    names = [n for n in data.archive.namelist() if n.startswith('database/Reactome-') and n.endswith('.json') and not n.endswith('.receipt.json')]
    entities = {str(data.json(n)['dbId']): data.json(n) for n in names}
    edges = []
    for key, entity in sorted(entities.items()):
        for relation in ('input', 'output', 'hasComponent', 'hasMember', 'hasCandidate', 'repeatedUnit', 'referenceEntity'):
            targets = entity.get(relation, [])
            for target in [targets] if isinstance(targets, dict) else targets:
                if isinstance(target, dict):
                    edges.append({'from': key, 'relation': relation, 'to': str(target['dbId'])})
                elif isinstance(target, int):
                    edges.append({'from': key, 'relation': relation, 'to': str(target)})
    donors = []
    for name in sorted(data.archive.namelist()):
        if re.fullmatch(r'database/QuickGO-[A-Z0-9]+-page1.json', name):
            export = data.json(name)
            require(len(export['results']) == export['numberOfHits'], 'Incomplete donor export')
            donors.append({'input': name, 'hits': export['numberOfHits'], 'records': export['results']})
    return {'rule_conditions': conditions, 'matching_sets': [r['index'] for r in conditions if r['satisfied']], 'reactome_edges': edges, 'donors': donors, 'complexes': [data.json('database/ComplexPortal-'+c+'-api.json') for c in ('CPX-438','CPX-421')]}


def interaction_projection(data, sources):
    records = list(csv.reader(io.StringIO(data.text('interactions/intact.tsv')), delimiter='\t'))
    matches = []
    for index in list(range(4,25)) + [71]:
        source = sources[index]
        pmid = source['original_reference_id'].split(':')[-1]
        partners = [v.split(':',1)[1] for v in source.get('supporting_entities',[]) if v.startswith('UniProtKB:')]
        partner = partners[0] if partners else 'Q9Y6C2'
        hits = []
        for line, fields in enumerate(records,1):
            if len(fields) < 36:
                continue
            if set(fields[:2]) == {'uniprotkb:Q9Y6C2','uniprotkb:'+partner} and 'pubmed:'+pmid in fields[8].split('|') and fields[35] == 'false':
                hits.append({'line':line,'accessions':fields[:2],'method':fields[6],'publication':fields[8],'record':fields[13],'negative':fields[35]})
        matches.append({'index':index,'partner':partner,'pmid':pmid,'intact_matches':hits})
    with zipfile.ZipFile(io.BytesIO(data.data('interactions/BioGRID.zip'))) as archive:
        names = [n for n in archive.namelist() if n.endswith('.txt')]
        require(len(names)==1,'BioGRID archive')
        records = list(csv.DictReader(io.StringIO(archive.read(names[0]).decode()),delimiter='\t'))
        biogrid = [r for r in records if r['Publication Source']=='PUBMED:21516116' and {r['Official Symbol Interactor A'],r['Official Symbol Interactor B']}=={'EMILIN1','MTMR9'}]
    bioplex = [{'line':i,'record':r} for i,r in enumerate(csv.DictReader(io.StringIO(data.text('interactions/BioPlex.tsv')),delimiter='\t'),2) if r['Bait Symbol']=='EMILIN1' and r['Prey Symbol']=='TAX1BP1']
    cx = data.json('interactions/NDEx.json')
    nodes = [n for aspect in cx for n in aspect.get('nodes',[]) if n.get('n')in('EMILIN1','LAIR2')]
    ids = {n['@id']for n in nodes}
    edges = [e for aspect in cx for e in aspect.get('edges',[]) if {e['s'],e['t']}==ids]
    return {'intact':matches,'biogrid':biogrid,'bioplex':bioplex,'ndex':{'nodes':nodes,'edges':edges}}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output',type=Path,required=True,help='New directory for reconstructed JSON outputs')
    args = parser.parse_args()
    require(not args.output.exists(), 'Preserve existing output directory')
    data = Inputs()
    sources = data.json('source/source-objects.json')
    raw = data.json('source/QuickGO.json')['results']
    tsv = list(csv.DictReader(io.StringIO(data.text('source/EMILIN1-goa.tsv')),delimiter='\t'))
    official = data.json('database/UniProt-Q9Y6C2.json')
    outputs = {'paint.json':paint_projection(data,sources,official),'database.json':database_projection(data,official),'interactions.json':interaction_projection(data,sources)}
    workbooks = {}
    for name in sorted(data.archive.namelist()):
        if name.startswith('tables/') and name.endswith('.xlsx'):
            workbooks[name] = workbook_targets(data.data(name), '23658023' in name)
    outputs['workbooks.json'] = workbooks
    columns = ['Protein IDs','Majority protein IDs','Gene names','Protein names','Unique peptides','Unique peptides Exp1','Unique peptides Exp2','Unique peptides Exp3','Sequence lengths','Intensity Exp1','Intensity Exp2','Intensity Exp3','Only identified by site','Reverse','Contaminant']
    groups = []
    for line,row in enumerate(csv.DictReader(io.StringIO(data.text('tables/23979707-proteinGroups.txt')),delimiter='\t'),2):
        if TOKEN.search(row.get('Gene names','')) or TOKEN.search(row.get('Protein IDs','')):
            groups.append({'line':line,'record':{key:row.get(key)for key in columns}})
    outputs['pride-target.json'] = groups
    summary = {'input_members':len(data.manifest['files']),'source_contexts':len(sources),'raw_contexts':len(raw),'normal_tsv_rows':len(tsv),'target_length':outputs['paint.json']['length'],'paint_source_joins':len(outputs['paint.json']['joins']),'paint_path_records':len(outputs['paint.json']['all_path_records']),'donor_exports':len(outputs['database.json']['donors']),'arba_matching_sets':outputs['database.json']['matching_sets'],'reactome_edges':len(outputs['database.json']['reactome_edges']),'intact_supported_source_rows':sum(bool(r['intact_matches'])for r in outputs['interactions.json']['intact']),'biogrid_targets':len(outputs['interactions.json']['biogrid']),'bioplex_targets':len(outputs['interactions.json']['bioplex']),'ndex_targets':len(outputs['interactions.json']['ndex']['edges']),'pride_target_groups':len(groups),'workbook_target_rows':{name:sum(len(s['target_rows'])for s in sheets)for name,sheets in workbooks.items()}}
    serialized = {name:(json.dumps(value,indent=2,ensure_ascii=False)+'\n').encode()for name,value in outputs.items()}
    result = {'summary':summary,'output_sha256':{name:sha(value)for name,value in serialized.items()}}
    expected = HERE/'expected-results.json'
    if expected.exists():
        require(result==json.loads(expected.read_text()),'Expected reconstruction changed')
    args.output.mkdir(parents=True)
    for name,value in serialized.items():
        (args.output/name).write_bytes(value)
    (args.output/'result.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'status':'PASS',**result},sort_keys=True))

if __name__ == '__main__':
    main()
