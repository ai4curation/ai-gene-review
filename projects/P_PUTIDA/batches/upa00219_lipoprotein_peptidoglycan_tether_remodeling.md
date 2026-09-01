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
- [x] Complete OpenScientist gene research or record terminal provider outcome.
- [x] Curate every GOA row for both genes.
- [x] Create a species-neutral, multi-part module with experimental exemplars.
- [x] Complete module research.
- [x] Complete module + pathway + taxon research.
- [x] Validate and render the reviews, module, and project page.
- [x] Open one non-draft PR: [#2847](https://github.com/ai4curation/ai-gene-review/pull/2847).
- [ ] Clear review and CI.

## Selected Genes

| Done | Gene | Locus | UniProt | Pathway role |
|---|---|---|---|---|
| [x] | `PP_2320` | PP_2320 | Q88KH0 | ErfK-family OprI anchoring L,D-transpeptidase |
| [x] | `PP_1451` | PP_1451 | Q88MW7 | YafK/LdtF-family OprI-tether hydrolase; OpenScientist timed out after 7200 seconds |

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
- The generic module report is useful for the conserved write/erase architecture
  but is strongly centered on enterobacterial Lpp. Its Lpp-specific
  C-terminal-lysine chemistry is not projected onto the Pseudomonas OprI
  system.
- None of the 23 genes supplied from the KEGG `ppu00550` neighborhood represents
  either tether enzyme or the OprI substrate. `PP_2320`, `PP_1451`, and `oprI`
  (`PP_2322`) are therefore retained as a literature- and orthology-supported
  module outside the KEGG peptidoglycan-biosynthesis gene set.
- The taxon-specific OpenScientist report classified `PP_1451` as uncertain
  from low-sensitivity k-mer and local-alignment comparisons. Exact
  PTHR36699:SF1 membership instead groups PP_1451 with PA14
  LdtPae3/A0A0H2ZF55 and experimentally characterized E. coli
  DpaA/LdtF/P0AA99; the review records why this family-level evidence
  supersedes the report's candidate call while retaining the absence of a
  direct KT2440 assay as an open gap.
- The gene-level OpenScientist request for `PP_1451` reached the configured
  7200-second provider limit and returned no report. The review therefore
  remains grounded in UniProt, exact PANTHER-subfamily correspondence,
  PAINT, PMID:37255442, PMID:33941679, and PMID:33947763; no provider file was
  synthesized manually.

## 2026-09-01 review follow-up

- Added the two direct E. coli DpaA/LdtF papers, PMID:33941679 and
  PMID:33947763, and the reviewed P0AA99 protein as an experimental exemplar.
- Resolved the PA14 experimental proteins by locus: PA14_27180/LdtPae2 is
  A0A0H2ZCT9 and PA14_15840/LdtPae3 is A0A0H2ZF55. Added the independently
  validated PAO1 PA2854/Q9HZZ0 anchoring exemplar.
- Revised PP_1451 from carboxypeptidase activity to PAINT-supported
  GO:0004175 endopeptidase activity, removed the contradicted peptidoglycan
  biosynthesis annotation, and changed signal-peptide localization evidence
  from ISS to ISM.
