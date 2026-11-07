---
title: Module literature, taxonomy and member review audit
maturity: IN_PROGRESS
last_reviewed: 2026-11-06
tags:
- BIOLOGY_DOMAIN
autolink_exclude:
- pins
---

# Module literature, taxonomy and member review audit

Audit every module in `modules/`, with one curation PR per module. Each audit must
search for relevant review literature, curate the references and mine specific
findings, attach evidence to individual steps and connections, assess the appropriate
taxonomic scope, verify family assignments and sample informative exemplars across
that scope, and complete individual member gene reviews. Follow each PR through
review, checks and merge. A module is not finished merely because its YAML validates
or its existing status says COMPLETE.

## Coverage and completion criteria

[Inventory](MODULE_TAXON_AUDIT/inventory.json) records the initial 702-module universe
at commit `18649bf003`, refreshed to 714 modules against `10fd59941f`, then 715 against `551ec0d122` on 2026-10-26. The 2026-11-05 refresh against `d72614fd33839f917e839f07668b671a990fec56` found 62 further modules, bringing the current universe to 777 with no removals. All additions enter as NOT_STARTED; their overlap checks and curation remain pending. [Refresh manifest](../analysis/module_audits/bacterial_c_di_gmp_signaling/inventory-refresh.yaml).
The 12 additions initially entered the queue as NOT_STARTED; their subsequent audit states are recorded below. Every module starts unaudited for this project, including the
20 already labelled COMPLETE. Structural counts are triage aids, not biological
judgments. Recheck upstream for new, renamed and removed modules before declaring
this project finished. Open PR overlaps are leads to inspect, not proof that the
work has been done; broad PR #5076 alone overlaps many modules.

For each module, record evidence that all of the following are satisfied:

1. Review literature was searched; relevant references have manual assessments and
   mined findings, corroborated with primary work for decisive mechanistic claims.
2. Individual steps and their connections cite evidence appropriate to the claim.
3. The taxonomic envelope and lineage-specific alternatives are explained without
   asserting universal presence from sparse samples.
4. Each applicable leaf has a verified family selector and informative exemplars
   spanning the relevant scope; missing family IDs stay unasserted until established.
5. Each exemplar has an individual gene review with source-specific reasoning,
   validation and session provenance. Unresolved biology is documented explicitly.
6. A module-specific PR has passed required checks, addressed review feedback and
   merged. Record its number and merge commit before marking the audit complete.

## Status

- [ ] `bacterial_methionine_cycle`: Comparative audit passes full validation on 125cfcb38c: 10,801 reviews, zero blocking errors and 727 frozen inputs verified. Publication, fresh review/CI and actual merge remain pending.

- [ ] `bacterial_isc_iron_sulfur_cluster_assembly`: PR #6175 scientific review follow-up passes full validation on 31d0901593; main 0a807fc555 is integrated with 320 frozen nonshared inputs preserved. Fresh review, CI and actual merge remain pending.

- [x] `bacterial_cellulose_biosynthesis`: PR #2143 actually merged as 0a807fc55576d0371b2dfacb482f8d695992535b; 291 changed nonshared files are byte-identical to the reviewed head and 21 changed reviews remain COMPLETE with no PENDING rows.

- [ ] `bacterial_flavonoid_degradation`: PR #6140 scientific review follow-up passes full validation on ee4222b667; main 5b68ef3aac is integrated with 361 frozen nonshared inputs preserved. Fresh review, CI and actual merge remain pending.

- [ ] `bacterial_choline_o_sulfate_uptake_and_desulfation`: PR #6105: integrated main 2f72fda87e into approved head 41649e7eae, preserving all frozen scientific inputs. Fresh review and CI on the integration head, followed by actual merge, remain pending. Historical full validation is scoped to its recorded science head.

- [ ] `bacterial_cytochrome_c_maturation_system_i`: PR #6121 provenance/CcmE follow-up passes full validation on 072461b9b2: 10,722 reviews, zero blocking errors and 374 frozen inputs verified. Fresh review, CI and actual merge pending. [PR #6121](https://github.com/ai4curation/ai-gene-review/pull/6121).

- [ ] `bacterial_ethanolamine_uptake_catabolism`: Comparative audit and full validation complete locally; adopted PR5970 update, renewed review, CI and actual merge pending [PR #5970](https://github.com/ai4curation/ai-gene-review/pull/5970).

- [ ] `bacterial_fatty_acid_beta_oxidation`: Comparative beta-oxidation curation covers 19 COMPLETE gene reviews across seven species and three bacterial phyla, preserving all 211 original annotation payloads, both inherited NEW rows and 40 raw/provider files. Six supported additions yield 217 rows. Seventeen references, including four review articles, supply 21 mined findings. Four required reactions use ten alternatives and eight reviewed protein families. Unknown physiological electron acceptors, matched partner requirements, substrate limits and distinct native versus biochemical endpoints are explicit. The source-scoped checker uses the production module circuit with 54 cases and 12 mutation checks; passing cases do not replace the literature assessment. Focused checks and full-corpus validation passed on 2026-11-06 (10,688 reviews; zero blocking errors). Corpus advisory reference issues outside this panel remain recorded in the validation proof. Published as [PR #6136](https://github.com/ai4curation/ai-gene-review/pull/6136); independent review, CI and actual merge remain pending.

- [ ] `bacterial_dsbab_oxidative_folding`: PR_OPEN. [PR #6129](https://github.com/ai4curation/ai-gene-review/pull/6129) contains fourteen completed gene reviews, fourteen curated references and 75 capacity cases. Full validation found only verified pre-existing reference errors; external review, CI and actual merge pending.

- [x] `osmoregulated_periplasmic_glucan_biosynthesis`: [PR #2142](https://github.com/ai4curation/ai-gene-review/pull/2142) merged at `fb8e3ee95b`; 179 scoped files verified identical to the approved head.

- [ ] `bacterial_chromosomal_dna_replication`: COMPLETE module; 52 completed gene reviews, 37 references and 97 passing capacity cases cover twelve required duplication roles. All 1,067 historical rows and 104 raw files are preserved. Full validation is terminal with 19 proven pre-existing reference errors in 17 unrelated yeast reviews (23 unchanged input blobs); no scoped blockers. PR [#6117](https://github.com/ai4curation/ai-gene-review/pull/6117) includes the validated review corrections; fresh external review/CI and actual merge remain pending.

- [ ] `bacterial_divisome_peptidoglycan_transpeptidation`: PR_OPEN. [PR #6123](https://github.com/ai4curation/ai-gene-review/pull/6123) includes nine completed member reviews, fourteen curated references and 57 capacity/evidence checks. Full validation found only verified pre-existing reference errors; renewed review, CI and actual merge remain pending.

- [x] `bacterial_assimilatory_nitrate_reduction`: [PR #5740](https://github.com/ai4curation/ai-gene-review/pull/5740) merged as `62f214ee641ee2c662c58c8e40a6eeba6a39c7f0` at 2026-10-30T06:46:53Z. All 209 scoped source/curation/history blobs match the approved head; 21 member reviews are COMPLETE with no PENDING annotations. [Merged-content proof](MODULE_TAXON_AUDIT/proofs/pr5740-merged-content.json). PR #5928 is a separate family-review follow-up.
- [x] `bacterial_aspartate_to_threonine_biosynthesis`: [PR #5858](https://github.com/ai4curation/ai-gene-review/pull/5858) merged as `225589950bb458a00b76f46024480ac6f68b76a6` at 2026-11-01T23:27:51Z after approval of `f074ad3642687ea4d2bb6eeb02757e2028e8b37e` and passing required/queue checks. All 152 scoped blobs match the approved head; 20 reviews, 192 machine rows and 40 raw sources are preserved. Final 193 rows include one restored inherited authored proposal; two others remain retired.
- [x] `bacterial_beta_aryl_ether_dimer_cleavage`: [PR #5930](https://github.com/ai4curation/ai-gene-review/pull/5930) merged as `22ee0c020b11a0455c6e75da1a36fb59af729954` at 2026-11-03T05:26:24Z after approval of `f54046b04cea6bb86bc49c9d38e5f06776aabaef` and passing head/queue checks. All 153 scoped blobs match the approved head; 16 COMPLETE reviews, nine original annotation rows and 32 raw sources are preserved, with no NEW annotations. [Merged-content proof](MODULE_TAXON_AUDIT/proofs/pr5930-merged-content.json).
- [x] `bacterial_c_di_amp_signaling`: [PR #5997](https://github.com/ai4curation/ai-gene-review/pull/5997) merged as `ad87fb94656fdac3baab05c26d9f22af6549607a` at 2026-11-05T07:10:18Z after approval of `46450254fe474862ee723803c4347d875f34d8b0` and passing head/queue checks. All 166 scoped blobs match the approved head; 17 COMPLETE reviews preserve 89 original rows and 34 raw sources, with nine NEW annotations and two explicit UNDECIDED claims. [Merged-content proof](MODULE_TAXON_AUDIT/proofs/pr5997-merged-content.json).
- [ ] `bacterial_c_di_gmp_signaling`: Audit in progress on 17 reference proteins spanning Pseudomonadota, Bacillota and Spirochaetota. Reworked local/global signalling, optional DdpA context, verified family selectors and gene reviews; Scoped validation is complete; the full run reports only 19 documented pre-existing citation failures outside this module. [PR #6062](https://github.com/ai4curation/ai-gene-review/pull/6062) is open; independent review, CI and actual merge remain pending. The original nitrate audit PR #5740 is verified merged; follow-up PR #5928 is tracked separately.

- [x] `bacterial_ammonia_assimilation`: [PR #5696](https://github.com/ai4curation/ai-gene-review/pull/5696) merged as `fc3465b477b55d7ee05ffcb7eb4c15e315967029` at 2026-10-28T20:07:15Z. All 126 scoped source/curation/history blobs match the approved head; 12 member reviews have no PENDING decisions. All member review statuses are COMPLETE. [Merged-content proof](MODULE_TAXON_AUDIT/proofs/pr5696-merged-content.json).

- [x] `2_aminoethylphosphonate_degradation`: [PR #5538](https://github.com/ai4curation/ai-gene-review/pull/5538) merged after approval and required checks, at `7d28f887b2dbbab34afee940716ba660efc3a173`. Six member reviews, comparative literature, step/edge evidence and taxon/family grounding were rechecked in the merged content.
- [x] `abscisic_acid_signaling`: [PR #5540](https://github.com/ai4curation/ai-gene-review/pull/5540) merged as `d4ae4f02f7ab9759d41d104d7cd7af0ec66abb16`. All 19 reviews (524 rows), 26 references and lineage-specific signaling constraints were verified in merged content after approved checks.
- [x] `acetylcholine_signaling`: Merged PR #5582 at e145466d152df2f67b82bbe3f775c7a4b43040ce after approval of 00eb524d6e and passing required checks. Verified 722 scoped paths against the approved head; 44 member reviews, 2786 original annotation rows and 88 raw sources are preserved.
- [x] `activin_receptor_signaling`: [PR #5541](https://github.com/ai4curation/ai-gene-review/pull/5541) merged as `aff0030d3689b50ae9f6d147fc8334a0b942f0a7`. All 11 reviews, 29 references, taxon/step evidence and session histories were verified unchanged from the approved head.
- [x] `adp_heptose_biosynthesis`: [PR #5542](https://github.com/ai4curation/ai-gene-review/pull/5542) merged as `8954a5dc480f1311f440eb4e50f5cefca5931980` after approval and required checks. Its 16 member reviews, 12 references and 26 histories were inspected; 44 curated/history files match the approved head.
- [x] `adrenal_steroidogenesis`: [PR #5571](https://github.com/ai4curation/ai-gene-review/pull/5571). Merged as `38c2b634f063c40c1e957bde87be87050daed719` after approval and passing checks. All 31 scoped curation, history and source files match approved head `74e860184b`. The corrective merge retains 22 supported organelle assertions across seven genes and preserves all 320 affected rows; the full module audit covers thirteen members.
- [x] `aerobic_nicotinate_degradation`: [PR #5544](https://github.com/ai4curation/ai-gene-review/pull/5544) merged as `94a80ada9f7143d2fb1b38b5e97a5301859c0a7c`. Twelve references and twelve member reviews (43 rows) were verified; 64 scoped curated/history files match the approved head. The NicD localization supersession is recorded in the older audit ledger.
- [x] `alcoholic_fermentation`: [PR #5572](https://github.com/ai4curation/ai-gene-review/pull/5572). Merged as `fe302bb372e476d4c1d6911c825e33bb49c23eac` after approval and passing checks. All 6 scoped curation, history and source files match approved head `337db24a4f`. The corrective merge retains both SCHPO adh4 mitochondrial assertions beside matrix assertions and preserves all fifteen affected rows.
- [x] `alginate_o_acetylation`: [PR #5546](https://github.com/ai4curation/ai-gene-review/pull/5546). Merged as `47f648bb3d97f15c19051afb270c527728b17e51` after current-head approval and passing required checks. All 83 scoped curation/history files match approved head `f15f9ec44b`; 12 reviews, 52 rows and 15 references are verified.
- [x] `alginate_polymerization_export`: [PR #5552](https://github.com/ai4curation/ai-gene-review/pull/5552). Merged PR #5552 as 2bb4ff1c018298e73c1ebd054a6e02949a2cd163 at 2026-10-26T17:25:41Z, after exact-head approval of efc62375b8ac2974d47ea2aaac0cdf8b9e920907. All 142 scoped approved science/source/history blobs match the actual merge; 21 reviews, 116 final rows, 42 raw sources verified. Three approved reviewer-authored ISS proposal source corrections are recorded separately from unchanged machine payloads; all 116 rows remain present.
- [x] `aliphatic_glucosinolate_myrosinase_defense`: [PR #5550](https://github.com/ai4curation/ai-gene-review/pull/5550) merged as `75d569bf94a697ed142f0f1397736819563b8d74`. All 187 scoped files from the 208-file paginated PR match the approved head; 35 reviews, 453 rows and 31 curated references are verified.
- [x] `androgen_receptor_signaling`: [PR #5554](https://github.com/ai4curation/ai-gene-review/pull/5554). Merged PR #5554 as 70a5964a22d14e7972cfb43fe02095aa4cb8a7c1 at 2026-10-26T15:23:25Z after current-head approval and successful queue checks. All 270 scoped science, source and history blobs match approved head 93ce23a1a7d136ce286372b29b6e3174abc45979. Fifteen reviews and 1,683 original rows are preserved.
- [x] `anti_crispr_suppression`: [PR #5555](https://github.com/ai4curation/ai-gene-review/pull/5555). Merged PR #5555 as aa66b5213685b58a3a8c3d5503aa1c44411c9b5e at 2026-10-26T17:25:40Z, after exact-head approval of 76b0361126d8dbe5cf7c170acf34d289426c9c2e. All 114 scoped approved science/source/history blobs match the actual merge; 13 reviews, 42 final rows, 26 raw sources verified.
- [ ] `apoptotic_execution_phase`: [PR #5558](https://github.com/ai4curation/ai-gene-review/pull/5558) merged as `6cea7bd0a5c9ed4fa53bd44e7c9cafd4185e338a` at 2026-10-27T18:54:34Z. All 185 scoped source/curation/history blobs match the approved head; 16 member reviews have no PENDING decisions. DIABLO still has DRAFT metadata; a module-specific follow-up remains before audit completion. [Merged-content proof](MODULE_TAXON_AUDIT/proofs/pr5558-merged-content.json).
- [x] `aps_dependent_assimilatory_sulfate_reduction`: [PR #5560](https://github.com/ai4curation/ai-gene-review/pull/5560). Merged as `6349c3ef3ea2c8604949502686281dde0c0aaa7a` after approval and passing checks. All 226 scoped curation, history and source files match approved head `8553f16ce5`. The audit covers 29 member reviews, 496 rows, 28 curated references and five qualified connections.
- [x] `arginine_biosynthesis`: [PR #5563](https://github.com/ai4curation/ai-gene-review/pull/5563). PR #5563 merged as bfd5d651c11e41f1c509f167bb15a003c2da4bc3 at 2026-10-26T16:46:07Z, after approval of b4971234e3c94371d017b6ea69791c636e4b730f. All 276 scoped approved science, source and history blobs are identical in the merge. The module has 43 reviewed members and 555 annotation rows; the shared CAR1 comparator is included in the wider content proof.
- [x] `arginine_catabolism_arginase_pathway`: [PR #5566](https://github.com/ai4curation/ai-gene-review/pull/5566). Merged PR #5566 as bb5f066dbaf3d5d968bde928c8852ea0d4062408 at 2026-10-26T17:52:57Z, after exact-head approval of 90bdd63dec857b055c5f9f9a03fd5a15c7209bec. All 144 scoped approved science/source/history blobs match the actual merge; 18 reviews, 359 final rows, 36 raw sources verified. The correct total is 357 original rows plus two supported ARGAH matrix proposals, giving 359 final rows.
- [x] `aspartate_asparagine_metabolism`: [PR #5568](https://github.com/ai4curation/ai-gene-review/pull/5568). PR #5568 merged as 551ec0d1221116c8753105bed861739daf5a6479 at 2026-10-26T17:07:11Z, after approval of 2c004eaaf8eab6febfe5abceb00f2f9ebce37b71. 406 of 407 scoped blobs are identical to the approved head. The sole exception is the shared GO-CAM index: a clean three-way merge with the independently merged threonine update reproduces the final index byte-for-byte. All 27 reviews, 548 annotation rows and 54 raw sources are preserved.
- [x] `aspartate_family_threonine_biosynthesis`: [PR #5569](https://github.com/ai4curation/ai-gene-review/pull/5569). PR #5569 merged as 3dd6e1dba91d22efd7bed30faeb9fbe6813925f8 at 2026-10-26T17:00:27Z, after approval of e12e959a11f41f682bfd71e9c567e227fee875b6. All 315 scoped approved science, source and history blobs are identical in the merge, including 24 reviews, 439 annotation rows and 48 raw files.
- [x] `autonomous_flowering_pathway`: [PR #5574](https://github.com/ai4curation/ai-gene-review/pull/5574). Merged PR #5574 at 9c626393756af403d2700b57f66374fae6a1331f after approval and passing checks. All 153 branch-scoped files, and the entire committed tree, match approved head b483aad33dd72e8ac687827a21834d161740077e. Fifteen reviews, 304 rows, 34 assessed references and ten connections are preserved.
- [x] `auxin_nuclear_signaling`: [PR #5576](https://github.com/ai4curation/ai-gene-review/pull/5576). Merged PR #5576 as 77121ffa32de060d9b717476356f41f2fabef3e3 at 2026-10-26T14:17:11Z after approval and passing checks. All 133 scoped science/history files match approved head c2b52875f38fa802ce967fbe9541025bc9652976. Fourteen reviews, 633 current rows, 29 references and thirteen connections remain verified.
- [x] `auxin_polar_transport`: [PR #5579](https://github.com/ai4curation/ai-gene-review/pull/5579) merged as `414b8d6a53e252e5aacc8fd7d45e1ad259ac0f6f` at 2026-10-29T15:36:36Z. All 229 scoped source/curation/history blobs match the approved head; 17 member reviews have no PENDING decisions. All member review statuses are COMPLETE. [Merged-content proof](MODULE_TAXON_AUDIT/proofs/pr5579-merged-content.json).
- [x] `b_cell_receptor_signaling`: [PR #5584](https://github.com/ai4curation/ai-gene-review/pull/5584). PR #5584 merged as 67e246011a263eeb00e61ef5219ee2fb8720d069 at 2026-10-26T17:21:03Z from approved head 49a03553b5d92f4e5162fb6514d4d26ba52b5ccc. Independent verification proves all 340 scoped gene, module, source and history blobs identical, with no exceptions. All 22 reviews and 2,645 original annotation payloads, including two inherited proposals, are preserved.
- [x] `bacterial_23s_rrna_m5u747_methylation`: [PR #5586](https://github.com/ai4curation/ai-gene-review/pull/5586). PR #5586 merged as 73657c1c70ac8806605910fadf123f60a3697cdc at 2026-10-26T16:59:36Z, after approval of cb5e106fdbe7aa0d29b116e2590a8590d493a96f. All 73 scoped approved science, source and history blobs are identical in the merge, including five reviews, 55 annotation rows and ten raw files.
- [x] `bacterial_2_3_butanediol_acetoin_catabolism`: Merged PR #5588 at 26807f2d0fdad001373db13ccb217173fcca1f4b after approval of 6ae71843c5 and passing required checks. Verified 174 scoped paths against the approved head and 2 shared-file automatic three-way unions; 20 member reviews, 83 original annotation rows and 40 raw sources are preserved with the explicitly documented authored-proposal supersessions.
- [x] `bacterial_4_hydroxybutyrate_oxidation`: Merged PR #5591 at e35438d6a9c450e03856faea0d93ac0abcec0cf2 after approval of 7d217c9452 and passing required checks. Verified 63 scoped paths against the approved head; 6 member reviews, 28 original annotation rows and 12 raw sources are preserved.
- [x] `bacterial_alkanesulfonate_uptake_desulfonation`: Merged PR #5593 at 384ea94e250c3aab07442ae0a08185c66ebffefe after approval of 00a883c844 and passing required checks. Verified 120 scoped paths against the approved head; 15 member reviews, 104 original annotation rows and 30 raw sources are preserved.
- [x] `bacterial_alkyl_hydroperoxide_reductase`: [PR #5595](https://github.com/ai4curation/ai-gene-review/pull/5595) merged as `2d4b5ac0f19441c4b00fb7b3e5cfd43b2189f014` at 2026-10-29T02:25:50Z. All 196 scoped source/curation/history blobs match the approved head; 15 member reviews have no PENDING decisions. All member review statuses are COMPLETE. [Merged-content proof](MODULE_TAXON_AUDIT/proofs/pr5595-merged-content.json).
- [x] `bacterial_aminoacyl_trna_charging`: [PR #5616](https://github.com/ai4curation/ai-gene-review/pull/5616) merged as `6f56c0addf030cb02af4c8ba7e8dfd470e8762ab` at 2026-10-30T03:27:06Z. All 314 scoped source/curation/history blobs match the approved head; 42 member reviews have no PENDING decisions. All member review statuses are COMPLETE. [Merged-content proof](MODULE_TAXON_AUDIT/proofs/pr5616-merged-content.json).
- [ ] Ledger snapshot after this integration: 777 modules; 35 COMPLETE, 9 PR_OPEN, 4 IN_PROGRESS, 729 NOT_STARTED. Counts retain dated row evidence and are not a fresh global GitHub survey.

## Notes

### 2026-10-25

The initial inventory found 682 DRAFT and 20 COMPLETE modules. A survey of 239 open
PRs, with a separate paginated file listing for #5076, found overlapping PRs for 318
current modules. GitHub's other PR file lists can be truncated; check exact paths
before assigning a module or treating an apparent absence as definitive.

The first audit uses the 2023 phosphonate-catabolism review (PMID:37836707), primary
PhnW biochemistry (PMID:12107130), comparative Bacillus/Salmonella PhnX biochemistry
(PMID:9649311), and alternative oxidative entry pathways (PMID:37876809). It preserves
the distinction between assayed proteins and homology-based KT2440 assignments.
Falcon/fallback research requests for new members failed authentication or quota
checks; individual notes document manual primary-literature research instead.

The ADP-heptose audit also checks the protein architecture boundary: standalone
HldA/HldC, bifunctional HldE and trifunctional SepB provide different implementations
of the same reactions. Archived DSM2067 records preserve strain identity after UniProt proteome pruning;
only the kinase has an exact published-construct match, while three assignments remain qualified; the engineered S2 host is not mislabeled
as an endogenous producer. The overlapping broad PR #5076 supplies ancestry edits
but does not replace this literature, taxon and member audit.

### 2026-10-26

Verified nicotinate merge content and continued the alginate and glucosinolate audits. The glucosinolate critical review supports Brassicaceae scope for chain-elongated methionine chemistry; broader glucosinolate occurrence is not evidence for this complete pathway. Family membership checks preserve dual P450 assignments and distinguish demonstrated single-member activity from unresolved subfamily boundaries.

The alginate acetylation audit deliberately uses `algV` for Azotobacter O52197, whose current UniProt primary name is `algJ` and synonym is `algV`. The alias distinguishes this acetylation protein from the historically named outer-membrane export AlgJ (Q44497, now `algE`); it is an explicit curation naming choice, not the fetched primary symbol. The final panel has 42 original GOA rows, four retained older proposals and six added proposals (52 total). Full validation has passed. History totals are reported by target scope rather than a moving PR delta after upstream merges.

## 2026-10-26 — subsequent audit progress

Glucosinolate reached approved merge-queue checks after source-level corrections. Alginate polymerization received coherent comparative molecular-function proposals and explicitly qualified PseudoCAP source-defect records. Androgen passed full validation and opened its own PR. Anti-CRISPR curation is committed while its single full validation continues. Apoptotic execution is the thirteenth started audit; conflicting Acinus evidence, AIF stimulus dependence and source-versus-function caspase adjudications are being examined rather than flattened into a uniform cascade.

## 2026-10-26 — sulfate integration and arginine expansion

All sulfate member panels are integrated (29 reviews, 496 rows); independent module QA retains measured chemistry separately from inferred native electron-carrier pairing. Full validation is running. Arginine review now covers the 39 original members, with literature-driven plant and archaeal sampling being developed. The shared automated-review failure is diagnosed from full workflow logs as an account usage limit; no scientific review ran for the latest affected heads. Build checks and independent curation continue, without bypassing approval.

## 2026-10-26 — forty-three arginine member reviews validated

The arginine member panel is complete: 43 proteins and 555 preserved annotation rows, including 2 prior proposals and no newly added rows. All focused member checks, histories and renders pass; full validation is running. The added archaeal ArgJ is recycling-only, plant NAGK/WIN1 anchor plastid reactions, and short mycobacterial ArgA retains its weak glutamate-efficiency caveat. Independent module QA remains in progress. Sulfate is committed and its full reference validation continues. Apoptosis PR #5558 is open; its automated review also hit the shared account quota before producing a verdict. The eight verified merges remain the only completed baseline audits.

Independent arginine module QA is now complete: all 43 family/member placements agree with fetched classifications, cached GO-CAM assertions were checked, and 22 curated references support 9 connections. The draft no longer attributes type 2 ArgC classification to an unrelated review passage or restricts ArgA initiation to the linear release route. Full validation remains the outstanding pre-PR gate.

## 2026-10-26 — arginase catabolism and CI follow-up

The sixteenth audit separates demonstrated budding-yeast compartmental flux from broader fungal inference, restores the fission-yeast Arg3 re-synthesis context, and adds the distinct plant arginase/agmatinase family. Thirty-two sources and four evidence-backed connections are drafted. Sulfate and arginine full validation remain live. Apoptosis CI exposed a real module logic failure: an empty context satisfies its current all-optional structure. A biology-aware correction is underway; no approval or merge gate is bypassed.

Sulfate full validation reached terminal success, current-main integration preserved all 197 scoped files, and PR #5560 is open. The apoptosis Boolean correction is published as `b4f92e028b` with 54 passing logic tests. All 18 arginase member checks now pass (357 preserved rows, no newly added rows); a direct ARGAH2 agmatinase result exposed an overly narrow family-level scope, which is being corrected from primary evidence.

Independent arginase QA now passes: 34 source entries, four evidence-backed connections, 46 module-logic tests and 14 route cases. The PTHR11358 SF32 correction retains all existing PAINT assertions and APAUH exceptions; the global family/gene crosscheck reports zero conflicts across 734 families. All eighteen gene reviews are committed as `bfdb0069d7`; full validation is running before PR creation.

The latest sulfate scientific-review run `40270283163` and corrected apoptosis run `40270373152` both ended with the verified account-usage-limit diagnostic before producing a review. Their build checks continue; no review approval is inferred from a workflow failure.

## 2026-10-26 — aspartate/asparagine audit begins

Arginine full validation and all 46 module-logic tests passed; PR #5563 is open. The seventeenth audit starts from a clean current-main worktree with 25 planned member reviews. The taxon boundary must distinguish the eukaryotic formation/turnover module from bacterial asparaginase comparators, add the plant N-terminal-nucleophile implementation, and avoid treating all reactions as glutamate-dependent transamination. Literature searches located comparative aminotransferase, ASNS and asparaginase reviews plus primary plant and fungal studies. The sulfate CI validation and suite jobs passed; remaining CI and scientific-review gates are still required.

The aspartate/asparagine panel expanded to six Arabidopsis proteins after the plastid review identified two distinct AspAT implementations. All 27 reviews now pass with 548 preserved rows and no added annotations. Independent QA confirmed nine family labels, 25 exemplar placements and 12 exact GO-CAM activity links. Thirteen route cases pass. The newer ASP3 evolutionary evidence is reconciled into PTHR11707 without changing PAINT seeds or verdicts. Full validation is running.

Arginase full validation passed with terminal exit zero and PR #5566 is open. Final Asp/Asn scientific QA corrected three negative localization rationales to UNDECIDED while retaining two directly assayed ASP5 negative enzyme activities. Final 548-row totals are 323 ACCEPT, 110 MODIFY, 65 non-core, 20 REMOVE, 25 UNDECIDED and 5 over-annotation assessments. No new annotations were added.

## 2026-10-26 — threonine backbone audit starts

Asp/Asn curation is committed and pushed as `98bd4c37e3`; full validation is still running. The eighteenth audit uses an independent worktree and 24 planned gene reviews. Two archaeal enzymes establish specific step exemplars, not an entire archaeal pathway. The proposed Arabidopsis ASAD locus At1g14810 lacks an official gene symbol and currently has prediction-heavy annotation; independent evidence must determine the strength of that exemplar. ThrH uses phosphoserine rather than ATP, plant O-phosphohomoserine also feeds methionine, and new Hom6/chromatin literature requires separation of metabolic and noncanonical effects.

## 2026-10-26 — review follow-ups and completed threonine member panels

Scientific review resumed for several PRs after earlier service quota failures.
Sulfate evidence corrections are published with focused validation. Arginine
review exposed an explicit root-organelle exception that also affects 22
aspartate/asparagine rows; both sets are being corrected before completion.
The arginine suite failure is two stale TreeGrafter ledger outcomes, not a
reason to revert supported biological decisions.

All 24 threonine member reviews now pass focused checks with 438 original
annotation payloads preserved. Their final 439 rows comprise 321 ACCEPT,
81 MODIFY, 18 KEEP_AS_NON_CORE, 10 REMOVE, six UNDECIDED, two
MARK_AS_OVER_ANNOTATED and one NEW stromal localization. Current GO-CAMs now
have forward causal edges missing from older cached models, and the module
revision is checking those current assertions. No new module is counted as
complete before its reviewed PR merges and the merged content is verified.

Threonine integration caught and corrected a negative-annotation error: ThrH’s experimentally supported NOT ATP-dependent kinase assertion is ACCEPT, while its positive phosphoserine-dependent phosphotransferase assertion remains separate. Final panel counts above include this correction.

## 2026-10-26 — completed follow-ups and full-validation gates

Five review follow-ups are published: androgen, anti-CRISPR, sulfate,
arginine biosynthesis and arginase catabolism. The apoptosis review is now
being addressed in two focused panels. A single alginate-acetylation review
retry follows observed recovery of the normal review service; no approval
gate is bypassed. Alginate polymerization is approved but retains its explicit
draft dependency on acetylation.

Aspartate/asparagine passed its first full validation, then received a fresh
full run after organelle-policy corrections. Threonine curation and independent
QA are complete and its first full run is live. Neither PR is opened before
terminal full-validation success. A retrospective read-only check is also
examining the eight previously merged audits for the newly noticed systematic
policy errors; any substantive finding will reopen the affected module rather
than treating prior approval as proof that it is correct.

## 2026-10-26 — two merged audits reopened after policy QA

The scoped retrospective check found 22 root-organelle refinement violations
across seven adrenal-steroidogenesis representatives and two in the fission-yeast
fermentation exemplar adh4. The other six previously merged modules have no
candidate root-organelle violations in their representative reviews, and no
curation-only/ontology-only module gaps were found in the eight-module check.
Adrenal and fermentation are reopened: prior approved merges remain provenance,
not evidence that these newly identified defects are acceptable. Separate
module-specific corrective PRs are required. Current baseline accounting is
six complete, twelve active/reopened and 684 not started (702 total).

## 2026-10-26 — two validated audits published and review corrections completed

Aspartate/asparagine and threonine passed full repository validation and opened separate PRs #5568 and #5569. Source-specific apoptosis corrections are published, including all 37 caspase uncertainty reassessments. Androgen and sulfate received approval before their remaining citation details were corrected in small follow-ups. Adrenal and fermentation corrections are committed on separate fresh branches and undergoing full validation. No open or reopened audit is counted complete.

Reconnaissance has started for the autonomous flowering pathway. The full Arabidopsis mechanism must be distinguished from comparative protein roles in other plants; both older claims of universal conservation and categorical absence of cereal FLC relatives need source-specific examination. Nineteen baseline modules have now entered audit; six remain verified complete.

## 2026-10-26 — corrective PRs, source-grounded flowering panel and review follow-up

Adrenal and fermentation corrective states passed full repository validation and opened PRs #5571 and #5572. Arginase has current-head approval and passing CI and is queued for merge. No queue entry is counted as a completed audit. Four terminal automated-review execution failures received one controlled retry each; scientific change requests remain separate from job failures.

The flowering panel covers 15 proteins and 303 final rows, with 302 pre-existing payloads preserved. Native Arabidopsis FLC regulation is distinguished from rice comparative protein evidence. Threonine and apoptosis review requests are being addressed; the apoptosis public node identifier is restored locally to preserve upstream TRAIL references. Six baseline audits remain verified complete, thirteen active (including two reopened), and 683 not started.

## 2026-10-26 — preserve reviewed biology through upstream merges; start auxin audit

Published apoptosis second follow-up and preserved its shared TRAIL target. Integrated upstream section backfills into alginate, sulfate and arginase without changing approved gene/module biology; updated heads need renewed approval and CI. Controlled review-job retries also failed without verdicts, so no approval is inferred. Autonomous flowering is committed and pushed while full validation remains active.

The twentieth audit, nuclear auxin signaling, has a 14-target, 632-row baseline and native Marchantia exemplars resolved to published clones/loci. Recent receptor adenylate-cyclase evidence and the 2015 primary-source correction will be assessed explicitly. Six baseline audits remain complete, fourteen active, 682 unstarted.

## 2026-10-26 — flowering PR, preserved integrations and complete inventory refresh

Published flowering PR #5574 after terminal full repository validation. The rebase preserved both branch commits exactly. Arginine, aspartate/asparagine and threonine integrate upstream metadata with their reviewed curated content byte-identical; the threonine scientific follow-up is separately recorded. Renewed reviews and CI are still required. Automated-review execution failures do not count as approvals or resolution of prior scientific requests.

Refreshed the module universe against `10fd59941f`: 12 additional modules are now explicitly tracked, for 714 total (six complete, fourteen active/reopened, 694 not started). The additions are `acetylcholine_signaling`, `dna_cytosine_methylation_cycle`, `dopamine_receptor_signaling`, `il21_signaling`, `il22_signaling`, `il34_signaling`, `nmj_achr_clustering`, `prostanoid_biosynthesis`, `protein_kinase_c_signaling`, `reelin_signaling`, `trail_apoptotic_signaling`, `visual_phototransduction`. All require the same literature, taxon, family, member-review and merged-PR evidence as the original 702.

## 2026-10-26 — nuclear auxin committed; polar transport review started

The nuclear auxin audit now has 14 complete member reviews, 633 rows, 29 assessed references and 13 supported edges. The TIR1 route requires its demonstrated cyclase activity; AFB2 and Marchantia activity remain unresolved. Exact ARF partner evidence was recovered normally and all source follow-ups preserve original payloads/actions. Independent scientific QA passes. Full validation restarted after an environmental disk-space failure; its earlier log is retained and no successful run is inferred from focused checks.

The polar-transport audit starts with 17 products and 483 original rows. An APFS copy-on-write checkout preserves full tracked content and independent edits without duplicating the repository data; this resolved the disk problem after Orca runtime and ordinary checkout failures. Current PR build checks pass, but automated scientific-review failures still prevent approval on pending branches. Six audits remain complete, fifteen active/reopened, 693 unstarted of 714.

## 2026-10-26 — nuclear auxin PR and comparative transport reviews

Nuclear auxin full repository validation reached terminal success and PR #5576 is open. Its 14 committed reviews match the final payload and source checks. The five polar-transport comparative reviews are complete, preserving 28 original rows plus one independently supported OsAUX1 influx proposal. The Arabidopsis panels and context-specific module integration continue. Six audits remain verified complete; opening a PR does not count as completion.

## 2026-10-26 — polar transport committed; acetylcholine audit starts

The 200-path polar-transport curation is committed in three scoped commits, ending at 822c77c674. All 17 gene reviews preserve 483 original payloads and add only OsAUX1 influx activity. Full repository validation is running on the completed curation. Review and native primary evidence distinguish transporter activity, tissue polarity and complete network conservation; a 2026 moss phyllid study refines the stage boundary. The next audit begins with the acetylcholine module and its 35 direct products plus VAChT interface, without dropping difficult subunits or treating a family label as functional evidence. Its isolated checkout is clean and dependency setup passed. No new audit is counted complete before reviewed merge verification.

Acetylcholine literature supports eight additional exemplars: human GNB5 for the RGS6 complex, mouse Chrm2/Rgs6/Gnb5 for native cardiac regulation, and rat and chicken alpha9/alpha10 receptors for directly compared species differences. Their verified identities give a planned 44-product panel. Comparative segments remain distinct from the complete human transmission mechanism.

## 2026-10-26 — shared-source repair and acetylcholine evidence integration

Polar transport full validation reached a terminal reference-check failure in the preexisting CHL1 alias of NPF6.3. Normal shared-source refresh exposed title-only quotations; nine quotations were replaced by actual source-body text, with all annotation payloads and actions unchanged. The three-file companion is committed and passes strict validation. The new full run is live; no PR is opened before terminal success, and the companion is not presented as a complete additional gene review.

Acetylcholine now has 32 family-grounded activities, 35 assessed references and evidence on every retained connection. Twenty nicotinic and nine supply/clearance/muscarinic member reviews pass strict validation and preserve all original rows. The remaining regulator panel and independent module checks continue. Direct coupling, effector assays, physiological inference and chemical continuity are kept distinct. The requested flowering rebase preserved all three commits by range-diff; the pushed head has fresh CI/review jobs. Six of 714 audits remain verified complete.

## 2026-10-26 — completed member reviews and open scientific follow-ups

Polar transport passed full repository validation (session 89160: 9,077 gene reviews and 54 pathway files) and opened PR #5579 at `248f567e19`; CI and scientific review are running. The flowering PR #5574 received CHANGES_REQUESTED at `9135cacef9`, with concrete SOC1 evidence preservation, FLK specificity, status and prose corrections under way. These are review follow-ups, not new completed audits.

All 44 acetylcholine reviews are COMPLETE. The 2,786 preserved original rows comprise 1,330 ACCEPT, 638 MODIFY, 418 KEEP_AS_NON_CORE, 270 REMOVE, 110 UNDECIDED, 19 MARK_AS_OVER_ANNOTATED and one inherited NEW; no new proposals were added. The completed module contains 38 family-grounded activities and 38 assessed references with evidence on every connection. Focused checks pass for all 44 reviews, 39 route cases (18 receptor plus 21 signaling) and all 672 replacement aspects. The three science commits end at `cde0859bff52e961f09856ddff278dfc1a2d7597`; full repository validation is live in session 14852 with log `.cache/module-audit-logs/acetylcholine-validate-all.log`. Its result is not inferred from focused success.

At the preceding tracker snapshot, 6 of 714 audits were complete, 22 had started and 692 were not started; B-cell receptor signaling was then only a preliminary survey. The subsequent start below supersedes that current-status count.

## 2026-10-26 — B-cell receptor curation starts

The 23rd audit now has a separate tracked-file APFS copy-on-write checkout on `cmungall/aigr-b-cell-receptor-taxon-audit`, verified clean at `6fb9e79b44d53f248675021c9a25f2183a9ec757`. Dependency setup is running in session 17849; the preliminary survey is copied to that checkout's `.cache/module-audit-logs/b-cell-preliminary-survey.md`. Normal gene seeding and original-payload capture are next. All seven original human products remain in scope; the inventory's six-accession list omitted PLCG2 (P16885). The planned panel has 22 verified identities: 12 human, seven mouse and three chicken. No member review is yet complete.

The audit will distinguish the default class IA/p110-delta BCR PI3K branch from contextual PIK3CG biology, place PI3K upstream of BTK recruitment, separate CD79 signal transduction from immunoglobulin antigen recognition, and establish exact taxon implementations rather than presume a fully conserved circuit. Baseline accounting is now 6 of 714 complete, 23 started (17 active/reopened), and 691 not started.

## 2026-10-26 — scientific review follow-up and seeded B-cell panel

Flowering corrections are pushed at `27613922b3`, with all 302 original annotation payloads preserved and two supported molecular-function proposals. The new full validation is live in session 11883. Polar transport received substantive scientific requests; the Q05085 duplicate, ABCB policy and prediction evidence are under review. Its CI failures were traced to a family title quote and script lint, not inferred to be transient. Acetylcholine science is pushed and its full validation session 14852 remains live. B-cell receptor normal seeding is complete: 22 products, 2,645 rows, all 1,715 preexisting rows preserved with documented deterministic augmentation. The sole-owner 748-PMID acquisition queue is live. Six of 714 module audits remain verified complete; 23 have started and 691 remain not started.

## 2026-10-26 — recovered scientific review and verified alginate merge

The review service resumed and produced current-head decisions. Alginate O-acetylation merged as `47f648bb3d`; all 83 scoped curation/history files match the approved head. This raises verified completion to seven of 714 modules. Six approved PRs were submitted for normal merge; arginine biosynthesis and arginase queue entries report integration conflicts, which remain work to resolve. No queue entry is counted as a merge. Polar transport passed its fresh full validation and was also submitted. Flowering passed fresh full validation before a content-preserving rebase; its new head now requires renewed CI/review.

Acetylcholine, apoptosis, Asp/Asn and threonine have concrete new review requests, now recorded individually above. Nuclear auxin follow-up is approved while its fresh full validation continues. The B-cell receptor audit has 18 committed source findings, a complete 749-PMID initial acquisition and seven finished member reviews preserving 802 annotation payloads. The remaining member panels and module mechanism/taxon integration continue.

## 2026-10-26 — three verified merges and continued B-cell receptor integration

Sulfate PR #5560 and the adrenal/fermentation corrections #5571/#5572 merged after approval and required checks. Direct blob comparisons found no differences across their 226, 31 and six scoped files respectively. The two reopened audits are therefore closed again, bringing verified completion to ten of 714 modules. Approved arginine, arginase and auxin PRs still need integration with newer main; a queued or requested merge is not counted as completion.

Acetylcholine follow-up d01f7211ca preserves all 2,786 row payloads and source hashes, adds thirteen manually mined findings and makes three supported peripheral-location action changes. Forty-two strict checks pass; a fresh full run remains live. B-cell receptor now has thirteen committed member reviews and 1,707 reviewed rows, with the final nine-member panel in checks. The integrated mechanism separates human class IA PI3K from the class IB gamma comparator and keeps mouse/chicken exemplars as incomplete comparative segments, not universal complete pathways.

The subsequent integrations preserved every scientific file. Renewed reviews found a tracker-only regression in arginine, arginase and polar transport: taking upstream omitted their own audit entries. Targeted entry restorations are assigned while preserving other upstream rows. Nuclear auxin and flowering received renewed approval; flowering passed all checks and was submitted for normal merge. Acetylcholine passed its fresh full validation. B-cell receptor now has all 22 reviews committed, final independent module QA passed, and full validation is live. Asp/Asn, threonine and anti-CRISPR corrections are committed, integrated and pushed with fresh full runs live. Alginate polymerization is ready after shared-AlgX compatibility checks.

## 2026-10-26 — flowering merge and rRNA specificity audit

Verified completion is now 11 of 714 modules; thirteen audits are active and 690 remain unstarted. Flowering PR #5574 merged with all 153 scoped files unchanged. The next audit compares dedicated U747 methylation with dual U747/U1939 specificity, using two bacterial phyla and a documented mollicute absence boundary. Automated reviews currently hit a session limit resetting at 14:50 UTC. Full logs distinguish partial reviews from immediate failures; five remaining ALAAT1 citation tokens are being corrected from an unfinished comment. No incomplete comment is treated as approval. Five existing full-validation processes were polled and remain live; none was restarted.

## 2026-10-26 — nuclear auxin merge, B-cell PR and completed validation runs

Nuclear auxin PR #5576 merged at 14:17:11 UTC as `77121ffa32de060d9b717476356f41f2fabef3e3` after approval and passing checks. All 133 scoped science/history files match approved head `c2b52875f38fa802ce967fbe9541025bc9652976`; completion is supported by the inspected merge proof, not inferred from a queue request. Twelve of 714 audits are now complete, twelve are active and 690 remain not started.

B-cell receptor PR #5584 is open at `499ccca22a`. Its full validation session 61187 ended successfully: 9,100 reviews valid, zero errors and 54 pathway PMID checks passed. The release audit verified 22 reviews, 2,645 preserved original payloads, 44 raw hashes and 883 committed local source dependencies. The module has 20 activities, twelve edges, 32 assessed references and 36 findings. Focused source/term checks and independent scientific QA pass with explicit CD79B contribution and core-coverage advisories; neither optional comparative segments nor structural presence tests establish autonomous native circuit sufficiency.

Three other full validation runs are now terminal with exit zero and final PASS lines: Asp/Asn session 3814 (9,098 reviews), threonine session 56949 (9,102) and anti-CRISPR session 1434 (9,092). Each reports zero errors and valid PMID citations in all 54 pathway files; repository-wide advisory warnings remain. ALAAT1's five citation-prose fixes are committed and pushed as `b402eb2fbf`. Apoptosis session 37836 remains live at the latest root poll. These validation results do not imply external scientific approval or merge.

The rRNA audit boundary has been deliberately revised from the original isolated U747 reaction to the paired U747/U1939 C5 methylation program, retaining its historical slug. Three native alternatives expose six site-specific activities: two dedicated E. coli enzymes, or dual-specific Bacillus/Streptococcus RlmCD. No catalytic order is asserted. Exact gene-product selectors carry verified PTHR11061 classification without extending substrate specificity to the whole family. Nine references include two reviews; twelve route cases pass and module validation has zero errors/warnings. All five reviews are complete with 55 preserved original rows and ten raw hashes: 28 ACCEPT, 25 MODIFY and two KEEP_AS_NON_CORE, with no NEW. Independent scientific QA passes after exact-selector and quotation fixes. All five focused source/term checks pass; two intentional E. coli advisories remain and the two RlmCD reviews have zero warnings. Full validation session 59894 is now live in `rrna-validate-all.log`. TrmA is a specificity comparator, and a mollicute U1939-only pathway is outside this paired boundary. No PR has been opened for this audit.

## Preserved branch and upstream integration notes

The dated sections below retain earlier branch-specific and upstream audit evidence. Their counts and workflow states are historical snapshots; the current inventory above governs current accounting.

## 2026-10-26 — restore the arginine audit after main integration

The arginine audit expanded the original 39-member panel to 43 proteins with recycling-only METJA/argJ, ARATH/NAGK and ARATH/WIN1, and the short MYCTU/argA architecture. Acetyl-CoA-dependent initiation and acetylornithine recycling remain distinct; short MYCTU/argA glutamine kinetics do not establish efficient glutamate turnover. Arg7 pre-import processing is distinguished from Arg5,6 import-dependent processing. The four-root taxon envelope describes sampled occurrence, without imposing a common compartment or complete pathway on every lineage.

All 555 member rows, including two inherited proposals, remain present. Independent module QA verified 43 family/member placements and checked the cached GO-CAM claims; 22 assessed references support nine connections. Historical full validation and 46 module-logic tests passed before subsequent integration. Follow-up corrected 22 root-mitochondrion actions, CAR1 urea-cycle consistency, arg3 propagation metadata and structured source defects; the latest reviewer explicitly approved the unchanged science. The current action totals are 404 ACCEPT, 102 MODIFY, 20 KEEP_AS_NON_CORE, 16 REMOVE, 10 UNDECIDED, 1 MARK_AS_OVER_ANNOTATED and 2 NEW.

Integration commit `a856224ea` retained the upstream tracker but dropped this audit's entry. This correction restores only the arginine entry among the 702 pre-existing rows, updates its structural metrics from the current module, and preserves every other existing audit row and narrative. The separate universe refresh adds twelve module paths verified on disk from the canonical inventory: eleven NOT_STARTED rows and the already published acetylcholine audit with its canonical PR evidence. Counts are recomputed for this branch rather than copied from the canonical tracker. No gene review, module or cached scientific source is changed; an active PR is not counted as complete.

## 2026-10-26 — arginase tracker restoration after integration

The integration at `78b415cf54` preserved the approved gene, family and module science but dropped this audit's tracker entry and historical notes. Restored the entry from the canonical tracker with current module-derived structure: nine family-based annotons, each with function-level evidence, 18 represented proteins, Eukaryota context qualified to characterized fungal, plant and animal implementations, 34 curated source entries and four connections. The 357 original rows are preserved; two approved ARGAH1/ARGAH2 matrix proposals bring the current review total to 359. No biological assertion was changed. The latest reviewer explicitly approves the science and requests only tracker restoration; this audit remains active until renewed review/checks and verified merge.

This branch's inventory initially contained 702 modules, not 714. Added the twelve missing canonical entries after verifying their module files: eleven remain NOT_STARTED, while acetylcholine_signaling retains its actual PR_OPEN status and evidence. The resulting 714-entry inventory has eight COMPLETE, eight active and 698 NOT_STARTED entries. Every unrelated pre-existing module entry and all upstream notes remain unchanged. These are branch-local totals, not a claim that main already carried the refreshed inventory or that an open PR has merged.

## 2026-10-26 — polar transport ledger restoration after main integration

PR #5579 scientific review approved the integrated biological content; the remaining
blocker was a tracker regression caused by selecting the upstream project files.
The restored inventory entry derives its structural counts directly from the current
module: 20 activities, each with a family descriptor and direct evidence, 41 curated
references and seven connections. Seventeen unique accessions map to seventeen
review files containing 484 rows. Q05085 is represented once as NRT1.1, preserving
CHL1/NPF6.3 alias provenance. The 483 baseline assertions, including five inherited
proposals, remain represented; the additional OsAUX1 proposal accounts for row 484.

The audit distinguishes six native Arabidopsis multiactivity mechanisms from optional
rice carrier segments and moss/Marchantia exporter comparators. Export assays alone
do not establish polarized tissue flow or conservation of a complete network.
Source-specific localization uncertainty, conditional ARATH/ABCB4 directionality, the
ABCB1/ABCB19 brassinosteroid-homeostasis non-core framing, and qualified TWD1
mechanisms remain as reviewed. This ledger repair changes none of those claims.

The latest review confirms the scientific follow-ups; the previously completed full
validation covered 9,076 reviews and 54 pathway files. The targeted tracker checks
verify counts, canonical addition provenance and preservation of every other existing
inventory row; a new project history and rendered page accompany this repair. The
audit remains open until the updated tracker passes review/checks and the PR merges.

The missing universe entries are acetylcholine_signaling, dna_cytosine_methylation_cycle,
dopamine_receptor_signaling, il21_signaling, il22_signaling, il34_signaling,
nmj_achr_clustering, prostanoid_biosynthesis, protein_kinase_c_signaling,
reelin_signaling, trail_apoptotic_signaling and visual_phototransduction. They were
imported verbatim from canonical ledger commit `3c93882525`: acetylcholine is PR_OPEN,
and the other eleven are NOT_STARTED. No existing non-polar inventory row was
replaced with a newer canonical state. This makes the 714-module universe complete
without silently changing the status of unrelated audits.

## 2026-10-26 — apoptosis source follow-up and tracker union

The apoptosis audit retains distinct executioner activities and optional contextual branches: XIAP restraint is specific to caspase-3/7; ICAD folding and nuclease inhibition remain separate; Acinus condensation depends on experimental context; AIF is not universally downstream of caspase-3. The mammalian envelope describes characterized human and mouse implementations, without claiming identical dependencies throughout mammals. The corrected module requires a supported caspase-3-or-caspase-7 execution route while keeping contextual branches optional; empty-context satisfaction is not permitted.

Follow-up `5c0c9cf686` reassesses 24 mouse and 12 human annotation review objects. Ten mouse non-core actions become ACCEPT, grounded in executioner substrate cleavage, cascade amplification, mitochondrial feedback, cytokine suppression and conditional GSDME activation. Native mouse evidence, human constructs, ortholog inference and abstract-only source limits remain distinct. All 1,608 original payloads and raw-source hashes are preserved, including two inherited proposals; the other fourteen member reviews and module graph are unchanged. Both focused gene validations pass with zero errors and warnings. Earlier full validation is historical; fresh validation after main integration remains underway.

The tracker is rebuilt from upstream `fe302bb372`, replacing only this audit's existing row and status bullet. It retains all other upstream audit rows and prose, rather than reintroducing older branch statuses. Twelve missing canonical module rows are added only after verifying their paths: eleven NOT_STARTED and acetylcholine's actual PR_OPEN entry with evidence. Aggregate counts are recomputed from this union. This project-only correction changes no gene review, module or scientific source; publication, current CI and renewed scientific review remain separate gates.

## 2026-10-26 — semantic tracker union for five current-main integrations

The acetylcholine, arginine, arginase, polar-transport and apoptotic-execution branches were reconciled against pinned main `77121ffa32` and canonical tracker `9a873125b8`. All 714 module identities remain present: 12 complete, 13 active and 689 not started. Current scientific metrics and annotation actions were recomputed from each branch’s committed module and full representative review panel, while newer canonical workflow statuses were retained. This corrects stale family/activity/member counts and preserves each branch’s source-specific audit evidence and historical notes. These are tracker integrations, not new biological judgments or claims of merged completion. Existing full-validation processes remain owner-managed.

Root subsequently verified apoptosis full-validation session 37836 exited zero, with 9,094 reviews and 54 pathway checks passing (29,664 existing corpus warnings). The threonine review retry began after the verified 14:50 UTC quota reset and remains in progress; no review success is inferred. These operational updates do not change completion counts.

## 2026-10-26 — verified androgen merge and current integration gates

Androgen PR #5554 merged normally as `70a5964a22d14e7972cfb43fe02095aa4cb8a7c1`. All 270 scoped science, source and history files match approved head `93ce23a1a7`. The verified universe remains 714 modules: 13 complete, 12 active and 689 not started. Open PRs remain active even when their scientific review is approved. `REVIEW_CHANGES_REQUESTED` explicitly preserves an outstanding submitted verdict; `PR_OPEN` records an open integration without implying approval. Detailed `review_decision` and CI fields record the remote snapshot.

The five pinned-main integrations are published at their current remote heads. Acetylcholine, arginine, arginase and apoptosis now have submitted approvals; polar transport has a tracker-only requested change while its biology remains approved. The cited polar review’s apoptosis premise has since been superseded by a fresh approval, while threonine still awaits a new formal verdict. Its attempt-2 failure was a real usage limit after the earlier reset, with no next reset exposed; attempt 3 is now running. No credential or workflow change is inferred.

BCR PR #5584’s analysis-table extension fix is published as `dcd0a70066`, with lossless content and unchanged biology. The exact local CI module command and twenty route cases pass. Paired rRNA methylation PR #5586 is open at `33b01f7afd`; full validation passed for 9,098 reviews, zero errors, 30,069 advisories and 54 pathway checks. Acetoin audit 25 has a ready 18-member panel plus two stable PedE/PedH drafts with final checks ongoing: 20 planned genes, 83 original rows and 86 current rows. A bounded PTHR22912:SF219 family-review follow-up also remains pending; this is not a completed twenty-member audit. Its 27 route cases and bounded module QA pass; final extension integration and full validation remain pending.


### 2026-10-26 — current follow-ups, queue boundaries and audit 26

Live GitHub heads and submitted reviews were rechecked rather than treating a pushed fix as approval. Current-head approvals supersede earlier requests for Asp/Asn, threonine and paired rRNA methylation; BCR received a new current-head CHANGES_REQUESTED review at 16:08:46 UTC, and acetylcholine retains its outstanding request while renewed review runs. Anti-CRISPR, arginine biosynthesis and paired rRNA methylation remain queued. Asp/Asn and threonine have normal exact-head auto-merge enabled. The new alginate head requires renewed review; the earlier approval is not represented as current. Arginase is clean against published main but conflicts with its synthetic PR5563 predecessor in only CAR1 notes/HTML and project HTML; approved science is preserved, and integration waits for the actual predecessor to publish. Polar has exact-head normal auto-merge enabled; an UNKNOWN merge-state field does not establish a conflict.

The committed acetoin package contains all 20 reviews and the conditional PedE/PedH extension. Its full run subsequently terminated successfully with 9,113 valid reviews, zero blocking errors and 54 passing pathway checks; PR #5588 is published at the verified committed head. Audit 26 begins only after the isolated workspace and environment were verified; the existing open PR4748 sidecar overlap is recorded before new curation. A tree comparison against live main 7aa770175ea0fa47b17b55097966e9936c4a7dc4 confirms exactly the existing 714 module paths, with no additions or removals. All completed and unrelated inventory rows retain their previous evidence.

## 2026-10-26 — verified merges, 715-module universe and canonical main integration

Seventeen audits are complete after scoped approved-content verification of arginine PR #5563 (276 blobs), threonine PR #5569 (315 blobs), paired rRNA methylation PR #5586 (73 blobs) and Asp/Asn PR #5568 (407 paths). Asp/Asn preserves 406 identical blobs; its shared GO-CAM index includes the independently merged threonine updates. A clean three-way merge reproduces that final index byte-for-byte. The 27 Asp/Asn reviews, 548 rows and 54 raw sources are unchanged. This is an explicit shared-index exception, not an unexamined content discrepancy.

The universe now contains 715 modules: 17 complete, ten active and 688 not started. Upstream PR #5562 added chaperone-mediated autophagy; creation of that module does not complete its independent audit. Audit 26 has six reviews, 28 rows and 12 unchanged raw sources, six activities, one connection, 15 references and 25 findings. Audit 27 has 15 reviews, 104 rows and 30 unchanged raw sources, nine activities, six connections, 12 references and 20 findings. Their full validations remain live in sessions 70329 and 77356 respectively. Audit 28 remains NOT_STARTED until its panel and scope are approved.

Current remote heads for arginase, polar transport and apoptosis are 90bdd63dec, 3a7688dd1d and 2cb571b3b0. Arginase has a new approval, polar transport has a current-head CHANGES_REQUESTED verdict, and apoptosis awaits renewed review. Acetoin baseline-only head 6ae71843c5 has a new approval; this supersedes rather than reuses an older head's approval. BCR, anti-CRISPR and alginate remain in the merge queue at this snapshot; auto-merge being null does not imply they are unqueued. Named checks and exact queue entries are retained in the inventory.

Pinned main 551ec0d122 conflicts with the canonical acetylcholine branch only in the two tracker sources and their two derived pages. All incoming dated notes were already present verbatim in the canonical copy, and incoming histories are imported unchanged. The resolution retains verified canonical completion states and records current open-review gates, rather than reverting to upstream's older workflow snapshot. Fifty-seven excluded dirty paths were backed up with their bytes, modes and index state before a named stash; restoration is verified separately. This checkpoint changes no scientific curation and does not restart any full-validation process. The newly integrated local head requires its own checks and review after publication.

### 2026-10-26 — BCR completion verified during checkpoint preparation

BCR PR #5584 merged as `67e246011a263eeb00e61ef5219ee2fb8720d069` at 17:21:03 UTC. Independent verification found all 340 scoped gene, module, source and history blobs identical to approved head `49a03553b5d92f4e5162fb6514d4d26ba52b5ccc`, including all 22 reviews and 2,645 preserved annotation payloads. This advances the immediately preceding snapshot to 18 complete, nine active and 688 not started out of 715. The pinned local main integration remains `551ec0d122`; knowledge of this later verified merge updates the tracker without pulling a moving main into the in-progress merge.

### 2026-10-26 — audit 26 full validation passes; audit 28 authorized

Audit 26 full-validation session 70329 terminated successfully with 9,145 valid reviews, zero blocking errors, 30,059 advisory warnings and 54 passing pathway files. Validated commit `886264d544` is prepared for publication; a successful full run is not a merged audit. Audit 27 session 77356 remains live. Root authorized audit 28 only after normal seeding captured 15 AhpC/native-donor exemplars, 258 original annotation rows and 30 raw sources. Its isolated worktree starts from `551ec0d122`; individual review and module owners are assigned, without asserting completed curation. The scope separates native regeneration chains and excludes other peroxiredoxin/redox systems. The new checkpoint is 18 complete, ten active and 687 not started out of 715.

Audit 26 is now published as [PR #5591](https://github.com/ai4curation/ai-gene-review/pull/5591) at `886264d5442163b6a3fc69a69eb5ac7224e13dd3`, with 56 committed scope paths and the terminal full-validation result above. All 28 annotation payloads and 12 raw files are preserved. Review and CI remain pending; aggregate status remains 18 complete, ten active and 687 not started.

## Preserved incoming historical notes

## 2026-10-26 — arginine_catabolism_arginase_pathway published-main integration

Integrated published main `bfd5d651c11e41f1c509f167bb15a003c2da4bc3` into PR #5566, preserving the newer canonical inventory from `d212f5def0662e6e99615968a023f99b63c5ffc6` and unique dated branch/upstream notes. Every approved scientific file is preserved except the explicitly documented CAR1 notes union and its regenerated HTML where applicable. This integration needs fresh head checks and review; prior scientific approval is not described as approval of the new merge commit. The inventory remains 714 modules, with the canonical snapshot of 13 complete, 13 active and 688 not started. Verified arginine merge completion is reported separately for the next canonical tracker update.

## 2026-10-26 — verified late merges and canonical checkpoint

All 715 module identities are retained. Incoming main has only 714 tracker rows, so its older snapshot does not remove the canonical chaperone-mediated autophagy entry or reset independently verified lifecycle states. Anti-CRISPR #5555, alginate #5552 and arginase #5566 are now verified COMPLETE: respectively 114, 142 and 144 scoped approved blobs match their actual merge commits. Alginate retains 116 rows and 42 raw files, with three explicitly approved source-metadata corrections to reviewer-authored ISS proposals. Arginase retains 357 original rows and 36 raw files; its two supported ARGAH matrix additions give 359 final rows. Apoptosis #5558 remains open at the captured approval and is not counted complete. Proofs are retained in `.cache/module-audit-logs/merged-audits-20261026-late/`.

The current totals are 21 complete, 8 active and 686 not started. Audit27 is published as #5593 after terminal full validation (9,196 reviews, zero blocking errors, 30,064 warnings). Audit28 has 15 completed member reviews and independent module QA; full validation 3306 remains live. Audit29's clean isolated worktree and research foundation are established, without claiming completed members or validation. Exact submitted review states, timestamps and heads are recorded separately from pushed fixes, current CI and the new integration's pending gates.

This integration uses actual published main `fcc638463778de3f75470a294d11261871cf67b9`, including its independent FBN1 update. Modern Git found only four shared tracker conflicts; the canonical inventory and prose are reconciled without altering approved scientific content. All 57 excluded local files and their modes, plus original index state, were backed up under a uniquely identified stash before integration and are verified on restoration. No full-validation process is restarted for this checkpoint.


## Preserved polar and incoming historical notes

## 2026-10-26 — explicit outstanding review states after integration

The three affected workflow entries are synchronized from canonical tracker commit `1ec2bc7f86`, using the current remote states verified there. Polar transport and threonine explicitly retain `REVIEW_CHANGES_REQUESTED`; their outstanding submitted verdicts are not flattened to `PR_OPEN`. Apoptosis has since received a new APPROVED review, superseding the premise of polar review 5654374584, so it remains `PR_OPEN` with `review_decision: APPROVED`. Approval does not count as merge. All nonterminal statuses are active for accounting; `PR_OPEN` describes lifecycle, while the explicit review field preserves the verdict.

This bounded correction leaves all 711 other inventory rows and all 714 module identities unchanged, including this branch’s historical 12 complete / 13 active / 689 not-started snapshot. The newer canonical tracker separately verifies androgen’s merge and records 13 complete / 12 active; that unrelated row is intentionally not rewritten in this three-entry follow-up. All module and gene scientific content is unchanged. New evidence elsewhere, including the later Asp/Asn approval, is outside this narrow correction.

## 2026-10-26 — auxin_polar_transport published-main integration

Integrated published main `bfd5d651c11e41f1c509f167bb15a003c2da4bc3` into PR #5579, preserving the newer canonical inventory from `d212f5def0662e6e99615968a023f99b63c5ffc6` and unique dated branch/upstream notes. Every approved scientific file is preserved. CAR1 arrived unchanged from published main; this polar branch performed no CAR1 journal union or rendering. This integration needs fresh head checks and review; prior scientific approval is not described as approval of the new merge commit. The inventory remains 714 modules, with the canonical snapshot of 13 complete, 13 active and 688 not started. Verified arginine merge completion is reported separately for the next canonical tracker update.

## 2026-10-26 — correct current review verdicts after integration

Rechecked the two stale outstanding-request flags identified by PR #5579 review. Acetylcholine #5582 is open and approved at the pinned snapshot head. B-cell receptor #5584 has since merged; all 340 scoped files match its approved head, so this branch now records its verified completion. The other 711 inventory rows retain their existing content; the polar row additionally records its observed integration head and pending tracker-only follow-up checks. Historical dated snapshot notes are retained. Corrected a never-true CAR1 exception copied into the polar integration history: this branch inherited CAR1 unchanged from main. No science or raw-source change is made.

## 2026-10-26 — reconcile the acetylcholine verdict fields

The PR #5579 follow-up had copied a timestamp from a subsequently dismissed review and left one contradictory progress sentence. Re-read the submitted reviews, selecting the actual APPROVED state on published head b4760e897b at 17:48:01 UTC. The head, review timestamp, progress, phase, follow-up and CI snapshot now describe the same observed revision. All other 713 inventory rows and all scientific content are unchanged. Historical dated snapshots remain historical; current approval is separate from still-running CI and from merge completion.

## 2026-10-26 — polar integration with the canonical checkpoint

Published main fcc638463778de3f75470a294d11261871cf67b9 is integrated after modern Git verified exactly four tracker conflicts. Canonical tracker 00eb524d6ecb1307fac668a68a592d33c1e04aa1 supplies all 715 identities, 21 verified completions and audit 29 IN_PROGRESS; the polar branch's unique dated notes and append-only records are retained. The totals remain 21 complete, 8 active and 686 not started. CMA retains its existing unaudited status.

The last actual submitted polar review remains CHANGES_REQUESTED, not approval of c21e7bf80e or this new integration. Its exact timestamp and reviewed commit are retained in the inventory. Fresh remote facts additionally record the new 4HB approval and the new alkanesulfonate requested changes. Canonical acetylcholine 00eb is published with fresh review/CI pending. Progress, phase and review-followup fields now agree, while older dated snapshots remain historical records.

All 17 polar member reviews, 484 rows and 34 current raw sources, plus the NRT1.1 legacy source snapshots, are preserved. All 42 excluded dirty files and their modes/staging state were backed up before a named stash and verified after restoration. No scientific curation, external comment or full-validation restart is part of this integration. Fresh CI and review are required for the resulting published head.

Integrated published main `bfd5d651c11e41f1c509f167bb15a003c2da4bc3` into PR #5558, preserving the newer canonical inventory from `d212f5def0662e6e99615968a023f99b63c5ffc6` and unique dated branch/upstream notes. Every approved scientific file is preserved except the explicitly documented CAR1 notes union and its regenerated HTML where applicable. This integration needs fresh head checks and review; prior scientific approval is not described as approval of the new merge commit. The inventory remains 714 modules, with the canonical snapshot of 13 complete, 13 active and 688 not started. Verified arginine merge completion is reported separately for the next canonical tracker update.

Pre-integration head 2cb571b3b0 is approved with all required head checks successful. Published main fcc6384637 introduced four shared-tracker conflicts; this integration retains the canonical 715-module inventory and all 21 verified completions. All 174 scoped scientific/source blobs, 16 reviews, 1,608 original rows and 32 raw sources are preserved. Renewed review and CI on the integration commit remain pending; the audit is not complete. The 714 unrelated canonical rows are unchanged. Historical source-branch and upstream note paragraphs are retained; checkpoint values describe pinned snapshots.

### 2026-10-27: merged-content verification and shared-tracker integration

Verified the actual merges of PRs #5591, #5582, #5588 and #5593 against their approved heads, original annotation snapshots and raw-source hashes. Acetoin has two expected shared-file unions: unrelated upstream quote-baseline pruning and TreeGrafter history additions; both exactly match automatic three-way merges. The live upstream universe remains 715 modules: 25 verified complete, five active and 685 not started. Reconciled the two approved open PRs against published main without changing their scientific assertions. The resulting integration commits require fresh review and checks. Historical dated notes above retain their original snapshot meanings.


## 2026-10-27 — restore tracker evidence, coherent snapshots and journal headings

Corrected the polar audit entry to retain its 17 members, 484 rows, 34 raw sources and NRT1.1 consolidation, without the unrelated apoptosis quote-baseline claim. The three open-PR entries now pin each observed head, exact latest submitted review and CI snapshot together; their phase, progress and review-followup text is identical. Approval of a captured head is not approval of the follow-up prepared here, whose review and CI remain pending. The status summary is derived from all 715 identities: 25 complete, five active (three open PRs and two audits in progress), and 685 not started.

Restored all six heading-bearing historical blocks from polar commit 0ca553b979 in place, retaining every existing journal paragraph and all incoming/main historical headings. The earlier 2026-10-27 integration note remains a historical snapshot. No gene, module, publication, raw-source or existing history file is changed by this correction. The new provenance record links this follow-up to its PR.

## 2026-10-29 — polar integration with published main

Seventeen member reviews contain 484 active rows, preserving 483 original annotation payloads; 34 raw sources and the NRT1.1 consolidation of Q05085 are preserved. All 224 scoped scientific/source/history paths are unchanged by this integration. Pinned GitHub snapshot 2026-10-29T14:51:06.922623+00:00: PR #5579 is OPEN at 30a3cf7f6644f25698db78ec16c2779dd8867292, with APPROVED review 5670621005 submitted at 2026-10-27T16:23:33Z and successful required checks on that head. The merge of main bb749eff8b133cccae14d5b91f202f5b03167630 prepared here requires fresh review and CI after publication; the prior approval does not cover the integration commit.

The incoming and approved tracker journals are identical and are retained in full, including all headings. All 715 module identities and the 714 unrelated inventory rows are preserved. This refresh is limited to the polar row; other rows retain their explicitly dated incoming evidence. The ledger remains at 25 COMPLETE, 3 PR_OPEN, 2 IN_PROGRESS and 685 NOT_STARTED. These are ledger counts, not a fresh global GitHub survey. A new append-only project history records the integration.

## 2026-11-04 — beta-aryl merge verified; c-di-AMP audit started

PR #5930 completion is now recorded from the actual merge and retained content proof, superseding its stale requested-changes snapshot. All 153 scoped blobs match the approved head. The next authorized module is bacterial c-di-AMP signaling; its isolated checkout starts at published main `bcead031369d8739c819091f3348deb68b24f321`. Initial research checks receptor-specific effects, cyclase compartments, degradation chemistry and taxonomic scope before choosing further exemplars. Other inventory rows and dated evidence are retained; this is not a fresh global status survey or a restart of the paused all-module goal.

## 2026-11-04 — c-di-AMP validation completed

Full just validate-all completed with exit 0 across 10300 reviews: zero errors, 109 advisory ontology-label issues, 51 advisory reference issues, and 27990 best-practice warnings. Ontology/reference warning paths were checked against starting main and remain unchanged. All 54 pathway files with PMID references passed. Scope remains 17 reviews, 89 original rows, 34 raw sources and zero NEW annotations. Publication, independent review, CI and actual merge remain pending.

## 2026-11-04 — c-di-AMP PR #5997 published

PR #5997 publishes 17 complete reviews, preserving 89 original rows and 34 raw sources; zero NEW and two explicit CpaA UNDECIDED claims. Full validation passed on 10300 reviews. Rebase onto f2068f974a preserved all 143 scoped blobs and 65 excluded local files; incoming GCK validation passed. Independent review, CI and actual merge remain pending.

## 2026-11-04 — c-di-AMP review findings addressed

PR #5997 review follow-up preserves all 89 original annotation payloads and 34 raw files, adds nine evidence-backed recommendations (seven binding activities, DarB enzyme activation and inferred DacA membrane location), and corrects three cyclase BP mappings to the supported cyclic di-AMP biosynthetic-process proposal. KtrA channel regulation is retained with target-species primary evidence; CabP and KhtT remain broader based on their different evidence. Two CpaA process claims remain UNDECIDED. Seventeen focused validations, module/source checks and 37 capacity cases pass. Fresh independent review and CI remain pending.

## 2026-11-05 — restore omitted nitrate completion

The PR count reconciliation found the original nitrate audit #5740 missing from the current tracker. Its 209 scoped blobs match the approved head and all 21 reviews are COMPLETE. This restores its verified completion; the later open family-review PR #5928 is tracked separately. The session has produced 34 initial module-audit PRs and two corrective follow-ups, all merged; c-di-GMP has not yet been published. Historical dated status snapshots above retain their original meanings.

## 2026-11-05 — c-di-GMP PR #6062 published

Published the 17-member, three-phyla audit after scoped checks passed and full validation reached its documented terminal result: 19 proven pre-existing citation failures outside this module, with schema, ontology, best-practices and pathway stages passing. Rebase onto f522d5fdf4 preserved all 146 scoped blobs and 44 excluded local files. The PR is open; independent review, CI and actual merge are pending. This is the session’s 37th module-audit/follow-up PR.

## 2026-11-06: O-acetylserine cysteine synthesis audit

The bacterial OAS/sulfide module now has 18 curated references, 30 findings, two
required reactions and three terminal alternatives. Sixteen completed gene reviews
span six species, including Mtb CysM as an OPS/CysO negative comparator; 15 proteins
represent the native OAS-route panel. Family and PAINT scope are qualified where
substrates diverge, and the Campylobacter placement has no invented PTN. The 59-case
capacity/preservation check passes with 158 historical rows, 32 raw files and three
provider artifacts preserved; one supported MF proposal brings the row total to 159.
Targeted gene, module and family validation pass. Full-corpus validation is terminal: 10,544 reviews, 17 reference errors in 16 unrelated yeast reviews, and zero best-practice errors. All 22 affected inputs are byte-identical to the pinned base; the exact errors, input blobs and log hash are recorded in preexisting-reference-failures.yaml. PR #6120 is open. The five-gene and family review follow-up passes focused checks and all 59 capacity cases; fresh full validation, renewed external review, CI and actual merge remain pending. See
[audit evidence](../analysis/module_audits/bacterial_cysteine_biosynthesis_via_o_acetylserine/README.md).


## 2026-11-06 — cysteine follow-up full validation

The PR #6120 scientific follow-up full run finished on 10,544 reviews, with zero best-practice errors and 54 referenced pathways passing. Its 17 reference errors match the previous run exactly and affect 16 unrelated yeast reviews; all 22 relevant inputs are identical to the pinned base. All 189 scoped publication files match the validated commit. Renewed review, CI and actual merge remain required.


## 2026-11-06 — cysteine integration with published main

Merged published main aabe4b253646e535bd700a8588e4982e20b873cc into approved cysteine head 2c755dd910f283d69d047aad656baf091e19b834. All189 scoped scientific/source/proof paths outside the three shared tracker/index files remain byte-identical. The777-row inventory keeps every incoming row unchanged except this cysteine audit row, which remains exactly the reviewed version. Both dated project journals are retained; last_reviewed is2026-11-06. No validation implementation changed in the incoming merge. The prior full run validates immutable cysteine science; fresh CI and review gate the integration commit. Four generated local caches were preserved in an exact-path stash and separately hashed backups.

## 2026-11-06 — module universe refresh and divisome audit tracking

Expanded the catalog from 715 to 779 verified module documents at pinned main `f0306d4de38a86ed077b066841167cc071bd56fe`. The 64 additions comprise 62 top-level modules and the two experimental GapMind histidine/isoleucine ModuleReviews; all enter NOT_STARTED. Preserved every unrelated prior inventory row, all prior inventory notes and the dated project journal. Only the divisome row moves to IN_PROGRESS, recording nine members, 160 original rows, eight curated references and three review articles while module participant integration remains pending. Derived ledger totals are 27 COMPLETE, four PR_OPEN, three IN_PROGRESS and 745 NOT_STARTED. This extends coverage of upstream additions without promoting unreviewed modules or refreshing unrelated stale lifecycle claims.

### Divisome integration — 2026-11-06

The [divisome audit and supporting evidence](https://github.com/ai4curation/ai-gene-review/pull/6123) integrates nine completed member reviews, four bacterial realizations and the conditional Bacillus PBP3 catalytic substitute. Fourteen curated references include three reviews and ten findings. The scoped checker passes 56 capacity cases plus a primary heterologous compatibility check, preserving all 160 original rows and 19 raw/provider files. Full-corpus validation and publication remain pending; no merged completion is claimed.


## 2026-11-06 — divisome full validation attribution

The divisome full run finished on 10,555 reviews. Schema and term checks pass; best practices report zero errors, and all 54 pathways with PMID references pass. The run exits nonzero for 17 reference errors in 16 unrelated yeast reviews. The audit verifies the exact failures and all 22 affected inputs against pinned base `f0306d4de38a86ed077b066841167cc071bd56fe`; none is introduced by this module. All 144 scoped scientific files match validated commit `579fdd34fec0c49c471e899244dcb6abf4473a83`. Publication, independent review, CI and actual merge remain outstanding.


The divisome audit is published as [PR #6123](https://github.com/ai4curation/ai-gene-review/pull/6123). Auto-merge is enabled through the normal review, CI and merge queue gates. Publication does not count as completed module-audit work; actual merge remains required.

## 2026-11-06 — divisome review follow-up

PR6123 review follow-up preserves all160 original machine rows, two inherited NEW rows and19raw/provider files; adds two experimentally supported enzyme-activator rows. Nine focused validations, renders and histories pass, as do57capacity/evidence controls. Target-specific support, wall-organization actions, FtsW flippase scope, official locus symbols and one InterPro defect are corrected. The rendered project evidence link now points to the live PR. Fresh full validation and renewed review/CI remain required.

## 2026-11-06 — divisome review fixes validated

The divisome review follow-up completed full validation on 10,555 reviews. The 17 reference errors are exactly the previously recorded errors in 16 unrelated yeast reviews; all 22 relevant inputs equal the pinned base. Schema and term checks pass, best practices report zero errors, and all 54 PMID-bearing pathways pass. All 161 scoped files matched validated science commit ab9b9b9ea919d6c8efa9e541bdade882f0207741. The nine member reviews preserve 160 original machine rows, two inherited NEW rows and 19 raw/provider files, adding two directly supported enzyme-activator annotations. The 57 scoped capacity/evidence checks pass. Renewed external review, CI and actual merge remain pending for PR #6123.

## 2026-11-06 — PR #6123 integration with published main

Integrated published main `fd782f231a` with the validated PR #6123 head `4b65e56304`. All 158 scoped files outside the shared tracker and rendered index remain byte-identical, including curated science and source evidence. The 777-row inventory retains every incoming row except this module's unchanged validated row; both dated journals are preserved. Validation implementation is unchanged. Prior validation remains evidence for the preserved science; renewed CI and review gate this integration commit.

## 2026-11-06: Replication PR #6117 review follow-up

Eleven reviewed genes preserve 131 annotation payloads, nine inherited NEW actions,
22 raw files and 49 referenced sources. HolD model/construct coordinates and
source-specific mapping defects are structured; generic binding policy is applied
consistently. Epsilon proofreading is refined to DNA-specific exonuclease activity
in the genes and module. Focused checks and all 97 pathway cases pass. Fresh full
validation, publication of the follow-up, independent review/CI and actual merge
remain outstanding.


## 2026-11-06 — PR #6117 integration with published main

Integrated published main `c27aa23b93` with the validated PR #6117 head `05b701415a`. All 575 scoped files outside the shared tracker and rendered index remain byte-identical, including curated science and source evidence. The 777-row inventory retains every incoming row except this module's unchanged validated row; both dated journals are preserved. Validation implementation is unchanged. Prior validation remains evidence for the preserved science; renewed CI and review gate this integration commit.


## 2026-11-06 — replication proposal refinements

PR #6117 round 2 refines two proposals authored within this PR, with both prior versions archived and independently verified against git and the pristine seed: HolD now uses DNA-templated DNA replication, while Bacillus DnaB has separate single- and double-stranded DNA-binding activities. Three DnaQ exonuclease rows refine directly to DNA-specific proofreading activity. DnaB membrane evidence explicitly distinguishes wild-type enrichment from mutant DnaD recruitment. Four focused review validations, renders and histories pass without curation warnings. All 1,067 original seed rows, including two inherited NEW rows, and 104 raw sources remain preserved across 52 COMPLETE reviews; the final count is 1,082 rows. The module remains unchanged. The capacity checker recognizes only the two independently verified DNA-binding descendant relationships and passes 100 cases, including removal and one-way entailment controls. Fresh full validation, publication, renewed review/CI and actual merge remain pending.


## 2026-11-06 — Replication round2 validated

Replication round2 completed full validation on 10,653 reviews. The17 reference errors are the exact known errors in16 unrelated yeast reviews; all22 relevant inputs equal the pinned base. Schema and terms pass; best practices report zero errors, and all54 PMID-bearing pathways pass. All588 scoped files match validated science commit 2ea0e902c55f0b3ddd219f8bb03511fca3b4b130. The 52 completed reviews preserve 1,067 pristine annotation rows (1,065 machine rows and two inherited proposals) and104 raw files;15 added rows yield1,082 current rows. Two proposals authored by this PR were revised with exact archives, distinguished from original seeds. The100 capacity cases pass, including one-way GO DNA-binding descendant entailment. Renewed independent review, CI and actual merge remain pending for PR#6117.

## 2026-11-06 — PR #6117 integration with published main

Integrated published main `1970e159b9` with the validated PR #6117 head `8df6fabd8d`. All 588 scoped files outside the shared tracker and rendered index remain byte-identical, including curated science and source evidence. The 777-row inventory retains every incoming row except this module's unchanged validated row; both dated journals are preserved. Validation implementation is unchanged. Prior validation remains evidence for the preserved science; renewed CI and review gate this integration commit.

## 2026-11-06 — OPG comparative audit integrated

The comparative OPG audit now covers 11 COMPLETE gene reviews across five species in Alphaproteobacteria and Gammaproteobacteria. All 91 original annotation payloads and 28 raw/provider sources are preserved; five supported additions yield 96 current rows. Thirteen curated literature references, including two comparative reviews, supply 18 findings. Seven parts and eight annotons distinguish OpgH-associated synthesis, OpgG participation with unresolved native chemistry, conditional OpgI and compatible ACP dependencies, E. coli OpgD hydrolysis, Xanthomonas OpgD cyclization, and the Caulobacter unresolved-product comparator. Two family reviews retain their mixed-function and PAINT-scope limitations. The executable checker passes 24 evidence-scoped cases and ten mutation cases. Full-corpus validation, publication to adopted PR #2142, renewed independent review, CI and actual merge remain pending.

## 2026-11-06 — OPG full validation completed

Comparative OPG science and focused validation are complete: 11 COMPLETE gene reviews, 91 original annotation payloads preserved, 96 current rows, 28 unchanged raw/provider sources, 13 literature references including two reviews, 18 findings, seven parts and eight annotons, two family reviews, 24 endpoint cases and ten mutation cases. The full-corpus run completed on science commit 074427cc8340be71f9fbdeea8440f551bdbea6b0 with schema, term, best-practice and pathway checks passing. Its 17 blocking reference errors in 16 unrelated yeast reviews exactly match the known baseline; all 22 relevant inputs are identical to the pinned base. These are addressed separately in PR #6134. Publication of this comparative revision to adopted PR #2142, renewed review, CI and actual merge remain pending.

## 2026-11-06 — PR #2142 integration with published main

Integrated published main `039e2ef630` with the validated PR #2142 head `79b979a1fa`. All 169 scoped files outside the shared tracker and rendered index remain byte-identical, including curated science and source evidence. The 777-row inventory retains every incoming row except this module's unchanged validated row; both dated journals are preserved. Incoming main adds warning-level ancestor-action consistency checks and qualifier-aware comparisons. All eleven scoped gene reviews pass focused validation under the incoming implementation. The historical full run is evidence for preserved science under its recorded implementation; renewed CI and review gate this integration commit.

## 2026-11-06 — OPG review follow-up validation

PR #2142 review fixes passed a fresh full-corpus validation on frozen science head 05230b5e38d6a055164e2825c0c0b8016f9304a8: 10,683 reviews, zero blocking errors and 54 pathway files. All 183 scoped files remained byte-identical through the run. The beta-glucan rows retain independently supported claims; Caulobacter synthesis support remains explicitly inferred; the OpgG hydrolysis proposals distinguish biochemical capability from unresolved physiological relevance. A subsequent import/hash-helper formatting fix addresses the CI lint failure without changing lineage assertions; both lint and the complete lineage check pass. Renewed review, CI and actual merge remain pending.

## 2026-11-06 — DsbA/DsbB comparative audit started

The next module audit begins from pinned main `ee3ce5f10c138b64413d054c3755e2fce95cb2c6`. Five original E. coli/P. putida reviews contain 49 historical annotation rows and ten frozen raw files. Comparative review literature and Pseudomonas PA14 reconstitution studies will guide additional sampling, family grounding and the boundary between DsbB-dependent oxidation and alternative redox systems. No completed review or module integration is claimed at this starting checkpoint.

## 2026-11-06 — DsbAB member and comparative evidence checkpoint

The DsbAB audit has13complete gene reviews across E. coli, KT2440, PA14, Bacillus168 and exact-sequence Campylobacter proteins;78original payloads and26raw files are preserved, with9supported additions. Four family reviews assess six actual PAINT assertions and pass49grounding/25quotation checks, retaining unresolved broad-family scope. Thirteen curated references include four reviews and23source-checked findings. Exact81116DsbB remains an explicit archived-accession gap. Module integration, full validation, publication and actual merge are still outstanding.

## 2026-11-06 — comparative DsbAB mechanism integrated

Integrated DsbB-dependent oxidative folding across three bacterial phyla with two required roles, explicit alternative relays, and optional PA14 DsbA2 biochemical context. Fourteen completed gene reviews preserve 78 original rows and 28 raw sources; fourteen supported additions yield 92 current rows. Official archived 81116 DsbB identity is bridged without fabricated raw data or family IDs. Fourteen references, including four reviews, provide 24 findings. Eight curated compatible pairs and 75 scoped controls retain assay, compartment and family-scope limits. Full validation, dedicated PR, independent review, CI and actual merge remain required.

## 2026-11-06 — DsbAB comparative audit validated

Full validation completed on 10,590 reviews. The 17 reference errors are the exact previously recorded errors in 16 unrelated yeast reviews; all 22 relevant inputs equal the pinned base. Schema and term checks pass, best practices report zero errors, and all 54 PMID-bearing pathways pass. All 170 scoped files matched validated science commit 3cc137856140e62b4f4a5c678ee689d0ec148698. Fourteen completed gene reviews preserve 78 original rows (including two inherited NEW rows), 28 raw files and the explicit UniSave archive; fourteen supported additions yield 92 current rows. Four family reviews preserve six PAINT assertions. Four review articles and ten primary papers provide 24 module findings. The 75 capacity/mutation cases and 95 evidence quotes pass. A dedicated PR, independent review, CI and actual merge remain required.

## 2026-11-06 — DsbAB audit integration with published main

Integrated published main `cd3a5e061f` with the validated DsbAB audit head `81119764e6`. All 168 scoped files outside the shared tracker and rendered index remain byte-identical, including curated science and source evidence. The 777-row inventory retains every incoming row except this module's unchanged validated row; both dated journals are preserved. Validation implementation is unchanged. Prior validation remains evidence for the preserved science; renewed CI and review gate this integration commit.

## 2026-11-06 — DsbAB PR published

Published the independently validated DsbAB comparative audit as PR #6129. Normal auto-merge is enabled; independent review, CI, merge-queue checks and actual merge remain required. This is the49th new PR in the session; adopted existing PRs are excluded.

## 2026-11-06 — DsbAB review follow-up validated

DsbAB PR #6129 follow-up passed nine focused gene validations and a fresh full run on `2edeb4ad91`. The 10,627-review corpus has zero best-practices errors; its 17 reference errors in 16 unrelated yeast reviews are proven pre-existing by 22 base-identical inputs. All 190 scoped files match the validated scientific commit. Three same-PR authored sequence-transfer proposals were explicitly archived and corrected to ISS; upstream payloads remain unchanged. Renewed independent review, CI and actual merge remain required.

## 2026-11-06 — PR #6129 integration with published main

Integrated published main `1970e159b9` with the validated PR #6129 head `aafe54e3d5`. All 188 scoped files outside the shared tracker and rendered index remain byte-identical, including curated science and source evidence. The 777-row inventory retains every incoming row except this module's unchanged validated row; both dated journals are preserved. Validation implementation is unchanged. Prior validation remains evidence for the preserved science; renewed CI and review gate this integration commit.

## 2026-11-06 — PR #6129 tracker placement and tally

Correct the shared project page after integration for PR #6129: place the bacterial_dsbab_oxidative_folding checkbox under Status and derive the displayed audit-state tally from all 777 inventory rows. This changes project prose and its rendering only; the inventory and all curated science/source files remain unchanged from 14cc2fc9ef7075abfa6bddce9556b222327bab42.

## 2026-11-06 — PR #6129 round2 full validation completed

The bacterial_dsbab_oxidative_folding PR #6129 round2 review follow-up completed a fresh full-corpus run on 5fc26f0eaccdc9050295cc6a0c111dbf198628f0. Schema, terms, best practices and all54 pathway checks passed. The only17 blocking errors are the known16 unrelated yeast citation reviews; their22 relevant inputs equal the pinned base, and all197 frozen publication files matched the tested head. Current main already fixes these citations in merged PR5975. Integrating that main, publishing the reviewed fixes, renewed review/CI and actual merge remain pending.

## 2026-11-06 — PR #6129 integration with published main

Integrated published main `488d370561` with the validated PR #6129 head `b0d63928fa`. All 199 scoped files outside the shared tracker and rendered index remain byte-identical, including curated science and source evidence. The 777-row inventory retains every incoming row except this module's unchanged validated row; both dated journals are preserved. Incoming main adds warning-level ancestor-action consistency checks and qualifier-aware comparisons. All scoped gene reviews pass best-practice and GO-hierarchy validation under the incoming implementation. The historical full run is evidence for preserved science under its recorded implementation; renewed CI and review gate this integration commit.

## 2026-11-06 — PR #6129 integration with published main

Integrated published main `fb8e3ee95b` with the validated PR #6129 head `68b726ee20`. All 201 scoped files outside the shared tracker and rendered index remain byte-identical, including curated science and source evidence. The 777-row inventory retains every incoming row except this module's unchanged validated row; both dated journals are preserved. Incoming main contains the merged OPG audit; validation implementation is unchanged. The reviewed DsbA/DsbB mechanistic distinctions and source evidence from the approved head are preserved. The historical full run is evidence for preserved science under its recorded implementation; renewed CI and review gate this integration commit.

## 2026-11-06 — comparative beta-oxidation audit

Comparative beta-oxidation curation covers 19 COMPLETE gene reviews across seven species and three bacterial phyla, preserving all 211 original annotation payloads, both inherited NEW rows and 40 raw/provider files. Six supported additions yield 217 rows. Seventeen references, including four review articles, supply 21 mined findings. Four required reactions use ten alternatives and eight reviewed protein families. Unknown physiological electron acceptors, matched partner requirements, substrate limits and distinct native versus biochemical endpoints are explicit. The source-scoped checker uses the production module circuit with 54 cases and 12 mutation checks; passing cases do not replace the literature assessment. Focused checks and full-corpus validation passed on 2026-11-06 (10,688 reviews; zero blocking errors). Corpus advisory reference issues outside this panel remain recorded in the validation proof. Published as [PR #6136](https://github.com/ai4curation/ai-gene-review/pull/6136); independent review, CI and actual merge remain pending.

## 2026-11-06 — beta-oxidation prepublication integration

Integrated current main 488d370561caf677da6e0c8ef94d5b0c7f4cb374 before beta-oxidation full validation, retaining the reviewed module, nineteen gene reviews, eight family reviews and their source artifacts. Shared tracker rows retain every incoming module except this audit's updated row. Main includes PR5975's citation corrections and warning-level annotation-consistency checks; the fresh full-corpus run will test the integrated implementation.

## 2026-11-06 — beta-oxidation review corrections

PR6136 review corrections preserve chain-length specificity independently of acceptor identity, accept target-specific inferred Bacillus ETF coupling, distinguish bound FAD from a net flavin acceptor, fix direct palmitate/C4 support, clarify hydratase conventions and remove description-level curation framing. All 217 current row payloads, prior NEW actions and 40 raw/provider files remain unchanged. Eleven revised gene reviews, one family review and the module require renewed focused/full validation, review, CI and merge.

[Source adjudication](../analysis/module_audits/bacterial_fatty_acid_beta_oxidation/round1-source-adjudication.md) records the decisions and remaining assay limits.

## 2026-11-06 — beta-oxidation revised science validated

The round1 full-corpus run passed on `f063b332b1c5aa1ff7b1ac043f43586bd51819a4`: 10,688 reviews, zero blocking errors and all 54 PMID-bearing pathways. All 290 frozen files were unchanged after the run. The 52 reference advisories in 31 files are outside this nineteen-member panel; the audit does not claim to repair them. Eleven revised reviews and the preserved 217 annotation payloads are covered by the new run. PR #6136 is ready for renewed external review and CI; actual merge remains pending.

## 2026-11-06 — PR #6136 integration with DsbAB merge 8daf92bfc8

Integrated published main `8daf92bfc8` with the validated PR #6136 head `b6811b89d6`. All 294 scoped files outside the shared tracker and rendered index remain byte-identical, including curated science and source evidence. The 777-row inventory retains every incoming row except this module's unchanged validated row; both dated journals are preserved. Incoming main contains the merged OPG and DsbAB audits; validation implementation is unchanged. All incoming completion records and dated journal entries remain intact. The historical full run is evidence for preserved science under its recorded implementation; renewed CI and review gate this integration commit.

Integration proof: [round1-main-integration.json](../analysis/module_audits/bacterial_fatty_acid_beta_oxidation/round1-main-integration.json).

## 2026-11-06 — adopted ethanolamine comparative audit integrated

The comparative ethanolamine audit now contains22 completed reviews (20 positive members and2 negative comparators),224 original rows and226 current rows, with47 raw/provider files preserved. One existing-PR-authored PA4022 evidence revision is archived and two new molecular-function rows are supported. Five exact EutB/EutC pairs span Pseudomonadota and Bacillota. Twenty literature references, including three reviews, plus two scoped primary-source records supply58 findings. The eight-part module preserves required deamination plus an oxidative fate; uptake, parallel reduction, cofactor recycling, reactivation and LT2 cargo scaffolding have explicit scope.79 capacity cases,8 mutations and153 module/profile quotations pass. PSEPK/pta is a related family-crosscheck correction that remains DRAFT, not an additional completed member. Full validation and publication to adopted PR5970, renewed review/CI and actual merge remain required.

## 2026-11-06 — ethanolamine comparative audit validated

Full validation completed on 10,637 reviews. The 17 reference errors are the exact previously recorded errors in 16 unrelated yeast reviews; all 22 relevant inputs equal the pinned base. Schema and term checks pass, best practices report zero errors, and all 54 PMID-bearing pathways pass. All 447 scoped files matched validated science commit 60b72729693b2b7c74ca1e1bb982cee1b9d94666. The comparative audit covers 22 completed gene reviews (20 positive members and two negative comparators), preserving 224 original rows and 47 raw/provider sources; two supported additions yield 226 current rows. Five compatible EutB/EutC pairs span Pseudomonadota and Bacillota. Twenty literature references, including three reviews, plus two scoped primary-source records supply 58 findings. All 79 capacity cases, eight mutation cases and 153 module/profile quotations pass. Ten family reviews retain their unresolved scope judgments. Publication to adopted PR #5970, renewed independent review, CI and actual merge remain required.

## 2026-11-06 — PR #5970 integration with published main

Integrated published main `1970e159b9` with the validated PR #5970 head `b1ecf59429`. All 445 scoped files outside the shared tracker and rendered index remain byte-identical, including curated science and source evidence. The 777-row inventory retains every incoming row except this module's unchanged validated row; both dated journals are preserved. Validation implementation is unchanged. Prior validation remains evidence for the preserved science; renewed CI and review gate this integration commit.

## 2026-11-06 — PR #5970 tracker placement and tally

Correct the shared project page after integration for PR #5970: place the bacterial_ethanolamine_uptake_catabolism checkbox under Status and derive the displayed audit-state tally from all 777 inventory rows. This changes project prose and its rendering only; the inventory and all curated science/source files remain unchanged from ea09de467d34d109e14184f8ccd3d78f134dbd3f.

## 2026-11-06 — PR #5970 round1 full validation completed

The bacterial_ethanolamine_uptake_catabolism PR #5970 round1 review follow-up completed a fresh full-corpus run on ffafeb78851a39226167dce82b5c2cb59e40be74. Schema, terms, best practices and all54 pathway checks passed. The only17 blocking errors are the known16 unrelated yeast citation reviews; their22 relevant inputs equal the pinned base, and all452 frozen publication files matched the tested head. Current main already fixes these citations in merged PR5975. Integrating that main, publishing the reviewed fixes, renewed review/CI and actual merge remain pending.

## 2026-11-06 — PR #5970 integration with published main

Integrated published main `488d370561` with the validated PR #5970 head `46d8264f6a`. All 455 scoped files outside the shared tracker and rendered index remain byte-identical, including curated science and source evidence. The 777-row inventory retains every incoming row except this module's unchanged validated row; both dated journals are preserved. Incoming main adds warning-level ancestor-action consistency checks and qualifier-aware comparisons. All scoped gene reviews pass best-practice and GO-hierarchy validation under the incoming implementation. The historical full run is evidence for preserved science under its recorded implementation; renewed CI and review gate this integration commit.

## 2026-11-06 — PR #5970 integration with published main 577501df51

Integrated published main `577501df51` with the validated PR #5970 head `754e29a9a9`. All 459 scoped files outside the shared tracker and rendered index remain byte-identical, including curated science and source evidence. The 777-row inventory retains every incoming row except this module's unchanged validated row (no earlier completion rows regressed); both dated journals are preserved. Incoming main contains the merged beta-oxidation audit; validation implementation is unchanged. All incoming completion records and dated journal entries remain intact. The historical full run is evidence for preserved science under its recorded implementation; renewed CI and review gate this integration commit.

Integration proof: [validated-head-main4-integration.json](../analysis/module_audits/bacterial_ethanolamine_uptake_catabolism/validated-head-main4-integration.json).

## 2026-11-06 — cytochrome c maturation comparative audit

The bacterial System I module now distinguishes canonical CcmG-supported/CcmFH maturation from the experimentally reconstructed G20 cysteine-CcmE System I* cassette. 24 curated references and 55 findings support all 16 annotons; 29 individual reviews cover three complete curated panels plus selected Rhodobacter/Shewanella roles. All 227 historical rows, 58 raw files and six provider artifacts remain intact; six new proposals bring the total to 233 rows. Seven family reviews qualify chemistry, partner and mixed-subfamily claims without changing original PAINT verdicts. The 151 capacity controls pass. Scoped checks pass. Full validation on 4c2bbabe931 is terminal exit 1: 10,548 reviews, 17 proven unrelated reference errors in 16 yeast reviews, 22 base-identical inputs and 28,001 best-practice warnings. No scoped blocker was found. PR #6121 is open; external review/CI and actual merge remain pending; prior module PR #5362 is already merged. Other inventory rows retain their dated evidence.

## 2026-11-06 — cytochrome review corrections

PR #6121 follow-up reconciles heme handoff versus transmembrane transport across the audited taxa, supports membrane locations with topology, and retains the distinct CcmE covalent intermediates. Thirteen focused gene validations and five supplemental reference-finding checks pass; all 151 capacity cases still pass. All original annotation payloads and raw/provider sources are preserved. Fresh full-corpus validation, current-head external review and CI remain pending; no merge is claimed.

## 2026-11-06 — cytochrome follow-up full validation

The PR #6121 scientific follow-up full run finished on 10,548 reviews, with zero best-practice errors and 54 referenced pathways passing. Its 17 reference errors match the previous run exactly and affect 16 unrelated yeast reviews; all 22 relevant inputs are identical to the pinned base. All 307 scoped publication files match the validated commit. Renewed review, CI and actual merge remain required.

## 2026-11-06 — cytochrome maturation location follow-up validated

Round 2 full validation completed on 10,548 reviews: 17 exact known reference errors in 16 unrelated yeast reviews, all 22 inputs identical to the pinned base, zero best-practice errors and all 54 PMID-bearing pathways passing. All 342 scoped files matched science commit 7641af14dc before metadata closure. Seventeen gene reviews now use claim-specific topology/location evidence, including two core-only location repairs; 233 annotation rows, 58 raw files and six provider files remain unchanged. Publication, renewed independent review/CI and actual merge remain pending.

## 2026-11-06 — PR #6121 integration with published main

Integrated published main `c27aa23b93` with the validated PR #6121 head `542a9102ed`. All 339 scoped files outside the shared tracker and rendered index remain byte-identical, including curated science and source evidence. The 777-row inventory retains every incoming row except this module's unchanged validated row; both dated journals are preserved. Validation implementation is unchanged. Prior validation remains evidence for the preserved science; renewed CI and review gate this integration commit.

## 2026-11-06 — PR #6121 integration with published main

Integrated published main `1970e159b9` with the validated PR #6121 head `6e98ed1c86`. All 341 scoped files outside the shared tracker and rendered index remain byte-identical, including curated science and source evidence. The 777-row inventory retains every incoming row except this module's unchanged validated row; both dated journals are preserved. Validation implementation is unchanged. Prior validation remains evidence for the preserved science; renewed CI and review gate this integration commit.

## 2026-11-06 — PR #6121 integration with published main

Integrated published main `488d370561` with the validated PR #6121 head `5316e29917`. All 342 scoped files outside the shared tracker and rendered index remain byte-identical, including curated science and source evidence. The 777-row inventory retains every incoming row except this module's unchanged validated row; both dated journals are preserved. Incoming main adds warning-level ancestor-action consistency checks and qualifier-aware comparisons. All scoped gene reviews pass best-practice and GO-hierarchy validation under the incoming implementation. The historical full run is evidence for preserved science under its recorded implementation; renewed CI and review gate this integration commit.

## 2026-11-06 — PR #6121 integration with published main 577501df51

Integrated published main `577501df51` with the validated PR #6121 head `6b379f89d2`. All 344 scoped files outside the shared tracker and rendered index remain byte-identical, including curated science and source evidence. The 777-row inventory retains every incoming row except this module's unchanged validated row (no earlier completion rows regressed); both dated journals are preserved. Incoming main contains the merged beta-oxidation audit; validation implementation is unchanged. All incoming completion records and dated journal entries remain intact. The historical full run is evidence for preserved science under its recorded implementation; renewed CI and review gate this integration commit.

Integration proof: [validated-head-main4-integration.json](../analysis/module_audits/bacterial_cytochrome_c_maturation_system_i/validated-head-main4-integration.json).

## 2026-11-07 — cytochrome-c provenance follow-up validates

PR6121 provenance/CcmE follow-up passes full validation on 072461b9b2: 10,722 reviews, zero blocking errors and 374 frozen inputs verified. Fresh review, CI and actual merge pending. Record-section metadata was added to 23 reviews; OLEA2 CcmE orientation is explicitly a comparative inference. One inherited ECOLI ccmE process proposal is retired in place, preserving its original action and payload. Redundant broad core processes are removed while specific linkage processes remain. All 233 original annotation payloads/order, 68 protected gene/source files and 40 publication caches are preserved. Twenty-three focused gene checks, 24 histories, 22 renders, 151 coverage cases and five retirement controls pass. [Full-run proof](../analysis/module_audits/bacterial_cytochrome_c_maturation_system_i/round3-full-validation.json).

## 2026-11-07 — cytochrome-c main integration

Integrated published main e9d31cced895d2d74c464d57cbd40381e15520ab after the passing full run on 072461b9b2. All 369 frozen files outside shared project metadata/index remain byte-identical. Every incoming inventory row is preserved except the current cytochrome audit row; no completion rows regress. This is an integration with preserved science, not an additional full-corpus pass. Fresh review, CI and actual merge remain pending.

## 2026-11-06 — PR #6105 integration with published main

Integrated published main `db69104296` with the approved PR #6105 head `c972401f1d`. All 106 scoped files outside the shared tracker and rendered index remain byte-identical, including curated science and source evidence. The 777-row inventory retains every incoming row except this module's unchanged approved row; both dated journals are preserved. Validation implementation is unchanged. Prior validation remains evidence for the preserved science; renewed CI and review gate this integration commit.

## 2026-11-06 — PR #6105 integration with published main

Integrated published main `fd782f231a` with the validated PR #6105 head `5a8d2dcec4`. All 108 scoped files outside the shared tracker and rendered index remain byte-identical, including curated science and source evidence. The 777-row inventory retains every incoming row except this module's unchanged validated row; both dated journals are preserved. Validation implementation is unchanged. Prior validation remains evidence for the preserved science; renewed CI and review gate this integration commit.

## 2026-11-06 — PR #6105 integration with published main

Integrated published main `1970e159b9` with the validated PR #6105 head `850b2c7398`. All 110 scoped files outside the shared tracker and rendered index remain byte-identical, including curated science and source evidence. The 777-row inventory retains every incoming row except this module's unchanged validated row; both dated journals are preserved. Validation implementation is unchanged. Prior validation remains evidence for the preserved science; renewed CI and review gate this integration commit.

## 2026-11-06 — PR #6105 integration with published main

Integrated published main `488d370561` with the validated PR #6105 head `80efe0807d`. All 111 scoped files outside the shared tracker and rendered index remain byte-identical, including curated science and source evidence. The 777-row inventory retains every incoming row except this module's unchanged validated row; both dated journals are preserved. Incoming main adds warning-level ancestor-action consistency checks and qualifier-aware comparisons. All scoped gene reviews pass best-practice and GO-hierarchy validation under the incoming implementation. The historical full run is evidence for preserved science under its recorded implementation; renewed CI and review gate this integration commit.

## 2026-11-06 — PR #6105 integration with published main 577501df51

Integrated published main `577501df51` with the validated PR #6105 head `187f78fdcb`. All 113 scoped files outside the shared tracker and rendered index remain byte-identical, including curated science and source evidence. The 777-row inventory retains every incoming row except this module's unchanged validated row (no earlier completion rows regressed); both dated journals are preserved. Incoming main contains the merged beta-oxidation audit; validation implementation is unchanged. All incoming completion records and dated journal entries remain intact. The historical full run is evidence for preserved science under its recorded implementation; renewed CI and review gate this integration commit.

Integration proof: [validated-head-main4-integration.json](../analysis/module_audits/bacterial_choline_o_sulfate_uptake_and_desulfation/validated-head-main4-integration.json).

## 2026-11-07 — choline sulfate follow-up passes full validation

PR6105 Ruegeria evidence and candidate-activity follow-up validated on d27f88a303: full 10,716-review run passes with zero blocking errors; 123 frozen inputs verified. Current-head review, CI and actual merge remain pending. Four record-section tags distinguish reviewed UniProt source evidence; Ruegeria BetT remains an optional, unassigned cargo candidate. All 49 active annotation payloads and actions, 12 active NEW rows, 47 protected gene/source/analysis files and 12 publication caches are preserved. The two aliased record-section tags in the BetC core are evidence metadata; biological assertions are unchanged. Repository advisories remain documented in [the validation proof](../analysis/module_audits/bacterial_choline_o_sulfate_uptake_and_desulfation/round3-full-validation.json).

## 2026-11-07 — choline-sulfate shared tracker integration

Merged published main e9d31cced895d2d74c464d57cbd40381e15520ab into approved choline-sulfate head 38dbf82b9789d7caf4794c82d334b91d2ad5baf4. All 119 frozen non-project inputs remain byte-identical. Incoming inventory rows are preserved except this audit row; no completed audits regress. The full validation remains the recorded d27f88a303 run, not a new full-corpus run on this integration.

## 2026-11-07 — bacterial_choline_o_sulfate_uptake_and_desulfation main integration

Integrated main 2f72fda87ec460ef99562726f68795f2a2d9552f into approved head 41649e7eaeec646b59abcbe875530454cbcf0105. All 124 frozen files outside shared project metadata remain byte-identical. Incoming inventory rows are retained except this audit row and 0 independently reverified merged-completion rows; 0 missing historical rows are retained from this branch, and no completed audit regresses. Historical full-validation results remain scoped to their recorded heads; this integration is not a new full-corpus run. Fresh review, CI and actual merge remain pending.

## 2026-11-06 — flavonoid comparative audit and OPG merge verification

Start comparative flavonoid audit from merged PR #5971. Freeze fourteen existing reviews, 34 annotation rows and 34 source files; inspect three review articles and the 2013/2016/2024 primary evidence. A live KEGG census places all 50 complete seven-KO coassignments in Pseudomonadota without proving pathway activity. Correct the unsupported exclusion of UDP-glucose epimerase activity in Hsero_1012 to UNDECIDED and qualify the FdeD reaction position while preserving all inherited NEW rows. Record independent full-text access for four HERSS reviews. Seven newly seeded BRADU comparisons are being reviewed separately. OPG PR #2142 actually merged and 179 scoped files match its approved head; mark that module COMPLETE. Flavonoid module science, validation, dedicated PR, review, CI and merge remain pending.

[Verified OPG merge content](MODULE_TAXON_AUDIT/proofs/pr2142-merged-content.json) records all 179 compared files.

## 2026-11-06 — flavonoid comparative science integration

Integrate seven independently verified USDA110 comparisons with fourteen existing reviews, preserving all 45 pre-existing/seed annotation rows, inherited NEW actions and 48 raw/provider files. Curate three review articles and six primary studies, including independent ORS285 whole-locus evidence. Scope to Pseudomonadota with explicit sampling limits. Separate unresolved FdeD/FdeH context from the six chemical roles; preserve untested late assignments as hypotheses. Forty-four production-compiler coverage checks pass and four mutations are rejected. Dedicated PR, full-corpus validation and actual merge remain pending.

## 2026-11-06 — flavonoid full-validation closeout

Full validation at 48ae00aa44d310c22de47fa2d50f71ff6f59739c completed with exit 0 on 2026-11-06T21:31:35Z. All 258 frozen files remain unchanged. The 10691-review corpus has zero blocking errors; 115 term advisories and 52 reference advisories persist, with all 31 reference-advisory files outside this 21-gene panel. Best-practices validation reports zero errors and 27775 warnings; 54 pathway-reference checks pass. Scoped schema, semantic, rendering, history and compiler checks already pass. Scientific limits on late reaction assignments, FdeD/H dependence, FdeG evidence access and comparator native flux remain explicit. Dedicated PR and actual merge are still pending.

## 2026-11-06 — PR #6140 integration with published main 096c918920

Integrated published main `096c918920` with the validated PR #6140 head `9f5e80dcd5`. All 258 scoped files outside the shared tracker and rendered index remain byte-identical, including curated science and source evidence. The 777-row inventory retains every incoming row except this module's unchanged validated row and the previously verified OPG completion record retained verbatim from the approved head; both dated journals are preserved. Incoming main contains the merged OPG and DsbAB audits and the unrelated GJB3 review; validation implementation is unchanged. The corresponding OPG completion bullet is also preserved; incoming completion records and all dated journal entries remain intact. The historical full run is evidence for preserved science under its recorded implementation; renewed CI and review gate this integration commit.

Integration proof: [validated-head-integration.json](../analysis/module_audits/bacterial_flavonoid_degradation/validated-head-integration.json).

## 2026-11-06 — flavonoid PR #6140 published

Opened PR #6140 after full validation passed at science commit 48ae00aa44. Integrated main 096c918920 with 258 scoped files unchanged relative to the validated publication head; no validation implementation changed. Preserved the previously verified OPG completion row and bullet because the incoming shared ledger had reverted them to IN_PROGRESS. Updated this audit to PR_OPEN and recomputed the ledger counts from the inventory. Review, CI and actual merge remain pending.

## 2026-11-06 — PR #6140 integration with published main 577501df51

Integrated published main `577501df51` with the validated PR #6140 head `b12b932c33`. All 261 scoped files outside the shared tracker and rendered index remain byte-identical, including curated science and source evidence. The 777-row inventory retains every incoming row except this module's unchanged validated row and the previously verified OPG completion record retained verbatim from the validated head; both dated journals are preserved. Incoming main contains the merged OPG and DsbAB audits and the beta-oxidation audit; validation implementation is unchanged. The corresponding OPG completion bullet is also preserved; incoming completion records and all dated journal entries remain intact. The historical full run is evidence for preserved science under its recorded implementation; renewed CI and review gate this integration commit.

Integration proof: [validated-head-main2-integration.json](../analysis/module_audits/bacterial_flavonoid_degradation/validated-head-main2-integration.json).

## 2026-11-06 — flavonoid review follow-up and proposal withdrawal

Address the two requested action/reason corrections and apply the same participation criterion across the 21-member flavonoid panel. Eleven reviews now pass focused validation. Nine inherited B/D/H/I/J process proposals are retired in place, preserving all 46 source payloads, all 16 historical proposal rows and all 85 protected sources. Seven supported proposals remain active. Hsero_1012 carries a probable EC source defect and a qualified over-annotation judgment; three FdeB reviews consistently leave bond specificity unresolved. Module provenance, descriptions and family narrative are aligned, without changing validators or claiming native complete catabolism from coverage. Forty-four coverage cases and four mutation controls pass; twenty module advisories document the unresolved assignments. The earlier full run applies to its recorded inputs; a renewed full run is required before publication.

## 2026-11-07 — flavonoid review follow-up passes full validation

PR #6140 revised science passes full validation on 9e1e860ce0: 10,717 reviews, zero blocking errors and 300 frozen inputs verified. Nine inherited process proposals are retired in place; seven remain active. Fresh review, CI and actual merge pending. Hsero_1012 retains a qualified over-specificity judgment and reports the upstream substrate-specific EC assertion rather than blaming EC2GO. FdeB peptide claims and unresolved ester specificity now agree across the three genera. All 46 original annotation payloads/order and 85 sources are preserved. The nine retired proposals remain as historical rows. [Validation proof](../analysis/module_audits/bacterial_flavonoid_degradation/round1-full-validation.json).

## 2026-11-07 — flavonoid round-2 evidence and withdrawal follow-up

PR #6140 round-2 follow-up: nine retired proposals use explicit withdrawal actions; three FdeB orthologs retain supported broad hydrolase core inference while substrate and catalytic geometry remain unresolved. Two speculative reaction terms moved to questions. Ten focused gene checks, 44 coverage cases and four mutations pass; fresh full validation and publication pending. All 46 original annotation payloads/order and 91 existing source files are preserved. Characterized-family site mapping corrects a provider residue number and avoids an unsupported activity-loss claim from an alternative histidine candidate. Earlier full runs remain historical.

## 2026-11-07 — bacterial flavonoid degradation full validation passes

PR #6140 follow-up passes full validation on 58063482b8: 10,722 reviews, zero blocking errors and 345 frozen inputs verified. Publication, fresh review/CI and actual merge remain pending. [Recorded proof](../analysis/module_audits/bacterial_flavonoid_degradation/round2-full-validation.json).

## 2026-11-07 — bacterial_flavonoid_degradation main integration

Integrated main 2f72fda87ec460ef99562726f68795f2a2d9552f after the passing full run on 58063482b8ade016b8e30aed621b4e0457c02daa. All 341 frozen files outside shared project metadata remain byte-identical. Incoming inventory rows are retained except this audit row and 1 independently reverified merged-completion rows; 0 missing historical rows are retained from this branch, and no completed audit regresses. This is preserved-science integration, not a new full-corpus run. Fresh review, CI and actual merge remain pending.

## 2026-11-07 — bacterial flavonoid degradation full validation passes

PR #6140 follow-up passes full validation on ee4222b667: 10,754 reviews, zero blocking errors and 367 frozen inputs verified. Publication, fresh review/CI and actual merge remain pending. [Recorded proof](../analysis/module_audits/bacterial_flavonoid_degradation/round3-full-run.json).

## 2026-11-07 — bacterial_flavonoid_degradation main integration

Integrated main 5b68ef3aaca8960576ae1ad557815fe675f1e8a6 after the passing full run on ee4222b667d93d9587aa0502d028d3b1b78dabf7. All 363 frozen files outside shared project metadata remain byte-identical. Incoming inventory rows are retained except this audit row and 1 independently reverified merged-completion rows; 0 missing historical rows are retained from this branch, and no completed audit regresses. This is preserved-science integration, not a new full-corpus run. Fresh review, CI and actual merge remain pending.

## 2026-11-07 — bacterial_flavonoid_degradation main integration

Integrated main 5f65fb600c4150f550f37e334c15eaf8dad4032a after the passing full run on ee4222b667d93d9587aa0502d028d3b1b78dabf7. 361 frozen files remain byte-identical outside shared metadata and 2 preservation checkers with previously verified formatting equivalence. The checker hashes still match the recorded equivalent versions. Incoming inventory rows are retained except this audit row and 1 independently reverified merged-completion rows; 0 missing historical rows are retained from this branch, and no completed audit regresses. This is preserved-science integration, not a new full-corpus run. Fresh review, CI and actual merge remain pending.

## 2026-11-06 — cellulose cross-taxon audit

Twenty-one member reviews complete; 17 module references curated; 23 production compiler cases and focused module validation pass. Full validation is running. Existing PR #2143 is adopted; this expanded audit has not yet been pushed. The scope includes Pseudomonas, Rhodobacter, Agrobacterium, E. coli, Komagataeibacter, cyanobacteria and Streptomyces. All 88 original annotation payloads and 42 raw files are preserved; 11 new proposals are separate from one inherited NEW. Native strain output and unresolved envelope mechanisms remain explicitly qualified. This update changes only the cellulose inventory row; all other rows retain their dated evidence.

## 2026-11-06 — cellulose audit prepared for renewed review

The comparative audit continues existing PR #2143 with 21 COMPLETE reviews, 17 curated references and 25 passing compiler/oracle cases. Full validation finished with only 19 proven pre-existing quote errors in 17 unrelated yeast reviews; all other phases pass. The module records five support/envelope architectures and explicit biological gaps. Current-main integration preserves the curated panel and all raw sources. Independent biological review found no blocker at the stated scope; sampled route context and external-oracle limitations are now explicit. Fresh GitHub review and CI are required, so the project remains PR_OPEN rather than COMPLETE. Only the cellulose row is updated; all 714 other rows retain their dated evidence.

## 2026-11-06 — cellulose round17 full-run closure

Approved science `3cdca2d091dd8f770d8dad14367bbbae8443220f` completed full validation: 10,553 reviews; exactly 19 pre-existing reference errors in 17 unrelated yeast reviews; 23 baseline inputs unchanged; schema, ontology, best-practices and 54 pathway checks pass. The terminal proof pins the log and scientific-input hashes. This update changes only cellulose closure metadata and its inventory row; no gene, module or checker science changes. Existing project-publication history is explicitly accounted for. The PR remains open pending closure publication, current-head review/CI and actual merge.

## 2026-11-06 — PR #2143 integration with published main

Integrated published main `db69104296` with the approved PR #2143 head `a6a75ca3fd`. All 256 scoped files outside the shared tracker and rendered index remain byte-identical, including curated science and source evidence. The 777-row inventory retains every incoming row except this module's unchanged approved row; both dated journals are preserved. Validation implementation is unchanged. Prior validation remains evidence for the preserved science; renewed CI and review gate this integration commit.

## 2026-11-06 — PR #2143 integration with published main

Integrated published main `1970e159b9` with the validated PR #2143 head `afa272c536`. All 258 scoped files outside the shared tracker and rendered index remain byte-identical, including curated science and source evidence. The 777-row inventory retains every incoming row except this module's unchanged validated row; both dated journals are preserved. Validation implementation is unchanged. Prior validation remains evidence for the preserved science; renewed CI and review gate this integration commit.

## 2026-11-06 — PR #2143 tracker placement and tally

Correct the shared project page after integration for PR #2143: place the bacterial_cellulose_biosynthesis checkbox under Status and derive the displayed audit-state tally from all 777 inventory rows. This changes project prose and its rendering only; the inventory and all curated science/source files remain unchanged from 1bea5fd775373af484646091e092770dd5f4b034.

## 2026-11-06 — PR #2143 integration with published main

Integrated published main `488d370561` with the validated PR #2143 head `285a8cda82`. All 261 scoped files outside the shared tracker and rendered index remain byte-identical, including curated science and source evidence. The 777-row inventory retains every incoming row except this module's unchanged validated row; both dated journals are preserved. Incoming main adds warning-level ancestor-action consistency checks and qualifier-aware comparisons. All scoped gene reviews pass best-practice and GO-hierarchy validation under the incoming implementation. The historical full run is evidence for preserved science under its recorded implementation; renewed CI and review gate this integration commit.

## 2026-11-06 — PR #2143 integration with published main 5f8f3b5c5e

Integrated published main `5f8f3b5c5e` with the approved PR #2143 head `18989a9f5e`. All 263 scoped files outside the shared tracker and rendered index remain byte-identical, including curated science and source evidence. The 777-row inventory retains every incoming row except this module's unchanged approved row; both dated journals are preserved. Validation implementation is unchanged. The historical full run retains its explicitly documented pre-existing reference errors outside the cellulose panel; it is not an unconditional corpus pass. Renewed CI and review gate this integration commit.

Integration proof: [validated-head-main4-integration.json](../analysis/module_audits/bacterial_cellulose_biosynthesis/validated-head-main4-integration.json).

## 2026-11-06 — PR #2143 integration with published main 577501df51

Integrated published main `577501df51` with the validated PR #2143 head `2ce09e385e`. All 265 scoped files outside the shared tracker and rendered index remain byte-identical, including curated science and source evidence. The 777-row inventory retains every incoming row except this module's unchanged validated row; both dated journals are preserved. Validation implementation is unchanged. The historical full run retains its explicitly documented pre-existing reference errors outside the cellulose panel; it is not an unconditional corpus pass. Renewed CI and review gate this integration commit.

Integration proof: [validated-head-main5-integration.json](../analysis/module_audits/bacterial_cellulose_biosynthesis/validated-head-main5-integration.json).

## 2026-11-06 — cellulose upstream reference repairs verified

The 19 errors in 17 unrelated yeast reviews and 23 unchanged pins describe the historical validation revision, not current HEAD. At 57dd76f99b, all 17 review pins diverge after upstream repairs; both publication sources and all four validation inputs still match. Focused reference validation of all 17 repaired reviews now passes with zero blocking errors. This does not retrospectively change the original full-run exit code or certify newly integrated reviews; current-head CI remains required. No cellulose gene, module, family, source or validation-rule file changed. The two review threads are addressed by explicit revision-scoped notes while the original error tuples, blob pins and run counts remain intact.

## 2026-11-07 — bacterial_cellulose_biosynthesis main integration

Integrated main e9d31cced895d2d74c464d57cbd40381e15520ab into approved head 7186e121a183cb68bf2ffb8beea91c57cea704e6. All 269 frozen files outside shared project metadata remain byte-identical. Incoming inventory rows are retained except this audit row and 0 independently reverified merged-completion rows; 0 missing historical rows are retained from this branch, and no completed audit regresses. Historical full-validation results remain scoped to their recorded heads; this integration is not a new full-corpus run. Fresh review, CI and actual merge remain pending.

## 2026-11-07 — bacterial_cellulose_biosynthesis main integration

Integrated main 2f72fda87ec460ef99562726f68795f2a2d9552f into reviewed head 43613a1fa0e5f53b2813a4f0fda305f71f08c92a. All 271 frozen files outside shared project metadata remain byte-identical. Incoming inventory rows are retained except this audit row and 0 independently reverified merged-completion rows; 0 missing historical rows are retained from this branch, and no completed audit regresses. Historical full-validation results remain scoped to their recorded heads; this integration is not a new full-corpus run. Fresh review, CI and actual merge remain pending.

## 2026-11-07 — cellulose tracker and provenance review follow-up

PR #2143 tracker and provenance follow-up integrates main 2f72fda87e, derives counts from the current ledger, restores per-path preservation evidence, and records the complete GO:0090540 definition caveat. Historical validation retains its 19 pre-existing errors; a fresh full run is required before publication. The earlier round26 discrepancy was 33/6/4/734 versus the displayed 33/5/4/735; current counts are derived after integration rather than copying either old snapshot.

## 2026-11-07 — bacterial cellulose biosynthesis full validation passes

PR #2143 follow-up passes full validation on acee1d329a: 10,764 reviews, zero blocking errors and 282 frozen inputs verified. Publication, fresh review/CI and actual merge remain pending. [Recorded proof](../analysis/module_audits/bacterial_cellulose_biosynthesis/round27-full-run.json).

## 2026-11-07 — bacterial_cellulose_biosynthesis main integration

Integrated main 5b68ef3aaca8960576ae1ad557815fe675f1e8a6 after the passing full run on acee1d329af2f36b7f8cd8855d5d896e73cb2999. All 278 frozen files outside shared project metadata remain byte-identical. Incoming inventory rows are retained except this audit row and 0 independently reverified merged-completion rows; 0 missing historical rows are retained from this branch, and no completed audit regresses. This is preserved-science integration, not a new full-corpus run. Fresh review, CI and actual merge remain pending.

## 2026-11-07 — bacterial_cellulose_biosynthesis main integration

Integrated main 5f65fb600c4150f550f37e334c15eaf8dad4032a after the passing full run on acee1d329af2f36b7f8cd8855d5d896e73cb2999. All 278 frozen files outside shared project metadata remain byte-identical. Incoming inventory rows are retained except this audit row and 0 independently reverified merged-completion rows; 0 missing historical rows are retained from this branch, and no completed audit regresses. This is preserved-science integration, not a new full-corpus run. Fresh review, CI and actual merge remain pending.

## 2026-11-07 — cellulose approved-head integration of 7eee074bca

PR #2143 approved at 3bbce661d5; main 7eee074bca integrated locally with all 288 approved nonshared files preserved. Focused integration checks are recorded separately; the full-corpus PASS remains scoped to acee1d329a. Publication, current-head review/CI and actual merge remain pending. [Per-path preservation and validation scope](../analysis/module_audits/bacterial_cellulose_biosynthesis/round28-main-integration.json). The incoming OPG completion and flavonoid row are retained exactly. All 33 previously complete rows remain unchanged; no completion is inferred from an open-row status or from this local integration. Both parents’ dated journal entries and the pins autolink exclusion are preserved. The historical round-17 module pin describes its recorded revision; round27-full-run.json supersedes its validation status, without retrospectively changing that earlier receipt.

## 2026-11-07 — Comparative Isc assembly and transfer

Comparative Isc curation integrates 18 COMPLETE gene reviews, 208 preserved original rows with one explicit historical-NEW retirement, 20 assessed references including five reviews, two family reconciliations and 17 function-qualified representatives. Canonical Fdx-supported/HscBA-assisted capacity is distinguished from anaerobic and suppressor bypasses. The capacity audit passes 38 scenarios, six evidence-gate sensitivity checks and two structural mutations. Full validation remains pending before a dedicated PR.

## 2026-11-07 — bacterial isc iron sulfur cluster assembly full validation passes

Comparative audit passes full validation on daf2de4dc7: 10,753 reviews, zero blocking errors and 268 frozen inputs verified. Publication, fresh review/CI and actual merge remain pending. [Recorded proof](../analysis/module_audits/bacterial_isc_iron_sulfur_cluster_assembly/full-validation.json).

## 2026-11-07 — bacterial_isc_iron_sulfur_cluster_assembly main integration

Integrated main f5b02387a85bfaa85982a32f0c7cc0e41fe60c9e after the passing full run on daf2de4dc7d5d5c1cf790f159425007757be841a. All 264 frozen files outside shared project metadata remain byte-identical. Incoming inventory rows are retained except this audit row and 0 independently reverified merged-completion rows; 0 missing historical rows are retained from this branch, and no completed audit regresses. This is preserved-science integration, not a new full-corpus run. Fresh review, CI and actual merge remain pending.

## 2026-11-07 — bacterial isc iron sulfur cluster assembly full validation passes

PR #6175 follow-up passes full validation on 31d0901593: 10,763 reviews, zero blocking errors and 324 frozen inputs verified. Publication, fresh review/CI and actual merge remain pending. [Recorded proof](../analysis/module_audits/bacterial_isc_iron_sulfur_cluster_assembly/round1-full-validation.json).

## 2026-11-07 — bacterial_isc_iron_sulfur_cluster_assembly main integration

Integrated main 0a807fc55576d0371b2dfacb482f8d695992535b after the passing full run on 31d09015932f61ba17a3fbb537901cf4949621a4. All 320 frozen files outside shared project metadata remain byte-identical. Incoming inventory rows are retained except this audit row and 0 independently reverified merged-completion rows; 0 missing historical rows are retained from this branch, and no completed audit regresses. This is preserved-science integration, not a new full-corpus run. Fresh review, CI and actual merge remain pending.

## 2026-11-07 — Cellulose audit merge verified

PR #2143 actually merged as 0a807fc55576d0371b2dfacb482f8d695992535b; 291 changed nonshared files are byte-identical to the reviewed head and 21 changed reviews remain COMPLETE with no PENDING rows. [Merge proof](MODULE_TAXON_AUDIT/proofs/pr2143-merged-content.json).

## 2026-11-07 — bacterial methionine cycle full validation passes

Comparative audit passes full validation on 125cfcb38c: 10,801 reviews, zero blocking errors and 727 frozen inputs verified. Publication, fresh review/CI and actual merge remain pending. [Recorded proof](../analysis/module_audits/bacterial_methionine_cycle/full-validation.json).

## 2026-11-07 — bacterial_methionine_cycle main integration

Integrated main bb89a377830600d2850d64215e0da94a47a06c6a after the passing full run on 125cfcb38cfa1ef3a0733a85281e10e37cb4cef5. All 723 frozen files outside shared project metadata remain byte-identical. Incoming inventory rows are retained except this audit row and 0 independently reverified merged-completion rows; 0 missing historical rows are retained from this branch, and no completed audit regresses. This is preserved-science integration, not a new full-corpus run. Fresh review, CI and actual merge remain pending.
