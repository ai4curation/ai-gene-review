"""Verify additive preservation and exact supersession of PR6196 gene edits."""

import argparse
import hashlib
import json
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[4]
A = Path(__file__).resolve().parent


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def payload(rows):
    return [{k: v for k, v in r.items() if k != "review"} for r in rows]


def lifecycle(rows):
    return [
        (i, r.get("retired", False), r["review"]["action"] == "NEW")
        for i, r in enumerate(rows)
    ]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--write",
        action="store_true",
        help="Create the initial receipt; omit for frozen read-only verification",
    )
    args = parser.parse_args()
    base = json.loads((A / "baseline.json").read_text())
    changed = json.loads((A / "changed-genes.json").read_text())
    allowed = set()
    for item in changed:
        path = Path(item["review"])
        allowed.update(
            {
                str(path),
                str(path.with_suffix(".html")),
                str(path.parent / f"{item['gene']}-notes.md"),
            }
        )
    updates = {}
    unchanged = {}
    for name, expected in base["all_preexisting_files"].items():
        current = sha(ROOT / name)
        if name in allowed and current != expected:
            updates[name] = {"before_sha256": expected, "after_sha256": current}
        else:
            assert current == expected, f"Unapproved modification: {name}"
            unchanged[name] = expected
    assert len(updates) == 39, len(updates)
    row_count = 0
    proposal_count = 0
    members = []
    for name, saved in base["reviews"].items():
        old = saved["document"]
        doc = yaml.safe_load((ROOT / name).read_text())
        assert payload(old["existing_annotations"]) == payload(
            doc["existing_annotations"]
        ), name
        assert lifecycle(old["existing_annotations"]) == lifecycle(
            doc["existing_annotations"]
        ), name
        assert doc["status"] == old["status"]
        assert doc.get("core_functions") == old.get("core_functions"), name
        row_count += len(doc["existing_annotations"])
        proposal_count += sum(
            r["review"]["action"] == "NEW" for r in doc["existing_annotations"]
        )
        members.append(
            {
                "review": name,
                "rows": len(doc["existing_annotations"]),
                "ordered_payload_and_lifecycle_exact": True,
            }
        )
    assert row_count == 192 and proposal_count == 4
    mta = yaml.safe_load((ROOT / "genes/THEMA/mtaD/mtaD-ai-review.yaml").read_text())
    refined = [
        r for r in mta["existing_annotations"] if r["review"]["action"] == "MODIFY"
    ]
    assert len(refined) == 5
    assert all(
        [t["id"] for t in r["review"]["proposed_replacement_terms"]]
        == ["GO:0050270", "GO:0090614"]
        for r in refined
    )
    assert all("MARK_AS_OVER_ANNOTATED tier" in r["review"]["reason"] for r in refined)
    action_changes = json.loads((A / "action-changes.json").read_text())
    assert len(action_changes) == 19
    assert all(
        x["before"] == "KEEP_AS_NON_CORE" and x["after"] == "ACCEPT"
        for x in action_changes
    )
    validations = json.loads((A / "validation-results.json").read_text())
    render_history = json.loads((A / "render-history-results.json").read_text())
    assert len(validations) == 13 and all(x["validate"] == 0 for x in validations)
    assert len(render_history) == 26 and all(
        x.get("render", 0) == 0 and x.get("validate_history", 0) == 0
        for x in render_history
    )
    # Published manifests are immutable historical snapshots, not silently refreshed.
    prior_manifests = {
        name: h
        for name, h in unchanged.items()
        if name.startswith(str(A.parent.relative_to(ROOT)) + "/")
        and Path(name).name == "handoff.json"
    }
    superseded = []
    for name, h in prior_manifests.items():
        manifest = json.loads((ROOT / name).read_text())
        entries = {
            p: {
                "recorded_sha256": oldhash,
                "published_before_sha256": updates[p]["before_sha256"],
                "after_sha256": updates[p]["after_sha256"],
            }
            for p, oldhash in manifest.get("files", {}).items()
            if p in updates
        }
        if entries:
            superseded.append(
                {
                    "manifest": name,
                    "manifest_sha256_preserved": h,
                    "superseded_entries": entries,
                }
            )
    publication = ROOT / "publications/PMID_12705835.md"
    receipt = {
        "status": "PASS",
        "published_head": base["head"],
        "affected_genes": len(changed),
        "updated_preexisting_files": updates,
        "unchanged_preexisting_files": unchanged,
        "original_manifests_preserved": prior_manifests,
        "explicit_supersessions": superseded,
        "supersession_rule": "The recorded old manifest remains historical. Apply only these exact current published-before to after transitions; a recorded hash differing from published-before reflects an earlier documented follow-up and is not rewritten.",
        "members": members,
        "published_rows_preserved": row_count,
        "prior_original_rows": 191,
        "historical_NEW_preserved": 3,
        "prior_authored_NEW_preserved": 1,
        "added_deleted_retired_rows": 0,
        "replacement_terms_withdrawn": 10,
        "binding_action_changes": 19,
        "new_parent_fetched_source": {
            str(publication.relative_to(ROOT)): sha(publication)
        },
        "validation": "13 gene validations,13 renders,13 new histories PASS",
        "module_semantics": "No curated module, family or project edits. Core reaction IDs and capacity routes unchanged.",
    }
    target = A / "preservation-supersession.json"
    if args.write:
        target.write_text(json.dumps(receipt, indent=2) + "\n")
    else:
        assert json.loads(target.read_text()) == receipt, (
            "Frozen additive receipt differs"
        )
    print(
        json.dumps(
            {
                "result": "PASS",
                "updated_files": len(updates),
                "unchanged_files": len(unchanged),
                "preserved_manifests": len(prior_manifests),
                "superseded_manifests": len(superseded),
                "reviews_checked": len(members),
                "published_rows": row_count,
                "NEW_rows_preserved": proposal_count,
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
