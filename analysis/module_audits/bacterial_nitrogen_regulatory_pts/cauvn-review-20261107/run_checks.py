"""Run owned focused checks, retaining exact commands, exit statuses, and logs."""
import json
import os
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
AUDIT = Path(__file__).resolve().parent
ENV = dict(os.environ, UV_NO_SYNC='1', PYTHONSAFEPATH='1', PYTHONDONTWRITEBYTECODE='1',
           PYTHONPATH=str(ROOT / 'src'), UV_PROJECT_ENVIRONMENT='/Users/cjm/orca/workspaces/ai-gene-review/aigr-modules-taxon/.venv')
PYTHON = ENV['UV_PROJECT_ENVIRONMENT'] + '/bin/python'
results = []
for gene in ('ptsP', 'ptsH', 'ptsN'):
    cmd = ['just', 'new-history', '--kind', 'gene', '--organism', 'CAUVN', '--slug', gene,
           '--event', 'REVIEW', '--outcome', 'changed', '--actor-name', 'codex', '--agent-tool', 'codex',
           '--summary', 'Complete NA1000 nitrogen-regulatory phosphorelay review',
           '--details', 'Reviewed every seeded row against full primary27109061; PtsP also uses26489861. Preserved original ordered source payloads and qualifiers, with no NEW or retired rows. Distinguished native NA1000 genetics/enriched-fraction chemistry from heterologous BTH and unresolved binary kinetics. Refined valid transferase chemistry, limited sugar-transport propagation, and retained uncertainty for an unverified PtsN kinase target. See cauvn-review-20261107 for immutable seeds, evidence limits, shared Falcon403 provenance and focused checks.',
           '--sections', 'description,existing_annotations,core_functions,references']
    run = subprocess.run(cmd, cwd=ROOT, env=ENV, text=True, capture_output=True, check=False)
    log = AUDIT / 'logs' / f'{gene}-history-create.log'
    log.write_text(run.stdout + run.stderr)
    results.append({'command': cmd, 'exit_code': run.returncode, 'log': str(log.relative_to(ROOT))})
    assert run.returncode == 0, run.stderr
    history = next(line.strip() for line in run.stdout.splitlines() if line.strip().startswith('history/'))
    for label, cmd in [
        ('validate', ['just', 'validate', 'CAUVN', gene]),
        ('history-validate', ['just', 'validate-history', history]),
        ('render', ['just', 'render', 'CAUVN', gene]),
    ]:
        log = AUDIT / 'logs' / f'{gene}-{label}.log'
        with log.open('w') as stream:
            run = subprocess.run(cmd, cwd=ROOT, env=ENV, text=True, stdout=stream, stderr=subprocess.STDOUT, check=False)
        results.append({'command': cmd, 'exit_code': run.returncode, 'log': str(log.relative_to(ROOT))})
        (AUDIT / 'check-results.json').write_text(json.dumps(results, indent=2) + '\n')
        print(gene, label, run.returncode, flush=True)
        if run.returncode:
            raise SystemExit(run.returncode)
