<!--
Thanks for contributing! A few quick notes:

- If this PR resolves a tracking issue (e.g., a "Review GO annotations: GENE" issue),
  please include a `Closes #N` line in the Summary so the issue auto-closes when this
  PR is merged. Without it, completed reviews leave their tracking issues open and
  the curation queue accumulates stale entries.
- For gene-review PRs, please confirm `just validate <organism> <gene>` passes.
- Commit the source files a review depends on (*-uniprot.txt, *-goa.tsv,
  *-deep-research-*.md, newly cached publications/*): validation checks quotes
  and annotations against them. Do not hand-edit them; regenerate with
  `just fetch-gene` / `just fetch-gene-pmids`.
-->

## Summary

<!-- 1-3 bullet points describing what this PR changes and why. -->

Closes #

## Validation

<!-- For gene-review PRs, paste the relevant `just validate` output or note "n/a". -->

## Test plan

<!-- Checklist of how to verify this PR. -->

- [ ]
