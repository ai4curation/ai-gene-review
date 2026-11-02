#!/usr/bin/env python3
"""Reproduce the DRC4 factual source projection from saved public inputs.

No network, credentials, curation decisions or database mutations are performed.
Input filenames and hashes are supplied in source-manifest.json. --input-map can
map those portable names to existing saved paths without copying large inputs.
"""
import argparse
import base64
import csv
import hashlib
import io
import json
from pathlib import Path
import re
import xml.etree.ElementTree as ET

def sha(data):
    return hashlib.sha256(data).hexdigest()

def rogid(sequence):
    return 'rogid:' + base64.b64encode(hashlib.sha1(sequence.encode()).digest()).decode().rstrip('=') + '9606'

def fasta(data):
    return ''.join(x.strip() for x in data.decode().splitlines() if not x.startswith('>'))

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    package = Path(__file__).resolve().parent
    parser.add_argument('--manifest', type=Path, default=package / 'source-manifest.json')
    parser.add_argument('--selection', type=Path, default=package / 'selection.json')
    parser.add_argument('--input-dir', type=Path)
    parser.add_argument('--input-map', type=Path)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    if args.input_dir is None and args.input_map is None:
        parser.error('Supply --input-dir or --input-map with genuine raw source paths')
    manifest = json.loads(args.manifest.read_text())
    mapping = json.loads(args.input_map.read_text()) if args.input_map else {}
    raw = {}
    for item in manifest['inputs']:
        name = item['name']
        path = Path(mapping[name]) if name in mapping else args.input_dir / name
        body = path.read_bytes()
        if sha(body) != item['sha256']:
            raise ValueError(f'Input checksum differs: {name}; use the pinned saved bytes, not an unqualified current response')
        raw[name] = body
    selection = json.loads(args.selection.read_text())
    seq = fasta(raw[selection['target_fasta']])
    target = selection['target']
    records = list(csv.reader(io.StringIO(raw['intact-O95995-tab27.tsv'].decode()), delimiter='\t'))
    official = {}
    for name in selection['uniprot_batches']:
        for entry in json.loads(raw[name])['results']:
            for acc in [entry['primaryAccession']] + entry.get('secondaryAccessions', []):
                official[acc] = entry
    projected = []
    for row in selection['binding_sources']:
        source = row['source']
        partner = source['supporting_entities'][0].split(':', 1)[1]
        entry = official[partner.split('-')[0]]
        partner_seq = fasta(raw[partner+'.fasta']) if '-' in partner else entry['sequence']['value']
        matches = []
        for line, fields in enumerate(records, 1):
            if 'pubmed:'+source['original_reference_id'].split(':')[1] not in fields[8].split('|'):
                continue
            for target_side in [0,1]:
                other = 1-target_side
                if fields[target_side] != 'uniprotkb:'+target or 'uniprotkb:'+partner not in fields[other].split('|')+fields[other+2].split('|'):
                    continue
                matches.append({'physical_line':line,'target_side':target_side,
                                'interactor_ids':fields[0:2], 'alternative_ids':fields[2:4],
                                'method':fields[6],'publication':fields[8], 'taxa':fields[9:11],
                                'interaction_type':fields[11], 'interaction_ids':fields[13],
                                'expansion':fields[15], 'roles':fields[16:20],
                                'checksums':fields[32:34], 'negative':fields[35], 'features':fields[36:38],
                                'target_parent_sequence_match':fields[32+target_side]==rogid(seq),
                                'partner_parent_sequence_match':fields[32+other]==rogid(partner_seq)})
        projected.append({'source_index':row['source_index'],'source':source,'partner':partner,
                          'primary_accession':entry['primaryAccession'],
                          'gene_names':[x['geneName']['value'] for x in entry.get('genes',[]) if 'geneName' in x],
                          'parent_sequence_length':len(partner_seq),'parent_sequence_sha256':sha(partner_seq.encode()),
                          'expected_parent_rogid':rogid(partner_seq),'records':matches})
    tree = json.loads(raw['PTHR31543-treeinfo.json'])['search']['tree_topology']['annotation_node']
    paths = {}
    def walk(node,path):
        path = path+[{'node':node.get('persistent_id'),'species':node.get('species',node.get('organism')),'event':node.get('event_type')}]
        if node.get('node_name'):
            paths[node['node_name']] = path
        children = node.get('children',{}).get('annotation_node',[])
        for child in children if isinstance(children,list) else [children]:
            walk(child,path)
    walk(tree,[])
    target_path = next(v for k,v in paths.items() if 'UniProtKB='+target in k)
    target_nodes = [x['node'] for x in target_path]
    gaf = [(i,row) for i,row in enumerate(csv.reader(io.StringIO(raw['IBD.gaf'].decode()),delimiter='\t'),1) if row and not row[0].startswith('!')]
    paint = []
    for row in selection['paint_sources']:
        source = row['source']; node = next(x.split(':',1)[1] for x in source['supporting_entities'] if x.startswith('PANTHER:PTN'))
        matches = [{'physical_line':line,'fields':fields} for line,fields in gaf if len(fields)>6 and fields[1]==node and fields[4]==source['term']['id'] and fields[6]=='IBD']
        paint.append({'source_index':row['source_index'],'source':source,'node':node,'target_descends':node in target_nodes,'ibd_records':matches})
    root = ET.fromstring(raw['HPA-DRC4.xml']); entry=root.find('entry')
    hpa={'entry_name':entry.findtext('name'),'summary':entry.findtext('cellExpression/summary'),'summary_verification':entry.findtext('cellExpression/verification'),'assays':[]}
    for antibody in entry.findall('antibody'):
        for sa in antibody.findall('cellExpression/subAssay'):
            assay={'antibody':antibody.get('id'),'type':sa.attrib,'verification':sa.findtext('verification'),'samples':[]}
            for data in sa.findall('data'):
                assay['samples'].append({'cell_line':data.findtext('cellLine'),'locations':[{'label':x.text,**x.attrib} for x in data.findall('location')],'image_urls':[x.text for x in data.findall('.//imageUrl')]})
            hpa['assays'].append(assay)
    result={'target':target,'target_parent_sequence_length':len(seq),'target_parent_rogid':rogid(seq),'raw_interaction_records':len(records),'binding_rows':projected,
            'paint':{'target_path':target_path,'contexts':paint,'target_path_ird_records':[{'physical_line':line,'fields':fields} for line,fields in gaf if len(fields)>6 and fields[1] in target_nodes and fields[6]=='IRD']},'HPA':hpa,
            'scope':'Factual source projection. Parent-sequence checksums do not erase separately recorded binding-region features. No annotation verdicts or physiological validation are generated.'}
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'inputs':len(raw),'binding_source_rows':len(projected),'matched_rows':sum(bool(x['records']) for x in projected),'paint_contexts':len(paint),'HPA_assays':len(hpa['assays']),'output_sha256':sha(args.output.read_bytes())}))

if __name__=='__main__':
    main()
