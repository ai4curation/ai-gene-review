# ARG2 (YJL071W, P40360) notes

- N-acetylglutamate synthase (EC 2.3.1.1), first step of arginine biosynthesis: "Open reading frame YJL071W of Saccharomyces cerevisiae was shown to be ARG2 and identified as the structural gene for acetylglutamate synthase, first step in arginine biosynthesis" [PMID:11553611].
- Fungal NAGS is not homologous to bacterial ArgA [PMID:11553611 "they showed no significant similarity to their prokaryotic equivalents"].
- Activity requires complex with Arg5,6 kinase: "The results imply that the synthase must interact stoichiometrically in vivo with the kinase, the reductase, or both to be active."; "hemagglutinin-tagged synthase coprecipitated with a protein proven by microsequencing to be the kinase" [PMID:11553611]. Reductase dispensable; metabolon couples feedback regulation [PMID:12603335].
- Feedback inhibition by arginine; regulated by arginine repression, glucose repression and GAAC [PMID:391804].
- Mitochondrial (particulate) [PMID:205532]; UniProt: Mitochondrion [UniProt:P40360].

## Curation decisions
- Core MF GO:0004042; BP GO:0006526, GO:0006592; CC GO:0005759; complex GO:0106098.
- RCA (GO_REF:0000123) cytosol: REMOVE (contradicted by fractionation).
- RCA GO:0103045 L-methionine N-acyltransferase: REMOVE (no evidence for methionine substrate; likely projection of the generic EC 2.3.1.1 name).


## 2026-10-26 systematic fungal annotation audit

Reviewed all 18 existing rows and the core functions with the review and annotation-reviewer workflows. Preserved every machine-sourced term, evidence code, qualifier, source identifier, WITH/FROM entry and row order. No new annotations were added in this audit.

PMID:11553611 supports the NAGS/NAGK assembly; PMID:12603335 clarifies that the kinase region is needed for NAGS support whereas the reductase is dispensable. The pathway-derived methionine acetyltransferase claim is refined to the established glutamate acceptor, without claiming an exhaustive substrate-exclusion assay.

Normal publication caching completed. Normal Falcon research with Perplexity-lite fallback was attempted for this gene; authentication/quota failures prevented a generated report. Manual review used the actual cached primary sources and curated UniProt, and no provider-named research file was fabricated. Per-gene attempts and validation logs are in `.cache/module-audit-logs/arginine-yeast-ARG2-*`. Abstract-only or bibliographic-only sources are distinguished from full text in reference reviews; unavailable source details are not treated as experimental refutations.

Actions: ACCEPT 14, MODIFY 3, REMOVE 1. Record sections were backfilled; focused schema/reference validation passed on the initial complete panel. Final targeted checks and HTML rendering are recorded in the audit logs.
