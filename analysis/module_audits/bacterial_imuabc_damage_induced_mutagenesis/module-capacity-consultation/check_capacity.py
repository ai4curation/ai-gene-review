"""Exercise production module logic with a bounded, source-backed member oracle.

Run from any directory with the repository environment. Synthetic counterfactuals
are controls, not new assertions about the biological proteins.
"""

import copy
import hashlib
import json
import re
from pathlib import Path

import yaml

from ai_gene_review.module_logic import compile_node, core_atoms, is_satisfied, iter_atoms

AUDIT = Path(__file__).resolve().parent
ROOT = AUDIT.parents[3]
ACCESSORIES = {
    "imua_accessory_protein", "imua_prime_accessory_protein", "myxococcus_imua_atpase"
}
EFFECTORS = ACCESSORIES | {"imub_accessory_protein", "dnae2_polymerase"}
OPTIONAL = {"reca_damage_sensor", "lexa_cassette_repressor"}


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def family_ids(raw):
    """Use frozen external database cross-references, not names or GO rows."""
    result = set()
    for line in raw.splitlines():
        if not line.startswith("DR   "):
            continue
        fields = [part.strip() for part in line[5:].split(";")]
        if len(fields) >= 2 and fields[0] in {"InterPro", "Pfam", "PANTHER"}:
            result.add(f"{fields[0]}:{fields[1]}")
    return result


def load_carriers(ledger):
    carriers = {}
    for accession, item in ledger["roles"].items():
        doc = yaml.safe_load((ROOT / item["review"]).read_text())
        assert doc["id"] == accession
        assert doc["taxon"]["id"] == item["taxon"]
        carriers[accession] = {
            "status": doc["status"],
            "taxon": doc["taxon"]["id"],
            "families": family_ids((ROOT / item["raw"]).read_text()),
            "cores": [
                {
                    "functions": {
                        core[slot]["id"]
                        for slot in ("molecular_function", "contributes_to_molecular_function")
                        if core.get(slot)
                    },
                    "processes": {term["id"] for term in core.get("directly_involved_in", [])},
                    "supported": bool(core.get("supported_by")),
                }
                for core in doc.get("core_functions", [])
            ],
        }
    return carriers


def oracle(atom, present, panel_name, ledger, carriers):
    """Require reviewed activity, actual membership and a compatible evidence panel."""
    panel = ledger["panels"].get(panel_name) or ledger.get("single_member_contexts", {}).get(panel_name)
    if panel is None:
        return False
    context_members = set(panel["members"] + panel["optional_context"])
    for accession in present & context_members & set(atom.uniprots):
        proof = ledger["roles"].get(accession)
        protein = carriers.get(accession)
        if not proof or not protein or proof["role"] != atom.node_id:
            continue
        if protein["status"] != "COMPLETE" or protein["taxon"] != panel["context_taxon"]:
            continue
        if atom.family_ids and not set(atom.family_ids) & protein["families"]:
            continue
        for core in protein["cores"]:
            if not core["supported"] or not set(atom.function_ids) <= core["functions"]:
                continue
            if atom.node_id in EFFECTORS:
                if not core["processes"] & set(ledger["approved_tls_core_terms"]):
                    continue
            return True
    return False


def main():
    ledger = yaml.safe_load((AUDIT / "evidence-ledger.yaml").read_text())
    ancestry = json.loads((ROOT / ledger["tls_hierarchy_source"]).read_text())
    assert "GO:0019985" in ancestry["0042276"]["data"]["results"][0]["ancestors"]
    for panel in list(ledger["panels"].values()) + list(ledger.get("single_member_contexts", {}).values()):
        publication = ROOT / "publications" / (panel["reference"].replace(":", "_") + ".md")
        assert re.sub(r"\s+", " ", panel["quote"]) in re.sub(r"\s+", " ", publication.read_text())
    module_path = ROOT / ledger["module"]
    document = yaml.safe_load(module_path.read_text())
    circuit = compile_node(document["module"], ROOT / "modules")
    atoms = {atom.node_id: atom for atom in iter_atoms(circuit)}
    # Fail visibly if module integration changes the audited role structure.
    assert set(atoms) == EFFECTORS | OPTIONAL, set(atoms)
    assert {atom.node_id for atom in core_atoms(circuit)} == {
        "imub_accessory_protein", "dnae2_polymerase"
    }
    assert atoms["imub_accessory_protein"].function_ids == ("GO:0030674",)
    assert atoms["dnae2_polymerase"].function_ids == ("GO:0003887",)
    assert atoms["myxococcus_imua_atpase"].function_ids == ("GO:0016887",)
    carriers = load_carriers(ledger)
    results = []

    def case(name, present, panel, expected, reason, modified=None, altered_ledger=None):
        evidence = altered_ledger or ledger
        proteins = modified if modified is not None else carriers
        held = {
            key for key, atom in atoms.items()
            if oracle(atom, set(present), panel, evidence, proteins)
        }
        actual = is_satisfied(circuit, lambda atom: atom.node_id in held)
        results.append({
            "name": name, "panel": panel, "present": sorted(present),
            "expected": expected, "actual": actual, "held_atoms": sorted(held),
            "reason": reason,
        })
        assert actual == expected, (name, held, expected)

    # Expectations come from three independently characterized cassette panels.
    for name, panel in ledger["panels"].items():
        members = panel["members"]
        case(f"{name}_complete_without_regulators", members, name, True,
             "Evidence-backed effector capacity; native induction is not tested by this Boolean result.")
        for omitted in members:
            case(f"{name}_missing_{omitted}", set(members) - {omitted}, name, False,
                 "Each accessory/adaptor/polymerase role is required by the characterized cassette.")
            case(f"{name}_only_{omitted}", {omitted}, name, False,
                 "A single characterized component does not establish full cassette capacity.")
        case(f"{name}_no_cassette_evidence", members, None, False,
             "Same-taxon co-occurrence and individual annotations do not establish the joint mechanism.")
        incomplete = copy.deepcopy(carriers)
        for accession in members:
            incomplete[accession]["cores"] = []
        case(f"{name}_family_hits_only", members, name, False,
             "Actual family membership without supported reviewed core roles cannot grant capacity.",
             modified=incomplete)
    p = ledger["panels"]["PSEPK"]
    for optional in [p["optional_context"], ["Q88ME4"], ["P59479"]]:
        case("PSEPK_with_" + "_".join(optional), p["members"] + optional, "PSEPK", True,
             "Optional induction context must neither supply nor block a required effector role.")
    case("only_RecA_LexA", p["optional_context"], "PSEPK", False,
         "Signaling/repression is not the three-component lesion-bypass machinery.")
    case("empty", [], "PSEPK", False, "No empty route may satisfy the required effector machinery.")
    case("mixed_three_taxa", ["Q88I84", "Q9A3J2", "P9WNT5"], "PSEPK", False,
         "Cross-species compatibility is unestablished, not biologically disproved.")
    case("MYCTU_wrong_accessory", ["Q88I84", "O50419", "P9WNT5"], "MYCTU", False,
         "A proteobacterial accessory cannot be substituted on family label alone.")
    case("RecA_cannot_replace_ImuA", ["Q88ME4", "Q88I83", "Q88I82"], "PSEPK", False,
         "DNA binding and ATP-dependent activity do not establish the required accessory role.")
    case("extra_heterologous_accessory", p["members"] + ["P9WKZ9"], "PSEPK", True,
         "A valid matched cassette does not require the alternative accessory to be absent.")
    for accession in p["members"]:
        altered = copy.deepcopy(carriers)
        altered[accession]["status"] = "INITIALIZED"
        case(f"unreviewed_{accession}", p["members"], "PSEPK", False,
             "A scaffold and its family hits are not a completed biological assessment.", modified=altered)
        altered = copy.deepcopy(carriers)
        for core in altered[accession]["cores"]:
            core["supported"] = False
        case(f"unsupported_core_{accession}", p["members"], "PSEPK", False,
             "A bare core label without evidence is insufficient.", modified=altered)
    for accession in ["Q88I83", "Q88I82"]:
        altered = copy.deepcopy(carriers)
        for core in altered[accession]["cores"]:
            core["functions"] = set()
        case(f"missing_required_MF_{accession}", p["members"], "PSEPK", False,
             "Process participation cannot replace the explicit adaptor/polymerase requirement.",
             modified=altered)
    altered = copy.deepcopy(carriers)
    for core in altered["Q88I83"]["cores"]:
        core["functions"] = {"GO:0003887"}
    case("polymerase_cannot_replace_adaptor", p["members"], "PSEPK", False,
         "A catalytic polymerase claim cannot fill the noncatalytic ImuB adaptor requirement.",
         modified=altered)
    altered = copy.deepcopy(carriers)
    altered["Q88I82"]["families"] = {"PANTHER:PTHR32294"}
    case("generic_type_C_polymerase", p["members"], "PSEPK", False,
         "A generic family and polymerase MF do not identify DnaE2; role-specific membership is required.",
         modified=altered)
    altered = copy.deepcopy(carriers)
    altered["Q88I84"]["families"] = {"PANTHER:PTHR35369"}
    case("generic_SulA_related_family", p["members"], "PSEPK", False,
         "A mixed SulA/ImuA/ImuB family is not proof of the ImuA accessory role.", modified=altered)
    altered = copy.deepcopy(carriers)
    for core in altered["Q88I84"]["cores"]:
        core["processes"] = set()
        core["functions"] = {"GO:0005524", "GO:0003677"}
    case("ATP_DNA_binding_without_accessory_role", p["members"], "PSEPK", False,
         "Isolated nucleotide/DNA activity does not establish ImuA cassette participation.", modified=altered)
    altered = copy.deepcopy(carriers)
    altered["Q88I83"]["taxon"] = "NCBITaxon:83332"
    case("mismatched_taxon_metadata", p["members"], "PSEPK", False,
         "A named member cannot bypass the actual target-taxon check.", modified=altered)
    altered_ledger = copy.deepcopy(ledger)
    del altered_ledger["roles"]["Q88I83"]
    case("unassessed_role_despite_membership", p["members"], "PSEPK", False,
         "A module representative and matching family do not replace independent role assessment.",
         altered_ledger=altered_ledger)

    isolated = ledger["single_member_contexts"]["MYXXD_accessory_only"]["members"]
    assert len(isolated) == 1
    assert oracle(atoms["myxococcus_imua_atpase"], set(isolated), "MYXXD_accessory_only",
                  ledger, carriers)
    case("verified_Myxococcus_accessory_is_not_complete_cassette", isolated,
         "MYXXD_accessory_only", False,
         "Verified accessory identity and measured ATP hydrolysis do not provide ImuB and DnaE2.")
    case("Myxococcus_with_heterologous_PSEPK_partners", isolated + ["Q88I83", "Q88I82"],
         "MYXXD_accessory_only", False,
         "An isolated protein assay does not establish cross-species partner compatibility.")
    altered = copy.deepcopy(carriers)
    for core in altered[isolated[0]]["cores"]:
        core["functions"] = {"GO:0005524"}
    assert not oracle(atoms["myxococcus_imua_atpase"], set(isolated), "MYXXD_accessory_only",
                      ledger, altered)
    assert set(atoms["reca_damage_sensor"].family_ids) & carriers[isolated[0]]["families"]
    assert not oracle(atoms["reca_damage_sensor"], set(isolated), "MYXXD_accessory_only",
                      ledger, carriers)

    # Direct production-compiler probes expose rather than hide its limitations.
    logical_cases = []
    for name, held, expected in [
        ("ImuA_route", {"imua_accessory_protein", "imub_accessory_protein", "dnae2_polymerase"}, True),
        ("ImuAprime_route", {"imua_prime_accessory_protein", "imub_accessory_protein", "dnae2_polymerase"}, True),
        ("Myxococcus_accessory_route", {"myxococcus_imua_atpase", "imub_accessory_protein", "dnae2_polymerase"}, True),
        ("both_accessories", EFFECTORS, True),
        ("neither_accessory", {"imub_accessory_protein", "dnae2_polymerase"}, False),
        ("no_polymerase", ACCESSORIES | {"imub_accessory_protein"} | OPTIONAL, False),
        ("no_adaptor", ACCESSORIES | {"dnae2_polymerase"} | OPTIONAL, False),
    ]:
        actual = is_satisfied(circuit, lambda atom: atom.node_id in held)
        assert actual == expected, name
        logical_cases.append({"name": name, "expected": expected, "actual": actual})
    mixed = {"Q88I84", "Q9A3J2", "P9WNT5"}
    naive = is_satisfied(circuit, lambda atom: bool(set(atom.uniprots) & mixed))
    assert naive  # Deliberate positive demonstration of a naive-oracle failure.
    protected = json.loads((AUDIT / "input-preservation.json").read_text())
    for path, expected in protected.items():
        assert digest(ROOT / path) == expected, path
    report = {
        "status": "PASS", "capacity_cases": results, "compiler_cases": logical_cases,
        "case_count": len(results) + len(logical_cases) + 4,
        "isolated_accessory_controls": {
            "verified_Myxococcus_ATPase_role": True,
            "ATP_binding_alone_cannot_fill_hydrolysis_role": True,
            "same_RecA_family_ImuA_does_not_grant_damage_sensor": True,
        },
        "naive_mixed_taxon_oracle_accepts": naive,
        "compiler_limits": ledger["limits"],
        "reviewed_inputs_unchanged": len(protected),
        "reviewed_genes": len(carriers),
        "module_sha256": digest(module_path),
        "compiler_sha256": digest(ROOT / "src/ai_gene_review/module_logic.py"),
        "evidence_ledger_sha256": digest(AUDIT / "evidence-ledger.yaml"),
    }
    (AUDIT / "capacity-results.json").write_text(json.dumps(report, indent=2) + "\n")
    print(f"PASS: {report['case_count']} cases; {len(protected)} source/review inputs unchanged")


if __name__ == "__main__":
    main()
