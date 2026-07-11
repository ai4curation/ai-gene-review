#!/usr/bin/env python3
"""First-pass curation for ppu02010 PotF-like polyamine-binding paralogs."""

from __future__ import annotations

from pathlib import Path

import yaml


SPECIES = "PSEPK"
MODULE_PATH = Path("modules/polyamine_transport_boundary.yaml")

POLYAMINE_TRANSPORT = {"id": "GO:0015846", "label": "polyamine transport"}
POLYAMINE_BINDING = {"id": "GO:0019808", "label": "polyamine binding"}
PERIPLASM = {"id": "GO:0042597", "label": "periplasmic space"}

GENES = {
    "PP_2195": {
        "accession": "Q88KU4",
        "locus": "PP_2195",
        "safe": "PP_2195",
        "cluster": "C30",
        "emb": "AAN67808.1",
        "subfamily": "PANTHER; PTHR30222:SF18; BIFUNCTIONAL POLYHYDROXYBUTYRATE SYNTHASE _ ABC TRANSPORTER PERIPLASMIC BINDING PROTEIN-RELATED; 1.",
    },
    "potF-II": {
        "accession": "Q88I54",
        "locus": "PP_3147",
        "safe": "potF_II",
        "cluster": "C43",
        "emb": "AAN68755.1",
        "subfamily": "PANTHER; PTHR30222:SF12; NORSPERMIDINE SENSOR; 1.",
    },
    "PP_3719": {
        "accession": "Q88GK2",
        "locus": "PP_3719",
        "safe": "PP_3719",
        "cluster": "C49",
        "emb": "AAN69316.1",
        "subfamily": "PANTHER; PTHR30222:SF12; NORSPERMIDINE SENSOR; 1.",
    },
    "potF-III": {
        "accession": "Q88G80",
        "locus": "PP_3845",
        "safe": "potF_III",
        "cluster": "C53",
        "emb": "AAN69439.1",
        "subfamily": "PANTHER; PTHR30222:SF12; NORSPERMIDINE SENSOR; 1.",
    },
    "potF-IV": {
        "accession": "Q88C42",
        "locus": "PP_5341",
        "safe": "potF_IV",
        "cluster": "C74",
        "emb": "AAN70906.1",
        "subfamily": "PANTHER; PTHR30222:SF12; NORSPERMIDINE SENSOR; 1.",
    },
}

MODULE_GENES = {
    "potF-I": {
        "accession": "Q88PH7",
        "locus": "PP_0873",
        "safe": "potF_I",
        "cluster": "C17",
        "title": "PotF-I putrescine-binding periplasmic protein",
    },
    **GENES,
}


def go_term(term_data: dict) -> dict:
    return {"id": term_data["id"], "label": term_data["label"]}


def gene_dir(gene: str) -> Path:
    return Path("genes") / SPECIES / gene


def review_path(gene: str) -> Path:
    return gene_dir(gene) / f"{gene}-ai-review.yaml"


def ref(gene: str, kind: str) -> str:
    return f"file:{SPECIES}/{gene}/{gene}-{kind}"


def support_goa(gene: str, term_id: str, label: str) -> dict:
    return {"reference_id": ref(gene, "goa.tsv"), "supporting_text": f"{term_id}\t{label}"}


def support_uniprot(gene: str, text: str) -> dict:
    return {"reference_id": ref(gene, "uniprot.txt"), "supporting_text": text}


def support_asta(gene: str, text: str) -> dict:
    return {"reference_id": ref(gene, "deep-research-asta.md"), "supporting_text": text}


def ensure_reference(doc: dict, ref_id: str, title: str, supporting_text: str | None = None) -> None:
    refs = doc.setdefault("references", [])
    for existing in refs:
        if existing.get("id") == ref_id:
            if supporting_text and not existing.get("findings"):
                existing["findings"] = [{"supporting_text": supporting_text}]
            return
    entry = {"id": ref_id, "title": title, "findings": []}
    if supporting_text:
        entry["findings"].append({"supporting_text": supporting_text})
    refs.append(entry)


def product_text(gene: str, cfg: dict) -> str:
    return f"Full=Putrescine-binding periplasmic protein"


def gene_display(gene: str, cfg: dict) -> str:
    if gene == cfg["locus"]:
        return gene
    return f"{gene} ({cfg['locus']})"


def asta_text(gene: str, cfg: dict) -> str:
    return f"SubName: Full=Putrescine-binding periplasmic protein {{ECO:0000313|EMBL:{cfg['emb']}}}"


def annotation_review(gene: str, term_id: str, label: str, cfg: dict) -> dict:
    family_text = "SPERMIDINE/PUTRESCINE-BINDING PERIPLASMIC PROTEIN"
    if term_id == POLYAMINE_TRANSPORT["id"]:
        return {
            "summary": "Polyamine transport is appropriate process context for this PotF-like periplasmic substrate-binding protein.",
            "action": "ACCEPT",
            "reason": (
                "UniProt names this product as a putrescine-binding periplasmic protein and InterPro/GOA "
                "associate the spermidine/putrescine-binding family with polyamine transport. The specific "
                "cognate permease and ATPase partners remain unresolved, so this is a component-level process annotation."
            ),
            "supported_by": [
                support_goa(gene, term_id, label),
                support_uniprot(gene, product_text(gene, cfg)),
                support_uniprot(gene, family_text),
            ],
        }
    if term_id == POLYAMINE_BINDING["id"]:
        return {
            "summary": "Polyamine binding is appropriate for this predicted putrescine-binding periplasmic protein.",
            "action": "ACCEPT",
            "reason": (
                "The product name, spermidine/putrescine-binding periplasmic-protein family assignment, "
                "and Asta retrieval all support substrate binding to putrescine or related polyamines."
            ),
            "supported_by": [
                support_goa(gene, term_id, label),
                support_uniprot(gene, product_text(gene, cfg)),
                support_uniprot(gene, family_text),
                support_asta(gene, asta_text(gene, cfg)),
            ],
        }
    if term_id == PERIPLASM["id"]:
        return {
            "summary": "Periplasmic localization is appropriate for this substrate-binding protein.",
            "action": "ACCEPT",
            "reason": "UniProt places the protein in the periplasm, matching its predicted soluble substrate-binding role.",
            "supported_by": [
                support_goa(gene, term_id, label),
                support_uniprot(gene, "Periplasm"),
            ],
        }
    raise ValueError(f"Unhandled term for {gene}: {term_id} {label}")


def curate_gene(gene: str, cfg: dict) -> None:
    path = review_path(gene)
    doc = yaml.safe_load(path.read_text())
    doc["status"] = "COMPLETE"
    doc["description"] = (
        f"{gene_display(gene, cfg)} encodes a predicted PotF-like periplasmic putrescine/polyamine "
        "substrate-binding protein in Pseudomonas putida KT2440. UniProt, InterPro/GOA, and Asta retrieval "
        "support periplasmic polyamine binding and polyamine-transport component context, while the cognate "
        "membrane permease and ATP-binding partners for this paralog remain unresolved."
    )

    for annotation in doc.get("existing_annotations", []):
        term = annotation.get("term", {})
        term_id = term.get("id")
        label = term.get("label")
        annotation["review"] = annotation_review(gene, term_id, label, cfg)

    ensure_reference(doc, ref(gene, "goa.tsv"), f"QuickGO GOA annotations for {gene}")
    ensure_reference(
        doc,
        ref(gene, "uniprot.txt"),
        f"UniProtKB entry for {gene} ({cfg['accession']})",
        product_text(gene, cfg),
    )
    ensure_reference(
        doc,
        ref(gene, "deep-research-asta.md"),
        f"Asta retrieval report for {gene} ({cfg['accession']})",
        asta_text(gene, cfg),
    )

    doc["core_functions"] = [
        {
            "description": "Periplasmic putrescine/polyamine substrate-binding protein with unresolved transporter partners.",
            "molecular_function": go_term(POLYAMINE_BINDING),
            "directly_involved_in": [go_term(POLYAMINE_TRANSPORT)],
            "locations": [go_term(PERIPLASM)],
            "supported_by": [
                support_goa(gene, POLYAMINE_BINDING["id"], POLYAMINE_BINDING["label"]),
                support_uniprot(gene, product_text(gene, cfg)),
                support_asta(gene, asta_text(gene, cfg)),
            ],
        }
    ]
    doc["proposed_new_terms"] = []
    doc["suggested_questions"] = [
        {
            "question": (
                f"Which permease and ATPase partners pair with {gene}, and does this PotF-like paralog "
                "prefer putrescine, spermidine, norspermidine, or another related polyamine?"
            )
        }
    ]
    doc["suggested_experiments"] = [
        {
            "description": (
                f"Measure purified {gene} ligand binding and compare deletion/complementation phenotypes "
                "for uptake or growth responses to putrescine, spermidine, norspermidine, and related polyamines."
            ),
            "experiment_type": "targeted PotF-like substrate-binding and polyamine-uptake assay",
        }
    ]
    path.write_text(yaml.safe_dump(doc, sort_keys=False, width=120))
    print(f"curated {path}")


def module_evidence() -> list[dict]:
    evidence = [
        {
            "source_id": "KEGG:ppu02010",
            "title": "ABC transporters - Pseudomonas putida KT2440",
            "statement": (
                "KEGG ppu02010 contributes potF-I, PP_2195, potF-II, PP_3719, potF-III, "
                "and potF-IV as singleton or locus-neighborhood PotF-like polyamine-binding "
                "components across clusters C17, C30, C43, C49, C53, and C74."
            ),
        },
        {
            "source_id": "file:projects/P_PUTIDA/batches/ppu02010_abc_transporters_boundary.tsv",
            "title": "PSEPK ppu02010 ABC-transporter partition batch",
            "statement": (
                "The ppu02010 partition batch records these PotF-like paralogs as putrescine-binding "
                "periplasmic proteins with polyamine transport, polyamine binding, and periplasmic-space GOA annotations."
            ),
        },
    ]
    for gene, cfg in MODULE_GENES.items():
        evidence.append(
            {
                "source_id": f"UniProtKB:{cfg['accession']}",
                "title": cfg.get("title", f"{gene} putrescine-binding periplasmic protein"),
                "statement": (
                    f"UniProt records {gene_display(gene, cfg)} as a putrescine-binding periplasmic protein "
                    "and assigns it to the spermidine/putrescine-binding periplasmic-protein family."
                ),
            }
        )
    return evidence


def module_annoton(gene: str, cfg: dict) -> dict:
    return {
        "id": f"{cfg['safe']}_polyamine_binding_annoton",
        "label": f"{gene}: putrescine/polyamine substrate-binding component",
        "participant": {
            "selector_type": "GENE",
            "gene": {"preferred_term": gene},
        },
        "function": {
            "preferred_term": "polyamine binding",
            "term": go_term(POLYAMINE_BINDING),
        },
        "processes": [
            {
                "preferred_term": "polyamine transport",
                "term": go_term(POLYAMINE_TRANSPORT),
            }
        ],
        "locations": [
            {
                "preferred_term": "periplasmic space",
                "term": go_term(PERIPLASM),
            }
        ],
        "role_description": (
            "Periplasmic putrescine/polyamine substrate-binding component with unresolved transporter partners."
        ),
    }


def curate_module() -> None:
    doc = yaml.safe_load(MODULE_PATH.read_text())
    doc["title"] = "PotF-like polyamine transport boundary"
    doc["description"] = (
        "Boundary module for Pseudomonas putida KT2440 PotF-like polyamine transport components encountered during "
        "ppu02010 ABC-transporter partitioning. The module covers potF-I, PP_2195, potF-II, PP_3719, potF-III, "
        "and potF-IV as predicted periplasmic putrescine/polyamine substrate-binding proteins. Their cognate "
        "membrane permease and ATP-binding partners remain unresolved, so this module records component-level "
        "polyamine binding rather than complete ABC uptake complexes."
    )
    doc["status"] = "DRAFT"
    doc["evidence"] = module_evidence()
    doc["module"] = {
        "id": "polyamine_transport_boundary",
        "label": "PotF-like polyamine transport boundary",
        "module_type": "TRANSPORT_STEP",
        "concepts": [
            {
                "preferred_term": "polyamine transport",
                "term": go_term(POLYAMINE_TRANSPORT),
                "description": "Transport of putrescine, spermidine, norspermidine, and related polyamines.",
            },
            {
                "preferred_term": "polyamine binding",
                "term": go_term(POLYAMINE_BINDING),
                "description": "Substrate binding by periplasmic PotF-like polyamine-binding proteins.",
            },
        ],
        "context": {
            "cellular_components": [
                {
                    "preferred_term": "bacterial periplasm",
                    "term": go_term(PERIPLASM),
                    "description": "PotF-like substrate-binding components are predicted periplasmic proteins.",
                }
            ]
        },
        "parts": [
            {
                "order": 1,
                "role": "PotF-like putrescine/polyamine binding components",
                "node": {
                    "id": "potF_like_polyamine_binding_components",
                    "label": "PotF-like putrescine/polyamine binding components",
                    "module_type": "TRANSPORT_STEP",
                    "description": (
                        "These PotF-like proteins are periplasmic putrescine/polyamine substrate-binding "
                        "components identified as ppu02010 singletons or boundary cases. They likely contribute "
                        "substrate recognition to polyamine uptake systems, but matched permease and ATP-binding "
                        "partners have not been assigned in this first-pass partition."
                    ),
                    "concepts": [
                        {
                            "preferred_term": "polyamine transport",
                            "term": go_term(POLYAMINE_TRANSPORT),
                        },
                        {
                            "preferred_term": "polyamine binding",
                            "term": go_term(POLYAMINE_BINDING),
                        },
                    ],
                    "annotons": [module_annoton(gene, cfg) for gene, cfg in MODULE_GENES.items()],
                },
            }
        ],
    }
    doc["notes"] = (
        "This boundary module was seeded from the C17 ppu02010 potF-I checkpoint and expanded after curating "
        "the C30, C43, C49, C53, and C74 PotF-like singleton paralogs. These proteins should remain separate "
        "from neighboring compatible-solute, peptide, or other ABC-importer modules until locus, genetics, or "
        "biochemical evidence establishes their cognate permease/ATPase partners and substrate preferences."
    )
    MODULE_PATH.write_text(yaml.safe_dump(doc, sort_keys=False, width=120))
    print(f"updated {MODULE_PATH}")


def main() -> None:
    for gene, cfg in GENES.items():
        curate_gene(gene, cfg)
    curate_module()


if __name__ == "__main__":
    main()
