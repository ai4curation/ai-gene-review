#!/usr/bin/env python3
"""First-pass curation for the ppu02010 PP_1068-PP_1071 GltIJKL importer."""

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
GLU_TRANSPORT = {"id": "GO:0015813", "label": "L-glutamate transmembrane transport"}
ASP_TRANSPORT = {"id": "GO:0070778", "label": "L-aspartate transmembrane transport"}
ATP_BINDING = {"id": "GO:0005524", "label": "ATP binding"}
ATP_HYDROLYSIS = {"id": "GO:0016887", "label": "ATP hydrolysis activity"}
ABC_COMPLEX = {"id": "GO:0043190", "label": "ATP-binding cassette (ABC) transporter complex"}
PLASMA_MEMBRANE = {"id": "GO:0005886", "label": "plasma membrane"}
PERIPLASM = {"id": "GO:0030288", "label": "outer membrane-bounded periplasmic space"}


GLT_PROCESS_TERMS = [GLU_TRANSPORT, ASP_TRANSPORT]


CONFIG = {
    "gltL": {
        "symbol": "gltL",
        "description": (
            "gltL (PP_1068) encodes the ATP-binding energy-coupling subunit of "
            "the predicted GltIJKL glutamate/aspartate ABC uptake system. Its "
            "ABC transporter ATP-binding domains support ATP hydrolysis-driven "
            "amino-acid transport with the adjacent GltK/GltJ permeases and GltI "
            "periplasmic solute-binding component."
        ),
        "uniprot_text": "Full=Glutamate / aspartate ABC transporter-ATP binding subunit",
        "asta_text": "Protein Description:** SubName: Full=Glutamate / aspartate ABC transporter-ATP binding subunit",
        "reviews": {
            "GO:0000166": (
                "Nucleotide binding is true but less informative than ATP binding for this ABC ATPase.",
                "MARK_AS_OVER_ANNOTATED",
                "The review retains the more specific ATP-binding and ATP-hydrolysis annotations for the transporter ATPase.",
                None,
                [support_uniprot("gltL", "Full=Glutamate / aspartate ABC transporter-ATP binding subunit")],
            ),
            "GO:0003333": (
                "Amino acid transmembrane transport is correct but too broad for the GltIJKL glutamate/aspartate uptake context.",
                "MODIFY",
                "The product name and adjacent GltK/GltJ/GltI components support substrate-specific L-glutamate and L-aspartate transmembrane transport as better process terms.",
                GLT_PROCESS_TERMS,
                [support_uniprot("gltL", "Full=Glutamate / aspartate ABC transporter-ATP binding subunit")],
            ),
            "GO:0005524": (
                "ATP binding is correct for the ABC-transporter nucleotide-binding component.",
                "ACCEPT",
                "GltL has ABC transporter ATP-binding domains and is named as the ATP-binding subunit of a glutamate/aspartate ABC transporter.",
                None,
                [support_uniprot("gltL", "FT   DOMAIN          14..248")],
            ),
            "GO:0005886": (
                "Plasma membrane localization is appropriate for this inner-membrane-associated ABC transporter ATPase.",
                "ACCEPT",
                "UniProt places GltL at the cell inner membrane as a peripheral membrane protein.",
                None,
                [support_uniprot("gltL", "Cell inner membrane")],
            ),
            "GO:0015424": (
                "ABC-type amino acid transporter activity is appropriate at first pass for this ATP-binding component.",
                "ACCEPT",
                "GltL is the ATP-binding component of a predicted glutamate/aspartate amino-acid ABC uptake system.",
                None,
                [support_asta("gltL", "Protein Description:** SubName: Full=Glutamate / aspartate ABC transporter-ATP binding subunit")],
            ),
            "GO:0016887": (
                "ATP hydrolysis activity is the correct mechanistic activity for the ABC ATPase subunit.",
                "ACCEPT",
                "ATP hydrolysis by GltL is expected to provide energy coupling to the GltIJKL ABC importer.",
                None,
                [support_uniprot("gltL", "Belongs to the ABC transporter superfamily.")],
            ),
        },
        "new_annotations": [
            {
                "term": GLU_TRANSPORT,
                "qualifier": "involved_in",
                "summary": "L-glutamate transmembrane transport is a useful missing process annotation for the GltL ATP-binding component.",
                "reason": "The product name identifies GltL as the ATP-binding subunit of a glutamate/aspartate ABC transporter.",
                "supporting_text": "Full=Glutamate / aspartate ABC transporter-ATP binding subunit",
            },
            {
                "term": ASP_TRANSPORT,
                "qualifier": "involved_in",
                "summary": "L-aspartate transmembrane transport is a useful missing process annotation for the GltL ATP-binding component.",
                "reason": "The product name identifies GltL as the ATP-binding subunit of a glutamate/aspartate ABC transporter.",
                "supporting_text": "Full=Glutamate / aspartate ABC transporter-ATP binding subunit",
            },
            {
                "term": ABC_COMPLEX,
                "qualifier": "part_of",
                "summary": "ABC transporter complex membership is appropriate for this GltL ATP-binding component.",
                "reason": "GltL is the ATP-binding subunit of the adjacent predicted GltIJKL amino-acid ABC importer.",
                "supporting_text": "Full=Glutamate / aspartate ABC transporter-ATP binding subunit",
            },
        ],
        "core": {
            "description": "ATP-binding energy-coupling subunit of a predicted GltIJKL glutamate/aspartate ABC uptake system.",
            "molecular_function": ATP_HYDROLYSIS,
            "contributes_to_molecular_function": ABC_AMINO_ACID,
            "directly_involved_in": GLT_PROCESS_TERMS,
            "locations": [PLASMA_MEMBRANE],
            "in_complex": ABC_COMPLEX,
            "support": ("GO:0016887", "ATP hydrolysis activity"),
        },
    },
    "gltK": {
        "symbol": "gltK",
        "description": (
            "gltK (PP_1069) encodes a predicted multi-pass inner-membrane "
            "permease of the GltIJKL glutamate/aspartate ABC uptake system. "
            "UniProt describes GltK as part of the GltIJKL complex involved in "
            "glutamate and aspartate uptake, probably responsible for substrate "
            "translocation across the membrane."
        ),
        "uniprot_text": "Full=Glutamate/aspartate import permease protein GltK",
        "asta_text": "Protein Description:** RecName: Full=Glutamate/aspartate import permease protein GltK",
        "function_text": "glutamate and aspartate uptake",
        "reviews": {
            "GO:0005886": (
                "Plasma membrane localization is appropriate for this predicted inner-membrane ABC permease.",
                "ACCEPT",
                "UniProt predicts GltK as a cell inner-membrane multi-pass membrane protein.",
                None,
                [support_uniprot("gltK", "Cell inner membrane")],
            ),
            "GO:0006865": (
                "Amino acid transport is correct but should be narrowed to glutamate/aspartate uptake for this GltIJKL permease.",
                "MODIFY",
                "UniProt states that GltK is part of the GltIJKL complex involved in glutamate and aspartate uptake, supporting L-glutamate and L-aspartate transmembrane transport as better process terms.",
                GLT_PROCESS_TERMS,
                [support_uniprot("gltK", "glutamate and aspartate uptake")],
            ),
            "GO:0016020": (
                "Membrane localization is true but less informative than plasma membrane for this bacterial inner-membrane permease.",
                "MARK_AS_OVER_ANNOTATED",
                "The record also has a plasma-membrane annotation and UniProt predicts a cell inner-membrane multi-pass protein.",
                None,
                [support_uniprot("gltK", "Cell inner membrane")],
            ),
            "GO:0022857": (
                "Generic transmembrane transporter activity is too broad for this ABC-transporter permease component.",
                "MODIFY",
                "GltK is a binding-protein-dependent transporter permease in the GltIJKL amino-acid ABC importer, so ABC-type amino-acid transporter activity is the better complex-level activity.",
                [ABC_AMINO_ACID],
                [support_uniprot("gltK", "Full=Glutamate/aspartate import permease protein GltK")],
            ),
            "GO:0043190": (
                "ABC transporter complex membership is appropriate for this GltK permease.",
                "ACCEPT",
                "UniProt describes GltK as part of the GltIJKL ABC transporter complex.",
                None,
                [support_uniprot("gltK", "Part of the ABC transporter complex GltIJKL involved in")],
            ),
            "GO:0055085": (
                "Transmembrane transport is true but broad relative to the glutamate/aspartate ABC-import context.",
                "MODIFY",
                "L-glutamate and L-aspartate transmembrane transport better capture the expected substrate processes for this GltIJKL permease.",
                GLT_PROCESS_TERMS,
                [support_uniprot("gltK", "glutamate and aspartate uptake")],
            ),
        },
        "new_annotations": [
            {
                "term": GLU_TRANSPORT,
                "qualifier": "involved_in",
                "summary": "L-glutamate transmembrane transport is a useful missing process annotation for GltK.",
                "reason": "UniProt states that the GltIJKL complex is involved in glutamate and aspartate uptake.",
                "supporting_text": "glutamate and aspartate uptake",
            },
            {
                "term": ASP_TRANSPORT,
                "qualifier": "involved_in",
                "summary": "L-aspartate transmembrane transport is a useful missing process annotation for GltK.",
                "reason": "UniProt states that the GltIJKL complex is involved in glutamate and aspartate uptake.",
                "supporting_text": "glutamate and aspartate uptake",
            },
        ],
        "core": {
            "description": "Multi-pass permease component contributing to a predicted GltIJKL glutamate/aspartate ABC uptake system.",
            "contributes_to_molecular_function": ABC_AMINO_ACID,
            "directly_involved_in": GLT_PROCESS_TERMS,
            "locations": [PLASMA_MEMBRANE],
            "in_complex": ABC_COMPLEX,
            "support": ("GO:0043190", "ATP-binding cassette (ABC) transporter complex"),
        },
    },
    "gltJ": {
        "symbol": "gltJ",
        "description": (
            "gltJ (PP_1070) encodes the second predicted multi-pass "
            "inner-membrane permease of the GltIJKL glutamate/aspartate ABC "
            "uptake system. Its MetI-like binding-protein-dependent transporter "
            "domains and adjacency to gltL, gltK, and gltI support a membrane "
            "channel role in ATP-driven acidic amino-acid import."
        ),
        "uniprot_text": "Full=Glutamate / aspartate ABC transporter-permease subunit",
        "asta_text": "Protein Description:** SubName: Full=Glutamate / aspartate ABC transporter-permease subunit",
        "reviews": {
            "GO:0005886": (
                "Plasma membrane localization is appropriate for this predicted inner-membrane ABC permease.",
                "ACCEPT",
                "UniProt predicts GltJ as a cell inner-membrane multi-pass membrane protein.",
                None,
                [support_uniprot("gltJ", "Cell inner membrane")],
            ),
            "GO:0006865": (
                "Amino acid transport is correct but too broad for the glutamate/aspartate ABC-import context.",
                "MODIFY",
                "The product name and local GltIJKL locus support substrate-specific L-glutamate and L-aspartate transmembrane transport as better process terms.",
                GLT_PROCESS_TERMS,
                [support_uniprot("gltJ", "Full=Glutamate / aspartate ABC transporter-permease subunit")],
            ),
            "GO:0016020": (
                "Membrane localization is true but less informative than plasma membrane for this bacterial inner-membrane permease.",
                "MARK_AS_OVER_ANNOTATED",
                "The record also has a plasma-membrane annotation and UniProt predicts a cell inner-membrane multi-pass protein.",
                None,
                [support_uniprot("gltJ", "Cell inner membrane")],
            ),
            "GO:0022857": (
                "Generic transmembrane transporter activity is too broad for this ABC-transporter permease component.",
                "MODIFY",
                "GltJ is a binding-protein-dependent transporter permease in a glutamate/aspartate ABC importer, so ABC-type amino-acid transporter activity is the better complex-level activity.",
                [ABC_AMINO_ACID],
                [support_uniprot("gltJ", "Full=Glutamate / aspartate ABC transporter-permease subunit")],
            ),
            "GO:0043190": (
                "ABC transporter complex membership is appropriate for this GltJ permease.",
                "ACCEPT",
                "GltJ is a binding-protein-dependent transport-system permease in the local GltIJKL importer locus.",
                None,
                [support_uniprot("gltJ", "Belongs to the binding-protein-dependent transport system")],
            ),
            "GO:0055085": (
                "Transmembrane transport is true but broad relative to the glutamate/aspartate ABC-import context.",
                "MODIFY",
                "L-glutamate and L-aspartate transmembrane transport better capture the expected substrate processes for this GltIJKL permease.",
                GLT_PROCESS_TERMS,
                [support_uniprot("gltJ", "Full=Glutamate / aspartate ABC transporter-permease subunit")],
            ),
        },
        "new_annotations": [
            {
                "term": GLU_TRANSPORT,
                "qualifier": "involved_in",
                "summary": "L-glutamate transmembrane transport is a useful missing process annotation for GltJ.",
                "reason": "The product name identifies GltJ as a glutamate/aspartate ABC transporter permease.",
                "supporting_text": "Full=Glutamate / aspartate ABC transporter-permease subunit",
            },
            {
                "term": ASP_TRANSPORT,
                "qualifier": "involved_in",
                "summary": "L-aspartate transmembrane transport is a useful missing process annotation for GltJ.",
                "reason": "The product name identifies GltJ as a glutamate/aspartate ABC transporter permease.",
                "supporting_text": "Full=Glutamate / aspartate ABC transporter-permease subunit",
            },
        ],
        "core": {
            "description": "Second multi-pass permease component contributing to a predicted GltIJKL glutamate/aspartate ABC uptake system.",
            "contributes_to_molecular_function": ABC_AMINO_ACID,
            "directly_involved_in": GLT_PROCESS_TERMS,
            "locations": [PLASMA_MEMBRANE],
            "in_complex": ABC_COMPLEX,
            "support": ("GO:0043190", "ATP-binding cassette (ABC) transporter complex"),
        },
    },
    "gltI": {
        "symbol": "gltI",
        "description": (
            "gltI (PP_1071) encodes a signal-peptide-bearing periplasmic "
            "solute-binding protein of the bacterial solute-binding protein 3 "
            "family. Its product name and locus position support a substrate "
            "recognition role in the predicted GltIJKL glutamate/aspartate ABC "
            "uptake system."
        ),
        "uniprot_text": "Full=Glutamate / aspartate ABC transporter-periplasmic binding protein",
        "asta_text": "Protein Description:** SubName: Full=Glutamate / aspartate ABC transporter-periplasmic binding protein",
        "reviews": {
            "GO:0005576": (
                "Extracellular region is a broad TreeGrafter location for this Gram-negative periplasmic binding protein.",
                "MARK_AS_OVER_ANNOTATED",
                "The same record has more informative periplasmic annotations, and UniProt predicts a periplasmic signal-peptide-bearing solute-binding protein.",
                None,
                [support_uniprot("gltI", "Periplasm")],
            ),
            "GO:0006865": (
                "Amino acid transport is correct but too broad for the glutamate/aspartate binding-component context.",
                "MODIFY",
                "The product name and local GltIJKL locus support substrate-specific L-glutamate and L-aspartate transmembrane transport as better process terms.",
                GLT_PROCESS_TERMS,
                [support_uniprot("gltI", "Full=Glutamate / aspartate ABC transporter-periplasmic binding protein")],
            ),
            "GO:0030288": (
                "Outer membrane-bounded periplasmic space is appropriate for this predicted Gram-negative solute-binding component.",
                "ACCEPT",
                "UniProt predicts GltI as a periplasmic protein with an N-terminal signal peptide.",
                None,
                [support_uniprot("gltI", "FT   SIGNAL          1..24")],
            ),
            "GO:0042597": (
                "Periplasmic space is correct but less precise than outer membrane-bounded periplasmic space for this Gram-negative protein.",
                "MARK_AS_OVER_ANNOTATED",
                "The review retains GO:0030288 as the more specific location for this P. putida periplasmic binding component.",
                None,
                [support_uniprot("gltI", "Periplasm")],
            ),
        },
        "new_annotations": [
            {
                "term": AA_BINDING,
                "qualifier": "enables",
                "summary": "Amino acid binding captures the substrate-recognition role expected for this GltI solute-binding protein.",
                "reason": "UniProt names GltI as a glutamate/aspartate ABC transporter periplasmic binding protein and records a solute-binding protein family domain.",
                "supporting_text": "Full=Glutamate / aspartate ABC transporter-periplasmic binding protein",
            },
            {
                "term": GLU_TRANSPORT,
                "qualifier": "involved_in",
                "summary": "L-glutamate transmembrane transport is a useful missing process annotation for GltI.",
                "reason": "The product name and adjacent GltL/GltK/GltJ transporter components support a glutamate/aspartate ABC uptake role.",
                "supporting_text": "Full=Glutamate / aspartate ABC transporter-periplasmic binding protein",
            },
            {
                "term": ASP_TRANSPORT,
                "qualifier": "involved_in",
                "summary": "L-aspartate transmembrane transport is a useful missing process annotation for GltI.",
                "reason": "The product name and adjacent GltL/GltK/GltJ transporter components support a glutamate/aspartate ABC uptake role.",
                "supporting_text": "Full=Glutamate / aspartate ABC transporter-periplasmic binding protein",
            },
            {
                "term": ABC_AMINO_ACID,
                "qualifier": "contributes_to",
                "summary": "GltI should be recorded as contributing to the ABC-type amino acid transporter activity of the adjacent importer.",
                "reason": "As a periplasmic solute-binding protein, GltI supplies substrate-recognition capacity rather than catalyzing transmembrane transport alone.",
                "supporting_text": "Full=Glutamate / aspartate ABC transporter-periplasmic binding protein",
            },
            {
                "term": ABC_COMPLEX,
                "qualifier": "part_of",
                "summary": "ABC transporter complex membership is appropriate for this GltI substrate-binding component.",
                "reason": "GltI is named as the periplasmic binding protein of an adjacent glutamate/aspartate ABC transporter locus.",
                "supporting_text": "Full=Glutamate / aspartate ABC transporter-periplasmic binding protein",
            },
        ],
        "core": {
            "description": "Periplasmic glutamate/aspartate-family substrate-binding component contributing substrate capture to a predicted ABC-type amino-acid uptake system.",
            "molecular_function": AA_BINDING,
            "contributes_to_molecular_function": ABC_AMINO_ACID,
            "directly_involved_in": GLT_PROCESS_TERMS,
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
            "question": "Does the PP_1068-PP_1071 GltIJKL ABC importer transport both L-glutamate and L-aspartate in P. putida KT2440, and does it show a strong preference for one substrate?"
        }
    ]
    doc["suggested_experiments"] = [
        {
            "description": "Measure uptake and growth phenotypes for gltL, gltK, gltJ, and gltI mutants with L-glutamate and L-aspartate supplied as carbon or nitrogen sources.",
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
