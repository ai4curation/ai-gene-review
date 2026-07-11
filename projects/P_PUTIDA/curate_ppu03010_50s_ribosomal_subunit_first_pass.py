#!/usr/bin/env python3
"""First-pass curation for the ppu03010 bacterial 50S ribosomal subunit batch."""

from __future__ import annotations

import csv
from pathlib import Path

import yaml


SPECIES = "PSEPK"
ROOT = Path(__file__).resolve().parents[2]
GENE_ROOT = ROOT / "genes" / SPECIES
BATCH = ROOT / "projects/P_PUTIDA/batches/ppu03010_bacterial_ribosome_partition.tsv"
BUCKET = "bacterial_50s_ribosomal_subunit"


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


def product_phrase(product: str) -> str:
    if product.startswith(("Large ", "Small ")):
        return product[:1].lower() + product[1:]
    return product


def description_for(gene: str, row: dict[str, str], terms: dict[str, str]) -> str:
    product = row["protein_name"].rstrip(".")
    phrase = product_phrase(product)
    locus = row["ordered_locus"]
    extra = ""
    if "GO:0008097" in terms:
        extra = " It specifically contacts 5S rRNA within the large subunit."
    elif "GO:0070180" in terms or "GO:0019843" in terms:
        extra = " It contacts large-subunit rRNA as part of 50S subunit architecture and assembly."
    elif "GO:0000049" in terms:
        extra = " It contributes to tRNA-contact interactions at the large subunit."
    elif "GO:0017148" in terms:
        extra = " It also has an autoregulatory translation-control annotation that is treated as secondary to its ribosomal structural role."
    return (
        f"{gene} ({locus}) encodes {phrase}, a conserved protein component of the bacterial "
        f"50S large ribosomal subunit in Pseudomonas putida KT2440. It functions as a structural "
        f"constituent of the ribosome and supports protein translation as part of the large "
        f"subunit.{extra}"
    )


def action_for(term_id: str, terms: dict[str, str]) -> tuple[str, str, str, list[dict[str, str]] | None]:
    if term_id == "GO:0003735":
        return (
            "ACCEPT",
            "structural constituent of ribosome is the defining molecular function of this 50S ribosomal protein",
            "This is the core ribosomal-protein molecular function for a conserved 50S large-subunit component.",
            None,
        )
    if term_id in {"GO:0006412", "GO:0002181"}:
        return (
            "ACCEPT",
            "translation is the core biological process carried out by the assembled ribosome",
            "The protein acts as a component of the large ribosomal subunit during translation.",
            None,
        )
    if term_id in {"GO:0005840", "GO:0015934", "GO:0022625"}:
        return (
            "ACCEPT",
            "ribosome/large-subunit membership is the correct cellular-component context",
            "The protein is a conserved bacterial 50S ribosomal protein and this cellular-component annotation is appropriate.",
            None,
        )
    if term_id == "GO:0005737":
        return (
            "KEEP_AS_NON_CORE",
            "cytoplasm localization is correct for a bacterial ribosomal protein but is less informative than ribosome or large-subunit membership",
            "Retain as non-core location context; the more informative location is the ribosome/large ribosomal subunit.",
            None,
        )
    if term_id == "GO:0003723":
        if {"GO:0019843", "GO:0070180", "GO:0008097", "GO:0003729", "GO:0000049"} & set(terms):
            return (
                "MARK_AS_OVER_ANNOTATED",
                "RNA binding is a generic parent term for a ribosomal protein with a more specific rRNA, 5S rRNA, mRNA, or tRNA binding annotation",
                "This broad RNA-binding term is less informative than the specific binding term already present.",
                None,
            )
        return (
            "KEEP_AS_NON_CORE",
            "RNA binding is compatible with the ribosomal-protein role but less specific than structural constituent of ribosome",
            "Retain as non-core ribosomal RNA/contact context in this first pass.",
            None,
        )
    if term_id == "GO:0019843" and {"GO:0070180", "GO:0008097"} & set(terms):
        return (
            "MARK_AS_OVER_ANNOTATED",
            "rRNA binding is a parent or broader sibling of the co-annotated large-subunit or 5S rRNA binding term",
            "The more specific rRNA-binding term captures the same role better.",
            None,
        )
    if term_id in {"GO:0019843", "GO:0070180", "GO:0008097", "GO:0000049"}:
        return (
            "ACCEPT",
            "specific rRNA/5S-rRNA/tRNA binding is a meaningful molecular role for this 50S ribosomal protein",
            "The specific nucleic-acid-binding annotation is consistent with the ribosomal-protein role.",
            None,
        )
    if term_id == "GO:0003729":
        return (
            "KEEP_AS_NON_CORE",
            "mRNA binding is plausible autoregulatory or ribosomal context but is secondary to the large-subunit structural role in this first pass",
            "Retain as non-core specific binding context pending deeper gene-specific review.",
            None,
        )
    if term_id == "GO:0017148":
        return (
            "KEEP_AS_NON_CORE",
            "negative regulation of translation likely reflects ribosomal-protein autoregulation and is secondary to the structural 50S role",
            "Retain as non-core regulatory context rather than the defining function of the gene product.",
            None,
        )
    if term_id == "GO:0000027":
        return (
            "ACCEPT",
            "ribosomal large-subunit assembly is a supported process-level role for this 50S ribosomal protein",
            "The assembly annotation is compatible with the protein's large-subunit structural role.",
            None,
        )
    if term_id == "GO:1902626":
        return (
            "MODIFY",
            "assembly of large subunit precursor of preribosome is more contorted than needed for this bacterial 50S protein; ribosomal large subunit assembly is the clearer replacement",
            "The underlying assembly role is plausible, but the recommended first-pass term is the clearer bacterial large-subunit assembly term.",
            [term("GO:0000027", "ribosomal large subunit assembly")],
        )
    if term_id == "GO:0008270":
        return (
            "KEEP_AS_NON_CORE",
            "zinc ion binding is a plausible structural cofactor annotation for this ribosomal protein but is not the defining ribosomal role",
            "Retain as non-core structural cofactor context.",
            None,
        )
    if term_id == "GO:0043022":
        return (
            "KEEP_AS_NON_CORE",
            "ribosome binding is compatible with large-subunit assembly but less informative than ribosome/large-subunit membership and structural constituent activity",
            "Retain as non-core assembly or association context.",
            None,
        )
    if term_id == "GO:0016740":
        return (
            "MARK_AS_OVER_ANNOTATED",
            "generic transferase activity is not an appropriate standalone molecular function for ribosomal protein L2; peptide-bond formation is a ribosomal/RNA-centered activity",
            "Treat this as an over-propagated generic catalytic annotation and retain the structural ribosomal role instead.",
            None,
        )
    return (
        "KEEP_AS_NON_CORE",
        "annotation is compatible with the 50S ribosomal-protein context but is not the defining first-pass role",
        "Retain conservatively as a non-core annotation pending deeper gene-specific review.",
        None,
    )


def review_for(gene: str, term_id: str, label: str, terms: dict[str, str]) -> dict:
    action, reason, summary, replacements = action_for(term_id, terms)
    review = {
        "summary": summary,
        "action": action,
        "reason": reason,
        "supported_by": uniq_support([goa_line(gene, term_id), uniprot_line(gene), asta_line(gene)]),
    }
    if replacements:
        review["proposed_replacement_terms"] = replacements
    return review


def best_location(terms: dict[str, str]) -> dict[str, str] | None:
    # Large-subunit component terms are valid trusted GOA existing annotations,
    # but the stricter review schema does not allow them in authored core
    # locations. Use the parent ribosome location only when present.
    if "GO:0005840" in terms:
        return term("GO:0005840", terms["GO:0005840"])
    return None


def core_functions(gene: str, row: dict[str, str], terms: dict[str, str]) -> list[dict]:
    product = row["protein_name"].rstrip(".")
    phrase = product_phrase(product)
    process_id = "GO:0002181" if "GO:0002181" in terms else "GO:0006412"
    processes = [term(process_id, terms[process_id])]
    if "GO:0000027" in terms:
        processes.append(term("GO:0000027", terms["GO:0000027"]))
    locations = []
    location = best_location(terms)
    if location:
        locations.append(location)

    base_support = [goa_line(gene, "GO:0003735"), goa_line(gene, process_id), uniprot_line(gene), asta_line(gene)]
    if location:
        base_support.append(goa_line(gene, location["id"]))
    functions: list[dict] = [
        {
            "description": (
                f"Serves as {phrase}, a structural protein component of the bacterial 50S "
                "large ribosomal subunit during translation."
            ),
            "molecular_function": term("GO:0003735", terms["GO:0003735"]),
            "directly_involved_in": processes,
            "locations": locations,
            "supported_by": uniq_support(base_support),
        }
    ]

    binding_terms = []
    if "GO:0008097" in terms:
        binding_terms.append("GO:0008097")
    if "GO:0070180" in terms:
        binding_terms.append("GO:0070180")
    elif "GO:0019843" in terms and "GO:0008097" not in terms:
        binding_terms.append("GO:0019843")
    if "GO:0000049" in terms:
        binding_terms.append("GO:0000049")

    for term_id in binding_terms:
        label = terms[term_id]
        functions.append(
            {
                "description": (
                    f"Binds {label.replace(' binding', '')} in the context of the assembled "
                    "bacterial large ribosomal subunit."
                ),
                "molecular_function": term(term_id, label),
                "directly_involved_in": [term(process_id, terms[process_id])],
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
