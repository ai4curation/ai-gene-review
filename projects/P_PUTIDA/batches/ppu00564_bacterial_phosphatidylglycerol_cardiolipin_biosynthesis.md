---
title: "PSEPK phosphatidylglycerol and cardiolipin biosynthesis batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK phosphatidylglycerol and cardiolipin biosynthesis

- Module seed: `bacterial_phosphatidylglycerol_cardiolipin_biosynthesis`
- Candidate genes from membership table: 23
- Primary bucket genes: 17
- Existing review files: 11
- Curated review files: 11
- Existing OpenScientist research files: 3

## Curated Boundary

This batch extracts one reusable connected module from the broad KEGG
`ppu00564` map. Its first coherent part converts CDP-diacylglycerol to
phosphatidylglycerol through PgsA and PgpA. Phosphatidylglycerol is both a valid
module output and the input to the downstream cardiolipin branch.

The cardiolipin part models alternative synthase chemistry as variants:

- ClsA/Q88C19 and ClsB/Q88HT9 use two phosphatidylglycerol molecules.
- PP_5276/Q88CA5 is a PANTHER ClsC-family candidate for the distinct
  phosphatidylethanolamine-plus-phosphatidylglycerol reaction; the exact PSEPK
  activity remains unresolved and is grounded by characterized E. coli ClsC.
- PP_0892/Q88PF8 is a ClsB-like PLD-family candidate retained as a knowledge
  gap, not as an established module implementation.

Selected genes: `pgsA`, `pgpA`, `clsA`, `clsB`, `PP_5276`, and `PP_0892`.
Upstream CDP-diacylglycerol formation, phosphatidylethanolamine and
phosphatidylcholine synthesis, lipid remodeling, and lipid turnover are outside
this boundary. No one-step standalone module is introduced.

## Required Workflow

- [x] Curate or update the species-neutral module.
- [ ] Run module-level OpenScientist deep research.
- [ ] Run module + pathway + PSEPK OpenScientist deep research.
- [x] Fetch all selected genes with `just fetch-gene PSEPK <gene>`.
- [ ] Run OpenScientist deep research for selected genes.
- [x] Curate each selected gene review.
- [x] Validate module and gene reviews.
- [ ] Open one PR for this module/pathway.
- [ ] Shepherd PR through review, CI, and merge readiness.

## Candidate Genes

| Done | Gene | Locus | UniProt | Primary bucket | Existing review | Curation | OpenScientist research | Protein |
|---|---|---|---|---|---|---|---|---|
| [ ] | `PP_0058` | PP_0058 | Q88RS1 | kegg:ppu00561 | MISSING | MISSING | MISSING | 1-acyl-sn-glycerol-3-phosphate acyltransferase |
| [ ] | `plsY` | PP_0391 | Q88QU5 | kegg:ppu00561 | MISSING | MISSING | MISSING | Glycerol-3-phosphate acyltransferase (Acyl-PO4 G3P acyltransferase) (Acyl-phosphate--glycerol-3-phosphate acyltransferas |
| [x] | `pgpA` | PP_0520 | Q88QH3 | kegg:ppu00564 | PRESENT | CURATED | MISSING | Phosphatidylglycerophosphatase A (EC 3.1.3.27) (Phosphatidylglycerolphosphate phosphatase A) |
| [ ] | `eutC` | PP_0542 | Q88QF2 | kegg:ppu00564 | MISSING | MISSING | MISSING | Ethanolamine ammonia-lyase small subunit (EAL small subunit) (EC 4.3.1.7) |
| [ ] | `eutB` | PP_0543 | Q88QF1 | kegg:ppu00564 | MISSING | MISSING | MISSING | Ethanolamine ammonia-lyase large subunit (EAL large subunit) (EC 4.3.1.7) |
| [ ] | `pcs` | PP_0731 | Q88PW7 | kegg:ppu00564 | MISSING | MISSING | MISSING | Phosphatidylcholine synthase (EC 2.7.8.24) |
| [x] | `PP_0892` | PP_0892 | Q88PF8 | kegg:ppu00564 | PRESENT | CURATED | MISSING | Phospholipase family protein |
| [x] | `glpD` | PP_1073 | Q88NY0 | kegg:ppu00564 | PRESENT | CURATED | PRESENT | Glycerol-3-phosphate dehydrogenase (EC 1.1.5.3) |
| [ ] | `plsB` | PP_1520 | Q88MQ0 | kegg:ppu00561 | MISSING | MISSING | MISSING | Glycerol-3-phosphate acyltransferase (GPAT) (EC 2.3.1.15) |
| [ ] | `cdsA` | PP_1596 | Q88MH5 | kegg:ppu00564 | MISSING | MISSING | MISSING | Phosphatidate cytidylyltransferase (EC 2.7.7.41) |
| [ ] | `dgkA-I` | PP_1636 | Q88MD7 | kegg:ppu00561 | MISSING | MISSING | MISSING | Diacylglycerol kinase (EC 2.7.1.107) |
| [ ] | `plsC` | PP_1844 | Q88LT3 | kegg:ppu00561 | MISSING | MISSING | MISSING | 1-acyl-sn-glycerol-3-phosphate acyltransferase (EC 2.3.1.51) |
| [ ] | `ugpQ` | PP_2152 | Q88KY7 | kegg:ppu00564 | MISSING | MISSING | MISSING | Glycerophosphoryl diester phosphodiesterase (EC 3.1.4.46) |
| [ ] | `dgkA-II` | PP_2973 | Q88IM6 | kegg:ppu00561 | MISSING | MISSING | MISSING | Diacylglycerol kinase (EC 2.7.1.107) |
| [x] | `clsB` | PP_3264 | Q88HT9 | kegg:ppu00564 | PRESENT | CURATED | MISSING | Cardiolipin synthase B (CL synthase) (EC 2.7.8.-) |
| [x] | `pssA` | PP_3664 | Q88GQ4 | kegg:ppu00564 | PRESENT | CURATED | PRESENT | CDP-diacylglycerol--serine O-phosphatidyltransferase (EC 2.7.8.8) |
| [x] | `pgsA` | PP_4097 | Q88FJ8 | kegg:ppu00564 | PRESENT | CURATED | MISSING | CDP-diacylglycerol--glycerol-3-phosphate 3-phosphatidyltransferase (EC 2.7.8.5) |
| [ ] | `gpsA` | PP_4169 | Q88FC9 | kegg:ppu00564 | PRESENT | CURATED | MISSING | Glycerol-3-phosphate dehydrogenase [NAD(P)+] (EC 1.1.1.94) (NAD(P)(+)-dependent glycerol-3-phosphate dehydrogenase) (NAD |
| [ ] | `PP_4677` | PP_4677 | Q88DZ1 | kegg:ppu00564 | PRESENT | CURATED | MISSING | CDP-diacylglycerol--serine O-phosphatidyltransferase (EC 2.7.8.8) (Phosphatidylserine synthase) |
| [x] | `psd` | PP_4908 | Q88DB9 | kegg:ppu00564 | PRESENT | CURATED | PRESENT | Phosphatidylserine decarboxylase proenzyme (EC 4.1.1.65) [Cleaved into: Phosphatidylserine decarboxylase alpha chain; Ph |
| [ ] | `pchP` | PP_5130 | Q88CQ0 | kegg:ppu00564 | MISSING | MISSING | MISSING | Phosphoethanolamine/phosphocholine phosphatase (EC 3.1.3.75) |
| [x] | `PP_5276` | PP_5276 | Q88CA5 | kegg:ppu00564 | PRESENT | CURATED | MISSING | Phospholipase D family protein |
| [x] | `clsA` | PP_5364 | Q88C19 | kegg:ppu00564 | PRESENT | CURATED | MISSING | Cardiolipin synthase A (CL synthase) (EC 2.7.8.-) |

## Notes

Generated UTC: 2026-08-11T13:22:12.404544+00:00

OpenScientist research was started for all six selected genes, the generic
module, and the PSEPK module-plus-pathway query with 8100-second wrapper and
7200-second provider allowances. Slow jobs are allowed to continue; incomplete
provider output is not substituted with manually authored deep-research files.
