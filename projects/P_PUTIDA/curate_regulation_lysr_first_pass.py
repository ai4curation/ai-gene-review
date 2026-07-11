#!/usr/bin/env python3
"""First-pass curation for LysR-family transcriptional regulators."""

from __future__ import annotations

import csv
import re
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[2]
GENE_ROOT = ROOT / "genes" / "PSEPK"
BATCH_TSV = (
    ROOT
    / "projects"
    / "P_PUTIDA"
    / "batches"
    / "module_regulation_signal_transduction_lysr_transcriptional_regulators.tsv"
)
MODULE_PATH = ROOT / "modules" / "lysr_transcriptional_regulator_boundary.yaml"
SPECIES = "PSEPK"

EXISTING_CURATED = {"pcaQ", "galR", "catR"}
ACTIVATOR_GENES = {"trpI", "gcdR", "lysR", "PP_4107", "PP_4494", "PP_5259"}
PATHWAY_NAMED_GENES = {
    "trpI",
    "PP_4107",
    "PP_5259",
    "metR-I",
    "metR-II",
    "lysR",
    "gcdR",
    "pcaQ",
    "galR",
    "catR",
}
NAMED_SIDE_GENES = {"PP_0661", "mexT", "cidR", "ybhD", "yneJ", "ynfL"}


class NoAliasDumper(yaml.SafeDumper):
    def ignore_aliases(self, data):  # type: ignore[override]
        return True


def term(go_id: str, label: str) -> dict[str, str]:
    return {"id": go_id, "label": label}


TERMS = {
    "GO:0000162": term("GO:0000162", "tryptophan biosynthetic process"),
    "GO:0000976": term("GO:0000976", "transcription cis-regulatory region binding"),
    "GO:0001216": term("GO:0001216", "DNA-binding transcription activator activity"),
    "GO:0003677": term("GO:0003677", "DNA binding"),
    "GO:0003700": term("GO:0003700", "DNA-binding transcription factor activity"),
    "GO:0005737": term("GO:0005737", "cytoplasm"),
    "GO:0005829": term("GO:0005829", "cytosol"),
    "GO:0006351": term("GO:0006351", "DNA-templated transcription"),
    "GO:0006355": term("GO:0006355", "regulation of DNA-templated transcription"),
    "GO:0009086": term("GO:0009086", "methionine biosynthetic process"),
    "GO:0009089": term("GO:0009089", "lysine biosynthetic process"),
    "GO:0009891": term("GO:0009891", "positive regulation of biosynthetic process"),
    "GO:0010628": term("GO:0010628", "positive regulation of gene expression"),
    "GO:0019619": term("GO:0019619", "3,4-dihydroxybenzoate catabolic process"),
    "GO:0032993": term("GO:0032993", "protein-DNA complex"),
    "GO:0043565": term("GO:0043565", "sequence-specific DNA binding"),
    "GO:0045893": term("GO:0045893", "positive regulation of DNA-templated transcription"),
    "GO:2000142": term("GO:2000142", "regulation of DNA-templated transcription initiation"),
}

LOCATION_TERMS = {"GO:0005737", "GO:0005829"}
PATHWAY_PROCESS_TERMS = {"GO:0000162", "GO:0009086", "GO:0009089", "GO:0019619"}


def read_batch_rows() -> dict[str, dict[str, str]]:
    with BATCH_TSV.open(encoding="utf-8") as handle:
        return {row["gene"]: row for row in csv.DictReader(handle, delimiter="\t")}


BATCH_ROWS = read_batch_rows()
GENES = list(BATCH_ROWS)


def gene_file(gene: str, suffix: str) -> Path:
    return GENE_ROOT / gene / f"{gene}-{suffix}"


def file_id(gene: str, suffix: str) -> str:
    return f"file:{SPECIES}/{gene}/{gene}-{suffix}"


def lines(path: Path) -> list[str]:
    if not path.exists():
        return []
    return path.read_text(encoding="utf-8").splitlines()


def first_line(path: Path, *needles: str) -> str | None:
    for line in lines(path):
        if all(needle in line for needle in needles):
            return line.strip()
    return None


def support(ref_id: str, text: str | None) -> dict[str, str] | None:
    if not text:
        return None
    return {"reference_id": ref_id, "supporting_text": text}


def add_support(items: list[dict[str, str]], item: dict[str, str] | None) -> None:
    if item and item["supporting_text"] and item not in items:
        items.append(item)


def goa_rows(gene: str) -> list[dict[str, str]]:
    path = gene_file(gene, "goa.tsv")
    if not path.exists() or path.stat().st_size == 0:
        return []
    with path.open(encoding="utf-8") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def goa_ids(gene: str) -> set[str]:
    return {row["GO TERM"] for row in goa_rows(gene) if row.get("GO TERM")}


def goa_quote(row: dict[str, str]) -> str:
    return f"{row['GO TERM']}\t{row['GO NAME']}"


def matching_goa_row(gene: str, annotation: dict) -> dict[str, str] | None:
    go_id = annotation.get("term", {}).get("id")
    evidence = annotation.get("evidence_type")
    reference = annotation.get("original_reference_id")
    for row in goa_rows(gene):
        if (
            row.get("GO TERM") == go_id
            and row.get("GO EVIDENCE CODE") == evidence
            and row.get("REFERENCE") == reference
        ):
            return row
    for row in goa_rows(gene):
        if row.get("GO TERM") == go_id:
            return row
    return None


def first_goa_support(gene: str, go_id: str) -> dict[str, str] | None:
    for row in goa_rows(gene):
        if row.get("GO TERM") == go_id:
            return support(file_id(gene, "goa.tsv"), goa_quote(row))
    return None


def uniprot_support_lines(gene: str) -> list[dict[str, str]]:
    path = gene_file(gene, "uniprot.txt")
    items: list[dict[str, str]] = []
    product = first_line(path, "DE   RecName:") or first_line(path, "DE   SubName:")
    add_support(items, support(file_id(gene, "uniprot.txt"), product))
    for line in lines(path):
        if (
            line.startswith("CC   -!- SIMILARITY:")
            or line.startswith("DR   InterPro; IPR000847;")
            or line.startswith("DR   InterPro; IPR005119;")
            or line.startswith("DR   InterPro; IPR050389;")
            or line.startswith("DR   InterPro; IPR050950;")
            or line.startswith("DR   InterPro; IPR058163;")
            or line.startswith("DR   InterPro; IPR037406;")
            or line.startswith("DR   InterPro; IPR037418;")
            or line.startswith("DR   InterPro; IPR012787;")
            or line.startswith("DR   Pfam; PF00126;")
            or line.startswith("DR   Pfam; PF03466;")
            or line.startswith("KW   DNA-binding")
            or line.startswith("KW   Transcription")
            or line.startswith("KW   Transcription regulation")
            or line.startswith("KW   Activator")
            or line.startswith("KW   Repressor")
            or line.startswith("FT   DOMAIN")
            or line.startswith("FT                   /note=")
        ):
            add_support(items, support(file_id(gene, "uniprot.txt"), line.strip()))
        if len(items) >= 10:
            break
    return items


def asta_support_lines(gene: str) -> list[dict[str, str]]:
    path = gene_file(gene, "deep-research-asta.md")
    items: list[dict[str, str]] = []
    for needle in ("protein_description:", "**Protein Description:**", "- **Protein Description:**"):
        line = first_line(path, needle)
        if line:
            add_support(items, support(file_id(gene, "deep-research-asta.md"), line))
            break
    for needle in ("protein_family:", "protein_domains:", "- **Key Domains:**"):
        line = first_line(path, needle)
        if line:
            add_support(items, support(file_id(gene, "deep-research-asta.md"), line))
    return items


def evidence_for(gene: str, go_id: str | None = None) -> list[dict[str, str]]:
    items: list[dict[str, str]] = []
    if go_id:
        add_support(items, first_goa_support(gene, go_id))
    for item in uniprot_support_lines(gene):
        add_support(items, item)
    for item in asta_support_lines(gene):
        add_support(items, item)
    return items


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


def normalize_go_ref_titles(doc: dict) -> None:
    for ref in doc.get("references", []):
        ref_id = str(ref.get("id", ""))
        if ref_id.startswith("GO_REF:") and str(ref.get("title", "")).startswith("TODO:"):
            ref["title"] = f"Gene Ontology annotation reference {ref_id}"


def description_for(gene: str) -> str:
    row = BATCH_ROWS[gene]
    product = row["protein_name"]
    if gene in ACTIVATOR_GENES:
        return (
            f"{gene} encodes a predicted LysR-family DNA-binding transcriptional activator in "
            f"Pseudomonas putida KT2440. The product annotation ({product}) and conserved LysR HTH "
            "and substrate-binding domains support transcriptional activation, but the direct promoters, "
            "effector ligand, and pathway-specific regulon require gene-specific validation."
        )
    if gene in {"metR-I", "metR-II"}:
        return (
            f"{gene} encodes a predicted MetR-like LysR-family DNA-binding transcriptional regulator in "
            "Pseudomonas putida KT2440. The conserved HTH and LysR substrate-binding domains support "
            "transcriptional regulation, while the methionine-biosynthesis regulon and effector response "
            "remain inferred from product and family context."
        )
    if gene == "mexT":
        return (
            "mexT encodes a predicted MexT-like LysR-family DNA-binding transcriptional regulator in "
            "Pseudomonas putida KT2440. The conserved LysR architecture supports transcriptional "
            "regulation, but this first-pass evidence does not establish a specific efflux or stress regulon."
        )
    if gene == "cidR":
        return (
            "cidR encodes a predicted LysR-family DNA-binding transcriptional regulator in Pseudomonas "
            "putida KT2440. Conserved LysR HTH and substrate-binding domains support a transcriptional "
            "regulatory role, but the target regulon and effector ligand are unresolved."
        )
    return (
        f"{gene} encodes a predicted LysR-family DNA-binding transcriptional regulator in Pseudomonas "
        "putida KT2440. The conserved N-terminal helix-turn-helix DNA-binding domain and C-terminal "
        "LysR substrate-binding domain support regulation of DNA-templated transcription, while the "
        "target regulon, regulatory direction, and effector ligand are unresolved."
    )


def review_text(gene: str, go_id: str) -> tuple[str, str, str, list[dict[str, str]] | None]:
    if go_id == "GO:0003700":
        if gene in ACTIVATOR_GENES:
            return (
                "MODIFY",
                "The parent transcription-factor term is correct but the product evidence supports the activator child term.",
                "The LysR-family DNA-binding regulator is named or annotated as a transcriptional activator, so GO:0001216 is the more informative molecular-function term.",
                [TERMS["GO:0001216"]],
            )
        return (
            "ACCEPT",
            "DNA-binding transcription factor activity is the supported shared LysR-family molecular function.",
            "The product, HTH DNA-binding domain, and LysR substrate-binding domain support transcription-factor activity without resolving a specific regulon.",
            None,
        )
    if go_id == "GO:0001216":
        return (
            "ACCEPT",
            "DNA-binding transcription activator activity is supported for this named activator.",
            "The product and family context support a positive transcriptional regulator role.",
            None,
        )
    if go_id == "GO:0000976":
        return (
            "ACCEPT",
            "Cis-regulatory-region binding fits the HTH DNA-binding output of a LysR-family transcription factor.",
            "The conserved LysR HTH domain supports promoter-region binding, although target promoters remain unresolved for most paralogs.",
            None,
        )
    if go_id == "GO:0043565":
        return (
            "ACCEPT",
            "Sequence-specific DNA binding is consistent with a LysR-family HTH transcription factor.",
            "The term captures the DNA-binding output domain but not the unresolved target regulon.",
            None,
        )
    if go_id == "GO:0003677":
        return (
            "MARK_AS_OVER_ANNOTATED",
            "Generic DNA binding is less informative than transcription-factor or promoter-binding terms.",
            "The protein is a LysR-family transcription regulator, so the broad DNA-binding parent term should not be treated as the core function.",
            None,
        )
    if go_id == "GO:0006351":
        return (
            "MODIFY",
            "DNA-templated transcription is too broad; LysR-family proteins regulate transcription rather than carry out transcription.",
            "The supported biological process is regulation of DNA-templated transcription by a DNA-binding transcription factor.",
            [TERMS["GO:0006355"]],
        )
    if go_id == "GO:0006355":
        return (
            "ACCEPT",
            "Regulation of DNA-templated transcription is the appropriate broad process for a LysR-family regulator.",
            "The product and domain architecture support transcriptional regulation while target regulons remain unresolved.",
            None,
        )
    if go_id in LOCATION_TERMS:
        return (
            "KEEP_AS_NON_CORE",
            "The cytosolic/cytoplasmic localization is plausible for a soluble bacterial transcription regulator but is not the core function.",
            "Keep this as localization context rather than the main functional assignment.",
            None,
        )
    if go_id in PATHWAY_PROCESS_TERMS:
        return (
            "MARK_AS_OVER_ANNOTATED",
            "The pathway-process term overstates direct participation by a transcriptional regulator.",
            "This protein likely regulates pathway gene expression, but it is not a catalytic enzyme in the pathway process.",
            None,
        )
    if go_id == "GO:0009891":
        return (
            "MARK_AS_OVER_ANNOTATED",
            "Positive regulation of biosynthetic process is a broad pathway-propagated regulatory term.",
            "The direct supported role is transcriptional regulation; the specific biosynthetic target pathway requires gene-specific evidence.",
            None,
        )
    if go_id == "GO:0010628":
        return (
            "KEEP_AS_NON_CORE",
            "Positive regulation of gene expression is plausible regulatory context but less precise than transcription regulation.",
            "Retain the annotation as non-core context unless a gene-specific activator regulon is established.",
            None,
        )
    if go_id == "GO:2000142":
        return (
            "KEEP_AS_NON_CORE",
            "Regulation of transcription initiation is plausible for a DNA-binding transcription factor but remains generic.",
            "Keep this as mechanism-level context while using DNA-binding transcription factor activity as the core function.",
            None,
        )
    if go_id == "GO:0032993":
        return (
            "KEEP_AS_NON_CORE",
            "Protein-DNA complex membership is a plausible DNA-bound state but is not the main molecular function.",
            "Promoter binding and transcription-factor activity capture the functional role more directly.",
            None,
        )
    raise KeyError(f"Unhandled GO term {go_id} for {gene}")


def make_review(gene: str, annotation: dict) -> dict:
    go_id = annotation["term"]["id"]
    action, summary, reason, replacements = review_text(gene, go_id)
    items: list[dict[str, str]] = []
    row = matching_goa_row(gene, annotation)
    if row:
        add_support(items, support(file_id(gene, "goa.tsv"), goa_quote(row)))
    for item in evidence_for(gene):
        add_support(items, item)
    review = {"summary": summary, "action": action, "reason": reason, "supported_by": items}
    if replacements:
        review["proposed_replacement_terms"] = replacements
    return review


def new_activator_annotation(gene: str) -> dict:
    return {
        "term": TERMS["GO:0001216"],
        "evidence_type": "IEA",
        "original_reference_id": file_id(gene, "uniprot.txt"),
        "qualifier": "enables",
        "review": {
            "summary": "DNA-binding transcription activator activity should be recorded for this named LysR activator.",
            "action": "NEW",
            "reason": "The product annotation identifies a LysR-family transcriptional activator, supporting the GO:0001216 child term.",
            "supported_by": evidence_for(gene),
        },
    }


def remove_authored_new_annotations(data: dict) -> None:
    data["existing_annotations"] = [
        annotation
        for annotation in data.get("existing_annotations", [])
        if not (
            annotation.get("term", {}).get("id") == "GO:0001216"
            and annotation.get("review", {}).get("action") == "NEW"
        )
    ]


def add_needed_new_annotations(gene: str, data: dict) -> None:
    existing_ids = {annotation.get("term", {}).get("id") for annotation in data.get("existing_annotations", [])}
    if gene in ACTIVATOR_GENES and "GO:0001216" not in existing_ids:
        data.setdefault("existing_annotations", []).append(new_activator_annotation(gene))


def core_functions(gene: str) -> list[dict]:
    if gene in ACTIVATOR_GENES:
        return [
            {
                "description": "LysR-family DNA-binding transcription activator activity.",
                "molecular_function": TERMS["GO:0001216"],
                "directly_involved_in": [TERMS["GO:0045893"]],
                "supported_by": evidence_for(gene, "GO:0003700"),
            }
        ]
    return [
        {
            "description": "LysR-family DNA-binding transcription factor activity.",
            "molecular_function": TERMS["GO:0003700"],
            "directly_involved_in": [TERMS["GO:0006355"]],
            "supported_by": evidence_for(gene, "GO:0003700"),
        }
    ]


def suggested_question(gene: str) -> str:
    if gene in PATHWAY_NAMED_GENES:
        return f"Which promoters, effector ligand, and regulatory direction define the {gene} LysR-family regulon in KT2440?"
    if gene == "mexT":
        return "Does KT2440 MexT directly regulate an efflux, oxidative-stress, or other stress-response regulon under native conditions?"
    return f"What target regulon and small-molecule effector define the {gene} LysR-family transcription factor?"


def suggested_experiment(gene: str) -> str:
    return (
        f"Construct a {gene} deletion and complemented strain, then combine RNA-seq with promoter binding "
        "assays under candidate nutrient, aromatic, amino-acid, and stress conditions."
    )


def curate_gene(gene: str) -> None:
    if gene in EXISTING_CURATED:
        print(f"Preserved existing curated review for {gene}")
        return
    path = gene_file(gene, "ai-review.yaml")
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    row = BATCH_ROWS[gene]
    product_line = first_line(gene_file(gene, "uniprot.txt"), "DE   RecName:") or first_line(
        gene_file(gene, "uniprot.txt"), "DE   SubName:"
    )
    asta_line = first_line(gene_file(gene, "deep-research-asta.md"), "protein_description:")

    data["gene_symbol"] = gene
    if row["ordered_locus"] and row["ordered_locus"] != gene:
        data["aliases"] = [row["ordered_locus"]]
    data["status"] = "DRAFT"
    data["description"] = description_for(gene)
    ensure_reference(data, file_id(gene, "goa.tsv"), f"QuickGO GOA annotations for {gene}")
    ensure_reference(data, file_id(gene, "uniprot.txt"), f"UniProtKB entry for {gene} ({row['uniprot_accession']})", product_line)
    ensure_reference(data, file_id(gene, "deep-research-asta.md"), f"Asta retrieval report for {gene} ({row['uniprot_accession']})", asta_line)
    normalize_go_ref_titles(data)

    remove_authored_new_annotations(data)
    for annotation in data.get("existing_annotations", []):
        annotation["review"] = make_review(gene, annotation)
    add_needed_new_annotations(gene, data)

    data["core_functions"] = core_functions(gene)
    data["proposed_new_terms"] = []
    data["suggested_questions"] = [{"question": suggested_question(gene)}]
    data["suggested_experiments"] = [
        {
            "description": suggested_experiment(gene),
            "experiment_type": "targeted transcriptional regulatory assay",
        }
    ]

    path.write_text(
        yaml.dump(data, Dumper=NoAliasDumper, sort_keys=False, allow_unicode=False, width=100),
        encoding="utf-8",
    )
    print(f"Curated {path.relative_to(ROOT)}")


def slug(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "_", text.lower()).strip("_")


def module_term(go_id: str) -> dict:
    item = TERMS[go_id]
    return {"preferred_term": item["label"], "term": item}


def annoton(gene: str, label: str, function_id: str, process_ids: list[str], role: str) -> dict:
    return {
        "id": slug(label),
        "label": label,
        "participant": {"selector_type": "GENE", "gene": {"preferred_term": gene}},
        "processes": [module_term(go_id) for go_id in process_ids],
        "locations": [],
        "role_description": role,
        "function": module_term(function_id),
    }


def grouped_part(order: int, role: str, node_id: str, label: str, description: str, annotons: list[dict]) -> dict:
    return {
        "order": order,
        "role": role,
        "node": {
            "id": node_id,
            "label": label,
            "module_type": "REGULATORY_STEP",
            "description": description,
            "annotons": annotons,
        },
    }


def build_module() -> None:
    pathway_named = [gene for gene in GENES if gene in PATHWAY_NAMED_GENES]
    named_side = [gene for gene in GENES if gene in NAMED_SIDE_GENES]
    generic = [gene for gene in GENES if gene not in set(pathway_named) | set(named_side)]
    doc = {
        "id": "MODULE:lysr_transcriptional_regulator_boundary",
        "title": "LysR-family transcriptional regulator boundary",
        "description": (
            "Boundary module for the PSEPK regulation/signal-transduction LysR-family expansion. "
            "It groups 107 predicted LysR-family transcription regulators, preserving existing "
            "curated pathway-specific anchors for pcaQ, galR, and catR while treating the remaining "
            "paralogs conservatively as DNA-binding transcription regulators until target regulons, "
            "effector ligands, and regulatory directions are experimentally resolved."
        ),
        "status": "DRAFT",
        "evidence": [
            {
                "source_id": "file:projects/P_PUTIDA/batches/module_regulation_signal_transduction_lysr_transcriptional_regulators.tsv",
                "title": "PSEPK regulation-bucket LysR split",
                "statement": "The functional-bucket partition groups 107 LysR-family transcriptional regulators for family-level first-pass curation.",
            }
        ],
        "notes": (
            "This module is a boundary/regulator-family grouping, not one satisfiable pathway. "
            "Direct pathway-process annotations on named TrpI, MetR, LysR, and other regulators are "
            "treated as pathway association rather than catalytic participation unless a curated anchor "
            "review supports pathway-specific transcription activation."
        ),
        "module": {
            "id": "lysr_transcriptional_regulator_boundary",
            "label": "LysR-family transcriptional regulator boundary",
            "module_type": "REGULATORY_STEP",
            "concepts": [
                module_term("GO:0003700"),
                module_term("GO:0001216"),
                module_term("GO:0000976"),
                module_term("GO:0006355"),
                module_term("GO:0045893"),
            ],
            "parts": [
                grouped_part(
                    1,
                    "Pathway-associated named LysR regulators",
                    "pathway_associated_named_lysr_regulators",
                    "Pathway-associated named LysR regulators",
                    "Named LysR-family regulators linked by product names or existing curation to aromatic or amino-acid pathway regulation.",
                    [
                        annoton(
                            gene,
                            f"{gene}: pathway-associated LysR regulator",
                            "GO:0001216" if gene in ACTIVATOR_GENES or gene in {"pcaQ", "galR", "catR"} else "GO:0003700",
                            ["GO:0045893"] if gene in ACTIVATOR_GENES or gene in {"pcaQ", "galR", "catR"} else ["GO:0006355"],
                            "Named LysR-family regulator with pathway association but usually unresolved KT2440 regulon details.",
                        )
                        for gene in pathway_named
                    ],
                ),
                grouped_part(
                    2,
                    "Named non-pathway or side-context LysR regulators",
                    "named_side_context_lysr_regulators",
                    "Named side-context LysR regulators",
                    "Named or operon-labeled LysR-family regulators whose exact regulons remain outside the current pathway modules.",
                    [
                        annoton(
                            gene,
                            f"{gene}: named LysR-family transcription regulator",
                            "GO:0003700",
                            ["GO:0006355"],
                            "Named LysR-family transcription regulator with unresolved target regulon.",
                        )
                        for gene in named_side
                    ],
                ),
                grouped_part(
                    3,
                    "Generic LysR-family transcription regulators",
                    "generic_lysr_family_transcription_regulators",
                    "Generic LysR-family transcription regulators",
                    "Large set of LysR-family paralogs curated to shared DNA-binding transcription-factor activity pending regulon evidence.",
                    [
                        annoton(
                            gene,
                            f"{gene}: generic LysR-family transcription regulator",
                            "GO:0003700",
                            ["GO:0006355"],
                            "Generic LysR-family transcription regulator with unresolved effector ligand and regulon.",
                        )
                        for gene in generic
                    ],
                ),
            ],
        },
    }
    MODULE_PATH.write_text(
        yaml.dump(doc, Dumper=NoAliasDumper, sort_keys=False, allow_unicode=False, width=100),
        encoding="utf-8",
    )
    print(f"Wrote {MODULE_PATH.relative_to(ROOT)}")


def main() -> None:
    for gene in GENES:
        curate_gene(gene)
    build_module()


if __name__ == "__main__":
    main()
