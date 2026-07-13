---
title: "PSEPK ppu00071 Fatty acid degradation batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK ppu00071: Fatty acid degradation

- Module seed: `bacterial_fatty_acid_beta_oxidation`
- Candidate genes from membership table: 22
- Primary bucket genes: 6
- Existing review files: 22
- Curated review files: 22
- Existing Asta research files: 22

## Required Workflow

- [x] Curate or update the species-neutral module.
- [x] Run module-level Falcon deep research.
- [x] Run module + pathway + PSEPK Falcon deep research.
- [x] Fetch all selected genes with `just fetch-gene PSEPK <gene>`.
- [x] Run Asta deep research for selected genes.
- [x] Curate each selected gene review.
- [x] Validate module and gene reviews.
- [ ] Open one PR for this module/pathway.
- [ ] Shepherd PR through review, CI, and merge readiness.

## Candidate Genes

| Done | Gene | Locus | UniProt | Primary bucket | Existing review | Curation | Asta research | Protein |
|---|---|---|---|---|---|---|---|---|
| [x] | `gcdH` | PP_0158 | Q88RH2 | kegg:ppu00380 | PRESENT | CURATED | PRESENT | glutaryl-CoA dehydrogenase (ETF) (EC 1.3.8.6) |
| [x] | `PP_0582` | PP_0582 | Q88QB2 | kegg:ppu00900 | PRESENT | CURATED | PRESENT | Thiolase family protein |
| [x] | `frmA` | PP_1616 | Q88MF5 | kegg:ppu00626 | PRESENT | CURATED | PRESENT | S-(hydroxymethyl)glutathione dehydrogenase (EC 1.1.1.1) (EC 1.1.1.284) (Alcohol dehydrogenase class-3) (Alcohol dehydrog |
| [x] | `fadE` | PP_1893 | Q88LN6 | kegg:ppu00071 | PRESENT | CURATED | PRESENT | Acyl-coenzyme A dehydrogenase (EC 1.3.8.7) (EC 1.3.8.8) |
| [x] | `fadA__Q88L84` | PP_2051 | Q88L84 | kegg:ppu00592 | PRESENT | CURATED | PRESENT | 3-ketoacyl-CoA thiolase (Thiolase I) (EC 2.3.1.16) |
| [x] | `fadB` | PP_2136 | Q88L02 | kegg:ppu00930 | PRESENT | CURATED | PRESENT | Fatty acid oxidation complex subunit alpha [Includes: Enoyl-CoA hydratase/Delta(3)-cis-Delta(2)-trans-enoyl-CoA isomeras |
| [x] | `fadA__Q88L01` | PP_2137 | Q88L01 | kegg:ppu00592 | PRESENT | CURATED | PRESENT | 3-ketoacyl-CoA thiolase (EC 2.3.1.16) (Acetyl-CoA acyltransferase) (Beta-ketothiolase) (Fatty acid oxidation complex sub |
| [x] | `PP_2215` | PP_2215 | Q88KS4 | kegg:ppu00900 | PRESENT | CURATED | PRESENT | Acetyl-CoA acetyltransferase (EC 2.3.1.9) |
| [x] | `acd` | PP_2216 | Q88KS3 | kegg:ppu00410 | PRESENT | CURATED | PRESENT | 3-sulfinopropanoyl-CoA desulfinase (EC 1.3.8.11) (EC 3.13.1.4) (3-sulfinopropionyl coenzyme A desulfinase) (Cyclohexane- |
| [x] | `PP_2217` | PP_2217 | Q88KS2 | kegg:ppu00930 | PRESENT | CURATED | PRESENT | enoyl-CoA hydratase (EC 4.2.1.17) |
| [x] | `PP_2437` | PP_2437 | Q88K54 | kegg:ppu00071 | PRESENT | CURATED | PRESENT | long-chain-acyl-CoA dehydrogenase (EC 1.3.8.8) |
| [x] | `PP_2793` | PP_2793 | Q88J56 | kegg:ppu00071 | PRESENT | CURATED | PRESENT | long-chain-acyl-CoA dehydrogenase (EC 1.3.8.8) |
| [x] | `paaF` | PP_3284 | Q88HR9 | kegg:ppu00930 | PRESENT | CURATED | PRESENT | Enoyl-CoA hydratase-isomerase (EC 4.2.1.17) |
| [x] | `PP_3355` | PP_3355 | Q88HK1 | kegg:ppu00900 | PRESENT | CURATED | PRESENT | Beta-ketothiolase |
| [x] | `PP_3725` | PP_3725 | Q88GJ7 | kegg:ppu00071 | PRESENT | CURATED | PRESENT | Acyl-CoA dehydrogenase |
| [x] | `bktB` | PP_3754 | Q88GH0 | kegg:ppu00900 | PRESENT | CURATED | PRESENT | Beta-ketothiolase BktB (EC 2.3.1.16, EC 2.3.1.9) |
| [x] | `adhP` | PP_3839 | Q88G86 | kegg:ppu00626 | PRESENT | CURATED | PRESENT | Short-chain alcohol dehydrogenase (EC 1.1.1.-, EC 1.1.1.1) |
| [x] | `fadD-I` | PP_4549 | Q88EB7 | kegg:ppu04146 | PRESENT | CURATED | PRESENT | Long-chain-fatty-acid--CoA ligase (EC 6.2.1.3) (Long-chain acyl-CoA synthetase) |
| [x] | `fadD-II` | PP_4550 | Q88EB6 | kegg:ppu04146 | PRESENT | CURATED | PRESENT | Long-chain-fatty-acid--CoA ligase (EC 6.2.1.3) (Long-chain acyl-CoA synthetase) |
| [x] | `yqeF` | PP_4636 | Q88E32 | kegg:ppu00900 | PRESENT | CURATED | PRESENT | Acetyl-CoA acetyltransferase (EC 2.3.1.9) |
| [x] | `alkT` | PP_5314 | Q88C69 | kegg:ppu00071 | PRESENT | CURATED | PRESENT | Rubredoxin-NAD(+) reductase (EC 1.18.1.1) |
| [x] | `PP_5371` | PP_5371 | Q88C12 | kegg:ppu00071 | PRESENT | CURATED | PRESENT | Rubredoxin/rubredoxin reductase |

## Promoted Gap-Fill / Conflict Genes

These genes are absent from the 22-gene KEGG membership batch but were checked
because the PSEPK Falcon pathway report identified them as missing beta-oxidation
coverage or as a possible missing activation candidate. `def2`/PP_4559 is
included here as a resolved identifier conflict rather than as a beta-oxidation
component.

| Done | Gene | Locus | UniProt | Source | Curation | Asta research | Protein / outcome |
|---|---|---|---|---|---|---|---|
| [x] | `PP_0368` | PP_0368 | Q88QW6 | Falcon gap-fill | CURATED | PRESENT | Promoted long-chain ACAD candidate; UniProt DMSP-family specificity conflict retained as follow-up |
| [x] | `PP_0370` | PP_0370 | Q88QW4 | Falcon gap-fill | CURATED | PRESENT | Promoted medium-chain ACAD candidate; UniProt DMSP-family specificity conflict retained as follow-up |
| [x] | `PP_0763` | PP_0763 | Q88PT5 | Falcon gap-fill | CURATED | PRESENT | Medium-chain fatty acid-CoA ligase candidate for C5/C6 activation |
| [x] | `hbd` | PP_3755 | Q88GG9 | Falcon gap-fill | CURATED | PRESENT | Short-chain 3-hydroxybutyryl-CoA dehydrogenase candidate |
| [x] | `def2` | PP_4559 | Q88EA7 | Falcon identifier conflict | CURATED | PRESENT | Current UniProt/GOA/PANTHER support peptide deformylase, not CoA ligase |

## Notes

Generated UTC: 2026-07-07T06:05:00+00:00

Completed first-pass state:

- Gene-level first pass is complete: all 22 KEGG candidate genes plus 5
  Falcon-promoted/conflict genes have review folders, Asta first-pass research,
  curated YAML reviews, and validation complete.
- Newly curated beta-oxidation acyl-CoA dehydrogenase candidates: `fadE`,
  `PP_2437`, and `PP_2793`.
- Newly curated unresolved/specialized acyl-CoA dehydrogenase-family candidates:
  `acd` and `PP_3725`.
- Newly curated alkane/rubredoxin electron-transfer side nodes: `alkT` and
  `PP_5371`.
- Falcon-promoted gap-fill genes now reviewed: `PP_0368`, `PP_0370`,
  `PP_0763`, and `hbd`/PP_3755. `def2`/PP_4559 was reviewed as a source
  conflict and should not be counted as beta-oxidation without new evidence.
- New bacterial module seed: `modules/bacterial_fatty_acid_beta_oxidation.yaml`.
  It validates structurally and by term labels after adding the promoted
  activation, ACAD, and short-chain oxidation context. The older
  `modules/fatty_acid_beta_oxidation.yaml` remains the cross-species
  mitochondrial module.
- Both Falcon reports are complete:
  `modules/bacterial_fatty_acid_beta_oxidation-deep-research-falcon.md` and
  `projects/P_PUTIDA/deep-research/PSEPK__bacterial_fatty_acid_beta_oxidation__ppu00071-deep-research-falcon.md`.
- Validation note: all 22 KEGG gene reviews, the 5 promoted/conflict reviews,
  and the module validate.
