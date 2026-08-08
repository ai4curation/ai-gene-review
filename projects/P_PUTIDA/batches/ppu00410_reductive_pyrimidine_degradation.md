---
title: "PSEPK ppu00410 reductive pyrimidine degradation"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK ppu00410: reductive pyrimidine degradation

- Module seed: `pyrimidine_degradation`
- Candidate genes from membership table: 15
- Primary bucket genes: 10
- Existing review files: 7
- Curated review files: 7
- Selected module genes: 4
- Selected gene reviews curated: 4
- Selected OpenScientist reports: 1 of 4 (`pydX`)

## Curated Boundary

- Required KT2440 candidates: the `pydA`-`pydX` reductase complex, `pydB`, and
  `hyuC`.
- The species-neutral module records the human DPYD, DPYS, and UPB1 route as a
  taxonomic alternative.
- The HyuC-family terminal assignment remains biologically uncertain because
  its seeded allantoate-deiminase annotation conflicts with the expected
  beta-ureidopropionase step.
- Pyrimidine biosynthesis, salvage, oxidation, and downstream propionyl-CoA
  metabolism are outside the boundary.

## Required Workflow

- [x] Curate or update the species-neutral module.
- [ ] Run module-level OpenScientist deep research.
- [ ] Run module + pathway + PSEPK OpenScientist deep research.
- [x] Fetch all selected genes with `just fetch-gene PSEPK <gene>`.
- [ ] Run OpenScientist deep research for selected genes.
- [x] Curate each selected gene review.
- [x] Validate module and gene reviews.
- [x] Open one PR for this module/pathway: [#2319](https://github.com/ai4curation/ai-gene-review/pull/2319).
- [ ] Shepherd PR through review, CI, and merge readiness.

2026-07-26: OpenScientist timed out after 7200s for the module + pathway +
PSEPK report; no report file was produced.

2026-07-26: The generic module-level OpenScientist run also timed out after
7200s without producing a report.

2026-07-26: The `pydA` gene-level run timed out after 7200s with no report.
The `pydX` run persisted a complete report and artifacts despite the wrapper
returning a timeout status. Its PydX/PydA subunit assignment was reconciled;
its explicitly noted FAD-versus-FMN ambiguity remains unresolved.

## Candidate Genes

| Done | Gene | Locus | UniProt | Primary bucket | Existing review | Curation | OpenScientist research | Protein |
|---|---|---|---|---|---|---|---|---|
| [ ] | `PP_0596` | PP_0596 | Q88Q98 | kegg:ppu00410 | MISSING | MISSING | MISSING | Omega-amino acid--pyruvate aminotransferase (EC 2.6.1.18) |
| [ ] | `mmsA-I` | PP_0597 | Q88Q97 | kegg:ppu00562 | MISSING | MISSING | MISSING | methylmalonate-semialdehyde dehydrogenase (CoA acylating) (EC 1.2.1.27) |
| [ ] | `PP_0614` | PP_0614 | Q88Q81 | kegg:ppu00410 | MISSING | MISSING | MISSING | N-carbamoyl-beta-alanine amidohydrolase/allantoine amidohydrolase 1 (EC 3.5.1.6, EC 3.5.3.9) |
| [ ] | `patD` | PP_1481 | Q88MT7 | kegg:ppu00410 | MISSING | MISSING | MISSING | Medium chain aldehyde dehydrogenase (EC 1.2.1.19, EC 1.2.1.54) |
| [ ] | `fadB` | PP_2136 | Q88L02 | kegg:ppu00930 | PRESENT | CURATED | MISSING | Fatty acid oxidation complex subunit alpha [Includes: Enoyl-CoA hydratase/Delta(3)-cis-Delta(2)-trans-enoyl-CoA isomeras |
| [ ] | `acd` | PP_2216 | Q88KS3 | kegg:ppu00410 | MISSING | MISSING | MISSING | 3-sulfinopropanoyl-CoA desulfinase (EC 1.3.8.11) (EC 3.13.1.4) (3-sulfinopropionyl coenzyme A desulfinase) (Cyclohexane- |
| [ ] | `PP_2217` | PP_2217 | Q88KS2 | kegg:ppu00930 | MISSING | MISSING | MISSING | enoyl-CoA hydratase (EC 4.2.1.17) |
| [ ] | `prr` | PP_2801 | Q88J48 | kegg:ppu00410 | MISSING | MISSING | MISSING | Gamma-aminobutyraldehyde dehydrogenase (EC 1.2.1.19) |
| [ ] | `paaF` | PP_3284 | Q88HR9 | kegg:ppu00930 | PRESENT | CURATED | PRESENT | Enoyl-CoA hydratase-isomerase (EC 4.2.1.17) |
| [x] | `hyuC` | PP_4034 | Q88FQ3 | kegg:ppu00410 | PRESENT | CURATED | MISSING | N-carbamoyl-beta-alanine amidohydrolase/allantoine amidohydrolase 2 (EC 3.5.1.6, EC 3.5.3.9) |
| [x] | `pydB` | PP_4036 | A0A140FWK2 | kegg:ppu00410 | PRESENT | CURATED | MISSING | D-hydantoinase/dihydropyrimidinase (EC 3.5.2.2) |
| [x] | `pydX` | PP_4037 | Q88FQ1 | kegg:ppu00410 | PRESENT | CURATED | PRESENT (OpenScientist) | dihydrouracil dehydrogenase (NAD(+)) (EC 1.3.1.1) (Dihydrothymine dehydrogenase) (Dihydrouracil dehydrogenase) |
| [x] | `pydA` | PP_4038 | Q88FQ0 | kegg:ppu00410 | PRESENT | CURATED | MISSING | dihydrouracil dehydrogenase (NAD(+)) (EC 1.3.1.1) (Dihydrothymine dehydrogenase) (Dihydrouracil dehydrogenase) |
| [ ] | `mmsA-II` | PP_4667 | Q88E01 | kegg:ppu00562 | MISSING | MISSING | MISSING | methylmalonate-semialdehyde dehydrogenase (CoA acylating) (EC 1.2.1.27) |
| [ ] | `panC` | PP_4700 | Q88DW8 | kegg:ppu00410 | PRESENT | CURATED | PRESENT | Pantothenate synthetase (PS) (EC 6.3.2.1) (Pantoate--beta-alanine ligase) (Pantoate-activating enzyme) |

## Notes

The checked rows implement the three-reaction reductive pathway. PydA and PydX
are two subunits of the first reductase activity, and HyuC remains explicitly
flagged as the least certain terminal assignment.

Generated UTC: 2026-07-27T01:17:17.150311+00:00
