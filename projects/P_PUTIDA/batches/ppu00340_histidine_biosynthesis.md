---
title: "PSEPK ppu00340 Histidine metabolism batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK ppu00340: Histidine metabolism

- Module seed: `histidine_biosynthesis`
- Candidate genes from membership table: 20
- Primary bucket genes: 18
- Existing review files: 20
- Curated review files: 20
- Existing Asta research files: 20

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
| [x] | `gshA` | PP_0243 | Q88R90 | kegg:ppu00340 | PRESENT | CURATED | PRESENT | Glutamate--cysteine ligase (EC 6.3.2.2) (Gamma-ECS) (GCS) (Gamma-glutamylcysteine synthetase) |
| [x] | `hisB` | PP_0289 | Q88R45 | kegg:ppu00340 | PRESENT | CURATED | PRESENT | Imidazoleglycerol-phosphate dehydratase (IGPD) (EC 4.2.1.19) |
| [x] | `hisH` | PP_0290 | Q88R44 | kegg:ppu00340 | PRESENT | CURATED | PRESENT | Imidazole glycerol phosphate synthase subunit HisH (EC 4.3.2.10) (IGP synthase glutaminase subunit) (EC 3.5.1.2) (IGP sy |
| [x] | `hisA` | PP_0292 | Q88R42 | kegg:ppu00340 | PRESENT | CURATED | PRESENT | 1-(5-phosphoribosyl)-5-[(5-phosphoribosylamino)methylideneamino] imidazole-4-carboxamide isomerase (EC 5.3.1.16) (Phosph |
| [x] | `hisF` | PP_0293 | Q88R41 | kegg:ppu00340 | PRESENT | CURATED | PRESENT | Imidazole glycerol phosphate synthase subunit HisF (EC 4.3.2.10) (IGP synthase cyclase subunit) (IGP synthase subunit Hi |
| [x] | `hisG` | PP_0965 | Q88P87 | kegg:ppu00340 | PRESENT | CURATED | PRESENT | ATP phosphoribosyltransferase (ATP-PRT) (ATP-PRTase) (EC 2.4.2.17) |
| [x] | `hisD` | PP_0966 | P59400 | kegg:ppu00340 | PRESENT | CURATED | PRESENT | Histidinol dehydrogenase (HDH) (EC 1.1.1.23) |
| [x] | `hisC` | PP_0967 | Q88P86 | kegg:ppu00401 | PRESENT | CURATED | PRESENT | Histidinol-phosphate aminotransferase (EC 2.6.1.9) (Imidazole acetol-phosphate transaminase) |
| [x] | `PP_1721` | PP_1721 | Q88M53 | kegg:ppu00340 | PRESENT | CURATED | PRESENT | Phosphoserine phosphatase (EC 3.1.3.-) |
| [x] | `PP_3157` | PP_3157 | Q88I44 | kegg:ppu00340 | PRESENT | CURATED | PRESENT | Histidinol-phosphatase (EC 3.1.3.15) |
| [x] | `hisZ` | PP_4890 | Q88DD7 | kegg:ppu00340 | PRESENT | CURATED | PRESENT | ATP phosphoribosyltransferase regulatory subunit |
| [x] | `PP_4983` | PP_4983 | Q88D45 | kegg:ppu00350 | PRESENT | CURATED | PRESENT | Tryptophan 2-monooxygenase (EC 1.13.12.3) |
| [x] | `hisI` | PP_5014 | Q88D15 | kegg:ppu00340 | PRESENT | CURATED | PRESENT | Phosphoribosyl-AMP cyclohydrolase (PRA-CH) (EC 3.5.4.19) |
| [x] | `hisE` | PP_5015 | Q88D14 | kegg:ppu00340 | PRESENT | CURATED | PRESENT | Phosphoribosyl-ATP pyrophosphatase (PRA-PH) (EC 3.6.1.31) |
| [x] | `hutG` | PP_5029 | Q88D00 | kegg:ppu00340 | PRESENT | CURATED | PRESENT | N-formylglutamate deformylase (EC 3.5.1.68) |
| [x] | `hutI` | PP_5030 | Q88CZ9 | kegg:ppu00340 | PRESENT | CURATED | PRESENT | Imidazolonepropionase (EC 3.5.2.7) (Imidazolone-5-propionate hydrolase) |
| [x] | `hutH` | PP_5032 | Q88CZ7 | kegg:ppu00340 | PRESENT | CURATED | PRESENT | Histidine ammonia-lyase (Histidase) (EC 4.3.1.3) |
| [x] | `hutU` | PP_5033 | Q88CZ6 | kegg:ppu00340 | PRESENT | CURATED | PRESENT | Urocanate hydratase (Urocanase) (EC 4.2.1.49) (Imidazolonepropionate hydrolase) |
| [x] | `hutF` | PP_5036 | Q88CZ3 | kegg:ppu00340 | PRESENT | CURATED | PRESENT | Formimidoylglutamate deiminase (EC 3.5.3.13) |
| [x] | `PP_5147` | PP_5147 | Q88CN3 | kegg:ppu00340 | PRESENT | CURATED | PRESENT | Histidinol-phosphatase (EC 3.1.3.15) (Histidinol-phosphate phosphatase) |

## Notes

Generated UTC: 2026-07-07T00:14:53.697015+00:00
