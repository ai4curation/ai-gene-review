"""Inspect SequenceCache files for an incremental CI cache generation; never fetch."""

import argparse
import hashlib
import json
import re
from pathlib import Path


def manifest(cache_dir: Path) -> dict[str, str]:
    """Hash regular, syntactically valid .seq/.sv files without changing them.

    These checks detect empty, malformed or unexpected files. They do not verify
    sequence completeness or provenance; the normal SequenceCache writer remains
    the source of entries.
    Version files are optional and may also be populated independently.
    """
    if cache_dir.is_symlink():
        raise ValueError(f"Cache directory is a symlink: {cache_dir}")
    if not cache_dir.exists():
        return {}
    result = {}
    for path in sorted(cache_dir.iterdir()):
        if path.is_symlink() or not path.is_file():
            raise ValueError(f"Not a regular cache file: {path}")
        if not re.fullmatch(r"[A-Z0-9]+(?:-[1-9][0-9]*)?\.(seq|sv)", path.name):
            raise ValueError(f"Unexpected cache filename: {path}")
        content = path.read_bytes()
        pattern = rb"[A-Z]+" if path.suffix == ".seq" else rb"[1-9][0-9]*"
        if re.fullmatch(pattern, content.strip()) is None:
            raise ValueError(f"Invalid cache content: {path}")
        result[path.name] = hashlib.sha256(content).hexdigest()
    return result


def generation(before: dict[str, str], after: dict[str, str]) -> tuple[bool, str]:
    """Only normal additions may extend a restored generation."""
    for name, digest in before.items():
        if after.get(name) != digest:
            raise ValueError(f"Restored cache file changed or disappeared: {name}")
    digest = hashlib.sha256(
        json.dumps(after, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()
    return before != after, digest


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("mode", choices=["before", "after"])
    parser.add_argument("--cache-dir", type=Path, required=True)
    parser.add_argument("--snapshot", type=Path, required=True)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    current = manifest(args.cache_dir)
    if args.mode == "before":
        args.snapshot.write_text(json.dumps(current, sort_keys=True) + "\n")
    else:
        if args.output is None:
            parser.error("after requires --output")
        changed, digest = generation(json.loads(args.snapshot.read_text()), current)
        with args.output.open("a") as stream:
            stream.write(f"changed={str(changed).lower()}\ndigest={digest}\n")
        print(f"Sequence cache: {len(current)} files; changed={changed}; digest={digest}")


if __name__ == "__main__":
    main()
