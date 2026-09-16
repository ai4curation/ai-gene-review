#!/usr/bin/env python3
"""Validate provenance and publication gates before reusing a Pages artifact."""

import argparse
import json
import hashlib
from pathlib import Path
from typing import Any

BUDGET = 1_000_000_000
ARCHIVE_BUDGET = 1_073_741_824
REQUIRED_STEPS = {
    'Render all gene review HTML pages', 'Render project pages',
    'Validate module YAML files', 'Render module pages',
    'Deploy browser app (data.js + index.html)', 'Stage GitHub Pages artifact',
    'Summarize staged Pages site', 'Upload Pages diagnostics',
    'Upload GitHub Pages artifact',
}


def validate_source(run: dict[str, Any], jobs: dict[str, Any], artifacts: dict[str, Any],
                    repository: str, branch: str, workflow_id: int) -> dict[str, int]:
    """A legacy PR failure is allowed; failed or untrusted builds are not."""
    if (run.get('status') != 'completed'
            or run.get('conclusion') not in {'success', 'failure'}
            or run.get('event') not in {'schedule', 'workflow_dispatch'}
            or run.get('workflow_id') != workflow_id
            or run.get('path') != '.github/workflows/generate-pages.yaml'
            or run.get('head_branch') != branch
            or run.get('head_repository', {}).get('full_name') != repository):
        raise ValueError('Source must be a completed Build and deploy site run from this repository default branch')
    builds = [j for j in jobs['jobs'] if j['name'] == 'generate-pages']
    if len(builds) != 1:
        raise ValueError('Expected exactly one generation job in the latest run attempt')
    successful = {s['name'] for s in builds[0]['steps'] if s.get('conclusion') == 'success'}
    # Previously uploaded artifacts retain the step label from before the rename.
    if 'Upload shadow GitHub Pages artifact' in successful:
        successful.add('Upload GitHub Pages artifact')
    if not REQUIRED_STEPS <= successful:
        raise ValueError(f'Build/publication steps did not succeed: {sorted(REQUIRED_STEPS - successful)}')
    selected = {}
    for name in ('pages-diagnostics', 'github-pages'):
        matches = [a for a in artifacts['artifacts'] if a['name'] == name]
        if len(matches) != 1 or matches[0].get('expired') or matches[0].get('size_in_bytes', 0) <= 0:
            raise ValueError(f'Expected exactly one available {name} artifact')
        artifact_id = matches[0].get('id')
        if type(artifact_id) is not int or artifact_id <= 0:
            raise ValueError('Invalid artifact ID')
        selected[name] = artifact_id
    return selected


def validate_manifest(manifest: dict[str, Any], archive: Path) -> None:
    """Recheck the manifest policy and the actual tar size without extracting it."""
    if (manifest.get('deployable') is not True
            or manifest.get('size_budget_bytes') != BUDGET
            or type(manifest.get('total_bytes')) is not int
            or not 0 < manifest['total_bytes'] <= BUDGET
            or manifest.get('linked_source_files_not_staged') != 0
            or manifest.get('broken_local_link_paths') != []
            or manifest.get('off_base_path_urls') != []):
        raise ValueError('Source manifest does not pass the publication policy')
    # Older verified builds have no archive-size field; check their actual tar.
    if manifest.get('archive_size_budget_bytes', ARCHIVE_BUDGET) != ARCHIVE_BUDGET:
        raise ValueError('Unexpected archive budget')
    if archive.is_symlink() or not archive.is_file() or not 0 < archive.stat().st_size <= ARCHIVE_BUDGET:
        raise ValueError('Pages tar archive is missing, empty, or over budget')
    expected_hash = manifest.get('archive_sha256')
    if manifest.get('archive_checksum_required') and not expected_hash:
        raise ValueError('Archive checksum is required by this manifest')
    if expected_hash is not None and expected_hash != archive_sha256(archive):
        raise ValueError('Archive checksum does not match source diagnostics')


def archive_sha256(archive: Path) -> str:
    digest = hashlib.sha256()
    with archive.open('rb') as source:
        for chunk in iter(lambda: source.read(1024 * 1024), b''):
            digest.update(chunk)
    return digest.hexdigest()


def record_archive(manifest_path: Path, archive: Path) -> dict[str, Any]:
    """Bind source diagnostics to the actual uploaded tar, not its estimate."""
    data = json.loads(manifest_path.read_text())
    data['archive_actual_bytes'] = archive.stat().st_size
    data['archive_sha256'] = archive_sha256(archive)
    validate_manifest(data, archive)
    manifest_path.write_text(json.dumps(data, indent=2) + '\n')
    return data


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest='command', required=True)
    source = commands.add_parser('source')
    for name in ('run', 'jobs', 'artifacts', 'repository', 'branch'):
        source.add_argument('--' + name, required=True)
    source.add_argument('--workflow-id', required=True, type=int)
    source.add_argument('--github-output', type=Path)
    manifest = commands.add_parser('manifest')
    manifest.add_argument('--manifest', required=True)
    manifest.add_argument('--archive', required=True, type=Path)
    record = commands.add_parser('record')
    record.add_argument('--manifest', required=True, type=Path)
    record.add_argument('--archive', required=True, type=Path)
    args = parser.parse_args()
    if args.command == 'source':
        run = json.loads(Path(args.run).read_text())
        selected = validate_source(run, json.loads(Path(args.jobs).read_text()),
                                   json.loads(Path(args.artifacts).read_text()),
                                   args.repository, args.branch, args.workflow_id)
        if args.github_output:
            with args.github_output.open('a') as output:
                output.write(f"manifest_artifact_id={selected['pages-diagnostics']}\n")
                output.write(f"pages_artifact_id={selected['github-pages']}\n")
        print(f"Validated source run {run['id']} at {run['head_sha']}: {selected}")
    elif args.command == 'record':
        data = record_archive(args.manifest, args.archive)
        print(f"Recorded actual archive: {data['archive_actual_bytes']} bytes; sha256:{data['archive_sha256']}")
    else:
        data = json.loads(Path(args.manifest).read_text())
        validate_manifest(data, args.archive)
        print(f"Publication checks passed: {data['total_bytes']} site bytes; {args.archive.stat().st_size} tar bytes")


if __name__ == '__main__':
    main()
