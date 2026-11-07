"""Verify the six original glycerol reviews without modifying any source.

Run: uv run python analysis/module_audits/bacterial_glycerol_uptake_catabolism/existing-member-consultation/verify_preservation.py
"""
import hashlib
import json
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[4]
BASELINE = ROOT / 'analysis/module_audits/bacterial_glycerol_uptake_catabolism/baseline.yaml'


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    baseline = yaml.safe_load(BASELINE.read_text())
    result = {'baseline_sha256': sha(BASELINE), 'reviews': {}, 'protected_sources': {}}
    for name, frozen in baseline['reviews'].items():
        current = yaml.safe_load((ROOT / name).read_text())
        payloads = [{k: v for k, v in row.items() if k != 'review'} for row in current['existing_annotations']]
        assert payloads == frozen['annotation_payloads'], f'Ordered payload mismatch: {name}'
        assert current['status'] == 'COMPLETE', name
        # The one historical proposal is itself frozen source content, not a new audit assertion.
        if name == 'genes/PSEPK/glpD/glpD-ai-review.yaml':
            assert current['existing_annotations'][3]['review']['action'] == 'NEW'
        result['reviews'][name] = {'rows': len(payloads), 'ordered_payloads_unchanged': True, 'sha256': sha(ROOT / name)}
    for name, original_hash in baseline['protected_sha256'].items():
        actual = sha(ROOT / name)
        assert actual == original_hash, f'Protected source changed: {name}'
        result['protected_sources'][name] = actual
    result.update(rows=sum(x['rows'] for x in result['reviews'].values()), historical_new=1, added_new=0,
                  protected_file_count=len(result['protected_sources']), status='PASS')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
