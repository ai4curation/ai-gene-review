"""Saved-input target extraction. No network, annotation decisions, or inferred edges."""
import argparse, csv, hashlib, json
from pathlib import Path


E = Path(__file__).resolve().parent
T = E.parent.parent

def run():
    seed = {'existing_annotations':json.loads((E/'source-contexts.json').read_text())}
    raw = E / 'raw/intact-P41091-tab27.tsv'
    records = list(csv.reader(raw.open(), delimiter='\t'))
    if any(len(r) != 42 for r in records):
        raise ValueError('Unexpected MITAB width')
    pairs = []
    for i, a in enumerate(seed['existing_annotations']):
        if a['term']['id'] != 'GO:0005515':
            continue
        partner = a['supporting_entities'][0].removeprefix('UniProtKB:')
        pmid = a['original_reference_id'].removeprefix('PMID:')
        selected = []
        for line, r in enumerate(records, 1):
            if set(r[:2]) != {'uniprotkb:P41091', 'uniprotkb:' + partner} or 'pubmed:' + pmid not in r[8].split('|'):
                continue
            selected.append({'line': line, 'ids': r[:2], 'method': r[6], 'taxa': r[9:11],
                'type': r[11], 'record': r[13], 'expansion': r[15], 'features': r[36:38],
                'annotations': r[25:28], 'negative': r[35], 'roles': r[16:20],
                'host': r[28], 'sequence_checksums': r[32:34]})
        pairs.append({'annotation_index': i, 'partner': partner, 'pmid': pmid, 'records': selected})
    tables = {}
    paths = {
        'opencell': E/'raw/OpenCell-protein-interactions.csv',
        'bioplex2': E/'raw/BioPlex_2.0_293T_DirectedEdges.tsv',
        'bioplex3': E/'raw/BioPlex_3.0_293T_DirectedEdges.tsv',
    }
    for name, p in paths.items():
        rows = list(csv.DictReader(p.open(), delimiter=',' if name == 'opencell' else '\t'))
        if name == 'opencell':
            target = [{'row': j, 'data': r} for j, r in enumerate(rows, 2)
                      if r['target_gene_name'] == 'EIF2S3' or 'EIF2S3' in r['interactor_gene_name'].split(';')]
            selected = [r for r in target if r['data']['target_gene_name'] == 'EIF2S3'
                        and r['data']['interactor_gene_name'] in ['CDC123','EIF2S1','EIF2S2']]
        else:
            target = [{'row': j, 'data': r} for j, r in enumerate(rows, 2)
                      if r['Bait Symbol'] == 'EIF2S3' or r['Prey Symbol'] == 'EIF2S3']
            selected = target
        tables[name] = {'sha256': hashlib.sha256(p.read_bytes()).hexdigest(), 'path': str(p),
            'total_rows': len(rows), 'target_rows': target, 'selected_rows': selected}
    p = E/'raw/PMID40205054-apms-network.json'
    cx = json.loads(p.read_text())
    def entries(key):
        return [v for chunk in cx for v in chunk.get(key, [])]
    nodes = {n['@id']:n for n in entries('nodes')}
    targets = {k for k,n in nodes.items() if n.get('n') == 'EIF2S3'}
    edges = [r for r in entries('edges') if r['s'] in targets or r['t'] in targets]
    selected = [r for r in edges if {nodes[r['s']]['n'], nodes[r['t']]['n']} == {'EIF2S3','CDC123'}]
    edge_ids = {r['@id'] for r in selected}
    graph = {'sha256':hashlib.sha256(p.read_bytes()).hexdigest(), 'path':str(p),
             'target_nodes':[nodes[k] for k in sorted(targets)], 'target_edges':edges,
             'selected_edges':selected, 'selected_attributes':[r for r in entries('edgeAttributes') if r['po'] in edge_ids],
             'neighbors':{str(k):nodes[k] for k in sorted({r[x] for r in edges for x in ['s','t']})}}
    return {'MITAB_total':len(records), 'pairs':pairs, 'tables':tables, 'graph':graph,
            'scope':'Exact primary IDs only; no-match is not negative evidence. Mixed peptide/accession groups remain literal. No directness or biological verdict is inferred.'}

if __name__ == '__main__':
    ap=argparse.ArgumentParser(); ap.add_argument('--output',required=True); args=ap.parse_args()
    Path(args.output).write_text(json.dumps(run(),indent=2)+'\n')
