"""Run only owned focused checks, helper histories and renders; no whole corpus."""
import json
import os
import subprocess
import time
from pathlib import Path

from ai_gene_review.render import render_gene_review

A = Path('analysis/module_audits/bacterial_nitrogen_regulatory_pts/ecoli-native-review-20261107')
assert not (A / 'handoff.json').exists()
ROOTPY = '/Users/cjm/orca/workspaces/ai-gene-review/aigr-modules-taxon/.venv/bin/python'
env = dict(os.environ, UV_PROJECT_ENVIRONMENT=str(Path(ROOTPY).parent.parent), UV_NO_SYNC='1', PYTHONPATH=str(Path.cwd() / 'src'), PYTHONDONTWRITEBYTECODE='1')
checks = []


def run(cmd, name):
    start = time.time()
    r = subprocess.run(cmd, env=env, text=True, capture_output=True)
    (A / (name + '.log')).write_text(r.stdout + r.stderr)
    checks.append({'command': cmd, 'log': str(A / (name + '.log')), 'exit_code': r.returncode, 'seconds': time.time() - start})
    (A / 'focused-checks.json').write_text(json.dumps(checks, indent=2) + '\n')
    assert r.returncode == 0, (name, r.stdout, r.stderr)
    return r.stdout


run(['just', 'validate', 'ECOLI', 'ptsO'], 'ptsO-validation-final')
histories = []
for gene in ('ptsP', 'ptsO', 'ptsN'):
    out = run([ROOTPY, '-P', 'scripts/new_history.py', '--kind', 'gene', '--organism', 'ECOLI', '--slug', gene,
               '--event', 'CREATE', '--outcome', 'changed', '--actor-name', 'codex', '--agent-tool', 'codex',
               '--summary', f'Review native E. coli nitrogen-PTS {gene}',
               '--sections', 'description,existing_annotations,references,core_functions,notes',
               '--details', 'Review all seeded rows while preserving ordered source payloads and qualifiers. Distinguish native PtsP-NPr-PtsN phosphotransfer from in-vitro crosstalk and other-species outputs. Use actual tree/PAINT ancestry and target evidence without guessed losses. No NEW rows; document abstract/full-text limits and the shared failed Falcon attempt. Focused gene, reference and preservation checks plus helper-history validation and render are recorded in the owned consultation.'], gene + '-history-create')
    candidates = [line.strip() for line in out.splitlines() if line.strip().startswith('history/') and line.strip().endswith('.yaml')]
    assert len(candidates) == 1, out
    history = candidates[0]
    histories.append(history)
    run(['just', 'validate-history', history], gene + '-history-validate')
    p = Path(f'genes/ECOLI/{gene}/{gene}-ai-review.yaml')
    target = p.with_suffix('.html')
    temporary = target.with_suffix('.html.render-tmp')
    render_gene_review(p, output_path=temporary)
    temporary.replace(target)
    checks.append({'command': f'render_gene_review({p}) with adjacent temporary output then atomic rename', 'exit_code': 0, 'output': str(target)})
(A / 'histories.json').write_text(json.dumps(histories, indent=2) + '\n')
(A / 'focused-checks.json').write_text(json.dumps(checks, indent=2) + '\n')
print(json.dumps({'status': 'PASS', 'histories': histories, 'renders': 3}))
