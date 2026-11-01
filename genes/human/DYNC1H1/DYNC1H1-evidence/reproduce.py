# /// script
# requires-python = ">=3.9"
# dependencies = ["PyYAML==6.0.3", "xlrd==2.0.2", "beautifulsoup4==4.14.3"]
# ///
"""Reproduce source records, measurements and graph paths without inferring verdicts.

Supply authenticated saved inputs with --input-map, or retrieve public URLs with
--download. Dynamic database responses may have changed; a hash mismatch stops the
run rather than silently substituting a newer source. PDF extraction needs pdftotext.
"""
import argparse
import csv
import hashlib
import io
import json
from pathlib import Path
import re
import subprocess
from urllib.request import Request, urlopen

from bs4 import BeautifulSoup
import xlrd
import yaml


def load_inputs(args, manifest):
    mapping = yaml.safe_load(args.input_map.read_text()) if args.input_map else {}
    resolved = {}
    for source in manifest['sources']:
        key = source['key']
        if key in mapping:
            path = Path(mapping[key]).expanduser()
        elif args.download:
            args.cache_dir.mkdir(parents=True, exist_ok=True)
            path = args.cache_dir / source['filename']
            if not path.exists():
                request = Request(source['url'], headers={'User-Agent': 'DYNC1H1-evidence-replay/1.0'})
                with urlopen(request, timeout=60) as response:
                    raw = response.read()
                if hashlib.sha256(raw).hexdigest() != source['sha256']:
                    raise ValueError(f'{key}: downloaded source differs from the recorded version')
                path.write_bytes(raw)
        else:
            raise ValueError(f'{key}: provide --input-map or explicitly select --download')
        raw = path.read_bytes()
        if hashlib.sha256(raw).hexdigest() != source['sha256'] or len(raw) != source['bytes']:
            raise ValueError(f'{key}: saved source hash/size mismatch')
        resolved[key] = path
    return resolved


def binding_records(inputs, selection):
    # Preserve reference-sequence checksums and separately recorded construct features.
    columns = {0:'id_a', 1:'id_b', 6:'method', 8:'publication', 9:'taxon_a', 10:'taxon_b',
               11:'interaction_type', 12:'source_db', 13:'interaction_id', 14:'score',
               15:'expansion', 18:'experimental_role_a', 19:'experimental_role_b',
               28:'host', 32:'checksum_a', 33:'checksum_b', 35:'negative',
               36:'feature_a', 37:'feature_b'}
    rows = {key:list(csv.reader(inputs[key].open(), delimiter='\t')) for key in ['intact','mint']}
    result = []
    for item in selection['binding_pairs']:
        matches = []
        for database, records in rows.items():
            for index, fields in enumerate(records):
                if len(fields) < 38:
                    raise ValueError(f'{database}: incomplete MITAB 2.7 record at line {index + 1}')
                if (set(fields[:2]) == {'uniprotkb:' + selection['target']['uniprot'], 'uniprotkb:' + item['partner']}
                        and 'pubmed:' + item['pmid'] in fields[8].split('|')):
                    matches.append({'database':database, 'physical_line_1based':index + 1,
                                    'fields':{name:fields[column] for column,name in columns.items()}})
        result.append(dict(item, records=matches))
    # Unmatched source rows remain visible, not classified as negative results.
    return {'source_record_counts':{k:len(v) for k,v in rows.items()}, 'pairs':result}


def measurements(inputs, selection):
    target = selection['target']
    result = []
    book = xlrd.open_workbook(str(inputs['rna-table']))
    for sheet in book.sheets():
        header = sheet.row_values(0)
        for index in range(1, sheet.nrows):
            row = sheet.row_values(index)
            if target['ensembl'] in row and target['symbol'] in row:
                result.append({'source':'PMID:22658674','sheet':sheet.name,'excel_row':index + 1,
                               'fields':dict(zip(header,row))})
    book = xlrd.open_workbook(str(inputs['parotid-table']))
    for sheet in book.sheets():
        header = sheet.row_values(0)
        if 'Gene' not in header:
            continue
        for index in range(1,sheet.nrows):
            row = sheet.row_values(index)
            if row[header.index('Gene')] == target['symbol']:
                names = ['LocusID','Description','Sequence Count','SpectrumCount','Sequence Coverage','Length','Gene']
                result.append({'source':'PMID:19199708','sheet':sheet.name,'excel_row':index + 1,
                               'fields':{name:row[header.index(name)] for name in names}})
    soup = BeautifulSoup(inputs['urinary-table'].read_bytes(), 'html.parser')
    for index, tr in enumerate(soup.find_all('tr')):
        cells = ['\n'.join(td.stripped_strings) for td in tr.find_all(['td','th'], recursive=False)]
        if len(cells) >= 8 and cells[1] == target['symbol']:
            result.append({'source':'PMID:19056867 author database','html_tr_zero_index':index,
                           'fields':{'protein_name':cells[0],'gene_name':cells[1],'peptide_count':cells[2],
                                     'refseq':cells[3],'reference_key':cells[7]},
                           'reference_key_scope':'2 = Gonzales et al. 2009 (PMID:19056867)'})
    data = list(csv.DictReader(inputs['opencell'].open()))
    for index, row in enumerate(data):
        if [row['target_gene_name'],row['interactor_gene_name']] in selection['opencell_pairs']:
            result.append({'source':'PMID:35271311 OpenCell','data_index_0based':index,
                           'physical_line_1based':index + 2,'fields':row})
    text = subprocess.run(['pdftotext','-layout',str(inputs['rna-thesis']),'-'],
                          check=True,capture_output=True,text=True).stdout
    for page, content in enumerate(text.split('\f'),1):
        pattern = r'^\s*(I{1,3})\s+' + re.escape(target['symbol']) + r'\s+((?:NA|-?\d+(?:\.\d+)?)\s+){4}(?:NA|-?\d+(?:\.\d+)?).*?$'
        for match in re.finditer(pattern, content, re.M):
            fields = match.group().split()
            result.append({'source':'PMID:22681889 author thesis','physical_pdf_page':page,
                           'group':fields[0],'gene':fields[1], 'numeric_columns_as_printed':fields[2:7],
                           'scope':'Supplementary Table 1 measurement row; group and five numeric columns retained without relabeling missing values.'})
    return {'target':target,'records':result}


def reactome_paths(inputs, selection):
    result = []
    for requested in selection['reactome_paths']:
        steps = []
        for step in requested['steps']:
            current = json.loads(inputs['reactome-' + str(step['from'])].read_text())
            children = current.get(step['edge'],[])
            if not isinstance(children,list):
                children = [children]
            ids = [child.get('dbId') if isinstance(child,dict) else child for child in children]
            if step['to'] not in ids:
                raise ValueError(f"Missing literal Reactome edge {step}")
            child = json.loads(inputs['reactome-' + str(step['to'])].read_text())
            steps.append(dict(step, name=child['displayName'], schema_class=child['schemaClass']))
        target = json.loads(inputs['reactome-' + str(steps[-1]['to'])].read_text())
        reference = target.get('referenceEntity',{})
        if reference.get('identifier') != selection['target']['uniprot']:
            raise ValueError('Reactome path did not terminate in the selected accession')
        result.append({'event':requested['event'],'steps':steps,'target_accession':reference['identifier'],
                       'start':target.get('startCoordinate'),'end':target.get('endCoordinate'),
                       'compartments':[x['displayName'] for x in target.get('compartment',[])],
                       'species':target.get('speciesName')})
    return {'paths':result,'scope':'Curated entity membership and compartment assignments; not independent localization experiments.'}


def phylogeny(inputs, selection):
    tree = json.loads(inputs['paint-tree'].read_text())
    msa = json.loads(inputs['paint-msa'].read_text())['search']['MSA_list']['sequence_info']
    nodes,parents = {},{}
    def walk(node,parent=None):
        key = node['persistent_id']; nodes[key] = node; parents[key] = parent
        children = node.get('children',{}).get('annotation_node',[])
        for child in ([children] if isinstance(children,dict) else children):
            walk(child,key)
    walk(tree['search']['tree_topology']['annotation_node'])
    target = selection['target']['uniprot']
    leaves = [key for key,node in nodes.items() if target in str({k:v for k,v in node.items() if k!='children'})]
    if len(leaves) != 1:
        raise ValueError('Target leaf is ambiguous or absent')
    leaf = leaves[0]; path = []; current = leaf
    while current:
        path.append(current); current = parents[current]
    path.reverse()
    sequence = re.sub('[^A-Za-z]','',next(x['sequence'] for x in msa if x['persistent_id']==leaf)).upper()
    official = json.loads(inputs['target-uniprot'].read_text())['sequence']['value']
    if sequence != official:
        raise ValueError('Target MSA sequence differs from the official reference')
    ibd = []
    for number,line in enumerate(inputs['paint-ibd'].read_text().splitlines(),1):
        fields = line.split('\t')
        if len(fields)>8 and fields[1] in path and fields[6] in ['IBD','IRD']:
            ibd.append({'line_1based':number,'fields':fields})
    joins = []
    for claim in selection['paint_claims']:
        matches = [row for row in ibd if row['fields'][1]==claim['node'] and row['fields'][4]==claim['term'] and row['fields'][6]=='IBD']
        if claim['node'] not in path or not matches:
            raise ValueError(f'Literal IBD/descent not established for {claim}')
        joins.append(dict(claim, literal_ibd=matches, target_descent=True))
    return {'family':'PTHR10676','tree_nodes':len(nodes),'msa_sequences':len(msa),'target_leaf':leaf,
            'target_path':path,'sequence_length':len(sequence),'sequence_sha256':hashlib.sha256(sequence.encode()).hexdigest(),
            'source_joins':joins,'target_path_ird':[row for row in ibd if row['fields'][6]=='IRD'],
            'scope':'Node placement and descent authenticate propagation; donor count and target self-grounding are not failure modes.'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--manifest',type=Path,default=Path(__file__).with_name('source-manifest.yaml'))
    parser.add_argument('--selection',type=Path,default=Path(__file__).with_name('selection.yaml'))
    parser.add_argument('--input-map',type=Path)
    parser.add_argument('--download',action='store_true')
    parser.add_argument('--cache-dir',type=Path,default=Path('source-downloads'))
    parser.add_argument('--output-dir',type=Path,required=True)
    args = parser.parse_args()
    manifest = yaml.safe_load(args.manifest.read_text()); selection = yaml.safe_load(args.selection.read_text())
    inputs = load_inputs(args,manifest)
    outputs = {'interactions.yaml':binding_records(inputs,selection),'measurements.yaml':measurements(inputs,selection),
               'reactome-paths.yaml':reactome_paths(inputs,selection),'phylogeny.yaml':phylogeny(inputs,selection)}
    args.output_dir.mkdir(parents=True,exist_ok=True)
    for name,data in outputs.items():
        (args.output_dir/name).write_text(yaml.safe_dump(data,sort_keys=False,allow_unicode=True))
    print(json.dumps({'authenticated_sources':len(inputs),'binding_pairs':len(outputs['interactions.yaml']['pairs']),
                      'measurement_records':len(outputs['measurements.yaml']['records']),
                      'reactome_paths':len(outputs['reactome-paths.yaml']['paths']),
                      'paint_joins':len(outputs['phylogeny.yaml']['source_joins'])}))


if __name__ == '__main__':
    main()
