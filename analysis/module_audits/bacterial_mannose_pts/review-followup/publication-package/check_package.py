"""Checkout-ready scoped publication checks; ignored acquisition files are optional."""
import argparse
import hashlib
import importlib.util
import json
import re
import sys
from pathlib import Path

import yaml
from bs4 import BeautifulSoup

from ai_gene_review.validation.local_source_text import quote_matches, resolve_local_source
from ai_gene_review.validation.supporting_text import build_supporting_text_validator

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
AUDIT = HERE.parent.parent
sys.dont_write_bytecode = True


def read(path):
    return json.loads(path.read_text())


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def import_file(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--verify-local-acquisitions', action='store_true')
    parser.add_argument('--deny-ignored-reads', action='store_true')
    args = parser.parse_args()
    if args.deny_ignored_reads:
        def audit(event, arguments):
            if event == 'open' and isinstance(arguments[0], (str, bytes)):
                p = Path(arguments[0]).resolve()
                if ROOT / '.cache' in p.parents:
                    raise AssertionError('Ignored-cache read prohibited: ' + str(p))
        sys.addaudithook(audit)
    mapping = read(HERE / 'publication-input-map.json')
    for path, record in mapping.items():
        assert not path.startswith('.cache/'), path
        assert sha(ROOT / path) == record['sha256'], path
    omitted = read(HERE / 'acquisition-mapping.json')
    assert len(omitted) == 32
    for item in omitted:
        assert (ROOT / item['durable_path']).is_file()
        if item['disposition'] == 'BYTE_IDENTICAL_DURABLE_COPY':
            assert sha(ROOT / item['durable_path']) == item['original_sha256']
        if args.verify_local_acquisitions:
            assert sha(ROOT / item['original_path']) == item['original_sha256']
    excerpts = read(HERE / 'bounded-excerpts.json')
    if args.verify_local_acquisitions:
        for row in excerpts:
            source = ROOT / row['original_path']
            assert sha(source) == row['original_sha256']
            text = source.read_text()
            if source.suffix == '.html':
                text = BeautifulSoup(text, 'html.parser').get_text(' ', strip=True)
            assert row['exact_excerpt'] in re.sub(r'\s+', ' ', text), row['publication']
    # Check scoped excerpts against the frozen curation ledger without needing full articles.
    ledger = yaml.safe_load((AUDIT / 'literature-consultation/evidence-ledger.yaml').read_text())
    for item in ledger:
        assert any(r['publication'] == item['id'] and r['exact_excerpt'] == item['supporting_text']
                   for r in excerpts), item['id']
    old = import_file('prior_closure_functions', AUDIT / 'capacity-consultation/check_closure.py')
    panel = read(HERE.parent / 'published-panel-baseline.json')
    docs = {}
    count = new = retired = 0
    for path, record in panel.items():
        doc = yaml.safe_load((ROOT / path).read_text())
        before, after = record['document']['existing_annotations'], doc['existing_annotations']
        assert len(before) == len(after)
        for a, b in zip(before, after, strict=True):
            assert {k: v for k, v in a.items() if k != 'review'} == {k: v for k, v in b.items() if k != 'review'}
            assert (a['review']['action'] == 'NEW') == (b['review']['action'] == 'NEW')
            new += b['review']['action'] == 'NEW'
            retired += b.get('retired', False)
        count += len(after)
        docs[path] = doc
    assert (count, new, retired) == (93, 2, 0)
    for path in ['modules/bacterial_mannose_pts.yaml', 'interpro/panther/PTHR33799/PTHR33799-review.yaml',
                 'interpro/panther/PTHR32502/PTHR32502-review.yaml']:
        docs[path] = yaml.safe_load((ROOT / path).read_text())
    validator, _ = build_supporting_text_validator(ROOT / 'publications')
    quote_count = 0
    for name, doc in docs.items():
        for ref, text in set(old.quotes(doc)):
            if ref.startswith('file:'):
                source = resolve_local_source(ref, ROOT)
                assert source and quote_matches(text, source), (name, ref)
            else:
                result = validator.validate(text, ref)
                assert result.is_valid and not result.skipped, (name, ref)
            quote_count += 1
    assert quote_count == 114
    cap = import_file('prior_capacity_functions', AUDIT / 'capacity-consultation/check_capacity.py')
    doc = yaml.safe_load((ROOT / 'modules/bacterial_mannose_pts.yaml').read_text())
    registry = cap.members()
    examples = cap.cases()
    outputs = []
    for case in examples:
        actual = cap.evaluate(doc, registry, case)
        assert all(actual[k] == v for k, v in case['expected'].items())
        outputs.append({'case': case['id'], **actual})
    published = read(AUDIT / 'capacity-consultation/results.json')
    assert outputs == published['cases'] and len(outputs) == 60
    # Repeat every published mutation/sensitivity witness without writing old results.
    from ai_gene_review.module_logic import compile_node, core_atoms
    mutations = []
    for label, model in cap.mutations(doc):
        failures = [c['id'] for c in examples if any(cap.evaluate(model, registry, c)[k] != v
                                                    for k, v in c['expected'].items())]
        structural = {a.node_id for a in core_atoms(compile_node(model['module']))} != {cap.RELAY, cap.TRANSPORT}
        assert failures or structural
        mutations.append({'mutation': label, 'detected_by_cases': failures,
                          'production_core_contract_detected': structural})
    assert mutations == published['mutations'] and len(mutations) == 13
    cases = {c['id']: c for c in examples}
    for witness in published['sensitivities']:
        case = cases[witness['case']]
        assert not cap.evaluate(doc, registry, case)['whole']
        assert cap.evaluate(doc, registry, case, [witness['erased_gate']])['whole']
    assert len(published['sensitivities']) == 9
    print(json.dumps({'status': 'PASS', 'publication_inputs': len(mapping), 'rows': count,
                      'historical_NEW': new, 'retired': retired, 'quotes': quote_count,
                      'bounded_excerpts': len(excerpts), 'ignored_dispositions': len(omitted),
                      'capacity_cases': 60, 'mutations': 13, 'sensitivities': 9,
                      'local_acquisitions_verified': args.verify_local_acquisitions,
                      'ignored_reads_denied': args.deny_ignored_reads}))


if __name__ == '__main__':
    main()
