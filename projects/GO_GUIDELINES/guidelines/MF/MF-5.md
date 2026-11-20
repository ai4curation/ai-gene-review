---
id: MF-5
title: 'Treat bare `GO:0005515` protein binding as uninformative: never propose it, and in review replace
  or remove it'
status: proposed
topic: MF
provenance: NEW
provenance_note: '[NEW] for the review actions (this repository''s policy, ahead of a pending GOC proposal);
  [GOC] for the QC rules.'
aspects:
- F
evidence_codes:
- IDA
- ISS
- TAS
- NAS
- IEA
go_terms:
- term_id: GO:0005515
  label: protein binding
- term_id: GO:0042802
  label: identical protein binding
- term_id: GO:0046983
  label: protein dimerization activity
- term_id: GO:0140767
  label: enzyme-substrate adaptor activity
enforced_by:
- src/ai_gene_review/validation/protein_binding_policy.py
differences:
- prior_source: '[wiki: Binding Guidelines](https://wiki.geneontology.org/index.php/Binding_Guidelines);
    [wiki: IPI](https://wiki.geneontology.org/index.php/Inferred_from_Physical_Interaction_%28IPI%29)'
  prior_said: Reciprocal GO:0005515 IPI annotations must be made
  we_recommend: Do not create new bare GO:0005515 annotations at all; reciprocity is moot for new work
  why: Protein binding records interaction, which MI databases curate; the 2026 IEA WG proposal would
    make it do-not-annotate
- prior_source: '[Drive: protein binding announcement (go-ontology#11094)](https://drive.google.com/open?id=1CDLNsl-FgwqdsLP3jTfuA7h3nTdGq_ASEyYyLiTLhWE)'
  prior_said: Convert identical protein binding and homodimerization rows to GO:0005515 with `has_input`
  we_recommend: Do not convert into GO:0005515; refine to an informative MF or remove
  why: Conversion moves the problem; the 2026 proposal treats both terms as equally uninformative
- prior_source: '[Drive: oligomerization obsoletion proposal](https://drive.google.com/open?id=1JxzNwl1fr5Fj-IJy_Fo1lLfAlAQB8IxPDwwYKxIXBZo)'
  prior_said: Assembled subunits may be given structural molecule activity, "protein binding, bridging"
    or protein binding
  we_recommend: Structural or adaptor terms only with evidence for them; never GO:0005515 as a landing
    term
  why: Same reason; "protein binding, bridging" is now `GO:0030674` and needs two partners
- prior_source: protein_binding_policy docstring vs [MOLECULAR_ADAPTOR_ACTIVITY](../../../MOLECULAR_ADAPTOR_ACTIVITY.md)
  prior_said: The policy says REMOVE is the general case and MODIFY when the paper supports an informative
    MF; the project page says the policy "prefers MODIFY"
  we_recommend: MODIFY when the row's paper supports the informative term; otherwise REMOVE
  why: The two repo texts read the same policy differently; the validator accepts either action, so the
    evidence decides
  issue: 6443
open_questions:
- '**Protein binding and oligomerisation terms.** Should GO adopt the 2026 IEA working group proposal
  to make `GO:0005515`, `GO:0042802` and the dimerization terms do-not-annotate, and archive the IntAct-derived
  rows in a MITAB file? This document assumes yes for new work but cannot retire existing rows.'
sources:
- kind: drive
  title: protein binding do_not_annotate proposal
  url: https://drive.google.com/open?id=1KKM7gxsPvQgszjppuyD_ZldM_T8cGV0ajSUIfLmyNQc
- kind: repo
  title: protein_binding_policy.py
  path: src/ai_gene_review/validation/protein_binding_policy.py
- kind: repo
  title: CLAUDE.md
  path: CLAUDE.md
- kind: wiki
  title: Binding Guidelines
  url: https://wiki.geneontology.org/index.php/Binding_Guidelines
- kind: issue
  title: go-annotation#3314
  url: https://github.com/geneontology/go-annotation/issues/3314
- kind: repo
  title: worked example
  path: projects/MOLECULAR_ADAPTOR_ACTIVITY/worked-example-RPTOR.md
- kind: issue
  title: go-annotation#2683
  url: https://github.com/geneontology/go-annotation/issues/2683
date: '2026-11-15'
---

# MF-5. Treat bare `GO:0005515` protein binding as uninformative: never propose it, and in review replace or remove it

## Decision

Never make a new bare `GO:0005515` annotation. In review, an existing bare
`GO:0005515` row is `MODIFY` when the row's paper supports a more informative MF
(adaptor, regulator, a class-level binding term), otherwise `REMOVE`, or `UNDECIDED` when
the paper cannot be read. Never `ACCEPT`, `KEEP_AS_NON_CORE` or `MARK_AS_OVER_ANNOTATED`
it. A `REMOVE` says the annotation is uninformative, not that the interaction is false.

## Context

GO:0005515 says that a protein sticks to something, not what it does. An
IEA working group proposal (2026) puts the scale plainly: protein binding is 33% of all
experimental annotations and 70% of experimental MF annotations, 82% of those come from
IntAct exports, and many groups do not curate it at all
([Drive: protein binding do_not_annotate proposal](https://drive.google.com/open?id=1KKM7gxsPvQgszjppuyD_ZldM_T8cGV0ajSUIfLmyNQc)).
The same proposal would add `GO:0042802` identical protein binding and
`GO:0046983` protein dimerization activity (and its homo- and hetero- children) to the
do-not-annotate subset, because they carry the same information content and
multimerisation is out of scope for GO. This repository already enforces the policy on
GO:0005515 as a validator warning
([protein_binding_policy.py](../../../../src/ai_gene_review/validation/protein_binding_policy.py)).
It is the one sanctioned case where `REMOVE` may be used on a true statement
([CLAUDE.md](../../../../CLAUDE.md)).

Rules that still apply to any surviving GO:0005515 row, and that a reviewer should
check: the partner must be in With/From (gorule-0000003, gorule-0000018); `NOT` must
not be used with GO:0005515; ISS must not be used; and interspecies binding is allowed
only for physiological interactions, with the experimentally used partner in With/From
([wiki: Binding Guidelines](https://wiki.geneontology.org/index.php/Binding_Guidelines);
[go-annotation#3314](https://github.com/geneontology/go-annotation/issues/3314)).

## Application

Worked example. RPTOR has 61 GO:0005515 rows. Split by partner, they fall into two
groups: binding to MTOR, and binding to TOS-motif substrates such as the 4E-BPs and
S6 kinases. The second group supports `GO:0140767` enzyme-substrate adaptor activity
(`MODIFY`); single co-immunoprecipitation hits with no bridging context are `REMOVE`
([worked example](../../../MOLECULAR_ADAPTOR_ACTIVITY/worked-example-RPTOR.md)).

For `GO:0042802` and `GO:0046983` rows: until GO decides the proposal, keep a row only
when the oligomer is itself functionally informative and the evidence shows it;
otherwise treat the row the way GO:0005515 is treated. Earlier GOC reviews moved
`IDA` heterodimerization rows to GO:0005515 with an interactor in With/From and removed
`NAS`/`TAS` rows
([go-annotation#2683](https://github.com/geneontology/go-annotation/issues/2683)).

<!-- BEGIN GENERATED: edit the frontmatter, then run `just build-guidelines` -->

## Record

| | |
|---|---|
| Status | proposed |
| Provenance | [NEW] for the review actions (this repository's policy, ahead of a pending GOC proposal); [GOC] for the QC rules. |
| Date | 2026-11-15 |
| Enforced by | [`src/ai_gene_review/validation/protein_binding_policy.py`](../../../../src/ai_gene_review/validation/protein_binding_policy.py) |
| Evidence codes | IDA, ISS, TAS, NAS, IEA |
| GO terms | `GO:0005515` protein binding; `GO:0042802` identical protein binding; `GO:0046983` protein dimerization activity; `GO:0140767` enzyme-substrate adaptor activity |

## Differences from prior guidance

| Prior source | What it said | What we recommend | Why |
|---|---|---|---|
| [wiki: Binding Guidelines](https://wiki.geneontology.org/index.php/Binding_Guidelines); [wiki: IPI](https://wiki.geneontology.org/index.php/Inferred_from_Physical_Interaction_%28IPI%29) | Reciprocal GO:0005515 IPI annotations must be made | Do not create new bare GO:0005515 annotations at all; reciprocity is moot for new work | Protein binding records interaction, which MI databases curate; the 2026 IEA WG proposal would make it do-not-annotate |
| [Drive: protein binding announcement (go-ontology#11094)](https://drive.google.com/open?id=1CDLNsl-FgwqdsLP3jTfuA7h3nTdGq_ASEyYyLiTLhWE) | Convert identical protein binding and homodimerization rows to GO:0005515 with `has_input` | Do not convert into GO:0005515; refine to an informative MF or remove | Conversion moves the problem; the 2026 proposal treats both terms as equally uninformative |
| [Drive: oligomerization obsoletion proposal](https://drive.google.com/open?id=1JxzNwl1fr5Fj-IJy_Fo1lLfAlAQB8IxPDwwYKxIXBZo) | Assembled subunits may be given structural molecule activity, "protein binding, bridging" or protein binding | Structural or adaptor terms only with evidence for them; never GO:0005515 as a landing term | Same reason; "protein binding, bridging" is now `GO:0030674` and needs two partners |
| protein_binding_policy docstring vs [MOLECULAR_ADAPTOR_ACTIVITY](../../../MOLECULAR_ADAPTOR_ACTIVITY.md) | The policy says REMOVE is the general case and MODIFY when the paper supports an informative MF; the project page says the policy "prefers MODIFY" | MODIFY when the row's paper supports the informative term; otherwise REMOVE | The two repo texts read the same policy differently; the validator accepts either action, so the evidence decides (#6443) |

## Open questions

1. **Protein binding and oligomerisation terms.** Should GO adopt the 2026 IEA working group proposal to make `GO:0005515`, `GO:0042802` and the dimerization terms do-not-annotate, and archive the IntAct-derived rows in a MITAB file? This document assumes yes for new work but cannot retire existing rows.

## Sources

- drive: [protein binding do_not_annotate proposal](https://drive.google.com/open?id=1KKM7gxsPvQgszjppuyD_ZldM_T8cGV0ajSUIfLmyNQc)
- repo: [protein_binding_policy.py](../../../../src/ai_gene_review/validation/protein_binding_policy.py)
- repo: [CLAUDE.md](../../../../CLAUDE.md)
- wiki: [Binding Guidelines](https://wiki.geneontology.org/index.php/Binding_Guidelines)
- issue: [go-annotation#3314](https://github.com/geneontology/go-annotation/issues/3314)
- repo: [worked example](../../../MOLECULAR_ADAPTOR_ACTIVITY/worked-example-RPTOR.md)
- issue: [go-annotation#2683](https://github.com/geneontology/go-annotation/issues/2683)

<!-- END GENERATED -->
