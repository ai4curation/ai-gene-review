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

## Campaign status — 2026-09-27 UTC

| Gene | Tier | Starting review status | Current state | Branch | PR |
|---|---|---|---|---|---|
| A4GALT | Definitive | INITIALIZED | Merged; final validation and CI passed | `cmungall/clingen-a4galt` | [#3127](https://github.com/ai4curation/ai-gene-review/pull/3127) |
| AARS1 | Definitive | COMPLETE | Merged; final validation and CI passed | `cmungall/clingen-aars1` | [#3129](https://github.com/ai4curation/ai-gene-review/pull/3129) |
| AARS2 | Definitive | COMPLETE | Merged; final validation and CI passed | `cmungall/clingen-aars2` | [#3128](https://github.com/ai4curation/ai-gene-review/pull/3128) |
| AASS | Definitive | INITIALIZED | Merged; final validation and CI passed | `cmungall/clingen-aass` | [#3133](https://github.com/ai4curation/ai-gene-review/pull/3133) |
| ABCA3 | Definitive | No review | Merged; final validation and CI passed | `cmungall/clingen-abca3` | [#3134](https://github.com/ai4curation/ai-gene-review/pull/3134) |
| ABCA4 | Definitive | No review | Merged; final validation and CI passed | `cmungall/clingen-abca4` | [#3132](https://github.com/ai4curation/ai-gene-review/pull/3132) |
| ABCB4 | Definitive | No review | Merged; final approval and required CI passed | `cmungall/clingen-abcb4` | [#3135](https://github.com/ai4curation/ai-gene-review/pull/3135) |
| ABCC6 | Definitive | No review | Merged; final approval and required CI passed | `cmungall/clingen-abcc6` | [#3138](https://github.com/ai4curation/ai-gene-review/pull/3138) |
| ABCC8 | Definitive | No review | Draft; current head approved; PMID:16924481 cache required | `cmungall/clingen-abcc8` | [#3136](https://github.com/ai4curation/ai-gene-review/pull/3136) |
| ABCC9 | Definitive | No review | Merged; final approval and required CI passed | `cmungall/clingen-abcc9` | [#3148](https://github.com/ai4curation/ai-gene-review/pull/3148) |
| ABCD1 | Definitive | No review | Draft; biological feedback resolved; PMID:16213491 cache required | `cmungall/clingen-abcd1` | [#3150](https://github.com/ai4curation/ai-gene-review/pull/3150) |
| ACAD8 | Definitive | INITIALIZED | Merged; final approval and required CI passed | `cmungall/clingen-acad8` | [#3151](https://github.com/ai4curation/ai-gene-review/pull/3151) |
| ACAD9 | Definitive | COMPLETE | Merged; final approval and required CI passed | `cmungall/clingen-acad9` | [#3152](https://github.com/ai4curation/ai-gene-review/pull/3152) |
| ACADM | Definitive | COMPLETE | Draft; biological blocker resolved; PMID:18459129 cache required | `cmungall/clingen-acadm` | [#3156](https://github.com/ai4curation/ai-gene-review/pull/3156) |
| ACADS | Definitive | COMPLETE | Merged; final approval and required CI passed | `cmungall/clingen-acads` | [#3155](https://github.com/ai4curation/ai-gene-review/pull/3155) |
| ACADSB | Definitive | INITIALIZED | Merged; final approval and required CI passed | `cmungall/clingen-acadsb` | [#3154](https://github.com/ai4curation/ai-gene-review/pull/3154) |
| ACADVL | Definitive | COMPLETE | Merged; final-head approval and required CI passed | `cmungall/clingen-acadvl` | [#3157](https://github.com/ai4curation/ai-gene-review/pull/3157) |
| ACAN | Definitive | COMPLETE | Draft; biological feedback resolved; PMID:11222505 cache required | `cmungall/clingen-acan` | [#3153](https://github.com/ai4curation/ai-gene-review/pull/3153) |
| ACAT1 | Definitive | COMPLETE | Draft; current head approved; eight donor caches required | `cmungall/clingen-acat1` | [#3158](https://github.com/ai4curation/ai-gene-review/pull/3158) |
| ACOX1 | Definitive | INITIALIZED | Draft; all biological feedback resolved; PMID:16672280 cache required | `cmungall/clingen-acox1` | [#3159](https://github.com/ai4curation/ai-gene-review/pull/3159) |
| ACOX2 | Definitive | INITIALIZED | Draft; current head approved; six required publication caches pending | `cmungall/clingen-acox2` | [#3161](https://github.com/ai4curation/ai-gene-review/pull/3161) |
| ACSL4 | Definitive | COMPLETE | Draft; current head approved; notes-only PMID:23766516 cache required | `cmungall/clingen-acsl4` | [#3160](https://github.com/ai4curation/ai-gene-review/pull/3160) |
| ACTA1 | Definitive | COMPLETE | Merged; final-head approval and required CI passed | `cmungall/clingen-acta1` | [#3163](https://github.com/ai4curation/ai-gene-review/pull/3163) |
| ACTA2 | Definitive | COMPLETE | Published; follow-up validated locally; automated re-review retry queued | `cmungall/clingen-acta2` | [#3164](https://github.com/ai4curation/ai-gene-review/pull/3164) |
| ACTB | Definitive | COMPLETE | Draft; independent audit and validation passed; two required publication caches pending | `cmungall/clingen-actb` | [#3184](https://github.com/ai4curation/ai-gene-review/pull/3184) |
| ADA | Definitive | INITIALIZED | Draft; independent audit and validation passed; six PMID and three Reactome caches pending | `cmungall/clingen-ada` | [#3179](https://github.com/ai4curation/ai-gene-review/pull/3179) |
| ADGRV1 | Definitive | COMPLETE | Substantive audit in progress | — | — |
| ADNP | Definitive | COMPLETE | Substantive audit in progress | — | — |
| ADSL | Definitive | INITIALIZED | Substantive audit in progress | — | — |

Branches for work without a PR may exist only in a local isolated checkout.
Published check and approval states are the last verified states from this session,
not a live dashboard. ABCC6 merged through protected auto-merge on September 26
at 21:22:34 UTC. A separate checkout inside the writable workspace supports local
Git commits while the original worktree's shared Git metadata remains read-only.
Publication uses GitHub's API with expected-head guards and exact tree verification.
Direct Git transport and normal publication-source downloads still encounter DNS
failures. No local or published draft is counted as merged or complete.

The [publication queue](publication-queue.json) records the exact local file sets
and SHA-256 hashes for the separately published gene revisions. Recheck each remote head
before publishing a follow-up, and keep project tracking in its own PR. ABCC8
still needs the normal cache fetch for PMID:16924481; ABCD1 needs PMID:16213491.
ACAN also needs PMID:11222505, and ACADM needs PMID:18459129. Their targeted validators pass with these warnings, but the reference-cache
requirement remains outstanding. ABCG5 initialization also failed at the normal
UniProt fetch because DNS access was unavailable; no seed files were invented.
ABCG5, ABCG8, ABHD12 and ABHD5 remain queued in the normal alphabetical order.
While those source downloads are unavailable, workers are auditing the next
available cached reviews, now reaching ACTA1 and ACTA2. This temporary
scheduling does not mark the earlier unseeded genes complete. The concurrent cached-review batch assigned ACAN before ACADVL; that was a scheduling exception to strict alphabetical order, and ACADVL has a dedicated audit PR with a published follow-up. ACAD8's genuine
Falcon/fallback launch attempts failed at dependency retrieval before provider
contact; its manual primary-source research is documented without a fabricated report.

The complete log of ABCB4's second review attempt reports the review account's
session limit, with reset at **2026-09-27 01:00 UTC**. That earlier comment accepted the biological fixes, but did not record formal approval at the time. ABCB4 later received current-head approval and merged.
The subsequent ABCB4 and ABCC9 reviews completed with concrete changes requested. Later ACAD8 and ACAD9 workflow runs completed successful reviews before that reset
time, demonstrating that the earlier failure was no longer universal. Reran the
earlier failed ABCB4 and ABCC9 reviews after that new evidence. Keep the normal
approval and CI gates and inspect each current run rather than assuming a fixed
outage window.

Merged project setup PR: [#3126](https://github.com/ai4curation/ai-gene-review/pull/3126).

The earliest unseeded nuclear protein-coding Definitive gene is **ABCG5**. **15 of
2,876 genes are complete** for this campaign. ABAT is in the Moderate tier.

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

- 2026-09-26 UTC: AASS, ABCA3, and ABCA4 have dedicated PRs (#3133, #3134,
  and #3132), with targeted validation, history validation, rendering, and source
  assertion preservation checks passed. Independent coordinator inspection found
  no blocking biological issue; external review and current-head CI remain pending.
  Reserved ABCC6 and ABCC8 for the next reviews. A4GALT is approved on
  `cc2386416e`; AARS1's biological fixes were approved on `f85785312d`, followed
  by a history-only wording correction on `f0f9e75cd4`. Neither is counted complete
  before merge. The earlier "CI passed" status referred to superseded heads and
  is replaced with current-head pending states.

- 2026-09-26 UTC: A4GALT PR #3127 merged at 02:50:20 UTC as
  `2de175d73c1746bedc98d758d5932643af176805`; AARS1 PR #3129 merged at
  02:54:38 UTC as `5b2c8193f4bc9875f17b0845e5f3165680e0c697`. Both had
  approval on their final heads and successful required CI, with targeted gene
  and history validation already passed. Their two inventory checkboxes are now
  complete, bringing the campaign total to three.

- 2026-09-26 UTC: ABCB4 PR #3135 contains 68 adjudicated assertions and 23
  propagation assessments, preserving both NOT flags. Targeted validation,
  history validation, rendering and source-object comparison pass; three evidence
  questions remain explicitly UNDECIDED. AASS and ABCA3 follow-ups were approved
  and await required checks. ABCC6/ABCC8 reviews are underway, ABCC9 is assigned,
  and ABCD1 has been initialized after checking its former symbol ALD and alias
  ALDP for existing reviews. The next unassigned Definitive gene is ABCG5.

- 2026-09-26 UTC: Opened progress PR [#3137](https://github.com/ai4curation/ai-gene-review/pull/3137)
  for the three confirmed completions. ABCC8 PR #3136 reviews 64 source assertions
  with 44 propagation assessments; ABCC6 PR #3138 reviews 69 assertions. The
  ABCC6 follow-up distinguishes mineral-deposition assays from ion-homeostasis
  evidence. ABCB4's local follow-up preserves all 68 assertions and both NOT
  flags, leaves clathrin-vesicle localization unresolved, and supplies the
  condition-specific cholesterol evidence from its original reference. Gene,
  history and rendering checks passed for ABCB4; the revision remains unpublished.

- 2026-09-26 UTC: Completed independent audits and local revisions for ABCB4,
  ABCC6 and ABCC8 after changes were requested on their published PRs. All 68,
  69 and 64 source assertions respectively remain intact. ABCC6 now removes
  uninformative generic binding terms without asserting absence of interaction,
  and distinguishes cellular ATP release from proven direct ATP cargo transport.
  ABCC8 now incorporates the mouse GO-CAM insulin-secretion evidence and direct
  SUR1 ATPase results, with PMID:16924481 still awaiting its normal cache fetch.
  Targeted gene and history validation and rendering pass for all three local
  follow-ups; publication remains pending.

- 2026-09-26 UTC: ABCC9's 53 annotations and ABCD1's 135 annotations received
  complete local reviews and independent biological audits. All seeded fields
  were preserved; gene validation, history validation and rendering pass. ABCD1
  retains eight evidence-limited UNDECIDED decisions and documents the missing
  PMID:16213491 cache. Neither gene has a published PR yet. The earlier ABCC8
  starting-state placeholder was resolved by checking for an existing human
  review before seeding: none was present, so its baseline is "No review".

- 2026-09-26 UTC: Public GitHub PR, commit and test pages confirm three further
  merges, all dated September 26 (exact clock times were not exposed): AASS
  [#3133](https://github.com/ai4curation/ai-gene-review/pull/3133) as
  `5f44a3fc98ffd3fa68a8ded0105cf83803e030b5`; ABCA3
  [#3134](https://github.com/ai4curation/ai-gene-review/pull/3134) as
  `52382b633dc98f8f5b12d5f35c3cf3761343d359`; and ABCA4
  [#3132](https://github.com/ai4curation/ai-gene-review/pull/3132) as
  `cbb8c133015f10ed37968a1ca71207c95dbd11b7`. Approval and successful current-head
  tests were verified for each. Their inventory checkboxes are now complete,
  bringing the campaign total to six. Tracking PR
  [#3137](https://github.com/ai4curation/ai-gene-review/pull/3137) is approved with
  its test passed but remains open; these newer local tracking updates have not
  been published to it.

- 2026-09-26 UTC: Recovered local Git operations in an independent checkout at
  the ignored workspace path `tmp/clingen-git`; the original Orca worktree and
  source files were preserved. Both follow-ups were committed locally and then
  published through GitHub's API with expected-head checks: ABCB4 #3135 at
  `5fa6ee26208562402e4295703a80ea7cf569b0e2` and ABCC6 #3138 at
  `681dc1cf8acc6a0487294b8841b0479b617e5fac`. GitHub tree hashes exactly match the
  corresponding validated local commit trees. Updated both PR descriptions.
  Direct Git HTTPS transport still cannot resolve its host; GitHub API access
  works. Normal fetches of PMID:16924481 and PMID:16213491 were retried once each
  and still failed DNS resolution, so their cache requirements remain open.


- 2026-09-26 UTC: ABCC6 PR #3138 merged at 21:22:34 UTC as
  `21121fc735d20bcb2dbf8328aa82d5da30185e5e`, after final-head approval and
  required CI. Checked its inventory row complete, bringing the total to seven.
  Published ABCC8's validated follow-up at `1bf52d95a381d852b6a2a1dc5b44c2bceaefd329`
  and kept PR #3136 in draft pending PMID:16924481. Opened ABCC9 PR #3148 at
  `dd674e49837004266dafbafccd62b0b98a2c7a98` and ABCD1 draft PR #3150 at
  `8090c5a86ab995ecdcc191e17e71f723853ede17`; the latter still requires the
  normal PMID:16213491 cache. The complete source manifests and remote/local tree
  equality checks are recorded in the publication queue. ABCC9's required test passed.

- 2026-09-26 UTC: Audited the next available cached reviews while earlier gene
  initialization remained unavailable. ACAD8 PR #3151 preserves 23 source rows,
  corrects substrate-specificity reasoning and passes validation without warnings.
  ACAD9 PR #3152 preserves 40 source rows, withdraws one redundant authored NEW
  row and retains directly supported beta-oxidation in its core; validation passes
  with one intentional advisory. ACAN draft PR #3153 preserves 40 source rows,
  corrects matrix-location and binding evidence, and withdraws an unsupported
  authored assembly row; its three warnings include the missing PMID:11222505
  cache. Independent biological inspection, history validation and rendering pass
  for all three. Existing source caches were preserved. ACADM, ACADS and ACADSB
  audits are now underway; no unmerged review is checked complete.

- 2026-09-26 UTC: Inspected the complete failed reviewer log rather than assuming
  a biological or Git failure. ABCB4's second attempt reports the reviewer account
  session limit, resetting September 27 at 01:00 UTC; no formal current-head
  approval was recorded. Further attempts are deferred until reset. Required
  review gates remain intact. The project branch's sole main-merge conflict is
  its generated inventory HTML; regenerate it from the updated source to retain
  the newly available gene links and the seven confirmed completion checkboxes.


- 2026-09-26 UTC: Published ACAD8 feedback commit
  `acd39fb8cbb021bbee3841ca977b247b8ac3f802`: broad mitochondrial rows retain their
  original source resolution, the encompassing short-chain GO term is accepted
  without changing its specific propionyl Rhea reaction, and full-text/pathway
  wording is corrected. Published ACAD9 feedback commit
  `53b3e3c398f59a40419f7c080954fd71d2de4b2e`: refine the supported beta-oxidation
  process, attribute neuronal details to externally read primary text and record
  the unresolved assembly molecular function. Both targeted validators now pass
  without warnings; all 23 and 40 source assertions respectively are preserved.

- 2026-09-26 UTC: Published ACADSB #3154 (28 source rows) and ACADS #3155 (30
  source rows), each with independent biological inspection and clean targeted
  validation. Published ACADM draft #3156 (50 source rows), whose original mouse
  process donor was recovered as PMID:18459129; its required normal cache fetch
  failed DNS. The review distinguishes metabolic repartitioning from a synthesis
  step and retains unresolved mechanistic evidence. Three further cached reviews
  are underway: ACADVL, ACAT1 and ACOX1. Review-service retries resumed only after
  newer workflows demonstrated successful runs; the previous session-limit report
  is historical evidence rather than a blanket block until its quoted reset time.

- 2026-09-26 UTC: Renewed reviewer feedback identified one remaining ABCB4
  YAML-alias mismatch. Published `85a037efcedc539102539973d26fbd2ae328133f`
  with both biliary secretion rows consistently replaced by phospholipid efflux;
  all 68 source assertions and other decisions are unchanged. ABCC9, ACADSB and
  ACADS received source-scope or wording feedback and are being revised. ACAD8
  and ACAD9 received approval on their latest published heads; protected auto-merge
  is enabled while required tests finish. They are not yet counted complete.

- 2026-09-26 UTC: Project review caught links to four unmerged gene pages in the
  generated inventory. Regenerated using only gene-review paths present in the
  project branch's target tree (`c58fcd6b4589c722799c6e39da663420db32dd7c`),
  so ABCB4, ABCC8, ABCC9 and ABCD1 remain unlinked until merge. The previous
  conflict-resolution note confused locally available reviews with published
  pages; this entry corrects that decision. ABCA3, ABCA4 and ABCC6 remain linked
  because their pages have merged. Future tracking renders must use the target
  Git tree's gene availability rather than the coordinator's working directories.

- 2026-09-26 22:38 UTC: Confirmed ACAD8 #3151 merged at 22:20:09 UTC as
  `9e34ed516aaa199a283a5042f6adf3b60ae45d54` and ACAD9 #3152 merged at 22:25:09
  as `e0d565bddebefd72f7c1c32562b588f75a893f69`; both final heads were approved
  and required CI succeeded. The local working tally at that point was nine complete;
  it was not a separately published project snapshot.
  Published ACADVL #3157 (42 source rows, clean validation) and ACAT1 draft #3158
  (49 source rows, eight missing donor caches listed). Published quote-scope
  corrections for ABCC9, matching binding judgments for ACADS, chemistry/provenance
  corrections for ACADSB, and the glycogen participation correction for ACADM.
  The unpublished local queue then recorded thirteen latest revisions and 84 hashes, verified against
  their recorded Git trees. ABCC9's latest four-file follow-up replaces its earlier
  34-file initial manifest; historical commits retain the earlier snapshot.
  Receipts identify published trees, not necessarily each PR's live head.

- 2026-09-26 22:38 UTC: Reviewed feedback on drafts as well as ready PRs. ABCC8
  needs a cache-availability flag correction; ABCD1 needs its elongation actions
  reconciled with source evidence; ACAN needs binding, localization, qualifier and
  narrative corrections. All retain required missing-cache gates. ACADM's biological
  blocker is resolved; its missing PMID:18459129 cache still blocks readiness.
  ACOX2 research is preserved while ACAN feedback takes priority. Targeted fetches
  and a read-only search of available local checkouts and current main found none
  of the missing publication caches; no replacements were invented.

- 2026-09-26 23:10 UTC: Confirmed four further completed genes: ABCB4 #3135 at 22:41:04,
  ACADS #3155 at 22:46:40, ABCC9 #3148 at 22:49:06, and ACADSB #3154 at
  22:57:39 UTC. Each final head was approved and required CI passed. The inventory
  now checks 13 of 2,876 genes complete. Project progress PR #3137 also merged;
  this is a separate tracking snapshot. Published ACOX1 #3159, ACSL4 #3160 and
  ACOX2 #3161 as drafts with explicit required-cache gates. Updated ACAN, ABCC8,
  ABCD1, ACAT1 and ACADVL follow-ups. The queue records 16 latest revisions and
  64 file hashes, all checked against their immutable published Git trees.
  Earlier larger manifests remain recoverable through their publication receipts.

- 2026-09-26 23:10 UTC: ACAN and ABCC8 re-reviews accepted the biological fixes
  and clarified that citation verification and cache availability are separate.
  Missing caches still prevent undrafting. ABCC8 identifier-spacing feedback is
  corrected in current prose and a new history record; published history remains
  unchanged. Notes-inclusive citation checks also identified ACSL4 PMID:23766516
  and six ACOX2 missing records, now explicit in their draft gates. Ordinary PubMed
  endpoint and fetch retries still failed DNS despite an unrelated institutional
  PDF download succeeding. No source or research report was fabricated.

- 2026-09-26 23:20 UTC: Corrected the provenance explanation for two generated
  history filenames carrying the scaffolder's default `claude-code` actor token.
  Codex performed the work; `--agent-tool codex` had been supplied but the separate
  `--actor-name codex` option was omitted. Actor metadata was corrected afterward;
  filenames and session ids were generated by the helper, not hand-written. New
  correctly scaffolded records document this explanation for ABCC8 and this project.
  Previously published history remains unchanged under the append-only rule.
  Future commands supply both actor name and agent tool explicitly. No inventory,
  biological judgment or publication receipt changes in this clarification.

- 2026-09-26 23:35 UTC: Confirmed ACADVL #3157 merged at 23:27:27 UTC as
  `af7a6ea1c9a6dd7ceecc8b04b120577d1a4070cb` after final-head approval and successful CI.
  The campaign total is 14 of 2,876 genes. ACTA1 #3163 and ACTA2 #3164 are published;
  ACTA1 review feedback is being addressed. ABCC8 and ACSL4 current heads are approved
  but remain drafts for their missing source caches. ACOX2 reaction and preparation-scope
  follow-up is published as a draft. ACTB and ADA are under substantive review. ADA is
  the next cached Definitive gene after unseeded ACTC1, ACTG1, ACTN1, ACTN2, ACVR1,
  ACVRL1 and ACY1 under the documented temporary source-access scheduling exception.

- 2026-09-26 23:35 UTC: Recovered the omitted ABCC8 `31c9d66b` publication receipt.
  Its original four-file manifest matches the immutable published blobs and the
  independently preserved local commit `7f3bf739` has the exact published tree.
  Historical receipts now include deterministic changed-file manifests and hashes,
  ordered newest first with parent continuity checked. The current queue records
  18 latest revisions and 71 file hashes; 8 of these PRs are merged, while the first
  6 campaign completions predate this queue. Correctly scaffolded history links this
  snapshot to PR #3162 and preserves the earlier generated actor-token record.

- 2026-09-27 00:05 UTC: Project #3162 merged as `62134e998e0e4fbda34cc79564fb081e8dbbd951`.
  Published ACTB #3184 and ADA #3179 as drafts after independent audits and targeted
  validation; their required source-cache gaps remain explicit. ACOX2 received final-head
  approval after restoring the exact upstream publication title. ACTA1 final head is
  approved with protected auto-merge enabled. ACTA2 follow-up is published; its automated
  reviewer failed before substantive execution, and one retry is queued. Gene and history
  steps in ACTA1 CI have passed while the remaining workflow runs. ADGRV1, ADNP and ADSL
  are under audit under the documented cached-gene scheduling exception.
  The local queue snapshot now records 20 latest revisions / 79 hashes and 20
  historical revisions / 142 hashes, with exact trees and parent continuity checked.

- 2026-09-27 00:10 UTC: Confirmed ACTA1 PR #3163 merged at 00:03:02 UTC as
  `1781be1cfc1f1f9b5e4be645c8fd1bb1ecb9d497` after current-head approval and successful CI.
  Checked its inventory row complete: 15 of 2,876 genes. This supersedes the earlier
  queued-auto-merge observation. The 20-entry queue now contains 9 merged PRs plus
  6 earlier campaign completions outside the queue. Project PR #3191 carries these
  shared tracking updates; gene-specific review work continues independently.
