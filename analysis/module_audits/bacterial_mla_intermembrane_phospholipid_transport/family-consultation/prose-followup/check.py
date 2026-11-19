"""Strict prose-only supersession: exact allowed fields and immutable prior release."""

import hashlib
import json
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def differences(a, b, p=()):
    if type(a) is not type(b):
        return [p]
    if isinstance(a, dict):
        if a.keys() != b.keys():
            return [p]
        return [d for k in a for d in differences(a[k], b[k], p + (k,))]
    if isinstance(a, list):
        if len(a) != len(b):
            return [p]
        return [
            d
            for i, (x, y) in enumerate(zip(a, b, strict=True))
            for d in differences(x, y, p + (i,))
        ]
    return [] if a == b else [p]


def main():
    previous = json.loads((HERE / "prior-release.json").read_text())
    assert sha(ROOT / previous["path"]) == previous["sha256"]
    release = json.loads((ROOT / previous["path"]).read_text())
    changes = json.loads((HERE / "changes.json").read_text())
    changed = {x["path"]: x for x in changes}
    for path, h in release["files"].items():
        assert sha(ROOT / path) == (
            changed[path]["after_sha256"] if path in changed else h
        ), path
    rows = []
    for row in changes:
        path = ROOT / row["path"]
        assert row["before_sha256"] == release["files"][row["path"]]
        after = yaml.safe_load(path.read_text())
        assert after == row["after"]
        before = row["before"]
        family = before["family_id"].split(":")[-1]
        go = "GO:0043190" if family == "PTHR43023" else "GO:0006869"
        i = next(
            i
            for i, t in enumerate(before["term_assessments"])
            if t["assessed_term"]["id"] == go
        )
        allowed = {("term_assessments", i, "scope_reason")}
        if family == "PTHR43023":
            i = next(
                i
                for i, s in enumerate(before["subfamilies"])
                if s["subfamily_id"].endswith(":SF6")
            )
            allowed.add(("subfamilies", i, "description"))
        else:
            allowed.add(("coherence_reason",))
            for i, s in enumerate(before["subfamilies"]):
                if (family == "PTHR30188" and s["subfamily_id"].endswith(":SF13")) or (
                    family == "PTHR33371" and not s["subfamily_id"].endswith(":SF4")
                ):
                    allowed.add(("subfamilies", i, "divergence_description"))
        actual = set(differences(before, after))
        assert actual == allowed, (family, actual, allowed)
        assert before["node_assessments"] == after["node_assessments"]
        rows.append(
            {
                "path": row["path"],
                "before_sha256": row["before_sha256"],
                "after_sha256": row["after_sha256"],
                "exact_changed_fields": [list(x) for x in sorted(actual, key=str)],
            }
        )
    receipt = {
        "status": "PASS",
        "supersedes": previous,
        "prior_files_unchanged_except_exact_three_reviews": True,
        "changes": rows,
        "PAINT_objects_enums_scope_values_references_quotes_members_unchanged": True,
        "limitation": "The original preservation checker describes the initial frozen stage; this additive checker proves the only later differences. Do not rerun a curation script over the frozen latest release.",
    }
    (HERE / "receipt.json").write_text(json.dumps(receipt, indent=2) + "\n")
    print(
        "PASS",
        len(rows),
        "reviews",
        sum(len(r["exact_changed_fields"]) for r in rows),
        "prose fields",
    )


if __name__ == "__main__":
    main()
