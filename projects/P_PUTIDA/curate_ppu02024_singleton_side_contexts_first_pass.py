#!/usr/bin/env python3
"""First-pass curation for the three remaining ppu02024 singleton side contexts."""

from __future__ import annotations

import csv
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[2]
SPECIES = "PSEPK"
GENE_ROOT = ROOT / "genes" / SPECIES


class NoAliasDumper(yaml.SafeDumper):
    def ignore_aliases(self, data):
        return True


GO_REF_TITLES = {
    "GO_REF:0000002": "Gene Ontology annotation through association of InterPro records with GO terms",
    "GO_REF:0000044": "Gene Ontology annotation based on UniProtKB/Swiss-Prot Subcellular Location vocabulary mapping, accompanied by conservative changes to GO terms applied by UniProt",
    "GO_REF:0000104": "Electronic Gene Ontology annotations created by transferring manual GO annotations between related proteins based on shared sequence features",
    "GO_REF:0000118": "TreeGrafter-generated GO annotations",
    "GO_REF:0000120": "Combined Automated Annotation using Multiple IEA Methods",
}

TRANSCRIPTION_CIS_REG_BINDING = {"id": "GO:0000976", "label": "transcription cis-regulatory region binding"}
DNA_BINDING = {"id": "GO:0003677", "label": "DNA binding"}
DNA_BINDING_TF_ACTIVITY = {"id": "GO:0003700", "label": "DNA-binding transcription factor activity"}
CYTOPLASM = {"id": "GO:0005737", "label": "cytoplasm"}
CYTOSOL = {"id": "GO:0005829", "label": "cytosol"}
TRANSCRIPTION_REGULATION = {"id": "GO:0006355", "label": "regulation of DNA-templated transcription"}
ZINC_BINDING = {"id": "GO:0008270", "label": "zinc ion binding"}
NEGATIVE_TRANSCRIPTION_REGULATION = {
    "id": "GO:0045892",
    "label": "negative regulation of DNA-templated transcription",
}
SECONDARY_METABOLITE_REGULATION = {
    "id": "GO:1900376",
    "label": "regulation of secondary metabolite biosynthetic process",
}
IRON_HOMEOSTASIS = {"id": "GO:0006879", "label": "intracellular iron ion homeostasis"}
CELL_ADHESION = {"id": "GO:0007155", "label": "cell adhesion"}
PLASMA_MEMBRANE = {"id": "GO:0005886", "label": "plasma membrane"}
TRANSMEMBRANE_TRANSPORTER = {"id": "GO:0022857", "label": "transmembrane transporter activity"}
TRANSMEMBRANE_TRANSPORT = {"id": "GO:0055085", "label": "transmembrane transport"}


GENES = {
    "fur__Q88RL0": {
        "accession": "Q88RL0",
        "locus": "PP_0119",
        "bucket": "fur_iron_regulation_spillover",
        "module": "iron_homeostasis_regulation_boundary",
        "kind": "fur",
        "description": (
            "fur__Q88RL0 (PP_0119) encodes a Fur-family ferric uptake regulation protein in Pseudomonas "
            "putida KT2440. It is a predicted cytoplasmic DNA-binding transcriptional regulator with FUR "
            "and winged-helix DNA-binding domains, supporting iron-responsive repression/regulation rather "
            "than direct quorum-signal synthesis or reception."
        ),
        "product_text": "Full=Ferric uptake regulation protein",
        "domain_text": "FUR.",
        "family_text": "Belongs to the Fur family.",
        "location_text": "SUBCELLULAR LOCATION: Cytoplasm",
        "asta_text": "Protein Description:** RecName: Full=Ferric uptake regulation protein",
    },
    "PP_0806": {
        "accession": "Q88PP2",
        "locus": "PP_0806",
        "bucket": "surface_adhesion_singleton",
        "module": "surface_adhesion_boundary",
        "kind": "adhesion",
        "description": (
            "PP_0806 encodes a very large predicted surface adhesion protein in Pseudomonas putida KT2440. "
            "UniProt product naming plus BapA/Bap-like, Big, Ig-like, and serralysin-like C-terminal domain "
            "features support broad cell-surface adhesion or biofilm-boundary context, but no direct quorum "
            "signal-synthesis or signal-receptor role is established."
        ),
        "product_text": "Full=Surface adhesion protein",
        "domain_text": "BapA-like_prefix-like.",
        "domain_text_2": "Ig-like_fold.",
        "asta_text": "Protein Description:** SubName: Full=Surface adhesion protein",
    },
    "PP_3609": {
        "accession": "Q88GV8",
        "locus": "PP_3609",
        "bucket": "dmt_transporter_singleton",
        "module": "dmt_transporter_boundary",
        "kind": "dmt",
        "description": (
            "PP_3609 encodes a small predicted DMT/YdcZ-family multi-pass membrane transporter in Pseudomonas "
            "putida KT2440. Current evidence supports plasma-membrane localization and generic transmembrane "
            "transport capability, while the transported substrate and any relationship to quorum-sensing "
            "biology remain unresolved."
        ),
        "product_text": "Full=DMT family transporter",
        "domain_text": "YdcZ.",
        "pfam_text": "DMT_YdcZ",
        "tm_text": "FT   TRANSMEM        44..69",
        "asta_text": "Protein Description:** RecName: Full=DMT family transporter",
    },
}


def go_term(term: dict[str, str]) -> dict[str, str]:
    return {"id": term["id"], "label": term["label"]}


def file_ref(gene: str, suffix: str) -> str:
    return f"file:{SPECIES}/{gene}/{gene}-{suffix}"


def support(reference_id: str, supporting_text: str) -> dict[str, str]:
    return {"reference_id": reference_id, "supporting_text": supporting_text}


def support_uniprot(gene: str, text: str) -> dict[str, str]:
    return support(file_ref(gene, "uniprot.txt"), text)


def support_asta(gene: str, text: str) -> dict[str, str]:
    return support(file_ref(gene, "deep-research-asta.md"), text)


def goa_rows(gene: str) -> dict[str, dict[str, str]]:
    with (GENE_ROOT / gene / f"{gene}-goa.tsv").open(encoding="utf-8") as handle:
        return {row["GO TERM"]: row for row in csv.DictReader(handle, delimiter="\t")}


def goa_quote(row: dict[str, str]) -> str:
    return f"{row['GO TERM']}\t{row['GO NAME']}"


def support_goa(gene: str, rows: dict[str, dict[str, str]], term_id: str) -> dict[str, str]:
    return support(file_ref(gene, "goa.tsv"), goa_quote(rows[term_id]))


def review(
    summary: str,
    action: str,
    reason: str,
    supported_by: list[dict[str, str]],
    proposed: list[dict[str, str]] | None = None,
) -> dict:
    result = {
        "summary": summary,
        "action": action,
        "reason": reason,
        "supported_by": supported_by,
    }
    if proposed:
        result["proposed_replacement_terms"] = proposed
    return result


def ensure_references(data: dict, gene: str, cfg: dict) -> None:
    refs = {entry["id"]: entry for entry in data.get("references", [])}
    for ref_id, title in GO_REF_TITLES.items():
        refs.setdefault(ref_id, {"id": ref_id, "title": title, "findings": []})

    findings = [{"statement": "UniProt product naming supports the first-pass assignment.", "supporting_text": cfg["product_text"]}]
    if cfg["kind"] == "fur":
        findings.extend(
            [
                {"statement": "FUR domain annotation supports a Fur-family transcription-regulator role.", "supporting_text": cfg["domain_text"]},
                {"statement": "UniProt places this regulator in the bacterial cytoplasm.", "supporting_text": cfg["location_text"]},
            ]
        )
    elif cfg["kind"] == "adhesion":
        findings.extend(
            [
                {"statement": "BapA-like domain context supports surface-adhesion/biofilm-boundary assignment.", "supporting_text": cfg["domain_text"]},
                {"statement": "Ig-like repeats support a large cell-surface adhesion protein architecture.", "supporting_text": cfg["domain_text_2"]},
            ]
        )
    else:
        findings.extend(
            [
                {"statement": "YdcZ/DMT family annotation supports a small membrane-transporter role.", "supporting_text": cfg["domain_text"]},
                {"statement": "Predicted transmembrane helices support membrane transporter topology.", "supporting_text": cfg["tm_text"]},
            ]
        )

    refs[file_ref(gene, "goa.tsv")] = {
        "id": file_ref(gene, "goa.tsv"),
        "title": f"QuickGO/GOA annotation table for {gene} in Pseudomonas putida KT2440",
        "findings": [],
    }
    refs[file_ref(gene, "uniprot.txt")] = {
        "id": file_ref(gene, "uniprot.txt"),
        "title": f"UniProt record {cfg['accession']} for {gene} in Pseudomonas putida KT2440",
        "findings": findings,
    }
    refs[file_ref(gene, "deep-research-asta.md")] = {
        "id": file_ref(gene, "deep-research-asta.md"),
        "title": f"Asta retrieval report for {gene} in Pseudomonas putida KT2440",
        "findings": [
            {
                "statement": "Asta retrieval was checked for this first pass and recapitulates the UniProt product assignment.",
                "supporting_text": cfg["asta_text"],
            }
        ],
    }
    data["references"] = list(refs.values())


def fur_support(gene: str, cfg: dict, rows: dict[str, dict[str, str]], term_id: str) -> list[dict[str, str]]:
    return [
        support_goa(gene, rows, term_id),
        support_uniprot(gene, cfg["product_text"]),
        support_uniprot(gene, cfg["domain_text"]),
        support_asta(gene, cfg["asta_text"]),
    ]


def fur_review(gene: str, cfg: dict, rows: dict[str, dict[str, str]], term_id: str) -> dict:
    if term_id == "GO:0000976":
        return review(
            "Cis-regulatory-region binding is appropriate for this Fur-family transcription regulator.",
            "ACCEPT",
            "The FUR and winged-helix DNA-binding domains support binding to regulatory DNA regions.",
            fur_support(gene, cfg, rows, term_id),
        )
    if term_id == "GO:0003677":
        return review(
            "DNA binding is true but less informative than cis-regulatory-region binding and transcription-factor activity.",
            "MARK_AS_OVER_ANNOTATED",
            "The same record has more specific transcriptional regulatory DNA-binding annotations.",
            fur_support(gene, cfg, rows, term_id),
        )
    if term_id == "GO:0003700":
        return review(
            "DNA-binding transcription factor activity is appropriate for this Fur-family regulator.",
            "ACCEPT",
            "The Fur-family product and DNA-binding domains support transcriptional regulatory activity.",
            fur_support(gene, cfg, rows, term_id),
        )
    if term_id == "GO:0005737":
        return review(
            "Cytoplasmic localization is appropriate for this bacterial transcription regulator.",
            "ACCEPT",
            "UniProt places the Fur-family regulator in the cytoplasm.",
            [support_goa(gene, rows, term_id), support_uniprot(gene, cfg["location_text"])],
        )
    if term_id == "GO:0005829":
        return review(
            "Cytosol localization is compatible with the bacterial cytoplasmic Fur-family regulator.",
            "KEEP_AS_NON_CORE",
            "Cytosol is compatible with cytoplasmic transcriptional regulation, but localization is not the core function.",
            [support_goa(gene, rows, term_id), support_uniprot(gene, cfg["location_text"])],
        )
    if term_id == "GO:0006355":
        return review(
            "Regulation of DNA-templated transcription is appropriate broad process context.",
            "ACCEPT",
            "Fur-family proteins are DNA-binding transcriptional regulators; this broad process captures the regulator role.",
            fur_support(gene, cfg, rows, term_id),
        )
    if term_id == "GO:0008270":
        return review(
            "Zinc ion binding is plausible Fur-family metal-binding context but not the main biological role.",
            "KEEP_AS_NON_CORE",
            "Fur-family regulators bind metal cofactors, but the primary curated role is iron-responsive transcriptional regulation.",
            fur_support(gene, cfg, rows, term_id),
        )
    if term_id == "GO:0045892":
        return review(
            "Negative regulation of DNA-templated transcription is appropriate for this predicted Fur-family repressor.",
            "ACCEPT",
            "The Fur-family product, repressor keyword, and regulatory DNA-binding domains support transcriptional repression context.",
            fur_support(gene, cfg, rows, term_id) + [support_uniprot(gene, "Repressor")],
        )
    if term_id == "GO:1900376":
        return review(
            "Regulation of secondary-metabolite biosynthesis is plausible siderophore/iron side context but not the core annotation.",
            "KEEP_AS_NON_CORE",
            "Fur regulators can regulate siderophore and other iron-responsive secondary-metabolite genes, but the term is broad and pathway-contextual.",
            fur_support(gene, cfg, rows, term_id),
        )
    raise KeyError(f"Unhandled Fur term {term_id}")


def dmt_review(gene: str, cfg: dict, rows: dict[str, dict[str, str]], term_id: str) -> dict:
    if term_id == "GO:0005886":
        return review(
            "Plasma membrane localization is appropriate for this predicted multi-pass DMT/YdcZ-family transporter.",
            "ACCEPT",
            "The YdcZ/DMT family assignment and predicted transmembrane helices support bacterial plasma-membrane localization.",
            [
                support_goa(gene, rows, term_id),
                support_uniprot(gene, cfg["product_text"]),
                support_uniprot(gene, cfg["domain_text"]),
                support_uniprot(gene, cfg["tm_text"]),
                support_asta(gene, cfg["asta_text"]),
            ],
        )
    raise KeyError(f"Unhandled DMT term {term_id}")


def new_annotation(term: dict[str, str], qualifier: str, gene: str, cfg: dict, summary: str, reason: str, extra: list[dict[str, str]]) -> dict:
    return {
        "term": go_term(term),
        "evidence_type": "IEA",
        "original_reference_id": file_ref(gene, "uniprot.txt"),
        "qualifier": qualifier,
        "review": {
            "summary": summary,
            "action": "NEW",
            "reason": reason,
            "supported_by": [support_uniprot(gene, cfg["product_text"]), support_asta(gene, cfg["asta_text"]), *extra],
        },
    }


def maybe_new_annotations(data: dict, gene: str, cfg: dict) -> None:
    existing_ids = {ann["term"]["id"] for ann in data.get("existing_annotations", [])}
    additions = []
    if cfg["kind"] == "fur" and IRON_HOMEOSTASIS["id"] not in existing_ids:
        additions.append(
            new_annotation(
                IRON_HOMEOSTASIS,
                "involved_in",
                gene,
                cfg,
                "Intracellular iron ion homeostasis is a missing process annotation for this Fur-family regulator.",
                "The ferric uptake regulator product, FUR domains, and iron/repressor context support iron-homeostasis regulation as the side-context process.",
                [support_uniprot(gene, cfg["domain_text"]), support_uniprot(gene, "Iron"), support_uniprot(gene, "Repressor")],
            )
        )
    if cfg["kind"] == "adhesion" and CELL_ADHESION["id"] not in existing_ids:
        additions.append(
            new_annotation(
                CELL_ADHESION,
                "involved_in",
                gene,
                cfg,
                "Cell adhesion is a missing broad process annotation for this large BapA/Bap-like surface adhesion protein.",
                "The product name and BapA/Bap-like, Big, and Ig-like domain architecture support surface-adhesion/biofilm-boundary context.",
                [support_uniprot(gene, cfg["domain_text"]), support_uniprot(gene, cfg["domain_text_2"])],
            )
        )
    if cfg["kind"] == "dmt":
        if TRANSMEMBRANE_TRANSPORTER["id"] not in existing_ids:
            additions.append(
                new_annotation(
                    TRANSMEMBRANE_TRANSPORTER,
                    "enables",
                    gene,
                    cfg,
                    "Transmembrane transporter activity is a missing molecular-function annotation for this DMT/YdcZ-family membrane protein.",
                    "The DMT/YdcZ family assignment and predicted multi-pass topology support a generic transporter activity while substrate remains unresolved.",
                    [support_uniprot(gene, cfg["domain_text"]), support_uniprot(gene, cfg["tm_text"])],
                )
            )
        if TRANSMEMBRANE_TRANSPORT["id"] not in existing_ids:
            additions.append(
                new_annotation(
                    TRANSMEMBRANE_TRANSPORT,
                    "involved_in",
                    gene,
                    cfg,
                    "Transmembrane transport is a missing broad process annotation for this DMT/YdcZ-family transporter.",
                    "Current evidence supports membrane transport but does not resolve the transported substrate.",
                    [support_uniprot(gene, cfg["domain_text"]), support_uniprot(gene, cfg["tm_text"])],
                )
            )
    data.setdefault("existing_annotations", []).extend(additions)


def core_functions(gene: str, cfg: dict) -> list[dict]:
    if cfg["kind"] == "fur":
        return [
            {
                "description": "Fur-family DNA-binding transcriptional regulator for iron-responsive homeostasis context.",
                "molecular_function": go_term(DNA_BINDING_TF_ACTIVITY),
                "directly_involved_in": [go_term(NEGATIVE_TRANSCRIPTION_REGULATION), go_term(IRON_HOMEOSTASIS)],
                "locations": [go_term(CYTOPLASM)],
                "supported_by": [
                    support_uniprot(gene, cfg["product_text"]),
                    support_uniprot(gene, cfg["domain_text"]),
                    support_uniprot(gene, cfg["location_text"]),
                    support_asta(gene, cfg["asta_text"]),
                ],
            }
        ]
    if cfg["kind"] == "adhesion":
        return [
            {
                "description": "Large BapA/Bap-like surface adhesion protein assigned to broad cell-adhesion/biofilm-boundary context.",
                "directly_involved_in": [go_term(CELL_ADHESION)],
                "supported_by": [
                    support_uniprot(gene, cfg["product_text"]),
                    support_uniprot(gene, cfg["domain_text"]),
                    support_uniprot(gene, cfg["domain_text_2"]),
                    support_asta(gene, cfg["asta_text"]),
                ],
            }
        ]
    return [
        {
            "description": "Small DMT/YdcZ-family multi-pass membrane transporter with unresolved substrate.",
            "molecular_function": go_term(TRANSMEMBRANE_TRANSPORTER),
            "directly_involved_in": [go_term(TRANSMEMBRANE_TRANSPORT)],
            "locations": [go_term(PLASMA_MEMBRANE)],
            "supported_by": [
                support_uniprot(gene, cfg["product_text"]),
                support_uniprot(gene, cfg["domain_text"]),
                support_uniprot(gene, cfg["tm_text"]),
                support_asta(gene, cfg["asta_text"]),
            ],
        }
    ]


def suggested_questions(gene: str, cfg: dict) -> list[dict[str, str]]:
    if cfg["kind"] == "fur":
        question = f"What regulon and metal responsiveness distinguish {gene}/PP_0119 from the second KT2440 Fur-family paralog Q88DT9/PP_4730?"
    elif cfg["kind"] == "adhesion":
        question = "What cell-surface structure, secretion route, and biofilm or attachment phenotype are mediated by PP_0806?"
    else:
        question = "What substrate is transported by PP_3609, and is it connected to any ppu02024-associated signaling or biofilm condition?"
    return [{"question": question}]


def suggested_experiments(gene: str, cfg: dict) -> list[dict[str, str]]:
    if cfg["kind"] == "fur":
        return [
            {
                "description": f"Compare {gene}/PP_0119 and PP_4730 Fur-family mutants by RNA-seq and ChIP-seq under iron-replete and iron-limited growth.",
                "experiment_type": "comparative Fur-family regulon mapping",
            }
        ]
    if cfg["kind"] == "adhesion":
        return [
            {
                "description": "Test PP_0806 deletion and complementation for surface attachment, biofilm biomass, cell aggregation, and localization/secretion of the large adhesion protein.",
                "experiment_type": "surface-adhesion and biofilm phenotype assay",
            }
        ]
    return [
        {
            "description": "Screen PP_3609 deletion and complemented strains for altered uptake or sensitivity across candidate DMT-family substrates and membrane-stress conditions.",
            "experiment_type": "targeted unresolved-transporter substrate screen",
        }
    ]


def curate_gene(gene: str, cfg: dict) -> None:
    path = GENE_ROOT / gene / f"{gene}-ai-review.yaml"
    data = yaml.safe_load(path.read_text())
    rows = goa_rows(gene)

    data["gene_symbol"] = gene
    data["status"] = "DRAFT"
    data["description"] = cfg["description"]
    ensure_references(data, gene, cfg)

    for ann in data.get("existing_annotations", []):
        if ann.get("review", {}).get("action") == "NEW":
            continue
        term_id = ann["term"]["id"]
        if cfg["kind"] == "fur":
            ann["review"] = fur_review(gene, cfg, rows, term_id)
        elif cfg["kind"] == "dmt":
            ann["review"] = dmt_review(gene, cfg, rows, term_id)
        else:
            raise KeyError(f"Unexpected existing annotation for {gene}: {term_id}")

    maybe_new_annotations(data, gene, cfg)
    data["core_functions"] = core_functions(gene, cfg)
    data["proposed_new_terms"] = []
    data["suggested_questions"] = suggested_questions(gene, cfg)
    data["suggested_experiments"] = suggested_experiments(gene, cfg)
    path.write_text(yaml.dump(data, Dumper=NoAliasDumper, sort_keys=False, width=1000))
    print(f"curated {path}")


def preferred(term: dict[str, str], description: str | None = None) -> dict:
    entry = {"preferred_term": term["label"], "term": go_term(term)}
    if description:
        entry["description"] = description
    return entry


def module_doc(gene: str, cfg: dict) -> dict:
    if cfg["kind"] == "fur":
        concepts = [
            preferred(DNA_BINDING_TF_ACTIVITY, "Fur-family transcription regulatory activity."),
            preferred(NEGATIVE_TRANSCRIPTION_REGULATION, "Repression/regulation of target genes."),
            preferred(IRON_HOMEOSTASIS, "Iron-homeostasis side context for the Fur-family regulator."),
        ]
        annoton = {
            "id": "fur_Q88RL0_iron_regulation_annoton",
            "label": "fur__Q88RL0: Fur-family iron-homeostasis regulator",
            "participant": {"selector_type": "GENE", "gene": {"preferred_term": gene}},
            "function": preferred(DNA_BINDING_TF_ACTIVITY),
            "processes": [preferred(NEGATIVE_TRANSCRIPTION_REGULATION), preferred(IRON_HOMEOSTASIS)],
            "locations": [preferred(CYTOPLASM)],
            "role_description": "Fur-family DNA-binding transcription regulator; side-context for ppu02024.",
        }
        title = "Iron homeostasis regulation boundary"
        desc = "Boundary module for the ppu02024 Fur-family PP_0119/fur__Q88RL0 side-context gene."
        module_type = "REGULATORY_STEP"
    elif cfg["kind"] == "adhesion":
        concepts = [preferred(CELL_ADHESION, "Broad cell-adhesion process for a large BapA/Bap-like surface protein.")]
        annoton = {
            "id": "PP_0806_surface_adhesion_annoton",
            "label": "PP_0806: large surface adhesion protein",
            "participant": {"selector_type": "GENE", "gene": {"preferred_term": gene}},
            "processes": [preferred(CELL_ADHESION)],
            "role_description": "BapA/Bap-like surface-adhesion/biofilm-boundary protein; not direct quorum-signal reception.",
        }
        title = "Surface adhesion boundary"
        desc = "Boundary module for the ppu02024 PP_0806 large surface-adhesion singleton."
        module_type = "BIOLOGICAL_PROCESS"
    else:
        concepts = [
            preferred(TRANSMEMBRANE_TRANSPORTER, "Generic transporter activity for unresolved DMT/YdcZ-family substrate."),
            preferred(TRANSMEMBRANE_TRANSPORT, "Broad transport process pending substrate evidence."),
        ]
        annoton = {
            "id": "PP_3609_dmt_transporter_annoton",
            "label": "PP_3609: DMT/YdcZ-family transporter",
            "participant": {"selector_type": "GENE", "gene": {"preferred_term": gene}},
            "function": preferred(TRANSMEMBRANE_TRANSPORTER),
            "processes": [preferred(TRANSMEMBRANE_TRANSPORT)],
            "locations": [preferred(PLASMA_MEMBRANE)],
            "role_description": "Small DMT/YdcZ-family membrane transporter with unresolved substrate.",
        }
        title = "DMT transporter boundary"
        desc = "Boundary module for the ppu02024 PP_3609 DMT/YdcZ-family transporter singleton."
        module_type = "TRANSPORT_STEP"
    return {
        "id": f"MODULE:{cfg['module']}",
        "title": title,
        "description": desc + " This module records ppu02024 side context and is not evidence for direct quorum sensing.",
        "status": "DRAFT",
        "evidence": [
            {
                "source_id": "KEGG:ppu02024",
                "title": "Quorum sensing - Pseudomonas putida KT2440",
                "statement": "KEGG ppu02024 includes this singleton, but the primary evidence supports side-context biology rather than LuxI/LuxR-type quorum sensing.",
            },
            {
                "source_id": f"UniProtKB:{cfg['accession']}",
                "title": f"{gene} {cfg['product_text'].replace('Full=', '')}",
                "statement": f"UniProt records {gene} ({cfg['locus']}) as {cfg['product_text'].replace('Full=', '')}.",
            },
        ],
        "module": {
            "id": cfg["module"],
            "label": title,
            "module_type": module_type,
            "concepts": concepts,
            "parts": [
                {
                    "order": 1,
                    "role": cfg["bucket"],
                    "node": {
                        "id": cfg["bucket"],
                        "label": title,
                        "module_type": module_type,
                        "annotons": [annoton],
                    },
                }
            ],
        },
        "notes": "Created during ppu02024 closure as a singleton side-context boundary module.",
    }


def write_modules() -> None:
    for gene, cfg in GENES.items():
        path = ROOT / "modules" / f"{cfg['module']}.yaml"
        path.write_text(yaml.dump(module_doc(gene, cfg), Dumper=NoAliasDumper, sort_keys=False, width=1000))
        print(f"wrote {path}")


def main() -> None:
    for gene, cfg in GENES.items():
        curate_gene(gene, cfg)
    write_modules()


if __name__ == "__main__":
    main()
