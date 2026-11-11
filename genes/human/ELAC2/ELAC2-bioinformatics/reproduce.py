#!/usr/bin/env python3
"""Offline ELAC2 database and product replay; Python 3.9+ standard library only."""
from pathlib import Path
import hashlib, json, os, subprocess, sys, tempfile, zipfile
sys.dont_write_bytecode=True
D=Path(__file__).resolve().parent

def need(ok,message):
    if not ok:raise ValueError(message)
def sha(data):return hashlib.sha256(data).hexdigest()
def pinned(data,item):
    need(len(data)==item['bytes'] and sha(data)==item['sha256'],'Changed input: '+item.get('member',item.get('path','input')))
def products(root):
    u=json.loads((root/'frozen-inputs/UniProt-Q9BQ52.json').read_text())
    seq=u['sequence']['value'];features={f['featureId']:f for f in u['features'] if f['type']=='Alternative sequence'}
    isoforms=next(c['isoforms'] for c in u['comments'] if c['commentType']=='ALTERNATIVE PRODUCTS')
    out=[]
    for iso in isoforms:
        assembled=seq
        for f in sorted([features[i] for i in iso.get('sequenceIds',[])],key=lambda x:x['location']['start']['value'],reverse=True):
            start=f['location']['start']['value']-1;end=f['location']['end']['value'];alt=f.get('alternativeSequence',{})
            if 'originalSequence' in alt:need(seq[start:end]==alt['originalSequence'],'VSP original residues differ')
            assembled=assembled[:start]+alt.get('alternativeSequences',[''])[0]+assembled[end:]
        ident=iso['isoformIds'][0]
        fasta=''.join(l.strip() for l in (root/'products'/(ident+'.fasta')).read_text().splitlines() if not l.startswith('>'))
        need(assembled==fasta,'Official splice product mismatch '+ident)
        out.append({'id':ident,'length':len(fasta),'sequence_sha256':sha(fasta.encode())})
    need({p.name for p in (root/'products').glob('*.fasta')}=={p['id']+'.fasta' for p in out},'Product inventory differs')
    return out

def run():
    cfg=json.loads((D/'inputs.json').read_text());archive=D/cfg['archive']['path'];pinned(archive.read_bytes(),cfg['archive'])
    need(sha((D/'expected-results.json').read_bytes())==cfg['expected_sha256'],'Changed expected results')
    need(sha((D/'retrieval-provenance.json').read_bytes())==cfg['provenance_sha256'],'Changed retrieval provenance')
    for p in cfg['scripts']:need(sha((D/p['path']).read_bytes())==p['sha256'],'Changed parser '+p['path'])
    provenance=json.loads((D/'retrieval-provenance.json').read_text());expected=json.loads((D/'expected-results.json').read_text())
    with tempfile.TemporaryDirectory(prefix='elac2-replay-')as temp:
        root=Path(temp)
        with zipfile.ZipFile(archive)as z:
            names=z.namelist();need(len(names)==len(set(names)) and set(names)=={p['member']for p in cfg['members']},'Archive member set differs')
            for p in cfg['members']:
                name=p['member'];need(not Path(name).is_absolute() and '..' not in Path(name).parts,'Unsafe member name')
                data=z.read(name);pinned(data,p);dest=root/name;dest.parent.mkdir(parents=True,exist_ok=True);dest.write_bytes(data)
        members={p['member']:p for p in cfg['members']}
        for rec in provenance['retrievals']:
            p=members[rec['member']];need(p['sha256']==rec['sha256'] and p['bytes']==rec['bytes'],'Receipt/data mismatch')
            need(rec['url'].startswith('https://'),'Unexpected source URL')
            need(rec['status']==200 or (rec['status']==404 and rec['member']=='raw/enzyme-3.1.26.11.txt'),'Unexpected acquisition status')
        for name in ['replay_database.py','reconstruct_paint.py']:(root/name).write_bytes((D/name).read_bytes())
        env=dict(os.environ);env['PYTHONDONTWRITEBYTECODE']='1'
        r=subprocess.run([sys.executable,str(root/'replay_database.py')],capture_output=True,text=True,env=env)
        need(r.returncode==0,'Database parser failed: '+r.stderr)
        computed=json.loads(r.stdout);need(computed==expected,'Raw database reconstruction differs from saved projection')
        product_rows=products(root)
        source_total=len(json.loads((root/'frozen-inputs/source-objects.json').read_text()))
        # Fail closed on a changed byte, using the same predicate as real inputs.
        p=cfg['members'][0];rejected=False
        try:pinned((root/p['member']).read_bytes()+b'changed',p)
        except ValueError:rejected=True
        need(rejected,'Changed-input control failed')
    return {'status':'PASS','raw_members':len(cfg['members']),'retrievals':len(provenance['retrievals']),'failed_unused_endpoint_responses':sum(r['status']!=200 for r in provenance['retrievals']),'source_objects':len(computed['exact_sources']),'whole_gene_source_objects':source_total,'term_definitions':len(computed['terms']),'tree_nodes':computed['paint']['nodes'],'MSA_sequences':computed['paint']['MSA_sequences'],'canonical_sequence_length':computed['paint']['target_sequence_length'],'IBA_joins':len(computed['paint']['joins']),'Reactome_source_rows':len(computed['reactome']['rows']),'products':product_rows,'changed_input_rejected':rejected,'network':False,'ordinary_suite':False}
if __name__=='__main__':print(json.dumps(run(),sort_keys=True))
