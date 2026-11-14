"""Verify the original seal plus the explicitly authorized quote-only successor."""

import hashlib
import json
from pathlib import Path

import yaml

A = Path(__file__).resolve().parent
ROOT = A.parents[3]


def current_seal():
    original = json.loads((A / "accepted-science-seal.json").read_text())["files"]
    supersession = json.loads((A / "quote-supersession.json").read_text())
    source = ROOT / supersession["source"]
    assert hashlib.sha256(source.read_bytes()).hexdigest() == supersession["source_sha256"]
    assert supersession["new_quote"] in source.read_text()

    def restore_quotes(value):
        if isinstance(value, dict):
            if value.get("supporting_text") == supersession["new_quote"]:
                value["supporting_text"] = supersession["old_quote"]
            for child in value.values():
                restore_quotes(child)
        elif isinstance(value, list):
            for child in value:
                restore_quotes(child)

    result = dict(original)
    for name, entry in supersession["files"].items():
        assert original[name] == entry["prior_sha256"], name
        current = (ROOT / name).read_bytes()
        assert hashlib.sha256(current).hexdigest() == entry["successor_sha256"], name
        restored = yaml.safe_load(current)
        restore_quotes(restored)
        prior_bytes = yaml.safe_dump(restored, sort_keys=False, allow_unicode=True, width=100).encode()
        assert hashlib.sha256(prior_bytes).hexdigest() == entry["prior_sha256"], name
        result[name] = entry["successor_sha256"]
    for name, expected in result.items():
        assert hashlib.sha256((ROOT / name).read_bytes()).hexdigest() == expected, name
    return result
