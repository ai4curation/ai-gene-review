# Historical project journal for PR #6150

These are the branch-only paragraphs from `projects/MODULE_TAXON_AUDIT.md` at `42622f83458631264d122106c09b91c7a8f90263`, preserved verbatim in source order. Dates, counts and validation claims describe their original snapshots. Current readiness is determined by GitHub review and CI. The shared project page and rendered HTML now follow incoming main `70e3fa209b3741446dd23cb676cd6a9774398531` exactly; this prevents unrelated audits from repeatedly conflicting on one shared append-only page.

- [ ] `bacterial_fused_puta_proline_catabolism`: PR #6150: main 0ca78c07ea integrated at dba12f6a23; 190 branch-specific files were verified unchanged at that integration. Subsequent review fixes are separately recorded. Fresh current-head review and CI govern merge readiness; historical full-corpus results retain their recorded scope.

- [x] `bacterial_fatty_acid_beta_oxidation`: [PR #6136](https://github.com/ai4curation/ai-gene-review/pull/6136) merged as `20043f67a6ed802902f84a968aa57c88a8ca3a8f` on 2026-11-06T22:09:45Z. All 294 scoped files match the approved head. [Merged-content proof](MODULE_TAXON_AUDIT/proofs/pr6136-merged-content.json).

- [ ] Ledger snapshot after this integration: 784 modules; 44 COMPLETE, 9 PR_OPEN, 1 IN_PROGRESS, 730 NOT_STARTED. Counts retain dated row evidence and are not a fresh global GitHub survey.

## 2026-11-06 — fused PutA comparative audit started

Begin the comparative fused-PutA audit from published main 5f8f3b5c5e. Preserve the five existing gene reviews with 143 annotation rows and 16 raw/provider files. The existing module has three gamma-proteobacterial PutA exemplars, all with regulatory RHH domains. Check the catalytic architecture against non-regulatory type A and B proteins, including directly studied Bradyrhizobium, Geobacter, Sinorhizobium and Corynebacterium proteins. Verify exact experimental strains and sequences before assigning accessions; do not generalize sodium-coupled uptake from a catalytic PutA exemplar alone. Search comparative reviews and primary studies, reassess family selection and taxon scope, complete gene consultation, validate and open one dedicated PR; actual merge remains required.

## 2026-11-06 — beta-oxidation merge verified

PR #6136 actually merged as 20043f67a6ed802902f84a968aa57c88a8ca3a8f at 2026-11-06T22:09:45Z. Independently compared Git object IDs for all 294 scoped scientific, source and audit files against approved head 8855038e451a9da8d72a499dc27db9e39598ea80; every blob is identical. Record the beta-oxidation audit as COMPLETE with a linked proof. The recorded full validation remains passing with its disclosed corpus advisories. Shared project metadata is excluded from the 294-file comparison and is updated here; unrelated inventory rows remain unchanged.

## 2026-11-06 — fused PutA cross-lineage integration

Completed eleven individual reviews while preserving 198 original/seed annotation payloads, order, the one historical NEW action, and 28 raw/provider files. Eight PutA exemplars now span the five characterized architecture/phylogeny classes and a Helicobacter comparison; three PutP exemplars include G27 as explicitly comparative inference. P12 transporter and J99 enzyme experiments are not G27 assays. Corynebacterium structural constructs do not establish native transport or membrane localization.

Curated sixteen references with 31 mined findings, including both comparative reviews (PMID:28712849; PMID:28990412) and the newly fetched 2025 SmPutA primary study (PMID:40738191). Individual catalytic, transport, and intermediate-handoff steps carry source evidence. The 2025 study names F7X6I3 and distinguishes crystallographic intermediates from simulation-based channeling.

Replace the narrow TIGR01238 GSALDH selector with full fused-PutA family IPR025703 plus the independently supported activity and same-polypeptide architecture. Current Geobacter, Corynebacterium and G27 records have IPR025703 but lack TIGR01238. Negative controls retain monofunctional RocA/PUT2 and non-proline PanF/ActP exclusions. Broaden quinone substrate identity from benzoquinones to CHEBI:36141; the reduced product remains a free-text descriptor rather than a guessed ontology identifier. Native quinone identity remains unresolved.

Bacterial scope is retained because the characterized catalytic architecture spans Pseudomonadota, Thermodesulfobacteriota, Campylobacterota and Actinomycetota. This is not a claim of universal bacterial distribution or a complete transport pathway in every enzyme source organism. The production-circuit checker separately enforces reviewed activity, fusion, and matched-strain evidence: 44 checks and six deliberate mechanism mutations. These rules do not turn a compiler family hit into proof of native flux. Full validation, publication and actual merge remain pending.

## 2026-11-06 — PutA full validation complete

PutA full validation passed on 5d01f7ba96fea3f93ec5a0fd61cfdcf212ef2a9b across 10701 reviews, with all 195 frozen inputs unchanged. Schema, term, reference and best-practice stages have no blocking errors; all 54 pathway-reference checks pass. There are 120 term-label advisories, 53 reference advisories and 27771 best-practice warnings. The eight panel term-label advisories match the current QuickGO GO:0003842 label; the validator cache has the earlier label. The eleven-member panel preserves 198 original/seed annotation payloads, its one historical NEW row and 28 raw/provider files. Sixteen curated references, including two comparative reviews, support the three steps. All 44 capacity checks and six mechanism mutations pass; module semantic validation has zero warnings. These checks do not establish native matched-system flux for component-only or inferred exemplars. Main integration, a dedicated PR, independent review, CI and actual merge remain required.

## 2026-11-06 — PutA audit integration with published main d2e41f09fb

Integrated published main `d2e41f09fb` with the validated PutA audit head `5f9ddc95a4`. All 196 scoped files outside the shared tracker and rendered index remain byte-identical, including curated science and source evidence. The 777-row inventory retains every incoming row except this module's validated row and the independently verified beta-oxidation completion row. All dated journals are preserved. Validation implementation is unchanged. The full run covered 10701 reviews and all 195 frozen inputs were verified unchanged before closeout; full-validation.json records its complete outcome and advisories. A dedicated PR, independent review and fresh CI still gate actual merge.

Integration proof: [validated-head-integration.json](../analysis/module_audits/bacterial_fused_puta_proline_catabolism/validated-head-integration.json).

## 2026-11-06 — module universe refresh to 784

The module universe was checked against published main d2e41f09fbe335e611d3bfe0b5d0dff01d5a8ea4 and the integrated checkout. Seven previously untracked modules bring inventory coverage from 777 to 784. Every existing row is preserved. All seven additions are NOT_STARTED: structural triage, source citations and declared status do not establish completed literature, taxon, exemplar, member-review or merged-PR audits. Their PR overlaps remain unchecked.

`bacterial_iad_auxin_catabolism`, `bombesin_receptor_signaling`, `endoplasmic_reticulum_lifecycle`, `er_cotranslational_translocation`, `er_oxidative_protein_folding`, `tsh_signaling`, `variovorax_metallophore_metal_homeostasis`.

Universe proof: [module-universe-20261106-d2e41f09.json](MODULE_TAXON_AUDIT/proofs/module-universe-20261106-d2e41f09.json).

## 2026-11-06 — PutA PR #6150 published

Opened PR #6150 after PutA full validation passed on 5d01f7ba96fea3f93ec5a0fd61cfdcf212ef2a9b across 10701 reviews with zero blocking errors. Published main d2e41f09fb was integrated with all 196 scoped files outside the shared tracker preserved, and the module universe was refreshed to 784 entries with seven unaudited additions. All eleven member reviews, 198 source annotation payloads, one historical NEW row and 28 raw/provider files remain preserved. The beta-oxidation actual-merge proof and completion row are retained. Independent review, fresh CI and actual merge remain pending.

## 2026-11-07 — PutA biological review follow-up

Addressed the changes-requested review on b4a3149: harmonized non-RHH transcription mapping rejection, left unsupported PSEPK membrane-face localization UNDECIDED, clarified inferred sodium binding, and aligned the existing yeast PUT2 glutamate-formation decision. The audit now includes eleven module-member reviews and one yeast comparator. All 221 original annotation payloads retain their order, with no added or retired rows. The explicit ledger documents sixteen earlier action reversals. The checker records retained, replacement and core claims with row provenance; its 44 cases, six mechanism mutations and ten extraction controls measure curation consistency, not independent assay confirmation. Six gene validations, renders and histories pass; family attribution retains claude-code and codex. The prior full pass remains historical evidence for its recorded head. Renewed full validation, publication, review, CI and actual merge are pending.

## 2026-11-07 — PutA review follow-up full validation passes

PR #6150 follow-up passes full validation on 6cd2f11830: 10,720 reviews, zero blocking errors and 226 frozen inputs verified. Publication, fresh review/CI and actual merge remain pending. [Recorded proof](../analysis/module_audits/bacterial_fused_puta_proline_catabolism/round1-full-validation.json).

## 2026-11-07 — bacterial_fused_puta_proline_catabolism main integration

Integrated main e9d31cced895d2d74c464d57cbd40381e15520ab after the passing full run on 6cd2f11830bdc7fc12b608f757934c1ba75d028f. All 222 frozen files outside shared project metadata remain byte-identical. Incoming inventory rows are retained except this audit row and 1 independently reverified merged-completion rows; 7 missing historical rows are retained from this branch, and no completed audit regresses. This is preserved-science integration, not a new full-corpus run. Fresh review, CI and actual merge remain pending.

## 2026-11-07 — bacterial_fused_puta_proline_catabolism main integration

Integrated main 2f72fda87ec460ef99562726f68795f2a2d9552f into approved head bd62f935e042cd9c68b9ba8c62eecba06037a6b7. All 237 frozen files outside shared project metadata remain byte-identical. Incoming inventory rows are retained except this audit row and 1 independently reverified merged-completion rows; 7 missing historical rows are retained from this branch, and no completed audit regresses. Historical full-validation results remain scoped to their recorded heads; this integration is not a new full-corpus run. Fresh review, CI and actual merge remain pending.

## 2026-11-07 — bacterial fused puta proline catabolism full validation passes

PR #6150 follow-up passes full validation on c7dd5c910d: 10,753 reviews, zero blocking errors and 252 frozen inputs verified. Publication, fresh review/CI and actual merge remain pending. [Recorded proof](../analysis/module_audits/bacterial_fused_puta_proline_catabolism/round3-full-run.json).

## 2026-11-07 — bacterial_fused_puta_proline_catabolism main integration

Integrated main 5b68ef3aaca8960576ae1ad557815fe675f1e8a6 after the passing full run on c7dd5c910df6a03cca652fedfd7b2a4c4d6a5fb2. All 248 frozen files outside shared project metadata remain byte-identical. Incoming inventory rows are retained except this audit row and 1 independently reverified merged-completion rows; 7 missing historical rows are retained from this branch, and no completed audit regresses. This is preserved-science integration, not a new full-corpus run. Fresh review, CI and actual merge remain pending.

## 2026-11-07 — bacterial_fused_puta_proline_catabolism main integration

Integrated main e9d50a8a42ab5e6b5560d09ff8c44e64f4c77360 into approved head e8c2bb40293e3c7bc36e163e16f99b20aae3e7b8. All 254 frozen files outside shared project metadata remain byte-identical. Incoming inventory rows are retained except this audit row and 1 independently reverified merged-completion rows; 7 missing historical rows are retained from this branch, and no completed audit regresses. Historical full-validation results remain scoped to their recorded heads; this integration is not a new full-corpus run. Fresh review, CI and actual merge remain pending.

## 2026-11-07 — bacterial_fused_puta_proline_catabolism main integration

Integrated main 0a807fc55576d0371b2dfacb482f8d695992535b into approved head 3b1282f50206a2e4e3bf9f13bf906c8a154bfc0d. All 256 frozen files outside shared project metadata remain byte-identical. Incoming inventory rows are retained except this audit row and 1 independently reverified merged-completion rows; 7 missing historical rows are retained from this branch, and no completed audit regresses. Historical full-validation results remain scoped to their recorded heads; this integration is not a new full-corpus run. Fresh review, CI and actual merge remain pending.

## 2026-11-08 — resume PR #6150 after disk cleanup

Integrate main a344758bae648a999bbe316e9b1e2289a958d1bc into paused PR #6150 at 17b275545cf62c5d335a7629568b7b54a26c12f9. All 180 branch-specific files outside shared project metadata retain their exact Git object ids. Conflicting project status entries and dated journal sections are retained from both parents. Prior validation/review results remain scoped to their recorded commits; this merge requires fresh CI and review.

## 2026-11-08 — resume PR #6150 after disk cleanup

Integrate main ec787ac8700cacbf94a72abbbbe9dee9b622592b into paused PR #6150 at c12f8d59e14f80c21181a327b1593cc713f35a56. All 181 branch-specific files outside shared project metadata retain their exact Git object ids. Conflicting project status entries and dated journal sections are retained from both parents. Prior validation/review results remain scoped to their recorded commits; this merge requires fresh CI and review.

## 2026-11-08 — reconcile resumed PR #6150 tracker

PR #6150: main ec787ac870 integrated at 4601a77cb9; 181 branch-specific files retain their exact pre-integration Git blob ids. Current review and CI govern merge readiness; earlier full-corpus results remain scoped to their recorded commits. Per-path identity proof: [analysis/module_audits/bacterial_fused_puta_proline_catabolism/resume-round2-20261108/integration-proof.json](../analysis/module_audits/bacterial_fused_puta_proline_catabolism/resume-round2-20261108/integration-proof.json). Current counts above are computed from this branch’s inventory; prior dated journal entries remain historical.

> - [ ] Ledger snapshot after this integration: 784 modules; 35 COMPLETE, 9 PR_OPEN, 3 IN_PROGRESS, 737 NOT_STARTED. Counts retain dated row evidence and are not a fresh global GitHub survey.

## 2026-11-10 — resume PR #6150 after disk cleanup

Integrate main 65bf77f9587b5f1614ed1a0434f015e9560b2516 into paused PR #6150 at 37292b6913e57560573fcc8d099e090b8631ed42. All 184 branch-specific files outside shared project metadata retain their exact Git object ids. Conflicting project status entries and dated journal sections are retained from both parents. Prior validation/review results remain scoped to their recorded commits; this merge requires fresh CI and review.

## 2026-11-10 — reconcile resumed PR #6150 tracker

PR #6150: main 65bf77f958 integrated at db8e33edc7; 184 branch-specific files retain their exact pre-integration Git blob ids. Current review and CI govern merge readiness; earlier full-corpus results remain scoped to their recorded commits. Per-path identity proof: [analysis/module_audits/bacterial_fused_puta_proline_catabolism/resume-round3-20261110/integration-proof.json](../analysis/module_audits/bacterial_fused_puta_proline_catabolism/resume-round3-20261110/integration-proof.json). Current counts above are computed from this branch’s inventory; prior dated journal entries remain historical.

> - [ ] Ledger snapshot after this integration: 784 modules; 38 COMPLETE, 11 PR_OPEN, 3 IN_PROGRESS, 732 NOT_STARTED. Counts retain dated row evidence and are not a fresh global GitHub survey.

## 2026-11-11 — resume PR #6150 after disk cleanup

Integrate main ac30fe31cf1a3155a6d56808212969efb09ddb00 into paused PR #6150 at dde9ae35cff65c4b3be9bcef7a75f272c9736552. All 187 branch-specific files outside shared project metadata retain their exact Git object ids. Conflicting project status entries and dated journal sections are retained from both parents. Prior validation/review results remain scoped to their recorded commits; this merge requires fresh CI and review.

## 2026-11-11 — reconcile resumed PR #6150 tracker

PR #6150: main ac30fe31cf integrated at 70ccbceabc; 187 branch-specific files retain their exact pre-integration Git blob ids. Current review and CI govern merge readiness; earlier full-corpus results remain scoped to their recorded commits. Per-path identity proof: [analysis/module_audits/bacterial_fused_puta_proline_catabolism/resume-round4-20261111/integration-proof.json](../analysis/module_audits/bacterial_fused_puta_proline_catabolism/resume-round4-20261111/integration-proof.json). Current counts above are computed from this branch’s inventory; prior dated journal entries remain historical.

> - [ ] Ledger snapshot after this integration: 784 modules; 43 COMPLETE, 9 PR_OPEN, 1 IN_PROGRESS, 731 NOT_STARTED. Counts retain dated row evidence and are not a fresh global GitHub survey.

## 2026-11-11 — resume PR #6150 after disk cleanup

Integrate main 0ca78c07ea0a7ee0ce4760193cc5b22848471d21 into paused PR #6150 at 5becc59fc9f072a1d665b3b1c246f3762f511881. All 190 branch-specific files outside shared project metadata retain their exact Git object ids. Conflicting project status entries and dated journal sections are retained from both parents. Prior validation/review results remain scoped to their recorded commits; this merge requires fresh CI and review.

## 2026-11-11 — current integration accounting for PR #6150

PR #6150: main 0ca78c07ea integrated at dba12f6a23; 190 branch-specific files were verified unchanged at that integration. Subsequent review fixes are separately recorded. Fresh current-head review and CI govern merge readiness; historical full-corpus results retain their recorded scope. [Preservation and follow-up record](../analysis/module_audits/bacterial_fused_puta_proline_catabolism/resume-round5-20261111/integration-proof.json).

## 2026-11-11 — reconcile inherited ledger snapshots for PR #6150

> - [ ] Ledger snapshot after this integration: 784 modules; 43 COMPLETE, 9 PR_OPEN, 1 IN_PROGRESS, 731 NOT_STARTED. Counts retain dated row evidence and are not a fresh global GitHub survey.
