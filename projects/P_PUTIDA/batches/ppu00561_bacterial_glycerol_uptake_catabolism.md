---
title: "PSEPK ppu00561 bacterial glycerol uptake and catabolism"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK ppu00561: bacterial glycerol uptake and catabolism

- Module seed: `bacterial_glycerol_uptake_catabolism`
- Candidate genes from membership table: 12
- Primary bucket genes: 12
- Existing review files: 4
- Curated review files: 4
- Selected module genes: 3
- Selected gene reviews curated: 3
- Selected OpenScientist reports: 1 of 3 (`glpD`)

## Curated Boundary

- Required route: `glpF`, `glpK`, and `glpD`.
- GlpF is a passive glycerol channel; ATP is consumed by GlpK, not by the
  transport step.
- KT2440 GlpD is the FAD-dependent quinone-linked enzyme, not an NAD-dependent
  soluble glycerol-3-phosphate dehydrogenase.
- Phospholipid turnover, glycerolipid biosynthesis, quinol reoxidation, and
  downstream glycolysis are outside the boundary.

## Required Workflow

- [x] Curate or update the species-neutral module.
- [ ] Run module-level OpenScientist deep research.
- [ ] Run module + pathway + PSEPK OpenScientist deep research.
- [x] Fetch all selected genes with `just fetch-gene PSEPK <gene>`.
- [ ] Run OpenScientist deep research for selected genes.
- [x] Curate each selected gene review.
- [x] Validate module and gene reviews.
- [x] Open one PR for this module/pathway: [#2321](https://github.com/ai4curation/ai-gene-review/pull/2321).
- [ ] Shepherd PR through review, CI, and merge readiness.

2026-07-26: OpenScientist timed out after 7200s for the module + pathway +
PSEPK report; no report file was produced.

2026-07-26: The generic module-level OpenScientist run also timed out after
7200s without producing a report.

2026-07-26: The `glpF` gene-level run timed out after 7200s with no report.
The `glpD` run persisted a complete report and artifacts despite the wrapper
returning a timeout status; its reaction and pathway claims were reconciled
against the UniProt record and PMID:25827416. The pre-existing `glpK` Asta
report remains the research source for that gene.

## Candidate Genes

| Done | Gene | Locus | UniProt | Primary bucket | Existing review | Curation | OpenScientist research | Protein |
|---|---|---|---|---|---|---|---|---|
| [ ] | `PP_0058` | PP_0058 | Q88RS1 | kegg:ppu00561 | MISSING | MISSING | MISSING | 1-acyl-sn-glycerol-3-phosphate acyltransferase |
| [ ] | `plsY` | PP_0391 | Q88QU5 | kegg:ppu00561 | MISSING | MISSING | MISSING | Glycerol-3-phosphate acyltransferase (Acyl-PO4 G3P acyltransferase) (Acyl-phosphate--glycerol-3-phosphate acyltransferas |
| [x] | `glpD` | PP_1073 | Q88NY0 | kegg:ppu00564 | PRESENT | CURATED | PRESENT (OpenScientist) | Glycerol-3-phosphate dehydrogenase (quinone) |
| [x] | `glpK` | PP_1075 | Q88NX8 | kegg:ppu00561 | PRESENT | CURATED | PRESENT (Asta) | Glycerol kinase (EC 2.7.1.30) (ATP:glycerol 3-phosphotransferase) (Glycerokinase) (GK) |
| [x] | `glpF` | PP_1076 | Q88NX7 | module:transport_membrane_efflux | PRESENT | CURATED | MISSING | Aquaglyceroporin |
| [ ] | `plsB` | PP_1520 | Q88MQ0 | kegg:ppu00561 | MISSING | MISSING | MISSING | Glycerol-3-phosphate acyltransferase (GPAT) (EC 2.3.1.15) |
| [ ] | `dgkA-I` | PP_1636 | Q88MD7 | kegg:ppu00561 | MISSING | MISSING | MISSING | Diacylglycerol kinase (EC 2.7.1.107) |
| [ ] | `plsC` | PP_1844 | Q88LT3 | kegg:ppu00561 | MISSING | MISSING | MISSING | 1-acyl-sn-glycerol-3-phosphate acyltransferase (EC 2.3.1.51) |
| [ ] | `plsX` | PP_1912 | Q88LL8 | kegg:ppu00561 | MISSING | MISSING | MISSING | Phosphate acyltransferase (EC 2.3.1.274) (Acyl-ACP phosphotransacylase) (Acyl-[acyl-carrier-protein]--phosphate acyltran |
| [ ] | `calA` | PP_2426 | Q88K65 | kegg:ppu00561 | PRESENT | CURATED | MISSING | Coniferyl alcohol dehydrogenase (EC 1.1.1.194) |
| [ ] | `dgkA-II` | PP_2973 | Q88IM6 | kegg:ppu00561 | MISSING | MISSING | MISSING | Diacylglycerol kinase (EC 2.7.1.107) |
| [ ] | `garK` | PP_3178 | Q88I24 | kegg:ppu00561 | MISSING | MISSING | MISSING | Glycerate kinase (EC 2.7.1.165) |
| [ ] | `ttuD` | PP_4300 | Q88F00 | kegg:ppu00561 | MISSING | MISSING | MISSING | Hydroxypyruvate reductase (EC 1.1.1.81) |
| [ ] | `lip` | PP_4854 | Q88DH1 | kegg:ppu00561 | MISSING | MISSING | MISSING | Lipase |

## Notes

The checked rows form the complete uptake-to-dihydroxyacetone-phosphate route.
GlpF and GlpD are cross-bucket members that the broad glycerolipid map does not
partition with the same biological boundary.

Generated UTC: 2026-07-27T01:17:31.970402+00:00
