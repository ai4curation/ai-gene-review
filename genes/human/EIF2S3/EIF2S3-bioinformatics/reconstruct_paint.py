from pathlib import Path
import hashlib,json,re


E = Path(__file__).resolve().parent
O=E.parent
T=O.parent
def run():
    seed={'existing_annotations':json.loads((E/'source-contexts.json').read_text())}
    tree=json.loads((E/'raw/PTHR42854-treeinfo.json').read_text())['search']['tree_topology']['annotation_node']
    nodes={};paths={}
    def walk(n,path):
        ident=n['persistent_id']
        if ident in nodes:raise RuntimeError('duplicate tree ID')
        nodes[ident]=n;paths[ident]=path+[ident]
        children=n.get('children',{}).get('annotation_node',[])
        for c in [children] if isinstance(children,dict) else children:walk(c,path+[ident])
    walk(tree,[])
    target=[x for x in nodes if nodes[x].get('node_name','').endswith('UniProtKB=P41091')]
    if len(target)!=1:raise RuntimeError('nonunique target')
    target=target[0];path=paths[target]
    msa=json.loads((E/'raw/PTHR42854-familymsa.json').read_text())['search']['MSA_list']['sequence_info']
    hit=[x for x in msa if x['persistent_id']==target]
    if len(hit)!=1:raise RuntimeError('MSA target')
    ungapped=re.sub('[^A-Za-z]','',hit[0]['sequence']).upper()
    official=json.loads((E/'raw/UniProt-P41091.json').read_text())['sequence']['value']
    if ungapped!=official:raise RuntimeError('MSA sequence mismatch')
    ibd=E/'raw/IBD.gaf'
    pathrecords=[]
    for line_no,line in enumerate(ibd.read_text().splitlines(),1):
        if not line or line.startswith('!'):continue
        fields=line.split('\t')
        if fields[1] in path:pathrecords.append({'line':line_no,'fields':fields})
    joins=[]
    for i,a in enumerate(seed['existing_annotations']):
        if a['evidence_type']!='IBA':continue
        donor_nodes=[x.split(':',1)[1] for x in a['supporting_entities'] if x.startswith('PANTHER:')]
        matches=[r for r in pathrecords if r['fields'][1] in donor_nodes and r['fields'][4]==a['term']['id'] and r['fields'][6]=='IBD' and 'NOT' not in r['fields'][3]]
        if len(matches)!=1:raise RuntimeError('IBD match '+str(i))
        carried=set(a['supporting_entities'])-{'PANTHER:'+n for n in donor_nodes}
        if set(matches[0]['fields'][7].split('|'))!=carried:raise RuntimeError('donor mismatch')
        joins.append({'annotation_index':i,'source':{k:v for k,v in a.items() if k!='review'},'IBD':matches[0],'node_on_target_path':all(n in path for n in donor_nodes)})
    donors={}
    for ac in ['P32481','Q09130']:
        d=json.loads((E/'raw'/f'QuickGO-{ac}-page1.json').read_text())
        if d['pageInfo']['total']!=1 or d['numberOfHits']!=len(d['results']):raise RuntimeError('incomplete donor')
        donors[ac]={'total':len(d['results']),'selected':[x for x in d['results'] if x['goId'] in {j['source']['term']['id'] for j in joins}|{'GO:0003924','GO:1990856'}]}
    output={'target':target,'target_node':{k:v for k,v in nodes[target].items() if k in ['node_name','gene_id','organism','gene_symbol']},'node_count':len(nodes),'MSA_count':len(msa),'target_path':path,'ungapped_sequence':ungapped,'sequence_length':len(ungapped),'exact_official_sequence':True,'path_IBD_IRD_records':pathrecords,'IBA_joins':joins,'donor_annotations':donors,'scope':'Literal saved database reconstruction; original donor bodies not newly interpreted by this script.'}
    return output

if __name__ == "__main__":
    import argparse
    ap=argparse.ArgumentParser();ap.add_argument("--output",required=True);args=ap.parse_args()
    Path(args.output).write_text(json.dumps(run(),indent=2)+"\n")
