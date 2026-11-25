"""Verify exact seed preservation and the scientifically important inference boundaries.
Run from repository root: uv run python <this-file>
"""

from pathlib import Path
from collections import Counter
import hashlib
import json
import yaml

ROOT = Path(".")
AUDIT = Path(__file__).parent
baseline = yaml.safe_load(
    Path(
        "analysis/module_audits/bacterial_glycerol_uptake_catabolism/bacillus-seed-baseline.yaml"
    ).read_text()
)


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


counts = Counter()
reviews = {}
source_count = 0
for path, seed in baseline["reviews"].items():
    d = yaml.safe_load(Path(path).read_text())
    reviews[d["gene_symbol"]] = d
    assert d["id"] == seed["id"], path
    rows = d["existing_annotations"]
    assert [{k: v for k, v in a.items() if k != "review"} for a in rows] == seed[
        "source_payloads"
    ], path
    for a in rows:
        assert a["review"]["action"] not in ["PENDING", "NEW"], (path, a)
        assert a["review"].get("supported_by"), (path, a)
        counts[a["review"]["action"]] += 1
    source_count += len(rows)
for path, h in baseline["protected_sha256"].items():
    assert sha(path) == h, path
assert source_count == 27 and len(baseline["protected_sha256"]) == 6
assert all(not d.get("proposed_new_terms") for d in reviews.values())
# Prevent a family-name driven architecture claim or unsupported membrane refinement.
glpD = reviews["glpD"]
mem = [a for a in glpD["existing_annotations"] if a["term"]["id"] == "GO:0016020"]
assert len(mem) == 1 and mem[0]["review"]["action"] == "UNDECIDED"
assert glpD["core_functions"][0]["molecular_function"]["id"] == "GO:0004368"
assert "in_complex" not in glpD["core_functions"][0]
assert [x["id"] for x in glpD["core_functions"][0]["locations"]] == ["GO:0005737"]
assert (
    "tetrazolium" in mem[0]["review"]["reason"]
    or "17,000" in Path("genes/BACSU/glpD/glpD-notes.md").read_text()
)
assert "PAINT synthesis" in glpD["core_functions"][0]["description"]
# Glycerol kinase forms G3P; it must not be made a G3P-catabolic catalyst.
glpK = reviews["glpK"]
assert (
    next(a for a in glpK["existing_annotations"] if a["term"]["id"] == "GO:0006072")[
        "review"
    ]["action"]
    == "ACCEPT"
)
assert all(
    x["id"] != "GO:0046168"
    for c in glpK["core_functions"]
    for x in c.get("directly_involved_in", [])
)
assert (
    next(a for a in glpK["existing_annotations"] if a["term"]["id"] == "GO:0005524")[
        "review"
    ]["action"]
    == "ACCEPT"
)
# Confirm no inaccurate access flag for externally read full primary papers.
assert not next(
    r for r in reviews["glpF"]["references"] if r["id"] == "PMID:8436953"
).get("full_text_unavailable")
assert not next(r for r in glpD["references"] if r["id"] == "PMID:4368746").get(
    "full_text_unavailable"
)
# Exact source hash snapshot includes the fetched literature; no cache rewrites.
source_hashes = json.loads((AUDIT / "source-sha256.json").read_text())
for path, h in source_hashes.items():
    assert sha(path) == h, path
result = {
    "original_payload_rows_preserved": source_count,
    "original_row_order_preserved": True,
    "original_raw_files_unchanged": 6,
    "all_protected_sources_unchanged": len(source_hashes),
    "actions": dict(counts),
    "historical_NEW": 0,
    "active_NEW": 0,
    "scientific_boundary_checks": "passed",
    "review_sha256": {p: sha(p) for p in baseline["reviews"]},
}
print(json.dumps(result, indent=2))
