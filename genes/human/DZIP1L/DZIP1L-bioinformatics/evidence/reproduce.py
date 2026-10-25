#!/usr/bin/env python3
"""Recompute literal identities and source joins; no biological verdicts are encoded.
Python 3.12 standard library. All scientific query inputs are external JSON/raw files.
"""
import argparse,base64,hashlib,json,re,tarfile,xml.etree.ElementTree as ET
from html.parser import HTMLParser
from pathlib import Path

def load(p):return json.loads(p.read_text())
def digest(data):return hashlib.sha256(data).hexdigest()
def fasta(p):return ''.join(s.strip() for s in p.read_text().splitlines()if not s.startswith('>'))
class Text(HTMLParser):
    def __init__(self):super().__init__();self.parts=[]
    def handle_data(self,s):self.parts.append(s)

def inputs(folder,cache):
    manifest=load(folder/'input-manifest.json');cache.mkdir(parents=True,exist_ok=True)
    with tarfile.open(folder/'raw-inputs.tar.gz','r:gz') as archive:
        expected={x['name'] for x in manifest}
        if set(archive.getnames())!=expected:raise ValueError('Archive member mismatch')
        for member in archive.getmembers():
            if not member.isfile()or Path(member.name).name!=member.name:raise ValueError('Unsafe member')
            data=archive.extractfile(member).read();record=next(x for x in manifest if x['name']==member.name)
            if digest(data)!=record['sha256']:raise ValueError('Archive checksum: '+member.name)
            dest=cache/member.name
            if dest.exists():
                if dest.read_bytes()!=data:raise ValueError('Local input differs: '+member.name)
            else:dest.write_bytes(data)
    return manifest

def interaction_records(raw,target,queries):
    lines=[s.split('\t')for s in raw.read_text().splitlines()if s and not s.startswith('#')]
    def identity(acc):
        u=load(raw.parent/('UniProt-'+acc.split('-')[0]+'.json'))
        seq=fasta(raw.parent/(acc+'.fasta'))if '-'in acc else u['sequence']['value'];taxon=u['organism']['taxonId']
        return dict(accession=acc,length=len(seq),taxon=taxon,sequence_sha256=digest(seq.encode()),rogid=base64.b64encode(hashlib.sha1(seq.encode()).digest()).decode().rstrip('=')+str(taxon))
    out=[]
    for q in queries:
        matches=[]
        for n,r in enumerate(lines):
            participants=[x.split(':',1)[1]for x in r[:2]]
            if q['pmid']not in r[8].split('|')or set(participants)!={target,q['partner']}:continue
            checks=[]
            for side,acc in enumerate(participants):
                c=identity(acc);c['literal_rogid']=r[32+side];c['matches']='rogid:'+c['rogid']in r[32+side].split('|');checks.append(c)
            matches.append(dict(record_index=n,id_a=r[0],id_b=r[1],method=r[6],publication=r[8],taxon_a=r[9],taxon_b=r[10],interaction_type=r[11],identifiers=r[13],expansion=r[15],roles=r[16:20],negative=r[35],feature_a=r[36],feature_b=r[37],checks=checks))
        out.append(dict(query=q,records=matches))
    return dict(raw_count=len(lines),pairs=out)

def tree_records(raw,q):
    tree=load(raw/(q['family']+'-tree.json'))['search']['tree_topology']['annotation_node'];nodes=[];matches=[]
    def walk(n,path):
        p=path+[n];nodes.append(n)
        if 'UniProtKB='+q['target'] in n.get('node_name','').split('|'):matches.append(p)
        children=n.get('children',{}).get('annotation_node',[])
        for c in ([children]if isinstance(children,dict)else children):walk(c,p)
    walk(tree,[])
    if len(matches)!=1:raise ValueError('Target leaf not unique')
    path=[{k:v for k,v in n.items()if k!='children'}for n in matches[0]];ids=[x['persistent_id']for x in path]
    msas=load(raw/(q['family']+'-familymsa.json'))['search']['MSA_list']['sequence_info'];msa=[s for s in msas if s['persistent_id']==ids[-1]]
    if len(msa)!=1:raise ValueError('Target MSA row not unique')
    unaligned=re.sub('[^A-Za-z]','',msa[0]['sequence']).upper();official=load(raw/('UniProt-'+q['target']+'.json'))['sequence']['value']
    ibds=[]
    for i,s in enumerate((raw/'IBD.gaf').read_text().splitlines()):
        if s.startswith('!'):continue
        c=s.split('\t')
        if len(c)>6 and c[1]in ids:ibds.append(dict(line_zero_based=i,fields=c))
    exp={'EXP','IDA','IPI','IMP','IGI','IEP','HTP','HDA','HMP','HGI','HEP'};rows=[]
    for i,a in enumerate(q['sources']):
        if a['evidence_type']!='IBA':continue
        ptns=[x.split(':',1)[1]for x in a.get('supporting_entities',[])if x.startswith('PANTHER:PTN')]
        matching=[x for x in ibds if x['fields'][1]in ptns and x['fields'][4]==a['term']['id']]
        donors=[]
        for donor in a.get('supporting_entities',[]):
            if donor.startswith('PANTHER:'):continue
            token=donor.split(':')[-1]
            leaves=[n for n in nodes if token in n.get('node_name','')]
            if len(leaves)!=1:raise ValueError('Donor leaf not unique: '+donor)
            leaf=leaves[0];acc=leaf['node_name'].split('UniProtKB=')[-1];u=load(raw/('UniProt-'+acc+'.json'));g=load(raw/('QuickGO-'+acc+'.json'))
            if g['pageInfo']['total']!=1:raise ValueError('Incomplete donor pagination')
            records=[x for x in g['results']if x['goId']==a['term']['id']]
            donors.append(dict(original_donor=donor,leaf={k:v for k,v in leaf.items()if k!='children'},accession=acc,taxon=u['organism']['taxonId'],matching_current_donor_records=records,direct_experimental_records=[x for x in records if x['goEvidence']in exp]))
        rows.append(dict(row=i,term=a['term']['id'],node_on_target_path=all(x in ids for x in ptns),literal_ibds=matching,donors=donors))
    return dict(node_count=len(nodes),path=path,target_msa=msa[0],unaligned_length=len(unaligned),sequence_match=unaligned==official,rows=rows)

def products(raw,q):
    u=load(raw/('UniProt-'+q['target']+'.json'));canonical=u['sequence']['value'];features={x['featureId']:x for x in u['features']if x['type']=='Alternative sequence'};out=[];seqs={}
    for p in [p for c in u['comments']if c['commentType']=='ALTERNATIVE PRODUCTS'for p in c['isoforms']]:
        seq=canonical;coords=list(range(1,len(seq)+1))
        for f in sorted([features[x]for x in p.get('sequenceIds',[])],key=lambda x:x['location']['start']['value'],reverse=True):
            a=f['location']['start']['value']-1;b=f['location']['end']['value'];alt=f.get('alternativeSequence',{});replacement=alt.get('alternativeSequences',[''])[0]
            if alt.get('originalSequence') and canonical[a:b]!=alt['originalSequence']:raise ValueError('Feature reference mismatch')
            seq=seq[:a]+replacement+seq[b:];coords=coords[:a]+[None]*len(replacement)+coords[b:]
        acc=p['isoformIds'][0];seqs[acc]=seq;domains=[]
        for f in u['features']:
            if f['type']not in q['feature_types']:continue
            a=f['location']['start']['value'];b=f['location']['end']['value'];retained=[i+1 for i,v in enumerate(coords)if v is not None and a<=v<=b]
            domains.append(dict(type=f['type'],canonical_range=[a,b],complete_unchanged=len(retained)==b-a+1,product_range=[min(retained),max(retained)]if retained else None))
        out.append(dict(id=acc,length=len(seq),sequence_sha256=digest(seq.encode()),official_fasta_exact=seq==fasta(raw/(acc+'.fasta')),domains=domains,feature_ids=p.get('sequenceIds',[])))
    clones=[]
    for accession in q['archived_clones']:
        text=(raw/(accession+'.embl')).read_text();m=re.search(r'/translation="(.*?)"',text,re.S)
        if not m:raise ValueError('Missing archived translation')
        seq=re.sub(r'\s','',re.sub(r'(?m)^FT\s+','',m.group(1)));clone=re.search(r'/clone="(.*?)"',text,re.S)
        comparisons=[]
        for acc,official in seqs.items():
            comparisons.append(dict(product=acc,length_match=len(seq)==len(official),differences=[dict(position=i+1,archived=a,current=b)for i,(a,b)in enumerate(zip(seq,official))if a!=b]if len(seq)==len(official)else None))
        clones.append(dict(accession=accession,clone=clone.group(1)if clone else None,length=len(seq),comparisons=comparisons))
    return dict(products=out,archived_translation_comparisons=clones)

def hpa(raw,q):
    entry=ET.parse(raw/('HPA-'+q['gene']+'.xml')).find('.//entry')
    if entry.findtext('name')!=q['gene']or entry.find('identifier').get('id')!=q['ensembl']:raise ValueError('HPA identity mismatch')
    parser=Text();parser.feed((raw/('HPA-'+q['gene']+'-subcellular.html')).read_text());text=' '.join(' '.join(parser.parts).split())
    start=text.index('Localized to the ');summary=text[start:text.index('Main location',start)]
    locations=list(dict.fromkeys(re.findall(r'([A-Za-z][A-Za-z -]*?) \((supported|uncertain|enhanced|approved)\)',summary,re.I)))
    records=[]
    for ab in entry.findall('antibody'):
        for ce in ab.findall('.//cellExpression'):
            if ce.get('technology')!='ICC/IF':continue
            for data in ce.findall('.//data'):records.append(dict(antibody=ab.get('id'),cell_line=data.findtext('cellLine'),locations=[dict(z.attrib,text=z.text)for z in data.findall('location')],image_urls=[z.text for z in data.findall('.//imageUrl')]))
    return dict(target=q['ensembl'],summary=summary,locations=[dict(label=re.sub(r'^(?:In addition )?[Ll]ocalized to the ', '', l).strip(),reliability=s.lower())for l,s in locations],records=records)

def rules_and_classes(raw,q):
    u=load(raw/('UniProt-'+q['target']+'.json'));iprs={x['id']for x in u['uniProtKBCrossReferences']if x['database']=='InterPro'};arba=[]
    for i,a in enumerate(q['sources']):
        for source in a.get('supporting_entities',[]):
            if not source.startswith('ARBA:'):continue
            rule=load(raw/(source.split(':')[1]+'.json'));sets=[]
            for j,cs in enumerate(rule['mainRule']['conditionSets']):
                conditions=[]
                for c in cs['conditions']:
                    values=[v['value']for v in c['conditionValues']];kind=c['type']
                    hit=any(v in iprs for v in values)if kind=='InterPro id' else any(v in u['organism']['lineage']for v in values)if kind=='taxon'else None
                    if c.get('isNegative')and hit is not None:hit=not hit
                    conditions.append(dict(condition=c,matches=hit))
                sets.append(dict(index=j,conditions=conditions,all_match=all(x['matches']is True for x in conditions)))
            arba.append(dict(row=i,rule=source,condition_sets=sets,annotations=rule['mainRule']['annotations']))
    classes=[]
    for acc in q['class_accessions']:
        p=load(raw/('UniProt-'+acc+'.json'));g=raw/('QuickGO-'+acc+'.json')
        classes.append(dict(accession=acc,official_name=p['proteinDescription'],official_comments=[c for c in p['comments']if c['commentType']in ['FUNCTION','SUBUNIT','SUBCELLULAR LOCATION','CATALYTIC ACTIVITY']],matching_current_records=load(g)['results']if g.exists()else []))
    return dict(arba=arba,SL_mapping=load(raw/'UniProt-SL-0046.json'),target_locations=[c for c in u['comments']if c['commentType']=='SUBCELLULAR LOCATION'],partner_class_records=classes)

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--inputs',type=Path,default=Path('.'));ap.add_argument('--cache',type=Path,required=True);ap.add_argument('--output',type=Path,required=True);ap.add_argument('--control-target');args=ap.parse_args();q=load(args.inputs/'queries.json');manifest=inputs(args.inputs,args.cache)
    queries=[dict(row=i,partner=a['supporting_entities'][0].split(':',1)[1],pmid=a['original_reference_id'].replace('PMID:','pubmed:'))for i,a in enumerate(q['sources'])if a['term']['id']=='GO:0005515']
    if args.control_target:
        queries=[dict(row=x['row'],partner=q['target'],pmid=x['pmid'])for x in queries if x['partner']==args.control_target]
        result={'interactions':interaction_records(args.cache/('IntAct-'+q['target']+'.mitab'),args.control_target,queries)}
    else:
        result=dict(interactions=interaction_records(args.cache/('IntAct-'+q['target']+'.mitab'),q['target'],queries),paint=tree_records(args.cache,q),products=products(args.cache,q),HPA=hpa(args.cache,q),propagation_and_classes=rules_and_classes(args.cache,q))
    args.output.parent.mkdir(parents=True,exist_ok=True);args.output.write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n');print(json.dumps({'inputs':len(manifest),'matched_interactions':sum(len(x['records'])for x in result['interactions']['pairs']),'rogid_checks':sum(len(r['checks'])for x in result['interactions']['pairs']for r in x['records']),'output':str(args.output)}))
if __name__=='__main__':main()
