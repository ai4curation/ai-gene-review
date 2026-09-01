---
title: "PSEPK lipoprotein-peptidoglycan tether remodeling"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
genes: [PP_1451, PP_2320]
autolink_gene_symbols: false
---

# PSEPK lipoprotein-peptidoglycan tether remodeling

This batch tests a two-reaction envelope-remodeling module: covalent anchoring
of the major outer-membrane lipoprotein OprI to peptidoglycan and hydrolytic
release of that tether. It is separated from glycan polymerization, canonical
4-3 peptide crosslinking, and low-molecular-mass PBP hydrolysis.

## Workflow

- [x] Fetch both PSEPK gene records.
- [ ] Complete OpenScientist gene research.
- [ ] Curate every GOA row for both genes.
- [x] Create a species-neutral, multi-part module with experimental exemplars.
- [ ] Complete module and module + pathway + taxon research.
- [ ] Validate and render the reviews, module, and project page.
- [ ] Open one non-draft PR and clear review and CI.

## Selected Genes

| Done | Gene | Locus | UniProt | Pathway role |
|---|---|---|---|---|
| [ ] | `PP_2320` | PP_2320 | Q88KH0 | ErfK-family OprI anchoring L,D-transpeptidase |
| [ ] | `PP_1451` | PP_1451 | Q88MW7 | YafK/LdtF-family OprI-tether hydrolase |

## Boundary Decisions

- `PP_2320` and `PP_1451` are not treated as interchangeable generic YkuD
  proteins. Their exact PANTHER subfamilies match experimentally distinguished
  Pseudomonas aeruginosa anchoring and release enzymes, respectively.
- The two reactions are modeled as distinct parts connected through the
  covalent lipoprotein-peptidoglycan tether.
- `dacB` and `pbpG` cleave 4-3 peptidoglycan crosslinks through low-molecular-
  mass PBP chemistry and belong in a separate remodeling module.
- No molecular-function identifier is asserted for tether hydrolysis because
  GO does not currently provide a term for that reaction.
