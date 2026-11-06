#!/usr/bin/env python3
"""Check the reviewed divisome panel with production module logic and a scoped oracle.

Run from anywhere with ``uv run python <this file> [--output PATH]``. The oracle
adds checks the production Atom intentionally does not encode: active units,
proposed molecular functions, contextual conditions and one shared pair witness.
This is reviewed-panel capacity, not a genome-wide absence or viability predictor.
"""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "src"))
from ai_gene_review.module_logic import compile_node, is_satisfied, iter_atoms  # noqa: E402

SLUG = "bacterial_divisome_peptidoglycan_transpeptidation"
MODULE = ROOT / "modules" / f"{SLUG}.yaml"
BASELINE = ROOT / "analysis/module_audits" / SLUG / "seed-baseline.yaml"
GT = "GO:0008955"
DD = "serine-type peptidoglycan D,D-transpeptidase activity"
GLYCAN = "peptidoglycan glycan strand bearing peptide stems"
DD_INPUTS = {
    GLYCAN,
    "peptidoglycan donor stem terminating in D-Ala-D-Ala",
    "amino acceptor on an adjacent stem peptide or its interpeptide bridge",
}
DD_OUTPUTS = {"D,D-crosslinked peptidoglycan", "D-alanine"}

# Independent evidence-backed witness registry; not generated from module topology.
# 30692671 directly tests STAA8/STRT2 recombinant interfaces, including TP-dead
# partners. ECOLI uses native complex20847002 + in-vivo33495624 and comparative
# activation biochemistry. BACSU uses168 compensation28792086 + PY7938480901;
# assigning its activation interface is an explicitly qualified inference.
PAIRS = {
    "ecoli": ("83333", "P0ABG4", "P0AD68"),
    "bacsu": ("224308", "O07639", "Q07868"),
    "staa8": ("93061", "Q2G2C2", "Q2FZ94"),
    "strt2": ("264199", "Q5M5I9", "Q5M2U8"),
}
ROLE_SOURCES = {
    "P0ABG4": {"PMID:33495624", "PMID:30692671"},
    "P0AD68": {"PMID:3531167", "PMID:20847002"},
    "O07639": {"PMID:38480901", "PMID:30692671"},
    "Q07868": {"PMID:28792086"},
    "P42971": {"PMID:28792086"},
    "Q2G2C2": {"PMID:30692671"},
    "Q2FZ94": {"PMID:30692671", "PMID:35703435"},
    "Q5M5I9": {"PMID:30692671"},
    "Q5M2U8": {"PMID:30692671"},
}


@dataclass
class Protein:
    accession: str
    taxon: str
    families: set[str]
    review: dict
    path: str


@dataclass
class Scenario:
    name: str
    inventory: set[str]
    catalytic_off: set[str] = field(default_factory=set)
    interface_off: set[str] = field(default_factory=set)
    conditional_bacsu: bool = False


@dataclass(frozen=True)
class Witness:
    lineage: str
    taxon: str
    polymerase: str
    partner: str
    crosslinker: str
    conditional: bool = False


def load_panel() -> tuple[dict[str, Protein], dict]:
    baseline = yaml.safe_load(BASELINE.read_text())
    panel = {}
    for member in baseline["members"]:
        path = ROOT / member["review_path"]
        review = yaml.safe_load(path.read_text())
        assert review["id"] == member["accession"]
        raw = path.with_name(path.name.replace("-ai-review.yaml", "-uniprot.txt"))
        families = set(
            re.findall(r"^DR\s+PANTHER; (PTHR\d+(?::SF\d+)?);", raw.read_text(), re.M)
        )
        families |= {f.split(":")[0] for f in families}
        panel[review["id"]] = Protein(
            review["id"],
            review["taxon"]["id"].split(":")[-1],
            families,
            review,
            member["review_path"],
        )
    return panel, baseline


def has_reviewed_role(protein: Protein) -> bool:
    if (
        protein.accession not in ROLE_SOURCES
        or protein.review.get("status") != "COMPLETE"
    ):
        return False
    supported = {
        e["reference_id"]
        for c in protein.review.get("core_functions", [])
        for e in c.get("supported_by", [])
        if e.get("supporting_text")
    }
    return ROLE_SOURCES[protein.accession] <= supported


def matches_function(protein: Protein, requirement: dict) -> bool:
    """Empty GO ids must not make a proposed-function requirement vacuously true."""
    if not has_reviewed_role(protein):
        return False
    term = (requirement.get("term") or {}).get("id")
    cores = protein.review.get("core_functions", [])
    if term:
        # No broad transferase, hydrolysis or L,D proxy satisfies this model.
        return term == GT and any(
            c.get("molecular_function", {}).get("id") == term and c.get("supported_by")
            for c in cores
        )
    if requirement.get("preferred_term") != DD:
        return False
    if {s["preferred_term"] for s in requirement.get("substrates", [])} != DD_INPUTS:
        return False
    if {s["preferred_term"] for s in requirement.get("products", [])} != DD_OUTPUTS:
        return False
    proposed = {
        p["proposed_name"]: p
        for p in protein.review.get("proposed_new_terms", []) or []
    }
    proposal = proposed.get(DD)
    if (
        not proposal
        or not proposal.get("proposed_definition")
        or not proposal.get("supported_by")
    ):
        return False
    return any(
        c.get("proposed_molecular_function") == DD and c.get("supported_by")
        for c in cores
    )


def selector_accepts(selector: dict, protein: Protein, scenario: Scenario) -> bool:
    if protein.accession not in scenario.inventory or not has_reviewed_role(protein):
        return False
    family = selector.get("family", {})
    required_families = {
        t["id"].removeprefix("PANTHER:")
        for t in [family.get("term"), *family.get("family_terms", [])]
        if t
    }
    if not required_families or not required_families.intersection(protein.families):
        return False
    requirement = selector.get("required_function")
    return not requirement or (
        protein.accession not in scenario.catalytic_off
        and matches_function(protein, requirement)
    )


def index_annotons(node: dict, inherited: dict | None = None) -> dict:
    context = {**(inherited or {}), **node.get("context", {})}
    result = {}
    for annoton in node.get("annotons", []):
        assert annoton["id"] not in result
        result[annoton["id"]] = (annoton, {**context, **annoton.get("context", {})})
    children = [p["node"] for p in node.get("parts", [])]
    children += [v for vs in node.get("variant_sets", []) for v in vs["variants"]]
    for child in children:
        sub = index_annotons(child, context)
        assert not result.keys() & sub.keys(), "Duplicate annoton ids"
        result.update(sub)
    return result


def witness_oracle(node: dict, scenario: Scenario, panel: dict, witness: Witness):
    index = index_annotons(node)

    def holds(atom) -> bool:
        annoton, context = index[atom.node_id]
        taxa = {
            t["term"]["id"].split(":")[-1]
            for t in context.get("taxa", [])
            if t.get("term")
        }
        if witness.taxon not in taxa:
            return False
        if context.get("conditions") and not (
            scenario.conditional_bacsu and witness.conditional
        ):
            return False
        selector = annoton.get("participant", {})
        if selector.get("selector_type") == "PROTEIN_COMPLEX":
            units = selector.get("protein_complex", {}).get("active_units", [])
            catalytic = [
                u
                for u in units
                if u.get("function", {}).get("term", {}).get("id") == GT
            ]
            structural = [u for u in units if not u.get("function")]
            # This bound two-unit synthase is not an empty, automatically true complex.
            if len(units) != 2 or len(catalytic) != 1 or len(structural) != 1:
                return False
            if annoton.get("function", {}).get("term", {}).get("id") != GT:
                return False
            w, p = panel.get(witness.polymerase), panel.get(witness.partner)
            if not w or not p or w.taxon != witness.taxon or p.taxon != witness.taxon:
                return False
            if {w.accession, p.accession} & scenario.interface_off:
                return False
            return (
                w.accession not in scenario.catalytic_off
                and matches_function(w, catalytic[0]["function"])
                and selector_accepts(catalytic[0]["participant"], w, scenario)
                and selector_accepts(structural[0]["participant"], p, scenario)
            )
        function = annoton.get("function")
        if function:
            protein = panel.get(witness.crosslinker)
            return bool(
                protein
                and protein.taxon == witness.taxon
                and protein.accession not in scenario.catalytic_off
                and matches_function(protein, function)
                and selector_accepts(selector, protein, scenario)
            )
        # The only noncatalytic leaf outside a polymerase complex is physical PBP2B
        # retention in the conditional Bacillus implementation. Never infer TP activity.
        protein = panel.get(witness.partner)
        return bool(
            witness.conditional
            and witness.partner == "Q07868"
            and protein
            and protein.taxon == witness.taxon
            and protein.accession not in scenario.interface_off
            and selector_accepts(selector, protein, scenario)
        )

    return holds


def witnesses(scenario: Scenario):
    for lineage, (taxon, w, p) in PAIRS.items():
        yield Witness(lineage, taxon, w, p, p)
        if (
            lineage == "bacsu"
            and scenario.conditional_bacsu
            and p in scenario.catalytic_off
        ):
            yield Witness(lineage, taxon, w, p, "P42971", True)


def capacity(node: dict, scenario: Scenario, panel: dict) -> bool:
    circuit = compile_node(node)
    return any(
        is_satisfied(circuit, witness_oracle(node, scenario, panel, w))
        for w in witnesses(scenario)
    )


def structural_checks(doc: dict, panel: dict) -> dict:
    node = doc["module"]
    parts = {p["node"]["id"]: p for p in node["parts"]}
    assert set(parts) == {"ftsw_glycan_polymerization", "ftsi_dd_transpeptidation"}
    assert not any(p.get("optional") for p in parts.values())
    assert all(p["node"]["module_type"] == "REACTION" for p in parts.values())
    index = index_annotons(node)
    assert {"ftsw_glycosyltransferase", "ftsi_dd_transpeptidase"} <= index.keys()
    assert {a.node_id for a in iter_atoms(compile_node(node))} == set(index)
    representatives = set()

    def scan(value):
        if isinstance(value, dict):
            for rep in value.get("representative_members", []):
                representatives.add(rep["term"]["id"].removeprefix("UniProtKB:"))
            for v in value.values():
                scan(v)
        elif isinstance(value, list):
            for v in value:
                scan(v)

    scan(node)
    assert representatives == set(panel), (
        "All nine reviewed representatives must remain"
    )
    for annoton, _ in index.values():
        function = annoton.get("function")
        if function and not function.get("term"):
            assert function["preferred_term"] == DD
            assert annoton["participant"]["required_function"] == function
    return {
        "root_required_reactions": 2,
        "annotons": len(index),
        "representatives": len(representatives),
    }


def run_cases(doc: dict, panel: dict) -> list[dict]:
    node = doc["module"]
    polymerization = node["parts"][0]["node"]
    crosslinking = node["parts"][1]["node"]
    results = []

    def test(name, expected, scenario, target=node, proteins=panel, reason=""):
        actual = capacity(target, scenario, proteins)
        results.append(
            {
                "case": name,
                "expected": expected,
                "actual": actual,
                "passed": actual == expected,
                "reason": reason,
            }
        )
        assert actual == expected, f"{name}: expected {expected}, got {actual}"

    for lineage, (_, w, p) in PAIRS.items():
        inventory = {w, p}
        test(
            f"{lineage}_native_pair",
            True,
            Scenario(lineage, inventory),
            reason="Two supported activities with one compatible native-reference witness; not autonomous native cytokinesis.",
        )
        test(f"{lineage}_without_FtsW", False, Scenario(lineage, {p}))
        test(f"{lineage}_without_bPBP", False, Scenario(lineage, {w}))
        test(f"{lineage}_FtsW_catalysis_off", False, Scenario(lineage, inventory, {w}))
        test(f"{lineage}_bPBP_catalysis_off", False, Scenario(lineage, inventory, {p}))
        test(
            f"{lineage}_TP_dead_polymerization",
            True,
            Scenario(lineage, inventory, {p}),
            polymerization,
            reason="Direct purified result for STAA8/STRT2; comparative structural-partner inference for ECOLI/BACSU.",
        )
        test(
            f"{lineage}_interface_disabled",
            False,
            Scenario(lineage, inventory, interface_off={p}),
        )
    bac = {"O07639", "Q07868", "P42971"}
    test(
        "bacsu_PBP2B_S309A_PBP3_active",
        True,
        Scenario("backup", bac, {"Q07868"}, conditional_bacsu=True),
    )
    test(
        "bacsu_PBP2B_S309A_no_PBP3",
        False,
        Scenario("backup", bac - {"P42971"}, {"Q07868"}, conditional_bacsu=True),
    )
    test(
        "bacsu_PBP2B_S309A_PBP3_S410A",
        False,
        Scenario("backup", bac, {"Q07868", "P42971"}, conditional_bacsu=True),
    )
    test(
        "bacsu_PBP2B_deleted_PBP3_present",
        False,
        Scenario("backup", bac - {"Q07868"}, conditional_bacsu=True),
    )
    test(
        "bacsu_backup_not_activated_without_context",
        False,
        Scenario("no-context", bac, {"Q07868"}),
    )
    test(
        "bacsu_PBP3_not_needed_in_normal_pair",
        True,
        Scenario("normal", bac - {"P42971"}),
    )
    test(
        "strt2_deltaTM_loses_polymerization",
        False,
        Scenario("deltaTM", {"Q5M5I9", "Q5M2U8"}, interface_off={"Q5M2U8"}),
        polymerization,
    )
    test(
        "strt2_deltaTM_retains_crosslink_catalysis",
        True,
        Scenario("deltaTM", {"Q5M2U8"}, interface_off={"Q5M2U8"}),
        crosslinking,
        reason="30692671 TP activity survives deltaTM with glycan from other polymerases; focused full route still fails.",
    )
    test(
        "strt2_FtsW_plus_staa8_PBP1",
        False,
        Scenario("incompatible", {"Q5M5I9", "Q2FZ94"}),
        reason="Directly incompatible in30692671; family presence cannot rescue it.",
    )
    test(
        "staa8_FtsW_plus_strt2_PBP2x",
        False,
        Scenario("incompatible", {"Q2G2C2", "Q5M2U8"}),
    )
    test(
        "cross_taxon_independent_half_pairs",
        False,
        Scenario("mixed", {"P0ABG4", "Q07868"}),
    )
    test("all_panel_reference_proteins", True, Scenario("panel", set(panel)))
    # Independent perturbations to the evidence objects: not expected values
    # computed from the same selectors that the oracle is meant to challenge.
    for name, accession, modification in [
        ("RodA_family_cannot_replace_FtsW", "P0ABG4", "roda"),
        ("SpoVE_family_cannot_replace_FtsW", "P0ABG4", "spove"),
        ("SF1_without_reviewed_division_role", "P0AD68", "role"),
        ("NTR_label_without_supported_core", "P0AD68", "core"),
        ("NTR_without_definition_support", "P0AD68", "proposal"),
        ("family_only_unknown_protein", "P0AD68", "unknown"),
        ("same_accession_wrong_taxon", "P0AD68", "taxon"),
        ("complex_contribution_is_not_autonomous_FtsW", "P0ABG4", "contributes"),
    ]:
        edited = copy.deepcopy(panel)
        protein = edited[accession]
        if modification in {"roda", "spove"}:
            protein.families = {
                "PTHR30474",
                "PTHR30474:SF3" if modification == "roda" else "PTHR30474:SF13",
            }
        elif modification == "role":
            protein.review["core_functions"][0]["supported_by"] = []
        elif modification == "core":
            protein.review["core_functions"][0].pop("proposed_molecular_function")
        elif modification == "proposal":
            protein.review["proposed_new_terms"][0]["supported_by"] = []
        elif modification == "unknown":
            protein.accession = "UNKNOWN_SAME_FAMILY"
        elif modification == "taxon":
            protein.taxon = "999999"
        elif modification == "contributes":
            core = protein.review["core_functions"][0]
            core["contributes_to_molecular_function"] = core.pop("molecular_function")
        test(name, False, Scenario(name, {"P0ABG4", "P0AD68"}), proteins=edited)
    for go_id in ["GO:0009002", "GO:0071972", "GO:0016746"]:
        edited = copy.deepcopy(node)
        a = edited["parts"][1]["node"]["variant_sets"][0]["variants"][0]["annotons"][0]
        a["function"]["term"] = {"id": go_id}
        a["participant"]["required_function"] = a["function"]
        test(
            f"incorrect_DD_proxy_{go_id}",
            False,
            Scenario("proxy", {"P0ABG4", "P0AD68"}),
            edited,
        )
    edited = copy.deepcopy(node)
    a = edited["parts"][1]["node"]["variant_sets"][0]["variants"][0]["annotons"][0]
    a["function"]["substrates"] = [{"preferred_term": "water"}]
    a["participant"]["required_function"] = a["function"]
    test(
        "same_NTR_wrong_substrate_scope",
        False,
        Scenario("water", {"P0ABG4", "P0AD68"}),
        edited,
    )
    for mutation in [
        "empty_complex",
        "missing_activator",
        "wrong_activator_family",
        "requiring_activator_catalysis",
    ]:
        edited = copy.deepcopy(node)
        a = edited["parts"][0]["node"]["variant_sets"][0]["variants"][1]["annotons"][0]
        units = a["participant"]["protein_complex"]["active_units"]
        if mutation == "empty_complex":
            units.clear()
        elif mutation == "missing_activator":
            units.pop()
        elif mutation == "wrong_activator_family":
            units[1]["participant"]["family"]["term"]["id"] = "PANTHER:PTHR30627:SF25"
        else:
            units[1]["participant"]["required_function"] = copy.deepcopy(
                node["parts"][1]["node"]["variant_sets"][0]["variants"][1]["annotons"][
                    0
                ]["function"]
            )
        test(
            mutation,
            False,
            Scenario("backup", bac, {"Q07868"}, conditional_bacsu=True),
            edited,
        )
    # In-vitro compatibility is intentionally a different question from native
    # panel completeness. Explicit positive counterexample to universal rejection
    # of heterologous pairs; no unreviewed protein is added to native gene capacity.
    source = (ROOT / "publications/PMID_30692671.md").read_text()
    quote = "StFtsW was able to polymerize Lipid II when combined either with its cognate bPBP, StPBP2x, or with the divisome bPBP from S. pneumoniae (SpPBP2x)"
    assert quote in source
    results.append(
        {
            "case": "documented_heterologous_StFtsW_SpPBP2x",
            "expected": True,
            "actual": True,
            "passed": True,
            "reason": "Independent primary positive compatibility, not an unreviewed complete native-panel witness.",
            "supporting_text": quote,
        }
    )
    return results


def preservation(panel: dict, baseline: dict) -> dict:
    for name, expected in baseline["protected_source_sha256"].items():
        assert hashlib.sha256((ROOT / name).read_bytes()).hexdigest() == expected, name
    counts = {
        "historical_rows": baseline["historical_rows"],
        "current_rows": 0,
        "NEW_rows": 0,
    }
    for protein in panel.values():
        rows = protein.review["existing_annotations"]
        counts["current_rows"] += len(rows)
        counts["NEW_rows"] += sum(a["review"]["action"] == "NEW" for a in rows)
        assert all(a["review"]["action"] != "PENDING" for a in rows)
    counts["protected_source_files"] = len(baseline["protected_source_sha256"])
    # Full payload proof uses frozen originals, never today's reviewed rows as baseline.
    # These captures are ignored operational artifacts; a clean checkout reports
    # their absence rather than fabricating a successful payload comparison.
    cache = ROOT / ".cache/module-audit-logs/divisome-20261106"
    old_path, seed_path = (
        cache / "original-members-baseline.json",
        cache / "additional-seed-state.json",
    )
    if old_path.exists() and seed_path.exists():
        originals = json.loads(old_path.read_text())["reviews"]
        seeds = json.loads(seed_path.read_text())["members"]
        originals.update({s["review_path"]: s for s in seeds})
        compared = 0
        for protein in panel.values():
            original = originals[protein.path]["rows"]
            current = protein.review["existing_annotations"]
            payload = lambda row: {k: v for k, v in row.items() if k != "review"}  # noqa: E731
            assert [payload(r) for r in current[: len(original)]] == [
                payload(r) for r in original
            ]
            assert all(r["review"]["action"] == "NEW" for r in current[len(original) :])
            compared += len(original)
        assert compared == 160
        counts["payload_comparison"] = {"status": "PASS", "rows": compared}
    else:
        counts["payload_comparison"] = {
            "status": "NOT_RUN",
            "reason": "Original operational capture unavailable; source hashes and row counts checked.",
        }
    assert counts["current_rows"] == 162 and counts["NEW_rows"] == 2
    return counts


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output", type=Path, help="Optional YAML report outside modules/ discovery"
    )
    args = parser.parse_args()
    panel, baseline = load_panel()
    doc = yaml.safe_load(MODULE.read_text())
    report = {
        "module": SLUG,
        "module_sha256": hashlib.sha256(MODULE.read_bytes()).hexdigest(),
        "checker_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "interpretation": "Reviewed-panel paired reaction capacity. Native-context inference, biochemical compatibility and cytokinesis sufficiency are distinct.",
        "structure": structural_checks(doc, panel),
        "preservation": preservation(panel, baseline),
        "cases": run_cases(doc, panel),
        "review_sha256": {
            p.path: hashlib.sha256((ROOT / p.path).read_bytes()).hexdigest()
            for p in panel.values()
        },
        "limitations": [
            "PROTEIN_COMPLEX active units and textual NTR functions are checked by this explicit oracle, not by Atom.function_ids.",
            "The native registry is a curated panel, not evidence that all cross-species pairs are incompatible or that unlisted genomes lack capacity.",
            "Bacillus activation is a qualified inference from native physical roles and comparative biochemistry; PBP3 catalytic rescue is not a purified linkage-product assay.",
            "The StFtsW construct omits current residues1-5 and its assay uses E. faecalis lipid II; native bridge identity is not assigned.",
        ],
    }
    report["case_count"] = len(report["cases"])
    report["passed"] = all(c["passed"] for c in report["cases"])
    if args.output:
        target = args.output.resolve()
        assert not target.is_relative_to(ROOT / "modules"), (
            "Audit YAML must stay outside module discovery"
        )
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(yaml.safe_dump(report, sort_keys=False, width=105))
    print(
        json.dumps(
            {
                k: report[k]
                for k in [
                    "case_count",
                    "passed",
                    "structure",
                    "preservation",
                    "module_sha256",
                ]
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
