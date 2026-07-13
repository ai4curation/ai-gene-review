#!/usr/bin/env python3
"""First-pass curation for the ppu02010 C03 PP_0140-PP_0142 Mce/MlaD-MlaE-like locus."""

from __future__ import annotations

from copy import deepcopy
from pathlib import Path

import yaml


SPECIES = "PSEPK"
MODULE_PATH = Path("modules/mce_mlad_mlae_like_phospholipid_transport_boundary.yaml")


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
    data = {
        "summary": summary,
        "action": action,
        "reason": reason,
        "supported_by": supported_by,
    }
    if proposed:
        data["proposed_replacement_terms"] = deepcopy(proposed)
    return data


def new_annotation(
    term: dict,
    qualifier: str,
    gene: str,
    summary: str,
    reason: str,
    supported_by: list[dict],
) -> dict:
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


def upsert_annotation(doc: dict, annotation: dict) -> None:
    annotations = doc.setdefault("existing_annotations", [])
    term_id = annotation["term"]["id"]
    qualifier = annotation.get("qualifier")
    for existing in annotations:
        if existing.get("term", {}).get("id") == term_id and existing.get("qualifier") == qualifier:
            existing.update(annotation)
            return
    annotations.append(annotation)


NUCLEOTIDE_BINDING = {"id": "GO:0000166", "label": "nucleotide binding"}
ATP_BINDING = {"id": "GO:0005524", "label": "ATP binding"}
ATP_HYDROLYSIS = {"id": "GO:0016887", "label": "ATP hydrolysis activity"}
PHOSPHOLIPID_BINDING = {"id": "GO:0005543", "label": "phospholipid binding"}
PHOSPHOLIPID_TRANSPORT = {"id": "GO:0015914", "label": "phospholipid transport"}
PLASMA_MEMBRANE = {"id": "GO:0005886", "label": "plasma membrane"}
ABC_COMPLEX = {
    "id": "GO:0043190",
    "label": "ATP-binding cassette (ABC) transporter complex",
}


GENES = {
    "PP_0140": {
        "accession": "Q88RI9",
        "status": "DRAFT",
        "description": (
            "PP_0140 encodes a small membrane-associated Mce/MlaD-domain protein in the "
            "PP_0140-PP_0142 locus. The domain architecture and adjacent MlaE-family "
            "permease support a putative role as an MlaD-like phospholipid-binding "
            "component of a candidate envelope phospholipid ABC transporter, but no "
            "direct P. putida experimental evidence or named reviewed pathway annotation "
            "was found in this first pass."
        ),
        "product_text": "Full=Mce/MlaD domain-containing protein",
        "domain_text": "InterPro; IPR003399; Mce/MlaD.",
        "pfam_text": "Pfam; PF02470; MlaD; 1.",
        "tm_text": "FT   TRANSMEM        7..29",
        "asta_text": "Protein Description:** RecName: Full=Mce/MlaD domain-containing protein",
    },
    "PP_0141": {
        "accession": "Q88RI8",
        "status": "COMPLETE",
        "description": (
            "PP_0141 encodes the predicted ABC ATP-binding protein adjacent to the "
            "PP_0140 Mce/MlaD-domain protein and the PP_0142 MlaE-family permease. "
            "Its supported molecular role is ATP binding and ATP hydrolysis by an ABC "
            "transporter nucleotide-binding domain; its substrate pathway assignment to "
            "the PP_0140-PP_0142 putative phospholipid transporter is inferred from "
            "locus context."
        ),
        "product_text": "Full=ABC transporter, ATP-binding protein",
        "domain_text": "InterPro; IPR003439; ABC_transporter-like_ATP-bd.",
        "cs_text": "InterPro; IPR017871; ABC_transporter-like_CS.",
        "ft_domain_text": "FT   DOMAIN          8..245",
        "asta_text": "Protein Description:** SubName: Full=ABC transporter, ATP-binding protein",
    },
    "PP_0142": {
        "accession": "Q88RI7",
        "status": "COMPLETE",
        "description": (
            "PP_0142 encodes a predicted multi-pass inner-membrane MlaE-family permease "
            "in the PP_0140-PP_0142 locus. UniProt places it in the cell inner membrane "
            "and assigns MlaE-family lipid ABC transporter permease features, supporting "
            "the existing phospholipid transport and ABC-transporter-complex annotations "
            "as a first-pass putative envelope phospholipid transporter call."
        ),
        "product_text": "Full=ABC transporter, permease protein",
        "family_text": "Belongs to the MlaE permease family.",
        "location_text": "Cell inner membrane",
        "domain_text": "InterPro; IPR003453; ABC_MlaE_roteobac.",
        "ncbifam_text": "NCBIfam; TIGR00056; MlaE family lipid ABC transporter permease subunit; 1.",
        "tm_text": "FT   TRANSMEM        171..195",
        "asta_text": "Protein Description:** SubName: Full=ABC transporter, permease protein",
    },
}


def add_common_references(doc: dict, gene: str, cfg: dict) -> None:
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


def curate_pp0140(doc: dict, gene: str, cfg: dict) -> None:
    phospholipid_binding_support = [
        support_uniprot(gene, cfg["product_text"]),
        support_uniprot(gene, cfg["domain_text"]),
        support_uniprot(gene, cfg["pfam_text"]),
        support_uniprot("PP_0142", GENES["PP_0142"]["family_text"]),
        support_uniprot("PP_0142", GENES["PP_0142"]["ncbifam_text"]),
        support_asta(gene, cfg["asta_text"]),
    ]
    transport_support = [
        support_uniprot(gene, cfg["domain_text"]),
        support_uniprot("PP_0142", GENES["PP_0142"]["family_text"]),
        support_uniprot("PP_0142", GENES["PP_0142"]["ncbifam_text"]),
        support_goa("PP_0142", "GO:0015914", "phospholipid transport"),
    ]
    upsert_annotation(
        doc,
        new_annotation(
            PHOSPHOLIPID_BINDING,
            "enables",
            gene,
            "Phospholipid binding is a plausible Mce/MlaD-domain function for PP_0140.",
            "PP_0140 is an Mce/MlaD-domain protein adjacent to an MlaE-family lipid ABC transporter permease; the exact substrate and binding activity remain inferred.",
            phospholipid_binding_support,
        ),
    )
    upsert_annotation(
        doc,
        new_annotation(
            PHOSPHOLIPID_TRANSPORT,
            "involved_in",
            gene,
            "Phospholipid transport is a putative locus-level process for PP_0140.",
            "The PP_0140 Mce/MlaD-domain protein is paired with PP_0142, an MlaE-family lipid ABC transporter permease with a GOA phospholipid-transport annotation.",
            transport_support,
        ),
    )
    upsert_annotation(
        doc,
        new_annotation(
            ABC_COMPLEX,
            "part_of",
            gene,
            "ABC transporter complex membership is inferred from the PP_0140-PP_0142 locus organization.",
            "PP_0140 lies next to an ABC ATP-binding protein and an MlaE-family permease; this supports a candidate ABC transporter complex part annotation, but the complex is not experimentally resolved.",
            [
                support_uniprot(gene, cfg["domain_text"]),
                support_uniprot("PP_0141", GENES["PP_0141"]["product_text"]),
                support_uniprot("PP_0142", GENES["PP_0142"]["family_text"]),
                support_goa("PP_0142", "GO:0043190", "ATP-binding cassette (ABC) transporter complex"),
            ],
        ),
    )


def curate_pp0141(doc: dict, gene: str, cfg: dict) -> None:
    for annotation in doc.get("existing_annotations", []):
        term = annotation.get("term", {})
        term_id = term.get("id")
        label = term.get("label")
        if term_id == "GO:0000166":
            annotation["review"] = review(
                gene,
                term_id,
                label,
                "Nucleotide binding is true but too broad for this ABC ATP-binding protein.",
                "MODIFY",
                "PP_0141 has an ABC transporter ATP-binding domain and a more informative ATP-binding annotation is already present.",
                proposed=[ATP_BINDING],
                extra_support=[
                    support_uniprot(gene, cfg["product_text"]),
                    support_uniprot(gene, cfg["domain_text"]),
                    support_uniprot(gene, cfg["ft_domain_text"]),
                ],
            )
        elif term_id == "GO:0005524":
            annotation["review"] = review(
                gene,
                term_id,
                label,
                "ATP binding is appropriate for PP_0141.",
                "ACCEPT",
                "PP_0141 is annotated as an ABC transporter ATP-binding protein and carries conserved ABC transporter ATP-binding signatures.",
                extra_support=[
                    support_uniprot(gene, cfg["product_text"]),
                    support_uniprot(gene, cfg["domain_text"]),
                    support_uniprot(gene, cfg["cs_text"]),
                    support_asta(gene, cfg["asta_text"]),
                ],
            )
        elif term_id == "GO:0016887":
            annotation["review"] = review(
                gene,
                term_id,
                label,
                "ATP hydrolysis activity is appropriate for the PP_0141 ABC ATP-binding protein.",
                "ACCEPT",
                "The ABC transporter nucleotide-binding domain supports ATP hydrolysis as PP_0141's core molecular activity.",
                extra_support=[
                    support_uniprot(gene, cfg["product_text"]),
                    support_uniprot(gene, cfg["domain_text"]),
                    support_uniprot(gene, cfg["cs_text"]),
                    support_asta(gene, cfg["asta_text"]),
                ],
            )
    upsert_annotation(
        doc,
        new_annotation(
            PHOSPHOLIPID_TRANSPORT,
            "involved_in",
            gene,
            "Phospholipid transport is a putative locus-level process for PP_0141.",
            "PP_0141 is the predicted ABC ATPase adjacent to PP_0142, an MlaE-family lipid ABC transporter permease with a phospholipid-transport annotation.",
            [
                support_uniprot(gene, cfg["product_text"]),
                support_uniprot("PP_0142", GENES["PP_0142"]["family_text"]),
                support_uniprot("PP_0142", GENES["PP_0142"]["ncbifam_text"]),
                support_goa("PP_0142", "GO:0015914", "phospholipid transport"),
            ],
        ),
    )
    upsert_annotation(
        doc,
        new_annotation(
            ABC_COMPLEX,
            "part_of",
            gene,
            "ABC transporter complex membership is appropriate for PP_0141.",
            "PP_0141 is an ABC ATP-binding protein adjacent to the PP_0142 MlaE-family permease in a candidate ABC transporter locus.",
            [
                support_uniprot(gene, cfg["product_text"]),
                support_uniprot(gene, cfg["domain_text"]),
                support_uniprot("PP_0142", GENES["PP_0142"]["family_text"]),
                support_goa("PP_0142", "GO:0043190", "ATP-binding cassette (ABC) transporter complex"),
            ],
        ),
    )


def curate_pp0142(doc: dict, gene: str, cfg: dict) -> None:
    for annotation in doc.get("existing_annotations", []):
        term = annotation.get("term", {})
        term_id = term.get("id")
        label = term.get("label")
        if term_id == "GO:0005886":
            annotation["review"] = review(
                gene,
                term_id,
                label,
                "Plasma membrane localization is appropriate for the PP_0142 inner-membrane MlaE-family permease.",
                "ACCEPT",
                "UniProt places PP_0142 in the cell inner membrane and predicts multiple transmembrane helices.",
                extra_support=[
                    support_uniprot(gene, cfg["location_text"]),
                    support_uniprot(gene, cfg["tm_text"]),
                ],
            )
        elif term_id == "GO:0015914":
            annotation["review"] = review(
                gene,
                term_id,
                label,
                "Phospholipid transport is appropriate as a first-pass MlaE-family permease process annotation.",
                "ACCEPT",
                "PP_0142 belongs to the MlaE permease family and is classified by NCBIfam as a lipid ABC transporter permease subunit.",
                extra_support=[
                    support_uniprot(gene, cfg["family_text"]),
                    support_uniprot(gene, cfg["domain_text"]),
                    support_uniprot(gene, cfg["ncbifam_text"]),
                    support_asta(gene, cfg["asta_text"]),
                ],
            )
        elif term_id == "GO:0043190":
            annotation["review"] = review(
                gene,
                term_id,
                label,
                "ABC transporter complex membership is appropriate for PP_0142.",
                "ACCEPT",
                "PP_0142 is an MlaE-family lipid ABC transporter permease paired with an adjacent ABC ATP-binding protein.",
                extra_support=[
                    support_uniprot(gene, cfg["family_text"]),
                    support_uniprot(gene, cfg["ncbifam_text"]),
                    support_uniprot("PP_0141", GENES["PP_0141"]["product_text"]),
                ],
            )


def core_functions(gene: str) -> list[dict]:
    if gene == "PP_0140":
        return [
            {
                "description": "Putative Mce/MlaD-domain phospholipid-binding component of the PP_0140-PP_0142 MlaE-like ABC transporter candidate.",
                "molecular_function": PHOSPHOLIPID_BINDING,
                "directly_involved_in": [PHOSPHOLIPID_TRANSPORT],
                "in_complex": ABC_COMPLEX,
                "supported_by": [
                    support_uniprot(gene, GENES[gene]["product_text"]),
                    support_uniprot(gene, GENES[gene]["domain_text"]),
                    support_uniprot(gene, GENES[gene]["pfam_text"]),
                    support_uniprot("PP_0142", GENES["PP_0142"]["family_text"]),
                    support_uniprot("PP_0142", GENES["PP_0142"]["ncbifam_text"]),
                ],
            }
        ]
    if gene == "PP_0141":
        return [
            {
                "description": "ATP-hydrolyzing ABC energy-coupling subunit of the PP_0140-PP_0142 MlaE-like phospholipid transporter candidate.",
                "molecular_function": ATP_HYDROLYSIS,
                "directly_involved_in": [PHOSPHOLIPID_TRANSPORT],
                "in_complex": ABC_COMPLEX,
                "supported_by": [
                    support_goa(gene, "GO:0016887", "ATP hydrolysis activity"),
                    support_uniprot(gene, GENES[gene]["product_text"]),
                    support_uniprot(gene, GENES[gene]["domain_text"]),
                    support_uniprot("PP_0142", GENES["PP_0142"]["family_text"]),
                    support_goa("PP_0142", "GO:0015914", "phospholipid transport"),
                ],
            }
        ]
    return [
        {
            "description": "Multi-pass inner-membrane MlaE-family permease of the PP_0140-PP_0142 MlaE-like phospholipid transporter candidate.",
            "directly_involved_in": [PHOSPHOLIPID_TRANSPORT],
            "locations": [PLASMA_MEMBRANE],
            "in_complex": ABC_COMPLEX,
            "supported_by": [
                support_goa(gene, "GO:0015914", "phospholipid transport"),
                support_goa(gene, "GO:0005886", "plasma membrane"),
                support_goa(gene, "GO:0043190", "ATP-binding cassette (ABC) transporter complex"),
                support_uniprot(gene, GENES[gene]["location_text"]),
                support_uniprot(gene, GENES[gene]["family_text"]),
                support_uniprot(gene, GENES[gene]["ncbifam_text"]),
            ],
        }
    ]


def curate_gene(gene: str) -> None:
    cfg = GENES[gene]
    path = Path("genes") / SPECIES / gene / f"{gene}-ai-review.yaml"
    doc = yaml.safe_load(path.read_text())
    doc["status"] = cfg["status"]
    doc["description"] = cfg["description"]
    add_common_references(doc, gene, cfg)
    if gene in {"PP_0140", "PP_0141"}:
        ensure_reference(
            doc,
            uniprot_ref("PP_0142"),
            "UniProtKB entry for PP_0142 (Q88RI7)",
            GENES["PP_0142"]["family_text"],
        )
    if gene == "PP_0140":
        ensure_reference(
            doc,
            goa_ref("PP_0142"),
            "QuickGO GOA annotations for PP_0142",
            "GO:0015914\tphospholipid transport",
        )
        ensure_reference(
            doc,
            uniprot_ref("PP_0141"),
            "UniProtKB entry for PP_0141 (Q88RI8)",
            GENES["PP_0141"]["product_text"],
        )
        curate_pp0140(doc, gene, cfg)
    elif gene == "PP_0141":
        ensure_reference(
            doc,
            goa_ref("PP_0142"),
            "QuickGO GOA annotations for PP_0142",
            "GO:0015914\tphospholipid transport",
        )
        curate_pp0141(doc, gene, cfg)
    else:
        ensure_reference(
            doc,
            uniprot_ref("PP_0141"),
            "UniProtKB entry for PP_0141 (Q88RI8)",
            GENES["PP_0141"]["product_text"],
        )
        curate_pp0142(doc, gene, cfg)
    doc["core_functions"] = core_functions(gene)
    doc["proposed_new_terms"] = []
    doc["suggested_questions"] = [
        {
            "question": (
                "Does the PP_0140-PP_0142 Mce/MlaD-MlaE-like locus form an active "
                "phospholipid ABC transporter in P. putida KT2440, and what is the "
                "directionality and physiological envelope-stress role?"
            )
        }
    ]
    doc["suggested_experiments"] = [
        {
            "description": (
                "Construct PP_0140, PP_0141, and PP_0142 single and combined deletion "
                "mutants and assay outer-membrane phospholipid asymmetry, envelope "
                "permeability, solvent sensitivity, and complementation by the intact locus."
            ),
            "experiment_type": "targeted Mce/MlaD-MlaE-like phospholipid transport phenotyping",
        }
    ]
    path.write_text(yaml.safe_dump(doc, sort_keys=False, width=120))


def write_module() -> None:
    module = {
        "id": "MODULE:mce_mlad_mlae_like_phospholipid_transport_boundary",
        "title": "PP_0140-PP_0142 Mce/MlaD-MlaE-like phospholipid transport candidate boundary",
        "description": (
            "Boundary module for the Pseudomonas putida KT2440 ppu02010 C03 "
            "PP_0140-PP_0142 locus. PP_0140 is an Mce/MlaD-domain protein, PP_0141 "
            "is an ABC ATP-binding protein, and PP_0142 is an inner-membrane "
            "MlaE-family lipid ABC transporter permease. The module records a "
            "putative envelope phospholipid ABC transporter candidate, distinct from "
            "the better supported PP_0958-PP_0962 Mla/Ttg2 system."
        ),
        "status": "DRAFT",
        "evidence": [
            {
                "source_id": "KEGG:ppu02010",
                "title": "ABC transporters - Pseudomonas putida KT2440",
                "statement": "KEGG ppu02010 contributes PP_0140, PP_0141, and PP_0142 as C03 ABC-transporter candidates.",
            },
            {
                "source_id": "file:projects/P_PUTIDA/batches/ppu02010_abc_transporters_boundary.tsv",
                "title": "PSEPK ppu02010 ABC-transporter partition batch",
                "statement": "The ppu02010 partition batch records cluster C03 as PP_0140, PP_0141, and PP_0142.",
            },
            {
                "source_id": "UniProtKB:Q88RI9",
                "title": "PP_0140 Mce/MlaD domain-containing protein",
                "statement": "UniProt records PP_0140 as an Mce/MlaD-domain protein with an MlaD/PF02470 domain.",
            },
            {
                "source_id": "UniProtKB:Q88RI8",
                "title": "PP_0141 ABC transporter ATP-binding protein",
                "statement": "UniProt records PP_0141 as an ABC transporter ATP-binding protein with ABC transporter ATP-binding domains.",
            },
            {
                "source_id": "UniProtKB:Q88RI7",
                "title": "PP_0142 MlaE-family lipid ABC transporter permease",
                "statement": "UniProt records PP_0142 as a cell-inner-membrane protein in the MlaE permease family and NCBIfam classifies it as an MlaE family lipid ABC transporter permease subunit.",
            },
        ],
        "module": {
            "id": "mce_mlad_mlae_like_phospholipid_transport_boundary",
            "label": "PP_0140-PP_0142 Mce/MlaD-MlaE-like phospholipid transport candidate",
            "module_type": "TRANSPORT_STEP",
            "concepts": [
                {
                    "preferred_term": "phospholipid transport",
                    "term": PHOSPHOLIPID_TRANSPORT,
                    "description": "Putative phospholipid transport by the PP_0140-PP_0142 Mce/MlaD-MlaE-like ABC transporter candidate.",
                },
                {
                    "preferred_term": "phospholipid binding",
                    "term": PHOSPHOLIPID_BINDING,
                    "description": "Inferred phospholipid-binding role for the PP_0140 Mce/MlaD-domain component.",
                },
                {
                    "preferred_term": "ATP hydrolysis activity",
                    "term": ATP_HYDROLYSIS,
                    "description": "ATP hydrolysis by the PP_0141 ABC energy-coupling subunit.",
                },
                {
                    "preferred_term": "ATP-binding cassette (ABC) transporter complex",
                    "term": ABC_COMPLEX,
                    "description": "Candidate ABC transporter complex represented by PP_0140, PP_0141, and PP_0142.",
                },
            ],
            "context": {
                "cellular_components": [
                    {
                        "preferred_term": "bacterial plasma membrane",
                        "term": PLASMA_MEMBRANE,
                        "description": "PP_0142 is a cell-inner-membrane MlaE-family permease.",
                    }
                ]
            },
            "parts": [
                {
                    "order": 1,
                    "role": "Mce/MlaD-MlaE-like phospholipid ABC transporter candidate",
                    "node": {
                        "id": "PP_0140_PP_0142_mce_mlad_mlae_like_transport",
                        "label": "PP_0140-PP_0142 Mce/MlaD-MlaE-like transport locus",
                        "module_type": "TRANSPORT_STEP",
                        "description": (
                            "The PP_0140-PP_0142 locus encodes an Mce/MlaD-domain "
                            "protein, an ABC ATP-binding protein, and an MlaE-family "
                            "inner-membrane permease. Current evidence supports a "
                            "putative phospholipid ABC transporter candidate but does "
                            "not establish direct substrate directionality."
                        ),
                        "concepts": [
                            {"preferred_term": "phospholipid transport", "term": PHOSPHOLIPID_TRANSPORT},
                            {"preferred_term": "phospholipid binding", "term": PHOSPHOLIPID_BINDING},
                        ],
                        "annotons": [
                            {
                                "id": "PP_0140_mce_mlad_component",
                                "label": "PP_0140: Mce/MlaD-domain phospholipid-binding candidate",
                                "participant": {
                                    "selector_type": "GENE",
                                    "gene": {"preferred_term": "PP_0140"},
                                },
                                "role_description": "Membrane-associated Mce/MlaD-domain component of the putative transporter.",
                                "function": {"preferred_term": "phospholipid binding", "term": PHOSPHOLIPID_BINDING},
                                "processes": [{"preferred_term": "phospholipid transport", "term": PHOSPHOLIPID_TRANSPORT}],
                            },
                            {
                                "id": "PP_0141_abc_atpase_component",
                                "label": "PP_0141: ABC ATP-binding energy-coupling subunit",
                                "participant": {
                                    "selector_type": "GENE",
                                    "gene": {"preferred_term": "PP_0141"},
                                },
                                "role_description": "Predicted ABC ATP-binding protein that supplies ATP hydrolysis.",
                                "function": {"preferred_term": "ATP hydrolysis activity", "term": ATP_HYDROLYSIS},
                                "processes": [{"preferred_term": "phospholipid transport", "term": PHOSPHOLIPID_TRANSPORT}],
                            },
                            {
                                "id": "PP_0142_mlae_like_permease",
                                "label": "PP_0142: MlaE-family inner-membrane permease",
                                "participant": {
                                    "selector_type": "GENE",
                                    "gene": {"preferred_term": "PP_0142"},
                                },
                                "role_description": "Multi-pass MlaE-family lipid ABC transporter permease.",
                                "processes": [{"preferred_term": "phospholipid transport", "term": PHOSPHOLIPID_TRANSPORT}],
                                "locations": [{"preferred_term": "plasma membrane", "term": PLASMA_MEMBRANE}],
                            },
                        ],
                    },
                }
            ],
        },
        "notes": (
            "This boundary was created from the ppu02010 ABC-transporter partition. "
            "It should remain distinct from the PP_0958-PP_0962 Mla/Ttg2 module until "
            "genetic or biochemical evidence establishes whether the C03 locus is a "
            "parallel Mla-like phospholipid transporter, a partial/remnant system, or "
            "a transporter with a more specific substrate."
        ),
    }
    MODULE_PATH.write_text(yaml.safe_dump(module, sort_keys=False, width=120))


def main() -> None:
    for gene in GENES:
        curate_gene(gene)
        print(f"curated {gene}")
    write_module()
    print(f"wrote {MODULE_PATH}")


if __name__ == "__main__":
    main()
