#!/usr/bin/env python3
"""First-pass curation for the ppu02010 PP_4863-PP_4867 Bra/Liv importer."""

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


BCAA_ACTIVITY = {
    "id": "GO:0015658",
    "label": "branched-chain amino acid transmembrane transporter activity",
}
BCAA_TRANSPORT = {"id": "GO:0015803", "label": "branched-chain amino acid transport"}
AA_BINDING = {"id": "GO:0016597", "label": "amino acid binding"}
L_VALINE_IMPORT = {"id": "GO:1903805", "label": "L-valine import across plasma membrane"}
L_VALINE_TRANSPORT = {"id": "GO:1903785", "label": "L-valine transmembrane transport"}
L_ISOLEUCINE_IMPORT = {
    "id": "GO:1903806",
    "label": "L-isoleucine import across plasma membrane",
}
L_LEUCINE_IMPORT = {"id": "GO:1903801", "label": "L-leucine import across plasma membrane"}
ATP_HYDROLYSIS = {"id": "GO:0016887", "label": "ATP hydrolysis activity"}
ABC_COMPLEX = {
    "id": "GO:0043190",
    "label": "ATP-binding cassette (ABC) transporter complex",
}
PLASMA_MEMBRANE = {"id": "GO:0005886", "label": "plasma membrane"}
PERIPLASM = {"id": "GO:0030288", "label": "outer membrane-bounded periplasmic space"}


GENES = {
    "livF-II": {
        "symbol": "livF-II",
        "kind": "livf_atpase",
        "description": (
            "livF-II (PP_4863) encodes a predicted ATP-binding energy-coupling "
            "subunit of the PP_4863-PP_4867 Bra/Liv high-affinity "
            "branched-chain amino-acid ABC uptake system. Its ABC ATPase domain "
            "supports ATP hydrolysis-driven transport with BraF, BraE, BraD, and "
            "the BraC-like periplasmic substrate-binding component PP_4867."
        ),
        "uniprot_text": "Full=High-affinity branched-chain amino acid transport ATP-binding protein",
        "asta_text": "Protein Description:** RecName: Full=High-affinity branched-chain amino acid transport ATP-binding protein",
        "panther_text": "PANTHER; PTHR43820:SF4; HIGH-AFFINITY BRANCHED-CHAIN AMINO ACID TRANSPORT ATP-BINDING PROTEIN LIVF; 1.",
        "domain_text": "FT   DOMAIN          6..237",
    },
    "braF": {
        "symbol": "braF",
        "kind": "braf_atpase",
        "description": (
            "braF (PP_4864) encodes a predicted ATP-binding energy-coupling "
            "subunit of the PP_4863-PP_4867 Bra/Liv high-affinity "
            "branched-chain amino-acid ABC uptake system. Automated annotations "
            "support an ATPase role in valine and isoleucine import with the "
            "adjacent LivF-II, BraE, BraD, and PP_4867 transporter components."
        ),
        "uniprot_text": "Full=High-affinity branched-chain amino acid transport ATP-binding protein BraF",
        "asta_text": "Protein Description:** SubName: Full=High-affinity branched-chain amino acid transport ATP-binding protein BraF",
        "panther_text": "PANTHER; PTHR45772:SF11; HIGH-AFFINITY BRANCHED-CHAIN AMINO ACID TRANSPORT ATP-BINDING PROTEIN LIVG; 1.",
        "domain_text": "FT   DOMAIN          7..285",
    },
    "braE": {
        "symbol": "braE",
        "kind": "brae_permease",
        "description": (
            "braE (PP_4865) encodes a predicted multi-pass inner-membrane "
            "permease component of the PP_4863-PP_4867 Bra/Liv high-affinity "
            "branched-chain amino-acid ABC uptake system. Its LivM-like "
            "binding-protein-dependent transporter domains support a channel "
            "role in branched-chain amino-acid import."
        ),
        "uniprot_text": "Full=High-affinity branched-chain amino acid transport system permease protein BraE",
        "asta_text": "Protein Description:** SubName: Full=High-affinity branched-chain amino acid transport system permease protein BraE",
        "panther_text": "PANTHER; PTHR30482:SF20; HIGH-AFFINITY BRANCHED-CHAIN AMINO ACID TRANSPORT SYSTEM PERMEASE PROTEIN LIVM; 1.",
    },
    "braD": {
        "symbol": "braD",
        "kind": "brad_permease",
        "description": (
            "braD (PP_4866) encodes a predicted multi-pass inner-membrane "
            "permease component of the PP_4863-PP_4867 Bra/Liv high-affinity "
            "branched-chain amino-acid ABC uptake system. Automated annotations "
            "support valine, isoleucine, and leucine transporter activity."
        ),
        "uniprot_text": "Full=High-affinity branched-chain amino acid transport system permease protein BraD",
        "asta_text": "Protein Description:** SubName: Full=High-affinity branched-chain amino acid transport system permease protein BraD",
        "panther_text": "PANTHER; PTHR11795:SF371; HIGH-AFFINITY BRANCHED-CHAIN AMINO ACID TRANSPORT SYSTEM PERMEASE PROTEIN LIVH; 1.",
    },
    "PP_4867": {
        "symbol": "PP_4867",
        "kind": "brac_binding",
        "description": (
            "PP_4867 encodes a signal-peptide-bearing BraC-like periplasmic "
            "substrate-binding component of the PP_4863-PP_4867 Bra/Liv "
            "branched-chain amino-acid ABC uptake system. UniProt names it as a "
            "branched-chain amino-acid ABC transporter periplasmic "
            "amino-acid-binding protein and places it in the leucine-binding "
            "protein family, supporting substrate capture for the adjacent Bra "
            "transport complex."
        ),
        "uniprot_text": "Full=Branched-chain amino acid ABC transporter, periplasmic amino acid-binding protein (BraC-like)",
        "asta_text": "Protein Description:** SubName: Full=Branched-chain amino acid ABC transporter, periplasmic amino acid-binding protein (BraC-like)",
        "panther_text": "PANTHER; PTHR47151; LEU/ILE/VAL-BINDING ABC TRANSPORTER SUBUNIT; 1.",
        "signal_text": "FT   SIGNAL          1..27",
    },
}


def atpase_review(gene: str, cfg: dict, term_id: str, label: str) -> dict:
    panther = support_uniprot(gene, cfg["panther_text"])
    domain = support_uniprot(gene, cfg["domain_text"])
    product = support_uniprot(gene, cfg["uniprot_text"])
    mapping = {
        "GO:0000166": (
            "Nucleotide binding is true but less informative than ATP binding for this ABC ATPase.",
            "MARK_AS_OVER_ANNOTATED",
            "The review retains the more specific ATP-binding and ATP-hydrolysis annotations for the transporter ATPase.",
            None,
            [product],
        ),
        "GO:0005524": (
            "ATP binding is correct for this ABC-transporter nucleotide-binding component.",
            "ACCEPT",
            "The protein has an ABC ATPase domain and is named/classified as a high-affinity branched-chain amino-acid transport ATP-binding protein.",
            None,
            [domain],
        ),
        "GO:0015658": (
            "Branched-chain amino acid transmembrane transporter activity is appropriate as the complex-level function to which this ATPase contributes.",
            "ACCEPT",
            "The product name and PANTHER subfamily support a role in a high-affinity branched-chain amino-acid ABC transporter.",
            None,
            [panther],
        ),
        "GO:0015803": (
            "Branched-chain amino acid transport is the correct first-pass process for this Bra/Liv ATP-binding component.",
            "ACCEPT",
            "The PP_4863-PP_4867 locus is a predicted high-affinity branched-chain amino-acid ABC uptake system.",
            None,
            [product],
        ),
        "GO:0015807": (
            "L-amino acid transport is true but too general for this Bra/Liv BCAA transporter ATPase.",
            "MARK_AS_OVER_ANNOTATED",
            "The specific branched-chain amino acid transport annotation should be used as the core process.",
            None,
            [product],
        ),
        "GO:0016887": (
            "ATP hydrolysis activity is the correct mechanistic activity for this ABC ATPase subunit.",
            "ACCEPT",
            "ATP hydrolysis by this subunit is expected to provide energy coupling to the Bra/Liv branched-chain amino-acid ABC importer.",
            None,
            [domain],
        ),
    }
    if cfg["kind"] == "braf_atpase":
        mapping.update(
            {
                "GO:0005304": (
                    "L-valine transmembrane transporter activity is consistent with the Bra/Liv branched-chain amino-acid ABC importer.",
                    "ACCEPT",
                    "BraF is classified as a high-affinity branched-chain amino-acid transport ATP-binding protein and has valine import process annotations.",
                    None,
                    [panther],
                ),
                "GO:0005886": (
                    "Plasma membrane localization is appropriate for a membrane-associated bacterial ABC transporter ATPase at first pass.",
                    "ACCEPT",
                    "The GOA row places BraF at the plasma membrane, consistent with its role in the inner-membrane Bra/Liv ABC transporter complex.",
                    None,
                    None,
                ),
                "GO:0015188": (
                    "L-isoleucine transmembrane transporter activity is consistent with the Bra/Liv branched-chain amino-acid ABC importer.",
                    "ACCEPT",
                    "The BraF PANTHER subfamily and isoleucine import annotations support this substrate-specific activity at the complex level.",
                    None,
                    [panther],
                ),
                "GO:0015192": (
                    "L-phenylalanine transporter activity may reflect broad hydrophobic-amino-acid family transfer rather than the core Bra/Liv BCAA assignment.",
                    "MARK_AS_OVER_ANNOTATED",
                    "The local product names and PANTHER subfamily support a branched-chain amino-acid transporter; phenylalanine transport is not promoted to core without PSEPK-specific substrate evidence.",
                    None,
                    [product],
                ),
                "GO:0015808": (
                    "L-alanine transport is plausible only as broad-family transfer and is not the core Bra/Liv function.",
                    "MARK_AS_OVER_ANNOTATED",
                    "The strongest locus-level evidence supports branched-chain amino-acid uptake, not alanine transport.",
                    None,
                    [product],
                ),
                "GO:0015823": (
                    "Phenylalanine transport is not supported as the core function of this Bra/Liv ATPase.",
                    "MARK_AS_OVER_ANNOTATED",
                    "The review treats phenylalanine transport as a hydrophobic-amino-acid family spillover pending direct substrate evidence.",
                    None,
                    [panther],
                ),
                "GO:0042941": (
                    "D-alanine transmembrane transport is not part of the core Bra/Liv branched-chain amino-acid uptake assignment.",
                    "MARK_AS_OVER_ANNOTATED",
                    "The local evidence supports BraF as a high-affinity BCAA transporter ATP-binding protein; D-alanine transport is treated as over-propagated family context.",
                    None,
                    [product],
                ),
                "GO:1903714": (
                    "Isoleucine transmembrane transport is directionally correct but less precise than the existing L-isoleucine import term.",
                    "MODIFY",
                    "The GOA also has L-isoleucine import across plasma membrane, which better captures the expected bacterial uptake direction and stereochemistry.",
                    [L_ISOLEUCINE_IMPORT],
                    [support_goa(gene, "GO:1903806", "L-isoleucine import across plasma membrane")],
                ),
                "GO:1903785": (
                    "L-valine transmembrane transport is consistent with the Bra/Liv BCAA uptake system.",
                    "ACCEPT",
                    "BraF is a branched-chain amino-acid transporter ATP-binding protein and has a matching L-valine import annotation.",
                    None,
                    [support_goa(gene, "GO:1903805", "L-valine import across plasma membrane")],
                ),
                "GO:1903805": (
                    "L-valine import across the plasma membrane is an appropriate substrate-specific process for this Bra/Liv importer component.",
                    "ACCEPT",
                    "The product name and PANTHER subfamily support BraF as part of a high-affinity branched-chain amino-acid ABC importer.",
                    None,
                    [panther],
                ),
                "GO:1903806": (
                    "L-isoleucine import across the plasma membrane is an appropriate substrate-specific process for this Bra/Liv importer component.",
                    "ACCEPT",
                    "The product name and PANTHER subfamily support BraF as part of a high-affinity branched-chain amino-acid ABC importer.",
                    None,
                    [panther],
                ),
            }
        )
    entry = mapping[term_id]
    return review(gene, term_id, label, entry[0], entry[1], entry[2], proposed=entry[3], extra_support=entry[4])


def permease_review(gene: str, cfg: dict, term_id: str, label: str) -> dict:
    panther = support_uniprot(gene, cfg["panther_text"])
    product = support_uniprot(gene, cfg["uniprot_text"])
    cell_inner = support_uniprot(gene, "Cell inner membrane")
    mapping = {
        "GO:0005886": (
            "Plasma membrane localization is appropriate for this predicted inner-membrane ABC permease.",
            "ACCEPT",
            "UniProt predicts this Bra/Liv permease as a cell inner-membrane multi-pass membrane protein.",
            None,
            [cell_inner],
        ),
        "GO:0015658": (
            "Branched-chain amino acid transmembrane transporter activity is appropriate as the complex-level function to which this permease contributes.",
            "ACCEPT",
            "The product name and PANTHER subfamily identify this protein as a high-affinity branched-chain amino-acid transport-system permease.",
            None,
            [panther],
        ),
        "GO:0015803": (
            "Branched-chain amino acid transport is the correct first-pass process for this Bra/Liv permease.",
            "ACCEPT",
            "The PP_4863-PP_4867 locus is a predicted high-affinity branched-chain amino-acid ABC uptake system.",
            None,
            [product],
        ),
        "GO:0016020": (
            "Membrane localization is true but less informative than plasma membrane for this bacterial inner-membrane permease.",
            "MARK_AS_OVER_ANNOTATED",
            "The record also has a plasma-membrane annotation and UniProt predicts a cell inner-membrane multi-pass protein.",
            None,
            [cell_inner],
        ),
        "GO:0022857": (
            "Generic transmembrane transporter activity is too broad for this Bra/Liv ABC-transporter permease component.",
            "MODIFY",
            "The product name and PANTHER subfamily support branched-chain amino acid transmembrane transporter activity as the better complex-level activity.",
            [BCAA_ACTIVITY],
            [product],
        ),
        "GO:0055085": (
            "Transmembrane transport is true but broad relative to the branched-chain amino-acid ABC-import context.",
            "MODIFY",
            "Branched-chain amino acid transport better captures the expected substrate class for this Bra/Liv permease.",
            [BCAA_TRANSPORT],
            [panther],
        ),
    }
    if cfg["kind"] == "brad_permease":
        mapping.update(
            {
                "GO:0005304": (
                    "L-valine transmembrane transporter activity is consistent with the Bra/Liv branched-chain amino-acid ABC importer.",
                    "ACCEPT",
                    "The BraD PANTHER subfamily supports a high-affinity branched-chain amino-acid transport-system permease.",
                    None,
                    [panther],
                ),
                "GO:0015188": (
                    "L-isoleucine transmembrane transporter activity is consistent with the Bra/Liv branched-chain amino-acid ABC importer.",
                    "ACCEPT",
                    "The BraD PANTHER subfamily supports a high-affinity branched-chain amino-acid transport-system permease.",
                    None,
                    [panther],
                ),
                "GO:0015190": (
                    "L-leucine transmembrane transporter activity is consistent with BraD in a Bra/Liv BCAA importer.",
                    "ACCEPT",
                    "BraD is part of a high-affinity branched-chain amino-acid transport system, and GOA supplies the L-leucine transporter activity row.",
                    None,
                    [panther],
                ),
                "GO:0015192": (
                    "L-phenylalanine transporter activity may reflect broad hydrophobic-amino-acid family transfer rather than the core Bra/Liv BCAA assignment.",
                    "MARK_AS_OVER_ANNOTATED",
                    "The local product names and PANTHER subfamilies support a branched-chain amino-acid transporter; phenylalanine transport is not promoted to core without PSEPK-specific substrate evidence.",
                    None,
                    [product],
                ),
                "GO:0015808": (
                    "L-alanine transport is plausible only as broad-family transfer and is not the core Bra/Liv function.",
                    "MARK_AS_OVER_ANNOTATED",
                    "The strongest locus-level evidence supports branched-chain amino-acid uptake, not alanine transport.",
                    None,
                    [panther],
                ),
                "GO:0015823": (
                    "Phenylalanine transport is not supported as the core function of this Bra/Liv permease.",
                    "MARK_AS_OVER_ANNOTATED",
                    "The review treats phenylalanine transport as a hydrophobic-amino-acid family spillover pending direct substrate evidence.",
                    None,
                    [product],
                ),
                "GO:0042941": (
                    "D-alanine transmembrane transport is not part of the core Bra/Liv branched-chain amino-acid uptake assignment.",
                    "MARK_AS_OVER_ANNOTATED",
                    "The local evidence supports BraD as a high-affinity BCAA transporter permease; D-alanine transport is treated as over-propagated family context.",
                    None,
                    [product],
                ),
                "GO:1903785": (
                    "L-valine transmembrane transport is consistent with the Bra/Liv BCAA uptake system.",
                    "ACCEPT",
                    "BraD is a high-affinity branched-chain amino-acid transport-system permease.",
                    None,
                    [panther],
                ),
                "GO:1903806": (
                    "L-isoleucine import across the plasma membrane is an appropriate substrate-specific process for this Bra/Liv importer component.",
                    "ACCEPT",
                    "The BraD permease supports a BCAA uptake-system interpretation.",
                    None,
                    [product],
                ),
            }
        )
    entry = mapping[term_id]
    return review(gene, term_id, label, entry[0], entry[1], entry[2], proposed=entry[3], extra_support=entry[4])


def binding_review(gene: str, cfg: dict, term_id: str, label: str) -> dict:
    return review(
        gene,
        term_id,
        label,
        "Amino acid transport is correct but too broad for the BraC-like BCAA-binding component.",
        "MODIFY",
        "The product name, leucine-binding family assignment, and Leu/Ile/Val-binding PANTHER family support branched-chain amino acid transport as the better process term.",
        proposed=[BCAA_TRANSPORT],
        extra_support=[
            support_uniprot(gene, cfg["uniprot_text"]),
            support_uniprot(gene, cfg["panther_text"]),
        ],
    )


def new_annotations(gene: str, cfg: dict) -> list[dict]:
    product_support = [support_uniprot(gene, cfg["uniprot_text"]), support_asta(gene, cfg["asta_text"])]
    panther_support = [support_uniprot(gene, cfg["panther_text"]), support_asta(gene, cfg["asta_text"])]
    if cfg["kind"] in {"livf_atpase", "brae_permease"}:
        return [
            {
                "term": ABC_COMPLEX,
                "qualifier": "part_of",
                "summary": f"ABC transporter complex membership is appropriate for this {cfg['symbol']} Bra/Liv component.",
                "reason": "The product is part of the adjacent PP_4863-PP_4867 high-affinity branched-chain amino-acid ABC transporter locus.",
                "support": product_support,
            }
        ]
    if cfg["kind"] == "braf_atpase":
        return [
            {
                "term": BCAA_ACTIVITY,
                "qualifier": "contributes_to",
                "summary": "Branched-chain amino acid transmembrane transporter activity captures the complex-level activity to which BraF contributes.",
                "reason": "BraF is an ATP-binding subunit of the adjacent Bra/Liv branched-chain amino-acid ABC transporter.",
                "support": panther_support,
            },
            {
                "term": ABC_COMPLEX,
                "qualifier": "part_of",
                "summary": "ABC transporter complex membership is appropriate for this BraF ATP-binding component.",
                "reason": "BraF is named and classified as an ATP-binding subunit of the adjacent Bra/Liv branched-chain amino-acid ABC transporter.",
                "support": product_support,
            },
        ]
    if cfg["kind"] == "brad_permease":
        return [
            {
                "term": BCAA_ACTIVITY,
                "qualifier": "contributes_to",
                "summary": "Branched-chain amino acid transmembrane transporter activity captures the complex-level activity to which BraD contributes.",
                "reason": "BraD is a permease subunit of the adjacent Bra/Liv branched-chain amino-acid ABC transporter.",
                "support": panther_support,
            },
            {
                "term": L_LEUCINE_IMPORT,
                "qualifier": "involved_in",
                "summary": "L-leucine import across the plasma membrane is a useful missing process annotation for the BraD permease.",
                "reason": "BraD has an L-leucine transporter activity annotation within a high-affinity branched-chain amino-acid ABC transporter context.",
                "support": [
                    support_goa(gene, "GO:0015190", "L-leucine transmembrane transporter activity"),
                    support_uniprot(gene, cfg["panther_text"]),
                ],
            },
            {
                "term": ABC_COMPLEX,
                "qualifier": "part_of",
                "summary": "ABC transporter complex membership is appropriate for this BraD permease.",
                "reason": "BraD is a permease subunit in the adjacent Bra/Liv branched-chain amino-acid ABC transporter locus.",
                "support": product_support,
            },
        ]
    return [
        {
            "term": AA_BINDING,
            "qualifier": "enables",
            "summary": "Amino acid binding captures the expected substrate-recognition role of this BraC-like periplasmic binding protein.",
            "reason": "PP_4867 is named as a periplasmic amino-acid-binding protein and belongs to the Leu/Ile/Val-binding ABC transporter subunit family.",
            "support": panther_support,
        },
        {
            "term": BCAA_TRANSPORT,
            "qualifier": "involved_in",
            "summary": "Branched-chain amino acid transport is a useful missing process annotation for PP_4867.",
            "reason": "PP_4867 is the BraC-like binding component of an adjacent high-affinity branched-chain amino-acid ABC transporter locus.",
            "support": product_support,
        },
        {
            "term": BCAA_ACTIVITY,
            "qualifier": "contributes_to",
            "summary": "PP_4867 contributes substrate recognition to the branched-chain amino acid transmembrane transporter activity of the Bra/Liv complex.",
            "reason": "As a periplasmic solute-binding component, PP_4867 supplies substrate capture rather than catalyzing membrane translocation alone.",
            "support": product_support,
        },
        {
            "term": PERIPLASM,
            "qualifier": "located_in",
            "summary": "Periplasmic localization is appropriate for this signal-peptide-bearing bacterial substrate-binding protein.",
            "reason": "The product name identifies PP_4867 as a periplasmic binding protein and UniProt predicts an N-terminal signal peptide.",
            "support": [support_uniprot(gene, cfg["signal_text"]), support_asta(gene, cfg["asta_text"])],
        },
        {
            "term": ABC_COMPLEX,
            "qualifier": "part_of",
            "summary": "ABC transporter complex membership is appropriate for this PP_4867 substrate-binding component.",
            "reason": "PP_4867 is named as the BraC-like periplasmic amino-acid-binding protein of the adjacent branched-chain amino-acid ABC transporter locus.",
            "support": product_support,
        },
    ]


def core_function(gene: str, cfg: dict) -> dict:
    core = {"description": ""}
    if cfg["kind"] in {"livf_atpase", "braf_atpase"}:
        core.update(
            {
                "description": f"ATP-binding energy-coupling subunit contributing to a predicted PP_4863-PP_4867 Bra/Liv branched-chain amino-acid ABC uptake system.",
                "molecular_function": ATP_HYDROLYSIS,
                "contributes_to_molecular_function": BCAA_ACTIVITY,
                "directly_involved_in": [BCAA_TRANSPORT]
                if cfg["kind"] == "livf_atpase"
                else [L_VALINE_IMPORT, L_ISOLEUCINE_IMPORT],
                "in_complex": ABC_COMPLEX,
            }
        )
        if cfg["kind"] == "braf_atpase":
            core["locations"] = [PLASMA_MEMBRANE]
        support = ("GO:0016887", "ATP hydrolysis activity")
    elif cfg["kind"] == "brae_permease":
        core.update(
            {
                "description": "Multi-pass permease component contributing to a predicted PP_4863-PP_4867 Bra/Liv branched-chain amino-acid ABC uptake system.",
                "contributes_to_molecular_function": BCAA_ACTIVITY,
                "directly_involved_in": [BCAA_TRANSPORT],
                "locations": [PLASMA_MEMBRANE],
                "in_complex": ABC_COMPLEX,
            }
        )
        support = ("GO:0015658", "branched-chain amino acid transmembrane transporter activity")
    elif cfg["kind"] == "brad_permease":
        core.update(
            {
                "description": "Multi-pass permease component contributing to a predicted PP_4863-PP_4867 Bra/Liv branched-chain amino-acid ABC uptake system.",
                "contributes_to_molecular_function": BCAA_ACTIVITY,
                "directly_involved_in": [L_VALINE_TRANSPORT, L_ISOLEUCINE_IMPORT, L_LEUCINE_IMPORT],
                "locations": [PLASMA_MEMBRANE],
                "in_complex": ABC_COMPLEX,
            }
        )
        support = ("GO:0015190", "L-leucine transmembrane transporter activity")
    else:
        core.update(
            {
                "description": "Periplasmic branched-chain amino-acid substrate-binding component contributing substrate capture to a predicted PP_4863-PP_4867 Bra/Liv ABC uptake system.",
                "molecular_function": AA_BINDING,
                "contributes_to_molecular_function": BCAA_ACTIVITY,
                "directly_involved_in": [BCAA_TRANSPORT],
                "locations": [PERIPLASM],
                "in_complex": ABC_COMPLEX,
            }
        )
        support = None

    core["supported_by"] = []
    if support:
        core["supported_by"].append(support_goa(gene, support[0], support[1]))
    core["supported_by"].extend([support_uniprot(gene, cfg["uniprot_text"]), support_asta(gene, cfg["asta_text"])])
    return core


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
        if cfg["kind"] in {"livf_atpase", "braf_atpase"}:
            ann["review"] = atpase_review(gene, cfg, term["id"], term["label"])
        elif cfg["kind"] in {"brae_permease", "brad_permease"}:
            ann["review"] = permease_review(gene, cfg, term["id"], term["label"])
        else:
            ann["review"] = binding_review(gene, cfg, term["id"], term["label"])

    existing_term_ids = {ann["term"]["id"] for ann in doc.get("existing_annotations", [])}
    for extra in new_annotations(gene, cfg):
        term = extra["term"]
        if term["id"] in existing_term_ids:
            continue
        doc.setdefault("existing_annotations", []).append(
            new_annotation(
                term,
                extra["qualifier"],
                uniprot_ref(gene),
                extra["summary"],
                extra["reason"],
                extra["support"],
            )
        )
        existing_term_ids.add(term["id"])

    doc["core_functions"] = [core_function(gene, cfg)]
    doc["proposed_new_terms"] = []
    doc["suggested_questions"] = [
        {
            "question": "Is the PP_4863-PP_4867 Bra/Liv ABC importer functionally redundant with the PP_1137-PP_1141 LivFGMHK system, or does it differ in regulation or substrate preference for L-leucine, L-isoleucine, L-valine, alanine, or related hydrophobic amino acids?"
        }
    ]
    doc["suggested_experiments"] = [
        {
            "description": "Measure uptake and growth phenotypes for livF-II, braF, braE, braD, and PP_4867 mutants, alone and in combination with the PP_1137-PP_1141 liv locus, using L-leucine, L-isoleucine, L-valine, alanine, and phenylalanine as candidate substrates.",
            "experiment_type": "targeted transporter mutant substrate-uptake and redundancy assay",
        }
    ]

    path.write_text(yaml.safe_dump(doc, sort_keys=False, width=1000))
    print(f"curated {path}")


def main() -> None:
    for gene, cfg in GENES.items():
        curate_gene(gene, cfg)


if __name__ == "__main__":
    main()
