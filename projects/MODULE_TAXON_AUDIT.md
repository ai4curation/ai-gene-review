---
title: Module literature, taxonomy and member review audit
maturity: IN_PROGRESS
last_reviewed: 2026-10-25
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
- [ ] `abscisic_acid_signaling`: [PR #5540](https://github.com/ai4curation/ai-gene-review/pull/5540) has 19 reviewed members (524 rows), passed full local validation and is approved in the normal merge queue.
- [ ] `activin_receptor_signaling`: [PR #5541](https://github.com/ai4curation/ai-gene-review/pull/5541) is approved with all required head checks green and awaits merge-queue integration. All 11 members and 29 references curated; full local validation passed.
- [ ] `adp_heptose_biosynthesis`: [PR #5542](https://github.com/ai4curation/ai-gene-review/pull/5542) is approved and queued after full repository validation. All 16 members, 12 references and 26 histories are complete.
- [ ] `adrenal_steroidogenesis`: [PR #5543](https://github.com/ai4curation/ai-gene-review/pull/5543) is ready after full validation. Its 13 gene reviews preserve 434 rows; 26 references and 21 histories are curated. Review fixes are pushed on `3837d4fbce`; upstream metadata-only conflicts are resolved on `988d038b7d` and renewed CI/review are running.
- [ ] `aerobic_nicotinate_degradation`: [draft PR #5544](https://github.com/ai4curation/ai-gene-review/pull/5544) has 12 curated references and 12 gene reviews. Follow-up `90df36ce72` retains all 42 original rows and adds one evidence-backed NicC process proposal (43 total); 27 histories and all targeted checks pass. Full validation is running.
- [ ] `alcoholic_fermentation`: [draft PR #5545](https://github.com/ai4curation/ai-gene-review/pull/5545) has 23 members and 487 original rows reviewed across yeast, plants, bacteria and Carassius; 34 curated references. Canonical and E1-derived entry variants, member-specific metal activation, native Bacillus branch and six comparative reviews are integrated. Targeted checks pass and full validation is running; the dedicated PR awaits full validation and review.
- [ ] Remaining 695 baseline modules: recorded individually as NOT_STARTED. One of 702 baseline audits is complete; six further module PRs are open. Refresh upstream additions before final completion.

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
