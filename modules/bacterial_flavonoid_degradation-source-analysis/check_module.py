"""Check represented Fde roles, without equating coverage with native catabolism.

The production compiler evaluates exact reviewed exemplars. These scenarios test
whether uncertain partners accidentally become requirements and whether the
proposed late chemical steps silently disappear. No scenario is a knockout
prediction or a demonstration of substrate specificity in an untested species.
All three FdeB reviews leave ester specificity and native pathway participation
unresolved; assigning a candidate carrier here does not assert either activity.
"""

from copy import deepcopy
from pathlib import Path
import json

import yaml

from ai_gene_review.module_logic import compile_module, compile_node, is_satisfied

ROOT = Path(__file__).resolve().parents[2]
MODULE = ROOT / "modules/bacterial_flavonoid_degradation.yaml"
OUTPUT = ROOT / "analysis/module_audits/bacterial_flavonoid_degradation/capacity-results.json"

# E, C, J, B, I are candidate carriers of the six chemical roles (I appears twice).
# D and H are associated proteins with unresolved position and necessity.
PANELS = {
    "HERSS": {"E": "D8J0W9", "C": "D8J0W7", "J": "D8J0X4", "B": "D8J0W6",
              "I": "D8J0X3", "D": "D8J0W8", "H": "D8J0X2"},
    "PSEPK": {"E": "Q88I03", "C": "Q88I05", "J": "Q88HZ6", "B": "Q88I07",
              "I": "Q88HZ7", "D": "Q88I04", "H": "Q88HZ8"},
    "BRADU": {"E": "Q89GC0", "C": "Q89GB8", "J": "Q89GC4", "B": "Q89GB7",
              "I": "Q89GC3", "D": "Q89GB9", "H": "Q89GC2"},
}


def covers(circuit, accessions):
    return is_satisfied(circuit, lambda a: bool(set(a.uniprots) & accessions))


def run_checks(doc):
    root = compile_module(doc)
    nodes = {p["node"]["id"]: p["node"] for p in doc["module"]["parts"]}
    entry = compile_node(nodes["r13074_naringenin_hydroxylation"])
    cleavage = compile_node(nodes["r13075_a_ring_cleavage"])
    results = []

    def check(name, actual, expected, basis):
        assert actual == expected, (name, actual, expected)
        results.append({"case": name, "observed": actual, "expected": expected,
                        "interpretation": basis})

    for species, panel in PANELS.items():
        role_carriers = {panel[k] for k in "ECJBI"}
        check(species + "_candidate_role_coverage", covers(root, role_carriers), True,
              "Coverage of proposed roles only; late specificity and native flux unresolved.")
        for extras in [set(), {panel["D"]}, {panel["H"]}, {panel["D"], panel["H"]}]:
            check(species + "_unresolved_context_" + "_".join(sorted(extras)),
                  covers(root, role_carriers | extras), True,
                  "No unsupported obligatory D/H conjunction; not a dispensability assay.")
        for role in "ECJBI":
            check(species + "_unfilled_proposed_role_" + role,
                  covers(root, set(panel.values()) - {panel[role]}), False,
                  "Missing represented role, not a claim that this gene is biologically necessary.")
        check(species + "_entry_without_D", covers(entry, {panel["E"]}), True,
              "HERSS purified FdeE works without added FdeD; other species are inferred carriers.")
        check(species + "_D_is_not_monooxygenase", covers(entry, {panel["D"]}), False,
              "Rieske cluster binding does not establish FdeE catalysis.")
        check(species + "_cleavage_without_asserted_H_partner", covers(cleavage, {panel["C"]}),
              True, "FdeH dependence is unresolved and is not asserted by coassignment.")
        check(species + "_H_is_not_established_dioxygenase", covers(cleavage, {panel["H"]}),
              False, "Cupin membership alone does not establish this ring-cleavage reaction.")
    check("generic_family_hit_does_not_prove_route",
          covers(root, {"PANTHER:PTHR13789", "PANTHER:PTHR22946"}), False,
          "Broad family labels cannot stand in for target sequence and substrate evidence.")
    check("empty_panel", covers(root, set()), False, "No represented carriers.")
    return results


def main():
    doc = yaml.safe_load(MODULE.read_text())
    results = run_checks(doc)
    mutations = []
    for target in ["fded_unresolved_locus_role", "fdeh_unresolved_locus_role"]:
        mutant = deepcopy(doc)
        next(p for p in mutant["module"]["parts"] if p["node"]["id"] == target)["optional"] = False
        mutations.append(("force_" + target + "_required", mutant))
    for target in ["r13076_c_c_hydrolysis", "r13077_lactone_hydrolysis"]:
        mutant = deepcopy(doc)
        next(p for p in mutant["module"]["parts"] if p["node"]["id"] == target)["optional"] = True
        mutations.append(("silently_drop_" + target, mutant))
    caught = []
    for name, mutant in mutations:
        try:
            run_checks(mutant)
        except AssertionError:
            caught.append(name)
        else:
            raise AssertionError("Undetected mutation: " + name)
    result = {"status": "PASS", "coverage_only": True,
              "native_complete_catabolism_inferred_from_coverage": False,
              "case_count": len(results), "cases": results, "mutations_rejected": caught,
              "limits": "Exact exemplars test modeled coverage. HERSS entry assays and whole-locus phenotypes do not establish every late carrier; PSEPK/BRADU substrate specificity remains inferred. All three FdeB representatives have unresolved bond specificity and native process participation; their inclusion is proposed-role coverage only."}
    OUTPUT.write_text(json.dumps(result, indent=2) + "\n")
    print(f"PASS: {len(results)} coverage checks; {len(caught)} mutations rejected")


if __name__ == "__main__":
    main()
