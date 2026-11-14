"""Run a strictly additive successor; never invoke the frozen oracle's main."""

import ast
import copy
import hashlib
import json
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
ORIGINAL = HERE.parents[1] / "capacity-consultation"


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write(name, data):
    (HERE / name).write_text(json.dumps(data, indent=2) + "\n")


def load_functions(path, name):
    # exec avoids writing __pycache__ beside the frozen original. Its guarded
    # main is not invoked; import-time behavior only reads the immutable fixtures.
    namespace = {"__name__": name, "__file__": str(path)}
    exec(compile(path.read_text(), str(path), "exec"), namespace)
    return namespace


def functions(path):
    return {
        node.name: ast.dump(node)
        for node in ast.parse(path.read_text()).body
        if isinstance(node, ast.FunctionDef)
    }


def verify_protected():
    snapshot = json.loads((HERE / "protected-inputs.json").read_text())
    for name, before in snapshot.items():
        path = ROOT / name
        assert sha(path) == before["sha256"], name
        assert oct(path.stat().st_mode & 0o777) == before["mode"], name
    return len(snapshot)


def refinement_case(spec, original_bank):
    bank = copy.deepcopy(original_bank)
    member = next(
        value
        for value in bank.values()
        if value["panel"] == "BORPE" and value["role"] == "C"
    )
    cores = member["review"]["core_functions"]
    binding_core = next(
        core
        for core in cores
        if core.get("molecular_function", {}).get("id") == "GO:0008429"
    )
    binding_core["molecular_function"] = {"id": spec["binding"]}
    if not spec["keep_transfer_core"]:
        member["review"]["core_functions"] = [binding_core]
    if spec.get("remove_transport_process"):
        binding_core["directly_involved_in"] = []
    if spec.get("location"):
        binding_core["locations"] = [{"id": spec["location"]}]
    case = {"id": spec["id"], "panel": spec.get("panel", "BORPE")}
    for key in ["keep_roles", "replace", "mask"]:
        if key in spec:
            case[key] = copy.deepcopy(spec[key])
    return bank, case, member


def main():
    protected = verify_protected()
    for name in ["biology.yaml", "cases.yaml", "family-controls.yaml"]:
        assert (HERE / name).read_bytes() == (ORIGINAL / name).read_bytes(), name
    old_functions = functions(ORIGINAL / "check_capacity.py")
    new_functions = functions(HERE / "check_capacity.py")
    changed = [
        name for name, body in old_functions.items() if body != new_functions.get(name)
    ]
    assert changed == ["core_activity", "evaluate"], changed
    assert set(new_functions) - set(old_functions) == {"carrier_binding_satisfies"}
    provenance = json.loads((HERE / "ontology-provenance.json").read_text())
    for item in provenance:
        assert item["http_status"] == 200
        assert item["url"].startswith("https://www.ebi.ac.uk/QuickGO/services/")
        assert sha(ROOT / item["path"]) == item["sha256"]
        if "ancestors" in item["url"]:
            assert item["url"].endswith("?relations=is_a")
    old = load_functions(ORIGINAL / "check_capacity.py", "frozen_readonly_probe")
    successor = load_functions(HERE / "check_capacity.py", "capacity_successor")
    doc = yaml.safe_load(successor["MODULE"].read_text())
    old_bank = old["members"]()
    old_results = [old["evaluate"](doc, case, old_bank) for case in old["all_cases"]()]
    expected = {case["id"]: case["expected"] for case in old["all_cases"]()}
    failures = [
        result for result in old_results if result["capacity"] != expected[result["id"]]
    ]
    assert {result["id"] for result in failures} == {
        "bordetella_five_component",
        "bordetella_flux_unknown_not_negative",
    }
    bp3761 = next(
        member
        for member in old_bank.values()
        if member["panel"] == "BORPE" and member["role"] == "C"
    )
    assert old["core_activity"](bp3761, "C")
    assert all(
        "declared_unit_activity" in result["failures"]["mlac_phospholipid_carrier"]
        for result in failures
    )
    write(
        "original-current-input-probe.json",
        {
            "original_main_executed": False,
            "original_script_sha256": sha(ORIGINAL / "check_capacity.py"),
            "case_count": len(old_results),
            "mismatches": failures,
            "current_BP3761_core_activity_passes_via_transfer_core": True,
            "failure_cause": "Exact declared phospholipid-binding term check rejects its PE-binding descendant",
            "case_results": old_results,
        },
    )
    # This main writes only under HERE. All original cases/mutations/sensitivities
    # and broad-family controls are retained by the AST and fixture checks above.
    successor["main"]()
    result = json.loads((HERE / "results.json").read_text())
    bank = successor["members"]()
    fixture = yaml.safe_load((HERE / "refinement-cases.yaml").read_text())
    controls, sensitivities = [], []
    for spec in fixture["cases"]:
        altered, case, member = refinement_case(spec, bank)
        actual = successor["evaluate"](doc, case, altered)
        assert actual["capacity"] == spec["expected"], (spec, actual)
        reasons = {
            reason for values in actual["failures"].values() for reason in values
        }
        if spec.get("expected_failure"):
            assert spec["expected_failure"] in reasons, (spec, reasons)
        controls.append(
            {
                "specification": spec,
                "core_activity": successor["core_activity"](member, "C"),
                "result": actual,
                "status": "PASS",
                "in_memory_counterfactual_only": True,
            }
        )
        if spec.get("bypass_function_must_rescue"):
            bypassed = successor["evaluate"](doc, case, altered, bypass=["function"])
            assert bypassed["capacity"]
            sensitivities.append(
                {
                    "case": spec["id"],
                    "gate": "function",
                    "normal": False,
                    "bypassed": True,
                    "status": "PASS",
                }
            )
    binding_test = successor["carrier_binding_satisfies"]
    assert binding_test({"GO:0008429"})
    assert binding_test({"GO:0005543"})
    assert not binding_test({"GO:0008289"})
    assert not binding_test({"GO:0005488"})
    witness = next(
        case
        for case in successor["all_cases"]()
        if case["id"] == "bordetella_five_component"
    )
    try:
        successor["carrier_binding_satisfies"] = lambda terms: "GO:0005543" in terms
        assert not successor["evaluate"](doc, witness, bank)["capacity"]
    finally:
        successor["carrier_binding_satisfies"] = binding_test
    assert successor["evaluate"](doc, witness, bank)["capacity"]
    sensitivities.append(
        {
            "case": witness["id"],
            "gate": "verified_ontology_entailment",
            "normal": True,
            "exact_terms_only": False,
            "status": "PASS",
        }
    )
    write(
        "refinement-results.json",
        {
            "status": "PASS",
            "controls": controls,
            "sensitivities": sensitivities,
            "ontology_checks": {
                "PE_binding_entails_phospholipid_binding": True,
                "generic_lipid_binding_does_not_entail_phospholipid_binding": True,
                "generic_binding_is_not_accepted": True,
            },
        },
    )
    new_by_id = {row["id"]: row for row in result["case_results"]}
    changes = [
        {
            "id": old_row["id"],
            "old": old_row["capacity"],
            "new": new_by_id[old_row["id"]]["capacity"],
        }
        for old_row in old_results
        if old_row["capacity"] != new_by_id[old_row["id"]]["capacity"]
    ]
    assert {change["id"] for change in changes} == {row["id"] for row in failures}
    write(
        "semantic-comparison.json",
        {
            "status": "PASS",
            "copied_original_fixtures_byte_identical": True,
            "existing_functions_changed": changed,
            "new_function": "carrier_binding_satisfies",
            "unchanged_existing_functions": sorted(set(old_functions) - set(changed)),
            "changed_original_case_outcomes": changes,
            "original_cases": result["cases"],
            "original_structural_mutations": result["structural_mutations"],
            "original_gate_sensitivities": result["gate_sensitivities"],
            "original_family_controls": len(result["broad_family_controls"]),
            "additional_refinement_cases": len(controls),
            "additional_sensitivities": len(sensitivities),
            "native_flux_claim": False,
            "scope": "Only carrier GO0005543 requirement accepts frozen is_a descendant GO0008429; other activity terms and all native-role gates unchanged",
        },
    )
    assert verify_protected() == protected
    write(
        "preservation-result.json",
        {
            "status": "PASS",
            "protected_byte_and_mode_inputs": protected,
            "original_oracle_outputs_untouched": True,
            "sealed_gene_and_source_closure_handoffs_untouched": True,
            "curated_or_raw_source_edits": 0,
        },
    )
    inputs = set(successor["INPUTS"]) | set(old["INPUTS"])
    inputs |= {
        HERE / name
        for name in [
            "run_successor.py",
            "refinement-cases.yaml",
            "ontology-provenance.json",
            "protected-inputs.json",
            "family-controls.yaml",
        ]
    }
    inputs |= {ORIGINAL / name for name in ["results.json", "input-hashes.json"]}
    write(
        "successor-input-hashes.json",
        {str(path.relative_to(ROOT)): sha(path) for path in sorted(inputs)},
    )
    print(
        json.dumps(
            {
                "status": "PASS",
                "original_cases": result["cases"],
                "structural_mutations": result["structural_mutations"],
                "original_sensitivities": result["gate_sensitivities"],
                "family_controls": len(result["broad_family_controls"]),
                "refinement_cases": len(controls),
                "additional_sensitivities": len(sensitivities),
                "protected_inputs": protected,
            }
        )
    )


if __name__ == "__main__":
    main()
