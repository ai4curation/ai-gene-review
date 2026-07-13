#!/usr/bin/env python3
"""First-pass curation for the ppu02010 PP_2748-PP_2753 BCAA importer."""

from __future__ import annotations

from copy import deepcopy
from pathlib import Path

import yaml


SPECIES = "PSEPK"
MODULE_PATH = Path("modules/branched_chain_amino_acid_abc_import_boundary.yaml")

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

LOCUS = "PP_2748-PP_2753"
LOCUS_DESC = "PP_2748-PP_2753 branched-chain amino-acid ABC importer"

GENES = {
    "PP_2748": {
        "accession": "Q88JA1",
        "kind": "atpase",
        "role": "branched-chain amino-acid ABC importer ATP-binding subunit",
        "description": (
            "PP_2748 encodes a predicted ATP-binding energy-coupling subunit of the adjacent "
            "PP_2748-PP_2753 branched-chain amino-acid ABC uptake system. Its ABC transporter "
            "ATP-binding and BCA ABC-transporter C-terminal domains, together with the adjacent "
            "PP_2749/PP_2750 permeases, PP_2751/PP_2752 leucine-family binding proteins, and "
            "PP_2753 second ATPase, support ATP hydrolysis-driven branched-chain amino-acid import."
        ),
        "uniprot_text": "Full=Branched-chain amino acid ABC transporter, ATP-binding protein",
        "asta_text": "Protein Description:** SubName: Full=Branched-chain amino acid ABC transporter, ATP-binding protein",
        "domain_text": "InterPro; IPR032823; BCA_ABC_TP_C.",
        "panther_text": "CONSERVED COMPONENT OF ABC TRANSPORTER FOR NATURAL AMINO ACIDS-RELATED",
        "has_membrane_goa": True,
    },
    "PP_2749": {
        "accession": "Q88JA0",
        "kind": "permease",
        "role": "branched-chain amino-acid ABC importer permease",
        "description": (
            "PP_2749 encodes a predicted multi-pass inner-membrane permease component of the "
            "PP_2748-PP_2753 branched-chain amino-acid ABC uptake system. UniProt places it in "
            "the cell inner membrane and assigns BCAA transport permease features, supporting a "
            "membrane-channel role in BCAA import."
        ),
        "uniprot_text": "Full=Branched-chain amino acid ABC transporter, permease protein",
        "asta_text": "Protein Description:** SubName: Full=Branched-chain amino acid ABC transporter, permease protein",
        "location_text": "Cell inner membrane",
        "domain_text": "InterPro; IPR052157; BCAA_transport_permease.",
        "panther_text": "BRANCHED-CHAIN AMINO ACID TRANSPORT SYSTEM PERMEASE PROTEIN LIVH",
    },
    "PP_2750": {
        "accession": "Q88J99",
        "kind": "permease",
        "role": "branched-chain amino-acid ABC importer permease",
        "description": (
            "PP_2750 encodes the second predicted multi-pass inner-membrane permease component "
            "of the PP_2748-PP_2753 branched-chain amino-acid ABC uptake system. Its LivM-like "
            "domain, high-affinity BCAA transport-system permease family assignment, and BCAA "
            "transporter GOA rows support a channel role in the same importer."
        ),
        "uniprot_text": "Full=Branched-chain amino acid ABC transporter, permease protein",
        "asta_text": "Protein Description:** SubName: Full=Branched-chain amino acid ABC transporter, permease protein",
        "location_text": "Cell inner membrane",
        "domain_text": "InterPro; IPR043428; LivM-like.",
        "panther_text": "HIGH-AFFINITY BRANCHED-CHAIN AMINO ACID TRANSPORT SYSTEM PERMEASE",
    },
    "PP_2751": {
        "accession": "Q88J98",
        "kind": "binding",
        "role": "leucine-family branched-chain amino-acid substrate-binding component",
        "description": (
            "PP_2751 encodes a signal-peptide-bearing leucine-binding protein family member "
            "within the PP_2748-PP_2753 ABC transporter locus. Its Leu-binding and periplasmic "
            "binding-protein domains support a substrate-recognition role in the predicted "
            "branched-chain amino-acid ABC uptake system."
        ),
        "uniprot_text": "Full=Leucine-binding protein domain-containing protein",
        "asta_text": "Protein Description:** RecName: Full=Leucine-binding protein domain-containing protein",
        "family_text": "Belongs to the leucine-binding protein family.",
        "domain_text": "InterPro; IPR028081; Leu-bd.",
        "periplasmic_domain_text": "InterPro; IPR028082; Peripla_BP_I.",
        "signal_text": "FT   SIGNAL          1..28",
    },
    "PP_2752": {
        "accession": "Q88J97",
        "kind": "binding",
        "role": "second leucine-family branched-chain amino-acid substrate-binding component",
        "description": (
            "PP_2752 encodes a second signal-peptide-bearing leucine-binding protein family member "
            "within the PP_2748-PP_2753 ABC transporter locus. Its Leu-binding and periplasmic "
            "binding-protein domains support a substrate-recognition role, with possible redundancy "
            "or specialization relative to the adjacent PP_2751 binding protein."
        ),
        "uniprot_text": "Full=Leucine-binding protein domain-containing protein",
        "asta_text": "Protein Description:** RecName: Full=Leucine-binding protein domain-containing protein",
        "family_text": "Belongs to the leucine-binding protein family.",
        "domain_text": "InterPro; IPR028081; Leu-bd.",
        "periplasmic_domain_text": "InterPro; IPR028082; Peripla_BP_I.",
        "signal_text": "FT   SIGNAL          1..28",
    },
    "PP_2753": {
        "accession": "Q88J96",
        "kind": "atpase",
        "role": "second branched-chain amino-acid ABC importer ATP-binding subunit",
        "description": (
            "PP_2753 encodes the second predicted ATP-binding energy-coupling subunit of the "
            "PP_2748-PP_2753 branched-chain amino-acid ABC uptake system. Its ABC ATPase domain, "
            "BCAA transport ATP-binding domain, and BCAA transporter GOA rows support ATP "
            "hydrolysis-driven import with the adjacent permease and binding-protein components."
        ),
        "uniprot_text": "Full=Branched-chain amino acid ABC transporter, ATP-binding protein",
        "asta_text": "Protein Description:** SubName: Full=Branched-chain amino acid ABC transporter, ATP-binding protein",
        "domain_text": "InterPro; IPR052156; BCAA_Transport_ATP-bd_LivF.",
        "panther_text": "HIGH-AFFINITY BRANCHED-CHAIN AMINO ACID TRANSPORT ATP-BINDING PROTEIN LIVF",
        "has_membrane_goa": False,
    },
}


def go_term(term: dict) -> dict:
    return {"id": term["id"], "label": term["label"]}


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


def new_annotation(gene: str, term: dict, qualifier: str, summary: str, reason: str, support: list[dict]) -> dict:
    return {
        "term": go_term(term),
        "evidence_type": "IEA",
        "original_reference_id": uniprot_ref(gene),
        "qualifier": qualifier,
        "review": {
            "summary": summary,
            "action": "NEW",
            "reason": reason,
            "supported_by": support,
        },
    }


def atpase_review(gene: str, cfg: dict, term_id: str, label: str) -> dict:
    product = support_uniprot(gene, cfg["uniprot_text"])
    domain = support_uniprot(gene, cfg["domain_text"])
    panther = support_uniprot(gene, cfg["panther_text"])
    asta = support_asta(gene, cfg["asta_text"])
    mapping = {
        "GO:0000166": (
            "Nucleotide binding is true but less informative than ATP binding for this ABC ATPase.",
            "MARK_AS_OVER_ANNOTATED",
            "The review retains the more specific ATP-binding and ATP-hydrolysis annotations for the transporter ATPase.",
            None,
            [product, domain],
        ),
        "GO:0005524": (
            "ATP binding is correct for this ABC-transporter nucleotide-binding component.",
            "ACCEPT",
            "The protein is named as a branched-chain amino-acid ABC transporter ATP-binding protein and has ABC ATPase domains.",
            None,
            [product, domain, asta],
        ),
        "GO:0005886": (
            "Plasma membrane localization is appropriate for a membrane-associated bacterial ABC transporter ATPase at first pass.",
            "ACCEPT",
            "The GOA row places this ATP-binding component at the plasma membrane, consistent with its role in an inner-membrane ABC transporter complex.",
            None,
            [product],
        ),
        "GO:0015658": (
            "Branched-chain amino acid transmembrane transporter activity is appropriate as the complex-level function to which this ATPase contributes.",
            "ACCEPT",
            f"{gene} is classified as a branched-chain amino-acid ABC transporter ATP-binding component in the {LOCUS} locus.",
            None,
            [product, panther, asta],
        ),
        "GO:0015803": (
            "Branched-chain amino acid transport is the correct first-pass process for this ABC ATP-binding component.",
            "ACCEPT",
            f"The {LOCUS} locus is a predicted branched-chain amino-acid ABC uptake system.",
            None,
            [product, panther, asta],
        ),
        "GO:0015807": (
            "L-amino acid transport is true but too general for this BCAA ABC transporter ATPase.",
            "MARK_AS_OVER_ANNOTATED",
            "The specific branched-chain amino acid transport annotation should be used as the core process.",
            None,
            [product, panther],
        ),
        "GO:0016887": (
            "ATP hydrolysis activity is the correct mechanistic activity for this ABC ATPase subunit.",
            "ACCEPT",
            f"ATP hydrolysis by {gene} is expected to provide energy coupling to the {LOCUS} branched-chain amino-acid ABC importer.",
            None,
            [product, domain, asta],
        ),
    }
    entry = mapping[term_id]
    return review(gene, term_id, label, entry[0], entry[1], entry[2], proposed=entry[3], extra_support=entry[4])


def permease_review(gene: str, cfg: dict, term_id: str, label: str) -> dict:
    product = support_uniprot(gene, cfg["uniprot_text"])
    location = support_uniprot(gene, cfg["location_text"])
    domain = support_uniprot(gene, cfg["domain_text"])
    panther = support_uniprot(gene, cfg["panther_text"])
    asta = support_asta(gene, cfg["asta_text"])
    mapping = {
        "GO:0005886": (
            "Plasma membrane localization is appropriate for this predicted inner-membrane ABC permease.",
            "ACCEPT",
            "UniProt predicts this permease as a cell inner-membrane multi-pass membrane protein.",
            None,
            [location, product, asta],
        ),
        "GO:0006865": (
            "Amino acid transport is correct but broad for this BCAA ABC-transporter permease.",
            "MODIFY",
            f"The product name and local {LOCUS} transporter context support branched-chain amino acid transport as the better process term.",
            [go_term(BCAA_TRANSPORT)],
            [product, domain, asta],
        ),
        "GO:0015658": (
            "Branched-chain amino acid transmembrane transporter activity is appropriate as the complex-level function to which this permease contributes.",
            "ACCEPT",
            "The product name and high-affinity BCAA transport-system permease family assignment identify this protein as a BCAA transport permease.",
            None,
            [product, panther, asta],
        ),
        "GO:0015803": (
            "Branched-chain amino acid transport is the correct first-pass process for this permease.",
            "ACCEPT",
            f"The {LOCUS} locus is a predicted branched-chain amino-acid ABC uptake system.",
            None,
            [product, panther, asta],
        ),
        "GO:0016020": (
            "Membrane localization is true but less informative than plasma membrane for this bacterial inner-membrane permease.",
            "MARK_AS_OVER_ANNOTATED",
            "The record also has a plasma-membrane annotation and UniProt predicts a cell inner-membrane multi-pass protein.",
            None,
            [location, product],
        ),
        "GO:0022857": (
            "Generic transmembrane transporter activity is too broad for this BCAA ABC-transporter permease component.",
            "MODIFY",
            "The product name and BCAA transport permease domain support branched-chain amino acid transmembrane transporter activity as the better complex-level activity.",
            [go_term(BCAA_ACTIVITY)],
            [product, domain, asta],
        ),
        "GO:0055085": (
            "Transmembrane transport is true but broad relative to the branched-chain amino-acid ABC-import context.",
            "MODIFY",
            "Branched-chain amino acid transport better captures the expected substrate class for this permease.",
            [go_term(BCAA_TRANSPORT)],
            [product, domain, asta],
        ),
    }
    entry = mapping[term_id]
    return review(gene, term_id, label, entry[0], entry[1], entry[2], proposed=entry[3], extra_support=entry[4])


def new_annotations_for_gene(gene: str, cfg: dict) -> list[dict]:
    product_support = [support_uniprot(gene, cfg["uniprot_text"]), support_asta(gene, cfg["asta_text"])]
    if cfg["kind"] == "atpase":
        return [
            new_annotation(
                gene,
                BCAA_ACTIVITY,
                "contributes_to",
                f"Branched-chain amino acid transmembrane transporter activity captures the complex-level activity to which {gene} contributes.",
                f"{gene} is an ATP-binding component of the adjacent {LOCUS} branched-chain amino-acid ABC transporter locus.",
                [support_uniprot(gene, cfg["uniprot_text"]), support_uniprot(gene, cfg["domain_text"]), support_asta(gene, cfg["asta_text"])],
            ),
            new_annotation(
                gene,
                BCAA_TRANSPORT,
                "involved_in",
                f"Branched-chain amino acid transport is a useful missing process annotation for {gene}.",
                f"{gene} is paired with BCAA transporter ATP-binding, permease, and leucine-family binding components.",
                product_support,
            ),
            new_annotation(
                gene,
                ABC_COMPLEX,
                "part_of",
                f"ABC transporter complex membership is appropriate for {gene}.",
                f"{gene} is an ATP-binding component of the adjacent {LOCUS} branched-chain amino-acid ABC transporter locus.",
                product_support,
            ),
        ]
    if cfg["kind"] == "permease":
        return [
            new_annotation(
                gene,
                BCAA_ACTIVITY,
                "contributes_to",
                f"Branched-chain amino acid transmembrane transporter activity captures the complex-level activity to which {gene} contributes.",
                f"{gene} is a permease subunit of the adjacent {LOCUS} branched-chain amino-acid ABC transporter.",
                [support_uniprot(gene, cfg["uniprot_text"]), support_uniprot(gene, cfg["domain_text"]), support_asta(gene, cfg["asta_text"])],
            ),
            new_annotation(
                gene,
                BCAA_TRANSPORT,
                "involved_in",
                f"Branched-chain amino acid transport is a useful missing process annotation for {gene}.",
                f"{gene} is paired with BCAA transporter ATP-binding, permease, and leucine-family binding components.",
                product_support,
            ),
            new_annotation(
                gene,
                ABC_COMPLEX,
                "part_of",
                f"ABC transporter complex membership is appropriate for {gene}.",
                f"{gene} is a permease component of the adjacent {LOCUS} branched-chain amino-acid ABC transporter locus.",
                product_support,
            ),
        ]
    return [
        new_annotation(
            gene,
            L_LEUCINE_BINDING,
            "enables",
            "L-leucine binding captures the expected substrate-recognition role of this leucine-binding protein family member.",
            f"{gene} is named as a leucine-binding protein domain-containing protein and belongs to the leucine-binding protein family.",
            [
                support_uniprot(gene, cfg["uniprot_text"]),
                support_uniprot(gene, cfg["family_text"]),
                support_uniprot(gene, cfg["domain_text"]),
                support_asta(gene, cfg["asta_text"]),
            ],
        ),
        new_annotation(
            gene,
            BCAA_TRANSPORT,
            "involved_in",
            f"Branched-chain amino acid transport is a useful process annotation for {gene}.",
            f"{gene} is a predicted substrate-binding component of the adjacent {LOCUS} branched-chain amino-acid ABC transporter locus.",
            [
                support_uniprot(gene, cfg["uniprot_text"]),
                support_uniprot(gene, cfg["domain_text"]),
                support_asta(gene, cfg["asta_text"]),
            ],
        ),
        new_annotation(
            gene,
            BCAA_ACTIVITY,
            "contributes_to",
            f"{gene} contributes substrate recognition to the branched-chain amino acid transmembrane transporter activity of the {LOCUS} complex.",
            "As a solute-binding component, it supplies substrate capture rather than catalyzing membrane translocation alone.",
            [
                support_uniprot(gene, cfg["uniprot_text"]),
                support_uniprot(gene, cfg["periplasmic_domain_text"]),
                support_asta(gene, cfg["asta_text"]),
            ],
        ),
        new_annotation(
            gene,
            PERIPLASM,
            "located_in",
            "Outer membrane-bounded periplasmic-space localization is appropriate for this signal-peptide-bearing Gram-negative substrate-binding protein.",
            f"{gene} has an N-terminal signal peptide and a periplasmic binding-protein domain.",
            [
                support_uniprot(gene, cfg["signal_text"]),
                support_uniprot(gene, cfg["periplasmic_domain_text"]),
                support_asta(gene, cfg["asta_text"]),
            ],
        ),
        new_annotation(
            gene,
            ABC_COMPLEX,
            "part_of",
            f"ABC transporter complex membership is appropriate for this {gene} substrate-binding component.",
            f"{gene} is a leucine-family binding component next to the {LOCUS} ABC ATPase/permease genes.",
            product_support,
        ),
    ]


def core_function(gene: str, cfg: dict) -> dict:
    if cfg["kind"] == "atpase":
        core = {
            "description": f"ATP-binding energy-coupling subunit contributing to the predicted {LOCUS} branched-chain amino-acid ABC uptake system.",
            "molecular_function": go_term(ATP_HYDROLYSIS),
            "contributes_to_molecular_function": go_term(BCAA_ACTIVITY),
            "directly_involved_in": [go_term(BCAA_TRANSPORT)],
            "in_complex": go_term(ABC_COMPLEX),
            "supported_by": [
                support_goa(gene, "GO:0016887", ATP_HYDROLYSIS["label"]),
                support_uniprot(gene, cfg["uniprot_text"]),
                support_uniprot(gene, cfg["domain_text"]),
                support_asta(gene, cfg["asta_text"]),
            ],
        }
        if cfg.get("has_membrane_goa"):
            core["locations"] = [go_term(PLASMA_MEMBRANE)]
            core["supported_by"].append(support_goa(gene, "GO:0005886", PLASMA_MEMBRANE["label"]))
    elif cfg["kind"] == "permease":
        core = {
            "description": f"Multi-pass permease component contributing to the predicted {LOCUS} branched-chain amino-acid ABC uptake system.",
            "contributes_to_molecular_function": go_term(BCAA_ACTIVITY),
            "directly_involved_in": [go_term(BCAA_TRANSPORT)],
            "locations": [go_term(PLASMA_MEMBRANE)],
            "in_complex": go_term(ABC_COMPLEX),
            "supported_by": [
                support_uniprot(gene, cfg["uniprot_text"]),
                support_uniprot(gene, cfg["domain_text"]),
                support_uniprot(gene, cfg["location_text"]),
                support_asta(gene, cfg["asta_text"]),
            ],
        }
    else:
        core = {
            "description": f"Periplasmic L-leucine/branched-chain amino-acid substrate-binding component contributing substrate capture to the predicted {LOCUS} ABC uptake system.",
            "molecular_function": go_term(L_LEUCINE_BINDING),
            "contributes_to_molecular_function": go_term(BCAA_ACTIVITY),
            "directly_involved_in": [go_term(BCAA_TRANSPORT)],
            "locations": [go_term(PERIPLASM)],
            "in_complex": go_term(ABC_COMPLEX),
            "supported_by": [
                support_uniprot(gene, cfg["uniprot_text"]),
                support_uniprot(gene, cfg["family_text"]),
                support_uniprot(gene, cfg["domain_text"]),
                support_uniprot(gene, cfg["signal_text"]),
                support_asta(gene, cfg["asta_text"]),
            ],
        }
    return core


def curate_gene(gene: str, cfg: dict) -> None:
    path = Path("genes") / SPECIES / gene / f"{gene}-ai-review.yaml"
    doc = yaml.safe_load(path.read_text())
    doc["gene_symbol"] = gene
    doc["status"] = "COMPLETE"
    doc["description"] = cfg["description"]

    ensure_reference(doc, goa_ref(gene), f"QuickGO GOA annotations for {gene}")
    ensure_reference(doc, uniprot_ref(gene), f"UniProtKB entry for {gene} ({cfg['accession']})", cfg["uniprot_text"])
    ensure_reference(doc, asta_ref(gene), f"Asta retrieval report for {gene} ({cfg['accession']})", cfg["asta_text"])

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
        if cfg["kind"] == "atpase":
            ann["review"] = atpase_review(gene, cfg, term["id"], term["label"])
        elif cfg["kind"] == "permease":
            ann["review"] = permease_review(gene, cfg, term["id"], term["label"])
        else:
            raise ValueError(f"Unexpected GOA annotation for binding-only gene {gene}: {term['id']}")

    existing_term_ids = {ann["term"]["id"] for ann in doc.get("existing_annotations", [])}
    for extra in new_annotations_for_gene(gene, cfg):
        term_id = extra["term"]["id"]
        if term_id in existing_term_ids:
            continue
        doc.setdefault("existing_annotations", []).append(extra)
        existing_term_ids.add(term_id)

    doc["core_functions"] = [core_function(gene, cfg)]
    doc["proposed_new_terms"] = []
    doc["suggested_questions"] = [
        {
            "question": (
                "What substrate range and regulation distinguish the PP_2748-PP_2753 BCAA ABC importer from the other "
                "P. putida KT2440 branched-chain amino-acid transporter loci?"
            )
        }
    ]
    doc["suggested_experiments"] = [
        {
            "description": (
                "Measure uptake and growth phenotypes for PP_2748-PP_2753 mutants, alone and in combination with other "
                "BCAA transporter loci, using L-leucine, L-isoleucine, L-valine, alanine, and related hydrophobic amino "
                "acids as candidate substrates."
            ),
            "experiment_type": "targeted transporter mutant substrate-uptake and redundancy assay",
        }
    ]

    path.write_text(yaml.safe_dump(doc, sort_keys=False, width=120))
    print(f"curated {path}")


def preferred(term: dict, preferred_term: str | None = None, description: str | None = None) -> dict:
    entry = {"preferred_term": preferred_term or term["label"], "term": go_term(term)}
    if description:
        entry["description"] = description
    return entry


def annoton(gene: str, cfg: dict) -> dict:
    base = {
        "id": f"{gene}_branched_chain_amino_acid_abc_{cfg['kind']}",
        "label": f"{gene}: {cfg['role']}",
        "participant": {"selector_type": "GENE", "gene": {"preferred_term": gene}},
        "processes": [preferred(BCAA_TRANSPORT)],
        "role_description": cfg["role"].capitalize() + ".",
    }
    if cfg["kind"] == "atpase":
        base["function"] = preferred(ATP_HYDROLYSIS)
        base["locations"] = [preferred(PLASMA_MEMBRANE)]
    elif cfg["kind"] == "permease":
        base["function"] = preferred(BCAA_ACTIVITY, "contributes to branched-chain amino acid transmembrane transporter activity")
        base["locations"] = [preferred(PLASMA_MEMBRANE)]
    else:
        base["function"] = preferred(L_LEUCINE_BINDING)
        base["locations"] = [preferred(PERIPLASM)]
    return base


def upsert_evidence(doc: dict, entry: dict) -> None:
    evidence = doc.setdefault("evidence", [])
    for idx, existing in enumerate(evidence):
        if existing.get("source_id") == entry["source_id"]:
            evidence[idx] = entry
            return
    evidence.append(entry)


def curate_module() -> None:
    doc = yaml.safe_load(MODULE_PATH.read_text())
    doc["description"] = (
        "Boundary module for five Pseudomonas putida KT2440 high-affinity branched-chain amino-acid "
        "ABC-transporter loci pulled from the KEGG ppu02010 ABC-transporter umbrella map. PP_1137-PP_1141 "
        "encodes the LivFGMHK system, PP_4863-PP_4867 encodes a related Bra/Liv system, PP_0615-PP_0619 "
        "encodes a third related system, PP_2767-PP_2770 encodes a fourth predicted BCAA importer, and "
        "PP_2748-PP_2753 encodes a fifth predicted BCAA importer with two ATP-binding subunits, two "
        "permeases, and two leucine-family substrate-binding components. The module records coherent "
        "predicted BCAA uptake systems while leaving relative specificity and redundancy open."
    )
    upsert_evidence(
        doc,
        {
            "source_id": "KEGG:ppu02010",
            "title": "ABC transporters - Pseudomonas putida KT2440",
            "statement": (
                "KEGG ppu02010 contributes the PP_0615-PP_0619, PP_1137-PP_1141, PP_2748-PP_2753, "
                "PP_2767-PP_2770, and PP_4863-PP_4867 loci as coherent amino-acid ABC transporter "
                "sub-batches within the broad ABC-transporter umbrella map."
            ),
        },
    )
    upsert_evidence(
        doc,
        {
            "source_id": "file:projects/P_PUTIDA/batches/ppu02010_abc_transporters_boundary.tsv",
            "title": "PSEPK ppu02010 ABC-transporter partition batch",
            "statement": (
                "The ppu02010 partition batch records cluster C14 as PP_0615-PP_0619, cluster C25 as "
                "livF-I, livG, livM, livH, and livK, cluster C38 as PP_2748, PP_2749, PP_2750, PP_2751, "
                "PP_2752, and PP_2753, cluster C40 as PP_2767, PP_2768, PP_2769, and PP_2770, and cluster "
                "C62 as livF-II, braF, braE, braD, and PP_4867 after first-pass curation."
            ),
        },
    )
    for gene, cfg in GENES.items():
        upsert_evidence(
            doc,
            {
                "source_id": f"UniProtKB:{cfg['accession']}",
                "title": f"{gene} {cfg['role']}",
                "statement": f"UniProt records {gene} as {cfg['uniprot_text'].removeprefix('Full=')}.",
            },
        )

    module = doc["module"]
    module["context"]["cellular_components"][0]["description"] = (
        "PP_0617/PP_0618, LivM/LivH, PP_2749/PP_2750, PP_2768/PP_2769, and BraE/BraD are predicted "
        "multi-pass inner-membrane permeases; PP_0615/PP_0616, LivF/LivG-family proteins, PP_2748/PP_2753, "
        "PP_2767, and LivF-II/BraF are ATP-binding energy-coupling components of the same transporter complexes."
    )
    module["context"]["cellular_components"][1]["description"] = (
        "PP_0619, LivK, PP_2751/PP_2752, PP_2770, and PP_4867 are predicted signal-peptide-bearing "
        "periplasmic branched-chain amino-acid substrate-binding proteins."
    )
    for concept in module["concepts"]:
        if concept.get("term", {}).get("id") == BCAA_TRANSPORT["id"]:
            concept["description"] = (
                "Uptake of branched-chain amino acids by the PP_0615-PP_0619, LivFGMHK, PP_2748-PP_2753, "
                "PP_2767-PP_2770, and Bra/Liv ABC importers."
            )
        elif concept.get("term", {}).get("id") == L_LEUCINE_BINDING["id"]:
            concept["description"] = (
                "Solute binding by LivK, PP_0619, PP_2751/PP_2752, PP_2770, and PP_4867 leucine-family "
                "substrate-recognition components."
            )

    parts = [
        part
        for part in module["parts"]
        if part.get("node", {}).get("id") != "pp2748_pp2753_branched_chain_amino_acid_abc_import"
    ]
    parts.append(
        {
            "order": 5,
            "role": "PP_2748-PP_2753 branched-chain amino-acid ABC import",
            "node": {
                "id": "pp2748_pp2753_branched_chain_amino_acid_abc_import",
                "label": "PP_2748-PP_2753 branched-chain amino-acid ABC import",
                "module_type": "TRANSPORT_STEP",
                "description": (
                    "The PP_2748-PP_2753 locus encodes a fifth predicted high-affinity branched-chain amino-acid "
                    "ABC importer. PP_2748 and PP_2753 are ATP-binding energy-coupling components, PP_2749 and "
                    "PP_2750 are membrane permeases, and PP_2751/PP_2752 are signal-peptide-bearing leucine-binding "
                    "protein family components. First-pass curation supports BCAA import while leaving relative "
                    "specificity, binding-protein redundancy, and regulatory differences from other P. putida BCAA "
                    "importers open."
                ),
                "concepts": [preferred(BCAA_TRANSPORT), preferred(BCAA_ACTIVITY), preferred(L_LEUCINE_BINDING)],
                "annotons": [
                    annoton(gene, GENES[gene])
                    for gene in ["PP_2748", "PP_2753", "PP_2749", "PP_2750", "PP_2751", "PP_2752"]
                ],
            },
        }
    )
    module["parts"] = sorted(parts, key=lambda part: part["order"])
    MODULE_PATH.write_text(yaml.safe_dump(doc, sort_keys=False, width=120))
    print(f"updated {MODULE_PATH}")


def main() -> None:
    for gene, cfg in GENES.items():
        curate_gene(gene, cfg)
    curate_module()


if __name__ == "__main__":
    main()
