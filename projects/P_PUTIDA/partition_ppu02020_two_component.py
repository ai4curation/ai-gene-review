#!/usr/bin/env python3
"""Partition KEGG ppu02020 into curation-scale submodules.

KEGG "Two-component system" mixes response regulators/sensor kinases with
transporters, pili, efflux pumps, ECF sigma systems, and other pathway context.
This script classifies the primary PSEPK ppu02020 batch into smaller curation
units so later work can fetch and review coherent modules rather than a 99-gene
umbrella.
"""

from __future__ import annotations

import csv
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
BATCH_TSV = ROOT / "projects/P_PUTIDA/batches/ppu02020_two_component_system_boundary.tsv"
OUT_TSV = ROOT / "projects/P_PUTIDA/batches/ppu02020_two_component_system_partition.tsv"
OUT_MD = ROOT / "projects/P_PUTIDA/batches/ppu02020_two_component_system_partition.md"


BUCKETS = {
    "dna_replication_spillover": {
        "label": "Replication spillover",
        "module": "bacterial_dna_replication",
        "action": "SIDE_CONTEXT",
        "status": "CURATED",
        "note": "KEGG spillover; DnaA belongs with bacterial DNA replication, not two-component signaling.",
        "completion_note": (
            "First-pass gene review and Asta gene research are complete. DnaA "
            "has been added to the bacterial_dna_replication module as the "
            "origin-recognition/initiation side context from ppu02020."
        ),
        "genes": ["dnaA"],
    },
    "heavy_metal_copper_zinc_response": {
        "label": "Heavy-metal/copper/zinc response and efflux",
        "module": "metal_cation_response_efflux_boundary",
        "action": "NEW_SUBMODULE",
        "status": "CURATED",
        "note": "Czc/Cop/Cus regulatory and efflux context; likely needs a metal-response boundary module.",
        "completion_note": (
            "First-pass gene reviews, Asta gene research, and the "
            "metal_cation_response_efflux_boundary module are complete. Falcon "
            "taxon-aware module/pathway research was attempted with the real "
            "command and failed with HTTP 402."
        ),
        "genes": [
            "czcR-I",
            "czrSA",
            "czcR-II",
            "PP_1437",
            "czcR-III",
            "PP_2157",
            "copR-I",
            "copR-II",
            "copS",
            "czcC",
            "cusB",
            "cusA",
            "cusF",
        ],
    },
    "iron_uptake_regulation": {
        "label": "Iron uptake regulation",
        "module": "iron_uptake_regulation_boundary",
        "action": "NEW_SUBMODULE",
        "status": "CURATED",
        "note": "Pfe/Fec/Fep iron-uptake regulatory and receptor context; separate from generic TCS.",
        "completion_note": (
            "First-pass gene reviews, Asta gene research, and the iron_uptake_regulation_boundary "
            "module are complete; Falcon taxon-aware module/pathway research was attempted with "
            "the real command and failed with HTTP 402."
        ),
        "genes": ["pfeS-I", "PP_0534", "PP_1651", "pfeS-II", "fepA", "PP_3576", "fecI", "PP_4607", "PP_4611", "PP_4612"],
    },
    "alginate_biofilm_regulation": {
        "label": "Alginate, c-di-GMP, and biofilm regulation",
        "module": "alginate_biofilm_regulation_boundary",
        "action": "NEW_SUBMODULE",
        "status": "CURATED",
        "note": "Alg/Kin/Wsp/Cbr/Fle-like regulatory context for biofilm or surface behavior.",
        "completion_note": (
            "First-pass gene reviews, Asta gene research, and the "
            "alginate_biofilm_regulation_boundary module are complete for KinB/AlgB, "
            "AlgR, WspC/CheR1, FleS, and PP_4696. Falcon taxon-aware module/pathway "
            "research was attempted with the real command and failed with HTTP 402."
        ),
        "genes": ["kinB", "algB", "algR", "wspC", "fleS", "PP_4696"],
    },
    "osmotic_envelope_efflux_regulation": {
        "label": "Osmotic, envelope, and multidrug-efflux regulation",
        "module": "osmotic_envelope_efflux_regulation_boundary",
        "action": "NEW_SUBMODULE",
        "status": "CURATED",
        "note": "OmpR/EnvZ, Evg-like, and Mdt efflux context; likely an envelope-stress/efflux boundary.",
        "completion_note": (
            "First-pass gene reviews, Asta gene research, and the "
            "osmotic_envelope_efflux_regulation_boundary module are complete; Falcon "
            "taxon-aware module/pathway research was attempted with the real command and "
            "failed with HTTP 402."
        ),
        "genes": ["ompR", "envZ", "PP_2100", "evgA", "mdtC", "mdtB", "mdtA"],
    },
    "dicarboxylate_tricarboxylate_transport_regulation": {
        "label": "Dicarboxylate/tricarboxylate transport regulation",
        "module": "dicarboxylate_tricarboxylate_transport_regulation_boundary",
        "action": "NEW_SUBMODULE",
        "status": "CURATED",
        "note": "Dct/Tct/Uhp transport regulators and transporter context; keep transporters with their regulated import systems.",
        "completion_note": (
            "First-pass gene reviews, Asta gene research, and the "
            "dicarboxylate_tricarboxylate_transport_regulation_boundary module "
            "are complete. Falcon taxon-aware module/pathway research was "
            "attempted with the real command and failed with HTTP 402."
        ),
        "genes": [
            "dctD-I",
            "PP_0264",
            "uhpA",
            "dctD-II",
            "PP_1067",
            "PP_1167",
            "PP_1168",
            "dctP",
            "dctA",
            "dctD-III",
            "dctB",
            "PP_1416",
            "PP_1417",
            "PP_1418",
            "tctD",
            "PP_1421",
            "dctA-II",
            "dctA-III",
            "PP_3124",
        ],
    },
    "ecf_sigma_anti_sigma": {
        "label": "ECF sigma/anti-sigma systems",
        "module": "ecf_sigma_anti_sigma_boundary",
        "action": "NEW_SUBMODULE",
        "status": "CURATED",
        "note": "ECF sigma factors and transmembrane anti-sigma/sensor proteins; not canonical His-Asp TCS.",
        "completion_note": (
            "First-pass gene reviews, Asta gene research, and the "
            "ecf_sigma_anti_sigma_boundary module are complete. Falcon "
            "taxon-aware module/pathway research was attempted with the real "
            "command and failed with HTTP 402."
        ),
        "genes": ["PP_0161", "PP_0162", "PP_0351", "PP_0352", "PP_0667", "PP_0703", "PP_0704", "PP_0866", "PP_3085", "PP_3086"],
    },
    "nitrogen_phosphate_potassium_homeostasis": {
        "label": "Nitrogen, phosphate, and potassium homeostasis",
        "module": "inorganic_nutrient_homeostasis_regulation_boundary",
        "action": "NEW_SUBMODULE",
        "status": "CURATED",
        "note": "NtrBC/GlnD, PhoBR, and Kdp potassium-transport/regulation context.",
        "completion_note": (
            "First-pass gene reviews, Asta gene research, and the "
            "inorganic_nutrient_homeostasis_regulation_boundary module are complete; "
            "Falcon taxon-aware module/pathway research was attempted with the real "
            "command and failed with HTTP 402."
        ),
        "genes": ["glnD", "glnL", "glnG", "phoB", "phoR", "kdpD", "kdpC", "kdpB", "kdpA", "kdpF"],
    },
    "pili_surface_adhesion": {
        "label": "Pili, adhesion, and surface structures",
        "module": "pili_surface_adhesion_boundary",
        "action": "NEW_SUBMODULE",
        "status": "CURATED",
        "note": "Pilin, fimbrial usher/chaperone, and Csu-like surface-adhesion context.",
        "completion_note": (
            "First-pass gene reviews, Asta gene research, and the "
            "pili_surface_adhesion_boundary module are complete. Falcon "
            "taxon-aware module/pathway research was attempted with the real "
            "command and failed with HTTP 402."
        ),
        "genes": ["pilA", "fimD", "PP_1890", "PP_2356", "PP_2357", "PP_2358", "PP_2359", "PP_2360", "PP_2361", "PP_2362", "PP_2363", "PP_3126"],
    },
    "orphan_generic_tcs": {
        "label": "Orphan or generic two-component regulators",
        "module": "orphan_two_component_regulators_boundary",
        "action": "NEW_SUBMODULE",
        "status": "CURATED",
        "note": "Predicted response regulators, sensor kinases, and one FecR-like anti-sigma sensor without resolved input signals or target regulons.",
        "completion_note": (
            "First-pass gene reviews, Asta gene research, and the "
            "orphan_two_component_regulators_boundary module are complete. Falcon "
            "taxon-aware module/pathway research was attempted with the real "
            "command and failed with HTTP 402."
        ),
        "genes": ["PP_0574", "PP_0887", "regA", "PP_1007", "bvgA", "PP_1181", "PP_1182", "PP_2671", "PP_3412", "PP_3413"],
    },
    "protein_phosphatase_spillover": {
        "label": "Protein-phosphatase spillover",
        "module": "protein_phosphorylation_boundary",
        "action": "SIDE_CONTEXT",
        "status": "CURATED",
        "note": "Etp is a tyrosine phosphatase side node, not a His-Asp two-component relay member.",
        "completion_note": (
            "First-pass gene review, Asta gene research, and the "
            "protein_phosphorylation_boundary side-context module are complete "
            "for Etp."
        ),
        "genes": ["etp"],
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
        'title: "PSEPK ppu02020 Two-component system partition"',
        "maturity: DRAFT",
        "tags: [BIOLOGY_DOMAIN, PIPELINE]",
        "species: [PSEPK]",
        "autolink_gene_symbols: false",
        "---",
        "",
        "# PSEPK ppu02020: Two-component system partition",
        "",
        "KEGG ppu02020 is an umbrella map, not a single satisfiable module. This",
        "partition keeps the primary 99-gene PSEPK batch as a triage table and",
        "splits it into curation-scale systems.",
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
            "- Treat `modules/two_component_relay.yaml` as the reusable motif, not as",
            "  the PSEPK ppu02020 umbrella module.",
            "- Do not fetch and curate all 99 genes as one PR. Create smaller boundary",
            "  modules from the partition table, starting with high-signal paired",
            "  systems such as Dct/Tct transport regulation, nutrient homeostasis,",
            "  and orphan/generic TCS systems.",
            "- Transporter, efflux, pili, and housekeeping genes should remain in the",
            "  relevant transport/envelope/replication modules unless the local",
            "  regulatory system needs them as boundary context.",
            "- `dnaA` and `etp` are side-context spillovers for this KEGG map and should",
            "  not be used as evidence for two-component signaling.",
            "",
            "## Completed Sub-batches",
            "",
            "- `nitrogen_phosphate_potassium_homeostasis`: first-pass gene reviews,",
            "  Asta gene research, and",
            "  `modules/inorganic_nutrient_homeostasis_regulation_boundary.yaml` are",
            "  complete for GlnD/NtrB/NtrC, PhoR/PhoB, and KdpD/KdpE/KdpFABC.",
            "- `dna_replication_spillover`: first-pass gene review and Asta gene",
            "  research are complete for dnaA, and dnaA has been added to",
            "  `modules/bacterial_dna_replication.yaml` as replication-origin",
            "  recognition/initiation side context from ppu02020.",
            "- `protein_phosphatase_spillover`: first-pass gene review, Asta gene",
            "  research, and `modules/protein_phosphorylation_boundary.yaml` are",
            "  complete for Etp protein tyrosine phosphatase side context.",
            "- Falcon taxon-aware module/pathway research for",
            "  `inorganic_nutrient_homeostasis_regulation_boundary` + `ppu02020` +",
            "  PSEPK was attempted with the real command and failed with HTTP 402, so",
            "  no Falcon report is cited for this sub-batch.",
            "- `iron_uptake_regulation`: first-pass gene reviews, Asta gene",
            "  research, and `modules/iron_uptake_regulation_boundary.yaml` are",
            "  complete for PfeS/PfeR-like two-component regulators, FepA",
            "  siderophore-iron uptake, and FecI/FecR-like ECF sigma regulation.",
            "- Falcon taxon-aware module/pathway research for",
            "  `iron_uptake_regulation_boundary` + `ppu02020` + PSEPK was",
            "  attempted with the real command and failed with HTTP 402, so no",
            "  Falcon report is cited for this sub-batch.",
            "- `osmotic_envelope_efflux_regulation`: first-pass gene reviews,",
            "  Asta gene research, and",
            "  `modules/osmotic_envelope_efflux_regulation_boundary.yaml` are",
            "  complete for EnvZ/OmpR, PP_2100/EvgA-like regulation, and",
            "  MdtABC efflux-pump context.",
            "- Falcon taxon-aware module/pathway research for",
            "  `osmotic_envelope_efflux_regulation_boundary` + `ppu02020` +",
            "  PSEPK was attempted with the real command and failed with HTTP 402,",
            "  so no Falcon report is cited for this sub-batch.",
            "- `alginate_biofilm_regulation`: first-pass gene reviews, Asta",
            "  gene research, and",
            "  `modules/alginate_biofilm_regulation_boundary.yaml` are",
            "  complete for KinB/AlgB, AlgR, WspC/CheR1 biofilm control,",
            "  FleS, and PP_4696 surface-behavior regulatory context.",
            "- Falcon taxon-aware module/pathway research for",
            "  `alginate_biofilm_regulation_boundary` + `ppu02020` + PSEPK",
            "  was attempted with the real command and failed with HTTP 402,",
            "  so no Falcon report is cited for this sub-batch.",
            "- `ecf_sigma_anti_sigma`: first-pass gene reviews, Asta gene",
            "  research, and `modules/ecf_sigma_anti_sigma_boundary.yaml` are",
            "  complete for the PP_0161/PP_0162, PP_0351/PP_0352,",
            "  PP_0703/PP_0704, and PP_3085/PP_3086 local pairs plus the",
            "  orphan PP_0667 ECF sigma factor and PP_0866 FecR-like sensor.",
            "- Falcon taxon-aware module/pathway research for",
            "  `ecf_sigma_anti_sigma_boundary` + `ppu02020` + PSEPK was",
            "  attempted with the real command and failed with HTTP 402,",
            "  so no Falcon report is cited for this sub-batch.",
            "- `heavy_metal_copper_zinc_response`: first-pass gene reviews,",
            "  Asta gene research, and",
            "  `modules/metal_cation_response_efflux_boundary.yaml` are complete",
            "  for Czc/Cop/Cus response regulators, CztS/SilS/CopS-like sensor",
            "  kinases, and the czcC-cusBAF copper/cation efflux locus.",
            "- Falcon taxon-aware module/pathway research for",
            "  `metal_cation_response_efflux_boundary` + `ppu02020` + PSEPK",
            "  was attempted with the real command and failed with HTTP 402,",
            "  so no Falcon report is cited for this sub-batch.",
            "- `pili_surface_adhesion`: first-pass gene reviews, Asta gene",
            "  research, and `modules/pili_surface_adhesion_boundary.yaml` are",
            "  complete for PilA type IV pilin context, a FimC/FimD-like",
            "  chaperone-usher pair, the PP_2356/PP_2357-PP_2363 Csu-like",
            "  surface-adhesion cluster, and PP_3126 polysaccharide-export",
            "  side context.",
            "- Falcon taxon-aware module/pathway research for",
            "  `pili_surface_adhesion_boundary` + `ppu02020` + PSEPK was",
            "  attempted with the real command and failed with HTTP 402,",
            "  so no Falcon report is cited for this sub-batch.",
            "- `orphan_generic_tcs`: first-pass gene reviews, Asta gene",
            "  research, and `modules/orphan_two_component_regulators_boundary.yaml`",
            "  are complete for PP_0887/regA, PP_1182/PP_1181,",
            "  PP_3413/PP_3412, orphan PP_0574, bvgA, PP_2671, and",
            "  the FecR-like PP_1007 anti-sigma sensor side context.",
            "- Falcon taxon-aware module/pathway research for",
            "  `orphan_two_component_regulators_boundary` + `ppu02020` + PSEPK",
            "  was attempted with the real command and failed with HTTP 402,",
            "  so no Falcon report is cited for this sub-batch.",
            "",
            "## Next Steps",
            "",
            "- Keep ppu02020 registered as `PARTITIONED` in the pathway worklist rather",
            "  than `NEEDS_MODULE_MAPPING`.",
            "- ppu02020 now has review and Asta coverage for all 99 partition-table",
            "  genes; continue with another pathway partition rather than reopening",
            "  the 99-gene two-component-system umbrella.",
            "- Run real Falcon module/pathway commands only for selected submodules; the",
            "  current Edison Falcon access failure mode is HTTP 402.",
        ]
    )
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(f"Wrote {OUT_TSV.relative_to(ROOT)}")
    print(f"Wrote {OUT_MD.relative_to(ROOT)}")
    for bucket_id, info in BUCKETS.items():
        print(f"{bucket_id}\t{counts[bucket_id]}\t{info['module']}")


if __name__ == "__main__":
    main()
