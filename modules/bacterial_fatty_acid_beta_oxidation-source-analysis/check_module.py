"""Check literature-bounded beta-oxidation realizations using the production circuit.

Family membership supplies a candidate, not an enzyme assignment. These witnesses
are limited to reviewed proteins, matched partners and the stated assay contexts.
They do not predict an arbitrary proteome or demonstrate unrestricted pathway flux.
"""

from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path

import yaml

from ai_gene_review.module_logic import compile_module, is_satisfied, iter_atoms

ROOT = Path(__file__).resolve().parents[2]
SLUG = "bacterial_fatty_acid_beta_oxidation"
AUDIT = ROOT / "analysis/module_audits" / SLUG
MODULE = ROOT / "modules" / (SLUG + ".yaml")
CONTRACT = AUDIT / "endpoint-contract.yaml"
ENTAILMENT = AUDIT / "go-entailment.json"
PROPOSED = "acyl-CoA dehydrogenase activity (acceptor unspecified)"
PARTS = {
    "bacterial_acyl_coa_dehydrogenation", "bacterial_enoyl_coa_hydration",
    "bacterial_hydroxyacyl_coa_oxidation", "bacterial_ketoacyl_coa_thiolysis",
}


def load(path):
    return yaml.safe_load(path.read_text())


def annotons(node):
    yield from node.get("annotons", [])
    for part in node.get("parts", []):
        yield from annotons(part["node"])
    for variants in node.get("variant_sets", []):
        for variant in variants["variants"]:
            yield from annotons(variant)


def structural_contract(module):
    parts = module["module"]["parts"]
    assert {p["node"]["id"] for p in parts} == PARTS
    assert all(not p.get("optional", False) for p in parts)
    leaves = {a["id"]: a for a in annotons(module["module"])}
    assert len(leaves) == 10
    for name in ["fade_acyl_coa_dehydrogenase_activity", "pao1_fade1_fade2", "bacillus_fade"]:
        function = leaves[name]["function"]
        assert not function.get("term"), "An unknown physiological acceptor acquired an ETF-specific GO assertion"
        assert function["preferred_term"] == PROPOSED
    return leaves


def documents(module):
    accessions = {acc for a in iter_atoms(compile_module(module)) for acc in a.uniprots}
    found = {}
    for organism in ["PSEPK", "ECOLI", "SALTY", "PSEFR", "MYCTU", "BACSU", "PSEAE"]:
        for path in (ROOT / "genes" / organism).glob("*/*-ai-review.yaml"):
            doc = load(path)
            if doc.get("id") in accessions:
                assert doc["id"] not in found
                assert doc.get("status") == "COMPLETE"
                assert all(r["review"]["action"] != "PENDING" for r in doc.get("existing_annotations", []))
                found[doc["id"]] = {"document": doc, "path": path}
    assert set(found) == accessions and len(found) == 19
    return found


def supported_terms(doc):
    terms = set()
    for row in doc.get("existing_annotations", []):
        if row.get("negated"):
            continue
        review = row["review"]
        if review["action"] in {"ACCEPT", "KEEP_AS_NON_CORE", "NEW"}:
            terms.add(row["term"]["id"])
        elif review["action"] == "MODIFY":
            terms.update(t["id"] for t in review.get("proposed_replacement_terms", []))
    for core in doc.get("core_functions", []):
        if core.get("molecular_function"):
            terms.add(core["molecular_function"]["id"])
    # A reviewed specific activity supports its ontology ancestors. Substrate
    # restrictions remain in the evidence profile; the ancestor does not erase them.
    for child, ancestors in json.loads(ENTAILMENT.read_text())["entailments"].items():
        if child in terms:
            terms.update(ancestors)
    return terms


def evaluate(case, module, contract, records):
    profile = contract["profiles"][case["profile"]]
    present = set(case.get("accessions", []))
    required = set(profile["roles"].values())
    if not required <= present or not required <= set(records):
        return "NOT_ESTABLISHED", "Exact source-supported proteins and compatible partners are required"
    if not set(profile["required_conditions"]) <= set(case.get("conditions", [])):
        return "NOT_ESTABLISHED", "Assay, substrate, partner or native-system context is missing"
    if case.get("requested_claim") != profile["claim"] or case.get("mutation"):
        return "NOT_ESTABLISHED", "The request exceeds the wild-type evidence scope"
    circuit = compile_module(module)
    atoms = {a.node_id: a for a in iter_atoms(circuit)}

    def holds(atom):
        acc = profile["roles"].get(atom.node_id)
        if acc not in present or acc not in atom.uniprots or acc not in records:
            return False
        doc = records[acc]["document"]
        if atom.function_ids:
            return set(atom.function_ids) <= supported_terms(doc)
        return any(core.get("proposed_molecular_function") == PROPOSED
                   for core in doc.get("core_functions", []))

    for name in profile["roles"]:
        if name not in atoms or not holds(atoms[name]):
            return "NOT_ESTABLISHED", "The actual module atom and reviewed molecular activity do not support this role"
    if profile["require_whole_module"] and not is_satisfied(circuit, holds):
        return "NOT_ESTABLISHED", "The production-compiled four-reaction circuit is not satisfied"
    return profile["level"], profile["claim"]


def run_cases(module, contract, records):
    result = []
    for case in contract["cases"]:
        observed, reason = evaluate(case, module, contract, records)
        result.append({"id": case["id"], "expected": case["expected"], "observed": observed,
                       "reason": reason, "pass": observed == case["expected"]})
    return result


def main():
    module, contract = load(MODULE), load(CONTRACT)
    structural_contract(module)
    records = documents(module)
    for profile in contract["profiles"].values():
        for ref in profile["source_ids"]:
            if ref.startswith("PMID:"):
                assert (ROOT / "publications" / (ref.replace(":", "_") + ".md")).exists(), ref
            elif ref.startswith("file:"):
                assert any((p / ref[5:]).exists() for p in [ROOT, ROOT / "genes"]), ref
    rows = run_cases(module, contract, records)
    assert all(r["pass"] for r in rows), [r for r in rows if not r["pass"]]
    mutations = []

    def mutation(name, changed_module=None, changed_records=None, changed_contract=None):
        altered = changed_module if changed_module is not None else module
        try:
            structural_contract(altered)
            tested = run_cases(altered, changed_contract or contract, changed_records or records)
            caught = any(not r["pass"] for r in tested)
        except (AssertionError, KeyError):
            caught = True
        mutations.append({"id": name, "detected": caught})
        assert caught, name

    for part in sorted(PARTS):
        changed = copy.deepcopy(module)
        next(p for p in changed["module"]["parts"] if p["node"]["id"] == part)["optional"] = True
        mutation("make_" + part + "_optional", changed_module=changed)
    changed = copy.deepcopy(module)
    leaf = next(a for a in annotons(changed["module"]) if a["id"] == "fade_acyl_coa_dehydrogenase_activity")
    leaf["function"]["term"] = {"id": "GO:0003995", "label": "acyl-CoA dehydrogenase activity"}
    mutation("invent_ETF_coupling", changed_module=changed)
    for acc in ["Q9I610", "O53871", "P28790"]:
        changed = copy.deepcopy(records)
        changed[acc]["document"]["core_functions"] = []
        for row in changed[acc]["document"].get("existing_annotations", []):
            row["review"] = {"action": "UNDECIDED"}
        mutation("remove_positive_activity_" + acc, changed_records=changed)
    for name in ["putida", "bacillus", "fragi_tfe", "mycobacterium_tfe"]:
        changed = copy.deepcopy(contract)
        changed["profiles"][name]["level"] = "AUTONOMOUS_COMPLETE_FLUX"
        mutation("upgrade_" + name + "_to_complete_flux", changed_contract=changed)
    result = {"status": "PASS", "scope": contract["scope"], "cases": rows, "mutation_checks": mutations,
              "module_sha256": hashlib.sha256(MODULE.read_bytes()).hexdigest(),
              "contract_sha256": hashlib.sha256(CONTRACT.read_bytes()).hexdigest(),
              "entailment_sha256": hashlib.sha256(ENTAILMENT.read_bytes()).hexdigest(),
              "gene_reviews": {a: {"path": str(r["path"].relative_to(ROOT)),
                                     "sha256": hashlib.sha256(r["path"].read_bytes()).hexdigest()}
                               for a, r in records.items()}}
    (AUDIT / "capacity-results.json").write_text(json.dumps(result, indent=2) + "\n")
    print(f"PASS: {len(rows)} source-scoped cases, {len(mutations)} mutations, {len(records)} complete reviews")


if __name__ == "__main__":
    main()
