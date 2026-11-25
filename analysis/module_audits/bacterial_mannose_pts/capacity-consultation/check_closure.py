"""Independently verify released receipts, ordered payloads, sources and exact quotations."""
import hashlib
import json
import re
import subprocess
from pathlib import Path

import yaml
from bs4 import BeautifulSoup

from ai_gene_review.validation.local_source_text import quote_matches, resolve_local_source
from ai_gene_review.validation.supporting_text import build_supporting_text_validator

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
AUDIT = HERE.parent
MODULE = 'modules/bacterial_mannose_pts.yaml'
MODULE_SHA = '221255e36172970f783904d5c6047ea8195c7480c6633b15082488e0baa228cc'


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read(path):
    return json.loads(path.read_text())


def walk(value):
    if isinstance(value, dict):
        yield value
        for item in value.values():
            yield from walk(item)
    elif isinstance(value, list):
        for item in value:
            yield from walk(item)


def quotes(value, inherited=None):
    if isinstance(value, dict):
        ref = value.get('reference_id', inherited)
        if value.get('id', '').startswith(('PMID:', 'file:')):
            ref = value['id']
        if value.get('supporting_text'):
            assert ref, value
            yield ref, value['supporting_text']
        for key, child in value.items():
            if key != 'supporting_text':
                yield from quotes(child, ref)
    elif isinstance(value, list):
        for child in value:
            yield from quotes(child, inherited)


def main():
    inputs = {}

    def capture(path, expected=None):
        path = ROOT / path if not Path(path).is_absolute() else Path(path)
        digest = sha(path)
        assert expected is None or expected == digest, (str(path), expected, digest)
        inputs[str(path.relative_to(ROOT))] = digest
        return path

    capture(MODULE, MODULE_SHA)
    capture('pages/modules/bacterial_mannose_pts.html')
    capture('src/ai_gene_review/module_logic.py')
    capture('src/ai_gene_review/module_qc.py')
    capture('src/ai_gene_review/module_gene_symbols.py')
    capture('src/ai_gene_review/render_modules.py')
    module_receipt = read(capture(AUDIT / 'root-module-complete.json'))
    assert module_receipt['sha256'] == MODULE_SHA
    for path in module_receipt['histories']:
        if path.startswith('history/modules/'):
            capture(path)
    successor_path = AUDIT / 'ecoli-consultation/core-contribution-followup/handoff.json'
    successor = read(capture(successor_path))
    delta = read(capture(successor_path.parent / 'preservation.json'))['authorized_superseded_paths']
    assert set(delta) == {f'genes/ECOLI/manX/manX-{suffix}' for suffix in ['ai-review.yaml', 'ai-review.html', 'notes.md']}
    for path, digest in successor['files'].items():
        capture(path, digest)
    manifests = []
    for directory in ['ecoli-consultation', 'il1403-consultation', 'ua159-consultation',
                      'literature-consultation', 'family-consultation']:
        path = capture(AUDIT / directory / 'handoff.json')
        manifest = read(path)
        if directory == 'ecoli-consultation':
            assert sha(path) == successor['original_handoff_sha256']
        for name, expected in manifest['files'].items():
            if directory == 'ecoli-consultation' and name in delta:
                assert expected == delta[name]['before']
                assert successor['files'][name] == delta[name]['after']
                expected = delta[name]['after']
            capture(name, expected)
        manifests.append({'path': str(path.relative_to(ROOT)), 'sha256': sha(path),
                          'file_count': len(manifest['files'])})
    for source_list in ['literature-consultation/source-sha256.json',
                        'ecoli-consultation/additional-protected.json']:
        values = read(capture(AUDIT / source_list))
        for path, expected in values.get('files', values).items():
            capture(path, expected)
    genes, protected = {}, {}
    for filename in ['baseline.json', 'additional-seed-baseline.json', 'ua159-seed-baseline.json']:
        baseline = read(capture(AUDIT / filename))
        genes.update(baseline.get('genes', baseline.get('reviews', {})))
        protected.update(baseline['protected_files_sha256'])
    for path, expected in protected.items():
        capture(path, expected)
    baseline_head = read(AUDIT / 'baseline.json')['head']
    history_roots = [f'history/genes/{Path(name).parts[1]}/{Path(name).parts[2]}' for name in genes]
    old_history_paths = subprocess.check_output(
        ['git', 'ls-tree', '-r', '--name-only', baseline_head, '--', *history_roots], cwd=ROOT, text=True).splitlines()
    for name in old_history_paths:
        original = subprocess.check_output(['git', 'show', f'{baseline_head}:{name}'], cwd=ROOT)
        capture(name, hashlib.sha256(original).hexdigest())
    row_count = historical_new = retired = 0
    documents = {MODULE: yaml.safe_load((ROOT / MODULE).read_text())}
    row_ledger = []
    for name, frozen in sorted(genes.items()):
        doc = yaml.safe_load(capture(name).read_text())
        old, new = frozen['document']['existing_annotations'], doc['existing_annotations']
        assert doc['status'] == 'COMPLETE' and len(old) == len(new), name
        for index, (a, b) in enumerate(zip(old, new, strict=True)):
            assert {k: v for k, v in a.items() if k != 'review'} == {k: v for k, v in b.items() if k != 'review'}, (name, index)
            assert (a['review']['action'] == 'NEW') == (b['review']['action'] == 'NEW')
            assert b['review']['action'] != 'PENDING'
            historical_new += b['review']['action'] == 'NEW'
            retired += b.get('retired', False)
        row_count += len(new)
        row_ledger.append({'review': name, 'seed_sha256': frozen['sha256'],
                           'current_sha256': sha(ROOT / name), 'rows': len(new)})
        documents[name] = doc
    assert (len(genes), row_count, historical_new, retired) == (9, 93, 2, 0)
    for family in ['PTHR33799', 'PTHR32502']:
        name = f'interpro/panther/{family}/{family}-review.yaml'
        documents[name] = yaml.safe_load(capture(name).read_text())
    validator, _ = build_supporting_text_validator(ROOT / 'publications')
    quote_ledger = []
    for name, doc in sorted(documents.items()):
        for ref, text in sorted(set(quotes(doc))):
            if ref.startswith('file:'):
                source = resolve_local_source(ref, ROOT)
                assert source and quote_matches(text, source), (name, ref, text)
            else:
                assert ref.startswith('PMID:'), (name, ref)
                result = validator.validate(text, ref)
                assert result.is_valid and not result.skipped, (name, ref, result.message)
                source = ROOT / 'publications' / (ref.replace(':', '_') + '.md')
            capture(source)
            quote_ledger.append({'document': name, 'reference': ref, 'supporting_text': text,
                                 'source': str(source.relative_to(ROOT)), 'source_sha256': sha(source)})
        # Include cited but unquoted publications and local evidence sources in closure.
        for item in walk(doc):
            for key in ['reference_id', 'source_id', 'id']:
                ref = item.get(key, '')
                if not isinstance(ref, str):
                    continue
                if ref.startswith('PMID:'):
                    capture('publications/' + ref.replace(':', '_') + '.md')
                elif ref.startswith('file:'):
                    source = resolve_local_source(ref, ROOT)
                    assert source, (name, ref)
                    capture(source)
    findings = yaml.safe_load(capture(AUDIT / 'literature-consultation/evidence-ledger.yaml').read_text())
    full_source_quotes = []
    for row in findings:
        source = capture(row['consulted_source'])
        text = source.read_text()
        if source.suffix == '.html':
            text = BeautifulSoup(text, 'html.parser').get_text(' ', strip=True)
        normalized = re.sub(r'\s+', ' ', text).strip()
        assert row['supporting_text'] in normalized, row['id']
        full_source_quotes.append({**row, 'source_sha256': sha(source)})
    assert len(full_source_quotes) == 14
    identity = read(capture(AUDIT / 'literature-consultation/identity-proof.json'))
    assert {x['accession'] for x in identity['verified_panels']} == {'Q9CEX8', 'Q9CEX7', 'Q9CEX6', 'Q8DSC4', 'Q8DSC3', 'Q8DSC2'}
    split = identity['split_CECT904']['proteins']
    assert len(split) == 4 and split[-1]['partial'] and split[-1]['length'] == 87
    closure_path = HERE / 'inputs.json'
    input_record = {'module_sha256': MODULE_SHA, 'sha256': dict(sorted(inputs.items()))}
    if closure_path.exists():
        assert read(closure_path) == input_record, 'Frozen input closure changed; investigate and explicitly supersede, never silently refresh.'
    else:
        closure_path.write_text(json.dumps(input_record, indent=2)+'\n')
    result = {'status': 'PASS', 'input_count': len(inputs), 'review_count': len(genes),
              'ordered_payloads': row_count, 'historical_NEW': historical_new,
              'active_NEW': historical_new-retired, 'retired': retired,
              'original_and_seed_sources': len(protected), 'original_history_files': len(old_history_paths), 'module_sha256': MODULE_SHA,
              'source_quote_count': len(quote_ledger), 'separately_acquired_quote_count': len(full_source_quotes),
              'verified_identity_bridges': 6, 'complete_split_reference_panels': 0,
              'receipt_manifests': manifests, 'explicit_authorized_supersession': delta,
              'reviews': row_ledger,
              'scope': 'Byte closure and literal source checks establish preservation/provenance, not native flux, isolated component catalysis or universal family functions.'}
    for filename, value in [('closure.json', result), ('quotes.json', quote_ledger), ('external-source-quotes.json', full_source_quotes)]:
        (HERE / filename).write_text(json.dumps(value, indent=2, ensure_ascii=False)+'\n')
    print(json.dumps({k: v for k, v in result.items() if not isinstance(v, (dict, list))}))


if __name__ == '__main__':
    main()
