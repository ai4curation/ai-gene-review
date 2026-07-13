#!/usr/bin/env python3
"""Partition KEGG ppu04122 sulfur relay system into curation-scale buckets."""

from __future__ import annotations

import csv
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
BATCH_TSV = ROOT / "projects/P_PUTIDA/batches/ppu04122_sulfur_relay_system_boundary.tsv"
OUT_TSV = ROOT / "projects/P_PUTIDA/batches/ppu04122_sulfur_relay_system_partition.tsv"
OUT_MD = ROOT / "projects/P_PUTIDA/batches/ppu04122_sulfur_relay_system_partition.md"
GENE_ROOT = ROOT / "genes/PSEPK"


BUCKETS = {
    "molybdopterin_moco_sulfur_relay": {
        "label": "Molybdopterin/MoCo sulfur relay",
        "module": "molybdopterin_biosynthesis_sulfur_relay_boundary",
        "action": "NEW_SUBMODULE",
        "note": "Moa/Moe sulfur-carrier adenylation and molybdopterin biosynthesis components; many already appear as side context in folate/MoCo-related maps.",
        "genes": ["moeB", "moaC", "moaD", "moaE", "PP_1969", "moaB-I", "PP_2482", "moaA", "moaB-II"],
    },
    "tus_mnma_trna_thiolation": {
        "label": "Tus/MnmA tRNA thiolation",
        "module": "mnma_tus_trna_thiolation_boundary",
        "action": "NEW_SUBMODULE",
        "note": "Tus sulfur-transfer chain and MnmA tRNA 2-thiouridylase context for wobble-uridine thiolation.",
        "genes": ["tusA-I", "tusA", "tusD", "PP_3994", "PP_3995", "tusE", "mnmA"],
    },
    "thiamine_this_sulfur_carrier": {
        "label": "ThiS thiamine sulfur-carrier context",
        "module": "thiamine_biosynthesis",
        "action": "EXISTING_OR_REUSE",
        "note": "ThiS sulfur carrier already promoted into the thiamine-biosynthesis module; keep separate from MoaD and Tus carriers.",
        "genes": ["PP_5105"],
    },
    "rhodanese_mercaptopyruvate_side_nodes": {
        "label": "Rhodanese/mercaptopyruvate sulfurtransferase side nodes",
        "module": "sulfur_metabolism_boundary",
        "action": "EXISTING_OR_REUSE",
        "note": "General rhodanese/3-mercaptopyruvate sulfurtransferases already handled in sulfur-metabolism side context.",
        "genes": ["rhdA", "sseA"],
    },
}


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
    with OUT_TSV.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, delimiter="\t")
        writer.writeheader()
        for row in rows:
            gene = row["suggested_review_name"]
            bucket_id = assigned[gene]
            info = BUCKETS[bucket_id]
            writer.writerow(
                {
                    "gene": gene,
                    "ordered_locus": row["ordered_locus"],
                    "uniprot_accession": row["uniprot_accession"],
                    "protein_name": row["protein_name"],
                    "partition_bucket": bucket_id,
                    "partition_label": info["label"],
                    "proposed_module": info["module"],
                    "recommended_action": info["action"],
                    "notes": info["note"],
                    "review_status": review_status(gene),
                    "curation_status": curation_status(gene),
                    "asta_research_status": asta_research_status(gene),
                }
            )

    counts = Counter(assigned.values())
    examples = defaultdict(list)
    for gene, bucket_id in assigned.items():
        if len(examples[bucket_id]) < 8:
            examples[bucket_id].append(gene)

    lines = [
        "---",
        'title: "PSEPK ppu04122 Sulfur relay system partition"',
        "maturity: DRAFT",
        "tags: [BIOLOGY_DOMAIN, PIPELINE]",
        "species: [PSEPK]",
        "autolink_gene_symbols: false",
        "---",
        "",
        "# PSEPK ppu04122: Sulfur relay system partition",
        "",
        "KEGG ppu04122 is a sulfur-transfer umbrella. The PSEPK primary set",
        "mixes molybdopterin/MoCo sulfur-carrier chemistry, Tus/MnmA tRNA",
        "thiolation, ThiS thiamine sulfur-carrier context, and general",
        "rhodanese/mercaptopyruvate sulfurtransferase side nodes.",
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
            "## Working Decisions",
            "",
            "- Do not curate all 19 primary genes as one generic sulfur-relay PR.",
            "- Keep MoaD/MoeB molybdopterin sulfur-carrier chemistry separate from",
            "  ThiS thiamine sulfur-carrier and Tus/MnmA tRNA thiolation.",
            "- Keep `rhdA` and `sseA` with sulfur-metabolism sulfurtransferase context",
            "  unless a specific sulfur-relay mechanism is selected.",
            "- `PP_5105` already belongs with the thiamine-biosynthesis ThiS gap-fill.",
            "",
            "## Completed Sub-batches",
            "",
            "- `tus_mnma_trna_thiolation`: seven genes fetched, Asta-backed,",
            "  first-pass curated, validated, and rendered; new module",
            "  `modules/mnma_tus_trna_thiolation_boundary.yaml` created and",
            "  validated. `tusA-I` and `PP_3994` have no fetched GOA rows, so",
            "  their inferred roles are recorded in `core_functions` and module",
            "  knowledge gaps rather than as synthetic `existing_annotations`.",
            "- `molybdopterin_moco_sulfur_relay`: nine genes present,",
            "  Asta-backed, first-pass curated, and validated; new module",
            "  `modules/molybdopterin_biosynthesis_sulfur_relay_boundary.yaml`",
            "  created and validated. `moeB` was curated as the MoaD",
            "  adenylyltransferase, with rhodanese/sulfotransferase",
            "  over-propagations removed, and `moaD` was curated as the sulfur",
            "  carrier subunit of molybdopterin synthase.",
            "",
            "## Next Steps",
            "",
            "- The primary ppu04122 curation gaps are now closed at first pass:",
            "  all 19 primary genes have review folders, Asta reports, and",
            "  curated review YAMLs.",
            "- Keep `PP_5105` with thiamine biosynthesis and `rhdA`/`sseA` with",
            "  sulfur-metabolism sulfurtransferase context unless a future",
            "  sulfur-relay-specific mechanism is selected.",
            "- Rerun real Falcon module/pathway commands only when Edison Falcon",
            "  access is available; current failure mode is HTTP 402.",
        ]
    )
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(f"Wrote {OUT_TSV.relative_to(ROOT)}")
    print(f"Wrote {OUT_MD.relative_to(ROOT)}")
    for bucket_id, info in BUCKETS.items():
        print(f"{bucket_id}\t{counts[bucket_id]}\t{info['module']}")


if __name__ == "__main__":
    main()
