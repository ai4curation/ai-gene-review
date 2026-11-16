"""Check literature quotes, citation identity and preservation of frozen source files."""
import hashlib
import json
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def normalize(text):
    return ' '.join(text.split())


def main():
    ledger = yaml.safe_load((HERE / 'ledger.yaml').read_text())
    references = ledger['references']
    inputs = {}
    findings = 0
    for ref in references:
        cache = ROOT / ref['access']['publication_cache']
        source = ROOT / ref['access']['consulted_text']
        metadata = yaml.safe_load(cache.read_text().split('---', 2)[1])
        assert ref['id'] == 'PMID:' + str(metadata['pmid'])
        assert ref['title'] == metadata['title']
        assert normalize(ref['checked_quote']) in normalize(source.read_text()), ref['id']
        assert digest(source) == ref['access']['consulted_text_sha256']
        assert ref['reference_review']['correctness'] == 'VERIFIED'
        assert ref['findings']
        findings += len(ref['findings'])
        inputs[str(cache.relative_to(ROOT))] = digest(cache)
        inputs[str(source.relative_to(ROOT))] = digest(source)
    assert len(references) == 9
    assert sum(r['publication_type'] == 'REVIEW' for r in references) == 3
    baseline = json.loads((HERE.parent / 'baseline.json').read_text())
    for name, expected in baseline['protected_files_sha256'].items():
        assert digest(ROOT / name) == expected, name
    assert not list(HERE.glob('*deep-research-falcon.md'))
    provider = json.loads((HERE / 'provider-attempt.json').read_text())
    assert digest(ROOT / provider['log_path']) == provider['log_sha256']
    assert '403' in (ROOT / provider['log_path']).read_text()
    result = {'status': 'PASS', 'references_manually_assessed': len(references),
              'review_articles': 3, 'primary_articles': 6,
              'checked_verbatim_quotes': len(references), 'source_scoped_findings': findings,
              'protected_baseline_sources': len(baseline['protected_files_sha256']),
              'inputs_sha256': inputs, 'provider': 'Real Falcon request failed403; no report generated',
              'scope': 'Quote/source integrity check; scientific judgments are manual and documented.'}
    (HERE / 'validation.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({k: v for k, v in result.items() if k != 'inputs_sha256'}, indent=2))


if __name__ == '__main__':
    main()
