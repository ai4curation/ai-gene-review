#!/usr/bin/env python3
"""First-pass curation for ppu02010 C69 plpB/NlpA-family lipoprotein."""

from __future__ import annotations

from pathlib import Path

import yaml


SPECIES = "PSEPK"
GENE = "plpB"
GENE_DIR = Path("genes") / SPECIES / GENE
REVIEW_PATH = GENE_DIR / f"{GENE}-ai-review.yaml"


def ref(kind: str) -> str:
    return f"file:{SPECIES}/{GENE}/{GENE}-{kind}"


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


def main() -> None:
    doc = yaml.safe_load(REVIEW_PATH.read_text())
    doc["status"] = "DRAFT"
    doc["description"] = (
        "plpB encodes a predicted membrane-anchored NlpA-family lipoprotein in "
        "Pseudomonas putida KT2440. The current record supports lipoprotein "
        "membrane localization and periplasmic-binding-protein-like family context, "
        "but does not establish a transported substrate or a direct role in the "
        "neighboring sulfate/thiosulfate ABC importer."
    )

    for annotation in doc.get("existing_annotations", []):
        term = annotation.get("term", {})
        if term.get("id") == "GO:0016020":
            annotation["review"] = {
                "summary": "Membrane localization is appropriate for this predicted NlpA-family lipoprotein but is not a specific functional annotation.",
                "action": "KEEP_AS_NON_CORE",
                "reason": (
                    "UniProt annotates plpB as membrane-associated and lipid-anchored. "
                    "The NlpA/MetQ-family context suggests a lipoprotein/periplasmic-binding-protein-like fold, "
                    "but the record does not support assigning sulfate import, methionine import, or another specific substrate."
                ),
                "supported_by": [
                    {"reference_id": ref("goa.tsv"), "supporting_text": "GO:0016020\tmembrane"},
                    {"reference_id": ref("uniprot.txt"), "supporting_text": "SUBCELLULAR LOCATION: Membrane"},
                    {"reference_id": ref("uniprot.txt"), "supporting_text": "Lipid-anchor"},
                    {"reference_id": ref("uniprot.txt"), "supporting_text": "Belongs to the NlpA lipoprotein family."},
                    {"reference_id": ref("uniprot.txt"), "supporting_text": "PANTHER; PTHR30429:SF0; METHIONINE-BINDING LIPOPROTEIN METQ; 1."},
                    {"reference_id": ref("deep-research-asta.md"), "supporting_text": "protein_family: Belongs to the NlpA lipoprotein family."},
                ],
            }

    ensure_reference(doc, ref("goa.tsv"), "QuickGO GOA annotations for plpB")
    ensure_reference(doc, ref("uniprot.txt"), "UniProtKB entry for plpB (Q88CL5)", "Full=NLPA lipoprotein")
    ensure_reference(
        doc,
        ref("deep-research-asta.md"),
        "Asta retrieval report for plpB (Q88CL5)",
        "protein_family: Belongs to the NlpA lipoprotein family.",
    )
    doc["core_functions"] = []
    doc["proposed_new_terms"] = []
    doc["suggested_questions"] = [
        {
            "question": (
                "Does plpB encode a substrate-binding lipoprotein for a specific ABC importer in KT2440, "
                "and if so is its substrate methionine, another amino acid, or an unrelated envelope ligand?"
            )
        },
        {
            "question": (
                "Is the proximity of plpB to the cysA/cysW/cysU/sbp-II sulfate-import locus functionally relevant, "
                "or only a locus-neighborhood artifact in the broad ppu02010 ABC-transporter partition?"
            )
        },
    ]
    doc["suggested_experiments"] = [
        {
            "description": (
                "Test plpB deletion and complementation for growth or uptake phenotypes under sulfate, thiosulfate, "
                "methionine, and other sulfur/amino-acid limitation conditions, separately from cysA/cysW/cysU/sbp-II mutants."
            ),
            "experiment_type": "targeted lipoprotein substrate and transporter-context phenotyping",
        }
    ]
    REVIEW_PATH.write_text(yaml.safe_dump(doc, sort_keys=False, width=120))
    print(f"curated {REVIEW_PATH}")


if __name__ == "__main__":
    main()
