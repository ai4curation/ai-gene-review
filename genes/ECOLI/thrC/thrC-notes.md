# thrC annotation-review notes

## 2026-10-26 complete native-function review

All 9 seeded rows reviewed. Raw UniProt/GOA source files and every non-review annotation payload are preserved. No NEW rows were proposed.

PMID:6316258 establishes the thrC coding sequence and matches the synthase N terminus. The independently curated target biochemical study PMID:7907888 supports PLP chemistry, phosphohomoserine turnover and side reactions; its abstract reports serine deamination at much lower efficiency than the primary biosynthetic reaction. Those side reactions were not turned into unsupported NEW physiological catabolism processes. The existing biosynthesis genetic rows are retained (PMID:4148765/4364333). Integrate PLP binding with the synthase core, and retain cytosolic localization from independent proteomic curation. Plant SAM activation should not be generalized to this bacterial enzyme.

## Retrieval and evidence limits

Normal fetch-gene seeded this review. Actual Falcon/default research and perplexity-lite fallback were attempted concurrently with normal fetch-gene-pmids; both providers failed access/authentication and no report was fabricated. The actual fetch-fitness attempt failed because no FEBA source was reachable; no fitness phenotype or file is claimed. Full provider/publication/fitness logs are in .cache/module-audit-logs/threonine-ECOLI-thrC-*.log. Additional references were normally fetched; transient 429 errors were retried serially. UniProt source quotes are curated reaction/function/family statements, including explicitly identified orthology inferences, never names/EC fields, electronic GO lines or GOA evidence.

Original experimental claims are judged holistically with independently established function; an abstract-only cache or title focused on another enzyme is not by itself evidence against the claim. The current QuickGO term definitions were inspected and saved in the audit log. Authored GO0004073 labels use the validator's ontology spelling while seeded labels remain untouched. Record-section backfill, strict schema/reference/term checks, helper history and HTML rendering accompany the review.


## 2026-10-26 PR #5569 second follow-up

Replaced the shared action-only summaries and catalytic boilerplate with enzyme-specific chemistry and row-specific source assessments. Existing annotation payloads and raw UniProt/GOA files remain unchanged. Distinct experimental, PAINT, domain/rule and homolog-transfer rows now state what each evidence stream establishes. No new biological annotation was proposed.

PMID:6316258 links the thrC sequence to purified threonine synthase by N-terminal sequencing. PLP-dependent gamma-elimination of phosphate followed by beta-addition of water is supported by the curated target mechanism; it is not invented as a new result of the sequence paper. Genetic complementation and pathway chemistry are distinguished.

All 24 current panel reviews remain within the preservation proof (439 rows, including the pre-existing proposal). Focused schema/term/source checks, derived record sections, renders and helper-generated Codex histories accompany the changed genes. No module, tracker, staging, commit or full-repository validation is part of this follow-up.

## 2026-10-26 — source-specific PR #5569 follow-up

The remaining action-only refinement summaries and generic refinement reasons were replaced with reaction-, pathway- or assembly-specific explanations. Existing actions and replacement terms are unchanged. The cytosol row keyed to PMID:15911532 now quotes that paper’s actual fractionation/2D-gel/MS statement, instead of the different MC4100 study PMID:18304323. The abstract does not name the target hit; the native curator assignment is retained without pretending the original protein table was reinspected.


## 2026-11-01 bacterial aspartate-to-threonine audit follow-up

Re-read the existing COMPLETE review and every annotation decision for the narrower bacterial route audit. Retained all annotation actions, machine-sourced payloads, standalone description, core functions and raw records. Added manual assessments and verbatim findings to existing references, distinguishing native experiments from comparative synthesis, bibliographic-only records and inference. No new annotation rows were proposed.

ThrC is the native PLP-dependent final step, converting phosphohomoserine to threonine with phosphate release. PMID:6316258 supplies sequence-to-enzyme identity, not all mechanistic chemistry. PMID:7907888 directly reports phosphohomoserine turnover (Km 0.5 mM; V 440 min−1) and much weaker serine beta-elimination (Km 150 mM; V 4.7 min−1) under its assay conditions.

These side reactions remain assay observations, without a physiological serine/threonine catabolic route or NEW side-activity annotation. PLP binding is integral to the retained synthase core. Plant regulatory properties, including SAM activation, are not transferred to the native E. coli enzyme.

Acquisition and evidence limits: `just mod-description-deep-research ECOLI thrA metL lysC asd thrB thrC` completed with all six skipped because no MOD provider is configured for ECOLI. A fresh normal Falcon request for ECOLI thrA failed with the shared Edison authentication/access 403; the same failed service was not retried for the other five. Earlier actual provider attempts remain documented above. No provider report was fabricated or rewritten. Manual review used existing primary-publication and curated UniProt caches. Logs are in the ignored `.cache/module-audit-logs/bacterial-threonine-ecoli/` directory.

PMID:11368768 supports the native route, but its nominal full-text HTML cache contains a duplicated abstract and PDF link rather than the full paper. The coordinating agent's normal PDF retrieval also returned an HTML interstitial. No unseen kinetic measurements or exact strain details are attributed to that abstract. Native proteomics annotations retain the caveat that individual target supplement rows were not independently reconstructed. Raw UniProt PANTHER membership and the official `interpro/panther/panther.obo` label were checked for module selectors; membership alone does not establish every family's substrate or regulatory specificity.
