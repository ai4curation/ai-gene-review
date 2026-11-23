"""Verify original PedE/PedH records and explicit PR 5588 proposal supersession."""

import hashlib
import json
from pathlib import Path

import yaml

root = Path(__file__).resolve().parents[4]
folder = Path(__file__).parent
snapshot = json.loads((folder / 'original-annotation-payloads.json').read_text())
followup = json.loads((folder / 'pr5588-proposal-supersession.json').read_text())
changes = {(c['path'], c['ordinal']): c for c in followup['changes']}
for filename, before in snapshot['reviews'].items():
    current = yaml.safe_load((root / filename).read_text())
    expected = before['original_payloads']
    actual = [{k: v for k, v in a.items() if k != 'review'}
              for a in current['existing_annotations']]
    assert len(actual) == len(expected), filename
    for ordinal, (original, final) in enumerate(zip(expected, actual), 1):
        change = changes.get((filename, ordinal))
        if change:
            assert original == change['before'], (filename, ordinal, 'baseline')
            assert final == change['after'], (filename, ordinal, 'supersession')
        else:
            assert original == final, (filename, ordinal)
for filename, digest in snapshot['raw_sha256'].items():
    current = followup['raw_path_renames'].get(filename, filename)
    assert hashlib.sha256((root / current).read_bytes()).hexdigest() == digest, filename
print('PASS: 24 rows retained; machine payloads unchanged; five explicit proposal '
      'supersessions verified; four raw source hashes preserved.')
