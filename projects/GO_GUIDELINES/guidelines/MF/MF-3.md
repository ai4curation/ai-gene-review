---
id: MF-3
title: Prefer an activity term to a binding term
status: proposed
topic: MF
provenance: GOC
aspects:
- F
go_terms:
- term_id: GO:0005515
  label: protein binding
- term_id: GO:0005068
  label: transmembrane receptor protein tyrosine kinase adaptor activity
- term_id: GO:0005091
  label: guanyl-nucleotide exchange factor adaptor activity
- term_id: GO:0001784
  label: phosphotyrosine residue binding
- term_id: GO:0051082
  obsolete: true
- term_id: GO:0044183
  label: protein folding chaperone
- term_id: GO:0140309
  label: unfolded protein holdase activity
- term_id: GO:0140318
  label: protein transporter activity
- term_id: GO:0019901
  label: protein kinase binding
- term_id: GO:0035612
  label: AP-2 adaptor complex binding
related:
- MF-6
open_questions:
- '**Holdase term.** `GO:0051082` unfolded protein binding is obsolete, and `GO:0140309` still requires
  escorting the client to an acceptor. In-situ holdases (CRYAA, CRYAB, HSPB6, CLU, DNAJB6, DNAJB8) need
  a general holdase chaperone term.'
sources:
- kind: wiki
  title: Non-catalytic Molecular Functions
  url: https://wiki.geneontology.org/index.php/Non-catalytic_Molecular_Functions
- kind: wiki
  title: Annotating binding
  url: https://wiki.geneontology.org/index.php/Annotating_binding
- kind: repo
  title: worked example
  path: projects/MOLECULAR_ADAPTOR_ACTIVITY/worked-example-GRB2.md
- kind: repo
  title: UNFOLDED_PROTEIN_BINDING
  path: projects/UNFOLDED_PROTEIN_BINDING.md
- kind: repo
  title: MOLECULAR_ADAPTOR_ACTIVITY
  path: projects/MOLECULAR_ADAPTOR_ACTIVITY.md
date: '2026-11-15'
---

# MF-3. Prefer an activity term to a binding term

## Decision

When the evidence shows what a binding interaction achieves (bridging, carrying,
sequestering, catalysis, regulation, signal transduction, folding), annotate that
activity. Use a binding term only when binding itself is the biologically meaningful
end point, or when binding is all that has been shown.

## Context

GO's stated aim is "an annotation to a term other than binding or protein
binding" for every gene product
([wiki: Non-catalytic Molecular Functions](https://wiki.geneontology.org/index.php/Non-catalytic_Molecular_Functions)).
Binding annotations are for interactions that inform the product's normal role;
"protein-protein interactions for which there is not yet sufficient biological context
are out of scope for GO MF annotations"
([wiki: Annotating binding](https://wiki.geneontology.org/index.php/Annotating_binding)).

## Application

Worked examples.

- GRB2 carries hundreds of `GO:0005515` rows. Its function is to link activated
  receptor tyrosine kinases to effectors: `GO:0005068` transmembrane receptor protein
  tyrosine kinase adaptor activity and `GO:0005091` guanyl-nucleotide exchange factor
  adaptor activity, with `GO:0001784` phosphotyrosine residue binding as the recognition
  step (`genes/human/GRB2`;
  [worked example](../../../MOLECULAR_ADAPTOR_ACTIVITY/worked-example-GRB2.md)).
- Chaperone rows on the obsolete `GO:0051082` unfolded protein binding were reassigned
  to mechanism terms: foldases to `GO:0044183` protein folding chaperone, carrier
  holdases such as the small TIMs to `GO:0140309` unfolded protein holdase activity, and
  SCG5 to `GO:0140318` protein transporter activity. In-situ holdases (CRYAB and others)
  have no fitting term yet and use a proposed "holdase chaperone activity" term
  ([UNFOLDED_PROTEIN_BINDING](../../../UNFOLDED_PROTEIN_BINDING.md)).
- When a binding protein's activity is unknown, a class-level binding term is the right
  stopping point, for example `GO:0019901` protein kinase binding or `GO:0035612` AP-2
  adaptor complex binding with the partner in `has_input` ([MF-6](MF-6.md)).

<!-- BEGIN GENERATED: edit the frontmatter, then run `just build-guidelines` -->

## Record

| | |
|---|---|
| Status | proposed |
| Provenance | [GOC] |
| Date | 2026-11-15 |
| Related | [MF-6](MF-6.md) |
| GO terms | `GO:0005515` protein binding; `GO:0005068` transmembrane receptor protein tyrosine kinase adaptor activity; `GO:0005091` guanyl-nucleotide exchange factor adaptor activity; `GO:0001784` phosphotyrosine residue binding; `GO:0051082`  (obsolete); `GO:0044183` protein folding chaperone; `GO:0140309` unfolded protein holdase activity; `GO:0140318` protein transporter activity; `GO:0019901` protein kinase binding; `GO:0035612` AP-2 adaptor complex binding |

## Open questions

1. **Holdase term.** `GO:0051082` unfolded protein binding is obsolete, and `GO:0140309` still requires escorting the client to an acceptor. In-situ holdases (CRYAA, CRYAB, HSPB6, CLU, DNAJB6, DNAJB8) need a general holdase chaperone term.

## Sources

- wiki: [Non-catalytic Molecular Functions](https://wiki.geneontology.org/index.php/Non-catalytic_Molecular_Functions)
- wiki: [Annotating binding](https://wiki.geneontology.org/index.php/Annotating_binding)
- repo: [worked example](../../../MOLECULAR_ADAPTOR_ACTIVITY/worked-example-GRB2.md)
- repo: [UNFOLDED_PROTEIN_BINDING](../../../UNFOLDED_PROTEIN_BINDING.md)
- repo: [MOLECULAR_ADAPTOR_ACTIVITY](../../../MOLECULAR_ADAPTOR_ACTIVITY.md)

<!-- END GENERATED -->
