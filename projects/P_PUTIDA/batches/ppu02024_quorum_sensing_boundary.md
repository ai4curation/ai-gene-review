---
title: "PSEPK ppu02024 Quorum sensing batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK ppu02024: Quorum sensing

- Module seed: `quorum_sensing_boundary`
- Candidate genes from membership table: 60
- Primary bucket genes: 60
- Existing review files: 60
- Curated review files: 60
- Existing Asta research files: 60

## Required Workflow

- [x] Curate or update the species-neutral module.
- [ ] Run module-level Falcon deep research. Attempted before 2026-07-11 status normalization; blocked by Edison HTTP 402 before report generation.
- [ ] Run module + pathway + PSEPK Falcon deep research. Attempted before 2026-07-11 status normalization; blocked by Edison HTTP 402 before report generation.
- [x] Fetch all selected genes with `just fetch-gene PSEPK <gene>`.
- [x] Run Asta deep research for selected genes.
- [x] Curate each selected gene review.
- [x] Validate module and gene reviews.
- [ ] Open one PR for this module/pathway.
- [ ] Shepherd PR through review, CI, and merge readiness.

## Candidate Genes

Status caveat: this generated candidate table still reflects the original
boundary TSV status for some rows. The current authoritative status is the
partition TSV (`projects/P_PUTIDA/batches/ppu02024_quorum_sensing_partition.tsv`)
plus on-disk review/Asta files: 60/60 review YAMLs and 60/60 Asta reports are
present.

| Done | Gene | Locus | UniProt | Primary bucket | Existing review | Curation | Asta research | Protein |
|---|---|---|---|---|---|---|---|---|
| [ ] | `fur__Q88RL0` | PP_0119 | Q88RL0 | kegg:ppu02024 | MISSING | MISSING | MISSING | Ferric uptake regulation protein |
| [ ] | `potA` | PP_0411 | Q88QS7 | kegg:ppu02024 | MISSING | MISSING | MISSING | Spermidine/putrescine import ATP-binding protein PotA (EC 7.6.2.11) |
| [ ] | `PP_0412` | PP_0412 | Q88QS6 | kegg:ppu02024 | MISSING | MISSING | MISSING | Polyamine ABC transporter, periplasmic polyamine-binding protein |
| [ ] | `PP_0413` | PP_0413 | Q88QS5 | kegg:ppu02024 | MISSING | MISSING | MISSING | Polyamine ABC transporter, permease protein |
| [ ] | `PP_0414` | PP_0414 | Q88QS4 | kegg:ppu02024 | MISSING | MISSING | MISSING | Polyamine ABC transporter, permease protein |
| [x] | `PP_0615` | PP_0615 | Q88Q80 | kegg:ppu02024 | PRESENT | CURATED | PRESENT | Branched-chain amino acid ABC transporter, ATP-binding protein |
| [x] | `PP_0616` | PP_0616 | Q88Q79 | kegg:ppu02024 | PRESENT | CURATED | PRESENT | Branched-chain amino acid ABC transporter, ATP binding protein |
| [x] | `PP_0617` | PP_0617 | Q88Q78 | kegg:ppu02024 | PRESENT | CURATED | PRESENT | Branched-chain amino acid ABC transporter, permease protein |
| [x] | `PP_0618` | PP_0618 | Q88Q77 | kegg:ppu02024 | PRESENT | CURATED | PRESENT | Branched-chain amino acid ABC transporter, permease protein |
| [x] | `PP_0619` | PP_0619 | Q88Q76 | kegg:ppu02024 | PRESENT | CURATED | PRESENT | Branched-chain amino acid ABC transporter, periplasmic amino acid-binding protein |
| [ ] | `PP_0806` | PP_0806 | Q88PP2 | kegg:ppu02024 | MISSING | MISSING | MISSING | Surface adhesion protein |
| [x] | `livF-I` | PP_1137 | Q88NR8 | kegg:ppu02024 | PRESENT | CURATED | PRESENT | High-affinity branched-chain amino acid transport ATP-binding protein |
| [x] | `livG` | PP_1138 | Q88NR7 | kegg:ppu02024 | PRESENT | CURATED | PRESENT | Branched chain amino acid transporter-ATP binding subunit |
| [x] | `livM` | PP_1139 | Q88NR6 | kegg:ppu02024 | PRESENT | CURATED | PRESENT | Branched chain amino acid transporter-permease subunit |
| [x] | `livH` | PP_1140 | Q88NR5 | kegg:ppu02024 | PRESENT | CURATED | PRESENT | Branched chain amino acid transporter-permease subunit |
| [x] | `livK` | PP_1141 | Q88NR4 | kegg:ppu02024 | PRESENT | CURATED | PRESENT | Branched-chain amino acids ABC transporter-periplasmic leucine binding subunit |
| [ ] | `ydcV` | PP_1482 | Q88MT6 | kegg:ppu02024 | MISSING | MISSING | MISSING | Polyamine ABC transporter, permease protein |
| [ ] | `ydcU` | PP_1483 | Q88MT5 | kegg:ppu02024 | MISSING | MISSING | MISSING | Polyamine ABC transporter, permease protein |
| [ ] | `ydcT` | PP_1484 | Q88MT4 | kegg:ppu02024 | MISSING | MISSING | MISSING | Predicted polyamine ABC transporter, ATP-binding protein (EC 3.6.3.31) |
| [ ] | `ydcS` | PP_1486 | Q88MT2 | kegg:ppu02024 | MISSING | MISSING | MISSING | Polyamine ABC transporter, periplasmic polyamine-binding protein |
| [ ] | `PP_1722` | PP_1722 | Q88M52 | kegg:ppu02024 | MISSING | MISSING | MISSING | ABC transporter, ATP-binding protein |
| [ ] | `PP_1723` | PP_1723 | Q88M51 | kegg:ppu02024 | MISSING | MISSING | MISSING | 2-aminoethylphosphonate transport system permease |
| [ ] | `PP_1724` | PP_1724 | Q88M50 | kegg:ppu02024 | MISSING | MISSING | MISSING | ABC-type 2-aminoethylphosphonate transporter permease |
| [ ] | `PP_1726` | PP_1726 | Q88M48 | kegg:ppu02024 | MISSING | MISSING | MISSING | ABC transporter, periplasmic binding protein |
| [ ] | `PP_2064` | PP_2064 | Q88L71 | kegg:ppu02024 | MISSING | MISSING | MISSING | Multidrug efflux RND membrane fusion protein |
| [ ] | `PP_2065` | PP_2065 | Q88L70 | kegg:ppu02024 | MISSING | MISSING | MISSING | Multidrug efflux RND transporter |
| [ ] | `PP_2713` | PP_2713 | Q88JD6 | kegg:ppu02024 | MISSING | MISSING | MISSING | DNA-binding response regulator |
| [ ] | `PP_2714` | PP_2714 | Q88JD5 | kegg:ppu02024 | MISSING | MISSING | MISSING | histidine kinase (EC 2.7.13.3) |
| [x] | `PP_2748` | PP_2748 | Q88JA1 | kegg:ppu02024 | PRESENT | CURATED | PRESENT | Branched-chain amino acid ABC transporter, ATP-binding protein |
| [x] | `PP_2749` | PP_2749 | Q88JA0 | kegg:ppu02024 | PRESENT | CURATED | PRESENT | Branched-chain amino acid ABC transporter, permease protein |
| [x] | `PP_2750` | PP_2750 | Q88J99 | kegg:ppu02024 | PRESENT | CURATED | PRESENT | Branched-chain amino acid ABC transporter, permease protein |
| [x] | `PP_2751` | PP_2751 | Q88J98 | kegg:ppu02024 | PRESENT | CURATED | PRESENT | Leucine-binding protein domain-containing protein |
| [x] | `PP_2752` | PP_2752 | Q88J97 | kegg:ppu02024 | PRESENT | CURATED | PRESENT | Leucine-binding protein domain-containing protein |
| [x] | `PP_2753` | PP_2753 | Q88J96 | kegg:ppu02024 | PRESENT | CURATED | PRESENT | Branched-chain amino acid ABC transporter, ATP-binding protein |
| [x] | `PP_2767` | PP_2767 | Q88J82 | kegg:ppu02024 | PRESENT | CURATED | PRESENT | Branched-chain amino acid ABC transporter, ATP-binding protein |
| [x] | `PP_2768` | PP_2768 | Q88J81 | kegg:ppu02024 | PRESENT | CURATED | PRESENT | Branched-chain amino acid ABC transporter, permease protein |
| [x] | `PP_2769` | PP_2769 | Q88J80 | kegg:ppu02024 | PRESENT | CURATED | PRESENT | Branched-chain amino acid ABC transporter, permease protein |
| [x] | `PP_2770` | PP_2770 | Q88J79 | kegg:ppu02024 | PRESENT | CURATED | PRESENT | Leucine-binding protein domain-containing protein |
| [ ] | `PP_2870` | PP_2870 | Q88IX9 | kegg:ppu02024 | MISSING | MISSING | MISSING | Spermidine/putrescine-binding periplasmic protein |
| [ ] | `PP_3220` | PP_3220 | Q88HY3 | kegg:ppu02024 | MISSING | MISSING | MISSING | ABC-type dipeptide transporter (EC 7.4.2.9) |
| [ ] | `PP_3221` | PP_3221 | Q88HY2 | kegg:ppu02024 | MISSING | MISSING | MISSING | ABC transporter, permease protein |
| [ ] | `PP_3222` | PP_3222 | Q88HY1 | kegg:ppu02024 | MISSING | MISSING | MISSING | ABC transporter, permease protein |
| [ ] | `PP_3223` | PP_3223 | Q88HY0 | kegg:ppu02024 | MISSING | MISSING | MISSING | ABC transporter, periplasmic binding protein |
| [ ] | `PP_3609` | PP_3609 | Q88GV8 | kegg:ppu02024 | MISSING | MISSING | MISSING | DMT family transporter |
| [ ] | `PP_3814` | PP_3814 | Q88GB0 | kegg:ppu02024 | MISSING | MISSING | MISSING | Polyamine ABC transporter, periplasmic polyamine-binding protein |
| [ ] | `PP_3815` | PP_3815 | Q88GA9 | kegg:ppu02024 | MISSING | MISSING | MISSING | Polyamine ABC transporter, permease protein |
| [ ] | `PP_3816` | PP_3816 | Q88GA8 | kegg:ppu02024 | MISSING | MISSING | MISSING | Polyamine ABC transporter, permease protein |
| [ ] | `PP_3817` | PP_3817 | Q88GA7 | kegg:ppu02024 | MISSING | MISSING | MISSING | Polyamine ABC transporter, ATP-binding protein |
| [ ] | `kdpE` | PP_4157 | Q88FE0 | kegg:ppu02024 | MISSING | MISSING | MISSING | Two-component system DNA-binding response activator KdpE |
| [ ] | `PP_4224` | PP_4224 | Q88F74 | kegg:ppu02024 | MISSING | MISSING | MISSING | histidine kinase (EC 2.7.13.3) |
| [ ] | `qseB` | PP_4225 | Q88F73 | kegg:ppu02024 | MISSING | MISSING | MISSING | Two component system DNA-binding transcriptional activator QseB |
| [ ] | `gsiA` | PP_4453 | Q88EK9 | kegg:ppu02024 | MISSING | MISSING | MISSING | Glutathione import ATP-binding protein GsiA (EC 7.4.2.10) (EC 7.4.2.9) |
| [ ] | `PP_4454` | PP_4454 | Q88EK8 | kegg:ppu02024 | MISSING | MISSING | MISSING | Opine ABC transporter, permease protein |
| [ ] | `gsiC` | PP_4455 | Q88EK7 | kegg:ppu02024 | MISSING | MISSING | MISSING | Glutathione ABC transporter permease subunit |
| [ ] | `PP_4458` | PP_4458 | Q88EK4 | kegg:ppu02024 | MISSING | MISSING | MISSING | Opine ABC transporter, periplasmic binding protein |
| [x] | `livF-II` | PP_4863 | Q88DG2 | kegg:ppu02024 | PRESENT | CURATED | PRESENT | High-affinity branched-chain amino acid transport ATP-binding protein |
| [x] | `braF` | PP_4864 | Q88DG1 | kegg:ppu02024 | PRESENT | CURATED | PRESENT | High-affinity branched-chain amino acid transport ATP-binding protein BraF |
| [x] | `braE` | PP_4865 | Q88DG0 | kegg:ppu02024 | PRESENT | CURATED | PRESENT | High-affinity branched-chain amino acid transport system permease protein BraE |
| [x] | `braD` | PP_4866 | Q88DF9 | kegg:ppu02024 | PRESENT | CURATED | PRESENT | High-affinity branched-chain amino acid transport system permease protein BraD |
| [x] | `PP_4867` | PP_4867 | Q88DF8 | kegg:ppu02024 | PRESENT | CURATED | PRESENT | Branched-chain amino acid ABC transporter, periplasmic amino acid-binding protein (BraC-like) |

## Notes

Generated UTC: 2026-07-09T12:11:26.653908+00:00

2026-07-11 PDT status sync: created and validated
`modules/quorum_sensing_boundary.yaml` as the ppu02024 parent boundary module.
The module records ppu02024 as a partitioned KEGG umbrella map, not as one
satisfiable LuxI/LuxR quorum-sensing pathway. The original boundary TSV and
candidate table above still lag at 25/60 present review/Asta rows, but the
current partition TSV records 60/60 genes as present, curated, and Asta-backed
across the nine sub-batches listed in
`projects/P_PUTIDA/batches/ppu02024_quorum_sensing_partition.md`.

Module validation passed with both module validators. The existing workflow
already records gene-review validation as complete through the partition
sub-batches.

Real Falcon commands were run:

```bash
just module-deep-research-falcon quorum_sensing_boundary
just module-pathway-deep-research-falcon quorum_sensing_boundary ppu02024 PSEPK
```

Both failed at Edison task creation with HTTP 402 Payment Required, so no
Falcon reports were written. The taxon-aware wrapper resolved the pathway
context as 60 primary genes and 84 total local members. Expected output paths
remain:

- `modules/quorum_sensing_boundary-deep-research-falcon.md`
- `projects/P_PUTIDA/deep-research/PSEPK__quorum_sensing_boundary__ppu02024-deep-research-falcon.md`

2026-07-09 PDT checkpoint: this 60-gene primary-only table is a partitioning
input, not a curation-complete batch. KEGG `ppu02024` has 84 total specific
members and, in PSEPK, the primary set is dominated by transporters and
regulatory side nodes rather than a single LuxI/LuxR quorum-sensing pathway.

The current partition is tracked in:

- `projects/P_PUTIDA/batches/ppu02024_quorum_sensing_partition.tsv`
- `projects/P_PUTIDA/batches/ppu02024_quorum_sensing_partition.md`

Next curation should select one partition bucket, such as QseBC-like
two-component regulation, polyamine ABC import, or peptide/opine/glutathione
ABC import, rather than fetching and curating all 60 genes as one PR.
