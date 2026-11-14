"""Verify the bounded PR6194 supersession without modifying prior receipts."""
import hashlib
import json
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def payloads(document):
    return [
        {key: value for key, value in row.items() if key != "review"}
        for row in document.get("existing_annotations", [])
    ]


def main():
    baseline = json.loads((HERE / "baseline.json").read_text())
    mutable = set(baseline["reviews"])
    changes = []
    counts = {"gene_rows": 0, "historical_new": 0, "retired": 0, "paint_assertions": 0}
    node_fields = {
        "node_id", "asserted_term", "evidence", "negated", "paint_snapshot", "seeds", "node_taxon"
    }
    permitted_nodes = {
        ("PTHR43194", "PANTHER:PTN002455972", "GO:0090499"),
        ("PTHR43194", "PANTHER:PTN002455972", "GO:0009102"),
        ("PTHR43798", "PANTHER:PTN008685307", "GO:0047372"),
        ("PTHR43798", "PANTHER:PTN008685307", "GO:0046464"),
    }
    for path, original in baseline["reviews"].items():
        before = original["document"]
        after = yaml.safe_load((ROOT / path).read_text())
        assert payloads(before) == payloads(after), path
        counts["gene_rows"] += len(payloads(before))
        for index, (old, new) in enumerate(zip(before.get("existing_annotations", []),
                                               after.get("existing_annotations", []), strict=True)):
            if old["review"]["action"] == "NEW":
                counts["historical_new"] += 1
                counts["retired"] += bool(old.get("retired"))
                assert new["review"]["action"] == "NEW", (path, index)
            if old != new:
                changes.append({"path": path, "row": index, "old": old, "new": new})
        for old, new in zip(before.get("node_assessments", []),
                            after.get("node_assessments", []), strict=True):
            counts["paint_assertions"] += 1
            assert {k: old[k] for k in node_fields if k in old} == {
                k: new[k] for k in node_fields if k in new
            }, path
            key = (before["family_id"].split(":")[-1], old["node_id"], old["asserted_term"]["id"])
            if key not in permitted_nodes:
                assert old == new, (path, key)
        if before.get("term_assessments") != after.get("term_assessments"):
            changes.append({"path": path, "kind": "term_assessments", "old": before.get("term_assessments"),
                            "new": after.get("term_assessments")})
        if path.startswith("genes/"):
            parent = Path(path).parent
            gene = parent.name
            mutable.update(str(parent / f"{gene}{suffix}") for suffix in ["-notes.md", "-ai-review.html"])
    unchanged = []
    for path, digest in baseline["protected"].items():
        if path not in mutable:
            assert sha(ROOT / path) == digest, path
            unchanged.append(path)
        elif path.endswith("-notes.md"):
            # Original bytes are recovered from published HEAD for append-only notes.
            import subprocess
            old = subprocess.check_output(["git", "show", f'{baseline["head"]}:{path}'], cwd=ROOT)
            assert (ROOT / path).read_bytes().startswith(old), path
    result = {"baseline_head": baseline["head"], "counts": counts,
              "unchanged_protected_files": unchanged, "payload_preserved": True,
              "unrelated_node_objects_preserved": True, "notes_append_only": True,
              "changes": changes}
    (HERE / "preservation.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({"counts": counts, "unchanged_protected_files": len(unchanged)}, indent=2))


if __name__ == "__main__":
    main()
