# ARG1 (YOL058W, P22768) notes

Evidence journal (no paid deep research run; built from UniProt and cached publications).

- Argininosuccinate synthase, EC 6.3.4.5, homotetramer [UniProt:P22768]. Purified enzyme: "Yeast argininosuccinate synthetase has been purified to homogeneity." and "The quaternary structure ... is tetrameric." [PMID:35347]
- Kinetics: "with MgATP as the variable substrate a sigmoid character" ; "Kinetic analysis provided evidence for a random addition of substrates." [PMID:35347]
- Dual role: "anabolic in the biosynthesis of arginine, catabolic as the first enzyme of citrulline utilization as nitrogen source" [PMID:35347]
- Gene identity: "The Saccharomyces cerevisiae ARG1 gene coding for argininosuccinate synthetase has been isolated" [PMID:2897249]; regulation by arginine-specific repression and general amino acid control [PMID:2897249].
- Location: cytosolic/soluble fraction, with the other ornithine-to-arginine enzymes [PMID:205532 "argininosuccinate synthetase, and argininosuccinate lyase, and the two first catabolic enzymes, arginase and ornithine aminotransferase, were in the"].

## Curation decisions
- Core MF: GO:0004055; BP GO:0006526; CC GO:0005829.
- Urea cycle (IBA, PTN000172504): MARK_AS_OVER_ANNOTATED. Yeast is not ureotelic; arginase (CAR1) is catabolic and, with OTCase, forms the epiarginase complex that blocks futile cycling [PMID:12679340]. Precedent: genes/PSEPK/argG REMOVE for the same node.
- ATP binding IEA: non-core (substrate).


## 2026-10-26 systematic fungal annotation audit

Reviewed all 15 existing rows and the core functions with the review and annotation-reviewer workflows. Preserved every machine-sourced term, evidence code, qualifier, source identifier, WITH/FROM entry and row order. No new annotations were added in this audit.

Argininosuccinate synthetase chemistry and soluble localization are supported by the primary yeast literature. PMID:35347 describes both arginine biosynthesis and a citrulline nitrogen-utilization role. The existing urea-cycle annotation is retained as a precise secondary network participation claim rather than rejected because yeast is not ureotelic.

Live GO:0000050 describes ornithine-to-arginine synthesis followed by arginine cleavage to urea and regenerated ornithine; it does not require ureotelic nitrogen excretion. PMID:20435771 directly measures S. pombe Car1/Car3 arginase-dependent urea production, and PMID:18849471 explicitly places OTC in the urea-cycle segment. Existing OTC/ASS/ASL rows are retained as non-core participation in this reaction topology, without asserting net full-cycle flux or universal simultaneous operation. The upstream acetylornithine-producing Arg1 is treated separately.

Normal publication caching completed. Normal Falcon research with Perplexity-lite fallback was attempted for this gene; authentication/quota failures prevented a generated report. Manual review used the actual cached primary sources and curated UniProt, and no provider-named research file was fabricated. Per-gene attempts and validation logs are in `.cache/module-audit-logs/arginine-yeast-ARG1-*`. Abstract-only or bibliographic-only sources are distinguished from full text in reference reviews; unavailable source details are not treated as experimental refutations.

Actions: ACCEPT 13, KEEP_AS_NON_CORE 1, MODIFY 1. Record sections were backfilled; focused schema/reference validation passed on the initial complete panel. Final targeted checks and HTML rendering are recorded in the audit logs.
