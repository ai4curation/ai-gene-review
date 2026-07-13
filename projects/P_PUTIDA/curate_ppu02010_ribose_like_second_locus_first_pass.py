#!/usr/bin/env python3
"""First-pass curation for the ppu02010 C39 ribose-like ABC transporter locus."""

from __future__ import annotations

from pathlib import Path

import yaml


SPECIES = "PSEPK"


def ref_path(gene: str, suffix: str) -> str:
    return f"file:{SPECIES}/{gene}/{gene}-{suffix}"


def goa_ref(gene: str) -> str:
    return ref_path(gene, "goa.tsv")


def uniprot_ref(gene: str) -> str:
    return ref_path(gene, "uniprot.txt")


def asta_ref(gene: str) -> str:
    return ref_path(gene, "deep-research-asta.md")


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
    uniprot_text: str | None = None,
    asta_text: str | None = None,
    proposed: list[dict] | None = None,
    extra_support: list[dict] | None = None,
) -> dict:
    supported_by = [support_goa(gene, term_id, label)]
    if uniprot_text:
        supported_by.append(support_uniprot(gene, uniprot_text))
    if asta_text:
        supported_by.append(support_asta(gene, asta_text))
    if extra_support:
        supported_by.extend(extra_support)
    result = {
        "summary": summary,
        "action": action,
        "reason": reason,
        "supported_by": supported_by,
    }
    if proposed:
        result["proposed_replacement_terms"] = proposed
    return result


def new_annotation(
    term: dict,
    qualifier: str,
    gene: str,
    summary: str,
    reason: str,
    supported_by: list[dict],
) -> dict:
    return {
        "term": term,
        "evidence_type": "IEA",
        "original_reference_id": uniprot_ref(gene),
        "qualifier": qualifier,
        "review": {
            "summary": summary,
            "action": "NEW",
            "reason": reason,
            "supported_by": supported_by,
        },
    }


CARBOHYDRATE_BINDING = {"id": "GO:0030246", "label": "carbohydrate binding"}
D_RIBOSE_TRANSMEMBRANE_TRANSPORT = {"id": "GO:0015752", "label": "D-ribose transmembrane transport"}
ABC_D_RIBOSE_TRANSPORTER = {"id": "GO:0015611", "label": "ABC-type D-ribose transporter activity"}
ABC_COMPLEX = {"id": "GO:0043190", "label": "ATP-binding cassette (ABC) transporter complex"}
PLASMA_MEMBRANE = {"id": "GO:0005886", "label": "plasma membrane"}
CELL_ENVELOPE = {"id": "GO:0030313", "label": "cell envelope"}
ATP_BINDING = {"id": "GO:0005524", "label": "ATP binding"}


CONFIG = {
    "PP_2757": {
        "symbol": "PP_2757",
        "description": (
            "PP_2757 encodes an unreviewed cell-envelope bacterial solute-binding protein "
            "near the PP_2758-PP_2761 ribose ABC transporter locus. Current annotations "
            "support carbohydrate binding and cell-envelope localization, but the ligand "
            "is not resolved enough to assign D-ribose-specific transport."
        ),
        "uniprot_text": "Full=Sugar-binding protein",
        "asta_text": "Protein Description:** SubName: Full=Sugar-binding protein",
        "reviews": {
            "GO:0030246": (
                "Carbohydrate binding is appropriate for this bacterial solute-binding protein, but the substrate is unresolved.",
                "ACCEPT",
                "UniProt names PP_2757 as a sugar-binding protein and assigns it to the bacterial solute-binding protein 2 family.",
                "Full=Sugar-binding protein",
            ),
            "GO:0030313": (
                "Cell envelope localization is appropriate for a signal-peptide-bearing solute-binding protein.",
                "ACCEPT",
                "UniProt places PP_2757 in the cell envelope.",
                "Cell envelope",
            ),
            "GO:0055085": (
                "Transmembrane transport is plausible for an adjacent solute-binding component but too broad and not substrate-resolved for PP_2757.",
                "MARK_AS_OVER_ANNOTATED",
                "The current evidence supports carbohydrate binding at the cell envelope, not a specific transport process for this component.",
                "Belongs to the bacterial solute-binding protein 2 family",
            ),
        },
        "new": [],
        "core": {
            "description": "Cell-envelope carbohydrate-binding solute-binding protein adjacent to the PP_2758-PP_2761 ribose ABC transporter locus.",
            "molecular_function": CARBOHYDRATE_BINDING,
            "locations": [CELL_ENVELOPE],
            "support": [
                support_goa("PP_2757", "GO:0030246", "carbohydrate binding"),
                support_uniprot("PP_2757", "Full=Sugar-binding protein"),
                support_uniprot("PP_2757", "Belongs to the bacterial solute-binding protein 2 family"),
                support_asta("PP_2757", "Protein Description:** SubName: Full=Sugar-binding protein"),
            ],
        },
    },
    "PP_2758": {
        "symbol": "PP_2758",
        "description": (
            "PP_2758 encodes the periplasmic ribose-binding solute-binding component "
            "of the PP_2758-PP_2761 RbsABC D-ribose ABC importer. The product name, "
            "cell-envelope localization, signal peptide, and local rbsA/permease "
            "context support a substrate-binding role in ATP-dependent ribose uptake."
        ),
        "uniprot_text": "Full=Ribose ABC transporter, periplasmic ribose-binding protein",
        "asta_text": "Protein Description:** SubName: Full=Ribose ABC transporter, periplasmic ribose-binding protein",
        "reviews": {
            "GO:0030246": (
                "Carbohydrate binding is appropriate but broad for this ribose-binding solute-binding component.",
                "ACCEPT",
                "UniProt names PP_2758 as a ribose ABC transporter periplasmic ribose-binding protein.",
                "Full=Ribose ABC transporter, periplasmic ribose-binding protein",
            ),
            "GO:0030313": (
                "Cell envelope localization is appropriate for this periplasmic binding component.",
                "ACCEPT",
                "UniProt places PP_2758 in the cell envelope and predicts a signal peptide.",
                "Cell envelope",
            ),
            "GO:0055085": (
                "Transmembrane transport is correct but too broad relative to D-ribose transmembrane transport for this Rbs importer component.",
                "MARK_AS_OVER_ANNOTATED",
                "The product name and local PP_2758-rbsA-PP_2760-PP_2761 context support D-ribose-specific ABC transport.",
                "Full=Ribose ABC transporter, periplasmic ribose-binding protein",
            ),
        },
        "new": [
            new_annotation(
                D_RIBOSE_TRANSMEMBRANE_TRANSPORT,
                "involved_in",
                "PP_2758",
                "PP_2758 should be represented with D-ribose transmembrane transport.",
                "PP_2758 is named as the periplasmic ribose-binding protein adjacent to rbsA and two ribose permease genes.",
                [
                    support_uniprot("PP_2758", "Full=Ribose ABC transporter, periplasmic ribose-binding protein"),
                ],
            ),
            new_annotation(
                ABC_D_RIBOSE_TRANSPORTER,
                "contributes_to",
                "PP_2758",
                "PP_2758 contributes the substrate-binding component of ABC-type D-ribose transporter activity.",
                "The PP_2758 product is the ribose-binding component of the local RbsABC importer.",
                [
                    support_uniprot("PP_2758", "Full=Ribose ABC transporter, periplasmic ribose-binding protein"),
                    support_uniprot("PP_2758", "Belongs to the bacterial solute-binding protein 2 family"),
                ],
            ),
            new_annotation(
                ABC_COMPLEX,
                "part_of",
                "PP_2758",
                "PP_2758 should be represented as part of the ribose ABC transporter complex.",
                "PP_2758 is the solute-binding component paired with the rbsA ATPase and PP_2760/PP_2761 permeases.",
                [support_uniprot("PP_2758", "Full=Ribose ABC transporter, periplasmic ribose-binding protein")],
            ),
        ],
        "core": {
            "description": "Periplasmic ribose-binding component of the PP_2758-PP_2761 RbsABC D-ribose ABC importer.",
            "molecular_function": CARBOHYDRATE_BINDING,
            "directly_involved_in": [D_RIBOSE_TRANSMEMBRANE_TRANSPORT],
            "locations": [CELL_ENVELOPE],
            "in_complex": ABC_COMPLEX,
            "support": [
                support_goa("PP_2758", "GO:0030246", "carbohydrate binding"),
                support_uniprot("PP_2758", "Full=Ribose ABC transporter, periplasmic ribose-binding protein"),
                support_uniprot("PP_2758", "Belongs to the bacterial solute-binding protein 2 family"),
                support_asta("PP_2758", "Protein Description:** SubName: Full=Ribose ABC transporter, periplasmic ribose-binding protein"),
            ],
        },
    },
    "rbsA": {
        "symbol": "rbsA",
        "description": (
            "rbsA (PP_2759) encodes the ATP-binding energy-coupling subunit of the "
            "PP_2758-PP_2761 RbsABC D-ribose ABC importer. Reviewed UniProt/HAMAP "
            "annotation describes RbsA as part of the RbsABC complex involved in ribose "
            "import and records EC 7.5.2.7 for ATP-dependent D-ribose import."
        ),
        "uniprot_text": "Part of the ABC transporter complex RbsABC involved in ribose",
        "asta_text": "Protein Description:** RecName: Full=Ribose import ATP-binding protein RbsA",
        "reviews": {
            "GO:0005524": (
                "ATP binding is appropriate for this ABC transporter ATP-binding subunit.",
                "ACCEPT",
                "Reviewed UniProt/HAMAP annotation identifies RbsA as the energy-coupling ATP-binding component.",
                "Responsible for energy coupling to the transport system",
            ),
            "GO:0005886": (
                "Plasma membrane localization is appropriate for this peripheral membrane ATPase subunit of the importer.",
                "ACCEPT",
                "Reviewed UniProt/HAMAP annotation places RbsA at the cell inner membrane as a peripheral membrane protein.",
                "Cell inner membrane",
            ),
            "GO:0015611": (
                "ABC-type D-ribose transporter activity is the correct substrate-specific molecular function for RbsA.",
                "ACCEPT",
                "Reviewed UniProt/HAMAP annotation describes RbsA as part of RbsABC involved in ribose import and records the D-ribose import reaction.",
                "Part of the ABC transporter complex RbsABC involved in ribose",
            ),
            "GO:0015752": (
                "D-ribose transmembrane transport is the correct biological process for RbsA.",
                "ACCEPT",
                "Reviewed UniProt/HAMAP annotation records D-ribose import by the RbsABC transporter.",
                "Reaction=D-ribose(out) + ATP + H2O = D-ribose(in)",
            ),
            "GO:0016887": (
                "ATP hydrolysis is correct mechanistic chemistry, but the substrate-specific ABC transporter activity is the core MF.",
                "KEEP_AS_NON_CORE",
                "ATP hydrolysis powers ABC transport, while GO:0015611 captures ATP-dependent D-ribose import.",
                "ATP",
            ),
        },
        "new": [
            new_annotation(
                ABC_COMPLEX,
                "part_of",
                "rbsA",
                "RbsA should be represented as the ATP-binding subunit of the ribose ABC transporter complex.",
                "Reviewed UniProt/HAMAP annotation describes RbsA as part of the RbsABC transporter complex.",
                [
                    support_uniprot("rbsA", "Part of the ABC transporter complex RbsABC involved in ribose"),
                    support_uniprot("rbsA", "The complex is composed of an ATP-binding protein (RbsA), two"),
                ],
            ),
        ],
        "core": {
            "description": "ATP-binding energy-coupling subunit of the PP_2758-PP_2761 RbsABC D-ribose ABC importer.",
            "molecular_function": ABC_D_RIBOSE_TRANSPORTER,
            "directly_involved_in": [D_RIBOSE_TRANSMEMBRANE_TRANSPORT],
            "locations": [PLASMA_MEMBRANE],
            "in_complex": ABC_COMPLEX,
            "support": [
                support_goa("rbsA", "GO:0015611", "ABC-type D-ribose transporter activity"),
                support_goa("rbsA", "GO:0015752", "D-ribose transmembrane transport"),
                support_uniprot("rbsA", "Part of the ABC transporter complex RbsABC involved in ribose"),
                support_uniprot("rbsA", "Reaction=D-ribose(out) + ATP + H2O = D-ribose(in)"),
                support_asta("rbsA", "Protein Description:** RecName: Full=Ribose import ATP-binding protein RbsA"),
            ],
        },
    },
    "PP_2760": {
        "symbol": "PP_2760",
        "description": (
            "PP_2760 encodes a multi-pass inner-membrane permease component of the "
            "PP_2758-PP_2761 RbsABC D-ribose ABC importer. Its ribose transport permease "
            "product name, AraH/RbsC permease-family assignment, and local rbsA/ribose-binding "
            "context support a membrane-channel role in D-ribose import."
        ),
        "uniprot_text": "Full=Ribose transport permease protein",
        "asta_text": "Protein Description:** SubName: Full=Ribose transport permease protein",
        "reviews": {
            "GO:0005886": (
                "Plasma membrane localization is appropriate for this multi-pass bacterial inner-membrane permease.",
                "ACCEPT",
                "UniProt places PP_2760 at the cell inner membrane and predicts a multi-pass membrane protein.",
                "Cell inner membrane",
            ),
            "GO:0016020": (
                "Membrane localization is correct but less specific than plasma membrane for this bacterial inner-membrane permease.",
                "MARK_AS_OVER_ANNOTATED",
                "The plasma membrane annotation is the more informative retained location.",
                "Cell inner membrane",
            ),
            "GO:0022857": (
                "Transmembrane transporter activity is correct but too broad for this ribose ABC permease.",
                "MARK_AS_OVER_ANNOTATED",
                "The product name and AraH/RbsC permease-family assignment support D-ribose ABC transporter context.",
                "Full=Ribose transport permease protein",
            ),
            "GO:0055085": (
                "Transmembrane transport is correct but too broad relative to D-ribose transmembrane transport.",
                "MARK_AS_OVER_ANNOTATED",
                "The product name and local RbsABC context support D-ribose-specific transmembrane transport.",
                "Full=Ribose transport permease protein",
            ),
        },
        "new": [
            new_annotation(
                D_RIBOSE_TRANSMEMBRANE_TRANSPORT,
                "involved_in",
                "PP_2760",
                "PP_2760 should be represented with D-ribose transmembrane transport.",
                "PP_2760 is a ribose transport permease in the PP_2758-rbsA-PP_2760-PP_2761 RbsABC locus.",
                [
                    support_uniprot("PP_2760", "Full=Ribose transport permease protein"),
                    support_uniprot("PP_2760", "AraH/RbsC subfamily"),
                ],
            ),
            new_annotation(
                ABC_D_RIBOSE_TRANSPORTER,
                "contributes_to",
                "PP_2760",
                "PP_2760 contributes the membrane permease component of ABC-type D-ribose transporter activity.",
                "PP_2760 is an AraH/RbsC-family ribose transport permease paired with the RbsA ATPase.",
                [
                    support_uniprot("PP_2760", "Full=Ribose transport permease protein"),
                    support_uniprot("PP_2760", "AraH/RbsC subfamily"),
                ],
            ),
            new_annotation(
                ABC_COMPLEX,
                "part_of",
                "PP_2760",
                "PP_2760 should be represented as part of the ribose ABC transporter complex.",
                "PP_2760 is one membrane permease component of the local RbsABC importer.",
                [support_uniprot("PP_2760", "Full=Ribose transport permease protein")],
            ),
        ],
        "core": {
            "description": "Membrane permease component of the PP_2758-PP_2761 RbsABC D-ribose ABC importer.",
            "contributes_to_molecular_function": ABC_D_RIBOSE_TRANSPORTER,
            "directly_involved_in": [D_RIBOSE_TRANSMEMBRANE_TRANSPORT],
            "locations": [PLASMA_MEMBRANE],
            "in_complex": ABC_COMPLEX,
            "support": [
                support_uniprot("PP_2760", "Full=Ribose transport permease protein"),
                support_uniprot("PP_2760", "AraH/RbsC subfamily"),
                support_asta("PP_2760", "Protein Description:** SubName: Full=Ribose transport permease protein"),
            ],
        },
    },
    "PP_2761": {
        "symbol": "PP_2761",
        "description": (
            "PP_2761 encodes a multi-pass inner-membrane permease component of the "
            "PP_2758-PP_2761 RbsABC D-ribose ABC importer. Its ribose ABC transporter "
            "permease product name, AraH/RbsC permease-family assignment, and local "
            "rbsA/ribose-binding context support a membrane-channel role in D-ribose import."
        ),
        "uniprot_text": "Full=Ribose ABC transporter, permease protein",
        "asta_text": "Protein Description:** SubName: Full=Ribose ABC transporter, permease protein",
        "reviews": {
            "GO:0005886": (
                "Plasma membrane localization is appropriate for this multi-pass bacterial inner-membrane permease.",
                "ACCEPT",
                "UniProt places PP_2761 at the cell inner membrane and predicts a multi-pass membrane protein.",
                "Cell inner membrane",
            ),
            "GO:0016020": (
                "Membrane localization is correct but less specific than plasma membrane for this bacterial inner-membrane permease.",
                "MARK_AS_OVER_ANNOTATED",
                "The plasma membrane annotation is the more informative retained location.",
                "Cell inner membrane",
            ),
            "GO:0022857": (
                "Transmembrane transporter activity is correct but too broad for this ribose ABC permease.",
                "MARK_AS_OVER_ANNOTATED",
                "The product name and AraH/RbsC permease-family assignment support D-ribose ABC transporter context.",
                "Full=Ribose ABC transporter, permease protein",
            ),
            "GO:0055085": (
                "Transmembrane transport is correct but too broad relative to D-ribose transmembrane transport.",
                "MARK_AS_OVER_ANNOTATED",
                "The product name and local RbsABC context support D-ribose-specific transmembrane transport.",
                "Full=Ribose ABC transporter, permease protein",
            ),
        },
        "new": [
            new_annotation(
                D_RIBOSE_TRANSMEMBRANE_TRANSPORT,
                "involved_in",
                "PP_2761",
                "PP_2761 should be represented with D-ribose transmembrane transport.",
                "PP_2761 is a ribose ABC transporter permease in the PP_2758-rbsA-PP_2760-PP_2761 RbsABC locus.",
                [
                    support_uniprot("PP_2761", "Full=Ribose ABC transporter, permease protein"),
                    support_uniprot("PP_2761", "AraH/RbsC subfamily"),
                ],
            ),
            new_annotation(
                ABC_D_RIBOSE_TRANSPORTER,
                "contributes_to",
                "PP_2761",
                "PP_2761 contributes the membrane permease component of ABC-type D-ribose transporter activity.",
                "PP_2761 is an AraH/RbsC-family ribose ABC transporter permease paired with the RbsA ATPase.",
                [
                    support_uniprot("PP_2761", "Full=Ribose ABC transporter, permease protein"),
                    support_uniprot("PP_2761", "AraH/RbsC subfamily"),
                ],
            ),
            new_annotation(
                ABC_COMPLEX,
                "part_of",
                "PP_2761",
                "PP_2761 should be represented as part of the ribose ABC transporter complex.",
                "PP_2761 is one membrane permease component of the local RbsABC importer.",
                [support_uniprot("PP_2761", "Full=Ribose ABC transporter, permease protein")],
            ),
        ],
        "core": {
            "description": "Membrane permease component of the PP_2758-PP_2761 RbsABC D-ribose ABC importer.",
            "contributes_to_molecular_function": ABC_D_RIBOSE_TRANSPORTER,
            "directly_involved_in": [D_RIBOSE_TRANSMEMBRANE_TRANSPORT],
            "locations": [PLASMA_MEMBRANE],
            "in_complex": ABC_COMPLEX,
            "support": [
                support_uniprot("PP_2761", "Full=Ribose ABC transporter, permease protein"),
                support_uniprot("PP_2761", "AraH/RbsC subfamily"),
                support_asta("PP_2761", "Protein Description:** SubName: Full=Ribose ABC transporter, permease protein"),
            ],
        },
    },
}


def curate_gene(gene: str, cfg: dict) -> None:
    path = Path("genes") / SPECIES / gene / f"{gene}-ai-review.yaml"
    doc = yaml.safe_load(path.read_text())
    doc["gene_symbol"] = cfg["symbol"]
    doc["status"] = "COMPLETE"
    doc["description"] = cfg["description"]

    ensure_reference(doc, goa_ref(gene), f"QuickGO GOA annotations for {gene}")
    ensure_reference(doc, uniprot_ref(gene), f"UniProtKB entry for {gene} ({doc['id']})", cfg["uniprot_text"])
    ensure_reference(doc, asta_ref(gene), f"Asta retrieval report for {gene} ({doc['id']})", cfg["asta_text"])

    doc["existing_annotations"] = [
        ann for ann in doc.get("existing_annotations", []) if ann.get("review", {}).get("action") != "NEW"
    ]

    for ann in doc.get("existing_annotations", []):
        term_id = ann["term"]["id"]
        if term_id not in cfg["reviews"]:
            raise ValueError(f"No review configured for {gene} {term_id}")
        summary, action, reason, uniprot_text = cfg["reviews"][term_id]
        ann["review"] = review(
            gene,
            term_id,
            ann["term"]["label"],
            summary,
            action,
            reason,
            uniprot_text=uniprot_text,
            asta_text=cfg["asta_text"],
        )

    doc["existing_annotations"].extend(cfg.get("new", []))

    core = dict(cfg["core"])
    support = core.pop("support")
    core["supported_by"] = support
    doc["core_functions"] = [core]
    doc["proposed_new_terms"] = []
    doc["suggested_questions"] = [
        {
            "question": "Do PP_2454-PP_2456 and PP_2758-PP_2761 encode redundant D-ribose importers or transporters with distinct pentose substrate ranges?"
        },
        {
            "question": "What ligand is bound by the adjacent PP_2757 solute-binding protein, and is it part of the same transport/regulatory neighborhood as PP_2758-PP_2761?"
        },
    ]
    doc["suggested_experiments"] = [
        {
            "description": "Compare D-ribose uptake and growth phenotypes in PP_2454-PP_2456, PP_2758-PP_2761, and double-locus transporter mutants.",
            "experiment_type": "ribose transporter mutant uptake and growth assay",
        },
        {
            "description": "Purify PP_2757 and PP_2758 solute-binding proteins and measure ligand binding against D-ribose and related pentoses/polyols.",
            "experiment_type": "solute-binding protein ligand-binding assay",
        },
    ]

    path.write_text(yaml.safe_dump(doc, sort_keys=False, width=1000))
    print(f"curated {path}")


def main() -> None:
    for gene, cfg in CONFIG.items():
        curate_gene(gene, cfg)


if __name__ == "__main__":
    main()
