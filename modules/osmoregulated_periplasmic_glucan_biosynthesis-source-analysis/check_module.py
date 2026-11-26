"""Evaluate the source-scoped OPG endpoints against the module and gene reviews.

This does not predict arbitrary proteomes. Unknown members, untested compatible
partners and unsupported product claims remain NOT_ESTABLISHED. The production
compiler supplies the actual module logic; the evidence profiles supply assay
context that the compiler deliberately does not model.
"""

from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path

import yaml

from ai_gene_review.module_logic import compile_module, is_satisfied, iter_atoms

ROOT = Path(__file__).resolve().parents[2]
SLUG = "osmoregulated_periplasmic_glucan_biosynthesis"
AUDIT = ROOT / "analysis/module_audits" / SLUG
MODULE = ROOT / "modules" / (SLUG + ".yaml")
CONTRACT = AUDIT / "endpoint-contract.yaml"
ENTAILMENT = AUDIT / "go-entailment.json"
SUPPORTED_ACTIONS = {"ACCEPT", "KEEP_AS_NON_CORE", "NEW"}
PROFILES = {
    "ecoli_native_opg": {
        "level": "SUPPORTED_NATIVE_PROCESS",
        "claim": "OPG formation in the E. coli system",
        "extra_atoms": ["ecoli_acp_compatible_factor"],
        "root": True,
    },
    "cers4_native_opg": {
        "level": "SUPPORTED_NATIVE_PROCESS",
        "claim": "OPG formation in strain 2.4.1",
        "extra_atoms": ["opgI_conditional_dependency"],
        "root": True,
    },
    "psepk_inferred_opg": {
        "level": "SUPPORTED_INFERENCE",
        "claim": "KT2440 OpgGH-associated pathway inference",
        "root": True,
    },
    "ecoli_opgD_hydrolysis": {
        "level": "SUPPORTED_IN_VITRO_REACTION",
        "claim": "supplied-substrate beta-1,2-glucan hydrolysis",
        "atom": "ecoli_opgD_hydrolysis",
        "molecular_function": "GO:0033913",
    },
    "ecoli_opgG_intrinsic_hydrolysis": {
        "level": "SUPPORTED_IN_VITRO_REACTION",
        "claim": "weak supplied-substrate beta-1,2-glucan hydrolysis",
        "review_only_activity": True,
        "molecular_function": "GO:0033913",
    },
    "xcc_opgD_cyclization": {
        "level": "SUPPORTED_IN_VITRO_REACTION",
        "claim": "supplied-substrate alpha-1,6 cyclization to DP16",
        "atom": "xcc_opgD_cyclization",
        "proposed_function": "alpha-1,6-cyclized beta-1,2-glucohexadecaose synthase activity",
    },
    "caulobacter_glucosyltransferase_inference": {
        "level": "SUPPORTED_INFERENCE",
        "claim": "Caulobacter glucosyltransferase activity inference",
        "atom": "caulobacter_opgH_comparator",
        "molecular_function": "GO:0046527",
    },
}


def load(path):
    return yaml.safe_load(path.read_text())


def documents(module):
    accessions = {acc for atom in iter_atoms(compile_module(module)) for acc in atom.uniprots}
    records = {}
    # Resolve only the audited species, then require exact accessions, never labels.
    for organism in ["ECOLI", "PSEPK", "CERS4", "CAUVN", "XANCP"]:
        for path in (ROOT / "genes" / organism).glob("*/*-ai-review.yaml"):
            doc = load(path)
            if doc.get("id") in accessions:
                assert doc["id"] not in records, doc["id"]
                assert doc.get("status") == "COMPLETE", path
                assert all(r.get("review", {}).get("action") != "PENDING"
                           for r in doc.get("existing_annotations", [])), path
                records[doc["id"]] = {"document": doc, "path": path}
    assert set(records) == accessions, accessions - set(records)
    return records


def positive_terms(doc, entailment):
    terms = set()
    for row in doc.get("existing_annotations", []):
        if row.get("negated"):
            continue
        review = row["review"]
        if review["action"] in SUPPORTED_ACTIONS:
            terms.add(row["term"]["id"])
        elif review["action"] == "MODIFY":
            terms.update(t["id"] for t in review.get("proposed_replacement_terms", []))
    for core in doc.get("core_functions", []):
        if core.get("molecular_function"):
            terms.add(core["molecular_function"]["id"])
        terms.update(t["id"] for t in core.get("directly_involved_in", []))
    for child, parents in entailment.items():
        if child in terms:
            terms.update(parents)
    return terms


def all_annotons(node):
    yield from node.get("annotons", [])
    for part in node.get("parts", []):
        yield from all_annotons(part["node"])
    for variants in node.get("variant_sets", []):
        for variant in variants.get("variants", []):
            yield from all_annotons(variant)


def module_contract(doc, records):
    """Check the actual biological distinctions that the endpoint oracle relies on."""
    anns = {a["id"]: a for a in all_annotons(doc["module"])}
    for name in ["opgG_glucan_biosynthesis_factor", "rhodobacter_opgG_factor"]:
        assert "function" not in anns[name], "Unresolved native OpgG chemistry became an asserted reaction"
    assert "processes" not in anns["caulobacter_opgH_comparator"], "Unresolved Caulobacter product became established OPG participation"
    assert "function" not in anns["opgI_conditional_dependency"], "Unknown OpgI role became an invented molecular function"
    xcc = anns["xcc_opgD_cyclization"]["function"]
    proposed = PROFILES["xcc_opgD_cyclization"]["proposed_function"]
    assert not xcc.get("term"), "Specific cyclase acquired an unsupported GO identifier"
    assert xcc["preferred_term"] == proposed
    assert any("fifteen beta-1,2" in p["preferred_term"] and "alpha-1,6" in p["preferred_term"]
               for p in xcc["products"]), "Cyclase product topology or size changed"
    review = records["Q8P3C6"]["document"]
    assert any(c.get("proposed_molecular_function") == proposed for c in review["core_functions"])
    assert any(p["proposed_name"] == proposed for p in review["proposed_new_terms"])
    assert any(m["term"]["id"] == "UniProtKB:Q9FA54"
               for m in anns["rhodobacter_opgG_factor"]["participant"]["family"]["representative_members"]), "Cyclic-product OpgGIH realization lost"
    return anns


def evaluate(case, module, contract, records, entailment, policies=PROFILES):
    name = case["profile"]
    profile = contract["profiles"][name]
    policy = policies[name]
    present = set(case.get("accessions", [])) - set(case.get("absent_accessions", []))
    required = set(profile["required_accessions"])
    if not required <= present:
        return "NOT_ESTABLISHED", "Missing a source-supported component; a family match is insufficient"
    if not set(profile.get("required_conditions", [])) <= set(case.get("conditions", [])):
        return "NOT_ESTABLISHED", "Required assay or native-system conditions are not established"
    requested = case.get("requested_claim", policy["claim"])
    if requested != policy["claim"]:
        return "NOT_ESTABLISHED", "Requested claim exceeds the evidence scope"
    if case.get("mutation"):
        return "NOT_ESTABLISHED", "Wild-type evidence is not assigned to an altered construct"
    if not required <= set(records):
        return "NOT_ESTABLISHED", "A required exact member lacks a completed review"
    terms = {acc: positive_terms(records[acc]["document"], entailment) for acc in required}
    if policy.get("molecular_function") and not all(
            policy["molecular_function"] in terms[a] for a in required):
        return "NOT_ESTABLISHED", "The reviewed molecular activity is not established"
    circuit = compile_module(module)
    atoms = {a.node_id: a for a in iter_atoms(circuit)}

    def holds(atom):
        # Restrict this evaluation to the profile's experimentally compatible or
        # explicitly inferred realization. Do not mix arbitrary species partners.
        candidates = required & present & set(atom.uniprots)
        return any(set(atom.function_ids) <= terms[acc] for acc in candidates)

    if policy.get("root") and not is_satisfied(circuit, holds):
        return "NOT_ESTABLISHED", "The actual compiled backbone module is not satisfied"
    for ident in policy.get("extra_atoms", []):
        if ident not in atoms or not holds(atoms[ident]):
            return "NOT_ESTABLISHED", "A conditional source-supported partner is absent"
    if policy.get("atom"):
        ident = policy["atom"]
        if ident not in atoms or not holds(atoms[ident]):
            return "NOT_ESTABLISHED", "The actual reaction/comparator annoton is unsupported"
    if policy.get("proposed_function"):
        for acc in required:
            cores = records[acc]["document"].get("core_functions", [])
            if not any(c.get("proposed_molecular_function") == policy["proposed_function"] for c in cores):
                return "NOT_ESTABLISHED", "Specific proposed activity is not supported by the gene review"
    return policy["level"], policy["claim"]


def run_cases(module, contract, records, entailment, policies=PROFILES):
    rows = []
    for case in contract["cases"]:
        observed, reason = evaluate(case, module, contract, records, entailment, policies)
        rows.append({"id": case["id"], "expected": case["expected"], "observed": observed,
                     "reason": reason, "pass": observed == case["expected"]})
    return rows


def main():
    module, contract = load(MODULE), load(CONTRACT)
    records = documents(module)
    entailment = json.loads(ENTAILMENT.read_text())["entailments"]
    module_contract(module, records)
    rows = run_cases(module, contract, records, entailment)
    assert all(r["pass"] for r in rows), [r for r in rows if not r["pass"]]
    mutations = []

    def check_mutation(name, changed_module=None, changed_contract=None, changed_policies=None):
        altered = changed_module if changed_module is not None else module
        try:
            module_contract(altered, records)
            tested = run_cases(altered, changed_contract or contract, records, entailment,
                               changed_policies or PROFILES)
            detected = any(not r["pass"] for r in tested)
        except (AssertionError, KeyError):
            detected = True
        mutations.append({"id": name, "detected": detected})
        assert detected, name

    mutated = copy.deepcopy(module)
    anns = {a["id"]: a for a in all_annotons(mutated["module"])}
    anns["opgG_glucan_biosynthesis_factor"]["function"] = {
        "term": {"id": "GO:0033913", "label": "glucan endo-1,2-beta-glucosidase activity"}}
    check_mutation("force_native_opgG_hydrolysis", changed_module=mutated)
    for part_id in ["rhodobacter_opgI_dependency", "ecoli_acp_dependency"]:
        mutated = copy.deepcopy(module)
        mutated["module"]["parts"] = [p for p in mutated["module"]["parts"] if p["node"]["id"] != part_id]
        check_mutation("delete_" + part_id, changed_module=mutated)
    mutated = copy.deepcopy(module)
    for part in mutated["module"]["parts"]:
        if part["node"]["id"] == "opgD_hydrolysis_step":
            part["optional"] = False
    check_mutation("make_opgD_universally_required", changed_module=mutated)
    mutated = copy.deepcopy(module)
    anns = {a["id"]: a for a in all_annotons(mutated["module"])}
    anns["xcc_opgD_cyclization"]["function"]["products"] = [{"preferred_term": "shorter linear chains"}]
    check_mutation("replace_cyclic_product_with_linear_product", changed_module=mutated)
    mutated = copy.deepcopy(module)
    for part in mutated["module"]["parts"]:
        if part["node"]["id"] == "opgG_periplasmic_glucan_biosynthesis_step":
            part["node"]["variant_sets"][0]["variants"].pop()
    check_mutation("exclude_cyclic_opgGIH_realization", changed_module=mutated)
    policies = copy.deepcopy(PROFILES)
    policies["cers4_native_opg"]["claim"] = "exact_2_4_1_DP18_alpha_1_6_closed_product"
    check_mutation("conflate_ws8_product_and_2_4_1_genetics", changed_policies=policies)
    policies = copy.deepcopy(PROFILES)
    policies["psepk_inferred_opg"]["level"] = "SUPPORTED_NATIVE_PROCESS"
    check_mutation("upgrade_homology_to_native_measurement", changed_policies=policies)
    for profile in ["ecoli_opgD_hydrolysis", "xcc_opgD_cyclization"]:
        policies = copy.deepcopy(PROFILES)
        policies[profile]["level"] = "SUPPORTED_NATIVE_PROCESS"
        check_mutation("upgrade_" + profile + "_to_native_pathway", changed_policies=policies)
    result = {"status": "PASS", "scope": "Audited exemplars and named evidence contexts only",
              "cases": rows, "mutation_checks": mutations,
              "gene_reviews": {a: {"path": str(v["path"].relative_to(ROOT)),
                                    "sha256": hashlib.sha256(v["path"].read_bytes()).hexdigest()}
                               for a, v in records.items()},
              "module_sha256": hashlib.sha256(MODULE.read_bytes()).hexdigest(),
              "contract_sha256": hashlib.sha256(CONTRACT.read_bytes()).hexdigest()}
    (AUDIT / "capacity-results.json").write_text(json.dumps(result, indent=2) + "\n")
    print(f"PASS: {len(rows)} endpoint cases, {len(mutations)} discriminating mutations, {len(records)} completed member reviews")


if __name__ == "__main__":
    main()
