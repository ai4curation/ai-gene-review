"""Reproduce target/source joins from checksum-verified raw inputs; Python standard library."""
from pathlib import Path
import argparse,base64,hashlib,io,json,re,tarfile
HERE=Path(__file__).resolve().parent

def load_inputs(input_dir=None):
    manifest=json.loads((HERE/'input-manifest.json').read_text())
    if input_dir:
        contents={x['name']:(input_dir/x['name']).read_bytes() for x in manifest['inputs']}
    else:
        archive=HERE/manifest['archive']['name']
        if not archive.is_file():
            raise SystemExit('Missing raw-inputs.tar.gz; restore the bundled archive or pass --input-dir with the exact archived inputs.')
        if hashlib.sha256(archive.read_bytes()).hexdigest()!=manifest['archive']['sha256']:
            raise SystemExit('Raw archive checksum mismatch.')
        with tarfile.open(archive,'r:gz') as tar:
            contents={x['name']:tar.extractfile(x['name']).read() for x in manifest['inputs']}
    for item in manifest['inputs']:
        if hashlib.sha256(contents[item['name']]).hexdigest()!=item['sha256']:
            raise SystemExit('Input checksum mismatch: '+item['name'])
    return contents

def analyze(raw):
    read=lambda name:json.loads(raw[name])
    source=read('source-contexts.json')
    nodes={};paths={}
    def visit(node,path):
        if isinstance(node,list):
            for item in node:visit(item,path)
            return
        identifier=node['persistent_id'];path=path+[identifier]
        nodes[identifier]=node;paths[identifier]=path
        visit(node.get('children',{}).get('annotation_node',[]),path)
    visit(read('PTHR23115-tree.json')['search']['tree_topology']['annotation_node'],[])
    leaves=[n for n,v in nodes.items() if 'UniProtKB=Q05639' in v.get('node_name','')]
    if len(leaves)!=1:raise ValueError('Target tree leaf is not unique')
    leaf=leaves[0];path=paths[leaf]
    msa=read('PTHR23115-familymsa.json')['search']['MSA_list']['sequence_info']
    seqs={x['persistent_id']:x['sequence'] for x in msa}
    official=read('UniProt-Q05639.json')['sequence']['value']
    ungapped=re.sub('[^A-Za-z]','',seqs[leaf]).upper()
    if ungapped!=official:raise ValueError('Target MSA is not the official sequence')
    ibd=[line.split('\t') for line in raw['IBD.gaf'].decode().splitlines() if line and not line.startswith('!')]
    imported_terms={x['term']['id'] for x in source}
    effective=[x for x in ibd if x[1] in path and x[6]=='IBD' and x[4] in imported_terms]
    losses=[x for x in ibd if x[1] in path and x[6] in ['IRD','IKR']]
    paint={'target_leaf':leaf,'path':path,'node_count':len(nodes),'msa_rows':len(msa),'alignment_width':len(seqs[leaf]),'target_length':len(official),'target_msa_exact':True,'effective_ibds':effective,'loss_annotations_on_target_path':losses}
    lines=[s.split('\t') for s in raw['IntAct-Q05639.mitab'].decode().splitlines() if s and not s.startswith('#')]
    def rogid(accession):
        u=read('UniProt-'+accession+'.json');seq=u['sequence']['value'];taxon=u['organism']['taxonId']
        return {'accession':accession,'taxon':taxon,'length':len(seq),'sequence_sha256':hashlib.sha256(seq.encode()).hexdigest(),'rogid':base64.b64encode(hashlib.sha1(seq.encode()).digest()).decode().rstrip('=')+str(taxon)}
    pairs=[]
    for i,annotation in enumerate(source):
        if annotation['term']['id'] not in ['GO:0005515','GO:0019901']:continue
        partners=[s.split(':',1)[1] for s in annotation.get('supporting_entities',[]) if s.startswith('UniProtKB:')]
        if len(partners)!=1:raise ValueError('Binding source does not identify one partner')
        partner=partners[0];pmid=annotation['original_reference_id'].split(':')[-1];records=[]
        for k,row in enumerate(lines):
            if 'pubmed:'+pmid not in row[8].split('|') or {row[0],row[1]}!={'uniprotkb:Q05639','uniprotkb:'+partner}:continue
            checks=[]
            for side in [0,1]:
                c=rogid(row[side].split(':',1)[1]);c['literal_rogid']=row[32+side]
                c['matches']='rogid:'+c['rogid'] in row[32+side].split('|');checks.append(c)
            ids=re.findall(r'EBI-\d+',row[13])
            records.append({'record_index_zero_based':k,'id_a':row[0],'id_b':row[1],'method':row[6],'publication':row[8],'taxon_a':row[9],'taxon_b':row[10],'interaction_type':row[11],'identifiers':row[13],'public_urls':['https://www.ebi.ac.uk/intact/interaction/'+v for v in ids],'expansion':row[15],'roles':row[16:20],'negative':row[35],'feature_a':row[36],'feature_b':row[37],'reference_sequence_checks':checks})
        pairs.append({'row':i,'partner':partner,'source':annotation['original_reference_id'],'records':records})
    cx={k:v for item in read('40205054-apms-network.json') for k,v in item.items()};nn={n['@id']:n for n in cx['nodes']}
    apms=[]
    for edge in cx['edges']:
        names={nn[edge['s']]['n'],nn[edge['t']]['n']}
        if names in [{'EEF1A2','TTLL12'},{'EEF1A2','ABTB1'}]:
            apms.append({'edge':edge,'source':nn[edge['s']],'target':nn[edge['t']],'attributes':[a for a in cx['edgeAttributes'] if a['po']==edge['@id']]})
    donors=[]
    for name in sorted(raw):
        if name not in ['QuickGO-P62631.json','QuickGO-Q71V39.json','QuickGO-P68104.json']:continue
        acc=name[8:-5];q=read(name);u=read('UniProt-'+acc+'.json')
        if len(q['results'])!=q['numberOfHits']:raise ValueError('Incomplete donor query: '+acc)
        donor_leaves=[n for n,v in nodes.items() if 'UniProtKB='+acc in v.get('node_name','')]
        donors.append({'accession':acc,'organism':u['organism'],'genes':u.get('genes'),'matching_current_donor_records':[x for x in q['results'] if x['goId'] in imported_terms],'alignment':[{'leaf':n,'sequence_exact':re.sub('[^A-Za-z]','',seqs[n]).upper()==u['sequence']['value']} for n in donor_leaves if n in seqs]})
    partners=[]
    for acc in sorted({p['partner'] for p in pairs}):
        u=read('UniProt-'+acc+'.json')
        partners.append({'accession':acc,'organism':u['organism'],'genes':u.get('genes'),'sequence_length':len(u['sequence']['value']),'classification_records':[x for x in u.get('comments',[]) if x['commentType'] in ['FUNCTION','CATALYTIC ACTIVITY','CAUTION','SIMILARITY']]})
    return {'target':'Q05639','source_rows':len(source),'paint':paint,'raw_intact_records':len(lines),'pairs':pairs,'donors':donors,'partner_classes':partners,'apms_edges':apms,'scope':'Database reference sequences, curated pair records and AP-MS coassociations; not experimental insert sequencing or proof of direct contact for every edge.'}

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--input-dir',type=Path);parser.add_argument('--output',type=Path,required=True);args=parser.parse_args()
    result=analyze(load_inputs(args.input_dir));args.output.write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n')
    print('PASS: raw-derived source joins for',result['source_rows'],'rows;',len(result['pairs']),'binding contexts;',len(result['paint']['effective_ibds']),'ancestral IBDs.')
if __name__=='__main__':main()
