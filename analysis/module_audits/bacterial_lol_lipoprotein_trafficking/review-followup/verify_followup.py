"""Read-only verification of the additive PR6188 curation release."""

import argparse
import hashlib
import json
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[4]
A = Path(__file__).resolve().parent


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--write", action="store_true", help="Create initial receipt before freeze"
    )
    args = parser.parse_args()
    baseline = json.loads((A / "baseline.json").read_text())
    changed = json.loads((A / "changed-genes.json").read_text())
    copies = json.loads((A / "historical-source-copy-receipt.json").read_text())
    allowed = set()
    for item in changed:
        path = Path(item["path"])
        allowed.update(
            [
                str(path),
                str(path.with_suffix(".html")),
                str(path.parent / (path.parts[-2] + "-notes.md")),
            ]
        )
    updates, dependencies, parent_owned = {}, {}, {}
    slug = "bacterial_lol_lipoprotein_trafficking"
    parent_paths = {
        f"modules/{slug}{suffix}" for suffix in [".yaml", ".html", "-notes.md"]
    }
    for name, expected in baseline["files"].items():
        if name in parent_paths:
            parent_owned[name] = expected
            continue
        if name in copies:
            target = copies[name]["durable_path"]
            assert sha(ROOT / target) == expected
            if (ROOT / name).exists():
                assert sha(ROOT / name) == expected
            dependencies[target] = expected
            continue
        current = sha(ROOT / name)
        if name in allowed and current != expected:
            updates[name] = {"before_sha256": expected, "after_sha256": current}
        else:
            assert current == expected, f"Unapproved change: {name}"
            dependencies[name] = expected
    assert len(updates) == 30
    row_count = proposal_count = 0
    action_changes = []
    for name, old in baseline["reviews"].items():
        current = yaml.safe_load((ROOT / name).read_text())
        before, after = old["existing_annotations"], current["existing_annotations"]
        assert len(before) == len(after)
        for i, (x, y) in enumerate(zip(before, after, strict=True)):
            assert {k: v for k, v in x.items() if k != "review"} == {
                k: v for k, v in y.items() if k != "review"
            }, (name, i)
            assert (x["review"]["action"] == "NEW") == (y["review"]["action"] == "NEW")
            if x["review"]["action"] != y["review"]["action"]:
                action_changes.append(
                    {
                        "path": name,
                        "index": i,
                        "term": x["term"]["id"],
                        "before": x["review"]["action"],
                        "after": y["review"]["action"],
                    }
                )
        assert current["status"] == old["status"]
        row_count += len(after)
        proposal_count += sum(x["review"]["action"] == "NEW" for x in after)
    assert row_count == 148 and proposal_count == 14
    assert len(action_changes) == 2
    assert all(
        x["term"] == "GO:0009279" and x["before"] == "ACCEPT" and x["after"] == "MODIFY"
        for x in action_changes
    )
    proposals = []
    for name in baseline["reviews"]:
        d = yaml.safe_load((ROOT / name).read_text())
        for p in d.get("proposed_new_terms", []):
            if p["proposed_name"] == "outer-membrane lipoprotein insertion activity":
                proposals.append((name, p["proposed_definition"], p["proposed_parent"]))
    assert len(proposals) == 5
    assert all(x[1:] == proposals[0][1:] for x in proposals)
    check = yaml.safe_load(
        (ROOT / "genes/FLAJ1/Fjoh_2111/Fjoh_2111-ai-review.yaml").read_text()
    )
    row = check["existing_annotations"][0]
    assert row["qualifier"] == "acts_upstream_of_or_within_positive_effect"
    assert row["review"]["action"] == "ACCEPT"
    assert row["review"]["source_defects"][0]["confidence"] == "SUSPECTED"
    assert row["review"]["source_defects"][0]["requested_change"] == "CHECK"
    validations = json.loads((A / "validation-results.json").read_text())
    renders = json.loads((A / "render-history-results.json").read_text())
    assert len(validations) == 10 and len(renders) == 20
    assert all(x["exit_code"] == 0 for x in validations + renders)
    supersessions = []
    for name, expected in baseline["manifests"].items():
        assert sha(ROOT / name) == expected
        d = json.loads((ROOT / name).read_text())
        entries = {}
        for field in [
            "files",
            "files_sha256",
            "input_closure",
            "input_sha256",
            "source_dependencies",
        ]:
            if not isinstance(d.get(field), dict):
                continue
            for n, oldhash in d[field].items():
                if n in updates:
                    entries[f"{field}/{n}"] = {
                        "path": n,
                        "recorded_sha256": oldhash,
                        **updates[n],
                    }
        if entries:
            supersessions.append(
                {
                    "manifest": name,
                    "manifest_sha256_preserved": expected,
                    "superseded_entries": entries,
                }
            )
    receipt = {
        "status": "PASS",
        "head": baseline["head"],
        "updated_files": updates,
        "source_dependencies": dependencies,
        "parent_owned_observed_not_frozen": parent_owned,
        "original_manifests_preserved": baseline["manifests"],
        "explicit_supersessions": supersessions,
        "original_rows_preserved": row_count,
        "existing_NEW_preserved": proposal_count,
        "added_deleted_retired_rows": 0,
        "action_changes": action_changes,
        "proposed_definition_consistency": {
            "count": len(proposals),
            "definition": proposals[0][1],
            "parent": proposals[0][2],
        },
        "validation": "10 gene validations, 10 renders and 10 new history validations PASS",
        "dependency_hold": "PR6186 remains a merge dependency; local validation does not lift that hold.",
    }
    target = A / "preservation-supersession.json"
    if args.write:
        target.write_text(json.dumps(receipt, indent=2) + "\n")
    else:
        assert json.loads(target.read_text()) == receipt, "Frozen receipt differs"
    print(
        json.dumps(
            {
                "status": "PASS",
                "rows": row_count,
                "NEW": proposal_count,
                "updates": len(updates),
                "source_dependencies": len(dependencies),
                "manifests_preserved": len(baseline["manifests"]),
                "superseded_manifests": len(supersessions),
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
