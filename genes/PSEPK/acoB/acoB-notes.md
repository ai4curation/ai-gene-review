# acoB curation notes

- Identity: Q88QE0 / PP_0554. The current UniProt RecName is an automated 2-oxoisovalerate-dehydrogenase assignment, but the submitted gene name, locus, primary literature, and acetoin-specific `PTHR43257:SF3` placement support AcoB.
- Verified exemplar: Cupriavidus necator AcoB P27746, reviewed and protein-level, in the same PANTHER subfamily.
- QuickGO returned no GOA rows for Q88QE0; the two `NEW` rows are conservative complex-level acetoin assignments.
- No completed gene-level OpenScientist artifact was present for acoB. Research was not restarted.


## 2026-10-26 source-specific annotation audit

The inherited E1 contribution and acetoin-process proposals are retained, with source-specific inference. H16 PMID:2061286 supports an alpha/beta E1 with alpha2-beta2 judged most likely; it does not directly measure KT2440 stoichiometry. Full PMID:42046433 tests native PP0554 acoB::mini-Tn5 growth on acetoin and butanediol, but explicitly warns of effects on acoC/adh and possibly acoA/acoX transcription. This is genuine native locus evidence, not a clean nonpolar AcoB-only necessity experiment. Subsequent Klebsiella budABC expression in the same study establishes engineered production, not biosynthetic functions for native AcoB.

Acquisition and preservation: the complete original review payloads and raw UniProt/GOA hashes were captured before editing in the audit baseline. All rows, including inherited proposals and retirement flags, are preserved. Actual Falcon and perplexity-lite fallback attempts failed; no provider report was fabricated. Normal gene-publication acquisition succeeded, and actual FEBA/fitness attempts failed without generating usable data. Logs are in `.cache/module-audit-logs/acetoin-pseudomonas-fetch/`; this manual research note records the independent review. PMID:7813883 remains abstract-only after normal force, publisher-page and PDF recovery attempts; the publisher minimal page adds references but not full text. Full PMID:34513815/36482024/42046433 were read where relevant. Existing provider artifacts are discovery aids, not substitutes for source verification. The annotation-reviewer consultation agreed with separating component activity from isolated-subunit catalysis, native catabolism from engineering, and condition-limited negative assays from universal absence.
