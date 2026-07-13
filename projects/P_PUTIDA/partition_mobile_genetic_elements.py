#!/usr/bin/env python3
"""Partition the PSEPK mobile-genetic-elements functional bucket."""

from __future__ import annotations

import csv
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
PARTITION_TSV = ROOT / "projects/P_PUTIDA/data/psepk_pathway_partition.tsv"
BATCH_DIR = ROOT / "projects/P_PUTIDA/batches"
OUT_TSV = BATCH_DIR / "module_mobile_genetic_elements_partition.tsv"
OUT_MD = BATCH_DIR / "module_mobile_genetic_elements_partition.md"
GENE_ROOT = ROOT / "genes/PSEPK"
SOURCE_BUCKET = "module:mobile_genetic_elements"


BUCKETS = {
    "transposase_goa_supported": {
        "label": "GOA-supported transposases and insertion-sequence integration proteins",
        "module": "mobile_genetic_elements_boundary",
        "action": "REUSE_OR_EXTEND_EXISTING",
        "status": "NEXT_SUBMODULE",
        "note": (
            "Transposase or transposase-subunit records with fetched GOA support for "
            "transposase activity, DNA transposition, DNA integration, or nucleic-acid "
            "binding. This is the highest-confidence first curation target."
        ),
    },
    "transposase_domain_or_fragment": {
        "label": "Domain-only or fragmentary transposase candidates",
        "module": "mobile_genetic_elements_boundary",
        "action": "DEFER_LOW_EVIDENCE",
        "status": "QUEUED",
        "note": (
            "Transposase-name records with no fetched GOA rows or only very broad "
            "binding rows. Treat short fragments and domain-only entries cautiously."
        ),
    },
    "integrase_mobile_element_context": {
        "label": "Integrase mobile-element context",
        "module": "mobile_genetic_elements_boundary",
        "action": "REUSE_OR_EXTEND_EXISTING",
        "status": "QUEUED",
        "note": (
            "Integrase-name records in the primary mobile-element bucket. Curate as "
            "mobile-element integration/recombination unless direct chromosomal repair "
            "evidence exists."
        ),
    },
    "prophage_structural_packaging": {
        "label": "Prophage structural, head-tail, portal, terminase, and packaging proteins",
        "module": "prophage_structural_packaging_boundary",
        "action": "NEW_SUBMODULE",
        "status": "QUEUED",
        "note": (
            "Prophage structural and packaging proteins: head/tail/capsid/portal/"
            "terminase/sheath/tube/fiber entries. Likely a structural boundary module "
            "rather than metabolic pathway curation."
        ),
    },
    "phage_dna_replication_processing": {
        "label": "Phage DNA replication and processing proteins",
        "module": "phage_dna_replication_processing_boundary",
        "action": "NEW_SUBMODULE",
        "status": "QUEUED",
        "note": (
            "Phage replication proteins, phage SSB, phage endodeoxyribonuclease, and "
            "DNA-circulation context."
        ),
    },
    "phage_lysis_host_interaction": {
        "label": "Phage lysis, holin, and host-interaction proteins",
        "module": "phage_lysis_host_interaction_boundary",
        "action": "NEW_SUBMODULE",
        "status": "QUEUED",
        "note": "Holin and host-interaction/infection proteins with sparse annotation.",
    },
    "phage_regulatory_toxin_antitoxin": {
        "label": "Phage regulators, repressors, and toxin-antitoxin context",
        "module": "phage_regulation_toxin_antitoxin_boundary",
        "action": "NEW_SUBMODULE",
        "status": "QUEUED",
        "note": (
            "XRE/Cro-like repressors and plasmid-stabilization/toxin-antitoxin "
            "context. Keep phage regulatory DNA binding separate from bacterial "
            "metabolic regulation."
        ),
    },
    "low_information_prophage_proteins": {
        "label": "Low-information prophage and phage proteins",
        "module": "mobile_genetic_elements_low_information_boundary",
        "action": "DEFER_LOW_EVIDENCE",
        "status": "QUEUED",
        "note": (
            "Generic prophage/phage proteins with limited or absent GO/domain signal. "
            "Do not promote core functions from names alone."
        ),
    },
}

BUCKET_ORDER = list(BUCKETS)

FIELDS = [
    "gene",
    "ordered_locus",
    "uniprot_accession",
    "protein_name",
    "ec_numbers",
    "go_ids",
    "interpro_ids",
    "pfam_ids",
    "panther_ids",
    "keywords",
    "partition_bucket",
    "partition_label",
    "proposed_module",
    "recommended_action",
    "bucket_status",
    "notes",
    "review_status",
    "curation_status",
    "asta_research_status",
]


def norm(value: str) -> str:
    return (value or "").casefold()


def has_any(text: str, terms: tuple[str, ...]) -> bool:
    lowered = norm(text)
    return any(term in lowered for term in terms)


def ids(row: dict[str, str], field: str) -> set[str]:
    return {part.strip() for part in row.get(field, "").split(";") if part.strip()}


def review_status(gene: str) -> str:
    return "PRESENT" if (GENE_ROOT / gene / f"{gene}-ai-review.yaml").exists() else "MISSING"


def curation_status(gene: str) -> str:
    path = GENE_ROOT / gene / f"{gene}-ai-review.yaml"
    if not path.exists():
        return "MISSING"
    text = path.read_text(encoding="utf-8")
    if "action: PENDING" in text or "TODO: Review" in text or "TODO: Add description" in text:
        return "PENDING"
    return "CURATED"


def asta_research_status(gene: str) -> str:
    return "PRESENT" if (GENE_ROOT / gene / f"{gene}-deep-research-asta.md").exists() else "MISSING"


def assign_bucket(row: dict[str, str]) -> str:
    gene = row["suggested_review_name"]
    product = row["protein_name"]
    go = ids(row, "go_ids")

    if gene in {"PP_1963", "PP_2825", "PP_3677"} or has_any(product, ("integrase",)):
        return "integrase_mobile_element_context"

    if has_any(product, ("transposase", "transposon", "tniq")) or gene == "tnpB":
        if go & {"GO:0004803", "GO:0006313", "GO:0015074"}:
            return "transposase_goa_supported"
        return "transposase_domain_or_fragment"

    if has_any(
        product,
        (
            "terminase",
            "portal",
            "head",
            "tail",
            "capsid",
            "connector",
            "sheath",
            "tube",
            "fiber",
            "assembly",
            "internal core",
            "tape",
        ),
    ):
        return "prophage_structural_packaging"

    if has_any(product, ("replication", "single-stranded dna-binding", "endodeoxyribonuclease", "dna circulation")):
        return "phage_dna_replication_processing"

    if has_any(product, ("holin", "infection protein")):
        return "phage_lysis_host_interaction"

    if has_any(product, ("repressor", "transcriptional xre", "plasmid stabilization")):
        return "phage_regulatory_toxin_antitoxin"

    return "low_information_prophage_proteins"


def make_row(source: dict[str, str]) -> dict[str, str]:
    gene = source["suggested_review_name"]
    bucket_id = assign_bucket(source)
    info = BUCKETS[bucket_id]
    return {
        "gene": gene,
        "ordered_locus": source["ordered_locus"],
        "uniprot_accession": source["uniprot_accession"],
        "protein_name": source["protein_name"],
        "ec_numbers": source["ec_numbers"],
        "go_ids": source["go_ids"],
        "interpro_ids": source["interpro_ids"],
        "pfam_ids": source["pfam_ids"],
        "panther_ids": source["panther_ids"],
        "keywords": source["keywords"],
        "partition_bucket": bucket_id,
        "partition_label": info["label"],
        "proposed_module": info["module"],
        "recommended_action": info["action"],
        "bucket_status": info["status"],
        "notes": info["note"],
        "review_status": review_status(gene),
        "curation_status": curation_status(gene),
        "asta_research_status": asta_research_status(gene),
    }


def write_rows(path: Path, rows: list[dict[str, str]]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS, delimiter="\t")
        writer.writeheader()
        writer.writerows(rows)


def write_batch_md(path: Path, title: str, rows: list[dict[str, str]], note: str) -> None:
    lines = [
        "---",
        f'title: "{title}"',
        "maturity: DRAFT",
        "tags: [BIOLOGY_DOMAIN, PIPELINE]",
        "species: [PSEPK]",
        "autolink_gene_symbols: false",
        "---",
        "",
        f"# {title}",
        "",
        note,
        "",
        "| Done | Gene | Locus | UniProt | Review | Curation | Asta | Protein |",
        "|---|---|---|---|---|---|---|---|",
    ]
    for row in rows:
        done = "[x]" if row["curation_status"] == "CURATED" and row["asta_research_status"] == "PRESENT" else "[ ]"
        lines.append(
            f"| {done} | `{row['gene']}` | {row['ordered_locus']} | {row['uniprot_accession']} | "
            f"{row['review_status']} | {row['curation_status']} | {row['asta_research_status']} | {row['protein_name']} |"
        )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def derived_bucket_status(rows: list[dict[str, str]], default_status: str) -> str:
    if rows and all(
        row["curation_status"] == "CURATED" and row["asta_research_status"] == "PRESENT"
        for row in rows
    ):
        return "COMPLETE"
    if any(
        row["review_status"] == "PRESENT" or row["asta_research_status"] == "PRESENT"
        for row in rows
    ):
        return "IN_PROGRESS"
    return default_status


def main() -> None:
    rows = [
        make_row(row)
        for row in csv.DictReader(PARTITION_TSV.open(encoding="utf-8"), delimiter="\t")
        if row["primary_bucket_id"] == SOURCE_BUCKET
    ]
    if not rows:
        raise SystemExit(f"No rows found for {SOURCE_BUCKET}")

    by_bucket: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        by_bucket[row["partition_bucket"]].append(row)

    for bucket_id, bucket_rows in by_bucket.items():
        status = derived_bucket_status(bucket_rows, BUCKETS[bucket_id]["status"])
        for row in bucket_rows:
            row["bucket_status"] = status

    write_rows(OUT_TSV, rows)

    lines = [
        "---",
        'title: "PSEPK mobile genetic elements functional-bucket partition"',
        "maturity: DRAFT",
        "tags: [BIOLOGY_DOMAIN, PIPELINE]",
        "species: [PSEPK]",
        "autolink_gene_symbols: false",
        "---",
        "",
        "# PSEPK mobile genetic elements functional-bucket partition",
        "",
        "The `module:mobile_genetic_elements` bucket is a broad UniProt-name/keyword bucket. It mixes insertion-sequence",
        "transposases, integrases, prophage structural proteins, phage DNA replication/processing proteins, phage lysis",
        "or host-interaction proteins, and low-information prophage proteins. It should not be curated as one pathway.",
        "",
        "## Outputs",
        "",
        "- Partition table: `projects/P_PUTIDA/batches/module_mobile_genetic_elements_partition.tsv`",
        "",
        "## Partition Summary",
        "",
        "| Bucket | Genes | Proposed module | Action | Status | Example genes |",
        "|---|---:|---|---|---|---|",
    ]
    for bucket_id in BUCKET_ORDER:
        bucket_rows = by_bucket[bucket_id]
        info = BUCKETS[bucket_id]
        examples = ", ".join(f"`{row['gene']}`" for row in bucket_rows[:8])
        status = bucket_rows[0]["bucket_status"] if bucket_rows else info["status"]
        lines.append(
            f"| `{bucket_id}` | {len(bucket_rows)} | `{info['module']}` | {info['action']} | {status} | {examples} |"
        )

    lines.extend(
        [
            "",
            "## Current Coverage",
            "",
            f"- Review status: {dict(Counter(row['review_status'] for row in rows))}",
            f"- Curation status: {dict(Counter(row['curation_status'] for row in rows))}",
            f"- Asta research status: {dict(Counter(row['asta_research_status'] for row in rows))}",
            "",
            "## Working Decisions",
            "",
            "- Start with the `transposase_goa_supported` split because it has direct GOA evidence for transposition or integration.",
            "- Keep domain-only/fragmentary transposases separate until each can be reviewed without overpromoting fragments.",
            "- Keep prophage structural and low-information proteins separate from enzymatic transposition/recombination calls.",
        ]
    )
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")

    for bucket_id in BUCKET_ORDER:
        info = BUCKETS[bucket_id]
        bucket_rows = by_bucket[bucket_id]
        stem = f"module_mobile_genetic_elements_{bucket_id}"
        write_rows(BATCH_DIR / f"{stem}.tsv", bucket_rows)
        write_batch_md(BATCH_DIR / f"{stem}.md", f"PSEPK mobile genetic elements: {info['label']}", bucket_rows, info["note"])


if __name__ == "__main__":
    main()
