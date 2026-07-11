---
title: "PSEPK ppu00760 Nicotinate and nicotinamide metabolism batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK ppu00760: Nicotinate and nicotinamide metabolism

- Module seed: `nad_biosynthesis_and_nicotinate_metabolism`
- Candidate genes from membership table: 30
- Primary bucket genes: 25
- Existing review files: 30
- Curated review files: 30
- Existing Asta research files: 30

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
| [x] | `pntB` | PP_0155 | Q88RH4 | kegg:ppu00760 | PRESENT | CURATED | PRESENT | NAD(P) transhydrogenase subunit beta (EC 7.1.1.1) (Nicotinamide nucleotide transhydrogenase subunit beta) |
| [x] | `pntAA` | PP_0156 | A0A140FVX4 | kegg:ppu00760 | PRESENT | CURATED | PRESENT | NAD(P) transhydrogenase subunit alpha part 1 (EC 7.1.1.1) (Nicotinamide nucleotide transhydrogenase subunit alpha 1) (Py |
| [x] | `davD` | PP_0213 | Q88RC0 | kegg:ppu00350 | PRESENT | CURATED | PRESENT | Glutarate-semialdehyde dehydrogenase (EC 1.2.1.-) |
| [x] | `nadC` | PP_0787 | Q88PR1 | kegg:ppu00760 | PRESENT | CURATED | PRESENT | Probable nicotinate-nucleotide pyrophosphorylase [carboxylating] (EC 2.4.2.19) (Quinolinate phosphoribosyltransferase [d |
| [x] | `nadA` | PP_1231 | Q88NH8 | kegg:ppu00760 | PRESENT | CURATED | PRESENT | Quinolinate synthase (EC 2.5.1.72) |
| [x] | `ushA` | PP_1414 | Q88N04 | kegg:ppu00760 | PRESENT | CURATED | PRESENT | 5'-nucleotidase-2',3'-cyclic phosphodiesterase (EC 3.1.3.5, EC 3.1.4.16, EC 3.6.1.45) |
| [x] | `nadB` | PP_1426 | Q88MZ2 | kegg:ppu00760 | PRESENT | CURATED | PRESENT | L-aspartate oxidase (EC 1.4.3.16) |
| [x] | `surE` | PP_1620 | Q88MF1 | kegg:ppu00760 | PRESENT | CURATED | PRESENT | 5'-nucleotidase SurE (EC 3.1.3.5) (Nucleoside 5'-monophosphate phosphohydrolase) |
| [x] | `pncC` | PP_1628 | Q88ME5 | kegg:ppu00760 | PRESENT | CURATED | PRESENT | NMN amidohydrolase (EC 3.5.1.42) |
| [x] | `mazG` | PP_1657 | Q88MB7 | kegg:ppu00770 | PRESENT | CURATED | PRESENT | Nucleoside triphosphate pyrophosphohydrolase (EC 3.6.1.8) |
| [x] | `nadK` | PP_2012 | Q88LC3 | kegg:ppu00760 | PRESENT | CURATED | PRESENT | NAD kinase (EC 2.7.1.23) (ATP-dependent NAD kinase) |
| [x] | `sthA` | PP_2151 | Q88KY8 | kegg:ppu00760 | PRESENT | CURATED | PRESENT | Soluble pyridine nucleotide transhydrogenase (STH) (EC 1.6.1.1) (NAD(P)(+) transhydrogenase [B-specific]) |
| [x] | `sad-I` | PP_2488 | Q88K05 | kegg:ppu00350 | PRESENT | CURATED | PRESENT | NAD+-dependent succinate semialdehyde dehydrogenase (EC 1.2.1.24) |
| [x] | `PP_2531` | PP_2531 | Q88JW6 | kegg:ppu00760 | PRESENT | CURATED | PRESENT | 5-nucleotidase |
| [x] | `PP_3103` | PP_3103 | Q88I96 | kegg:ppu00760 | PRESENT | CURATED | PRESENT | Uncharacterized protein |
| [x] | `sad-II` | PP_3151 | Q88I50 | kegg:ppu00760 | PRESENT | CURATED | PRESENT | NAD+-dependent succinate semialdehyde dehydrogenase (EC 1.2.1.24) |
| [x] | `nicF` | PP_3941 | Q88FY5 | kegg:ppu00760 | PRESENT | CURATED | PRESENT | Maleamate amidohydrolase (EC 3.5.1.107) (Nicotinate degradation protein F) |
| [x] | `maiA` | PP_3942 | Q88FY4 | kegg:ppu00760 | PRESENT | CURATED | PRESENT | Maleate isomerase (EC 5.2.1.1) (Maleate cis-trans isomerase) (Nicotinate degradation protein E) |
| [x] | `nicD` | PP_3943 | Q88FY3 | kegg:ppu00760 | PRESENT | CURATED | PRESENT | N-formylmaleamate deformylase (EC 3.5.1.106) (Nicotinate degradation protein D) |
| [x] | `nicC` | PP_3944 | Q88FY2 | kegg:ppu00760 | PRESENT | CURATED | PRESENT | 6-hydroxynicotinate 3-monooxygenase (6-HNA monooxygenase) (EC 1.14.13.114) (Nicotinate degradation protein C) |
| [x] | `nicX` | PP_3945 | Q88FY1 | kegg:ppu00760 | PRESENT | CURATED | PRESENT | 2,5-dihydroxypyridine 5,6-dioxygenase (2,5-DHP dioxygenase) (EC 1.13.11.9) (Nicotinate degradation protein X) |
| [x] | `nicA` | PP_3947 | Q88FX9 | kegg:ppu00760 | PRESENT | CURATED | PRESENT | Nicotinate dehydrogenase subunit A (EC 1.17.2.1) (Nicotinate degradation protein A) (Nicotinate dehydrogenase small subu |
| [x] | `nicB` | PP_3948 | Q88FX8 | kegg:ppu00760 | PRESENT | CURATED | PRESENT | Nicotinate dehydrogenase subunit B (EC 1.17.2.1) (Nicotinate degradation protein B) (Nicotinate dehydrogenase large subu |
| [x] | `nudC` | PP_4029 | Q88FQ8 | kegg:ppu04146 | PRESENT | CURATED | PRESENT | NAD-capped RNA hydrolase NudC (DeNADding enzyme NudC) (EC 3.6.1.-) (NADH pyrophosphatase) (EC 3.6.1.22) |
| [x] | `gabD-II` | PP_4422 | Q88EN2 | kegg:ppu00350 | PRESENT | CURATED | PRESENT | Succinate-semialdehyde dehydrogenase (NADP+) (EC 1.2.1.79) |
| [x] | `nadD` | PP_4810 | Q88DL5 | kegg:ppu00760 | PRESENT | CURATED | PRESENT | Probable nicotinate-nucleotide adenylyltransferase (EC 2.7.7.18) (Deamido-NAD(+) diphosphorylase) (Deamido-NAD(+) pyroph |
| [x] | `pncB` | PP_4868 | Q88DF7 | kegg:ppu00760 | PRESENT | CURATED | PRESENT | Nicotinate phosphoribosyltransferase (NAPRTase) (EC 6.3.4.21) |
| [x] | `nadE` | PP_4869 | Q88DF6 | kegg:ppu00760 | PRESENT | CURATED | PRESENT | NH(3)-dependent NAD(+) synthetase (EC 6.3.1.5) |
| [x] | `cobB__Q88BY5` | PP_5402 | Q88BY5 | kegg:ppu00760 | PRESENT | CURATED | PRESENT | NAD-dependent protein deacylase (EC 2.3.1.286) (Regulatory protein SIR2 homolog) |
| [x] | `pntAB` | PP_5747 | A0A140FVX3 | kegg:ppu00760 | PRESENT | CURATED | PRESENT | proton-translocating NAD(P)(+) transhydrogenase (EC 7.1.1.1) |

## Notes

Generated UTC: 2026-07-07T11:38:33.926540+00:00
