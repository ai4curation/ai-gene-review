"""Rerun the prior biological oracle with the approved normalized NTR definition.

Only the exact target proposal definition and output directory are adapted. All
32 cases, seven mutations, seven sensitivity gates and four bridge-fault controls
come from the immutable prior implementation. No science file is written.
"""

from copy import deepcopy
import contextlib
import importlib.util
import io
import json

import yaml

from seal import AUDIT, HERE, IMPL, ROOT, sha, verify_seal

DEFINITION = (
    "Catalysis of the hydrolysis of ester bonds in medium-chain-length poly(3-hydroxyalkanoate), "
    "yielding 3-hydroxyalkanoate monomers and oligomers."
)


def without_gaps(value):
    if isinstance(value, dict):
        return {k: without_gaps(v) for k, v in value.items() if k != "knowledge_gaps"}
    if isinstance(value, list):
        return [without_gaps(v) for v in value]
    return value


def run():
    accepted = verify_seal()
    previous = HERE.parent / "module-integration"
    spec = importlib.util.spec_from_file_location("mcl_prior_integration", previous / "check_capacity.py")
    oracle = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(oracle)
    module_name = "modules/bacterial_mcl_pha_synthesis_and_mobilization.yaml"
    baseline = json.loads((IMPL / "baseline.json").read_text())
    current = yaml.safe_load((ROOT / module_name).read_text())
    assert without_gaps(baseline["documents"][module_name]["document"]) == without_gaps(current)
    # Preserve all identity, evidence, parent and substrate checks; update only
    # the exact normalized definition accepted in round two.
    oracle.DEFINITION = DEFINITION
    oracle.HERE = HERE
    with contextlib.redirect_stdout(io.StringIO()):
        oracle.main()
    result = json.loads((HERE / "capacity-results.json").read_text())
    prior = json.loads((previous / "capacity-results.json").read_text())
    assert (result["case_count"], len(result["mutations"]), len(result["gate_sensitivity"]),
            len(result["new_bridge_controls"])) == (32, 7, 7, 4)
    for key in ["cases", "mutations", "gate_sensitivity", "new_bridge_controls"]:
        assert result[key] == prior[key], key
    for accession, alignment in result["review_alignment"].items():
        old = deepcopy(prior["review_alignment"][accession])
        old.pop("review_sha256")
        now = deepcopy(alignment)
        now.pop("review_sha256")
        assert now == old, accession
    assert result["gpo1_exact_oligomer_reaction_granted"] is False
    result.pop("module_changed")
    result["science_files_modified_by_checker"] = False
    result["module_unchanged_outside_knowledge_gaps"] = True
    result["all_prior_cases_controls_and_activity_grants_unchanged"] = True
    result["adaptation"] = "Recognize only the approved normalized P26495 proposed definition; the supported GO:0016788 genus bridge and all biological exclusions are unchanged."
    paths = [HERE / "check_capacity.py", HERE / "seal.py", HERE / "phaA-quote-repair.json", IMPL / "handoff.json",
             previous / "check_capacity.py", previous / "capacity-results.json",
             AUDIT / "capacity-consultation/check_capacity.py", AUDIT / "capacity-consultation/fixtures.yaml",
             ROOT / "src/ai_gene_review/module_logic.py"]
    result["input_hashes"] = dict(sorted({**accepted["source_dependencies"], **accepted["files"],
                                        **{str(p.relative_to(ROOT)): sha(p) for p in paths}}.items()))
    verify_seal()
    (HERE / "capacity-results.json").write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    return result


if __name__ == "__main__":
    result = run()
    print(json.dumps({"status": result["status"], "cases": result["case_count"],
                      "mutations": len(result["mutations"]),
                      "sensitivities": len(result["gate_sensitivity"]),
                      "bridge_controls": len(result["new_bridge_controls"])}))
