"""Rerun the unchanged biological oracle against the accepted round-one science.

No historical output is overwritten. New assertions below bind the explicit Fe-S
proposal/cofactor and assay-qualified donor cores; they do not change expected
capacity, case membership, mutation operators or sensitivity gates.
"""

import hashlib
import importlib.util
import json
from pathlib import Path

import yaml
from accepted_seal import current_seal

A = Path(__file__).resolve().parent
ROOT = A.parents[3]
OLD = A.parent / "capacity-consultation"


def run():
    spec = importlib.util.spec_from_file_location("historical_mnma_oracle", OLD / "check_capacity.py")
    oracle = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(oracle)
    seal = current_seal()
    for name, expected in seal.items():
        assert hashlib.sha256((ROOT / name).read_bytes()).hexdigest() == expected, name
    # The measured cluster row does not turn native cluster occupancy into an assumption.
    mnma = yaml.safe_load((ROOT / "genes/THET2/mnmA/mnmA-ai-review.yaml").read_text())
    rows = [a for a in mnma["existing_annotations"] if a["term"]["id"] == "GO:0051539"]
    assert len(rows) == 1
    row = rows[0]
    assert row["review"]["action"] == "NEW" and row["evidence_type"] == "IDA"
    assert row["original_reference_id"] == "PMID:31801798"
    assert "reconstituted" in row["review"]["reason"]
    doc = yaml.safe_load(oracle.MODULE.read_text())
    ctype = next(a for n in oracle.walk(doc["module"]) for a in n.get("annotons", [])
                 if a["id"] == "ctype_mnma_activity")
    assert any(c["preferred_term"] == "[4Fe–4S] cluster" for c in ctype["function"]["cofactors"])
    assert any(e.get("source_id") == "PMID:31801798" and "3.72" in e.get("supporting_text", "")
               for e in ctype["evidence"])
    for symbol in ["TT_C0087", "TT_C1373"]:
        donor = yaml.safe_load((ROOT / f"genes/THET2/{symbol}/{symbol}-ai-review.yaml").read_text())
        assert all(not c.get("directly_involved_in") for c in donor["core_functions"])
        assert any(c.get("molecular_function", {}).get("id") == "GO:0031071"
                   and "reconstitution" in c["description"] for c in donor["core_functions"])
    result = oracle.run()
    assert result["counts"] == {
        "cases": 59, "mutations_detected": 9, "gate_sensitivities": 8,
        "reviewed_members": 19, "real_controls": 3,
        "production_atoms": 10, "production_routes": 4,
    }
    previous = json.loads((OLD / "results.json").read_text())
    for field in ["routes", "cases", "mutations", "sensitivities"]:
        assert result[field] == previous[field], field
    result["round1_contract"] = {
        "exact_reconstituted_THET2_FeS_NEW": "PASS",
        "explicit_module_cofactor_with_primary_support": "PASS",
        "Thermus_donor_core_MF_retained_process_unqualified_claim_removed": "PASS",
        "all_historical_case_diagnostics_routes_mutations_sensitivities_unchanged": True,
        "interpretation": "Evidence-qualified capacity, not native flux or cluster occupancy.",
    }
    for p in [Path(__file__).resolve(), A / "accepted-science-seal.json", OLD / "results.json",
              A / "accepted_seal.py", A / "quote-supersession.json"]:
        result["input_hashes"][str(p.relative_to(ROOT))] = hashlib.sha256(p.read_bytes()).hexdigest()
    result["input_hashes"] = dict(sorted(result["input_hashes"].items()))
    return result


if __name__ == "__main__":
    print(json.dumps(run(), indent=2, sort_keys=True))
