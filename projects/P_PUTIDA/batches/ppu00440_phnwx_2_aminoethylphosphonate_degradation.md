---
title: "PSEPK ppu00440 PhnWX 2-aminoethylphosphonate degradation batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
genes: [phnW, phnX]
autolink_gene_symbols: false
---

# PSEPK ppu00440: PhnWX 2-aminoethylphosphonate degradation

- Reusable module: `modules/2_aminoethylphosphonate_degradation.yaml`
- Selected genes: 2
- Ordered reactions: 2
- Gene-level provider for the newly fetched review: OpenScientist
- Module and PSEPK satisfiability provider: OpenScientist

## Satisfiability

| Order | Reaction | PSEPK protein | UniProt | Decision |
|---|---|---|---|---|
| 1 | 2-aminoethylphosphonate + pyruvate to phosphonoacetaldehyde + L-alanine | `phnW` | Q88KT0 | Covered by reviewed PhnW-family enzyme |
| 2 | phosphonoacetaldehyde hydrolysis to acetaldehyde + phosphate | `phnX` | Q88KT1 | Covered by reviewed PhnX-family enzyme |

The focused PhnWX pathway is satisfiable in KT2440. Both exact representatives
are reviewed UniProt entries and are adjacent at PP_2208-PP_2209.

## Boundary

- The module begins with intracellular 2-aminoethylphosphonate transamination;
  transport and induction are not assumed.
- It ends with acetaldehyde and inorganic phosphate. Acetaldehyde oxidation and
  assimilation are downstream.
- PhnWAY oxidation is an alternative phosphonoacetaldehyde-processing route and
  is not collapsed into the PhnX hydrolysis step.
- The broad KEGG phosphonate/phosphinate map is not treated as one indivisible
  pathway.

## Curation

- The existing `phnW` review already identifies the exact transaminase activity.
- The new `phnX` review accepts phosphonoacetaldehyde hydrolase and organic
  phosphonate catabolism, retains magnesium binding and cytosol as non-core,
  and removes PANTHER-propagated phosphoglycolate phosphatase and DNA repair.
- OpenScientist reports were completed for PhnX and for the combined module +
  ppu00440 + PSEPK satisfiability question. The reports support both core steps
  while distinguishing family-level inference from direct KT2440 experiments.

## Validation

- The PhnX review covers all 7 GOA rows with no `PENDING` or `UNDECIDED`
  actions and passes strict gene-review validation.
- The reusable module has two substantive reaction parts, passes LinkML schema
  validation, and passes module semantic validation.
- The gene review, module page, and batch project page were rendered after
  curation; `git diff --check` passes.

## Residual issues

- Neither KT2440 enzyme has been assayed directly; assignments are supported by
  exact HAMAP/PANTHER/InterPro families, reviewed UniProt records, pathway
  adjacency, and experiments in other P. putida strains or orthologs.
- The physiological KT2440 2-aminoethylphosphonate importer is unresolved and
  remains outside the core module boundary.
- PP_2210 is a plausible AepR-like regulator by neighborhood and homology, but
  its regulatory role has not been established directly in KT2440.
