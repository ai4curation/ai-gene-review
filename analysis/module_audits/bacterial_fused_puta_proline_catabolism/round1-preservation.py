"""Verify source-order/payload preservation against the reviewed PR head.

Only original annotation fields are compared; review judgments may change. Raw,
provider, and cited publication files are compared byte-for-byte to git. The
local pre-edit snapshot additionally covers every publication present at start.
"""
from pathlib import Path
import hashlib
import json
import subprocess
import yaml

ROOT = Path(__file__).resolve().parents[3]
AUDIT = Path(__file__).resolve().parent
HEAD = 'b4a3149dfba627e423b9356c74b7b757018a09fa'
PANEL = [('PSEPK', 'putA'), ('ECOLI', 'putA'), ('SALTY', 'putA'),
         ('BRADU', 'putA'), ('SINMM', 'putA'), ('GEOSL', 'putA'),
         ('9CORY', 'putA'), ('HELPG', 'putA'), ('PSEPK', 'putP'),
         ('ECOLI', 'putP'), ('HELPG', 'putP'), ('yeast', 'PUT2')]


def git_bytes(path, revision=HEAD):
    return subprocess.check_output(['git', 'show', f'{revision}:{path}'], cwd=ROOT)


def payloads(review):
    return [{k: v for k, v in row.items() if k != 'review'}
            for row in review['existing_annotations']]


def main():
    reviews = {}
    protected = set()
    tracked = subprocess.check_output(['git', 'ls-tree', '-r', '--name-only', HEAD],
                                     cwd=ROOT, text=True).splitlines()
    for species, gene in PANEL:
        folder = f'genes/{species}/{gene}/'
        path = folder + f'{gene}-ai-review.yaml'
        original = yaml.safe_load(git_bytes(path))
        current = yaml.safe_load((ROOT / path).read_text())
        assert payloads(original) == payloads(current), path
        reviews[path] = dict(rows=len(payloads(current)), ordered_payloads_unchanged=True,
                             current_sha256=hashlib.sha256((ROOT / path).read_bytes()).hexdigest())
        protected.update(p for p in tracked if p.startswith(folder) and
                         any(x in p for x in ['-uniprot.', '-goa.', '-deep-research', '-citations.']))
        for ref in original.get('references', []):
            if ref['id'].startswith('PMID:'):
                p = 'publications/' + ref['id'].replace(':', '_') + '.md'
                if p in tracked:
                    protected.add(p)
    source_hashes = {}
    for p in sorted(protected):
        data = (ROOT / p).read_bytes()
        assert data == git_bytes(p), p
        source_hashes[p] = hashlib.sha256(data).hexdigest()
    # Also retain the original five reviews' pre-audit rows, including historical NEW.
    initial = yaml.safe_load((AUDIT / 'baseline.yaml').read_text())
    initial_count = 0
    for path, original in initial['reviews'].items():
        current = yaml.safe_load((ROOT / path).read_text())
        assert payloads(current) == original['annotation_payloads'], path
        initial_count += len(payloads(current))
    snapshot = ROOT / '.cache/module-audit-logs/puta-20261106/round1/before.json'
    broad_check = None
    if snapshot.exists():
        before = json.loads(snapshot.read_text())
        for path, sha in before['protected'].items():
            assert hashlib.sha256((ROOT / path).read_bytes()).hexdigest() == sha, path
        broad_check = dict(preexisting_sources_checked=len(before['protected']), all_unchanged=True,
                           snapshot_sha256=hashlib.sha256(snapshot.read_bytes()).hexdigest())
    result = dict(status='PASS', reviewed_head=HEAD, pre_audit_commit=initial['base_commit'],
                  panel_reviews=11, comparator_reviews=1,
                  panel_rows=sum(v['rows'] for p, v in reviews.items() if '/yeast/' not in p),
                  comparator_rows=reviews['genes/yeast/PUT2/PUT2-ai-review.yaml']['rows'],
                  original_five_rows=initial_count, rows_added=0, rows_deleted=0,
                  source_payload_and_order_preserved=True,
                  protected_tracked_source_count=len(source_hashes), protected_sha256=source_hashes,
                  reviews=reviews, local_pre_edit_snapshot_check=broad_check)
    (AUDIT / 'round1-preservation.yaml').write_text(yaml.safe_dump(result, sort_keys=False))
    print({k: v for k, v in result.items() if k not in ['protected_sha256', 'reviews']})


if __name__ == '__main__':
    main()
