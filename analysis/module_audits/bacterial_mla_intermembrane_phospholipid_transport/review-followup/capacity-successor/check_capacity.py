"""Production-circuit evaluation with explicit source-grounded biological gates."""

from pathlib import Path
import collections
import copy
import hashlib
import json
import re
import yaml
from ai_gene_review.module_logic import (
    compile_node,
    core_atoms,
    enumerate_routes,
    is_satisfied,
    iter_atoms,
)

A = Path(__file__).resolve().parent
ROOT = A.parents[4]
MODULE = ROOT / "modules/bacterial_mla_intermembrane_phospholipid_transport.yaml"
BIO = yaml.safe_load((A / "biology.yaml").read_text())
TEST = yaml.safe_load((A / "cases.yaml").read_text())
INPUTS = {
    MODULE,
    A / "biology.yaml",
    A / "cases.yaml",
    Path(__file__).resolve(),
    ROOT / "src/ai_gene_review/module_logic.py",
}


def read(path):
    p = ROOT / path
    INPUTS.add(p)
    return yaml.safe_load(p.read_text())


def walk(node):
    yield node
    for part in node.get("parts", []):
        yield from walk(part["node"])
    for vs in node.get("variant_sets", []):
        for variant in vs.get("variants", []):
            yield from walk(variant)


def annotations(doc):
    return {a["id"]: a for n in walk(doc["module"]) for a in n.get("annotons", [])}


def actual_units(annoton):
    p = annoton["participant"]
    if p["selector_type"] == "PROTEIN_COMPLEX":
        return p["protein_complex"].get("active_units", [])
    return [
        {"id": "carrier", "participant": p, "function": annoton.get("function", {})}
    ]


def family_ids(participant):
    f = participant.get("family", {})
    return {
        x["id"] for x in [f.get("term", {})] + f.get("family_terms", []) if x.get("id")
    }


def representative_ids(participant):
    f = participant.get("family", {})
    return {
        x["term"]["id"].removeprefix("UniProtKB:")
        for x in f.get("representative_members", [])
    }


def source_check():
    for item in BIO["sources"].values():
        p = ROOT / item["path"]
        INPUTS.add(p)
        text = p.read_text()
        if item.get("quote"):
            assert re.sub(r"\s+", " ", item["quote"]) in re.sub(r"\s+", " ", text), (
                item["path"]
            )


def members():
    result = {}
    for panel, profile in BIO["panels"].items():
        for role, path in profile["roles"].items():
            d = read(path)
            raw = ROOT / Path(path).with_name(
                Path(path).name.replace("-ai-review.yaml", "-uniprot.txt")
            )
            INPUTS.add(raw)
            text = raw.read_text()
            if profile.get("reference_loci"):
                assert "OrderedLocusNames=" + profile["reference_loci"][role] in text, (
                    path
                )
            assert re.search(r"^AC\s+" + re.escape(d["id"]) + r";", text, re.M), path
            ids = set(re.findall(r"^DR\s+PANTHER; (PTHR\d+(?::SF\d+)?);", text, re.M))
            # The original Q88P90 record is immutable and lacks its current classification.
            # Consult the independently archived current official UniProt snapshot instead.
            extra = (
                ROOT
                / f"analysis/module_audits/bacterial_mla_intermembrane_phospholipid_transport/family-consultation/{d['id']}-uniprot.json"
            )
            if extra.is_file():
                e = json.loads(extra.read_text())
                INPUTS.add(extra)
                if e.get("primaryAccession") == d["id"]:
                    ids |= {
                        x["id"]
                        for x in e.get("uniProtKBCrossReferences", [])
                        if x["database"] == "PANTHER"
                    }
            assert d["status"] == "COMPLETE", path
            assert d["taxon"]["id"] == profile["taxon"], (panel, d["taxon"])
            result[d["id"]] = {
                "accession": d["id"],
                "panel": panel,
                "role": role,
                "review": d,
                "path": path,
                "families": {"PANTHER:" + x for x in ids},
                "sources": list(profile["sources"]),
                "masks": set(),
            }
    return result


def carrier_binding_satisfies(asserted_terms):
    """Use only frozen official is_a ancestors for the carrier binding requirement.

    Unknown terms receive no inferred ancestry. This does not relax transport,
    native-panel, source, identity, location, partner or assembly requirements.
    """
    ancestors = {"GO:0005543": {"GO:0005543"}}
    definitions_path = A / "binding-terms.json"
    INPUTS.add(definitions_path)
    definitions = {
        item["id"]: item for item in json.loads(definitions_path.read_text())["results"]
    }
    assert all(not item["isObsolete"] for item in definitions.values())
    assert {"id": "GO:0008429", "relation": "is_a"} in definitions["GO:0005543"][
        "children"
    ]
    for name, expected_id in [
        ("pe-binding-ancestors.json", "GO:0008429"),
        ("lipid-binding-ancestors.json", "GO:0008289"),
    ]:
        path = A / name
        INPUTS.add(path)
        records = json.loads(path.read_text())["results"]
        assert len(records) == 1 and records[0]["id"] == expected_id
        assert not records[0]["isObsolete"]
        ancestors[expected_id] = set(records[0]["ancestors"])
    assert "GO:0005543" in ancestors["GO:0008429"]
    assert "GO:0005543" not in ancestors["GO:0008289"]
    return any("GO:0005543" in ancestors.get(term, {term}) for term in asserted_terms)


def core_activity(member, role):
    cores = member["review"].get("core_functions", [])
    mf = {c.get("molecular_function", {}).get("id") for c in cores}
    contribution = {
        c.get("contributes_to_molecular_function", {}).get("id") for c in cores
    }
    location = {x["id"] for c in cores for x in c.get("locations", [])}
    bp = {x["id"] for c in cores for x in c.get("directly_involved_in", [])}
    rule = BIO["requirements"]["role_activity"][role]
    if rule.get("molecular_function") and rule["molecular_function"] not in mf:
        return False
    if rule.get("qualified_transfer") and "GO:0120014" not in mf | contribution:
        return False
    if rule.get("carrier"):
        if not (
            "GO:0120014" in mf or (carrier_binding_satisfies(mf) and "GO:0120010" in bp)
        ):
            return False
    if rule.get("structural_or_transfer_contribution"):
        structural = (
            any(
                c.get("in_complex", {}).get("id") == "GO:0043190"
                and c.get("supported_by")
                for c in cores
            )
            and "GO:0120010" in bp
        )
        if "GO:0120014" not in mf | contribution and not structural:
            return False
    return not rule.get("location") or rule["location"] in location


def case_members(case, bank):
    selected = [copy.deepcopy(x) for x in bank.values() if x["panel"] == case["panel"]]
    selected = [x for x in selected if x["role"] not in case.get("remove_roles", [])]
    if case.get("keep_roles"):
        selected = [x for x in selected if x["role"] in case["keep_roles"]]
    if case.get("replace"):
        r = case["replace"]
        selected = [x for x in selected if x["role"] != r["role"]]
        selected += [
            copy.deepcopy(x)
            for x in bank.values()
            if x["panel"] == r["donor_panel"] and x["role"] == r["role"]
        ]
    for m in selected:
        masks = case.get("mask", {})
        m["masks"] = set(masks.get("all", [])) | set(masks.get(m["role"], []))
        if "function" in m["masks"]:
            m["review"]["core_functions"] = []
        if "source" in m["masks"]:
            m["sources"] = []
        if "role" in m["masks"]:
            m["role"] = None
        if "identity" in m["masks"]:
            m["accession"] = "MASKED_IDENTITY"
        if "family" in m["masks"]:
            m["families"] = set()
    return selected


def evaluate(doc, case, bank, bypass=()):
    annotons = annotations(doc)
    circuit = compile_node(doc["module"], ROOT / "modules")
    selected = case_members(case, bank)
    context = set(BIO["requirements"]["contexts"]) | {"assembly_support"}
    context -= set(case.get("remove_context", []))
    failures = collections.defaultdict(set)
    hits = {}

    def fail(atom, reason):
        failures[atom].add(reason)
        return False

    def unit_ok(member, unit, role, atom):
        p = unit["participant"]
        if "identity" not in bypass and (
            member["accession"] not in representative_ids(p)
        ):
            return fail(atom, "member_identity")
        if "family" not in bypass and not family_ids(p).issubset(member["families"]):
            return fail(atom, "family_identity")
        if "role" not in bypass and (member["role"] != role):
            return fail(atom, "source_role")
        if "source" not in bypass and (
            not member["sources"]
            or any(s not in BIO["sources"] for s in member["sources"])
        ):
            return fail(atom, "source_support")
        if "function" not in bypass and (not core_activity(member, role)):
            return fail(atom, "reviewed_activity")
        if "function" not in bypass:
            declared = unit.get("function", {}).get("term", {}).get("id")
            if declared:
                supported = {
                    c.get(slot, {}).get("id")
                    for c in member["review"].get("core_functions", [])
                    for slot in [
                        "molecular_function",
                        "contributes_to_molecular_function",
                    ]
                }
                # Only the carrier phospholipid-binding requirement gains
                # verified subclass entailment; other unit terms stay exact.
                carrier_refinement = (
                    role == "C"
                    and declared == "GO:0005543"
                    and carrier_binding_satisfies(supported)
                )
                if declared not in supported and not carrier_refinement:
                    return fail(atom, "declared_unit_activity")
        if "matched_panel" not in bypass and member["panel"] != case["panel"]:
            return fail(atom, "matched_panel")
        return True

    def holds(atom):
        aid = atom.node_id
        if "context" not in bypass:
            absent = set(BIO["requirements"]["contexts"]) - context
            if absent:
                return fail(aid, "context:" + ",".join(sorted(absent)))
        profile = BIO["requirements"]["route_profiles"][aid]
        if profile in {"with_B", "without_identifiable_B"} and "assembly" not in bypass:
            if "assembly_support" not in context:
                return fail(aid, "assembly_evidence")
            if BIO["panels"][case["panel"]]["assembly"] != profile:
                return fail(aid, "assembly_context")
        expected_activity = BIO["requirements"]["declared_activities"]["annotons"][
            profile
        ]
        if (
            annotons[aid].get("function", {}).get("term", {}).get("id")
            != expected_activity
        ):
            return fail(aid, "declared_annoton_activity")
        required_location = BIO["requirements"]["declared_locations"][profile]
        declared_locations = {
            x.get("term", {}).get("id") for x in annotons[aid].get("locations", [])
        }
        if required_location not in declared_locations:
            return fail(aid, "declared_annoton_compartment")
        units = actual_units(annotons[aid])
        witnesses = []
        for unit in units:
            role = (
                "C"
                if unit["id"] == "carrier"
                else BIO["requirements"]["module_units"].get(unit["id"])
            )
            if role is None:
                return fail(aid, "unmapped_unit")
            matches = [m for m in selected if unit_ok(m, unit, role, aid)]
            if not matches:
                return fail(aid, "missing_role:" + role)
            witnesses.append(
                {"unit": unit["id"], "role": role, "member": matches[0]["accession"]}
            )
        hits[aid] = witnesses
        return True

    truth = {atom.node_id: holds(atom) for atom in iter_atoms(circuit)}
    answer = is_satisfied(circuit, lambda a: truth[a.node_id])
    return {
        "id": case["id"],
        "capacity": answer,
        "atom_truth": truth,
        "witnesses": hits,
        "failures": {k: sorted(v) for k, v in failures.items() if not truth.get(k)},
        "evidence_tier": BIO["panels"][case["panel"]]["evidence_tier"],
        "native_flux_claim": False,
        "conditional_comparator": case.get("conditional_context"),
    }


def structural_contract(doc):
    problems = []
    a = annotations(doc)
    expected = BIO["requirements"]["annoton_roles"]
    if set(a) != set(expected):
        problems.append(
            "outer/carrier/assembly atom inventory disagrees with independent source profile"
        )
    for aid in sorted(set(a) & set(expected)):
        profile = BIO["requirements"]["route_profiles"][aid]
        declared = a[aid].get("function", {}).get("term", {}).get("id")
        if declared != BIO["requirements"]["declared_activities"]["annotons"][profile]:
            problems.append(
                aid + ": unsupported or missing declared molecular function"
            )
        required_location = BIO["requirements"]["declared_locations"][profile]
        if required_location not in {
            x.get("term", {}).get("id") for x in a[aid].get("locations", [])
        }:
            problems.append(aid + ": unsupported declared compartment")
        for unit in actual_units(a[aid]):
            role = BIO["requirements"]["module_units"].get(unit["id"])
            required = BIO["requirements"]["declared_activities"]["units"].get(role)
            if (
                required
                and unit.get("function", {}).get("term", {}).get("id") != required
            ):
                problems.append(
                    unit["id"] + ": missing or incorrect catalytic/interface function"
                )
        roles = [
            "C"
            if u["id"] == "carrier"
            else BIO["requirements"]["module_units"].get(u["id"])
            for u in actual_units(a[aid])
        ]
        if sorted(roles, key=str) != sorted(expected[aid]):
            problems.append(
                aid + ": active-unit roles disagree with source-supported assembly"
            )
    routes = [
        {x.node_id for x in r} for r in enumerate_routes(compile_node(doc["module"]))
    ]
    for route in routes:
        roles = set().union(*(set(expected.get(x, [])) for x in route))
        if not set(BIO["requirements"]["complete_roles"]).issubset(roles):
            problems.append("a route omits a required interface or catalytic role")
        if (
            sum(
                x in route
                for x in [
                    "mlafedb_phospholipid_transporter",
                    "mlafed_b_independent_phospholipid_transporter",
                ]
            )
            != 1
        ):
            problems.append(
                "route does not represent one supported assembly architecture"
            )
    return problems


def all_cases():
    cases = copy.deepcopy(TEST["cases"])
    for panel in TEST["matrices"]["missing_roles"]["panels"]:
        for role in TEST["matrices"]["missing_roles"]["roles"]:
            cases.append(
                {
                    "id": f"missing_{panel}_{role}",
                    "panel": panel,
                    "remove_roles": [role],
                    "expected": False,
                }
            )
    for gate in TEST["matrices"]["masks"]["gates"]:
        for role in TEST["matrices"]["masks"]["roles"]:
            cases.append(
                {
                    "id": f"mask_{gate}_{role}",
                    "panel": "ECOLI",
                    "mask": {role: [gate]},
                    "expected": False,
                }
            )
    return cases


def mutate(doc, spec):
    d = copy.deepcopy(doc)
    root = d["module"]
    operation = spec["operation"]
    if operation == "remove_part":
        root["parts"] = [p for p in root["parts"] if p["order"] != spec["part_order"]]
    elif operation == "optional_part":
        next(p for p in root["parts"] if p["order"] == spec["part_order"])[
            "optional"
        ] = True
    elif operation in {"remove_unit", "family"}:
        for a in annotations(d).values():
            for u in list(actual_units(a)):
                if u["id"] == spec["unit"]:
                    if operation == "remove_unit":
                        a["participant"]["protein_complex"]["active_units"].remove(u)
                    else:
                        u["participant"]["family"]["term"]["id"] = spec["replacement"]
    elif operation == "unit_function":
        for a in annotations(d).values():
            for unit in actual_units(a):
                if unit["id"] == spec["unit"]:
                    unit["function"]["term"]["id"] = spec["replacement"]
    elif operation == "annoton_function":
        annoton = annotations(d)[spec["annoton"]]
        if spec["replacement"] is None:
            annoton.pop("function", None)
        else:
            annoton["function"]["term"]["id"] = spec["replacement"]
    elif operation == "annoton_location":
        annotations(d)[spec["annoton"]]["locations"][0]["term"]["id"] = spec[
            "replacement"
        ]
    elif operation == "force_B":
        a = annotations(d)
        b = copy.deepcopy(
            next(
                u
                for u in actual_units(a["mlafedb_phospholipid_transporter"])
                if u["id"] == "mlab_accessory_unit"
            )
        )
        a["mlafed_b_independent_phospholipid_transporter"]["participant"][
            "protein_complex"
        ]["active_units"].append(b)
    elif operation == "optional_variants":
        for n in walk(root):
            for v in n.get("variant_sets", []):
                v["selection"] = "ZERO_OR_MORE"
    elif operation == "conjoin_variants":
        for n in list(walk(root)):
            if n.get("variant_sets"):
                branches = n.pop("variant_sets")[0]["variants"]
                n["parts"] = [
                    {"order": i + 1, "node": x} for i, x in enumerate(branches)
                ]
    return d


def broad_family_controls(doc, bank):
    fixture = read(str((A / "family-controls.yaml").relative_to(ROOT)))
    evidence = read(fixture["source"])
    controls = []
    for control in fixture["controls"]:
        family = control["family"].removeprefix("PANTHER:").split(":")[0]
        if control.get("official_source"):
            raw = ROOT / control["official_source"]
            INPUTS.add(raw)
            text = raw.read_text()
            assert "AC   " + control["accession"] + ";" in text
            assert control["family"].removeprefix("PANTHER:") in text
            assert control["shared_domain"] in text
        else:
            entries = [
                e
                for e in evidence[family]["reference_leaves"]
                if e["uniprot"] == control["accession"]
            ]
            assert entries and any(
                "PANTHER:" + e["subfamily"] == control["family"] for e in entries
            ), control
        units = [
            u
            for a in annotations(doc).values()
            for u in actual_units(a)
            if BIO["requirements"]["module_units"].get(u["id"]) == control["role"]
        ]
        matches = any(control["family"] in family_ids(u["participant"]) for u in units)
        assert matches == control["expected_selector_match"]
        assert control["accession"] not in bank
        # Give the unrelated protein the tested role's complete reviewed activity as
        # an adversarial assumption. Identity/source/cognate-system evidence still matters.
        altered = copy.deepcopy(bank)
        target = next(
            k
            for k, v in altered.items()
            if v["panel"] == "ECOLI" and v["role"] == control["role"]
        )
        altered[target]["accession"] = control["accession"]
        altered[target]["families"] = {control["family"]}
        altered[target]["sources"] = []
        result = evaluate(
            doc, {"id": "substitute_" + control["accession"], "panel": "ECOLI"}, altered
        )
        assert not result["capacity"]
        controls.append(
            {
                **control,
                "observed_selector_match": matches,
                "exact_profile_capacity": False,
                "inherited_activity_assumed_for_challenge": True,
                "reason": "No exact matched representative/role/source interface license; not an assertion of absent secondary lipid activity.",
            }
        )
    return controls


def main():
    source_check()
    doc = yaml.safe_load(MODULE.read_text())
    bank = members()
    assert len(bank) == 18
    assert not structural_contract(doc), structural_contract(doc)
    cases = all_cases()
    byid = {x["id"]: x for x in cases}
    results = []
    for case in cases:
        result = evaluate(doc, case, bank)
        assert result["capacity"] == case["expected"], (case["id"], result)
        reasons = {x for failures in result["failures"].values() for x in failures}
        if case.get("remove_roles") and not case.get("conditional_context"):
            assert any(
                "missing_role:" + role in reasons for role in case["remove_roles"]
            ), (case["id"], reasons)
        if case.get("reason") in {"matched_panel", "member_identity"}:
            assert case["reason"] in reasons, (case["id"], reasons)
        if case.get("conditional_context"):
            assert case["conditional_context"] in BIO["conditional_comparators"]
            assert not BIO["conditional_comparators"][case["conditional_context"]][
                "encoded_positive"
            ]
        if case.get("remove_context"):
            assert any(
                x.startswith("context:") or x == "assembly_evidence" for x in reasons
            ), (case["id"], reasons)
        result["expected_capacity_checked"] = True
        result["specific_failure_reason_checked"] = bool(
            case.get("remove_roles")
            or case.get("reason") in {"matched_panel", "member_identity"}
            or case.get("remove_context")
        )
        results.append(result)
    mutations = []
    for spec in TEST["structural_mutations"]:
        variant = mutate(doc, spec)
        problems = structural_contract(variant)
        before = evaluate(doc, byid[spec["witness"]], bank)["capacity"]
        after = evaluate(variant, byid[spec["witness"]], bank)["capacity"]
        assert problems or before != after, spec["id"]
        mutations.append(
            {
                "id": spec["id"],
                "witness": spec["witness"],
                "original_capacity": before,
                "mutated_capacity": after,
                "contract_problems": problems,
                "detected": True,
            }
        )
    sensitivity = []
    for gate in ["source", "role", "function", "identity"]:
        case = byid[f"mask_{gate}_F"]
        assert not evaluate(doc, case, bank)["capacity"]
        value = evaluate(doc, case, bank, bypass=[gate])["capacity"]
        assert value, gate
        sensitivity.append(
            {"gate": gate, "witness": case["id"], "normal": False, "bypassed": value}
        )
    for gate, cid in [
        ("context", "ATPase_gene_without_ATP"),
        ("context", "absent_cargo"),
        ("context", "absent_compatible_interfaces"),
        ("context", "wrong_compartment_context"),
        ("context", "non_diderm_context"),
        ("assembly", "assembly_without_context"),
    ]:
        value = evaluate(doc, byid[cid], bank, bypass=[gate])["capacity"]
        assert value, (gate, cid)
        sensitivity.append(
            {"gate": gate, "witness": cid, "normal": False, "bypassed": value}
        )
    for gate, cid in [("matched_panel", "cross_panel_carrier")]:
        value = evaluate(doc, byid[cid], bank, bypass=[gate])["capacity"]
        assert value, (gate, cid)
        sensitivity.append(
            {"gate": gate, "witness": cid, "normal": False, "bypassed": value}
        )
    family_case = {
        "id": "masked_actual_family",
        "panel": "ECOLI",
        "mask": {"F": ["family"]},
    }
    assert not evaluate(doc, family_case, bank)["capacity"]
    assert evaluate(doc, family_case, bank, bypass=["family"])["capacity"]
    sensitivity.append(
        {
            "gate": "family",
            "witness": family_case["id"],
            "normal": False,
            "bypassed": True,
        }
    )
    controls = broad_family_controls(doc, bank)
    circuit = compile_node(doc["module"])
    naive = is_satisfied(circuit, lambda atom: True)
    without_units = copy.deepcopy(doc)
    for a in annotations(without_units).values():
        if a["participant"]["selector_type"] == "PROTEIN_COMPLEX":
            a["participant"]["protein_complex"]["active_units"] = []

    def signature(d):
        return [
            [x.node_id for x in r] for r in enumerate_routes(compile_node(d["module"]))
        ]

    assert signature(doc) == signature(without_units)
    without_edges = copy.deepcopy(doc)

    def remove_edges(value):
        if isinstance(value, dict):
            value.pop("connections", None)
            for child in value.values():
                remove_edges(child)
        elif isinstance(value, list):
            for child in value:
                remove_edges(child)

    remove_edges(without_edges)
    assert signature(doc) == signature(without_edges)
    result = {
        "result": "PASS",
        "compiler_observations": {
            "removing_all_active_units_preserves_raw_routes": True,
            "removing_connections_preserves_raw_routes": True,
            "all_four_atoms_including_both_EXACTLY_ONE_branches_is_satisfied": naive,
        },
        "members": len(bank),
        "cases": len(results),
        "structural_mutations": len(mutations),
        "gate_sensitivities": len(sensitivity),
        "atoms": [x.node_id for x in iter_atoms(circuit)],
        "routes": [[x.node_id for x in r] for r in enumerate_routes(circuit)],
        "core_atoms": [x.node_id for x in core_atoms(circuit)],
        "naive_complex_presence_all_atoms_true": naive,
        "production_limitations": [
            "active_units, biological context and edges are not evaluated by production compile_node/is_satisfied",
            "EXACTLY_ONE is at-least-one in production; this wrapper supplies context-qualified atom predicates",
            "Finite positive representatives and evidence profiles are not a genome classifier or native flux assay",
        ],
        "broad_family_controls": controls,
        "case_results": results,
        "mutations": mutations,
        "sensitivities": sensitivity,
    }
    (A / "results.json").write_text(json.dumps(result, indent=2) + "\n")
    ledger = {
        str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest()
        for p in sorted(INPUTS)
    }
    (A / "input-hashes.json").write_text(json.dumps(ledger, indent=2) + "\n")
    print(
        json.dumps(
            {
                k: result[k]
                for k in [
                    "result",
                    "members",
                    "cases",
                    "structural_mutations",
                    "gate_sensitivities",
                ]
            }
        )
    )


if __name__ == "__main__":
    main()
