"""Additional restored-classification controls; no biological universality claim."""
import copy
import importlib.util
import json
import sys
from pathlib import Path

import yaml

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("copied_capacity", HERE / "check_capacity.py")
base = importlib.util.module_from_spec(spec)
spec.loader.exec_module(base)


def main():
    doc = yaml.safe_load(base.MODULE.read_text())
    circuit, _ = base.structural_requirements(doc)
    atoms = {atom.node_id: atom for atom in base.iter_atoms(circuit)}
    members = base.registry()
    targets = {
        "ahcy_activity": ("PANTHER:PTHR23420", "O51933", "THEMA"),
        "mtnn_activity": ("PANTHER:PTHR46832", "P0AF12", "ECOLI"),
        "meth_activity": ("PANTHER:PTHR45833", "P13009", "ECOLI"),
        "mete_activity": ("PANTHER:PTHR30519", "P25665", "ECOLI"),
    }
    cases = []
    sensitivities = {}
    mutations = {}
    for role, (family, accession, organism) in targets.items():
        atom = atoms[role]
        assert atom.family_ids == (family,), (role, atom.family_ids)
        profile = base.CONTEXT_PROFILES[organism]
        context = {
            "organism": organism, "members": [accession],
            "available_inputs": profile["available"],
            "profile": "biochemical_capacity",
        }
        variants = [
            ("qualified positive", {}, True),
            ("classification removed", {"masked_classifications": [family]}, False),
            ("function evidence removed", {
                "masked_functions": {accession: list(atom.function_ids)}}, False),
            ("role/architecture qualification removed", {
                "masked_roles": {accession: [role]}}, False),
            ("direct source support removed", {"unsupported_roles": [role]}, False),
            ("native flux not inferred", {"profile": "native_flux"}, False),
        ]
        for label, update, expected in variants:
            ctx = {**context, **update}
            actual = base.is_satisfied(atom, base.Oracle(members, ctx))
            assert actual == expected, (role, label, actual)
            cases.append({"role": role, "name": label, "expected": expected,
                          "actual": actual, "context": ctx})
            if label == "classification removed":
                bypass = base.is_satisfied(atom, base.Oracle(members, ctx, ["family"]))
                assert bypass is True
                sensitivities[role] = "Removing only the classification gate flips this negative"
        # A broad family hit with even an asserted MF cannot bypass exact-panel evidence.
        proxy = "synthetic_unreviewed_" + role
        fixture = copy.deepcopy(members)
        fixture[proxy] = {**copy.deepcopy(members[accession]), "roles": [role]}
        ctx = {**context, "members": [proxy]}
        actual = base.is_satisfied(atom, base.Oracle(fixture, ctx))
        assert actual is False
        cases.append({"role": role, "name": "same-family unreviewed proxy excluded",
                      "expected": False, "actual": actual,
                      "limit": "Synthetic evidence-control fixture, not a real protein or activity-loss claim"})
        for mutation in ["remove", "wrong_family"]:
            changed = copy.deepcopy(doc)
            participant = base.index_nodes(changed)[role]["participant"]["family"]
            if mutation == "remove":
                participant.pop("term")
            else:
                participant["term"] = {"id": "PANTHER:PTHR11964"}
            altered = {a.node_id: a for a in base.iter_atoms(base.compile_node(changed["module"]))}
            assert altered[role].family_ids != (family,)
            if mutation == "remove":
                # Removing the selector must be caught because it admits a witness
                # from which the required classification evidence was removed.
                changed_context = {**context, "masked_classifications": [family]}
                counterfactual = base.is_satisfied(altered[role], base.Oracle(members, changed_context))
                assert counterfactual is True
                expected = False
            else:
                # A wrong selector must reject the independently grounded positive.
                counterfactual = base.is_satisfied(altered[role], base.Oracle(members, context))
                assert counterfactual is False
                expected = True
            mutations[role + ":" + mutation] = {
                "status": "DETECTED", "correct_model_expected": expected,
                "mutated_actual": counterfactual,
                "declaration_check": "exact verified classification also required"}
    # Compare the prior suite by biological expectations, not obsolete file hashes.
    prior = json.loads((HERE.parent / "review-followup/root-integration/capacity-results.json").read_text())
    rerun = json.loads((HERE / "prior-capacity-results.json").read_text())
    def signature(result):
        return [(c["name"], c["node"], c["context"], c["expected"], c["actual"])
                for c in result["cases"]]
    assert signature(prior) == signature(rerun)
    assert prior["mutations"] == rerun["mutations"]
    assert prior["gate_sensitivities"] == rerun["gate_sensitivities"]
    result = {
        "status": "PASS", "prior_cases": len(rerun["cases"]),
        "prior_mutations": len(rerun["mutations"]), "prior_gate_sensitivities": 10,
        "added_cases": len(cases), "added_mutations": len(mutations),
        "added_classification_sensitivities": len(sensitivities),
        "total_cases": len(rerun["cases"]) + len(cases),
        "prior_expectations_preserved": True, "cases": cases,
        "mutations": mutations, "classification_sensitivities": sensitivities,
        "limits": "Finite reviewed-panel evidence tests; architecture is curated role qualification, not sequence discovery. Unreviewed proteins are unsupported, not biologically inactive."
    }
    (HERE / "extended-capacity-results.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({k: v for k, v in result.items() if k not in {
        "cases", "mutations", "classification_sensitivities", "limits"}}))


if __name__ == "__main__":
    main()
