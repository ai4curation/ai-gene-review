---
title: "PSEPK choline uptake and glycine betaine biosynthesis batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK UPA00529: choline uptake and glycine betaine biosynthesis

- Module seed: `bacterial_choline_to_glycine_betaine_biosynthesis`
- Candidate genes from membership table: 3
- Primary bucket genes: 1
- Existing review files: 3
- Curated review files: 3
- Selected module genes: 3
- Selected gene reviews curated: 3
- Selected OpenScientist reports: 1/3

## Curated Boundary

- Required KT2440 proteins: `betT-I`, `betA`, and `betB`.
- BetT-I is not present in the UniPathway table but is included because it
  supplies choline to the adjacent `betIBA` locus.
- `betI` is a transcriptional regulator and is not a metabolic module part.
- The terminal reaction is assigned to dedicated BetB. A possible secondary
  betaine-aldehyde activity of BetA remains unresolved and is not duplicated as
  a required step.
- Direct glycine-betaine uptake, osmotic-stress regulation, and glycine-betaine
  catabolism are outside the boundary.

## Required Workflow

- [x] Curate or update the species-neutral module.
- [ ] Run module-level OpenScientist deep research.
- [x] Run module + pathway + PSEPK OpenScientist deep research.
- [x] Fetch all selected genes with `just fetch-gene PSEPK <gene>`.
- [ ] Run OpenScientist deep research for selected genes.
- [x] Curate each selected gene review.
- [x] Validate module and gene reviews.
- [x] Open one PR for this module/pathway: [#2320](https://github.com/ai4curation/ai-gene-review/pull/2320).
- [ ] Shepherd PR through review, CI, and merge readiness.

2026-07-26: The `betA` OpenScientist report completed. The `betT-I` run
timed out after 7200s without producing a report; the bounded batch did not
start a third sequential gene request.

2026-07-26: The generic module-level OpenScientist run also timed out after
7200s without producing a report.

## Candidate Genes

| Done | Gene | Locus | UniProt | Primary bucket | Existing review | Curation | OpenScientist research | Protein |
|---|---|---|---|---|---|---|---|---|
| [x] | `betT-I` | PP_5061 | Q88CW9 | module:transport_membrane_efflux | PRESENT | CURATED | MISSING | Choline transporter |
| [x] | `betB` | PP_5063 | Q88CW7 | kegg:ppu00670 | PRESENT | CURATED | MISSING | Betaine aldehyde dehydrogenase (BADH) (EC 1.2.1.8) |
| [x] | `betA` | PP_5064 | Q88CW6 | kegg:ppu00670 | PRESENT | CURATED | PRESENT (OpenScientist) | Oxygen-dependent choline dehydrogenase (CDH) (CHD) (EC 1.1.99.1) (Betaine aldehyde dehydrogenase) (BADH) (EC 1.2.1.8) |
| [ ] | `betI` | PP_5719 | A0A140FWS5 | unipathway:UPA00529 | MISSING | MISSING | MISSING | HTH-type transcriptional regulator BetI |

## Notes

The checked rows implement import plus the two oxidation reactions. The
UniPathway bucket captures only the regulatory locus member, so BetT-I, BetA,
and BetB are included explicitly from the curated pathway boundary.

Generated UTC: 2026-07-27T01:17:48.530706+00:00
