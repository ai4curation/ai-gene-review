#!/usr/bin/env python3
"""First-pass curation for the ppu02010 PP_4483-PP_4486 His/ArgT importer."""

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


ATP_HYDROLYSIS = {"id": "GO:0016887", "label": "ATP hydrolysis activity"}
ATP_BINDING = {"id": "GO:0005524", "label": "ATP binding"}
ABC_AMINO_ACID_ACTIVITY = {
    "id": "GO:0015424",
    "label": "ABC-type amino acid transporter activity",
}
BASIC_AA_TRANSPORT = {
    "id": "GO:1990822",
    "label": "basic amino acid transmembrane transport",
}
AMINO_ACID_BINDING = {"id": "GO:0016597", "label": "amino acid binding"}
ABC_COMPLEX = {
    "id": "GO:0043190",
    "label": "ATP-binding cassette (ABC) transporter complex",
}
PLASMA_MEMBRANE = {"id": "GO:0005886", "label": "plasma membrane"}
PERIPLASM = {"id": "GO:0030288", "label": "outer membrane-bounded periplasmic space"}


GENES = {
    "hisP": {
        "kind": "atpase",
        "description": (
            "hisP encodes the ATP-binding energy-coupling subunit of the "
            "PP_4483-PP_4486 His/ArgT-family basic-amino-acid ABC uptake "
            "system. UniProt names the protein as a histidine/lysine/arginine/"
            "ornithine ABC transporter ATP-binding subunit, and its ABC ATPase "
            "domains support ATP hydrolysis-driven import with HisM/HisQ "
            "permeases and the ArgT periplasmic substrate-binding component."
        ),
        "uniprot_text": "Full=Histidine lysine / arginine / ornithine ABC transporter-ATP binding subunit",
        "asta_text": "Protein Description:** SubName: Full=Histidine lysine / arginine / ornithine ABC transporter-ATP binding subunit",
        "domain_text": "FT   DOMAIN          4..249",
        "family_text": "Belongs to the ABC transporter superfamily.",
    },
    "hisM": {
        "kind": "permease",
        "description": (
            "hisM encodes a predicted multi-pass inner-membrane permease "
            "component of the PP_4483-PP_4486 His/ArgT-family basic-amino-acid "
            "ABC uptake system. The product name and binding-protein-dependent "
            "transporter domains support a channel-forming role with HisQ, "
            "HisP, and ArgT."
        ),
        "uniprot_text": "Full=Histidine/lysine/arginine/ornithine transport system permease protein HisM",
        "asta_text": "Protein Description:** RecName: Full=Histidine/lysine/arginine/ornithine transport system permease protein HisM",
        "family_text": "Belongs to the binding-protein-dependent transport system",
        "domain_text": "FT   DOMAIN          19..216",
    },
    "hisQ": {
        "kind": "permease",
        "description": (
            "hisQ encodes the second predicted multi-pass inner-membrane "
            "permease component of the PP_4483-PP_4486 His/ArgT-family "
            "basic-amino-acid ABC uptake system. Its HisMQ/MetI-like "
            "permease domains and product name support a membrane-channel role "
            "in ATP-driven transport of basic amino acids."
        ),
        "uniprot_text": "Full=Histidine / lysine / arginine / ornithine ABC transporter-permease subunit",
        "asta_text": "Protein Description:** SubName: Full=Histidine / lysine / arginine / ornithine ABC transporter-permease subunit",
        "family_text": "Belongs to the binding-protein-dependent transport system",
        "domain_text": "FT   DOMAIN          13..213",
    },
    "argT": {
        "kind": "binding",
        "description": (
            "argT encodes a signal-peptide-bearing periplasmic "
            "lysine/arginine/ornithine substrate-binding component associated "
            "with the adjacent HisP/HisM/HisQ ABC transporter. The local locus "
            "supports a basic-amino-acid import role, while exact substrate "
            "preference among histidine, lysine, arginine, and ornithine remains "
            "to be resolved experimentally in KT2440."
        ),
        "uniprot_text": "Full=Lysine / arginine / ornithine ABC transporter-periplasmic binding protein",
        "asta_text": "Protein Description:** SubName: Full=Lysine / arginine / ornithine ABC transporter-periplasmic binding protein",
        "domain_text": "FT   DOMAIN          25..254",
        "signal_text": "FT   SIGNAL          1..21",
    },
}


def atpase_review(gene: str, cfg: dict, term_id: str, label: str) -> dict:
    product = support_uniprot(gene, cfg["uniprot_text"])
    asta = support_asta(gene, cfg["asta_text"])
    domain = support_uniprot(gene, cfg["domain_text"])
    mapping = {
        "GO:0000166": (
            "Nucleotide binding is true but less informative than ATP binding for this ABC ATPase.",
            "MARK_AS_OVER_ANNOTATED",
            "The review retains the more specific ATP-binding and ATP-hydrolysis annotations for the HisP-family energy-coupling subunit.",
            None,
            [product],
        ),
        "GO:0003333": (
            "Amino acid transmembrane transport is correct but broad for the His/ArgT-family basic-amino-acid ABC importer.",
            "MODIFY",
            "The product name identifies histidine, lysine, arginine, and ornithine transporter context, so basic amino acid transmembrane transport is the better first-pass process term.",
            [BASIC_AA_TRANSPORT],
            [product, asta],
        ),
        "GO:0005524": (
            "ATP binding is correct for this ABC-transporter nucleotide-binding component.",
            "ACCEPT",
            "HisP has an ABC transporter ATP-binding domain and is named as the ATP-binding subunit of the amino-acid transporter.",
            None,
            [domain],
        ),
        "GO:0005886": (
            "Plasma membrane localization is appropriate for the inner-membrane-associated ABC transporter ATPase.",
            "ACCEPT",
            "UniProt places HisP at the cell inner membrane, consistent with an energy-coupling component of an inner-membrane ABC importer.",
            None,
            [support_uniprot(gene, "Cell inner membrane")],
        ),
        "GO:0015424": (
            "ABC-type amino acid transporter activity is appropriate as the complex-level activity to which HisP contributes.",
            "ACCEPT",
            "The product name and ABC ATPase family support a role in a histidine/lysine/arginine/ornithine ABC transporter.",
            None,
            [product, asta],
        ),
        "GO:0016887": (
            "ATP hydrolysis activity is the correct mechanistic activity for the HisP ATPase subunit.",
            "ACCEPT",
            "ATP hydrolysis by HisP is expected to energize the adjacent amino-acid ABC importer.",
            None,
            [domain],
        ),
    }
    summary, action, reason, proposed, support = mapping[term_id]
    return review(
        gene,
        term_id,
        label,
        summary,
        action,
        reason,
        proposed=proposed,
        extra_support=support,
    )


def permease_review(gene: str, cfg: dict, term_id: str, label: str) -> dict:
    product = support_uniprot(gene, cfg["uniprot_text"])
    asta = support_asta(gene, cfg["asta_text"])
    family = support_uniprot(gene, cfg["family_text"])
    mapping = {
        "GO:0005886": (
            "Plasma membrane localization is appropriate for this predicted inner-membrane ABC permease.",
            "ACCEPT",
            "UniProt predicts the permease as a cell inner-membrane multi-pass membrane protein.",
            None,
            [support_uniprot(gene, "Cell inner membrane")],
        ),
        "GO:0006865": (
            "Amino acid transport is correct but broad for the His/ArgT-family basic-amino-acid ABC importer.",
            "MODIFY",
            "The product name identifies histidine/lysine/arginine/ornithine transport context, so basic amino acid transmembrane transport is the better first-pass process term.",
            [BASIC_AA_TRANSPORT],
            [product, asta],
        ),
        "GO:0016020": (
            "Membrane localization is true but less informative than plasma membrane for this bacterial inner-membrane permease.",
            "MARK_AS_OVER_ANNOTATED",
            "The record also has or is better represented by a plasma-membrane annotation and UniProt predicts a cell inner-membrane protein.",
            None,
            [support_uniprot(gene, "Cell inner membrane")],
        ),
        "GO:0022857": (
            "Generic transmembrane transporter activity is too broad for this ABC-transporter permease component.",
            "MODIFY",
            "The binding-protein-dependent transporter family and ABC-complex context support ABC-type amino acid transporter activity as the better complex-level activity.",
            [ABC_AMINO_ACID_ACTIVITY],
            [family],
        ),
        "GO:0043190": (
            "ABC transporter complex membership is appropriate for this HisM/HisQ-family permease.",
            "ACCEPT",
            "The permease belongs to a binding-protein-dependent transport system and is adjacent to HisP and ArgT components.",
            None,
            [family],
        ),
        "GO:0055085": (
            "Transmembrane transport is true but broad relative to the basic-amino-acid ABC-import context.",
            "MODIFY",
            "The product name and adjacent transporter components support basic amino acid transmembrane transport as the better first-pass process term.",
            [BASIC_AA_TRANSPORT],
            [product, asta],
        ),
    }
    summary, action, reason, proposed, support = mapping[term_id]
    return review(
        gene,
        term_id,
        label,
        summary,
        action,
        reason,
        proposed=proposed,
        extra_support=support,
    )


def binding_review(gene: str, cfg: dict, term_id: str, label: str) -> dict:
    mapping = {
        "GO:0030288": (
            "Outer membrane-bounded periplasmic-space localization is appropriate for this bacterial solute-binding protein.",
            "ACCEPT",
            "ArgT has a signal peptide and UniProt places it in the periplasm.",
            None,
            [support_uniprot(gene, cfg["signal_text"]), support_uniprot(gene, "Periplasm")],
        ),
        "GO:0042597": (
            "Periplasmic-space localization is true but less specific than the bacterial outer membrane-bounded periplasm term already present.",
            "MARK_AS_OVER_ANNOTATED",
            "The more specific outer membrane-bounded periplasmic-space annotation better captures this Gram-negative periplasmic binding protein.",
            None,
            [support_uniprot(gene, "Periplasm")],
        ),
    }
    summary, action, reason, proposed, support = mapping[term_id]
    return review(
        gene,
        term_id,
        label,
        summary,
        action,
        reason,
        proposed=proposed,
        extra_support=support,
    )


def add_new_terms(doc: dict, gene: str, cfg: dict) -> None:
    term_ids = {ann["term"]["id"] for ann in doc.get("existing_annotations", [])}
    product_support = [support_uniprot(gene, cfg["uniprot_text"]), support_asta(gene, cfg["asta_text"])]

    if BASIC_AA_TRANSPORT["id"] not in term_ids:
        doc["existing_annotations"].append(
            new_annotation(
                BASIC_AA_TRANSPORT,
                "involved_in",
                uniprot_ref(gene),
                "Basic amino acid transmembrane transport is a useful missing first-pass process annotation for this His/ArgT-family ABC-import component.",
                "The local product names support a histidine/lysine/arginine/ornithine ABC transporter assignment, but exact substrate preference remains unresolved.",
                product_support,
            )
        )
        term_ids.add(BASIC_AA_TRANSPORT["id"])

    if cfg["kind"] in {"atpase", "binding"} and ABC_COMPLEX["id"] not in term_ids:
        doc["existing_annotations"].append(
            new_annotation(
                ABC_COMPLEX,
                "part_of",
                uniprot_ref(gene),
                "ABC transporter complex membership is a useful missing annotation for this component of the PP_4483-PP_4486 importer.",
                "The gene is part of a contiguous HisP/HisM/HisQ/ArgT ABC-transporter locus.",
                product_support,
            )
        )
        term_ids.add(ABC_COMPLEX["id"])

    if cfg["kind"] == "binding" and AMINO_ACID_BINDING["id"] not in term_ids:
        doc["existing_annotations"].append(
            new_annotation(
                AMINO_ACID_BINDING,
                "enables",
                uniprot_ref(gene),
                "Amino acid binding is a useful missing molecular-function annotation for ArgT.",
                "UniProt names ArgT as a lysine/arginine/ornithine ABC transporter periplasmic binding protein and records a Lys/Arg/Orn-binding domain.",
                [
                    support_uniprot(gene, cfg["uniprot_text"]),
                    support_uniprot(gene, "InterPro; IPR005768; Lys_Arg_Orn-bd."),
                    support_asta(gene, cfg["asta_text"]),
                ],
            )
        )


def set_core_functions(doc: dict, gene: str, cfg: dict) -> None:
    product_support = [support_uniprot(gene, cfg["uniprot_text"]), support_asta(gene, cfg["asta_text"])]
    if cfg["kind"] == "atpase":
        core = {
            "description": "ATP-binding energy-coupling subunit contributing to a predicted His/ArgT-family basic-amino-acid ABC uptake system.",
            "molecular_function": ATP_HYDROLYSIS,
            "contributes_to_molecular_function": ABC_AMINO_ACID_ACTIVITY,
            "directly_involved_in": [BASIC_AA_TRANSPORT],
            "locations": [PLASMA_MEMBRANE],
            "in_complex": ABC_COMPLEX,
            "supported_by": [
                support_goa(gene, ATP_HYDROLYSIS["id"], ATP_HYDROLYSIS["label"]),
                support_uniprot(gene, cfg["domain_text"]),
                *product_support,
            ],
        }
    elif cfg["kind"] == "permease":
        core = {
            "description": "Multi-pass permease component contributing to a predicted His/ArgT-family basic-amino-acid ABC uptake system.",
            "contributes_to_molecular_function": ABC_AMINO_ACID_ACTIVITY,
            "directly_involved_in": [BASIC_AA_TRANSPORT],
            "locations": [PLASMA_MEMBRANE],
            "in_complex": ABC_COMPLEX,
            "supported_by": [
                support_goa(gene, ABC_COMPLEX["id"], ABC_COMPLEX["label"]),
                support_uniprot(gene, cfg["domain_text"]),
                *product_support,
            ],
        }
    else:
        core = {
            "description": "Periplasmic basic-amino-acid substrate-binding component of a predicted HisP/HisM/HisQ ABC importer.",
            "molecular_function": AMINO_ACID_BINDING,
            "directly_involved_in": [BASIC_AA_TRANSPORT],
            "locations": [PERIPLASM],
            "in_complex": ABC_COMPLEX,
            "supported_by": [
                support_goa(gene, PERIPLASM["id"], PERIPLASM["label"]),
                support_uniprot(gene, cfg["uniprot_text"]),
                support_uniprot(gene, "InterPro; IPR005768; Lys_Arg_Orn-bd."),
                support_asta(gene, cfg["asta_text"]),
            ],
        }
    doc["core_functions"] = [core]
    doc["proposed_new_terms"] = []
    doc["suggested_questions"] = [
        {
            "question": (
                "Does the PP_4483-PP_4486 His/ArgT-family ABC importer prefer "
                "L-histidine, L-lysine, L-arginine, L-ornithine, or a broader "
                "basic-amino-acid substrate range in P. putida KT2440?"
            )
        }
    ]
    doc["suggested_experiments"] = [
        {
            "description": (
                "Measure uptake and growth phenotypes for hisP, hisM, hisQ, and "
                "argT mutants with L-histidine, L-lysine, L-arginine, and "
                "L-ornithine supplied as nitrogen or carbon sources."
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
        if cfg["kind"] == "atpase":
            ann["review"] = atpase_review(gene, cfg, term_id, label)
        elif cfg["kind"] == "permease":
            ann["review"] = permease_review(gene, cfg, term_id, label)
        else:
            ann["review"] = binding_review(gene, cfg, term_id, label)

    add_new_terms(doc, gene, cfg)
    set_core_functions(doc, gene, cfg)

    path.write_text(yaml.safe_dump(doc, sort_keys=False, width=1000))
    print(f"curated {path}")


def main() -> None:
    for gene, cfg in GENES.items():
        curate_gene(gene, cfg)


if __name__ == "__main__":
    main()
