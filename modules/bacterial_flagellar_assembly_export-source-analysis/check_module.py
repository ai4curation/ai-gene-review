"""Check curated assembly/stator distinctions using the production module compiler.

These checks cover represented components, not genome-level sufficiency. External
assembly prerequisites and experimental exceptions are documented in the contract.
"""

from copy import deepcopy
from itertools import combinations
from pathlib import Path
import json

import yaml

from ai_gene_review.module_logic import (
    compile_module,
    compile_node,
    is_satisfied,
    iter_atoms,
)

ROOT = Path(__file__).resolve().parents[2]
MODULE = ROOT / "modules/bacterial_flagellar_assembly_export.yaml"
OUTPUT = (
    ROOT
    / "analysis/module_audits/bacterial_flagellar_assembly_export/capacity-results.json"
)


def covers(circuit, proteins):
    """Only exact reviewed members establish the represented role in these checks."""
    return is_satisfied(circuit, lambda atom: bool(set(atom.uniprots) & set(proteins)))


def run_checks(doc):
    parts = {p["node"]["id"]: p["node"] for p in doc["module"]["parts"]}
    root = compile_module(doc)
    stator = compile_node(parts["motab_stator_installation"])
    late = compile_node(parts["flagellar_late_transcription"])
    export = compile_node(parts["flagellar_type_iii_export"])
    # Independent native identities, verified from raw records and PMID36409076.
    required_psepk = {
        "Q88EV8",
        "Q88EU8",
        "Q88EV1",
        "Q88EU9",
        "Q88EV0",
        "Q88ET7",
        "Q88ET6",
        "Q88ET8",
        "Q88ET4",
        "Q88ET5",
        "Q88EU5",
        "Q88EU6",
        "Q88ER8",
        "Q88ER2",
        "Q88ER3",
        "Q88ER7",
        "Q88ER4",
        "Q88ER5",
        "Q88EU2",
        "Q88ES2",
        "Q88ES5",
        "Q88ES3",
        "Q88ES7",
    }
    motab = {"Q88DC2", "Q88DC3"}
    motcd = {"Q88EW6", "Q88EW7"}
    pomab = {"O06873", "O06874"}
    pairs = [motab, motcd, pomab]
    results = []

    def check(name, actual, expected, source):
        assert actual == expected, (name, actual, expected)
        results.append(
            {"case": name, "observed": actual, "expected": expected, "source": source}
        )

    # Native assisted configuration coverage, not a biological impossibility claim
    # for deletions: suppressors/reconstitution can supply different realizations.
    check(
        "represented_assembly_without_stators",
        covers(root, required_psepk),
        True,
        "PMID:39766194",
    )
    check(
        "FlgM_deletion_does_not_block_component_coverage",
        covers(root, required_psepk | {"Q88EW1"}),
        True,
        "PMID:10972838",
    )
    check(
        "complete_PSEPK_represented_components",
        covers(root, required_psepk | motab | motcd | {"Q88EW1", "Q88EQ8"}),
        True,
        "PMID:36409076",
    )
    for protein in sorted(required_psepk):
        check(
            "missing_represented_native_assisted_role_" + protein,
            covers(root, required_psepk - {protein}),
            False,
            "PMID:39766194; PMID:21934659",
        )
    check("FliA_without_inhibitor", covers(late, {"Q88EW1"}), True, "PMID:10972838")
    check(
        "FliA_with_checkpoint_inhibitor",
        covers(late, {"Q88EW1", "Q88EQ8"}),
        True,
        "PMID:10972838",
    )
    check(
        "FlgM_is_not_a_positive_sigma_factor",
        covers(late, {"Q88EQ8"}),
        False,
        "PMID:10972838",
    )
    check(
        "no_native_transcription_configuration",
        covers(late, set()),
        False,
        "PMID:34859548",
    )
    export_members = {a.uniprots[0] for a in iter_atoms(export)}
    check(
        "normal_assisted_export_configuration",
        covers(export, export_members),
        True,
        "PMID:21934659",
    )
    check(
        "FliHI_bypass_is_not_the_normal_assisted_configuration",
        covers(export, export_members - {"Q88ET6", "Q88ET7"}),
        False,
        "PMID:18216858",
    )
    check(
        "isolated_FliI_is_not_an_export_apparatus",
        covers(export, {"P26465"}),
        False,
        "PMID:29946050",
    )
    check(
        "family_label_is_not_a_reviewed_export_member",
        covers(export, {"PANTHER:PTHR15184:SF81"}),
        False,
        "PMID:24064315",
    )
    # Exhaustively discriminate three complete pairs from every mixed/single set.
    subunits = sorted(set.union(*pairs))
    for size in range(len(subunits) + 1):
        for subset in combinations(subunits, size):
            expected = any(pair <= set(subset) for pair in pairs)
            check(
                "matched_stator_subset_" + ("_".join(subset) or "empty"),
                covers(stator, subset),
                expected,
                "PMID:36409076; PMID:18326582",
            )
    check(
        "broad_MotA_MotB_family_hits_do_not_establish_native_pair",
        covers(stator, {"PANTHER:PTHR30433", "PANTHER:PTHR30329"}),
        False,
        "PMID:39766194",
    )

    # The actual pair can be covered while its ion/species endpoint is unsupported.
    # This additional oracle is necessary because the compiler does not evaluate context.
    def native_stator(proteins, background, ion):
        if not covers(stator, proteins):
            return "NOT_ESTABLISHED"
        if (
            background == "PSEPK"
            and ion == "H+"
            and any(p <= set(proteins) for p in [motab, motcd])
        ):
            return "SUPPORTED_WITH_INFERRED_ION_COUPLING"
        if background == "VIBAL" and ion == "Na+" and pomab <= set(proteins):
            return "SUPPORTED_BY_NATIVE_AND_STRUCTURAL_ASSAYS"
        return "NOT_ESTABLISHED"

    for label, proteins, background, ion, expected in [
        (
            "MotAB_native_H",
            motab,
            "PSEPK",
            "H+",
            "SUPPORTED_WITH_INFERRED_ION_COUPLING",
        ),
        (
            "MotCD_native_H",
            motcd,
            "PSEPK",
            "H+",
            "SUPPORTED_WITH_INFERRED_ION_COUPLING",
        ),
        (
            "PomAB_native_Na",
            pomab,
            "VIBAL",
            "Na+",
            "SUPPORTED_BY_NATIVE_AND_STRUCTURAL_ASSAYS",
        ),
        ("PomAB_H_not_established", pomab, "VIBAL", "H+", "NOT_ESTABLISHED"),
        ("MotAB_Na_not_established", motab, "PSEPK", "Na+", "NOT_ESTABLISHED"),
        (
            "PomAB_PSEPK_transfer_not_established",
            pomab,
            "PSEPK",
            "Na+",
            "NOT_ESTABLISHED",
        ),
        (
            "MotAB_Vibrio_transfer_not_established",
            motab,
            "VIBAL",
            "H+",
            "NOT_ESTABLISHED",
        ),
        (
            "FlhA_sodium_export_is_not_PomAB_torque",
            {"P40729"},
            "VIBAL",
            "Na+",
            "NOT_ESTABLISHED",
        ),
    ]:
        check(
            label,
            native_stator(proteins, background, ion),
            expected,
            "PMID:36409076; PMID:39793043; PMID:26943926",
        )
    return results


def main():
    doc = yaml.safe_load(MODULE.read_text())
    results = run_checks(doc)
    mutations = []
    # Wrong biological interpretations must fail the same independent cases.
    for name in [
        "require_stator_for_assembly",
        "require_FlgM_for_FliA",
        "require_all_stator_pairs",
        "omit_FliQ_from_normal_gate",
    ]:
        bad = deepcopy(doc)
        parts = {p["node"]["id"]: p for p in bad["module"]["parts"]}
        if name == "require_stator_for_assembly":
            parts["motab_stator_installation"]["optional"] = False
        elif name == "require_FlgM_for_FliA":
            parts["flagellar_late_transcription"]["node"]["parts"][0]["optional"] = (
                False
            )
        elif name == "require_all_stator_pairs":
            n = parts["motab_stator_installation"]["node"]
            variants = n.pop("variant_sets")[0]["variants"]
            n["parts"] = [{"node": v} for v in variants]
        else:
            n = parts["flagellar_type_iii_export"]["node"]
            n["annotons"] = [a for a in n["annotons"] if a["id"] != "fliq_export_gate"]
        try:
            run_checks(bad)
        except AssertionError as error:
            mutations.append(
                {"mutation": name, "detected": True, "failed_case": str(error)}
            )
        else:
            raise AssertionError("Undetected mutation: " + name)
    output = {
        "status": "PASS",
        "cases": len(results),
        "mutation_cases": len(mutations),
        "limits": [
            "Production compiler coverage is not proof of complete native flagellum sufficiency.",
            "Unrepresented FliE/envelope/chaperone/substrate/energy prerequisites must be supplied and justified externally.",
            "NOT_ESTABLISHED describes the curated evidence boundary, not biological absence or impossible engineering.",
            "Normal assisted export coverage excludes documented FliHI bypass configurations without denying their activity.",
            "These tests cannot replace review of the biological assertions or source-specific conditions.",
        ],
        "results": results,
        "mutations": mutations,
    }
    OUTPUT.write_text(json.dumps(output, indent=2) + "\n")
    print(
        f"PASS: {len(results)} source-scoped cases, {len(mutations)} detected mechanism mutations"
    )


if __name__ == "__main__":
    main()
