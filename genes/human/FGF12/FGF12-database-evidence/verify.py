"""Verify compact FGF12 source evidence; never download or write.

Default: checks included official records, target mappings and published projections.
--tree-raw / --msa-raw additionally reproduce projections from exact retained captures.
The tree capture is intentionally partial; no missing tokens are synthesized.
"""
from pathlib import Path
import argparse,csv,hashlib,json,re
D=Path(__file__).resolve().parent
H=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
J=lambda p:json.loads(Path(p).read_text())
def prefix_value(text,pos=0):
    # Parse only actual complete tokens. An unfinished container is retained as
    # partial; no missing field, token or closing delimiter is invented.
    n=len(text)
    def ws(i):
        while i<n and text[i].isspace():i+=1
        return i
    def value(i):
        i=ws(i)
        if i==n:return None,i,False
        ch=text[i]
        if ch=='"':
            try:v,j=json.decoder.scanstring(text,i+1,True);return v,j,True
            except ValueError:return None,n,False
        if ch=='{':
            out={};i=ws(i+1)
            if i<n and text[i]=='}':return out,i+1,True
            while i<n:
                assert text[i]=='"',('invalid key token',i)
                k,i,ok=value(i)
                if not ok:return out,i,False
                i=ws(i)
                if i==n:return out,i,False
                assert text[i]==':';v,i,ok=value(i+1)
                if ok or isinstance(v,(dict,list)):out[k]=v
                if not ok:return out,i,False
                i=ws(i)
                if i==n:return out,i,False
                if text[i]=='}':return out,i+1,True
                assert text[i]==',';i=ws(i+1)
            return out,i,False
        if ch=='[':
            out=[];i=ws(i+1)
            if i<n and text[i]==']':return out,i+1,True
            while i<n:
                v,i,ok=value(i)
                if ok or isinstance(v,(dict,list)):out.append(v)
                if not ok:return out,i,False
                i=ws(i)
                if i==n:return out,i,False
                if text[i]==']':return out,i+1,True
                assert text[i]==',';i=ws(i+1)
            return out,i,False
        m=re.match(r'(?:true|false|null|-?(?:0|[1-9][0-9]*)(?:\.[0-9]+)?(?:[eE][+-]?[0-9]+)?)',text[i:])
        assert m,('invalid value token',i)
        token=m.group();return json.loads(token),i+len(token),True
    return value(pos)

def derive_family_assertions(rows, path):
    """Classify every literal family row, without interpreting GO-slim summaries.

    Pair each target-path IRD with its explicit same-term positive source node.
    This is not a general PAINT implementation or a review of donor experiments.
    """
    assert len(path) == len(set(path))
    on_path = set(path)
    all_rows = []
    target_losses = []
    for i, row in enumerate(rows):
        assert row['family'] == 'PTHR11486'
        assert row['negated'] in ('true', 'false')
        all_rows.append({'TSV_index': i, 'row': row,
                         'on_target_path': row['node'] in on_path})
        if row['node'] not in on_path or row['negated'] != 'true':
            continue
        assert row['evidence'] == 'IRD'
        sources = row['seeds'].split('|')
        paired = []
        for source in sources:
            assert source.startswith('PANTHER:PTN')
            ancestor = source.split(':', 1)[1]
            assert ancestor in on_path
            assert path.index(ancestor) < path.index(row['node'])
            matches = [(j, x) for j, x in enumerate(rows)
                       if x['node'] == ancestor and x['go_id'] == row['go_id']
                       and x['evidence'] == 'IBD' and x['negated'] == 'false']
            assert len(matches) == 1
            j, positive = matches[0]
            paired.append({'source_node_CURIE': source, 'positive_IBD_TSV_index': j,
                           'positive_IBD_seeds': positive['seeds'].split('|')})
        target_losses.append({'IRD_TSV_index': i, 'go_id': row['go_id'],
                              'loss_node': row['node'], 'source_IBD_joins': paired})
    positive = [i for i, r in enumerate(rows)
                if r['node'] in on_path and r['evidence'] == 'IBD'
                and r['negated'] == 'false']
    blocked = {p['positive_IBD_TSV_index'] for n in target_losses
               for p in n['source_IBD_joins']}
    target_indices = [x['TSV_index'] for x in all_rows if x['on_target_path']]
    negative_indices = [i for i, r in enumerate(rows) if r['negated'] == 'true']
    return {'all_family_assertions': all_rows,
            'counts': {'family_total': len(rows),
                       'family_positive': len(rows) - len(negative_indices),
                       'family_negative': len(negative_indices),
                       'on_target_path': len(target_indices),
                       'target_positive_IBD': len(positive),
                       'target_negative_IRD': len(target_losses),
                       'off_target_path': len(rows) - len(target_indices)},
            'target_path_TSV_indices': target_indices,
            'off_target_path_TSV_indices': [x['TSV_index'] for x in all_rows
                                            if not x['on_target_path']],
            'target_IRD_source_joins': target_losses,
            'same_term_blocked_ancestral_IBD_indices': sorted(blocked),
            'same_term_unblocked_target_IBD_indices': sorted(set(positive) - blocked)}

def verify_family_assertions(rows, projection):
    actual = derive_family_assertions(rows, projection['root_to_target_path'])
    assert actual == projection['complete_family_assertion_inventory'], 'Family assertion omission or mismatch'
    assert set(actual['same_term_unblocked_target_IBD_indices']) == {
        j['TSV_index'] for j in projection['literal_IBD_joins']
    }, 'Imported positive joins differ from same-term unblocked path assertions'
    return actual


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--uniprot',type=Path,default=D.parent/'FGF12-uniprot.txt')
    ap.add_argument('--paint',type=Path,default=D.parents[3]/'interpro/panther/PTHR11486/PTHR11486-paint.tsv')
    ap.add_argument('--records-dir',type=Path,default=D,help='Directory holding unchanged source-receipts.json and data/; default is this package')
    ap.add_argument('--tree-raw',type=Path)
    ap.add_argument('--msa-raw',type=Path)
    args=ap.parse_args();E=args.records_dir;p=J(D/'projections.json');receipts=J(E/'source-receipts.json')
    for name,r in receipts['included_records'].items():
        assert H(E/name)==r['sha256'] and (E/name).stat().st_size==r['body_bytes']
        assert r['http_status']==200 and r['complete'] and not r['error']
    for fn,rel in [(args.uniprot,'genes/human/FGF12/FGF12-uniprot.txt'),(args.paint,'interpro/panther/PTHR11486/PTHR11486-paint.tsv')]:
        pin=receipts['repository_inputs'][rel];assert H(fn)==pin['sha256'] and fn.stat().st_size==pin['bytes']
    u=args.uniprot.read_text();assert 'AC   P61328;'in u
    ff=set(re.findall(r'^DR   FunFam; ([^;]+)',u,re.M));ipr=set(re.findall(r'^DR   InterPro; ([^;]+)',u,re.M));pan=set(re.findall(r'^DR   PANTHER; ([^;]+)',u,re.M))
    lineage={x.strip().rstrip('.')for l in u.splitlines()if l.startswith('OC   ')for x in l[5:].split(';')if x.strip()}
    for expected in p['ARBA_expected_matches']:
        rule=J(E/'data'/ (expected['rule_id']+'.json'));hits=[]
        for i,cs in enumerate(rule['mainRule']['conditionSets']):
            def match(c):
                known={'FunFam id':ff,'InterPro id':ipr,'PANTHER id':pan,'taxon':lineage}.get(c['type'],set())
                ok=any(v['value']in known for v in c['conditionValues']);return not ok if c.get('isNegative')else ok
            if all(match(c)for c in cs['conditions']):hits.append({'zero_based_condition_set':i,'conditions':cs['conditions']})
        assert hits==expected['matching_sets'];assert rule['mainRule']['annotations']==expected['output_annotations']
    entry=J(E/'data/IPR002209.json')['metadata'];target=J(E/'data/InterPro-P61328.json')
    assert target['next']is None;matches=[x for x in target['results']if x['metadata']['accession']=='IPR002209'];assert matches==[p['InterPro_target_match']]
    assert any(x['identifier']=='GO:0008083'for x in entry['go_terms'])
    target_protein=matches[0]['proteins'][0];assert target_protein['accession']=='p61328'and target_protein['protein_length']==243 and target_protein['organism']=='9606'
    info=J(E/'data/P61328-geneinfo.json')['search'];assert info['product']['version']==p['family_api_version'];gene=info['mapped_genes']['gene']
    assert gene['family_id']==p['family']and gene['accession']==p['target_identity']['node_name']and gene['sf_id']==p['target_identity']['prop_sf_id']
    rows=list(csv.DictReader(args.paint.open(),delimiter='\t'));family=verify_family_assertions(rows,p);assert len(p['literal_IBD_joins'])==4
    for j in p['literal_IBD_joins']:
        assert rows[j['TSV_index']]==j['row'];assert j['row']['node']in p['root_to_target_path']and j['row']['negated']=='false'
    assert p['root_to_target_path'][-1]==p['target_leaf']==p['msa_target']['persistent_id']
    assert [(x['parent'],x['child'])for x in p['received_edges']]==list(zip(p['root_to_target_path'],p['root_to_target_path'][1:]))
    seq=re.sub('[^A-Za-z]','',p['msa_target']['sequence']).upper();official=''.join(re.findall('[A-Z]+',u.split('\nSQ   ',1)[1].split('\n',1)[1].split('//',1)[0]))
    assert seq==official and len(seq)==p['canonical_length'];assert hashlib.sha256(seq.encode()).hexdigest()==p['canonical_sequence_sha256']
    anc=J(E/'data/GO0022008-ancestors.json')['results'][0];assert anc['id']=='GO:0022008'and 'GO:0007399'in anc['ancestors']
    reproduced={'tree':False,'msa':False}
    if args.tree_raw:
        r=receipts['external_captures']['PTHR11486-tree.json'];assert H(args.tree_raw)==r['sha256'];assert not r['complete']and r['error']
        text=args.tree_raw.read_text();tree,pos,complete=prefix_value(text);assert not complete and pos==len(text)
        hits=[]
        def walk(o,path,edges):
            if isinstance(o,list):
                for x in o:walk(x,path,edges)
            elif isinstance(o,dict):
                ident=o['persistent_id'];here=path+[ident]
                if o.get('node_name')==p['target_identity']['node_name']:hits.append((o,here,edges))
                children=o.get('children',{}).get('annotation_node',[]);children=children if isinstance(children,list)else[children]
                for i,c in enumerate(children):walk(c,here,edges+[{'parent':ident,'child':c['persistent_id'],'child_ordinal':i}])
        walk(tree['search']['tree_topology']['annotation_node'],[],[]);assert len(hits)==1
        node,path,edges=hits[0];assert path==p['root_to_target_path']and edges==p['received_edges']
        assert {k:node.get(k)for k in p['target_identity']}==p['target_identity'];assert tree['search']['product']['version']==p['family_api_version']
        capture=p['complete_target_leaf_capture'];obj,end=json.JSONDecoder().raw_decode(text,capture['start_character']);assert obj==node and end==capture['end_character']
        assert hashlib.sha256(text[capture['start_character']:end].encode()).hexdigest()==capture['raw_leaf_sha256'];reproduced['tree']=True
    if args.msa_raw:
        r=receipts['external_captures']['PTHR11486-MSA.json'];assert H(args.msa_raw)==r['sha256']and r['complete']and not r['error']
        msa=J(args.msa_raw)['search'];assert msa['product']['version']==p['family_api_version'];ss=msa['MSA_list']['sequence_info'];assert len(ss)==p['msa_sequence_count']
        assert [x for x in ss if x['persistent_id']==p['target_leaf']]==[p['msa_target']];reproduced['msa']=True
    print(json.dumps({'result':'PASS','ARBA_matches':3,'InterPro_target_mapping':True,'literal_IBD_joins':4,'family_assertions':family['counts'],'target_IRD_go_ids':[x['go_id']for x in family['target_IRD_source_joins']],'canonical_sequence_match':True,'projection_reproduced_from_external_raw':reproduced,'complete_tree_download':False,'limitation':'Default mode checks compact evidence consistency; original large captures are required to reproduce tree/MSA extraction.'},indent=2))
if __name__=='__main__':main()
