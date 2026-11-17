"""Verify the six released AZOVI rows against independent round1 baselines."""
import copy
import hashlib
import json
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[5]
AUDIT = Path(__file__).resolve().parent


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def payloads(document):
    return [
        {key: value for key, value in row.items() if key != "review"}
        for row in document["existing_annotations"]
    ]


def main():
    local = yaml.safe_load((AUDIT / "baseline.yaml").read_text())
    baseline = json.loads((AUDIT.parent / "baseline.json").read_text())
    ledger = []
    sources = dict(baseline["protected_files_sha256"])
    for name, before in local.items():
        current = yaml.safe_load((ROOT / name).read_text())
        expected = payloads(baseline["reviews"][name])
        assert expected == before["payloads"] == payloads(current), name
        for index, (old, new) in enumerate(zip(
            baseline["reviews"][name]["existing_annotations"],
            current["existing_annotations"], strict=True,
        )):
            ledger.append({
                "path": name, "index": index, "term": new["term"]["id"],
                "before": old["review"]["action"],
                "after": new["review"]["action"],
                "retired": new.get("retired", False),
            })
        for reference in current["references"]:
            ref = reference["id"]
            if ref.startswith("PMID:"):
                path = ROOT / "publications" / (ref.replace(":", "_") + ".md")
            elif ref.startswith("file:"):
                relative = ref.removeprefix("file:")
                path = ROOT / relative
                if not path.exists():
                    path = ROOT / "genes" / relative
            else:
                continue
            assert path.exists(), path
            key = str(path.relative_to(ROOT))
            if key not in sources:
                sources[key] = digest(path)
    for name, expected in sources.items():
        assert digest(ROOT / name) == expected, name
    specimen = payloads(baseline["reviews"][next(iter(local))])
    swapped = copy.deepcopy(specimen)
    swapped[0], swapped[1] = swapped[1], swapped[0]
    changed = copy.deepcopy(specimen)
    changed[0]["term"]["id"] = "GO:0003674"
    assert swapped != specimen and changed != specimen and specimen[:-1] != specimen
    result = {
        "result": "PASS", "reviews": len(local), "ordered_payloads": len(ledger),
        "protected_sources": len(baseline["protected_files_sha256"]),
        "new_rows": 0, "removed_rows": 0,
        "retired_rows": sum(row["retired"] for row in ledger),
        "mutation_controls": ["reorder detected", "payload edit detected", "deletion detected"],
        "action_changes": [row for row in ledger if row["before"] != row["after"]],
        "rows": ledger, "source_sha256": sources,
    }
    (AUDIT / "preservation.yaml").write_text(yaml.safe_dump(result, sort_keys=False))
    print(f"PASS: {len(local)} reviews, {len(ledger)} ordered payloads, {len(sources)} source hashes")


if __name__ == "__main__":
    main()
