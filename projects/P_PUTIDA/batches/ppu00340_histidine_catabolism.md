---
title: "PSEPK ppu00340 histidine catabolism batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK ppu00340: histidine catabolism to glutamate

- Module seed: `histidine_catabolism`
- Candidate genes from membership table: 20
- Primary bucket genes: 18
- Existing review files: 18
- Curated review files: 18
- Selected module genes: 5
- Selected gene reviews curated: 5
- Selected OpenScientist reports: 1 of 5 (`hutU`)

## Curated Boundary

- Required PSEPK realization: `hutH`, `hutU`, `hutI`, `hutF`, and `hutG`.
- The first three reactions produce formiminoglutamate; the PSEPK two-step
  `hutF`-`hutG` route then releases formate and glutamate.
- The one-step formamide and folate-coupled terminal chemistries are reusable
  route variants, not PSEPK gene requirements. Their exemplars do not restrict
  the module's taxonomic scope.
- Histidine biosynthesis, histidyl-tRNA charging, and unrelated histidine
  modification genes in the KEGG map are outside the boundary.

## Required Workflow

- [x] Curate or update the species-neutral module.
- [x] Run module-level OpenScientist deep research.
- [x] Run module + pathway + PSEPK OpenScientist deep research.
- [x] Fetch all selected genes with `just fetch-gene PSEPK <gene>`.
- [x] Run bounded OpenScientist deep research for high-priority selected genes
  and record incomplete runs.
- [x] Curate each selected gene review.
- [x] Validate module and gene reviews.
- [x] Open one PR for this module/pathway: [#2329](https://github.com/ai4curation/ai-gene-review/pull/2329).
- [ ] Shepherd PR through review, CI, and merge readiness.

2026-07-26: OpenScientist timed out after 7200s for the module + pathway +
PSEPK report; no report file was produced.

2026-07-26: The generic module-level OpenScientist run also timed out after
7200s without producing a report.

2026-07-26: The `hutH` gene-level run timed out after 7200s with no report.
The `hutU` run persisted a complete report and artifacts; its direct
same-species urocanase claims were reconciled against four cached primary
publication abstracts. The remaining three selected genes have no provider
report in this bounded first pass; HutF and HutG additionally use the cached
same-species hut-locus paper, while HutI retains UniProt and family-level
evidence.

2026-09-01 repair checkpoint: Both OpenScientist reruns completed within the
7200s allowance. The module is now explicitly chemistry-defined rather than
taxon-defined. Terminal-route selection is `ONE_OR_MORE` as a conservative
relaxation: the generic report generally expects one route but leaves
coexistence unresolved, so the module asserts neither exclusivity nor parallel
route occurrence. The one-step formimidoylglutamase exemplar P42068 is
represented by the exact verified `PTHR11358:SF35` subfamily, while
function-specific `InterPro:IPR005923` is retained as complementary evidence;
uncertain HutF/HutG PANTHER or PTN assertions remain omitted.
Annotation-reviewer audit confirmed the five selected catalytic reviews require
no conservative changes, and `hutT` remains outside the chemistry module.
Module schema and semantic validation pass; the semantic check retains only the
expected advisory that InterPro labels are not ontology-validated. The `hutH`,
`hutU`, `hutI`, `hutF`, `hutG`, and boundary `hutT` reviews also validate, and
the changed module and batch outputs were rendered. Repair PR:
[#2881](https://github.com/ai4curation/ai-gene-review/pull/2881).

## Candidate Genes

| Done | Gene | Locus | UniProt | Primary bucket | Existing review | Curation | OpenScientist research | Protein |
|---|---|---|---|---|---|---|---|---|
| [ ] | `gshA` | PP_0243 | Q88R90 | kegg:ppu00340 | MISSING | MISSING | MISSING | Glutamate--cysteine ligase (EC 6.3.2.2) (Gamma-ECS) (GCS) (Gamma-glutamylcysteine synthetase) |
| [ ] | `hisB` | PP_0289 | Q88R45 | kegg:ppu00340 | PRESENT | CURATED | PRESENT | Imidazoleglycerol-phosphate dehydratase (IGPD) (EC 4.2.1.19) |
| [ ] | `hisH` | PP_0290 | Q88R44 | kegg:ppu00340 | PRESENT | CURATED | PRESENT | Imidazole glycerol phosphate synthase subunit HisH (EC 4.3.2.10) (IGP synthase glutaminase subunit) (EC 3.5.1.2) (IGP sy |
| [ ] | `hisA` | PP_0292 | Q88R42 | kegg:ppu00340 | PRESENT | CURATED | PRESENT | 1-(5-phosphoribosyl)-5-[(5-phosphoribosylamino)methylideneamino] imidazole-4-carboxamide isomerase (EC 5.3.1.16) (Phosph |
| [ ] | `hisF` | PP_0293 | Q88R41 | kegg:ppu00340 | PRESENT | CURATED | MISSING | Imidazole glycerol phosphate synthase subunit HisF (EC 4.3.2.10) (IGP synthase cyclase subunit) (IGP synthase subunit Hi |
| [ ] | `hisG` | PP_0965 | Q88P87 | kegg:ppu00340 | PRESENT | CURATED | PRESENT | ATP phosphoribosyltransferase (ATP-PRT) (ATP-PRTase) (EC 2.4.2.17) |
| [ ] | `hisD` | PP_0966 | P59400 | kegg:ppu00340 | PRESENT | CURATED | PRESENT | Histidinol dehydrogenase (HDH) (EC 1.1.1.23) |
| [ ] | `hisC` | PP_0967 | Q88P86 | kegg:ppu00401 | PRESENT | CURATED | PRESENT | Histidinol-phosphate aminotransferase (EC 2.6.1.9) (Imidazole acetol-phosphate transaminase) |
| [ ] | `PP_1721` | PP_1721 | Q88M53 | kegg:ppu00340 | MISSING | MISSING | MISSING | Phosphoserine phosphatase (EC 3.1.3.-) |
| [ ] | `PP_3157` | PP_3157 | Q88I44 | kegg:ppu00340 | PRESENT | CURATED | PRESENT | Histidinol-phosphatase (EC 3.1.3.15) |
| [ ] | `hisZ` | PP_4890 | Q88DD7 | kegg:ppu00340 | PRESENT | CURATED | PRESENT | ATP phosphoribosyltransferase regulatory subunit |
| [ ] | `PP_4983` | PP_4983 | Q88D45 | kegg:ppu00350 | PRESENT | CURATED | MISSING | Tryptophan 2-monooxygenase (EC 1.13.12.3) |
| [ ] | `hisI` | PP_5014 | Q88D15 | kegg:ppu00340 | PRESENT | CURATED | PRESENT | Phosphoribosyl-AMP cyclohydrolase (PRA-CH) (EC 3.5.4.19) |
| [ ] | `hisE` | PP_5015 | Q88D14 | kegg:ppu00340 | PRESENT | CURATED | MISSING | Phosphoribosyl-ATP pyrophosphatase (PRA-PH) (EC 3.6.1.31) |
| [x] | `hutG` | PP_5029 | Q88D00 | kegg:ppu00340 | PRESENT | CURATED | MISSING | N-formylglutamate deformylase (EC 3.5.1.68) |
| [x] | `hutI` | PP_5030 | Q88CZ9 | kegg:ppu00340 | PRESENT | CURATED | MISSING | Imidazolonepropionase (EC 3.5.2.7) (Imidazolone-5-propionate hydrolase) |
| [x] | `hutH` | PP_5032 | Q88CZ7 | kegg:ppu00340 | PRESENT | CURATED | MISSING | Histidine ammonia-lyase (Histidase) (EC 4.3.1.3) |
| [x] | `hutU` | PP_5033 | Q88CZ6 | kegg:ppu00340 | PRESENT | CURATED | PRESENT (OpenScientist) | Urocanate hydratase (Urocanase) (EC 4.2.1.49) (Imidazolonepropionate hydrolase) |
| [x] | `hutF` | PP_5036 | Q88CZ3 | kegg:ppu00340 | PRESENT | CURATED | MISSING | Formimidoylglutamate deiminase (EC 3.5.3.13) |
| [ ] | `PP_5147` | PP_5147 | Q88CN3 | kegg:ppu00340 | PRESENT | CURATED | PRESENT | Histidinol-phosphatase (EC 3.1.3.15) (Histidinol-phosphate phosphatase) |

## Notes

Checked rows are the five Hut proteins required by the PSEPK two-step route.
Histidine-biosynthesis enzymes remain visible as excluded candidates from the
broader KEGG map.

Generated UTC: 2026-07-27T01:16:09.666264+00:00
