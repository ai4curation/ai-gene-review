"""Recovery accepts only validated artifacts from trusted default-branch builds."""

import copy
from pathlib import Path

import pytest
import yaml

from scripts.validate_pages_recovery import BUDGET, REQUIRED_STEPS, validate_manifest, validate_source


def source_inputs():
    return (
        {'status': 'completed', 'conclusion': 'failure', 'event': 'workflow_dispatch',
         'workflow_id': 123, 'path': '.github/workflows/generate-pages.yaml',
         'head_branch': 'main', 'head_repository': {'full_name': 'owner/repo'}},
        {'jobs': [{'name': 'generate-pages', 'conclusion': 'failure', 'steps': [
            {'name': name, 'conclusion': 'success'} for name in REQUIRED_STEPS
        ] + [{'name': 'Create or update regeneration PR', 'conclusion': 'failure'}]}]},
        {'artifacts': [{'id': i, 'name': name, 'expired': False, 'size_in_bytes': 100}
                       for i, name in enumerate(('pages-diagnostics', 'github-pages'), 1)]},
    )


def test_legacy_pr_failure_does_not_disqualify_validated_artifact():
    assert validate_source(*source_inputs(), 'owner/repo', 'main', 123) == {
        'pages-diagnostics': 1, 'github-pages': 2,
    }


@pytest.mark.parametrize('field,value', [
    ('status', 'in_progress'), ('conclusion', 'cancelled'), ('event', 'pull_request'), ('workflow_id', 999),
    ('path', '.github/workflows/other.yaml'), ('head_branch', 'untrusted'),
    ('head_repository', {'full_name': 'fork/repo'}),
])
def test_rejects_untrusted_or_unfinished_source(field, value):
    run, jobs, artifacts = source_inputs()
    run[field] = value
    with pytest.raises(ValueError, match='Source must be'):
        validate_source(run, jobs, artifacts, 'owner/repo', 'main', 123)


@pytest.mark.parametrize('name', sorted(REQUIRED_STEPS))
def test_rejects_any_failed_publication_step(name):
    run, jobs, artifacts = source_inputs()
    next(step for step in jobs['jobs'][0]['steps'] if step['name'] == name)['conclusion'] = 'failure'
    with pytest.raises(ValueError, match='did not succeed'):
        validate_source(run, jobs, artifacts, 'owner/repo', 'main', 123)


@pytest.mark.parametrize('case', ['expired', 'missing', 'duplicate'])
def test_rejects_unavailable_or_ambiguous_artifact(case):
    run, jobs, artifacts = source_inputs()
    if case == 'expired':
        artifacts['artifacts'][0]['expired'] = True
    elif case == 'missing':
        artifacts['artifacts'].pop()
    else:
        artifacts['artifacts'].append(copy.deepcopy(artifacts['artifacts'][0]))
    with pytest.raises(ValueError, match='Expected exactly one available'):
        validate_source(run, jobs, artifacts, 'owner/repo', 'main', 123)


def good_manifest():
    return {'deployable': True, 'size_budget_bytes': BUDGET, 'total_bytes': 10,
            'linked_source_files_not_staged': 0, 'broken_local_link_paths': [], 'off_base_path_urls': []}


@pytest.mark.parametrize('field,value', [
    ('deployable', False), ('size_budget_bytes', BUDGET + 1), ('total_bytes', BUDGET + 1),
    ('total_bytes', True), ('linked_source_files_not_staged', 1),
    ('broken_local_link_paths', ['missing.html']), ('off_base_path_urls', ['/genes/x']),
])
def test_rechecks_publication_policy(tmp_path, field, value):
    archive = tmp_path / 'artifact.tar'
    archive.write_bytes(b'archive')
    manifest = good_manifest()
    manifest[field] = value
    with pytest.raises(ValueError, match='publication policy'):
        validate_manifest(manifest, archive)


def test_checks_actual_archive_size(tmp_path):
    archive = tmp_path / 'artifact.tar'
    with pytest.raises(ValueError, match='archive'):
        validate_manifest(good_manifest(), archive)
    archive.write_bytes(b'archive')
    validate_manifest(good_manifest(), archive)
    with archive.open('wb') as stream:
        stream.truncate(BUDGET + 1)
    with pytest.raises(ValueError, match='archive'):
        validate_manifest(good_manifest(), archive)


def test_deployment_still_requires_opt_in_and_manifest_after_legacy_failure():
    workflow = yaml.safe_load(Path('.github/workflows/generate-pages.yaml').read_text())
    condition = workflow['jobs']['deploy-pages']['if']
    assert 'always()' in condition and '!cancelled()' in condition
    assert "vars.PAGES_ARTIFACT_DEPLOY_ENABLED == 'true'" in condition
    assert "needs.generate-pages.outputs.deployable == 'true'" in condition
    steps = workflow['jobs']['generate-pages']['steps']
    assert REQUIRED_STEPS <= {step.get('name') for step in steps}
    create = next(step['run'] for step in steps if step.get('name') == 'Create or update regeneration PR')
    assert 'PR_URL="$(gh pr create' in create
    assert 'PR_NUMBER="${PR_URL##*/}"' in create
    assert 'gh pr list' not in create[create.index('PR_URL="$(gh pr create'):]


def test_recovery_is_manual_default_branch_only_and_verifies_before_upload():
    workflow = yaml.safe_load(Path('.github/workflows/recover-pages.yaml').read_text())
    triggers = workflow.get('on', workflow.get(True))
    assert set(triggers) == {'workflow_dispatch'}
    job = workflow['jobs']['recover-pages']
    assert "vars.PAGES_ARTIFACT_DEPLOY_ENABLED == 'true'" in job['if']
    assert 'github.event.repository.default_branch' in job['if']
    assert job['environment']['name'] == 'github-pages'
    names = [step.get('name') for step in job['steps']]
    assert names.index('Verify source run and successful publication steps') < names.index('Download source Pages archive')
    assert names.index('Verify manifest and archive size') < names.index('Upload validated archive for deployment')
    assert names.index('Upload validated archive for deployment') < names.index('Deploy validated Pages artifact')
