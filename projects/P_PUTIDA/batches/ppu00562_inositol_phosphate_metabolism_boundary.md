---
title: "PSEPK ppu00562 Inositol phosphate metabolism batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK ppu00562: Inositol phosphate metabolism

- Module seed: `inositol_phosphate_metabolism_boundary`
- Candidate genes from membership table: 4
- Primary bucket genes: 4
- Existing review files: 4
- Curated review files: 4
- Existing Asta research files: 4

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
| [x] | `mmsA-I` | PP_0597 | Q88Q97 | kegg:ppu00562 | PRESENT | CURATED | PRESENT | methylmalonate-semialdehyde dehydrogenase (CoA acylating) (EC 1.2.1.27) |
| [x] | `suhB` | PP_0838 | Q88PL2 | kegg:ppu00562 | PRESENT | CURATED | PRESENT | Inositol-1-monophosphatase (EC 3.1.3.25) |
| [x] | `mmsA-II` | PP_4667 | Q88E01 | kegg:ppu00562 | PRESENT | CURATED | PRESENT | methylmalonate-semialdehyde dehydrogenase (CoA acylating) (EC 1.2.1.27) |
| [x] | `tpiA` | PP_4715 | Q88DV4 | kegg:ppu00562 | PRESENT | CURATED | PRESENT | Triosephosphate isomerase (TIM) (TPI) (EC 5.3.1.1) (Triose-phosphate isomerase) |

## Notes

Generated UTC: 2026-07-08T10:55:30.256793+00:00

Completed first-pass curation on 2026-07-08 UTC.

Main conclusions:

- PSEPK `ppu00562` is a boundary/absence map, not evidence for a complete
  phosphatidylinositol or inositol-polyphosphate signalling pathway in KT2440.
- `suhB` is the only direct inositol-phosphate enzyme in the KEGG candidate
  set. Its review accepts EC 3.1.3.25 inositol-monophosphatase activity and
  adds a `NEW` transcription antitermination process lead from the UniProt
  rrnTAC function note.
- `suhB` signal-transduction context was marked over-annotated, and
  phosphatidylinositol dephosphorylation was removed as an over-propagated
  InterPro process annotation for this bacterial protein.
- `mmsA-I`, `mmsA-II`, and `tpiA` are side nodes from valine/thymine/propanoate
  metabolism and central carbon metabolism, not inositol-specific pathway
  enzymes.

## Workflow Notes

- 2026-07-11 status sync: ran `just module-deep-research-falcon inositol_phosphate_metabolism_boundary`
  and `just module-pathway-deep-research-falcon inositol_phosphate_metabolism_boundary ppu00562 PSEPK`.
  Both Edison task creation attempts failed immediately with HTTP 402 Payment Required, so
  the Falcon workflow boxes remain unchecked and no Falcon report files were written. Expected
  output paths remain `modules/inositol_phosphate_metabolism_boundary-deep-research-falcon.md`
  and `projects/P_PUTIDA/deep-research/PSEPK__inositol_phosphate_metabolism_boundary__ppu00562-deep-research-falcon.md`.
