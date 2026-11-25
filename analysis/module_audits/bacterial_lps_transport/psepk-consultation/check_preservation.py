"""Verify the seven-member LPS consultation without changing curated/source files."""

import copy
import hashlib
import json
from pathlib import Path
import subprocess

import yaml

from ai_gene_review.validation.local_source_text import quote_matches, resolve_local_source
from ai_gene_review.validation.supporting_text import build_supporting_text_validator

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def quotations(value, reference=None):
    if isinstance(value, dict):
        own = value.get('id', '')
        if own.startswith(('PMID:', 'file:')):
            reference = own
        ref = value.get('reference_id') or reference
        if value.get('supporting_text'):
            yield ref, value['supporting_text']
        for key, child in value.items():
            if key != 'supporting_text':
                yield from quotations(child, ref)
    elif isinstance(value, list):
        for child in value:
            yield from quotations(child, reference)


def main():
    before = json.loads((HERE / 'before.json').read_text())
    root_baseline = json.loads((HERE.parent / 'baseline.json').read_text())
    validator, _ = build_supporting_text_validator(ROOT / 'publications')
    rows, new_rows, quoted = 0, 0, 0
    ledger, source_hashes, history_hashes = [], {}, {}
    for relative, prior in before['reviews'].items():
        assert prior == root_baseline['reviews'][relative]
        old = prior['document']
        current = yaml.safe_load((ROOT / relative).read_text())
        assert (old['id'], old['taxon']) == (current['id'], current['taxon'])
        assert current['status'] == 'COMPLETE'
        assert len(old['existing_annotations']) == len(current['existing_annotations'])
        for i, (a, b) in enumerate(zip(old['existing_annotations'], current['existing_annotations'], strict=True)):
            assert {k: v for k, v in a.items() if k != 'review'} == {
                k: v for k, v in b.items() if k != 'review'}, (relative, i, 'payload/order/lifecycle changed')
            assert a['review']['action'] == b['review']['action'], (relative, i, 'action changed')
            assert b['review'].get('reason') and b['review'].get('supported_by'), (relative, i)
            rows += 1
            new_rows += b['review']['action'] == 'NEW'
            ledger.append(dict(path=relative, index=i, term=a['term']['id'], action=b['review']['action'],
                               evidence_type=a['evidence_type'], historical_NEW=a['review']['action'] == 'NEW',
                               retired=a.get('retired', False), reason=b['review']['reason']))
        # Core evidence and explanatory prose may improve, but functional assertions do not change.
        def assertions(review):
            cores = copy.deepcopy(review.get('core_functions', []))
            for core in cores:
                core.pop('description', None)
                core.pop('supported_by', None)
            return cores
        assert assertions(old) == assertions(current), (relative, 'core assertion changed')
        original_references = {r['id']: r['title'] for r in old['references']}
        current_references = {r['id']: r['title'] for r in current['references']}
        assert original_references.items() <= current_references.items(), relative
        for ref, quote in set(quotations(current)):
            assert ref, (relative, quote)
            if ref.startswith('file:'):
                source = resolve_local_source(ref, ROOT)
                assert source and quote_matches(quote, source), (relative, ref, quote)
            else:
                assert ref.startswith('PMID:'), (relative, ref)
                result = validator.validate(quote, ref)
                assert result.is_valid and not result.skipped, (relative, ref, result.message)
                source = ROOT / 'publications' / (ref.replace(':', '_') + '.md')
            source_hashes[str(source.relative_to(ROOT))] = sha(source)
            quoted += 1
        gene = old['gene_symbol']
        log = (HERE / 'paint-checks' / f'paint-{gene}.log').read_text()
        assert old['id'] + ' is not a leaf of this tree; losses not checked.' in log
        assert '403' in (HERE / 'provider-attempts' / f'falcon-{gene}.log').read_text()
        history_root = f'history/genes/PSEPK/{gene}'
        previous = subprocess.check_output(
            ['git', 'ls-tree', '-r', '--name-only', root_baseline['head'], '--', history_root],
            cwd=ROOT, text=True).splitlines()
        for path in previous:
            original = subprocess.check_output(['git', 'show', f'{root_baseline["head"]}:{path}'], cwd=ROOT)
            expected = hashlib.sha256(original).hexdigest()
            assert sha(ROOT / path) == expected, (path, 'historical record edited')
            history_hashes[path] = expected
    assert (rows, new_rows) == (46, 2)
    for relative, expected in before['protected_files_sha256'].items():
        assert sha(ROOT / relative) == expected, (relative, 'protected source modified')
        source_hashes[relative] = expected
    result = dict(status='PASS', reviews=7, original_ordered_rows=rows, original_actions_unchanged=True,
                  original_functional_core_assertions_unchanged=True, historical_NEW=new_rows,
                  active_NEW=new_rows, retired_NEW=0, added_rows=0, deleted_rows=0,
                  lifecycle_changes=0, protected_baseline_files=len(before['protected_files_sha256']),
                  checked_distinct_per_review_quotations=quoted, source_files_sha256=source_hashes,
                  previous_history_files_sha256=history_hashes,
                  unresolved_PAINT_lineages=7, actual_failed_Falcon_attempts=7,
                  baseline_sha256=sha(HERE / 'before.json'))
    (HERE / 'preservation.json').write_text(json.dumps(result, indent=2) + '\n')
    (HERE / 'action-ledger.yaml').write_text(yaml.safe_dump(ledger, sort_keys=False, width=105))
    print(json.dumps({k: result[k] for k in ['status', 'reviews', 'original_ordered_rows',
                                           'historical_NEW', 'protected_baseline_files',
                                           'checked_distinct_per_review_quotations']}))


if __name__ == '__main__':
    main()
