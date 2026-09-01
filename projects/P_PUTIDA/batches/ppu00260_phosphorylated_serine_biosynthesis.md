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

## Wave108 Repair

- The module remains a reusable, species-neutral three-reaction pathway with
  molecular functions confined to its leaf annotons.
- Each reaction selector now uses the exact PANTHER subfamily shared by its
  PSEPK target and reviewed cross-species exemplar: `PTHR43761:SF1` for SerA,
  `PTHR43247:SF1` for SerC, and `PTHR43344:SF2` for SerB.
- No PTN is asserted. The local PAINT exports identify family-level IBD nodes
  but do not establish that the PSEPK targets descend from those nodes.
- The `serA` secondary R-2-hydroxyglutarate activity is now `UNDECIDED`
  because its target-specific support is automated rather than biochemical.
- The `serC` non-core cytoplasm and PLP-binding decisions now cite exact
  UniProt text. The `serB` cytoplasm annotation is retained as non-core
  phylogenetic context and removed from its core function.
- Two independent annotation-reviewer passes covered all three gene reviews.
  The first identified the unsupported PTN and SerA confidence issues; the
  second found no blocking findings after repair.
- The wave108 module/pathway/PSEPK OpenScientist request was left running for
  the full configured 7,200 seconds. It reached the client timeout without
  returning a report, so no partial or nonexistent provider output is cited.

## Boundary Notes

- `serA` also carries an automated annotation to (R)-2-hydroxyglutarate
  dehydrogenase activity. Its gene-level decision is `UNDECIDED`, and the
  secondary reaction is outside this pathway boundary.
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
