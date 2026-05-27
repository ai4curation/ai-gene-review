---
name: aigr-pr-review
description: >
  Review AI Gene Review pull requests and curation changes for GO term quality,
  evidence support, core function identification, and annotation action justification.
  Use for PR review comments, review follow-up automation, and QA of gene review YAML.
---

# AIGR PR Review Skill

Use this skill when reviewing AIGR pull requests or drafting review feedback about
gene review YAML, GO annotation decisions, evidence support, or UniProt-backed summaries.

Use the repository's existing guidance and agents where appropriate, especially
`CLAUDE.md` and `.claude/agents/annotation-reviewer.md`.

## Trust Validation

Do not re-check what `just validate` already covers.

If validation passes, do not spend review effort on:
- YAML formatting or whitespace
- Empty or null optional keys
- Required-vs-optional field presence
- Enum spelling, structural schema shape, or other deterministic validation concerns

The reviewer's job is the non-deterministic part: biological judgment, GO ontology judgment,
evidence quality, and whether the curation narrative is coherent.

## Focus Areas

1. GO term specificity and aspect correctness
- Prefer the most accurate GO term supported by the evidence, not the nearest generic match.
- Flag terms that are too broad, too narrow, or placed in the wrong GO aspect.
- Be especially skeptical of vague terms like `protein binding` when a more informative MF term is available.
- If recommending `MODIFY`, provide the concrete replacement term(s) with GO IDs.

2. Evidence quality
- Each annotation review should be supported by accessible evidence.
- Check that cited PMIDs, GO references, file references, and supporting text actually justify the claimed action.
- Do not accept unsupported `NEW` annotations.
- If the relevant publication or evidence cannot be accessed, prefer `UNDECIDED`.

3. Core function identification
- `core_functions` should capture the gene's main conserved molecular/cellular role.
- Do not treat every phenotype, developmental consequence, or systems-level effect as core.
- Use the combination of review YAML, UniProt annotations, deep research, notes, and cited publications to infer what is core vs peripheral.

4. Annotation action justification
- Every action should have a reason that matches the evidence.
- `ACCEPT` and `KEEP_AS_NON_CORE` need positive support, not just absence of contradiction.
- `REMOVE` and `MARK_AS_OVER_ANNOTATED` need a clear explanation of why the current term overshoots the evidence.
- `MODIFY` should explain both why the current term is off and why the replacement is better.

## Common Issues To Catch

- Over-generic GO terms that blur the real function.
- Wrong GO aspect classification: MF vs BP vs CC confusion.
- Missing deep research or notes support for a substantial curation conclusion.
- Existing annotations or proposed new terms with no usable evidence behind them.
- `core_functions` sections that mirror phenotypes rather than molecular/cellular function.
- `review.reason` or `review.summary` text that does not justify the chosen action.
- UniProt-backed claims that are overstated relative to the actual UniProt entry.

## Things Not To Flag

- Formatting-only issues that `just validate` would catch.
- Empty YAML keys or omitted optional sections if the file validates.
- Requests to hand-edit derived context files such as `*-uniprot.txt`, `*-goa.tsv`, `*-deep-research*.md`, or `publications/PMID_*.md`.
  These should usually trigger a suggestion against review YAML/notes, a thread reply, or a tooling issue instead.

## Review Standard

Approve only when the PR is biologically and curatorially sound, not merely schema-valid.

Request changes when you find any blocking problem such as:
- major GO term specificity errors
- wrong aspect classification
- unsupported or mismatched evidence
- missing justification for a strong action decision
- core function summaries that materially misstate the gene's main role

Leave a comment rather than requesting changes when the issue is real but not clearly blocking,
or when the biology is ambiguous enough that a narrower question is more useful than a binary verdict.

Do not defer clear, fixable problems to a future PR. If a concrete curation problem is present now,
surface it now.
