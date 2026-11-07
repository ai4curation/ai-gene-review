"""Production module circuit plus explicit, source-qualified biological predicates."""

import copy
import hashlib
import json
import re
from pathlib import Path

import yaml

from ai_gene_review.module_logic import (
    compile_node,
    enumerate_routes,
    is_satisfied,
    iter_atoms,
)

A = Path(__file__).resolve().parent
ROOT = A.parents[3]
MODULE = ROOT / "modules/bacterial_mnma_trna_thiolation.yaml"
BIO = yaml.safe_load((A / "biology.yaml").read_text())
CASES = json.loads((A / "cases.json").read_text())["cases"]
INPUTS = {
    MODULE,
    A / "biology.yaml",
    A / "cases.json",
    Path(__file__).resolve(),
    ROOT / "src/ai_gene_review/module_logic.py",
}

INPUTS.update(
    ROOT / "src/ai_gene_review" / name
    for name in ["render_modules.py", "module_gene_symbols.py", "module_qc.py"]
)


def walk(node):
    yield node
    for part in node.get("parts", []):
        yield from walk(part["node"])
    for variants in node.get("variant_sets", []):
        for branch in variants["variants"]:
            yield from walk(branch)


def load(path):
    path = ROOT / path
    INPUTS.add(path)
    return yaml.safe_load(path.read_text())


def normalize(text):
    return re.sub(r"\s+", " ", text)


def catalog():
    for source in BIO["sources"].values():
        path = ROOT / source["path"]
        INPUTS.add(path)
        text = path.read_text()
        if source.get("quote"):
            assert normalize(source["quote"]) in normalize(text), source["path"]
    result = {}
    for panel, profile in BIO["panels"].items():
        for role, (symbol, accession) in profile["roles"].items():
            path = Path(f"genes/{panel}/{symbol}/{symbol}-ai-review.yaml")
            review = load(path)
            assert review["id"] == accession and review["status"] == "COMPLETE"
            assert review["taxon"]["id"] == profile["taxon"]
            raw = ROOT / path.with_name(symbol + "-uniprot.txt")
            INPUTS.add(raw)
            text = raw.read_text()
            assert re.search(r"^AC\s+" + accession + r";", text, re.M)
            families = set(
                re.findall(r"^DR\s+PANTHER; (PTHR\d+(?::SF\d+)?);", text, re.M)
            )
            result[accession] = {
                "panel": panel,
                "role": role,
                "review": review,
                "families": {"PANTHER:" + f for f in families},
                "sources": profile["sources"],
            }
    for accession, control in BIO["controls"].items():
        record = load(control["path"])
        assert record["primaryAccession"] == accession
        result[accession] = {
            "panel": "CONTROL",
            "role": None,
            "review": {},
            "families": {
                "PANTHER:" + x["id"]
                for x in record["uniProtKBCrossReferences"]
                if x["database"] == "PANTHER"
            },
            "sources": [],
        }
    assert len(result) == 22
    return result


def core_ok(member, role):
    requirement = BIO["role_requirements"][role]
    cores = member["review"].get("core_functions", [])
    if requirement.get("mf"):
        return any(
            c.get("molecular_function", {}).get("id") == requirement["mf"]
            and c.get("supported_by")
            for c in cores
        )
    return any(
        c.get("in_complex", {}).get("id") == requirement["structural_complex"]
        and c.get("supported_by")
        and any(p["id"] == "GO:0002143" for p in c.get("directly_involved_in", []))
        for c in cores
    )


def evaluate(doc, case, bank, bypass=()):
    nodes = {node["id"]: node for node in walk(doc["module"])}
    annotons = {a["id"]: a for n in nodes.values() for a in n.get("annotons", [])}
    circuit = compile_node(doc["module"], ROOT / "modules")
    selected = {
        accession: copy.deepcopy(bank[accession]) for accession in case["members"]
    }
    for member in selected.values():
        if case.get("mask") == "sources":
            member["sources"] = []
        elif case.get("mask") == "core":
            member["review"]["core_functions"] = []
        elif case.get("mask") == "family":
            member["families"] = set()
    context = set(BIO["contexts"]) - set(case.get("remove_context", []))
    panel_results = {}
    for panel in BIO["panels"]:
        failures = {}
        assignments = {}

        def unit_matches(unit, role):
            family = unit["participant"].get("family", {})
            ids = {
                r["term"]["id"].split(":")[1]
                for r in family.get("representative_members", [])
            }
            family_id = family.get("term", {}).get("id")
            hits = []
            for accession, member in sorted(selected.items()):
                if "identity" not in bypass and accession not in ids:
                    continue
                if "panel" not in bypass and member["panel"] != panel:
                    continue
                if "role" not in bypass and member["role"] != role:
                    continue
                if "sources" not in bypass and not member["sources"]:
                    continue
                if "core" not in bypass and not core_ok(member, role):
                    continue
                if "family" not in bypass and family_id not in member["families"]:
                    continue
                hits.append(accession)
            return hits

        def holds(atom):
            reasons = []
            if "context" not in bypass and not set(BIO["contexts"]).issubset(context):
                reasons.append("missing sulfur/ATP/susceptible U34 substrate context")
            if (
                atom.node_id == "ctype_mnma_activity"
                and "cluster" not in bypass
                and not case.get("active_ctype_cluster", True)
            ):
                reasons.append("inactive C-type cluster state")
            annoton = annotons[atom.node_id]
            participant = annoton["participant"]
            units = participant.get("protein_complex", {}).get("active_units")
            if units is not None:
                hitmap = {
                    u["id"]: unit_matches(u, BIO["unit_roles"][u["id"]]) for u in units
                }
                if not units or not all(hitmap.values()):
                    reasons.append("incomplete compatible TusBCD role-bearing assembly")
            else:
                hitmap = {
                    atom.node_id: unit_matches(annoton, BIO["atom_roles"][atom.node_id])
                }
                if not all(hitmap.values()):
                    reasons.append(
                        "no source-qualified member with required role/core/family/interface"
                    )
            failures[atom.node_id] = reasons
            assignments[atom.node_id] = hitmap
            return not reasons

        # Evaluate every atom for deterministic diagnostics, then use production evaluator.
        atom_values = {a.node_id: holds(a) for a in iter_atoms(circuit)}
        accepted = is_satisfied(circuit, lambda atom: atom_values[atom.node_id])
        panel_results[panel] = {
            "satisfied": accepted,
            "atom_values": atom_values,
            "assignments": assignments,
            "failures": failures,
        }
    return {
        "satisfied": any(r["satisfied"] for r in panel_results.values()),
        "panels": panel_results,
    }


def mutate(doc, name):
    result = copy.deepcopy(doc)
    nodes = {node["id"]: node for node in walk(result["module"])}
    if name.startswith("drop_unit_"):
        unit = name.removeprefix("drop_unit_")
        units = nodes["tusbcd_transfer"]["annotons"][0]["participant"][
            "protein_complex"
        ]["active_units"]
        units[:] = [u for u in units if u["id"] != unit]
    elif name.startswith("drop_step_"):
        target = name.removeprefix("drop_step_")
        for node in nodes.values():
            node["parts"] = [
                p for p in node.get("parts", []) if p["node"]["id"] != target
            ]
    elif name == "force_tus_only":
        vs = result["module"]["variant_sets"][0]
        vs["variants"] = [v for v in vs["variants"] if v["id"] == "tus_relay_route"]
    elif name == "require_both_thermus_donors":
        donor = nodes["ctype_donor_supply"]
        vs = donor.pop("variant_sets")[0]
        donor["parts"] = [{"node": v} for v in vs["variants"]]
    else:
        raise AssertionError(name)
    return result


def run():
    bank = catalog()
    for accession, member in bank.items():
        if member["panel"] != "CONTROL":
            assert core_ok(member, member["role"]), accession
    doc = load(MODULE)
    circuit = compile_node(doc["module"], ROOT / "modules")
    routes = [[a.node_id for a in route] for route in enumerate_routes(circuit)]
    assert len(routes) == 4
    results = []
    for case in CASES:
        result = evaluate(doc, case, bank)
        assert result["satisfied"] == case["expected"], case["id"]
        results.append({"case": case["id"], "expected": case["expected"], **result})
    mutations = {}
    names = [
        "drop_step_tusa_handoff",
        "drop_step_tuse_delivery",
        "drop_step_cognate_donor_mobilization",
        "drop_step_ctype_mnma_thiolation",
        "drop_unit_tusb_unit",
        "drop_unit_tusc_unit",
        "drop_unit_tusd_unit",
        "force_tus_only",
        "require_both_thermus_donors",
    ]
    for name in names:
        changed = mutate(doc, name)
        failures = [
            c["id"]
            for c in CASES
            if evaluate(changed, c, bank)["satisfied"] != c["expected"]
        ]
        assert failures, name
        mutations[name] = {"detected_by": failures}
    sensitivity_specs = {
        "source_gate": ("ecoli_no_source", ["sources"]),
        "core_gate": ("bacillus_no_core", ["core"]),
        "family_gate": ("ecoli_no_family", ["family"]),
        "interface_gate": ("mixed_ecoli_kt2440_tusd", ["panel"]),
        "supply_gate": ("ecoli_without_ATP", ["context"]),
        "active_cluster_gate": ("thermus_inactive_cluster", ["cluster"]),
        "same_sf8_family_only_is_unsafe": (
            "egtE_same_sf8_donor",
            ["identity", "panel", "role", "sources", "core"],
        ),
        "true_desulfurase_wrong_pair": (
            "bacillus_with_ecoli_iscs",
            ["identity", "panel"],
        ),
    }
    sensitivities = {}
    for name, (case_id, bypass) in sensitivity_specs.items():
        case = next(c for c in CASES if c["id"] == case_id)
        assert not evaluate(doc, case, bank)["satisfied"]
        disabled = evaluate(doc, case, bank, bypass)["satisfied"]
        assert disabled, name
        sensitivities[name] = {
            "case": case_id,
            "bypassed_gates": bypass,
            "baseline": False,
            "unsafe_relaxed_result": disabled,
        }
    return {
        "status": "PASS",
        "counts": {
            "cases": len(results),
            "mutations_detected": len(mutations),
            "gate_sensitivities": len(sensitivities),
            "reviewed_members": 19,
            "real_controls": 3,
            "production_atoms": len(list(iter_atoms(circuit))),
            "production_routes": len(routes),
        },
        "module_sha256": hashlib.sha256(MODULE.read_bytes()).hexdigest(),
        "routes": routes,
        "cases": results,
        "mutations": mutations,
        "sensitivities": sensitivities,
        "input_hashes": {
            str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest()
            for p in sorted(INPUTS)
        },
    }


if __name__ == "__main__":
    print(json.dumps(run(), indent=2, sort_keys=True))
