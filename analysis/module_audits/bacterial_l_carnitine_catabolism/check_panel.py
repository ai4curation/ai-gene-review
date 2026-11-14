"""Check the complete carnitine panel against independently captured original/seed rows."""

from collections import Counter
import copy
import hashlib
import json
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[3]
AUDIT = Path(__file__).resolve().parent
EXCEPTIONS = {
    ("genes/RHIME/bcoG/bcoG-ai-review.yaml", 3): "GO:0042413",
    ("genes/PSEAE/cdhB/cdhB-ai-review.yaml", 3): "GO:0016289",
    ("genes/PSEAE/cdhC/cdhC-ai-review.yaml", 3): "GO:0016747",
}


def main():
    baseline = json.loads((AUDIT / "baseline.json").read_text())
    seeded = json.loads(
        (AUDIT / "pseae-consultation/new-seed-baseline.json").read_text()
    )
    originals = {p: row["document"] for p, row in baseline["reviews"].items()}
    assert not originals.keys() & seeded["reviews"].keys()
    documents = {**originals, **seeded["reviews"]}
    protected = dict(baseline["protected_files_sha256"])
    for p, expected in seeded["protected"].items():
        assert p not in protected or protected[p] == expected
        protected[p] = expected
    for p, expected in protected.items():
        assert hashlib.sha256((ROOT / p).read_bytes()).hexdigest() == expected, p
    report = {"reviews": {}, "retirement_exceptions": [], "action_changes": []}
    historical_new = active_new = original_rows = seeded_rows = 0
    all_actions = Counter()
    for p, original in documents.items():
        current = yaml.safe_load((ROOT / p).read_text())
        assert (
            current["id"] == original["id"] and current["taxon"] == original["taxon"]
        ), p
        assert current["status"] == "COMPLETE", p
        before = original.get("existing_annotations", [])
        after = current.get("existing_annotations", [])
        assert len(before) == len(after), p
        original_rows += len(before) if p in originals else 0
        seeded_rows += len(before) if p in seeded["reviews"] else 0
        actions = Counter()
        for i, (old, new) in enumerate(zip(before, after, strict=True)):
            old_payload = {k: v for k, v in old.items() if k != "review"}
            new_payload = copy.deepcopy({k: v for k, v in new.items() if k != "review"})
            if (p, i) in EXCEPTIONS:
                assert old["term"]["id"] == EXCEPTIONS[(p, i)]
                assert old["review"]["action"] == new["review"]["action"] == "NEW"
                assert (
                    "retired" not in old_payload and new_payload.pop("retired") is True
                )
                report["retirement_exceptions"].append(
                    {"path": p, "index": i, "term": old["term"]["id"]}
                )
            assert new_payload == old_payload, (p, i, "source payload differs")
            action = new["review"]["action"]
            assert action != "PENDING" and new["review"].get("reason"), (p, i)
            actions[action] += 1
            if old["review"]["action"] == "NEW":
                historical_new += 1
                assert action == "NEW", (p, i, "historical action lost")
            elif action == "NEW":
                raise AssertionError((p, i, "new proposal manufactured"))
            active_new += action == "NEW" and not new.get("retired", False)
            if old["review"]["action"] != action:
                report["action_changes"].append(
                    {
                        "path": p,
                        "index": i,
                        "term": old["term"]["id"],
                        "before": old["review"]["action"],
                        "after": action,
                        "newly_seeded": p in seeded["reviews"],
                    }
                )
        all_actions.update(actions)
        report["reviews"][p] = {
            "rows": len(after),
            "actions": dict(actions),
            "sha256": hashlib.sha256((ROOT / p).read_bytes()).hexdigest(),
        }
    assert len(documents) == 14 and original_rows == 94 and seeded_rows == 52
    assert (
        historical_new == 11
        and active_new == 8
        and len(report["retirement_exceptions"]) == 3
    )
    report.update(
        original_reviews=len(originals),
        new_seed_reviews=len(seeded["reviews"]),
        original_rows=original_rows,
        seeded_rows=seeded_rows,
        total_rows=original_rows + seeded_rows,
        historical_NEW=historical_new,
        active_NEW=active_new,
        added_proposals=0,
        protected_source_files=len(protected),
        actions=dict(all_actions),
        scope="Ordered source-payload and proposal-lifecycle preservation, not validation of scientific truth. UNDECIDED remains explicitly unresolved.",
    )
    (AUDIT / "panel-preservation.json").write_text(json.dumps(report, indent=2) + "\n")
    print(
        json.dumps(
            {
                k: v
                for k, v in report.items()
                if k not in ["reviews", "action_changes", "retirement_exceptions"]
            }
        )
    )


if __name__ == "__main__":
    main()
