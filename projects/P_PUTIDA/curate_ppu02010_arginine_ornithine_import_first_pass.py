#!/usr/bin/env python3
"""First-pass curation for the ppu02010 PP_0280-PP_0283 arginine/ornithine ABC importer."""

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


ABC_AMINO_ACID = {"id": "GO:0015424", "label": "ABC-type amino acid transporter activity"}
AA_BINDING = {"id": "GO:0016597", "label": "amino acid binding"}
ARG_TRANSPORT = {"id": "GO:1903826", "label": "L-arginine transmembrane transport"}
ORN_TRANSPORT = {"id": "GO:1903352", "label": "L-ornithine transmembrane transport"}
ATP_BINDING = {"id": "GO:0005524", "label": "ATP binding"}
ATP_HYDROLYSIS = {"id": "GO:0016887", "label": "ATP hydrolysis activity"}
ABC_COMPLEX = {"id": "GO:0043190", "label": "ATP-binding cassette (ABC) transporter complex"}
PLASMA_MEMBRANE = {"id": "GO:0005886", "label": "plasma membrane"}
PERIPLASM = {"id": "GO:0030288", "label": "outer membrane-bounded periplasmic space"}


CONFIG = {
    "PP_0280": {
        "symbol": "PP_0280",
        "description": (
            "PP_0280 encodes ArtM, a predicted multi-pass inner-membrane permease "
            "component of the PP_0280-PP_0283 arginine/basic-amino-acid ABC uptake "
            "locus. Its ArtM/MetI-like permease domains support a channel-forming "
            "role in an ATP-driven amino-acid importer rather than an independent "
            "ATPase or soluble substrate-binding protein."
        ),
        "uniprot_text": "Full=Arginine ABC transporter permease protein ArtM",
        "asta_text": "Protein Description:** RecName: Full=Arginine ABC transporter permease protein ArtM",
        "reviews": {
            "GO:0005886": (
                "Plasma membrane localization is appropriate for this predicted inner-membrane ABC permease.",
                "ACCEPT",
                "UniProt predicts PP_0280 as a cell inner-membrane multi-pass membrane protein.",
                None,
                [support_uniprot("PP_0280", "Cell inner membrane")],
            ),
            "GO:0006865": (
                "Amino acid transport is correct but too broad for the ArtM-family arginine transporter context.",
                "MODIFY",
                "The product name and PANTHER subfamily identify ArtM as an arginine ABC-transporter permease, so L-arginine transmembrane transport is the more informative first-pass process term.",
                [ARG_TRANSPORT],
                [support_uniprot("PP_0280", "PANTHER; PTHR30614:SF10; ARGININE ABC TRANSPORTER PERMEASE PROTEIN ARTM; 1.")],
            ),
            "GO:0016020": (
                "Membrane localization is true but less informative than plasma membrane for this bacterial inner-membrane permease.",
                "MARK_AS_OVER_ANNOTATED",
                "The record also has a plasma-membrane annotation and UniProt predicts a cell inner-membrane multi-pass protein.",
                None,
                [support_uniprot("PP_0280", "Cell inner membrane")],
            ),
            "GO:0022857": (
                "Generic transmembrane transporter activity is too broad for this ABC-transporter permease component.",
                "MODIFY",
                "The binding-protein-dependent transporter domains and ABC-transporter complex annotation support ABC-type amino-acid transporter activity as the better complex-level activity.",
                [ABC_AMINO_ACID],
                [support_uniprot("PP_0280", "Full=Arginine ABC transporter permease protein ArtM")],
            ),
            "GO:0043190": (
                "ABC transporter complex membership is appropriate for this ArtM permease.",
                "ACCEPT",
                "PP_0280 is a binding-protein-dependent transport-system permease in the local Art/Aot ABC importer locus.",
                None,
                [support_uniprot("PP_0280", "Belongs to the binding-protein-dependent transport system")],
            ),
            "GO:0055085": (
                "Transmembrane transport is true but broad relative to the arginine ABC-import context.",
                "MODIFY",
                "L-arginine transmembrane transport better captures the expected transported substrate for this ArtM-family permease.",
                [ARG_TRANSPORT],
                [support_uniprot("PP_0280", "Full=Arginine ABC transporter permease protein ArtM")],
            ),
        },
        "core": {
            "description": "Multi-pass permease component contributing to a predicted ABC-type L-arginine uptake system.",
            "contributes_to_molecular_function": ABC_AMINO_ACID,
            "directly_involved_in": [ARG_TRANSPORT],
            "locations": [PLASMA_MEMBRANE],
            "in_complex": ABC_COMPLEX,
            "support": ("GO:0043190", "ATP-binding cassette (ABC) transporter complex"),
        },
    },
    "PP_0281": {
        "symbol": "PP_0281",
        "description": (
            "PP_0281 encodes a predicted ArtQ-like multi-pass permease in the "
            "PP_0280-PP_0283 arginine/basic-amino-acid ABC uptake locus. It belongs "
            "to the HisMQ/MetI-like binding-protein-dependent transport-system "
            "permease family and is best treated as the second membrane channel "
            "component of the transporter."
        ),
        "uniprot_text": "Full=Amino acid ABC transporter, permease protein",
        "asta_text": "Protein Description:** SubName: Full=Amino acid ABC transporter, permease protein",
        "reviews": {
            "GO:0005886": (
                "Plasma membrane localization is appropriate for this predicted inner-membrane ABC permease.",
                "ACCEPT",
                "UniProt predicts PP_0281 as a cell inner-membrane multi-pass membrane protein.",
                None,
                [support_uniprot("PP_0281", "Cell inner membrane")],
            ),
            "GO:0016020": (
                "Membrane localization is true but less informative than plasma membrane for this bacterial inner-membrane permease.",
                "MARK_AS_OVER_ANNOTATED",
                "The record also has a plasma-membrane annotation and UniProt predicts a cell inner-membrane multi-pass protein.",
                None,
                [support_uniprot("PP_0281", "Cell inner membrane")],
            ),
            "GO:0022857": (
                "Generic transmembrane transporter activity is too broad for this ABC-transporter permease component.",
                "MODIFY",
                "The ArtQ PANTHER subfamily and binding-protein-dependent transporter domains support ABC-type amino-acid transporter activity as the better complex-level activity.",
                [ABC_AMINO_ACID],
                [support_uniprot("PP_0281", "PANTHER; PTHR30133:SF2; ARGININE ABC TRANSPORTER PERMEASE PROTEIN ARTQ; 1.")],
            ),
            "GO:0043190": (
                "ABC transporter complex membership is appropriate for this ArtQ-like permease.",
                "ACCEPT",
                "PP_0281 is a binding-protein-dependent transport-system permease in the local Art/Aot ABC importer locus.",
                None,
                [support_uniprot("PP_0281", "Belongs to the binding-protein-dependent transport system")],
            ),
            "GO:0055085": (
                "Transmembrane transport is true but broad relative to the arginine ABC-import context.",
                "MODIFY",
                "The ArtQ PANTHER subfamily and colocalization with artJ/aotP support L-arginine transmembrane transport as a better first-pass process term.",
                [ARG_TRANSPORT],
                [support_uniprot("PP_0281", "PANTHER; PTHR30133:SF2; ARGININE ABC TRANSPORTER PERMEASE PROTEIN ARTQ; 1.")],
            ),
        },
        "new_annotations": [
            {
                "term": ARG_TRANSPORT,
                "qualifier": "involved_in",
                "summary": "L-arginine transmembrane transport is a useful missing process annotation for this ArtQ-like permease.",
                "reason": "PP_0281 is an ArtQ-family permease adjacent to ArtM, ArtJ, and AotP in a predicted arginine/basic-amino-acid ABC importer.",
                "supporting_text": "PANTHER; PTHR30133:SF2; ARGININE ABC TRANSPORTER PERMEASE PROTEIN ARTQ; 1.",
            }
        ],
        "core": {
            "description": "Second multi-pass permease component contributing to a predicted ABC-type L-arginine uptake system.",
            "contributes_to_molecular_function": ABC_AMINO_ACID,
            "directly_involved_in": [ARG_TRANSPORT],
            "locations": [PLASMA_MEMBRANE],
            "in_complex": ABC_COMPLEX,
            "support": ("GO:0043190", "ATP-binding cassette (ABC) transporter complex"),
        },
    },
    "artJ": {
        "symbol": "artJ",
        "description": (
            "artJ (PP_0282) encodes a signal-peptide-bearing bacterial solute-binding "
            "protein 3 family member named as the L-arginine ABC transporter "
            "periplasmic binding subunit. It is the predicted periplasmic substrate "
            "recognition component of the adjacent PP_0280-PP_0283 Art/Aot ABC "
            "amino-acid uptake system."
        ),
        "uniprot_text": "Full=L-arginine ABC transporter-periplasmic binding subunit",
        "asta_text": "Protein Description:** SubName: Full=L-arginine ABC transporter-periplasmic binding subunit",
        "new_annotations": [
            {
                "term": AA_BINDING,
                "qualifier": "enables",
                "summary": "Amino acid binding captures the substrate-binding role expected for this ArtJ solute-binding protein.",
                "reason": "UniProt names ArtJ as an L-arginine ABC transporter periplasmic binding subunit and records a bacterial solute-binding protein family domain.",
                "supporting_text": "Full=L-arginine ABC transporter-periplasmic binding subunit",
            },
            {
                "term": PERIPLASM,
                "qualifier": "located_in",
                "summary": "Outer membrane-bounded periplasmic space is the appropriate location for this predicted Gram-negative solute-binding component.",
                "reason": "ArtJ has an N-terminal signal peptide and is named as a periplasmic binding subunit.",
                "supporting_text": "FT   SIGNAL          1..23",
            },
            {
                "term": ARG_TRANSPORT,
                "qualifier": "involved_in",
                "summary": "L-arginine transmembrane transport is a useful missing process annotation for ArtJ.",
                "reason": "The product name and adjacent ArtM/ArtQ/AotP transporter components support an L-arginine ABC uptake role.",
                "supporting_text": "Full=L-arginine ABC transporter-periplasmic binding subunit",
            },
            {
                "term": ABC_AMINO_ACID,
                "qualifier": "contributes_to",
                "summary": "ArtJ should be recorded as contributing to the ABC-type amino acid transporter activity of the adjacent importer.",
                "reason": "As a periplasmic solute-binding protein, ArtJ supplies substrate-recognition capacity rather than catalyzing transmembrane transport alone.",
                "supporting_text": "Full=L-arginine ABC transporter-periplasmic binding subunit",
            },
            {
                "term": ABC_COMPLEX,
                "qualifier": "part_of",
                "summary": "ABC transporter complex membership is appropriate for this ArtJ substrate-binding component.",
                "reason": "ArtJ is named as the periplasmic binding subunit of an L-arginine ABC transporter and is adjacent to the ArtM/ArtQ permeases and AotP ATP-binding component.",
                "supporting_text": "Full=L-arginine ABC transporter-periplasmic binding subunit",
            },
        ],
        "core": {
            "description": "Periplasmic L-arginine-family substrate-binding component contributing substrate capture to a predicted ABC-type amino-acid uptake system.",
            "molecular_function": AA_BINDING,
            "contributes_to_molecular_function": ABC_AMINO_ACID,
            "directly_involved_in": [ARG_TRANSPORT],
            "locations": [PERIPLASM],
            "in_complex": ABC_COMPLEX,
            "support": None,
            "support_in_goa": False,
        },
    },
    "aotP": {
        "symbol": "aotP",
        "description": (
            "aotP (PP_0283) encodes the ATP-binding energy-coupling subunit of a "
            "predicted arginine/ornithine ABC uptake system. Its ABC transporter "
            "ATP-binding domains support ATP hydrolysis-driven transport in the "
            "PP_0280-PP_0283 Art/Aot locus."
        ),
        "uniprot_text": "Full=Arginine/ornithine transport ATP-binding protein AotP",
        "asta_text": "Protein Description:** SubName: Full=Arginine/ornithine transport ATP-binding protein AotP",
        "reviews": {
            "GO:0000166": (
                "Nucleotide binding is true but less informative than ATP binding for this ABC ATPase.",
                "MARK_AS_OVER_ANNOTATED",
                "The review retains the more specific ATP-binding and ATP-hydrolysis annotations for the transporter ATPase.",
            ),
            "GO:0003333": (
                "Amino acid transmembrane transport is correct but too broad for the arginine/ornithine transporter ATPase context.",
                "MODIFY",
                "UniProt names AotP as an arginine/ornithine transport ATP-binding protein, so L-arginine and L-ornithine transmembrane transport are better first-pass process terms.",
                [ARG_TRANSPORT, ORN_TRANSPORT],
                [support_uniprot("aotP", "Full=Arginine/ornithine transport ATP-binding protein AotP")],
            ),
            "GO:0005524": (
                "ATP binding is correct for the ABC-transporter nucleotide-binding component.",
                "ACCEPT",
                "AotP has ABC transporter ATP-binding domains and is named as the ATP-binding protein of an arginine/ornithine transport system.",
                None,
                [support_uniprot("aotP", "FT   DOMAIN          8..253")],
            ),
            "GO:0005886": (
                "Plasma membrane localization is appropriate for the inner-membrane-associated ABC transporter ATPase.",
                "ACCEPT",
                "UniProt places AotP at the cell inner membrane as a peripheral membrane protein.",
                None,
                [support_uniprot("aotP", "Cell inner membrane")],
            ),
            "GO:0015424": (
                "ABC-type amino acid transporter activity is appropriate for this ATP-binding component at first pass.",
                "ACCEPT",
                "AotP is the ATP-binding component of an arginine/ornithine amino-acid ABC transport system.",
                None,
                [support_asta("aotP", "Protein Description:** SubName: Full=Arginine/ornithine transport ATP-binding protein AotP")],
            ),
            "GO:0016887": (
                "ATP hydrolysis activity is the correct mechanistic activity for the ABC ATPase subunit.",
                "ACCEPT",
                "ATP hydrolysis by AotP is expected to provide energy coupling to the Art/Aot ABC importer.",
                None,
                [support_uniprot("aotP", "Full=Arginine/ornithine transport ATP-binding protein AotP")],
            ),
        },
        "new_annotations": [
            {
                "term": ARG_TRANSPORT,
                "qualifier": "involved_in",
                "summary": "L-arginine transmembrane transport is a useful missing process annotation for AotP.",
                "reason": "The product name identifies AotP as the ATP-binding component of an arginine/ornithine transport system.",
                "supporting_text": "Full=Arginine/ornithine transport ATP-binding protein AotP",
            },
            {
                "term": ORN_TRANSPORT,
                "qualifier": "involved_in",
                "summary": "L-ornithine transmembrane transport is a useful missing process annotation for AotP.",
                "reason": "The product name identifies AotP as the ATP-binding component of an arginine/ornithine transport system.",
                "supporting_text": "Full=Arginine/ornithine transport ATP-binding protein AotP",
            },
            {
                "term": ABC_COMPLEX,
                "qualifier": "part_of",
                "summary": "ABC transporter complex membership is appropriate for this AotP ATP-binding component.",
                "reason": "AotP is named as the ATP-binding protein of the adjacent arginine/ornithine ABC transport system.",
                "supporting_text": "Full=Arginine/ornithine transport ATP-binding protein AotP",
            },
        ],
        "core": {
            "description": "ATP-binding energy-coupling subunit contributing to a predicted arginine/ornithine ABC uptake system.",
            "molecular_function": ATP_HYDROLYSIS,
            "contributes_to_molecular_function": ABC_AMINO_ACID,
            "directly_involved_in": [ARG_TRANSPORT, ORN_TRANSPORT],
            "locations": [PLASMA_MEMBRANE],
            "in_complex": ABC_COMPLEX,
            "support": ("GO:0016887", "ATP hydrolysis activity"),
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
        doc.setdefault("existing_annotations", []).append(
            new_annotation(
                term,
                extra["qualifier"],
                uniprot_ref(gene),
                extra["summary"],
                extra["reason"],
                [
                    support_uniprot(gene, extra["supporting_text"]),
                    support_asta(gene, cfg["asta_text"]),
                ],
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
            "question": "Does the PP_0280-PP_0283 Art/Aot ABC importer transport L-arginine only, or does it also import L-ornithine and other basic amino acids in P. putida KT2440?"
        }
    ]
    doc["suggested_experiments"] = [
        {
            "description": "Measure uptake and growth phenotypes for PP_0280, PP_0281, artJ, and aotP mutants with L-arginine, L-ornithine, L-lysine, and related amino acids as nitrogen or carbon sources.",
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
