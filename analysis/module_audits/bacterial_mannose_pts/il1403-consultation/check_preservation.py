"""Verify IL1403 seed payloads, sources, and the earlier frozen E. coli handoff."""

import hashlib
import json
from collections import Counter
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    seed = HERE.parent / "additional-seed-baseline.json"
    baseline = json.loads(seed.read_text())
    summaries = []
    count = 0
    for path, frozen in baseline["genes"].items():
        old = frozen["document"]["existing_annotations"]
        current = yaml.safe_load((ROOT / path).read_text())
        new = current["existing_annotations"]
        assert current["status"] == "COMPLETE"
        assert len(old) == len(new)
        for i, (a, b) in enumerate(zip(old, new, strict=True)):
            assert {k: v for k, v in a.items() if k != "review"} == {
                k: v for k, v in b.items() if k != "review"
            }, (path, i)
            assert a.get("retired", False) == b.get("retired", False)
            assert b["review"]["action"] not in {"NEW", "PENDING"}
        count += len(new)
        summaries.append(
            {
                "path": path,
                "seed_sha256": frozen["sha256"],
                "review_sha256": sha(ROOT / path),
                "rows": len(new),
                "actions": dict(Counter(r["review"]["action"] for r in new)),
            }
        )
    sources = dict(baseline["protected_files_sha256"])
    consulted = json.loads((HERE / "consulted-sources.json").read_text())
    sources.update(consulted)
    for path, digest in sources.items():
        assert sha(ROOT / path) == digest, path
    previous_path = HERE.parent / "ecoli-consultation/handoff.json"
    previous = json.loads(previous_path.read_text())
    files = previous["files"]
    if isinstance(files, list):
        files = {row["path"]: row["sha256"] for row in files}
    followup_dir = HERE.parent / "ecoli-consultation/core-contribution-followup"
    followup = json.loads((followup_dir / "handoff.json").read_text())
    for path, digest in followup["files"].items():
        assert sha(ROOT / path) == digest, ("Ecoli additive followup", path)
    superseded = json.loads((followup_dir / "preservation.json").read_text())[
        "authorized_superseded_paths"
    ]
    for path, digest in files.items():
        expected = superseded[path]["after"] if path in superseded else digest
        assert sha(ROOT / path) == expected, ("frozen Ecoli handoff", path)
    assert count == 15
    result = {
        "status": "PASS",
        "baseline_sha256": sha(seed),
        "ordered_source_payloads": count,
        "seed_raw_sources": len(baseline["protected_files_sha256"]),
        "consulted_publications_unchanged": len(consulted),
        "original_NEW": 0,
        "added_NEW": 0,
        "retired": 0,
        "frozen_ecoli_handoff_sha256": sha(previous_path),
        "frozen_ecoli_files_verified": len(files),
        "explicit_ecoli_core_followup": sha(followup_dir / "handoff.json"),
        "reviews": summaries,
    }
    (HERE / "preservation.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
