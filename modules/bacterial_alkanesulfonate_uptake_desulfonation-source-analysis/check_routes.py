"""Test canonical role coverage and independently active S-313 reconciliation.

The production compiler exposes one atom per annoton, including a complex atom.
The oracle below therefore requires every exact named complex unit; it never
satisfies a complex from one representative or a mixture of species. Presence
means an expressed, functional capability in the declared chemical context.
"""

from pathlib import Path
import json
import yaml
import itertools
from dataclasses import asdict
from ai_gene_review.module_logic import (
    compile_module,
    compile_node,
    is_satisfied,
    abduce,
)

ROOT = Path(__file__).resolve().parents[2]
SLUG = "bacterial_alkanesulfonate_uptake_desulfonation"
doc = yaml.safe_load((ROOT / "modules" / f"{SLUG}.yaml").read_text())
variants = doc["module"]["variant_sets"][0]["variants"]
assert len(variants) == 3
requirements = {}
sets = {}
for v in variants:
    ids = set()
    for part in v["parts"]:
        for a in part["node"]["annotons"]:
            p = a["participant"]
            ps = (
                [u["participant"] for u in p["protein_complex"]["active_units"]]
                if p["selector_type"] == "PROTEIN_COMPLEX"
                else [p]
            )
            assert all(x["selector_type"] == "GENE_PRODUCT" for x in ps)
            accs = {
                x["gene_product"]["term"]["id"].removeprefix("UniProtKB:") for x in ps
            }
            assert len(accs) == (3 if p["selector_type"] == "PROTEIN_COMPLEX" else 1)
            requirements[a["id"]] = accs
            ids |= accs
    sets[v["id"]] = ids
assert len(set.union(*sets.values())) == 15
circuit = compile_module(doc)
results = []


def holds(present):
    return lambda atom: requirements[atom.node_id] <= present


def case(name, present, expected):
    actual = is_satisfied(circuit, holds(present))
    assert actual == expected, (name, actual)
    results.append({"case": name, "canonical_coverage": actual, "expected": expected})


case("empty_context", set(), False)
for name, accs in sets.items():
    case(name + "_complete", accs, True)
    for a in sorted(accs):
        case(name + "_without_" + a, accs - {a}, False)
    for a in sorted(accs):
        case(name + "_singleton_" + a, {a}, False)
# All D/E proteins cannot substitute for a complete importer.
allacc = set.union(*sets.values())
transport = set.union(*(x for k, x in requirements.items() if "ssuabc" in k))
case("all_oxygenases_reductases_without_transport", allacc - transport, False)
# Every one-unit-per-species hybrid: retain all D/E proteins, but no intact native transporter.
tgroups = [requirements[v["parts"][0]["node"]["annotons"][0]["id"]] for v in variants]
for i, combo in enumerate(itertools.product(*[sorted(s) for s in tgroups])):
    case(
        "one_subunit_from_each_species_" + str(i),
        set(combo) | (allacc - transport),
        False,
    )
# Explicit native activity assertion is reconciled, not overwritten by coverage.
s313 = next(v for v in variants if v["id"] == "s313_canonical_ssu")
present = sets[s313["id"]] - {"O85762"}
reconciliation = abduce(compile_node(s313), holds(present), asserted_active=True)
assert reconciliation.classification == "ABDUCTION_TARGET"
assert "s313_ssue_fmn_reduction" in reconciliation.gap_steps
result = {
    "cases": len(results),
    "passed": len(results),
    "reconciliation": asdict(reconciliation),
    "biological_interpretation": "Native S-313 growth without SsuE remains established. The missing canonical atom identifies an unmodeled reduced-FMN supplier or alternative route; it does not predict inactivity. SsuF and alternative uptake remain outside the named-capability sufficiency claim.",
    "scenarios": results,
}
print(json.dumps(result, indent=2))
