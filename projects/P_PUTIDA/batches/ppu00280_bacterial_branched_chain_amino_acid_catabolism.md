---
title: "PSEPK bacterial branched-chain amino acid catabolism batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
genes: [ilvE, bkdAA, bkdAB, bkdB, lpdV, ivd, mccA, mccB, liuC, mvaB, mmsB, mmsA-II]
autolink_gene_symbols: true
---

# PSEPK bacterial branched-chain amino acid catabolism

This batch curates the bacterial shared entry chemistry and connects it to
substrate-specific downstream routes for KEGG `ppu00280`. The adjacent TSV
records the 12 KT2440 exemplars used to test the reusable module. The source
KEGG bucket contains 35 proteins, but generic fatty-acid oxidation,
acetoacetate activation, 3-oxoadipate CoA transfer, and unassigned thiolase
hits are not promoted to dedicated branched-chain amino-acid roles.

## Required Workflow

- [x] Read the module-curation and annotation-reviewer workflows.
- [x] Inspect the P_PUTIDA worklist, all 35 KEGG members, existing modules,
  and prior BCAA-related pull requests.
- [x] Preserve the human-focused `branched_chain_amino_acid_catabolism` module.
- [x] Reuse the landed distal L-leucine module rather than duplicating its tree.
- [x] Start generic module-level and module + pathway + PSEPK OpenScientist
  research with provider timeout `7200`.
- [x] Audit all touched PSEPK gene reviews annotation by annotation.
- [x] Assess the completed species-aware report and record unavailable generic
  module/gene artifacts without delaying publication.
- [x] Validate and render reviews, module, and project artifacts.
- [x] Open one draft pull request.

## Module Boundary

| Position | KT2440 exemplar(s) | Modeled role | Disposition |
|---|---|---|---|
| shared entry 1 | ilvE / Q88H54 | reversible BCAA transamination | explicit leaf |
| shared entry 2, E1 | bkdAA / Q88EQ2; bkdAB / Q88EQ1 | branched-chain 2-oxoacid decarboxylation | one alpha2-beta2 complex leaf |
| shared entry 2, E2 | bkdB / Q88EQ0 | lipoyl branched-chain acyl transfer to CoA | explicit complex leaf |
| shared entry 2, E3 | lpdV / Q88EP9 | BCKDH-specific lipoyl-arm reoxidation | explicit complex leaf |
| leucine branch | ivd, mccA, mccB, liuC, mvaB | 3-methylbutanoyl-CoA to acetoacetate + acetyl-CoA | delegated to `leucine_catabolism` |
| valine branch | mmsB / Q88E02; mmsA-II / Q88E01 | 3-hydroxyisobutyrate to propionyl-CoA | explicit distal leaves |
| isoleucine branch | unresolved in KT2440 | 2-methylbutanoyl-CoA to propionyl-CoA + acetyl-CoA | chemistry modeled; genes not asserted |

## Biological Decisions

- The module is species-neutral. PSEPK proteins are representative members on
  leaf annotons, not constraints on the reusable pathway.
- No cytoplasm/cytosol term is placed on the module. Compartment is not needed
  to define the bacterial chemistry, and there is no redundant location pair.
- Molecular functions occur only on leaf annotons. The root and downstream
  partition carry biological-process concepts and pathway structure.
- IlvE is modeled as reversible. Its review now recognizes both biosynthetic
  and catabolic flux without claiming that either direction is constitutive.
- The PP_4401-PP_4404 cluster is the pathway-specific BCKDH implementation.
  Direct biochemical evidence summarized for LpdV distinguishes it from the
  housekeeping 2-oxoglutarate-dehydrogenase E3.
- The leucine branch stores only an Ivd gateway exemplar and points to the
  existing four-step `leucine_catabolism` module for the complete reaction
  tree.
- The valine branch exposes MmsB and MmsA-II because their exact records and
  genomic adjacency support consecutive distal reactions. Early bacterial
  hydration/deacylation positions remain unassigned.
- The isoleucine reaction sequence is retained as a branch boundary, but the
  broad KEGG acyl-CoA dehydrogenase, hydratase, dehydrogenase, and thiolase hits
  do not establish KT2440 substrate specificity. This remains an explicit
  knowledge gap.

## Research Provenance

- Existing gene-level OpenScientist reports were reused for ilvE and lpdV.
- Full OpenScientist jobs were started for bkdAA, bkdAB, bkdB, mmsB, and
  mmsA-II with `--timeout 7200`.
- Generic module research targets
  `modules/bacterial_branched_chain_amino_acid_catabolism-deep-research-openscientist.md`.
- Species-aware research targets
  `projects/P_PUTIDA/deep-research/PSEPK__bacterial-branched-chain-amino-acid-catabolism__ppu00280-deep-research-openscientist.md`.
- The species-aware report completed in 972.83 seconds. It supports the small
  dedicated shared core, mmsB-mmsA-II valine assignment, exclusion of about 15
  generic beta-oxidation hits, and the propionyl-CoA/acetyl-CoA boundary. Its
  unresolved PP_3394-versus-MvaB suggestion is not adopted because the landed
  distal leucine curation already selected MvaB after sequence and literature
  review.
- At publication, no BCAA-specific provider process was active and no generic
  module or five additional gene reports had been written. These absent
  artifacts are recorded as `NO_ARTIFACT`; no provider process was stopped or
  awaited.
