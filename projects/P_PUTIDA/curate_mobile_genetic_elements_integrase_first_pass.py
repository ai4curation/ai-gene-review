#!/usr/bin/env python3
"""First-pass curation for PSEPK broad-bucket mobile-element integrase candidates."""

from __future__ import annotations

from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[2]
GENE_ROOT = ROOT / "genes" / "PSEPK"
MODULE_PATH = ROOT / "modules" / "mobile_genetic_elements_boundary.yaml"
BATCH_TSV = ROOT / "projects/P_PUTIDA/batches/module_mobile_genetic_elements_integrase_mobile_element_context.tsv"


class NoAliasDumper(yaml.SafeDumper):
    def ignore_aliases(self, data):
        return True


TERM = {
    "GO:0003677": {"id": "GO:0003677", "label": "DNA binding"},
    "GO:0015074": {"id": "GO:0015074", "label": "DNA integration"},
}

GENES = ["PP_1963", "PP_2825", "PP_3677"]
SUPPORTED_INTEGRASES = {"PP_2825"}
UNRESOLVED_INTEGRASES = {"PP_1963", "PP_3677"}


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
    for marker in ("Belongs to the 'phage' integrase family", "DR   PANTHER; PTHR30629", "DR   Pfam; PF22022"):
        add_unique(items, support(file_id(gene, "uniprot.txt"), optional_first_line(path, marker)))
    asta = gene_file(gene, "deep-research-asta.md")
    add_unique(items, support(file_id(gene, "deep-research-asta.md"), optional_first_line(asta, "uniprot_accession:")))
    add_unique(items, support(file_id(gene, "deep-research-asta.md"), optional_first_line(asta, "protein_description:")))
    add_unique(items, support(file_id(gene, "deep-research-asta.md"), optional_first_line(asta, "protein_family:")))
    add_unique(items, support(file_id(gene, "deep-research-asta.md"), optional_first_line(asta, "protein_domains:")))
    return items


def description_for(gene: str) -> str:
    product = (product_line(gene) or "integrase candidate").removeprefix("DE   ").rstrip(".")
    if gene in SUPPORTED_INTEGRASES:
        return (
            f"{gene} encodes a phage-integrase-family DNA-binding protein ({product}) with integrase/recombinase "
            "domain support. It is associated with mobile-element DNA integration, likely through DNA recognition at "
            "phage or integrative-element attachment sites."
        )
    return (
        f"{gene} encodes a large protein currently labeled as an integrase ({product}). The local record lacks conserved "
        "family or catalytic-domain support, so its mobile-element role and molecular activity remain unresolved."
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
    if term_id == "GO:0003677":
        return {
            "summary": "DNA binding is the supported molecular-function evidence for this phage-integrase-family protein.",
            "action": "ACCEPT",
            "reason": "The fetched GOA row and UniProt phage-integrase domains support a DNA-binding role. A more specific catalytic recombinase activity is not asserted without a corresponding local annotation.",
            "supported_by": evidence_for(gene, term_id, ("DNA_brk_join_enz", "Integrase_recombinase_N", "Phage_Integrase")),
        }
    if term_id == "GO:0015074":
        return {
            "summary": "DNA integration is supported by the UniProt GO cross-reference and phage-integrase domain context.",
            "action": "NEW",
            "reason": "The UniProt flat file records DNA integration for this phage-integrase-family protein, but the fetched GOA table did not include the process row. It is added as an authored first-pass annotation.",
            "supported_by": evidence_for(gene, term_id, ("Integrase_recombinase_N", "Phage_Integrase", "Phage_int_M")),
        }
    raise ValueError(f"No review rule for {gene} {term_id}")


def ensure_new_integration_row(data: dict, gene: str) -> None:
    if gene not in SUPPORTED_INTEGRASES:
        return
    rows = data.setdefault("existing_annotations", [])
    if any(row.get("term", {}).get("id") == "GO:0015074" for row in rows):
        return
    rows.append(
        {
            "term": TERM["GO:0015074"],
            "evidence_type": "IEA",
            "original_reference_id": file_id(gene, "uniprot.txt"),
            "qualifier": "involved_in",
            "review": review_for(gene, "GO:0015074"),
        }
    )


def core_functions_for(gene: str) -> list[dict]:
    if gene in UNRESOLVED_INTEGRASES:
        return []
    return [
        {
            "description": "Phage-integrase-family DNA binding associated with mobile-element DNA integration.",
            "supported_by": evidence_for(gene, "GO:0003677", ("DNA_brk_join_enz", "Integrase_recombinase_N", "Phage_Integrase")),
            "molecular_function": TERM["GO:0003677"],
            "directly_involved_in": [TERM["GO:0015074"]],
        }
    ]


def suggested_questions_for(gene: str) -> list[dict[str, str]]:
    if gene in SUPPORTED_INTEGRASES:
        question = f"What attachment-site substrate and partner factors define the mobile-element integration role of {gene}?"
    else:
        question = f"Does {gene} encode a real mobile-element integrase, and can conserved catalytic or DNA-binding features be detected beyond the product name?"
    return [{"question": question}]


def suggested_experiments_for(gene: str) -> list[dict[str, str]]:
    if gene in SUPPORTED_INTEGRASES:
        return [
            {
                "experiment_type": "site-specific integration assay",
                "description": f"Test {gene} with candidate phage or integrative-element attachment-site DNA substrates from its genomic neighborhood.",
                "hypothesis": f"{gene} binds integrase target DNA and contributes to mobile-element DNA integration.",
            }
        ]
    return [
        {
            "experiment_type": "domain validation and recombination assay",
            "description": f"Re-evaluate {gene} with sensitive profile/domain searches and test candidate DNA substrates only if catalytic or DNA-binding features are recovered.",
            "hypothesis": f"{gene} may be a highly diverged or misnamed mobile-element integrase candidate.",
        }
    ]


def curate_gene(gene: str) -> None:
    path = GENE_ROOT / gene / f"{gene}-ai-review.yaml"
    data = yaml.safe_load(path.read_text())
    data["status"] = "DRAFT"
    data["description"] = description_for(gene)
    ensure_references(data, gene)
    ensure_new_integration_row(data, gene)
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
    if gene in SUPPORTED_INTEGRASES:
        return {
            "id": f"{gene.lower()}_phage_integrase_dna_binding",
            "label": f"{gene}: phage-integrase-family DNA binding in DNA integration",
            "participant": participant(gene),
            "role_description": "phage-integrase-family DNA binding in DNA integration",
            "function": descriptor("GO:0003677"),
            "processes": [descriptor("GO:0015074")],
        }
    return {
        "id": f"{gene.lower()}_unresolved_integrase_context",
        "label": f"{gene}: unresolved product-name-only integrase candidate",
        "participant": participant(gene),
        "role_description": "unresolved product-name-only integrase candidate",
        "notes": "No fetched GOA rows and no conserved family/domain support in the local UniProt/Asta context; no core GO function asserted.",
    }


def add_or_replace_module_part() -> None:
    data = yaml.safe_load(MODULE_PATH.read_text())
    evidence = data.setdefault("evidence", [])
    source_id = "file:projects/P_PUTIDA/batches/module_mobile_genetic_elements_integrase_mobile_element_context.tsv"
    if not any(item.get("source_id") == source_id for item in evidence):
        evidence.append(
            {
                "source_id": source_id,
                "title": "PSEPK mobile-genetic-elements integrase split table",
                "statement": "The split table routes three broad mobile-genetic-elements genes to integrase/mobile-element context.",
            }
        )

    note = (
        "The module:mobile_genetic_elements integrase_mobile_element_context sub-batch adds three broad-bucket integrase "
        "candidates; PP_2825 is retained as a phage-integrase-family DNA-binding/integration protein, while PP_1963 and "
        "PP_3677 remain unresolved product-name-only candidates with no core GO function asserted."
    )
    current_notes = data.get("notes", "").replace(note, "").strip()
    data["notes"] = f"{current_notes} {note}".strip()

    parts = data["module"].setdefault("parts", [])
    parts[:] = [
        part
        for part in parts
        if part.get("node", {}).get("id") != "mobile_bucket_integrase_context"
    ]
    parts.append(
        {
            "order": max([part.get("order", 0) for part in parts] or [0]) + 1,
            "role": "Integrase candidates from broad mobile-genetic-elements bucket",
            "node": {
                "id": "mobile_bucket_integrase_context",
                "label": "Broad-bucket integrase candidates",
                "module_type": "BIOLOGICAL_PROCESS",
                "annotons": [annoton(gene) for gene in GENES],
            },
        }
    )
    MODULE_PATH.write_text(yaml.dump(data, Dumper=NoAliasDumper, sort_keys=False, allow_unicode=False, width=120), encoding="utf-8")


def main() -> None:
    if not BATCH_TSV.exists():
        raise FileNotFoundError(BATCH_TSV)
    for gene in GENES:
        curate_gene(gene)
    add_or_replace_module_part()
    print(f"Curated {len(GENES)} gene reviews")
    print(f"Updated {MODULE_PATH}")


if __name__ == "__main__":
    main()
