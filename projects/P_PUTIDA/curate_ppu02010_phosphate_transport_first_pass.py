#!/usr/bin/env python3
"""First-pass curation for the ppu02010 Pst-like phosphate ABC importers."""

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
    extra_support: list[dict] | None = None,
) -> dict:
    supported_by = [support_goa(gene, term_id, label)]
    if uniprot_text:
        supported_by.append(support_uniprot(gene, uniprot_text))
    if asta_text:
        supported_by.append(support_asta(gene, asta_text))
    if extra_support:
        supported_by.extend(extra_support)
    return {
        "summary": summary,
        "action": action,
        "reason": reason,
        "supported_by": supported_by,
    }


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


PHOSPHATE_BINDING = {"id": "GO:0042301", "label": "phosphate ion binding"}
PHOSPHATE_TRANSPORTER = {
    "id": "GO:0005315",
    "label": "phosphate transmembrane transporter activity",
}
ATPASE_COUPLED_PHOSPHATE_TRANSPORTER = {
    "id": "GO:0015415",
    "label": "ATPase-coupled phosphate ion transmembrane transporter activity",
}
PHOSPHATE_TRANSPORT = {"id": "GO:0006817", "label": "phosphate ion transport"}
PHOSPHATE_TRANSMEMBRANE_TRANSPORT = {
    "id": "GO:0035435",
    "label": "phosphate ion transmembrane transport",
}
ABC_COMPLEX = {"id": "GO:0043190", "label": "ATP-binding cassette (ABC) transporter complex"}
PLASMA_MEMBRANE = {"id": "GO:0005886", "label": "plasma membrane"}
MEMBRANE = {"id": "GO:0016020", "label": "membrane"}
ATP_BINDING = {"id": "GO:0005524", "label": "ATP binding"}
ATP_HYDROLYSIS = {"id": "GO:0016887", "label": "ATP hydrolysis activity"}


CONFIG = {
    "pstS": {
        "symbol": "pstS",
        "description": (
            "pstS (PP_2656) encodes the phosphate-binding solute-binding component of the "
            "PstSACB high-affinity phosphate ABC importer. UniProt describes PstS as part "
            "of the PstSACB complex involved in phosphate import, with PstC/PstA permeases "
            "and PstB ATP-binding proteins completing the importer."
        ),
        "uniprot_text": "Full=Phosphate-binding protein PstS",
        "asta_text": "Protein Description:** RecName: Full=Phosphate-binding protein PstS",
        "reviews": {
            "GO:0035435": (
                "Phosphate ion transmembrane transport is appropriate process context for the PstS substrate-binding component.",
                "ACCEPT",
                "UniProt describes PstS as part of the PstSACB ABC transporter complex involved in phosphate import.",
                "phosphate import",
            ),
            "GO:0042301": (
                "Phosphate ion binding is the direct molecular function for this PstS solute-binding component.",
                "ACCEPT",
                "The PstS product name and PstS phosphate-binding family support phosphate substrate binding.",
                "Full=Phosphate-binding protein PstS",
            ),
            "GO:0043190": (
                "ABC transporter complex membership is appropriate for PstS.",
                "ACCEPT",
                "UniProt describes PstS as the solute-binding protein in a PstSACB ABC transporter complex.",
                "two transmembrane proteins (PstC and PstA) and a solute-binding protein",
            ),
        },
        "core": {
            "description": "Phosphate-binding solute-binding component of the PstSACB high-affinity phosphate ABC importer.",
            "molecular_function": PHOSPHATE_BINDING,
            "directly_involved_in": [PHOSPHATE_TRANSMEMBRANE_TRANSPORT],
            "in_complex": ABC_COMPLEX,
            "support": [
                support_goa("pstS", "GO:0042301", "phosphate ion binding"),
                support_uniprot("pstS", "Full=Phosphate-binding protein PstS"),
                support_asta("pstS", "Protein Description:** RecName: Full=Phosphate-binding protein PstS"),
            ],
        },
    },
    "pstC": {
        "symbol": "pstC",
        "description": (
            "pstC (PP_2657) encodes a multi-pass inner-membrane permease component of the "
            "PstSACB high-affinity phosphate ABC importer. Its PstC-specific domain, "
            "binding-protein-dependent transport-system family assignment, and local "
            "pstS-pstC-pstA-pstB1 locus support phosphate translocation across the plasma membrane."
        ),
        "uniprot_text": "Full=Phosphate transport system permease protein",
        "asta_text": "Protein Description:** RecName: Full=Phosphate transport system permease protein",
        "reviews": {
            "GO:0005315": (
                "Phosphate transmembrane transporter activity is appropriate for this PstC permease component.",
                "ACCEPT",
                "PstC is the membrane permease responsible for substrate translocation in the phosphate binding-protein-dependent transport system.",
                "phosphate; probably responsible for the translocation of the substrate",
            ),
            "GO:0005886": (
                "Plasma membrane localization is appropriate for this multi-pass bacterial inner-membrane permease.",
                "ACCEPT",
                "UniProt predicts PstC as a cell-inner-membrane and cell-membrane multi-pass membrane protein.",
                "Cell inner membrane",
            ),
            "GO:0006817": (
                "Phosphate ion transport is correct but less specific than phosphate ion transmembrane transport for this permease.",
                "MARK_AS_OVER_ANNOTATED",
                "The transporter-system evidence supports movement of phosphate across the membrane, which is captured more precisely by GO:0035435.",
                "phosphate; probably responsible for the translocation of the substrate",
            ),
            "GO:0016020": (
                "Membrane localization is correct but less specific than plasma membrane for this bacterial inner-membrane permease.",
                "MARK_AS_OVER_ANNOTATED",
                "The plasma membrane annotation is the more informative retained location.",
                "Cell membrane",
            ),
            "GO:0043190": (
                "ABC transporter complex membership is appropriate for PstC.",
                "ACCEPT",
                "PstC is the Pst permease in a binding-protein-dependent phosphate ABC transporter system.",
                "Belongs to the binding-protein-dependent transport system",
            ),
            "GO:0055085": (
                "Transmembrane transport is true but broad relative to phosphate ion transmembrane transport.",
                "MARK_AS_OVER_ANNOTATED",
                "The PstC-specific domain and phosphate-translocation function support phosphate-specific transport.",
                "Phosphate_PstC",
            ),
        },
        "new": [
            new_annotation(
                PHOSPHATE_TRANSMEMBRANE_TRANSPORT,
                "involved_in",
                "pstC",
                "PstC should be represented with phosphate ion transmembrane transport.",
                "UniProt describes PstC as part of the phosphate binding-protein-dependent transport system responsible for substrate translocation across the membrane.",
                [
                    support_uniprot("pstC", "phosphate; probably responsible for the translocation of the substrate"),
                    support_asta("pstC", "Protein Description:** RecName: Full=Phosphate transport system permease protein"),
                ],
            ),
            new_annotation(
                ATPASE_COUPLED_PHOSPHATE_TRANSPORTER,
                "contributes_to",
                "pstC",
                "PstC contributes the membrane channel component of ATPase-coupled phosphate ion transporter activity.",
                "The local PstSACB importer uses PstC/PstA permeases plus PstB ATPase components for phosphate import.",
                [
                    support_uniprot("pstC", "Full=Phosphate transport system permease protein"),
                    support_uniprot("pstC", "Phosphate_PstC"),
                ],
            ),
        ],
        "core": {
            "description": "Multi-pass PstC permease component of the high-affinity phosphate ABC importer.",
            "contributes_to_molecular_function": ATPASE_COUPLED_PHOSPHATE_TRANSPORTER,
            "directly_involved_in": [PHOSPHATE_TRANSMEMBRANE_TRANSPORT],
            "locations": [PLASMA_MEMBRANE],
            "in_complex": ABC_COMPLEX,
            "support": [
                support_uniprot("pstC", "Full=Phosphate transport system permease protein"),
                support_uniprot("pstC", "phosphate; probably responsible for the translocation of the substrate"),
                support_asta("pstC", "Protein Description:** RecName: Full=Phosphate transport system permease protein"),
            ],
        },
    },
    "pstA": {
        "symbol": "pstA",
        "description": (
            "pstA (PP_2658) encodes the second multi-pass inner-membrane permease component "
            "of the PstSACB high-affinity phosphate ABC importer. Its PstA-specific domain "
            "and adjacent pstS/pstC/pstB1 genes support phosphate movement across the plasma membrane."
        ),
        "uniprot_text": "Full=Phosphate transport system permease protein PstA",
        "asta_text": "Protein Description:** RecName: Full=Phosphate transport system permease protein PstA",
        "reviews": {
            "GO:0005315": (
                "Phosphate transmembrane transporter activity is appropriate for this PstA permease component.",
                "ACCEPT",
                "PstA is a PstA-family membrane permease in the phosphate transport system.",
                "Full=Phosphate transport system permease protein PstA",
            ),
            "GO:0005886": (
                "Plasma membrane localization is appropriate for this multi-pass bacterial inner-membrane permease.",
                "ACCEPT",
                "UniProt predicts PstA as a cell-inner-membrane and cell-membrane multi-pass membrane protein.",
                "Cell inner membrane",
            ),
            "GO:0016020": (
                "Membrane localization is correct but less specific than plasma membrane for this bacterial inner-membrane permease.",
                "MARK_AS_OVER_ANNOTATED",
                "The plasma membrane annotation is the more informative retained location.",
                "Cell membrane",
            ),
            "GO:0035435": (
                "Phosphate ion transmembrane transport is appropriate process context for PstA.",
                "ACCEPT",
                "The PstA-specific permease assignment and phosphate transport keyword support phosphate movement across the membrane.",
                "Phosphate_PstA",
            ),
            "GO:0043190": (
                "ABC transporter complex membership is appropriate for PstA.",
                "ACCEPT",
                "PstA is a binding-protein-dependent transport-system permease in the local PstSACB phosphate importer.",
                "Belongs to the binding-protein-dependent transport system",
            ),
            "GO:0055085": (
                "Transmembrane transport is true but broad relative to phosphate ion transmembrane transport.",
                "MARK_AS_OVER_ANNOTATED",
                "The PstA-specific domain and phosphate transport annotations support phosphate-specific transport.",
                "Phosphate_PstA",
            ),
        },
        "new": [
            new_annotation(
                ATPASE_COUPLED_PHOSPHATE_TRANSPORTER,
                "contributes_to",
                "pstA",
                "PstA contributes the second membrane channel component of ATPase-coupled phosphate ion transporter activity.",
                "The local PstSACB importer uses PstC/PstA permeases plus PstB ATPase components for phosphate import.",
                [
                    support_uniprot("pstA", "Full=Phosphate transport system permease protein PstA"),
                    support_uniprot("pstA", "Phosphate_PstA"),
                ],
            ),
        ],
        "core": {
            "description": "Multi-pass PstA permease component of the high-affinity phosphate ABC importer.",
            "contributes_to_molecular_function": ATPASE_COUPLED_PHOSPHATE_TRANSPORTER,
            "directly_involved_in": [PHOSPHATE_TRANSMEMBRANE_TRANSPORT],
            "locations": [PLASMA_MEMBRANE],
            "in_complex": ABC_COMPLEX,
            "support": [
                support_goa("pstA", "GO:0035435", "phosphate ion transmembrane transport"),
                support_uniprot("pstA", "Full=Phosphate transport system permease protein PstA"),
                support_asta("pstA", "Protein Description:** RecName: Full=Phosphate transport system permease protein PstA"),
            ],
        },
    },
    "pstB1": {
        "symbol": "pstB1",
        "description": (
            "pstB1 (PP_2659) encodes the reviewed ATP-binding energy-coupling subunit of the "
            "PstSACB high-affinity phosphate ABC importer. UniProt/HAMAP describes PstB1 as "
            "part of the PstSACB complex, assigns EC 7.3.2.1, and records ATP-driven phosphate import."
        ),
        "uniprot_text": "Full=Phosphate import ATP-binding protein PstB 1",
        "asta_text": "Protein Description:** RecName: Full=Phosphate import ATP-binding protein PstB 1",
        "reviews": {
            "GO:0005315": (
                "Phosphate transmembrane transporter activity is directionally correct but less specific than ATPase-coupled phosphate ion transporter activity for PstB1.",
                "MARK_AS_OVER_ANNOTATED",
                "GO:0015415 captures the ATPase-coupled ABC transporter activity assigned to the reviewed PstB1 record.",
                "Full=Phosphate import ATP-binding protein PstB 1",
            ),
            "GO:0005524": (
                "ATP binding is appropriate for this ABC ATP-binding subunit.",
                "ACCEPT",
                "PstB1 is the ATP-binding component of the phosphate import ABC transporter.",
                "ATP-binding protein PstB 1",
            ),
            "GO:0005886": (
                "Plasma membrane localization is appropriate for the membrane-associated ATPase component of the importer.",
                "ACCEPT",
                "UniProt places PstB1 at the cell inner membrane as a peripheral membrane protein.",
                "Cell inner membrane",
            ),
            "GO:0015415": (
                "ATPase-coupled phosphate ion transmembrane transporter activity is the core molecular-function annotation for PstB1.",
                "ACCEPT",
                "Reviewed UniProt/HAMAP annotation records EC 7.3.2.1 and the ATP-driven phosphate import reaction.",
                "Reaction=phosphate(out) + ATP + H2O = ADP + 2 phosphate(in) + H(+);",
            ),
            "GO:0016020": (
                "Membrane localization is correct but less specific than plasma membrane for this membrane-associated ATPase.",
                "MARK_AS_OVER_ANNOTATED",
                "The plasma membrane annotation is the more informative retained location.",
                "Cell inner membrane",
            ),
            "GO:0016887": (
                "ATP hydrolysis is correct mechanistic chemistry, but the substrate-specific ABC phosphate transporter activity is the core MF.",
                "KEEP_AS_NON_CORE",
                "ATP hydrolysis powers the transporter, while GO:0015415 captures ATPase-coupled phosphate import.",
                "ATP",
            ),
            "GO:0035435": (
                "Phosphate ion transmembrane transport is appropriate process context for PstB1.",
                "ACCEPT",
                "Reviewed UniProt/HAMAP annotation describes PstB1 as part of PstSACB involved in phosphate import.",
                "phosphate import",
            ),
        },
        "new": [
            new_annotation(
                ABC_COMPLEX,
                "part_of",
                "pstB1",
                "PstB1 should be represented as an ATP-binding subunit of the PstSACB ABC transporter complex.",
                "Reviewed UniProt/HAMAP annotation states that the PstSACB complex contains PstB ATP-binding proteins, PstC/PstA transmembrane proteins, and PstS solute-binding protein.",
                [
                    support_uniprot("pstB1", "The complex is composed of two ATP-binding proteins (PstB)"),
                    support_uniprot("pstB1", "two transmembrane proteins (PstC and PstA) and a solute-binding protein"),
                ],
            ),
        ],
        "core": {
            "description": "ATP-binding energy-coupling subunit of the PstSACB high-affinity phosphate ABC importer.",
            "molecular_function": ATPASE_COUPLED_PHOSPHATE_TRANSPORTER,
            "directly_involved_in": [PHOSPHATE_TRANSMEMBRANE_TRANSPORT],
            "locations": [PLASMA_MEMBRANE],
            "in_complex": ABC_COMPLEX,
            "support": [
                support_goa("pstB1", "GO:0015415", "ATPase-coupled phosphate ion transmembrane transporter activity"),
                support_uniprot("pstB1", "Full=Phosphate import ATP-binding protein PstB 1"),
                support_asta("pstB1", "Protein Description:** RecName: Full=Phosphate import ATP-binding protein PstB 1"),
            ],
        },
    },
    "pstB2": {
        "symbol": "pstB2",
        "description": (
            "pstB2 (PP_5326) encodes the ATP-binding energy-coupling subunit of a second "
            "Pst-like phosphate ABC importer in KT2440. UniProt/HAMAP describes PstB2 as "
            "part of a PstSACB ABC transporter complex involved in ATP-driven phosphate import."
        ),
        "uniprot_text": "Full=Phosphate import ATP-binding protein PstB 2",
        "asta_text": "Protein Description:** RecName: Full=Phosphate import ATP-binding protein PstB 2",
        "reviews": {
            "GO:0005315": (
                "Phosphate transmembrane transporter activity is directionally correct but less specific than ATPase-coupled phosphate ion transporter activity for PstB2.",
                "MARK_AS_OVER_ANNOTATED",
                "GO:0015415 captures the ATPase-coupled ABC transporter activity assigned to the PstB2 record.",
                "Full=Phosphate import ATP-binding protein PstB 2",
            ),
            "GO:0005524": (
                "ATP binding is appropriate for this ABC ATP-binding subunit.",
                "ACCEPT",
                "PstB2 is the ATP-binding component of the second Pst-like phosphate import ABC transporter.",
                "ATP-binding protein PstB 2",
            ),
            "GO:0005886": (
                "Plasma membrane localization is appropriate for the membrane-associated ATPase component of the importer.",
                "ACCEPT",
                "UniProt places PstB2 at the cell inner membrane as a peripheral membrane protein.",
                "Cell inner membrane",
            ),
            "GO:0015415": (
                "ATPase-coupled phosphate ion transmembrane transporter activity is the core molecular-function annotation for PstB2.",
                "ACCEPT",
                "Reviewed UniProt/HAMAP annotation records EC 7.3.2.1 and the ATP-driven phosphate import reaction.",
                "Reaction=phosphate(out) + ATP + H2O = ADP + 2 phosphate(in) + H(+);",
            ),
            "GO:0016020": (
                "Membrane localization is correct but less specific than plasma membrane for this membrane-associated ATPase.",
                "MARK_AS_OVER_ANNOTATED",
                "The plasma membrane annotation is the more informative retained location.",
                "Cell inner membrane",
            ),
            "GO:0016887": (
                "ATP hydrolysis is correct mechanistic chemistry, but the substrate-specific ABC phosphate transporter activity is the core MF.",
                "KEEP_AS_NON_CORE",
                "ATP hydrolysis powers the transporter, while GO:0015415 captures ATPase-coupled phosphate import.",
                "ATP",
            ),
            "GO:0035435": (
                "Phosphate ion transmembrane transport is appropriate process context for PstB2.",
                "ACCEPT",
                "Reviewed UniProt/HAMAP annotation describes PstB2 as part of PstSACB involved in phosphate import.",
                "phosphate import",
            ),
        },
        "new": [
            new_annotation(
                ABC_COMPLEX,
                "part_of",
                "pstB2",
                "PstB2 should be represented as an ATP-binding subunit of the Pst-like ABC transporter complex.",
                "Reviewed UniProt/HAMAP annotation states that the PstSACB complex contains PstB ATP-binding proteins, PstC/PstA transmembrane proteins, and PstS solute-binding protein.",
                [
                    support_uniprot("pstB2", "The complex is composed of two ATP-binding proteins (PstB)"),
                    support_uniprot("pstB2", "two transmembrane proteins (PstC and PstA) and a solute-binding protein"),
                ],
            ),
        ],
        "core": {
            "description": "ATP-binding energy-coupling subunit of the PP_5326-PP_5329 Pst-like phosphate ABC importer.",
            "molecular_function": ATPASE_COUPLED_PHOSPHATE_TRANSPORTER,
            "directly_involved_in": [PHOSPHATE_TRANSMEMBRANE_TRANSPORT],
            "locations": [PLASMA_MEMBRANE],
            "in_complex": ABC_COMPLEX,
            "support": [
                support_goa("pstB2", "GO:0015415", "ATPase-coupled phosphate ion transmembrane transporter activity"),
                support_uniprot("pstB2", "Full=Phosphate import ATP-binding protein PstB 2"),
                support_asta("pstB2", "Protein Description:** RecName: Full=Phosphate import ATP-binding protein PstB 2"),
            ],
        },
    },
    "PP_5327": {
        "symbol": "PP_5327",
        "description": (
            "PP_5327 encodes a PstA-like multi-pass inner-membrane permease component of the "
            "PP_5326-PP_5329 Pst-like phosphate ABC importer. Its PstA-specific domain, "
            "binding-protein-dependent transport-system family assignment, and adjacent pstB2, "
            "PP_5328, and phosphate-binding PP_5329 genes support phosphate translocation across the plasma membrane."
        ),
        "uniprot_text": "Full=Phosphate transport system permease protein PstA",
        "asta_text": "Protein Description:** RecName: Full=Phosphate transport system permease protein PstA",
        "reviews": {
            "GO:0005315": (
                "Phosphate transmembrane transporter activity is appropriate for this PstA-like permease component.",
                "ACCEPT",
                "PP_5327 is the PstA-family membrane permease in the second Pst-like phosphate transport system.",
                "Full=Phosphate transport system permease protein PstA",
            ),
            "GO:0005886": (
                "Plasma membrane localization is appropriate for this multi-pass bacterial inner-membrane permease.",
                "ACCEPT",
                "UniProt predicts PP_5327 as a cell-inner-membrane and cell-membrane multi-pass membrane protein.",
                "Cell inner membrane",
            ),
            "GO:0016020": (
                "Membrane localization is correct but less specific than plasma membrane for this bacterial inner-membrane permease.",
                "MARK_AS_OVER_ANNOTATED",
                "The plasma membrane annotation is the more informative retained location.",
                "Cell membrane",
            ),
            "GO:0035435": (
                "Phosphate ion transmembrane transport is appropriate process context for PP_5327.",
                "ACCEPT",
                "The PstA-specific permease assignment and phosphate transport annotation support phosphate movement across the membrane.",
                "Phosphate_PstA",
            ),
            "GO:0043190": (
                "ABC transporter complex membership is appropriate for PP_5327.",
                "ACCEPT",
                "PP_5327 is a binding-protein-dependent transport-system permease in the local Pst-like phosphate importer.",
                "Belongs to the binding-protein-dependent transport system",
            ),
            "GO:0055085": (
                "Transmembrane transport is true but broad relative to phosphate ion transmembrane transport.",
                "MARK_AS_OVER_ANNOTATED",
                "The PstA-specific domain and phosphate transport annotations support phosphate-specific transport.",
                "Phosphate_PstA",
            ),
        },
        "new": [
            new_annotation(
                ATPASE_COUPLED_PHOSPHATE_TRANSPORTER,
                "contributes_to",
                "PP_5327",
                "PP_5327 contributes a membrane-channel component of ATPase-coupled phosphate ion transporter activity.",
                "The local PP_5326-PP_5329 Pst-like importer uses PP_5327 and PP_5328 permeases plus the PstB2 ATPase component for phosphate import.",
                [
                    support_uniprot("PP_5327", "Full=Phosphate transport system permease protein PstA"),
                    support_uniprot("PP_5327", "Phosphate_PstA"),
                ],
            ),
        ],
        "core": {
            "description": "PstA-like multi-pass permease component of the PP_5326-PP_5329 phosphate ABC importer.",
            "contributes_to_molecular_function": ATPASE_COUPLED_PHOSPHATE_TRANSPORTER,
            "directly_involved_in": [PHOSPHATE_TRANSMEMBRANE_TRANSPORT],
            "locations": [PLASMA_MEMBRANE],
            "in_complex": ABC_COMPLEX,
            "support": [
                support_goa("PP_5327", "GO:0035435", "phosphate ion transmembrane transport"),
                support_uniprot("PP_5327", "Full=Phosphate transport system permease protein PstA"),
                support_asta("PP_5327", "Protein Description:** RecName: Full=Phosphate transport system permease protein PstA"),
            ],
        },
    },
    "PP_5328": {
        "symbol": "PP_5328",
        "description": (
            "PP_5328 encodes the second multi-pass membrane permease component of the "
            "PP_5326-PP_5329 Pst-like phosphate ABC importer. UniProt names it as a phosphate "
            "transport system permease protein and places it in the binding-protein-dependent "
            "transport-system permease family."
        ),
        "uniprot_text": "Full=Phosphate transport system permease protein",
        "asta_text": "Protein Description:** SubName: Full=Phosphate transport system permease protein",
        "reviews": {
            "GO:0005886": (
                "Plasma membrane localization is appropriate for this multi-pass bacterial membrane permease.",
                "ACCEPT",
                "UniProt predicts PP_5328 as a cell-membrane multi-pass membrane protein.",
                "Cell membrane",
            ),
            "GO:0016020": (
                "Membrane localization is correct but less specific than plasma membrane for this bacterial membrane permease.",
                "MARK_AS_OVER_ANNOTATED",
                "The plasma membrane annotation is the more informative retained location.",
                "Cell membrane",
            ),
            "GO:0043190": (
                "ABC transporter complex membership is appropriate for PP_5328.",
                "ACCEPT",
                "PP_5328 is a binding-protein-dependent transport-system permease in the local Pst-like phosphate importer.",
                "Belongs to the binding-protein-dependent transport system",
            ),
            "GO:0055085": (
                "Transmembrane transport is true but broad relative to phosphate ion transmembrane transport.",
                "MARK_AS_OVER_ANNOTATED",
                "The product name and local PP_5326-PP_5329 transporter context support phosphate-specific transmembrane transport.",
                "Full=Phosphate transport system permease protein",
            ),
        },
        "new": [
            new_annotation(
                PHOSPHATE_TRANSMEMBRANE_TRANSPORT,
                "involved_in",
                "PP_5328",
                "PP_5328 should be represented with phosphate ion transmembrane transport.",
                "UniProt names PP_5328 as a phosphate transport system permease and places it in the binding-protein-dependent transport-system permease family.",
                [
                    support_uniprot("PP_5328", "Full=Phosphate transport system permease protein"),
                    support_uniprot("PP_5328", "Belongs to the binding-protein-dependent transport system"),
                    support_asta("PP_5328", "Protein Description:** SubName: Full=Phosphate transport system permease protein"),
                ],
            ),
            new_annotation(
                PHOSPHATE_TRANSPORTER,
                "enables",
                "PP_5328",
                "PP_5328 should be represented with phosphate transmembrane transporter activity.",
                "The protein is annotated as a phosphate transport system permease in an ABC-transmembrane type-1 domain-containing family.",
                [
                    support_uniprot("PP_5328", "Full=Phosphate transport system permease protein"),
                    support_uniprot("PP_5328", "ABC transmembrane type-1"),
                ],
            ),
            new_annotation(
                ATPASE_COUPLED_PHOSPHATE_TRANSPORTER,
                "contributes_to",
                "PP_5328",
                "PP_5328 contributes the second membrane-channel component of ATPase-coupled phosphate ion transporter activity.",
                "The local PP_5326-PP_5329 Pst-like importer pairs this permease with PP_5327, PstB2, and the phosphate-binding PP_5329 component.",
                [
                    support_uniprot("PP_5328", "Full=Phosphate transport system permease protein"),
                    support_uniprot("PP_5328", "ABC transmembrane type-1"),
                ],
            ),
        ],
        "core": {
            "description": "Multi-pass permease component of the PP_5326-PP_5329 phosphate ABC importer.",
            "contributes_to_molecular_function": ATPASE_COUPLED_PHOSPHATE_TRANSPORTER,
            "directly_involved_in": [PHOSPHATE_TRANSMEMBRANE_TRANSPORT],
            "locations": [PLASMA_MEMBRANE],
            "in_complex": ABC_COMPLEX,
            "support": [
                support_uniprot("PP_5328", "Full=Phosphate transport system permease protein"),
                support_uniprot("PP_5328", "Belongs to the binding-protein-dependent transport system"),
                support_asta("PP_5328", "Protein Description:** SubName: Full=Phosphate transport system permease protein"),
            ],
        },
    },
    "PP_5329": {
        "symbol": "PP_5329",
        "description": (
            "PP_5329 encodes a periplasmic PstS-family phosphate-binding component of the "
            "PP_5326-PP_5329 Pst-like phosphate ABC importer. UniProt describes it as involved "
            "in phosphate transport across the cytoplasmic membrane and assigns phosphate ion binding."
        ),
        "uniprot_text": "Full=Phosphate-binding protein",
        "asta_text": "Protein Description:** RecName: Full=Phosphate-binding protein",
        "reviews": {
            "GO:0005576": (
                "Extracellular region is a broad secreted/periplasmic location; periplasmic space is the more informative bacterial location.",
                "MARK_AS_OVER_ANNOTATED",
                "UniProt places PP_5329 in the periplasm and also marks it secreted, so the retained periplasmic annotation should be preferred.",
                "Secreted",
            ),
            "GO:0006817": (
                "Phosphate ion transport is correct but less specific than phosphate ion transmembrane transport for this PstS-like substrate-binding component.",
                "MARK_AS_OVER_ANNOTATED",
                "UniProt describes PP_5329 as involved in phosphate transport across the cytoplasmic membrane, supporting GO:0035435 as the more specific process.",
                "Involved in the system for phosphate transport across the",
            ),
            "GO:0007155": (
                "Cell adhesion appears to be an over-propagated electronic annotation for this PstS-family phosphate-binding protein.",
                "REMOVE",
                "The local evidence supports a periplasmic phosphate-binding component of an ABC importer, not a cell-adhesion role.",
                "Full=Phosphate-binding protein",
            ),
            "GO:0042301": (
                "Phosphate ion binding is the direct molecular function for this PstS-family substrate-binding component.",
                "ACCEPT",
                "The product name, Phos-bd domain, and UniRule GO annotation support phosphate binding.",
                "Full=Phosphate-binding protein",
            ),
            "GO:0042597": (
                "Periplasmic space localization is appropriate for this Gram-negative solute-binding component.",
                "ACCEPT",
                "UniProt places PP_5329 in the periplasm.",
                "Periplasm",
            ),
        },
        "new": [
            new_annotation(
                PHOSPHATE_TRANSMEMBRANE_TRANSPORT,
                "involved_in",
                "PP_5329",
                "PP_5329 should be represented with phosphate ion transmembrane transport as the PstS-like solute-binding component.",
                "UniProt describes PP_5329 as involved in phosphate transport across the cytoplasmic membrane.",
                [
                    support_uniprot("PP_5329", "Involved in the system for phosphate transport across the"),
                    support_uniprot("PP_5329", "cytoplasmic membrane"),
                    support_asta("PP_5329", "Protein Description:** RecName: Full=Phosphate-binding protein"),
                ],
            ),
            new_annotation(
                ABC_COMPLEX,
                "part_of",
                "PP_5329",
                "PP_5329 should be represented as the solute-binding component of the Pst-like ABC transporter complex.",
                "UniProt and domain annotations identify PP_5329 as a phosphate ABC transporter periplasmic phosphate-binding protein.",
                [
                    support_uniprot("PP_5329", "Phosphate ABC transporter periplasmic phosphate-binding protein"),
                    support_uniprot("PP_5329", "PANTHER; PTHR30570; PERIPLASMIC PHOSPHATE BINDING COMPONENT OF PHOSPHATE ABC TRANSPORTER"),
                ],
            ),
        ],
        "core": {
            "description": "Periplasmic phosphate-binding solute-binding component of the PP_5326-PP_5329 phosphate ABC importer.",
            "molecular_function": PHOSPHATE_BINDING,
            "directly_involved_in": [PHOSPHATE_TRANSMEMBRANE_TRANSPORT],
            "locations": [{"id": "GO:0042597", "label": "periplasmic space"}],
            "in_complex": ABC_COMPLEX,
            "support": [
                support_goa("PP_5329", "GO:0042301", "phosphate ion binding"),
                support_uniprot("PP_5329", "Full=Phosphate-binding protein"),
                support_asta("PP_5329", "Protein Description:** RecName: Full=Phosphate-binding protein"),
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
            asta_text=cfg["asta_text"] if action in {"ACCEPT", "MODIFY"} else None,
        )

    doc["existing_annotations"].extend(cfg.get("new", []))

    core = dict(cfg["core"])
    support = core.pop("support")
    core["supported_by"] = support
    doc["core_functions"] = [core]
    doc["proposed_new_terms"] = []
    doc["suggested_questions"] = [
        {
            "question": "How are the PP_2656-PP_2659 and PP_5326-PP_5329 Pst-like phosphate import systems regulated and partitioned under phosphate limitation in KT2440?"
        }
    ]
    doc["suggested_experiments"] = [
        {
            "description": "Measure phosphate uptake and growth under phosphate limitation in single-locus and double-locus Pst transporter mutants, with complementation of the PP_2656-PP_2659 locus.",
            "experiment_type": "targeted phosphate transporter mutant uptake and phosphate-limitation growth assay",
        }
    ]

    path.write_text(yaml.safe_dump(doc, sort_keys=False, width=1000))
    print(f"curated {path}")


def main() -> None:
    for gene, cfg in CONFIG.items():
        curate_gene(gene, cfg)


if __name__ == "__main__":
    main()
