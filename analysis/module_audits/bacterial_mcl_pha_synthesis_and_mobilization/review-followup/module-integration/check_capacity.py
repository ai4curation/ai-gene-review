"""Additive PR6194 oracle: preserve cases; recognize the reviewed NTR genus."""
from copy import deepcopy
import importlib.util
import json
import sys
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
AUDIT = HERE.parents[1]
OLD = AUDIT / "capacity-consultation"
SPEC = importlib.util.spec_from_file_location("published_mcl_capacity", OLD / "check_capacity.py")
OLD_CODE = importlib.util.module_from_spec(SPEC)
sys.dont_write_bytecode = True
SPEC.loader.exec_module(OLD_CODE)
NAME = "medium-chain-length poly(3-hydroxyalkanoate) depolymerase activity"
DEFINITION = (
    "Catalysis of the hydrolysis of ester bonds in medium-chain-length poly(3-hydroxyalkanoate), "
    "yielding shorter polyester chains and hydroxyalkanoate products."
)


def qualified_activities(accession, review):
    """Only a specifically adjudicated proposal entails its supported GO genus."""
    activities = {c.get("molecular_function", {}).get("id") for c in review.get("core_functions", [])}
    activities.discard(None)
    if accession == "P26495":
        for core in review.get("core_functions", []):
            if core.get("proposed_molecular_function") != NAME:
                continue
            for proposal in review.get("proposed_new_terms", []):
                if (proposal.get("proposed_name") == NAME
                        and proposal.get("proposed_definition") == DEFINITION
                        and proposal.get("proposed_parent", {}).get("id") == "GO:0016788"
                        and (proposal.get("supported_by") or core.get("supported_by"))):
                    activities.add("GO:0016788")
    return activities


def bind_reviews(fixtures, overrides=None):
    """Remove capabilities not supported by current reviews, before circuit tests."""
    result = deepcopy(fixtures)
    proofs = {}
    for accession, member in result["members"].items():
        org, gene = member["gene"].split("/")
        path = ROOT / f"genes/{org}/{gene}/{gene}-ai-review.yaml"
        review = (overrides or {}).get(accession, yaml.safe_load(path.read_text()))
        assert review["id"] == accession and review["status"] == "COMPLETE"
        supported = qualified_activities(accession, review)
        member["activities"] = [a for a in member["activities"] if a in supported]
        proofs[accession] = {"review_sha256": OLD_CODE.sha(path), "activities": member["activities"],
                            "proposal_genus_bridge": accession == "P26495" and "GO:0016788" in supported}
    return result, proofs


def main():
    module_path = ROOT / "modules/bacterial_mcl_pha_synthesis_and_mobilization.yaml"
    node = yaml.safe_load(module_path.read_text())["module"]
    fixtures = yaml.safe_load((OLD / "fixtures.yaml").read_text())
    bound, proofs = bind_reviews(fixtures)
    for accession, member in fixtures["members"].items():
        assert bound["members"][accession]["activities"] == member["activities"], accession
    cases = OLD_CODE.run_cases(node, bound)
    assert not any(c["errors"] for c in cases)
    mutations = OLD_CODE.mutation_checks(node, bound)
    gates = OLD_CODE.sensitivity_checks(node, bound)
    # These independently fault the new review-to-capability bridge. They are not
    # replacements for any original biological cases, mutations or sensitivities.
    review_path = ROOT / "genes/ECTOL/phaZ/phaZ-ai-review.yaml"
    review = yaml.safe_load(review_path.read_text())
    witness = {"panel": "GPo1", "members": ["P26494", "P26495"]}
    assert OLD_CODE.evaluate(node, witness, bound)["combined"]
    controls = {}
    for name in ["unknown_proposal", "wrong_parent", "wrong_substrate", "no_support"]:
        bad = deepcopy(review)
        if name == "unknown_proposal":
            bad["core_functions"][0]["proposed_molecular_function"] = "uncharacterized hydrolase"
        elif name == "wrong_parent":
            bad["proposed_new_terms"][0]["proposed_parent"]["id"] = "GO:0047372"
        elif name == "wrong_substrate":
            bad["proposed_new_terms"][0]["proposed_definition"] = "Hydrolysis of monoacylglycerol."
        else:
            bad["core_functions"][0]["supported_by"] = []
            bad["proposed_new_terms"][0]["supported_by"] = []
        revised, _ = bind_reviews(fixtures, {"P26495": bad})
        assert not OLD_CODE.evaluate(node, witness, revised)["combined"], name
        controls[name] = {"gpo1_combined_capacity": False}
    assert "GO:0050527" not in qualified_activities("P26495", review)
    assert OLD_CODE.run_cases(node, bound) == cases
    output = {"status": "PASS", "module_sha256": OLD_CODE.sha(module_path),
              "module_changed": False, "original_checker_sha256": OLD_CODE.sha(OLD / "check_capacity.py"),
              "original_fixtures_sha256": OLD_CODE.sha(OLD / "fixtures.yaml"),
              "case_count": len(cases), "cases": cases, "mutations": mutations,
              "gate_sensitivity": gates, "new_bridge_controls": controls, "review_alignment": proofs,
              "gpo1_exact_oligomer_reaction_granted": False,
              "limits": "Finite source-qualified capacity, not genome discovery or native flux. Original external substrate, panel, access and evidence gates are unchanged. Only the exact reviewed P26495 proposal is recognized through its declared supported genus; no general NTR-to-GO lookup is asserted."}
    (HERE / "capacity-results.json").write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"cases": len(cases), "mutations": len(mutations), "sensitivities": len(gates),
                      "additional_bridge_controls": len(controls), "status": "PASS"}))


if __name__ == "__main__":
    main()
