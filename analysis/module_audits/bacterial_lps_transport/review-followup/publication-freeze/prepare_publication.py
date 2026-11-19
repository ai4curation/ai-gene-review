"""Build an exact additive publication allowlist and scoped supersession receipt."""
import hashlib
import json
import subprocess
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
FOLLOWUP = HERE.parent
CACHE = ROOT / '.cache/module-audit-logs/lps-20261107/review-followup'
PUBLISHED = '91ea10e56b187447b0b6d65d905fb715d4605fd0'
OLD_FULL_HEAD = '4dbf88cb9832e29c7d82b073279a997e1faf68eb'
PROJECT_HISTORY = 'history/projects/MODULE_TAXON_AUDIT/2026-11-07T120515Z-codex-4ab8ae.yaml'


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read(path):
    return json.loads(path.read_text())


def git(*args):
    return subprocess.check_output(['git', *args], cwd=ROOT)


def main():
    assert git('rev-parse', 'HEAD').decode().strip() == PUBLISHED
    CACHE.mkdir(parents=True, exist_ok=True)
    assert not (CACHE / 'publication-manifest-sha256.json').exists()
    mapping = read(FOLLOWUP / 'source-packaging/replacement-map.json')['replacements']
    prior = read(HERE / 'prior-publication-manifest.json')
    assert len(prior) == 476
    assert sha(HERE / 'prior-publication-manifest.json') == sha(ROOT / '.cache/module-audit-logs/lps-20261107/publication-manifest-sha256.json')
    implementation = read(FOLLOWUP / 'implementation/handoff.json')
    integration = read(FOLLOWUP / 'module-integration/handoff.json')
    changes = read(FOLLOWUP / 'implementation/supersession.json')['changes']
    changes.update(read(FOLLOWUP / 'module-integration/module-supersession.json')['changes'])
    project_before = read(HERE / 'project-before.json')
    current_inventory = read(ROOT / 'projects/MODULE_TAXON_AUDIT/inventory.json')
    before_inventory = json.loads(git('show', PUBLISHED + ':projects/MODULE_TAXON_AUDIT/inventory.json'))
    assert {r['module']: hashlib.sha256(json.dumps(r, sort_keys=True).encode()).hexdigest() for r in before_inventory['modules']} == project_before['inventory_row_sha256']
    current_rows, previous_rows = current_inventory['modules'], before_inventory['modules']
    assert len(current_rows) == len(previous_rows)
    changed_rows = []
    for before, after in zip(previous_rows, current_rows, strict=True):
        assert before['module'] == after['module']
        if before != after:
            changed_rows.append(before['module'])
    assert changed_rows == ['bacterial_lps_transport']
    assert {k: v for k, v in current_inventory.items() if k != 'modules'} == {k: v for k, v in before_inventory.items() if k != 'modules'}
    assert read(ROOT / 'pages/projects/MODULE_TAXON_AUDIT/inventory.json') == current_inventory
    for path, expected in project_before['files_sha256'].items():
        assert hashlib.sha256(git('show', PUBLISHED + ':' + path)).hexdigest() == expected
    assert set(git('diff', '--cached', '--name-only').decode().splitlines()) == set(mapping)
    assert all(line.startswith('D\t') for line in git('diff', '--cached', '--name-status').decode().splitlines())

    allowlist, provenance, superseded = {}, {}, {}
    def include(path, expected=None, origin='current'):
        if path in mapping:
            row = mapping[path]
            assert expected is None or expected == row['original_sha256']
            assert sha(ROOT / path) == row['original_sha256'], ('local original changed', path)
            original_path = path
            path, expected = row['replacement_path'], row['replacement_sha256']
            origin += ': explicit replacement for ' + original_path
        actual = sha(ROOT / path)
        if expected is not None and actual != expected:
            allowed = changes.get(path)
            if allowed and expected == allowed['before_sha256'] and actual == allowed['after_sha256']:
                superseded[path] = allowed
            elif path in project_before['files_sha256'] and expected == prior[path]:
                superseded[path] = {'full_run_sha256': expected,
                    'published_sha256': project_before['files_sha256'][path], 'current_sha256': actual,
                    'authorization': 'Only LPS inventory row/status notes plus project render; other module rows exact.'}
            else:
                raise AssertionError(('undeclared supersession', path, expected, actual))
        assert not path.startswith('.cache/'), path
        assert path not in allowlist or allowlist[path] == actual
        allowlist[path] = actual
        provenance.setdefault(path, []).append(origin)
    for path, expected in prior.items():
        # Verify the historical manifest describes committed original full-run bytes.
        assert hashlib.sha256(git('show', OLD_FULL_HEAD + ':' + path)).hexdigest() == expected, path
        include(path, expected, 'prior 476-file publication freeze')
    for name, data in [('implementation', implementation), ('module-integration', integration)]:
        release = FOLLOWUP / name / 'handoff.json'
        include(str(release.relative_to(ROOT)), origin=name + ' frozen handoff')
        for field in ('files', 'source_dependencies'):
            for path, expected in data[field].items():
                include(path, expected, name + '/' + field)
    include(PROJECT_HISTORY, origin='new project history')
    for path in project_before['files_sha256']:
        include(path, origin='current LPS-only project update')
    for path in sorted(HERE.rglob('*')):
        if path.is_file() and '__pycache__' not in path.parts:
            include(str(path.relative_to(ROOT)), origin='new publication-freeze artifact')
    receipt = {
        'status': 'FROZEN_PENDING_COMMIT_AND_FULL_RUN', 'prior_publication_head': PUBLISHED,
        'historical_full_validation_head': OLD_FULL_HEAD, 'old_publication_input_count': len(prior),
        'prior_manifest_sha256': sha(HERE / 'prior-publication-manifest.json'),
        'union_before_receipt': len(allowlist), 'supersessions': superseded,
        'cache_replacements': mapping, 'only_tracker_row_changed': changed_rows,
        'no_blanket_source_exclusions': True,
        'input_origins': provenance, 'input_hashes_before_receipt': dict(sorted(allowlist.items())),
        'limits': 'No fresh full-run PASS claimed. Historical original caches remain local; only nine explicit index deletions. Four full-text dependencies are replaced by scoped excerpts, not reconstructed complete articles.'}
    target = HERE / 'publication-receipt.json'
    assert not target.exists()
    target.write_text(json.dumps(receipt, indent=2) + '\n')
    include(str(target.relative_to(ROOT)), origin='publication receipt')
    manifest = CACHE / 'publication-manifest-sha256.json'
    manifest.write_text(json.dumps(dict(sorted(allowlist.items())), indent=2) + '\n')
    (CACHE / 'prepare-summary.json').write_text(json.dumps({'files': len(allowlist),
        'index_deletions': list(sorted(mapping)), 'supersession_count': len(superseded),
        'manifest_sha256': sha(manifest), 'receipt_sha256': sha(target)}, indent=2) + '\n')
    print(json.dumps({'files': len(allowlist), 'supersessions': len(superseded), 'index_deletions': len(mapping),
                      'manifest': str(manifest.relative_to(ROOT))}))


if __name__ == '__main__':
    main()
