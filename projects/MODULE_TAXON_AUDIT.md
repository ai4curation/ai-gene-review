---
title: Module literature, taxonomy and member review audit
maturity: IN_PROGRESS
last_reviewed: 2026-10-26
tags: [BIOLOGY_DOMAIN]
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
at commit `18649bf003`. Every module starts unaudited for this project, including the
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

- [x] `2_aminoethylphosphonate_degradation`: [PR #5538](https://github.com/ai4curation/ai-gene-review/pull/5538) merged after approval and required checks, at `7d28f887b2dbbab34afee940716ba660efc3a173`. Six member reviews, comparative literature, step/edge evidence and taxon/family grounding were rechecked in the merged content.
- [x] `abscisic_acid_signaling`: [PR #5540](https://github.com/ai4curation/ai-gene-review/pull/5540) merged as `d4ae4f02f7ab9759d41d104d7cd7af0ec66abb16`. All 19 reviews (524 rows), 26 references and lineage-specific signaling constraints were verified in merged content after approved checks.
- [x] `activin_receptor_signaling`: [PR #5541](https://github.com/ai4curation/ai-gene-review/pull/5541) merged as `aff0030d3689b50ae9f6d147fc8334a0b942f0a7`. All 11 reviews, 29 references, taxon/step evidence and session histories were verified unchanged from the approved head.
- [x] `adp_heptose_biosynthesis`: [PR #5542](https://github.com/ai4curation/ai-gene-review/pull/5542) merged as `8954a5dc480f1311f440eb4e50f5cefca5931980` after approval and required checks. Its 16 member reviews, 12 references and 26 histories were inspected; 44 curated/history files match the approved head.
- [x] `adrenal_steroidogenesis`: [PR #5543](https://github.com/ai4curation/ai-gene-review/pull/5543) merged as `72b4d12be1a4b1dbbd1e4abd526ecfd4e06b7a3f` after approval and required checks. All 13 reviews (434 rows), 26 references and 25 histories are curated; 65 scoped curation/history files match the approved head.
- [x] `aerobic_nicotinate_degradation`: [PR #5544](https://github.com/ai4curation/ai-gene-review/pull/5544) merged as `94a80ada9f7143d2fb1b38b5e97a5301859c0a7c`. Twelve references and twelve member reviews (43 rows) were verified; 64 scoped curated/history files match the approved head. The NicD localization supersession is recorded in the older audit ledger.
- [x] `alcoholic_fermentation`: [PR #5545](https://github.com/ai4curation/ai-gene-review/pull/5545) merged as `16bffd8e632185a8be7f5d9936d01c18017d33f7`. All 23 members (487 original rows), 34 references and revised BdhA family scope were verified; all 105 scoped curation/history files match the approved head.
- [ ] `alginate_o_acetylation`: [PR #5546](https://github.com/ai4curation/ai-gene-review/pull/5546): 12 reviews (52 rows), 15 references and full validation complete. Approval and all head checks passed. The shared tracker conflict following #5550 was resolved without changing biological curation; renewed checks/review required.
- [ ] `alginate_polymerization_export`: [draft PR #5552](https://github.com/ai4curation/ai-gene-review/pull/5552): 18 reviews (99 rows), 23 references; cross-species MF and source-defect follow-up plus supported Azotobacter Alg8 ISS proposal `1a4548547f` validated. Full validation passed. Awaiting shared AlgX completion in #5546 and renewed review.
- [x] `aliphatic_glucosinolate_myrosinase_defense`: [PR #5550](https://github.com/ai4curation/ai-gene-review/pull/5550) merged as `75d569bf94a697ed142f0f1397736819563b8d74`. All 187 scoped files from the 208-file paginated PR match the approved head; 35 reviews, 453 rows and 31 curated references are verified.
- [ ] `androgen_receptor_signaling`: [PR #5554](https://github.com/ai4curation/ai-gene-review/pull/5554): 15 reviews across human, mouse, medaka, zebrafish and shark (1,683 preserved rows); 26 curated references. Full validation passed; review requested claim-specific evidence and rationale corrections, now underway.
- [ ] `anti_crispr_suppression`: [PR #5555](https://github.com/ai4curation/ai-gene-review/pull/5555) opened after full validation passed. Thirteen reviewed representatives, 42 rows and qualified alternative mechanisms are committed on `ad799f71a2`; CI and scientific review are running.
- [ ] `apoptotic_execution_phase`: sixteen human/mouse reviews complete (1,608 preserved rows), with 35 curated references and ten qualified edges. All focused checks pass; full validation is running.
- [ ] `aps_dependent_assimilatory_sulfate_reduction`: 14th audit started. Comparative research distinguishes plant glutathione-dependent APR1, fungal/PAPS routes and the unresolved Pseudomonas CysI donor. Reviewing 26 existing members and adding three verified Arabidopsis exemplars.
- [ ] `arginine_catabolism_arginase_pathway`: [PR #5566](https://github.com/ai4curation/ai-gene-review/pull/5566). Eighteen reviews preserve 357 original rows (359 current rows after two matrix proposals); 34 curated sources and four evidence-backed connections. Science remains approved at integrated head `78b415cf54`. Restoring the dropped tracker entry is the sole current review blocker; renewed review and merge remain required.
- [ ] Remaining 698 of 714 inventoried modules: recorded as NOT_STARTED. 8 audits are complete; 8 further audits are active. This branch began with 702 entries; the explicit twelve-entry refresh is documented below. Recheck upstream additions before final completion.

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


## Restored historical audit notes

The following three dated sections were authored during this audit and were lost when the shared tracker was resolved entirely to upstream. They describe progress at those earlier sessions, not current PR states; the current arginase status and row accounting appear in the checklist and restoration note below. Existing upstream notes are preserved verbatim.

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

## 2026-10-26 — arginase tracker restoration after integration

The integration at `78b415cf54` preserved the approved gene, family and module science but dropped this audit's tracker entry and historical notes. Restored the entry from the canonical tracker with current module-derived structure: nine family-based annotons, each with function-level evidence, 18 represented proteins, Eukaryota context qualified to characterized fungal, plant and animal implementations, 34 curated source entries and four connections. The 357 original rows are preserved; two approved ARGAH1/ARGAH2 matrix proposals bring the current review total to 359. No biological assertion was changed. The latest reviewer explicitly approves the science and requests only tracker restoration; this audit remains active until renewed review/checks and verified merge.

This branch's inventory initially contained 702 modules, not 714. Added the twelve missing canonical entries after verifying their module files: eleven remain NOT_STARTED, while acetylcholine_signaling retains its actual PR_OPEN status and evidence. The resulting 714-entry inventory has eight COMPLETE, eight active and 698 NOT_STARTED entries. Every unrelated pre-existing module entry and all upstream notes remain unchanged. These are branch-local totals, not a claim that main already carried the refreshed inventory or that an open PR has merged.
