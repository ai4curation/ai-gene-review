"""Restore byte-identical missing public cache inputs; never replace a file."""
import argparse
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def safe_path(root, relative, cache=False):
    rel = Path(relative)
    if rel.is_absolute() or '..' in rel.parts or (cache and rel.parts[0] != '.cache'):
        raise ValueError(f'Unsafe relative path: {relative}')
    candidate = root / rel
    for path in [candidate, *candidate.parents]:
        if path == root:
            break
        if path.is_symlink():
            raise ValueError(f'Refusing symlink: {path}')
    return candidate


def restore(root, verify_only=False):
    root = root.resolve()
    mapping = json.loads((HERE / 'mapping.json').read_text())
    prepared = []
    for row in mapping['files']:
        source = safe_path(HERE, row['bundle_path'])
        target = safe_path(root, row['cache_path'], cache=True)
        if sha(source) != row['sha256'] or source.stat().st_size != row['bytes']:
            raise ValueError(f'Bundle integrity failure: {source}')
        if target.exists() and (not target.is_file() or sha(target) != row['sha256']):
            raise ValueError(f'Refusing mismatched existing cache input: {target}')
        if verify_only and not target.exists():
            raise ValueError(f'Missing cache input: {target}')
        prepared.append((source, target, row['sha256']))
    restored = unchanged = 0
    # All conflicts are checked before any writes. Exclusive creation also refuses
    # replacement if another process creates a destination after the preflight.
    for source, target, digest in prepared:
        if target.exists():
            unchanged += 1
            continue
        target.parent.mkdir(parents=True, exist_ok=True)
        safe_path(root, str(target.relative_to(root)), cache=True)
        try:
            with target.open('xb') as handle:
                handle.write(source.read_bytes())
            restored += 1
        except FileExistsError:
            if not target.is_file() or sha(target) != digest:
                raise ValueError(f'Concurrent mismatched cache input: {target}') from None
            unchanged += 1
        if sha(target) != digest:
            raise ValueError(f'Restored file failed integrity check: {target}')
    return {'status': 'PASS', 'restored': restored, 'already_identical': unchanged,
            'inputs': mapping['count'], 'bytes': mapping['bytes'], 'verify_only': verify_only}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=HERE.parents[4],
                        help='Checkout root; defaults to the repository containing this bundle')
    parser.add_argument('--verify-only', action='store_true')
    args = parser.parse_args()
    print(json.dumps(restore(args.root, args.verify_only), sort_keys=True))


if __name__ == '__main__':
    main()
