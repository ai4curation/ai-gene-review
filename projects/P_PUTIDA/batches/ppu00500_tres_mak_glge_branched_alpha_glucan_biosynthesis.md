---
title: "PSEPK ppu00500 TreS-Mak-GlgE alpha-glucan batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK ppu00500: TreS-Mak-GlgE branched alpha-glucan biosynthesis

- Module seed: `tres_mak_glge_branched_alpha_glucan_biosynthesis`
- Candidate genes from membership table: 18
- Primary bucket genes: 12
- Existing review files: 12
- Curated review files: 12
- Selected module genes: 3
- Selected gene reviews curated: 3
- Selected OpenScientist reports: 3 of 3 complete

## Curated Boundary

- Required pathway proteins: bifunctional `treSB`, `glgE`, and `glgB`.
- TreSB supplies two consecutive activities: trehalose-to-maltose isomerization
  and ATP-dependent maltose phosphorylation.
- GlgE extends alpha-glucan with maltose 1-phosphate; GlgB introduces branch
  linkages.
- Trehalose synthesis, glycogen breakdown, and the classical ADP-glucose GlgA
  route are outside this module.

## Required Workflow

- [x] Curate or update the species-neutral module.
- [ ] Run module-level OpenScientist deep research.
- [x] Run module + pathway + PSEPK OpenScientist deep research.
- [x] Fetch all selected genes with `just fetch-gene PSEPK <gene>`.
- [x] Run OpenScientist deep research for selected genes.
- [x] Curate each selected gene review.
- [x] Validate module and gene reviews.
- [x] Review the merged baseline from [#2326](https://github.com/ai4curation/ai-gene-review/pull/2326).
- [ ] Open one repair PR for this module/pathway.
- [ ] Shepherd PR through review, CI, and merge readiness.

## Annotation-Reviewer Audit

The annotation-reviewer protocol was applied separately to every selected
gene against the current GOA, UniProt record, literature, and family evidence:

- `treSB`: all 3 seeded GOA rows reviewed; 2 missing activity/pathway
  annotations retained as `NEW`; no `PENDING` actions.
- `glgE`: all 5 seeded GOA rows reviewed; the GH13 hydrolase over-propagation
  remains `REMOVE`; no `PENDING` actions.
- `glgB`: all 9 seeded GOA rows reviewed; the GH13 hydrolase over-propagation
  remains `REMOVE` and unsupported cation binding remains `UNDECIDED`; no
  `PENDING` actions.

2026-09-01: The module + pathway + PSEPK OpenScientist run completed in
1156.91 seconds and produced a report plus HTML/PDF artifacts. Its assignment
of `treSB`, `glgE`, and `glgB` to the four-step pathway agrees with the curated
module. Claims that the pathway is primary or sole, that `glgC` is absent, and
that the three genes form an operon were not promoted because the report did
not provide sufficient target-specific evidence for those stronger claims.

2026-09-01: Two generic module-level OpenScientist attempts were allowed to
run to provider failure (3439.86 and 1120.16 seconds). Both ended with a DNS
resolution `ConnectError` and produced no report. The successful combined
module/pathway/taxon report supplies the module-level research artifact.

2026-09-01: OpenScientist reports are complete for `glgE` (5283.11 seconds),
`glgB` (1461.43 seconds), and `treSB` (1025.98 provider seconds; 1028.84 wall
seconds). Two earlier `treSB` attempts were allowed to run to provider failure
(3234.92 and 1118.35 seconds); both ended with the same DNS resolution error.

## Candidate Genes

| Done | Gene | Locus | UniProt | Primary bucket | Existing review | Curation | OpenScientist research | Protein |
|---|---|---|---|---|---|---|---|---|
| [ ] | `glk` | PP_1011 | Q88P42 | kegg:ppu00052 | PRESENT | CURATED | MISSING | Glucokinase (EC 2.7.1.2) (Glucose kinase) |
| [ ] | `bglX` | PP_1403 | Q88N13 | kegg:ppu00999 | MISSING | MISSING | MISSING | Periplasmic beta-glucosidase (EC 3.2.1.21) (Beta-D-glucoside glucohydrolase) (Cellobiase) (Gentiobiase) |
| [ ] | `cpsG` | PP_1777 | Q88LZ9 | kegg:ppu00052 | PRESENT | CURATED | MISSING | phosphomannomutase (EC 5.4.2.8) |
| [ ] | `pgi1` | PP_1808 | Q88LW9 | kegg:ppu00500 | PRESENT | CURATED | MISSING | Glucose-6-phosphate isomerase 1 (GPI 1) (EC 5.3.1.9) (Phosphoglucose isomerase 1) (PGI 1) (Phosphohexose isomerase 1) (P |
| [ ] | `bcsA` | PP_2635 | Q88JL4 | kegg:ppu00500 | PRESENT | CURATED | PRESENT | Cellulose synthase catalytic subunit [UDP-forming] (EC 2.4.1.12) |
| [ ] | `pgm` | PP_3578 | Q88GY7 | kegg:ppu00052 | PRESENT | CURATED | MISSING | Phosphoglucomutase (EC 5.4.2.2) |
| [ ] | `galU` | PP_3821 | Q88GA4 | kegg:ppu00040 | MISSING | MISSING | MISSING | UTP--glucose-1-phosphate uridylyltransferase (EC 2.7.7.9) (UDP-glucose pyrophosphorylase) |
| [ ] | `glgA` | PP_4050 | Q88FN9 | kegg:ppu00500 | MISSING | MISSING | MISSING | Glycogen synthase (EC 2.4.1.21) (Starch [bacterial glycogen] synthase) |
| [ ] | `treZ` | PP_4051 | Q88FN8 | kegg:ppu00500 | PRESENT | CURATED | MISSING | Malto-oligosyltrehalose trehalohydrolase (MTHase) (EC 3.2.1.141) (4-alpha-D-((1->4)-alpha-D-glucano)trehalose trehalohyd |
| [ ] | `malQ` | PP_4052 | Q88FN7 | kegg:ppu00500 | MISSING | MISSING | MISSING | 4-alpha-glucanotransferase (EC 2.4.1.25) (Amylomaltase) (Disproportionating enzyme) |
| [ ] | `treY` | PP_4053 | Q88FN6 | kegg:ppu00500 | PRESENT | CURATED | MISSING | Maltooligosyl trehalose synthase (EC 5.4.99.15) |
| [ ] | `glgX` | PP_4055 | Q88FN4 | kegg:ppu00500 | MISSING | MISSING | MISSING | Glycogen debranching enzyme (EC 3.2.1.33) |
| [x] | `glgB` | PP_4058 | Q88FN1 | kegg:ppu00500 | PRESENT | CURATED | PRESENT | 1,4-alpha-glucan branching enzyme GlgB (EC 2.4.1.18) (1,4-alpha-D-glucan:1,4-alpha-D-glucan 6-glucosyl-transferase) (Alp |
| [x] | `treSB` | PP_4059 | Q88FN0 | kegg:ppu00500 | PRESENT | CURATED | PRESENT | Maltokinase (EC 2.7.1.175) (EC 5.4.99.16) (Maltose alpha-D-glucosyltransferase) (Maltose-1-phosphate synthase) |
| [x] | `glgE` | PP_4060 | Q88FM9 | kegg:ppu00500 | PRESENT | CURATED | PRESENT | Alpha-1,4-glucan:maltose-1-phosphate maltosyltransferase (GMPMT) (EC 2.4.99.16) ((1->4)-alpha-D-glucan:maltose-1-phospha |
| [ ] | `pgi2` | PP_4701 | Q88DW7 | kegg:ppu00500 | PRESENT | CURATED | MISSING | Glucose-6-phosphate isomerase 2 (GPI 2) (EC 5.3.1.9) (Phosphoglucose isomerase 2) (PGI 2) (Phosphohexose isomerase 2) (P |
| [ ] | `glgP` | PP_5041 | Q88CY8 | kegg:ppu00500 | MISSING | MISSING | MISSING | Alpha-1,4 glucan phosphorylase (EC 2.4.1.1) |
| [ ] | `algC` | PP_5288 | Q88C93 | kegg:ppu00052 | PRESENT | CURATED | MISSING | Phosphomannomutase/phosphoglucomutase (PMM / PGM) (EC 5.4.2.2) (EC 5.4.2.8) |

## Notes

The three checked proteins implement four ordered reaction roles because TreSB
contains both the trehalose synthase and maltokinase activities. Cellulose,
classical glycogen synthesis, trehalose synthesis, and glucan breakdown remain
outside this module.

Updated: 2026-09-01
