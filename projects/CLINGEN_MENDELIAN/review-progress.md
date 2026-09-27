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
| ABCC8 | Definitive | No review | Merged; final-head substantive approval and required CI passed; all required source follow-ups merged | `cmungall/clingen-abcc8` | [#3136](https://github.com/ai4curation/ai-gene-review/pull/3136) |
| ABCC9 | Definitive | No review | Merged; final approval and required CI passed | `cmungall/clingen-abcc9` | [#3148](https://github.com/ai4curation/ai-gene-review/pull/3148) |
| ABCD1 | Definitive | No review | Merged; final-head approval and required CI passed; all required source caches published | `cmungall/clingen-abcd1` | [#3150](https://github.com/ai4curation/ai-gene-review/pull/3150) |
| ACAD8 | Definitive | INITIALIZED | Merged; final approval and required CI passed | `cmungall/clingen-acad8` | [#3151](https://github.com/ai4curation/ai-gene-review/pull/3151) |
| ACAD9 | Definitive | COMPLETE | Merged; final approval and required CI passed | `cmungall/clingen-acad9` | [#3152](https://github.com/ai4curation/ai-gene-review/pull/3152) |
| ACADM | Definitive | COMPLETE | Merged; final-head approval and required CI passed; all required source caches published | `cmungall/clingen-acadm` | [#3156](https://github.com/ai4curation/ai-gene-review/pull/3156) |
| ACADS | Definitive | COMPLETE | Merged; final approval and required CI passed | `cmungall/clingen-acads` | [#3155](https://github.com/ai4curation/ai-gene-review/pull/3155) |
| ACADSB | Definitive | INITIALIZED | Merged; final approval and required CI passed | `cmungall/clingen-acadsb` | [#3154](https://github.com/ai4curation/ai-gene-review/pull/3154) |
| ACADVL | Definitive | COMPLETE | Merged; final-head approval and required CI passed | `cmungall/clingen-acadvl` | [#3157](https://github.com/ai4curation/ai-gene-review/pull/3157) |
| ACAN | Definitive | COMPLETE | Merged; final-head approval and required CI passed; all required source caches published | `cmungall/clingen-acan` | [#3153](https://github.com/ai4curation/ai-gene-review/pull/3153) |
| ACAT1 | Definitive | COMPLETE | Original review merged; ready cache follow-up #3250 validates without warnings and awaits current checks | `cmungall/clingen-acat1` | [#3158](https://github.com/ai4curation/ai-gene-review/pull/3158) |
| ACOX1 | Definitive | INITIALIZED | Merged; final-head approval and required CI passed; all required source caches published | `cmungall/clingen-acox1` | [#3159](https://github.com/ai4curation/ai-gene-review/pull/3159) |
| ACOX2 | Definitive | INITIALIZED | Original review merged; draft cache follow-up #3248 closes six review/notes gaps; two hypothesis-only citations remain | `cmungall/clingen-acox2` | [#3161](https://github.com/ai4curation/ai-gene-review/pull/3161) |
| ACSL4 | Definitive | COMPLETE | Original review merged; ready cache follow-up #3247 awaits current-head review, CI and merge | `cmungall/clingen-acsl4` | [#3160](https://github.com/ai4curation/ai-gene-review/pull/3160) |
| ACTA1 | Definitive | COMPLETE | Merged; final-head approval and required CI passed | `cmungall/clingen-acta1` | [#3163](https://github.com/ai4curation/ai-gene-review/pull/3163) |
| ACTA2 | Definitive | COMPLETE | Merged; final-head approval and required CI passed; all cited publication caches available | `cmungall/clingen-acta2` | [#3164](https://github.com/ai4curation/ai-gene-review/pull/3164) |
| ACTB | Definitive | COMPLETE | Merged; final-head approval and required CI passed; all required sources published | `cmungall/clingen-actb` | [#3184](https://github.com/ai4curation/ai-gene-review/pull/3184) |
| ADA | Definitive | INITIALIZED | Original review merged; ready post-merge source follow-up #3263 awaits current-head review, required CI and merge | `cmungall/clingen-ada` | [#3179](https://github.com/ai4curation/ai-gene-review/pull/3179) |
| ADGRV1 | Definitive | COMPLETE | Ready; five visual/light rows retained as non-core and redundant core sound term removed; all source assertions preserved; current checks pending | `cmungall/clingen-adgrv1` | [#3192](https://github.com/ai4curation/ai-gene-review/pull/3192) |
| ADNP | Definitive | COMPLETE | Ready follow-up; source evidence and current reviewer comments addressed; final-head review and required CI pending | `cmungall/clingen-adnp` | [#3193](https://github.com/ai4curation/ai-gene-review/pull/3193) |
| ADSL | Definitive | INITIALIZED | Ready follow-up; source evidence and current reviewer comments addressed; final-head review and required CI pending | `cmungall/clingen-adsl` | [#3194](https://github.com/ai4curation/ai-gene-review/pull/3194) |
| AFG3L2 | Definitive | COMPLETE | Ready follow-up; source evidence and current reviewer comments addressed; final-head review and required CI pending | `cmungall/clingen-afg3l2` | [#3196](https://github.com/ai4curation/ai-gene-review/pull/3196) |
| AGK | Definitive | COMPLETE | Merged; final-head approval and required CI passed; all required source caches published | `cmungall/clingen-agk` | [#3195](https://github.com/ai4curation/ai-gene-review/pull/3195) |
| AGL | Definitive | INITIALIZED | Ready; four PMID and seven Reactome records published; all 35 decisions preserved; COMPLETE without warnings; current checks pending | `cmungall/clingen-agl` | [#3197](https://github.com/ai4curation/ai-gene-review/pull/3197) |
| AGO1 | Definitive | COMPLETE | Ready; stale access sentence corrected with all 113 decisions unchanged; all 38 review/notes PMIDs cached; current checks pending | `cmungall/clingen-ago1` | [#3207](https://github.com/ai4curation/ai-gene-review/pull/3207) |
| AGO2 | Definitive | COMPLETE | Original review merged; draft post-merge follow-up #3264 publishes eight PMIDs and one Reactome; two provider-only PMID caches remain | `cmungall/clingen-ago2` | [#3210](https://github.com/ai4curation/ai-gene-review/pull/3210) |
| AGPAT2 | Definitive | INITIALIZED | Merged; final-head approval and required CI passed; all required source caches published | `cmungall/clingen-agpat2` | [#3208](https://github.com/ai4curation/ai-gene-review/pull/3208) |
| AGPS | Definitive | INITIALIZED | Merged; final-head approval and required CI passed; all required source caches published | `cmungall/clingen-agps` | [#3209](https://github.com/ai4curation/ai-gene-review/pull/3209) |
| AGXT | Definitive | INITIALIZED | Merged; final-head approval and required CI passed; all required source caches published | `cmungall/clingen-agxt` | [#3212](https://github.com/ai4curation/ai-gene-review/pull/3212) |
| AHDC1 | Definitive | COMPLETE | Merged; final-head substantive approval and required CI passed; all required source follow-ups merged | `cmungall/clingen-ahdc1` | [#3213](https://github.com/ai4curation/ai-gene-review/pull/3213) |
| AHI1 | Definitive | COMPLETE | Ready follow-up; source evidence and current reviewer comments addressed; final-head review and required CI pending | `cmungall/clingen-ahi1` | [#3215](https://github.com/ai4curation/ai-gene-review/pull/3215) |
| AKT1 | Limited | COMPLETE | Draft; 54 Reactome records and verified full-text replacement published; all 445 decisions preserved; three correction PMIDs remain | `cmungall/clingen-akt1` | [#3242](https://github.com/ai4curation/ai-gene-review/pull/3242) |
| AGRN | Definitive | COMPLETE | Draft #3243; three PMID caches remain; review service stopped at its session limit without submitting a review | `cmungall/clingen-agrn` | [#3243](https://github.com/ai4curation/ai-gene-review/pull/3243) |
| AHCY | Definitive | COMPLETE | Draft #3244; six PMID caches remain; review service stopped at its session limit without submitting a review | `cmungall/clingen-ahcy` | [#3244](https://github.com/ai4curation/ai-gene-review/pull/3244) |
| AIMP1 | Definitive | COMPLETE | Draft #3262; all 50 seeded assertions audited, two cores; seven required publication caches remain | `cmungall/clingen-aimp1` | [#3262](https://github.com/ai4curation/ai-gene-review/pull/3262) |
| AIMP2 | Definitive | COMPLETE | Draft #3256; all 51 seeded assertions audited, one scaffold core, two prior NEW proposals withdrawn; five publication caches remain | `cmungall/clingen-aimp2` | [#3256](https://github.com/ai4curation/ai-gene-review/pull/3256) |
| AIPL1 | Definitive | COMPLETE | Draft #3257; 13 seeded assertions and prior HSP90 NEW audited; human citation corrected; two notes-only publication caches remain | `cmungall/clingen-aipl1` | [#3257](https://github.com/ai4curation/ai-gene-review/pull/3257) |
| AIRE | Definitive | COMPLETE | Draft #3265; all 55 assertions audited, one integrated core, 36 reference assessments; twelve publication caches remain | `cmungall/clingen-aire` | [#3265](https://github.com/ai4curation/ai-gene-review/pull/3265) |
| AKR1D1 | Definitive | INITIALIZED | Draft #3266; independent full audit published; validation, history, rendering and source-preservation checks passed; 6 publication and 1 Reactome caches remain | `cmungall/clingen-akr1d1` | [#3266](https://github.com/ai4curation/ai-gene-review/pull/3266) |
| ALAS2 | Definitive | INITIALIZED | Draft #3267; independent full audit published; validation, history, rendering and source-preservation checks passed; 2 publication and 0 Reactome caches remain | `cmungall/clingen-alas2` | [#3267](https://github.com/ai4curation/ai-gene-review/pull/3267) |
| ALDH18A1 | Definitive | INITIALIZED | Draft #3269; independent full audit published; validation, history, rendering and source-preservation checks passed; 7 publication and 0 Reactome caches remain | `cmungall/clingen-aldh18a1` | [#3269](https://github.com/ai4curation/ai-gene-review/pull/3269) |
| ALDH4A1 | Definitive | COMPLETE | Draft #3271; independent full audit published; validation, history, rendering and source-preservation checks passed; 1 publication and 0 Reactome caches remain | `cmungall/clingen-aldh4a1` | [#3271](https://github.com/ai4curation/ai-gene-review/pull/3271) |
| ALDH5A1 | Definitive | INITIALIZED | Draft #3268; independent full audit published; validation, history, rendering and source-preservation checks passed; 3 publication and 0 Reactome caches remain | `cmungall/clingen-aldh5a1` | [#3268](https://github.com/ai4curation/ai-gene-review/pull/3268) |
| ALDH7A1 | Definitive | IN_PROGRESS | Full audit in progress; exact main baseline and canonical/alias overlap verified | — | — |

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
before publishing a follow-up, and keep project tracking in its own PR. Five
merged original reviews still require follow-up merges before campaign completion:
ACSL4, ACAT1, ACOX2, ADA and AGO2. Their follow-up PRs are #3247, #3250, #3248,
#3263 and #3264. ABCC8's source follow-up #3211 has merged. ADA's required caches
are published in its ready follow-up; AGO2 still needs two provider-only citations,
and ACOX2 still needs two hypothesis-only citations.

The second bounded read-only source recovery imported eight publication records
and 65 Reactome records after artifact and individual hash checks. AKT1's full-text
candidate was subsequently assessed against the primary source and published in
its gene PR. [Exact second-batch import receipt](reference-recovery2.json).
The third recovery remains queued for 14 PMIDs and eight initial gene seeds:
ABCG5, ABCG8, ABHD12, ABHD5, AICDA, AGTPBP1, AIFM1 and AK2 remain unseeded until
actual results are verified. The fourth recovery is queued for 27 PMIDs needed by
AIMP1, AIMP2, AIPL1, AGO2 and AIRE. The fifth is queued for 15 PMIDs and one
Reactome record needed by AKR1D1, ALAS2 and ALDH18A1. No retrieval success is assumed.

New full audits and the next active reviews are recorded in the table above.
AKT1's Limited-tier audit remains an explicit scheduling exception; it does not
change tier order or complete earlier unavailable genes. Failed provider attempts
remain documented without invented reports. AGRN and AHCY's review service runs
reported a session limit, with reset at 06:00 UTC; those runs submitted no reviews.
Local review and validation continue while their normal approval gates remain open.

The complete log of ABCB4's second review attempt reports the review account's
session limit, with reset at **2026-09-27 01:00 UTC**. That earlier comment accepted the biological fixes, but did not record formal approval at the time. ABCB4 later received current-head approval and merged.
The subsequent ABCB4 and ABCC9 reviews completed with concrete changes requested. Later ACAD8 and ACAD9 workflow runs completed successful reviews before that reset
time, demonstrating that the earlier failure was no longer universal. Reran the
earlier failed ABCB4 and ABCC9 reviews after that new evidence. Keep the normal
approval and CI gates and inspect each current run rather than assuming a fixed
outage window.

Merged project setup PR: [#3126](https://github.com/ai4curation/ai-gene-review/pull/3126).

The earliest unseeded nuclear protein-coding Definitive gene is **ABCG5**. **27 of
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

- 2026-09-27 00:27 UTC: Published ADGRV1 #3192, ADNP #3193 and ADSL #3194 after
  independent biological review and targeted validation. Required publication-cache
  gaps keep all three in draft. Current-head automated reviews for ACTA2, ADA, ACTB
  and ADGRV1 failed before substantive execution; ACTA2 also failed on its single
  retry. Logs report zero cost and no permission denials, but do not expose the
  provider reason. No repeated retries are scheduled without new recovery evidence.
  ACTA2 code validation passed. AFG3L2, AGK and AGL are now under substantive audit.
  Verified 23 latest receipts / 91 file hashes and 20 historical receipts / 142 hashes,
  including exact local/published tree equality and continuous follow-up parents.
  The completion count remains 15 of 2,876; publishing drafts does not advance it.

- 2026-09-27 00:35 UTC: AGK #3195 is published as a draft after independent review
  and validation; two required publication caches remain. AGO1 is under audit after
  exact current-main baseline and canonical/alias overlap checks. The queue now
  includes 24 latest revisions / 95 hashes and 20 historical revisions / 142 hashes.
  ADNP and project #3191 also encountered the same automated-review startup failure.
  ADA code validation passed. ADGRV1 CI identified a newly added reference-title
  format mismatch; its separate gene follow-up is being validated locally.

- 2026-09-27 00:51 UTC: Published AFG3L2 #3196 and AGL #3197 as drafts with
  explicit source-cache requirements. ADGRV1 #3192 now carries the validated exact
  fetched-title correction; its initial receipt remains in the immutable history.
  Verified 26 latest receipts / 103 file hashes and 21 historical receipts / 146
  hashes, with local/published tree equality and continuous follow-up parents.
  The repository agent ai4c-agent independently merged ABCC8, ACAT1, ACSL4 and
  ACOX2 at 00:42:49, 00:43:00, 00:43:12 and 00:43:24 UTC, respectively. Their
  final heads were approved and code CI passed. All four retain the recorded
  missing-source follow-ups, so there are 19 merged gene PRs but still 15 fully
  complete inventory entries. Source requirements are not waived by merge.
  A substantive successful ACSL4 post-merge review demonstrates reviewer-service
  recovery; ACTA2 and ADA reruns are queued. No cache artifacts were retained by
  the checked CI workflow, and no source cache was fabricated. AGO1, AGO2 and
  AGPAT2 audits continue. Project links use the verified 1781be1c gene index;
  subsequent remote merges add bacterial reviews but no human review directories.

- 2026-09-27: Published AGO1 #3207, AGPAT2 #3208, AGPS #3209, AGO2 #3210 and AGXT #3212,
  and validated follow-ups for ACTA2, ADA, ADGRV1, AGK, AGL, AGO1, AGPAT2, ADNP and ADSL.
  The queue now verifies 31 latest revisions / 123 file hashes and 30 historical
  revisions / 182 hashes against exact local and published trees. ABCC8
  [post-merge correction #3211](https://github.com/ai4curation/ai-gene-review/pull/3211)
  has a separate four-file receipt based on current main; its original merged PR
  and all earlier receipts remain intact. Source-cache requirements are unchanged.
  There are 37 genes with audit PRs, 19 original PRs merged and 15 completed
  inventory rows. AHDC1 audit continues; ACTB review feedback is being
  addressed. ACTA2 protected auto-merge waits for its current checks.
  Exact current main a18dacfd was reconstructed in the independent writable
  checkout from 120 real, hash-verified blobs; the protected original Git metadata
  was untouched. Its gene index contains 4,996 review paths, including newly
  merged human ABCC8 and seven bacterial reviews. This corrects the earlier
  assumption that the intervening merges added no human review directory.
  Recent ADNP, ADSL and AFG3L2 workflow logs explicitly report the review account
  usage limit. Later ACTA2, ADA and AGK heads received substantive approvals;
  AGO1/AGO2/AGPAT2/AGPS comments are being assessed independently. No quota reset time is inferred.

- 2026-09-27: ACTA2 #3164 merged at 01:52:05 UTC as `9541f70405e9e9bef718106c32ec1a54a8051bda` after final-head approval and required CI. Its 32 cited PMIDs are cached; the inventory now has 16 completed genes. The campaign has 20 original merged gene PRs, four still requiring source follow-ups. AHDC1 #3213 brings the audited set to 38 genes. Published validated follow-ups for ACTB, AGO1, ADSL, AGPS, AGPAT2 and AGO2, preserving each original source assertion and earlier receipt. The queue verifies 32 latest revisions/127 hashes and 36 historical revisions/206 hashes, plus the separate ABCC8 post-merge receipt.
  Read-only standard-reference recovery run [36286975328](https://github.com/ai4curation/ai-gene-review/actions/runs/36286975328) succeeded for its bounded 67-request list. Its artifact transfer and hash verification remain pending; no source requirement is declared cleared merely from run success. AHI1 and AKT1 substantive audits continue. AICDA initialization failed normal UniProt DNS access and remains unseeded.

  AKT1 is in the Limited tier. Its already-started cached audit is an explicit scheduling exception while earlier gene initialization is unavailable; it does not change tier order or mark intervening genes complete.

- 2026-09-27 02:50 UTC: AHI1 [#3215](https://github.com/ai4curation/ai-gene-review/pull/3215) brings the campaign to 39 audited genes. Its four missing notes-inclusive references remain explicit. Published and marked ready the validated source-cache follow-ups for ABCD1, ACAN, ACADM, ACOX1, ADSL, AGPS, AGPAT2, AGK and ADNP. AGXT is ready after its specificity/evidence follow-up; AFG3L2 remains draft for its newly examined human-protein source. These PRs await current-head review and CI, so the completed inventory remains 16 of 2,876 genes.
  The queue now verifies 33 latest receipts / 157 hashes and 47 historical receipts / 250 hashes, plus the separate ABCC8 post-merge receipt. All earlier receipt chains are preserved.
  The read-only recovery and transport runs delivered 67 genuine machine-generated publication records (17 full text, 50 abstracts). ZIP and record hashes were checked before local import; the [recovery manifest](reference-recovery.json) records exact provenance and file hashes. Cache availability does not imply full-text access, biological certainty or campaign completion. Remaining local records are being assessed and included in their respective gene follow-ups. A second bounded source-fetch workflow is in preparation for newly cited papers and missing Reactome records. AKT1 substantive review continues.

- 2026-09-27: The second bounded source-recovery run [36289953066](https://github.com/ai4curation/ai-gene-review/actions/runs/36289953066) is queued at exact task-branch head `fecff1befb769b1753300fa1bc2e3442813e9dd2`. It requests nine papers and 65 cited Reactome records using normal fetchers, read-only permissions and temporary output directories. A metadata-only AKT1 record will be retrieved as a separate comparison candidate. The first dispatch was rejected because runner context was unavailable in job-level environment settings; moving those two paths to runner initialization fixed the workflow without changing the source list or fetcher. No source-recovery result is claimed before verified artifact import. AGRN substantive review has started; AKT1 continues.

- 2026-09-27 03:36 UTC: Completed protected merges for AGXT #3212, ABCD1 #3150, ACAN #3153, ACADM #3156 and ACOX1 #3159 after final-head approvals and passing required CI. Campaign completion is 21 of 2,876; 25 original gene PRs are merged and four still require their post-merge follow-ups. The exact current main is `23787fa952f4d41c0b92795752e367b2d9a207b1`; its 4,997 review paths include newly merged human ABCD1.
  Published draft substantive audits AKT1 #3242 (445 seeded annotations), AGRN #3243 (102) and AHCY #3244 (25 plus a retained prior NEW with corrected evidence), bringing the campaign to 42 audited genes. ADGRV1, ACTB, AGO1 and AHDC1 source-cache follow-ups are ready. ABCC8 #3211 and new ACAT1 #3250 / ACSL4 #3247 follow-ups are ready; ACOX2 #3248 remains draft for its separate hypothesis-only citations. All earlier provenance chains are preserved. AIMP1 and AIMP2 substantive audits continue; current-head ADSL, AFG3L2 and AHI1 feedback is being assessed.
  Verified 36 latest receipts / 180 hashes, 51 historical receipts / 266 hashes and 5 post-merge revision receipts / 35 hashes across four PRs. Source recovery batch2 is queued, with no result inferred.

- 2026-09-27 04:16 UTC: AGK #3195, AGPAT2 #3208 and AGPS #3209 completed final-head-approved, required-CI-green protected merges. Completion is now 24 of 2,876. ADA #3179 and AGO2 #3210 subsequently merged independently and still require their source-cache follow-ups: 30 original reviews are merged, six not yet campaign-complete. The exact current-main snapshot is `3e4b386077392a633b451112065243c8577d132b`, with 4,998 review paths; all 18 intervening commits were imported with verified trees and source blobs.
  Published AIMP1 #3262, AIMP2 #3256 and AIPL1 #3257 after independent full biological audits and passing checks, reaching 45 audited genes. Their seven, five and two missing citation caches remain explicit draft gates. ADSL, AFG3L2, AHI1 and ADNP follow-ups were published after source/quotation/core or audit-harness corrections; AFG3L2 and AHI1 have no remaining required-cache gaps. AIRE review and ADA/AGL/AGO2/AKT1 source closures continue.
  Preserved prior provenance chains; verified 39 latest receipts / 190 hashes, 55 historical receipts / 294 hashes and 5 post-merge revision receipts / 35 hashes. Source2 imported 73 canonical records plus one isolated candidate; source3 remains queued.

- 2026-09-27: ACTB #3184 completed its approved, required-CI-green protected merge at 04:26 UTC (`c7078166039c9abd5c62704489283403eb520007`), bringing campaign completion to 25 of 2,876. There are 31 merged original gene PRs; six remain incomplete pending their follow-up merges. AIRE #3265 brings dedicated audit PRs to 46 genes, with 12 explicit cache gaps remaining. ADA #3263 and AGO2 #3264 preserve their original merged receipts while publishing source follow-ups.
  Published AGL source closure (all required records), AKT1 source2 follow-up (three PMID gates remain), AGO1 stale-access correction (all 113 decisions unchanged), and ADGRV1 physiological-scope/core-redundancy follow-up. Current ABCC8 and AHDC1 heads received substantive approvals; required tests were still in progress at 04:41 UTC. Batch4 run 36294925088 is queued for 27 deduplicated PMIDs; batch3 is also queued. AKR1D1 and ALAS2 source baselines and canonical/alias overlaps were verified before editing; ALDH18A1 preflight continues.
  Verified 40 latest receipts / 253 hashes, 59 historical receipts / 317 hashes, and 7 post-merge revision receipts / 61 hashes. Every prior receipt chain is preserved. Rendering uses the exact imported ACTB merge snapshot; its 4,998 review paths are unchanged from the preceding snapshot.

- 2026-09-27: ABCC8 follow-up #3211 and AHDC1 #3213 completed current-head-approved, required-CI-green protected merges at 04:47 UTC. Campaign completion is 27 of 2,876, with 32 original gene PRs merged and five still requiring follow-ups.
  Published AKR1D1 #3266, ALAS2 #3267, ALDH18A1 #3269, ALDH4A1 #3271, ALDH5A1 #3268. There are 51 dedicated gene audit PRs. Draft source gaps remain explicit. Batch5 run 36295820535 is queued, as are batches3 and4; queued jobs are not successful recoveries.
  Verified 45 latest receipts / 273 hashes, 59 historical receipts / 317 hashes, and 7 post-merge revision receipts / 61 hashes. Every prior receipt chain and original merge is preserved. Rendering uses the exact imported AHDC1 merge snapshot.
