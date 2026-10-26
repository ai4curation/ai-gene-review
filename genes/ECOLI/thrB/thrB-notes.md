# thrB annotation-review notes

## 2026-10-26 complete native-function review

All 10 seeded rows reviewed. Raw UniProt/GOA source files and every non-review annotation payload are preserved. No NEW rows were proposed.

PMID:177283 directly purifies native E. coli homoserine kinase and establishes competitive, noncooperative threonine inhibition at the homoserine site. PMID:8973190 characterizes homoserine analogues and separates ATPase from kinase activity through mutagenesis. The curated function explicitly excludes L-serine and L-threonine as kinase substrates. The native reaction uses ATP; neither PLP chemistry nor the phosphoserine donor of Pseudomonas ThrH applies. Existing threonine-biosynthesis genetic rows (PMID:4148765/4364333) agree with the enzymatic step. Cytosolic proteomic assignments are retained without pretending the abstract reconstructs each peptide table. No NEW promiscuous-substrate or ATPase annotation was proposed.

## Retrieval and evidence limits

Normal fetch-gene seeded this review. Actual Falcon/default research and perplexity-lite fallback were attempted concurrently with normal fetch-gene-pmids; both providers failed access/authentication and no report was fabricated. The actual fetch-fitness attempt failed because no FEBA source was reachable; no fitness phenotype or file is claimed. Full provider/publication/fitness logs are in .cache/module-audit-logs/threonine-ECOLI-thrB-*.log. Additional references were normally fetched; transient 429 errors were retried serially. UniProt source quotes are curated reaction/function/family statements, including explicitly identified orthology inferences, never names/EC fields, electronic GO lines or GOA evidence.

Original experimental claims are judged holistically with independently established function; an abstract-only cache or title focused on another enzyme is not by itself evidence against the claim. The current QuickGO term definitions were inspected and saved in the audit log. Authored GO0004073 labels use the validator's ontology spelling while seeded labels remain untouched. Record-section backfill, strict schema/reference/term checks, helper history and HTML rendering accompany the review.
