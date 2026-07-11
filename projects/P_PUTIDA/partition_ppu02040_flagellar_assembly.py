#!/usr/bin/env python3
"""Partition KEGG ppu02040 flagellar assembly into curation-scale buckets."""

from __future__ import annotations

import csv
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
BATCH_TSV = ROOT / "projects/P_PUTIDA/batches/ppu02040_bacterial_flagellar_assembly_boundary.tsv"
OUT_TSV = ROOT / "projects/P_PUTIDA/batches/ppu02040_bacterial_flagellar_assembly_partition.tsv"
OUT_MD = ROOT / "projects/P_PUTIDA/batches/ppu02040_bacterial_flagellar_assembly_partition.md"


BUCKETS = {
    "flagellar_regulation_sigma_master_control": {
        "label": "Flagellar sigma/master regulation",
        "module": "flagellar_regulation_boundary",
        "action": "NEW_SUBMODULE",
        "note": "Sigma factors, anti-sigma factor, and master/AAA+ transcriptional regulators that control flagellar expression rather than form the apparatus.",
        "genes": ["rpoD", "rpoN", "fliA", "atoC", "fleQ", "flgM"],
    },
    "nonflagellar_transport_envelope_spillovers": {
        "label": "Nonflagellar transport/envelope spillovers",
        "module": "transport_envelope_spillover_boundary",
        "action": "EXISTING_OR_REUSE",
        "note": "Cystine/sugar-binding and OmpA-family proteins that should not be treated as flagellar apparatus members without stronger evidence.",
        "genes": ["fliY", "PP_1087", "PP_5157"],
    },
    "flagellar_export_assembly_chaperones": {
        "label": "Flagellar export and assembly/chaperone proteins",
        "module": "flagellar_export_assembly_boundary",
        "action": "NEW_SUBMODULE",
        "note": "Flagellar type-III-like export gate, export ATPase complex, hook-length control, and secretion/assembly chaperones.",
        "genes": [
            "flhA",
            "flhB",
            "fliR",
            "fliQ",
            "fliP",
            "fliO",
            "fliK",
            "fliJ",
            "fliI",
            "fliH",
            "fliT",
            "fliS",
            "flgA",
            "PP_4396",
        ],
    },
    "flagellar_basal_body_hook_filament": {
        "label": "Flagellar basal body, hook, and filament",
        "module": "flagellar_basal_body_hook_filament_boundary",
        "action": "NEW_SUBMODULE",
        "note": "Basal-body rings/rod, hook, hook-filament junction, cap, and flagellin structural components plus FlgJ peptidoglycan access context.",
        "genes": [
            "fliF",
            "fliE",
            "fliD",
            "fliC",
            "flgL",
            "flgK",
            "flgJ",
            "flgI",
            "flgH",
            "flgG",
            "flgF",
            "flgE",
            "flgD",
            "flgC",
            "flgB",
        ],
    },
    "flagellar_motor_switch_stator": {
        "label": "Flagellar motor, switch, and stator",
        "module": "flagellar_motor_switch_stator_boundary",
        "action": "NEW_SUBMODULE",
        "note": "Motor/stator rotation proteins and C-ring/switch components, including FliL-family motor-associated proteins.",
        "genes": ["PP_4335", "PP_4336", "fliN", "fliM", "fliL", "fliG", "motB", "motA", "PP_5209"],
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
                    "review_status": row["review_status"],
                    "curation_status": row["curation_status"],
                    "asta_research_status": row["asta_research_status"],
                }
            )

    counts = Counter(assigned.values())
    examples = defaultdict(list)
    for gene, bucket_id in assigned.items():
        if len(examples[bucket_id]) < 8:
            examples[bucket_id].append(gene)

    lines = [
        "---",
        'title: "PSEPK ppu02040 Flagellar assembly partition"',
        "maturity: DRAFT",
        "tags: [BIOLOGY_DOMAIN, PIPELINE]",
        "species: [PSEPK]",
        "autolink_gene_symbols: false",
        "---",
        "",
        "# PSEPK ppu02040: Flagellar assembly partition",
        "",
        "KEGG ppu02040 is a coherent flagellar biology map, but the PSEPK",
        "primary set is too broad for one first-pass curation batch. It mixes",
        "structural apparatus, export/assembly factors, motor components,",
        "regulators, and a few nonflagellar transport/envelope side entries.",
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
            "- Do not curate all 47 primary genes as one first-pass flagellar PR.",
            "- Keep `fliY`, `PP_1087`, and `PP_5157` out of the flagellar apparatus",
            "  core unless specific evidence ties them to flagellum assembly.",
            "- Separate global sigma/master regulation from structural apparatus",
            "  curation so broad transcription annotations do not dominate the module.",
            "- The strongest flagellar-apparatus batches are export/assembly,",
            "  basal-body/hook/filament, and motor/switch/stator.",
            "",
            "## Completed First-Pass Sub-Batches",
            "",
            "- `flagellar_motor_switch_stator`: 9/9 genes now have review folders,",
            "  Asta reports, first-pass curation, rendered gene pages, and a",
            "  validated/rendered module",
            "  (`modules/flagellar_motor_switch_stator_boundary.yaml`). PP_4335",
            "  and PP_4336 are treated as MotD/MotC aliases for the MotCD stator,",
            "  while FliL paralog roles remain unresolved.",
            "- `flagellar_export_assembly_chaperones`: 14/14 genes now have",
            "  review folders, Asta reports, first-pass curation, rendered gene",
            "  pages, and a validated/rendered module",
            "  (`modules/flagellar_export_assembly_boundary.yaml`). The batch",
            "  separates the membrane export gate, FliI/FliH/FliJ export-energy",
            "  module, hook-length control, and late assembly/chaperone support.",
            "- `flagellar_basal_body_hook_filament`: 15/15 genes now have",
            "  review folders, Asta reports, first-pass curation, rendered gene",
            "  pages, and a validated/rendered module",
            "  (`modules/flagellar_basal_body_hook_filament_boundary.yaml`).",
            "  The batch separates MS-ring/early basal body, rod/peptidoglycan",
            "  clearance, P/L rings, hook/hook-filament junction, and",
            "  filament/cap structural layers.",
            "- `flagellar_regulation_sigma_master_control`: 6/6 genes now have",
            "  review folders, Asta reports, first-pass curation, rendered gene",
            "  pages, and a validated/rendered module",
            "  (`modules/flagellar_regulation_boundary.yaml`). The batch",
            "  separates housekeeping sigma context, RpoN/sigma-54, FliA",
            "  sigma-28, FleQ/AtoC-like activators, and the FlgM anti-sigma",
            "  checkpoint.",
            "- `nonflagellar_transport_envelope_spillovers`: 3/3 genes now",
            "  have review folders, Asta reports, first-pass curation, rendered",
            "  gene pages, and a validated/rendered boundary module",
            "  (`modules/transport_envelope_spillover_boundary.yaml`). The",
            "  batch keeps fliY, PP_1087, and PP_5157 outside the flagellar",
            "  apparatus core unless direct evidence emerges.",
            "",
            "## Next Steps",
            "",
            "- The ppu02040 first-pass partition is complete: all five buckets",
            "  now have curated/researched gene reviews and validated/rendered",
            "  modules or boundary modules.",
            "- Keep the spillover module out of the flagellar apparatus core",
            "  unless direct functional evidence emerges.",
            "- Run real Falcon module/pathway commands only after a concrete submodule",
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
