"""In-memory negative controls for dependency union and exact supersession gates."""
import copy
import hashlib
import importlib.util
import json
from pathlib import Path
from unittest.mock import patch

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
SPEC = importlib.util.spec_from_file_location('current_closure_guards', HERE / 'check_current.py')
CURRENT = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(CURRENT)


def run():
    original = CURRENT.read_json
    implementation = HERE.parent / 'implementation/handoff.json'
    missing = 'publications/PMID_UNDECLARED_SOURCE_CONTROL.md'
    assert not (ROOT / missing).exists()
    before = {str(p): hashlib.sha256(p.read_bytes()).hexdigest() for p in HERE.iterdir() if p.is_file()}
    outcomes = []
    for kind in ('unfrozen_source_dependency', 'unauthorized_hash_change'):
        def altered(path, kind=kind):
            data = original(path)
            if path == implementation:
                data = copy.deepcopy(data)
                if kind == 'unfrozen_source_dependency':
                    data.setdefault('source_dependencies', {})[missing] = '0' * 64
                else:
                    key = next(iter(data['files']))
                    data['files'][key] = '0' * 64
            return data

        with patch.object(CURRENT, 'read_json', altered):
            try:
                CURRENT.main()
            except (AssertionError, FileNotFoundError) as error:
                if kind == 'unfrozen_source_dependency':
                    assert isinstance(error, FileNotFoundError) and missing in str(error)
                else:
                    assert isinstance(error, AssertionError) and '00000000' in str(error)
                outcomes.append({'control': kind, 'detected': True, 'exception': type(error).__name__})
            else:
                raise AssertionError(('guard failed', kind))
    after = {str(p): hashlib.sha256(p.read_bytes()).hexdigest() for p in HERE.iterdir() if p.is_file()}
    assert after == before, 'negative controls must fail before writing outputs'
    (HERE / 'guard-results.json').write_text(json.dumps({'status': 'PASS', 'controls': outcomes,
        'historical_or_current_inputs_mutated': False}, indent=2) + '\n')
    print('PASS: missing source dependency and unauthorized hash change both rejected before output writes')


if __name__ == '__main__':
    run()
