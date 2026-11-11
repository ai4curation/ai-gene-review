"""Evaluate curated fructose-system coverage through the production circuit.

This is an explicit, scoped evidence oracle, not a proteome classifier. The
compiler exposes family/function ids but not free-text fusion semantics. Rules
in the audited fixture supply those constraints and require their domains on
one protein. Matched-system coverage is distinct from native flux or experimental
proof of every internal transfer. Component tests retain secondary TagK activity.
"""
from copy import deepcopy
from pathlib import Path
import hashlib
import json

import yaml

from ai_gene_review.module_logic import compile_module, is_satisfied, iter_atoms

ROOT = Path(__file__).resolve().parents[2]
MODULE = ROOT / "modules/bacterial_fructose_pts_catabolism.yaml"
AUDIT = ROOT / "analysis/module_audits/bacterial_fructose_pts_catabolism"
FIXTURES = AUDIT / "capacity-fixtures.yaml"


def eligible(atom, protein, rule, architecture=True, specificity=True):
    if not set(atom.family_ids).intersection(protein["family_ids"]):
        return False
    if specificity and rule["function"] not in protein["functions"]:
        return False
    return not architecture or set(rule["domains_all"]) <= set(protein["domain_ids"])


def run_checks(doc, fixtures, architecture=True, specificity=True, match_system=True):
    circuit = compile_module(doc)
    atoms = {a.node_id: a for a in iter_atoms(circuit)}
    rules = fixtures["requirements"]
    proteins = fixtures["proteins"]
    assert set(atoms) == set(rules), "A biochemical step disappeared or changed identity"
    selectors = {
        a["id"]: a["participant"]
        for part in doc["module"]["parts"] for a in part["node"]["annotons"]
    }
    for key, rule in rules.items():
        if "module_architecture_descriptor" in rule:
            assert selectors[key]["required_domain"]["preferred_term"] == rule["module_architecture_descriptor"], key
    rows = []

    def component(key, available, data=proteins):
        return any(eligible(atoms[key], data[p], rules[key], architecture, specificity)
                   for p in available)

    def coverage(available):
        candidates = [set(available)]
        if match_system:
            systems = {proteins[p]["system"] for p in available}
            candidates = [{p for p in available if proteins[p]["system"] == system}
                          for system in systems if system != "CONTROL"]
        return any(is_satisfied(circuit, lambda atom: any(
            eligible(atom, proteins[p], rules[atom.node_id], architecture, specificity)
            for p in candidate)) for candidate in candidates)

    def check(name, actual, expected, interpretation):
        assert actual == expected, (name, actual, expected)
        rows.append({"case": name, "observed": actual, "expected": expected,
                     "interpretation": interpretation})

    for system in fixtures["complete_fused_panels"]:
        panel = fixtures["matched_panels"][system]
        check(system + "_matched_coverage", coverage(set(panel.values())), True,
              "Curated matched-role coverage; assay and strain limits remain in the member reviews.")
        for role in "BAK":
            check(system + "_missing_" + role, coverage(set(panel.values()) - {panel[role]}), False,
                  "The missing modeled component is not silently supplied by another role.")
        for key, role in [("frub_pep_phosphotransferase_activity", "B"),
                          ("frub_internal_relay_activity", "B"),
                          ("frua_transport_phosphorylation_activity", "A"), ("fruk_activity", "K")]:
            check(system + "_component_" + role + "_" + key,
                  component(key, {panel[role]}), True, "Supported component predicate, not independent native flux.")
    for system in fixtures["partial_panels"]:
        panel = fixtures["matched_panels"][system]
        check(system + "_no_asserted_fused_relay", coverage(set(panel.values())), False,
              "Component evidence does not establish a complete fused-relay pathway.")
        check(system + "_A_component", component("frua_transport_phosphorylation_activity", {panel["A"]}), True,
              "Fructose PTS capability; Deinococcus native donor remains unresolved.")
        check(system + "_K_component", component("fruk_activity", {panel["K"]}), True,
              "Specific kinase assignment is reviewed separately from whole-pathway capacity.")
    for acc in ["P08839", "P37177"]:
        for key in ["frub_pep_phosphotransferase_activity", "frub_internal_relay_activity"]:
            check(acc + "_not_fused_FruB_" + key, component(key, {acc}), False,
                  "Enzyme-I activity and family membership do not supply HPr/EIIA on the same protein.")
    check("MngA_not_fructose_specific", component("frua_transport_phosphorylation_activity", {"P54745"}), False,
          "A related fused PTS transports mannosyl-glycerate, not the asserted fructose substrate.")
    check("6PFK_not_1PFK", component("fruk_activity", {"P06999"}), False,
          "Fructose 6-phosphate and fructose 1-phosphate are different kinase substrates.")
    for acc in ["D4GYE6", "Q65EY9"]:
        check(acc + "_1PFK_activity_not_denied", component("fruk_activity", {acc}), True,
              "Direct archaeal 1-PFK or secondary TagK activity is real; it does not prove a matched bacterial route.")
    # Even granting shared net activity to the archaeal component set cannot
    # substitute a union of separate proteins for the same-protein requirement.
    partial = deepcopy(proteins)
    for acc in ["D4GYE1", "D4GYE5"]:
        partial[acc]["functions"] = ["GO:0022877"]
    check("split_archaeal_components_not_fused", component(
        "frua_transport_phosphorylation_activity", {"D4GYE1", "D4GYE5"}, partial), False,
        "Grant system-level substrate capability for this probe; EIIB/EIIC must still coexist on one protein.")
    mixed = {fixtures["matched_panels"]["RHOCA"]["B"],
             fixtures["matched_panels"]["PSEPK"]["A"], fixtures["matched_panels"]["PSEPK"]["K"]}
    check("unverified_cross_species_mix", coverage(mixed), False,
          "No asserted matched-system evidence; this does not predict that heterologous complementation is impossible.")
    check("empty_evidence", coverage(set()), False, "No carrier evidence.")
    return rows


def main():
    doc = yaml.safe_load(MODULE.read_text())
    fixtures = yaml.safe_load(FIXTURES.read_text())
    for protein in fixtures["proteins"].values():
        for key in ["source", "review"]:
            if key in protein:
                assert hashlib.sha256((ROOT / protein[key]).read_bytes()).hexdigest() == protein[key + "_sha256"], protein[key]
    cases = run_checks(doc, fixtures)
    mutations = []
    for label, kwargs in [("ignore_same_protein_architecture", {"architecture": False}),
                          ("ignore_substrate_specificity", {"specificity": False}),
                          ("mix_unverified_systems", {"match_system": False})]:
        mutations.append((label, doc, fixtures, kwargs))
    for index in [2, 3]:
        mutant = deepcopy(doc)
        mutant["module"]["parts"][index]["optional"] = True
        mutations.append(("make_component_optional_" + str(index), mutant, fixtures, {}))
    for index in [0, 1]:
        mutant = deepcopy(doc)
        mutant["module"]["parts"].pop(index)
        mutations.append(("drop_phosphorelay_step_" + str(index), mutant, fixtures, {}))
    caught = []
    for label, mutant, data, kwargs in mutations:
        try:
            run_checks(mutant, data, **kwargs)
        except AssertionError:
            caught.append(label)
        else:
            raise AssertionError("Undetected mutation: " + label)
    result = {"status": "PASS", "case_count": len(cases), "cases": cases,
              "mutations_rejected": caught, "native_flux_asserted": False,
              "oracle": "Explicit audited activity/domain/system evidence supplied to the production circuit; no automatic enforcement of free-text descriptors claimed.",
              "limits": fixtures["limits"]}
    (AUDIT / "capacity-results.json").write_text(json.dumps(result, indent=2) + "\n")
    print(f"PASS: {len(cases)} evidence-coverage checks; {len(caught)} mutations rejected")


if __name__ == "__main__":
    main()
