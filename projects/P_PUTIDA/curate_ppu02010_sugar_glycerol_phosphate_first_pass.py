#!/usr/bin/env python3
"""First-pass curation for the ppu02010 C32 sugar/glycerol-phosphate ABC locus."""

from __future__ import annotations

from pathlib import Path

import yaml


SPECIES = "PSEPK"


def file_ref(gene: str, suffix: str) -> str:
    return f"file:{SPECIES}/{gene}/{gene}-{suffix}"


def goa_ref(gene: str) -> str:
    return file_ref(gene, "goa.tsv")


def uniprot_ref(gene: str) -> str:
    return file_ref(gene, "uniprot.txt")


def asta_ref(gene: str) -> str:
    return file_ref(gene, "deep-research-asta.md")


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


ATP_BINDING = {"id": "GO:0005524", "label": "ATP binding"}
ABC_TYPE_TRANSPORTER = {"id": "GO:0140359", "label": "ABC-type transporter activity"}
CARBOHYDRATE_BINDING = {"id": "GO:0030246", "label": "carbohydrate binding"}
TRANSMEMBRANE_TRANSPORT = {"id": "GO:0055085", "label": "transmembrane transport"}
PLASMA_MEMBRANE = {"id": "GO:0005886", "label": "plasma membrane"}
CELL_ENVELOPE = {"id": "GO:0030313", "label": "cell envelope"}
ABC_COMPLEX = {"id": "GO:0043190", "label": "ATP-binding cassette (ABC) transporter complex"}


def atpase_reviews(gene: str, product_text: str, is_generic_sugar: bool = False) -> dict:
    transport_summary = (
        "The local product and domain context support a sugar/glycerol-phosphate-like ABC transporter, not a ferric-iron transporter."
    )
    reviews = {
        "GO:0000166": (
            "Nucleotide binding is correct but broad for this ABC ATP-binding component.",
            "MARK_AS_OVER_ANNOTATED",
            "ATP binding is the more informative nucleotide-binding term for this ABC transporter ATPase.",
            "ATP-binding protein",
        ),
        "GO:0005524": (
            "ATP binding is appropriate for this ABC transporter ATP-binding component.",
            "ACCEPT",
            "The UniProt product name and ABC transporter ATP-binding domains support ATP binding.",
            "ATP-binding protein",
        ),
        "GO:0006826": (
            "Iron ion transport is not supported for this locus and appears to be an InterPro FbpC spillover.",
            "REMOVE",
            transport_summary,
            product_text,
        ),
        "GO:0015408": (
            "ABC-type ferric iron transporter activity is not supported for this locus and appears over-propagated from a broad FbpC-like domain.",
            "REMOVE",
            transport_summary,
            product_text,
        ),
        "GO:0016020": (
            "Membrane localization is plausible for a subunit of a membrane ABC transporter complex but is not the core function of the ATPase.",
            "KEEP_AS_NON_CORE",
            "The local locus encodes a membrane transporter complex, while this subunit is the ATP-binding component.",
            "ABC_transpr_MalK/UgpC-like",
        ),
        "GO:0016887": (
            "ATP hydrolysis is correct mechanistic chemistry but non-core relative to ABC transporter energy coupling.",
            "KEEP_AS_NON_CORE",
            "ATP hydrolysis powers ABC transport, while substrate specificity remains unresolved in this first pass.",
            "ABC_transporter-like_ATP-bd",
        ),
        "GO:0034755": (
            "Iron ion transmembrane transport is not supported for this sugar/glycerol-phosphate-like locus.",
            "REMOVE",
            transport_summary,
            product_text,
        ),
        "GO:0043190": (
            "ABC transporter complex membership is appropriate for this ATP-binding subunit.",
            "ACCEPT",
            "The product is an ABC transporter ATP-binding protein in a local ABC transporter locus.",
            "ABC_transpr_MalK/UgpC-like",
        ),
        "GO:0055052": (
            "A substrate-binding-subunit-containing ABC transporter complex is appropriate for this importer locus.",
            "ACCEPT",
            "The adjacent PP_2264 product is a periplasmic sugar-binding protein, consistent with an ABC importer complex.",
            product_text,
        ),
        "GO:0098655": (
            "Monoatomic cation transmembrane transport is a downstream inference from the unsupported ferric-iron term and should be removed.",
            "REMOVE",
            transport_summary,
            product_text,
        ),
    }
    if is_generic_sugar:
        reviews["GO:0055085"] = (
            "Transmembrane transport is appropriate but broad for this unresolved sugar/glycerol-phosphate ABC transporter locus.",
            "ACCEPT",
            "The product is a sugar ABC transporter ATP-binding protein, but the transported substrate is not resolved.",
            product_text,
        )
        reviews["GO:0140359"] = (
            "Generic ABC-type transporter activity is appropriate at first pass because substrate specificity is unresolved.",
            "ACCEPT",
            "The product is an ABC transporter ATP-binding protein in a sugar/glycerol-phosphate-like importer locus.",
            product_text,
        )
    return reviews


CONFIG = {
    "PP_2260": {
        "symbol": "PP_2260",
        "description": (
            "PP_2260 encodes an ATP-binding component of the PP_2260-PP_2264 unresolved "
            "sugar/glycerol-phosphate-like ABC importer locus. The product is named a "
            "glycerol-phosphate ABC transporter ATP-binding protein, but neighboring "
            "permease and binding-protein annotations are sugar-transporter-like, so "
            "the first-pass substrate call remains unresolved."
        ),
        "uniprot_text": "Full=Glycerol-phosphate ABC transporter, ATP-binding protein",
        "asta_text": "Protein Description:** SubName: Full=Glycerol-phosphate ABC transporter, ATP-binding protein",
        "reviews": atpase_reviews("PP_2260", "Full=Glycerol-phosphate ABC transporter, ATP-binding protein"),
        "new": [
            new_annotation(
                ABC_TYPE_TRANSPORTER,
                "contributes_to",
                "PP_2260",
                "PP_2260 contributes ATP-binding energy coupling to a generic ABC-type transporter activity.",
                "The locus supports an ABC importer, but substrate specificity is not resolved enough for a substrate-specific transporter term.",
                [
                    support_uniprot("PP_2260", "Full=Glycerol-phosphate ABC transporter, ATP-binding protein"),
                    support_uniprot("PP_2260", "ABC_transpr_MalK/UgpC-like"),
                    support_asta("PP_2260", "Protein Description:** SubName: Full=Glycerol-phosphate ABC transporter, ATP-binding protein"),
                ],
            ),
            new_annotation(
                TRANSMEMBRANE_TRANSPORT,
                "involved_in",
                "PP_2260",
                "PP_2260 should be represented with transmembrane transport as a generic process term for this unresolved ABC importer.",
                "The locus supports an ABC importer, but substrate specificity is not resolved enough for a substrate-specific transport process.",
                [
                    support_uniprot("PP_2260", "Full=Glycerol-phosphate ABC transporter, ATP-binding protein"),
                    support_uniprot("PP_2260", "ABC_transpr_MalK/UgpC-like"),
                ],
            ),
        ],
        "core": {
            "description": "ATP-binding component of the unresolved PP_2260-PP_2264 sugar/glycerol-phosphate-like ABC importer.",
            "molecular_function": ATP_BINDING,
            "directly_involved_in": [TRANSMEMBRANE_TRANSPORT],
            "in_complex": ABC_COMPLEX,
            "support": [
                support_goa("PP_2260", "GO:0005524", "ATP binding"),
                support_uniprot("PP_2260", "Full=Glycerol-phosphate ABC transporter, ATP-binding protein"),
                support_uniprot("PP_2260", "ABC_transpr_MalK/UgpC-like"),
                support_asta("PP_2260", "Protein Description:** SubName: Full=Glycerol-phosphate ABC transporter, ATP-binding protein"),
            ],
        },
    },
    "PP_2261": {
        "symbol": "PP_2261",
        "description": (
            "PP_2261 encodes a second ATP-binding component of the PP_2260-PP_2264 "
            "unresolved sugar/glycerol-phosphate-like ABC importer locus. Its product "
            "name and domains support ABC transporter energy coupling, while ferric-iron "
            "IEA terms appear to be broad FbpC-family spillovers."
        ),
        "uniprot_text": "Full=Sugar ABC transporter, ATP-binding protein",
        "asta_text": "Protein Description:** SubName: Full=Sugar ABC transporter, ATP-binding protein",
        "reviews": atpase_reviews("PP_2261", "Full=Sugar ABC transporter, ATP-binding protein", True),
        "new": [],
        "core": {
            "description": "ATP-binding component of the unresolved PP_2260-PP_2264 sugar/glycerol-phosphate-like ABC importer.",
            "molecular_function": ATP_BINDING,
            "directly_involved_in": [TRANSMEMBRANE_TRANSPORT],
            "in_complex": ABC_COMPLEX,
            "support": [
                support_goa("PP_2261", "GO:0005524", "ATP binding"),
                support_uniprot("PP_2261", "Full=Sugar ABC transporter, ATP-binding protein"),
                support_uniprot("PP_2261", "ABC_transpr_MalK/UgpC-like"),
                support_asta("PP_2261", "Protein Description:** SubName: Full=Sugar ABC transporter, ATP-binding protein"),
            ],
        },
    },
    "PP_2262": {
        "symbol": "PP_2262",
        "description": (
            "PP_2262 encodes a multi-pass plasma-membrane permease component of the "
            "PP_2260-PP_2264 unresolved sugar/glycerol-phosphate-like ABC importer. "
            "Its product name and PANTHER/InterPro annotations are sugar ABC "
            "transporter-like, but the transported substrate remains unresolved."
        ),
        "uniprot_text": "Full=Sugar ABC transporter, permease protein",
        "asta_text": "Protein Description:** SubName: Full=Sugar ABC transporter, permease protein",
        "reviews": {
            "GO:0005886": (
                "Plasma membrane localization is appropriate for this multi-pass transporter permease.",
                "ACCEPT",
                "UniProt places PP_2262 at the cell membrane and predicts a multi-pass membrane protein.",
                "Cell membrane",
            ),
            "GO:0016020": (
                "Membrane localization is correct but less specific than plasma membrane for this bacterial permease.",
                "MARK_AS_OVER_ANNOTATED",
                "The plasma membrane annotation is the more informative retained location.",
                "Cell membrane",
            ),
            "GO:0043190": (
                "ABC transporter complex membership is appropriate for this permease subunit.",
                "ACCEPT",
                "The product is a sugar ABC transporter permease in a local ABC importer locus.",
                "Full=Sugar ABC transporter, permease protein",
            ),
            "GO:0055085": (
                "Transmembrane transport is appropriate but broad because substrate specificity is unresolved.",
                "ACCEPT",
                "The product and domains support a sugar ABC permease, but not a specific transported sugar or glycerol-phosphate ligand.",
                "Sugar_ABC_transporter",
            ),
        },
        "new": [
            new_annotation(
                ABC_TYPE_TRANSPORTER,
                "contributes_to",
                "PP_2262",
                "PP_2262 contributes a membrane permease component to generic ABC-type transporter activity.",
                "The locus supports an ABC importer, but substrate specificity is unresolved.",
                [
                    support_uniprot("PP_2262", "Full=Sugar ABC transporter, permease protein"),
                    support_uniprot("PP_2262", "Sugar_ABC_transporter"),
                    support_asta("PP_2262", "Protein Description:** SubName: Full=Sugar ABC transporter, permease protein"),
                ],
            ),
        ],
        "core": {
            "description": "Membrane permease component of the unresolved PP_2260-PP_2264 sugar/glycerol-phosphate-like ABC importer.",
            "contributes_to_molecular_function": ABC_TYPE_TRANSPORTER,
            "directly_involved_in": [TRANSMEMBRANE_TRANSPORT],
            "locations": [PLASMA_MEMBRANE],
            "in_complex": ABC_COMPLEX,
            "support": [
                support_goa("PP_2262", "GO:0005886", "plasma membrane"),
                support_uniprot("PP_2262", "Full=Sugar ABC transporter, permease protein"),
                support_uniprot("PP_2262", "Sugar_ABC_transporter"),
                support_asta("PP_2262", "Protein Description:** SubName: Full=Sugar ABC transporter, permease protein"),
            ],
        },
    },
    "PP_2263": {
        "symbol": "PP_2263",
        "description": (
            "PP_2263 encodes a second multi-pass plasma-membrane permease component of "
            "the PP_2260-PP_2264 unresolved sugar/glycerol-phosphate-like ABC importer. "
            "Its product name and binding-protein-dependent ABC permease domains support "
            "a transporter-subunit role, but not a resolved substrate call."
        ),
        "uniprot_text": "Full=Sugar ABC transporter, permease protein",
        "asta_text": "Protein Description:** SubName: Full=Sugar ABC transporter, permease protein",
        "reviews": {
            "GO:0005886": (
                "Plasma membrane localization is appropriate for this multi-pass transporter permease.",
                "ACCEPT",
                "UniProt places PP_2263 at the cell membrane and predicts a multi-pass membrane protein.",
                "Cell membrane",
            ),
            "GO:0016020": (
                "Membrane localization is correct but less specific than plasma membrane for this bacterial permease.",
                "MARK_AS_OVER_ANNOTATED",
                "The plasma membrane annotation is the more informative retained location.",
                "Cell membrane",
            ),
            "GO:0043190": (
                "ABC transporter complex membership is appropriate for this permease subunit.",
                "ACCEPT",
                "The product is a sugar ABC transporter permease in a local ABC importer locus.",
                "Full=Sugar ABC transporter, permease protein",
            ),
            "GO:0055085": (
                "Transmembrane transport is appropriate but broad because substrate specificity is unresolved.",
                "ACCEPT",
                "The product and domains support an ABC permease, but not a specific transported sugar or glycerol-phosphate ligand.",
                "BP-dep_ABC_trans_perm",
            ),
        },
        "new": [
            new_annotation(
                ABC_TYPE_TRANSPORTER,
                "contributes_to",
                "PP_2263",
                "PP_2263 contributes a membrane permease component to generic ABC-type transporter activity.",
                "The locus supports an ABC importer, but substrate specificity is unresolved.",
                [
                    support_uniprot("PP_2263", "Full=Sugar ABC transporter, permease protein"),
                    support_uniprot("PP_2263", "BP-dep_ABC_trans_perm"),
                    support_asta("PP_2263", "Protein Description:** SubName: Full=Sugar ABC transporter, permease protein"),
                ],
            ),
        ],
        "core": {
            "description": "Membrane permease component of the unresolved PP_2260-PP_2264 sugar/glycerol-phosphate-like ABC importer.",
            "contributes_to_molecular_function": ABC_TYPE_TRANSPORTER,
            "directly_involved_in": [TRANSMEMBRANE_TRANSPORT],
            "locations": [PLASMA_MEMBRANE],
            "in_complex": ABC_COMPLEX,
            "support": [
                support_goa("PP_2263", "GO:0005886", "plasma membrane"),
                support_uniprot("PP_2263", "Full=Sugar ABC transporter, permease protein"),
                support_uniprot("PP_2263", "BP-dep_ABC_trans_perm"),
                support_asta("PP_2263", "Protein Description:** SubName: Full=Sugar ABC transporter, permease protein"),
            ],
        },
    },
    "PP_2264": {
        "symbol": "PP_2264",
        "description": (
            "PP_2264 encodes the predicted periplasmic sugar-binding component of the "
            "PP_2260-PP_2264 unresolved sugar/glycerol-phosphate-like ABC importer. "
            "The product name, signal peptide, and bacterial solute-binding-protein "
            "family support carbohydrate binding, but not a resolved ligand."
        ),
        "uniprot_text": "Full=Sugar ABC transporter, periplasmic sugar-binding protein",
        "asta_text": "Protein Description:** SubName: Full=Sugar ABC transporter, periplasmic sugar-binding protein",
        "reviews": {
            "GO:0022857": (
                "Transmembrane transporter activity is too broad and directly assigned to a periplasmic binding component.",
                "MARK_AS_OVER_ANNOTATED",
                "PP_2264 is better represented as a carbohydrate-binding solute-binding component that contributes to an ABC transporter complex.",
                "Full=Sugar ABC transporter, periplasmic sugar-binding protein",
            ),
            "GO:0055085": (
                "Transmembrane transport is plausible process context for this solute-binding component but remains broad and substrate-unresolved.",
                "ACCEPT",
                "The product is a periplasmic sugar-binding component of an ABC transporter locus, but the ligand is unresolved.",
                "Full=Sugar ABC transporter, periplasmic sugar-binding protein",
            ),
        },
        "new": [
            new_annotation(
                CARBOHYDRATE_BINDING,
                "enables",
                "PP_2264",
                "PP_2264 should be represented with carbohydrate binding.",
                "The product is named as a periplasmic sugar-binding protein.",
                [
                    support_uniprot("PP_2264", "Full=Sugar ABC transporter, periplasmic sugar-binding protein"),
                    support_uniprot("PP_2264", "Bact_solute-bd_prot1"),
                    support_asta("PP_2264", "Protein Description:** SubName: Full=Sugar ABC transporter, periplasmic sugar-binding protein"),
                ],
            ),
            new_annotation(
                CELL_ENVELOPE,
                "located_in",
                "PP_2264",
                "PP_2264 should be represented as a cell-envelope/periplasmic solute-binding component.",
                "The product is named periplasmic and has an N-terminal signal peptide.",
                [
                    support_uniprot("PP_2264", "periplasmic sugar-binding protein"),
                    support_uniprot("PP_2264", "SIGNAL          1..28"),
                ],
            ),
            new_annotation(
                ABC_COMPLEX,
                "part_of",
                "PP_2264",
                "PP_2264 should be represented as part of an ABC transporter complex.",
                "The product is the periplasmic sugar-binding component of a local ABC transporter locus.",
                [support_uniprot("PP_2264", "Full=Sugar ABC transporter, periplasmic sugar-binding protein")],
            ),
            new_annotation(
                ABC_TYPE_TRANSPORTER,
                "contributes_to",
                "PP_2264",
                "PP_2264 contributes the substrate-binding component to generic ABC-type transporter activity.",
                "The transported ligand is unresolved, so a generic ABC transporter contribution is safer than a substrate-specific term.",
                [
                    support_uniprot("PP_2264", "Full=Sugar ABC transporter, periplasmic sugar-binding protein"),
                    support_uniprot("PP_2264", "Bact_solute-bd_prot1"),
                ],
            ),
        ],
        "core": {
            "description": "Periplasmic carbohydrate-binding component of the unresolved PP_2260-PP_2264 sugar/glycerol-phosphate-like ABC importer.",
            "molecular_function": CARBOHYDRATE_BINDING,
            "directly_involved_in": [TRANSMEMBRANE_TRANSPORT],
            "locations": [CELL_ENVELOPE],
            "in_complex": ABC_COMPLEX,
            "support": [
                support_uniprot("PP_2264", "Full=Sugar ABC transporter, periplasmic sugar-binding protein"),
                support_uniprot("PP_2264", "Bact_solute-bd_prot1"),
                support_uniprot("PP_2264", "SIGNAL          1..28"),
                support_asta("PP_2264", "Protein Description:** SubName: Full=Sugar ABC transporter, periplasmic sugar-binding protein"),
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
            "question": "Does PP_2260-PP_2264 import glycerol-3-phosphate, a specific sugar, or a broader sugar alcohol/oligosaccharide substrate range?"
        },
        {
            "question": "Do PP_2260 and PP_2261 both function as ATP-binding components of the same importer, or are they paralogous alternatives used under different conditions?"
        },
    ]
    doc["suggested_experiments"] = [
        {
            "description": "Measure uptake and growth phenotypes for PP_2260-PP_2264 mutants on sn-glycerol-3-phosphate, glycerol, glucose, trehalose, maltose/maltodextrin, and related sugar substrates.",
            "experiment_type": "ABC transporter substrate uptake and growth assay",
        },
        {
            "description": "Purify PP_2264 and test ligand binding against glycerol-3-phosphate and candidate sugar/polyol substrates.",
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
