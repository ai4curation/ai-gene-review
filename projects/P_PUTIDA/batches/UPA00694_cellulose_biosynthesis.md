---
title: "PSEPK UPA00694 cellulose biosynthesis batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK UPA00694: Cellulose biosynthesis

- Module seed: `bacterial_cellulose_biosynthesis`
- Pull request: https://github.com/ai4curation/ai-gene-review/pull/2143
- Candidate genes from membership table: 3
- Accessory/name-correction genes added during curation: 1
- Primary bucket genes: 2
- Existing review files: 0
- Curated review files: 4
- Existing OpenScientist research files: 4 gene-level; 2 module/pathway-level

## Required Workflow

- [x] Curate or update the species-neutral module.
- [x] Run module-level OpenScientist deep research.
- [x] Run module + pathway + PSEPK OpenScientist deep research.
- [x] Fetch all selected genes with `just fetch-gene PSEPK <gene>`.
- [x] Run OpenScientist deep research for selected genes.
- [x] Curate each selected gene review.
- [x] Validate module and gene reviews.
- [x] Open one PR for this module/pathway.
- [ ] Shepherd PR through review, CI, and merge readiness.

## Candidate Genes

| Done | Gene | Locus | UniProt | Primary bucket | Existing review | Curation | OpenScientist research | Protein |
|---|---|---|---|---|---|---|---|---|
| [x] | `bcsA` | PP_2635 | Q88JL4 | kegg:ppu00500 | MISSING | CURATED | PRESENT | Cellulose synthase catalytic subunit [UDP-forming] (EC 2.4.1.12) |
| [x] | `bcsB` | PP_2636 | Q88JL3 | unipathway:UPA00694 | MISSING | CURATED | PRESENT | Cyclic di-GMP-binding protein (Cellulose synthase regulatory subunit) |
| [x] | `PP_2638` | PP_2638 | Q88JL1 | unipathway:UPA00694 | MISSING | CURATED | PRESENT | Cellulose synthase operon C protein |
| [x] | `PP_2634` | PP_2634 | Q88JL5 | accessory/name-correction | MISSING | CURATED | PRESENT | BcsQ/YhjQ-family P-loop NTPase; UniProt name is generic "Cellulose synthase" |

## Notes

Generated UTC: 2026-07-11T22:30:25.048526+00:00

OpenScientist pathway research found UPA00694 satisfiable in KT2440 once bcsA
is included explicitly. bcsA was initially assigned a different primary bucket
by the partition heuristic, but it is the catalytic UPA00694 BcsA subunit and
must stay in this module. PP_2634 was added as an accessory curation item because
its domain architecture identifies BcsQ/YhjQ rather than a second cellulose
synthase.

2026-07-15 refinement: revised the module from a KT2440-specific record into a
reusable Gram-negative BcsA/BcsB/BcsC cellulose synthase/export module with PSEPK
representative UniProt exemplars. Kept PP_2634 as BcsQ/YhjQ accessory context
and left broader bcs-locus hydrolase/editing factors for a later accessory-module
pass.
