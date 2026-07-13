#!/usr/bin/env python3
"""First-pass curation for the ppu02010 C18 Dpp dipeptide ABC importer."""

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
    replacements: list[dict] | None = None,
) -> dict:
    supported_by = [support_goa(gene, term_id, label)]
    if uniprot_text:
        supported_by.append(support_uniprot(gene, uniprot_text))
    if asta_text:
        supported_by.append(support_asta(gene, asta_text))
    obj = {
        "summary": summary,
        "action": action,
        "reason": reason,
        "supported_by": supported_by,
    }
    if replacements:
        obj["proposed_replacement_terms"] = deepcopy(replacements)
    return obj


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


ATP_BINDING = {"id": "GO:0005524", "label": "ATP binding"}
ATP_HYDROLYSIS = {"id": "GO:0016887", "label": "ATP hydrolysis activity"}
PLASMA_MEMBRANE = {"id": "GO:0005886", "label": "plasma membrane"}
MEMBRANE = {"id": "GO:0016020", "label": "membrane"}
OUTER_MEMBRANE_BOUNDED_PERIPLASM = {
    "id": "GO:0030288",
    "label": "outer membrane-bounded periplasmic space",
}
PEPTIDE_TRANSPORT = {"id": "GO:0015833", "label": "peptide transport"}
DIPEPTIDE_TRANSPORT = {"id": "GO:0042938", "label": "dipeptide transport"}
DIPEPTIDE_TRANSMEMBRANE_TRANSPORT = {
    "id": "GO:0035442",
    "label": "dipeptide transmembrane transport",
}
DIPEPTIDE_TRANSPORTER_ACTIVITY = {
    "id": "GO:0071916",
    "label": "dipeptide transmembrane transporter activity",
}
PEPTIDE_TRANSPORTER_ACTIVITY = {
    "id": "GO:1904680",
    "label": "peptide transmembrane transporter activity",
}
ABC_COMPLEX = {"id": "GO:0043190", "label": "ATP-binding cassette (ABC) transporter complex"}


ATPASES = {
    "dppF": {
        "accession": "Q88PH2",
        "symbol": "dppF",
        "product": "Full=ABC-type dipeptide transporter",
        "asta": "Protein Description:** RecName: Full=ABC-type dipeptide transporter",
        "description": (
            "DppF is an ABC ATP-binding subunit of the predicted DppABCDF dipeptide uptake system. "
            "It contains an ABC transporter ATP-binding domain and likely supplies ATP hydrolysis energy "
            "for dipeptide import together with DppD, DppB/DppC permeases, and one or more DppA-family "
            "periplasmic binding proteins."
        ),
    },
    "dppD": {
        "accession": "Q88PH1",
        "symbol": "dppD",
        "product": "Full=ABC-type dipeptide transporter",
        "asta": "Protein Description:** RecName: Full=ABC-type dipeptide transporter",
        "description": (
            "DppD is an ABC ATP-binding subunit of the predicted DppABCDF dipeptide uptake system. "
            "It belongs to the ABC transporter superfamily, contains ABC ATP-binding domains, and likely "
            "works with DppF as the energy-coupling pair for the DppB/DppC dipeptide permease."
        ),
    },
}


PERMEASES = {
    "dppC": {
        "accession": "Q88PH0",
        "symbol": "dppC",
        "product": "Full=Dipeptide ABC transporter-putative membrane subunit",
        "asta": "Protein Description:** SubName: Full=Dipeptide ABC transporter-putative membrane subunit",
        "description": (
            "DppC is a predicted multi-pass membrane permease subunit of the DppABCDF dipeptide ABC importer. "
            "It has MetI-like binding-protein-dependent transporter domains and pairs with DppB, DppD/DppF, "
            "and DppA-family periplasmic binding proteins for dipeptide uptake."
        ),
    },
    "dppB": {
        "accession": "Q88PG9",
        "symbol": "dppB",
        "product": "Full=Dipeptide ABC transporter-putative membrane subunit",
        "asta": "Protein Description:** SubName: Full=Dipeptide ABC transporter-putative membrane subunit",
        "description": (
            "DppB is a predicted multi-pass membrane permease subunit of the DppABCDF dipeptide ABC importer. "
            "It contains MetI-like binding-protein-dependent transporter domains and likely forms the membrane "
            "translocation path with DppC."
        ),
    },
}


BINDING_PROTEINS = {
    "dppA-I": {
        "accession": "Q88PG8",
        "symbol": "dppA-I",
        "product": "Full=Dipeptide ABC transporter-periplasmic binding protein",
        "asta": "Protein Description:** SubName: Full=Dipeptide ABC transporter-periplasmic binding protein",
        "signal": "SIGNAL          1..36",
        "description": (
            "DppA-I is a signal-peptide-bearing SBP_5-family periplasmic binding component of the predicted "
            "DppABCDF dipeptide ABC importer. It likely contributes substrate capture for dipeptide uptake, "
            "one of several DppA-family binding proteins encoded near the Dpp permease and ATPase subunits."
        ),
    },
    "dppA-II": {
        "accession": "Q88PG6",
        "symbol": "dppA-II",
        "product": "Full=Dipeptide ABC transporter-periplasmic binding protein",
        "asta": "Protein Description:** SubName: Full=Dipeptide ABC transporter-periplasmic binding protein",
        "signal": "SIGNAL          1..24",
        "description": (
            "DppA-II is a signal-peptide-bearing SBP_5-family periplasmic binding component associated with "
            "the predicted DppABCDF dipeptide ABC importer. It likely contributes substrate recognition for "
            "dipeptide uptake, with exact ligand preference unresolved."
        ),
    },
    "dppA-III": {
        "accession": "Q88PG5",
        "symbol": "dppA-III",
        "product": "Full=Dipeptide ABC transporter-periplasmic binding protein",
        "asta": "Protein Description:** SubName: Full=Dipeptide ABC transporter-periplasmic binding protein",
        "signal": "SIGNAL          1..24",
        "description": (
            "DppA-III is a signal-peptide-bearing SBP_5-family periplasmic binding component associated with "
            "the predicted DppABCDF dipeptide ABC importer. It likely contributes substrate recognition for "
            "dipeptide uptake, with exact ligand preference unresolved."
        ),
    },
}


def curate_atpase(gene: str, cfg: dict) -> None:
    path = Path("genes") / SPECIES / gene / f"{gene}-ai-review.yaml"
    doc = yaml.safe_load(path.read_text())
    doc["gene_symbol"] = cfg["symbol"]
    doc["status"] = "COMPLETE"
    doc["description"] = cfg["description"]

    ensure_reference(doc, goa_ref(gene), f"QuickGO GOA annotations for {gene}")
    ensure_reference(doc, uniprot_ref(gene), f"UniProtKB entry for {gene} ({cfg['accession']})", cfg["product"])
    ensure_reference(doc, asta_ref(gene), f"Asta retrieval report for {gene} ({cfg['accession']})", cfg["asta"])

    doc["existing_annotations"] = [
        ann for ann in doc.get("existing_annotations", []) if ann.get("review", {}).get("action") != "NEW"
    ]

    reviews = {
        "GO:0000166": (
            "Generic nucleotide binding is over-broad for this ABC ATP-binding subunit.",
            "MARK_AS_OVER_ANNOTATED",
            "ATP binding and ATP hydrolysis in an ABC transporter complex are more informative than generic nucleotide binding.",
            "ABC transporter",
            None,
        ),
        "GO:0005524": (
            "ATP binding is appropriate for this ABC ATP-binding subunit, but ATP hydrolysis/energy coupling is the more informative core function.",
            "KEEP_AS_NON_CORE",
            "DppF/DppD contain ABC ATP-binding domains and supply ATP-dependent energy coupling to the Dpp importer.",
            "ABC transporter",
            None,
        ),
        "GO:0005886": (
            "Plasma membrane localization is appropriate for this inner-membrane-associated ABC transporter ATP-binding subunit.",
            "ACCEPT",
            "UniProt places the DppABCDF ATP-binding subunit at the cell inner membrane.",
            "Cell inner membrane",
            None,
        ),
        "GO:0015833": (
            "Peptide transport is true but broad for this DppABCDF energy-coupling subunit.",
            "MODIFY",
            "The product name and DppABCDF UniProt function support the more specific dipeptide transmembrane transport process.",
            "Part of the ABC transporter DppABCDF involved in the uptake",
            [DIPEPTIDE_TRANSMEMBRANE_TRANSPORT],
        ),
        "GO:0016887": (
            "ATP hydrolysis activity is appropriate for this ABC ATP-binding energy-coupling subunit.",
            "ACCEPT",
            "The ABC transporter ATP-binding domain and EC assignment support ATP hydrolysis by this energy-coupling subunit.",
            "ABC transporter",
            None,
        ),
        "GO:0055085": (
            "Transmembrane transport is correct only as broad system context and is less precise than dipeptide transmembrane transport.",
            "MARK_AS_OVER_ANNOTATED",
            "The DppABCDF system is predicted for dipeptide uptake; the ATPase does not itself form the membrane channel.",
            "Part of the ABC transporter DppABCDF involved in the uptake",
            None,
        ),
    }

    for ann in doc.get("existing_annotations", []):
        term_id = ann["term"]["id"]
        summary, action, reason, uniprot_text, replacements = reviews[term_id]
        ann["review"] = review(
            gene,
            term_id,
            ann["term"]["label"],
            summary,
            action,
            reason,
            uniprot_text=uniprot_text,
            asta_text=cfg["asta"],
            replacements=replacements,
        )

    doc["existing_annotations"].extend(
        [
            new_annotation(
                DIPEPTIDE_TRANSMEMBRANE_TRANSPORT,
                "involved_in",
                gene,
                f"{gene} should be represented in dipeptide transmembrane transport.",
                "UniProt describes the local DppABCDF transporter as involved in dipeptide uptake.",
                [
                    support_uniprot(gene, "Part of the ABC transporter DppABCDF involved in the uptake"),
                    support_asta(gene, cfg["asta"]),
                ],
            ),
            new_annotation(
                ABC_COMPLEX,
                "part_of",
                gene,
                f"{gene} should be represented as part of the DppABCDF ABC transporter complex.",
                "The protein is an ABC ATP-binding subunit of the DppABCDF transporter.",
                [
                    support_uniprot(gene, cfg["product"]),
                    support_uniprot(gene, "ABC transporter"),
                ],
            ),
        ]
    )

    doc["core_functions"] = [
        {
            "description": f"ATP-binding energy-coupling subunit of the DppABCDF dipeptide ABC importer.",
            "molecular_function": ATP_HYDROLYSIS,
            "directly_involved_in": [DIPEPTIDE_TRANSMEMBRANE_TRANSPORT],
            "locations": [PLASMA_MEMBRANE],
            "in_complex": ABC_COMPLEX,
            "supported_by": [
                support_goa(gene, "GO:0016887", "ATP hydrolysis activity"),
                support_uniprot(gene, "Part of the ABC transporter DppABCDF involved in the uptake"),
                support_asta(gene, cfg["asta"]),
            ],
        }
    ]
    doc["proposed_new_terms"] = []
    doc["suggested_questions"] = [
        {
            "question": "Which of the adjacent DppA-family binding proteins supplies the primary substrate specificity for the DppB/DppC/DppD/DppF dipeptide importer?"
        }
    ]
    doc["suggested_experiments"] = [
        {
            "description": "Measure dipeptide uptake and growth phenotypes for dppD/dppF ATPase mutants and paired dppA binding-protein mutants with representative dipeptides and oligopeptides.",
            "experiment_type": "targeted dipeptide transporter mutant uptake/growth assay",
        }
    ]
    path.write_text(yaml.safe_dump(doc, sort_keys=False, width=1000))
    print(f"curated {path}")


def curate_permease(gene: str, cfg: dict) -> None:
    path = Path("genes") / SPECIES / gene / f"{gene}-ai-review.yaml"
    doc = yaml.safe_load(path.read_text())
    doc["gene_symbol"] = cfg["symbol"]
    doc["status"] = "COMPLETE"
    doc["description"] = cfg["description"]

    ensure_reference(doc, goa_ref(gene), f"QuickGO GOA annotations for {gene}")
    ensure_reference(doc, uniprot_ref(gene), f"UniProtKB entry for {gene} ({cfg['accession']})", cfg["product"])
    ensure_reference(doc, asta_ref(gene), f"Asta retrieval report for {gene} ({cfg['accession']})", cfg["asta"])

    doc["existing_annotations"] = [
        ann for ann in doc.get("existing_annotations", []) if ann.get("review", {}).get("action") != "NEW"
    ]

    reviews = {
        "GO:0005886": (
            "Plasma membrane localization is appropriate for this multi-pass bacterial inner-membrane permease.",
            "ACCEPT",
            "UniProt predicts a cell-membrane multi-pass transporter subunit.",
            "Cell membrane",
        ),
        "GO:0016020": (
            "Membrane localization is correct but less specific than plasma membrane for this bacterial inner-membrane permease.",
            "MARK_AS_OVER_ANNOTATED",
            "The plasma membrane annotation is the more informative retained location.",
            "Cell membrane",
        ),
        "GO:0035442": (
            "Dipeptide transmembrane transport is appropriate process context for this Dpp permease.",
            "ACCEPT",
            "The product name identifies the protein as a dipeptide ABC transporter membrane subunit.",
            cfg["product"],
        ),
        "GO:0043190": (
            "ABC transporter complex membership is appropriate for this Dpp permease.",
            "ACCEPT",
            "The MetI-like binding-protein-dependent transporter domain supports ABC transporter complex membership.",
            "MetI-like",
        ),
        "GO:0055085": (
            "Transmembrane transport is true but broad relative to dipeptide transmembrane transport.",
            "MARK_AS_OVER_ANNOTATED",
            "GO:0035442 captures the substrate-specific transport process.",
            cfg["product"],
        ),
        "GO:0071916": (
            "Dipeptide transmembrane transporter activity is appropriate for this permease component of the DppABCDF importer.",
            "ACCEPT",
            "The Dpp permease contributes the membrane translocation component of the dipeptide ABC transporter.",
            cfg["product"],
        ),
    }

    for ann in doc.get("existing_annotations", []):
        term_id = ann["term"]["id"]
        summary, action, reason, uniprot_text = reviews[term_id]
        ann["review"] = review(
            gene,
            term_id,
            ann["term"]["label"],
            summary,
            action,
            reason,
            uniprot_text=uniprot_text,
            asta_text=cfg["asta"],
        )

    doc["core_functions"] = [
        {
            "description": "Membrane permease component of the DppABCDF dipeptide ABC importer.",
            "contributes_to_molecular_function": DIPEPTIDE_TRANSPORTER_ACTIVITY,
            "directly_involved_in": [DIPEPTIDE_TRANSMEMBRANE_TRANSPORT],
            "locations": [PLASMA_MEMBRANE],
            "in_complex": ABC_COMPLEX,
            "supported_by": [
                support_goa(gene, "GO:0035442", "dipeptide transmembrane transport"),
                support_uniprot(gene, cfg["product"]),
                support_uniprot(gene, "MetI-like"),
                support_asta(gene, cfg["asta"]),
            ],
        }
    ]
    doc["proposed_new_terms"] = []
    doc["suggested_questions"] = [
        {
            "question": "What is the substrate range of the DppB/DppC permease across dipeptides and longer oligopeptides in KT2440?"
        }
    ]
    doc["suggested_experiments"] = [
        {
            "description": "Measure uptake and growth phenotypes for dppB/dppC permease mutants with representative dipeptides, tripeptides, and amino-acid controls.",
            "experiment_type": "targeted peptide transporter mutant uptake/growth assay",
        }
    ]
    path.write_text(yaml.safe_dump(doc, sort_keys=False, width=1000))
    print(f"curated {path}")


def curate_binding_protein(gene: str, cfg: dict) -> None:
    path = Path("genes") / SPECIES / gene / f"{gene}-ai-review.yaml"
    doc = yaml.safe_load(path.read_text())
    doc["gene_symbol"] = cfg["symbol"]
    doc["status"] = "COMPLETE"
    doc["description"] = cfg["description"]

    ensure_reference(doc, goa_ref(gene), f"QuickGO GOA annotations for {gene}")
    ensure_reference(doc, uniprot_ref(gene), f"UniProtKB entry for {gene} ({cfg['accession']})", cfg["product"])
    ensure_reference(doc, asta_ref(gene), f"Asta retrieval report for {gene} ({cfg['accession']})", cfg["asta"])

    doc["existing_annotations"] = [
        ann for ann in doc.get("existing_annotations", []) if ann.get("review", {}).get("action") != "NEW"
    ]

    reviews = {
        "GO:0015833": (
            "Peptide transport is broad but acceptable process context for this DppA-family substrate-binding component.",
            "KEEP_AS_NON_CORE",
            "The more specific dipeptide transport annotation captures the likely primary process.",
            cfg["product"],
            None,
        ),
        "GO:0030288": (
            "Outer membrane-bounded periplasmic space localization is appropriate for this signal-peptide-bearing substrate-binding protein.",
            "ACCEPT",
            "The protein has an N-terminal signal peptide and SBP_5 periplasmic-binding-protein domain architecture.",
            cfg["signal"],
            None,
        ),
        "GO:0042938": (
            "Dipeptide transport is appropriate process context for this DppA-family binding component.",
            "ACCEPT",
            "The product name and SBP_5 dipeptide-binding family support a dipeptide transport role.",
            cfg["product"],
            None,
        ),
        "GO:0043190": (
            "ABC transporter complex membership is appropriate for this substrate-binding component.",
            "ACCEPT",
            "The protein is a periplasmic binding component of a local Dpp ABC transporter locus.",
            "Dipeptide ABC transporter, substrate-binding protein",
            None,
        ),
        "GO:0055085": (
            "Transmembrane transport is correct only as transporter-system context and is less precise than dipeptide transport.",
            "MARK_AS_OVER_ANNOTATED",
            "This protein is a periplasmic substrate-binding component; DppB/DppC provide the membrane channel.",
            cfg["product"],
            None,
        ),
        "GO:1904680": (
            "Peptide transmembrane transporter activity is broad and should be represented as contribution to the dipeptide ABC transporter complex.",
            "MODIFY",
            "The protein is a periplasmic substrate-binding component and should not be treated as an independent membrane transporter.",
            "Dipeptide ABC transporter, substrate-binding protein",
            [DIPEPTIDE_TRANSPORTER_ACTIVITY],
        ),
    }

    for ann in doc.get("existing_annotations", []):
        term_id = ann["term"]["id"]
        summary, action, reason, uniprot_text, replacements = reviews[term_id]
        ann["review"] = review(
            gene,
            term_id,
            ann["term"]["label"],
            summary,
            action,
            reason,
            uniprot_text=uniprot_text,
            asta_text=cfg["asta"],
            replacements=replacements,
        )

    doc["existing_annotations"].append(
        new_annotation(
            DIPEPTIDE_TRANSPORTER_ACTIVITY,
            "contributes_to",
            gene,
            f"{gene} should be represented as contributing substrate recognition to dipeptide ABC transporter activity.",
            "The protein is a signal-peptide-bearing SBP_5 DppA-family binding component, not the membrane channel itself.",
            [
                support_uniprot(gene, cfg["product"]),
                support_uniprot(gene, cfg["signal"]),
                support_uniprot(gene, "Dipeptide ABC transporter, substrate-binding protein"),
                support_asta(gene, cfg["asta"]),
            ],
        )
    )

    doc["core_functions"] = [
        {
            "description": "Periplasmic substrate-binding component contributing substrate capture to the DppABCDF dipeptide ABC importer.",
            "contributes_to_molecular_function": DIPEPTIDE_TRANSPORTER_ACTIVITY,
            "directly_involved_in": [DIPEPTIDE_TRANSPORT],
            "locations": [OUTER_MEMBRANE_BOUNDED_PERIPLASM],
            "in_complex": ABC_COMPLEX,
            "supported_by": [
                support_goa(gene, "GO:0042938", "dipeptide transport"),
                support_uniprot(gene, cfg["product"]),
                support_uniprot(gene, cfg["signal"]),
                support_asta(gene, cfg["asta"]),
            ],
        }
    ]
    doc["proposed_new_terms"] = []
    doc["suggested_questions"] = [
        {
            "question": f"What ligands does {gene} bind, and how does its specificity differ from the adjacent DppA-family binding proteins?"
        }
    ]
    doc["suggested_experiments"] = [
        {
            "description": f"Measure purified {gene} ligand binding and mutant uptake/growth phenotypes across representative dipeptides and longer oligopeptides.",
            "experiment_type": "targeted periplasmic binding protein ligand-binding and transporter uptake assay",
        }
    ]
    path.write_text(yaml.safe_dump(doc, sort_keys=False, width=1000))
    print(f"curated {path}")


def main() -> None:
    for gene, cfg in ATPASES.items():
        curate_atpase(gene, cfg)
    for gene, cfg in PERMEASES.items():
        curate_permease(gene, cfg)
    for gene, cfg in BINDING_PROTEINS.items():
        curate_binding_protein(gene, cfg)


if __name__ == "__main__":
    main()
