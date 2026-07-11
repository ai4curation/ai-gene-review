#!/usr/bin/env python3
"""First-pass curate the PSEPK ThiJ/DJ-1/PfpI stress split."""

from __future__ import annotations

import csv
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[2]
GENE_ROOT = ROOT / "genes" / "PSEPK"
BATCH_DIR = ROOT / "projects" / "P_PUTIDA" / "batches"
BATCH_TSV = BATCH_DIR / "module_stress_detoxification_thij_dj1_pfpi_detoxification_candidates.tsv"
PARTITION_TSV = BATCH_DIR / "module_stress_detoxification_partition.tsv"
MODULE_YAML = ROOT / "modules" / "stress_detoxification_spillover_boundary.yaml"


class NoAliasDumper(yaml.SafeDumper):
    def ignore_aliases(self, data):
        return True


TERM = {
    "GO:0005737": {"id": "GO:0005737", "label": "cytoplasm"},
    "GO:0019172": {"id": "GO:0019172", "label": "glyoxalase III activity"},
    "GO:0051596": {"id": "GO:0051596", "label": "methylglyoxal catabolic process"},
}


GENE_INFO = {
    "PP_2491": {
        "accession": "Q88K02",
        "role": "HSP31-like glutathione-independent glyoxalase candidate",
        "description": (
            "PP_2491 encodes a cytoplasmic ThiJ/PfpI/DJ-1-family, HSP31-like protein in Pseudomonas putida KT2440. "
            "TreeGrafter/PANTHER and DJ-1/PfpI domain evidence support glyoxalase III activity, a glutathione-independent "
            "conversion of methylglyoxal to D-lactate, and methylglyoxal catabolic process context."
        ),
    },
    "PP_2992": {
        "accession": "Q88IK7",
        "role": "HSP31-like glutathione-independent glyoxalase candidate",
        "description": (
            "PP_2992 encodes a cytoplasmic DJ-1/PfpI domain-containing, HSP31-like protein in Pseudomonas putida KT2440. "
            "TreeGrafter/PANTHER and DJ-1/PfpI domain evidence support glyoxalase III activity, a glutathione-independent "
            "conversion of methylglyoxal to D-lactate, and methylglyoxal catabolic process context."
        ),
    },
    "PP_3431": {
        "accession": "Q88HC9",
        "role": "HSP31-like glutathione-independent glyoxalase candidate",
        "description": (
            "PP_3431 encodes a cytoplasmic ThiJ/PfpI/DJ-1-family, HSP31-like protein in Pseudomonas putida KT2440. "
            "TreeGrafter/PANTHER and DJ-1/PfpI domain evidence support glyoxalase III activity, a glutathione-independent "
            "conversion of methylglyoxal to D-lactate, and methylglyoxal catabolic process context."
        ),
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


def first_prefixed_lines(path: Path, prefix: str, limit: int = 3) -> list[str]:
    return [line for line in read_lines(path) if line.startswith(prefix)][:limit]


def file_id(gene: str, suffix: str) -> str:
    return f"file:PSEPK/{gene}/{gene}-{suffix}"


def support(reference_id: str, text: str) -> dict[str, str]:
    return {"reference_id": reference_id, "supporting_text": text}


def add_unique(items: list[dict[str, str]], item: dict[str, str]) -> None:
    if item["supporting_text"] not in {existing["supporting_text"] for existing in items}:
        items.append(item)


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
            add_unique(data, support(file_id(gene, "uniprot.txt"), line))
    for marker in (
        ("CC   -!- SIMILARITY:",),
        ("DR   PANTHER;",),
        ("DR   Pfam;",),
        ("FT   DOMAIN",),
    ):
        line = optional_first_line(uniprot, *marker)
        if line:
            add_unique(data, support(file_id(gene, "uniprot.txt"), line))
    for line in first_prefixed_lines(uniprot, "DR   InterPro;", 4):
        add_unique(data, support(file_id(gene, "uniprot.txt"), line))
    return data


def asta_evidence(gene: str) -> list[dict[str, str]]:
    asta = GENE_ROOT / gene / f"{gene}-deep-research-asta.md"
    data = [support(file_id(gene, "deep-research-asta.md"), first_line(asta, "  uniprot_accession:"))]
    for marker in ("  protein_description:", "  protein_family:", "  protein_domains:"):
        line = optional_first_line(asta, marker)
        if line:
            add_unique(data, support(file_id(gene, "deep-research-asta.md"), line))
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
            "summary": "Cytoplasmic localization is compatible with the soluble HSP31-like DJ-1/PfpI enzyme context.",
            "action": "ACCEPT",
            "reason": "The cytoplasm row is TreeGrafter-derived and fits the soluble DJ-1/PfpI/HSP31-like family context.",
            "supported_by": standard_support(gene, term_id),
        }
    if term_id == "GO:0019172":
        return {
            "summary": "Glyoxalase III activity is the supported direct molecular function for this HSP31-like DJ-1/PfpI candidate.",
            "action": "ACCEPT",
            "reason": (
                "The annotation is a TreeGrafter/PANTHER call to the HSP31-like DJ-1/PfpI subfamily. QuickGO confirms "
                "GO:0019172 as the active glutathione-independent methylglyoxal-to-D-lactate activity, so this is the "
                "right direct molecular-function term for the first pass."
            ),
            "supported_by": standard_support(gene, term_id),
        }
    if term_id == "GO:0051596":
        return {
            "summary": "Methylglyoxal catabolic process is the appropriate process context inferred from glyoxalase III activity.",
            "action": "ACCEPT",
            "reason": (
                "The GOA row is a logical-inference process annotation from GO:0019172. It is retained as broad process "
                "context for detoxification of methylglyoxal; no separate protein-deglycase or nucleotide-deglycase term "
                "is added in this first pass."
            ),
            "supported_by": standard_support(gene, term_id),
        }
    raise ValueError(f"No review rule for {gene} {term_id}")


def core_for(gene: str) -> dict:
    return {
        "description": GENE_INFO[gene]["role"],
        "molecular_function": TERM["GO:0019172"],
        "directly_involved_in": [TERM["GO:0051596"]],
        "locations": [TERM["GO:0005737"]],
        "supported_by": standard_support(gene, "GO:0019172"),
    }


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
                f"Does {gene} function as a bona fide glutathione-independent glyoxalase III enzyme in KT2440 cells, "
                "and what stress conditions induce or require it?"
            )
        }
    ]
    data["suggested_experiments"] = [
        {
            "experiment_type": "methylglyoxal detoxification assay",
            "description": (
                f"Measure methylglyoxal-to-D-lactate conversion by purified {gene} and compare wild-type, deletion, "
                "and complemented strains for methylglyoxal sensitivity and D-lactate accumulation."
            ),
        }
    ]
    path.write_text(yaml.dump(data, Dumper=NoAliasDumper, sort_keys=False, width=120), encoding="utf-8")


def write_notes(gene: str) -> None:
    evidence = standard_support(gene, "GO:0019172")
    lines = [
        f"# {gene} notes",
        "",
        "2026-07-10: First-pass ThiJ/DJ-1/PfpI stress-bucket curation.",
        GENE_INFO[gene]["description"],
        "",
        "Primary provenance:",
    ]
    for item in evidence[:8]:
        lines.append(f"- [{item['reference_id']} \"{item['supporting_text']}\"]")
    lines.extend(
        [
            "",
            "Decision: accept the TreeGrafter/PANTHER glyoxalase III activity and methylglyoxal catabolic process at the "
            "family-supported level. Do not add protein-deglycase or nucleotide-deglycase terms without gene-specific "
            "or subfamily-specific evidence beyond the broad DJ-1/PfpI domain metadata.",
        ]
    )
    (GENE_ROOT / gene / f"{gene}-notes.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def descriptor(term_id: str, description: str) -> dict:
    return {"preferred_term": TERM[term_id]["label"], "term": TERM[term_id], "description": description}


def gene_ref(gene: str) -> dict:
    return {"selector_type": "GENE", "gene": {"preferred_term": gene}}


def annoton(gene: str) -> dict:
    return {
        "id": f"{gene}_glyoxalase_iii",
        "label": f"{gene}: HSP31-like glyoxalase III candidate",
        "participant": gene_ref(gene),
        "function": {
            "preferred_term": TERM["GO:0019172"]["label"],
            "term": TERM["GO:0019172"],
            "substrates": [{"preferred_term": "methylglyoxal"}],
            "products": [{"preferred_term": "D-lactate"}],
        },
        "processes": [{"preferred_term": TERM["GO:0051596"]["label"], "term": TERM["GO:0051596"]}],
        "locations": [{"preferred_term": TERM["GO:0005737"]["label"], "term": TERM["GO:0005737"]}],
        "role_description": "HSP31-like DJ-1/PfpI methylglyoxal-detoxification side node.",
    }


def write_module() -> None:
    genes = list(GENE_INFO)
    module = {
        "id": "MODULE:stress_detoxification_spillover_boundary",
        "title": "Stress detoxification spillover boundary",
        "description": (
            "Boundary module for Pseudomonas putida KT2440 stress/detoxification spillover genes that are real stress "
            "or damage-response candidates but do not form one coherent peroxide, glutathione, metal-resistance, "
            "universal-stress, or heat-shock pathway. This first version records the ThiJ/DJ-1/PfpI split as "
            "HSP31-like glutathione-independent glyoxalase III/methylglyoxal detoxification context."
        ),
        "status": "DRAFT",
        "evidence": [
            {
                "source_id": "file:projects/P_PUTIDA/batches/module_stress_detoxification_thij_dj1_pfpi_detoxification_candidates.tsv",
                "title": "PSEPK stress/detoxification ThiJ/DJ-1/PfpI split",
                "statement": (
                    "The batch table records PP_2491, PP_2992, and PP_3431 as ThiJ/DJ-1/PfpI stress/detoxification candidates."
                ),
            },
            {
                "source_id": "file:interpro/panther/PTHR48094/PTHR48094-metadata.yaml",
                "title": "PANTHER PTHR48094 protein/nucleic acid deglycase family metadata",
                "statement": (
                    "PTHR48094 is the protein/nucleic acid deglycase family; the PSEPK candidates are assigned to the "
                    "HSP31-related glutathione-independent glyoxalase subfamily in UniProt/PANTHER metadata."
                ),
            },
        ]
        + [
            {
                "source_id": f"file:PSEPK/{gene}/{gene}-ai-review.yaml",
                "title": f"Curated {gene} review",
                "statement": (
                    f"The {gene} review accepts cytoplasm, glyoxalase III activity, and methylglyoxal catabolic process "
                    "from TreeGrafter/PANTHER and DJ-1/PfpI domain evidence."
                ),
            }
            for gene in genes
        ],
        "module": {
            "id": "stress_detoxification_spillover_boundary",
            "label": "Stress detoxification spillover boundary",
            "module_type": "BIOLOGICAL_PROCESS",
            "concepts": [
                {
                    "preferred_term": "ThiJ/DJ-1/PfpI HSP31-like family",
                    "description": (
                        "DJ-1/PfpI domain proteins in the HSP31-like peptidase C56 family, represented here as "
                        "methylglyoxal-detoxification candidates."
                    ),
                },
                descriptor(
                    "GO:0019172",
                    "Direct molecular function for the HSP31-like glutathione-independent methylglyoxal-to-D-lactate activity.",
                ),
                descriptor(
                    "GO:0051596",
                    "Detoxification process context inferred from glyoxalase III activity.",
                ),
            ],
            "context": {
                "cellular_components": [
                    descriptor("GO:0005737", "TreeGrafter places the three HSP31-like candidates in the cytoplasm.")
                ]
            },
            "parts": [
                {
                    "order": 1,
                    "role": "ThiJ/DJ-1/PfpI methylglyoxal-detoxification candidates",
                    "node": {
                        "id": "thij_dj1_pfpi_glyoxalase_candidates",
                        "label": "HSP31-like ThiJ/DJ-1/PfpI glyoxalase III candidates",
                        "module_type": "MOLECULAR_FUNCTION",
                        "description": (
                            "PP_2491, PP_2992, and PP_3431 are HSP31-like DJ-1/PfpI proteins with TreeGrafter/PANTHER "
                            "support for glyoxalase III activity and methylglyoxal catabolism. This part records the "
                            "methylglyoxal-detoxification call without asserting protein- or nucleotide-deglycase activity."
                        ),
                        "annotons": [annoton(gene) for gene in genes],
                    },
                }
            ],
            "notes": (
                "This boundary is intended for compact stress/detoxification spillover splits. The current HSP31-like "
                "sub-batch is biochemically coherent, but it remains separate from glutathione-dependent GloA/GloB "
                "glyoxalase chemistry and from generic stress-response regulation."
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
