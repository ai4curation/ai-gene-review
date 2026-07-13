#!/usr/bin/env python3
"""Partition KEGG ppu02025 biofilm formation into curation-scale buckets."""

from __future__ import annotations

import csv
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
BATCH_TSV = ROOT / "projects/P_PUTIDA/batches/ppu02025_biofilm_formation_pseudomonas_boundary.tsv"
OUT_TSV = ROOT / "projects/P_PUTIDA/batches/ppu02025_biofilm_formation_pseudomonas_partition.tsv"
OUT_MD = ROOT / "projects/P_PUTIDA/batches/ppu02025_biofilm_formation_pseudomonas_partition.md"


BUCKETS = {
    "global_gac_csr_crp_biofilm_regulation": {
        "label": "Global Gac/Csr/Crp biofilm regulation",
        "module": "global_biofilm_regulation_boundary",
        "action": "NEW_SUBMODULE",
        "status": "CURATED",
        "note": "Global transcriptional and post-transcriptional regulators with biofilm/motility context.",
        "completion_note": (
            "First-pass gene reviews, Asta gene research, and the "
            "global_biofilm_regulation_boundary module are complete for crp, "
            "gacS, uvrY/gacA, csrA__Q88M29, csrA__Q88G93, and csrA__Q88EJ0. "
            "The ppu02025 uvrY row is represented by the existing local gacA "
            "review folder with uvrY as an alias. Falcon taxon-aware "
            "module/pathway research was attempted with the real command and "
            "failed with HTTP 402."
        ),
        "genes": ["crp", "gacS", "uvrY", "csrA__Q88M29", "csrA__Q88G93", "csrA__Q88EJ0"],
    },
    "wsp_chemotaxis_c_di_gmp_cluster": {
        "label": "Wsp-like chemotaxis/c-di-GMP cluster",
        "module": "wsp_surface_sensing_c_di_gmp_boundary",
        "action": "NEW_SUBMODULE",
        "status": "CURATED",
        "note": "Wsp/Che-like surface-sensing cluster with CheA/CheW/CheB and a diguanylate cyclase.",
        "completion_note": (
            "First-pass gene reviews, Asta gene research, and the "
            "wsp_surface_sensing_c_di_gmp_boundary module are complete. WspC/PP_1490 "
            "is included as already curated local cluster context. Falcon taxon-aware "
            "module/pathway research was attempted with the real command and failed "
            "with HTTP 402."
        ),
        "genes": ["PP_1488", "PP_1489", "PP_1491", "PP_1492", "cheB3", "PP_1494"],
    },
    "c_di_gmp_turnover": {
        "label": "c-di-GMP turnover",
        "module": "c_di_gmp_turnover_boundary",
        "action": "NEW_SUBMODULE",
        "status": "CURATED",
        "note": "Diguanylate cyclase and cyclic-di-GMP phosphodiesterase nodes affecting biofilm/motility state.",
        "completion_note": (
            "First-pass gene reviews, Asta gene research, and the "
            "c_di_gmp_turnover_boundary module are complete for PP_0914, "
            "PP_3581, TpbB, and pde. pde is retained as broad cyclic-nucleotide "
            "phosphodiesterase side context, not as a c-di-GMP-specific EAL "
            "enzyme. Falcon taxon-aware module/pathway research was attempted "
            "with the real command and failed with HTTP 402."
        ),
        "genes": ["PP_0914", "PP_3581", "TpbB", "pde"],
    },
    "t6ss_biofilm_context": {
        "label": "T6SS/biofilm context",
        "module": "bacterial_secretion_system_boundary",
        "action": "EXISTING_OR_REUSE",
        "status": "CURATED",
        "note": "T6SS apparatus/baseplate/sheath and neighboring side context already adjacent to ppu03070.",
        "completion_note": (
            "First-pass gene reviews and Asta gene research are complete for "
            "PP_2617, PP_2620, PP_2623, PP_2624, PP_3088, PP_3093, "
            "PP_3096, puuD, PP_3100, PP_4074, PP_4078, PP_4080, and "
            "PP_5561. The pass reuses modules/bacterial_secretion_system_boundary.yaml "
            "rather than creating a biofilm-specific T6SS module. puuD/PP_3099 is "
            "treated as a likely TssC/VipB-family sheath protein and its EC-derived "
            "urate oxidase activity annotation is marked for removal."
        ),
        "genes": [
            "PP_2617",
            "PP_2620",
            "PP_2623",
            "PP_2624",
            "PP_3088",
            "PP_3093",
            "PP_3096",
            "puuD",
            "PP_3100",
            "PP_4074",
            "PP_4078",
            "PP_4080",
            "PP_5561",
        ],
    },
    "orphan_biofilm_regulatory_sensors": {
        "label": "Orphan biofilm regulatory sensors",
        "module": "orphan_biofilm_regulatory_sensors_boundary",
        "action": "NEW_SUBMODULE",
        "status": "CURATED",
        "note": "Predicted histidine kinases, Hpt/hybrid phosphorelay proteins, and anti-sigma factor context retained as a conservative unresolved regulatory-sensor boundary.",
        "completion_note": (
            "First-pass gene reviews and Asta gene research are complete for "
            "PP_1875, PP_2664, PP_4173, PP_4362, PP_4363, PP_4364, "
            "PP_4781, and PP_4824/retS. The pass created "
            "modules/orphan_biofilm_regulatory_sensors_boundary.yaml and "
            "keeps ligand identities, response-regulator partners, and target "
            "regulons unresolved except for the existing KT2440 retS K1-T6SS "
            "regulatory evidence."
        ),
        "genes": ["PP_1875", "PP_2664", "PP_4173", "PP_4362", "PP_4363", "PP_4364", "PP_4781", "PP_4824"],
    },
    "pil_chp_twitching_regulation": {
        "label": "Pil/Chp twitching regulation",
        "module": "pil_chp_twitching_motility_boundary",
        "action": "NEW_SUBMODULE",
        "status": "CURATED",
        "note": "PilGHIJ and CheA-like proteins for type IV pilus/twitching regulatory signaling.",
        "completion_note": (
            "First-pass gene reviews, Asta gene research, and the "
            "pil_chp_twitching_motility_boundary module are complete for "
            "PP_4987, PP_4988, pilJ, pilI, pilH, and pilG. The pass treats "
            "type IV pilus-dependent motility as pathway context rather than "
            "a directly proven gene-level output for every component. Falcon "
            "taxon-aware module/pathway research was attempted with the real "
            "command and failed with HTTP 402."
        ),
        "genes": ["PP_4987", "PP_4988", "pilJ", "pilI", "pilH", "pilG"],
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
        "bucket_status",
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
                    "bucket_status": info.get("status", "OPEN"),
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
        'title: "PSEPK ppu02025 Biofilm formation partition"',
        "maturity: DRAFT",
        "tags: [BIOLOGY_DOMAIN, PIPELINE]",
        "species: [PSEPK]",
        "autolink_gene_symbols: false",
        "---",
        "",
        "# PSEPK ppu02025: Biofilm formation partition",
        "",
        "KEGG ppu02025 is a Pseudomonas aeruginosa biofilm-formation umbrella.",
        "The PSEPK primary set mixes regulatory, chemotaxis, c-di-GMP, type IV",
        "pilus, and T6SS context rather than a single linear pathway.",
        "",
        "## Outputs",
        "",
        f"- Source batch: `{BATCH_TSV.relative_to(ROOT)}`",
        f"- Partition table: `{OUT_TSV.relative_to(ROOT)}`",
        "",
        "## Partition Summary",
        "",
        "| Bucket | Genes | Proposed module | Action | Status | Example genes |",
        "|---|---:|---|---|---|---|",
    ]
    for bucket_id, info in BUCKETS.items():
        lines.append(
            f"| `{bucket_id}` | {counts[bucket_id]} | `{info['module']}` | "
            f"{info['action']} | {info.get('status', 'OPEN')} | "
            f"{', '.join(f'`{g}`' for g in examples[bucket_id])} |"
        )
    lines.extend(
        [
            "",
            "## Working Decisions",
            "",
            "- Do not curate all 43 primary genes as one biofilm-formation PR.",
            "- Reuse the bacterial secretion-system boundary for T6SS apparatus",
            "  genes instead of creating a biofilm-specific T6SS module.",
            "- The strongest new biofilm-specific batches are Wsp-like surface sensing,",
            "  c-di-GMP turnover, Gac/Csr/Crp global regulation, and Pil/Chp",
            "  twitching regulation.",
            "- The orphan histidine kinase/Hpt/anti-sigma entries are captured as a",
            "  conservative unresolved regulatory-sensor boundary rather than direct",
            "  per-gene biofilm-output assertions.",
            "",
            "## Completed Sub-batches",
            "",
            "- `wsp_chemotaxis_c_di_gmp_cluster`: first-pass gene reviews, Asta gene",
            "  research, and `modules/wsp_surface_sensing_c_di_gmp_boundary.yaml`",
            "  are complete for PP_1488, PP_1489, PP_1491, PP_1492, cheB3, and",
            "  PP_1494, with already curated wspC/PP_1490 included as local cluster",
            "  context.",
            "- Falcon taxon-aware module/pathway research for",
            "  `wsp_surface_sensing_c_di_gmp_boundary` + `ppu02025` + PSEPK was",
            "  attempted with the real command and failed with HTTP 402, so no",
            "  Falcon report is cited for this sub-batch.",
            "- `c_di_gmp_turnover`: first-pass gene reviews, Asta gene research,",
            "  and `modules/c_di_gmp_turnover_boundary.yaml` are complete for",
            "  PP_0914, PP_3581, TpbB, and pde.",
            "- Falcon taxon-aware module/pathway research for",
            "  `c_di_gmp_turnover_boundary` + `ppu02025` + PSEPK was attempted",
            "  with the real command and failed with HTTP 402, so no Falcon",
            "  report is cited for this sub-batch.",
            "- `pil_chp_twitching_regulation`: first-pass gene reviews, Asta",
            "  gene research, and `modules/pil_chp_twitching_motility_boundary.yaml`",
            "  are complete for PP_4987, PP_4988, pilJ, pilI, pilH, and pilG.",
            "- Falcon taxon-aware module/pathway research for",
            "  `pil_chp_twitching_motility_boundary` + `ppu02025` + PSEPK was",
            "  attempted with the real command and failed with HTTP 402, so no",
            "  Falcon report is cited for this sub-batch.",
            "- `global_gac_csr_crp_biofilm_regulation`: first-pass gene reviews,",
            "  Asta gene research, and `modules/global_biofilm_regulation_boundary.yaml`",
            "  are complete for crp, gacS, uvrY/gacA, csrA__Q88M29,",
            "  csrA__Q88G93, and csrA__Q88EJ0.",
            "- Falcon taxon-aware module/pathway research for",
            "  `global_biofilm_regulation_boundary` + `ppu02025` + PSEPK was",
            "  attempted with the real command and failed with HTTP 402, so no",
            "  Falcon report is cited for this sub-batch.",
            "- `t6ss_biofilm_context`: first-pass gene reviews and Asta",
            "  gene research are complete for PP_2617, PP_2620, PP_2623,",
            "  PP_2624, PP_3088, PP_3093, PP_3096, puuD, PP_3100,",
            "  PP_4074, PP_4078, PP_4080, and PP_5561. This bucket reuses",
            "  `modules/bacterial_secretion_system_boundary.yaml`; puuD/PP_3099",
            "  is interpreted as a likely TssC/VipB-family sheath protein and",
            "  its EC-derived urate oxidase activity annotation is marked for",
            "  removal.",
            "- `orphan_biofilm_regulatory_sensors`: first-pass gene reviews,",
            "  Asta gene research, and",
            "  `modules/orphan_biofilm_regulatory_sensors_boundary.yaml` are",
            "  complete for PP_1875, PP_2664, PP_4173, PP_4362, PP_4363,",
            "  PP_4364, PP_4781, and PP_4824/retS.",
            "",
            "## Next Steps",
            "",
            "- Register ppu02025 as `PARTITIONED` in the pathway worklist.",
            "- Treat all six ppu02025 sub-buckets as first-pass complete: Wsp-like",
            "  surface sensing, c-di-GMP turnover, Pil/Chp twitching regulation,",
            "  Gac/Csr/Crp global regulation, T6SS context via the secretion",
            "  boundary module, and orphan regulatory sensors.",
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
