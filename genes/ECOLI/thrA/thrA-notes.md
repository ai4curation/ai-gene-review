# thrA annotation-review notes

## 2026-10-26 complete native-function review

All 21 seeded rows reviewed. Raw UniProt/GOA source files and every non-review annotation payload are preserved. No NEW rows were proposed.

ThrA has two activities on one polypeptide: aspartate kinase and homoserine dehydrogenase (PMID:4364333 genetic cistrons are historical functional subdivisions, not two separate modern gene products). PMID:11368768 assays pathway enzyme kinetics; normal cache is abstract-only. PMID:204643 directly measures a concentration-dependent dimer/tetramer equilibrium in threonine and reports both forms retain dehydrogenase activity; the inactive monomer was produced by chaotropic treatment. Retain specific self-binding and tetramer assembly as non-core rather than general protein-binding removal.

The current QuickGO definition of GO0004412 names NADP+ specifically, whereas GO0004022 is alcohol oxidation with NAD+. The normally fetched UniProt record separately curates NADP(H) and NAD(H) reactions by similarity to Arabidopsis Q9SA18. Retain the original NAD-dependent alcohol-dehydrogenase and NAD-binding rows as non-core inferred cofactor usage; do not replace them with the NADP-specific term and lose the NAD claim, and do not infer ethanol turnover. No direct target comparison establishing equal physiological NAD/NADP use was recovered. Only kinase and NADP-homoserine chemistry are highlighted as cores. Generic oxidoreductase refinement includes both existing specific activities.

## Retrieval and evidence limits

Normal fetch-gene seeded this review. Actual Falcon/default research and perplexity-lite fallback were attempted concurrently with normal fetch-gene-pmids; both providers failed access/authentication and no report was fabricated. The actual fetch-fitness attempt failed because no FEBA source was reachable; no fitness phenotype or file is claimed. Full provider/publication/fitness logs are in .cache/module-audit-logs/threonine-ECOLI-thrA-*.log. Additional references were normally fetched; transient 429 errors were retried serially. UniProt source quotes are curated reaction/function/family statements, including explicitly identified orthology inferences, never names/EC fields, electronic GO lines or GOA evidence.

Original experimental claims are judged holistically with independently established function; an abstract-only cache or title focused on another enzyme is not by itself evidence against the claim. The current QuickGO term definitions were inspected and saved in the audit log. Authored GO0004073 labels use the validator's ontology spelling while seeded labels remain untouched. Record-section backfill, strict schema/reference/term checks, helper history and HTML rendering accompany the review.
