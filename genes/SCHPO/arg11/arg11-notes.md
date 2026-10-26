# arg11 (SPAC4G9.09c, UniProt P31318) notes

## Naming trap
- S. pombe arg11 = ARG5,6-type acetylglutamate kinase / NAGSA reductase polyprotein. S. cerevisiae ARG11 = ORT1 mitochondrial ornithine carrier (different protein).

## Evidence
- Van Huffel et al. 1992 (abstract only): [PMID:1313366 "The acetylglutamate kinase and acetylglutamate-phosphate reductase domains have been defined by their identity with the S. cerevisiae ARG5,6 protein."]; cloned by complementation [PMID:1313366 "were cloned by functional complementation of S. pombe arg3 and"]; no cross-complementation [PMID:1313366 "The cloned arg11 gene from S. pombe does not complement an arg5,6 mutation in S. cerevisiae"].
- UniProt cites EC 2.7.2.8 and EC 1.2.1.38 with ECO:0000269 from PMID:1313366; transit peptide 1..59; chains 60..550 (kinase) and 551..885 (reductase) [UniProt:P31318 "PTM: The protein precursor is probably cleaved into the two"]; [UniProt:P31318 "ACTIVITY REGULATION: The kinase activity is inhibited by arginine."].
- GO-CAM gomodel:6690711d00000916 models both activities (GO:0003991, GO:0003942) in mitochondrial matrix.

## Decisions
- All experimental rows accepted (deferred to curator, full text not cached).
- Cytoplasm (InterPro2GO) MODIFY -> matrix; NAD binding over-annotated (NADP enzyme); generic BPs/MF MODIFY.
- No NAGS/NAGK complex added: no S. pombe evidence (ARG5,6 has IPI in budding yeast) - raised as suggested question.


## 2026-10-26 systematic fungal annotation audit

Reviewed all 21 existing rows and the core functions with the review and annotation-reviewer workflows. Preserved every machine-sourced term, evidence code, qualifier, source identifier, WITH/FROM entry and row order. No new annotations were added in this audit.

Kinase and reductase activities are attributed to precursor regions. Internal proteolysis is a curated comparative inference here, not a fresh direct S. pombe cleavage assay; budding-yeast import-dependent processing must not be automatically transplanted as an observed event. PMID:1313366 supports mitochondrial targeting and functional differences in cross-species complementation. NAD cofactor mapping is refined to NADP.

Normal publication caching completed. Normal Falcon research with Perplexity-lite fallback was attempted for this gene; authentication/quota failures prevented a generated report. Manual review used the actual cached primary sources and curated UniProt, and no provider-named research file was fabricated. Per-gene attempts and validation logs are in `.cache/module-audit-logs/arginine-SCHPO-arg11-*`. Abstract-only or bibliographic-only sources are distinguished from full text in reference reviews; unavailable source details are not treated as experimental refutations.

Actions: ACCEPT 14, MODIFY 7. Record sections were backfilled; focused schema/reference validation passed on the initial complete panel. Final targeted checks and HTML rendering are recorded in the audit logs.

Ontology-cache advisory: live QuickGO confirms GO:0003942 has the NADP+-specific label; the local ontology cache retains the older shorter label. The machine payload and current chemically specific label are preserved rather than rewritten to silence a stale-label warning.
