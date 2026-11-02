#!/usr/bin/env python3
"""Recompute source joins from authenticated inputs; no network or review writes."""
import argparse,collections,hashlib,json,re,tarfile
from pathlib import Path
from io import BytesIO
from bs4 import BeautifulSoup
import openpyxl

def sha(data):
    return hashlib.sha256(data).hexdigest()

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--inputs',type=Path,default=Path('raw-inputs.tar.gz'))
    parser.add_argument('--manifest',type=Path,default=Path('input-manifest.json'))
    parser.add_argument('--queries',type=Path,default=Path('queries.json'))
    parser.add_argument('--output',type=Path,required=True)
    parser.add_argument('--workbook',type=Path,help='Exact publisher Table S1 workbook; not bundled in the source archive')
    args=parser.parse_args()
    manifest=json.loads(args.manifest.read_text());query=json.loads(args.queries.read_text())
    raw={}
    if args.inputs.is_dir():
        raw={item['name']:(args.inputs/item['name']).read_bytes() for item in manifest if (args.inputs/item['name']).is_file()}
    else:
        with tarfile.open(args.inputs,'r:gz')as archive:
            present=set(archive.getnames())
            raw={item['name']:archive.extractfile(item['name']).read() for item in manifest if item['name'] in present}
    workbook_name=query['workbook']['filename']
    if args.workbook is not None:
        if not args.workbook.is_file():
            raise SystemExit('Workbook path does not exist: '+str(args.workbook))
        raw[workbook_name]=args.workbook.read_bytes()
    missing=[item['name'] for item in manifest if item['name'] not in raw]
    if missing:
        raise SystemExit('Missing exact input(s): '+', '.join(missing)+'. Table S1 is not bundled. Supply --workbook PATH, or run python fetch_inputs.py --output external-inputs and use --workbook external-inputs/'+workbook_name)
    for item in manifest:
        if sha(raw[item['name']])!=item['sha256']:
            raise SystemExit('Input mismatch: '+item['name'])
    def js(name):
        return json.loads(raw[name])
    target=query['target'];family=query['family'];protein=js('UniProt-'+target+'.json')
    root=js(family+'-tree.json')['search']['tree_topology']['annotation_node']
    nodes=[];paths=[]
    def visit(node,path):
        path=path+[node];nodes.append(node)
        if 'UniProtKB='+target in node.get('node_name',''):
            paths.append(path)
        children=node.get('children',{}).get('annotation_node',[])
        if isinstance(children,dict):
            children=[children]
        for child in children:
            visit(child,path)
    visit(root,[])
    if len(paths)!=1:
        raise SystemExit('Target family leaf is missing or ambiguous')
    path=paths[0];pids=[node['persistent_id']for node in path]
    msa=js(family+'-msa.json')['search']['MSA_list']['sequence_info']
    target_msa=next(row for row in msa if row['persistent_id']==pids[-1])
    def sequence(aligned):
        return re.sub('[^A-Za-z]','',aligned).upper()
    if sequence(target_msa['sequence'])!=protein['sequence']['value']:
        raise SystemExit('Target alignment sequence differs from official input')
    ibds=[]
    for index,line in enumerate(raw['IBD.gaf'].decode().splitlines()):
        fields=line.split('\t')
        if not line.startswith('!')and len(fields)>6 and fields[1]in pids:
            ibds.append({'line_zero_based':index,'fields':fields})
    paint=[]
    for index,source in enumerate(query['sources']):
        if source['evidence_type']!='IBA':
            continue
        source_nodes=[x.split(':',1)[1]for x in source.get('supporting_entities',[])if x.startswith('PANTHER:')]
        matching=[x for x in ibds if x['fields'][1]in source_nodes and x['fields'][4]==source['term']['id']]
        paint.append({'row':index,'original_term':source['term'],'source_nodes':source_nodes,'on_target_path':all(x in pids for x in source_nodes),'literal_ibds':matching})

    anchor=query['anchor'];anchor_record=js('UniProt-'+anchor+'.json')
    anchor_nodes=[node for node in nodes if 'UniProtKB='+anchor in node.get('node_name','')]
    if len(anchor_nodes)!=1:
        raise SystemExit('Anchor family leaf is missing or ambiguous')
    anchor_msa=next(row for row in msa if row['persistent_id']==anchor_nodes[0]['persistent_id'])
    if sequence(anchor_msa['sequence'])!=anchor_record['sequence']['value']:
        raise SystemExit('Anchor alignment sequence differs from official input')
    def positions(aligned):
        n=0;result={}
        for column,residue in enumerate(aligned):
            if residue.isalpha():
                n+=1;result[n]=(column,residue.upper())
        return result
    anchor_positions=positions(anchor_msa['sequence'])
    target_positions=positions(target_msa['sequence'])
    reverse={column:(position,residue)for position,(column,residue)in target_positions.items()}
    sites=[]
    for feature in anchor_record.get('features',[]):
        if feature['type']!='Binding site'or feature.get('ligand',{}).get('id')!='ChEBI:CHEBI:29105':
            continue
        anchor_position=feature['location']['start']['value']
        column,residue=anchor_positions[anchor_position]
        sites.append({'anchor_accession':anchor,'anchor_position':anchor_position,'anchor_residue':residue,'anchor_feature':feature,'alignment_column_zero_based':column,'target_position_and_residue':reverse.get(column)})

    workbook_name=query['workbook']['filename'];workbook_bytes=raw[workbook_name]
    md5=hashlib.md5(workbook_bytes).hexdigest()
    if md5!=query['workbook']['published_md5']:
        raise SystemExit('Workbook differs from the article-published MD5')
    workbook=openpyxl.load_workbook(BytesIO(workbook_bytes),read_only=True,data_only=True)
    pattern=re.compile(r'(?<![A-Za-z0-9])(?:'+re.escape(target)+'|'+re.escape(query['gene'])+r')(?![A-Za-z0-9])')
    records=[]
    for sheet in workbook:
        headings=[];groups=[]
        for row_number,values in enumerate(sheet.iter_rows(values_only=True),1):
            if row_number==1:
                current=None
                for value in values:
                    if value is not None:
                        current=value
                    groups.append(current)
            if row_number==2:
                headings=list(values)
            if row_number<3 or not any(isinstance(value,str)and pattern.search(value)for value in values):
                continue
            selected=[]
            for column,value in enumerate(values):
                if value is None or value=='':
                    continue
                heading=headings[column]if column<len(headings)else None
                group=groups[column]if column<len(groups)else None
                if heading in query['workbook']['identity_columns']or isinstance(value,(int,float))or heading in ['Classification','Classification with subclusters','Category']:
                    selected.append({'column_one_based':column+1,'group':group,'heading':heading,'value':value})
            records.append({'sheet':sheet.title,'excel_row':row_number,'fields':selected})

    reactions=[]
    for name,data in raw.items():
        if not name.startswith('RHEA-')or not name.endswith('.html'):
            continue
        rid=name.split('-')[1].split('.')[0]
        text=BeautifulSoup(data,'html.parser').get_text(' ',strip=True)
        marker='RHEA: '+rid
        equation=text[text.index(marker):].split('Reaction information')[0].strip()
        reactions.append({'rhea':rid,'equation':equation})
    iprs=[]
    for name,data in raw.items():
        if name.startswith('IPR')and name.endswith('.json'):
            record=json.loads(data)
            iprs.append({'input':name,'id':record['metadata']['accession'],'name':record['metadata']['name'],'go_terms':record['metadata']['go_terms'],'target_matches':record.get('proteins',[])})
    rule=js('ARBA00026962.json')
    result={'input_count':len(manifest),'target':target,'official_length':len(protein['sequence']['value']),'family':family,'tree_nodes':len(nodes),'msa_sequences':len(msa),'target_path':[{'id':node['persistent_id'],'name':node.get('node_name')}for node in path],'paint_rows':paint,'zinc_anchor_sites':sites,'proteomics':{'published_md5':md5,'records':records,'scope':'Protein-group measurements. Matrix GO column is imported annotation; peripheral category is operational fractionation, not membrane-face localization.'},'reactions':sorted(reactions,key=lambda x:x['rhea']),'interpro':iprs,'subcellular_location_mapping':js('SL-0170.json'),'ARBA':{'output':rule['mainRule']['annotations'],'condition_sets':len(rule['mainRule']['conditionSets']),'condition_types':dict(collections.Counter(condition['type']for item in rule['mainRule']['conditionSets']for condition in item['conditions'])),'scope':'No complete target FunFam trigger is asserted.'},'scope':'Raw-source computation is not an independent experiment, metal-occupancy assay, or isoform-specific functional test.'}
    args.output.write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n')
    print(json.dumps({'status':'PASS','inputs':len(manifest),'source_rows':len(query['sources']),'tree_nodes':len(nodes),'literal_IBD_joins':sum(len(x['literal_ibds'])for x in paint),'table_records':len(records),'zinc_site_correspondences':len(sites)}))

if __name__=='__main__':
    main()
