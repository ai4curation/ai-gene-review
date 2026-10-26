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
- [ ] `adrenal_steroidogenesis`: [PR #5571](https://github.com/ai4curation/ai-gene-review/pull/5571), head `74e860184b`. Corrective PR #5571 restores 22 supported organelle assertions across seven genes, preserving all 320 original rows and separate subcompartment claims. Full repository validation passed before publication; current review and CI remain pending.
- [x] `aerobic_nicotinate_degradation`: [PR #5544](https://github.com/ai4curation/ai-gene-review/pull/5544) merged as `94a80ada9f7143d2fb1b38b5e97a5301859c0a7c`. Twelve references and twelve member reviews (43 rows) were verified; 64 scoped curated/history files match the approved head. The NicD localization supersession is recorded in the older audit ledger.
- [ ] `alcoholic_fermentation`: [PR #5572](https://github.com/ai4curation/ai-gene-review/pull/5572), head `337db24a4f`. Corrective PR #5572 retains both SCHPO adh4 mitochondrial assertions alongside its matrix claims. All 15 row payloads and module YAML are unchanged. Full repository validation passed before publication; current review and CI remain pending.
- [ ] `alginate_o_acetylation`: [PR #5546](https://github.com/ai4curation/ai-gene-review/pull/5546): 12 reviews, 52 rows and 15 references; full validation and all current CI checks pass. Head `8318b128ea` received scientific approval and is in the merge queue (entry verified live, position 10). Keep the dependent polymerization PR in draft until the merge and scoped content are verified.
- [ ] `alginate_polymerization_export`: [draft PR #5552](https://github.com/ai4curation/ai-gene-review/pull/5552): 18 reviews, 99 rows and 23 references. Head `639f50743b` is approved with all checks passing. Keep draft until shared AlgX work in #5546 merges, then integrate and verify that dependency.
- [x] `aliphatic_glucosinolate_myrosinase_defense`: [PR #5550](https://github.com/ai4curation/ai-gene-review/pull/5550) merged as `75d569bf94a697ed142f0f1397736819563b8d74`. All 187 scoped files from the 208-file paginated PR match the approved head; 35 reviews, 453 rows and 31 curated references are verified.
- [ ] `androgen_receptor_signaling`: [PR #5554](https://github.com/ai4curation/ai-gene-review/pull/5554), head `93ce23a1a7`. All 15 reviews and 1,683 row payloads are preserved. The citation-only follow-up passed focused checks. Current-head automated review terminated with an execution error; one controlled retry was submitted after confirming terminal failure. CI validation is still running.
- [ ] `anti_crispr_suppression`: [PR #5555](https://github.com/ai4curation/ai-gene-review/pull/5555), head `b2bba44f7f`. Thirteen reviews preserve all 42 rows. The latest follow-up removes the unused reproduction landing cache and incorrect unavailable flags on local excerpts; canonical paper access limitations remain explicit. Focused checks and all build CI pass. Current-head scientific review failed before assessment; one controlled retry was submitted.
- [ ] `apoptotic_execution_phase`: [PR #5558](https://github.com/ai4curation/ai-gene-review/pull/5558), head `0a964c9114`. The first follow-up corrected organelle scope and 37 source-traced caspase rows. Re-review identified 20 additional generic mouse uncertainty rows; the expanded CASP3/Casp3 audit is underway. CI also exposed a renamed node referenced by TRAIL: restoring the established executioner_caspase_proteolysis ID passes a 714-module current-main compatibility check and preserves the CASP3/CASP7 requirement. These additional fixes are not yet published.
- [ ] `aps_dependent_assimilatory_sulfate_reduction`: [PR #5560](https://github.com/ai4curation/ai-gene-review/pull/5560), head `f94190a1bb`. All 29 reviews and 496 rows remain intact. The canonical citation/target-legend follow-up received current-head approval; validation and suite CI pass, with the aggregate test job still pending.
- [ ] `arginine_biosynthesis`: [PR #5563](https://github.com/ai4curation/ai-gene-review/pull/5563), head `bf58a08050`. Forty-three member reviews preserve 555 rows, with companion CAR1 harmonized. The residual SCHPO arg3 mitochondrial propagation assessment now agrees with ACCEPT, without changing row payloads or the four valid cytoplasm refinements. Focused checks pass. Current-head review terminated with an execution error; one controlled retry was submitted.
- [ ] `arginine_catabolism_arginase_pathway`: [PR #5566](https://github.com/ai4curation/ai-gene-review/pull/5566), head `b49ce26701`. Eighteen reviews preserve 357 original rows, with 359 final rows including separately supported plant matrix claims. Current-head scientific approval and all required CI checks pass. Submitted to the merge queue and verified QUEUED (entry MQE_lQDOPk5H7c8AAAABKsTlnc4ABJzTzgN8x8k); not yet merged.
- [ ] `aspartate_asparagine_metabolism`: [PR #5568](https://github.com/ai4curation/ai-gene-review/pull/5568), head `aea3abd270`. Twenty-seven reviews preserve 548 rows, spanning 25 eukaryotic exemplars and two bacterial comparators. Full local validation and all build CI pass. Automated scientific review failed before assessment; one controlled retry was submitted.
- [ ] `aspartate_family_threonine_biosynthesis`: [PR #5569](https://github.com/ai4curation/ai-gene-review/pull/5569), head `8a4da618f6`. The 24-member, 439-row audit passed full validation before publication. Scientific review requested enzyme/cofactor specificity, cross-gene consistency, source support and prose repairs. These are being checked against live GO definitions and primary evidence; the NAD versus NADP distinction requires an evidence-based response rather than automatic term substitution.
- [ ] `autonomous_flowering_pathway`: Local audit. All 15 member reviews are complete: 13 native Arabidopsis proteins and two accession-resolved rice comparators. All 302 pre-existing row payloads are preserved; one supported SDG26 DNA-binding proposal gives 303 final rows. Focused schema/term/source checks pass, with documented nonblocking output-panel advisories. The module now has 13 native activities with verified classification descriptors, 10 evidence-backed edges and context-qualified regulatory contributions. Native FLC wiring is not generalized to rice. Module integration, 12 route cases and 46 logic tests pass; full repository validation is running.
- [ ] Remaining 683 baseline modules: recorded as NOT_STARTED. Six of 702 baseline audits are complete; thirteen audits are active, including two reopened after retrospective QA. Refresh upstream additions before final completion.

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
