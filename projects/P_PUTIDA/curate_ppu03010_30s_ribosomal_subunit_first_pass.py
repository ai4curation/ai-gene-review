#!/usr/bin/env python3
"""First-pass curation for the ppu03010 bacterial 30S ribosomal subunit batch."""

from __future__ import annotations

import csv
from pathlib import Path

import yaml


SPECIES = "PSEPK"
ROOT = Path(__file__).resolve().parents[2]
GENE_ROOT = ROOT / "genes" / SPECIES
BATCH = ROOT / "projects/P_PUTIDA/batches/ppu03010_bacterial_ribosome_partition.tsv"
BUCKET = "bacterial_30s_ribosomal_subunit"


class NoAliasDumper(yaml.SafeDumper):
    def ignore_aliases(self, data):
        return True


GO_REF_TITLES = {
    "GO_REF:0000002": "Gene Ontology annotation through association of InterPro records with GO terms",
    "GO_REF:0000104": (
        "Electronic Gene Ontology annotations created by transferring manual GO annotations "
        "between related proteins based on shared sequence features"
    ),
    "GO_REF:0000117": "Electronic Gene Ontology annotations created by ARBA machine learning models",
    "GO_REF:0000118": "TreeGrafter-generated GO annotations",
    "GO_REF:0000120": "Combined Automated Annotation using Multiple IEA Methods",
}


def term(term_id: str, label: str) -> dict[str, str]:
    return {"id": term_id, "label": label}


def ref_id(gene: str, suffix: str) -> str:
    return f"file:{SPECIES}/{gene}/{gene}-{suffix}"


def support(reference_id: str, text: str) -> dict[str, str]:
    return {"reference_id": reference_id, "supporting_text": text}


def find_line(path: Path, needle: str) -> str:
    for line in path.read_text(encoding="utf-8").splitlines():
        if needle in line:
            return line
    raise ValueError(f"{needle!r} not found in {path}")


def goa_rows(gene: str) -> list[dict[str, str]]:
    path = GENE_ROOT / gene / f"{gene}-goa.tsv"
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def goa_line(gene: str, term_id: str) -> dict[str, str]:
    path = GENE_ROOT / gene / f"{gene}-goa.tsv"
    return support(ref_id(gene, "goa.tsv"), find_line(path, term_id))


def uniprot_line(gene: str, needle: str = "DE   RecName:") -> dict[str, str]:
    path = GENE_ROOT / gene / f"{gene}-uniprot.txt"
    return support(ref_id(gene, "uniprot.txt"), find_line(path, needle))


def asta_line(gene: str, needle: str = "- **Protein Description:**") -> dict[str, str]:
    path = GENE_ROOT / gene / f"{gene}-deep-research-asta.md"
    return support(ref_id(gene, "deep-research-asta.md"), find_line(path, needle))


def uniq_support(items: list[dict[str, str]]) -> list[dict[str, str]]:
    seen: set[tuple[str, str]] = set()
    out: list[dict[str, str]] = []
    for item in items:
        key = (item["reference_id"], item["supporting_text"])
        if key not in seen:
            out.append(item)
            seen.add(key)
    return out


def read_batch() -> dict[str, dict[str, str]]:
    with BATCH.open(newline="", encoding="utf-8") as handle:
        return {
            row["gene"]: row
            for row in csv.DictReader(handle, delimiter="\t")
            if row["partition_bucket"] == BUCKET
        }


def term_map(rows: list[dict[str, str]]) -> dict[str, str]:
    return {row["GO TERM"]: row["GO NAME"] for row in rows}


def normalize_references(existing: list[dict], gene: str) -> list[dict]:
    refs: list[dict] = []
    seen: set[str] = set()
    for entry in existing or []:
        ref = dict(entry)
        ref_id_value = ref.get("id")
        if not ref_id_value or ref_id_value in seen:
            continue
        if ref_id_value in GO_REF_TITLES:
            ref = {"id": ref_id_value, "title": GO_REF_TITLES[ref_id_value], "findings": []}
        refs.append(ref)
        seen.add(ref_id_value)

    for ref in [
        {
            "id": ref_id(gene, "uniprot.txt"),
            "title": f"UniProtKB entry for {gene}",
            "findings": [
                {
                    "statement": (
                        "UniProt protein name, family/domain, and functional annotation lines "
                        "used for first-pass ribosomal-protein curation."
                    )
                }
            ],
        },
        {
            "id": ref_id(gene, "goa.tsv"),
            "title": f"QuickGO GOA annotations for {gene}",
            "findings": [{"statement": "Fetched GOA rows reviewed in this first-pass curation file."}],
        },
        {
            "id": ref_id(gene, "deep-research-asta.md"),
            "title": f"Asta retrieval report for {gene}",
            "findings": [
                {
                    "statement": (
                        "Asta retrieval was used as fast gene-level literature/metadata context; "
                        "no unsupported hypotheses were imported."
                    )
                }
            ],
        },
    ]:
        local_name = ref["id"].split("/")[-1]
        if ref["id"] not in seen and (GENE_ROOT / gene / local_name).exists():
            refs.append(ref)
            seen.add(ref["id"])
    return refs


def description_for(gene: str, row: dict[str, str], terms: dict[str, str]) -> str:
    product = row["protein_name"].rstrip(".")
    locus = row["ordered_locus"]
    extra = ""
    if "GO:0003729" in terms:
        extra = " It also has a specific mRNA-binding role in positioning transcripts on the small subunit."
    elif "GO:0070181" in terms or "GO:0019843" in terms:
        extra = " It contacts small-subunit rRNA as part of 30S subunit architecture and assembly."
    elif "GO:0000049" in terms:
        extra = " It contributes to tRNA-contact or decoding-center interactions during translation."
    return (
        f"{gene} ({locus}) encodes {product}, a conserved protein component of the bacterial "
        f"30S small ribosomal subunit in Pseudomonas putida KT2440. It functions as a structural "
        f"constituent of the ribosome and supports protein translation as part of the small "
        f"subunit.{extra}"
    )


def action_for(term_id: str, terms: dict[str, str]) -> tuple[str, str, str]:
    if term_id == "GO:0003735":
        return (
            "ACCEPT",
            "structural constituent of ribosome is the defining molecular function of this 30S ribosomal protein",
            "This is the core ribosomal-protein molecular function for a conserved 30S small-subunit component.",
        )
    if term_id == "GO:0006412":
        return (
            "ACCEPT",
            "translation is the core biological process carried out by the assembled ribosome",
            "The protein acts as a component of the small ribosomal subunit during translation.",
        )
    if term_id in {"GO:0005840", "GO:0015935", "GO:0022627"}:
        return (
            "ACCEPT",
            "ribosome/small-subunit membership is the correct cellular-component context",
            "The protein is a conserved bacterial 30S ribosomal protein and this cellular-component annotation is appropriate.",
        )
    if term_id in {"GO:0005737", "GO:0005829"}:
        return (
            "KEEP_AS_NON_CORE",
            "cytoplasm/cytosol localization is correct for a bacterial ribosomal protein but is less informative than ribosome or small-subunit membership",
            "Retain as non-core location context; the more informative location is the ribosome/small ribosomal subunit.",
        )
    if term_id == "GO:0003676":
        return (
            "MARK_AS_OVER_ANNOTATED",
            "nucleic acid binding is a generic parent term; the review retains more informative RNA, rRNA, mRNA, or tRNA binding annotations where present",
            "This broad parent term is less informative than the specific nucleic-acid-binding annotations on the same protein.",
        )
    if term_id == "GO:0003723":
        if {"GO:0019843", "GO:0070181", "GO:0003729", "GO:0000049"} & set(terms):
            return (
                "MARK_AS_OVER_ANNOTATED",
                "RNA binding is a generic parent term for a ribosomal protein with a more specific rRNA, mRNA, or tRNA binding annotation",
                "This broad RNA-binding term is less informative than the specific binding term already present.",
            )
        return (
            "KEEP_AS_NON_CORE",
            "RNA binding is compatible with the ribosomal-protein role but less specific than structural constituent of ribosome",
            "Retain as non-core ribosomal RNA/contact context in this first pass.",
        )
    if term_id == "GO:0019843" and "GO:0070181" in terms:
        return (
            "MARK_AS_OVER_ANNOTATED",
            "rRNA binding is a parent of the co-annotated small ribosomal subunit rRNA binding term",
            "The more specific small ribosomal subunit rRNA binding term captures the same role better.",
        )
    if term_id in {"GO:0000049", "GO:0003729", "GO:0019843", "GO:0070181"}:
        return (
            "ACCEPT",
            "specific RNA/rRNA/mRNA/tRNA binding is a meaningful molecular role for this 30S ribosomal protein",
            "The specific nucleic-acid-binding annotation is consistent with the ribosomal-protein role.",
        )
    if term_id in {"GO:0000028", "GO:0042254", "GO:0042274"}:
        return (
            "ACCEPT",
            "ribosomal small-subunit assembly or biogenesis is a supported process-level role for this 30S ribosomal protein",
            "The assembly/biogenesis annotation is compatible with the protein's small-subunit structural role.",
        )
    return (
        "KEEP_AS_NON_CORE",
        "annotation is compatible with the 30S ribosomal-protein context but is not the defining first-pass role",
        "Retain conservatively as a non-core annotation pending deeper gene-specific review.",
    )


def review_for(gene: str, term_id: str, label: str, terms: dict[str, str]) -> dict:
    action, reason, summary = action_for(term_id, terms)
    return {
        "summary": summary,
        "action": action,
        "reason": reason,
        "supported_by": uniq_support([goa_line(gene, term_id), uniprot_line(gene), asta_line(gene)]),
    }


def best_location(terms: dict[str, str]) -> dict[str, str] | None:
    # Small-subunit component terms are valid GOA existing annotations, but the
    # stricter review schema does not allow them in author-written core
    # locations. Use the parent ribosome location only when it is present.
    if "GO:0005840" in terms:
        return term("GO:0005840", terms["GO:0005840"])
    return None


def core_functions(gene: str, row: dict[str, str], terms: dict[str, str]) -> list[dict]:
    product = row["protein_name"].rstrip(".")
    processes = [term("GO:0006412", terms["GO:0006412"])]
    for term_id in ("GO:0000028", "GO:0042254", "GO:0042274"):
        if term_id in terms:
            processes.append(term(term_id, terms[term_id]))
    locations = []
    location = best_location(terms)
    if location:
        locations.append(location)

    base_support = [goa_line(gene, "GO:0003735"), goa_line(gene, "GO:0006412"), uniprot_line(gene), asta_line(gene)]
    if location:
        base_support.append(goa_line(gene, location["id"]))
    functions: list[dict] = [
        {
            "description": (
                f"Serves as {product}, a structural protein component of the bacterial 30S "
                "small ribosomal subunit during translation."
            ),
            "molecular_function": term("GO:0003735", terms["GO:0003735"]),
            "directly_involved_in": processes,
            "locations": locations,
            "supported_by": uniq_support(base_support),
        }
    ]

    binding_terms = []
    if "GO:0003729" in terms:
        binding_terms.append("GO:0003729")
    if "GO:0070181" in terms:
        binding_terms.append("GO:0070181")
    elif "GO:0019843" in terms:
        binding_terms.append("GO:0019843")
    if "GO:0000049" in terms:
        binding_terms.append("GO:0000049")

    for term_id in binding_terms:
        label = terms[term_id]
        functions.append(
            {
                "description": (
                    f"Binds {label.replace(' binding', '')} in the context of the assembled "
                    "bacterial small ribosomal subunit."
                ),
                "molecular_function": term(term_id, label),
                "directly_involved_in": [term("GO:0006412", terms["GO:0006412"])],
                "locations": locations,
                "supported_by": uniq_support([goa_line(gene, term_id), uniprot_line(gene), asta_line(gene)]),
            }
        )
    return functions


def curate_gene(gene: str, row: dict[str, str]) -> None:
    path = GENE_ROOT / gene / f"{gene}-ai-review.yaml"
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    rows = goa_rows(gene)
    terms = term_map(rows)

    data["status"] = "DRAFT"
    data["gene_symbol"] = gene
    data["description"] = description_for(gene, row, terms)
    data["references"] = normalize_references(data.get("references", []), gene)

    for annotation in data.get("existing_annotations", []) or []:
        term_id = annotation["term"]["id"]
        label = annotation["term"]["label"]
        annotation["review"] = review_for(gene, term_id, label, terms)

    data["core_functions"] = core_functions(gene, row, terms)
    data["proposed_new_terms"] = []
    data["suggested_questions"] = []
    data["suggested_experiments"] = []

    path.write_text(
        yaml.dump(data, Dumper=NoAliasDumper, sort_keys=False, allow_unicode=False, width=100),
        encoding="utf-8",
    )
    print(f"Curated {path.relative_to(ROOT)}")


def main() -> None:
    batch = read_batch()
    for gene in batch:
        curate_gene(gene, batch[gene])


if __name__ == "__main__":
    main()
