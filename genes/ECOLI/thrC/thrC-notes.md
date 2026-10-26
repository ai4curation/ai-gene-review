# thrC annotation-review notes

## 2026-10-26 complete native-function review

All 9 seeded rows reviewed. Raw UniProt/GOA source files and every non-review annotation payload are preserved. No NEW rows were proposed.

PMID:6316258 establishes the thrC coding sequence and matches the synthase N terminus. The independently curated target biochemical study PMID:7907888 supports PLP chemistry, phosphohomoserine turnover and side reactions; its abstract reports serine deamination at much lower efficiency than the primary biosynthetic reaction. Those side reactions were not turned into unsupported NEW physiological catabolism processes. The existing biosynthesis genetic rows are retained (PMID:4148765/4364333). Integrate PLP binding with the synthase core, and retain cytosolic localization from independent proteomic curation. Plant SAM activation should not be generalized to this bacterial enzyme.

## Retrieval and evidence limits

Normal fetch-gene seeded this review. Actual Falcon/default research and perplexity-lite fallback were attempted concurrently with normal fetch-gene-pmids; both providers failed access/authentication and no report was fabricated. The actual fetch-fitness attempt failed because no FEBA source was reachable; no fitness phenotype or file is claimed. Full provider/publication/fitness logs are in .cache/module-audit-logs/threonine-ECOLI-thrC-*.log. Additional references were normally fetched; transient 429 errors were retried serially. UniProt source quotes are curated reaction/function/family statements, including explicitly identified orthology inferences, never names/EC fields, electronic GO lines or GOA evidence.

Original experimental claims are judged holistically with independently established function; an abstract-only cache or title focused on another enzyme is not by itself evidence against the claim. The current QuickGO term definitions were inspected and saved in the audit log. Authored GO0004073 labels use the validator's ontology spelling while seeded labels remain untouched. Record-section backfill, strict schema/reference/term checks, helper history and HTML rendering accompany the review.
