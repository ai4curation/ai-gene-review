#!/usr/bin/env python3
"""First-pass curation for PSEPK phage DNA replication/processing mobile-element split."""

from __future__ import annotations

from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[2]
GENE_ROOT = ROOT / "genes" / "PSEPK"
MODULE_PATH = ROOT / "modules" / "phage_dna_replication_processing_boundary.yaml"


class NoAliasDumper(yaml.SafeDumper):
    def ignore_aliases(self, data):
        return True


TERM = {
    "GO:0003677": {"id": "GO:0003677", "label": "DNA binding"},
    "GO:0003688": {"id": "GO:0003688", "label": "DNA replication origin binding"},
    "GO:0003697": {"id": "GO:0003697", "label": "single-stranded DNA binding"},
    "GO:0005524": {"id": "GO:0005524", "label": "ATP binding"},
    "GO:0006260": {"id": "GO:0006260", "label": "DNA replication"},
    "GO:0008833": {"id": "GO:0008833", "label": "deoxyribonuclease IV (phage-T4-induced) activity"},
    "GO:0015074": {"id": "GO:0015074", "label": "DNA integration"},
    "GO:0016032": {"id": "GO:0016032", "label": "viral process"},
}

GENES = ["PP_1551", "PP_1552", "PP_2267", "PP_2268", "PP_3864", "PP_3894"]
PHAGE_O_GENES = {"PP_1551", "PP_3894"}


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
    for marker in ("DR   PANTHER;", "KW   DNA-binding", "DR   Pfam;"):
        add_unique(items, support(file_id(gene, "uniprot.txt"), optional_first_line(path, marker)))
    asta = gene_file(gene, "deep-research-asta.md")
    add_unique(items, support(file_id(gene, "deep-research-asta.md"), optional_first_line(asta, "uniprot_accession:")))
    add_unique(items, support(file_id(gene, "deep-research-asta.md"), optional_first_line(asta, "protein_description:")))
    add_unique(items, support(file_id(gene, "deep-research-asta.md"), optional_first_line(asta, "protein_domains:")))
    return items


def description_for(gene: str) -> str:
    product = (product_line(gene) or "phage DNA-processing protein").removeprefix("DE   ").rstrip(".")
    if gene in PHAGE_O_GENES:
        return (
            f"{gene} encodes a phage replication protein O-family protein ({product}) with phage lambda VrpO_N and "
            "winged-helix-like DNA-binding domain support. It is associated with prophage DNA replication initiation "
            "or origin-recognition context."
        )
    if gene == "PP_1552":
        return (
            f"{gene} encodes an IstB/P-loop NTPase-family phage replication protein ({product}). Its supported role is "
            "ATP binding in phage or insertion-sequence-associated DNA replication context."
        )
    if gene == "PP_2267":
        return (
            f"{gene} encodes a T7-like phage single-stranded DNA-binding protein ({product}) with OB-fold/SSB-family "
            "domain support, consistent with binding exposed single-stranded DNA during phage DNA replication."
        )
    if gene == "PP_2268":
        return (
            f"{gene} encodes a phage endodeoxyribonuclease I-family protein ({product}) with T7 gp3/restriction-"
            "endonuclease-like domain support. It is associated with phage DNA cleavage and integration-related viral "
            "DNA processing."
        )
    return (
        f"{gene} encodes a phage FluMu DNA-circulation-domain protein ({product}). The local record supports phage DNA "
        "circulation context but lacks GOA rows or a resolved molecular activity."
    )


def ensure_references(data: dict, gene: str) -> None:
    refs = data.setdefault("references", [])
    by_id = {ref.get("id"): ref for ref in refs}
    local_refs = [
        (file_id(gene, "uniprot.txt"), f"UniProtKB entry for {gene}", product_line(gene)),
        (file_id(gene, "goa.tsv"), f"QuickGO GOA annotations for {gene}", None),
        (
            file_id(gene, "deep-research-asta.md"),
            f"Asta retrieval report for {gene}",
            optional_first_line(gene_file(gene, "deep-research-asta.md"), "uniprot_accession:"),
        ),
    ]
    for ref_id, title, quote in local_refs:
        if ref_id in by_id:
            continue
        finding = {"statement": "Local first-pass source used for phage DNA-processing review."}
        if quote:
            finding["supporting_text"] = quote
        refs.append({"id": ref_id, "title": title, "findings": [finding]})


def review_for(gene: str, term_id: str) -> dict:
    if gene in PHAGE_O_GENES and term_id == "GO:0006260":
        return {
            "summary": "DNA replication is compatible with phage replication protein O domain evidence.",
            "action": "ACCEPT",
            "reason": "The product name and phage lambda VrpO_N/Phage_rep_O domain evidence support a prophage DNA replication role.",
            "supported_by": evidence_for(gene, term_id, ("Phage_lambda_VrpO_N", "WH-like_DNA-bd_sf", "Phage_rep_O")),
        }
    if gene in PHAGE_O_GENES and term_id == "GO:0003688":
        return {
            "summary": "DNA replication origin binding is the conservative molecular-function call for this phage O-family protein.",
            "action": "NEW",
            "reason": "The fetched GOA has only the DNA replication process row, while the phage O-family and winged-helix-like DNA-binding domain support an origin-recognition molecular role.",
            "supported_by": evidence_for(gene, None, ("Phage_lambda_VrpO_N", "WH-like_DNA-bd_sf", "Phage_rep_O")),
        }
    if gene == "PP_1552" and term_id == "GO:0005524":
        return {
            "summary": "ATP binding is supported by the IstB/P-loop NTPase domains.",
            "action": "ACCEPT",
            "reason": "The GOA row and InterPro domain support ATP binding. No narrower ATPase or helicase activity is asserted from the current evidence.",
            "supported_by": evidence_for(gene, term_id, ("AAA+_ATPase", "IstB_ATP-bd", "P-loop_NTPase", "IstB_IS21")),
        }
    if gene == "PP_1552" and term_id == "GO:0006260":
        return {
            "summary": "DNA replication is compatible with the phage replication protein and TreeGrafter context.",
            "action": "ACCEPT",
            "reason": "The product name, P-loop/ISTB-family context, and TreeGrafter-derived process row support DNA replication context without resolving a precise catalytic mechanism.",
            "supported_by": evidence_for(gene, term_id, ("AAA+_ATPase", "IstB_ATP-bd", "P-loop_NTPase", "IstB_IS21")),
        }
    if gene == "PP_2267" and term_id == "GO:0003677":
        return {
            "summary": "The broad DNA-binding row is correct but should be replaced by single-stranded DNA binding.",
            "action": "MODIFY",
            "reason": "The product and OB-fold/T7 SSB domains specifically support a single-stranded DNA-binding protein rather than generic DNA binding.",
            "proposed_replacement_terms": [TERM["GO:0003697"]],
            "supported_by": evidence_for(gene, term_id, ("NA-bd_OB-fold", "SBB_BPT7", "SSB_T7", "SBB_T7")),
        }
    if gene == "PP_2267" and term_id == "GO:0003697":
        return {
            "summary": "Single-stranded DNA binding is supported by T7-like SSB domain evidence.",
            "action": "NEW",
            "reason": "The fetched GOA row is generic DNA binding, while the product and OB-fold/T7 SSB domains support the more specific single-stranded DNA-binding function.",
            "supported_by": evidence_for(gene, None, ("NA-bd_OB-fold", "SBB_BPT7", "SSB_T7", "SBB_T7")),
        }
    if gene == "PP_2267" and term_id == "GO:0006260":
        return {
            "summary": "DNA replication is added as the process context for the T7-like phage SSB protein.",
            "action": "NEW",
            "reason": "Single-stranded DNA-binding proteins stabilize exposed ssDNA during replication; here the phage SSB product and OB-fold/T7 SSB domains support phage DNA replication context.",
            "supported_by": evidence_for(gene, None, ("NA-bd_OB-fold", "SBB_BPT7", "SSB_T7", "SBB_T7")),
        }
    if gene == "PP_2268" and term_id == "GO:0008833":
        return {
            "summary": "Phage endodeoxyribonuclease activity is the supported catalytic function.",
            "action": "ACCEPT",
            "reason": "The GOA row, product name, and T7 gp3/restriction-endonuclease-like domain evidence support phage endodeoxyribonuclease activity.",
            "supported_by": evidence_for(gene, term_id, ("Phage_T7_Gp3_endoDNaseI", "Restrct_endonuc-II-like", "Phage_endo_I")),
        }
    if gene == "PP_2268" and term_id == "GO:0015074":
        return {
            "summary": "DNA integration is retained as the mobile-element DNA-processing context for this phage nuclease.",
            "action": "ACCEPT",
            "reason": "The InterPro-derived process row is compatible with a phage endodeoxyribonuclease participating in mobile-element DNA processing and integration.",
            "supported_by": evidence_for(gene, term_id, ("Phage_T7_Gp3_endoDNaseI", "Restrct_endonuc-II-like", "Phage_endo_I")),
        }
    if gene == "PP_2268" and term_id == "GO:0016032":
        return {
            "summary": "Viral process is correct but broad relative to the specific nuclease and DNA-integration context.",
            "action": "KEEP_AS_NON_CORE",
            "reason": "The phage nuclease/domain evidence supports viral DNA processing, but viral process is too broad to be the core functional call.",
            "supported_by": evidence_for(gene, term_id, ("Phage_T7_Gp3_endoDNaseI", "Restrct_endonuc-II-like", "Phage_endo_I")),
        }
    raise ValueError(f"No review rule for {gene} {term_id}")


def ensure_new_rows(data: dict, gene: str) -> None:
    rows = data.setdefault("existing_annotations", [])
    if gene in PHAGE_O_GENES and not any(row.get("term", {}).get("id") == "GO:0003688" for row in rows):
        rows.append(
            {
                "term": TERM["GO:0003688"],
                "evidence_type": "IEA",
                "original_reference_id": file_id(gene, "uniprot.txt"),
                "qualifier": "enables",
                "review": review_for(gene, "GO:0003688"),
            }
        )
    if gene == "PP_2267" and not any(row.get("term", {}).get("id") == "GO:0003697" for row in rows):
        rows.append(
            {
                "term": TERM["GO:0003697"],
                "evidence_type": "IEA",
                "original_reference_id": file_id(gene, "uniprot.txt"),
                "qualifier": "enables",
                "review": review_for(gene, "GO:0003697"),
            }
        )
    if gene == "PP_2267" and not any(row.get("term", {}).get("id") == "GO:0006260" for row in rows):
        rows.append(
            {
                "term": TERM["GO:0006260"],
                "evidence_type": "IEA",
                "original_reference_id": file_id(gene, "uniprot.txt"),
                "qualifier": "involved_in",
                "review": review_for(gene, "GO:0006260"),
            }
        )


def core_functions_for(gene: str) -> list[dict]:
    if gene in PHAGE_O_GENES:
        return [
            {
                "description": "Phage O-family DNA replication origin binding in prophage DNA replication context.",
                "supported_by": evidence_for(gene, None, ("Phage_lambda_VrpO_N", "WH-like_DNA-bd_sf", "Phage_rep_O")),
                "molecular_function": TERM["GO:0003688"],
                "directly_involved_in": [TERM["GO:0006260"]],
            }
        ]
    if gene == "PP_1552":
        return [
            {
                "description": "IstB/P-loop NTPase ATP binding in phage DNA replication context.",
                "supported_by": evidence_for(gene, "GO:0005524", ("AAA+_ATPase", "IstB_ATP-bd", "P-loop_NTPase", "IstB_IS21")),
                "molecular_function": TERM["GO:0005524"],
                "directly_involved_in": [TERM["GO:0006260"]],
            }
        ]
    if gene == "PP_2267":
        return [
            {
                "description": "T7-like single-stranded DNA binding in phage DNA replication context.",
                "supported_by": evidence_for(gene, None, ("NA-bd_OB-fold", "SBB_BPT7", "SSB_T7", "SBB_T7")),
                "molecular_function": TERM["GO:0003697"],
                "directly_involved_in": [TERM["GO:0006260"]],
            }
        ]
    if gene == "PP_2268":
        return [
            {
                "description": "Phage endodeoxyribonuclease activity in mobile-element DNA integration and viral DNA processing.",
                "supported_by": evidence_for(gene, "GO:0008833", ("Phage_T7_Gp3_endoDNaseI", "Restrct_endonuc-II-like", "Phage_endo_I")),
                "molecular_function": TERM["GO:0008833"],
                "directly_involved_in": [TERM["GO:0015074"]],
            }
        ]
    return []


def suggested_questions_for(gene: str) -> list[dict[str, str]]:
    questions = {
        "PP_1551": "What prophage origin sequence is recognized by PP_1551 during phage DNA replication?",
        "PP_1552": "Does PP_1552 hydrolyze ATP and act with a specific phage replication or transposition complex?",
        "PP_2267": "Which phage replication intermediate is bound by PP_2267 as a T7-like SSB protein?",
        "PP_2268": "What DNA substrate is cleaved by PP_2268 during phage DNA integration or viral DNA processing?",
        "PP_3864": "What molecular activity, if any, is associated with the PP_3864 FluMu DNA-circulation domain?",
        "PP_3894": "What prophage origin sequence is recognized by PP_3894 during phage DNA replication?",
    }
    return [{"question": questions[gene]}]


def suggested_experiments_for(gene: str) -> list[dict[str, str]]:
    return [
        {
            "experiment_type": "phage DNA substrate assay",
            "description": f"Test {gene} with candidate prophage-origin, single-stranded DNA, or integration-site substrates selected from its genomic neighborhood.",
            "hypothesis": f"{gene} contributes to prophage DNA replication or DNA processing.",
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


def annoton(gene: str) -> dict:
    if gene in PHAGE_O_GENES:
        return {
            "id": f"{gene.lower()}_phage_o_origin_binding",
            "label": f"{gene}: phage O-family DNA replication origin binding",
            "participant": participant(gene),
            "role_description": "phage O-family DNA replication origin binding",
            "function": descriptor("GO:0003688"),
            "processes": [descriptor("GO:0006260")],
        }
    if gene == "PP_1552":
        return {
            "id": "pp_1552_istb_atp_binding",
            "label": "PP_1552: IstB/P-loop NTPase ATP binding in DNA replication",
            "participant": participant(gene),
            "role_description": "IstB/P-loop NTPase ATP binding in DNA replication",
            "function": descriptor("GO:0005524"),
            "processes": [descriptor("GO:0006260")],
        }
    if gene == "PP_2267":
        return {
            "id": "pp_2267_t7_ssb",
            "label": "PP_2267: T7-like single-stranded DNA binding",
            "participant": participant(gene),
            "role_description": "T7-like single-stranded DNA binding",
            "function": descriptor("GO:0003697"),
            "processes": [descriptor("GO:0006260")],
        }
    if gene == "PP_2268":
        return {
            "id": "pp_2268_phage_endodeoxyribonuclease",
            "label": "PP_2268: phage endodeoxyribonuclease activity",
            "participant": participant(gene),
            "role_description": "phage endodeoxyribonuclease activity",
            "function": descriptor("GO:0008833"),
            "processes": [descriptor("GO:0015074"), descriptor("GO:0016032")],
        }
    return {
        "id": "pp_3864_unresolved_dna_circulation_context",
        "label": "PP_3864: unresolved FluMu DNA-circulation-domain protein",
        "participant": participant(gene),
        "role_description": "unresolved FluMu DNA-circulation-domain protein",
        "notes": "No fetched GOA rows and no resolved molecular activity; retained as phage DNA-processing context.",
    }


def write_module() -> None:
    data = {
        "id": "MODULE:phage_dna_replication_processing_boundary",
        "title": "Phage DNA replication and processing boundary",
        "description": "Boundary module for PSEPK prophage DNA replication, single-stranded DNA binding, endodeoxyribonuclease, and DNA-circulation candidates.",
        "status": "DRAFT",
        "evidence": [
            {
                "source_id": "file:projects/P_PUTIDA/batches/module_mobile_genetic_elements_phage_dna_replication_processing.tsv",
                "title": "PSEPK mobile-genetic-elements phage DNA replication and processing split table",
                "statement": "The split table routes six broad mobile-genetic-elements genes to phage DNA replication or DNA-processing context.",
            }
        ],
        "notes": "PP_3864 is retained as an unresolved FluMu DNA-circulation-domain protein with no core GO function asserted.",
        "module": {
            "id": "phage_dna_replication_processing_boundary",
            "label": "Phage DNA replication and processing boundary",
            "module_type": "BIOLOGICAL_PROCESS",
            "concepts": [
                descriptor("GO:0003688", "Phage O-family origin-recognition DNA binding."),
                descriptor("GO:0005524", "ATP binding by IstB/P-loop NTPase-family phage replication proteins."),
                descriptor("GO:0003697", "Single-stranded DNA binding by T7-like phage SSB proteins."),
                descriptor("GO:0008833", "Phage endodeoxyribonuclease activity."),
                descriptor("GO:0006260", "DNA replication process context."),
                descriptor("GO:0015074", "DNA integration process context."),
            ],
            "parts": [
                {
                    "order": 1,
                    "role": "Phage DNA replication and processing candidates",
                    "node": {
                        "id": "phage_dna_replication_processing_candidates",
                        "label": "Phage DNA replication/processing candidates",
                        "module_type": "BIOLOGICAL_PROCESS",
                        "annotons": [annoton(gene) for gene in GENES],
                    },
                }
            ],
        },
    }
    MODULE_PATH.write_text(yaml.dump(data, Dumper=NoAliasDumper, sort_keys=False, allow_unicode=False, width=120), encoding="utf-8")


def main() -> None:
    for gene in GENES:
        curate_gene(gene)
    write_module()
    print(f"Curated {len(GENES)} gene reviews")
    print(f"Wrote {MODULE_PATH}")


if __name__ == "__main__":
    main()
