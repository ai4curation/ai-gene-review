# MJ0571 annotation-review notes

## 2026-10-26 complete native-function review

All 8 seeded rows reviewed. Raw UniProt/GOA source files and every non-review annotation payload are preserved. No NEW rows were proposed.

Current UniProt Q57991 has no GN Name; its ordered locus is MJ0571. Use that verified locus as gene symbol, not an invented lysC or ask alias. PMID:17012784 directly characterizes recombinant native-sequence M. jannaschii aspartokinase and its substrate-bound structure. The normal cache initially remained abstract-only; full text was additionally read online at https://pmc.ncbi.nlm.nih.gov/articles/PMC2225177/ (Results3.1–3.2). It describes a dimer-of-dimers tetramer, threonine sensitivity and no lysine effect up to 10 mM; historical automatic lysine-sensitive naming was explicitly disproved. The structural experiment itself is not a localization assay; cytosol is retained as an independently inherited soluble-enzyme location.

The lysine-biosynthetic assertion is not removed merely because this is archaeal: M. jannaschii uses a DAP pathway, unlike fungi. The full primary context supports the shared trunk, and direct downstream methanococcal DapL work is consistent (https://pmc.ncbi.nlm.nih.gov/articles/PMC2897669/). Two archaeal exemplars in this audit do not establish all five native module steps. The co-occurring kinase activity row is refined to the specific existing aspartate kinase term; no NEW process or regulatory role is proposed.

## Retrieval and evidence limits

Normal fetch-gene seeded this review. Actual Falcon/default research and perplexity-lite fallback were attempted concurrently with normal fetch-gene-pmids; both providers failed access/authentication and no report was fabricated. The actual fetch-fitness attempt failed because no FEBA source was reachable; no fitness phenotype or file is claimed. Full provider/publication/fitness logs are in .cache/module-audit-logs/threonine-METJA-MJ0571-*.log. Additional references were normally fetched; transient 429 errors were retried serially. UniProt source quotes are curated reaction/function/family statements, including explicitly identified orthology inferences, never names/EC fields, electronic GO lines or GOA evidence.

Original experimental claims are judged holistically with independently established function; an abstract-only cache or title focused on another enzyme is not by itself evidence against the claim. The current QuickGO term definitions were inspected and saved in the audit log. Authored GO0004073 labels use the validator's ontology spelling while seeded labels remain untouched. Record-section backfill, strict schema/reference/term checks, helper history and HTML rendering accompany the review.


Retrieval update: normal force-fetch of PMID:17012784 subsequently obtained the full text; Results3.2 now directly supplies the threonine-inhibition quote in the review. PMID:20418392 was normally cached and read as downstream native DAP-pathway corroboration, not as a direct MJ0571 assay.
