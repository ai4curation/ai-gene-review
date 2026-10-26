# arg41 (SPBC1539.03c, UniProt P50514) notes

## Identity
- UniProt gene name is "argx" (ARLZ_SCHPO); PomBase name arg41. Fetched with `-u P50514`.
- [UniProt:P50514 "RecName: Full=Probable argininosuccinate lyase;"]; ortholog of S. cerevisiae ARG4. Paralog arg7 (SPBC1773.14).

## Evidence
- [PMID:32896087 "arg7 is one of two argininosuccinate lyases (with deletion of the other one, arg41, showing arginine auxotrophy)"] -> arg41 is the paralog needed for prototrophy.
- Cytosol (ORFeome HDA).
- PomBase GO-CAM: both arg7 (IMP PMID:1868575) and arg41 (IBA only) enable GO:0004056 in cytosol.

## Decisions
- urea cycle IC/IEA MARK_AS_OVER_ANNOTATED; catalytic activity MODIFY -> GO:0004056.
- Core = ARG4 core: GO:0004056, GO:0006526, cytosol.


## 2026-10-26 systematic fungal annotation audit

Reviewed all 10 existing rows and the core functions with the review and annotation-reviewer workflows. Preserved every machine-sourced term, evidence code, qualifier, source identifier, WITH/FROM entry and row order. No new annotations were added in this audit.

PMID:32896087 supports arginine auxotrophy after arg41 deletion under the tested conditions, not quantitative dominance in every condition. The catalytic assignment also rests on conserved lyase architecture and phylogenetic inference; knockout alone is not a direct enzyme assay. Suggested experiments now ask for paralog-specific activity/flux rather than treating phenotype as an assay substitute.

Live GO:0000050 describes ornithine-to-arginine synthesis followed by arginine cleavage to urea and regenerated ornithine; it does not require ureotelic nitrogen excretion. PMID:20435771 directly measures S. pombe Car1/Car3 arginase-dependent urea production, and PMID:18849471 explicitly places OTC in the urea-cycle segment. Existing OTC/ASS/ASL rows are retained as non-core participation in this reaction topology, without asserting net full-cycle flux or universal simultaneous operation. The upstream acetylornithine-producing Arg1 is treated separately.

Normal publication caching completed. Normal Falcon research with Perplexity-lite fallback was attempted for this gene; authentication/quota failures prevented a generated report. Manual review used the actual cached primary sources and curated UniProt, and no provider-named research file was fabricated. Per-gene attempts and validation logs are in `.cache/module-audit-logs/arginine-SCHPO-arg41-*`. Abstract-only or bibliographic-only sources are distinguished from full text in reference reviews; unavailable source details are not treated as experimental refutations.

Actions: ACCEPT 7, KEEP_AS_NON_CORE 2, MODIFY 1. Record sections were backfilled; focused schema/reference validation passed on the initial complete panel. Final targeted checks and HTML rendering are recorded in the audit logs.
