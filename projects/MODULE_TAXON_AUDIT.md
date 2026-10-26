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
- [ ] `alginate_polymerization_export`: [draft PR #5552](https://github.com/ai4curation/ai-gene-review/pull/5552): 18 reviews (99 rows), 23 references; cross-species MF and source-defect corrections approved; subsequent ISS source-tracing follow-up `639f50743b` validated and pushed. Full validation passed. Awaiting shared AlgX completion in #5546 and renewed review.
- [x] `aliphatic_glucosinolate_myrosinase_defense`: [PR #5550](https://github.com/ai4curation/ai-gene-review/pull/5550) merged as `75d569bf94a697ed142f0f1397736819563b8d74`. All 187 scoped files from the 208-file paginated PR match the approved head; 35 reviews, 453 rows and 31 curated references are verified.
- [ ] `androgen_receptor_signaling`: [PR #5554](https://github.com/ai4curation/ai-gene-review/pull/5554): 15 reviews across human, mouse, medaka, zebrafish and shark (1,683 preserved rows); 26 curated references. Full validation passed; all requested evidence/rationale corrections published as `65e616afb8` with focused validation. Renewed CI and review are required.
- [ ] `anti_crispr_suppression`: [PR #5555](https://github.com/ai4curation/ai-gene-review/pull/5555) opened after full validation passed. Thirteen reviewed representatives, 42 rows and qualified alternative mechanisms are committed on `ad799f71a2`; CI validation passed; automated scientific review failed twice with the explicit account usage-limit diagnostic, before producing a verdict.
- [ ] `apoptotic_execution_phase`: [PR #5558](https://github.com/ai4curation/ai-gene-review/pull/5558), sixteen human/mouse reviews complete (1,608 preserved rows), with 35 curated references and ten qualified edges. All focused checks and full repository validation pass; normal CI and scientific review are pending.
- [ ] `aps_dependent_assimilatory_sulfate_reduction`: 29 bacterial, fungal and plant reviews complete (496 rows), 28 curated references and five qualified edges. Independent module QA and all focused checks pass; full validation is running. Donor uncertainties and mixed-family restrictions remain explicit.
- [ ] `arginine_biosynthesis`: 15th audit started. Thirty-nine original bacterial/fungal exemplars are being reviewed or normally seeded; primary plant/archaeal work guides expanded sampling. Donor-specific ArgJ activities and the fungal NAGS/NAGK metabolon are being checked against primary experiments.
- [ ] Remaining 687 baseline modules: recorded as NOT_STARTED. Eight of 702 baseline audits are complete; seven further audits are active. Refresh upstream additions before final completion.

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
