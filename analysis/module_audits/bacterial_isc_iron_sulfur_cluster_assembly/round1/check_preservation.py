"""Compare the Isc review follow-up with its published, immutable baseline."""

from collections import Counter
import hashlib
import json
from pathlib import Path

import yaml


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]


def digest(path):
    return hashlib.sha256((ROOT / path).read_bytes()).hexdigest()


def main():
    baseline = json.loads((HERE / "baseline.json").read_text())
    actions = Counter()
    changes = []
    new_count = 0
    active_new = 0
    rows = 0
    reviews = {}
    for path, old in baseline["reviews"].items():
        current = yaml.safe_load((ROOT / path).read_text())
        assert current["id"] == old["id"] and current["status"] == "COMPLETE", path
        before = old["existing_annotations"]
        after = current["existing_annotations"]
        assert len(before) == len(after), path
        for i, (a, b) in enumerate(zip(before, after, strict=True)):
            assert {k: v for k, v in a.items() if k != "review"} == {
                k: v for k, v in b.items() if k != "review"
            }, (path, i)
            aa, ba = a["review"]["action"], b["review"]["action"]
            assert ba != "PENDING", (path, i)
            assert (aa == "NEW") == (ba == "NEW"), (path, i)
            actions[ba] += 1
            rows += 1
            if ba == "NEW":
                new_count += 1
                active_new += not b.get("retired", False)
            if aa != ba:
                changes.append(
                    {
                        "path": path,
                        "index": i,
                        "term": b["term"]["id"],
                        "before": aa,
                        "after": ba,
                    }
                )
        reviews[path] = {"sha256": digest(path), "rows": len(after)}
    assert len(reviews) == 18 and rows == 208 and new_count == 3 and active_new == 2
    for path, expected in baseline["protected_files_sha256"].items():
        assert digest(path) == expected, path
    # Keep the withdrawn proposal itself, including its review prose, unchanged.
    path = "genes/PSEPK/hscA/hscA-ai-review.yaml"
    assert (
        yaml.safe_load((ROOT / path).read_text())["existing_annotations"][4]
        == baseline["reviews"][path]["existing_annotations"][4]
    )
    for path, before in baseline["families"].items():
        after = yaml.safe_load((ROOT / path).read_text())
        key = "term_assessments"
        assert len(before.get(key, [])) == len(after.get(key, [])), path
        for a, b in zip(before.get(key, []), after.get(key, []), strict=True):
            for field in [
                "node_id",
                "asserted_term",
                "evidence",
                "seeds",
                "paint_snapshot",
                "negated",
                "node_taxon",
            ]:
                assert a.get(field) == b.get(field), (path, field)
    result = {
        "status": "PASS",
        "published_head": baseline["head"],
        "review_count": len(reviews),
        "ordered_rows": rows,
        "historical_NEW": new_count,
        "active_NEW": active_new,
        "added_rows": 0,
        "deleted_rows": 0,
        "retirement_changes": 0,
        "protected_sources": len(baseline["protected_files_sha256"]),
        "actions": dict(actions),
        "action_changes": changes,
        "reviews": reviews,
        "scope": "Source payloads, order, lifecycle and PAINT provenance only; scientific validity is assessed separately.",
    }
    (HERE / "preservation-results.json").write_text(json.dumps(result, indent=2) + "\n")
    print(
        json.dumps(
            {k: v for k, v in result.items() if k not in ["reviews", "action_changes"]}
        )
    )


if __name__ == "__main__":
    main()
