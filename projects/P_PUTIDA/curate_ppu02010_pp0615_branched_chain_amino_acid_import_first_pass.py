#!/usr/bin/env python3
"""First-pass curation for the ppu02010 PP_0615-PP_0619 BCAA importer."""

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
L_LEUCINE_BINDING = {"id": "GO:0070728", "label": "L-leucine binding"}
ATP_HYDROLYSIS = {"id": "GO:0016887", "label": "ATP hydrolysis activity"}
ABC_COMPLEX = {
    "id": "GO:0043190",
    "label": "ATP-binding cassette (ABC) transporter complex",
}
PLASMA_MEMBRANE = {"id": "GO:0005886", "label": "plasma membrane"}
PERIPLASM = {"id": "GO:0030288", "label": "outer membrane-bounded periplasmic space"}


GENES = {
    "PP_0615": {
        "kind": "livf_like_atpase",
        "description": (
            "PP_0615 encodes a predicted ATP-binding energy-coupling subunit of "
            "the PP_0615-PP_0619 high-affinity branched-chain amino-acid ABC "
            "uptake system. Its ABC ATPase domain and LivF-family PANTHER "
            "assignment support ATP hydrolysis-driven transport with the adjacent "
            "PP_0616 ATP-binding partner, PP_0617/PP_0618 permeases, and PP_0619 "
            "periplasmic substrate-binding component."
        ),
        "uniprot_text": "Full=Branched-chain amino acid ABC transporter, ATP-binding protein",
        "asta_text": "Protein Description:** SubName: Full=Branched-chain amino acid ABC transporter, ATP-binding protein",
        "panther_text": "PANTHER; PTHR43820; HIGH-AFFINITY BRANCHED-CHAIN AMINO ACID TRANSPORT ATP-BINDING PROTEIN LIVF; 1.",
        "domain_text": "FT   DOMAIN          2..229",
    },
    "PP_0616": {
        "kind": "livg_like_atpase",
        "description": (
            "PP_0616 encodes a predicted ATP-binding energy-coupling subunit of "
            "the PP_0615-PP_0619 branched-chain amino-acid ABC uptake system. "
            "The product name and ABC transporter ATP-binding domain support an "
            "ATPase role paired with PP_0615 and the adjacent permease/binding "
            "components."
        ),
        "uniprot_text": "Full=Branched-chain amino acid ABC transporter, ATP binding protein",
        "asta_text": "Protein Description:** SubName: Full=Branched-chain amino acid ABC transporter, ATP binding protein",
        "panther_text": "PANTHER; PTHR45772; CONSERVED COMPONENT OF ABC TRANSPORTER FOR NATURAL AMINO ACIDS-RELATED; 1.",
        "domain_text": "FT   DOMAIN          6..248",
    },
    "PP_0617": {
        "kind": "livm_like_permease",
        "description": (
            "PP_0617 encodes a predicted multi-pass inner-membrane permease "
            "component of the PP_0615-PP_0619 branched-chain amino-acid ABC "
            "uptake system. Its product name and binding-protein-dependent "
            "transporter domains support a membrane-channel role in BCAA import."
        ),
        "uniprot_text": "Full=Branched-chain amino acid ABC transporter, permease protein",
        "asta_text": "Protein Description:** SubName: Full=Branched-chain amino acid ABC transporter, permease protein",
        "panther_text": "PANTHER; PTHR30482; HIGH-AFFINITY BRANCHED-CHAIN AMINO ACID TRANSPORT SYSTEM PERMEASE; 1.",
    },
    "PP_0618": {
        "kind": "livh_like_permease",
        "description": (
            "PP_0618 encodes a predicted multi-pass inner-membrane permease "
            "component of the PP_0615-PP_0619 branched-chain amino-acid ABC "
            "uptake system. UniProt places it in the cell inner membrane and "
            "assigns the LivH-family BCAA transport permease family."
        ),
        "uniprot_text": "Full=Branched-chain amino acid ABC transporter, permease protein",
        "asta_text": "Protein Description:** SubName: Full=Branched-chain amino acid ABC transporter, permease protein",
        "panther_text": "PANTHER; PTHR11795; BRANCHED-CHAIN AMINO ACID TRANSPORT SYSTEM PERMEASE PROTEIN LIVH; 1.",
    },
    "PP_0619": {
        "kind": "binding",
        "description": (
            "PP_0619 encodes a signal-peptide-bearing periplasmic "
            "branched-chain amino-acid substrate-binding component of the "
            "PP_0615-PP_0619 ABC uptake system. UniProt places it in the "
            "leucine-binding protein family, and PANTHER assigns a "
            "leucine-specific/periplasmic ABC transporter binding-protein family."
        ),
        "uniprot_text": "Full=Branched-chain amino acid ABC transporter, periplasmic amino acid-binding protein",
        "asta_text": "Protein Description:** SubName: Full=Branched-chain amino acid ABC transporter, periplasmic amino acid-binding protein",
        "panther_text": "PANTHER; PTHR30483; LEUCINE-SPECIFIC-BINDING PROTEIN; 1.",
        "signal_text": "FT   SIGNAL          1..28",
    },
}


def atpase_review(gene: str, cfg: dict, term_id: str, label: str) -> dict:
    product = support_uniprot(gene, cfg["uniprot_text"])
    panther = support_uniprot(gene, cfg["panther_text"])
    domain = support_uniprot(gene, cfg["domain_text"])
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
            "The product has an ABC ATPase domain and is named as a branched-chain amino-acid ABC transporter ATP-binding protein.",
            None,
            [domain],
        ),
        "GO:0005886": (
            "Plasma membrane localization is appropriate for a membrane-associated bacterial ABC transporter ATPase at first pass.",
            "ACCEPT",
            "The GOA row places this ATP-binding component at the plasma membrane, consistent with its role in an inner-membrane ABC transporter complex.",
            None,
            None,
        ),
        "GO:0015658": (
            "Branched-chain amino acid transmembrane transporter activity is appropriate as the complex-level function to which this ATPase contributes.",
            "ACCEPT",
            "The product name and PANTHER family support a role in a branched-chain amino-acid ABC transporter.",
            None,
            [panther],
        ),
        "GO:0015803": (
            "Branched-chain amino acid transport is the correct first-pass process for this ATP-binding component.",
            "ACCEPT",
            "The PP_0615-PP_0619 locus is a predicted branched-chain amino-acid ABC uptake system.",
            None,
            [product],
        ),
        "GO:0015807": (
            "L-amino acid transport is true but too general for this BCAA transporter ATPase.",
            "MARK_AS_OVER_ANNOTATED",
            "The specific branched-chain amino acid transport annotation should be used as the core process.",
            None,
            [product],
        ),
        "GO:0016887": (
            "ATP hydrolysis activity is the correct mechanistic activity for this ABC ATPase subunit.",
            "ACCEPT",
            "ATP hydrolysis by this subunit is expected to provide energy coupling to the PP_0615-PP_0619 branched-chain amino-acid ABC importer.",
            None,
            [domain],
        ),
    }
    entry = mapping[term_id]
    return review(gene, term_id, label, entry[0], entry[1], entry[2], proposed=entry[3], extra_support=entry[4])


def permease_review(gene: str, cfg: dict, term_id: str, label: str) -> dict:
    product = support_uniprot(gene, cfg["uniprot_text"])
    panther = support_uniprot(gene, cfg["panther_text"])
    cell_inner = support_uniprot(gene, "Cell inner membrane")
    mapping = {
        "GO:0005886": (
            "Plasma membrane localization is appropriate for this predicted inner-membrane ABC permease.",
            "ACCEPT",
            "UniProt predicts this permease as a cell inner-membrane multi-pass membrane protein.",
            None,
            [cell_inner],
        ),
        "GO:0006865": (
            "Amino acid transport is correct but too broad for this BCAA ABC-transporter permease.",
            "MODIFY",
            "The product name and local PP_0615-PP_0619 transporter context support branched-chain amino acid transport as the better process term.",
            [BCAA_TRANSPORT],
            [product],
        ),
        "GO:0015658": (
            "Branched-chain amino acid transmembrane transporter activity is appropriate as the complex-level function to which this permease contributes.",
            "ACCEPT",
            "The product name and PANTHER family identify this protein as a BCAA transport-system permease.",
            None,
            [panther],
        ),
        "GO:0015803": (
            "Branched-chain amino acid transport is the correct first-pass process for this permease.",
            "ACCEPT",
            "The PP_0615-PP_0619 locus is a predicted branched-chain amino-acid ABC uptake system.",
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
            "Generic transmembrane transporter activity is too broad for this BCAA ABC-transporter permease component.",
            "MODIFY",
            "The product name and PANTHER family support branched-chain amino acid transmembrane transporter activity as the better complex-level activity.",
            [BCAA_ACTIVITY],
            [product],
        ),
        "GO:0055085": (
            "Transmembrane transport is true but broad relative to the branched-chain amino-acid ABC-import context.",
            "MODIFY",
            "Branched-chain amino acid transport better captures the expected substrate class for this permease.",
            [BCAA_TRANSPORT],
            [product],
        ),
    }
    entry = mapping[term_id]
    return review(gene, term_id, label, entry[0], entry[1], entry[2], proposed=entry[3], extra_support=entry[4])


def new_annotations(gene: str, cfg: dict) -> list[dict]:
    product_support = [support_uniprot(gene, cfg["uniprot_text"]), support_asta(gene, cfg["asta_text"])]
    panther_support = [support_uniprot(gene, cfg["panther_text"]), support_asta(gene, cfg["asta_text"])]
    if cfg["kind"] in {"livf_like_atpase", "livg_like_atpase"}:
        additions = [
            {
                "term": ABC_COMPLEX,
                "qualifier": "part_of",
                "summary": f"ABC transporter complex membership is appropriate for {gene}.",
                "reason": "The product is an ATP-binding component of the adjacent PP_0615-PP_0619 branched-chain amino-acid ABC transporter locus.",
                "support": product_support,
            }
        ]
        if cfg["kind"] == "livg_like_atpase":
            additions.extend(
                [
                    {
                        "term": BCAA_ACTIVITY,
                        "qualifier": "contributes_to",
                        "summary": "Branched-chain amino acid transmembrane transporter activity captures the complex-level activity to which PP_0616 contributes.",
                        "reason": "PP_0616 is named as a branched-chain amino-acid ABC transporter ATP-binding protein in the adjacent PP_0615-PP_0619 BCAA transporter locus.",
                        "support": product_support,
                    },
                    {
                        "term": BCAA_TRANSPORT,
                        "qualifier": "involved_in",
                        "summary": "Branched-chain amino acid transport is a useful missing process annotation for PP_0616.",
                        "reason": "PP_0616 is paired with BCAA transporter ATP-binding, permease, and periplasmic binding components.",
                        "support": product_support,
                    },
                ]
            )
        return additions
    if cfg["kind"] in {"livm_like_permease", "livh_like_permease"}:
        additions = [
            {
                "term": ABC_COMPLEX,
                "qualifier": "part_of",
                "summary": f"ABC transporter complex membership is appropriate for {gene}.",
                "reason": "The product is a permease component of the adjacent PP_0615-PP_0619 branched-chain amino-acid ABC transporter locus.",
                "support": product_support,
            }
        ]
        if cfg["kind"] == "livh_like_permease":
            additions.extend(
                [
                    {
                        "term": BCAA_ACTIVITY,
                        "qualifier": "contributes_to",
                        "summary": "Branched-chain amino acid transmembrane transporter activity captures the complex-level activity to which PP_0618 contributes.",
                        "reason": "PP_0618 is named as a branched-chain amino-acid ABC transporter permease and belongs to the LivH BCAA permease family.",
                        "support": panther_support,
                    },
                    {
                        "term": BCAA_TRANSPORT,
                        "qualifier": "involved_in",
                        "summary": "Branched-chain amino acid transport is a useful missing process annotation for PP_0618.",
                        "reason": "PP_0618 is paired with BCAA transporter ATP-binding, permease, and periplasmic binding components.",
                        "support": product_support,
                    },
                ]
            )
        return additions
    return [
        {
            "term": L_LEUCINE_BINDING,
            "qualifier": "enables",
            "summary": "L-leucine binding captures the expected substrate-recognition role of this periplasmic binding protein.",
            "reason": "PP_0619 is in the leucine-binding protein family and PANTHER assigns a leucine-specific-binding protein family.",
            "support": panther_support,
        },
        {
            "term": BCAA_TRANSPORT,
            "qualifier": "involved_in",
            "summary": "Branched-chain amino acid transport is a useful missing process annotation for PP_0619.",
            "reason": "PP_0619 is the periplasmic binding component of an adjacent branched-chain amino-acid ABC transporter locus.",
            "support": product_support,
        },
        {
            "term": BCAA_ACTIVITY,
            "qualifier": "contributes_to",
            "summary": "PP_0619 contributes substrate recognition to the branched-chain amino acid transmembrane transporter activity of the PP_0615-PP_0619 complex.",
            "reason": "As a periplasmic solute-binding component, PP_0619 supplies substrate capture rather than catalyzing membrane translocation alone.",
            "support": product_support,
        },
        {
            "term": PERIPLASM,
            "qualifier": "located_in",
            "summary": "Periplasmic localization is appropriate for this signal-peptide-bearing bacterial substrate-binding protein.",
            "reason": "The product name identifies PP_0619 as a periplasmic binding protein and UniProt predicts an N-terminal signal peptide.",
            "support": [support_uniprot(gene, cfg["signal_text"]), support_asta(gene, cfg["asta_text"])],
        },
        {
            "term": ABC_COMPLEX,
            "qualifier": "part_of",
            "summary": "ABC transporter complex membership is appropriate for this PP_0619 substrate-binding component.",
            "reason": "PP_0619 is named as the periplasmic amino-acid-binding protein of the adjacent branched-chain amino-acid ABC transporter locus.",
            "support": product_support,
        },
    ]


def core_function(gene: str, cfg: dict) -> dict:
    if cfg["kind"] in {"livf_like_atpase", "livg_like_atpase"}:
        core = {
            "description": "ATP-binding energy-coupling subunit contributing to a predicted PP_0615-PP_0619 branched-chain amino-acid ABC uptake system.",
            "molecular_function": ATP_HYDROLYSIS,
            "contributes_to_molecular_function": BCAA_ACTIVITY,
            "directly_involved_in": [BCAA_TRANSPORT],
            "in_complex": ABC_COMPLEX,
        }
        if cfg["kind"] == "livg_like_atpase":
            core["locations"] = [PLASMA_MEMBRANE]
        support = ("GO:0016887", "ATP hydrolysis activity")
    elif cfg["kind"] in {"livm_like_permease", "livh_like_permease"}:
        core = {
            "description": "Multi-pass permease component contributing to a predicted PP_0615-PP_0619 branched-chain amino-acid ABC uptake system.",
            "contributes_to_molecular_function": BCAA_ACTIVITY,
            "directly_involved_in": [BCAA_TRANSPORT],
            "locations": [PLASMA_MEMBRANE],
            "in_complex": ABC_COMPLEX,
        }
        support = ("GO:0015658", "branched-chain amino acid transmembrane transporter activity") if cfg["kind"] == "livm_like_permease" else None
    else:
        core = {
            "description": "Periplasmic L-leucine/branched-chain amino-acid substrate-binding component contributing substrate capture to a predicted PP_0615-PP_0619 ABC uptake system.",
            "molecular_function": L_LEUCINE_BINDING,
            "contributes_to_molecular_function": BCAA_ACTIVITY,
            "directly_involved_in": [BCAA_TRANSPORT],
            "locations": [PERIPLASM],
            "in_complex": ABC_COMPLEX,
        }
        support = None

    core["supported_by"] = []
    if support:
        core["supported_by"].append(support_goa(gene, support[0], support[1]))
    core["supported_by"].extend([support_uniprot(gene, cfg["uniprot_text"]), support_asta(gene, cfg["asta_text"])])
    return core


def curate_gene(gene: str, cfg: dict) -> None:
    path = Path("genes") / SPECIES / gene / f"{gene}-ai-review.yaml"
    doc = yaml.safe_load(path.read_text())
    doc["gene_symbol"] = gene
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
        if cfg["kind"] in {"livf_like_atpase", "livg_like_atpase"}:
            ann["review"] = atpase_review(gene, cfg, term["id"], term["label"])
        else:
            ann["review"] = permease_review(gene, cfg, term["id"], term["label"])

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
            "question": "What substrate range and regulation distinguish the PP_0615-PP_0619 BCAA ABC importer from the other P. putida KT2440 BCAA transporter loci?"
        }
    ]
    doc["suggested_experiments"] = [
        {
            "description": "Measure uptake and growth phenotypes for PP_0615-PP_0619 mutants, alone and with other BCAA transporter loci, using L-leucine, L-isoleucine, L-valine, alanine, and related hydrophobic amino acids as candidate substrates.",
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
