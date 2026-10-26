# thrB annotation-review notes

## 2026-10-26 complete native-function review

All 10 seeded rows reviewed. Raw UniProt/GOA source files and every non-review annotation payload are preserved. No NEW rows were proposed.

PMID:177283 directly purifies native E. coli homoserine kinase and establishes competitive, noncooperative threonine inhibition at the homoserine site. PMID:8973190 characterizes homoserine analogues and separates ATPase from kinase activity through mutagenesis. The curated function explicitly excludes L-serine and L-threonine as kinase substrates. The native reaction uses ATP; neither PLP chemistry nor the phosphoserine donor of Pseudomonas ThrH applies. Existing threonine-biosynthesis genetic rows (PMID:4148765/4364333) agree with the enzymatic step. Cytosolic proteomic assignments are retained without pretending the abstract reconstructs each peptide table. No NEW promiscuous-substrate or ATPase annotation was proposed.

## Retrieval and evidence limits

Normal fetch-gene seeded this review. Actual Falcon/default research and perplexity-lite fallback were attempted concurrently with normal fetch-gene-pmids; both providers failed access/authentication and no report was fabricated. The actual fetch-fitness attempt failed because no FEBA source was reachable; no fitness phenotype or file is claimed. Full provider/publication/fitness logs are in .cache/module-audit-logs/threonine-ECOLI-thrB-*.log. Additional references were normally fetched; transient 429 errors were retried serially. UniProt source quotes are curated reaction/function/family statements, including explicitly identified orthology inferences, never names/EC fields, electronic GO lines or GOA evidence.

Original experimental claims are judged holistically with independently established function; an abstract-only cache or title focused on another enzyme is not by itself evidence against the claim. The current QuickGO term definitions were inspected and saved in the audit log. Authored GO0004073 labels use the validator's ontology spelling while seeded labels remain untouched. Record-section backfill, strict schema/reference/term checks, helper history and HTML rendering accompany the review.


## 2026-10-26 PR #5569 second follow-up

Replaced the shared action-only summaries and catalytic boilerplate with enzyme-specific chemistry and row-specific source assessments. Existing annotation payloads and raw UniProt/GOA files remain unchanged. Distinct experimental, PAINT, domain/rule and homolog-transfer rows now state what each evidence stream establishes. No new biological annotation was proposed.

PMID:177283 directly purifies ThrB and tests homoserine/threonine competition and Mg2+ effects. Competitive inhibition is not recast as cooperative allostery. Genetic operon/mapping studies (PMID:4148765/4364333) are separated from catalytic evidence (PMID:8973190).

All 24 current panel reviews remain within the preservation proof (439 rows, including the pre-existing proposal). Focused schema/term/source checks, derived record sections, renders and helper-generated Codex histories accompany the changed genes. No module, tracker, staging, commit or full-repository validation is part of this follow-up.

## 2026-10-26 — source-specific PR #5569 follow-up

The remaining action-only refinement summaries and generic refinement reasons were replaced with reaction-, pathway- or assembly-specific explanations. Existing actions and replacement terms are unchanged. The cytosol row keyed to PMID:15911532 now quotes that paper’s actual fractionation/2D-gel/MS statement, instead of the different MC4100 study PMID:18304323. The abstract does not name the target hit; the native curator assignment is retained without pretending the original protein table was reinspected.
