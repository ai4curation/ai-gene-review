"""Additive PR6184 capacity regression; published cases and receipts remain immutable."""

import copy
import hashlib
import importlib.util
import json
import sys
from pathlib import Path

import yaml

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
BASE = HERE.parents[1]
ROOT = BASE.parents[2]
OLD = BASE / "capacity-consultation"
spec = importlib.util.spec_from_file_location(
    "published_lipoprotein_capacity", OLD / "check_capacity.py"
)
legacy = importlib.util.module_from_spec(spec)
spec.loader.exec_module(legacy)
EXPECTED_MODULE = "0baadae89cee21b3824638eeba6a8caa4aab6e33b82982c39d3ef4025b170961"


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


class Round1Oracle(legacy.Oracle):
    def match(self, participant, accession):
        if participant["selector_type"] == "GENE_PRODUCT":
            selected = participant["gene_product"]["term"]["id"].split(":", 1)[1]
            # A mutation deliberately undoes the exact selector; this is not production policy.
            if selected == "P54392" and self.policy in {
                "universal_lhat",
                "drop_exact_lhat",
            }:
                return "PANTHER:PTHR40042" in self.catalog[accession]["families"]
            return selected == accession
        return super().match(participant, accession)


def evaluate(doc, catalog, case, policy="strict"):
    records = copy.deepcopy(catalog)
    for acc, overrides in case.get("catalog_overrides", {}).items():
        for field, value in overrides.items():
            records[acc][field] = (
                set(value) if field in {"enables", "contributes", "families"} else value
            )
    oracle = Round1Oracle(doc, records, case, policy)
    nodes = {n["id"]: n for n in legacy.walk(doc["module"]) if "module_type" in n}
    circuit = legacy.compile_node(doc["module"], ROOT / "modules")
    result = {"module": legacy.is_satisfied(circuit, oracle)}
    for short, node in legacy.ROUTES.items():
        result[short] = legacy.is_satisfied(
            legacy.compile_node(nodes[node], ROOT / "modules"), oracle
        )
    products = {
        "three_long_acyl_chains"
        if policy == "collapse_products"
        else legacy.PRODUCTS[r]
        for r in legacy.ROUTES
        if result[r]
    }
    result["terminal_products"] = sorted(products)
    result["complete_products"] = sorted(products) if result["module"] else []
    return result


def extra_cases(catalog):
    catalog["fixture:reviewed_generic_acetylase"] = {
        "taxon": 224308,
        "families": {"PANTHER:PTHR40042", "PANTHER:PTHR40042:SF1"},
        "enables": {"GO:0008080"},
        "contributes": set(),
        "qualified": True,
        "scope": "Synthetic reviewed generic activity; not evidence of the exact LhaT substrate reaction.",
    }
    catalog["fixture:inactive_Ba_preparation"] = {
        "taxon": 1392,
        "families": {"PANTHER:PTHR40042"},
        "enables": {"GO:0008080"},
        "contributes": set(),
        "qualified": False,
        "scope": "Negative preparation context from PMID40626731; synthetic identifier/family challenge, no invented accession or PAINT placement.",
    }
    template = {
        "panel_taxon": 224308,
        "mode": "native",
        "mature_diacyllipoprotein": True,
        "precursor": True,
        "pg_for_lgt": True,
        "acetylated_lipid_carrier": True,
        "donor_accessible": True,
        "expected": {"lhat": False},
    }
    cases = []
    for name, proteins, overrides in [
        (
            "round1_generic_family_and_reviewed_8080_not_exact_lhat",
            ["fixture:reviewed_generic_acetylase"],
            {},
        ),
        ("round1_missing_exact_lhat_target", ["O34752", "Q45479"], {}),
        (
            "round1_exact_target_without_reviewed_activity",
            ["P54392"],
            {"catalog_overrides": {"P54392": {"enables": []}}},
        ),
        (
            "round1_inactive_homolog_preparation_not_positive",
            ["fixture:inactive_Ba_preparation"],
            {"panel_taxon": 1392},
        ),
    ]:
        case = copy.deepcopy(template)
        case.update({"name": name, "proteins": proteins, **overrides})
        cases.append(case)
    return cases


def main():
    assert sha(legacy.MODULE) == EXPECTED_MODULE
    doc = yaml.safe_load(legacy.MODULE.read_text())
    catalog, closure, source_hashes = legacy.load_members()
    published_cases = json.loads((OLD / "cases.json").read_text())
    published_results = json.loads((OLD / "results.json").read_text())
    assert len(published_cases) == len(published_results["cases"]) == 35
    assert len(published_results["mutations"]) == 10
    assert [c["name"] for c in published_cases] == [
        c["name"] for c in published_results["cases"]
    ]
    cases = published_cases + extra_cases(catalog)
    circuit = legacy.compile_node(doc["module"], ROOT / "modules")
    assert {a.node_id for a in legacy.core_atoms(circuit)} == legacy.CORE
    atoms = list(legacy.iter_atoms(circuit))
    assert len(atoms) == 7
    lhat = next(a for a in atoms if a.node_id == "lhat_n_acetyltransferase")
    assert set(lhat.uniprots) == {"P54392"} and not lhat.family_ids
    selected = {
        m["term"]["id"].split(":", 1)[1]
        for n in legacy.walk(doc["module"])
        for m in n.get("representative_members", [])
    }
    selected.update(
        n["gene_product"]["term"]["id"].split(":", 1)[1]
        for n in legacy.walk(doc["module"])
        if n.get("selector_type") == "GENE_PRODUCT"
    )
    assert selected == set(legacy.MEMBERS)
    for node in legacy.walk(doc["module"]):
        if node.get("id") in {
            "lnt_n_acyltransferase",
            "lnb_n_acyltransferase",
            "lnsab_n_acyltransferase",
            "lhat_n_acetyltransferase",
        }:
            assert "GO:0042160" in {p["term"]["id"] for p in node["processes"]}
    results = []
    for index, case in enumerate(cases):
        actual = evaluate(doc, catalog, case)
        assert not legacy.compare(case["expected"], actual), (case["name"], actual)
        if index < 35:
            assert actual == published_results["cases"][index]["capacity"], case["name"]
        results.append(
            {
                "name": case["name"],
                "result": "PASS",
                "capacity": actual,
                "historical_case": index < 35,
                "meaning": "Evidence-qualified capacity; false is not a universal biological absence claim.",
            }
        )
    mutations = []
    policies = [
        "drop_partner_gate",
        "ignore_compatibility",
        "universal_lhat",
        "ignore_donors",
        "collapse_products",
        "force_lnb_pg",
        "go_only",
        "ignore_taxon",
    ]
    for policy in policies:
        killed = [
            c["name"]
            for c in published_cases
            if legacy.compare(c["expected"], evaluate(doc, catalog, c, policy))
        ]
        assert killed, policy
        mutations.append(
            {
                "mutation": policy,
                "historical": True,
                "detected_by": killed,
                "note": "universal_lhat deliberately restores broad family matching and removes activity qualification"
                if policy == "universal_lhat"
                else "Original biological violation retained",
            }
        )
    forced = copy.deepcopy(doc)
    lnt_node = next(
        n for n in legacy.walk(doc["module"]) if n.get("id") == legacy.ROUTES["lnt"]
    )
    forced["module"]["parts"].append({"order": 4, "node": copy.deepcopy(lnt_node)})
    killed = [
        c["name"]
        for c in published_cases
        if legacy.compare(c["expected"], evaluate(forced, catalog, c))
    ]
    assert killed
    mutations.append(
        {"mutation": "force_lnt_required", "historical": True, "detected_by": killed}
    )
    erased = copy.deepcopy(doc)
    unit_parent = next(n for n in legacy.walk(erased) if "active_units" in n)
    unit_parent["active_units"] = unit_parent["active_units"][:1]
    try:
        evaluate(
            erased,
            catalog,
            next(c for c in published_cases if c["name"] == "lnsa_alone"),
        )
    except AssertionError as error:
        assert "partner requirement erased" in str(error)
        mutations.append(
            {
                "mutation": "erase_lnsb_active_unit",
                "historical": True,
                "detected_by": [str(error)],
            }
        )
    else:
        raise AssertionError("Partner erasure survived")
    killed = [
        c["name"]
        for c in cases
        if legacy.compare(c["expected"], evaluate(doc, catalog, c, "drop_exact_lhat"))
    ]
    assert "round1_generic_family_and_reviewed_8080_not_exact_lhat" in killed
    mutations.append(
        {"mutation": "drop_exact_lhat", "historical": False, "detected_by": killed}
    )
    assert sum(m["historical"] for m in mutations) == 10
    for ref in legacy.refs_in(doc):
        path = legacy.resolve(ref)
        source_hashes[str(path.relative_to(ROOT))] = sha(path)
    for path in [
        legacy.MODULE,
        OLD / "check_capacity.py",
        OLD / "cases.json",
        OLD / "results.json",
        ROOT / "src/ai_gene_review/module_logic.py",
        BASE / "lnsab-consultation/pairing-evidence.json",
    ]:
        source_hashes[str(path.relative_to(ROOT))] = sha(path)
    for filename, value in closure.items():
        assert value["active_proposals"] == value["proposal_rows_present"], filename
    assert sum(m["ordered_rows"] for m in closure.values()) == 88
    assert sum(m["active_proposals"] for m in closure.values()) == 16
    (HERE / "member-closure.json").write_text(json.dumps(closure, indent=2) + "\n")
    (HERE / "source-hashes.json").write_text(json.dumps(source_hashes, indent=2) + "\n")
    (HERE / "additional-cases.json").write_text(json.dumps(cases[35:], indent=2) + "\n")
    result = {
        "result": "PASS",
        "module_sha256": sha(legacy.MODULE),
        "cases": results,
        "mutations": mutations,
        "historical_cases_exact_outcomes_preserved": 35,
        "historical_mutations_detected": 10,
        "new_cases": 4,
        "new_mutations": 1,
        "members": len(closure),
        "ordered_rows": 88,
        "active_historical_NEW": 16,
        "production_atoms": [
            {
                "id": a.node_id,
                "members": a.uniprots,
                "families": a.family_ids,
                "functions": a.function_ids,
            }
            for a in atoms
        ],
        "limits": "The production compiler does not encode donor availability, native flux, pairing compatibility, or activity qualification; the external source-bound oracle does. GO0042160 is validated context, not a new catalytic gate. All original tests and full result vectors retained; no old output rewritten.",
        "full_corpus_validation": False,
    }
    (HERE / "results.json").write_text(json.dumps(result, indent=2) + "\n")
    print(
        json.dumps(
            {
                "result": "PASS",
                "cases": len(results),
                "mutations": len(mutations),
                "members": len(closure),
            }
        )
    )


if __name__ == "__main__":
    main()
