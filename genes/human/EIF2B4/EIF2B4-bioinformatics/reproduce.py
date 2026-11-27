"""Replay EIF2B4 saved database inputs; no network, verdicts or article text."""
from pathlib import Path
import argparse,base64,csv,hashlib,json,re,tempfile,zipfile
RAW=None
ID_A,ID_B,METHOD,REFERENCE=0,1,6,8
TAXON_A,TAXON_B,INTERACTION_TYPE,INTERACTION_ID=9,10,11,13
COMMENT,HOST,ROGID_A,ROGID_B,NEGATIVE,FEATURE_A,FEATURE_B=27,28,32,33,35,36,37
def need(value,message):
    if not value:raise ValueError(message)
def load(path):return json.loads(Path(path).read_text())
J=load
def digest(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def pin(path):return {'path':Path(path).name,'sha256':digest(path)}

def derive_interactions():
    seed = RAW / 'normal-source-objects.json'
    doc = {'existing_annotations': load(seed)}
    records = []
    with (RAW / 'IntAct-Q9UI10.tsv').open() as handle:
        for line, fields in enumerate(csv.reader(handle, delimiter='\t'), 1):
            if not fields or fields[0].startswith('#'):
                continue
            need(len(fields) >= 42, 'Truncated MITAB row ' + str(line))
            records.append({
                'line': line, 'fields': fields,
                'participants': [fields[ID_A], fields[ID_B]],
                'method': fields[METHOD], 'reference': fields[REFERENCE],
                'taxa': [fields[TAXON_A], fields[TAXON_B]],
                'interaction_type': fields[INTERACTION_TYPE],
                'interaction_id': fields[INTERACTION_ID],
                'comment': fields[COMMENT], 'host': fields[HOST],
                'reference_ROGIDs': [fields[ROGID_A], fields[ROGID_B]],
                'negative': fields[NEGATIVE],
                'assayed_features': [fields[FEATURE_A], fields[FEATURE_B]],
            })
    partners = {}
    for path in sorted(RAW.glob('UniProt-*.json')):
        if path.name.endswith('.receipt.json'):
            continue
        u = load(path)
        sequence, taxon = u['sequence']['value'], u['organism']['taxonId']
        rog = base64.b64encode(hashlib.sha1(sequence.encode()).digest()).decode().rstrip('=') + str(taxon)
        partners[u['primaryAccession']] = dict(
            pin=pin(path), taxon=taxon, genes=u.get('genes', []),
            name=u.get('proteinDescription'), sequence=sequence, length=len(sequence),
            reference_ROGID=rog,
            functions=[c for c in u.get('comments', []) if c['commentType'] == 'FUNCTION'],
            features=u.get('features', []),
            comments=[c for c in u.get('comments', []) if c['commentType'] in
                      ['ALTERNATIVE PRODUCTS', 'SUBUNIT', 'CATALYTIC ACTIVITY', 'DOMAIN']])
    fasta = RAW / 'P40337-2.fasta'
    sequence = ''.join(fasta.read_text().splitlines()[1:])
    partners['P40337-2'] = dict(pin=pin(fasta), taxon=9606, length=len(sequence),
        sequence=sequence,
        reference_ROGID=base64.b64encode(hashlib.sha1(sequence.encode()).digest()).decode().rstrip('=')+'9606',
        feature_parent='P40337', isoform_sequence_only=True)
    joins = []
    for index, annotation in enumerate(doc['existing_annotations']):
        if annotation['term']['id'] != 'GO:0005515':
            continue
        reference = annotation['original_reference_id'].replace('PMID:', 'pubmed:')
        wanted = {s[len('UniProtKB:'):] for s in annotation.get('supporting_entities', [])
                  if s.startswith('UniProtKB:')}
        selected = []
        for record in records:
            if reference not in record['reference'].split('|'):
                continue
            ids = [f.split(':', 1)[-1] for f in record['participants']]
            if 'Q9UI10' not in ids:
                continue
            target_side = ids.index('Q9UI10')
            if wanted and ids[1-target_side] not in wanted:
                continue
            checks = []
            for side, accession in enumerate(ids):
                if accession not in partners:
                    continue
                expected = partners[accession]['reference_ROGID']
                observed = record['reference_ROGIDs'][side]
                checks.append(dict(side=side, accession=accession, expected=expected,
                    observed=observed, matches=expected in observed,
                    scope='Curated reference sequence only; not proof of assayed insert length.'))
            selected.append(dict(**record, sequence_checks=checks))
        joins.append(dict(index=index, source={k:v for k,v in annotation.items() if k != 'review'},
                          expected_partners=sorted(wanted), records=selected))
    return dict(input=pin(RAW/'IntAct-Q9UI10.tsv'), seed=pin(seed),
                all_records=len(records), joins=joins, partners=partners)


def derive_contexts():
    raw=RAW; u=load(raw/'UniProt-Q9UI10.json')
    funfams={x['id'] for x in u['uniProtKBCrossReferences'] if x['database']=='FunFam'}
    rules=[]
    for ident in ['ARBA00028188','ARBA00088579','ARBA00026561','ARBA00029247']:
        p=raw/f'{ident}.json';d=load(p); matches=[]
        for i,c in enumerate(d['mainRule']['conditionSets']):
            if any(f in json.dumps(c) for f in funfams): matches.append({'condition_set_index':i,'conditions':c})
        rules.append(dict(id=ident,input=pin(p),matching_condition_sets=matches,annotations=d['mainRule']['annotations'],relation_scope='The literal rule conclusion is retained; no unexposed source relation is inferred.'))
    re={};sources=[]
    for n in [72670,72722,72526,72528,72529,72521]:
        p=raw/f'Reactome-{n}.json'
        re[n]=load(p);sources.append(pin(p))
    projection={}
    for n,d in re.items():
        projection[str(n)]={k:d[k] for k in ['dbId','stId','displayName','speciesName','compartment','input','output','catalystActivity','physicalEntity','hasComponent','activity','startCoordinate','endCoordinate'] if k in d}
    target=re[72521]
    projection['72521']['referenceEntity']={k:target['referenceEntity'][k] for k in ['identifier','databaseName','sequenceLength','checksum']}
    if target['referenceEntity']['identifier']!='Q9UI10' or target['species']['taxId']!='9606':raise ValueError('Target identity mismatch')
    if not any(x['dbId']==72521 for x in re[72526]['hasComponent']):raise ValueError('No literal delta component')
    q=load(raw/'UniProt-Q53XC2.json');b=load(raw/'UniProt-P49770.json');v=load(raw/'UniProt-P40337.json')
    fasta=''.join((raw/'P40337-2.fasta').read_text().splitlines()[1:]);seq=v['sequence']['value']
    features=[x for x in v['features'] if x.get('featureId')=='VSP_004488']
    if len(features)!=1:raise ValueError('VHL feature unresolved')
    f=features[0];start=f['location']['start']['value'];end=f['location']['end']['value']
    reconstructed=seq[:start-1]+seq[end:]
    if reconstructed!=fasta:raise ValueError('VHL isoform sequence mismatch')
    return dict(rules=rules,reactome_sources=sources,reactome=projection,partner_sequence_scope={
        'Q53XC2_equals_P49770':q['sequence']['value']==b['sequence']['value'],
        'beta_lengths':[q['sequence']['length'],b['sequence']['length']],
        'P40337-2_length':len(fasta),'P40337-2_deleted_canonical_interval':[start,end],
        'P40337-2_exact_FASTA_reconstruction':True,
        'limit':'Reference entity identity does not authenticate assayed insert length or partner catalytic activity.'})

def derive_propagation():
    paths={p.name:p for p in RAW.iterdir() if p.is_file()}
    u=J(paths['UniProt-Q9UI10.json']);rat=J(paths['UniProt-Q63186.json']);tree=J(paths['PTHR10233-treeinfo.json'])['search']['tree_topology']['annotation_node'];msa=J(paths['PTHR10233-msa.json'])['search']['MSA_list']['sequence_info']
    nodes=[]
    def walk(value,path):
     if isinstance(value,dict):
      here=path+[value['persistent_id']] if 'persistent_id' in value else path
      if 'persistent_id' in value:nodes.append((here,value))
      for child in value.values():
       if isinstance(child,(dict,list)):walk(child,here)
     elif isinstance(value,list):
      for child in value:walk(child,path)
    walk(tree,[])
    targets=[(p,n) for p,n in nodes if n.get('tree_node_type')=='LEAF' and re.search(r'UniProtKB=Q9UI10(?:\||$)',n.get('node_name',''))]
    need(len(targets)==1,'Exactly one target leaf');path,target=targets[0];node='PTN000027922';need(node in path,'Named ancestor on target path')
    seqs=[r for r in msa if r['persistent_id']==target['persistent_id']];need(len(seqs)==1,'Exactly one target alignment');seq=re.sub(r'[-.]','',seqs[0]['sequence']).upper()
    need(u['primaryAccession']=='Q9UI10' and u['organism']['taxonId']==9606,'Human target identity');need(seq==u['sequence']['value'],'Exact target MSA equality')
    ibds=[]
    for n,line in enumerate(paths['IBD.gaf'].read_text().splitlines(),1):
     c=line.split('\t')
     if len(c)>=15 and c[1] in path:ibds.append({'line':n,'fields':c})
    normal=J(paths['normal-source-objects.json']);rows=[]
    for i,a in enumerate(normal):
     if a['evidence_type']=='IBA':
      ancestral=[e.removeprefix('PANTHER:') for e in a.get('supporting_entities',[]) if e.startswith('PANTHER:PTN')]
      records=[r for r in ibds if r['fields'][1] in ancestral and r['fields'][4]==a['term']['id']]
      rows.append({'normal_source_index':i,'source':a,'named_nodes':ancestral,'all_named_nodes_on_path':all(n in path for n in ancestral),'matching_literal_records':records})
    q=J(paths['Q63186-QuickGO-page1.json']);need(q['numberOfHits']==len(q['results']) and q['pageInfo']['total']==1,'Complete saved donor query')
    need(rat['primaryAccession']=='Q63186' and rat['organism']['taxonId']==10116,'Rat identity')
    terms=['GO:0031369','GO:0009408','GO:0009749','GO:0043434'];donors=[]
    for term in terms:
     records=[{'raw_result_index':i,'record':r} for i,r in enumerate(q['results']) if r['goId']==term]
     donors.append({'term':term,'exact_records':records,'reference_ids':sorted({r['record']['reference'] for r in records})})
    result={'scope':'Mechanical saved-source reconstruction; no annotation decisions or original-body assessment.','target':{'accession':u['primaryAccession'],'taxon':u['organism']['taxonId'],'tree_node':target['persistent_id'],'tree_name':target['node_name'],'sequence_length':len(seq),'sequence_sha256':hashlib.sha256(seq.encode()).hexdigest(),'official_sequence_exact':True},'family':{'nodes':len(nodes),'msa_sequences':len(msa),'ancestral_path':path,'requested_ancestor':node,'requested_ancestor_records':[r for r in ibds if r['fields'][1]==node],'full_path_records':ibds,'full_path_negated_records':[r for r in ibds if 'NOT' in r['fields'][3].split('|')],'IBD_sha256':hashlib.sha256(paths['IBD.gaf'].read_bytes()).hexdigest()},'normal_IBA_joins':rows,'rat_donor':{'accession':'Q63186','taxon':10116,'official_length':rat['sequence']['length'],'query_records':q['numberOfHits'],'exact_term_joins':donors},'limits':['The path-level absence statement is limited to the complete saved IBD snapshot and this target path.','Literal extant evidence sources are not counted as evidence quality; target self-evidence remains intact.','QuickGO source references are a provenance map, not independent verification of their original experiments.','Canonical target sequence equality does not establish natural alternative-product functional equivalence.']}
    return result


def derive():
    return {'interactions':derive_interactions(),'contexts':derive_contexts(),'propagation':derive_propagation()}
def validate(folder,manifest):
    for entry in manifest['inputs']:
        p=folder/entry['name']
        need(p.is_file() and p.stat().st_size==entry['bytes'] and digest(p)==entry['sha256'],'Input mismatch: '+entry['name'])
def main():
    global RAW
    here=Path(__file__).resolve().parent
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--saved-dir',type=Path,help='Directory containing all exact manifest input filenames')
    parser.add_argument('--output',type=Path,required=True)
    parser.add_argument('--check',type=Path,help='Compare full derived result with a saved result')
    args=parser.parse_args();manifest=load(here/'source-manifest.json')
    with tempfile.TemporaryDirectory(prefix='eif2b4-evidence-') as temporary:
        if args.saved_dir:RAW=args.saved_dir
        else:
            RAW=Path(temporary);archive=here/manifest['archive']['path']
            need(digest(archive)==manifest['archive']['sha256'],'Archive hash mismatch')
            with zipfile.ZipFile(archive) as z:
                need(set(z.namelist())=={r['name']for r in manifest['inputs']},'Archive member boundary')
                for name in z.namelist():
                    need(Path(name).name==name,'Unsafe member name');(RAW/name).write_bytes(z.read(name))
        validate(RAW,manifest);result=derive()
        if args.check:need(result==load(args.check),'Derived result mismatch')
        args.output.write_text(json.dumps(result,indent=2)+'\n')
        print(json.dumps({'status':'PASS','inputs':len(manifest['inputs']),'interaction_records':result['interactions']['all_records'],'PAINT_nodes':result['propagation']['family']['nodes'],'rat_records':result['propagation']['rat_donor']['query_records']}))
if __name__=='__main__':main()
