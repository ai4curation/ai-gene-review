---
id: MF-9
title: Support catalytic activity with evidence of catalysis, at the enzyme's natural specificity
status: proposed
topic: MF
provenance: GOC
aspects:
- F
evidence_codes:
- IPI
go_terms:
- term_id: GO:0003824
  label: catalytic activity
- term_id: GO:0004620
  label: glycerophospholipase activity
- term_id: GO:0036424
  label: L-phosphoserine phosphatase activity
- term_id: GO:0042800
  label: histone H3K4 methyltransferase activity
differences:
- prior_source: '[wiki: Annotating binding](https://wiki.geneontology.org/index.php/Annotating_binding)'
  prior_said: Binding annotations use IPI
  we_recommend: IPI when the partner can be identified; IDA when it cannot; never IPI for catalytic terms
  why: Matches the IPI page; the binding page oversimplifies
sources:
- kind: wiki
  title: IPI
  url: https://wiki.geneontology.org/index.php/Inferred_from_Physical_Interaction_%28IPI%29
- kind: issue
  title: go-annotation#2131
  url: https://github.com/geneontology/go-annotation/issues/2131
- kind: wiki
  title: Annotation Conf. Call 2021-08-03
  url: https://wiki.geneontology.org/index.php/Annotation_Conf._Call_2021-08-03
- kind: wiki
  title: Guidelines for catalytic activity terms
  url: https://wiki.geneontology.org/index.php/Guidelines_for_catalytic_activity_terms
date: '2026-11-15'
---

# MF-9. Support catalytic activity with evidence of catalysis, at the enzyme's natural specificity

## Decision

Annotate a catalytic activity only from evidence that the product catalyses the
reaction (an activity assay, a catalytic-residue mutant, a complementation with
activity read-out). Never use IPI for catalytic activity terms. Choose the term whose
substrate range matches the enzyme's in vivo specificity: annotate the L-amino acid or
D-sugar form by default, and annotate both the NAD+ and NADP+ terms when the enzyme
uses both.

## Context

Gorule-0000007 forbids IPI for `is_a` descendants of `GO:0003824` catalytic
activity: "It is unlikely that enough information can be obtained from a binding
interaction to support such an annotation"
([wiki: IPI](https://wiki.geneontology.org/index.php/Inferred_from_Physical_Interaction_%28IPI%29);
[go-annotation#2131](https://github.com/geneontology/go-annotation/issues/2131)). The
2021 Rhea jamboree set the specificity rules: "The specificity of GO MFs is at the same
level of the specificity of enzymes; we do not create terms for each substrate if an
enzyme can act on a group of substrates"; amino acids default to the L form and sugars
to the D form; NAD(P) in a GO label means the cofactor is *unknown*, unlike IUBMB usage,
so an enzyme known to use both gets two annotations
([wiki: Annotation Conf. Call 2021-08-03](https://wiki.geneontology.org/index.php/Annotation_Conf._Call_2021-08-03);
[wiki: Guidelines for catalytic activity terms](https://wiki.geneontology.org/index.php/Guidelines_for_catalytic_activity_terms)).

## Application

Worked examples. Phospholipases that act on many acyl chains are annotated to the
general reaction (`GO:0004620` glycerophospholipase activity and its reaction-level
children), not to one Rhea reaction per chain. Phosphoserine phosphatases are annotated
to `GO:0036424` L-phosphoserine phosphatase activity; the parent and the D-form term
were merged or obsoleted after a spot check showed every annotation concerned the L
form. Positional terms for protein substrates are out of scope except for the histone
code (`GO:0042800` histone H3K4 methyltransferase activity) and ncRNA modifications.

<!-- BEGIN GENERATED: edit the frontmatter, then run `just build-guidelines` -->

## Record

| | |
|---|---|
| Status | proposed |
| Provenance | [GOC] |
| Date | 2026-11-15 |
| Evidence codes | IPI |
| GO terms | `GO:0003824` catalytic activity; `GO:0004620` glycerophospholipase activity; `GO:0036424` L-phosphoserine phosphatase activity; `GO:0042800` histone H3K4 methyltransferase activity |

## Differences from prior guidance

| Prior source | What it said | What we recommend | Why |
|---|---|---|---|
| [wiki: Annotating binding](https://wiki.geneontology.org/index.php/Annotating_binding) | Binding annotations use IPI | IPI when the partner can be identified; IDA when it cannot; never IPI for catalytic terms | Matches the IPI page; the binding page oversimplifies |

## Sources

- wiki: [IPI](https://wiki.geneontology.org/index.php/Inferred_from_Physical_Interaction_%28IPI%29)
- issue: [go-annotation#2131](https://github.com/geneontology/go-annotation/issues/2131)
- wiki: [Annotation Conf. Call 2021-08-03](https://wiki.geneontology.org/index.php/Annotation_Conf._Call_2021-08-03)
- wiki: [Guidelines for catalytic activity terms](https://wiki.geneontology.org/index.php/Guidelines_for_catalytic_activity_terms)

<!-- END GENERATED -->
