---
title: "InterPro Mapping Review Project"
maturity: SCOPING
tags: [PIPELINE]
---

**This project identifies InterPro-to-GO mappings that need correction, narrower
scope, or additional evidence.** It combines gene-level annotation reviews with
family-level evidence to distinguish functions shared across an InterPro entry
from functions restricted to particular members.

**The current deliverable contains 25 mapping assessments across nine InterPro
entries:** four removal proposals, ten proposals to narrow or qualify a mapping,
and eleven endorsements or additions. These are proposals for curator assessment;
they do not establish that InterPro has adopted the changes.

**Start here:** [Proposed mapping edits](INTERPRO/interpro2go.sssom.yaml) ·
[Prioritized entry worklist](INTERPRO/interpro_family_priorities.tsv) ·
[Gene-level evidence and reasons](INTERPRO/suspect_interpro_mappings.tsv)

## Findings and proposed curation actions

The [mapping set](INTERPRO/interpro2go.sssom.yaml) records the individual GO terms,
verdicts, and rationales. The following summarizes its recommendations; family-level
research proposals still require checking against the entry's membership and
experimental evidence.

| InterPro entry | Finding in the family assessment | Proposed action |
|----------------|----------------------------------|-----------------|
| IPR000719 — Protein kinase domain | Pseudokinase members challenge the assumption that every domain match binds ATP and phosphorylates proteins. | Remove the blanket ATP-binding and protein-phosphorylation mappings; assess narrower catalytic entries. |
| IPR001128 — Cytochrome P450 | The assessment supports cofactor-binding mappings but questions uniform catalytic assignments across functionally diverse members. | Retain the binding mappings; review the scope of monooxygenase and oxidoreductase mappings. |
| IPR001424 — Cu/Zn superoxide dismutase domain | Copper-chaperone members challenge a domain-wide superoxide-metabolism assignment. | Remove the blanket process mapping; assess metal binding separately. |
| IPR000276 — Rhodopsin-like GPCRs | The assessment flags atypical receptors as exceptions to canonical G-protein coupling. | Review receptor-activity and signaling mappings at subfamily level, verifying evidence for the proposed exceptions. |
| IPR001046 — NRAMP / SLC11 | The assessment supports broad metal-transport terms rather than substrate-specific assignments across the entry. | Retain broad transport mappings; evaluate more specific functions on individual members. |
| IPR012724 — Chaperone DnaJ | The assessment attributes ATP binding to the Hsp70 partner rather than DnaJ. | Remove the ATP-binding mapping; retain protein folding and review the scope of the heat-response mapping. |
| IPR007197 — Radical SAM | Diverse reactions can justify a broad family-level molecular-function term. | Retain catalytic activity and iron-sulfur-cluster binding; avoid unsupported specialization across the domain. |
| IPR020849 — Ras-type small GTPases | The assessment proposes GTPase activity in addition to GTP binding. | Check the proposed addition against family-wide catalytic competence; narrow process and localization assignments where needed. |
| IPR002100 — MADS-box domain | The assessment distinguishes domain-level DNA binding and dimerization from whole-protein transcription-factor function. | Retain the two domain-level mappings; do not infer transcription-factor activity from the domain alone. |

A recurring curation question is **whether a function holds across the matched
entry**, not simply whether it is well established for one member. Conversely, a
broad term can be appropriate for a diverse family even when a more specific term
is preferable for an individual gene.

## What curators can act on

1. **Assess the four removal proposals first:** ATP binding and protein
   phosphorylation for IPR000719, superoxide metabolic process for IPR001424, and
   ATP binding for IPR012724. Verify the cited exceptions and the current entry scope.
2. **Resolve the proposed GTPase-activity addition for IPR020849.** Confirm that the
   assignment is supported across the entry, including divergent members.
3. **Separate gene-level refinement from mapping-level error.** A `MODIFY` or
   `KEEP_AS_NON_CORE` decision on one gene does not by itself justify changing a
   family-wide mapping. Record whether a proposal requires removal, a narrower entry,
   or only a more specific annotation on that gene.
4. **Check apparently accepted annotations on exception members.** Prioritize
   pseudokinases, copper chaperones, and other members whose functions diverge from
   the mapped activity; update gene reviews when the evidence supports a correction.
5. **Extend the family assessments using the ranked worklist.** Each recommendation
   should identify the affected entry and GO term, supporting evidence, and a specific
   requested change for InterPro curators.

## Evidence snapshot

The committed [annotation table](INTERPRO/suspect_interpro_mappings.tsv) contains
**3,652 InterPro2GO annotation records**. Its priority table covers **1,826 resolved
InterPro entries**, plus an unresolved-source group. These are stored extraction
results, not live counts of the growing review collection.

| Gene-review action | Count |
|--------------------|------:|
| ACCEPT | 1,870 |
| MODIFY | 609 |
| KEEP_AS_NON_CORE | 523 |
| MARK_AS_OVER_ANNOTATED | 391 |
| REMOVE | 194 |
| NEW | 30 |
| UNDECIDED | 15 |
| PENDING | 20 |

The worklist flags **1,732 records (47%)**: `MODIFY`, `KEEP_AS_NON_CORE`,
`MARK_AS_OVER_ANNOTATED`, `REMOVE`, or `UNDECIDED`. **This is a review-priority
measure, not an estimated mapping error rate.** It includes valid but non-core
annotations, specificity refinements, and unresolved judgments. `NEW` and `PENDING`
records are excluded from this flag.

### Entries with repeated gene-level flags

These counts prioritize investigation; they are not family-level verdicts. A record
can cite several entries, so counts across entries should not be summed.

| InterPro entry | Annotation records | Flagged records |
|----------------|-------------------:|----------------:|
| IPR000719 | 112 | 50 |
| IPR008271 | 55 | 34 |
| IPR001128 | 44 | 26 |
| IPR036396 | 44 | 26 |
| IPR001424 | 20 | 16 |
| IPR036423 | 20 | 16 |
| IPR001046 | 27 | 15 |
| IPR012724 | 24 | 13 |
| IPR000276 | 21 | 12 |

See the [complete worklist](INTERPRO/interpro_family_priorities.tsv) for action
breakdowns, example genes, and affected GO terms.

## Supporting material

- [Proposed InterPro2GO edits](INTERPRO/interpro2go.sssom.yaml) — 25 mapping assessments
  dated 2026-06-20, with term identifiers and rationales. In this project's encoding,
  `exactMatch` endorses or proposes a mapping, `broadMatch` flags a scope or specificity
  issue, and `exactMatch` with `predicate_modifier: Not` proposes removal.
- [Methods, data, and reproducibility](INTERPRO/README.md) — extraction, family research,
  mapping format, and validation commands.
- [Status and historical notes](INTERPRO/notes.md) — open follow-up tasks, archived
  workstream checklists, and session chronology.
- [Protein families](FAMILIES.md) · [IBA annotation review](IBA_REVIEW.md) ·
  [Over-annotation patterns](OVER_ANNOTATION_PATTERNS.html) — related collections.
