"""Check the two exact round3 edits; run from any working directory."""
from pathlib import Path
from copy import deepcopy
import hashlib
import json
import importlib.util
import yaml

AUDIT = Path(__file__).resolve().parent
ROOT = AUDIT.parents[3]
BASE = json.loads((AUDIT / 'baseline.json').read_text())
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
checks = {}
for name, before in BASE['reviews'].items():
    current = yaml.safe_load((ROOT / name).read_text())
    original_rows = before['existing_annotations']
    rows = current['existing_annotations']
    payload = lambda rs: [{k: v for k, v in r.items() if k != 'review'} for r in rs]
    assert payload(rows) == payload(original_rows), name
    expected = deepcopy(before)
    if '/PSEPK/' in name:
        assert rows[12]['term']['id'] == 'GO:0098562'
        review = rows[12]['review']
        assert review['action'] == 'UNDECIDED'
        assert 'proposed_replacement_terms' not in review
        assert rows[7]['term']['id'] == 'GO:0009898'
        assert rows[7]['review']['action'] == 'UNDECIDED'
        assert review['supported_by'] == rows[7]['review']['supported_by']
        assert not any(c.get('locations') for c in current['core_functions'])
        expected['existing_annotations'][12]['review'] = review
    else:
        assert rows[7]['term']['id'] == 'GO:0055129'
        old = original_rows[7]['review']['supported_by']
        assert len(old) == 3 and old[0] == old[2]
        assert rows[7]['review']['supported_by'] == old[:2]
        expected['existing_annotations'][7]['review']['supported_by'] = old[:2]
    assert current == expected, 'Unexpected structured edit: ' + name
    checks[name] = {'ordered_machine_payloads_preserved': len(rows),
                    'core_functions_unchanged': True,
                    'only_exact_authorized_edit': True,
                    'historical_NEW': sum(r['review']['action'] == 'NEW' for r in original_rows),
                    'active_NEW': sum(r['review']['action'] == 'NEW' and not r.get('retired') for r in rows),
                    'sha256': sha(ROOT / name)}
for name, digest in BASE['protected_sha256'].items():
    assert sha(ROOT / name) == digest, name
# Import only: calling the module main would rewrite the root-owned audit results.
checker = ROOT / 'modules/bacterial_fused_puta_proline_catabolism-source-analysis/check_module.py'
spec = importlib.util.spec_from_file_location('puta_checker', checker)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
p = 'genes/PSEPK/putA/putA-ai-review.yaml'
old_claims = set(module.curated_functions(BASE['reviews'][p]))
new_claims = set(module.curated_functions(yaml.safe_load((ROOT / p).read_text())))
assert old_claims - new_claims == {'GO:0009898'}
assert not new_claims - old_claims
assert {'GO:0004657', 'GO:0003842'} <= new_claims
ledger = yaml.safe_load((AUDIT / 'action-ledger-addition.yaml').read_text())
assert ledger['changes'][0]['after_review'] == yaml.safe_load((ROOT / p).read_text())['existing_annotations'][12]['review']
result = {'status': 'PASS', 'baseline_head': BASE['head'], 'reviews': checks,
          'ordered_rows_preserved': sum(len(x['existing_annotations']) for x in BASE['reviews'].values()),
          'protected_sources_preserved': len(BASE['protected_sha256']),
          'root_checker_impact': {'removed_retained_claim': 'GO:0009898',
                                  'required_catalytic_functions_unchanged': True,
                                  'capacity_output_source_hashes_need_refresh': True}}
(AUDIT / 'proof.json').write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps(result, indent=2))
