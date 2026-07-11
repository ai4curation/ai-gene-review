#!/usr/bin/env python3
"""First-pass curation updates for KEGG ppu04146 peroxisome boundary."""

from __future__ import annotations

from pathlib import Path

import yaml


SPECIES = "PSEPK"
ROOT = Path("genes") / SPECIES


GO_REF_TITLES = {
    "GO_REF:0000002": "Gene Ontology annotation through association of InterPro records with GO terms",
    "GO_REF:0000108": "Automatic assignment of GO terms using logical inference, based on on inter-ontology links",
    "GO_REF:0000117": "Electronic Gene Ontology annotations created by ARBA machine learning models",
    "GO_REF:0000118": "TreeGrafter-generated GO annotations",
    "GO_REF:0000120": "Combined Automated Annotation using Multiple IEA Methods",
}


SODA_REFERENCES = [
    {
        "id": "PMID:10742227",
        "title": "Superoxide dismutase activity in Pseudomonas putida affects utilization of sugars and growth on root surfaces.",
        "findings": [
            {
                "statement": "P. putida sodA encodes manganese-superoxide dismutase; sodA/sodB mutant work supports SOD roles in oxidative-stress and root-surface growth phenotypes.",
                "supporting_text": "mutants of Pseudomonas putida lacking manganese-superoxide\ndismutase (MnSOD) (sodA), iron-superoxide dismutase (FeSOD) (sodB), or both were\ngenerated.",
            }
        ],
    },
    {
        "id": "PMID:14641572",
        "title": "Proteome reference map of Pseudomonas putida strain KT2440 for genome expression profiling: distinct responses of KT2440 and Pseudomonas aeruginosa strain PAO1 to iron deprivation and a new form of superoxide dismutase.",
        "findings": [
            {
                "statement": "KT2440 proteomics reported a SodA/SodB heterodimer under the assayed condition.",
                "supporting_text": "The Sod enzyme of KT2440 was shown to be a novel heterodimer of the\nSodA and SodB polypeptides.",
            }
        ],
    },
]


def support_for(term_id: str, label: str, gene: str) -> dict:
    return {
        "reference_id": f"file:{SPECIES}/{gene}/{gene}-goa.tsv",
        "supporting_text": f"{term_id}\t{label}",
    }


def unique_references(existing: list[dict], gene: str) -> list[dict]:
    refs: list[dict] = []
    seen: set[str] = set()
    for ref in existing:
        ref_id = ref.get("id")
        if not ref_id or ref_id in seen:
            continue
        if ref_id in GO_REF_TITLES:
            ref = {"id": ref_id, "title": GO_REF_TITLES[ref_id], "findings": []}
        refs.append(ref)
        seen.add(ref_id)
    for ref in [
        {
            "id": f"file:{SPECIES}/{gene}/{gene}-uniprot.txt",
            "title": f"UniProtKB entry for {gene}",
            "findings": [
                {
                    "statement": "UniProt identity, protein name, family, and domain metadata used for first-pass pathway curation."
                }
            ],
        },
        {
            "id": f"file:{SPECIES}/{gene}/{gene}-goa.tsv",
            "title": f"QuickGO GOA annotations for {gene}",
            "findings": [
                {"statement": "GOA table containing the annotations reviewed in this file."}
            ],
        },
        {
            "id": f"file:{SPECIES}/{gene}/{gene}-deep-research-asta.md",
            "title": f"Asta retrieval report for {gene}",
            "findings": [
                {
                    "statement": "Asta retrieval used as fast gene-level literature context; no unsupported hypotheses were imported."
                }
            ],
        },
    ]:
        if ref["id"] not in seen:
            refs.append(ref)
            seen.add(ref["id"])
    if gene == "sodA":
        for ref in SODA_REFERENCES:
            if ref["id"] not in seen:
                refs.append(ref)
                seen.add(ref["id"])
    return refs


def curate_soda() -> None:
    gene = "sodA"
    path = ROOT / gene / f"{gene}-ai-review.yaml"
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    data["status"] = "DRAFT"
    data["description"] = (
        "sodA (PP_0946) encodes the manganese-type iron/manganese-family superoxide "
        "dismutase of Pseudomonas putida KT2440. It disproportionates superoxide "
        "radicals to oxygen and hydrogen peroxide as part of cytoplasmic oxidative-stress "
        "defense, and KT2440 proteomics reported a condition-dependent SodA/SodB "
        "heterodimer under iron limitation."
    )

    decisions = {
        "GO:0004784": ("ACCEPT", "superoxide dismutase activity is the core catalytic function of SodA"),
        "GO:0005737": ("ACCEPT", "cytoplasm is appropriate for a soluble bacterial superoxide dismutase"),
        "GO:0006801": (
            "MODIFY",
            "superoxide metabolic process is directionally correct but less specific than removal of superoxide radicals",
            [{"id": "GO:0019430", "label": "removal of superoxide radicals"}],
        ),
        "GO:0019430": ("ACCEPT", "removal of superoxide radicals exactly captures the SOD detoxification process"),
        "GO:0030145": ("ACCEPT", "manganese ion binding matches the SodA/MnSOD assignment and GOA annotation"),
        "GO:0046872": (
            "MODIFY",
            "generic metal ion binding is less informative than the specific manganese cofactor term for SodA",
            [{"id": "GO:0030145", "label": "manganese ion binding"}],
        ),
    }

    for ann in data.get("existing_annotations", []):
        term = ann["term"]
        action, reason, *rest = decisions[term["id"]]
        if action == "ACCEPT":
            summary = f"{term['label']} is supported for SodA in the ppu04146 first-pass curation."
        else:
            summary = f"{term['label']} should be replaced by a more specific term for SodA."
        review = {
            "summary": summary,
            "action": action,
            "reason": reason,
            "supported_by": [support_for(term["id"], term["label"], gene)],
        }
        if term["id"] == "GO:0004784":
            review["additional_reference_ids"] = ["PMID:10742227", "PMID:14641572"]
        if term["id"] == "GO:0019430":
            review["supported_by"].append(
                {
                    "reference_id": "PMID:10742227",
                    "supporting_text": "mutants of Pseudomonas putida lacking manganese-superoxide\ndismutase (MnSOD) (sodA), iron-superoxide dismutase (FeSOD) (sodB), or both were\ngenerated.",
                }
            )
        if rest:
            review["proposed_replacement_terms"] = rest[0]
        ann["review"] = review

    data["core_functions"] = [
        {
            "description": (
                "Manganese-type superoxide dismutase converting superoxide radicals "
                "to oxygen and hydrogen peroxide during cytoplasmic oxidative-stress defense."
            ),
            "molecular_function": {
                "id": "GO:0004784",
                "label": "superoxide dismutase activity",
            },
            "directly_involved_in": [
                {"id": "GO:0019430", "label": "removal of superoxide radicals"}
            ],
            "locations": [{"id": "GO:0005737", "label": "cytoplasm"}],
            "supported_by": [
                support_for("GO:0004784", "superoxide dismutase activity", gene),
                support_for("GO:0019430", "removal of superoxide radicals", gene),
                {
                    "reference_id": "PMID:14641572",
                    "supporting_text": "The Sod enzyme of KT2440 was shown to be a novel heterodimer of the\nSodA and SodB polypeptides.",
                },
            ],
        }
    ]
    data["proposed_new_terms"] = []
    data["suggested_questions"] = [
        {
            "question": "Under which growth and iron-availability conditions does KT2440 SodA act as a homodimer versus the reported SodA/SodB heterodimer?"
        }
    ]
    data["suggested_experiments"] = [
        {
            "description": "Compare native SOD complexes, metal occupancy, and paraquat sensitivity in sodA, sodB, and double mutants under iron-replete and iron-limited growth.",
            "experiment_type": "native protein complex and oxidative-stress phenotype assay",
        }
    ]
    data["references"] = unique_references(data.get("references", []), gene)
    path.write_text(yaml.safe_dump(data, sort_keys=False, width=120), encoding="utf-8")


def main() -> None:
    curate_soda()
    for gene in ["sodB"]:
        path = ROOT / gene / f"{gene}-ai-review.yaml"
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
        data["references"] = unique_references(data.get("references", []), gene)
        path.write_text(yaml.safe_dump(data, sort_keys=False, width=120), encoding="utf-8")


if __name__ == "__main__":
    main()
