"""Recompute EGLN1 database joins and supplementary measurements from verified inputs."""
from pathlib import Path
import argparse,hashlib,io,json,re,tarfile,zipfile
BASE=Path(__file__).resolve().parent

def require(test,message):
    if not test:raise ValueError(message)

def sha(data):return hashlib.sha256(data).hexdigest()

def load_inputs(archive,manifest):
    data=archive.read_bytes();require(sha(data)==manifest['archive_sha256'],'Input archive SHA256 mismatch')
    expected={x['name']:x for x in manifest['inputs']};out={}
    with tarfile.open(fileobj=io.BytesIO(data),mode='r:gz')as tar:
        require({x.name for x in tar.getmembers()}==set(expected),'Archive membership mismatch')
        for member in tar.getmembers():
            require(member.isfile(),'Non-file archive member')
            body=tar.extractfile(member).read();r=expected[member.name]
            require(len(body)==r['bytes']and sha(body)==r['sha256'],'Input mismatch '+member.name)
            out[member.name]=body
    return out

def project_database(inputs,config):
    j=lambda name:json.loads(inputs[name]);target=config['target'];u=j('UniProt-'+target+'.json');seq=u['sequence']['value'];rows=config['source_assertions']
    tree=j('PTHR12907-tree.json')['search']['tree_topology']['annotation_node'];nodes={};paths={}
    def descend(n,parents):
        p=n['persistent_id'];nodes[p]=n;paths[p]=parents+[p]
        for child in n.get('children',{}).get('annotation_node',[]):descend(child,paths[p])
    descend(tree,[])
    leaves=[p for p,n in nodes.items()if 'UniProtKB='+target in n.get('node_name','').split('|')];require(len(leaves)==1,'Unique target leaf')
    leaf=leaves[0];msa={x['persistent_id']:x['sequence']for x in j('PTHR12907-familymsa.json')['search']['MSA_list']['sequence_info']};a=msa[leaf]
    require(re.sub('[^A-Za-z]','',a).upper()==seq,'Canonical MSA identity')
    positions={};p=0
    for col,aa in enumerate(a):
        if aa.isalpha():p+=1;positions[p]=col
    alignment=[]
    for acc in config['alignment_accessions']:
        for node,n in nodes.items():
            if 'UniProtKB='+acc in n.get('node_name','').split('|'):
                alignment.append({'accession':acc,'node':node,'columns_1based':[positions[x]+1 for x in config['metal_positions']],'residues':[msa[node][positions[x]]for x in config['metal_positions']]})
    ibd=[]
    for n,line in enumerate(inputs['IBD.gaf'].decode().splitlines(),1):
        c=line.split('\t')
        if len(c)>8 and c[1]in paths[leaf]:ibd.append({'line':n,'node':c[1],'qualifier':c[3],'term':c[4],'evidence':c[6],'donors':c[7].split('|')})
    interactions=[];mitab=inputs['IntAct-Q9GZT9.mitab'].decode().splitlines()
    fields={'id_a':0,'id_b':1,'method':6,'reference':8,'taxon_a':9,'taxon_b':10,'interaction_type':11,'interaction_id':13,'confidence':14,'expansion':15,'role_a':18,'role_b':19,'host':28,'negative':35,'feature_a':36,'feature_b':37}
    for index,row in enumerate(rows):
        if row['term']['id']!='GO:0005515':continue
        pm=row['original_reference_id'].split(':')[-1];partners=row.get('supporting_entities',[]);records=[]
        for n,line in enumerate(mitab,1):
            c=line.split('\t')
            if len(c)<42 or 'pubmed:'+pm not in c[8]:continue
            if not any(x.replace('UniProtKB:','uniprotkb:')in c[0]+'|'+c[1]for x in partners):continue
            if 'uniprotkb:'+target not in c[0]+'|'+c[1]:continue
            records.append({'line':n,**{k:c[v]for k,v in fields.items()}})
        interactions.append({'row':index,'reference':row['original_reference_id'],'partners':partners,'records':records})
    objects={int(n.split('-')[1].split('.')[0]):json.loads(b)for n,b in inputs.items()if n.startswith('Reactome-')}
    leafobj=objects[config['reactome_target']];require(leafobj['referenceEntity']['identifier']==target,'Reactome target identity');routes=[]
    def trace(node,path):
        if node==config['reactome_target']:routes.append(path);return
        if node not in objects:return
        for edge in ['input','output','catalystActivity','physicalEntity','hasComponent','hasMember']:
            values=objects[node].get(edge,[]);values=values if isinstance(values,list)else[values]
            for value in values:
                child=value.get('dbId')if isinstance(value,dict)else value
                if isinstance(child,int)and child not in [x['id']for x in path]:trace(child,path+[{'edge':edge,'id':child}])
    for root in config['reactome_roots']:trace(root,[{'id':root}])
    entity=j('RCSB-polymer_entity-5V18-1.json');pseq=entity['entity_poly']['pdbx_seq_one_letter_code_can'];blocks=[]
    for b in entity['rcsb_polymer_entity_align'][0]['aligned_regions']:
        left=pseq[b['entity_beg_seq_id']-1:b['entity_beg_seq_id']-1+b['length']];right=seq[b['ref_beg_seq_id']-1:b['ref_beg_seq_id']-1+b['length']]
        require(left==right,'Deposited target alignment');blocks.append({**b,'exact':True})
    products=[]
    for section in u['comments']:
        if section['commentType']!='ALTERNATIVE PRODUCTS':continue
        for iso in section['isoforms']:
            product=seq;features=[next(f for f in u['features']if f.get('featureId')==sid)for sid in iso.get('sequenceIds',[])]
            for f in sorted(features,key=lambda x:x['location']['start']['value'],reverse=True):
                product=product[:f['location']['start']['value']-1]+f.get('alternativeSequence',{}).get('alternativeSequences',[''])[0]+product[f['location']['end']['value']:]
            products.append({'id':iso['isoformIds'][0],'name':iso['name']['value'],'length':len(product),'sequence_sha256':sha(product.encode()),'sequenceIds':iso.get('sequenceIds',[])})
    donors=[]
    for name,body in inputs.items():
        if not name.startswith('QuickGO-'):continue
        d=json.loads(body)
        for record in d.get('results',[]):
            if record.get('goEvidence')in ['EXP','IDA','IPI','IMP','IGI','IEP','HTP','HDA','HMP','HGI','HEP']:
                donors.append({'record_file':name,'record':record})
    return {'target':target,'products':products,'paint':{'target_leaf':leaf,'node_count':len(nodes),'path':paths[leaf],'IBD_records':ibd,'metal_alignment':alignment},'interactions':interactions,'reactome':{'roots':config['reactome_roots'],'target':config['reactome_target'],'reference':leafobj['referenceEntity']['identifier'],'coordinates':[leafobj['startCoordinate'],leafobj['endCoordinate']],'compartments':leafobj['compartment'],'paths':routes},'structure':{'model':'5V18','entity':1,'aligned_blocks':blocks,'nonmapped_prefix':pseq[:min(b['entity_beg_seq_id']for b in blocks)-1],'metal':j('RCSB-nonpolymer_entity-5V18-4.json')},'experimental_donor_records':donors,'interpro':j('IPR006620.json'),'ARBA_available_rule':j('ARBA00098150-query.json')}

def project_pdz(path,manifest,inputs,database):
    try:import openpyxl
    except ImportError as e:raise RuntimeError('Install openpyxl from requirements.txt to replay the workbook')from e
    spec=manifest['external_supplement'];body=path.read_bytes();require(sha(body)==spec['sha256'],'PDZ supplement SHA256 mismatch')
    with zipfile.ZipFile(io.BytesIO(body))as archive:
        workbook=archive.read(spec['workbook_member']);require(sha(workbook)==spec['workbook_sha256'],'Workbook SHA256 mismatch')
    w=openpyxl.load_workbook(io.BytesIO(workbook),read_only=True,data_only=True);found=[]
    for n,values in enumerate(w[spec['sheet']].iter_rows(max_col=36,values_only=True),1):
        if len(values)>2 and values[2]==database['target']:
            found.append({'row':n,'values':[[i,v]for i,v in enumerate(values)if v is not None]})
    w.close();joins=[];positive=[];target_seq=json.loads(inputs['UniProt-'+database['target']+'.json'])['sequence']['value']
    for pair in database['interactions']:
        if pair['reference']!='PMID:36115835':continue
        require(len(pair['partners'])==1,'Single imported PDZ partner');acc=pair['partners'][0].split(':')[-1];u=json.loads(inputs['UniProt-'+acc+'.json'])
        names=[v['value']for gene in u['genes']for key in ['geneName','synonyms']for v in (gene.get(key,[])if isinstance(gene.get(key,[]),list)else[gene[key]])]
        matches=[]
        for record in found:
            v=dict(record['values']);domain=v[0];base=domain.rsplit('_',1)[0]if re.search(r'_\d+$',domain)else domain
            if base.casefold()not in {s.casefold()for s in names}:continue
            item={'table_row':record['row'],'domain':domain,'BI':v.get(12),'pKd':v.get(16),'method':v.get(33),'replicates':v.get(11),'assumed_Kd_microM':v.get(15)};matches.append(item)
            if isinstance(v.get(12),(int,float))and v[12]>0.05 and isinstance(v.get(16),(int,float))and v[16]>0:
                number=int(domain.rsplit('_',1)[1]);feature=next(f for f in u['features']if f['type']=='Domain'and f['description']==f'PDZ {number}');literal=[]
                for r in pair['records']:
                    side='a'if r['id_a'].split(':')[-1]==acc else'b'
                    for start,end in re.findall(r'(\d+)-(\d+)',r['feature_'+side]):
                        if int(start)<=feature['location']['start']['value']and int(end)>=feature['location']['end']['value']:literal.append(r['interaction_id'])
                require(v[3]==target_seq[-len(v[3]):],'Target C-terminal peptide')
                positive.append({'row':pair['row'],'accession':acc,'taxon':u['organism']['taxonId'],'domain':domain,'measurement':item,'official_domain':feature,'matching_IntAct_records':literal})
        joins.append({'row':pair['row'],'accession':acc,'official_names':names,'measurements':matches})
    return {'target_measurements':found,'imported_partner_joins':joins,'positive_imported_partners':positive,'all_positive_domains':[dict(r['values'])[0]for r in found if isinstance(dict(r['values']).get(16),(int,float))and dict(r['values'])[16]>0],'limits':'BI is thresholded at 0.05; pKd is estimated where quantitative. Below-threshold measurements do not demonstrate nonbinding. Gene/domain name joins do not authenticate insert sequence or natural isoform.'}

def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--inputs',type=Path,default=BASE/'inputs.tar.gz');ap.add_argument('--pdz-supplement',type=Path,required=True,help='Authentic PMID36115835 supplementary ZIP; not bundled. See fetch_supplement.py.');ap.add_argument('--check',action='store_true');ap.add_argument('--output',type=Path);args=ap.parse_args()
    manifest=json.loads((BASE/'input-manifest.json').read_text());config=json.loads((BASE/'config.json').read_text());inputs=load_inputs(args.inputs,manifest);result=project_database(inputs,config);result['pdz']=project_pdz(args.pdz_supplement,manifest,inputs,result)
    if args.check:require(result==json.loads((BASE/'results.json').read_text()),'Recomputed results differ')
    if args.output:args.output.write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n')
    print(json.dumps({'status':'PASS','inputs':len(inputs),'products':len(result['products']),'source_binding_contexts':len(result['interactions']),'PDZ_measurements':len(result['pdz']['target_measurements']),'PDZ_positive_domains':len(result['pdz']['all_positive_domains']),'PDZ_positive_imported_partners':len(result['pdz']['positive_imported_partners']),'literal_positive_IntAct_domains':sum(bool(x['matching_IntAct_records'])for x in result['pdz']['positive_imported_partners']),'Reactome_paths':len(result['reactome']['paths'])}))
if __name__=='__main__':main()
