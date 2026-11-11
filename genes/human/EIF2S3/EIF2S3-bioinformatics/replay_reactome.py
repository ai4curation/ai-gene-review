"""Reconstruct bounded entity paths from saved official Reactome page captures."""
import argparse, collections, hashlib, json, re
from pathlib import Path


E = Path(__file__).resolve().parent

def run():
    files = [E/'reactome/web-recovery-13.json', E/'reactome/web-recovery-14.json', *sorted(p for p in (E/'reactome').glob('web*.json') if p.name not in {'web-recovery-13.json','web-recovery-14.json'})]
    pages = collections.defaultdict(list)
    labels = collections.defaultdict(set)
    for p in files:
        for block in json.loads(p.read_text()).split('--------------------------------------------------------------------------------'):
            match = re.search(r'Reactome \| (.*?) \(https://reactome.org/content/detail/(R-HSA-\d+)\)', block)
            if not match:
                continue
            label, ident = match.groups()
            labels[' '.join(label.split())].add(ident)
            lines = [(int(m[1]),m[2].strip()) for m in re.finditer(r'L(\d+):\s*(.*?)(?=L\d+:|\Z)', block, re.S)]
            pages[ident].append({'path':str(p), 'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),
                'web_ref':re.search(r'turn\d+view\d+',block)[0], 'label':label, 'lines':lines})
    edges = []
    for ident, captures in pages.items():
        for capture in captures:
            active = False; relation = None
            for line, content in capture['lines']:
                if content == 'Participants': active = True; continue
                if active and content in ['Participates','Catalyst Activity','Orthologous Events','Inferred To']:
                    active = False
                if not active: continue
                if content in ['Input','Output','components']: relation=content; continue
                for m in re.finditer(r'\ue200cite\ue202(\d+)\u2020(.*?)\ue201', content):
                    label = m[2].removesuffix(' (Homo sapiens)').strip()
                    matches = labels.get(' '.join(label.split()), set())
                    if len(matches) == 1 and relation:
                        edges.append({'from':ident,'relation':relation,'to':next(iter(matches)),
                            'link_label':label,'link_id':int(m[1]),'line':line,'capture':capture['path'],'web_ref':capture['web_ref']})
    # Only a forward input/output or literal component chain is used; reverse membership is excluded.
    by_from=collections.defaultdict(list)
    for edge in edges: by_from[edge['from']].append(edge)
    seed={'existing_annotations':json.loads((E/'source-contexts.json').read_text())}
    rows=[]
    for i,a in enumerate(seed['existing_annotations']):
        if not a['original_reference_id'].startswith('Reactome:'): continue
        root=a['original_reference_id'].split(':',1)[1]; q=collections.deque([(root,[])]); visited=set(); found=None
        while q:
            node,path=q.popleft()
            if node == 'R-HSA-72514': found=path; break
            if node in visited: continue
            visited.add(node)
            for edge in by_from[node]: q.append((edge['to'],path+[edge]))
        if found is None: raise ValueError('No literal target path for '+root)
        rows.append({'annotation_index':i,'source':{k:v for k,v in a.items() if k!='review'},'root':root,'path':found})
    leaf='\n'.join(content for c in pages['R-HSA-72514'] for _,content in c['lines'])
    if 'UniProt:P41091 EIF2S3' not in leaf or 'chain:2-472' not in leaf: raise ValueError('Target identity not authenticated')
    return {'rows':rows,'target':'R-HSA-72514','target_reference':'UniProt:P41091','target_processing':'initiator methionine:1, chain:2-472',
        'captured_pages':sorted(pages), 'edges':edges,
        'scope':'Selected official public-page input/output/component paths only. API 403 retained separately. No exhaustive graph closure, primary-paper read, or transfer of the event catalyst activity is asserted.'}

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--output',required=True);args=ap.parse_args()
    Path(args.output).write_text(json.dumps(run(),indent=2)+'\n')
