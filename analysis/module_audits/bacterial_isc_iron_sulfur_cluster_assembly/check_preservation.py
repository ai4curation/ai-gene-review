"""Verify original Isc rows, explicit retirement and immutable source inputs."""

import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path

import yaml


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read(path):
    return yaml.safe_load(path.read_text())


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    baseline = read(HERE / "baseline.json")
    azo = read(HERE / "azotobacter-consultation/seed-baseline.yaml")
    members = dict(baseline["members"])
    for gene, original in azo["genes"].items():
        path = f"genes/AZOVI/{gene}/{gene}-ai-review.yaml"
        members[path] = {
            "id": original["id"],
            "ordered_annotation_payloads": original["annotations"],
            "historical_new_indices": [],
        }
    sources = dict(baseline["sources_sha256"])
    sources.update(azo["protected"])
    sources.update(read(HERE / "psepk-consultation/baseline.json")["sources"])
    sources.update(
        read(HERE / "ecoli-consultation/preservation-baseline.json")[
            "protected_sha256"
        ]
    )
    sources.update(
        read(HERE / "family-consultation/receipt.json")["protected_sources_sha256"]
    )
    for path, expected in sources.items():
        assert sha(ROOT / path) == expected, path
    results = []
    actions = Counter()
    retirement = []
    for path, original in members.items():
        current = read(ROOT / path)
        assert current["id"] == original["id"], path
        assert current["status"] == "COMPLETE", path
        rows = current["existing_annotations"]
        expected = original["ordered_annotation_payloads"]
        assert len(rows) == len(expected), path
        for i, (row, old) in enumerate(zip(rows, expected, strict=True)):
            payload = {k: v for k, v in row.items() if k != "review"}
            if path == "genes/PSEPK/hscA/hscA-ai-review.yaml" and i == 4:
                assert old["term"]["id"] == "GO:0140662"
                assert payload.pop("retired") is True
                assert row["review"]["action"] == "NEW"
                retirement.append({"path": path, "index": i, "term": "GO:0140662"})
            assert payload == old, (path, i)
            action = row["review"]["action"]
            assert action != "PENDING", (path, i)
            actions[action] += 1
        new_indices = [i for i, row in enumerate(rows) if row["review"]["action"] == "NEW"]
        assert new_indices == original["historical_new_indices"], path
        results.append(
            {
                "path": path,
                "sha256": sha(ROOT / path),
                "rows": len(rows),
                "historical_NEW": len(new_indices),
                "active_NEW": sum(not rows[i].get("retired") for i in new_indices),
            }
        )
    handoffs = {}
    for name in ["psepk", "ecoli", "azotobacter", "family"]:
        receipt = read(HERE / f"root-{name}-receipt.json")
        files = receipt["files"]
        if name == "psepk":
            durable = read(HERE / "psepk-handoff-files.json")
            assert durable["source_handoff_sha256"] == receipt["handoff_sha256"]
            files = durable["files"]
        if isinstance(files, dict):
            files = [{"path": p, "sha256": h} for p, h in files.items()]
        for entry in files:
            expected = entry["sha256"]
            normalization = receipt.get("format_normalizations", {}).get(entry["path"])
            if normalization:
                assert normalization["before_sha256"] == expected
                assert normalization["parsed_yaml_unchanged"]
                original_yaml = normalization["original_yaml"]
                assert hashlib.sha256(original_yaml.encode()).hexdigest() == expected
                assert read(ROOT / entry["path"]) == yaml.safe_load(original_yaml)
                expected = normalization["after_sha256"]
            assert sha(ROOT / entry["path"]) == expected, entry["path"]
        handoffs[name] = len(files)
    result = {
        "status": "PASS",
        "reviewed_genes": len(results),
        "original_ordered_rows": sum(r["rows"] for r in results),
        "new_rows": 0,
        "historical_NEW": sum(r["historical_NEW"] for r in results),
        "active_NEW": sum(r["active_NEW"] for r in results),
        "explicit_retirements": retirement,
        "actions": dict(actions),
        "protected_sources_sha256": sources,
        "handoff_files_verified": handoffs,
        "genes": results,
        "limits": "Preservation and completeness only; not evidence of biological correctness.",
    }
    if args.output:
        args.output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({k: v for k, v in result.items() if k not in {"genes", "protected_sources_sha256"}}))


if __name__ == "__main__":
    main()
