# arg3 (SPAC4G9.10, UniProt P31317) notes

## Key S. pombe-specific difference
- OTC is mitochondrial in S. pombe (cytosolic in S. cerevisiae): [PMID:1313366 "in contrast to the S. pombe enzyme, more than 95% of the S. cerevisiae enzyme remains in the S. pombe cytoplasm"]; Arg3-GFP mitochondrial [PMID:32896087 "fusion localises to mitochondria"]. So pombe exports citrulline (GO-CAM comment; transporter SPBC365.16).

## Evidence
- Deletion auxotrophy [PMID:32896087 "Strain with arg3 gene deletion"]; library strain was mis-annotated.
- Trx2 dependence (Song et al. 2008, abstract only): [PMID:18849471 "arg3(+) transcript, Arg3 protein, and OCTase activity were all decreased in"]; [PMID:18849471 "we observed a direct interaction between Trx2 and Arg3 in cell extracts"]. No protein-binding GO row present; not proposed.

## Decisions
- Core differs from S. cerevisiae ARG3 in location only (mitochondrial matrix, not cytosol); BPs GO:0006526 + GO:0019240.
- HDA cytoplasm UNDECIDED (conflicts with fractionation/GFP; image not assessable). ARBA cytoplasm MODIFY -> matrix.
- urea cycle IC MARK_AS_OVER_ANNOTATED (consistent across arg3/arg12/arg41 and cerevisiae ARG1).


## 2026-10-26 systematic fungal annotation audit

Reviewed all 22 existing rows and the core functions with the review and annotation-reviewer workflows. Preserved every machine-sourced term, evidence code, qualifier, source identifier, WITH/FROM entry and row order. No new annotations were added in this audit.

The native S. pombe OTC is mitochondrial, unlike budding-yeast ARG3. PMID:1313366 and native mitochondrial evidence support location. PMID:18849471 links Trx2 to OTC stability/activity without requiring Trx2 catalytic cysteines; this is not automatically a redox catalytic edge. Ornithine binding is retained as a conserved catalytic property, distinguished from a new target-specific binding assay.

Live GO:0000050 describes ornithine-to-arginine synthesis followed by arginine cleavage to urea and regenerated ornithine; it does not require ureotelic nitrogen excretion. PMID:20435771 directly measures S. pombe Car1/Car3 arginase-dependent urea production, and PMID:18849471 explicitly places OTC in the urea-cycle segment. Existing OTC/ASS/ASL rows are retained as non-core participation in this reaction topology, without asserting net full-cycle flux or universal simultaneous operation. The upstream acetylornithine-producing Arg1 is treated separately.

Normal publication caching completed. Normal Falcon research with Perplexity-lite fallback was attempted for this gene; authentication/quota failures prevented a generated report. Manual review used the actual cached primary sources and curated UniProt, and no provider-named research file was fabricated. Per-gene attempts and validation logs are in `.cache/module-audit-logs/arginine-SCHPO-arg3-*`. Abstract-only or bibliographic-only sources are distinguished from full text in reference reviews; unavailable source details are not treated as experimental refutations.

Actions: ACCEPT 14, KEEP_AS_NON_CORE 1, MODIFY 7. Record sections were backfilled; focused schema/reference validation passed on the initial complete panel. Final targeted checks and HTML rendering are recorded in the audit logs.
