"""Strict payload/source preservation and scientifically important role boundaries.
Run from repository root with uv run python <this-file>.
"""

from pathlib import Path
from collections import Counter
import json
import yaml
import hashlib

AUDIT = Path(__file__).parent
b = json.loads(
    Path(
        "analysis/module_audits/bacterial_groel_groes_chaperonin_folding/new-cage-member-baseline.json"
    ).read_text()
)


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


counts = Counter()
rows = 0
raw = 0
reviews = {}
for m in b["members"]:
    p = m["review_path"]
    d = yaml.safe_load(Path(p).read_text())
    reviews[(m["organism"], m["gene"])] = d
    assert d["id"] == m["accession"] and d["taxon"] == m["taxon"], p
    assert [
        {k: v for k, v in a.items() if k != "review"} for a in d["existing_annotations"]
    ] == m["payloads"], p
    for a in d["existing_annotations"]:
        r = a["review"]
        assert r["action"] not in ["PENDING", "NEW"]
        assert r.get("supported_by")
        counts[r["action"]] += 1
    rows += len(d["existing_annotations"])
    for p, h in m["raw_sha256"].items():
        assert sha(p) == h, p
        raw += 1
assert (
    rows == 64 and raw == 8
)  # Actual frozen baseline: 13+7+28+16, correcting task count 65.
for key in [("BACSU", "groES"), ("MYCTU", "groES")]:
    d = reviews[key]
    c = d["core_functions"][0]
    assert c["molecular_function"]["id"] == "GO:0051087"
    assert c["contributes_to_molecular_function"]["id"] == "GO:0140662"
    assert (
        next(
            a["review"]["action"]
            for a in d["existing_annotations"]
            if a["term"]["id"] == "GO:0005524"
        )
        == "UNDECIDED"
    )
    assert (
        next(
            a["review"]["action"]
            for a in d["existing_annotations"]
            if a["term"]["id"] == "GO:0044183"
        )
        == "ACCEPT"
    )
    assert all(
        "ATPase" not in c["molecular_function"]["label"] for c in d["core_functions"]
    )
mt = reviews[("MYCTU", "groES")]
assert all(
    a["review"]["action"] == "ACCEPT"
    for a in mt["existing_annotations"]
    if a["term"]["id"] == "GO:0046872"
)
assert (
    next(
        a["review"]["action"]
        for a in reviews[("BACSU", "groES")]["existing_annotations"]
        if a["term"]["id"] == "GO:0046872"
    )
    == "UNDECIDED"
)
el = reviews[("MYCTU", "groEL2")]
for go in ["GO:0140662", "GO:0044183"]:
    assert (
        next(
            a["review"]["action"]
            for a in el["existing_annotations"]
            if a["term"]["id"] == go
        )
        == "ACCEPT"
    )
assert "ATP-independent" in el["core_functions"][0]["description"]
assert all(
    a["review"]["action"] == "REMOVE"
    for d in reviews.values()
    for a in d["existing_annotations"]
    if a["term"]["id"] == "GO:0005515"
)
assert all(not d.get("proposed_new_terms") for d in reviews.values())
for d in reviews.values():
    for r in d["references"]:
        if r["id"] in ["PMID:12082092", "PMID:12837792"]:
            assert not r.get("full_text_unavailable")
for p, h in json.loads((AUDIT / "source-sha256.json").read_text()).items():
    assert sha(p) == h, p
print(
    json.dumps(
        {
            "original_rows_preserved": rows,
            "order_preserved": True,
            "original_raw_files_unchanged": raw,
            "protected_sources_unchanged": len(
                json.loads((AUDIT / "source-sha256.json").read_text())
            ),
            "actions": dict(counts),
            "historical_NEW": 0,
            "active_NEW": 0,
            "role_and_evidence_boundary_checks": "passed",
            "review_sha256": {
                m["review_path"]: sha(m["review_path"]) for m in b["members"]
            },
        },
        indent=2,
    )
)
