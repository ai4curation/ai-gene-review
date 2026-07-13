---
title: "PSEPK ppu00660 C5-Branched dibasic acid metabolism batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK ppu00660: C5-Branched dibasic acid metabolism

- Module seed: `c5_branched_dibasic_acid_metabolism_boundary`
- Candidate genes from membership table: 10
- Primary bucket genes: 10
- Existing review files: 10
- Curated review files: 10
- Existing Asta research files: 10

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
| [x] | `PP_1157` | PP_1157 | Q877U6 | kegg:ppu00660 | PRESENT | CURATED | PRESENT | Acetolactate synthase |
| [x] | `PP_1394` | PP_1394 | Q88N22 | kegg:ppu00660 | PRESENT | CURATED | PRESENT | Acetolactate synthase, large subunit |
| [x] | `leuC` | PP_1985 | Q88LE8 | kegg:ppu00660 | PRESENT | CURATED | PRESENT | 3-isopropylmalate dehydratase large subunit (EC 4.2.1.33) (Alpha-IPM isomerase) (IPMI) (Isopropylmalate isomerase) |
| [x] | `leuD` | PP_1986 | Q88LE7 | kegg:ppu00660 | PRESENT | CURATED | PRESENT | 3-isopropylmalate dehydratase small subunit (EC 4.2.1.33) (Alpha-IPM isomerase) (IPMI) (Isopropylmalate isomerase) |
| [x] | `leuB` | PP_1988 | Q88LE5 | kegg:ppu00660 | PRESENT | CURATED | PRESENT | 3-isopropylmalate dehydrogenase (EC 1.1.1.85) (3-IPM-DH) (Beta-IPM dehydrogenase) (IMDH) |
| [x] | `galC` | PP_2514 | Q88JX9 | kegg:ppu00660 | PRESENT | CURATED | PRESENT | 4-carboxy-4-hydroxy-2-oxoadipic acid aldolase (CHA aldolase) (EC 4.1.3.17) (Gallate degradation protein C) |
| [x] | `sucD` | PP_4185 | Q88FB3 | kegg:ppu00660 | PRESENT | CURATED | PRESENT | Succinate--CoA ligase [ADP-forming] subunit alpha (EC 6.2.1.5) (Succinyl-CoA synthetase subunit alpha) (SCS-alpha) |
| [x] | `sucC` | PP_4186 | Q88FB2 | kegg:ppu00660 | PRESENT | CURATED | PRESENT | Succinate--CoA ligase [ADP-forming] subunit beta (EC 6.2.1.5) (Succinyl-CoA synthetase subunit beta) (SCS-beta) |
| [x] | `ilvH` | PP_4679 | Q88DY9 | kegg:ppu00660 | PRESENT | CURATED | PRESENT | Acetolactate synthase small subunit (AHAS) (ALS) (EC 2.2.1.6) (Acetohydroxy-acid synthase small subunit) |
| [x] | `ilvI` | PP_4680 | Q88DY8 | kegg:ppu00660 | PRESENT | CURATED | PRESENT | Acetolactate synthase (EC 2.2.1.6) |

## Notes

Generated UTC: 2026-07-08T14:17:23.417063+00:00

## Workflow Notes

- 2026-07-11 status sync: ran `just module-deep-research-falcon c5_branched_dibasic_acid_metabolism_boundary`
  and `just module-pathway-deep-research-falcon c5_branched_dibasic_acid_metabolism_boundary ppu00660 PSEPK`.
  Both Edison task creation attempts failed immediately with HTTP 402 Payment Required, so the
  Falcon workflow boxes remain unchecked and no Falcon report files were written. Expected output
  paths remain `modules/c5_branched_dibasic_acid_metabolism_boundary-deep-research-falcon.md`
  and `projects/P_PUTIDA/deep-research/PSEPK__c5_branched_dibasic_acid_metabolism_boundary__ppu00660-deep-research-falcon.md`.
