#!/usr/bin/env python3
"""Partition KEGG ppu03010 ribosome into 30S and 50S curation batches."""

from __future__ import annotations

import csv
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
BATCH_TSV = ROOT / "projects/P_PUTIDA/batches/ppu03010_bacterial_ribosome_boundary.tsv"
OUT_TSV = ROOT / "projects/P_PUTIDA/batches/ppu03010_bacterial_ribosome_partition.tsv"
OUT_MD = ROOT / "projects/P_PUTIDA/batches/ppu03010_bacterial_ribosome_partition.md"


BUCKETS = {
    "bacterial_30s_ribosomal_subunit": {
        "label": "Bacterial 30S ribosomal subunit proteins",
        "module": "bacterial_30s_ribosomal_subunit_boundary",
        "action": "NEW_SUBMODULE",
        "note": "Small-subunit ribosomal proteins; curate as 30S subunit/rRNA-binding/translation contributors.",
        "genes": [
            "rpsU",
            "rpsL",
            "rpsG",
            "rpsJ",
            "rpsS",
            "rpsC",
            "rpsQ",
            "rpsN",
            "rpsH",
            "rpsE",
            "rpsM",
            "rpsK",
            "rpsD",
            "rpsT",
            "rpsI",
            "rpsP",
            "rpsB",
            "rpsA",
            "rpsO",
            "rpsR",
            "rpsF",
        ],
    },
    "bacterial_50s_ribosomal_subunit": {
        "label": "Bacterial 50S ribosomal subunit proteins",
        "module": "bacterial_50s_ribosomal_subunit_boundary",
        "action": "NEW_SUBMODULE",
        "note": "Large-subunit ribosomal proteins; curate as 50S subunit/rRNA-binding/translation contributors.",
        "genes": [
            "rpmH",
            "rplK",
            "rplA",
            "rplJ",
            "rplL",
            "rplC",
            "rplD",
            "rplW",
            "rplB",
            "rplV",
            "rplP",
            "rpmC",
            "rplN",
            "rplX",
            "rplE",
            "rplF",
            "rplR",
            "rpmD",
            "rplO",
            "rpmJ",
            "rplQ",
            "rplU",
            "rpmA",
            "rplY",
            "rplM",
            "rplS",
            "rpmF",
            "rpmI",
            "rplT",
            "rplI",
            "rpmE",
            "rpmG",
            "rpmB",
        ],
    },
}


def main() -> None:
    rows = list(csv.DictReader(BATCH_TSV.open(), delimiter="\t"))
    row_by_gene = {row["suggested_review_name"]: row for row in rows}

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

    fields = [
        "gene",
        "ordered_locus",
        "uniprot_accession",
        "protein_name",
        "partition_bucket",
        "partition_label",
        "proposed_module",
        "recommended_action",
        "notes",
        "review_status",
        "curation_status",
        "asta_research_status",
    ]
    out_rows = []
    with OUT_TSV.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, delimiter="\t")
        writer.writeheader()
        for row in rows:
            gene = row["suggested_review_name"]
            bucket_id = assigned[gene]
            info = BUCKETS[bucket_id]
            out_row = {
                "gene": gene,
                "ordered_locus": row["ordered_locus"],
                "uniprot_accession": row["uniprot_accession"],
                "protein_name": row["protein_name"],
                "partition_bucket": bucket_id,
                "partition_label": info["label"],
                "proposed_module": info["module"],
                "recommended_action": info["action"],
                "notes": info["note"],
                "review_status": row["review_status"],
                "curation_status": row["curation_status"],
                "asta_research_status": row["asta_research_status"],
            }
            out_rows.append(out_row)
            writer.writerow(out_row)

    counts = Counter(assigned.values())
    examples = defaultdict(list)
    for gene, bucket_id in assigned.items():
        if len(examples[bucket_id]) < 10:
            examples[bucket_id].append(gene)

    lines = [
        "---",
        'title: "PSEPK ppu03010 Ribosome partition"',
        "maturity: DRAFT",
        "tags: [BIOLOGY_DOMAIN, PIPELINE]",
        "species: [PSEPK]",
        "autolink_gene_symbols: false",
        "---",
        "",
        "# PSEPK ppu03010: Ribosome partition",
        "",
        "KEGG ppu03010 is a coherent bacterial ribosome protein set. There is",
        "no unknown/spillover bucket in the primary PSEPK membership, but the",
        "54-gene list should be curated as 30S and 50S subunit batches rather",
        "than as one all-ribosome PR.",
        "",
        "## Outputs",
        "",
        f"- Source batch: `{BATCH_TSV.relative_to(ROOT)}`",
        f"- Partition table: `{OUT_TSV.relative_to(ROOT)}`",
        "",
        "## Partition Summary",
        "",
        "| Bucket | Genes | Proposed module | Action | Example genes |",
        "|---|---:|---|---|---|",
    ]
    for bucket_id, info in BUCKETS.items():
        lines.append(
            f"| `{bucket_id}` | {counts[bucket_id]} | `{info['module']}` | "
            f"{info['action']} | {', '.join(f'`{g}`' for g in examples[bucket_id])} |"
        )

    lines.extend(
        [
            "",
            "## Current Curation Status",
            "",
            "| Bucket | Genes | Review folders | Curated reviews | Asta reports | Module file |",
            "|---|---:|---:|---:|---:|---|",
        ]
    )
    for bucket_id, info in BUCKETS.items():
        bucket_rows = [row for row in out_rows if row["partition_bucket"] == bucket_id]
        review_count = sum(row["review_status"] == "PRESENT" for row in bucket_rows)
        curated_count = sum(row["curation_status"] == "CURATED" for row in bucket_rows)
        asta_count = sum(row["asta_research_status"] == "PRESENT" for row in bucket_rows)
        module_path = ROOT / "modules" / f"{info['module']}.yaml"
        module_status = f"`{module_path.relative_to(ROOT)}`" if module_path.exists() else "missing"
        lines.append(
            f"| `{bucket_id}` | {len(bucket_rows)} | {review_count} | {curated_count} | "
            f"{asta_count} | {module_status} |"
        )
    lines.extend(
        [
            "",
            "## Working Decisions",
            "",
            "- Do not curate all 54 primary genes as one first-pass ribosome PR.",
            "- There is no unknown bucket: every primary member is a small- or",
            "  large-subunit ribosomal protein.",
            "- Split curation into 30S and 50S subunit modules to keep complex",
            "  membership, rRNA binding, and translation contributions tractable.",
            "",
            "## Next Steps",
            "",
            "- Keep ppu03010 registered as `PARTITIONED` in the pathway worklist",
            "  until both subunit batches are complete.",
            "- Treat a subunit bucket as complete once all rows are present,",
            "  curated, Asta-backed, validated, and rendered, and the matching",
            "  `modules/<subunit>_boundary.yaml` validates.",
            "- Once both subunit buckets are complete, treat ppu03010 as a",
            "  completed partitioned pathway rather than collapsing the two",
            "  modules into one 54-gene review unit.",
            "- Run real Falcon module/pathway commands only after one subunit module",
            "  is selected; current Edison Falcon access failure mode is HTTP 402.",
        ]
    )
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(f"Wrote {OUT_TSV.relative_to(ROOT)}")
    print(f"Wrote {OUT_MD.relative_to(ROOT)}")
    for bucket_id, info in BUCKETS.items():
        print(f"{bucket_id}\t{counts[bucket_id]}\t{info['module']}")


if __name__ == "__main__":
    main()
