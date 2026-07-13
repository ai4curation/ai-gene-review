#!/usr/bin/env python3
"""First-pass curation for the ppu02010 PP_3828-PP_3830 ModABC importer."""

from __future__ import annotations

from copy import deepcopy
from pathlib import Path

import yaml


SPECIES = "PSEPK"


def goa_ref(gene: str) -> str:
    return f"file:{SPECIES}/{gene}/{gene}-goa.tsv"


def uniprot_ref(gene: str) -> str:
    return f"file:{SPECIES}/{gene}/{gene}-uniprot.txt"


def asta_ref(gene: str) -> str:
    return f"file:{SPECIES}/{gene}/{gene}-deep-research-asta.md"


def support_goa(gene: str, term_id: str, label: str) -> dict:
    return {"reference_id": goa_ref(gene), "supporting_text": f"{term_id}\t{label}"}


def support_uniprot(gene: str, text: str) -> dict:
    return {"reference_id": uniprot_ref(gene), "supporting_text": text}


def support_asta(gene: str, text: str) -> dict:
    return {"reference_id": asta_ref(gene), "supporting_text": text}


def ensure_reference(doc: dict, ref_id: str, title: str, supporting_text: str | None = None) -> None:
    refs = doc.setdefault("references", [])
    for ref in refs:
        if ref.get("id") == ref_id:
            if supporting_text and not ref.get("findings"):
                ref["findings"] = [{"supporting_text": supporting_text}]
            return
    ref = {"id": ref_id, "title": title, "findings": []}
    if supporting_text:
        ref["findings"].append({"supporting_text": supporting_text})
    refs.append(ref)


def review(
    gene: str,
    term_id: str,
    label: str,
    summary: str,
    action: str,
    reason: str,
    *,
    proposed: list[dict] | None = None,
    extra_support: list[dict] | None = None,
) -> dict:
    supported_by = [support_goa(gene, term_id, label)]
    if extra_support:
        supported_by.extend(extra_support)
    result = {
        "summary": summary,
        "action": action,
        "reason": reason,
        "supported_by": supported_by,
    }
    if proposed:
        result["proposed_replacement_terms"] = deepcopy(proposed)
    return result


def new_annotation(
    term: dict,
    qualifier: str,
    original_reference_id: str,
    summary: str,
    reason: str,
    supported_by: list[dict],
) -> dict:
    return {
        "term": deepcopy(term),
        "evidence_type": "IEA",
        "original_reference_id": original_reference_id,
        "qualifier": qualifier,
        "review": {
            "summary": summary,
            "action": "NEW",
            "reason": reason,
            "supported_by": supported_by,
        },
    }


MOLYBDATE_TRANSPORT = {"id": "GO:0015689", "label": "molybdate ion transport"}
MOLYBDATE_BINDING = {"id": "GO:0030973", "label": "molybdate ion binding"}
TUNGSTATE_BINDING = {"id": "GO:1901359", "label": "tungstate binding"}
MOLYBDATE_TRANSPORTER = {
    "id": "GO:0015098",
    "label": "molybdate ion transmembrane transporter activity",
}
ABC_MOLYBDATE_TRANSPORTER = {
    "id": "GO:0015412",
    "label": "ABC-type molybdate transporter activity",
}
ATP_BINDING = {"id": "GO:0005524", "label": "ATP binding"}
ATP_HYDROLYSIS = {"id": "GO:0016887", "label": "ATP hydrolysis activity"}
ABC_COMPLEX = {
    "id": "GO:0043190",
    "label": "ATP-binding cassette (ABC) transporter complex",
}
PLASMA_MEMBRANE = {"id": "GO:0005886", "label": "plasma membrane"}
PERIPLASM = {"id": "GO:0030288", "label": "outer membrane-bounded periplasmic space"}


GENES = {
    "modA": {
        "kind": "binding",
        "description": (
            "modA encodes the periplasmic molybdate-binding component of the "
            "PP_3828-PP_3830 ModABC uptake system. Its signal peptide, ModA "
            "solute-binding family assignment, and GOA molybdate-binding and "
            "transport annotations support a substrate-recognition role for "
            "molybdate import, with tungstate binding retained as a secondary "
            "family-supported ligand lead."
        ),
        "uniprot_text": "Full=Molybdate-binding periplasmic protein",
        "asta_text": "Protein Description:** SubName: Full=Molybdate-binding periplasmic protein",
        "signal_text": "FT   SIGNAL          1..24",
        "family_text": "Belongs to the bacterial solute-binding protein ModA",
        "panther_text": "PANTHER; PTHR30632; MOLYBDATE-BINDING PERIPLASMIC PROTEIN; 1.",
        "subunit_text": "The complex is composed of two ATP-binding proteins (ModC),",
    },
    "modB": {
        "kind": "permease",
        "description": (
            "modB encodes the multi-pass inner-membrane permease component of "
            "the PP_3828-PP_3830 ModABC molybdate uptake system. UniProt places "
            "it in a binding-protein-dependent transport system for molybdenum "
            "and identifies it as the substrate-translocation component."
        ),
        "uniprot_text": "Full=Molybdenum transport system permease",
        "asta_text": "Protein Description:** RecName: Full=Molybdenum transport system permease",
        "function_text": "molybdenum; probably responsible for the translocation of the substrate",
        "family_text": "Belongs to the binding-protein-dependent transport system",
        "domain_text": "FT   DOMAIN          11..217",
    },
    "modC": {
        "kind": "atpase",
        "description": (
            "modC encodes the ATP-binding energy-coupling subunit of the "
            "PP_3828-PP_3830 ModABC molybdate importer. UniProt identifies the "
            "reviewed protein as ModC, part of the ModABC complex for molybdenum "
            "import, and assigns EC 7.3.2.5 for ATP-dependent molybdate import."
        ),
        "uniprot_text": "Full=Molybdenum import ATP-binding protein ModC",
        "asta_text": "Protein Description:** RecName: Full=Molybdenum import ATP-binding protein ModC",
        "function_text": "Part of the ABC transporter complex ModABC involved in",
        "catalytic_text": "Reaction=molybdate(out) + ATP + H2O = molybdate(in) + ADP + phosphate +",
        "domain_text": "FT   DOMAIN          1..236",
        "family_text": "Belongs to the ABC transporter superfamily. Molybdate",
    },
}


def binding_review(gene: str, cfg: dict, term_id: str, label: str) -> dict:
    product = support_uniprot(gene, cfg["uniprot_text"])
    asta = support_asta(gene, cfg["asta_text"])
    mapping = {
        "GO:0015689": (
            "Molybdate ion transport is correct for the periplasmic substrate-binding component of ModABC.",
            "ACCEPT",
            "ModA is the molybdate-binding periplasmic component of the adjacent ModABC importer.",
            None,
            [product, asta],
        ),
        "GO:0030973": (
            "Molybdate ion binding is the core molecular function of ModA.",
            "ACCEPT",
            "The product name, ModA family assignment, and GOA support molybdate binding.",
            None,
            [product, support_uniprot(gene, cfg["panther_text"]), asta],
        ),
        "GO:1901359": (
            "Tungstate binding is plausible for the ModA/WtpA family but is secondary to the molybdate importer assignment at this pass.",
            "KEEP_AS_NON_CORE",
            "The PANTHER subfamily name includes tungstate/molybdate/chromate binding, but the local product name and transporter context support molybdate import as the core module function.",
            None,
            [support_uniprot(gene, "PANTHER; PTHR30632:SF14; TUNGSTATE_MOLYBDATE_CHROMATE-BINDING PROTEIN MODA; 1.")],
        ),
    }
    summary, action, reason, proposed, support = mapping[term_id]
    return review(gene, term_id, label, summary, action, reason, proposed=proposed, extra_support=support)


def permease_review(gene: str, cfg: dict, term_id: str, label: str) -> dict:
    product = support_uniprot(gene, cfg["uniprot_text"])
    asta = support_asta(gene, cfg["asta_text"])
    mapping = {
        "GO:0005886": (
            "Plasma membrane localization is appropriate for this predicted inner-membrane ModB permease.",
            "ACCEPT",
            "UniProt predicts ModB as a cell inner-membrane multi-pass membrane protein.",
            None,
            [support_uniprot(gene, "Cell inner membrane")],
        ),
        "GO:0015098": (
            "Molybdate ion transmembrane transporter activity is appropriate as a complex-level activity to which ModB contributes.",
            "ACCEPT",
            "ModB is the binding-protein-dependent permease responsible for substrate translocation in the molybdenum/molybdate transport system.",
            None,
            [product, support_uniprot(gene, cfg["function_text"]), asta],
        ),
        "GO:0015689": (
            "Molybdate ion transport is the correct first-pass process for ModB.",
            "ACCEPT",
            "The local ModABC transporter context and ModB function line support molybdate/molybdenum import across the membrane.",
            None,
            [support_uniprot(gene, cfg["function_text"]), asta],
        ),
        "GO:0016020": (
            "Membrane localization is true but less informative than plasma membrane for this bacterial inner-membrane permease.",
            "MARK_AS_OVER_ANNOTATED",
            "The record also has a plasma-membrane annotation and UniProt predicts a cell inner-membrane multi-pass protein.",
            None,
            [support_uniprot(gene, "Cell inner membrane")],
        ),
        "GO:0043190": (
            "ABC transporter complex membership is appropriate for this ModB permease.",
            "ACCEPT",
            "ModB belongs to a binding-protein-dependent transport system and is adjacent to ModA and ModC components.",
            None,
            [support_uniprot(gene, cfg["family_text"])],
        ),
        "GO:0055085": (
            "Transmembrane transport is correct but broad relative to the molybdate-import context.",
            "MODIFY",
            "Molybdate ion transport better captures the expected substrate and process for this ModB permease.",
            [MOLYBDATE_TRANSPORT],
            [support_uniprot(gene, cfg["function_text"]), asta],
        ),
    }
    summary, action, reason, proposed, support = mapping[term_id]
    return review(gene, term_id, label, summary, action, reason, proposed=proposed, extra_support=support)


def atpase_review(gene: str, cfg: dict, term_id: str, label: str) -> dict:
    product = support_uniprot(gene, cfg["uniprot_text"])
    asta = support_asta(gene, cfg["asta_text"])
    mapping = {
        "GO:0005524": (
            "ATP binding is correct for this ABC-transporter nucleotide-binding component.",
            "ACCEPT",
            "ModC has an ABC transporter ATP-binding domain and is the ATP-binding subunit of ModABC.",
            None,
            [support_uniprot(gene, cfg["domain_text"])],
        ),
        "GO:0005886": (
            "Plasma membrane localization is appropriate for the inner-membrane-associated ModC ATPase.",
            "ACCEPT",
            "UniProt places ModC at the cell inner membrane as a peripheral membrane protein.",
            None,
            [support_uniprot(gene, "Cell inner membrane")],
        ),
        "GO:0015098": (
            "Molybdate ion transmembrane transporter activity is correct but less specific than the ABC-type molybdate transporter activity also present.",
            "MARK_AS_OVER_ANNOTATED",
            "The reviewed ModC record supports the more specific ABC-type molybdate transporter activity for the ModABC complex.",
            None,
            [support_uniprot(gene, cfg["function_text"]), product],
        ),
        "GO:0015412": (
            "ABC-type molybdate transporter activity is the most specific transporter activity for ModC.",
            "ACCEPT",
            "UniProt assigns EC 7.3.2.5 and the Rhea reaction for ATP-dependent molybdate import.",
            None,
            [support_uniprot(gene, cfg["catalytic_text"]), product, asta],
        ),
        "GO:0015689": (
            "Molybdate ion transport is the correct first-pass process for ModC.",
            "ACCEPT",
            "ModC is part of the ModABC complex involved in molybdenum/molybdate import.",
            None,
            [support_uniprot(gene, cfg["function_text"]), asta],
        ),
        "GO:0016020": (
            "Membrane localization is true but less informative than plasma membrane for this membrane-associated ATPase.",
            "MARK_AS_OVER_ANNOTATED",
            "The record also has a plasma-membrane annotation and UniProt places ModC at the cell inner membrane.",
            None,
            [support_uniprot(gene, "Cell inner membrane")],
        ),
        "GO:0016887": (
            "ATP hydrolysis activity is the correct mechanistic activity for the ModC ATPase subunit.",
            "ACCEPT",
            "ATP hydrolysis by ModC energizes molybdate import by the ModABC transporter.",
            None,
            [support_uniprot(gene, cfg["catalytic_text"]), support_uniprot(gene, cfg["domain_text"])],
        ),
        "GO:0055085": (
            "Transmembrane transport is correct but broad relative to molybdate ion transport.",
            "MODIFY",
            "Molybdate ion transport better captures the expected substrate and process for ModC.",
            [MOLYBDATE_TRANSPORT],
            [support_uniprot(gene, cfg["function_text"]), asta],
        ),
        "GO:0140359": (
            "Generic ABC-type transporter activity is correct but less specific than ABC-type molybdate transporter activity.",
            "MODIFY",
            "The reviewed ModC record and EC 7.3.2.5 support ABC-type molybdate transporter activity as the more informative term.",
            [ABC_MOLYBDATE_TRANSPORTER],
            [support_uniprot(gene, cfg["catalytic_text"]), product],
        ),
    }
    summary, action, reason, proposed, support = mapping[term_id]
    return review(gene, term_id, label, summary, action, reason, proposed=proposed, extra_support=support)


def add_new_terms(doc: dict, gene: str, cfg: dict) -> None:
    term_ids = {ann["term"]["id"] for ann in doc.get("existing_annotations", [])}
    product_support = [support_uniprot(gene, cfg["uniprot_text"]), support_asta(gene, cfg["asta_text"])]

    if cfg["kind"] == "binding":
        if PERIPLASM["id"] not in term_ids:
            doc["existing_annotations"].append(
                new_annotation(
                    PERIPLASM,
                    "located_in",
                    uniprot_ref(gene),
                    "Outer membrane-bounded periplasmic-space localization is a useful missing annotation for ModA.",
                    "ModA is named as a periplasmic molybdate-binding protein and carries a signal peptide.",
                    [support_uniprot(gene, cfg["uniprot_text"]), support_uniprot(gene, cfg["signal_text"])],
                )
            )
            term_ids.add(PERIPLASM["id"])
        if ABC_COMPLEX["id"] not in term_ids:
            doc["existing_annotations"].append(
                new_annotation(
                    ABC_COMPLEX,
                    "part_of",
                    uniprot_ref(gene),
                    "ABC transporter complex membership is a useful missing annotation for ModA.",
                    "UniProt states that the ModABC complex contains ModC ATP-binding proteins, ModB transmembrane proteins, and ModA solute-binding protein.",
                    [support_uniprot(gene, cfg["subunit_text"]), *product_support],
                )
            )
    elif cfg["kind"] == "permease":
        if ABC_MOLYBDATE_TRANSPORTER["id"] not in term_ids:
            doc["existing_annotations"].append(
                new_annotation(
                    ABC_MOLYBDATE_TRANSPORTER,
                    "enables",
                    uniprot_ref(gene),
                    "ABC-type molybdate transporter activity is a useful missing complex-level annotation for ModB.",
                    "ModB is the permease component of the ModABC molybdate import system.",
                    [support_uniprot(gene, cfg["function_text"]), *product_support],
                )
            )
    elif ABC_COMPLEX["id"] not in term_ids:
        doc["existing_annotations"].append(
            new_annotation(
                ABC_COMPLEX,
                "part_of",
                uniprot_ref(gene),
                "ABC transporter complex membership is a useful missing annotation for ModC.",
                "UniProt identifies ModC as part of the ABC transporter complex ModABC.",
                [support_uniprot(gene, cfg["function_text"]), *product_support],
            )
        )


def set_core_functions(doc: dict, gene: str, cfg: dict) -> None:
    if cfg["kind"] == "binding":
        core = {
            "description": "Periplasmic molybdate-binding substrate-recognition component of the predicted ModABC importer.",
            "molecular_function": MOLYBDATE_BINDING,
            "directly_involved_in": [MOLYBDATE_TRANSPORT],
            "locations": [PERIPLASM],
            "in_complex": ABC_COMPLEX,
            "supported_by": [
                support_goa(gene, MOLYBDATE_BINDING["id"], MOLYBDATE_BINDING["label"]),
                support_uniprot(gene, cfg["uniprot_text"]),
                support_uniprot(gene, cfg["signal_text"]),
                support_asta(gene, cfg["asta_text"]),
            ],
        }
    elif cfg["kind"] == "permease":
        core = {
            "description": "Multi-pass permease component contributing to the predicted ModABC molybdate uptake system.",
            "contributes_to_molecular_function": ABC_MOLYBDATE_TRANSPORTER,
            "directly_involved_in": [MOLYBDATE_TRANSPORT],
            "locations": [PLASMA_MEMBRANE],
            "in_complex": ABC_COMPLEX,
            "supported_by": [
                support_goa(gene, MOLYBDATE_TRANSPORTER["id"], MOLYBDATE_TRANSPORTER["label"]),
                support_goa(gene, ABC_COMPLEX["id"], ABC_COMPLEX["label"]),
                support_uniprot(gene, cfg["function_text"]),
                support_asta(gene, cfg["asta_text"]),
            ],
        }
    else:
        core = {
            "description": "ATP-binding energy-coupling subunit catalyzing ATP-dependent molybdate import by the ModABC transporter.",
            "molecular_function": ATP_HYDROLYSIS,
            "contributes_to_molecular_function": ABC_MOLYBDATE_TRANSPORTER,
            "directly_involved_in": [MOLYBDATE_TRANSPORT],
            "locations": [PLASMA_MEMBRANE],
            "in_complex": ABC_COMPLEX,
            "supported_by": [
                support_goa(gene, ABC_MOLYBDATE_TRANSPORTER["id"], ABC_MOLYBDATE_TRANSPORTER["label"]),
                support_goa(gene, ATP_HYDROLYSIS["id"], ATP_HYDROLYSIS["label"]),
                support_uniprot(gene, cfg["catalytic_text"]),
                support_asta(gene, cfg["asta_text"]),
            ],
        }
    doc["core_functions"] = [core]
    doc["proposed_new_terms"] = []
    doc["suggested_questions"] = [
        {
            "question": (
                "Does PP_3828-PP_3830 function primarily as a molybdate importer in "
                "P. putida KT2440, and does ModA's tungstate-binding family signal "
                "correspond to physiologically relevant tungstate uptake?"
            )
        }
    ]
    doc["suggested_experiments"] = [
        {
            "description": (
                "Measure molybdate and tungstate uptake, molybdenum-cofactor enzyme "
                "activity, and growth phenotypes for modA, modB, and modC mutants "
                "under molybdate-limited conditions."
            ),
            "experiment_type": "targeted transporter mutant substrate-uptake and growth assay",
        }
    ]


def curate_gene(gene: str, cfg: dict) -> None:
    path = Path("genes") / SPECIES / gene / f"{gene}-ai-review.yaml"
    doc = yaml.safe_load(path.read_text())
    doc["status"] = "COMPLETE"
    doc["description"] = cfg["description"]

    ensure_reference(doc, goa_ref(gene), f"QuickGO GOA annotations for {gene}")
    ensure_reference(doc, uniprot_ref(gene), f"UniProtKB entry for {gene} ({doc['id']})", cfg["uniprot_text"])
    ensure_reference(doc, asta_ref(gene), f"Asta retrieval report for {gene} ({doc['id']})", cfg["asta_text"])

    for ann in doc.get("existing_annotations", []):
        term_id = ann["term"]["id"]
        label = ann["term"]["label"]
        if cfg["kind"] == "binding":
            ann["review"] = binding_review(gene, cfg, term_id, label)
        elif cfg["kind"] == "permease":
            ann["review"] = permease_review(gene, cfg, term_id, label)
        else:
            ann["review"] = atpase_review(gene, cfg, term_id, label)

    add_new_terms(doc, gene, cfg)
    set_core_functions(doc, gene, cfg)

    path.write_text(yaml.safe_dump(doc, sort_keys=False, width=1000))
    print(f"curated {path}")


def main() -> None:
    for gene, cfg in GENES.items():
        curate_gene(gene, cfg)


if __name__ == "__main__":
    main()
