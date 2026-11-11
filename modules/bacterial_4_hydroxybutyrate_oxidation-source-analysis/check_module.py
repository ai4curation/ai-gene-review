import dataclasses
import json
import re
from pathlib import Path

import yaml

from ai_gene_review.module_logic import compile_module, is_satisfied
from ai_gene_review.validation.module_validator import validate_module_file

r = Path(".")
o = r / ".cache/module-audit-logs"
panel = json.loads((Path(__file__).parent / "member-grounding.json").read_text())[
    "members"
]
o.mkdir(parents=True, exist_ok=True)
members = {}
genes = {}
for x in panel:
    p = Path(x["review_path"])
    text = (p.parent / (x["gene"] + "-uniprot.txt")).read_text()
    families = re.findall(r"^DR   PANTHER; (PTHR\d+:SF\d+);", text, re.M)
    assert len(families) == 1
    members[x["accession"]] = families[0]
    genes[x["accession"]] = p
res = validate_module_file(
    Path("modules/bacterial_4_hydroxybutyrate_oxidation.yaml"),
    member_index=members,
    gene_index=genes,
)
d = dataclasses.asdict(res) if dataclasses.is_dataclass(res) else vars(res)
(o / "hydroxybutyrate-module-validation.json").write_text(
    json.dumps(d, indent=2, default=str) + "\n"
)
print(json.dumps(d, indent=2, default=str))
doc = yaml.safe_load(
    Path("modules/bacterial_4_hydroxybutyrate_oxidation.yaml").read_text()
)
c = compile_module(doc)
tests = []
# All 64 member subsets exercise the required native pair versus every optional/mixed combination.
for mask in range(64):
    present = {p["accession"] for i, p in enumerate(panel) if mask & (1 << i)}
    actual = is_satisfied(
        c,
        lambda a: a.uniprot in present
        or (a.uniprot or "").removeprefix("UniProtKB:") in present,
    )
    expected = {"Q59104", "Q9RBF6"} <= present
    tests.append(
        {
            "present": sorted(present),
            "expected": expected,
            "actual": actual,
            "pass": actual == expected,
        }
    )
(o / "hydroxybutyrate-route-cases.json").write_text(
    json.dumps(
        {
            "predicate_semantics": "Exact activity-capable members in the described selected/expressing context; not a prediction of wild-type growth from genomic presence.",
            "cases": tests,
            "passed": sum(x["pass"] for x in tests),
            "total": len(tests),
        },
        indent=2,
    )
    + "\n"
)
assert all(x["pass"] for x in tests)
print("All 64 exhaustive member-subset cases passed")
raise SystemExit(bool(d.get("errors")))
