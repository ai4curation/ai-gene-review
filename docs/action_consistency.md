# Action Consistency

A gene review judges **claims about the gene**, not evidence codes. GOA often holds
several rows for one term (say IBA, IEA and NAS for `GPI-anchor transamidase complex`);
they are independent lines of evidence for one claim and reinforce each other. The
review's actions on them may differ in emphasis but must not contradict each other.
Picking the "best" evidence code and REMOVEing the rest is wrong: REMOVE says the
claim is unlikely to be correct.

## The rules table

Which action combinations are contradictions, and how severe each is, is declared in
[`src/ai_gene_review/schema/action_consistency.yaml`](https://github.com/ai4curation/ai-gene-review/blob/main/src/ai_gene_review/schema/action_consistency.yaml)
and enforced by `ai_gene_review.validation.action_consistency` during
best-practices validation (`check_type: action_consistency`).

Each rule reads as a sentence, left to right: *the `action_1` row's term is
`relation` the `action_2` row's term*.

| Column | Meaning |
|---|---|
| `action_1`, `action_2` | An `ActionEnum` value, or a list of them (any of) |
| `relation` | `SAME_TERM`: both rows carry the same term (symmetric). `DESCENDANT_OF`: `action_1` is on the **more specific** term, a strict `is_a`/`part_of` descendant of `action_2`'s. `ANCESTOR_OF`: `action_1` is on the **more general** term |
| `severity` | `OK` (documented as consistent, not reported), `INFO`, `WARNING`, `ERROR` |
| `rationale` | Shown as the suggestion in validation reports |
| `negated_1`, `negated_2` | Optional, default `false`; `true` selects NOT rows on that side |
| `term_1`, `term_2` | Optional term filters (below) |

`A ANCESTOR_OF B` and `B DESCENDANT_OF A` are the same rule; the loader rejects a
table that lists both.

### Exceptions: term filters

A rule can be restricted to rows whose term matches, with optional `term_1` and
`term_2` (one per side; SAME_TERM rows share a term, so they take `term_1` only):

```yaml
term_1: {exact: GO:0005515}                         # this term only
term_1: {exact: [GO:0003674, GO:0008150, GO:0005575]}  # any of these
```

An exception is just a more specific rule, usually with severity `OK`. When several
rules match a pair of rows, the one with the most term filters wins. Equally specific
rules that can match the same rows but disagree on severity are rejected when the
table loads, so there is never a silent tie.

Deliberately not supported: NOT/AND expressions, ancestor-of matchers, and per-gene
exceptions in the table (see per-annotation exceptions below for the rare real case). `{self_or_descendant: ...}` (a term or anything
below it) is reserved and rejected until the hierarchical relations are evaluated,
since it needs the ontology too. Protein binding wants `exact` anyway: its
descendants (enzyme binding, kinase binding, ...) are informative and follow the
normal rules.

Rows annotated to two different isoforms are not compared with each other. Pairs not
in the table are not checked.

### NOT annotations

Polarity is part of every rule (`negated_1`/`negated_2`, default positive), because
NOT runs the logic the other way:

- A positive annotation entails its ancestors; a NOT entails its descendants. Keeping
  a positive term and keeping NOT on the same term (or, once hierarchical rules are
  evaluated, on an ancestor of it) is a contradiction.
- REMOVE on a NOT row only doubts the negative claim; it does not assert the positive
  one. So REMOVE on both a term and NOT the term is consistent (agnostic), and so is
  keeping the NOT while removing the positive.
- TOO_GENERAL is never used on a NOT row (an ERROR): a NOT on a broad term is the
  strongest negative claim, not an uninformative one.

GOA legitimately carries conflicting positive and NOT annotations from different
papers. The review should still decide (REMOVE or UNDECIDED one side), or, when both
genuinely hold in different contexts, record a per-annotation exception.

### Per-annotation exceptions

For very rare cases where an apparent contradiction is correct, a row can declare it:

```yaml
review:
  action: ACCEPT
  consistency_exception:
    reason: NOT in roots (PMID:...), positive in shoots (PMID:...)
```

Conflicts involving that row are still reported, at INFO with the reason, so they stay
visible. An exception on a row that is not in any conflict is flagged (WARNING) so it
cannot go stale. Exceptions do not apply to single-row checks such as TOO_GENERAL on a
NOT row.

Strictness is ratcheted by editing the table: add a pair, or raise a severity, once
the existing reviews that violate it have been fixed.

### Current state

| action_1 | relation | action_2 | severity | reads as |
|---|---|---|---|---|
| ACCEPT | SAME_TERM | REMOVE | WARNING | an ACCEPT row and a REMOVE row share a term |
| ACCEPT (term_1 exactly GO:0005515) | SAME_TERM | REMOVE | OK | exception: protein binding is tracked by its own policy |
| [ACCEPT, KEEP_AS_NON_CORE], negated_1 | SAME_TERM | [ACCEPT, KEEP_AS_NON_CORE, NEW, TOO_GENERAL] | WARNING | a kept NOT row and a kept positive row share a term |
| TOO_GENERAL | ANCESTOR_OF | ACCEPT | OK | the TOO_GENERAL term is more general than an ACCEPTed term |
| TOO_GENERAL | ANCESTOR_OF | KEEP_AS_NON_CORE | OK | the TOO_GENERAL term is more general than a kept term |

When it was introduced, the ACCEPT/REMOVE rule fired on 35 reviews (325 row pairs; the
REMOVEd rows are mostly TAS, IDA, IMP and IPI); with the protein binding exception,
34 reviews (301 row pairs). The NOT rule fired on 23 reviews (54 row pairs; e.g. GAI,
RGA, WUS, Akt1). Both stay WARNINGs until those are fixed, then can become ERRORs.

`DESCENDANT_OF` and `ANCESTOR_OF` rules are not evaluated yet (they need the ontology at validation
time), so the loader only accepts `OK` for them.

Unlike the older `inconsistent_review_actions` warning, this check has no exemption for
REMOVE rows that cite a different reference: REMOVE is a judgment on the claim,
whatever paper the row cites.

### Baseline (October 2026)

A corpus scan of 6,528 reviews and 20,432 non-negated REMOVE rows, comparing each REMOVE
with what the same review asserts as true (ACCEPT, KEEP_AS_NON_CORE, NEW, MODIFY
replacement):

| Pattern | REMOVE rows | Reviews |
|---|---|---|
| REMOVE vs ACCEPT/KEEP_AS_NON_CORE, same term | 122 | 55 |
| REMOVE on an ancestor of an asserted term (excluding protein binding) | 253 | 168 |
| REMOVE on `GO:0005515` protein binding with an asserted descendant | 13,887 | ~700 |

Protein binding is tracked separately, under its own policy
(`validation/protein_binding_policy.py`).

Other combinations on the same term worth future rules: MODIFY + REMOVE (437 term
groups), MARK_AS_OVER_ANNOTATED + REMOVE (44), NEW + REMOVE (14).

## TOO_GENERAL

`TOO_GENERAL` is for a term that is **true of the gene but uninformative**, because a
more specific term asserted elsewhere in the same review already entails it:
`hydrolase activity` beside an accepted `metalloendopeptidase activity`, or `membrane`
beside an accepted `endoplasmic reticulum membrane`.

It judges the term, not the row's evidence, which is weighed separately, and it never
means the claim is false. How it differs from the other actions:

| Action | Says |
|---|---|
| REMOVE | The claim is unlikely to be correct |
| MODIFY | This row's own evidence supports a better term |
| MARK_AS_OVER_ANNOTATED | The claim goes beyond what the evidence supports |
| TOO_GENERAL | The claim is true but subsumed by a more specific asserted term |

Use it sparingly. A broader term that still says something useful (a pathway-level
process beside a specific step, `endoplasmic reticulum` from a localization screen
beside `ER membrane`) stays ACCEPT or KEEP_AS_NON_CORE. It is not used for
`GO:0005515` protein binding.

Examples: `genes/SCHPO/gaa1`, `genes/PSEAE/rhlB`, `genes/AGKCO/fibrolase`.
