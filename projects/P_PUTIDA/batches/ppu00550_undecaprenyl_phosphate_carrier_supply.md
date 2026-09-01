---
title: "PSEPK undecaprenyl-phosphate carrier supply"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
genes: [uppS, uppP]
autolink_gene_symbols: false
---

# PSEPK undecaprenyl-phosphate carrier supply

This batch covers synthesis of undecaprenyl diphosphate and its conversion to
the undecaprenyl-phosphate carrier used by multiple cell-envelope glycan
pathways. It is separated from pathway-specific lipid I/lipid II synthesis,
glycan polymerization, and peptide crosslinking.

## Workflow

- [x] Fetch both PSEPK gene records.
- [x] Complete OpenScientist gene research (uppP completed; uppS reached the 7200-second limit without a report).
- [x] Curate every GOA row for both genes.
- [x] Create a species-neutral, multi-part module with exact UniProt exemplars.
- [x] Complete module and module + pathway + taxon research (taxon review completed; generic module research reached the 7200-second limit without a report).
- [ ] Validate and render the reviews, module, and project page.
- [ ] Open one non-draft PR and clear review and CI.

## Selected Genes

| Done | Gene | Locus | UniProt | Pathway role |
|---|---|---|---|---|
| [x] | `uppS` | PP_1595 | Q88MH6 | C55 undecaprenyl-diphosphate synthesis |
| [x] | `uppP` | PP_2862 | Q88IY7 | C55-PP dephosphorylation and carrier-pool maintenance |

## Boundary Decisions

- The product C55-P is shared by peptidoglycan, lipopolysaccharide, and other
  envelope-glycan pathways, so this is a carrier-supply module rather than a
  peptidoglycan-only module.
- `mraY`, `murG`, and `murJ` own pathway-specific lipid I/lipid II synthesis
  and export in the existing peptidoglycan-precursor module.
- SEDS proteins and PBPs own downstream peptidoglycan polymerization and
  crosslinking.
- The UppS PANTHER subfamily identifier is omitted from the module because its
  official label describes eukaryotic dehydrodolichyl diphosphate synthase 2,
  despite containing the exact bacterial UppS exemplars. Exact UniProt
  exemplars are retained instead of relabeling or guessing a family ID.
- Species-aware research confirms both canonical steps are present but finds
  probable asymmetry in redundancy: UppS appears single-copy, whereas
  PP_0251, PP_0900, and PP_4813 are PAP2-family candidates that may overlap
  UppP activity.
- Those PAP2 candidates remain candidate-uncertain; broad PAP2 membership is
  not sufficient to assign GO:0050380 because family members can prefer
  glycerophospholipid or LPS substrates.
- No direct KT2440 biochemical or genetic evidence was found for either
  canonical protein. Ortholog-derived periplasm-facing UppP catalysis and a
  proposed flippase role are not promoted to core-function assertions.

## Provider Outcome

The UppS gene request and generic module request were each allowed to run for
the full configured 7200 seconds on 2026-09-01. Both timed out without reports.
No provider-named files were synthesized manually. The module remains grounded
in the completed UppP report, the species-aware pathway review, exact UniProt
records, GO terms, and verified family exemplars.
