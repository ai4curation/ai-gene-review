---
title: "PSEPK UPA00094 UniPathway UPA00094 batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK UPA00094: UniPathway UPA00094

- Module seed: `fatty_acid_biosynthesis`
- Candidate genes from membership table: 8
- Primary bucket genes: 1
- Existing review files: 8
- Curated review files: 8
- Existing Asta research files: 8

## Required Workflow

- [x] Curate or update the species-neutral module.
- [x] Run module-level Falcon deep research.
- [ ] Run module + pathway + PSEPK Falcon deep research. Attempted before 2026-07-11 status normalization; blocked by Edison HTTP 402 before report generation.
- [x] Fetch all selected genes with `just fetch-gene PSEPK <gene>`.
- [x] Run Asta deep research for selected genes.
- [x] Curate each selected gene review.
- [x] Validate module and gene reviews.
- [ ] Open one PR for this module/pathway.
- [ ] Shepherd PR through review, CI, and merge readiness.

## Candidate Genes

| Done | Gene | Locus | UniProt | Primary bucket | Existing review | Curation | Asta research | Protein |
|---|---|---|---|---|---|---|---|---|
| [x] | `accB` | PP_0559 | Q88QD5 | kegg:ppu00061 | PRESENT | CURATED | PRESENT | Biotin carboxyl carrier protein of acetyl-CoA carboxylase |
| [x] | `fabG` | PP_1914 | Q88LL6 | kegg:ppu00780 | PRESENT | CURATED | PRESENT | 3-oxoacyl-[acyl-carrier-protein] reductase (EC 1.1.1.100) |
| [x] | `acpP` | PP_1915 | Q88LL5 | unipathway:UPA00094 | PRESENT | CURATED | PRESENT | Acyl carrier protein (ACP) |
| [x] | `fabF` | PP_1916 | Q88LL4 | kegg:ppu00780 | PRESENT | CURATED | PRESENT | 3-oxoacyl-[acyl-carrier-protein] synthase 2 (EC 2.3.1.179) |
| [x] | `PP_3303` | PP_3303 | Q88HQ0 | kegg:ppu00780 | PRESENT | CURATED | PRESENT | 3-oxoacyl-[acyl-carrier-protein] synthase 2 (EC 2.3.1.179) |
| [x] | `fabA` | PP_4174 | Q88FC4 | kegg:ppu00061 | PRESENT | CURATED | PRESENT | 3-hydroxydecanoyl-[acyl-carrier-protein] dehydratase (EC 4.2.1.59) (3-hydroxyacyl-[acyl-carrier-protein] dehydratase Fab |
| [x] | `fabB` | PP_4175 | Q88FC3 | kegg:ppu00780 | PRESENT | CURATED | PRESENT | 3-oxoacyl-[acyl-carrier-protein] synthase 1 (EC 2.3.1.41) (3-oxoacyl-[acyl-carrier-protein] synthase I) (Beta-ketoacyl-A |
| [x] | `fabV` | PP_4635 | Q88E33 | kegg:ppu00061 | PRESENT | CURATED | PRESENT | Enoyl-[acyl-carrier-protein] reductase [NADH] (ENR) (EC 1.3.1.9) |

## Notes

Generated UTC: 2026-07-10T02:18:59.647953+00:00

Session update:

- UPA00094 is treated as an ACP-linked support view inside the existing `fatty_acid_biosynthesis` module, not as a separate module.
- `acpP` was fetched, Asta-retrieved, curated, and validated; the other seven UPA00094 members already had curated reviews and Asta files.
- `modules/fatty_acid_biosynthesis.yaml` now records `UniPathway:UPA00094` evidence and an explicit `acpP`/Q88LL5 acyl-carrier annoton.
- The existing generic Falcon module report is reused: `modules/fatty_acid_biosynthesis-deep-research-falcon.md`.
- The real pathway-specific Falcon command was run for `fatty_acid_biosynthesis UPA00094 PSEPK`; Edison returned `402 Payment Required`, so no `projects/P_PUTIDA/deep-research/PSEPK__fatty_acid_biosynthesis__upa00094-deep-research-falcon.md` report was produced.
- Module validation and `just validate PSEPK acpP` pass.
