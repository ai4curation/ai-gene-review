"""Reproduce the ECOLI ManXYZ ordered-payload and construct preservation audit."""

import hashlib
import json
import re
from collections import Counter
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
BASELINE = HERE.parent / "baseline.json"


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    baseline = json.loads(BASELINE.read_text())
    extra = json.loads((HERE / "additional-protected.json").read_text())
    assert extra["baseline_head"] == baseline["head"]
    for path, digest in extra["files"].items():
        assert sha(ROOT / path) == digest, path
    rows = historical_new = 0
    results = []
    for path, frozen in baseline["reviews"].items():
        old = frozen["document"]
        current = yaml.safe_load((ROOT / path).read_text())
        assert current["status"] == "COMPLETE"
        before, after = old["existing_annotations"], current["existing_annotations"]
        assert len(before) == len(after)
        changed = []
        for index, (a, b) in enumerate(zip(before, after, strict=True)):
            assert {k: v for k, v in a.items() if k != "review"} == {
                k: v for k, v in b.items() if k != "review"
            }, (path, index)
            assert (a["review"]["action"] == "NEW") == (b["review"]["action"] == "NEW")
            assert a.get("retired", False) == b.get("retired", False)
            historical_new += a["review"]["action"] == "NEW"
            if a["review"]["action"] != b["review"]["action"]:
                changed.append(
                    {
                        "index": index,
                        "term": a["term"]["id"],
                        "before": a["review"]["action"],
                        "after": b["review"]["action"],
                    }
                )
        rows += len(before)
        results.append(
            {
                "path": path,
                "before_sha256": frozen["sha256"],
                "after_sha256": sha(ROOT / path),
                "rows": len(after),
                "action_counts": dict(Counter(a["review"]["action"] for a in after)),
                "changed_actions": changed,
            }
        )
    for path, digest in baseline["protected_files_sha256"].items():
        assert sha(ROOT / path) == digest, path
    identities = json.loads((HERE / "identity/results.json").read_text())
    for row in identities:
        record = ROOT / f"genes/ECOLI/{row['gene']}/{row['gene']}-uniprot.txt"
        sequence = "".join(
            re.findall(
                "[A-Z]+",
                record.read_text().split("\nSQ   ")[1].split("\n", 1)[1].split("//")[0],
            )
        )
        entity_path = HERE / f"identity/6K1H-{row['entity']}.json"
        assert sha(entity_path) == row["sha256"]
        entity = json.loads(entity_path.read_text())
        expected = sequence + ("HHHHHHHH" if row["gene"] == "manY" else "")
        assert entity["entity_poly"]["pdbx_seq_one_letter_code_can"] == expected
        assert entity["rcsb_polymer_entity_container_identifiers"]["uniprot_ids"] == [
            row["accession"]
        ]
    assert rows == 63 and historical_new == 2
    result = {
        "status": "PASS",
        "baseline_sha256": sha(BASELINE),
        "ordered_rows": rows,
        "historical_NEW": historical_new,
        "added_NEW": 0,
        "retired_rows": 0,
        "protected_sources": len(baseline["protected_files_sha256"]),
        "additional_provider_prediction_files": len(extra["files"]),
        "reviews": results,
        "exact_construct_comparisons": identities,
        "source_caches_refreshed": [],
        "full_corpus_run": False,
    }
    (HERE / "preservation.json").write_text(json.dumps(result, indent=2) + "\n")
    print(
        json.dumps(
            {
                k: v
                for k, v in result.items()
                if k not in {"reviews", "exact_construct_comparisons"}
            }
        )
    )


if __name__ == "__main__":
    main()
