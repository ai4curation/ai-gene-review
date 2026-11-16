"""Repeat the immutable biological cases with an explicit proposal capability.

The published GPo1 descriptor has no GO identifier. For this finite oracle only,
a private evidence token connects that exact descriptor to its independently
supported gene proposal; it is never exported as a biological annotation.
"""
from copy import deepcopy
from dataclasses import replace
import importlib.util
import json
from pathlib import Path
import sys

import yaml

ROOT = Path(__file__).resolve().parents[4]
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / "src"))
PRIOR = HERE.parent / "capacity-consultation"
spec = importlib.util.spec_from_file_location("prior_capacity", PRIOR / "check_capacity.py")
oracle = importlib.util.module_from_spec(spec)
spec.loader.exec_module(oracle)
NAME = "medium-chain-length poly(3-hydroxyalkanoate) depolymerase activity"
DEFINITION = (
    "Catalysis of the hydrolysis of ester bonds in medium-chain-length poly(3-hydroxyalkanoate), "
    "yielding 3-hydroxyalkanoate monomers and oligomers."
)
TOKEN = "EVIDENCE:gpo1_mcl_pha_depolymerase"

original_compile = oracle.compile_node


def compile_with_proposal_token(node):
    """Keep production topology; add the finite oracle's proposal predicate."""
    identifiers = {
        annoton["id"]
        for part in oracle.walk(node)
        for annoton in part.get("annotons", [])
        if annoton.get("function", {}).get("term", {}).get("id") == TOKEN
    }
    circuit = original_compile(node)

    def attach(value):
        if hasattr(value, "children"):
            value.children = [attach(child) for child in value.children]
            return value
        if value.node_id in identifiers:
            assert not value.function_ids
            return replace(value, function_ids=(TOKEN,))
        return value

    return attach(circuit)


oracle.compile_node = compile_with_proposal_token


def bind(fixtures, override=None):
    result = deepcopy(fixtures)
    proof = {}
    for accession, member in result["members"].items():
        org, gene = member["gene"].split("/")
        path = ROOT / f"genes/{org}/{gene}/{gene}-ai-review.yaml"
        review = (override or {}).get(accession, yaml.safe_load(path.read_text()))
        activities = {c.get("molecular_function", {}).get("id") for c in review["core_functions"]}
        if accession == "P26495":
            for core in review["core_functions"]:
                for proposed in review.get("proposed_new_terms", []):
                    if (
                        core.get("proposed_molecular_function") == NAME
                        and proposed.get("proposed_name") == NAME
                        and proposed.get("proposed_definition") == DEFINITION
                        and proposed.get("proposed_parent", {}).get("id") == "GO:0016788"
                        and (core.get("supported_by") or proposed.get("supported_by"))
                    ):
                        activities.add(TOKEN)
        member["activities"] = [a for a in member["activities"] if a in activities]
        proof[accession] = {"review_sha256": oracle.sha(path), "activities": member["activities"]}
    return result, proof


def main():
    path = ROOT / "modules/bacterial_mcl_pha_synthesis_and_mobilization.yaml"
    published = yaml.safe_load(path.read_text())["module"]
    node = deepcopy(published)
    function = oracle.find(node, "mcl_phaz_gpo1")["annotons"][0]["function"]
    assert "term" not in function and function["preferred_term"] == NAME
    function["term"] = {"id": TOKEN, "label": NAME}
    fixtures = yaml.safe_load((PRIOR / "fixtures.yaml").read_text())
    assert fixtures["members"]["P26495"]["activities"] == ["GO:0016788"]
    fixtures["members"]["P26495"]["activities"] = [TOKEN]
    bound, proof = bind(fixtures)
    for key in fixtures["members"]:
        assert bound["members"][key]["activities"] == fixtures["members"][key]["activities"], key
    cases = oracle.run_cases(node, bound)
    assert len(cases) == 32 and not any(c["errors"] for c in cases)
    mutations = oracle.mutation_checks(node, bound)
    sensitivity = oracle.sensitivity_checks(node, bound)
    review = yaml.safe_load((ROOT / "genes/ECTOL/phaZ/phaZ-ai-review.yaml").read_text())
    controls = {}
    witness = {"panel": "GPo1", "members": ["P26494", "P26495"]}
    for name in ["unknown_proposal", "wrong_parent", "wrong_substrate", "no_support"]:
        bad = deepcopy(review)
        if name == "unknown_proposal":
            bad["core_functions"][0]["proposed_molecular_function"] = "unknown"
        elif name == "wrong_parent":
            bad["proposed_new_terms"][0]["proposed_parent"]["id"] = "GO:0047372"
        elif name == "wrong_substrate":
            bad["proposed_new_terms"][0]["proposed_definition"] = "Hydrolysis of monoacylglycerol."
        else:
            bad["core_functions"][0]["supported_by"] = []
            bad["proposed_new_terms"][0]["supported_by"] = []
        fault, _ = bind(fixtures, {"P26495": bad})
        assert not oracle.evaluate(node, witness, fault)["combined"], name
        controls[name] = {"gpo1_combined_capacity": False}
    assert published == yaml.safe_load(path.read_text())["module"]
    previous = json.loads((HERE.parent / "review-followup/round2-capacity/capacity-results.json").read_text())
    for key, result in [("cases", cases), ("mutations", mutations), ("gate_sensitivity", sensitivity), ("new_bridge_controls", controls)]:
        assert previous[key] == result, key
    output = {"status": "PASS", "case_count": len(cases), "cases": cases,
              "mutations": mutations, "gate_sensitivity": sensitivity,
              "new_bridge_controls": controls, "review_alignment": proof,
              "module_sha256": oracle.sha(path), "original_checker_sha256": oracle.sha(PRIOR / "check_capacity.py"),
              "original_fixture_sha256": oracle.sha(PRIOR / "fixtures.yaml"),
              "all_prior_biological_outcomes_unchanged": True,
              "limits": "Private evidence token used only in this oracle; published module has no GO id for GPo1 activity. No exact oligomer chemistry, universal family grant or native flux inferred."}
    (HERE / "capacity-results.json").write_text(json.dumps(output, indent=2) + "\n")
    print(json.dumps({"status": "PASS", "cases": len(cases), "mutations": len(mutations),
                      "sensitivities": len(sensitivity), "proposal_controls": len(controls)}))


if __name__ == "__main__":
    main()
