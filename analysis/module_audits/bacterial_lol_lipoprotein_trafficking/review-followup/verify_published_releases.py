"""Verify both immutable Lol releases with one explicit non-source runtime exception."""

import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    exception = json.loads((HERE / "publication-runtime-exception.json").read_text())
    merged = {}
    for rel in ["handoff.json", "module-integration/handoff.json"]:
        data = json.loads((HERE / rel).read_text())
        for field in ["files", "source_dependencies"]:
            for name, digest in data[field].items():
                if name in merged:
                    assert merged[name] == digest, (
                        "Conflicting current release hash",
                        name,
                    )
                merged[name] = digest
    runtime = exception["path"]
    assert merged.pop(runtime) == exception["preserved_local_sha256"]
    if (ROOT / runtime).exists():
        assert sha(ROOT / runtime) == exception["preserved_local_sha256"]
    assert (
        sha(ROOT / exception["source_counterpart"])
        == exception["source_counterpart_sha256"]
    )
    for name, digest in merged.items():
        assert sha(ROOT / name) == digest, name
    print(
        json.dumps(
            {
                "status": "PASS",
                "mandatory_source_and_artifact_inputs": len(merged),
                "runtime_exception": runtime,
                "local_runtime_hash_checked": (ROOT / runtime).exists(),
                "missing_biological_sources": 0,
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
