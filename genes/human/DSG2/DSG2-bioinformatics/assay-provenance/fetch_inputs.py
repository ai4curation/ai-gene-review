"""Fetch exact public inputs; stop on failed access or changed content."""
import argparse
import hashlib
import io
import json
from pathlib import Path
import urllib.request
import zipfile


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest", type=Path, default=Path(__file__).with_name("input-manifest.json"))
    parser.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args()
    manifest = json.loads(args.manifest.read_text())
    args.output_dir.mkdir(parents=True, exist_ok=True)
    for source in manifest["sources"]:
        target = args.output_dir / source["filename"]
        if Path(source["filename"]).name != source["filename"]:
            raise ValueError("Source filename must be a basename")
        if target.exists():
            data = target.read_bytes()
        else:
            request = urllib.request.Request(source["url"], headers={"User-Agent": "DSG2-evidence-reproduction/1.0"})
            with urllib.request.urlopen(request, timeout=120) as response:
                data = response.read()
            if "zip_member_basename" in source:
                with zipfile.ZipFile(io.BytesIO(data)) as archive:
                    names = [name for name in archive.namelist()
                             if Path(name).name == source["zip_member_basename"]]
                    if len(names) != 1:
                        raise ValueError("Expected one exact supplementary workbook member")
                    data = archive.read(names[0])
        actual = hashlib.sha256(data).hexdigest()
        if actual != source["sha256"]:
            raise ValueError(f"Changed input {source['key']}: {actual}; do not substitute silently")
        if not target.exists():
            target.write_bytes(data)
        print(source["key"], actual)


if __name__ == "__main__":
    main()
