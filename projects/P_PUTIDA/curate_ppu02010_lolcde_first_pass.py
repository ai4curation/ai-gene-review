#!/usr/bin/env python3
"""First-pass curation for the ppu02010 PP_2154-PP_2156 LolCDE system."""

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


LIPOPROTEIN_TRANSPORT = {"id": "GO:0042953", "label": "lipoprotein transport"}
LIPOPROTEIN_LOCALIZATION_OUTER_MEMBRANE = {
    "id": "GO:0044874",
    "label": "lipoprotein localization to outer membrane",
}
LIPOPROTEIN_LOCALIZATION_MEMBRANE = {
    "id": "GO:0044873",
    "label": "lipoprotein localization to membrane",
}
PROTEIN_LOCALIZATION_OUTER_MEMBRANE = {
    "id": "GO:0089705",
    "label": "protein localization to outer membrane",
}
TRANSMM_TRANSPORT = {"id": "GO:0055085", "label": "transmembrane transport"}
TRANSPORTER_ACTIVITY = {"id": "GO:0022857", "label": "transmembrane transporter activity"}
ATPASE_COUPLED_TRANSPORTER = {
    "id": "GO:0042626",
    "label": "ATPase-coupled transmembrane transporter activity",
}
ATP_BINDING = {"id": "GO:0005524", "label": "ATP binding"}
ATP_HYDROLYSIS = {"id": "GO:0016887", "label": "ATP hydrolysis activity"}
PLASMA_MEMBRANE = {"id": "GO:0005886", "label": "plasma membrane"}
MEMBRANE = {"id": "GO:0016020", "label": "membrane"}
PLASMA_MEMBRANE_PROTEIN_COMPLEX = {
    "id": "GO:0098797",
    "label": "plasma membrane protein complex",
}


GENES = {
    "lolC": {
        "kind": "permease",
        "accession": "Q88KY5",
        "description": (
            "lolC encodes one of the two multi-pass membrane permease components "
            "of the PP_2154-PP_2156 LolCDE lipoprotein-releasing ABC transporter. "
            "UniProt places LolC in the cell membrane and assigns the LolC/E "
            "lipoprotein-release domain family; GOA supports lipoprotein transport "
            "and localization to the outer membrane."
        ),
        "product_text": "Full=LolC",
        "asta_text": "Protein Description:** SubName: Full=LolC",
        "location_text": "Cell membrane",
        "family_text": "Belongs to the ABC-4 integral membrane protein family.",
        "domain_text": "InterPro; IPR011925; LolCE_TM.",
    },
    "lolD": {
        "kind": "atpase",
        "accession": "Q88KY4",
        "description": (
            "lolD encodes the reviewed ATP-binding energy-coupling subunit of the "
            "PP_2154-PP_2156 LolCDE lipoprotein-releasing ABC transporter. "
            "UniProt describes LolCDE as translocating mature outer membrane-directed "
            "lipoproteins from the inner membrane to the periplasmic chaperone LolA "
            "and forming the LolA-lipoprotein complex in an ATP-dependent manner."
        ),
        "product_text": "Full=Lipoprotein-releasing system ATP-binding protein LolD",
        "asta_text": "Protein Description:** RecName: Full=Lipoprotein-releasing system ATP-binding protein LolD",
        "function_text": "Part of the ABC transporter complex LolCDE involved in the",
        "translocation_text": "translocation of mature outer membrane-directed lipoproteins, from the",
        "formation_text": "formation of the LolA-lipoprotein complex in an ATP-dependent manner.",
        "subunit_text": "The complex is composed of two ATP-binding proteins (LolD) and",
        "location_text": "Cell inner membrane",
        "family_text": "Belongs to the ABC transporter superfamily. Lipoprotein",
        "domain_text": "InterPro; IPR011924; LolD_lipo_ATP-bd.",
        "ft_domain_text": "FT   DOMAIN          7..227",
    },
    "lolE": {
        "kind": "permease",
        "accession": "Q88KY3",
        "description": (
            "lolE encodes the second multi-pass membrane permease component of the "
            "PP_2154-PP_2156 LolCDE lipoprotein-releasing ABC transporter. UniProt "
            "names the protein as a lipoprotein releasing-system permease, places it "
            "in the cell membrane, and assigns the LolC/E domain family."
        ),
        "product_text": "Full=Lipoprotein releasing system, permease protein",
        "asta_text": "Protein Description:** SubName: Full=Lipoprotein releasing system, permease protein",
        "location_text": "Cell membrane",
        "family_text": "Belongs to the ABC-4 integral membrane protein family.",
        "domain_text": "InterPro; IPR011925; LolCE_TM.",
    },
}


def permease_review(gene: str, cfg: dict, term_id: str, label: str) -> dict:
    product = support_uniprot(gene, cfg["product_text"])
    domain = support_uniprot(gene, cfg["domain_text"])
    asta = support_asta(gene, cfg["asta_text"])
    mapping = {
        "GO:0005886": (
            "Plasma membrane localization is appropriate for this bacterial LolCDE membrane component.",
            "ACCEPT",
            "UniProt places the protein in the cell membrane as a multi-pass membrane protein.",
            None,
            [support_uniprot(gene, cfg["location_text"])],
        ),
        "GO:0016020": (
            "Membrane localization is true but less informative than plasma membrane for this inner-membrane LolCDE component.",
            "MARK_AS_OVER_ANNOTATED",
            "The record also has a plasma-membrane annotation and UniProt places the protein in the cell membrane.",
            None,
            [support_uniprot(gene, cfg["location_text"])],
        ),
        "GO:0042953": (
            "Lipoprotein transport is a correct process annotation for this LolCDE permease component.",
            "ACCEPT",
            "The LolC/E domain and local LolCDE context support a role in lipoprotein transport.",
            None,
            [product, domain, asta],
        ),
        "GO:0044874": (
            "Lipoprotein localization to outer membrane is an appropriate process for this LolCDE component.",
            "ACCEPT",
            "The LolCDE system releases mature outer membrane-directed lipoproteins for transfer to LolA.",
            None,
            [product, domain, asta],
        ),
        "GO:0098797": (
            "Plasma membrane protein complex membership is appropriate for this LolCDE permease component.",
            "ACCEPT",
            "LolC and LolE are the transmembrane components of the plasma-membrane LolCDE lipoprotein-release complex.",
            None,
            [product, support_uniprot(gene, cfg["family_text"]), domain],
        ),
    }
    summary, action, reason, proposed, support = mapping[term_id]
    return review(gene, term_id, label, summary, action, reason, proposed=proposed, extra_support=support)


def atpase_review(gene: str, cfg: dict, term_id: str, label: str) -> dict:
    product = support_uniprot(gene, cfg["product_text"])
    function = support_uniprot(gene, cfg["function_text"])
    translocation = support_uniprot(gene, cfg["translocation_text"])
    formation = support_uniprot(gene, cfg["formation_text"])
    domain = support_uniprot(gene, cfg["domain_text"])
    asta = support_asta(gene, cfg["asta_text"])
    mapping = {
        "GO:0005524": (
            "ATP binding is correct for the LolD ABC ATP-binding component.",
            "ACCEPT",
            "Reviewed UniProt names LolD as the ATP-binding protein of the LolCDE complex.",
            None,
            [product, domain],
        ),
        "GO:0005886": (
            "Plasma membrane localization is appropriate for this inner-membrane-associated LolD ATPase.",
            "ACCEPT",
            "UniProt places LolD at the cell inner membrane as a peripheral membrane protein.",
            None,
            [support_uniprot(gene, cfg["location_text"])],
        ),
        "GO:0016020": (
            "Membrane localization is true but less informative than plasma membrane for this membrane-associated LolD ATPase.",
            "MARK_AS_OVER_ANNOTATED",
            "The record also has a plasma-membrane annotation and UniProt places LolD at the cell inner membrane.",
            None,
            [support_uniprot(gene, cfg["location_text"])],
        ),
        "GO:0016887": (
            "ATP hydrolysis activity is the correct core mechanistic activity for LolD.",
            "ACCEPT",
            "LolD energizes LolCDE-dependent formation of the LolA-lipoprotein complex in an ATP-dependent manner.",
            None,
            [product, formation, domain, asta],
        ),
        "GO:0022857": (
            "Generic transmembrane transporter activity is correct but less informative than the ATPase-coupled transporter context.",
            "MODIFY",
            "LolD is the ATP-binding subunit of the LolCDE ABC transporter complex.",
            [ATPASE_COUPLED_TRANSPORTER],
            [function, product, domain],
        ),
        "GO:0044873": (
            "Lipoprotein localization to membrane is true but less specific than outer-membrane lipoprotein localization for LolCDE.",
            "MODIFY",
            "Reviewed UniProt describes translocation of mature outer membrane-directed lipoproteins.",
            [LIPOPROTEIN_LOCALIZATION_OUTER_MEMBRANE],
            [function, translocation],
        ),
        "GO:0044874": (
            "Lipoprotein localization to outer membrane is the correct core process for LolD.",
            "ACCEPT",
            "LolD is part of the LolCDE complex that translocates mature outer membrane-directed lipoproteins to LolA.",
            None,
            [function, translocation, formation],
        ),
        "GO:0055085": (
            "Transmembrane transport is correct but too broad for the LolCDE lipoprotein-release system.",
            "MODIFY",
            "Lipoprotein transport/localization better captures the transported substrate class and pathway role.",
            [LIPOPROTEIN_TRANSPORT],
            [function, translocation, formation],
        ),
        "GO:0089705": (
            "Protein localization to outer membrane is correct but less specific than lipoprotein localization to outer membrane.",
            "MODIFY",
            "LolCDE handles mature outer membrane-directed lipoproteins, not arbitrary proteins.",
            [LIPOPROTEIN_LOCALIZATION_OUTER_MEMBRANE],
            [function, translocation],
        ),
    }
    summary, action, reason, proposed, support = mapping[term_id]
    return review(gene, term_id, label, summary, action, reason, proposed=proposed, extra_support=support)


def add_new_annotations(doc: dict, gene: str, cfg: dict) -> None:
    if cfg["kind"] != "atpase":
        return
    existing_ids = {ann["term"]["id"] for ann in doc.get("existing_annotations", [])}
    if PLASMA_MEMBRANE_PROTEIN_COMPLEX["id"] in existing_ids:
        return
    doc.setdefault("existing_annotations", []).append(
        new_annotation(
            PLASMA_MEMBRANE_PROTEIN_COMPLEX,
            "part_of",
            gene,
            "Plasma membrane protein complex membership is a useful missing annotation for LolD.",
            "Reviewed UniProt states that LolD is part of the LolCDE ABC transporter complex.",
            [
                support_uniprot(gene, cfg["function_text"]),
                support_uniprot(gene, cfg["subunit_text"]),
                support_asta(gene, cfg["asta_text"]),
            ],
        )
    )


def build_core_function(gene: str, cfg: dict) -> dict:
    if cfg["kind"] == "permease":
        return {
            "description": "Multi-pass LolCDE permease component for lipoprotein transport and outer-membrane lipoprotein localization.",
            "directly_involved_in": [
                deepcopy(LIPOPROTEIN_TRANSPORT),
                deepcopy(LIPOPROTEIN_LOCALIZATION_OUTER_MEMBRANE),
            ],
            "locations": [deepcopy(PLASMA_MEMBRANE)],
            "in_complex": deepcopy(PLASMA_MEMBRANE_PROTEIN_COMPLEX),
            "supported_by": [
                support_goa(gene, "GO:0042953", "lipoprotein transport"),
                support_goa(gene, "GO:0044874", "lipoprotein localization to outer membrane"),
                support_goa(gene, "GO:0098797", "plasma membrane protein complex"),
                support_uniprot(gene, cfg["product_text"]),
                support_uniprot(gene, cfg["domain_text"]),
                support_asta(gene, cfg["asta_text"]),
            ],
        }
    return {
        "description": "ATP-binding energy-coupling subunit of the LolCDE lipoprotein-release system.",
        "molecular_function": deepcopy(ATP_HYDROLYSIS),
        "directly_involved_in": [deepcopy(LIPOPROTEIN_LOCALIZATION_OUTER_MEMBRANE)],
        "locations": [deepcopy(PLASMA_MEMBRANE)],
        "in_complex": deepcopy(PLASMA_MEMBRANE_PROTEIN_COMPLEX),
        "supported_by": [
            support_goa(gene, "GO:0016887", "ATP hydrolysis activity"),
            support_goa(gene, "GO:0044874", "lipoprotein localization to outer membrane"),
            support_uniprot(gene, cfg["function_text"]),
            support_uniprot(gene, cfg["translocation_text"]),
            support_uniprot(gene, cfg["formation_text"]),
            support_asta(gene, cfg["asta_text"]),
        ],
    }


def curate_gene(gene: str) -> None:
    cfg = GENES[gene]
    path = Path("genes") / SPECIES / gene / f"{gene}-ai-review.yaml"
    doc = yaml.safe_load(path.read_text())
    doc["status"] = "COMPLETE"
    doc["description"] = cfg["description"]
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
        if cfg["kind"] == "permease":
            ann["review"] = permease_review(gene, cfg, term["id"], term["label"])
        else:
            ann["review"] = atpase_review(gene, cfg, term["id"], term["label"])

    add_new_annotations(doc, gene, cfg)
    ensure_reference(doc, goa_ref(gene), f"QuickGO GOA annotations for {gene}")
    ensure_reference(
        doc,
        uniprot_ref(gene),
        f"UniProtKB entry for {gene} ({cfg['accession']})",
        cfg["product_text"],
    )
    ensure_reference(
        doc,
        asta_ref(gene),
        f"Asta retrieval report for {gene} ({cfg['accession']})",
        cfg["asta_text"],
    )
    doc["core_functions"] = [build_core_function(gene, cfg)]
    doc["proposed_new_terms"] = []
    doc["suggested_questions"] = [
        {
            "question": (
                "Does the PP_2154-PP_2156 LolCDE system have the canonical "
                "LolC/LolE/LolD stoichiometry and substrate range in P. putida KT2440?"
            )
        }
    ]
    doc["suggested_experiments"] = [
        {
            "description": (
                "Test LolCDE dependence for outer-membrane lipoprotein localization using "
                "conditional lolC, lolD, or lolE depletion and lipoprotein localization assays."
            ),
            "experiment_type": "conditional essential-gene depletion with lipoprotein localization assay",
        }
    ]
    path.write_text(yaml.safe_dump(doc, sort_keys=False, allow_unicode=False))
    print(f"curated {path}")


def main() -> None:
    for gene in GENES:
        curate_gene(gene)


if __name__ == "__main__":
    main()
