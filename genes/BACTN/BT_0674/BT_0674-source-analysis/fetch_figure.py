"""Retrieve the inspected publisher figure and verify its pinned content hash."""

import hashlib
import json
from pathlib import Path
import sys
from urllib.request import urlopen


def main():
    if len(sys.argv) != 2:
        raise SystemExit("Usage: fetch_figure.py OUTPUT_PATH")
    source = json.loads(Path(__file__).with_name("provenance.json").read_text())[0]
    output = Path(sys.argv[1])
    with urlopen(source["source_url"], timeout=60) as response:
        content = response.read()
    if hashlib.sha256(content).hexdigest() != source["sha256"]:
        raise SystemExit("Publisher content changed; inspect before updating provenance")
    if output.exists() and output.read_bytes() != content:
        raise SystemExit("Refusing to overwrite a different existing file")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_bytes(content)
    print(f"Verified source saved to {output}")


if __name__ == "__main__":
    main()
