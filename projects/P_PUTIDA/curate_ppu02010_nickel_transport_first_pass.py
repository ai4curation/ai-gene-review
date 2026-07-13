#!/usr/bin/env python3
"""First-pass curation for the ppu02010 NikABCDE nickel ABC transporter block."""

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
    extra_support: list[dict] | None = None,
) -> dict:
    supported_by = [support_goa(gene, term_id, label)]
    if asta_text:
        supported_by.append(support_asta(gene, asta_text))
    if extra_support:
        supported_by.extend(extra_support)
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
    term: dict,
    qualifier: str,
    original_reference_id: str,
    summary: str,
    reason: str,
    supported_by: list[dict],
) -> dict:
    return {
        "term": term,
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


NICKEL_BINDING = {"id": "GO:0016151", "label": "nickel cation binding"}
NICKEL_TRANSPORT = {"id": "GO:0015675", "label": "nickel cation transport"}
NICKEL_TRANSMEMBRANE_TRANSPORT = {
    "id": "GO:0035444",
    "label": "nickel cation transmembrane transport",
}
NICKEL_TRANSMEMBRANE_TRANSPORTER = {
    "id": "GO:0015099",
    "label": "nickel cation transmembrane transporter activity",
}
ABC_NICKEL_TRANSPORTER = {"id": "GO:0015413", "label": "ABC-type nickel transporter activity"}
ABC_COMPLEX = {"id": "GO:0043190", "label": "ATP-binding cassette (ABC) transporter complex"}
PLASMA_MEMBRANE = {"id": "GO:0005886", "label": "plasma membrane"}
PERIPLASM_OM = {"id": "GO:0030288", "label": "outer membrane-bounded periplasmic space"}


CONFIG = {
    "nikA": {
        "symbol": "nikA",
        "description": (
            "nikA (PP_3342) encodes the signal-peptide-bearing periplasmic substrate-binding "
            "component of a predicted NikABCDE nickel ABC importer. Its nickel/peptide-binding "
            "solute-binding-protein domains and local nikABCDE locus support nickel capture for "
            "delivery to the NikB/NikC permease and NikD/NikE ATPase components."
        ),
        "asta_text": "Protein Description:** SubName: Full=Nickel ABC transporter periplasmic binding protein",
        "uniprot_text": "Full=Nickel ABC transporter periplasmic binding protein",
        "reviews": {
            "GO:0015675": (
                "Nickel cation transport is appropriate process context for NikA.",
                "ACCEPT",
                "NikA is the periplasmic binding component in the local NikABCDE nickel ABC importer and carries nickel/peptide-binding solute-binding-protein domains.",
            ),
            "GO:0015833": (
                "Peptide transport is a likely family-level spillover and should not be treated as the core function for this NikA protein.",
                "MARK_AS_OVER_ANNOTATED",
                "The product name, nickel-binding InterPro annotation, and adjacent nikBCDE genes support a nickel-import system; peptide transport remains at most weak family context.",
            ),
            "GO:0016151": (
                "Nickel cation binding is the direct molecular function expected for this periplasmic substrate-binding component.",
                "ACCEPT",
                "NikA is named as a nickel ABC transporter periplasmic binding protein and carries nickel-binding solute-binding-protein domains.",
            ),
            "GO:0020037": (
                "Heme binding appears to be an InterPro2GO spillover from the broad CntA-like family and is not supported for this NikA nickel-import component.",
                "REMOVE",
                "The local NikABCDE locus, nickel-binding annotation, and product name support nickel substrate binding rather than heme binding.",
            ),
            "GO:0030288": (
                "Outer membrane-bounded periplasmic space is appropriate for this signal-peptide-bearing Gram-negative solute-binding protein.",
                "ACCEPT",
                "UniProt predicts an N-terminal signal peptide and mature chain for NikA, consistent with a periplasmic substrate-binding component.",
            ),
            "GO:0043190": (
                "ABC transporter complex membership is appropriate for the NikA binding component.",
                "ACCEPT",
                "NikA is the solute-binding component of the local NikABCDE ABC import locus.",
            ),
            "GO:0055085": (
                "Transmembrane transport is true only as pathway context and is less precise than nickel cation transport for this binding component.",
                "MARK_AS_OVER_ANNOTATED",
                "NikA is the periplasmic substrate-binding component, while NikB/NikC form the membrane pathway.",
            ),
            "GO:1904680": (
                "Peptide transmembrane transporter activity is not supported as a core function for NikA.",
                "REMOVE",
                "This protein is a periplasmic nickel-binding component in a NikABCDE locus, not a membrane peptide transporter.",
            ),
        },
        "core": {
            "description": "Periplasmic nickel-binding component contributing substrate capture to the NikABCDE nickel ABC importer.",
            "molecular_function": NICKEL_BINDING,
            "directly_involved_in": [NICKEL_TRANSPORT],
            "locations": [PERIPLASM_OM],
            "in_complex": ABC_COMPLEX,
            "support": ("GO:0016151", "nickel cation binding"),
        },
    },
    "nikB": {
        "symbol": "nikB",
        "description": (
            "nikB (PP_3343) encodes a predicted multi-pass inner-membrane permease subunit of "
            "the NikABCDE nickel ABC importer. Its NikB-family domain and position between nikA "
            "and nikCDE support a nickel-translocation role; dipeptide transporter annotations are "
            "best treated as family spillover."
        ),
        "asta_text": "Protein Description:** SubName: Full=Nickel ABC transporter permease subunit",
        "uniprot_text": "Full=Nickel ABC transporter permease subunit",
        "reviews": {
            "GO:0005886": (
                "Plasma membrane localization is appropriate for this multi-pass inner-membrane permease.",
                "ACCEPT",
                "UniProt predicts NikB as a cell-membrane multi-pass membrane protein.",
            ),
            "GO:0015099": (
                "Nickel cation transmembrane transporter activity is the best molecular-function annotation for NikB.",
                "ACCEPT",
                "NikB carries the nickel NikB permease domain and is located in the NikABCDE nickel-import locus.",
            ),
            "GO:0016020": (
                "Membrane localization is correct but less specific than plasma membrane.",
                "MARK_AS_OVER_ANNOTATED",
                "The plasma membrane annotation is more informative for this bacterial inner-membrane permease.",
            ),
            "GO:0035442": (
                "Dipeptide transmembrane transport appears to be a TreeGrafter/GOC spillover from related peptide-import permeases.",
                "REMOVE",
                "The product name and nickel-specific NikB domain support nickel cation transmembrane transport rather than dipeptide import.",
            ),
            "GO:0035444": (
                "Nickel cation transmembrane transport is appropriate process context for NikB.",
                "ACCEPT",
                "NikB is the membrane permease subunit in a nickel ABC transporter locus.",
            ),
            "GO:0043190": (
                "ABC transporter complex membership is appropriate for NikB.",
                "ACCEPT",
                "NikB is one of the predicted membrane permease components of the NikABCDE ABC importer.",
            ),
            "GO:0055085": (
                "Transmembrane transport is true but broad relative to nickel cation transmembrane transport.",
                "MARK_AS_OVER_ANNOTATED",
                "GO:0035444 captures the substrate-specific transport process.",
            ),
            "GO:0071916": (
                "Dipeptide transmembrane transporter activity is not supported as the core function for NikB.",
                "REMOVE",
                "The local NikABCDE context and nickel-specific domain support nickel transporter activity rather than dipeptide transport.",
            ),
        },
        "core": {
            "description": "Multi-pass membrane permease component of the NikABCDE nickel ABC importer.",
            "molecular_function": NICKEL_TRANSMEMBRANE_TRANSPORTER,
            "directly_involved_in": [NICKEL_TRANSMEMBRANE_TRANSPORT],
            "locations": [PLASMA_MEMBRANE],
            "in_complex": ABC_COMPLEX,
            "support": ("GO:0015099", "nickel cation transmembrane transporter activity"),
        },
    },
    "nikC": {
        "symbol": "nikC",
        "description": (
            "nikC (PP_3344) encodes the second predicted multi-pass inner-membrane permease "
            "subunit of the NikABCDE nickel ABC importer. Its NikC-family domain and local "
            "nikABCDE context support nickel import, while peptide/dipeptide annotations reflect "
            "broader permease-family transfer."
        ),
        "asta_text": "Protein Description:** SubName: Full=Nickel ABC transporter permease subunit",
        "uniprot_text": "Full=Nickel ABC transporter permease subunit",
        "reviews": {
            "GO:0005886": (
                "Plasma membrane localization is appropriate for this multi-pass inner-membrane permease.",
                "ACCEPT",
                "UniProt predicts NikC as a cell-membrane multi-pass membrane protein.",
            ),
            "GO:0015099": (
                "Nickel cation transmembrane transporter activity is the best molecular-function annotation for NikC.",
                "ACCEPT",
                "NikC carries the nickel NikC permease domain and is located in the NikABCDE nickel-import locus.",
            ),
            "GO:0016020": (
                "Membrane localization is correct but less specific than plasma membrane.",
                "MARK_AS_OVER_ANNOTATED",
                "The plasma membrane annotation is more informative for this bacterial inner-membrane permease.",
            ),
            "GO:0035442": (
                "Dipeptide transmembrane transport appears to be a TreeGrafter/GOC spillover from related peptide-import permeases.",
                "REMOVE",
                "The product name and nickel-specific NikC domain support nickel cation transmembrane transport rather than dipeptide import.",
            ),
            "GO:0035444": (
                "Nickel cation transmembrane transport is appropriate process context for NikC.",
                "ACCEPT",
                "NikC is the membrane permease subunit in a nickel ABC transporter locus.",
            ),
            "GO:0043190": (
                "ABC transporter complex membership is appropriate for NikC.",
                "ACCEPT",
                "NikC is one of the predicted membrane permease components of the NikABCDE ABC importer.",
            ),
            "GO:0055085": (
                "Transmembrane transport is true but broad relative to nickel cation transmembrane transport.",
                "MARK_AS_OVER_ANNOTATED",
                "GO:0035444 captures the substrate-specific transport process.",
            ),
            "GO:0071916": (
                "Dipeptide transmembrane transporter activity is not supported as the core function for NikC.",
                "REMOVE",
                "The local NikABCDE context and nickel-specific domain support nickel transporter activity rather than dipeptide transport.",
            ),
        },
        "core": {
            "description": "Multi-pass membrane permease component of the NikABCDE nickel ABC importer.",
            "molecular_function": NICKEL_TRANSMEMBRANE_TRANSPORTER,
            "directly_involved_in": [NICKEL_TRANSMEMBRANE_TRANSPORT],
            "locations": [PLASMA_MEMBRANE],
            "in_complex": ABC_COMPLEX,
            "support": ("GO:0015099", "nickel cation transmembrane transporter activity"),
        },
    },
    "nikD": {
        "symbol": "nikD",
        "description": (
            "nikD (PP_3345) encodes a reviewed ATP-binding subunit of the NikABCDE nickel "
            "ABC importer. UniProt/HAMAP identifies NikD as part of the NikABCDE complex "
            "involved in nickel import and assigns EC 7.2.2.11 for ATP-driven nickel uptake."
        ),
        "asta_text": "Protein Description:** RecName: Full=Nickel import ATP-binding protein NikD",
        "uniprot_text": "Part of the ABC transporter complex NikABCDE involved in",
        "reviews": {
            "GO:0005524": (
                "ATP binding is correct for the ABC transporter nucleotide-binding subunit.",
                "ACCEPT",
                "NikD is a reviewed ABC-transporter ATP-binding protein in the nickel importer family.",
            ),
            "GO:0005886": (
                "Plasma membrane localization is appropriate for the membrane-associated ABC ATPase.",
                "ACCEPT",
                "UniProt places NikD at the cell inner membrane as a peripheral membrane protein.",
            ),
            "GO:0015413": (
                "ABC-type nickel transporter activity is the core function for NikD.",
                "ACCEPT",
                "The reviewed UniProt entry assigns EC 7.2.2.11 and describes NikD as part of the NikABCDE nickel import complex.",
            ),
            "GO:0015675": (
                "Nickel cation transport is correct process context for NikD.",
                "ACCEPT",
                "NikD is part of the NikABCDE complex involved in nickel import.",
            ),
            "GO:0016151": (
                "Nickel cation binding is likely a broad nickel-importer family annotation rather than the core activity of this ATPase subunit.",
                "MARK_AS_OVER_ANNOTATED",
                "NikD's direct role is ATP binding/hydrolysis and energy coupling for nickel import; substrate binding is primarily expected for NikA.",
            ),
            "GO:0016887": (
                "ATP hydrolysis activity is correct mechanistic context for the ABC ATPase.",
                "KEEP_AS_NON_CORE",
                "ATP hydrolysis powers nickel import, while ABC-type nickel transporter activity captures the substrate-specific complex function.",
            ),
            "GO:0035444": (
                "Nickel cation transmembrane transport is correct process context for NikD.",
                "ACCEPT",
                "The NikABCDE reaction transports Ni(2+) across the membrane using ATP hydrolysis.",
            ),
        },
        "new_annotations": [
            {
                "term": ABC_COMPLEX,
                "qualifier": "part_of",
                "summary": "ABC transporter complex membership is a useful missing annotation for NikD.",
                "reason": "The reviewed UniProt entry explicitly describes NikD as part of the NikABCDE ABC transporter complex involved in nickel import.",
                "supporting_text": "Part of the ABC transporter complex NikABCDE involved in",
            }
        ],
        "core": {
            "description": "ATP-binding energy-coupling subunit of the NikABCDE nickel ABC importer.",
            "molecular_function": ABC_NICKEL_TRANSPORTER,
            "directly_involved_in": [NICKEL_TRANSMEMBRANE_TRANSPORT],
            "locations": [PLASMA_MEMBRANE],
            "in_complex": ABC_COMPLEX,
            "support": ("GO:0015413", "ABC-type nickel transporter activity"),
        },
    },
    "nikE": {
        "symbol": "nikE",
        "description": (
            "nikE (PP_3346) encodes a reviewed ATP-binding subunit of the NikABCDE nickel "
            "ABC importer. UniProt/HAMAP identifies NikE as part of the NikABCDE complex "
            "involved in nickel import and assigns EC 7.2.2.11 for ATP-driven nickel uptake."
        ),
        "asta_text": "Protein Description:** RecName: Full=Nickel import ATP-binding protein NikE",
        "uniprot_text": "Part of the ABC transporter complex NikABCDE involved in",
        "reviews": {
            "GO:0005524": (
                "ATP binding is correct for the ABC transporter nucleotide-binding subunit.",
                "ACCEPT",
                "NikE is a reviewed ABC-transporter ATP-binding protein in the nickel importer family.",
            ),
            "GO:0005886": (
                "Plasma membrane localization is appropriate for the membrane-associated ABC ATPase.",
                "ACCEPT",
                "UniProt places NikE at the cell inner membrane as a peripheral membrane protein.",
            ),
            "GO:0015413": (
                "ABC-type nickel transporter activity is the core function for NikE.",
                "ACCEPT",
                "The reviewed UniProt entry assigns EC 7.2.2.11 and describes NikE as part of the NikABCDE nickel import complex.",
            ),
            "GO:0015675": (
                "Nickel cation transport is correct process context for NikE.",
                "ACCEPT",
                "NikE is part of the NikABCDE complex involved in nickel import.",
            ),
            "GO:0016151": (
                "Nickel cation binding is likely a broad nickel-importer family annotation rather than the core activity of this ATPase subunit.",
                "MARK_AS_OVER_ANNOTATED",
                "NikE's direct role is ATP binding/hydrolysis and energy coupling for nickel import; substrate binding is primarily expected for NikA.",
            ),
            "GO:0016887": (
                "ATP hydrolysis activity is correct mechanistic context for the ABC ATPase.",
                "KEEP_AS_NON_CORE",
                "ATP hydrolysis powers nickel import, while ABC-type nickel transporter activity captures the substrate-specific complex function.",
            ),
            "GO:0035444": (
                "Nickel cation transmembrane transport is correct process context for NikE.",
                "ACCEPT",
                "The NikABCDE reaction transports Ni(2+) across the membrane using ATP hydrolysis.",
            ),
            "GO:0055085": (
                "Transmembrane transport is true but broad relative to nickel cation transmembrane transport.",
                "MARK_AS_OVER_ANNOTATED",
                "GO:0035444 captures the substrate-specific transport process.",
            ),
        },
        "new_annotations": [
            {
                "term": ABC_COMPLEX,
                "qualifier": "part_of",
                "summary": "ABC transporter complex membership is a useful missing annotation for NikE.",
                "reason": "The reviewed UniProt entry explicitly describes NikE as part of the NikABCDE ABC transporter complex involved in nickel import.",
                "supporting_text": "Part of the ABC transporter complex NikABCDE involved in",
            }
        ],
        "core": {
            "description": "ATP-binding energy-coupling subunit of the NikABCDE nickel ABC importer.",
            "molecular_function": ABC_NICKEL_TRANSPORTER,
            "directly_involved_in": [NICKEL_TRANSMEMBRANE_TRANSPORT],
            "locations": [PLASMA_MEMBRANE],
            "in_complex": ABC_COMPLEX,
            "support": ("GO:0015413", "ABC-type nickel transporter activity"),
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
        extra_support = entry[4] if len(entry) > 4 else None
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
            "question": "What is the physiological nickel-demand context for NikABCDE in P. putida KT2440, and does this transporter also import nickel-peptide complexes?"
        }
    ]
    doc["suggested_experiments"] = [
        {
            "description": "Measure nickel uptake and nickel-dependent growth or enzyme activity in nikA/nikB/nikC/nikD/nikE mutants, with free Ni(2+) and peptide-complexed nickel supplied separately.",
            "experiment_type": "targeted transporter mutant nickel-uptake and growth/enzyme-activity assay",
        }
    ]

    path.write_text(yaml.safe_dump(doc, sort_keys=False, width=1000))
    print(f"curated {path}")


def main() -> None:
    for gene, cfg in CONFIG.items():
        curate_gene(gene, cfg)


if __name__ == "__main__":
    main()
