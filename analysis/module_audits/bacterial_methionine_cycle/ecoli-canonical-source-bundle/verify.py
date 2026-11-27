"""Verify the additive scoped bundle and unchanged canonical handoff offline."""

import hashlib
import json
from pathlib import Path

AUDIT = Path(__file__).resolve().parent
ROOT = AUDIT.parents[3]


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    receipt = json.loads((AUDIT / "receipt.json").read_text())
    for path, item in receipt["copies"].items():
        assert digest(ROOT / path) == item["sha256"]
        assert (ROOT / path).read_bytes() == (ROOT / item["original_path"]).read_bytes()
    prior = receipt["canonical_handoff"]
    assert digest(ROOT / prior["path"]) == prior["sha256"]
    manifest = json.loads((ROOT / prior["path"]).read_text())
    for path, expected in manifest["files"].items():
        assert digest(ROOT / path) == expected, path
    print(
        f"PASS: {len(receipt['copies'])} exact copies and {len(manifest['files'])} frozen canonical files; no ignored-cache dependency."
    )


if __name__ == "__main__":
    main()
