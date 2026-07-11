#!/usr/bin/env python3
"""Partition the PSEPK stress/detoxification functional bucket."""

from __future__ import annotations

import csv
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
PARTITION_TSV = ROOT / "projects/P_PUTIDA/data/psepk_pathway_partition.tsv"
BATCH_DIR = ROOT / "projects/P_PUTIDA/batches"
OUT_TSV = BATCH_DIR / "module_stress_detoxification_partition.tsv"
OUT_MD = BATCH_DIR / "module_stress_detoxification_partition.md"
GENE_ROOT = ROOT / "genes/PSEPK"
SOURCE_BUCKET = "module:stress_detoxification"


BUCKETS = {
    "peroxide_peroxiredoxin_detoxification": {
        "label": "Peroxide and peroxiredoxin detoxification",
        "module": "oxidative_stress_peroxide_detoxification_boundary",
        "action": "COMPLETED_SUBMODULE",
        "status": "CURATED",
        "note": (
            "OsmC/Ohr/AhpC/Tpx/TsaA/Bcp-family peroxidases plus cytochrome-c, DyP, "
            "and non-heme chloroperoxidase candidates. Curate as bacterial peroxide "
            "and hydroperoxide detoxification, not peroxisome organelle biology."
        ),
        "genes": [
            "osmC",
            "PP_0235",
            "tsaA",
            "PP_1235",
            "ohr",
            "ahpC",
            "PP_2943",
            "PP_3248",
            "tpx",
            "cpo",
        ],
    },
    "glutathione_thiol_detoxification": {
        "label": "Glutathione, thiol, and conjugation detoxification",
        "module": "glutathione_metabolism_boundary",
        "action": "COMPLETED_REUSE_EXISTING",
        "status": "CURATED",
        "note": (
            "GST-family proteins, glutathione-dependent thiol reductase, formaldehyde "
            "dehydrogenase, and methionine-derivative detoxification candidates. "
            "Reuse the glutathione boundary where the function is genuinely "
            "glutathione-linked; keep generic GST-family spillovers conservative."
        ),
        "genes": ["PP_0335", "yffB", "PP_1939", "PP_2023", "PP_3742", "PP_4104", "mnaT"],
    },
    "arsenic_copper_metal_resistance": {
        "label": "Arsenic and copper resistance",
        "module": "metal_resistance_detoxification_boundary",
        "action": "COMPLETED_SUBMODULE",
        "status": "CURATED",
        "note": (
            "Two ArsH/arsenate-reductase pairs and two CopA/CopB copper-resistance "
            "pairs. Curate as metal/arsenical/copper resistance rather than broad "
            "oxidative stress."
        ),
        "genes": ["PP_1927", "PP_1928", "arsH", "PP_2716", "copB-I", "copA-I", "copB-II", "copA-II"],
    },
    "universal_stress_proteins": {
        "label": "Universal stress protein candidates",
        "module": "universal_stress_protein_boundary",
        "action": "COMPLETED_SUBMODULE",
        "status": "CURATED",
        "note": (
            "USP-domain proteins with weak pathway specificity. First-pass curation "
            "should separate ATP-binding USP proteins from low-information stress "
            "protein candidates and avoid assigning specific stress responses without "
            "direct evidence."
        ),
        "genes": [
            "PP_1269",
            "PP_2132",
            "PP_2187",
            "PP_2326",
            "PP_2648",
            "PP_2745",
            "PP_3156",
            "PP_3237",
            "PP_3288",
            "PP_3290",
            "PP_3294",
        ],
    },
    "cold_heat_shock_chaperone_spillovers": {
        "label": "Cold/heat shock and small chaperone spillovers",
        "module": "integrated_stress_response_boundary",
        "action": "COMPLETED_REUSE_EXISTING",
        "status": "CURATED",
        "note": (
            "Cold-shock proteins and Hsp20/small heat-shock proteins. Reuse the "
            "bacterial stress/proteostasis boundary where appropriate, while keeping "
            "cold-shock RNA-binding and Hsp20 chaperone biology distinct."
        ),
        "genes": ["capB", "cspA-I", "ibpA", "PP_3313", "PP_3314"],
    },
    "thij_dj1_pfpi_detoxification_candidates": {
        "label": "ThiJ/DJ-1/PfpI detoxification candidates",
        "module": "stress_detoxification_spillover_boundary",
        "action": "COMPLETED_SUBMODULE",
        "status": "CURATED",
        "note": (
            "ThiJ/PfpI/DJ-1-family candidates with likely stress/damage-response or "
            "protease/glyoxalase-family context. Keep specific catalytic claims tied "
            "to domains and GOA evidence."
        ),
        "genes": ["PP_2491", "PP_2992", "PP_3431"],
    },
    "stress_regulatory_or_misc_spillovers": {
        "label": "Stress regulatory and miscellaneous spillovers",
        "module": "stress_detoxification_spillover_boundary",
        "action": "COMPLETED_SUBMODULE",
        "status": "CURATED",
        "note": (
            "Stress-response kinase, Dps, phenylacetate thioesterase detoxification, "
            "bleomycin resistance, OxyR regulation, and low-information stress-induced "
            "proteins. Curate with gene-specific restraint rather than forcing a single "
            "pathway."
        ),
        "genes": ["srkA", "dps", "PP_3269", "paaY", "PP_3509", "PP_3963", "oxyR", "PP_5593"],
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


def write_rows(path: Path, rows: list[dict[str, str]]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS, delimiter="\t")
        writer.writeheader()
        writer.writerows(rows)


def make_row(source: dict[str, str], bucket_id: str) -> dict[str, str]:
    info = BUCKETS[bucket_id]
    gene = source["suggested_review_name"]
    return {
        "gene": gene,
        "ordered_locus": source["ordered_locus"],
        "uniprot_accession": source["uniprot_accession"],
        "protein_name": source["protein_name"],
        "ec_numbers": source["ec_numbers"],
        "go_ids": source["go_ids"],
        "interpro_ids": source["interpro_ids"],
        "pfam_ids": source["pfam_ids"],
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
        "| Gene | Ordered locus | UniProt | Protein | Review | Asta |",
        "|---|---|---|---|---|---|",
    ]
    for row in rows:
        lines.append(
            f"| `{row['gene']}` | `{row['ordered_locus']}` | `{row['uniprot_accession']}` | "
            f"{row['protein_name']} | {row['curation_status']} | {row['asta_research_status']} |"
        )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    source_rows = [
        row
        for row in csv.DictReader(PARTITION_TSV.open(encoding="utf-8"), delimiter="\t")
        if row["primary_bucket_id"] == SOURCE_BUCKET
    ]
    if not source_rows:
        raise SystemExit(f"No rows found for {SOURCE_BUCKET}")

    row_by_gene = {row["suggested_review_name"]: row for row in source_rows}
    assigned: dict[str, str] = {}
    for bucket_id, info in BUCKETS.items():
        for gene in info["genes"]:
            if gene in assigned:
                raise SystemExit(f"{gene} assigned twice: {assigned[gene]} and {bucket_id}")
            assigned[gene] = bucket_id

    missing = sorted(set(row_by_gene) - set(assigned))
    extra = sorted(set(assigned) - set(row_by_gene))
    if missing or extra:
        raise SystemExit(f"Partition mismatch; missing={missing}; extra={extra}")

    rows = [make_row(row_by_gene[gene], assigned[gene]) for gene in row_by_gene]
    write_rows(OUT_TSV, rows)

    by_bucket: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        by_bucket[row["partition_bucket"]].append(row)

    counts = Counter(row["partition_bucket"] for row in rows)
    examples: dict[str, list[str]] = defaultdict(list)
    for row in rows:
        if len(examples[row["partition_bucket"]]) < 8:
            examples[row["partition_bucket"]].append(row["gene"])

    lines = [
        "---",
        'title: "PSEPK stress/detoxification functional-bucket partition"',
        "maturity: DRAFT",
        "tags: [BIOLOGY_DOMAIN, PIPELINE]",
        "species: [PSEPK]",
        "autolink_gene_symbols: false",
        "---",
        "",
        "# PSEPK stress/detoxification functional-bucket partition",
        "",
        "The `module:stress_detoxification` bucket is a UniProt name/keyword",
        "umbrella. It mixes peroxide detoxification enzymes, GST and thiol",
        "detoxification candidates, metal-resistance proteins, universal stress",
        "proteins, cold/heat-shock proteins, ThiJ/DJ-1/PfpI candidates, and",
        "miscellaneous regulatory or low-information stress spillovers.",
        "",
        "## Outputs",
        "",
        f"- Source table: `{PARTITION_TSV.relative_to(ROOT)}`",
        f"- Full partition table: `{OUT_TSV.relative_to(ROOT)}`",
        "",
        "## Partition Summary",
        "",
        "| Bucket | Genes | Proposed module | Action | Status | Example genes |",
        "|---|---:|---|---|---|---|",
    ]
    for bucket_id in BUCKET_ORDER:
        info = BUCKETS[bucket_id]
        module = info["module"] or "(none)"
        example_text = ", ".join(f"`{gene}`" for gene in examples[bucket_id])
        lines.append(
            f"| `{bucket_id}` | {counts[bucket_id]} | `{module}` | "
            f"{info['action']} | {info['status']} | {example_text} |"
        )

    lines.extend(
        [
            "",
            "## Working Decisions",
            "",
            "- Do not curate the 52-gene functional bucket as one satisfiable module.",
            "- Use the peroxide/peroxiredoxin detoxification split as the first",
            "  follow-up batch because it is biologically compact and complements",
            "  earlier catalase/SOD oxidative-stress curation without implying",
            "  bacterial peroxisome localization.",
            "- Reuse the existing `glutathione_metabolism_boundary` for genes with",
            "  supported glutathione-linked detoxification, but keep generic GST",
            "  candidates conservative until gene-level evidence is reviewed.",
            "- Route cold/heat-shock proteins toward bacterial proteostasis/chaperone",
            "  context rather than eukaryotic integrated-stress-response signaling.",
            "- Treat metal-resistance genes as arsenic/copper detoxification rather",
            "  than as generic oxidative-stress members.",
            "",
        ]
    )
    OUT_MD.write_text("\n".join(lines), encoding="utf-8")

    for bucket_id in BUCKET_ORDER:
        info = BUCKETS[bucket_id]
        bucket_rows = by_bucket[bucket_id]
        stem = f"module_stress_detoxification_{bucket_id}"
        write_rows(BATCH_DIR / f"{stem}.tsv", bucket_rows)
        write_batch_md(
            BATCH_DIR / f"{stem}.md",
            f"PSEPK stress/detoxification: {info['label']}",
            bucket_rows,
            info["note"],
        )

    print(f"Wrote {OUT_TSV.relative_to(ROOT)} with {len(rows)} rows")
    for bucket_id in BUCKET_ORDER:
        print(f"{bucket_id}: {counts[bucket_id]}")


if __name__ == "__main__":
    main()
