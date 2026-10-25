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

## Completion checkpoint 394 — 2026-10-13 16:34:02 UTC

**394 complete / 2,482 remaining in the frozen 2,876-gene catalogue.**
This checkpoint adds 44 distinct gene reviews to the merged checkpoint 350.
The cutoff is the final CPT1A merge `a9655bc9362c58342ad7a7d077637d13d75a3d49`.

The original checkpoint omitted CPAMD8 despite its actual merge at 12:58:43 UTC,
before this cutoff. Its [final approval](https://github.com/ai4curation/ai-gene-review/pull/4961#pullrequestreview-5494780287)
and [detailed review](https://github.com/ai4curation/ai-gene-review/pull/4961#issuecomment-6130393612)
leave no blocking request. The [ordinary merge-group validation](https://github.com/ai4curation/ai-gene-review/actions/runs/38397964845/job/115297920929)
passed before the merge. All 15 approved modes, types and blobs match the merge;
its complete parent delta is exactly those 15 paths. This corrects the omission
without moving the cutoff or counting later merges.

| Gene | PR | Approved head | Merge time UTC | Merge commit | Full PR paths | Parent delta |
|---|---|---|---|---|---:|---:|
| CLN6 | [#4717](https://github.com/ai4curation/ai-gene-review/pull/4717) | `f49f0215585d9810b909d581af9526c39478872a` | 2026-10-12T17:38:25Z | [7d915faa876d](https://github.com/ai4curation/ai-gene-review/commit/7d915faa876d30e0bfb6767b7f97b5e3c0b35f1f) | 45 | 45 |
| COL6A3 | [#4943](https://github.com/ai4curation/ai-gene-review/pull/4943) | `ba6811be38e4cc73ebb2dd37b79f3c86e7e06a62` | 2026-10-12T18:04:09Z | [e565df36bca8](https://github.com/ai4curation/ai-gene-review/commit/e565df36bca8b4576db502478a555d1bf8b81020) | 32 | 20 |
| CLN3 | [#4704](https://github.com/ai4curation/ai-gene-review/pull/4704) | `9e12ec8e19eec2b044c0531a4395524ef42045af` | 2026-10-12T18:22:43Z | [7daf2acc4586](https://github.com/ai4curation/ai-gene-review/commit/7daf2acc4586a5a520a276b3c76245f52444afff) | 23 | 21 |
| CLN8 | [#4722](https://github.com/ai4curation/ai-gene-review/pull/4722) | `7cc52a288ae8cebd9f4df6a09590c2c7ae1b9414` | 2026-10-12T18:43:29Z | [dc8bc5b2c884](https://github.com/ai4curation/ai-gene-review/commit/dc8bc5b2c88408ee0743bcdfa0db2d4428196680) | 17 | 14 |
| CLPP | [#4733](https://github.com/ai4curation/ai-gene-review/pull/4733) | `09926b14b66defe050738f59887c14d26cf26408` | 2026-10-12T19:05:40Z | [8a0bae1506be](https://github.com/ai4curation/ai-gene-review/commit/8a0bae1506be4345f6da2f96e6c64e01312b6312) | 8 | 8 |
| CNTNAP2 | [#4841](https://github.com/ai4curation/ai-gene-review/pull/4841) | `5074fc70da81979f6ef36164659d599a44eedb5c` | 2026-10-12T19:30:59Z | [d79d76cb2029](https://github.com/ai4curation/ai-gene-review/commit/d79d76cb2029578a346bbccd66ee794d7d994dbc) | 21 | 21 |
| CNNM4 | [#4794](https://github.com/ai4curation/ai-gene-review/pull/4794) | `7aa3425f439285db4e5a0439afeb6f1f3937bee4` | 2026-10-12T19:56:02Z | [3ebf728a1d03](https://github.com/ai4curation/ai-gene-review/commit/3ebf728a1d03536be3e879f04c47da5e3358cc79) | 16 | 16 |
| COG4 | [#4872](https://github.com/ai4curation/ai-gene-review/pull/4872) | `f65662ed586b956ebb31f3ddafd79196b35c2b5d` | 2026-10-12T20:13:55Z | [b22904f4f1d3](https://github.com/ai4curation/ai-gene-review/commit/b22904f4f1d3fcb06369bf34c28bde0c7cf4e24c) | 16 | 14 |
| COL7A1 | [#4944](https://github.com/ai4curation/ai-gene-review/pull/4944) | `fa493c4929b48feca35eb4a638911d630bacb90c` | 2026-10-12T20:35:33Z | [3256629f18e0](https://github.com/ai4curation/ai-gene-review/commit/3256629f18e0fdbd5e6321346dd71e0f76341687) | 30 | 30 |
| COG7 | [#4912](https://github.com/ai4curation/ai-gene-review/pull/4912) | `65c1f800ebbf4ccdff1e839f5e4fa51fb210475c` | 2026-10-12T20:59:59Z | [803eff6ca53b](https://github.com/ai4curation/ai-gene-review/commit/803eff6ca53b70018349c99195f451920972f979) | 16 | 14 |
| COL11A2 | [#4918](https://github.com/ai4curation/ai-gene-review/pull/4918) | `08102d2ca1d0dc0ef6ea79391b63dcc6c0d6125d` | 2026-10-12T21:24:10Z | [b59857269769](https://github.com/ai4curation/ai-gene-review/commit/b59857269769c0a39fe5de480614e336c741e38a) | 19 | 19 |
| CNNM2 | [#4791](https://github.com/ai4curation/ai-gene-review/pull/4791) | `fea62aab7284f228db1e605558f9c98d5108228e` | 2026-10-12T21:49:22Z | [69df7d3a5071](https://github.com/ai4curation/ai-gene-review/commit/69df7d3a5071f865111be4691f7d26d86018438d) | 22 | 19 |
| COL9A1 | [#4945](https://github.com/ai4curation/ai-gene-review/pull/4945) | `81a76e778330d253be6c205b7a104b6e9c36f42e` | 2026-10-12T22:15:26Z | [81a43a71cfc9](https://github.com/ai4curation/ai-gene-review/commit/81a43a71cfc99fc205ee1e531e442f55c4817ba8) | 19 | 19 |
| COA8 | [#4870](https://github.com/ai4curation/ai-gene-review/pull/4870) | `201df218220b05783e0056a6a57c9f841846af9a` | 2026-10-12T22:36:18Z | [0325db35893b](https://github.com/ai4curation/ai-gene-review/commit/0325db35893b793cc08a6e1c07afa4516952355c) | 16 | 16 |
| COCH | [#4871](https://github.com/ai4curation/ai-gene-review/pull/4871) | `58ca87ff3e564c7684a6a1cf5694e400ec4061c4` | 2026-10-12T22:54:22Z | [ed000cae872f](https://github.com/ai4curation/ai-gene-review/commit/ed000cae872f15c07cf99b2fb56daefa9ac6fcba) | 23 | 23 |
| COL2A1 | [#4931](https://github.com/ai4curation/ai-gene-review/pull/4931) | `2ada5e144cac4fdea13cb88ffdcd53fab5d7ecc4` | 2026-10-12T23:13:45Z | [f1097102f74a](https://github.com/ai4curation/ai-gene-review/commit/f1097102f74ab95ef198faf651d08b4a38d3edc6) | 34 | 29 |
| COL18A1 | [#4919](https://github.com/ai4curation/ai-gene-review/pull/4919) | `a2d6b3f2562ded2bb812b11c6d23292138ee1928` | 2026-10-12T23:39:25Z | [c24d195707c7](https://github.com/ai4curation/ai-gene-review/commit/c24d195707c715e4e0483c8d0a667c76d1f292dd) | 31 | 30 |
| COL1A1 | [#4921](https://github.com/ai4curation/ai-gene-review/pull/4921) | `d1d3ae87eff5bb58c2d52e9c891af4afe630fa76` | 2026-10-13T00:04:36Z | [84cdd162363b](https://github.com/ai4curation/ai-gene-review/commit/84cdd162363b825b6eb8f4a961cdf0d14436f1cf) | 47 | 47 |
| CNGA1 | [#4746](https://github.com/ai4curation/ai-gene-review/pull/4746) | `92905a9d99d85e97c9728c2574f006bc6f7ea5be` | 2026-10-13T00:31:17Z | [c494c60261c2](https://github.com/ai4curation/ai-gene-review/commit/c494c60261c2ffbfed9a3e89d3558a44c2252179) | 20 | 11 |
| CLRN1 | [#4736](https://github.com/ai4curation/ai-gene-review/pull/4736) | `a0bc87d865903004de6c52c9c0a5d3d0a34f8187` | 2026-10-13T00:53:00Z | [61ba4c431e43](https://github.com/ai4curation/ai-gene-review/commit/61ba4c431e435e90248eb0f12774b7c6d8562515) | 15 | 15 |
| COA6 | [#4857](https://github.com/ai4curation/ai-gene-review/pull/4857) | `9398a5da2d1038ffb3752258e1fda2a13c9e450b` | 2026-10-13T01:11:02Z | [1e778d3c04c2](https://github.com/ai4curation/ai-gene-review/commit/1e778d3c04c230535b5348b2e356abbac6460948) | 10 | 10 |
| COL3A1 | [#4932](https://github.com/ai4curation/ai-gene-review/pull/4932) | `bed5cc754e5f5e0f025463389118484cdc091477` | 2026-10-13T01:36:52Z | [aa2a8779acf6](https://github.com/ai4curation/ai-gene-review/commit/aa2a8779acf63d1aa325da88efc1c1b7cf0a6b9e) | 41 | 38 |
| COL10A1 | [#4916](https://github.com/ai4curation/ai-gene-review/pull/4916) | `ac8aaeca977ec833099771024aa3c589075bc5a8` | 2026-10-13T01:58:34Z | [70e5b6140518](https://github.com/ai4curation/ai-gene-review/commit/70e5b6140518d4eb6d21222585d072569dd3cc93) | 16 | 14 |
| COA7 | [#4866](https://github.com/ai4curation/ai-gene-review/pull/4866) | `16fa6255c3002e5a2bcb518fdf5937ad275a2b01` | 2026-10-13T02:23:37Z | [0ee74dc9812b](https://github.com/ai4curation/ai-gene-review/commit/0ee74dc9812b1ad9afe20dd7a30153f35934dca3) | 10 | 10 |
| COL9A3 | [#4946](https://github.com/ai4curation/ai-gene-review/pull/4946) | `246a667cd9ec769d6a17c32891e44f290b9009c2` | 2026-10-13T02:48:51Z | [43b6bd2bfe31](https://github.com/ai4curation/ai-gene-review/commit/43b6bd2bfe31390c5de2d1f375d3397b913110fe) | 14 | 9 |
| COL4A5 | [#4936](https://github.com/ai4curation/ai-gene-review/pull/4936) | `02d6ec7bad1394e8dee0b0d6baff8088122220a0` | 2026-10-13T03:11:02Z | [b15b0e0879c9](https://github.com/ai4curation/ai-gene-review/commit/b15b0e0879c93fd9c1cf46d7cbbd99cd6f7cbfd7) | 20 | 20 |
| COL4A3 | [#4934](https://github.com/ai4curation/ai-gene-review/pull/4934) | `5f9454f5ea1201dac4686ee0d381a837c824d156` | 2026-10-13T03:31:57Z | [2b4dcaf9c440](https://github.com/ai4curation/ai-gene-review/commit/2b4dcaf9c44052a6eaffa0e1ac607822731041eb) | 28 | 24 |
| COL5A1 | [#4937](https://github.com/ai4curation/ai-gene-review/pull/4937) | `ef531e3cb41553cdcdb55259518e366a5dd62a02` | 2026-10-13T03:58:00Z | [e3fdba00c248](https://github.com/ai4curation/ai-gene-review/commit/e3fdba00c248bfb276b36ac5c2f2faee1e0bb5f2) | 28 | 24 |
| COL1A2 | [#4928](https://github.com/ai4curation/ai-gene-review/pull/4928) | `f2f01c7e3c1d256f7b70c46522d563e521802557` | 2026-10-13T04:21:39Z | [ff03322aaefa](https://github.com/ai4curation/ai-gene-review/commit/ff03322aaefa1fc98548241a2cf669ab82b5082f) | 12 | 11 |
| COL4A4 | [#4935](https://github.com/ai4curation/ai-gene-review/pull/4935) | `e18da0afbb44026347921a93b05ac94e3ad9cfd5` | 2026-10-13T04:46:58Z | [63b613d7142b](https://github.com/ai4curation/ai-gene-review/commit/63b613d7142bfb955d92cd0fe9d928733e4b37e9) | 19 | 16 |
| COL5A2 | [#4938](https://github.com/ai4curation/ai-gene-review/pull/4938) | `4711c9d5beb0df208488a18d2f05659e3cf4a97f` | 2026-10-13T05:07:20Z | [1d51d6d60861](https://github.com/ai4curation/ai-gene-review/commit/1d51d6d60861dab1f148901ba15a55d8e80ebe4f) | 22 | 12 |
| COL4A1 | [#4933](https://github.com/ai4curation/ai-gene-review/pull/4933) | `50af702da83e1714048d0786e56207e73636c2f7` | 2026-10-13T05:57:31Z | [b4b1dae2ede9](https://github.com/ai4curation/ai-gene-review/commit/b4b1dae2ede98c83a0fba2f1e8c0aa0fe6deed08) | 12 | 12 |
| CORO1A | [#4952](https://github.com/ai4curation/ai-gene-review/pull/4952) | `ef0febd87a4d4ae888df1ff2bdd911f72fd4ddb3` | 2026-10-13T07:02:29Z | [95c769b1c1cd](https://github.com/ai4curation/ai-gene-review/commit/95c769b1c1cd36316bd1b722e27c868c9abb3a1d) | 31 | 31 |
| COX10 | [#4953](https://github.com/ai4curation/ai-gene-review/pull/4953) | `2023f325c91b0d9221e0e014363396598a8ab322` | 2026-10-13T07:27:37Z | [c1574b6f0d59](https://github.com/ai4curation/ai-gene-review/commit/c1574b6f0d59975ffd9fb34faa2ed8847525d67a) | 9 | 9 |
| COMP | [#4951](https://github.com/ai4curation/ai-gene-review/pull/4951) | `0725b4c9b97b1dcb3763ef5980ee4244a4658bf4` | 2026-10-13T07:54:10Z | [4d00a6de6693](https://github.com/ai4curation/ai-gene-review/commit/4d00a6de66934299f14016e155001cb8c031a2e2) | 22 | 22 |
| COX15 | [#4956](https://github.com/ai4curation/ai-gene-review/pull/4956) | `280c9b4d93a163e226f2a8b801b0a20342ab5aa6` | 2026-10-13T08:13:10Z | [a90e9a2afbea](https://github.com/ai4curation/ai-gene-review/commit/a90e9a2afbea1bb7911097f9ffe87736084b1161) | 8 | 8 |
| COX6B1 | [#4957](https://github.com/ai4curation/ai-gene-review/pull/4957) | `b6d6eee9972a97e45df6bf4fab32d52af3804831` | 2026-10-13T08:31:27Z | [233c920c84b2](https://github.com/ai4curation/ai-gene-review/commit/233c920c84b24fa09c0a69c7f349641f0b7ed07d) | 9 | 9 |
| COXFA4 | [#4958](https://github.com/ai4curation/ai-gene-review/pull/4958) | `3d79a3ba499e2fee22bbfdd4c766054059a1b8e3` | 2026-10-13T10:09:26Z | [44d5a199822a](https://github.com/ai4curation/ai-gene-review/commit/44d5a199822a630b2c46ac69734618094b73e352) | 17 | 17 |
| CP | [#4959](https://github.com/ai4curation/ai-gene-review/pull/4959) | `ad2e58fbcefb3f7d3c81cbe4a7c8c0e1b0d1ba5a` | 2026-10-13T11:29:27Z | [4a1c58370745](https://github.com/ai4curation/ai-gene-review/commit/4a1c58370745fd99071dc53c531b9f4b52d62db6) | 25 | 25 |
| CPAMD8 | [#4961](https://github.com/ai4curation/ai-gene-review/pull/4961) | `bae41e46d9198aaed97ef99219318926f6305a14` | 2026-10-13T12:58:43Z | [6e66bd1c2eed](https://github.com/ai4curation/ai-gene-review/commit/6e66bd1c2eed3ec7a1254ea6caea596d62989858) | 15 | 15 |
| CPLANE1 | [#4964](https://github.com/ai4curation/ai-gene-review/pull/4964) | `27fb4d6bd9639dceb273d900f93c984775ab12e2` | 2026-10-13T13:25:46Z | [a87b3c1a87ed](https://github.com/ai4curation/ai-gene-review/commit/a87b3c1a87ed64ecb1906ffb048dbdbcb4fc80df) | 12 | 12 |
| CPAP | [#4963](https://github.com/ai4curation/ai-gene-review/pull/4963) | `965cde4fa1039cb92b3fdc59544c84dcea75acf3` | 2026-10-13T15:43:04Z | [f44840baae84](https://github.com/ai4curation/ai-gene-review/commit/f44840baae84c94bf03d35f6363c26f6a5773845) | 23 | 23 |
| CPOX | [#4965](https://github.com/ai4curation/ai-gene-review/pull/4965) | `ad948941fff6f94a4a50c77a5e23b987c5a0046c` | 2026-10-13T16:09:26Z | [df60d6da2141](https://github.com/ai4curation/ai-gene-review/commit/df60d6da21411b5820e99cad678ae4a6c2721ff3) | 16 | 16 |
| CPT1A | [#4968](https://github.com/ai4curation/ai-gene-review/pull/4968) | `c155487423cdd4de0660a760aece8a8ea26ce54e` | 2026-10-13T16:34:02Z | [a9655bc9362c](https://github.com/ai4curation/ai-gene-review/commit/a9655bc9362c58342ad7a7d077637d13d75a3d49) | 29 | 29 |

The complete approved inventories contain 918 path occurrences across these
44 PRs. Each approved path agrees with its actual merged mode, type and blob,
including the confirmed deletion in COXFA4; the 847 parent-relative changes
contain no extra paths. Parent-identical shared paths remain part of the full
inventories but add no integration delta or gene credit. Final approvals and
required checks were verified in the accepted merge evidence for each PR.

COXFA4 is the single catalogue gene HGNC:7687, whose retained ClinGen source
symbol is NDUFA4. PR #4958 removes the obsolete NDUFA4 review path and retains
the COXFA4 review; this is one gene, not two. Its association text is unchanged.

Update 73 appends these 44 genes only. All 72 prior updates, all 235 historical
queue records, all 2,876 catalogue association texts and their order are preserved.
Completed, campaign_audited_merged and the legacy original_merged field are 394;
pending_followups remains zero. Products, follow-up commits and shared sources
do not receive separate credits.

The baseline tracker [PR #4962](https://github.com/ai4curation/ai-gene-review/pull/4962)
merged at 2026-10-13 12:31:49 UTC as
[`fdcbaab48e51`](https://github.com/ai4curation/ai-gene-review/commit/fdcbaab48e51e3ba89d9775685ff5850a3647221),
preserving its approved head `32da3e6e03e8763801f689837ace186af98eba7d`. That tracker merge adds no gene credit.
The old checkpoint sections below retain their original observations and wording,
including statuses that were OPEN or QUEUED when recorded.

[Publication session history](https://github.com/ai4curation/ai-gene-review/blob/main/history/projects/CLINGEN_MENDELIAN/2026-10-13T173920Z-codex-afd312.yaml).

## Completion checkpoint 350 — 2026-10-12 17:16:33 UTC

**350 complete / 2,526 remaining in the frozen 2,876-gene catalog.**
CNKSR2 is the sole addition beyond checkpoint 349 and was absent from all 71
prior completion updates. It was unchecked in that preserved proposal.

| Gene | PR | Approved head | Approval | API merge time UTC | Merge commit |
|---|---|---|---|---|---|
| CNKSR2 | [#4781](https://github.com/ai4curation/ai-gene-review/pull/4781) | `b7e2e9e807fd9e9467a9a2731ab0daff36b568ac` | [Approved](https://github.com/ai4curation/ai-gene-review/pull/4781#pullrequestreview-5486106263) | 2026-10-12T17:16:33Z | `3f28b1714ba53f3d9173ed69992ac335f7e92c4c` |

All 12 complete PR paths have identical approved-head and merge blobs. The JSON
completion entry records their hashes and actual parent-relative path accounting.
The later merge is disjoint from every path in the two preceding collagen PRs
and leaves all six published tracker341 preimages unchanged. This is one primary
gene credit, not another credit for either of its genuine history records.

Update 72 adds CNKSR2 alone. Update 71 preserves the separate COL6A1/COL6A2
proofs; all 70 earlier completion updates, all 235 historical queue objects and
all 2,876 association texts remain exact. Completed, campaign_audited_merged and
legacy original_merged are 350; pending_followups remains zero. Tracker #4806's
merge remains recorded in checkpoint349 and adds no gene completion. Earlier
checkpoint observations remain historical; this is the final frozen cutoff for
this proposal.

[Publication session history](https://github.com/ai4curation/ai-gene-review/blob/main/history/projects/CLINGEN_MENDELIAN/2026-10-12T175402Z-codex-078897.yaml).

## Completion checkpoint 349 — 2026-10-12 16:50:16 UTC

**349 complete / 2,527 remaining in the frozen 2,876-gene catalog.**
COL6A1 and COL6A2 are the only additions beyond frozen checkpoint 347. Both
were unchecked and absent from all 70 prior completion updates.

| Gene | PR | Approved head | Approval | API merge time UTC | Merge commit |
|---|---|---|---|---|---|
| COL6A1 | [#4941](https://github.com/ai4curation/ai-gene-review/pull/4941) | `37f1aa9535e07fb7aface73af24c1ca4e44e0044` | [Approved](https://github.com/ai4curation/ai-gene-review/pull/4941#pullrequestreview-5486015912) | 2026-10-12T16:33:15Z | `c5d3421c60bbf6ed470b5c03263ccf70186bcd49` |
| COL6A2 | [#4942](https://github.com/ai4curation/ai-gene-review/pull/4942) | `0d765fa4a87a383ebaa301c913d6f50b79cd2c88` | [Approved](https://github.com/ai4curation/ai-gene-review/pull/4942#pullrequestreview-5486040814) | 2026-10-12T16:50:16Z | `55a60723b3369503c6b3caaee74208918278cf3d` |

The complete PR inventories contain 26 COL6A1 paths and 24 COL6A2 paths. Every
approved-head blob equals its merge blob and its blob at the frozen main cutoff.
The JSON completion entry records each Git blob, content hash and parent-relative
delta, including shared caches already identical in a parent. These are two
distinct primary genes; their products, follow-ups and history records add no
separate credit. This checkpoint does not reassess their scientific conclusions.

Update 71 adds both genes. All 70 previous updates remain exact, including the
separate staged checkpoints 343–347. All 235 historical queue objects and all
2,876 association texts remain unchanged. Completed, campaign_audited_merged and
legacy original_merged are 349; pending_followups remains zero.

The previously published checkpoint 341 in tracker #4806 merged at
2026-10-12T16:07:55Z as `6091dffa32318a8f33450bb4c75a240fb5aab07c`,
from head `260cf538c0256bcd2d678e45b688d7bffc1cfbfa`. Its six publication
files remain exact at the cutoff. Older checkpoint entries retain their original
observations, including the then-queued tracker state. The tracker merge adds no
gene completion. No separate checkpoint348 proposal was created; the first
collagen merge established348 and the second established349.

[Publication session history](https://github.com/ai4curation/ai-gene-review/blob/main/history/projects/CLINGEN_MENDELIAN/2026-10-12T175402Z-codex-078897.yaml).

## Completion checkpoint 347 — 2026-10-12 14:29:11 UTC

**347 complete / 2,529 remaining in the frozen 2,876-gene catalog.**
COG5 is the sole addition beyond staged checkpoint 346. It was unchecked in
that proposal and absent from all 69 prior completion updates.

| Gene | PR | Approved head | Approval | API merge time UTC | Merge commit |
|---|---|---|---|---|---|
| COG5 | [#4880](https://github.com/ai4curation/ai-gene-review/pull/4880) | `e2a1c0cead5759c0e664a98556e5aa4f840ecc6d` | [Approved](https://github.com/ai4curation/ai-gene-review/pull/4880#pullrequestreview-5484859321) | 2026-10-12T14:29:11Z | `5375ac52c3f4c4ab078b8beeec63b11853088bcb` |

All 14 PR paths have identical approved-head and merge blobs, including the review,
source artifacts and two genuine gene history records. The actual merge delta has
13 paths; PMID_27066481.md was already identical in the parent. The JSON completion
entry retains the exact path/blob/hash evidence. This adds one distinct gene,
not a biological reassessment or separate credits for products or follow-ups.

Update 70 contains COG5 alone. All 69 previous updates remain unchanged, including
update 69 for COG8, update 68 for COG6, update 67 for CNGA3 and update 66 for
CNOT3/CNGB1. All 235 queue objects and 2,876 association texts remain exact; only
COG5's checkbox changes from staged346. Completed, campaign_audited_merged and
legacy original_merged are 347; pending_followups remains zero. Tracker #4806 was
observed queued at 2026-10-12 14:32:13 UTC, at
`260cf538c0256bcd2d678e45b688d7bffc1cfbfa`; this pending proposal makes no
change to that PR. A genuine session history will be created only at publication.

[Publication session history](https://github.com/ai4curation/ai-gene-review/blob/main/history/projects/CLINGEN_MENDELIAN/2026-10-12T175402Z-codex-078897.yaml).

## Completion checkpoint 346 — 2026-10-12 14:02:20 UTC

**346 complete / 2,530 remaining in the frozen 2,876-gene catalog.**
COG8 is the sole addition beyond staged checkpoint 345. It was unchecked in
that proposal and absent from all 68 prior completion updates.

| Gene | PR | Approved head | Approval | API merge time UTC | Merge commit |
|---|---|---|---|---|---|
| COG8 | [#4913](https://github.com/ai4curation/ai-gene-review/pull/4913) | `cc51fff7d8ccfae688b8d14175ed88311a0a4f49` | [Approved](https://github.com/ai4curation/ai-gene-review/pull/4913#pullrequestreview-5484876526) | 2026-10-12T14:02:20Z | `1ec0b0b2fed4675003ae94a7684ac6e20296685b` |

All 15 PR paths have identical approved-head and merge blobs, including the review,
source artifacts and two genuine gene history records. The actual merge delta has
14 paths; PMID_27066481.md was already identical in the parent. The JSON completion
entry retains the exact path/blob/hash evidence. This adds one distinct gene,
not a biological reassessment or separate credits for products or follow-ups.

Update 69 contains COG8 alone. All 68 previous updates remain unchanged, including
update 68 for COG6, update 67 for CNGA3 and update 66 for CNOT3/CNGB1. All 235 queue
objects and 2,876 association texts remain exact; only COG8's checkbox changes from
staged345. Completed, campaign_audited_merged and legacy original_merged are 346;
pending_followups remains zero. Tracker #4806 remains queued at
`260cf538c0256bcd2d678e45b688d7bffc1cfbfa`; this pending proposal makes no
change to that PR. A genuine session history will be created only at publication.

[Publication session history](https://github.com/ai4curation/ai-gene-review/blob/main/history/projects/CLINGEN_MENDELIAN/2026-10-12T175402Z-codex-078897.yaml).

## Completion checkpoint 345 — 2026-10-12 13:43:54 UTC

**345 complete / 2,531 remaining in the frozen 2,876-gene catalog.**
COG6 is the sole addition beyond staged checkpoint 344. It was unchecked in
that proposal and absent from all 67 prior completion updates.

| Gene | PR | Approved head | Approval | API merge time UTC | Merge commit |
|---|---|---|---|---|---|
| COG6 | [#4902](https://github.com/ai4curation/ai-gene-review/pull/4902) | `8ca06f0e055f23daf52cb9324afb049301091496` | [Approved](https://github.com/ai4curation/ai-gene-review/pull/4902#pullrequestreview-5484896251) | 2026-10-12T13:43:54Z | `91cea6ec7a9a2f8a77e79ed8636148c65a9ebcf3` |

All 16 PR paths have identical approved-head and merge blobs, including the review,
source artifacts and two genuine gene history records. The JSON completion entry
retains exact path/blob/hash evidence. This adds one distinct gene completion,
not a biological reassessment or separate credits for products or follow-ups.

Update 68 contains COG6 alone. All 67 previous updates remain unchanged, including
update 67 for CNGA3 and update 66 for CNOT3/CNGB1. All 235 queue objects and 2,876
association texts remain exact; only COG6's checkbox changes from staged344.
Completed, campaign_audited_merged and legacy original_merged are 345;
pending_followups remains zero. Tracker #4806 remains queued at
`260cf538c0256bcd2d678e45b688d7bffc1cfbfa`; this pending proposal makes no
change to that PR. A genuine session history will be created only at publication.

[Publication session history](https://github.com/ai4curation/ai-gene-review/blob/main/history/projects/CLINGEN_MENDELIAN/2026-10-12T175402Z-codex-078897.yaml).

## Completion checkpoint 344 — 2026-10-12 13:25:41 UTC

**344 complete / 2,532 remaining in the frozen 2,876-gene catalog.**
CNGA3 is the sole addition beyond staged checkpoint 343. It was unchecked in
that proposal and absent from all 66 prior completion updates.

| Gene | PR | Approved head | Approval | API merge time UTC | Merge commit |
|---|---|---|---|---|---|
| CNGA3 | [#4750](https://github.com/ai4curation/ai-gene-review/pull/4750) | `d003c2986007378390e4dcd50d9f57df773d4056` | [Approved](https://github.com/ai4curation/ai-gene-review/pull/4750#pullrequestreview-5484823656) | 2026-10-12T13:25:41Z | `b55d5643c7ba3064cf073f9d7452dadcd6b1ebed` |

All 26 PR paths have identical approved-head and merge blobs, including the review,
source artifacts and three genuine gene history records. The JSON completion entry
retains their exact path/blob/hash evidence. This adds one distinct gene completion,
not a new biological assessment or credit for each product, follow-up or history.

Update 67 appends CNGA3 while preserving update 66 for CNOT3/CNGB1 verbatim as a
parsed object, all earlier updates, all 235 queue objects and all 2,876 association
texts. Only the CNGA3 checkbox changes relative to the staged343 proposal.
Completed, campaign_audited_merged and legacy original_merged are 344;
pending_followups remains zero. The approved tracker PR #4806 remains queued at
`260cf538c0256bcd2d678e45b688d7bffc1cfbfa`; this is a pending proposal and does
not alter that PR. A genuine session history will be created only at publication.

[Publication session history](https://github.com/ai4curation/ai-gene-review/blob/main/history/projects/CLINGEN_MENDELIAN/2026-10-12T175402Z-codex-078897.yaml).

## Completion checkpoint 343 — 2026-10-12 01:01:00 UTC

**343 complete / 2,533 remaining in the frozen 2,876-gene catalog.**
CNOT3 and CNGB1 are the only new completions beyond checkpoint 341. Both were
unchecked in tracker revision `260cf538c0256bcd2d678e45b688d7bffc1cfbfa` and absent from its completion additions.

| Gene | PR | Approved head | Approval | API merge time UTC | Merge commit |
|---|---|---|---|---|---|
| CNOT3 | [#4826](https://github.com/ai4curation/ai-gene-review/pull/4826) | `69afb67456dff36741d9a7726fae178bad481908` | [Approved](https://github.com/ai4curation/ai-gene-review/pull/4826#pullrequestreview-5484342518) | 2026-10-12T00:28:15Z | `5d0b91e92a2fb621ceda58b58961b06f8dfdc888` |
| CNGB1 | [#4772](https://github.com/ai4curation/ai-gene-review/pull/4772) | `2e5deeaf8b0738188afee353988fa40e864ad03f` | [Approved](https://github.com/ai4curation/ai-gene-review/pull/4772#pullrequestreview-5484488856) | 2026-10-12T01:01:00Z | `d9f82bb33f6e1ee2b9a65520a05263f30d6ddc13` |

The accepted merge qualifications compare all 24 CNOT3 PR paths and all 29 CNGB1
PR paths with the approved revisions. Sixteen and 27 paths, respectively, were
new integration changes; eight and two shared paths were already identical in
the merge parent. All 31 CNOT3 and 26 CNGB1 cached/local references were checked.
The JSON completion entry retains exact paths, blob identities, hashes, approvals
and successful check receipts. This tracker amendment adds no biological claims.

Exactly two catalog checkboxes change. All 2,876 association texts, frontmatter,
235 queue objects, 65 prior completion entries and previous progress text remain
unchanged. Update 66 is appended to identical JSON mirrors. Completed,
campaign_audited_merged and legacy original_merged are 343; pending_followups is
zero. Existing counter definitions and earlier checkpoint scope remain in force.

[Publication session history](https://github.com/ai4curation/ai-gene-review/blob/main/history/projects/CLINGEN_MENDELIAN/2026-10-12T175402Z-codex-078897.yaml).

## Completion checkpoint 341 — 2026-10-11 23:54:55 UTC

**341 complete / 2,535 remaining in the frozen 2,876-gene catalog.**
CNOT1 is the sole new completion. It was unchecked at the actual pending tracker
revision `7d5112b980bd82bf7af5eb2e4d99685780df40f0` and absent from its 64 completion additions.

| Gene | PR | Approved head | Approval | API merge time UTC | Merge commit |
|---|---|---|---|---|---|
| CNOT1 | [#4820](https://github.com/ai4curation/ai-gene-review/pull/4820) | `3c61cc26ebcf933ee1318ecab60303ed71b426d6` | [Approved](https://github.com/ai4curation/ai-gene-review/pull/4820#pullrequestreview-5484483416) | 2026-10-11T23:54:55Z | `9ce0404b697131c6465edbea9af026a5a4a00cf5` |

Approval was submitted at **2026-10-11T18:48:45Z** on the final head.
The exact-head approval resolves the earlier blocking review. Remaining suggestions
were explicitly non-blocking. The required test and reviewer workflow both succeeded before merge:

- [Build and test / test (3.12)](https://github.com/ai4curation/ai-gene-review/actions/runs/38140009323/job/114471751002) completed at **2026-10-11T18:01:29Z**.
- [Claude Code Review / claude-review](https://github.com/ai4curation/ai-gene-review/actions/runs/38140009321/job/114471751318) completed at **2026-10-11T18:49:01Z**.

Merge queue integration completed at the API time above. The 27 changed PR paths,
complete six-file gene directory, and all 35 cache/local reference objects (32 PMID
caches, two Reactome entries and the cited source-evidence file) are identical at
the approved head and actual merge. All 27 PR paths are also actual integration changes; none was omitted as already present. Captured main equals that merge. The JSON
completion entry records paths, Git blob IDs and SHA-256 hashes; no scientific
claims or new primary-source readings are added by this tracker update.

Exactly one catalog checkbox changes. All 2,876 association texts, frontmatter,
235 queue objects, 64 earlier completion entries, prior progress text and existing
history records are preserved. Update 65 is appended to identical JSON mirrors.
The counts `completed`, `campaign_audited_merged` and legacy `original_merged` are
341; `pending_followups` remains zero. Neither pending reviews nor tracker commits
add completions. Existing checkpoint scope and counter definitions remain in force.

[Checkpoint 341 session history](https://github.com/ai4curation/ai-gene-review/blob/main/history/projects/CLINGEN_MENDELIAN/2026-10-12T001215Z-codex-3576e4.yaml).

## Completion checkpoint 340 — 2026-10-11 23:13:41 UTC

**340 complete / 2,536 remaining in the frozen 2,876-gene catalog.**
CNGB3 is the sole new completion. It was unchecked at the actual pending tracker
revision `8e0400093727037c8250f2b7ec1c4536ab8ea74b` and absent from its 63 completion additions.

| Gene | PR | Approved head | Approval | API merge time UTC | Merge commit |
|---|---|---|---|---|---|
| CNGB3 | [#4768](https://github.com/ai4curation/ai-gene-review/pull/4768) | `a040afa672fab99d939b91d24bba1108754fcfb0` | [Approved](https://github.com/ai4curation/ai-gene-review/pull/4768#pullrequestreview-5484422996) | 2026-10-11T23:13:41Z | `f6bb52a1888bb449150cfee7bae168e1e6578570` |

Approval was submitted at **2026-10-11T18:29:02Z** on the final head.
The exact-head approval resolves the earlier blocking review. Remaining suggestions
were explicitly non-blocking. The required test and reviewer workflow both succeeded before merge:

- [Build and test / test (3.12)](https://github.com/ai4curation/ai-gene-review/actions/runs/38144133686/job/114483834957) completed at **2026-10-11T17:59:48Z**.
- [Claude Code Review / claude-review](https://github.com/ai4curation/ai-gene-review/actions/runs/38144133640/job/114483834942) completed at **2026-10-11T18:29:19Z**.

Merge queue integration completed at the API time above. The 18 changed PR paths,
complete six-file gene directory, and 10 referenced PMID caches are identical at
the approved head and actual merge. All 18 PR paths are also actual integration changes; none was omitted as already present. Captured main equals that merge. The JSON
completion entry records paths, Git blob IDs and SHA-256 hashes; no scientific
claims or new primary-source readings are added by this tracker update.

Exactly one catalog checkbox changes. All 2,876 association texts, frontmatter,
235 queue objects, 63 earlier completion entries, prior progress text and existing
history records are preserved. Update 64 is appended to identical JSON mirrors.
The counts `completed`, `campaign_audited_merged` and legacy `original_merged` are
340; `pending_followups` remains zero. Neither pending reviews nor tracker commits
add completions. Existing checkpoint scope and counter definitions remain in force.

[Checkpoint 340 session history](https://github.com/ai4curation/ai-gene-review/blob/main/history/projects/CLINGEN_MENDELIAN/2026-10-11T233509Z-codex-49c813.yaml).

## Completion checkpoint 339 — 2026-10-11 12:44:47 UTC

**339 complete / 2,537 remaining in the frozen 2,876-gene catalog.**
CNTN2 is the sole new completion. It was unchecked at the actual pending tracker
revision `14a07a782e17fdd094b283f76c0f2824c9c73487` and absent from its 62 completion additions.

| Gene | PR | Approved head | Approval | API merge time UTC | Merge commit |
|---|---|---|---|---|---|
| CNTN2 | [#4830](https://github.com/ai4curation/ai-gene-review/pull/4830) | `d6e14551e979eb3200bc214dcc629d6c617e666c` | [Approved](https://github.com/ai4curation/ai-gene-review/pull/4830#pullrequestreview-5483274032) | 2026-10-11T12:44:47Z | `eeccfc52335ab3ea5e4f16f9c30daa4eb308405b` |

Approval was submitted at **2026-10-11T12:21:03Z** on the final head.
ROOT read the complete approval and detailed review; remaining suggestions were
optional. The required test and reviewer workflow both succeeded before merge:

- [Build and test / test (3.12)](https://github.com/ai4curation/ai-gene-review/actions/runs/38123329179/job/114422399510) completed at **2026-10-11T12:32:08Z**.
- [Claude Code Review / claude-review](https://github.com/ai4curation/ai-gene-review/actions/runs/38123329147/job/114422399625) completed at **2026-10-11T12:21:21Z**.

Squash merge completed at the API time above. The 26 changed PR paths,
complete six-file gene directory, and 20 referenced PMID caches are identical at
the approved head and actual merge. All 26 PR paths are also actual squash changes; none was omitted as already present. Captured main equals that merge. The JSON
completion entry records paths, Git blob IDs and SHA-256 hashes; no scientific
claims or new primary-source readings are added by this tracker update.

Exactly one catalog checkbox changes. All 2,876 association texts, frontmatter,
235 queue objects, 62 earlier completion entries, prior progress text and existing
history records are preserved. Update 63 is appended to identical JSON mirrors.
The counts `completed`, `campaign_audited_merged` and legacy `original_merged` are
339; `pending_followups` remains zero. Neither pending reviews nor tracker commits
add completions. Existing checkpoint scope and counter definitions remain in force.

[Checkpoint 339 session history](https://github.com/ai4curation/ai-gene-review/blob/main/history/projects/CLINGEN_MENDELIAN/2026-10-11T125009Z-codex-dc5831.yaml).

## Completion checkpoint 338 — 2026-10-11 11:03:24 UTC

**338 complete / 2,538 remaining in the frozen 2,876-gene catalog.**
CLN5 is the sole new completion. It was unchecked at the actual pending tracker
revision `b268c1432f697b432dc39b6da1b5b985fc0895e2` and absent from its 61 completion additions.

| Gene | PR | Approved head | Approval | API merge time UTC | Merge commit |
|---|---|---|---|---|---|
| CLN5 | [#4710](https://github.com/ai4curation/ai-gene-review/pull/4710) | `c3358f58561a2067a67f4f62a644f1700a4c0cf8` | [Approved](https://github.com/ai4curation/ai-gene-review/pull/4710#pullrequestreview-5483013319) | 2026-10-11T11:03:24Z | `b7934f19c0fc20c5f57601b41a87fc02850082d6` |

Approval was submitted at **2026-10-11T10:50:13Z** on the final head.
ROOT read the complete approval and detailed review; remaining suggestions were
optional. The required test and reviewer workflow both succeeded before merge:

- [Build and test / test (3.12)](https://github.com/ai4curation/ai-gene-review/actions/runs/38120588158/job/114414311733) completed at **2026-10-11T11:03:18Z**.
- [Claude Code Review / claude-review](https://github.com/ai4curation/ai-gene-review/actions/runs/38120588098/job/114414311908) completed at **2026-10-11T10:50:31Z**.

Squash merge completed at the API time above. The 26 changed PR paths,
complete six-file gene directory, and 25 referenced PMID caches are identical at
the approved head and actual merge. All 26 PR paths are also actual squash changes; none was omitted as already present. Captured main equals that merge. The JSON
completion entry records paths, Git blob IDs and SHA-256 hashes; no scientific
claims or new primary-source readings are added by this tracker update.

Exactly one catalog checkbox changes. All 2,876 association texts, frontmatter,
235 queue objects, 61 earlier completion entries, prior progress text and existing
history records are preserved. Update 62 is appended to identical JSON mirrors.
The counts `completed`, `campaign_audited_merged` and legacy `original_merged` are
338; `pending_followups` remains zero. Neither pending reviews nor tracker commits
add completions. Existing checkpoint scope and counter definitions remain in force.

[Checkpoint 338 session history](https://github.com/ai4curation/ai-gene-review/blob/main/history/projects/CLINGEN_MENDELIAN/2026-10-11T111210Z-codex-c209d2.yaml).

## Completion checkpoint 337 — 2026-10-11 10:33:02 UTC

**337 complete / 2,539 remaining in the frozen 2,876-gene catalog.**
CLCN5 is the sole new completion. It was unchecked at the actual pending tracker
revision `0314bf1973a88ddab8c71030db41203b30205dc1` and absent from its 60 completion additions.

| Gene | PR | Approved head | Approval | API merge time UTC | Merge commit |
|---|---|---|---|---|---|
| CLCN5 | [#4686](https://github.com/ai4curation/ai-gene-review/pull/4686) | `b44200220f3dd257ea0980f29d22ddcf077f110e` | [Approved](https://github.com/ai4curation/ai-gene-review/pull/4686#pullrequestreview-5482880006) | 2026-10-11T10:33:02Z | `d0f37ace6af1e18e19b58afbda935e2f753110a5` |

Approval was submitted at **2026-10-11T10:09:54Z** on the final head.
ROOT read the complete approval and detailed review; remaining suggestions were
optional. The required test and reviewer workflow both succeeded before merge:

- [Build and test / test (3.12)](https://github.com/ai4curation/ai-gene-review/actions/runs/38118877254/job/114409299276) completed at **2026-10-11T10:29:46Z**.
- [Claude Code Review / claude-review](https://github.com/ai4curation/ai-gene-review/actions/runs/38118877260/job/114409299468) completed at **2026-10-11T10:10:12Z**.

Squash merge completed at the API time above. The 18 changed PR paths,
complete six-file gene directory, and 11 referenced PMID caches are identical at
the approved head and actual merge. The squash changes 13 paths; five shared
files were already identical in its parent and are preserved. Captured main equals that merge. The JSON
completion entry records paths, Git blob IDs and SHA-256 hashes; no scientific
claims or new primary-source readings are added by this tracker update.

Exactly one catalog checkbox changes. All 2,876 association texts, frontmatter,
235 queue objects, 60 earlier completion entries, prior progress text and existing
history records are preserved. Update 61 is appended to identical JSON mirrors.
The counts `completed`, `campaign_audited_merged` and legacy `original_merged` are
337; `pending_followups` remains zero. Neither pending reviews nor tracker commits
add completions. Existing checkpoint scope and counter definitions remain in force.

[Checkpoint 337 session history](https://github.com/ai4curation/ai-gene-review/blob/main/history/projects/CLINGEN_MENDELIAN/2026-10-11T103826Z-codex-9b0957.yaml).

## Completion checkpoint 336 — 2026-10-11 10:15:33 UTC

**336 complete / 2,540 remaining in the frozen 2,876-gene catalog.**
CLCN4 is the sole new completion. It was unchecked at the actual pending tracker
revision `4ad06a72170d5ce10eaff72e510491243a21973b` and absent from its 59 completion additions.

| Gene | PR | Approved head | Approval | API merge time UTC | Merge commit |
|---|---|---|---|---|---|
| CLCN4 | [#4681](https://github.com/ai4curation/ai-gene-review/pull/4681) | `156891895a65241cb02212ab69125151a4b792b3` | [Approved](https://github.com/ai4curation/ai-gene-review/pull/4681#pullrequestreview-5482841340) | 2026-10-11T10:15:33Z | `38b117f6c544544dd9034bb1fd9ed12f25a08e21` |

Approval was submitted at **2026-10-11T09:59:49Z** on the final head.
ROOT read the complete approval and detailed review; remaining suggestions were
optional. The required test and reviewer workflow both succeeded before merge:

- [Build and test / test (3.12)](https://github.com/ai4curation/ai-gene-review/actions/runs/38118515575/job/114408226675) completed at **2026-10-11T10:15:06Z**.
- [Claude Code Review / claude-review](https://github.com/ai4curation/ai-gene-review/actions/runs/38118515578/job/114408226723) completed at **2026-10-11T10:00:31Z**.

Automatic squash merge completed at the API time above. The 22 changed PR paths,
complete six-file gene directory, and 13 referenced PMID caches are identical at
the approved head and actual merge. Captured main equals that merge. The JSON
completion entry records paths, Git blob IDs and SHA-256 hashes; no scientific
claims or new primary-source readings are added by this tracker update.

Exactly one catalog checkbox changes. All 2,876 association texts, frontmatter,
235 queue objects, 59 earlier completion entries, prior progress text and existing
history records are preserved. Update 60 is appended to identical JSON mirrors.
The counts `completed`, `campaign_audited_merged` and legacy `original_merged` are
336; `pending_followups` remains zero. Neither pending reviews nor tracker commits
add completions. Existing checkpoint scope and counter definitions remain in force.

[Checkpoint 336 session history](https://github.com/ai4curation/ai-gene-review/blob/main/history/projects/CLINGEN_MENDELIAN/2026-10-11T102604Z-codex-e4d494.yaml).

## Completion checkpoint 335 — 2026-10-11 08:23:41 UTC

**335 complete / 2,541 remaining in the frozen 2,876-gene catalog.**
CLDN16 is the sole new qualifying completion. It was unchecked in the actual
pending tracker334 proposal and absent from all 58 prior completion additions.
The two rounds of its gene review count as one audit, with no additional count
for products or justified UNDECIDED decisions.

| Gene | PR | Approved head | Approval | API merge time UTC | Merge commit |
|---|---|---|---|---|---|
| CLDN16 | [#4700](https://github.com/ai4curation/ai-gene-review/pull/4700) | `0005e0722bc3720721c81c3fb4384afc655ddc65` | [Approved](https://github.com/ai4curation/ai-gene-review/pull/4700#pullrequestreview-5482461058) | 2026-10-11T08:23:41Z | `72f77443344b3bdd8f49d54f237b85b4d70fa0a3` |

The exact-head approval was submitted at **2026-10-11T08:01:10Z**.
The reviewer explicitly resolved both mandatory issues and approved the final
source-scoped magnesium and partner-dependent adhesion decisions. Suggestions
about a new term, boolean wording and optional core cargo specificity are nonblocking.
The approval noted that tests were still running; the final gate independently
verified both required checks succeeded before the merge:

- [Build and test / test (3.12)](https://github.com/ai4curation/ai-gene-review/actions/runs/38112098235/job/114389598527) succeeded at **2026-10-11T08:14:46Z**.
- [Claude Code Review / claude-review](https://github.com/ai4curation/ai-gene-review/actions/runs/38112098322/job/114389599097) succeeded at **2026-10-11T08:02:06Z**.

The complete final review, detailed comment and empty review-thread set were
read. No actionable objection remains. ROOT's actual merge and publisher-state
receipts are reused without another merge or workflow retry. This checkpoint
makes no new scientific claim or primary-source reading claim.

### Exact content and source proof

All **19 changed PR paths** have identical approved-head, merge and captured-current-main
blobs, including both gene histories and all added publication caches. The complete
six-file CLDN16 directory is also identical at those three commits. All **11 referenced
PMID cache pairs** match; the unchanged source annotations and ancillary reference
identities remain those of the approved gene review. Exact paths, Git object IDs,
SHA-256 hashes and sizes are recorded in queue update **59**.

The gene cutoff is `72f77443344b3bdd8f49d54f237b85b4d70fa0a3`, API merged at **2026-10-11T08:23:41Z**.
Its Git commit time is recorded separately as **2026-10-11T09:23:40+01:00**.
The later applicability snapshot `f057b5f28fd4eff091a80d1e1bb7a72c1b1136d3` adds no completion.

### Pending tracker baseline and preservation

The baseline is the actual open [tracker334 #4806](https://github.com/ai4curation/ai-gene-review/pull/4806)
head `68ca45f3b459de78ed4c7ef4326a21993f160030`. Its queue is byte-identical to the already verified tracker334 proposal;
the prior 334-gene evidence is reused, not reconstructed from a stale main-branch
page and not recounted. The baseline tracker is **pending**, not described as merged.
The coordinator will amend that PR only after reviewing this isolated delta.

Exactly one checkbox changes. All 2,876 association texts, frontmatter, **235 queue
objects**, **58 prior completion updates**, unrelated queue metadata and the complete
prior progress text remain exact. Update **59** is appended and the two JSON mirrors
are identical. The nine existing parent-page session links and all **152 project
history records** present at the baseline are preserved. ROOT alone creates and
validates the new session record; this proposal does not rewrite any history.

Counts are **335** for `completed`, `campaign_audited_merged` and legacy
`original_merged`, **0** for `pending_followups`, and **2,541** remaining.
No other open or newly merged gene is counted by this frozen amendment. In particular,
CLPP and FH remain unchecked under the preserved checkpoint334 scope.

Ordinary frontmatter tests and both project renders compare the baseline and
proposal using the same authenticated current-main renderer and complete gene-review
context. Missing-review availability warnings must remain identical; availability
alone is never completion. Final check counts are recorded in the proposal handoff.

[Checkpoint 335 session history](https://github.com/ai4curation/ai-gene-review/blob/main/history/projects/CLINGEN_MENDELIAN/2026-10-11T085605Z-codex-f501c7.yaml).

## Completion checkpoint 334 — 2026-10-11 06:08:52 UTC

**334 complete / 2,542 remaining in the frozen 2,876-gene catalog.**
CHEK2, CHAMP1, CHN1, CIITA, CIB2, CHD3, CHD4, CHRNA1, CHRNA4, CISD2 and CLDN14
are eleven distinct completions beyond checkpoint 323. Every gene was unchecked
in that actual merged tracker and absent from its prior completion additions.
Each counts once after its first qualifying substantive audit; products, repeated
follow-ups, DRAFT status and justified uncertainty add no extra counts or holds.

| Gene | PR | Approved head | Approval | API merge time UTC | Merge commit |
|---|---|---|---|---|---|
| CHEK2 | [#4599](https://github.com/ai4curation/ai-gene-review/pull/4599) | `30679cb6be4eadff942500ba2ca7b3f403faeef4` | [Approved](https://github.com/ai4curation/ai-gene-review/pull/4599#pullrequestreview-5481160015) | 2026-10-10T23:45:01Z | `d6a01fd305ee7d7fdc6fbc2d1c7a72eff02c8835` |
| CHAMP1 | [#4569](https://github.com/ai4curation/ai-gene-review/pull/4569) | `8260449b4cc8fa36662f9962d9ab0db92da6a472` | [Approved](https://github.com/ai4curation/ai-gene-review/pull/4569#pullrequestreview-5481260002) | 2026-10-11T00:13:02Z | `3b771a1473998724cead92201d9c97c2ba2c27f1` |
| CHN1 | [#4607](https://github.com/ai4curation/ai-gene-review/pull/4607) | `3c4842dbfea343d3906067e8134796d9ee7ad8ec` | [Approved](https://github.com/ai4curation/ai-gene-review/pull/4607#pullrequestreview-5481272084) | 2026-10-11T00:14:03Z | `405c9880e95895ba19e80e4c7cdff193ef2c81b6` |
| CIITA | [#4670](https://github.com/ai4curation/ai-gene-review/pull/4670) | `4b7eb79c5400331d0d7da27e0f7bff885adf24df` | [Approved](https://github.com/ai4curation/ai-gene-review/pull/4670#pullrequestreview-5481386409) | 2026-10-11T01:08:53Z | `a783a11b511f3591d5e8c65643f0cce5a5ac2ade` |
| CIB2 | [#4657](https://github.com/ai4curation/ai-gene-review/pull/4657) | `c4454c5300ad3ede6d5840b7a4b6abd010df88e2` | [Approved](https://github.com/ai4curation/ai-gene-review/pull/4657#pullrequestreview-5481431163) | 2026-10-11T01:30:43Z | `272b1676c210ef2b0124d4c443679cad40886796` |
| CHD3 | [#4587](https://github.com/ai4curation/ai-gene-review/pull/4587) | `54454f7071c2a8d594df30a2e4252eab72f31167` | [Approved](https://github.com/ai4curation/ai-gene-review/pull/4587#pullrequestreview-5481653963) | 2026-10-11T03:14:30Z | `f8337fea41c734214bea2c20b927d275a14bddc5` |
| CHD4 | [#4589](https://github.com/ai4curation/ai-gene-review/pull/4589) | `f72a9310a39ddf15b465e423aacbb52ef6818146` | [Approved](https://github.com/ai4curation/ai-gene-review/pull/4589#pullrequestreview-5481741065) | 2026-10-11T03:52:34Z | `5907529e17896a411a4a3189ba1258e6f86df88c` |
| CHRNA1 | [#4611](https://github.com/ai4curation/ai-gene-review/pull/4611) | `46fb369be19bd1c2143fe00f4d2a02116ba08533` | [Approved](https://github.com/ai4curation/ai-gene-review/pull/4611#pullrequestreview-5481839369) | 2026-10-11T04:30:24Z | `74044c73dede57c71d69c52af72cb0e0fa7a538e` |
| CHRNA4 | [#4630](https://github.com/ai4curation/ai-gene-review/pull/4630) | `773f99e05d03a6564bc922767d31b0097535c89d` | [Approved](https://github.com/ai4curation/ai-gene-review/pull/4630#pullrequestreview-5481869914) | 2026-10-11T04:37:31Z | `e597d4b125bc07507d5d636e76e2c631a062e89f` |
| CISD2 | [#4673](https://github.com/ai4curation/ai-gene-review/pull/4673) | `8616575159a579b480a8cda060988c88fbd6a04d` | [Approved](https://github.com/ai4curation/ai-gene-review/pull/4673#pullrequestreview-5481992499) | 2026-10-11T05:36:17Z | `6d2064d1ce862a8e2c601657c52eb2ba17369257` |
| CLDN14 | [#4693](https://github.com/ai4curation/ai-gene-review/pull/4693) | `1b0fe59a6da31228619e53fc2a7eecc3a4862260` | [Approved](https://github.com/ai4curation/ai-gene-review/pull/4693#pullrequestreview-5482113015) | 2026-10-11T06:08:52Z | `0a6db3106b108a9001acebd41df887c750b41faf` |

- **CHEK2**: approved 2026-10-10T23:18:12Z; [test (3.12)](https://github.com/ai4curation/ai-gene-review/actions/runs/38087268856/job/114316269968) succeeded 2026-10-10T23:42:38Z; [claude-review](https://github.com/ai4curation/ai-gene-review/actions/runs/38087268846/job/114316270078) succeeded 2026-10-10T23:18:33Z.
- **CHAMP1**: approved 2026-10-11T00:01:33Z; [test (3.12)](https://github.com/ai4curation/ai-gene-review/actions/runs/38072748452/job/114273376152) succeeded 2026-10-10T19:11:31Z; [claude-review](https://github.com/ai4curation/ai-gene-review/actions/runs/38072748466/job/114318899352) succeeded 2026-10-11T00:01:48Z.
- **CHN1**: approved 2026-10-11T00:05:50Z; [test (3.12)](https://github.com/ai4curation/ai-gene-review/actions/runs/38070425702/job/114266520240) succeeded 2026-10-10T18:04:30Z; [claude-review](https://github.com/ai4curation/ai-gene-review/actions/runs/38070425705/job/114318949925) succeeded 2026-10-11T00:06:27Z.
- **CIITA**: approved 2026-10-11T00:50:07Z; [test (3.12)](https://github.com/ai4curation/ai-gene-review/actions/runs/38090575689/job/114325990040) succeeded 2026-10-11T01:04:12Z; [claude-review](https://github.com/ai4curation/ai-gene-review/actions/runs/38090575669/job/114325990208) succeeded 2026-10-11T00:51:07Z.
- **CIB2**: approved 2026-10-11T01:07:00Z; [test (3.12)](https://github.com/ai4curation/ai-gene-review/actions/runs/38091999838/job/114330151582) succeeded 2026-10-11T01:25:26Z; [claude-review](https://github.com/ai4curation/ai-gene-review/actions/runs/38091999882/job/114330152175) succeeded 2026-10-11T01:07:49Z.
- **CHD3**: approved 2026-10-11T02:49:17Z; [test (3.12)](https://github.com/ai4curation/ai-gene-review/actions/runs/38099151604/job/114351266815) succeeded 2026-10-11T03:07:54Z; [claude-review](https://github.com/ai4curation/ai-gene-review/actions/runs/38099151592/job/114351266975) succeeded 2026-10-11T02:49:53Z.
- **CHD4**: approved 2026-10-11T03:31:54Z; [test (3.12)](https://github.com/ai4curation/ai-gene-review/actions/runs/38100140250/job/114354201083) succeeded 2026-10-11T03:48:15Z; [claude-review](https://github.com/ai4curation/ai-gene-review/actions/runs/38100140261/job/114354201075) succeeded 2026-10-11T03:32:37Z.
- **CHRNA1**: approved 2026-10-11T04:09:20Z; [test (3.12)](https://github.com/ai4curation/ai-gene-review/actions/runs/38101023808/job/114356802452) succeeded 2026-10-11T04:19:36Z; [claude-review](https://github.com/ai4curation/ai-gene-review/actions/runs/38101023807/job/114356803013) succeeded 2026-10-11T04:09:34Z.
- **CHRNA4**: approved 2026-10-11T04:19:03Z; [test (3.12)](https://github.com/ai4curation/ai-gene-review/actions/runs/38101155830/job/114357185027) succeeded 2026-10-11T04:30:09Z; [claude-review](https://github.com/ai4curation/ai-gene-review/actions/runs/38101155823/job/114357185385) succeeded 2026-10-11T04:20:03Z.
- **CISD2**: approved 2026-10-11T05:12:06Z; [test (3.12)](https://github.com/ai4curation/ai-gene-review/actions/runs/38102525950/job/114361236268) succeeded 2026-10-11T05:31:25Z; [claude-review](https://github.com/ai4curation/ai-gene-review/actions/runs/38102525912/job/114361236496) succeeded 2026-10-11T05:12:44Z.
- **CLDN14**: approved 2026-10-11T06:02:31Z; [test (3.12)](https://github.com/ai4curation/ai-gene-review/actions/runs/38096799014/job/114344250702) succeeded 2026-10-11T02:21:38Z; [claude-review](https://github.com/ai4curation/ai-gene-review/actions/runs/38096799030/job/114369742198) succeeded 2026-10-11T06:03:10Z.

All eleven approvals are attached to the stated heads, and both required checks
completed successfully before the corresponding merges. Final feedback remains
identical to the prior merge captures, with no unresolved review threads. Prior
completion-verification packets are reused at their stated scope; their eight
mutation-free verifiers pass again. CISD2 and CLDN14 have separate actual-merge
receipts and reviewed-file proofs. Remaining reviewer suggestions are nonblocking;
this tracker does not reopen their gene reviews or claim new primary-source reads.

### Actual content and source checks

| Gene | Changed PR paths | Complete gene-directory files | Referenced cached-source pairs | Gene-tree OID at head, merge and cutoff |
|---|---:|---:|---:|---|
| CHEK2 | 20 | 6 | 56 | `d785335b2538644c97dc640e7b95009f97844f6b` |
| CHAMP1 | 13 | 8 | 14 | `a283916c79c7cf5770f725290656311424afce56` |
| CHN1 | 18 | 6 | 16 | `0b7bc02c021a8c029965176bdd104d971ba409ff` |
| CIITA | 24 | 6 | 20 | `b06a24540a9d6db2ad82717ae5b4464efee62601` |
| CIB2 | 19 | 6 | 16 | `77a02aa95c4140225ca90f4ecf9c974e67bb702d` |
| CHD3 | 35 | 6 | 47 | `a017b166fbe5fdec9f7a617dcfc280ea5caa76ed` |
| CHD4 | 40 | 6 | 61 | `5115269721dffdc4ba099e0e52ed2c845b58041c` |
| CHRNA1 | 36 | 6 | 16 | `28f1f6628ec5eb301ae7fc1f6adb86c8afeae190` |
| CHRNA4 | 35 | 6 | 29 | `900c8dccabc8a3b9381ba2d33d6687562a67b6c3` |
| CISD2 | 17 | 6 | 13 | `75250ac0a6e9bd038642ba802940797fbdc2bbbc` |
| CLDN14 | 14 | 6 | 13 | `d810954830891988f3c5e8b48907657e82748722` |

All **271 changed PR paths** match approved-head and merged
blobs. All **68 complete gene-directory files** match at
approved head, individual merge, counted cutoff and authenticated source. The
**301 referenced cached-source pairs** are also exact
between each head, merge and current source; repeated publications across genes
are counted as pairs, not distinct files. Complete directory checks include
unchanged machine/provider inputs. Exact paths, byte counts, Git blob IDs and
SHA-256 hashes are recorded in queue update **58**. There are no shared-path
exceptions in this eleven-gene batch; checkpoint 323's external CRLS1 exceptions
remain preserved in its historical record.

### Baseline, cutoff and unchanged records

The baseline is the actually merged [tracker323 #4688](https://github.com/ai4curation/ai-gene-review/pull/4688),
approved head `0558665cb9098522d9581177d3bbc4656b3438ee`, merge `4e9ce09b86d9efc203871f8f7839b2645a7e3466`,
API merge time **2026-10-11T06:07:21Z**. Its seven changed files match
approved and merged content. This tracker merge is provenance, not a twelfth gene.
The gene cutoff and authenticated source are [CLDN14 merge 0a6db3106b10](https://github.com/ai4curation/ai-gene-review/commit/0a6db3106b108a9001acebd41df887c750b41faf),
API merge time **2026-10-11T06:08:52Z**. Later application bases and open PRs are not counted.
API merge times and Git commit times are recorded separately.

The catalog keeps all 2,876 association texts and frontmatter. Exactly eleven
checkboxes change. All **235 queue objects**, all **57 prior completion updates**,
all unrelated queue metadata and the complete prior progress text remain exact;
update **58** is appended and both JSON mirrors are identical. All **151 existing
project histories** and all eight existing parent-page history links are protected.
ROOT will append a new genuine history record at publication.

Checkpoint 323's phrase **“prior 322-member verified set”** means its published
315-member baseline plus the seven genes counted before CRLS1: CHD7, CHRNB1,
CHST6, CHSY1, CHRNG, CHST14 and CHRNB2. CRLS1 then made 323. CLPP and FH were in
neither group. This explicit derivation addresses review #4688's editorial
suggestion without rewriting the old checkpoint or append-only history. The
optional relocation of parent-page history links is deferred so existing links
remain intact.

CLPP and FH remain unchecked here. Their earlier external reviews were excluded
for evidence-specific campaign-policy follow-up; neither is among these eleven
qualifying merges. An unmerged corrective review cannot supply a completion.
This exclusion does not reverse a counted gene or change the preserved legacy
`pending_followups` counter. Counters are **334** for `completed`,
`campaign_audited_merged` and legacy `original_merged`, **0** for
`pending_followups`, and **2,542** remaining.

### Validation and availability context

The ordinary frontmatter checks and both project renders use exact files from
the authenticated source. Parent availability warnings are **1,837**,
identical for the fresh baseline and proposal; progress has zero. Compared with
checkpoint 323's preview (**1,848**), eleven availability warnings
resolve and none is new: ten newly counted genes plus RAD51D. CHAMP1 already had
a review file at the earlier source. Link availability is not audit completion;
RAD51D adds no count in this batch. The live queue is recorded for publication
applicability only and does not alter this frozen completion set.

[Checkpoint 334 session history](https://github.com/ai4curation/ai-gene-review/blob/main/history/projects/CLINGEN_MENDELIAN/2026-10-11T070056Z-codex-71fc99.yaml).

## Completion checkpoint 323 — 2026-10-10 22:30:43 UTC

**323 complete / 2,553 remaining in the frozen 2,876-gene catalog.**
CHD7, CHRNB1, CHST6, CHSY1, CHRNG, CHST14, CHRNB2 and CRLS1 are the eight new
distinct completions beyond published checkpoint 315. Each counts once after its
first qualifying substantive audit, including audits of pre-existing reviews and
qualifying work in another project. Products, review rounds, annotation actions,
DRAFT status and justified uncertainty add neither counts nor completion holds.
The existing counter definitions and historical exceptions remain in force.

| Gene | PR | Approved head | Approval | API merge time UTC | Merge commit |
|---|---|---|---|---|---|
| CHD7 | [#4592](https://github.com/ai4curation/ai-gene-review/pull/4592) | `dd3f3c660230aef11063a848124a9c808b5e462a` | [Approved](https://github.com/ai4curation/ai-gene-review/pull/4592#pullrequestreview-5480749662) | 2026-10-10T21:11:56Z | `0d8fed3b0f6a80edc6b776b818089929704101b8` |
| CHRNB1 | [#4632](https://github.com/ai4curation/ai-gene-review/pull/4632) | `8607a3dfbf6f592233ea36a0fb2f33087712351d` | [Approved](https://github.com/ai4curation/ai-gene-review/pull/4632#pullrequestreview-5480782910) | 2026-10-10T21:13:31Z | `93e292cb53ac066bf702090f2912ce2c0a22eb79` |
| CHST6 | [#4650](https://github.com/ai4curation/ai-gene-review/pull/4650) | `6fca64372e56c4793852c15de4c3cf01b7e6c632` | [Approved](https://github.com/ai4curation/ai-gene-review/pull/4650#pullrequestreview-5480767823) | 2026-10-10T21:14:38Z | `35d102bc46bae9377ad6c60151bed1f07c62bf85` |
| CHSY1 | [#4651](https://github.com/ai4curation/ai-gene-review/pull/4651) | `f6f28cf203783842e7124f2b34fa178bbf9284a4` | [Approved](https://github.com/ai4curation/ai-gene-review/pull/4651#pullrequestreview-5480814893) | 2026-10-10T21:33:17Z | `970f1d12e51dd7619a0c37b8d19c21abb34ed67a` |
| CHRNG | [#4639](https://github.com/ai4curation/ai-gene-review/pull/4639) | `de8a670ac47a5907179bdaf9fd38fd59b22362a7` | [Approved](https://github.com/ai4curation/ai-gene-review/pull/4639#pullrequestreview-5480832850) | 2026-10-10T21:35:04Z | `7c548120f93ee47df41bc80084a48f655cf1a0e9` |
| CHST14 | [#4643](https://github.com/ai4curation/ai-gene-review/pull/4643) | `e7b3c7df77fc5b7ddd849d9a4666701e5a522916` | [Approved](https://github.com/ai4curation/ai-gene-review/pull/4643#pullrequestreview-5480844571) | 2026-10-10T21:42:16Z | `6e2cfa65abae96aa195040053a5e22374eb11659` |
| CHRNB2 | [#4637](https://github.com/ai4curation/ai-gene-review/pull/4637) | `1074fbc54ba5d27469230d2caf76dddb5862c0d9` | [Approved](https://github.com/ai4curation/ai-gene-review/pull/4637#pullrequestreview-5480930133) | 2026-10-10T22:15:01Z | `4a45273dbcf15330bbf4b9b0ea698104cbb1338f` |
| CRLS1 | [#4476](https://github.com/ai4curation/ai-gene-review/pull/4476) | `870d8f5806dae5445751f1397a954ee8c718b53f` | [Approved](https://github.com/ai4curation/ai-gene-review/pull/4476#pullrequestreview-5475390620) | 2026-10-10T22:30:43Z | `a4b3afbbe831bdf07e4bea97064fd7a5fd814e71` |

- **CHD7**: approved 2026-10-10T20:46:12Z; [test (3.12)](https://github.com/ai4curation/ai-gene-review/actions/runs/38081860989/job/114300260369) succeeded 2026-10-10T21:07:08Z; [claude-review](https://github.com/ai4curation/ai-gene-review/actions/runs/38081860983/job/114300260799) succeeded 2026-10-10T20:46:32Z.
- **CHRNB1**: approved 2026-10-10T20:58:29Z; [test (3.12)](https://github.com/ai4curation/ai-gene-review/actions/runs/38081974472/job/114300595506) succeeded 2026-10-10T21:08:36Z; [claude-review](https://github.com/ai4curation/ai-gene-review/actions/runs/38081974475/job/114300595887) succeeded 2026-10-10T20:59:14Z.
- **CHST6**: approved 2026-10-10T20:53:01Z; [test (3.12)](https://github.com/ai4curation/ai-gene-review/actions/runs/38082198600/job/114301241299) succeeded 2026-10-10T21:11:07Z; [claude-review](https://github.com/ai4curation/ai-gene-review/actions/runs/38082198595/job/114301241943) succeeded 2026-10-10T20:53:17Z.
- **CHSY1**: approved 2026-10-10T21:10:36Z; [test (3.12)](https://github.com/ai4curation/ai-gene-review/actions/runs/38083574103/job/114305293627) succeeded 2026-10-10T21:30:55Z; [claude-review](https://github.com/ai4curation/ai-gene-review/actions/runs/38083574120/job/114305294103) succeeded 2026-10-10T21:10:51Z.
- **CHRNG**: approved 2026-10-10T21:16:45Z; [test (3.12)](https://github.com/ai4curation/ai-gene-review/actions/runs/38084117199/job/114306897441) succeeded 2026-10-10T21:30:57Z; [claude-review](https://github.com/ai4curation/ai-gene-review/actions/runs/38084117196/job/114306897739) succeeded 2026-10-10T21:17:04Z.
- **CHST14**: approved 2026-10-10T21:20:22Z; [test (3.12)](https://github.com/ai4curation/ai-gene-review/actions/runs/38084754502/job/114308842295) succeeded 2026-10-10T21:41:05Z; [claude-review](https://github.com/ai4curation/ai-gene-review/actions/runs/38084754688/job/114308842999) succeeded 2026-10-10T21:20:37Z.
- **CHRNB2**: approved 2026-10-10T21:51:46Z; [test (3.12)](https://github.com/ai4curation/ai-gene-review/actions/runs/38085230022/job/114310246457) succeeded 2026-10-10T22:12:33Z; [claude-review](https://github.com/ai4curation/ai-gene-review/actions/runs/38085230013/job/114310246685) succeeded 2026-10-10T21:52:05Z.
- **CRLS1**: approved 2026-10-09T21:10:45Z; [test (3.12)](https://github.com/ai4curation/ai-gene-review/actions/runs/37991214697/job/114025564175) succeeded 2026-10-09T21:47:45Z; [claude-review](https://github.com/ai4curation/ai-gene-review/actions/runs/37991214623/job/114025921387) succeeded 2026-10-09T21:10:59Z.

Every approval and both required check completions match the final approved head
and precede its actual merge. Complete final formal reviews and detailed approval
comments were read; blocking findings were discharged and remaining suggestions
were explicitly nonblocking. All review-thread collections are complete with zero
unresolved threads. Reviews that could not run local validation do not substitute
for the separately authenticated successful required CI.

Changed PR paths, changed gene files and complete gene directories are distinct:

| Gene | Changed PR paths | Changed gene files | Complete gene-directory blobs | Complete gene-tree OID |
|---|---:|---:|---:|---|
| CHD7 | 30 | 6 | 6 | `2b4d8bdb67a42552926475d1a691117eacd4566c` |
| CHRNB1 | 19 | 6 | 6 | `56b1f8bd83bd3bea7f57106d02bd76679bb54e16` |
| CHST6 | 21 | 6 | 6 | `7510be5a4e91778c637728eaa311876c737b68e8` |
| CHSY1 | 15 | 6 | 6 | `e8ddf7f66371437b826a346e8290a8ec0ef9fe94` |
| CHRNG | 17 | 6 | 6 | `a0f64b6cbef59a6d37d26d8ac2bdf6902cb4be7a` |
| CHST14 | 17 | 6 | 6 | `a1a164dbce6b06ca767de59f2edebddbaf263807` |
| CHRNB2 | 59 | 6 | 6 | `827e93c5245c7ae4c87dd635e248a74641b792d7` |
| CRLS1 | 159 | 8 | 8 | `713e066f8c6ea2234b74baba4a3775694211b766` |

The first seven gene PRs have **178** changed paths, all exact between approved
heads and merges. The external MitoTOL PR has **159** changed paths, **156** exact:
`cache/go/terms.csv`, `pages/projects/HOMOLOGY_PROPAGATION.html` and
`pages/projects/index.html` incorporate unrelated shared context at merge.
The GO cache gains 129 rows without removal; the two project pages gain unrelated
links/cards. No whole-PR equality is claimed for #4476. Its complete CRLS1 directory,
relevant history and all **17** referenced source blobs match its approved head
and actual merge exactly. The 337 gene-PR paths plus seven tracker315 paths give
**344** examined pairs, **341** exact and those three disclosed exceptions.

All **50 complete counted-gene directory blobs** match at the approved head,
individual merge, counted cutoff and authenticated source. This includes unchanged
machine/provider sources. Exact paths, Git blobs, byte counts and SHA-256 hashes
are recorded in queue update **57**.

### External qualification and excluded merged reviews

CRLS1 (HGNC:16148) was unchecked and had no prior review at the pre-#4476 main.
The merged work reviews all 30 GOA assertions (27 ACCEPT, two REMOVE, one
UNDECIDED), preserves two products and 24 references, and supplies a specific
CDP-dependent cardiolipin-synthase core and curation history. Its 30 source tuples
match literally. ROOT accepted the independently audited qualification at
**2026-10-10 23:01:03 UTC**. The external approval and qualification audit are used
at their recorded scope; this checkpoint is not a new full primary-literature or
quotation audit of CRLS1. It adds one completion, not all genes in the MitoTOL PR.

**CLPP and FH remain merged but incomplete for this campaign.** Their #4476
reviews contain 22 and 13 generic protein-binding REMOVE decisions respectively,
justified by informativeness or unestablished native context while allowing the
reported interactions to be real. The project's retention instruction and its
existing BCKDHB/BCL10/BCS1L/BIN1/BLM precedent require evidence-specific follow-up.
Neither gene was in the prior 322-member verified set. CLPP's earlier #4426 review
and the existence of newly merged FH files do not bypass that rule. Keep both
checkboxes untouched; do not convert actions mechanically or declare the interactions
false. These excluded, not-yet-qualified audits are not reversals of counted
completions and do not alter the preserved legacy `pending_followups` counter.

### Source, preserved history and editorial clarification

The frozen gene cutoff is [CRLS1 merge a4b3afbbe831](https://github.com/ai4curation/ai-gene-review/commit/a4b3afbbe831bdf07e4bea97064fd7a5fd814e71),
API `merged_at` **2026-10-10T22:30:43Z**. The authenticated source is the later
[tracker315 #4660 merge 147727e314dd](https://github.com/ai4curation/ai-gene-review/commit/147727e314ddf887b4dc501b9914af0f6eee833f),
API `merged_at` **2026-10-10T23:01:50Z**. Tracker315 was approved on
`c800bcdd95d5677cc6f4d93a74aebbead2baf50d`; both required checks preceded its merge and all seven changed paths
match approved and merged blobs. API merge times and commit times are recorded
separately. Later source or publication-base dates cannot add uncounted genes.

All **150** existing project history files remain protected under tree
`adf55b384cdda1e5d22295233b69b47b91af7267`. All seven existing parent-page history links
and the complete prior progress text are preserved. Reviewer #4660's editorial
points are addressed in current prose: the rule is **one count per gene**, the
term is **exact-head approval**, and availability warnings are measured against
the actual source context. For checkpoint 315, the committed parent render changed
from 1,860 to 1,857 warnings because CHCHD10, CHD2 and CHD8 became available;
calling that historical preview delta unchanged was imprecise. An identical fresh
baseline/candidate warning set is a different comparison. This clarification does
not rewrite any prior append-only history. Current parent preview warnings are **1,848**, equal to a fresh baseline using the
same source; progress has zero. Compared with checkpoint 315's preview, nine
availability warnings resolve (the eight counted genes plus FH), with no new
warnings. FH's newly available link does not grant campaign completion.

All 2,876 catalog association texts and frontmatter, the **235-object / 235-symbol**
queue array, all **56** prior completion-update texts and unrelated queue metadata
remain exact. Eight checkboxes change and update **57** is appended with an identical
JSON mirror. The first unchecked literal entry remains ACBD5. Counters are 323 for
`completed`, `campaign_audited_merged` and legacy `original_merged`, zero for
`pending_followups`, and 2,553 remaining.

The saved 22:57 UTC queue audit includes 15 PRs, including CLCN4 #4681 and the
published CHST3/CIB2 follow-up heads. Tracker315 is now actually merged; the other
open PRs remain excluded. The new session provenance will be linked at publication.

[Checkpoint 323 session history](https://github.com/ai4curation/ai-gene-review/blob/main/history/projects/CLINGEN_MENDELIAN/2026-10-10T233005Z-codex-3f117f.yaml).

## Completion checkpoint 315 — 2026-10-10 19:51:39 UTC

**315 complete / 2,561 remaining in the frozen 2,876-gene catalog.**
CHMP2B, CHCHD10, CHD8 and CHD2 are the four new distinct campaign completions
beyond published checkpoint 311. Each counts once after its first qualifying
substantive campaign audit, including audits of pre-existing reviews. Products,
review rounds, annotation actions, DRAFT status and justified uncertainty add
neither extra completions nor holds. Prior counting rules and exceptions stand.

| Gene | PR | Approved head | Approval | API merge time UTC | Merge commit |
|---|---|---|---|---|---|
| CHMP2B | [#4605](https://github.com/ai4curation/ai-gene-review/pull/4605) | [30be2a43fc2f](https://github.com/ai4curation/ai-gene-review/commit/30be2a43fc2f47d32320251b66082b767556c738) | [Approved](https://github.com/ai4curation/ai-gene-review/pull/4605#pullrequestreview-5480443860) | 2026-10-10T19:41:06Z | [6e9b6acc8eb9](https://github.com/ai4curation/ai-gene-review/commit/6e9b6acc8eb902937093965ab58f54fccff8cc5b) |
| CHCHD10 | [#4574](https://github.com/ai4curation/ai-gene-review/pull/4574) | [7729ff7dad9e](https://github.com/ai4curation/ai-gene-review/commit/7729ff7dad9ecc0d210d8a8aa1524bbf0eab51f5) | [Approved](https://github.com/ai4curation/ai-gene-review/pull/4574#pullrequestreview-5480469507) | 2026-10-10T19:42:32Z | [3aedc52f8279](https://github.com/ai4curation/ai-gene-review/commit/3aedc52f82794f012bc437275c3ece1d30151281) |
| CHD8 | [#4595](https://github.com/ai4curation/ai-gene-review/pull/4595) | [10ab59bc71ac](https://github.com/ai4curation/ai-gene-review/commit/10ab59bc71acad2ffcbb41c95d1fecfb3f0a6520) | [Approved](https://github.com/ai4curation/ai-gene-review/pull/4595#pullrequestreview-5480497659) | 2026-10-10T19:43:14Z | [0cb3cb1509e1](https://github.com/ai4curation/ai-gene-review/commit/0cb3cb1509e154b723d87e535dd2552bdf7c3d05) |
| CHD2 | [#4583](https://github.com/ai4curation/ai-gene-review/pull/4583) | [3db922a437a0](https://github.com/ai4curation/ai-gene-review/commit/3db922a437a0e0eecd79cf55aba9d15ccf44aa88) | [Approved](https://github.com/ai4curation/ai-gene-review/pull/4583#pullrequestreview-5480514357) | 2026-10-10T19:51:39Z | [e20dd96d4115](https://github.com/ai4curation/ai-gene-review/commit/e20dd96d41152636ac61f320e462b1339edba66f) |

- **CHMP2B**: approved at 19:11:48 UTC; [test (3.12)](https://github.com/ai4curation/ai-gene-review/actions/runs/38073806920/job/114276477674) succeeded at 19:31:57 UTC; [claude-review](https://github.com/ai4curation/ai-gene-review/actions/runs/38073806935/job/114276478279) succeeded at 19:12:03 UTC.
- **CHCHD10**: approved at 19:19:59 UTC; [test (3.12)](https://github.com/ai4curation/ai-gene-review/actions/runs/38074571626/job/114278736005) succeeded at 19:38:37 UTC; [claude-review](https://github.com/ai4curation/ai-gene-review/actions/runs/38074571631/job/114278736604) succeeded at 19:20:14 UTC.
- **CHD8**: approved at 19:28:00 UTC; [test (3.12)](https://github.com/ai4curation/ai-gene-review/actions/runs/38074813505/job/114279473299) succeeded at 19:39:26 UTC; [claude-review](https://github.com/ai4curation/ai-gene-review/actions/runs/38074813523/job/114279475834) succeeded at 19:28:15 UTC.
- **CHD2**: approved at 19:31:11 UTC; [test (3.12)](https://github.com/ai4curation/ai-gene-review/actions/runs/38075681998/job/114282033949) succeeded at 19:49:31 UTC; [claude-review](https://github.com/ai4curation/ai-gene-review/actions/runs/38075681996/job/114282034188) succeeded at 19:31:30 UTC.

All approvals and required check completions match the final heads and precede
the corresponding merges; there are zero unresolved review threads. Complete
final formal approvals and detailed comments were read. The reviewers discharged
the important findings and identified only nonblocking suggestions. These are
completed campaign audits, not counts of newly created files or additional isoforms.

Changed paths and complete gene directories have different scopes:

| Gene | Changed PR paths | Changed gene files | All gene-directory blobs at cutoff | Complete gene-tree OID |
|---|---:|---:|---:|---|
| CHMP2B | 13 | 6 | 8 | `16e1b37b20fcfd231e2b4e99b2e18b0a66307329` |
| CHCHD10 | 18 | 6 | 6 | `95effecc352323b1531c537390b87a5c9804e75b` |
| CHD8 | 24 | 5 | 5 | `eb0be3b2a37b700545e33eb8b1dd0eb1020a8358` |
| CHD2 | 15 | 6 | 6 | `2f333a6dcc8c31e1ef06b4d596e53f92a048e703` |

All **70 changed gene-PR paths** have equal blobs at the approved head and merge.
All **25 complete gene-directory artifacts** match at the approved head, individual
merge, counted-gene cutoff and authenticated tracker source. Unchanged source and
provider artifacts are included in the complete directories. Exact paths, sizes,
Git blobs and SHA-256 hashes are recorded in queue update **56**.

The frozen counted-gene cutoff is [CHD2 merge e20dd96d4115](https://github.com/ai4curation/ai-gene-review/commit/e20dd96d41152636ac61f320e462b1339edba66f),
API `merged_at` **2026-10-10T19:51:39Z**. The later authenticated source is
[tracker311 #4648 merge d1ce0f02e084](https://github.com/ai4curation/ai-gene-review/commit/d1ce0f02e084844e241b6003bed77cfa20569466),
API `merged_at` **2026-10-10T20:49:21Z**. Tracker311 was approved on
`8f74fe943668dfcdab99c2a50b20096babddb01d` at 20:30:21 UTC;
both required checks succeeded before its merge, and all **seven** changed-path
blobs match its approved and merge trees. GitHub API merge times and commit times
are recorded separately. The source contains all four counted merges and the
published checkpoint 311; its later date does not count any additional gene.
A later publication base cannot advance the fixed count without reconciliation.
CHD7 and all other open or subsequent PR merges are outside this checkpoint.

All **149 existing session histories** under `history/projects/CLINGEN_MENDELIAN/`
remain protected, authenticated by tree `877465c4fee26447284021757559a3ae195ef856`.
The six existing history links remain unchanged. The prior checkpoint 311's
forward-looking history sentence is corrected to describe its already committed
record; no old session-history file is rewritten. All other prior progress is exact.

All 2,876 catalog associations and frontmatter, the **235-object / 235-symbol**
serialized queue array, all **55 prior completion-update texts** and unrelated
queue metadata remain unchanged. Only the four named checkboxes change; update
**56** is appended with an identical JSON mirror. The first unchecked literal
entry remains ACBD5. Counter values are 315 for `completed`,
`campaign_audited_merged` and the legacy `original_merged` alias, zero for
`pending_followups`, and 2,561 remaining. Normal render previews use the complete
authenticated source-main inventory for link availability, independently of counts.

Session provenance accompanies this checkpoint at publication.

[Checkpoint 315 session history](https://github.com/ai4curation/ai-gene-review/blob/main/history/projects/CLINGEN_MENDELIAN/2026-10-10T211146Z-codex-4853e6.yaml).

## Completion checkpoint 311 — 2026-10-10 19:26:28 UTC

**311 complete / 2,565 remaining in the frozen 2,876-gene catalog.**
CFTR is the sole new completion beyond checkpoint 310. This counts the first
qualifying campaign audit of an existing review, not a newly created gene file.
The prior counting rules and exceptions are unchanged: one completed campaign
audit per primary gene, with no additional count or hold for products, repeated
reviews, annotation actions or justified biological uncertainty.

| Gene | PR | Approved head | Approval | API merge time UTC | Merge commit |
|---|---|---|---|---|---|
| CFTR | [#4568](https://github.com/ai4curation/ai-gene-review/pull/4568) | [6d3565c7c9eb](https://github.com/ai4curation/ai-gene-review/commit/6d3565c7c9eb5575203f5d8ac2d99e757fbe7b40) | [Approved](https://github.com/ai4curation/ai-gene-review/pull/4568#pullrequestreview-5480414462) | 2026-10-10T19:26:28Z | [4a9875aae93b](https://github.com/ai4curation/ai-gene-review/commit/4a9875aae93b762f99d87baf4621c9ededf6d71c) |

CFTR approval was submitted at **19:02:19 UTC**;
[test (3.12)](https://github.com/ai4curation/ai-gene-review/actions/runs/38073199144/job/114274687566) succeeded at 19:18:13 UTC; [claude-review](https://github.com/ai4curation/ai-gene-review/actions/runs/38073199273/job/114274688530) succeeded at 19:02:31 UTC. All gates match the final head and precede the actual merge,
with zero unresolved threads. The full final formal approval and detailed comment
were read; remaining suggestions are explicitly nonblocking. The audit preserves
203 historical annotation objects while revising their scientific assessments and
three core functions; the review's expanded-source deferral remains explicit.

All **13 changed PR paths** have equal blobs in the approved-head and merge
commit trees. Six changed gene-directory files are distinguished from the
**12 total recursive gene-directory blobs** at the cutoff: unchanged source and
provider artifacts remain part of the complete gene tree. The complete
[CFTR tree at the cutoff](https://github.com/ai4curation/ai-gene-review/tree/4a9875aae93b762f99d87baf4621c9ededf6d71c/genes/human/CFTR)
`b42601a3ce347fec5156f10641d9cbcca0b00aca` matches the approved, merge and authenticated source trees.
Exact paths, sizes, Git blobs and SHA-256 hashes are retained in queue update 55.

The authenticated source is [commit 4a9875aae93b](https://github.com/ai4curation/ai-gene-review/commit/4a9875aae93b762f99d87baf4621c9ededf6d71c),
which is also the frozen CFTR completion cutoff. It contains the earlier
[tracker310 #4631](https://github.com/ai4curation/ai-gene-review/pull/4631)
merge `bb51b3177deed88185627c2017483b18a4de0f94` at **19:25:37 UTC**. That tracker was approved
at 19:08:32 UTC on `a92f2976550ad7b7e9f37df24b2d85f5a04ea4e6`;
both required checks succeeded before its merge, and all seven changed-path
blobs match the approved head and merge tree. Merge times use **GitHub API
`merged_at`**, with `committedDate` recorded separately; the values coincide for
both of these merges. A later publication base is distinct and cannot count any
subsequent gene merge without another reconciliation.

All **148 existing records** in `history/projects/CLINGEN_MENDELIAN/`, authenticated
by tree `c7db335f2efd5854a2d7e02d24c06c864facaf9a`, are protected. The five session-history
links already present in the parent page remain unchanged:

- `history/projects/CLINGEN_MENDELIAN/2026-10-10T081738Z-codex-0d3c8d.yaml`
- `history/projects/CLINGEN_MENDELIAN/2026-10-10T092814Z-codex-e50f41.yaml`
- `history/projects/CLINGEN_MENDELIAN/2026-10-10T110009Z-codex-bd1c4a.yaml`
- `history/projects/CLINGEN_MENDELIAN/2026-10-10T132811Z-codex-22f68a.yaml`
- `history/projects/CLINGEN_MENDELIAN/2026-10-10T174737Z-codex-0f8ff7.yaml`

The checkpoint 311 session history is committed and linked below.
No existing history or gene artifact is edited. Render previews use the complete
authenticated source-main gene-review inventory; later link availability can change
independently of this fixed count.

All 2,876 catalog associations and frontmatter, the **235-object / 235-symbol**
serialized queue array, all **54 prior completion-update object texts**, unrelated
queue metadata and prior progress are preserved. Only CFTR's checkbox changes;
update **55** is appended with an identical JSON mirror. The first unchecked
literal entry remains ACBD5. Counter values are 311 for `completed`,
`campaign_audited_merged` and the legacy `original_merged` alias, with zero
`pending_followups` and 2,565 remaining.

[Checkpoint 311 session history](https://github.com/ai4curation/ai-gene-review/blob/main/history/projects/CLINGEN_MENDELIAN/2026-10-10T193909Z-codex-ab8464.yaml).

## Completion checkpoint 310 — 2026-10-10 17:19:03 UTC

**310 complete / 2,566 remaining in the frozen 2,876-gene catalog.**
CHAT is the sole new completion beyond checkpoint 309. The existing counting
rules and queue exceptions are unchanged: one qualifying campaign audit per
primary gene, with no additional count or hold for products, repeated reviews,
annotation actions or justified biological uncertainty.

| Gene | PR | Approved head | Approval | API merge time UTC | Merge commit |
|---|---|---|---|---|---|
| CHAT | [#4572](https://github.com/ai4curation/ai-gene-review/pull/4572) | [e589d7f1f8b2](https://github.com/ai4curation/ai-gene-review/commit/e589d7f1f8b21010ea16ec68c9b76a587512177c) | [Approved](https://github.com/ai4curation/ai-gene-review/pull/4572#pullrequestreview-5480030944) | 2026-10-10T17:19:03Z | [d029f88f542f](https://github.com/ai4curation/ai-gene-review/commit/d029f88f542f1702a286982b20a89349e979c302) |

CHAT approval was submitted at **17:12:28 UTC**; [test (3.12)](https://github.com/ai4curation/ai-gene-review/actions/runs/38056392609/job/114225683545) succeeded at 14:36:38 UTC; [claude-review](https://github.com/ai4curation/ai-gene-review/actions/runs/38056392616/job/114261905807) succeeded at 17:13:28 UTC.
These gates all match the final head and precede the actual merge, with zero
unresolved review threads. The complete final approval and review comment were
read; remaining suggestions are explicitly nonblocking. This first campaign
review creates the CHAT review and counts once.

All **18 changed PR paths** have equal blobs in the approved-head and merge
commit trees. The **six changed gene-directory files** are also the **six total
recursive gene-directory blobs** at the cutoff. The complete
[CHAT tree at the cutoff](https://github.com/ai4curation/ai-gene-review/tree/d029f88f542f1702a286982b20a89349e979c302/genes/human/CHAT)
`5cc5a36bb01904cd8ce8c39836dc47a6a6ff2a7a` matches the approved, merge and authenticated source trees.
Exact path, size, Git-blob and SHA-256 evidence is retained in queue update 54.

The source snapshot is [commit 8cd2c9286f44](https://github.com/ai4curation/ai-gene-review/commit/8cd2c9286f44f998ce175f034a56ee6c7b49f4cc),
the actual [tracker309 #4581](https://github.com/ai4curation/ai-gene-review/pull/4581)
merge at **17:25:21 UTC**, after the frozen CHAT cutoff at **17:19:03 UTC**.
The source tracker was approved at 17:14:22 UTC on
`ded21ac6da3d0cf79152a77d1ae65ad5aa5869f6` and both required checks succeeded before merge;
all seven tracker changed-path blobs match its approved head and merge tree.
The times in this checkpoint use **GitHub API `merged_at`**, not commit timestamps:
CHAT's merge commit has `committedDate` **17:19:02 UTC**, while its API merge time
is **17:19:03 UTC**. A later publication base is a third reference point and must
preserve the six project preimages without adding subsequent gene completions.

All **147 existing records** in `history/projects/CLINGEN_MENDELIAN/`, authenticated
by tree `f9251d3d41ff393dcc472a1a257b43acda7d81c3`, are protected. In particular, the four
session-history links already present in the parent page remain unchanged:

- `history/projects/CLINGEN_MENDELIAN/2026-10-10T081738Z-codex-0d3c8d.yaml`
- `history/projects/CLINGEN_MENDELIAN/2026-10-10T092814Z-codex-e50f41.yaml`
- `history/projects/CLINGEN_MENDELIAN/2026-10-10T110009Z-codex-bd1c4a.yaml`
- `history/projects/CLINGEN_MENDELIAN/2026-10-10T132811Z-codex-22f68a.yaml`

The publisher will scaffold and validate the new session history normally.
No existing history or gene artifact is edited. The render preview uses the
complete authenticated source-main gene-review inventory; later link availability
can change independently of this fixed count.

All 2,876 catalog associations and frontmatter, the **235-object / 235-symbol**
serialized queue array, all **53 prior completion-update object texts**, unrelated
queue metadata and all prior progress are preserved. Only CHAT's checkbox changes;
update **54** is appended, with an identical JSON mirror. The first unchecked
literal catalog entry remains ACBD5. Counter values are 310 for `completed`,
`campaign_audited_merged` and the legacy `original_merged` alias, with zero
`pending_followups` and 2,566 remaining.

[Checkpoint 310 session history](https://github.com/ai4curation/ai-gene-review/blob/main/history/projects/CLINGEN_MENDELIAN/2026-10-10T174737Z-codex-0f8ff7.yaml).

## Completion checkpoint 309 — 2026-10-10 13:12:56 UTC

**309 complete / 2,567 remaining in the frozen 2,876-gene catalog.** The first
qualifying campaign reviews for CFH, CFAP410, CFAP418, CFAP43, CFL2, CFI add 6 distinct completions
beyond published checkpoint 303. An older review's existence does not substitute
for its substantive campaign audit. Products, repeated reviews, annotation actions
and justified biological uncertainty add neither completions nor holds.

| Gene | PR | Final head | Approval | Merged UTC | Merge commit |
|---|---|---|---|---|---|
| CFH | [#4555](https://github.com/ai4curation/ai-gene-review/pull/4555) | [cebc1de09e28](https://github.com/ai4curation/ai-gene-review/commit/cebc1de09e286ac927413c20d549153b56e56df6) | [Approved](https://github.com/ai4curation/ai-gene-review/pull/4555#pullrequestreview-5478810092) | 2026-10-10T12:08:30Z | [0cd7233f9167](https://github.com/ai4curation/ai-gene-review/commit/0cd7233f916785d509328947a2b38b2190aa7446) |
| CFAP410 | [#4550](https://github.com/ai4curation/ai-gene-review/pull/4550) | [e5d232ede4e4](https://github.com/ai4curation/ai-gene-review/commit/e5d232ede4e46c42f1c751904feeeb159f77d058) | [Approved](https://github.com/ai4curation/ai-gene-review/pull/4550#pullrequestreview-5478864008) | 2026-10-10T12:33:27Z | [5173dba5df3f](https://github.com/ai4curation/ai-gene-review/commit/5173dba5df3f36f8d47fc3aad086d22d5c3c8bba) |
| CFAP418 | [#4553](https://github.com/ai4curation/ai-gene-review/pull/4553) | [2c646dedf1d1](https://github.com/ai4curation/ai-gene-review/commit/2c646dedf1d1d05bf021a355fc5718729aeebe53) | [Approved](https://github.com/ai4curation/ai-gene-review/pull/4553#pullrequestreview-5478887253) | 2026-10-10T13:07:39Z | [4b7aeee762b0](https://github.com/ai4curation/ai-gene-review/commit/4b7aeee762b01f13d4fa8e7052d71d22122cd27d) |
| CFAP43 | [#4554](https://github.com/ai4curation/ai-gene-review/pull/4554) | [4c1d18eeca0c](https://github.com/ai4curation/ai-gene-review/commit/4c1d18eeca0c3ee70e77918525ffee4ad00853d6) | [Approved](https://github.com/ai4curation/ai-gene-review/pull/4554#pullrequestreview-5478890423) | 2026-10-10T13:09:11Z | [7e2ad4dc8150](https://github.com/ai4curation/ai-gene-review/commit/7e2ad4dc81505816c470a5e4a95a64791fc86743) |
| CFL2 | [#4562](https://github.com/ai4curation/ai-gene-review/pull/4562) | [33d284c3a2bc](https://github.com/ai4curation/ai-gene-review/commit/33d284c3a2bc15dc47232273aa6de3a29f23e071) | [Approved](https://github.com/ai4curation/ai-gene-review/pull/4562#pullrequestreview-5478969623) | 2026-10-10T13:11:24Z | [76a745c581ad](https://github.com/ai4curation/ai-gene-review/commit/76a745c581ad8a346ea47d815f9b805f3ff6de3a) |
| CFI | [#4556](https://github.com/ai4curation/ai-gene-review/pull/4556) | [1cd882936145](https://github.com/ai4curation/ai-gene-review/commit/1cd882936145451b4ef89348b98dfe5f9075df41) | [Approved](https://github.com/ai4curation/ai-gene-review/pull/4556#pullrequestreview-5478998677) | 2026-10-10T13:12:56Z | [91bbc12a004a](https://github.com/ai4curation/ai-gene-review/commit/91bbc12a004a42b6c26f3f9c58a1bd5f33556398) |

**CFH:** approval at 11:40:56 UTC; [test (3.12)](https://github.com/ai4curation/ai-gene-review/actions/runs/38046731142/job/114197660739) succeeded at 12:02:41 UTC; [claude-review](https://github.com/ai4curation/ai-gene-review/actions/runs/38046731130/job/114197661141) succeeded at 11:41:52 UTC. All gates precede the actual merge at 12:08:30 UTC and refer to the same approved head, with zero unresolved threads. This is a newly added primary review, counted once. The **39 changed PR paths**, **6 changed gene-directory files** and **6 total recursive gene-directory blobs at the cutoff** are separate measurements. All changed paths have equal blobs at the approved-head and merge-commit trees. The [complete cutoff CFH tree](https://github.com/ai4curation/ai-gene-review/tree/91bbc12a004a42b6c26f3f9c58a1bd5f33556398/genes/human/CFH) `1dea1de4748d6e29411c4d1c020454ff033ff2c3` matches the approved and merge trees; exact artifacts and changed-path blobs are recorded in the queue update.

**CFAP410:** approval at 12:02:18 UTC; [test (3.12)](https://github.com/ai4curation/ai-gene-review/actions/runs/38047741349/job/114200581789) succeeded at 12:25:26 UTC; [claude-review](https://github.com/ai4curation/ai-gene-review/actions/runs/38047741389/job/114200582130) succeeded at 12:03:00 UTC. All gates precede the actual merge at 12:33:27 UTC and refer to the same approved head, with zero unresolved threads. This is a substantive campaign audit of a pre-existing review, counted once. The **6 changed PR paths**, **4 changed gene-directory files** and **11 total recursive gene-directory blobs at the cutoff** are separate measurements. All changed paths have equal blobs at the approved-head and merge-commit trees. The [complete cutoff CFAP410 tree](https://github.com/ai4curation/ai-gene-review/tree/91bbc12a004a42b6c26f3f9c58a1bd5f33556398/genes/human/CFAP410) `deb34bbdd7a5bc9670fd0c0b1eab73022a7aa7c3` matches the approved and merge trees; exact artifacts and changed-path blobs are recorded in the queue update.

**CFAP418:** approval at 12:11:44 UTC; [test (3.12)](https://github.com/ai4curation/ai-gene-review/actions/runs/38047978384/job/114201256887) succeeded at 12:28:35 UTC; [claude-review](https://github.com/ai4curation/ai-gene-review/actions/runs/38047978387/job/114201257058) succeeded at 12:12:01 UTC. All gates precede the actual merge at 13:07:39 UTC and refer to the same approved head, with zero unresolved threads. This is a substantive campaign audit of a pre-existing review, counted once. The **15 changed PR paths**, **9 changed gene-directory files** and **33 total recursive gene-directory blobs at the cutoff** are separate measurements. All changed paths have equal blobs at the approved-head and merge-commit trees. The [complete cutoff CFAP418 tree](https://github.com/ai4curation/ai-gene-review/tree/91bbc12a004a42b6c26f3f9c58a1bd5f33556398/genes/human/CFAP418) `35e8ceff95da33f38db7b34a9099b8bc74b36bcb` matches the approved and merge trees; exact artifacts and changed-path blobs are recorded in the queue update.

**CFAP43:** approval at 12:13:07 UTC; [test (3.12)](https://github.com/ai4curation/ai-gene-review/actions/runs/38048081716/job/114201552446) succeeded at 12:31:41 UTC; [claude-review](https://github.com/ai4curation/ai-gene-review/actions/runs/38048081725/job/114201552646) succeeded at 12:13:53 UTC. All gates precede the actual merge at 13:09:11 UTC and refer to the same approved head, with zero unresolved threads. This is a newly added primary review, counted once. The **16 changed PR paths**, **6 changed gene-directory files** and **6 total recursive gene-directory blobs at the cutoff** are separate measurements. All changed paths have equal blobs at the approved-head and merge-commit trees. The [complete cutoff CFAP43 tree](https://github.com/ai4curation/ai-gene-review/tree/91bbc12a004a42b6c26f3f9c58a1bd5f33556398/genes/human/CFAP43) `3cbd3238d7312e00ddcc773b5f08adec1aa49b6a` matches the approved and merge trees; exact artifacts and changed-path blobs are recorded in the queue update.

**CFL2:** approval at 12:41:09 UTC; [test (3.12)](https://github.com/ai4curation/ai-gene-review/actions/runs/38049488145/job/114205563121) succeeded at 13:03:37 UTC; [claude-review](https://github.com/ai4curation/ai-gene-review/actions/runs/38049487913/job/114205563854) succeeded at 12:41:24 UTC. All gates precede the actual merge at 13:11:24 UTC and refer to the same approved head, with zero unresolved threads. This is a newly added primary review, counted once. The **16 changed PR paths**, **6 changed gene-directory files** and **6 total recursive gene-directory blobs at the cutoff** are separate measurements. All changed paths have equal blobs at the approved-head and merge-commit trees. The [complete cutoff CFL2 tree](https://github.com/ai4curation/ai-gene-review/tree/91bbc12a004a42b6c26f3f9c58a1bd5f33556398/genes/human/CFL2) `376b6960951f160dd4451be2f224447bfe5d7635` matches the approved and merge trees; exact artifacts and changed-path blobs are recorded in the queue update.

**CFI:** approval at 12:50:10 UTC; [test (3.12)](https://github.com/ai4curation/ai-gene-review/actions/runs/38050053284/job/114207189972) succeeded at 13:09:26 UTC; [claude-review](https://github.com/ai4curation/ai-gene-review/actions/runs/38050053248/job/114207190412) succeeded at 12:50:21 UTC. All gates precede the actual merge at 13:12:56 UTC and refer to the same approved head, with zero unresolved threads. This is a newly added primary review, counted once. The **17 changed PR paths**, **6 changed gene-directory files** and **6 total recursive gene-directory blobs at the cutoff** are separate measurements. All changed paths have equal blobs at the approved-head and merge-commit trees. The [complete cutoff CFI tree](https://github.com/ai4curation/ai-gene-review/tree/91bbc12a004a42b6c26f3f9c58a1bd5f33556398/genes/human/CFI) `590581a3ed5d3312aaac972742382a57023d9c2f` matches the approved and merge trees; exact artifacts and changed-path blobs are recorded in the queue update.

The authenticated source snapshot is
[commit 91bbc12a004a](https://github.com/ai4curation/ai-gene-review/commit/91bbc12a004a42b6c26f3f9c58a1bd5f33556398).
It contains [tracker303 PR #4551](https://github.com/ai4curation/ai-gene-review/pull/4551),
actually merged at **12:10:12 UTC** in `39a7a8a8454f9a3efc2bee1ac1ff714afff70af5` from approved head
`d5017584923ae614f2f6868737f9560bec24f573`. Its exact-head approval, required checks and complete
changed-path blob equality were authenticated separately. The frozen gene-completion
cutoff is **13:12:56 UTC** at `91bbc12a004a42b6c26f3f9c58a1bd5f33556398`. Any later publication checkout is a third
reference point: ROOT must verify the six project preimages before import and must
not fold subsequent gene merges into this checkpoint. All four existing tracker
history records remain exact; new parent/progress history links will be scaffolded
normally by the publisher.

The render produced from main is authoritative for gene-link availability.
This preview uses the complete authenticated source-main gene-review inventory,
including the newly completed genes. Later link availability can change as genes
merge without changing this frozen completion count.

Counter meanings are unchanged: `campaign_audited_merged`, legacy `original_merged`
and `completed` are 309; `pending_followups` is zero. Literal `$.genes` remains
**235 objects / 235 distinct symbols**. All 2,876 catalog associations and
frontmatter, the serialized queue array, all **52 prior update object texts**,
unrelated queue metadata and previous progress text remain exact. Only the listed
6 checkboxes change; update **53** is appended and the JSON mirror is
byte-identical. The first unchecked literal catalog gene remains ACBD5. No gene
science, source cache or old history record is edited.

Evidence inspected and checkpoint recorded at 2026-10-10 13:15:09 UTC.

[Checkpoint 309 session history](https://github.com/ai4curation/ai-gene-review/blob/main/history/projects/CLINGEN_MENDELIAN/2026-10-10T132811Z-codex-22f68a.yaml).

## Completion checkpoint 303 — 2026-10-10 10:35:31 UTC

**303 complete / 2,573 remaining in the frozen 2,876-gene catalog.** Count only
CFAP300's first qualifying substantive campaign audit beyond checkpoint 302.
The primary YAML was modified, not newly created: its older review did not already
constitute this campaign's completion. Products, retained authored annotations and
unresolved molecular-function biology are not additional counts or completion holds.

| Gene | PR | Final head | Approval | Merged UTC | Merge commit |
|---|---|---|---|---|---|
| CFAP300 | [#4537](https://github.com/ai4curation/ai-gene-review/pull/4537) | [2ce993337db4](https://github.com/ai4curation/ai-gene-review/commit/2ce993337db434922b345a71d2e62d062dfbe9e8) | [Approved](https://github.com/ai4curation/ai-gene-review/pull/4537#pullrequestreview-5478629937) | 2026-10-10T10:35:31Z | [2f68dd87cb96](https://github.com/ai4curation/ai-gene-review/commit/2f68dd87cb96a240d03d5debc6c7f131bb7b2808) |

Approval was submitted at 10:32:35 UTC; [test (3.12)](https://github.com/ai4curation/ai-gene-review/actions/runs/38038301303/job/114173278760) succeeded at 09:20:49 UTC; [claude-review](https://github.com/ai4curation/ai-gene-review/actions/runs/38038301308/job/114184993286) succeeded at 10:32:53 UTC.
All three gates refer to the same final head and precede the actual 10:35:31 UTC
merge. There are no unresolved review threads. All **seven changed PR paths**
have identical blobs at the approved-head and merge-commit trees. The **four changed
gene-directory files** are a different scope from **all 19 recursive gene-directory
blobs at the cutoff**, which include preserved sources and provider artifacts.
The complete [CFAP300 tree](https://github.com/ai4curation/ai-gene-review/tree/2f68dd87cb96a240d03d5debc6c7f131bb7b2808/genes/human/CFAP300)
`b7b7cdbf9c76ece61c8157b9a11517d6b7ef13cb` is equal at head and merge/cutoff.
The appended queue record contains every changed-path blob and all 19 cutoff artifacts.

The exact tracker preimage is open [PR #4551](https://github.com/ai4curation/ai-gene-review/pull/4551)
[head 13435e510e4f](https://github.com/ai4curation/ai-gene-review/commit/13435e510e4f68f6b0b345c62deed08b63996d3d), preserving its
301/302 checkpoints, three existing history records and later review corrections.
It is not described as a merged tracker snapshot. The distinct biological cutoff
is actual main [commit 2f68dd87cb96](https://github.com/ai4curation/ai-gene-review/commit/2f68dd87cb96a240d03d5debc6c7f131bb7b2808).
A later publisher base cannot advance that cutoff; ROOT must guard the same six
project preimages, preserve the PR ancestry and append genuine session history.
The prior correction distinguishing changed artifacts from whole-directory files
and the restored CERKL review link remain intact.

Counter definitions are unchanged: `campaign_audited_merged`, legacy
`original_merged` and `completed` are 303; `pending_followups` is zero. Literal
`$.genes` is still **235 objects / 235 distinct symbols**, not the count of every
nested historical gene key. All 2,876 catalog associations and frontmatter, the
serialized queue array, all 51 prior update object texts, unrelated queue metadata
and all previous progress text are preserved. Only CFAP300's checkbox changes;
update 52 is appended and the JSON mirror is exact. The first unchecked literal
catalog gene remains ACBD5. No gene science or source cache is edited.

Evidence inspected and this follow-up recorded at 2026-10-10 10:51:57 UTC.

[Checkpoint 303 session history](https://github.com/ai4curation/ai-gene-review/blob/main/history/projects/CLINGEN_MENDELIAN/2026-10-10T110009Z-codex-bd1c4a.yaml).

## Completion checkpoint 302 — 2026-10-10 09:06:56 UTC

**302 complete / 2,574 remaining in the frozen 2,876-gene catalog.** CERKL
adds one first counted primary campaign review beyond checkpoint 301. Its
primary review YAML was added by the qualifying PR. Its eight products and
COMPLETE artifact status are not additional campaign completions. No completion
holds remain, and no later gene merge is included.

| Gene | PR | Final head | Approval | Merged UTC | Merge commit |
|---|---|---|---|---|---|
| CERKL | [#4531](https://github.com/ai4curation/ai-gene-review/pull/4531) | [eea866be3895](https://github.com/ai4curation/ai-gene-review/commit/eea866be3895951957a67d93b3ca9a76077aae9c) | [Approved](https://github.com/ai4curation/ai-gene-review/pull/4531#pullrequestreview-5478354438) | 2026-10-10T09:06:56Z | [5928e194d4a4](https://github.com/ai4curation/ai-gene-review/commit/5928e194d4a4e43bdd74b9b1f307a142107daa46) |

The final head was approved at 08:42:54 UTC;
[test (3.12)](https://github.com/ai4curation/ai-gene-review/actions/runs/38036729073/job/114168591113) succeeded at 09:03:17 UTC on the same head; [claude-review](https://github.com/ai4curation/ai-gene-review/actions/runs/38036729057/job/114168591533) succeeded at 08:43:10 UTC on the same head. Both checks and approval precede the 09:06:56 UTC merge.
Authenticated review threads contain no unresolved entries. All
**20 changed PR paths** have equal blobs at the approved head and actual merge.
The **six changed gene-directory files** and **all six gene-directory blobs** at
the cutoff are separate counted scopes. For a case where the counts differ,
see the [checkpoint 301 CEP290 example](#completion-checkpoint-301-2026-10-10-075854-utc):
four changed gene files versus eight directory blobs. The complete CERKL tree
[b0c153f1efc1](https://github.com/ai4curation/ai-gene-review/tree/5928e194d4a4e43bdd74b9b1f307a142107daa46/genes/human/CERKL)
is identical at the approved head and merge/cutoff. The appended queue evidence
records every changed-path blob and every cutoff gene artifact, with hashes.

The tracker preimage is [PR #4551](https://github.com/ai4curation/ai-gene-review/pull/4551)
at [head 7005ce6da531](https://github.com/ai4curation/ai-gene-review/commit/7005ce6da5315135560efb283ebd698790a584b3),
which already contains checkpoint 301 and its genuine session history. That PR
was open when this update was prepared; this is a follow-up on the same PR,
not a claim that checkpoint 301 had merged. The biological completion cutoff
is actual main [commit 5928e194d4a4](https://github.com/ai4curation/ai-gene-review/commit/5928e194d4a4e43bdd74b9b1f307a142107daa46).
These are distinct source roles. The publisher must preserve the existing PR
ancestry, guard its exact project preimages, append genuine session history and
rerender. A later publication base does not move the cutoff.

The checkpoint 288 counter definitions continue unchanged:
`campaign_audited_merged` and its legacy compatibility alias `original_merged`
are 302; `pending_followups` is zero; `completed` is 302. The literal queue
array `$.genes` remains **235 objects / 235 distinct symbols**, independently
parsed from baseline [blob c3d049524fd0](https://github.com/ai4curation/ai-gene-review/blob/7005ce6da5315135560efb283ebd698790a584b3/projects/CLINGEN_MENDELIAN/publication-queue.json).
Historical nested observations are not queue-array entries. The checkpoint 301
cardinality and artifact-scope clarifications are preserved without rewriting.

All 2,876 catalog rows, association text and frontmatter, the complete serialized
235-object queue array, all 50 prior completion-update object texts, and all
previous progress text are preserved. Only the CERKL checkbox changes; update
51 is appended, and both queue mirrors remain identical. No gene science,
provider report or cached source is changed. DRAFT status or a justified
UNDECIDED annotation does not itself create a campaign hold. The first unchecked
gene in literal catalog order remains ACBD5.

Authenticated evidence was read and this follow-up recorded at 2026-10-10 09:20:21 UTC.


The committed project pages were regenerated using the six authenticated CERKL
artifacts at the frozen merge cutoff as temporary rendering context. CERKL now
links to its review; the parent page retains 1,865 missing-review warnings for
other genes. This rendering context does not add gene files to the tracker PR.

[Tracker review follow-up history](https://github.com/ai4curation/ai-gene-review/blob/main/history/projects/CLINGEN_MENDELIAN/2026-10-10T101502Z-codex-2b22e1.yaml).

[Checkpoint 302 session history](https://github.com/ai4curation/ai-gene-review/blob/main/history/projects/CLINGEN_MENDELIAN/2026-10-10T092814Z-codex-e50f41.yaml).

## Completion checkpoint 301 — 2026-10-10 07:58:54 UTC

**301 complete / 2,575 remaining in the frozen 2,876-gene catalog.** CEP57,
CEP85L and CFAP221 add three first counted primary campaign audits beyond
checkpoint 298. Each PR adds its primary review file and counts once as a
catalog gene, irrespective of product count. No required follow-up holds remain.
Supplementary products and repeated reviews of already counted genes add no
completion.

| Gene | PR | Final head | Approval | Merged UTC | Merge commit |
|---|---|---|---|---|---|
| CEP57 | [#4516](https://github.com/ai4curation/ai-gene-review/pull/4516) | [9b0f809ae8bf](https://github.com/ai4curation/ai-gene-review/commit/9b0f809ae8bf9dda7c50b928c0efa2c003817380) | [Approved](https://github.com/ai4curation/ai-gene-review/pull/4516#pullrequestreview-5478159239) | 2026-10-10T07:45:32Z | [074064fe4e3e](https://github.com/ai4curation/ai-gene-review/commit/074064fe4e3e486281e905dd4dd654a923dab37b) |
| CEP85L | [#4525](https://github.com/ai4curation/ai-gene-review/pull/4525) | [056d7d9341c5](https://github.com/ai4curation/ai-gene-review/commit/056d7d9341c5543169305007ca922c2db3ca9a4a) | [Approved](https://github.com/ai4curation/ai-gene-review/pull/4525#pullrequestreview-5478158300) | 2026-10-10T07:46:04Z | [2268291181e3](https://github.com/ai4curation/ai-gene-review/commit/2268291181e331573261bb670e68d761d98cd96d) |
| CFAP221 | [#4534](https://github.com/ai4curation/ai-gene-review/pull/4534) | [b3e0d12f0cb6](https://github.com/ai4curation/ai-gene-review/commit/b3e0d12f0cb6a122f611034aea5490c80f573e81) | [Approved](https://github.com/ai4curation/ai-gene-review/pull/4534#pullrequestreview-5478179123) | 2026-10-10T07:58:54Z | [8a69f3d2b551](https://github.com/ai4curation/ai-gene-review/commit/8a69f3d2b551d632a37bfeb6217a7d667db8d51b) |

CEP57's exact head was approved at 07:38:37 UTC; [test (3.12)](https://github.com/ai4curation/ai-gene-review/actions/runs/38033332968/job/114158593362) succeeded at 07:40:42 UTC; [claude-review](https://github.com/ai4curation/ai-gene-review/actions/runs/38033333052/job/114162799683) succeeded at 07:39:27 UTC, before its 07:45:32 UTC merge.

CEP85L's exact head was approved at 07:38:13 UTC; [test (3.12)](https://github.com/ai4curation/ai-gene-review/actions/runs/38033552053/job/114159239207) succeeded at 07:33:34 UTC; [claude-review](https://github.com/ai4curation/ai-gene-review/actions/runs/38033552061/job/114162800012) succeeded at 07:38:26 UTC, before its 07:46:04 UTC merge.

CFAP221's exact head was approved at 07:44:57 UTC; [test (3.12)](https://github.com/ai4curation/ai-gene-review/actions/runs/38034626296/job/114162399058) succeeded at 07:58:00 UTC; [claude-review](https://github.com/ai4curation/ai-gene-review/actions/runs/38034626300/job/114163215577) succeeded at 07:45:11 UTC, before its 07:58:54 UTC merge.

Authenticated records contain zero unresolved review threads. Every changed
PR path has the same blob at the approved head and actual merge. Each complete
gene-directory tree is also identical at the approved head, actual merge and
frozen CFAP221 cutoff. The baseline tracker298 final head, approval, required
checks, merge and all seven changed paths were independently verified.

| Gene | All changed PR paths | Changed gene-directory files | All gene-directory blobs at cutoff | Cutoff tree |
|---|---:|---:|---:|---|
| CEP57 | 19 | 6 | 6 | [cb01c0989f37](https://github.com/ai4curation/ai-gene-review/tree/8a69f3d2b551d632a37bfeb6217a7d667db8d51b/genes/human/CEP57) |
| CEP85L | 12 | 6 | 6 | [fcf3ce9f98fa](https://github.com/ai4curation/ai-gene-review/tree/8a69f3d2b551d632a37bfeb6217a7d667db8d51b/genes/human/CEP85L) |
| CFAP221 | 15 | 6 | 6 | [2fdda0119110](https://github.com/ai4curation/ai-gene-review/tree/8a69f3d2b551d632a37bfeb6217a7d667db8d51b/genes/human/CFAP221) |

These are three separate scopes: the complete PR diff, changed files under the
gene directory, and every blob recursively present in that directory at the
cutoff. The new queue evidence names each scope explicitly and records the
path/blob lists. In the preserved checkpoint 298 records, the legacy
`cutoff_gene_artifact_count` field counted changed gene-directory files:
CEP290 had four changed files but eight total directory blobs; CEP41 had six
in both scopes. Those historical values are not rewritten.

The source snapshot is [commit e49cb9becb5b](https://github.com/ai4curation/ai-gene-review/commit/e49cb9becb5bf0b3bcb307b23d8fa4a535c41536),
the actual [tracker298 #4533](https://github.com/ai4curation/ai-gene-review/pull/4533)
merge at 2026-10-10T07:56:46Z. Four source files and two derived-page preimages
are authenticated there and unchanged at the later CFAP221 completion cutoff.
CEP57 and CEP85L merged before that tracker source snapshot, but its frozen
checkpoint 298 did not count them. The eventual publication branch base is
separate: if later, all six preimages must match and that base must be recorded.
No later completion is included.

The counter definitions established at checkpoint 288 remain in force:
`campaign_audited_merged` counts distinct frozen-catalog primary genes with a
merged campaign review; subtracting `pending_followups` gives `completed`.
`original_merged` remains the compatibility alias in this appended snapshot.
The three applicable values are 301, 0 and 301. Existing file presence,
supplementary products and repeated reviews do not independently add campaign
completions. Checkpoints 299 and 300 are not separately published; these three
verified merges are incorporated together without double counting.

The literal queue array `$.genes` has **235 objects and 235 distinct `gene`
values**, independently parsed from the identical
[queue blob 2a945cd59fc5](https://github.com/ai4curation/ai-gene-review/blob/e49cb9becb5bf0b3bcb307b23d8fa4a535c41536/projects/CLINGEN_MENDELIAN/publication-queue.json)
at tracker298's approved head, actual merge and this cutoff. The reviewer-reported
244 objects / 236 symbols is reproduced only by counting all six-space-indented
`gene` properties across the entire document. That includes nine historical
context fields outside `$.genes`: ATP1A1, ATP2B2, ATP6AP1 (three observations),
ATRX, BAP1, AKR1D1 and BRAF. BRAF is the additional distinct symbol. It is not
the array's cardinality; no queue object is added or removed to fit that count.
The appended machine evidence records the exact extra JSON paths and baseline
hash. This clarification preserves all prior records.

All 2,876 catalog rows and association text, all 235 historical queue objects,
all 49 prior completion updates and all previous progress text are preserved.
Only the CEP57, CEP85L and CFAP221 checkboxes change; update 50 is appended.
Both queue mirrors remain identical. Biological DRAFT status or justified
UNDECIDED annotations alone create no hold. Later work remains outside this
fixed completion cutoff. The first unchecked gene in literal catalog order
remains ACBD5.

Authenticated evidence was read and this proposal recorded at 2026-10-10 08:06:48 UTC.

[Checkpoint 301 session history](https://github.com/ai4curation/ai-gene-review/blob/main/history/projects/CLINGEN_MENDELIAN/2026-10-10T081738Z-codex-0d3c8d.yaml).

## Completion checkpoint 298 — 2026-10-10 07:02:47 UTC

**298 complete / 2,578 remaining in the frozen 2,876-gene catalog.** CEP290 and
CEP41 add two first counted primary campaign audits beyond checkpoint 296.
CEP290 is a substantive audit of a pre-existing review; CEP41 adds a new review.
Both count once as primary genes, irrespective of products or prior file
presence. No required follow-up holds remain. Supplementary products and
repeated reviews of already counted genes add no completion.

| Gene | PR | Final head | Approval | Merged UTC | Merge commit |
|---|---|---|---|---|---|
| CEP290 | [#4512](https://github.com/ai4curation/ai-gene-review/pull/4512) | [25047b2caee9](https://github.com/ai4curation/ai-gene-review/commit/25047b2caee9002dda126cb937ea97bbee050951) | [Approved](https://github.com/ai4curation/ai-gene-review/pull/4512#pullrequestreview-5477968533) | 2026-10-10T06:55:54Z | [5b6c5bc6df4d](https://github.com/ai4curation/ai-gene-review/commit/5b6c5bc6df4d274e22094cd1a65a6901664a56e5) |
| CEP41 | [#4513](https://github.com/ai4curation/ai-gene-review/pull/4513) | [08986810564b](https://github.com/ai4curation/ai-gene-review/commit/08986810564bdc47042342c994b8ef8b959c30b3) | [Approved](https://github.com/ai4curation/ai-gene-review/pull/4513#pullrequestreview-5477997606) | 2026-10-10T07:02:47Z | [3fbffb264074](https://github.com/ai4curation/ai-gene-review/commit/3fbffb26407414459e21ed806ebfa28885e8d809) |

CEP290's exact head was approved at 06:34:44 UTC; test (3.12) succeeded at 06:53:29 UTC; claude-review succeeded at 06:34:59 UTC, before its 06:55:54 UTC merge.
CEP41's exact head was approved at 06:43:40 UTC; test (3.12) succeeded at 07:01:34 UTC; claude-review succeeded at 06:44:21 UTC, before its 07:02:47 UTC merge.

Authenticated live records contain zero unresolved review threads. All eight
CEP290 and 15 CEP41 changed PR paths have identical approved-head and actual
merge-tree blobs. Their complete gene-directory trees also match their final
heads, actual merges and this frozen cutoff (8 CEP290 and 6 CEP41 entries).
The baseline tracker296 head, approval, required checks, merge and all changed
paths were independently verified.

The source snapshot is [commit 156c3de28880](https://github.com/ai4curation/ai-gene-review/commit/156c3de288803dcf20e18b312d20f64f59f7f845),
the actual [tracker296 #4515](https://github.com/ai4curation/ai-gene-review/pull/4515)
merge at 2026-10-10T06:51:33Z. Four source files and two derived-page preimages
are authenticated at that snapshot and are unchanged at the later CEP41
completion cutoff. The eventual publication branch base is separate: if it is
later, all six preimages must match and that base must be recorded. No future
branch identity or subsequent completion is assumed.

The counter definitions established at checkpoint 288 remain in force:
`campaign_audited_merged` counts distinct frozen-catalog primary genes with a
merged campaign review; subtracting `pending_followups` gives `completed`.
`original_merged` remains the compatibility alias in this appended snapshot.
The three applicable values are 298, 0 and 298. Existing review-file presence,
supplementary products and repeated reviews do not independently add campaign
completions. No separate checkpoint297 is published; the two verified merges
are incorporated together without double counting.

All 2,876 catalog rows and association text, all 235 historical queue entries,
all 48 prior completion updates and all previous progress text are preserved.
Only the CEP290 and CEP41 checkboxes change; update 49 is appended. The queue
gene array remains unchanged. Biological DRAFT status or justified UNDECIDED
annotations alone create no hold. CEP57, CEP85L and later work remain outside
this fixed completion cutoff. The first unchecked gene in literal catalog
order remains ACBD5.

Authenticated evidence was read and this proposal recorded at 2026-10-10 07:07:28 UTC.

[Checkpoint 298 session history](https://github.com/ai4curation/ai-gene-review/blob/main/history/projects/CLINGEN_MENDELIAN/2026-10-10T072443Z-codex-55f359.yaml).

## Completion checkpoint 296 — 2026-10-10 06:07:16 UTC

**296 complete / 2,580 remaining in the frozen 2,876-gene catalog.** CEP164 and
CEP250 add two first counted primary campaign audits beyond checkpoint 294.
CEP164 is a substantive audit of a pre-existing review; CEP250 adds a new review
file. Both count once as primary genes, irrespective of products or prior file
presence. No required follow-up holds remain. Supplementary products and
repeated reviews of already counted genes add no completion.

| Gene | PR | Final head | Approval | Merged UTC | Merge commit |
|---|---|---|---|---|---|
| CEP164 | [#4508](https://github.com/ai4curation/ai-gene-review/pull/4508) | [f596d88e3b5c](https://github.com/ai4curation/ai-gene-review/commit/f596d88e3b5cc14bf41331a4f3c670b11fa5c77b) | [Approved](https://github.com/ai4curation/ai-gene-review/pull/4508#pullrequestreview-5477762192) | 2026-10-10T05:43:15Z | [88a6b9a1b7e9](https://github.com/ai4curation/ai-gene-review/commit/88a6b9a1b7e9b800c1e00a0879389ea38659587d) |
| CEP250 | [#4510](https://github.com/ai4curation/ai-gene-review/pull/4510) | [02a91a83f87b](https://github.com/ai4curation/ai-gene-review/commit/02a91a83f87beac809b56a549668ab6db18bbf87) | [Approved](https://github.com/ai4curation/ai-gene-review/pull/4510#pullrequestreview-5477819434) | 2026-10-10T06:07:16Z | [88df55227943](https://github.com/ai4curation/ai-gene-review/commit/88df552279432a342e5928b8edb0290745e2776b) |

CEP164's exact head was approved at 05:20:31 UTC, with successful claude-review
at 05:20:48 UTC and test (3.12) at 05:40:08 UTC, before its 05:43:15 UTC merge.
CEP250's exact head was approved at 05:43:02 UTC, with successful claude-review
at 05:43:33 UTC and test (3.12) at 06:06:00 UTC, before its 06:07:16 UTC merge.
Captured pre-merge and independent live records contain zero unresolved review
threads. All eight CEP164 and all 24 CEP250 changed PR paths have identical
approved-head blobs and blobs at their respective merge-commit trees. The
eight CEP164 and six CEP250 gene artifacts also match their approved heads,
the frozen cutoff and the authenticated source snapshot.

The source snapshot is [commit f5d0abbae8a1](https://github.com/ai4curation/ai-gene-review/commit/f5d0abbae8a1e96993f4814b86c88194e743a09e),
the actual [tracker294 #4514](https://github.com/ai4curation/ai-gene-review/pull/4514)
merge at 2026-10-10T06:14:26Z. Its exact approved head and successful required
checks were independently verified. This later snapshot supplies the published
294 baseline without advancing the earlier CEP250 completion cutoff.
The eventual publication branch base is a separate fact. Four source-file and
two derived-page preimages are authenticated at this snapshot; if publication
uses a later base, all six must be checked identical and that base recorded in
the publication receipt. No future branch identity is assumed here.

The counter definitions established at checkpoint 288 remain in force:
`campaign_audited_merged` counts distinct frozen-catalog primary genes with a
merged campaign review; subtracting `pending_followups` gives `completed`.
`original_merged` remains the compatibility alias in this appended snapshot.
The three applicable values are 296, 0 and 296. Existing review-file presence,
supplementary products and repeated reviews do not independently add campaign
completions. A separate checkpoint295 was not published; its preliminary CEP164
evidence is incorporated into this two-gene checkpoint without double counting.

All 2,876 catalog rows and association text, all 235 historical queue entries,
all 47 prior completion updates and all previous progress text are preserved.
Only the CEP164 and CEP250 checkboxes change; update 48 is appended. The queue
gene array remains unchanged. Biological DRAFT status or justified UNDECIDED
annotations alone create no hold. CEP290, CEP41, CEP57 and later work remain
outside this fixed completion cutoff. The first unchecked gene in literal
catalog order remains ACBD5.

Authenticated evidence was read and this proposal recorded at 2026-10-10 06:17:06 UTC.

[Checkpoint 296 session history](https://github.com/ai4curation/ai-gene-review/blob/main/history/projects/CLINGEN_MENDELIAN/2026-10-10T062653Z-codex-fb098d.yaml).

## Completion checkpoint 294 — 2026-10-10 05:23:30 UTC

**294 complete / 2,582 remaining in the frozen 2,876-gene catalog.** CEP152 adds
one first counted primary campaign audit beyond checkpoint 293. Its review file
already existed; this completion records the substantive current-rule audit,
not another count for that earlier file. No required follow-up holds remain.
Supplementary products and repeated reviews of already counted genes add no
completion.

| Gene | PR | Final head | Approval | Merged UTC | Merge commit |
|---|---|---|---|---|---|
| CEP152 | [#4507](https://github.com/ai4curation/ai-gene-review/pull/4507) | [0692518e68c0](https://github.com/ai4curation/ai-gene-review/commit/0692518e68c0b54775e5acc8a648546437e63ae4) | [Approved](https://github.com/ai4curation/ai-gene-review/pull/4507#pullrequestreview-5477671213) | 2026-10-10T05:23:30Z | [0762762ef0ee](https://github.com/ai4curation/ai-gene-review/commit/0762762ef0eec9d013ac7979de66f9ab3a69f185) |

The final head was approved at 04:55:42 UTC, with successful claude-review at
04:56:19 UTC and test (3.12) at 05:17:22 UTC, all before the 05:23:30 UTC merge.
The captured pre-merge and independent live records contain zero unresolved
review threads. All seven changed PR paths have identical approved-head blobs
and blobs at the merge-commit tree. All seven gene artifacts also match the
frozen cutoff and the source main.

The source main is [commit b8e2b0a8753f](https://github.com/ai4curation/ai-gene-review/commit/b8e2b0a8753f9d3f08bfbd0d95a64e802bad7501),
which contains the gene merge and the later baseline tracker merge.
The published baseline [tracker #4511](https://github.com/ai4curation/ai-gene-review/pull/4511)
merged at 2026-10-10T05:38:06Z as [b8e2b0a8753f](https://github.com/ai4curation/ai-gene-review/commit/b8e2b0a8753f9d3f08bfbd0d95a64e802bad7501).
The later source snapshot does not move the biological completion cutoff.

The counter definitions established at checkpoint 288 remain in force:
`campaign_audited_merged` counts distinct frozen-catalog primary genes with a
merged campaign review; subtracting `pending_followups` gives `completed`.
`original_merged` remains a compatibility alias in this new snapshot. The three
applicable values are 294, 0 and 294. Existing review-file presence, supplementary
products and repeated reviews do not independently add campaign completions.

All 2,876 catalog rows and association text, all 235 historical queue entries,
all 46 prior completion updates and all previous progress text are preserved.
Only the CEP152 checkbox changes; update 47 is appended. The queue gene array
remains unchanged; new completion evidence is appended to the update series.
Biological DRAFT status or justified UNDECIDED annotations alone create no hold.
CEP164 #4508, CEP250 #4510, CEP290 and later work are outside this fixed
cutoff. The primary CEP152 review file was modified by its PR. The first unchecked
gene in literal catalog order remains ACBD5.

Authenticated evidence was read and this proposal recorded at 2026-10-10 05:40:57 UTC.

[Checkpoint 294 session history](https://github.com/ai4curation/ai-gene-review/blob/main/history/projects/CLINGEN_MENDELIAN/2026-10-10T054945Z-codex-7014b6.yaml).

## Completion checkpoint 293 — 2026-10-10 04:52:48 UTC

**293 complete / 2,583 remaining in the frozen 2,876-gene catalog.** CEP120 adds
one first primary campaign completion beyond checkpoint 292. No required
follow-up holds remain. Supplementary products and repeated reviews of already
counted genes add no completion.

| Gene | PR | Final head | Approval | Merged UTC | Merge commit |
|---|---|---|---|---|---|
| CEP120 | [#4505](https://github.com/ai4curation/ai-gene-review/pull/4505) | [cef801e8b875](https://github.com/ai4curation/ai-gene-review/commit/cef801e8b8754c4bc7afc7fe63680a9e3bc97c2f) | [Approved](https://github.com/ai4curation/ai-gene-review/pull/4505#pullrequestreview-5477575495) | 2026-10-10T04:52:48Z | [6ae4685964aa](https://github.com/ai4curation/ai-gene-review/commit/6ae4685964aa1aae16bfec2647cab2ccfed750f6) |

The final head has successful test (3.12) and claude-review checks on that same
commit before merge. All 17 changed PR paths match their approved-head and merge
blobs; all six gene artifacts also match the frozen cutoff and source.
The source main is [commit ea02a3dc102c](https://github.com/ai4curation/ai-gene-review/commit/ea02a3dc102c093a1a5e34359f3800a4ee83195b),
which contains the gene merge and the later baseline tracker merge.
The published baseline [tracker #4509](https://github.com/ai4curation/ai-gene-review/pull/4509)
merged at 2026-10-10T05:09:12Z as [ea02a3dc102c](https://github.com/ai4curation/ai-gene-review/commit/ea02a3dc102c093a1a5e34359f3800a4ee83195b).
The later source snapshot does not move the biological completion cutoff.

The counter definitions established at checkpoint 288 remain in force:
`campaign_audited_merged` counts distinct frozen-catalog primary genes with a
merged campaign review; subtracting `pending_followups` gives `completed`.
`original_merged` remains a compatibility alias in this new snapshot. The three
applicable values are 293, 0 and 293. Existing review-file presence, supplementary
products and repeated reviews do not independently add campaign completions.

All 2,876 catalog rows and association text, all 235 historical queue entries,
all 45 prior completion updates and all previous progress text are preserved.
Only the CEP120 checkbox changes; update 46 is appended. The queue gene array
remains unchanged; new completion evidence is appended to the update series.
Biological DRAFT status or justified UNDECIDED annotations alone create no hold.
CEP152 #4507, CEP164 #4508, CEP250 #4510 and later work are outside this fixed
cutoff. The primary CEP120 review file was added by its PR. The first unchecked
gene in literal catalog order remains ACBD5.

Authenticated evidence was read and this proposal recorded at 2026-10-10 05:14:24 UTC.

[Checkpoint 293 session history](https://github.com/ai4curation/ai-gene-review/blob/main/history/projects/CLINGEN_MENDELIAN/2026-10-10T051833Z-codex-2fb312.yaml).

## Completion checkpoint 292 — 2026-10-10 04:42:08 UTC

**292 complete / 2,584 remaining in the frozen 2,876-gene catalog.** CEBPA and
CEP104 add two first primary campaign completions beyond checkpoint 290. No
required follow-up holds remain. Supplementary products and repeated reviews of
already counted genes add no completion.

| Gene | PR | Final head | Approval | Merged UTC | Merge commit |
|---|---|---|---|---|---|
| CEBPA | [#4502](https://github.com/ai4curation/ai-gene-review/pull/4502) | [8dcb615dc28f](https://github.com/ai4curation/ai-gene-review/commit/8dcb615dc28f7b2d8804048166fc8063d857f0f8) | [Approved](https://github.com/ai4curation/ai-gene-review/pull/4502#pullrequestreview-5477523334) | 2026-10-10T04:34:29Z | [074caa8e219a](https://github.com/ai4curation/ai-gene-review/commit/074caa8e219a6301d749afeb84571006f4b9d650) |
| CEP104 | [#4503](https://github.com/ai4curation/ai-gene-review/pull/4503) | [cbd9e3d57ea9](https://github.com/ai4curation/ai-gene-review/commit/cbd9e3d57ea95efb19807ad8a8cfc64fc81d47d6) | [Approved](https://github.com/ai4curation/ai-gene-review/pull/4503#pullrequestreview-5477553863) | 2026-10-10T04:42:08Z | [04685e86ca43](https://github.com/ai4curation/ai-gene-review/commit/04685e86ca438d813fae98a3ac8e507cb32838e5) |

Both final heads have successful test (3.12) and claude-review checks on those
same commits before merge. All 50 changed PR paths match their approved-head and
merge blobs; all 16 gene artifacts also match the frozen cutoff and source.
The source main is [commit 2b6a4561b112](https://github.com/ai4curation/ai-gene-review/commit/2b6a4561b112799f115b70c8fdbf46494a1fb143),
which contains both gene merges and the later baseline tracker merge.
The published baseline [tracker #4506](https://github.com/ai4curation/ai-gene-review/pull/4506)
merged at 2026-10-10T04:42:51Z as [2b6a4561b112](https://github.com/ai4curation/ai-gene-review/commit/2b6a4561b112799f115b70c8fdbf46494a1fb143).
The later source snapshot does not move the biological completion cutoff.

The counter definitions established at checkpoint 288 remain in force:
`campaign_audited_merged` counts distinct frozen-catalog primary genes with a
merged campaign review; subtracting `pending_followups` gives `completed`.
`original_merged` remains a compatibility alias in this new snapshot. The three
applicable values are 292, 0 and 292. Existing review-file presence, supplementary
products and repeated reviews do not independently add campaign completions.

All 2,876 catalog rows and association text, all 235 historical queue entries,
all 44 prior completion updates and all previous progress text are preserved.
Only the CEBPA and CEP104 checkboxes change; update 45 is appended. The queue gene
array remains unchanged; new completion evidence is appended to the update series.
Biological DRAFT status or justified UNDECIDED annotations alone create no hold.
CEP120 #4505, CEP152 #4507, CEP164 #4508 and later work are outside this fixed cutoff.
Both primary review files were added by their respective PRs. The first unchecked
gene in literal catalog order remains ACBD5.

For the previously counted CDKN2A gene, the separately rendered
[ARF product review](https://ai4curation.io/ai-gene-review/genes/human/CDKN2A__Q8N726/CDKN2A__Q8N726-ai-review.html)
and [p16 product review](https://ai4curation.io/ai-gene-review/genes/human/CDKN2A/CDKN2A-ai-review.html)
are both available. These two products still contribute one CDKN2A catalog completion.

Authenticated evidence was read and this proposal recorded at 2026-10-10T04:45:58.760797+00:00.

[Checkpoint 292 session history](https://github.com/ai4curation/ai-gene-review/blob/main/history/projects/CLINGEN_MENDELIAN/2026-10-10T044658Z-codex-7ed45f.yaml).

## Completion checkpoint 290 — 2026-10-10 04:04:04 UTC

**290 complete / 2,586 remaining in the frozen 2,876-gene catalog.** CDKN2A adds
one first primary campaign completion beyond checkpoint 289. No required
follow-up holds remain. Supplementary products and repeated reviews of already
counted genes add no completion.

| Gene | PR | Final head | Approval | Merged UTC | Merge commit |
|---|---|---|---|---|---|
| CDKN2A | [#4499](https://github.com/ai4curation/ai-gene-review/pull/4499) | [4841d73f6c01](https://github.com/ai4curation/ai-gene-review/commit/4841d73f6c011b08e33f2adbf4b3f3e74ac0e1d1) | [Approved](https://github.com/ai4curation/ai-gene-review/pull/4499#pullrequestreview-5477410622) | 2026-10-10T04:04:04Z | [ebb4123eeb1e](https://github.com/ai4curation/ai-gene-review/commit/ebb4123eeb1e0ec6bf1a8ccf6bf5bacb483e7368) |

The final head has successful test (3.12) and claude-review checks on that same
commit before merge. All 66 changed PR paths match their approved-head and merge
blobs; all 19 gene artifacts also match the frozen source/cutoff. The source main
is [commit 498c72e4bea4](https://github.com/ai4curation/ai-gene-review/commit/498c72e4bea435fe5f11cd82010fe5024c3dd791),
which contains both the CDKN2A merge at 2026-10-10T04:04:04Z and the later baseline tracker merge.
The published baseline [tracker #4504](https://github.com/ai4curation/ai-gene-review/pull/4504)
merged at 2026-10-10T04:06:05Z as [498c72e4bea4](https://github.com/ai4curation/ai-gene-review/commit/498c72e4bea435fe5f11cd82010fe5024c3dd791).
The later source snapshot does not move the biological completion cutoff.

The counter definitions established at checkpoint 288 remain in force:
`campaign_audited_merged` counts distinct frozen-catalog primary genes with a
merged campaign review; subtracting `pending_followups` gives `completed`.
`original_merged` remains a compatibility alias in this new snapshot. The three
applicable values are 290, 0 and 290. Existing review-file presence, supplementary
products and repeated reviews do not independently add campaign completions.

All 2,876 catalog rows and association text, all 235 actual historical queue
entries, all 43 prior completion updates and all previous progress text are
preserved. Only CDKN2A's checkbox changes; update 44 is appended. The queue gene
array remains unchanged; new completion evidence is appended to the update series.
Biological DRAFT status or justified UNDECIDED annotations alone create no hold.
CEBPA #4502, CEP104 #4503, CEP120 #4505, CEP152 and later work are outside this fixed cutoff.
The P42771 p16 and Q8N726 ARF reviews together count as one CDKN2A catalog completion, not two products.
The primary review file was added by #4499; this is its first counted campaign review. The first unchecked
gene in literal catalog order remains ACBD5.

Authenticated evidence was read and this proposal recorded at 2026-10-10T04:11:20.175487+00:00.

[Checkpoint 290 session history](https://github.com/ai4curation/ai-gene-review/blob/main/history/projects/CLINGEN_MENDELIAN/2026-10-10T041722Z-codex-cbea44.yaml).

## Completion checkpoint 289 — 2026-10-10 03:28:19 UTC

**289 complete / 2,587 remaining in the frozen 2,876-gene catalog.** CDT1 adds
one first primary campaign completion beyond checkpoint 288. No required
follow-up holds remain. Supplementary products and repeated reviews of already
counted genes add no completion.

| Gene | PR | Final head | Approval | Merged UTC | Merge commit |
|---|---|---|---|---|---|
| CDT1 | [#4500](https://github.com/ai4curation/ai-gene-review/pull/4500) | [84bf468a05a4](https://github.com/ai4curation/ai-gene-review/commit/84bf468a05a4df293c4ba6968529ec9171ad2b51) | [Approved](https://github.com/ai4curation/ai-gene-review/pull/4500#pullrequestreview-5477289703) | 2026-10-10T03:28:19Z | [7a6b71b1a228](https://github.com/ai4curation/ai-gene-review/commit/7a6b71b1a2286c223dcc0336b1334e716972016f) |

The final head has successful test (3.12) and claude-review checks on that same
commit before merge. All 27 changed PR paths match their approved-head and merge
blobs; all six gene artifacts also match the frozen source/cutoff. The source main
is [commit 7a6b71b1a228](https://github.com/ai4curation/ai-gene-review/commit/7a6b71b1a2286c223dcc0336b1334e716972016f),
the CDT1 merge at 2026-10-10T03:28:19Z. The published baseline [tracker #4501](https://github.com/ai4curation/ai-gene-review/pull/4501)
merged as [9dfaa0a45aed](https://github.com/ai4curation/ai-gene-review/commit/9dfaa0a45aedac6184dd4d0419de92c524e7683c).

The counter definitions established at checkpoint 288 remain in force:
`campaign_audited_merged` counts distinct frozen-catalog primary genes with a
merged campaign review; subtracting `pending_followups` gives `completed`.
`original_merged` remains a compatibility alias in this new snapshot. The three
applicable values are 289, 0 and 289. Existing review-file presence, supplementary
products and repeated reviews do not independently add campaign completions.

All 2,876 catalog rows and association text, all 235 actual historical queue
entries, all 42 prior completion updates and all previous progress text are
preserved. Only CDT1's checkbox changes; update 43 is appended. The queue gene
array remains unchanged; new completion evidence is appended to the update series.
Biological DRAFT status or justified UNDECIDED annotations alone create no hold.
CDKN2A, CEBPA and later merges are outside this fixed cutoff. The first unchecked
gene in literal catalog order remains ACBD5.

Authenticated evidence was read and this proposal recorded at 2026-10-10T03:33:18.439324+00:00.

[Checkpoint 289 session history](https://github.com/ai4curation/ai-gene-review/blob/main/history/projects/CLINGEN_MENDELIAN/2026-10-10T034138Z-codex-80263b.yaml).

## Completion checkpoint 288 — 2026-10-10 02:29:14 UTC

**288 complete / 2,588 remaining in the frozen 2,876-gene catalog.** CDKL5 and
the substantive CDKN1C audit add two distinct primary campaign completions beyond
checkpoint 286. No required follow-up holds remain. Supplementary products and
repeat reviews of already counted genes add no completion.

| Gene | PR | Final head | Approval | Merged UTC | Merge commit |
|---|---|---|---|---|---|
| CDKL5 | [#4494](https://github.com/ai4curation/ai-gene-review/pull/4494) | [cbc605964281](https://github.com/ai4curation/ai-gene-review/commit/cbc605964281ee0f2a0a87ac0305cc046529fccf) | [Approved](https://github.com/ai4curation/ai-gene-review/pull/4494#pullrequestreview-5476993578) | 2026-10-10T02:06:16Z | [e2c5e7f01a9f](https://github.com/ai4curation/ai-gene-review/commit/e2c5e7f01a9f1af595ca96c475b1e75b49e07d88) |
| CDKN1C | [#4497](https://github.com/ai4curation/ai-gene-review/pull/4497) | [79c234184757](https://github.com/ai4curation/ai-gene-review/commit/79c2341847573828a3d62f1a82b849c38974f292) | [Approved](https://github.com/ai4curation/ai-gene-review/pull/4497#pullrequestreview-5477035318) | 2026-10-10T02:29:14Z | [e94991ceada8](https://github.com/ai4curation/ai-gene-review/commit/e94991ceada8507158f48e9902087033919dd36b) |

Both final heads have successful test (3.12) and claude-review checks on the same
commit before the merge. All 35 changed PR paths match their approved-head and
merge blobs; all 10 gene artifacts additionally match the fixed source/cutoff.
The [source main e94991ceada8](https://github.com/ai4curation/ai-gene-review/commit/e94991ceada8507158f48e9902087033919dd36b)
is the CDKN1C merge at 2026-10-10T02:29:14Z; the baseline [tracker #4498](https://github.com/ai4curation/ai-gene-review/pull/4498)
merged as [eb43e5708cf3](https://github.com/ai4curation/ai-gene-review/commit/eb43e5708cf3cfa98472b2bffb6a38e6a4ef1c5c) at 2026-10-10T02:25:25Z.

The new `campaign_audited_merged` counter counts distinct frozen-catalog primary
genes with a merged campaign review, including any counted gene awaiting a
required follow-up; subtracting `pending_followups` gives `completed`. At this
cutoff all three applicable values are 288, 0 and 288. A substantive first
campaign audit of an existing review qualifies; creating a review file is not
the criterion. CDKN1C modifies an existing review, while CDKL5 adds one.

The legacy `original_merged` key and `distinct_original_increment` are retained
as compatibility fields in this new snapshot with that campaign scope. Their
names must not be read as a census of first-ever review-file merges. This is an
append-only clarification; it does not silently rewrite older records or assert
that every historical use of the old label was unambiguous.

The bounded audit of the published 41-update series found that every prior
`original_merged` equals `completed + pending_followups`. CDKN1B is unchecked
in the authenticated checkpoint-283 project and checked at checkpoint 286;
its first named completion entry is update 41, and it is absent from the 235
historical queue entries. An older CDKN1B review-file merge does not establish
that it was included in an earlier campaign count. No count is reduced on that
unsupported premise. This audit does not reconstruct every historical repository
review merge or change the authoritative checkbox count.

All 2,876 catalog rows and their association text, all 235 historical queue
entries, all 41 prior completion updates and all previous progress text remain
unchanged. Only CDKL5 and CDKN1C checkboxes change; update 42 is appended.
Biological DRAFT status or justified UNDECIDED annotations alone create no hold.
CDKN2A, CDT1 and later merges are outside this fixed cutoff. The first unchecked
gene in literal catalog order remains ACBD5.
Authenticated evidence was read and this proposal recorded at 2026-10-10T02:40:24.759913+00:00.

[Checkpoint 288 session history](https://github.com/ai4curation/ai-gene-review/blob/main/history/projects/CLINGEN_MENDELIAN/2026-10-10T024556Z-codex-38e3b8.yaml).

## Completion checkpoint 286 — 2026-10-10 01:50:04 UTC

**286 complete / 2,590 remaining in the frozen 2,876-gene catalog.** Three distinct
primary-gene campaign reviews add three originals and completions beyond checkpoint 283.
No follow-up holds remain. Supplementary genes and repeat reviews add no count.

| Gene | PR | Final head | Approval | Merged UTC | Merge commit |
|---|---|---|---|---|---|
| CDHR1 | [#4491](https://github.com/ai4curation/ai-gene-review/pull/4491) | [7d4210d5a86e](https://github.com/ai4curation/ai-gene-review/commit/7d4210d5a86e322821a50cc0e113469e970f1638) | [Approved](https://github.com/ai4curation/ai-gene-review/pull/4491#pullrequestreview-5476772148) | 2026-10-10T01:27:47Z | [3eb71be1db01](https://github.com/ai4curation/ai-gene-review/commit/3eb71be1db01bd2aca493de7984aa9484aaa66ef) |
| CDK13 | [#4492](https://github.com/ai4curation/ai-gene-review/pull/4492) | [b26f957911df](https://github.com/ai4curation/ai-gene-review/commit/b26f957911dfaf5a7d5f5110629c21a6c808708c) | [Approved](https://github.com/ai4curation/ai-gene-review/pull/4492#pullrequestreview-5476861498) | 2026-10-10T01:49:55Z | [407f9f331915](https://github.com/ai4curation/ai-gene-review/commit/407f9f3319152f2254114de8df7ca48d50756491) |
| CDKN1B | [#4495](https://github.com/ai4curation/ai-gene-review/pull/4495) | [341379300d25](https://github.com/ai4curation/ai-gene-review/commit/341379300d25c2c0741135eaff0b4a004444ef22) | [Approved](https://github.com/ai4curation/ai-gene-review/pull/4495#pullrequestreview-5476913459) | 2026-10-10T01:50:04Z | [faaaf56614b1](https://github.com/ai4curation/ai-gene-review/commit/faaaf56614b1d6e317b6f7ff25629bb166b7ba90) |

Each approval belongs to its listed final head. Both test (3.12) and claude-review
succeeded on that same commit before merge, verified through check-suite commit IDs.
All 38 changed PR paths match approved heads and merge commits. All 17 gene artifacts
match both the fixed cutoff and later source main. CDKN1B receives its first campaign
completion after a substantive audit; its preexisting COMPLETE status did not close
the campaign task. Biological DRAFT status and justified UNDECIDED annotations do
not themselves create completion holds.

The completion cutoff is [faaaf56614b1](https://github.com/ai4curation/ai-gene-review/commit/faaaf56614b1d6e317b6f7ff25629bb166b7ba90) at 2026-10-10T01:50:04Z.
The later [source main snapshot 4d4eedf35ac6](https://github.com/ai4curation/ai-gene-review/commit/4d4eedf35ac645f2ec5899f6665ed0b968156edf)
contains these gene merges and [tracker PR #4496](https://github.com/ai4curation/ai-gene-review/pull/4496),
which published checkpoint 283. Its later source-capture time does not add gene completions.
Authenticated evidence was read and this proposal recorded at 2026-10-10T01:53:45.247199+00:00.

All 2,876 catalog rows and association text, all 235 historical queue entries,
all 40 earlier completion updates and every prior dated progress section are preserved.
Only the three named primary checkboxes change, and a 41st completion update is appended.
Older dated observations remain historical. CDKL5, CDKN1C and CDKN2A are outside
this checkpoint regardless of later PR changes. The first unchecked gene in literal
catalog order remains ACBD5.

[Checkpoint 286 session history](https://github.com/ai4curation/ai-gene-review/blob/main/history/projects/CLINGEN_MENDELIAN/2026-10-10T015708Z-codex-be4d78.yaml).

## Completion checkpoint 283 — 2026-10-10 01:04:37 UTC

**283 complete / 2,593 remaining in the frozen 2,876-gene catalog.** Five distinct
primary-gene campaign reviews add five originals and completions beyond checkpoint 278.
No follow-up holds remain. Supplementary genes and repeat reviews add no count.

| Gene | PR | Final head | Approval | Merged UTC | Merge commit |
|---|---|---|---|---|---|
| CDH11 | [#4486](https://github.com/ai4curation/ai-gene-review/pull/4486) | [36084b8f8c3b](https://github.com/ai4curation/ai-gene-review/commit/36084b8f8c3bf747a2c3be6e326a7e9628bbd789) | [Approved](https://github.com/ai4curation/ai-gene-review/pull/4486#pullrequestreview-5476563602) | 2026-10-10T00:52:07Z | [dccca414ec3a](https://github.com/ai4curation/ai-gene-review/commit/dccca414ec3aee49285c02d4cae8ec4498bcb7a9) |
| CDH2 | [#4485](https://github.com/ai4curation/ai-gene-review/pull/4485) | [b94cb3bb39bd](https://github.com/ai4curation/ai-gene-review/commit/b94cb3bb39bdbd6a0190da67efd6886a19f902c3) | [Approved](https://github.com/ai4curation/ai-gene-review/pull/4485#pullrequestreview-5476598449) | 2026-10-10T00:52:57Z | [936cc03bfaa4](https://github.com/ai4curation/ai-gene-review/commit/936cc03bfaa4ad2017482fba735adedaf1dab770) |
| CDH23 | [#4488](https://github.com/ai4curation/ai-gene-review/pull/4488) | [597e5068026d](https://github.com/ai4curation/ai-gene-review/commit/597e5068026d4d22551d7ce39be23180218df3bf) | [Approved](https://github.com/ai4curation/ai-gene-review/pull/4488#pullrequestreview-5476612754) | 2026-10-10T00:55:59Z | [f7075527f6e4](https://github.com/ai4curation/ai-gene-review/commit/f7075527f6e4dc11a19f2d621b82090b44806de3) |
| CDH3 | [#4490](https://github.com/ai4curation/ai-gene-review/pull/4490) | [93e90cb9f65a](https://github.com/ai4curation/ai-gene-review/commit/93e90cb9f65aad5bce033015ebf12cc418a13fb7) | [Approved](https://github.com/ai4curation/ai-gene-review/pull/4490#pullrequestreview-5476668634) | 2026-10-10T01:01:23Z | [70c867e88cd2](https://github.com/ai4curation/ai-gene-review/commit/70c867e88cd267242f4f3beffdb9c8c91b90310b) |
| CDH1 | [#4489](https://github.com/ai4curation/ai-gene-review/pull/4489) | [f09ac48d6dc1](https://github.com/ai4curation/ai-gene-review/commit/f09ac48d6dc12daab564213cc04dfa0a961c8203) | [Approved](https://github.com/ai4curation/ai-gene-review/pull/4489#pullrequestreview-5476714977) | 2026-10-10T01:04:37Z | [436d15327509](https://github.com/ai4curation/ai-gene-review/commit/436d15327509f7aa96cb41ba0c63ec35db1d9ed4) |

Each approval belongs to its listed final head. Both test (3.12) and claude-review
succeeded on that same commit before merge, verified through check-suite commit IDs.
All 85 changed PR paths match approved heads and merge commits. All 26 gene artifacts
match the fixed CDH1 cutoff commit. These checks preserve the accepted reviews
without reopening their scientific decisions. Biological DRAFT status and justified
UNDECIDED annotations do not themselves create completion holds.

The completion cutoff is [436d15327509](https://github.com/ai4curation/ai-gene-review/commit/436d15327509f7aa96cb41ba0c63ec35db1d9ed4) at 2026-10-10T01:04:37Z.
The later [source main snapshot ffaf00ab93d4](https://github.com/ai4curation/ai-gene-review/commit/ffaf00ab93d40e5fe2e71b283ac42f10ffb22d2f)
contains these gene merges and [tracker PR #4493](https://github.com/ai4curation/ai-gene-review/pull/4493),
which published checkpoint 278. Its later source-capture time does not add gene completions.
Authenticated evidence was read at 2026-10-10T01:21:45.219910+00:00.

All 2,876 catalog rows and association text, all 235 historical queue entries,
all 39 earlier completion updates and every prior dated progress section are preserved.
Only the five named primary checkboxes change, and a 40th completion update is appended.
Older dated observations remain historical; the cutoff excludes all later merges
and pending work. The first unchecked gene in literal catalog order remains ACBD5.

CDHR1, CDK13 and CDKL5 remain outside this checkpoint regardless of later PR changes.

[Checkpoint 283 session history](https://github.com/ai4curation/ai-gene-review/blob/main/history/projects/CLINGEN_MENDELIAN/2026-10-10T012544Z-codex-10fc5a.yaml).

## Completion checkpoint 278 — 2026-10-10 00:09:16 UTC

**278 complete / 2,598 remaining in the frozen 2,876-gene catalog.** This adds
CDC42 and CDC73 beyond [published checkpoint 276](https://github.com/ai4curation/ai-gene-review/pull/4487).
The completion cutoff is the CDC73 merge, not the later source-capture time.

| Gene | PR | Final head | Approval | Merged UTC | Merge commit |
|---|---|---|---|---|---|
| CDC42 | [#4468](https://github.com/ai4curation/ai-gene-review/pull/4468) | [49587154183a](https://github.com/ai4curation/ai-gene-review/commit/49587154183abdb4845739169f77032bf444a59e) | [Approved](https://github.com/ai4curation/ai-gene-review/pull/4468#pullrequestreview-5476359898) | 2026-10-09T23:53:12Z | [765c0cfb2adf](https://github.com/ai4curation/ai-gene-review/commit/765c0cfb2adf5c68e72efd94c6435aab0bbf2712) |
| CDC73 | [#4474](https://github.com/ai4curation/ai-gene-review/pull/4474) | [9245b7b68999](https://github.com/ai4curation/ai-gene-review/commit/9245b7b6899958dd59f859107204b5c08dbc2000) | [Approved](https://github.com/ai4curation/ai-gene-review/pull/4474#pullrequestreview-5476400373) | 2026-10-10T00:09:16Z | [c488afbe915c](https://github.com/ai4curation/ai-gene-review/commit/c488afbe915c1b6b58ebf39c5820bb383f581910) |

Each approval belongs to the listed final head. The test (3.12) and claude-review
checks succeeded on that same commit before its actual merge time, verified
through check-suite commit IDs. All 102 changed PR paths match between approved
heads and merge commits. All 12 changed gene artifacts also match the cutoff
commit and the later fixed source-main snapshot. These checks preserve the
accepted scientific reviews; they do not reopen the genes or re-audit older completions.

**Two new original reviews, no holds:** both genes add one distinct primary
completion. The 276 prior originals and completions therefore become 278, with
zero pending completion holds. Only CDC42 and CDC73 primary checkboxes change.
Supplementary genes and repeat reviews add no completion. Biological DRAFT
status and justified UNDECIDED annotations do not themselves create a hold.

The completion cutoff is [c488afbe915c](https://github.com/ai4curation/ai-gene-review/commit/c488afbe915c1b6b58ebf39c5820bb383f581910) at 2026-10-10T00:09:16Z.
The later [source main snapshot 10eda3330253](https://github.com/ai4curation/ai-gene-review/commit/10eda3330253be3140fe764020499de4f8ce8bf3)
contains both gene merges and the [baseline tracker #4487](https://github.com/ai4curation/ai-gene-review/pull/4487), which merged at 2026-10-10T00:46:18Z.
That tracker publishes the earlier 276 checkpoint; its later merge time does
not shift this checkpoint's gene-completion cutoff. Any other later merges or
open PRs remain outside these totals.
Fresh source evidence was read at 2026-10-10T00:47:44.008147+00:00.

All 2,876 catalog entries and association text, 235 historical queue entries,
38 prior completion updates, the cleared current source-hold list and every
earlier dated progress section remain preserved. One 39th update is appended.
Older counts and states remain dated observations, superseded for current
totals by this checkpoint. The first unchecked gene in literal catalog order
remains ACBD5.

[Checkpoint 278 session history](https://github.com/ai4curation/ai-gene-review/blob/main/history/projects/CLINGEN_MENDELIAN/2026-10-10T005709Z-codex-0ec475.yaml).

## Completion checkpoint 276 — 2026-10-09 23:33:32 UTC

**276 complete / 2,600 remaining in the frozen 2,876-gene catalog.** This adds
CDC45 and closes the AKR1D1 source hold beyond [published checkpoint 274](https://github.com/ai4curation/ai-gene-review/pull/4472).
The fixed [main snapshot 5c3a43a48ef7](https://github.com/ai4curation/ai-gene-review/commit/5c3a43a48ef70fac4f5438c17cd2989515e50865)
contains both contributing merges and the preceding tracker merge. Completion
evidence stops at the AKR1D1 follow-up merge at the stated cutoff.

| Gene | PR | Final head | Approval | Merged UTC | Merge commit |
|---|---|---|---|---|---|
| CDC45 | [#4470](https://github.com/ai4curation/ai-gene-review/pull/4470) | [6026f164dc69](https://github.com/ai4curation/ai-gene-review/commit/6026f164dc6914ea2c36d6a37412d75c52705e15) | [Approved](https://github.com/ai4curation/ai-gene-review/pull/4470#pullrequestreview-5474402152) | 2026-10-09T19:39:58Z | [64e6a5204644](https://github.com/ai4curation/ai-gene-review/commit/64e6a5204644adbf05385bffc595a5e696ec1a4b) |
| AKR1D1 | [#4465](https://github.com/ai4curation/ai-gene-review/pull/4465) | [5239e0fca43d](https://github.com/ai4curation/ai-gene-review/commit/5239e0fca43d641210daa8b2fd10fdab2e9757ca) | [Approved](https://github.com/ai4curation/ai-gene-review/pull/4465#pullrequestreview-5475471749) | 2026-10-09T23:33:32Z | [5c3a43a48ef7](https://github.com/ai4curation/ai-gene-review/commit/5c3a43a48ef70fac4f5438c17cd2989515e50865) |

Each approval belongs to the listed final head. The test (3.12) and claude-review
checks completed successfully on that same commit before its actual merge time,
verified using their check-suite commit IDs. All 35 changed PR paths have the
same Git blob at the approved head and merge commit. All nine changed gene
artifacts also match the fixed cutoff snapshot. These checks preserve the
result of the accepted scientific reviews rather than reopening them.

**The last hold closes without double-counting:** AKR1D1 was already among
the 275 original reviewed genes at checkpoint 274. Its [original review #3266](https://github.com/ai4curation/ai-gene-review/pull/3266)
and [prior follow-up #3941](https://github.com/ai4curation/ai-gene-review/pull/3941)
had merged while the Reactome:R-HSA-193755 source gate remained open. The
accepted archived-source recovery and supporting-evidence corrections now
merged in [#4465](https://github.com/ai4curation/ai-gene-review/pull/4465)
close that gate. This adds one completion and no second original-gene merge.

CDC45 adds one new original reviewed gene to the prior 275, giving **276**.
The AKR1D1 closure reduces the holds from one to zero, giving **276 complete**.
Only the CDC45 and AKR1D1 primary checkboxes change. Supplementary genes and
repeat reviews add no further completion. Biological DRAFT status and justified
UNDECIDED annotations remain independent of campaign closure.

Fresh remote evidence was read at 2026-10-09T23:38:49.211263+00:00. Merge times determine inclusion,
not the later observation time. Tracker #4472 merged at 2026-10-09T23:31:07Z
and supplies the published 274 baseline; its own earlier evidence cutoff
excluded CDC45. Later merges and open work are outside this checkpoint. The
first unchecked gene in literal catalog order remains ACBD5.

The project status, queue status and latest completion timestamp use this
checkpoint. All 235 historical queue entries, 37 prior completion updates and
earlier dated progress sections are preserved. Their older states and counts
remain dated observations, superseded for current totals by this section.

[Checkpoint 276 session history](https://github.com/ai4curation/ai-gene-review/blob/main/history/projects/CLINGEN_MENDELIAN/2026-10-09T235057Z-codex-dd0cc6.yaml).

## Completion checkpoint 274 — 2026-10-09 18:49:44 UTC

[Session history](https://github.com/ai4curation/ai-gene-review/blob/main/history/projects/CLINGEN_MENDELIAN/2026-10-09T190426Z-codex-a50c7e.yaml).

**274 complete / 2,602 remaining in the frozen 2,876-gene catalog.** This adds
four completions beyond [published checkpoint 270](https://github.com/ai4curation/ai-gene-review/pull/4467).
The fixed [main snapshot db510ed9a7ef](https://github.com/ai4curation/ai-gene-review/commit/db510ed9a7efdcb0cbf24a3d98be7f9b07898eb3)
contains all four gene/follow-up merges and the preceding tracker merge.
Completion evidence stops at the BCL10 follow-up merge at the stated cutoff.

| Gene | PR | Final head | Approval | Merged UTC | Merge commit |
|---|---|---|---|---|---|
| CDC14A | [#4463](https://github.com/ai4curation/ai-gene-review/pull/4463) | [38335fdf45db](https://github.com/ai4curation/ai-gene-review/commit/38335fdf45dbe22eab3af8e35651a63546e39a81) | [Approved](https://github.com/ai4curation/ai-gene-review/pull/4463#pullrequestreview-5473578312) | 2026-10-09T18:26:46Z | [c93df3ff8545](https://github.com/ai4curation/ai-gene-review/commit/c93df3ff85451116d0a0f729ecaffdf82d4f0c85) |
| BIN1 | [#4461](https://github.com/ai4curation/ai-gene-review/pull/4461) | [f2f8421ff73f](https://github.com/ai4curation/ai-gene-review/commit/f2f8421ff73fca4ae7001e66b35b03d69833bf8e) | [Approved](https://github.com/ai4curation/ai-gene-review/pull/4461#pullrequestreview-5473611058) | 2026-10-09T18:26:55Z | [9e7ccfbd0ad4](https://github.com/ai4curation/ai-gene-review/commit/9e7ccfbd0ad4c37dbe08d410077065c95fb96922) |
| BLM | [#4464](https://github.com/ai4curation/ai-gene-review/pull/4464) | [8bde66823a63](https://github.com/ai4curation/ai-gene-review/commit/8bde66823a63f71234c27b4c014cd42d3f37a671) | [Approved](https://github.com/ai4curation/ai-gene-review/pull/4464#pullrequestreview-5473679205) | 2026-10-09T18:27:02Z | [70a01c34741c](https://github.com/ai4curation/ai-gene-review/commit/70a01c34741ccf9644d9149196c8114a34ad84fe) |
| BCL10 | [#4458](https://github.com/ai4curation/ai-gene-review/pull/4458) | [0b2a5d48eb48](https://github.com/ai4curation/ai-gene-review/commit/0b2a5d48eb480afd3e3c207bcc2b219b4923d511) | [Approved](https://github.com/ai4curation/ai-gene-review/pull/4458#pullrequestreview-5473866657) | 2026-10-09T18:49:44Z | [db510ed9a7ef](https://github.com/ai4curation/ai-gene-review/commit/db510ed9a7efdcb0cbf24a3d98be7f9b07898eb3) |

Each approval belongs to the listed final head. The test (3.12) and claude-review
checks completed successfully on that same commit before its actual merge time,
verified using their check-suite commit IDs. All 43 changed PR paths have the
same Git blob at the approved head and merge commit. All 17 changed gene
artifacts also match the fixed cutoff snapshot. These checks do not substitute
for or re-open the already completed scientific reviews.

**Three holds close without double-counting original reviews:**

| Gene | Original review already counted | Original merge | Closing follow-up |
|---|---|---|---|
| BCL10 | [#3649](https://github.com/ai4curation/ai-gene-review/pull/3649) | [92de042a96a5](https://github.com/ai4curation/ai-gene-review/commit/92de042a96a53a6bbd036e6f910b1e0101e780ad) (2026-10-05T23:23:15Z) | [#4458](https://github.com/ai4curation/ai-gene-review/pull/4458) |
| BIN1 | [#3689](https://github.com/ai4curation/ai-gene-review/pull/3689) | [8446f4d12098](https://github.com/ai4curation/ai-gene-review/commit/8446f4d120987a9edded916ad5c85948c949581e) (2026-10-05T23:24:18Z) | [#4461](https://github.com/ai4curation/ai-gene-review/pull/4461) |
| BLM | [#3706](https://github.com/ai4curation/ai-gene-review/pull/3706) | [ed30b12d9918](https://github.com/ai4curation/ai-gene-review/commit/ed30b12d99188c9def4fcd8227f5c500a3fc9dbe) (2026-10-05T23:24:31Z) | [#4464](https://github.com/ai4curation/ai-gene-review/pull/4464) |

CDC14A adds one distinct original reviewed gene to the prior 274, giving **275**.
BIN1, BLM and BCL10 were already among those original reviews; their required
follow-ups supply three further completions and reduce the holds from four to
one. Thus 275 minus one hold gives 274 complete. Exactly these four primary
checkboxes change; supplementary genes and repeat reviews add no further
completion.

**Merged original review but incomplete at this cutoff:** AKR1D1 retains its
required Reactome:R-HSA-193755 source-follow-up gate. Its [follow-up #4465](https://github.com/ai4curation/ai-gene-review/pull/4465)
had not merged at the fixed cutoff, so proposed source recovery and evidence
corrections do not yet close the campaign hold. This does not claim that every
underlying source remains inaccessible. Biological DRAFT status and justified
UNDECIDED annotations remain independent of campaign closure.

Fresh remote evidence was read at 2026-10-09T18:54:37.586442+00:00. The recorded merge times,
rather than the later observation time, determine inclusion. Tracker #4467
merged at 2026-10-09T18:26:37Z and is the published baseline. Subsequent merges
and open work are outside this checkpoint. The first unchecked gene in literal
catalog order remains ACBD5.

The project status, queue status and latest completion timestamp use this
checkpoint. All 235 historical queue entries, 36 prior completion updates and
earlier dated progress sections are preserved. Their older PR states and counts
remain historical observations, superseded for current totals by this section.

## Completion checkpoint 270 — 2026-10-09 17:36:48 UTC

**270 complete / 2,606 remaining in the frozen 2,876-gene catalog.** This adds
eight completions beyond [published checkpoint 262](https://github.com/ai4curation/ai-gene-review/pull/4459).
The fixed [main snapshot fd81ce72cba2](https://github.com/ai4curation/ai-gene-review/commit/fd81ce72cba2618655d3bc7351581ef4a6abf9f2)
contains all eight gene merges and the preceding tracker merge. Completion
evidence stops at the BCS1L follow-up merge at the stated cutoff.

| Gene | PR | Final head | Approval | Merged UTC | Merge commit |
|---|---|---|---|---|---|
| BCAP31 | [#3605](https://github.com/ai4curation/ai-gene-review/pull/3605) | [d0650b3fbc6c](https://github.com/ai4curation/ai-gene-review/commit/d0650b3fbc6c76dc79d8b95a90ffe3412478589b) | [Approved](https://github.com/ai4curation/ai-gene-review/pull/3605#pullrequestreview-5472636799) | 2026-10-09T16:36:48Z | [f7911a500f1b](https://github.com/ai4curation/ai-gene-review/commit/f7911a500f1b503f735e6a551c577251c41dffff) |
| BCOR | [#3669](https://github.com/ai4curation/ai-gene-review/pull/3669) | [326a03a22810](https://github.com/ai4curation/ai-gene-review/commit/326a03a22810c77a2b2a0731605bf2bba15b700c) | [Approved](https://github.com/ai4curation/ai-gene-review/pull/3669#pullrequestreview-5472687886) | 2026-10-09T16:37:50Z | [34a24b719bd0](https://github.com/ai4curation/ai-gene-review/commit/34a24b719bd09f800256e5f5d5d66bef65d3fa44) |
| CDAN1 | [#4456](https://github.com/ai4curation/ai-gene-review/pull/4456) | [316d1fe4894c](https://github.com/ai4curation/ai-gene-review/commit/316d1fe4894c0eca32372b1a1f980380e81b6c9c) | [Approved](https://github.com/ai4curation/ai-gene-review/pull/4456#pullrequestreview-5472731219) | 2026-10-09T16:47:23Z | [fe9d0eec86d1](https://github.com/ai4curation/ai-gene-review/commit/fe9d0eec86d1f5b949960c82e206f1a330bba618) |
| BCKDHB | [#4457](https://github.com/ai4curation/ai-gene-review/pull/4457) | [49370df72373](https://github.com/ai4curation/ai-gene-review/commit/49370df723737c5d859366f69b5f195bda69e982) | [Approved](https://github.com/ai4curation/ai-gene-review/pull/4457#pullrequestreview-5472759309) | 2026-10-09T16:55:25Z | [8304d7366c63](https://github.com/ai4curation/ai-gene-review/commit/8304d7366c63e6cc673f92efe82cf2378fab23c9) |
| CD70 | [#4446](https://github.com/ai4curation/ai-gene-review/pull/4446) | [36325439ce74](https://github.com/ai4curation/ai-gene-review/commit/36325439ce748a0e33241135aa1472fc87e552cd) | [Approved](https://github.com/ai4curation/ai-gene-review/pull/4446#pullrequestreview-5473281701) | 2026-10-09T17:34:07Z | [3c072d130a74](https://github.com/ai4curation/ai-gene-review/commit/3c072d130a74361b7b9f1a55fe453953d4d2147d) |
| CD79A | [#4453](https://github.com/ai4curation/ai-gene-review/pull/4453) | [ed8dff6d008e](https://github.com/ai4curation/ai-gene-review/commit/ed8dff6d008e0f79e76724605198cad84cbbd4b7) | [Approved](https://github.com/ai4curation/ai-gene-review/pull/4453#pullrequestreview-5473297643) | 2026-10-09T17:34:17Z | [956eca1abfa5](https://github.com/ai4curation/ai-gene-review/commit/956eca1abfa5ca0b84b8818171b658756421073b) |
| CD79B | [#4455](https://github.com/ai4curation/ai-gene-review/pull/4455) | [503f8b6beda9](https://github.com/ai4curation/ai-gene-review/commit/503f8b6beda9660ea4eb3193265c6616498368bb) | [Approved](https://github.com/ai4curation/ai-gene-review/pull/4455#pullrequestreview-5473305496) | 2026-10-09T17:34:28Z | [a6fbc79b744d](https://github.com/ai4curation/ai-gene-review/commit/a6fbc79b744dfe7ee59fed591f6563be5bafe651) |
| BCS1L | [#4460](https://github.com/ai4curation/ai-gene-review/pull/4460) | [63120c89599a](https://github.com/ai4curation/ai-gene-review/commit/63120c89599aa7f23513e534585c5c9b50e3cd2c) | [Approved](https://github.com/ai4curation/ai-gene-review/pull/4460#pullrequestreview-5473289008) | 2026-10-09T17:36:48Z | [fd81ce72cba2](https://github.com/ai4curation/ai-gene-review/commit/fd81ce72cba2618655d3bc7351581ef4a6abf9f2) |

Each approval belongs to the listed final head. The test (3.12) and claude-review
checks completed successfully on that same commit before its actual merge time,
verified using their check-suite commit IDs. All 93 changed PR paths were checked
against their approved heads and merge commits. The 92 identical paths include
all 35 changed gene artifacts, which also match the fixed cutoff snapshot. The
sole shared-cache difference is BCOR: its merge retains the newer main GO cache
rows and adds only the approved GO:0140261 BCOR complex row. This cache is not
claimed to be byte-identical to its older PR head.

**Two holds close without double-counting original reviews:**

| Gene | Original review already counted | Original merge | Closing follow-up |
|---|---|---|---|
| BCKDHB | [#3616](https://github.com/ai4curation/ai-gene-review/pull/3616) | [c3f9ef9a3bdc](https://github.com/ai4curation/ai-gene-review/commit/c3f9ef9a3bdc8ab235a473fe15d0db7d36e88288) (2026-10-05T23:23:02Z) | [#4457](https://github.com/ai4curation/ai-gene-review/pull/4457) |
| BCS1L | [#3658](https://github.com/ai4curation/ai-gene-review/pull/3658) | [9da157e0d2bb](https://github.com/ai4curation/ai-gene-review/commit/9da157e0d2bb032c387c6aed858e9518f94d96f4) (2026-10-05T23:23:38Z) | [#4460](https://github.com/ai4curation/ai-gene-review/pull/4460) |

BCAP31, BCOR, CDAN1, CD70, CD79A and CD79B add six distinct original reviewed
genes to the prior 268, giving **274**. BCKDHB and BCS1L were already among
those original reviews; their follow-ups supply two further completions and
reduce the holds from six to four. Thus 274 minus four holds gives 270 complete.
Exactly these eight primary checkboxes change; supplementary genes and repeat
reviews add no further completion.

**Merged but incomplete at this cutoff:** AKR1D1 retains its recorded
Reactome:R-HSA-193755 source gate; BCL10, BIN1 and BLM retain their recorded
binding-policy follow-up requirement. Later proposed corrections do not close
these holds at this snapshot. Biological DRAFT status and justified UNDECIDED
annotations remain independent of campaign closure.

Fresh remote evidence was read at 2026-10-09T17:42:42.558201+00:00. The recorded merge times,
rather than the later observation time, determine inclusion. Tracker #4459
merged at 2026-10-09T17:34:40Z and is the published baseline. Subsequent merges
and open work are outside this checkpoint. The first unchecked gene in literal
catalog order remains ACBD5.

The project status, queue status and latest completion timestamp use this
checkpoint. All 235 historical queue entries, 35 prior completion updates and
earlier dated progress sections are preserved. Their older PR states and counts
remain historical observations, superseded for current totals by this section.

[Checkpoint curation history](../../history/projects/CLINGEN_MENDELIAN/2026-10-09T175417Z-codex-02c570.yaml) records this update.

## Completion checkpoint 262 — 2026-10-09 16:19:32 UTC

**262 complete / 2,614 remaining in the frozen 2,876-gene catalog.** This adds
five completions beyond [published checkpoint 257](https://github.com/ai4curation/ai-gene-review/pull/4450).
The fixed [main snapshot 1353583bdcc0](https://github.com/ai4curation/ai-gene-review/commit/1353583bdcc0ad7116be610523f84594bd21b9c6)
contains all five gene merges and the preceding tracker merge. Completion evidence
stops at the BBS5 merge at the stated cutoff.

| Gene | PR | Final head | Approval | Merged UTC | Merge commit |
|---|---|---|---|---|---|
| CD40LG | [#4442](https://github.com/ai4curation/ai-gene-review/pull/4442) | [95855ddee197](https://github.com/ai4curation/ai-gene-review/commit/95855ddee197c2604864f447c87d3c2b805eb4e5) | [Approved](https://github.com/ai4curation/ai-gene-review/pull/4442#pullrequestreview-5471894778) | 2026-10-09T15:32:28Z | [4d0debe40f95](https://github.com/ai4curation/ai-gene-review/commit/4d0debe40f95b9ee2d17bf3ad91f5e9dcf742335) |
| BBS7 | [#3596](https://github.com/ai4curation/ai-gene-review/pull/3596) | [10f97c076fce](https://github.com/ai4curation/ai-gene-review/commit/10f97c076fce2ed875a7e6bd58611fb603b11734) | [Approved](https://github.com/ai4curation/ai-gene-review/pull/3596#pullrequestreview-5471888058) | 2026-10-09T15:34:07Z | [e1cf41205fa0](https://github.com/ai4curation/ai-gene-review/commit/e1cf41205fa0d4733866efee8f1ddef4c4692161) |
| CD46 | [#4444](https://github.com/ai4curation/ai-gene-review/pull/4444) | [f58c5c03b1dd](https://github.com/ai4curation/ai-gene-review/commit/f58c5c03b1dd5626bf2bde984ab20b13192ac032) | [Approved](https://github.com/ai4curation/ai-gene-review/pull/4444#pullrequestreview-5472203815) | 2026-10-09T16:02:20Z | [e92ea9b751fa](https://github.com/ai4curation/ai-gene-review/commit/e92ea9b751fad6c20145b94fdc86c5094509dce1) |
| BBS9 | [#3604](https://github.com/ai4curation/ai-gene-review/pull/3604) | [94f9165fefd1](https://github.com/ai4curation/ai-gene-review/commit/94f9165fefd1091b2410352a3eb84ef2ba407d9d) | [Approved](https://github.com/ai4curation/ai-gene-review/pull/3604#pullrequestreview-5472316757) | 2026-10-09T16:09:49Z | [7570bc0a5e0f](https://github.com/ai4curation/ai-gene-review/commit/7570bc0a5e0f298c29573cda10cb67b22f1b974f) |
| BBS5 | [#3592](https://github.com/ai4curation/ai-gene-review/pull/3592) | [0c231ad1487d](https://github.com/ai4curation/ai-gene-review/commit/0c231ad1487d4abd04bba9bbd0cdf289f96716ce) | [Approved](https://github.com/ai4curation/ai-gene-review/pull/3592#pullrequestreview-5472509358) | 2026-10-09T16:19:32Z | [1353583bdcc0](https://github.com/ai4curation/ai-gene-review/commit/1353583bdcc0ad7116be610523f84594bd21b9c6) |

Each approval belongs to the listed final head. The test (3.12) and claude-review
checks completed successfully on that same commit before merge, verified using
their check-suite commit IDs. Exactly these five primary checkboxes change.
Supplementary genes and repeat reviews add no completion.

**Merged but incomplete:** the six holds remain AKR1D1, BCKDHB, BCL10, BCS1L,
BIN1 and BLM. AKR1D1 retains its unresolved Reactome:R-HSA-193755 source gate;
the other five retain their recorded binding-policy follow-up requirement.
The fresh [BCKDHB follow-up #4457](https://github.com/ai4curation/ai-gene-review/pull/4457)
is open at the separate observation below and does not close its hold. Thus 268
distinct primary genes have merged original campaign reviews: 262 completions
and six holds. DRAFT review status and justified UNDECIDED annotations remain
independent of campaign closure.

**Open campaign PRs**, observed 2026-10-09T16:29:40.461702+00:00:
these dated observations add no completion at the fixed cutoff.

| Gene | PR | Observed head | Review | test (3.12) | Review workflow |
|---|---|---|---|---|---|
| BCAP31 | [#3605](https://github.com/ai4curation/ai-gene-review/pull/3605) | [d0650b3fbc6c](https://github.com/ai4curation/ai-gene-review/commit/d0650b3fbc6c76dc79d8b95a90ffe3412478589b) | APPROVED | IN_PROGRESS | SUCCESS |
| BCKDHB | [#4457](https://github.com/ai4curation/ai-gene-review/pull/4457) | [49370df72373](https://github.com/ai4curation/ai-gene-review/commit/49370df723737c5d859366f69b5f195bda69e982) | REVIEW_REQUIRED | IN_PROGRESS | IN_PROGRESS |
| BCOR | [#3669](https://github.com/ai4curation/ai-gene-review/pull/3669) | [326a03a22810](https://github.com/ai4curation/ai-gene-review/commit/326a03a22810c77a2b2a0731605bf2bba15b700c) | APPROVED | IN_PROGRESS | SUCCESS |
| CD70 | [#4446](https://github.com/ai4curation/ai-gene-review/pull/4446) | [936f131d4710](https://github.com/ai4curation/ai-gene-review/commit/936f131d47101fef6da6659ae76f198cb70cd737) | APPROVED | IN_PROGRESS | SUCCESS |
| CD79A | [#4453](https://github.com/ai4curation/ai-gene-review/pull/4453) | [752bbe2df6d3](https://github.com/ai4curation/ai-gene-review/commit/752bbe2df6d3ce58347d8a5d3efa0e753d96661e) | CHANGES_REQUESTED | SUCCESS | SUCCESS |
| CD79B | [#4455](https://github.com/ai4curation/ai-gene-review/pull/4455) | [36973541616d](https://github.com/ai4curation/ai-gene-review/commit/36973541616dcc3cc06dbdfed7b281720d350646) | CHANGES_REQUESTED | IN_PROGRESS | SUCCESS |
| CDAN1 | [#4456](https://github.com/ai4curation/ai-gene-review/pull/4456) | [316d1fe4894c](https://github.com/ai4curation/ai-gene-review/commit/316d1fe4894c0eca32372b1a1f980380e81b6c9c) | REVIEW_REQUIRED | IN_PROGRESS | IN_PROGRESS |

Continue these reviews and their actionable feedback. The first unchecked gene
in literal catalog order remains ACBD5; active work elsewhere does not mark
earlier catalog entries complete.

[Checkpoint curation history](../../history/projects/CLINGEN_MENDELIAN/2026-10-09T163721Z-codex-30b1ba.yaml) records this update.

The project status, queue status and latest completion timestamp use this
checkpoint. All 235 historical queue entries, 34 prior completion updates and
earlier dated progress sections are preserved. Their older PR states and counts
remain historical observations, superseded for current totals by this section.

## Completion checkpoint 257 — 2026-10-09 14:48:08 UTC

**257 complete / 2,619 remaining in the frozen 2,876-gene catalog.** This adds
six completions beyond [published checkpoint 251](https://github.com/ai4curation/ai-gene-review/pull/4432).
The fixed [main snapshot de56024a5a3e](https://github.com/ai4curation/ai-gene-review/commit/de56024a5a3ed1e32ca0654ee5dc8def94e804a2)
includes the BBS4 merge at the stated cutoff. No pending approval or later merge
is included.

| Gene | PR | Final approved head | Merged UTC | Merge commit |
|---|---|---|---|---|
| BBS1 | [#3586](https://github.com/ai4curation/ai-gene-review/pull/3586) | [0c25363c49ec](https://github.com/ai4curation/ai-gene-review/pull/3586#pullrequestreview-5470755472) | 2026-10-09T13:57:01Z | [67c4ec0a6e4a](https://github.com/ai4curation/ai-gene-review/commit/67c4ec0a6e4af272150f387028eee8efdc72152e) |
| BBS10 | [#3587](https://github.com/ai4curation/ai-gene-review/pull/3587) | [a751ae7465bf](https://github.com/ai4curation/ai-gene-review/pull/3587#pullrequestreview-5470921488) | 2026-10-09T14:10:22Z | [35f6d3a75628](https://github.com/ai4curation/ai-gene-review/commit/35f6d3a75628e6276cf1d689a1200298ba94c8bb) |
| CD3G | [#4431](https://github.com/ai4curation/ai-gene-review/pull/4431) | [9564eb79dd2e](https://github.com/ai4curation/ai-gene-review/pull/4431#pullrequestreview-5470928794) | 2026-10-09T14:14:25Z | [fd0499e2fa48](https://github.com/ai4curation/ai-gene-review/commit/fd0499e2fa48be8a8ef4a9275816076c21a95920) |
| BBS2 | [#3590](https://github.com/ai4curation/ai-gene-review/pull/3590) | [d2565cbf2cbc](https://github.com/ai4curation/ai-gene-review/pull/3590#pullrequestreview-5471185120) | 2026-10-09T14:40:32Z | [4f6e56c0f97e](https://github.com/ai4curation/ai-gene-review/commit/4f6e56c0f97ea7d982b76a3880d70d9c6e7a8854) |
| CD40 | [#4437](https://github.com/ai4curation/ai-gene-review/pull/4437) | [0c3cb34ea333](https://github.com/ai4curation/ai-gene-review/pull/4437#pullrequestreview-5471163875) | 2026-10-09T14:41:35Z | [c8681adfdbc0](https://github.com/ai4curation/ai-gene-review/commit/c8681adfdbc0745beaf08f7d04983263e67a0226) |
| BBS4 | [#3591](https://github.com/ai4curation/ai-gene-review/pull/3591) | [412f235a3d7a](https://github.com/ai4curation/ai-gene-review/pull/3591#pullrequestreview-5471313397) | 2026-10-09T14:48:08Z | [de56024a5a3e](https://github.com/ai4curation/ai-gene-review/commit/de56024a5a3ed1e32ca0654ee5dc8def94e804a2) |

Each listed head has an APPROVED review and successful test (3.12) and
claude-review checks on that same commit. All six primary catalog checkboxes
change from unchecked to checked. No supplemental gene or repeated review adds
to the completion count.

**Merged but incomplete:** the same six required follow-ups remain unchecked:
[AKR1D1 #3266/#3941](https://github.com/ai4curation/ai-gene-review/pull/3941)
for the unresolved Reactome:R-HSA-193755 source gate;
[BCKDHB #3616](https://github.com/ai4curation/ai-gene-review/pull/3616),
[BCL10 #3649](https://github.com/ai4curation/ai-gene-review/pull/3649),
[BCS1L #3658](https://github.com/ai4curation/ai-gene-review/pull/3658),
[BIN1 #3689](https://github.com/ai4curation/ai-gene-review/pull/3689) and
[BLM #3706](https://github.com/ai4curation/ai-gene-review/pull/3706) for the
previously documented, row-specific binding-policy follow-ups. Thus 263 primary
genes have merged campaign reviews, comprising 257 completions and six holds.
Justified UNDECIDED annotations and biological DRAFT status remain independent
of campaign closure.

**Open campaign PRs**, observed 2026-10-09T14:59:20.102408+00:00:
these are a separate current-work observation, not additional completions.

| Gene | PR | Observed head | Review | test (3.12) | Review workflow |
|---|---|---|---|---|---|
| BBS5 | [#3592](https://github.com/ai4curation/ai-gene-review/pull/3592) | 6963bc0c862a | CHANGES_REQUESTED | IN_PROGRESS | SUCCESS |
| BBS7 | [#3596](https://github.com/ai4curation/ai-gene-review/pull/3596) | 32fbd403feac | CHANGES_REQUESTED | IN_PROGRESS | QUEUED |
| BBS9 | [#3604](https://github.com/ai4curation/ai-gene-review/pull/3604) | 85458a897999 | CHANGES_REQUESTED | SUCCESS | SUCCESS |
| BCAP31 | [#3605](https://github.com/ai4curation/ai-gene-review/pull/3605) | e5edf4a90794 | CHANGES_REQUESTED | SUCCESS | SUCCESS |
| BCOR | [#3669](https://github.com/ai4curation/ai-gene-review/pull/3669) | 2b44abc319a4 | CHANGES_REQUESTED | SUCCESS | SUCCESS |
| CD40LG | [#4442](https://github.com/ai4curation/ai-gene-review/pull/4442) | 39cfbc94b731 | CHANGES_REQUESTED | SUCCESS | SUCCESS |
| CD46 | [#4444](https://github.com/ai4curation/ai-gene-review/pull/4444) | 9022fd678447 | CHANGES_REQUESTED | IN_PROGRESS | SUCCESS |

BBS5 is the earliest open campaign PR. Continue the open reviews and their
feedback, with CD40LG and CD46 preceding the saved CD70 continuation. The first
unchecked gene in literal catalog order remains ACBD5; this work order does not
imply that earlier unchecked genes are complete.

The parent project status, queue status and latest completion timestamp all use
this checkpoint. The 235 historical queue entries and all earlier completion
updates are preserved. The prior reconciliation and dated tables below remain
historical observations at their original cutoffs, superseded for current totals
by this section.

## Completion reconciliation — 2026-10-09

**251 complete / 2,625 remaining in the frozen 2,876-gene catalog.** The published
checkpoint 240 gains the following 11 completions. The first six were already
confirmed in the saved session checkpoint 246; the last five merged on October 6.

| Gene | PR | Merged UTC | Merge commit |
|---|---|---|---|
| CCM2 | [#4239](https://github.com/ai4curation/ai-gene-review/pull/4239) | 2026-10-05T01:59:05Z | [`fa209203c572`](https://github.com/ai4curation/ai-gene-review/commit/fa209203c572d1587fd611fcddfc04346ffa7ca0) |
| CCNO | [#4253](https://github.com/ai4curation/ai-gene-review/pull/4253) | 2026-10-05T03:34:33Z | [`0c68977b2022`](https://github.com/ai4curation/ai-gene-review/commit/0c68977b2022b597208b6ee258ee28e4aee78db6) |
| CCN6 | [#4240](https://github.com/ai4curation/ai-gene-review/pull/4240) | 2026-10-05T04:53:11Z | [`68355bad3b0b`](https://github.com/ai4curation/ai-gene-review/commit/68355bad3b0b564a8147e3d03949edae5a872c9d) |
| CD19 | [#4256](https://github.com/ai4curation/ai-gene-review/pull/4256) | 2026-10-05T05:26:51Z | [`44c0cfeaa6a6`](https://github.com/ai4curation/ai-gene-review/commit/44c0cfeaa6a64f3b0e0817b35094adf13c310d7e) |
| CD320 | [#4273](https://github.com/ai4curation/ai-gene-review/pull/4273) | 2026-10-05T06:00:49Z | [`7df8e72f6937`](https://github.com/ai4curation/ai-gene-review/commit/7df8e72f6937e8325011bf300dbce593afbeab18) |
| CD27 | [#4307](https://github.com/ai4curation/ai-gene-review/pull/4307) | 2026-10-05T06:48:46Z | [`866a9ea15d96`](https://github.com/ai4curation/ai-gene-review/commit/866a9ea15d966ecfc9572cd5765ce29c238cad7a) |
| CD247 | [#4264](https://github.com/ai4curation/ai-gene-review/pull/4264) | 2026-10-06T11:39:16Z | [`a834dfb54079`](https://github.com/ai4curation/ai-gene-review/commit/a834dfb54079139ddd388d3a38c3a1878620be27) |
| CD2AP | [#4287](https://github.com/ai4curation/ai-gene-review/pull/4287) | 2026-10-06T11:40:18Z | [`23bf11486ff1`](https://github.com/ai4curation/ai-gene-review/commit/23bf11486ff17dd82fe53773c548a70141e89c25) |
| CD3D | [#4293](https://github.com/ai4curation/ai-gene-review/pull/4293) | 2026-10-06T11:41:17Z | [`4987e0d39b1d`](https://github.com/ai4curation/ai-gene-review/commit/4987e0d39b1d90afd30d687b8c6f75aad0cf8f5d) |
| ASB10 | [#4308](https://github.com/ai4curation/ai-gene-review/pull/4308) | 2026-10-06T11:43:34Z | [`4fb7e051901a`](https://github.com/ai4curation/ai-gene-review/commit/4fb7e051901a4d7b71650e36d48ad2312ba314b9) |
| CD3E | [#4313](https://github.com/ai4curation/ai-gene-review/pull/4313) | 2026-10-06T11:43:47Z | [`7c1ba7f73a84`](https://github.com/ai4curation/ai-gene-review/commit/7c1ba7f73a846f59f86506c67d95bc995ea2e253) |

All 11 PRs have approval on the final head and successful `test (3.12)` and
`claude-review` checks. For the five October 6 closures, current main retains
DRAFT review status and the recorded evidence uncertainties; campaign closure
does not turn these into resolved biological assertions. ASB10 is counted once
after its required binding-policy follow-up #4308.

**Merged but incomplete:** AKR1D1 #3266/#3941 retains its unresolved
Reactome:R-HSA-193755 source gate. Five other merged PRs require project-policy
follow-up; 29 generic-binding removals were identified for row-specific
assessment:

| Gene | Merged PR | Generic `GO:0005515` REMOVE rows requiring follow-up |
|---|---|---:|
| BCKDHB | [#3616](https://github.com/ai4curation/ai-gene-review/pull/3616) | 5 |
| BCL10 | [#3649](https://github.com/ai4curation/ai-gene-review/pull/3649) | 4 |
| BCS1L | [#3658](https://github.com/ai4curation/ai-gene-review/pull/3658) | 1 |
| BIN1 | [#3689](https://github.com/ai4curation/ai-gene-review/pull/3689) | 4 |
| BLM | [#3706](https://github.com/ai4curation/ai-gene-review/pull/3706) | 15 |

Their approvals applied the repository-wide informational-exclusion policy,
whereas this project explicitly retains supported generic interactions as
KEEP_AS_NON_CORE unless a supported refinement exists. Review each row against
its evidence; do not replace removals mechanically. These five and AKR1D1 stay
unchecked. The 257 distinct primary genes with merged campaign PRs therefore
comprise 251 completed genes and six required follow-ups.

**Open campaign PRs:** all nine remain CHANGES_REQUESTED with required CI green.

| Gene | PR | State |
|---|---|---|
| BBS1 | [#3586](https://github.com/ai4curation/ai-gene-review/pull/3586) | CHANGES_REQUESTED; test (3.12) SUCCESS |
| BBS10 | [#3587](https://github.com/ai4curation/ai-gene-review/pull/3587) | CHANGES_REQUESTED; test (3.12) SUCCESS |
| BBS2 | [#3590](https://github.com/ai4curation/ai-gene-review/pull/3590) | CHANGES_REQUESTED; test (3.12) SUCCESS |
| BBS4 | [#3591](https://github.com/ai4curation/ai-gene-review/pull/3591) | CHANGES_REQUESTED; test (3.12) SUCCESS |
| BBS5 | [#3592](https://github.com/ai4curation/ai-gene-review/pull/3592) | CHANGES_REQUESTED; test (3.12) SUCCESS |
| BBS7 | [#3596](https://github.com/ai4curation/ai-gene-review/pull/3596) | CHANGES_REQUESTED; test (3.12) SUCCESS |
| BBS9 | [#3604](https://github.com/ai4curation/ai-gene-review/pull/3604) | CHANGES_REQUESTED; test (3.12) SUCCESS |
| BCAP31 | [#3605](https://github.com/ai4curation/ai-gene-review/pull/3605) | CHANGES_REQUESTED; test (3.12) SUCCESS |
| BCOR | [#3669](https://github.com/ai4curation/ai-gene-review/pull/3669) | CHANGES_REQUESTED; test (3.12) SUCCESS |

Resume the saved in-progress review at CD3G, then CD40, CD40LG, CD46 and CD70;
keep the older open PRs and merged follow-ups visible in the queue. The literal
first unchecked Definitive inventory gene is ACBD5, so the saved continuation
cursor is not a claim that every earlier gene is complete.

The mixed 707-path MAPK_CASCADES PR #3381 is excluded from this count; its BRAF
changes still need a campaign assessment. Unrelated project reviews, repeated
reviews and supplemental work do not increment the primary denominator or
completion count. The mitochondrial, RNA, other-locus and undetermined-inheritance
lists are already included in the frozen 2,876.

The following historical status table and all earlier dated observations are
preserved at their original cutoff.

## Campaign status — completion evidence through 2026-10-05 01:02:15 UTC

| Gene | Tier | Starting review status | Current state | Branch | PR |
|---|---|---|---|---|---|
| A4GALT | Definitive | INITIALIZED | Merged; final validation and CI passed | `cmungall/clingen-a4galt` | [#3127](https://github.com/ai4curation/ai-gene-review/pull/3127) |
| AARS1 | Definitive | COMPLETE | Post-merge source follow-up #3301 merged; exact-head approval and required CI passed; all 15 scoped merged blobs verified | `cmungall/clingen-aars1` | [#3129](https://github.com/ai4curation/ai-gene-review/pull/3129) |
| AARS2 | Definitive | COMPLETE | Merged; final validation and CI passed | `cmungall/clingen-aars2` | [#3128](https://github.com/ai4curation/ai-gene-review/pull/3128) |
| AASS | Definitive | INITIALIZED | Merged; final validation and CI passed | `cmungall/clingen-aass` | [#3133](https://github.com/ai4curation/ai-gene-review/pull/3133) |
| ABCA3 | Definitive | No review | Post-merge source follow-up #3303 merged; current-head approval and required CI passed; all 15 scoped merged blobs verified | `cmungall/clingen-abca3` | [#3134](https://github.com/ai4curation/ai-gene-review/pull/3134) |
| ABCA4 | Definitive | No review | Post-merge source follow-up #3308 merged; current-head approval and required CI passed; all 16 scoped merged blobs verified | `cmungall/clingen-abca4` | [#3132](https://github.com/ai4curation/ai-gene-review/pull/3132) |
| ABCB4 | Definitive | No review | Merged; final approval and required CI passed | `cmungall/clingen-abcb4` | [#3135](https://github.com/ai4curation/ai-gene-review/pull/3135) |
| ABCC6 | Definitive | No review | Merged; final approval and required CI passed | `cmungall/clingen-abcc6` | [#3138](https://github.com/ai4curation/ai-gene-review/pull/3138) |
| ABCC8 | Definitive | No review | Post-merge source follow-up #3310 merged; current-head approval and required CI passed; all 19 scoped merged blobs verified | `cmungall/clingen-abcc8` | [#3136](https://github.com/ai4curation/ai-gene-review/pull/3136) |
| ABCC9 | Definitive | No review | Merged; final approval and required CI passed | `cmungall/clingen-abcc9` | [#3148](https://github.com/ai4curation/ai-gene-review/pull/3148) |
| ABCD1 | Definitive | No review | Post-merge source follow-up #3311 merged; current-head approval and required CI passed; all 20 scoped merged blobs verified | `cmungall/clingen-abcd1` | [#3150](https://github.com/ai4curation/ai-gene-review/pull/3150) |
| ACAD8 | Definitive | INITIALIZED | Merged; final approval and required CI passed | `cmungall/clingen-acad8` | [#3151](https://github.com/ai4curation/ai-gene-review/pull/3151) |
| ACAD9 | Definitive | COMPLETE | Merged; final approval and required CI passed | `cmungall/clingen-acad9` | [#3152](https://github.com/ai4curation/ai-gene-review/pull/3152) |
| ACADM | Definitive | COMPLETE | Merged; final-head approval and required CI passed; all required source caches published | `cmungall/clingen-acadm` | [#3156](https://github.com/ai4curation/ai-gene-review/pull/3156) |
| ACADS | Definitive | COMPLETE | Merged; final approval and required CI passed | `cmungall/clingen-acads` | [#3155](https://github.com/ai4curation/ai-gene-review/pull/3155) |
| ACADSB | Definitive | INITIALIZED | Merged; final approval and required CI passed | `cmungall/clingen-acadsb` | [#3154](https://github.com/ai4curation/ai-gene-review/pull/3154) |
| ACADVL | Definitive | COMPLETE | Merged; final-head approval and required CI passed | `cmungall/clingen-acadvl` | [#3157](https://github.com/ai4curation/ai-gene-review/pull/3157) |
| ACAN | Definitive | COMPLETE | Merged; final-head approval and required CI passed; all required source caches published | `cmungall/clingen-acan` | [#3153](https://github.com/ai4curation/ai-gene-review/pull/3153) |
| ACAT1 | Definitive | COMPLETE | Original and follow-up merged; final-head approval and required CI passed; all 15 scoped merged blobs verified | `cmungall/clingen-acat1` | [#3158](https://github.com/ai4curation/ai-gene-review/pull/3158) |
| ACOX1 | Definitive | INITIALIZED | Merged; final-head approval and required CI passed; all required source caches published | `cmungall/clingen-acox1` | [#3159](https://github.com/ai4curation/ai-gene-review/pull/3159) |
| ACOX2 | Definitive | INITIALIZED | Post-merge source follow-up #3248 merged; exact-head approval and required CI passed; all 25 scoped merged blobs verified | `cmungall/clingen-acox2` | [#3161](https://github.com/ai4curation/ai-gene-review/pull/3161) |
| ACSL4 | Definitive | COMPLETE | Post-merge source follow-up #3247 merged; exact-head approval and required CI passed; all 50 scoped merged blobs verified | `cmungall/clingen-acsl4` | [#3160](https://github.com/ai4curation/ai-gene-review/pull/3160) |
| ACTA1 | Definitive | COMPLETE | Merged; final-head approval and required CI passed | `cmungall/clingen-acta1` | [#3163](https://github.com/ai4curation/ai-gene-review/pull/3163) |
| ACTA2 | Definitive | COMPLETE | Merged; final-head approval and required CI passed; all cited publication caches available | `cmungall/clingen-acta2` | [#3164](https://github.com/ai4curation/ai-gene-review/pull/3164) |
| ACTB | Definitive | COMPLETE | Post-merge source follow-up #3302 merged; current-head approval and required CI passed; all 24 scoped merged blobs verified | `cmungall/clingen-actb` | [#3184](https://github.com/ai4curation/ai-gene-review/pull/3184) |
| ADA | Definitive | INITIALIZED | Merged; final-head approval and required CI passed; all required source follow-ups merged | `cmungall/clingen-ada` | [#3179](https://github.com/ai4curation/ai-gene-review/pull/3179) |
| ADGRV1 | Definitive | COMPLETE | Post-merge source follow-up #3304 merged; current-head approval and required CI passed; all 21 scoped merged blobs verified | `cmungall/clingen-adgrv1` | [#3192](https://github.com/ai4curation/ai-gene-review/pull/3192) |
| ADNP | Definitive | COMPLETE | Review #3193 merged; exact-head approval and required CI passed; all 44 scoped merged blobs verified | `cmungall/clingen-adnp` | [#3193](https://github.com/ai4curation/ai-gene-review/pull/3193) |
| ADSL | Definitive | INITIALIZED | Merged #3194; final-head approval and required CI passed; all 23 scoped merged blobs verified | `cmungall/clingen-adsl` | [#3194](https://github.com/ai4curation/ai-gene-review/pull/3194) |
| AFG3L2 | Definitive | COMPLETE | Post-merge source follow-up #3312 merged; current-head approval and required CI passed; all 13 scoped merged blobs verified | `cmungall/clingen-afg3l2` | [#3196](https://github.com/ai4curation/ai-gene-review/pull/3196) |
| AGK | Definitive | COMPLETE | Post-merge source follow-up #3314 merged; current-head approval and required CI passed; all 46 scoped merged blobs verified | `cmungall/clingen-agk` | [#3195](https://github.com/ai4curation/ai-gene-review/pull/3195) |
| AGL | Definitive | INITIALIZED | Merged; final-head approval and required CI passed; all required source follow-ups merged | `cmungall/clingen-agl` | [#3197](https://github.com/ai4curation/ai-gene-review/pull/3197) |
| AGO1 | Definitive | COMPLETE | Post-merge source follow-up #3313 merged; current-head approval and required CI passed; all 13 scoped merged blobs verified | `cmungall/clingen-ago1` | [#3207](https://github.com/ai4curation/ai-gene-review/pull/3207) |
| AGO2 | Definitive | COMPLETE | Post-merge source follow-up #3288 merged; exact-head approval and required CI passed; all 21 scoped merged blobs verified | `cmungall/clingen-ago2` | [#3210](https://github.com/ai4curation/ai-gene-review/pull/3210) |
| AGPAT2 | Definitive | INITIALIZED | Merged; final-head approval and required CI passed; all required source caches published | `cmungall/clingen-agpat2` | [#3208](https://github.com/ai4curation/ai-gene-review/pull/3208) |
| AGPS | Definitive | INITIALIZED | Merged; final-head approval and required CI passed; all required source caches published | `cmungall/clingen-agps` | [#3209](https://github.com/ai4curation/ai-gene-review/pull/3209) |
| AGXT | Definitive | INITIALIZED | Merged; final-head approval and required CI passed; all required source caches published | `cmungall/clingen-agxt` | [#3212](https://github.com/ai4curation/ai-gene-review/pull/3212) |
| AHDC1 | Definitive | COMPLETE | Merged; final-head substantive approval and required CI passed; all required source follow-ups merged | `cmungall/clingen-ahdc1` | [#3213](https://github.com/ai4curation/ai-gene-review/pull/3213) |
| AHI1 | Definitive | COMPLETE | Review #3215 merged; exact-head approval and required CI passed; all 37 scoped merged blobs verified | `cmungall/clingen-ahi1` | [#3215](https://github.com/ai4curation/ai-gene-review/pull/3215) |
| AKT1 | Limited | COMPLETE | Review merged; final-head approval and required CI passed; all 69 scoped merged blobs verified | `cmungall/clingen-akt1` | [#3242](https://github.com/ai4curation/ai-gene-review/pull/3242) |
| AGRN | Definitive | COMPLETE | Review #3243 merged; current-head approval and required CI passed; all 55 scoped merged blobs verified | `cmungall/clingen-agrn` | [#3243](https://github.com/ai4curation/ai-gene-review/pull/3243) |
| AHCY | Definitive | COMPLETE | Review merged; final-head approval and required CI passed; all 14 scoped merged blobs verified | `cmungall/clingen-ahcy` | [#3244](https://github.com/ai4curation/ai-gene-review/pull/3244) |
| AIMP1 | Definitive | COMPLETE | Review merged; final-head approval and required CI passed; all 21 scoped merged blobs verified | `cmungall/clingen-aimp1` | [#3262](https://github.com/ai4curation/ai-gene-review/pull/3262) |
| AIMP2 | Definitive | COMPLETE | Post-merge source follow-up #3289 merged; exact-head approval and required CI passed; all 24 scoped merged blobs verified | `cmungall/clingen-aimp2` | [#3256](https://github.com/ai4curation/ai-gene-review/pull/3256) |
| AIPL1 | Definitive | COMPLETE | Merged #3257; final-head approval and required CI passed; all 24 scoped merged blobs verified | `cmungall/clingen-aipl1` | [#3257](https://github.com/ai4curation/ai-gene-review/pull/3257) |
| AIRE | Definitive | COMPLETE | Review merged; final-head approval and required CI passed; all 22 scoped merged blobs verified | `cmungall/clingen-aire` | [#3265](https://github.com/ai4curation/ai-gene-review/pull/3265) |
| AKR1D1 | Definitive | INITIALIZED | Original #3266 externally observed merged; scoped reviewed/merged blobs verified; Required source R-HSA-193755 remains unresolved; merge does not grant completion. | `cmungall/clingen-akr1d1` | [#3266](https://github.com/ai4curation/ai-gene-review/pull/3266) |
| ALAS2 | Definitive | INITIALIZED | Merged #3267; final-head approval and required CI passed; all 21 scoped merged blobs verified | `cmungall/clingen-alas2` | [#3267](https://github.com/ai4curation/ai-gene-review/pull/3267) |
| ALDH18A1 | Definitive | INITIALIZED | Review merged; final-head approval and required CI passed; all 15 scoped merged blobs verified | `cmungall/clingen-aldh18a1` | [#3269](https://github.com/ai4curation/ai-gene-review/pull/3269) |
| ALDH4A1 | Definitive | COMPLETE | Review merged; final-head approval and required CI passed; all 9 scoped merged blobs verified | `cmungall/clingen-aldh4a1` | [#3271](https://github.com/ai4curation/ai-gene-review/pull/3271) |
| ALDH5A1 | Definitive | INITIALIZED | Review merged; final-head approval and required CI passed; all 11 scoped merged blobs verified | `cmungall/clingen-aldh5a1` | [#3268](https://github.com/ai4curation/ai-gene-review/pull/3268) |
| ALDH7A1 | Definitive | IN_PROGRESS | Review merged; final-head approval and required CI passed; all 18 scoped merged blobs verified | `cmungall/clingen-aldh7a1` | [#3277](https://github.com/ai4curation/ai-gene-review/pull/3277) |
| ALDOB | Definitive | INITIALIZED | Review #3279 merged; exact-head approval and required CI passed; all 16 scoped merged blobs verified | `cmungall/clingen-aldob` | [#3279](https://github.com/ai4curation/ai-gene-review/pull/3279) |
| ALG1 | Definitive | INITIALIZED | Review merged; final-head approval and required CI passed; all 12 scoped merged blobs verified | `cmungall/clingen-alg1` | [#3280](https://github.com/ai4curation/ai-gene-review/pull/3280) |
| ALG12 | Definitive | INITIALIZED | Review #3281 merged; exact-head approval and required CI passed; all 10 scoped merged blobs verified | `cmungall/clingen-alg12` | [#3281](https://github.com/ai4curation/ai-gene-review/pull/3281) |
| ALG13 | Definitive | INITIALIZED | Review merged; final-head approval and required CI passed; all 9 scoped merged blobs verified | `cmungall/clingen-alg13` | [#3282](https://github.com/ai4curation/ai-gene-review/pull/3282) |
| ALG3 | Definitive | INITIALIZED | Review merged; final-head approval and required CI passed; all 12 scoped merged blobs verified | `cmungall/clingen-alg3` | [#3283](https://github.com/ai4curation/ai-gene-review/pull/3283) |
| ABCG5 | Definitive | No review | Review merged; final-head approval and required CI passed; all 28 scoped merged blobs verified | `cmungall/clingen-abcg5` | [#3285](https://github.com/ai4curation/ai-gene-review/pull/3285) |
| ABCG8 | Definitive | No review | Review #3284 merged; exact-head approval and required CI passed; all 24 scoped merged blobs verified | `cmungall/clingen-abcg8` | [#3284](https://github.com/ai4curation/ai-gene-review/pull/3284) |
| ABHD12 | Definitive | No review | Review #3286 merged; exact-head approval and required CI passed; all 24 scoped merged blobs verified | `cmungall/clingen-abhd12` | [#3286](https://github.com/ai4curation/ai-gene-review/pull/3286) |
| ABHD5 | Definitive | No review | Review merged; final-head approval and required CI passed; all 15 scoped merged blobs verified | `cmungall/clingen-abhd5` | [#3287](https://github.com/ai4curation/ai-gene-review/pull/3287) |
| AICDA | Definitive | No review | Review #3290 merged; exact-head approval and required CI passed; all 27 scoped merged blobs verified | `cmungall/clingen-aicda` | [#3290](https://github.com/ai4curation/ai-gene-review/pull/3290) |
| AGTPBP1 | Definitive | No review | Review merged; final-head approval and required CI passed; all 19 scoped merged blobs verified | `cmungall/clingen-agtpbp1` | [#3292](https://github.com/ai4curation/ai-gene-review/pull/3292) |
| AIFM1 | Definitive | No review | Review #3295 merged; exact-head approval and required CI passed; all 25 scoped merged blobs verified | `cmungall/clingen-aifm1` | [#3295](https://github.com/ai4curation/ai-gene-review/pull/3295) |
| AK2 | Definitive | No review | Review #3297 merged; exact-head approval and required CI passed; all 19 scoped merged blobs verified | `cmungall/clingen-ak2` | [#3297](https://github.com/ai4curation/ai-gene-review/pull/3297) |
| ALG6 | Definitive | INITIALIZED | Review #3296 merged; exact-head approval and required CI passed; all 9 scoped merged blobs verified | `cmungall/clingen-alg6` | [#3296](https://github.com/ai4curation/ai-gene-review/pull/3296) |
| ALG8 | Definitive | INITIALIZED | Review #3298 merged; exact-head approval and required CI passed; all 10 scoped merged blobs verified | `cmungall/clingen-alg8` | [#3298](https://github.com/ai4curation/ai-gene-review/pull/3298) |
| ALG9 | Definitive | INITIALIZED | Review #3299 merged; exact-head approval and required CI passed; all 11 scoped merged blobs verified | `cmungall/clingen-alg9` | [#3299](https://github.com/ai4curation/ai-gene-review/pull/3299) |
| ALB | Definitive | No review | Review #3305 merged; current-head approval and required CI passed; all 41 scoped merged blobs verified | `cmungall/clingen-alb` | [#3305](https://github.com/ai4curation/ai-gene-review/pull/3305) |
| ALK | Definitive | INITIALIZED | Review #3316 merged; current-head approval and required CI passed; all 70 scoped merged blobs verified | `cmungall/clingen-alk` | [#3316](https://github.com/ai4curation/ai-gene-review/pull/3316) |
| ALMS1 | Definitive | INITIALIZED | Review #3318 merged; current-head approval and required CI passed; all 39 scoped merged blobs verified | `cmungall/clingen-alms1` | [#3318](https://github.com/ai4curation/ai-gene-review/pull/3318) |
| ALPK1 | Definitive | INITIALIZED | Review #3317 merged; current-head approval and required CI passed; all 29 scoped merged blobs verified | `cmungall/clingen-alpk1` | [#3317](https://github.com/ai4curation/ai-gene-review/pull/3317) |
| AMT | Definitive | INITIALIZED | Review #3315 merged; current-head approval and required CI passed; all 12 scoped merged blobs verified | `cmungall/clingen-amt` | [#3315](https://github.com/ai4curation/ai-gene-review/pull/3315) |
| ALPK3 | Definitive | INITIALIZED | Review #3325 merged; current-head approval and required CI passed; all 18 scoped merged blobs verified | `cmungall/clingen-alpk3` | [#3325](https://github.com/ai4curation/ai-gene-review/pull/3325) |
| ALPL | Definitive | COMPLETE | Review #3320 merged; current-head approval and required CI passed; all 47 scoped merged blobs verified | `cmungall/clingen-alpl` | [#3320](https://github.com/ai4curation/ai-gene-review/pull/3320) |
| ALX3 | Definitive | INITIALIZED | Review #3324 merged; current-head approval and required CI passed; all 13 scoped merged blobs verified | `cmungall/clingen-alx3` | [#3324](https://github.com/ai4curation/ai-gene-review/pull/3324) |
| ALS2 | Definitive | INITIALIZED | Review #3326 merged; current-head approval and required CI passed; all 23 scoped merged blobs verified | `cmungall/clingen-als2` | [#3326](https://github.com/ai4curation/ai-gene-review/pull/3326) |
| ALX1 | Definitive | INITIALIZED | Review #3327 merged; current-head approval and required CI passed; all 21 scoped merged blobs verified | `cmungall/clingen-alx1` | [#3327](https://github.com/ai4curation/ai-gene-review/pull/3327) |
| ALX4 | Definitive | INITIALIZED | Review #3328 merged; current-head approval and required CI passed; all 19 scoped merged blobs verified | `cmungall/clingen-alx4` | [#3328](https://github.com/ai4curation/ai-gene-review/pull/3328) |
| AMER1 | Definitive | INITIALIZED | Review #3329 merged; current-head approval and required CI passed; all 42 scoped merged blobs verified | `cmungall/clingen-amer1` | [#3329](https://github.com/ai4curation/ai-gene-review/pull/3329) |
| ANK1 | Definitive | INITIALIZED | Review #3332 merged; current-head approval and required CI passed; all 31 scoped merged blobs verified | `cmungall/clingen-ank1` | [#3332](https://github.com/ai4curation/ai-gene-review/pull/3332) |
| ANGPTL3 | Definitive | INITIALIZED | Review #3336 merged; current-head approval and required CI passed; all 18 scoped merged blobs verified | `cmungall/clingen-angptl3` | [#3336](https://github.com/ai4curation/ai-gene-review/pull/3336) |
| ANK2 | Definitive | INITIALIZED | Review #3338 merged; current-head approval and required CI passed; all 30 scoped merged blobs verified | `cmungall/clingen-ank2` | [#3338](https://github.com/ai4curation/ai-gene-review/pull/3338) |
| ANKRD11 | Definitive | INITIALIZED | Review #3337 merged; current-head approval and required CI passed; all 14 scoped merged blobs verified | `cmungall/clingen-ankrd11` | [#3337](https://github.com/ai4curation/ai-gene-review/pull/3337) |
| ANKRD17 | Definitive | INITIALIZED | Review #3340 merged; current-head approval and required CI passed; all 14 scoped merged blobs verified | `cmungall/clingen-ankrd17` | [#3340](https://github.com/ai4curation/ai-gene-review/pull/3340) |
| ANKRD26 | Definitive | INITIALIZED | Review #3339 merged; current-head approval and required CI passed; all 13 scoped merged blobs verified | `cmungall/clingen-ankrd26` | [#3339](https://github.com/ai4curation/ai-gene-review/pull/3339) |
| ANKS6 | Definitive | COMPLETE | Review #3343 merged; current-head approval and required CI passed; all 16 scoped merged blobs verified | `cmungall/clingen-anks6` | [#3343](https://github.com/ai4curation/ai-gene-review/pull/3343) |
| ANO10 | Definitive | INITIALIZED | Review #3347 merged; current-head approval and required CI passed; all 17 scoped merged blobs verified | `cmungall/clingen-ano10` | [#3347](https://github.com/ai4curation/ai-gene-review/pull/3347) |
| ANO5 | Definitive | INITIALIZED | Review #3349 merged; current-head approval and required CI passed; all 24 scoped merged blobs verified | `cmungall/clingen-ano5` | [#3349](https://github.com/ai4curation/ai-gene-review/pull/3349) |
| ANOS1 | Definitive | INITIALIZED | Review #3350 merged; current-head approval and required CI passed; all 15 scoped merged blobs verified | `cmungall/clingen-anos1` | [#3350](https://github.com/ai4curation/ai-gene-review/pull/3350) |
| ANTXR1 | Definitive | INITIALIZED | Review #3351 merged; current-head approval and required CI passed; all 22 scoped merged blobs verified | `cmungall/clingen-antxr1` | [#3351](https://github.com/ai4curation/ai-gene-review/pull/3351) |
| ANTXR2 | Definitive | INITIALIZED | Review #3352 merged; current-head approval and required CI passed; all 26 scoped merged blobs verified | `cmungall/clingen-antxr2` | [#3352](https://github.com/ai4curation/ai-gene-review/pull/3352) |
| ANXA11 | Definitive | INITIALIZED | Review #3353 merged; current-head approval and required CI passed; all 35 scoped merged blobs verified | `cmungall/clingen-anxa11` | [#3353](https://github.com/ai4curation/ai-gene-review/pull/3353) |
| AP4E1 | Definitive | INITIALIZED | Review #3354 merged; current-head approval and required CI passed; all 20 scoped merged blobs verified | `cmungall/clingen-ap4e1` | [#3354](https://github.com/ai4curation/ai-gene-review/pull/3354) |
| AP5Z1 | Definitive | INITIALIZED | Review #3355 merged; current-head approval and required CI passed; all 16 scoped merged blobs verified | `cmungall/clingen-ap5z1` | [#3355](https://github.com/ai4curation/ai-gene-review/pull/3355) |
| AP1G1 | Definitive | INITIALIZED | Review #3357 merged; current-head approval and required CI passed; all 47 scoped merged blobs verified | `cmungall/clingen-ap1g1` | [#3357](https://github.com/ai4curation/ai-gene-review/pull/3357) |
| AP2M1 | Definitive | INITIALIZED | Review #3358 merged; current-head approval and required CI passed; all 104 scoped merged blobs verified | `cmungall/clingen-ap2m1` | [#3358](https://github.com/ai4curation/ai-gene-review/pull/3358) |
| APC2 | Strong | INITIALIZED | Review #3359 merged; current-head approval and required CI passed; all 21 scoped merged blobs verified | `cmungall/clingen-apc2` | [#3359](https://github.com/ai4curation/ai-gene-review/pull/3359) |
| APC | Definitive | INITIALIZED | Review #3360 merged; current-head approval and required CI passed; all 122 scoped merged blobs verified | `cmungall/clingen-apc` | [#3360](https://github.com/ai4curation/ai-gene-review/pull/3360) |
| ARG1 | Definitive | COMPLETE | Review #3361 merged; current-head approval and required CI passed; all 22 scoped merged blobs verified | `cmungall/clingen-arg1` | [#3361](https://github.com/ai4curation/ai-gene-review/pull/3361) |
| APOL1 | Definitive | INITIALIZED | Review #3363 merged; current-head approval and required CI passed; all 18 scoped merged blobs verified | `cmungall/clingen-apol1` | [#3363](https://github.com/ai4curation/ai-gene-review/pull/3363) |
| ARHGAP29 | Definitive | INITIALIZED | Review #3362 merged; current-head approval and required CI passed; all 17 scoped merged blobs verified | `cmungall/clingen-arhgap29` | [#3362](https://github.com/ai4curation/ai-gene-review/pull/3362) |
| APOB | Definitive | INITIALIZED | Review #3365 merged at 2026-10-03 02:24:02 UTC; final-head approval and required CI passed; 107 explicitly scoped files and 52 complete PR diff paths verified. Biological YAML remains COMPLETE, with 158 annotations and 33 UNDECIDED judgments. | `cmungall/clingen-apob` | [#3365](https://github.com/ai4curation/ai-gene-review/pull/3365) |
| AR | Definitive | INITIALIZED | Review #3364 merged; current-head approval and required CI passed; all 114 scoped merged blobs verified | `cmungall/clingen-ar` | [#3364](https://github.com/ai4curation/ai-gene-review/pull/3364) |
| ARHGEF9 | Definitive | INITIALIZED | Review #3366 merged; current-head approval and required CI passed; all 19 scoped merged blobs verified | `cmungall/clingen-arhgef9` | [#3366](https://github.com/ai4curation/ai-gene-review/pull/3366) |
| ARID1A | Definitive | INITIALIZED | Review #3367 merged; current-head approval and required CI passed; all 53 scoped merged blobs verified | `cmungall/clingen-arid1a` | [#3367](https://github.com/ai4curation/ai-gene-review/pull/3367) |
| ARID1B | Definitive | INITIALIZED | Review #3370 merged; current-head approval and required CI passed; all 35 scoped merged blobs verified | `cmungall/clingen-arid1b` | [#3370](https://github.com/ai4curation/ai-gene-review/pull/3370) |
| ARID2 | Definitive | INITIALIZED | Review #3372 merged at 2026-10-02 21:50:40 UTC; final-head approval and required CI passed; all 37 scoped merged blobs and 15 PR paths verified. Biological YAML remains COMPLETE independently of campaign completion. | `cmungall/clingen-arid2` | [#3372](https://github.com/ai4curation/ai-gene-review/pull/3372) |
| ARMC2 | Definitive | INITIALIZED | Review #3369 merged; current-head approval and required CI passed; all 11 scoped merged blobs verified | `cmungall/clingen-armc2` | [#3369](https://github.com/ai4curation/ai-gene-review/pull/3369) |
| ARMC9 | Definitive | INITIALIZED | Review #3371 merged at 2026-10-02 20:57:05 UTC; final-head approval and required CI passed; all 14 scoped merged blobs and 11 PR paths verified. Biological YAML remains COMPLETE independently of campaign completion. | `cmungall/clingen-armc9` | [#3371](https://github.com/ai4curation/ai-gene-review/pull/3371) |
| ARL13B | Definitive | INITIALIZED | Review #3374 merged at 2026-10-02 20:57:23 UTC; final-head approval and required CI passed; all 32 scoped merged blobs and 18 PR paths verified. Biological YAML remains COMPLETE independently of campaign completion. | `cmungall/clingen-arl13b` | [#3374](https://github.com/ai4curation/ai-gene-review/pull/3374) |
| ARL2BP | Definitive | INITIALIZED | Review #3373 merged; current-head approval and required CI passed; all 33 scoped merged blobs verified | `cmungall/clingen-arl2bp` | [#3373](https://github.com/ai4curation/ai-gene-review/pull/3373) |
| ARPC1B | Definitive | INITIALIZED | Review #3378 merged; current-head approval and required CI passed; all 27 scoped merged blobs verified | `cmungall/clingen-arpc1b` | [#3378](https://github.com/ai4curation/ai-gene-review/pull/3378) |
| ARSA | Definitive | PREEXISTING_REVIEW_AUGMENTED | Review #3376 merged; current-head approval and required CI passed; all 31 scoped merged blobs verified | `cmungall/clingen-arsa` | [#3376](https://github.com/ai4curation/ai-gene-review/pull/3376) |
| ARSB | Definitive | PREEXISTING_REVIEW_AUGMENTED | Review #3379 merged; current-head approval and required CI passed; all 30 scoped merged blobs verified | `cmungall/clingen-arsb` | [#3379](https://github.com/ai4curation/ai-gene-review/pull/3379) |
| ARSL | Definitive | NORMAL_PENDING_SEED_REVIEWED | Review #3382 merged; current-head approval and required CI passed; all 13 scoped merged blobs verified | `cmungall/clingen-arsl` | [#3382](https://github.com/ai4curation/ai-gene-review/pull/3382) |
| ARX | Definitive | NORMAL_PENDING_SEED_REVIEWED | Review #3384 merged; current-head approval and required CI passed; all 19 scoped merged blobs verified | `cmungall/clingen-arx` | [#3384](https://github.com/ai4curation/ai-gene-review/pull/3384) |
| ASAH1 | Definitive | PREEXISTING_REVIEW_AUGMENTED | Review #3383 merged; current-head approval and required CI passed; all 32 scoped merged blobs verified | `cmungall/clingen-asah1` | [#3383](https://github.com/ai4curation/ai-gene-review/pull/3383) |
| ASL | Definitive | PREEXISTING_REVIEW_AUGMENTED | Review #3385 merged at 2026-10-02 20:57:44 UTC; final-head approval and required CI passed; all 25 scoped merged blobs and 8 PR paths verified. Biological YAML remains COMPLETE independently of campaign completion. | `cmungall/clingen-asl` | [#3385](https://github.com/ai4curation/ai-gene-review/pull/3385) |
| ASH1L | Definitive | NORMAL_PENDING_SEED_REVIEWED | Review #3387 merged; current-head approval and required CI passed; all 17 scoped merged blobs verified | `cmungall/clingen-ash1l` | [#3387](https://github.com/ai4curation/ai-gene-review/pull/3387) |
| ASNS | Definitive | NORMAL_PENDING_SEED_REVIEWED | Review #3438 merged at 2026-10-02 20:57:57 UTC; final-head approval and required CI passed; all 20 scoped merged blobs and 16 PR paths verified. Biological YAML remains COMPLETE independently of campaign completion. | `cmungall/clingen-asns` | [#3438](https://github.com/ai4curation/ai-gene-review/pull/3438) |
| ASPA | Definitive | NORMAL_PENDING_SEED_REVIEWED | Review #3440 merged; current-head approval and required CI passed; all 25 scoped merged blobs verified | `cmungall/clingen-aspa` | [#3440](https://github.com/ai4curation/ai-gene-review/pull/3440) |
| ASS1 | Definitive | DRAFT (existing authored review) | Review #3473 merged; current-head approval and required CI passed; all 35 scoped merged blobs verified; published YAML is COMPLETE; original merge receipt DRAFT metadata is a documented discrepancy | `cmungall/clingen-ass1` | [#3473](https://github.com/ai4curation/ai-gene-review/pull/3473) |
| ASPM | Definitive | ABSENT | Review #3501 merged; current-head approval and required CI passed; all 14 scoped merged blobs verified | `cmungall/clingen-aspm` | [#3501](https://github.com/ai4curation/ai-gene-review/pull/3501) |
| ASXL1 | Definitive | ABSENT | Review #3526 merged; current-head approval and required CI passed; all 23 scoped merged blobs verified; biological YAML remains DRAFT with three documented generic-binding advisories | `cmungall/clingen-asxl1` | [#3526](https://github.com/ai4curation/ai-gene-review/pull/3526) |
| ASXL2 | Definitive | ABSENT | Review #3539 merged; current-head approval and required CI passed; all 16 scoped merged blobs verified; published YAML is COMPLETE; original merge receipt DRAFT metadata is a documented discrepancy | `cmungall/clingen-asxl2` | [#3539](https://github.com/ai4curation/ai-gene-review/pull/3539) |
| ATF6 | Definitive | ABSENT | Review #3536 merged; current-head approval and required CI passed; all 39 scoped merged blobs verified; published YAML is COMPLETE; original merge receipt DRAFT metadata is a documented discrepancy | `cmungall/clingen-atf6` | [#3536](https://github.com/ai4curation/ai-gene-review/pull/3536) |
| ASXL3 | Definitive | ABSENT | Review #3543 merged; current-head approval and required CI passed; all 12 scoped merged blobs verified | `cmungall/clingen-asxl3` | [#3543](https://github.com/ai4curation/ai-gene-review/pull/3543) |
| ATL1 | Definitive | ABSENT | Review #3545 merged; current-head approval and required CI passed; all 22 scoped merged blobs verified | `cmungall/clingen-atl1` | [#3545](https://github.com/ai4curation/ai-gene-review/pull/3545) |
| ATM | Definitive | ABSENT | Review #3547 merged; current-head approval and required CI passed; all 187 scoped merged blobs verified | `cmungall/clingen-atm` | [#3547](https://github.com/ai4curation/ai-gene-review/pull/3547) |
| ATP6AP2 | Definitive | Existing review audited | Review #3548 merged; current-head approval and required CI passed; all 28 scoped merged blobs verified | `cmungall/clingen-atp6ap2` | [#3548](https://github.com/ai4curation/ai-gene-review/pull/3548) |
| ATN1 | Definitive | Newly seeded | Review #3549 merged; current-head approval and required CI passed; all 23 scoped merged blobs verified | `cmungall/clingen-atn1` | [#3549](https://github.com/ai4curation/ai-gene-review/pull/3549) |
| ATP13A2 | Definitive | Newly seeded | Review #3552 merged; current-head approval and required CI passed; all 38 scoped merged blobs verified | `cmungall/clingen-atp13a2` | [#3552](https://github.com/ai4curation/ai-gene-review/pull/3552) |
| ATP1A1 | Definitive | Newly seeded | Review #3553 merged at 2026-10-02 19:44:22 UTC; final-head approval and required CI passed; all 49 scoped merged blobs and 35 PR paths verified. Biological YAML remains DRAFT independently of campaign completion. | `cmungall/clingen-atp1a1` | [#3553](https://github.com/ai4curation/ai-gene-review/pull/3553) |
| ATP6AP1 | Definitive | Existing review audited | Review #3550 merged at 2026-10-02 20:58:10 UTC; final-head approval and required CI passed; all 30 scoped merged blobs and 8 PR paths verified. Biological YAML remains DRAFT independently of campaign completion. | `cmungall/clingen-atp6ap1` | [#3550](https://github.com/ai4curation/ai-gene-review/pull/3550) |
| ATP6V0A2 | Definitive | Existing review audited | Review #3551 merged at 2026-10-02 22:19:51 UTC; final-head approval and required CI passed; 27 explicitly scoped merged blobs and 12 complete PR diff paths verified. Biological YAML remains DRAFT, with 5 UNDECIDED judgments preserved. | `cmungall/clingen-atp6v0a2` | [#3551](https://github.com/ai4curation/ai-gene-review/pull/3551) |
| ATP1A2 | Definitive | Newly seeded | Review #3558 merged; current-head approval and required CI passed; all 26 scoped merged blobs verified | `cmungall/clingen-atp1a2` | [#3558](https://github.com/ai4curation/ai-gene-review/pull/3558) |
| ATP1A3 | Definitive | Newly seeded | Review #3555 merged; current-head approval and required CI passed; all 20 scoped merged blobs verified | `cmungall/clingen-atp1a3` | [#3555](https://github.com/ai4curation/ai-gene-review/pull/3555) |
| ATP2B2 | Definitive | Newly seeded | Review #3554 merged; current-head approval and required CI passed; all 24 scoped merged blobs verified | `cmungall/clingen-atp2b2` | [#3554](https://github.com/ai4curation/ai-gene-review/pull/3554) |
| ATP6V1B1 | Definitive | Existing review audited | Review #3556 merged; current-head approval and required CI passed; all 36 scoped merged blobs verified | `cmungall/clingen-atp6v1b1` | [#3556](https://github.com/ai4curation/ai-gene-review/pull/3556) |
| ATP13A3 | Definitive | Newly seeded | Review #3559 merged; current-head approval and required CI passed; all 12 scoped merged blobs verified | `cmungall/clingen-atp13a3` | [#3559](https://github.com/ai4curation/ai-gene-review/pull/3559) |
| ATP7B | Definitive | Existing review audited | Review #3560 merged at 2026-10-02 23:37:41 UTC; final-head approval and required CI passed; 35 explicitly scoped merged blobs and 9 complete PR diff paths verified. Biological YAML remains DRAFT, with 3 UNDECIDED judgments preserved. | `cmungall/clingen-atp7b` | [#3560](https://github.com/ai4curation/ai-gene-review/pull/3560) |
| ATP7A | Definitive | Newly seeded | Review #3561 merged at 2026-10-02 22:18:02 UTC; final-head approval and required CI passed; 35 explicitly scoped merged blobs and 31 complete PR diff paths verified. Biological YAML remains DRAFT, with 8 UNDECIDED judgments preserved. | `cmungall/clingen-atp7a` | [#3561](https://github.com/ai4curation/ai-gene-review/pull/3561) |
| ATP8A2 | Definitive | Newly seeded | Review #3562 merged; current-head approval and required CI passed; all 17 scoped merged blobs verified | `cmungall/clingen-atp8a2` | [#3562](https://github.com/ai4curation/ai-gene-review/pull/3562) |
| B3GALNT2 | Definitive | Existing review | Review #3563 merged at 2026-10-03 01:55:18 UTC; final-head approval and required CI passed; 16 explicitly scoped files and 6 complete PR diff paths verified. Biological YAML remains DRAFT, with 16 annotations and 1 UNDECIDED judgments. | `cmungall/clingen-b3galnt2` | [#3563](https://github.com/ai4curation/ai-gene-review/pull/3563) |
| ATRX | Definitive | Not started | Review #3564 merged; current-head approval and required CI passed; all 41 scoped merged blobs verified | `cmungall/clingen-atrx` | [#3564](https://github.com/ai4curation/ai-gene-review/pull/3564) |
| ATXN2 | Definitive | Not started | Review #3566 merged at 2026-10-02 22:21:54 UTC; final-head approval and required CI passed; 34 explicitly scoped merged blobs and 21 complete PR diff paths verified. Biological YAML remains DRAFT, with 9 UNDECIDED judgments preserved. | `cmungall/clingen-atxn2` | [#3566](https://github.com/ai4curation/ai-gene-review/pull/3566) |
| AUH | Definitive | Existing review | Review #3565 merged; current-head approval and required CI passed; all 17 scoped merged blobs verified | `cmungall/clingen-auh` | [#3565](https://github.com/ai4curation/ai-gene-review/pull/3565) |
| AURKC | Definitive | Not started | Review #3568 merged at 2026-10-02 21:31:27 UTC; final-head approval and required CI passed; all 24 scoped merged blobs and 19 PR paths verified. Biological YAML remains DRAFT independently of campaign completion. | `cmungall/clingen-aurkc` | [#3568](https://github.com/ai4curation/ai-gene-review/pull/3568) |
| AUTS2 | Definitive | Not started | Review #3569 merged at 2026-10-02 21:35:42 UTC; final-head approval and required CI passed; all 17 scoped merged blobs and 12 PR paths verified. Biological YAML remains DRAFT independently of campaign completion. | `cmungall/clingen-auts2` | [#3569](https://github.com/ai4curation/ai-gene-review/pull/3569) |
| AXIN2 | Definitive | Not started | Review #3572 merged; current-head approval and required CI passed; all 48 scoped merged blobs verified | `cmungall/clingen-axin2` | [#3572](https://github.com/ai4curation/ai-gene-review/pull/3572) |
| B3GALT6 | Definitive | Not started | Review #3573 merged; current-head approval and required CI passed; all 16 scoped merged blobs verified | `cmungall/clingen-b3galt6` | [#3573](https://github.com/ai4curation/ai-gene-review/pull/3573) |
| B3GLCT | Definitive | INITIALIZED seed | Review #3575 merged; current-head approval and required CI passed; all 18 scoped merged blobs verified | `cmungall/clingen-b3glct` | [#3575](https://github.com/ai4curation/ai-gene-review/pull/3575) |
| B4GALNT1 | Definitive | Existing review | Review #3574 merged; current-head approval and required CI passed; all 16 scoped merged blobs verified | `cmungall/clingen-b4galnt1` | [#3574](https://github.com/ai4curation/ai-gene-review/pull/3574) |
| B4GALT1 | Definitive | Existing review | Review #3576 merged at 2026-10-02 12:10:43 UTC; final-head approval and required CI passed; all 50 scoped merged blobs and 11 PR paths verified. | `cmungall/clingen-b4galt1` | [#3576](https://github.com/ai4curation/ai-gene-review/pull/3576) |
| B4GALT7 | Definitive | INITIALIZED seed | Review #3577 merged; current-head approval and required CI passed; all 20 scoped merged blobs verified | `cmungall/clingen-b4galt7` | [#3577](https://github.com/ai4curation/ai-gene-review/pull/3577) |
| B9D1 | Definitive | INITIALIZED seed | Review #3579 merged at 2026-10-02 21:39:02 UTC; final-head approval and required CI passed; all 21 scoped merged blobs and 10 PR paths verified. Biological YAML remains COMPLETE independently of campaign completion. | `cmungall/clingen-b9d1` | [#3579](https://github.com/ai4curation/ai-gene-review/pull/3579) |
| BAG3 | Definitive | Existing review | Review #3578 merged at 2026-10-02 21:37:39 UTC; final-head approval and required CI passed; all 44 scoped merged blobs and 8 PR paths verified. Biological YAML remains COMPLETE independently of campaign completion. | `cmungall/clingen-bag3` | [#3578](https://github.com/ai4curation/ai-gene-review/pull/3578) |
| BAP1 | Definitive | INITIALIZED seed | Review #3580 merged at 2026-09-30T14:22:32Z; exact-head approval and required CI passed; all 40 scoped merged blobs and 23 PR paths verified. | `cmungall/clingen-bap1` | [#3580](https://github.com/ai4curation/ai-gene-review/pull/3580) |
| BARD1 | Definitive | INITIALIZED seed | Review #3584 merged at 2026-09-30T15:49:23Z; exact-head approval and required CI passed; all 107 scoped merged blobs and 16 PR paths verified. | `cmungall/clingen-bard1` | [#3584](https://github.com/ai4curation/ai-gene-review/pull/3584) |
| BBIP1 | Definitive | Existing review | Review #3581 merged at 2026-09-30T15:58:42Z; exact-head approval and required CI passed; all 20 scoped merged blobs and 7 PR paths verified. | `cmungall/clingen-bbip1` | [#3581](https://github.com/ai4curation/ai-gene-review/pull/3581) |
| BBS12 | Definitive | Existing review | Review #3588 merged at 2026-09-30T16:54:55Z; exact-head approval and required CI passed; all 18 scoped merged blobs and 8 PR paths verified. | `cmungall/clingen-bbs12` | [#3588](https://github.com/ai4curation/ai-gene-review/pull/3588) |
| BCAT2 | Definitive | Existing review | Review #3606 merged at 2026-09-30T23:38:40Z; exact-head approval and required CI passed; all 24 scoped merged blobs and 9 PR paths verified. | `cmungall/clingen-bcat2` | [#3606](https://github.com/ai4curation/ai-gene-review/pull/3606) |
| BCL11A | Definitive | INITIALIZED seed | Review #3650 merged at 2026-10-01T03:07:23Z; final-head approval and required CI passed; all 22 scoped merged blobs and 19 PR paths verified. | `cmungall/clingen-bcl11a` | [#3650](https://github.com/ai4curation/ai-gene-review/pull/3650) |
| BCKDHA | Definitive | Existing review | Review #3614 merged at 2026-10-01T03:11:14Z; final-head approval and required CI passed; all 35 scoped merged blobs and 17 PR paths verified. | `cmungall/clingen-bckdha` | [#3614](https://github.com/ai4curation/ai-gene-review/pull/3614) |
| BCKDK | Definitive | INITIALIZED seed | Review #3646 merged at 2026-10-01T05:18:33Z; final-head approval and required CI passed; all 23 scoped merged blobs and 15 PR paths verified. | `cmungall/clingen-bckdk` | [#3646](https://github.com/ai4curation/ai-gene-review/pull/3646) |
| BCL11B | Definitive | INITIALIZED seed | Review #3664 merged at 2026-10-01T06:16:11Z; final-head approval and required CI passed; all 16 scoped merged blobs and 10 PR paths verified. | `cmungall/clingen-bcl11b` | [#3664](https://github.com/ai4curation/ai-gene-review/pull/3664) |
| BEST1 | Definitive | INITIALIZED seed | Review #3718 merged at 2026-10-01T12:20:24Z; final-head approval and required CI passed; all 32 scoped merged blobs and 19 PR paths verified. | `cmungall/clingen-best1` | [#3718](https://github.com/ai4curation/ai-gene-review/pull/3718) |
| BLNK | Definitive | INITIALIZED seed | Review #3741 merged at 2026-10-01T13:49:16Z; final-head approval and required CI passed; all 24 scoped merged blobs and 12 PR paths verified. | `cmungall/clingen-blnk` | [#3741](https://github.com/ai4curation/ai-gene-review/pull/3741) |
| BICRA | Definitive | INITIALIZED seed | Review #3713 merged at 2026-10-01T17:30:00Z; final-head approval and required CI passed; all 16 scoped merged blobs and 11 PR paths verified. | `cmungall/clingen-bicra` | [#3713](https://github.com/ai4curation/ai-gene-review/pull/3713) |
| BLTP1 | Definitive | INITIALIZED seed | Review #3796 merged at 2026-10-01T19:21:16Z; final-head approval and required CI passed; all 16 scoped merged blobs and 15 PR paths verified. | `cmungall/clingen-bltp1` | [#3796](https://github.com/ai4curation/ai-gene-review/pull/3796) |
| BLVRA | Moderate | INITIALIZED seed | Review #3775 merged at 2026-10-01T20:08:37Z; final-head approval and required CI passed; all 21 scoped merged blobs and 6 PR paths verified. | `cmungall/clingen-blvra` | [#3775](https://github.com/ai4curation/ai-gene-review/pull/3775) |
| BLOC1S5 | Definitive | INITIALIZED seed | Review #3781 merged at 2026-10-01T20:37:09Z; final-head approval and required CI passed; all 20 scoped merged blobs and 10 PR paths verified. | `cmungall/clingen-bloc1s5` | [#3781](https://github.com/ai4curation/ai-gene-review/pull/3781) |
| BLOC1S6 | Definitive | INITIALIZED seed | Review #3770 merged at 2026-10-01T20:46:03Z; final-head approval and required CI passed; all 36 scoped merged blobs and 23 PR paths verified. | `cmungall/clingen-bloc1s6` | [#3770](https://github.com/ai4curation/ai-gene-review/pull/3770) |
| BMPR1A | Definitive | INITIALIZED seed | Review #3854 merged at 2026-10-02 16:24:25 UTC; final-head approval and required CI passed; all 47 scoped merged blobs and 45 PR paths verified. Biological YAML remains DRAFT independently of campaign completion. | `cmungall/clingen-bmpr1a` | [#3854](https://github.com/ai4curation/ai-gene-review/pull/3854) |
| BMP6 | Limited | INITIALIZED seed | Review #3852 merged at 2026-10-02 17:42:12 UTC; final-head approval and required CI passed; all 37 scoped merged blobs and 34 PR paths verified. Biological YAML remains DRAFT independently of campaign completion. | `cmungall/clingen-bmp6` | [#3852](https://github.com/ai4curation/ai-gene-review/pull/3852) |
| BOLA3 | Definitive | COMPLETE existing review | Review #3860 merged at 2026-10-02 18:07:12 UTC; final-head approval and required CI passed; all 20 scoped merged blobs and 6 PR paths verified. Biological YAML remains COMPLETE independently of campaign completion. | `cmungall/clingen-bola3` | [#3860](https://github.com/ai4curation/ai-gene-review/pull/3860) |
| BLOC1S1 | Moderate | INITIALIZED seed | Review #3749 merged at 2026-10-02 19:42:37 UTC; final-head approval and required CI passed; all 24 scoped merged blobs and 10 PR paths verified. Biological YAML remains COMPLETE independently of campaign completion. | `cmungall/clingen-bloc1s1` | [#3749](https://github.com/ai4curation/ai-gene-review/pull/3749) |
| BLOC1S3 | Moderate | INITIALIZED seed | Review #3758 merged at 2026-10-02 21:40:19 UTC; final-head approval and required CI passed; all 16 scoped merged blobs and 9 PR paths verified. Biological YAML remains COMPLETE independently of campaign completion. | `cmungall/clingen-bloc1s3` | [#3758](https://github.com/ai4curation/ai-gene-review/pull/3758) |
| BMP10 | Limited | INITIALIZED seed | Review #3818 merged at 2026-10-02 21:41:37 UTC; final-head approval and required CI passed; all 22 scoped merged blobs and 21 PR paths verified. Biological YAML remains DRAFT independently of campaign completion. | `cmungall/clingen-bmp10` | [#3818](https://github.com/ai4curation/ai-gene-review/pull/3818) |
| BMP4 | Definitive | INITIALIZED seed | Review #3851 merged at 2026-10-02 21:43:03 UTC; final-head approval and required CI passed; all 62 scoped merged blobs and 44 PR paths verified. Biological YAML remains DRAFT independently of campaign completion. | `cmungall/clingen-bmp4` | [#3851](https://github.com/ai4curation/ai-gene-review/pull/3851) |
| BMPR2 | Definitive | INITIALIZED seed | Review #3878 merged at 2026-10-03 01:13:18 UTC; final-head approval and required CI passed; 43 explicitly scoped merged files and 15 complete PR diff paths verified. Biological YAML is COMPLETE, with 152 annotations and 38 UNDECIDED judgments preserved. | `cmungall/clingen-bmpr2` | [#3878](https://github.com/ai4curation/ai-gene-review/pull/3878) |
| BPTF | Definitive | INITIALIZED seed | Review #3880 merged at 2026-10-03 04:40:38 UTC; final-head approval and required CI passed; 28 explicitly scoped files and 24 complete PR diff paths verified. Biological YAML remains DRAFT: 45 source assertions plus one NEW H3K4me3-reader assertion, with three UNDECIDED judgments preserved. | `cmungall/clingen-bptf` | [#3880](https://github.com/ai4curation/ai-gene-review/pull/3880) |
| BRAT1 | Definitive | INITIALIZED seed | Review #3884 merged at 2026-10-03 05:43:10 UTC after final-head approval and required CI success; 17 paths verified at that merge commit, 10 PR diff paths. Status-only #3892 merged at 07:20:29 UTC, correcting COMPLETE to DRAFT with 18 paths verified and four PR diff paths; zero additional gene completion. All 41 source assertions, three alternative_products and six UNDECIDED judgments remain; contextual mitochondrial-localization over-annotation is unchanged. | `cmungall/clingen-brat1` | [#3884](https://github.com/ai4curation/ai-gene-review/pull/3884), [#3892](https://github.com/ai4curation/ai-gene-review/pull/3892) |
| BRCA1 | Definitive | COMPLETE existing review | Review #3888 merged at 2026-10-03 07:14:38 UTC after final-head approval and required CI success; 177 paths verified at that merge commit, five PR diff paths. Biological YAML is DRAFT with all 275 source assertions assessed, 26 UNDECIDED, no NEW and three cores. Eight named UniProt products are discussed in notes; the structured alternative_products slot remains absent. | `cmungall/clingen-brca1` | [#3888](https://github.com/ai4curation/ai-gene-review/pull/3888) |
| BRCA2 | Definitive | Existing review audited | PR #3893 merged at 2026-10-03 09:08:30 UTC after exact-head approval and required CI success. Six paths verified at the merge commit: three gene outputs and three histories. Biological DRAFT, 149 source assertions, 27 UNDECIDED, no NEW and two cores remain; campaign closure does not resolve evidence gaps. | `cmungall/clingen-brca2` | [#3893](https://github.com/ai4curation/ai-gene-review/pull/3893) |
| BRIP1 | Definitive | Existing review audited | PR #3895 merged at 2026-10-03 10:26:05 UTC after exact-head approval and required CI success. Six gene/history paths verified. Biological DRAFT, 92 source assertions, three UNDECIDED, three cores and two alternative products remain; campaign closure does not resolve the open crosslink-response step. | `cmungall/clingen-brip1` | [#3895](https://github.com/ai4curation/ai-gene-review/pull/3895) |
| BRD4 | Definitive | INITIALIZED normal seed | PR #3896 merged at 2026-10-03 10:42:33 UTC after exact-head approval and required CI success; 31 added paths verified. Biological DRAFT with 81 source assertions, 13 UNDECIDED, 40 references, three products, two cores and 21 warnings remains. Catalytic and individual-mark uncertainties are not resolved by campaign closure. | `cmungall/clingen-brd4` | [#3896](https://github.com/ai4curation/ai-gene-review/pull/3896) |
| BRPF1 | Definitive | No review | PR #3898 merged at 2026-10-03 10:55:34 UTC; 9 exact changed paths verified at the merge commit. Biological COMPLETE retains four UNDECIDED source assessments, 36 source assertions, four alternative products and two cores; no uncertainty is resolved merely by campaign closure. | `cmungall/clingen-brpf1` | [#3898](https://github.com/ai4curation/ai-gene-review/pull/3898) |
| BRSK2 | Definitive | INITIALIZED normal seed | PR #3899 merged at 2026-10-03 11:10:19 UTC; 14 exact changed paths verified at the merge commit. Biological DRAFT retains nine UNDECIDED assessments, 48 source assertions, six alternative products and one catalytic core. Combined SAD A/B experimental limits remain. | `cmungall/clingen-brsk2` | [#3899](https://github.com/ai4curation/ai-gene-review/pull/3899) |
| BRWD3 | Definitive | No review | PR #3901 merged at 2026-10-03 12:32:23 UTC; 13 exact changed paths verified at the merge commit. Biological COMPLETE retains the two supplied source assertions, five alternative products and one core. The documented UniProt/normal-GOA discrepancy and species limits remain explicit. | `cmungall/clingen-brwd3` | [#3901](https://github.com/ai4curation/ai-gene-review/pull/3901) |
| BSCL2 | Definitive | No review | PR #3902 merged at 2026-10-03 12:33:32 UTC; 17 exact changed paths verified at the merge commit. Biological DRAFT retains 30 original source assertions plus one NEW tether activity, seven UNDECIDED assessments, three alternative products and two cores. Thermogenesis and human and fly assay limits remain. | `cmungall/clingen-bscl2` | [#3902](https://github.com/ai4curation/ai-gene-review/pull/3902) |
| BSND | Definitive | INITIALIZED normal seed | PR #3903 merged at 2026-10-03 13:08:02 UTC; final-head approval and CI success verified; 16 exact changed paths verified at the merge commit. Biological DRAFT retains 52 source assertions and one channel-regulatory core; no structured products slot. Thirty-one screen-binding decisions retain explicit curator-deference and uninspected target-assay limits. Barttin is the auxiliary subunit, not the channel pore. | `cmungall/clingen-bsnd` | [#3903](https://github.com/ai4curation/ai-gene-review/pull/3903) |
| BTD | Definitive | Existing review audited (INITIALIZED) | PR #3904 merged at 2026-10-03 13:08:19 UTC; final-head approval and CI success verified; 14 exact changed paths verified at the merge commit. Biological COMPLETE retains 20 source assertions, six UNDECIDED assessments, four products and one extracellular biotin-recycling core. Fine mitochondrial localization, screen-binding and CNS-development evidence remain unresolved. | `cmungall/clingen-btd` | [#3904](https://github.com/ai4curation/ai-gene-review/pull/3904) |
| BTK | Definitive | INITIALIZED normal seed | PR #3905 merged at 2026-10-03 14:20:21 UTC; final-head approval and CI success verified; 35 exact changed paths verified at the merge commit. Biological DRAFT retains 149 source assertions, 31 UNDECIDED assessments, two products and two cores. PLC regulation is distinguished from covalent substrate phosphorylation; remaining interaction and source-access limits persist. | `cmungall/clingen-btk` | [#3905](https://github.com/ai4curation/ai-gene-review/pull/3905) |
| C19orf12 | Definitive | INITIALIZED normal seed | PR #3906 merged at 2026-10-03 14:31:06 UTC; final-head approval and CI success verified; 12 exact changed paths verified at the merge commit. Biological COMPLETE retains 22 source assertions, four products and one process core. The molecular activity remains unresolved; positive autophagy regulation and contextual apoptosis over-annotation are preserved. | `cmungall/clingen-c19orf12` | [#3906](https://github.com/ai4curation/ai-gene-review/pull/3906) |
| BUB1B | Definitive | COMPLETE existing review | PR #3908 merged at 2026-10-03 14:49:33 UTC; final-head approval and CI success verified; 10 exact changed paths verified at the merge commit. Biological DRAFT retains 119 source assertions, 11 UNDECIDED assessments, three products and two cores. Seven catalytic assertions remain disputed; supported CDC20 inhibition and kinetochore adaptor functions do not settle the kinase controversy. | `cmungall/clingen-bub1b` | [#3908](https://github.com/ai4curation/ai-gene-review/pull/3908) |
| C1QA | Definitive | INITIALIZED normal seed | PR #3909 merged at 2026-10-03 15:13:09 UTC; final-head approval and CI success verified; 34 exact changed paths verified at the merge commit. Biological DRAFT retains 83 source assertions, six UNDECIDED assessments and three cores; no structured products slot. Bibliography-only and fine synaptic/extracellular-matrix evidence limits remain. Whole-C1q contributions do not establish isolated A-chain sufficiency. | `cmungall/clingen-c1qa` | [#3909](https://github.com/ai4curation/ai-gene-review/pull/3909) |
| C1QB | Definitive | INITIALIZED normal seed | PR #3916 merged at 2026-10-03 16:18:20 UTC; final-head approval and CI success verified; 8 exact changed paths verified at the merge commit. Biological DRAFT retains 62 source assertions, six UNDECIDED assessments and three cores; no structured products slot. Fine donor localization and other source limits remain; recognition, protease recruitment and signaling are scoped to contribution within C1q. | `cmungall/clingen-c1qb` | [#3916](https://github.com/ai4curation/ai-gene-review/pull/3916) |
| C1QTNF5 | Definitive | INITIALIZED normal seed | PR #3911 merged at 2026-10-03 16:21:15 UTC; final-head approval and CI success verified; 13 exact changed paths verified at the merge commit. Biological DRAFT retains 23 source assertions, three UNDECIDED assessments and one core; no structured products slot. Collagen-stalk inference is distinguished from directly observed globular trimers, and receptor inhibition from chronic perturbation phenotypes. | `cmungall/clingen-c1qtnf5` | [#3911](https://github.com/ai4curation/ai-gene-review/pull/3911) |
| C2CD3 | Definitive | INITIALIZED normal seed | PR #3917 merged at 2026-10-03 16:41:31 UTC; final-head approval and CI success verified; 10 exact changed paths verified at the merge commit. Biological DRAFT retains 30 source assertions plus one NEW structural-function assertion, five products and one core. Human spatial/depletion evidence is separated from mouse cryo-ET context; direct microtubule affinity, ring-node composition and catalytic activity remain unestablished. | `cmungall/clingen-c2cd3` | [#3917](https://github.com/ai4curation/ai-gene-review/pull/3917) |
| C1QBP | Definitive | Existing review audited | PR #3914 merged at 2026-10-03 16:43:30 UTC; final-head approval and CI success verified; 9 exact changed paths verified at the merge commit. Biological DRAFT retains 125 source assertions, five UNDECIDED assessments and four cores; no structured products slot. Reconciled partner/donor distinctions and source-specific screen limits remain; precursor/mature localization is described without manufacturing product fields. | `cmungall/clingen-c1qbp` | [#3914](https://github.com/ai4curation/ai-gene-review/pull/3914) |
| C3 | Definitive | INITIALIZED normal seed | PR #3925 merged at 2026-10-03 18:15:29 UTC; final-head approval and CI success verified; 72 exact changed paths verified at the merge commit. Biological DRAFT retains 142 source assertions, nine UNDECIDED assessments and three cores. Four authored processed-product classes are distinct from alternative splice products. C3a versus ASP/C5L2 context and exact source access limits remain; no new annotation is introduced. | `cmungall/clingen-c3` | [#3925](https://github.com/ai4curation/ai-gene-review/pull/3925) |
| C9orf72 | Definitive | INITIALIZED normal seed | PR #3927 merged at 2026-10-03 18:25:30 UTC; final-head approval and CI success verified; 18 exact changed paths verified at the merge commit. Biological DRAFT retains 110 source assertions, 23 UNDECIDED assessments, two alternative products and three cores. Reagent-specific localization and GEF/GAP context limits remain; campaign closure does not resolve those biological uncertainties. | `cmungall/clingen-c9orf72` | [#3927](https://github.com/ai4curation/ai-gene-review/pull/3927) |
| CA5A | Definitive | INITIALIZED normal seed | PR #3928 merged at 2026-10-03 20:22:13 UTC; final-head approval and CI success verified; 19 exact changed paths verified at the merge commit. Biological COMPLETE retains 20 source assertions, 0 UNDECIDED assessments and 1 core function. No new annotation is introduced. | `cmungall/clingen-ca5a` | [#3928](https://github.com/ai4curation/ai-gene-review/pull/3928) |
| CA8 | Moderate | Existing review | PR #3929 merged at 2026-10-03 21:54:27 UTC; final-head approval and CI success verified; 7 exact changed paths verified at the merge commit. Biological DRAFT retains 26 source assertions plus 2 NEW assertions, 0 UNDECIDED assessments and 1 core function. Campaign completion preserves the merged biological assessment and its evidence limits. | `cmungall/clingen-ca8` | [#3929](https://github.com/ai4curation/ai-gene-review/pull/3929) |
| CABP2 | Definitive | INITIALIZED normal seed | PR #3938 merged at 2026-10-04 04:18:38 UTC; final-head approval and CI success verified; 12 exact changed paths verified at the merge commit. Biological DRAFT retains 49 source assertions, 1 UNDECIDED assessment and 1 core function. Campaign completion preserves the merged biological assessment and its evidence limits. | `cmungall/clingen-cabp2` | [#3938](https://github.com/ai4curation/ai-gene-review/pull/3938) |
| CACNA1B | Moderate | INITIALIZED normal seed | PR #3947 merged at 2026-10-04 04:20:41 UTC; final-head approval and CI success verified; 15 exact changed paths verified at the merge commit. Biological DRAFT retains 29 source assertions, 1 UNDECIDED assessment and 1 core function. Campaign completion preserves the merged biological assessment and its evidence limits. | `cmungall/clingen-cacna1b` | [#3947](https://github.com/ai4curation/ai-gene-review/pull/3947) |
| CACNA1D | Definitive | INITIALIZED normal seed | PR #3949 merged at 2026-10-04 04:21:48 UTC; final-head approval and CI success verified; 15 exact changed paths verified at the merge commit. Biological COMPLETE retains 78 source assertions, 6 UNDECIDED assessments and 1 core function. Campaign completion preserves the merged biological assessment and its evidence limits. | `cmungall/clingen-cacna1d` | [#3949](https://github.com/ai4curation/ai-gene-review/pull/3949) |
| CAD | Definitive | Existing review | PR #3980 merged at 2026-10-04 04:41:00 UTC; final-head approval and CI success verified; 15 exact changed paths verified at the merge commit. Biological DRAFT retains 84 source assertions, 16 UNDECIDED assessments and 3 core functions. Campaign completion preserves the merged biological assessment and its evidence limits. | `cmungall/clingen-cad` | [#3980](https://github.com/ai4curation/ai-gene-review/pull/3980) |
| CALM1 | Definitive | Existing review | PR #3989 merged at 2026-10-04 04:42:55 UTC; final-head approval and CI success verified; 5 exact changed paths verified at the merge commit. Biological DRAFT retains 176 source assertions, 8 UNDECIDED assessments and 3 core functions. Campaign completion preserves the merged biological assessment and its evidence limits. | `cmungall/clingen-calm1` | [#3989](https://github.com/ai4curation/ai-gene-review/pull/3989) |
| CACNA1E | Definitive | INITIALIZED normal seed | PR #4020 merged at 2026-10-04 06:07:21 UTC; final-head approval and CI success verified; 11 exact changed paths verified at the merge commit. Biological DRAFT retains 23 source assertions, 1 UNDECIDED assessment and 1 core function. Campaign completion preserves the merged biological assessment and its evidence limits. | `cmungall/clingen-cacna1e` | [#4020](https://github.com/ai4curation/ai-gene-review/pull/4020) |
| CACNA1G | Definitive | INITIALIZED normal seed | PR #4011 merged at 2026-10-04 06:16:13 UTC; final-head approval and CI success verified; 16 exact changed paths verified at the merge commit. Biological DRAFT retains 41 source assertions, 5 UNDECIDED assessments and 1 core function. Campaign completion preserves the merged biological assessment and its evidence limits. | `cmungall/clingen-cacna1g` | [#4011](https://github.com/ai4curation/ai-gene-review/pull/4011) |
| CALM2 | Definitive | INITIALIZED normal seed | PR #4018 merged at 2026-10-04 06:39:56 UTC; final-head approval and CI success verified; 7 exact changed paths verified at the merge commit. Biological DRAFT retains 105 source assertions, 3 UNDECIDED assessments and 3 core functions. Campaign completion preserves the merged biological assessment and its evidence limits. | `cmungall/clingen-calm2` | [#4018](https://github.com/ai4curation/ai-gene-review/pull/4018) |
| CALM3 | Definitive | Existing review | PR #4016 merged at 2026-10-04 07:07:22 UTC; final-head approval and CI success verified; 12 exact changed paths verified at the merge commit. Biological DRAFT retains 115 source assertions, 10 UNDECIDED assessments and 5 core functions. Campaign completion preserves the merged biological assessment and its evidence limits. | `cmungall/clingen-calm3` | [#4016](https://github.com/ai4curation/ai-gene-review/pull/4016) |
| CACNA2D4 | Definitive | INITIALIZED normal seed | PR #4022 merged at 2026-10-04 07:08:57 UTC; final-head approval and CI success verified; 11 exact changed paths verified at the merge commit. Biological COMPLETE retains 7 source assertions plus 1 NEW assertion, 1 UNDECIDED assessment and 1 core function. Campaign completion preserves the merged biological assessment and its evidence limits. | `cmungall/clingen-cacna2d4` | [#4022](https://github.com/ai4curation/ai-gene-review/pull/4022) |
| CACNA1C | Definitive | INITIALIZED normal seed | PR #3948 merged at 2026-10-04 07:13:11 UTC; final-head approval and CI success verified; 36 exact changed paths verified at the merge commit. Biological DRAFT retains 136 source assertions, 8 UNDECIDED assessments and 1 core function. Campaign completion preserves the merged biological assessment and its evidence limits. | `cmungall/clingen-cacna1c` | [#3948](https://github.com/ai4curation/ai-gene-review/pull/3948) |
| CACNA1F | Definitive | INITIALIZED normal seed | PR #4024 merged at 2026-10-04 07:22:48 UTC; final-head approval and CI success verified; 15 exact changed paths verified at the merge commit. Biological COMPLETE retains 24 source assertions, 4 UNDECIDED assessments and 1 core function. Campaign completion preserves the merged biological assessment and its evidence limits. | `cmungall/clingen-cacna1f` | [#4024](https://github.com/ai4curation/ai-gene-review/pull/4024) |
| CAMK2A | Definitive | Existing review | PR #4043 merged at 2026-10-04 08:21:48 UTC; final-head approval and CI success verified; 5 exact changed paths verified at the merge commit. Biological DRAFT retains 171 source assertions, 11 UNDECIDED assessments and 1 core function. Campaign completion preserves the merged biological assessment and its evidence limits. | `cmungall/clingen-camk2a` | [#4043](https://github.com/ai4curation/ai-gene-review/pull/4043) |
| CA2 | Definitive | INITIALIZED normal seed | PR #4042 merged at 2026-10-04 08:23:31 UTC; final-head approval and CI success verified; 68 exact changed paths verified at the merge commit. Biological DRAFT retains 89 source assertions, 4 UNDECIDED assessments and 1 core function. Campaign completion preserves the merged biological assessment and its evidence limits. | `cmungall/clingen-ca2` | [#4042](https://github.com/ai4curation/ai-gene-review/pull/4042) |
| CAMTA1 | Definitive | INITIALIZED normal seed | PR #4049 merged at 2026-10-04 08:47:19 UTC; final-head approval and CI success verified; 12 exact changed paths verified at the merge commit. Biological COMPLETE retains 10 source assertions, 2 UNDECIDED assessments and 1 core function. Campaign completion preserves the merged biological assessment and its evidence limits. | `cmungall/clingen-camta1` | [#4049](https://github.com/ai4curation/ai-gene-review/pull/4049) |
| CANT1 | Definitive | INITIALIZED normal seed | PR #4071 merged at 2026-10-04 10:34:22 UTC; final-head approval and CI success verified; 13 exact changed paths verified at the merge commit. Biological DRAFT retains 37 source assertions, 4 UNDECIDED assessments and 1 core function. Campaign completion preserves the merged biological assessment and its evidence limits. | `cmungall/clingen-cant1` | [#4071](https://github.com/ai4curation/ai-gene-review/pull/4071) |
| CAPN3 | Definitive | INITIALIZED normal seed | PR #4093 merged at 2026-10-04 11:36:42 UTC; final-head approval and CI success verified; 25 exact changed paths verified at the merge commit. Biological DRAFT retains 96 source assertions, 16 UNDECIDED assessments and 2 core functions. Campaign completion preserves the merged biological assessment and its evidence limits. | `cmungall/clingen-capn3` | [#4093](https://github.com/ai4curation/ai-gene-review/pull/4093) |
| CAPN5 | Definitive | INITIALIZED normal seed | PR #4099 merged at 2026-10-04 12:13:23 UTC; final-head approval and CI success verified; 16 exact changed paths verified at the merge commit. Biological DRAFT retains 14 source assertions, 4 UNDECIDED assessments and 1 core function. Campaign completion preserves the merged biological assessment and its evidence limits. | `cmungall/clingen-capn5` | [#4099](https://github.com/ai4curation/ai-gene-review/pull/4099) |
| CARD11 | Definitive | INITIALIZED normal seed | PR #4116 merged at 2026-10-04 12:47:21 UTC; final-head approval and CI success verified; 20 exact changed paths verified at the merge commit. Biological DRAFT retains 88 source assertions, 3 UNDECIDED assessments and 1 core function. Campaign completion preserves the merged biological assessment and its evidence limits. | `cmungall/clingen-card11` | [#4116](https://github.com/ai4curation/ai-gene-review/pull/4116) |
| CARMIL2 | Definitive | INITIALIZED normal seed | PR #4121 merged at 2026-10-04 14:10:18 UTC; final-head approval and CI success verified; 16 exact changed paths verified at the merge commit. Biological DRAFT retains 45 source assertions plus 1 NEW molecular-function assertion, 3 UNDECIDED assessments and 2 core functions. Campaign completion preserves the merged biological assessment and its evidence limits. | `cmungall/clingen-carmil2` | [#4121](https://github.com/ai4curation/ai-gene-review/pull/4121) |
| CASK | Definitive | INITIALIZED normal seed | PR #4132 merged at 2026-10-04T14:29:51Z; final-head approval and CI success verified; 23 changed paths and 20 reused scoped paths verified. Biological DRAFT retains 118 source assertions, 31 UNDECIDED assessments and 2 core functions. Campaign completion preserves the merged biological assessment and its evidence limits. | `cmungall/clingen-cask` | [#4132](https://github.com/ai4curation/ai-gene-review/pull/4132) |
| CASP8 | Definitive | Existing review from PR #3672 | PR #4139 merged at 2026-10-04T15:11:44Z; final-head approval and CI success verified; 6 changed paths and 128 reused scoped paths verified. Biological DRAFT retains 264 source assertions, 21 UNDECIDED assessments and 2 core functions. Campaign completion preserves the merged biological assessment and its evidence limits. This is the first campaign completion of the existing review, not a second original review. | `cmungall/clingen-casp8-whole-review` | [#4139](https://github.com/ai4curation/ai-gene-review/pull/4139) |
| CASQ2 | Definitive | INITIALIZED normal seed | PR #4142 merged at 2026-10-04T15:17:41Z; final-head approval and CI success verified; 22 changed paths and 1 reused scoped path verified. Biological DRAFT retains 57 source assertions, 12 UNDECIDED assessments and 2 core functions. Campaign completion preserves the merged biological assessment and its evidence limits. | `cmungall/clingen-casq2` | [#4142](https://github.com/ai4curation/ai-gene-review/pull/4142) |
| CASR | Definitive | INITIALIZED normal seed | PR #4147 merged at 2026-10-04T16:52:11Z; final-head approval and CI success verified; 42 changed paths and 6 reused scoped paths verified. Biological DRAFT retains 123 source assertions, 33 UNDECIDED assessments and 1 core function. Campaign completion preserves the merged biological assessment and its evidence limits. | `cmungall/clingen-casr` | [#4147](https://github.com/ai4curation/ai-gene-review/pull/4147) |
| CAV1 | Definitive | INITIALIZED normal seed | PR #4165 merged at 2026-10-04T18:27:15Z; final-head approval and CI success verified; 57 changed paths and 51 reused scoped paths verified. Biological DRAFT retains 273 source assertions, 37 UNDECIDED assessments and 3 core functions. Campaign completion preserves the merged biological assessment and its evidence limits. | `cmungall/clingen-cav1` | [#4165](https://github.com/ai4curation/ai-gene-review/pull/4165) |
| CAVIN1 | Definitive | INITIALIZED normal seed | PR #4180 merged at 2026-10-04T19:58:03Z; final-head approval and CI success verified; 12 changed paths and 13 reused scoped paths verified. Biological DRAFT retains 77 source assertions plus 1 NEW assertion, 12 UNDECIDED assessments and 2 core functions. Campaign completion preserves the merged biological assessment and its evidence limits. The one NEW assertion is GO:0070836 caveola assembly, not a molecular-function annotation. | `cmungall/clingen-cavin1` | [#4180](https://github.com/ai4curation/ai-gene-review/pull/4180) |
| CAV3 | Definitive | INITIALIZED normal seed | PR #4175 merged at 2026-10-04T20:37:20Z; final-head approval and required CI success verified; 27 changed and 9 reused scoped paths verified. Biological DRAFT retains 116 source assertions, 28 UNDECIDED assessments and 2 core functions. Campaign completion preserves the merged scientific evidence limits. | `cmungall/clingen-cav3` | [#4175](https://github.com/ai4curation/ai-gene-review/pull/4175) |
| CBS | Definitive | Existing review | PR #4191 merged at 2026-10-04T21:11:07Z; final-head approval and required CI success verified; 6 changed and 28 reused scoped paths verified. Biological DRAFT retains 101 source assertions, 12 UNDECIDED assessments and 1 core function. Campaign completion preserves the merged scientific evidence limits. | `cmungall/clingen-cbs-whole-review` | [#4191](https://github.com/ai4curation/ai-gene-review/pull/4191) |
| CBFB | Definitive | INITIALIZED normal seed | PR #4215 merged at 2026-10-04T22:33:17Z; final-head approval and required CI success verified; 86 changed and 33 reused scoped paths verified. Biological DRAFT retains 136 source assertions, 3 UNDECIDED assessments and 1 core function. Campaign completion preserves the merged scientific evidence limits. | `cmungall/clingen-cbfb` | [#4215](https://github.com/ai4curation/ai-gene-review/pull/4215) |
| CBL | Definitive | Existing review | PR #4210 merged at 2026-10-04T22:36:18Z; final-head approval and required CI success verified; 7 changed and 162 reused scoped paths verified. Biological DRAFT retains 305 source assertions plus 1 historical NEW proposal, 16 UNDECIDED assessments and 3 core functions. Campaign completion preserves the merged scientific evidence limits. The retained NEW-labelled FGFR-regulation row predates this campaign revision. | `cmungall/clingen-cbl-whole-review` | [#4210](https://github.com/ai4curation/ai-gene-review/pull/4210) |
| CCDC39 | Definitive | INITIALIZED normal seed | PR #4228 merged at 2026-10-04T23:22:31Z; final-head approval and required CI success verified; 12 changed and 2 reused scoped paths verified. Biological COMPLETE retains 30 source assertions plus 1 NEW molecular-function assertion, 5 UNDECIDED assessments and 1 core function. COMPLETE is the normal validation status and does not resolve its five UNDECIDED assessments. | `cmungall/clingen-ccdc39` | [#4228](https://github.com/ai4curation/ai-gene-review/pull/4228) |
| CC2D2A | Definitive | Existing review | PR #4209 merged at 2026-10-04T23:39:16Z; final-head approval and required CI success verified; 6 changed and 10 reused scoped paths verified. Biological DRAFT retains 19 source assertions, 0 UNDECIDED assessments and 1 core function. Its DRAFT status reflects an unused-research advisory; no annotation remains UNDECIDED. | `cmungall/clingen-cc2d2a-whole-review` | [#4209](https://github.com/ai4curation/ai-gene-review/pull/4209) |
| CC2D1A | Definitive | INITIALIZED normal seed | PR #4222 merged at 2026-10-04T23:54:43Z; final-head approval and required CI success verified; 13 changed and 8 reused scoped paths verified. Biological DRAFT retains 21 source assertions plus one NEW signaling-adaptor molecular-function assertion, 4 UNDECIDED assessments and 2 core functions. DRAFT is the validation-advisory status; campaign completion preserves the merged evidence limits. | `cmungall/clingen-cc2d1a` | [#4222](https://github.com/ai4curation/ai-gene-review/pull/4222) |
| CCDC40 | Definitive | INITIALIZED normal seed | PR #4235 merged at 2026-10-05T00:59:13Z; final-head approval and required CI success verified; 7 changed and 7 reused scoped paths verified. Biological DRAFT retains 33 source assertions, 2 UNDECIDED assessments and 1 core function. DRAFT is the validation-advisory status; campaign completion preserves the merged evidence limits. | `cmungall/clingen-ccdc40` | [#4235](https://github.com/ai4curation/ai-gene-review/pull/4235) |
| CCND2 | Definitive | INITIALIZED normal seed | PR #4244 merged at 2026-10-05T01:02:15Z; final-head approval and required CI success verified; 7 changed and 29 reused scoped paths verified. Biological DRAFT retains 77 source assertions, 3 UNDECIDED assessments and 1 core function. DRAFT is the validation-advisory status; campaign completion preserves the merged evidence limits. | `cmungall/clingen-ccnd2` | [#4244](https://github.com/ai4curation/ai-gene-review/pull/4244) |

Branches for work without a PR may exist only in a local isolated checkout.
Published check and approval states are the last verified states from this session,
not a live dashboard. ABCC6 merged through protected auto-merge on September 26
at 21:22:34 UTC. A separate checkout inside the writable workspace supports local
Git commits while the original worktree's shared Git metadata remains read-only.
Publication uses GitHub's API with expected-head guards and exact tree verification.
Direct Git transport and normal publication-source downloads still encounter DNS
failures. No local or published draft is counted as merged or complete.

The [publication queue](publication-queue.json) retains immutable publication hashes,
signed publication/file checks and append-only receipt chains. **240 of 2,876 genes
are complete**; 241 gene-level original reviews have merged, with 1 requiring a source
follow-up. The 161 dedicated full-audit PRs are the historical total at checkpoint 95;
this completion update does not refresh audit or import totals.

The table records independently verified publication and completion states. A published
source follow-up, imported normal cache, approval, successful CI and verified merge are
separate events. Earlier source-gate lists describe their historical publication time.
The original ALB PENDING seed and every prior publication/history receipt remain intact.

Checkpoint 95 uses the fixed 2026-09-30 13:59:34 UTC evidence cut. Seven publication revisions comprise B9D1’s first follow-up; BAP1’s initial audit, first follow-up and notes clarification; BBIP1’s initial audit and first follow-up; and BARD1’s initial audit. The three new audit PRs bring the total to 161. No new merge is counted: 139 complete / 140 original merges, with AKR1D1 the one pending source follow-up. BAP1 #3580 at cb70226f has exact-head approval, with required CI observed in progress. B9D1 #3579 remains on the documented generic-binding policy hold under the supplied ActionEnum. BBIP1 #3581 and BARD1 #3584 have exact-head changes requested; their subsequent scientific revisions are outside this cut. Six executed imports add 28 exact files: Seed43 primary3 and auxiliary14, Source83 one cache, Seed44 primary3 and auxiliary5, and Source84 two caches. The cumulative ledger reaches 71 import receipts / 435 creates; imports do not grant gene completion. Source85’s later observed/import lifecycle and any subsequent BAP1 merge are excluded. Earlier dated observations, the existing Seed42 zero-write disposition, seven older policy holds, six deferred import closures, and incomplete global validation remain preserved.

Completion reconciliation on 2026-10-01 UTC adds five verified merges after that cut: BAP1 #3580, BARD1 #3584, BBIP1 #3581, BBS12 #3588 and BCAT2 #3606. The saved final approvals, required CI, signed merge commits and complete scoped blob checks support 144 completed genes and 145 original merges; AKR1D1 remains the one required source follow-up. All 2,876 catalog genes and their ClinGen association text are retained. Checkpoint 95 and earlier observations remain historical records. Later open PRs, audit totals and import totals are outside this completion-only update; no fresh lifecycle polling or global validation is claimed.

Completion update at 2026-10-01 03:11:14 UTC adds BCL11A #3650 and BCKDHA #3614. Both have final-head approvals, passing required CI and signed merge commits with every scoped file verified. The count is now 146 completed genes and 147 original merges, with 2,730 genes remaining and AKR1D1 still requiring its source follow-up. Earlier completion and checkpoint observations remain historical; this update does not refresh other open PRs, audit totals or import totals.

Completion update at 2026-10-01 05:18:33 UTC adds BCKDK #3646. Its final-head approval, passing required CI and signed merge commit include verification of all 23 scoped files and 15 PR paths. The count is now 147 completed genes and 148 original merges, with 2,729 genes remaining and AKR1D1 still requiring its source follow-up. Earlier completion and checkpoint observations remain historical; this update does not refresh other open PRs, audit totals or import totals.

Completion update at 2026-10-01 06:16:11 UTC adds BCL11B #3664. Its final-head approval, passing required CI and signed merge commit include verification of all 16 scoped files and 10 PR paths. The count is now 148 completed genes and 149 original merges, with 2,728 genes remaining and AKR1D1 still requiring its source follow-up. Earlier completion and checkpoint observations remain historical; this update does not refresh other open PRs, audit totals or import totals.

Completion update at 2026-10-01 12:20:24 UTC adds BEST1 #3718. Its final-head approval, passing required CI and signed merge commit include verification of all 32 scoped files and 19 PR paths. The count is now 149 completed genes and 150 original merges, with 2,727 genes remaining and AKR1D1 still requiring its source follow-up. Earlier completion and checkpoint observations remain historical; this update does not refresh other open PRs, audit totals or import totals.

Completion update at 2026-10-01 13:49:16 UTC adds BLNK #3741. Its final-head approval, passing required CI and signed merge commit include verification of all 24 scoped files and 12 PR paths. The count is now 150 completed genes and 151 original merges, with 2,726 genes remaining and AKR1D1 still requiring its source follow-up. Earlier completion and checkpoint observations remain historical; this update does not refresh other open PRs, audit totals or import totals.

Completion update at 2026-10-01 17:30:00 UTC adds BICRA #3713. Its final-head approval, passing required CI and signed merge commit include verification of all 16 scoped files and 11 PR paths. The count is now 151 completed genes and 152 original merges, with 2,725 genes remaining and AKR1D1 still requiring its source follow-up. Earlier completion and checkpoint observations remain historical; this update does not refresh other open PRs, audit totals or import totals.

Completion update at 2026-10-01 19:21:16 UTC adds BLTP1 #3796. Its final-head approval, passing required CI and signed merge commit include verification of all 16 scoped files and 15 PR paths. The count is now 152 completed genes and 153 original merges, with 2,724 genes remaining and AKR1D1 still requiring its source follow-up. Earlier completion and checkpoint observations remain historical; this update does not refresh other open PRs, audit totals or import totals.

Completion update through 2026-10-01 20:46:03 UTC adds BLVRA #3775, BLOC1S5 #3781 and BLOC1S6 #3770. Their final-head approvals, passing required CI and signed merge commits include verification of all scoped files and complete PR path lists. The count is now 155 completed genes and 156 original merges, with 2,721 genes remaining and AKR1D1 still requiring its source follow-up. BLOC1S5 retains its biological YAML DRAFT status; its verified source-complete merge is counted separately from that field. Earlier completion and checkpoint observations remain historical; this update does not refresh other open PRs, audit totals or import totals.

Completion update through 2026-10-02 12:10:43 UTC adds B4GALT1 #3576. Its final-head approval, passing required CI and signed merge commit are confirmed with all 50 scoped files and the complete 11-path PR verified. The count is now 156 completed genes and 157 original merges, with 2,720 genes remaining and AKR1D1 still requiring its source follow-up. B4GALT1 retains its biological YAML DRAFT status independently of campaign completion. Checkpoint95 audit/import totals and prior completion observations remain historical.

Completion update through 2026-10-02 16:24:25 UTC adds BMPR1A #3854. Its final-head approval, passing required CI and signed merge commit are confirmed with all 47 scoped merged blobs and 45 PR paths verified. The count is now 157 completed genes and 158 original merges, with 2,719 genes remaining and AKR1D1 still requiring its source follow-up. BMPR1A retains its biological YAML DRAFT status independently of campaign completion. This supersedes its dated completion156 in-progress observation; all earlier checkpoint and source-import observations remain historical.

Completion update through 2026-10-02 18:07:12 UTC adds BMP6 #3852, BOLA3 #3860. Exact-head approvals, required CI success and signed merge receipts were independently confirmed by ROOT. The count is now 159 completed genes and 160 original gene PR merges, with 2,717 genes remaining and AKR1D1 still requiring its source follow-up. Biological YAML status is recorded separately from campaign completion. PANTHER family/index work is not a gene completion. Earlier completion, audit and import observations retain their dated checkpoint scope.

Completion update through 2026-10-02 19:44:22 UTC adds BLOC1S1 #3749, ATP1A1 #3553. Exact-head approvals, required CI success and signed merge receipts were independently confirmed by ROOT. The count is now 161 completed genes and 162 original gene PR merges, with 2,715 genes remaining and AKR1D1 still requiring its source follow-up. ATP1A1 retains biological YAML DRAFT status and its eight UNDECIDED source judgments; campaign completion does not assert that those evidence limits are resolved. BLOC1S1 retains biological YAML COMPLETE status. PANTHER family/index work is not a gene completion. Earlier completion, audit and import observations retain their dated checkpoint scope.

Completion update through 2026-10-02 21:50:40 UTC adds ARMC9 #3371, ARL13B #3374, ASL #3385, ASNS #3438, ATP6AP1 #3550, AURKC #3568, AUTS2 #3569, BAG3 #3578, B9D1 #3579, BLOC1S3 #3758, BMP10 #3818, BMP4 #3851, ARID2 #3372. Exact-head approvals, required CI success and signed merge receipts were independently confirmed by ROOT. The count is now 174 completed genes and 175 original gene PR merges, with 2,702 genes remaining and AKR1D1 still requiring its source follow-up. Biological YAML DRAFT status is preserved for ATP6AP1, AURKC, AUTS2, BMP10, BMP4. Campaign completion does not resolve remaining UNDECIDED evidence judgments. PANTHER family/index work is not a gene completion. Earlier completion, policy, audit and import observations retain their dated checkpoint scope.

Completion update through 2026-10-02 23:37:41 UTC adds ATP7A #3561, ATP6V0A2 #3551, ATXN2 #3566, ATP7B #3560. Exact-head approvals, required CI success and the enumerated merged blobs were independently confirmed by the coordinating ROOT agent. This internal verification is not external maintainer sign-off. The count is now 178 completed genes and 179 original gene PR merges, with 2,698 genes remaining and AKR1D1 still requiring its source follow-up. All four biological YAML records remain DRAFT; campaign completion does not resolve their UNDECIDED judgments. PANTHER and tracker infrastructure PRs contribute no gene completions. Earlier observations and checkpoint95 audit/import totals retain their dated scope.

Completion update through 2026-10-03 01:13:18 UTC adds BMPR2 #3878, independently confirmed by the coordinating ROOT agent after exact-head approval and required CI success. This internal verification is not external maintainer sign-off. The count is now 179 completed genes and 180 original gene PR merges, with 2,697 genes remaining and AKR1D1 still requiring its source follow-up. BMPR2 biological YAML is COMPLETE and preserves all 152 annotations, including 38 UNDECIDED judgments. The four earlier additions in checkpoint 178 retain their own DRAFT states and dated evidence. Campaign completion does not resolve annotation uncertainty; infrastructure PRs contribute no gene completions.

Completion update through 2026-10-03 04:40:38 UTC adds B3GALNT2 #3563, APOB #3365 and BPTF #3880. Exact-head approvals, required CI success and the enumerated merged blobs were independently confirmed by the coordinating ROOT agent; this internal verification is not external maintainer sign-off. The count is now 182 completed genes and 183 original gene PR merges, with 2,694 genes remaining and AKR1D1 still requiring its source follow-up. B3GALNT2 and BPTF retain biological YAML DRAFT status; APOB retains COMPLETE. Their 1, 3 and 33 UNDECIDED judgments, respectively, remain unchanged. BPTF has 45 source assertions plus one NEW H3K4me3-reader assertion and three alternative_products. BRAT1 remains unchecked pending a verified merge. Infrastructure PRs contribute no gene completions; earlier completion and checkpoint95 audit/import observations remain dated historical records.

Completion update through 2026-10-03 07:20:29 UTC adds BRAT1 #3884 and BRCA1 #3888, each from an approved, required-CI-passing, independently confirmed scoped merge. There are now 184 completed genes and 185 original gene PR merges, with 2,692 remaining and the AKR1D1 source follow-up still open. BRAT1 originally merged with COMPLETE; status-only #3892 subsequently corrected it to DRAFT without changing its biological assertions or adding a completion. BRCA1 also remains DRAFT. Their six and 26 UNDECIDED judgments remain unresolved. Campaign completion records merged curation work, not warning-free biological review or resolved evidence. ROOT means the internal coordinating agent, not external maintainer sign-off. Earlier dated checkpoint observations remain historical.

Completion update through 2026-10-03 09:08:30 UTC adds BRCA2 #3893 at signed merge `cb7f1f3d8d7e9745fd1d498503c9ff4af71c67e4`. The coordinating agent verified exact-head approval, required CI and six enumerated merged blobs; this is internal verification, not external maintainer sign-off. The campaign now has 185 completed genes, 186 original gene merges, one unresolved AKR1D1 source follow-up and 2,691 remaining. Biological DRAFT and all 27 UNDECIDED judgments are preserved. BRIP1 publication, BRD4 scientific peer and BRPF1 source retrieval contribute no completion increment. Earlier dated observations remain historical.

Source-limited UNDECIDED judgments remain valid. AKT1's completed Limited-tier audit
remains a scheduling exception. Project setup merged in
[#3126](https://github.com/ai4curation/ai-gene-review/pull/3126).

### Evidence scope and persistence for the completion update to 178

Local `tmp/` receipt paths and SHA-256 values in the publication queue identify session-local verification records; those files are not promised as durable repository artifacts. Durable evidence is recorded separately in each updated gene’s `durable_merge_evidence`: the approved head, merge commit/tree and exact path-to-blob map. The links below resolve the published merge commits. The reported checked scope is only that explicit map, which can include unchanged source files; the complete PR diff count is a separate measure. A source category is covered only when its paths are present in the map.

| Gene | Published merge | Explicitly checked paths | Complete PR diff paths |
|---|---|---|---:|
| ATP7A | [`dc52f85f5976`](https://github.com/ai4curation/ai-gene-review/commit/dc52f85f59768fa5bf27bc67f67fa5a65dac5fc1) | 35: 5 gene files, 3 history records, 25 publication caches, 2 Reactome caches | 31 |
| ATP6V0A2 | [`7e750322d14f`](https://github.com/ai4curation/ai-gene-review/commit/7e750322d14f7887e1fa3b73bfd9156929bb814a) | 27: 7 gene files, 4 history records, 12 publication caches, 4 Reactome caches | 12 |
| ATXN2 | [`d84235c9c95f`](https://github.com/ai4curation/ai-gene-review/commit/d84235c9c95fa130ab5b0ed765c2e706ec97f0e7) | 34: 5 gene files, 3 history records, 26 publication caches | 21 |
| ATP7B | [`66ce2256a512`](https://github.com/ai4curation/ai-gene-review/commit/66ce2256a5127a440a67e832b45c71f15e0b259d) | 35: 6 gene files, 4 history records, 23 publication caches, 2 Reactome caches | 9 |

ATXN2 has no Reactome paths in its checked map. ATP7B preserves its partner-specific COMMD1 and ATOX1 source assertions; independent corroboration does not imply that the original ATOX1 assay was read. No biological assertion or cached source is changed by this tracker update.

### BMPR2 evidence scope for completion 179

The following durable merge evidence extends the preceding checkpoint; its session-local receipts and exact checked path/blob map are retained in the new BMPR2 queue entry. The 43 checked files are not 43 annotation objects: the unchanged review has 152 annotation objects.

| Gene | Published merge | Explicitly checked paths | Complete PR diff paths |
|---|---|---|---:|
| BMPR2 | [`ecd8e02fac9c`](https://github.com/ai4curation/ai-gene-review/commit/ecd8e02fac9c236bad1d822a421d3069a8c3a465) | 43: 5 gene files, 2 history records, 27 publication caches, 9 Reactome caches | 15 |

No source, annotation, core function, product or negation was changed by this tracker update. The prior checkpoint 178 evidence, all 175 earlier queue entries and the existing checkpoint 178 history remain unchanged.

### Evidence scope for completion 182

The exact checked path/blob maps and durable merge links are recorded in the three queue entries. Session-local TMP receipts are verification records, not promised repository artifacts. Checked file counts include only their enumerated paths, and differ from complete PR diff counts and annotation counts.

| Gene | Published merge | Explicitly checked paths | Complete PR diff paths |
|---|---|---|---:|
| B3GALNT2 | [`709497a019bd`](https://github.com/ai4curation/ai-gene-review/commit/709497a019bdf6d60d31b96c42468c789cffc801) | 16: 6 gene files, 3 history records, 5 publication caches, 2 Reactome caches | 6 |
| APOB | [`e5820bd78bf5`](https://github.com/ai4curation/ai-gene-review/commit/e5820bd78bf536be8855e1acad10e02714801236) | 107: 5 gene files, 4 history records, 31 publication caches, 67 Reactome caches | 52 |
| BPTF | [`2014c5cc32fa`](https://github.com/ai4curation/ai-gene-review/commit/2014c5cc32fa60b0bd96426fc30e16132b99d49b) | 28: 5 gene files, 3 history records, 20 publication caches | 24 |

BPTF has no Reactome path in its checked map. No biological review, source, product or existing history changes in this tracker update. Earlier checkpoint records, including the unresolved AKR1D1 source follow-up, are preserved.

### Evidence scope for completion 184

New queue entries contain durable merge, tree and path/blob records. Paths below were verified at the stated merge commit; the scope does not imply that every possible gene, publication or Reactome file was checked. Prior session-local TMP proof arrays remain historical and unchanged; this checkpoint adds none to the durable queue.

| Gene or correction | Published merge | Paths verified at merge commit | Complete PR diff paths |
|---|---|---|---:|
| BRAT1 | [`071161d1f8ec`](https://github.com/ai4curation/ai-gene-review/commit/071161d1f8ecc71024d2fa696113a0d53dd4109b) | 17: 5 gene files, 2 history records, 10 publication caches | 10 |
| BRCA1 | [`bd8838fb7cdc`](https://github.com/ai4curation/ai-gene-review/commit/bd8838fb7cdc8a4e2cb7345b6b2a2db9831ea8b7) | 177: 9 gene files, 2 history records, 111 publication caches, 55 Reactome caches | 5 |
| BRAT1 status correction | [`ec5a323284fa`](https://github.com/ai4curation/ai-gene-review/commit/ec5a323284fab0e7b1d217aa0815bc99bfa0ec42) | 18: 5 gene files, 3 history records, 10 publication caches | 4 |

No gene review, source, product or prior history is changed by this tracker update.

### Evidence scope for completion 185

This checkpoint adds **one completion queue entry**, for BRCA2, plus three separate in-progress observations. The original queue `snapshot_date_utc` remains the 2026-09-27 initialization date; `latest_completion_snapshot_utc` identifies this 2026-10-03 completion evidence cut. Existing TMP proof arrays are preserved as historical records, and no new ones are added.

| Gene | Verified merge | Paths verified at that merge commit | Complete PR diff paths |
|---|---|---|---:|
| BRCA2 | [`cb7f1f3d8d7e`](https://github.com/ai4curation/ai-gene-review/commit/cb7f1f3d8d7e9745fd1d498503c9ff4af71c67e4) | Six: three gene outputs and three project-independent gene histories | 6 |

[Standard project history](https://github.com/ai4curation/ai-gene-review/blob/main/history/projects/CLINGEN_MENDELIAN/2026-10-03T091329Z-codex-9a4324.yaml). The durable queue enumerates these six path/blob pairs. This scope does not assert that all BRCA2 publication or Reactome caches were newly checked.


### Evidence scope for completion 240

[Checkpoint 240 history](https://github.com/ai4curation/ai-gene-review/blob/main/history/projects/CLINGEN_MENDELIAN/2026-10-05T014551Z-codex-fd1fdc.yaml).

The fixed **2026-10-05 01:02:15 UTC** cutoff adds **CC2D1A, CCDC40 and CCND2** to published checkpoint 237: **240 complete / 2,636 remaining**, with **241 gene-level original review merges** and one required source follow-up outstanding for AKR1D1. Tracker, source-workflow and validator PRs add no gene completions. CCM2, CCN6, CCNO and CD19 contribute none at this cutoff. External CD48 work is outside the verified campaign completion ledger.

| Gene | Verified merge | Changed / reused scoped paths | Biological assessment retained |
|---|---|---|---|
| CC2D1A | [`19c410fb456a`](https://github.com/ai4curation/ai-gene-review/commit/19c410fb456a6ba6cc2e562dace8b4c3fba93340), 2026-10-04T23:54:43Z | 13 / 8; every path/blob pair is in the queue | Biological DRAFT retains 21 source assertions plus one NEW signaling-adaptor molecular-function assertion, 4 UNDECIDED assessments and 2 core functions. DRAFT is the validation-advisory status; campaign completion preserves the merged evidence limits. |
| CCDC40 | [`91bf7fd651da`](https://github.com/ai4curation/ai-gene-review/commit/91bf7fd651da695a591326c3aa3a65cc76a16d7f), 2026-10-05T00:59:13Z | 7 / 7; every path/blob pair is in the queue | Biological DRAFT retains 33 source assertions, 2 UNDECIDED assessments and 1 core function. DRAFT is the validation-advisory status; campaign completion preserves the merged evidence limits. |
| CCND2 | [`450f063da90c`](https://github.com/ai4curation/ai-gene-review/commit/450f063da90cdfc8de24965e6974140f16d0991a), 2026-10-05T01:02:15Z | 7 / 29; every path/blob pair is in the queue | Biological DRAFT retains 77 source assertions, 3 UNDECIDED assessments and 1 core function. DRAFT is the validation-advisory status; campaign completion preserves the merged evidence limits. |

The three final PR heads have verified approval and successful required checks. Their signed merges account for **27 changed path/blob pairs** and **44 unchanged reused scope objects**, totaling **71 verified scoped objects**. These are per-review counts; shared sources can occur in several scopes. The queue enumerates both maps, identically in each new gene entry and the matching completion update.

The merged reviews retain **131 original source assertions and nine UNDECIDED assessments**, with 132 total reviewed assertions. CC2D1A adds one reviewed GO:0035591 signaling-adaptor molecular-function assertion; CCDC40 and CCND2 add no annotations. All three retain DRAFT validation status because advisories remain, independently of their retained uncertainties. Alternative-product counts are 2, 5 and 2, and core counts are 2, 1 and 1, respectively.

The published checkpoint 237 merge [`1c7db872ce45`](https://github.com/ai4curation/ai-gene-review/commit/1c7db872ce453bb8b07318df110ec4c49cce434d) remains the baseline. Its original post-merge guard stopped after an independent CD48 merge advanced main between readiness and merge. A separate signed proof verified the actual intervening parent [`edc890c57e8d`](https://github.com/ai4curation/ai-gene-review/commit/edc890c57e8d129021224a2316143165859ba687), all seven unchanged tracker preimages, all seven tracker outputs and all five source trees preserved from that actual parent. The original readiness assessment and failed guard are retained; the supplemental proof adds no gene completion and does not certify CD48 campaign completion.

All **232 existing `genes[]` queue entries** are preserved, followed by three entries. Queue-entry count is distinct from the completed-gene baseline. All 2,876 gene inventory entries and their frozen associations, the checkpoint 228 CASP8 correction, both corrected CARMIL2 reuse maps, earlier completion records and history, and the checkpoint 95 audit/import boundary remain exact.

[Published checkpoint 237 history](https://github.com/ai4curation/ai-gene-review/blob/main/history/projects/CLINGEN_MENDELIAN/2026-10-05T000032Z-codex-52d5fe.yaml).

### Evidence scope for completion 237

[Checkpoint 237 history](https://github.com/ai4curation/ai-gene-review/blob/main/history/projects/CLINGEN_MENDELIAN/2026-10-05T000032Z-codex-52d5fe.yaml).

The fixed **2026-10-04 23:39:16 UTC** cutoff adds **CAV3, CBS, CBFB, CBL, CCDC39 and CC2D2A** to published checkpoint 231: **237 complete / 2,639 remaining**, with **238 gene-level original review merges** and one required source follow-up outstanding for AKR1D1. Tracker, source-workflow and generated-page PRs add no gene completions. Reviews #4235, #4236, #4239 and #4222 contribute none at this cutoff.

| Gene | Verified merge | Changed / reused scoped paths | Biological assessment retained |
|---|---|---|---|
| CAV3 | [`530eafda0322`](https://github.com/ai4curation/ai-gene-review/commit/530eafda032262d5f322b0168bc6433d7561219b), 2026-10-04T20:37:20Z | 27 / 9; every path/blob pair is in the queue | Biological DRAFT retains 116 source assertions, 28 UNDECIDED assessments and 2 core functions. Campaign completion preserves the merged scientific evidence limits. |
| CBS | [`62791a27b3b4`](https://github.com/ai4curation/ai-gene-review/commit/62791a27b3b45f7f450eafb36a4851bc5421b460), 2026-10-04T21:11:07Z | 6 / 28; every path/blob pair is in the queue | Biological DRAFT retains 101 source assertions, 12 UNDECIDED assessments and 1 core function. Campaign completion preserves the merged scientific evidence limits. |
| CBFB | [`673823f39a4f`](https://github.com/ai4curation/ai-gene-review/commit/673823f39a4fd596b2e0fc91d506fc88ebe4f930), 2026-10-04T22:33:17Z | 86 / 33; every path/blob pair is in the queue | Biological DRAFT retains 136 source assertions, 3 UNDECIDED assessments and 1 core function. Campaign completion preserves the merged scientific evidence limits. |
| CBL | [`e4cac0ee313f`](https://github.com/ai4curation/ai-gene-review/commit/e4cac0ee313f9a079c6fd92eac9d9dcb2ef7f381), 2026-10-04T22:36:18Z | 7 / 162; every path/blob pair is in the queue | Biological DRAFT retains 305 source assertions plus 1 historical NEW proposal, 16 UNDECIDED assessments and 3 core functions. Campaign completion preserves the merged scientific evidence limits. The retained NEW-labelled FGFR-regulation row predates this campaign revision. |
| CCDC39 | [`8552bad4435e`](https://github.com/ai4curation/ai-gene-review/commit/8552bad4435e1129aa19549ffa474bb20db49172), 2026-10-04T23:22:31Z | 12 / 2; every path/blob pair is in the queue | Biological COMPLETE retains 30 source assertions plus 1 NEW molecular-function assertion, 5 UNDECIDED assessments and 1 core function. COMPLETE is the normal validation status and does not resolve its five UNDECIDED assessments. |
| CC2D2A | [`ecc0fc3d9990`](https://github.com/ai4curation/ai-gene-review/commit/ecc0fc3d9990285ba523a5f4a57aefe02723210e), 2026-10-04T23:39:16Z | 6 / 10; every path/blob pair is in the queue | Biological DRAFT retains 19 source assertions, 0 UNDECIDED assessments and 1 core function. Its DRAFT status reflects an unused-research advisory; no annotation remains UNDECIDED. |

The six final PR heads have verified approval and successful required checks. Their signed merges account for **144 changed path/blob pairs** and **244 unchanged reused scope objects**, totaling **388 verified scoped objects**. These are per-review counts; shared sources can occur in several scopes. The queue enumerates both maps. CAV3 has 28 whole-PR paths but 27 merge changes after one exact shared-source reuse; the reused path remains within its nine-object reuse map.

The merged payloads retain **707 original source assertions and 64 UNDECIDED assessments**, with 709 total reviewed assertions. Of the two NEW-labelled rows, CBL preserves its historical GO:0040037 FGFR-regulation proposal, whereas CCDC39 adds the reviewed GO:0005200 structural molecular function. No other gene in this tranche adds an annotation. Five reviews remain DRAFT and CCDC39 is COMPLETE. COMPLETE is a normal validation status, not a claim that its five UNDECIDED assessments are resolved; CC2D2A is DRAFT with no UNDECIDED rows because an unused-research advisory remains. The alternative-product counts are 0, 2, 2, 0, 2 and 4 in table order: CAV3 and CBL have no alternative-products slot, not an assertion of zero protein products. Core counts are 2, 1, 1, 3, 1 and 1.

All **226 existing `genes[]` queue entries** are preserved, followed by six entries. Queue-entry count is distinct from the completed-gene baseline. All 2,876 gene inventory entries and their frozen associations, the checkpoint 228 CASP8 count correction, both corrected CARMIL2 reuse maps, earlier completion records and history, and the checkpoint 95 audit/import boundary remain exact.

[Published checkpoint 231 history](https://github.com/ai4curation/ai-gene-review/blob/main/history/projects/CLINGEN_MENDELIAN/2026-10-04T201348Z-codex-f25fc3.yaml).

### Evidence scope for completion 231

[Checkpoint 231 history](https://github.com/ai4curation/ai-gene-review/blob/main/history/projects/CLINGEN_MENDELIAN/2026-10-04T201348Z-codex-f25fc3.yaml).

The fixed **2026-10-04 19:58:03 UTC** cutoff adds **CASR, CAV1 and CAVIN1** to published checkpoint 228: **231 complete / 2,645 remaining**, with **232 gene-level original review merges** and one required source follow-up outstanding for AKR1D1. Tracker, generated-page and source-workflow PRs add no gene completions. Open reviews #4209, #4210, #4191 and #4175 contribute none at this cutoff.

| Gene | Verified merge | Changed / reused scoped paths | Biological assessment retained |
|---|---|---|---|
| CASR | [`207bae9a4420`](https://github.com/ai4curation/ai-gene-review/commit/207bae9a4420f402d71ff09ad5c0acfb799fbcdb), 2026-10-04T16:52:11Z | 42 / 6; every path/blob pair is in the queue | Biological DRAFT retains 123 source assertions, 33 UNDECIDED assessments and 1 core function. Campaign completion preserves the merged biological assessment and its evidence limits. |
| CAV1 | [`acaa8bd532ef`](https://github.com/ai4curation/ai-gene-review/commit/acaa8bd532ef9586f14ea97b7fd431da787b3570), 2026-10-04T18:27:15Z | 57 / 51; every path/blob pair is in the queue | Biological DRAFT retains 273 source assertions, 37 UNDECIDED assessments and 3 core functions. Campaign completion preserves the merged biological assessment and its evidence limits. |
| CAVIN1 | [`e575922d0239`](https://github.com/ai4curation/ai-gene-review/commit/e575922d0239043ea0ab792779d69af9d27fc78e), 2026-10-04T19:58:03Z | 12 / 13; every path/blob pair is in the queue | Biological DRAFT retains 77 source assertions plus 1 NEW assertion, 12 UNDECIDED assessments and 2 core functions. Campaign completion preserves the merged biological assessment and its evidence limits. The one NEW assertion is GO:0070836 caveola assembly, not a molecular-function annotation. |

The three final PR heads have verified approval and successful required checks. Their signed merges account for **111 changed path/blob pairs** and **70 unchanged reused scope objects**, totaling **181 verified scoped objects** across the three reviews. These are per-review counts; a shared source may occur in more than one scope. The queue enumerates both maps. CAVIN1 has 15 whole-PR paths but only 12 merge changes: PMID:19525939, PMID:19726876 and PMID:24013648 had become exact main-branch source reuses before its merge and remain explicitly included in the 13-object reuse map.

All three biological reviews remain **DRAFT**, retaining **473 original source assertions and 82 UNDECIDED assessments**. CAVIN1 adds one reviewed NEW biological-process assertion, GO:0070836 caveola assembly, for 474 total reviewed assertions across this tranche. CASR and CAV1 add none. CASR and CAV1 each retain two alternative products, CAVIN1 three; their core-function counts are one, three and two respectively. Campaign completion records finished review and publication while preserving these evidence limits.

All **223 existing `genes[]` queue entries** are preserved, followed by three entries; queue-entry count is distinct from the completed-gene baseline. The checkpoint 228 CASP8 correction, both corrected CARMIL2 source reuse maps, all 2,876 gene inventory entries and their frozen associations, all earlier completion records and history, and the checkpoint 95 audit/import boundary remain exact.

[Published checkpoint 228 history](https://github.com/ai4curation/ai-gene-review/blob/main/history/projects/CLINGEN_MENDELIAN/2026-10-04T161209Z-codex-6c9ecc.yaml).

### Evidence scope for completion 228

[Checkpoint 228 history](https://github.com/ai4curation/ai-gene-review/blob/main/history/projects/CLINGEN_MENDELIAN/2026-10-04T161209Z-codex-6c9ecc.yaml).

The fixed **2026-10-04 15:17:41 UTC** cutoff adds **CASK, CASP8 and CASQ2** to published checkpoint 225: **228 complete / 2,648 remaining**, with **229 gene-level original review merges** and one required source follow-up outstanding for AKR1D1. Tracker, generated-page and source-workflow PRs add no gene completions. Other pending reviews contribute none at this cutoff.

The planned total of 227 omitted CASP8 because its earlier repository review was mistaken for an already recorded campaign completion. The published checkpoint 225 inventory leaves CASP8 unchecked, and its queue and progress ledger contain no CASP8 entry. Original multi-gene apoptosis PR [#3672](https://github.com/ai4curation/ai-gene-review/pull/3672) merged as `6202dafbf7a64866df30e2a500bf3c8a80427870` on 2026-10-03 at 21:22:04 UTC. The substantive campaign revision [#4139](https://github.com/ai4curation/ai-gene-review/pull/4139) is now its first verified campaign completion. Thus **225 + 3 = 228**; CASP8 original #3672 contributes one newly recognized gene-level original review, and #4139 is not counted as a second original. No prior published checkpoint count is rewritten.

| Gene | Verified merge | Changed / reused scoped paths | Biological assessment retained |
|---|---|---|---|
| CASK | [`72e64874c80b`](https://github.com/ai4curation/ai-gene-review/commit/72e64874c80b5ea68cac52b36b802595c83d5ea0), 2026-10-04T14:29:51Z | 23 / 20; every path/blob pair is in the queue | Biological DRAFT retains 118 source assertions, 31 UNDECIDED assessments and 2 core functions. Campaign completion preserves the merged biological assessment and its evidence limits. |
| CASP8 | [`91b5ea418917`](https://github.com/ai4curation/ai-gene-review/commit/91b5ea4189172fa75f9fe54b4786fc6eb5c9849c), 2026-10-04T15:11:44Z | 6 / 128; every path/blob pair is in the queue | Biological DRAFT retains 264 source assertions, 21 UNDECIDED assessments and 2 core functions. Campaign completion preserves the merged biological assessment and its evidence limits. This is the first campaign completion of the existing review, not a second original review. |
| CASQ2 | [`b4fb9e72ca0a`](https://github.com/ai4curation/ai-gene-review/commit/b4fb9e72ca0a090d2b726560d4925f375b70f313), 2026-10-04T15:17:41Z | 22 / 1; every path/blob pair is in the queue | Biological DRAFT retains 57 source assertions, 12 UNDECIDED assessments and 2 core functions. Campaign completion preserves the merged biological assessment and its evidence limits. |

All three final PR heads have verified approval and successful required checks. Their signed merges account for **51 changed path/blob pairs** and **149 unchanged reused scope objects**, totaling **200 verified scoped objects** across the three reviews. These are per-review counts; a shared source may occur in more than one scope. The durable queue enumerates both changed and reused blobs. All three biological reviews remain **DRAFT**, retaining **439 source assertions and 64 UNDECIDED assessments**, with no NEW assertions. CASK retains six alternative products, CASP8 nine, and CASQ2 two; each has two core functions. Campaign completion records finished review and publication while preserving biological uncertainty.

All **220 existing `genes[]` queue entries** are preserved, followed by three entries; this entry count is distinct from the 225 completed-gene baseline. The corrected CARMIL2 reuse maps for PMID:19946888 and PMID:23793062 remain exact in both durable locations. All 2,876 gene inventory entries and their frozen associations, all prior completion records and dated history, and the checkpoint 95 audit/import boundary remain unchanged.

[Published checkpoint 225 correction history](https://github.com/ai4curation/ai-gene-review/blob/main/history/projects/CLINGEN_MENDELIAN/2026-10-04T145323Z-codex-9c8b76.yaml).

### Evidence scope for completion 225

[Checkpoint 225 history](https://github.com/ai4curation/ai-gene-review/blob/main/history/projects/CLINGEN_MENDELIAN/2026-10-04T142312Z-codex-03233c.yaml).

The fixed **2026-10-04 14:10:18 UTC** cutoff adds **CARMIL2** to published checkpoint 224: **225 complete / 2,651 remaining**, with 226 original gene PR merges. AKR1D1 remains excluded pending its required source follow-up. Tracker, generated-page and source-workflow PRs add no gene completions. Other pending gene reviews contribute no completion in this checkpoint.

| Gene | Verified merge | Exact changed paths verified at merge | Biological assessment retained |
|---|---|---|---|
| CARMIL2 | [`adee3d6ced9b`](https://github.com/ai4curation/ai-gene-review/commit/adee3d6ced9b32d6782902ff109733d6c7cf2565), 2026-10-04 14:10:18 UTC | 16; every path/blob pair is in the queue | Biological DRAFT retains 45 source assertions plus 1 NEW molecular-function assertion, 3 UNDECIDED assessments and 2 core functions. Campaign completion preserves the merged biological assessment and its evidence limits. |

The final PR head has verified approval and successful required checks. The signed merge record matches **16 changed path/blob pairs** within an 18-path verified scope, including two reused sources: `publications/PMID_19946888.md` and `publications/PMID_23793062.md`. Their exact merge-commit blob hashes are enumerated in both matching durable-evidence entries in the queue; 16 changed paths plus two unchanged reused sources account for the 18-path scope. This is the checked merge scope, not a new audit of reused sources outside that scope. The merged biological review remains **DRAFT**, retaining **45 source assertions plus one NEW molecular-function assertion**, for 46 total annotations: **33 ACCEPT, 8 KEEP_AS_NON_CORE, 3 UNDECIDED, 1 MODIFY and 1 NEW**. The NEW annotation is **GO:0035591 signaling adaptor activity**; no new biological-process annotation is introduced. The review began with a normal initialized seed and retains two core functions. Campaign completion records the finished review and verified publication, without implying that every biological assertion is certain. All **219 existing `genes[]` queue entries** are preserved, followed by this entry; that entry count is distinct from the 224 completed-gene baseline. All 2,876 inventory rows and association text, prior dated records, the fixed checkpoint 224 cutoff and history, and the checkpoint 95 audit/import boundary remain intact.

[Published checkpoint 224 history](https://github.com/ai4curation/ai-gene-review/blob/main/history/projects/CLINGEN_MENDELIAN/2026-10-04T130936Z-codex-a08be8.yaml).

### Evidence scope for completion 224

[Checkpoint 224 history](https://github.com/ai4curation/ai-gene-review/blob/main/history/projects/CLINGEN_MENDELIAN/2026-10-04T130936Z-codex-a08be8.yaml).

The fixed **2026-10-04 12:47:21 UTC** cutoff adds **CAPN5 and CARD11** to published checkpoint 222: **224 complete / 2,652 remaining**, with 225 original gene PR merges. AKR1D1 remains excluded pending its required source follow-up. Tracker, generated-page and source-workflow PRs add no gene completions. Other pending gene reviews contribute no completion in this checkpoint.

| Gene | Verified merge | Exact changed paths verified at merge | Biological assessment retained |
|---|---|---|---|
| CAPN5 | [`33a9b5b4b20c`](https://github.com/ai4curation/ai-gene-review/commit/33a9b5b4b20cc7907b845f3fa2720d82cc88af1b), 2026-10-04 12:13:23 UTC | 16; every path/blob pair is in the queue | Biological DRAFT retains 14 source assertions, 4 UNDECIDED assessments and 1 core function. Campaign completion preserves the merged biological assessment and its evidence limits. |
| CARD11 | [`47548efbbc18`](https://github.com/ai4curation/ai-gene-review/commit/47548efbbc186b23b745125e3611b16e511c9c5f), 2026-10-04 12:47:21 UTC | 20; every path/blob pair is in the queue | Biological DRAFT retains 88 source assertions, 3 UNDECIDED assessments and 1 core function. Campaign completion preserves the merged biological assessment and its evidence limits. |

Both final PR heads have verified approval and successful required checks. Signed merge records match **36 changed path/blob pairs**. This is the checked merge scope, not a new audit of reused sources outside those diffs. Both merged biological states remain **DRAFT**, retaining **102 source assertions and 7 UNDECIDED assessments**, with no NEW assertions. Both reviews began with normal initialized seeds. Campaign completion records the finished review and verified publication, without implying that every biological assertion is certain. All **217 existing `genes[]` queue entries** are preserved, followed by these two entries; that entry count is distinct from the 222 completed-gene baseline. All 2,876 inventory rows and association text, prior dated records, the fixed checkpoint 222 cutoff and history, and the checkpoint 95 audit/import boundary remain intact.

[Published checkpoint 222 history](https://github.com/ai4curation/ai-gene-review/blob/main/history/projects/CLINGEN_MENDELIAN/2026-10-04T120639Z-codex-9a92c4.yaml).

### Evidence scope for completion 222

[Checkpoint 222 history](https://github.com/ai4curation/ai-gene-review/blob/main/history/projects/CLINGEN_MENDELIAN/2026-10-04T120639Z-codex-9a92c4.yaml).

The fixed **2026-10-04 11:36:42 UTC** cutoff adds **CANT1 and CAPN3** to published checkpoint 220: **222 complete / 2,654 remaining**, with 223 original gene PR merges. AKR1D1 remains excluded pending its required source follow-up. Tracker, generated-page and source-workflow PRs add no gene completions. Other pending gene reviews contribute no completion in this checkpoint.

| Gene | Verified merge | Exact changed paths verified at merge | Biological assessment retained |
|---|---|---|---|
| CANT1 | [`c06607d5f36e`](https://github.com/ai4curation/ai-gene-review/commit/c06607d5f36e3558ead32d9e7c4336d67824d5f4), 2026-10-04 10:34:22 UTC | 13; every path/blob pair is in the queue | Biological DRAFT retains 37 source assertions, 4 UNDECIDED assessments and 1 core function. Campaign completion preserves the merged biological assessment and its evidence limits. |
| CAPN3 | [`8b5e616456b0`](https://github.com/ai4curation/ai-gene-review/commit/8b5e616456b0d955e7bda32a6a0eb43a98bee1ec), 2026-10-04 11:36:42 UTC | 25; every path/blob pair is in the queue | Biological DRAFT retains 96 source assertions, 16 UNDECIDED assessments and 2 core functions. Campaign completion preserves the merged biological assessment and its evidence limits. |

Both final PR heads have verified approval and successful required checks. Signed merge records match **38 changed path/blob pairs**. This is the checked merge scope, not a new audit of reused sources outside those diffs. Both merged biological states remain **DRAFT**, retaining **133 source assertions and 20 UNDECIDED assessments**, with no NEW assertions. Both reviews began with normal initialized seeds. Campaign completion records the finished review and verified publication, without implying that every biological assertion is certain. All **215 existing `genes[]` queue entries** are preserved, followed by these two entries; that entry count is distinct from the 220 completed-gene baseline. All 2,876 inventory rows and association text, prior dated records, the fixed checkpoint 220 cutoff and history, and the checkpoint 95 audit/import boundary remain intact.

[Published checkpoint 220 history](https://github.com/ai4curation/ai-gene-review/blob/main/history/projects/CLINGEN_MENDELIAN/2026-10-04T090853Z-codex-9e7abf.yaml).

### Evidence scope for completion 220

[Checkpoint 220 history](https://github.com/ai4curation/ai-gene-review/blob/main/history/projects/CLINGEN_MENDELIAN/2026-10-04T090853Z-codex-9e7abf.yaml).

The fixed **2026-10-04 08:47:19 UTC** cutoff adds **CACNA1F, CAMK2A, CA2 and CAMTA1** to published checkpoint 216: **220 complete / 2,656 remaining**, with 221 original gene PR merges. AKR1D1 remains excluded pending its required source follow-up. Tracker, generated-page and source-workflow PRs add no gene completions. Other pending gene reviews contribute no completion in this checkpoint.

| Gene | Verified merge | Exact changed paths verified at merge | Biological assessment retained |
|---|---|---|---|
| CACNA1F | [`7f72807cfe3b`](https://github.com/ai4curation/ai-gene-review/commit/7f72807cfe3b7406ed4a90ed55ca7a1d9e9ff3e3), 2026-10-04 07:22:48 UTC | 15; every path/blob pair is in the queue | Biological COMPLETE retains 24 source assertions, 4 UNDECIDED assessments and 1 core function. Campaign completion preserves the merged biological assessment and its evidence limits. |
| CAMK2A | [`ab4c372c9a04`](https://github.com/ai4curation/ai-gene-review/commit/ab4c372c9a04f5700ab9a6da9ad36b4d599661dc), 2026-10-04 08:21:48 UTC | 5; every path/blob pair is in the queue | Biological DRAFT retains 171 source assertions, 11 UNDECIDED assessments and 1 core function. Campaign completion preserves the merged biological assessment and its evidence limits. |
| CA2 | [`798fb7343e8f`](https://github.com/ai4curation/ai-gene-review/commit/798fb7343e8f3fa8708c7d483d72d4559d2a33d8), 2026-10-04 08:23:31 UTC | 68; every path/blob pair is in the queue | Biological DRAFT retains 89 source assertions, 4 UNDECIDED assessments and 1 core function. Campaign completion preserves the merged biological assessment and its evidence limits. |
| CAMTA1 | [`938e8bc2b648`](https://github.com/ai4curation/ai-gene-review/commit/938e8bc2b64862ff2d337c38c044695a7cf281c8), 2026-10-04 08:47:19 UTC | 12; every path/blob pair is in the queue | Biological COMPLETE retains 10 source assertions, 2 UNDECIDED assessments and 1 core function. Campaign completion preserves the merged biological assessment and its evidence limits. |

All four final PR heads have verified approval and successful required checks. Signed merge records match **100 changed path/blob pairs**. This is the checked merge scope, not a new audit of reused sources outside those diffs. The merged biological states remain **two DRAFT and two COMPLETE**, retaining **294 source assertions and 21 UNDECIDED assessments**, with no NEW assertions. CAMK2A updates an existing review; the other three reviews began with normal initialized seeds. Campaign completion records the finished review and verified publication, without implying that every biological assertion is certain. All **211 existing `genes[]` queue entries** are preserved, followed by these four entries; that entry count is distinct from the 216 completed-gene baseline. All 2,876 inventory rows and association text, prior dated records, the fixed checkpoint 216 cutoff and history, and the checkpoint 95 audit/import boundary remain intact.

[Published checkpoint 216 history](https://github.com/ai4curation/ai-gene-review/blob/main/history/projects/CLINGEN_MENDELIAN/2026-10-04T072125Z-codex-7b57bd.yaml).

### Evidence scope for completion 216

[Checkpoint 216 history](https://github.com/ai4curation/ai-gene-review/blob/main/history/projects/CLINGEN_MENDELIAN/2026-10-04T072125Z-codex-7b57bd.yaml).

The fixed **2026-10-04 07:13:11 UTC** cutoff adds **CA5A, CA8, CABP2, CACNA1B, CACNA1D, CAD, CALM1, CACNA1E, CACNA1G, CALM2, CALM3, CACNA2D4 and CACNA1C** to published checkpoint 203: **216 complete / 2,660 remaining**, with 217 original gene PR merges. AKR1D1 remains excluded pending its required source follow-up. Tracker, generated-page and source-workflow PRs add no gene completions. Other pending gene reviews contribute no completion in this checkpoint.

| Gene | Verified merge | Exact changed paths verified at merge | Biological assessment retained |
|---|---|---|---|
| CA5A | [`201b20f8160a`](https://github.com/ai4curation/ai-gene-review/commit/201b20f8160a7527633f0968de92008219d781a9), 2026-10-03 20:22:13 UTC | 19; every path/blob pair is in the queue | Biological COMPLETE retains 20 source assertions, 0 UNDECIDED assessments and 1 core function. No new annotation is introduced. |
| CA8 | [`bb9979ca5cdc`](https://github.com/ai4curation/ai-gene-review/commit/bb9979ca5cdce7df6e8ed116ad1fa926b1011f9c), 2026-10-03 21:54:27 UTC | 7; every path/blob pair is in the queue | Biological DRAFT retains 26 source assertions plus 2 NEW assertions, 0 UNDECIDED assessments and 1 core function. Campaign completion preserves the merged biological assessment and its evidence limits. |
| CABP2 | [`fd95b92c752b`](https://github.com/ai4curation/ai-gene-review/commit/fd95b92c752bd3b1c23c529a7d103a0c4d012500), 2026-10-04 04:18:38 UTC | 12; every path/blob pair is in the queue | Biological DRAFT retains 49 source assertions, 1 UNDECIDED assessment and 1 core function. Campaign completion preserves the merged biological assessment and its evidence limits. |
| CACNA1B | [`3a94c2a1b96c`](https://github.com/ai4curation/ai-gene-review/commit/3a94c2a1b96cc599a3190262523bd00661d561de), 2026-10-04 04:20:41 UTC | 15; every path/blob pair is in the queue | Biological DRAFT retains 29 source assertions, 1 UNDECIDED assessment and 1 core function. Campaign completion preserves the merged biological assessment and its evidence limits. |
| CACNA1D | [`a2df2d2932ce`](https://github.com/ai4curation/ai-gene-review/commit/a2df2d2932cec737b0d5d47d379f71e7d7eb8f34), 2026-10-04 04:21:48 UTC | 15; every path/blob pair is in the queue | Biological COMPLETE retains 78 source assertions, 6 UNDECIDED assessments and 1 core function. Campaign completion preserves the merged biological assessment and its evidence limits. |
| CAD | [`97c7c5ece722`](https://github.com/ai4curation/ai-gene-review/commit/97c7c5ece7226030784993b7dd577976dfcd240c), 2026-10-04 04:41:00 UTC | 15; every path/blob pair is in the queue | Biological DRAFT retains 84 source assertions, 16 UNDECIDED assessments and 3 core functions. Campaign completion preserves the merged biological assessment and its evidence limits. |
| CALM1 | [`96522b759322`](https://github.com/ai4curation/ai-gene-review/commit/96522b759322c4e263e9d376e579bf047f080727), 2026-10-04 04:42:55 UTC | 5; every path/blob pair is in the queue | Biological DRAFT retains 176 source assertions, 8 UNDECIDED assessments and 3 core functions. Campaign completion preserves the merged biological assessment and its evidence limits. |
| CACNA1E | [`e519f0da8bd3`](https://github.com/ai4curation/ai-gene-review/commit/e519f0da8bd36d7ae48f5e106b41a2f8386c0049), 2026-10-04 06:07:21 UTC | 11; every path/blob pair is in the queue | Biological DRAFT retains 23 source assertions, 1 UNDECIDED assessment and 1 core function. Campaign completion preserves the merged biological assessment and its evidence limits. |
| CACNA1G | [`b9ae52478bd7`](https://github.com/ai4curation/ai-gene-review/commit/b9ae52478bd743e4aba9638f2c0209a054e051fd), 2026-10-04 06:16:13 UTC | 16; every path/blob pair is in the queue | Biological DRAFT retains 41 source assertions, 5 UNDECIDED assessments and 1 core function. Campaign completion preserves the merged biological assessment and its evidence limits. |
| CALM2 | [`a96daa90cb60`](https://github.com/ai4curation/ai-gene-review/commit/a96daa90cb60a09e4595a8cdecd5e3ba904bdf1c), 2026-10-04 06:39:56 UTC | 7; every path/blob pair is in the queue | Biological DRAFT retains 105 source assertions, 3 UNDECIDED assessments and 3 core functions. Campaign completion preserves the merged biological assessment and its evidence limits. |
| CALM3 | [`ddb719a6b474`](https://github.com/ai4curation/ai-gene-review/commit/ddb719a6b474d16b456a540078e430e401fa2b6c), 2026-10-04 07:07:22 UTC | 12; every path/blob pair is in the queue | Biological DRAFT retains 115 source assertions, 10 UNDECIDED assessments and 5 core functions. Campaign completion preserves the merged biological assessment and its evidence limits. |
| CACNA2D4 | [`93b454926db7`](https://github.com/ai4curation/ai-gene-review/commit/93b454926db758d72d89b9f5a94c21bc4b9936af), 2026-10-04 07:08:57 UTC | 11; every path/blob pair is in the queue | Biological COMPLETE retains 7 source assertions plus 1 NEW assertion, 1 UNDECIDED assessment and 1 core function. Campaign completion preserves the merged biological assessment and its evidence limits. |
| CACNA1C | [`fbf4cfae0dba`](https://github.com/ai4curation/ai-gene-review/commit/fbf4cfae0dba1cc7b1299cc51b005d39870c661a), 2026-10-04 07:13:11 UTC | 36; every path/blob pair is in the queue | Biological DRAFT retains 136 source assertions, 8 UNDECIDED assessments and 1 core function. Campaign completion preserves the merged biological assessment and its evidence limits. |

All thirteen final PR heads have verified approval and successful required checks. Signed merge records match **181 changed path/blob pairs**. This is the checked merge scope, not a new audit of reused sources outside those diffs. CACNA1C’s PR diff contains 37 paths; its merge changes 36, because the identical PMID:12181424 cache was already on main after CACNA2D4. The merged biological states remain **ten DRAFT and three COMPLETE**, including **60 UNDECIDED assessments**; CA8 retains two reviewed NEW assertions and CACNA2D4 retains one. Campaign completion records the finished review and verified publication, without implying that every biological assertion is certain. All **198 existing `genes[]` queue entries** are preserved, followed by these thirteen entries; that entry count is distinct from the 203 completed-gene baseline. All 2,876 inventory rows and association text, prior dated records, and the checkpoint 95 audit/import boundary remain intact.

[Published checkpoint 203 history](https://github.com/ai4curation/ai-gene-review/blob/main/history/projects/CLINGEN_MENDELIAN/2026-10-03T192552Z-codex-582548.yaml).

### Evidence scope for completion 203

[Checkpoint 203 history](https://github.com/ai4curation/ai-gene-review/blob/main/history/projects/CLINGEN_MENDELIAN/2026-10-03T192552Z-codex-582548.yaml).

The fixed **2026-10-03 18:25:30 UTC** cutoff adds **C3 and C9orf72** to published checkpoint 201: **203 complete / 2,673 remaining**, with 204 original gene PR merges. AKR1D1 remains excluded pending its required source follow-up. Tracker, generated-page and source-workflow PRs add no gene completions. CA5A and CA8 remain unchecked in this checkpoint.

| Gene | Verified merge | Exact changed paths verified at merge | Biological assessment retained |
|---|---|---|---|
| C3 | [`6b0ca24ae70c`](https://github.com/ai4curation/ai-gene-review/commit/6b0ca24ae70c1c9f49ba8afbed42a286a2b76c2d), 18:15:29 UTC | 72; every path/blob pair is in the queue | Biological DRAFT retains 142 source assertions, nine UNDECIDED assessments and three cores. Four authored processed-product classes are distinct from alternative splice products. C3a versus ASP/C5L2 context and exact source access limits remain; no new annotation is introduced. |
| C9orf72 | [`46872d06c54e`](https://github.com/ai4curation/ai-gene-review/commit/46872d06c54e3f42443900481ff697c8c9b3d6e8), 18:25:30 UTC | 18; every path/blob pair is in the queue | Biological DRAFT retains 110 source assertions, 23 UNDECIDED assessments, two alternative products and three cores. Reagent-specific localization and GEF/GAP context limits remain; campaign closure does not resolve those biological uncertainties. |

Both final PR heads have verified approval and successful required checks. Signed merge records match **90 changed path/blob pairs**. This is the checked merge scope, not a new audit of reused sources outside those diffs. Both biological reviews remain DRAFT with **32 UNDECIDED assessments** in total. All **196 existing `genes[]` queue entries** are preserved, followed by these two entries; that entry count is distinct from the 201 completed-gene baseline. All 2,876 inventory rows and association text, prior dated records, and the checkpoint 95 audit/import boundary remain intact.

### Evidence scope for completion 201

[Checkpoint 201 history](https://github.com/ai4curation/ai-gene-review/blob/main/history/projects/CLINGEN_MENDELIAN/2026-10-03T165841Z-codex-6975d9.yaml).

The fixed **2026-10-03 16:43:30 UTC** cutoff adds **C1QA, C1QB, C1QTNF5, C2CD3 and C1QBP** to the completion ledger published at checkpoint 196: **201 complete / 2,675 remaining**, with 202 original gene PR merges. AKR1D1 remains excluded while its required source follow-up is outstanding. Tracker, generated-page and source-workflow PRs add no gene completions.

| Gene | Verified merge | Exact changed paths verified at merge | Biological assessment retained |
|---|---|---|---|
| C1QA | [`b07074cf21fb`](https://github.com/ai4curation/ai-gene-review/commit/b07074cf21fb59b16b8ddafefe8352c6b3085fce), 15:13:09 UTC | 34; every path/blob pair is in the queue | Biological DRAFT retains 83 source assertions, six UNDECIDED assessments and three cores; no structured products slot. Bibliography-only and fine synaptic/extracellular-matrix evidence limits remain. Whole-C1q contributions do not establish isolated A-chain sufficiency. |
| C1QB | [`f229b827c95c`](https://github.com/ai4curation/ai-gene-review/commit/f229b827c95cc698b676b74d6a4c8e66b3ab756d), 16:18:20 UTC | 8; every path/blob pair is in the queue | Biological DRAFT retains 62 source assertions, six UNDECIDED assessments and three cores; no structured products slot. Fine donor localization and other source limits remain; recognition, protease recruitment and signaling are scoped to contribution within C1q. |
| C1QTNF5 | [`4086522913b0`](https://github.com/ai4curation/ai-gene-review/commit/4086522913b00d4021707930b26874fcf35bd9f5), 16:21:15 UTC | 13; every path/blob pair is in the queue | Biological DRAFT retains 23 source assertions, three UNDECIDED assessments and one core; no structured products slot. Collagen-stalk inference is distinguished from directly observed globular trimers, and receptor inhibition from chronic perturbation phenotypes. |
| C2CD3 | [`311d3f706642`](https://github.com/ai4curation/ai-gene-review/commit/311d3f7066427929aaa634c7d8e748c3825a6e5e), 16:41:31 UTC | 10; every path/blob pair is in the queue | Biological DRAFT retains 30 source assertions plus one NEW structural-function assertion, five products and one core. Human spatial/depletion evidence is separated from mouse cryo-ET context; direct microtubule affinity, ring-node composition and catalytic activity remain unestablished. |
| C1QBP | [`2bf7e325e50c`](https://github.com/ai4curation/ai-gene-review/commit/2bf7e325e50cb0e37be6afc04274f230339472ea), 16:43:30 UTC | 9; every path/blob pair is in the queue | Biological DRAFT retains 125 source assertions, five UNDECIDED assessments and four cores; no structured products slot. Reconciled partner/donor distinctions and source-specific screen limits remain; precursor/mature localization is described without manufacturing product fields. |

All five final PR heads have verified approval and successful checks. Signed merge records and complete PR file lists match **74 changed path/blob pairs**. This does not claim a new audit of reused sources outside those diffs. The five merged reviews remain DRAFT, including **20 UNDECIDED source assessments**; C2CD3 separately retains one reviewed NEW structural-function assertion. All 191 earlier queue entries, all 2,876 gene rows and ClinGen association text, old dated checkpoints, the checkpoint 95 audit/import boundary and prior histories remain unchanged. Other pending gene work contributes no completion here.

### Evidence scope for completion 196

[Checkpoint 196 history](https://github.com/ai4curation/ai-gene-review/blob/main/history/projects/CLINGEN_MENDELIAN/2026-10-03T152007Z-codex-77f6db.yaml).

The fixed **2026-10-03 14:49:33 UTC** cutoff adds **BSND, BTD, BTK, C19orf12 and BUB1B** to the completion ledger published at checkpoint 191: **196 complete / 2,680 remaining**, with 197 original gene PR merges. AKR1D1 remains excluded from completion while its required source follow-up is outstanding. Shared tracker, generated-page and source-workflow PRs add no gene completions.

| Gene | Verified merge | Exact changed paths verified at merge | Biological assessment retained |
|---|---|---|---|
| BSND | [`66aae0854d61`](https://github.com/ai4curation/ai-gene-review/commit/66aae0854d610012825991d1fbad54e66686ba5e), 13:08:02 UTC | 16; every path/blob pair is in the queue | Biological DRAFT retains 52 source assertions and one channel-regulatory core; no structured products slot. Thirty-one screen-binding decisions retain explicit curator-deference and uninspected target-assay limits. Barttin is the auxiliary subunit, not the channel pore. |
| BTD | [`56b1fad8f80c`](https://github.com/ai4curation/ai-gene-review/commit/56b1fad8f80caf615b5b8d67e80e90001c53b355), 13:08:19 UTC | 14; every path/blob pair is in the queue | Biological COMPLETE retains 20 source assertions, six UNDECIDED assessments, four products and one extracellular biotin-recycling core. Fine mitochondrial localization, screen-binding and CNS-development evidence remain unresolved. |
| BTK | [`a5d697b6e4af`](https://github.com/ai4curation/ai-gene-review/commit/a5d697b6e4afe4355dc921758af2319aacc79d78), 14:20:21 UTC | 35; every path/blob pair is in the queue | Biological DRAFT retains 149 source assertions, 31 UNDECIDED assessments, two products and two cores. PLC regulation is distinguished from covalent substrate phosphorylation; remaining interaction and source-access limits persist. |
| C19orf12 | [`76ce56c2cfc3`](https://github.com/ai4curation/ai-gene-review/commit/76ce56c2cfc38b6a4082ed00b545feedaf037438), 14:31:06 UTC | 12; every path/blob pair is in the queue | Biological COMPLETE retains 22 source assertions, four products and one process core. The molecular activity remains unresolved; positive autophagy regulation and contextual apoptosis over-annotation are preserved. |
| BUB1B | [`847ce08c9bc1`](https://github.com/ai4curation/ai-gene-review/commit/847ce08c9bc1313a25f8798507752c5ce2dd0984), 14:49:33 UTC | 10; every path/blob pair is in the queue | Biological DRAFT retains 119 source assertions, 11 UNDECIDED assessments, three products and two cores. Seven catalytic assertions remain disputed; supported CDC20 inhibition and kinetochore adaptor functions do not settle the kinase controversy. |

All five final PR heads have verified approval and successful checks. The signed merge records and complete PR file lists match **87 changed path/blob pairs**; this does not claim a new audit of every reused publication or Reactome cache. All 186 earlier queue entries, all 2,876 gene rows and their ClinGen association text, old dated checkpoints, the checkpoint 95 audit/import boundary and earlier histories remain unchanged. Biological review statuses and unresolved source assessments remain as merged. C1QA, C1QB, C1QBP and other pending work contribute no completion here.

### Evidence scope for completion 191

The fixed **2026-10-03 12:33:32 UTC** cutoff adds **BRPF1, BRSK2, BRWD3 and BSCL2** to published checkpoint 187: **191 complete / 2,685 remaining**, with 192 original gene PR merges and AKR1D1’s one required source follow-up still outstanding. These are four gene completions; shared tracking and source-workflow changes contribute none.

| Gene | Verified merge | Exact changed paths verified at merge | Biological assessment retained |
|---|---|---|---|
| BRPF1 | [`d221bee44a92`](https://github.com/ai4curation/ai-gene-review/commit/d221bee44a92497c85b2daed08350e6eac0a0bf8), 10:55:34 UTC | 9; the queue enumerates every path/blob pair | Biological COMPLETE retains four UNDECIDED source assessments, 36 source assertions, four alternative products and two cores; no uncertainty is resolved merely by campaign closure. |
| BRSK2 | [`a23171822631`](https://github.com/ai4curation/ai-gene-review/commit/a23171822631d413dd046408b064f512f69fc406), 11:10:19 UTC | 14; the queue enumerates every path/blob pair | Biological DRAFT retains nine UNDECIDED assessments, 48 source assertions, six alternative products and one catalytic core. Combined SAD A/B experimental limits remain. |
| BRWD3 | [`78cc3cc0e4d1`](https://github.com/ai4curation/ai-gene-review/commit/78cc3cc0e4d19a5470df7d355646f03be2c566e3), 12:32:23 UTC | 13; the queue enumerates every path/blob pair | Biological COMPLETE retains the two supplied source assertions, five alternative products and one core. The documented UniProt/normal-GOA discrepancy and species limits remain explicit. |
| BSCL2 | [`20c0b77ea607`](https://github.com/ai4curation/ai-gene-review/commit/20c0b77ea607b3160826d8c29c7e55c030ac9c0a), 12:33:32 UTC | 17; the queue enumerates every path/blob pair | Biological DRAFT retains 30 original source assertions plus one NEW tether activity, seven UNDECIDED assessments, three alternative products and two cores. Thermogenesis and human and fly assay limits remain. |

The durable queue records 53 merge-specific path/blob pairs, not a universal gene/publication/Reactome inventory. All 182 earlier queue entries, all 2,876 ClinGen association rows, prior dated observations and the checkpoint 95 audit/import boundary remain intact. The four former pending table rows are updated; their earlier dated evidence sections remain historical. Other genes remain unchecked, and no pending approval, source import or local review is counted as a merge.

[Standard project history](https://github.com/ai4curation/ai-gene-review/blob/main/history/projects/CLINGEN_MENDELIAN/2026-10-03T125438Z-codex-ce3948.yaml).

### Evidence scope for completion 187

This checkpoint uses the fixed **2026-10-03 10:42:33 UTC** completion cutoff and adds **BRIP1 and BRD4** to published checkpoint 185. It reaches **187 complete / 2,689 remaining**, with 188 original gene PR merges including the unresolved AKR1D1 source follow-up. Both genes had exact-head approval and passing required CI before their signed merges.

| Gene | Verified merge | Exact paths verified at merge | Biological review retained |
|---|---|---|---|
| BRIP1 | [`8156c9b7b58c`](https://github.com/ai4curation/ai-gene-review/commit/8156c9b7b58cc0526b41b6613bf6fe6718f2d054), 10:26:05 UTC | Six: three gene outputs and three histories | DRAFT; 92 source assertions; 65 ACCEPT, 23 KEEP_AS_NON_CORE, three UNDECIDED, one REMOVE; three cores; two alternative products |
| BRD4 | [`82005fc0057b`](https://github.com/ai4curation/ai-gene-review/commit/82005fc0057b32f30e23d061d62c8860753451bd), 10:42:33 UTC | 31 added paths: five gene files, two histories, 22 normal publication caches, two Reactome caches | DRAFT; 81 source assertions; 38 ACCEPT, 24 KEEP_AS_NON_CORE, six MODIFY, 13 UNDECIDED; 40 references; three products; two cores; 21 disclosed validation warnings |

The durable queue enumerates all 37 merge-specific path/blob pairs. Campaign completion does not settle BRIP1's precise interstrand-crosslink-response step or BRD4's catalytic and individual-mark uncertainties. All 180 earlier queue entries, all 2,876 association rows and earlier dated observations are preserved. The unpublished intermediate 186 proposal is superseded by this combined checkpoint and contributes no extra completion or history.

As observed at fixed 2026-10-03 10:42:33 UTC, BRPF1's follow-up was published, with approval not yet verified in this checkpoint and required CI pending; BRSK2's core-coverage follow-up is applied and validated but unpublished; BRWD3's seed is imported and its six-paper fetch succeeded with artifact recovery pending; BSCL2's normal sources are imported and scientific review is underway. These four work observations add no completions. Later events are outside this fixed checkpoint. BRAF's previously observed mixed 725-path PR #3381 and AKR1D1's source follow-up remain excluded; no fresh BRAF ownership/lifecycle audit is claimed. PANTHER family/index work does not count as a gene completion. Historical checkpoint 95 audit/import totals remain unchanged.

[Standard project history](https://github.com/ai4curation/ai-gene-review/blob/main/history/projects/CLINGEN_MENDELIAN/2026-10-03T105722Z-codex-aeb9aa.yaml).

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

- 2026-09-27 05:50 UTC: Published ALDH7A1 #3277, ALDOB #3279, ALG1 #3280 and ALG12 #3281 after independent biological review and local checks. There are 55 dedicated gene audit PRs; completion remains 27 of 2,876. Source gaps and current-head approval/test gates remain explicit. ALG13 and ALG3 full audits continue.
  Verified 49 latest receipts / 289 hashes, 59 historical receipts / 317 hashes and 7 post-merge revision receipts / 61 hashes. All previous gene receipt chains and merge records are unchanged. Source3 succeeded but awaits verified import; source4/5/6 and source3 transport are queued. The six identified review-service failures submitted no reviews. Rendering remains tied to the exact imported ba3ff58d snapshot.

- 2026-09-27 06:35 UTC: Published ALG13 #3282 and ALG3 #3283, bringing dedicated full-audit PRs to 57; completion remains 27 of 2,876. Published verified source3 follow-ups for AKT1, ACOX2, AHCY and AGRN. AGRN stays draft for 15 newly identified provider-only cache gaps. Recorded 101 verified local imports, eight new PENDING seeds, source7 dispatch and three bounded review retries. Every prior receipt and completion checkbox is preserved.
  Verified 51 latest receipts / 253 hashes, 62 historical receipts / 384 hashes and 8 post-merge revision receipts / 67 hashes. Project gene links remain rendered against the exact imported ba3ff58d snapshot.

- 2026-09-27 07:08 UTC: Recorded AFG3L2 #3196, AGL #3197 and ADA follow-up #3263 protected merges after final-head approval, required CI and complete source census: 30 of 2,876 genes complete. Published ABCG8 #3284, ABCG5 #3285 and ABHD12 #3286: 60 full-audit PRs. Published AIPL1 and AHI1 evidence corrections; both remain draft for explicit source gaps. ADNP is held draft for newly discovered supporting-report citations. Recorded successful source4 metadata and transport, plus fixed source8 dispatch. Prior receipts and original merge records remain preserved.
  Verified 54 latest receipts / 292 hashes, 64 historical receipts / 397 hashes and 8 post-merge revisions / 67 hashes. Project links remain rendered against exact imported ba3ff58d membership; no unmerged review links are inferred.

- 2026-09-27 07:40 UTC: Recorded ADGRV1 and AGO1 completion (32/2,876), ABHD5 #3287 and AICDA #3290 full audits (62 audit PRs), AIMP1 evidence revision, and source-complete AIPL1/AIRE revisions. Recorded AIMP2 and AGO2 observed merges without declaring completion: their remaining source4 follow-ups are #3289 and #3288. All 27 source4 records passed archive, identity, raw-copy and no-overwrite checks; partial source5 transport and fixed source9 dispatch are explicit. AGTPBP1 full audit started after fresh overlap checks.
  Verified 56 latest receipts / 333 hashes, 67 historical receipts / 409 hashes and 10 post-merge revisions / 81 hashes. Project links remain pinned to verified ba3ff58d membership; existing receipts are retained.

- 2026-09-27 08:22 UTC: Recorded AGTPBP1 #3292 (63 full-audit PRs), AIMP1 source4 publication and AGO2/AIMP2 DOI follow-ups. Imported 15 unchanged verified source5 records with no overwrites. Reopened ten previously complete genes for 68 primary-identity-verified missing papers and eight separate DOI-only works, correcting current completion from 32 to 22 while retaining every original merge/history receipt. Held approved ALDH7A1 draft for nine further sources. Source6 artifact awaits verified transport; batches 10–13 are dispatched.
  Verified 57 latest / 349 file hashes, 68 historical / 413 hashes and 12 post-merge / 87 hashes. Prior receipts are preserved.

- 2026-09-27 09:11 UTC: ADSL #3194 merged after final-head approval, required CI and a 23-file merged-blob check: 23 complete genes and 38 original merges. AIFM1 #3295, ALG6 #3296 and AK2 #3297 bring full-audit PRs to66. Published ALAS2/ALDH18A1/AKR1D1 source5 and ALDH4A1/ALDH5A1 source6 follow-ups, plus ACAT1/ACSL4 reviewer corrections. ACSL4 is returned to draft for a newly expanded provider/DOI census (36 candidate missing PMIDs and two DOI-only works; final census verification and normal attempts continue). No previous merge or published history is rewritten. Source6 has ten exact no-overwrite imports; source7 archive is retrieved, source8/9 workflows succeeded, and source14 was dispatched at its exact reviewed task head. ACOX2, AHCY and AKT1 new feedback is being addressed. ALB identity and alias checks pass; its ordinary seed fetch failed and a finite ALB-only recovery proposal is in preparation.
  Recorded 60 latest/402 hashes, 73 historical/433 hashes and 14 post-merge/95 hashes; all earlier receipt chains retained.

- 2026-09-27 tracking44 checkpoint: AIPL1 #3257 and ALAS2 #3267 merged after final-head approvals, required CI and verification of all 24 and 21 scoped merged blobs, respectively. Only these two genes gain completion checkboxes: 25/2,876 complete, 40 original merges, 67 dedicated full-audit PRs. ALG8 #3298 is a new draft with one required publication cache. Published AHCY/AKT1/AIRE evidence corrections, ALG1/ALG12/ALG13/ALG3 source7 and ALDOB source6 follow-ups, ACOX2 #3248 post-merge evidence corrections, and ready ABHD5/AICDA source10 follow-ups. Sources7/8/9/10 have eleven/54/25/eleven exact no-overwrite imports, respectively; imported records for other drafts still require gene-specific assessment and publication. Source11 imported 26 exact records whose gene-specific review remains pending; source12/13 workflows succeeded with artifacts pending. ALB-only seed recovery and source15 fixed 36-publication recovery were dispatched and last observed queued. All earlier publication, merge and recovery receipts remain unchanged.
  Recorded 61 latest/395 hashes, 83 historical/513 hashes and 15 post-merge/99 hashes.

- 2026-09-27 checkpoint45: AHCY and ACAT1 completion closes after exact final-head approval, required CI and merged-byte checks (14 and 15 files). Counts are 27/2,876 complete, 41 original merges and 68 full-audit PRs. Added ALG9 and the published evidence/source follow-ups listed above; preserve all earlier publication and merge receipts. Source12 import mirrors exact receipt bytes; transport12/13/14 and source16 states remain explicitly separated from canonical import and gene completion.
  Recorded 62 latest/387 hashes, 90 historical/593 hashes and 17 post-merge/120 hashes.

- 2026-09-27 checkpoint46: Mark only AKT1, ALG13, ALG3, AIRE, ABHD5 and ALDH18A1 newly complete after exact-head approval, required CI and all scoped merged-byte checks. Counts:33/2,876 complete,47 original merges,68 full-audit PRs. Record published evidence/source revisions and recovery states separately from gene completion; preserve every earlier verification log and receipt.
  Verified 62 latest/384 hashes, 96 historical/631 hashes, 18 post-merge/124 hashes and 1 early-gene post-merge/9 hashes.

- 2026-09-27 checkpoint47: Mark only ALDH4A1, AGTPBP1, ABCG5, AIMP1, ALDH5A1, ALG1, ALDH7A1 newly complete after exact-head approval, required CI and all scoped merged-byte checks. Counts: 40/2,876 complete, 54 original merges, 68 full-audit PRs. Record published source/evidence follow-ups, exact source15/16 imports and the ALB seed separately from completed reviews. Preserve every earlier verification log and receipt.
  Verified 62 latest/392 hashes, 108 historical/732 hashes, 22 post-merge/176 hashes and 1 early-gene post-merge/9 hashes.

- 2026-09-27 checkpoint48: Mark only AICDA, ALG6, ABCG8, ADNP, ALG12, AGO2, AIMP2, ALG9, ACOX2, ABHD12, AK2 newly complete after exact-head approval, required CI and scoped merged-byte checks. Counts: 51/2,876 complete, 62 distinct original merges, 11 pending post-merge source follow-ups and 68 full-audit PRs. Preserve original merges and append separate follow-up completion receipts. Record published AARS1, ABCA3, ACTB, AGRN, AIFM1 and ALDOB revisions, exact source17 import, and actual source18/19 states without equating recovery with gene completion.
  Verified 62 latest/400 hashes, 111 historical/751 hashes, 23 post-merge/189 hashes and 3 early-gene post-merge/22 hashes.

- 2026-09-27 checkpoint49: Mark AARS1, AIFM1, ALDOB, ALG8, AHI1, ACSL4 newly complete after current-head approval, required CI and every scoped merged-byte check. 57/2,876 complete; 66 original merges; 9 pending source follow-ups; 68 full-audit PRs. Preserve all original histories/merges and distinguish published source follow-ups, source19 staging/import, source20 dispatch and ALB auxiliary import from completion.

- 2026-09-27 checkpoint50: Record ALB full audit, AGRN/ACTB source19 follow-ups, four assessed source20 imports and the exact two-PMID source21 dispatch. Newly complete: ACTB. 58/2,876 complete; 66 original merges; 8 pending source follow-ups; 69 full-audit PRs. Preserve all prior histories, source receipts and original merge identities.

- 2026-09-27 checkpoint51: Record verified source follow-ups, exact source21 import and independently reconciled first-review versus post-merge completions. Newly complete: ABCA3, ALB, ADGRV1, AGRN, ABCA4. 63/2,876 complete; 68 original merges; 5 pending source follow-ups; 69 full-audit PRs. Preserve all prior histories, source receipts and original merge identities.

- 2026-09-27 checkpoint52: Record verified source follow-ups, explicitly receipted source/seed imports and independently reconciled first-review versus post-merge completions. Authored successors follow verified effective branch heads while preserving earlier synchronization receipts. Newly complete: ABCC8, AFG3L2, AGO1, ABCD1. 67/2,876 complete; 69 original merges; 2 pending source follow-ups; 69 full-audit PRs. Preserve all prior histories, source receipts and original merge identities.

- 2026-09-27 checkpoint53: Record verified source follow-ups, explicitly receipted source/seed imports and independently reconciled first-review versus post-merge completions. Authored successors follow verified effective branch heads while preserving earlier synchronization receipts. Newly complete: AGK, AMT. 69/2,876 complete; 70 original merges; 1 pending source follow-ups; 73 full-audit PRs. Preserve all prior histories, source receipts and original merge identities.

- 2026-09-27 checkpoint54: Record verified source follow-ups, explicitly receipted source/seed imports and independently reconciled first-review versus post-merge completions. Authored successors follow verified effective branch heads while preserving earlier synchronization receipts. Newly complete: ALPK1, ALK, ALMS1, ALPL. 73/2,876 complete; 74 original merges; 1 pending source follow-ups; 76 full-audit PRs. Preserve all prior histories, source receipts and original merge identities.

- 2026-09-27 checkpoint55: Record verified source follow-ups, explicitly receipted source/seed imports and independently reconciled first-review versus post-merge completions. Authored successors follow verified effective branch heads while preserving earlier synchronization receipts. Newly complete: ALX3, ALPK3. 75/2,876 complete; 76 original merges; 1 pending source follow-ups; 79 full-audit PRs. Preserve all prior histories, source receipts and original merge identities.

- 2026-09-27 checkpoint56: Record verified source follow-ups, explicitly receipted source/seed imports and independently reconciled first-review versus post-merge completions. Authored successors follow verified effective branch heads while preserving earlier synchronization receipts. Newly complete: ALX1, ALX4, ALS2, AMER1. 79/2,876 complete; 80 original merges; 1 pending source follow-ups; 81 full-audit PRs. Preserve all prior histories, source receipts and original merge identities.

- 2026-09-27 checkpoint57: Record verified source follow-ups, explicitly receipted source/seed imports and independently reconciled first-review versus post-merge completions. Authored successors follow verified effective branch heads while preserving earlier synchronization receipts. Newly complete: none at this checkpoint. 79/2,876 complete; 80 original merges; 1 pending source follow-ups; 86 full-audit PRs. Preserve all prior histories, source receipts and original merge identities.

- 2026-09-28 checkpoint58: Record verified source follow-ups, explicitly receipted source/seed imports and independently reconciled first-review versus post-merge completions. Authored successors follow verified effective branch heads while preserving earlier synchronization receipts. Newly complete: ANGPTL3, ANK2, ANKRD11, ANKRD26, ANKRD17. 84/2,876 complete; 85 original merges; 1 pending source follow-ups; 87 full-audit PRs. Preserve all prior histories, source receipts and original merge identities.

- 2026-09-28 checkpoint59: Record verified source follow-ups, explicitly receipted source/seed imports and independently reconciled first-review versus post-merge completions. Authored successors follow verified effective branch heads while preserving earlier synchronization receipts. Newly complete: ANK1. 85/2,876 complete; 86 original merges; 1 pending source follow-ups; 90 full-audit PRs. Preserve all prior histories, source receipts and original merge identities.

- 2026-09-28 checkpoint60: Record verified source follow-ups, explicitly receipted source/seed imports and independently reconciled first-review versus post-merge completions. Authored successors follow verified effective branch heads while preserving earlier synchronization receipts. Newly complete: ANKS6. 86/2,876 complete; 87 original merges; 1 pending source follow-ups; 93 full-audit PRs. Preserve all prior histories, source receipts and original merge identities.

- 2026-09-28 checkpoint61: Record verified source follow-ups, explicitly receipted source/seed imports and independently reconciled first-review versus post-merge completions. Authored successors follow verified effective branch heads while preserving earlier synchronization receipts. Newly complete: ANO5, ANOS1, ANTXR1. 89/2,876 complete; 90 original merges; 1 pending source follow-ups; 95 full-audit PRs. Preserve all prior histories, source receipts and original merge identities.

- 2026-09-28 checkpoint62: Record verified source follow-ups, explicitly receipted source/seed imports and independently reconciled first-review versus post-merge completions. Authored successors follow verified effective branch heads while preserving earlier synchronization receipts. Newly complete: ANO10, ANTXR2. 91/2,876 complete; 92 original merges; 1 pending source follow-ups; 96 full-audit PRs. Preserve all prior histories, source receipts and original merge identities.

- 2026-09-28 checkpoint63: Record verified source follow-ups, explicitly receipted source/seed imports and independently reconciled first-review versus post-merge completions. Authored successors follow verified effective branch heads while preserving earlier synchronization receipts. Newly complete: ANXA11, AP5Z1. 93/2,876 complete; 94 original merges; 1 pending source follow-ups; 98 full-audit PRs. Preserve all prior histories, source receipts and original merge identities.

- 2026-09-28 checkpoint64: Record verified source follow-ups, explicitly receipted source/seed imports and independently reconciled first-review versus post-merge completions. Authored successors follow verified effective branch heads while preserving earlier synchronization receipts. Newly complete: AP1G1. 94/2,876 complete; 95 original merges; 1 pending source follow-ups; 100 full-audit PRs. Preserve all prior histories, source receipts and original merge identities.

- 2026-09-28 checkpoint65: Record verified source follow-ups, explicitly receipted source/seed imports and independently reconciled first-review versus post-merge completions. Authored successors follow verified effective branch heads while preserving earlier synchronization receipts. Newly complete: AP4E1, AP2M1, APC. 97/2,876 complete; 98 original merges; 1 pending source follow-ups; 102 full-audit PRs. Preserve all prior histories, source receipts and original merge identities.

- 2026-09-28 checkpoint66: Record verified source follow-ups, explicitly receipted source/seed imports and independently reconciled first-review versus post-merge completions. Authored successors follow verified effective branch heads while preserving earlier synchronization receipts. Newly complete: APOL1, ARHGAP29. 99/2,876 complete; 100 original merges; 1 pending source follow-ups; 106 full-audit PRs. Preserve all prior histories, source receipts and original merge identities.

- 2026-09-28 checkpoint67: Record verified source follow-ups, explicitly receipted source/seed imports and independently reconciled first-review versus post-merge completions. Authored successors follow verified effective branch heads while preserving earlier synchronization receipts. Newly complete: ARHGEF9, ARID1A, AR, ARMC2. 103/2,876 complete; 104 original merges; 1 pending source follow-ups; 110 full-audit PRs. Preserve all prior histories, source receipts and original merge identities.

- 2026-09-28 checkpoint68: Record verified source follow-ups, explicitly receipted source/seed imports and independently reconciled first-review versus post-merge completions. Authored successors follow verified effective branch heads while preserving earlier synchronization receipts. Newly complete: ARID1B. 104/2,876 complete; 105 original merges; 1 pending source follow-ups; 112 full-audit PRs. Preserve all prior histories, source receipts and original merge identities.

- 2026-09-28 checkpoint69: Record verified source follow-ups, explicitly receipted source/seed imports and independently reconciled first-review versus post-merge completions. Authored successors follow verified effective branch heads while preserving earlier synchronization receipts. Newly complete: ARL2BP. 105/2,876 complete; 106 original merges; 1 pending source follow-ups; 114 full-audit PRs. Preserve all prior histories, source receipts and original merge identities.

- 2026-09-28 checkpoint70: Record verified source follow-ups, explicitly receipted source/seed imports and independently reconciled first-review versus post-merge completions. Authored successors follow verified effective branch heads while preserving earlier synchronization receipts. Newly complete: ARSA, ARSB, ARPC1B. 108/2,876 complete; 109 original merges; 1 pending source follow-ups; 115 full-audit PRs. Preserve all prior histories, source receipts and original merge identities.

- 2026-09-28 checkpoint71: Record seven verified publication events and two reconciled completions; no new source or seed imports enter this cut. Preserve the APC2 failed local gate and the exact-head quota/CI observations. Authored successors follow verified effective branch heads while preserving earlier synchronization receipts. Newly complete: ARG1, APC2. 110/2,876 complete; 111 original merges; 1 pending source follow-ups; 119 full-audit PRs. Preserve all prior histories, source receipts and original merge identities.

- 2026-09-28 checkpoint72: Record two verified ASH1L publication events and one reconciled ARX completion; no new source or seed imports enter this cut. Preserve the APC2 failed local gate and the exact-head quota/CI observations. Authored successors follow verified effective branch heads while preserving earlier synchronization receipts. Newly complete: ARX. 111/2,876 complete; 112 original merges; 1 pending source follow-ups; 120 full-audit PRs. Preserve all prior histories, source receipts and original merge identities.

- 2026-09-28 checkpoint73: Record ASNS and ASPA initial publications plus the bounded ASH1L scientific comment and pending quota-reset review retry; no new source or seed imports enter this cut. Preserve the APC2 failed local gate and the exact-head quota/CI observations. Authored successors follow verified effective branch heads while preserving earlier synchronization receipts. Newly complete: none at this checkpoint. 111/2,876 complete; 112 original merges; 1 pending source follow-ups; 122 full-audit PRs. Preserve all prior histories, source receipts and original merge identities.

- 2026-09-28 checkpoint74: Record the verified ASH1L merge; completed Source50–58 and Seed13–18 imports await separate ledger reconciliation; no new source or seed imports enter this cut. Preserve the APC2 failed local gate and the exact-head quota/CI observations. Authored successors follow verified effective branch heads while preserving earlier synchronization receipts. Newly complete: ASH1L. 112/2,876 complete; 113 original merges; 1 pending source follow-ups; 122 full-audit PRs. Preserve all prior histories, source receipts and original merge identities.

- 2026-09-29 checkpoint75: Record the verified ARSL and ASAH1 merges, the ASPA/ASL/ASNS published followups, the ASS1 initial publication and 21 completed Source50–58/Seed13–18 import events. Reconciliation grants no extra gene completion and performs no new cache writes. Preserve the APC2 failed local gate and the exact-head quota/CI observations. Authored successors follow verified effective branch heads while preserving earlier synchronization receipts. Newly complete: ARSL, ASAH1. 114/2,876 complete; 115 original merges; 1 pending source follow-ups; 123 full-audit PRs. Preserve all prior histories, source receipts and original merge identities.

- 2026-09-29 checkpoint76: Record the verified ASPA merge and ASPM initial publication. Completed Source59/60 and Seed19/20 primary and auxiliary imports await a separately bounded ledger reconciliation; this cut performs no cache writes. Preserve the APC2 failed local gate and the exact-head quota/CI observations. Authored successors follow verified effective branch heads while preserving earlier synchronization receipts. Newly complete: ASPA. 115/2,876 complete; 116 original merges; 1 pending source follow-ups; 124 full-audit PRs. Preserve all prior histories, source receipts and original merge identities.

- 2026-09-29 checkpoint77: Record ASXL1, ASXL2 and ATF6 initial audits, ASS1 and ASPM published followups, and seven completed Source61/62 and Seed21/22/23 import events. No new cache writes or gene completions occur; six older closures and Seed23 auxiliary remain outside this fixed cut. Preserve the APC2 failed local gate and the exact-head quota/CI observations. Authored successors follow verified effective branch heads while preserving earlier synchronization receipts. Newly complete: none at this checkpoint. 115/2,876 complete; 116 original merges; 1 pending source follow-ups; 127 full-audit PRs. Preserve all prior histories, source receipts and original merge identities.

- 2026-09-29 checkpoint78: Record ASPM completion, the ASXL3 initial audit, ASXL2 and ATF6 published followups, and four completed Source63 and Seed23/24 import events. No new cache writes occur; six older closures and Source64/65 and Seed25 remain outside this fixed cut. Preserve the APC2 failed local gate and the exact-head quota/CI observations. Authored successors follow verified effective branch heads while preserving earlier synchronization receipts. Newly complete: ASPM. 116/2,876 complete; 117 original merges; 1 pending source follow-ups; 128 full-audit PRs. Preserve all prior histories, source receipts and original merge identities.

- 2026-09-29 checkpoint79: Record ATL1 initial audit, ASXL1 and ASS1 published followups, three completed Source64 and Seed25 import events, and six exact-head review/test observations. No new cache writes or gene completions occur; six older closures, Source65 and Seed26 remain outside this fixed cut. Preserve the APC2 failed local gate and the exact-head quota/CI observations. Authored successors follow verified effective branch heads while preserving earlier synchronization receipts. Newly complete: none at this checkpoint. 116/2,876 complete; 117 original merges; 1 pending source follow-ups; 129 full-audit PRs. Preserve all prior histories, source receipts and original merge identities.

- 2026-09-29 checkpoint80: Record the ATM initial audit, completed Source65 nine-source import, actual repository validation limitation, Source66 and Seed26–28 lifecycle observations, and the unpublished ATN1 authored draft. No new cache writes, merges or gene completions occur; six older closures remain deferred. Preserve the APC2 failed local gate and the exact-head quota/CI observations. Authored successors follow verified effective branch heads while preserving earlier synchronization receipts. Newly complete: none at this checkpoint. 116/2,876 complete; 117 original merges; 1 pending source follow-ups; 130 full-audit PRs. Preserve all prior histories, source receipts and original merge identities.

- 2026-09-29 checkpoint81: Record the verified ASXL1 initial merge and its exact-head successful required CI and review. Biological YAML remains DRAFT with three documented generic-binding advisories. Seed29–31 were each dispatched once and remained queued at their saved observations. The four saved retry observations remain queued without a biological verdict; no cache writes or new audits occur, and six older closures remain deferred. Preserve the APC2 failed local gate and the exact-head quota/CI observations. Authored successors follow verified effective branch heads while preserving earlier synchronization receipts. Newly complete: ASXL1. 117/2,876 complete; 118 original merges; 1 pending source follow-ups; 130 full-audit PRs. Preserve all prior histories, source receipts and original merge identities.

- 2026-09-29 checkpoint82: Record three exact-head approved merges (ASXL2, ATF6, ASS1), ATP6AP2 initial publication, ATL1 followup, Source66 one-cache closure and two observed terminal seed jobs. Published DRAFT biology and unresolved generic-binding policy remain explicit; no seed import or queued-job completion is inferred. Preserve the APC2 failed local gate and the exact-head quota/CI observations. Authored successors follow verified effective branch heads while preserving earlier synchronization receipts. Newly complete: ASXL2, ATF6, ASS1. 120/2,876 complete; 121 original merges; 1 pending source follow-ups; 131 full-audit PRs. Preserve all prior histories, source receipts and original merge identities.

- 2026-09-29 checkpoint83: Record five verified merges (ASXL3, ATL1, ATP6AP2, ATM, ATN1), five newly recorded audit PRs and eight closed same-PR followups. Ten completed import receipts cover 78 exclusive creates. ATP1A1 HTTP502 transport/readback recovery remains distinct; AP1 policy hold and other pending reviews do not imply completion. Preserve the APC2 failed local gate and the exact-head quota/CI observations. Authored successors follow verified effective branch heads while preserving earlier synchronization receipts. Newly complete: ASXL3, ATL1, ATP6AP2, ATM, ATN1. 125/2,876 complete; 126 original merges; 1 pending source follow-ups; 136 full-audit PRs. Preserve all prior histories, source receipts and original merge identities.

- 2026-09-29 checkpoint84: Record the verified ATP13A2 merge, four new audit PRs (ATP2B2, ATP1A3, ATP6V1B1, ATP1A2) and four same-PR followups. Four completed import receipts cover 19 exclusive creates. Six published heads remain open after failed automated reviews: V0/A1 quota causes are verified, while the other four causes are unknown. No reviewer retry or completion is inferred. Preserve the APC2 failed local gate and the exact-head quota/CI observations. Authored successors follow verified effective branch heads while preserving earlier synchronization receipts. Newly complete: ATP13A2. 126/2,876 complete; 127 original merges; 1 pending source follow-ups; 140 full-audit PRs. Preserve all prior histories, source receipts and original merge identities.

- 2026-09-29 checkpoint85: Record two new audit PRs, ATP13A3 and ATP7B, without any completion change. Five completed import receipts cover 32 exclusive creates. Saved observations retain six earlier failed automated reviews with successful CI; only V0/A1 quota causes are verified. The two newly published audits had checks in progress. The global validation reference phase was incomplete after Crossref DNS failure. ATP7A prospective consultation and ATP8A2 preparation remain outside published completion. No reviewer retry or merge is inferred. Preserve the APC2 failed local gate and the exact-head quota/CI observations. Authored successors follow verified effective branch heads while preserving earlier synchronization receipts. Newly complete: none at this checkpoint. 126/2,876 complete; 127 original merges; 1 pending source follow-ups; 142 full-audit PRs. Preserve all prior histories, source receipts and original merge identities.

- 2026-09-29 checkpoint86: Record ATP7A initial audit and ATP13A3 first follow-up without a completion change. Seed33 primary and auxiliary imports add four exclusive creates. Six saved earlier heads have successful tests and failed automated reviews without current-head formal verdicts; only V0/A1 quota causes are verified. ATP7A and the new ATP13A3 head had tests/review in progress at their saved observations. Preserve the separate aggregate old-head change request for ATP13A3 without presenting it as a new-head verdict. Later ATP7B feedback publication is outside this cut. Preserve the prior incomplete global reference-validation result and all historical records. No reviewer retry, new merge or source-cache write is inferred. 126/2,876 complete; 127 original merges; 1 pending source follow-ups; 143 full-audit PRs.

- 2026-09-29 checkpoint87: Record ATP7B first, ATP7A first and ATP13A3 second same-PR follow-ups. Source72 imports six exact normal caches without overwrite. One authorized rerun of each of five failed older reviewer jobs is pending at the saved cut; successful required tests alone do not grant approval. ATP6V0A2 review retry succeeded but returned a generic-binding policy disagreement; ATP7A has the same policy hold. Post-cut ATP13A3 merged at its exact approved head after required CI passed; one completion is added and the earlier pending observation is retained as history. Seed34 has one verified queued dispatch without source outcomes/import; ATP8A2 remains unpublished. Preserve incomplete global validation and six older deferred import closures. 127/2,876 complete; 128 original merges; 1 pending source follow-ups; 143 full-audit PRs.

- 2026-09-29 checkpoint88: Record ATP8A2 initial publication and ATP2B2 second, ATP1A3 first, ATP1A2 first, ATP1A1 third and ATP6V1B1 first follow-ups. At the saved 21:10:42 UTC observation, ATP2B2 has current-head approval and required CI in progress; ATP8A2 has current-head changes requested on the generic-binding policy conflict with CI in progress. ATP1A3 CI is in progress and its review queued; the other three follow-ups have queued checks and no current-head formal verdict. ATRX primary3/auxiliary22 source imports are closed; its biological review and additional Source73 recovery remain separate from publication/completion at this fixed cut. No new merge or checkbox. Preserve the prior incomplete global-validation boundary and six older deferred imports. 127/2,876 complete; 128 original merges; 1 pending source follow-ups; 144 full-audit PRs.

- 2026-09-29 checkpoint89: At the saved 23:10 UTC cut, reconcile four verified merges (ATP2B2, ATP1A3, ATP1A2, ATP6V1B1), B3GALNT2 initial ready PR3563 with queued checks/review, and Source73 five normal-cache imports. Source74 is queued; AUTS2 Seed37 was dispatched once and is queued, without source outcomes. ATRX additional references are integrated with focused validation/render/history checks passed (15 advisories), but no publication. Preserve historical policy holds, six deferred import closures and the incomplete global-reference-validation boundary. 131/2,876 complete; 132 original merges; 1 pending source follow-ups; 145 full-audit PRs.

- 2026-09-30 checkpoint90: At the fixed 01:16:20 UTC evidence cut, reconcile ATP8A2 first follow-up and verified merge, ATRX #3564, AUH #3565 and ATXN2 #3566 initial audits and B3GALNT2 #3563 follow-up. Four current heads have changes requested; ATXN2 required test is still running, while the other three tests passed. Sources 74/75 and Seeds 35/36/37 primary plus auxiliary closures add 33 exact files, giving 49 receipts/342 creates. Source76 is once-dispatched queued; no outcomes or import claimed. Preserve historical policy holds, six deferred closures and incomplete global-reference validation. 132/2,876 complete; 133 original merges; 1 pending source follow-ups; 148 full-audit PRs.

- 2026-09-30 checkpoint91: At the fixed 03:30:51 UTC cut, reconcile six publication revisions and the approved, CI-successful AUH merge. AURKC #3568 and AUTS2 #3569 are the two new audit PRs. Sources 76/77 and Seeds 38/39 primary+auxiliary add 29 exact creates, giving 55 receipts/371 creates. Current formal reviews/CI for four remaining open heads are not separately reconciled; no completion inferred. Parser 66cb16d9/issue 3570 disclose deferred data repairs. Source 78 recovery/import and later AXIN2, ATRX second and parser roundtrip publications remain excluded. Preserve seven older policy holds, six deferred closures and incomplete global validation. 133/2,876 complete; 134 original merges; 1 pending source follow-up; 150 full-audit PRs.

- 2026-09-30 checkpoint92: At the fixed 05:15:38 UTC cut, reconcile five publication revisions and three approved, required-CI-successful merges: ATRX #3564, B3GALT6 #3573 and AXIN2 #3572. Initial AXIN2/B3GALT6 publications add two audit PRs. Sources 78/79 and Seed 40 primary/auxiliary add ten exact creates, giving 59 receipts/381 creates. B3GLCT and B4GALNT1 drafts remain incomplete. Parser #3567 merged; issue #3570 still holds 29 data repairs across 17 reviews. Seed 40 explicitly uses the merged parser runtime. Unchanged open-head observations remain dated checkpoint91; Source80 and later biological work are excluded. Preserve seven older policy holds, six deferred closures and incomplete global validation. 136/2,876 complete; 137 original merges; 1 pending source follow-up; 152 full-audit PRs.

- 2026-09-30 checkpoint93: At the fixed 09:11:33 UTC cut, reconcile eleven publication revisions and two verified merges: B4GALNT1 #3574 and B3GLCT #3575. Four initial audits add four full-audit PRs. B4GALT1 third follow-up remains changes-requested with CI in progress in its saved observation; B4GALT7 history clarification is approved with CI in progress. Five executed imports add 24 exact creates, giving 64 receipts/405 creates. Seed42 auxiliary disposition made zero writes and is counted separately. Earlier dated observations, seven policy holds, six deferred closures and incomplete global validation remain unchanged. 138/2,876 complete; 139 original merges; 1 pending source follow-up; 156 full-audit PRs.

- 2026-09-30 checkpoint94: Fixed 10:28:54 UTC cut: three publication revisions (BAG3 initial and first follow-up; B9D1 initial), one verified merge (B4GALT7 #3577), and one Source82 import with two creates. BAG3’s current-head policy hold remains; B9D1’s formal changes-requested event at 10:26:57 precedes the cut although its saved observation was fetched later. Required CI was observed in progress, with no cutoff-time CI poll claimed. Seed43 publication, one dispatch and successful terminal workflow remain operation-only, with no report or imports counted. Earlier dated observations, seven older policy holds, the Seed42 zero-write disposition, six deferred closures and incomplete global validation are preserved. 139/2,876 complete; 140 original merges; 1 pending source follow-up; 158 full-audit PRs.

- 2026-09-30 checkpoint95: Fixed 13:59:34 UTC cut: seven publication revisions across B9D1, BAP1, BBIP1 and BARD1, with no new merge counted. BAP1 has exact-head approval while required CI was observed in progress; B9D1 remains on the supplied-ActionEnum policy hold, and BBIP1/BARD1 have exact-head changes requested. Six executed imports create 28 files (Seed43 primary3+auxiliary14, Source83 one, Seed44 primary3+auxiliary5, Source84 two), giving 71 receipts/435 creates. Later Source85 import and subsequent merge or follow-up events are excluded. Historical observations, Seed42 zero-write disposition, six deferred closures and incomplete global validation are preserved. 139/2,876 complete; 140 original merges; 1 pending source follow-up; 161 full-audit PRs.

- 2026-10-01 UTC: Reconciled the five saved, verified merge receipts for BAP1, BARD1, BBIP1, BBS12 and BCAT2. Updated their inventory checkboxes and progress rows and appended exact merge provenance to the publication queue. Completion count: 139 → 144; original gene PR merges: 140 → 145; remaining catalog genes: 2,732. Preserved checkpoint 95 audit/import totals, historical observations and all association data.

- 2026-10-01 UTC: Recorded the verified BCL11A #3650 and BCKDHA #3614 merges. Completion count: 144 → 146; original gene PR merges: 145 → 147; remaining catalog genes: 2,730. Both inventory checkboxes, progress rows and exact merge receipts are recorded; earlier campaign observations and ClinGen association data are preserved.

- 2026-10-01 UTC: Recorded the verified BCKDK #3646 merge. Completion count: 146 → 147; original gene PR merges: 147 → 148; remaining catalog genes: 2,729. The inventory checkbox, progress row and exact merge receipt are recorded; earlier campaign observations and ClinGen association data are preserved.

- 2026-10-01 UTC: Recorded the verified BCL11B #3664 merge. Completion count: 147 → 148; original gene PR merges: 148 → 149; remaining catalog genes: 2,728. The inventory checkbox, progress row and exact merge receipt are recorded; earlier campaign observations and ClinGen association data are preserved.

- 2026-10-01 UTC: Recorded the verified BEST1 #3718 merge. Completion count: 148 → 149; original gene PR merges: 149 → 150; remaining catalog genes: 2,727. The inventory checkbox, progress row and exact merge receipt are recorded; earlier campaign observations and ClinGen association data are preserved.

- 2026-10-01 UTC: Recorded the verified BLNK #3741 merge. Completion count: 149 → 150; original gene PR merges: 150 → 151; remaining catalog genes: 2,726. The inventory checkbox, progress row and exact merge receipt are recorded; earlier campaign observations and ClinGen association data are preserved.

- 2026-10-01 UTC: Recorded the verified BICRA #3713 merge. Completion count: 150 → 151; original gene PR merges: 151 → 152; remaining catalog genes: 2,725. The inventory checkbox, progress row and exact merge receipt are recorded; earlier campaign observations and ClinGen association data are preserved.

- 2026-10-01 UTC: Recorded the verified BLTP1 #3796 merge. Completion count: 151 → 152; original gene PR merges: 152 → 153; remaining catalog genes: 2,724. The inventory checkbox, progress row and exact merge receipt are recorded; earlier campaign observations and ClinGen association data are preserved.

- 2026-10-01 UTC: Recorded verified merges for BLVRA #3775, BLOC1S5 #3781 and BLOC1S6 #3770. Completion count: 152 → 155; original gene PR merges: 153 → 156; remaining catalog genes: 2,721. Inventory checkboxes, progress rows and exact merge receipts are recorded; earlier campaign observations and ClinGen association data are preserved.

- 2026-10-02 UTC: Recorded the verified B4GALT1 #3576 merge. Completion count: 155 → 156; original gene PR merges: 156 → 157; remaining catalog genes: 2,720. All earlier checkpoint observations, ClinGen associations and the unresolved AKR1D1 follow-up are preserved.

### Selected work in progress — 2026-10-02 receipt update

These dated observations add no completion and do not revise checkpoint95 totals.

- BOLA3: Published exact native review; no merge counted. PR [#3860](https://github.com/ai4curation/ai-gene-review/pull/3860) at `71bdefc23e655305d6db8cc0c09b99fad0f3f6df`.
- PANTHER shared family review: Published family follow-up; latest saved review requests changes. This shared family repair does not count as a gene completion. PR [#3853](https://github.com/ai4curation/ai-gene-review/pull/3853) at `4827cd02fcdf19f552f5a40e6637253440dc7427`.
- BMPR1A: Initial review published; round-one follow-up passed distinct science review and awaits publication. No merge counted. PR [#3854](https://github.com/ai4curation/ai-gene-review/pull/3854) at `478ecef8f4ce509c5b4aecdab6424c234f56ddfb`.
- BRAF: Independent annotation candidate prepared in TMP for distinct science review; no publication or merge claimed.
- BMPR2 / Seed62: Recovery workflow completed successfully; artifact source inspection and canonical seed import remain pending. Workflow success is not gene-review completion. Run [36974959734](https://github.com/ai4curation/ai-gene-review/actions/runs/36974959734).

- 2026-10-02 UTC: Recorded the verified BMPR1A #3854 merge. Completion count: 156 → 157; original gene PR merges: 157 → 158; remaining catalog genes: 2,719. Its earlier in-progress receipt observation remains historical. All ClinGen associations, prior publication records and the unresolved AKR1D1 follow-up are preserved.

- 2026-10-02 UTC: Recorded verified BMP6 #3852, BOLA3 #3860 completion. Completed genes: 157 → 159; original gene PR merges: 158 → 160; remaining catalog genes: 2,717. All 169 prior queue entries, all ClinGen associations and the unresolved AKR1D1 follow-up remain unchanged. Family/index PRs do not increment the gene count.

- 2026-10-02 UTC: Recorded verified BLOC1S1 #3749 and ATP1A1 #3553 completion. Completed genes: 159 → 161; original gene PR merges: 160 → 162; remaining catalog genes: 2,715. Preserve all 171 prior queue entries: ATP1A1 gains a completion receipt and superseding lifecycle status, with its prior observation retained; the other 170 entries are unchanged. Add BLOC1S1 as the 172nd queue entry. All ClinGen associations, historical checkpoint95 totals and the unresolved AKR1D1 follow-up remain unchanged.

- 2026-10-02 UTC: Recorded 13 verified gene PR merges from the published161 checkpoint: ARMC9 #3371, ARL13B #3374, ASL #3385, ASNS #3438, ATP6AP1 #3550, AURKC #3568, AUTS2 #3569, BAG3 #3578, B9D1 #3579, BLOC1S3 #3758, BMP10 #3818, BMP4 #3851, ARID2 #3372. Completed genes: 161 → 174; original gene PR merges: 162 → 175; remaining catalog genes: 2,702. Preserve all 172 prior queue entries and their historical evidence, retaining superseded lifecycle observations; add BLOC1S3, BMP10 and BMP4 for 175 queue entries. All ClinGen associations, historical checkpoint95 totals, project curation instructions and the unresolved AKR1D1 follow-up remain unchanged.

- 2026-10-03 UTC: Recorded four confirmed gene merges through 2026-10-02 23:37:41 UTC: ATP7A #3561, ATP6V0A2 #3551, ATXN2 #3566, ATP7B #3560. Completion 174 → 178; original merges 175 → 179; remaining genes 2,698. All 175 queue entries, their historical fields, the ClinGen associations and unresolved AKR1D1 follow-up are preserved. The introductory 14-gene snapshot is explicitly historical. Session-local receipts are distinguished from durable merge/path/blob evidence, with precise per-gene checked scope. Biological DRAFT/UNDECIDED states are unchanged.

- 2026-10-03 UTC: Added confirmed BMPR2 #3878 merge ecd8e02fac9c through 2026-10-03 01:13:18 UTC. Completion 178 → 179; original merges 179 → 180; remaining 2,697. Added the 176th queue entry while preserving all 175 prior entries and the prior checkpoint 178 history. The exact 43-file merged scope, 15-path PR diff and actual biological COMPLETE/152 annotations/38 UNDECIDED are recorded separately. All 2,876 association rows, published task policy and the unresolved AKR1D1 follow-up remain unchanged except the BMPR2 completion checkbox. Checkpoints 178 and 179 are prepared for one combined tracker publication.

- 2026-10-03 UTC: Recorded the three independently confirmed B3GALNT2 #3563, APOB #3365 and BPTF #3880 merges through 04:40:38 UTC. Completion 179 → 182; original gene merges 180 → 183; 2,694 remain. Preserved all 2,876 association rows except these three checkboxes, all 176 existing queue entries with two superseded current statuses retained as historical observations, and all prior history. Added the 177th queue entry for BPTF. Biological statuses and unresolved assertions remain unchanged; BRAT1 is not counted. Updated the current table heading and the two stale APOB/B3GALNT2 pending rows, while preserving all dated verification log entries.

- 2026-10-03 UTC: Recorded BRAT1 #3884 and BRCA1 #3888 at the fixed 07:20:29 UTC evidence cutoff, including BRAT1 status correction #3892 with zero additional completion. Completion 182 → 184; original gene merges 183 → 185; 2,692 remain. Preserved all 2,876 association rows except the two checkboxes, all 177 prior queue entries and dated observations; appended BRAT1 and BRCA1 as entries 178–179. Both current biological statuses are DRAFT; uncertainty is preserved.

- 2026-10-03 09:08:30 UTC completion cut: BRCA2 #3893 advances checkpoint 184 → 185 complete, 186 original gene merges and 2,691 remaining. Preserve all 2,876 association rows except its checkbox and all 179 earlier queue entries. Add one completion entry plus separate BRIP1, BRD4 and BRPF1 work observations; their publication/review/source-run states do not constitute completion. [History](https://github.com/ai4curation/ai-gene-review/blob/main/history/projects/CLINGEN_MENDELIAN/2026-10-03T091329Z-codex-9a4324.yaml).

- 2026-10-03 10:42:33 UTC fixed completion cutoff: BRIP1 #3895 and BRD4 #3896 advance published checkpoint 185 → 187 complete, 188 original gene merges and 2,689 remaining. Exact approved heads, required CI, signed merges and 37 enumerated merged paths checked. All 2,876 associations and 180 prior queue entries preserved; only the two gene checkboxes change. Four pending-work observations add no completions. Unpublished 186 is superseded without a separate history or publication. [History](https://github.com/ai4curation/ai-gene-review/blob/main/history/projects/CLINGEN_MENDELIAN/2026-10-03T105722Z-codex-aeb9aa.yaml).

- 2026-10-03 12:33:32 UTC fixed completion cutoff: BRPF1 #3898, BRSK2 #3899, BRWD3 #3901 and BSCL2 #3902 advance checkpoint 187 → 191 complete, 192 original gene merges and 2,685 remaining. All 53 changed merge-path blobs, four source review projections and the durable merge identities were checked. All 2,876 associations, 182 earlier queue entries and old histories remain; pending genes stay unchecked. [History](https://github.com/ai4curation/ai-gene-review/blob/main/history/projects/CLINGEN_MENDELIAN/2026-10-03T125438Z-codex-ce3948.yaml).

- 2026-10-03 14:49:33 UTC fixed completion cutoff: BSND #3903, BTD #3904, BTK #3905, C19orf12 #3906 and BUB1B #3908 advance checkpoint 191 → 196 complete, 197 original gene merges and 2,680 remaining. Exact final-head approval/check success, signed merges and all 87 changed-path blobs were verified. All 2,876 inventory rows, 186 earlier queue entries, dated checkpoints and prior histories remain. AKR1D1 and other pending work stay excluded.

- 2026-10-03 16:43:30 UTC fixed completion cutoff: C1QA #3909, C1QB #3916, C1QTNF5 #3911, C2CD3 #3917 and C1QBP #3914 advance checkpoint 196 → 201 complete, 202 original gene merges and 2,675 remaining. Final-head approval/check success, signed merges and all 74 changed-path blobs were verified. All 2,876 inventory rows, 191 earlier queue entries, dated checkpoints and prior histories remain. Biological DRAFT statuses, 20 UNDECIDED assessments and C2CD3’s one reviewed NEW assertion remain as merged; AKR1D1 and pending work stay excluded.

- 2026-10-03 18:25:30 UTC fixed completion cutoff: C3 #3925 and C9orf72 #3927 advance checkpoint 201 → 203 complete, 204 original gene merges and 2,673 remaining. Signed merge identities and 90 changed-path blobs are verified with final-head approval and required-check success. Preserve 196 prior queue entries, all 2,876 inventory associations, both biological DRAFT statuses and 32 UNDECIDED assessments. CA5A, CA8 and other pending work contribute no completion. The prior checkpoint 201 history cross-link is now explicit.

- 2026-10-04 07:13:11 UTC fixed completion cutoff: CA5A #3928, CA8 #3929, CABP2 #3938, CACNA1B #3947, CACNA1D #3949, CAD #3980, CALM1 #3989, CACNA1E #4020, CACNA1G #4011, CALM2 #4018, CALM3 #4016, CACNA2D4 #4022, CACNA1C #3948 advance checkpoint 203 → 216 complete, 217 original gene merges and 2,660 remaining. Signed merge identities and 181 changed-path blobs are verified with final-head approval and required-check success. Preserve 198 prior queue entries, all 2,876 inventory associations, ten DRAFT and three COMPLETE biological review states, 60 UNDECIDED assessments and CA8’s two and CACNA2D4’s one NEW assertions. AKR1D1 remains excluded pending its required source follow-up. Other pending work contributes no completion at this cutoff.

- 2026-10-04 08:47:19 UTC fixed completion cutoff: CACNA1F #4024, CAMK2A #4043, CA2 #4042, CAMTA1 #4049 advance checkpoint 216 → 220 complete, 221 original gene merges and 2,656 remaining. Signed merge identities and 100 changed-path blobs are verified with final-head approval and required-check success. Preserve 211 prior queue entries, all 2,876 inventory associations, two DRAFT and two COMPLETE biological review states, 294 source assertions and 21 UNDECIDED assessments; no NEW assertions are introduced. AKR1D1 remains excluded pending its required source follow-up. Other pending work contributes no completion at this cutoff.

- 2026-10-04 11:36:42 UTC fixed completion cutoff: CANT1 #4071 and CAPN3 #4093 advance checkpoint 220 → 222 complete, 223 original gene merges and 2,654 remaining. Signed merge identities and 38 changed-path blobs are verified with final-head approval and required-check success. Preserve 215 prior queue entries, all 2,876 inventory associations, two DRAFT biological review states, 133 source assertions and 20 UNDECIDED assessments; no NEW assertions are introduced. AKR1D1 remains excluded pending its required source follow-up. Other pending work contributes no completion at this cutoff.

- 2026-10-04 12:47:21 UTC fixed completion cutoff: CAPN5 #4099 and CARD11 #4116 advance checkpoint 222 → 224 complete, 225 original gene merges and 2,652 remaining. Signed merge identities and 36 changed-path blobs are verified with final-head approval and required-check success. Preserve 217 prior queue entries, all 2,876 inventory associations, two DRAFT biological review states, 102 source assertions and 7 UNDECIDED assessments; no NEW assertions are introduced. AKR1D1 remains excluded pending its required source follow-up. Other pending work contributes no completion at this cutoff.

- 2026-10-04 14:10:18 UTC fixed completion cutoff: CARMIL2 #4121 advances checkpoint 224 → 225 complete, 226 original gene merges and 2,651 remaining. The signed merge identity and 16 changed-path blobs are verified with final-head approval and required-check success; all 18 scoped paths, including two reused sources, are verified. Preserve 219 prior queue entries, all 2,876 inventory associations, the DRAFT biological review state, 45 source assertions and 3 UNDECIDED assessments. One NEW molecular-function assertion (GO:0035591 signaling adaptor activity) brings the review to 46 annotations; no new biological-process assertion is introduced. AKR1D1 remains excluded pending its required source follow-up. Other pending work contributes no completion at this cutoff.

- 2026-10-04 15:17:41 UTC fixed completion cutoff: CASK #4132, CASP8 #4139 and CASQ2 #4142 advance checkpoint 225 → 228 complete, 229 gene-level original reviews and 2,648 remaining. The planned 227 total omitted CASP8, whose original #3672 was never campaign-complete in the published inventory or queue; accepted revision #4139 counts once, not as a second original review. All 51 changed and 149 reused scope objects are enumerated and verified against signed merges, current-head approval and successful required CI. Preserve 220 prior queue entries, all 2,876 gene inventory entries and their frozen associations, the exact corrected CARMIL2 reuse maps, all prior histories, three DRAFT states, 439 source assertions, 64 UNDECIDED assessments and no NEW assertions. AKR1D1 remains excluded pending its required source follow-up.

- 2026-10-04 19:58:03 UTC fixed completion cutoff: CASR #4147, CAV1 #4165 and CAVIN1 #4180 advance checkpoint 228 → 231 complete, 232 gene-level original reviews and 2,645 remaining. All 111 changed and 70 reused scoped objects are enumerated and verified against signed merges, final-head approval and successful required CI. CAVIN1’s 15-path PR has 12 actual merge changes after three exact source reuses; these remain explicit. Preserve 223 prior queue entries, all 2,876 gene inventory entries and their frozen associations, the CASP8 count correction, both corrected CARMIL2 reuse maps and all prior histories. Retain three DRAFT states, 473 original source assertions, 82 UNDECIDED assessments and CAVIN1’s one reviewed NEW caveola-assembly assertion. AKR1D1 and all open work remain excluded.

- 2026-10-04 23:39:16 UTC fixed cutoff: CAV3 #4175, CBS #4191, CBFB #4215, CBL #4210, CCDC39 #4228 and CC2D2A #4209 advance checkpoint 231 → 237 complete, 238 gene-level original reviews and 2,639 remaining. All 144 changed and 244 reused scoped objects are enumerated and verified against signed merges, final-head approval and successful required CI. Preserve 226 prior queue entries, all 2,876 gene inventory entries and their frozen associations, the CASP8 correction, both CARMIL2 reuse maps and all earlier histories. The merged reviews retain 707 original source assertions, 64 UNDECIDED assessments, five DRAFT states and one COMPLETE state; the two NEW-labelled rows comprise CBL’s historical proposal and CCDC39’s structural molecular-function addition. AKR1D1 and work outside this fixed cutoff remain excluded.

- 2026-10-05 01:02:15 UTC fixed cutoff: CC2D1A #4222, CCDC40 #4235 and CCND2 #4244 advance checkpoint 237 → 240 complete, 241 gene-level original reviews and 2,636 remaining. All 27 changed and 44 reused scoped objects are enumerated and verified against signed merges, final-head approval and successful required CI. Preserve 232 prior queue entries, all 2,876 gene inventory entries and their frozen associations, the CASP8 correction, both CARMIL2 reuse maps and all earlier histories. The three DRAFT reviews retain 131 source assertions and nine UNDECIDED assessments; CC2D1A contributes one reviewed NEW signaling-adaptor molecular function, giving 132 total assertions. Preserve the checkpoint 237 post-merge-race supplemental proof and original failed guard without counting external CD48 work. AKR1D1 and work outside this cutoff remain excluded.

## Completion checkpoint 413 — 2026-10-14 01:31:47 UTC

**413 complete; 2,463 remaining out of 2,876 primary catalogue genes.**
The 19 distinct additions below extend merged checkpoint 394. The completion
cutoff is [CTCF merge 5e2706cd8198](https://github.com/ai4curation/ai-gene-review/commit/5e2706cd819805cc1e881da111e9418779254827).
The source tracker [#4988](https://github.com/ai4curation/ai-gene-review/pull/4988)
merged later as [488cf4ada7bb](https://github.com/ai4curation/ai-gene-review/commit/488cf4ada7bb34f80c7bdaeeb1e8228020852bce),
at 2026-10-14 02:23:05 UTC. These are deliberately different boundaries.

Rendering availability is separate from completion credit. The committed main-page render changed from 1,788 to 1,769 missing-review warnings (19 cleared; none added). Sixteen cleared warnings belong to the 19 counted genes; CPS1, CPT2 and CSF1R were already linked before this render. The other three cleared warnings are ADAM17, RIPK1 and RORB: their review links became available, but they remain unchecked and receive no completion credit. Under the same frozen 2,924-review inventory, a fresh baseline render also has 1,769 warnings, equal to the checkpoint render; that fresh-render comparison does not erase the committed 1,788-to-1,769 change. The progress page has zero rendering warnings.

| Gene | Review PR | Approved head | Actual merge | Merged UTC | Full PR paths / parent delta |
| --- | --- | --- | --- | --- | --- |
| CPS1 | [#4967](https://github.com/ai4curation/ai-gene-review/pull/4967) | `c758f4c5f7d5` | [350e9e3a9958](https://github.com/ai4curation/ai-gene-review/commit/350e9e3a995808131367317a88cba2a3580aa508) | 2026-10-13 16:55:45 | 45 / 45 |
| CPT2 | [#4969](https://github.com/ai4curation/ai-gene-review/pull/4969) | `6885166bdbc8` | [7cb48b0a7894](https://github.com/ai4curation/ai-gene-review/commit/7cb48b0a78940956d8a171dc20b29da345ade85b) | 2026-10-13 17:14:48 | 21 / 21 |
| CR2 | [#4970](https://github.com/ai4curation/ai-gene-review/pull/4970) | `bd4986696bf5` | [444bd0a2197e](https://github.com/ai4curation/ai-gene-review/commit/444bd0a2197eb08062e2aebf7d8e6cea0aa378cd) | 2026-10-13 17:41:25 | 23 / 23 |
| CRADD | [#4971](https://github.com/ai4curation/ai-gene-review/pull/4971) | `44fd6c512ff6` | [c8be91268fbf](https://github.com/ai4curation/ai-gene-review/commit/c8be91268fbf9d87afd6df3868e6a97463292bdc) | 2026-10-13 18:03:33 | 27 / 27 |
| CRB1 | [#4973](https://github.com/ai4curation/ai-gene-review/pull/4973) | `983cd30d33ac` | [2fb75d4c8ec7](https://github.com/ai4curation/ai-gene-review/commit/2fb75d4c8ec72ff98f8a1c336f902cb89594cc75) | 2026-10-13 18:29:32 | 27 / 27 |
| CRB2 | [#4974](https://github.com/ai4curation/ai-gene-review/pull/4974) | `7eef84585f12` | [38361ca08760](https://github.com/ai4curation/ai-gene-review/commit/38361ca08760238b2fc74085bb8f603c5be1ef52) | 2026-10-13 18:57:05 | 24 / 20 |
| CRPPA | [#4976](https://github.com/ai4curation/ai-gene-review/pull/4976) | `bd638a9dbaa8` | [d73f140b43a6](https://github.com/ai4curation/ai-gene-review/commit/d73f140b43a67a8509e25fa3d13fa72ca5b05dd4) | 2026-10-13 19:23:15 | 12 / 12 |
| CREBBP | [#4975](https://github.com/ai4curation/ai-gene-review/pull/4975) | `59a37cf72359` | [55b67a6a02e0](https://github.com/ai4curation/ai-gene-review/commit/55b67a6a02e07a5bfc9fcf5c0b5a2185f5499b8a) | 2026-10-13 19:50:48 | 99 / 99 |
| CRX | [#4977](https://github.com/ai4curation/ai-gene-review/pull/4977) | `657584bac14a` | [314e2c866be9](https://github.com/ai4curation/ai-gene-review/commit/314e2c866be9f8861e20e84c96f0a7db64f0fb3c) | 2026-10-13 20:18:16 | 21 / 21 |
| CSDE1 | [#4978](https://github.com/ai4curation/ai-gene-review/pull/4978) | `63cfd2557543` | [980669d44911](https://github.com/ai4curation/ai-gene-review/commit/980669d44911afeca6c093c06bf0c73732e853a3) | 2026-10-13 20:40:02 | 15 / 14 |
| CSF2RA | [#4980](https://github.com/ai4curation/ai-gene-review/pull/4980) | `228baf4cb705` | [967b016268fc](https://github.com/ai4curation/ai-gene-review/commit/967b016268fc03aa43ece65b281861622d075326) | 2026-10-13 21:06:27 | 26 / 26 |
| CSF1R | [#4979](https://github.com/ai4curation/ai-gene-review/pull/4979) | `705af916d431` | [e2fdd68e95ed](https://github.com/ai4curation/ai-gene-review/commit/e2fdd68e95edcc9aeb931ed1356f97dc44c2d614) | 2026-10-13 21:28:59 | 10 / 10 |
| CSF2RB | [#4981](https://github.com/ai4curation/ai-gene-review/pull/4981) | `70a5ca76f485` | [ab45ccd17825](https://github.com/ai4curation/ai-gene-review/commit/ab45ccd1782535d4f608b9cea776c4299557d000) | 2026-10-13 21:49:55 | 35 / 27 |
| CSNK2A1 | [#4982](https://github.com/ai4curation/ai-gene-review/pull/4982) | `4855783f0a0b` | [27eca918c9f0](https://github.com/ai4curation/ai-gene-review/commit/27eca918c9f01a10c5eb9eab099626c5012f7792) | 2026-10-13 22:17:53 | 36 / 36 |
| CSPP1 | [#4983](https://github.com/ai4curation/ai-gene-review/pull/4983) | `b27ea22b9780` | [1baaa9693348](https://github.com/ai4curation/ai-gene-review/commit/1baaa96933489886741d2c1de028e56002b64031) | 2026-10-13 22:43:38 | 19 / 19 |
| CSRP3 | [#4984](https://github.com/ai4curation/ai-gene-review/pull/4984) | `767e5bd09051` | [211f2c2993a0](https://github.com/ai4curation/ai-gene-review/commit/211f2c2993a0cfb09e3ecac17b666a48046356c0) | 2026-10-13 23:04:16 | 18 / 18 |
| CSTB | [#4985](https://github.com/ai4curation/ai-gene-review/pull/4985) | `74f03ecb03b3` | [b0f4c5769323](https://github.com/ai4curation/ai-gene-review/commit/b0f4c576932331a543869e29164a637ebd800591) | 2026-10-13 23:28:57 | 16 / 16 |
| CTC1 | [#4986](https://github.com/ai4curation/ai-gene-review/pull/4986) | `3bdb911d96e3` | [aebcb27ec7bb](https://github.com/ai4curation/ai-gene-review/commit/aebcb27ec7bb32cf0ea35df23a9bc76569addd2a) | 2026-10-13 23:55:58 | 28 / 28 |
| CTCF | [#4987](https://github.com/ai4curation/ai-gene-review/pull/4987) | `12c2f7bbab59` | [5e2706cd8198](https://github.com/ai4curation/ai-gene-review/commit/5e2706cd819805cc1e881da111e9418779254827) | 2026-10-14 01:31:47 | 31 / 31 |

Every listed gene has accepted final-head approval, required CI and an actual
merge. Complete PR-path modes, types and blobs match the approved head at the
merge; parent-relative deltas contain no unaccounted paths. The combined proof
covers 533 full PR-path occurrences,
520 changed-path occurrences and
13 paths already identical in their
respective parents. The [queue JSON](publication-queue.json) records complete
heads, merge IDs, approval/comment IDs and test-job locators.

This is an identity-based reconciliation. CPAMD8 was already corrected into
checkpoint 394 and remains counted once. CPS1 was still unchecked in that
merged tracker and is included here. Earlier local numerical receipts predate
the CPAMD8 correction; their original bytes and counters are preserved rather
than treated as new identities automatically.

The prior tracker passed its [ordinary merge-queue test](https://github.com/ai4curation/ai-gene-review/actions/runs/38499021750/job/115641288386).
Its later [main-push test](https://github.com/ai4curation/ai-gene-review/actions/runs/38500737166/job/115646989334)
failed only the sorted/deduplicated GO-cache test: GO:0140632 precedes GO:0140619,
and GO:0006910 and GO:0097528 are duplicated. Exact committed parent 99d78b3 and
merge 488cf4a have identical cache bytes and reproduce those three findings;
the seven tracker paths did not introduce them. The reason the queue run passed
on the same merge commit is not established. This checkpoint preserves that
failed historical result and does not claim a successful post-main test.

All 235 historical queue records, all 73 prior completion updates, every earlier
progress paragraph and all 161 existing project history records remain
unchanged. The 2,876 HGNC identities and association texts are unchanged; only
the 19 unchecked entries above become checked. No queued or merely published
gene, including CTNNA1 or CTNNB1, receives completion credit. Existing review
status labels do not substitute for the accepted source-specific reviews and
merge evidence. No new gene annotation decision is made by this tracker update.

The complete 20-commit interval audit now resolves to these 19 accepted gene
reviews and the LRV tooling upgrade [#4947](https://github.com/ai4curation/ai-gene-review/pull/4947).
CSF1R and CSF2RB were initially withheld from an unpublished 411-gene preparation.
Their full approved-head, ordinary-queue, later main-push and merged-path proofs
have since been accepted, so both are counted here once. That preparation remains
preserved separately; it was not a published tracker checkpoint. The completion
cutoff remains CTCF, and the later CTLA4 merge is outside this snapshot.

[Curation session](https://github.com/ai4curation/ai-gene-review/blob/cmungall/clingen-tracker-413-20261014/history/projects/CLINGEN_MENDELIAN/2026-10-14T032418Z-codex-815c48.yaml)

## Completion checkpoint 425 — 2026-10-14 07:48:59 UTC

**425 complete; 2,451 remaining out of 2,876 primary catalogue genes.**
The 12 distinct additions below extend merged checkpoint 413. The completion
cutoff is [CUL3 699711b0e7d1](https://github.com/ai4curation/ai-gene-review/commit/699711b0e7d1c66b75bfe0d74fcc965f035741f6);
this is a receipt-based snapshot, not an exhaustive claim about every repository
review merge. Source and rendering context are frozen at main `99a36bd05946bbd4d66a3a7e47b3260072c2e9c7`.
ROOT, the coordinating AI agent, accepted each complete merge proof; this is
not a claim of human maintainer review.

Rendering availability is separate from completion credit. The committed main-page render has 1,769 missing-review warnings; the fresh baseline and checkpoint renders under the same frozen 2,946-review inventory have 1,751 (18 cleared; none added). Eight cleared warnings belong to these 12 counted genes. CTLA4, CTNNA1, CTNNB1, CUL3 were already linked. The other ten cleared warnings are CHM, CHST3, CIC, LDLR, LIPA, MSX1, PAX7, PCSK9, PNPLA2, TFAP2B: their review links became available, but they remain unchecked and receive no completion credit. This same-context comparison does not erase the committed-to-fresh change. The progress page has zero rendering warnings.

| Gene | PR | Approved head | Merge | Merged UTC | Full PR / parent delta paths |
| --- | --- | --- | --- | --- | --- |
| CTLA4 | [#4989](https://github.com/ai4curation/ai-gene-review/pull/4989) | `57752c15ea12` | [de285b1f26a4](https://github.com/ai4curation/ai-gene-review/commit/de285b1f26a49ab92ef3493c96186873be1718ef) | 2026-10-14 02:48:02 | 10 / 10 |
| CTNNB1 | [#4991](https://github.com/ai4curation/ai-gene-review/pull/4991) | `6fcafcde4ce0` | [4ad9a0175d31](https://github.com/ai4curation/ai-gene-review/commit/4ad9a0175d31b7c85bda696abfaf414c413b8a75) | 2026-10-14 03:16:44 | 12 / 12 |
| CTNND1 | [#4992](https://github.com/ai4curation/ai-gene-review/pull/4992) | `f0d2744ed575` | [7d5c823e80e3](https://github.com/ai4curation/ai-gene-review/commit/7d5c823e80e375030346000b5c8bf882c9dc5d29) | 2026-10-14 03:44:07 | 36 / 36 |
| CTPS1 | [#4993](https://github.com/ai4curation/ai-gene-review/pull/4993) | `cdc7baa1e1ab` | [22a69a66d01f](https://github.com/ai4curation/ai-gene-review/commit/22a69a66d01fb20ab1131fa48a251f4f39b97d16) | 2026-10-14 04:11:24 | 22 / 22 |
| CTNNA1 | [#4990](https://github.com/ai4curation/ai-gene-review/pull/4990) | `1bcc46b740d1` | [1a622391f31c](https://github.com/ai4curation/ai-gene-review/commit/1a622391f31c5ae8b75b639a9fb5165dcb7feb3a) | 2026-10-14 04:30:33 | 18 / 18 |
| CTSA | [#4994](https://github.com/ai4curation/ai-gene-review/pull/4994) | `036501714ac7` | [08e2a9d6fda7](https://github.com/ai4curation/ai-gene-review/commit/08e2a9d6fda7fbb0ab2f6becc30c63a47f70d92a) | 2026-10-14 04:50:11 | 17 / 17 |
| CTSF | [#4996](https://github.com/ai4curation/ai-gene-review/pull/4996) | `3eb0187853a4` | [9d1bdc6f9151](https://github.com/ai4curation/ai-gene-review/commit/9d1bdc6f9151f1c28406d62a1e4a37ca3ea549c1) | 2026-10-14 05:17:16 | 19 / 19 |
| CTSD | [#4995](https://github.com/ai4curation/ai-gene-review/pull/4995) | `8629b15c70da` | [4d4ed80803ac](https://github.com/ai4curation/ai-gene-review/commit/4d4ed80803ac7c79b4fc6125b23ced29dca6e1a5) | 2026-10-14 05:37:16 | 24 / 23 |
| CTSK | [#4997](https://github.com/ai4curation/ai-gene-review/pull/4997) | `1ec38baa28f8` | [cb8992c9155e](https://github.com/ai4curation/ai-gene-review/commit/cb8992c9155ed1e77dc9e56e0662743d696417b9) | 2026-10-14 06:26:56 | 23 / 22 |
| CUL4B | [#5000](https://github.com/ai4curation/ai-gene-review/pull/5000) | `b1ff3a07748d` | [f4ad933c9bc4](https://github.com/ai4curation/ai-gene-review/commit/f4ad933c9bc45503afa2035b14da90c8315e1f4b) | 2026-10-14 06:53:48 | 9 / 9 |
| CWF19L1 | [#5002](https://github.com/ai4curation/ai-gene-review/pull/5002) | `fd2ac6bba817` | [6f3803683c26](https://github.com/ai4curation/ai-gene-review/commit/6f3803683c260f80cad882798cdb1edbac8d8fe4) | 2026-10-14 07:20:56 | 13 / 13 |
| CUL3 | [#5001](https://github.com/ai4curation/ai-gene-review/pull/5001) | `757d855a65ce` | [699711b0e7d1](https://github.com/ai4curation/ai-gene-review/commit/699711b0e7d1c66b75bfe0d74fcc965f035741f6) | 2026-10-14 07:48:59 | 12 / 12 |

Every listed gene has final approval on its exact head, a successful ordinary
merge-queue test and a separate successful post-merge main-push test. Queue
jobs passed the full test suite. Post-main scopes are recorded per gene in the
[queue JSON](publication-queue.json); successful scoped-only runs are not
represented as full-suite runs. All 215 full PR-path occurrences match the
approved modes, types and blobs at merge. The exact parent deltas contain
213 changed-path occurrences; 2 PR paths were already identical in
their respective parents. No unaccounted parent changes were accepted.

The prior checkpoint 413 tracker [#4999](https://github.com/ai4curation/ai-gene-review/pull/4999)
merged at `b9da9839c93ff74b6be6cf30102747f8973984f2` with its eight approved paths exact.
Its queue and separate main-push full suites succeeded after the independent
GO-cache repair. This later success does not rewrite the failed historical
checkpoint 394 post-main test recorded above.

All 235 historical queue records, all 74 prior completion updates, the complete
previous progress text, all 163 existing project history records and the frozen
catalogue source files remain unchanged. The 2,876 HGNC identities and their
association text are preserved; only these 12 unchecked identities become
checked. CYB5A, CWC27 and other published or available reviews receive no
completion credit in this snapshot. No gene annotation or source is changed.

[Curation session](https://github.com/ai4curation/ai-gene-review/blob/cmungall/clingen-tracker-425-20261015/history/projects/CLINGEN_MENDELIAN/2026-10-15T143837Z-codex-94c5f2.yaml)

## Completion checkpoint 426 — 2026-10-16 10:41:28 UTC

**426 complete; 2,450 remaining out of 2,876 primary catalogue genes.**
Only CWC27 is added to the 425 checked genes in tracker [#5034](https://github.com/ai4curation/ai-gene-review/pull/5034),
whose exact approved head was `48efb320877bcbe219856ddcef8c5af42c8bbe5e` and which subsequently
merged as [56a970dd16a3](https://github.com/ai4curation/ai-gene-review/commit/56a970dd16a33e4685edc8b23bd9d1303d7e7e6a).
Tracker publication itself does not add gene credit. The completion cutoff is
the CWC27 merge below; this is not an exhaustive claim about every repository
review merge. ROOT, the coordinating AI agent, accepted this completion proof.

| Gene | PR | Approved head | Merge | Merged UTC | Full PR / parent delta paths |
| --- | --- | --- | --- | --- | --- |
| CWC27 | [#5003](https://github.com/ai4curation/ai-gene-review/pull/5003) | `c75d783131ad` | [8b87c39aea83](https://github.com/ai4curation/ai-gene-review/commit/8b87c39aea838985bfff03d14cc3bb13ac93f582) | 2026-10-16 10:41:28 | 9 / 9 |

The [final formal approval](https://github.com/ai4curation/ai-gene-review/pull/5003#pullrequestreview-5534904007)
and [complete detailed review](https://github.com/ai4curation/ai-gene-review/pull/5003#issuecomment-6194574317)
clear all prior scientific blockers on that exact head. Required
[PR validation](https://github.com/ai4curation/ai-gene-review/actions/runs/38751823079)
passed. The [ordinary merge-group run](https://github.com/ai4curation/ai-gene-review/actions/runs/38885535910)
passed all-gene schema validation, examples and the full test suite before merge.
The separate [post-main push run](https://github.com/ai4curation/ai-gene-review/actions/runs/38888888905)
then materialized the exact merged commit and passed scoped CWC27 and history
validation. Its full test suite was skipped for the source-only push, not rerun.

All nine approved file modes, types and blobs equal the merged full PR paths,
and the actual parent delta contains exactly nine paths. Prior substantive
source review, the final Figure S1 locator correction, all 16 original source
objects, two official products and the explicit isoform-scoped new molecular
function are retained. Derived DRAFT reflects a nonblocking secondary-research
citation advisory, not an unresolved action or outstanding scientific blocker.
This completion follows validated final review, cleared actionable feedback and
merger; it does not infer completion from a status label alone.

All 2,876 catalogue identities and association texts, all 235 historical queue
records, all 75 prior completion updates and the entire previous progress text
remain unchanged. Only the previously unchecked CWC27 identity becomes checked.
Earlier statements excluding CWC27 remain historical checkpoint records.
Review-link availability and rendering warnings remain separate from completion;
no other gene is counted by this update. All earlier project history records
remain append-only and no gene annotation or source file changes.

Rendering availability remains separate from completion credit. The committed main-page render contains 1,751 missing-review warnings; the fresh baseline and checkpoint 426 render under the same frozen 2,966-human-review inventory contain 1,733 (18 cleared; none added). The cleared genes are CYB5A, DNAH17, DNAH8, FBXL4, MT-TC, MT-TH, MT-TK, MT-TL1, MT-TM, MT-TQ, MT-TS1, MT-TS2, MT-TV, MT-TW, MTFMT, SUCLA2, TARS2, TRMT10C. All remain unchecked and receive no completion credit here. CWC27 was already linked; its newly recorded completion follows the accepted merge evidence. The progress page has zero rendering warnings.

[Curation session](https://github.com/ai4curation/ai-gene-review/blob/cmungall/clingen-tracker-426-20261016/history/projects/CLINGEN_MENDELIAN/2026-10-16T114448Z-codex-51b38b.yaml)

## Completion checkpoint 427 — 2026-10-16 11:40:12 UTC

**427 complete; 2,449 remaining out of 2,876 primary catalogue genes.**
Only CYB5A is added to the 426 checked genes in tracker [#5053](https://github.com/ai4curation/ai-gene-review/pull/5053),
using its exact checkpoint-426 head `7173ebea8f29d62fb2f17eeb755e8f0c0f225d38` as the preimage.
This is a follow-up on that existing tracker PR. Tracker publication itself
adds no gene credit. ROOT, the coordinating AI agent, accepted the independent
completion proof; this is not a human maintainer sign-off.

| Gene | PR | Approved head | Merge | Merged UTC | Full PR / parent delta paths |
| --- | --- | --- | --- | --- | --- |
| CYB5A | [#5033](https://github.com/ai4curation/ai-gene-review/pull/5033) | `a0cbfb16972e` | [782b3b5a78c7](https://github.com/ai4curation/ai-gene-review/commit/782b3b5a78c788e9c88c99b98aae2baa0af3dba0) | 2026-10-16 11:40:12 | 21 / 21 |

The [final formal approval](https://github.com/ai4curation/ai-gene-review/pull/5033#pullrequestreview-5535363788)
and [complete detailed review](https://github.com/ai4curation/ai-gene-review/pull/5033#issuecomment-6195231459)
clear the four prior scientific blockers on that exact head. Three residual
presentation/exception suggestions are explicitly optional; there are no open
review threads. Required [PR validation](https://github.com/ai4curation/ai-gene-review/actions/runs/38756453055)
passed. The [merge-group run](https://github.com/ai4curation/ai-gene-review/actions/runs/38892124958)
passed scoped gene/history validation, all-gene schema validation, examples,
the full test suite and automation checks. The separate
[actual-main push run](https://github.com/ai4curation/ai-gene-review/actions/runs/38895302561)
then materialized the same merged commit and passed scoped CYB5A and history
validation, completing at 11:45:27 UTC. Its full test suite was skipped by the
workflow; it is not represented as a full-suite rerun.

All 21 approved file modes, types and blobs equal the merged full PR paths,
and the actual parent delta contains exactly those 21 additions. All four final
review/notes/source-guide/render artifacts are exact, as are 24 protected
scientific paths. The accepted science preserves 21 original annotation source
objects, 23 reference identities, all three official product identities and
three exact quotations, with one explicitly homolog-inferred electron-transfer
assertion. The review's DRAFT status and three justified UNDECIDED annotations
remain biological/source-access statements, not outstanding required feedback.
The seven documented validation advisories are unchanged and nonblocking.

All 2,876 catalogue identities and association texts, all 235 historical queue
records, all 76 prior completion updates, the entire preceding progress text
(including checkpoint 426), and all existing project histories remain unchanged.
Only the previously unchecked CYB5A identity becomes checked. Earlier statements
excluding CYB5A retain their historical checkpoint scope. No gene annotations,
source caches or earlier histories change.

The rendering inventory remains frozen at main `782b3b5a78c788e9c88c99b98aae2baa0af3dba0`:
7,824 total review YAMLs and 2,966 human review YAMLs. The checkpoint-426 baseline
has 1,733 main-page missing-review warnings and zero progress-page warnings.
No availability change is proposed here; ROOT will derive the two updated HTML
pages in this same inventory and record their actual results separately.

The final render passed all eight frontmatter checks and reproduced exactly the baseline warning lists: 1,733 for the main page and zero for the progress page. The completion counts are 427 checked and 2,449 unchecked catalogue genes.

[Curation session](https://github.com/ai4curation/ai-gene-review/blob/cmungall/clingen-tracker-426-20261016/history/projects/CLINGEN_MENDELIAN/2026-10-16T120914Z-codex-756f94.yaml)

## Completion checkpoint 428 — 2026-10-16 12:05:50 UTC

**428 complete; 2,448 remaining out of 2,876 primary catalogue genes.**
Only CXCR4 is added to checkpoint 427 in tracker [#5053](https://github.com/ai4curation/ai-gene-review/pull/5053).
The exact prior tracker head is `d69551859e986bbcb2e37d44ae14daebf7fd9851`. ROOT, the coordinating
AI agent, accepted the independent completion audit; this is not a human
maintainer sign-off. The entire prior checkpoint 426 and 427 record is preserved.

| Gene | PR | Approved head | Merge | Merged UTC | Full PR / parent delta paths |
| --- | --- | --- | --- | --- | --- |
| CXCR4 | [#5035](https://github.com/ai4curation/ai-gene-review/pull/5035) | `f019a43cbb9c` | [9cff2a2e29e9](https://github.com/ai4curation/ai-gene-review/commit/9cff2a2e29e9221d04e45143abb00951b0277a49) | 2026-10-16 12:05:50 | 54 / 54 |

The [final formal approval](https://github.com/ai4curation/ai-gene-review/pull/5035#pullrequestreview-5536596991)
and [complete detailed review](https://github.com/ai4curation/ai-gene-review/pull/5035#issuecomment-6197047569)
resolve the six prior review requests on that exact head. There are no open
review threads; the remaining presentation suggestions are optional.
[Required PR validation](https://github.com/ai4curation/ai-gene-review/actions/runs/38769178578)
passed. The [merge-group run](https://github.com/ai4curation/ai-gene-review/actions/runs/38895306397)
passed scoped gene/history validation, all-gene schema validation, examples,
3,889 tests and 251 automation tests. The separate
[actual-main push run](https://github.com/ai4curation/ai-gene-review/actions/runs/38898166465)
validated the merged CXCR4 and history files, completing at 12:12:56 UTC.
The full suite was skipped on that push; its successful execution belongs to
the merge-group run.

All 54 approved file modes, types and blobs equal the merged full PR paths
and the complete actual parent delta. The accepted science preserves all 117
annotation source objects, both official products, 79 reference identities,
19 exact excerpts and one core. The original 118 GOA rows deterministically
seeded 117 objects through one duplicate collapse. All 84 protected scientific
paths remain exact. Five justified UNDECIDED decisions, DRAFT status and two
nonblocking validation advisories remain explicit; none is unresolved required
feedback. The review comment's count of eight new excerpts is an arithmetic
slip: the verified inventory is 12 prior plus seven new, totaling 19.

### Current render inventory and correction of the prior freeze

The checkpoint-427 render was frozen at main `782b3b5a78c788e9c88c99b98aae2baa0af3dba0` even though its
branch had already incorporated the CXCR4 merge. Its 7,824 total / 2,966 human
inventory and 1,733 warnings describe that historical render only. They do not
describe the current branch. This appended disclosure corrects the current
state without rewriting either earlier checkpoint or history record.

The branch now has **7,825 review YAMLs, including 2,967 human reviews**, exactly
matching main `9cff2a2e29e9221d04e45143abb00951b0277a49`. CXCR4 is the sole added review since the
checkpoint-427 inventory and must become a link instead of a missing-review
warning. The complete tracker PR therefore has **19 cumulative availability
gains**, reducing the prior-main warning list from 1,751 to **1,732**, with no
new missing reviews. The 19 are CXCR4, CYB5A, DNAH17, DNAH8, FBXL4, MT-TC, MT-TH, MT-TK, MT-TL1, MT-TM, MT-TQ, MT-TS1, MT-TS2, MT-TV, MT-TW, MTFMT, SUCLA2, TARS2, TRMT10C.
The incremental change since checkpoint 427 is one link and one removed warning,
CXCR4. These are exact Git-inventory and frontmatter-path results; ROOT will
regenerate both HTML pages against the current branch and record the actual
1,732 / zero warning results before publication.

Availability and accepted completion are separate. CXCR4 is checked here only
because its independent audit and separate actual-main validation are now
accepted, not because its YAML is present. The earlier request to leave it
unchecked correctly described the pre-audit boundary. No other available review
receives credit. All 2,876 catalogue identities and association texts, all 235
historical queue objects, all 77 prior completion updates, the full preceding
progress text and all 166 prior project histories remain unchanged. Existing
cosmetic spacing in historical queue/history text remains preserved.

The final render passed all eight frontmatter checks and cleared exactly the stale CXCR4 availability warning: 1,732 warnings remain for the main page and zero for the progress page. The actual branch inventory contains 7,825 reviews, including 2,967 human reviews. The completion counts are 428 checked and 2,448 unchecked catalogue genes.

[Curation session](https://github.com/ai4curation/ai-gene-review/blob/cmungall/clingen-tracker-426-20261016/history/projects/CLINGEN_MENDELIAN/2026-10-16T124217Z-codex-d73d47.yaml)

## Completion checkpoint 430 — 2026-10-17 05:42:20 UTC

**430 complete; 2,446 remaining out of 2,876 primary catalogue genes.**
CYFIP2 and CYB5R3 are the only additions to checkpoint 428 on tracker
[#5053](https://github.com/ai4curation/ai-gene-review/pull/5053), whose prior head is
`2409002e46c2034acd6d9fcabd7b7d76c3b3fae9`. ROOT accepted both completion audits at 2026-10-17T05:52:50.199573+00:00.
ROOT is the coordinating AI agent; this records verified provenance and is not
a human maintainer sign-off. All earlier checkpoint text remains unchanged.

| Gene | PR | Approved head | Merge | Merged UTC | Full PR / parent delta paths | Actual-main validation |
| --- | --- | --- | --- | --- | --- | --- |
| CYFIP2 | [#5037](https://github.com/ai4curation/ai-gene-review/pull/5037) | `3184ce0f9edd` | [74290d411a6f](https://github.com/ai4curation/ai-gene-review/commit/74290d411a6ff4e547b9454a373c9677c963c22e) | 2026-10-17T00:11:09Z | 19 / 19 | [run 38985181650](https://github.com/ai4curation/ai-gene-review/actions/runs/38985181650) |
| CYB5R3 | [#5036](https://github.com/ai4curation/ai-gene-review/pull/5036) | `2ce15d1c9773` | [04ba970bf897](https://github.com/ai4curation/ai-gene-review/commit/04ba970bf8973abdda90bf8bbf3349870ee014ef) | 2026-10-17T05:42:20Z | 22 / 21 | [run 39007238786](https://github.com/ai4curation/ai-gene-review/actions/runs/39007238786) |

The [CYFIP2 approval](https://github.com/ai4curation/ai-gene-review/pull/5037#pullrequestreview-5537492723)
applies to the exact 19-file approved head, and all 19 merged files match it.
Its separate main push [test job](https://github.com/ai4curation/ai-gene-review/actions/runs/38985181650/job/117254874615)
completed successfully at 2026-10-17T00:16:42Z.
All 28 protected scientific source paths remained exact. Five documented
validation advisories remain; they are not unresolved required feedback.

The [CYB5R3 approval](https://github.com/ai4curation/ai-gene-review/pull/5036#pullrequestreview-5543953732)
applies to all 22 final PR paths. The actual merge changes 21 paths because the
identical shared `reactome/R-HSA-198824.md` cache was already on parent main.
All 22 final modes, types and blobs still equal the approved files, and all 37
protected scientific source paths remained exact. The separate main push
[test job](https://github.com/ai4curation/ai-gene-review/actions/runs/39007238786/job/117322091749) completed
successfully at 2026-10-17T05:48:10Z.
Its 33 documented validation advisories remain explicit. The completion audits
check the scoped gene and history validation in these actual-main jobs; the job
name is not used to claim a full-suite run.

### Current review availability

The tracker head contains 7,825 review YAMLs, including 2,967 human reviews.
Current main `04ba970bf8973abdda90bf8bbf3349870ee014ef` contains **7,856 review YAMLs,
including 2,997 human reviews**. The tracker branch has no gene changes since
its merge base, and main has not changed the selected tracker target files.
ROOT will incorporate current main and render the project against that actual
inventory. The exact frontmatter/path comparison predicts **1,716 missing-review
warnings**, down from 1,732 at checkpoint 428, and zero progress-page warnings.
These are expected results from Git paths, not a claim that this owner ran the
renderer. ROOT records the actual render results before publication.

The 16 newly available catalogue reviews are AGA, CTNS, CYB5R3, CYFIP2, CYP27B1, FBP1, FUCA1, GALNT3, GNPTAB, HNF1A, HNF4A, KCNJ11, MT-ND1, MT-ND5, MT-ND6, NAGA.
No new missing review appears in the comparison. Only CYFIP2 and CYB5R3 earn
completion credit here; the other available reviews remain at their existing
checkbox states until separately accepted completion evidence is available.

### Pending reviews remain uncredited

At the saved 2026-10-17 05:42:59 UTC queue observation, CYLD, CYP11B2, CYP27A1,
CYP1B1, CYP2U1, CYP4V2, CYP7B1, D2HGDH, DAG1 and DARS2 were approved and open in
the merge queue. The newer selected observation at 2026-10-17T05:56:13.253237+00:00 confirms
[DCAF17 #5073](https://github.com/ai4curation/ai-gene-review/pull/5073) remains
approved and queued at `87bf8aa55fa996cd5b729b279b0e7870efec7228`.
[DBT #5074](https://github.com/ai4curation/ai-gene-review/pull/5074) has the revised
head `2a70bf366aca76c6eba7686b4d987df75ab7cfc4` and awaits fresh review; the
previous changes-requested decision remains visible. No pending PR receives
completion credit. These timestamped observations are not an exhaustive new
queue census or a guarantee of later queue positions.

All 2,876 catalogue identities and association texts, 235 historical queue
objects, 78 previous completion updates, the full preceding progress text and
167 prior project history records are preserved. This appends one completion
update containing two distinct genes. Products and follow-up commits are not
additional campaign genes.

ROOT incorporated main `b17aa10c2915a7ed409475664718fbfff9e03dfe`, including the newly merged CYLD review, before rendering. The final render passed all eight frontmatter checks: 1,715 missing-review warnings remain for the main page and zero for the progress page. Seventeen warnings cleared since checkpoint 428, including CYLD beyond the sixteen predicted above; no warnings were added. The actual branch inventory contains 7,857 reviews, including 2,998 human reviews. CYLD remains uncredited here pending its separate completion audit. The completion counts are 430 checked and 2,446 unchecked catalogue genes.

[Curation session](https://github.com/ai4curation/ai-gene-review/blob/cmungall/clingen-tracker-426-20261016/history/projects/CLINGEN_MENDELIAN/2026-10-17T060834Z-codex-e7f969.yaml)

## Completion checkpoint 431 — 2026-10-17 06:04:48 UTC

**431 complete; 2,445 remaining out of 2,876 primary catalogue genes.**
CYLD is the only addition to checkpoint 430. Its approved head
`5186f4184ce6e35e4e86343ef3829c0cadc641e3` in
[#5045](https://github.com/ai4curation/ai-gene-review/pull/5045) merged as
[`b17aa10c2915`](https://github.com/ai4curation/ai-gene-review/commit/b17aa10c2915a7ed409475664718fbfff9e03dfe).
All 28 approved file modes, types and blobs match the merge, all 28 paths form
the actual parent-to-merge delta, and all 56 protected scientific source paths
remain exact. The [approval](https://github.com/ai4curation/ai-gene-review/pull/5045#pullrequestreview-5544095962)
applies to that exact head; all required review findings were resolved.

The separate actual-main push [run 39008579742](https://github.com/ai4curation/ai-gene-review/actions/runs/39008579742)
and [test job 117326023627](https://github.com/ai4curation/ai-gene-review/actions/runs/39008579742/job/117326023627)
completed successfully at 2026-10-17T06:11:58Z. The scoped gene validation passed
with nine documented generic-binding advisories; 12,007 history records had no
issues, and all 42 history tests passed. This records scoped validation, not a
claim that the full repository test suite ran. ROOT is the coordinating AI
agent; its provenance acceptance is not a human maintainer sign-off.

This update preserves all 2,876 catalogue identities and association texts,
235 historical queue objects, 79 earlier completion updates, the complete
preceding progress text and 168 earlier project history records. The catalogue
changes only CYLD from unchecked to checked. The branch already contained the
CYLD review for checkpoint 430 rendering; its availability now gains completion
credit because the separate completion audit has passed.

DBT [#5074](https://github.com/ai4curation/ai-gene-review/pull/5074) is approved
at `2a70bf366aca76c6eba7686b4d987df75ab7cfc4` and was confirmed in the normal
merge queue in the saved selected observation. DCC [#5080](https://github.com/ai4curation/ai-gene-review/pull/5080)
has passed checks at `63405caa5b9be2ccde240f170ea4149f40697717` and is undergoing
review follow-up. DCDC2 source review and DCLRE1C preparation are ongoing.
These selected status observations add no completion credit and are not a new
exhaustive queue census.

The actual branch inventory remains 7,857 reviews, including 2,998 human reviews. All eight frontmatter checks and both ordinary renders passed. The warning lists are unchanged from checkpoint 430: 1,715 missing-review warnings on the catalogue and zero on the progress page. Counts are 431 checked and 2,445 unchecked catalogue genes.

[Curation session](https://github.com/ai4curation/ai-gene-review/blob/cmungall/clingen-tracker-426-20261016/history/projects/CLINGEN_MENDELIAN/2026-10-17T062231Z-codex-665f41.yaml)

## Completion checkpoint 432 — 2026-10-17 06:35:24 UTC

**432 complete; 2,444 remaining out of 2,876 primary catalogue genes.**
CYP11B2 is the only addition to checkpoint 431. Its approved head
`4b3aa8b4dafb59bafbc0c7c5d828ff0cb56d5037` in
[#5046](https://github.com/ai4curation/ai-gene-review/pull/5046) merged as
[`a87ae568676c`](https://github.com/ai4curation/ai-gene-review/commit/a87ae568676c4012ea4abe5393967aeff1b52ae7).
All nine approved file modes, types and blobs match the merge, all nine paths
form the actual parent-to-merge delta, and all 23 protected scientific source
paths remain exact. The [approval](https://github.com/ai4curation/ai-gene-review/pull/5046#pullrequestreview-5544347766)
applies to that exact head; all required review findings were resolved.

The separate actual-main push [run 39010474868](https://github.com/ai4curation/ai-gene-review/actions/runs/39010474868)
and [test job 117331762104](https://github.com/ai4curation/ai-gene-review/actions/runs/39010474868/job/117331762104)
completed successfully at 2026-10-17T06:43:28Z. Scoped gene validation passed
with two documented source-specific action advisories, including the distinction
between positive and negated cortisol claims. All 12,009 history records had
no issues, and all 42 history tests passed. The full test suite was skipped on
this push job; the completion check does not claim a full-suite run.
The coordinating AI agent's acceptance is not a human maintainer sign-off.

This update preserves all 2,876 catalogue identities and association texts,
235 historical queue objects, 80 earlier completion updates, the complete
preceding progress text and 169 earlier project history records. The catalogue
changes only CYP11B2 from unchecked to checked. JSON escaping is explicitly
kept at the preceding checkpoint's literal UTF-8 setting; earlier queue values
are unchanged. This update's queue prose uses ordinary spacing. The completion
cutoff is also stated directly on the main project page.

DCC [#5080](https://github.com/ai4curation/ai-gene-review/pull/5080) is approved
at `08e1797356e01101c5de7091b61dd1b61c97e92b` and entered the normal merge
queue. DCDC2 [#5082](https://github.com/ai4curation/ai-gene-review/pull/5082)
has passed validation and is undergoing review follow-up. DCLRE1C source
review continues. The existing DCX review requires a bounded interaction
follow-up before completion credit under the project's current instruction.
These selected status observations add no completion credit and are not a new
exhaustive queue census.

The actual branch inventory remains 7,857 reviews, including 2,998 human reviews. All eight frontmatter checks and both ordinary renders passed. The warning lists are unchanged from checkpoint 431: 1,715 missing-review warnings on the catalogue and zero on the progress page. Counts are 432 checked and 2,444 unchecked catalogue genes.

[Curation session](https://github.com/ai4curation/ai-gene-review/blob/cmungall/clingen-tracker-426-20261016/history/projects/CLINGEN_MENDELIAN/2026-10-17T064927Z-codex-6f8b44.yaml)

## Completion checkpoint 433 — 2026-10-17 07:07:09 UTC

**433 complete; 2,443 remaining out of 2,876 primary catalogue genes.**
CYP27A1 is the only addition to checkpoint 432. Its approved head
`930aefe5b3b095210095b09bb33f425a815a3cb6` in
[#5047](https://github.com/ai4curation/ai-gene-review/pull/5047) merged as
[`1f2d0f4c42bd`](https://github.com/ai4curation/ai-gene-review/commit/1f2d0f4c42bde7e51deeed7d0486ef015657404b).
All eleven approved file modes, types and blobs match the merge, all eleven paths
form the actual parent-to-merge delta, and all 38 protected scientific source
paths remain exact. The [approval](https://github.com/ai4curation/ai-gene-review/pull/5047#pullrequestreview-5545111481)
applies to that exact head; all required review findings were resolved.

The separate actual-main push [run 39012439782](https://github.com/ai4curation/ai-gene-review/actions/runs/39012439782)
and [test job 117337633319](https://github.com/ai4curation/ai-gene-review/actions/runs/39012439782/job/117337633319)
completed successfully at 2026-10-17T07:13:32Z. Scoped gene validation passed
without gene-validation warnings. All 12,011 history records had
no issues, and all 42 history tests passed. The full test suite was skipped on
this push job; the completion check does not claim a full-suite run.
The coordinating AI agent's acceptance is not a human maintainer sign-off.

This update preserves all 2,876 catalogue identities and association texts,
235 historical queue objects, 81 earlier completion updates, the complete
preceding progress text and 170 earlier project history records. The catalogue
changes only CYP27A1 from unchecked to checked. Earlier queue values and literal UTF-8 formatting are unchanged. The completion
cutoff is also stated directly on the main project page.

DCC [#5080](https://github.com/ai4curation/ai-gene-review/pull/5080) is approved
at `08e1797356e01101c5de7091b61dd1b61c97e92b` and entered the normal merge
queue. DCDC2 [#5082](https://github.com/ai4curation/ai-gene-review/pull/5082)
is approved at `6d095b754e8d53597421072c84270e86e1329603` and queued.
DCLRE1C [#5083](https://github.com/ai4curation/ai-gene-review/pull/5083) and
DDB2 [#5084](https://github.com/ai4curation/ai-gene-review/pull/5084) await review.
The DCX follow-up is undergoing validation; DDC and DDHD1 source assessment continues.
These selected status observations add no completion credit and are not a new
exhaustive queue census.

The actual branch inventory remains 7,857 reviews, including 2,998 human reviews. All eight frontmatter checks and both ordinary renders passed. The warning lists are unchanged from checkpoint 432: 1,715 missing-review warnings on the catalogue and zero on the progress page. Counts are 433 checked and 2,443 unchecked catalogue genes.

[Curation session](https://github.com/ai4curation/ai-gene-review/blob/cmungall/clingen-tracker-426-20261016/history/projects/CLINGEN_MENDELIAN/2026-10-17T071959Z-codex-6bbe43.yaml)

## Completion checkpoint 434 — 2026-10-17 07:38:48 UTC

**434 complete; 2,442 remaining out of 2,876 primary catalogue genes.**
CYP2U1 is the only addition to checkpoint 433. Its approved head
`9e15617075a94611247854991769f782ba9a03d8` in
[#5049](https://github.com/ai4curation/ai-gene-review/pull/5049) merged as
[`e32937e9a43d`](https://github.com/ai4curation/ai-gene-review/commit/e32937e9a43d197137f795d76417027d318843f0).
All 21 approved file modes, types and blobs match the merge, all 21 paths
form the actual parent-to-merge delta, and all 17 protected scientific source
paths remain exact. The [approval](https://github.com/ai4curation/ai-gene-review/pull/5049#pullrequestreview-5545846816)
applies to that exact head.

The separate actual-main push [run 39014407121](https://github.com/ai4curation/ai-gene-review/actions/runs/39014407121)
and [test job 117343409663](https://github.com/ai4curation/ai-gene-review/actions/runs/39014407121/job/117343409663)
completed successfully at 2026-10-17T07:45:38Z. Scoped gene validation passed
with one inherited mixed-action monooxygenase advisory. All 12,013 history
records were valid, all 42 history tests passed, and all 695 family files
validated. The full test suite was skipped on the main push; the separate
successful [merge-group run 39012443172](https://github.com/ai4curation/ai-gene-review/actions/runs/39012443172)
provides the full-suite evidence for the merge candidate. These are distinct
validation events. The coordinating AI agent's acceptance is not a human
maintainer sign-off.

This update preserves all 2,876 catalogue identities and association texts,
235 historical queue objects, 82 earlier completion updates, the complete
preceding progress text and 172 earlier project history records. The catalogue
changes only CYP2U1 from unchecked to checked. Earlier queue values and literal
UTF-8 formatting are unchanged. The completion cutoff is also stated directly
on the main project page.

DDC [#5086](https://github.com/ai4curation/ai-gene-review/pull/5086) and
DDHD1 [#5087](https://github.com/ai4curation/ai-gene-review/pull/5087) have been
published for review. DDB2 [#5084](https://github.com/ai4curation/ai-gene-review/pull/5084)
has a provenance follow-up at `ee8a2dd11241467cb1fe1c6666a0456275cd2689`.
DCLRE1C [#5083](https://github.com/ai4curation/ai-gene-review/pull/5083) is approved
at `5a2760761b431c0ba318236e86611fe3322c5be1` and entered the normal merge queue.
DCX documentation follow-up and DDR2/DDX11 source assessment continue. These
selected status observations add no completion credit and are not a new
exhaustive queue census.

The actual branch inventory remains 7,858 reviews, including 2,999 human reviews. All eight frontmatter checks and both ordinary renders passed. The catalogue has 1,714 missing-review warnings, one fewer than checkpoint 433 because CYP2U1 now has a review. The progress page has no warnings. Counts are 434 checked and 2,442 unchecked catalogue genes.

[Curation session](https://github.com/ai4curation/ai-gene-review/blob/cmungall/clingen-tracker-426-20261016/history/projects/CLINGEN_MENDELIAN/2026-10-17T080750Z-codex-f286a0.yaml)

## Completion checkpoint 435 — 2026-10-17 08:10:20 UTC

**435 complete; 2,441 remaining out of 2,876 primary catalogue genes.**
CYP4V2 is the only addition to checkpoint 434. Its approved head
`ab461cf6a1357c01b7e15f10219929d63f354a7b` in
[#5050](https://github.com/ai4curation/ai-gene-review/pull/5050) merged as
[`40c8c08b26b8`](https://github.com/ai4curation/ai-gene-review/commit/40c8c08b26b8ba217b428bcbbaf11935991afb5d).
All 14 approved file modes, types and blobs match the merge, all 14 paths
form the actual parent-to-merge delta, and all 15 protected source and prior
provenance paths remain exact. The [approval](https://github.com/ai4curation/ai-gene-review/pull/5050#pullrequestreview-5546006171)
applies to that exact head.

The separate actual-main push [run 39016360461](https://github.com/ai4curation/ai-gene-review/actions/runs/39016360461)
and [test job 117349178779](https://github.com/ai4curation/ai-gene-review/actions/runs/39016360461/job/117349178779)
completed successfully at 2026-10-17T08:17:21Z. Scoped CYP4V2 validation passed
with two generic-binding advisories retained under the explicit project policy.
All 12,015 history records were valid, all 42 history tests passed, and all
695 family files validated. The full test suite was skipped on the main push;
the separate successful [merge-group run 39014408739](https://github.com/ai4curation/ai-gene-review/actions/runs/39014408739)
provides the full-suite evidence for the exact merge candidate. These are distinct
validation events. The coordinating AI agent's acceptance is not a human
maintainer sign-off.

This update preserves all 2,876 catalogue identities and association texts,
235 historical queue objects, 83 earlier completion updates, the complete
preceding progress text and 173 earlier project history records. The catalogue
changes only CYP4V2 from unchecked to checked. Earlier queue values and literal
UTF-8 formatting are unchanged. The completion cutoff is also stated directly
on the main project page. The rendered review links and availability counts are
qualified against incorporated main [`a3bfd308b643`](https://github.com/ai4curation/ai-gene-review/commit/a3bfd308b6432eac0114cae92f702bb5e2edf39e),
which also includes the newly available CYP1B1 review. CYP1B1 remains unchecked
pending completion verification; its availability adds no completion credit.

The actual branch inventory remains 7,860 reviews, including 3,001 human reviews. All eight frontmatter checks and both ordinary renders passed. The catalogue has 1,712 missing-review warnings, two fewer than checkpoint 434 because CYP4V2 and CYP1B1 now have reviews; CYP1B1 remains unchecked. The progress page has no warnings. Counts are 435 checked and 2,441 unchecked catalogue genes.

[Curation session](https://github.com/ai4curation/ai-gene-review/blob/cmungall/clingen-tracker-426-20261016/history/projects/CLINGEN_MENDELIAN/2026-10-17T084245Z-codex-8e6cce.yaml)

## Completion checkpoint 436 — 2026-10-17 08:31:18 UTC

**436 complete; 2,440 remaining out of 2,876 primary catalogue genes.**
CYP1B1 is the only addition to checkpoint 435. Its approved head
`e46195e4fbeb664c4ef8cd6438662b34968a2142` in
[#5048](https://github.com/ai4curation/ai-gene-review/pull/5048) merged as
[`a3bfd308b643`](https://github.com/ai4curation/ai-gene-review/commit/a3bfd308b6432eac0114cae92f702bb5e2edf39e).
All 49 approved file modes, types and blobs match the merge. The actual
parent-to-merge delta contains 46 paths; three shared Reactome files were already
identical on parent main. All 49 protected source and provenance positions remain
exact. These 49 protected paths comprise 42 machine sources, four prior history
records and three accepted authored review artifacts; this protection set is
distinct from the PR delta. The [approval](https://github.com/ai4curation/ai-gene-review/pull/5048#pullrequestreview-5547093134)
applies to that exact head.

The separate actual-main push [run 39017675880](https://github.com/ai4curation/ai-gene-review/actions/runs/39017675880)
and [test job 117353019495](https://github.com/ai4curation/ai-gene-review/actions/runs/39017675880/job/117353019495)
completed successfully at 2026-10-17T08:38:15Z. Scoped CYP1B1 validation passed
without annotation advisories. All 12,020 history records were valid, all 42
history tests passed, and all 695 family files validated. The full test suite
was skipped on the main push. The separate successful
[merge-group run 39016362284](https://github.com/ai4curation/ai-gene-review/actions/runs/39016362284)
and [job 117349183993](https://github.com/ai4curation/ai-gene-review/actions/runs/39016362284/job/117349183993)
provide full-suite evidence for the exact merge candidate: 3,912 tests passed
with one skipped and 83 deselected, 252 passed with 37 skipped in the separate
suite, and 415 automation checks passed. These remain distinct validation events.
The coordinating AI agent's acceptance is not a human maintainer sign-off.

This update preserves all 2,876 catalogue identities and association texts,
235 historical queue objects, 84 earlier completion updates, the complete
preceding progress text and 174 earlier project history records. The catalogue
changes only CYP1B1 from unchecked to checked. Update 85 is appended; earlier
queue values and literal UTF-8 formatting are unchanged. Review availability at incorporated main
`66f848da36501873b7f42e8edff5226bdff2702a` is 7,860 review files, including 3,001 human
reviews. CYP7B1 was updated on main and remains unchecked pending completion
verification. CYP1B1 now
receives completion credit because its approval, merge and actual-main checks
have been verified; availability alone did not establish that credit.

The actual branch inventory contains 7,860 reviews, including 3,001 human reviews. All eight frontmatter checks and both ordinary renders passed. The catalogue has 1,712 missing-review warnings, unchanged from checkpoint 435; CYP7B1 remains unchecked. The progress page has no warnings. Counts are 436 checked and 2,440 unchecked catalogue genes.

[Curation session](https://github.com/ai4curation/ai-gene-review/blob/cmungall/clingen-tracker-426-20261016/history/projects/CLINGEN_MENDELIAN/2026-10-17T090405Z-codex-4ae10d.yaml)

## Completion checkpoint 437 — 2026-10-17 08:58:31 UTC

**437 complete; 2,439 remaining out of 2,876 primary catalogue genes.**
CYP7B1 is the only addition to checkpoint 436. Its approved head
`75c32d63eb7a3594a4bed871c21b0b5e45324c01` in
[#5051](https://github.com/ai4curation/ai-gene-review/pull/5051) merged as
[`66f848da3650`](https://github.com/ai4curation/ai-gene-review/commit/66f848da36501873b7f42e8edff5226bdff2702a).
All 19 approved file modes, types and blobs match the merge. The actual
parent-to-merge delta contains 18 paths; publication PMID 24275569 was already
identical on parent main. The separate protection set contains 62 positions:
32 machine source files, 29 other context files and one prior PR history record.
All remain exact. These counts describe distinct sets. The historical GOA
snapshot is preserved byte for byte, and both approved curation histories match
the merge. The [approval](https://github.com/ai4curation/ai-gene-review/pull/5051#pullrequestreview-5547301213)
and [final discussion](https://github.com/ai4curation/ai-gene-review/pull/5051#issuecomment-6214673452)
cover that exact head.

The separate actual-main push [run 39019360739](https://github.com/ai4curation/ai-gene-review/actions/runs/39019360739)
and [test job 117357894268](https://github.com/ai4curation/ai-gene-review/actions/runs/39019360739/job/117357894268)
completed successfully at 2026-10-17T09:05:03Z. Scoped CYP7B1 validation passed
with the same two supported generic-binding KEEP_AS_NON_CORE advisories as the
approved-head and merge-group checks. All 12,022 history records were valid,
all 42 history tests passed, and all 695 family files validated. The full test
suite was skipped on the main push. The separate successful
[merge-group run 39017677239](https://github.com/ai4curation/ai-gene-review/actions/runs/39017677239)
and [job 117353023833](https://github.com/ai4curation/ai-gene-review/actions/runs/39017677239/job/117353023833)
provide full-suite evidence for the exact same merge SHA: 3,912 tests passed
with one skipped and 83 deselected, 252 doctests passed with 37 skipped,
415 automation tests and 19 JavaScript tests passed. The all-gene schema,
12 valid/invalid examples, mypy and lint checks also passed. The standalone
changed-source-evidence step was skipped; it is not reported as passed.
These remain distinct validation events. DRAFT and two UNDECIDED annotations
are retained; project completion means the review was finished, approved and
merged, not that every scientific uncertainty was resolved. The coordinating
AI agent's acceptance is not a human maintainer sign-off.

This update preserves all 2,876 catalogue identities and association texts,
235 historical queue objects, 85 earlier completion updates, the complete
preceding progress text and 175 earlier project history records. The catalogue
changes only CYP7B1 from unchecked to checked. Update 86 is appended; earlier
queue values and literal UTF-8 formatting are unchanged. Review availability is
7,861 review files, including 3,002 human reviews, against incorporated main
9db646fd420946e2c8a9f325be9cd5b62b2c3d4c. D2HGDH is newly available but remains
unchecked pending verification; it receives no credit in this checkpoint. CYP7B1
already had a review; this accepted augmentation supplies completion credit
without adding an inventory item. Other available and pending reviews receive
no credit from this update.

The actual branch inventory contains 7,861 reviews, including 3,002 human reviews. All eight frontmatter checks and both ordinary renders passed. The catalogue has 1,711 missing-review warnings, one fewer than checkpoint 436 because D2HGDH is newly available but remains unchecked; CYP7B1 is now checked. The progress page has no warnings. Counts are 437 checked and 2,439 unchecked catalogue genes.

[Curation session](https://github.com/ai4curation/ai-gene-review/blob/cmungall/clingen-tracker-426-20261016/history/projects/CLINGEN_MENDELIAN/2026-10-17T093348Z-codex-4a0537.yaml)

## Completion checkpoint 438 — 2026-10-17 09:29:48 UTC

**438 complete; 2,438 remaining out of 2,876 primary catalogue genes.**
D2HGDH is the only addition to checkpoint 437. Its approved head
`50483db1f01e0e791d3a08ef907b39d287813714` in
[#5052](https://github.com/ai4curation/ai-gene-review/pull/5052) merged as
[`9db646fd4209`](https://github.com/ai4curation/ai-gene-review/commit/9db646fd420946e2c8a9f325be9cd5b62b2c3d4c).
All 17 approved file modes, types and blobs match the merge, and all 17 paths
are actual parent-to-merge changes. The separate protection set contains 41
positions: 13 machine source files, 27 other context files and one prior PR
history record. All remain exact. These counts describe distinct sets. The
historical GOA snapshot is preserved byte for byte, and both approved curation
histories match the merge. The [approval](https://github.com/ai4curation/ai-gene-review/pull/5052#pullrequestreview-5547556150)
and [final discussion](https://github.com/ai4curation/ai-gene-review/pull/5052#issuecomment-6215129827)
cover that exact head.

The separate actual-main push [run 39021341700](https://github.com/ai4curation/ai-gene-review/actions/runs/39021341700)
and [test job 117363611688](https://github.com/ai4curation/ai-gene-review/actions/runs/39021341700/job/117363611688)
completed successfully at 2026-10-17T09:36:40Z. Scoped D2HGDH validation passed
with zero gene advisories. All 12,024 history records were valid, all 42 history
tests passed, and all 695 family files validated. The full test suite was skipped
on the main push. The separate successful
[merge-group run 39019362379](https://github.com/ai4curation/ai-gene-review/actions/runs/39019362379)
and [job 117357899592](https://github.com/ai4curation/ai-gene-review/actions/runs/39019362379/job/117357899592)
provide full-suite evidence for the exact same merge SHA: 3,912 tests passed
with one skipped and 83 deselected, 252 doctests passed with 37 skipped,
415 automation tests and 19 JavaScript tests passed. The all-gene schema,
12 valid/invalid examples, mypy and lint checks also passed. The standalone
changed-source-evidence step was skipped; it is not reported as passed.
These remain distinct validation events. The review retains COMPLETE status
and two UNDECIDED negated source assertions; project completion means the review
was finished, approved and merged, not that every scientific uncertainty was
resolved. The coordinating AI agent's acceptance is not a human maintainer sign-off.

This update preserves all 2,876 catalogue identities and association texts,
235 historical queue objects, 86 earlier completion updates, the complete
preceding progress text and 176 earlier project history records. The catalogue
changes only D2HGDH from unchecked to checked. Update 87 is appended; earlier
queue values and literal UTF-8 formatting are unchanged. Review availability is
unchanged from checkpoint 437: 7,861 review files, including 3,002 human reviews,
against incorporated main 9db646fd420946e2c8a9f325be9cd5b62b2c3d4c. D2HGDH
added one review at that merge; checkpoint 437 already recorded its availability
without credit. This update supplies the verified completion credit without
counting that inventory addition again. Other available and pending reviews
receive no credit from this update.

All eight frontmatter checks and both ordinary renders passed against the actual branch inventory of 7,861 reviews, including 3,002 human reviews. The catalogue has 1,711 missing-review warnings and the progress page has no warnings, unchanged from checkpoint 437. Counts are 438 checked and 2,438 unchecked catalogue genes.

[Curation session](https://github.com/ai4curation/ai-gene-review/blob/cmungall/clingen-tracker-426-20261016/history/projects/CLINGEN_MENDELIAN/2026-10-17T095628Z-codex-07f7ee.yaml)

## Completion checkpoint 439 — 2026-10-17 10:01:42 UTC

**439 complete; 2,437 remaining out of 2,876 primary catalogue genes.**
DAG1 is the only addition to checkpoint 438. Its approved head
`3d949f3bd8f428c3e1d1710284b292e661a4954e` in
[#5054](https://github.com/ai4curation/ai-gene-review/pull/5054) merged as
[`f6be2985c3b5`](https://github.com/ai4curation/ai-gene-review/commit/f6be2985c3b532458ebf9383357cc1e519d97c7e).
All 64 approved file modes, types and blobs match the merge, and all 64 paths
are actual parent-to-merge changes. The separate protection set contains 122
positions: 93 machine source files, 27 other context files and two prior PR
history records. All remain exact. These counts describe distinct sets. The
historical GOA snapshot is preserved byte for byte, and all three approved curation
histories match the merge. The [approval](https://github.com/ai4curation/ai-gene-review/pull/5054#pullrequestreview-5549342181)
and [final discussion](https://github.com/ai4curation/ai-gene-review/pull/5054#issuecomment-6217821485)
cover that exact head.

The separate actual-main push [run 39023334577](https://github.com/ai4curation/ai-gene-review/actions/runs/39023334577)
and [test job 117369341944](https://github.com/ai4curation/ai-gene-review/actions/runs/39023334577/job/117369341944)
completed successfully at 2026-10-17T10:06:51Z. Scoped DAG1 validation passed
with five disclosed and accepted gene advisories: a stale GO-label warning,
three supported generic-binding policy warnings and one synthesized-core
coverage warning. All 12,027 history records were valid, all 42 history
tests passed, and all 695 family files validated. The full test suite was skipped
on the main push. The separate successful
[merge-group run 39021343335](https://github.com/ai4curation/ai-gene-review/actions/runs/39021343335)
and [job 117363615962](https://github.com/ai4curation/ai-gene-review/actions/runs/39021343335/job/117363615962)
provide full-suite evidence for the exact same merge SHA: 3,912 tests passed
with one skipped and 83 deselected, 252 doctests passed with 37 skipped,
415 automation tests and 19 JavaScript tests passed. The all-gene schema,
12 valid/invalid examples, mypy and lint checks also passed. The standalone
changed-source-evidence step was skipped; it is not reported as passed.
These remain distinct validation events. The review retains DRAFT status
and ten UNDECIDED source assertions; project completion means the review
was finished, approved and merged, not that every scientific uncertainty was
resolved. The coordinating AI agent's acceptance is not a human maintainer sign-off.

This update preserves all 2,876 catalogue identities and association texts,
235 historical queue objects, 87 earlier completion updates, the complete
preceding progress text and 177 earlier project history records. The catalogue
changes only DAG1 from unchecked to checked. Update 88 is appended; earlier
queue values and literal UTF-8 formatting are unchanged. Review availability rises from checkpoint 438's 7,861 total / 3,002 human
reviews to 7,862 / 3,003 at main f6be2985c3b532458ebf9383357cc1e519d97c7e.
DAG1 adds one available review and receives the sole new verified credit.
Other available and pending reviews
receive no credit from this update.

All eight frontmatter checks and both ordinary renders passed against the actual branch inventory of 7,862 reviews, including 3,003 human reviews. The catalogue has 1,710 missing-review warnings and the progress page has no warnings, one fewer than checkpoint 438. Counts are 439 checked and 2,437 unchecked catalogue genes.

[Curation session](https://github.com/ai4curation/ai-gene-review/blob/cmungall/clingen-tracker-426-20261016/history/projects/CLINGEN_MENDELIAN/2026-10-17T102135Z-codex-3dcc7e.yaml)

## Completion checkpoint 440 — 2026-10-17 10:32:17 UTC

**440 complete; 2,436 remaining out of 2,876 primary catalogue genes.**
DARS2 is the sole addition to checkpoint 439. Its approved head
`722a2bd80bba55a3b3b34067d0a7d8ec6b0196bb` in
[#5060](https://github.com/ai4curation/ai-gene-review/pull/5060) merged as
[`6328c89e41e0`](https://github.com/ai4curation/ai-gene-review/commit/6328c89e41e0cc646e4a1437079844d87ad7e3b7).
All 11 approved PR file modes and blobs match the merge. The actual parent delta
contains 10 paths because PMID_24275569.md was already present with identical bytes.
The separate set of 59 protected positions comprises 28 machine-source/provider
files, 28 other context files and three earlier PR histories. All remain exact.
The 54 source annotation dictionaries, 35 inherited quotations, 3,446-byte notes
prefix and previously merged target history are preserved. The exact-head
[approval](https://github.com/ai4curation/ai-gene-review/pull/5060#pullrequestreview-5549390951)
and [final discussion](https://github.com/ai4curation/ai-gene-review/pull/5060#issuecomment-6217890878)
resolve the blockers and record the remaining nonblocking collagen-refinement judgment.

The actual-main push [run 39025275210](https://github.com/ai4curation/ai-gene-review/actions/runs/39025275210)
and [job 117374923665](https://github.com/ai4curation/ai-gene-review/actions/runs/39025275210/job/117374923665)
passed at 2026-10-17T10:39:12Z. Scoped DARS2 validation passed with 11 accepted
advisories; all 12,030 histories validated, 42 history tests passed and 695 family
files validated. The full suite was skipped on this push. The separate successful
[merge-group run 39023336329](https://github.com/ai4curation/ai-gene-review/actions/runs/39023336329)
and [job 117369347335](https://github.com/ai4curation/ai-gene-review/actions/runs/39023336329/job/117369347335)
tested the exact same merge SHA: 3,912 tests passed, one skipped, 83 deselected;
252 doctests passed, 37 skipped; 415 automation tests and 19 JavaScript tests passed.
All-gene schemas, 12 valid/invalid examples, mypy and lint also passed. The standalone
prediction/source-evidence step was skipped and is not claimed as executed.

DARS2 retains DRAFT status and three UNDECIDED source assertions. Completion means
the review was finished, approved and merged; it does not resolve all scientific
uncertainty or imply a human maintainer sign-off by the coordinating AI agent.
DARS2 was already available as a review: repository availability remains 7,862
reviews, including 3,003 human reviews. Of 1,166 catalogue genes with available
reviews, 440 are credited and 726 remain uncredited; 1,710 still lack review files.

This update preserves all 2,876 catalogue identities and association texts, 235
historical queue objects, all 88 earlier completion updates, the complete preceding
progress text and 178 prior project histories. Only the DARS2 checkbox changes;
completion update 89 is appended. Other available and pending reviews receive no
credit from this update.

All eight frontmatter checks and both ordinary renders passed against the actual branch inventory of 7,862 reviews, including 3,003 human reviews. The catalogue has 1,710 missing-review warnings and the progress page has no warnings, unchanged from checkpoint 439. Counts are 440 checked and 2,436 unchecked catalogue genes.

[Curation session](https://github.com/ai4curation/ai-gene-review/blob/cmungall/clingen-tracker-426-20261016/history/projects/CLINGEN_MENDELIAN/2026-10-17T104628Z-codex-760612.yaml)

## Completion checkpoint 441 — 2026-10-17 10:58:01 UTC

**441 complete; 2,435 remaining out of 2,876 primary catalogue genes.**
DCAF17 is the sole addition to checkpoint 440. Its approved head
`87bf8aa55fa996cd5b729b279b0e7870efec7228` in
[#5073](https://github.com/ai4curation/ai-gene-review/pull/5073) merged as
[`1b47f6653c7f`](https://github.com/ai4curation/ai-gene-review/commit/1b47f6653c7fa96e61b6a6ac5fe76b989961b59c).
All 13 approved PR file modes and blobs match the merge. The actual parent delta
contains 12 paths; `publications/PMID_15815621.md` was already identical on the parent.
The exact-head [approval](https://github.com/ai4curation/ai-gene-review/pull/5073#pullrequestreview-5550019338)
and separate actual-main validation establish this completion.

The actual-main push [run 39026890723](https://github.com/ai4curation/ai-gene-review/actions/runs/39026890723)
and [job 117379542492](https://github.com/ai4curation/ai-gene-review/actions/runs/39026890723/job/117379542492)
succeeded at 2026-10-17T11:03:25Z. Scoped gene, history and family validation
passed; the full test suite was skipped on this push. The separate successful
[merge-group run 39025277296](https://github.com/ai4curation/ai-gene-review/actions/runs/39025277296)
and [job 117374929386](https://github.com/ai4curation/ai-gene-review/actions/runs/39025277296/job/117374929386)
tested the same merge SHA and ran the full test suite, examples, all-gene schemas
and automation checks. The standalone prediction/source-evidence step was skipped
and is not claimed as executed. Completion records the finished, approved and
merged review; it is not a human maintainer sign-off by the coordinating AI agent.

The 46 inspected positions overlap the 13 approved PR paths: seven were added
among the 12 merge changes, one approved cache was already identical on the parent,
and 38 pre-existing context paths were unchanged. These are the selected
post-publication preservation inventory, not 46 files that all predated the merge.
Their explicit categories and paths are:

- tracker source records (2): `projects/CLINGEN_MENDELIAN.md`, `projects/CLINGEN_MENDELIAN/publication-queue.json`.
- pathway and model sources (6): `gocams/index.tsv`, `reactome/R-HSA-8952638.md`, `reactome/R-HSA-8952639.md`, `reactome/R-HSA-8955245.md`, `reactome/R-HSA-8955285.md`, `reactome/R-HSA-8956045.md`.
- repository runtime and build context (25): `CLAUDE.md`, `AGENTS.md`, `docs/history.md`, `genes/human/RBFOX3/RBFOX3-bioinformatics/rbfox3_analysis/pyproject.toml`, `genes/human/RBFOX3/RBFOX3-bioinformatics/rbfox3_analysis/README.md`, `genes/yeast/MTC7/MTC7-bioinformatics/pyproject.toml`, `genes/yeast/MTC7/MTC7-bioinformatics/README.md`, `genes/human/CFAP418/CFAP418-bioinformatics/pyproject.toml`, `genes/human/CFAP418/CFAP418-bioinformatics/README.md`, `genes/PSEPK/pedH/pedH-bioinformatics/pyproject.toml`, `genes/PSEPK/pedH/pedH-bioinformatics/README.md`, `genes/human/C18orf21/C18orf21-bioinformatics/pyproject.toml`, `genes/human/C18orf21/C18orf21-bioinformatics/README.md`, `genes/human/C18orf21/C18orf21-bioinformatics/genes/human/C18orf21/C18orf21-bioinformatics/pyproject.toml`, `genes/human/C18orf21/C18orf21-bioinformatics/genes/human/C18orf21/C18orf21-bioinformatics/README.md`, `genes/PENCH/aatA/aatA-bioinformatics/pyproject.toml`, `genes/PENCH/aatA/aatA-bioinformatics/README.md`, `genes/METBS/Pks1/Pks1-bioinformatics/pyproject.toml`, `genes/METBS/Pks1/Pks1-bioinformatics/README.md`, `genes/human/GATA3/GATA3-bioinformatics/pyproject.toml`, `genes/human/GATA3/GATA3-bioinformatics/README.md`, `genes/RAMVA/RvY_13070/RvY_13070-bioinformatics/pyproject.toml`, `projects/THLAR_OILSEED/ortholog_mapping/pyproject.toml`, `analysis/mf_metabolic_network/pyproject.toml`, `src/ai_gene_review/schema/gene_review.yaml`.
- publication caches (10): `publications/PMID_14702039.md`, `publications/PMID_15489334.md`, `publications/PMID_16949367.md`, `publications/PMID_17974005.md`, `publications/PMID_29907856.md`, `publications/PMID_15815621.md`, `publications/PMID_19026396.md`, `publications/PMID_30068992.md`, `publications/PMID_36509865.md`, `publications/PMID_40449516.md`.
- DCAF17 machine source files (2): `genes/human/DCAF17/DCAF17-goa.tsv`, `genes/human/DCAF17/DCAF17-uniprot.txt`.
- prior DCAF17 session history (1): `history/genes/human/DCAF17/2026-10-16T144134Z-codex-bd0f40.yaml`.

The runtime/build category records the exact historical DCAF17 execution inventory
listed above; it is not an exhaustive inventory of repository runtime. The merge
preserved the 38 pre-existing context paths and the already-identical cache, and
introduced the seven remaining listed paths. This checkpoint separately updates
the two tracker source records and their related project files; other positions
retain their accepted merge contents. DCAF17 had zero validation advisories.
No gene annotation is edited by this tracker update.

DCAF17 adds a review file. Repository availability is now 7,863 reviews,
including 3,004 human reviews. Of 1,167 catalogue genes with available
reviews, 441 are credited and 726 remain uncredited; 1,709 still lack
review files. Availability and completion remain different measures.

This update preserves all 2,876 catalogue identities and association texts, 235
historical queue objects, all 89 earlier completion updates, the complete preceding
progress text and 179 prior project histories. Only the DCAF17 checkbox changes;
completion update 90 is appended. Other available and pending reviews receive no
credit from this update.

All eight frontmatter checks and both ordinary renders passed against the actual branch inventory of 7,863 reviews, including 3,004 human reviews. The catalogue has 1,709 missing-review warnings and the progress page has no warnings, reflecting the new DCAF17 review. Counts are 441 checked and 2,435 unchecked catalogue genes.

[Curation session](https://github.com/ai4curation/ai-gene-review/blob/cmungall/clingen-tracker-426-20261016/history/projects/CLINGEN_MENDELIAN/2026-10-17T113125Z-codex-90e568.yaml)

## Completion checkpoint 442 — 2026-10-17 13:46:17 UTC

**442 complete; 2,434 remaining out of 2,876 primary catalogue genes.**
DNAH12 is the sole addition to checkpoint 441. Its approved head
`d9a78ab63b0da51e49b3f80341668c68e2599efd` in
[#4877](https://github.com/ai4curation/ai-gene-review/pull/4877) merged as
[`298fede2212a`](https://github.com/ai4curation/ai-gene-review/commit/298fede2212a4d540865542e5e8b396bec69107c).
The exact-head [approval](https://github.com/ai4curation/ai-gene-review/pull/4877#pullrequestreview-5517454210)
resolves the required review changes. All 27 approved path modes and types are
preserved. Twenty-six blobs are identical; `cache/go/terms.csv` contains exactly
the approved GO:0036156 insertion applied to the newer parent. Removing that
single line reproduces the parent cache byte for byte. The actual merge delta
has 25 additions and two modifications. Its 17 machine-source/provider additions
and six history additions are exact approved blobs; all other tracked paths are
unchanged by this merge. These additions are not pre-existing protected files.

The separate actual-main push [run 39037932465](https://github.com/ai4curation/ai-gene-review/actions/runs/39037932465)
and [job 117411414646](https://github.com/ai4curation/ai-gene-review/actions/runs/39037932465/job/117411414646)
completed successfully at 2026-10-17T14:07:58Z. Scoped DNAH12 validation passed
with zero gene curation advisories. All 12,200 history records validated, 42
history tests passed and 705 family files validated. The full suite actually ran
on this push: 3,912 tests passed, one skipped and 83 deselected; 252 doctests
passed and 37 skipped. All 12 valid/invalid examples, mypy and lint passed.

The distinct successful [merge-group run 39035866797](https://github.com/ai4curation/ai-gene-review/actions/runs/39035866797)
and [job 117405388809](https://github.com/ai4curation/ai-gene-review/actions/runs/39035866797/job/117405388809)
tested the same merge SHA. They independently passed the full suite and doctests
with the same counts, plus all-gene schemas, modules, 415 automation tests and
19 JavaScript tests. All-gene schemas, modules and agentic automation were skipped
on the main push. Standalone changed prediction/source-evidence steps were
skipped in both events and are not claimed as executed.

Zero DNAH12 curation advisories does not mean every check was warning-free.
The passing suites reported nine test warnings and eight doctest warnings;
family checks retained unrelated unresolved membership/residue cases and skipped
snippet checks. The approving reviewer left three nonblocking notes: attribute
the mouse expression panel precisely, move a curation-framed phylogeny sentence
out of the description, and investigate a prior DuplicateKeyError as tooling.
The review remains COMPLETE with one UNDECIDED binding assertion. Completion
records finished, approved and merged curation; it does not resolve all scientific
uncertainty or imply a human maintainer sign-off by the coordinating AI agent.

Repository availability is now 7,965 reviews, including 3,005 human reviews.
DNAH12 accounts for the one new human review since checkpoint 441; other net
review-file additions receive no completion credit here. Of 1,168 catalogue
genes with available reviews, 442 are credited and 726 remain uncredited;
1,708 catalogue genes still lack reviews. The later publication source main
`bff21ea8eb90bc3e07bb2fbedf14c25d37080161` has the same inventory; the completion
cutoff remains the DNAH12 merge at 13:46:17 UTC.

This update preserves all 2,876 catalogue identities and association texts, all
235 historical queue objects, all 90 earlier completion updates, the complete
preceding progress text and 181 prior project history records. Only the DNAH12
checkbox changes; completion update 91 is appended. No gene annotation, source
cache or earlier history record is edited by this tracker update.

All eight frontmatter checks and both ordinary renders passed against the actual branch inventory of 7,965 reviews, including 3,005 human reviews. The catalogue has 1,708 missing-review warnings and the progress page has no warnings, reflecting the new DNAH12 review. Counts are 442 checked and 2,434 unchecked catalogue genes.

[Curation session](https://github.com/ai4curation/ai-gene-review/blob/cmungall/clingen-tracker-426-20261016/history/projects/CLINGEN_MENDELIAN/2026-10-17T142405Z-codex-a230e1.yaml)

## Completion checkpoint 443 — 2026-10-18 15:14:14 UTC

**443 complete; 2,433 remaining out of 2,876 primary catalogue genes.**
DCC is the sole addition to checkpoint 442. Its approved head
`08e1797356e01101c5de7091b61dd1b61c97e92b` in
[#5080](https://github.com/ai4curation/ai-gene-review/pull/5080) merged as
[`7bbbe4f59c5b`](https://github.com/ai4curation/ai-gene-review/commit/7bbbe4f59c5b14d9b053d691deba3a8c5726d9bf).
The exact-head [approval](https://github.com/ai4curation/ai-gene-review/pull/5080#pullrequestreview-5556675186)
and [detailed review](https://github.com/ai4curation/ai-gene-review/pull/5080#issuecomment-6230751438)
close the required changes. The reviewer explicitly retracts the earlier
generic-binding objection after verifying the project's binding instruction and
accepts the revised core representation. There are no inline comments or review
threads. The older changes-requested review belongs to an earlier revision.

All 18 approved files have identical blobs and modes in the merge. Its sole
parent is `23a506fc6b8bd5a2822d76bc2151276fa7bddac4`; the complete delta contains
exactly those 18 additions, including two DCC history records and ten publication
caches. All 158,727 paths outside the delta are unchanged.
Complete saved tree listings were reconstructed and authenticated against the
Git commit tree hashes, and the 18 captured file contents were checked against
their Git blob identifiers.

The actual-main push [run 39139563867](https://github.com/ai4curation/ai-gene-review/actions/runs/39139563867)
and [test job 117710997259](https://github.com/ai4curation/ai-gene-review/actions/runs/39139563867/job/117710997259)
completed successfully at 2026-10-18T15:21:25Z. The complete raw job log is retained
in the merge audit. Its operative sections identify this main revision and its
parent, detect the exact 18-file delta, and execute strict changed-gene validation
on DCC. That validation passed with six generic-binding policy warnings, whose
scientific dispositions were accepted in the approving review. All 12,956 history
records validated, 42 history tests passed, and 708 family files validated. Family
checks reported no failures while retaining unrelated unresolved membership and
residue cases and skipped snippet checks.

This was a scoped main-push workflow: the general test suite, example validation,
agentic checks and standalone source-evidence validation were skipped. No fresh
full-suite run is claimed. All test-job steps and its three annotations were
read; the annotations concern Node.js migration, scoped validation and the future
runner image, not DCC scientific failures. The separate main-push documentation
run 39139563863 also succeeded. The distinct [merge-group run 39137566672](https://github.com/ai4curation/ai-gene-review/actions/runs/39137566672)
completed successfully at the same merge SHA; its run metadata is preserved, but
its full job log was not re-audited and is not substituted for actual-main proof.

The review file remains DRAFT, with three UNDECIDED annotations and the six
acknowledged policy warnings. The approving reviewer left only nonblocking
suggestions about provenance wording, comparator interpretation and a structured
knowledge gap. Completion records approved and merged curation, not resolution
of every biological uncertainty or a human maintainer sign-off by the
coordinating AI agent.

Repository availability at this actual-main cutoff is 7,981 reviews,
including 3,006 human reviews. Of 1,169 catalogue genes with
available reviews, 443 are credited and 726 remain uncredited;
1,707 catalogue genes still lack reviews. These counts were recomputed
from the complete main tree and the unchanged catalogue, not copied from the
preceding checkpoint. DCC alone receives new completion credit.

This update preserves all 2,876 catalogue identities and association texts,
all 235 historical queue objects, all 91 earlier completion updates, the complete
preceding progress text and 182 prior project history records. Only the DCC
checkbox changes; completion update 92 is appended. No gene review, source cache,
runtime file or earlier history record is edited by this tracker update.

All eight frontmatter checks and both ordinary renders passed against the actual branch inventory of 7,981 reviews, including 3,006 human reviews. The catalogue has 1,707 missing-review warnings and the progress page has no warnings, reflecting the new DCC review. Counts are 443 checked and 2,433 unchecked catalogue genes.

[Curation session](https://github.com/ai4curation/ai-gene-review/blob/cmungall/clingen-tracker-426-20261016/history/projects/CLINGEN_MENDELIAN/2026-10-18T153706Z-codex-1e95f8.yaml)

## Completion checkpoint 444 — 2026-10-18 15:47:45 UTC

**444 complete; 2,432 remaining out of 2,876 primary catalogue genes.**
DCDC2 is the sole addition to checkpoint 443. Its approved head
`6d095b754e8d53597421072c84270e86e1329603` in
[#5082](https://github.com/ai4curation/ai-gene-review/pull/5082) merged as
[`28ce6af8efa0`](https://github.com/ai4curation/ai-gene-review/commit/28ce6af8efa0c260e8bae7b6b0783376deef99cf).
The exact-head [approval](https://github.com/ai4curation/ai-gene-review/pull/5082#pullrequestreview-5556761735)
and [detailed review](https://github.com/ai4curation/ai-gene-review/pull/5082#issuecomment-6230973558)
resolve the two required changes. The reviewer accepts the microtubule-binding
support and withdraws the blocking partner-class objection after checking the
project instruction and explicit assay limits. Remaining suggestions are advisory;
there are no inline comments or unresolved review threads.

All 17 approved files have identical blobs and modes in the merge. Its sole
parent is `7bbbe4f59c5b14d9b053d691deba3a8c5726d9bf`; the complete delta contains
exactly those 17 additions, including two DCDC2 history records and ten publication
caches. All 158,745 paths outside the delta are unchanged.
Complete saved trees were authenticated against the Git commit tree hashes, and
all 17 captured file contents were checked against their Git blob identifiers.

The actual-main push [run 39142088672](https://github.com/ai4curation/ai-gene-review/actions/runs/39142088672)
and [test job 117718406876](https://github.com/ai4curation/ai-gene-review/actions/runs/39142088672/job/117718406876)
completed successfully at 2026-10-18T15:53:59Z. Its full raw log is preserved in the
merge audit. The operative log identifies main and its parent, detects the exact
17-file delta and passes strict changed-gene validation on DCDC2 with 19 documented
generic-binding policy advisories. The approving reviewer accepts the retained
association/class distinctions under the project instruction. All 12,958 history
records validated, 42 history tests passed and 708 family reviews validated.
Residue-site checks recorded 10,417 passes, no failures and 23 unresolved cases;
gene residue checks recorded 617 passes, no failures and two unresolved cases.
Other unrelated family/member uncertainties remain disclosed by those checks.

This main-push workflow was scoped: general tests, examples, merge-queue schema,
agentic checks and standalone source-evidence validation were skipped. No fresh
full-suite execution is claimed. ROOT read all test/docs steps and annotations;
the owner independently read all test steps and operative gene/history/family
results. There are no failure annotations. The separate documentation push
run 39142088680 also succeeded. The distinct [merge-group run 39139566172](https://github.com/ai4curation/ai-gene-review/actions/runs/39139566172)
succeeded at the same SHA; only its run metadata is used here, not a repeated
full job-log audit or a substitute for actual-main evidence.

The review file remains DRAFT with the 19 accepted policy advisories. Advisory
review suggestions about wording, product representation and knowledge gaps do
not become required changes. Completion records approved, merged curation; ROOT
is the coordinating AI agent, not a human maintainer sign-off.

Availability was recomputed from the complete actual-main tree: 7,982
reviews, including 3,007 human reviews. Of 1,170 catalogue
genes with reviews, 444 are credited and 726 remain uncredited;
1,706 catalogue genes still lack a review. DCDC2 alone supplies the
one added review and completion since the preceding checkpoint.

This update preserves all 2,876 catalogue identities and association texts,
all 235 historical queue objects, all 92 earlier completion updates, the complete
preceding progress text and 183 prior project history records. Only the
DCDC2 checkbox changes; completion update 93 is appended. No gene review, source
cache, runtime file or earlier history record is edited by this tracker update.

## Completion checkpoint 445 — 2026-10-18 16:14:34 UTC

**445 complete; 2,431 remaining out of 2,876 primary catalogue genes.**
DCLRE1C is the sole addition to checkpoint 444. Its approved head
`5a2760761b431c0ba318236e86611fe3322c5be1` in
[#5083](https://github.com/ai4curation/ai-gene-review/pull/5083) merged as
[`e734e32bef52`](https://github.com/ai4curation/ai-gene-review/commit/e734e32bef526741f14422b1489a0a6cf03f1e50).
The exact-head [formal approval](https://github.com/ai4curation/ai-gene-review/pull/5083#pullrequestreview-5556870444)
and [detailed review](https://github.com/ai4curation/ai-gene-review/pull/5083#issuecomment-6231293539)
accept the three requested changes and qualifier correction. Remaining observations
are nonblocking; no inline comments or unresolved review threads remain at the audit.

All 45 approved files have identical blobs and modes in the merge. The immediate
parent is `28ce6af8efa0c260e8bae7b6b0783376deef99cf`. The delta consists of six gene
files, two append-only history records, 30 publication caches and seven Reactome
caches. All 158,762 paths outside that delta are unchanged. Complete saved trees
were authenticated against their Git commit hashes, and every changed file was
checked against its Git blob identifier. The commit's older authored timestamp
does not replace the verified PR merge event time.

The actual-main [push run 39144107165](https://github.com/ai4curation/ai-gene-review/actions/runs/39144107165)
and [test job 117724327377](https://github.com/ai4curation/ai-gene-review/actions/runs/39144107165/job/117724327377)
completed successfully at 2026-10-18T16:21:02Z. Its saved log shows strict validation
of the changed DCLRE1C review, 12,960 history records, 42 history tests and 708 family
files passing. General tests, examples, all-gene schema validation and automation
were skipped on this scoped push; those are not represented as post-merge runs.

The distinct [merge-group run 39142091286](https://github.com/ai4curation/ai-gene-review/actions/runs/39142091286)
at the same exact SHA completed successfully before merge. Its actual log shows
all-gene schema validation with no issues, 12 valid/invalid examples passing,
3,940 main tests passing with one skipped and 84 deselected, 252 doctests passing
with 37 skipped, and 415 automation tests passing. Typing and lint checks passed.
All 82 selected job steps and eight annotations were inspected across the merge
group, main push and [documentation run 39144107160](https://github.com/ai4curation/ai-gene-review/actions/runs/39144107160).
No failure annotation was present. Unrelated module/family ontology warnings,
documentation-link warnings and action deprecations remain disclosed. The docs
workflow pushed gh-pages; no independent served-page inspection is asserted.
Eight incidental issue-comment workflows were skipped. Earlier PR test/review
success is retained as metadata, distinct from the inspected merge/main logs.

The merged review is COMPLETE and retains one explicit UNDECIDED annotation.
Completion records accepted and merged curation, not a claim that every scientific
uncertainty is resolved. ROOT independently accepted the merge proof after replay
and complete review/CI inspection; ROOT is the coordinating AI agent, not a human
maintainer sign-off.

The complete actual-main tree contains 7,983 reviews, including 3,008
human reviews. Of 1,171 catalogue genes with reviews, 445 are
credited and 726 remain uncredited; 1,705 catalogue
genes still lack a review file. DCLRE1C alone supplies the additional available
review and completion since checkpoint 444.

This update preserves all 2,876 catalogue identities and association texts,
235 historical queue objects, 93 prior completion updates, the complete preceding
progress text and 183 prior project history records. Only the DCLRE1C checkbox
changes relative to checkpoint 444, and update 94 is appended. No gene review,
source cache, runtime file or earlier history is edited by this tracker update.

## Completion checkpoint 446 — 2026-10-18 16:48:20 UTC

**446 complete; 2,430 remaining out of 2,876 primary catalogue genes.**
DDB2 is the sole addition to checkpoint 445. Its approved head
`ee8a2dd11241467cb1fe1c6666a0456275cd2689` in
[#5084](https://github.com/ai4curation/ai-gene-review/pull/5084) merged as
[`95963b9be78a`](https://github.com/ai4curation/ai-gene-review/commit/95963b9be78a614c8db78e75759e02b15ed645b5).
The exact-head [formal approval](https://github.com/ai4curation/ai-gene-review/pull/5084#pullrequestreview-5556929290)
and [detailed review](https://github.com/ai4curation/ai-gene-review/pull/5084#issuecomment-6231443645)
accept the clarified original-source provenance and the complex-contribution core
correction. Remaining suggestions are nonblocking. No inline comments or
unresolved review threads were present in the audit.

All five approved file blobs and modes are identical in the merge. The immediate
parent is `e734e32bef526741f14422b1489a0a6cf03f1e50`. The delta modifies the review
YAML and HTML and adds notes plus two history records. All 158,805 paths outside
that delta are unchanged. Complete saved head, merge and parent trees were
authenticated against their commit objects, and each changed file against its Git
blob identifier. The PR merge event time above is distinct from authored dates.

The actual-main [push run 39146677012](https://github.com/ai4curation/ai-gene-review/actions/runs/39146677012)
and [test job 117731814617](https://github.com/ai4curation/ai-gene-review/actions/runs/39146677012/job/117731814617)
completed successfully at 2026-10-18T16:54:49Z. Strict DDB2 validation passed with
18 retained generic-binding advisories under the standing ClinGen instruction.
The log separately shows 12,962 history records, 42 history tests and 708 family
files passing. History coverage, all-gene schemas, general tests, examples,
modules and automation were skipped on this scoped push; no pass is claimed for
those skipped steps.

The separate exact-SHA [merge-group run 39144109780](https://github.com/ai4curation/ai-gene-review/actions/runs/39144109780)
completed successfully before merge. Its actual log shows all-gene schemas with
no issues, 12 examples passing, 3,940 main tests passing with one skipped and 84
deselected, 252 doctests passing with 37 skipped, and 415 automation tests passing.
Typing and lint passed. The earlier exact-head PR test also passed scoped review
validation with the same 18 advisories; its history-coverage step passed. The
reviewer could not run the ordinary suite itself, so its approval is not used as
a substitute for these actual CI results.

All 130 job steps and 14 annotations were inspected across the PR test/review,
merge group and main push test/docs. No failure annotation was present. Unrelated
family/module ontology notices, test dependency and infrastructure deprecations,
and documentation-link warnings remain disclosed. The [docs push 39146676998](https://github.com/ai4curation/ai-gene-review/actions/runs/39146676998)
completed and pushed gh-pages, without an independent served-page inspection.
Incidental issue-comment workflows are outside this DDB2 gate and were inspected
only as metadata; one was still active at capture.

The sole YAML semantic change moves the second core's GO:0004842 from
`molecular_function` to `contributes_to_molecular_function`. All 81 source and
review objects, 60 references, five products and other YAML content remain exact.
The merged file retains its inherited COMPLETE status, while the accepted
histories disclose the pre-existing computed DRAFT discrepancy. No new status
calculation or warning-driven rewrite is implied. ROOT independently accepted the
merge proof after replay and full review/CI inspection; this is coordinating AI
agent acceptance, not a human maintainer sign-off.

There are still 7,983 review files, including 3,008 human reviews.
Of 1,171 catalogue genes with reviews, 446 are credited and
725 remain uncredited; 1,705 catalogue genes lack a review
file. DDB2 already had a review, so availability is unchanged. This is its first
accepted campaign completion, not an extra credit for a product or follow-up.

This update preserves all 2,876 catalogue identities and association texts,
235 historical queue objects, 94 prior completion updates, the full preceding
progress text and 183 prior project history records. Only DDB2's checkbox changes
relative to checkpoint 445, and update 95 is appended. No gene review, source
cache, runtime file or earlier history is edited by this tracker update.

## Completion checkpoint 447 — 2026-10-18 17:10:05 UTC

**447 complete; 2,429 remaining out of 2,876 primary catalogue genes.**
DCX is the sole addition to checkpoint 446. Approved head
`2204701c7274a7aa9228e34739139db55cac3751` in
[#5085](https://github.com/ai4curation/ai-gene-review/pull/5085) merged as
[`22f429edcf1a`](https://github.com/ai4curation/ai-gene-review/commit/22f429edcf1adff6285ecc152aa2a898d56646e5),
with immediate parent `95963b9be78a614c8db78e75759e02b15ed645b5`.
The exact-head [formal approval](https://github.com/ai4curation/ai-gene-review/pull/5085#pullrequestreview-5556998310)
and [detailed review](https://github.com/ai4curation/ai-gene-review/pull/5085#issuecomment-6231652422)
resolve the blocking evidence objections. The reviewer withdrew the ancestor and
stoichiometry objections, accepted the assay versus native-context limits, and
recorded the axoneme-action disagreement as nonblocking. No inline comments or
review threads were present. Remaining evidence-navigation and historical-prose
suggestions are nonblocking and do not authorize rewriting earlier histories.

All eight approved file blobs and modes match the merge. Three DCX files are
modified (review YAML, rendered HTML and notes); the source-evidence guide, two
history records and two publication caches are added. All 158,807 paths outside
this delta are unchanged. Complete saved head, parent and merge trees were
authenticated against their commits, and each changed blob against its Git
identifier. The merge event time above is distinct from authored dates.

The actual-main [push run 39148316947](https://github.com/ai4curation/ai-gene-review/actions/runs/39148316947)
and [test job 117736623696](https://github.com/ai4curation/ai-gene-review/actions/runs/39148316947/job/117736623696)
completed successfully at 2026-10-18T17:17:27Z. Its full log and operative command,
validation and warning windows were inspected: strict DCX validation passed with
seven retained generic-binding advisories under the explicit ClinGen project
instruction; 12,964 history records, 42 history tests and 708 family files passed.
All-gene schemas, modules, general tests, examples and automation were skipped on
this scoped push. The current-main snapshot equals the audited merge.

The separate exact-SHA [merge-group run 39146679553](https://github.com/ai4curation/ai-gene-review/actions/runs/39146679553)
passed before merge. Its operative log shows all-gene schemas with no issues,
12 examples passing, 3,940 tests passing with one skipped and 84 deselected,
252 doctests passing with 37 skipped, and 415 automation tests passing; typing
and lint passed. The exact-head PR test also succeeded with the same seven
advisories, satisfying the review's conditional approval. The reviewer did not
run the ordinary suite itself; that approval is not substituted for actual CI.
The [docs push 39148316995](https://github.com/ai4curation/ai-gene-review/actions/runs/39148316995)
completed and pushed gh-pages; no served-page inspection is claimed.

The first merge audit captured the push while running; a separately sealed
terminal addendum completed the proof without replacing that earlier snapshot.
All 35 terminal push steps and all three current annotations were read, with no
failed step or failure annotation. The two other merge-SHA jobs contributed
47 inspected steps and five annotations; the earlier pending push annotation
snapshot was empty and is not treated as the final annotation count. Family
validation retains unrelated unresolved records and infrastructure notices.
The complete logs remain available, with actual read windows and scope stated;
no source-paper body reading or new gene validation was performed for this audit.

All 39 imported annotation dictionaries and the inherited NEW dictionary are
preserved. The merged 40 entries comprise 11 ACCEPT, 13 MODIFY,
12 KEEP_AS_NON_CORE, 3 UNDECIDED and one inherited NEW. Description, both products
and core functions are unchanged from the immediate parent. The merged DRAFT
status and seven accepted policy advisories are explicit; completion here means
an accepted, verified campaign review, not disappearance of unresolved evidence.
ROOT accepted both saved proofs and the complete operative review/CI evidence.
That is coordinating AI-agent acceptance, not a human maintainer sign-off.

There remain 7,983 review files, including 3,008 human reviews.
Of 1,171 catalogue genes with reviews, 447 are credited and
724 remain uncredited; 1,705 catalogue genes lack a review
file. DCX already had a review, so availability is unchanged. Only its first
accepted campaign completion is counted.

This update preserves all 2,876 catalogue identities and association texts,
235 historical queue objects, 95 prior completion updates, the complete preceding
progress text and 183 prior project history records. Only DCX's checkbox changes
relative to checkpoint 446, and update 96 is appended. No gene review, source
cache, runtime file or prior history is edited by this tracker update.

## Completion checkpoint 448 — 2026-10-18 17:32:58 UTC

**448 complete; 2,428 remaining out of 2,876 primary catalogue genes.**
DDC is the sole addition to checkpoint 447. Approved head
`b276d279c68e23af68285f74a3b4a94433c87862` in
[#5086](https://github.com/ai4curation/ai-gene-review/pull/5086) merged as
[`c4be76827e7a`](https://github.com/ai4curation/ai-gene-review/commit/c4be76827e7a4cb01fb9c77ed9d3f4b98933b1fb),
with immediate parent `22f429edcf1adff6285ecc152aa2a898d56646e5`.
The exact-head [formal approval](https://github.com/ai4curation/ai-gene-review/pull/5086#pullrequestreview-5557039655)
and [detailed review](https://github.com/ai4curation/ai-gene-review/pull/5086#issuecomment-6231794240)
accept the previous blockers as resolved or adequately answered. The amino-acid
process was refined to GO:0009072; the AR-term objection was withdrawn after
consideration of the dated official ontology response. The remaining external
source-note reproducibility limitation was explicitly nonblocking because the
load-bearing claims had independent validator-checked support. Residual core-scope,
ontology-cache and wording suggestions are optional. No inline comments or review
threads were present; this tracker does not implement optional scientific edits.

All ten approved file blobs and modes match the merge. Three DDC files are modified
(review YAML, rendered HTML and notes); two evidence/source guides, two history
records and three publication caches are added. All 158,812 paths outside this
delta are unchanged. Complete saved head, parent and merge trees, commit identities
and changed blobs were authenticated. This proves the approved payload at the
merge, not equality between the entire PR tree and main. The merge event time above
is distinct from authored dates.

The actual-main [push run 39150099881](https://github.com/ai4curation/ai-gene-review/actions/runs/39150099881)
[test job 117741791093](https://github.com/ai4curation/ai-gene-review/actions/runs/39150099881/job/117741791093)
completed successfully at 2026-10-18T17:40:19Z. All 35 terminal step records and three
annotations were read. Its full log is saved, with operative command/result windows
inspected: strict DDC validation passed with one retained generic-binding NC
advisory, 12,966 history records had no issues, 42 history tests passed, and 708
family files had no blocking issues. All-gene schemas, modules, history coverage,
examples, general tests, agentic automation and full upstream PAINT were skipped on
this scoped push. They are not claimed to have run on actual main.

The separate exact-SHA [merge-group run 39148319713](https://github.com/ai4curation/ai-gene-review/actions/runs/39148319713)
passed before merge. Its operative log shows all-gene schemas, scoped modules,
12 examples, 3,940 tests with one skipped and 84 deselected, 252 doctests with 37
skipped, and 415 automation tests passing; typing passed for 268 files. It also
passed the history and family checks. History-coverage and full upstream-PAINT
steps were skipped. The exact-approved-head test and reviewer jobs succeeded.
The reviewer's eight permission denials and `is_error: false` are reported
separately from its independently present exact-head approval; they are not CI
failures. The [docs push 39150099911](https://github.com/ai4curation/ai-gene-review/actions/runs/39150099911)
completed and pushed the site; no served-page inspection is claimed.

The original merge snapshot captured actual-main CI while running. A separately
sealed terminal addendum completed that proof without replacing the prior snapshot.
The four previously terminal jobs supplied 95 recorded steps and 11 annotations;
the later push supplied its own 35 steps and three annotations. All annotations
were notices/warnings, with no failure-level annotation. Unrelated family
adjudication categories and infrastructure notices remain explicitly distinct
from blocking failures. Complete logs are archived, but only stated operative
windows are claimed read. No source-paper body or new local gene suite was read or
run for this completion update.

The merged review retains 27 annotations: 17 ACCEPT, five TOO_GENERAL,
three KEEP_AS_NON_CORE and two MODIFY, with no UNDECIDED. It contains four products
and two core functions and remains DRAFT. The accepted generic-binding advisory
and DRAFT status do not prevent completion of an accepted and verified campaign
review. ROOT accepted both saved merge proofs and their review/CI evidence; this
is coordinating AI-agent acceptance, not a human maintainer sign-off.

There remain 7,983 review files, including 3,008 human reviews.
Of 1,171 catalogue genes with reviews, 448 are credited and
723 remain uncredited; 1,705 catalogue genes lack a review
file. DDC already had a review, so availability is unchanged. Only its first
accepted campaign completion is counted.

This update preserves all 2,876 catalogue identities and association texts,
235 historical queue objects, 96 prior completion updates, the complete preceding
progress text and 183 prior project history records. Only DDC's checkbox changes
relative to checkpoint 447, and update 97 is appended. No gene review, source
cache, runtime file or prior history is edited. The publication preimage remains
queued checkpoint 443; this private successor is held until ROOT separately
requalifies and authorizes publication.

## Completion checkpoint 449 — 2026-10-18 18:05:01 UTC

**449 complete; 2,427 remaining out of 2,876 primary catalogue genes.**
DDHD1 is the sole addition to checkpoint 448. Approved head
`bbe34f00d09d848d64d3e3ebb3cea1fda256b6e6` in
[#5087](https://github.com/ai4curation/ai-gene-review/pull/5087) merged as
[`66220febb3d8`](https://github.com/ai4curation/ai-gene-review/commit/66220febb3d8e4c2c16095885a79ceaac6d3b937),
with immediate parent `c4be76827e7a4cb01fb9c77ed9d3f4b98933b1fb`.
The exact-head [formal approval](https://github.com/ai4curation/ai-gene-review/pull/5087#pullrequestreview-5557023674)
and [detailed review](https://github.com/ai4curation/ai-gene-review/pull/5087#issuecomment-6231757131)
accept the prior blockers as resolved. The reviewer explicitly withdraws its
generic-binding objection under the standing ClinGen instruction. Tissue and
SPG28 context, product scope, oligomerization notes, source locators and append-only
history are accepted. Experiments, a possible later HuRI refinement, policy-warning
wording and optional short quotations remain suggestions, not blocking requests.
There are no inline comments or review threads.

All 20 approved PR file blobs and modes match the merge. The actual immediate-parent
delta contains 19 additions: six gene files, two histories, two PANTHER lookup
files, eight publication caches and one Reactome cache. The twentieth PR path,
`publications/PMID_23186163.md`, was already identical in the parent. All 158,822
paths outside the 19-path delta are unchanged. Complete saved head, parent and
merge trees and their commit objects were authenticated, together with all 20
saved blobs. This establishes approved-path equality, not equality of the entire
PR branch and main. The cutoff is the merge event time, not an authored date.

The actual-main [push test run 39152524224](https://github.com/ai4curation/ai-gene-review/actions/runs/39152524224)
and [job 117748902797](https://github.com/ai4curation/ai-gene-review/actions/runs/39152524224/job/117748902797)
passed strict changed-DDHD1 validation with one expected generic-binding non-core
advisory, 12,968 history records without issues, 42 history tests, and 708 family
files. Its all-gene schemas, modules, history coverage, examples, general tests,
automation and full upstream PAINT steps were skipped. Those scopes are not
claimed as actual-main executions.

The exact-SHA [merge-group run 39150102446](https://github.com/ai4curation/ai-gene-review/actions/runs/39150102446)
passed the scoped checks and broad schemas/modules, 12 examples, 3,940 tests with
one skipped and 84 deselected, 252 doctests with 37 skipped, typing for 268 files,
Ruff, 415 Python automation tests and 19 JavaScript tests with zero failures.
History coverage and full upstream PAINT were skipped there. An ignored SQL
destructor exception appears after the successful general-test summary; subsequent
checks and the job succeeded. The event is retained in the evidence rather than
silently omitted or characterized as a failed suite.

The approved-head [test run 39017424539](https://github.com/ai4curation/ai-gene-review/actions/runs/39017424539)
passed scoped DDHD1 validation, 12,017 histories, 42 history tests, 695 family files
and history coverage identifying both DDHD1 session records. Its broad test scopes
were skipped. The [review run 39017424544](https://github.com/ai4curation/ai-gene-review/actions/runs/39017424544)
succeeded and recorded the exact-head approval; three permission denials with
`is_error: false` did not prevent that output. Independent test jobs provide the
validation evidence. The actual-main [documentation run 39152524403](https://github.com/ai4curation/ai-gene-review/actions/runs/39152524403)
successfully built and pushed gh-pages despite nonblocking documentation warnings;
no served-page inspection is claimed.

All five operative jobs were terminal success. All 130 step records and 14
annotations were read; annotations were notices/warnings, with no failure level.
Full logs are archived and exact operative windows were inspected; whole
installation logs are not claimed read. Incidental comment/mention workflows
were inventoried separately as skipped, not counted as DDHD1 validation.

The merged review deliberately remains DRAFT: 12 source assertions comprise three
ACCEPT, four MODIFY, two REMOVE, two KEEP_AS_NON_CORE and one UNDECIDED, with no NEW.
It retains four products, one core function and 15 references. The one undecided
source and accepted policy advisory remain visible; neither changes the fact that
the campaign review was approved, merged and verified. ROOT accepted the saved
merge proof and complete review/CI audit as completion 449. This is coordinating
AI-agent acceptance, not a human maintainer sign-off. No primary source body or
ordinary local suite was reread or run for this tracker update.

The authenticated main tree now contains 7,984 review files, including
3,009 human reviews. Of 1,172 catalogue genes with reviews,
449 are credited and 723 remain uncredited; 1,704 lack a review
file. DDHD1 adds one available review and one completion; no other gene receives
credit. Availability was re-inventoried from this exact tree.

All 2,876 catalogue identities and association texts, 235 historical queue objects,
97 prior completion updates, the entire preceding progress text and 183 project
history records remain preserved. Only DDHD1's checkbox changes relative to
checkpoint 448; update 98 is appended. No gene, source cache, runtime or prior
history is edited. The publication preimage remains queued checkpoint 443; this
private successor is held until ROOT separately requalifies publication.

## Completion checkpoint 450 — 2026-10-18 18:27:44 UTC

**450 complete; 2, 426 remaining out of 2,876 primary catalogue genes.**
DDR2 is the sole addition to checkpoint 449. Approved head
`a43188ff51c0ddbaa3e409cbcd119b943bf4eaf5` in
[#5089](https://github.com/ai4curation/ai-gene-review/pull/5089) merged as
[`ac35012f4993`](https://github.com/ai4curation/ai-gene-review/commit/ac35012f4993a7d06938bf7b7069c6e7d921dcc0),
with immediate parent `66220febb3d8e4c2c16095885a79ceaac6d3b937`.
The exact-head [formal approval](https://github.com/ai4curation/ai-gene-review/pull/5089#pullrequestreview-5557446385)
and [detailed review](https://github.com/ai4curation/ai-gene-review/pull/5089#issuecomment-6232957392)
accept the two expression-response annotations as UNDECIDED, rather than the
reviewer's earlier over-annotation suggestion. The reviewer acknowledges the
limits of abstract-only evidence. All seven earlier suggestions were implemented
or explicitly declined; the remaining cache-versus-original-access wording
suggestion is expressly nonblocking. Both earlier inline threads are resolved
and outdated.

All 25 approved PR blobs and modes match the merge. All 25 paths are additions
relative to the immediate parent: seven gene files, including historical rendered
HTML, two history records and 16 publication caches. All 158,841 paths outside
that delta are unchanged. Complete saved head, parent and merge trees authenticate
against their commit objects. This proves equality of the approved paths, not
identity of the whole PR branch and main. The cutoff is the merge event time.

The actual-main [push test run 39154253413](https://github.com/ai4curation/ai-gene-review/actions/runs/39154253413)
and [job 117754074534](https://github.com/ai4curation/ai-gene-review/actions/runs/39154253413/job/117754074534)
passed strict changed-DDR2 validation with two expected generic-binding non-core
advisories, 12,970 history records, 42 history-schema tests and 708 family files.
Broad schemas, modules, examples, general tests and automation were skipped in
this job; they are not represented as actual-main executions.

The exact-SHA [merge-group run 39152527229](https://github.com/ai4curation/ai-gene-review/actions/runs/39152527229)
passed those scoped checks plus broad schemas/modules, 12 examples, 3,940 tests
with one skipped and 84 deselected, 252 doctests with 37 skipped, typing/lint,
415 Python automation tests and 19 JavaScript tests. An ignored SQL destructor
exception followed the passing pytest summary; later checks and the whole job
succeeded. History coverage and full upstream PAINT were skipped in this job.

The approved-head [test run 39021892379](https://github.com/ai4curation/ai-gene-review/actions/runs/39021892379)
passed scoped DDR2 validation, 12,026 histories, 42 history tests, 695 families and
history coverage. Its broad suites were skipped. The successful second attempt
of [review run 39021892380](https://github.com/ai4curation/ai-gene-review/actions/runs/39021892380)
produced the exact-head approval. Its nine permission denials did not prevent
artifact review; the reviewer explicitly deferred unavailable local validation
to independent CI. The first attempt failed on a logged session limit, with 13
steps and 7 annotations, four at failure level. That historical service failure
is preserved separately and was superseded on the same head; it is not fresh
scientific changes requested.

The actual-main [documentation run 39154253423](https://github.com/ai4curation/ai-gene-review/actions/runs/39154253423)
built and pushed gh-pages despite nonfatal link/deprecation warnings. No browser
inspection of every deployed page is claimed. All five operative jobs were
terminal success. The accepted merge audit read all 130 operative steps and 14
annotations, none at failure level, plus the full current reviews and resolved
threads. Full logs are archived with exact operative windows; whole installation
logs are not claimed read. Incidental comment/mention workflows were inventoried
as skipped and are not counted as DDR2 validation.

The merged review remains DRAFT with 74 source rows: 17 ACCEPT, 38 KEEP_AS_NON_CORE,
14 MODIFY, 4 UNDECIDED and 1 TOO_GENERAL. One core and 31 references are retained.
There is no alternative_products or gene_products block; the committed history
records one 855-residue precursor. This tracker update makes no new product
judgment or status recomputation. The four unresolved sources and two policy
advisories remain visible. ROOT accepted the full merge/CI evidence as completion
450; ROOT is the coordinating AI agent, not a human maintainer sign-off.

The authenticated main tree now contains 7,985 reviews, including
3,010 human reviews. Of 1,173 catalogue genes with reviews,
450 are credited and 723 remain uncredited; 1,703 lack a review
file. DDR2 adds one available review and one completion. No other gene gains credit.

All 2,876 catalogue identities and association texts, 235 historical queue objects,
98 prior completion updates, the complete prior progress text and 183 project
history records remain preserved. Only DDR2's checkbox changes relative to 449;
update 99 is appended. No gene, source cache, runtime or prior history is edited.
The publication preimage remains queued checkpoint 443. This private successor
is held until ROOT separately requalifies publication; no remote action occurs.

## Completion checkpoint 451 — 2026-10-18 19:00:24 UTC

**451 complete; 2,425 remaining out of 2,876 primary catalogue genes.**
DDX11 is the sole addition to checkpoint 450. Approved head
`38c2dcfcb8bca92ce14b2492f50375025ad35d74` in
[#5088](https://github.com/ai4curation/ai-gene-review/pull/5088) merged as
[`d00415e9a6d8`](https://github.com/ai4curation/ai-gene-review/commit/d00415e9a6d83d80030610ea88875ac196fb0db4),
with immediate parent `ac35012f4993a7d06938bf7b7069c6e7d921dcc0`.
The exact-head [formal approval](https://github.com/ai4curation/ai-gene-review/pull/5088#pullrequestreview-5557462174)
and [detailed review](https://github.com/ai4curation/ai-gene-review/pull/5088#issuecomment-6232955655)
resolve all three blockers: seven action/reason mismatches, source-specific
helicase refinements, and replication/cohesion core process coverage. Remaining
suggestions are optional. There are no inline comments or review threads.

All 18 approved PR blobs and modes match the merge. All are additions relative
to the immediate parent: six gene files (including historical rendered HTML),
two history records, nine publication caches and one Reactome cache. All 158,866
outside paths remain unchanged. Complete saved trees authenticate against their
commit objects. This verifies approved paths without asserting whole-branch
identity. The cutoff is the merge event time.

The actual-main [push test run 39156749671](https://github.com/ai4curation/ai-gene-review/actions/runs/39156749671)
([job 117761445338](https://github.com/ai4curation/ai-gene-review/actions/runs/39156749671/job/117761445338))
passed strict changed-DDX11 validation, 12,972 histories, 42 history tests and
708 family files. Eight generic-binding non-core warnings and one chromatin-binding
consistency advisory remain acknowledged. Broad schemas, modules, examples,
general tests and automation were skipped in this actual-main job.

The exact-SHA [merge-group run 39154256066](https://github.com/ai4curation/ai-gene-review/actions/runs/39154256066)
passed those scoped checks plus all-gene schemas, 673 modules, 12 examples,
3,940 tests (one skipped, 84 deselected), 252 doctests (37 skipped), typing/lint,
415 Python automation tests and 19 JavaScript tests. An ignored SQL destructor
exception followed the passing pytest summary; subsequent checks and the job
passed. History coverage and full upstream PAINT checks were skipped here.

The approved-head [test run 39021231928](https://github.com/ai4curation/ai-gene-review/actions/runs/39021231928)
passed strict DDX11 validation, 12,024 histories, 42 history tests, 695 family
files and history coverage. Its broad suites were skipped. Attempt 2 of
[review run 39021231914](https://github.com/ai4curation/ai-gene-review/actions/runs/39021231914)
produced the approval. Its seven permission denials and unavailable local
validation are recorded; independent CI passed. Attempt 1 failed on an explicit
session limit (13 steps, seven annotations, four at failure level) and was
superseded on the same head. That service failure is retained separately.

The actual-main [documentation run 39156749659](https://github.com/ai4curation/ai-gene-review/actions/runs/39156749659)
built and pushed gh-pages despite nonfatal link/deprecation warnings. No visual
inspection of every deployed page is claimed. All five operative jobs passed;
the accepted audit accounts for all 130 operative steps and 14 annotations,
none at failure level. Full logs and operative windows are archived. Incidental
skipped comment workflows are not counted as validation.

The merged review remains DRAFT with 87 sources: 34 ACCEPT, 31 KEEP_AS_NON_CORE,
19 MODIFY and three UNDECIDED. It retains five official alternative products,
one core, 22 references and its NOT flag. No new product judgment or status
recomputation is made here. ROOT, the coordinating AI agent, accepted the
merge evidence as completion 451; this is not a human maintainer sign-off.

The authenticated tree contains 7,986 reviews, including 3,011 human reviews.
Of 1,174 catalogue genes with reviews, 451 are credited and
723 remain uncredited; 1,702 lack a review file.
All 2,876 catalogue identities and association texts, 235 historical queue
objects, 99 prior completion updates, prior progress text and 183 project
histories remain preserved. Only DDX11's checkbox changes relative to 450;
update 100 is appended. Gene, source, runtime and historical files are unchanged.
The publication preimage remains queued checkpoint 443. This private successor
is held pending separate publication qualification; no remote action occurs.

## Completion checkpoint 452 — 2026-10-18 20:02:38 UTC

**452 complete; 2,424 remaining out of 2,876 primary catalogue genes.**
DEPDC5 is the sole addition to checkpoint 451. Approved head
`1df572006295104a82e18622efe4e94f20f24144` in
[#5091](https://github.com/ai4curation/ai-gene-review/pull/5091) merged as
[`790ca0a86e3a`](https://github.com/ai4curation/ai-gene-review/commit/790ca0a86e3abf240be01bfad42ffa9a348646d2),
with immediate parent `a82ae1968bd472f368fe7c141c5938229db1168c`.
The exact-head [formal approval](https://github.com/ai4curation/ai-gene-review/pull/5091#pullrequestreview-5557538719)
and [detailed review](https://github.com/ai4curation/ai-gene-review/pull/5091#issuecomment-6233230306)
resolved the core-coverage and evidence-support requests. Minor spacing and
duplication suggestions are nonblocking. There are no inline comments or review threads.

All 26 approved PR blobs and modes match the merge, and all are additions relative
to its immediate parent. The other 158,912 paths are unchanged. Complete saved
trees authenticate against their commit objects. The two append-only histories,
machine sources, rendered artifact and accepted candidate files match the final
published evidence. This verifies the approved paths without asserting whole-branch identity.

The approved-head [test run 39027766145](https://github.com/ai4curation/ai-gene-review/actions/runs/39027766145),
[review run 39027766126](https://github.com/ai4curation/ai-gene-review/actions/runs/39027766126),
exact-SHA [merge-group run 39158973668](https://github.com/ai4curation/ai-gene-review/actions/runs/39158973668),
actual-main [push test 39161493056](https://github.com/ai4curation/ai-gene-review/actions/runs/39161493056),
and actual-main [documentation run 39161492882](https://github.com/ai4curation/ai-gene-review/actions/runs/39161492882)
all succeeded. The actual-main test completed at 20:10:15 UTC; documentation built
and pushed gh-pages. No visual inspection of the deployed site is claimed.

All three test jobs passed strict DEPDC5 validation with five expected generic-binding
non-core advisories under the standing project instruction. Actual-main and
merge-group history validation covered 12,996 records and 42 tests; family validation
covered 708 families. Broad schema, examples, tests and automation ran in the merge
group, including 3,940 passing tests, 252 doctests, 415 automation tests and 19 JavaScript
tests. Those broad suites were skipped on the PR and actual-main jobs. An ignored SQL
destructor exception followed the passing test summary; later checks and the job passed.
The reviewer could not run local validation; the successful independent CI is separate
evidence. Nonfatal dependency and documentation-link warnings remain recorded.

The audit captured ten runs, twelve jobs, 130 steps and fourteen annotations, with no
failure annotation. Five jobs executed; seven incidental comment/review jobs were skipped.
Full logs and operative windows are archived. The merged review remains DRAFT with
44 sources (25 ACCEPT, seven MODIFY, twelve KEEP_AS_NON_CORE), eight official products,
one integrated core and 28 references. No new product judgment or status recomputation
is made here. ROOT, the coordinating AI agent, accepted the merge evidence as completion
452; this is not a human maintainer sign-off.

The authenticated tree contains 7,987 reviews, including 3,012 human reviews.
Of 1,175 catalogue genes with reviews, 452 are credited and
723 remain uncredited; 1,701 lack a review file.
All 2,876 catalogue identities and association texts, 235 historical queue objects,
100 prior completion updates and prior progress text remain preserved. Only DEPDC5's
checkbox changes relative to 451; update 101 is appended. Gene, source, runtime and
historical files are unchanged. The publication preimage remains queued checkpoint 443;
this private successor is held pending separate publication qualification.

## Completion checkpoint 473 — 2026-10-21 00:21:17 UTC

**473 complete; 2,403 remaining out of 2,876 primary catalogue genes.**
This update preserves checkpoint 452 and adds exactly 21 distinct genes: DDX41
(452→453), the first ten-gene audit batch (453→463), and the second ten-gene batch
(463→473). Later batches are excluded. The coordinating agent accepted the three
sealed audit records; this is not a human maintainer sign-off or a new biological
re-review. Accepted source decisions, unresolved annotations and product limits
remain unchanged.

| Gene / PR | Approved head / merge | Approval / detail | Exact PR paths | Immediate main test / docs | Exact merge-group test |
|---|---|---|---:|---|---|
| [DDX41 #5090](https://github.com/ai4curation/ai-gene-review/pull/5090) | [`babb88ce2f40`](https://github.com/ai4curation/ai-gene-review/commit/babb88ce2f4056502a5ab32bf1581edd083f0006) / [`653a15c8309e`](https://github.com/ai4curation/ai-gene-review/commit/653a15c8309ed6cd9a9c5cff373a07c7a65a4a93) | [approval](https://github.com/ai4curation/ai-gene-review/pull/5090#pullrequestreview-5557581837) / [detail](https://github.com/ai4curation/ai-gene-review/pull/5090#issuecomment-6233362245) | 29 | [39164000966](https://github.com/ai4curation/ai-gene-review/actions/runs/39164000966) success / [39164000992](https://github.com/ai4curation/ai-gene-review/actions/runs/39164000992) success | [39161495647](https://github.com/ai4curation/ai-gene-review/actions/runs/39161495647) success |
| [DGKE #5094](https://github.com/ai4curation/ai-gene-review/pull/5094) | [`f94d4f7d86c9`](https://github.com/ai4curation/ai-gene-review/commit/f94d4f7d86c9339be463af6de0cbbbe641f850c3) / [`51f9e16d8801`](https://github.com/ai4curation/ai-gene-review/commit/51f9e16d8801f450624e5697659a099852b3ba33) | [approval](https://github.com/ai4curation/ai-gene-review/pull/5094#pullrequestreview-5557598083) / [detail](https://github.com/ai4curation/ai-gene-review/pull/5094#issuecomment-6233396695) | 22 | [39166466485](https://github.com/ai4curation/ai-gene-review/actions/runs/39166466485) success / [39166466508](https://github.com/ai4curation/ai-gene-review/actions/runs/39166466508) success | [39164003526](https://github.com/ai4curation/ai-gene-review/actions/runs/39164003526) success |
| [DEGS1 #5092](https://github.com/ai4curation/ai-gene-review/pull/5092) | [`277db2c325e2`](https://github.com/ai4curation/ai-gene-review/commit/277db2c325e201f9fdc6ccce7211d8a4295be3ae) / [`4a05f894ee6d`](https://github.com/ai4curation/ai-gene-review/commit/4a05f894ee6d7fd6754f9729fac54218f180dc28) | [approval](https://github.com/ai4curation/ai-gene-review/pull/5092#pullrequestreview-5557637596) / [detail](https://github.com/ai4curation/ai-gene-review/pull/5092#issuecomment-6233509172) | 9 | [39168514887](https://github.com/ai4curation/ai-gene-review/actions/runs/39168514887) success / [39168515160](https://github.com/ai4curation/ai-gene-review/actions/runs/39168515160) success | [39166468593](https://github.com/ai4curation/ai-gene-review/actions/runs/39166468593) success |
| [DDX3X #5093](https://github.com/ai4curation/ai-gene-review/pull/5093) | [`465ce8334e2d`](https://github.com/ai4curation/ai-gene-review/commit/465ce8334e2d78e32df0f197a9c9e76159498446) / [`f4a4941aefd6`](https://github.com/ai4curation/ai-gene-review/commit/f4a4941aefd68e2ada4c9f78f16157cd3ea931c7) | [approval](https://github.com/ai4curation/ai-gene-review/pull/5093#pullrequestreview-5557655715) / [detail](https://github.com/ai4curation/ai-gene-review/pull/5093#issuecomment-6233552216) | 55 | [39180447214](https://github.com/ai4curation/ai-gene-review/actions/runs/39180447214) success / [39180447185](https://github.com/ai4curation/ai-gene-review/actions/runs/39180447185) success | [39179010406](https://github.com/ai4curation/ai-gene-review/actions/runs/39179010406) success |
| [DES #5095](https://github.com/ai4curation/ai-gene-review/pull/5095) | [`00ffdd5fac63`](https://github.com/ai4curation/ai-gene-review/commit/00ffdd5fac63da75e4daeb9cbb1ecfbe20543bda) / [`94ac62eafce3`](https://github.com/ai4curation/ai-gene-review/commit/94ac62eafce3bf2645f1fe17a8695795c21851e3) | [approval](https://github.com/ai4curation/ai-gene-review/pull/5095#pullrequestreview-5557849249) / [detail](https://github.com/ai4curation/ai-gene-review/pull/5095#issuecomment-6234095718) | 31 | [39181828974](https://github.com/ai4curation/ai-gene-review/actions/runs/39181828974) success / [39181828957](https://github.com/ai4curation/ai-gene-review/actions/runs/39181828957) success | [39180449829](https://github.com/ai4curation/ai-gene-review/actions/runs/39180449829) success |
| [DGUOK #5096](https://github.com/ai4curation/ai-gene-review/pull/5096) | [`49076e9e3e15`](https://github.com/ai4curation/ai-gene-review/commit/49076e9e3e15703ce83b0eb7783109ccbb092c94) / [`f8a49c1b5036`](https://github.com/ai4curation/ai-gene-review/commit/f8a49c1b5036720d8754e3dd7d22a0fe7b2bce2a) | [approval](https://github.com/ai4curation/ai-gene-review/pull/5096#pullrequestreview-5557900129) / [detail](https://github.com/ai4curation/ai-gene-review/pull/5096#issuecomment-6234213320) | 12 | [39183168173](https://github.com/ai4curation/ai-gene-review/actions/runs/39183168173) cancelled / [39183168066](https://github.com/ai4curation/ai-gene-review/actions/runs/39183168066) success | [39181831026](https://github.com/ai4curation/ai-gene-review/actions/runs/39181831026) success |
| [DHCR24 #5097](https://github.com/ai4curation/ai-gene-review/pull/5097) | [`587ac7bda814`](https://github.com/ai4curation/ai-gene-review/commit/587ac7bda81494384d1751f3687a8bd4473d3a18) / [`a76e2eefb45e`](https://github.com/ai4curation/ai-gene-review/commit/a76e2eefb45e8419701a148ecae36a3077ae4a78) | [approval](https://github.com/ai4curation/ai-gene-review/pull/5097#pullrequestreview-5557944765) / [detail](https://github.com/ai4curation/ai-gene-review/pull/5097#issuecomment-6234363366) | 16 | [39183672110](https://github.com/ai4curation/ai-gene-review/actions/runs/39183672110) cancelled / [39183672116](https://github.com/ai4curation/ai-gene-review/actions/runs/39183672116) success | [39182172955](https://github.com/ai4curation/ai-gene-review/actions/runs/39182172955) success |
| [DHDDS #5098](https://github.com/ai4curation/ai-gene-review/pull/5098) | [`8c035e287392`](https://github.com/ai4curation/ai-gene-review/commit/8c035e28739251d366c86e1e75289106217d9c22) / [`3fe42af909db`](https://github.com/ai4curation/ai-gene-review/commit/3fe42af909db02f8d77b395c338b57af145eec0e) | [approval](https://github.com/ai4curation/ai-gene-review/pull/5098#pullrequestreview-5557995490) / [detail](https://github.com/ai4curation/ai-gene-review/pull/5098#issuecomment-6234491409) | 14 | [39183673052](https://github.com/ai4curation/ai-gene-review/actions/runs/39183673052) cancelled / [39183673049](https://github.com/ai4curation/ai-gene-review/actions/runs/39183673049) cancelled | [39182174939](https://github.com/ai4curation/ai-gene-review/actions/runs/39182174939) success |
| [DHCR7 #5099](https://github.com/ai4curation/ai-gene-review/pull/5099) | [`95e4139036f8`](https://github.com/ai4curation/ai-gene-review/commit/95e4139036f8f97dd82ca64fcc7eced437f36836) / [`3df2def4d26b`](https://github.com/ai4curation/ai-gene-review/commit/3df2def4d26ba94be2bb841bfdac847ccf0a7257) | [approval](https://github.com/ai4curation/ai-gene-review/pull/5099#pullrequestreview-5558004769) / [detail](https://github.com/ai4curation/ai-gene-review/pull/5099#issuecomment-6234523529) | 9 | [39183674278](https://github.com/ai4curation/ai-gene-review/actions/runs/39183674278) cancelled / [39183674220](https://github.com/ai4curation/ai-gene-review/actions/runs/39183674220) cancelled | [39182177176](https://github.com/ai4curation/ai-gene-review/actions/runs/39182177176) success |
| [DHODH #5100](https://github.com/ai4curation/ai-gene-review/pull/5100) | [`244b6c627a7f`](https://github.com/ai4curation/ai-gene-review/commit/244b6c627a7fba91c6b7ddfbfb3bda0b2b0bb422) / [`02ba969a6693`](https://github.com/ai4curation/ai-gene-review/commit/02ba969a6693acb3e327cc9c7f8c3ce67a7e43ed) | [approval](https://github.com/ai4curation/ai-gene-review/pull/5100#pullrequestreview-5558050890) / [detail](https://github.com/ai4curation/ai-gene-review/pull/5100#issuecomment-6234619294) | 12 | [39183674954](https://github.com/ai4curation/ai-gene-review/actions/runs/39183674954) success / [39183674944](https://github.com/ai4curation/ai-gene-review/actions/runs/39183674944) success | [39182178020](https://github.com/ai4curation/ai-gene-review/actions/runs/39182178020) success |
| [DHTKD1 #5101](https://github.com/ai4curation/ai-gene-review/pull/5101) | [`dbc5c226176e`](https://github.com/ai4curation/ai-gene-review/commit/dbc5c226176e999dcdaa83e26bb92100ee68369d) / [`41c0e159f6cb`](https://github.com/ai4curation/ai-gene-review/commit/41c0e159f6cbd5c0a67c3f56d7004d399c14a32d) | [approval](https://github.com/ai4curation/ai-gene-review/pull/5101#pullrequestreview-5558200635) / [detail](https://github.com/ai4curation/ai-gene-review/pull/5101#issuecomment-6234975384) | 20 | [39187058970](https://github.com/ai4curation/ai-gene-review/actions/runs/39187058970) cancelled / [39187058954](https://github.com/ai4curation/ai-gene-review/actions/runs/39187058954) cancelled | [39182180976](https://github.com/ai4curation/ai-gene-review/actions/runs/39182180976) success |
| [DHX30 #5104](https://github.com/ai4curation/ai-gene-review/pull/5104) | [`acb5a15c1f0e`](https://github.com/ai4curation/ai-gene-review/commit/acb5a15c1f0e49344517ba6426d98daecd7bfedf) / [`6e2c9512f547`](https://github.com/ai4curation/ai-gene-review/commit/6e2c9512f5470b3213e884a94e9de2e0971e6d6e) | [approval](https://github.com/ai4curation/ai-gene-review/pull/5104#pullrequestreview-5558688756) / [detail](https://github.com/ai4curation/ai-gene-review/pull/5104#issuecomment-6236356873) | 15 | [39187061624](https://github.com/ai4curation/ai-gene-review/actions/runs/39187061624) cancelled / [39187061641](https://github.com/ai4curation/ai-gene-review/actions/runs/39187061641) cancelled | [39183560931](https://github.com/ai4curation/ai-gene-review/actions/runs/39183560931) success |
| [DIAPH3 #5107](https://github.com/ai4curation/ai-gene-review/pull/5107) | [`624277d51efb`](https://github.com/ai4curation/ai-gene-review/commit/624277d51efbb0cfdbfc6ec9a69547243a327e77) / [`093159b74f94`](https://github.com/ai4curation/ai-gene-review/commit/093159b74f945e8aff403c922f3fc828388c03d2) | [approval](https://github.com/ai4curation/ai-gene-review/pull/5107#pullrequestreview-5558704630) / [detail](https://github.com/ai4curation/ai-gene-review/pull/5107#issuecomment-6236358086) | 29 | [39187083163](https://github.com/ai4curation/ai-gene-review/actions/runs/39187083163) cancelled / [39187083168](https://github.com/ai4curation/ai-gene-review/actions/runs/39187083168) cancelled | [39183628155](https://github.com/ai4curation/ai-gene-review/actions/runs/39183628155) success |
| [DIS3L2 #5112](https://github.com/ai4curation/ai-gene-review/pull/5112) | [`e589819b9cdb`](https://github.com/ai4curation/ai-gene-review/commit/e589819b9cdb9ca713adfe846cb33f0fd1e6f820) / [`3b05624a9f1e`](https://github.com/ai4curation/ai-gene-review/commit/3b05624a9f1e5d3dcd2538feea179e34c0152a4b) | [approval](https://github.com/ai4curation/ai-gene-review/pull/5112#pullrequestreview-5558774436) / [detail](https://github.com/ai4curation/ai-gene-review/pull/5112#issuecomment-6236579467) | 16 | [39187084244](https://github.com/ai4curation/ai-gene-review/actions/runs/39187084244) cancelled / [39187084239](https://github.com/ai4curation/ai-gene-review/actions/runs/39187084239) cancelled | [39183629782](https://github.com/ai4curation/ai-gene-review/actions/runs/39183629782) success |
| [DICER1 #5111](https://github.com/ai4curation/ai-gene-review/pull/5111) | [`398a29f56c91`](https://github.com/ai4curation/ai-gene-review/commit/398a29f56c917f2d7561f8dc1a15a09c24f21216) / [`9b42a011248d`](https://github.com/ai4curation/ai-gene-review/commit/9b42a011248d0f68f0104504639dc6445c00008a) | [approval](https://github.com/ai4curation/ai-gene-review/pull/5111#pullrequestreview-5558808807) / [detail](https://github.com/ai4curation/ai-gene-review/pull/5111#issuecomment-6236636197) | 39 | [39187085727](https://github.com/ai4curation/ai-gene-review/actions/runs/39187085727) cancelled / [39187085740](https://github.com/ai4curation/ai-gene-review/actions/runs/39187085740) cancelled | [39183677788](https://github.com/ai4curation/ai-gene-review/actions/runs/39183677788) success |
| [DISP1 #5113](https://github.com/ai4curation/ai-gene-review/pull/5113) | [`2560fb0489f4`](https://github.com/ai4curation/ai-gene-review/commit/2560fb0489f459c740ae180d8a4239cfcf5bd4e0) / [`bd4061b01e12`](https://github.com/ai4curation/ai-gene-review/commit/bd4061b01e128bb9265e8f06f19b92ff1bf345b9) | [approval](https://github.com/ai4curation/ai-gene-review/pull/5113#pullrequestreview-5558866652) / [detail](https://github.com/ai4curation/ai-gene-review/pull/5113#issuecomment-6236917853) | 18 | [39187106249](https://github.com/ai4curation/ai-gene-review/actions/runs/39187106249) cancelled / [39187106248](https://github.com/ai4curation/ai-gene-review/actions/runs/39187106248) cancelled | [39184686456](https://github.com/ai4curation/ai-gene-review/actions/runs/39184686456) success |
| [DIAPH1 #5106](https://github.com/ai4curation/ai-gene-review/pull/5106) | [`b2cc6c0f777a`](https://github.com/ai4curation/ai-gene-review/commit/b2cc6c0f777a34fec33592dcde3672c3508edaf1) / [`6155bb365387`](https://github.com/ai4curation/ai-gene-review/commit/6155bb3653871f5397fec9cc103b4b8a3dad352c) | [approval](https://github.com/ai4curation/ai-gene-review/pull/5106#pullrequestreview-5558936828) / [detail](https://github.com/ai4curation/ai-gene-review/pull/5106#issuecomment-6237111789) | 31 | [39187107447](https://github.com/ai4curation/ai-gene-review/actions/runs/39187107447) cancelled / [39187107461](https://github.com/ai4curation/ai-gene-review/actions/runs/39187107461) cancelled | [39184893342](https://github.com/ai4curation/ai-gene-review/actions/runs/39184893342) success |
| [DIABLO #5105](https://github.com/ai4curation/ai-gene-review/pull/5105) | [`54140f8251fe`](https://github.com/ai4curation/ai-gene-review/commit/54140f8251fe587084b98492b95a0bc8f1070ad7) / [`894e016ddd0f`](https://github.com/ai4curation/ai-gene-review/commit/894e016ddd0f9cb3da7644891970dacd3b8e1168) | [approval](https://github.com/ai4curation/ai-gene-review/pull/5105#pullrequestreview-5559024229) / [detail](https://github.com/ai4curation/ai-gene-review/pull/5105#issuecomment-6237325377) | 10 | [39187108123](https://github.com/ai4curation/ai-gene-review/actions/runs/39187108123) cancelled / [39187108065](https://github.com/ai4curation/ai-gene-review/actions/runs/39187108065) cancelled | [39185053319](https://github.com/ai4curation/ai-gene-review/actions/runs/39185053319) success |
| [DKC1 #5116](https://github.com/ai4curation/ai-gene-review/pull/5116) | [`e3607a505307`](https://github.com/ai4curation/ai-gene-review/commit/e3607a5053074cbe8f63438630135620f5ab51c2) / [`57fb4720a939`](https://github.com/ai4curation/ai-gene-review/commit/57fb4720a9395797a5752c90a89a366d4ee69b1a) | [approval](https://github.com/ai4curation/ai-gene-review/pull/5116#pullrequestreview-5559098133) / [detail](https://github.com/ai4curation/ai-gene-review/pull/5116#issuecomment-6237584282) | 31 | [39187610495](https://github.com/ai4curation/ai-gene-review/actions/runs/39187610495) cancelled / [39187610587](https://github.com/ai4curation/ai-gene-review/actions/runs/39187610587) success | [39186097967](https://github.com/ai4curation/ai-gene-review/actions/runs/39186097967) success |
| [DLG3 #5115](https://github.com/ai4curation/ai-gene-review/pull/5115) | [`c2c50812909a`](https://github.com/ai4curation/ai-gene-review/commit/c2c50812909a0c47238671841e2b7a2fcd98aba7) / [`1ed4061082c2`](https://github.com/ai4curation/ai-gene-review/commit/1ed4061082c2b361f9da06d23a492cbdc235b439) | [approval](https://github.com/ai4curation/ai-gene-review/pull/5115#pullrequestreview-5559266634) / [detail](https://github.com/ai4curation/ai-gene-review/pull/5115#issuecomment-6238228841) | 28 | [39187653317](https://github.com/ai4curation/ai-gene-review/actions/runs/39187653317) cancelled / [39187653845](https://github.com/ai4curation/ai-gene-review/actions/runs/39187653845) success | [39186302052](https://github.com/ai4curation/ai-gene-review/actions/runs/39186302052) success |
| [DLD #5126](https://github.com/ai4curation/ai-gene-review/pull/5126) | [`4033131ca553`](https://github.com/ai4curation/ai-gene-review/commit/4033131ca5532631b41a1b7b692b28133cafc8aa) / [`bf0db45a4fe2`](https://github.com/ai4curation/ai-gene-review/commit/bf0db45a4fe26275fdf708410771b75b1f721a83) | [approval](https://github.com/ai4curation/ai-gene-review/pull/5126#pullrequestreview-5559305300) / [detail](https://github.com/ai4curation/ai-gene-review/pull/5126#issuecomment-6238414131) | 19 | [39187910583](https://github.com/ai4curation/ai-gene-review/actions/runs/39187910583) cancelled / [39187910613](https://github.com/ai4curation/ai-gene-review/actions/runs/39187910613) cancelled | [39186483421](https://github.com/ai4curation/ai-gene-review/actions/runs/39186483421) success |

All 465 approved PR path occurrences match their merge blobs and modes. The
saved audits also verify that paths outside each PR delta are unchanged relative
to its immediate parent. All selected paths still match main `0ad352a6266763efcd3daaaa2a32a0755d5b54cd`;
a captured chain of commit objects proves containment of every merge. Shared
publication paths may occur in more than one audit, so this sum is not a count of
unique files. Optional review suggestions are preserved in the audits; no current
mandatory request or unresolved review thread was accepted as completed.

DDX41 and five genes in the first batch have successful immediate main test runs.
For DGUOK, DHCR24, DHDDS, DHCR7 and DHTKD1, and all ten genes in the second batch,
the immediate main test was cancelled. DHX30 and DLG3 also have failed aggregate
gates caused by cancellation. These outcomes remain recorded as cancellations or
failures, not successful main gene validation. Each exact merge commit separately
passed its merge-group checks. Successful descendants support the finite bridge:
DGUOK, DHCR24, DHDDS and DHCR7 retain their approved payloads and executable runtime
at [`02ba969a6693`](https://github.com/ai4curation/ai-gene-review/commit/02ba969a6693acb3e327cc9c7f8c3ce67a7e43ed),
with [test 39183674954](https://github.com/ai4curation/ai-gene-review/actions/runs/39183674954) and
[docs 39183674944](https://github.com/ai4curation/ai-gene-review/actions/runs/39183674944). DHTKD1 and the second batch retain
their payloads at [`bb50821d7123`](https://github.com/ai4curation/ai-gene-review/commit/bb50821d71232c86e36c9dee6ed1d0604f6b5505),
with [test 39200674021](https://github.com/ai4curation/ai-gene-review/actions/runs/39200674021) and
[docs 39200673967](https://github.com/ai4curation/ai-gene-review/actions/runs/39200673967). Its only relevant runtime differences
are documented additive GO-cache rows, affecting no reviewed term of those genes.
A descendant job's scoped gene validation covers its own changed paths; it is not
claimed to rerun validation for every earlier gene. The original approved-head and
exact merge-group validations provide that earlier gene-specific evidence.

Documentation success means the recorded MkDocs/schema build and deployment;
it does not establish regeneration or visual inspection of every gene HTML page.
The original audits retain event-specific skipped steps, warning annotations,
review-service limitations and optional suggestions. No ordinary suite, source
research or workflow rerun was performed to prepare this tracker update.

The current main snapshot contains 8,467 review files, including 3,102 human
reviews; 1,248 catalogue genes have reviews, 1,628 lack them, and
775 available catalogue reviews remain uncredited. This inventory includes
other existing reviews without awarding them completion credit. All 2,876 catalogue
identities and association texts, 235 historical queue objects, 101 earlier
completion updates and prior progress bytes are preserved. Update 102 appends the
three accepted audit stages and exact per-gene evidence. No gene, publication,
runtime or history file is modified.

The publication preimage is checkpoint 443, merged through
[#5053](https://github.com/ai4curation/ai-gene-review/pull/5053) at
[`7873440186c6`](https://github.com/ai4curation/ai-gene-review/commit/7873440186c62052a1cb7e255b2882a82484c273)
on 2026-10-19 at 04:13:34 UTC. Its six tracker files still match this captured main.
Accepted private checkpoints 444–452 are retained in full before this addition.
The current runtime includes dependency update [#4972](https://github.com/ai4curation/ai-gene-review/pull/4972);
publication uses the publisher's current-runtime checks, two ordinary project
renders and a new append-only history record. The publication checkout at
`a17627810d4a13efede28a3c07a481aa0b44131b` contains 8,472 review files, including
3,102 human reviews. All eight frontmatter checks and both renders passed;
the catalogue reports 1,628 missing-review warnings and the progress page reports none.
The inventory above remains the explicitly pinned audit snapshot.

[Curation session](https://github.com/ai4curation/ai-gene-review/blob/cmungall/clingen-tracker473-20261021/history/projects/CLINGEN_MENDELIAN/2026-10-21T004045Z-codex-b8ec9c.yaml)

## Completion checkpoint 541 — 2026-10-21 00:53:59 UTC

**541 complete; 2,335 remaining out of 2,876 primary catalogue genes.**
This appends exactly 68 accepted distinct genes from batches 03–09 to the published
473 checkpoint. The coordinating agent accepted the sealed merge audits; this is
not a human maintainer sign-off or a new biological review. EGR2, EHMT1 and EGFR
remain excluded. Existing source decisions, unresolved annotations and product
limits are unchanged.

| Gene / PR | Approved head / merge | Approval / detail | Exact PR paths | Immediate main test / docs | Exact merge-group test |
|---|---|---|---:|---|---|
| [DMD #5143](https://github.com/ai4curation/ai-gene-review/pull/5143) | [`4aefd77b3080`](https://github.com/ai4curation/ai-gene-review/commit/4aefd77b30801cc14aab2bf3f042790e39f2fb64) / [`d87957d33b6b`](https://github.com/ai4curation/ai-gene-review/commit/d87957d33b6be948d2dfb611ceb61f3cb25e8d80) | [approval](https://github.com/ai4curation/ai-gene-review/pull/5143#pullrequestreview-5560125374) / [detail](https://github.com/ai4curation/ai-gene-review/pull/5143#issuecomment-6241153024) | 93 | [39187911774](https://github.com/ai4curation/ai-gene-review/actions/runs/39187911774) cancelled / [39187911820](https://github.com/ai4curation/ai-gene-review/actions/runs/39187911820) cancelled | [39186523486](https://github.com/ai4curation/ai-gene-review/actions/runs/39186523486) success |
| [DMRT1 #5137](https://github.com/ai4curation/ai-gene-review/pull/5137) | [`039a1748dfd9`](https://github.com/ai4curation/ai-gene-review/commit/039a1748dfd905d76e7215196cd1a9010698cb8e) / [`bfd1a7762bd2`](https://github.com/ai4curation/ai-gene-review/commit/bfd1a7762bd2132ce7e2022e0b2c0b0989868284) | [approval](https://github.com/ai4curation/ai-gene-review/pull/5137#pullrequestreview-5560176227) / [detail](https://github.com/ai4curation/ai-gene-review/pull/5137#issuecomment-6241335801) | 23 | [39187961366](https://github.com/ai4curation/ai-gene-review/actions/runs/39187961366) cancelled / [39187961360](https://github.com/ai4curation/ai-gene-review/actions/runs/39187961360) cancelled | [39186566983](https://github.com/ai4curation/ai-gene-review/actions/runs/39186566983) success |
| [DNAJB6 #5159](https://github.com/ai4curation/ai-gene-review/pull/5159) | [`a6b6af6fe047`](https://github.com/ai4curation/ai-gene-review/commit/a6b6af6fe0475c82ef1a67870c3ec99f5a278369) / [`b39a1cb3f4e3`](https://github.com/ai4curation/ai-gene-review/commit/b39a1cb3f4e33814679ac2af999e7d5eac681b6f) | [approval](https://github.com/ai4curation/ai-gene-review/pull/5159#pullrequestreview-5560194426) / [detail](https://github.com/ai4curation/ai-gene-review/pull/5159#issuecomment-6241367207) | 9 | [39187962574](https://github.com/ai4curation/ai-gene-review/actions/runs/39187962574) cancelled / [39187962550](https://github.com/ai4curation/ai-gene-review/actions/runs/39187962550) success | [39186610942](https://github.com/ai4curation/ai-gene-review/actions/runs/39186610942) success |
| [DNAJC21 #5160](https://github.com/ai4curation/ai-gene-review/pull/5160) | [`8bfb849689de`](https://github.com/ai4curation/ai-gene-review/commit/8bfb849689de411947bcef3d0923286d35da9b73) / [`c8ec8c24406e`](https://github.com/ai4curation/ai-gene-review/commit/c8ec8c24406e0d21b91114d3f4d0c82365781b6f) | [approval](https://github.com/ai4curation/ai-gene-review/pull/5160#pullrequestreview-5560227287) / [detail](https://github.com/ai4curation/ai-gene-review/pull/5160#issuecomment-6241475723) | 10 | [39188517354](https://github.com/ai4curation/ai-gene-review/actions/runs/39188517354) cancelled / [39188517394](https://github.com/ai4curation/ai-gene-review/actions/runs/39188517394) success | [39187131353](https://github.com/ai4curation/ai-gene-review/actions/runs/39187131353) success |
| [DNAAF1 #5142](https://github.com/ai4curation/ai-gene-review/pull/5142) | [`48e448043ff3`](https://github.com/ai4curation/ai-gene-review/commit/48e448043ff340f7af3b3e2c45096df76dd9b414) / [`91b8d9960ee6`](https://github.com/ai4curation/ai-gene-review/commit/91b8d9960ee6792d452531db963712aa407adc1b) | [approval](https://github.com/ai4curation/ai-gene-review/pull/5142#pullrequestreview-5560284122) / [detail](https://github.com/ai4curation/ai-gene-review/pull/5142#issuecomment-6241784152) | 9 | [39188517758](https://github.com/ai4curation/ai-gene-review/actions/runs/39188517758) cancelled / [39188517713](https://github.com/ai4curation/ai-gene-review/actions/runs/39188517713) success | [39187168564](https://github.com/ai4curation/ai-gene-review/actions/runs/39187168564) success |
| [DLG4 #5141](https://github.com/ai4curation/ai-gene-review/pull/5141) | [`cfaa650ed3a9`](https://github.com/ai4curation/ai-gene-review/commit/cfaa650ed3a9478ef97a678a4e49eab61c2dc3fe) / [`3aedf3afbe24`](https://github.com/ai4curation/ai-gene-review/commit/3aedf3afbe24ac09d9837c41a61f76edd0ff501d) | [approval](https://github.com/ai4curation/ai-gene-review/pull/5141#pullrequestreview-5560310684) / [detail](https://github.com/ai4curation/ai-gene-review/pull/5141#issuecomment-6241886528) | 65 | [39188940630](https://github.com/ai4curation/ai-gene-review/actions/runs/39188940630) cancelled / [39188940588](https://github.com/ai4curation/ai-gene-review/actions/runs/39188940588) cancelled | [39187507583](https://github.com/ai4curation/ai-gene-review/actions/runs/39187507583) success |
| [DNAAF19 #5145](https://github.com/ai4curation/ai-gene-review/pull/5145) | [`144f1e87eb82`](https://github.com/ai4curation/ai-gene-review/commit/144f1e87eb824f7625e5db35633eed329f011502) / [`d0d98a87fe34`](https://github.com/ai4curation/ai-gene-review/commit/d0d98a87fe34b148a2cc339c71eeef63736a64a9) | [approval](https://github.com/ai4curation/ai-gene-review/pull/5145#pullrequestreview-5560292265) / [detail](https://github.com/ai4curation/ai-gene-review/pull/5145#issuecomment-6241835833) | 14 | [39189048360](https://github.com/ai4curation/ai-gene-review/actions/runs/39189048360) cancelled / [39189048306](https://github.com/ai4curation/ai-gene-review/actions/runs/39189048306) cancelled | [39187612323](https://github.com/ai4curation/ai-gene-review/actions/runs/39187612323) success |
| [DNAAF5 #5150](https://github.com/ai4curation/ai-gene-review/pull/5150) | [`4356434a016b`](https://github.com/ai4curation/ai-gene-review/commit/4356434a016b243a87761ca94ed5c02384be36d3) / [`ef281598e742`](https://github.com/ai4curation/ai-gene-review/commit/ef281598e74241228b64c0dc3fb52ec339dcdd66) | [approval](https://github.com/ai4curation/ai-gene-review/pull/5150#pullrequestreview-5560266964) / [detail](https://github.com/ai4curation/ai-gene-review/pull/5150#issuecomment-6241698555) | 14 | [39189049668](https://github.com/ai4curation/ai-gene-review/actions/runs/39189049668) cancelled / [39189049667](https://github.com/ai4curation/ai-gene-review/actions/runs/39189049667) success | [39187655939](https://github.com/ai4curation/ai-gene-review/actions/runs/39187655939) success |
| [DNAJC30 #5161](https://github.com/ai4curation/ai-gene-review/pull/5161) | [`2152e7a87a89`](https://github.com/ai4curation/ai-gene-review/commit/2152e7a87a89e4146a2d006e58aef05a4ec8332e) / [`69b742f2ee16`](https://github.com/ai4curation/ai-gene-review/commit/69b742f2ee165f2fbe404560ce73303aca328f6f) | [approval](https://github.com/ai4curation/ai-gene-review/pull/5161#pullrequestreview-5560289804) / [detail](https://github.com/ai4curation/ai-gene-review/pull/5161#issuecomment-6241816900) | 9 | [39189233128](https://github.com/ai4curation/ai-gene-review/actions/runs/39189233128) cancelled / [39189233126](https://github.com/ai4curation/ai-gene-review/actions/runs/39189233126) cancelled | [39187768552](https://github.com/ai4curation/ai-gene-review/actions/runs/39187768552) success |
| [DNAAF11 #5146](https://github.com/ai4curation/ai-gene-review/pull/5146) | [`4117de879ccf`](https://github.com/ai4curation/ai-gene-review/commit/4117de879ccf5e8778b06c97d5816e450a051b0d) / [`aa1885d8bb10`](https://github.com/ai4curation/ai-gene-review/commit/aa1885d8bb102d8ce249072b11e0ecb2eb4fd319) | [approval](https://github.com/ai4curation/ai-gene-review/pull/5146#pullrequestreview-5560364100) / [detail](https://github.com/ai4curation/ai-gene-review/pull/5146#issuecomment-6242060792) | 18 | [39189234291](https://github.com/ai4curation/ai-gene-review/actions/runs/39189234291) cancelled / [39189234305](https://github.com/ai4curation/ai-gene-review/actions/runs/39189234305) success | [39187914173](https://github.com/ai4curation/ai-gene-review/actions/runs/39187914173) success |
| [DNAL1 #5162](https://github.com/ai4curation/ai-gene-review/pull/5162) | [`db557d9516b0`](https://github.com/ai4curation/ai-gene-review/commit/db557d9516b06942e87d65db9c3f2a0f9d9f1f07) / [`002583730642`](https://github.com/ai4curation/ai-gene-review/commit/002583730642ea1fcb225dbdf54b37d6d55a17b6) | [approval](https://github.com/ai4curation/ai-gene-review/pull/5162#pullrequestreview-5560337325) / [detail](https://github.com/ai4curation/ai-gene-review/pull/5162#issuecomment-6241988575) | 10 | [39189632983](https://github.com/ai4curation/ai-gene-review/actions/runs/39189632983) cancelled / [39189633015](https://github.com/ai4curation/ai-gene-review/actions/runs/39189633015) success | [39187965245](https://github.com/ai4curation/ai-gene-review/actions/runs/39187965245) success |
| [DNAJB2 #5158](https://github.com/ai4curation/ai-gene-review/pull/5158) | [`4274e9cc4f6f`](https://github.com/ai4curation/ai-gene-review/commit/4274e9cc4f6f75308911aff82636cbd522477bb5) / [`cf96752efc52`](https://github.com/ai4curation/ai-gene-review/commit/cf96752efc524f028ef0208e93b13ca2c5228d4d) | [approval](https://github.com/ai4curation/ai-gene-review/pull/5158#pullrequestreview-5560372249) / [detail](https://github.com/ai4curation/ai-gene-review/pull/5158#issuecomment-6242097183) | 13 | [39189743504](https://github.com/ai4curation/ai-gene-review/actions/runs/39189743504) cancelled / [39189743506](https://github.com/ai4curation/ai-gene-review/actions/runs/39189743506) success | [39188201729](https://github.com/ai4curation/ai-gene-review/actions/runs/39188201729) success |
| [DNAJC19 #5157](https://github.com/ai4curation/ai-gene-review/pull/5157) | [`628c6d0a23fd`](https://github.com/ai4curation/ai-gene-review/commit/628c6d0a23fd323ed52dd6b54bb3073d28e67afa) / [`af2d3d44164a`](https://github.com/ai4curation/ai-gene-review/commit/af2d3d44164aa625683cbc1bdd4cb9c45b9807de) | [approval](https://github.com/ai4curation/ai-gene-review/pull/5157#pullrequestreview-5560377859) / [detail](https://github.com/ai4curation/ai-gene-review/pull/5157#issuecomment-6242128278) | 11 | [39190257375](https://github.com/ai4curation/ai-gene-review/actions/runs/39190257375) cancelled / [39190257374](https://github.com/ai4curation/ai-gene-review/actions/runs/39190257374) success | [39188519926](https://github.com/ai4curation/ai-gene-review/actions/runs/39188519926) success |
| [DNAH8 #5152](https://github.com/ai4curation/ai-gene-review/pull/5152) | [`2eca53bbcb0a`](https://github.com/ai4curation/ai-gene-review/commit/2eca53bbcb0a9ed5f991dc8a872b48278b1a47de) / [`8035864699cb`](https://github.com/ai4curation/ai-gene-review/commit/8035864699cb5472923445bb7f40fa2a91111185) | [approval](https://github.com/ai4curation/ai-gene-review/pull/5152#pullrequestreview-5560428047) / [detail](https://github.com/ai4curation/ai-gene-review/pull/5152#issuecomment-6242311233) | 5 | [39190404930](https://github.com/ai4curation/ai-gene-review/actions/runs/39190404930) cancelled / [39190405014](https://github.com/ai4curation/ai-gene-review/actions/runs/39190405014) cancelled | [39188894055](https://github.com/ai4curation/ai-gene-review/actions/runs/39188894055) success |
| [DNAI1 #5155](https://github.com/ai4curation/ai-gene-review/pull/5155) | [`c823aef039b3`](https://github.com/ai4curation/ai-gene-review/commit/c823aef039b31ab4304aed87e2c4b859a64b8676) / [`310c7ae87d11`](https://github.com/ai4curation/ai-gene-review/commit/310c7ae87d11066c2a99a59aa8f00dc0e1cb34f0) | [approval](https://github.com/ai4curation/ai-gene-review/pull/5155#pullrequestreview-5560441782) / [detail](https://github.com/ai4curation/ai-gene-review/pull/5155#issuecomment-6242360608) | 17 | [39190405751](https://github.com/ai4curation/ai-gene-review/actions/runs/39190405751) cancelled / [39190405824](https://github.com/ai4curation/ai-gene-review/actions/runs/39190405824) cancelled | [39188942834](https://github.com/ai4curation/ai-gene-review/actions/runs/39188942834) success |
| [DNAI2 #5156](https://github.com/ai4curation/ai-gene-review/pull/5156) | [`fc0c50b25008`](https://github.com/ai4curation/ai-gene-review/commit/fc0c50b250086de1ff6aab6a13a52c5d702b3a89) / [`7bd7d235ed1a`](https://github.com/ai4curation/ai-gene-review/commit/7bd7d235ed1ac8096a90be314c0a67ae6d4edb6c) | [approval](https://github.com/ai4curation/ai-gene-review/pull/5156#pullrequestreview-5560453958) / [detail](https://github.com/ai4curation/ai-gene-review/pull/5156#issuecomment-6242410910) | 27 | [39190449220](https://github.com/ai4curation/ai-gene-review/actions/runs/39190449220) cancelled / [39190449173](https://github.com/ai4curation/ai-gene-review/actions/runs/39190449173) cancelled | [39189051611](https://github.com/ai4curation/ai-gene-review/actions/runs/39189051611) success |
| [DNAAF3 #5148](https://github.com/ai4curation/ai-gene-review/pull/5148) | [`57422dc7a00d`](https://github.com/ai4curation/ai-gene-review/commit/57422dc7a00d0a46c260deb6228e0821ec78c1c2) / [`2e5ae6740fe6`](https://github.com/ai4curation/ai-gene-review/commit/2e5ae6740fe600706b87eebebbba6efecb5adf60) | [approval](https://github.com/ai4curation/ai-gene-review/pull/5148#pullrequestreview-5560471345) / [detail](https://github.com/ai4curation/ai-gene-review/pull/5148#issuecomment-6242453461) | 15 | [39190449878](https://github.com/ai4curation/ai-gene-review/actions/runs/39190449878) cancelled / [39190449905](https://github.com/ai4curation/ai-gene-review/actions/runs/39190449905) success | [39189052844](https://github.com/ai4curation/ai-gene-review/actions/runs/39189052844) success |
| [DNAAF4 #5149](https://github.com/ai4curation/ai-gene-review/pull/5149) | [`6d980bcdaf60`](https://github.com/ai4curation/ai-gene-review/commit/6d980bcdaf609249ed628039d03e994d4817ec64) / [`ed8061507edb`](https://github.com/ai4curation/ai-gene-review/commit/ed8061507edb3036108cf9c30c5d9529739144ec) | [approval](https://github.com/ai4curation/ai-gene-review/pull/5149#pullrequestreview-5560548684) / [detail](https://github.com/ai4curation/ai-gene-review/pull/5149#issuecomment-6242809075) | 18 | [39190699924](https://github.com/ai4curation/ai-gene-review/actions/runs/39190699924) cancelled / [39190700045](https://github.com/ai4curation/ai-gene-review/actions/runs/39190700045) success | [39189236702](https://github.com/ai4curation/ai-gene-review/actions/runs/39189236702) success |
| [DNAAF2 #5147](https://github.com/ai4curation/ai-gene-review/pull/5147) | [`d0374e4a65f6`](https://github.com/ai4curation/ai-gene-review/commit/d0374e4a65f614f2ac172b81d655d0674f754171) / [`c4d984a59437`](https://github.com/ai4curation/ai-gene-review/commit/c4d984a59437531255d63e73de22521334b17a12) | [approval](https://github.com/ai4curation/ai-gene-review/pull/5147#pullrequestreview-5560570961) / [detail](https://github.com/ai4curation/ai-gene-review/pull/5147#issuecomment-6242886312) | 20 | [39191111520](https://github.com/ai4curation/ai-gene-review/actions/runs/39191111520) cancelled / [39191111317](https://github.com/ai4curation/ai-gene-review/actions/runs/39191111317) success | [39189634754](https://github.com/ai4curation/ai-gene-review/actions/runs/39189634754) success |
| [DNAAF6 #5151](https://github.com/ai4curation/ai-gene-review/pull/5151) | [`441ccd42b8d9`](https://github.com/ai4curation/ai-gene-review/commit/441ccd42b8d97d3972aa95a4ae47024216f49bf9) / [`2a58063332e6`](https://github.com/ai4curation/ai-gene-review/commit/2a58063332e64b82d0e33812d3e8d07ce5f4c1bd) | [approval](https://github.com/ai4curation/ai-gene-review/pull/5151#pullrequestreview-5560606904) / [detail](https://github.com/ai4curation/ai-gene-review/pull/5151#issuecomment-6243008839) | 24 | [39191112043](https://github.com/ai4curation/ai-gene-review/actions/runs/39191112043) cancelled / [39191112553](https://github.com/ai4curation/ai-gene-review/actions/runs/39191112553) success | [39189745266](https://github.com/ai4curation/ai-gene-review/actions/runs/39189745266) success |
| [DOCK11 #5171](https://github.com/ai4curation/ai-gene-review/pull/5171) | [`c015258574f8`](https://github.com/ai4curation/ai-gene-review/commit/c015258574f81d05cfe5cf85d2ff06b2e3cddca0) / [`e7adbec2048f`](https://github.com/ai4curation/ai-gene-review/commit/e7adbec2048f0c753b6efa076fa97db71d1385a5) | [approval](https://github.com/ai4curation/ai-gene-review/pull/5171#pullrequestreview-5561006604) / [detail](https://github.com/ai4curation/ai-gene-review/pull/5171#issuecomment-6244402496) | 27 | [39191657344](https://github.com/ai4curation/ai-gene-review/actions/runs/39191657344) cancelled / [39191657475](https://github.com/ai4curation/ai-gene-review/actions/runs/39191657475) success | [39190260091](https://github.com/ai4curation/ai-gene-review/actions/runs/39190260091) success |
| [DNMT3A #5170](https://github.com/ai4curation/ai-gene-review/pull/5170) | [`bfb486a5fc25`](https://github.com/ai4curation/ai-gene-review/commit/bfb486a5fc2573711353c7c1a5519c26343ebd27) / [`29efd5e1e346`](https://github.com/ai4curation/ai-gene-review/commit/29efd5e1e34684328f64e886425b557e7ca8e40d) | [approval](https://github.com/ai4curation/ai-gene-review/pull/5170#pullrequestreview-5561022491) / [detail](https://github.com/ai4curation/ai-gene-review/pull/5170#issuecomment-6244452967) | 28 | [39191833685](https://github.com/ai4curation/ai-gene-review/actions/runs/39191833685) cancelled / [39191833696](https://github.com/ai4curation/ai-gene-review/actions/runs/39191833696) cancelled | [39190309258](https://github.com/ai4curation/ai-gene-review/actions/runs/39190309258) success |
| [DNMT1 #5167](https://github.com/ai4curation/ai-gene-review/pull/5167) | [`822362e01633`](https://github.com/ai4curation/ai-gene-review/commit/822362e01633d73d93ca46d16600d363b93cfe0e) / [`9a1b5a39a111`](https://github.com/ai4curation/ai-gene-review/commit/9a1b5a39a1110336ec5319cc38190679231eb0a4) | [approval](https://github.com/ai4curation/ai-gene-review/pull/5167#pullrequestreview-5561060128) / [detail](https://github.com/ai4curation/ai-gene-review/pull/5167#issuecomment-6244539919) | 20 | [39191835649](https://github.com/ai4curation/ai-gene-review/actions/runs/39191835649) cancelled / [39191835674](https://github.com/ai4curation/ai-gene-review/actions/runs/39191835674) success | [39190409062](https://github.com/ai4curation/ai-gene-review/actions/runs/39190409062) success |
| [DNMT3B #5169](https://github.com/ai4curation/ai-gene-review/pull/5169) | [`09e528221f4b`](https://github.com/ai4curation/ai-gene-review/commit/09e528221f4ba8259e1b170cf7618c1d84d9d1e0) / [`26236c3c82d6`](https://github.com/ai4curation/ai-gene-review/commit/26236c3c82d6e193d0c1881a05753aaed8083409) | [approval](https://github.com/ai4curation/ai-gene-review/pull/5169#pullrequestreview-5561042871) / [detail](https://github.com/ai4curation/ai-gene-review/pull/5169#issuecomment-6244497906) | 22 | [39191834266](https://github.com/ai4curation/ai-gene-review/actions/runs/39191834266) cancelled / [39191834319](https://github.com/ai4curation/ai-gene-review/actions/runs/39191834319) cancelled | [39190407682](https://github.com/ai4curation/ai-gene-review/actions/runs/39190407682) success |
| [DNM1L #5166](https://github.com/ai4curation/ai-gene-review/pull/5166) | [`ad720c8913ed`](https://github.com/ai4curation/ai-gene-review/commit/ad720c8913ed74798a9f5616c795340658175a8f) / [`e902e7ed5bfb`](https://github.com/ai4curation/ai-gene-review/commit/e902e7ed5bfbe7b75b101e0ca084ef561e1a1f96) | [approval](https://github.com/ai4curation/ai-gene-review/pull/5166#pullrequestreview-5561071033) / [detail](https://github.com/ai4curation/ai-gene-review/pull/5166#issuecomment-6244563709) | 13 | [39191971333](https://github.com/ai4curation/ai-gene-review/actions/runs/39191971333) cancelled / [39191971311](https://github.com/ai4curation/ai-gene-review/actions/runs/39191971311) cancelled | [39190451175](https://github.com/ai4curation/ai-gene-review/actions/runs/39190451175) success |
| [DOCK6 #5174](https://github.com/ai4curation/ai-gene-review/pull/5174) | [`eaa59b3d397d`](https://github.com/ai4curation/ai-gene-review/commit/eaa59b3d397dceebfed519411f8c7d273b30a4b0) / [`afdc59380483`](https://github.com/ai4curation/ai-gene-review/commit/afdc5938048354da746ae2646c73fab2282c0a13) | [approval](https://github.com/ai4curation/ai-gene-review/pull/5174#pullrequestreview-5561082621) / [detail](https://github.com/ai4curation/ai-gene-review/pull/5174#issuecomment-6244619341) | 14 | [39192127336](https://github.com/ai4curation/ai-gene-review/actions/runs/39192127336) cancelled / [39192127466](https://github.com/ai4curation/ai-gene-review/actions/runs/39192127466) success | [39190701958](https://github.com/ai4curation/ai-gene-review/actions/runs/39190701958) success |
| [DNM2 #5168](https://github.com/ai4curation/ai-gene-review/pull/5168) | [`09e9a65cdec6`](https://github.com/ai4curation/ai-gene-review/commit/09e9a65cdec6bfec9f9f3b3e8e684a5957eb1ea6) / [`c9dd834fefc5`](https://github.com/ai4curation/ai-gene-review/commit/c9dd834fefc58b135f458d1ddec409d0f80cbfd3) | [approval](https://github.com/ai4curation/ai-gene-review/pull/5168#pullrequestreview-5561095269) / [detail](https://github.com/ai4curation/ai-gene-review/pull/5168#issuecomment-6244646991) | 41 | [39192497984](https://github.com/ai4curation/ai-gene-review/actions/runs/39192497984) cancelled / [39192498061](https://github.com/ai4curation/ai-gene-review/actions/runs/39192498061) success | [39191114254](https://github.com/ai4curation/ai-gene-review/actions/runs/39191114254) success |
| [DOCK2 #5175](https://github.com/ai4curation/ai-gene-review/pull/5175) | [`e0ef2857f3a3`](https://github.com/ai4curation/ai-gene-review/commit/e0ef2857f3a3dd2eadb78f0475f38c3a7f0ea9e3) / [`0372a9c59eb2`](https://github.com/ai4curation/ai-gene-review/commit/0372a9c59eb2d501b46dfa5c438d89eeaf4ab1f7) | [approval](https://github.com/ai4curation/ai-gene-review/pull/5175#pullrequestreview-5561111627) / [detail](https://github.com/ai4curation/ai-gene-review/pull/5175#issuecomment-6244698085) | 24 | [39192499221](https://github.com/ai4curation/ai-gene-review/actions/runs/39192499221) cancelled / [39192499143](https://github.com/ai4curation/ai-gene-review/actions/runs/39192499143) success | [39191115546](https://github.com/ai4curation/ai-gene-review/actions/runs/39191115546) success |
| [DOCK7 #5176](https://github.com/ai4curation/ai-gene-review/pull/5176) | [`75d22cf922bc`](https://github.com/ai4curation/ai-gene-review/commit/75d22cf922bca48fd1925c2bf460f74347627427) / [`1ddc38b26cc3`](https://github.com/ai4curation/ai-gene-review/commit/1ddc38b26cc37326d2058c5413bd69d34af825e3) | [approval](https://github.com/ai4curation/ai-gene-review/pull/5176#pullrequestreview-5561141102) / [detail](https://github.com/ai4curation/ai-gene-review/pull/5176#issuecomment-6244785065) | 38 | [39193043623](https://github.com/ai4curation/ai-gene-review/actions/runs/39193043623) cancelled / [39193043621](https://github.com/ai4curation/ai-gene-review/actions/runs/39193043621) success | [39191658870](https://github.com/ai4curation/ai-gene-review/actions/runs/39191658870) success |
| [DOK7 #5177](https://github.com/ai4curation/ai-gene-review/pull/5177) | [`b6399867d721`](https://github.com/ai4curation/ai-gene-review/commit/b6399867d72139d431343335e907bb8d2ca47530) / [`d1c971ac8733`](https://github.com/ai4curation/ai-gene-review/commit/d1c971ac8733acaa24c8b02bb464454e05895617) | [approval](https://github.com/ai4curation/ai-gene-review/pull/5177#pullrequestreview-5561268305) / [detail](https://github.com/ai4curation/ai-gene-review/pull/5177#issuecomment-6245157259) | 18 | [39193157984](https://github.com/ai4curation/ai-gene-review/actions/runs/39193157984) cancelled / [39193158011](https://github.com/ai4curation/ai-gene-review/actions/runs/39193158011) cancelled | [39191660369](https://github.com/ai4curation/ai-gene-review/actions/runs/39191660369) success |
| [DOCK8 #5178](https://github.com/ai4curation/ai-gene-review/pull/5178) | [`beb3d6d0d283`](https://github.com/ai4curation/ai-gene-review/commit/beb3d6d0d28336a1d6c3df408ca00c1ae7ed019e) / [`a066dcf2b38d`](https://github.com/ai4curation/ai-gene-review/commit/a066dcf2b38dd92e7b4895d7af660182c7df53f9) | [approval](https://github.com/ai4curation/ai-gene-review/pull/5178#pullrequestreview-5561283477) / [detail](https://github.com/ai4curation/ai-gene-review/pull/5178#issuecomment-6245213069) | 31 | [39193158990](https://github.com/ai4curation/ai-gene-review/actions/runs/39193158990) cancelled / [39193158943](https://github.com/ai4curation/ai-gene-review/actions/runs/39193158943) cancelled | [39191837788](https://github.com/ai4curation/ai-gene-review/actions/runs/39191837788) success |
| [DOLK #5179](https://github.com/ai4curation/ai-gene-review/pull/5179) | [`b702277e430e`](https://github.com/ai4curation/ai-gene-review/commit/b702277e430e6b2b24323b4d52903f6a839aa9eb) / [`ee9a871cc585`](https://github.com/ai4curation/ai-gene-review/commit/ee9a871cc585eef81fb83534dfc7e06d425fd5e6) | [approval](https://github.com/ai4curation/ai-gene-review/pull/5179#pullrequestreview-5561320533) / [detail](https://github.com/ai4curation/ai-gene-review/pull/5179#issuecomment-6245328836) | 39 | [39193160109](https://github.com/ai4curation/ai-gene-review/actions/runs/39193160109) cancelled / [39193159955](https://github.com/ai4curation/ai-gene-review/actions/runs/39193159955) success | [39191838572](https://github.com/ai4curation/ai-gene-review/actions/runs/39191838572) success |
| [DPAGT1 #5180](https://github.com/ai4curation/ai-gene-review/pull/5180) | [`594f32073592`](https://github.com/ai4curation/ai-gene-review/commit/594f32073592adcb30f2c8fea6b409ecbd8407b5) / [`a7a19e059c4b`](https://github.com/ai4curation/ai-gene-review/commit/a7a19e059c4bd5680d5ef90c9d4e389d45051031) | [approval](https://github.com/ai4curation/ai-gene-review/pull/5180#pullrequestreview-5561418458) / [detail](https://github.com/ai4curation/ai-gene-review/pull/5180#issuecomment-6245598860) | 10 | [39193322914](https://github.com/ai4curation/ai-gene-review/actions/runs/39193322914) cancelled / [39193322917](https://github.com/ai4curation/ai-gene-review/actions/runs/39193322917) success | [39191973501](https://github.com/ai4curation/ai-gene-review/actions/runs/39191973501) success |
| [DPF2 #5181](https://github.com/ai4curation/ai-gene-review/pull/5181) | [`caff9ddfe06c`](https://github.com/ai4curation/ai-gene-review/commit/caff9ddfe06cefc7242c59e86b17673ae945a296) / [`21c22151b39e`](https://github.com/ai4curation/ai-gene-review/commit/21c22151b39ed7c4c775129b9a639b98aff22dc4) | [approval](https://github.com/ai4curation/ai-gene-review/pull/5181#pullrequestreview-5561491244) / [detail](https://github.com/ai4curation/ai-gene-review/pull/5181#issuecomment-6245797001) | 26 | [39193640339](https://github.com/ai4curation/ai-gene-review/actions/runs/39193640339) cancelled / [39193640407](https://github.com/ai4curation/ai-gene-review/actions/runs/39193640407) cancelled | [39192128880](https://github.com/ai4curation/ai-gene-review/actions/runs/39192128880) success |
| [DPY19L2 #5184](https://github.com/ai4curation/ai-gene-review/pull/5184) | [`34272ec51bcd`](https://github.com/ai4curation/ai-gene-review/commit/34272ec51bcd6703df20839b5f87d682fe5cc3ef) / [`40ac2eaa80d5`](https://github.com/ai4curation/ai-gene-review/commit/40ac2eaa80d54950df02821ecb2a41e204f4da91) | [approval](https://github.com/ai4curation/ai-gene-review/pull/5184#pullrequestreview-5561527829) / [detail](https://github.com/ai4curation/ai-gene-review/pull/5184#issuecomment-6245908477) | 18 | [39193778825](https://github.com/ai4curation/ai-gene-review/actions/runs/39193778825) cancelled / [39193778832](https://github.com/ai4curation/ai-gene-review/actions/runs/39193778832) success | [39192366441](https://github.com/ai4curation/ai-gene-review/actions/runs/39192366441) success |
| [DPH1 #5182](https://github.com/ai4curation/ai-gene-review/pull/5182) | [`4330af836f24`](https://github.com/ai4curation/ai-gene-review/commit/4330af836f247fa7c438f3bc9036cc4ded71d3e2) / [`a44f07ba473d`](https://github.com/ai4curation/ai-gene-review/commit/a44f07ba473d1cfd1e8c6eb940b1a6b227c4b37c) | [approval](https://github.com/ai4curation/ai-gene-review/pull/5182#pullrequestreview-5561532488) / [detail](https://github.com/ai4curation/ai-gene-review/pull/5182#issuecomment-6245934400) | 15 | [39194050778](https://github.com/ai4curation/ai-gene-review/actions/runs/39194050778) cancelled / [39194050729](https://github.com/ai4curation/ai-gene-review/actions/runs/39194050729) success | [39192501158](https://github.com/ai4curation/ai-gene-review/actions/runs/39192501158) success |
| [DPM1 #5183](https://github.com/ai4curation/ai-gene-review/pull/5183) | [`92402e4181d4`](https://github.com/ai4curation/ai-gene-review/commit/92402e4181d44ff22f1f9a38f8f111cb3be406bf) / [`4b38a493196d`](https://github.com/ai4curation/ai-gene-review/commit/4b38a493196da1564744dcd5491b83eab6c9ce29) | [approval](https://github.com/ai4curation/ai-gene-review/pull/5183#pullrequestreview-5561624440) / [detail](https://github.com/ai4curation/ai-gene-review/pull/5183#issuecomment-6246172677) | 23 | [39194608242](https://github.com/ai4curation/ai-gene-review/actions/runs/39194608242) cancelled / [39194608284](https://github.com/ai4curation/ai-gene-review/actions/runs/39194608284) cancelled | [39193070200](https://github.com/ai4curation/ai-gene-review/actions/runs/39193070200) success |
| [DRC1 #5186](https://github.com/ai4curation/ai-gene-review/pull/5186) | [`623841bd26d1`](https://github.com/ai4curation/ai-gene-review/commit/623841bd26d17eaf91c82aed2040f117568652cc) / [`9b5c8c67d999`](https://github.com/ai4curation/ai-gene-review/commit/9b5c8c67d9998489f3be74276da5b24323fe7613) | [approval](https://github.com/ai4curation/ai-gene-review/pull/5186#pullrequestreview-5561638314) / [detail](https://github.com/ai4curation/ai-gene-review/pull/5186#issuecomment-6246203719) | 12 | [39194653608](https://github.com/ai4curation/ai-gene-review/actions/runs/39194653608) cancelled / [39194653597](https://github.com/ai4curation/ai-gene-review/actions/runs/39194653597) cancelled | [39193111849](https://github.com/ai4curation/ai-gene-review/actions/runs/39193111849) success |
| [DRC2 #5187](https://github.com/ai4curation/ai-gene-review/pull/5187) | [`ef2c0153f4a6`](https://github.com/ai4curation/ai-gene-review/commit/ef2c0153f4a6fe110cb925368a5ab03f5213a59a) / [`023c6f73c5e9`](https://github.com/ai4curation/ai-gene-review/commit/023c6f73c5e902f9c00e1b57794f799b21ba6f9b) | [approval](https://github.com/ai4curation/ai-gene-review/pull/5187#pullrequestreview-5561726274) / [detail](https://github.com/ai4curation/ai-gene-review/pull/5187#issuecomment-6246436907) | 12 | [39194654994](https://github.com/ai4curation/ai-gene-review/actions/runs/39194654994) cancelled / [39194655058](https://github.com/ai4curation/ai-gene-review/actions/runs/39194655058) success | [39193162028](https://github.com/ai4curation/ai-gene-review/actions/runs/39193162028) success |
| [DRC4 #5188](https://github.com/ai4curation/ai-gene-review/pull/5188) | [`7ab4969cb43f`](https://github.com/ai4curation/ai-gene-review/commit/7ab4969cb43f3a0a8fe1a1ae34405f78d40c04d3) / [`d05e9f2348ac`](https://github.com/ai4curation/ai-gene-review/commit/d05e9f2348ac95df795c5f8031774ff1955e7d70) | [approval](https://github.com/ai4curation/ai-gene-review/pull/5188#pullrequestreview-5561932517) / [detail](https://github.com/ai4curation/ai-gene-review/pull/5188#issuecomment-6247052075) | 27 | [39194863186](https://github.com/ai4curation/ai-gene-review/actions/runs/39194863186) cancelled / [39194863196](https://github.com/ai4curation/ai-gene-review/actions/runs/39194863196) success | [39193325269](https://github.com/ai4curation/ai-gene-review/actions/runs/39193325269) success |
| [DSE #5190](https://github.com/ai4curation/ai-gene-review/pull/5190) | [`ab6b0fdca25f`](https://github.com/ai4curation/ai-gene-review/commit/ab6b0fdca25f9f86040c26fba95b3af993e49a15) / [`21eda734da77`](https://github.com/ai4curation/ai-gene-review/commit/21eda734da7725d2dc5fc503edd197eed802a874) | [approval](https://github.com/ai4curation/ai-gene-review/pull/5190#pullrequestreview-5561950328) / [detail](https://github.com/ai4curation/ai-gene-review/pull/5190#issuecomment-6247132283) | 15 | [39195171996](https://github.com/ai4curation/ai-gene-review/actions/runs/39195171996) cancelled / [39195171953](https://github.com/ai4curation/ai-gene-review/actions/runs/39195171953) success | [39193642108](https://github.com/ai4curation/ai-gene-review/actions/runs/39193642108) success |
| [DSC2 #5189](https://github.com/ai4curation/ai-gene-review/pull/5189) | [`e636319d505f`](https://github.com/ai4curation/ai-gene-review/commit/e636319d505f36b4f2f294d494c801fd41994ff3) / [`2556e031729c`](https://github.com/ai4curation/ai-gene-review/commit/2556e031729cfc0399b778793875925eb83edf17) | [approval](https://github.com/ai4curation/ai-gene-review/pull/5189#pullrequestreview-5562051331) / [detail](https://github.com/ai4curation/ai-gene-review/pull/5189#issuecomment-6247420388) | 25 | [39195350971](https://github.com/ai4curation/ai-gene-review/actions/runs/39195350971) cancelled / [39195350913](https://github.com/ai4curation/ai-gene-review/actions/runs/39195350913) cancelled | [39193780479](https://github.com/ai4curation/ai-gene-review/actions/runs/39193780479) success |
| [DSPP #5191](https://github.com/ai4curation/ai-gene-review/pull/5191) | [`d94ee03e2a0d`](https://github.com/ai4curation/ai-gene-review/commit/d94ee03e2a0d76c9264d3ffb4350521f047e4df3) / [`5b34aefb94ae`](https://github.com/ai4curation/ai-gene-review/commit/5b34aefb94ae9d0aa9ea599bd08a96b093625b2c) | [approval](https://github.com/ai4curation/ai-gene-review/pull/5191#pullrequestreview-5562219152) / [detail](https://github.com/ai4curation/ai-gene-review/pull/5191#issuecomment-6247971623) | 24 | [39195398487](https://github.com/ai4curation/ai-gene-review/actions/runs/39195398487) cancelled / [39195398424](https://github.com/ai4curation/ai-gene-review/actions/runs/39195398424) success | [39194052484](https://github.com/ai4curation/ai-gene-review/actions/runs/39194052484) success |
| [DSP #5192](https://github.com/ai4curation/ai-gene-review/pull/5192) | [`95a97d3c58fc`](https://github.com/ai4curation/ai-gene-review/commit/95a97d3c58fcf7c02494cc25278d139a94e0c462) / [`a532a7e2a80a`](https://github.com/ai4curation/ai-gene-review/commit/a532a7e2a80a40000cd1fc2de1453eeef4bebc93) | [approval](https://github.com/ai4curation/ai-gene-review/pull/5192#pullrequestreview-5562245042) / [detail](https://github.com/ai4curation/ai-gene-review/pull/5192#issuecomment-6248012201) | 42 | [39195900296](https://github.com/ai4curation/ai-gene-review/actions/runs/39195900296) cancelled / [39195900287](https://github.com/ai4curation/ai-gene-review/actions/runs/39195900287) success | [39194505866](https://github.com/ai4curation/ai-gene-review/actions/runs/39194505866) success |
| [DSG2 #5193](https://github.com/ai4curation/ai-gene-review/pull/5193) | [`cc1b22a58fcf`](https://github.com/ai4curation/ai-gene-review/commit/cc1b22a58fcf047bf9afa85c10ead212ce78ba2e) / [`75aa3e00937b`](https://github.com/ai4curation/ai-gene-review/commit/75aa3e00937b5e9917481cc2e7fa7b93af1a4b4b) | [approval](https://github.com/ai4curation/ai-gene-review/pull/5193#pullrequestreview-5562443524) / [detail](https://github.com/ai4curation/ai-gene-review/pull/5193#issuecomment-6248412698) | 35 | [39195901249](https://github.com/ai4curation/ai-gene-review/actions/runs/39195901249) cancelled / [39195901445](https://github.com/ai4curation/ai-gene-review/actions/runs/39195901445) cancelled | [39194610015](https://github.com/ai4curation/ai-gene-review/actions/runs/39194610015) success |
| [DST #5194](https://github.com/ai4curation/ai-gene-review/pull/5194) | [`572573c3c88d`](https://github.com/ai4curation/ai-gene-review/commit/572573c3c88d56212a9cd6f9f8db02c439c0b508) / [`fc7905919eba`](https://github.com/ai4curation/ai-gene-review/commit/fc7905919eba92a7b64c0053a832e0e5f0dd4514) | [approval](https://github.com/ai4curation/ai-gene-review/pull/5194#pullrequestreview-5562472606) / [detail](https://github.com/ai4curation/ai-gene-review/pull/5194#issuecomment-6248486691) | 27 | [39196041995](https://github.com/ai4curation/ai-gene-review/actions/runs/39196041995) cancelled / [39196041953](https://github.com/ai4curation/ai-gene-review/actions/runs/39196041953) success | [39194656802](https://github.com/ai4curation/ai-gene-review/actions/runs/39194656802) success |
| [DYNC2H1 #5195](https://github.com/ai4curation/ai-gene-review/pull/5195) | [`589cc2bcfa69`](https://github.com/ai4curation/ai-gene-review/commit/589cc2bcfa691aaa72e1c76914d0062eacf7cbc3) / [`cf4e305fd676`](https://github.com/ai4curation/ai-gene-review/commit/cf4e305fd6764de9fa0a6684e91e63eb2c3eb585) | [approval](https://github.com/ai4curation/ai-gene-review/pull/5195#pullrequestreview-5562664256) / [detail](https://github.com/ai4curation/ai-gene-review/pull/5195#issuecomment-6249056551) | 16 | [39196191841](https://github.com/ai4curation/ai-gene-review/actions/runs/39196191841) cancelled / [39196191806](https://github.com/ai4curation/ai-gene-review/actions/runs/39196191806) success | [39194657870](https://github.com/ai4curation/ai-gene-review/actions/runs/39194657870) success |
| [DTNBP1 #5196](https://github.com/ai4curation/ai-gene-review/pull/5196) | [`03d41d65b557`](https://github.com/ai4curation/ai-gene-review/commit/03d41d65b5577b6597cb17a35ff75707525acd01) / [`fb63079d569c`](https://github.com/ai4curation/ai-gene-review/commit/fb63079d569c7c90ed896fe10783ac620b517165) | [approval](https://github.com/ai4curation/ai-gene-review/pull/5196#pullrequestreview-5562705125) / [detail](https://github.com/ai4curation/ai-gene-review/pull/5196#issuecomment-6249229218) | 38 | [39196449647](https://github.com/ai4curation/ai-gene-review/actions/runs/39196449647) cancelled / [39196449636](https://github.com/ai4curation/ai-gene-review/actions/runs/39196449636) cancelled | [39194865002](https://github.com/ai4curation/ai-gene-review/actions/runs/39194865002) success |
| [DYNC1H1 #5197](https://github.com/ai4curation/ai-gene-review/pull/5197) | [`6e18c9fee11d`](https://github.com/ai4curation/ai-gene-review/commit/6e18c9fee11de522fec40dceea6d07352ea11afb) / [`80e71bc89765`](https://github.com/ai4curation/ai-gene-review/commit/80e71bc897654ac90f70b5792cf8a160acc5f761) | [approval](https://github.com/ai4curation/ai-gene-review/pull/5197#pullrequestreview-5562818228) / [detail](https://github.com/ai4curation/ai-gene-review/pull/5197#issuecomment-6249493883) | 16 | [39196612953](https://github.com/ai4curation/ai-gene-review/actions/runs/39196612953) cancelled / [39196612959](https://github.com/ai4curation/ai-gene-review/actions/runs/39196612959) success | [39195173513](https://github.com/ai4curation/ai-gene-review/actions/runs/39195173513) success |
| [DYNC2I1 #5198](https://github.com/ai4curation/ai-gene-review/pull/5198) | [`1e03c1c23080`](https://github.com/ai4curation/ai-gene-review/commit/1e03c1c23080e9e523754bdbca5390cbc61d9a70) / [`fb4523358525`](https://github.com/ai4curation/ai-gene-review/commit/fb4523358525fa85ee3f667d64a74695a0e12cad) | [approval](https://github.com/ai4curation/ai-gene-review/pull/5198#pullrequestreview-5562889655) / [detail](https://github.com/ai4curation/ai-gene-review/pull/5198#issuecomment-6249611850) | 13 | [39196818398](https://github.com/ai4curation/ai-gene-review/actions/runs/39196818398) cancelled / [39196818396](https://github.com/ai4curation/ai-gene-review/actions/runs/39196818396) cancelled | [39195352469](https://github.com/ai4curation/ai-gene-review/actions/runs/39195352469) success |
| [DYNC2I2 #5199](https://github.com/ai4curation/ai-gene-review/pull/5199) | [`b62674f50cce`](https://github.com/ai4curation/ai-gene-review/commit/b62674f50cce2a15db3e88300070be3e8878b8af) / [`d27e12acf159`](https://github.com/ai4curation/ai-gene-review/commit/d27e12acf159518bbe9284b1a876c473b59c2d89) | [approval](https://github.com/ai4curation/ai-gene-review/pull/5199#pullrequestreview-5562991309) / [detail](https://github.com/ai4curation/ai-gene-review/pull/5199#issuecomment-6249882551) | 15 | [39196864128](https://github.com/ai4curation/ai-gene-review/actions/runs/39196864128) cancelled / [39196864086](https://github.com/ai4curation/ai-gene-review/actions/runs/39196864086) success | [39195400174](https://github.com/ai4curation/ai-gene-review/actions/runs/39195400174) success |
| [DZIP1L #5200](https://github.com/ai4curation/ai-gene-review/pull/5200) | [`6f162afe0af2`](https://github.com/ai4curation/ai-gene-review/commit/6f162afe0af2f88c488f8ed766874f80df7b1235) / [`226af0294fc8`](https://github.com/ai4curation/ai-gene-review/commit/226af0294fc8afe63595871fd238fffc1b2b2a2a) | [approval](https://github.com/ai4curation/ai-gene-review/pull/5200#pullrequestreview-5563291296) / [detail](https://github.com/ai4curation/ai-gene-review/pull/5200#issuecomment-6250757324) | 24 | [39197258526](https://github.com/ai4curation/ai-gene-review/actions/runs/39197258526) cancelled / [39197258604](https://github.com/ai4curation/ai-gene-review/actions/runs/39197258604) cancelled | [39195902343](https://github.com/ai4curation/ai-gene-review/actions/runs/39195902343) success |
| [DYSF #5201](https://github.com/ai4curation/ai-gene-review/pull/5201) | [`49b5a265f90e`](https://github.com/ai4curation/ai-gene-review/commit/49b5a265f90ed06d3be175ddb9ca2dd5ec1aec66) / [`1068c61a9bc4`](https://github.com/ai4curation/ai-gene-review/commit/1068c61a9bc4c06a6bed0b51ee652573175cbecc) | [approval](https://github.com/ai4curation/ai-gene-review/pull/5201#pullrequestreview-5563163099) / [detail](https://github.com/ai4curation/ai-gene-review/pull/5201#issuecomment-6250400278) | 64 | [39197257972](https://github.com/ai4curation/ai-gene-review/actions/runs/39197257972) cancelled / [39197257858](https://github.com/ai4curation/ai-gene-review/actions/runs/39197257858) success | [39195858820](https://github.com/ai4curation/ai-gene-review/actions/runs/39195858820) success |
| [DYRK1A #5202](https://github.com/ai4curation/ai-gene-review/pull/5202) | [`6597d1785ec4`](https://github.com/ai4curation/ai-gene-review/commit/6597d1785ec43f141c6454e9a2bf4bf34a9b2d2f) / [`406f5938e971`](https://github.com/ai4curation/ai-gene-review/commit/406f5938e9714f4691d785ec90a0e09471a31a25) | [approval](https://github.com/ai4curation/ai-gene-review/pull/5202#pullrequestreview-5563341932) / [detail](https://github.com/ai4curation/ai-gene-review/pull/5202#issuecomment-6250910959) | 40 | [39197545128](https://github.com/ai4curation/ai-gene-review/actions/runs/39197545128) cancelled / [39197545204](https://github.com/ai4curation/ai-gene-review/actions/runs/39197545204) success | [39196042828](https://github.com/ai4curation/ai-gene-review/actions/runs/39196042828) success |
| [EARS2 #5203](https://github.com/ai4curation/ai-gene-review/pull/5203) | [`47586cd9ec28`](https://github.com/ai4curation/ai-gene-review/commit/47586cd9ec28e61b1bab3fe016f04bf38d03ea41) / [`112b5bcc30f5`](https://github.com/ai4curation/ai-gene-review/commit/112b5bcc30f58eba2217df67296df6096a854d0c) | [approval](https://github.com/ai4curation/ai-gene-review/pull/5203#pullrequestreview-5563380442) / [detail](https://github.com/ai4curation/ai-gene-review/pull/5203#issuecomment-6251036843) | 19 | [39197634082](https://github.com/ai4curation/ai-gene-review/actions/runs/39197634082) cancelled / [39197633986](https://github.com/ai4curation/ai-gene-review/actions/runs/39197633986) success | [39196193202](https://github.com/ai4curation/ai-gene-review/actions/runs/39196193202) success |
| [EBF3 #5204](https://github.com/ai4curation/ai-gene-review/pull/5204) | [`c40488eaa2a4`](https://github.com/ai4curation/ai-gene-review/commit/c40488eaa2a4a50cd94d6c3c90103919dd90257c) / [`6ed8e2a7f55e`](https://github.com/ai4curation/ai-gene-review/commit/6ed8e2a7f55e81007afbfe997efcd9a6c7f10da6) | [approval](https://github.com/ai4curation/ai-gene-review/pull/5204#pullrequestreview-5563376538) / [detail](https://github.com/ai4curation/ai-gene-review/pull/5204#issuecomment-6251018312) | 17 | [39197924600](https://github.com/ai4curation/ai-gene-review/actions/runs/39197924600) cancelled / [39197924606](https://github.com/ai4curation/ai-gene-review/actions/runs/39197924606) cancelled | [39196451008](https://github.com/ai4curation/ai-gene-review/actions/runs/39196451008) success |
| [EBP #5206](https://github.com/ai4curation/ai-gene-review/pull/5206) | [`68f7809eaf59`](https://github.com/ai4curation/ai-gene-review/commit/68f7809eaf59425cb19a9c2cf9c6639d61fdf1a3) / [`b54117406d6e`](https://github.com/ai4curation/ai-gene-review/commit/b54117406d6e27c79d4d7226636ffea62ffe4ebc) | [approval](https://github.com/ai4curation/ai-gene-review/pull/5206#pullrequestreview-5563650354) / [detail](https://github.com/ai4curation/ai-gene-review/pull/5206#issuecomment-6251553396) | 18 | [39198396486](https://github.com/ai4curation/ai-gene-review/actions/runs/39198396486) cancelled / [39198396497](https://github.com/ai4curation/ai-gene-review/actions/runs/39198396497) cancelled | [39196820332](https://github.com/ai4curation/ai-gene-review/actions/runs/39196820332) success |
| [ECHS1 #5207](https://github.com/ai4curation/ai-gene-review/pull/5207) | [`59891106a316`](https://github.com/ai4curation/ai-gene-review/commit/59891106a316a4aa4189bcb60b9eb1a3adfe6400) / [`398bc75deb14`](https://github.com/ai4curation/ai-gene-review/commit/398bc75deb144c27f5efc2a5dc338c677dd83dd4) | [approval](https://github.com/ai4curation/ai-gene-review/pull/5207#pullrequestreview-5563770156) / [detail](https://github.com/ai4curation/ai-gene-review/pull/5207#issuecomment-6251928089) | 18 | [39198538846](https://github.com/ai4curation/ai-gene-review/actions/runs/39198538846) cancelled / [39198538917](https://github.com/ai4curation/ai-gene-review/actions/runs/39198538917) success | [39197217052](https://github.com/ai4curation/ai-gene-review/actions/runs/39197217052) success |
| [EDAR #5209](https://github.com/ai4curation/ai-gene-review/pull/5209) | [`ee11a9c9ed0b`](https://github.com/ai4curation/ai-gene-review/commit/ee11a9c9ed0b87ce13b2e15612da2dea074bf87c) / [`71b6c5799dfc`](https://github.com/ai4curation/ai-gene-review/commit/71b6c5799dfc936e6fde3443fe83a1cd07a18345) | [approval](https://github.com/ai4curation/ai-gene-review/pull/5209#pullrequestreview-5563884824) / [detail](https://github.com/ai4curation/ai-gene-review/pull/5209#issuecomment-6252319106) | 26 | [39198820516](https://github.com/ai4curation/ai-gene-review/actions/runs/39198820516) cancelled / [39198820467](https://github.com/ai4curation/ai-gene-review/actions/runs/39198820467) success | [39197259771](https://github.com/ai4curation/ai-gene-review/actions/runs/39197259771) success |
| [EEF1A2 #5210](https://github.com/ai4curation/ai-gene-review/pull/5210) | [`4c9c7d3ac8f4`](https://github.com/ai4curation/ai-gene-review/commit/4c9c7d3ac8f4cbae7b3bf4007b7bcfae58623370) / [`d564c0d6318a`](https://github.com/ai4curation/ai-gene-review/commit/d564c0d6318a1856b1c1569a6afde8eacffc0d24) | [approval](https://github.com/ai4curation/ai-gene-review/pull/5210#pullrequestreview-5563957383) / [detail](https://github.com/ai4curation/ai-gene-review/pull/5210#issuecomment-6252551937) | 27 | [39199086385](https://github.com/ai4curation/ai-gene-review/actions/runs/39199086385) cancelled / [39199086378](https://github.com/ai4curation/ai-gene-review/actions/runs/39199086378) cancelled | [39197546581](https://github.com/ai4curation/ai-gene-review/actions/runs/39197546581) success |
| [EFL1 #5212](https://github.com/ai4curation/ai-gene-review/pull/5212) | [`ed0f1b2d871f`](https://github.com/ai4curation/ai-gene-review/commit/ed0f1b2d871f6c98a196ac529929f596040cedfa) / [`6a7cc1874c90`](https://github.com/ai4curation/ai-gene-review/commit/6a7cc1874c9051e487e2b66b8af98760ea8d111a) | [approval](https://github.com/ai4curation/ai-gene-review/pull/5212#pullrequestreview-5564046076) / [detail](https://github.com/ai4curation/ai-gene-review/pull/5212#issuecomment-6252843357) | 20 | [39199088053](https://github.com/ai4curation/ai-gene-review/actions/runs/39199088053) cancelled / [39199087994](https://github.com/ai4curation/ai-gene-review/actions/runs/39199087994) success | [39197635176](https://github.com/ai4curation/ai-gene-review/actions/runs/39197635176) success |
| [EFEMP1 #5211](https://github.com/ai4curation/ai-gene-review/pull/5211) | [`eebf417e370c`](https://github.com/ai4curation/ai-gene-review/commit/eebf417e370c1d173dec3b7bd6997e2cfac38b17) / [`8e7fec328553`](https://github.com/ai4curation/ai-gene-review/commit/8e7fec328553636be3af4dd95ed927ba92612826) | [approval](https://github.com/ai4curation/ai-gene-review/pull/5211#pullrequestreview-5564121765) / [detail](https://github.com/ai4curation/ai-gene-review/pull/5211#issuecomment-6253045187) | 22 | [39199472305](https://github.com/ai4curation/ai-gene-review/actions/runs/39199472305) cancelled / [39199472302](https://github.com/ai4curation/ai-gene-review/actions/runs/39199472302) cancelled | [39197926121](https://github.com/ai4curation/ai-gene-review/actions/runs/39197926121) success |
| [EFNB1 #5216](https://github.com/ai4curation/ai-gene-review/pull/5216) | [`c25a84d61d9f`](https://github.com/ai4curation/ai-gene-review/commit/c25a84d61d9f32c08eb42da78c0738a46156cdc4) / [`aedd27b9cba6`](https://github.com/ai4curation/ai-gene-review/commit/aedd27b9cba617c13644a87b447f532665666b88) | [approval](https://github.com/ai4curation/ai-gene-review/pull/5216#pullrequestreview-5564381802) / [detail](https://github.com/ai4curation/ai-gene-review/pull/5216#issuecomment-6253747878) | 32 | [39199555560](https://github.com/ai4curation/ai-gene-review/actions/runs/39199555560) cancelled / [39199555516](https://github.com/ai4curation/ai-gene-review/actions/runs/39199555516) success | [39198104288](https://github.com/ai4curation/ai-gene-review/actions/runs/39198104288) success |
| [EFEMP2 #5214](https://github.com/ai4curation/ai-gene-review/pull/5214) | [`c8945f77bb2a`](https://github.com/ai4curation/ai-gene-review/commit/c8945f77bb2a5a5ee061af9085b8717e37023790) / [`1032e54fff10`](https://github.com/ai4curation/ai-gene-review/commit/1032e54fff10e15b19220fcb5e39667efeced56c) | [approval](https://github.com/ai4curation/ai-gene-review/pull/5214#pullrequestreview-5564407856) / [detail](https://github.com/ai4curation/ai-gene-review/pull/5214#issuecomment-6253780134) | 38 | [39200006193](https://github.com/ai4curation/ai-gene-review/actions/runs/39200006193) cancelled / [39200006150](https://github.com/ai4curation/ai-gene-review/actions/runs/39200006150) success | [39198398570](https://github.com/ai4curation/ai-gene-review/actions/runs/39198398570) success |
| [EFTUD2 #5217](https://github.com/ai4curation/ai-gene-review/pull/5217) | [`dc7af6e90ee4`](https://github.com/ai4curation/ai-gene-review/commit/dc7af6e90ee4573eb0bced9f5fb645751250e701) / [`f83a00550e18`](https://github.com/ai4curation/ai-gene-review/commit/f83a00550e186baad06ca43b627446aa4888466f) | [approval](https://github.com/ai4curation/ai-gene-review/pull/5217#pullrequestreview-5564562667) / [detail](https://github.com/ai4curation/ai-gene-review/pull/5217#issuecomment-6254008010) | 31 | [39200007097](https://github.com/ai4curation/ai-gene-review/actions/runs/39200007097) cancelled / [39200007094](https://github.com/ai4curation/ai-gene-review/actions/runs/39200007094) cancelled | [39198400037](https://github.com/ai4curation/ai-gene-review/actions/runs/39198400037) success |
| [EGLN1 #5218](https://github.com/ai4curation/ai-gene-review/pull/5218) | [`f0b9710c5988`](https://github.com/ai4curation/ai-gene-review/commit/f0b9710c59889a7149ab9a28baa14376e523dde1) / [`58b90b0b579a`](https://github.com/ai4curation/ai-gene-review/commit/58b90b0b579a24cd9fd9d826dad874a04e0ada75) | [approval](https://github.com/ai4curation/ai-gene-review/pull/5218#pullrequestreview-5564793906) / [detail](https://github.com/ai4curation/ai-gene-review/pull/5218#issuecomment-6254699274) | 39 | [39200135501](https://github.com/ai4curation/ai-gene-review/actions/runs/39200135501) cancelled / [39200135508](https://github.com/ai4curation/ai-gene-review/actions/runs/39200135508) cancelled | [39198540735](https://github.com/ai4curation/ai-gene-review/actions/runs/39198540735) success |
| [DNAH17 #5154](https://github.com/ai4curation/ai-gene-review/pull/5154) | [`ba791f830b16`](https://github.com/ai4curation/ai-gene-review/commit/ba791f830b16f50e2dc6fe632286ff8111d42a78) / [`0b6ca0183624`](https://github.com/ai4curation/ai-gene-review/commit/0b6ca01836243691ec860840e326b4369a7b36cb) | [approval](https://github.com/ai4curation/ai-gene-review/pull/5154#pullrequestreview-5561786441) / [detail](https://github.com/ai4curation/ai-gene-review/pull/5154#issuecomment-6246649944) | 7 | [39297514802](https://github.com/ai4curation/ai-gene-review/actions/runs/39297514802) cancelled / [39297514592](https://github.com/ai4curation/ai-gene-review/actions/runs/39297514592) cancelled | [39293010123](https://github.com/ai4curation/ai-gene-review/actions/runs/39293010123) success |
| [DNASE1L3 #5164](https://github.com/ai4curation/ai-gene-review/pull/5164) | [`95c9f6a6bb26`](https://github.com/ai4curation/ai-gene-review/commit/95c9f6a6bb26af8f2c7fde6ab3a006a7bce1b5f2) / [`87ce1e9437b5`](https://github.com/ai4curation/ai-gene-review/commit/87ce1e9437b5c02efcf5ec8f99e41626a1d85617) | [approval](https://github.com/ai4curation/ai-gene-review/pull/5164#pullrequestreview-5561781270) / [detail](https://github.com/ai4curation/ai-gene-review/pull/5164#issuecomment-6246651948) | 20 | [39297517088](https://github.com/ai4curation/ai-gene-review/actions/runs/39297517088) success / [39297516955](https://github.com/ai4curation/ai-gene-review/actions/runs/39297516955) success | [39293061047](https://github.com/ai4curation/ai-gene-review/actions/runs/39293061047) success |

All 1,610 approved PR path occurrences match their merge blobs and modes and
remain identical at captured main `a17627810d4a13efede28a3c07a481aa0b44131b`. Saved commit objects prove
containment of all 68 merges. Each accepted audit also establishes unchanged
paths outside its complete PR delta relative to its immediate parent. Shared
source paths may occur in multiple audits; this total counts path occurrences.
No accepted current mandatory review request or unresolved thread remains.

The immediate main builds comprise 67 cancellations and one success
(DNASE1L3); 40 immediate documentation runs succeeded. These outcomes are
preserved individually above. Exact approved-head and actual-merge merge-group
checks supply gene-specific evidence. Successful descendants corroborate preserved
payload and runtime; they are not claimed to revalidate every earlier gene.
The accepted batch limits are retained explicitly:

Batch 03 (473→483): All ten immediate main builds cancelled; six aggregate gates failed due to cancellation. DNAJB6 and DNAAF1 completed actual-main gene validation before later cancellation, without a successful whole main build. Each exact merge commit passed merge-group checks. Descendant bridge preserves all payloads and executable runtime; only eleven unrelated GO-cache terms added. Its scoped validation does not revalidate these ten. Docs deployments do not imply fresh individual gene HTML. No new science/quotes or ordinary local suite in this audit.

Batch 04 (483→493): All ten immediate main builds cancelled; six cancellation-dependent gates failed. DNAJB2, DNAAF4 and DNAAF6 passed actual-main gene/history checks before later family-step cancellation. No whole main build is relabeled successful. Exact actual merge commits all passed merge-group checks. The successful descendant preserves all 160 payload paths and executable runtime; eleven unrelated GO-cache additions only. Its scoped validation does not revalidate these ten. Seven immediate docs successes describe schema/MkDocs deployment, not individual gene HTML regeneration. Two failed log-retrieval attempts and v1 prose-total correction remain recorded. Effective recovered log and 160-path proof passed. No ordinary local suite or scientific quotations added.

Batch 05 (493→503): All ten immediate main builds cancelled. Exact approved-head and actual-merge merge-group checks passed; cancelled aggregate outcomes remain cancelled or failed. Successful descendant bb50821d71232c86e36c9dee6ed1d0604f6b5505 preserves selected payloads and executable runtime, with eleven unrelated additive GO-cache rows. Its scoped validation does not revalidate these earlier genes. Six immediate docs successes are schema/MkDocs deployment, not individual gene HTML regeneration. No ordinary local suite or scientific quotation added during audit. DOCK6/DOCK2 passed gene/history checks before later family cancellation; six aggregate gates failed due to cancellation. DNM2 and DOCK2 retain explicitly disclosed stale committed HTML.

Batch 06 (503→513): All ten immediate main builds cancelled. Exact approved-head and actual-merge merge-group checks passed; cancelled aggregate outcomes remain cancelled or failed. Successful descendant bb50821d71232c86e36c9dee6ed1d0604f6b5505 preserves selected payloads and executable runtime, with eleven unrelated additive GO-cache rows. Its scoped validation does not revalidate these earlier genes. Six immediate docs successes are schema/MkDocs deployment, not individual gene HTML regeneration. No ordinary local suite or scientific quotation added during audit. DPAGT1 gene validation passed but history pytest was interrupted. DPH1 displayed validations passed but job/API conclusion remains cancelled and gate failed. Eight aggregate gates failed due to cancellation. DOLK eight resolved inline threads were read by delegated auditor.

Batch 07 (513→523): All ten immediate-main builds cancelled; eight aggregate gates failed due to cancellation. DSPP gene/history passed before family cancellation; DYNC2H1 gene passed but history interrupted. No cancelled or skipped test is relabeled successful. Exact approved-head and actual-merge merge-group checks passed. Successful bb508 descendant preserves 251 selected paths and executable runtime, with eleven unrelated additive GO-cache rows; it does not revalidate these ten earlier genes. Six immediate docs successes mean schema/MkDocs deployment, not individual gene HTML regeneration. No local ordinary suite or scientific quote added by this audit.

Batch 08 (523→533): All ten immediate-main builds cancelled; seven aggregate gates failed due to cancellation. DYNC2I2 gene/history passed before family cancellation; DZIP1L/EARS2/ECHS1 gene passed but history completion not established. Main broad tests were skipped. Exact approved-head and actual-merge merge-group checks passed. Successful bb508 descendant preserves all 268 paths and executable runtime, with eleven or ten unrelated additive GO-cache rows. Its scoped validation does not revalidate these ten earlier genes. Six immediate docs successes mean schema/MkDocs deployment, not individual gene HTML regeneration. No ordinary local suite or scientific quotation added during audit.

Batch 09 (533→541): Seven immediate-main builds cancelled; three aggregate gates failed due to cancellation. EFL1/EFNB1 gene/history passed before family cancellation. DNASE1L3 actual main gene/history/family passed; broad suite and history coverage were skipped. Exact approved-head and actual-merge merge-group checks passed for all eight. First six preserve selected paths/runtime to bb508 except ten unrelated additive GO-cache rows. DNAH17 instead preserves all payload and 298 runtime blobs to later successful DNASE1L3 merge [`87ce1e9437b5`](https://github.com/ai4curation/ai-gene-review/commit/87ce1e9437b5c02efcf5ec8f99e41626a1d85617). DNASE1L3 uses its own actual-main pass; neither successor is claimed to revalidate prior genes. Four immediate docs successes mean schema/MkDocs deployment, not individual gene HTML regeneration. Incorrect old-successor attempt retained as failure and replaced by versioned correct proof. No ordinary local suite or scientific quotation added during audit.

The shared successful descendant [`bb50821d7123`](https://github.com/ai4curation/ai-gene-review/commit/bb50821d71232c86e36c9dee6ed1d0604f6b5505)
has [build 39200674021](https://github.com/ai4curation/ai-gene-review/actions/runs/39200674021) and
[docs 39200673967](https://github.com/ai4curation/ai-gene-review/actions/runs/39200673967).
DNAH17 uses the later DNASE1L3 merge [`87ce1e9437b5`](https://github.com/ai4curation/ai-gene-review/commit/87ce1e9437b5c02efcf5ec8f99e41626a1d85617),
with [build 39297517088](https://github.com/ai4curation/ai-gene-review/actions/runs/39297517088) and
[docs 39297516955](https://github.com/ai4curation/ai-gene-review/actions/runs/39297516955); DNASE1L3 uses its own main pass.
Documentation success denotes schema/MkDocs generation and deployment, not fresh
rendering or visual inspection of every gene HTML page. DNM2 and DOCK2 retain the
explicitly disclosed stale committed HTML. Accepted generic-binding advisories
and source uncertainties are not silently removed by this completion update.

The current main inventory contains 8,472 review files, including 3,102 human
reviews. 1,248 catalogue genes have reviews and 1,628 lack them;
707 available catalogue reviews remain uncredited. All 2,876 catalogue
identities and association texts and 235 historical queue objects remain exact.
The 102 updates already published on this PR branch remain exact; 92 of those
pre-existed on main. This follow-up appends update 103. Previous progress text,
including checkpoint 473's original inventory, is preserved byte-for-byte.

The publication preimage is open [PR #5253](https://github.com/ai4curation/ai-gene-review/pull/5253) at
`a6b08818d82e62d653bd9f330df66697ecb082cb`, containing checkpoint 473 and its existing history.
Relative to main checkpoint 443, the combined PR has 98 checkbox changes
(30 already published plus these 68) and 103 updates rather than main's 92.
The publisher ran all eight project frontmatter checks, rendered both project
pages and validated a new append-only history record. The catalogue render
reports 1,628 missing-review warnings; the progress render reports none. The
combined PR has eight paths, retaining the earlier checkpoint 473 history.
Gene reviews, source caches and runtime files remain unchanged by this update.

[Curation session](https://github.com/ai4curation/ai-gene-review/blob/cmungall/clingen-tracker473-20261021/history/projects/CLINGEN_MENDELIAN/2026-10-21T010856Z-codex-decdef.yaml)

Terminal publication preflight observed EGR2 merging after that evidence cut,
advancing main to [`a1dc7cee46ff`](https://github.com/ai4curation/ai-gene-review/commit/a1dc7cee46ff3f4a7c8b06efe4221e0bfe17e6ae).
A complete 26-path tree comparison confirms no tracker, project-history or runtime
change and no change to the 1,610 accepted path occurrences. The inventory counts
remain 8,472 total reviews, 3,102 human, 1,248 available catalogue reviews and
1,628 missing. The open-head gate changed only by removing merged PR #5249 and
then stabilized at 163 heads. This bridge adds no EGR2 completion credit; the
frozen checkpoint remains 541.

## Completion checkpoint 544 — 2026-10-21 02:35:41 UTC

**544 complete; 2,332 remaining out of 2,876 primary catalogue genes.**
This checkpoint adds exactly EGR2, EHMT1 and EGFR to the merged 541 checkpoint.
The coordinating AI agent accepted each complete merge audit; this is not a
human maintainer sign-off or a new biological review. Products, follow-up PRs
and the tracker publication receive no additional gene credit.

| Gene / PR | Approved head / merge | Approval / detail | Exact PR paths | Immediate main build / docs | Exact merge-group build |
|---|---|---|---:|---|---|
| [EGR2 #5249](https://github.com/ai4curation/ai-gene-review/pull/5249) | [`53560956d08a`](https://github.com/ai4curation/ai-gene-review/commit/53560956d08ae0d01ce116e1af5e483d2431b66e) / [`a1dc7cee46ff`](https://github.com/ai4curation/ai-gene-review/commit/a1dc7cee46ff3f4a7c8b06efe4221e0bfe17e6ae) | [approval](https://github.com/ai4curation/ai-gene-review/pull/5249#pullrequestreview-5593478509) / [detail](https://github.com/ai4curation/ai-gene-review/pull/5249#issuecomment-6304890310) | 26 | [39524461723](https://github.com/ai4curation/ai-gene-review/actions/runs/39524461723) success / [39524461748](https://github.com/ai4curation/ai-gene-review/actions/runs/39524461748) success | [39522566057](https://github.com/ai4curation/ai-gene-review/actions/runs/39522566057) success |
| [EHMT1 #5251](https://github.com/ai4curation/ai-gene-review/pull/5251) | [`a455c87f9263`](https://github.com/ai4curation/ai-gene-review/commit/a455c87f9263c4d3e4f518b572a4d52f0470de86) / [`f1f1f9b20ec6`](https://github.com/ai4curation/ai-gene-review/commit/f1f1f9b20ec60f6a0b489b98867c3fcf33663823) | [approval](https://github.com/ai4curation/ai-gene-review/pull/5251#pullrequestreview-5593669020) / [detail](https://github.com/ai4curation/ai-gene-review/pull/5251#issuecomment-6305268790) | 34 | [39526942091](https://github.com/ai4curation/ai-gene-review/actions/runs/39526942091) success / [39526942097](https://github.com/ai4curation/ai-gene-review/actions/runs/39526942097) success | [39525021979](https://github.com/ai4curation/ai-gene-review/actions/runs/39525021979) success |
| [EGFR #5252](https://github.com/ai4curation/ai-gene-review/pull/5252) | [`0638a3b2722e`](https://github.com/ai4curation/ai-gene-review/commit/0638a3b2722e15b68ec28aa4a3c03c409bd4052a) / [`8eeb6f927b0f`](https://github.com/ai4curation/ai-gene-review/commit/8eeb6f927b0f7cc733934c6706d5710fc65f8eb8) | [approval](https://github.com/ai4curation/ai-gene-review/pull/5252#pullrequestreview-5593970737) / [detail](https://github.com/ai4curation/ai-gene-review/pull/5252#issuecomment-6305907508) | 35 | [39531434283](https://github.com/ai4curation/ai-gene-review/actions/runs/39531434283) cancelled / [39531434228](https://github.com/ai4curation/ai-gene-review/actions/runs/39531434228) success | [39529711313](https://github.com/ai4curation/ai-gene-review/actions/runs/39529711313) success |

All 95 approved PR path occurrences match their merged blobs and modes and
remain identical at main `81298ef287dae81220ae068a10a524f17628bf7d`. Authenticated commit objects establish
the EGR2 → EHMT1 → EGFR → tracker sequence. Each accepted merge audit also
checks the complete immediate-parent delta and unchanged paths outside it.
The final approved heads have no unresolved review threads or blocking requests.

EGR2 passed scoped gene validation and 42 history tests on its PR and main
builds; broad suites, all-schema and module checks ran on the merge-group.
History coverage ran on the PR only. Its DRAFT status and inherited uncited
research-report advisory remain recorded. EHMT1 passed scoped gene, history
and family checks on main, with broad suites, schemas and modules on the
merge-group; unresolved scientific contexts and optional suggestions remain.

EGFR's immediate main build [39531434283](https://github.com/ai4curation/ai-gene-review/actions/runs/39531434283)
was cancelled during checkout by a higher-priority main request. Its aggregate
failed because dependencies were cancelled; this is not a successful run.
The immediate tracker successor [`81298ef287da`](https://github.com/ai4curation/ai-gene-review/commit/81298ef287dae81220ae068a10a524f17628bf7d)
changed only eight project, render and history paths, preserving all 35 EGFR
payload paths and 18 runtime/workflow roots. Its successful
[build 39531567708](https://github.com/ai4curation/ai-gene-review/actions/runs/39531567708) ran broad tests and
history checks but explicitly skipped scoped gene validation. EGFR's exact
approved-head and actual-merge merge-group checks supply the gene checks;
successor success is not presented as fresh EGFR validation. The earlier failed
[merge-group 39526448256](https://github.com/ai4curation/ai-gene-review/actions/runs/39526448256), caused by a
stale source-report assertion, remains part of the record; the corrected final
head and merge-group passed.

EGFR remains DRAFT with 1,008 reviewed rows, 41 UNDECIDED annotations, four
products and one core function. Its 177 advisories comprise 169 generic-binding
and eight source-context warnings. Completion denotes accepted review delivery,
not certainty about every annotation. The documentation runs succeeded,
including the [tracker successor docs](https://github.com/ai4curation/ai-gene-review/actions/runs/39531567710);
the EGFR/successor docs retained 21 warnings. Documentation success covers
schema/MkDocs generation and deployment, not fresh individual gene HTML
rendering or visual inspection.

[Tracker PR #5253](https://github.com/ai4curation/ai-gene-review/pull/5253) landed checkpoint 541 at
`81298ef287dae81220ae068a10a524f17628bf7d` from approved head `e556803f9ba33e51eac8d98e197940424083881f`. Its eight
paths were verified exactly; that publication adds no gene credit. This update
starts from that merged main snapshot rather than modifying the closed PR.
All 235 historical queue objects and 103 previous completion updates remain
exact; this is update 104. Prior progress text, including older inventories and
then-pending gene statements, is preserved as historical evidence.

Current main has 8,473 review files, including 3,103 human reviews.
1,249 catalogue genes have reviews and 1,627 lack them; 705
available catalogue reviews remain uncredited. All 2,876 catalogue identities
and association texts are unchanged; only the three accepted checkboxes change.
No gene review, cache, runtime file or existing history is modified by this
checkpoint. The publisher passed eight project frontmatter checks, rendered both project
pages and validated one new append-only history record. The catalogue render
reports 1,627 missing-review warnings; the progress render reports none. These
four source changes, two HTML renders and new history form seven publication paths.

[Curation session](https://github.com/ai4curation/ai-gene-review/blob/cmungall/clingen-tracker544-20261021/history/projects/CLINGEN_MENDELIAN/2026-10-21T024452Z-codex-095029.yaml)
## Completion checkpoint 545 — 2026-10-21 16:59:33 UTC

**545 complete; 2,331 remaining out of 2,876 primary catalogue genes.**
This checkpoint adds only [EIF2B2 #5283](https://github.com/ai4curation/ai-gene-review/pull/5283)
to the merged 544 checkpoint. The coordinating AI agent accepted the complete
merge audit; this is not a human maintainer sign-off. Products, follow-up PRs
and the tracker publication receive no additional gene credit.

Approved head [`184a3beedb18`](https://github.com/ai4curation/ai-gene-review/commit/184a3beedb1835da7e15d39e63b88a8c1bb5aaa9)
merged at [`078fd7636b0a`](https://github.com/ai4curation/ai-gene-review/commit/078fd7636b0acb0abaef497d65b76bee22a485a9)
on 2026-10-21 at 06:27:56 UTC. All 25 approved paths, blobs and modes equal
the complete merge delta and this later pinned main snapshot; no extra path was
introduced. The current [approval](https://github.com/ai4curation/ai-gene-review/pull/5283#pullrequestreview-5595264244)
and [detailed review](https://github.com/ai4curation/ai-gene-review/pull/5283#issuecomment-6308625352)
have no unresolved threads or blocking requests.

The actual [merge-group build](https://github.com/ai4curation/ai-gene-review/actions/runs/39553679049)
passed strict EIF2B2 validation, all gene-schema and module checks, 14,749
history records, 42 history tests and family checks. It actually ran the full
suite: 4,168 tests passed, 268 doctests passed, 12 examples passed, typing and
lint passed, and 432 agentic plus 19 JavaScript tests passed. Skips and
dependency warnings remain in the audit.

The actual [main build](https://github.com/ai4curation/ai-gene-review/actions/runs/39555562252)
passed strict EIF2B2, history and family checks. Change filtering skipped
the general suite and all-gene/module scopes; the final test job only checked
upstream conclusions. The [documentation run](https://github.com/ai4curation/ai-gene-review/actions/runs/39555562068)
successfully built and deployed MkDocs, retaining navigation/dependency
warnings. This is not a claim of fresh gene HTML visual inspection.

EIF2B2 remains DRAFT with 42 reviewed source rows: 18 ACCEPT, 9 MODIFY,
8 KEEP_AS_NON_CORE, 4 UNDECIDED and 3 MARK_AS_OVER_ANNOTATED; one core function,
33 references and no publication quotations. The four accepted validation
advisories concern generic binding and source-specific action differences.
Completion means accepted review delivery, not certainty about every annotation.
Renderer [PR #5285](https://github.com/ai4curation/ai-gene-review/pull/5285)
is the immediate merge parent; its three approved files remain exact and it
receives no gene credit.

Main advanced through 1,212 unrelated paths after the merge audit. A bounded
comparison preserves all 25 EIF2B2 and three renderer paths exactly; it supplies
no additional gene credit or new CI claims. The inventory below is freshly
recounted from that successor.

This update starts from main `613523bf19bba276b9ea72840a06c56e606897f2`, with the seven
checkpoint-544 publication paths inherited from merged [tracker #5271](https://github.com/ai4curation/ai-gene-review/pull/5271).
All 235 historical queue objects and 104 previous completion updates remain
exact; this is update 105. Previous progress text remains byte-for-byte intact.
All 2,876 catalogue identities and association texts are unchanged; only the
EIF2B2 checkbox changes.

The pinned inventory has 8,550 review files, including 3,109 human reviews.
1,252 catalogue genes have reviews and 1,624 lack them; 707
available catalogue reviews remain uncredited. Four source changes, two
generated project pages and one new append-only history record form the
publication scope. No gene, source cache, runtime or prior history is edited.

The publisher passed eight project frontmatter checks, rendered both project
pages and validated the appended history record. The catalogue render reports
1,624 missing-review warnings; the progress render reports none.

[Curation session](https://github.com/ai4curation/ai-gene-review/blob/cmungall/clingen-tracker545-20261021/history/projects/CLINGEN_MENDELIAN/2026-10-21T170052Z-codex-877798.yaml)
## Completion checkpoint 546 — 2026-10-21 17:57:11 UTC

**546 complete; 2,330 remaining out of 2,876 primary catalogue genes.**
This checkpoint adds only [EIF2B3 #5284](https://github.com/ai4curation/ai-gene-review/pull/5284)
to merged checkpoint 545. The coordinating AI agent accepted the complete
merge audit and terminal main addendum; this is not a human maintainer sign-off.
Products, follow-up PRs and tracker publications receive no additional credit.

Approved head [`39624d66898c`](https://github.com/ai4curation/ai-gene-review/commit/39624d66898c4d816dc4f92d2ceceedf0a3a5894)
merged at [`06bb22ebd22c`](https://github.com/ai4curation/ai-gene-review/commit/06bb22ebd22c7ff13472ac27d3a2016c938c2d73)
on 2026-10-21 at 17:24:29 UTC. All 20 approved paths, blobs and modes equal
the complete merge delta and remain exact on the pinned main snapshot. The
current [approval](https://github.com/ai4curation/ai-gene-review/pull/5284#pullrequestreview-5596119912)
and [detailed review](https://github.com/ai4curation/ai-gene-review/pull/5284#issuecomment-6310142286)
have no unresolved threads or blocking requests. Advisory suggestions remain
recorded with their original scope.

The actual [merge-group build](https://github.com/ai4curation/ai-gene-review/actions/runs/39641181545)
passed strict EIF2B3 validation, all gene-schema and module checks, 14,895 history
records, 42 history tests and family checks. It actually ran the full suite:
4,176 tests passed, 268 doctests passed, 12 examples passed, typing and lint
passed, and 432 agentic plus 19 JavaScript tests passed. Skips, dependency
warnings and unresolved corpus diagnostics remain in the audit.

The actual [main build](https://github.com/ai4curation/ai-gene-review/actions/runs/39643518333)
passed strict EIF2B3, history and family checks. Change filtering skipped
the general suite and all-gene/module scopes; the final test job only checked
upstream conclusions. The [documentation run](https://github.com/ai4curation/ai-gene-review/actions/runs/39643518280)
successfully built and deployed MkDocs, retaining navigation/dependency warnings.
This is not a claim of fresh gene HTML visual inspection.

EIF2B3 has computed status COMPLETE with 34 reviewed source rows: 21 ACCEPT,
5 MODIFY, 4 KEEP_AS_NON_CORE, 3 UNDECIDED and 1 MARK_AS_OVER_ANNOTATED;
three natural products, one core function and no publication quotations.
Completion records accepted review delivery; the three unresolved source
judgments remain visible. The strict gene validation returned no annotation
warnings. The tracker publication adds no scientific decision or gene credit.

This update starts from main `31717524f1710d19c5f8b22c5418f37b9e08b6eb`, whose seven checkpoint-545
publication paths equal the approved payload of merged [tracker #5313](https://github.com/ai4curation/ai-gene-review/pull/5313).
All 235 historical queue objects and 105 previous completion updates remain
exact; this is update 106. Previous progress text remains byte-for-byte intact.
All 2,876 catalogue identities and association texts are unchanged; only the
EIF2B3 checkbox changes.

The pinned inventory has 8,551 review files, including 3,110 human reviews.
1,253 catalogue genes have reviews and 1,623 lack them; 707
available catalogue reviews remain uncredited. Four source changes, two generated
project pages and one new append-only history record form the publication scope.
No gene, source cache, runtime or prior history is edited.

The publisher passed eight project frontmatter checks, rendered both project
pages and validated the appended history record. The catalogue render reports
1,623 missing-review warnings; the progress render reports none.

[Curation session](https://github.com/ai4curation/ai-gene-review/blob/cmungall/clingen-tracker546-20261021/history/projects/CLINGEN_MENDELIAN/2026-10-21T180246Z-codex-d35b4c.yaml)
## Completion checkpoint 547 — 2026-10-21 18:55:39 UTC

**547 complete; 2,329 remaining out of 2,876 primary catalogue genes.**
This checkpoint adds only [EIF2B4 #5301](https://github.com/ai4curation/ai-gene-review/pull/5301)
to merged checkpoint 546. The coordinating AI agent accepted the complete
merge audit and terminal main addendum; this is not a human maintainer sign-off.
Products, follow-up PRs and tracker publications receive no additional credit.

Approved head [`566979dc1095`](https://github.com/ai4curation/ai-gene-review/commit/566979dc1095190b989461deecd3fd832e7bca5a)
merged at [`538ebfa38cf7`](https://github.com/ai4curation/ai-gene-review/commit/538ebfa38cf7bded4389af18fceab0fbccec61fa)
on 2026-10-21 at 18:28:09 UTC, with actual parent `31717524f1710d19c5f8b22c5418f37b9e08b6eb`.
All 19 approved paths, blobs and modes equal the complete merge delta and
remain exact on the pinned main snapshot. The current
[approval](https://github.com/ai4curation/ai-gene-review/pull/5301#pullrequestreview-5604007982)
and [detailed review](https://github.com/ai4curation/ai-gene-review/pull/5301#issuecomment-6322784586)
have no unresolved threads or blocking requests.

The actual [merge-group build](https://github.com/ai4curation/ai-gene-review/actions/runs/39650395859)
passed strict EIF2B4 validation, all gene-schema checks, 699 module checks,
14,900 history records, 42 history tests and 715 family checks. It actually ran
the full suite: 4,176 tests, 268 doctests, 12 examples, typing, lint, 432 automation
Python tests and 19 JavaScript tests passed. Skips, dependency warnings and an
ignored destructor error remain disclosed in the audit; the jobs succeeded.

The actual [main build](https://github.com/ai4curation/ai-gene-review/actions/runs/39652986406)
passed strict gene, history and family validation. Change filtering skipped the
general suite; the final test job checked upstream conclusions. Strict gene
validation retains 10 advisories: nine supported generic-binding policy warnings
and one inherited Falcon quotation mismatch. The existing quoted text was
preserved. The [documentation run](https://github.com/ai4curation/ai-gene-review/actions/runs/39652986498)
successfully built and deployed MkDocs, with navigation/dependency warnings.
This is not a claim of fresh gene HTML visual inspection.

The accepted review preserves 53 source objects: 49 active and four retired
contexts. Its actions are 21 ACCEPT, 13 MODIFY, 14 KEEP_AS_NON_CORE,
2 UNDECIDED and 3 MARK_AS_OVER_ANNOTATED. It records three natural products,
one core function and 57 inherited quotations; no new quotation was added.
Completion records accepted review delivery, with unresolved judgments visible.

This update starts from main `d2587858a920bf0ebb731c6c8e9cb74036c4d5db`. Its seven checkpoint-546
publication paths equal the approved payload of merged
[tracker #5316](https://github.com/ai4curation/ai-gene-review/pull/5316), merge `d2587858a920bf0ebb731c6c8e9cb74036c4d5db`.
All 235 historical queue objects and 106 previous completion updates remain
exact; this is update 107. Previous progress text remains byte-for-byte intact.
All 2,876 catalogue identities and association texts are unchanged; only the
EIF2B4 checkbox changes. The project instructions also document the standing
campaign convention of adding no new publication quotations, while preserving
inherited quotations and requiring verifiable sources and access limits.

The pinned inventory has 8,551 review files, including 3,110 human reviews.
1,253 catalogue genes have reviews and 1,623 lack them;
706 available catalogue reviews remain uncredited. Four source changes,
two generated project pages and one new append-only history record form the
publication scope. No gene, source cache, runtime or prior history is edited.

The publisher passed eight project frontmatter checks, rendered both project
pages and validated the appended history record. The catalogue render reports
1,623 missing-review warnings; the progress render reports none.

[Curation session](https://github.com/ai4curation/ai-gene-review/blob/cmungall/clingen-tracker547-20261021/history/projects/CLINGEN_MENDELIAN/2026-10-21T185556Z-codex-be2135.yaml)

## Completion checkpoint 549 — 2026-10-21 19:46:21 UTC

**549 complete; 2,327 remaining out of 2,876 primary catalogue genes.**
This checkpoint adds [EIF2S3 #5314](https://github.com/ai4curation/ai-gene-review/pull/5314)
and [EIF3F #5315](https://github.com/ai4curation/ai-gene-review/pull/5315) to merged checkpoint 547.
The coordinating AI agent accepted their merge audits; this is not a human
maintainer sign-off. Products, follow-ups and trackers receive no extra credit.

EIF2S3 approved head `d7140993c185a1dea61187562e05358af517377a` merged at `4d4b0ea1e8ede4bd5ce45128123c83b6d529ff39`
with actual parent `c5d0b8f3d69bb45714a85a7734651e317b93ece0`. All 31 approved paths, blobs and modes
match the actual merge delta and pinned main. The current formal approval and
detailed review remain unchanged with no unresolved threads. Its
[merge-group build](https://github.com/ai4curation/ai-gene-review/actions/runs/39656094067) ran
4,176 tests, 268 doctests, 12 examples, typing, lint and 432 Python/19 JavaScript
automation tests successfully. Its [actual main build](https://github.com/ai4curation/ai-gene-review/actions/runs/39659047032)
passed strict EIF2S3 validation, 14,905 history records, 42 history tests and 715
family checks. Main change filtering skipped the general suite. The 33 strict
advisories comprise 32 supported generic-binding warnings and one optional
propagation-metadata warning. Its [documentation run](https://github.com/ai4curation/ai-gene-review/actions/runs/39659046970)
built and deployed successfully. The review retains 81 sources from 82 raw
records, two cores, one 472-residue product and zero new quotations.

EIF3F approved head `18c2b74730af07e228e4f60ac58903e4075956e2` merged at `c5d0b8f3d69bb45714a85a7734651e317b93ece0`
with actual parent `d2587858a920bf0ebb731c6c8e9cb74036c4d5db`. All 29 approved paths, blobs and modes
match the actual merge delta and pinned main. Its formal approval and detailed
review remain unchanged with no unresolved threads. Its
[merge-group build](https://github.com/ai4curation/ai-gene-review/actions/runs/39655244958) passed
the same full test suite, strict EIF3F validation, 14,903 history records,
42 history tests and 715 family checks. Its [documentation run](https://github.com/ai4curation/ai-gene-review/actions/runs/39658205474)
built and deployed successfully.

EIF3F's [actual main run](https://github.com/ai4curation/ai-gene-review/actions/runs/39658205293)
was cancelled because a higher-priority main build was waiting. Strict EIF3F
validation passed with 49 supported generic-binding advisories and 14,903 history
records were checked, but the history pytest step was interrupted and the
aggregate failed. The general suite was filtered out. None of those incomplete
or skipped checks is reported as executed success.

The successful immediate EIF2S3 descendant preserves all 29 EIF3F payloads,
388 protected positions, 316 runtime pins and 14 complete validation-runtime
roots. This is the campaign's documented cancelled-main bridge convention;
it does not reclassify the cancelled run or claim that EIF2S3's strict step
revalidated EIF3F. EIF3F retains 119 sources: 30 ACCEPT, 36 MODIFY,
52 KEEP_AS_NON_CORE and one UNDECIDED; two cores, one 357-residue product and
zero new quotations. Review completion leaves that uncertainty visible.

This update starts from main `bf2af2d12324277c67537afb3e8f55cb96a21c57`. All seven predecessor tracker paths
match approved [tracker #5318](https://github.com/ai4curation/ai-gene-review/pull/5318), merge `bf2af2d12324277c67537afb3e8f55cb96a21c57`.
All 235 queue objects and 107 previous completion updates remain exact; this is
update 108. Previous progress text remains byte-for-byte intact. All 2,876
catalogue identities and association texts remain unchanged; only EIF2S3 and
EIF3F checkboxes change. The existing quotation convention now explicitly
attributes its authority to the user's standing instruction.

The pinned inventory has 8,553 reviews, including 3,112 human reviews.
1,255 catalogue genes have reviews; 1,621 lack them, and
706 available catalogue reviews remain uncredited. Three source files,
three generated files and one append-only history record form the publication
scope. No gene, source cache, runtime or previous history is edited.

The publisher passed eight project frontmatter checks, rendered both project
pages and validated the appended history record. The catalogue render reports
1,621 missing-review warnings; the progress render reports none.

[Curation session](https://github.com/ai4curation/ai-gene-review/blob/cmungall/clingen-tracker549-20261021/history/projects/CLINGEN_MENDELIAN/2026-10-21T194705Z-codex-08c9fb.yaml)

## Completion checkpoint 552 — 2026-10-21 22:15:21 UTC

**552 complete; 2,324 remaining out of 2,876 primary catalogue genes.**
This checkpoint adds ELAC2, ELF4 and ELANE to merged checkpoint 549.
The coordinating AI agent accepted their exact-head reviews and merge audits;
this is not a human maintainer sign-off. Products, follow-ups and tracker
publications receive no extra credit. ELN and ELOVL4 receive no credit here.

| Gene / PR | Approved head | Actual merge | Actual parent | Exact approved paths at merge |
| --- | --- | --- | --- | --- |
| [ELAC2 #5317](https://github.com/ai4curation/ai-gene-review/pull/5317) | [`75b47d953f5e`](https://github.com/ai4curation/ai-gene-review/commit/75b47d953f5e4bdc8fed2bcd3ba5f3ecb66272d9) | [`1abe4bf2c030`](https://github.com/ai4curation/ai-gene-review/commit/1abe4bf2c0309ac3bad7500e5ecb6701e7cfe344) | `0d5a010702a4` | 32/32 |
| [ELF4 #5321](https://github.com/ai4curation/ai-gene-review/pull/5321) | [`e1de9ec5ca9e`](https://github.com/ai4curation/ai-gene-review/commit/e1de9ec5ca9e2db9320596a3643819c74ff15270) | [`44cdc2dbe050`](https://github.com/ai4curation/ai-gene-review/commit/44cdc2dbe05063e8eae9eb3716464768704da817) | `1abe4bf2c030` | 25/26 |
| [ELANE #5320](https://github.com/ai4curation/ai-gene-review/pull/5320) | [`db127beeec42`](https://github.com/ai4curation/ai-gene-review/commit/db127beeec420bdbd587bb5dae419ae3eb6f1623) | [`cd7e12584376`](https://github.com/ai4curation/ai-gene-review/commit/cd7e12584376e4fff47f4e9b13d8bd20c967a7b6) | `44cdc2dbe050` | 51/52 |

ELAC2 preserves all 32 approved path modes/OIDs, including its 29 science
payloads. ELF4 preserves 25 of 26 paths exactly; its aggregate report contains
all 18 parent rows plus two exact ELF4 rows, for 20. Relative to its approved
18-row report, the two ELAC2 parent rows are retained. ELANE preserves 51 of
52 paths exactly; its aggregate contains all 20 parent rows plus its exact
query row, for 21. Relative to its approved 17-row report, four ELAC2/ELF4
parent rows are retained. These are explicit report-union exceptions, not
claims that every aggregate blob equals its approved head. All three merges'
other payloads remain exact at the pinned main, and all report records are preserved.

The accepted CI evidence is linked separately for each event:

- ELAC2: [merge group](https://github.com/ai4curation/ai-gene-review/actions/runs/39676861125), [actual main](https://github.com/ai4curation/ai-gene-review/actions/runs/39679097253) and [docs](https://github.com/ai4curation/ai-gene-review/actions/runs/39679097289).
- ELF4: [merge group](https://github.com/ai4curation/ai-gene-review/actions/runs/39678825030), [actual main](https://github.com/ai4curation/ai-gene-review/actions/runs/39681455350) and [docs](https://github.com/ai4curation/ai-gene-review/actions/runs/39681455419).
- ELANE: [merge group](https://github.com/ai4curation/ai-gene-review/actions/runs/39680202603), [actual main](https://github.com/ai4curation/ai-gene-review/actions/runs/39682864328) and [docs](https://github.com/ai4curation/ai-gene-review/actions/runs/39682864226).

All three merge groups passed the full suite: 4,176 Python tests (one skipped,
84 deselected), 268 doctests (37 skipped), 12 examples, typing, lint, 432
Python automation tests and 19 JavaScript tests. Their actual-main builds
passed scoped strict validation, history validation/tests and family checks;
the broad main suites were skipped by path filters. Aggregate jobs checked
job conclusions and did not execute these tests. ELAC2 retains one accepted
advisory; ELANE retains 11, including ten generic-binding policy warnings and
one source-specific exosome warning. The actual log governs that count even
though reviewer prose omitted the latter. Docs workflows built and pushed
gh-pages successfully; no independent live-page or pixel inspection is claimed.

The merged reviews retain ELAC2's 36 sources/four products/one core, ELF4's
42 sources/one product/one core and ELANE's 102 sources/one product/one core.
All add zero publication quotations. ELAC2 and ELANE keep computed DRAFT
status; ELF4 is COMPLETE. ELAC2 retains one UNDECIDED annotation, ELF4 four,
and ELANE five. Campaign completion records accepted merged
review work and does not relabel those uncertainties as resolved.

The baseline is main `cd7e12584376e4fff47f4e9b13d8bd20c967a7b6`. All seven predecessor tracker paths match approved
[tracker #5319](https://github.com/ai4curation/ai-gene-review/pull/5319), head `6749bce965d6f56e161bb620a9b5986d57495b42`
and actual merge `0d5a010702a4fcbf92209dc76eda9f22a8e1a81b`. All 235 queue objects and 108 prior completion
updates remain exact; this is update 109. Previous progress bytes and all
2,876 catalogue identities/association texts are preserved. Only ELAC2,
ELF4 and ELANE checkboxes change; the existing quotation convention is unchanged.

The pinned inventory contains 8,556 reviews, including 3,115 human reviews.
1,258 catalogue genes have files; 1,618 lack files and
706 available reviews remain uncredited. Three source files, the queue
mirror, two rendered pages and an append-only history record form the
publication scope. No gene, source cache, runtime or prior history is
changed by this tracker.
The publication passed eight project frontmatter checks, rendered both project
pages and validated the appended history record. The catalogue render reports
1,618 missing-review warnings; the progress render reports none.

[Curation session](https://github.com/ai4curation/ai-gene-review/blob/cmungall/clingen-tracker552-20261021/history/projects/CLINGEN_MENDELIAN/2026-10-21T223102Z-codex-2f1a51.yaml)

## Completion checkpoint 553 — 2026-10-21 23:25:39 UTC

**553 complete; 2,323 remaining out of 2,876 primary catalogue genes.**
This checkpoint adds only [ELN #5322](https://github.com/ai4curation/ai-gene-review/pull/5322)
to merged checkpoint 552. The coordinating AI agent accepted the exact-head
review and merge audit; this is not a human maintainer sign-off. Products,
follow-ups, private drafts and tracker publications add no credit.

| Gene / PR | Approved head | Actual merge | Actual parent | Exact approved paths at merge |
| --- | --- | --- | --- | --- |
| [ELN #5322](https://github.com/ai4curation/ai-gene-review/pull/5322) | [`2fd23fe02242`](https://github.com/ai4curation/ai-gene-review/commit/2fd23fe02242dc65c995cb869bfed64b9f76f23b) | [`c4275075822f`](https://github.com/ai4curation/ai-gene-review/commit/c4275075822f1cb9e9e28ae49b90090793bdf2f7) | `cd7e12584376` | 31/31 |

All 31 approved path modes and blobs match the actual ELN merge. Its aggregate
source-defect report preserves 21 parent records and adds one exact conditional
ELN/MGI query, for 22 records. The tracker successor changes no ELN payload.
The review preserves 48 source annotations and 13 natural products, with two
core functions and zero new publication quotations. Decisions are 9 ACCEPT,
17 MODIFY and 22 KEEP_AS_NON_CORE. Its computed status remains DRAFT with five
accepted advisories; completion does not suppress these qualifications.

The [merge-group build](https://github.com/ai4curation/ai-gene-review/actions/runs/39687733885)
executed the full suite: 4,176 Python tests (one skipped, 84 deselected),
268 doctests (37 skipped), 12 examples, typing, lint, 432 Python automation
tests and 19 JavaScript tests. The [actual-main build](https://github.com/ai4curation/ai-gene-review/actions/runs/39689841584)
passed strict gene validation, 14,915 history records, 42 history tests and
715 family checks. Its broad suite was filtered, not executed again.
Aggregate jobs checked conclusions rather than running these tests.
The [documentation workflow](https://github.com/ai4curation/ai-gene-review/actions/runs/39689841571)
built and pushed gh-pages successfully; no independent live-page inspection is claimed.

The pinned inventory at main `7f1f8f7147f165a688c45300b0da8052adfdadf1` contains 8,557 reviews, including 3,116
human reviews. Of the 2,876 catalogue genes, 1,259 have review files and 1,617
lack them; 706 available reviews remain uncredited. All seven predecessor
[tracker #5324](https://github.com/ai4curation/ai-gene-review/pull/5324) paths
match its approved head `797605851a52befe7c870379624d1a16b1ab0714` at the merge.
All 235 queue objects, 109 earlier completion updates and earlier progress
bytes remain exact. This is update 110; only the ELN checkbox changes, and all
2,876 catalogue identities and association texts are preserved.

Publication scope is three project sources, their queue mirror, two rendered
pages and a scaffolded append-only history record. It changes no gene review,
source cache, runtime or earlier history. ELOVL4 and ELP2 remain uncredited.
The publication passed eight project frontmatter checks, rendered both project
pages and validated the appended history record. The catalogue render reports
1,617 missing-review warnings; the progress render reports none.

[Curation session](https://github.com/ai4curation/ai-gene-review/blob/cmungall/clingen-tracker553-20261021/history/projects/CLINGEN_MENDELIAN/2026-10-21T232923Z-codex-8fec8a.yaml)

## Completion checkpoint 557 — 2026-10-24 06:14:02 UTC

**557 complete; 2,319 remaining out of 2,876 primary catalogue genes.**
This checkpoint adds four accepted merges to [checkpoint 553, tracker #5326](https://github.com/ai4curation/ai-gene-review/pull/5326).
The coordinating AI agent accepted the exact-head reviews and merge audits;
this is not a human maintainer sign-off. Products, follow-ups, private drafts
and tracker publications add no credit.

| Gene / PR | Approved head | Actual merge | Actual parent | Exact approved paths |
| --- | --- | --- | --- | --- |
| [ELP2 #5325](https://github.com/ai4curation/ai-gene-review/pull/5325) | [`21343d5f60e3`](https://github.com/ai4curation/ai-gene-review/commit/21343d5f60e3e9b1838d351339aa7793e838172c) | [`1a193ad5a9a8`](https://github.com/ai4curation/ai-gene-review/commit/1a193ad5a9a87357491e981d5abc3f615e39a139) | `eb83fa701eb9` | 20/20 |
| [ELOVL4 #5323](https://github.com/ai4curation/ai-gene-review/pull/5323) | [`9ed941653b45`](https://github.com/ai4curation/ai-gene-review/commit/9ed941653b4501e0bb98c1e51b52eab6318e7ab3) | [`f96d2abc07b1`](https://github.com/ai4curation/ai-gene-review/commit/f96d2abc07b18943f7c239622eff90a33dcfb3bc) | `1a193ad5a9a8` | 20/20 |
| [EML1 #5327](https://github.com/ai4curation/ai-gene-review/pull/5327) | [`b28e213dbe95`](https://github.com/ai4curation/ai-gene-review/commit/b28e213dbe95cb5c4638256e67c4ad94c43a8b5f) | [`02a780ad3cef`](https://github.com/ai4curation/ai-gene-review/commit/02a780ad3cef37a9ed984620990ee33b2650e4bc) | `f96d2abc07b1` | 19/19 |
| [EMILIN1 #5329](https://github.com/ai4curation/ai-gene-review/pull/5329) | [`3e2b4f91315b`](https://github.com/ai4curation/ai-gene-review/commit/3e2b4f91315b390e8c0ee73e93cf96137313362f) | [`83dcbe1d939d`](https://github.com/ai4curation/ai-gene-review/commit/83dcbe1d939d3a29daecb0e16145bdd29c339d3a) | `02a780ad3cef` | 29/29 |

All 88 approved path modes and Git objects match at the actual merges and
pinned main, including source caches, supporting material and histories.
The full gene directories also match. The reviews retain their imported
annotations and natural products; no new publication quotations were added.
ELOVL4's 32 inherited quotations remain preserved.

| Gene | Sources | Products | Cores | Decisions | Computed status |
| --- | ---: | ---: | ---: | --- | --- |
| ELP2 | 20 | 7 | 1 | 7 ACCEPT, 7 KEEP_AS_NON_CORE, 6 MODIFY | COMPLETE |
| ELOVL4 | 37 | 1 | 1 | 19 ACCEPT, 5 KEEP_AS_NON_CORE, 7 MODIFY, 2 REMOVE, 4 UNDECIDED | DRAFT |
| EML1 | 39 | 2 | 1 | 11 ACCEPT, 23 KEEP_AS_NON_CORE, 4 MODIFY, 1 UNDECIDED | DRAFT |
| EMILIN1 | 99 | 2 | 2 | 29 ACCEPT, 48 KEEP_AS_NON_CORE, 17 MODIFY, 1 REMOVE, 4 UNDECIDED | DRAFT |

Product counts include the displayed canonical protein when no alternative-product
list is present; ELOVL4 has one source-described 314-aa product.

ELOVL4 retains four unresolved annotations and two binding advisories; EML1
retains one unresolved annotation and eight binding advisories. EMILIN1 retains
four unresolved annotations and 24 advisories (22 binding, two propagation).
ELP2 has no gene-validation warnings. Accepted campaign completion does not
convert DRAFT files to COMPLETE or remove uncertainty.

Each accepted merge-group build executed 4,214 Python tests (one skipped,
84 deselected, nine warnings), 270 doctests (37 skipped, eight warnings),
12 examples, typing across 284 files, lint, 438 additional Python automation
tests and 19 JavaScript tests. The additional automation tests overlap the
broad suite and are not additive unique coverage. Validation executed 42 history
tests, scoped gene validation, all-gene schema checks, modules and families.
The all-gene check is schema-only; aggregate jobs report job conclusions.

Builds: [ELP2](https://github.com/ai4curation/ai-gene-review/actions/runs/40066991538), [ELOVL4](https://github.com/ai4curation/ai-gene-review/actions/runs/40066992452), [EML1](https://github.com/ai4curation/ai-gene-review/actions/runs/40066993531), [EMILIN1](https://github.com/ai4curation/ai-gene-review/actions/runs/40067208919).

The inventory at main `83dcbe1d939d3a29daecb0e16145bdd29c339d3a` contains 8,868 reviews,
including 3,196 human reviews. Of the 2,876 catalogue genes, 1,277
have review files and 1,599 lack them; 720 available reviews remain
uncredited. All 235 queue objects, 110 earlier completion updates and earlier
progress bytes are preserved. This is update 111; only four checkboxes change,
and all 2,876 catalogue identities and association texts remain exact.

Publication scope is three project sources, their queue mirror, two rendered
pages and a scaffolded append-only history record. ENG, ENPP1, ENTPD1 and EOGT
remain uncredited by this checkpoint. This checkpoint does not claim an
independent documentation build or live-page inspection for the four merges.

[Curation session](https://github.com/ai4curation/ai-gene-review/blob/cmungall/clingen-tracker557-20261024/history/projects/CLINGEN_MENDELIAN/2026-10-24T061743Z-codex-2fc9e5.yaml)

## Completion checkpoint 559 — 2026-10-24 07:08:59 UTC

**559 complete; 2,317 remaining out of 2,876 primary catalogue genes.**
This checkpoint adds ENG and ENPP1 to [merged checkpoint 557, tracker #5379](https://github.com/ai4curation/ai-gene-review/pull/5379).
The coordinating AI agent accepted the exact-head reviews and actual-merge audits;
this is not a human maintainer sign-off. Products, follow-ups, private drafts
and tracker publications add no credit.

| Gene / PR | Approved head | Actual merge | Actual parent | Exact approved paths |
| --- | --- | --- | --- | --- |
| [ENG #5374](https://github.com/ai4curation/ai-gene-review/pull/5374) | [`ca7bef2fb4fe`](https://github.com/ai4curation/ai-gene-review/commit/ca7bef2fb4feb301b2c20b8b951a5d9d6ff92db0) | [`eeb6b2ea3fe4`](https://github.com/ai4curation/ai-gene-review/commit/eeb6b2ea3fe4415887d3d7ff5fa358b0d922f6c9) | `83dcbe1d939d` | 41/41 |
| [ENPP1 #5377](https://github.com/ai4curation/ai-gene-review/pull/5377) | [`a3d10688e084`](https://github.com/ai4curation/ai-gene-review/commit/a3d10688e084920f2bec5c61e157332c6f9d0a44) | [`ec0663817767`](https://github.com/ai4curation/ai-gene-review/commit/ec0663817767fc39466497bdb2ebe9fd21391e21) | `eeb6b2ea3fe4` | 32/32 |

All 73 approved file objects and modes, including normal caches and histories,
match the actual merges and pinned main. Complete gene directories also match.
Imported annotation contexts and source-described natural products are preserved;
no new publication quotations were added. ENPP1 has one displayed canonical
product because the source does not enumerate alternative products; this is not
a claim that no other transcript exists.

| Gene | Sources | Products | Cores | Decisions | Computed status | Advisories |
| --- | ---: | ---: | ---: | --- | --- | ---: |
| ENG | 104 | 2 | 2 | 29 ACCEPT, 59 KEEP_AS_NON_CORE, 2 MARK_AS_OVER_ANNOTATED, 4 MODIFY, 10 UNDECIDED | DRAFT | 13 |
| ENPP1 | 97 | 1 | 2 | 39 ACCEPT, 20 KEEP_AS_NON_CORE, 6 MARK_AS_OVER_ANNOTATED, 11 MODIFY, 21 UNDECIDED | DRAFT | 6 |

ENG retains ten unresolved annotations and 13 advisories: eleven generic binding,
one source-action split and one CI ontology-label lag. ENPP1 retains 21 unresolved
annotations and six advisories: one generic binding, three propagation-metadata
and two source-action splits. Accepted campaign completion does not convert
DRAFT files to COMPLETE or remove uncertainty.

Each actual merge-group suite ran 4,214 Python tests (one skipped, 84 deselected,
nine warnings), 270 doctests (37 skipped, eight warnings), 12 examples, mypy on 284
files, Ruff, 438 overlapping Python automation tests and 19 JavaScript tests.
Validation included scoped gene checks, all-gene schema checks, 703 modules,
718 families and 42 history tests. History-record totals were 15,627 for ENG and
15,629 for ENPP1. Global advisories and skipped steps remain documented; the
ignored post-pytest SQLAlchemy destructor diagnostic did not fail either job.
The all-gene check is schema-only; aggregate jobs report job conclusions.

Builds: [ENG](https://github.com/ai4curation/ai-gene-review/actions/runs/40068917287), [ENPP1](https://github.com/ai4curation/ai-gene-review/actions/runs/40070735296).

At main `04f1f31db8f36ff1bed22c0e5ff8220567c219ce`, the inventory contains 8,870 reviews,
including 3,198 human reviews. Of 2,876 catalogue genes, 1,279 have
review files and 1,597 lack them; 720 available reviews remain uncredited.
All 235 queue objects, 111 earlier completion updates and earlier progress bytes
are preserved. This is update 112; only the ENG and ENPP1 checkboxes change,
and all 2,876 catalogue identities and association texts remain exact.

Publication scope is three project sources, their queue mirror, two rendered
pages and a scaffolded append-only history record. EOGT, ENTPD1 and EP300 remain
uncredited by this checkpoint. No independent documentation build or live-page
inspection for these gene merges is claimed.

[Curation session](https://github.com/ai4curation/ai-gene-review/blob/cmungall/clingen-tracker559-20261024/history/projects/CLINGEN_MENDELIAN/2026-10-24T071001Z-codex-768730.yaml)

## Completion checkpoint 561 — 2026-10-24 07:51:14 UTC

**561 complete; 2,315 remaining out of 2,876 primary catalogue genes.**
This checkpoint adds EOGT and ENTPD1 to [merged checkpoint 559, tracker #5382](https://github.com/ai4curation/ai-gene-review/pull/5382).
The coordinating AI agent accepted the exact-head reviews and actual-merge audits;
this is not a human maintainer sign-off. Products, follow-ups, private drafts
and tracker publications add no credit.

| Gene / PR | Approved head | Actual merge | Actual parent | Exact approved paths |
| --- | --- | --- | --- | --- |
| [EOGT #5381](https://github.com/ai4curation/ai-gene-review/pull/5381) | [`70677246ec7e`](https://github.com/ai4curation/ai-gene-review/commit/70677246ec7e7ccc176372dd9ba4bab69200bc98) | [`bc777faa7a96`](https://github.com/ai4curation/ai-gene-review/commit/bc777faa7a968fa182d20c6ff4264cf398a18f33) | `04f1f31db8f3` | 22/22 |
| [ENTPD1 #5380](https://github.com/ai4curation/ai-gene-review/pull/5380) | [`536ec2d369d3`](https://github.com/ai4curation/ai-gene-review/commit/536ec2d369d34706376b50ceed13a4435f48127e) | [`9ba348f4516c`](https://github.com/ai4curation/ai-gene-review/commit/9ba348f4516cf6f675880116ac3060f7a54a8b59) | `bc777faa7a96` | 33/33 |

All 55 approved file objects and modes, including normal caches and histories,
match the actual merges and pinned main. Complete gene directories also match.
Imported annotation contexts and source-described natural products are preserved;
no new publication quotations were added.

| Gene | Annotation rows | Products | Cores | Decisions | Computed status | Advisories |
| --- | ---: | ---: | ---: | --- | --- | ---: |
| EOGT | 8 | 3 | 1 | 7 ACCEPT, 1 MODIFY | COMPLETE | 0 |
| ENTPD1 | 70 | 6 | 1 | 53 ACCEPT, 3 KEEP_AS_NON_CORE, 8 MODIFY, 1 REMOVE, 5 UNDECIDED | DRAFT | 4 |

EOGT retains eight reviewed annotation rows, three source-described products and
one core function, with COMPLETE status and no validation warnings. ENTPD1 retains
70 reviewed annotation rows, six products, one core function and five unresolved
annotations. Its four actual CI advisories comprise one generic-binding warning,
one UDP-annotation action split and two stale-exception warnings. The latter reflect
the validator's exception matching; they were not erased by the approving review.
Accepted campaign completion does not convert ENTPD1 from DRAFT to COMPLETE.

Each actual merge-group suite ran 4,214 Python tests (one skipped, 84 deselected,
nine warnings), 270 doctests (37 skipped, eight warnings), 12 examples, mypy on 284
files, Ruff, 438 overlapping Python automation tests and 19 JavaScript tests.
Validation included scoped gene checks, all-gene schema checks, 703 modules,
718 families and 42 history tests. History-record totals were 15,632 for EOGT and
15,634 for ENTPD1. Global advisories and skipped steps remain documented; the
ignored post-pytest SQLAlchemy destructor diagnostic did not fail either job.
The all-gene check is schema-only; aggregate jobs report job conclusions.

Builds: [EOGT](https://github.com/ai4curation/ai-gene-review/actions/runs/40072822896), [ENTPD1](https://github.com/ai4curation/ai-gene-review/actions/runs/40073130021).

At main `273712aad3cb515aa95f60294a37dff884258011`, the inventory contains 8,872 reviews,
including 3,200 human reviews. Of 2,876 catalogue genes, 1,281 have
review files and 1,595 lack them; 720 available reviews remain uncredited.
All 235 queue objects, 112 earlier completion updates and earlier progress bytes
are preserved. This is update 113; only the EOGT and ENTPD1 checkboxes change,
and all 2,876 catalogue identities and association texts remain exact.

Publication scope is three project sources, their queue mirror, two rendered
pages and a scaffolded append-only history record. EP300 and EPCAM remain
uncredited by this checkpoint. No independent documentation build or live-page
inspection for these gene merges is claimed.

[Curation session](https://github.com/ai4curation/ai-gene-review/blob/cmungall/clingen-tracker561-20261024/history/projects/CLINGEN_MENDELIAN/2026-10-24T075154Z-codex-6ed544.yaml)

## Completion checkpoint 563 — 2026-10-24 09:38:44 UTC

**563 complete; 2,313 remaining out of 2,876 primary catalogue genes.**
This checkpoint adds only EP300 and EPCAM to [merged checkpoint 561, tracker #5383](https://github.com/ai4curation/ai-gene-review/pull/5383).
The coordinating AI agent accepted both exact-head reviews and independent actual-merge
audits; this is not a human maintainer sign-off. Products, follow-ups, private drafts
and tracker publications add no credit. EP300 was accepted as gene 562 and EPCAM
as gene 563; both are recorded together in this publication update.

| Gene / PR | Approved head | Actual merge | Actual parent | Exact approved paths |
| --- | --- | --- | --- | --- |
| [EP300 #5384](https://github.com/ai4curation/ai-gene-review/pull/5384) | [`7b5643c079a0`](https://github.com/ai4curation/ai-gene-review/commit/7b5643c079a0e391193da1e2a3d1dcd5971f604a) | [`cb6bb5ec57f8`](https://github.com/ai4curation/ai-gene-review/commit/cb6bb5ec57f815572bee8e519c8101ad91b0070e) | `7293c5a1c39e` | 90/90 |
| [EPCAM #5385](https://github.com/ai4curation/ai-gene-review/pull/5385) | [`fe9ed9ed05ca`](https://github.com/ai4curation/ai-gene-review/commit/fe9ed9ed05ca1dfbedaaf2cd3ee1eb3c8aeff6be) | [`5cc22e30227e`](https://github.com/ai4curation/ai-gene-review/commit/5cc22e30227e8948cc5f800b9e91213750e533ea) | `cb6bb5ec57f8` | 24/24 |

All approved paths match in mode, object type and blob ID at their approved heads,
actual merges and pinned main. Each complete five-file gene directory also matches.
Imported annotation contexts, normal source caches and displayed protein products
are preserved. No new publication quotations were added.

EP300 retains 471 reviewed annotations: 218 ACCEPT, 115 MODIFY,
115 KEEP_AS_NON_CORE and 23 UNDECIDED. Its two core functions are distinct from
its one displayed canonical protein product, Q09472 (2,414 residues). EPCAM retains
40 reviewed annotations: 15 ACCEPT, 16 KEEP_AS_NON_CORE, four MODIFY and five
UNDECIDED. It has one core function and one displayed canonical product, P16422
(314 residues). Neither committed review or UniProt record lists alternative
products. EPCAM's released EpEX/EpICD fragments are not counted as splice products.
Accepted completion preserves both DRAFT statuses and unresolved questions.

[EP300 merge-group Build and test run 40079507159](https://github.com/ai4curation/ai-gene-review/actions/runs/40079507159)
and [EPCAM run 40081006893](https://github.com/ai4curation/ai-gene-review/actions/runs/40081006893)
each completed all three jobs successfully before their respective merges at
2026-10-24T09:09:21Z and 2026-10-24T09:31:30Z. Each suite executed 4,239 Python
tests (one skipped, 84 deselected, nine warnings), 275 doctests (37 skipped, eight
warnings), 12 examples, mypy on 285 files, Ruff, 438 overlapping Python automation
tests and 19 JavaScript tests. Aggregate dependency gates did not execute additional
suites. Counts overlap and are not summed as unique tests.

Changed-gene validation actually ran in each run. EP300 passed with 48 advisories:
42 generic-binding policy warnings and six source-specific action-consistency
warnings. EPCAM passed with four generic-binding policy advisories. The separate
all-gene batches were schema-only. Both runs also checked 703 modules and 718
families; EP300 checked 15,640 history records and EPCAM checked 15,643, each followed
by 42 history tests. Ignored post-pytest oaklib/SQLAlchemy destructor diagnostics
did not fail the jobs. Prediction-review, BioReason/GO-GPT, prediction-upload,
curation-history-coverage, sequence-save and full-run upstream PAINT checks were
skipped; the captured job steps distinguish these from executed checks. No
independent actual-main scientific validation or documentation build is claimed.

At fixed main `5cc22e30227e8948cc5f800b9e91213750e533ea`, there are 8,874 reviews,
including 3,202 human reviews. Of 2,876 catalogue genes, 1,283 have review
files and 1,593 lack them; 720 available reviews remain uncredited.
All 235 queue objects, 113 earlier completion updates and earlier progress bytes
are preserved. This is update 114; only EP300 and EPCAM checkboxes change, and all
2,876 catalogue identities and association texts remain exact.

This checkpoint updates three project sources, their queue mirror and two rendered
pages. The append-only curation history is linked below.

[Curation session](https://github.com/ai4curation/ai-gene-review/blob/cmungall/clingen-tracker563-20261024/history/projects/CLINGEN_MENDELIAN/2026-10-24T094406Z-codex-ddcd2b.yaml)

## Completion checkpoint 566 — 2026-10-24 10:52:05 UTC

**566 complete; 2,310 remaining out of 2,876 primary catalogue genes.**
This checkpoint adds only EPHB4, EPG5 and EPM2A to [merged checkpoint 563, tracker #5389](https://github.com/ai4curation/ai-gene-review/pull/5389).
The coordinating AI agent accepted all three exact-head reviews and independent
actual-merge audits; this is not a human maintainer sign-off. EPHB4 was accepted
as gene 564, EPG5 as gene 565 and EPM2A as gene 566. Products, follow-ups, private
drafts, queued work and tracker publications add no credit. ERCC2 is not included.

| Gene / PR | Approved head | Actual merge | Actual parent | Exact approved paths |
| --- | --- | --- | --- | --- |
| [EPHB4 #5387](https://github.com/ai4curation/ai-gene-review/pull/5387) | [`8545c5a11968`](https://github.com/ai4curation/ai-gene-review/commit/8545c5a11968bfc066943ddd1fc5a1871dd00efd) | [`cbc176846687`](https://github.com/ai4curation/ai-gene-review/commit/cbc17684668719d61014b39606d5a54f858e6a77) | `5cc22e30227e` | 19/19 |
| [EPG5 #5386](https://github.com/ai4curation/ai-gene-review/pull/5386) | [`f7a58aaa3629`](https://github.com/ai4curation/ai-gene-review/commit/f7a58aaa3629f9b909696a1f5af95581ce39e8cf) | [`775e51508889`](https://github.com/ai4curation/ai-gene-review/commit/775e515088898ce6a5d947e856e1c5fedcc51a6a) | `cbc176846687` | 9/9 |
| [EPM2A #5388](https://github.com/ai4curation/ai-gene-review/pull/5388) | [`cf1b24450a65`](https://github.com/ai4curation/ai-gene-review/commit/cf1b24450a65162be6a4ef7c27873c0b993d7f80) | [`671b48213218`](https://github.com/ai4curation/ai-gene-review/commit/671b48213218d1c94a959a01e7dbf768ee4d8bfc) | `775e51508889` | 46/46 |

All approved paths match in mode, object type and blob ID at their approved heads,
actual merges and pinned main. Complete gene directories also match: five EPHB4,
six EPG5 and five EPM2A files. The accepted audits verify 53, eight and 46 published
normal-source dependencies, respectively. Imported annotation contexts, historical
records, normal caches and distinct source-described products are preserved.
No new publication quotations were added.

EPHB4 retains 76 imported annotation records: 46 ACCEPT, 22 MODIFY and eight
UNDECIDED. It has one core function and COMPLETE status with no CI advisories;
COMPLETE does not erase its eight unresolved records. Its four source-described
products remain distinct: P54760-1 (987 residues), P54760-2 (516), P54760-3 (306)
and P54760-4 (414). Their shared activity is not assumed.

EPG5 retains 16 total records, comprising 12 imported contexts, three historical
proposal contexts and one newly proposed record. Fifteen are active and one
historical UNDECIDED record remains retired. Total actions are three ACCEPT,
four MODIFY, four KEEP_AS_NON_CORE, two UNDECIDED and three NEW; active actions
exclude the one retired UNDECIDED. All 33 inherited publication quotation values
and their paths remain exact. The two distinct products, Q9HCE0-1 (2,579 residues)
and Q9HCE0-2 (2,481), and two core functions remain explicit. The review is DRAFT
with one generic-binding CI advisory.

EPM2A retains 81 imported O95278 annotation contexts: 31 ACCEPT,
17 KEEP_AS_NON_CORE, 19 MODIFY, 11 UNDECIDED, two MARK_AS_OVER_ANNOTATED and one
REMOVE. It has 48 references, two core functions and DRAFT status. Three CI
advisories concern action consistency for nucleus, endoplasmic-reticulum membrane
and protein dephosphorylation. Seven O95278 products retain lengths 331, 317,
152, 224, 88, 177 and 193 residues (products 1, 2, 4, 5, 6, 7 and 8). The eighth,
external B3EWF7-1, is independently sourced at 344 residues; its four GO assertions
remain separate from the 81 O95278 contexts. No activity equivalence is inferred.
The accepted audit also preserves all 50 private normal-publication cache
preimages; only the 33 cited publication caches are public dependencies. There
are no new annotations or publication quotations in this EPM2A review.

[EPHB4 merge-group Build and test run 40082869200](https://github.com/ai4curation/ai-gene-review/actions/runs/40082869200),
[EPG5 run 40084288443](https://github.com/ai4curation/ai-gene-review/actions/runs/40084288443)
and [EPM2A run 40084842231](https://github.com/ai4curation/ai-gene-review/actions/runs/40084842231)
each completed all three jobs successfully before their respective actual merges
at 2026-10-24T10:02:23Z, 2026-10-24T10:21:55Z and 2026-10-24T10:37:48Z.
Each suite executed 4,239 Python tests (one skipped, 84 deselected, nine warnings),
275 doctests (37 skipped, eight warnings), 12 examples, mypy on 285 files, Ruff,
438 overlapping Python automation tests and 19 JavaScript tests. Aggregate
dependency gates did not execute additional suites. Counts overlap and are not
summed as unique tests.

Changed-gene validation actually ran in all three runs. EPHB4 passed with no
advisories, EPG5 with one and EPM2A with three. The separate all-gene batches were
schema-only. Each run also checked 703 modules, 718 families and 42 history tests;
the history-record counts were 15,645, 15,648 and 15,650, respectively. Ignored
post-pytest oaklib/SQLAlchemy destructor diagnostics did not fail the jobs.
Prediction-review, BioReason/GO-GPT, prediction-upload, curation-history-coverage,
sequence-save and full-run upstream PAINT checks were skipped; captured job steps
distinguish these from executed checks. No independent actual-main scientific
validation or documentation build is claimed.

At fixed main `fcbef68494c3bd156a9c3625ae37de0a9f5df27c`, there are 8,876 reviews,
including 3,204 human reviews. Of 2,876 catalogue genes, 1,285 have review
files and 1,591 lack them; 719 available reviews remain uncredited.
All 235 queue objects, 114 earlier completion updates and earlier progress bytes
are preserved. This is update 115; only EPHB4, EPG5 and EPM2A checkboxes change,
and all 2,876 catalogue identities and association texts remain exact.

[Curation session](https://github.com/ai4curation/ai-gene-review/blob/cmungall/clingen-tracker566-20261024/history/projects/CLINGEN_MENDELIAN/2026-10-24T105619Z-codex-5b4d98.yaml)

## Completion checkpoint 570 — 2026-10-24 14:30:02 UTC

**570 complete; 2,306 remaining out of 2,876 primary catalogue genes.**
This adds only ERCC2, ERCC3, ERCC4 and ERCC5 to the
[merged 566 tracker, PR #5391](https://github.com/ai4curation/ai-gene-review/pull/5391).
Each has an exact-head approval and an independently accepted actual-merge audit.
Acceptance by the coordinating AI agent is not a human maintainer sign-off.
Products, follow-ups and tracker publications do not add gene credit. ERCC6 and
ERCC6L2 remain uncredited here.

| Gene / PR | Approved head | Actual merge | Merged at (UTC) | Approved paths |
| --- | --- | --- | --- | --- |
| [ERCC2 #5390](https://github.com/ai4curation/ai-gene-review/pull/5390) | [`965e844b78cb`](https://github.com/ai4curation/ai-gene-review/commit/965e844b78cbb86685a1586c46b7fb10e443b0e0) | [`41adae91d2e7`](https://github.com/ai4curation/ai-gene-review/commit/41adae91d2e786e57182400041738a653db90c26) | 2026-10-24T11:04:03Z | 24 |
| [ERCC3 #5392](https://github.com/ai4curation/ai-gene-review/pull/5392) | [`6b2d97d944ad`](https://github.com/ai4curation/ai-gene-review/commit/6b2d97d944ad38fead65429bcc695270fab44f26) | [`b60f053738c4`](https://github.com/ai4curation/ai-gene-review/commit/b60f053738c48d7fcaa0e2f651a5ee8f73149611) | 2026-10-24T12:17:42Z | 23 |
| [ERCC4 #5393](https://github.com/ai4curation/ai-gene-review/pull/5393) | [`451ee1dc76a7`](https://github.com/ai4curation/ai-gene-review/commit/451ee1dc76a7de97bc7043933911a0c6984eaef5) | [`d6debbce31dd`](https://github.com/ai4curation/ai-gene-review/commit/d6debbce31ddd59d0bd5931218389d821e33641a) | 2026-10-24T13:38:28Z | 10 |
| [ERCC5 #5396](https://github.com/ai4curation/ai-gene-review/pull/5396) | [`a038096b703e`](https://github.com/ai4curation/ai-gene-review/commit/a038096b703e4a33aa0ae23b498f86ffbd84efb9) | [`e7236877cf14`](https://github.com/ai4curation/ai-gene-review/commit/e7236877cf14aa3343182f032eb225f15ed4efe4) | 2026-10-24T14:00:39Z | 25 |

All 82 approved paths match in mode, type and blob at approved head, actual merge
and pinned main `e7236877cf14aa3343182f032eb225f15ed4efe4`. The complete ERCC2/3/4/5 gene
directories also match (six, six, seven and six files), with 102, 112, 48 and 35
normal-source dependencies verified in the accepted audits. ERCC4 has ten PR paths
but nine net merge changes because PMID:22323595 was already present on its parent.
Actual merge times come from GitHub merge metadata, not queue-commit timestamps.

ERCC2 retains 151 contexts, 109 references, two products (760 and 405 residues)
and two cores. Its actions are 97 ACCEPT, 22 MODIFY, 21 KEEP_AS_NON_CORE,
ten UNDECIDED and one MARK_AS_OVER_ANNOTATED. Measured ATP hydrolysis remains
separate from directional helicase activity; the scaffold role does not imply
an additional catalytic activity.

ERCC3 retains 162 contexts, 118 references, one displayed 782-residue product and
two cores. Actions are 93 ACCEPT, 14 MODIFY, 45 KEEP_AS_NON_CORE, eight UNDECIDED
and two MARK_AS_OVER_ANNOTATED. The principal DNA-translocation role and measured
ATP hydrolysis remain explicit; historical unwinding assays retain their bounded
non-core interpretation.

ERCC4 retains 97 records: 96 active imported contexts plus one retired historical
proposal. Its 100 genuine refreshed GOA rows reconcile to those 96 imported
contexts; the legacy UniProt and provider files remain unchanged. Actions are
45 ACCEPT, 32 KEEP_AS_NON_CORE, 12 MODIFY, six UNDECIDED, one REMOVE and one retired
TOO_GENERAL. The 55 references, two products (916 and 372 residues), two contextual
nuclease core units, negated source assertion and all 52 inherited quotation paths
remain preserved. The two core units describe contexts of the same enzyme.

ERCC5 retains 77 contexts, 41 references, three products (1,186, 419 and 232
residues) and one core. Actions are 35 ACCEPT, 20 MODIFY, 13 KEEP_AS_NON_CORE,
eight UNDECIDED and one TOO_GENERAL. No shared activity is assumed among the
natural products. None of these four publications adds a new annotation or a new
publication quotation.

All four reviews remain DRAFT. Their successful changed-gene validations retain
18, 34, 22 and five advisories: respectively 17, 33, 21 and four supported
generic-binding warnings, plus one research/provider-citation advisory per gene.
These warnings and unresolved annotations are not erased by completion credit.

| Actual merge-group run | Broad Python tests passed | Doctests passed | Gene advisories | History records |
| --- | --- | --- | --- | --- |
| [ERCC2 run 40087008874](https://github.com/ai4curation/ai-gene-review/actions/runs/40087008874) | 4,239 | 275 | 18 | 15,653 |
| [ERCC3 run 40092038098](https://github.com/ai4curation/ai-gene-review/actions/runs/40092038098) | 4,239 | 275 | 34 | 15,656 |
| [ERCC4 run 40097532447](https://github.com/ai4curation/ai-gene-review/actions/runs/40097532447) | 4,245 | 276 | 22 | 15,667 |
| [ERCC5 run 40099095412](https://github.com/ai4curation/ai-gene-review/actions/runs/40099095412) | 4,245 | 276 | 5 | 15,669 |

All three jobs in each merge-group run completed successfully. Each run also
executed 12 examples, 438 overlapping automation tests, 19 JavaScript tests,
mypy on 285 source files and two Ruff commands. Broad pytest had one skipped,
84 deselected and nine warnings; doctests had 37 skipped and eight warnings.
Counts overlap and are not summed. Changed-gene validation ran; the separate
all-gene batch was schema-only. Each run checked 703 module schemas, 718 family
schemas and 42 history tests. The aggregate dependency gate added no suite.
An ignored destructor diagnostic did not fail the runs.

The PR broad suites were skipped by path filtering; their success labels alone
are not broad-test evidence. Prediction/BioReason checks, prediction evidence
upload, curation-history coverage, sequence-save and full-run upstream PAINT
steps were skipped in the captured merge workflows. No independent actual-main
scientific validation or documentation build is claimed by this update.

All 2,876 catalogue identities and association text, 235 queue objects, 115 earlier
completion updates and preceding progress bytes remain exact. This is update 116;
only the four named checkboxes change. Source inventories and dated availability
snapshots are preserved without a fresh availability recount. The append-only history was scaffolded and validated through the normal repository commands; both project pages were regenerated.

[Curation session](https://github.com/ai4curation/ai-gene-review/blob/cmungall/clingen-tracker570-20261024/history/projects/CLINGEN_MENDELIAN/2026-10-24T144924Z-codex-9e8160.yaml)

## Completion checkpoint 574 — 2026-10-24 17:14:26 UTC

**574 complete; 2,302 remaining out of 2,876 primary catalogue genes.**
This adds only ERCC6, ERCC6L2, ERCC8 and ERF to the
[merged 570 tracker, PR #5409](https://github.com/ai4curation/ai-gene-review/pull/5409).
Each has an exact-head approval and an independently accepted actual-merge audit.
Acceptance by the coordinating AI agent is not a human maintainer sign-off.
Products, fusion siblings, follow-ups and tracker publications do not add gene
credit. ERLIN1 and ERLIN2 remain uncredited here.

| Gene / PR | Approved head | Actual merge | Merged at (UTC) | Approved path entries |
| --- | --- | --- | --- | --- |
| [ERCC6 #5401](https://github.com/ai4curation/ai-gene-review/pull/5401) | [`698d023e16e8`](https://github.com/ai4curation/ai-gene-review/commit/698d023e16e81509a69159c5b5845b844002ad2a) | [`8dd02fff434c`](https://github.com/ai4curation/ai-gene-review/commit/8dd02fff434c025d5b6e02b35e030e0e0c8e6ea5) | 2026-10-24T15:16:17Z | 51 |
| [ERCC6L2 #5405](https://github.com/ai4curation/ai-gene-review/pull/5405) | [`97d48ec2383b`](https://github.com/ai4curation/ai-gene-review/commit/97d48ec2383b3c86d26b8229c4d0355b8408041c) | [`b28805f7842b`](https://github.com/ai4curation/ai-gene-review/commit/b28805f7842b33a261c3aa2be33168b1ead3c084) | 2026-10-24T16:48:20Z | 14 |
| [ERCC8 #5408](https://github.com/ai4curation/ai-gene-review/pull/5408) | [`0d421ad2bf24`](https://github.com/ai4curation/ai-gene-review/commit/0d421ad2bf243988b071896f15a8afbd4e3ca846) | [`e5a60e057d21`](https://github.com/ai4curation/ai-gene-review/commit/e5a60e057d21c19eb0b92e4e93993f57df609790) | 2026-10-24T16:51:32Z | 17 |
| [ERF #5411](https://github.com/ai4curation/ai-gene-review/pull/5411) | [`243b49524eda`](https://github.com/ai4curation/ai-gene-review/commit/243b49524eda63cce0159451616a09193098b855) | [`a98198438715`](https://github.com/ai4curation/ai-gene-review/commit/a9819843871530062eb4b2878778b5bdd778e6b9) | 2026-10-24T16:59:30Z | 13 |

Approved-head and actual-merge payloads match for all 95 path entries across the
four PRs. Complete gene directories (11 ERCC6/cognate fusion files, five ERCC6L2,
five ERCC8 and six ERF) retain exact mode/type/blob parity at fixed main
`a9819843871530062eb4b2878778b5bdd778e6b9`. Normal-dependency comparisons cover 70, ten,
39 and nine external paths respectively. These counts overlap across genes.
ERCC6 has 51 PR paths but 50 net merge changes because PMID:16246722 was already
present on its parent; ERCC6L2 has 14 PR paths but 12 net changes because the two
PTHR45629 files already matched its parent. ERCC8 has 17 net changes, including
one accepted publication refresh; ERF has 13 additions.

One historical source blob is deliberately superseded on this fixed main:
ERCC6's abstract-only PMID:26620705 was replaced by the accepted ERCC8 genuine
full-text record. The original body remains an exact prefix, with only the
availability/extraction metadata changed and the original text appended.
The current blob exactly matches the ERCC8 approved head and actual merge;
every other selected gene/dependency blob retains its prior accepted content.
The later remote-main observation `a5be4091f08c69c7238275dd2200e4aaf474e1a8` is recorded as an
observation, not as a second payload-parity cut.

ERCC6 retains 139 primary contexts (53 ACCEPT, 21 MODIFY, 61 KEEP_AS_NON_CORE,
four UNDECIDED), 62 references and four core activity units. The 1,493-residue
CSB and external 1,061-residue CSB-PGBD3 product remain distinct. The validated
ERCC6__P0DP91 sibling separately retains all 11 fusion contexts, including literal
extension groups/partner identifiers, four references and no core. Its three
ACCEPT, five KEEP_AS_NON_CORE and three UNDECIDED assessments do not imply that
the fusion inherits the CSB motor. Its three product records include external
cross-references to CSB and PGBD3, not three extra ERCC6 gene credits. Both reviews
remain DRAFT, with 44 and three advisories respectively.

ERCC6L2 retains 24 imported contexts plus one accepted NEW DNA-helicase activity
annotation specifically on the experimentally tested Q5T890-1 product. Its 25
assessments are nine ACCEPT, two MODIFY, eight KEEP_AS_NON_CORE, five UNDECIDED
and one NEW, with 13 references and one core. The source-described 1,561-, 1,550-
and 712-residue products remain distinct. The ATP-dependent unwinding component
is bounded to the tested short-overhang/substrate and SSB conditions; residual
melting and the unresolved link to repair contexts remain explicit. DRAFT retains
four binding advisories; the NEW assertion was justified by the measured activity,
not by warning removal.

ERCC8 retains 77 source contexts, 43 references, distinct 396- and 205-residue
products and one substrate-adaptor core. Actions are 45 ACCEPT, 12 MODIFY,
17 KEEP_AS_NON_CORE and three UNDECIDED. Ligase substrate recruitment is separated
from RBX1 catalytic machinery and the CSB motor, with species and experimental
assembly boundaries retained. It remains DRAFT with five generic-binding
advisories.

ERF retains 24 source contexts, 15 references, distinct 548- and 473-residue
products and one chromatin-localized transcriptional-repression core. Actions
are eight ACCEPT, 11 MODIFY and five KEEP_AS_NON_CORE. Promoter-specific DNA
recognition remains distinct from the HT-SELEX naked-DNA motif assay; bounded
TLE5/AES-2 binding does not imply an assayed recruitment mechanism. DRAFT retains
five advisories: three generic-binding, one deliberate source-specific action
split, and one unused manual-research-reference warning.

None of these publications adds a supporting-text quotation. Source contexts,
natural product boundaries and unresolved judgments remain part of the accepted
records; completion credit does not imply every annotation is resolved.

| Actual merge-group run | Broad Python tests passed | Doctests passed | Gene advisories | History records |
| --- | --- | --- | --- | --- |
| [ERCC6 run 40104791174](https://github.com/ai4curation/ai-gene-review/actions/runs/40104791174) | 4,245 | 276 | 44 + 3 fusion | 15,675 |
| [ERCC6L2 run 40110584409](https://github.com/ai4curation/ai-gene-review/actions/runs/40110584409) | 4,245 | 276 | 4 | 15,683 |
| [ERCC8 run 40110626350](https://github.com/ai4curation/ai-gene-review/actions/runs/40110626350) | 4,245 | 276 | 5 | 15,688 |
| [ERF run 40112161497](https://github.com/ai4curation/ai-gene-review/actions/runs/40112161497) | 4,245 | 276 | 5 | 15,691 |

All three jobs in each actual merge-group run completed successfully. Each run
executed 12 examples, 438 overlapping automation tests, 19 JavaScript tests,
mypy on 285 source files and two Ruff commands. Broad pytest had one skipped,
84 deselected and nine warnings; doctests had 37 skipped and eight warnings.
Counts overlap and are not summed. Changed-gene validation ran (two reviews for
ERCC6); the separate all-gene batch was schema-only. Each run checked 703 module
schemas, 718 family schemas and 42 history tests. The aggregate gate added no
suite. The PR broad suites were skipped by path filtering, so their successful
labels alone are not broad-test evidence. Prediction and upstream PAINT checks
were skipped in these captured merge workflows.

ERF's saved API response reports completed/SUCCESS jobs while five nested suite
steps still have pending/in-progress states and the gate has no step array.
A bounded direct-job recheck resolved the validation steps but retained these
metadata limits. Full terminal logs establish the successful commands and counts;
no terminal nested-step metadata was invented. No independent all-main biological
validation or documentation build is claimed by this update.

All 2,876 catalogue identities and association text, 235 queue objects, 116 earlier
completion updates and preceding progress bytes remain exact. This is update 117;
only the four named checkboxes change. Source inventories and dated availability
snapshots are preserved without a fresh availability recount. The append-only history was scaffolded and validated through the normal repository commands; both project pages were regenerated.

[Curation session](https://github.com/ai4curation/ai-gene-review/blob/cmungall/clingen-tracker574-20261024/history/projects/CLINGEN_MENDELIAN/2026-10-24T172508Z-codex-7cbb12.yaml)

## Completion checkpoint 579 — 2026-10-24 20:10:52 UTC

**579 complete; 2,297 remaining out of 2,876 primary catalogue genes.**
This adds only the five accepted actual merges below to
[tracker 574, PR #5438](https://github.com/ai4curation/ai-gene-review/pull/5438).
Each exact-head approval and actual-merge audit was checked independently;
acceptance by the coordinating AI agent is not a human maintainer sign-off.
ESRRB, ETFB and ETFDH remain uncredited.

| Gene / PR | Approved head | Actual merge | Active + retired contexts | References / cores | DRAFT advisories |
| --- | --- | --- | --- | --- | --- |
| [ERLIN1 #5429](https://github.com/ai4curation/ai-gene-review/pull/5429) | [`38e73810a2a8`](https://github.com/ai4curation/ai-gene-review/commit/38e73810a2a82b9d025a87bfb92c5b52f54133c2) | [`46463aea153a`](https://github.com/ai4curation/ai-gene-review/commit/46463aea153a62d821a88f970f71ef5e2ab14a41) | 53 + 5 | 33 / 2 | 25 |
| [ERLIN2 #5441](https://github.com/ai4curation/ai-gene-review/pull/5441) | [`8aa9bf645000`](https://github.com/ai4curation/ai-gene-review/commit/8aa9bf64500012bf13709f323cdb826b008ef588) | [`7d2955f3f04f`](https://github.com/ai4curation/ai-gene-review/commit/7d2955f3f04f0dcbd25b2c6fc1ff478959bdf778) | 59 + 5 | 49 / 3 | 16 |
| [ESCO2 #5443](https://github.com/ai4curation/ai-gene-review/pull/5443) | [`884b57b4e82f`](https://github.com/ai4curation/ai-gene-review/commit/884b57b4e82f43c9dc4a43d2add7823532dd8ed2) | [`625ad38e3a3b`](https://github.com/ai4curation/ai-gene-review/commit/625ad38e3a3bc5eaf7821e242d9976f84b7f7ffc) | 29 + 0 | 15 / 1 | 4 |
| [ESPN #5446](https://github.com/ai4curation/ai-gene-review/pull/5446) | [`1519f7b56246`](https://github.com/ai4curation/ai-gene-review/commit/1519f7b56246bfa2ac14613d75990bc1a6253c33) | [`f93a466f6e7a`](https://github.com/ai4curation/ai-gene-review/commit/f93a466f6e7a8854069ba774a4ecdfc9a7e93737) | 18 + 0 | 12 / 1 | 1 |
| [ETFA #5452](https://github.com/ai4curation/ai-gene-review/pull/5452) | [`d2e21e55a62e`](https://github.com/ai4curation/ai-gene-review/commit/d2e21e55a62e9db549e291056c717a23c156e423) | [`0974627b3c89`](https://github.com/ai4curation/ai-gene-review/commit/0974627b3c895ff1e5701f6c6013c4b98de29d5c) | 36 + 1 | 26 / 4 | 2 |

All 82 approved PR path entries, 36 complete gene-directory files and 178
external dependency entries match their approved head, actual merge and fixed
main `0974627b3c895ff1e5701f6c6013c4b98de29d5c` in mode, type and blob. Dependency counts overlap across genes.
ERLIN2 has 18 PR paths but 17 net changes because PMID:19751772 already matched
its merge parent; the other PR path sets equal their net changes. The read-only
remote-main observation was `0974627b3c895ff1e5701f6c6013c4b98de29d5c`; it is recorded
separately from the fixed parity cut. The five records preserve 132 inherited
quotation anchors in total and introduce no new quotation or NEW annotation.

ERLIN1 and ERLIN2 retain distinct protein and substrate scopes. Their structural
units contribute to the erlin complex's scaffold activity; neither is assigned
ubiquitin-transfer chemistry. ERLIN1 cholesterol binding is distinguished from
unresolved ERLIN2-specific native-cholesterol binding. Activated receptor turnover
and misfolded-protein quality control remain separate experimental contexts.
ERLIN1's 348-residue product and ERLIN2's 339-, 152- and 206-residue products are
not treated as functionally equivalent.

ESCO2 retains acetyl-CoA-dependent protein-lysine acetylation coupled to cohesion
and replication-fork regulation. Human ESCO2-fragment, combined ESCO1/2-depletion
and mouse-loss evidence remain distinct; no purified full-length human
ESCO2–SMC3 assay is implied. ESPN retains direct actin cross-linking and
microvillar assembly, with human espin 3A assays distinguished from rodent
localization and the two source products.

ETFA retains direct alpha-subunit FAD contacts alongside its contribution to the
assembled ETFA–ETFB carrier. MCAD/GCDH-to-DCIP assays do not establish isolated
alpha activity, ETFDH's separate ubiquinone reaction or complete metabolic flux.
The 333-residue precursor, its processed mature chain and the alternative
284-residue product remain distinct. Five ETFA judgments are UNDECIDED; retired
historical contexts in ETFA and the erlins remain visible. Completion is not a
claim that every annotation or product mechanism is resolved.

All three jobs in each actual merge-group run succeeded: [ERLIN1](https://github.com/ai4curation/ai-gene-review/actions/runs/40118864897), [ERLIN2](https://github.com/ai4curation/ai-gene-review/actions/runs/40122236875), [ESCO2](https://github.com/ai4curation/ai-gene-review/actions/runs/40124476015), [ESPN](https://github.com/ai4curation/ai-gene-review/actions/runs/40124578712), [ETFA](https://github.com/ai4curation/ai-gene-review/actions/runs/40125951462).
Each broad suite ran 4,245 Python tests (one skipped, 84 deselected), 276 doctests
(37 skipped), 12 examples, 438 overlapping automation tests and 19 JavaScript
tests, plus mypy and Ruff. Counts overlap and are not summed. Changed-gene
validation ran with the advisories above; the separate all-gene batch was
schema-only. The corresponding PR broad suites were path-filtered and skipped.
Prediction and upstream PAINT checks were skipped in the recorded merge jobs;
the aggregate gates added no tests. Recorded warnings and an ignored SQL
finalizer diagnostic are not hidden by the successful terminal conclusions.

All 2,876 catalogue identities and association text, 235 queue objects, 117
earlier completion updates and preceding progress bytes are preserved. This is
update 118; only the five named checkboxes change. Dated source inventories
remain historical and are not refreshed by this completion update.

The append-only history was scaffolded and validated through the normal repository commands; both project pages were regenerated.

[Curation session](https://github.com/ai4curation/ai-gene-review/blob/cmungall/clingen-tracker579-20261024/history/projects/CLINGEN_MENDELIAN/2026-10-24T201537Z-codex-48a79e.yaml)

## Completion checkpoint 582 — 2026-10-24 22:42:53 UTC

**582 complete; 2,294 remaining out of 2,876 primary catalogue genes.**
This adds only the three accepted actual merges below to
[tracker 579, PR #5467](https://github.com/ai4curation/ai-gene-review/pull/5467).
Independent audit acceptance is by the coordinating AI agent, not a human
maintainer sign-off. Other pending genes receive no credit.

| Gene / PR | Approved head | Actual merge | Contexts | References / cores | Status / advisories |
| --- | --- | --- | --- | --- | --- |
| [ESRRB #5461](https://github.com/ai4curation/ai-gene-review/pull/5461) | [`2dc84ba6ac5b`](https://github.com/ai4curation/ai-gene-review/commit/2dc84ba6ac5beafa6ad3e0bf74256ea21b719d72) | [`2cb3afa8a856`](https://github.com/ai4curation/ai-gene-review/commit/2cb3afa8a856b1faab7217c00b212f8b2bdcb55b) | 53 | 31 / 1 | COMPLETE / 0 |
| [ETFDH #5468](https://github.com/ai4curation/ai-gene-review/pull/5468) | [`246dc94621f1`](https://github.com/ai4curation/ai-gene-review/commit/246dc94621f1cf938b6bd118cdd19ce0ad8eeb0e) | [`9cb3fe3a3e21`](https://github.com/ai4curation/ai-gene-review/commit/9cb3fe3a3e2161a86c5bebc6d9a295233cb7c200) | 37 | 19 / 5 | DRAFT / 7 |
| [ETHE1 #5470](https://github.com/ai4curation/ai-gene-review/pull/5470) | [`8cf5cbe3040e`](https://github.com/ai4curation/ai-gene-review/commit/8cf5cbe3040efbae4295c15ecb0446a5bfdd9781) | [`5cffa2f757b5`](https://github.com/ai4curation/ai-gene-review/commit/5cffa2f757b5ae147f0f128177b0ffd0dbe0d096) | 27 | 16 / 1 | DRAFT / 5 |

All 46 approved PR paths, 16 complete gene-directory files and 49 external
dependency entries match approved head, actual merge and fixed main
`5cffa2f757b5ae147f0f128177b0ffd0dbe0d096` in mode, type and blob. Dependency counts can overlap.
The separate remote-main observation was `5cffa2f757b5ae147f0f128177b0ffd0dbe0d096`.
All 42 inherited quotation anchors belong to ETFDH and remain exact; ESRRB and
ETHE1 have none. No new quotation or NEW annotation is introduced.

ESRRB retains human DNA-binding and transcription-activation evidence, with
long and short constructs corresponding to current 508- and 433-residue
accession sequences, without verifying historical plasmid sequences or the
untested 500-residue product. Mouse developmental contexts remain separate. Its computed COMPLETE
status leaves six UNDECIDED judgments visible.

ETFDH retains the ETF-to-ubiquinone reaction with FAD and a 4Fe–4S cluster,
separate from the soluble ETFA–ETFB carrier. Human enzyme assays and the native
porcine structure remain distinct; neither establishes full respiratory flux or
functional equivalence of the 617- and 570-residue products. Two stress-process
judgments remain UNDECIDED.

ETHE1 retains iron-dependent glutathione-persulfide oxidation to sulfite and
glutathione in the matrix. Historical cytoplasmic observations remain non-core;
independent matrix evidence and the unresolved two-zinc source-model query are
preserved. Engineered truncations, native processing and separate shorter
RefSeq products are not treated as functionally equivalent.

All three jobs succeeded in each actual merge-group run: [ESRRB](https://github.com/ai4curation/ai-gene-review/actions/runs/40136643412), [ETFDH](https://github.com/ai4curation/ai-gene-review/actions/runs/40136974831), [ETHE1](https://github.com/ai4curation/ai-gene-review/actions/runs/40136976805).
Each broad suite executed 4,268 Python tests (one skipped, 84 deselected),
277 doctests (37 skipped), 12 examples, 438 overlapping automation tests and
19 JavaScript tests, plus mypy over 285 source files and Ruff. Counts overlap
and are not summed. Changed-gene validation retained the advisories above;
the separate all-gene batch was schema-only. The PR broad suites, prediction
checks and upstream PAINT checks were skipped in their recorded scopes.
Global warnings and unresolved residue claims remain; aggregate gates add no tests.

This is update 119. All 2,876 identities and association text, 235 queue objects,
118 earlier updates and preceding progress bytes remain exact; only the three
named checkboxes change. Dated availability inventories are unchanged.

The append-only history was scaffolded and validated through the normal repository commands; both project pages were regenerated.

[Curation session](https://github.com/ai4curation/ai-gene-review/blob/cmungall/clingen-tracker582-20261024/history/projects/CLINGEN_MENDELIAN/2026-10-24T225256Z-codex-c6114a.yaml)

## Completion checkpoint 585 — 2026-10-24 23:50:50 UTC

**585 complete; 2,291 remaining out of 2,876 primary catalogue genes.**
This adds only the three accepted actual merges below to
[tracker 582, PR #5479](https://github.com/ai4curation/ai-gene-review/pull/5479).
Independent audit acceptance is by the coordinating AI agent, not a human
maintainer sign-off. Other pending genes receive no credit.

| Gene / PR | Approved head | Actual merge | Contexts | References / cores | Status / advisories |
| --- | --- | --- | --- | --- | --- |
| [ETFB #5466](https://github.com/ai4curation/ai-gene-review/pull/5466) | [`4ac38fb32d36`](https://github.com/ai4curation/ai-gene-review/commit/4ac38fb32d36ccdfec36992029483b669d073dfa) | [`d0388f87fd10`](https://github.com/ai4curation/ai-gene-review/commit/d0388f87fd10973d0bfd5db1d0b01cff97b8a3c4) | 28 | 22 / 2 | DRAFT / 4 |
| [ETV6 #5472](https://github.com/ai4curation/ai-gene-review/pull/5472) | [`75ee95de50ee`](https://github.com/ai4curation/ai-gene-review/commit/75ee95de50ee421755637c4457de9bfd6d042b53) | [`e4ed1ee4b2ab`](https://github.com/ai4curation/ai-gene-review/commit/e4ed1ee4b2abb67d0293a263367896abf42b5ce1) | 43 | 32 / 1 | DRAFT / 7 |
| [EVC #5476](https://github.com/ai4curation/ai-gene-review/pull/5476) | [`61dc504b83df`](https://github.com/ai4curation/ai-gene-review/commit/61dc504b83df6f796cb5d206060ca4b3e02111fb) | [`1ca4af83c61f`](https://github.com/ai4curation/ai-gene-review/commit/1ca4af83c61fd140120fe91b379ce15ff6db087e) | 19 | 15 / 1 | COMPLETE / 0 |

All 36 approved PR paths, 16 complete gene-directory files and 54 external
dependency entries match approved head, actual merge and fixed main
`5e62db5cf9887be68578d786c36f0e647a90cf7b` in mode, type and blob. Dependency counts can overlap.
The separate remote-main observation was `5e62db5cf9887be68578d786c36f0e647a90cf7b`.
All 41 inherited quotation anchors belong to ETFB and remain exact; ETV6 and
EVC have none. No new quotation or NEW annotation is introduced.

ETFB contributes to the assembled mitochondrial ETFA–ETFB electron carrier,
with a distinct AMP-binding facet. Its fatty-acid and amino-acid oxidation roles
are kept separate from ETFDH-mediated quinone reduction. Human heterodimer
assays do not establish isolated beta-subunit turnover or equivalence of the
255- and 346-residue products; the S1P-stabilized assembly remains model-bounded.

ETV6 retains native ETS-site recognition and transcriptional repression with
functional corepressor associations, alongside contextual activation evidence.
Ten pathological fusion-protein projections are removed from native ETV6
annotations. M1/M43 experimental constructs and separately documented natural
transcripts remain distinct; no universal product equivalence or native kinase
activity is asserted.

EVC retains ciliary Smoothened-pathway participation and positive regulation,
with basal-body and ciliary-membrane localization bounds. Mouse mechanistic
experiments remain distinct from human imaging and gene-level inference. Its
individual molecular function remains unspecified, and one judgment is
UNDECIDED despite computed COMPLETE status and zero advisories.

All three jobs succeeded in each actual merge-group run: [ETFB](https://github.com/ai4curation/ai-gene-review/actions/runs/40139334008), [ETV6](https://github.com/ai4curation/ai-gene-review/actions/runs/40140515525), [EVC](https://github.com/ai4curation/ai-gene-review/actions/runs/40141323927).
Each broad suite executed 4,293 Python tests (one skipped, 84 deselected),
278 doctests (37 skipped), 12 examples, 438 overlapping automation tests and
19 JavaScript tests, plus mypy over 287 source files and Ruff. Counts overlap
and are not summed. Changed-gene validation retained the advisories above;
the separate all-gene batch was schema-only. The PR broad suites, prediction
checks and upstream PAINT checks were skipped in their recorded scopes.
Global warnings and unresolved residue claims remain; aggregate gates add no tests.

This is update 120. All 2,876 identities and association text, 235 queue objects,
119 earlier updates and preceding progress bytes remain exact; only the three
named checkboxes change. Dated availability inventories are unchanged.

The append-only history was scaffolded and validated through the normal repository commands; both project pages were regenerated.

[Curation session](https://github.com/ai4curation/ai-gene-review/blob/cmungall/clingen-tracker585-20261024/history/projects/CLINGEN_MENDELIAN/2026-10-25T000127Z-codex-1c9b39.yaml)

## Completion checkpoint 587 — 2026-10-25 02:14:40 UTC

**587 complete; 2,289 remaining out of 2,876 primary catalogue genes.**
This adds only EVC2 and EXOC6B to
[tracker 585, PR #5489](https://github.com/ai4curation/ai-gene-review/pull/5489).
Independent audit acceptance is by the coordinating AI agent, not a human
maintainer sign-off. Other pending genes receive no credit.

| Gene / PR | Approved head | Actual merge | Contexts | References / cores | Status / advisories |
| --- | --- | --- | --- | --- | --- |
| [EVC2 #5477](https://github.com/ai4curation/ai-gene-review/pull/5477) | [`9909a981c35d`](https://github.com/ai4curation/ai-gene-review/commit/9909a981c35d7fcafb37b1e3f25ce1150f9170bf) | [`60c2825da3e3`](https://github.com/ai4curation/ai-gene-review/commit/60c2825da3e3ed6b694e469d4cf6ec34b0621e1a) | 14 | 10 / 1 | DRAFT / 1 |
| [EXOC6B #5480](https://github.com/ai4curation/ai-gene-review/pull/5480) | [`3acaf58e2071`](https://github.com/ai4curation/ai-gene-review/commit/3acaf58e2071e85a66edf28c5006120b7bcde64f) | [`0fcfcd6ce63d`](https://github.com/ai4curation/ai-gene-review/commit/0fcfcd6ce63d58c6f9ee4830337d5cce9454eb43) | 11 | 17 / 1 | DRAFT / 4 |

All 28 approved PR path entries, 10 complete gene-directory files and 24
external dependency entries match approved head, actual merge and fixed main
`0fcfcd6ce63d58c6f9ee4830337d5cce9454eb43` in mode, type and blob. There are 26 net merge paths:
two EVC2 publication caches already existed identically on its merge parent.
Dependency counts can overlap. The separate remote-main observation was
`0fcfcd6ce63d58c6f9ee4830337d5cce9454eb43`. Both reviews contain zero quotations and zero
NEW assertions. Three EVC2 products and two EXOC6B products remain distinct.

EVC2 retains seven ACCEPT, four MODIFY and three KEEP_AS_NON_CORE decisions.
EXOC6B retains five ACCEPT, four KEEP_AS_NON_CORE and two UNDECIDED decisions.
Both remain DRAFT, with one core-coverage advisory and four generic-binding
advisories respectively. No biological uncertainty is silently resolved by
recording the merges.

All three jobs succeeded in each actual merge-group run: [EVC2](https://github.com/ai4curation/ai-gene-review/actions/runs/40150759238), [EXOC6B](https://github.com/ai4curation/ai-gene-review/actions/runs/40151238545).
Each broad suite executed 4,293 Python tests (one skipped, 84 deselected),
278 doctests (37 skipped), 12 examples, 438 overlapping automation tests and
19 JavaScript tests, plus mypy over 287 source files and Ruff. Counts overlap
and are not summed. Strict target validation retained the advisories above;
the separate all-gene batch was schema-only. History validation covered
16,471 and 16,474 records respectively, with 42 history tests in each run.
The earlier PR broad suites and conditional prediction/upstream PAINT checks
were skipped in their recorded scopes. Global warnings, unresolved residue
claims and the nonfatal SQL cleanup exception remain recorded; aggregate
gates add no tests.

The accepted gene histories use immutable merge-commit links:

- [EVC2 accepted curation history](https://github.com/ai4curation/ai-gene-review/blob/60c2825da3e3ed6b694e469d4cf6ec34b0621e1a/history/genes/human/EVC2/2026-10-24T233603Z-codex-7aae6b.yaml)
- [EXOC6B accepted curation history](https://github.com/ai4curation/ai-gene-review/blob/0fcfcd6ce63d58c6f9ee4830337d5cce9454eb43/history/genes/human/EXOC6B/2026-10-24T234753Z-codex-017055.yaml)

This is update 121. All 2,876 identities and association text, 235 queue objects,
120 earlier updates and preceding progress bytes remain exact; only the two
named checkboxes change. Dated availability inventories are unchanged.

The append-only history was scaffolded and validated through the normal repository commands; both project pages were regenerated.

Curation session: `history/projects/CLINGEN_MENDELIAN/2026-10-25T021558Z-codex-69f821.yaml`.

## Completion checkpoint 591 — 2026-10-25 03:26:01 UTC

**591 complete; 2,285 remaining out of 2,876 primary catalogue genes.**
This adds only EXT2, EXT1, EYA1 and EYS to
[tracker 587, PR #5494](https://github.com/ai4curation/ai-gene-review/pull/5494).
Independent actual-merge acceptance is by the coordinating AI agent, not a
human maintainer sign-off. Other pending genes receive no credit.

| Gene / PR | Approved head | Actual merge | Contexts | References / cores | Status / advisories |
| --- | --- | --- | --- | --- | --- |
| [EXT2 #5490](https://github.com/ai4curation/ai-gene-review/pull/5490) | [`f3299defabac`](https://github.com/ai4curation/ai-gene-review/commit/f3299defabacbb021ca0c28f13d12a2f4e8c4f33) | [`212f56f04101`](https://github.com/ai4curation/ai-gene-review/commit/212f56f041010b01c80ce8a2a680e6fc3a03bf45) | 60 | 33 / 1 | DRAFT / 6 |
| [EXT1 #5488](https://github.com/ai4curation/ai-gene-review/pull/5488) | [`0621827756fb`](https://github.com/ai4curation/ai-gene-review/commit/0621827756fb4ca0301d89f669acbcb0caf2b778) | [`ab72d4752747`](https://github.com/ai4curation/ai-gene-review/commit/ab72d475274707f696b6823c251115b8af50c9d6) | 61 | 30 / 2 | DRAFT / 1 |
| [EYA1 #5491](https://github.com/ai4curation/ai-gene-review/pull/5491) | [`62fe39ec04f1`](https://github.com/ai4curation/ai-gene-review/commit/62fe39ec04f1789232ce9dc79bd3a80dd6b3bc8d) | [`980ac0e0a2f1`](https://github.com/ai4curation/ai-gene-review/commit/980ac0e0a2f14e779f6cc588d8d4260a7e5b0093) | 33 | 28 / 2 | COMPLETE / 0 |
| [EYS #5493](https://github.com/ai4curation/ai-gene-review/pull/5493) | [`3367c5a7fbbe`](https://github.com/ai4curation/ai-gene-review/commit/3367c5a7fbbe108e409ca806bd4ca1f2b65e4e33) | [`501b51748c62`](https://github.com/ai4curation/ai-gene-review/commit/501b51748c62be09a902b9b7272cf325a2dadea4) | 21 | 15 / 1 | COMPLETE / 0 |

All 56 approved PR path entries, 21 complete gene-directory files and 89
external dependency entries match approved heads, actual merges and fixed main
`b2b10f56fdd7e6996d24885376d9ff6b10f19377` in mode, type and blob. The 51 net merge paths
exclude five EXT1 publication paths already present identically on its parent.
The dependency ledger distinguishes 25 entries introduced by their gene merge
from 64 reused entries; shared dependencies can appear more than once.
EYA1 retains all 60 inherited quotation anchors and its two inherited NEW
annotations. No quotations, source bytes or gene decisions change here.

**EXT2.** EXT2 supplies the principal GlcNAc-transfer step of the Golgi EXT1–EXT2 heparan-sulfate elongation complex. Its assembled contribution to GlcA transfer is distinct from low activity in older separately expressed preparations.

**EXT1.** EXT1 supplies the principal GlcA-transfer step and has measured secondary GlcNAc-transfer capacity. Its quantitative GlcNAc contribution in the native complex remains unresolved; the review retains preparation and protein-stability limits.

**EYA1.** EYA1 combines conserved SIX-associated transcriptional coactivation with protein-tyrosine dephosphorylation, including H2AX-dependent regulation of the DNA-damage response. It is not assigned DNA strand-restoration chemistry, and intrinsic Ser/Thr catalysis remains unresolved.

**EYS.** EYS provides conserved extracellular structural support associated with photoreceptor maintenance. The precise human interphotoreceptor topology and the functions of the four natural products remain unresolved; observed intracellular pools are not assumed to perform the same structural role.

EXT2 and EXT1 retain one and two UNDECIDED judgments, respectively; EYA1 and
EYS retain three and four despite their computed COMPLETE status. Source and
product limits remain part of the accepted reviews.

All three jobs passed in each actual merge-group run: [EXT2](https://github.com/ai4curation/ai-gene-review/actions/runs/40152868921), [EXT1](https://github.com/ai4curation/ai-gene-review/actions/runs/40153258542), [EYA1](https://github.com/ai4curation/ai-gene-review/actions/runs/40153641652), [EYS](https://github.com/ai4curation/ai-gene-review/actions/runs/40154709309).
Each broad suite ran 4,293 Python tests (one skipped, 84 deselected),
278 doctests (37 skipped), 12 examples, 438 overlapping automation tests,
19 JavaScript tests, mypy over 287 files and Ruff. Counts overlap and are not
summed. Target strict checks retained the advisories shown above; the separate
all-gene batch was schema-only. Conditional prediction and upstream PAINT
checks were skipped. Global warnings, unresolved checks and the nonfatal SQL
cleanup exception remain recorded in the accepted audits; aggregate gates
add no tests. The queue update preserves the per-run evidence and skip lists.

- [EXT2 accepted curation history](https://github.com/ai4curation/ai-gene-review/blob/212f56f041010b01c80ce8a2a680e6fc3a03bf45/history/genes/human/EXT2/2026-10-25T014149Z-codex-6225f1.yaml)
- [EXT1 accepted curation history](https://github.com/ai4curation/ai-gene-review/blob/ab72d475274707f696b6823c251115b8af50c9d6/history/genes/human/EXT1/2026-10-25T015241Z-codex-2325ba.yaml)
- [EYA1 accepted curation history](https://github.com/ai4curation/ai-gene-review/blob/980ac0e0a2f14e779f6cc588d8d4260a7e5b0093/history/genes/human/EYA1/2026-10-25T020022Z-codex-0af32f.yaml)
- [EYS accepted curation history](https://github.com/ai4curation/ai-gene-review/blob/501b51748c62be09a902b9b7272cf325a2dadea4/history/genes/human/EYS/2026-10-25T020807Z-codex-7df027.yaml)

Update 122 preserves all 2,876 identities and association text, 235 queue
objects, 121 earlier updates and preceding progress bytes. Only the four named
checkboxes change. The separate remote-main observation at 2026-10-25T03:26:01.626618+00:00
was `b2b10f56fdd7e6996d24885376d9ff6b10f19377`; source inventories remain historical.

The append-only history was scaffolded and validated through the normal repository commands; both project pages were regenerated.

Curation session: [history record](https://github.com/ai4curation/ai-gene-review/blob/8c7ae8004be4e7855e189a3475bb67ae0f21afb3/history/projects/CLINGEN_MENDELIAN/2026-10-25T033732Z-codex-767415.yaml).

## Completion checkpoint 595 — 2026-10-25 04:57:30 UTC

**595 complete; 2,281 remaining out of 2,876 primary catalogue genes.**
This adds only EYA4, EZH2, F10 and F11 to
[tracker 591, PR #5498](https://github.com/ai4curation/ai-gene-review/pull/5498).
Actual-merge acceptance is by the coordinating AI agent, not a human
maintainer sign-off. Other pending genes receive no credit.

| Gene / PR | Approved head | Actual merge | Contexts | References / cores | Status / advisories |
| --- | --- | --- | --- | --- | --- |
| [EYA4 #5492](https://github.com/ai4curation/ai-gene-review/pull/5492) | [`bdadf273c590`](https://github.com/ai4curation/ai-gene-review/commit/bdadf273c590b952d320e6f6b120c749ee638092) | [`a47ce8ba01b1`](https://github.com/ai4curation/ai-gene-review/commit/a47ce8ba01b18294a8361b9e81366affed61237e) | 19 | 14 / 2 | COMPLETE / 0 |
| [EZH2 #5496](https://github.com/ai4curation/ai-gene-review/pull/5496) | [`cc0254df56f8`](https://github.com/ai4curation/ai-gene-review/commit/cc0254df56f8c7a3c3b3ef0bd74d1254e1396278) | [`f477bb7bd7f4`](https://github.com/ai4curation/ai-gene-review/commit/f477bb7bd7f4bee62db4a950c62dc5a9ca1bddf6) | 186 | 108 / 2 | DRAFT / 54 |
| [F10 #5497](https://github.com/ai4curation/ai-gene-review/pull/5497) | [`4486ba7bcb42`](https://github.com/ai4curation/ai-gene-review/commit/4486ba7bcb4219cc3f8697ca61269a6a9829e020) | [`df37cff6f3ba`](https://github.com/ai4curation/ai-gene-review/commit/df37cff6f3bacd6900da5e0eec3dcf34fb2ed675) | 58 | 42 / 1 | DRAFT / 4 |
| [F11 #5500](https://github.com/ai4curation/ai-gene-review/pull/5500) | [`d5255b7e6464`](https://github.com/ai4curation/ai-gene-review/commit/d5255b7e64643c9397e506cb784f5686b47247a8) | [`db8135f603bf`](https://github.com/ai4curation/ai-gene-review/commit/db8135f603bf131e28c36950b3162c2610e55b64) | 38 | 28 / 1 | DRAFT / 1 |

All 140 approved PR paths are also the 140 net merge paths. The 20 complete
gene-directory files and 177 external dependency entries match approved heads,
actual merges and fixed main `db8135f603bf131e28c36950b3162c2610e55b64` in mode,
type and blob. Of those dependency entries, 108 were introduced by the
corresponding gene merge and 69 reused from its parent; there are 177 unique
external paths in this four-gene closure. These counts describe overlapping
payload and dependency sets and are not added together. EYA4 retains its three
explicitly authorized NEW rows. No gene decisions, source bytes or quotations
change in this tracker update.

**EYA4.** EYA4 combines protein-tyrosine phosphatase activity with SIX-associated transcriptional coactivation. Human PLK1 regulation and peptide chemistry remain distinct from conserved DNA-repair inference; historical construct and five-product boundaries remain explicit.

**EZH2.** EZH2 supplies the H3K27 methyltransferase site in PRC2 and binds tested long noncoding RNAs. EED reader activity and accessory targeting are kept separate from EZH2 catalysis; RNA binding does not impose a universal recruitment or regulatory outcome.

**F10.** Activated factor Xa converts prothrombin to thrombin and acts on additional coagulation substrates. The same protease activity also cleaves PAR2 with barrier protection in a defined endothelial-cell model; that result is not generalized to all signaling contexts or mTOR regulation.

**F11.** Activated factor XIa performs sequential factor IX cleavage in the intrinsic coagulation pathway. Its A3 recognition region and platelet-surface association support this catalytic unit; untested shorter-product equivalence and contextual fibrinolysis evidence remain bounded.

Local status computation and validation recorded EYA4 as COMPLETE with zero
advisories, while one UNDECIDED judgment remains. EZH2, F10 and F11 remain DRAFT
with 54, four and one advisories, and 16, three and one UNDECIDED judgments,
respectively. The advisories concern supported generic-binding contexts;
completion does not erase these source and biological limits.

All three jobs passed in each actual merge-group run: [EYA4](https://github.com/ai4curation/ai-gene-review/actions/runs/40157854148), [EZH2](https://github.com/ai4curation/ai-gene-review/actions/runs/40161582748), [F10](https://github.com/ai4curation/ai-gene-review/actions/runs/40161661337), [F11](https://github.com/ai4curation/ai-gene-review/actions/runs/40161878292).
The accepted operative CI reads record 4,293 Python test passes (one skipped,
84 deselected), 278 doctest passes (37 skipped), 12 examples, 438 overlapping
automation tests, 19 JavaScript tests, mypy over 287 files and Ruff. Counts
overlap and are not summed. Target strict checks retained the advisories above;
the separate all-gene batch was schema-only. Module, history and family checks
ran, while conditional prediction checks, history-coverage checks and full-run
upstream PAINT verification were skipped. Global snippet skips, unresolved
identifiers and the nonfatal SQL cleanup exception remain in the accepted
receipts. Aggregate gates add no tests. The queue update retains per-run job
links and exact skipped-step lists. No new workflow or validator ran for this
private tracker proposal.

- [EYA4 accepted curation history](https://github.com/ai4curation/ai-gene-review/blob/a47ce8ba01b18294a8361b9e81366affed61237e/history/genes/human/EYA4/2026-10-25T030619Z-codex-348d64.yaml)
- [EZH2 accepted curation history](https://github.com/ai4curation/ai-gene-review/blob/f477bb7bd7f4bee62db4a950c62dc5a9ca1bddf6/history/genes/human/EZH2/2026-10-25T040727Z-codex-ab5d34.yaml)
- [F10 accepted curation history](https://github.com/ai4curation/ai-gene-review/blob/df37cff6f3bacd6900da5e0eec3dcf34fb2ed675/history/genes/human/F10/2026-10-25T041001Z-codex-bd9a5e.yaml)
- [F11 accepted curation history](https://github.com/ai4curation/ai-gene-review/blob/db8135f603bf131e28c36950b3162c2610e55b64/history/genes/human/F11/2026-10-25T041342Z-codex-ccb3cd.yaml)

Update 123 preserves all 2,876 identities and association text, 235 queue
objects, 122 earlier updates and preceding progress bytes. Only the four named
checkboxes change. The separate remote-main observation at 2026-10-25T04:57:30.932556+00:00
was `db8135f603bf131e28c36950b3162c2610e55b64`; source inventories remain historical.

The append-only history was scaffolded and validated through the normal repository commands; both project pages were regenerated.

Curation session: [history record](https://github.com/ai4curation/ai-gene-review/blob/5ab2f723c88e861c08f6095f17dcb005db096262/history/projects/CLINGEN_MENDELIAN/2026-10-25T051225Z-codex-a3d1af.yaml).

## Completion checkpoint 597 — 2026-10-25 06:51:14 UTC

**597 complete; 2,279 remaining out of 2,876 primary catalogue genes.**
Only F12 and F13A1 are added to [tracker 595, PR #5504](https://github.com/ai4curation/ai-gene-review/pull/5504).
Acceptance is by the coordinating AI agent, not a human maintainer sign-off.

| Gene / PR | Approved head | Actual merge | Contexts | References / cores | Status / advisories |
| --- | --- | --- | --- | --- | --- |
| [F12 #5501](https://github.com/ai4curation/ai-gene-review/pull/5501) | [`abe1ca5de2c0`](https://github.com/ai4curation/ai-gene-review/commit/abe1ca5de2c08a06df2959f3adb9fcef87c30be1) | [`cb90c6f3df01`](https://github.com/ai4curation/ai-gene-review/commit/cb90c6f3df010204fd74fc52a8d42057164045e5) | 63 | 38 / 1 | DRAFT / 10 |
| [F13A1 #5502](https://github.com/ai4curation/ai-gene-review/pull/5502) | [`3b34fd96c0f4`](https://github.com/ai4curation/ai-gene-review/commit/3b34fd96c0f45ab374f131a1d28be2ad6b2d4a49) | [`5e597e6e08e8`](https://github.com/ai4curation/ai-gene-review/commit/5e597e6e08e8006c81764e88155a19a826b63dee) | 48 | 26 / 1 | DRAFT / 22 |

The accepted F12 and F13A1 closures contain 45 and 31 files, respectively,
including their complete gene directories, histories and selected sources.
Every file matches the accepted head and actual merge evidence and fixed main
`5e597e6e08e8006c81764e88155a19a826b63dee`. These overlapping sets are not summed.
F12 has 31 approved PR paths and 30 net merge paths: the identical
R-HSA-9936430 cache was already present on its actual merge parent. F13A1 has
23 approved PR paths and 23 net merge paths. No gene decision or source byte
changes in this tracker update. The accepted F13A1 review retains its one NEW
calcium-binding annotation, and neither review adds publication quotations.

**F12.** Activated factor XII supplies serine endopeptidase activity in contact-system and coagulation reactions. Source-specific signaling, surface and product boundaries remain explicit; two contexts remain undecided.

**F13A1.** Activated factor XIII A catalyzes protein cross-linking that stabilizes fibrin. The added calcium-binding annotation is supported by a human A-subunit structure and corroborating evidence, while precursor versus active-complex and inaccessible-original limits remain explicit.

F12 remains DRAFT with 10 advisories (eight supported non-core binding and two
context-consistency advisories) and two UNDECIDED contexts. F13A1 remains DRAFT
with 22 supported non-core binding advisories and one UNDECIDED context.
Original-access and assay limits remain visible in the gene reviews.

The three Build and test jobs passed on each actual merge in
[F12 run 40165165689](https://github.com/ai4curation/ai-gene-review/actions/runs/40165165689)
and [F13A1 run 40168349716](https://github.com/ai4curation/ai-gene-review/actions/runs/40168349716).
Accepted operative log reads cover the executed test, strict-target, schema,
history and family checks. Global skipped snippets, unresolved family/gene
claims and the nonfatal post-test SQL cleanup exception remain disclosed in
the accepted evidence. Aggregate gates add no tests. This tracker proposal
does not rerun gene validators or claim those global uncertainties are resolved.

- [F12 accepted curation history](https://github.com/ai4curation/ai-gene-review/blob/cb90c6f3df010204fd74fc52a8d42057164045e5/history/genes/human/F12/2026-10-25T045958Z-codex-6867ca.yaml)
- [F13A1 accepted curation history](https://github.com/ai4curation/ai-gene-review/blob/5e597e6e08e8006c81764e88155a19a826b63dee/history/genes/human/F13A1/2026-10-25T053201Z-codex-0423ae.yaml)

Update 124 preserves all 2,876 catalogue identities and association text,
235 queue objects, 123 earlier updates and all preceding progress bytes.
Only the F12 and F13A1 checkboxes change. Dated source inventories remain historical.

The append-only history was scaffolded and validated through the normal repository commands; both project pages were regenerated.

Curation session: [history record](https://github.com/ai4curation/ai-gene-review/blob/ad3d4b87db7ef790c7418a16f8c072694bb6c04b/history/projects/CLINGEN_MENDELIAN/2026-10-25T070241Z-codex-cecf61.yaml).
