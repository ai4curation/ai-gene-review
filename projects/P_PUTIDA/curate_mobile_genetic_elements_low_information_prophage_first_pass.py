#!/usr/bin/env python3
"""First-pass curation for low-information PSEPK prophage proteins."""

from __future__ import annotations

from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[2]
GENE_ROOT = ROOT / "genes" / "PSEPK"
MODULE_PATH = ROOT / "modules" / "phage_structural_packaging_boundary.yaml"
BATCH_ID = "module_mobile_genetic_elements_low_information_prophage_proteins"


class NoAliasDumper(yaml.SafeDumper):
    def ignore_aliases(self, data):
        return True


TERM = {
    "GO:0005198": {"id": "GO:0005198", "label": "structural molecule activity"},
    "GO:0019068": {"id": "GO:0019068", "label": "virion assembly"},
}

GENES = [
    "PP_1538",
    "PP_1546",
    "PP_1557",
    "PP_1571",
    "PP_2285",
    "PP_3049",
    "PP_3860",
    "PP_3861",
    "PP_3870",
    "PP_3871",
    "PP_3873",
    "PP_3888",
    "PP_3906",
    "PP_5637",
]

STRUCTURAL = {"PP_1571", "PP_3860", "PP_3871"}
PROCESS_ONLY = {"PP_2285"}
UNRESOLVED = set(GENES) - STRUCTURAL - PROCESS_ONLY

DOMAIN_NEEDLES = {
    "PP_1571": ("HK97-gp10_tail", "HK97-gp10_like"),
    "PP_2285": ("Gp14", "T7_gp14"),
    "PP_3860": ("Barrel_Baseplate_J-like", "Baseplate_J-like_C", "Baseplate_J_M", "Phage_Baseplate_Assmbl_Protein"),
    "PP_3861": ("Phage_Mu_Gp46", "GP46"),
    "PP_3870": ("DUF2635",),
    "PP_3871": ("Phage_JBD30_tail_term-like", "Phage_tail_terminator"),
    "PP_3888": ("HSP_DnaJ_Cys-rich_dom_sf",),
}


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


def add_unique(items: list[dict], item: dict | None) -> None:
    if item and item not in items:
        items.append(item)


def file_id(gene: str, suffix: str) -> str:
    return f"file:PSEPK/{gene}/{gene}-{suffix}"


def gene_file(gene: str, suffix: str) -> Path:
    return GENE_ROOT / gene / f"{gene}-{suffix}"


def product_line(gene: str) -> str | None:
    path = gene_file(gene, "uniprot.txt")
    return optional_first_line(path, "DE   RecName") or optional_first_line(path, "DE   SubName")


def product_text(gene: str) -> str:
    return (product_line(gene) or "DE   RecName: Full=prophage protein").removeprefix("DE   ").rstrip(".")


def goa_line(gene: str, term_id: str) -> str | None:
    return optional_first_line(gene_file(gene, "goa.tsv"), term_id)


def evidence_for(gene: str, term_id: str | None = None) -> list[dict[str, str]]:
    path = gene_file(gene, "uniprot.txt")
    items: list[dict[str, str]] = []
    if term_id:
        add_unique(items, support(file_id(gene, "goa.tsv"), goa_line(gene, term_id)))
    add_unique(items, support(file_id(gene, "uniprot.txt"), product_line(gene)))
    if term_id:
        add_unique(items, support(file_id(gene, "uniprot.txt"), optional_first_line(path, f"DR   GO; {term_id};")))
    for needle in DOMAIN_NEEDLES.get(gene, ()):
        add_unique(items, support(file_id(gene, "uniprot.txt"), optional_first_line(path, needle)))
    for marker in ("DR   PANTHER;", "DR   Pfam;", "KW   Signal"):
        add_unique(items, support(file_id(gene, "uniprot.txt"), optional_first_line(path, marker)))
    asta = gene_file(gene, "deep-research-asta.md")
    add_unique(items, support(file_id(gene, "deep-research-asta.md"), optional_first_line(asta, "uniprot_accession:")))
    add_unique(items, support(file_id(gene, "deep-research-asta.md"), optional_first_line(asta, "protein_description:")))
    add_unique(items, support(file_id(gene, "deep-research-asta.md"), optional_first_line(asta, "protein_domains:")))
    return items


def description_for(gene: str) -> str:
    product = product_text(gene)
    if gene == "PP_1571":
        return (
            f"{gene} encodes an HK97 gp10-family phage protein ({product}) with HK97 gp10 tail-domain support, consistent "
            "with a prophage structural tail/head-associated component."
        )
    if gene == "PP_3860":
        return (
            f"{gene} encodes a FluMu gp47/Mu gp47-family prophage protein ({product}) with baseplate J-like and phage "
            "baseplate assembly domain support, consistent with a structural baseplate-associated role."
        )
    if gene == "PP_3871":
        return (
            f"{gene} encodes a phage tail-terminator-like protein ({product}) with JBD30 tail-terminator domain support, "
            "consistent with prophage tail structural context."
        )
    if gene == "PP_2285":
        return (
            f"{gene} encodes a phage Gp14-like protein ({product}) with a GOA process annotation for symbiont genome "
            "ejection through the host cell envelope. The current record does not resolve a specific molecular function."
        )
    if gene == "PP_3861":
        return (
            f"{gene} encodes a FluMu gp46-domain prophage protein ({product}). The record supports prophage structural or "
            "assembly context but does not resolve a specific molecular function."
        )
    if gene == "PP_3870":
        return (
            f"{gene} encodes a FluMu gp38/DUF2635 prophage protein ({product}). The domain evidence supports prophage "
            "context but not a resolved molecular function."
        )
    if gene == "PP_3888":
        return (
            f"{gene} encodes a prophage PssSM-03 protein ({product}) with DnaJ cysteine-rich-domain superfamily evidence. "
            "The current record does not resolve a phage-specific molecular function."
        )
    return (
        f"{gene} encodes a low-information prophage or phage-related protein ({product}) without GOA or domain support "
        "sufficient to resolve a molecular function."
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
        finding = {"statement": "Local first-pass source used for low-information prophage review."}
        if quote:
            finding["supporting_text"] = quote
        refs.append({"id": ref_id, "title": title, "findings": [finding]})


def review_for(gene: str, term_id: str) -> dict:
    if gene in STRUCTURAL and term_id == "GO:0005198":
        return {
            "summary": "Structural molecule activity is added for the domain-supported prophage structural component.",
            "action": "NEW",
            "reason": "The product and phage structural domains support a prophage virion structural role, while no enzymatic function is asserted.",
            "supported_by": evidence_for(gene, None),
        }
    if gene in STRUCTURAL and term_id == "GO:0019068":
        return {
            "summary": "Virion assembly is added as structural process context.",
            "action": "NEW",
            "reason": "The phage tail, baseplate, or tail-terminator domain context supports assembly into a prophage structural particle.",
            "supported_by": evidence_for(gene, None),
        }
    if gene == "PP_2285" and term_id == "GO:0039678":
        return {
            "summary": "The genome-ejection process row is retained as non-core process context.",
            "action": "KEEP_AS_NON_CORE",
            "reason": "The Gp14/T7_gp14 domain and signal peptide support phage genome-ejection context, but the record does not resolve a GO molecular function for a core function entry.",
            "supported_by": evidence_for(gene, term_id),
        }
    raise ValueError(f"No review rule for {gene} {term_id}")


def ensure_new_rows(data: dict, gene: str) -> None:
    if gene not in STRUCTURAL:
        return
    rows = data.setdefault("existing_annotations", [])
    if not any(row.get("term", {}).get("id") == "GO:0005198" for row in rows):
        rows.append(
            {
                "term": TERM["GO:0005198"],
                "evidence_type": "IEA",
                "original_reference_id": file_id(gene, "uniprot.txt"),
                "qualifier": "enables",
                "review": review_for(gene, "GO:0005198"),
            }
        )
    if not any(row.get("term", {}).get("id") == "GO:0019068" for row in rows):
        rows.append(
            {
                "term": TERM["GO:0019068"],
                "evidence_type": "IEA",
                "original_reference_id": file_id(gene, "uniprot.txt"),
                "qualifier": "involved_in",
                "review": review_for(gene, "GO:0019068"),
            }
        )


def core_functions_for(gene: str) -> list[dict]:
    if gene not in STRUCTURAL:
        return []
    return [
        {
            "description": "Prophage structural molecule activity in virion assembly.",
            "supported_by": evidence_for(gene, None),
            "molecular_function": TERM["GO:0005198"],
            "directly_involved_in": [TERM["GO:0019068"]],
        }
    ]


def questions_for(gene: str) -> list[dict[str, str]]:
    if gene in STRUCTURAL:
        text = f"Is {gene} part of an intact prophage structural locus, and is the predicted structural role experimentally detectable?"
    elif gene == "PP_2285":
        text = f"What molecular function, if any, mediates the predicted PP_2285 role in phage genome ejection?"
    else:
        text = f"Does {gene} encode a functional prophage protein or a low-information remnant?"
    return [{"question": text}]


def experiments_for(gene: str) -> list[dict[str, str]]:
    return [
        {
            "experiment_type": "prophage locus inspection",
            "description": f"Inspect the genomic neighborhood of {gene} for synteny with structural, packaging, lysis, and regulatory prophage modules.",
            "hypothesis": f"{gene} belongs to a coherent local prophage locus rather than an isolated annotation remnant.",
        },
        {
            "experiment_type": "comparative sequence analysis",
            "description": f"Compare {gene} against curated phage proteins to test domain completeness and family specificity.",
            "hypothesis": f"{gene} retains enough conserved sequence features to support its assigned prophage context.",
        },
    ]


def curate_gene(gene: str) -> None:
    path = GENE_ROOT / gene / f"{gene}-ai-review.yaml"
    data = yaml.safe_load(read_text(path))
    data["status"] = "DRAFT"
    data["description"] = description_for(gene)
    ensure_references(data, gene)
    for row in data.get("existing_annotations") or []:
        term_id = row.get("term", {}).get("id")
        row["review"] = review_for(gene, term_id)
    ensure_new_rows(data, gene)
    data["core_functions"] = core_functions_for(gene)
    data["proposed_new_terms"] = []
    data["suggested_questions"] = questions_for(gene)
    data["suggested_experiments"] = experiments_for(gene)
    path.write_text(yaml.dump(data, Dumper=NoAliasDumper, sort_keys=False, width=120), encoding="utf-8")


def descriptor(term_id: str) -> dict:
    return {"preferred_term": TERM[term_id]["label"], "term": TERM[term_id]}


def annoton(gene: str) -> dict:
    role = "low-information-bucket prophage structural molecule activity in virion assembly"
    return {
        "id": f"{gene.lower()}_low_information_structural",
        "label": f"{gene}: {role}",
        "participant": {"selector_type": "GENE", "gene": {"preferred_term": gene}},
        "role_description": role,
        "function": descriptor("GO:0005198"),
        "processes": [descriptor("GO:0019068")],
    }


def extend_structural_module() -> None:
    data = yaml.safe_load(read_text(MODULE_PATH))
    source_id = f"file:projects/P_PUTIDA/batches/{BATCH_ID}.tsv"
    if not any(e.get("source_id") == source_id for e in data.get("evidence", [])):
        data.setdefault("evidence", []).append(
            {
                "source_id": source_id,
                "title": "PSEPK mobile-genetic-elements low-information prophage split table",
                "statement": "The split table routes 14 low-information prophage genes; three have enough phage structural domain evidence for structural molecule activity, one has process-only genome-ejection context, and the rest remain unresolved.",
            }
        )
    note = (
        " The low_information_prophage_proteins sub-batch contributes three additional domain-supported structural "
        "annotons (PP_1571, PP_3860, PP_3871). PP_2285 keeps process-only genome-ejection context, and the remaining "
        "name-only or ambiguous records remain no-core unresolved in gene reviews."
    )
    if note.strip() not in data.get("notes", ""):
        data["notes"] = (data.get("notes", "") + note).strip()
    parts = data["module"].setdefault("parts", [])
    parts = [
        part for part in parts if part.get("node", {}).get("id") != "low_information_phage_structural_exceptions"
    ]
    parts.append(
        {
            "order": 2,
            "role": "Domain-supported structural exceptions from low-information prophage bucket",
            "node": {
                "id": "low_information_phage_structural_exceptions",
                "label": "Low-information-bucket structural exceptions",
                "module_type": "BIOLOGICAL_PROCESS",
                "annotons": [annoton(gene) for gene in sorted(STRUCTURAL)],
            },
        }
    )
    data["module"]["parts"] = parts
    MODULE_PATH.write_text(yaml.dump(data, Dumper=NoAliasDumper, sort_keys=False, width=120), encoding="utf-8")


def main() -> None:
    for gene in GENES:
        curate_gene(gene)
    extend_structural_module()
    print(f"Curated {len(GENES)} gene reviews")
    print(f"Extended {MODULE_PATH}")


if __name__ == "__main__":
    main()
