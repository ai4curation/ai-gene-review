---
title: "PSEPK ppu00552 Teichoic acid biosynthesis batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK ppu00552: Teichoic acid biosynthesis

- Module seed: `teichoic_acid_biosynthesis_boundary`
- Candidate genes from membership table: 2
- Primary bucket genes: 2
- Existing review files: 2
- Curated review files: 2
- Existing Asta research files: 2

## Required Workflow

- [x] Curate or update the species-neutral module.
- [ ] Run module-level Falcon deep research. Attempted on 2026-07-11; blocked by Edison HTTP 402 before report generation.
- [ ] Run module + pathway + PSEPK Falcon deep research. Attempted on 2026-07-11; blocked by Edison HTTP 402 before report generation.
- [x] Fetch all selected genes with `just fetch-gene PSEPK <gene>`.
- [x] Run Asta deep research for selected genes.
- [x] Curate each selected gene review.
- [x] Validate module and gene reviews.
- [ ] Open one PR for this module/pathway.
- [ ] Shepherd PR through review, CI, and merge readiness.

## Candidate Genes

| Done | Gene | Locus | UniProt | Primary bucket | Existing review | Curation | Asta research | Protein |
|---|---|---|---|---|---|---|---|---|
| [x] | `wbpM` | PP_1805 | Q88LX2 | kegg:ppu00552 | PRESENT | CURATED | PRESENT | Polysaccharide biosynthesis protein |
| [x] | `uppP` | PP_2862 | Q88IY7 | kegg:ppu00552 | PRESENT | CURATED | PRESENT | Undecaprenyl-diphosphatase (EC 3.6.1.27) (Bacitracin resistance protein) (Undecaprenyl pyrophosphate phosphatase) |

## Notes

Generated UTC: 2026-07-08T10:20:22.006615+00:00

Completed first-pass curation on 2026-07-08 UTC.

Main conclusions:

- PSEPK `ppu00552` is a boundary/absence batch, not evidence for a complete
  Gram-positive teichoic-acid biosynthesis route in KT2440.
- The two KEGG members are `wbpM`, an unresolved
  polysaccharide-biosynthesis/CapD-like membrane protein with no specific
  molecular-function GOA row, and `uppP`, the shared
  undecaprenyl-diphosphatase/BacA carrier-recycling enzyme.
- `uppP` should be interpreted as shared cell-envelope lipid-carrier recycling
  and peptidoglycan precursor context, not as teichoic-acid-specific pathway
  evidence.
- `wbpM` remains deliberately unresolved with no core function until substrate
  or pathway-specific evidence is available.

## Workflow Notes

- 2026-07-11 status sync: ran `just module-deep-research-falcon teichoic_acid_biosynthesis_boundary`
  and `just module-pathway-deep-research-falcon teichoic_acid_biosynthesis_boundary ppu00552 PSEPK`.
  Both Edison task creation attempts failed immediately with HTTP 402 Payment Required, so
  the Falcon workflow boxes remain unchecked and no Falcon report files were written. Expected
  output paths remain `modules/teichoic_acid_biosynthesis_boundary-deep-research-falcon.md`
  and `projects/P_PUTIDA/deep-research/PSEPK__teichoic_acid_biosynthesis_boundary__ppu00552-deep-research-falcon.md`.
