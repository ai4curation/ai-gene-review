---
title: "microTrait Rule Review — Plan & Input Spec"
maturity: SCOPING
tags: [PIPELINE]
---

# microTrait Rule Review — Plan & Input Spec

[← microTrait Framework Integration](../MICROTRAIT.md)

This is the working spec for reviewing microTrait rules as first-class annotation rules,
alongside UniRule/ARBA. It defines (1) the input we need from Ulas, (2) where reviews live,
(3) the per-rule review YAML layout, and (4) the review workflow. **No rule content has been
authored yet** — this page is the landing zone.

## 1. Input needed from Ulas

The tractable asset is the curated **rule table** — the predicate logic that maps HMM/gene
presence/absence to a trait. We do **not** need the ~170 MB packaged HMM database to review
the rules. Ideally a single tidy table (TSV/CSV/Excel), one row per rule (or per
rule × condition-set), with at least:

| Field | Description | Example |
|---|---|---|
| `rule_id` | Stable identifier for the rule | (Ulas's convention) |
| `trait` | The trait asserted when the rule fires | `Resource Acquisition:...` |
| `trait_granularity` | Which of the 3 granularity levels (1/2/3) | `3` |
| `trait_category` | Top-level category | Resource Acquisition / Resource Use / Stress Tolerance / Energy / Life-history |
| `logic` | The predicate-logic expression over HMM/gene names (AND/OR/NOT) | `hmmA AND (hmmB OR hmmC)` |
| `hmm_members` | The HMM/gene identifiers referenced, with human-readable names | |
| `references` | Literature basis for the trait (if available — cf. `ST8.microtrait_references.txt`) | PMIDs/DOIs |

If the rules are only available as the R package's internal representation, an export of the
`rule_matrix` / rule definitions (whatever produces the boolean assertions) plus the
HMM→gene→trait mapping is sufficient. **Flag whether the provided table is the current
public version or an updated/cleaned one**, so provenance is recorded.

## 2. Where reviews live

Per-rule reviews go under a new `rules/microtrait/` tree, mirroring `rules/arba/` and
`rules/unirule/`:

```
rules/microtrait/
  <rule_id>/
    <rule_id>-review.yaml     # the RuleReview (see §3)
    <rule_id>-review.html     # rendered (generated)
```

The raw provided table is cached (unedited) alongside the project, e.g.
`projects/MICROTRAIT/microtrait-rules.<ext>`, and the stubs are generated from it.

## 3. Per-rule review YAML layout

Reviews use the existing `RuleReview` class (validated with `-C RuleReview`), now that
`RuleTypeEnum.MICROTRAIT` and `ConditionTypeEnum.HMM` exist. Conventions specific to
microTrait:

- `rule_type: MICROTRAIT`.
- The **asserted trait** (microTrait's native consequent) is recorded in `description`
  (name + granularity + category), since the schema's `go_annotations` slot is reserved for
  the reviewer's **trait→GO equivalent** (the crosswalk).
- `condition_sets` express the predicate logic: each set is an AND of `HMM` conditions;
  multiple sets are OR-ed; absence is `negated: true`. For very large logic, summarize (as
  the ARBA reviews do) rather than enumerating exhaustively.
- `go_annotations` holds the GO term(s) the reviewer judges the trait to correspond to —
  this is the crosswalk byproduct.
- CAZy-family conditions **must** take their GO equivalent from the existing `cazy2go`
  mapping (`projects/GLYCOBIOLOGY`), not a fresh derivation.

### Illustrative template (placeholder values — NOT a real microTrait rule)

```yaml
id: MT_EXAMPLE_0001
description: >-
  microTrait rule asserting trait "<TRAIT NAME>" (granularity 3, category
  "<CATEGORY>"). PLACEHOLDER — replace with the real rule from Ulas's table.
status: PENDING
rule_type: MICROTRAIT
rule:
  rule_id: MT_EXAMPLE_0001
  condition_sets:
    - number: 1
      conditions:
        - condition_type: HMM
          value: "<hmm_or_gene_id_1>"
          label: "<human readable gene name>"
        - condition_type: HMM
          value: "<hmm_or_gene_id_2>"
          label: "<human readable gene name>"
          negated: false
  go_annotations:      # reviewer's trait -> GO mapping (the crosswalk)
    - go_id: "GO:XXXXXXX"
      go_label: "<GO term the trait corresponds to>"
      aspect: P
  entries: []
review_summary: |
  <Assessment: is the HMM logic sound? does the asserted trait match the genes? is the
  GO equivalent correct and appropriately specific?>
action: UNDECIDED          # ACCEPT | MODIFY | DEPRECATE | SPLIT | MERGE | UNDECIDED
action_rationale: |
  <Rationale for the action.>
```

Validate a stub with:

```bash
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C RuleReview \
  rules/microtrait/MT_EXAMPLE_0001/MT_EXAMPLE_0001-review.yaml
```

## 4. Workflow (once the table lands)

1. **Cache** the provided table under `projects/MICROTRAIT/` (unedited).
2. **Generate stubs**: one `RuleReview` YAML per rule with `status: PENDING`, populating
   `rule_type`, `description` (trait/granularity/category), and `condition_sets` from the
   logic column. (A small ingestion script, analogous to `src/ai_gene_review/etl/
   rule_review_init.py`, if the volume warrants it.)
3. **Review** each rule: HMM logic soundness, trait↔gene coherence, trait→GO correctness
   and specificity, taxonomic scope, then set `action`. Reuse `cazy2go` for CAZy conditions.
4. **Render** and surface in the rules browser as with ARBA/UniRule.

## 5. Constraints / honesty notes

- We are reviewing **rules**, not running genome inference; a rule review assesses the
  rule's design, not any particular genome's traits.
- microTrait traits are **genome-inferred capabilities** (hypotheses), and the trait
  vocabulary is ecology-oriented, so trait→GO mappings will be partial and curated, not a
  mechanical join.
- No rule content is invented here; all rule logic and trait assignments come from the
  provided table.
