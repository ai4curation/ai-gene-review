#!/usr/bin/env python3
"""Reproduce EML1 database joins offline, without extracting archive members."""
import argparse
import csv
import hashlib
import io
import json
from pathlib import Path, PurePosixPath
import re
import stat
import xml.etree.ElementTree as ET
import zipfile


def require(value, message):
    if not value:
        raise ValueError(message)


def digest(data):
    return hashlib.sha256(data).hexdigest()


def encoded(value):
    return (json.dumps(value, indent=2, ensure_ascii=False) + "\n").encode()


def read_inputs(root):
    config = json.loads((root / "config.json").read_text())
    inventory = json.loads((root / "inputs.json").read_text())
    archive_name = config["archive"]
    require(Path(archive_name).name == archive_name, "archive must be a local basename")
    archive = (root / archive_name).read_bytes()
    require(digest(archive) == config["archive_sha256"], "archive hash mismatch")
    members = inventory["members"]
    expected = {x["member"]: x for x in members}
    require(len(expected) == len(members), "duplicate input-manifest member")
    data = {}
    with zipfile.ZipFile(io.BytesIO(archive)) as bundle:
        infos = bundle.infolist()
        require(len(infos) == len({x.filename for x in infos}), "duplicate archive member")
        require({x.filename for x in infos} == set(expected), "archive membership mismatch")
        require(sum(x.file_size for x in infos) <= 32 * 1024 * 1024, "oversize archive")
        for item in infos:
            path = PurePosixPath(item.filename)
            require(not path.is_absolute() and all(x not in ("", ".", "..") for x in item.filename.split("/")), "unsafe member path")
            require("\\" not in item.filename and ":" not in item.filename, "unsafe member name")
            mode = item.external_attr >> 16
            require(stat.S_ISREG(mode) and not item.is_dir(), "non-regular archive member")
            require(not item.flag_bits & 1, "encrypted archive member")
            raw = bundle.read(item)
            pin = expected[item.filename]
            require(mode == pin["mode"] and len(raw) == pin["bytes"] and digest(raw) == pin["sha256"], "input integrity mismatch: " + item.filename)
            data[item.filename] = raw
    return data


def project(data):
    get = lambda name: json.loads(data[name])
    sources = get('source/source-objects.json')
    goa = list(csv.DictReader(io.StringIO(data['source/EML1-goa.tsv'].decode()), delimiter='\t'))
    def sk(x):
        return (x['term']['id'], x['evidence_type'], x['original_reference_id'], x.get('qualifier',''), tuple(sorted(x.get('supporting_entities',[]))))
    def gk(x):
        return (x['GO TERM'], x['GO EVIDENCE CODE'], x['REFERENCE'], x['QUALIFIER'], tuple(sorted(filter(None,x['WITH/FROM'].split('|')))))
    joins = [{'source_index':i,'goa_data_indices':[j for j,row in enumerate(goa) if sk(source)==gk(row)]} for i,source in enumerate(sources)]
    require(all(x['goa_data_indices'] for x in joins),'missing source context')
    require(sorted(j for x in joins for j in x['goa_data_indices'])==list(range(len(goa))),'GOA coverage or duplicate mismatch')
    human = get('official/UniProt-O00423.json')
    mouse = get('official/UniProt-Q05BC3.json')
    sequence = human['sequence']['value']
    isoforms = next(x['isoforms'] for x in human['comments'] if x['commentType']=='ALTERNATIVE PRODUCTS')
    edits = {x['featureId']:x for x in human['features'] if x['type']=='Alternative sequence'}
    products=[]
    for isoform in isoforms:
        identifier=isoform['isoformIds'][0];value=sequence
        for edit in sorted((edits[k] for k in isoform.get('sequenceIds',[])),key=lambda x:x['location']['start']['value'],reverse=True):
            start,end=edit['location']['start']['value']-1,edit['location']['end']['value'];alt=edit.get('alternativeSequence',{})
            require(not alt.get('originalSequence') or sequence[start:end]==alt['originalSequence'],'VSP preimage')
            replacements=alt.get('alternativeSequences',['']);require(len(replacements)==1,'ambiguous VSP')
            value=value[:start]+replacements[0]+value[end:]
        fasta=data['official/'+identifier+'.fasta'].decode().splitlines();require(sum(x.startswith('>') for x in fasta)==1,'FASTA cardinality')
        require(value==''.join(x.strip() for x in fasta if not x.startswith('>')),'product sequence')
        products.append({'id':identifier,'length':len(value),'sha256':digest(value.encode()),'sequence_ids':isoform.get('sequenceIds',[])})
    tree=get('database/PTHR13720-tree.json')['search']['tree_topology']['annotation_node'];nodes={};paths={}
    def walk(node,path):
        key=node['persistent_id'];require(key not in nodes,'duplicate node');nodes[key]=node;paths[key]=path+[key]
        children=node.get('children',{}).get('annotation_node',[])
        if isinstance(children,dict):children=[children]
        for child in children:walk(child,paths[key])
    walk(tree,[])
    msa={x['persistent_id']:re.sub('[^A-Za-z]','',x['sequence']).upper() for x in get('database/PTHR13720-msa.json')['search']['MSA_list']['sequence_info']}
    sequences=[]
    for accession,record in [('O00423',human),('Q05BC3',mouse)]:
        matches=[k for k,n in nodes.items() if 'UniProtKB='+accession in n.get('node_name','')];require(len(matches)==1,'reference leaf identity')
        key=matches[0];require(msa[key]==record['sequence']['value'],'MSA reference match')
        sequences.append({'accession':accession,'leaf':key,'symbol':nodes[key]['gene_symbol'],'length':len(msa[key]),'sha256':digest(msa[key].encode()),'path':paths[key]})
    human_path=sequences[0]['path'];paint=list(csv.DictReader(io.StringIO(data['database/PTHR13720-paint.tsv'].decode()),delimiter='\t'));traces=[]
    for i,source in enumerate(sources):
        if source['evidence_type']!='IBA':continue
        node=next(x.split(':',1)[1] for x in source['supporting_entities'] if x.startswith('PANTHER:'))
        rows=[x for x in paint if x['node']==node and x['go_id']==source['term']['id'] and x['evidence']=='IBD']
        require(len(rows)==1 and node in human_path,'literal IBD ancestry')
        traces.append({'source_index':i,'ibd':rows[0],'on_target_path':True})
    losses=[x for x in paint if x['node'] in human_path and (x['negated']=='true' or x['evidence'] in ['IRD','IKR'])]
    donors={}
    for accession in ['Q05BC3','O95834','Q9VUI3']:
        response=get('database/QuickGO-'+accession+'.json');rows=response['results']
        require(response['pageInfo']['total']==1 and len(rows)==response['numberOfHits'],'complete captured donor page')
        donors[accession]={'total_records':len(rows),'experimental_relevant_records':[x for x in rows if x['goId'] in {s['term']['id'] for s in sources} and x['reference'].startswith('PMID:')]}
    terms={x['id']:x for x in get('database/QuickGO-terms.json')['results']}
    ancestors={identifier:get('database/'+identifier.replace(':','')+'-ancestors-is_a.json')['results'][0]['ancestors'] for identifier in terms}
    rules={}
    for identifier in ['ARBA00044431','ARBA00043642']:
        rule=get('database/'+identifier+'.json');rules[identifier]={'condition_sets':rule['mainRule']['conditionSets'],'outputs':rule['mainRule']['annotations'],'modified':rule['modifiedDate']}
    intact=list(csv.reader(io.StringIO(data['interactions/intact-O00423-tab27.tsv'].decode()),delimiter='\t'))
    biogrid=list(csv.DictReader(io.StringIO(data['interactions/BioGRID-EML1.tab3.txt'].decode()),delimiter='\t'))
    interactions=[]
    for i,source in enumerate(sources):
        if source['term']['id']!='GO:0005515':continue
        partner=source['supporting_entities'][0].split(':',1)[1];pmid=source['original_reference_id'].split(':')[1]
        hits=[]
        for line,row in enumerate(intact,1):
            pair={row[0].lower(),row[1].lower()}
            if pair=={'uniprotkb:o00423','uniprotkb:'+partner.lower()} and 'pubmed:'+pmid in row[8].split('|'):
                require(row[35]=='false','negated interaction')
                hits.append({'line':line,'id':row[13],'method':row[6],'type':row[11],'host':row[28],'negative':row[35]})
        bg=[row for row in biogrid if {row['SWISS-PROT Accessions Interactor A'],row['SWISS-PROT Accessions Interactor B']}=={'O00423',partner} and row['Publication Source']=='PUBMED:'+pmid]
        require(hits or bg,'missing source-specific pair')
        interactions.append({'source_index':i,'partner':partner,'pmid':pmid,'IntAct':hits,'BioGRID':[{'id':x['#BioGRID Interaction ID'],'method':x['Experimental System'],'speciesA':x['Organism ID Interactor A'],'speciesB':x['Organism ID Interactor B']} for x in bg]})
    bioplex=list(csv.DictReader(io.StringIO(data['interactions/BioPlex-selected.tsv'].decode()),delimiter='\t'))
    require(all(x['Bait GeneID']=='2009' and x['Prey GeneID']=='10726' for x in bioplex) and bioplex,'BioPlex positive selected edge')
    return {'source_objects':len(sources),'normalized_goa_rows':len(goa),'joins':joins,'products':products,'reference_MSA_matches':sequences,'paint':{'captured_family_rows':len(paint),'tree_nodes':len(nodes),'IBD_traces':traces,'loss_records_on_target_path_in_captured_family_table':losses},'donors':donors,'terms':terms,'is_a_ancestors':ancestors,'microtubule_binding_is_a_tubulin_binding':'GO:0015631' in ancestors['GO:0008017'],'rules':rules,'interaction_queries':{'IntAct_records':len(intact),'BioGRID_records':len(biogrid),'source_joins':interactions,'BioPlex_selected_edges':bioplex},'limits':['Database snapshots and literal source joins only; no primary experiment or curation verdict is reproduced.','The BioPlex member is a declared positive-edge subset, not evidence of global absence.','Rule predicates are reproduced; target-specific FunFam clause matching was not independently established.','Sequence identity does not establish equal activity among natural products or identify experimental constructs.','The family-table absence of a loss on this path is limited to the captured table/version.','O95834 is human EML2; source identities are accession-based.']}


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--output',type=Path);args=parser.parse_args()
    root=Path(__file__).resolve().parent;result=encoded(project(read_inputs(root)))
    require(result==(root/'results.json').read_bytes(),'derived results differ')
    if args.output:
        with args.output.open('xb') as handle:handle.write(result)
    print(json.dumps({'status':'PASS','source_objects':json.loads(result)['source_objects'],'products':len(json.loads(result)['products']),'input_members':len(json.loads((root/'inputs.json').read_text())['members'])},sort_keys=True))

if __name__=='__main__':main()
