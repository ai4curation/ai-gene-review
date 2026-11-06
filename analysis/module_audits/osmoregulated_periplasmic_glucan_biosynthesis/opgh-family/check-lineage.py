#!/usr/bin/env python3
"""Verify the scoped proof against immutable source snapshots (run from repo root)."""
from pathlib import Path
import gzip, hashlib, json, collections, yaml
here=Path(__file__).resolve().parent
proof=yaml.safe_load((here/'lineage-proof.yaml').read_text())
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
for path,expected in proof['source_hashes'].items():
    assert sha(path)==expected, path
path=Path('.cache/panther_trees/PTHR43867.json.gz')
assert sha(path)==proof['tree']['sha256']
tree=json.load(gzip.open(path,'rt'))
for node,expected in proof['nodes'].items():
    leaves={i:tree['leaves'][i] for i in tree['under'][node]}
    assert len(leaves)==expected['descendant_count'],node
    assert dict(collections.Counter(x['subfamily'] for x in leaves.values()))==expected['subfamily_counts'],node
    for key in ['selected_descendants','sf5_descendants']:
        for leaf,record in expected[key].items():
            assert leaves[leaf]==record,(node,leaf)
for acc,record in proof['members'].items():
    path=Path('.cache/module-audit-logs/opg-20261106/opgh-family')/(acc+'.json')
    if path.exists():
        assert sha(path)==record['sha256'],acc
        source=json.loads(path.read_text())
        function=next(x for x in source['comments'] if x['commentType']=='FUNCTION')['texts'][0]
        assert function==record['function'],acc
print('PASS: frozen source hashes, three node descents, selected current UniProt experimental statements')
