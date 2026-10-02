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
| APOB | Definitive | INITIALIZED | Ready #3365; audit published; 0 PMID and 0 Reactome cache gates; current-head review, CI and merge remain separate | `cmungall/clingen-apob` | [#3365](https://github.com/ai4curation/ai-gene-review/pull/3365) |
| AR | Definitive | INITIALIZED | Review #3364 merged; current-head approval and required CI passed; all 114 scoped merged blobs verified | `cmungall/clingen-ar` | [#3364](https://github.com/ai4curation/ai-gene-review/pull/3364) |
| ARHGEF9 | Definitive | INITIALIZED | Review #3366 merged; current-head approval and required CI passed; all 19 scoped merged blobs verified | `cmungall/clingen-arhgef9` | [#3366](https://github.com/ai4curation/ai-gene-review/pull/3366) |
| ARID1A | Definitive | INITIALIZED | Review #3367 merged; current-head approval and required CI passed; all 53 scoped merged blobs verified | `cmungall/clingen-arid1a` | [#3367](https://github.com/ai4curation/ai-gene-review/pull/3367) |
| ARID1B | Definitive | INITIALIZED | Review #3370 merged; current-head approval and required CI passed; all 35 scoped merged blobs verified | `cmungall/clingen-arid1b` | [#3370](https://github.com/ai4curation/ai-gene-review/pull/3370) |
| ARID2 | Definitive | INITIALIZED | Ready #3372; audit published; 0 PMID and 0 Reactome cache gates; current-head review, CI and merge remain separate | `cmungall/clingen-arid2` | [#3372](https://github.com/ai4curation/ai-gene-review/pull/3372) |
| ARMC2 | Definitive | INITIALIZED | Review #3369 merged; current-head approval and required CI passed; all 11 scoped merged blobs verified | `cmungall/clingen-armc2` | [#3369](https://github.com/ai4curation/ai-gene-review/pull/3369) |
| ARMC9 | Definitive | INITIALIZED | Changes requested #3371; exact-head review remains unresolved; approval, CI and merge remain pending | `cmungall/clingen-armc9` | [#3371](https://github.com/ai4curation/ai-gene-review/pull/3371) |
| ARL13B | Definitive | INITIALIZED | Held on exact-head review #3374; the remaining generic-binding policy request conflicts with the explicit user action definitions. No approval, CI completion or merge claimed. | `cmungall/clingen-arl13b` | [#3374](https://github.com/ai4curation/ai-gene-review/pull/3374) |
| ARL2BP | Definitive | INITIALIZED | Review #3373 merged; current-head approval and required CI passed; all 33 scoped merged blobs verified | `cmungall/clingen-arl2bp` | [#3373](https://github.com/ai4curation/ai-gene-review/pull/3373) |
| ARPC1B | Definitive | INITIALIZED | Review #3378 merged; current-head approval and required CI passed; all 27 scoped merged blobs verified | `cmungall/clingen-arpc1b` | [#3378](https://github.com/ai4curation/ai-gene-review/pull/3378) |
| ARSA | Definitive | PREEXISTING_REVIEW_AUGMENTED | Review #3376 merged; current-head approval and required CI passed; all 31 scoped merged blobs verified | `cmungall/clingen-arsa` | [#3376](https://github.com/ai4curation/ai-gene-review/pull/3376) |
| ARSB | Definitive | PREEXISTING_REVIEW_AUGMENTED | Review #3379 merged; current-head approval and required CI passed; all 30 scoped merged blobs verified | `cmungall/clingen-arsb` | [#3379](https://github.com/ai4curation/ai-gene-review/pull/3379) |
| ARSL | Definitive | NORMAL_PENDING_SEED_REVIEWED | Review #3382 merged; current-head approval and required CI passed; all 13 scoped merged blobs verified | `cmungall/clingen-arsl` | [#3382](https://github.com/ai4curation/ai-gene-review/pull/3382) |
| ARX | Definitive | NORMAL_PENDING_SEED_REVIEWED | Review #3384 merged; current-head approval and required CI passed; all 19 scoped merged blobs verified | `cmungall/clingen-arx` | [#3384](https://github.com/ai4curation/ai-gene-review/pull/3384) |
| ASAH1 | Definitive | PREEXISTING_REVIEW_AUGMENTED | Review #3383 merged; current-head approval and required CI passed; all 32 scoped merged blobs verified | `cmungall/clingen-asah1` | [#3383](https://github.com/ai4curation/ai-gene-review/pull/3383) |
| ASL | Definitive | PREEXISTING_REVIEW_AUGMENTED | Ready #3385; audit published; 0 PMID and 0 Reactome cache gates; current-head review, CI and merge remain separate | `cmungall/clingen-asl` | [#3385](https://github.com/ai4curation/ai-gene-review/pull/3385) |
| ASH1L | Definitive | NORMAL_PENDING_SEED_REVIEWED | Review #3387 merged; current-head approval and required CI passed; all 17 scoped merged blobs verified | `cmungall/clingen-ash1l` | [#3387](https://github.com/ai4curation/ai-gene-review/pull/3387) |
| ASNS | Definitive | NORMAL_PENDING_SEED_REVIEWED | Ready #3438; audit published; 0 PMID and 0 Reactome cache gates; current-head review, CI and merge remain separate | `cmungall/clingen-asns` | [#3438](https://github.com/ai4curation/ai-gene-review/pull/3438) |
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
| ATP1A1 | Definitive | Newly seeded | Ready #3553; required CI and review queued; no current-head formal review or merge. Earlier-head formal reviews remain historical. | `cmungall/clingen-atp1a1` | [#3553](https://github.com/ai4curation/ai-gene-review/pull/3553) |
| ATP6AP1 | Definitive | Existing review audited | Ready #3550; exact-head CI and review job succeeded; policy-only CHANGES_REQUESTED remains under user ActionEnum; no merge | `cmungall/clingen-atp6ap1` | [#3550](https://github.com/ai4curation/ai-gene-review/pull/3550) |
| ATP6V0A2 | Definitive | Existing review audited | Ready #3551; prior saved tests passed and review attempt 2 completed successfully, but its formal verdict is CHANGES_REQUESTED solely on the documented generic-binding policy conflict. No merge. | `cmungall/clingen-atp6v0a2` | [#3551](https://github.com/ai4curation/ai-gene-review/pull/3551) |
| ATP1A2 | Definitive | Newly seeded | Review #3558 merged; current-head approval and required CI passed; all 26 scoped merged blobs verified | `cmungall/clingen-atp1a2` | [#3558](https://github.com/ai4curation/ai-gene-review/pull/3558) |
| ATP1A3 | Definitive | Newly seeded | Review #3555 merged; current-head approval and required CI passed; all 20 scoped merged blobs verified | `cmungall/clingen-atp1a3` | [#3555](https://github.com/ai4curation/ai-gene-review/pull/3555) |
| ATP2B2 | Definitive | Newly seeded | Review #3554 merged; current-head approval and required CI passed; all 24 scoped merged blobs verified | `cmungall/clingen-atp2b2` | [#3554](https://github.com/ai4curation/ai-gene-review/pull/3554) |
| ATP6V1B1 | Definitive | Existing review audited | Review #3556 merged; current-head approval and required CI passed; all 36 scoped merged blobs verified | `cmungall/clingen-atp6v1b1` | [#3556](https://github.com/ai4curation/ai-gene-review/pull/3556) |
| ATP13A3 | Definitive | Newly seeded | Review #3559 merged; current-head approval and required CI passed; all 12 scoped merged blobs verified | `cmungall/clingen-atp13a3` | [#3559](https://github.com/ai4curation/ai-gene-review/pull/3559) |
| ATP7B | Definitive | Existing review audited | Ready #3560; audit published; 0 PMID and 0 Reactome cache gates; current-head review, CI and merge remain separate; YAML remains DRAFT for documented scientific uncertainties or validator advisories, while the PR is ready and required source caches are closed | `cmungall/clingen-atp7b` | [#3560](https://github.com/ai4curation/ai-gene-review/pull/3560) |
| ATP7A | Definitive | Newly seeded | Ready #3561; second formal review CHANGES_REQUESTED on the documented generic-binding policy conflict. The reviewer reported CI still running; this extract contains no separate new-head CI check result. No merge. | `cmungall/clingen-atp7a` | [#3561](https://github.com/ai4curation/ai-gene-review/pull/3561) |
| ATP8A2 | Definitive | Newly seeded | Review #3562 merged; current-head approval and required CI passed; all 17 scoped merged blobs verified | `cmungall/clingen-atp8a2` | [#3562](https://github.com/ai4curation/ai-gene-review/pull/3562) |
| B3GALNT2 | Definitive | Existing review | Ready #3563; exact-head changes requested; required tests and automated review job succeeded. Biological follow-up remains pending; no merge or completion. | `cmungall/clingen-b3galnt2` | [#3563](https://github.com/ai4curation/ai-gene-review/pull/3563) |
| ATRX | Definitive | Not started | Review #3564 merged; current-head approval and required CI passed; all 41 scoped merged blobs verified | `cmungall/clingen-atrx` | [#3564](https://github.com/ai4curation/ai-gene-review/pull/3564) |
| ATXN2 | Definitive | Not started | Ready #3566; exact publication and metadata verified. Current-head formal review and CI were not separately reconciled at this fixed cut; no merge or completion claimed. | `cmungall/clingen-atxn2` | [#3566](https://github.com/ai4curation/ai-gene-review/pull/3566) |
| AUH | Definitive | Existing review | Review #3565 merged; current-head approval and required CI passed; all 17 scoped merged blobs verified | `cmungall/clingen-auh` | [#3565](https://github.com/ai4curation/ai-gene-review/pull/3565) |
| AURKC | Definitive | Not started | Ready #3568; exact publication and metadata verified. Current-head formal review and CI were not separately reconciled at this fixed cut; no merge or completion claimed. | `cmungall/clingen-aurkc` | [#3568](https://github.com/ai4curation/ai-gene-review/pull/3568) |
| AUTS2 | Definitive | Not started | Ready #3569; exact publication and metadata verified. Current-head formal review and CI were not separately reconciled at this fixed cut; no merge or completion claimed. | `cmungall/clingen-auts2` | [#3569](https://github.com/ai4curation/ai-gene-review/pull/3569) |
| AXIN2 | Definitive | Not started | Review #3572 merged; current-head approval and required CI passed; all 48 scoped merged blobs verified | `cmungall/clingen-axin2` | [#3572](https://github.com/ai4curation/ai-gene-review/pull/3572) |
| B3GALT6 | Definitive | Not started | Review #3573 merged; current-head approval and required CI passed; all 16 scoped merged blobs verified | `cmungall/clingen-b3galt6` | [#3573](https://github.com/ai4curation/ai-gene-review/pull/3573) |
| B3GLCT | Definitive | INITIALIZED seed | Review #3575 merged; current-head approval and required CI passed; all 18 scoped merged blobs verified | `cmungall/clingen-b3glct` | [#3575](https://github.com/ai4curation/ai-gene-review/pull/3575) |
| B4GALNT1 | Definitive | Existing review | Review #3574 merged; current-head approval and required CI passed; all 16 scoped merged blobs verified | `cmungall/clingen-b4galnt1` | [#3574](https://github.com/ai4curation/ai-gene-review/pull/3574) |
| B4GALT1 | Definitive | Existing review | Review #3576 merged at 2026-10-02 12:10:43 UTC; final-head approval and required CI passed; all 50 scoped merged blobs and 11 PR paths verified. | `cmungall/clingen-b4galt1` | [#3576](https://github.com/ai4curation/ai-gene-review/pull/3576) |
| B4GALT7 | Definitive | INITIALIZED seed | Review #3577 merged; current-head approval and required CI passed; all 20 scoped merged blobs verified | `cmungall/clingen-b4galt7` | [#3577](https://github.com/ai4curation/ai-gene-review/pull/3577) |
| B9D1 | Definitive | INITIALIZED seed | Ready #3579; first follow-up published. Exact-head review holds on the generic-binding policy disagreement under the supplied ActionEnum; no further cosmetic revision or repeated review request. Required test was observed in progress; no approval, merge or completion. | `cmungall/clingen-b9d1` | [#3579](https://github.com/ai4curation/ai-gene-review/pull/3579) |
| BAG3 | Definitive | Existing review | Ready #3578; initial and first follow-up published. Exact-head changes requested at 10:25:30 UTC; biology and provenance corrections accepted, remaining generic-binding policy disagreement held under the supplied ActionEnum. CI observed in progress; no merge readiness or completion. | `cmungall/clingen-bag3` | [#3578](https://github.com/ai4curation/ai-gene-review/pull/3578) |
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

Branches for work without a PR may exist only in a local isolated checkout.
Published check and approval states are the last verified states from this session,
not a live dashboard. ABCC6 merged through protected auto-merge on September 26
at 21:22:34 UTC. A separate checkout inside the writable workspace supports local
Git commits while the original worktree's shared Git metadata remains read-only.
Publication uses GitHub's API with expected-head guards and exact tree verification.
Direct Git transport and normal publication-source downloads still encounter DNS
failures. No local or published draft is counted as merged or complete.

The [publication queue](publication-queue.json) retains immutable publication hashes,
signed publication/file checks and append-only receipt chains. **159 of 2,876 genes
are complete**; 160 original gene PRs have merged, with 1 requiring a source
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

Source-limited UNDECIDED judgments remain valid. AKT1's completed Limited-tier audit
remains a scheduling exception. Project setup merged in
[#3126](https://github.com/ai4curation/ai-gene-review/pull/3126).

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
