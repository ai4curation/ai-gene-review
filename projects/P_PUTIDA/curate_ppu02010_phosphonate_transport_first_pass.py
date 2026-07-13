#!/usr/bin/env python3
"""First-pass curation for the ppu02010 phosphonate ABC transporter block."""

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
    asta_text: str | None = None,
    proposed: list[dict] | None = None,
) -> dict:
    supported_by = [support_goa(gene, term_id, label)]
    if asta_text:
        supported_by.append(support_asta(gene, asta_text))
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
    term_id: str,
    label: str,
    qualifier: str,
    original_reference_id: str,
    summary: str,
    reason: str,
    supported_by: list[dict],
) -> dict:
    return {
        "term": {"id": term_id, "label": label},
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


PHOSPHONATE_TRANSPORT = {"id": "GO:0015716", "label": "organic phosphonate transport"}
PHOSPHONATE_TRANSPORTER = {
    "id": "GO:0015416",
    "label": "ABC-type phosphonate transporter activity",
}
ABC_COMPLEX = {"id": "GO:0043190", "label": "ATP-binding cassette (ABC) transporter complex"}
PLASMA_MEMBRANE = {"id": "GO:0005886", "label": "plasma membrane"}
PERIPLASM = {"id": "GO:0042597", "label": "periplasmic space"}


CONFIG = {
    "ptxB": {
        "symbol": "ptxB",
        "description": (
            "ptxB (PP_0824) encodes a predicted periplasmic solute-binding component of a "
            "phosphonate ABC import system. Its signal peptide and PhnD-like phosphonate-binding "
            "domain support a role in capturing extracellular or periplasmic phosphonate substrate "
            "for delivery to the PhnC/PtxC/PhnE transporter complex."
        ),
        "asta_text": "Protein Description:** SubName: Full=Phosphonate transport system-binding protein",
        "uniprot_text": "Full=Phosphonate transport system-binding protein",
        "reviews": {
            "GO:0043190": (
                "ABC transporter complex membership is appropriate for this PhnD-like phosphonate-binding component.",
                "ACCEPT",
                "The protein is named as a phosphonate transport system-binding protein and carries PhnD/phosphonate-binding InterPro domains, consistent with a solute-binding component of an ABC-type importer.",
            ),
            "GO:0055085": (
                "Transmembrane transport is correct but too broad for this phosphonate-binding ABC-import component.",
                "MODIFY",
                "The local ptxB-phnC-phnE-ptxC block and PhnD-like domain support organic phosphonate transport as the more informative biological-process assertion.",
                [PHOSPHONATE_TRANSPORT],
            ),
        },
        "new_annotations": [
            {
                "term": PERIPLASM,
                "qualifier": "located_in",
                "summary": "Periplasmic localization is a reasonable new first-pass location annotation for this signal-peptide-bearing ABC solute-binding protein.",
                "reason": "PtxB is a predicted phosphonate transport system-binding protein with an N-terminal signal peptide and a mature chain, matching the expected periplasmic solute-binding component of a Gram-negative ABC importer.",
                "supporting_text": "FT   SIGNAL          1..23",
            }
        ],
        "core": {
            "description": "Periplasmic phosphonate-binding component that contributes substrate capture to an ABC-type phosphonate import system.",
            "contributes_to_molecular_function": PHOSPHONATE_TRANSPORTER,
            "directly_involved_in": [PHOSPHONATE_TRANSPORT],
            "locations": [PERIPLASM],
            "in_complex": ABC_COMPLEX,
            "support": ("GO:0043190", "ATP-binding cassette (ABC) transporter complex"),
        },
    },
    "phnC": {
        "symbol": "phnC",
        "description": (
            "phnC (PP_0825) encodes the ATP-binding energy-coupling component of the PhnCDE/Ptx "
            "phosphonate ABC importer. The reviewed UniProt record assigns EC 7.3.2.2 and describes "
            "ATP-driven import of phosphonates across the bacterial inner membrane."
        ),
        "asta_text": "Protein Description:** RecName: Full=Phosphonates import ATP-binding protein PhnC",
        "uniprot_text": "Part of the ABC transporter complex PhnCDE involved in",
        "reviews": {
            "GO:0005524": (
                "ATP binding is correct for the nucleotide-binding domain of PhnC.",
                "ACCEPT",
                "PhnC is the ATP-binding energy-coupling subunit of the phosphonate importer and has canonical ABC transporter ATP-binding-domain features.",
            ),
            "GO:0005886": (
                "Plasma membrane localization is appropriate for the inner-membrane-associated ABC importer ATPase.",
                "ACCEPT",
                "UniProt places PhnC at the cell inner membrane as a peripheral membrane protein associated with the PhnCDE transporter.",
            ),
            "GO:0015416": (
                "ABC-type phosphonate transporter activity is the core functional assignment for PhnC.",
                "ACCEPT",
                "The reviewed UniProt record assigns EC 7.3.2.2 and the phosphonate import reaction, identifying PhnC as the energy-coupling ATPase for ABC-type phosphonate import.",
            ),
            "GO:0015716": (
                "Organic phosphonate transport is the correct biological-process context for PhnC.",
                "ACCEPT",
                "The transporter reaction moves phosphonate from outside to inside using ATP hydrolysis, directly supporting organic phosphonate import.",
            ),
            "GO:0016887": (
                "ATP hydrolysis activity is correct mechanistic context for the ABC transporter ATPase.",
                "KEEP_AS_NON_CORE",
                "ATP hydrolysis powers the transporter, but the substrate-specific core assertion is ABC-type phosphonate transporter activity.",
            ),
        },
        "new_annotations": [
            {
                "term": ABC_COMPLEX,
                "qualifier": "part_of",
                "summary": "ABC transporter complex membership is a useful missing annotation for PhnC.",
                "reason": "The reviewed UniProt entry explicitly describes PhnC as part of the PhnCDE ABC transporter complex responsible for phosphonate import.",
                "supporting_text": "Part of the ABC transporter complex PhnCDE involved in",
            }
        ],
        "core": {
            "description": "ATP-binding energy-coupling component of an ABC-type phosphonate importer, driving phosphonate uptake through ATP hydrolysis.",
            "molecular_function": PHOSPHONATE_TRANSPORTER,
            "directly_involved_in": [PHOSPHONATE_TRANSPORT],
            "locations": [PLASMA_MEMBRANE],
            "in_complex": ABC_COMPLEX,
            "support": ("GO:0015416", "ABC-type phosphonate transporter activity"),
        },
    },
    "phnE": {
        "symbol": "phnE",
        "description": (
            "phnE (PP_0826) encodes a predicted multi-pass inner-membrane permease component of "
            "the phosphonate ABC import locus. It is best treated as a transporter subunit that "
            "contributes the membrane channel component of the PhnC/PtxC/PhnE phosphonate uptake system."
        ),
        "asta_text": "Protein Description:** SubName: Full=Phosphonate ABC transporter, permease protein",
        "uniprot_text": "Full=Phosphonate ABC transporter, permease protein",
        "reviews": {
            "GO:0005886": (
                "Plasma membrane localization is appropriate for this multi-pass transporter permease.",
                "ACCEPT",
                "UniProt predicts PhnE as a cell-membrane multi-pass membrane protein with an ABC transmembrane type-1 domain.",
            ),
            "GO:0016020": (
                "Membrane localization is correct but less specific than the plasma-membrane annotation.",
                "MARK_AS_OVER_ANNOTATED",
                "The same record has the more informative plasma membrane annotation, so the generic membrane term adds little.",
            ),
            "GO:0043190": (
                "ABC transporter complex membership is appropriate for this permease component.",
                "ACCEPT",
                "The protein is a binding-protein-dependent transport-system permease in the local phosphonate ABC import locus.",
            ),
            "GO:0055085": (
                "Transmembrane transport is correct but too broad for this phosphonate ABC permease.",
                "MODIFY",
                "The phosphonate permease product name, PhnE/PtxC-family context, and adjacent phnC/ptxC genes support organic phosphonate transport as the better process term.",
                [PHOSPHONATE_TRANSPORT],
            ),
        },
        "core": {
            "description": "Multi-pass inner-membrane permease component contributing to ABC-type phosphonate import.",
            "contributes_to_molecular_function": PHOSPHONATE_TRANSPORTER,
            "directly_involved_in": [PHOSPHONATE_TRANSPORT],
            "locations": [PLASMA_MEMBRANE],
            "in_complex": ABC_COMPLEX,
            "support": ("GO:0043190", "ATP-binding cassette (ABC) transporter complex"),
        },
    },
    "ptxC": {
        "symbol": "ptxC",
        "description": (
            "ptxC (PP_0827) encodes a predicted PhnE/PtxC-family multi-pass permease component of "
            "an ABC-type phosphonate import system. Together with PhnC, PhnE, and the PtxB "
            "solute-binding protein, it forms the membrane transport machinery for organic phosphonate uptake."
        ),
        "asta_text": "Protein Description:** SubName: Full=Phosphonate transport system permease protein PtxC",
        "uniprot_text": "Full=Phosphonate transport system permease protein PtxC",
        "reviews": {
            "GO:0005886": (
                "Plasma membrane localization is appropriate for this multi-pass permease.",
                "ACCEPT",
                "UniProt predicts PtxC as a cell-membrane multi-pass membrane protein, and GOA supports plasma membrane localization.",
            ),
            "GO:0015416": (
                "ABC-type phosphonate transporter activity is appropriate for this PhnE/PtxC-family permease component.",
                "ACCEPT",
                "The InterPro PhnE/PtxC assignment and phosphonate transporter product name support the substrate-specific transporter activity annotation.",
            ),
            "GO:0015716": (
                "Organic phosphonate transport is the correct process context for PtxC.",
                "ACCEPT",
                "The PhnE/PtxC-family permease assignment supports participation in ABC-type phosphonate uptake.",
            ),
            "GO:0016020": (
                "Membrane localization is correct but less specific than plasma membrane.",
                "MARK_AS_OVER_ANNOTATED",
                "The plasma-membrane annotation gives the more specific cellular location for this transporter component.",
            ),
            "GO:0043190": (
                "ABC transporter complex membership is appropriate for this permease component.",
                "ACCEPT",
                "PtxC is a PhnE/PtxC-family permease in a local phosphonate ABC import locus.",
            ),
            "GO:0055085": (
                "Transmembrane transport is true but broad relative to the existing organic phosphonate transport annotation.",
                "MARK_AS_OVER_ANNOTATED",
                "GO:0015716 already captures the substrate-specific biological process for this transporter component.",
            ),
        },
        "core": {
            "description": "Multi-pass PhnE/PtxC-family permease component of an ABC-type phosphonate importer.",
            "molecular_function": PHOSPHONATE_TRANSPORTER,
            "directly_involved_in": [PHOSPHONATE_TRANSPORT],
            "locations": [PLASMA_MEMBRANE],
            "in_complex": ABC_COMPLEX,
            "support": ("GO:0015416", "ABC-type phosphonate transporter activity"),
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

    for ann in doc.get("existing_annotations", []):
        term = ann["term"]
        term_id = term["id"]
        label = term["label"]
        entry = cfg["reviews"][term_id]
        proposed = entry[3] if len(entry) > 3 else None
        asta_text = cfg["asta_text"] if term_id == cfg["core"]["support"][0] else None
        ann["review"] = review(
            gene,
            term_id,
            label,
            entry[0],
            entry[1],
            entry[2],
            asta_text=asta_text,
            proposed=proposed,
        )

    existing_term_ids = {ann["term"]["id"] for ann in doc.get("existing_annotations", [])}
    for extra in cfg.get("new_annotations", []):
        term = extra["term"]
        if term["id"] in existing_term_ids:
            continue
        doc.setdefault("existing_annotations", []).append(
            new_annotation(
                term["id"],
                term["label"],
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

    core = dict(cfg["core"])
    support_term = core.pop("support")
    core["supported_by"] = [
        support_goa(gene, support_term[0], support_term[1]),
        support_uniprot(gene, cfg["uniprot_text"]),
        support_asta(gene, cfg["asta_text"]),
    ]
    doc["core_functions"] = [core]
    doc["proposed_new_terms"] = []
    doc["suggested_questions"] = [
        {
            "question": "Which organic phosphonates are transported by the PP_0824-PP_0827 phosphonate ABC importer in P. putida KT2440, and is it induced under phosphate limitation?"
        }
    ]
    doc["suggested_experiments"] = [
        {
            "description": "Test growth and uptake of wild type and PP_0824-PP_0827 transporter mutants on 2-aminoethylphosphonate and related phosphonates as phosphorus sources, with phosphate-replete and phosphate-limited controls.",
            "experiment_type": "targeted transporter mutant growth and substrate-uptake assay",
        }
    ]

    path.write_text(yaml.safe_dump(doc, sort_keys=False, width=1000))
    print(f"curated {path}")


def main() -> None:
    for gene, cfg in CONFIG.items():
        curate_gene(gene, cfg)


if __name__ == "__main__":
    main()
