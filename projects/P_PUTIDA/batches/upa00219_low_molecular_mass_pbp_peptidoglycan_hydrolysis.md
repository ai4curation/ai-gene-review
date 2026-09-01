---
title: "PSEPK low-molecular-mass PBP peptidoglycan hydrolysis"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
genes: [dacB, pbpG]
autolink_gene_symbols: false
---

# PSEPK low-molecular-mass PBP peptidoglycan hydrolysis

This batch separates two hydrolytic low-molecular-mass PBP reactions:
pentapeptide stem trimming and cleavage of D-Ala-mDAP 4-3 crosslinks. It is
distinct from peptidoglycan polymerization, crosslink formation, and
lipoprotein-peptidoglycan tether remodeling.

## Workflow

- [x] Fetch both PSEPK gene records.
- [x] Complete OpenScientist gene research.
- [x] Curate every GOA row for both genes.
- [x] Create a species-neutral, multi-part module with experimental exemplars.
- [x] Attempt module and module + pathway + taxon research; both OpenScientist jobs reached the 7200-second limit without reports.
- [x] Validate and render the reviews, module, and project page.
- [ ] Open one non-draft PR and clear review and CI.

## Selected Genes

| Done | Gene | Locus | UniProt | Pathway role |
|---|---|---|---|---|
| [x] | `dacB` | PP_2098 | Q88L37 | Bifunctional PBP4, predominantly D,D-endopeptidase |
| [x] | `pbpG` | PP_3794 | Q88GD0 | PBP7 D,D-endopeptidase |

## Boundary Decisions

- D,D-carboxypeptidation and D,D-endopeptidation are separate reaction parts,
  not successive required steps.
- DacB appears in both parts because the close Pseudomonas ortholog performs
  both reactions; PbpG is assigned only to crosslink hydrolysis.
- GO:0009002 is not treated as a synonym for D,D-endopeptidase activity.
- The broad proteolysis annotations are removed because the substrates are
  peptidoglycan stem peptides rather than proteins.

## Provider Outcome

Both long-form OpenScientist requests were allowed to run for the full
configured 7200 seconds on 2026-09-01. The generic module request and the
module + ppu00550 + PSEPK request each timed out and returned no report. No
provider-named file was synthesized manually. The module remains grounded in
the completed dacB and pbpG gene reports, curated UniProt/GOA records,
PANTHER exemplars, and cached primary literature.
