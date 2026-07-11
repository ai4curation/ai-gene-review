#!/usr/bin/env python3
"""First-pass curation for the ppu02010 C48 partial glycine-betaine ABC transporter pair."""

from __future__ import annotations

from copy import deepcopy
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
) -> dict:
    supported_by = [support_goa(gene, term_id, label)]
    if uniprot_text:
        supported_by.append(support_uniprot(gene, uniprot_text))
    if asta_text:
        supported_by.append(support_asta(gene, asta_text))
    return {
        "summary": summary,
        "action": action,
        "reason": reason,
        "supported_by": supported_by,
    }


def new_annotation(term: dict, qualifier: str, gene: str, summary: str, reason: str, supported_by: list[dict]) -> dict:
    return {
        "term": deepcopy(term),
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


GLYCINE_BETAINE_TRANSPORT = {"id": "GO:0031460", "label": "glycine betaine transport"}
QUATERNARY_AMMONIUM_TRANSPORTER = {
    "id": "GO:0015418",
    "label": "ABC-type quaternary ammonium compound transporting activity",
}
ABC_COMPLEX = {"id": "GO:0043190", "label": "ATP-binding cassette (ABC) transporter complex"}
PERIPLASM = {"id": "GO:0042597", "label": "periplasmic space"}
PLASMA_MEMBRANE = {"id": "GO:0005886", "label": "plasma membrane"}


CONFIG = {
    "PP_3558": {
        "symbol": "PP_3558",
        "description": (
            "PP_3558 encodes a signal-peptide-bearing substrate-binding component with an "
            "OpuAC/ABC glycine-betaine transport-system substrate-binding domain. Although "
            "the product name says amino acid-binding protein, the domain assignment and "
            "adjacent PP_3559 glycine-betaine permease support a first-pass role as the "
            "periplasmic binding component of a partial glycine-betaine-compatible-solute "
            "ABC transporter pair."
        ),
        "uniprot_text": "Full=Amino acid transporter, periplasmic amino acid-binding protein",
        "asta_text": "Protein Description:** SubName: Full=Amino acid transporter, periplasmic amino acid-binding protein",
        "reviews": {
            "GO:0022857": (
                "Generic transmembrane transporter activity is too broad and potentially misleading for this substrate-binding component.",
                "MARK_AS_OVER_ANNOTATED",
                "PP_3558 likely supplies substrate recognition to an ABC importer rather than forming the membrane translocation pathway itself.",
                "ABC_Gly_betaine_transp_sub-bd",
            ),
            "GO:0043190": (
                "ABC transporter complex membership is appropriate for this substrate-binding component.",
                "ACCEPT",
                "The OpuAC/ABC glycine-betaine substrate-binding domain and adjacent PP_3559 permease support an ABC transporter component role.",
                "ABC_Gly_betaine_transp_sub-bd",
            ),
            "GO:0055085": (
                "Transmembrane transport is correct only as transporter-system context and is less precise than glycine betaine compatible-solute transport.",
                "MARK_AS_OVER_ANNOTATED",
                "The protein is a signal-peptide-bearing substrate-binding component; the adjacent PP_3559 permease would provide the membrane channel.",
                "Full=Amino acid transporter, periplasmic amino acid-binding protein",
            ),
        },
        "new": [
            new_annotation(
                GLYCINE_BETAINE_TRANSPORT,
                "involved_in",
                "PP_3558",
                "PP_3558 should be represented with glycine betaine transport as compatible-solute process context.",
                "The OpuAC/ABC glycine-betaine substrate-binding domain and adjacent PP_3559 glycine-betaine permease support this process assignment.",
                [
                    support_uniprot("PP_3558", "ABC_Gly_betaine_transp_sub-bd"),
                    support_uniprot("PP_3558", "SIGNAL          1..26"),
                    support_asta("PP_3558", "Protein Description:** SubName: Full=Amino acid transporter, periplasmic amino acid-binding protein"),
                ],
            ),
            new_annotation(
                QUATERNARY_AMMONIUM_TRANSPORTER,
                "contributes_to",
                "PP_3558",
                "PP_3558 should be recorded as contributing substrate recognition to ABC-type quaternary ammonium compound transport.",
                "As a periplasmic OpuAC-family binding component, PP_3558 likely contributes substrate recognition rather than ATP hydrolysis or membrane translocation.",
                [
                    support_uniprot("PP_3558", "ABC_Gly_betaine_transp_sub-bd"),
                    support_uniprot("PP_3558", "Full=Amino acid transporter, periplasmic amino acid-binding protein"),
                ],
            ),
            new_annotation(
                PERIPLASM,
                "located_in",
                "PP_3558",
                "PP_3558 should be represented as a periplasmic substrate-binding component.",
                "UniProt predicts an N-terminal signal peptide and an OpuAC/periplasmic-binding-protein-like domain architecture.",
                [
                    support_uniprot("PP_3558", "SIGNAL          1..26"),
                    support_uniprot("PP_3558", "Periplasmic binding protein-like"),
                ],
            ),
        ],
        "core": {
            "description": "Periplasmic substrate-binding component of a partial PP_3558-PP_3559 glycine-betaine compatible-solute ABC transporter pair.",
            "contributes_to_molecular_function": QUATERNARY_AMMONIUM_TRANSPORTER,
            "directly_involved_in": [GLYCINE_BETAINE_TRANSPORT],
            "locations": [PERIPLASM],
            "in_complex": ABC_COMPLEX,
            "support": [
                support_uniprot("PP_3558", "ABC_Gly_betaine_transp_sub-bd"),
                support_uniprot("PP_3558", "SIGNAL          1..26"),
                support_asta("PP_3558", "Protein Description:** SubName: Full=Amino acid transporter, periplasmic amino acid-binding protein"),
            ],
        },
    },
    "PP_3559": {
        "symbol": "PP_3559",
        "description": (
            "PP_3559 encodes a predicted multi-pass membrane permease of a glycine betaine "
            "ABC transporter. Its product name, MetI-like ABC transmembrane domain, plasma "
            "membrane localization, and adjacent PP_3558 OpuAC-family binding component "
            "support a compatible-solute importer role, with the ATPase partner unresolved "
            "in the immediate two-gene locus."
        ),
        "uniprot_text": "Full=Glycine betaine ABC transporter (Permease)",
        "asta_text": "Protein Description:** SubName: Full=Glycine betaine ABC transporter (Permease)",
        "reviews": {
            "GO:0005275": (
                "Amine transmembrane transporter activity is true but broad for this glycine-betaine permease.",
                "MARK_AS_OVER_ANNOTATED",
                "Glycine betaine transport and ABC complex membership better capture the substrate-specific role.",
                "Full=Glycine betaine ABC transporter (Permease)",
            ),
            "GO:0005886": (
                "Plasma membrane localization is appropriate for this multi-pass bacterial inner-membrane permease.",
                "ACCEPT",
                "UniProt places PP_3559 at the cell membrane and predicts multiple transmembrane helices.",
                "Cell membrane",
            ),
            "GO:0015226": (
                "Carnitine transmembrane transporter activity is plausible Cbc-family context but not the strongest PP_3559 substrate call.",
                "KEEP_AS_NON_CORE",
                "The product name and ARBA/PANTHER assignments are strongest for glycine betaine/proline betaine permease context.",
                "Full=Glycine betaine ABC transporter (Permease)",
            ),
            "GO:0015837": (
                "Amine transport is broad compatible-solute context and is less informative than glycine betaine transport.",
                "MARK_AS_OVER_ANNOTATED",
                "The product and family assignments support a glycine-betaine ABC permease rather than generic amine transport.",
                "Full=Glycine betaine ABC transporter (Permease)",
            ),
            "GO:0015871": (
                "Choline transport is plausible compatible-solute context but is not the core PP_3559 substrate call.",
                "KEEP_AS_NON_CORE",
                "TreeGrafter links this permease family to choline/betaine/carnitine transport, but the product name is specifically glycine betaine ABC transporter permease.",
                "Full=Glycine betaine ABC transporter (Permease)",
            ),
            "GO:0016020": (
                "Membrane localization is correct but less specific than plasma membrane for this bacterial inner-membrane permease.",
                "MARK_AS_OVER_ANNOTATED",
                "The plasma membrane annotation is the more informative retained location.",
                "Cell membrane",
            ),
            "GO:0031460": (
                "Glycine betaine transport is the best supported process annotation for PP_3559.",
                "ACCEPT",
                "The product name identifies PP_3559 as a glycine betaine ABC transporter permease.",
                "Full=Glycine betaine ABC transporter (Permease)",
            ),
            "GO:0043190": (
                "ABC transporter complex membership is appropriate for this permease component.",
                "ACCEPT",
                "The product and MetI-like binding-protein-dependent transport-system permease domain support ABC transporter complex membership.",
                "Belongs to the binding-protein-dependent transport system",
            ),
            "GO:0055085": (
                "Transmembrane transport is true but broad relative to glycine betaine transport for this permease.",
                "MARK_AS_OVER_ANNOTATED",
                "The glycine betaine transport annotation better captures the substrate-specific biological process.",
                "Full=Glycine betaine ABC transporter (Permease)",
            ),
            "GO:1902603": (
                "Carnitine transmembrane transport is plausible Cbc-family context but should be kept non-core for PP_3559.",
                "KEEP_AS_NON_CORE",
                "The product name is specifically glycine betaine ABC transporter permease, so carnitine transport should not be treated as the defining process.",
                "Full=Glycine betaine ABC transporter (Permease)",
            ),
        },
        "new": [
            new_annotation(
                QUATERNARY_AMMONIUM_TRANSPORTER,
                "contributes_to",
                "PP_3559",
                "PP_3559 should be represented as contributing the membrane permease function to ABC-type quaternary ammonium compound transport.",
                "Glycine betaine is a quaternary-amine compatible solute, and PP_3559 is the predicted membrane permease component.",
                [
                    support_uniprot("PP_3559", "Full=Glycine betaine ABC transporter (Permease)"),
                    support_uniprot("PP_3559", "MetI-like"),
                    support_asta("PP_3559", "Protein Description:** SubName: Full=Glycine betaine ABC transporter (Permease)"),
                ],
            )
        ],
        "core": {
            "description": "Multi-pass membrane permease of a partial PP_3558-PP_3559 glycine-betaine compatible-solute ABC transporter pair.",
            "contributes_to_molecular_function": QUATERNARY_AMMONIUM_TRANSPORTER,
            "directly_involved_in": [GLYCINE_BETAINE_TRANSPORT],
            "locations": [PLASMA_MEMBRANE],
            "in_complex": ABC_COMPLEX,
            "support": [
                support_goa("PP_3559", "GO:0031460", "glycine betaine transport"),
                support_uniprot("PP_3559", "Full=Glycine betaine ABC transporter (Permease)"),
                support_uniprot("PP_3559", "MetI-like"),
                support_asta("PP_3559", "Protein Description:** SubName: Full=Glycine betaine ABC transporter (Permease)"),
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

    doc["existing_annotations"].extend(deepcopy(cfg.get("new", [])))

    core = deepcopy(cfg["core"])
    core["supported_by"] = core.pop("support")
    doc["core_functions"] = [core]
    doc["proposed_new_terms"] = []
    doc["suggested_questions"] = [
        {
            "question": "Which ATPase partner completes the PP_3558-PP_3559 compatible-solute ABC importer, and what is the exact ligand range?"
        }
    ]
    doc["suggested_experiments"] = [
        {
            "description": "Test PP_3558 ligand binding and PP_3558/PP_3559 mutant uptake or osmotic-stress growth phenotypes with glycine betaine, proline betaine, choline, and carnitine.",
            "experiment_type": "targeted transporter mutant substrate-uptake and ligand-binding assay",
        }
    ]

    path.write_text(yaml.safe_dump(doc, sort_keys=False, width=1000))
    print(f"curated {path}")


def main() -> None:
    for gene, cfg in CONFIG.items():
        curate_gene(gene, cfg)


if __name__ == "__main__":
    main()
