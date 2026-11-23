"""Check only the two approved PTHR35369 prose changes and scoped support."""

import copy
import hashlib
import json
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[4]
OUT = Path(__file__).resolve().parent
PATH = ROOT / "interpro/panther/PTHR35369/PTHR35369-review.yaml"
BASE = json.loads((OUT / "baseline.json").read_text())
after = yaml.safe_load(PATH.read_text())
before = BASE["review"]
expected = copy.deepcopy(before)
expected["notes"] = after["notes"]
assert "any homologous one" not in after["notes"]
assert "do not exclude homology" in after["notes"]
index = next(
    i
    for i, a in enumerate(before["term_assessments"])
    if a["assessed_term"]["id"] == "GO:0042276"
)
new = after["term_assessments"][index]
old = before["term_assessments"][index]
expected["term_assessments"][index]["scope_reason"] = new["scope_reason"]
assert (
    "stationary-phase" in new["scope_reason"]
    and "MMS mutagenesis" in new["scope_reason"]
)
added = new["supported_by"][len(old["supported_by"]) :]
assert [a["reference_id"] for a in added] == ["PMID:17331811", "PMID:28118378"]
for a in added:
    pub = ROOT / ("publications/PMID_" + a["reference_id"].split(":")[1] + ".md")
    assert a["supporting_text"] in pub.read_text()
expected["term_assessments"][index]["supported_by"] += added
assert [r["id"] for r in after["references"][:2]] == ["PMID:17331811", "PMID:28118378"]
expected["references"] = after["references"][:2] + before["references"]
assert after == expected, "Unexpected change outside approved prose/support"
for name, sha in BASE["sources"].items():
    assert hashlib.sha256((ROOT / name).read_bytes()).hexdigest() == sha, name
receipt = {
    "status": "PASS",
    "scope_enums_applicable_subfamilies_members_and_PAINT": "exactly unchanged",
    "new_quotes": "exact cached substrings",
    "protected_sources": BASE["sources"],
    "review_sha256": hashlib.sha256(PATH.read_bytes()).hexdigest(),
}
(OUT / "receipt.json").write_text(json.dumps(receipt, indent=2) + "\n")
print("PASS: only authorized prose/support changes; protected sources unchanged")
