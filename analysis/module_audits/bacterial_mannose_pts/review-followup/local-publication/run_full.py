"""Run one fresh full validation only after verifying the committed scoped freeze."""
import datetime
import hashlib
import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
CACHE = ROOT / '.cache/module-audit-logs/mannose-20261107/round1-full'


def now():
    return datetime.datetime.now(datetime.timezone.utc).isoformat()


def main():
    state_path = CACHE / 'state.json'
    log = CACHE / 'validate-all.log'
    assert not state_path.exists() and not log.exists(), 'Fresh run only; never overwrite an earlier run.'
    freeze = json.loads((CACHE / 'frozen-publication-inputs.json').read_text())
    head = subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=ROOT, text=True).strip()
    assert head == freeze['head'], (head, freeze['head'])
    for path, expected in freeze['sha256'].items():
        current = (ROOT / path).read_bytes()
        assert hashlib.sha256(current).hexdigest() == expected, path
        assert subprocess.check_output(['git', 'show', head + ':' + path], cwd=ROOT) == current, path
    state = {'status': 'RUNNING', 'head': head, 'frozen_inputs': len(freeze['sha256']),
             'started_at': now(), 'command': ['just', 'validate-all'],
             'log': str(log.relative_to(ROOT))}
    state_path.write_text(json.dumps(state, indent=2) + '\n')
    print(json.dumps(state), flush=True)
    with log.open('w') as stream:
        result = subprocess.run(['just', 'validate-all'], cwd=ROOT, stdout=stream, stderr=subprocess.STDOUT)
    state.update(status='TERMINAL', exit_code=result.returncode, finished_at=now(),
                 log_sha256=hashlib.sha256(log.read_bytes()).hexdigest())
    state_path.write_text(json.dumps(state, indent=2) + '\n')
    print(json.dumps(state), flush=True)
    raise SystemExit(result.returncode)


if __name__ == '__main__':
    main()
