#!/usr/bin/env python3
"""First-pass curate the PSEPK universal-stress-protein stress split."""

from __future__ import annotations

import csv
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[2]
GENE_ROOT = ROOT / "genes" / "PSEPK"
BATCH_DIR = ROOT / "projects" / "P_PUTIDA" / "batches"
BATCH_TSV = BATCH_DIR / "module_stress_detoxification_universal_stress_proteins.tsv"
PARTITION_TSV = BATCH_DIR / "module_stress_detoxification_partition.tsv"
MODULE_YAML = ROOT / "modules" / "universal_stress_protein_boundary.yaml"


class NoAliasDumper(yaml.SafeDumper):
    def ignore_aliases(self, data):
        return True


TERM = {
    "GO:0005737": {"id": "GO:0005737", "label": "cytoplasm"},
}


GENE_INFO = {
    "PP_1269": {
        "role": "single-domain universal stress protein family member",
        "description": (
            "PP_1269 encodes a single-domain Universal Stress Protein A-family protein in Pseudomonas putida KT2440. "
            "The first-pass evidence supports only USP-family/domain context; no specific molecular activity, substrate, "
            "or stress-response process is assigned."
        ),
        "locations": [],
    },
    "PP_2132": {
        "role": "cytoplasmic single-domain universal stress protein",
        "description": (
            "PP_2132 encodes a cytoplasmic single-domain Universal Stress Protein A-family protein in Pseudomonas putida KT2440. "
            "The first-pass evidence supports USP-family context and cytoplasmic localization, but no specific molecular "
            "activity or stress-response process."
        ),
        "locations": [TERM["GO:0005737"]],
    },
    "PP_2187": {
        "role": "cytoplasmic tandem-USP stress-associated protein candidate",
        "description": (
            "PP_2187 encodes a cytoplasmic tandem-domain Universal Stress Protein A-family protein in Pseudomonas putida KT2440. "
            "UniProt transfers a DNA-damaging-agent resistance comment by similarity, but this first pass treats that as "
            "context rather than a gene-specific GO process annotation."
        ),
        "locations": [TERM["GO:0005737"]],
    },
    "PP_2326": {
        "role": "single-domain universal stress protein",
        "description": (
            "PP_2326 encodes a single-domain Universal Stress Protein A-family protein in Pseudomonas putida KT2440. "
            "The first-pass evidence supports only USP-family/domain context; no specific molecular activity, substrate, "
            "localization, or stress-response process is assigned."
        ),
        "locations": [],
    },
    "PP_2648": {
        "role": "cytoplasmic tandem-USP family protein",
        "description": (
            "PP_2648 encodes a cytoplasmic tandem-domain Universal Stress Protein A-family protein in Pseudomonas putida KT2440. "
            "The first-pass evidence supports USP-family context and cytoplasmic localization, but no specific molecular "
            "activity or stress-response process."
        ),
        "locations": [TERM["GO:0005737"]],
    },
    "PP_2745": {
        "role": "cytoplasmic universal-stress-protein candidate with DNA-damage-resistance context",
        "description": (
            "PP_2745 encodes a cytoplasmic Universal Stress Protein A-family protein in Pseudomonas putida KT2440. "
            "UniProt transfers a DNA-damaging-agent resistance comment by similarity, but this first pass treats that as "
            "context rather than a gene-specific GO process annotation."
        ),
        "locations": [TERM["GO:0005737"]],
    },
    "PP_3156": {
        "role": "cytoplasmic tandem-USP stress-associated protein candidate",
        "description": (
            "PP_3156 encodes a cytoplasmic tandem-domain Universal Stress Protein A-family protein in Pseudomonas putida KT2440. "
            "UniProt transfers a DNA-damaging-agent resistance comment by similarity, but this first pass treats that as "
            "context rather than a gene-specific GO process annotation."
        ),
        "locations": [TERM["GO:0005737"]],
    },
    "PP_3237": {
        "role": "cytoplasmic tandem-USP stress-associated protein candidate",
        "description": (
            "PP_3237 encodes a cytoplasmic tandem-domain Universal Stress Protein A-family protein in Pseudomonas putida KT2440. "
            "UniProt transfers a DNA-damaging-agent resistance comment by similarity, but this first pass treats that as "
            "context rather than a gene-specific GO process annotation."
        ),
        "locations": [TERM["GO:0005737"]],
    },
    "PP_3288": {
        "role": "cytoplasmic universal-stress-protein candidate with DNA-damage-resistance context",
        "description": (
            "PP_3288 encodes a cytoplasmic Universal Stress Protein A-family protein in Pseudomonas putida KT2440. "
            "UniProt transfers a DNA-damaging-agent resistance comment by similarity, but this first pass treats that as "
            "context rather than a gene-specific GO process annotation."
        ),
        "locations": [TERM["GO:0005737"]],
    },
    "PP_3290": {
        "role": "cytoplasmic tandem-USP stress-associated protein candidate",
        "description": (
            "PP_3290 encodes a cytoplasmic tandem-domain Universal Stress Protein A-family protein in Pseudomonas putida KT2440. "
            "UniProt transfers a DNA-damaging-agent resistance comment by similarity, but this first pass treats that as "
            "context rather than a gene-specific GO process annotation."
        ),
        "locations": [TERM["GO:0005737"]],
    },
    "PP_3294": {
        "role": "cytoplasmic tandem-USP stress-associated protein candidate",
        "description": (
            "PP_3294 encodes a cytoplasmic tandem-domain Universal Stress Protein A-family protein in Pseudomonas putida KT2440. "
            "UniProt transfers a DNA-damaging-agent resistance comment by similarity, but this first pass treats that as "
            "context rather than a gene-specific GO process annotation."
        ),
        "locations": [TERM["GO:0005737"]],
    },
}


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def read_lines(path: Path) -> list[str]:
    return read_text(path).splitlines()


def first_line(path: Path, *needles: str) -> str:
    for line in read_lines(path):
        if all(needle in line for needle in needles):
            return line
    raise ValueError(f"No line in {path} contains all needles: {needles}")


def optional_first_line(path: Path, *needles: str) -> str | None:
    for line in read_lines(path):
        if all(needle in line for needle in needles):
            return line
    return None


def file_id(gene: str, suffix: str) -> str:
    return f"file:PSEPK/{gene}/{gene}-{suffix}"


def support(reference_id: str, text: str) -> dict[str, str]:
    return {"reference_id": reference_id, "supporting_text": text}


def goa_support(gene: str, term_id: str) -> dict[str, str] | None:
    line = optional_first_line(GENE_ROOT / gene / f"{gene}-goa.tsv", term_id)
    if not line:
        return None
    return support(file_id(gene, "goa.tsv"), line)


def uniprot_evidence(gene: str, term_id: str | None = None) -> list[dict[str, str]]:
    uniprot = GENE_ROOT / gene / f"{gene}-uniprot.txt"
    data = [support(file_id(gene, "uniprot.txt"), first_line(uniprot, "DE   "))]
    if term_id:
        line = optional_first_line(uniprot, f"DR   GO; {term_id};")
        if line:
            data.append(support(file_id(gene, "uniprot.txt"), line))
    for marker in (
        ("CC   -!- FUNCTION:",),
        ("CC   -!- SUBUNIT:",),
        ("CC   -!- SUBCELLULAR LOCATION:",),
        ("CC   -!- SIMILARITY:",),
        ("DR   InterPro;",),
        ("DR   Pfam;",),
        ("FT   DOMAIN",),
    ):
        line = optional_first_line(uniprot, *marker)
        if line and line not in {item["supporting_text"] for item in data}:
            data.append(support(file_id(gene, "uniprot.txt"), line))
    return data


def asta_evidence(gene: str) -> list[dict[str, str]]:
    asta = GENE_ROOT / gene / f"{gene}-deep-research-asta.md"
    data = [support(file_id(gene, "deep-research-asta.md"), first_line(asta, "  protein_description:"))]
    for marker in ("  protein_family:", "  protein_domains:"):
        line = optional_first_line(asta, marker)
        if line:
            data.append(support(file_id(gene, "deep-research-asta.md"), line))
    return data


def standard_support(gene: str, term_id: str | None = None) -> list[dict[str, str]]:
    data: list[dict[str, str]] = []
    if term_id:
        goa = goa_support(gene, term_id)
        if goa:
            data.append(goa)
    data.extend(uniprot_evidence(gene, term_id))
    data.extend(asta_evidence(gene))
    return data


def reference_list(existing_refs: list[dict], gene: str, accession: str) -> list[dict]:
    refs: list[dict] = []
    seen = set()
    for ref in existing_refs:
        ref_id = ref["id"]
        seen.add(ref_id)
        refs.append(ref)
    titles = {
        file_id(gene, "goa.tsv"): f"QuickGO GOA annotations for {gene} ({accession})",
        file_id(gene, "uniprot.txt"): f"UniProtKB entry for {gene} ({accession})",
        file_id(gene, "deep-research-asta.md"): f"Asta retrieval report for {gene} ({accession})",
    }
    for ref_id, title in titles.items():
        if ref_id not in seen:
            refs.append({"id": ref_id, "title": title, "findings": []})
    return refs


def review_for_annotation(gene: str, term_id: str) -> dict:
    if term_id == "GO:0005737":
        return {
            "summary": "Cytoplasmic localization is compatible with the soluble USP-family protein context.",
            "action": "ACCEPT",
            "reason": (
                "The GOA row comes from UniProt subcellular-location mapping, and the UniProt entry itself records "
                "cytoplasmic localization for this USP-family protein. This localization is useful context but not a "
                "pathway-defining molecular function."
            ),
            "supported_by": standard_support(gene, term_id),
        }
    raise ValueError(f"No review rule for {gene} {term_id}")


def core_for(gene: str) -> dict:
    info = GENE_INFO[gene]
    core = {
        "description": info["role"],
        "supported_by": standard_support(gene, "GO:0005737" if info["locations"] else None),
    }
    if info["locations"]:
        core["locations"] = info["locations"]
    return core


def apply_review(gene: str, accession: str) -> None:
    path = GENE_ROOT / gene / f"{gene}-ai-review.yaml"
    data = yaml.safe_load(read_text(path))
    data["gene_symbol"] = gene
    data["status"] = "DRAFT"
    data["description"] = GENE_INFO[gene]["description"]
    data["references"] = reference_list(data.get("references") or [], gene, accession)
    existing = data.get("existing_annotations") or []
    for annotation in existing:
        annotation["review"] = review_for_annotation(gene, annotation["term"]["id"])
    data["existing_annotations"] = existing
    data["core_functions"] = [core_for(gene)]
    data["proposed_new_terms"] = []
    data["suggested_questions"] = [
        {
            "question": (
                f"What molecular activity, if any, and which stress condition define the physiological role of {gene} "
                "in Pseudomonas putida KT2440?"
            )
        }
    ]
    data["suggested_experiments"] = [
        {
            "description": (
                f"Test a clean {gene} deletion and complemented strain across starvation, oxidative, osmotic, heat, and "
                "DNA-damaging stress panels, then assay nucleotide binding or other biochemical activity only if sequence "
                "or structural evidence supports it."
            ),
            "experiment_type": "stress-phenotyping and targeted biochemical assay",
        }
    ]
    path.write_text(yaml.dump(data, Dumper=NoAliasDumper, sort_keys=False, width=120), encoding="utf-8")


def write_notes(gene: str) -> None:
    info = GENE_INFO[gene]
    evidence = standard_support(gene, "GO:0005737" if info["locations"] else None)
    lines = [
        f"# {gene} notes",
        "",
        "2026-07-10: First-pass universal-stress-protein stress-bucket curation.",
        info["description"],
        "",
        "Primary provenance:",
    ]
    for item in evidence[:6]:
        lines.append(f"- [{item['reference_id']} \"{item['supporting_text']}\"]")
    lines.extend(
        [
            "",
            "Decision: keep the assignment conservative. The records support USP-family/domain context and, for most genes, "
            "cytoplasmic localization. They do not support a specific molecular function, substrate, ATP-binding claim, or "
            "stress-response GO process in this first pass.",
        ]
    )
    (GENE_ROOT / gene / f"{gene}-notes.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def descriptor(term_id: str, description: str) -> dict:
    term = TERM[term_id]
    return {"preferred_term": term["label"], "term": term, "description": description}


def gene_ref(gene: str) -> dict:
    return {"selector_type": "GENE", "gene": {"preferred_term": gene}}


def annoton(annoton_id: str, label: str, gene: str, role_description: str, cytoplasm: bool) -> dict:
    item = {
        "id": annoton_id,
        "label": label,
        "participant": gene_ref(gene),
        "role_description": role_description,
    }
    if cytoplasm:
        item["locations"] = [{"preferred_term": TERM["GO:0005737"]["label"], "term": TERM["GO:0005737"]}]
    return item


def write_module() -> None:
    single = ["PP_1269", "PP_2132", "PP_2326"]
    dna_context = ["PP_2187", "PP_2745", "PP_3156", "PP_3237", "PP_3288", "PP_3290", "PP_3294"]
    other_tandem = ["PP_2648"]
    module = {
        "id": "MODULE:universal_stress_protein_boundary",
        "title": "Universal stress protein boundary",
        "description": (
            "Boundary module for the Pseudomonas putida KT2440 Universal Stress Protein A-family split from the "
            "stress/detoxification functional bucket. The module records USP-family candidates and their supported "
            "localization/domain context without forcing a shared molecular activity or a specific stress-response process."
        ),
        "status": "DRAFT",
        "evidence": [
            {
                "source_id": "file:projects/P_PUTIDA/batches/module_stress_detoxification_universal_stress_proteins.tsv",
                "title": "PSEPK stress/detoxification universal-stress-protein split",
                "statement": (
                    "The batch table records eleven PSEPK stress/detoxification genes assigned to the universal-stress-protein "
                    "split: PP_1269, PP_2132, PP_2187, PP_2326, PP_2648, PP_2745, PP_3156, PP_3237, PP_3288, PP_3290, and PP_3294."
                ),
            },
            {
                "source_id": "file:projects/P_PUTIDA/batches/module_stress_detoxification_partition.tsv",
                "title": "PSEPK stress/detoxification functional-bucket partition",
                "statement": (
                    "The stress/detoxification umbrella was partitioned into peroxide/peroxiredoxin, glutathione/thiol, "
                    "arsenic/copper metal resistance, universal-stress-protein, cold/heat-shock, ThiJ/DJ-1/PfpI, and "
                    "miscellaneous stress-regulatory splits."
                ),
            },
        ],
        "module": {
            "id": "universal_stress_protein_boundary",
            "label": "Universal stress protein boundary",
            "module_type": "MODULE",
            "concepts": [
                {
                    "preferred_term": "Universal Stress Protein A family",
                    "description": "USP-family/domain context supported by UniProt, Pfam PF00582, and InterPro UspA records.",
                }
            ],
            "context": {
                "cellular_components": [
                    descriptor("GO:0005737", "Most reviewed USP-family entries carry UniProt subcellular-location mapping to cytoplasm.")
                ]
            },
            "parts": [
                {
                    "order": 1,
                    "role": "Single-domain USP-family candidates",
                    "node": {
                        "id": "single_domain_usp_candidates",
                        "label": "Single-domain Universal Stress Protein A-family candidates",
                        "module_type": "MODULE",
                        "description": (
                            "PP_1269, PP_2132, and PP_2326 are single-domain USP-family proteins. PP_2132 has supported "
                            "cytoplasmic localization; PP_1269 and PP_2326 currently have no GOA rows."
                        ),
                        "annotons": [
                            annoton(
                                f"{gene}_single_domain_usp",
                                f"{gene}: single-domain USP-family protein",
                                gene,
                                "USP-family candidate with no resolved molecular activity in this first pass.",
                                bool(GENE_INFO[gene]["locations"]),
                            )
                            for gene in single
                        ],
                    },
                },
                {
                    "order": 2,
                    "role": "Tandem-USP family candidates",
                    "node": {
                        "id": "tandem_usp_candidates",
                        "label": "Tandem-domain Universal Stress Protein A-family candidates",
                        "module_type": "MODULE",
                        "description": (
                            "Several PSEPK USP-family proteins have tandem USP domains. The first-pass reviews retain "
                            "cytoplasmic localization where present but do not assign ATP binding or a specific stress process."
                        ),
                        "annotons": [
                            annoton(
                                f"{gene}_tandem_usp",
                                f"{gene}: tandem-domain USP-family protein",
                                gene,
                                "Tandem-domain USP-family candidate with no resolved molecular activity in this first pass.",
                                bool(GENE_INFO[gene]["locations"]),
                            )
                            for gene in other_tandem + dna_context
                        ],
                    },
                },
                {
                    "order": 3,
                    "role": "DNA-damaging-agent resistance context",
                    "node": {
                        "id": "dna_damaging_agent_resistance_context",
                        "label": "Transferred DNA-damaging-agent resistance context",
                        "module_type": "BIOLOGICAL_PROCESS",
                        "description": (
                            "PP_2187, PP_2745, PP_3156, PP_3237, PP_3288, PP_3290, and PP_3294 carry a UniProt transferred "
                            "comment stating that the protein is required for resistance to DNA-damaging agents. This is kept "
                            "as contextual evidence only; no gene-specific DNA-damage-response GO process is proposed."
                        ),
                        "annotons": [
                            annoton(
                                f"{gene}_dna_damage_context",
                                f"{gene}: USP-family DNA-damaging-agent resistance context",
                                gene,
                                "UniProt-by-similarity DNA-damaging-agent resistance context; not promoted to a GO process in this pass.",
                                True,
                            )
                            for gene in dna_context
                        ],
                    },
                },
            ],
            "notes": (
                "Open curation questions: determine whether any PSEPK USP proteins bind ATP or another nucleotide, "
                "which environmental or DNA-damaging stresses induce each paralog, and whether tandem-domain USP proteins "
                "have nonredundant phenotypes. Until then, avoid assigning specific MF or BP terms beyond supported localization."
            ),
        },
    }
    MODULE_YAML.write_text(yaml.dump(module, Dumper=NoAliasDumper, sort_keys=False, width=120), encoding="utf-8")


def update_batch_status(path: Path, genes: set[str]) -> None:
    rows = list(csv.DictReader(path.open(encoding="utf-8"), delimiter="\t"))
    if not rows:
        return
    for row in rows:
        if row["gene"] in genes:
            row["recommended_action"] = "COMPLETED_SUBMODULE"
            row["bucket_status"] = "CURATED"
            row["review_status"] = "PRESENT"
            row["curation_status"] = "CURATED"
            row["asta_research_status"] = "PRESENT"
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=rows[0].keys(), delimiter="\t")
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    rows = list(csv.DictReader(BATCH_TSV.open(encoding="utf-8"), delimiter="\t"))
    genes = {row["gene"] for row in rows}
    for row in rows:
        gene = row["gene"]
        apply_review(gene, row["uniprot_accession"])
        write_notes(gene)
        print(f"Curated {gene}")
    write_module()
    update_batch_status(BATCH_TSV, genes)
    update_batch_status(PARTITION_TSV, genes)
    print(f"Wrote {MODULE_YAML.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
