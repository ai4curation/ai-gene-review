"""Reproduce EGR2 database evidence from authenticated saved database inputs."""
import argparse,base64,csv,hashlib,io,json,re,tarfile
from pathlib import Path

HERE=Path(__file__).resolve().parent
MITAB={'id_a':0,'id_b':1,'method':6,'publication':8,'taxon_a':9,'taxon_b':10,
       'interaction_type':11,'interaction_id':13,'host':28,'rogid_a':32,'rogid_b':33,
       'negative':35,'features_a':36,'features_b':37}
def require(ok,message):
    if not ok:raise ValueError(message)
def derive(raw,config):
    def data(name):return json.loads(raw[name])
    official=data('UniProt-P11161.json');accession=official['primaryAccession'];seq=official['sequence']['value']
    nodes={};paths={}
    def visit(n,anc):
        key=n['persistent_id'];require(key not in nodes,'Repeated tree node')
        nodes[key]=n;paths[key]=anc+[key]
        children=n.get('children',{}).get('annotation_node',[])
        if isinstance(children,dict):children=[children]
        for child in children:visit(child,paths[key])
    visit(data('PTHR23235-tree.json')['search']['tree_topology']['annotation_node'],[])
    leaves=[n for n in nodes.values()if n.get('node_name','').endswith('UniProtKB='+accession)]
    require(len(leaves)==1,'Target leaf missing or ambiguous');leaf=leaves[0];key=leaf['persistent_id']
    align=[s for s in data('PTHR23235-msa.json')['search']['MSA_list']['sequence_info']if s['persistent_id']==key]
    require(len(align)==1,'Target MSA sequence missing or ambiguous')
    require(re.sub('[^A-Za-z]','',align[0]['sequence']).upper()==seq,'Target MSA/official sequence mismatch')
    terms={s['term']['id']for s in config['source_objects']if s['evidence_type']=='IBA'}
    ibds=[]
    for line,text in enumerate(raw['IBD.gaf'].decode().splitlines(),1):
        f=text.split('\t')
        if len(f)>6 and f[1] in paths[key] and f[4] in terms and f[6]=='IBD':
            ibds.append({'physical_line':line,'fields':f})
    require(terms=={x['fields'][4]for x in ibds},'An imported IBA term has no ancestral IBD')
    donor=data('P08152-QuickGO-page1.json');require(donor['numberOfHits']==len(donor['results']),'Incomplete donor response')
    rogid=lambda sequence,taxon:base64.b64encode(hashlib.sha1(sequence.encode()).digest()).decode().rstrip('=')+str(taxon)
    partners={}
    for name in ['P51610','O00308','Q60793']:
        d=data(name+'-UniProt.json');s=d['sequence']['value']
        partners[name]={'taxon':d['organism']['taxonId'],'length':len(s),'reference_ROGID':rogid(s,d['organism']['taxonId']),
                        'gene':d['genes'][0],'function_comments':[c for c in d.get('comments',[])if c['commentType']=='FUNCTION']}
    interactions=[]
    for line,f in enumerate(csv.reader(io.StringIO(raw['IntAct-P11161.tsv'].decode()),delimiter='\t'),1):
        require(len(f)>=42,'Incomplete MITAB 2.7 row '+str(line))
        interactions.append({'physical_line':line,'raw_fields':f,'fields':{name:f[i]for name,i in MITAB.items()}})
    selected=[x for x in interactions if 'pubmed:14532282'in x['fields']['publication'].split('|')]
    require(len(selected)==1,'HCFC1 source-record boundary changed')
    require([selected[0]['fields']['rogid_a'],selected[0]['fields']['rogid_b']]==['rogid:'+rogid(seq,9606),'rogid:'+partners['P51610']['reference_ROGID']],'Reference sequence checksums differ')
    objects={}
    for name in raw:
        if name.startswith(('R-HSA-','Reactome-')):
            d=data(name);objects[d['dbId']]=d
    target=objects[config['reactome_target']]
    require(target['referenceEntity']['identifier']==accession and target['species']['taxId']=='9606','Reactome target identity changed')
    def walk(entity,path,seen):
        id=entity if isinstance(entity,int)else entity['dbId']
        if id in seen:return []
        if id==target['dbId']:return [path]
        full=objects.get(id,entity if isinstance(entity,dict)else{})
        out=[]
        for rel in ['hasMember','hasComponent','hasCandidate']:
            for child in full.get(rel,[]):
                cid=child if isinstance(child,int)else child['dbId']
                out+=walk(child,path+[{'from':id,'relation':rel,'to':cid}],seen|{id})
        return out
    reactions=[]
    for index,source in enumerate(config['source_objects']):
        ref=source['original_reference_id']
        if not ref.startswith('Reactome:'):continue
        event=objects[int(ref.rsplit('-',1)[1])];chains=[]
        for role in ['input','output']:
            for entity in event.get(role,[]):
                eid=entity if isinstance(entity,int)else entity['dbId']
                chains+=walk(entity,[{'from':event['dbId'],'relation':role,'to':eid}],set())
        require(chains,'No target chain for '+ref)
        reactions.append({'source_index':index,'reference':ref,'event_name':event['displayName'],'target_paths':chains})
    go={}
    for name in ['GO-all-seeded-terms.json','GO-binding-export-terms.json']:
        for term in data(name)['results']:go[term['id']]=term
    return {'target':{'accession':accession,'length':len(seq),'reference_ROGID':rogid(seq,9606)},
            'paint':{'node_count':len(nodes),'target_node':key,'target_name':leaf['node_name'],'target_subfamily':leaf['prop_sf_id'],'target_path':paths[key],'exact_MSA_sequence':True,'IBDs':ibds},
            'mouse_donor':{'numberOfHits':donor['numberOfHits'],'results':donor['results']},
            'IntAct':{'count':len(interactions),'records':interactions,'HCFC1':selected,'official_partner_classes':partners,
                      'scope':'Reference ROGIDs and assayed feature intervals are separate. Parent checksum matching does not prove the species, complete insert or natural isoform tested in a paper.'},
            'Reactome':{'source_count':len(reactions),'raw_object_count':len(objects),'target':{k:target[k]for k in ['dbId','stId','compartment','species','startCoordinate','endCoordinate']},'reference':{k:target['referenceEntity'][k]for k in ['identifier','databaseName','sequenceLength']},'rows':reactions},
            'GO_definitions':go,'GO_typed_ancestors':data('GO-binding-export-ancestors.json')}
def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--archive',type=Path,default=HERE/'inputs.tar.gz')
    p.add_argument('--inputs-dir',type=Path,help='Optional directory containing the exact uncompressed input filenames')
    p.add_argument('--output',type=Path,required=True)
    p.add_argument('--compare',type=Path)
    args=p.parse_args();manifest=json.loads((HERE/'input-manifest.json').read_text());config=json.loads((HERE/'config.json').read_text())
    wanted={x['file']:x for x in manifest['inputs']};raw={}
    if args.inputs_dir:
        raw={name:(args.inputs_dir/name).read_bytes()for name in wanted}
    else:
        require(hashlib.sha256(args.archive.read_bytes()).hexdigest()==manifest['archive']['sha256'],'Archive hash mismatch')
        with tarfile.open(args.archive,'r:gz')as archive:
            members=archive.getmembers();require(len(members)==len(wanted),'Unexpected archive member count')
            require({m.name for m in members}==set(wanted)and all(m.isfile()for m in members),'Unexpected archive members')
            raw={m.name:archive.extractfile(m).read()for m in members}
    for name,content in raw.items():require(hashlib.sha256(content).hexdigest()==wanted[name]['sha256'],'Input hash mismatch: '+name)
    result=derive(raw,config)
    if args.compare:require(result==json.loads(args.compare.read_text()),'Computed results differ from recorded results')
    args.output.parent.mkdir(parents=True,exist_ok=True);args.output.write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n')
    print(json.dumps({'status':'PASS','input_files':len(raw),'tree_nodes':result['paint']['node_count'],'IBDs':len(result['paint']['IBDs']),'mouse_donor_rows':result['mouse_donor']['numberOfHits'],'IntAct_records':result['IntAct']['count'],'Reactome_rows':result['Reactome']['source_count'],'reference_sequence_match':True}))
if __name__=='__main__':main()
