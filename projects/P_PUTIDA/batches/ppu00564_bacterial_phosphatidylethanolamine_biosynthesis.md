---
title: "PSEPK ppu00564 phosphatidylethanolamine biosynthesis"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK ppu00564: phosphatidylethanolamine biosynthesis through phosphatidylserine

- Module seed: `bacterial_phosphatidylethanolamine_biosynthesis`
- Candidate genes from membership table: 23
- Primary bucket genes: 17
- Existing review files: 4
- Curated review files: 4
- Selected module genes: 3
- Selected gene reviews curated: 3
- Selected OpenScientist reports: 3/3 complete

## Curated Boundary

- Required reactions: phosphatidylserine formation followed by `psd`-dependent
  decarboxylation.
- KT2440 encodes two phosphatidylserine-synthase candidates, class-I `pssA`
  (PP_3664) and class-II `PP_4677`; either architecture can satisfy the first
  reaction, and their relative in-vivo contributions are unresolved.
- `psd` (PP_4908) performs the terminal phosphatidylethanolamine-forming step.
- CDP-diacylglycerol supply, phosphatidylglycerol/cardiolipin branches,
  acyl-chain remodeling, and alternative Kennedy-type routes are outside the
  two-reaction module.

## 2026-09-01 Repair Decisions

- The reusable module retains two ordered reactions and models type-I and
  type-II PssA as alternatives within the phosphatidylserine-forming step.
  Molecular functions remain on the three leaf annotons.
- The KT2440-specific question about the relative flux through Q88GQ4 and
  Q88DZ1 belongs here, not in the reusable module's knowledge gaps.
- The heterogeneous PTHR12586 family is constrained by the verified
  `PTN001758495` phosphatidylserine-synthase node. The type-II role uses the
  serine-specific InterPro family because no functionally equivalent PAINT
  node was established. The Psd role uses the verified PTHR10067 parent family
  rather than its misleading mitochondria-named subfamily label.
- Current GOA coverage is complete: `pssA` 6/6, `PP_4677` 4/4, and `psd` 4/4,
  with no PENDING actions. The broad `PP_4677` membrane row is `MODIFY` to
  plasma membrane rather than being retained alongside a redundant NEW row.

## Required Workflow

- [x] Curate or update the species-neutral module.
- [x] Run module-level OpenScientist deep research.
- [x] Run module + pathway + PSEPK OpenScientist deep research.
- [x] Fetch all selected genes with `just fetch-gene PSEPK <gene>`.
- [x] Run OpenScientist deep research for selected genes.
- [x] Curate each selected gene review.
- [x] Validate module and gene reviews.
- [x] Open one PR for this module/pathway: [#2323](https://github.com/ai4curation/ai-gene-review/pull/2323).
- [ ] Shepherd PR through review, CI, and merge readiness.

2026-07-26: OpenScientist reports completed for `pssA` and `psd`.
The `PP_4677` request timed out after 7200s without producing a report.

2026-07-26: The generic module-level OpenScientist run timed out after 7200s
without producing a report.

2026-09-01: The repair pass completed the missing generic module report in
1153.78s and the missing `PP_4677` gene report in 1508.52s. Earlier attempts
remained queued after client-side DNS polling failures and were not cancelled.
The completed reports were reviewed as retrieval support; family class-I
terminology in the gene report was reconciled with bacterial PssA type-II
nomenclature rather than copied into the curated model.

## Candidate Genes

| Done | Gene | Locus | UniProt | Primary bucket | Existing review | Curation | OpenScientist research | Protein |
|---|---|---|---|---|---|---|---|---|
| [ ] | `PP_0058` | PP_0058 | Q88RS1 | kegg:ppu00561 | MISSING | MISSING | MISSING | 1-acyl-sn-glycerol-3-phosphate acyltransferase |
| [ ] | `plsY` | PP_0391 | Q88QU5 | kegg:ppu00561 | MISSING | MISSING | MISSING | Glycerol-3-phosphate acyltransferase (Acyl-PO4 G3P acyltransferase) (Acyl-phosphate--glycerol-3-phosphate acyltransferas |
| [ ] | `pgpA` | PP_0520 | Q88QH3 | kegg:ppu00564 | MISSING | MISSING | MISSING | Phosphatidylglycerophosphatase A (EC 3.1.3.27) (Phosphatidylglycerolphosphate phosphatase A) |
| [ ] | `eutC` | PP_0542 | Q88QF2 | kegg:ppu00564 | MISSING | MISSING | MISSING | Ethanolamine ammonia-lyase small subunit (EAL small subunit) (EC 4.3.1.7) |
| [ ] | `eutB` | PP_0543 | Q88QF1 | kegg:ppu00564 | MISSING | MISSING | MISSING | Ethanolamine ammonia-lyase large subunit (EAL large subunit) (EC 4.3.1.7) |
| [ ] | `pcs` | PP_0731 | Q88PW7 | kegg:ppu00564 | MISSING | MISSING | MISSING | Phosphatidylcholine synthase (EC 2.7.8.24) |
| [ ] | `PP_0892` | PP_0892 | Q88PF8 | kegg:ppu00564 | MISSING | MISSING | MISSING | Phospholipase family protein |
| [ ] | `glpD` | PP_1073 | Q88NY0 | kegg:ppu00564 | MISSING | MISSING | MISSING | Glycerol-3-phosphate dehydrogenase (EC 1.1.5.3) |
| [ ] | `plsB` | PP_1520 | Q88MQ0 | kegg:ppu00561 | MISSING | MISSING | MISSING | Glycerol-3-phosphate acyltransferase (GPAT) (EC 2.3.1.15) |
| [ ] | `cdsA` | PP_1596 | Q88MH5 | kegg:ppu00564 | MISSING | MISSING | MISSING | Phosphatidate cytidylyltransferase (EC 2.7.7.41) |
| [ ] | `dgkA-I` | PP_1636 | Q88MD7 | kegg:ppu00561 | MISSING | MISSING | MISSING | Diacylglycerol kinase (EC 2.7.1.107) |
| [ ] | `plsC` | PP_1844 | Q88LT3 | kegg:ppu00561 | MISSING | MISSING | MISSING | 1-acyl-sn-glycerol-3-phosphate acyltransferase (EC 2.3.1.51) |
| [ ] | `ugpQ` | PP_2152 | Q88KY7 | kegg:ppu00564 | MISSING | MISSING | MISSING | Glycerophosphoryl diester phosphodiesterase (EC 3.1.4.46) |
| [ ] | `dgkA-II` | PP_2973 | Q88IM6 | kegg:ppu00561 | MISSING | MISSING | MISSING | Diacylglycerol kinase (EC 2.7.1.107) |
| [ ] | `clsB` | PP_3264 | Q88HT9 | kegg:ppu00564 | MISSING | MISSING | MISSING | Cardiolipin synthase B (CL synthase) (EC 2.7.8.-) |
| [x] | `pssA` | PP_3664 | Q88GQ4 | kegg:ppu00564 | PRESENT | CURATED | PRESENT | CDP-diacylglycerol--serine O-phosphatidyltransferase (EC 2.7.8.8) |
| [ ] | `pgsA` | PP_4097 | Q88FJ8 | kegg:ppu00564 | MISSING | MISSING | MISSING | CDP-diacylglycerol--glycerol-3-phosphate 3-phosphatidyltransferase (EC 2.7.8.5) |
| [ ] | `gpsA` | PP_4169 | Q88FC9 | kegg:ppu00564 | PRESENT | CURATED | MISSING | Glycerol-3-phosphate dehydrogenase [NAD(P)+] (EC 1.1.1.94) (NAD(P)(+)-dependent glycerol-3-phosphate dehydrogenase) (NAD |
| [x] | `PP_4677` | PP_4677 | Q88DZ1 | kegg:ppu00564 | PRESENT | CURATED | PRESENT | CDP-diacylglycerol--serine O-phosphatidyltransferase (EC 2.7.8.8) (Phosphatidylserine synthase) |
| [x] | `psd` | PP_4908 | Q88DB9 | kegg:ppu00564 | PRESENT | CURATED | PRESENT | Phosphatidylserine decarboxylase proenzyme (EC 4.1.1.65) [Cleaved into: Phosphatidylserine decarboxylase alpha chain; Ph |
| [ ] | `pchP` | PP_5130 | Q88CQ0 | kegg:ppu00564 | MISSING | MISSING | MISSING | Phosphoethanolamine/phosphocholine phosphatase (EC 3.1.3.75) |
| [ ] | `PP_5276` | PP_5276 | Q88CA5 | kegg:ppu00564 | MISSING | MISSING | MISSING | Phospholipase D family protein |
| [ ] | `clsA` | PP_5364 | Q88C19 | kegg:ppu00564 | MISSING | MISSING | MISSING | Cardiolipin synthase A (CL synthase) (EC 2.7.8.-) |

## Notes

The resolved module/pathway/taxon report finds both reactions covered and
supports the two mechanistically distinct PssA candidates. Their relative
physiological contribution, rather than pathway satisfiability, remains the
open question.

Generated UTC: 2026-07-27T01:18:05.538159+00:00
