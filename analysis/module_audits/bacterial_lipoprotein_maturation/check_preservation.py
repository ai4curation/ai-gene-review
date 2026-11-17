"""Verify source payloads, consultation releases and manually selected reference quotes."""
from pathlib import Path
import hashlib
import json
import yaml

A = Path('analysis/module_audits/bacterial_lipoprotein_maturation')
base = json.loads((A / 'baseline.json').read_text())
for path, expected in base['protected_files_sha256'].items():
    assert hashlib.sha256(Path(path).read_bytes()).hexdigest() == expected, path
original_rows = 0
for path, record in base['reviews'].items():
    before = record['document']['existing_annotations']
    after = yaml.safe_load(Path(path).read_text())['existing_annotations']
    assert len(before) == len(after), path
    for a, b in zip(before, after, strict=True):
        assert {k: v for k, v in a.items() if k != 'review'} == {
            k: v for k, v in b.items() if k != 'review'
        }, path
        assert (a['review']['action'] == 'NEW') == (b['review']['action'] == 'NEW'), path
    original_rows += len(before)
assert original_rows == 73
handoffs = sorted(A.glob('*-consultation/handoff.*'))
assert len(handoffs) >= 8
verified = 0
for path in handoffs:
    record = yaml.safe_load(path.read_text())
    manifest = record.get('files', record.get('files_sha256', {}))
    assert manifest, path
    for file, expected in manifest.items():
        if isinstance(expected, dict):
            expected = expected['sha256']
        assert hashlib.sha256(Path(file).read_bytes()).hexdigest() == expected, file
        verified += 1
    for key in ['consumed_external_sources_sha256', 'unchanged_inputs_sha256',
                'unchanged_dependency_sha256', 'source_protection', 'protected_sources']:
        for file, expected in record.get(key, {}).items():
            if isinstance(expected, dict):
                expected = expected['sha256']
            assert hashlib.sha256(Path(file).read_bytes()).hexdigest() == expected, file
module = yaml.safe_load(Path('modules/bacterial_lipoprotein_maturation.yaml').read_text())
quotes = 0
for ref in module['references']:
    source = Path('publications/' + ref['id'].replace(':', '_') + '.md').read_text()
    metadata = yaml.safe_load(source.split('---', 2)[1])
    assert ' '.join(metadata['title'].split()) == ' '.join(ref['title'].split()), ref['id']
    for finding in ref.get('findings', []):
        if 'supporting_text' in finding:
            assert ' '.join(finding['supporting_text'].split()) in ' '.join(source.split()), ref['id']
            quotes += 1
print(json.dumps({'original_rows': original_rows, 'baseline_sources': 57,
                  'handoffs': len(handoffs), 'verified_handoff_paths': verified,
                  'module_reference_quotes': quotes}))
