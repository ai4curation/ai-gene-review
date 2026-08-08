---
title: "PSEPK ppu00330 gamma-glutamyl putrescine catabolism batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK ppu00330: gamma-glutamyl putrescine catabolism

- Reusable module: `modules/gamma_glutamyl_putrescine_catabolism.yaml`
- Correct pathway boundary: putrescine to GABA through four gamma-glutamyl reactions
- Broad ppu00330 candidates inspected: 39
- Newly reviewed PSEPK proteins: 4
- Module/pathway/taxon provider: OpenScientist

## Workflow

- [x] Separate the gamma-glutamyl route from the parallel SpuC transaminase route.
- [x] End the diagnostic module at GABA rather than absorbing the shared GABA shunt.
- [x] Recover PuuA and PuuD candidates missed by the KEGG-derived bucket.
- [x] Review one strong KT2440 anchor or candidate for each reaction.
- [x] Add reviewed UniProt exemplars and an exact PuuD PAINT node.
- [x] Preserve PP_2589 substrate specificity as candidate-uncertain.
- [x] Validate and render the module, genes, and project page.
- [ ] Open one PR for this module.
- [ ] Shepherd review and CI.

## Satisfiability

| Order | Reaction | PSEPK implementation | UniProt | Decision |
|---|---|---|---|---|
| 1 | Putrescine gamma-glutamylation | `puuA-I`; `puuA-II` and broader Spu ligases | Q88KW1; Q88C84 | Covered by exact EC 6.3.1.11 assignments |
| 2 | Gamma-glutamylputrescine oxidation | `puuB` | Q88K44 | Covered by exact PTHR13847:SF275 and reviewed P37906 exemplar |
| 3 | Gamma-glutamyl aminoaldehyde oxidation | leading candidate `PP_2589` | Q88JR0 | Candidate-uncertain: K09472 and PuuC CDD support, but substrate untested |
| 4 | Gamma-glutamyl-GABA hydrolysis | `PP_5298`; `spuA`; `PP_3598` | Q88C85; Q88KW0; Q88GW9 | Covered by exact EC 3.5.1.94 assignments |

The reusable four-reaction route is complete. KT2440 has strong candidates for
all steps, but its PuuC locus remains a hypothesis rather than an accepted
substrate-specific gene annotation. This is recorded as a locus-level knowledge
gap, not hidden by the broad aldehyde-dehydrogenase family assignment.

## Annotation Decisions

- The exact glutamate-putrescine ligase term is accepted for PuuA-I; generic
  catalytic/ligase terms are marked over-annotated and the erroneous glutamine
  synthetase transfer is removed.
- PuuB receives a new putrescine-catabolism process annotation, but no invented
  GO molecular-function ID. A substrate-specific GO term is proposed instead.
- PP_2589 is curated only to generic NAD(P)-linked aldehyde dehydrogenase
  activity; its PuuC role remains an explicit candidate.
- The exact PuuD hydrolase term is accepted for PP_5298, while an erroneous
  L-glutamine-metabolism transfer is removed.
- Putrescine catabolic process is added where direct pathway placement supports it.

## Boundary Decisions

- Putrescine import and arginine/agmatine-derived putrescine supply are upstream.
- SpuC putrescine:pyruvate transamination is a parallel, non-glutamylated route.
- GABA transaminase and succinate-semialdehyde dehydrogenase belong to the shared
  downstream GABA shunt and are not diagnostic module parts.
- Broad ppu00330 arginine, proline, opine, and ornithine reactions are excluded.

## Grounding

Each leaf has a concrete KT2440 UniProt protein and a reviewed E. coli reaction
exemplar. Exact Rhea reactions define all four chemical transitions. PuuD is
additionally grounded by PAINT node PTN000230196; no PTN is asserted for the
other roles because the available node evidence did not support their exact
molecular functions.

## Research Status

The OpenScientist report and artifacts are stored under
`projects/P_PUTIDA/deep-research/`. Local UniProt, GOA, PANTHER, PAINT, CDD, and
Rhea data were used to qualify the report's stronger satisfiability claim.

## Validation

All four gene reviews passed schema, GOA, reference, best-practice, and
ontology-term validation. The module passed LinkML and semantic validation with
zero warnings. Gene, module, and project renderers completed successfully.
