---
title: "PSEPK ppu00640 Propanoate metabolism batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK ppu00640: Propanoate metabolism

- Module seed: `propanoate_metabolism_boundary`
- Candidate genes from membership table: 33
- Primary bucket genes: 7
- Existing review files: 33
- Curated review files: 33
- Existing Asta research files: 33

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
| [x] | `accC` | PP_0558 | Q88QD6 | kegg:ppu00061 | PRESENT | CURATED | PRESENT | Biotin carboxylase (EC 6.3.4.14) (Acetyl-coenzyme A carboxylase biotin carboxylase subunit A) |
| [x] | `accB` | PP_0559 | Q88QD5 | kegg:ppu00061 | PRESENT | CURATED | PRESENT | Biotin carboxyl carrier protein of acetyl-CoA carboxylase |
| [x] | `PP_0596` | PP_0596 | Q88Q98 | kegg:ppu00410 | PRESENT | CURATED | PRESENT | Omega-amino acid--pyruvate aminotransferase (EC 2.6.1.18) |
| [x] | `mmsA-I` | PP_0597 | Q88Q97 | kegg:ppu00562 | PRESENT | CURATED | PRESENT | methylmalonate-semialdehyde dehydrogenase (CoA acylating) (EC 1.2.1.27) |
| [x] | `pta` | PP_0774 | Q88PS4 | kegg:ppu00430 | PRESENT | CURATED | PRESENT | Phosphate acetyltransferase (EC 2.3.1.8) (Phosphotransacetylase) |
| [x] | `accA` | PP_1607 | Q88MG4 | kegg:ppu00061 | PRESENT | CURATED | PRESENT | Acetyl-coenzyme A carboxylase carboxyl transferase subunit alpha (ACCase subunit alpha) (Acetyl-CoA carboxylase carboxyl |
| [x] | `accD` | PP_1996 | Q88LD9 | kegg:ppu00061 | PRESENT | CURATED | PRESENT | Acetyl-coenzyme A carboxylase carboxyl transferase subunit beta (ACCase subunit beta) (Acetyl-CoA carboxylase carboxyltr |
| [x] | `acnA-I` | PP_2112 | Q88L24 | kegg:ppu00020 | PRESENT | CURATED | PRESENT | Aconitate hydratase (Aconitase) (EC 4.2.1.3) |
| [x] | `fadB` | PP_2136 | Q88L02 | kegg:ppu00930 | PRESENT | CURATED | PRESENT | Fatty acid oxidation complex subunit alpha [Includes: Enoyl-CoA hydratase/Delta(3)-cis-Delta(2)-trans-enoyl-CoA isomeras |
| [x] | `PP_2213` | PP_2213 | Q88KS6 | kegg:ppu00680 | PRESENT | CURATED | PRESENT | Acyl-CoA synthetase (EC 6.2.1.-) |
| [x] | `acd` | PP_2216 | Q88KS3 | kegg:ppu00410 | PRESENT | CURATED | PRESENT | 3-sulfinopropanoyl-CoA desulfinase (EC 1.3.8.11) (EC 3.13.1.4) (3-sulfinopropionyl coenzyme A desulfinase) (Cyclohexane- |
| [x] | `PP_2217` | PP_2217 | Q88KS2 | kegg:ppu00930 | PRESENT | CURATED | PRESENT | enoyl-CoA hydratase (EC 4.2.1.17) |
| [x] | `prpB` | PP_2334 | Q88KF6 | kegg:ppu00640 | PRESENT | CURATED | PRESENT | 2-methylisocitrate lyase (2-MIC) (MICL) (EC 4.1.3.30) ((2R,3S)-2-methylisocitrate lyase) |
| [x] | `prpC` | PP_2335 | Q88KF5 | kegg:ppu00020 | PRESENT | CURATED | PRESENT | Citrate synthase |
| [x] | `acnA-II` | PP_2336 | Q88KF4 | kegg:ppu00640 | PRESENT | CURATED | PRESENT | aconitate hydratase (EC 4.2.1.3) |
| [x] | `prpF` | PP_2337 | Q88KF3 | kegg:ppu00640 | PRESENT | CURATED | PRESENT | Aconitate isomerase |
| [x] | `prpD` | PP_2338 | Q88KF2 | kegg:ppu00640 | PRESENT | CURATED | PRESENT | 2-methylcitrate dehydratase (EC 4.2.1.79) |
| [x] | `acnB` | PP_2339 | Q88KF1 | kegg:ppu00020 | PRESENT | CURATED | PRESENT | Aconitate hydratase B (EC 4.2.1.3) (EC 4.2.1.99) (2-methylisocitrate dehydratase) |
| [x] | `prpE` | PP_2351 | Q88KD9 | kegg:ppu00640 | PRESENT | CURATED | PRESENT | Propionyl-CoA synthetase (EC 6.2.1.17) |
| [x] | `yqhD` | PP_2492 | Q88K01 | kegg:ppu00640 | PRESENT | CURATED | PRESENT | Alcohol dehydrogenase, NAD(P)-dependent (EC 1.1.1.1) |
| [x] | `paaF` | PP_3284 | Q88HR9 | kegg:ppu00930 | PRESENT | CURATED | PRESENT | Enoyl-CoA hydratase-isomerase (EC 4.2.1.17) |
| [x] | `aceA` | PP_4116 | Q88FI0 | kegg:ppu00640 | PRESENT | CURATED | PRESENT | Isocitrate lyase (EC 4.1.3.1) |
| [x] | `sucD` | PP_4185 | Q88FB3 | kegg:ppu00660 | PRESENT | CURATED | PRESENT | Succinate--CoA ligase [ADP-forming] subunit alpha (EC 6.2.1.5) (Succinyl-CoA synthetase subunit alpha) (SCS-alpha) |
| [x] | `sucC` | PP_4186 | Q88FB2 | kegg:ppu00660 | PRESENT | CURATED | PRESENT | Succinate--CoA ligase [ADP-forming] subunit beta (EC 6.2.1.5) (Succinyl-CoA synthetase subunit beta) (SCS-beta) |
| [x] | `lpdG` | PP_4187 | Q88FB1 | kegg:ppu00785 | PRESENT | CURATED | PRESENT | Dihydrolipoyl dehydrogenase (EC 1.8.1.4) |
| [x] | `bkdAA` | PP_4401 | Q88EQ2 | kegg:ppu00785 | PRESENT | CURATED | PRESENT | 2-oxoisovalerate dehydrogenase subunit alpha (EC 1.2.4.4) (Branched-chain alpha-keto acid dehydrogenase E1 component alp |
| [x] | `bkdAB` | PP_4402 | Q88EQ1 | kegg:ppu00785 | PRESENT | CURATED | PRESENT | 2-oxoisovalerate dehydrogenase subunit beta (EC 1.2.4.4) (Branched-chain alpha-keto acid dehydrogenase E1 component beta |
| [x] | `bkdB` | PP_4403 | Q88EQ0 | kegg:ppu00785 | PRESENT | CURATED | PRESENT | Dihydrolipoamide acetyltransferase component of pyruvate dehydrogenase complex (EC 2.3.1.-) |
| [x] | `lpdV` | PP_4404 | Q88EP9 | kegg:ppu00785 | PRESENT | CURATED | PRESENT | Dihydrolipoyl dehydrogenase (EC 1.8.1.4) |
| [x] | `acsA1` | PP_4487 | Q88EH6 | kegg:ppu00680 | PRESENT | CURATED | PRESENT | Acetyl-coenzyme A synthetase 1 (AcCoA synthetase 1) (Acs 1) (EC 6.2.1.1) (Acetate--CoA ligase 1) (Acyl-activating enzyme |
| [x] | `mmsA-II` | PP_4667 | Q88E01 | kegg:ppu00562 | PRESENT | CURATED | PRESENT | methylmalonate-semialdehyde dehydrogenase (CoA acylating) (EC 1.2.1.27) |
| [x] | `acsA2` | PP_4702 | Q88DW6 | kegg:ppu00680 | PRESENT | CURATED | PRESENT | Acetyl-coenzyme A synthetase 2 (AcCoA synthetase 2) (Acs 2) (EC 6.2.1.1) (Acetate--CoA ligase 2) (Acyl-activating enzyme |
| [x] | `lpd` | PP_5366 | Q88C17 | kegg:ppu00785 | PRESENT | CURATED | PRESENT | Dihydrolipoyl dehydrogenase (EC 1.8.1.4) |

## Notes

Generated UTC: 2026-07-08T13:36:57.131167+00:00

## Workflow Notes

- 2026-07-11 status sync: ran `just module-deep-research-falcon propanoate_metabolism_boundary`
  and `just module-pathway-deep-research-falcon propanoate_metabolism_boundary ppu00640 PSEPK`.
  Both Edison task creation attempts failed immediately with HTTP 402 Payment Required, so the
  Falcon workflow boxes remain unchecked and no Falcon report files were written. Expected output
  paths remain `modules/propanoate_metabolism_boundary-deep-research-falcon.md`
  and `projects/P_PUTIDA/deep-research/PSEPK__propanoate_metabolism_boundary__ppu00640-deep-research-falcon.md`.
