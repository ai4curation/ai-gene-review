---
id: MF-4
title: Do not co-annotate binding that an activity term already implies
status: proposed
topic: MF
provenance: GOC
aspects:
- F
evidence_codes:
- IDA
- IEA
go_terms:
- term_id: GO:0004674
  label: protein serine/threonine kinase activity
- term_id: GO:0005524
  label: ATP binding
- term_id: GO:0046872
  label: metal ion binding
related:
- MF-13
differences:
- prior_source: '[wiki: Annotating binding](https://wiki.geneontology.org/index.php/Annotating_binding)
    (2020 proposal)'
  prior_said: '"Annotation to these compounds is not discouraged" (substrate and cofactor binding)'
  we_recommend: Do not co-annotate substrate, product, cofactor or solute binding implied by an activity
  why: The sentence contradicts its own heading and the older [Binding Guidelines](https://wiki.geneontology.org/index.php/Binding_Guidelines);
    we read it as a typo for "is discouraged"
sources:
- kind: wiki
  title: Binding Guidelines
  url: https://wiki.geneontology.org/index.php/Binding_Guidelines
- kind: wiki
  title: Annotating binding
  url: https://wiki.geneontology.org/index.php/Annotating_binding
date: '2026-11-15'
---

# MF-4. Do not co-annotate binding that an activity term already implies

## Decision

Do not add binding annotations for the substrates, products, cofactors or transported
solutes of an enzyme or transporter activity that is annotated. Annotate the binding term
only when binding is shown and the activity is not.

## Context

"An enzyme MUST bind all of the substrates and products of the reaction it
catalyzes. Similarly, a transporter MUST bind the molecules it transports"
([wiki: Binding Guidelines](https://wiki.geneontology.org/index.php/Binding_Guidelines)).
Redundant binding rows add noise and are a common carrier for pseudoenzyme errors,
because cofactor-binding IEA rows travel with the catalytic term ([MF-13](MF-13.md)).

## Application

Worked examples.

- A kinase annotated to `GO:0004674` protein serine/threonine kinase activity does not
  need `GO:0005524` ATP binding from the same evidence.
- A paper that shows binding of a non-hydrolysable ATP analogue but no ATPase activity
  supports `GO:0005524` ATP binding by IDA, with the analogue in With/From where the
  evidence code allows it ([wiki: Binding Guidelines](https://wiki.geneontology.org/index.php/Binding_Guidelines)).
- Do not put the bound entity in an extension when the term already names it
  (`GO:0005524` ATP binding with `has_input` ATP is redundant).

In review, an existing implied-binding row is true; it is not `REMOVE`. Use
`KEEP_AS_NON_CORE`, or `TOO_GENERAL` when it is a general term such as `GO:0046872`
metal ion binding beside an activity that specifies the metal-dependent chemistry.

<!-- BEGIN GENERATED: edit the frontmatter, then run `just build-guidelines` -->

## Record

| | |
|---|---|
| Status | proposed |
| Provenance | [GOC] |
| Date | 2026-11-15 |
| Related | [MF-13](MF-13.md) |
| Evidence codes | IDA, IEA |
| GO terms | `GO:0004674` protein serine/threonine kinase activity; `GO:0005524` ATP binding; `GO:0046872` metal ion binding |

## Differences from prior guidance

| Prior source | What it said | What we recommend | Why |
|---|---|---|---|
| [wiki: Annotating binding](https://wiki.geneontology.org/index.php/Annotating_binding) (2020 proposal) | "Annotation to these compounds is not discouraged" (substrate and cofactor binding) | Do not co-annotate substrate, product, cofactor or solute binding implied by an activity | The sentence contradicts its own heading and the older [Binding Guidelines](https://wiki.geneontology.org/index.php/Binding_Guidelines); we read it as a typo for "is discouraged" |

## Sources

- wiki: [Binding Guidelines](https://wiki.geneontology.org/index.php/Binding_Guidelines)
- wiki: [Annotating binding](https://wiki.geneontology.org/index.php/Annotating_binding)

<!-- END GENERATED -->
