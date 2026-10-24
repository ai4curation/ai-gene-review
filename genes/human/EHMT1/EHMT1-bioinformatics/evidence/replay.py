#!/usr/bin/env python3
"""Replay literal EHMT1 database joins from an authenticated archive, offline."""
from pathlib import Path, PurePosixPath
import argparse
import collections
import csv
import hashlib
import io
import json
import re
import zipfile
import xml.etree.ElementTree as ET

BASE = Path(__file__).resolve().parent

def require(condition, message):
    if not condition:
        raise ValueError(message)

def digest(data):
    return hashlib.sha256(data).hexdigest()

class Inputs:
    def __init__(self, archive, manifest):
        data = archive.read_bytes()
        require(digest(data) == manifest['archive_sha256'], 'Archive checksum mismatch')
        self.zip = zipfile.ZipFile(io.BytesIO(data))
        infos = self.zip.infolist()
        names = [x.filename for x in infos]
        require(len(names) == len(set(names)), 'Duplicate archive members')
        require(set(names) == {x['name'] for x in manifest['inputs']}, 'Unexpected or missing archive member')
        self.rows = {x['name']:x for x in manifest['inputs']}
        for info in infos:
            path = PurePosixPath(info.filename)
            require(not path.is_absolute() and '..' not in path.parts and not info.is_dir(), 'Unsafe archive name')
            require(info.file_size == self.rows[info.filename]['bytes'] and info.file_size < 20_000_000, 'Unexpected member size')
        require(sum(x.file_size for x in infos) < 50_000_000, 'Unexpected total archive size')
    def raw(self, name):
        data = self.zip.read(name)
        require(digest(data) == self.rows[name]['sha256'], 'Input checksum mismatch: ' + name)
        return data
    def text(self, name):
        return self.raw(name).decode('utf-8')
    def json(self, name):
        return json.loads(self.text(name))

def entities(value):
    return tuple(sorted(set(value if isinstance(value,list) else filter(None,value.replace(',','|').split('|')))))

def source_key(row):
    return (row['term']['id'],row['evidence_type'],row['original_reference_id'],entities(row.get('supporting_entities',[])),bool(row.get('negated')),row.get('qualifier',''),row.get('isoform'))

def raw_key(row):
    product = row['GENE PRODUCT ID'].split(':')[-1]
    q = row['QUALIFIER'].split('|')
    return (row['GO TERM'],row['GO EVIDENCE CODE'],row['REFERENCE'],entities(row['WITH/FROM']),'NOT' in q,'|'.join(x for x in q if x != 'NOT'),product if '-' in product else None)

def derive(inputs, config):
    target = config['target']
    sources = inputs.json('source-objects.json')
    goa = list(csv.DictReader(io.StringIO(inputs.text('EHMT1-goa.tsv')),delimiter='\t'))
    require(set(map(source_key,sources)) == set(map(raw_key,goa)), 'GOA source context mismatch')
    source_joins = [{'row':i,'raw_rows':[j for j,r in enumerate(goa) if raw_key(r)==source_key(s)]} for i,s in enumerate(sources)]
    official = inputs.json('UniProt-'+target+'.json')
    products = []
    features = {x['featureId']:x for x in official['features'] if x.get('featureId')}
    alternatives = next(x['isoforms'] for x in official['comments'] if x['commentType']=='ALTERNATIVE PRODUCTS')
    for product in alternatives:
        seq = official['sequence']['value']
        edits = [features[x] for x in product.get('sequenceIds',[])]
        for edit in sorted(edits,key=lambda x:x['location']['start']['value'],reverse=True):
            a,b = edit['location']['start']['value']-1,edit['location']['end']['value']
            replacement = edit.get('alternativeSequence',{}).get('alternativeSequences',[''])[0]
            seq = seq[:a]+replacement+seq[b:]
        accession = product['isoformIds'][0]
        fasta = ''.join(x.strip() for x in inputs.text(accession+'.fasta').splitlines() if not x.startswith('>'))
        require(seq == fasta, 'Official product reconstruction mismatch: '+accession)
        products.append({'id':accession,'length':len(seq),'sequence_sha256':digest(seq.encode()),'sequenceIds':product.get('sequenceIds',[]),'reconstruction_features':edits})
    tree = inputs.json(config['tree'])['search']['tree_topology']['annotation_node']
    nodes, paths = {}, {}
    def walk(node,path):
        key=node['persistent_id'];nodes[key]={k:v for k,v in node.items() if k!='children'};paths[key]=path+[key]
        children=node.get('children',{}).get('annotation_node',[])
        for child in children if isinstance(children,list) else [children]:walk(child,path+[key])
    walk(tree,[])
    hits = [n for n in nodes.values() if 'UniProtKB='+target in n.get('node_name','')]
    require(len(hits)==1,'Target tree identity is not unique')
    path=paths[hits[0]['persistent_id']]
    ibds=[x.split('\t') for x in inputs.text('IBD.gaf').splitlines() if x.startswith('PANTHER\t') and x.split('\t')[1] in path]
    msa=inputs.json(config['msa'])['search']['MSA_list']['sequence_info']
    seq=next(x['sequence'] for x in msa if x['persistent_id']==hits[0]['persistent_id']).replace('.','').replace('-','').upper()
    require(seq==official['sequence']['value'],'Target MSA/reference mismatch')
    paint={'node_count':len(nodes),'target_path':[{'persistent_id':x,'name':nodes[x].get('node_name'),'gene_symbol':nodes[x].get('gene_symbol')}for x in path],'literal_IBD':ibds,'aligned_target_length':len(seq)}
    # Current donor records are not all independent experiments; preserve evidence labels.
    donor_joins=[]
    for i,s in enumerate(sources):
        for entity in s.get('supporting_entities',[]):
            accession=config['donors'].get(entity)
            if accession:
                donor=inputs.json('QuickGO-'+accession+'-page1.json')
                donor_joins.append({'row':i,'source_id':entity,'accession':accession,'matching_current_records':[r for r in donor.get('results',[]) if r['goId']==s['term']['id']],'pageInfo':donor.get('pageInfo'),'numberOfHits':donor.get('numberOfHits')})
    funfam={r['id']for r in official['uniProtKBCrossReferences']if r['database']=='FunFam'}
    lineage=set(official['organism']['lineage'])|{official['organism']['scientificName']}
    rules=[]
    for name in config['rules']:
        rule=inputs.json(name);matches=[]
        for i,cs in enumerate(rule.get('mainRule',{}).get('conditionSets',[])):
            decisions=[]
            for condition in cs['conditions']:
                values={x['value']for x in condition['conditionValues']}
                universe=funfam if condition['type']=='FunFam id' else lineage if condition['type']=='taxon' else None
                # Unknown predicate types are not inferred from free-text descriptions.
                if universe is None:decisions.append(False)
                else:
                    match=bool(values & universe)
                    decisions.append(not match if condition.get('isNegative') else match)
            if decisions and all(decisions):matches.append({'index':i,'conditionSet':cs})
        rules.append({'rule':name,'matching_sets':matches,'condition_set_count':len(rule.get('mainRule',{}).get('conditionSets',[])),'annotations':rule.get('mainRule',{}).get('annotations',[]),'retrieval_error':rule.get('messages')})
    # Follow only literal child edges whose model name identifies the target.
    roots=[s['original_reference_id'].split('-')[-1]for s in sources if s['original_reference_id'].startswith('Reactome:')]
    model_paths=[]
    def trace(nid,path,visited):
        require(nid not in visited and len(visited)<30,'Unexpected model cycle/depth')
        obj=inputs.json('Reactome-'+str(nid)+'.json');p=path+[{'dbId':obj['dbId'],'name':obj.get('displayName'),'class':obj.get('schemaClass')}]
        if obj.get('identifier')==target:model_paths.append(p);return
        for edge in ['input','output','catalystActivity','physicalEntity','hasComponent','hasMember','hasCandidate','referenceEntity']:
            value=obj.get(edge,[]);value=value if isinstance(value,list)else[value]
            for child in value:
                if isinstance(child,dict)and 'dbId'in child and (edge=='referenceEntity' or re.search(r'EHMT1|GLP|Q9H9B1',child.get('displayName',''),re.I)):
                    trace(child['dbId'],p+[{'edge':edge}],visited|{nid})
    for root in roots:trace(int(root),[],set())
    # Retain accession side, method, species and stable interaction IDs from the export.
    lines=inputs.text('IntAct-'+target+'.mitab').splitlines();pairs=[]
    for i,s in enumerate(sources):
        if s['evidence_type']!='IPI':continue
        pmid=s['original_reference_id'].replace('PMID:','');partners=[x.replace('UniProtKB:','')for x in s.get('supporting_entities',[])if x.startswith('UniProtKB:')]
        matches=[]
        for n,line in enumerate(lines,1):
            fields=line.split('\t')
            if len(fields)>13 and 'pubmed:'+pmid in fields[8] and any('uniprotkb:'+p in fields[:2] for p in partners):
                matches.append({'line_1based':n,'id_a':fields[0],'id_b':fields[1],'method':fields[6],'publication':fields[8],'taxon_a':fields[9],'taxon_b':fields[10],'interaction_type':fields[11],'interaction_id':fields[13]})
        pairs.append({'row':i,'reference':s['original_reference_id'],'partners':partners,'records':matches})
    xml=ET.fromstring(inputs.raw('HPA-EHMT1.xml'))
    expression=[{'summary':x.findtext('summary'),'verification':x.findtext('verification'),'locations':[{'label':a.text,**a.attrib}for a in x.findall('.//location')]}for x in xml.findall('entry/cellExpression')]
    html=inputs.text('HPA-EHMT1-subcellular.html')
    reliability=[{'line_1based':i+1,'text':line.strip()}for i,line in enumerate(html.splitlines())if 'Nucleoplasm (supported), Nuclear bodies (supported)'in line]
    require(reliability,'Per-location HPA reliability absent')
    partners=[]
    for accession in config['partners']:
        record=inputs.json('UniProt-'+accession+'.json')
        partners.append({'accession':record['primaryAccession'],'organism':record['organism'],'proteinDescription':record['proteinDescription'],'functions':[x for x in record.get('comments',[])if x['commentType']in['FUNCTION','SUBUNIT']],'domains':[x for x in record.get('features',[])if x['type']in['Domain','Region']]})
    return {'source_contexts':{'raw_count':len(goa),'normalized_count':len(sources),'joins':source_joins},'products':products,'paint':paint,'donor_joins':donor_joins,'arba':rules,'reactome':{'roots':roots,'target_paths':model_paths},'interactions':pairs,'hpa':{'expression':expression,'per_location_html':reliability,'image_pixels_inspected':False},'partner_class_sources':partners}

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--archive',type=Path,default=BASE/'inputs.zip')
    parser.add_argument('--output',type=Path)
    parser.add_argument('--check',action='store_true',help='Compare with the committed results without writing')
    args=parser.parse_args()
    manifest=json.loads((BASE/'input-manifest.json').read_text())
    config=json.loads((BASE/'config.json').read_text())
    inputs=Inputs(args.archive,manifest)
    try:result=derive(inputs,config)
    finally:inputs.zip.close()
    if args.check:
        require(result==json.loads((BASE/'results.json').read_text()),'Derived results differ')
        print(json.dumps({'status':'PASS','inputs':len(manifest['inputs']),'sources':result['source_contexts']['normalized_count'],'products':len(result['products']),'PAINT_nodes':result['paint']['node_count'],'Reactome_paths':len(result['reactome']['target_paths'])}))
    elif args.output:
        require(args.output.resolve() not in {(BASE/x).resolve() for x in ['inputs.zip','input-manifest.json','config.json','replay.py']},'Refuse to overwrite input/program')
        args.output.write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n')
    else:print(json.dumps(result,indent=2,ensure_ascii=False))

if __name__=='__main__':
    main()
