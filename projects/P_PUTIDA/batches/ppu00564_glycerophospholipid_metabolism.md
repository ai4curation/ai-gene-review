---
title: "PSEPK ppu00564 Glycerophospholipid metabolism batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK ppu00564: Glycerophospholipid metabolism

- Module seed: `glycerophospholipid_metabolism`
- Candidate genes from membership table: 23
- Primary bucket genes: 17
- Existing review files: 23
- Curated review files: 23
- Existing Asta research files: 23

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
| [x] | `PP_0058` | PP_0058 | Q88RS1 | kegg:ppu00561 | PRESENT | CURATED | PRESENT | 1-acyl-sn-glycerol-3-phosphate acyltransferase |
| [x] | `plsY` | PP_0391 | Q88QU5 | kegg:ppu00561 | PRESENT | CURATED | PRESENT | Glycerol-3-phosphate acyltransferase (Acyl-PO4 G3P acyltransferase) (Acyl-phosphate--glycerol-3-phosphate acyltransferas |
| [x] | `pgpA` | PP_0520 | Q88QH3 | kegg:ppu00564 | PRESENT | CURATED | PRESENT | Phosphatidylglycerophosphatase A (EC 3.1.3.27) (Phosphatidylglycerolphosphate phosphatase A) |
| [x] | `eutC` | PP_0542 | Q88QF2 | kegg:ppu00564 | PRESENT | CURATED | PRESENT | Ethanolamine ammonia-lyase small subunit (EAL small subunit) (EC 4.3.1.7) |
| [x] | `eutB` | PP_0543 | Q88QF1 | kegg:ppu00564 | PRESENT | CURATED | PRESENT | Ethanolamine ammonia-lyase large subunit (EAL large subunit) (EC 4.3.1.7) |
| [x] | `pcs` | PP_0731 | Q88PW7 | kegg:ppu00564 | PRESENT | CURATED | PRESENT | Phosphatidylcholine synthase (EC 2.7.8.24) |
| [x] | `PP_0892` | PP_0892 | Q88PF8 | kegg:ppu00564 | PRESENT | CURATED | PRESENT | Phospholipase family protein |
| [x] | `glpD` | PP_1073 | Q88NY0 | kegg:ppu00564 | PRESENT | CURATED | PRESENT | Glycerol-3-phosphate dehydrogenase (EC 1.1.5.3) |
| [x] | `plsB` | PP_1520 | Q88MQ0 | kegg:ppu00561 | PRESENT | CURATED | PRESENT | Glycerol-3-phosphate acyltransferase (GPAT) (EC 2.3.1.15) |
| [x] | `cdsA` | PP_1596 | Q88MH5 | kegg:ppu00564 | PRESENT | CURATED | PRESENT | Phosphatidate cytidylyltransferase (EC 2.7.7.41) |
| [x] | `dgkA-I` | PP_1636 | Q88MD7 | kegg:ppu00561 | PRESENT | CURATED | PRESENT | Diacylglycerol kinase (EC 2.7.1.107) |
| [x] | `plsC` | PP_1844 | Q88LT3 | kegg:ppu00561 | PRESENT | CURATED | PRESENT | 1-acyl-sn-glycerol-3-phosphate acyltransferase (EC 2.3.1.51) |
| [x] | `ugpQ` | PP_2152 | Q88KY7 | kegg:ppu00564 | PRESENT | CURATED | PRESENT | Glycerophosphoryl diester phosphodiesterase (EC 3.1.4.46) |
| [x] | `dgkA-II` | PP_2973 | Q88IM6 | kegg:ppu00561 | PRESENT | CURATED | PRESENT | Diacylglycerol kinase (EC 2.7.1.107) |
| [x] | `clsB` | PP_3264 | Q88HT9 | kegg:ppu00564 | PRESENT | CURATED | PRESENT | Cardiolipin synthase B (CL synthase) (EC 2.7.8.-) |
| [x] | `pssA` | PP_3664 | Q88GQ4 | kegg:ppu00564 | PRESENT | CURATED | PRESENT | CDP-diacylglycerol--serine O-phosphatidyltransferase (EC 2.7.8.8) |
| [x] | `pgsA` | PP_4097 | Q88FJ8 | kegg:ppu00564 | PRESENT | CURATED | PRESENT | CDP-diacylglycerol--glycerol-3-phosphate 3-phosphatidyltransferase (EC 2.7.8.5) |
| [x] | `gpsA` | PP_4169 | Q88FC9 | kegg:ppu00564 | PRESENT | CURATED | PRESENT | Glycerol-3-phosphate dehydrogenase [NAD(P)+] (EC 1.1.1.94) (NAD(P)(+)-dependent glycerol-3-phosphate dehydrogenase) (NAD |
| [x] | `PP_4677` | PP_4677 | Q88DZ1 | kegg:ppu00564 | PRESENT | CURATED | PRESENT | CDP-diacylglycerol--serine O-phosphatidyltransferase (EC 2.7.8.8) (Phosphatidylserine synthase) |
| [x] | `psd` | PP_4908 | Q88DB9 | kegg:ppu00564 | PRESENT | CURATED | PRESENT | Phosphatidylserine decarboxylase proenzyme (EC 4.1.1.65) [Cleaved into: Phosphatidylserine decarboxylase alpha chain; Ph |
| [x] | `pchP` | PP_5130 | Q88CQ0 | kegg:ppu00564 | PRESENT | CURATED | PRESENT | Phosphoethanolamine/phosphocholine phosphatase (EC 3.1.3.75) |
| [x] | `PP_5276` | PP_5276 | Q88CA5 | kegg:ppu00564 | PRESENT | CURATED | PRESENT | Phospholipase D family protein |
| [x] | `clsA` | PP_5364 | Q88C19 | kegg:ppu00564 | PRESENT | CURATED | PRESENT | Cardiolipin synthase A (CL synthase) (EC 2.7.8.-) |

## Notes

Generated UTC: 2026-07-08T11:21:46.170244+00:00

First-pass conclusion: `ppu00564` is a broad glycerophospholipid metabolism map,
not one linear route. Direct membrane-phospholipid chemistry is covered by
phosphatidic-acid/CDP-DAG precursor enzymes, phosphatidylglycerol/cardiolipin
branch genes, and PS/PE/PC branch genes. `gpsA`/`glpD`, `ugpQ`/`pchP`, and
`eutB`/`eutC` are glycerol-3-phosphate, headgroup-turnover, and ethanolamine
side contexts rather than strict phospholipid-synthesis steps. `PP_5276` remains
the main unresolved PLD-family substrate question.

## Workflow Notes

- 2026-07-11 status sync: ran `just module-deep-research-falcon glycerophospholipid_metabolism`
  and `just module-pathway-deep-research-falcon glycerophospholipid_metabolism ppu00564 PSEPK`.
  Both Edison task creation attempts failed immediately with HTTP 402 Payment Required, so
  the Falcon workflow boxes remain unchecked and no Falcon report files were written. Expected
  output paths remain `modules/glycerophospholipid_metabolism-deep-research-falcon.md`
  and `projects/P_PUTIDA/deep-research/PSEPK__glycerophospholipid_metabolism__ppu00564-deep-research-falcon.md`.
