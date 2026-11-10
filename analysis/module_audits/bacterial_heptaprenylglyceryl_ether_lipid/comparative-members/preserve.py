"""Check comparative-member source bytes and ordered seed payload preservation."""

from pathlib import Path
from collections import Counter
import json
import hashlib
import yaml

ROOT = Path(__file__).resolve().parents[4]
HERE = Path(__file__).resolve().parent


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def main():
    baseline = HERE / "baseline.json"
    b = json.loads(baseline.read_text())
    receipt = {
        "baseline_sha256": sha(baseline),
        "reviews": {},
        "sources": {},
        "ledger": [],
    }
    counts = Counter()
    for key, seed in b["seeds"].items():
        org, g = key.split("/")
        p = ROOT / "genes" / org / g / f"{g}-ai-review.yaml"
        d = yaml.safe_load(p.read_text())
        rows = d["existing_annotations"]
        assert d["id"] == seed["accession"] and d["status"] == "COMPLETE", key
        payloads = [{k: v for k, v in r.items() if k != "review"} for r in rows]
        assert payloads == seed["ordered_payloads"], key
        for path, expected in seed["sources"].items():
            assert sha(ROOT / path) == expected, path
        receipt["reviews"][key] = {
            "sha256": sha(p),
            "rows": len(rows),
            "status": d["status"],
            "ordered_payloads_preserved": True,
        }
        for i, r in enumerate(rows):
            a = r["review"]["action"]
            assert a != "PENDING"
            counts[a] += 1
            receipt["ledger"].append(
                {
                    "gene": key,
                    "index": i,
                    "term": r["term"]["id"],
                    "before": "PENDING",
                    "after": a,
                    "reason": r["review"]["reason"],
                }
            )
    for path, expected in b["protected"].items():
        if path.endswith("-ai-review.yaml"):
            continue
        assert sha(ROOT / path) == expected, path
        receipt["sources"][path] = expected
    assert sum(counts.values()) == 24 and counts["NEW"] == 0
    receipt.update(
        status="PASS",
        rows=24,
        actions=dict(counts),
        source_files_preserved=len(receipt["sources"]),
        rows_added=0,
        rows_deleted=0,
        retirements=0,
    )
    (HERE / "preservation.json").write_text(json.dumps(receipt, indent=2) + "\n")
    print(
        {k: v for k, v in receipt.items() if k not in ["reviews", "sources", "ledger"]}
    )


if __name__ == "__main__":
    main()
