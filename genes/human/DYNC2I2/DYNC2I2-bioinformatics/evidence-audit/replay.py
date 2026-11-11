"""Recompute selected interaction, lineage, rule and compartment records from raw data."""
from pathlib import Path
import argparse,base64,hashlib,html,json,re,zipfile,difflib

def derive(directory):
    manifest=json.loads((directory/'source-manifest.json').read_text())
    archive=zipfile.ZipFile(directory/'source-inputs.zip')
    raw={x['name']:archive.read(x['name']) for x in manifest['inputs']}
    for item in manifest['inputs']:
        assert hashlib.sha256(raw[item['name']]).hexdigest()==item['sha256'],item['name']
    def read(name):return json.loads(raw[name])
    config=json.loads((directory/'selection.json').read_text())
    accession=config['accession'];uniprot=read('UniProt-'+accession+'.json')
    mitab=[line.split('\t') for line in raw['IntAct-'+accession+'.mitab'].decode().splitlines() if line and not line.startswith('#')]
    pairs=[]
    for selection in config['pairs']:
        records=[]
        for i,row in enumerate(mitab):
            if {row[0],row[1]}!={'uniprotkb:'+accession,'uniprotkb:'+selection['partner']}:continue
            if 'pubmed:'+selection['pmid'] not in row[8].split('|'):continue
            checks=[]
            for side in range(2):
                acc=row[side].split(':',1)[1];u=read('UniProt-'+acc+'.json');seq=u['sequence']['value']
                rogid=base64.b64encode(hashlib.sha1(seq.encode()).digest()).decode().rstrip('=')+str(u['organism']['taxonId'])
                checks.append({'accession':acc,'length':len(seq),'taxon':u['organism']['taxonId'],'rogid':rogid,'matches':'rogid:'+rogid in row[32+side].split('|')})
            records.append({'record_index':i,'participants':row[:2],'method':row[6],'publication':row[8],'taxa':row[9:11],'type':row[11],'identifiers':row[13],'expansion':row[15],'roles':row[16:20],'negative':row[35],'feature_a':row[36],'feature_b':row[37],'checks':checks})
        pairs.append({**selection,'records':records})
    tree=read(config['family']+'-tree.json')['search']['tree_topology']['annotation_node'];nodes=[];paths=[]
    def walk(node,path):
        path=path+[node];nodes.append(node)
        if accession in str({k:v for k,v in node.items() if k!='children'}):paths.append(path)
        children=node.get('children',{}).get('annotation_node',[])
        for child in ([children] if isinstance(children,dict) else children):walk(child,path)
    walk(tree,[]);assert len(paths)==1
    pids=[n['persistent_id'] for n in paths[0]]
    sequences=read(config['family']+'-familymsa.json')['search']['MSA_list']['sequence_info']
    seq=next(x for x in sequences if x['persistent_id']==pids[-1]);ungapped=re.sub('[^A-Za-z]','',seq['sequence']).upper()
    ibds=[]
    for i,line in enumerate(raw['IBD.gaf'].decode().splitlines()):
        if not line or line.startswith('!'):continue
        fields=line.split('\t')
        if fields[1] in pids and fields[4] in config['paint_terms']:ibds.append({'line':i,'fields':fields})
    rules=[];ids={x['id'] for x in uniprot['uniProtKBCrossReferences']};taxa=set(uniprot['organism']['lineage'])|{uniprot['organism']['scientificName']}
    for rule in config['rules']:
        matched=[]
        for i,conditions in enumerate(read(rule+'.json')['mainRule']['conditionSets']):
            flags=[]
            for c in conditions['conditions']:
                found=bool({v['value'] for v in c['conditionValues']} & (taxa if c['type']=='taxon' else ids))
                flags.append(not found if c.get('isNegative') else found)
            if all(flags):matched.append({'index':i,'conditions':conditions})
        rules.append({'rule':rule,'matching_condition_sets':matched})
    database={}
    for name in raw:
        if name.startswith('Reactome-') and name.endswith('.json'):
            obj=read(name);database[obj['dbId']]=obj
    def trace(node,path=()):
        if node in path or node not in database:return []
        obj=database[node];path=path+(node,)
        if obj.get('referenceEntity',{}).get('identifier')==accession:return [list(path)]
        return [p for relation in ['input','output','hasComponent','hasMember','hasCandidate'] for child in obj.get(relation,[]) for p in trace(child['dbId'] if isinstance(child,dict) else child,path)]
    reactome=[{'root_id':root,'name':database[root]['displayName'],'paths':trace(root)} for root in config['reactome_roots']]
    text=html.unescape(re.sub('<[^>]+>',' ',raw['HPA-DYNC2I2-subcellular.html'].decode()))
    text=re.sub(r'\s+',' ',text)
    hpa=[{'location':name,'reliability':score} for name,score in re.findall(r'(Nucleoplasm|Centrosome|Basal body|Nucleoli|Nuclear bodies|Primary cilium|Cytosol)\s*\((uncertain|supported|approved)\)',text)]
    hpa=list({(x['location'],x['reliability']):x for x in hpa}.values())
    cx={k:v for block in read('40205054-apms-network.json') for k,v in block.items()};cxnodes={n['@id']:n for n in cx['nodes']}
    edges=[]
    for edge in cx['edges']:
        if {cxnodes[edge['s']]['n'],cxnodes[edge['t']]['n']}==set(config['apms_pair']):
            edges.append({'edge':edge,'source':cxnodes[edge['s']],'target':cxnodes[edge['t']],'attributes':[a for a in cx['edgeAttributes'] if a.get('po')==edge['@id']]})
    partner,comparator=[read('UniProt-'+acc+'.json') for acc in config['meox2_comparison']]
    a,b=partner['sequence']['value'],comparator['sequence']['value'];alignment=difflib.SequenceMatcher(None,a,b,autojunk=False).get_opcodes()
    domains=[]
    for feature in comparator.get('features',[]):
        if feature['type']!='DNA binding' or feature.get('description')!='Homeobox':continue
        start=feature['location']['start']['value']-1;end=feature['location']['end']['value']
        mappings=[]
        for tag,a0,a1,b0,b1 in alignment:
            if tag=='equal' and b0<=start and end<=b1:
                left=a0+start-b0;right=a0+end-b0
                mappings.append({'partner_range':[left+1,right],'comparator_range':[start+1,end],'identical':a[left:right]==b[start:end]})
        domains.append({'feature':feature,'mappings':mappings})
    trim=[]
    for name in ['QuickGO-Q9BYV2.json','QuickGO-Q9BYV2-page2.json']:
        trim.extend(x for x in read(name)['results'] if x['goId']=='GO:0061630')
    return {'target':{'accession':accession,'length':len(uniprot['sequence']['value'])},'interactions':pairs,
        'paint':{'nodes':len(nodes),'target_path':pids,'target_sequence_matches':ungapped==uniprot['sequence']['value'],'ibds':ibds},
        'arba':rules,'reactome':reactome,'hpa_per_location':hpa,'apms':edges,
        'MEOX2_reference_comparison':{'accessions':config['meox2_comparison'],'lengths':[len(a),len(b)],'opcodes':alignment,'homeobox':domains},'TRIM54_class_records':trim}

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--output',type=Path);parser.add_argument('--check',action='store_true');args=parser.parse_args()
    directory=Path(__file__).resolve().parent;result=derive(directory)
    # Round-trip makes tuples from the alignment comparable to stored JSON lists.
    result=json.loads(json.dumps(result))
    if args.check:assert result==json.loads((directory/'results.json').read_text()),'Derived output differs'
    if args.output:args.output.write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n')
    print(json.dumps({'status':'PASS','positive_pair_records':sum(len(p['records']) for p in result['interactions']),
      'sequence_checks':sum(len(r['checks']) for p in result['interactions'] for r in p['records']),
      'target_sequence_matches':result['paint']['target_sequence_matches'],'IBDs':len(result['paint']['ibds']),
      'Reactome_paths':sum(len(r['paths']) for r in result['reactome']),'APMS_edges':len(result['apms'])}))
if __name__=='__main__':main()
