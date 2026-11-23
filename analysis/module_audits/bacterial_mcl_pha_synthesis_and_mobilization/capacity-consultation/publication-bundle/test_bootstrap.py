"""Exercise restoration in isolated directories and prove the frozen release intact."""
import hashlib
import json
from pathlib import Path
import tempfile

from bootstrap import HERE, restore


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    root = HERE.parents[4]
    frozen = HERE.parent / 'handoff.json'
    assert sha(frozen) == 'f628d09c662bd2d0c552f56d8a879d438a162f0d92e59347f2abe11cca663623'
    original = json.loads(frozen.read_text())
    for rel, expected in original['files'].items():
        assert sha(root / rel) == expected, rel
    mapping = json.loads((HERE / 'mapping.json').read_text())
    closure = json.loads((HERE.parent / 'input-closure.json').read_text())
    assert sha(HERE.parent / 'input-closure.json') == mapping['original_input_closure_sha256']
    expected_cache = {p: h for p, h in closure['files'].items() if p.startswith('.cache/')}
    assert {r['cache_path']: r['sha256'] for r in mapping['files']} == expected_cache
    assert mapping['count'] == len(expected_cache) == 56
    assert mapping['bytes'] == sum(r['bytes'] for r in mapping['files']) == 8550156
    with tempfile.TemporaryDirectory(prefix='mcl-cache-bootstrap-') as directory:
        destination = Path(directory)
        first = restore(destination)
        assert first['restored'] == 56 and first['already_identical'] == 0
        for row in mapping['files']:
            assert sha(destination / row['cache_path']) == row['sha256']
        repeat = restore(destination)
        assert repeat['restored'] == 0 and repeat['already_identical'] == 56
        verified = restore(destination, verify_only=True)
        assert verified['restored'] == 0 and verified['already_identical'] == 56
    with tempfile.TemporaryDirectory(prefix='mcl-cache-conflict-') as directory:
        destination = Path(directory)
        bad = destination / mapping['files'][-1]['cache_path']
        bad.parent.mkdir(parents=True)
        bad.write_bytes(b'intentional conflicting fixture\n')
        before = sha(bad)
        try:
            restore(destination)
        except ValueError as error:
            assert 'Refusing mismatched existing' in str(error)
        else:
            raise AssertionError('Existing mismatch was not rejected')
        assert sha(bad) == before
        assert len([p for p in destination.rglob('*') if p.is_file()]) == 1
    with tempfile.TemporaryDirectory(prefix='mcl-cache-symlink-') as directory:
        destination = Path(directory)
        outside = destination / 'outside'
        outside.mkdir()
        (destination / '.cache').symlink_to(outside, target_is_directory=True)
        try:
            restore(destination)
        except ValueError as error:
            assert 'Refusing symlink' in str(error)
        else:
            raise AssertionError('Symlink was not rejected')
        assert not list(outside.iterdir())
    # This run only verifies the live WT; it does not overwrite or restore it.
    live = restore(root, verify_only=True)
    result = {'status': 'PASS', 'cache_inputs': 56, 'source_bytes': 8550156,
              'isolated_restore': first, 'idempotent_repeat': repeat,
              'isolated_verify': verified, 'live_verify': live,
              'mismatch_rejected_without_any_write': True,
              'symlink_rejected_without_any_write': True,
              'original_release_sha256': sha(frozen),
              'original_release_files_unchanged': len(original['files']),
              'closure_cache_coverage_exact': True}
    (HERE / 'verification.json').write_text(json.dumps(result, indent=2, sort_keys=True) + '\n')
    print(json.dumps(result, sort_keys=True))


if __name__ == '__main__':
    main()
