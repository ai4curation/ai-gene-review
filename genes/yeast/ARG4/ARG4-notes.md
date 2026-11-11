# ARG4 (YHR018C, P04076) notes

- Argininosuccinate lyase, EC 4.3.2.1: "Reaction=2-(N(omega)-L-arginino)succinate = fumarate + L-arginine;" final step 3/3 of arginine formation from ornithine; homotetramer; lyase 1 family [UniProt:P04076].
- Cytosolic (soluble fraction) [PMID:205532].
- IDA source PMID:4578972 ("Studies on the kinetics of the enzyme sequence mediating arginine synthesis in Saccharomyces cerevisiae") has no cached abstract; curator's IDA accepted (consistent with all other data).
- ARG4 locus is a classic meiotic recombination hotspot / marker (background knowledge; not annotated).

## Curation decisions
- Core MF GO:0004056; BP GO:0006526; CC GO:0005829.
- Generic "catalytic activity" IEA -> MODIFY to GO:0004056.


## 2026-10-26 systematic fungal annotation audit

Reviewed all 12 existing rows and the core functions with the review and annotation-reviewer workflows. Preserved every machine-sourced term, evidence code, qualifier, source identifier, WITH/FROM entry and row order. No new annotations were added in this audit.

Argininosuccinate lyase performs the terminal biosynthetic cleavage, with soluble localization supported by PMID:205532. Old PMID:4578972 has only bibliographic access in the cache; independent conserved catalytic/curated evidence supports the function, without pretending to re-read unavailable kinetics.

Normal publication caching completed. Normal Falcon research with Perplexity-lite fallback was attempted for this gene; authentication/quota failures prevented a generated report. Manual review used the actual cached primary sources and curated UniProt, and no provider-named research file was fabricated. Per-gene attempts and validation logs are in `.cache/module-audit-logs/arginine-yeast-ARG4-*`. Abstract-only or bibliographic-only sources are distinguished from full text in reference reviews; unavailable source details are not treated as experimental refutations.

Actions: ACCEPT 11, MODIFY 1. Record sections were backfilled; focused schema/reference validation passed on the initial complete panel. Final targeted checks and HTML rendering are recorded in the audit logs.
