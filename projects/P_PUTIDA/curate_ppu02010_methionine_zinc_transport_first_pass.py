#!/usr/bin/env python3
"""First-pass curation for ppu02010 methionine and zinc ABC importers."""

from __future__ import annotations

from pathlib import Path

import yaml


SPECIES = "PSEPK"


def goa_ref(gene: str) -> str:
    return f"file:{SPECIES}/{gene}/{gene}-goa.tsv"


def uniprot_ref(gene: str) -> str:
    return f"file:{SPECIES}/{gene}/{gene}-uniprot.txt"


def asta_ref(gene: str) -> str:
    return f"file:{SPECIES}/{gene}/{gene}-deep-research-asta.md"


def goa_text(term_id: str, label: str) -> str:
    return f"{term_id}\t{label}"


def support_goa(gene: str, term_id: str, label: str) -> dict:
    return {"reference_id": goa_ref(gene), "supporting_text": goa_text(term_id, label)}


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
    evidence_type: str,
    original_reference_id: str,
    summary: str,
    reason: str,
    supported_by: list[dict],
) -> dict:
    return {
        "term": term,
        "evidence_type": evidence_type,
        "original_reference_id": original_reference_id,
        "qualifier": qualifier,
        "review": {
            "summary": summary,
            "action": "NEW",
            "reason": reason,
            "supported_by": supported_by,
        },
    }


ATP_BINDING = {"id": "GO:0005524", "label": "ATP binding"}
ATP_HYDROLYSIS = {"id": "GO:0016887", "label": "ATP hydrolysis activity"}
PLASMA_MEMBRANE = {"id": "GO:0005886", "label": "plasma membrane"}
MEMBRANE = {"id": "GO:0016020", "label": "membrane"}
PERIPLASM = {"id": "GO:0042597", "label": "periplasmic space"}
ABC_COMPLEX = {"id": "GO:0043190", "label": "ATP-binding cassette (ABC) transporter complex"}
D_MET_TRANSPORT = {"id": "GO:0048473", "label": "D-methionine transmembrane transport"}
ABC_D_MET = {"id": "GO:0033232", "label": "ABC-type D-methionine transporter activity"}
AMINO_ACID_TRANSPORT = {"id": "GO:0006865", "label": "amino acid transport"}
TRANSMEMBRANE_TRANSPORT = {"id": "GO:0055085", "label": "transmembrane transport"}
ZINC_RESPONSE = {"id": "GO:0010043", "label": "response to zinc ion"}
ZINC_TRANSPORT = {"id": "GO:0006829", "label": "zinc ion transport"}
ZINC_TRANSMEMBRANE_TRANSPORT = {"id": "GO:0071577", "label": "zinc ion transmembrane transport"}
ABC_ZINC = {"id": "GO:0015633", "label": "ABC-type zinc transporter activity"}
ZINC_BINDING = {"id": "GO:0008270", "label": "zinc ion binding"}
METAL_TRANSPORT = {"id": "GO:0030001", "label": "metal ion transport"}
METAL_BINDING = {"id": "GO:0046872", "label": "metal ion binding"}
CELL_ADHESION = {"id": "GO:0007155", "label": "cell adhesion"}


CONFIG = {
    "metQ": {
        "symbol": "metQ",
        "description": (
            "metQ (PP_0112) encodes the predicted lipoprotein substrate-binding component of the "
            "MetNIQ methionine ABC importer. The product name, MetQ/NlpA-family domain, and local "
            "metQ-metI-metN1 locus support a methionine-import role, with the exact L- versus "
            "D-methionine substrate range inferred from the cognate MetN1/MetI annotations rather "
            "than directly assayed in KT2440."
        ),
        "uniprot_text": "Full=Methionine ABC transporter, periplasmic binding protein",
        "asta_text": "Protein Description:** SubName: Full=Methionine ABC transporter, periplasmic binding protein",
        "reviews": {
            "GO:0016020": (
                "Membrane localization is appropriate for this predicted signal-peptide-bearing lipoprotein substrate-binding component.",
                "ACCEPT",
                "UniProt records MetQ as a membrane lipoprotein with a signal peptide and MetQ-family product name.",
                "Membrane",
            ),
        },
        "new": [
            new_annotation(
                D_MET_TRANSPORT,
                "involved_in",
                "IEA",
                "file:PSEPK/metQ/metQ-uniprot.txt",
                "MetQ should be represented as the substrate-binding component contributing to the MetNIQ D-methionine transport system.",
                "The adjacent MetI/MetN1 components carry D-methionine transport annotations, and the MetQ product/domain context identifies it as the cognate periplasmic binding component.",
                [
                    support_uniprot("metQ", "Full=Methionine ABC transporter, periplasmic binding protein"),
                    support_asta(
                        "metQ",
                        "Protein Description:** SubName: Full=Methionine ABC transporter, periplasmic binding protein",
                    ),
                ],
            ),
            new_annotation(
                ABC_COMPLEX,
                "part_of",
                "IEA",
                "file:PSEPK/metQ/metQ-uniprot.txt",
                "MetQ is the substrate-binding component of a methionine ABC transporter complex.",
                "The local metQ-metI-metN1 locus and product name support membership in the MetNIQ ABC importer.",
                [
                    support_uniprot("metQ", "Full=Methionine ABC transporter, periplasmic binding protein"),
                    support_asta(
                        "metQ",
                        "Protein Description:** SubName: Full=Methionine ABC transporter, periplasmic binding protein",
                    ),
                ],
            ),
        ],
        "core": {
            "description": "Predicted lipoprotein substrate-binding component of the MetNIQ methionine ABC importer.",
            "directly_involved_in": [D_MET_TRANSPORT],
            "locations": [MEMBRANE],
            "in_complex": ABC_COMPLEX,
            "support": [
                support_uniprot("metQ", "Full=Methionine ABC transporter, periplasmic binding protein"),
                support_asta(
                    "metQ",
                    "Protein Description:** SubName: Full=Methionine ABC transporter, periplasmic binding protein",
                ),
            ],
        },
        "question": "Does the KT2440 MetQ/MetI/MetN1 importer transport L-methionine, D-methionine, or both under physiological conditions?",
    },
    "metI": {
        "symbol": "metI",
        "description": (
            "metI (PP_0113) encodes the predicted multi-pass inner-membrane permease component of "
            "the MetNIQ methionine ABC importer. Its MetI-like permease domains and adjacent "
            "metQ/metN1 genes support methionine translocation across the plasma membrane."
        ),
        "uniprot_text": "Full=Methionine ABC transporter, permease protein",
        "asta_text": "Protein Description:** SubName: Full=Methionine ABC transporter, permease protein",
        "reviews": {
            "GO:0005886": (
                "Plasma membrane localization is appropriate for this multi-pass inner-membrane permease.",
                "ACCEPT",
                "UniProt predicts MetI as a cell-membrane multi-pass membrane protein.",
                "Cell membrane",
            ),
            "GO:0006865": (
                "Amino acid transport is directionally correct but less precise than D-methionine transmembrane transport for this locus.",
                "MARK_AS_OVER_ANNOTATED",
                "The MetI-like domain, product name, and local MetQ/MetN1 partners support methionine-specific transport rather than a generic amino acid process.",
                None,
            ),
            "GO:0016020": (
                "Membrane localization is correct but less specific than plasma membrane for this bacterial inner-membrane permease.",
                "MARK_AS_OVER_ANNOTATED",
                "The plasma membrane annotation better captures the relevant bacterial membrane location.",
                "Cell membrane",
            ),
            "GO:0043190": (
                "ABC transporter complex membership is appropriate for MetI.",
                "ACCEPT",
                "MetI is the membrane permease component of a binding-protein-dependent methionine ABC importer.",
                "Full=Methionine ABC transporter, permease protein",
            ),
            "GO:0048473": (
                "D-methionine transmembrane transport is appropriate process context for MetI.",
                "ACCEPT",
                "MetI is the permease subunit paired with MetN1, whose reviewed UniProt entry records D-methionine and L-methionine import reactions.",
                "Full=Methionine ABC transporter, permease protein",
            ),
            "GO:0055085": (
                "Transmembrane transport is true but broad relative to D-methionine transmembrane transport.",
                "MARK_AS_OVER_ANNOTATED",
                "GO:0048473 captures the substrate-specific transport process for this locus.",
                None,
            ),
        },
        "core": {
            "description": "Multi-pass membrane permease component of the MetNIQ methionine ABC importer.",
            "contributes_to_molecular_function": ABC_D_MET,
            "directly_involved_in": [D_MET_TRANSPORT],
            "locations": [PLASMA_MEMBRANE],
            "in_complex": ABC_COMPLEX,
            "support": [
                support_goa("metI", "GO:0048473", "D-methionine transmembrane transport"),
                support_uniprot("metI", "Full=Methionine ABC transporter, permease protein"),
                support_asta("metI", "Protein Description:** SubName: Full=Methionine ABC transporter, permease protein"),
            ],
        },
        "question": "Does MetI pair exclusively with MetN1/MetQ, or can it function with other methionine-binding components in KT2440?",
    },
    "metN1": {
        "symbol": "metN1",
        "description": (
            "metN1 (PP_0114) encodes the reviewed ATP-binding energy-coupling subunit of the "
            "MetNIQ methionine ABC importer. UniProt/HAMAP describes MetN1 as part of the "
            "MetNIQ complex and records ATP-driven L- and D-methionine import reactions."
        ),
        "uniprot_text": "Full=Methionine import ATP-binding protein MetN 1",
        "asta_text": "Protein Description:** RecName: Full=Methionine import ATP-binding protein MetN 1",
        "reviews": {
            "GO:0005524": (
                "ATP binding is appropriate for this ABC ATP-binding subunit.",
                "ACCEPT",
                "UniProt records an ABC transporter domain and ATP-binding site for MetN1.",
                "ATP",
            ),
            "GO:0005886": (
                "Plasma membrane localization is appropriate for the membrane-associated ATPase component of the importer.",
                "ACCEPT",
                "UniProt places MetN1 at the cell inner membrane as a peripheral membrane protein.",
                "Cell inner membrane",
            ),
            "GO:0016887": (
                "ATP hydrolysis is correct mechanistic chemistry, but the substrate-specific ABC-type D-methionine transporter activity is the core MF.",
                "KEEP_AS_NON_CORE",
                "ATP hydrolysis powers the transporter, while GO:0033232 captures the more specific molecular function.",
                "ATP",
            ),
            "GO:0033232": (
                "ABC-type D-methionine transporter activity is the best existing molecular-function term for MetN1.",
                "ACCEPT",
                "Reviewed UniProt/HAMAP annotation identifies MetN1 as the ATP-binding energy-coupling subunit of MetNIQ and records D-methionine import.",
                "Full=Methionine import ATP-binding protein MetN 1",
            ),
            "GO:0048473": (
                "D-methionine transmembrane transport is appropriate process context for MetN1.",
                "ACCEPT",
                "Reviewed UniProt/HAMAP annotation records a D-methionine(out) to D-methionine(in) ATP-driven transport reaction.",
                "D-methionine(out)",
            ),
        },
        "new": [
            new_annotation(
                ABC_COMPLEX,
                "part_of",
                "IEA",
                "file:PSEPK/metN1/metN1-uniprot.txt",
                "MetN1 should be represented as an ATP-binding subunit of the MetNIQ ABC transporter complex.",
                "Reviewed UniProt/HAMAP annotation states that the MetNIQ complex contains two MetN ATP-binding proteins plus MetI and MetQ components.",
                [
                    support_uniprot("metN1", "The complex is composed of two ATP-binding proteins (MetN)"),
                    support_uniprot("metN1", "two transmembrane proteins (MetI) and a solute-binding protein (MetQ)"),
                ],
            ),
        ],
        "core": {
            "description": "ATP-binding energy-coupling subunit of the MetNIQ methionine ABC importer.",
            "molecular_function": ABC_D_MET,
            "directly_involved_in": [D_MET_TRANSPORT],
            "locations": [PLASMA_MEMBRANE],
            "in_complex": ABC_COMPLEX,
            "support": [
                support_goa("metN1", "GO:0033232", "ABC-type D-methionine transporter activity"),
                support_uniprot("metN1", "Full=Methionine import ATP-binding protein MetN 1"),
                support_asta(
                    "metN1",
                    "Protein Description:** RecName: Full=Methionine import ATP-binding protein MetN 1",
                ),
            ],
        },
        "question": "What is the in vivo contribution of the MetNIQ importer to L-methionine versus D-methionine uptake in KT2440?",
    },
    "metP": {
        "symbol": "metP",
        "description": (
            "metP (PP_0219) encodes the predicted multi-pass inner-membrane permease component "
            "of a second MetNIQ-like methionine ABC importer. Its product name, MetI-like "
            "PANTHER assignment, and adjacent metN2/PP_0221 genes support methionine "
            "translocation across the plasma membrane."
        ),
        "uniprot_text": "Full=L,D-methionine D-methionine ABC transporter-permease subunit",
        "asta_text": "Protein Description:** SubName: Full=L,D-methionine D-methionine ABC transporter-permease subunit",
        "reviews": {
            "GO:0005886": (
                "Plasma membrane localization is appropriate for this multi-pass inner-membrane permease.",
                "ACCEPT",
                "UniProt predicts MetP as a cell-membrane multi-pass membrane protein.",
                "Cell membrane",
            ),
            "GO:0006865": (
                "Amino acid transport is directionally correct but less precise than D-methionine transmembrane transport for this locus.",
                "MARK_AS_OVER_ANNOTATED",
                "The MetI-like family assignment, product name, and local MetN2/MetQ-like partner support methionine-specific transport rather than a generic amino acid process.",
                "D-METHIONINE TRANSPORT SYSTEM PERMEASE PROTEIN METI-RELATED",
            ),
            "GO:0016020": (
                "Membrane localization is correct but less specific than plasma membrane for this bacterial inner-membrane permease.",
                "MARK_AS_OVER_ANNOTATED",
                "The plasma membrane annotation better captures the relevant bacterial membrane location.",
                "Cell membrane",
            ),
            "GO:0043190": (
                "ABC transporter complex membership is appropriate for MetP.",
                "ACCEPT",
                "MetP is the membrane permease component of a MetNIQ-like methionine ABC importer.",
                "Full=L,D-methionine D-methionine ABC transporter-permease subunit",
            ),
            "GO:0048473": (
                "D-methionine transmembrane transport is appropriate process context for MetP.",
                "ACCEPT",
                "MetP is a MetI-like permease subunit paired with MetN2, whose reviewed UniProt entry records D-methionine and L-methionine import reactions.",
                "D-methionine transmembrane transport",
            ),
            "GO:0055085": (
                "Transmembrane transport is true but broad relative to D-methionine transmembrane transport.",
                "MARK_AS_OVER_ANNOTATED",
                "GO:0048473 captures the substrate-specific transport process for this locus.",
                "Full=L,D-methionine D-methionine ABC transporter-permease subunit",
            ),
        },
        "core": {
            "description": "Multi-pass membrane permease component of a MetNIQ-like methionine ABC importer.",
            "contributes_to_molecular_function": ABC_D_MET,
            "directly_involved_in": [D_MET_TRANSPORT],
            "locations": [PLASMA_MEMBRANE],
            "in_complex": ABC_COMPLEX,
            "support": [
                support_goa("metP", "GO:0048473", "D-methionine transmembrane transport"),
                support_uniprot("metP", "Full=L,D-methionine D-methionine ABC transporter-permease subunit"),
                support_asta(
                    "metP",
                    "Protein Description:** SubName: Full=L,D-methionine D-methionine ABC transporter-permease subunit",
                ),
            ],
        },
        "question": "Does the PP_0219-PP_0221 MetNIQ-like importer transport L-methionine, D-methionine, or both under physiological conditions?",
    },
    "metN2": {
        "symbol": "metN2",
        "description": (
            "metN2 (PP_0220) encodes the reviewed ATP-binding energy-coupling subunit of a "
            "MetNIQ methionine ABC importer. UniProt/HAMAP describes MetN2 as part of a "
            "MetNIQ complex and records ATP-driven L- and D-methionine import reactions."
        ),
        "uniprot_text": "Full=Methionine import ATP-binding protein MetN 2",
        "asta_text": "Protein Description:** RecName: Full=Methionine import ATP-binding protein MetN 2",
        "reviews": {
            "GO:0005524": (
                "ATP binding is appropriate for this ABC ATP-binding subunit.",
                "ACCEPT",
                "UniProt records an ABC transporter domain and ATP-binding protein product name for MetN2.",
                "ATP",
            ),
            "GO:0005886": (
                "Plasma membrane localization is appropriate for the membrane-associated ATPase component of the importer.",
                "ACCEPT",
                "UniProt places MetN2 at the cell inner membrane as a peripheral membrane protein.",
                "Cell inner membrane",
            ),
            "GO:0016887": (
                "ATP hydrolysis is correct mechanistic chemistry, but the substrate-specific ABC-type D-methionine transporter activity is the core MF.",
                "KEEP_AS_NON_CORE",
                "ATP hydrolysis powers the transporter, while GO:0033232 captures the more specific molecular function.",
                "ATP",
            ),
            "GO:0033232": (
                "ABC-type D-methionine transporter activity is the best existing molecular-function term for MetN2.",
                "ACCEPT",
                "Reviewed UniProt/HAMAP annotation identifies MetN2 as an ATP-binding subunit of MetNIQ and records D-methionine import.",
                "Full=Methionine import ATP-binding protein MetN 2",
            ),
            "GO:0048473": (
                "D-methionine transmembrane transport is appropriate process context for MetN2.",
                "ACCEPT",
                "Reviewed UniProt/HAMAP annotation records a D-methionine(out) to D-methionine(in) ATP-driven transport reaction.",
                "D-methionine(out)",
            ),
        },
        "new": [
            new_annotation(
                ABC_COMPLEX,
                "part_of",
                "IEA",
                "file:PSEPK/metN2/metN2-uniprot.txt",
                "MetN2 should be represented as an ATP-binding subunit of a MetNIQ ABC transporter complex.",
                "Reviewed UniProt/HAMAP annotation states that the MetNIQ complex contains two MetN ATP-binding proteins plus MetI and MetQ components.",
                [
                    support_uniprot("metN2", "The complex is composed of two ATP-binding proteins (MetN)"),
                    support_uniprot("metN2", "two transmembrane proteins (MetI) and a solute-binding protein (MetQ)"),
                ],
            ),
        ],
        "core": {
            "description": "ATP-binding energy-coupling subunit of a MetNIQ-like methionine ABC importer.",
            "molecular_function": ABC_D_MET,
            "directly_involved_in": [D_MET_TRANSPORT],
            "locations": [PLASMA_MEMBRANE],
            "in_complex": ABC_COMPLEX,
            "support": [
                support_goa("metN2", "GO:0033232", "ABC-type D-methionine transporter activity"),
                support_uniprot("metN2", "Full=Methionine import ATP-binding protein MetN 2"),
                support_asta(
                    "metN2",
                    "Protein Description:** RecName: Full=Methionine import ATP-binding protein MetN 2",
                ),
            ],
        },
        "question": "What is the in vivo contribution of the PP_0219-PP_0221 importer to L-methionine versus D-methionine uptake in KT2440?",
    },
    "PP_0221": {
        "symbol": "PP_0221",
        "description": (
            "PP_0221 encodes a predicted MetQ-like lipoprotein substrate-binding component of "
            "a methionine ABC importer adjacent to metP and metN2. Its MetQ/NlpA-family "
            "assignment and product name support methionine-import context, although the "
            "exact L- versus D-methionine substrate range is inferred from its cognate "
            "MetP/MetN2 partners rather than directly assayed in KT2440."
        ),
        "uniprot_text": "Full=Methionine ABC transporter periplasmic-binding lipoprotein (MetQ-like protein)",
        "asta_text": "Protein Description:** SubName: Full=Methionine ABC transporter periplasmic-binding lipoprotein (MetQ-like protein)",
        "reviews": {
            "GO:0016020": (
                "Membrane localization is appropriate for this predicted MetQ-like lipoprotein substrate-binding component.",
                "ACCEPT",
                "UniProt records PP_0221 as a membrane lipoprotein and assigns it to the NlpA lipoprotein family.",
                "Membrane",
            ),
        },
        "new": [
            new_annotation(
                D_MET_TRANSPORT,
                "involved_in",
                "IEA",
                "file:PSEPK/PP_0221/PP_0221-uniprot.txt",
                "PP_0221 should be represented as the substrate-binding component contributing to a MetNIQ-like D-methionine transport system.",
                "The adjacent MetP/MetN2 components carry D-methionine transport annotations, and the PP_0221 product/domain context identifies it as the cognate MetQ-like binding component.",
                [
                    support_uniprot(
                        "PP_0221",
                        "Full=Methionine ABC transporter periplasmic-binding lipoprotein (MetQ-like protein)",
                    ),
                    support_asta(
                        "PP_0221",
                        "Protein Description:** SubName: Full=Methionine ABC transporter periplasmic-binding lipoprotein (MetQ-like protein)",
                    ),
                ],
            ),
            new_annotation(
                ABC_COMPLEX,
                "part_of",
                "IEA",
                "file:PSEPK/PP_0221/PP_0221-uniprot.txt",
                "PP_0221 is the predicted substrate-binding component of a MetNIQ-like ABC transporter complex.",
                "The local PP_0221-metP-metN2 locus and product name support membership in a methionine ABC importer.",
                [
                    support_uniprot(
                        "PP_0221",
                        "Full=Methionine ABC transporter periplasmic-binding lipoprotein (MetQ-like protein)",
                    ),
                    support_asta(
                        "PP_0221",
                        "Protein Description:** SubName: Full=Methionine ABC transporter periplasmic-binding lipoprotein (MetQ-like protein)",
                    ),
                ],
            ),
        ],
        "core": {
            "description": "Predicted MetQ-like lipoprotein substrate-binding component of a methionine ABC importer.",
            "directly_involved_in": [D_MET_TRANSPORT],
            "locations": [MEMBRANE],
            "in_complex": ABC_COMPLEX,
            "support": [
                support_uniprot(
                    "PP_0221",
                    "Full=Methionine ABC transporter periplasmic-binding lipoprotein (MetQ-like protein)",
                ),
                support_asta(
                    "PP_0221",
                    "Protein Description:** SubName: Full=Methionine ABC transporter periplasmic-binding lipoprotein (MetQ-like protein)",
                ),
            ],
        },
        "question": "Does PP_0221 bind L-methionine, D-methionine, or another sulfur-containing amino acid in vivo?",
    },
    "znuB": {
        "symbol": "znuB",
        "description": (
            "znuB (PP_0117) encodes the multi-pass membrane permease component of the ZnuABC "
            "high-affinity zinc uptake system. Its ZnuB-family annotation, zinc-transport keywords, "
            "and adjacent znuC/PP_0120 genes support a zinc import role."
        ),
        "uniprot_text": "Full=High-affinity zinc uptake system membrane protein ZnuB",
        "asta_text": "Protein Description:** RecName: Full=High-affinity zinc uptake system membrane protein ZnuB",
        "reviews": {
            "GO:0005886": (
                "Plasma membrane localization is appropriate for this multi-pass ZnuB permease.",
                "ACCEPT",
                "UniProt describes ZnuB as a cell-inner-membrane multi-pass membrane protein.",
                "Cell inner membrane",
            ),
            "GO:0010043": (
                "Response to zinc ion is indirect and less precise than zinc ion transport for this importer subunit.",
                "MARK_AS_OVER_ANNOTATED",
                "ZnuB directly contributes to zinc uptake rather than acting as a regulatory response factor.",
                "high-affinity zinc uptake",
            ),
            "GO:0043190": (
                "ABC transporter complex membership is appropriate for ZnuB.",
                "ACCEPT",
                "ZnuB is the membrane permease component of the ZnuABC high-affinity zinc uptake system.",
                "Full=High-affinity zinc uptake system membrane protein ZnuB",
            ),
            "GO:0055085": (
                "Transmembrane transport is true but broad relative to zinc ion transmembrane transport.",
                "MARK_AS_OVER_ANNOTATED",
                "The ZnuB product name and UniProt zinc-transport keywords support zinc-specific transport context.",
                "Zinc transport",
            ),
        },
        "new": [
            new_annotation(
                ZINC_TRANSPORT,
                "involved_in",
                "IEA",
                "file:PSEPK/znuB/znuB-uniprot.txt",
                "Zinc ion transport is the appropriate substrate-specific process for ZnuB.",
                "UniProt describes ZnuB as part of a high-affinity zinc uptake transport system and records zinc transport keywords.",
                [
                    support_uniprot("znuB", "Involved in the high-affinity zinc uptake transport system"),
                    support_goa("znuB", "GO:0055085", "transmembrane transport"),
                ],
            ),
            new_annotation(
                ZINC_TRANSMEMBRANE_TRANSPORT,
                "involved_in",
                "IEA",
                "file:PSEPK/znuB/znuB-uniprot.txt",
                "ZnuB should be represented as the membrane permease contributing zinc ion movement across the plasma membrane.",
                "UniProt places ZnuB in the inner membrane and describes it as part of high-affinity zinc uptake.",
                [
                    support_uniprot("znuB", "Cell inner membrane"),
                    support_uniprot("znuB", "high-affinity zinc uptake transport system"),
                ],
            ),
        ],
        "core": {
            "description": "Multi-pass membrane permease component of the ZnuABC high-affinity zinc importer.",
            "contributes_to_molecular_function": ABC_ZINC,
            "directly_involved_in": [ZINC_TRANSMEMBRANE_TRANSPORT],
            "locations": [PLASMA_MEMBRANE],
            "in_complex": ABC_COMPLEX,
            "support": [
                support_uniprot("znuB", "Full=High-affinity zinc uptake system membrane protein ZnuB"),
                support_asta("znuB", "Protein Description:** RecName: Full=High-affinity zinc uptake system membrane protein ZnuB"),
            ],
        },
        "question": "Does KT2440 use this ZnuABC locus as the primary zinc importer under zinc limitation, and what regulator controls it?",
    },
    "znuC": {
        "symbol": "znuC",
        "description": (
            "znuC (PP_0118) encodes the reviewed ATP-binding energy-coupling subunit of the "
            "ZnuABC high-affinity zinc importer. UniProt/HAMAP records ZnuC as part of the "
            "ZnuABC complex and assigns ATP-driven zinc import activity."
        ),
        "uniprot_text": "Full=Zinc import ATP-binding protein ZnuC",
        "asta_text": "Protein Description:** RecName: Full=Zinc import ATP-binding protein ZnuC",
        "reviews": {
            "GO:0005524": (
                "ATP binding is appropriate for this ABC ATP-binding subunit.",
                "ACCEPT",
                "UniProt records an ABC transporter domain and ATP-binding site for ZnuC.",
                "ATP",
            ),
            "GO:0005886": (
                "Plasma membrane localization is appropriate for the membrane-associated ATPase component of the importer.",
                "ACCEPT",
                "UniProt places ZnuC at the cell inner membrane as a peripheral membrane protein.",
                "Cell inner membrane",
            ),
            "GO:0010043": (
                "Response to zinc ion is indirect and less precise than zinc ion transmembrane transport for this importer component.",
                "MARK_AS_OVER_ANNOTATED",
                "ZnuC directly powers zinc uptake; response-to-zinc annotations should not be treated as the core function.",
                "zinc import",
            ),
            "GO:0015633": (
                "ABC-type zinc transporter activity is the core molecular function for ZnuC.",
                "ACCEPT",
                "Reviewed UniProt/HAMAP annotation identifies ZnuC as the ATP-binding component of ZnuABC and records ATP-driven Zn(2+) import.",
                "Full=Zinc import ATP-binding protein ZnuC",
            ),
            "GO:0016887": (
                "ATP hydrolysis is correct mechanistic chemistry, but the substrate-specific ABC-type zinc transporter activity is the core MF.",
                "KEEP_AS_NON_CORE",
                "ATP hydrolysis powers the transporter, while GO:0015633 captures the more specific molecular function.",
                "ATP",
            ),
            "GO:0071577": (
                "Zinc ion transmembrane transport is appropriate process context for ZnuC.",
                "ACCEPT",
                "Reviewed UniProt/HAMAP annotation records an ATP-driven Zn(2+) import reaction.",
                "Zn(2+)(out)",
            ),
        },
        "new": [
            new_annotation(
                ABC_COMPLEX,
                "part_of",
                "IEA",
                "file:PSEPK/znuC/znuC-uniprot.txt",
                "ZnuC should be represented as an ATP-binding subunit of the ZnuABC transporter complex.",
                "Reviewed UniProt/HAMAP annotation states that the ZnuABC complex contains ZnuC, ZnuB, and ZnuA subunits.",
                [
                    support_uniprot("znuC", "The complex is composed of two ATP-binding proteins (ZnuC)"),
                    support_uniprot("znuC", "two transmembrane proteins (ZnuB) and a solute-binding protein (ZnuA)"),
                ],
            ),
        ],
        "core": {
            "description": "ATP-binding energy-coupling subunit of the ZnuABC high-affinity zinc importer.",
            "molecular_function": ABC_ZINC,
            "directly_involved_in": [ZINC_TRANSMEMBRANE_TRANSPORT],
            "locations": [PLASMA_MEMBRANE],
            "in_complex": ABC_COMPLEX,
            "support": [
                support_goa("znuC", "GO:0015633", "ABC-type zinc transporter activity"),
                support_uniprot("znuC", "Full=Zinc import ATP-binding protein ZnuC"),
                support_asta("znuC", "Protein Description:** RecName: Full=Zinc import ATP-binding protein ZnuC"),
            ],
        },
        "question": "Does ZnuC pair only with PP_0120/ZnuA and ZnuB, or are additional metal-binding proteins connected to this importer?",
    },
    "PP_0120": {
        "symbol": "PP_0120",
        "description": (
            "PP_0120 encodes a predicted ZnuA-family periplasmic substrate-binding component of "
            "the ZnuABC high-affinity zinc uptake system. UniProt describes the protein as binding "
            "zinc with high affinity and delivering it to the ZnuB permease for import."
        ),
        "uniprot_text": "Full=High-affinity zinc uptake system protein ZnuA",
        "asta_text": "Protein Description:** RecName: Full=High-affinity zinc uptake system protein ZnuA",
        "reviews": {
            "GO:0006829": (
                "Zinc ion transport is appropriate process context for this ZnuA-family binding component.",
                "ACCEPT",
                "UniProt describes PP_0120 as part of the ZnuABC zinc import system.",
                "ZnuABC involved in zinc import",
            ),
            "GO:0007155": (
                "Cell adhesion is a family-level InterPro spillover from adhesin-like metal-binding proteins and is not supported for this KT2440 ZnuA component.",
                "REMOVE",
                "The product name, ZnuA domains, and UniProt function support zinc uptake rather than adhesion.",
                "ZnuA",
            ),
            "GO:0030001": (
                "Metal ion transport is directionally correct but less precise than zinc ion transport.",
                "MARK_AS_OVER_ANNOTATED",
                "The ZnuA product name and function comment support zinc-specific uptake.",
                "zinc import",
            ),
            "GO:0042597": (
                "Periplasmic space is appropriate for this signal-peptide-bearing ZnuA substrate-binding protein.",
                "ACCEPT",
                "UniProt places PP_0120 in the periplasm and predicts a signal peptide.",
                "Periplasm",
            ),
            "GO:0046872": (
                "Metal ion binding is too broad for this ZnuA-family protein and should be narrowed to zinc ion binding.",
                "MODIFY",
                "UniProt states that PP_0120 binds zinc with high affinity and specificity.",
                "Binds zinc with high affinity",
                [ZINC_BINDING],
            ),
        },
        "new": [
            new_annotation(
                ABC_COMPLEX,
                "part_of",
                "IEA",
                "file:PSEPK/PP_0120/PP_0120-uniprot.txt",
                "PP_0120 should be represented as the periplasmic binding component of the ZnuABC transporter complex.",
                "UniProt describes PP_0120 as part of the ZnuABC ABC transport system involved in zinc import.",
                [
                    support_uniprot("PP_0120", "Part of the ATP-binding cassette (ABC) transport system"),
                    support_uniprot("PP_0120", "ZnuABC involved in zinc import"),
                ],
            ),
        ],
        "core": {
            "description": "Periplasmic high-affinity zinc-binding component of the ZnuABC zinc importer.",
            "molecular_function": ZINC_BINDING,
            "directly_involved_in": [ZINC_TRANSPORT],
            "locations": [PERIPLASM],
            "in_complex": ABC_COMPLEX,
            "support": [
                support_uniprot("PP_0120", "Binds zinc with high affinity"),
                support_goa("PP_0120", "GO:0006829", "zinc ion transport"),
                support_asta("PP_0120", "Protein Description:** RecName: Full=High-affinity zinc uptake system protein ZnuA"),
            ],
        },
        "question": "Should PP_0120 be renamed znuA in the local review once locus-level naming conventions are reconciled?",
    },
}


def apply_config(gene: str, cfg: dict) -> None:
    path = Path("genes") / SPECIES / gene / f"{gene}-ai-review.yaml"
    doc = yaml.safe_load(path.read_text())
    doc["gene_symbol"] = cfg["symbol"]
    doc["status"] = "COMPLETE"
    doc["description"] = cfg["description"]

    ensure_reference(doc, goa_ref(gene), f"QuickGO GOA annotations for {gene}")
    ensure_reference(doc, uniprot_ref(gene), f"UniProtKB entry for {gene} ({doc['id']})", cfg["uniprot_text"])
    ensure_reference(doc, asta_ref(gene), f"Asta retrieval report for {gene} ({doc['id']})", cfg["asta_text"])

    existing_annotations = [
        annotation
        for annotation in doc.get("existing_annotations", [])
        if annotation.get("review", {}).get("action") != "NEW"
    ]
    doc["existing_annotations"] = existing_annotations

    for annotation in doc.get("existing_annotations", []):
        term_id = annotation["term"]["id"]
        if term_id not in cfg["reviews"]:
            raise ValueError(f"No review configured for {gene} {term_id}")
        summary, action, reason, uniprot_text, *rest = cfg["reviews"][term_id]
        proposed = rest[0] if rest else None
        annotation["review"] = review(
            gene,
            term_id,
            annotation["term"]["label"],
            summary,
            action,
            reason,
            uniprot_text=uniprot_text,
            asta_text=cfg["asta_text"] if action in {"ACCEPT", "MODIFY"} else None,
            proposed=proposed,
        )

    doc["existing_annotations"].extend(cfg.get("new", []))

    core = dict(cfg["core"])
    support = core.pop("support")
    core["supported_by"] = support
    doc["core_functions"] = [core]
    doc["proposed_new_terms"] = []
    doc["suggested_questions"] = [{"question": cfg["question"]}]
    doc["suggested_experiments"] = [
        {
            "description": (
                "Measure substrate uptake and growth phenotypes for the matched transporter deletion "
                "mutants under substrate limitation, then complement the full locus to confirm importer assignment."
            ),
            "experiment_type": "targeted ABC-transporter mutant uptake and growth assay",
        }
    ]

    path.write_text(yaml.safe_dump(doc, sort_keys=False, allow_unicode=False))
    print(f"curated {path}")


def main() -> None:
    for gene, cfg in CONFIG.items():
        apply_config(gene, cfg)


if __name__ == "__main__":
    main()
