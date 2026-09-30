---
title: "PSEPK aerobic nicotinate degradation batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK UPA01010: aerobic nicotinate degradation

- Module seed: `aerobic_nicotinate_degradation`
- Candidate genes from membership table: 9
- Primary bucket genes: 2
- Existing review files: 9
- Curated review files: 9
- Selected module genes: 7
- Selected gene reviews curated: 7
- Selected gene research: Falcon (7/7)

## Curated Boundary

- Required reactions: `nicA`-`nicB`, `nicC`, `nicX`, `nicD`, `nicF`, and `maiA`.
- `nicA` and `nicB` form one nicotinate dehydrogenase activity and are not
  separate pathway reactions.
- `nicR` and `nicS` are locus regulators and remain outside the metabolic
  module.
- The module ends at fumarate formation; fumarate utilization and respiratory
  electron-transfer partners are outside the boundary.

## Required Workflow

- [x] Curate or update the species-neutral module.
- [ ] Run module-level OpenScientist deep research.
- [ ] Run module + pathway + PSEPK OpenScientist deep research.
- [x] Fetch all selected genes with `just fetch-gene PSEPK <gene>`.
- [x] Review the existing Falcon deep-research reports for selected genes.
- [x] Curate each selected gene review.
- [x] Re-audit all seven selected reviews as annotation reviewer.
- [x] Validate module and gene reviews.
- [x] Open one PR for this module/pathway: [#2325](https://github.com/ai4curation/ai-gene-review/pull/2325).
- [x] Shepherd PR through review, CI, and merge readiness; PR #2325 is merged.

2026-07-26: OpenScientist timed out after 7200s for the module + pathway +
PSEPK report; no report file was produced.

2026-07-26: The generic module-level OpenScientist run also timed out after
7200s without producing a report.

2026-08-13: Fresh OpenScientist retries for the seven genes, the generic
module, and the module + `ppu00760` + PSEPK combination returned no artifacts.
They were not restarted during annotation review. The existing PSEPK
`ppu00760` OpenScientist synthesis was inspected, but it models NAD+
biosynthesis/salvage and explicitly excludes nicotinate degradation; it
therefore supports separation of these boundaries rather than the chemistry of
this catabolic module.

2026-08-13: Annotation re-review retained the GOA-sourced `enables` relations
for NicA and NicB while recording complex-level contribution semantics in the
core functions. It also replaced broad monooxygenase retention with
specific-term modifications for NicC, treated MaiA oligomerization as
unresolved, and replaced overbroad pathway selectors with
reaction-constrained ortholog selectors. PR #2571 records this refinement of
the canonical module.

## Candidate Genes

| Done | Gene | Locus | UniProt | Primary bucket | Existing review | Curation | Gene research | Protein |
|---|---|---|---|---|---|---|---|---|
| [x] | `nicF` | PP_3941 | Q88FY5 | kegg:ppu00760 | PRESENT | CURATED | PRESENT (Falcon) | Maleamate amidohydrolase (EC 3.5.1.107) (Nicotinate degradation protein F) |
| [x] | `maiA` | PP_3942 | Q88FY4 | kegg:ppu00760 | PRESENT | CURATED | PRESENT (Falcon) | Maleate isomerase (EC 5.2.1.1) (Maleate cis-trans isomerase) (Nicotinate degradation protein E) |
| [x] | `nicD` | PP_3943 | Q88FY3 | kegg:ppu00760 | PRESENT | CURATED | PRESENT (Falcon) | N-formylmaleamate deformylase (EC 3.5.1.106) (Nicotinate degradation protein D) |
| [x] | `nicC` | PP_3944 | Q88FY2 | kegg:ppu00760 | PRESENT | CURATED | PRESENT (Falcon) | 6-hydroxynicotinate 3-monooxygenase (6-HNA monooxygenase) (EC 1.14.13.114) (Nicotinate degradation protein C) |
| [x] | `nicX` | PP_3945 | Q88FY1 | kegg:ppu00760 | PRESENT | CURATED | PRESENT (Falcon) | 2,5-dihydroxypyridine 5,6-dioxygenase (2,5-DHP dioxygenase) (EC 1.13.11.9) (Nicotinate degradation protein X) |
| [ ] | `nicR` | PP_3946 | Q88FY0 | unipathway:UPA01010 | PRESENT | CURATED | MISSING | HTH-type transcriptional repressor NicR (Nicotinate degradation protein R) |
| [x] | `nicA` | PP_3947 | Q88FX9 | kegg:ppu00760 | PRESENT | CURATED | PRESENT (Falcon) | Nicotinate dehydrogenase subunit A (EC 1.17.2.1) (Nicotinate degradation protein A) (Nicotinate dehydrogenase small subu |
| [x] | `nicB` | PP_3948 | Q88FX8 | kegg:ppu00760 | PRESENT | CURATED | PRESENT (Falcon) | Nicotinate dehydrogenase subunit B (EC 1.17.2.1) (Nicotinate degradation protein B) (Nicotinate dehydrogenase large subu |
| [ ] | `nicS` | PP_3949 | Q88FX7 | unipathway:UPA01010 | PRESENT | CURATED | MISSING | HTH-type transcriptional repressor NicS (Nicotinate degradation protein S) |

## Notes

The seven checked genes implement six consecutive reactions from nicotinate to
fumarate. `nicR` and `nicS` remain in the candidate partition as
transcriptional regulators but are not catalytic module parts.

Generated UTC: 2026-07-27T01:15:55.508594+00:00
