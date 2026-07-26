---
title: "PSEPK phosphorylated L-serine biosynthesis batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
genes: [serA, serC, serB]
autolink_gene_symbols: false
---

# PSEPK phosphorylated L-serine biosynthesis

This batch tests the complete three-reaction route from
3-phospho-D-glycerate to L-serine. The 66-gene KEGG `ppu00260` snapshot is
retained in the adjacent TSV, but the module boundary excludes serine
degradation, one-carbon metabolism, glycine cleavage, threonine metabolism,
and phospholipid synthesis.

## Required Workflow

- [x] Fetch the selected PSEPK records from UniProt and GOA.
- [x] Attempt OpenScientist deep research for the selected genes; the corrected
  SerA and SerB requests each exhausted the 7,200-second provider timeout
  without a report.
- [x] Curate the new `serA` and `serB` reviews.
- [x] Reuse the `serC` review from PR #2174 without duplicating its files.
- [x] Create and semantically validate the species-neutral module.
- [x] Run generic module-level OpenScientist research.
- [x] Attempt module + pathway + PSEPK OpenScientist research; the corrected
  request exhausted the 7,200-second provider timeout without a report.
- [x] Validate and render all changed reviews, the module, and project pages.
- [x] Open one non-draft PR for this module:
  [#2236](https://github.com/ai4curation/ai-gene-review/pull/2236).
- [x] Resolve review and CI feedback.

## Selected Genes

| Step | Gene | Locus | UniProt | Role | Review |
|---|---|---|---|---|---|
| 1 | `serA` | PP_5155 | Q88CM5 | phosphoglycerate dehydrogenase | this batch |
| 2 | `serC` | PP_1768 | Q88M07 | phosphoserine aminotransferase | PR #2174 |
| 3 | `serB` | PP_4909 | Q88DB8 | phosphoserine phosphatase | this batch |

## Boundary Notes

- `serA` also carries an inferred (R)-2-hydroxyglutarate dehydrogenase
  activity; that secondary reaction is retained as non-core in its gene
  review but is outside this pathway.
- `serC` also supplies phosphohydroxythreonine aminotransferase chemistry to
  DXP-dependent vitamin B6 synthesis; that is captured by the separate
  vitamin B6 module and does not make this a one-enzyme module.
- The broad KEGG snapshot is provenance for candidate selection, not the
  curated module membership list.
- Generic OpenScientist research independently recovered the same three
  obligatory reaction roles and treated the SerA and SerC secondary
  activities as boundary-excluded chemistry.
- The SerA, SerB, and species-aware requests were each allowed the full
  configured 7,200 seconds with three iterations. No report was returned, so
  no nonexistent source is cited or represented as pathway evidence.
