---
title: "PSEPK succinylarginine catabolism batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
genes: [astA-I, astA-II, astB, argD, astD, astE]
autolink_gene_symbols: false
---

# PSEPK succinylarginine catabolism

- Reusable module: `modules/bacterial_succinylarginine_catabolism.yaml`
- Boundary: five reactions from L-arginine to L-glutamate and succinate
- Selected KT2440 proteins: six
- Imported GOA rows reviewed: 23
- New gene-level proposals: two for the AstC-like role of `argD`/PP_4481

## Workflow

- [x] Fetch or reuse all six selected gene-review inputs.
- [x] Consume every materialized OpenScientist output in the completed bundle.
- [x] Resolve the AstA subunit architecture and ArgD/AstC specialization.
- [x] Curate every imported GOA row with no `PENDING` actions.
- [x] Verify exact UniProt exemplars, PANTHER families, and GOA PTNs.
- [x] Curate a species-neutral five-part module with MF only on annotons.
- [x] Validate and render all scoped artifacts.
- [x] Open draft PR [#2579](https://github.com/ai4curation/ai-gene-review/pull/2579) for this module.
- [ ] Address CI and reviewer feedback.

## Satisfiability

| Order | Reaction | KT2440 implementation | UniProt | Decision |
|---|---|---|---|---|
| 1 | L-arginine succinylation | `astA-I` + `astA-II` | Q88EI3 + Q88EI2 | Covered as a predicted split-chain complex; each chain contributes to GO:0008791 rather than independently enabling it |
| 2 | N-succinylarginine hydrolysis | `astB` | Q88EI5 | Covered by reviewed UniProt EC 3.5.3.23/RHEA:19533 and PTHR30420:SF2 |
| 3 | N-succinylornithine transamination | `argD`/AstC candidate | P59319 | Strong orthology, subfamily, and locus-context support; direct KT2440 substrate kinetics remain absent |
| 4 | Semialdehyde oxidation | `astD` | Q88EI4 | Covered by reviewed UniProt EC 1.2.1.71/RHEA:10812 and AstD-specific signatures |
| 5 | Terminal desuccinylation | `astE` | Q88EI7 | Covered by reviewed UniProt EC 3.5.1.96/RHEA:15169 and PTHR15162:SF7 |

The pathway is satisfiable in KT2440. The reusable module also models the
single-chain AstA implementation represented by reviewed E. coli P0AE37 as an
alternative to the Pseudomonas split-chain enzyme. It does not force both
architectures into one organism.

## Annotation Decisions

- `astA-I` and `astA-II`: retain the L-arginine-catabolism process annotation;
  mark direct `enables GO:0008791` as over-annotated because the homologous
  Pseudomonas enzyme is a two-alpha/two-beta heterotetramer. Both reviews use
  `contributes_to_molecular_function` for the complex-level activity.
- `astB`: accept the exact dihydrolase activity and catabolic process; retain
  broad arginine metabolism as non-core.
- `argD`: retain plausible acetylornithine activity as non-core, but assign the
  primary AstC-like GO:0043825 reaction and L-arginine catabolism as new
  orthology/context-supported terms. P59319 is in PTHR11986:SF113 with reviewed
  AstC/AruC exemplars O30508 and P77581.
- `astD`: accept GO:0043824 and the catabolic process; mark generic
  oxidoreductase activity as over-annotated.
- `astE`: accept GO:0009017 and the catabolic process, retain zinc binding and
  the broad amide-hydrolase parent as non-core, and remove the ester-bond
  hydrolase mapping because the exact reaction cleaves an amide C-N bond.

## Boundary And Module Design

- The module contains five required reaction parts, not a species-specific gene list.
- Arginine transport, ArgR regulation, alternative arginase/deiminase/transaminase
  routes, and downstream glutamate/succinate metabolism are outside the boundary.
- GO:0006527 is the module-level biological process. Every molecular function is
  attached to a leaf annoton.
- Family selectors are constrained by exact activities and oriented with
  reviewed UniProt exemplars plus the selected KT2440 proteins.
- The split and single-chain AstA architectures are explicit alternatives.

## Identifier Audit

The following accessions were verified against current UniProt records:
Q88EI3, Q88EI2, Q88EI5, P59319, Q88EI4, Q88EI7, P80357, P80358,
P0AE37, P76216, O30508, P77581, P76217, and P76215. The selected proteins map
to PTHR30420:SF1 (AstA chains), PTHR30420:SF2 (AstB), PTHR11986:SF113
(AstC-like P59319), PTHR11699 (AstD), and PTHR15162:SF7 (AstE).

GOA uses PTN002279553 for broad PLP/self-binding annotations on P59319 and
PTN002309601 for the broad amide-hydrolase annotation on Q88EI7. Both IDs were
verified in the local GOA snapshots. Neither is asserted as a module ancestral
node because the available evidence does not establish the exact AstC or AstE
substrate-specific function at that node.

Because KT2440 gene symbols do not transparently identify the corresponding
P. aeruginosa chain, current UniProt FASTA sequences were compared globally
with Biopython `PairwiseAligner`. Q88EI2 is 85.8% identical across aligned
residues to alpha-chain P80357 but 40.4% to beta-chain P80358; Q88EI3 is 85.6%
identical to P80358 but 38.0% to P80357. The module therefore describes Q88EI2
as alpha-like and Q88EI3 as beta-like while retaining the native KT2440 symbols.

## Research Provenance

The completed bundle contains one materialized OpenScientist gene report:
`genes/PSEPK/argD/argD-deep-research-openscientist.md`, with HTML and PDF
artifacts. It was integrated critically with UniProt, GOA, local PANTHER data,
and primary literature (PMID:7523119, PMID:9393691, PMID:2865249, and
PMID:23484010). No materialized OpenScientist report files are present for
`astA-I`, `astA-II`, `astB`, `astD`, `astE`, the generic module query, or the
module+pathway+taxon query. Those completed-but-unavailable outputs were not
restarted, reconstructed, or cited.

## Residual Uncertainty

- The KT2440 AstA-I/AstA-II complex has not been reconstituted directly; chain
  stoichiometry and division of catalytic labor are inferred from the highly
  similar Pseudomonas aeruginosa AruF/AruG system.
- P59319 has not been assayed directly with succinylornithine versus
  acetylornithine, so its physiological specialization remains an especially
  strong orthology and operon-context inference rather than direct enzymology.
- KT2440-specific kinetics and oligomeric states remain unmeasured for AstB,
  AstD, and AstE.

## Validation

All six gene reviews are required to pass schema, GOA coverage, reference,
best-practice, and ontology-term validation. The module is required to pass
both LinkML and semantic validation. Gene, module, and project pages are
rendered from the curated sources, followed by `git diff --check`.
