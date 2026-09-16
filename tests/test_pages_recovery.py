"""Recovery accepts only validated artifacts from trusted default-branch builds."""

import copy
import hashlib
import json
from pathlib import Path

import pytest
import yaml

from scripts.validate_pages_recovery import ARCHIVE_BUDGET, BUDGET, REQUIRED_STEPS, validate_manifest, validate_source


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


@pytest.mark.parametrize('upload_name', [
    'Upload GitHub Pages artifact', 'Upload shadow GitHub Pages artifact',
])
@pytest.mark.parametrize('conclusion', ['success', 'failure'])
def test_upload_step_rename_preserves_validation_of_existing_builds(upload_name, conclusion):
    run, jobs, artifacts = source_inputs()
    step = next(s for s in jobs['jobs'][0]['steps'] if 'GitHub Pages artifact' in s['name'] and s['name'].startswith('Upload'))
    step.update(name=upload_name, conclusion=conclusion)
    if conclusion == 'success':
        assert validate_source(run, jobs, artifacts, 'owner/repo', 'main', 123)['github-pages'] == 2
    else:
        with pytest.raises(ValueError, match='did not succeed'):
            validate_source(run, jobs, artifacts, 'owner/repo', 'main', 123)


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
        stream.truncate(ARCHIVE_BUDGET + 1)
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
    workflow = yaml.safe_load(Path('.github/workflows/deploy-existing-pages.yaml').read_text())
    triggers = workflow.get('on', workflow.get(True))
    assert set(triggers) == {'workflow_dispatch'}
    job = workflow['jobs']['deploy-existing-pages']
    assert "vars.PAGES_ARTIFACT_DEPLOY_ENABLED == 'true'" in job['if']
    assert 'github.event.repository.default_branch' in job['if']
    assert job['environment']['name'] == 'github-pages'
    names = [step.get('name') for step in job['steps']]
    assert names.index('Verify source run and successful publication steps') < names.index('Download source Pages archive')
    assert names.index('Verify manifest and archive size') < names.index('Upload validated archive for deployment')
    assert names.index('Upload validated archive for deployment') < names.index('Deploy validated Pages artifact')


def test_recovery_upload_name_matches_pages_deployment():
    workflow = yaml.safe_load(Path('.github/workflows/deploy-existing-pages.yaml').read_text())
    steps = workflow['jobs']['deploy-existing-pages']['steps']
    upload = next(step for step in steps if step.get('name') == 'Upload validated archive for deployment')
    deploy = next(step for step in steps if step.get('name') == 'Deploy validated Pages artifact')
    assert upload['with']['name'] == deploy['with']['artifact_name'] == 'github-pages'
    assert set(upload['with']) == {'name', 'path', 'if-no-files-found', 'retention-days'}
    assert upload['with']['path'] == 'payload/artifact.tar'


def test_recovery_and_normal_build_have_identical_separate_budgets():
    from ai_gene_review.tools.stage_pages import PAGES_ARCHIVE_BUDGET_BYTES, PAGES_SIZE_BUDGET_BYTES
    assert BUDGET == PAGES_SIZE_BUDGET_BYTES
    assert ARCHIVE_BUDGET == PAGES_ARCHIVE_BUDGET_BYTES


def test_checksum_detects_corruption_without_requiring_exact_size_estimate(tmp_path):
    archive = tmp_path / 'artifact.tar'
    archive.write_bytes(b'archive')
    manifest = good_manifest()
    manifest['archive_bytes'] = 1234  # An estimate is not an integrity claim.
    manifest['archive_size_budget_bytes'] = ARCHIVE_BUDGET
    manifest['archive_checksum_required'] = True
    with pytest.raises(ValueError, match='checksum is required'):
        validate_manifest(manifest, archive)
    manifest['archive_sha256'] = hashlib.sha256(b'archive').hexdigest()
    validate_manifest(manifest, archive)
    archive.write_bytes(b'Archive')  # Same byte count, different contents.
    with pytest.raises(ValueError, match='checksum does not match'):
        validate_manifest(manifest, archive)


def test_record_binds_manifest_to_the_actual_archive(tmp_path):
    from scripts.validate_pages_recovery import record_archive

    archive = tmp_path / 'artifact.tar'
    archive.write_bytes(b'actual tar bytes')
    manifest_path = tmp_path / 'manifest.json'
    manifest = good_manifest()
    manifest['archive_checksum_required'] = True
    manifest_path.write_text(json.dumps(manifest))
    record_archive(manifest_path, archive)
    recorded = json.loads(manifest_path.read_text())
    assert recorded['archive_actual_bytes'] == len(b'actual tar bytes')
    assert recorded['archive_sha256'] == hashlib.sha256(b'actual tar bytes').hexdigest()
    validate_manifest(recorded, archive)


def test_archive_cap_allows_tar_overhead_without_raising_site_limit(tmp_path):
    archive = tmp_path / 'artifact.tar'
    with archive.open('wb') as stream:
        stream.truncate(BUDGET + 1)
    validate_manifest(good_manifest(), archive)
    manifest = good_manifest()
    manifest['total_bytes'] = BUDGET + 1
    with pytest.raises(ValueError, match='publication policy'):
        validate_manifest(manifest, archive)


def test_source_records_checksum_before_uploading_diagnostics_and_deploying():
    job = yaml.safe_load(Path('.github/workflows/generate-pages.yaml').read_text())['jobs']['generate-pages']
    names = [step.get('name') for step in job['steps']]
    assert names.index('Upload GitHub Pages artifact') < names.index('Record uploaded archive checksum')
    assert names.index('Record uploaded archive checksum') < names.index('Upload Pages diagnostics')
    assert "steps.archive-check.outcome == 'success'" in job['outputs']['deployable']
    record = next(step for step in job['steps'] if step.get('id') == 'archive-check')
    assert "steps.pages-summary.outputs.deployable == 'true'" in record['if']
    assert 'if [ ! -f "$PAGES_ARCHIVE_PATH" ]' in record['run']
    assert '::error title=Pages archive missing::' in record['run']
