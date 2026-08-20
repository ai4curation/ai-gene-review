---
title: "PSEPK bacterial glycogen synthesis and mobilization batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK ppu00500: bacterial glycogen synthesis and mobilization

- Module seed: `glycogen_synthesis_and_mobilization`
- Candidate genes from membership table: 18
- Primary bucket genes: 12
- Existing review files: 15
- Curated review files: 15
- Existing OpenScientist research files: 2
- Selected module genes: 5
- Selected gene reviews curated: 5

## Curated Boundary

- The connected reusable module has two substantive arms: canonical bacterial
  glycogen synthesis and later glycogen mobilization.
- Canonical glycogen synthesis uses GlgC/ADP-glucose-dependent GlgA followed by
  GlgB branch formation. The Pseudomonas GalU/UDP-glucose-dependent GlgA branch
  forms linear alpha-glucan but is not connected directly to GlgB here.
- Mobilization requires GlgP phosphorolysis and GlgX branch removal; glucose
  1-phosphate is the module output, so `pgm` is downstream context.
- Exact KT2440 exemplars are `galU` (Q88GA4), `glgA` (Q88FN9), `glgB`
  (Q88FN1), `glgP` (Q88CY8), and `glgX` (Q88FN4).
- No `glgC`/EC 2.7.7.27 candidate is present in the current KT2440 UniProt
  metadata. Experimental work in PAO1 supports UDP-glucose-dependent GlgA, but
  GalU is only a candidate source of that shared metabolite pool and Q88FN9
  donor specificity remains open.
- TreY-TreZ trehalose synthesis and TreS-Mak-GlgE alpha-glucan synthesis remain
  separate neighboring modules. Cellulose synthesis, glucose isomerization,
  and broad KEGG ppu00500 membership do not define this module.

## Required Workflow

- [x] Curate or update the species-neutral module.
- [x] Start module-level OpenScientist deep research with the full timeout.
- [x] Start module + pathway + PSEPK OpenScientist deep research with the full timeout.
- [x] Fetch all selected genes with `just fetch-gene PSEPK <gene>`.
- [x] Start OpenScientist deep research for the four newly fetched genes.
- [x] Curate each selected gene review.
- [x] Validate module and gene reviews.
- [x] Open one PR for this module/pathway.
- [ ] Shepherd PR through review, CI, and merge readiness.

## Candidate Genes

| Done | Gene | Locus | UniProt | Primary bucket | Existing review | Curation | OpenScientist research | Protein |
|---|---|---|---|---|---|---|---|---|
| [ ] | `glk` | PP_1011 | Q88P42 | kegg:ppu00052 | PRESENT | CURATED | MISSING | Glucokinase (EC 2.7.1.2) (Glucose kinase) |
| [ ] | `bglX` | PP_1403 | Q88N13 | kegg:ppu00999 | MISSING | MISSING | MISSING | Periplasmic beta-glucosidase (EC 3.2.1.21) (Beta-D-glucoside glucohydrolase) (Cellobiase) (Gentiobiase) |
| [ ] | `cpsG` | PP_1777 | Q88LZ9 | kegg:ppu00052 | PRESENT | CURATED | MISSING | phosphomannomutase (EC 5.4.2.8) |
| [ ] | `pgi1` | PP_1808 | Q88LW9 | kegg:ppu00500 | PRESENT | CURATED | MISSING | Glucose-6-phosphate isomerase 1 (GPI 1) (EC 5.3.1.9) (Phosphoglucose isomerase 1) (PGI 1) (Phosphohexose isomerase 1) (P |
| [ ] | `bcsA` | PP_2635 | Q88JL4 | kegg:ppu00500 | PRESENT | CURATED | PRESENT | Cellulose synthase catalytic subunit [UDP-forming] (EC 2.4.1.12) |
| [ ] | `pgm` | PP_3578 | Q88GY7 | kegg:ppu00052 | PRESENT | CURATED | MISSING | Phosphoglucomutase (EC 5.4.2.2) |
| [x] | `galU` | PP_3821 | Q88GA4 | kegg:ppu00040 | PRESENT | CURATED | RUNNING | UTP--glucose-1-phosphate uridylyltransferase (EC 2.7.7.9) (UDP-glucose pyrophosphorylase) |
| [x] | `glgA` | PP_4050 | Q88FN9 | kegg:ppu00500 | PRESENT | CURATED | RUNNING | Glycogen synthase (EC 2.4.1.21) (Starch [bacterial glycogen] synthase) |
| [ ] | `treZ` | PP_4051 | Q88FN8 | kegg:ppu00500 | PRESENT | CURATED | MISSING | Malto-oligosyltrehalose trehalohydrolase (MTHase) (EC 3.2.1.141) (4-alpha-D-((1->4)-alpha-D-glucano)trehalose trehalohyd |
| [ ] | `malQ` | PP_4052 | Q88FN7 | kegg:ppu00500 | MISSING | MISSING | MISSING | 4-alpha-glucanotransferase (EC 2.4.1.25) (Amylomaltase) (Disproportionating enzyme) |
| [ ] | `treY` | PP_4053 | Q88FN6 | kegg:ppu00500 | PRESENT | CURATED | MISSING | Maltooligosyl trehalose synthase (EC 5.4.99.15) |
| [x] | `glgX` | PP_4055 | Q88FN4 | kegg:ppu00500 | PRESENT | CURATED | RUNNING | Glycogen debranching enzyme (EC 3.2.1.33) |
| [x] | `glgB` | PP_4058 | Q88FN1 | kegg:ppu00500 | PRESENT | CURATED | RUNNING | 1,4-alpha-glucan branching enzyme GlgB (EC 2.4.1.18) (1,4-alpha-D-glucan:1,4-alpha-D-glucan 6-glucosyl-transferase) (Alp |
| [ ] | `treSB` | PP_4059 | Q88FN0 | kegg:ppu00500 | PRESENT | CURATED | MISSING | Maltokinase (EC 2.7.1.175) (EC 5.4.99.16) (Maltose alpha-D-glucosyltransferase) (Maltose-1-phosphate synthase) |
| [ ] | `glgE` | PP_4060 | Q88FM9 | kegg:ppu00500 | PRESENT | CURATED | PRESENT | Alpha-1,4-glucan:maltose-1-phosphate maltosyltransferase (GMPMT) (EC 2.4.99.16) ((1->4)-alpha-D-glucan:maltose-1-phospha |
| [ ] | `pgi2` | PP_4701 | Q88DW7 | kegg:ppu00500 | PRESENT | CURATED | MISSING | Glucose-6-phosphate isomerase 2 (GPI 2) (EC 5.3.1.9) (Phosphoglucose isomerase 2) (PGI 2) (Phosphohexose isomerase 2) (P |
| [x] | `glgP` | PP_5041 | Q88CY8 | kegg:ppu00500 | PRESENT | CURATED | RUNNING | Alpha-1,4 glucan phosphorylase (EC 2.4.1.1) |
| [ ] | `algC` | PP_5288 | Q88C93 | kegg:ppu00052 | PRESENT | CURATED | MISSING | Phosphomannomutase/phosphoglucomutase (PMM / PGM) (EC 5.4.2.2) (EC 5.4.2.8) |

## Notes

2026-08-11: Added one reusable connected bacterial turnover module alongside
the existing glycogen biosynthesis and glycogenolysis modules. Those existing
eukaryotic boundaries remain unchanged. The old #2049 Asta artifacts were
inspected as leads only; current UniProt, GOA, OpenScientist, and current-schema
validation remain authoritative.

2026-08-12: Full-timeout OpenScientist jobs were started for the four newly
fetched genes, the reusable module, and module + ppu00500 + PSEPK
satisfiability. They are allowed to run for the documented provider timeout.

2026-08-12: Annotation review corrected the Pseudomonas pathway boundary. The
module no longer asserts a GalU-GlgA-GlgB shortcut; GlgA-derived linear glucan
is treated as input to the neighboring TreY/TreZ and TreS-Mak-GlgE network.
