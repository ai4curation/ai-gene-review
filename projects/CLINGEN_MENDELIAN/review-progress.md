---
title: "ClinGen Mendelian review progress"
species: [human]
autolink_gene_symbols: false
---

# ClinGen Mendelian review progress

[Project and complete gene inventory](../CLINGEN_MENDELIAN.md)

Process the nuclear Definitive, Strong, Moderate, and Limited tiers in order,
alphabetically within each tier, followed by the mitochondrial and
undetermined-inheritance follow-ups. Existing reviews receive a substantive audit;
an existing COMPLETE status does not by itself complete this project's assessment.

Each gene has one dedicated PR containing its review, supporting research and
references, notes, and session history. Address biological review feedback and
in-scope validation failures on that PR. Mark a gene complete only after the final
review is validated, all actionable PR feedback is addressed, and its PR is merged.
Preserve justified UNDECIDED annotations when evidence remains inaccessible; record
the limitation rather than replacing it with an unsupported decision.

## Active batch — 2026-09-25

| Gene | Tier | Starting review status | Current state | Branch | PR |
|---|---|---|---|---|---|
| A4GALT | Definitive | INITIALIZED | Reviewing | `cmungall/clingen-a4galt` | Pending |
| AARS1 | Definitive | COMPLETE | Reviewing | `cmungall/clingen-aars1` | Pending |
| AARS2 | Definitive | COMPLETE | Reviewing | `cmungall/clingen-aars2` | Pending |

The next unassigned gene is **AASS**. No genes are complete for this campaign yet.

## Verification log

- 2026-09-25: Checked open repository PRs before assigning the first batch; no open
  A4GALT, AARS1, or AARS2 PR was found. Started a repository-wide baseline
  `just validate-all`; gene-specific validation remains required on each branch.
