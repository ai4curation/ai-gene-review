# thrB annotation-review notes

## 2026-10-26 complete native-function review

All 5 seeded rows reviewed. Raw UniProt/GOA source files and every non-review annotation payload are preserved. No NEW rows were proposed.

Current UniProt Q58504 names thrB, ordered locus MJ1104. PMID:11188689 establishes its ADP-bound GHMP structure; PMID:11535056 resolves ternary homoserine/ATP-analogue complexes and magnesium coordination. PMID:11114929 directly compares separately purified archaeal homoserine kinase and shikimate kinase: no overlapping activity detected, with greater than 1000-fold specificity for their own substrates. The shikimate-focused title therefore must not be used to dismiss the actual homoserine-kinase data. Do not generalize the shared GHMP superfamily to a shared substrate. The cytoplasm assertion is retained at its curated inference precision; no experimentally resolved subcellular location is claimed. These sources establish this one native enzyme, not completeness of the full archaeal threonine pathway.

## Retrieval and evidence limits

Normal fetch-gene seeded this review. Actual Falcon/default research and perplexity-lite fallback were attempted concurrently with normal fetch-gene-pmids; both providers failed access/authentication and no report was fabricated. The actual fetch-fitness attempt failed because no FEBA source was reachable; no fitness phenotype or file is claimed. Full provider/publication/fitness logs are in .cache/module-audit-logs/threonine-METJA-thrB-*.log. Additional references were normally fetched; transient 429 errors were retried serially. UniProt source quotes are curated reaction/function/family statements, including explicitly identified orthology inferences, never names/EC fields, electronic GO lines or GOA evidence.

Original experimental claims are judged holistically with independently established function; an abstract-only cache or title focused on another enzyme is not by itself evidence against the claim. The current QuickGO term definitions were inspected and saved in the audit log. Authored GO0004073 labels use the validator's ontology spelling while seeded labels remain untouched. Record-section backfill, strict schema/reference/term checks, helper history and HTML rendering accompany the review.


## 2026-10-26 PR #5569 second follow-up

Replaced the shared action-only summaries and catalytic boilerplate with enzyme-specific chemistry and row-specific source assessments. Existing annotation payloads and raw UniProt/GOA files remain unchanged. Distinct experimental, PAINT, domain/rule and homolog-transfer rows now state what each evidence stream establishes. No new biological annotation was proposed.

PMID:11114929 compares archaeal homoserine and shikimate kinases directly and finds more than 1000-fold substrate preference. PMID:11535056 locates homoserine, ATP analogues and a magnesium-associated nucleotide geometry in the target structure. These establish substrate-specific kinase chemistry; the curated cytoplasmic assignment is kept separate from heterologous enzyme crystallization.

All 24 current panel reviews remain within the preservation proof (439 rows, including the pre-existing proposal). Focused schema/term/source checks, derived record sections, renders and helper-generated Codex histories accompany the changed genes. No module, tracker, staging, commit or full-repository validation is part of this follow-up.

## 2026-10-26 — source-specific PR #5569 follow-up

The remaining action-only refinement summaries and generic refinement reasons were replaced with reaction-, pathway- or assembly-specific explanations. Existing actions and replacement terms are unchanged.
