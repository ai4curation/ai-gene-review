"""Acquire official reference evidence into this consultation; never refresh raw caches."""
import hashlib
import json
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import requests

from ai_gene_review.etl.panther_trees import compact_tree

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]


def get(spec):
    name, url = spec
    path = HERE / name
    if path.exists():
        return {'path': str(path.relative_to(ROOT)), 'url': url, 'status': 'existing_not_refreshed',
                'sha256': hashlib.sha256(path.read_bytes()).hexdigest()}
    result = requests.get(url, timeout=60)
    result.raise_for_status()
    path.write_bytes(result.content)
    return {'path': str(path.relative_to(ROOT)), 'url': result.url, 'status': result.status_code,
            'retrieved': '2026-11-07', 'sha256': hashlib.sha256(result.content).hexdigest()}


def main():
    jobs = [(f'{f}-tree.json', f'https://pantherdb.org/services/oai/pantherdb/treeinfo?family={f}')
            for f in ['PTHR33799', 'PTHR32502']]
    jobs += [(f'{a}-uniprot.json', f'https://rest.uniprot.org/uniprotkb/{a}.json')
             for a in ['P26379', 'P26381', 'P26382', 'P0C8J8', 'P0C8K0', 'Q9CEX8', 'Q9CEX7', 'Q9CEX6', 'Q8DSC4', 'Q8DSC3', 'Q8DSC2']]
    jobs += [('go-terms.json', 'https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/' +
              ','.join(['GO:0008982', 'GO:0009401', 'GO:1902495', 'GO:0005886',
                        'GO:0008047', 'GO:0022870', 'GO:0015758', 'GO:0008983']))]
    with ThreadPoolExecutor(max_workers=4) as pool:
        output = list(pool.map(get, jobs))
    (HERE / 'acquisition.json').write_text(json.dumps(output, indent=2)+'\n')
    trees = {}
    for family in ['PTHR33799', 'PTHR32502']:
        trees[family] = compact_tree(json.loads((HERE / f'{family}-tree.json').read_text()))
    (HERE / 'trees-compact.json').write_text(json.dumps(trees, indent=2)+'\n')
    print([(k, len(v['leaves'])) for k, v in trees.items()])


if __name__ == '__main__':
    main()
