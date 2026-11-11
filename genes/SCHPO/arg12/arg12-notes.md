# arg12 (SPBC428.05c, UniProt O94354) notes

## Naming trap
- S. pombe arg12 = argininosuccinate synthase = ortholog of S. cerevisiae ARG1.

## Evidence
- Fujita et al. 2005 (abstract only): [PMID:15704224 "We developed three new auxotrophic marker genes (arg12(+), tyr1(+) and ade7(+))"]; UniProt: [UniProt:O94354 "DISRUPTION PHENOTYPE: Causes arginine auxotrophy."].
- Cytosol by ORFeome HDA [UniProt:O94354 "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000269|PubMed:16823372}."].
- GO-CAM: arg12 GO:0004055 in cytosol, downstream of citrulline export by SPBC365.16, upstream of arg7/arg41 ASL.

## Decisions
- urea cycle IBA MARK_AS_OVER_ANNOTATED (same as ARG1 review), with propagation_review.
- Core identical to S. cerevisiae ARG1: GO:0004055, GO:0006526, cytosol.


## 2026-10-26 systematic fungal annotation audit

Reviewed all 12 existing rows and the core functions with the review and annotation-reviewer workflows. Preserved every machine-sourced term, evidence code, qualifier, source identifier, WITH/FROM entry and row order. No new annotations were added in this audit.

Argininosuccinate synthetase participates in the supported downstream arginine reaction segment; PMID:15704224 native deletion-marker experiments and conserved enzyme architecture support the role. The urea-cycle row is contextual and does not assert measured complete-cycle flux.

Live GO:0000050 describes ornithine-to-arginine synthesis followed by arginine cleavage to urea and regenerated ornithine; it does not require ureotelic nitrogen excretion. PMID:20435771 directly measures S. pombe Car1/Car3 arginase-dependent urea production, and PMID:18849471 explicitly places OTC in the urea-cycle segment. Existing OTC/ASS/ASL rows are retained as non-core participation in this reaction topology, without asserting net full-cycle flux or universal simultaneous operation. The upstream acetylornithine-producing Arg1 is treated separately.

Normal publication caching completed. Normal Falcon research with Perplexity-lite fallback was attempted for this gene; authentication/quota failures prevented a generated report. Manual review used the actual cached primary sources and curated UniProt, and no provider-named research file was fabricated. Per-gene attempts and validation logs are in `.cache/module-audit-logs/arginine-SCHPO-arg12-*`. Abstract-only or bibliographic-only sources are distinguished from full text in reference reviews; unavailable source details are not treated as experimental refutations.

Actions: ACCEPT 10, KEEP_AS_NON_CORE 1, MODIFY 1. Record sections were backfilled; focused schema/reference validation passed on the initial complete panel. Final targeted checks and HTML rendering are recorded in the audit logs.
