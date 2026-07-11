---
title: "PSEPK ppu01503 Cationic antimicrobial peptide (CAMP) resistance batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK ppu01503: Cationic antimicrobial peptide (CAMP) resistance

- Module seed: `cationic_antimicrobial_peptide_resistance_boundary`
- Candidate genes from membership table: 21
- Primary bucket genes: 9
- Existing review files: 21
- Curated review files: 21
- Existing Asta research files: 21

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
| [x] | `PP_0024` | PP_0024 | Q88RV5 | kegg:ppu00540 | PRESENT | CURATED | PRESENT | Membrane-associated metal-dependent hydrolase |
| [x] | `dsbA` | PP_0127 | Q88RK2 | kegg:ppu01503 | PRESENT | CURATED | PRESENT | Thiol:disulfide interchange protein |
| [x] | `PP_0906` | PP_0906 | Q88PE4 | kegg:ppu01501 | PRESENT | CURATED | PRESENT | Multidrug efflux RND transporter |
| [x] | `PP_0907` | PP_0907 | Q88PE3 | kegg:ppu01501 | PRESENT | CURATED | PRESENT | RND efflux membrane fusion protein-related protein |
| [x] | `phoP` | PP_1186 | Q88NM1 | kegg:ppu01503 | PRESENT | CURATED | PRESENT | Two component system DNA-binding transcriptional dual regulator |
| [x] | `phoQ` | PP_1187 | Q88NM0 | kegg:ppu01503 | PRESENT | CURATED | PRESENT | histidine kinase (EC 2.7.13.3) |
| [x] | `PP_1202` | PP_1202 | Q88NK5 | kegg:ppu01503 | PRESENT | CURATED | PRESENT | Phosphatidylglycerol lysyltransferase (EC 2.3.2.3) (Lysylphosphatidylglycerol synthase) |
| [x] | `ttgB` | PP_1385 | Q88N31 | kegg:ppu01501 | PRESENT | CURATED | PRESENT | Probable efflux pump membrane transporter TtgB |
| [x] | `ttgA` | PP_1386 | Q88N30 | kegg:ppu01501 | PRESENT | CURATED | PRESENT | Probable efflux pump periplasmic linker TtgA |
| [x] | `PP_1430` | PP_1430 | Q88MY8 | kegg:ppu01503 | PRESENT | CURATED | PRESENT | Probable periplasmic serine endoprotease DegP-like (EC 3.4.21.107) (Protease Do) |
| [x] | `lpxA` | PP_1603 | Q88MG8 | kegg:ppu00540 | PRESENT | CURATED | PRESENT | Acyl-[acyl-carrier-protein]--UDP-N-acetylglucosamine O-acyltransferase (UDP-N-acetylglucosamine acyltransferase) (EC 2.3 |
| [x] | `PP_1798` | PP_1798 | Q88LX9 | kegg:ppu01501 | PRESENT | CURATED | PRESENT | Outer membrane efflux protein |
| [x] | `PP_2320` | PP_2320 | Q88KH0 | kegg:ppu01503 | PRESENT | CURATED | PRESENT | L,D-TPase catalytic domain-containing protein |
| [x] | `cpxR` | PP_3372 | Q88HI5 | kegg:ppu01503 | PRESENT | CURATED | PRESENT | CpxR-Pasp DNA-binding transcriptional two-component system regulator |
| [x] | `PP_3455` | PP_3455 | Q88HA5 | kegg:ppu01501 | PRESENT | CURATED | PRESENT | Multidrug efflux RND membrane fusion protein |
| [x] | `mexB` | PP_3456 | Q88HA4 | kegg:ppu01501 | PRESENT | CURATED | PRESENT | Efflux pump membrane transporter |
| [x] | `PP_4503` | PP_4503 | Q88EG2 | kegg:ppu01503 | PRESENT | CURATED | PRESENT | DNA-binding response regulator |
| [x] | `ppiA` | PP_4541 | Q88EC5 | kegg:ppu03250 | PRESENT | CURATED | PRESENT | Peptidyl-prolyl cis-trans isomerase (PPIase) (EC 5.2.1.8) |
| [x] | `PP_4592` | PP_4592 | Q88E74 | kegg:ppu00540 | PRESENT | CURATED | PRESENT | Metal dependent hydrolase |
| [x] | `amiC` | PP_4897 | Q88DD0 | kegg:ppu01503 | PRESENT | CURATED | PRESENT | N-acetylmuramoyl-L-alanine amidase AmiC (EC 3.5.1.28) |
| [x] | `PP_4923` | PP_4923 | Q88DA4 | kegg:ppu01501 | PRESENT | CURATED | PRESENT | Outer membrane efflux protein |

## Notes

Generated UTC: 2026-07-08T19:38:27.996230+00:00

## Workflow Notes

- 2026-07-11 status sync: ran `just module-deep-research-falcon cationic_antimicrobial_peptide_resistance_boundary`
  and `just module-pathway-deep-research-falcon cationic_antimicrobial_peptide_resistance_boundary ppu01503 PSEPK`.
  Both Edison task creation attempts failed immediately with HTTP 402 Payment Required, so the
  Falcon workflow boxes remain unchecked and no Falcon report files were written. Expected output
  paths remain `modules/cationic_antimicrobial_peptide_resistance_boundary-deep-research-falcon.md`
  and `projects/P_PUTIDA/deep-research/PSEPK__cationic_antimicrobial_peptide_resistance_boundary__ppu01503-deep-research-falcon.md`.
