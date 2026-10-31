#!/usr/bin/env python3
"""Replay saved database evidence offline. Does not decide biological annotation actions."""
from pathlib import Path, PurePosixPath
import argparse,collections,csv,hashlib,importlib.util,io,json,re,stat,zipfile
D=Path(__file__).resolve().parent

def require(value,message):
    if not value: raise ValueError(message)

def digest(data):return hashlib.sha256(data).hexdigest()

def load_inputs():
    manifest=json.loads((D/'inputs.json').read_text())
    archive=D/manifest['archive']
    require(archive.is_file(),'Missing database-inputs.zip; keep it beside this script.')
    require(digest(archive.read_bytes())==manifest['sha256'],'Archive SHA256 mismatch')
    with zipfile.ZipFile(archive)as z:
        info=z.infolist();names=[x.filename for x in info]
        require(len(names)==len(set(names)) and set(names)==set(manifest['members']),'Archive member inventory mismatch')
        require(sum(x.file_size for x in info)<200_000_000,'Archive expansion limit exceeded')
        data={}
        for x in info:
            p=PurePosixPath(x.filename)
            require(not p.is_absolute() and '..'not in p.parts and '\\'not in x.filename,'Unsafe archive path')
            require(not stat.S_ISLNK(x.external_attr>>16),'Archive symlink not permitted')
            b=z.read(x);record=manifest['members'][x.filename]
            require(len(b)==record['bytes'] and digest(b)==record['sha256'],'Input hash mismatch: '+x.filename)
            data[x.filename]=b
    return data

def derive(data):
    text=lambda n:data[n].decode('utf-8')
    read=lambda n:json.loads(text(n))
    sources=read('inputs/source-objects.json')
    goa=list(csv.DictReader(io.StringIO(text('inputs/EIF3F-goa.tsv')),delimiter='\t'))
    def key(term,evidence,reference,qualifier,entities,accession):
        q=qualifier.split('|')
        return(term,evidence,reference,next((x for x in q if x!='NOT'),''),tuple(sorted(set(entities)-{''})),'NOT'in q,accession if '-'in accession else None)
    def sk(x):return(x['term']['id'],x['evidence_type'],x['original_reference_id'],x.get('qualifier',''),tuple(sorted(x.get('supporting_entities',[]))),x.get('negated',False),x.get('isoform'))
    by=collections.defaultdict(list)
    for i,x in enumerate(goa):by[key(x['GO TERM'],x['GO EVIDENCE CODE'],x['REFERENCE'],x['QUALIFIER'],x['WITH/FROM'].split('|'),x['GENE PRODUCT ID'])].append(i)
    require(set(by)==set(map(sk,sources)),'GOA/source full-context mismatch')
    joins=[{'source_index':i,'goa_data_rows_0based':by[sk(x)]}for i,x in enumerate(sources)]
    require(all(x['term']['label']==goa[j]['GO NAME']for x in sources for j in by[sk(x)]),'GO labels differ from source')
    mitab=[l.split('\t')for l in text('owner/IntAct-O00303.tsv').splitlines()]
    pairs=[]
    for i,x in enumerate(sources):
        if x['term']['id']not in ['GO:0005515','GO:0042802']:continue
        partners=[z.split(':',1)[1]for z in x.get('supporting_entities',[])if z.startswith('UniProtKB:')]
        ids=['uniprotkb:'+p for p in partners];pm=x['original_reference_id'].split(':')[1]
        records=[]
        for k,f in enumerate(mitab):
            require(len(f)>=38,'Malformed MITAB row')
            match='pubmed:'+pm in f[8].split('|')and'uniprotkb:O00303'in f[:2]and (all(z=='uniprotkb:O00303'for z in f[:2])if x['term']['id']=='GO:0042802'else any(z in ids for z in f[:2]))
            if match:records.append({'line':k+1,'id_a':f[0],'id_b':f[1],'method':f[6],'publication':f[8],'species_a':f[9],'species_b':f[10],'interaction_type':f[11],'host':f[28],'negative':f[35],'feature_a':f[36],'feature_b':f[37],'source_locator':f[27]})
        identity={}
        for a in partners:
            name='inputs/UniProt-O00303.json'if a=='O00303'else'owner/UniProt-'+a.split('-')[0]+'.json'
            if name in data:
                u=read(name);identity[a]={'accession':u['primaryAccession'],'organism':u['organism'],'genes':u.get('genes'),'length':u['sequence']['length'],'input':name}
        pairs.append({'source_index':i,'partners':partners,'records':records,'identity':identity})
    react={int(n.split('-')[-1].split('.')[0]):read(n)for n in data if n.startswith('owner/Reactome-')}
    def paths(n,seen=()):
        if n==72540:return [[]]
        if n in seen or n not in react:return []
        out=[]
        for rel in ['input','output','hasComponent']:
            for x in react[n].get(rel,[]):
                k=x if isinstance(x,int)else x['dbId']
                for tail in paths(k,seen+(n,)):out.append([{'from':n,'relation':rel,'to':k}]+tail)
        return out
    roots=[{'root':n,'name':react[n]['displayName'],'paths':paths(n)}for n in [156808,156823,157849,72619,72621,72676,72691,72697]]
    require(all(x['paths']for x in roots),'Missing target component path')
    require(react[72540]['referenceEntity']['identifier']=='O00303','Reactome target identity')
    oc=list(csv.DictReader(io.StringIO(text('tables/OpenCell.csv'))))
    oc_hits=[{'data_row_1based':i+1,'fields':x}for i,x in enumerate(oc)if'O00303'in x['interactor_uniprot_ids'].split(';')]
    exact=[x for x in oc_hits if x['fields']['target_ensg_id']=='ENSG00000106263'];require(len(exact)==1,'OpenCell pair')
    cx=read('tables/NDEx.json');nodes={n['@id']:n for b in cx for n in b.get('nodes',[])};edges=[e for b in cx for e in b.get('edges',[])]
    f=[k for k,v in nodes.items()if v['n']=='EIF3F'];require(len(f)==1,'NDEx target')
    target_edges=[e for e in edges if f[0]in[e['s'],e['t']]];selected=[]
    for row,partner in [(81,'EIF3H'),(82,'EIF3B'),(83,'EIF3M')]:
        hits=[e for e in target_edges if {nodes[e['s']]['n'],nodes[e['t']]['n']}=={'EIF3F',partner}];require(len(hits)==1,'NDEx pair')
        selected.append({'source_index':row,'edge':hits[0],'nodes':[nodes[hits[0]['s']],nodes[hits[0]['t']]]})
    spec=importlib.util.spec_from_file_location('propagation',D/'propagation.py');p=importlib.util.module_from_spec(spec);spec.loader.exec_module(p);p.read=read;p.text=text;prop=p.compute()
    term_defs={x['id']:x for x in read('owner/GO-source-terms.json')['results']}
    return {'source_reconciliation':{'raw_records':len(goa),'distinct_contexts':len(by),'sources':len(sources),'duplicate_groups':[v for v in by.values()if len(v)>1],'joins':joins},'interactions':{'MITAB_records':len(mitab),'source_rows':len(pairs),'pairs':pairs,'scope':'Literal current IntAct joins; absent joins do not negate historical experimental assertions. Partner identity does not establish a functional subtype.'},'reactome':{'roots':roots,'target':react[72540],'scope':'Literal curated component paths, not independent biochemical experiments.'},'opencell':{'target_rows':oc_hits,'source_row80':exact,'scope':'Released positive association table; no global negative inference.'},'ndex':{'network_edges':len(edges),'target_edges':target_edges,'selected':selected,'scope':'Released positive AP-MS network, not binary interfaces.'},'propagation':prop,'source_term_definitions':term_defs}

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--write',type=Path,help='Write a new projection file; refuses an existing destination.');args=ap.parse_args()
    data=load_inputs();result=derive(data)
    if args.write:
        with args.write.open('x')as f:json.dump(result,f,indent=2,ensure_ascii=False);f.write('\n')
    else:
        expected=json.loads((D/'results.json').read_text());require(result==expected,'Derived results differ from results.json')
    print(json.dumps({'status':'PASS','inputs':len(data),'raw_GOA':result['source_reconciliation']['raw_records'],'sources':len(result['source_reconciliation']['joins']),'interaction_rows':result['interactions']['source_rows'],'MITAB_records':result['interactions']['MITAB_records'],'reactome_paths':sum(len(x['paths'])for x in result['reactome']['roots']),'tree_nodes':result['propagation']['paint-evidence.json']['tree_nodes'],'IBA_traces':len(result['propagation']['paint-evidence.json']['requested_iba_traces']),'no_network':True,'biological_actions_recomputed':False}))
if __name__=='__main__':main()
