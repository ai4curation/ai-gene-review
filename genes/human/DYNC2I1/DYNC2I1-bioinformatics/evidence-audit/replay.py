#!/usr/bin/env python3
"""Reproduce DYNC2I1 database joins from authenticated, portable saved inputs."""
import argparse,base64,csv,hashlib,io,json,re,sys,zipfile
from pathlib import Path

def digest(raw):return hashlib.sha256(raw).hexdigest()

def load_inputs(base):
    manifest=json.loads((base/'source-manifest.json').read_text())
    archive=(base/manifest['archive']).read_bytes()
    if digest(archive)!=manifest['archive_sha256']:raise ValueError('Archive hash mismatch')
    data={}
    with zipfile.ZipFile(io.BytesIO(archive)) as z:
        if set(z.namelist())!={x['member'] for x in manifest['inputs']}:raise ValueError('Archive inventory mismatch')
        for x in manifest['inputs']:
            raw=z.read(x['member'])
            if len(raw)!=x['bytes'] or digest(raw)!=x['sha256']:raise ValueError('Input mismatch: '+x['member'])
            data[x['member']]=raw
    return manifest,data

def j(data,name):return json.loads(data[name])

def paint(data,accession):
    root=j(data,'PTHR16022-tree.json')['search']['tree_topology']['annotation_node'];nodes=[]
    def walk(n,path):
        path=path+[n['persistent_id']]
        nodes.append({**{k:v for k,v in n.items() if k!='children'},'path':path})
        children=n.get('children',{}).get('annotation_node',[])
        for child in children if isinstance(children,list) else [children]:walk(child,path)
    walk(root,[])
    selected=[n for n in nodes if re.search(r'UniProtKB='+re.escape(accession)+r'(?:\||$)',n.get('node_name',''))]
    if len(selected)!=1:raise ValueError('Expected one target tree leaf: '+accession)
    target=selected[0];msa=j(data,'PTHR16022-msa.json')['search']['MSA_list']['sequence_info']
    aligned=[x for x in msa if x['persistent_id']==target['persistent_id']]
    if len(aligned)!=1:raise ValueError('MSA leaf join failed')
    sequence=re.sub('[^A-Za-z]','',aligned[0]['sequence']).upper()
    official=j(data,'UniProt-'+accession+'.json')['sequence']['value']
    if sequence!=official:raise ValueError('MSA/official sequence mismatch: '+accession)
    rows=[];headers=[]
    for number,line in enumerate(data['IBD.gaf'].decode().splitlines(),1):
        if line.startswith('!'):headers.append(line);continue
        f=line.split('\t')
        if len(f)>=17 and f[1] in target['path']:rows.append({'line_1based':number,'fields':f})
    assertions=j(data,'source-assertions.json')
    joins=[]
    if accession=='Q8WVS4':
        for index,a in enumerate(assertions):
            if a['evidence_type']!='IBA':continue
            matches=[r for r in rows if r['fields'][4]==a['term']['id'] and r['fields'][6]=='IBD'
                     and 'PANTHER:'+r['fields'][1] in a.get('supporting_entities',[])]
            joins.append({'annotation_index':index,'term':a['term']['id'],'source_nodes':a.get('supporting_entities',[]),
                          'matching_IBD_lines':[r['line_1based'] for r in matches]})
    return {'accession':accession,'target':target,'tree_nodes':len(nodes),'MSA_sequences':len(msa),
            'sequence_length':len(sequence),'sequence_sha256':digest(sequence.encode()),'IBD_headers':headers,
            'literal_path_rows':rows,'source_joins':joins}

def interactions(data):
    rows=list(csv.reader(io.StringIO(data['intact-Q8WVS4.tsv'].decode()),delimiter='\t'))
    assertions=j(data,'source-assertions.json');pairs=[];proof=[]
    for index,a in enumerate(assertions):
        if a['term']['id']!='GO:0005515':continue
        pmid=a['original_reference_id'].removeprefix('PMID:')
        partners=[x.removeprefix('UniProtKB:') for x in a.get('supporting_entities',[]) if x.startswith('UniProtKB:')]
        matches=[]
        for number,r in enumerate(rows,1):
            if len(r)<38 or 'pubmed:'+pmid not in r[8].split('|'):continue
            if 'uniprotkb:Q8WVS4' not in r[:2] or not any('uniprotkb:'+p in r[:2] for p in partners):continue
            matches.append({'line_1based':number,'fields':r})
            for participant,identifier in enumerate(r[:2]):
                if not identifier.startswith('uniprotkb:'):continue
                accession=identifier.removeprefix('uniprotkb:');name='UniProt-'+accession+'.json'
                if name not in data:continue
                up=j(data,name);seq=up['sequence']['value']
                rogid=base64.b64encode(hashlib.sha1(seq.encode()).digest()).decode().rstrip('=')+str(up['organism']['taxonId'])
                proof.append({'annotation_index':index,'line_1based':number,'accession':accession,
                              'sequence_length':len(seq),'calculated_ROGID':rogid,'observed_checksums':r[32+participant],
                              'matches':'rogid:'+rogid in r[32+participant].split('|')})
        pairs.append({'annotation_index':index,'source':a,'matched_records':len(matches),'records':matches})
    return {'raw_records':len(rows),'source_pairs':pairs,'ROGID_comparisons':proof}

def apms(data,symbol,partner):
    parts={k:v for aspect in j(data,'40205054-apms-network.json') for k,v in aspect.items()}
    nodes={n['@id']:n for n in parts['nodes']}
    selected=[n for n in nodes.values() if n['n']==symbol]
    if len(selected)!=1:raise ValueError('Ambiguous AP-MS target')
    target=selected[0];records=[]
    for edge in parts['edges']:
        if target['@id'] not in [edge['s'],edge['t']]:continue
        records.append({'edge':edge,'source':nodes[edge['s']],'target':nodes[edge['t']],
                        'edge_attributes':[x for x in parts['edgeAttributes'] if x.get('po')==edge['@id']],
                        'node_attributes':[x for x in parts['nodeAttributes'] if x.get('po') in [edge['s'],edge['t']]],
                        'selected_pair':{nodes[edge['s']]['n'],nodes[edge['t']]['n']}=={symbol,partner}})
    return {'network_nodes':len(nodes),'network_edges':len(parts['edges']),'target':target,
            'incident_count':len(records),'selected_count':sum(x['selected_pair'] for x in records),'records':records}

def reactome(data,roots,accession):
    db={}
    for name in data:
        if name.startswith('reactome/'):
            d=j(data,name);db[d['dbId']]=d
    relations=['input','output','hasComponent','hasMember','hasCandidate']
    def trace(node,path=()):
        if node in path or node not in db:return []
        d=db[node];path=path+(node,)
        if d.get('referenceEntity',{}).get('identifier')==accession:return [list(path)]
        out=[]
        for relation in relations:
            for child in d.get(relation,[]):out+=trace(child.get('dbId') if isinstance(child,dict) else child,path)
        return out
    events={str(root):{'name':db[root]['displayName'],'paths':trace(root)} for root in roots}
    nodes={str(n):{'name':d['displayName'],'compartments':[x.get('displayName') for x in d.get('compartment',[])],
                   'reference':d.get('referenceEntity',{}).get('identifier'),'start':d.get('startCoordinate'),
                   'end':d.get('endCoordinate')} for n,d in db.items()}
    return {'events':events,'nodes':nodes,'event_count':len(events),'path_count':sum(len(x['paths']) for x in events.values())}

def ontology(data):
    terms={}
    for name in data:
        if name.startswith('GO') or name=='typed-ancestors.json':
            for term in j(data,name).get('results',[]):terms[term['id']]={**terms.get(term['id'],{}),**term}
    base,tip,cilium='GO:0097546','GO:0097542','GO:0005929'
    bp1,bp2='GO:0060271','GO:0035721'
    return {'terms':terms,'relation_filter':['is_a','part_of'],
            'base_tip_nonredundant':base not in terms[tip]['ancestors'] and tip not in terms[base]['ancestors'],
            'both_locations_descend_from_cilium':all(cilium in terms[t]['ancestors'] for t in [base,tip]),
            'process_pair_nonredundant':bp1 not in terms[bp2]['ancestors'] and bp2 not in terms[bp1]['ancestors']}

def calculate(manifest,data):
    return {'paint':paint(data,manifest['target']),'interactions':interactions(data),
            'apms':apms(data,manifest['symbol'],manifest['selection']['apms_partner']),
            'reactome':reactome(data,manifest['selection']['reactome_roots'],manifest['target']),
            'ontology':ontology(data)}

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--base',type=Path,default=Path(__file__).resolve().parent)
    parser.add_argument('--output',type=Path);parser.add_argument('--check',action='store_true')
    parser.add_argument('--paint-target',help='Run only the generic PAINT/sequence join for another packaged target')
    args=parser.parse_args();manifest,data=load_inputs(args.base)
    result=paint(data,args.paint_target) if args.paint_target else calculate(manifest,data)
    if args.check:
        if args.paint_target:parser.error('--check uses the full target result; use --output for alternate targets')
        expected=json.loads((args.base/'results.json').read_text())
        if result!=expected:raise ValueError('Recomputed results differ from results.json')
    if args.output:args.output.write_text(json.dumps(result,indent=2)+'\n')
    if args.paint_target:summary={'target':args.paint_target,'sequence_length':result['sequence_length'],'tree_nodes':result['tree_nodes']}
    else:
        p=result['paint'];i=result['interactions'];r=result['reactome'];o=result['ontology']
        summary={'target':manifest['target'],'tree_nodes':p['tree_nodes'],'MSA_sequences':p['MSA_sequences'],
                 'sequence_length':p['sequence_length'],'IBA_joins':len(p['source_joins']),
                 'joined_IBAs':sum(bool(x['matching_IBD_lines']) for x in p['source_joins']),
                 'IntAct_raw_records':i['raw_records'],'source_pairs':len(i['source_pairs']),
                 'matched_records':sum(x['matched_records'] for x in i['source_pairs']),
                 'ROGID_matches':sum(x['matches'] for x in i['ROGID_comparisons']),
                 'ROGID_comparisons':len(i['ROGID_comparisons']),
                 'APMS_incident':result['apms']['incident_count'],'APMS_selected':result['apms']['selected_count'],
                 'Reactome_events':r['event_count'],'Reactome_paths':r['path_count'],
                 'base_tip_nonredundant':o['base_tip_nonredundant'],'process_pair_nonredundant':o['process_pair_nonredundant']}
    print(json.dumps({'status':'PASS','checked_saved_result':args.check,'summary':summary},sort_keys=True))

if __name__=='__main__':main()
