"""Fetch a pinned source, checking existing bytes and every download before use.

The manifest supplies URLs and checksums. A failed publisher fetch falls back to
its documented archive mirror. No source is accepted on filename alone.
"""

import argparse
import hashlib
import io
import os
from pathlib import Path
import tempfile
import urllib.error
import urllib.request
import zipfile

import yaml


def verify(data, manifest):
    actual = {
        "bytes": len(data),
        "sha256": hashlib.sha256(data).hexdigest(),
        "md5": hashlib.md5(data).hexdigest(),
    }
    if any(actual[k] != manifest[k] for k in actual):
        raise ValueError(f"Source integrity mismatch: {actual}")
    return actual


def download(source, manifest):
    request = urllib.request.Request(
        source["url"], headers={"User-Agent": "ai-gene-review-source-fetch/1.0"}
    )
    with urllib.request.urlopen(request, timeout=60) as response:
        data = response.read()
    if source["format"] == "file":
        verify(data, manifest)
        return data
    if source["format"] != "zip":
        raise ValueError(f"Unsupported source format: {source['format']}")
    with zipfile.ZipFile(io.BytesIO(data)) as archive:
        members = [
            n for n in archive.namelist() if Path(n).name == source["member_basename"]
        ]
        if len(members) != 1:
            raise ValueError(f"Expected exactly one archive member; found {members}")
        data = archive.read(members[0])
    verify(data, manifest)
    return data


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument(
        "--source", help="Use only the named manifest source (diagnostic)."
    )
    args = parser.parse_args()
    manifest = yaml.safe_load(args.manifest.read_text())
    if args.output.exists():
        # Never overwrite a damaged or different cached source silently.
        verify(args.output.read_bytes(), manifest)
        print(f"Verified existing source: {args.output}")
        return
    sources = manifest["sources"]
    if args.source:
        sources = [s for s in sources if s["id"] == args.source]
        if not sources:
            raise ValueError(f"Unknown source: {args.source}")
    failures = []
    for source in sources:
        try:
            data = download(source, manifest)
        except (OSError, ValueError, zipfile.BadZipFile) as exc:
            failures.append(f"{source['id']}: {exc}")
            print(f"Source failed verification or retrieval: {failures[-1]}")
            continue
        args.output.parent.mkdir(parents=True, exist_ok=True)
        temporary = None
        try:
            with tempfile.NamedTemporaryFile(
                dir=args.output.parent, delete=False
            ) as handle:
                temporary = Path(handle.name)
                handle.write(data)
            os.replace(temporary, args.output)
        finally:
            if temporary is not None:
                temporary.unlink(missing_ok=True)
        print(
            f"Fetched and verified {len(data)} bytes from {source['id']}: {args.output}"
        )
        return
    raise RuntimeError("All source retrievals failed: " + "; ".join(failures))


if __name__ == "__main__":
    main()
