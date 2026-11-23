"""Sequential focused validation/render receipts; no full corpus invocation."""
import datetime
import hashlib
import json
import os
import shutil
import subprocess
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
ENV = {**os.environ, 'UV_NO_SYNC': '1', 'UV_OFFLINE': '1', 'PYTHONDONTWRITEBYTECODE': '1'}
MODULE = 'modules/bacterial_chemotaxis_signal_transduction.yaml'
COMMANDS = [
    ('ECOLI-cheW', ['just', 'validate', 'ECOLI', 'cheW']),
    ('BACSU-cheY', ['just', 'validate', 'BACSU', 'cheY']),
    ('module-schema', ['.venv/bin/linkml-validate', '--schema', 'src/ai_gene_review/schema/gene_review.yaml', '--target-class', 'ModuleReview', MODULE]),
    ('module-conformance', ['.venv/bin/python', '-B', '-m', 'ai_gene_review.validation.module_validator', MODULE]),
    ('history-cheW', ['just', 'validate-history', 'history/genes/ECOLI/cheW/2026-11-07T133537Z-codex-bdfd75.yaml']),
    ('history-cheY', ['just', 'validate-history', 'history/genes/BACSU/cheY/2026-11-07T133537Z-codex-890390.yaml']),
    ('history-module', ['just', 'validate-history', 'history/modules/bacterial_chemotaxis_signal_transduction/2026-11-07T133537Z-codex-f576a1.yaml']),
    ('render-cheW', ['just', 'render', 'ECOLI', 'cheW']),
    ('render-cheY', ['just', 'render', 'BACSU', 'cheY']),
    ('render-module', ['just', 'render-module', MODULE]),
]


def main():
    result = {'status': 'RUNNING', 'checks': []}
    for name, command in COMMANDS:
        assert shutil.disk_usage(ROOT).free > 256 * 1024 * 1024
        start = datetime.datetime.now(datetime.timezone.utc).isoformat()
        log = HERE / (name + '.log')
        with log.open('w') as output:
            proc = subprocess.run(command, cwd=ROOT, env=ENV, stdout=output, stderr=subprocess.STDOUT, check=False)
        result['checks'].append({'name': name, 'command': command, 'cwd': str(ROOT),
                                 'started_at': start, 'finished_at': datetime.datetime.now(datetime.timezone.utc).isoformat(),
                                 'exit_code': proc.returncode, 'log': str(log.relative_to(ROOT)),
                                 'log_sha256': hashlib.sha256(log.read_bytes()).hexdigest()})
        (HERE / 'results.json').write_text(json.dumps(result, indent=2) + '\n')
        print(name, proc.returncode, flush=True)
        if proc.returncode:
            result['status'] = 'FAILED_STOPPED'
            (HERE / 'results.json').write_text(json.dumps(result, indent=2) + '\n')
            return
    result['status'] = 'PASS'
    (HERE / 'results.json').write_text(json.dumps(result, indent=2) + '\n')


if __name__ == '__main__':
    main()
