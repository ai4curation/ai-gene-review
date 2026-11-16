"""Rerun frozen Lol cases into additive outputs; audit additional evidence gates."""

import copy
import hashlib
import importlib.util
import json
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
OLD = HERE.parents[1] / "capacity-consultation"
MODULE = ROOT / "modules/bacterial_lol_lipoprotein_trafficking.yaml"


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main():
    legacy = load("lol_original_capacity", OLD / "check_capacity.py")
    out = HERE / "original-rerun"
    out.mkdir(exist_ok=True)
    original_files = {
        str(p.relative_to(ROOT)): sha(p) for p in OLD.iterdir() if p.is_file()
    }
    (out / "cases.yaml").write_bytes((OLD / "cases.yaml").read_bytes())
    legacy.HERE = out
    legacy.main()  # unchanged 32 cases, five actual-module mutations and five sensitivities
    assert all(sha(ROOT / p) == h for p, h in original_files.items())
    records = legacy.load_members()
    document = yaml.safe_load(MODULE.read_text())
    rules = yaml.safe_load((HERE / "gates.yaml").read_text())
    for record in records.values():
        doc = yaml.safe_load((ROOT / record["path"]).read_text())
        record["locations"] = {
            loc["id"] for c in doc["core_functions"] for loc in c.get("locations", [])
        }
        record["source_licensed"] = all(
            bool(c.get("supported_by")) for c in doc["core_functions"]
        )

    def contract(doc):
        anns = {
            a["id"]: a
            for n in legacy.walk(doc["module"])
            for a in n.get("annotons", [])
        }
        for aid, rule in rules["annoton_contracts"].items():
            ann = anns[aid]
            fn = ann.get("function", {})
            if "function" in rule and fn.get("term", {}).get("id") != rule["function"]:
                return False
            if "proposed" in rule and fn.get("preferred_term") != rule["proposed"]:
                return False
            if rule["location"] not in {
                loc["term"]["id"] for loc in ann.get("locations", [])
            }:
                return False
        units = {
            u["id"]: u
            for a in anns.values()
            for u in a.get("participant", {})
            .get("protein_complex", {})
            .get("active_units", [])
        }
        return all(
            units[uid].get("function", {}).get("term", {}).get("id") == "GO:0016887"
            for uid in rules["active_atpase_units"]
        )

    def evaluate(
        doc,
        case,
        recs,
        *,
        domain=True,
        compartment=True,
        source=True,
        atpase=True,
        **kwargs,
    ):
        assert contract(doc), (
            "Module function/location declaration no longer matches source-grounded requirement"
        )
        filtered = {}
        for acc, rec in recs.items():
            rule = rules["role_requirements"][rec["role"]]
            if domain:
                if (
                    "domains_any" in rule
                    and not set(rule["domains_any"]) & rec["families"]
                ):
                    continue
                if not set(rule.get("domains_all", [])) <= rec["families"]:
                    continue
            if compartment and rule["location"] not in rec["locations"]:
                continue
            if source and not rec["source_licensed"]:
                continue
            if atpase and "activity" in rule and rule["activity"] not in rec["mf"]:
                continue
            filtered[acc] = rec
        return legacy.evaluate(doc, case, filtered, **kwargs)

    cases = yaml.safe_load((OLD / "cases.yaml").read_text())["cases"]
    cases.extend(
        [
            dict(
                id="taxon_label_without_members",
                members=[],
                context="ECOLI",
                expected=dict(extraction=False, delivery=False, complete=False),
            ),
            dict(
                id="flaj1_pair_with_foreign_extractor",
                members=["P0ADC3", "P75957", "P75958", "A5FI22", "A5FL25"],
                context="reviewed_native_panel",
                expected=dict(extraction=True, delivery=False, complete=False),
            ),
        ]
    )
    results = []
    for case in cases:
        result, atoms = evaluate(document, case, records)
        assert result == case["expected"], case["id"]
        results.append({"id": case["id"], "result": result, "atom_truth": atoms})
    ecoli = next(c for c in cases if c["id"] == "ecoli_complete")
    sensitivities = []
    for name, acc, field, flag in [
        ("carrier_domain", "P61316", "families", "domain"),
        ("carrier_compartment", "P61316", "locations", "compartment"),
        ("insertase_compartment", "P61320", "locations", "compartment"),
        ("membrane_domain", "P0ADC3", "families", "domain"),
        ("carrier_source", "P61316", "source_licensed", "source"),
        ("canonical_ATPase", "P75957", "mf", "atpase"),
    ]:
        masked = copy.deepcopy(records)
        if field == "source_licensed":
            masked[acc][field] = False
        elif field == "families":
            # Preserve the original family selector, removing only domain signatures.
            masked[acc][field] = {
                x for x in masked[acc][field] if not x.startswith("Pfam:")
            }
        else:
            masked[acc][field].clear()
        qualified = evaluate(document, ecoli, masked)[0]
        weakened = evaluate(document, ecoli, masked, **{flag: False})[0]
        assert not qualified["complete"] and weakened["complete"], (
            name,
            qualified,
            weakened,
        )
        sensitivities.append(
            {"gate": name, "qualified": qualified, "disabled_gate": weakened}
        )
    mutations = []
    for name in [
        "carrier_function_removed",
        "ATPase_function_wrong",
        "carrier_compartment_wrong",
        "insertion_function_wrong",
    ]:
        mutated = copy.deepcopy(document)
        anns = {
            a["id"]: a
            for n in legacy.walk(mutated["module"])
            for a in n.get("annotons", [])
        }
        if name == "carrier_function_removed":
            anns["lola_carrier"].pop("function")
        elif name == "ATPase_function_wrong":
            units = anns["lolcde_release_complex"]["participant"]["protein_complex"][
                "active_units"
            ]
            next(u for u in units if u["id"] == "lold_unit")["function"]["term"][
                "id"
            ] = "GO:0005524"
        elif name == "carrier_compartment_wrong":
            anns["lola_carrier"]["locations"][0]["term"]["id"] = "GO:0005737"
        else:
            anns["classical_lolb_insertase"]["function"]["preferred_term"] = (
                "lipoprotein carrier activity"
            )
        assert not contract(mutated), name
        mutations.append({"mutation": name, "detected": True})
    proposals = []
    for rec in records.values():
        doc = yaml.safe_load((ROOT / rec["path"]).read_text())
        for proposal in doc.get("proposed_new_terms", []):
            if proposal["proposed_name"] == legacy.INSERTION:
                proposals.append(
                    {
                        "path": rec["path"],
                        "definition": proposal["proposed_definition"],
                        "parent": proposal["proposed_parent"],
                    }
                )
    assert len(proposals) == 5
    assert all(
        (p["definition"], p["parent"])
        == (proposals[0]["definition"], proposals[0]["parent"])
        for p in proposals
    )
    report = {
        "status": "PASS",
        "module_sha256": sha(MODULE),
        "original_checker_sha256": sha(OLD / "check_capacity.py"),
        "case_count": len(results),
        "cases": results,
        "additional_gate_sensitivities": sensitivities,
        "additional_declaration_mutations": mutations,
        "aligned_proposals": proposals,
        "original_outputs_unchanged": original_files,
        "limitations": [
            "Domain/location/source and function-contract gates are explicit external checks, not compiler features.",
            "Masking supported metadata is a methodological sensitivity test, not evidence of protein loss or inactivity.",
            "Inferred target compartments and carrier roles retain their source-qualified evidence tier; native flux is not inferred.",
        ],
    }
    (HERE / "integration-results.json").write_text(json.dumps(report, indent=2) + "\n")
    print(
        json.dumps(
            {
                "status": "PASS",
                "cases": len(results),
                "additional_sensitivities": len(sensitivities),
                "additional_mutations": len(mutations),
            }
        )
    )


if __name__ == "__main__":
    main()
