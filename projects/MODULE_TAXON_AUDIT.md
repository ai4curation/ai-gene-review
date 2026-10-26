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
at commit `18649bf003`, refreshed to 714 modules against `10fd59941f` on 2026-10-26.
The 12 additions are explicitly queued as NOT_STARTED. Every module starts unaudited for this project, including the
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
- [ ] `adrenal_steroidogenesis`: [PR #5571](https://github.com/ai4curation/ai-gene-review/pull/5571), head `74e860184b`. The corrective PR restores 22 supported organelle assertions across seven genes while preserving all 320 original rows. Full local validation and all build CI pass. Automated scientific review failed before assessment; the audit remains reopened until the correction is reviewed and merged.
- [x] `aerobic_nicotinate_degradation`: [PR #5544](https://github.com/ai4curation/ai-gene-review/pull/5544) merged as `94a80ada9f7143d2fb1b38b5e97a5301859c0a7c`. Twelve references and twelve member reviews (43 rows) were verified; 64 scoped curated/history files match the approved head. The NicD localization supersession is recorded in the older audit ledger.
- [ ] `alcoholic_fermentation`: [PR #5572](https://github.com/ai4curation/ai-gene-review/pull/5572), head `337db24a4f`. The corrective PR retains both SCHPO adh4 mitochondrial assertions alongside its matrix claims, preserving all 15 payloads and module YAML. Full local validation and all build CI pass. Automated review failed before assessment; the audit remains reopened.
- [ ] `alginate_o_acetylation`: [PR #5546](https://github.com/ai4curation/ai-gene-review/pull/5546), head `f15f9ec44b`. Four metadata-only conflicts were resolved with all 83 reviewed curated/history paths unchanged. Focused checks and all build CI pass. Current-head automated review failed before assessment; approval remains required.
- [ ] `alginate_polymerization_export`: [draft PR #5552](https://github.com/ai4curation/ai-gene-review/pull/5552): 18 reviews, 99 rows and 23 references. Head `639f50743b` is approved with all checks passing. Keep draft until shared AlgX work in #5546 merges, then integrate and verify that dependency.
- [x] `aliphatic_glucosinolate_myrosinase_defense`: [PR #5550](https://github.com/ai4curation/ai-gene-review/pull/5550) merged as `75d569bf94a697ed142f0f1397736819563b8d74`. All 187 scoped files from the 208-file paginated PR match the approved head; 35 reviews, 453 rows and 31 curated references are verified.
- [ ] `androgen_receptor_signaling`: [PR #5554](https://github.com/ai4curation/ai-gene-review/pull/5554), head `93ce23a1a7`. Fifteen reviews and 1,683 original row payloads are preserved. Citation follow-up passed focused checks and all build CI. Automated scientific review and its controlled retry both terminated before assessment; current-head approval is still required.
- [ ] `anti_crispr_suppression`: [PR #5555](https://github.com/ai4curation/ai-gene-review/pull/5555), head `b2bba44f7f`. Thirteen reviews preserve all 42 rows. The availability cleanup passed focused checks and all build CI; canonical full-paper access limitations remain explicit. Automated review and its controlled retry failed before assessment; no approval is inferred.
- [ ] `apoptotic_execution_phase`: [PR #5558](https://github.com/ai4curation/ai-gene-review/pull/5558), head `bb9c384a39`. Published 38 additional CASP3/Casp3 review corrections, preserving 399 payloads and both cores. Expanded 75-claim audit has 25 specific uncertainties. Restored shared executioner node ID; 714 current-main modules compile and 54 local logic tests pass. Current-head CI/review required.
- [ ] `aps_dependent_assimilatory_sulfate_reduction`: [PR #5560](https://github.com/ai4curation/ai-gene-review/pull/5560), head `8553f16ce5`. Integrated upstream section metadata without changing the 29 approved gene YAMLs or module. All focused normal checks, 46 logic tests and current build CI pass. Current-head automated review failed before assessment; this audit is not yet complete.
- [ ] `arginine_biosynthesis`: [PR #5563](https://github.com/ai4curation/ai-gene-review/pull/5563), head `c590f53f16`. The source-grounded arg3 follow-up preserves 555 member rows and companion CAR1 consistency. Integrated main after 19 metadata-only conflicts, preserving all 227 branch-scoped curated/history paths. All 19 focused gene checks pass. Published updated head requires current CI and scientific review; prior requests are not treated as cleared.
- [ ] `arginine_catabolism_arginase_pathway`: [PR #5566](https://github.com/ai4curation/ai-gene-review/pull/5566), head `0cb2da6900`. Integrated four upstream metadata-only conflicts while preserving all 100 approved curated/history paths. Four focused term/source checks and all build CI pass. Current-head automated review failed before assessment; no merge or approval is inferred.
- [ ] `aspartate_asparagine_metabolism`: [PR #5568](https://github.com/ai4curation/ai-gene-review/pull/5568), head `51e9648743`. Twenty-seven reviews preserve 548 rows across the comparative panel. Integrated main after 3 metadata-only conflicts, preserving all 146 branch-scoped curated/history paths. All 3 focused gene checks pass. Published updated head requires current CI and scientific review; prior requests are not treated as cleared.
- [ ] `aspartate_family_threonine_biosynthesis`: [PR #5569](https://github.com/ai4curation/ai-gene-review/pull/5569), head `cd5fc8efd8`. Published the scientific follow-up: 19 reviewed genes retain 379 original payloads; source-specific enzyme/cofactor, sulfur-pathway, localization and prose corrections are validated. All 24 members now have 439 final rows. Integrated main after 4 metadata-only conflicts, preserving all 152 branch-scoped curated/history paths. All 4 focused gene checks pass. Published updated head requires current CI and scientific review; prior requests are not treated as cleared.
- [ ] `autonomous_flowering_pathway`: [PR #5574](https://github.com/ai4curation/ai-gene-review/pull/5574), head `8de312ffd9`. Published the 15-member, 303-row audit as PR #5574 after full repository validation passed. Both commits survived rebase onto 10fd59941f unchanged by range-diff. Thirteen native Arabidopsis activities have verified family descriptors; two rice proteins remain reviewed comparators. All 34 references, 10 edges, 12 route cases and 46 logic tests are documented. All current-head build CI pass; automated scientific review failed before assessment, so approval remains required.
- [ ] `auxin_nuclear_signaling`: [PR #5576](https://github.com/ai4curation/ai-gene-review/pull/5576). PR #5576 is open after full repository validation passed. All 14 reviews preserve 632 original payloads, with 633 final rows including one supported TIR1 cyclase proposal. Nineteen family-grounded activity annotons, 29 assessed references and 13 primary-backed edges separate Arabidopsis and Marchantia implementations. Independent scientific QA, 22 route cases and 46 logic tests pass; review and CI remain required.
- [ ] `auxin_polar_transport`: Five rice/moss/liverwort reviews preserve all 28 original rows and add one supported OsAUX1 influx MF (29 final); focused checks, histories and renders pass. Twelve Arabidopsis reviews remain active. Full comparative and compartmentation reviews are mined; module integration is checking native route context, tissue polarity, ABCB cooperation and kinase/chaperone regulation. No complete network is inferred from a lone exporter.
- [ ] Remaining 693 modules are NOT_STARTED. Six of714 current audits are complete; fifteen are active, including two reopened.

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

The arginine member panel is complete:43 proteins and555 preserved annotation rows, including2 prior proposals and no newly added rows. All focused member checks, histories and renders pass; full validation is running. The added archaeal ArgJ is recycling-only, plant NAGK/WIN1 anchor plastid reactions, and short mycobacterial ArgA retains its weak glutamate-efficiency caveat. Independent module QA remains in progress. Sulfate is committed and its full reference validation continues. Apoptosis PR5558 is open; its automated review also hit the shared account quota before producing a verdict. The eight verified merges remain the only completed baseline audits.

Independent arginine module QA is now complete: all43 family/member placements agree with fetched classifications, cached GO-CAM assertions were checked, and22 curated references support9 connections. The draft no longer attributes type2 ArgC classification to an unrelated review passage or restricts ArgA initiation to the linear release route. Full validation remains the outstanding pre-PR gate.

## 2026-10-26 — arginase catabolism and CI follow-up

The sixteenth audit separates demonstrated budding-yeast compartmental flux from broader fungal inference, restores the fission-yeast Arg3 re-synthesis context, and adds the distinct plant arginase/agmatinase family. Thirty-two sources and four evidence-backed connections are drafted. Sulfate and arginine full validation remain live. Apoptosis CI exposed a real module logic failure: an empty context satisfies its current all-optional structure. A biology-aware correction is underway; no approval or merge gate is bypassed.

Sulfate full validation reached terminal success, current-main integration preserved all 197 scoped files, and PR #5560 is open. The apoptosis Boolean correction is published as `b4f92e028b` with 54 passing logic tests. All 18 arginase member checks now pass (357 preserved rows, no newly added rows); a direct ARGAH2 agmatinase result exposed an overly narrow family-level scope, which is being corrected from primary evidence.

Independent arginase QA now passes: 34 source entries, four evidence-backed connections, 46 module-logic tests and 14 route cases. The PTHR11358 SF32 correction retains all existing PAINT assertions and APAUH exceptions; the global family/gene crosscheck reports zero conflicts across 734 families. All eighteen gene reviews are committed as `bfdb0069d7`; full validation is running before PR creation.

The latest sulfate scientific-review run `40270283163` and corrected apoptosis run `40270373152` both ended with the verified account-usage-limit diagnostic before producing a review. Their build checks continue; no review approval is inferred from a workflow failure.

## 2026-10-26 — aspartate/asparagine audit begins

Arginine full validation and all 46 module-logic tests passed; PR #5563 is open. The seventeenth audit starts from a clean current-main worktree with 25 planned member reviews. The taxon boundary must distinguish the eukaryotic formation/turnover module from bacterial asparaginase comparators, add the plant N-terminal-nucleophile implementation, and avoid treating all reactions as glutamate-dependent transamination. Literature searches located comparative aminotransferase, ASNS and asparaginase reviews plus primary plant and fungal studies. The sulfate CI validation and suite jobs passed; remaining CI and scientific-review gates are still required.

The aspartate/asparagine panel expanded to six Arabidopsis proteins after the plastid review identified two distinct AspAT implementations. All 27 reviews now pass with 548 preserved rows and no added annotations. Independent QA confirmed nine family labels,25 exemplar placements and12 exact GO-CAM activity links. Thirteen route cases pass. The newer ASP3 evolutionary evidence is reconciled into PTHR11707 without changing PAINT seeds or verdicts. Full validation is running.

Arginase full validation passed with terminal exit zero and PR #5566 is open. Final Asp/Asn scientific QA corrected three negative localization rationales to UNDECIDED while retaining two directly assayed ASP5 negative enzyme activities. Final548-row totals are323 ACCEPT,110 MODIFY,65 non-core,20 REMOVE,25 UNDECIDED and5 over-annotation assessments. No new annotations were added.

## 2026-10-26 — threonine backbone audit starts

Asp/Asn curation is committed and pushed as `98bd4c37e3`; full validation is still running. The eighteenth audit uses an independent worktree and24 planned gene reviews. Two archaeal enzymes establish specific step exemplars, not an entire archaeal pathway. The proposed Arabidopsis ASAD locus At1g14810 lacks an official gene symbol and currently has prediction-heavy annotation; independent evidence must determine the strength of that exemplar. ThrH uses phosphoserine rather than ATP, plant O-phosphohomoserine also feeds methionine, and new Hom6/chromatin literature requires separation of metabolic and noncanonical effects.

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

The twentieth audit, nuclear auxin signaling, has a14-target632-row baseline and native Marchantia exemplars resolved to published clones/loci. Recent receptor adenylate-cyclase evidence and the 2015 primary-source correction will be assessed explicitly. Six baseline audits remain complete, fourteen active, 682 unstarted.

## 2026-10-26 — flowering PR, preserved integrations and complete inventory refresh

Published flowering PR #5574 after terminal full repository validation. The rebase preserved both branch commits exactly. Arginine, aspartate/asparagine and threonine integrate upstream metadata with their reviewed curated content byte-identical; the threonine scientific follow-up is separately recorded. Renewed reviews and CI are still required. Automated-review execution failures do not count as approvals or resolution of prior scientific requests.

Refreshed the module universe against `10fd59941f`: 12 additional modules are now explicitly tracked, for 714 total (six complete, fourteen active/reopened, 694 not started). The additions are `acetylcholine_signaling`, `dna_cytosine_methylation_cycle`, `dopamine_receptor_signaling`, `il21_signaling`, `il22_signaling`, `il34_signaling`, `nmj_achr_clustering`, `prostanoid_biosynthesis`, `protein_kinase_c_signaling`, `reelin_signaling`, `trail_apoptotic_signaling`, `visual_phototransduction`. All require the same literature, taxon, family, member-review and merged-PR evidence as the original 702.

## 2026-10-26 — nuclear auxin committed; polar transport review started

The nuclear auxin audit now has14 complete member reviews,633 rows,29 assessed references and13 supported edges. The TIR1 route requires its demonstrated cyclase activity; AFB2 and Marchantia activity remain unresolved. Exact ARF partner evidence was recovered normally and all source follow-ups preserve original payloads/actions. Independent scientific QA passes. Full validation restarted after an environmental disk-space failure; its earlier log is retained and no successful run is inferred from focused checks.

The polar-transport audit starts with17 products and483 original rows. An APFS copy-on-write checkout preserves full tracked content and independent edits without duplicating the repository data; this resolved the disk problem after Orca runtime and ordinary checkout failures. Current PR build checks pass, but automated scientific-review failures still prevent approval on pending branches. Six audits remain complete, fifteen active/reopened,693 unstarted of714.

## 2026-10-26 — nuclear auxin PR and comparative transport reviews

Nuclear auxin full repository validation reached terminal success and PR #5576 is open. Its 14 committed reviews match the final payload and source checks. The five polar-transport comparative reviews are complete, preserving 28 original rows plus one independently supported OsAUX1 influx proposal. The Arabidopsis panels and context-specific module integration continue. Six audits remain verified complete; opening a PR does not count as completion.
