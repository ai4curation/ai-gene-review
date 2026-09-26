---
title: "ClinGen Mendelian review progress"
species: [human]
autolink_gene_symbols: false
---

# ClinGen Mendelian review progress

[Project and complete gene inventory](../CLINGEN_MENDELIAN.md)

Process the nuclear protein-coding Definitive, Strong, Moderate, and Limited tiers
in order, alphabetically within each tier, followed by mitochondrial protein genes,
RNA genes, other HGNC locus types, and undetermined-inheritance follow-ups. Keep
RNA genes in scope and use `just fetch-ncrna human SYMBOL` (RNAcentral identifiers)
before reviewing their functional literature. The archived HGNC subset records both
`locus_group` and `locus_type`: 2,837 protein-coding genes, 35 non-coding RNAs, and
4 other loci (readthrough, immunoglobulin, or T-cell receptor genes).

Existing reviews receive a substantive audit; a COMPLETE status does not certify
assessment against this campaign's current evidence and curation rules. The first
batch already demonstrates the value: AARS1's unconditional monomer claim needed
new disease-mechanism evidence, while AARS2 had untraced propagation judgments and
modeled variant effects presented as measured results. Prioritize new substantive
findings, evidence access, and rule compliance; do not manufacture changes to a
sound review merely to enlarge a PR.

Each gene has one dedicated PR containing its review, supporting research and
references, notes, and session history. Address biological review feedback and
in-scope validation failures on that PR. Mark a gene complete only after the final
review is validated, all actionable PR feedback is addressed, and its PR is merged.
Preserve justified UNDECIDED annotations when evidence remains inaccessible; record
the limitation rather than replacing it with an unsupported decision.

## Ownership of shared files

Gene PRs change only the gene, its required cached sources, and gene history.
They do **not** change this log, the shared inventory, or generated project pages.
The coordinator updates those shared files serially in the project branch after
checking each PR's authoritative state. Only after merge does the coordinator tick
the gene's inventory checkbox and record the merged PR and final validation.
The current concurrency is three gene reviewers, not one worker per inventory row.

## Symbol migration checks

Before fetching a gene, check its HGNC ID and both current and historical symbols
against existing review directories. These six source-to-approved mappings are
verified by HGNC `prev_symbol`, not guessed from aliases:

| ClinGen source symbol | Approved symbol | Existing review at campaign start |
|---|---|---|
| BVES | POPDC1 | Neither symbol has a review |
| CCDC115 | VMA22 | Neither symbol has a review |
| CENPJ | CPAP | Neither symbol has a review |
| NAT8L | ASPNAT | Neither symbol has a review |
| NDUFA4 | COXFA4 | `genes/human/NDUFA4/NDUFA4-ai-review.yaml` |
| TRAF3IP1 | IFT54 | Neither symbol has a review |

COXFA4 must reuse and migrate the existing NDUFA4 review in its dedicated gene PR;
do not fetch a second review independently under COXFA4. Preserve history through
`target.superseded_by` as documented in `docs/history.md`. Recheck the directories
at assignment time because other work may have added or renamed a review.

Human-qualified frontmatter deliberately avoids linking same-symbol reviews in
other species. The initial renderer check demonstrated that bare ALB and CDT1
were ambiguous without a human review, and a symbol found in only one nonhuman
species can be linked there despite the human hint. Missing-human-review warnings
are therefore expected; existing human reviews still link normally.

## Campaign status — 2026-09-26 UTC

| Gene | Tier | Starting review status | Current state | Branch | PR |
|---|---|---|---|---|---|
| A4GALT | Definitive | INITIALIZED | Review feedback in progress; CI passed | `cmungall/clingen-a4galt` | [#3127](https://github.com/ai4curation/ai-gene-review/pull/3127) |
| AARS1 | Definitive | COMPLETE | Review feedback in progress; CI passed | `cmungall/clingen-aars1` | [#3129](https://github.com/ai4curation/ai-gene-review/pull/3129) |
| AARS2 | Definitive | COMPLETE | Merged; final validation and CI passed | `cmungall/clingen-aars2` | [#3128](https://github.com/ai4curation/ai-gene-review/pull/3128) |
| AASS | Definitive | INITIALIZED | Audit in progress | `cmungall/clingen-aass` | — |
| ABCA3 | Definitive | No review | Annotation review in progress | `cmungall/clingen-abca3` | — |
| ABCA4 | Definitive | No review | Annotation review in progress | `cmungall/clingen-abca4` | — |
| ABCB4 | Definitive | No review | Primary evidence and annotation review in progress | `cmungall/clingen-abcb4` | — |

Merged project setup PR: [#3126](https://github.com/ai4curation/ai-gene-review/pull/3126).

The next unassigned nuclear protein-coding Definitive gene is **ABCC6**. **1 of
2,876 genes is complete** for this campaign. ABAT is in the Moderate tier.

## Verification log

- 2026-09-25: Checked open repository PRs before assigning the first batch; no open
  A4GALT, AARS1, or AARS2 PR was found. Started a repository-wide baseline
  `just validate-all`; gene-specific validation remains required on each branch.

- 2026-09-25: A4GALT targeted validation and history validation passed. Independent
  biological review found no blocking issue; final research artifact and GitHub
  review/checks remain pending on PR #3127.

- 2026-09-25: AARS2 targeted and history validations passed; independent biological
  review found no blocker. PR #3128 awaits GitHub review and required checks.

- 2026-09-25: AARS1 validation and history checks passed and independent biological
  feedback was addressed. PR #3129 includes a genuine late Falcon report; the
  wrapper had already timed out, and the report remains unverified as direct evidence.

- 2026-09-25: Repository-wide baseline `just validate-all` passed for 4,975 reviews
  and 54 pathway files. No blocking schema, ontology, reference, or best-practice
  failures remained; advisory warnings were retained.

- 2026-09-25: AARS2 received approval on commit `3b3d7cd710`. All three nonblocking
  suggestions were answered with source/schema evidence; required CI remains pending.

- 2026-09-25: Project review caught unexpanded RNA/other-locus count placeholders.
  Fixed the generator and authored page, checked the complete generated output for
  unresolved placeholders, and regenerated the affected project pages.

- 2026-09-26 UTC: Verified AARS2 PR [#3128](https://github.com/ai4curation/ai-gene-review/pull/3128)
  merged on 2026-09-25 at 22:40:15 UTC as `66219c3f16cd45254d0ed751869341c1f0047855`.
  The final gene and history validations passed, reviewer approval covered the final
  head, all actionable feedback was answered, and required CI passed. Checked its
  inventory row complete; the gene review's remaining evidence limitations are
  documented rather than treated as unsupported annotations.

- 2026-09-26 UTC: Project setup PR #3126 passed review and required CI and merged
  as `2bbd35ae337fbd15918289caa9e7ddc78c4b1eb8`. A4GALT and AARS1 remain open with
  further evidence-framing feedback being addressed; neither is counted complete.
  ABCB4 is now assigned, with 68 source annotations seeded, publication caching
  complete, and a genuine Falcon report available for independent verification.
