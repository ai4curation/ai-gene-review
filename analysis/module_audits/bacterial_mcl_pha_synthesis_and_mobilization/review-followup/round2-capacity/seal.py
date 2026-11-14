"""Read-only verification of the explicitly accepted round-two release."""

import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
AUDIT = HERE.parents[1]
IMPL = HERE.parent / "round2-implementation"
HANDOFF_SHA256 = "1373ae9006a19fdea2dbf17620e64ba9b99dd800c8ba080f36349509dc273071"


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def verify_seal():
    # Pin the exact parent-authorized receipt, not a mutable latest-file lookup.
    assert sha(IMPL / "handoff.json") == HANDOFF_SHA256
    handoff = json.loads((IMPL / "handoff.json").read_text())
    assert len(handoff["source_dependencies"]) == 433
    for name, digest in {**handoff["source_dependencies"], **handoff["files"]}.items():
        assert (ROOT / name).is_file(), f"Missing sealed input: {name}"
        assert sha(ROOT / name) == digest, f"Changed sealed input: {name}"
    repair = json.loads((HERE / "phaA-quote-repair.json").read_text())
    target = ROOT / repair["target"]
    assert sha(target) == repair["successor_sha256"]
    current = target.read_text()
    offset = repair["removed_character_offset"]
    restored = current[:offset] + repair["removed_text"] + current[offset:]
    assert hashlib.sha256(restored.encode()).hexdigest() == repair["prior_sha256"]
    assert sha(ROOT / repair["primary_source"]) == repair["primary_source_sha256"]
    assert repair["primary_identity_quote"] in (ROOT / repair["primary_source"]).read_text()
    assert sha(ROOT / repair["old_closure"]) == repair["old_closure_sha256"]
    assert sha(ROOT / repair["history"]) == repair["history_sha256"]
    handoff["files"][repair["target"]] = repair["successor_sha256"]
    handoff["files"][repair["history"]] = repair["history_sha256"]
    return handoff
