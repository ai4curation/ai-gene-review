#!/usr/bin/env python3
"""First-pass curation for PSEPK small phage lysis/regulatory mobile-element splits."""

from __future__ import annotations

from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[2]
GENE_ROOT = ROOT / "genes" / "PSEPK"
LYSIS_MODULE = ROOT / "modules" / "phage_lysis_host_interaction_boundary.yaml"
REG_MODULE = ROOT / "modules" / "phage_regulation_toxin_antitoxin_boundary.yaml"


class NoAliasDumper(yaml.SafeDumper):
    def ignore_aliases(self, data):
        return True


TERM = {
    "GO:0003676": {"id": "GO:0003676", "label": "nucleic acid binding"},
    "GO:0003677": {"id": "GO:0003677", "label": "DNA binding"},
    "GO:0004519": {"id": "GO:0004519", "label": "endonuclease activity"},
    "GO:0006351": {"id": "GO:0006351", "label": "DNA-templated transcription"},
    "GO:0006355": {"id": "GO:0006355", "label": "regulation of DNA-templated transcription"},
    "GO:0008270": {"id": "GO:0008270", "label": "zinc ion binding"},
    "GO:0090729": {"id": "GO:0090729", "label": "toxin activity"},
}

LYSIS_GENES = ["PP_1561", "PP_4858"]
REG_GENES = ["PP_2500", "PP_5558", "PP_5626"]
GENES = LYSIS_GENES + REG_GENES


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def optional_first_line(path: Path, *needles: str) -> str | None:
    if not path.exists():
        return None
    for line in read_text(path).splitlines():
        if all(needle in line for needle in needles):
            return line
    return None


def support(reference_id: str, text: str | None) -> dict[str, str] | None:
    if not text:
        return None
    return {"reference_id": reference_id, "supporting_text": text}


def add_unique(items: list[dict[str, str]], item: dict[str, str] | None) -> None:
    if item and item not in items:
        items.append(item)


def file_id(gene: str, suffix: str) -> str:
    return f"file:PSEPK/{gene}/{gene}-{suffix}"


def gene_file(gene: str, suffix: str) -> Path:
    return GENE_ROOT / gene / f"{gene}-{suffix}"


def product_line(gene: str) -> str | None:
    path = gene_file(gene, "uniprot.txt")
    return optional_first_line(path, "DE   RecName") or optional_first_line(path, "DE   SubName")


def goa_line(gene: str, term_id: str) -> str | None:
    return optional_first_line(gene_file(gene, "goa.tsv"), term_id)


def evidence_for(gene: str, term_id: str | None = None, domain_needles: tuple[str, ...] = ()) -> list[dict[str, str]]:
    path = gene_file(gene, "uniprot.txt")
    items: list[dict[str, str]] = []
    if term_id:
        add_unique(items, support(file_id(gene, "goa.tsv"), goa_line(gene, term_id)))
    add_unique(items, support(file_id(gene, "uniprot.txt"), product_line(gene)))
    if term_id:
        add_unique(items, support(file_id(gene, "uniprot.txt"), optional_first_line(path, f"DR   GO; {term_id};")))
    for needle in domain_needles:
        add_unique(items, support(file_id(gene, "uniprot.txt"), optional_first_line(path, needle)))
    for marker in (
        "Belongs to the RelE toxin family",
        "DR   PANTHER; PTHR33755",
        "KW   Toxin-antitoxin system",
        "KW   Signal",
    ):
        add_unique(items, support(file_id(gene, "uniprot.txt"), optional_first_line(path, marker)))
    asta = gene_file(gene, "deep-research-asta.md")
    add_unique(items, support(file_id(gene, "deep-research-asta.md"), optional_first_line(asta, "uniprot_accession:")))
    add_unique(items, support(file_id(gene, "deep-research-asta.md"), optional_first_line(asta, "protein_description:")))
    add_unique(items, support(file_id(gene, "deep-research-asta.md"), optional_first_line(asta, "protein_family:")))
    add_unique(items, support(file_id(gene, "deep-research-asta.md"), optional_first_line(asta, "protein_domains:")))
    return items


def description_for(gene: str) -> str:
    product = (product_line(gene) or "mobile-element protein").removeprefix("DE   ").rstrip(".")
    if gene == "PP_1561":
        return (
            f"{gene} encodes a small prophage-associated HNH nuclease-domain protein ({product}). Although the product "
            "name mentions holin, the supported molecular features are nucleic-acid binding, endonuclease activity, and "
            "zinc binding from the HNH nuclease domain."
        )
    if gene == "PP_4858":
        return (
            f"{gene} encodes a predicted phage infection protein ({product}) with a signal peptide but no conserved "
            "family, domain, or GO support in the local record. Its role in host interaction remains unresolved."
        )
    if gene == "PP_2500":
        return (
            f"{gene} encodes a RelE/ParE-family toxin-antitoxin protein ({product}). Domain, family, and keyword evidence "
            "support a type-II toxin role in mobile-element or plasmid-stabilization context, while the precise cellular "
            "target is unresolved."
        )
    if gene == "PP_5558":
        return (
            f"{gene} encodes an XRE-family phage-origin DNA-binding protein ({product}). Its lambda-like DNA-binding "
            "domain supports phage regulatory DNA-binding context."
        )
    return (
        f"{gene} encodes a phage repressor-like Cro/C1-type helix-turn-helix DNA-binding protein ({product}). It is "
        "associated with phage regulatory DNA binding and regulation of DNA-templated transcription."
    )


def ensure_references(data: dict, gene: str) -> None:
    refs = data.setdefault("references", [])
    by_id = {ref.get("id"): ref for ref in refs}
    local_refs = [
        (
            file_id(gene, "uniprot.txt"),
            f"UniProtKB entry for {gene}",
            product_line(gene),
            "UniProt provides product, GO cross-reference, family, and domain context used in this first-pass review.",
        ),
        (
            file_id(gene, "goa.tsv"),
            f"QuickGO GOA annotations for {gene}",
            None,
            "The fetched GOA table contains the machine-sourced annotations reviewed for this gene.",
        ),
        (
            file_id(gene, "deep-research-asta.md"),
            f"Asta retrieval report for {gene}",
            optional_first_line(gene_file(gene, "deep-research-asta.md"), "uniprot_accession:"),
            "Asta retrieval was generated for this first-pass review and used as lightweight identity/retrieval context.",
        ),
    ]
    for ref_id, title, quote, statement in local_refs:
        if ref_id in by_id:
            continue
        finding = {"statement": statement}
        if quote:
            finding["supporting_text"] = quote
        refs.append({"id": ref_id, "title": title, "findings": [finding]})


def review_for(gene: str, term_id: str) -> dict:
    if gene == "PP_1561" and term_id == "GO:0004519":
        return {
            "summary": "Endonuclease activity is the supported catalytic molecular function for this HNH-domain protein.",
            "action": "ACCEPT",
            "reason": "The fetched GOA row and UniProt InterPro/Pfam records consistently identify an HNH nuclease domain. This is stronger than the holin product name for molecular-function curation.",
            "supported_by": evidence_for(gene, term_id, ("HNH.", "HNH_nuc", "PF01844")),
        }
    if gene == "PP_1561" and term_id == "GO:0003676":
        return {
            "summary": "Nucleic acid binding is compatible with the HNH nuclease domain but is less specific than endonuclease activity.",
            "action": "KEEP_AS_NON_CORE",
            "reason": "The broad substrate-binding term is retained as context for the HNH nuclease-family protein, while endonuclease activity is the more informative molecular-function call.",
            "supported_by": evidence_for(gene, term_id, ("HNH.", "HNH_nuc", "PF01844")),
        }
    if gene == "PP_1561" and term_id == "GO:0008270":
        return {
            "summary": "Zinc ion binding is compatible with the HNH nuclease domain but is not the core functional call.",
            "action": "KEEP_AS_NON_CORE",
            "reason": "The InterPro-derived zinc-binding annotation reflects the HNH nuclease domain architecture. It is retained as cofactor/domain context rather than the main function.",
            "supported_by": evidence_for(gene, term_id, ("HNH.", "HNH_nuc", "PF01844")),
        }
    if gene == "PP_2500" and term_id == "GO:0090729":
        return {
            "summary": "Toxin activity is supported by RelE/ParE toxin-family and toxin-antitoxin-system evidence.",
            "action": "NEW",
            "reason": "The local UniProt record has no GOA rows, but InterPro, PANTHER, Pfam, family, and keyword evidence all support a type-II toxin-antitoxin toxin role. A generic toxin-activity term is used because the precise cellular target is not resolved.",
            "supported_by": evidence_for(gene, None, ("RelE/ParE_toxin", "TA_system_RelE-like_toxin", "ParE_toxin")),
        }
    if gene in {"PP_5558", "PP_5626"} and term_id == "GO:0003677":
        return {
            "summary": "DNA binding is supported by lambda/Cro/C1-like phage repressor domain evidence.",
            "action": "ACCEPT",
            "reason": "The GOA row and UniProt domain context support a phage regulatory DNA-binding protein. A more specific operator sequence or regulatory target is not known.",
            "supported_by": evidence_for(gene, term_id, ("Lambda_DNA-bd_dom_sf", "Cro/C1-type_HTH", "HTH_3")),
        }
    if gene == "PP_5626" and term_id == "GO:0006355":
        return {
            "summary": "Regulation of DNA-templated transcription is compatible with the phage repressor-like DNA-binding domain.",
            "action": "ACCEPT",
            "reason": "The UniRule-derived process row is consistent with a Cro/C1-type HTH phage repressor-like DNA-binding protein, although the specific regulated promoter is not known.",
            "supported_by": evidence_for(gene, term_id, ("Cro/C1-type_HTH", "Lambda_DNA-bd_dom_sf", "HTH_3")),
        }
    if gene == "PP_5626" and term_id == "GO:0006351":
        return {
            "summary": "DNA-templated transcription is too broad for this phage repressor-like protein.",
            "action": "MODIFY",
            "reason": "The protein is not part of the transcription machinery; the supported process is regulatory DNA binding affecting transcription. The more specific regulation term is already present on the record.",
            "proposed_replacement_terms": [TERM["GO:0006355"]],
            "supported_by": evidence_for(gene, "GO:0006355", ("Cro/C1-type_HTH", "Lambda_DNA-bd_dom_sf", "HTH_3")),
        }
    raise ValueError(f"No review rule for {gene} {term_id}")


def ensure_new_rows(data: dict, gene: str) -> None:
    if gene != "PP_2500":
        return
    rows = data.setdefault("existing_annotations", [])
    if any(row.get("term", {}).get("id") == "GO:0090729" for row in rows):
        return
    rows.append(
        {
            "term": TERM["GO:0090729"],
            "evidence_type": "IEA",
            "original_reference_id": file_id(gene, "uniprot.txt"),
            "qualifier": "enables",
            "review": review_for(gene, "GO:0090729"),
        }
    )


def core_functions_for(gene: str) -> list[dict]:
    if gene == "PP_1561":
        return [
            {
                "description": "HNH-domain endonuclease activity in prophage/mobile-element context.",
                "supported_by": evidence_for(gene, "GO:0004519", ("HNH.", "HNH_nuc", "PF01844")),
                "molecular_function": TERM["GO:0004519"],
            }
        ]
    if gene == "PP_2500":
        return [
            {
                "description": "RelE/ParE-family toxin activity in toxin-antitoxin or plasmid-stabilization context.",
                "supported_by": evidence_for(gene, None, ("RelE/ParE_toxin", "TA_system_RelE-like_toxin", "ParE_toxin")),
                "molecular_function": TERM["GO:0090729"],
            }
        ]
    if gene == "PP_5558":
        return [
            {
                "description": "XRE-family phage regulatory DNA binding.",
                "supported_by": evidence_for(gene, "GO:0003677", ("Lambda_DNA-bd_dom_sf",)),
                "molecular_function": TERM["GO:0003677"],
            }
        ]
    if gene == "PP_5626":
        return [
            {
                "description": "Cro/C1-type phage repressor-like DNA binding in regulation of DNA-templated transcription.",
                "supported_by": evidence_for(gene, "GO:0003677", ("Cro/C1-type_HTH", "Lambda_DNA-bd_dom_sf", "HTH_3")),
                "molecular_function": TERM["GO:0003677"],
                "directly_involved_in": [TERM["GO:0006355"]],
            }
        ]
    return []


def suggested_questions_for(gene: str) -> list[dict[str, str]]:
    questions = {
        "PP_1561": "Is PP_1561 a prophage HNH nuclease despite the holin product name, and what DNA substrate does it cleave?",
        "PP_4858": "Does PP_4858 encode a real phage host-interaction protein, and is the predicted signal peptide functional?",
        "PP_2500": "What is the target and cognate antitoxin partner for the PP_2500 RelE/ParE-family toxin candidate?",
        "PP_5558": "What phage regulatory DNA sequence or promoter is bound by PP_5558?",
        "PP_5626": "What phage regulatory DNA sequence or promoter is bound by PP_5626?",
    }
    return [{"question": questions[gene]}]


def suggested_experiments_for(gene: str) -> list[dict[str, str]]:
    if gene == "PP_1561":
        return [
            {
                "experiment_type": "nuclease assay",
                "description": "Test purified PP_1561 against candidate DNA substrates and mutate conserved HNH residues if identifiable.",
                "hypothesis": "PP_1561 is an HNH-family endonuclease rather than a holin pore protein.",
            }
        ]
    if gene == "PP_4858":
        return [
            {
                "experiment_type": "localization and infection-context assay",
                "description": "Validate PP_4858 signal-peptide-dependent localization and assay phenotypes in prophage induction or envelope stress conditions.",
                "hypothesis": "PP_4858 contributes to prophage host interaction or envelope-associated infection biology.",
            }
        ]
    if gene == "PP_2500":
        return [
            {
                "experiment_type": "toxicity and antitoxin suppression assay",
                "description": "Express PP_2500 with and without candidate neighboring antitoxins and test growth inhibition plus RNA or DNA target effects.",
                "hypothesis": "PP_2500 is an active RelE/ParE-family toxin whose toxicity is suppressed by a cognate antitoxin.",
            }
        ]
    return [
        {
            "experiment_type": "DNA-binding and reporter assay",
            "description": f"Test purified {gene} against candidate prophage operator sequences and use reporter assays for transcriptional regulation.",
            "hypothesis": f"{gene} is a phage regulatory DNA-binding protein.",
        }
    ]


def curate_gene(gene: str) -> None:
    path = GENE_ROOT / gene / f"{gene}-ai-review.yaml"
    data = yaml.safe_load(path.read_text())
    data["status"] = "DRAFT"
    data["description"] = description_for(gene)
    ensure_references(data, gene)
    ensure_new_rows(data, gene)
    for ann in data.get("existing_annotations") or []:
        ann["review"] = review_for(gene, ann["term"]["id"])
    data["core_functions"] = core_functions_for(gene)
    data["proposed_new_terms"] = []
    data["suggested_questions"] = suggested_questions_for(gene)
    data["suggested_experiments"] = suggested_experiments_for(gene)
    path.write_text(yaml.dump(data, Dumper=NoAliasDumper, sort_keys=False, allow_unicode=False, width=120), encoding="utf-8")


def descriptor(term_id: str, description: str | None = None) -> dict:
    item = {"preferred_term": TERM[term_id]["label"], "term": TERM[term_id]}
    if description:
        item["description"] = description
    return item


def participant(gene: str) -> dict:
    return {"selector_type": "GENE", "gene": {"preferred_term": gene}}


def module_review(path: Path, data: dict) -> None:
    path.write_text(yaml.dump(data, Dumper=NoAliasDumper, sort_keys=False, allow_unicode=False, width=120), encoding="utf-8")


def write_modules() -> None:
    module_review(
        LYSIS_MODULE,
        {
            "id": "MODULE:phage_lysis_host_interaction_boundary",
            "title": "Phage lysis and host-interaction boundary",
            "description": "Boundary module for sparse PSEPK prophage lysis, infection, and host-interaction candidates.",
            "status": "DRAFT",
            "evidence": [
                {
                    "source_id": "file:projects/P_PUTIDA/batches/module_mobile_genetic_elements_phage_lysis_host_interaction.tsv",
                    "title": "PSEPK mobile-genetic-elements phage lysis and host-interaction split table",
                    "statement": "The split table routes two broad mobile-genetic-elements genes to phage lysis or host-interaction context.",
                }
            ],
            "notes": "PP_1561 is curated from HNH nuclease evidence rather than the holin product name. PP_4858 is retained as an unresolved signal-peptide-containing phage infection protein candidate with no core GO function asserted.",
            "module": {
                "id": "phage_lysis_host_interaction_boundary",
                "label": "Phage lysis and host-interaction boundary",
                "module_type": "BIOLOGICAL_PROCESS",
                "concepts": [
                    descriptor("GO:0004519", "HNH-domain endonuclease activity in prophage/mobile-element context."),
                ],
                "parts": [
                    {
                        "order": 1,
                        "role": "HNH nuclease and unresolved host-interaction candidates",
                        "node": {
                            "id": "phage_lysis_host_interaction_candidates",
                            "label": "Phage lysis/host-interaction candidates",
                            "module_type": "BIOLOGICAL_PROCESS",
                            "annotons": [
                                {
                                    "id": "pp_1561_hnh_endonuclease",
                                    "label": "PP_1561: HNH-domain endonuclease candidate",
                                    "participant": participant("PP_1561"),
                                    "role_description": "HNH-domain endonuclease candidate in prophage context",
                                    "function": descriptor("GO:0004519"),
                                },
                                {
                                    "id": "pp_4858_unresolved_phage_infection_context",
                                    "label": "PP_4858: unresolved phage infection protein candidate",
                                    "participant": participant("PP_4858"),
                                    "role_description": "unresolved phage infection protein candidate",
                                    "notes": "No fetched GOA rows and no conserved family/domain support; signal peptide and product name only.",
                                },
                            ],
                        },
                    }
                ],
            },
        },
    )
    module_review(
        REG_MODULE,
        {
            "id": "MODULE:phage_regulation_toxin_antitoxin_boundary",
            "title": "Phage regulation and toxin-antitoxin boundary",
            "description": "Boundary module for PSEPK phage-origin regulatory DNA-binding proteins and mobile-element toxin-antitoxin candidates.",
            "status": "DRAFT",
            "evidence": [
                {
                    "source_id": "file:projects/P_PUTIDA/batches/module_mobile_genetic_elements_phage_regulatory_toxin_antitoxin.tsv",
                    "title": "PSEPK mobile-genetic-elements phage regulatory and toxin-antitoxin split table",
                    "statement": "The split table routes three broad mobile-genetic-elements genes to phage regulatory or toxin-antitoxin context.",
                }
            ],
            "notes": "PP_2500 is curated as a RelE/ParE-family toxin candidate with generic toxin activity. PP_5558 and PP_5626 are phage-origin DNA-binding regulatory proteins; PP_5626 keeps transcription regulation but not the broad DNA-templated transcription parent process as core.",
            "module": {
                "id": "phage_regulation_toxin_antitoxin_boundary",
                "label": "Phage regulation and toxin-antitoxin boundary",
                "module_type": "BIOLOGICAL_PROCESS",
                "concepts": [
                    descriptor("GO:0090729", "Generic toxin activity for RelE/ParE-family toxin-antitoxin candidates."),
                    descriptor("GO:0003677", "DNA binding by phage-origin XRE/Cro/C1-like regulatory proteins."),
                    descriptor("GO:0006355", "Regulation of DNA-templated transcription by phage repressor-like proteins."),
                ],
                "parts": [
                    {
                        "order": 1,
                        "role": "Toxin-antitoxin and phage regulatory proteins",
                        "node": {
                            "id": "phage_regulatory_toxin_antitoxin_candidates",
                            "label": "Phage regulatory/toxin-antitoxin candidates",
                            "module_type": "BIOLOGICAL_PROCESS",
                            "annotons": [
                                {
                                    "id": "pp_2500_rele_pare_toxin",
                                    "label": "PP_2500: RelE/ParE-family toxin activity",
                                    "participant": participant("PP_2500"),
                                    "role_description": "RelE/ParE-family toxin activity",
                                    "function": descriptor("GO:0090729"),
                                },
                                {
                                    "id": "pp_5558_xre_dna_binding",
                                    "label": "PP_5558: XRE-family phage-origin DNA binding",
                                    "participant": participant("PP_5558"),
                                    "role_description": "XRE-family phage-origin DNA binding",
                                    "function": descriptor("GO:0003677"),
                                },
                                {
                                    "id": "pp_5626_phage_repressor_dna_binding",
                                    "label": "PP_5626: phage repressor-like DNA binding",
                                    "participant": participant("PP_5626"),
                                    "role_description": "phage repressor-like DNA binding",
                                    "function": descriptor("GO:0003677"),
                                    "processes": [descriptor("GO:0006355")],
                                },
                            ],
                        },
                    }
                ],
            },
        },
    )


def main() -> None:
    for gene in GENES:
        curate_gene(gene)
    write_modules()
    print(f"Curated {len(GENES)} gene reviews")
    print(f"Wrote {LYSIS_MODULE}")
    print(f"Wrote {REG_MODULE}")


if __name__ == "__main__":
    main()
