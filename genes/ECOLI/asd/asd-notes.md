# asd annotation-review notes

## 2026-10-26 complete native-function review

All 25 seeded rows reviewed. Raw UniProt/GOA source files and every non-review annotation payload are preserved. No NEW rows were proposed.

Native Asd is the NADPH-dependent reductive dephosphorylase of aspartyl phosphate. PMID:6102909 purifies the enzyme, identifies two identical/similar subunits, detects an acyl-enzyme intermediate and establishes stereospecific NADPH hydrogen transfer. PMID:14726201 tests cystine-mediated modification of catalytic Cys135; this is a reversible inhibitor mechanism, not evidence that Asd carries out cystine metabolism. PMID:11368768 gives integrated native pathway kinetics; UniProt records target-linked NADPH and substrate Km values.

NAD binding is not equivalent to physiological NAD preference. PMID:26662025 explicitly contrasts inefficient wild-type NAD utilization with engineered variants improving kcat/Km by 44/66-fold. Retain the weak existing NAD-binding claim as non-core rather than declaring no binding or attributing mutant behavior to wild type. Core remains NADP(H) dependent. PMID:11967071 is an expression-array response to mitomycin C, retained as non-core DNA-damage response rather than DNA repair; unavailable target-specific full tables were not used to overrule its experimental curation. All four downstream amino-acid branches are direct chemical pathway participation, not merely phenotypic necessity.

## Retrieval and evidence limits

Normal fetch-gene seeded this review. Actual Falcon/default research and perplexity-lite fallback were attempted concurrently with normal fetch-gene-pmids; both providers failed access/authentication and no report was fabricated. The actual fetch-fitness attempt failed because no FEBA source was reachable; no fitness phenotype or file is claimed. Full provider/publication/fitness logs are in .cache/module-audit-logs/threonine-ECOLI-asd-*.log. Additional references were normally fetched; transient 429 errors were retried serially. UniProt source quotes are curated reaction/function/family statements, including explicitly identified orthology inferences, never names/EC fields, electronic GO lines or GOA evidence.

Original experimental claims are judged holistically with independently established function; an abstract-only cache or title focused on another enzyme is not by itself evidence against the claim. The current QuickGO term definitions were inspected and saved in the audit log. Authored GO0004073 labels use the validator's ontology spelling while seeded labels remain untouched. Record-section backfill, strict schema/reference/term checks, helper history and HTML rendering accompany the review.
