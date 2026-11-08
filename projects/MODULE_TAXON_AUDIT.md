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



## 2026-11-07 — ImuABC cross-species audit

Comparative ImuABC audit: two narrative reviews and 15 assessed references, 12 reviewed exemplars, three matched cassette panels and a separately characterized Myxococcus ImuA ATPase. Original 80 rows plus three new-gene seed rows are preserved; one new ATPase annotation. 63 capacity/compiler cases pass. Final focused validation and full corpus run precede publication; fresh review, CI and actual merge remain pending.

## 2026-11-07 — bacterial imuabc damage induced mutagenesis full validation passes

Comparative audit passes full validation on 9d7cbd20fe: 10,748 reviews, zero blocking errors and 212 frozen inputs verified. Publication, fresh review/CI and actual merge remain pending. [Recorded proof](../analysis/module_audits/bacterial_imuabc_damage_induced_mutagenesis/full-validation.json).

## 2026-11-07 — bacterial_imuabc_damage_induced_mutagenesis main integration

Integrated main e9d50a8a42ab5e6b5560d09ff8c44e64f4c77360 after the passing full run on 9d7cbd20fe52fa4c3be3a3d1563baff493539a67. All 208 frozen files outside shared project metadata remain byte-identical. Incoming inventory rows are retained except this audit row and 0 independently reverified merged-completion rows; 0 missing historical rows are retained from this branch, and no completed audit regresses. This is preserved-science integration, not a new full-corpus run. Fresh review, CI and actual merge remain pending.

## 2026-11-07 — bacterial imuabc damage induced mutagenesis full validation passes

PR #6169 follow-up passes full validation on 357df862a5: 10,757 reviews, zero blocking errors and 238 frozen inputs verified. Publication, fresh review/CI and actual merge remain pending. [Recorded proof](../analysis/module_audits/bacterial_imuabc_damage_induced_mutagenesis/round1-full-validation.json).

## 2026-11-07 — bacterial_imuabc_damage_induced_mutagenesis main integration

Integrated main 7eee074bca991ff31c7ec235110dd6c93ebb2ece after the passing full run on 357df862a5b54dfad3483658a831b357c88c85f3. All 234 frozen files outside shared project metadata remain byte-identical. Incoming inventory rows are retained except this audit row and 0 independently reverified merged-completion rows; 0 missing historical rows are retained from this branch, and no completed audit regresses. This is preserved-science integration, not a new full-corpus run. Fresh review, CI and actual merge remain pending.

## 2026-11-07 — bacterial imuabc damage induced mutagenesis full validation passes

PR #6169 follow-up passes full validation on 90ccb6b4b3: 10,766 reviews, zero blocking errors and 247 frozen inputs verified. Publication, fresh review/CI and actual merge remain pending. [Recorded proof](../analysis/module_audits/bacterial_imuabc_damage_induced_mutagenesis/round2-full-validation.json).

## 2026-11-07 — bacterial_imuabc_damage_induced_mutagenesis main integration

Integrated main 0a807fc55576d0371b2dfacb482f8d695992535b after the passing full run on 90ccb6b4b319515f57990aed214e082c7aae7b71. All 243 frozen files outside shared project metadata remain byte-identical. Incoming inventory rows are retained except this audit row and 0 independently reverified merged-completion rows; 0 missing historical rows are retained from this branch, and no completed audit regresses. This is preserved-science integration, not a new full-corpus run. Fresh review, CI and actual merge remain pending.

## 2026-11-07 — bacterial_imuabc_damage_induced_mutagenesis main integration

Integrated main 597e48b1634d7b6b85739e8cd037571b949f372f after the passing full run on 90ccb6b4b319515f57990aed214e082c7aae7b71. All 258 frozen files outside shared project metadata remain byte-identical. Incoming inventory rows are retained except this audit row and 0 independently reverified merged-completion rows; 0 missing historical rows are retained from this branch, and no completed audit regresses. This is preserved-science integration, not a new full-corpus run. Fresh review, CI and actual merge remain pending.

## 2026-11-08 — resume PR #6125 after disk cleanup

Integrate main a344758bae648a999bbe316e9b1e2289a958d1bc into paused PR #6125 at 435168522a542b6eb7111e65e8bdcfb6ba82bd91. All 199 branch-specific files outside shared project metadata retain their exact Git object ids. Conflicting project status entries and dated journal sections are retained from both parents. Prior validation/review results remain scoped to their recorded commits; this merge requires fresh CI and review.
