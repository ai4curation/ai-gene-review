---
title: "PSEPK ppu00780 Biotin metabolism batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK ppu00780: Biotin metabolism

- Module seed: `biotin_metabolism_boundary`
- Candidate genes from membership table: 16
- Primary bucket genes: 16
- Existing review files: 16
- Curated review files: 16
- Existing Asta research files: 16

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
| [x] | `bioB` | PP_0362 | Q88QX2 | kegg:ppu00780 | PRESENT | CURATED | PRESENT | Biotin synthase (EC 2.8.1.6) |
| [x] | `bioF` | PP_0363 | Q88QX1 | kegg:ppu00780 | PRESENT | CURATED | PRESENT | 8-amino-7-oxononanoate synthase (AONS) (EC 2.3.1.47) (7-keto-8-amino-pelargonic acid synthase) (7-KAP synthase) (KAPA sy |
| [x] | `bioH` | PP_0364 | Q88QX0 | kegg:ppu00780 | PRESENT | CURATED | PRESENT | Pimeloyl-[acp] methyl ester esterase (EC 3.1.1.1, EC 3.1.1.85) |
| [x] | `bioC` | PP_0365 | Q88QW9 | kegg:ppu00780 | PRESENT | CURATED | PRESENT | Malonyl-[acyl-carrier protein] O-methyltransferase (Malonyl-ACP O-methyltransferase) (EC 2.1.1.197) (Biotin synthesis pr |
| [x] | `bioD` | PP_0366 | Q88QW8 | kegg:ppu00780 | PRESENT | CURATED | PRESENT | ATP-dependent dethiobiotin synthetase BioD (EC 6.3.3.3) (DTB synthetase) (DTBS) (Dethiobiotin synthase) |
| [x] | `birA` | PP_0437 | Q88QQ1 | kegg:ppu00780 | PRESENT | CURATED | PRESENT | Bifunctional ligase/repressor BirA (Biotin operon repressor) (Biotin--[acetyl-CoA-carboxylase] ligase) (EC 6.3.4.15) (Bi |
| [x] | `PP_0581` | PP_0581 | Q88QB3 | kegg:ppu00780 | PRESENT | CURATED | PRESENT | 3-oxoacyl-(Acyl-carrier-protein) reductase |
| [x] | `fabZ` | PP_1602 | Q88MG9 | kegg:ppu00780 | PRESENT | CURATED | PRESENT | 3-hydroxyacyl-[acyl-carrier-protein] dehydratase FabZ (EC 4.2.1.59) ((3R)-hydroxymyristoyl-[acyl-carrier-protein] dehydr |
| [x] | `PP_1852` | PP_1852 | Q88LS6 | kegg:ppu00780 | PRESENT | CURATED | PRESENT | Enoyl-[acyl-carrier-protein] reductase (NADPH, B-specific) (EC 1.3.1.10) |
| [x] | `fabG` | PP_1914 | Q88LL6 | kegg:ppu00780 | PRESENT | CURATED | PRESENT | 3-oxoacyl-[acyl-carrier-protein] reductase (EC 1.1.1.100) |
| [x] | `fabF` | PP_1916 | Q88LL4 | kegg:ppu00780 | PRESENT | CURATED | PRESENT | 3-oxoacyl-[acyl-carrier-protein] synthase 2 (EC 2.3.1.179) |
| [x] | `PP_2540` | PP_2540 | Q88JV7 | kegg:ppu00780 | PRESENT | CURATED | PRESENT | Oxidoreductase, short-chain dehydrogenase/reductase family |
| [x] | `PP_2783` | PP_2783 | Q88J66 | kegg:ppu00780 | PRESENT | CURATED | PRESENT | 2,3-dihydroxy-2,3-dihydro-p-cumate dehydrogenase (EC 1.3.1.58) (Biphenyl-2,3-dihydro-2,3-diol dehydrogenase) |
| [x] | `PP_3303` | PP_3303 | Q88HQ0 | kegg:ppu00780 | PRESENT | CURATED | PRESENT | 3-oxoacyl-[acyl-carrier-protein] synthase 2 (EC 2.3.1.179) |
| [x] | `fabB` | PP_4175 | Q88FC3 | kegg:ppu00780 | PRESENT | CURATED | PRESENT | 3-oxoacyl-[acyl-carrier-protein] synthase 1 (EC 2.3.1.41) (3-oxoacyl-[acyl-carrier-protein] synthase I) (Beta-ketoacyl-A |
| [x] | `bioA` | PP_4984 | Q88D44 | kegg:ppu00780 | PRESENT | CURATED | PRESENT | Adenosylmethionine-8-amino-7-oxononanoate aminotransferase (EC 2.6.1.62) (7,8-diamino-pelargonic acid aminotransferase)  |

## Notes

Generated UTC: 2026-07-08T15:04:55.693035+00:00

## Workflow Notes

- 2026-07-11 status sync: ran `just module-deep-research-falcon biotin_metabolism_boundary`
  and `just module-pathway-deep-research-falcon biotin_metabolism_boundary ppu00780 PSEPK`.
  Both Edison task creation attempts failed immediately with HTTP 402 Payment Required, so the
  Falcon workflow boxes remain unchecked and no Falcon report files were written. Expected output
  paths remain `modules/biotin_metabolism_boundary-deep-research-falcon.md`
  and `projects/P_PUTIDA/deep-research/PSEPK__biotin_metabolism_boundary__ppu00780-deep-research-falcon.md`.
