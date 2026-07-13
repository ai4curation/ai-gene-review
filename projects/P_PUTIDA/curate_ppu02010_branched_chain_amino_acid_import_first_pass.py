#!/usr/bin/env python3
"""First-pass curation for the ppu02010 PP_1137-PP_1141 LivFGMHK importer."""

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


BCAA_ACTIVITY = {
    "id": "GO:0015658",
    "label": "branched-chain amino acid transmembrane transporter activity",
}
BCAA_TRANSPORT = {"id": "GO:0015803", "label": "branched-chain amino acid transport"}
L_VALINE_ACTIVITY = {"id": "GO:0005304", "label": "L-valine transmembrane transporter activity"}
L_ISOLEUCINE_ACTIVITY = {
    "id": "GO:0015188",
    "label": "L-isoleucine transmembrane transporter activity",
}
L_LEUCINE_ACTIVITY = {"id": "GO:0015190", "label": "L-leucine transmembrane transporter activity"}
L_VALINE_TRANSPORT = {"id": "GO:1903785", "label": "L-valine transmembrane transport"}
L_VALINE_IMPORT = {"id": "GO:1903805", "label": "L-valine import across plasma membrane"}
L_ISOLEUCINE_IMPORT = {
    "id": "GO:1903806",
    "label": "L-isoleucine import across plasma membrane",
}
L_LEUCINE_IMPORT = {"id": "GO:1903801", "label": "L-leucine import across plasma membrane"}
L_LEUCINE_BINDING = {"id": "GO:0070728", "label": "L-leucine binding"}
ATP_BINDING = {"id": "GO:0005524", "label": "ATP binding"}
ATP_HYDROLYSIS = {"id": "GO:0016887", "label": "ATP hydrolysis activity"}
ABC_COMPLEX = {
    "id": "GO:0043190",
    "label": "ATP-binding cassette (ABC) transporter complex",
}
PLASMA_MEMBRANE = {"id": "GO:0005886", "label": "plasma membrane"}
PERIPLASM = {"id": "GO:0030288", "label": "outer membrane-bounded periplasmic space"}


BCAA_PROCESS_TERMS = [BCAA_TRANSPORT]
LIV_SUBSTRATE_ACTIVITY_TERMS = [L_VALINE_ACTIVITY, L_ISOLEUCINE_ACTIVITY, L_LEUCINE_ACTIVITY]
LIV_SUBSTRATE_PROCESS_TERMS = [L_VALINE_IMPORT, L_ISOLEUCINE_IMPORT, L_LEUCINE_IMPORT]
LIVH_SUBSTRATE_PROCESS_TERMS = [L_VALINE_TRANSPORT, L_ISOLEUCINE_IMPORT, L_LEUCINE_IMPORT]


CONFIG = {
    "livF-I": {
        "symbol": "livF-I",
        "description": (
            "livF-I (PP_1137) encodes a predicted ATP-binding energy-coupling "
            "subunit of the PP_1137-PP_1141 LivFGMHK high-affinity branched-chain "
            "amino-acid ABC uptake system. Its ABC ATPase domain supports ATP "
            "hydrolysis-driven transport together with the LivM/LivH membrane "
            "permeases, the LivG ATP-binding partner, and the LivK periplasmic "
            "leucine/branched-chain amino-acid binding component."
        ),
        "uniprot_text": "Full=High-affinity branched-chain amino acid transport ATP-binding protein",
        "asta_text": "Protein Description:** RecName: Full=High-affinity branched-chain amino acid transport ATP-binding protein",
        "reviews": {
            "GO:0000166": (
                "Nucleotide binding is true but less informative than ATP binding for this ABC ATPase.",
                "MARK_AS_OVER_ANNOTATED",
                "The review retains the more specific ATP-binding and ATP-hydrolysis annotations for the transporter ATPase.",
                None,
                [support_uniprot("livF-I", "Full=High-affinity branched-chain amino acid transport ATP-binding protein")],
            ),
            "GO:0003333": (
                "Amino acid transmembrane transport is correct but too broad for the Liv branched-chain amino-acid ABC importer context.",
                "MODIFY",
                "The product name and PANTHER subfamily identify LivF as a high-affinity branched-chain amino-acid transport ATP-binding protein, so branched-chain amino acid transport is the better process term.",
                [BCAA_TRANSPORT],
                [support_uniprot("livF-I", "PANTHER; PTHR43820:SF4; HIGH-AFFINITY BRANCHED-CHAIN AMINO ACID TRANSPORT ATP-BINDING PROTEIN LIVF; 1.")],
            ),
            "GO:0005524": (
                "ATP binding is correct for the ABC-transporter nucleotide-binding component.",
                "ACCEPT",
                "LivF has an ABC transporter ATP-binding domain and is named as the ATP-binding component of a high-affinity branched-chain amino-acid transport system.",
                None,
                [support_uniprot("livF-I", "FT   DOMAIN          2..233")],
            ),
            "GO:0015658": (
                "Branched-chain amino acid transmembrane transporter activity is appropriate as the complex-level function to which this ATPase contributes.",
                "ACCEPT",
                "The product name and PANTHER subfamily support LivF as an ATP-binding component of a high-affinity branched-chain amino-acid ABC transporter.",
                None,
                [support_uniprot("livF-I", "Full=High-affinity branched-chain amino acid transport ATP-binding protein")],
            ),
            "GO:0015803": (
                "Branched-chain amino acid transport is the correct first-pass process for this Liv ATP-binding component.",
                "ACCEPT",
                "The PP_1137-PP_1141 locus is named and classified as a Liv branched-chain amino-acid ABC uptake system.",
                None,
                [support_asta("livF-I", "Protein Description:** RecName: Full=High-affinity branched-chain amino acid transport ATP-binding protein")],
            ),
            "GO:0015804": (
                "Neutral amino acid transport is compatible with branched-chain amino-acid uptake but less informative than the BCAA-specific process.",
                "MARK_AS_OVER_ANNOTATED",
                "The BCAA-specific GOA and UniProt/PANTHER evidence provide a more precise process assignment for this Liv system.",
                None,
                [support_uniprot("livF-I", "PANTHER; PTHR43820:SF4; HIGH-AFFINITY BRANCHED-CHAIN AMINO ACID TRANSPORT ATP-BINDING PROTEIN LIVF; 1.")],
            ),
            "GO:0015807": (
                "L-amino acid transport is true but too general for the Liv BCAA transporter ATPase.",
                "MARK_AS_OVER_ANNOTATED",
                "The specific branched-chain amino acid transport annotation should be used as the core process.",
                None,
                [support_uniprot("livF-I", "Full=High-affinity branched-chain amino acid transport ATP-binding protein")],
            ),
            "GO:0016887": (
                "ATP hydrolysis activity is the correct mechanistic activity for this ABC ATPase subunit.",
                "ACCEPT",
                "ATP hydrolysis by LivF is expected to provide energy coupling to the Liv branched-chain amino-acid ABC importer.",
                None,
                [support_uniprot("livF-I", "FT   DOMAIN          2..233")],
            ),
            "GO:1905039": (
                "Carboxylic acid transmembrane transport is too broad and chemically indirect for this Liv BCAA importer.",
                "MARK_AS_OVER_ANNOTATED",
                "The specific branched-chain amino acid transport annotation captures the supported substrate class without broadening to all carboxylic acids.",
                None,
                [support_goa("livF-I", "GO:0015803", "branched-chain amino acid transport")],
            ),
        },
        "new_annotations": [
            {
                "term": ABC_COMPLEX,
                "qualifier": "part_of",
                "summary": "ABC transporter complex membership is appropriate for this LivF ATP-binding component.",
                "reason": "LivF is named and classified as an ATP-binding subunit of the adjacent LivFGMHK branched-chain amino-acid ABC transporter.",
                "supporting_text": "Full=High-affinity branched-chain amino acid transport ATP-binding protein",
            }
        ],
        "core": {
            "description": "ATP-binding energy-coupling subunit contributing to a predicted LivFGMHK branched-chain amino-acid ABC uptake system.",
            "molecular_function": ATP_HYDROLYSIS,
            "contributes_to_molecular_function": BCAA_ACTIVITY,
            "directly_involved_in": BCAA_PROCESS_TERMS,
            "in_complex": ABC_COMPLEX,
            "support": ("GO:0016887", "ATP hydrolysis activity"),
        },
    },
    "livG": {
        "symbol": "livG",
        "description": (
            "livG (PP_1138) encodes the second predicted ATP-binding "
            "energy-coupling subunit of the PP_1137-PP_1141 LivFGMHK "
            "branched-chain amino-acid ABC uptake system. Automated annotations "
            "and PANTHER classification support an ATPase role in valine and "
            "isoleucine import with the adjacent LivF, LivM, LivH, and LivK "
            "transporter components."
        ),
        "uniprot_text": "Full=Branched chain amino acid transporter-ATP binding subunit",
        "asta_text": "Protein Description:** SubName: Full=Branched chain amino acid transporter-ATP binding subunit",
        "reviews": {
            "GO:0000166": (
                "Nucleotide binding is true but less informative than ATP binding for this ABC ATPase.",
                "MARK_AS_OVER_ANNOTATED",
                "The review retains the more specific ATP-binding and ATP-hydrolysis annotations for the transporter ATPase.",
            ),
            "GO:0005304": (
                "L-valine transmembrane transporter activity is consistent with the Liv branched-chain amino-acid ABC importer.",
                "ACCEPT",
                "LivG is classified as a high-affinity branched-chain amino-acid transport ATP-binding protein and has valine import process annotations.",
                None,
                [support_uniprot("livG", "PANTHER; PTHR45772:SF11; HIGH-AFFINITY BRANCHED-CHAIN AMINO ACID TRANSPORT ATP-BINDING PROTEIN LIVG; 1.")],
            ),
            "GO:0005524": (
                "ATP binding is correct for the ABC-transporter nucleotide-binding component.",
                "ACCEPT",
                "LivG has an ABC transporter ATP-binding domain and is named as the ATP-binding subunit of a branched-chain amino-acid transporter.",
                None,
                [support_uniprot("livG", "FT   DOMAIN          6..254")],
            ),
            "GO:0005886": (
                "Plasma membrane localization is appropriate for a membrane-associated bacterial ABC transporter ATPase at first pass.",
                "ACCEPT",
                "The GOA row places LivG at the plasma membrane, consistent with its role in the inner-membrane Liv ABC transporter complex.",
            ),
            "GO:0015188": (
                "L-isoleucine transmembrane transporter activity is consistent with the Liv branched-chain amino-acid ABC importer.",
                "ACCEPT",
                "The LivG PANTHER subfamily and isoleucine import annotations support this substrate-specific activity at the complex level.",
                None,
                [support_uniprot("livG", "PANTHER; PTHR45772:SF11; HIGH-AFFINITY BRANCHED-CHAIN AMINO ACID TRANSPORT ATP-BINDING PROTEIN LIVG; 1.")],
            ),
            "GO:0015192": (
                "L-phenylalanine transporter activity may reflect broad hydrophobic-amino-acid family transfer rather than the core Liv BCAA assignment.",
                "MARK_AS_OVER_ANNOTATED",
                "The local product names and PANTHER subfamily support a branched-chain amino-acid transporter; phenylalanine transport is not promoted to core without PSEPK-specific substrate evidence.",
                None,
                [support_uniprot("livG", "Full=Branched chain amino acid transporter-ATP binding subunit")],
            ),
            "GO:0015808": (
                "L-alanine transport is plausible only as a broad-family transfer and is not the core LivFGMHK function.",
                "MARK_AS_OVER_ANNOTATED",
                "The strongest locus-level evidence supports branched-chain amino-acid uptake, not alanine transport.",
                None,
                [support_uniprot("livG", "Full=Branched chain amino acid transporter-ATP binding subunit")],
            ),
            "GO:0015823": (
                "Phenylalanine transport is not supported as the core function of this Liv branched-chain amino-acid ATPase.",
                "MARK_AS_OVER_ANNOTATED",
                "The review treats phenylalanine transport as a hydrophobic-amino-acid family spillover pending direct substrate evidence.",
                None,
                [support_uniprot("livG", "PANTHER; PTHR45772:SF11; HIGH-AFFINITY BRANCHED-CHAIN AMINO ACID TRANSPORT ATP-BINDING PROTEIN LIVG; 1.")],
            ),
            "GO:0016887": (
                "ATP hydrolysis activity is the correct mechanistic activity for this ABC ATPase subunit.",
                "ACCEPT",
                "ATP hydrolysis by LivG is expected to provide energy coupling to the Liv branched-chain amino-acid ABC importer.",
                None,
                [support_uniprot("livG", "FT   DOMAIN          6..254")],
            ),
            "GO:0042941": (
                "D-alanine transmembrane transport is not part of the core Liv branched-chain amino-acid uptake assignment.",
                "MARK_AS_OVER_ANNOTATED",
                "The local evidence supports LivG as a high-affinity BCAA transporter ATP-binding protein; D-alanine transport is treated as over-propagated family context.",
                None,
                [support_uniprot("livG", "Full=Branched chain amino acid transporter-ATP binding subunit")],
            ),
            "GO:1903714": (
                "Isoleucine transmembrane transport is directionally correct but less precise than the existing L-isoleucine import term.",
                "MODIFY",
                "The GOA also has L-isoleucine import across plasma membrane, which better captures the expected bacterial uptake direction and stereochemistry.",
                [L_ISOLEUCINE_IMPORT],
                [support_goa("livG", "GO:1903806", "L-isoleucine import across plasma membrane")],
            ),
            "GO:1903785": (
                "L-valine transmembrane transport is consistent with the Liv BCAA uptake system.",
                "ACCEPT",
                "LivG is a branched-chain amino-acid transporter ATP-binding subunit and has a matching L-valine import annotation.",
                None,
                [support_goa("livG", "GO:1903805", "L-valine import across plasma membrane")],
            ),
            "GO:1903805": (
                "L-valine import across the plasma membrane is an appropriate substrate-specific process for this Liv importer component.",
                "ACCEPT",
                "The product name and PANTHER subfamily support LivG as part of a high-affinity branched-chain amino-acid ABC importer.",
                None,
                [support_uniprot("livG", "PANTHER; PTHR45772:SF11; HIGH-AFFINITY BRANCHED-CHAIN AMINO ACID TRANSPORT ATP-BINDING PROTEIN LIVG; 1.")],
            ),
            "GO:1903806": (
                "L-isoleucine import across the plasma membrane is an appropriate substrate-specific process for this Liv importer component.",
                "ACCEPT",
                "The product name and PANTHER subfamily support LivG as part of a high-affinity branched-chain amino-acid ABC importer.",
                None,
                [support_uniprot("livG", "PANTHER; PTHR45772:SF11; HIGH-AFFINITY BRANCHED-CHAIN AMINO ACID TRANSPORT ATP-BINDING PROTEIN LIVG; 1.")],
            ),
        },
        "new_annotations": [
            {
                "term": BCAA_ACTIVITY,
                "qualifier": "contributes_to",
                "summary": "Branched-chain amino acid transmembrane transporter activity captures the complex-level activity to which LivG contributes.",
                "reason": "LivG is an ATP-binding subunit of the adjacent LivFGMHK branched-chain amino-acid ABC transporter.",
                "supporting_text": "PANTHER; PTHR45772:SF11; HIGH-AFFINITY BRANCHED-CHAIN AMINO ACID TRANSPORT ATP-BINDING PROTEIN LIVG; 1.",
            },
            {
                "term": ABC_COMPLEX,
                "qualifier": "part_of",
                "summary": "ABC transporter complex membership is appropriate for this LivG ATP-binding component.",
                "reason": "LivG is named and classified as an ATP-binding subunit of the adjacent LivFGMHK branched-chain amino-acid ABC transporter.",
                "supporting_text": "Full=Branched chain amino acid transporter-ATP binding subunit",
            },
        ],
        "core": {
            "description": "Second ATP-binding energy-coupling subunit contributing to a predicted LivFGMHK branched-chain amino-acid ABC uptake system.",
            "molecular_function": ATP_HYDROLYSIS,
            "contributes_to_molecular_function": BCAA_ACTIVITY,
            "directly_involved_in": [L_VALINE_IMPORT, L_ISOLEUCINE_IMPORT],
            "locations": [PLASMA_MEMBRANE],
            "in_complex": ABC_COMPLEX,
            "support": ("GO:0016887", "ATP hydrolysis activity"),
        },
    },
    "livM": {
        "symbol": "livM",
        "description": (
            "livM (PP_1139) encodes a predicted multi-pass inner-membrane "
            "permease component of the PP_1137-PP_1141 LivFGMHK high-affinity "
            "branched-chain amino-acid ABC uptake system. Its LivM-like "
            "binding-protein-dependent transporter domains support a channel "
            "role in branched-chain amino-acid import rather than independent "
            "ATPase or soluble substrate-binding activity."
        ),
        "uniprot_text": "Full=Branched chain amino acid transporter-permease subunit",
        "asta_text": "Protein Description:** SubName: Full=Branched chain amino acid transporter-permease subunit",
        "reviews": {
            "GO:0005886": (
                "Plasma membrane localization is appropriate for this predicted inner-membrane ABC permease.",
                "ACCEPT",
                "UniProt predicts LivM as a cell inner-membrane multi-pass membrane protein.",
                None,
                [support_uniprot("livM", "Cell inner membrane")],
            ),
            "GO:0015658": (
                "Branched-chain amino acid transmembrane transporter activity is appropriate as the complex-level function to which this permease contributes.",
                "ACCEPT",
                "The product name and PANTHER subfamily identify LivM as a high-affinity branched-chain amino-acid transport-system permease.",
                None,
                [support_uniprot("livM", "PANTHER; PTHR30482:SF20; HIGH-AFFINITY BRANCHED-CHAIN AMINO ACID TRANSPORT SYSTEM PERMEASE PROTEIN LIVM; 1.")],
            ),
            "GO:0015803": (
                "Branched-chain amino acid transport is the correct first-pass process for this Liv permease.",
                "ACCEPT",
                "The PP_1137-PP_1141 locus is named and classified as a Liv branched-chain amino-acid ABC uptake system.",
                None,
                [support_asta("livM", "Protein Description:** SubName: Full=Branched chain amino acid transporter-permease subunit")],
            ),
            "GO:0016020": (
                "Membrane localization is true but less informative than plasma membrane for this bacterial inner-membrane permease.",
                "MARK_AS_OVER_ANNOTATED",
                "The record also has a plasma-membrane annotation and UniProt predicts a cell inner-membrane multi-pass protein.",
                None,
                [support_uniprot("livM", "Cell inner membrane")],
            ),
            "GO:0022857": (
                "Generic transmembrane transporter activity is too broad for this Liv ABC-transporter permease component.",
                "MODIFY",
                "The product name and LivM PANTHER subfamily support branched-chain amino acid transmembrane transporter activity as the better complex-level activity.",
                [BCAA_ACTIVITY],
                [support_uniprot("livM", "Full=Branched chain amino acid transporter-permease subunit")],
            ),
            "GO:0055085": (
                "Transmembrane transport is true but broad relative to the branched-chain amino-acid ABC-import context.",
                "MODIFY",
                "Branched-chain amino acid transport better captures the expected substrate class for this LivM permease.",
                [BCAA_TRANSPORT],
                [support_uniprot("livM", "PANTHER; PTHR30482:SF20; HIGH-AFFINITY BRANCHED-CHAIN AMINO ACID TRANSPORT SYSTEM PERMEASE PROTEIN LIVM; 1.")],
            ),
        },
        "new_annotations": [
            {
                "term": ABC_COMPLEX,
                "qualifier": "part_of",
                "summary": "ABC transporter complex membership is appropriate for this LivM permease.",
                "reason": "LivM is a permease subunit in the adjacent LivFGMHK branched-chain amino-acid ABC transporter locus.",
                "supporting_text": "Full=Branched chain amino acid transporter-permease subunit",
            }
        ],
        "core": {
            "description": "Multi-pass permease component contributing to a predicted LivFGMHK branched-chain amino-acid ABC uptake system.",
            "contributes_to_molecular_function": BCAA_ACTIVITY,
            "directly_involved_in": BCAA_PROCESS_TERMS,
            "locations": [PLASMA_MEMBRANE],
            "in_complex": ABC_COMPLEX,
            "support": ("GO:0015658", "branched-chain amino acid transmembrane transporter activity"),
        },
    },
    "livH": {
        "symbol": "livH",
        "description": (
            "livH (PP_1140) encodes a predicted multi-pass inner-membrane "
            "permease component of the PP_1137-PP_1141 LivFGMHK high-affinity "
            "branched-chain amino-acid ABC uptake system. Automated annotations "
            "support valine, isoleucine, and leucine transporter activity, while "
            "the adjacent LivK substrate-binding protein provides additional "
            "leucine/branched-chain amino-acid context."
        ),
        "uniprot_text": "Full=Branched chain amino acid transporter-permease subunit",
        "asta_text": "Protein Description:** SubName: Full=Branched chain amino acid transporter-permease subunit",
        "reviews": {
            "GO:0005304": (
                "L-valine transmembrane transporter activity is consistent with the Liv branched-chain amino-acid ABC importer.",
                "ACCEPT",
                "The LivH PANTHER subfamily supports a high-affinity branched-chain amino-acid transport-system permease.",
                None,
                [support_uniprot("livH", "PANTHER; PTHR11795:SF371; HIGH-AFFINITY BRANCHED-CHAIN AMINO ACID TRANSPORT SYSTEM PERMEASE PROTEIN LIVH; 1.")],
            ),
            "GO:0005886": (
                "Plasma membrane localization is appropriate for this predicted inner-membrane ABC permease.",
                "ACCEPT",
                "UniProt predicts LivH as a cell inner-membrane multi-pass membrane protein.",
                None,
                [support_uniprot("livH", "Cell inner membrane")],
            ),
            "GO:0015188": (
                "L-isoleucine transmembrane transporter activity is consistent with the Liv branched-chain amino-acid ABC importer.",
                "ACCEPT",
                "The LivH PANTHER subfamily supports a high-affinity branched-chain amino-acid transport-system permease.",
                None,
                [support_uniprot("livH", "PANTHER; PTHR11795:SF371; HIGH-AFFINITY BRANCHED-CHAIN AMINO ACID TRANSPORT SYSTEM PERMEASE PROTEIN LIVH; 1.")],
            ),
            "GO:0015190": (
                "L-leucine transmembrane transporter activity is consistent with LivH in a LivFGMHK BCAA importer.",
                "ACCEPT",
                "The adjacent LivK binding protein is leucine-family, and the LivH permease is part of the high-affinity branched-chain amino-acid transport system.",
                None,
                [support_uniprot("livH", "PANTHER; PTHR11795:SF371; HIGH-AFFINITY BRANCHED-CHAIN AMINO ACID TRANSPORT SYSTEM PERMEASE PROTEIN LIVH; 1.")],
            ),
            "GO:0015192": (
                "L-phenylalanine transporter activity may reflect broad hydrophobic-amino-acid family transfer rather than the core Liv BCAA assignment.",
                "MARK_AS_OVER_ANNOTATED",
                "The local product names and PANTHER subfamilies support a branched-chain amino-acid transporter; phenylalanine transport is not promoted to core without PSEPK-specific substrate evidence.",
                None,
                [support_uniprot("livH", "Full=Branched chain amino acid transporter-permease subunit")],
            ),
            "GO:0015808": (
                "L-alanine transport is plausible only as a broad-family transfer and is not the core LivFGMHK function.",
                "MARK_AS_OVER_ANNOTATED",
                "The strongest locus-level evidence supports branched-chain amino-acid uptake, not alanine transport.",
                None,
                [support_uniprot("livH", "PANTHER; PTHR11795:SF371; HIGH-AFFINITY BRANCHED-CHAIN AMINO ACID TRANSPORT SYSTEM PERMEASE PROTEIN LIVH; 1.")],
            ),
            "GO:0015823": (
                "Phenylalanine transport is not supported as the core function of this Liv branched-chain amino-acid permease.",
                "MARK_AS_OVER_ANNOTATED",
                "The review treats phenylalanine transport as a hydrophobic-amino-acid family spillover pending direct substrate evidence.",
                None,
                [support_uniprot("livH", "Full=Branched chain amino acid transporter-permease subunit")],
            ),
            "GO:0016020": (
                "Membrane localization is true but less informative than plasma membrane for this bacterial inner-membrane permease.",
                "MARK_AS_OVER_ANNOTATED",
                "The record also has a plasma-membrane annotation and UniProt predicts a cell inner-membrane multi-pass protein.",
                None,
                [support_uniprot("livH", "Cell inner membrane")],
            ),
            "GO:0022857": (
                "Generic transmembrane transporter activity is too broad for this Liv ABC-transporter permease component.",
                "MODIFY",
                "The LivH PANTHER subfamily supports branched-chain amino acid transmembrane transporter activity as the better complex-level activity.",
                [BCAA_ACTIVITY],
                [support_uniprot("livH", "PANTHER; PTHR11795:SF371; HIGH-AFFINITY BRANCHED-CHAIN AMINO ACID TRANSPORT SYSTEM PERMEASE PROTEIN LIVH; 1.")],
            ),
            "GO:0042941": (
                "D-alanine transmembrane transport is not part of the core Liv branched-chain amino-acid uptake assignment.",
                "MARK_AS_OVER_ANNOTATED",
                "The local evidence supports LivH as a high-affinity BCAA transporter permease; D-alanine transport is treated as over-propagated family context.",
                None,
                [support_uniprot("livH", "Full=Branched chain amino acid transporter-permease subunit")],
            ),
            "GO:0055085": (
                "Transmembrane transport is true but broad relative to the branched-chain amino-acid ABC-import context.",
                "MODIFY",
                "Branched-chain amino acid transport better captures the expected substrate class for this LivH permease.",
                [BCAA_TRANSPORT],
                [support_uniprot("livH", "PANTHER; PTHR11795:SF371; HIGH-AFFINITY BRANCHED-CHAIN AMINO ACID TRANSPORT SYSTEM PERMEASE PROTEIN LIVH; 1.")],
            ),
            "GO:1903785": (
                "L-valine transmembrane transport is consistent with the Liv BCAA uptake system.",
                "ACCEPT",
                "LivH is a high-affinity branched-chain amino-acid transport-system permease.",
                None,
                [support_uniprot("livH", "PANTHER; PTHR11795:SF371; HIGH-AFFINITY BRANCHED-CHAIN AMINO ACID TRANSPORT SYSTEM PERMEASE PROTEIN LIVH; 1.")],
            ),
            "GO:1903806": (
                "L-isoleucine import across the plasma membrane is an appropriate substrate-specific process for this Liv importer component.",
                "ACCEPT",
                "The LivH permease and adjacent LivK binding protein support a BCAA uptake-system interpretation.",
                None,
                [support_uniprot("livH", "Full=Branched chain amino acid transporter-permease subunit")],
            ),
        },
        "new_annotations": [
            {
                "term": BCAA_ACTIVITY,
                "qualifier": "contributes_to",
                "summary": "Branched-chain amino acid transmembrane transporter activity captures the complex-level activity to which LivH contributes.",
                "reason": "LivH is a permease subunit of the adjacent LivFGMHK branched-chain amino-acid ABC transporter.",
                "supporting_text": "PANTHER; PTHR11795:SF371; HIGH-AFFINITY BRANCHED-CHAIN AMINO ACID TRANSPORT SYSTEM PERMEASE PROTEIN LIVH; 1.",
            },
            {
                "term": L_LEUCINE_IMPORT,
                "qualifier": "involved_in",
                "summary": "L-leucine import across the plasma membrane is a useful missing process annotation for the LivH permease.",
                "reason": "LivH has an L-leucine transporter activity annotation and is adjacent to the LivK leucine-specific binding protein.",
                "support": [
                    support_goa("livH", "GO:0015190", "L-leucine transmembrane transporter activity"),
                    support_uniprot("livH", "PANTHER; PTHR11795:SF371; HIGH-AFFINITY BRANCHED-CHAIN AMINO ACID TRANSPORT SYSTEM PERMEASE PROTEIN LIVH; 1."),
                ],
            },
            {
                "term": ABC_COMPLEX,
                "qualifier": "part_of",
                "summary": "ABC transporter complex membership is appropriate for this LivH permease.",
                "reason": "LivH is a permease subunit in the adjacent LivFGMHK branched-chain amino-acid ABC transporter locus.",
                "supporting_text": "Full=Branched chain amino acid transporter-permease subunit",
            },
        ],
        "core": {
            "description": "Multi-pass permease component contributing to a predicted LivFGMHK branched-chain amino-acid ABC uptake system.",
            "contributes_to_molecular_function": BCAA_ACTIVITY,
            "directly_involved_in": LIVH_SUBSTRATE_PROCESS_TERMS,
            "locations": [PLASMA_MEMBRANE],
            "in_complex": ABC_COMPLEX,
            "support": ("GO:0015190", "L-leucine transmembrane transporter activity"),
        },
    },
    "livK": {
        "symbol": "livK",
        "description": (
            "livK (PP_1141) encodes a signal-peptide-bearing periplasmic "
            "substrate-binding component of the PP_1137-PP_1141 LivFGMHK "
            "branched-chain amino-acid ABC uptake system. UniProt and PANTHER "
            "classify it as a leucine/branched-chain amino-acid binding protein, "
            "supporting substrate capture for leucine and related branched-chain "
            "amino acids before delivery to the LivH/LivM permease complex."
        ),
        "uniprot_text": "Full=Branched-chain amino acids ABC transporter-periplasmic leucine binding subunit",
        "asta_text": "Protein Description:** SubName: Full=Branched-chain amino acids ABC transporter-periplasmic leucine binding subunit",
        "reviews": {
            "GO:0006865": (
                "Amino acid transport is correct but too broad for the LivK leucine/branched-chain amino-acid binding component.",
                "MODIFY",
                "The product name, leucine-binding protein family assignment, and PANTHER subfamily support branched-chain amino acid transport and L-leucine import across the plasma membrane as better process terms.",
                [BCAA_TRANSPORT, L_LEUCINE_IMPORT],
                [
                    support_uniprot("livK", "Full=Branched-chain amino acids ABC transporter-periplasmic leucine binding subunit"),
                    support_uniprot("livK", "PANTHER; PTHR47151:SF3; LEUCINE-SPECIFIC-BINDING PROTEIN; 1."),
                ],
            )
        },
        "new_annotations": [
            {
                "term": L_LEUCINE_BINDING,
                "qualifier": "enables",
                "summary": "L-leucine binding captures the expected substrate-recognition function of this LivK periplasmic binding protein.",
                "reason": "UniProt names LivK as a periplasmic leucine binding subunit and PANTHER assigns the leucine-specific-binding protein subfamily.",
                "supporting_text": "PANTHER; PTHR47151:SF3; LEUCINE-SPECIFIC-BINDING PROTEIN; 1.",
            },
            {
                "term": BCAA_TRANSPORT,
                "qualifier": "involved_in",
                "summary": "Branched-chain amino acid transport is a useful missing process annotation for LivK.",
                "reason": "LivK is the periplasmic binding component of a branched-chain amino-acid ABC transporter locus.",
                "supporting_text": "Full=Branched-chain amino acids ABC transporter-periplasmic leucine binding subunit",
            },
            {
                "term": L_LEUCINE_IMPORT,
                "qualifier": "involved_in",
                "summary": "L-leucine import across the plasma membrane is a useful missing process annotation for LivK.",
                "reason": "LivK is named as a periplasmic leucine binding subunit and is assigned to a leucine-specific binding-protein subfamily.",
                "supporting_text": "PANTHER; PTHR47151:SF3; LEUCINE-SPECIFIC-BINDING PROTEIN; 1.",
            },
            {
                "term": BCAA_ACTIVITY,
                "qualifier": "contributes_to",
                "summary": "LivK contributes substrate recognition to the branched-chain amino acid transmembrane transporter activity of the Liv complex.",
                "reason": "As a periplasmic solute-binding component, LivK supplies substrate capture rather than catalyzing membrane translocation alone.",
                "supporting_text": "Full=Branched-chain amino acids ABC transporter-periplasmic leucine binding subunit",
            },
            {
                "term": PERIPLASM,
                "qualifier": "located_in",
                "summary": "Periplasmic localization is appropriate for this signal-peptide-bearing bacterial substrate-binding protein.",
                "reason": "The product name identifies LivK as a periplasmic binding subunit and UniProt predicts an N-terminal signal peptide.",
                "supporting_text": "FT   SIGNAL          1..22",
            },
            {
                "term": ABC_COMPLEX,
                "qualifier": "part_of",
                "summary": "ABC transporter complex membership is appropriate for this LivK substrate-binding component.",
                "reason": "LivK is named as the periplasmic leucine binding subunit of the adjacent branched-chain amino-acid ABC transporter locus.",
                "supporting_text": "Full=Branched-chain amino acids ABC transporter-periplasmic leucine binding subunit",
            },
        ],
        "core": {
            "description": "Periplasmic L-leucine/branched-chain amino-acid substrate-binding component contributing substrate capture to a predicted LivFGMHK ABC uptake system.",
            "molecular_function": L_LEUCINE_BINDING,
            "contributes_to_molecular_function": BCAA_ACTIVITY,
            "directly_involved_in": [BCAA_TRANSPORT, L_LEUCINE_IMPORT],
            "locations": [PERIPLASM],
            "in_complex": ABC_COMPLEX,
            "support": None,
            "support_in_goa": False,
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
        ann
        for ann in doc.get("existing_annotations", [])
        if not (
            ann.get("original_reference_id") == uniprot_ref(gene)
            and ann.get("review", {}).get("action") == "NEW"
        )
    ]

    for ann in doc.get("existing_annotations", []):
        term = ann["term"]
        term_id = term["id"]
        label = term["label"]
        entry = cfg["reviews"][term_id]
        proposed = entry[3] if len(entry) > 3 else None
        extra_support = entry[4] if len(entry) > 4 else None
        ann["review"] = review(
            gene,
            term_id,
            label,
            entry[0],
            entry[1],
            entry[2],
            proposed=proposed,
            extra_support=extra_support,
        )

    existing_term_ids = {ann["term"]["id"] for ann in doc.get("existing_annotations", [])}
    for extra in cfg.get("new_annotations", []):
        term = extra["term"]
        if term["id"] in existing_term_ids:
            continue
        supported_by = extra.get("support") or [
            support_uniprot(gene, extra["supporting_text"]),
            support_asta(gene, cfg["asta_text"]),
        ]
        doc.setdefault("existing_annotations", []).append(
            new_annotation(
                term,
                extra["qualifier"],
                uniprot_ref(gene),
                extra["summary"],
                extra["reason"],
                supported_by,
            )
        )
        existing_term_ids.add(term["id"])

    core = deepcopy(cfg["core"])
    support_term = core.pop("support", None)
    support_in_goa = core.pop("support_in_goa", True)
    core["supported_by"] = []
    if support_term and support_in_goa:
        core["supported_by"].append(support_goa(gene, support_term[0], support_term[1]))
    core["supported_by"].extend(
        [
            support_uniprot(gene, cfg["uniprot_text"]),
            support_asta(gene, cfg["asta_text"]),
        ]
    )
    doc["core_functions"] = [core]
    doc["proposed_new_terms"] = []
    doc["suggested_questions"] = [
        {
            "question": "What is the in vivo substrate range of the PP_1137-PP_1141 LivFGMHK ABC importer in P. putida KT2440, and does LivK confer strongest specificity for L-leucine versus L-isoleucine or L-valine?"
        }
    ]
    doc["suggested_experiments"] = [
        {
            "description": "Measure uptake and growth phenotypes for livF-I, livG, livM, livH, and livK mutants with L-leucine, L-isoleucine, L-valine, and non-BCAA hydrophobic amino acids supplied as nitrogen or carbon sources.",
            "experiment_type": "targeted transporter mutant substrate-uptake and growth assay",
        }
    ]

    path.write_text(yaml.safe_dump(doc, sort_keys=False, width=1000))
    print(f"curated {path}")


def main() -> None:
    for gene, cfg in CONFIG.items():
        curate_gene(gene, cfg)


if __name__ == "__main__":
    main()
