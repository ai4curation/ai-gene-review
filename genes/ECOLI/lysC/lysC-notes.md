# lysC annotation-review notes

## 2026-10-26 complete native-function review

All 11 seeded rows reviewed. Raw UniProt/GOA source files and every non-review annotation payload are preserved. No NEW rows were proposed.

Native aspartokinase III, not acetylglutamate kinase: PMID:14623187 assays both paralogous amino-acid kinases and specifically states that AKIII phosphorylates aspartate. Its experimental mutagenesis and homodimer result support activity and assembly. PMID:16905770 resolves active R-state and lysine-bound inhibitory T-state, with tetramer formation. Do not infer an invariant dimer or universal threonine feedback from other family members. PMID:4360904 is bibliographic-only in the cache; homodimerization is independently corroborated by PMID:14623187, not rejected for lack of its abstract. PMID:6249791 uses lysC-lac transcriptional fusions; it corroborates regulated gene identity, while target chemistry is supported independently. The kinase supplies both lysine/DAP and homoserine branches, so the homoserine rows are valid even though the isozyme is called lysine sensitive.

## Retrieval and evidence limits

Normal fetch-gene seeded this review. Actual Falcon/default research and perplexity-lite fallback were attempted concurrently with normal fetch-gene-pmids; both providers failed access/authentication and no report was fabricated. The actual fetch-fitness attempt failed because no FEBA source was reachable; no fitness phenotype or file is claimed. Full provider/publication/fitness logs are in .cache/module-audit-logs/threonine-ECOLI-lysC-*.log. Additional references were normally fetched; transient 429 errors were retried serially. UniProt source quotes are curated reaction/function/family statements, including explicitly identified orthology inferences, never names/EC fields, electronic GO lines or GOA evidence.

Original experimental claims are judged holistically with independently established function; an abstract-only cache or title focused on another enzyme is not by itself evidence against the claim. The current QuickGO term definitions were inspected and saved in the audit log. Authored GO0004073 labels use the validator's ontology spelling while seeded labels remain untouched. Record-section backfill, strict schema/reference/term checks, helper history and HTML rendering accompany the review.


## 2026-10-26 PR #5569 second follow-up

Replaced the shared action-only summaries and catalytic boilerplate with enzyme-specific chemistry and row-specific source assessments. Existing annotation payloads and raw UniProt/GOA files remain unchanged. Distinct experimental, PAINT, domain/rule and homolog-transfer rows now state what each evidence stream establishes. No new biological annotation was proposed.

PMID:14623187 directly probes AKIII catalytic/substrate-binding residues; PMID:6249791 studies lysC–lac regulation rather than being relabeled as purified-enzyme kinetics. Independent direct target catalysis supports the legacy kinase claim. Active dimer and lysine-inhibited tetramer contexts remain distinct (PMID:16905770).

All 24 current panel reviews remain within the preservation proof (439 rows, including the pre-existing proposal). Focused schema/term/source checks, derived record sections, renders and helper-generated Codex histories accompany the changed genes. No module, tracker, staging, commit or full-repository validation is part of this follow-up.

## 2026-10-26 — source-specific PR #5569 follow-up

The remaining action-only refinement summaries and generic refinement reasons were replaced with reaction-, pathway- or assembly-specific explanations. Existing actions and replacement terms are unchanged.


## 2026-11-01 bacterial aspartate-to-threonine audit follow-up

Re-read the existing COMPLETE review and every annotation decision for the narrower bacterial route audit. Retained all annotation actions, machine-sourced payloads, standalone description, core functions and raw records. Added manual assessments and verbatim findings to existing references, distinguishing native experiments from comparative synthesis, bibliographic-only records and inference. No new annotation rows were proposed.

LysC is the native monofunctional AKIII alternative at the shared aspartyl-phosphate supply step. Lysine-responsive regulation does not make the product exclusive to lysine biosynthesis; homoserine-derived synthesis can use the common precursor. PMID:14623187 separately tests AKIII and N-acetylglutamate kinase and states: "AKIII is homodimeric and is inhibited by lysine." AKIII findings are not conflated with parallel NAGK experiments.

PMID:16905770 distinguishes active R-state assembly from lysine-promoted inactive T-state tetramer formation. PMID:6249791 supports regulation of lysC expression using lysC-lac fusions, not purified kinase kinetics. PMID:4360904 is bibliographic-only, but independent direct assembly evidence is available. Existing homoserine and lysine process annotations already convey shared precursor participation; no mechanically mirrored NEW row is needed.

Acquisition and evidence limits: `just mod-description-deep-research ECOLI thrA metL lysC asd thrB thrC` completed with all six skipped because no MOD provider is configured for ECOLI. A fresh normal Falcon request for ECOLI thrA failed with the shared Edison authentication/access 403; the same failed service was not retried for the other five. Earlier actual provider attempts remain documented above. No provider report was fabricated or rewritten. Manual review used existing primary-publication and curated UniProt caches. Logs are in the ignored `.cache/module-audit-logs/bacterial-threonine-ecoli/` directory.

PMID:11368768 supports the native route, but its nominal full-text HTML cache contains a duplicated abstract and PDF link rather than the full paper. The coordinating agent's normal PDF retrieval also returned an HTML interstitial. No unseen kinetic measurements or exact strain details are attributed to that abstract. Native proteomics annotations retain the caveat that individual target supplement rows were not independently reconstructed. Raw UniProt PANTHER membership and the official `interpro/panther/panther.obo` label were checked for module selectors; membership alone does not establish every family's substrate or regulatory specificity.
