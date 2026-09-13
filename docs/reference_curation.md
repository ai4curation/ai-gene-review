# Curating reference identifiers and conflicting evidence

Keep `existing_annotations[].original_reference_id` as supplied by GOA/UniProt.
The annotation's `review.supported_by` can cite a different publication, whether
it is a canonical replacement record or a paper that changes the interpretation.
Declare both references in the top-level `references` list.

## Deleted or incorrect identifiers

Record an established mapping on the original reference:

```yaml
references:
  - id: PMID:34521819
    title: >-
      SARS-CoV-2 N protein antagonizes type I interferon signaling by suppressing
      phosphorylation and nuclear translocation of STAT1 and STAT2.
    is_invalid: true
    reference_review:
      replacement:
        reference_id: PMID:32953130
        reason: DUPLICATE_RECORD
        review_notes: >-
          PubMed's redirection notice identifies this as a duplicate of
          PMID:32953130. The original PMID is retained for source provenance.
  - id: PMID:32953130
    title: >-
      SARS-CoV-2 N protein antagonizes type I interferon signaling by suppressing
      phosphorylation and nuclear translocation of STAT1 and STAT2.
```

`replacement.reason` is one of:

- `DUPLICATE_RECORD`: the authority deleted or merged a duplicate record.
- `REPLACED_RECORD`: the authority explicitly replaced the source record.
- `WRONG_IDENTIFIER`: the citation used the wrong identifier; the target identifies
  the intended paper. Record the evidence establishing that intent.

The target and reason are required. The target must be declared in `references`;
self-replacements and replacement cycles fail best-practice validation. Existing
reviews without this optional metadata remain valid. Record the mapping's source
and verification in `replacement.review_notes`.

For a deleted duplicate, retain `is_invalid: true` on the old reference alongside
`replacement`. The flag describes the replaced record; it does not invalidate the
canonical paper or establish that its findings were retracted. This is consistent
with `mark_invalid_pmids()`, which otherwise re-adds the flag. Keep the publication
title in `title` (for a verified duplicate, use the cached canonical title), and put
the deletion explanation and the title's provenance in `replacement.review_notes`.
Do not mark the canonical reference invalid merely because an obsolete ID points
to it.

`replacement.reason` explains the identifier mapping; `reference_review.correctness`
assesses citation correctness and scientific soundness. A `DUPLICATE_RECORD`
mapping does not imply `correctness: WRONG_IDENTIFIER`, because both records
identify the same paper. Leave correctness unset until separately assessed.

When a PMID fetch fails, inspect the PubMed web page for an explicit redirection
notice. E-utilities may return an empty result or error for a deleted duplicate
without identifying the retained record. A fetch failure alone establishes
neither replacement nor retraction. Do not guess a target from similar titles.

Quote the canonical paper under its own identifier:

```yaml
original_reference_id: PMID:34521819
review:
  action: KEEP_AS_NON_CORE
  supported_by:
    - reference_id: PMID:32953130
      supporting_text: >-
        Moreover, our result showed that SARS-CoV-2 N interfered with the
        interactions of STAT1 with JAK1 and STAT2 with TYK2
```

This metadata does **not** silently redirect validation or fetches. LRV checks
each snippet against its explicit `reference_id`. The old reference may still
produce an advisory fetch warning until upstream LRV supports curated mappings;
`is_invalid: true` is not currently guaranteed to suppress LRV's fetch warning.
Do not copy canonical publication text into the old PMID's cache or rewrite the
GOA-derived identifier to silence that warning. Duplicate-record deletion does
not imply that the paper or its findings were retracted.

## A finding from P1 contradicted by P2

Use the existing per-finding `finding_review`, with `finding_status: DISPUTED`
(contested) or `OVERTURNED` (refuted). `superseded_by` identifies the relevant
papers; `finding_review.supported_by` now holds their exact quoted evidence.
This assesses a particular statement rather than declaring the entire P1 paper
invalid. `CORROBORATED` can similarly carry corroborating evidence.

The following is a **synthetic** example; replace all example identifiers and
sentences with verified sources when curating:

```yaml
references:
  - id: PMID:1
    title: Original study
    findings:
      - statement: Activity occurs without a cofactor.
        supporting_text: Activity occurs without a cofactor.
        finding_review:
          finding_status: DISPUTED
          superseded_by: [PMID:2]
          review_notes: The follow-up reports a cofactor requirement.
          supported_by:
            - reference_id: PMID:2
              supporting_text: A cofactor was required.
  - id: PMID:2
    title: Follow-up study
```

The finding's direct `supporting_text` belongs to P1. The assessment's nested
snippet explicitly belongs to P2. Never place P2's text directly on P1's finding
and rely on `superseded_by` or `replacement` to change its attribution. When
revisiting an annotation, cite P2 in `review.supported_by` and explain the curation
decision in `review.reason`, retaining P1 as `original_reference_id`.

Validate with `just validate <organism> <gene>` and add a curation history record
as described in [History Records](history.md).
