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

- [x] `2_aminoethylphosphonate_degradation`: [PR #5538](https://github.com/ai4curation/ai-gene-review/pull/5538) merged after approval and required checks, at `7d28f887b2dbbab34afee940716ba660efc3a173`. Six member reviews, comparative literature, step/edge evidence and taxon/family grounding were rechecked in the merged content.
- [x] `abscisic_acid_signaling`: [PR #5540](https://github.com/ai4curation/ai-gene-review/pull/5540) merged as `d4ae4f02f7ab9759d41d104d7cd7af0ec66abb16`. All 19 reviews (524 rows), 26 references and lineage-specific signaling constraints were verified in merged content after approved checks.
- [ ] `acetylcholine_signaling`: [PR #5582](https://github.com/ai4curation/ai-gene-review/pull/5582). Follow-up d04592d5a1 resolves six CHRNA7 amyloid-related transfers using the available full text, distinguishes soluble oligomers from later plaque burden, and repairs source-analysis and module prose. All 44 reviews, 2,786 original rows and 88 raw sources are preserved. The submitted verdict remains CHANGES_REQUESTED pending a superseding review; fresh review and build checks are running.
- [x] `activin_receptor_signaling`: [PR #5541](https://github.com/ai4curation/ai-gene-review/pull/5541) merged as `aff0030d3689b50ae9f6d147fc8334a0b942f0a7`. All 11 reviews, 29 references, taxon/step evidence and session histories were verified unchanged from the approved head.
- [x] `adp_heptose_biosynthesis`: [PR #5542](https://github.com/ai4curation/ai-gene-review/pull/5542) merged as `8954a5dc480f1311f440eb4e50f5cefca5931980` after approval and required checks. Its 16 member reviews, 12 references and 26 histories were inspected; 44 curated/history files match the approved head.
- [x] `adrenal_steroidogenesis`: [PR #5571](https://github.com/ai4curation/ai-gene-review/pull/5571). Merged as `38c2b634f063c40c1e957bde87be87050daed719` after approval and passing checks. All 31 scoped curation, history and source files match approved head `74e860184b`. The corrective merge retains 22 supported organelle assertions across seven genes and preserves all 320 affected rows; the full module audit covers thirteen members.
- [x] `aerobic_nicotinate_degradation`: [PR #5544](https://github.com/ai4curation/ai-gene-review/pull/5544) merged as `94a80ada9f7143d2fb1b38b5e97a5301859c0a7c`. Twelve references and twelve member reviews (43 rows) were verified; 64 scoped curated/history files match the approved head. The NicD localization supersession is recorded in the older audit ledger.
- [x] `alcoholic_fermentation`: [PR #5572](https://github.com/ai4curation/ai-gene-review/pull/5572). Merged as `fe302bb372e476d4c1d6911c825e33bb49c23eac` after approval and passing checks. All 6 scoped curation, history and source files match approved head `337db24a4f`. The corrective merge retains both SCHPO adh4 mitochondrial assertions beside matrix assertions and preserves all fifteen affected rows.
- [x] `alginate_o_acetylation`: [PR #5546](https://github.com/ai4curation/ai-gene-review/pull/5546). Merged as `47f648bb3d97f15c19051afb270c527728b17e51` after current-head approval and passing required checks. All 83 scoped curation/history files match approved head `f15f9ec44b`; 12 reviews, 52 rows and 15 references are verified.
- [ ] `alginate_polymerization_export`: [PR #5552](https://github.com/ai4curation/ai-gene-review/pull/5552). Published follow-up 9aa3abc09d adds direct Alg8 catalytic evidence from PMID:16391057 and PMID:18524915, clarifies two inherited ISS donor provenances, and anchors AlgG to PMID:8144447. All 21 reviews, 116 rows and 42 raw sources are preserved; graph, selectors and functions are unchanged. Thirteen route cases pass, with no focused errors and documented existing advisories. The previous approval was dismissed after the new push; current status is REVIEW_REQUIRED with fresh review and CI pending.
- [x] `aliphatic_glucosinolate_myrosinase_defense`: [PR #5550](https://github.com/ai4curation/ai-gene-review/pull/5550) merged as `75d569bf94a697ed142f0f1397736819563b8d74`. All 187 scoped files from the 208-file paginated PR match the approved head; 35 reviews, 453 rows and 31 curated references are verified.
- [x] `androgen_receptor_signaling`: [PR #5554](https://github.com/ai4curation/ai-gene-review/pull/5554). Merged PR #5554 as 70a5964a22d14e7972cfb43fe02095aa4cb8a7c1 at 2026-10-26T15:23:25Z after current-head approval and successful queue checks. All 270 scoped science, source and history blobs match approved head 93ce23a1a7d136ce286372b29b6e3174abc45979. Fifteen reviews and 1,683 original rows are preserved.
- [ ] `anti_crispr_suppression`: [PR #5555](https://github.com/ai4curation/ai-gene-review/pull/5555). Approved head ff70e1f8ff has passing required head checks and is in the normal merge queue, awaiting predecessor/queue checks. Thirteen reviews retain 42 original annotation objects and 26 raw sources. Full follow-up validation passed; seven documented module advisories remain.
- [ ] `apoptotic_execution_phase`: [PR #5558](https://github.com/ai4curation/ai-gene-review/pull/5558). Approved head 752e52b0b0 preserves 16 reviews, 1,608 original rows and 32 raw sources. The scientific review and suite passed; required validation is still running. Full local validation previously passed, and no integration or completion is inferred from an UNKNOWN merge-state field.
- [x] `aps_dependent_assimilatory_sulfate_reduction`: [PR #5560](https://github.com/ai4curation/ai-gene-review/pull/5560). Merged as `6349c3ef3ea2c8604949502686281dde0c0aaa7a` after approval and passing checks. All 226 scoped curation, history and source files match approved head `8553f16ce5`. The audit covers 29 member reviews, 496 rows, 28 curated references and five qualified connections.
- [ ] `arginine_biosynthesis`: [PR #5563](https://github.com/ai4curation/ai-gene-review/pull/5563). Approved head b4971234e3 preserves 43 reviews and 555 rows. Required head checks passed; the normal merge queue is awaiting predecessor/queue checks. The audit remains open until publication and merged-content verification.
- [ ] `arginine_catabolism_arginase_pathway`: [PR #5566](https://github.com/ai4curation/ai-gene-review/pull/5566). Approved head 64aec812fd preserves 18 reviews, 357 original rows and 359 current rows. Required head checks passed. Queue conflict diagnosis finds only CAR1 HTML, CAR1 notes and project HTML conflicting with the synthetic PR5563 predecessor; all 18 review YAMLs and the module survive unchanged. Current published main merges cleanly. Wait for the predecessor to publish before one targeted integration; no speculative rebase was performed.
- [ ] `aspartate_asparagine_metabolism`: [PR #5568](https://github.com/ai4curation/ai-gene-review/pull/5568). Source-note follow-up 2c004eaaf8 makes eleven ALAAT1 reference assessments source-specific, restores the existing targeting finding and synchronizes one ASNS local-note citation. All 548 panel payloads/actions and 54 raw sources remain preserved; the two touched strict checks pass without warnings. Current-head approval at 16:03:29 UTC supersedes the earlier request; fresh validation is running and the suite passed. Full session 3814 previously passed. Exact-head normal auto-merge is enabled; no queue entry is present at this snapshot.
- [ ] `aspartate_family_threonine_biosynthesis`: [PR #5569](https://github.com/ai4curation/ai-gene-review/pull/5569). Follow-up e12e959a11 repairs source-specific support and summaries without changing the 24-member, 439-row panel. Eight focused strict checks pass without warnings. Formal approval at 15:59:35 UTC supersedes the earlier request and historical reviewer quota failure. The suite passed; required validation is running. Full session 56949 previously passed. Exact-head normal auto-merge is enabled; no queue entry is present at this snapshot.
- [x] `autonomous_flowering_pathway`: [PR #5574](https://github.com/ai4curation/ai-gene-review/pull/5574). Merged PR #5574 at 9c626393756af403d2700b57f66374fae6a1331f after approval and passing checks. All 153 branch-scoped files, and the entire committed tree, match approved head b483aad33dd72e8ac687827a21834d161740077e. Fifteen reviews, 304 rows, 34 assessed references and ten connections are preserved.
- [x] `auxin_nuclear_signaling`: [PR #5576](https://github.com/ai4curation/ai-gene-review/pull/5576). Merged PR #5576 as 77121ffa32de060d9b717476356f41f2fabef3e3 at 2026-10-26T14:17:11Z after approval and passing checks. All 133 scoped science/history files match approved head c2b52875f38fa802ce967fbe9541025bc9652976. Fourteen reviews, 633 current rows, 29 references and thirteen connections remain verified.
- [ ] `auxin_polar_transport`: [PR #5579](https://github.com/ai4curation/ai-gene-review/pull/5579). Approved head 78145a0a3e retains the consolidated NRT1.1 review and the 17-member, 484-row panel. All required head checks now pass. Exact-head normal auto-merge is enabled; the current snapshot has no merge-queue entry yet. No admin bypass or merge completion is claimed.
- [ ] `b_cell_receptor_signaling`: [PR #5584](https://github.com/ai4curation/ai-gene-review/pull/5584). Follow-up b930bc41fc clarifies CD79 receptor versus adaptor roles, mouse Syk pathway coverage and the mouse Plcg2 inference boundary. All 22 reviews, 2,645 original rows and 44 raw sources are preserved; no NEW annotation was added. A new current-head review submitted at 16:08:46 UTC requests changes; root is assessing its concrete follow-up requirements. Suite passed; validation is running. Earlier full session 61187 passed.
- [ ] `bacterial_23s_rrna_m5u747_methylation`: [PR #5586](https://github.com/ai4curation/ai-gene-review/pull/5586). Follow-up cb5e106fdb restores precise SAM-dependent tRNA U54 activity and represents the established tmRNA reaction separately, without adding an annotation row. RlmC cofactor wording and module review-source scope are clarified. Five reviews preserve 55 original rows and ten raw sources; 12 route cases pass with unchanged module logic. Formal current-head approval at 15:55:34 UTC supersedes the earlier request; validation is running and suite passed. Full session 59894 previously passed. Normal merge queue entry is AWAITING_CHECKS (position 7 at this snapshot).
- [ ] `bacterial_2_3_butanediol_acetoin_catabolism`: [PR #5588](https://github.com/ai4curation/ai-gene-review/pull/5588). Audit 25 has a committed, independently checked package at 17ec2c0537: 20 complete reviews preserve 83 original rows and 40 raw sources, with three MF contribution proposals yielding 86 rows and no NEW BP. Four native variants contain 15 activities, 15 edges and 11 assessed references with 22 findings. Conditional PedE/PedH entry and unknown native E3 partners remain explicit; SF219 grounding is repaired. All 27 route cases pass. Full validation session 40946 terminated successfully: 9,113 valid reviews, zero blocking errors, 30,064 corpus warnings and 54 passing pathway checks. PR #5588 is now published at the verified head after the terminal full-validation PASS; review and CI remain pending.
- [ ] `bacterial_4_hydroxybutyrate_oxidation`: Audit 26 has a verified clean isolated worktree at base 6391160817, with independent index and successful environment setup. Source-foundation research is underway; no member review or curated edit is complete. Open PR #4748 overlaps the PSEPK gbd/sad-I/sad-II sidecar reviews and is being inspected. The original gbd accession Q88JJ9 is PP_2650, not PP_2049; native H16 evidence and KT2440 transfer limits are under assessment.
- [ ] Remaining 688 modules are NOT_STARTED. Thirteen of 714 current audits are complete; thirteen remain active.

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
