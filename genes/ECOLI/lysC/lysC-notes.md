# lysC annotation-review notes

## 2026-10-26 complete native-function review

All 11 seeded rows reviewed. Raw UniProt/GOA source files and every non-review annotation payload are preserved. No NEW rows were proposed.

Native aspartokinase III, not acetylglutamate kinase: PMID:14623187 assays both paralogous amino-acid kinases and specifically states that AKIII phosphorylates aspartate. Its experimental mutagenesis and homodimer result support activity and assembly. PMID:16905770 resolves active R-state and lysine-bound inhibitory T-state, with tetramer formation. Do not infer an invariant dimer or universal threonine feedback from other family members. PMID:4360904 is bibliographic-only in the cache; homodimerization is independently corroborated by14623187, not rejected for lack of its abstract. PMID:6249791 uses lysC-lac transcriptional fusions; it corroborates regulated gene identity, while target chemistry is supported independently. The kinase supplies both lysine/DAP and homoserine branches, so the homoserine rows are valid even though the isozyme is called lysine sensitive.

## Retrieval and evidence limits

Normal fetch-gene seeded this review. Actual Falcon/default research and perplexity-lite fallback were attempted concurrently with normal fetch-gene-pmids; both providers failed access/authentication and no report was fabricated. The actual fetch-fitness attempt failed because no FEBA source was reachable; no fitness phenotype or file is claimed. Full provider/publication/fitness logs are in .cache/module-audit-logs/threonine-ECOLI-lysC-*.log. Additional references were normally fetched; transient 429 errors were retried serially. UniProt source quotes are curated reaction/function/family statements, including explicitly identified orthology inferences, never names/EC fields, electronic GO lines or GOA evidence.

Original experimental claims are judged holistically with independently established function; an abstract-only cache or title focused on another enzyme is not by itself evidence against the claim. The current QuickGO term definitions were inspected and saved in the audit log. Authored GO0004073 labels use the validator's ontology spelling while seeded labels remain untouched. Record-section backfill, strict schema/reference/term checks, helper history and HTML rendering accompany the review.
