---
title: "PSEPK ppu00785 Lipoic acid metabolism batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK ppu00785: Lipoic acid metabolism

- Module seed: `lipoic_acid_metabolism_boundary`
- Candidate genes from membership table: 19
- Primary bucket genes: 19
- Existing review files: 19
- Curated review files: 19
- Existing Asta research files: 19

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
| [x] | `aceF` | PP_0338 | Q88QZ6 | kegg:ppu00785 | PRESENT | CURATED | PRESENT | Acetyltransferase component of pyruvate dehydrogenase complex (EC 2.3.1.12) |
| [x] | `aceE` | PP_0339 | Q88QZ5 | kegg:ppu00785 | PRESENT | CURATED | PRESENT | Pyruvate dehydrogenase E1 component (EC 1.2.4.1) |
| [x] | `acoC` | PP_0553 | Q88QE1 | kegg:ppu00785 | PRESENT | CURATED | PRESENT | Dihydrolipoyllysine-residue acetyltransferase component of acetoin cleaving system (EC 2.3.1.12) |
| [x] | `gcvT-I` | PP_0986 | Q88P67 | kegg:ppu00785 | PRESENT | CURATED | PRESENT | aminomethyltransferase (EC 2.1.2.10) (Glycine cleavage system T protein) |
| [x] | `gcvP1` | PP_0988 | Q88P65 | kegg:ppu00785 | PRESENT | CURATED | PRESENT | Glycine dehydrogenase (decarboxylating) 1 (EC 1.4.4.2) (Glycine cleavage system P-protein 1) (Glycine decarboxylase 1) ( |
| [x] | `gcvH1` | PP_0989 | Q88P64 | kegg:ppu00785 | PRESENT | CURATED | PRESENT | Glycine cleavage system H protein 1 |
| [x] | `lpdG` | PP_4187 | Q88FB1 | kegg:ppu00785 | PRESENT | CURATED | PRESENT | Dihydrolipoyl dehydrogenase (EC 1.8.1.4) |
| [x] | `sucB` | PP_4188 | Q88FB0 | kegg:ppu00785 | PRESENT | CURATED | PRESENT | Dihydrolipoyllysine-residue succinyltransferase component of 2-oxoglutarate dehydrogenase complex (EC 2.3.1.61) (2-oxogl |
| [x] | `sucA` | PP_4189 | Q88FA9 | kegg:ppu00785 | PRESENT | CURATED | PRESENT | 2-oxoglutarate dehydrogenase E1 component (EC 1.2.4.2) (Alpha-ketoglutarate dehydrogenase) |
| [x] | `bkdAA` | PP_4401 | Q88EQ2 | kegg:ppu00785 | PRESENT | CURATED | PRESENT | 2-oxoisovalerate dehydrogenase subunit alpha (EC 1.2.4.4) (Branched-chain alpha-keto acid dehydrogenase E1 component alp |
| [x] | `bkdAB` | PP_4402 | Q88EQ1 | kegg:ppu00785 | PRESENT | CURATED | PRESENT | 2-oxoisovalerate dehydrogenase subunit beta (EC 1.2.4.4) (Branched-chain alpha-keto acid dehydrogenase E1 component beta |
| [x] | `bkdB` | PP_4403 | Q88EQ0 | kegg:ppu00785 | PRESENT | CURATED | PRESENT | Dihydrolipoamide acetyltransferase component of pyruvate dehydrogenase complex (EC 2.3.1.-) |
| [x] | `lpdV` | PP_4404 | Q88EP9 | kegg:ppu00785 | PRESENT | CURATED | PRESENT | Dihydrolipoyl dehydrogenase (EC 1.8.1.4) |
| [x] | `lipA` | PP_4800 | Q88DM5 | kegg:ppu00785 | PRESENT | CURATED | PRESENT | Lipoyl synthase (EC 2.8.1.8) (Lip-syn) (LS) (Lipoate synthase) (Lipoic acid synthase) (Sulfur insertion protein LipA) |
| [x] | `lipB` | PP_4801 | Q88DM4 | kegg:ppu00785 | PRESENT | CURATED | PRESENT | Octanoyltransferase (EC 2.3.1.181) (Lipoate-protein ligase B) (Lipoyl/octanoyl transferase) (Octanoyl-[acyl-carrier-prot |
| [x] | `gcvP2` | PP_5192 | Q88CI9 | kegg:ppu00785 | PRESENT | CURATED | PRESENT | Glycine dehydrogenase (decarboxylating) 2 (EC 1.4.4.2) (Glycine cleavage system P-protein 2) (Glycine decarboxylase 2) ( |
| [x] | `gcvH2` | PP_5193 | Q88CI8 | kegg:ppu00785 | PRESENT | CURATED | PRESENT | Glycine cleavage system H protein 2 |
| [x] | `gcvT` | PP_5194 | Q88CI7 | kegg:ppu00785 | PRESENT | CURATED | PRESENT | Aminomethyltransferase (EC 2.1.2.10) (Glycine cleavage system T protein) |
| [x] | `lpd` | PP_5366 | Q88C17 | kegg:ppu00785 | PRESENT | CURATED | PRESENT | Dihydrolipoyl dehydrogenase (EC 1.8.1.4) |

## Notes

Generated UTC: 2026-07-08T15:18:35.883173+00:00

## Workflow Notes

- 2026-07-11 status sync: ran `just module-deep-research-falcon lipoic_acid_metabolism_boundary`
  and `just module-pathway-deep-research-falcon lipoic_acid_metabolism_boundary ppu00785 PSEPK`.
  Both Edison task creation attempts failed immediately with HTTP 402 Payment Required, so the
  Falcon workflow boxes remain unchecked and no Falcon report files were written. Expected output
  paths remain `modules/lipoic_acid_metabolism_boundary-deep-research-falcon.md`
  and `projects/P_PUTIDA/deep-research/PSEPK__lipoic_acid_metabolism_boundary__ppu00785-deep-research-falcon.md`.
