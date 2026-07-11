---
title: "PSEPK ppu00380 Tryptophan metabolism batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK ppu00380: Tryptophan metabolism

- Module seed: `tryptophan_metabolism_boundary`
- Candidate genes from membership table: 20
- Primary bucket genes: 2
- Existing review files: 20
- Curated review files: 20
- Existing Asta research files: 20

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
| [x] | `katE` | PP_0115 | Q88RL4 | kegg:ppu04146 | PRESENT | CURATED | PRESENT | Catalase (EC 1.11.1.6) |
| [x] | `gcdH` | PP_0158 | Q88RH2 | kegg:ppu00380 | PRESENT | CURATED | PRESENT | glutaryl-CoA dehydrogenase (ETF) (EC 1.3.8.6) |
| [x] | `katA` | PP_0481 | Q88QK9 | kegg:ppu04146 | PRESENT | CURATED | PRESENT | Catalase (EC 1.11.1.6) |
| [x] | `PP_0582` | PP_0582 | Q88QB2 | kegg:ppu00900 | PRESENT | CURATED | PRESENT | Thiolase family protein |
| [x] | `fadB` | PP_2136 | Q88L02 | kegg:ppu00930 | PRESENT | CURATED | PRESENT | Fatty acid oxidation complex subunit alpha [Includes: Enoyl-CoA hydratase/Delta(3)-cis-Delta(2)-trans-enoyl-CoA isomeras |
| [x] | `PP_2215` | PP_2215 | Q88KS4 | kegg:ppu00900 | PRESENT | CURATED | PRESENT | Acetyl-CoA acetyltransferase (EC 2.3.1.9) |
| [x] | `PP_2217` | PP_2217 | Q88KS2 | kegg:ppu00930 | PRESENT | CURATED | PRESENT | enoyl-CoA hydratase (EC 4.2.1.17) |
| [x] | `PP_2552` | PP_2552 | Q88JU5 | kegg:ppu00350 | PRESENT | CURATED | PRESENT | DOPA decarboxylase (EC 4.1.1.28) |
| [x] | `PP_2887` | PP_2887 | Q88IW2 | kegg:ppu04146 | PRESENT | CURATED | PRESENT | Catalase-related peroxidase (EC 1.11.1.-) |
| [x] | `PP_2932` | PP_2932 | Q88IR7 | kegg:ppu00643 | PRESENT | CURATED | PRESENT | Amidase family protein |
| [x] | `paaF` | PP_3284 | Q88HR9 | kegg:ppu00930 | PRESENT | CURATED | PRESENT | Enoyl-CoA hydratase-isomerase (EC 4.2.1.17) |
| [x] | `PP_3355` | PP_3355 | Q88HK1 | kegg:ppu00900 | PRESENT | CURATED | PRESENT | Beta-ketothiolase |
| [x] | `katG` | PP_3668 | Q88GQ0 | kegg:ppu00380 | PRESENT | CURATED | PRESENT | Catalase-peroxidase (CP) (EC 1.11.1.21) (Peroxidase/catalase) |
| [x] | `bktB` | PP_3754 | Q88GH0 | kegg:ppu00900 | PRESENT | CURATED | PRESENT | Beta-ketothiolase BktB (EC 2.3.1.16, EC 2.3.1.9) |
| [x] | `lpdG` | PP_4187 | Q88FB1 | kegg:ppu00785 | PRESENT | CURATED | PRESENT | Dihydrolipoyl dehydrogenase (EC 1.8.1.4) |
| [x] | `sucB` | PP_4188 | Q88FB0 | kegg:ppu00785 | PRESENT | CURATED | PRESENT | Dihydrolipoyllysine-residue succinyltransferase component of 2-oxoglutarate dehydrogenase complex (EC 2.3.1.61) (2-oxogl |
| [x] | `lpdV` | PP_4404 | Q88EP9 | kegg:ppu00785 | PRESENT | CURATED | PRESENT | Dihydrolipoyl dehydrogenase (EC 1.8.1.4) |
| [x] | `yqeF` | PP_4636 | Q88E32 | kegg:ppu00900 | PRESENT | CURATED | PRESENT | Acetyl-CoA acetyltransferase (EC 2.3.1.9) |
| [x] | `PP_4983` | PP_4983 | Q88D45 | kegg:ppu00350 | PRESENT | CURATED | PRESENT | Tryptophan 2-monooxygenase (EC 1.13.12.3) |
| [x] | `lpd` | PP_5366 | Q88C17 | kegg:ppu00785 | PRESENT | CURATED | PRESENT | Dihydrolipoyl dehydrogenase (EC 1.8.1.4) |

## Notes

Generated UTC: 2026-07-07T21:48:49.926754+00:00

## Workflow Notes

- 2026-07-11 status sync: ran `just module-deep-research-falcon tryptophan_metabolism_boundary`
  and `just module-pathway-deep-research-falcon tryptophan_metabolism_boundary ppu00380 PSEPK`.
  Both Edison task creation attempts failed immediately with HTTP 402 Payment Required, so
  the Falcon workflow boxes remain unchecked and no Falcon report files were written. Expected
  output paths remain `modules/tryptophan_metabolism_boundary-deep-research-falcon.md`
  and `projects/P_PUTIDA/deep-research/PSEPK__tryptophan_metabolism_boundary__ppu00380-deep-research-falcon.md`.
