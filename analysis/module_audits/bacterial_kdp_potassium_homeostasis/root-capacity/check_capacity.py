"""Evidence-qualified Kdp capacity tests; never edits curated inputs.

The production compiler owns AND/OR structure. This oracle supplies explicitly
qualified molecular witnesses, not expression/flux measurements or genome absence.
"""

import copy
import hashlib
import json
import re
from dataclasses import asdict
from pathlib import Path

import yaml

from ai_gene_review.module_logic import (
    compile_node,
    core_atoms,
    is_satisfied,
    iter_atoms,
)

ROOT = Path(__file__).resolve().parents[4]
AUDIT = Path(__file__).resolve().parent
MODULE = ROOT / "modules/bacterial_kdp_potassium_homeostasis.yaml"
GATES = json.loads((AUDIT / "evidence-gates.json").read_text())
QUOTES = json.loads((AUDIT / "source-quotes.json").read_text())
READ = {MODULE, ROOT / "src/ai_gene_review/module_logic.py"}
PUMP = "GO:0008556"
COMPLEX = "GO:0031004"
RECEIVER = "GO:0000156"
DNA = "GO:0000987"
OUTPUT = "GO:0045893"
ROLE_FAMILIES = {
    "kdpA": "PANTHER:PTHR30607:SF2",
    "kdpB": "PANTHER:PTHR43743:SF1",
    "kdpC": "PANTHER:PTHR30042:SF2",
    "kdpF": "NCBIfam:TIGR02115",
}


def load(path):
    READ.add(path)
    return yaml.safe_load(path.read_text())


def term_ids(value):
    if isinstance(value, dict):
        return {value["id"]} if "id" in value else set()
    return set().union(*(term_ids(item) for item in value or []))


def review_record(org, gene):
    path = ROOT / "genes" / org / gene / f"{gene}-ai-review.yaml"
    raw = path.with_name(f"{gene}-uniprot.txt")
    d = load(path)
    READ.add(raw)
    raw_text = raw.read_text()
    accessions = set(
        re.findall(
            r"[A-Z0-9]+",
            " ".join(
                line[5:] for line in raw_text.splitlines() if line.startswith("AC   ")
            ),
        )
    )
    assert d["id"] in accessions, (path, d["id"])
    assert (
        re.search(r"^OX   NCBI_TaxID=(\d+)", raw_text, re.M).group(1)
        == d["taxon"]["id"].split(":")[1]
    ), path
    families = {
        f"{db}:{identifier}"
        for db, identifier in re.findall(
            r"^DR   (PANTHER|NCBIfam); ([^;]+);", raw.read_text(), re.M
        )
    }
    molecular, contributes, complexes, processes = set(), set(), set(), set()
    for core in d.get("core_functions", []):
        molecular |= term_ids(core.get("molecular_function"))
        contributes |= term_ids(core.get("contributes_to_molecular_function"))
        complexes |= term_ids(core.get("in_complex"))
        processes |= term_ids(core.get("directly_involved_in"))
    # Current accepted DNA-binding annotations complement E. coli's more specific
    # core activator MF. An unreviewed GOA row never supplies an oracle claim.
    for row in d.get("existing_annotations", []):
        review = row.get("review", {})
        if not review.get("retired") and review.get("action") in {
            "ACCEPT",
            "KEEP_AS_NON_CORE",
            "NEW",
        }:
            molecular |= term_ids(row.get("term")) & {DNA}
    return {
        "accession": d["id"],
        "instance": d["id"],
        "panel": org,
        "taxon": d["taxon"]["id"],
        "gene": gene,
        "families": sorted(families),
        "molecular": sorted(molecular),
        "contributes": sorted(contributes),
        "complexes": sorted(complexes),
        "processes": sorted(processes),
        "review": str(path.relative_to(ROOT)),
        "raw": str(raw.relative_to(ROOT)),
    }


RECORDS = []
for organism, genes in {
    "ECOLI": [f"kdp{x}" for x in "ABCDEF"],
    "PSEPK": [f"kdp{x}" for x in "ABCDEF"],
    "CAUVN": [f"kdp{x}" for x in "ABCDE"],
    "DESVH": ["Q725T7"],
    "DEIGD": ["Dgeo_2852"],
    "STAA8": ["kdpD"],
}.items():
    RECORDS.extend(review_record(organism, gene) for gene in genes)
DOC = load(MODULE)


def nodes(node):
    yield node
    for part in node.get("parts", []):
        yield from nodes(part["node"])
    for variants in node.get("variant_sets", []):
        for child in variants["variants"]:
            yield from nodes(child)


def panel(name, without=()):
    return copy.deepcopy(
        [r for r in RECORDS if r["panel"] == name and r["gene"] not in without]
    )


def match_selector(record, selector, disabled):
    family = selector.get("family", {})
    required = family.get("term", {}).get("id")
    if "family" not in disabled and required and required not in record["families"]:
        return False
    req = selector.get("required_function", {}).get("term", {}).get("id")
    return "activity" in disabled or not req or req in record["molecular"]


def evaluate(records, condition="native_membrane", disabled=(), module=None):
    """Return supported capacity; false means missing compatible evidence only."""
    module = module or DOC["module"]
    index = {n["id"]: n for n in nodes(module)}
    annotons = {a["id"]: a for n in index.values() for a in n.get("annotons", [])}
    circuit = compile_node(module)
    disabled = set(disabled)
    groups = (
        [records]
        if "panel" in disabled
        else [
            [r for r in records if r["panel"] == org]
            for org in sorted({r["panel"] for r in records})
        ]
    )
    reports = []
    for group in groups:
        primary_panel = group[0]["panel"] if group else None
        facts = GATES.get(primary_panel, {})

        def taxon_ok(r):
            return "taxon" in disabled or r["taxon"] == GATES.get(r["panel"], {}).get(
                "taxon", r["taxon"]
            )

        def scalar_candidates(a, output=False):
            selector = a["participant"]
            function = a["function"]["term"]["id"]
            representatives = {
                x["term"]["id"].split(":", 1)[1]
                for x in selector.get("family", {}).get("representative_members", [])
            }
            return [
                r
                for r in group
                if taxon_ok(r)
                and match_selector(r, selector, disabled)
                and ("activity" in disabled or function in r["molecular"])
                and ("source" in disabled or r["accession"] in representatives)
                and (not output or "activity" in disabled or OUTPUT in r["processes"])
            ]

        def pump_holds(a):
            units = a["participant"]["protein_complex"]["active_units"]
            expected_roles = set("ABCF" if len(units) == 4 else "ABC")
            actual_families = {u["participant"]["family"]["term"]["id"] for u in units}
            # Independent biological contract, not merely mirroring declared units.
            if actual_families != {
                ROLE_FAMILIES["kdp" + role] for role in expected_roles
            }:
                return False
            assembly = "FABC" if "F" in expected_roles else "ABC"
            if "source" not in disabled:
                evidence = facts.get(assembly, {})
                if condition not in evidence.get("conditions", []):
                    return False
            assigned = []
            for unit in units:
                specific = unit.get("function", {}).get("term", {}).get("id")
                if unit["participant"]["family"]["term"]["id"] == ROLE_FAMILIES["kdpA"]:
                    specific = "GO:0030955"
                candidates = [
                    r
                    for r in group
                    if taxon_ok(r)
                    and match_selector(r, unit["participant"], disabled)
                    and (
                        "activity" in disabled
                        or (
                            PUMP in r["contributes"]
                            and COMPLEX in r["complexes"]
                            and (not specific or specific in r["molecular"])
                        )
                    )
                ]
                if not candidates:
                    return False
                assigned.append({r["instance"] for r in candidates})

            # Distinct physical subunits, not one broadly annotated protein.
            def injective(remaining, used):
                if not remaining:
                    return True
                return any(
                    injective(remaining[1:], used | {item})
                    for item in remaining[0] - used
                )

            return injective(assigned, set())

        def holds(atom):
            a = annotons[atom.node_id]
            if a["participant"]["selector_type"] == "PROTEIN_COMPLEX":
                return pump_holds(a)
            optional_function = a["function"]["term"]["id"]
            if optional_function in GATES["optional"]:
                return any(
                    "source" in disabled
                    or r["accession"] in GATES["optional"][optional_function]
                    for r in scalar_candidates(a)
                )
            caulo = atom.node_id.startswith("caulobacter_")
            profile = "caulobacter" if caulo else "canonical"
            if "source" not in disabled and profile not in facts:
                return False
            candidates = scalar_candidates(a, optional_function == DNA)
            if optional_function in {RECEIVER, DNA} and "polypeptide" not in disabled:
                candidates = [
                    r
                    for r in candidates
                    if {RECEIVER, DNA} <= set(r["molecular"])
                    and OUTPUT in r["processes"]
                ]
            return bool(candidates)

        atom_results = {a.node_id: holds(a) for a in iter_atoms(circuit)}
        reports.append(
            {
                "panel": primary_panel,
                "module": is_satisfied(circuit, holds),
                "transport": is_satisfied(
                    compile_node(index["kdp_transport_capacity"]), holds
                ),
                "regulatory": is_satisfied(
                    compile_node(index["kdp_regulatory_control"]), holds
                ),
                "atoms": atom_results,
            }
        )
    return {
        "module": any(r["module"] for r in reports),
        "transport": any(r["transport"] for r in reports),
        "regulatory": any(r["regulatory"] for r in reports),
        "groups": reports,
    }


CASES = []


def case(name, records, expected, condition="native_membrane", **kwargs):
    result = evaluate(records, condition, **kwargs)
    for endpoint, truth in expected.items():
        assert result[endpoint] == truth, (name, endpoint, truth, result)
    CASES.append(
        {
            "name": name,
            "condition": condition,
            "expected": expected,
            "input_instances": [r["instance"] for r in records],
            "result": result,
            "disabled_gates": list(kwargs.get("disabled", ())),
        }
    )
    return result


case("ecoli_FABC_canonical", panel("ECOLI"), {"module": True, "transport": True})
case(
    "ecoli_ABC_native_0.1mM",
    panel("ECOLI", {"kdpF"}),
    {"module": True},
    "native_membrane_0.1mM_K",
)
case(
    "ecoli_ABC_detergent_no_supported_capacity",
    panel("ECOLI", {"kdpF"}),
    {"module": False, "transport": False},
    "detergent",
)
case("psepk_inferred_FABC_canonical", panel("PSEPK"), {"module": True})
case(
    "psepk_ABC_no_dispensability_claim",
    panel("PSEPK", {"kdpF"}),
    {"module": False, "transport": False},
)
case("caulo_native_ABC_KdpE", panel("CAUVN"), {"module": True}, "native_low_K")
case(
    "caulo_without_cognate_D",
    panel("CAUVN", {"kdpD"}),
    {"module": True},
    "native_low_K",
)
case(
    "caulo_without_KdpE",
    panel("CAUVN", {"kdpE"}),
    {"module": False, "transport": True},
    "native_low_K",
)
case("lone_DESVH_B", panel("DESVH"), {"module": False, "transport": False})
case("Dgeo_ASK_only", panel("DEIGD"), {"module": False, "transport": False})
case("Staa_binding_only", panel("STAA8"), {"module": False, "transport": False})
case(
    "Ecoli_inhibitor_only",
    [r for r in panel("ECOLI") if r["gene"] == "kdpD"],
    {"module": False, "transport": False},
)
for gene, function in [("kdpA", "GO:0030955"), ("kdpB", "GO:0016887")]:
    deficient = panel("ECOLI")
    for record in deficient:
        if record["gene"] == gene:
            record["molecular"].remove(function)
    case(
        "missing_role_activity_" + gene,
        deficient,
        {"module": False, "transport": False},
    )

for role in "ABC":
    case(
        "missing_" + role,
        panel("ECOLI", {"kdp" + role}),
        {"module": False, "transport": False},
    )
case(
    "cross_panel_pump",
    panel("ECOLI", {"kdpB"}) + [r for r in panel("PSEPK") if r["gene"] == "kdpB"],
    {"module": False, "transport": False},
)
case(
    "cross_panel_regulator",
    panel("ECOLI", {"kdpE"}) + [r for r in panel("PSEPK") if r["gene"] == "kdpE"],
    {"module": False, "regulatory": False},
)
case(
    "short_Dgeo_cannot_fill_HK",
    panel("ECOLI", {"kdpD"}) + panel("DEIGD"),
    {"module": False, "transport": True},
)
for gene, replacement in [
    ("kdpB", ["NCBIfam:TIGR01494"]),
    ("kdpE", ["PANTHER:PTHR48111"]),
]:
    mutated = panel("ECOLI")
    for r in mutated:
        if r["gene"] == gene:
            r["families"] = replacement
    case("synthetic_generic_family_" + gene, mutated, {"module": False})
    case(
        "sensitivity_ignore_family_" + gene,
        mutated,
        {"module": True},
        disabled={"family"},
    )
mutated = panel("ECOLI")
for r in mutated:
    if r["gene"] == "kdpC":
        r["contributes"] = []
case("C_membership_without_contribution_evidence", mutated, {"module": False})
case("sensitivity_ignore_activity", mutated, {"module": True}, disabled={"activity"})
mutated = panel("ECOLI", {"kdpE"})
e = next(r for r in panel("ECOLI") if r["gene"] == "kdpE")
receiver, output = copy.deepcopy(e), copy.deepcopy(e)
receiver.update(instance="synthetic_receiver_fragment", molecular=[RECEIVER])
output.update(instance="synthetic_DNA_output_fragment", molecular=[DNA])
mutated.extend([receiver, output])
case("split_receiver_and_output", mutated, {"module": False, "regulatory": False})
case(
    "sensitivity_ignore_same_polypeptide",
    mutated,
    {"module": True},
    disabled={"polypeptide"},
)
case(
    "sensitivity_remove_ABC_source_gate",
    panel("PSEPK", {"kdpF"}),
    {"module": True},
    disabled={"source"},
)
case(
    "sensitivity_allow_cross_panel",
    panel("ECOLI", {"kdpB"}) + [r for r in panel("PSEPK") if r["gene"] == "kdpB"],
    {"module": True},
    disabled={"panel"},
)
mutated = panel("ECOLI")
for r in mutated:
    if r["gene"] == "kdpB":
        r["taxon"] = "NCBITaxon:160488"
case("synthetic_taxon_mismatch", mutated, {"module": False})
case("sensitivity_ignore_taxon", mutated, {"module": True}, disabled={"taxon"})

# Explicit optional-step specificity: neither family identity nor an output sign
# creates an unmeasured ligand-binding function or mandatory kinase requirement.
optional_checks = {}
for organism, positive, negative in [
    (
        "DEIGD",
        {"kdpd_serine_inhibition_activity"},
        {"kdpd_sensor_kinase", "staphylococcal_kdpd_cdiamp_binding_activity"},
    ),
    (
        "STAA8",
        {"staphylococcal_kdpd_cdiamp_binding_activity"},
        {"kdpd_serine_inhibition_activity"},
    ),
    (
        "PSEPK",
        set(),
        {"kdpd_serine_inhibition_activity", "kdpd_kdpe_dephosphorylation_activity"},
    ),
    (
        "CAUVN",
        {"kdpd_kdpe_dephosphorylation_activity"},
        {"kdpd_serine_inhibition_activity"},
    ),
]:
    outcome = evaluate(
        panel(organism), "native_low_K" if organism == "CAUVN" else "native_membrane"
    )
    atoms = outcome["groups"][0]["atoms"]
    assert all(atoms[name] for name in positive), organism
    assert not any(atoms[name] for name in negative), organism
    optional_checks[organism] = {
        "present": sorted(positive),
        "not_asserted": sorted(negative),
    }

# Module mutations test that the independent ABC contract catches an omitted role.
structural_mutations = []
for removed_role in "ABC":
    mutated_module = copy.deepcopy(DOC["module"])
    for n in nodes(mutated_module):
        for a in n.get("annotons", []):
            complex_ = a.get("participant", {}).get("protein_complex")
            if complex_:
                complex_["active_units"] = [
                    u
                    for u in complex_["active_units"]
                    if u["participant"]["family"]["term"]["id"]
                    != ROLE_FAMILIES["kdp" + removed_role]
                ]
    outcome = evaluate(panel("ECOLI"), "native_membrane_0.1mM_K", module=mutated_module)
    assert not outcome["module"]
    structural_mutations.append(
        {"removed_declared_role": removed_role, "module": outcome["module"]}
    )

# A deliberately weak activity-only oracle exposes compiler/oracle separation.
weak_inventory = panel("DESVH")
weak_functions = set().union(
    *(set(r["molecular"]) | set(r["contributes"]) for r in weak_inventory)
)
pump_node = next(n for n in nodes(DOC["module"]) if n["id"] == "kdp_transport_capacity")
weak_lone_b_transport = is_satisfied(
    compile_node(pump_node), lambda atom: set(atom.function_ids) <= weak_functions
)
assert weak_lone_b_transport is True

# Optional inhibition is a state overlay. Monotone assembled-capacity logic cannot
# infer active flux or encode measured inhibition by merely adding a gene.
base = evaluate(panel("ECOLI"))
assert base["module"]
state_test = {
    "assembled_capacity": base["module"],
    "active_flux_claim": "inhibited under measured KdpB serine-phosphorylation conditions",
    "source": "PMID:38622146",
    "universality": "not transferred to untested panels",
}

# Source excerpts and every gate citation must resolve; hash actual inspected inputs.
for value in QUOTES.values():
    path = ROOT / value["path"]
    READ.add(path)
    assert re.sub(r"\s+", " ", value["supporting_text"]) in re.sub(
        r"\s+", " ", path.read_text()
    )
for group in GATES.values():
    for fact in group.values():
        if isinstance(fact, dict):
            for source in fact.get("sources", []):
                if source not in QUOTES:
                    path = ROOT / source
                    assert path.exists(), source
                    READ.add(path)
for function in GATES["optional"].values():
    for fact in function.values():
        path = ROOT / fact["source"]
        assert path.exists()
        READ.add(path)
# Independently reproduce the target-to-assayed-strain protein sequence bridge.
bridge_root = (
    ROOT
    / "analysis/module_audits/bacterial_kdp_potassium_homeostasis/regulatory-comparators"
)
donor_path = bridge_root / "A0A0H2XIE2.json"
bridge_path = bridge_root / "staa8-sequence-comparison.json"
READ.update({donor_path, bridge_path})
donor = json.loads(donor_path.read_text())
bridge = json.loads(bridge_path.read_text())
target_text = (ROOT / "genes/STAA8/kdpD/kdpD-uniprot.txt").read_text()
target_sequence = re.sub(
    r"[^A-Z]",
    "",
    target_text.split("SQ   SEQUENCE", 1)[1].split("\n", 1)[1].split("//", 1)[0],
)
assert donor["primaryAccession"] == bridge["donor"] == "A0A0H2XIE2"
assert target_sequence == donor["sequence"]["value"]
assert len(target_sequence) == 885
assert hashlib.sha256(target_sequence.encode()).hexdigest() == bridge["sequence_sha256"]

# Regulatory signs and scope are checked from the actual module edge, not assumed
# from the shared KdpD family name or a ligand-response assay.
staa_edge = next(
    e
    for e in DOC["module"]["connections"]
    if e["source"] == "staphylococcal_kdpd_cdiamp_binding"
)
assert staa_edge["connection_type"] == "NEGATIVELY_REGULATES"
assert staa_edge["target"] == "canonical_kdpde_control"
assert any(t["term"]["id"] == "NCBITaxon:1280" for t in staa_edge["context"]["taxa"])
assert "autokinase" in staa_edge["description"]
assert (
    "GO:0180001"
    not in next(r for r in RECORDS if r["accession"] == "Q1J2K3")["molecular"]
)
release_checks = {}
release_archive = AUDIT / "frozen-input-releases.json"
READ.add(release_archive)
for consultation, frozen in json.loads(release_archive.read_text()).items():
    manifest = frozen["manifest"]
    for rel, expected in manifest["files"].items():
        assert hashlib.sha256((ROOT / rel).read_bytes()).hexdigest() == expected, rel
    release_checks[consultation] = {
        "sha256": frozen["sha256"],
        "unchanged_files": len(manifest["files"]),
    }
(AUDIT / "release-receipt.json").write_text(json.dumps(release_checks, indent=2) + "\n")
(AUDIT / "boundary-snapshot.json").write_text(
    json.dumps(
        {
            "module_id": DOC["module"]["id"],
            "notes": DOC["notes"],
            "required_parts": [
                p["node"]["id"] for p in DOC["module"]["parts"] if not p.get("optional")
            ],
            "optional_parts": [
                p["node"]["id"] for p in DOC["module"]["parts"] if p.get("optional")
            ],
            "variant_sets": [
                v for n in nodes(DOC["module"]) for v in n.get("variant_sets", [])
            ],
            "connections": DOC["module"]["connections"],
        },
        indent=2,
    )
    + "\n"
)

# Hash the frozen comparator proof and all directly referenced provenance files.
for rel in [
    "genes/DEIGD/Dgeo_2852/Dgeo_2852-source-analysis/construct-scope.md",
    "genes/DEIGD/Dgeo_2852/Dgeo_2852-source-analysis/provenance.json",
    "genes/STAA8/kdpD/kdpD-notes.md",
    "analysis/module_audits/bacterial_kdp_potassium_homeostasis/regulatory-comparators/handoff.json",
]:
    p = ROOT / rel
    if p.exists():
        READ.add(p)
READ.update(
    {
        AUDIT / "evidence-gates.json",
        AUDIT / "source-quotes.json",
        Path(__file__).resolve(),
    }
)
for family in ["PTHR30607", "PTHR43743", "PTHR30042", "PTHR45569", "PTHR48111"]:
    READ.add(ROOT / "interpro/panther" / family / (family + "-review.yaml"))
circuit = compile_node(DOC["module"])
result = {
    "optional_checks": optional_checks,
    "structural_mutations": structural_mutations,
    "weak_activity_only_lone_B_transport": weak_lone_b_transport,
    "cases": CASES,
    "case_count": len(CASES),
    "state_overlay": state_test,
    "core_atoms": [a.node_id for a in core_atoms(circuit)],
    "compiled_atoms": [asdict(a) for a in iter_atoms(circuit)],
    "input_records": RECORDS,
    "input_hashes": {
        str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest()
        for p in sorted(READ)
    },
}
(AUDIT / "results.json").write_text(json.dumps(result, indent=2) + "\n")
print(
    json.dumps(
        {
            "cases_passed": len(CASES),
            "compiled_atoms": len(result["compiled_atoms"]),
            "core_atoms": result["core_atoms"],
            "input_files": len(READ),
        }
    )
)
