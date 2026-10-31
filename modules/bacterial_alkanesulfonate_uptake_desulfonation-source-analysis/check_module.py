"""Bounded production checks with independently fetched UniProt classifications.

No release-wide index is downloaded. Mapping is read from raw records, never from
this module's declarations. Run from repository root with the installed environment.
"""

from pathlib import Path
import json
import re
import yaml
from ai_gene_review.validation.module_validator import validate_module_file

ROOT = Path(__file__).resolve().parents[2]
SLUG = "bacterial_alkanesulfonate_uptake_desulfonation"
index = {}
genes = {}
for org in ("ECOLI", "PSEPK", "PSEPU"):
    for gene in ("ssuA", "ssuB", "ssuC", "ssuD", "ssuE"):
        p = ROOT / f"genes/{org}/{gene}/{gene}-ai-review.yaml"
        d = yaml.safe_load(p.read_text())
        acc = d["id"]
        genes[acc] = p
        raw = p.with_name(gene + "-uniprot.txt").read_text()
        ids = re.findall(r"^DR   PANTHER; (PTHR\d+(?::SF\d+)?);", raw, re.M)
        assert ids, (p, "No independent classification")
        index[acc] = next((x for x in ids if ":SF" in x), ids[0])
result = validate_module_file(
    ROOT / "modules" / f"{SLUG}.yaml", member_index=index, gene_index=genes
)
for x in result.errors:
    print("ERROR", x)
for x in result.warnings:
    print("WARNING", x)
print(
    json.dumps(
        {
            "errors": len(result.errors),
            "warnings": len(result.warnings),
            "members": len(index),
            "independent_membership": index,
        },
        indent=2,
    )
)
raise SystemExit(bool(result.errors))
